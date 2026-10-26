#!/usr/bin/env python3
"""Build library/families/*.json and library/confusables/*.json from the sources in this folder.

Usage: python3 tools/wordfamilies/build.py [--app <app root>]   (default: the repo this file lives in)
Each family member is checked against the lexicon (data/lexicon/core-*.json); members not in it get a
chapter gloss so tap lookup still answers. Drills are generated here: English → Greek production items
from every family member and every confusable word, plus the authored gap-fills.
"""
import json, os, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
APP = sys.argv[sys.argv.index("--app") + 1] if "--app" in sys.argv else os.path.abspath(os.path.join(HERE, "..", ".."))

import fam_a, fam_b, fam_c, fam_d, conf_a, conf_b, conf_c
from gloss_extra import GLOSS

PARTS = {
    "Α": ("Τα δομικά υλικά", "The building blocks"),
    "Β": ("Προθήματα", "Prefixes"),
    "Γ": ("Επιθήματα", "Suffixes"),
    "Δ": ("Ρίζες και οικογένειες", "Root families"),
}
# Extra spellings accepted in the drills (standard variants).
ACCEPT = {
    "φοβιτσιάρης": ["φοβητσιάρης"],
    "παρατρώω": ["παρατρώγω"],
    "ξεχνώ": ["ξεχνάω"], "ξεκινώ": ["ξεκινάω"], "ξενυχτώ": ["ξενυχτάω"], "ξεπουλώ": ["ξεπουλάω"], "ξεπερνώ": ["ξεπερνάω"],
    "ξαναζώ": ["ξαναζάω"], "ξαναλέω": ["ξαναλέγω"], "προχωρώ": ["προχωράω"], "προτιμώ": ["προτιμάω"], "προσπαθώ": ["προσπαθάω"],
    "συζητώ": ["συζητάω"], "συμφωνώ": ["συμφωνάω"], "διαφωνώ": ["διαφωνάω"], "αποχωρώ": ["αποχωράω"], "αφαιρώ": ["αφαιράω"],
    "παρατηρώ": ["παρατηράω"], "παρακολουθώ": ["παρακολουθάω"], "κατηγορώ": ["κατηγοράω"], "κατοικώ": ["κατοικάω"],
    "συγχωρώ": ["συγχωράω"], "αντιδρώ": ["αντιδράω"], "αντιπαθώ": ["αντιπαθάω"], "αμφισβητώ": ["αμφισβητάω"],
    "οδηγώ": ["οδηγάω"], "κρατώ": ["κρατάω"], "μετρώ": ["μετράω"], "φιλώ": ["φιλάω"],
    "συγκρατώ": ["συγκρατάω"], "επικρατώ": ["επικρατάω"], 
    "επιθυμώ": ["επιθυμάω"], "θυμάμαι": ["θυμούμαι"],
    "φέρνω": ["φέρω"], "στέλνω": ["στέλλω"], "λέω": ["λέγω"],
    "αποδεικνύω": ["αποδείχνω"], "υπερήφανος": ["περήφανος"],
}

def load_lex():
    lex = {}
    for f in ["core-1000.json", "core-3000.json"]:
        for e in json.load(open(os.path.join(APP, "data", "lexicon", f), encoding="utf-8")):
            lex.setdefault(e["lemma"], e)
    return lex

