#!/usr/bin/env python3
"""Build the bilingual history reader (#istoria) from src/e*.py into app/library/istoria/.
Usage: python3 build.py [--out /mnt/project-files/app]"""
import json, sys, os, importlib, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "src"))
from images import IMAGES
import re as _re
GL = {}
for _l in open(os.path.join(HERE, "src/gloss.txt"), encoding="utf-8"):
    if "=" in _l and not _l.startswith("#"):
        _f, _g = _l.split("=", 1); GL[_f.strip()] = _g.strip()
def chapter_gloss(ch):
    txt = json.dumps({k: v for k, v in ch.items() if k not in ("sources",)}, ensure_ascii=False)
    forms = set(_re.findall(r"[\u0370-\u03ff\u1f00-\u1fff]+", txt))
    return {f: GL[f] for f in sorted(forms) if f in GL}
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "/mnt/project-files/app"
THEMES = [
    {"id": "language", "el": "Γλώσσα", "en": "Language"},
    {"id": "art", "el": "Τέχνη", "en": "Art"},
    {"id": "culture", "el": "Πολιτισμός", "en": "Culture"},
    {"id": "politics", "el": "Πολιτική", "en": "Politics and society"},
    {"id": "science", "el": "Επιστήμη", "en": "Science and technology"},
]
eras = sorted(f[:-3] for f in os.listdir(os.path.join(HERE, "src")) if f.startswith("e") and f[1:-3].isdigit())
eras.sort(key=lambda e: int(e[1:]))
idx = {"kind": "bilingual", "el": "Ιστορία των Ελλήνων", "title": "Greek history, from prehistory to the eve of 1821",
       "intro_el": "Η ιστορία του ελληνικού κόσμου από την Παλαιολιθική εποχή ως τις παραμονές της Επανάστασης του 1821, σε οκτώ εποχές. Κάθε εποχή έχει πέντε κεφάλαια: γλώσσα, τέχνη, πολιτισμός, πολιτική και επιστήμη. Τα ελληνικά γίνονται σταδιακά πιο απαιτητικά, από το Β1+ ως το Γ1.",
       "intro_en": "The history of the Greek world from the Palaeolithic to the eve of the Revolution of 1821, in eight eras of five chapters each: language, art, culture, politics and society, science and technology. The Greek is written at about B2 and grows gradually harder, from B1+ in prehistory to C1 under Ottoman and Venetian rule; the English beside it is not a word-for-word crib but a fuller account that adds the dates, names, debates and context the Greek leaves out. Each chapter has grammar notes on the structures it introduces, definitions of new terms, questions, a word list for your review, and numbered sources for every paragraph.",
       "parts": [], "themes": THEMES, "items": []}
os.makedirs(os.path.join(OUT, "library/istoria"), exist_ok=True)
seen_terms = {}
for e in eras:
    m = importlib.import_module(e)
    era = dict(m.ERA)
    idx["parts"].append({k: era[k] for k in ("id", "el", "en", "dates", "dates_en", "intro_el", "intro_en") if k in era})
    for ch in m.CH:
        ch = dict(ch)
        ch.setdefault("level", era["level"])
        ch["part"] = era["id"]
        im = IMAGES.get(ch.get("image"))
        if im: ch["image"] = im
        else: ch.pop("image", None)
        ch["sources"] = [dict(s, n=i + 1) for i, s in enumerate(ch["sources"])]
        n = len(ch["sources"])
        for s in ch["sections"]:
            for p in s["paras"]:
                assert all(1 <= c <= n for c in p["cite"]), (ch["id"], p["cite"])
        for t in ch["terms"]:
            if t["el"] in seen_terms: print("term repeated:", t["el"], ch["id"], "first in", seen_terms[t["el"]])
            seen_terms.setdefault(t["el"], ch["id"])
        ch["gloss"] = chapter_gloss(ch)
        for q in ch["questions"]:
            random.Random(ch["id"] + q["q"]).shuffle(q["options"])
        fn = ch["id"] + ".json"
        json.dump(ch, open(os.path.join(OUT, "library/istoria", fn), "w"), ensure_ascii=False, indent=1)
        idx["items"].append({"id": ch["id"], "file": fn, "el": ch["el"], "title": ch["title"], "level": ch["level"], "part": era["id"], "theme": ch["theme"], "dates": ch.get("dates", "")})
json.dump(idx, open(os.path.join(OUT, "library/istoria/index.json"), "w"), ensure_ascii=False, indent=1)
print(len(idx["items"]), "chapters in", len(idx["parts"]), "eras")
