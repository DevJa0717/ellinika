"""Bundle the app into one folder for an Artifact preview: page with inlined CSS/JS, plus lessons/ and data/.
Usage: python3 tools/bundle_preview.py OUT_DIR   (run from /mnt/project-files/app)"""
import sys, re, os, shutil, glob
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
h = open("index.html").read()
h = re.sub(r"<!doctype html>\s*<html[^>]*>\s*<head>\s*", "", h)
h = re.sub(r'<meta charset[^>]*>\s*<meta name="viewport"[^>]*>\s*', "", h)
h = re.sub(r'<link rel="stylesheet" href="app\.css(\?v=\w+)?">', lambda m: "<style>\n" + open("app.css").read() + "\n</style>", h)
h = h.replace('<link rel="stylesheet" href="app.css">', "<style>\n" + open("app.css").read() + "\n</style>")
h = re.sub(r'<script src="profiles\.js(\?v=\w+)?"></script>', lambda m: "<script>\n" + open("profiles.js").read() + "\n</script>", h)
h = re.sub(r'<script src="lookup\.js(\?v=\w+)?"></script>', lambda m: "<script>\n" + open("lookup.js").read() + "\n</script>", h)
h = re.sub(r'<script src="library\.js(\?v=\w+)?"></script>', lambda m: "<script>\n" + open("library.js").read() + "\n</script>", h)
h = re.sub(r'<script src="app\.js(\?v=\w+)?"></script>', lambda m: "<script>\n" + open("app.js").read() + "\n</script>", h)
h = re.sub(r"</head>\s*<body>\s*", "", h)
h = re.sub(r"</body>\s*</html>\s*$", "", h)
open(os.path.join(out, "index.html"), "w").write(h)
shutil.copytree("lessons", os.path.join(out, "lessons"), dirs_exist_ok=True)
shutil.copytree("img", os.path.join(out, "img"), dirs_exist_ok=True)
shutil.copytree("icons", os.path.join(out, "icons"), dirs_exist_ok=True)
for f in ["manifest.webmanifest", "sw.js", "offline-files.json"]:
    if os.path.exists(f): shutil.copy(f, out)
if os.path.isdir("library"): shutil.copytree("library", os.path.join(out, "library"), dirs_exist_ok=True)
shutil.copytree("../data", os.path.join(out, "data"), dirs_exist_ok=True)
print("\n".join(sorted(os.path.relpath(p, out) for p in glob.glob(out + "/**/*.json", recursive=True))))
