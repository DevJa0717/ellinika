/* Ελληνικά news digest: current affairs rewritten at B1, B2 and C1, a new issue every morning.
   Registers #digest (latest issue), #digest.<date> (an archived issue) and #digest.<date>~<story> in window.EllinikaAddons.
   Content is data: library/digest/index.json lists the issues (newest first); each issue is library/digest/<date>.json,
   built by deploy/news/build_issue.py. Each story has the same news at three levels with its own glossary and questions.
   The chosen level is kept in localStorage "ellinika.digest.level", so it is per profile. */
(function () {
  "use strict";
  const A = () => window.Ellinika;
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});
  const BASE = "library/digest/", LEVEL_KEY = "ellinika.digest.level", LEVELS = ["B1", "B2", "C1"];
  const css = `
.dg-hero { margin: 4px 0 14px; }
.dg-hero h2 { margin: 0 0 4px; font: 400 2rem/1.15 var(--f-display); }
.dg-hero .dg-intro p { margin: 8px 0 0; }
.dg-hero .dg-intro .en { color: var(--muted); font-size: .95rem; }
.dg-date { font: 600 .85rem/1.3 var(--f-ui); color: var(--terra); letter-spacing: .03em; margin: 10px 0 0; }
.dg-bar { position: sticky; top: var(--bar-h, calc(env(safe-area-inset-top, 0px) + 49px)); z-index: 4; display: flex; gap: 8px; flex-wrap: wrap; align-items: center; padding: 8px 0; background: var(--paper); border-bottom: 1px solid var(--line); margin: 0 0 12px; }
.dg-seg { display: inline-flex; border: 1px solid var(--line); border-radius: 999px; overflow: hidden; }
.dg-seg button { border: 0; background: transparent; color: var(--ink); font: 600 .85rem/1 var(--f-ui); padding: 8px 14px; min-height: 36px; cursor: pointer; }
.dg-seg button[aria-pressed="true"] { background: var(--aegean, #0a2747); color: #fff; }
.dg-bar .sub { font-size: .8rem; }
.dg-sec { margin: 22px 0 6px; font: 600 1.05rem/1.3 var(--f-ui); }
.dg-sec .el { font: 400 1.3rem/1.25 var(--f-display); margin-right: 6px; }
.dg-row .lr-title { white-space: normal; }
.dg-row-chips { display: flex; gap: 4px; flex-wrap: wrap; justify-content: flex-end; }
.dg-head { display: grid; gap: 6px; margin: 4px 0 12px; }
.dg-chips { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
.dg-head h2 { margin: 0; font: 400 1.9rem/1.2 var(--f-display); }
.dg-head .dg-en { font: 500 1rem/1.35 var(--f-ui); color: var(--muted); }
.dg-text p { margin: 0 0 14px; font-size: 1.06rem; line-height: 1.65; }
.dg-gloss { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 6px 14px; margin: 0; }
.dg-gloss dt { font: 600 1rem/1.35 var(--f-body); overflow-wrap: anywhere; }
.dg-gloss dd { margin: 0; color: var(--muted); font-size: .95rem; overflow-wrap: anywhere; }
.dg-gram h4 { margin: 0 0 6px; font: 600 1rem/1.3 var(--f-ui); display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
.dg-gram p { margin: 0 0 6px; }
.dg-gram ul { margin: 6px 0 0; padding-left: 18px; }
.dg-gram li { margin: 0 0 4px; }
.dg-gram li .ex-en { display: block; }
.dg-src ol { margin: 0; padding-left: 22px; font-size: .9rem; }
.dg-src li { margin: 0 0 6px; overflow-wrap: anywhere; }
.dg-nav { display: flex; gap: 8px; flex-wrap: wrap; margin: 20px 0 0; }
.dg-nav .btn { max-width: 100%; white-space: normal; text-align: left; }
.dg-arch li a { display: block; }
.dg-note { font-size: .85rem; color: var(--muted); margin: 14px 0 0; }
`;
  function style() {
    if (document.getElementById("dg-style")) return;
    const s = document.createElement("style"); s.id = "dg-style"; s.textContent = css; document.head.append(s);
  }
  const level = () => { try { const v = localStorage.getItem(LEVEL_KEY); return LEVELS.includes(v) ? v : "B2"; } catch (e) { return "B2"; } };
  const setLevel = (v) => { try { localStorage.setItem(LEVEL_KEY, v); } catch (e) { /* private mode */ } };
  // The index changes every morning: ask the network once per day (the date in the URL), fall back to the saved copy offline.
  async function index() {
    const E = A(), day = new Date().toISOString().slice(0, 10);
    try { const r = await fetch(`${BASE}index.json?d=${day}`); if (r.ok) return await r.json(); } catch (e) { /* offline */ }
    return E.getJSON(BASE + "index.json");
  }
  const seg = (lv) => `<div class="dg-seg" role="group" aria-label="Level">${LEVELS.map((l) => `<button type="button" data-lv="${l}" aria-pressed="${l === lv}">${l}</button>`).join("")}</div>`;
  const bindSeg = (root, redraw) => root.querySelectorAll(".dg-seg button").forEach((b) => (b.onclick = () => { setLevel(b.dataset.lv); redraw(); }));
  const key = (iss, st, lv) => `digest/${iss}/${st}/${lv}`;

  async function issuePage(id) {
    const E = A(), idx = await index(), meta = id ? idx.issues.find((i) => i.id === id) : idx.issues[0];
    if (!meta) { E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><p>No issue yet. The first one appears after the next morning run.</p>`; return; }
    const iss = await E.getJSON(BASE + meta.file), latest = meta === idx.issues[0], done = E.progress.library || {};
    document.title = (latest ? idx.el : meta.el) + " · Ελληνικά";
    E.$("#bar-meta").textContent = "News digest";
    const draw = () => {
      const lv = level();
      const row = (s) => {
        const v = s.levels[lv], sc = done[key(iss.id, s.id, lv)];
        const ticks = LEVELS.filter((l) => done[key(iss.id, s.id, l)] != null);
        return `<li><a class="lesson-row dg-row" href="#digest.${E.esc(iss.id)}~${E.esc(s.id)}"><span class="lr-num">${iss.stories.indexOf(s) + 1}</span>
          <span class="lr-main"><span class="lr-title" lang="el">${E.esc(v.el)}</span><span class="lr-en">${E.esc(v.title)}</span></span>
          <span class="dg-row-chips">${sc != null ? `<span class="chip done">${Math.round(sc * 100)}%</span>` : ticks.length ? `<span class="chip">${ticks.join(" ")} ✓</span>` : ""}</span></a></li>`;
      };
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a>${latest ? "" : ` · <a href="#digest">Today's issue</a>`}</p>
        <div class="dg-hero"><h2 lang="el">${E.esc(idx.el)}</h2><span class="ex-en">${E.esc(idx.title || "")}</span>
          ${latest ? `<div class="dg-intro"><p lang="el">${E.esc(idx.intro_el || "")}</p></div>` : ""}
          <p class="dg-date" lang="el">${E.esc(iss.date_el)}${latest ? "" : " · αρχείο"}</p></div>
        <div class="dg-bar">${seg(lv)}<span class="sub">${{ B1: "Shorter, everyday words", B2: "Exam level", C1: "Fuller, press register" }[lv]}</span></div>
        ${(iss.sections || []).map((sec) => `<h3 class="dg-sec"><span class="el" lang="el">${E.esc(sec.el)}</span><span class="sub">${E.esc(sec.en)}</span></h3>
          <ul class="lessons">${iss.stories.filter((s) => s.section === sec.id).map(row).join("")}</ul>`).join("")}
        <h3 class="dg-sec"><span class="el" lang="el">Αρχείο</span><span class="sub">Past issues</span></h3>
        <ul class="lessons dg-arch">${idx.issues.map((i) => `<li><a class="lesson-row" href="#digest.${E.esc(i.id)}"><span class="lr-main"><span class="lr-title" lang="el">${E.esc(i.el)}</span><span class="lr-en" lang="el">${E.esc(i.lead || "")}</span></span><span class="chip">${i.count}</span></a></li>`).join("")}</ul>
        <p class="dg-note">Each story is written for learners from the reports linked under it; facts and quotations come from those reports, the wording does not.</p>`;
      bindSeg(E.view, draw);
    };
    draw(); window.scrollTo(0, 0);
  }

  async function storyPage(issueId, storyId) {
    const E = A(), idx = await index(), meta = idx.issues.find((i) => i.id === issueId);
    if (!meta) { location.hash = "digest"; return; }
    const iss = await E.getJSON(BASE + meta.file), s = iss.stories.find((x) => x.id === storyId);
    if (!s) { location.hash = "digest." + issueId; return; }
    const pos = iss.stories.indexOf(s), prev = iss.stories[pos - 1], next = iss.stories[pos + 1];
    const sec = (iss.sections || []).find((x) => x.id === s.section);
    E.setGloss(iss.gloss);
    E.$("#bar-meta").textContent = "News digest";
    const draw = (keepScroll) => {
      const lv = level(), v = s.levels[lv], k = key(iss.id, s.id, lv), y = window.scrollY;
      document.title = v.el + " · Ειδήσεις";
      E.view.innerHTML = `<p class="crumbs"><a href="#digest${idx.issues[0].id === iss.id ? "" : "." + E.esc(iss.id)}">← <span lang="el">${E.esc(iss.date_el)}</span></a></p>
        <div class="dg-head"><div class="dg-chips">${sec ? `<span class="chip" lang="el">${E.esc(sec.el)}</span>` : ""}<span class="chip">${lv}</span></div>
          <h2 lang="el">${E.esc(v.el)}</h2><span class="dg-en">${E.esc(v.title)}</span></div>
        <div class="dg-bar">${seg(lv)}<span class="sub">Same story, ${lv === "B1" ? "simplest" : lv === "B2" ? "exam-level" : "fullest"} version</span></div>
        <div class="dg-text" lang="el">${v.paras.map((p) => `<p>${E.esc(p.el)}</p>`).join("")}</div>
        <details class="rd-en"><summary>English translation</summary>${v.paras.map((p) => `<p>${E.esc(p.en)}</p>`).join("")}</details>
        <section class="card"><h3>Glossary · ${lv}</h3><dl class="dg-gloss">${v.glossary.map((g) => `<dt lang="el">${E.esc(g.el)}</dt><dd>${E.esc(g.en)}</dd>`).join("")}</dl></section>
        ${s.grammar ? `<section class="card dg-gram"><h3>Grammar in this story</h3><h4><span class="chip">${E.esc(s.grammar.level)}</span><span lang="el">${E.esc(s.grammar.title)}</span></h4><p>${E.md(s.grammar.en)}</p>${(s.grammar.examples || []).length ? `<ul>${s.grammar.examples.map((x) => `<li><span lang="el">${E.esc(x.el)}</span><span class="ex-en">${E.esc(x.en)}</span></li>`).join("")}</ul>` : ""}</section>` : ""}
        <section class="card story-q"><h3>Questions · ${lv}</h3>${v.questions.map((q, i) => `<div class="sq" data-i="${i}"><p class="q-prompt" lang="el">${E.esc(q.q)}</p><div class="options">${shuffle(q.options, k + i).map((o) => `<button class="opt" lang="el">${E.esc(o)}</button>`).join("")}</div><p class="ex-en sq-why" hidden></p></div>`).join("")}<p class="sub" id="sq-score"></p></section>
        ${(s.vocab || []).length ? `<section class="card"><h3>Words to keep</h3><p class="word-cloud" lang="el">${s.vocab.map((w) => E.esc(w)).join(" · ")}</p><button class="btn small" id="dg-add">Add all to my words</button></section>` : ""}
        <section class="dg-src"><h3>Based on</h3><ol>${s.sources.map((x) => `<li>${E.esc(x.name)}${x.date ? `, ${E.esc(x.date)}` : ""} · <a href="${E.esc(x.url)}" target="_blank" rel="noopener">${E.esc(x.url.replace(/^https?:\/\/(www\.)?/, "").split("/")[0])}</a></li>`).join("")}</ol></section>
        <div class="dg-nav">${prev ? `<a class="btn ghost" href="#digest.${E.esc(iss.id)}~${E.esc(prev.id)}">← <span lang="el">${E.esc(prev.levels[lv].el)}</span></a>` : ""}${next ? `<a class="btn" href="#digest.${E.esc(iss.id)}~${E.esc(next.id)}">Next: <span lang="el">${E.esc(next.levels[lv].el)}</span></a>` : ""}</div>`;
      E.view.querySelectorAll(".dg-head h2, .dg-text, .dg-gloss dt, .dg-gram [lang=el], .story-q").forEach((n) => E.wrapGreek(n));
      bindSeg(E.view, () => draw(true));
      let right = 0, answered = 0;
      E.view.querySelectorAll(".sq").forEach((box) => {
        const q = v.questions[box.dataset.i];
        box.querySelectorAll(".opt").forEach((b) => (b.onclick = () => {
          box.querySelectorAll(".opt").forEach((x) => { x.disabled = true; if (x.textContent === q.answer) x.classList.add("right"); });
          if (b.textContent === q.answer) right++; else b.classList.add("wrong");
          if (q.why) { const w = box.querySelector(".sq-why"); w.textContent = q.why; w.hidden = false; }
          if (++answered === v.questions.length) {
            const p = E.progress; p.library = p.library || {}; p.library[k] = Math.max(p.library[k] || 0, right / answered); E.saveProgress();
            E.$("#sq-score").textContent = `${right} of ${answered} right`;
          }
        }));
      });
      const add = E.$("#dg-add");
      if (add) add.onclick = () => {
        const p = E.progress, vv = p.vocab || (p.vocab = {}), now = Date.now(); let n = 0;
        for (const l of s.vocab) if (!vv[l]) { vv[l] = { ivl: 0, reps: 0, lapses: 0, rec: 1, seen: now, due: now }; n++; }
        E.saveProgress(); add.outerHTML = `<span class="lk-state">${n} added · they come up in your next word recall</span>`;
      };
      window.scrollTo(0, keepScroll ? y : 0);
    };
    draw(false);
  }
  // Options are stored with the right answer first; show them in a fixed shuffled order per question.
  function shuffle(a, seed) {
    let h = 0; for (const c of seed) h = (h * 31 + c.charCodeAt(0)) >>> 0;
    const out = a.slice();
    for (let i = out.length - 1; i > 0; i--) { h = (h * 1103515245 + 12345) >>> 0; const j = h % (i + 1); [out[i], out[j]] = [out[j], out[i]]; }
    return out;
  }

  routes.digest = async (tab) => {
    style();
    const [issueId, storyId] = (tab || "").split("~");
    try { await (storyId ? storyPage(issueId, storyId) : issuePage(issueId)); }
    catch (e) { A().view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><p>The news digest could not load: ${A().esc(e.message)}</p>`; }
  };
})();
