# Accent- and case-insensitive topic check across exam and listening titles.
# Usage: python3 tools/exam/dup_titles.py               -> list titles used in more than one set
#        python3 tools/exam/dup_titles.py γυπ σαπων ...  -> list existing titles containing any of these stems
# (plain grep -i misses Greek capitals and accents, so check new topics with this before writing.)
import json, glob, os, re, sys, unicodedata, collections
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def norm(s):
    s = re.sub(r'\s*\((α|β)΄ μέρος\)|\s*\(λογοτεχνικό απόσπασμα\)', '', s)
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn').strip()
rows = []
for f in sorted(glob.glob(os.path.join(root, 'library/exam/*.json'))):
    for t in json.load(open(f, encoding='utf-8')).get('tasks', []):
        if t.get('title') and not t['title'].startswith('Περίληψη'): rows.append((t['title'], os.path.basename(f), t['id']))
for f in sorted(glob.glob(os.path.join(root, 'library/listening/*.json'))):
    for t in json.load(open(f, encoding='utf-8')).get('items', []):
        rows.append((t['title'], os.path.basename(f), t['id']))
if len(sys.argv) > 1:
    pats = [norm(p) for p in sys.argv[1:]]
    for title, f, i in rows:
        if any(p in norm(title) for p in pats): print(f"{title}  [{f} {i}]")
else:
    d = collections.defaultdict(list)
    for title, f, i in rows: d[norm(title)].append(f"{f}:{i}")
    for k, v in d.items():
        sets = {re.sub(r'-(reading|use)-\d+$', '', x.split(':')[1]) for x in v}
        if len(sets) > 1: print(k, v)
