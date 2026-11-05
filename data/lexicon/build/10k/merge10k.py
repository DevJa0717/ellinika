#!/usr/bin/env python3
"""Collect the 10k-extension entries (out/*.out.json, written per brief_10k.md) into entries.json + names_add.json,
which finalize.py then merges into core-3000.json, forms-index.json and names.json. Also writes ../added-10k.json
and a cross-check report (check10k.txt): principal parts that Wiktionary's inflection table does not contain.
Usage: python3 -I merge10k.py [MAP.json]   (MAP from kaikki_map.py; without it, wikt_forms.json is used as cached)"""
import json, glob, os, sys, re, unicodedata, collections
H = os.path.dirname(os.path.abspath(__file__)); L = os.path.join(H, '..', '..')
GREEK = re.compile(r'^[Ͱ-Ͽ]+$')
def nfc(s): return unicodedata.normalize('NFC', s)
def skey(x):  # finalize.py's same-word key: keeps accents, folds -άω into -ώ
    k = nfc(x.lower()); return k[:-2] + 'ώ' if k.endswith('άω') else k
def bare(s): return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')

lex = json.load(open(f'{L}/core-1000.json')) + json.load(open(f'{L}/core-3000.json'))
SRC10 = 'wordfreq Greek frequency list (CC BY-SA 4.0) + Wiktionary inflection tables (kaikki.org, CC BY-SA); entry written by Claude'
prev10 = {e['lemma'] for e in lex if e.get('source') == SRC10}       # entries an earlier finalize run already merged
known = {skey(e['lemma']) for e in lex if e['lemma'] not in prev10}
fi = json.load(open(f'{L}/forms-index.json'))['forms']
wf = json.load(open(f'{H}/wikt_forms.json')) if os.path.exists(f'{H}/wikt_forms.json') else {}
M = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else None
if M:
    inv = collections.defaultdict(set)
    for f, ls in M['forms'].items():
        for l in ls: inv[l].add(f)
def wikt(lem):
    if lem not in wf and M: wf[lem] = sorted(inv.get(lem, ()))
    return wf.get(lem, [])

POS = {'noun', 'verb', 'adjective', 'adverb', 'pronoun', 'preposition', 'conjunction', 'particle', 'numeral', 'article', 'other'}
entries = {}; skips = collections.Counter(); problems = []; order = []
for fo in sorted(glob.glob(f'{H}/out/*.out.json')):
    fin = fo.replace('/out/', '/in/').replace('.out.', '.in.')
    cin = json.load(open(fin)); cout = json.load(open(fo))
    for x in cout:
        i = x.get('i'); c = cin[i] if isinstance(i, int) and i < len(cin) else {}
        if x.get('skip') or not x.get('lemma'):
            skips[re.sub(r'\s.*', '', str(x.get('skip', '?')).lower())[:20]] += 1; continue
        e = {k: v for k, v in x.items() if k not in ('i', 'forms', 'cand_i')}
        e['lemma'] = nfc(e['lemma'].strip())
        if e.get('pos') not in POS: problems.append(f"{e['lemma']}: pos {e.get('pos')}"); continue
        if not e.get('gloss') or not (e.get('example') or {}).get('el'): problems.append(f"{e['lemma']}: missing gloss/example"); continue
        k = skey(e['lemma'])
        if k in known: skips['known'] += 1; continue
        forms = {nfc(f.strip().lower()) for f in (x.get('forms') or []) if isinstance(f, str) and f.strip() and ' ' not in f.strip()}
        src = 'agent' if forms else 'wikt'
        forms |= {f for f in wikt(e['lemma']) if ' ' not in f}
        if c.get('lemma') and c['lemma'] != e['lemma'] and not x.get('forms'):
            forms |= set(c.get('corpus_forms', []))            # agent renamed the lemma without giving forms
        forms.add(e['lemma'].lower())
        rank = c.get('rank', 99999)
        if k in entries:                                       # same lemma from two batches: keep the better-ranked
            old = entries[k]; old['_forms'] |= forms; old['_rank'] = min(old['_rank'], rank); skips['dup'] += 1; continue
        e['_forms'] = forms; e['_rank'] = rank; e['_fsrc'] = src
        entries[k] = e; order.append(k)

