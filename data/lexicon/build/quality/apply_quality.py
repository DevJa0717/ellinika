#!/usr/bin/env python3
"""Apply quality/q*.out.json: gloss/example -> build/spotcheck7.out.json (finalize.py applies it on every run, so restores
and re-merges keep it); collocations/synonyms/antonyms/family -> collocations.json directly.
Usage: python3 apply_quality.py [--write], then python3 ../finalize.py --write. Idempotent (sets values)."""
import json, glob, os, sys
B = os.path.dirname(os.path.abspath(__file__)); L = os.path.dirname(os.path.dirname(B))
cores = {f: json.load(open(f'{L}/{f}')) for f in ('core-1000.json', 'core-3000.json')}
idx = {e['lemma']: e for d in cores.values() for e in d}
C = json.load(open(f'{L}/collocations.json')); spot = []; n = {'gloss': 0, 'example': 0, 'colloc': 0, 'missing': 0}
for f in sorted(glob.glob(f'{B}/q*.out.json')):
    for x in json.load(open(f)):
        e = idx.get(x.get('lemma'))
        if not e: n['missing'] += 1; continue
        st = {}
        if x.get('gloss'): st['gloss'] = x['gloss']; n['gloss'] += 1
        ex = x.get('example')
        if isinstance(ex, dict) and ex.get('el') and ex.get('en'): st['example'] = {'el': ex['el'], 'en': ex['en']}; n['example'] += 1
        if st: spot.append({'lemma': x['lemma'], 'set': st, 'why': 'quality pass: ' + str(x.get('why', ''))})
        ce = C['entries'].get(x['lemma'])
        if ce is not None:
            for k in ('collocations', 'synonyms', 'antonyms', 'family'):
                if isinstance(x.get(k), list) and (k != 'collocations' or x[k]): ce[k] = x[k]; n['colloc'] += 1
print(n)
if '--write' in sys.argv:
    json.dump(spot, open(f'{L}/build/spotcheck7.out.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(C, open(f'{L}/collocations.json', 'w'), ensure_ascii=False, separators=(',', ':'))
