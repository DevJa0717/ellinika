#!/usr/bin/env python3
"""Build one arts-and-tradition bilingual reader shelf (mousiki, skini, eortes) into library/<shelf>/.
Usage: python3 build.py <shelf> [--out DIR]   (default /mnt/project-files/app/library/<shelf>)
Sources: <shelf>/shelf.py (SHELF = {el, title, intro_el, intro_en}) and <shelf>/part*.py, each defining
  PART = dict(id, el, en, dates?, intro_el, intro_en)
  SRC = {key: (text, url_or_None)}                      sources cited by this part's chapters
  GLOSS = {form: "lemma — gloss"}                       tap-lookup glosses for forms the lexicon misses (all chapters of the part)
  CHAPTERS = [dict(id, el, title, level, dates, summary_en, sections=[dict(id, el, en, paras=[(el, en, [src keys])])],
                   grammar=[dict(level, title, el, en, examples=[(el, en)])], terms=[(el, en, def_el, def_en)],
                   questions=[(q, [options], answer, why)], vocab=[lemmas], listen=[(title, url, note_en)]?)]
Images: <shelf>/images.json {chapter_id: {file, caption, caption_en, credit, license, source}}.
A part file that fails to import is skipped with a warning, so writers can work on parts in parallel."""
import importlib.util, json, os, re, sys, glob, urllib.parse, traceback
HERE = os.path.dirname(os.path.abspath(__file__))
shelf = sys.argv[1]
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else f"/mnt/project-files/app/library/{shelf}"
D = os.path.join(HERE, shelf)
os.makedirs(OUT, exist_ok=True)

def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3] + "_" + shelf, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def wc(t):
    m = re.search(r"“([^”]+)”|«([^»]+)»", t)
    q = (m.group(1) or m.group(2)) if m else (t.split(",")[1].strip() if "," in t else t)
    return "https://search.worldcat.org/search?q=" + urllib.parse.quote(q)

SHELF = load(os.path.join(D, "shelf.py")).SHELF
IMAGES = json.load(open(os.path.join(D, "images.json"))) if os.path.exists(os.path.join(D, "images.json")) else {}
GLOBAL_GLOSS = {}
if os.path.exists(os.path.join(HERE, "gloss.txt")):
    for line in open(os.path.join(HERE, "gloss.txt"), encoding="utf-8"):
        if "=" in line and not line.startswith("#"):
            f, g = line.split("=", 1); GLOBAL_GLOSS[f.strip()] = g.strip()

parts, items, nq = [], [], 0
for path in sorted(glob.glob(os.path.join(D, "part*.py")), key=lambda p: int(re.sub(r"\D", "", os.path.basename(p)) or 0)):
    try:
        m = load(path)
        P, SRC, GL = m.PART, getattr(m, "SRC", {}), getattr(m, "GLOSS", {})
        built = []
        for c in m.CHAPTERS:
            order = []
            for s in c["sections"]:
                for p in s["paras"]:
                    for k in p[2]:
                        if k not in SRC: raise ValueError(f"{c['id']}: unknown source {k}")
                        if k not in order: order.append(k)
            num = {k: i + 1 for i, k in enumerate(order)}
            ch = {"id": c["id"], "el": c["el"], "title": c["title"], "level": c["level"], "dates": c.get("dates", ""), "part": P["id"]}
            if c["id"] in IMAGES: ch["image"] = IMAGES[c["id"]]
            ch["summary_en"] = c["summary_en"]
            ch["sections"] = [{"id": s["id"], "el": s["el"], "en": s["en"],
                               "paras": [{"el": p[0], "en": p[1], "cite": [num[k] for k in p[2]]} for p in s["paras"]]} for s in c["sections"]]
            ch["grammar"] = [{"level": g["level"], "title": g["title"], "el": g.get("el", ""), "en": g["en"],
                              "examples": [{"el": e[0], "en": e[1]} for e in g.get("examples", [])]} for g in c["grammar"]]
            ch["terms"] = [{"el": t[0], "en": t[1], "def_el": t[2], "def_en": t[3]} for t in c["terms"]]
            if c.get("listen"): ch["listen"] = [{"title": l[0], "url": l[1], "note": l[2] if len(l) > 2 else ""} for l in c["listen"]]
            ch["gloss"] = {}
            ch["questions"] = [{"q": q[0], "options": q[1], "answer": q[2], "why": q[3]} for q in c["questions"]]
            for q in ch["questions"]:
                if q["answer"] not in q["options"]: raise ValueError(f"{c['id']}: answer not in options: {q['q']}")
            ch["vocab"] = c["vocab"]
            ch["sources"] = [{"n": num[k], "text": SRC[k][0], "url": SRC[k][1] or wc(SRC[k][0])} for k in order]
            toks = set(re.findall(r"[Ͱ-Ͽἀ-῿]+", json.dumps(ch, ensure_ascii=False)))
            low = {t.lower() for t in toks}
            gl = {**GLOBAL_GLOSS, **GL, **c.get("gloss", {})}
            ch["gloss"] = {f: g for f, g in gl.items() if f in toks or f.lower() in low}
            built.append(ch)
        for ch in built:
            json.dump(ch, open(os.path.join(OUT, ch["id"] + ".json"), "w"), ensure_ascii=False, indent=1)
            items.append({"id": ch["id"], "file": ch["id"] + ".json", "el": ch["el"], "title": ch["title"], "level": ch["level"], "part": P["id"], "dates": ch["dates"]})
            nq += len(ch["questions"])
        parts.append({k: P[k] for k in ("id", "el", "en", "dates", "intro_el", "intro_en") if k in P})
    except Exception:
        print(f"WARNING: skipped {os.path.basename(path)}:\n" + traceback.format_exc(limit=2), file=sys.stderr)

idx = {"kind": "bilingual", **{k: SHELF[k] for k in ("el", "title", "intro_el", "intro_en")}, "parts": parts, "items": items}
json.dump(idx, open(os.path.join(OUT, "index.json"), "w"), ensure_ascii=False, indent=1)
print(f"{shelf}: {len(items)} chapters in {len(parts)} parts, {nq} questions → {OUT}")
