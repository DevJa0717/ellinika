#!/usr/bin/env python3
"""Resolve picture candidates to direct image URL + licence + author.
Usage: python3 resolve_img.py <spec> ...   spec = curid:N | file:Title.jpg | met:N | flickr:URL
Prints JSON lines {spec, url, license, artist, page}."""
import json, re, sys, urllib.parse, urllib.request
UA = {"User-Agent": "EllinikaReader/1.0 (personal study app; https://github.com/DevJa0717/ellinika)"}
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40).read().decode("utf-8", "replace")
def strip(h): return re.sub(r"<[^>]+>", "", h or "").strip()
def commons(**q):
    q.update(action="query", prop="imageinfo", iiprop="url|extmetadata", iiurlwidth="1100", format="json")
    d = json.loads(get("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(q)))
    p = list(d["query"]["pages"].values())[0]; ii = p["imageinfo"][0]; m = ii["extmetadata"]
    return dict(url=ii.get("thumburl") or ii["url"], license=m.get("LicenseShortName", {}).get("value"), artist=strip(m.get("Artist", {}).get("value"))[:150],
                page=ii["descriptionurl"], title=p["title"], desc=strip(m.get("ImageDescription", {}).get("value"))[:200], date=strip(m.get("DateTimeOriginal", {}).get("value"))[:40])
for s in sys.argv[1:]:
    k, v = s.split(":", 1)
    try:
        if k == "curid": r = commons(pageids=v)
        elif k == "file": r = commons(titles="File:" + v)
        elif k == "met":
            d = json.loads(get("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + v))
            r = dict(url=d["primaryImage"], license="CC0" if d["isPublicDomain"] else "NOT PD", artist=d.get("artistDisplayName"), page=d["objectURL"], title=d["title"], date=d.get("objectDate"), desc=d.get("culture"))
        elif k == "flickr":
            h = get(v)
            img = re.search(r'property="og:image" content="([^"]+)"', h); t = re.search(r'property="og:title" content="([^"]+)"', h)
            lic = re.findall(r'(Public Domain[^"<]*|CC0[^"<]*|No known copyright[^"<]*|Some rights reserved|All rights reserved)', h)
            own = re.search(r'"ownername":"([^"]+)"', h)
            r = dict(url=img and img.group(1), license=(lic[:2] if lic else None), artist=own and own.group(1), page=v, title=t and t.group(1))
        else: r = {"error": "unknown"}
    except Exception as e: r = {"error": str(e)[:100]}
    print(json.dumps({"spec": s, **r}, ensure_ascii=False))