# unresolved-form pass (out_unres/*.out.json per brief_unres.md): new entries, extra forms, names and abbreviations
R = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else (json.load(open(f'{H}/rank_lite.json')) if os.path.exists(f'{H}/rank_lite.json') else None)
pm2rank = [(x['per_million'], x['rank']) for x in (R or {}).get('new', [])]
def rank_of(pm): return next((r for p_, r in pm2rank if p_ <= pm), 99999)
extra_forms = collections.defaultdict(set); unames = {}
lexlem = {e['lemma'] for e in lex}
for fo in sorted(glob.glob(f'{H}/out_unres/*.out.json')):
    cin = json.load(open(fo.replace('/out_unres/', '/in_unres/').replace('.out.', '.in.')))
    pmw = {x['w']: x['per_million'] for x in cin}
    for x in json.load(open(fo)):
        t = x.get('type'); w = nfc(str(x.get('w', '')).lower())
        if t == 'new' and x.get('entry', {}).get('lemma'):
            e = {k: v for k, v in x['entry'].items() if k not in ('i', 'forms', 'cand_i')}; e['lemma'] = nfc(e['lemma'].strip())
            if e.get('pos') not in POS or not e.get('gloss') or not (e.get('example') or {}).get('el'): problems.append(f"{e['lemma']}: bad unres entry"); continue
            k = skey(e['lemma'])
            forms = {nfc(f.strip().lower()) for f in (x.get('forms') or []) if isinstance(f, str) and f.strip() and ' ' not in f.strip()} | {w, e['lemma'].lower()}
            if k in known: extra_forms[next(l for l in lexlem if skey(l) == k)] |= forms; skips['known'] += 1; continue
            if k in entries: entries[k]['_forms'] |= forms; skips['dup'] += 1; continue
            e['_forms'] = forms | set(wikt(e['lemma'])); e['_rank'] = rank_of(pmw.get(x.get('w'), 0)); e['_fsrc'] = 'agent'
            entries[k] = e; order.append(k)
        elif t == 'form' and x.get('lemma'):
            extra_forms[nfc(x['lemma'])].add(w)
        elif t in ('name', 'abbr') and x.get('lemma') and x.get('gloss'):
            unames[(w, nfc(x['lemma']))] = f"{nfc(x['lemma'])}|{x['gloss']}"
        else: skips['unres-' + str(t)] += 1
# route extra forms to a new entry or an existing lemma (finalize.py indexes both)
known_forms = collections.defaultdict(set)
for lem, fs in extra_forms.items():
    k = skey(lem)
    if k in entries: entries[k]['_forms'] |= fs
    elif lem in lexlem: known_forms[lem] |= fs
    else:
        m = next((l for l in lexlem if skey(l) == k), None)
        if m: known_forms[m] |= fs
        else: problems.append(f'form of unknown lemma {lem}: {sorted(fs)[:5]}')
json.dump({l: sorted(v) for l, v in sorted(known_forms.items())}, open(f'{H}/known_forms_add.json', 'w'), ensure_ascii=False, indent=0)

# cross-check principal parts against Wiktionary's table (only where Wiktionary has a real table)
for e in entries.values():
    W = set(wikt(e['lemma']))
    if len(W) < 3: continue
    chk = []
    if e['pos'] == 'noun' and (e.get('noun') or {}).get('gen_sg'): chk.append(('gen_sg', e['noun']['gen_sg']))
    if e['pos'] == 'verb':
        for f in ('aorist_1sg', 'aorist_passive_1sg', 'participle'):
            if (e.get('verb') or {}).get(f): chk.append((f, e['verb'][f]))
    if e['pos'] == 'adjective':
        for g in ('f', 'n'):
            if (e.get('adjective') or {}).get(g): chk.append((g, e['adjective'][g]))
    for f, v in chk:
        vs = [p.strip().lower() for p in re.split(r'[/,]', str(v)) if p.strip()]
        if vs and not any(p in W for p in vs): problems.append(f"{e['lemma']}: {f}={v} not in Wiktionary table ({', '.join(sorted(W)[:12])})")

# names: Wiktionary proper names among the frequent forms, only where no common word shares the accent-free spelling
names = {}
common = {bare(f) for f in fi} | {bare(e['lemma']) for e in lex} | {bare(f) for e in entries.values() for f in e['_forms']}
for (w, lem), val in unames.items():
    for f in {w, lem.lower()}:
        if GREEK.match(f) and bare(f) not in common:
            names[lem if f == lem.lower() else (f[0].upper() + f[1:] if not lem.isupper() else f.upper())] = val
