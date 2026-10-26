/* Ελληνικά Writing workbook (Τετράδιο γραπτού λόγου): graded letters, emails, opinion pieces, essays, reports and speeches
   for the B2 writing paper and beyond, with model texts, a connectives bank and a correction checklist.
   Content is data in library/tetradio/ (built from tools/tetradio/src/*.py by tools/tetradio/build.py).
   Registers #tetradio and #tetradio.<id> in window.EllinikaAddons. Drafts are saved in progress.library.drafts["tetradio/<task>"],
   drill scores in progress.library["tetradio/<id>"], checklist ticks in localStorage "ellinika.tetradio.checks". */
(function () {
  "use strict";
  const A = () => window.Ellinika;
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});
  const BASE = "library/tetradio/";
  const HEAD = "Writing workbook";
  const REG = { "Φ": "friendly", "Ο": "neutral", "Ε": "formal" };
  const GREEK = /[Ͱ-Ͽἀ-῿]+/g;

  const CSS = `
.tt-doc { display: grid; gap: 14px; }
.tt-doc .card { gap: 12px; }
.tt-doc p { margin: 0; }
.tt-doc h3 { margin: 0; display: grid; gap: 2px; font: 400 1.35rem/1.2 var(--f-display); }
.tt-doc h3 .ex-en { font-size: 0.85rem; }
.tt-tip { border-left-color: var(--terra); background: rgba(242, 193, 78, 0.07); border-radius: 0 8px 8px 0; padding: 10px 12px 10px 14px; }
.tt-tools { display: flex; gap: 8px; flex-wrap: wrap; margin: 4px 0 2px; }
.tt-part { margin: 18px 0 6px; display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; }
.tt-part h3 { margin: 0; font: 400 1.25rem/1.2 var(--f-display); }
.tt-text { display: grid; gap: 10px; font-size: 1.06rem; line-height: 1.6; }
.tt-text p { white-space: pre-line; }
.tt-task { border-left: 3px solid var(--line); padding-left: 12px; }
.tt-before { opacity: 0.8; font-style: italic; }
.tt-doc mark.tt-con { background: none; color: inherit; border-radius: 3px; }
.tt-hl mark.tt-con { background: rgba(242, 193, 78, 0.28); box-shadow: 0 0 0 1px rgba(242, 193, 78, 0.35); }
.tt-bar { display: flex; gap: 8px; flex-wrap: wrap; align-items: center; justify-content: space-between; }
.tt-notes { margin: 0; padding-left: 18px; display: grid; gap: 6px; }
.tt-ph { display: grid; gap: 4px; }
.tt-ph li { display: grid; gap: 1px; }
.tt-draft textarea { width: 100%; box-sizing: border-box; min-height: 220px; font: inherit; font-size: 1rem; line-height: 1.5; padding: 10px; border-radius: 10px; border: 1px solid var(--line); background: transparent; color: inherit; resize: vertical; }
.tt-plan { margin: 0; padding-left: 18px; display: grid; gap: 4px; }
.tt-check-item { display: grid; grid-template-columns: auto 1fr; gap: 10px; align-items: start; padding: 6px 0; border-bottom: 1px dashed var(--line); }
.tt-check-item:last-child { border-bottom: 0; }
.tt-check-item input { width: 20px; height: 20px; margin-top: 2px; }
.tt-wr { display: grid; gap: 2px; margin-top: 4px; font-size: 0.92rem; }
.tt-wr .bad { text-decoration: line-through; text-decoration-color: #d9534f; opacity: 0.8; }
.tt-wr .good::before { content: "✓ "; color: #3c9d5d; }
.tt-con-row { display: grid; gap: 3px; padding: 8px 0; border-bottom: 1px dashed var(--line); }
.tt-con-row:last-child { border-bottom: 0; }
.tt-con-head { display: flex; gap: 8px; align-items: baseline; flex-wrap: wrap; }
.tt-con-head strong { font-size: 1.05rem; }
.tt-reg { font: 600 0.72rem/1 var(--f-ui); padding: 3px 6px; border-radius: 6px; border: 1px solid var(--line); }
.tt-filter { display: flex; gap: 6px; flex-wrap: wrap; }
.tt-filter input { flex: 1 1 160px; min-width: 0; padding: 8px 10px; border-radius: 10px; border: 1px solid var(--line); background: transparent; color: inherit; font: inherit; }
.tt-filter .chip { cursor: pointer; }
.tt-filter .chip.on { outline: 2px solid currentColor; }
.tt-sq { display: grid; gap: 8px; }
.tt-nav { display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap; }
table.tt-tbl td, table.tt-tbl th { font-size: 0.95rem; vertical-align: top; }
table.tt-tbl th[scope="row"] { text-transform: none; letter-spacing: 0; font-weight: 600; min-width: 7.5em; }
table.tt-tbl th[scope="row"] .ex-en { font-weight: 400; font-size: 0.82rem; }
`;
  if (!document.getElementById("tt-css")) { const st = document.createElement("style"); st.id = "tt-css"; st.textContent = CSS; document.head.appendChild(st); }

  const wc = (s) => (String(s || "").match(/[\p{L}\p{N}]+(?:['’][\p{L}]+)?/gu) || []).length;
  const ls = { get(k, d) { try { const v = localStorage.getItem(k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } }, set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* storage off */ } } };

  function block(E, b) {
    if (b.p != null) return `<p>${E.md(b.p)}</p>`;
    if (b.tip != null) return `<div class="callout tt-tip"><p>${E.md(b.tip)}</p></div>`;
    if (b.list) return `<ul class="ref-notes">${b.list.map((x) => `<li>${E.md(x)}</li>`).join("")}</ul>`;
    if (b.table) {
      const t = b.table;
      return `<div class="tbl-wrap"><table class="tt-tbl"><thead><tr>${t.head.map((h) => `<th scope="col">${E.md(h)}</th>`).join("")}</tr></thead>
        <tbody>${t.rows.map((r) => `<tr>${r.map((c) => `<td>${E.md(c)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
    }
    return "";
  }

  // Connective phrases for highlighting, longest first; "…" splits a correlative into its parts.
  let conRe = null;
  async function connectives(E) {
    if (conRe) return conRe;
    try {
      const bank = await E.getJSON(BASE + "connectives.json");
      const set = new Set();
      for (const g of bank.groups) for (const c of g.items) {
        if (c.hl === false) continue;
        for (const v of c.el.split(" / ")) for (const part of v.replace(/\(.*?\)/g, " ").split("…")) {
          const s = part.trim().replace(/[.,;]$/, ""); if (s && !/^(να|ότι)$/.test(s)) set.add(s);
        }
      }
      const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
      conRe = new RegExp(`(^|[^\\p{L}])(${[...set].sort((a, b) => b.length - a.length).map(esc).join("|")})(?![\\p{L}])`, "giu");
    } catch (e) { conRe = /$^/; }
    return conRe;
  }
  const mark = (html, re) => html.replace(/>([^<]+)</g, (m, t) => ">" + t.replace(re, (x, pre, w) => `${pre}<mark class="tt-con">${w}</mark>`) + "<");

  function textBlock(E, paras, re) {
    return `<div class="tt-text" lang="el">${paras.map((p) => mark(`<p>${E.md(p)}</p>`, re)).join("")}</div>`;
  }

  function drills(E, list) {
    if (!list || !list.length) return "";
    return `<section class="card"><h3><span lang="el">Ασκήσεις</span><span class="ex-en">Quick check · ${list.length} questions</span></h3>
      ${list.map((q) => `<div class="sq tt-sq" data-q="${E.esc(JSON.stringify(q))}"><p class="q-prompt" lang="el">${E.md(q.q)}</p>
        <div class="options">${q.options.map((o) => `<button class="opt" lang="el">${E.esc(o)}</button>`).join("")}</div><p class="ex-en sq-why" hidden></p></div>`).join("")}
      <p class="sub" id="tt-score"></p></section>`;
  }

  function wireDrills(E, id) {
    const boxes = [...E.view.querySelectorAll(".sq")];
    let right = 0, answered = 0;
    boxes.forEach((box) => {
      const q = JSON.parse(box.dataset.q);
      box.querySelectorAll(".opt").forEach((b) => (b.onclick = () => {
        box.querySelectorAll(".opt").forEach((x) => { x.disabled = true; if (x.textContent === q.answer) x.classList.add("right"); });
        if (b.textContent === q.answer) right++; else b.classList.add("wrong");
        if (q.why) { const w = box.querySelector(".sq-why"); w.innerHTML = E.md(q.why); w.hidden = false; E.wrapGreek(w); }
        answered++;
        E.$("#tt-score").textContent = `${right} of ${answered} right${answered < boxes.length ? `, ${boxes.length - answered} to go` : ""}`;
        if (answered === boxes.length) {
          const p = E.progress, key = "tetradio/" + id;
          p.library = p.library || {}; p.library[key] = Math.max(p.library[key] || 0, right / answered); E.saveProgress();
        }
      }));
    });
  }

  function drafts(E) { const lib = E.progress.library || (E.progress.library = {}); return lib.drafts || (lib.drafts = {}); }

  function taskCard(E, t, re, i) {
    const d = drafts(E)["tetradio/" + t.id] || "";
    return `<section class="card tt-task-card" id="tt-task-${i}">
      <div class="tt-bar"><span><span class="chip">${E.esc(t.level)}</span> <span class="chip">${t.words} words</span></span><span class="sub">Task ${i + 1}</span></div>
      <div class="tt-task" lang="el"><p>${E.md(t.el)}</p></div>
      <details><summary>English</summary><p class="ex-en">${E.md(t.en)}</p></details>
      ${t.plan ? `<div><p class="sub">Plan</p><ul class="tt-plan">${t.plan.map((x) => `<li>${E.md(x)}</li>`).join("")}</ul></div>` : ""}
      <div class="tt-draft"><textarea lang="el" spellcheck="true" autocomplete="off" placeholder="Γράψτε εδώ…" data-task="${E.esc(t.id)}" data-target="${t.words}">${E.esc(d)}</textarea>
        <div class="tt-bar"><span class="sub tt-count"></span><span class="tt-tools"><a class="btn ghost" href="#tetradio.checklist">Checklist</a><button class="btn ghost tt-copy">Copy</button></span></div></div>
      ${t.model ? `<details class="tt-model"><summary>Model answer · ${t.model_words} words (open after you have written and checked yours)</summary>
        ${textBlock(E, t.model, re)}<details><summary>English translation</summary><div class="tt-text">${t.model_en.map((p) => `<p>${E.md(p)}</p>`).join("")}</div></details></details>` : ""}
    </section>`;
  }

  function wireDrafts(E) {
    E.view.querySelectorAll(".tt-draft").forEach((box) => {
      const ta = box.querySelector("textarea"), out = box.querySelector(".tt-count"), target = +ta.dataset.target;
      let timer;
      const sync = (save) => {
        const n = wc(ta.value), lo = Math.round(target * 0.9), hi = Math.round(target * 1.1);
        out.textContent = `${n} / ${target} words${n ? (n < lo ? " · a little short" : n > hi ? " · a little long" : " · on target") : ""}`;
        if (save) { clearTimeout(timer); timer = setTimeout(() => { drafts(E)["tetradio/" + ta.dataset.task] = ta.value; E.saveProgress(); }, 450); }
      };
      ta.oninput = () => sync(true); sync(false);
      box.querySelector(".tt-copy").onclick = async (ev) => {
        const b = ev.currentTarget;
        try { await navigator.clipboard.writeText(ta.value); b.textContent = "Copied"; } catch (e) { ta.select(); b.textContent = "Selected"; }
        setTimeout(() => (b.textContent = "Copy"), 1500);
      };
    });
  }

  async function unit(E, d, idx, re) {
    const parts = [];
    if ((d.intro || []).length) parts.push(`<section class="card">${d.intro.map((b) => block(E, b)).join("")}</section>`);
    if (d.structure) parts.push(`<section class="card"><h3><span lang="el">Η δομή</span><span class="ex-en">Structure</span></h3>
      <div class="tbl-wrap"><table class="tt-tbl"><tbody>${d.structure.map((r) => `<tr><th scope="row" lang="el">${E.esc(r[0])}<div class="ex-en">${E.esc(r[1])}</div></th><td>${E.md(r[2])}</td></tr>`).join("")}</tbody></table></div></section>`);
    (d.sections || []).forEach((s) => parts.push(`<section class="card"><h3><span lang="el">${E.esc(s.el)}</span><span class="ex-en">${E.esc(s.en)}</span></h3>${s.body.map((b) => block(E, b)).join("")}</section>`));
    (d.models || []).forEach((m, i) => parts.push(`<section class="card">
      <div class="tt-bar"><span><span class="chip">${E.esc(m.level)}</span> <span class="chip">${m.words} words</span></span><button class="btn ghost tt-hl-btn" aria-pressed="false">Show connectives</button></div>
      <h3><span lang="el">${E.esc(m.el)}</span><span class="ex-en">Model text${d.models.length > 1 ? " " + (i + 1) : ""} · ${E.esc(m.en)}</span></h3>
      <div class="tt-task" lang="el"><p>${E.md(m.task_el)}</p></div><details><summary>English</summary><p class="ex-en">${E.md(m.task_en)}</p></details>
      ${m.before ? `<div><p class="sub">Before</p><p class="tt-before" lang="el">${E.md(m.before)}</p><p class="sub">After</p></div>` : ""}
      ${textBlock(E, m.text, re)}
      <details><summary>English translation</summary><div class="tt-text">${m.text_en.map((p) => `<p>${E.md(p)}</p>`).join("")}</div></details>
      <div><p class="sub">Why it works</p><ul class="tt-notes">${m.notes.map((n) => `<li>${E.md(n)}</li>`).join("")}</ul></div></section>`));
    if (d.phrases) parts.push(`<section class="card"><h3><span lang="el">Χρήσιμες φράσεις</span><span class="ex-en">Phrases to borrow</span></h3>
      ${d.phrases.map((g) => `<details open><summary><span lang="el">${E.esc(g.el)}</span> · ${E.esc(g.en)}</summary><ul class="ex-list tt-ph">${g.items.map((x) => `<li><span class="ex-el" lang="el">${E.esc(x.el)}${x.reg ? ` <span class="tt-reg" title="${REG[x.reg]}">${x.reg}</span>` : ""}</span><span class="ex-en">${E.esc(x.en)}</span></li>`).join("")}</ul></details>`).join("")}</section>`);
    (d.grammar || []).forEach((g) => parts.push(`<section class="card"><h3><span lang="el">Γραμματική</span><span class="ex-en">${E.esc(g.title)}</span></h3><p>${E.md(g.en)}</p>
      <ul class="ex-list">${g.examples.map((x) => `<li><span class="ex-el" lang="el">${E.esc(x.el)}</span><span class="ex-en">${E.esc(x.en)}</span></li>`).join("")}</ul></section>`));
    parts.push(drills(E, d.drills));
    if (d.tasks && d.tasks.length) parts.push(`<h3 class="tt-part"><span lang="el">Γράψτε</span> <span class="ex-en">Your turn · drafts are saved on this device</span></h3>` + d.tasks.map((t, i) => taskCard(E, t, re, i)).join(""));
    return parts.join("");
  }

  function bank(E, d) {
    const groups = d.groups.map((g) => `<section class="card tt-group" data-g="${g.id}"><h3><span lang="el">${E.esc(g.el)}</span><span class="ex-en">${E.esc(g.en)}</span></h3>
      ${g.items.map((c) => `<div class="tt-con-row" data-reg="${c.reg}" data-s="${E.esc((c.el + " " + c.en).toLowerCase())}">
        <div class="tt-con-head"><strong lang="el">${E.esc(c.el)}</strong><span class="tt-reg" title="${REG[c.reg]}">${c.reg}</span><span class="ex-en">${E.esc(c.en)}</span></div>
        ${c.note ? `<span class="sub">${E.md(c.note)}</span>` : ""}
        <span class="ex-el" lang="el">${E.esc(c.ex.el)}</span><span class="ex-en">${E.esc(c.ex.en)}</span></div>`).join("")}</section>`).join("");
    return `<section class="card">${d.intro.map((b) => block(E, b)).join("")}
      <div class="tt-filter"><input type="search" id="tt-q" placeholder="Search: e.g. however, ωστόσο" aria-label="Search connectives">
        ${["all", "Φ", "Ο", "Ε"].map((r) => `<button class="chip${r === "all" ? " on" : ""}" data-r="${r}">${r === "all" ? "All" : r + " " + REG[r]}</button>`).join("")}</div>
      <div class="tt-tools">${d.groups.map((g) => `<button class="chip tt-jump" data-g="${g.id}" lang="el">${E.esc(g.el)}</button>`).join("")}</div></section>
      ${groups}
      ${(d.sections || []).map((s) => `<section class="card"><h3><span lang="el">${E.esc(s.el)}</span><span class="ex-en">${E.esc(s.en)}</span></h3>${s.body.map((b) => block(E, b)).join("")}</section>`).join("")}
      ${drills(E, d.drills)}`;
  }

  function wireBank(E) {
    let reg = "all";
    const apply = () => {
      const q = (E.$("#tt-q").value || "").trim().toLowerCase();
      E.view.querySelectorAll(".tt-group").forEach((g) => {
        let any = false;
        g.querySelectorAll(".tt-con-row").forEach((r) => { const ok = (reg === "all" || r.dataset.reg === reg) && (!q || r.dataset.s.includes(q)); r.hidden = !ok; any = any || ok; });
        g.hidden = !any;
      });
    };
    E.$("#tt-q").oninput = apply;
    E.view.querySelectorAll(".tt-filter .chip").forEach((b) => (b.onclick = () => { reg = b.dataset.r; E.view.querySelectorAll(".tt-filter .chip").forEach((x) => x.classList.toggle("on", x === b)); apply(); }));
    E.view.querySelectorAll(".tt-jump").forEach((b) => (b.onclick = () => E.view.querySelector(`.tt-group[data-g="${b.dataset.g}"]`).scrollIntoView({ behavior: "smooth", block: "start" })));
  }

  const CK = "ellinika.tetradio.checks";
  function checklist(E, d) {
    const done = ls.get(CK, {});
    return `<section class="card">${d.intro.map((b) => block(E, b)).join("")}<div class="tt-bar"><span class="sub" id="tt-ck-n"></span><button class="btn ghost" id="tt-ck-reset">Reset for a new text</button></div></section>
      ${d.checks.map((s, si) => `<section class="card"><h3><span lang="el">${E.esc(s.el)}</span><span class="ex-en">${E.esc(s.en)}</span></h3>
        ${s.items.map((k, ki) => { const id = `${si}-${ki}`; return `<label class="tt-check-item"><input type="checkbox" data-k="${id}"${done[id] ? " checked" : ""}>
          <span><span lang="el">${E.esc(k.el)}</span><br><span class="ex-en">${E.md(k.en)}</span>
          ${k.wrong ? `<span class="tt-wr"><span class="bad" lang="el">${E.esc(k.wrong)}</span><span class="good" lang="el">${E.esc(k.right)}</span></span>` : ""}</span></label>`; }).join("")}</section>`).join("")}`;
  }
  function wireChecklist(E) {
    const boxes = [...E.view.querySelectorAll(".tt-check-item input")];
    const count = () => (E.$("#tt-ck-n").textContent = `${boxes.filter((b) => b.checked).length} of ${boxes.length} checked`);
    boxes.forEach((b) => (b.onchange = () => { const d = ls.get(CK, {}); if (b.checked) d[b.dataset.k] = 1; else delete d[b.dataset.k]; ls.set(CK, d); count(); }));
    E.$("#tt-ck-reset").onclick = () => { ls.set(CK, {}); boxes.forEach((b) => (b.checked = false)); count(); };
    count();
  }

  routes.tetradio = async (id) => {
    const E = A();
    let idx = { items: [], parts: [] };
    try { idx = await E.getJSON(BASE + "index.json"); } catch (e) { /* not built */ }
    E.$("#bar-meta").textContent = HEAD;
    const prog = E.progress.library || {}, dr = drafts(E);
    if (!id) {
      document.title = HEAD + " · Ελληνικά";
      let n = 0;
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p>
        <h2 lang="el">${E.esc(idx.el || "Τετράδιο γραπτού λόγου")}</h2>
        <p class="sub">Graded writing for the B2 exam and beyond: friendly letters and emails (Part A), formal letters (Part B), then opinion articles, reviews, essays, reports and speeches at Γ1 level. Each unit has an annotated model, phrases to borrow, a grammar point, quick drills and three tasks with a saved draft box and model answers.</p>
        <div class="tt-tools"><a class="btn" href="#tetradio.connectives">Connectives bank</a><a class="btn ghost" href="#tetradio.checklist">Correction checklist</a><a class="btn ghost" href="#writingcoach">Official prompts</a></div>
        ${idx.parts.filter((p) => p.id !== "tools").map((p) => {
          const its = idx.items.filter((x) => x.part === p.id);
          return `<div class="tt-part"><h3 lang="el">${E.esc(p.el)}</h3><span class="ex-en">${E.esc(p.en)}${p.level ? " · " + E.esc(p.level) : ""}</span></div>
          <ul class="lessons">${its.map((x) => { n++; const wrote = x.tasks.filter((t) => wc(dr["tetradio/" + t]) >= 30).length, sc = prog["tetradio/" + x.id];
            return `<li><a class="lesson-row" href="#tetradio.${E.esc(x.id)}"><span class="lr-num">${n}</span>
            <span class="lr-main"><span class="lr-title" lang="el">${E.esc(x.el)}</span><span class="lr-en">${E.esc(x.level)} · ${E.esc(x.title)}</span></span>
            ${wrote ? `<span class="chip done">✎ ${wrote}/${x.tasks.length}</span>` : sc != null ? `<span class="chip done">${Math.round(sc * 100)}%</span>` : `<span class="chip new">${x.tasks.length ? x.tasks.length + " tasks" : "guide"}</span>`}</a></li>`; }).join("")}</ul>`;
        }).join("")}`;
      E.wrapGreek(E.view);
      return window.scrollTo(0, 0);
    }
    const meta = idx.items.find((x) => x.id === id);
    if (!meta) { location.hash = "tetradio"; return; }
    const d = await E.getJSON(BASE + meta.file);
    document.title = d.el + " · " + HEAD;
    E.setGloss(d.gloss || {});
    const re = await connectives(E);
    const order = idx.items.filter((x) => x.part !== "tools"), pos = order.indexOf(meta), prev = order[pos - 1], next = order[pos + 1];
    const body = d.kind === "bank" ? bank(E, d) : d.kind === "checklist" ? checklist(E, d) : await unit(E, d, idx, re);
    E.view.innerHTML = `<p class="crumbs"><a href="#tetradio">← ${HEAD}</a></p>
      <div class="story-head"><span class="chip">${E.esc(d.level)}</span><h2 lang="el">${E.esc(d.el)}</h2><span class="ex-en">${E.esc(d.title)}</span></div>
      <div class="tt-doc">${body}
      <nav class="tt-nav">${pos > 0 && prev ? `<a class="btn ghost" href="#tetradio.${E.esc(prev.id)}">← <span lang="el">${E.esc(prev.el)}</span></a>` : `<span></span>`}
        ${pos >= 0 && next ? `<a class="btn" href="#tetradio.${E.esc(next.id)}">Next: <span lang="el">${E.esc(next.el)}</span></a>` : `<a class="btn" href="#tetradio">All units</a>`}</nav></div>`;
    E.wrapGreek(E.view.querySelector(".tt-doc"));
    E.view.querySelectorAll(".tt-hl-btn").forEach((b) => (b.onclick = () => {
      const card = b.closest(".card"), on = !card.classList.contains("tt-hl");
      card.classList.toggle("tt-hl", on); b.setAttribute("aria-pressed", on); b.textContent = on ? "Hide connectives" : "Show connectives";
      card.querySelectorAll(".tt-model").forEach((m) => m.classList.toggle("tt-hl", on));
    }));
    E.view.querySelectorAll(".tt-model").forEach((m) => m.addEventListener("toggle", () => { if (m.open) m.classList.add("tt-hl"); }));
    wireDrills(E, d.id);
    if (d.kind === "bank") wireBank(E);
    if (d.kind === "checklist") wireChecklist(E);
    wireDrafts(E);
    window.scrollTo(0, 0);
  };
})();
