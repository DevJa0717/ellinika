#!/usr/bin/env python3
"""Topic-overlap check for exam tasks: compare each task of the given set ids with every
other task of the same type (reading-1, use-3, ...) by content-word overlap.
Usage: python3 tools/exam/simchk_exam.py b2-p253 c1-p241 ...   (scores >= ~0.12 deserve a look)"""
import json, glob, re, sys, unicodedata, os
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def norm(s): return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
STOP = set(norm(w) for w in "οποίος οποία οποίο οποίοι οποίες οποίων οποίου οποίας είναι ήταν έχουν είχαν μπορεί μπορούν αλλά επίσης όμως πολύ πολλά πολλοί πολλές περισσότερο κάποιοι κάποια μέχρι ακόμη ακόμα σήμερα πρέπει γιατί επειδή όταν αυτό αυτή αυτός αυτά αυτές αυτούς αυτήν μετά πριν χρόνια χρόνο χρονών μέρες μέρα κάθε όλοι όλες όλα όλους λέει λένε έγινε γίνεται γίνονται".split())
def toks(t):
    s = norm(' '.join(str(t.get(k, '')) for k in ('title', 'text_el')))
    return set(w for w in re.findall(r'[α-ω]{5,}', s) if w not in STOP)
tasks = []
for f in glob.glob(os.path.join(root, 'library/exam/*-tasks*.json')):
    j = json.load(open(f)); j = j['tasks'] if isinstance(j, dict) else j
    tasks += [t for t in j if isinstance(t, dict) and 'id' in t]
def kind(i): return i.split('-')[0] + '-' + '-'.join(i.split('-')[-2:])
for sid in sys.argv[1:]:
    for t in [t for t in tasks if t['id'].startswith(sid + '-')]:
        a = toks(t); k = kind(t['id']); res = []
        for u in tasks:
            if u['id'] == t['id'] or kind(u['id']) != k or u['id'].startswith(sid + '-'): continue
            b = toks(u)
            if a and b: res.append((len(a & b) / len(a | b), u['id'], u['title']))
        res.sort(reverse=True)
        print(t['id'], '|', t['title'][:40], '|', ['%.2f %s %s' % (s, i, ti[:30]) for s, i, ti in res[:2]])
