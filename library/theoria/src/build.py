#!/usr/bin/env python3
"""Build library/theoria/<id>.json and index.json (Schaum's-style grammar outline: theory, solved problems, drills).

Source format: one file per chapter, NN-id.txt (NN = chapter number and order). Same block syntax as library/syntax/src,
plus solved problems:
  header lines until the first "## ":   id: / el: / title: / span: / blurb:   then free intro paragraphs
  "## LEVEL | Greek heading | English heading"  starts a section
  blocks are separated by blank lines:
    | a | b | c          table; the first row is the header, "|-" lines are ignored
    > Greek || English   example lines
    ! text               pitfall / tip callout
    - item               bullet list
    S problem => solution || explanation                             solved problem (worked example, answer shown)
    ? question | option | *right option | option || explanation     multiple choice drill
    ~ cue | Greek sentence | other accepted order || explanation     put the words in order (tiles from the first sentence)
    = prompt => answer | other accepted answer || explanation        write the answer
    @ lesson-id, pos.<doc>~<n>, syntax.<doc>, cards.<id>, klisi        "Go deeper" links (checked here)
    anything else        paragraph (**bold**, *italic*)
Every drill gets a stable id (chapter id + hash of prompt and answer) for the spaced-repetition schedule in theoria.js.
"""
import hashlib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
APP = os.path.dirname(os.path.dirname(OUT))


def link_table():
    t = {"klisi": {"href": "#klisi", "kind": "Drill books", "el": "Τετράδια κλίσης", "title": "Declension and conjugation drill books"},
         "errors": {"href": "#errors", "kind": "Error hunt", "el": "Βρες το λάθος", "title": "Error hunt"},
         "ref": {"href": "#ref", "kind": "Tables", "el": "Πίνακες γραμματικής", "title": "Grammar tables"}}
    course = json.load(open(os.path.join(APP, "lessons/course.json"), encoding="utf-8"))
    for u in course["units"]:
        for l in u.get("lessons", []):
            t[l["id"]] = {"href": "#" + l["id"], "kind": "Lesson", "el": l.get("el", ""), "title": l.get("title", "")}
    for shelf, kind in (("pos", "Part of speech"), ("syntax", "Syntax")):
        idx = json.load(open(os.path.join(APP, f"library/{shelf}/index.json"), encoding="utf-8"))
        for it in idx["items"]:
            d = json.load(open(os.path.join(APP, f"library/{shelf}", it["file"]), encoding="utf-8"))
            t[f"{shelf}.{it['id']}"] = {"href": f"#{shelf}.{it['id']}", "kind": kind, "el": d["el"], "title": d["title"]}
            for i, s in enumerate(d["sections"]):
                t[f"{shelf}.{it['id']}~{i}"] = {"href": f"#{shelf}.{it['id']}~{i}", "kind": kind, "el": s["el"], "title": s["title"]}
    cards = os.path.join(APP, "library/cards/index.json")
    if os.path.exists(cards):
        for c in json.load(open(cards, encoding="utf-8"))["cards"]:
            t["cards." + c["id"]] = {"href": "#cards." + c["id"], "kind": "Card", "el": c["el"], "title": c["title"]}
    return t


def parse(path):
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    head, _, rest = text.partition("\n## ")
    doc = {"sections": []}
    intro = []
    for blk in re.split(r"\n\s*\n", head.strip()):
        lines = blk.strip().split("\n")
        if all(re.match(r"^(id|el|title|span|blurb|part):", l) for l in lines):
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


def words(s):
    return [w.lower() for w in re.findall(r"[\w'’,]+", s.replace(",", ""))]


def blocks_of(blk, path):
    lines = [l.rstrip() for l in blk.strip().split("\n")]
    out = []
    kind = lambda l: l[:1] if l[:1] in "|>!-?~=@S" and (l[1:2] == " " or l[:1] == "|") else "p"
    groups = []
    ex_kinds = "?~="
    for l in lines:
        k = kind(l)
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
        elif k == "S":
            sv = []
            for l in ls:
                body, _, why = l[2:].partition("||")
                q, arrow, a = body.partition("=>")
                if not arrow:
                    sys.exit(f"{path}: solved problem needs '=> solution': {l}")
                sv.append({"q": q.strip(), "a": a.strip(), "why": why.strip()})
            out.append({"solved": sv})
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
                    if len(set(o.lstrip("*") for o in opts)) != len(opts):
                        sys.exit(f"{path}: duplicate option: {l}")
                    q = {"type": "choice", "q": parts[0], "options": [o.lstrip("*") for o in opts], "answer": ans[0], "why": why}
                elif l[0] == "~":
                    parts = [p.strip() for p in body.split(" | ")]
                    if len(parts) < 2:
                        sys.exit(f"{path}: order item needs a cue and a sentence: {l}")
                    for alt in parts[2:]:
                        if sorted(words(alt)) != sorted(words(parts[1])):
                            sys.exit(f"{path}: accepted order uses other words than the first: {alt}")
                    q = {"type": "order", "q": parts[0], "answer": parts[1], "accept": parts[2:], "why": why}
                else:
                    prompt, arrow, ans = body.partition("=>")
                    if not arrow:
                        sys.exit(f"{path}: write item needs '=> answer': {l}")
                    acc = [a.strip() for a in ans.split(" | ") if a.strip()]
                    q = {"type": "write", "q": prompt.strip(), "answer": acc[0], "accept": acc[1:], "why": why}
                qs.append(q)
            out.append({"check": qs})
    return out