def strip(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()

def write(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)

def build_families(lex):
    out_dir = os.path.join(APP, "library", "families")
    items, total, inlex = [], 0, 0
    chapters = [c for m in (fam_a, fam_b, fam_c, fam_d) for c in m.CHAPTERS]
    for c in chapters:
        gloss, drill = {}, []
        for g in c["groups"]:
            for m in g["members"]:
                total += 1
                e = lex.get(m["el"])
                m["lex"] = bool(e)
                if e:
                    inlex += 1
                    if e.get("pos"):
                        m["pos"] = e["pos"]
                else:
                    gloss[m["el"]] = f'{m["el"]} — {m["en"]}'
                    # Lower-case form too, for capitalised demonyms at the start of a sentence.
                if g.get("nodrill"):
                    continue
                drill.append({"en": m["en"], "hint": g["key"], "meaning": g["meaning"], "answer": m["el"],
                              "accept": ACCEPT.get(m["el"], []), "lex": m["lex"]})
        # Two members of one chapter with the same English would make an unanswerable item: keep both answers.
        by_en = {}
        for d in drill:
            by_en.setdefault((d["en"], d["hint"]), []).append(d)
        for ds in by_en.values():
            if len(ds) > 1:
                alts = [d["answer"] for d in ds]
                for d in ds:
                    d["accept"] = sorted(set(d["accept"] + [a for a in alts if a != d["answer"]]))
        doc = {k: c[k] for k in ("id", "part", "el", "title", "level", "intro")}
        if c.get("sections"):
            doc["sections"] = c["sections"]
        doc["groups"] = c["groups"]
        doc["drill"] = drill
        doc["gloss"] = {**GLOSS, **gloss}
        write(os.path.join(out_dir, c["id"] + ".json"), doc)
        items.append({"id": c["id"], "file": c["id"] + ".json", "part": c["part"], "el": c["el"], "title": c["title"],
                      "level": c["level"], "groups": len(c["groups"]), "words": sum(len(g["members"]) for g in c["groups"])})
    write(os.path.join(out_dir, "index.json"), {
        "el": "Οικογένειες λέξεων", "title": "Word families: roots, prefixes and suffixes",
        "parts": [{"id": k, "el": v[0], "title": v[1]} for k, v in PARTS.items()],
        "items": items, "words": total})
    print(f"families: {len(items)} chapters, {sum(i['groups'] for i in items)} families, {total} words ({inlex} in the lexicon), "
          f"{sum(len(json.load(open(os.path.join(out_dir, i['file'])))['drill']) for i in items)} drill items")

def build_confusables(lex):
    out_dir = os.path.join(APP, "library", "confusables")
    items, n_pairs, n_gaps = [], 0, 0
    chapters = [c for m in (conf_a, conf_b, conf_c) for c in m.CHAPTERS]
    for c in chapters:
        gloss, produce = {}, []
        for p in c["pairs"]:
            for w in p["words"]:
                # Phrases and non-words (e.g. a wrong spelling shown as a warning) are not production items.
                if w["en"].startswith("(") or " " in w["el"] and not w["el"].startswith(("οι ", "τα ", "ο ", "η ", "το ")):
                    continue
                el = w["el"]
                if el.startswith(("οι ", "τα ", "ο ", "η ", "το ")):
                    el = el.split(" ", 1)[1]
                if "/" in el or "(" in el:
                    continue
                if not lex.get(el):
                    gloss[el] = f'{el} — {w["en"]}'
                produce.append({"en": w["en"], "answer": el, "accept": ACCEPT.get(el, []), "set": [x["el"] for x in p["words"]], "lex": bool(lex.get(el))})
            for gp in p["gaps"]:
                assert "___" in gp["s"], gp
                assert gp["a"] not in gp["o"], gp
                n_gaps += 1
        # Same English twice (polysemy cards) → one production item per answer is enough.
        seen, uniq = set(), []
        for x in produce:
            k = (x["en"], x["answer"])
            if k not in seen:
                seen.add(k); uniq.append(x)
        n_pairs += len(c["pairs"])
        doc = {"id": c["id"], "el": c["el"], "title": c["title"], "level": c["level"], "intro": c["intro"],
               "pairs": c["pairs"], "produce": uniq, "gloss": {**GLOSS, **gloss}}
        write(os.path.join(out_dir, c["id"] + ".json"), doc)
        items.append({"id": c["id"], "file": c["id"] + ".json", "el": c["el"], "title": c["title"], "level": c["level"],
                      "pairs": len(c["pairs"])})
    write(os.path.join(out_dir, "index.json"), {
        "el": "Ψευδόφιλοι και παρώνυμα", "title": "False friends and confusables", "items": items})
    print(f"confusables: {len(items)} chapters, {n_pairs} sets, {n_gaps} gap-fills")

if __name__ == "__main__":
    lex = load_lex()
    build_families(lex)
    build_confusables(lex)
