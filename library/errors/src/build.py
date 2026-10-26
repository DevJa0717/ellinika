#!/usr/bin/env python3
"""Builds library/errors/*.json from the plain-text sources in this folder.

Category files NN-<code>.txt: '# key: value' header (code, el, en, about), then items:
  @ LEVEL [ok]
  sentence with markers [wrong|right|other accepted right]{optional category}
  = English translation of the corrected sentence
  ? one explanation per marker, in order (ok items: one line saying why nothing is wrong)
Paragraph files p-<level>.txt: items start '@ LEVEL', then 'T: Greek title | English title',
then the text (one line, ' / ' separates paragraphs), '=' translation, '?' per marker; every marker needs {category}.
Run: python3 library/errors/src/build.py
"""
import json, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
LEVELS = ["A2", "B1", "B2", "C1"]
MARK = re.compile(r"\[([^\[\]|]+)\|([^\[\]]+)\](?:\{(\w+)\})?")
errors = []


def parse(path):
    head, items, cur = {}, [], None
    for n, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip():
            continue
        if line.startswith("# "):
            k, v = line[2:].split(":", 1)
            head[k.strip()] = v.strip()
        elif line.startswith("@ "):
            bits = line[2:].split()
            cur = {"level": bits[0], "ok": "ok" in bits[1:], "line": n, "why": [], "text": None}
            items.append(cur)
        elif line.startswith("T: "):
            el, en = line[3:].split("|")
            cur["el"], cur["title"] = el.strip(), en.strip()
        elif line.startswith("= "):
            cur["en"] = line[2:].strip()
        elif line.startswith("? "):
            cur["why"].append(line[2:].strip())
        else:
            if cur["text"] is not None:
                errors.append(f"{path}:{n}: second text line")
            cur["text"] = line.strip()
    return head, items


def build_item(path, it, default_cat, cats, iid):
    where = f"{os.path.basename(path)}:{it['line']}"
    if it["level"] not in LEVELS:
        errors.append(f"{where}: bad level {it['level']}")
    parts, errs, pos = [], [], 0
    for m in MARK.finditer(it["text"] or ""):
        if m.start() > pos:
            parts.append(it["text"][pos:m.start()])
        wrong, rights = m.group(1), m.group(2).split("|")
        cat = m.group(3) or default_cat
        if not cat or cat not in cats:
            errors.append(f"{where}: unknown or missing category {cat!r}")
        if wrong in rights:
            errors.append(f"{where}: wrong form {wrong!r} is listed as right")
        parts.append(len(errs))
        errs.append({"w": wrong, "r": rights, "c": cat})
        pos = m.end()
    if pos < len(it["text"] or ""):
        parts.append(it["text"][pos:])
    if re.search(r"[\[\]{}|]", "".join(p for p in parts if isinstance(p, str))):
        errors.append(f"{where}: stray bracket or bar in text")
    if it["ok"]:
        if errs:
            errors.append(f"{where}: ok item has markers")
        if len(it["why"]) != 1:
            errors.append(f"{where}: ok item needs exactly one '?' line")
    else:
        if not errs:
            errors.append(f"{where}: item has no marker (add 'ok' if it is correct)")
        if len(it["why"]) != len(errs):
            errors.append(f"{where}: {len(errs)} markers but {len(it['why'])} explanations")
    for e, w in zip(errs, it["why"]):
        e["why"] = w
    if not it.get("en"):
        errors.append(f"{where}: no translation")
    out = {"id": iid, "level": it["level"], "parts": parts, "en": it.get("en", "")}
    if errs:
        out["errs"] = errs
    else:
        out["ok"] = True
        out["why"] = it["why"][0] if it["why"] else ""
    if "el" in it:
        out["el"], out["title"] = it["el"], it["title"]
    return out


def fixed(item):
    return "".join(p if isinstance(p, str) else item["errs"][p]["r"][0] for p in item["parts"])


def wrong(item):
    return "".join(p if isinstance(p, str) else item["errs"][p]["w"] for p in item["parts"])


def main():
    files = sorted(glob.glob(os.path.join(HERE, "[0-9][0-9]-*.txt")))
    heads = [(f, *parse(f)) for f in files]
    cats = {h["code"]: h for _, h, _ in heads}
    index = {"categories": [], "paragraphs": []}
    for f, h, items in heads:
        code = h["code"]
        built = []
        for i, it in enumerate(items, 1):
            built.append(build_item(f, it, code, cats, f"{code}-{i:02d}"))
        order = {l: k for k, l in enumerate(LEVELS)}
        built.sort(key=lambda x: order.get(x["level"], 9))
        doc = {"id": code, "el": h["el"], "title": h["en"], "about": h.get("about", ""), "items": built}
        json.dump(doc, open(os.path.join(OUT, code + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        index["categories"].append({"id": code, "el": h["el"], "title": h["en"], "file": code + ".json",
                                    "count": len(built), "levels": {l: sum(1 for x in built if x["level"] == l) for l in LEVELS},
                                    "errors": sum(len(x.get("errs", [])) for x in built)})
    paras = []
    for f in sorted(glob.glob(os.path.join(HERE, "p-*.txt"))):
        _, items = parse(f)
        lvl = os.path.basename(f)[2:-4].upper()
        for i, it in enumerate(items, 1):
            if "el" not in it:
                errors.append(f"{f}:{it['line']}: paragraph without 'T:' title")
            x = build_item(f, it, None, cats, f"p-{lvl.lower()}-{i:02d}")
            paras.append(x)
    order = {l: k for k, l in enumerate(LEVELS)}
    paras.sort(key=lambda x: (order.get(x["level"], 9), x["id"]))
    json.dump({"items": paras}, open(os.path.join(OUT, "paragraphs.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    index["paragraphs"] = [{"id": p["id"], "el": p["el"], "title": p["title"], "level": p["level"], "errors": len(p.get("errs", []))} for p in paras]
    json.dump(index, open(os.path.join(OUT, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # plain dump of every corrected and wrong text, for the spelling and lookup checks
    with open(os.path.join(HERE, "corrected.txt"), "w", encoding="utf-8") as fo:
        for f, h, _ in heads:
            for x in json.load(open(os.path.join(OUT, h["code"] + ".json"), encoding="utf-8"))["items"]:
                fo.write(f"{x['id']}\t{fixed(x) if 'errs' in x else ''.join(x['parts'])}\n")
        for x in paras:
            fo.write(f"{x['id']}\t{fixed(x)}\n")
    n_items = sum(c["count"] for c in index["categories"])
    n_err = sum(c["errors"] for c in index["categories"]) + sum(p["errors"] for p in index["paragraphs"])
    print(f"{len(cats)} categories, {n_items} sentences, {len(paras)} paragraphs, {n_err} errors to find")
    for e in errors:
        print("PROBLEM", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