def main():
    links = link_table()
    files = sorted(f for f in os.listdir(HERE) if re.match(r"^\d\d-.*\.txt$", f))
    docs = []
    for f in files:
        d = parse(os.path.join(HERE, f))
        d["num"] = int(f[:2])
        docs.append(d)
    for d in docs:
        links["theoria." + d["id"]] = {"href": "#theoria." + d["id"], "kind": "Chapter", "el": d["el"], "title": d["title"]}
    bad = 0
    seen = {}

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
    tot = {"solved": 0, "choice": 0, "order": 0, "write": 0}
    for doc in docs:
        resolve(doc["intro"], doc["id"])
        nsolved = 0
        for s in doc["sections"]:
            resolve(s["body"], doc["id"] + " / " + s["title"])
            for b in s["body"]:
                if "solved" in b:
                    nsolved += len(b["solved"])
                for q in b.get("check", []):
                    h = hashlib.sha1((q["q"] + "|" + q["answer"]).encode("utf-8")).hexdigest()[:8]
                    q["id"] = f"{doc['id']}-{h}"
                    if q["id"] in seen:
                        print(f"  duplicate drill in {doc['id']}: {q['q']}"); bad += 1
                    seen[q["id"]] = 1
        qs = [q for s in doc["sections"] for b in s["body"] if "check" in b for q in b["check"]]
        with open(os.path.join(OUT, doc["id"] + ".json"), "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=0)
        items.append({"id": doc["id"], "num": doc["num"], "file": doc["id"] + ".json", "el": doc["el"], "title": doc["title"],
                      "span": doc.get("span", ""), "blurb": doc.get("blurb", ""), "sections": len(doc["sections"]),
                      **({"part": [x.strip() for x in doc["part"].split("|")]} if doc.get("part") else {}),
                      "solved": nsolved, "questions": len(qs), "ids": [q["id"] for q in qs]})
        kinds = {k: sum(q["type"] == k for q in qs) for k in ("choice", "order", "write")}
        tot["solved"] += nsolved
        for k, v in kinds.items():
            tot[k] += v
        print(f"{doc['num']:2} {doc['id']:16} {len(doc['sections']):2} sections {nsolved:3} solved {len(qs):4} drills {kinds}")
    with open(os.path.join(OUT, "index.json"), "w", encoding="utf-8") as fh:
        json.dump({"items": items}, fh, ensure_ascii=False, indent=0)
    # every drill in one file, for the spaced-review sessions that mix chapters
    bank = {}
    for doc in docs:
        for si, s in enumerate(doc["sections"]):
            for b in s["body"]:
                for q in b.get("check", []):
                    bank[q["id"]] = {**{k: v for k, v in q.items() if k != "id" and v not in ("", [])}, "c": doc["id"], "s": si}
    with open(os.path.join(OUT, "drills.json"), "w", encoding="utf-8") as fh:
        json.dump(bank, fh, ensure_ascii=False, separators=(",", ":"))
    ref = os.path.join(HERE, "references.txt")
    if os.path.exists(ref):
        r = parse(ref)
        resolve(r["intro"], "references")
        with open(os.path.join(OUT, "references.json"), "w", encoding="utf-8") as fh:
            json.dump(r, fh, ensure_ascii=False, indent=0)
    gloss = {}
    gl = os.path.join(HERE, "gloss.lst")
    if os.path.exists(gl):
        for l in open(gl, encoding="utf-8"):
            if l.strip() and not l.startswith("#"):
                k, _, v = l.partition("=")
                gloss[k.strip()] = v.strip()
    with open(os.path.join(OUT, "gloss.json"), "w", encoding="utf-8") as fh:
        json.dump(gloss, fh, ensure_ascii=False, indent=0)
    print(f"total: {len(docs)} chapters, {sum(i['sections'] for i in items)} sections, {tot['solved']} solved problems, "
          f"{tot['choice'] + tot['order'] + tot['write']} drills {tot}")
    if bad:
        sys.exit(f"{bad} problems")


if __name__ == "__main__":
    main()
