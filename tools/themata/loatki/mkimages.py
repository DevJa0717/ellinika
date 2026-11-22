import json,os,urllib.parse
out={}
lic_url={"CC0":"CC0","CC BY 2.0":"CC BY 2.0","CC BY 2.5":"CC BY 2.5","CC BY 3.0":"CC BY 3.0","CC BY 4.0":"CC BY 4.0","CC BY-SA 2.0":"CC BY-SA 2.0","CC BY-SA 2.5":"CC BY-SA 2.5","CC BY-SA 3.0":"CC BY-SA 3.0","CC BY-SA 4.0":"CC BY-SA 4.0"}
credits=[]
for l in open(__import__("os").path.join(__import__("os").path.dirname(__file__),"pictures.tsv"),encoding="utf-8"):
    cid,url,cr,lic,cap,capen=l.rstrip("\n").split("\t")
    f=f"/home/user/ellinika/img/loatki/{cid}.jpg"
    if not (os.path.exists(f) and os.path.getsize(f)>15000): continue
    name=urllib.parse.unquote(url.rsplit("/",1)[1])
    page="https://commons.wikimedia.org/wiki/File:"+urllib.parse.quote(name)
    out[cid]={"file":f"img/loatki/{cid}.jpg","caption":cap,"caption_en":capen,"credit":f"{cr} · Wikimedia Commons","license":lic,"source":page,"source_title":name}
    credits.append(f"| loatki/{cid}.jpg | {cap} | {cr} · Wikimedia Commons | {lic} | [{name}]({page}) |")
json.dump(out,open("/home/user/ellinika/tools/themata/loatki/images.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
open("/tmp/loatki-credits.md","w").write("\n## LGBTQ+ Greece reader (img/loatki/), added 2026-11-22\n\n| File | Caption | Creator · Source | Licence | Original |\n|---|---|---|---|---|\n"+"\n".join(credits)+"\n")
print(len(out))
