import json, unicodedata, sys
S=sys.argv[1]
def strip(s): return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
core=json.load(open('/mnt/project-files/data/lexicon/core-1000.json'))
known=set()
for e in core:
    known.add(strip(e['lemma']))
    for k in ('verb','noun','adjective'):
        for v in (e.get(k) or {}).values():
            if isinstance(v,str): known.add(strip(v))
lem=json.load(open('/tmp/claude-0/freq/lemmas.json'))
c=[]
for x in lem:
    if strip(x['lemma']) in known or any(strip(f) in known for f in x['forms'][:1]): continue
    if len(x['lemma'])<2: continue
    c.append({'cand':x['lemma'],'upos':x['upos'],'forms':x['forms'][:5],'count':x['count']})
for i,x in enumerate(c): x['i']=i
json.dump(c,open(f'{S}/candidates.json','w'),ensure_ascii=False)
print(len(c)); json.dump(sorted(known),open(f'{S}/known_core.json','w'),ensure_ascii=False)
for k in range(4):
    json.dump(c[k*170:(k+1)*170],open(f'{S}/batches/b1_{k}.in.json','w'),ensure_ascii=False)
print(c[0],c[679])
