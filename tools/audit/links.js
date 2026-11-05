#!/usr/bin/env node
// Link and file check for the whole app (2026-11-05, "Validate all content end to end").
//   internal: "#shelf.id" / "#lesson-id" routes in JSON and markdown resolve to a library file, a lesson or a known route;
//             image/file paths ("file", "img", "image", "src") exist; offline-files.json and the sw.js SHELL list exist;
//             quiz items: answer among options, no duplicate options.
//   external (--web): every unique http(s) URL is fetched (HEAD, then GET); 404/410/DNS failures are reported.
//             403/429/5xx are "unverifiable" (bot walls), not failures. Results are cached in tools/audit/.url-cache.json.
// Usage: node tools/audit/links.js [--web] [paths...]   (default: library lessons data/c1 data/grammar)
const fs = require("fs"), path = require("path"), cp = require("child_process");
const ROOT = path.resolve(__dirname, "../..");
const args = process.argv.slice(2), WEB = args.includes("--web");
const targets = args.filter((a) => !a.startsWith("--")); if (!targets.length) targets.push("library", "lessons", "data/c1", "data/grammar");
const files = [];
const visit = (p) => { const st = fs.statSync(p); if (st.isDirectory()) for (const f of fs.readdirSync(p).sort()) visit(path.join(p, f)); else if (p.endsWith(".json")) files.push(p); };
for (const t of targets) visit(path.resolve(ROOT, t));
const exists = (p) => fs.existsSync(path.join(ROOT, p.split(/[?#]/)[0]));
const js = fs.readdirSync(ROOT).filter((f) => f.endsWith(".js")).map((f) => fs.readFileSync(path.join(ROOT, f), "utf8")).join("\n");
const routeOK = (r) => {
  const [head, rest] = r.replace(/^#/, "").split(/[.~]/, 2);
  if (!head) return true;
  if (exists(`lessons/${head}.json`)) return !rest || true;
  if (fs.existsSync(path.join(ROOT, "library", head))) {
    if (!rest || /^(review|weak|refs|drill|search|index|all|due|print)$/.test(rest)) return true;
    return exists(`library/${head}/${rest}.json`) || fs.readdirSync(path.join(ROOT, "library", head)).some((f) => f.startsWith(rest)) || new RegExp(`["']${rest}["']`).test(fs.readFileSync(path.join(ROOT, "library", head, fs.existsSync(path.join(ROOT, "library", head, "index.json")) ? "index.json" : fs.readdirSync(path.join(ROOT, "library", head))[0]), "utf8"));
  }
  return new RegExp(`["'#]${head}["'.~]`).test(js);
};
const bad = [], urls = new Map();
const note = (f, msg) => bad.push(`${path.relative(ROOT, f)}: ${msg}`);
for (const f of files) {
  let o; try { o = JSON.parse(fs.readFileSync(f, "utf8")); } catch (e) { note(f, "INVALID JSON " + e.message); continue; }
  const walk = (x, k) => {
    if (typeof x === "string") {
      const found = /^https?:\/\/\S+$/.test(x) ? [x] : [...x.matchAll(/https?:\/\/(?:[^\s"'<>()\]]|\([^\s()]*\))+/g)].map((m) => m[0].replace(/[.,;:]+$/, ""));
      for (const u of found) { if (!urls.has(u)) urls.set(u, new Set()); urls.get(u).add(path.relative(ROOT, f)); }
      const routes = [];
      if (/^#[a-z]/.test(x) && !/\s/.test(x) && !/^#[0-9a-f]{3,8}$/i.test(x)) routes.push(x);
      for (const m of x.matchAll(/\]\((#[a-z][^)\s]*)\)/g)) routes.push(m[1]);
      for (const r of routes) if (!routeOK(r)) note(f, `broken route ${r}`);
      if (/^(file|img|image|src|picture|thumb)$/.test(k) && !/^(https?:|data:)/.test(x) && /\.(jpe?g|png|svg|webp|gif|mp3|m4a|ogg|pdf)$/i.test(x) && !exists(x)) note(f, `missing file ${x}`);
    } else if (Array.isArray(x)) x.forEach((y) => walk(y, k));
    else if (x && typeof x === "object") {
      if (Array.isArray(x.options) && x.options.length > 1 && typeof x.answer === "string" && !/^[α-δa-d]$|\//.test(x.answer) && x.options.every((o) => typeof o === "string")) {
        if (!x.options.includes(x.answer)) note(f, `answer not among options: ${x.answer.slice(0, 60)}`);
        if (new Set(x.options).size !== x.options.length) note(f, `duplicate options: ${x.options.join(" | ").slice(0, 90)}`);
      }
      for (const [kk, v] of Object.entries(x)) walk(v, kk);
    }
  };
  walk(o, "");
}
// offline list and service-worker shell
const off = JSON.parse(fs.readFileSync(path.join(ROOT, "offline-files.json"), "utf8"));
for (const p of [].concat(off.files || off)) if (typeof p === "string" && !exists(p)) bad.push(`offline-files.json: missing ${p}`);
const shell = (fs.readFileSync(path.join(ROOT, "sw.js"), "utf8").match(/SHELL\s*=\s*\[([^\]]*)\]/) || [, ""])[1].match(/"([^"]+)"/g) || [];
for (const s of shell.map((x) => x.slice(1, -1))) if (s !== "./" && !exists(s)) bad.push(`sw.js SHELL: missing ${s}`);
// every library JSON reachable offline
const offSet = new Set([].concat(off.files || off));
for (const f of files.filter((f) => f.includes("/library/"))) { const r = path.relative(ROOT, f); if (!offSet.has(r) && !/\/src\//.test(r)) bad.push(`not in offline-files.json: ${r}`); }

console.log(`checked ${files.length} files, ${urls.size} external URLs: ${bad.length} internal problems`);
const byMsg = {}; for (const b of bad) { const k = b.replace(/: .*?: /, ": ").split(":")[1]; byMsg[k] = (byMsg[k] || 0) + 1; }
for (const b of bad.slice(0, 400)) console.log("  " + b);
if (bad.length > 400) console.log(`  … ${bad.length - 400} more`);

if (WEB) {
  const cacheF = path.join(__dirname, ".url-cache.json");
  const cache = fs.existsSync(cacheF) ? JSON.parse(fs.readFileSync(cacheF)) : {};
  const todo = [...urls.keys()].filter((u) => !(u in cache) || cache[u] === 0);
  const get = (u) => new Promise((res) => cp.execFile("curl", ["-s", "-o", "/dev/null", "-L", "-m", "20", "-A", "Mozilla/5.0 (ellinika link check)", "-w", "%{http_code}", u], (e, out) => res(parseInt(out) || 0)));
  (async () => {
    let i = 0; const N = 12;
    await Promise.all(Array.from({ length: N }, async () => { while (i < todo.length) { const u = todo[i++]; cache[u] = await get(u); if (i % 200 === 0) { fs.writeFileSync(cacheF, JSON.stringify(cache)); process.stderr.write(`${i}/${todo.length}\n`); } } }));
    fs.writeFileSync(cacheF, JSON.stringify(cache, null, 0));
    const dead = [...urls.keys()].filter((u) => [404, 410, 0].includes(cache[u]));
    const unver = [...urls.keys()].filter((u) => cache[u] >= 400 && ![404, 410].includes(cache[u]));
    console.log(`external: ${urls.size} URLs, ${dead.length} dead (404/410/no answer), ${unver.length} unverifiable (403/429/5xx)`);
    for (const u of dead) console.log(`  DEAD ${cache[u]} ${u}  ← ${[...urls.get(u)].slice(0, 3).join(", ")}`);
    process.exitCode = bad.length || dead.length ? 1 : 0;
  })();
} else process.exitCode = bad.length ? 1 : 0;
