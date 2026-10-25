import json, unicodedata
T='/mnt/project-files/data/c1/texts/'
OUT='/mnt/project-files/app/lessons/'
def src(i, mono=True):
    d=json.load(open(T+i+'.json'))
    t=d.get('text_monotonic') if mono and d.get('text_monotonic') else d['text']
    return d, [p for p in t.split('\n\n')]
def fix(s, pairs):
    for a,b in pairs:
        assert a in s, ('missing', a)
        s=s.replace(a,b)
    return s
def q(prompt, answer, others, why):
    opts=[answer]+others
    assert len(opts)==4
    # rotate answer position deterministically
    k=sum(map(ord,prompt))%4
    opts=others[:k]+[answer]+others[k:]
    return {"prompt":prompt,"answer":answer,"options":opts,"why":why}
def mc(prompt, answer, others, why):
    return q(prompt, answer, others, why)
def check_gloss(block):
    import re
    words=set(re.findall(r"[^\s«»\"'’᾽,.;:!?·()\[\]…—―\-*]+", block['text']))
    norm=lambda w: unicodedata.normalize('NFC',w)
    missing=[k for k in block['gloss'] if norm(k) not in {norm(w) for w in words}]
    return missing
def write(name, d):
    for b in d['blocks']:
        if b['type']=='reading':
            m=check_gloss(b)
            assert len(b["gloss"])<=20, b["title"]
            if m: print(name, b['title'], 'GLOSS NOT IN TEXT:', m)
            n=len(b['text'].split())
            print(f"  {b['title'][:40]}: {n} words, {len(b['gloss'])} gloss, {len(b['questions'])} q")
            for qq in b['questions']: assert qq['answer'] in qq['options'] and len(set(qq['options']))==4
    for p in d['practice']:
        for it in p['items']:
            if p['gen']=='mc': assert it['answer'] in it['options'] and len(set(it['options']))==4, it
    json.dump(d, open(OUT+name+'.json','w'), ensure_ascii=False, indent=1)
    json.load(open(OUT+name+'.json'))
    print('wrote', name)