if R and M:
    def short(g):
        g = re.sub(r'\s*\(([A-Z][^()]*)\)', lambda m: f' ({m.group(1)})', g).strip()
        return g[:90]
    for x in R['new']:
        if not x['name'] or x['rank'] > 12000: continue
        g = x['wikt_gloss']
        if not g or g.lower().startswith(('alternative form', 'misspelling')): continue
        lem = x['lemma']
        for f in set(wikt(lem)) | {lem.lower()} | set(x['forms']):
            if not GREEK.match(f) or bare(f) in common: continue
            fc = f[0].upper() + f[1:] if not lem.isupper() else f.upper()
            names[fc] = f'{lem}|{short(g)}'
json.dump(names, open(f'{H}/names_add.json', 'w'), ensure_ascii=False, indent=0)

# tidy: drop null optional verb fields; indeclinable adjectives get model indecl; hand fixes from fixes10k.json
FIX = json.load(open(f'{H}/fixes10k.json')) if os.path.exists(f'{H}/fixes10k.json') else {}
for k in list(entries):
    e = entries[k]
    for f in ('aorist_passive_1sg', 'participle'):
        if (e.get('verb') or {}).get(f, 1) is None: del e['verb'][f]
    if e['pos'] == 'adjective' and not e.get('adjective') and e.get('form_key') == 'indecl':
        e['adjective'] = {'m': e['lemma'], 'f': e['lemma'], 'n': e['lemma'], 'model': 'indecl'}
    if e['pos'] == 'noun' and not e.get('noun') and e.get('form_key') == 'indecl':
        e['noun'] = {'gen_sg': e['lemma'], 'gender': 'n', 'declension': None, 'model': 'indecl'}   # loanwords are mostly neuter; exceptions in fixes10k.json
    for path, val in FIX.get(e['lemma'], {}).items():
        if path == 'DROP': del entries[k]; order.remove(k); break
        if path == 'FORMS': e['_forms'] |= set(val); continue
        h, _, kk = path.partition('.')
        if not kk: e[h] = val
        else: e.setdefault(h, {})[kk] = val
# principal parts the entry states are forms too (Wiktionary tables sometimes give only one of two valid variants)
for e in entries.values():
    for k in ('noun', 'verb', 'adjective'):
        for kk, v in (e.get(k) or {}).items():
            if isinstance(v, str) and kk not in ('model', 'gender', 'conj_group'):
                for part in re.split(r'[/,]', v):
                    part = part.strip().lower()
                    if GREEK.match(part): e['_forms'].add(part)
out = []
for k in order:
    e = entries[k]; forms = sorted(e.pop('_forms')); rank = e.pop('_rank'); e.pop('_fsrc')
    if not e.get('needs_review'): e.pop('needs_review', None)
    e['source'] = SRC10
    out.append({'entry': e, 'forms': forms, 'wf_rank': rank})
out.sort(key=lambda r: r['wf_rank'])
json.dump(out, open(f'{H}/entries.json', 'w'), ensure_ascii=False, indent=0)
json.dump({l: wf[l] for l in sorted(wf)}, open(f'{H}/wikt_forms.json', 'w'), ensure_ascii=False)
open(f'{H}/check10k.txt', 'w').write('\n'.join(problems) + '\n')
total = len({skey(e['lemma']) for e in lex if e['lemma'] not in prev10}) + len(out)
added = {'about': 'Words added to the lexicon (data/lexicon/core-3000.json) on 2026-11-05 to reach the 10,000 most frequent Modern Greek lemmas. freq_rank = rank among all Greek lemmas by frequency per million words (wordfreq).',
         'source': 'wordfreq 3.1 Greek list (Robyn Speer et al., CC BY-SA 4.0: Wikipedia, OpenSubtitles, news, web, social media), lemmatized with the lexicon forms-index and kaikki.org Wiktionary data (CC BY-SA). Tools: data/lexicon/build/10k/.',
         'count': len(out), 'lexicon_total': total,
         'words': [{'lemma': r['entry']['lemma'], 'freq_rank': r['wf_rank'], 'pos': r['entry']['pos'], 'gloss': r['entry']['gloss'],
                    'cefr': r['entry'].get('cefr_est'), **({'themes': r['entry']['themes']} if r['entry'].get('themes') else {})} for r in out]}
json.dump(added, open(f'{H}/../added-10k.json', 'w'), ensure_ascii=False, indent=0)
print('entries', len(out), 'lexicon total', total, 'skips', dict(skips.most_common(12)), 'problems', len(problems), 'names', len(names))
