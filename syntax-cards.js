/* Ελληνικά Syntax and discourse guide (#syntax, #syntax.<id>~<n>) and Pocket grammar cards (#cards, #cards.<id>).
   Content is data: library/syntax/<id>.json built from library/syntax/src/*.txt, library/cards/<group>.json built from
   library/cards/src/*.txt (run both build.py scripts). Registers both routes in window.EllinikaAddons. */
(function () {
  "use strict";
  const A = () => window.Ellinika;
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});
  const SB = "library/syntax/", CB = "library/cards/";
  const SHEAD = "Syntax and discourse", CHEAD = "Pocket grammar cards";
  const LV = ["A1", "A2", "B1", "B2", "C1"];

  const CSS = `
.syn-doc { display: grid; gap: 14px; }
.syn-doc .card, .gc-card { gap: 12px; }
.syn-doc p, .gc-card p { margin: 0; }
.syn-sec { scroll-margin-top: 80px; }
.syn-sec h3, .gc-card h2 { display: grid; gap: 2px; margin: 0; font: 400 1.45rem/1.2 var(--f-display); }
.syn-sec h3 .ex-en, .gc-card h2 .ex-en { font-size: 0.85rem; }
.syn-head { display: flex; justify-content: space-between; align-items: center; gap: 8px; }
.syn-n { font: 600 0.8rem/1 var(--f-ui); color: var(--muted); font-variant-numeric: tabular-nums; }
.syn-tip { border-left-color: var(--terra); background: rgba(242, 193, 78, 0.07); border-radius: 0 8px 8px 0; padding: 10px 12px 10px 14px; }
.syn-ex { border-left: 2px solid var(--line); padding-left: 12px; }
table.syn-tbl td { font-size: 1rem; }
table.syn-tbl th[scope="row"] { text-transform: none; letter-spacing: 0; font-size: 0.85rem; }
.syn-toc summary { cursor: pointer; font: 600 0.9rem/1.3 var(--f-ui); }
.syn-toc ol { margin: 0; padding-left: 0; list-style: none; display: grid; gap: 2px; }
.syn-jump { all: unset; cursor: pointer; display: block; padding: 7px 4px; border-radius: 6px; line-height: 1.35; }
.syn-jump:hover, .syn-jump:focus-visible { background: rgba(127, 127, 127, 0.12); }
.syn-jump .ex-en { margin-left: 4px; }
.syn-ex-h { font: 600 0.72rem/1.2 var(--f-ui); letter-spacing: 0.12em; text-transform: uppercase; color: var(--terra); }
.syn-check { display: grid; gap: 18px; border-top: 1px dashed var(--line); padding-top: 12px; }
.syn-q .q-prompt { margin: 0 0 8px; }
.syn-kind { font: 600 0.68rem/1 var(--f-ui); letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted); margin-bottom: 4px; display: block; }
.syn-built { min-height: 2.9rem; display: flex; flex-wrap: wrap; gap: 6px; align-items: center; padding: 8px; border: 1px dashed var(--line); border-radius: 8px; }
.syn-built.right { border-style: solid; border-color: var(--good); background: var(--good-soft); }
.syn-built.wrong { border-style: solid; border-color: var(--bad); background: var(--bad-soft); }
.syn-tiles { display: flex; flex-wrap: wrap; gap: 6px; margin: 8px 0; }
.syn-tile { padding: 8px 11px; border: 1px solid var(--line); border-radius: 8px; background: var(--paper); color: var(--ink); font-size: 1.05rem; cursor: pointer; }
.syn-tile:disabled { opacity: 0.3; cursor: default; }
.syn-acts { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 4px; }
.syn-why { margin-top: 8px !important; }
.syn-ans { margin-top: 6px !important; }
.syn-links { display: grid; gap: 6px; }
.syn-links-h { font: 600 0.72rem/1.2 var(--f-ui); letter-spacing: 0.12em; text-transform: uppercase; color: var(--muted); }
.syn-links ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 6px; }
.syn-links a { display: inline-flex; gap: 6px; align-items: baseline; padding: 6px 10px; border: 1px solid var(--line); border-radius: 999px; text-decoration: none; color: inherit; font-size: 0.9rem; line-height: 1.3; }
.syn-links a:hover { border-color: var(--terra); }
.syn-links .lk-k { font: 600 0.62rem/1 var(--f-ui); letter-spacing: 0.06em; text-transform: uppercase; color: var(--terra); }
.syn-nav { display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap; }
.gc-groups { display: grid; gap: 18px; }
.gc-group h3 { margin: 0 0 8px; font: 400 1.2rem/1.2 var(--f-display); display: flex; gap: 8px; align-items: baseline; flex-wrap: wrap; }
.gc-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 8px; }
.gc-tile { display: grid; gap: 4px; align-content: start; padding: 12px; border: 1px solid var(--line); border-radius: 10px; background: var(--card); text-decoration: none; color: inherit; min-height: 84px; }
.gc-tile:hover { border-color: var(--terra); }
.gc-tile .lr-title { font-size: 1rem; line-height: 1.25; }
.gc-tile .lr-en { font-size: 0.8rem; }
.gc-tile .gc-meta { display: flex; gap: 6px; align-items: center; }
.gc-bar { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }
.gc-test td.gc-hide { color: transparent; text-shadow: none; background: repeating-linear-gradient(135deg, rgba(127,127,127,.14) 0 6px, rgba(127,127,127,.06) 6px 12px); cursor: pointer; }
.gc-test td.gc-hide * { color: transparent !important; }
.gc-pos { font: 600 0.8rem/1 var(--f-ui); color: var(--muted); font-variant-numeric: tabular-nums; }
@media print {
  .ell-nav, .bar, .crumbs, .gc-bar, .syn-nav, .syn-check, .syn-links, .syn-toc, .lk-pop, #keypad { display: none !important; }
  .gc-card, .syn-doc .card { box-shadow: none !important; background: #fff !important; color: #000 !important; border-color: #999 !important; }
  .gc-card * { color: #000 !important; }
  .gc-test td.gc-hide { color: #000 !important; background: none !important; }
}
`;
  if (!document.getElementById("syn-css")) { const st = document.createElement("style"); st.id = "syn-css"; st.textContent = CSS; document.head.appendChild(st); }

  const linksHTML = (E, b) => !b.links.length ? "" : `<nav class="syn-links"><span class="syn-links-h">Go deeper in the app</span><ul>${b.links.map((l) =>
    `<li><a href="${E.esc(l.href)}"><span class="lk-k">${E.esc(l.kind)}</span><span lang="el">${E.esc(l.el)}</span></a></li>`).join("")}</ul></nav>`;

  function block(E, b, ctx) {
    if (b.p != null) return `<p>${E.md(b.p)}</p>`;
    if (b.tip != null) return `<div class="callout syn-tip"><p>${E.md(b.tip)}</p></div>`;
    if (b.list) return `<ul class="ref-notes">${b.list.map((x) => `<li>${E.md(x)}</li>`).join("")}</ul>`;
    if (b.ex) return `<ul class="ex-list syn-ex">${b.ex.map((x) => `<li><span class="ex-el" lang="el">${E.md(x.el)}</span>${x.en ? `<span class="ex-en">${E.md(x.en)}</span>` : ""}</li>`).join("")}</ul>`;
    if (b.links) return linksHTML(E, b);
    if (b.table) {
      const t = b.table, blank = t.head.every((h) => !h);
      return `<div class="tbl-wrap"><table class="syn-tbl">${blank ? "" : `<thead><tr>${t.head.map((h) => `<th scope="col">${E.md(h)}</th>`).join("")}</tr></thead>`}
        <tbody>${t.rows.map((r) => `<tr>${r.map((c, i) => i === 0 && !blank ? `<th scope="row">${E.md(c)}</th>` : `<td>${E.md(c)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
    }
    if (b.check) return `<div class="syn-check"><span class="syn-ex-h">Exercises</span>${b.check.map((q) => {
      ctx.n++;
      const kind = { choice: "Choose", order: "Put the words in order", write: "Write" }[q.type];
      const head = `<span class="syn-kind">${kind}</span><p class="q-prompt">${E.md(q.q)}</p>`;
      const tail = `<p class="ex-en syn-ans" hidden></p><p class="ex-en syn-why" hidden></p>`;
      if (q.type === "choice") return `<div class="syn-q" data-i="${ctx.n}">${head}<div class="options">${q.options.map((o) => `<button class="opt" lang="el">${E.md(o)}</button>`).join("")}</div>${tail}</div>`;
      if (q.type === "order") return `<div class="syn-q" data-i="${ctx.n}">${head}<div class="syn-built" lang="el" aria-live="polite"></div><div class="syn-tiles"></div>
        <div class="syn-acts"><button class="btn small syn-check-btn">Check</button><button class="btn small ghost syn-undo">Undo</button></div>${tail}</div>`;
      return `<div class="syn-q" data-i="${ctx.n}">${head}<form class="answer-row"><input lang="el" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Greek"><button class="btn">Check</button></form>${tail}</div>`;
    }).join("")}</div>`;
    return "";
  }

  // Grading: case, punctuation, quotes and spacing never count; final ν (τη/την, δε/δεν, μη/μην) and accents count as "almost".
  const ACC = { "ά": "α", "έ": "ε", "ή": "η", "ί": "ι", "ό": "ο", "ύ": "υ", "ώ": "ω", "ΐ": "ϊ", "ΰ": "ϋ" };
  const norm = (s) => String(s).normalize("NFC").toLowerCase().replace(/[’‘`]/g, "'").replace(/ό,\s?τι/g, "ό|τι")
    .replace(/[.,;;!?·«»"“”()…\-–—]/g, " ").replace(/σ(?=\s|$)/g, "ς").replace(/\s+/g, " ").trim();
  const loose = (s) => norm(s).replace(/[άέήίόύώΐΰ]/g, (c) => ACC[c]).replace(/(^|\s)(σ?τη|αυτη|δε|μη|καμια)ν(?=\s|$)/g, "$1$2");
  const grade = (input, forms) => forms.some((f) => norm(f) === norm(input)) ? "right" : forms.some((f) => loose(f) === loose(input)) ? "almost" : "wrong";
  const words = (s) => String(s).replace(/[.;;!?·]+$/, "").split(/\s+/).filter(Boolean);
  const shuffle = (a, seed) => { const r = a.slice(); let x = seed || 7; for (let i = r.length - 1; i > 0; i--) { x = (x * 9301 + 49297) % 233280; const j = Math.floor((x / 233280) * (i + 1)); [r[i], r[j]] = [r[j], r[i]]; } return r; };

  function wireChecks(E, qs, onDone) {
    const boxes = [...E.view.querySelectorAll(".syn-q")];
    let right = 0, answered = 0;
    const finish = (box, q, ok, shown) => {
      answered++; if (ok) right++;
      const ans = box.querySelector(".syn-ans");
      if (shown) { ans.innerHTML = shown; ans.hidden = false; }
      if (q.why) { const w = box.querySelector(".syn-why"); w.innerHTML = E.md(q.why); w.hidden = false; }
      E.wrapGreek(ans); E.wrapGreek(box.querySelector(".syn-why"));
      onDone(right, answered, boxes.length);
    };
    const answerLine = (q) => `Answer: <span lang="el">${E.md([q.answer, ...(q.accept || [])].join(" · "))}</span>`;
    boxes.forEach((box) => {
      const q = qs[+box.dataset.i - 1];
      if (q.type === "choice") {
        box.querySelectorAll(".opt").forEach((b, k) => (b.onclick = () => {
          box.querySelectorAll(".opt").forEach((x, j) => { x.disabled = true; if (q.options[j] === q.answer) x.classList.add("right"); });
          const ok = q.options[k] === q.answer; if (!ok) b.classList.add("wrong");
          finish(box, q, ok, "");
        }));
      } else if (q.type === "order") {
        const ws = words(q.answer), end = (q.answer.match(/[.;;!?·]+$/) || [""])[0];
        // the first word is shown in lower case so its capital does not give the order away (no exercise starts with a name)
        const tiles = shuffle(ws.map((w, i) => ({ w: i === 0 ? w.charAt(0).toLowerCase() + w.slice(1) : w, i })), +box.dataset.i * 31 + ws.length);
        const built = box.querySelector(".syn-built"), tl = box.querySelector(".syn-tiles"), picked = [];
        tl.innerHTML = tiles.map((t, k) => `<button class="syn-tile" data-k="${k}" lang="el">${E.esc(t.w)}</button>`).join("");
        const draw = () => { built.textContent = picked.map((k) => tiles[k].w).join(" "); };
        tl.querySelectorAll(".syn-tile").forEach((b) => (b.onclick = () => { picked.push(+b.dataset.k); b.disabled = true; draw(); }));
        box.querySelector(".syn-undo").onclick = () => { const k = picked.pop(); if (k != null) tl.querySelector(`[data-k="${k}"]`).disabled = false; draw(); };
        box.querySelector(".syn-check-btn").onclick = (ev) => {
          if (picked.length < tiles.length) { built.classList.add("wrong"); setTimeout(() => built.classList.remove("wrong"), 600); return; }
          const said = picked.map((k) => tiles[k].w).join(" ") + end;
          const ok = [q.answer, ...(q.accept || [])].some((f) => norm(f) === norm(said));
          built.classList.add(ok ? "right" : "wrong");
          tl.querySelectorAll("button").forEach((b) => (b.disabled = true)); ev.target.disabled = true; box.querySelector(".syn-undo").disabled = true;
          finish(box, q, ok, ok ? "" : answerLine(q));
        };
      } else {
        const form = box.querySelector("form"), inp = form.querySelector("input");
        form.onsubmit = (ev) => {
          ev.preventDefault(); if (!inp.value.trim()) return;
          const g = grade(inp.value, [q.answer, ...(q.accept || [])]);
          inp.classList.add(g); inp.readOnly = true; form.querySelector("button").disabled = true;
          finish(box, q, g !== "wrong", g === "right" ? "" : (g === "almost" ? "Nearly: check the accents or the final -ν. " : "") + answerLine(q));
        };
      }
    });
  }

  // Glosses for words the lexicon does not know (built from library/syntax/src/gloss.lst), shared by both shelves.
  let glossP;
  const gloss = (E) => (glossP = glossP || E.getJSON(SB + "gloss.json").catch(() => ({})));

  /* ---------- #syntax ---------- */
  routes.syntax = async (id) => {
    const E = A();
    let sec = null;
    if (id && id.includes("~")) [id, sec] = id.split("~");
    let idx = { items: [] };
    try { idx = await E.getJSON(SB + "index.json"); } catch (e) { /* not built */ }
    E.$("#bar-meta").textContent = SHEAD;
    const done = E.progress.library || {};
    if (!id) {
      document.title = SHEAD + " · Ελληνικά";
      const total = idx.items.reduce((a, x) => a + x.questions, 0);
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p>
        <h2 lang="el">Σύνταξη και λόγος</h2><p class="sub">${SHEAD}: how Greek builds sentences and texts, from word order and weak pronouns to να-chains, conditionals and reported speech. ${idx.items.length} topics, each graded from its simplest use to C1, with ${total} exercises: choose, put the words in order, or write the Greek.</p>
        <p><a class="btn ghost small" href="#cards">Pocket grammar cards</a> <a class="btn ghost small" href="downloads/textbook/Ellinika-Syntax.pdf" target="_blank" rel="noopener">PDF</a></p>
        <ul class="lessons">${idx.items.map((x, i) => `
          <li><a class="lesson-row" href="#syntax.${E.esc(x.id)}"><span class="lr-num">${i + 1}</span>
          <span class="lr-main"><span class="lr-title" lang="el">${E.esc(x.el)}</span><span class="lr-en">${E.esc(x.title)}${x.span ? " · " + E.esc(x.span) : ""}</span></span>
          ${done["syntax/" + x.id] != null ? `<span class="chip done">${Math.round(done["syntax/" + x.id] * 100)}%</span>` : `<span class="chip new">${x.questions} exercises</span>`}</a></li>`).join("")}</ul>`;
      E.wrapGreek(E.view.querySelector(".sub"));
      return window.scrollTo(0, 0);
    }
    const meta = idx.items.find((x) => x.id === id);
    if (!meta) { location.hash = "syntax"; return; }
    const d = await E.getJSON(SB + meta.file);
    document.title = d.el + " · " + SHEAD;
    E.setGloss(await gloss(E));
    const pos = idx.items.indexOf(meta), prev = idx.items[pos - 1], next = idx.items[pos + 1];
    const levels = LV.filter((l) => d.sections.some((s) => s.level === l));
    const ctx = { n: 0 }, qs = [];
    d.sections.forEach((s) => s.body.forEach((b) => b.check && qs.push(...b.check)));
    E.view.innerHTML = `<p class="crumbs"><a href="#syntax">← ${SHEAD}</a></p>
      <div class="story-head"><span class="chip">${E.esc(d.span || "")}</span><h2 lang="el">${E.esc(d.el)}</h2><span class="ex-en">${E.esc(d.title)}</span></div>
      <div class="syn-doc">
      ${d.intro.length ? `<section class="card">${d.intro.map((b) => block(E, b, ctx)).join("")}</section>` : ""}
      <details class="card syn-toc" open><summary>Contents · ${d.sections.length} parts${levels.length > 1 ? ` · ${levels[0]} to ${levels[levels.length - 1]}` : ""} · ${qs.length} exercises</summary>
        <ol>${d.sections.map((s, i) => `<li><button class="syn-jump" data-i="${i}"><span class="chip">${E.esc(s.level)}</span> <span lang="el">${E.esc(s.el)}</span> <span class="ex-en">${E.esc(s.title)}</span></button></li>`).join("")}</ol></details>
      ${d.sections.map((s, i) => `<section class="card syn-sec" id="syn-s${i}">
        <div class="syn-head"><span class="chip">${E.esc(s.level)}</span><span class="syn-n">${i + 1}</span></div>
        <h3><span lang="el">${E.esc(s.el)}</span><span class="ex-en">${E.esc(s.title)}</span></h3>
        ${s.body.map((b) => block(E, b, ctx)).join("")}</section>`).join("")}
      <p class="sub" id="syn-score"></p>
      <nav class="syn-nav">${prev ? `<a class="btn ghost" href="#syntax.${E.esc(prev.id)}">← <span lang="el">${E.esc(prev.el)}</span></a>` : "<span></span>"}
        ${next ? `<a class="btn" href="#syntax.${E.esc(next.id)}">Next: <span lang="el">${E.esc(next.el)}</span></a>` : `<a class="btn" href="#syntax">All topics</a>`}</nav>
      </div>`;
    E.wrapGreek(E.view.querySelector(".syn-doc"));
    E.view.querySelectorAll(".syn-jump").forEach((b) => (b.onclick = () => E.$("#syn-s" + b.dataset.i).scrollIntoView({ behavior: "smooth", block: "start" })));
    wireChecks(E, qs, (right, answered, total) => {
      E.$("#syn-score").textContent = `Exercises: ${right} of ${answered} right${answered < total ? `, ${total - answered} to go` : ""}`;
      if (answered === total) {
        const p = E.progress, key = "syntax/" + id;
        p.library = p.library || {}; p.library[key] = Math.max(p.library[key] || 0, right / answered); E.saveProgress();
      }
    });
    if (sec && E.$("#syn-s" + sec)) E.$("#syn-s" + sec).scrollIntoView({ block: "start" });
    else window.scrollTo(0, 0);
  };

  /* ---------- #cards ---------- */
  let cardCache = null;
  async function allCards(E) {
    if (cardCache) return cardCache;
    const idx = await E.getJSON(CB + "index.json");
    const groups = await Promise.all(idx.groups.map((g) => E.getJSON(CB + g.file)));
    return (cardCache = { idx, groups, cards: groups.flatMap((g) => g.cards.map((c) => ({ ...c, gel: g.el, gtitle: g.title }))) });
  }
  const testKey = "ellinika.cards.test";
  const getTest = () => { try { return localStorage.getItem(testKey) === "1"; } catch (e) { return false; } };
  const setTest = (v) => { try { localStorage.setItem(testKey, v ? "1" : "0"); } catch (e) { /* private mode */ } };

  routes.cards = async (id) => {
    const E = A();
    E.$("#bar-meta").textContent = CHEAD;
    let data;
    try { data = await allCards(E); } catch (e) { E.view.innerHTML = `<p>The cards could not load.</p>`; return; }
    const seen = E.progress.library || {};
    if (!id) {
      document.title = CHEAD + " · Ελληνικά";
      const n = data.cards.filter((c) => seen["cards/" + c.id]).length;
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p>
        <h2 lang="el">Κάρτες γραμματικής</h2><p class="sub">${CHEAD}: ${data.cards.length} one-page summaries, one per topic, for quick revision. Each card has the tables, the rules and the traps, and links to the lessons and guides that go deeper. Turn on <strong>Test me</strong> on a card to hide the table cells and recall them; tap a cell to check.${n ? ` You have revised ${n} of ${data.cards.length}.` : ""}</p>
        <p class="gc-bar"><a class="btn ghost small" href="downloads/textbook/Ellinika-Grammar-cards.pdf" target="_blank" rel="noopener">Printable PDF (one card per page)</a> <a class="btn ghost small" href="#syntax">Syntax and discourse guide</a></p>
        <div class="gc-groups">${data.groups.map((g) => `<section class="gc-group"><h3><span lang="el">${E.esc(g.el)}</span><span class="ex-en">${E.esc(g.title)}</span></h3>
          <div class="gc-grid">${g.cards.map((c) => `<a class="gc-tile" href="#cards.${E.esc(c.id)}"><span class="gc-meta"><span class="chip">${E.esc(c.level)}</span>${seen["cards/" + c.id] ? `<span class="chip done">✓</span>` : ""}</span>
            <span class="lr-title" lang="el">${E.esc(c.el)}</span><span class="lr-en">${E.esc(c.title)}</span></a>`).join("")}</div></section>`).join("")}</div>`;
      return window.scrollTo(0, 0);
    }
    const i = data.cards.findIndex((c) => c.id === id);
    if (i < 0) { location.hash = "cards"; return; }
    const c = data.cards[i], prev = data.cards[i - 1], next = data.cards[i + 1];
    document.title = c.el + " · " + CHEAD;
    E.setGloss(await gloss(E));
    const ctx = { n: 0 };
    E.view.innerHTML = `<p class="crumbs"><a href="#cards">← ${CHEAD}</a> · <span lang="el">${E.esc(c.gel)}</span></p>
      <article class="card gc-card" id="gc-card">
        <div class="syn-head"><span class="chip">${E.esc(c.level)}</span><span class="gc-pos">${i + 1} / ${data.cards.length}</span></div>
        <h2><span lang="el">${E.esc(c.el)}</span><span class="ex-en">${E.esc(c.title)}</span></h2>
        ${c.body.map((b) => block(E, b, ctx)).join("")}
      </article>
      <div class="gc-bar"><button class="btn small ghost" id="gc-test" aria-pressed="false">Test me</button>
        <button class="btn small ghost" id="gc-seen">${seen["cards/" + c.id] ? "Revised ✓" : "Mark as revised"}</button>
        <button class="btn small ghost" id="gc-print">Print this card</button></div>
      <nav class="syn-nav">${prev ? `<a class="btn ghost" href="#cards.${E.esc(prev.id)}">← <span lang="el">${E.esc(prev.el)}</span></a>` : "<span></span>"}
        ${next ? `<a class="btn" href="#cards.${E.esc(next.id)}">Next: <span lang="el">${E.esc(next.el)}</span></a>` : `<a class="btn" href="#cards">All cards</a>`}</nav>`;
    const card = E.$("#gc-card");
    E.wrapGreek(card);
    // Test me: hide every table cell except the row labels; tapping a cell shows it again.
    const tb = E.$("#gc-test");
    const apply = (on) => {
      tb.setAttribute("aria-pressed", on); tb.textContent = on ? "Show all" : "Test me";
      card.classList.toggle("gc-test", on);
      card.querySelectorAll("tbody td").forEach((td) => td.classList.toggle("gc-hide", on));
    };
    tb.onclick = () => { const on = tb.getAttribute("aria-pressed") !== "true"; setTest(on); apply(on); };
    card.addEventListener("click", (ev) => {
      const td = ev.target.closest("td.gc-hide");
      if (td) { ev.preventDefault(); ev.stopPropagation(); td.classList.remove("gc-hide"); }
    }, true);
    apply(getTest());
    E.$("#gc-seen").onclick = (ev) => {
      const p = E.progress; p.library = p.library || {}; p.library["cards/" + c.id] = Date.now(); E.saveProgress();
      ev.target.textContent = "Revised ✓";
    };
    E.$("#gc-print").onclick = () => window.print();
    // Swipe left or right to move between cards.
    let x0 = null, y0 = null;
    card.addEventListener("touchstart", (ev) => { if (ev.touches.length === 1) { x0 = ev.touches[0].clientX; y0 = ev.touches[0].clientY; } }, { passive: true });
    card.addEventListener("touchend", (ev) => {
      if (x0 == null) return;
      const dx = ev.changedTouches[0].clientX - x0, dy = ev.changedTouches[0].clientY - y0; x0 = null;
      if (Math.abs(dx) > 70 && Math.abs(dx) > 2 * Math.abs(dy) && !ev.target.closest(".tbl-wrap")) {
        const to = dx < 0 ? next : prev; if (to) location.hash = "cards." + to.id;
      }
    }, { passive: true });
    window.scrollTo(0, 0);
  };
})();
