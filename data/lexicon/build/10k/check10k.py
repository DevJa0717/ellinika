#!/usr/bin/env python3
"""Accuracy checks on the 10k-extension entries (build/10k/entries.json), the same rule set as the 2026-10-25 audit:
el_GR hunspell word list (LibreOffice, 828k words; EL_DIC=path or argv[1]) for lemma, principal parts and every word of
the example; mixed Latin/Greek letters; final σ/ς; double accents; accented monosyllables; final-ν rule after
τη(ν)/στη(ν)/δε(ν)/μη(ν); entry structure (gen_sg for nouns, f/n for adjectives, aorist for verbs, valid models);
headword present in its own example; article gender against the noun's gender right before the headword.
Usage: python3 -I check10k.py [el_GR.dic]  -> prints problems, exits 0."""
import json, os, re, sys, unicodedata
H = os.path.dirname(os.path.abspath(__file__)); L = os.path.join(H, '..', '..')
DIC = sys.argv[1] if len(sys.argv) > 1 else os.environ.get('EL_DIC', '/tmp/claude-0/dict/el_GR.dic')
words = {l.split('/')[0].strip().lower() for l in open(DIC, encoding='iso-8859-7').read().split('\n')[1:] if l.strip()}
fi = json.load(open(f'{L}/forms-index.json'))['forms']
R = json.load(open(f'{H}/entries.json'))
newforms = {f for r in R for f in r['forms']}
okset = words | set(fi) | newforms
def bare(s): return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
def accents(w): return sum(1 for c in unicodedata.normalize('NFD', w) if c in '́͂')
GR = re.compile(r'[Ͱ-Ͽἀ-῿]+')
NMOD = set('m-ας-a m-ας-b m-ης m-ος-fixed m-ος-antepenult-a m-ος-antepenult-b m-έας m-imparisyllabic-final m-imparisyllabic-penult m-imparisyllabic-antepenult f-α-a f-α-b f-η-ες f-ος f-η-εις f-imparisyllabic-ά f-imparisyllabic-ού f-ω-b common-ής-είς n-ο-a n-ο-b n-ί n-ι n-ος-2syl n-ος-3syl n-μα n-ιμο n-ας n-ως n-ον indecl irregular'.split())
AMOD = set('adj-ος-η-ο adj-ος-α-ο adj-ος-ια-ο adj-ύς-ιά-ύ adj-ύς-εία-ύ adj-ής-ιά-ί adj-πολύς adj-ής-ές-fixed adj-ης-ες-shift adj-ης-α-ικο adj-άς-ού-άδικο adj-ων-ουσα-ον indecl irregular'.split())
ART = {'ο': 'm', 'τον': 'm', 'του': 'mn', 'η': 'f', 'την': 'f', 'τη': 'f', 'της': 'f', 'το': 'n', 'οι': 'mf', 'τους': 'm', 'τις': 'f', 'τα': 'n', 'των': 'mfn'}
MONO_OK = {'πού', 'πώς', 'ή', 'μού', 'σού', 'τού', 'μάς', 'σάς', 'τούς', 'τής', 'τόν', 'τήν', 'τό', 'τά', 'τί', 'γιά', 'νά'}
probs = []
def p(e, msg): probs.append(f"{e['lemma']}: {msg}")
for r in R:
    e = r['entry']; lem = e['lemma']; ex = e.get('example') or {}
    strs = [lem, ex.get('el', '')] + [str(v) for k in ('noun', 'verb', 'adjective') for kk, v in (e.get(k) or {}).items() if isinstance(v, str) and kk not in ('model', 'gender', 'conj_group')]
    for s in strs:
        if re.search(r'[A-Za-z][Ͱ-Ͽ]|[Ͱ-Ͽ][A-Za-z]', s): p(e, f'mixed script: {s[:40]}')
        for w in GR.findall(s):
            if re.search(r'ς\B', w) or re.search(r'σ$', w): p(e, f'final sigma: {w}')
            if accents(w) > 1 and not re.search(re.escape(w) + r'\s+(μου|σου|του|της|μας|σας|τους|τον|την|το|τα|τις|τη|με|σε)\b', s): p(e, f'double accent: {w}')
            if len(w) > 1 and w.lower() not in okset and w.lower() not in MONO_OK: p(e, f'unknown word: {w}')
    for m in re.finditer(r'(?<!\w)(σ?την|σ?τη|δεν|δε|μην|μη)\s+(\w\w?)', ex.get('el', ''), re.I):
        art, nxt = m.group(1).lower(), m.group(2).lower()
        keep = bare(nxt[0]) in 'αεηιουωκπτξψ' or nxt in ('μπ', 'ντ', 'γκ', 'τσ', 'τζ')
        if art in ('την', 'στην', 'τη', 'στη') and art.endswith('ν') != keep: p(e, f'final-ν: {m.group(0)}')
    # structure
    if e['pos'] == 'noun':
        n = e.get('noun') or {}
        if not n.get('gen_sg') and not n.get('pl_only'): p(e, 'noun without gen_sg')
        if n.get('model') not in NMOD: p(e, f"noun model {n.get('model')}")
        if n.get('gender') not in ('m', 'f', 'n', 'common'): p(e, f"gender {n.get('gender')}")
    if e['pos'] == 'adjective':
        a = e.get('adjective') or {}
        if not (a.get('f') and a.get('n')) and a.get('model') != 'indecl': p(e, 'adjective without f/n')
        if a.get('model') not in AMOD: p(e, f"adjective model {a.get('model')}")
    if e['pos'] == 'verb':
        v = e.get('verb') or {}
        if 'aorist_1sg' not in v: p(e, 'verb without aorist_1sg')
        if v.get('conj_group') not in ('A', 'B1', 'B2', 'deponent', 'irregular'): p(e, f"conj_group {v.get('conj_group')}")
    # headword used in its example
    toks = [t.lower() for t in GR.findall(ex.get('el', ''))]
    forms = set(r['forms']) | {lem.lower()}
    if ' ' not in lem and not any(t in forms for t in toks) and not any(bare(t) in {bare(f) for f in forms} for t in toks):
        p(e, f"headword not in example: {ex.get('el', '')}")
    # article right before the headword: gender agreement (nouns only)
    if e['pos'] == 'noun' and (e.get('noun') or {}).get('gender') in ('m', 'f', 'n'):
        g = e['noun']['gender']
        for a, b in zip(toks, toks[1:]):
            if b in forms and a in ART and g not in ART[a] and not (a == 'του' and g == 'f') and a not in ('της', 'του', 'τους'):
                p(e, f'article/gender: {a} {b} ({g})')
    if not ex.get('en'): p(e, 'example without English')
print('\n'.join(probs)); print(f'-- {len(R)} entries, {len(probs)} flags', file=sys.stderr)
