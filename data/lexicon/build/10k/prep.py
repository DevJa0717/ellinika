#!/usr/bin/env python3
"""Split rank.json into agent batches. Usage: python3 -I prep.py MAP.json RANK.json WORKDIR N_CAND BATCH"""
import json, sys, re, collections, os
M = json.load(open(sys.argv[1])); R = json.load(open(sys.argv[2])); W = sys.argv[3]; N = int(sys.argv[4]); B = int(sys.argv[5])
inv = collections.defaultdict(set)
for f, ls in M['forms'].items():
    for l in ls: inv[l].add(f)
cand = [x for x in R['new'] if not x['name'] and not re.fullmatch(r'[Α-ΩΆ-Ώ]+', x['lemma'])][:N]
cut = cand[-1]['per_million']
unres = [x for x in R['unresolved'] if x['per_million'] >= cut and len(x['w']) > 2]
items = []
for x in cand:
    items.append({'lemma': x['lemma'], 'rank': x['rank'], 'corpus_forms': x['forms'], 'wikt_pos': x['wikt_pos'],
                  'wikt_gloss': x['wikt_gloss'][:120], 'wikt_forms': len(inv.get(x['lemma'], ()))})
for x in unres: items.append({'w': x['w'], 'per_million': x['per_million'], 'unresolved': True})
os.makedirs(f'{W}/in', exist_ok=True)
for i in range(0, len(items), B):
    json.dump(items[i:i + B], open(f'{W}/in/b{i // B:02d}.in.json', 'w'), ensure_ascii=False, indent=0)
json.dump({l: sorted(inv.get(l, ())) for l in [x['lemma'] for x in cand]}, open(f'{W}/wikt_forms.json', 'w'), ensure_ascii=False)
print('candidates', len(cand), 'cut per_million', cut, 'last rank', cand[-1]['rank'], 'unresolved', len(unres), 'batches', -(-len(items) // B))
