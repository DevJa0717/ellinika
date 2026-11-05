#!/usr/bin/env python3
"""Rank Modern Greek lemmas by corpus frequency and list the most frequent ones the lexicon lacks.
Frequency source: wordfreq 3.x Greek list (Robyn Speer et al., CC BY-SA 4.0; blends Wikipedia, OpenSubtitles,
news, web text and social media). Word forms are lemmatized with the lexicon's own forms-index first, then with
kaikki.org's Wiktionary extract (map from kaikki_map.py). A form's frequency is split among its lemmas.
Usage: python3 -I rank.py MAP.json OUT.json [N_NEW]"""
import json, sys, re, unicodedata, collections, os
import wordfreq
H = os.path.dirname(os.path.abspath(__file__)); L = os.path.join(H, '..', '..')
def strip(s): return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
GREEK = re.compile(r'^[Ͱ-Ͽ]+$')
M = json.load(open(sys.argv[1])); kforms = M['forms']; klem = M['lemmas']
lex = json.load(open(f'{L}/core-1000.json')) + json.load(open(f'{L}/core-3000.json'))
ours = {e['lemma'] for e in lex}; ourlow = {x.lower(): x for x in ours}
fi = json.load(open(f'{L}/forms-index.json'))['forms']
names = {k.lower() for k in json.load(open(f'{L}/names.json'))}
fis = collections.defaultdict(set)
for k, v in fi.items(): fis[strip(k)].update(v)
freq = collections.Counter(); seen = collections.defaultdict(list); unres = collections.Counter()
for w in wordfreq.top_n_list('el', 100000):
    w = re.sub('σ$', 'ς', w)
    if not GREEK.match(w) or len(w) < 2: continue
    f = wordfreq.word_frequency(w, 'el') * 1e6   # per million words
    if w in fi: lems = [('O', x) for x in fi[w]]
    elif w in names: continue
    elif w in kforms:
        ks = kforms[w]
        # a kaikki lemma that is ours (or a form of ours) counts for ours
        lems = []
        for k in ks:
            if k in ours: lems.append(('O', k))
            elif k.lower() in ourlow: lems.append(('O', ourlow[k.lower()]))
            elif k.lower() in fi: lems += [('O', x) for x in fi[k.lower()]]
            else: lems.append(('K', k))
        # a name reading competes with a common-word reading: drop names when any non-name lemma exists
        nn = [x for x in lems if not (x[0] == 'K' and klem.get(x[1], {}).get('name'))]
        lems = nn or lems
    elif strip(w) in fis: lems = [('O', x) for x in fis[strip(w)]]
    else: unres[w] += f; continue
    lems = list(dict.fromkeys(lems))
    for x in lems: freq[x] += f / len(lems); seen[x].append(w)
ranked = sorted(freq.items(), key=lambda kv: -kv[1])
out = []; rank = 0; nours = 0
for (src, lem), f in ranked:
    rank += 1
    if src == 'O': nours += 1; continue
    info = klem.get(lem, {})
    out.append({'lemma': lem, 'rank': rank, 'per_million': round(f, 3), 'forms': seen[(src, lem)][:8],
                'wikt_pos': info.get('pos', []), 'wikt_gloss': info.get('gloss', ''), 'name': info.get('name', False)})
print('lemmas ranked', len(ranked), 'ours ranked', nours, 'of', len(ours), 'new', len(out), 'unresolved forms', len(unres))
json.dump({'new': out, 'unresolved': [{'w': w, 'per_million': round(f, 3)} for w, f in unres.most_common(6000)]},
          open(sys.argv[2], 'w'), ensure_ascii=False, indent=0)
