# Topic pre-check: accent/diaeresis-insensitive search of titles and bodies of all exam and listening files.
# Usage: python3 tools/exam/topic_chk.py <stem> <stem> ...
import json,glob,unicodedata,sys,os
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def n(s): return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
T=[]
for f in glob.glob(ROOT+'/library/exam/*.json')+glob.glob(ROOT+'/library/listening/*.json'):
    d=json.load(open(f))
    for it in d.get('items',d.get('tasks',[])): T.append((f.split('/')[-1],n(it.get('title','')+' '+it.get('title_en','')), n(json.dumps(it,ensure_ascii=False))))
for k in sys.argv[1:]:
    k2=n(k); hits=sorted(set(t[0] for t in T if k2 in t[2]))
    print(f"{k}: body {len(hits)} title {sum(k2 in t[1] for t in T)} {hits[:4]}")
