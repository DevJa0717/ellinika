import json,glob,sys,unicodedata
def n(s): return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
files=[(f,json.load(open(f))) for f in glob.glob('library/listening/*.json')+glob.glob('library/exam/*.json')]
for k in sys.argv[1:]:
  r=[]
  for f,d in files:
    for i in d.get('items',d.get('tasks',[])):
      if n(k) in n(i.get('title','')+' '+i.get('title_en','')) or n(k) in n(json.dumps(i.get('script',''),ensure_ascii=False)): r.append(f.split('/')[-1][:-5].replace('listening-','L').replace('tasks-','')+':'+i['title'][:38])
  ex=[x for x in r if not x.startswith("L")]; print(k,len(r),"exam:",ex[:15],"listening:",[x for x in r if x.startswith("L")][:6])
