/* Ελληνικά Grammar by part of speech: one document per part of speech (article, noun, verb …),
   each running from the simplest uses to the most complex. Content is data in library/pos/
   (built from library/pos/src/*.txt by build.py). Registers #pos and #pos.<id> in window.EllinikaAddons. */
(function () {
  "use strict";
  const A = () => window.Ellinika;
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});
  const BASE = "library/pos/";
  const HEAD = "Grammar by part of speech";
  const LV = ["A1", "A2", "B1", "B2", "C1"];

  const CSS = `
.pos-doc { display: grid; gap: 14px; }
.pos-doc .card { gap: 12px; }
.pos-doc p { margin: 0; }
.pos-sec { scroll-margin-top: 80px; }
.pos-sec h3 { display: grid; gap: 2px; margin: 0; font: 400 1.45rem/1.2 var(--f-display); }
.pos-sec h3 .ex-en { font-size: 0.85rem; }
.pos-sec-head { display: flex; justify-content: space-between; align-items: center; }
.pos-n { font: 600 0.8rem/1 var(--f-ui); color: var(--muted); font-variant-numeric: tabular-nums; }
.pos-tip { border-left-color: var(--terra); background: rgba(242, 193, 78, 0.07); border-radius: 0 8px 8px 0; padding: 10px 12px 10px 14px; }
.pos-ex { border-left: 2px solid var(--line); padding-left: 12px; }
table.pos-tbl td { font-size: 1rem; }
table.pos-tbl th[scope="row"] { white-space: nowrap; text-transform: none; letter-spacing: 0; font-size: 0.85rem; }
.pos-toc summary { cursor: pointer; font: 600 0.9rem/1.3 var(--f-ui); }
.pos-toc ol { margin: 0; padding-left: 0; list-style: none; display: grid; gap: 2px; }
.pos-jump { all: unset; cursor: pointer; display: block; padding: 7px 4px; border-radius: 6px; line-height: 1.35; }
.pos-jump:hover, .pos-jump:focus-visible { background: rgba(127, 127, 127, 0.12); }
.pos-jump .ex-en { margin-left: 4px; }
.pos-check { display: grid; gap: 16px; border-top: 1px dashed var(--line); padding-top: 12px; }
.pos-nav { display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap; }
`;
  if (!document.getElementById("pos-css")) { const st = document.createElement("style"); st.id = "pos-css"; st.textContent = CSS; document.head.appendChild(st); }

  function block(E, b) {
    if (b.p != null) return `<p>${E.md(b.p)}</p>`;
    if (b.tip != null) return `<div class="callout pos-tip"><p>${E.md(b.tip)}</p></div>`;
    if (b.list) return `<ul class="ref-notes">${b.list.map((x) => `<li>${E.md(x)}</li>`).join("")}</ul>`;
    if (b.ex) return `<ul class="ex-list pos-ex">${b.ex.map((x) => `<li><span class="ex-el" lang="el">${E.md(x.el)}</span>${x.en ? `<span class="ex-en">${E.md(x.en)}</span>` : ""}</li>`).join("")}</ul>`;
    if (b.table) {
      const t = b.table;
      return `<div class="tbl-wrap"><table class="pos-tbl"><thead><tr>${t.head.map((h) => `<th scope="col">${E.md(h)}</th>`).join("")}</tr></thead>
        <tbody>${t.rows.map((r) => `<tr>${r.map((c, i) => i === 0 ? `<th scope="row">${E.md(c)}</th>` : `<td>${E.md(c)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
    }
    if (b.check) return `<div class="pos-check">${b.check.map((q) => `<div class="sq" data-q="${E.esc(JSON.stringify(q))}"><p class="q-prompt">${E.md(q.q)}</p>
        <div class="options">${q.options.map((o) => `<button class="opt" lang="el">${E.esc(o)}</button>`).join("")}</div><p class="ex-en sq-why" hidden></p></div>`).join("")}</div>`;
    return "";
  }

  routes.pos = async (id) => {
    const E = A();
    // #pos.<id>~<n> opens a document at section n (for links from search).
    let sec = null;
    if (id && id.includes("~")) [id, sec] = id.split("~");
    let idx = { items: [] };
    try { idx = await E.getJSON(BASE + "index.json"); } catch (e) { /* not built */ }
    E.$("#bar-meta").textContent = HEAD;
    const done = E.progress.library || {};
    if (!id) {
      document.title = HEAD + " · Ελληνικά";
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p>
        <h2>${HEAD}</h2>
        <p class="sub">The course teaches grammar level by level. These documents take the other road: one part of speech at a time, from its simplest use to its most complex, so you can see the whole of what a noun, a pronoun or a verb does in Greek in one place.</p>
        <ul class="lessons">${idx.items.map((x, i) => `
          <li><a class="lesson-row" href="#pos.${E.esc(x.id)}"><span class="lr-num">${i + 1}</span>
          <span class="lr-main"><span class="lr-title" lang="el">${E.esc(x.el)}</span><span class="lr-en">${E.esc(x.title)}${x.span ? " · " + E.esc(x.span) : ""}</span></span>
          ${done["pos/" + x.id] != null ? `<span class="chip done">${Math.round(done["pos/" + x.id] * 100)}%</span>` : `<span class="chip new">${x.sections} parts</span>`}</a></li>`).join("")}</ul>`;
      return window.scrollTo(0, 0);
    }
    const meta = idx.items.find((x) => x.id === id);
    if (!meta) { location.hash = "pos"; return; }
    const d = await E.getJSON(BASE + meta.file);
    document.title = d.el + " · " + HEAD;
    E.setGloss({});
    const pos = idx.items.indexOf(meta), prev = idx.items[pos - 1], next = idx.items[pos + 1];
    const levels = LV.filter((l) => d.sections.some((s) => s.level === l));
    E.view.innerHTML = `<p class="crumbs"><a href="#pos">← ${HEAD}</a></p>
      <div class="story-head"><span class="chip">${E.esc(d.span || "")}</span><h2 lang="el">${E.esc(d.el)}</h2><span class="ex-en">${E.esc(d.title)}</span></div>
      <div class="pos-doc">
      ${d.intro.length ? `<section class="card pos-intro">${d.intro.map((b) => block(E, b)).join("")}</section>` : ""}
      <details class="card pos-toc" open><summary>Contents · ${d.sections.length} parts${levels.length > 1 ? ` · ${levels[0]} to ${levels[levels.length - 1]}` : ""}</summary>
        <ol>${d.sections.map((s, i) => `<li><button class="pos-jump" data-i="${i}"><span class="chip">${E.esc(s.level)}</span> <span lang="el">${E.esc(s.el)}</span> <span class="ex-en">${E.esc(s.title)}</span></button></li>`).join("")}</ol></details>
      ${d.sections.map((s, i) => `<section class="card pos-sec" id="pos-s${i}">
        <div class="pos-sec-head"><span class="chip">${E.esc(s.level)}</span><span class="pos-n">${i + 1}</span></div>
        <h3><span lang="el">${E.esc(s.el)}</span><span class="ex-en">${E.esc(s.title)}</span></h3>
        ${s.body.map((b) => block(E, b)).join("")}</section>`).join("")}
      <p class="sub" id="pos-score"></p>
      <nav class="pos-nav">${prev ? `<a class="btn ghost" href="#pos.${E.esc(prev.id)}">← <span lang="el">${E.esc(prev.el)}</span></a>` : "<span></span>"}
        ${next ? `<a class="btn" href="#pos.${E.esc(next.id)}">Next: <span lang="el">${E.esc(next.el)}</span></a>` : `<a class="btn" href="#pos">All parts of speech</a>`}</nav>
      </div>`;
    E.wrapGreek(E.view.querySelector(".pos-doc"));
    E.view.querySelectorAll(".pos-jump").forEach((b) => (b.onclick = () => E.$("#pos-s" + b.dataset.i).scrollIntoView({ behavior: "smooth", block: "start" })));
    // Self-checks: the first answer counts; the best share right across the document is saved.
    const boxes = [...E.view.querySelectorAll(".sq")];
    let right = 0, answered = 0;
    boxes.forEach((box) => {
      const q = JSON.parse(box.dataset.q);
      box.querySelectorAll(".opt").forEach((b) => (b.onclick = () => {
        box.querySelectorAll(".opt").forEach((x) => { x.disabled = true; if (x.textContent === q.answer) x.classList.add("right"); });
        if (b.textContent === q.answer) right++; else b.classList.add("wrong");
        if (q.why) { const w = box.querySelector(".sq-why"); w.innerHTML = E.md(q.why); w.hidden = false; E.wrapGreek(w); }
        answered++;
        E.$("#pos-score").textContent = `Self-checks: ${right} of ${answered} right${answered < boxes.length ? `, ${boxes.length - answered} to go` : ""}`;
        if (answered === boxes.length) {
          const p = E.progress, key = "pos/" + id;
          p.library = p.library || {}; p.library[key] = Math.max(p.library[key] || 0, right / answered); E.saveProgress();
        }
      }));
    });
    if (sec && E.$("#pos-s" + sec)) E.$("#pos-s" + sec).scrollIntoView({ block: "start" });
    else window.scrollTo(0, 0);
  };
})();
