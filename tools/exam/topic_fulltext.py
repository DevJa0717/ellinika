# Accent-free full-text topic search over all exam tasks and listening items.
# Usage: python3 tools/exam/topic_fulltext.py word1 "two words" ...  (prints hit count and the first ids)
import sys,unicodedata,json,glob,os
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
def n(s): return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
docs=[]
for f in glob.glob(os.path.join(ROOT,'library/exam/*.json')):
    for t in json.load(open(f)).get("tasks",[]): docs.append((t['id'],n(t.get('title','')+' '+t.get('text_el','')+' '+t.get('instructions_el',''))))
for f in glob.glob(os.path.join(ROOT,'library/listening/*.json')):
    for i in json.load(open(f))['items']: docs.append((i['id'],n(i.get('title','')+' '+i.get('title_en','')+' '+' '.join(s['el'] for s in i['script']))))
for w in sys.argv[1:]:
    h=[d[0] for d in docs if n(w) in d[1]]
    print(w, len(h), ' '.join(h[:5]))
