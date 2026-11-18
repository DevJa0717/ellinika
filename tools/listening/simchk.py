# Near-duplicate check for listening items: python3 tools/listening/simchk.py <first new batch number>
# Prints, for each item in batches >= N, the two most similar items (Jaccard overlap of 6-letter word stems).
# Anything above ~0.17 deserves a look; above ~0.2 is usually a rewrite of an older item.
import json,glob,re,sys,unicodedata
def n(s): return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
def toks(it):
    t=n(' '.join(s['el'] for s in it['script']))
    w=set(x[:6] for x in re.findall(r'[α-ω]{5,}',t))
    return w
old=[];new=[]
lo=int(sys.argv[1])
for f in glob.glob('library/listening/listening-*.json'):
    k=int(re.search(r'-(\d+)\.json',f).group(1))
    for it in json.load(open(f))['items']:
        (new if k>=lo else old).append((k,it['title'],toks(it)))
for k,t,w in new:
    best=sorted(((len(w&w2)/len(w|w2),k2,t2) for k2,t2,w2 in old+[x for x in new if x[1]!=t]),reverse=True)[:2]
    print(k,t,'|',['%.2f %d %s'%b for b in best])
