#!/usr/bin/env python3
"""Cross-check the verb tables of the grammar outline against Holton et al.'s table of irregular verbs
(data/grammar/verbs-holton.json, section 6.25): every table row whose first cell is a present form found in
Holton's list must give the same active aorist, passive aorist or -μένος participle where the outline gives one.
Usage: python3 tools/theoria/crosscheck.py"""
import glob, json, os, re, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); APP = os.path.join(HERE, "../..")
V = json.load(open(os.path.join(APP, "data/grammar/verbs-holton.json"), encoding="utf-8"))["irregular_verbs_6.25"]["verbs"]
H = {}
for v in V:
    for p in re.split(r"\s*[/,]\s*|\s+\(", v["present"]):
        p = p.strip(" )")
        if p: H[p] = v
forms = lambda s: {x.strip(" *") for x in re.split(r"\s*/\s*|\s*,\s*", s or "") if x.strip()}
checked = bad = 0
for f in sorted(glob.glob(os.path.join(APP, "library/theoria/src/[0-9][0-9]-*.txt"))):
    head = None
    for n, l in enumerate(open(f, encoding="utf-8"), 1):
        if not l.startswith("|"): head = None; continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if head is None: head = [c.lower() for c in cells]; continue
        if set("".join(cells)) <= set("-: "): continue
        for i0 in range(len(cells)):
            pres = cells[i0]
            if pres not in H or i0 + 1 >= len(cells): continue
            v = H[pres]
            for j in range(i0 + 1, min(i0 + 3, len(cells))):
                if j >= len(head) or not re.search(r"aorist|participle|μένος", head[j]): continue
                c = forms(cells[j])
                keys = ("passive_perfect_participle",) if re.search(r"participle|μένος", head[j]) else \
                    ("passive_simple_past",) if "passive" in head[j] else ("active_simple_past", "passive_simple_past") if pres.endswith("μαι") else ("active_simple_past",)
                for key in keys:
                    ref = forms(v.get(key))
                    if not ref or not c: continue
                    same_kind = any(x[-2:] == y[-2:] or x[-4:] == y[-4:] for x in c for y in ref)
                    if not same_kind: continue
                    checked += 1
                    if not (c & ref):
                        bad += 1
                        print(f"{os.path.basename(f)}:{n}: {pres} → outline {sorted(c)} vs Holton {key} {sorted(ref)}")
print(f"{checked} forms compared with Holton §6.25, {bad} differences")
