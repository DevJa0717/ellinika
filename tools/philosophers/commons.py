"""Fetch a Wikimedia Commons file as a resized JPEG via the upload.wikimedia.org thumb URL (the API rate-limits hard).
Usage: python3 commons.py "<File name without File:>" <out.jpg> [width]"""
import hashlib, subprocess, sys, urllib.parse, os
name = sys.argv[1].replace(" ", "_"); out = sys.argv[2]; w = sys.argv[3] if len(sys.argv) > 3 else "1280"
h = hashlib.md5(name.encode()).hexdigest()
q = urllib.parse.quote(name)
ext = name.rsplit(".", 1)[-1].lower()
thumb = f"{w}px-{q}" + (".jpg" if ext in ("tif", "tiff") else "")
url = f"https://upload.wikimedia.org/wikipedia/commons/thumb/{h[0]}/{h[:2]}/{q}/{thumb}"
tmp = out + ".dl"
r = subprocess.run(["curl", "-sSfL", "-A", "EllinikaReader/1.0 (personal Greek study app; https://github.com/DevJa0717/ellinika)", "-o", tmp, url])
if r.returncode:
    url = f"https://upload.wikimedia.org/wikipedia/commons/{h[0]}/{h[:2]}/{q}"
    r = subprocess.run(["curl", "-sSfL", "-A", "EllinikaReader/1.0 (personal Greek study app; https://github.com/DevJa0717/ellinika)", "-o", tmp, url])
if r.returncode: sys.exit("download failed: " + url)
from PIL import Image
im = Image.open(tmp).convert("RGB"); im.thumbnail((1100, 1100)); im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
os.remove(tmp); print(out, im.size, os.path.getsize(out) // 1024, "KB", url)
