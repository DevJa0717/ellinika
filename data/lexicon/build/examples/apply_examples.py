#!/usr/bin/env python3
"""Collect examples/x*.out.json into build/spotcheck9.out.json (finalize.py applies it on every run) and add any
new gen_sg/aorist forms to forms-index.json. Usage: python3 apply_examples.py [--write]; then finalize.py --write."""
import json, glob, os, sys
B = os.path.dirname(os.path.abspath(__file__)); L = os.path.dirname(os.path.dirname(B))
lem = {e['lemma'] for f in ('core-1000.json', 'core-3000.json') for e in json.load(open(f'{L}/{f}'))}
spot = []; n = {'example': 0, 'grammar': 0, 'missing': 0, 'forms_added': 0}
FI = json.load(open(f'{L}/forms-index.json')); fi = FI['forms']
for f in sorted(glob.glob(f'{B}/x*.out.json')):
    for x in json.load(open(f)):
        if x.get('lemma') not in lem or not isinstance(x.get('set'), dict): n['missing'] += 1; continue
        st = {k: v for k, v in x['set'].items() if k == 'example' and isinstance(v, dict) and v.get('el') and v.get('en') or k != 'example' and v not in (None, '')}
        if not st: continue
        n['example'] += 'example' in st; n['grammar'] += any(k != 'example' for k in st)
        spot.append({'lemma': x['lemma'], 'set': st, 'why': 'example/grammar pass: ' + str(x.get('why', ''))})
        for k in ('noun.gen_sg', 'verb.aorist_1sg', 'verb.aorist_passive_1sg', 'verb.participle', 'adjective.f', 'adjective.n'):
            v = st.get(k)
            if isinstance(v, str) and ' ' not in v.strip():
                key = v.strip().lower()
                cur = fi.get(key)
                if cur is None: fi[key] = [x['lemma']]; n['forms_added'] += 1
                elif isinstance(cur, list) and x['lemma'] not in cur: cur.append(x['lemma']); n['forms_added'] += 1
print(n)
if '--write' in sys.argv:
    json.dump(spot, open(f'{L}/build/spotcheck9.out.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(FI, open(f'{L}/forms-index.json', 'w'), ensure_ascii=False, separators=(',', ':'))
