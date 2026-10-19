/* Ελληνικά offline worker: used when the app is served from its own site and added to a home screen.
   - The page itself is network-first, but gives up after a few seconds on a weak connection and opens the saved copy.
   - Scripts and styles open from the saved copy at once and refresh in the background for the next launch.
   - Lessons, data and photos live in a cache that survives app updates; each file is re-checked in the background,
     big word lists at most twice a day so the phone does not re-download megabytes on every launch.
   Bump CACHE whenever app.css/app.js/any script changes (with the ?v= in index.html). */
const CACHE = "ellinika-v25";
const DATA = "ellinika-data";
const FONTS = "ellinika-fonts";
const SHELL = ["./", "index.html", "app.css", "profiles.js", "lookup.js", "lookup-worker.js", "library.js", "app.js", "manifest.webmanifest",
  "icons/icon-192.png", "icons/apple-touch-icon.png"];
const PAGE_WAIT = 3500;            // ms before a slow network gives way to the saved page
const BIG = 300 * 1024, BIG_AGE = 12 * 36e5;

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then(async (c) => {
    // Store the exact ?v= URLs the page asks for, so the first offline launch finds them.
    let refs = [];
    try { const html = await (await fetch("index.html", { cache: "no-cache" })).text(); refs = [...html.matchAll(/(?:src|href)="([^":]+\.(?:js|css)(?:\?[^"]*)?)"/g)].map((m) => m[1]); } catch (err) { /* offline install */ }
    await Promise.all([...SHELL, ...refs].map((u) => c.add(new Request(u, { cache: "no-cache" })).catch(() => {})));
  }).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (e) => {
  e.waitUntil((async () => {
    const keep = [CACHE, DATA, FONTS];
    for (const k of await caches.keys()) {
      if (!k.startsWith("ellinika-") || keep.includes(k)) continue;
      // Versions before v8 kept lessons and data with the shell: drop only their shell files, so an offline copy is not lost
      // (data requests still look there until a fresh copy lands in DATA).
      const old = await caches.open(k), reqs = await old.keys(), shell = reqs.filter((r) => !isData(new URL(r.url)));
      if (shell.length === reqs.length) await caches.delete(k); else await Promise.all(shell.map((r) => old.delete(r)));
    }
    await self.clients.claim();
  })());
});

const isData = (url) => /\/(lessons|data|library|img)\//.test(url.pathname) || url.pathname.endsWith("offline-files.json");
const FONT_HOSTS = ["fonts.googleapis.com", "fonts.gstatic.com"];

// Saved copies carry the time they were fetched and their size, so re-checks can be spaced out.
async function store(cache, req, r) {
  if (!r.ok || r.type === "opaque") return r;
  const body = await r.clone().blob(), h = new Headers(r.headers);
  h.set("x-ell-at", String(Date.now())); h.set("x-ell-size", String(body.size)); h.set("x-ell-v", CACHE);
  await cache.put(req, new Response(body, { status: r.status, statusText: r.statusText, headers: h }));
  return r;
}
const stale = (hit, url) => {
  if (/\/img\/.+\.(jpe?g|png|webp)$/.test(url.pathname)) return false; // photos never change under the same name
  const at = +hit.headers.get("x-ell-at") || 0, size = +hit.headers.get("x-ell-size") || 0;
  return size < BIG || Date.now() - at > BIG_AGE;
};

self.addEventListener("fetch", (e) => {
  const req = e.request, url = new URL(req.url);
  if (req.method !== "GET") return;
  if (FONT_HOSTS.includes(url.hostname)) {
    e.respondWith(caches.open(FONTS).then(async (c) => (await c.match(req)) || fetch(req).then((r) => { if (r.ok || r.type === "opaque") c.put(req, r.clone()); return r; })));
    return;
  }
  if (url.origin !== location.origin) return;

  if (req.mode === "navigate") {
    e.respondWith(caches.open(CACHE).then(async (c) => {
      const net = fetch(req).then((r) => { if (r.ok) c.put("index.html", r.clone()); return r; });
      const saved = () => c.match("index.html").then((r) => r || c.match("./"));
      const timer = new Promise((res) => setTimeout(res, PAGE_WAIT)).then(saved);
      const r = await Promise.race([net.catch(saved), timer]);
      if (r) { e.waitUntil(net.catch(() => {})); return r; }
      return net.catch(saved).then((x) => x || Response.error());
    }));
    return;
  }

  if (isData(url)) {
    e.respondWith(caches.open(DATA).then(async (c) => {
      const hit = await c.match(req, { ignoreSearch: true }) || await caches.match(req, { ignoreSearch: true });
      const net = () => fetch(req).then((r) => store(c, req, r));
      if (!hit) return net();
      // First open of a lesson after an app update: try for the new copy, falling back to the saved one on a slow line.
      if (hit.headers.get("x-ell-v") !== CACHE && !(+hit.headers.get("x-ell-size") >= BIG) && stale(hit, url)) {
        const fresh = net().then((r) => (r.ok ? r : hit)).catch(() => hit);
        e.waitUntil(fresh);
        return Promise.race([fresh, new Promise((res) => setTimeout(() => res(hit), 2500))]);
      }
      if (stale(hit, url)) e.waitUntil(net().catch(() => {}));
      return hit;
    }));
    return;
  }

  // Scripts, styles, icons, manifest: saved copy first, refreshed in the background.
  e.respondWith(caches.open(CACHE).then(async (c) => {
    const hit = await c.match(req) || (url.search ? null : await c.match(req, { ignoreSearch: true }));
    const net = fetch(req).then((r) => { if (r.ok) c.put(req, r.clone()); return r; });
    if (hit) { e.waitUntil(net.catch(() => {})); return hit; }
    return net.catch(() => c.match(req, { ignoreSearch: true }).then((r) => r || Response.error()));
  }));
});

// The Profiles page can ask for every lesson and data file to be stored for offline use.
self.addEventListener("message", (e) => {
  if (e.data?.type !== "cache-all" || !Array.isArray(e.data.urls)) return;
  const port = e.ports[0];
  e.waitUntil(caches.open(DATA).then(async (c) => {
    let done = 0;
    for (const u of e.data.urls) {
      if (!(await c.match(u, { ignoreSearch: true }))) await fetch(u).then((r) => store(c, new Request(u), r)).catch(() => {});
      done++; if (port && done % 10 === 0) port.postMessage({ done, total: e.data.urls.length });
    }
    if (port) port.postMessage({ done, total: e.data.urls.length, finished: true });
  }));
});
