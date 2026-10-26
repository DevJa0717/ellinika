#!/usr/bin/env python3
"""Build library/politeia/ (index.json + one JSON per chapter) from the part*.py sources in this folder.
Usage: python3 build.py [out_dir]   (default /mnt/project-files/app/library/politeia)
Glosses: gloss.json in this folder, {chapter_id: {form: "lemma — gloss"}} plus "*" for glosses shared by every chapter.
Images: images.json in this folder, {chapter_id: {file, caption, caption_en, credit, license, source}}."""
import importlib.util, json, os, sys, glob, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import SRC

OUT = sys.argv[1] if len(sys.argv) > 1 else "/mnt/project-files/app/library/politeia"
os.makedirs(OUT, exist_ok=True)
load = lambda f: json.load(open(os.path.join(HERE, f))) if os.path.exists(os.path.join(HERE, f)) else {}
def wc(t):
    """WorldCat search for a source without a URL: the quoted title, else the part after the author."""
    m = re.search(r"“([^”]+)”", t)
    q = m.group(1) if m else (t.split(",")[1].strip() if "," in t else t)
    return "https://search.worldcat.org/search?q=" + urllib.parse.quote(q)


GLOSS, IMAGES = load("gloss.json"), load("images.json")
import re
GTXT = {}
for line in open(os.path.join(HERE, "gloss.txt"), encoding="utf-8"):
    if "=" in line and not line.startswith("#"):
        f, g = line.split("=", 1); GTXT[f.strip()] = g.strip()

parts, items = [], []
for path in sorted(glob.glob(os.path.join(HERE, "part*.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
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
        ch["gloss"] = {**{f: g for f, g in GTXT.items() if f in toks}, **GLOSS.get("*", {}), **GLOSS.get(c["id"], {})}
        ch["questions"] = [{"q": q[0], "options": q[1], "answer": q[2], "why": q[3]} for q in c["questions"]]
        for q in ch["questions"]:
            assert q["answer"] in q["options"], (c["id"], q["q"])
        ch["vocab"] = c["vocab"]
        ch["sources"] = [{"n": num[k], "text": SRC[k][0], "url": SRC[k][1] or wc(SRC[k][0])} for k in order]
        fn = c["id"] + ".json"
        json.dump(ch, open(os.path.join(OUT, fn), "w"), ensure_ascii=False, indent=1)
        items.append({"id": c["id"], "file": fn, "el": c["el"], "title": c["title"], "level": c["level"], "part": m.PART["id"], "dates": c.get("dates", "")})

idx = {"kind": "bilingual", "el": "Το ελληνικό πολίτευμα", "title": "The Greek polity: state, law and politics",
       "intro_el": "Πώς λειτουργεί το ελληνικό κράτος: το Σύνταγμα, οι θεσμοί, η δικαιοσύνη, η διοίκηση, τα κόμματα, οι σχέσεις κράτους και κοινωνίας, οι επιρροές στη δημόσια πολιτική και η ελληνική πολιτική κουλτούρα. Τα ελληνικά κείμενα ξεκινούν γύρω στο Β1 και ανεβαίνουν σταδιακά ως το Γ1.",
       "intro_en": "How the Greek state works: the Constitution, the institutions, the courts, the administration, the parties, the relations between state and society, the internal and external forces that shape public policy, and the nuances of Greek political culture. The Greek text starts around B1 and rises gradually to C1; the English parallel carries the fuller detail. Each chapter has new-term definitions, grammar notes on the structures it uses, a quiz, words to keep and numbered sources; tap any Greek word to look it up.",
       "parts": [{k: p[k] for k in ("id", "el", "en", "intro_el", "intro_en") if k in p} for p in parts], "items": items}
json.dump(idx, open(os.path.join(OUT, "index.json"), "w"), ensure_ascii=False, indent=1)
print(f"{len(items)} chapters in {len(parts)} parts → {OUT}")
