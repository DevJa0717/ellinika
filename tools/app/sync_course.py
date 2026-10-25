"""Mark course.json lessons that carry a reading block (used by the tracker's reading bar). Run from app/."""
import json, os
c = json.load(open("lessons/course.json"))
for u in c["units"]:
    for l in u["lessons"]:
        f = "lessons/" + l.get("file", "")
        if l.get("file") and os.path.exists(f):
            has = any(b.get("type") == "reading" for b in json.load(open(f)).get("blocks", []))
            if has: l["reading"] = True
            else: l.pop("reading", None)
json.dump(c, open("lessons/course.json", "w"), ensure_ascii=False, indent=1)
print(sum(1 for u in c["units"] for l in u["lessons"] if l.get("reading")), "lessons with readings")
