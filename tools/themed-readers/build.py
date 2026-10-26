#!/usr/bin/env python3
"""Build one bilingual reader shelf (shared format, viewer app/bilingual.js) from the sources in <shelf>/.
Usage: python3 build.py <shelf> [out_dir]   shelves: epistimi, mathiatriki, athlitismos
 <shelf>/meta.py     SHELF = dict(el, title, intro_el, intro_en)
 <shelf>/sources.py  SRC = {key: (text, url or None)}
 <shelf>/part*.py    PART = dict(id, el, en, dates?, intro_el?, intro_en?); CHAPTERS = [dict(...)] with paragraphs (el, en, [source keys])
 <shelf>/images.json {chapter_id: {file, caption, caption_en, credit, license, source}}
 gloss.txt (shared) and <shelf>/gloss.txt: "form = lemma — gloss" lines; a chapter gets only the forms it uses.
Default out: /mnt/project-files/app/library/<shelf>"""
import importlib.util, json, os, re, sys, glob, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
SHELF = sys.argv[1]
D = os.path.join(HERE, SHELF)
OUT = sys.argv[2] if len(sys.argv) > 2 else f"/mnt/project-files/app/library/{SHELF}"
os.makedirs(OUT, exist_ok=True)

def mod(path):
    spec = importlib.util.spec_from_file_location(SHELF + "_" + os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

META = mod(os.path.join(D, "meta.py")).SHELF
SRC = mod(os.path.join(D, "sources.py")).SRC
IMAGES = json.load(open(os.path.join(D, "images.json"), encoding="utf-8")) if os.path.exists(os.path.join(D, "images.json")) else {}
GTXT = {}
for gf in (os.path.join(HERE, "gloss.txt"), os.path.join(D, "gloss.txt")):
    if os.path.exists(gf):
        for line in open(gf, encoding="utf-8"):
            if "=" in line and not line.startswith("#"):
                f, g = line.split("=", 1); GTXT[f.strip()] = g.strip()

def wc(t):
    m = re.search(r"“([^”]+)”", t)
    q = m.group(1) if m else (t.split(",")[1].strip() if "," in t else t)
    return "https://search.worldcat.org/search?q=" + urllib.parse.quote(q)

parts, items, nq = [], [], 0
for path in sorted(glob.glob(os.path.join(D, "part*.py")), key=lambda p: int(re.search(r"part(\d+)", p).group(1))):
    m = mod(path)
    parts.append(m.PART)
    for c in m.CHAPTERS:
        order = []
        for s in c["sections"]:
            for p in s["paras"]:
                for k in p[2]:
                    if k not in SRC: raise SystemExit(f"{c['id']}: unknown source {k}")
                    if k not in order: order.append(k)
        num = {k: i + 1 for i, k in enumerate(order)}
        ch = {"id": c["id"], "el": c["el"], "title": c["title"], "level": c["level"], "dates": c.get("dates", ""), "part": m.PART["id"]}
        if c["id"] in IMAGES: ch["image"] = IMAGES[c["id"]]
        ch["summary_en"] = c["summary_en"]
        ch["sections"] = [{"id": s["id"], "el": s["el"], "en": s["en"],
                           "paras": [{"el": p[0], "en": p[1], "cite": [num[k] for k in p[2]]} for p in s["paras"]]} for s in c["sections"]]
        ch["grammar"] = [{"level": g["level"], "title": g["title"], "el": g.get("el", ""), "en": g["en"],
                          "examples": [{"el": e[0], "en": e[1]} for e in g.get("examples", [])]} for g in c["grammar"]]
        ch["terms"] = [{"el": t[0], "en": t[1], "def_el": t[2], "def_en": t[3]} for t in c["terms"]]
        toks = set(re.findall(r"[Ͱ-Ͽἀ-῿]+", json.dumps(ch, ensure_ascii=False) + json.dumps(c, ensure_ascii=False)))
        ch["gloss"] = {f: g for f, g in GTXT.items() if f in toks}
        ch["questions"] = [{"q": q[0], "options": q[1], "answer": q[2], "why": q[3]} for q in c["questions"]]
        for q in ch["questions"]:
            assert q["answer"] in q["options"], (c["id"], q["q"])
        nq += len(ch["questions"])
        ch["vocab"] = c["vocab"]
        ch["sources"] = [{"n": num[k], "text": SRC[k][0], "url": SRC[k][1] or wc(SRC[k][0])} for k in order]
        fn = c["id"] + ".json"
        json.dump(ch, open(os.path.join(OUT, fn), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        items.append({"id": c["id"], "file": fn, "el": c["el"], "title": c["title"], "level": c["level"], "part": m.PART["id"], "dates": c.get("dates", "")})

idx = {"kind": "bilingual", "el": META["el"], "title": META["title"], "intro_el": META["intro_el"], "intro_en": META["intro_en"],
       "parts": [{k: p[k] for k in ("id", "el", "en", "dates", "intro_el", "intro_en") if k in p} for p in parts], "items": items}
json.dump(idx, open(os.path.join(OUT, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{SHELF}: {len(items)} chapters, {nq} questions in {len(parts)} parts → {OUT}")
