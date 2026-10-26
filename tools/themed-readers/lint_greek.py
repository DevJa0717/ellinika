#!/usr/bin/env python3
"""Spelling lint for built reader chapters, following the 2026-10-25 audit categories:
final -ν of τη(ν)/στη(ν)/αυτή(ν)/δε(ν)/μη(ν), polysyllables without an accent, accented clitic monosyllables.
Usage: python3 lint_greek.py <dir with chapter json>..."""
import json, os, re, sys, unicodedata
ACC = set("άέήίόύώΆΈΉΊΌΎΏΐΰ")
VOW = "αεηιουωάέήίόύώϊϋΐΰ"
def needs_n(w):
    w = w.lower()
    return w[:1] in VOW or w[:1] in "κπτξψ" or w[:2] in ("γκ", "μπ", "ντ", "τσ", "τζ")
SKIP_NOACC = set("και μου σου του της τους μας σας τον την τη το τα των οι ο η να θα δε δεν μη μην σε στο στη στην στα στον στους στις για με ως απ απο αν αλλ".split())
CLITIC_ACC = {"τού", "μού", "σού", "τό", "νά", "θά", "τά", "τής", "μάς", "σάς", "τούς"}
def texts(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k in ("el", "caption", "q", "a", "word", "greek") and isinstance(v, str): yield v
            elif isinstance(v, (dict, list)): yield from texts(v)
    elif isinstance(o, list):
        for v in o: yield from texts(v)
n = 0
for d in sys.argv[1:]:
    for f in sorted(os.listdir(d)):
        if not f.endswith(".json") or f == "index.json": continue
        ch = json.load(open(os.path.join(d, f)))
        for t in texts(ch):
            t = re.sub(r"[*_]", "", t)
            toks = re.findall(r"[Α-Ωα-ωΆ-Ώά-ώϊϋΐΰ]+", t)
            for i, w in enumerate(toks[:-1]):
                lw = w.lower(); nxt = toks[i + 1]
                if lw in ("τη", "στη") and needs_n(nxt) and not re.search(w + r"\s*[«(]", t):
                    print(f"{f}: {w} {nxt}  (→ {w}ν)"); n += 1
                if lw in ("την", "στην") and not needs_n(nxt) and re.search(w + r" " + nxt, t):
                    print(f"{f}: {w} {nxt}  (→ {w[:-1]}) [style]"); n += 1
            for w in toks:
                lw = w.lower()
                if lw in CLITIC_ACC: print(f"{f}: accented clitic {w}"); n += 1
                vowels = len(re.findall(r"[αεηιουω]+|[άέήίόύώΐΰϊϋ]", unicodedata.normalize("NFC", lw)))
                if vowels >= 2 and not (set(lw) & ACC) and lw not in SKIP_NOACC and not w.isupper():
                    print(f"{f}: no accent {w}"); n += 1
print("issues:", n)
