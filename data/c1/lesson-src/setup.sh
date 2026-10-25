#!/bin/bash
# Copy app to a scratch site with C1 lessons wired into a test course.json
S=/tmp/claude-0/-home-user/0382d7bb-6b8c-530a-8ab0-98d2dee28f52/scratchpad/test
rm -rf $S/site; mkdir -p $S/site; cp -r /mnt/project-files/app $S/site/app; ln -s /mnt/project-files/data $S/site/data
python3 - <<'PY'
import json,glob,os
S='/tmp/claude-0/-home-user/0382d7bb-6b8c-530a-8ab0-98d2dee28f52/scratchpad/test/site/app/lessons'
c=json.load(open(S+'/course.json'))
ls=[]
for f in sorted(glob.glob(S+'/c1-*.json')):
    d=json.load(open(f)); ls.append({"id":os.path.basename(f)[:-5],"el":d["el"],"title":d["title"],"file":os.path.basename(f)})
c['units'].append({"label":"C1 test","title":"C1","lessons":ls})
json.dump(c,open(S+'/course.json','w'),ensure_ascii=False)
print(len(ls),'c1 lessons')
PY
