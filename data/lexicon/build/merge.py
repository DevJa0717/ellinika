# Rebuild core-1000.json / core-3000.json from the published files plus worker outputs.
# usage: python3 merge.py WORKDIR   (WORKDIR has batches/*.out.json, enrich/*.out.json, freq/lemmas.json)
# Safe to re-run: it starts from the published files each time and skips lemmas already present.
import json, glob, unicodedata, sys, collections
W = sys.argv[1]
L = '/mnt/project-files/data/lexicon/'
CAND = L + 'build/candidates.json'
SRC_NEW = 'OpenSubtitles 2018 frequency list (hermitdave/FrequencyWords, CC BY-SA 4.0); entry written by Claude'
def s(x):
    k = ''.join(c for c in unicodedata.normalize('NFD', x.lower()) if unicodedata.category(c) != 'Mn')
    return k[:-2] + 'ω' if k.endswith('αω') else k  # τραβάω = τραβώ

c1 = json.load(open(L + 'core-1000.json'))
c3 = json.load(open(L + 'core-3000.json'))

# 1. enrichment outputs replace entries by (file, lemma)
fix = {}
for f in sorted(glob.glob(f'{W}/enrich/*.out.json')):
    for e in json.load(open(f)):
        fix[(e.get('_file'), e['lemma'])] = e
def apply(lst, name):
    out = []
    for e in lst:
        n = fix.get((name, e['lemma']))
        if n:
            n = {k: v for k, v in n.items() if k != '_file'}
            for k in ('rank', 'source', 'freq_count'):
                if k in e: n[k] = e[k]
            e = n
        out.append(e)
    return out
c1 = apply(c1, 'core-1000'); c3 = apply(c3, 'core-3000')

# 2. new entries
known = {s(e['lemma']) for e in c1}
seen = {s(e['lemma']): e for e in c3}
cand = {c['i']: c for c in json.load(open(CAND))}
new = 0; dropped = []
for f in sorted(glob.glob(f'{W}/batches/*.out.json')):
    for e in json.load(open(f)):
        k = s(e['lemma']); ids = e.pop('cand_i', []) or []
        cnt = sum(cand[i]['count'] for i in ids if i in cand)
        if k in known: dropped.append(e['lemma']); continue
        if k in seen:
            if seen[k].get('source') == SRC_NEW and seen[k].get('_new'): seen[k]['freq_count'] += cnt
            continue
        e['freq_count'] = cnt; e['source'] = SRC_NEW; e['_new'] = True
        seen[k] = e; c3.append(e); new += 1

# 3. corpus frequency for entries without one (core-1000), from the spaCy-lemmatized list
lemcount = collections.Counter()
for x in json.load(open(f'{W}/freq/lemmas.json')): lemcount[s(x['lemma'])] += x['count']
for e in c1:
    e['freq_count'] = lemcount.get(s(e['lemma']), 0)

# 3b. drop exact duplicates (same accented lemma, -άω = -ώ): core-1000 wins, else the more frequent entry
def k2(x): x = x.lower(); return x[:-2] + 'ώ' if x.endswith('άω') else x
have = {k2(e['lemma']) for e in c1}; keep = {}
for e in sorted(c3, key=lambda e: -e.get('freq_count', 0)):
    k = k2(e['lemma'])
    if k in have: continue
    if k in keep: keep[k]['freq_count'] += e.get('freq_count', 0); continue
    keep[k] = e
print('dedup dropped', len(c3) - len(keep)); c3 = list(keep.values())
# 4. order and rank
c3.sort(key=lambda e: -e.get('freq_count', 0))
for r, e in enumerate(c3, 1001): e['rank'] = r; e.pop('_new', None)
allx = c1 + c3
for r, e in enumerate(sorted(allx, key=lambda e: -e.get('freq_count', 0)), 1): e['freq_rank'] = r

order = ['rank', 'lemma', 'lemma_fix', 'translit', 'pos', 'pos_raw', 'form_key', 'gloss', 'example', 'noun', 'verb', 'adjective',
         'cefr_est', 'themes', 'freq_count', 'freq_rank', 'source', 'needs_review']
def tidy(e):
    if not e.get('needs_review'): e.pop('needs_review', None)
    if not e.get('themes'): e.pop('themes', None)
    return {k: e[k] for k in order if k in e} | {k: v for k, v in e.items() if k not in order}
c1 = [tidy(e) for e in c1]; c3 = [tidy(e) for e in c3]

# 5. checks
bad = []
for e in c1 + c3:
    for k in ('lemma', 'translit', 'pos', 'gloss', 'example', 'cefr_est'):
        if not e.get(k): bad.append((e['lemma'], k))
    if e['pos'] == 'noun' and not (e.get('noun') or {}).get('model'): bad.append((e['lemma'], 'noun.model'))
    if e['pos'] == 'verb' and not (e.get('verb') or {}).get('conj_group'): bad.append((e['lemma'], 'conj_group'))
if '--write' in sys.argv:
    json.dump(c1, open(L + 'core-1000.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(c3, open(L + 'core-3000.json', 'w'), ensure_ascii=False, indent=1)
print('core-1000', len(c1), 'core-3000', len(c3), 'total', len(c1) + len(c3), 'new', new, 'dropped-known', len(dropped))
print('pos', collections.Counter(e['pos'] for e in c1 + c3))
print('cefr', collections.Counter(e.get('cefr_est') for e in c1 + c3))
print('themes', collections.Counter(t for e in c1 + c3 for t in e.get('themes', [])))
print('review', sum(1 for e in c1 + c3 if e.get('needs_review')), 'missing', len(bad), collections.Counter(k for _, k in bad))
