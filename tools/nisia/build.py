#!/usr/bin/env python3
"""Build a bilingual reader shelf (shared format, app/bilingual.js) from the part*.py sources in a folder.
Used by tools/nisia (the islands one by one) and tools/diaspora (the Greek diaspora).
Usage: python3 build.py [src_dir]   (default: this folder). The folder holds:
  meta.py     SHELF, EL, TITLE, INTRO_EL, INTRO_EN
  common.py   SRC = {key: (text, url or None)}
  part*.py    PART = dict(id, el, en, dates?, intro_el, intro_en); CHAPTERS = [dict(...)], paragraphs are (el, en, [source keys]);
              a key "wp:Title" or "el:Τίτλος" cites that English or Greek Wikipedia article without listing it in common.py
  gloss.txt   "form = lemma — gloss" lines; a chapter gets the entries whose form occurs in it
              (tools/nisia/gloss.txt is also read as a fallback for every shelf)
  images.json {chapter_id: {file, caption, caption_en, credit, license, source}}
A chapter may list see=[(shelf, chapter_id, el, en)] for links to related chapters on other shelves."""
import importlib.util, json, os, re, sys, glob, urllib.parse
HERE = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import meta
from common import SRC

OUT = f"/mnt/project-files/app/library/{meta.SHELF}"
os.makedirs(OUT, exist_ok=True)
load = lambda f: json.load(open(os.path.join(HERE, f), encoding="utf-8")) if os.path.exists(os.path.join(HERE, f)) else {}
IMAGES = load("images.json")


def wc(t):
    """WorldCat search for a source without a URL: the quoted title, else the part after the author."""
    m = re.search(r"“([^”]+)”|«([^»]+)»", t)
    q = (m.group(1) or m.group(2)) if m else (t.split(",")[1].strip() if "," in t else t)
    return "https://search.worldcat.org/search?q=" + urllib.parse.quote(q)


GTXT = {}
for path in [os.path.join(HERE, "gloss.txt"), os.path.join(os.path.dirname(os.path.abspath(__file__)), "gloss.txt"), os.path.join(os.path.dirname(os.path.abspath(__file__)), "gloss-common.txt")]:
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            if "=" in line and not line.startswith("#"):
                f, g = line.split("=", 1); GTXT.setdefault(f.strip(), g.strip())

parts, items, nq = [], [], 0
for path in sorted(glob.glob(os.path.join(HERE, "part*.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    if not m.CHAPTERS: continue
    if not any(x["id"] == m.PART["id"] for x in parts): parts.append(m.PART)  # a part may span part2.py, part2b.py …
    for c in m.CHAPTERS:
        order = []
        for s in c["sections"]:
            for p in s["paras"]:
                for k in p[2]:
                    if k[:3] in ("wp:", "el:") and k not in SRC:
                        lang = "en" if k[:3] == "wp:" else "el"
                        SRC[k] = (f"Wikipedia ({'English' if lang == 'en' else 'ελληνική'}), “{k[3:]}”", f"https://{lang}.wikipedia.org/wiki/" + urllib.parse.quote(k[3:].replace(" ", "_")))
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
        if c.get("see"): ch["see"] = [{"href": f"#{s[0]}.{s[1]}", "el": s[2], "en": s[3]} for s in c["see"]]
        ch["sources"] = [{"n": num[k], "text": SRC[k][0], "url": SRC[k][1] or wc(SRC[k][0])} for k in order]
        fn = c["id"] + ".json"
        json.dump(ch, open(os.path.join(OUT, fn), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        items.append({"id": c["id"], "file": fn, "el": c["el"], "title": c["title"], "level": c["level"], "part": m.PART["id"], "dates": c.get("dates", "")})

idx = {"kind": "bilingual", "el": meta.EL, "title": meta.TITLE, "intro_el": meta.INTRO_EL, "intro_en": meta.INTRO_EN,
       "parts": [{k: p[k] for k in ("id", "el", "en", "dates", "intro_el", "intro_en") if k in p} for p in parts], "items": items}
json.dump(idx, open(os.path.join(OUT, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{meta.SHELF}: {len(items)} chapters in {len(parts)} parts, {nq} questions → {OUT}")
