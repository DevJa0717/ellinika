/* Ελληνικά offline worker: used when the app is served from its own site and added to a home screen.
   The page shell is network-first; lessons, data and photos are served from cache and refreshed in the background. */
const CACHE = "ellinika-v1";
const SHELL = ["./", "index.html", "app.css", "profiles.js", "lookup.js", "library.js", "app.js", "manifest.webmanifest",
  "lessons/course.json", "img/manifest.json", "icons/icon-192.png", "icons/apple-touch-icon.png"];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => Promise.all(SHELL.map((u) => c.add(u).catch(() => {})))).then(() => self.skipWaiting()));
});
self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k.startsWith("ellinika-") && k !== CACHE).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});

const isShell = (url) => url.pathname.endsWith("/") || /\.(html|js|css|webmanifest)$/.test(url.pathname);

self.addEventListener("fetch", (e) => {
  const req = e.request, url = new URL(req.url);
  if (req.method !== "GET" || url.origin !== location.origin) return;
  if (req.mode === "navigate" || isShell(url)) {
    e.respondWith(fetch(req).then((r) => { if (r.ok) { const copy = r.clone(); caches.open(CACHE).then((c) => c.put(req, copy)); } return r; })
      .catch(() => caches.match(req, { ignoreSearch: true }).then((r) => r || caches.match("index.html"))));
    return;
  }
  e.respondWith(caches.open(CACHE).then(async (c) => {
    const hit = await c.match(req);
    const net = fetch(req).then((r) => { if (r.ok) c.put(req, r.clone()); return r; }).catch(() => hit || Response.error());
    if (hit) { e.waitUntil(net.catch(() => {})); return hit; }
    return net;
  }));
});

// The Profiles page can ask for every lesson and data file to be stored for offline use.
self.addEventListener("message", (e) => {
  if (e.data?.type !== "cache-all" || !Array.isArray(e.data.urls)) return;
  const port = e.ports[0];
  e.waitUntil(caches.open(CACHE).then(async (c) => {
    let done = 0;
    for (const u of e.data.urls) {
      if (!(await c.match(u))) await c.add(u).catch(() => {});
      done++; if (port && done % 10 === 0) port.postMessage({ done, total: e.data.urls.length });
    }
    if (port) port.postMessage({ done, total: e.data.urls.length, finished: true });
  }));
});
