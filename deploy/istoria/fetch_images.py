#!/usr/bin/env python3
"""Fetch the reader's public-domain pictures listed in images_spec.json into app/img/istoria/ (1100 px JPEG)
and write src/images.json with caption, credit, licence and source for each. Already-fetched files are kept."""
import json, os, re, sys, time, io, urllib.request, urllib.parse
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
APP = "/mnt/project-files/app"
UA = {"User-Agent": "EllinikaReader/1.0 (personal study app; github.com/DevJa0717/ellinika)"}
def get(u, raw=False):
    for t in range(int(os.environ.get('TRIES', '3'))):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()
            return r if raw else json.loads(r)
        except Exception as e:
            print("  retry", t, e); time.sleep(5 * (t + 1))
    raise RuntimeError("failed " + u)
spec = json.load(open(os.path.join(HERE, "images_spec.json")))
outp = os.path.join(HERE, "src/images.json")
out = json.load(open(outp)) if os.path.exists(outp) else {}
os.makedirs(os.path.join(APP, "img/istoria"), exist_ok=True)
strip = lambda s: re.sub(r"\s+", " ", re.sub("<[^>]+>", "", s or "")).strip()
for key, s in spec.items():
    if s.get("reuse"):
        out[key] = {"file": s["reuse"], "caption": s["caption"], "caption_en": s["caption_en"], "credit": s["credit"], "license": s["license"], "source": s["source"]}
        continue
    fn = f"img/istoria/{key}.jpg"; path = os.path.join(APP, fn)
    if key in out and os.path.exists(path) and out[key].get("caption") == s["caption"] and out[key].get("caption_en") == s["caption_en"]:
        continue
    if s["src"] == "met":
        try: o = get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{s['id']}")
        except RuntimeError as e: print('SKIP', key, e); continue
        assert o["isPublicDomain"], key
        url = o["primaryImage"]
        who = o.get("artistDisplayName") or o.get("culture") or ""
        credit = f"{who + ', ' if who else ''}{o['title']} ({o['objectDate']}) · The Metropolitan Museum of Art, {o.get('creditLine','').split(',')[0]}"
        lic, source = "Public domain (CC0)", o["objectURL"]
    else:
        import hashlib
        name = s["file"].replace("File:", "").replace(" ", "_")
        h = hashlib.md5(name.encode()).hexdigest()
        q = urllib.parse.quote(name)
        url = f"https://upload.wikimedia.org/wikipedia/commons/thumb/{h[0]}/{h[:2]}/{q}/960px-{q}"
        if s.get("small"): url = f"https://upload.wikimedia.org/wikipedia/commons/{h[0]}/{h[:2]}/{q}"
        lic = s["license"]; credit = s["credit"]; source = "https://commons.wikimedia.org/wiki/File:" + q
        time.sleep(20)
    try: data = get(url, raw=True)
    except RuntimeError as e: print('SKIP', key, e); continue
    im = Image.open(io.BytesIO(data)).convert("RGB")
    if max(im.size) > 1100: im.thumbnail((1100, 1100))
    im.save(path, "JPEG", quality=82, optimize=True, progressive=True)
    out[key] = {"file": fn, "caption": s["caption"], "caption_en": s["caption_en"], "credit": s.get("credit") or credit, "license": lic, "source": source}
    json.dump(out, open(outp, "w"), ensure_ascii=False, indent=1)
    print("ok", key, im.size, os.path.getsize(path) // 1024, "KB")
json.dump(out, open(outp, "w"), ensure_ascii=False, indent=1)
