#!/usr/bin/env python3
"""Copy the arts readers (mousiki, skini, eortes) into a repo clone and make the small shared-file edits, idempotently.
Usage: python3 publish.py <repo>   (then commit only the paths it prints)"""
import json, os, re, shutil, subprocess, sys
R = [a for a in sys.argv[1:] if not a.startswith("--")][0]; P = "/mnt/project-files"; HERE = os.path.dirname(os.path.abspath(__file__))
SH = {"mousiki": ("Η ελληνική μουσική", "Bilingual music reader: Byzantine chant, folk song, rebetiko and its slang, Hatzidakis, Theodorakis, laïkó and today", "Music", "B1+–C1",
                  "Greek music · Η ελληνική μουσική: bilingual reader from Byzantine chant and folk song to rebetiko and its slang, Hatzidakis, Theodorakis, laïkó and the scene today"),
      "skini": ("Θέατρο και κινηματογράφος", "Bilingual theatre and cinema reader: ancient drama, Karagiozis, the modern stage, Finos Film, Cacoyannis, Angelopoulos and the Weird Wave", "Theatre-cinema", "B1–C1",
                "Theatre and cinema · Θέατρο και κινηματογράφος: bilingual reader from Dionysus and Epidaurus to Karagiozis, Koun, Finos Film, Angelopoulos, the Weird Wave and summer cinemas"),
      "eortes": ("Ο χρόνος της Ορθοδοξίας", "Bilingual reader on the Greek Orthodox year: feasts, fasts, Holy Week and Easter, saints' days, customs and church Greek", "Orthodox-year", "B1+–C1",
                 "The Orthodox year · Ο χρόνος της Ορθοδοξίας: bilingual reader on the church calendar, name days, Christmas to Epiphany, carnival and Lent, Holy Week and Easter, the summer feasts and church Greek")}
touched = []
def cp(src, dst):
    if os.path.exists(dst) and os.path.realpath(src) == os.path.realpath(dst): return
    if os.path.isdir(src):
        if os.path.exists(dst): shutil.rmtree(dst)
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", "*.log"))
    else:
        os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy2(src, dst)
    touched.append(os.path.relpath(dst, R))
for s in SH:
    cp(f"{P}/app/library/{s}", f"{R}/library/{s}")
    cp(f"{P}/app/img/{s}", f"{R}/img/{s}")
    pdf = f"{P}/downloads/textbook/Ellinika-{SH[s][2]}.pdf"
    if os.path.exists(pdf): cp(pdf, f"{R}/downloads/textbook/Ellinika-{SH[s][2]}.pdf")
cp(HERE, f"{R}/tools/arts")
# library/index.json rows after the last bilingual shelf row
p = f"{R}/library/index.json"; t = open(p, encoding="utf-8").read(); d = json.loads(t)
shelves = d if isinstance(d, list) else d.get("shelves") or d.get("items")
have = {x.get("id") for x in shelves}
pos = max(i for i, x in enumerate(shelves) if x.get("id") in ("politeia", "kouzina", "athlitismos", "mathiatriki", "epistimi", "nisia", "diaspora", "simera")) + 1
for s, v in SH.items():
    if s not in have:
        shelves.insert(pos, {"id": s, "route": s, "el": v[0], "title": v[1], "ready": True}); pos += 1
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1); open(p, "a").write("\n") if t.endswith("\n") else None
touched.append("library/index.json")
# credits
p = f"{R}/img/CREDITS.md"; t = open(p, encoding="utf-8").read()
H = "## Music, theatre/cinema and Orthodox year readers"
if H in t:
    a = t.index(H); b = t.find("\n## ", a + 3); t = t[:a].rstrip("\n") + ("\n" + t[b:] if b > 0 else "\n")
if True:
    rows = ["", "## Music, theatre/cinema and Orthodox year readers (img/mousiki/, img/skini/, img/eortes/)", "", "| File | Subject | Author | License | Source |", "|---|---|---|---|---|"]
    for s in SH:
        f = os.path.join(HERE, s, "images.json")
        for cid, im in (json.load(open(f)) if os.path.exists(f) else {}).items():
            rows.append(f"| {s}/{cid}.jpg | {im['caption']} | {im['credit']} | {im['license']} | [{im['source']}]({im['source']}) |")
    open(p, "w", encoding="utf-8").write(t.rstrip("\n") + "\n" + "\n".join(rows) + "\n")
touched.append("img/CREDITS.md")
# offline files
p = f"{R}/offline-files.json"; d = json.load(open(p)); fresh = "library/mousiki/index.json" not in d["files"]
add = sorted(os.path.relpath(os.path.join(dp, f), R) for s in SH for base in (f"{R}/library/{s}", f"{R}/img/{s}") for dp, _, fs in os.walk(base) for f in fs)
d["files"] = sorted(set(d["files"]) | set(add)); json.dump(d, open(p, "w"), ensure_ascii=False); touched.append("offline-files.json")
# sw cache bump
p = f"{R}/sw.js"; t = open(p).read()
if fresh or "--bump" in sys.argv:
  n = int(re.search(r'ellinika-v(\d+)', t).group(1))
  open(p, "w").write(t.replace(f"ellinika-v{n}", f"ellinika-v{n+1}", 1)); touched.append("sw.js"); print("sw", n + 1)
# textbook index lines
p = f"{R}/downloads/textbook/index.html"
if not os.path.exists(p): print("\n".join(sorted(set(touched)))); sys.exit()
t = open(p, encoding="utf-8").read()
for s, v in SH.items():
    pdf = f"{R}/downloads/textbook/Ellinika-{v[2]}.pdf"
    if not os.path.exists(pdf) or f"Ellinika-{v[2]}.pdf" in t: continue
    pages = int(subprocess.run(["python3", "-c", f"import pikepdf;print(len(pikepdf.open('{pdf}').pages))"], capture_output=True, text=True).stdout.strip() or 0)
    idx = json.load(open(f"{R}/library/{s}/index.json")); nq = sum(len(json.load(open(f"{R}/library/{s}/{x['file']}"))["questions"]) for x in idx["items"])
    npic = len(os.listdir(f"{R}/img/{s}"))
    li = f'<li><a href="Ellinika-{v[2]}.pdf"><span class="lv">{v[3]}</span><span class="t">{v[4]}<small>{pages} pages · {os.path.getsize(pdf)/1e6:.1f} MB · {len(idx["items"])} chapters, {npic} pictures, {nq} questions</small></span></a></li>'
    anchor = re.findall(r'<li><a href="Ellinika-(?:Science|Sport|Maths-Medicine|Greece-today|Polity|Music|Theatre-cinema|Orthodox-year)\.pdf">.*?</li>', t)[-1]
    t = t.replace(anchor, anchor + "\n" + li, 1)
open(p, "w", encoding="utf-8").write(t); touched.append("downloads/textbook/index.html")
print("\n".join(sorted(set(touched))))
