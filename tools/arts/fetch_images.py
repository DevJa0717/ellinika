#!/usr/bin/env python3
"""Download every picture in images_spec.py to /mnt/project-files/app/img/<shelf>/<id>.jpg (max 1100 px) and write <shelf>/images.json.
Skips files that already exist. Commons via upload.wikimedia.org thumbs (tools/philosophers/commons.py), spaced out."""
import json, os, re, subprocess, sys, time, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from images_spec import S
UA = "EllinikaReader/1.0 (personal study app; https://github.com/DevJa0717/ellinika)"
from PIL import Image
out = {}
for cid, (shelf, src, cel, cen, credit, lic, page) in S.items():
    d = f"/mnt/project-files/app/img/{shelf}"; os.makedirs(d, exist_ok=True); f = f"{d}/{cid}.jpg"
    if not os.path.exists(f):
        try:
            if src.startswith("commons:"):
                r = subprocess.run(["python3", "/mnt/project-files/tools/philosophers/commons.py", src[8:], f, "960"], capture_output=True, text=True)
                print(cid, r.stdout.strip() or r.stderr.strip()[-200:]); time.sleep(45)
            else:
                u = src[4:]
                if u.startswith("MET:"):
                    u = json.loads(urllib.request.urlopen("https://collectionapi.metmuseum.org/public/collection/v1/objects/" + u[4:], timeout=60).read())["primaryImage"]
                if u.startswith("FLICKR:"):
                    h = urllib.request.urlopen(urllib.request.Request("https://www.flickr.com/photos/" + u[7:], headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read().decode("utf-8", "replace")
                    u = re.search(r'property="og:image" content="([^"]+)"', h).group(1)
                tmp = f + ".dl"; urllib.request.urlretrieve(u, tmp) if False else open(tmp, "wb").write(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=120).read())
                im = Image.open(tmp).convert("RGB"); im.thumbnail((1100, 1100)); im.save(f, "JPEG", quality=82, optimize=True, progressive=True); os.remove(tmp)
                print(cid, im.size, os.path.getsize(f) // 1024, "KB")
        except Exception as e:
            print(cid, "FAILED", e)
    if os.path.exists(f):
        out.setdefault(shelf, {})[cid] = {"file": f"img/{shelf}/{cid}.jpg", "caption": cel, "caption_en": cen, "credit": credit, "license": lic, "source": page}
for shelf, m in out.items():
    json.dump(m, open(os.path.join(HERE, shelf, "images.json"), "w"), ensure_ascii=False, indent=1)
    print(shelf, len(m), "pictures")
