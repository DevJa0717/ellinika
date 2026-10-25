import json
T='/mnt/project-files/data/c1/texts/'
def src(i): return json.load(open(T+i+'.json'))
def paras(i): return src(i)['text'].split('\n\n')
def P(i,*idx,fix=None):
    ps=paras(i); out=[]
    for k in idx:
        if k=='cut': out.append('[…]'); continue
        out.append(ps[k])
    t='\n\n'.join(out)
    for a,b in (fix or []):
        assert a in t,(a); t=t.replace(a,b)
    return t
def R(title,text,en,gloss,qs):
    for k in gloss: assert k in text,('gloss key missing',k)
    for q in qs:
        assert q['answer'] in q['options'] and len(q['options'])==4,q
    assert 6<=len(gloss)<=20,(title,len(gloss))
    return {"type":"reading","title":title,"text":text,"en":en,"gloss":gloss,"questions":qs}
def Q(prompt,answer,others,why):
    return {"prompt":prompt,"answer":answer,"options":[answer]+others if True else None,"why":why}
import random
def Qs(prompt,answer,others,why,pos=0):
    o=list(others); o.insert(pos%4,answer)
    return {"prompt":prompt,"answer":answer,"options":o,"why":why}
def save(id,d):
    for it in d['practice']:
        for x in it['items']:
            if it['gen']=='mc': assert x['answer'] in x['options'] and len(x['options'])==4,x
    p='/mnt/project-files/app/lessons/%s.json'%id
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
    json.load(open(p))
    import re
    nw=[len(b['text'].split()) for b in d['blocks'] if b['type']=='reading']
    print(id,'saved; reading words',nw)
