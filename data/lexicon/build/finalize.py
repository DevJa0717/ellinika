# Run after apply_forms.py. Adds lesson-vocabulary results (build/misses/*.out.json), writes names.json,
# extends forms-index.json, and recomputes freq_count / freq_rank from the corpus counts of each word's forms.
# usage: python3 finalize.py [--write]      Idempotent: re-running adds nothing twice.
import json, glob, sys, collections, unicodedata
import os
B = os.path.dirname(os.path.abspath(__file__)) + '/'; L = os.path.dirname(B.rstrip('/')) + '/'
SRC = 'Lesson vocabulary (word found in the app lessons); entry written by Claude'
def strip(x):  # same-word key: keeps accents (θόλος ≠ θολός, πότε ≠ ποτέ), folds -άω into -ώ (γαμάω = γαμώ)
    k = unicodedata.normalize('NFC', x.lower())
    return k[:-2] + 'ώ' if k.endswith('άω') else k

c1 = json.load(open(L + 'core-1000.json')); c3 = json.load(open(L + 'core-3000.json'))
idx = collections.defaultdict(set, {k: set(v) for k, v in json.load(open(L + 'forms-index.json'))['forms'].items()})
lemmas = {e['lemma'] for e in c1 + c3}; skeys = {strip(e['lemma']): e['lemma'] for e in c1 + c3}
nokey = {''.join(c for c in unicodedata.normalize('NFD', e['lemma'].lower()) if unicodedata.category(c) != 'Mn'): e['lemma'] for e in c1 + c3}
ALIAS = {'αδελφός': 'αδερφός'}
names = {}; added = 0; formmaps = 0; unresolved = []; types = collections.Counter()
for f in sorted(glob.glob(B + 'misses/*.out.json')):
    for x in json.load(open(f)):
        t = x.get('type'); types[t] += 1; w = x['w'].lower()
        if t == 'name' and x.get('lemma'):
            names[x['lemma']] = f"{x['lemma']}|{x.get('gloss', '')}"
            if w != x['lemma'].lower(): names[x['w']] = f"{x['lemma']}|{x.get('gloss', '')}"
        elif t == 'new' and x.get('entry'):
            e = x['entry']; e.pop('cand_i', None)
            if e['lemma'] in ALIAS: skeys[strip(e['lemma'])] = ALIAS[e['lemma']]  # spelling variant of an existing headword
            bare = ''.join(c for c in unicodedata.normalize('NFD', e['lemma'].lower()) if unicodedata.category(c) != 'Mn')
            if bare == e['lemma'].lower() and bare in nokey: skeys[strip(e['lemma'])] = nokey[bare]  # unaccented spelling of a known word (ρισπεκτ)
            if e['lemma'] not in lemmas and strip(e['lemma']) not in skeys:
                e['source'] = SRC; c3.append(e); lemmas.add(e['lemma']); skeys[strip(e['lemma'])] = e['lemma']; added += 1
            tgt = e['lemma'] if e['lemma'] in lemmas else skeys[strip(e['lemma'])]  # same word already entered (γαμώ = γαμάω)
            for v in set(x.get('forms') or []) | {w, e['lemma']}: idx[v.strip().lower()].add(tgt)
        elif t == 'form' and x.get('lemma'):
            if x['lemma'] in lemmas: idx[w].add(x['lemma']); formmaps += 1
            elif strip(x['lemma']) in skeys: idx[w].add(skeys[strip(x['lemma'])]); formmaps += 1
            else: unresolved.append((x['w'], x['lemma']))
# 'form' items whose lemma only arrived as a 'new' entry in a later chunk
for w, lem in list(unresolved):
    if lem in lemmas: idx[w.lower()].add(lem); unresolved.remove((w, lem)); formmaps += 1

