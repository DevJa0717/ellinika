#!/usr/bin/env python3
"""Which of the most common Greek lemmas never appear in any learning content?
Corpus: lessons/, library/ (all shelves), data/c1, data/colloquial (JSON/txt/html, every Greek token).
Lemmas: data/lexicon/core-1000.json + core-3000.json (ranked by the OpenSubtitles 2018 frequency
list, hermitdave/FrequencyWords, CC BY-SA 4.0) plus data/lexicon/build/added-10k.json when present.
Forms -> lemma through data/lexicon/forms-index.json (plus the lemma itself).
Usage: python3 tools/themes/coverage.py [--exclude library/themata] [--out file.json]"""
import json, os, re, sys, glob, unicodedata, collections
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
args = sys.argv[1:]
excl = [args[i+1] for i, a in enumerate(args) if a == "--exclude"]
out = args[args.index("--out")+1] if "--out" in args else None
GR = re.compile(r"[Ͱ-Ͽἀ-῿]+")
def strip(s): return "".join(c for c in unicodedata.normalize("NFD", s) if not unicodedata.combining(c))
lex = []
for f in ("core-1000.json", "core-3000.json"):
    lex += json.load(open(os.path.join(R, "data/lexicon", f), encoding="utf-8"))
add = os.path.join(R, "data/lexicon/build/added-10k.json")
if os.path.exists(add):
    a = json.load(open(add, encoding="utf-8")); a = a if isinstance(a, list) else a.get("words", a.get("entries", []))
    lex += a
forms = json.load(open(os.path.join(R, "data/lexicon/forms-index.json"), encoding="utf-8"))["forms"]
tok = collections.Counter()
files = []
for d in ("lessons", "library", "data/c1", "data/colloquial"):
    for p in glob.glob(os.path.join(R, d, "**", "*"), recursive=True):
        if not os.path.isfile(p) or not p.endswith((".json", ".txt", ".html", ".md")): continue
        rel = os.path.relpath(p, R)
        if any(rel.startswith(e) for e in excl) or "/src/" in rel and rel.endswith(".py"): continue
        files.append(rel)
        for t in GR.findall(open(p, encoding="utf-8", errors="ignore").read()):
            tok[t.lower()] += 1
seen = collections.Counter()
for t, n in tok.items():
    for l in forms.get(t, [t]): seen[l] += n
    if t not in forms:
        for l in forms.get(strip(t), []): seen[l] += n
lexs = {}
for e in lex:
    l = e.get("lemma"); r = e.get("freq_rank") or e.get("rank") or 10**6
    if l and (l not in lexs or r < lexs[l]["r"]): lexs[l] = {"r": r, "pos": e.get("pos"), "gloss": e.get("gloss", "")}
miss = sorted(((v["r"], l, v["pos"], v["gloss"]) for l, v in lexs.items() if seen[l] == 0))
rare = sorted(((v["r"], l, v["pos"], v["gloss"], seen[l]) for l, v in lexs.items() if 0 < seen[l] < 3))
print(f"{len(files)} files, {len(tok)} distinct tokens; {len(lexs)} lemmas; never used: {len(miss)}; used once or twice: {len(rare)}")
for band in (1000, 3000, 5000, 8000, 10000):
    print(f"  top {band}: missing {sum(1 for m in miss if m[0] <= band)}")
if out:
    json.dump({"missing": [dict(rank=r, lemma=l, pos=p, gloss=g) for r, l, p, g in miss],
               "rare": [dict(rank=r, lemma=l, pos=p, gloss=g, uses=n) for r, l, p, g, n in rare]},
              open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
