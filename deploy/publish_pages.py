"""Mirror the whole project folder into a clone of github.com/DevJa0717/ellinika, which GitHub Pages serves from main at
https://devja0717.github.io/ellinika/ (the only host; Netlify was retired on 2026-10-25).

Usage: python3 /mnt/project-files/deploy/publish_pages.py REPO_DIR
Then in REPO_DIR: git add -A && git commit -m "..." && git push origin main (or a branch + PR).

Repo layout (project path -> repo path):
  app/*            -> /            (the site itself: index.html, scripts, lessons/, library/, img/ ...)
  app/tools/       -> tools/app/   (build helpers, not part of the site)
  data/            -> data/        (everything, including build intermediates, PDFs and MP3s)
  downloads/       -> downloads/   (textbook PDFs, Ellinika.html single-file build)
  deploy/ ledger/ plan/ screens/ tools/ .notes/ -> same names
uploads/ is left out: it holds the original uploaded books (copyrighted), and the repo is public.
Files in the repo that no longer exist in the project are deleted, except .git, .github, .nojekyll and README.md.
offline-files.json ("Save every lesson for offline use") is regenerated from the runtime JSON and photos."""
import os, sys, json, shutil, filecmp

ROOT = "/mnt/project-files"
if len(sys.argv) < 2: sys.exit(__doc__)
REPO = os.path.abspath(sys.argv[1])
KEEP = {".git", ".github", ".nojekyll", "README.md"}
SKIP_NAMES = {"__pycache__", ".DS_Store", "ellinika-netlify.zip", "netlify.toml", "_headers"}

def walk(src, dst_prefix):
    for dirpath, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in SKIP_NAMES]
        for f in files:
            if f in SKIP_NAMES or f.endswith(".pyc"): continue
            p = os.path.join(dirpath, f)
            yield p, os.path.normpath(os.path.join(dst_prefix, os.path.relpath(p, src)))

plan = {}
for p, rel in walk(ROOT + "/app", "."):
    if rel.startswith("tools/"): rel = "tools/app/" + rel[len("tools/"):]
    plan[rel] = p
for d in ("data", "downloads", "deploy", "ledger", "plan", "screens", "tools", ".notes"):
    if os.path.isdir(f"{ROOT}/{d}"):
        for p, rel in walk(f"{ROOT}/{d}", d): plan[rel] = p
plan.pop("offline-files.json", None)

# Runtime files the app saves for offline use (same rule as the old desktop build).
def runtime(rel):
    if rel.endswith(".jpg"): return rel.startswith(("img/", "data/"))
    if not rel.endswith(".json"): return False
    if rel.startswith("data/"):
        return not rel.startswith(("data/lexicon/build/", "data/colloquial/parts/", "data/colloquial/tools/"))
    return not rel.startswith(("tools/", "deploy/", "plan/", "ledger/", "downloads/", "library/classics/src/"))
offline = sorted(r for r in plan if runtime(r))

bad = []
for r in offline:
    if r.endswith(".json"):
        try: json.load(open(plan[r], encoding="utf-8"))
        except Exception as e: bad.append(f"{r}: {e}")
if bad: print("WARNING invalid JSON:\n  " + "\n  ".join(bad))

copied = removed = 0
for rel, src in plan.items():
    dst = os.path.join(REPO, rel)
    if os.path.exists(dst) and filecmp.cmp(src, dst, shallow=False): continue
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst); copied += 1
with open(os.path.join(REPO, "offline-files.json"), "w", encoding="utf-8") as f:
    json.dump({"files": offline}, f, ensure_ascii=False)
wanted = set(plan) | {"offline-files.json"}
for dirpath, dirs, files in os.walk(REPO, topdown=True):
    if dirpath == REPO: dirs[:] = [d for d in dirs if d not in KEEP]
    for f in files:
        rel = os.path.relpath(os.path.join(dirpath, f), REPO)
        if rel in KEEP or rel in wanted: continue
        os.remove(os.path.join(dirpath, f)); removed += 1
for dirpath, dirs, files in os.walk(REPO, topdown=False):
    if ".git" not in dirpath.split(os.sep) and dirpath != REPO and not os.listdir(dirpath): os.rmdir(dirpath)
print(f"{REPO}: {len(plan) + 1} files ({copied} updated, {removed} removed), offline list {len(offline)} files")
