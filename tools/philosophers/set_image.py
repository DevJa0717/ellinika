"""Set the image of a chapter: set_image.py <id> <file> <caption_el> <caption_en> <credit> <license> <source>"""
import json, sys
i, f, cel, cen, cr, lic, src = sys.argv[1:8]
p = f"/mnt/project-files/app/library/philosophers/{i}.json"
d = json.load(open(p, encoding="utf-8"))
img = {"file": f, "caption": cel, "caption_en": cen, "credit": cr, "license": lic, "source": src}
out = {}
for k, v in d.items():
    if k == "image": continue
    out[k] = v
    if k == "dates": out["image"] = img
json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("ok", i)
