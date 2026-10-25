import spacy, json, collections, unicodedata, sys
nlp = spacy.load('el_core_news_md')
rows=[l.split() for l in open('/tmp/claude-0/freq/el_50k.txt',encoding='utf-8')][:25000]
words=[w for w,c in rows]; counts={w:int(c) for w,c in rows}
agg=collections.Counter(); pos=collections.defaultdict(collections.Counter); forms=collections.defaultdict(list)
for doc,w in zip(nlp.pipe(words,batch_size=2000),words):
    if len(doc)!=1: continue
    t=doc[0]
    if not any('Ͱ'<=ch<='Ͽ' or 'ἀ'<=ch<='῿' for ch in w): continue
    if t.pos_ in ('PROPN','X','PUNCT','NUM','SYM'): continue
    lem=t.lemma_.lower()
    agg[lem]+=counts[w]; pos[lem][t.pos_]+=counts[w]; forms[lem].append(w)
out=[{'lemma':l,'count':c,'upos':pos[l].most_common(1)[0][0],'forms':forms[l][:6]} for l,c in agg.most_common()]
json.dump(out,open('/tmp/claude-0/freq/lemmas.json','w'),ensure_ascii=False)
print(len(out))
