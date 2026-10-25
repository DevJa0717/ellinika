"""Build the whole app as ONE .html file that works opened straight from a desktop (file://), offline.
Lessons, library, data and photos are packed inside it (gzip + base64) and served to the app through a fetch shim.
Also writes offline-files.json, the list the home-screen app uses for "Save everything for offline".
Usage: python3 tools/build_standalone.py [OUT_FILE]   (run from /mnt/project-files/app; default ../downloads/Ellinika.html)"""
import sys, os, re, json, gzip, base64, glob

out = sys.argv[1] if len(sys.argv) > 1 else "../downloads/Ellinika.html"

# What the app can request: (pack key as the app asks for it, file on disk)
files = []
for f in sorted(glob.glob("lessons/*.json")): files.append((f, f))
for f in sorted(glob.glob("library/**/*.json", recursive=True)): files.append((f, f))
files.append(("img/manifest.json", "img/manifest.json"))
for pat in ["grammar/*.json", "lexicon/*.json", "colloquial/*.json", "c1/syllabus/reading-tasks.json"]:
    for f in sorted(glob.glob("../data/" + pat)): files.append(("data/" + f[len("../data/"):], f))

pack, raw_total = {}, 0
for key, path in files:
    try: s = json.dumps(json.load(open(path, encoding="utf-8")), ensure_ascii=False, separators=(",", ":")).encode()
    except Exception as e: print("skip", path, e); continue
    raw_total += len(s)
    pack[key] = base64.b64encode(gzip.compress(s, 9, mtime=0)).decode()
images = {}
for f in sorted(glob.glob("img/*.jpg")):
    images[f] = "data:image/jpeg;base64," + base64.b64encode(open(f, "rb").read()).decode()

shim = """<script>
/* Packed course files for the single-file version: the app fetches them as if they were beside the page. */
window.__ELL_PACK = %s;
window.__ELL_IMG = %s;
(function () {
  const P = window.__ELL_PACK, I = window.__ELL_IMG, base = location.href.replace(/[#?].*$/, "").replace(/[^/]*$/, ""), done = {};
  const keyOf = (u) => { u = String(u).replace(/[#?].*$/, ""); if (u.startsWith(base)) u = u.slice(base.length); return u.replace(/^\\.\\//, ""); };
  function unpack(k) {
    if (!done[k]) { const b = Uint8Array.from(atob(P[k]), (c) => c.charCodeAt(0));
      done[k] = new Response(new Blob([b]).stream().pipeThrough(new DecompressionStream("gzip"))).text(); }
    return done[k];
  }
  const realFetch = window.fetch.bind(window);
  window.fetch = function (input, init) {
    const k = keyOf(typeof input === "string" ? input : input && input.url);
    if (P[k]) return unpack(k).then((t) => new Response(t, { status: 200, headers: { "Content-Type": "application/json" } }));
    if (/^(lessons|library|data|img)\\//.test(k) && location.protocol === "file:") return Promise.resolve(new Response("", { status: 404 }));
    return realFetch(input, init);
  };
  // Photos: swap img/… references for the packed copies as the app draws them.
  const fix = (el) => {
    if (el.tagName === "IMG") { const s = el.getAttribute("src"); if (s && I[s]) el.src = I[s]; }
    const st = el.getAttribute && el.getAttribute("style");
    if (st && st.includes("img/")) el.setAttribute("style", st.replace(/url\\((['"]?)(img\\/[^'")]+)\\1\\)/g, (m, q, p) => I[p] ? `url('${I[p]}')` : m));
  };
  new MutationObserver((ms) => { for (const m of ms) {
    if (m.type === "attributes") fix(m.target);
    else for (const n of m.addedNodes) if (n.nodeType === 1) { fix(n); n.querySelectorAll("img,[style*='img/']").forEach(fix); }
  } }).observe(document.documentElement, { subtree: true, childList: true, attributes: true, attributeFilter: ["src", "style"] });
})();
</script>
""" % (json.dumps(pack, separators=(",", ":")), json.dumps(images, separators=(",", ":")))

h = open("index.html", encoding="utf-8").read()
h = re.sub(r'\s*<link rel="manifest"[^>]*>', "", h)
h = re.sub(r'<link rel="stylesheet" href="app\.css(\?v=\w+)?">', lambda m: "<style>\n" + open("app.css", encoding="utf-8").read() + "\n</style>", h)
icon = "data:image/png;base64," + base64.b64encode(open("icons/favicon-64.png", "rb").read()).decode()
touch = "data:image/png;base64," + base64.b64encode(open("icons/apple-touch-icon.png", "rb").read()).decode()
h = re.sub(r'<link rel="icon"[^>]*>', f'<link rel="icon" href="{icon}">', h)
h = re.sub(r'<link rel="apple-touch-icon"[^>]*>', f'<link rel="apple-touch-icon" href="{touch}">', h)
first = True
for js in ["profiles.js", "lookup.js", "library.js", "app.js"]:
    m = re.search(r'<script src="%s(\?v=\w+)?"></script>' % re.escape(js), h)
    if not m: continue
    body = (shim if first else "") + "<script>\n" + open(js, encoding="utf-8").read().replace("</script", "<\\/script") + "\n</script>"
    h = h[:m.start()] + body + h[m.end():]
    first = False
os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
open(out, "w", encoding="utf-8").write(h)
json.dump({"files": [k for k in pack] + list(images)}, open("offline-files.json", "w"), separators=(",", ":"))
print(f"{out}: {os.path.getsize(out)/1e6:.1f} MB ({len(pack)} data files, {raw_total/1e6:.1f} MB unpacked; {len(images)} photos)")
