/* Ελληνικά Error hunt: an error-correction workbook. Sentences and short texts with typical learner mistakes;
   tap the mistake, type the fix, read why. Data in library/errors/ (built from library/errors/src/*.txt by build.py).
   Registers #errors, #errors.<category>, #errors.mix-<level> and #errors.p-<id> in window.EllinikaAddons.
   Best scores: progress.library["errors/<id>"]; wrong fixes also go to the mistakes notebook (kind "Error hunt"). */
(function () {
  "use strict";
  const A = () => window.Ellinika;
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});
  const BASE = "library/errors/";
  const HEAD = "Error hunt";
  const LV = ["A2", "B1", "B2", "C1"];
  const PDF = "downloads/textbook/Ellinika-Errors.pdf";

  const CSS = `
.ef-hub h3 { margin: 0; }
.ef-levels { display: flex; flex-wrap: wrap; gap: 8px; }
.ef-card { display: grid; gap: 14px; }
.ef-text { font: 400 1.25rem/2.1 var(--f-display, inherit); margin: 0; }
.ef-text.ef-para { font-size: 1.1rem; line-height: 2; }
.ef-tok { all: unset; cursor: pointer; border-radius: 6px; padding: 1px 2px; margin: 0 -1px; -webkit-tap-highlight-color: transparent; }
.ef-tok:hover, .ef-tok:focus-visible { background: rgba(127, 127, 127, 0.14); }
.ef-tok.miss { background: var(--bad-soft); color: var(--bad); animation: ef-shake 0.3s; }
.ef-tok.found { background: var(--warn-soft); color: var(--warn); outline: 1px solid var(--warn); }
.ef-done .ef-tok { cursor: default; }
.ef-fix-ok { background: var(--good-soft); color: var(--good); border-radius: 6px; padding: 1px 3px; }
.ef-fix-bad { background: var(--bad-soft); color: var(--bad); border-radius: 6px; padding: 1px 3px; }
.ef-was { text-decoration: line-through; opacity: 0.6; font-size: 0.85em; margin-right: 3px; }
.ef-fixbox { display: grid; gap: 8px; border-top: 1px dashed var(--line); padding-top: 12px; }
.ef-acts { display: flex; flex-wrap: wrap; gap: 8px; }
.ef-why { display: grid; gap: 10px; }
.ef-why p { margin: 0; }
.ef-en { color: var(--muted); font-style: italic; }
.ef-cat { font: 600 0.72rem/1 var(--f-ui); text-transform: uppercase; letter-spacing: 0.04em; color: var(--muted); }
.ef-count { font: 600 0.85rem/1.3 var(--f-ui); color: var(--muted); }
.ef-about { margin: 0; }
.ef-about summary { cursor: pointer; font: 600 0.9rem/1.3 var(--f-ui); }
@keyframes ef-shake { 0%, 100% { transform: none; } 25% { transform: translateX(-3px); } 75% { transform: translateX(3px); } }
@media (prefers-reduced-motion: reduce) { .ef-tok.miss { animation: none; } }
`;
  if (!document.getElementById("ef-css")) { const st = document.createElement("style"); st.id = "ef-css"; st.textContent = CSS; document.head.appendChild(st); }

  const norm = (s) => String(s).normalize("NFC").toLocaleLowerCase("el").replace(/[’']/g, "'").replace(/\s+/g, " ").replace(/^[\s.,;:!·]+|[\s.,;:!·]+$/g, "");
  const shuffle = (a) => { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const fixed = (it) => it.parts.map((p) => (typeof p === "string" ? p : it.errs[p].r[0])).join("");
  const wrongText = (it) => it.parts.map((p) => (typeof p === "string" ? p : it.errs[p].w)).join("");

  let idxCache = null, gloss = null;
  async function loadIndex(E) {
    if (!idxCache) idxCache = await E.getJSON(BASE + "index.json");
    if (!gloss) { try { gloss = await E.getJSON(BASE + "gloss.json"); } catch (e) { gloss = {}; } }
    return idxCache;
  }
  const catName = (idx, c) => (idx.categories.find((x) => x.id === c) || { el: c }).el;

  function logMistake(E, it, e, given) {
    const p = E.progress; p.library = p.library || {};
    const list = (p.library.mistakes = p.library.mistakes || []);
    let prompt = it.parts.map((q) => (typeof q === "string" ? q : q === it.errs.indexOf(e) ? `⟦${it.errs[q].w}⟧` : it.errs[q].r[0])).join("");
    if (it.title) { // a text: keep only the sentence with the mistake
      const a = prompt.indexOf("⟦"), b = prompt.indexOf("⟧");
      const from = Math.max(...[". ", "! ", "; ", "? ", ": "].map((x) => prompt.lastIndexOf(x, a))) + 2;
      const ends = [". ", "! ", "; ", "? "].map((x) => prompt.indexOf(x, b)).filter((x) => x >= 0);
      prompt = prompt.slice(from >= 2 ? from : 0, ends.length ? Math.min(...ends) + 1 : prompt.length).trim();
    }
    const k = "Error hunt", ex = list.findIndex((m) => m.p === prompt && m.k === k);
    const m = ex >= 0 ? list.splice(ex, 1)[0] : { k, p: prompt, a: e.r, h: location.hash, mc: false, n: 0 };
    m.g = given || "—"; m.t = Date.now(); m.n++; list.unshift(m); list.length = Math.min(list.length, 400);
  }

  // Splits an item into tappable word tokens; the words of a marker sit in one .ef-span and carry its index.
  function tokens(E, it) {
    const words = (text, e) => text.split(/(\s+)/).map((chunk) => {
      if (!chunk) return "";
      if (/^\s+$/.test(chunk)) return " ";
      const m = chunk.match(/^([«"“(]*)(.*?)([»"”).,;:!?·…]*)$/);
      const [, pre, core, post] = m && m[2] ? m : ["", "", chunk, ""];
      return `${E.esc(pre)}<button class="ef-tok" data-e="${e}" lang="el">${E.esc(core)}</button>${E.esc(post)}`;
    }).join("");
    return it.parts.map((p) => (typeof p === "string" ? words(p, -1) : `<span class="ef-span" data-s="${p}">${words(it.errs[p].w, p)}</span>`)).join("");
  }

  // Renders one item into box; calls done(score 0..1, details) when the learner has finished it.
  function play(E, idx, it, box, opts, done) {
    const para = !!it.title, errs = it.errs || [];
    const state = errs.map(() => ({ found: false, fixed: null, tries: 0 }));
    let falseTaps = 0, firstTapWrong = false, finished = false, tapped = false;
    box.innerHTML = `<section class="card ef-card">
      ${para ? `<div><span class="chip">${E.esc(it.level)}</span> <strong lang="el">${E.esc(it.el)}</strong> <span class="ex-en">${E.esc(it.title)}</span></div>` : ""}
      <p class="ef-count" id="ef-count"></p>
      <p class="ef-text${para ? " ef-para" : ""}" id="ef-text">${tokens(E, it)}</p>
      <div id="ef-fix"></div>
      <div class="ef-acts" id="ef-acts">
        ${para ? "" : `<button class="btn small ghost" id="ef-none">No mistake</button>`}
        <button class="btn small ghost" id="ef-en-b">English</button>
        <button class="btn small ghost" id="ef-show">Show the answer</button>
      </div>
      <p class="ef-en" id="ef-en" hidden>${E.esc(it.en)}</p>
      <div id="ef-out"></div></section>`;
    const $ = (s) => box.querySelector(s);
    const count = () => {
      if (finished) return;
      if (!para) { $("#ef-count").textContent = opts.hideHint ? "Tap the mistake, or choose “No mistake”." : "Tap the word or phrase that is wrong, or choose “No mistake”."; return; }
      const left = state.filter((s) => s.fixed === null).length;
      $("#ef-count").textContent = `${errs.length} mistakes in this text · ${left} still to fix${falseTaps ? ` · ${falseTaps} false alarm${falseTaps > 1 ? "s" : ""}` : ""}`;
    };
    count();
    $("#ef-en-b").onclick = () => { const p = $("#ef-en"); p.hidden = !p.hidden; };

    const spans = (i) => [...box.querySelectorAll(`.ef-tok[data-e="${i}"]`)];
    const replaceSpan = (i, ok) => {
      const w = box.querySelector(`.ef-span[data-s="${i}"]`), e = errs[i];
      if (!w) return;
      w.innerHTML = ok ? `<span class="ef-fix-ok" lang="el">${E.esc(e.r[0])}</span>` : `<span class="ef-fix-bad" lang="el"><span class="ef-was">${E.esc(e.w)}</span>${E.esc(e.r[0])}</span>`;
    };

    const finish = () => {
      if (finished) return;
      finished = true;
      box.querySelector(".ef-card").classList.add("ef-done");
      $("#ef-fix").innerHTML = "";
      $("#ef-acts").style.display = "none";
      $("#ef-count").textContent = "";
      let score;
      if (it.ok) score = tapped ? 0 : 1;
      else {
        const good = state.filter((s) => s.fixed === true && s.tries === 1).length;
        score = para ? Math.max(0, good - falseTaps) / errs.length : (good === 1 && !firstTapWrong ? 1 : 0);
      }
      const why = it.ok ? `<p>${E.md(it.why)}</p>` : errs.map((e, i) => `<p><span class="ef-cat">${E.esc(catName(idx, e.c))}</span><br>
        <span class="mk-bad" lang="el">${E.esc(e.w)}</span> → <strong class="mk-ok" lang="el">${E.esc(e.r[0])}</strong>${e.r.length > 1 ? ` <span class="sub">(also: <span lang="el">${e.r.slice(1).map(E.esc).join(", ")}</span>)</span>` : ""}${state[i].fixed === true && state[i].tries === 1 ? " ✓" : ""}<br>${E.md(e.why)}</p>`).join("");
      $("#ef-out").innerHTML = `<div class="feedback ${score >= 0.999 ? "right" : score > 0 ? "almost" : "wrong"}"><strong>${it.ok ? (score ? "Right: this one has no mistake." : "This sentence was correct as it stood.") : para ? `${Math.round(score * 100)}%: ${state.filter((s) => s.fixed === true && s.tries === 1).length} of ${errs.length} fixed at the first try${falseTaps ? `, ${falseTaps} false alarm${falseTaps > 1 ? "s" : ""}` : ""}` : score ? "Well spotted." : state[0] && state[0].fixed === true ? (firstTapWrong ? "Fixed, after a wrong first tap." : "Fixed at the second try.") : "Here is the fix."}</strong></div>
        ${it.ok ? "" : `<p lang="el" class="ef-text${para ? " ef-para" : ""}" id="ef-right">${E.esc(fixed(it))}</p>`}
        <p class="ef-en">${E.esc(it.en)}</p><div class="ef-why">${why}</div>
        <div class="ef-acts">${opts.next ? `<button class="btn" id="ef-next">${E.esc(opts.next)}</button>` : ""}</div>`;
      E.setGloss(gloss || {});
      E.wrapGreek($("#ef-out"));
      if ($("#ef-next")) $("#ef-next").onclick = () => done(score);
      else done(score);
      E.saveProgress();
    };

    const openFix = (i) => {
      const e = errs[i];
      spans(i).forEach((t) => t.classList.add("found"));
      $("#ef-fix").innerHTML = `<div class="ef-fixbox"><label class="sub" for="ef-in">Correct it (edit the words, then Check):</label>
        <div class="answer-row"><input id="ef-in" lang="el" autocomplete="off" autocapitalize="off" spellcheck="false" value="${E.esc(e.w)}"><button class="btn" id="ef-go">Check</button></div>
        <div id="ef-fb"></div></div>`;
      const inp = $("#ef-in");
      inp.focus(); try { inp.setSelectionRange(inp.value.length, inp.value.length); } catch (err) { /* not supported */ }
      const go = () => {
        const v = inp.value, st = state[i];
        st.tries++;
        if (e.r.some((r) => norm(r) === norm(v))) {
          st.fixed = true; replaceSpan(i, true); $("#ef-fix").innerHTML = "";
        } else if (st.tries < 2 && norm(v) !== norm(e.w)) {
          inp.classList.add("wrong"); $("#ef-fb").innerHTML = `<p class="sub">Not quite. One more try.</p>`; return;
        } else if (st.tries < 2) {
          inp.classList.add("wrong"); $("#ef-fb").innerHTML = `<p class="sub">That is the original. Change it, then Check.</p>`; st.tries--; return;
        } else {
          st.fixed = false; logMistake(E, it, e, v); replaceSpan(i, false); $("#ef-fix").innerHTML = "";
        }
        count();
        if (state.every((s) => s.fixed !== null)) finish();
      };
      $("#ef-go").onclick = go;
      inp.onkeydown = (ev) => { if (ev.key === "Enter") { ev.preventDefault(); go(); } };
    };

    box.querySelector("#ef-text").addEventListener("click", (ev) => {
      const t = ev.target.closest(".ef-tok");
      if (!t || finished) return;
      ev.stopPropagation();
      const i = +t.dataset.e;
      if (it.ok) { tapped = true; t.classList.add("miss"); finish(); return; }
      if (i < 0) {
        if (!state.some((s) => s.found)) firstTapWrong = true;
        falseTaps += para ? 1 : 0;
        t.classList.remove("miss"); void t.offsetWidth; t.classList.add("miss");
        if (!para && firstTapWrong) $("#ef-count").textContent = "That part is fine. Look again.";
        else count();
        return;
      }
      if (state[i].fixed !== null) return;
      state[i].found = true;
      openFix(i);
    });
    if ($("#ef-none")) $("#ef-none").onclick = () => {
      if (it.ok) finish();
      else { firstTapWrong = true; errs.forEach((e, i) => { if (state[i].fixed === null) { state[i].fixed = false; logMistake(E, it, e, "(no mistake)"); replaceSpan(i, false); } }); finish(); }
    };
    $("#ef-show").onclick = () => {
      if (it.ok) { tapped = true; finish(); return; }
      errs.forEach((e, i) => { if (state[i].fixed === null) { state[i].fixed = false; logMistake(E, it, e, "(shown)"); replaceSpan(i, false); } });
      finish();
    };
  }

  // A run of items, one at a time, with a result screen; best score saved under key.
  function session(E, idx, items, key, back, label) {
    let i = 0, total = 0;
    const show = () => {
      if (i >= items.length) {
        const sc = items.length ? total / items.length : 0, p = E.progress;
        p.library = p.library || {}; p.library[key] = Math.max(p.library[key] || 0, sc); E.saveProgress();
        E.view.innerHTML = `<p class="crumbs"><a href="${back}">← ${E.esc(label)}</a></p>
          <section class="card result"><div class="score">${Math.round(sc * 100)}%</div>
          <p>${Math.round(total * 10) / 10} of ${items.length} right. Fixes you missed are in the <a href="#mistakes">mistakes notebook</a>.</p>
          <div class="ef-acts"><a class="btn" href="${back}">Back</a><button class="btn ghost" id="ef-again">Again</button></div></section>`;
        E.$("#ef-again").onclick = () => { i = 0; total = 0; show(); };
        return window.scrollTo(0, 0);
      }
      const it = items[i];
      E.view.innerHTML = `<p class="crumbs"><a href="${back}">← ${E.esc(label)}</a></p>
        <div class="pmeta"><span>${E.esc(it.level)}${it.errs ? " · " + E.esc(catName(idx, it.errs[0].c)) : ""}</span><span>${i + 1} / ${items.length}</span></div><div id="ef-box"></div>`;
      play(E, idx, it, E.$("#ef-box"), { next: i + 1 < items.length ? "Next" : "See the result", hideHint: i > 0 }, (s) => { total += s; i++; show(); });
      window.scrollTo(0, 0);
    };
    show();
  }

  async function hub(E) {
    const idx = await loadIndex(E), done = (E.progress.library || {});
    const best = (k) => done["errors/" + k];
    const chip = (k, txt) => best(k) != null ? `<span class="chip done">${Math.round(best(k) * 100)}%</span>` : `<span class="chip new">${txt}</span>`;
    document.title = HEAD + " · Ελληνικά";
    const totalS = idx.categories.reduce((n, c) => n + c.count, 0);
    E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p>
      <div class="ef-hub">
      <h2><span lang="el">Βρες το λάθος</span> · ${HEAD}</h2>
      <p class="sub">${totalS} sentences and ${idx.paragraphs.length} short texts with the mistakes English speakers and other learners make most in Greek, from A2 to C1. Tap the mistake, type the fix, then read why. Some sentences are correct: say so with “No mistake”. Every Greek word in the answers can be tapped for its meaning.</p>
      <section class="card"><h3>Mixed practice by level</h3><p class="sub">Twelve sentences from every topic, in random order.</p>
        <div class="ef-levels">${LV.map((l) => `<a class="btn small" href="#errors.mix-${l}">${l}</a>${best("mix-" + l) != null ? ` <span class="chip done">${Math.round(best("mix-" + l) * 100)}%</span>` : ""}`).join("")}</div></section>
      <h3>By topic</h3>
      <ul class="lessons">${idx.categories.map((c, i) => `<li><a class="lesson-row" href="#errors.${E.esc(c.id)}"><span class="lr-num">${i + 1}</span>
        <span class="lr-main"><span class="lr-title" lang="el">${E.esc(c.el)}</span><span class="lr-en">${E.esc(c.title)} · ${LV.filter((l) => c.levels[l]).join(" ")}</span></span>${chip(c.id, c.count + " sentences")}</a></li>`).join("")}</ul>
      <h3>Find all the mistakes in a text</h3>
      <ul class="lessons">${idx.paragraphs.map((p, i) => `<li><a class="lesson-row" href="#errors.${E.esc(p.id)}"><span class="lr-num">${E.esc(p.level)}</span>
        <span class="lr-main"><span class="lr-title" lang="el">${E.esc(p.el)}</span><span class="lr-en">${E.esc(p.title)}</span></span>${chip(p.id, p.errors + " mistakes")}</a></li>`).join("")}</ul>
      <p class="sub"><a href="${PDF}" target="_blank" rel="noopener">Printable workbook (PDF) with answer key</a></p>
      </div>`;
    window.scrollTo(0, 0);
  }

  routes.errors = async (arg) => {
    const E = A();
    E.$("#bar-meta").textContent = HEAD;
    E.setGloss({});
    if (!arg) return hub(E);
    const idx = await loadIndex(E);
    if (arg.startsWith("mix-")) {
      const lvl = arg.slice(4);
      if (!LV.includes(lvl)) { location.hash = "errors"; return; }
      const all = (await Promise.all(idx.categories.map((c) => E.getJSON(BASE + c.file)))).flatMap((d) => d.items.filter((x) => x.level === lvl));
      // one per topic first, then fill to twelve, at most two correct sentences
      const byCat = {};
      shuffle(all).forEach((x) => { const c = x.errs ? x.errs[0].c : "ok"; (byCat[c] = byCat[c] || []).push(x); });
      const pick = [];
      Object.keys(byCat).filter((c) => c !== "ok").forEach((c) => pick.push(byCat[c].shift()));
      shuffle(pick).splice(10);
      pick.push(...(byCat.ok || []).slice(0, 2));
      document.title = `${HEAD} ${lvl} · Ελληνικά`;
      return session(E, idx, shuffle(pick), "errors/mix-" + lvl, "#errors", HEAD);
    }
    if (arg.startsWith("p-")) {
      const data = await E.getJSON(BASE + "paragraphs.json"), it = data.items.find((x) => x.id === arg);
      if (!it) { location.hash = "errors"; return; }
      document.title = it.el + " · " + HEAD;
      const pos = data.items.indexOf(it), next = data.items[pos + 1];
      E.view.innerHTML = `<p class="crumbs"><a href="#errors">← ${HEAD}</a></p><div id="ef-box"></div>`;
      play(E, idx, it, E.$("#ef-box"), { next: next ? "Next text" : "Back to the list" }, (s) => {
        const p = E.progress; p.library = p.library || {}; p.library["errors/" + it.id] = Math.max(p.library["errors/" + it.id] || 0, s); E.saveProgress();
        location.hash = next ? "errors." + next.id : "errors";
      });
      return window.scrollTo(0, 0);
    }
    const meta = idx.categories.find((c) => c.id === arg);
    if (!meta) { location.hash = "errors"; return; }
    const d = await E.getJSON(BASE + meta.file);
    document.title = d.el + " · " + HEAD;
    const start = (lvl) => session(E, idx, lvl ? d.items.filter((x) => x.level === lvl) : d.items, "errors/" + d.id, "#errors." + d.id, d.el);
    E.view.innerHTML = `<p class="crumbs"><a href="#errors">← ${HEAD}</a></p>
      <div class="story-head"><h2 lang="el">${E.esc(d.el)}</h2><span class="ex-en">${E.esc(d.title)}</span></div>
      <section class="card"><p>${E.md(d.about)}</p></section>
      <section class="card"><p class="sub">${d.items.length} sentences, easiest first. Start with all of them or pick a level.</p>
      <div class="ef-levels"><button class="btn" data-l="">All ${d.items.length}</button>${LV.filter((l) => meta.levels[l]).map((l) => `<button class="btn small ghost" data-l="${l}">${l} · ${meta.levels[l]}</button>`).join("")}</div></section>`;
    E.wrapGreek(E.view.querySelector(".card"));
    E.view.querySelectorAll("[data-l]").forEach((b) => (b.onclick = () => start(b.dataset.l)));
    window.scrollTo(0, 0);
  };
})();
