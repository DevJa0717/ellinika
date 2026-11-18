# Usage: python3 tools/exam/title_check.py <stem> [<stem> ...]  — searches every exam and listening title (Greek + English) for each stem, to spot repeated topics before writing.
import json,glob,sys
T=[]
for f in glob.glob('library/listening/listening*.json'):
    for it in json.load(open(f))['items']: T.append(it['title']+' | '+it.get('title_en',''))
for f in glob.glob('library/exam/*.json'):
    for t in json.load(open(f)).get('tasks',[]): T.append(t.get('title',''))
for k in sys.argv[1:]:
    m=[t for t in T if k.lower() in t.lower()]
    print(k,len(m),m[:3])
