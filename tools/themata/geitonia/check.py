#!/usr/bin/env python3
"""Check a geitonia part: which assigned target lemmas appear in its Greek text (any inflected form, via forms-index).
Usage: python3 tools/themata/geitonia/check.py part3   (prints missing targets and structural problems)"""
import json, os, re, sys, importlib.util, unicodedata
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, "../../.."))
part = sys.argv[1]
spec = importlib.util.spec_from_file_location("p", os.path.join(H, part + ".py")); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
forms = json.load(open(os.path.join(R, "data/lexicon/forms-index.json"), encoding="utf-8"))["forms"]
def strip(s): return "".join(ch for ch in unicodedata.normalize("NFD", s) if not unicodedata.combining(ch))
txt = []
for c in m.CHAPTERS:
    for k in ("id", "el", "title", "level", "summary_en", "sections", "grammar", "terms", "questions", "vocab"):
        assert k in c, (c.get("id"), "missing key", k)
    for s in c["sections"]:
        for p in s["paras"]:
            assert len(p) == 3 and isinstance(p[2], list), (c["id"], "para must be (el, en, [])")
            txt.append(p[0])
    for q in c["questions"]:
        assert q[2] in q[1], (c["id"], "answer not in options", q[0])
seen = set()
for t in re.findall(r"[Ͱ-Ͽἀ-῿]+", " ".join(txt)):
    t = t.lower(); seen.add(t)
    for l in forms.get(t, []) + forms.get(strip(t), []): seen.add(l)
tg = json.load(open(os.path.join(H, "targets.json"), encoding="utf-8"))[part]
low = " ".join(txt).lower()
miss = [w["lemma"] for w in tg if w["lemma"] not in seen and w["lemma"].lower() not in seen and not ((" " in w["lemma"] or "-" in w["lemma"]) and w["lemma"].lower() in low)]
words = len(" ".join(txt).split())
print(f"{part}: {len(m.CHAPTERS)} chapters, {words} Greek words in story text; targets used {len(tg)-len(miss)}/{len(tg)}")
if miss: print("MISSING:", ", ".join(miss))
