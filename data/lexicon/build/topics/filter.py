#!/usr/bin/env python3
"""Topic lists t*.out.json -> candidates the lexicon lacks. Gate: lemma must be in el_GR hunspell (or el_50k) and not known
as lemma or form. Writes topics/missing.json [{w, per_million, theme, level, pos}] and prints stats."""
import json, glob, os, re, unicodedata, collections, sys
B = os.path.dirname(os.path.abspath(__file__)); L = os.path.dirname(os.path.dirname(B))
nfc = lambda s: unicodedata.normalize('NFC', s.strip())
def strip(s): return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
lex = []
for f in ('core-1000.json', 'core-3000.json'): lex += json.load(open(f'{L}/{f}'))
known = {strip(e['lemma']) for e in lex}
fi = json.load(open(f'{L}/forms-index.json')); fi = fi.get('forms', fi)
forms = {strip(k) for k in fi}
D = set(); dic = os.environ.get('EL_DIC', '/tmp/claude-0/dict/el_GR.dic')
for l in open(dic, encoding='iso-8859-7'): D.add(nfc(l.split('/')[0]).lower())
pm = {}
for l in open(f'{L}/build/el_50k.txt', encoding='utf-8'):
    p = l.split()
    if len(p) == 2: pm[nfc(p[0]).lower()] = int(p[1])
tot = sum(pm.values()) or 1
THEME = {'t01': 'work', 't02': 'society', 't03': 'environment', 't04': 'technology', 't05': 'health', 't06': 'education',
         't07': 'culture', 't08': 'society', 't09': 'work', 't10': 'society'}
out = {}; st = collections.Counter(); gated = []
for f in sorted(glob.glob(f'{B}/t*.out.json')):
    t = os.path.basename(f)[:3]
    for x in json.load(open(f)):
        w = nfc(x['lemma']); k = strip(w); st['listed'] += 1
        if ' ' in w: st['phrase'] += 1; continue
        if k in known: st['known'] += 1; continue
        if k in forms: st['known-form'] += 1; continue
        if w.lower() not in D and w.lower() not in pm: gated.append(w); st['gate'] += 1; continue
        if k in out: continue
        out[k] = {'w': w, 'per_million': round(pm.get(w.lower(), 0) * 1e6 / tot, 3), 'theme': THEME[t], 'level': x.get('level'), 'pos': x.get('pos')}
for f in sorted(glob.glob(f'{B}/drafts/t*.draft.txt')):
    t = os.path.basename(f)[:3]
    for line in open(f, encoding='utf-8'):
        lv = (re.findall(r'\b(B1|B2|C1)\b', line) or ['C1'])[0]
        for w in re.findall(r'[\u0370-\u03ff\u1f00-\u1fff]+', line):
            w = nfc(w); k = strip(w); st['draft'] += 1
            if k in known or k in forms or k in out: continue
            if w.lower() not in D and w.lower() not in pm: gated.append(w); st['gate'] += 1; continue
            out[k] = {'w': w, 'per_million': round(pm.get(w.lower(), 0) * 1e6 / tot, 3), 'theme': THEME[t], 'level': lv, 'pos': None, 'src': 'draft'}
st['missing'] = len(out)
json.dump(list(out.values()), open(f'{B}/missing.json', 'w'), ensure_ascii=False, indent=1)
json.dump(gated, open(f'{B}/gated.json', 'w'), ensure_ascii=False, indent=1)
print(dict(st))
