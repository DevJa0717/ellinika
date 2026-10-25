# Apply the forms/consistency pass and build forms-index.json.
# usage: python3 apply_forms.py WORKDIR [--write]   (WORKDIR has forms/*.out.json)
import json, glob, sys, collections, unicodedata
W = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else '/mnt/project-files/data/lexicon/build'
L = '/mnt/project-files/data/lexicon/'
KEEP = {('τηλεφωνώ', 'verb.conj_group'): 'B1'}  # settled by hand where two passes disagreed
def strip(x): return ''.join(c for c in unicodedata.normalize('NFD', x.lower()) if unicodedata.category(c) != 'Mn')

files = {f: json.load(open(L + f)) for f in ('core-1000.json', 'core-3000.json')}
by = collections.defaultdict(list)
for f, lst in files.items():
    for e in lst:
        by[e['lemma']].append(e)
        if e.get('lemma_was'): by[e['lemma_was']].append(e)

forms = collections.defaultdict(set); nfix = 0; missing = []
for f in sorted(glob.glob(f'{W}/forms/*.out.json')):
    for x in json.load(open(f)):
        es = by.get(x['lemma'])
        if not es: missing.append(x['lemma']); continue
        forms[es[0]['lemma']].update(w.strip() for w in x.get('forms', []) if isinstance(w, str) and w.strip())
        for path, val in (x.get('fix') or {}).items():
            if (x['lemma'], path) in KEEP: val = KEEP[(x['lemma'], path)]
            for e in es:
                if path == 'lemma_fix': e['lemma_fix'] = val; nfix += 1; continue
                if path == 'needs_review': e['needs_review'] = val; continue
                head, _, key = path.partition('.')
                if key and isinstance(e.get(head), dict): e[head][key] = val; nfix += 1
                elif key and head in ('noun', 'verb', 'adjective') and e['pos'] in (head, 'other', 'pronoun', 'numeral'):
                    e[head] = {key: val}; nfix += 1
for (lem, path), val in KEEP.items():
    for e in by.get(lem, []):
        h, _, k = path.partition('.'); e.get(h, {})[k] = val

# lemma_fix: rename; if the right lemma already exists, fold this entry into it
renamed = []; dropped = []
all_lemmas = {e['lemma'] for lst in files.values() for e in lst}
for f, lst in files.items():
    out = []
    for e in lst:
        fx = e.pop('lemma_fix', None)
        if fx and fx != e['lemma']:
            old = e['lemma']
            forms[fx] |= forms.pop(old, set()) | {old}
            if fx in all_lemmas:
                tgt = next(t for l2 in files.values() for t in l2 if t['lemma'] == fx)
                tgt['freq_count'] = tgt.get('freq_count', 0) + e.get('freq_count', 0); dropped.append(f'{old}->{fx}'); continue
            e['lemma'] = fx; e['lemma_was'] = old; all_lemmas.add(fx); renamed.append(f'{old}->{fx}')
        if not e.get('needs_review'): e.pop('needs_review', None)
        out.append(e)
    files[f] = out

# index: written form -> lemmas (lowercase keys keep accents; the app can also strip accents for a fuzzy match)
idx = collections.defaultdict(set)
for f, lst in files.items():
    for e in lst:
        lem = e['lemma']
        for w in forms.get(lem, set()) | {lem}:
            for part in [w] + (w.split('/') if '/' in w else []):
                part = part.strip().lower()
                if part: idx[part].add(lem)
index = {k: sorted(v) for k, v in sorted(idx.items())}
nolist = [e['lemma'] for lst in files.values() for e in lst if e['lemma'] not in forms]
print('fixes', nfix, 'renamed', len(renamed), renamed[:20], 'folded', dropped, 'unknown lemmas in forms', missing[:10])
print('entries', sum(map(len, files.values())), 'index forms', len(index), 'ambiguous', sum(1 for v in index.values() if len(v) > 1), 'entries without forms', len(nolist), nolist[:10])
print('review', [e['lemma'] for lst in files.values() for e in lst if e.get('needs_review')])
if '--write' in sys.argv:
    for f, lst in files.items(): json.dump(lst, open(L + f, 'w'), ensure_ascii=False, indent=1)
    json.dump({'about': 'Inflected form (lowercase, accented) -> lemma(s) in core-1000.json / core-3000.json, for tap-to-look-up. Forms written by Claude per entry; strip accents on both sides for a fuzzy fallback.',
               'forms': index}, open(L + 'forms-index.json', 'w'), ensure_ascii=False, separators=(',', ':'))
