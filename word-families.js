/* Ελληνικά Word families and False friends: two Resources shelves.
   #families, #families.<chapter>, #families.mix   roots, prefixes and suffixes with the families they generate
   #confusables, #confusables.<chapter>             false friends, look-alikes and near-synonyms with contrastive examples
   Data in library/families/ and library/confusables/ (built by tools/wordfamilies/build.py). Both end in production
   drills: the English is shown and the Greek is typed. Best scores go to progress.library["families/<id>"] and
   progress.library["confusables/<id>"]; missed words can be sent to the word recall queue (progress.vocab). */
(function () {
  "use strict";
  const A = () => window.Ellinika;
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});
  const FAM = "library/families/", CONF = "library/confusables/";
  const HEAD_F = "Word families", HEAD_C = "False friends and confusables";

  const CSS = `
.wf { display: grid; gap: 14px; }
.wf .card { gap: 12px; }
.wf p { margin: 0; }
.wf-part { display: grid; gap: 6px; margin-top: 8px; }
.wf-part h3 { margin: 0; display: flex; gap: 10px; align-items: baseline; font: 400 1.25rem/1.2 var(--f-display); }
.wf-part h3 .ex-en { font-size: 0.85rem; }
.wf-g { scroll-margin-top: 80px; }
.wf-g-head { display: grid; gap: 2px; }
.wf-key { font: 400 1.6rem/1.15 var(--f-display); color: var(--terra); overflow-wrap: anywhere; }
.wf-mean { font: 600 0.9rem/1.3 var(--f-ui); color: var(--ink); }
.wf-base { font: 400 0.85rem/1.3 var(--f-ui); color: var(--muted); }
.wf-members { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 230px), 1fr)); gap: 2px 14px; }
.wf-members li { display: grid; gap: 0; padding: 6px 0; border-bottom: 1px dashed var(--line); min-width: 0; }
.wf-members .m-el { font-size: 1.08rem; overflow-wrap: anywhere; }
.wf-members .m-en { font: 400 0.84rem/1.3 var(--f-ui); color: var(--muted); }
.wf-note { border-left: 3px solid var(--terra); padding: 4px 0 4px 12px; font-size: 0.97rem; line-height: 1.5; }
.wf-ex { border-left: 2px solid var(--line); padding-left: 12px; }
.wf-toc summary { cursor: pointer; font: 600 0.9rem/1.3 var(--f-ui); }
.wf-toc ol { margin: 8px 0 0; padding: 0; list-style: none; display: flex; flex-wrap: wrap; gap: 6px; }
.wf-jump { all: unset; cursor: pointer; border: 1px solid var(--line); border-radius: 999px; padding: 6px 10px; font: 600 0.82rem/1 var(--f-ui); }
.wf-jump:hover, .wf-jump:focus-visible { border-color: var(--terra); }
.wf-sec h3 { margin: 0; display: grid; gap: 2px; font: 400 1.3rem/1.2 var(--f-display); }
.wf-sec h3 .ex-en { font-size: 0.85rem; }
table.wf-tbl td, table.wf-tbl th { font-size: 0.95rem; }
.wf-tip { border-left: 3px solid var(--terra); background: rgba(242, 193, 78, 0.07); border-radius: 0 8px 8px 0; padding: 10px 12px 10px 14px; }
.wf-drill { display: grid; gap: 12px; }
.wf-q-en { font: 400 1.5rem/1.25 var(--f-display); color: var(--aegean); overflow-wrap: anywhere; }
.wf-q-hint { font: 400 0.88rem/1.35 var(--f-ui); color: var(--muted); }
.wf-q-hint b { color: var(--terra); font-weight: 600; }
.wf-acts { display: flex; gap: 8px; flex-wrap: wrap; }
.wf-bar { height: 4px; background: var(--line); border-radius: 2px; overflow: hidden; }
.wf-bar > i { display: block; height: 100%; background: var(--terra); transition: width .25s; }
.wf-miss { list-style: none; margin: 0; padding: 0; display: grid; gap: 4px; }
.wf-trap { font: 600 0.8rem/1.2 var(--f-ui); letter-spacing: 0.02em; color: var(--bad); }
.wf-words { display: flex; flex-wrap: wrap; gap: 8px; }
.wf-word { border: 1px solid var(--line); border-radius: 10px; padding: 8px 12px; display: grid; gap: 1px; min-width: 0; max-width: 100%; }
.wf-word .m-el { font: 400 1.25rem/1.2 var(--f-display); color: var(--aegean); overflow-wrap: anywhere; }
.wf-word .m-en { font: 400 0.84rem/1.3 var(--f-ui); color: var(--muted); }
.wf-gap { font-size: 1.15rem; line-height: 1.45; }
.wf-gap .blank { display: inline-block; min-width: 3.5em; border-bottom: 2px solid var(--terra); text-align: center; }
.wf-tabs { display: flex; gap: 8px; flex-wrap: wrap; }
.wf-tabs button[aria-pressed="true"] { background: var(--terra); border-color: var(--terra); color: #10233b; }
.wf-nav { display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap; }
`;
  if (!document.getElementById("wf-css")) { const st = document.createElement("style"); st.id = "wf-css"; st.textContent = CSS; document.head.appendChild(st); }

  /* ---------- helpers ---------- */
  const ACC = { "ά": "α", "έ": "ε", "ή": "η", "ί": "ι", "ό": "ο", "ύ": "υ", "ώ": "ω", "ΐ": "ϊ", "ΰ": "ϋ" };
  const bare = (s) => s.replace(/[άέήίόύώΐΰ]/g, (c) => ACC[c]);
  const norm = (s) => String(s).normalize("NFC").trim().toLowerCase().replace(/[’‘`]/g, "'").replace(/[.!;·?«»"]+$/g, "").replace(/\s+/g, " ").replace(/σ(?=$|\s)/g, "ς");
  // "right", "almost" (only an accent differs) or "wrong"
  function grade(input, forms, strictAccent) {
    const n = norm(input); if (!n) return "wrong";
    const ok = forms.map(norm);
    if (ok.includes(n)) return "right";
    if (ok.map(bare).includes(bare(n))) return strictAccent ? "wrong" : "almost";
    return "wrong";
  }
  const shuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  // Affix and root fragments in notes (e.g. "-είο", "γραφ-") are not words: take them out of tap lookup.
  function unwrapFragments(root) {
    root.querySelectorAll(".w").forEach((w) => {
      const prev = w.previousSibling, next = w.nextSibling;
      const before = prev && prev.nodeType === 3 ? prev.nodeValue : "", after = next && next.nodeType === 3 ? next.nodeValue : "";
      if (/-$/.test(before) || /^-/.test(after)) w.replaceWith(document.createTextNode(w.textContent));
    });
  }
  function block(E, b) {
    if (b.p != null) return `<p>${E.md(b.p)}</p>`;
    if (b.tip != null) return `<div class="wf-tip"><p>${E.md(b.tip)}</p></div>`;
    if (b.list) return `<ul class="ref-notes">${b.list.map((x) => `<li>${E.md(x)}</li>`).join("")}</ul>`;
    if (b.ex) return `<ul class="ex-list wf-ex">${b.ex.map((x) => `<li><span class="ex-el" lang="el">${E.md(x.el)}</span>${x.en ? `<span class="ex-en">${E.md(x.en)}</span>` : ""}</li>`).join("")}</ul>`;
    if (b.table) {
      const t = b.table;
      return `<div class="tbl-wrap"><table class="wf-tbl"><thead><tr>${t.head.map((h) => `<th scope="col">${E.md(h)}</th>`).join("")}</tr></thead>
        <tbody>${t.rows.map((r) => `<tr>${r.map((c, i) => i === 0 ? `<th scope="row">${E.md(c)}</th>` : `<td>${E.md(c)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
    }
    return "";
  }
  const exList = (E, ex) => ex && ex.length ? `<ul class="ex-list wf-ex">${ex.map((x) => `<li><span class="ex-el" lang="el">${E.md(x.el)}</span><span class="ex-en">${E.md(x.en)}</span></li>`).join("")}</ul>` : "";
  const scoreChip = (v, fallback) => v != null ? `<span class="chip done">${Math.round(v * 100)}%</span>` : `<span class="chip new">${fallback}</span>`;
  function saveBest(key, share) {
    const E = A(), p = E.progress;
    p.library = p.library || {}; p.library[key] = Math.max(p.library[key] || 0, share); E.saveProgress();
  }
  // Send missed words to the spaced recall queue, in the same shape as the lookup card's "+ Add to my words".
  function addToRecall(lemmas) {
    const E = A(), p = E.progress; p.vocab = p.vocab || {};
    let n = 0;
    for (const l of lemmas) if (!p.vocab[l]) { p.vocab[l] = { ivl: 0, reps: 0, lapses: 0, rec: 1, seen: Date.now(), due: Date.now() }; n++; }
    E.saveProgress(); return n;
  }

  /* ---------- typed production drill (shared) ---------- */
  // items: [{en, hint (html), answer, accept[], lex}]; done(right, total, missed[])
  function typingDrill(E, box, items, opts) {
    let i = 0, right = 0; const missed = [];
    const strict = !!opts.strictAccent;
    function show() {
      if (i >= items.length) return finish();
      const it = items[i]; let tries = 0, shown = 0;
      box.innerHTML = `<div class="wf-bar"><i style="width:${(i / items.length) * 100}%"></i></div>
        <p class="sub">${i + 1} of ${items.length} · type the Greek</p>
        <div class="wf-q-en">${E.esc(it.en)}</div>
        ${it.hint ? `<div class="wf-q-hint">${it.hint}</div>` : ""}
        <div class="answer-row"><input lang="el" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Γράψε στα ελληνικά" enterkeyhint="done"><button class="btn" data-a="check">Check</button></div>
        <div class="wf-acts"><button class="btn ghost small" data-a="letter">Show a letter</button><button class="btn ghost small" data-a="skip">I don't know</button></div>
        <div class="wf-fb"></div>`;
      E.wrapGreek(box.querySelector(".wf-q-hint")); if (box.querySelector(".wf-q-hint")) unwrapFragments(box.querySelector(".wf-q-hint"));
      const inp = box.querySelector("input"), fb = box.querySelector(".wf-fb"), forms = [it.answer, ...(it.accept || [])];
      const reveal = (cls, label) => {
        inp.disabled = true; inp.className = cls;
        box.querySelector(".wf-acts").remove();
        box.querySelector('[data-a="check"]').remove();
        fb.innerHTML = `<div class="feedback ${cls}"><strong>${label}</strong>${cls !== "right" ? `<span>Answer: <span lang="el">${E.esc(it.answer)}</span>${(it.accept || []).length ? ` <span class="ex-en">(also ${E.esc(it.accept.join(", "))})</span>` : ""}</span>` : ""}</div>
          <p style="margin-top:10px"><button class="btn" data-a="next">${i + 1 < items.length ? "Next" : "See my score"}</button></p>`;
        E.wrapGreek(fb.querySelector(".feedback"));
        const nb = fb.querySelector('[data-a="next"]'); nb.onclick = () => { i++; show(); }; nb.focus({ preventScroll: true });
        fb.scrollIntoView({ block: "nearest" });
      };
      const check = () => {
        const g = grade(inp.value, forms, strict);
        tries++;
        if (g === "right") { if (tries === 1 && !shown) right++; else missed.push(it); return reveal("right", tries === 1 && !shown ? "Right" : "Right, this time"); }
        if (g === "almost") { if (tries === 1 && !shown) right++; else missed.push(it); return reveal("almost", "Right word, check the accent"); }
        if (tries < 2) { inp.className = "wrong"; fb.innerHTML = `<div class="feedback wrong"><strong>Not quite. One more try.</strong></div>`; inp.select(); return; }
        missed.push(it); reveal("wrong", "Not this time");
      };
      box.querySelector('[data-a="check"]').onclick = check;
      inp.addEventListener("keydown", (e) => { if (e.key === "Enter") { e.preventDefault(); if (!inp.disabled) check(); } });
      box.querySelector('[data-a="letter"]').onclick = () => { shown++; inp.value = it.answer.slice(0, Math.min(it.answer.length - 1, shown)); inp.focus(); };
      box.querySelector('[data-a="skip"]').onclick = () => { missed.push(it); reveal("wrong", "Here it is"); };
      if (i > 0) inp.focus({ preventScroll: true });
    }
    function finish() { opts.done(right, items.length, missed); }
    show();
  }
  function scoreCard(E, box, right, total, missed, again) {
    const lemmas = [...new Set(missed.filter((m) => m.lex).map((m) => m.answer))];
    box.innerHTML = `<div class="wf-bar"><i style="width:100%"></i></div>
      <div class="wf-q-en">${right} of ${total} right first time</div>
      ${missed.length ? `<p class="sub">To go over:</p><ul class="wf-miss">${missed.map((m) => `<li><span lang="el">${E.esc(m.answer)}</span> <span class="ex-en">${E.esc(m.en)}</span></li>`).join("")}</ul>` : `<p>Every one on the first try.</p>`}
      <div class="wf-acts">${lemmas.length ? `<button class="btn" data-a="recall">Add ${lemmas.length} missed word${lemmas.length > 1 ? "s" : ""} to my words</button>` : ""}<button class="btn ghost" data-a="again">Another round</button></div>`;
    E.wrapGreek(box.querySelector(".wf-miss"));
    const r = box.querySelector('[data-a="recall"]');
    if (r) r.onclick = () => { const n = addToRecall(lemmas); r.outerHTML = `<span class="sub">${n ? `Added ${n}. They come up in your next practice.` : "Already in your words."}</span>`; };
    box.querySelector('[data-a="again"]').onclick = again;
  }

  /* ---------- #families ---------- */
  routes.families = async (id) => {
    const E = A();
    let idx = { items: [], parts: [] };
    try { idx = await E.getJSON(FAM + "index.json"); } catch (e) { /* not built */ }
    E.$("#bar-meta").textContent = HEAD_F;
    const done = E.progress.library || {};
    if (!id) {
      document.title = HEAD_F + " · Ελληνικά";
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p>
        <h2><span lang="el">${E.esc(idx.el || "Οικογένειες λέξεων")}</span></h2>
        <p class="sub">Roots, prefixes and suffixes, and the families of words they generate: ${idx.words || ""} words in ${idx.items.reduce((s, x) => s + x.groups, 0)} families. Learn one root and the family comes with it. Every chapter ends with a drill: you see the English and the root, you type the Greek.</p>
        <p><a class="btn" href="#families.mix">Mixed practice from every chapter</a></p>
        <div class="wf">${idx.parts.map((p) => {
          const its = idx.items.filter((x) => x.part === p.id);
          return `<section class="wf-part"><h3><span lang="el">${E.esc(p.id)}. ${E.esc(p.el)}</span><span class="ex-en">${E.esc(p.title)}</span></h3>
            <ul class="lessons">${its.map((x) => `<li><a class="lesson-row" href="#families.${E.esc(x.id)}"><span class="lr-num">${idx.items.indexOf(x) + 1}</span>
              <span class="lr-main"><span class="lr-title" lang="el">${E.esc(x.el)}</span><span class="lr-en">${E.esc(x.title)} · ${E.esc(x.level)}</span></span>
              ${scoreChip(done["families/" + x.id], x.words + " words")}</a></li>`).join("")}</ul></section>`;
        }).join("")}</div>`;
      return window.scrollTo(0, 0);
    }
    if (id === "mix") return familiesMix(E, idx);
    const meta = idx.items.find((x) => x.id === id);
    if (!meta) { location.hash = "families"; return; }
    const d = await E.getJSON(FAM + meta.file);
    document.title = d.el + " · " + HEAD_F;
    E.setGloss(d.gloss || {});
    const pos = idx.items.indexOf(meta), prev = idx.items[pos - 1], next = idx.items[pos + 1];
    E.view.innerHTML = `<p class="crumbs"><a href="#families">← ${HEAD_F}</a></p>
      <div class="story-head"><span class="chip">${E.esc(d.level)}</span><h2 lang="el">${E.esc(d.el)}</h2><span class="ex-en">${E.esc(d.title)}</span></div>
      <div class="wf">
      ${d.intro && d.intro.length ? `<section class="card">${d.intro.map((b) => block(E, b)).join("")}</section>` : ""}
      ${(d.sections || []).map((s) => `<section class="card wf-sec"><span class="chip" style="justify-self:start">${E.esc(s.level)}</span>
        <h3><span lang="el">${E.esc(s.el)}</span><span class="ex-en">${E.esc(s.title)}</span></h3>${s.body.map((b) => block(E, b)).join("")}</section>`).join("")}
      ${d.groups.length > 2 ? `<details class="card wf-toc" open><summary>${d.groups.length} families · ${d.drill.length} words to practise</summary>
        <ol>${d.groups.map((g, i) => `<li><button class="wf-jump no-look" data-i="${i}" lang="el">${E.esc(g.key)}</button></li>`).join("")}<li><button class="wf-jump" data-i="drill">Practise ↓</button></li></ol></details>` : ""}
      ${d.groups.map((g, i) => `<section class="card wf-g" id="wf-g${i}">
        <div class="wf-g-head"><span class="wf-key no-look" lang="el">${E.esc(g.key)}</span><span class="wf-mean">${E.esc(g.meaning)}</span>${g.el ? `<span class="wf-base">from <span lang="el">${E.esc(g.el)}</span></span>` : ""}</div>
        <ul class="wf-members">${g.members.map((m) => `<li><span class="m-el" lang="el">${E.esc(m.el)}</span><span class="m-en">${E.esc(m.en)}</span></li>`).join("")}</ul>
        ${g.note ? `<div class="wf-note">${E.md(g.note)}</div>` : ""}
        ${exList(E, g.ex)}</section>`).join("")}
      <section class="card wf-drill" id="wf-drill"><h3 style="margin:0">Practise: say it in Greek</h3>
        <p class="sub">${d.drill.length} words in this chapter. A round is 12 at random; you get two tries, and a missing accent counts as right with a note.${done["families/" + d.id] != null ? ` Best so far: ${Math.round(done["families/" + d.id] * 100)}%.` : ""}</p>
        <div class="wf-box"><button class="btn" data-a="start">Start a round</button></div></section>
      <nav class="wf-nav">${prev ? `<a class="btn ghost" href="#families.${E.esc(prev.id)}">← <span lang="el">${E.esc(prev.el)}</span></a>` : "<span></span>"}
        ${next ? `<a class="btn" href="#families.${E.esc(next.id)}">Next: <span lang="el">${E.esc(next.el)}</span></a>` : `<a class="btn" href="#families">All chapters</a>`}</nav>
      </div>`;
    const doc = E.view.querySelector(".wf");
    E.wrapGreek(doc); unwrapFragments(doc);
    E.view.querySelectorAll(".wf-jump").forEach((b) => (b.onclick = () => E.$(b.dataset.i === "drill" ? "#wf-drill" : "#wf-g" + b.dataset.i).scrollIntoView({ behavior: "smooth", block: "start" })));
    const box = E.view.querySelector(".wf-box");
    const round = () => {
      const items = shuffle(d.drill).slice(0, 12).map((x) => ({ ...x, hint: `<b lang="el">${E.esc(x.hint)}</b> · ${E.esc(x.meaning)}` }));
      typingDrill(E, box, items, { done: (r, t, missed) => { saveBest("families/" + d.id, r / t); scoreCard(E, box, r, t, missed, round); } });
    };
    box.querySelector('[data-a="start"]').onclick = round;
    window.scrollTo(0, 0);
  };

  async function familiesMix(E, idx) {
    document.title = "Mixed practice · " + HEAD_F;
    E.view.innerHTML = `<p class="crumbs"><a href="#families">← ${HEAD_F}</a></p><h2>Mixed practice</h2>
      <p class="sub">15 words from every part of the guide. The hint names the root or affix; you type the Greek word.</p>
      <section class="card wf-drill"><div class="wf-box"><p class="loading">Loading…</p></div></section>`;
    const docs = await Promise.all(idx.items.map((x) => E.getJSON(FAM + x.file).catch(() => null)));
    const gloss = Object.assign({}, ...docs.filter(Boolean).map((d) => d.gloss || {}));
    E.setGloss(gloss);
    const pool = docs.filter(Boolean).flatMap((d) => d.drill.map((x) => ({ ...x, ch: d.el })));
    const box = E.view.querySelector(".wf-box");
    const round = () => {
      const items = shuffle(pool).slice(0, 15).map((x) => ({ ...x, hint: `<b lang="el">${E.esc(x.hint)}</b> · ${E.esc(x.meaning)}` }));
      typingDrill(E, box, items, { done: (r, t, missed) => { saveBest("families/mix", r / t); scoreCard(E, box, r, t, missed, round); } });
    };
    round();
    window.scrollTo(0, 0);
  }

  /* ---------- #confusables ---------- */
  routes.confusables = async (id) => {
    const E = A();
    let idx = { items: [] };
    try { idx = await E.getJSON(CONF + "index.json"); } catch (e) { /* not built */ }
    E.$("#bar-meta").textContent = HEAD_C;
    const done = E.progress.library || {};
    if (!id) {
      document.title = HEAD_C + " · Ελληνικά";
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p>
        <h2><span lang="el">${E.esc(idx.el || "Ψευδόφιλοι και παρώνυμα")}</span></h2>
        <p class="sub">Words that look like English but mean something else, words that differ by one letter or one accent, and near-synonyms Greek keeps apart: ${idx.items.reduce((s, x) => s + x.pairs, 0)} sets in all, each with contrastive examples. Each chapter has two drills: choose the right word in a sentence, and say it in Greek.</p>
        <ul class="lessons">${idx.items.map((x, i) => `<li><a class="lesson-row" href="#confusables.${E.esc(x.id)}"><span class="lr-num">${i + 1}</span>
          <span class="lr-main"><span class="lr-title" lang="el">${E.esc(x.el)}</span><span class="lr-en">${E.esc(x.title)} · ${E.esc(x.level)}</span></span>
          ${scoreChip(done["confusables/" + x.id], x.pairs + " sets")}</a></li>`).join("")}</ul>`;
      return window.scrollTo(0, 0);
    }
    const meta = idx.items.find((x) => x.id === id);
    if (!meta) { location.hash = "confusables"; return; }
    const d = await E.getJSON(CONF + meta.file);
    document.title = d.el + " · " + HEAD_C;
    E.setGloss(d.gloss || {});
    const pos = idx.items.indexOf(meta), prev = idx.items[pos - 1], next = idx.items[pos + 1];
    const gaps = d.pairs.flatMap((p) => p.gaps.map((g) => ({ ...g, words: p.words })));
    const strict = d.id === "stress-pairs" || d.id === "homophones";
    E.view.innerHTML = `<p class="crumbs"><a href="#confusables">← ${HEAD_C}</a></p>
      <div class="story-head"><span class="chip">${E.esc(d.level)}</span><h2 lang="el">${E.esc(d.el)}</h2><span class="ex-en">${E.esc(d.title)}</span></div>
      <div class="wf">
      <section class="card">${d.intro.map((p) => `<p>${E.md(p)}</p>`).join("")}
        <div class="wf-acts"><button class="btn small" data-go="gaps">Choose the word ↓</button><button class="btn ghost small" data-go="say">Say it in Greek ↓</button></div></section>
      ${d.pairs.map((p) => `<section class="card">
        ${p.trap ? `<span class="wf-trap">${E.esc(p.trap)}</span>` : ""}
        <div class="wf-words">${p.words.map((w) => `<div class="wf-word"><span class="m-el" lang="el">${E.esc(w.el)}</span><span class="m-en">${E.esc(w.en)}</span></div>`).join("")}</div>
        <p>${E.md(p.note)}</p>${exList(E, p.ex)}</section>`).join("")}
      <section class="card wf-drill" id="wf-gaps"><h3 style="margin:0">Choose the right word</h3>
        <p class="sub">${gaps.length} sentences. Pick the word that fits; the translation and the reason follow.</p>
        <div class="wf-box" data-k="gaps"><button class="btn" data-a="start">Start</button></div></section>
      <section class="card wf-drill" id="wf-say"><h3 style="margin:0">Say it in Greek</h3>
        <p class="sub">${d.produce.length} words from this chapter. You see the English; type the Greek.${strict ? " Here the accent is part of the answer." : ""}</p>
        <div class="wf-box" data-k="say"><button class="btn" data-a="start">Start a round</button></div></section>
      <p class="sub" id="wf-score">${done["confusables/" + d.id] != null ? `Best so far: ${Math.round(done["confusables/" + d.id] * 100)}%.` : ""}</p>
      <nav class="wf-nav">${prev ? `<a class="btn ghost" href="#confusables.${E.esc(prev.id)}">← <span lang="el">${E.esc(prev.el)}</span></a>` : "<span></span>"}
        ${next ? `<a class="btn" href="#confusables.${E.esc(next.id)}">Next: <span lang="el">${E.esc(next.el)}</span></a>` : `<a class="btn" href="#confusables">All chapters</a>`}</nav>
      </div>`;
    const doc = E.view.querySelector(".wf");
    E.wrapGreek(doc); unwrapFragments(doc);
    E.view.querySelectorAll("[data-go]").forEach((b) => (b.onclick = () => E.$("#wf-" + b.dataset.go).scrollIntoView({ behavior: "smooth", block: "start" })));

    // Gap-fill: choose among the set's forms.
    const gbox = E.view.querySelector('[data-k="gaps"]');
    const gapRound = () => {
      const items = shuffle(gaps); let i = 0, right = 0; const missed = [];
      const show = () => {
        if (i >= items.length) {
          saveBest("confusables/" + d.id, right / items.length);
          gbox.innerHTML = `<div class="wf-bar"><i style="width:100%"></i></div><div class="wf-q-en">${right} of ${items.length} right</div>
            ${missed.length ? `<ul class="wf-miss">${missed.map((g) => `<li><span lang="el">${E.esc(g.s.replace("___", g.a))}</span></li>`).join("")}</ul>` : "<p>All of them.</p>"}
            <div class="wf-acts"><button class="btn ghost" data-a="again">Again</button></div>`;
          E.wrapGreek(gbox.querySelector(".wf-miss"));
          gbox.querySelector('[data-a="again"]').onclick = gapRound; return;
        }
        const g = items[i], opts = shuffle([g.a, ...g.o]);
        const [pre, post] = g.s.split("___");
        gbox.innerHTML = `<div class="wf-bar"><i style="width:${(i / items.length) * 100}%"></i></div><p class="sub">${i + 1} of ${items.length}</p>
          <p class="wf-gap" lang="el">${E.esc(pre)}<span class="blank no-look">…</span>${E.esc(post)}</p>
          <div class="options">${opts.map((o) => `<button class="opt" lang="el">${E.esc(o)}</button>`).join("")}</div><div class="wf-fb"></div>`;
        E.wrapGreek(gbox.querySelector(".wf-gap"));
        gbox.querySelectorAll(".opt").forEach((b) => (b.onclick = () => {
          const ok = b.textContent === g.a;
          gbox.querySelectorAll(".opt").forEach((x) => { x.disabled = true; if (x.textContent === g.a) x.classList.add("right"); });
          if (ok) right++; else { b.classList.add("wrong"); missed.push(g); }
          gbox.querySelector(".blank").textContent = g.a;
          const fb = gbox.querySelector(".wf-fb");
          fb.innerHTML = `<div class="feedback ${ok ? "right" : "wrong"}"><strong>${ok ? "Right" : "Not this one"}</strong><span class="why">${E.esc(g.en)}</span>
            <span class="why">${g.words.map((w) => `<span lang="el">${E.esc(w.el)}</span> = ${E.esc(w.en)}`).join(" · ")}</span></div>
            <p style="margin-top:10px"><button class="btn" data-a="next">${i + 1 < items.length ? "Next" : "See my score"}</button></p>`;
          E.wrapGreek(fb);
          const nb = fb.querySelector('[data-a="next"]'); nb.onclick = () => { i++; show(); }; nb.focus({ preventScroll: true });
          fb.scrollIntoView({ block: "nearest" });
        }));
      };
      show();
    };
    gbox.querySelector('[data-a="start"]').onclick = gapRound;

    // Production: English → Greek, with the set as a hint on request.
    const sbox = E.view.querySelector('[data-k="say"]');
    const sayRound = () => {
      const items = shuffle(d.produce).slice(0, 12).map((x) => ({ ...x, hint: "" }));
      typingDrill(E, sbox, items, { strictAccent: strict, done: (r, t, missed) => { saveBest("confusables/" + d.id, r / t); scoreCard(E, sbox, r, t, missed, sayRound); } });
    };
    sbox.querySelector('[data-a="start"]').onclick = sayRound;
    window.scrollTo(0, 0);
  };
})();
