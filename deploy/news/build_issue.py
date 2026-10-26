"""Build one issue of the graded news digest (#digest) from its source and register it in the archive.

Usage (from the repo root):
  python3 deploy/news/build_issue.py 2026-10-26          # build library/digest/2026-10-26.json + index + offline list
  python3 deploy/news/build_issue.py 2026-10-26 --check  # then run the checker

Source of an issue, either of:
  deploy/news/src/<date>/*.py   each module defines STORIES = [story(...), ...] (helpers in deploy/news/src/helpers.py)
  deploy/news/src/<date>.json   {"stories": [...]} in the same story format (see deploy/news/README.md)
Story modules are read in file-name order, so a.py, b.py, c.py give the issue order.

Tap lookup: forms the app's lexicon does not know get a per-issue gloss from deploy/news/gloss.txt
(one line per form: "form<TAB>lemma — English"). After building, the checker lists remaining MISS forms;
add them to gloss.txt and build again until there are none.

Archive: every issue stays in library/digest/ and in library/digest/index.json (newest first). Only the newest
OFFLINE_KEEP issues are put on the "save everything for offline use" list, so a phone does not store a year of news.
If /mnt/project-files/app exists (a project thread), the digest files are mirrored there too."""
import os, sys, re, json, glob, shutil, subprocess, importlib.util
sys.dont_write_bytecode = True  # keep __pycache__ out of the repo
from datetime import date as Date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "library", "digest")
OFFLINE_KEEP = 7
SECTIONS = [("ellada", "Ελλάδα", "Greece"), ("europi", "Ευρώπη", "Europe"), ("kosmos", "Κόσμος", "World"),
            ("oikonomia", "Οικονομία", "Economy"), ("epistimi", "Επιστήμη και περιβάλλον", "Science and environment"),
            ("politismos", "Πολιτισμός", "Culture"), ("athlitismos", "Αθλητισμός", "Sport")]
DAYS = ["Δευτέρα", "Τρίτη", "Τετάρτη", "Πέμπτη", "Παρασκευή", "Σάββατο", "Κυριακή"]
MONTHS = ["Ιανουαρίου", "Φεβρουαρίου", "Μαρτίου", "Απριλίου", "Μαΐου", "Ιουνίου", "Ιουλίου", "Αυγούστου", "Σεπτεμβρίου", "Οκτωβρίου", "Νοεμβρίου", "Δεκεμβρίου"]

def el_date(d):
    return f"{DAYS[d.weekday()]} {d.day} {MONTHS[d.month - 1]} {d.year}"

def load_stories(day):
    src = os.path.join(HERE, "src", day)
    if os.path.isfile(src + ".json"):
        return json.load(open(src + ".json", encoding="utf-8"))["stories"]
    sys.path.insert(0, os.path.join(HERE, "src"))
    stories = []
    for f in sorted(glob.glob(os.path.join(src, "*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        stories += m.STORIES
    if not stories: sys.exit(f"no stories found in {src}/*.py or {src}.json")
    return stories

def read_gloss():
    g = {}
    p = os.path.join(HERE, "gloss.txt")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.rstrip("\n")
            if not line.strip() or line.startswith("#"): continue
            form, _, val = line.partition("\t")
            if val: g[form.strip()] = val.strip()
    return g

TOK = re.compile(r"[Ͱ-Ͽἀ-῿]+")
def texts(s):
    for v in s["levels"].values():
        yield v["el"]
        for p in v["paras"]: yield p["el"]
        for g in v["glossary"]: yield g["el"]
        for q in v["questions"]: yield q["q"]; yield from q["options"]
    if s.get("grammar"):
        for x in s["grammar"]["examples"]: yield x["el"]
    yield from s.get("vocab", [])

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    day = args[0] if args else Date.today().isoformat()
    d = Date.fromisoformat(day)
    stories = load_stories(day)
    order = {k: i for i, (k, _, _) in enumerate(SECTIONS)}
    stories.sort(key=lambda s: order.get(s["section"], 99))  # stable: keeps source order inside a section
    gloss_all, used = read_gloss(), set()
    for s in stories:
        for t in texts(s): used.update(TOK.findall(t))
    gloss = {k: v for k, v in gloss_all.items() if k in used}
    issue = {"id": day, "date": day, "date_el": el_date(d), "sections": [{"id": k, "el": e, "en": n} for k, e, n in SECTIONS if any(s["section"] == k for s in stories)],
             "stories": stories, "gloss": gloss}
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, day + ".json"), "w", encoding="utf-8") as f: json.dump(issue, f, ensure_ascii=False, indent=1)

    idx_p = os.path.join(OUT, "index.json")
    idx = json.load(open(idx_p, encoding="utf-8")) if os.path.exists(idx_p) else {}
    idx.update({"kind": "digest", "el": "Ειδήσεις σε τρία επίπεδα", "title": "News digest: current affairs rewritten at B1, B2 and C1, a new issue every morning",
                "intro_el": "Κάθε πρωί, οι σημαντικότερες ειδήσεις από την Ελλάδα και τον κόσμο, γραμμένες από την αρχή σε τρία επίπεδα: Β1, Β2 και Γ1. Διαλέξτε επίπεδο, πατήστε όποια λέξη δεν ξέρετε και λύστε τις ερωτήσεις.",
                "intro_en": "Every morning, the main news from Greece and the world, rewritten from scratch at three levels (B1, B2, C1) with a glossary and questions for each. Each story links to the reports it is based on."})
    issues = [i for i in idx.get("issues", []) if i["id"] != day]
    issues.append({"id": day, "file": day + ".json", "date": day, "el": el_date(d), "count": len(stories),
                   "lead": stories[0]["levels"]["B2"]["el"], "lead_en": stories[0]["levels"]["B2"]["title"]})
    issues.sort(key=lambda i: i["id"], reverse=True)
    idx["issues"] = issues
    with open(idx_p, "w", encoding="utf-8") as f: json.dump(idx, f, ensure_ascii=False, indent=1)

    # Offline list: keep only the newest issues on it.
    off_p = os.path.join(ROOT, "offline-files.json")
    if os.path.exists(off_p):
        off = json.load(open(off_p, encoding="utf-8"))
        keep = {"library/digest/index.json"} | {"library/digest/" + i["file"] for i in issues[:OFFLINE_KEEP]}
        files = [x for x in off["files"] if not x.startswith("library/digest/")] + sorted(keep)
        off["files"] = sorted(set(files))
        with open(off_p, "w", encoding="utf-8") as f: json.dump(off, f, ensure_ascii=False)

    words = sum(len(p["el"].split()) for s in stories for v in s["levels"].values() for p in v["paras"])
    print(f"library/digest/{day}.json: {len(stories)} stories, {words} Greek words, {len(gloss)} glossed forms; archive {len(issues)} issues")

    mirror = "/mnt/project-files/app/library/digest"
    if os.path.isdir("/mnt/project-files/app/library"):
        os.makedirs(mirror, exist_ok=True)
        for f in (day + ".json", "index.json"): shutil.copyfile(os.path.join(OUT, f), os.path.join(mirror, f))

    if "--check" in sys.argv:
        r = subprocess.run(["node", os.path.join(HERE, "check_issue.js"), os.path.join(OUT, day + ".json")])
        sys.exit(r.returncode)

if __name__ == "__main__":
    main()
