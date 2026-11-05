#!/usr/bin/env python3
"""commons_pd.py "query" [n]: Wikimedia Commons files under CC0 / public domain (width >= 800), as JSON lines
{title, url (1280px thumb), page, artist, license, w, h}. Used to pick reader pictures."""
import sys, json, re, time, urllib.request, urllib.parse
def get(params):
    u = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    for a in range(6):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "EllinikaReader/1.0 (personal study app)"}), timeout=60))
        except Exception:
            time.sleep(8 * (a + 1))
    return {}
def search(q, n=5):
    d = get({"action": "query", "format": "json", "generator": "search", "gsrsearch": q + " filetype:bitmap", "gsrnamespace": 6, "gsrlimit": 40,
             "prop": "imageinfo", "iiprop": "url|size|extmetadata", "iiurlwidth": 1280})
    out = []
    pages = sorted(d.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 0))
    for p in pages:
        ii = (p.get("imageinfo") or [{}])[0]; m = ii.get("extmetadata", {})
        lic = (m.get("LicenseShortName", {}).get("value") or "")
        if not re.search(r"(?i)^(cc0|public domain|pd\b|pdm)", lic): continue
        if ii.get("width", 0) < 800 or ii.get("width", 0) < ii.get("height", 1) * 0.9: continue
        art = re.sub(r"<[^>]+>", "", m.get("Artist", {}).get("value", "")).strip()[:60]
        out.append({"title": p["title"][5:], "url": ii.get("thumburl"), "page": ii.get("descriptionurl"), "artist": art or "unknown", "license": lic, "w": ii.get("width"), "h": ii.get("height")})
        if len(out) >= n: break
    return out
if __name__ == "__main__":
    for r in search(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 5): print(json.dumps(r, ensure_ascii=False))
