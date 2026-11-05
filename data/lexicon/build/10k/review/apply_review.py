#!/usr/bin/env python3
"""Fold review/*.out.json (brief_review.md) into ../fixes10k.json. Then rebuild: restore the pre-10k lexicon files,
run merge10k.py and finalize.py --write (fixes, incl. DROP, apply at merge). Usage: python3 apply_review.py"""
import json, glob, os, collections
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(H)
F = json.load(open(f'{P}/fixes10k.json')); n = collections.Counter()
for f in sorted(glob.glob(f'{H}/r*.out.json')):
    for x in json.load(open(f)):
        l = x.get('lemma'); s = x.get('set') or {}
        if not l or not s: continue
        d = F.setdefault(l, {})
        for k, v in s.items():
            if k == 'DROP':
                if v: d['DROP'] = True; n['drop'] += 1
                continue
            d[k] = v; n[k.split('.')[0]] += 1
json.dump(F, open(f'{P}/fixes10k.json', 'w'), ensure_ascii=False, indent=1)
print(dict(n))
