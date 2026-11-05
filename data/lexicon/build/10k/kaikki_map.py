#!/usr/bin/env python3
"""Form -> lemma map from kaikki.org's Greek Wiktionary extract (CC BY-SA), for ranking lemmas by frequency.
Usage: python3 -I kaikki_map.py /path/kaikki.org-dictionary-Greek.jsonl OUT.json
OUT = {"lemmas": {lemma: {pos:[..], gloss}}, "forms": {form: [lemma,...]}}"""
import json, sys, collections, re
GREEK = re.compile(r'^[Ͱ-Ͽἀ-῿]+$')
SKIPTAG = {'romanization', 'table-tags', 'inflection-template', 'class'}
lemmas = {}; forms = collections.defaultdict(set)
for line in open(sys.argv[1], encoding='utf-8'):
    d = json.loads(line); w = d.get('word', ''); pos = d.get('pos')
    if not GREEK.match(w) or pos in ('character', 'symbol', 'abbrev', 'suffix', 'prefix', 'affix', 'punct'): continue
    senses = d.get('senses', [])
    fo = [f.get('word') for s in senses for f in (s.get('form_of') or []) + (s.get('alt_of') or []) if f.get('word')]
    allform = all(s.get('form_of') or 'form-of' in (s.get('tags') or []) for s in senses) and fo
    if allform:
        for l in fo:
            if GREEK.match(l): forms[w.lower()].add(l)
        continue
    g = next((s['glosses'][0] for s in senses if s.get('glosses')), '')
    L = lemmas.setdefault(w, {'pos': [], 'gloss': g, 'name': False})
    if pos not in L['pos']: L['pos'].append(pos)
    if pos == 'name': L['name'] = True
    forms[w.lower()].add(w)
    for f in d.get('forms', []):
        t = set(f.get('tags', []))
        if t & SKIPTAG or 'alternative' in t: continue
        x = f.get('form', '').strip()
        if GREEK.match(x): forms[x.lower()].add(w)
json.dump({'lemmas': lemmas, 'forms': {k: sorted(v) for k, v in forms.items()}}, open(sys.argv[2], 'w'), ensure_ascii=False)
print(len(lemmas), 'lemmas', len(forms), 'forms')
