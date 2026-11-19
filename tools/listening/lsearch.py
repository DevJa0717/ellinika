import json,glob,unicodedata,sys
def n(s): return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
items=[i for f in glob.glob('library/listening/*.json') for i in json.load(open(f))['items']]
for w in sys.argv[1:]:
  w2=n(w); hits=[i['id'] for i in items if w2 in n(json.dumps(i,ensure_ascii=False))]
  print(w,len(hits),hits[:6])