# 10k extension (build/10k/entries.json from merge10k.py): append new entries, index their forms, add names
if os.path.exists(B + '10k/entries.json'):
    n10 = 0
    for r in json.load(open(B + '10k/entries.json')):
        e = r['entry']
        if e['lemma'] not in lemmas and strip(e['lemma']) not in skeys:
            c3.append(e); lemmas.add(e['lemma']); skeys[strip(e['lemma'])] = e['lemma']; n10 += 1
        tgt = e['lemma'] if e['lemma'] in lemmas else skeys[strip(e['lemma'])]
        for v in r['forms']: idx[v.strip().lower()].add(tgt)
    for k, v in json.load(open(B + '10k/names_add.json')).items(): names.setdefault(k, v)
    for kf in ('10k/known_forms_add.json', '10k/known_forms_manual.json'):
      if os.path.exists(B + kf):
        for lem, fs in json.load(open(B + kf)).items():
            if lem in lemmas:
                for v in fs: idx[v.strip().lower()].add(lem)
    print('10k entries appended', n10)
# spot-check corrections (dotted paths); model changes to null are skipped ("irregular" is a valid model)
import os
byl = {e['lemma']: e for e in c1 + c3}
for sf in sorted(glob.glob(B + 'spotcheck*.out.json')):
    for x in json.load(open(sf)):
        e = byl.get(x['lemma'])
        if not e: continue
        for path, val in x.get('set', {}).items():
            if path.endswith('.model') and val is None or path in ('needs_review', 'noun.declension') and x.get('set', {}).get('noun.model', 1) is None: continue
            h, _, k = path.partition('.')
            if not k: e[h] = val
            elif isinstance(e.get(h), dict): e[h][k] = val
# form_key labels (audit 2026-10-25 convention): adjectives "f: X, n: Y" unless two-termination (m = f) "m/f: X, n: Y";
# nouns with no genitive singular in use show "Gen: —"
import re as _re
for e in c1 + c3:
    a = e.get('adjective') or {}
    if e['pos'] == 'adjective' and a.get('f') and a.get('n') and a.get('model') != 'indecl' and _re.match(r'(m/f|f): ', e.get('form_key', '')):
        e['form_key'] = f"{'m/f' if a.get('m') == a['f'] else 'f'}: {a['f']}, n: {a['n']}"
    if e.get('form_key', '').startswith('Gen: None'): e['form_key'] = 'Gen: —' + e['form_key'][9:]
# transliteration from the rule set (loanwords marked indecl keep their spelled-out form)
sys.path.insert(0, B); from translit import translit
for e in c1 + c3:
    if (e.get('noun') or {}).get('model') == 'indecl' or (e.get('adjective') or {}).get('model') == 'indecl': continue
    if all(ch.isalpha() or ch == ' ' for ch in e['lemma']): e['translit'] = translit(e['lemma'])
# corpus frequency: each form's count is shared among the lemmas it can belong to
cnt = {}
for line in open(B + 'el_50k.txt', encoding='utf-8'):
    w, c = line.split(); cnt[w] = cnt.get(w, 0) + int(c)
freq = collections.Counter()
for form, lems in idx.items():
    c = cnt.get(form, 0)
    if c:
        for l in lems: freq[l] += c / len(lems)
for e in c1 + c3:
    f = round(freq.get(e['lemma'], 0))
    if f or not e.get('freq_count'): e['freq_count'] = f
c3.sort(key=lambda e: -e.get('freq_count', 0))
for r, e in enumerate(c3, 1001): e['rank'] = r
for r, e in enumerate(sorted(c1 + c3, key=lambda e: -e.get('freq_count', 0)), 1): e['freq_rank'] = r

print('types', dict(types), 'new entries', added, 'form mappings', formmaps, 'names', len(names), 'unresolved', unresolved[:15])
print('core-1000', len(c1), 'core-3000', len(c3), 'total', len(c1) + len(c3), 'index forms', len(idx), 'zero-freq', sum(1 for e in c1 + c3 if not e.get('freq_count')))
if '--write' in sys.argv:
    json.dump(c1, open(L + 'core-1000.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(c3, open(L + 'core-3000.json', 'w'), ensure_ascii=False, indent=1)
    about = json.load(open(L + 'forms-index.json'))['about']
    json.dump({'about': about, 'forms': {k: sorted(v) for k, v in sorted(idx.items())}}, open(L + 'forms-index.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    json.dump(dict(sorted(names.items())), open(L + 'names.json', 'w'), ensure_ascii=False, indent=0)
