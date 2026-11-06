"""Flag nouns whose gen_sg does not match their declension model (data/lexicon core files)."""
import json, sys, unicodedata, os
L = os.path.join(os.path.dirname(__file__), '..', '..')
def strip(w): return ''.join(c for c in unicodedata.normalize('NFD', w) if unicodedata.category(c) != 'Mn')
V = set('αεηιουω')
def sylls(w):
    # count vowel groups (rough): positions of vowel letters, digraphs merged
    s = strip(w).lower(); out = []; i = 0
    while i < len(s):
        if s[i] in V:
            j = i + 1
            if s[i:i+2] in ('αι', 'ει', 'οι', 'ου', 'υι', 'αυ', 'ευ') : j = i + 2
            out.append((i, j)); i = j
        else: i += 1
    return out
def stress_from_end(w):
    n = unicodedata.normalize('NFD', w); pos = None; k = 0; base = []
    for c in n:
        if unicodedata.category(c) == 'Mn':
            if c in '́': pos = len(base) - 1
        else: base.append(c)
    if pos is None: return None
    sy = sylls(''.join(base))
    for idx, (a, b) in enumerate(sy):
        if a <= pos < b: return len(sy) - idx
    return None
def exp_add(lemma, gen, suffix_len_drop, add):
    return strip(gen) == strip(lemma[:len(lemma)-suffix_len_drop] + add) if suffix_len_drop else strip(gen) == strip(lemma + add)
R = []
lex = json.load(open(f'{L}/core-1000.json')) + json.load(open(f'{L}/core-3000.json'))
for e in lex:
    if e.get('pos') != 'noun': continue
    n = e.get('noun') or {}; m = n.get('model'); g = n.get('gen_sg'); w = e['lemma']
    if not g or n.get('pl_only') or ' ' in w: continue
    bad = None
    if m in ('f-α-a', 'f-α-b', 'f-η-ες', 'f-η-εις', 'f-imparisyllabic-ά', 'f-imparisyllabic-ού'):
        if g != w + 'ς': bad = 'expected ' + w + 'ς'
    elif m in ('m-ης', 'm-ας-a', 'm-ας-b', 'm-έας', 'm-imparisyllabic-final', 'm-imparisyllabic-penult', 'm-imparisyllabic-antepenult'):
        if g != w[:-1]: bad = 'expected ' + w[:-1]
    elif m in ('m-ος-fixed', 'm-ος-antepenult-a', 'm-ος-antepenult-b', 'f-ος'):
        if strip(g) != strip(w[:-2] + 'ου'): bad = 'ending'
        else:
            sl, sg = stress_from_end(w), stress_from_end(g)
            if m == 'm-ος-fixed' and sl != sg and sl != 3: bad = f'stress moved {sl}->{sg}'
            if m == 'm-ος-antepenult-a' and sg != 2: bad = f'antepenult-a should move stress to penult ({sg})'
            if m == 'm-ος-antepenult-b' and sg != sl: bad = f'antepenult-b should keep stress ({sl}->{sg})'
            if m == 'm-ος-fixed' and sl == 3 and sg != 3: bad = 'antepenult noun labelled fixed but stress moves (should be antepenult-a)'
    elif m in ('n-ο-a', 'n-ο-b'):
        if strip(g) != strip(w[:-1] + 'ου'): bad = 'ending'
        else:
            sl, sg = stress_from_end(w), stress_from_end(g)
            if m == 'n-ο-b' and sl != sg: bad = f'n-ο-b should keep stress ({sl}->{sg})'
            if m == 'n-ο-a' and sl == 3 and sg == 3: bad = 'stress kept: should be n-ο-b'
    elif m in ('n-ι', 'n-ί'):
        if strip(g) != strip(w + 'ου') or not g.endswith('ού'): bad = 'expected -ιού'
    elif m == 'n-μα':
        if strip(g) != strip(w + 'τος'): bad = 'expected -ματος'
    elif m in ('n-ος-2syl', 'n-ος-3syl'):
        if strip(g) != strip(w[:-2] + 'ους'): bad = 'expected -ους'
    elif m == 'n-ιμο':
        if strip(g) != strip(w[:-1] + 'ατος'): bad = 'expected -ίματος'
    if bad: R.append((w, m, g, bad))
for r in R: print(*r, sep=' | ')
print(len(R), 'flags', file=sys.stderr)
