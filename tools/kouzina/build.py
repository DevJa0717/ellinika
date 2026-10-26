#!/usr/bin/env python3
"""Build library/kouzina/ (index.json + one JSON per chapter) from the part*.py sources in this folder.
Usage: python3 build.py [out_dir]   (default /mnt/project-files/app/library/kouzina)
Same bilingual format as the other readers, plus two optional blocks rendered by app/bilingual.js and build_bilingual.py:
  section tables=[dict(el, en, cols=[(header, "el"|"en")], rows=[(cell, …)])]
  chapter recipe=dict(serves=(el, en), time=(el, en), groups=[(el, en, [(el, en), …])], steps=[(el, en)], tips=[(el, en)])
Glosses: gloss.txt ("form = lemma — gloss", added to a chapter when the form occurs in it). Images: images.json {chapter_id: {...}}."""
import importlib.util, json, os, re, sys, glob, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import SRC

OUT = sys.argv[1] if len(sys.argv) > 1 else "/mnt/project-files/app/library/kouzina"
os.makedirs(OUT, exist_ok=True)
IMAGES = json.load(open(os.path.join(HERE, "images.json"))) if os.path.exists(os.path.join(HERE, "images.json")) else {}
def wc(t):
    m = re.search(r"“([^”]+)”", t)
    q = m.group(1) if m else (t.split(",")[1].strip() if "," in t else t)
    return "https://search.worldcat.org/search?q=" + urllib.parse.quote(q)
GTXT = {}
for line in open(os.path.join(HERE, "gloss.txt"), encoding="utf-8"):
    if "=" in line and not line.startswith("#"):
        f, g = line.split("=", 1); GTXT[f.strip()] = g.strip()

parts, items, seen_terms = [], [], {}
for path in sorted(glob.glob(os.path.join(HERE, "part*.py")), key=lambda p: int(re.search(r"part(\d+)", p).group(1))):
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
        if c.get("region"): ch["region"] = c["region"]
        if c["id"] in IMAGES: ch["image"] = IMAGES[c["id"]]
        ch["summary_en"] = c["summary_en"]
        secs = []
        for s in c["sections"]:
            o = {"id": s["id"], "el": s["el"], "en": s["en"], "paras": [{"el": p[0], "en": p[1], "cite": [num[k] for k in p[2]]} for p in s["paras"]]}
            if s.get("tables"):
                o["tables"] = [{"el": t.get("el", ""), "en": t.get("en", ""), "cols": [{"h": h, "lang": l} for h, l in t["cols"]],
                                "rows": [list(r) for r in t["rows"]]} for t in s["tables"]]
                for t in o["tables"]:
                    for r in t["rows"]: assert len(r) == len(t["cols"]), (c["id"], r)
            secs.append(o)
        ch["sections"] = secs
        if c.get("recipe"):
            r = c["recipe"]
            ch["recipe"] = {"serves_el": r["serves"][0], "serves_en": r["serves"][1], "time_el": r["time"][0], "time_en": r["time"][1],
                            "groups": [{"el": g[0], "en": g[1], "items": [{"el": x[0], "en": x[1]} for x in g[2]]} for g in r["groups"]],
                            "steps": [{"el": x[0], "en": x[1]} for x in r["steps"]], "tips": [{"el": x[0], "en": x[1]} for x in r.get("tips", [])]}
        ch["grammar"] = [{"level": g["level"], "title": g["title"], "el": g.get("el", ""), "en": g["en"],
                          "examples": [{"el": e[0], "en": e[1]} for e in g.get("examples", [])]} for g in c["grammar"]]
        ch["terms"] = [{"el": t[0], "en": t[1], "def_el": t[2], "def_en": t[3]} for t in c["terms"]]
        for t in c["terms"]:
            if t[0] in seen_terms: print(f"  note: term {t[0]} repeats ({seen_terms[t[0]]} and {c['id']})")
            seen_terms.setdefault(t[0], c["id"])
        toks = set(re.findall(r"[Ͱ-Ͽἀ-῿]+", json.dumps(ch, ensure_ascii=False) + json.dumps(c, ensure_ascii=False)))
        ch["gloss"] = {f: g for f, g in GTXT.items() if f in toks}
        ch["questions"] = [{"q": q[0], "options": q[1], "answer": q[2], "why": q[3]} for q in c["questions"]]
        for q in ch["questions"]:
            assert q["answer"] in q["options"], (c["id"], q["q"])
        ch["vocab"] = c["vocab"]
        ch["sources"] = [{"n": num[k], "text": SRC[k][0], "url": SRC[k][1] or wc(SRC[k][0])} for k in order]
        fn = c["id"] + ".json"
        json.dump(ch, open(os.path.join(OUT, fn), "w"), ensure_ascii=False, indent=1)
        items.append({"id": c["id"], "file": fn, "el": c["el"], "title": c["title"], "level": c["level"], "part": m.PART["id"], "dates": c.get("dates", "")})

idx = {"kind": "bilingual", "el": "Η ελληνική κουζίνα", "title": "The Greek kitchen: a bilingual cookbook of the regions, with the history, goods and heritage of Greek food",
       "intro_el": "Οι πιο γνωστές συνταγές από όλες τις περιοχές της Ελλάδας, με τα υλικά, τα σκεύη, τα ρήματα και τις μονάδες μέτρησης που χρειάζεται κανείς για να μαγειρέψει στα ελληνικά. Ακολουθούν η ιστορία της μαγειρικής από την αρχαιότητα ως σήμερα, τα καθημερινά και τα πολύτιμα αγαθά, η γεωργία, τα προστατευμένα προϊόντα και η μεσογειακή διατροφή. Τα ελληνικά κείμενα είναι γύρω στο Β2 και ανεβαίνουν σταδιακά.",
       "intro_en": "The best-known dishes of every region of Greece, with the ingredients, utensils, cooking verbs and measures you need to cook in Greek. After the recipes come the history of Greek cooking from antiquity to the present, the everyday and luxury goods of the Greek food system, the nature of Greek farming, the protected foods that stand for Greek identity, and the Greek part in the “Mediterranean diet” and its health benefits. The Greek text is around B2 and rises gradually; the English parallel carries the fuller detail. Every recipe gives its ingredients and method in both languages, written with the imperative as Greek cookbooks do; each chapter has new terms, grammar notes, a quiz, words to keep and numbered sources. Tap any Greek word to look it up.",
       "parts": [{k: p[k] for k in ("id", "el", "en", "dates", "intro_el", "intro_en") if k in p} for p in parts], "items": items}
json.dump(idx, open(os.path.join(OUT, "index.json"), "w"), ensure_ascii=False, indent=1)
print(f"{len(items)} chapters in {len(parts)} parts → {OUT}")
