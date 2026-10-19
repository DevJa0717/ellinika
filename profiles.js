/* Ελληνικά profiles: several learners on one device, each with their own saved progress.
   Loaded before every other script. It namespaces the app's "ellinika.*" storage keys per profile,
   so app.js and library.js keep reading and writing "ellinika.progress.v1" unchanged.
   Works from a web page, a home-screen app and a local .html file; backups move progress between devices. */
(function () {
  "use strict";

  const REG_KEY = "ellinika.profiles.v1";
  const SYNC_KEY = "ellinika.sync.v1", STASH_KEY = "ellinika.sync.stash";
  const SHARED = new Set([REG_KEY, SYNC_KEY, STASH_KEY]); // device-level keys, never per profile
  const SY = { applying: false, timer: 0, pushing: null }; // save-destination state for this page
  const LEGACY = "ellinika.progress.v1";
  const S = window.Storage && Storage.prototype;
  const raw = S ? { get: S.getItem, set: S.setItem, del: S.removeItem } : null;
  let ls = null; try { ls = window.localStorage; ls && raw.get.call(ls, REG_KEY); } catch (e) { ls = null; }
  const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const today = () => new Date().toISOString().slice(0, 10);
  const COLORS = ["#f2c14e", "#8be0a8", "#8fc4ff", "#ffa496", "#c9a6ff", "#7fe0e0", "#ffcf99", "#e6e6e6"];

  /* ---------- registry ---------- */
  function readReg() { try { return JSON.parse(raw.get.call(ls, REG_KEY)) || null; } catch (e) { return null; } }
  function writeReg(r) { try { raw.set.call(ls, REG_KEY, JSON.stringify(r)); changed(); } catch (e) { /* storage full or blocked */ } }
  const newId = () => "p" + Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
  const scoped = (key, id) => key + "~" + id;

  let reg = ls ? readReg() : null;
  if (ls && !reg) {
    // First run with profiles: whatever this browser already saved becomes the first profile.
    const id = newId();
    reg = { v: 1, active: id, ask: true, list: [{ id, name: "", color: COLORS[0], created: today() }] };
    const old = [], orphans = new Set();
    for (let i = 0; i < ls.length; i++) { const k = ls.key(i); if (!k || !k.startsWith("ellinika.") || SHARED.has(k)) continue; if (k.includes("~")) orphans.add(k.slice(k.lastIndexOf("~") + 1)); else old.push(k); }
    for (const k of old) raw.set.call(ls, scoped(k, id), raw.get.call(ls, k)); // the unscoped originals stay as a safety copy
    // Profile data whose list was lost (cleared or damaged) comes back as profiles rather than vanishing.
    let n = 1; for (const o of orphans) reg.list.push({ id: o, name: "Learner " + ++n, color: COLORS[(n - 1) % COLORS.length], created: today() });
    writeReg(reg);
  }
  if (reg && !reg.list.find((p) => p.id === reg.active)) { reg.active = reg.list[0].id; writeReg(reg); }

  // This tab keeps the profile it opened with, even if another tab switches.
  const ACTIVE = reg ? reg.active : null;
  let frozen = false; // set while switching, so a late save cannot land in the wrong profile

  if (ls && S) {
    const map = (k) => (typeof k === "string" && k.startsWith("ellinika.") && !SHARED.has(k) && !k.includes("~") ? scoped(k, ACTIVE) : k);
    S.getItem = function (k) { return this === ls ? raw.get.call(this, map(k)) : raw.get.call(this, k); };
    S.setItem = function (k, v) {
      if (this !== ls) return raw.set.call(this, k, v);
      if (frozen && map(k) !== k) return;
      const r = raw.set.call(this, map(k), v);
      if (map(k) !== k) changed();
      return r;
    };
    S.removeItem = function (k) { return this === ls ? raw.del.call(this, map(k)) : raw.del.call(this, k); };
  }

  /* ---------- profile data helpers ---------- */
  function profileKeys(id) {
    const out = [];
    for (let i = 0; i < ls.length; i++) { const k = ls.key(i); if (k && k.endsWith("~" + id) && k.startsWith("ellinika.")) out.push(k); }
    return out;
  }
  function progressOf(id) { try { return JSON.parse(raw.get.call(ls, scoped(LEGACY, id))) || {}; } catch (e) { return {}; } }
  function summary(p) {
    const lessons = Object.keys(p).filter((k) => p[k] && p[k].best != null).length;
    const vocab = p.vocab || {}, words = Object.keys(vocab).length;
    return { lessons, words };
  }
  function snapshot(id) {
    const keys = {};
    for (const k of profileKeys(id)) keys[k.slice(0, k.lastIndexOf("~"))] = raw.get.call(ls, k);
    return keys;
  }
  function restore(id, keys) {
    for (const k of profileKeys(id)) raw.del.call(ls, k);
    for (const [k, v] of Object.entries(keys || {})) if (k.startsWith("ellinika.") && !SHARED.has(k) && typeof v === "string") raw.set.call(ls, scoped(k, id), v);
  }
  const prof = (id) => reg.list.find((p) => p.id === id);
  const label = (p) => p.name || "Learner";
  const initial = (p) => (label(p).trim()[0] || "?").toUpperCase();

  function switchTo(id) {
    if (!prof(id)) return;
    reg = readReg() || reg; reg.active = id; prof(id).used = today(); writeReg(reg);
    frozen = true;
    try { sessionStorage.setItem("ellinika.picked", "1"); } catch (e) { /* ignore */ }
    location.hash = ""; location.reload();
  }

  /* ---------- backup files ---------- */
  async function saveFile(filename, data) {
    // claude.ai preview: downloads capability. Phones: the share sheet. Elsewhere: a plain download link.
    const dl = window.claude?.use ? await window.claude.use("downloads").catch(() => null) : null;
    if (dl) { await dl.save({ filename, data }); return "saved"; }
    const blob = new Blob([data], { type: "application/json" });
    const coarse = window.matchMedia && matchMedia("(pointer: coarse)").matches;
    if (coarse && navigator.canShare && window.File) {
      const file = new File([blob], filename, { type: "application/json" });
      if (navigator.canShare({ files: [file] })) {
        try { await navigator.share({ files: [file], title: filename }); return "saved"; }
        catch (e) { if (e && e.name === "AbortError") return "cancelled"; }
      }
    }
    const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = filename;
    document.body.append(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(a.href), 2000);
    return "saved";
  }
  function exportProfiles(ids) {
    const profiles = ids.map((id) => { const p = prof(id); return { name: label(p), color: p.color, created: p.created, keys: snapshot(id) }; });
    const progress = ids.length === 1 ? progressOf(ids[0]) : undefined; // single-profile files also restore through Library → Backup
    return JSON.stringify({ app: "ellinika", kind: "profiles", v: 1, saved: new Date().toISOString(), profiles, progress });
  }
  function markBackedUp(ids) { reg = readReg() || reg; for (const id of ids) if (prof(id)) prof(id).backup = today(); writeReg(reg); }
  // Accepts this file format and the older Library → Backup format ({app, progress}).
  function parseBackup(text) {
    const d = JSON.parse(text);
    if (!d || d.app !== "ellinika") throw new Error("this is not an Ελληνικά backup");
    if (Array.isArray(d.profiles)) return d.profiles.map((p) => ({ name: String(p.name || "Learner").slice(0, 40), color: p.color, keys: p.keys || {} }));
    if (d.progress && typeof d.progress === "object") return [{ name: "", keys: { [LEGACY]: JSON.stringify(d.progress) } }];
    throw new Error("the file has no progress in it");
  }

  /* ---------- styles ---------- */
  const css = `
.pf-chip { display: inline-flex; align-items: center; gap: 8px; margin-left: auto; padding: 3px 10px 3px 3px; border: 1px solid var(--line); border-radius: 999px; background: transparent; color: var(--ink); font: 600 0.8rem/1 var(--f-ui); cursor: pointer; text-decoration: none; align-self: center; }
.pf-chip:hover { border-color: var(--muted); }
.pf-dot { width: 26px; height: 26px; border-radius: 50%; display: inline-grid; place-items: center; font: 600 0.85rem/1 var(--f-ui); color: #0a2747; flex: none; }
.pf-dot.big { width: 44px; height: 44px; font-size: 1.2rem; }
.pf-chip-name { max-width: 9rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
@media (max-width: 480px) { .pf-chip-name { display: none; } .pf-chip { padding-right: 3px; } }
.bar:has(.pf-chip) { align-items: center; }
.bar:has(.pf-chip) .bar-meta { order: 2; }
.bar:has(.pf-chip) .pf-chip { order: 3; margin-left: 0; }
.pf-list { list-style: none; margin: 18px 0 12px; padding: 0; display: grid; gap: 10px; }
#view > .card { margin-top: 18px; }
#pf-editor:not(:empty) { margin-top: 18px; }
.pf-row { display: grid; grid-template-columns: auto 1fr auto; gap: 12px; align-items: center; padding: 12px; border: 1px solid var(--line); border-radius: 10px; background: var(--card); }
.pf-row.on { border-color: var(--terra); }
.pf-row .pf-name { font: 400 1.15rem/1.2 var(--f-display); }
.pf-row .pf-meta { font: 400 0.82rem/1.3 var(--f-ui); color: var(--muted); }
.pf-row-actions { display: flex; gap: 6px; flex-wrap: wrap; justify-content: flex-end; }
.pf-field { display: grid; gap: 6px; font: 500 0.85rem/1.3 var(--f-ui); color: var(--muted); }
.pf-field input[type=text] { padding: 10px 12px; border-radius: 8px; border: 1px solid var(--line); background: var(--paper); color: var(--ink); font: 400 1rem/1.2 var(--f-ui); }
.pf-colors { display: flex; gap: 8px; flex-wrap: wrap; }
.pf-colors button { width: 30px; height: 30px; border-radius: 50%; border: 2px solid transparent; cursor: pointer; }
.pf-colors button[aria-pressed=true] { border-color: var(--ink); }
.pf-toggle { display: flex; gap: 10px; align-items: center; font: 500 0.92rem/1.3 var(--f-ui); }
.pf-note { font: 400 0.85rem/1.45 var(--f-ui); color: var(--muted); margin: 0; }
.pf-warn { border-color: var(--warn); }
.pf-overlay { position: fixed; inset: 0; z-index: 50; background: var(--paper); display: grid; place-items: center; padding: max(16px, env(safe-area-inset-top, 0px)) 16px 16px; overflow: auto; }
.pf-picker { width: 100%; max-width: 30rem; display: grid; gap: 22px; text-align: center; }
.pf-picks { display: grid; grid-template-columns: repeat(auto-fit, minmax(7rem, 1fr)); gap: 12px; }
.pf-pick { display: grid; justify-items: center; gap: 8px; padding: 18px 8px; border: 1px solid var(--line); border-radius: 12px; background: var(--card); color: var(--ink); cursor: pointer; font: 400 1.05rem/1.2 var(--f-display); }
.pf-pick:hover, .pf-pick:focus-visible { border-color: var(--terra); }
.pf-banner { position: fixed; left: 50%; bottom: max(16px, env(safe-area-inset-bottom, 0px)); transform: translateX(-50%); z-index: 40; background: var(--card); border: 1px solid var(--terra); border-radius: 10px; padding: 10px 14px; font: 500 0.88rem/1.3 var(--f-ui); display: flex; gap: 10px; align-items: center; max-width: calc(100% - 32px); box-shadow: 0 10px 28px rgba(0,0,0,.35); }
`;
  function addStyle() { const s = document.createElement("style"); s.textContent = css; document.head.append(s); }

  /* ---------- header chip and start-up picker ---------- */
  const dot = (p, big) => `<span class="pf-dot${big ? " big" : ""}" style="background:${esc(p.color || COLORS[0])}" aria-hidden="true">${esc(initial(p))}</span>`;
  function addChip() {
    const bar = document.querySelector(".bar"); if (!bar || !reg) return;
    const p = prof(ACTIVE), a = document.createElement("a");
    a.className = "pf-chip"; a.href = "#profiles"; a.title = "Profiles · Προφίλ";
    a.setAttribute("aria-label", `Profile: ${label(p)}. Switch or manage profiles`);
    a.innerHTML = `${dot(p)}<span class="pf-chip-name">${esc(label(p))}</span>`;
    bar.append(a);
  }
  function refreshChip() { document.querySelector(".pf-chip")?.remove(); addChip(); }

  function picker() {
    let seen = false; try { seen = sessionStorage.getItem("ellinika.picked") === "1"; } catch (e) { seen = true; }
    if (!reg || !reg.ask || reg.list.length < 2 || seen || location.hash === "#profiles") return;
    const o = document.createElement("div");
    o.className = "pf-overlay"; o.setAttribute("role", "dialog"); o.setAttribute("aria-label", "Who's learning?");
    o.innerHTML = `<div class="pf-picker"><div><span class="eyebrow">Ελληνικά</span><h1 style="margin-top:6px">Ποιος μαθαίνει;</h1><p class="sub">Who's learning today?</p></div>
      <div class="pf-picks">${reg.list.map((p) => `<button class="pf-pick" data-id="${esc(p.id)}">${dot(p, true)}<span>${esc(label(p))}</span></button>`).join("")}</div>
      <p class="sub"><a href="#profiles" id="pf-manage">Manage profiles</a></p></div>`;
    document.body.append(o);
    const done = () => { try { sessionStorage.setItem("ellinika.picked", "1"); } catch (e) { /* ignore */ } o.remove(); };
    o.querySelectorAll(".pf-pick").forEach((b) => b.onclick = () => { if (b.dataset.id === ACTIVE) { reg.list.find((p) => p.id === ACTIVE).used = today(); writeReg(reg); done(); } else switchTo(b.dataset.id); });
    o.querySelector("#pf-manage").onclick = done;
    o.querySelector(".pf-pick")?.focus();
  }

  // Another tab switched profile: this tab still saves to its own, but say so.
  window.addEventListener("storage", (e) => {
    if (e.key !== REG_KEY || !ls) return;
    const r = readReg(); if (!r || r.active === ACTIVE || document.querySelector(".pf-banner")) return;
    const n = r.list.find((p) => p.id === r.active);
    const b = document.createElement("div"); b.className = "pf-banner";
    b.innerHTML = `<span>Another tab switched to ${esc(n ? label(n) : "another profile")}. This tab keeps saving for ${esc(label(prof(ACTIVE) || {}))}.</span><button class="btn small ghost">Switch here too</button>`;
    b.querySelector("button").onclick = () => { frozen = true; location.hash = ""; location.reload(); };
    document.body.append(b);
  });

  /* ---------- #profiles page ---------- */
  function where() {
    if (location.protocol === "file:") return "a file on this computer. Progress is kept by this browser for local files, so open the file with the same browser each time";
    if (window.matchMedia && matchMedia("(display-mode: standalone)").matches || navigator.standalone) return "the app on your home screen";
    return "this browser";
  }
  async function askPersist(msg) {
    if (!navigator.storage?.persist) return;
    try { const ok = (await navigator.storage.persisted()) || (await navigator.storage.persist()); if (msg && ok) msg.textContent = "This browser has agreed to keep the saved progress even when space runs low."; } catch (e) { /* not offered */ }
  }

  function renderPage() {
    const E = window.Ellinika, view = document.getElementById("view");
    document.title = "Profiles · Ελληνικά"; const meta = document.getElementById("bar-meta"); if (meta) meta.textContent = "Profiles";
    if (!ls || !reg) {
      view.innerHTML = `<p class="crumbs"><a href="#">← Course</a></p><h2>Profiles</h2><section class="card pf-warn"><p>This browser is not letting the app save anything (private browsing, or site data blocked), so progress will be lost when the page closes. Open the app in a normal window to keep progress and use profiles.</p></section>`;
      return;
    }
    reg = readReg() || reg;
    const stale = reg.list.filter((p) => { const s = summary(progressOf(p.id)); return (s.lessons || s.words) && (!p.backup || (Date.now() - Date.parse(p.backup)) / 864e5 > 14); });
    view.innerHTML = `<p class="crumbs"><a href="#">← Course</a></p>
      <span class="eyebrow">ΠΡΟΦΙΛ · profiles</span><h2>Who's learning</h2>
      <p class="sub">Each profile keeps its own lessons, word recall, notebook and scores. Progress is saved in ${esc(where())}.</p>
      <ul class="pf-list">${reg.list.map((p) => { const s = summary(progressOf(p.id)), on = p.id === ACTIVE;
        return `<li class="pf-row${on ? " on" : ""}">${dot(p, true)}<div><div class="pf-name">${esc(label(p))}${on ? ` <span class="chip done">active</span>` : ""}</div>
          <div class="pf-meta">${s.lessons} lesson${s.lessons === 1 ? "" : "s"} · ${s.words} word${s.words === 1 ? "" : "s"} in recall · ${p.backup ? "backed up " + esc(p.backup) : "never backed up"}</div></div>
          <div class="pf-row-actions">${on ? "" : `<button class="btn small" data-act="use" data-id="${esc(p.id)}">Switch</button>`}<button class="btn small ghost" data-act="edit" data-id="${esc(p.id)}">Edit</button></div></li>`; }).join("")}</ul>
      <div class="actions" style="justify-content:flex-start"><button class="btn ghost" id="pf-add">+ Add a profile</button></div>
      <div id="pf-editor"></div>
      <div id="pf-sync"></div>

      <section class="card${stale.length ? " pf-warn" : ""}"><h3>Backup by hand</h3>
        <p class="pf-note">Without a save destination, progress lives only on this device. A backup file keeps it safe and carries it to another device: save it here, then open the app there and restore it. It always has the same name, so saving to the same folder replaces the old copy. ${stale.length ? `<strong>${esc(stale.map(label).join(", "))}</strong> ${stale.length === 1 ? "has" : "have"} no backup from the last two weeks.` : ""}</p>
        <div class="actions" style="justify-content:flex-start"><button class="btn" id="pf-exp-one">Back up ${esc(label(prof(ACTIVE)))}</button>${reg.list.length > 1 ? `<button class="btn ghost" id="pf-exp-all">Back up all ${reg.list.length} profiles</button>` : ""}
          <label class="btn ghost">Restore from file<input type="file" id="pf-imp" accept="application/json,.json" hidden></label></div>
        <p class="pf-note" id="pf-msg" role="status"></p>
      </section>

      <section class="card"><h3>On this device</h3>
        <label class="pf-toggle"><input type="checkbox" id="pf-ask"${reg.ask ? " checked" : ""}> Ask who's learning when the app opens${reg.list.length < 2 ? " (once there are two profiles)" : ""}</label>
        <p class="pf-note">${installNote()}</p>
        <div id="pf-offline"></div>
        <p class="pf-note" id="pf-persist"></p>
      </section>`;

    const msg = view.querySelector("#pf-msg");
    view.querySelectorAll("[data-act=use]").forEach((b) => b.onclick = () => switchTo(b.dataset.id));
    view.querySelectorAll("[data-act=edit]").forEach((b) => b.onclick = () => editor(b.dataset.id));
    view.querySelector("#pf-add").onclick = () => editor(null);
    view.querySelector("#pf-ask").onchange = (e) => { reg = readReg() || reg; reg.ask = e.target.checked; writeReg(reg); };
    const doExport = async (ids, name) => {
      if (E && ids.includes(ACTIVE)) E.saveProgress();
      try {
        const r = await saveFile(name === "all-profiles" ? SYNC_FILE : `ellinika-${name}.json`, exportProfiles(ids));
        if (r === "saved") { markBackedUp(ids); msg.textContent = "Backup file saved. Keep it somewhere you can reach from your other devices."; setTimeout(renderPage, 1500); }
        else msg.textContent = "Not saved.";
      } catch (err) { msg.textContent = err?.code === "declined" ? "Not saved." : "Could not save: " + (err?.message || err); }
    };
    view.querySelector("#pf-exp-one").onclick = () => doExport([ACTIVE], slug(label(prof(ACTIVE))));
    const all = view.querySelector("#pf-exp-all"); if (all) all.onclick = () => doExport(reg.list.map((p) => p.id), "all-profiles");
    view.querySelector("#pf-imp").onchange = async (e) => {
      const f = e.target.files[0]; e.target.value = ""; if (!f) return;
      try { importer(parseBackup(await f.text()), f.name); } catch (err) { msg.textContent = "Could not restore: " + err.message; }
    };
    syncCard(view.querySelector("#pf-sync"));
    askPersist(view.querySelector("#pf-persist"));
    offlineButton(view.querySelector("#pf-offline"));
    window.scrollTo(0, 0);
  }
  const slug = (s) => s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9α-ω]+/g, "-").replace(/^-|-$/g, "") || "profile";

  function installNote() {
    if (location.protocol === "file:") return "Running from a file: everything works offline except videos. To use it on a phone, open the online version and add it to your home screen; move progress across with a backup file.";
    if (window.matchMedia && matchMedia("(display-mode: standalone)").matches || navigator.standalone) return "Installed on your home screen. Progress stays on this device; back it up now and then.";
    return "On a phone, use the browser's Share or menu button and choose <strong>Add to Home Screen</strong> to keep the app one tap away. Safari clears data from websites you have not opened for a few weeks, so the home-screen app plus an occasional backup is the safe way.";
  }

  // Home-screen app: store every lesson and data file now, so later lessons open without a connection.
  function offlineButton(box) {
    const sw = navigator.serviceWorker?.controller; if (!sw || !box) return;
    box.innerHTML = `<div class="actions" style="justify-content:flex-start"><button class="btn ghost small" id="pf-cache">Save every lesson for offline use</button><span class="pf-note" id="pf-cmsg"></span></div>`;
    box.querySelector("#pf-cache").onclick = async (e) => {
      const m = box.querySelector("#pf-cmsg"); e.target.disabled = true; m.textContent = "Preparing…";
      try {
        const list = (await (await fetch("offline-files.json")).json()).files;
        const root = window.Ellinika ? await window.Ellinika.dataRoot() : "data/";
        const urls = list.map((f) => f.startsWith("data/") ? root + f.slice(5) : f);
        const ch = new MessageChannel();
        ch.port1.onmessage = (ev) => { const d = ev.data; m.textContent = d.finished ? `All ${d.total} files saved; the app now works without a connection (videos excepted).` : `Saving ${d.done} of ${d.total}…`; };
        sw.postMessage({ type: "cache-all", urls }, [ch.port2]);
      } catch (err) { m.textContent = "Could not prepare the offline copy: " + err.message; e.target.disabled = false; }
    };
  }

  function editor(id) {
    const box = document.getElementById("pf-editor"), p = id ? prof(id) : null, isNew = !p;
    let color = p?.color || COLORS[reg.list.length % COLORS.length];
    const others = reg.list.length > 1;
    box.innerHTML = `<section class="card"><h3>${isNew ? "New profile" : "Edit " + esc(label(p))}</h3>
      <label class="pf-field">Name<input type="text" id="pf-name" maxlength="40" value="${esc(p?.name || "")}" placeholder="for example Devon" autocomplete="off"></label>
      <div class="pf-field">Colour<div class="pf-colors">${COLORS.map((c) => `<button type="button" data-c="${c}" style="background:${c}" aria-label="colour ${c}" aria-pressed="${c === color}"></button>`).join("")}</div></div>
      <div class="actions"><div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn" id="pf-ok">${isNew ? "Create" : "Save"}</button><button class="btn ghost" id="pf-cancel">Cancel</button></div>
      ${!isNew && others ? `<button class="btn small ghost" id="pf-del" style="border-color:var(--bad);color:var(--bad)">Delete profile</button>` : ""}</div>
      <p class="pf-note" id="pf-emsg"></p></section>`;
    const name = box.querySelector("#pf-name"); name.focus();
    box.querySelectorAll(".pf-colors button").forEach((b) => b.onclick = () => { color = b.dataset.c; box.querySelectorAll(".pf-colors button").forEach((x) => x.setAttribute("aria-pressed", x === b)); });
    box.querySelector("#pf-cancel").onclick = () => { box.innerHTML = ""; };
    box.querySelector("#pf-ok").onclick = () => {
      const n = name.value.trim();
      if (!n) { box.querySelector("#pf-emsg").textContent = "Give the profile a name."; return; }
      reg = readReg() || reg;
      if (isNew) { const nid = newId(); reg.list.push({ id: nid, name: n, color, created: today() }); writeReg(reg);
        if (confirm(`Switch to ${n} now?`)) return switchTo(nid); }
      else { Object.assign(prof(id), { name: n, color }); writeReg(reg); }
      refreshChip(); renderPage();
    };
    const del = box.querySelector("#pf-del");
    if (del) del.onclick = () => {
      const s = summary(progressOf(id));
      const typed = prompt(`Delete ${label(p)} and all of their progress (${s.lessons} lessons, ${s.words} words) from this device? This cannot be undone. Type DELETE to confirm.`);
      if (typed !== "DELETE") return;
      reg = readReg() || reg;
      for (const k of profileKeys(id)) raw.del.call(ls, k);
      reg.list = reg.list.filter((x) => x.id !== id);
      if (id === ACTIVE) { reg.active = reg.list[0].id; writeReg(reg); frozen = true; location.hash = ""; return location.reload(); }
      writeReg(reg); renderPage();
    };
    box.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  function importer(incoming, fname) {
    const box = document.getElementById("pf-editor");
    const rows = incoming.map((x, i) => { let s = { lessons: 0, words: 0 }; try { s = summary(JSON.parse(x.keys[LEGACY] || "{}")); } catch (e) { /* empty */ }
      const match = reg.list.find((p) => x.name && label(p).toLowerCase() === x.name.toLowerCase());
      return `<li class="pf-row"><span class="pf-dot big" style="background:${esc(x.color || COLORS[i % COLORS.length])}">${esc((x.name || "?")[0].toUpperCase())}</span>
        <div><div class="pf-name">${esc(x.name || "Backup")}</div><div class="pf-meta">${s.lessons} lessons · ${s.words} words in recall</div></div>
        <select data-i="${i}" class="pf-sel" style="max-width:12rem;padding:8px;border-radius:8px;background:var(--paper);color:var(--ink);border:1px solid var(--line)">
          <option value="new"${match ? "" : " selected"}>Add as a new profile</option>
          ${reg.list.map((p) => `<option value="${esc(p.id)}"${match && match.id === p.id ? " selected" : ""}>Replace ${esc(label(p))}</option>`).join("")}
          <option value="skip">Skip</option></select></li>`; }).join("");
    box.innerHTML = `<section class="card"><h3>Restore from ${esc(fname)}</h3><ul class="pf-list">${rows}</ul>
      <p class="pf-note">Replacing a profile overwrites the progress it has on this device with the progress in the file.</p>
      <div class="actions" style="justify-content:flex-start"><button class="btn" id="pf-go">Restore</button><button class="btn ghost" id="pf-cancel">Cancel</button></div></section>`;
    box.querySelector("#pf-cancel").onclick = () => { box.innerHTML = ""; };
    box.querySelector("#pf-go").onclick = () => {
      reg = readReg() || reg;
      let touchedActive = false;
      box.querySelectorAll(".pf-sel").forEach((sel) => {
        const x = incoming[+sel.dataset.i], v = sel.value;
        if (v === "skip") return;
        let id = v;
        if (v === "new") { id = newId(); reg.list.push({ id, name: x.name || "Learner " + (reg.list.length + 1), color: x.color || COLORS[reg.list.length % COLORS.length], created: today(), backup: today() }); }
        else { const p = prof(id); p.backup = today(); if (!p.name && x.name) p.name = x.name; if (id === ACTIVE) touchedActive = true; }
        restore(id, x.keys);
      });
      writeReg(reg);
      if (touchedActive) { frozen = true; location.hash = ""; return location.reload(); }
      refreshChip(); renderPage();
    };
    box.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  /* ---------- offline and home screen ---------- */
  function registerWorker() {
    // Only for the app served from its own site; local files and embedded previews skip it.
    if (!("serviceWorker" in navigator) || !/^https?:$/.test(location.protocol) || window.top !== window || window.__ELL_PACK) return;
    fetch("sw.js", { method: "HEAD" }).then((r) => { if (r.ok) navigator.serviceWorker.register("sw.js").catch(() => {}); }).catch(() => {});
  }

  /* ---------- save destination: one save file, overwritten in place, read back when the app opens ---------- */
  // Targets: a secret GitHub gist (works on every device, iPhone included) or a file on this computer (Chrome/Edge desktop).
  // The file holds every profile on the device; whichever side changed last wins, and the other side is kept for "Undo".
  const SYNC_FILE = "ellinika-progress.json";
  function syncCfg() { try { return JSON.parse(raw.get.call(ls, SYNC_KEY)) || {}; } catch (e) { return {}; } }
  function setSync(patch) { const c = Object.assign(syncCfg(), patch); try { raw.set.call(ls, SYNC_KEY, JSON.stringify(c)); } catch (e) { /* full */ } return c; }
  function changed() {
    if (SY.applying || !ls) return;
    const c = syncCfg(); if (!c.kind) return;
    if (!c.dirtyAt) setSync({ dirtyAt: new Date().toISOString() });
    clearTimeout(SY.timer); SY.timer = setTimeout(() => push().catch(() => {}), 4000);
  }
  function syncSnapshot() {
    const r = readReg() || reg;
    return { app: "ellinika", kind: "sync", v: 1, saved: new Date().toISOString(),
      profiles: r.list.map((p) => ({ id: p.id, name: label(p), color: p.color, created: p.created, keys: snapshot(p.id) })) };
  }
  // Make this device match a sync file exactly (profiles deleted elsewhere go here too).
  function applySnapshot(d) {
    SY.applying = true;
    try {
      const r = readReg() || reg, keep = new Set(d.profiles.map((p) => p.id));
      for (const p of r.list) if (!keep.has(p.id)) for (const k of profileKeys(p.id)) raw.del.call(ls, k);
      r.list = d.profiles.map((p) => { const old = r.list.find((x) => x.id === p.id) || {}; restore(p.id, p.keys);
        return Object.assign({}, old, { id: p.id, name: p.name === "Learner" && !old.name ? "" : p.name, color: p.color || old.color || COLORS[0], created: p.created || old.created || today() }); });
      if (!r.list.length) return;
      if (!r.list.find((p) => p.id === r.active)) r.active = r.list[0].id;
      raw.set.call(ls, REG_KEY, JSON.stringify(r)); reg = r;
    } finally { SY.applying = false; }
  }
  const validSync = (d) => d && d.app === "ellinika" && Array.isArray(d.profiles) && d.profiles.every((p) => p && typeof p.id === "string" && p.keys);

  // IndexedDB keeps the file handle (handles cannot go in localStorage).
  function idb(mode, fn) {
    return new Promise((res, rej) => { const o = indexedDB.open("ellinika-sync", 1);
      o.onupgradeneeded = () => o.result.createObjectStore("h");
      o.onsuccess = () => { const t = o.result.transaction("h", mode), q = fn(t.objectStore("h")); t.oncomplete = () => res(q && q.result); t.onerror = () => rej(t.error); };
      o.onerror = () => rej(o.error); });
  }
  const getHandle = () => idb("readonly", (s) => s.get("file"));
  const putHandle = (h) => idb("readwrite", (s) => (h ? s.put(h, "file") : s.delete("file")));

  const GH = "https://api.github.com";
  const ghHead = (t) => ({ Authorization: "Bearer " + t, Accept: "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28" });
  async function gh(path, opt = {}) {
    const c = syncCfg(), r = await fetch(GH + path, Object.assign({ cache: "no-store" }, opt, { headers: Object.assign(ghHead(opt.token || c.token), opt.body ? { "Content-Type": "application/json" } : {}) }));
    if (r.status === 401) throw new Error("GitHub did not accept the token (it may have expired)");
    if (r.status === 404) throw new Error("the save file on GitHub was not found");
    if (!r.ok) throw new Error("GitHub answered " + r.status);
    return r.json();
  }
  const target = {
    gist: {
      async read() {
        const g = await gh(`/gists/${syncCfg().gistId}`), f = g.files && g.files[SYNC_FILE]; if (!f) return null;
        const text = f.truncated ? await (await fetch(f.raw_url, { cache: "no-store" })).text() : f.content;
        return text ? JSON.parse(text) : null;
      },
      write: (text) => gh(`/gists/${syncCfg().gistId}`, { method: "PATCH", body: JSON.stringify({ files: { [SYNC_FILE]: { content: text } } }) }),
      label: () => "a secret gist on your GitHub account",
    },
    file: {
      async handle(ask) {
        const h = await getHandle(); if (!h) throw new Error("no save file is linked");
        let p = await h.queryPermission({ mode: "readwrite" });
        if (p !== "granted" && ask) p = await h.requestPermission({ mode: "readwrite" });
        if (p !== "granted") { const e = new Error("the browser needs your OK to open " + h.name); e.needsTap = true; throw e; }
        return h;
      },
      async read(ask) { const t = await (await (await this.handle(ask)).getFile()).text(); return t.trim() ? JSON.parse(t) : null; },
      async write(text, ask) { const w = await (await this.handle(ask)).createWritable(); await w.write(text); await w.close(); },
      label: () => "a file on this computer",
    },
  };

  async function push(ask) {
    const c = syncCfg(); if (!c.kind || !target[c.kind]) return;
    if (SY.pushing) return SY.pushing;
    SY.pushing = (async () => {
      const startedDirty = c.dirtyAt, d = syncSnapshot();
      try {
        await target[c.kind].write(JSON.stringify(d), ask);
        const now = syncCfg(); setSync({ lastRemote: d.saved, lastOk: d.saved, err: null, dirtyAt: now.dirtyAt === startedDirty ? null : now.dirtyAt });
        reg = readReg() || reg; for (const p of reg.list) p.backup = today(); raw.set.call(ls, REG_KEY, JSON.stringify(reg));
        syncStatus();
      } catch (e) { setSync({ err: e.message, needsTap: !!e.needsTap }); syncStatus(); throw e; }
      finally { SY.pushing = null; }
    })();
    return SY.pushing;
  }

  // On opening: read the save file; take it if it is newer than this device, otherwise write this device's progress to it.
  async function pull(ask) {
    const c = syncCfg(); if (!c.kind || !target[c.kind]) return "off";
    let d;
    try { d = await target[c.kind].read(ask); } catch (e) { setSync({ err: e.message, needsTap: !!e.needsTap }); syncStatus(); return "error"; }
    setSync({ err: null, needsTap: false });
    if (!d) { await push(ask).catch(() => {}); return "pushed"; }
    if (!validSync(d)) { setSync({ err: "the save file is not an Ελληνικά progress file" }); syncStatus(); return "error"; }
    const fresh = !c.lastRemote || d.saved > c.lastRemote;
    if (!fresh) { if (c.dirtyAt) await push(ask).catch(() => {}); else setSync({ lastOk: new Date().toISOString() }); syncStatus(); return "same"; }
    if (c.dirtyAt && c.dirtyAt > d.saved) { // both changed; this device's change is the later one
      try { raw.set.call(ls, STASH_KEY, JSON.stringify({ at: new Date().toISOString(), from: "save file", snap: d })); } catch (e) { /* full */ }
      await push(ask).catch(() => {}); return "pushed";
    }
    if (c.dirtyAt) try { raw.set.call(ls, STASH_KEY, JSON.stringify({ at: new Date().toISOString(), from: "this device", snap: syncSnapshot() })); } catch (e) { /* full */ }
    applySnapshot(d); setSync({ lastRemote: d.saved, lastOk: new Date().toISOString(), dirtyAt: null });
    return "applied";
  }

  function syncStatus() {
    const el = document.getElementById("pf-sync-status"); if (el) el.innerHTML = syncLine();
    const c = syncCfg(), bar = document.querySelector(".pf-banner.sync");
    if (c.kind === "file" && c.needsTap && !bar) {
      const b = document.createElement("div"); b.className = "pf-banner sync";
      b.innerHTML = `<span>Your progress is saved to a file. Allow the app to open it again.</span><button class="btn small">Open save file</button>`;
      b.querySelector("button").onclick = async () => { b.remove(); const r = await pull(true); if (r === "applied") reloadAfterSync(); };
      document.body.append(b);
    } else if (bar && !c.needsTap) bar.remove();
  }
  function syncLine() {
    const c = syncCfg(); if (!c.kind) return "Not set: progress is only on this device.";
    const t = (iso) => iso ? new Date(iso).toLocaleString([], { dateStyle: "medium", timeStyle: "short" }) : "never";
    return `Saving to ${esc(target[c.kind].label())}${c.kind === "file" && c.fileName ? ` (<strong>${esc(c.fileName)}</strong>)` : ""}. Last saved ${esc(t(c.lastOk))}.${c.dirtyAt ? " Changes waiting to be saved." : ""}${c.err ? ` <span style="color:var(--bad)">Problem: ${esc(c.err)}.</span>` : ""}`;
  }
  function reloadAfterSync() {
    try { sessionStorage.setItem("ellinika.picked", sessionStorage.getItem("ellinika.picked") || ""); sessionStorage.setItem("ellinika.synced", "1"); } catch (e) { /* ignore */ }
    frozen = true; location.reload();
  }
  async function syncOnOpen() {
    if (!ls || !syncCfg().kind) return;
    let once = false; try { once = sessionStorage.getItem("ellinika.synced") === "1"; sessionStorage.removeItem("ellinika.synced"); } catch (e) { /* ignore */ }
    if (once) { toast("Progress loaded from your save file."); syncStatus(); return; }
    if ((await pull(false)) === "applied") reloadAfterSync(); else syncStatus();
  }
  function toast(t) {
    const b = document.createElement("div"); b.className = "pf-banner"; b.textContent = t; document.body.append(b); setTimeout(() => b.remove(), 3500);
  }
  // Leaving or hiding the app (iPhone home screen): save straight away instead of waiting.
  document.addEventListener("visibilitychange", () => { if (document.visibilityState === "hidden" && syncCfg().dirtyAt) { clearTimeout(SY.timer); push().catch(() => {}); } });
  window.addEventListener("online", () => { if (syncCfg().dirtyAt) push().catch(() => {}); });

  // The "Save destination" card on #profiles.
  function syncCard(box) {
    if (!box) return;
    const c = syncCfg(), canFile = !!window.showSaveFilePicker, stash = (() => { try { return JSON.parse(raw.get.call(ls, STASH_KEY)); } catch (e) { return null; } })();
    box.innerHTML = `<section class="card"><h3>Save destination</h3>
      <p class="pf-note">Pick one place for the save file. Every change is written over that same file, and each time the app opens it loads the file if another device saved something newer.</p>
      <p class="pf-note" id="pf-sync-status" role="status">${syncLine()}</p>
      ${c.kind ? `<div class="actions" style="justify-content:flex-start"><button class="btn small" id="sy-now">Save now</button><button class="btn small ghost" id="sy-pull">Load from save file</button><button class="btn small ghost" id="sy-off">Stop using it</button></div>` : `
      <div class="actions" style="justify-content:flex-start"><button class="btn" id="sy-gh">GitHub (any device, iPhone too)</button>${canFile ? `<button class="btn ghost" id="sy-new">New file on this computer</button><button class="btn ghost" id="sy-open">Existing file on this computer</button>` : ""}</div>
      <p class="pf-note">${canFile ? "" : "This browser cannot keep writing to a file on the device (iPhone and iPad browsers do not allow it), so GitHub is the automatic option here. "}Backups saved by hand use the fixed name <strong>${SYNC_FILE}</strong>, so the Files app offers to replace the old copy.</p>`}
      ${stash ? `<p class="pf-note">The last sync replaced progress from ${esc(stash.from)} (${esc(new Date(stash.at).toLocaleString())}). <button class="btn small ghost" id="sy-undo">Undo that</button></p>` : ""}
      <div id="sy-form"></div><p class="pf-note" id="sy-msg" role="status"></p></section>`;
    const msg = box.querySelector("#sy-msg"), $b = (id) => box.querySelector(id);
    const fail = (e) => { msg.textContent = "Could not use it: " + (e?.message || e); };
    // Linking: the destination may already hold progress from another device.
    async function link(kind, extra) {
      setSync(Object.assign({ kind, lastRemote: null, lastOk: null, err: null, needsTap: false, dirtyAt: null }, extra));
      let d = null; try { d = await target[kind].read(true); } catch (e) { setSync({ kind: null }); return fail(e); }
      if (d && validSync(d) && d.profiles.length) {
        const names = d.profiles.map((p) => p.name).join(", ");
        $b("#sy-form").innerHTML = `<p class="pf-note">The save file already holds progress for <strong>${esc(names)}</strong> (saved ${esc(new Date(d.saved).toLocaleString())}).</p>
          <div class="actions" style="justify-content:flex-start"><button class="btn small" id="sy-take">Load it onto this device</button><button class="btn small ghost" id="sy-mine">Replace it with this device's progress</button></div>`;
        $b("#sy-take").onclick = () => { try { raw.set.call(ls, STASH_KEY, JSON.stringify({ at: new Date().toISOString(), from: "this device", snap: syncSnapshot() })); } catch (e) { /* full */ }
          applySnapshot(d); setSync({ lastRemote: d.saved, lastOk: new Date().toISOString() }); reloadAfterSync(); };
        $b("#sy-mine").onclick = () => push(true).then(renderPage, fail);
        return;
      }
      await push(true).then(renderPage, fail);
    }
    if ($b("#sy-gh")) $b("#sy-gh").onclick = () => {
      $b("#sy-form").innerHTML = `<ol class="pf-note" style="padding-left:1.2em;margin:0;display:grid;gap:6px">
          <li>Open <a href="https://github.com/settings/tokens/new?scopes=gist&amp;description=Ellinika%20progress" target="_blank" rel="noopener">GitHub → new token</a> (it opens with only the <strong>gist</strong> box ticked). Set the expiry to <strong>No expiration</strong> or a long one, then <strong>Generate token</strong> and copy it.</li>
          <li>Paste it here. It stays in this browser and can only touch your gists. On your other devices, paste the same token.</li></ol>
        <label class="pf-field">GitHub token<input type="text" id="sy-tok" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="ghp_…"></label>
        <div class="actions" style="justify-content:flex-start"><button class="btn small" id="sy-go">Connect</button></div>`;
      $b("#sy-go").onclick = async () => {
        const token = $b("#sy-tok").value.trim(); if (!token) return;
        msg.textContent = "Connecting…";
        try {
          // Reuse the save file another device already made, else create a secret gist.
          let id = null;
          for (let page = 1; page <= 5 && !id; page++) {
            const list = await gh(`/gists?per_page=100&page=${page}`, { token });
            id = (list.find((g) => g.files && g.files[SYNC_FILE]) || {}).id || null; if (list.length < 100) break;
          }
          if (!id) id = (await gh("/gists", { token, method: "POST", body: JSON.stringify({ description: "Ελληνικά progress (saved by the app)", public: false, files: { [SYNC_FILE]: { content: "{}" } } }) })).id;
          msg.textContent = ""; await link("gist", { token, gistId: id });
        } catch (e) { fail(e); }
      };
      $b("#sy-tok").focus();
    };
    if ($b("#sy-new")) $b("#sy-new").onclick = async () => {
      try { const h = await showSaveFilePicker({ suggestedName: SYNC_FILE, types: [{ description: "Ελληνικά progress", accept: { "application/json": [".json"] } }] });
        await putHandle(h); setSync({ kind: "file", fileName: h.name, lastRemote: null, dirtyAt: null }); await push(true); renderPage(); }
      catch (e) { if (e?.name !== "AbortError") fail(e); }
    };
    if ($b("#sy-open")) $b("#sy-open").onclick = async () => {
      try { const [h] = await showOpenFilePicker({ types: [{ description: "Ελληνικά progress", accept: { "application/json": [".json"] } }] });
        await putHandle(h); await link("file", { fileName: h.name }); }
      catch (e) { if (e?.name !== "AbortError") fail(e); }
    };
    if ($b("#sy-now")) $b("#sy-now").onclick = () => { msg.textContent = "Saving…"; push(true).then(() => { msg.textContent = "Saved."; }, fail); };
    if ($b("#sy-pull")) $b("#sy-pull").onclick = async () => { msg.textContent = "Loading…"; const r = await pull(true); if (r === "applied") reloadAfterSync(); else msg.textContent = r === "error" ? "" : "This device already has the latest progress."; };
    if ($b("#sy-off")) $b("#sy-off").onclick = async () => {
      if (!confirm("Stop saving to this destination? The progress stays on this device and in the save file.")) return;
      try { raw.del.call(ls, SYNC_KEY); await putHandle(null).catch(() => {}); } catch (e) { /* ignore */ }
      renderPage();
    };
    if ($b("#sy-undo")) $b("#sy-undo").onclick = () => {
      if (!confirm(`Put back the progress from ${stash.from} as it was on ${new Date(stash.at).toLocaleString()}?`)) return;
      applySnapshot(stash.snap); raw.del.call(ls, STASH_KEY); setSync({ dirtyAt: new Date().toISOString(), lastRemote: new Date().toISOString() });
      push(true).catch(() => {}).then(reloadAfterSync);
    };
  }

  /* ---------- wiring ---------- */
  (window.EllinikaAddons = window.EllinikaAddons || {}).profiles = renderPage;
  window.EllinikaProfiles = { active: ACTIVE, list: () => (reg ? reg.list.slice() : []), switchTo, saveNow };
  // "Save & quit": write the save file now and say where it went.
  async function saveNow() {
    window.Ellinika?.saveProgress?.();
    const c = syncCfg();
    if (!c.kind) { toast("Saved on this device. Choose a save destination under Profiles to keep a copy elsewhere."); return "local"; }
    clearTimeout(SY.timer);
    try { await push(true); toast(c.kind === "gist" ? "Progress saved to GitHub." : `Progress saved to ${c.fileName || "your save file"}.`); return "saved"; }
    catch (e) { toast("Saved on this device; the save file could not be written: " + e.message); return "error"; }
  }
  const start = () => { addStyle(); addChip(); picker(); registerWorker(); syncOnOpen().catch(() => {}); };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
