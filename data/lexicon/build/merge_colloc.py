#!/usr/bin/env python3
"""Merge colloc/colloc_*.out.json (brief_colloc.md) into ../collocations.json, keyed by lemma. Idempotent: an
existing lemma keeps its current entry (the audit edited some). Only lemmas present in the lexicon are added.
Usage: python3 merge_colloc.py [--write]"""
import json, glob, os, sys
B = os.path.dirname(os.path.abspath(__file__)); L = os.path.dirname(B)
C = json.load(open(f'{L}/collocations.json')); E = C['entries']
lex = {e['lemma'] for f in ('core-1000.json', 'core-3000.json') for e in json.load(open(f'{L}/{f}'))}
added = 0; bad = []
for f in sorted(glob.glob(f'{B}/colloc/colloc_*.out.json')):
    for x in json.load(open(f)):
        l = x.get('lemma')
        if not l or l in E: continue
        if l not in lex: bad.append(l); continue
        cs = [c for c in x.get('collocations', []) if isinstance(c, dict) and c.get('el') and c.get('en')]
        if not cs: bad.append(l); continue
        E[l] = {'collocations': cs, 'synonyms': x.get('synonyms', []), 'antonyms': x.get('antonyms', []), 'family': x.get('family', [])}
        added += 1
C['about'] = f'Collocations (el/en), synonyms, antonyms and word family for the {len(E):,} most frequent content words in core-1000/core-3000, keyed by lemma. Written by Claude for production practice.'
print('added', added, 'total', len(E), 'skipped', len(bad), bad[:10])
if '--write' in sys.argv: json.dump(C, open(f'{L}/collocations.json', 'w'), ensure_ascii=False, separators=(',', ':'))
