import os,sys,importlib.util,urllib.request,urllib.parse,json,re
shelf=sys.argv[1]; keys=sys.argv[2:]
spec=importlib.util.spec_from_file_location("s",os.path.join(os.path.dirname(os.path.abspath(__file__)), shelf, "sources.py")); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
by={}
for k in keys:
    u=m.SRC[k][1]
    mm=re.match(r"https://(en|el)\.(wikipedia|wiktionary)\.org/wiki/(.+)",u)
    if not mm: print("SKIP(non-wiki)",k,u); continue
    by.setdefault((mm.group(1),mm.group(2)),[]).append((k,urllib.parse.unquote(mm.group(3))))
for (lang,site),lst in by.items():
    for i in range(0,len(lst),40):
        ch=lst[i:i+40]
        q=urllib.parse.urlencode({"action":"query","format":"json","redirects":1,"titles":"|".join(t for _,t in ch)})
        import time
        for a in range(8):
            try:
                d=json.load(urllib.request.urlopen(urllib.request.Request(f"https://{lang}.{site}.org/w/api.php?"+q,headers={"User-Agent":"EllinikaReader/1.0 (personal study app)"}),timeout=60)); break
            except Exception as e:
                time.sleep(10*(a+1))
        miss={p["title"] for p in d["query"]["pages"].values() if "missing" in p or "invalid" in p}
        norm={n["from"]:n["to"] for n in d["query"].get("normalized",[])}
        for k,t in ch:
            t2=norm.get(t.replace("_"," "),t.replace("_"," "))
            print(("MISSING " if t2 in miss else "ok ")+k)
