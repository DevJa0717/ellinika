#!/usr/bin/env python3
"""Spelling and form checks for the history reader: every Greek word in app/library/istoria/*.json against the
LibreOffice el_GR word list plus the app lexicon's forms index; final-ν rule after τη(ν)/στη(ν)/δε(ν)/μη(ν); mixed scripts."""
import json, os, re, sys, glob, unicodedata
DIC = sys.argv[1] if len(sys.argv) > 1 else "/tmp/claude-0/-home-user-ellinika/4aae0be0-d441-59f8-9a70-1458d683e840/scratchpad/dict/el_GR.dic"
words = set()
for line in open(DIC, encoding="iso-8859-7").read().split("\n")[1:]:
    w = line.split("/")[0].strip()
    if w: words.add(w)
fi = json.load(open("/mnt/project-files/data/lexicon/forms-index.json"))
fi = fi.get("forms", fi)
low = {w.lower() for w in words} | {k.lower() for k in fi}
names = json.load(open("/mnt/project-files/data/lexicon/names.json")) if os.path.exists("/mnt/project-files/data/lexicon/names.json") else {}
low |= {k.lower() for k in names}
ok_extra = set(open(os.path.join(os.path.dirname(__file__), "src/ok_words.txt")).read().split()) if os.path.exists(os.path.join(os.path.dirname(__file__), "src/ok_words.txt")) else set()
GR = re.compile(r"[Ͱ-Ͽἀ-῿]+")
def strings(o, key=None):
    if isinstance(o, str):
        if key not in ("en", "def_en", "title", "summary_en", "why", "text", "url", "file", "credit", "license", "source", "caption_en", "id", "theme", "part", "level", "dates", "image"): yield o
    elif isinstance(o, list):
        for x in o: yield from strings(x, key)
    elif isinstance(o, dict):
        for k, v in o.items():
            if k != "gloss": yield from strings(v, k)
files = sorted(glob.glob("/mnt/project-files/app/library/istoria/e*.json")) if len(sys.argv) < 3 else sys.argv[2:]
bad_total = 0
for f in files:
    ch = json.load(open(f)); bad = {}
    for s in strings(ch):
        if re.search(r"[A-Za-z][Ͱ-Ͽ]|[Ͱ-Ͽ][A-Za-z]", s): bad.setdefault("MIXED", set()).add(s[:40])
        for m in re.finditer(r"\b(σ?την|σ?τη|δεν|δε|μην|μη)\s+(\w)", s):
            art, nxt = m.group(1), m.group(2).lower()
            keep = nxt in "αάεέηήιίοόυύωώκπτξψ" or s[m.end(2)-1:m.end(2)+1].lower() in ("μπ", "ντ", "γκ", "τσ", "τζ")
            if art.endswith("ν") != keep and art in ("την", "στην", "τη", "στη"): bad.setdefault("FINAL-N", set()).add(s[m.start():m.end()+8])
        for w in GR.findall(s):
            if len(w) < 2: continue
            if w.lower() in low or w in ok_extra or w.lower() in ok_extra: continue
            bad.setdefault("UNKNOWN", set()).add(w)
    if bad:
        bad_total += sum(map(len, bad.values()))
        print(os.path.basename(f))
        for k, v in bad.items(): print(" ", k + ":", " · ".join(sorted(v)))
print("issues:", bad_total)
