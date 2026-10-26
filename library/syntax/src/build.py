#!/usr/bin/env python3
"""Build library/syntax/<id>.json and index.json (syntax and discourse guide) from the plain-text sources in this folder.

Same source format as library/pos/src (one file per topic, NN-id.txt, NN gives the order), plus two exercise kinds
and related-link lines:
  header lines until the first "## ":   id: / el: / title: / span: / blurb:   then free intro paragraphs
  "## LEVEL | Greek heading | English heading"  starts a section
  blocks are separated by blank lines:
    | a | b | c          table; the first row is the header, "|-" lines are ignored
    > Greek || English   example lines
    ! text               pitfall / tip callout
    - item               bullet list
    ? question | option | *right option | option || explanation     multiple choice
    ~ cue | Greek sentence | other accepted order || explanation     put the words in order (tiles from the first sentence)
    = prompt => answer | other accepted answer || explanation        write the answer
    @ lesson-id, pos.<doc>~<n>, syntax.<doc>~<n>, cards.<id>          "Related in the app" links (checked here)
    anything else        paragraph (**bold**, *italic*)
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
APP = os.path.dirname(os.path.dirname(OUT))


def link_table():
    """Every target an @ line may name, with its Greek and English title."""
    t = {}
    course = json.load(open(os.path.join(APP, "lessons/course.json"), encoding="utf-8"))
    for u in course["units"]:
        for l in u.get("lessons", []):
            t[l["id"]] = {"href": "#" + l["id"], "kind": "Lesson", "el": l.get("el", ""), "title": l.get("title", "")}
    pos = json.load(open(os.path.join(APP, "library/pos/index.json"), encoding="utf-8"))
    for it in pos["items"]:
        d = json.load(open(os.path.join(APP, "library/pos", it["file"]), encoding="utf-8"))
        t["pos." + it["id"]] = {"href": "#pos." + it["id"], "kind": "Part of speech", "el": d["el"], "title": d["title"]}
        for i, s in enumerate(d["sections"]):
            t[f"pos.{it['id']}~{i}"] = {"href": f"#pos.{it['id']}~{i}", "kind": "Part of speech", "el": s["el"], "title": s["title"]}
    return t


def parse(path):
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    head, _, rest = text.partition("\n## ")
    doc = {"sections": []}
    intro = []
    for blk in re.split(r"\n\s*\n", head.strip()):
        lines = blk.strip().split("\n")
        if all(re.match(r"^(id|el|title|span|blurb):", l) for l in lines):
            for l in lines:
                k, v = l.split(":", 1)
                doc[k] = v.strip()
        else:
            intro.append(blocks_of(blk, path))
    doc["intro"] = [b for x in intro for b in x]
    if rest:
        for chunk in ("## " + rest).split("\n## "):
            chunk = chunk[3:] if chunk.startswith("## ") else chunk
            first, _, body = chunk.partition("\n")
            parts = [p.strip() for p in first.split("|")]
            if len(parts) != 3:
                sys.exit(f"{path}: bad section header: {first}")
            sec = {"level": parts[0], "el": parts[1], "title": parts[2], "body": []}
            for blk in re.split(r"\n\s*\n", body.strip()):
                if blk.strip():
                    sec["body"] += blocks_of(blk, path)
            doc["sections"].append(sec)
    for k in ("id", "el", "title"):
        if k not in doc:
            sys.exit(f"{path}: missing {k}")
    return doc


def blocks_of(blk, path):
    lines = [l.rstrip() for l in blk.strip().split("\n")]
    out = []
    kind = lambda l: l[:1] if l[:1] in "|>!-?~=@" and (l[1:2] == " " or l[:1] == "|") else "p"
    groups = []
    ex_kinds = "?~="
    for l in lines:
        k = kind(l)
        # the three exercise kinds share one block, so a section's exercises stay together
        if groups and (groups[-1][0] == k or (k in ex_kinds and groups[-1][0] in ex_kinds)) and k != "p":
            groups[-1][1].append(l)
        elif groups and groups[-1][0] == "p" and k == "p":
            groups[-1][1].append(l)
        else:
            groups.append((k, [l]))
    for k, ls in groups:
        if k == "p":
            out.append({"p": " ".join(x.strip() for x in ls)})
        elif k == "|":
            rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in ls if not re.match(r"^\|\s*-", l)]
            w = max(len(r) for r in rows)
            rows = [r + [""] * (w - len(r)) for r in rows]
            out.append({"table": {"head": rows[0], "rows": rows[1:]}})
        elif k == ">":
            ex = []
            for l in ls:
                el, _, en = l[2:].partition("||")
                ex.append({"el": el.strip(), "en": en.strip()})
            out.append({"ex": ex})
        elif k == "!":
            out.append({"tip": " ".join(l[2:].strip() for l in ls)})
        elif k == "-":
            out.append({"list": [l[2:].strip() for l in ls]})
        elif k == "@":
            out.append({"links": [x.strip() for l in ls for x in l[2:].split(",") if x.strip()]})
        elif k in ex_kinds:
            qs = []
            for l in ls:
                body, _, why = l[2:].partition("||")
                why = why.strip()
                if l[0] == "?":
                    parts = [p.strip() for p in body.split(" | ")]
                    opts = parts[1:]
                    ans = [o[1:] for o in opts if o.startswith("*")]
                    if len(ans) != 1 or len(opts) < 2:
                        sys.exit(f"{path}: question needs exactly one *answer: {l}")
                    qs.append({"type": "choice", "q": parts[0], "options": [o.lstrip("*") for o in opts], "answer": ans[0], "why": why})
                elif l[0] == "~":
                    parts = [p.strip() for p in body.split(" | ")]
                    if len(parts) < 2:
                        sys.exit(f"{path}: order item needs a cue and a sentence: {l}")
                    for alt in parts[2:]:
                        if sorted(words(alt)) != sorted(words(parts[1])):
                            sys.exit(f"{path}: accepted order uses other words than the first: {alt}")
                    qs.append({"type": "order", "q": parts[0], "answer": parts[1], "accept": parts[2:], "why": why})
                else:
                    prompt, arrow, ans = body.partition("=>")
                    if not arrow:
                        sys.exit(f"{path}: write item needs '=> answer': {l}")
                    acc = [a.strip() for a in ans.split(" | ") if a.strip()]
                    qs.append({"type": "write", "q": prompt.strip(), "answer": acc[0], "accept": acc[1:], "why": why})
            out.append({"check": qs})
    return out


def words(s):
    return [w.lower() for w in re.findall(r"[\w'’,]+", s.replace(",", ""))]


def main():
    links = link_table()
    files = sorted(f for f in os.listdir(HERE) if f.endswith(".txt"))
    docs = [parse(os.path.join(HERE, f)) for f in files]
    for d in docs:
        links["syntax." + d["id"]] = {"href": "#syntax." + d["id"], "kind": "Syntax", "el": d["el"], "title": d["title"]}
        for i, s in enumerate(d["sections"]):
            links[f"syntax.{d['id']}~{i}"] = {"href": f"#syntax.{d['id']}~{i}", "kind": "Syntax", "el": s["el"], "title": s["title"]}
    cards = os.path.join(APP, "library/cards/index.json")
    if os.path.exists(cards):
        for c in json.load(open(cards, encoding="utf-8"))["cards"]:
            links["cards." + c["id"]] = {"href": "#cards." + c["id"], "kind": "Card", "el": c["el"], "title": c["title"]}
    bad = 0
    def resolve(blocks, where):
        nonlocal bad
        for b in blocks:
            if "links" in b:
                res = []
                for x in b["links"]:
                    if x not in links:
                        print(f"  unknown link {x} in {where}"); bad += 1
                    else:
                        res.append(links[x])
                b["links"] = res
    items = []
    for doc in docs:
        resolve(doc["intro"], doc["id"])
        for s in doc["sections"]:
            resolve(s["body"], doc["id"] + " / " + s["title"])
        qs = [q for s in doc["sections"] for b in s["body"] if "check" in b for q in b["check"]]
        with open(os.path.join(OUT, doc["id"] + ".json"), "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
        items.append({"id": doc["id"], "file": doc["id"] + ".json", "el": doc["el"], "title": doc["title"],
                      "span": doc.get("span", ""), "blurb": doc.get("blurb", ""), "sections": len(doc["sections"]), "questions": len(qs)})
        kinds = {k: sum(q["type"] == k for q in qs) for k in ("choice", "order", "write")}
        print(f"{doc['id']:14} {len(doc['sections']):3} sections {len(qs):3} exercises {kinds}")
    with open(os.path.join(OUT, "index.json"), "w", encoding="utf-8") as fh:
        json.dump({"items": items}, fh, ensure_ascii=False, indent=1)
    gloss = {}
    for l in open(os.path.join(HERE, "gloss.lst"), encoding="utf-8"):
        if l.strip() and not l.startswith("#"):
            k, _, v = l.partition("=")
            gloss[k.strip()] = v.strip()
    with open(os.path.join(OUT, "gloss.json"), "w", encoding="utf-8") as fh:
        json.dump(gloss, fh, ensure_ascii=False, indent=0)
    print(f"total: {sum(i['sections'] for i in items)} sections, {sum(i['questions'] for i in items)} exercises")
    if bad:
        sys.exit(f"{bad} unknown links")


if __name__ == "__main__":
    main()
