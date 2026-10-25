#!/usr/bin/env python3
"""Build library/pos/<id>.json and index.json from the plain-text sources in this folder.

Source format (one file per part of speech, NN-id.txt, NN gives the order):
  header lines until the first "## ":   id: / el: / title: / span: / blurb:   then free intro paragraphs
  "## LEVEL | Greek heading | English heading"  starts a section
  blocks are separated by blank lines:
    | a | b | c          table; the first row is the header, "|-" lines are ignored
    > Greek || English   example lines
    ! text               pitfall / tip callout
    - item               bullet list
    ? question | option | *right option | option || explanation     self-check question
    anything else        paragraph (**bold**, *italic*)
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)


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
    kind = lambda l: l[:1] if l[:1] in "|>!-?" and (l[1:2] == " " or l[:1] == "|") else "p"
    groups = []
    for l in lines:
        k = kind(l)
        if groups and groups[-1][0] == k and k != "p":
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
        elif k == "?":
            qs = []
            for l in ls:
                body, _, why = l[2:].partition("||")
                parts = [p.strip() for p in body.split(" | ")]
                opts = parts[1:]
                ans = [o[1:] for o in opts if o.startswith("*")]
                if len(ans) != 1 or len(opts) < 2:
                    sys.exit(f"{path}: question needs exactly one *answer: {l}")
                qs.append({"q": parts[0], "options": [o.lstrip("*") for o in opts], "answer": ans[0], "why": why.strip()})
            out.append({"check": qs})
    return out


def main():
    files = sorted(f for f in os.listdir(HERE) if f.endswith(".txt"))
    items = []
    for f in files:
        doc = parse(os.path.join(HERE, f))
        nq = sum(len(b["check"]) for s in doc["sections"] for b in s["body"] if "check" in b)
        with open(os.path.join(OUT, doc["id"] + ".json"), "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
        items.append({"id": doc["id"], "file": doc["id"] + ".json", "el": doc["el"], "title": doc["title"],
                      "span": doc.get("span", ""), "blurb": doc.get("blurb", ""), "sections": len(doc["sections"]), "questions": nq})
        print(f"{doc['id']:14} {len(doc['sections']):3} sections {nq:3} questions")
    with open(os.path.join(OUT, "index.json"), "w", encoding="utf-8") as fh:
        json.dump({"items": items}, fh, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
