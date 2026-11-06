/* Ελληνικά frequency-ranked vocabulary course (#lexi).
   #lexi             all 38 bands of 500 words (every word of the lexicon, most frequent first), totals, due reviews
   #lexi.<n>         one band: progress, study session, recognition quiz, word list
   #lexi.review      every production review that is due, from all bands
   Data in library/lexi/ (built by tools/lexi/build.py from data/lexicon/). Progress is shared with the lessons' word
   recall in progress.vocab (localStorage "ellinika.progress.v1", per profile): a word counts as known only when it is
   produced English → Greek and still recalled 90+ days on; recognition (Greek → English) is counted separately in
   v.rec / v.recTry and never makes a word known. Course settings live in "ellinika.lexi.v1". */
(function () {
  "use strict";
  const A = () => window.Ellinika;
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});
  const BASE = "library/lexi/";
  const KEY = "ellinika.lexi.v1";
  const KNOWN_DAYS = 90;
  const HEAD = "Λεξιλόγιο κατά συχνότητα";
  const PDF = (vol) => `downloads/textbook/Ellinika-Vocabulary-${String(vol).padStart(2, "0")}.pdf`;
  const POS_EN = { noun: "noun", verb: "verb", adjective: "adjective", adverb: "adverb", pronoun: "pronoun", conjunction: "conjunction",
    preposition: "preposition", particle: "particle", numeral: "numeral", article: "article", other: "expression" };

  const CSS = `
.lx-hero h2 { margin: 0; font: 400 2rem/1.15 var(--f-display); }
.lx-hero p { margin: 6px 0 0; }
.lx-stats { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; margin: 14px 0; }
@media (max-width: 420px) { .lx-stats { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
.lx-stat { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 10px 6px; text-align: center; min-width: 0; }
.lx-stat b { display: block; font: 400 1.5rem/1.1 var(--f-display); font-variant-numeric: tabular-nums; }
.lx-stat span { font: 500 .72rem/1.2 var(--f-ui); color: var(--muted); }
.lx-acts { display: flex; flex-wrap: wrap; gap: 8px; margin: 4px 0 14px; }
.lx-bands { display: grid; gap: 10px; grid-template-columns: repeat(auto-fill, minmax(min(100%, 230px), 1fr)); margin: 12px 0 20px; }
.lx-band { display: grid; gap: 5px; text-decoration: none; color: var(--ink); background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 12px 14px; min-width: 0; }
.lx-band .el { font: 400 1.2rem/1.2 var(--f-display); }
.lx-band .smp { font-size: .92rem; color: var(--muted); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.lx-band .meta { display: flex; justify-content: space-between; gap: 8px; font: 500 .76rem/1.2 var(--f-ui); color: var(--muted); }
.lx-band.cur { border-color: var(--terra); box-shadow: 0 0 0 1px var(--terra) inset; }
.lx-meter { position: relative; height: 6px; border-radius: 3px; background: var(--paper); overflow: hidden; }
.lx-meter i { position: absolute; left: 0; top: 0; bottom: 0; }
.lx-meter i.r { background: var(--terra); opacity: .45; }
.lx-meter i.k { background: var(--good); }
.lx-legend { display: flex; gap: 14px; flex-wrap: wrap; font: 500 .76rem/1.2 var(--f-ui); color: var(--muted); }
.lx-legend i { display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin-right: 5px; vertical-align: -1px; }
.lx-chips { display: flex; flex-wrap: wrap; gap: 6px; }
.lx-chips button { border: 1px solid var(--line); background: transparent; color: var(--ink); border-radius: 999px; padding: 8px 12px; min-height: 36px; font: 500 .85rem/1 var(--f-ui); cursor: pointer; }
.lx-chips button[aria-pressed="true"] { background: var(--ink); color: var(--paper); border-color: var(--ink); }
.lx-list { list-style: none; margin: 10px 0 0; padding: 0; display: grid; }
.lx-list li { border-bottom: 1px solid var(--line); }
.lx-row { all: unset; box-sizing: border-box; cursor: pointer; display: grid; grid-template-columns: 3.2em minmax(0, 1fr) auto; gap: 2px 10px; align-items: baseline; width: 100%; padding: 9px 2px; }
.lx-row .rk { font: 500 .74rem/1 var(--f-ui); color: var(--muted); font-variant-numeric: tabular-nums; }
.lx-row .w { font-size: 1.12rem; overflow-wrap: anywhere; }
.lx-row .g { grid-column: 2 / 4; font: 400 .86rem/1.3 var(--f-ui); color: var(--muted); }
.lx-more { padding: 0 2px 12px 3.6em; display: grid; gap: 6px; font-size: .95rem; }
.lx-more .h { font: 500 .8rem/1.3 var(--f-ui); color: var(--muted); }
.lx-st { font: 600 .68rem/1 var(--f-ui); letter-spacing: .04em; text-transform: uppercase; border-radius: 999px; padding: 4px 7px; white-space: nowrap; }
.lx-st.known { background: var(--good); color: #fff; }
.lx-st.recall { background: var(--terra); color: #10233b; }
.lx-st.rec { border: 1px solid var(--line); color: var(--muted); }
.lx-card { gap: 12px; }
.lx-top { display: flex; justify-content: space-between; align-items: center; gap: 8px; font: 500 .8rem/1.2 var(--f-ui); color: var(--muted); }
.lx-bar { height: 4px; background: var(--paper); border-radius: 2px; overflow: hidden; }
.lx-bar i { display: block; height: 100%; background: var(--terra); transition: width .2s; }
.lx-task { font: 600 .8rem/1.3 var(--f-ui); letter-spacing: .06em; text-transform: uppercase; color: var(--terra); }
.lx-big { font: 400 2.2rem/1.15 var(--f-display); overflow-wrap: anywhere; }
.lx-en { font: 400 1.45rem/1.25 var(--f-display); color: var(--aegean); overflow-wrap: anywhere; }
.lx-pos { font: 500 .85rem/1.3 var(--f-ui); color: var(--muted); }
.lx-opts { display: grid; gap: 8px; }
.lx-opts button { text-align: left; border: 1px solid var(--line); background: var(--card); color: var(--ink); border-radius: 10px; padding: 12px 14px; min-height: 48px; font: 400 1rem/1.3 var(--f-ui); cursor: pointer; }
.lx-opts button.right { border-color: var(--good); box-shadow: inset 0 0 0 1px var(--good); }
.lx-opts button.wrong { border-color: var(--bad); box-shadow: inset 0 0 0 1px var(--bad); }
.lx-card .answer-row input { font-size: 1.25rem; }
.lx-info { display: grid; gap: 6px; border-left: 3px solid var(--terra); padding: 4px 0 4px 12px; }
.lx-info .hd { font: 500 .82rem/1.3 var(--f-ui); color: var(--muted); }
.lx-info .ex { font-size: 1.02rem; line-height: 1.45; }
.lx-info .ex small, .lx-more small { display: block; color: var(--muted); font: italic 400 .88rem/1.35 var(--f-ui); }
.lx-col { list-style: none; margin: 0; padding: 0; display: grid; gap: 3px; font-size: .95rem; }
.lx-col span { color: var(--muted); font: 400 .85rem/1.3 var(--f-ui); }
.lx-hint { font: 500 .95rem/1.3 var(--f-ui); color: var(--muted); letter-spacing: .12em; }
.lx-say { all: unset; cursor: pointer; font-size: 1.1rem; padding: 2px 8px; border-radius: 8px; border: 1px solid var(--line); vertical-align: middle; margin-left: 6px; }
.lx-foot { display: flex; justify-content: space-between; gap: 8px; flex-wrap: wrap; }
.lx-set { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; font: 500 .85rem/1.3 var(--f-ui); color: var(--muted); }
`;
  if (!document.getElementById("lx-css")) { const st = document.createElement("style"); st.id = "lx-css"; st.textContent = CSS; document.head.appendChild(st); }

  /* ---------- storage ---------- */
  const settings = () => { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } };
  const saveSettings = (s) => { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) { /* storage unavailable */ } };
  const vstore = () => { const p = A().progress; return p.vocab || (p.vocab = {}); };
  // Same schedule as the lessons' word recall (app.js vocabGrade): ×2.5 per correct recall, ×1.5 if only the accent was off.
  function gradeProd(lemma, result) {
    const vs = vstore(), now = Date.now();
    const v = vs[lemma] || (vs[lemma] = { ivl: 0, reps: 0, lapses: 0, rec: 0, seen: now });
    if (result === "wrong") { v.lapses++; v.ivl = 0; v.due = now + 10 * 6e4; }
    else { v.reps++; v.ivl = v.ivl ? Math.round(v.ivl * (result === "almost" ? 1.5 : 2.5)) : 1; v.due = now + v.ivl * 864e5 - 4 * 36e5; v.last = now; }
    A().saveProgress();
  }
  // Recognition is tracked on its own; a first recognition schedules the word for production in 10 minutes (as in lessons).
  function gradeRec(lemma, ok, schedule) {
    const vs = vstore(), now = Date.now();
    const v = vs[lemma] || (vs[lemma] = { ivl: 0, reps: 0, lapses: 0, rec: 0, seen: now });
    v.recTry = (v.recTry || 0) + 1; if (ok) v.rec = (v.rec || 0) + 1; v.recLast = now;
    if (schedule && !v.due) v.due = now + 10 * 6e4;
    A().saveProgress();
  }
  const status = (l) => {
    const v = vstore()[l];
    if (!v) return "new";
    if (v.ivl >= KNOWN_DAYS) return "known";
    if (v.reps > 0 && v.ivl > 0) return "recall";
    if (v.due || v.reps || v.lapses) return "learning";
    if (v.rec > 0) return "rec";
    return "new";
  };
  const isDue = (l, now) => { const v = vstore()[l]; return !!(v && v.due && v.due <= now); };

  /* ---------- data ---------- */
  let idxP = null, lemP = null; const bandP = {};
  const index = () => (idxP = idxP || A().getJSON(BASE + "index.json"));
  const lemmas = () => (lemP = lemP || A().getJSON(BASE + "lemmas.json"));
  const band = (n) => (bandP[n] = bandP[n] || A().getJSON(`${BASE}band-${String(n).padStart(2, "0")}.json`));

  /* ---------- helpers ---------- */
  const esc = (s) => A().esc(s == null ? "" : String(s));
  const shuffle = (a) => { const b = a.slice(); for (let i = b.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [b[i], b[j]] = [b[j], b[i]]; } return b; };
  const uniq = (a) => [...new Set(a)];
  const withArt = (w) => (w.a ? `${w.a} ${w.l}` : w.l);
  const fmt = (n) => n.toLocaleString("en-GB");
  const grade = (input, forms) => (window.__ellinika?.grade ? window.__ellinika.grade(input, forms) : (String(input).trim() === forms[0] ? "right" : "wrong"));
  const stripAcc = (s) => s.normalize("NFD").replace(/[̀-ͯ]/g, "").normalize("NFC");
  const elVoice = () => (window.speechSynthesis?.getVoices() || []).find((v) => /^el(-|_|$)/i.test(v.lang));
  function say(text) {
    const ss = window.speechSynthesis; if (!ss) return;
    ss.cancel(); const u = new SpeechSynthesisUtterance(text); u.lang = "el-GR"; const v = elVoice(); if (v) u.voice = v; u.rate = 0.9; ss.speak(u);
  }
  const sayBtn = (text) => (window.speechSynthesis ? `<button class="lx-say" type="button" data-say="${esc(text)}" aria-label="Listen">🔊</button>` : "");
  const bindSay = (root) => root.querySelectorAll("[data-say]").forEach((b) => { b.onclick = (e) => { e.preventDefault(); e.stopPropagation(); say(b.dataset.say); }; });
  const wrap = (sel) => { try { const el = typeof sel === "string" ? A().$(sel) : sel; if (el) A().wrapGreek(el); } catch (e) { /* lookup optional */ } };
  function info(w) {
    return `<div class="lx-info">
      ${w.h ? `<div class="hd" lang="el">${esc(w.h)}</div>` : ""}
      ${w.x ? `<div class="ex lx-gk"><span lang="el">${esc(w.x[0])}</span>${sayBtn(w.x[0])}<small>${esc(w.x[1])}</small></div>` : ""}
      ${w.c?.length ? `<ul class="lx-col lx-gk">${w.c.map((c) => `<li><span lang="el" style="color:var(--ink);font:inherit">${esc(c[0])}</span> <span>${esc(c[1])}</span></li>`).join("")}</ul>` : ""}
    </div>`;
  }
  const chip = (st) => ({ known: `<span class="lx-st known">known</span>`, recall: `<span class="lx-st recall">in recall</span>`, learning: `<span class="lx-st rec">learning</span>`, rec: `<span class="lx-st rec">recognised</span>` }[st] || "");

  async function bandCounts() {
    const L = await lemmas(), now = Date.now();
    return L.map((ls) => {
      const c = { known: 0, recall: 0, rec: 0, seen: 0, due: 0, total: ls.length };
      for (const l of ls) {
        const st = status(l);
        if (st === "known") c.known++;
        if (st === "known" || st === "recall") c.recall++;
        if ((vstore()[l]?.rec || 0) > 0) c.rec++;
        if (st !== "new") c.seen++;
        if (isDue(l, now)) c.due++;
      }
      return c;
    });
  }

  /* ---------- #lexi ---------- */
  async function renderHome() {
    const E = A();
    document.title = `${HEAD} · Ελληνικά`; E.$("#bar-meta").textContent = "Vocabulary course";
    E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><p class="sub">Loading the word bands…</p>`;
    const [ix, counts] = await Promise.all([index(), bandCounts()]);
    const tot = counts.reduce((a, c) => ({ known: a.known + c.known, recall: a.recall + c.recall, rec: a.rec + c.rec, due: a.due + c.due, seen: a.seen + c.seen }), { known: 0, recall: 0, rec: 0, due: 0, seen: 0 });
    const cur = (counts.findIndex((c) => c.seen < c.total) + 1) || ix.bands.length;
    const st = settings();
    E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p>
      <section class="lx-hero"><h2 lang="el">${HEAD}</h2>
        <p>All ${fmt(ix.total)} words of the app's dictionary, most frequent first, in ${ix.bands.length} bands of ${ix.band}. Each new word is met once as a recognition question (Greek → English), then you type it in Greek from the English. A word counts as <b>known</b> only when you can still produce it 90+ days after you learnt it; recognising it is tracked separately.</p></section>
      <div class="lx-stats">
        <div class="lx-stat"><b>${fmt(tot.known)}</b><span>known (produced)</span></div>
        <div class="lx-stat"><b>${fmt(tot.recall)}</b><span>in recall</span></div>
        <div class="lx-stat"><b>${fmt(tot.rec)}</b><span>recognised</span></div>
        <div class="lx-stat"><b>${fmt(tot.due)}</b><span>due now</span></div>
      </div>
      <div class="lx-acts">
        <a class="btn" href="#lexi.${cur}">${tot.seen ? "Continue" : "Start"}: words ${fmt(ix.bands[cur - 1].from)}–${fmt(ix.bands[cur - 1].to)}</a>
        ${tot.due ? `<a class="btn ghost" href="#lexi.review">Review all due (${fmt(tot.due)})</a>` : ""}
      </div>
      <div class="lx-set">New words per session: <span class="lx-chips" id="lx-per">${[5, 10, 15, 20].map((n) => `<button type="button" data-n="${n}" aria-pressed="${(st.per || 10) === n}">${n}</button>`).join("")}</span></div>
      <h3>Bands</h3>
      <div class="lx-legend"><span><i style="background:var(--good)"></i>known</span><span><i style="background:var(--terra);opacity:.45"></i>in recall</span></div>
      <div class="lx-bands">${ix.bands.map((b, i) => { const c = counts[i]; return `<a class="lx-band${i + 1 === cur ? " cur" : ""}" href="#lexi.${b.n}">
          <span class="el" lang="el">Λέξεις ${fmt(b.from)}–${fmt(b.to)}</span>
          <span class="smp" lang="el">${esc(b.sample.slice(0, 6).join(", "))}</span>
          <span class="lx-meter"><i class="r" style="width:${(c.recall / c.total) * 100}%"></i><i class="k" style="width:${(c.known / c.total) * 100}%"></i></span>
          <span class="meta"><span>${c.known} known · ${c.recall} in recall</span><span>${c.due ? `${c.due} due` : esc(topCefr(b.cefr))}</span></span></a>`; }).join("")}</div>
      <section class="card"><h3>Printable word books</h3><p class="sub">One PDF per 1,000 words (two bands), with every word, its grammar, an example and common combinations, plus a self-test page per band.</p>
        <p class="lx-chips">${Array.from({ length: Math.ceil(ix.bands.length / 2) }, (_, v) => `<a class="btn small ghost" href="${PDF(v + 1)}" target="_blank" rel="noopener">${fmt(v * 1000 + 1)}–${fmt(Math.min((v + 1) * 1000, ix.total))}</a>`).join("")}</p></section>`;
    E.$("#lx-per").onclick = (e) => { const b = e.target.closest("button"); if (!b) return; const s = settings(); s.per = +b.dataset.n; saveSettings(s); E.$("#lx-per").querySelectorAll("button").forEach((x) => x.setAttribute("aria-pressed", x === b)); };
    window.scrollTo(0, 0);
  }
  const topCefr = (c) => { const tot = Object.values(c).reduce((a, b) => a + b, 0); return Object.entries(c).filter(([k]) => k !== "?").sort((a, b) => b[1] - a[1]).slice(0, 2).map(([k, n]) => `${k} ${Math.round((n / tot) * 100)}%`).join(" · "); };

  /* ---------- #lexi.<n> ---------- */
  async function renderBand(n, filter = "all") {
    const E = A();
    const ix = await index(), b = ix.bands[n - 1];
    if (!b) { location.hash = "lexi"; return; }
    const words = await band(n), now = Date.now();
    const st = words.map((w) => status(w.l));
    const c = { known: st.filter((s) => s === "known").length, recall: st.filter((s) => s === "known" || s === "recall").length,
      rec: words.filter((w) => (vstore()[w.l]?.rec || 0) > 0).length, fresh: st.filter((s) => s === "new" || s === "rec").length, due: words.filter((w) => isDue(w.l, now)).length };
    const per = settings().per || 10;
    document.title = `Λέξεις ${b.from}–${b.to} · Ελληνικά`; E.$("#bar-meta").textContent = "Vocabulary course";
    const shown = words.map((w, i) => [w, st[i]]).filter(([w, s]) => filter === "all" || (filter === "new" ? s === "new" || s === "rec" : filter === "recall" ? s === "recall" || s === "learning" : s === filter));
    E.view.innerHTML = `<p class="crumbs"><a href="#lexi">← ${HEAD}</a></p>
      <section class="lx-hero"><h2 lang="el">Λέξεις ${fmt(b.from)}–${fmt(b.to)}</h2><p class="sub">Band ${n} of ${ix.bands.length} · ${esc(topCefr(b.cefr))} · ${Object.entries(b.pos).map(([k, v]) => `${v} ${POS_EN[k] || k}${v === 1 ? "" : "s"}`).join(", ")}</p></section>
      <div class="lx-stats">
        <div class="lx-stat"><b>${c.known}</b><span>known</span></div>
        <div class="lx-stat"><b>${c.recall}</b><span>in recall</span></div>
        <div class="lx-stat"><b>${c.rec}</b><span>recognised</span></div>
        <div class="lx-stat"><b>${c.due}</b><span>due now</span></div>
      </div>
      <div class="lx-acts">
        ${c.fresh ? `<a class="btn" href="#lexi.${n}.learn">Learn ${Math.min(per, c.fresh)} new${c.due ? ` + ${Math.min(c.due, 20)} due` : ""}</a>` : ""}
        ${c.due ? `<a class="btn${c.fresh ? " ghost" : ""}" href="#lexi.${n}.due">Review due (${c.due})</a>` : ""}
        <a class="btn ghost" href="#lexi.${n}.quiz">Recognition quiz</a>
        ${n < ix.bands.length ? `<a class="btn ghost" href="#lexi.${n + 1}">Next band →</a>` : ""}
      </div>
      <section class="card"><div class="lx-foot"><h3 style="margin:0">Word list</h3><a class="btn small ghost" href="${PDF(Math.ceil(n / 2))}" target="_blank" rel="noopener">PDF</a></div>
        <div class="lx-chips" id="lx-filt">${[["all", `All ${words.length}`], ["new", `New ${c.fresh}`], ["recall", "Learning"], ["known", `Known ${c.known}`]].map(([k, t]) => `<button type="button" data-f="${k}" aria-pressed="${filter === k}">${t}</button>`).join("")}</div>
        <ul class="lx-list" id="lx-list">${shown.map(([w, s]) => `<li><button class="lx-row" type="button" data-l="${esc(w.l)}"><span class="rk">${w.r}</span><span class="w" lang="el">${esc(withArt(w))}</span>${chip(s) || "<span></span>"}<span class="g">${esc(w.g)}</span></button></li>`).join("") || `<li class="sub" style="padding:10px 0">No words here yet.</li>`}</ul></section>`;
    E.$("#lx-filt").onclick = (e) => { const t = e.target.closest("button"); if (t) renderBand(n, t.dataset.f); };
    const byL = new Map(words.map((w) => [w.l, w]));
    E.$("#lx-list").onclick = (e) => {
      const row = e.target.closest(".lx-row"); if (!row) return;
      const li = row.parentElement, open = li.querySelector(".lx-more");
      if (open) { open.remove(); return; }
      const w = byL.get(row.dataset.l), d = document.createElement("div"); d.className = "lx-more";
      d.innerHTML = `<div>${sayBtn(withArt(w))} <span class="h">${esc(POS_EN[w.p] || w.p)}</span></div>${info(w)}`;
      li.appendChild(d); bindSay(d); d.querySelectorAll(".lx-gk").forEach(wrap);
    };
    window.scrollTo(0, 0);
  }

  /* ---------- sessions ---------- */
  function mcItem(w, pool) {
    const same = pool.filter((x) => x.p === w.p && x.g !== w.g && x.l !== w.l);
    const others = (same.length >= 3 ? same : pool.filter((x) => x.g !== w.g && x.l !== w.l));
    const opts = shuffle(uniq([w.g, ...shuffle(others).slice(0, 6).map((x) => x.g)]).slice(0, 4));
    if (!opts.includes(w.g)) opts[0] = w.g;
    return { kind: "rec", w, opts: shuffle(opts) };
  }
  const prodItem = (w) => ({ kind: "prod", w, forms: uniq([withArt(w), w.l, ...(w.alt || [])]) });

  async function session(mode, n) {
    const E = A(), now = Date.now(), per = settings().per || 10;
    const ix = await index();
    let pool = [], back = "#lexi", title = "Review";
    if (mode === "review") {
      const L = await lemmas(), due = [];
      L.forEach((ls, i) => ls.forEach((l) => { if (isDue(l, now)) due.push([i + 1, l]); }));
      due.sort((a, b) => (vstore()[a[1]].due || 0) - (vstore()[b[1]].due || 0));
      const pick = due.slice(0, 30), bands = uniq(pick.map((d) => d[0]));
      const loaded = await Promise.all(bands.map(band));
      const by = new Map(loaded.flat().map((w) => [w.l, w]));
      pool = loaded.flat();
      const items = pick.map((d) => by.get(d[1])).filter(Boolean).map(prodItem);
      return run(items, pool, "#lexi", "Review: all bands");
    }
    const b = ix.bands[n - 1]; if (!b) { location.hash = "lexi"; return; }
    pool = await band(n); back = `#lexi.${n}`; title = `Λέξεις ${fmt(b.from)}–${fmt(b.to)}`;
    const due = pool.filter((w) => isDue(w.l, now)).sort((a, x) => vstore()[a.l].due - vstore()[x.l].due);
    if (mode === "quiz") {
      // Recognition only: Greek → English, mostly words already met, topped up with new ones. Never makes a word known.
      const met = pool.filter((w) => status(w.l) !== "new"), fresh = pool.filter((w) => status(w.l) === "new");
      const pick = shuffle(met).slice(0, 20); for (const w of fresh) { if (pick.length >= 20) break; pick.push(w); }
      return run(shuffle(pick).map((w) => ({ ...mcItem(w, pool), quiz: true })), pool, back, `${title} · recognition quiz`);
    }
    if (mode === "due") return run(due.slice(0, 40).map(prodItem), pool, back, `${title} · review`);
    // learn: new words (never produced) in frequency order, met once as recognition, then produced with the due ones
    const fresh = pool.filter((w) => { const s = status(w.l); return s === "new" || s === "rec"; }).slice(0, per);
    const items = [...fresh.map((w) => mcItem(w, pool)), ...shuffle(due.slice(0, 20)).map(prodItem), ...fresh.map(prodItem)];
    return run(items, pool, back, title);
  }

  function run(items, pool, back, title) {
    const E = A();
    if (!items.length) {
      E.view.innerHTML = `<p class="crumbs"><a href="${back}">← Back</a></p><section class="card"><p>Nothing to practise here right now. Come back when reviews are due, or learn new words.</p><p><a class="btn" href="${back}">Back</a></p></section>`;
      return;
    }
    const queue = items.slice(), done = [], again = new Set();
    let right = 0, graded = 0, recR = 0, recN = 0;
    const next = () => (queue.length ? show(queue.shift()) : finish());
    const head = (q) => { const i = done.length + 1, all = done.length + queue.length + 1;
      return `<p class="crumbs"><a href="${back}">← ${esc(title)}</a></p><article class="card lx-card" id="lx-card">
        <div class="lx-top"><span>${i} / ${all}</span><span>${graded ? `${Math.round((right / graded) * 100)}% typed right` : ""}</span></div>
        <div class="lx-bar"><i style="width:${Math.round(((i - 1) / all) * 100)}%"></i></div>`; };
    const show = (q) => {
      if (q.kind === "rec") {
        E.view.innerHTML = `${head(q)}<div class="lx-task">${q.quiz ? "Recognise" : "New word"} · what does it mean?</div>
          <div class="lx-big" lang="el">${esc(withArt(q.w))}${sayBtn(withArt(q.w))}</div><div class="lx-pos">${esc(POS_EN[q.w.p] || q.w.p)} · #${q.w.r}</div>
          <div class="lx-opts" id="lx-opts">${q.opts.map((o, i) => `<button type="button" data-i="${i}">${esc(o)}</button>`).join("")}</div><div id="lx-fb"></div></article>`;
        bindSay(E.view);
        E.$("#lx-opts").onclick = (ev) => {
          const bt = ev.target.closest("button"); if (!bt || E.$("#lx-opts").dataset.done) return;
          E.$("#lx-opts").dataset.done = "1";
          const ok = q.opts[+bt.dataset.i] === q.w.g;
          E.$("#lx-opts").querySelectorAll("button").forEach((x, i) => { if (q.opts[i] === q.w.g) x.classList.add("right"); else if (x === bt) x.classList.add("wrong"); });
          recN++; if (ok) recR++;
          gradeRec(q.w.l, ok, !q.quiz);
          done.push({ q, ok });
          E.$("#lx-fb").innerHTML = `<div class="feedback ${ok ? "right" : "wrong"}"><b>${ok ? "Right." : "Not this time."}</b> <span lang="el">${esc(withArt(q.w))}</span> = ${esc(q.w.g)}</div>${info(q.w)}
            <div class="actions"><button class="btn" id="lx-next">${queue.length ? "Next" : "See results"}</button></div>`;
          E.$("#lx-fb").querySelectorAll(".lx-gk").forEach(wrap); bindSay(E.$("#lx-fb"));
          const nb = E.$("#lx-next"); nb.onclick = next; nb.focus({ preventScroll: true });
          E.$("#lx-fb").scrollIntoView({ block: "nearest", behavior: "smooth" });
        };
        return;
      }
      // production: English → Greek, typed
      const w = q.w, first = !again.has(w.l);
      const hint = `${w.a ? w.a + " " : ""}${[...w.l].map((ch, i) => (i === 0 || ch === " " ? ch : "·")).join("")}`;
      E.view.innerHTML = `${head(q)}<div class="lx-task">Say it in Greek${first ? "" : " · once more"}</div>
        <div class="lx-en">${esc(w.g)}</div><div class="lx-pos">${esc(POS_EN[w.p] || w.p)}${w.a ? " · with its article" : ""}</div>
        <form class="answer-row" id="lx-f" autocomplete="off"><input id="lx-in" lang="el" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="go" aria-label="Greek word"><button class="btn" id="lx-ok">Check</button></form>
        <div class="lx-foot"><button type="button" class="btn small ghost" id="lx-hint">Hint</button><span class="lx-hint" id="lx-hs" lang="el"></span></div>
        <div id="lx-fb"></div></article>`;
      const inp = E.$("#lx-in"); inp.focus({ preventScroll: true });
      let hinted = false, answered = false;
      E.$("#lx-hint").onclick = () => { hinted = true; E.$("#lx-hs").textContent = hint; inp.focus({ preventScroll: true }); };
      E.$("#lx-f").onsubmit = (ev) => {
        ev.preventDefault();
        if (answered) return next();
        const val = inp.value; if (!val.trim()) return;
        answered = true;
        // Article optional: a bare noun counts; an accent slip is "almost"; a hint caps the result at "almost".
        let res = grade(val, q.forms);
        if (res === "right" && hinted) res = "almost";
        const snap = JSON.stringify(vstore()[w.l] || null);
        if (first) { graded++; if (res !== "wrong") right++; gradeProd(w.l, res); }
        done.push({ q, ok: res !== "wrong", res, val, first });
        if (res === "wrong" && first) { again.add(w.l); queue.splice(Math.min(queue.length, 3), 0, q); }
        inp.readOnly = true; inp.classList.add(res === "wrong" ? "wrong" : res === "almost" ? "almost" : "right");
        E.$("#lx-ok").textContent = queue.length ? "Next" : "See results";
        const msg = res === "right" ? "Right." : res === "almost" ? (hinted ? "Right, with a hint." : "Almost: check the accent.") : "Not quite.";
        E.$("#lx-fb").innerHTML = `<div class="feedback ${res}"><b>${msg}</b> <span class="why">Answer: <b lang="el">${esc(withArt(w))}</b>${sayBtn(withArt(w))}</span></div>${info(w)}
          ${res === "wrong" && first ? `<div class="actions"><button class="kbd-toggle" type="button" id="lx-ovr">I was right</button></div>` : ""}`;
        E.$("#lx-fb").querySelectorAll(".lx-gk").forEach(wrap); bindSay(E.$("#lx-fb"));
        const ov = E.$("#lx-ovr");
        if (ov) ov.onclick = () => {
          const vs = vstore(), prev = JSON.parse(snap); if (prev) vs[w.l] = prev; else delete vs[w.l];
          gradeProd(w.l, "right"); right++; again.delete(w.l);
          const k = queue.indexOf(q); if (k >= 0) queue.splice(k, 1);
          done[done.length - 1].ok = true; ov.remove(); inp.classList.remove("wrong"); inp.classList.add("right");
          E.$("#lx-ok").textContent = queue.length ? "Next" : "See results";
        };
        E.$("#lx-ok").focus({ preventScroll: true });
        E.$("#lx-fb").scrollIntoView({ block: "nearest", behavior: "smooth" });
      };
    };
    const finish = () => {
      const miss = done.filter((d) => d.q.kind === "prod" && d.first && !d.ok);
      E.view.innerHTML = `<p class="crumbs"><a href="${back}">← ${esc(title)}</a></p>
        <section class="card result">${graded ? `<div class="score">${Math.round((right / graded) * 100)}%</div><p>${right} of ${graded} words produced in Greek.</p>` : ""}
        ${recN ? `<p>${recR} of ${recN} recognised.</p>` : ""}
        <p class="sub">Words you typed right come back after 1 day, then after about 3, 8, 20 and 50 days; a word becomes <b>known</b> when its next gap passes 90 days, so about five months of correct recall. Misses come back in 10 minutes.</p>
        <div class="actions"><a class="btn" href="${back}">Done</a></div></section>
        ${miss.length ? `<section class="card"><h3>To remember</h3><ul class="ex-list">${miss.map((d) => `<li><span class="ex-el" lang="el">${esc(withArt(d.q.w))}</span><span class="ex-en">${esc(d.q.w.g)} · you wrote <span lang="el">${esc(d.val)}</span></span></li>`).join("")}</ul></section>` : ""}`;
      window.scrollTo(0, 0);
    };
    next();
  }

  routes.lexi = async (arg) => {
    try {
      if (!arg) return await renderHome();
      if (arg === "review") return await session("review");
      const n = parseInt(arg, 10);
      const sub = location.hash.split(".")[2];
      if (!sub) return await renderBand(n);
      if (sub === "learn" || sub === "due" || sub === "quiz") return await session(sub, n);
      return await renderBand(n);
    } catch (e) {
      A().view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><section class="card"><p>The vocabulary course could not load: ${esc(e.message)}</p></section>`;
    }
  };
})();
