/* Σιγανή φωτιά: illustrated Greek reader (Greek edition of "Fuoco Lento"), routes #sigani and #sigani.<id>.
   Tap any Greek word for the lookup; the device's Greek voice narrates sentence by sentence with the sentence highlighted;
   each paragraph has an English line on demand; key words go into word recall; questions score into progress.library["sigani/<id>"].
   Data: library/sigani/book.json (built by tools/sigani-fotia/export_app.py). */
(function () {
  "use strict";
  const A = () => window.Ellinika;
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});
  const RATE_KEY = "ellinika.sigani.rate", EN_KEY = "ellinika.sigani.en";
  const get = (k, d) => { try { return localStorage.getItem(k) ?? d; } catch (e) { return d; } };
  const put = (k, v) => { try { localStorage.setItem(k, v); } catch (e) { /* private mode */ } };

  function style() {
    if (document.getElementById("sg-style")) return;
    const s = document.createElement("style"); s.id = "sg-style";
    s.textContent = `
.sg-hero { text-align: center; margin: 4px 0 14px; }
.sg-hero img { width: min(100%, 420px); border-radius: 12px; border: 1px solid var(--line); display: block; margin: 10px auto 0; }
.sg-hero h2 { font-size: clamp(2rem, 9vw, 2.8rem); margin: .1em 0 .1em; }
.sg-tag { font-style: italic; color: var(--muted); max-width: 34ch; margin: 0 auto; }
.sg-front p { line-height: 1.65; }
.sg-part { margin: 22px 0 8px; }
.sg-part h3 { margin: 0 0 4px; }
.sg-part .sub { display: block; }
.sg-closing { margin: 14px 0 6px; text-align: center; }
.sg-closing img { width: min(100%, 460px); border-radius: 12px; border: 1px solid var(--line); }
.sg-closing figcaption { font-style: italic; color: var(--muted); margin-top: 8px; }
.sg-eyebrow { font-size: .78rem; letter-spacing: .14em; text-transform: uppercase; color: var(--muted); }
.sg-pre { border-left: 3px solid var(--line); padding: 2px 0 2px 12px; color: var(--muted); font-style: italic; margin: 8px 0 14px; }
.sg-fig { margin: 10px 0 14px; text-align: center; }
.sg-fig img { width: min(100%, 480px); max-height: 70vh; object-fit: contain; border-radius: 10px; border: 1px solid var(--line); }
.sg-bar { position: sticky; top: calc(var(--bar-h, 56px) + env(safe-area-inset-top, 0px)); z-index: 5; display: flex; flex-wrap: wrap; gap: 8px; align-items: center; padding: 8px 10px; margin: 8px 0 12px; background: var(--paper, #fff); border: 1px solid var(--line); border-radius: 12px; }
.sg-bar select { font: inherit; }
.sg-bar .sg-now { font-size: .85rem; color: var(--muted); margin-left: auto; }
.sg-p { position: relative; margin: 0 0 14px; }
.sg-p p.el { margin: 0; font-size: 1.08rem; line-height: 1.75; }
.sg-p .sg-tools { display: flex; gap: 6px; margin-top: 4px; }
.sg-p .sg-tools button { font-size: .78rem; padding: 2px 9px; border-radius: 999px; border: 1px solid var(--line); background: transparent; color: var(--muted); cursor: pointer; }
.sg-p p.en { margin: 6px 0 0; padding-left: 12px; border-left: 3px solid var(--line); color: var(--muted); font-size: .95rem; line-height: 1.55; }
.sg-s.sg-on { background: var(--aegean-soft, #dbe9f7); border-radius: 4px; box-shadow: 0 0 0 2px var(--aegean-soft, #dbe9f7); }
.sg-lex { margin: 0; padding: 0; list-style: none; columns: 2 220px; column-gap: 20px; }
.sg-lex li { break-inside: avoid; margin: 0 0 6px; line-height: 1.4; }
.sg-lex .g { font-weight: 600; }
.sg-lex .e { color: var(--muted); font-size: .9rem; }
.sg-gram ul { margin: 0; padding-left: 1.1em; line-height: 1.55; }
.sg-gram li { margin: 0 0 4px; }
.sg-app-t { width: 100%; border-collapse: collapse; font-size: .95rem; }
.sg-app-t td { padding: 4px 6px 4px 0; vertical-align: top; border-bottom: 1px solid var(--line); }
.sg-app-t td.e { color: var(--muted); }
.sg-reflect p { font-style: italic; line-height: 1.6; }
`;
    document.head.append(s);
  }

  /* ---------- narration: the device's Greek voice, one sentence at a time ---------- */
  const greekVoices = () => new Promise((res) => {
    const ss = window.speechSynthesis; if (!ss) return res([]);
    const pick = () => ss.getVoices().filter((v) => /^el(-|_|$)/i.test(v.lang));
    const v = pick(); if (v.length) return res(v);
    let done = false; const fin = () => { if (!done) { done = true; res(pick()); } };
    ss.addEventListener?.("voiceschanged", fin, { once: true }); setTimeout(fin, 1500);
  });
  const splitSentences = (t) => (t.match(/[^.!;…]+(?:[.!;…]+[»"]?|$)\s*/g) || [t]).map((x) => x).filter((x) => x.trim());
  const sayable = (t) => t.replace(/[«»“”"]/g, "").replace(/\s+/g, " ").trim();

  let narr = null;
  window.addEventListener("hashchange", () => { narr?.stop(); });

  function narrator(E, root, voices) {
    const ss = window.speechSynthesis, sents = [...root.querySelectorAll(".sg-s")];
    const btn = root.querySelector("#sg-play"), now = root.querySelector("#sg-now");
    let rate = +get(RATE_KEY, "0.9"), at = 0, run = 0, playing = false;
    const voice = voices.find((v) => /el-GR/i.test(v.lang) && /premium|enhanced|neural|natural/i.test(v.name)) || voices.find((v) => /el-GR/i.test(v.lang)) || voices[0];
    const mark = (i) => {
      sents.forEach((s, j) => s.classList.toggle("sg-on", j === i));
      const s = sents[i]; if (!s) { now.textContent = ""; return; }
      now.textContent = `${i + 1} / ${sents.length}`;
      const r = s.getBoundingClientRect(), barB = root.querySelector(".sg-bar").getBoundingClientRect().bottom;
      if (r.top < barB + 8 || r.bottom > window.innerHeight - 24) s.scrollIntoView({ block: "center", behavior: "smooth" });
    };
    const label = () => (btn.textContent = playing ? "❚❚ Pause" : at > 0 && at < sents.length ? "▶ Resume" : "▶ Listen");
    const speakFrom = (i, stopAt) => {
      const my = ++run; ss.cancel(); playing = true; label();
      const next = (k) => {
        if (my !== run) return;
        if (k >= sents.length || (stopAt != null && k >= stopAt)) { playing = false; at = k >= sents.length ? 0 : k; mark(-1); label(); return; }
        at = k; mark(k);
        const u = new SpeechSynthesisUtterance(sayable(sents[k].textContent));
        u.lang = "el-GR"; if (voice) u.voice = voice; u.rate = rate;
        u.onend = () => setTimeout(() => next(k + 1), 180);
        u.onerror = (e) => { if (e.error !== "interrupted" && e.error !== "canceled") next(k + 1); };
        ss.speak(u);
      };
      next(i);
    };
    const ctl = {
      stop: () => { run++; ss?.cancel(); playing = false; mark(-1); label(); },
      toggle: () => { if (playing) { run++; ss.cancel(); playing = false; label(); } else speakFrom(at); },
      para: (p) => { const idx = sents.findIndex((s) => p.contains(s)); const end = sents.findIndex((s, j) => j > idx && !p.contains(s)); speakFrom(idx, end < 0 ? null : end); },
      from: (s) => speakFrom(sents.indexOf(s)),
      setRate: (r) => { rate = r; put(RATE_KEY, String(r)); if (playing) speakFrom(at); },
    };
    root.querySelector("#sg-rate").value = String(rate);
    label();
    return ctl;
  }

  /* ---------- pages ---------- */
  async function shelf(E, book) {
    const done = E.progress.library || {};
    document.title = book.el + " · Ελληνικά";
    E.$("#bar-meta").textContent = book.el;
    const row = (it, n) => `<li><a class="lesson-row" href="#sigani.${E.esc(it.id)}"><span class="lr-num">${n}</span>
      <span class="lr-main"><span class="lr-title" lang="el">${E.esc(it.el)}</span><span class="lr-en">${E.esc(it.eyebrow)}</span></span>
      <span class="bl-row-chips"><span class="chip">${E.esc(it.level.split("·").pop().trim())}</span>${done["sigani/" + it.id] != null ? `<span class="chip done">${Math.round(done["sigani/" + it.id] * 100)}%</span>` : ""}</span></a></li>`;
    let n = 0;
    E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p>
      <div class="sg-hero"><span class="sg-eyebrow no-look">Illustrated stories · B2–C1</span><h2 lang="el">${E.esc(book.el)}</h2>
        <p class="sg-tag" lang="el">${E.esc(book.tagline)}</p><img src="${E.esc(book.cover)}" alt="" loading="lazy"></div>
      <details class="card sg-front"><summary>Για ποιον είναι αυτό το βιβλίο · About this book</summary>${book.front.map((p) => `<p lang="el">${p}</p>`).join("")}</details>
      ${book.parts.map((p) => `<section class="sg-part"><h3 lang="el">${E.esc(p.el)}</h3><span class="sub no-look">${E.esc(p.en)}</span>
        ${p.intro ? `<div class="card">${p.intro.map((x, i) => `<div class="sg-p" data-i="${i}"><p class="el" lang="el">${E.esc(x.el)}</p><div class="sg-tools no-look"><button class="sg-en">English</button></div><p class="en" hidden>${E.esc(x.en)}</p></div>`).join("")}</div>` : ""}
        <ul class="lessons">${book.items.filter((it) => it.part === p.id).map((it) => row(it, n++)).join("")}</ul>
        <figure class="sg-closing"><img src="${E.esc(p.closing.file)}" alt="${E.esc(p.closing.alt)}" loading="lazy"><figcaption lang="el">${E.esc(p.closing.caption)}</figcaption></figure></section>`).join("")}
      <ul class="lessons"><li><a class="lesson-row" href="#sigani.lexilogio"><span class="lr-num">★</span><span class="lr-main"><span class="lr-title" lang="el">${E.esc(book.appendix.el)}</span><span class="lr-en">Vocabulary of the senses and questions to think about</span></span></a></li></ul>
      <p class="sub"><a href="${E.esc(book.pdf)}" target="_blank" rel="noopener">The book as a PDF</a></p>`;
    E.view.querySelectorAll(".sg-en").forEach((b) => (b.onclick = () => { const en = b.closest(".sg-p").querySelector(".en"); en.hidden = !en.hidden; }));
    E.wrapGreek(E.view.querySelector(".sg-hero")); E.view.querySelectorAll(".sg-front, .sg-part .card, .sg-closing figcaption").forEach((x) => E.wrapGreek(x));
    window.scrollTo(0, 0);
  }

  function addWords(E, lemmas, btn) {
    const p = E.progress, v = p.vocab || (p.vocab = {}), now = Date.now(); let n = 0;
    for (const l of lemmas) if (!v[l]) { v[l] = { ivl: 0, reps: 0, lapses: 0, rec: 1, seen: now, due: now }; n++; }
    E.saveProgress(); btn.outerHTML = `<span class="lk-state">${n ? `${n} added · they come up in your next word recall` : "All of these are already in your words"}</span>`;
  }

  async function story(E, book, id) {
    const pos = book.items.findIndex((x) => x.id === id), it = book.items[pos];
    if (!it) { location.hash = "sigani"; return; }
    const prev = book.items[pos - 1], next = book.items[pos + 1], showEn = get(EN_KEY, "0") === "1";
    document.title = it.el + " · " + book.el;
    E.$("#bar-meta").textContent = book.el;
    E.setGloss(book.gloss);
    const para = (p, i) => `<div class="sg-p" data-i="${i}"><p class="el" lang="el">${splitSentences(p.el).map((s) => `<span class="sg-s">${E.esc(s)}</span>`).join("")}</p>
      <div class="sg-tools no-look"><button class="sg-say" aria-label="Read this paragraph aloud">▶ Paragraph</button><button class="sg-en">English</button></div><p class="en"${showEn ? "" : " hidden"}>${E.esc(p.en)}</p></div>`;
    E.view.innerHTML = `<p class="crumbs"><a href="#sigani">← ${E.esc(book.el)}</a></p>
      <span class="sg-eyebrow" lang="el">${E.esc(it.eyebrow)}</span><h2 lang="el" style="margin:.15em 0 .3em">${E.esc(it.el)}</h2><span class="chip">${E.esc(it.level)}</span>
      ${it.pre ? `<p class="sg-pre no-look"><b>Before you read.</b> ${E.esc(it.pre)}</p>` : ""}
      ${it.images.map((im) => `<figure class="sg-fig"><img src="${E.esc(im.file)}" alt="${E.esc(im.alt)}" loading="lazy"></figure>`).join("")}
      <div class="sg-bar no-look"><button class="btn small" id="sg-play">▶ Listen</button><button class="btn small ghost" id="sg-stop">■</button>
        <label class="sub">Speed <select id="sg-rate"><option value="0.7">slow</option><option value="0.9">normal</option><option value="1.05">fast</option></select></label>
        <label class="sub"><input type="checkbox" id="sg-all-en"${showEn ? " checked" : ""}> English</label><span class="sg-now" id="sg-now"></span></div>
      <p class="sub no-look" id="sg-novoice" hidden>This device has no Greek voice, so the story can't be read aloud here. On iPhone: Settings → Accessibility → Spoken Content → Voices → Greek.</p>
      <section class="sg-text">${it.paras.map(para).join("")}</section>
      <section class="card"><h3><span lang="el">Βασικό λεξιλόγιο</span> <span class="sub no-look">· Key words</span></h3>
        <ul class="sg-lex">${it.lex.map((x) => `<li><span class="g" lang="el">${E.esc(x.el)}</span> <span class="e no-look">${E.esc(x.en)}</span></li>`).join("")}</ul>
        ${it.vocab.length ? `<p><button class="btn small" id="sg-add">Add ${it.vocab.length} words to my recall</button></p>` : ""}</section>
      <section class="card sg-gram"><h3><span lang="el">Γραμματική</span> <span class="sub no-look">· What to notice</span></h3><ul lang="el">${it.grammar.map((g) => `<li>${g}</li>`).join("")}</ul></section>
      <section class="card story-q"><h3>Ερωτήσεις · Questions</h3>${it.questions.map((q, i) => `<div class="sq" data-i="${i}"><p class="q-prompt" lang="el">${i + 1}. ${E.esc(q.q)}</p><div class="options">${q.options.map((o) => `<button class="opt" lang="el">${E.esc(o)}</button>`).join("")}</div><p class="ex-en sq-why" lang="el" hidden></p></div>`).join("")}<p class="sub" id="sq-score"></p></section>
      <div class="bl-nav">${prev ? `<a class="btn ghost" href="#sigani.${E.esc(prev.id)}">← <span lang="el">${E.esc(prev.el)}</span></a>` : ""}${next ? `<a class="btn" href="#sigani.${E.esc(next.id)}">Next: <span lang="el">${E.esc(next.el)}</span></a>` : `<a class="btn" href="#sigani.lexilogio">Next: <span lang="el">${E.esc(book.appendix.el)}</span></a>`}</div>`;
    E.view.querySelectorAll(".sg-text p.el, .sg-lex .g, .sg-gram ul, .story-q, .sg-eyebrow, h2[lang=el]").forEach((n) => E.wrapGreek(n));
    E.view.querySelectorAll(".sg-en").forEach((b) => (b.onclick = () => { const en = b.closest(".sg-p").querySelector(".en"); en.hidden = !en.hidden; }));
    E.$("#sg-all-en").onchange = (e) => { put(EN_KEY, e.target.checked ? "1" : "0"); E.view.querySelectorAll(".sg-text .en").forEach((x) => (x.hidden = !e.target.checked)); };
    const add = E.$("#sg-add"); if (add) add.onclick = () => addWords(E, it.vocab, add);
    // questions
    let right = 0, answered = 0;
    E.view.querySelectorAll(".sq").forEach((box) => {
      const q = it.questions[box.dataset.i];
      box.querySelectorAll(".opt").forEach((b) => (b.onclick = () => {
        if (box.dataset.done) return; box.dataset.done = "1";
        box.querySelectorAll(".opt").forEach((x) => { x.disabled = true; if (x.textContent === q.answer) x.classList.add("right"); });
        if (b.textContent === q.answer) right++; else b.classList.add("wrong");
        const w = box.querySelector(".sq-why"); w.textContent = q.why; w.hidden = false;
        if (++answered === it.questions.length) {
          const p = E.progress; p.library = p.library || {}; p.library["sigani/" + it.id] = Math.max(p.library["sigani/" + it.id] || 0, right / answered); E.saveProgress();
          E.$("#sq-score").textContent = `${right} of ${answered} right`;
        }
      }));
    });
    // narration
    const voices = await greekVoices();
    if (!voices.length) { E.$("#sg-novoice").hidden = false; E.view.querySelectorAll("#sg-play, #sg-stop, #sg-rate, .sg-say").forEach((b) => (b.disabled = true)); window.scrollTo(0, 0); return; }
    narr = narrator(E, E.view, voices);
    E.$("#sg-play").onclick = () => narr.toggle();
    E.$("#sg-stop").onclick = () => narr.stop();
    E.$("#sg-rate").onchange = (e) => narr.setRate(+e.target.value);
    E.view.querySelectorAll(".sg-say").forEach((b) => (b.onclick = () => narr.para(b.closest(".sg-p"))));
    window.scrollTo(0, 0);
  }

  async function appendix(E, book) {
    document.title = book.appendix.el + " · " + book.el;
    E.$("#bar-meta").textContent = book.el;
    E.setGloss(book.gloss);
    E.view.innerHTML = `<p class="crumbs"><a href="#sigani">← ${E.esc(book.el)}</a></p>
      <h2 lang="el">${E.esc(book.appendix.el)}</h2><p class="sub" lang="el">${E.esc(book.appendix.sub)}</p>
      ${book.appendix.groups.map((g) => `<section class="card"><h3 lang="el">${E.esc(g.el)}</h3><table class="sg-app-t">${g.rows.map((r) => `<tr><td lang="el">${E.esc(r.el)}</td><td class="e no-look">${E.esc(r.en)}</td></tr>`).join("")}</table></section>`).join("")}
      <section class="card sg-reflect"><h3 lang="el">Για σκέψη</h3>${book.reflect.map((r) => `<p lang="el">${E.esc(r)}</p>`).join("")}
        <p class="sub no-look">Write your answer in the writing workbook or say it aloud; tap any word you need.</p></section>`;
    E.view.querySelectorAll("[lang=el]").forEach((n) => E.wrapGreek(n));
    window.scrollTo(0, 0);
  }

  routes.sigani = async (id) => {
    const E = A(); style();
    try {
      const book = await E.getJSON("library/sigani/book.json");
      if (!id) return shelf(E, book);
      if (id === "lexilogio") return appendix(E, book);
      return story(E, book, id);
    } catch (e) { E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><p>This reader could not load: ${E.esc(e.message)}</p>`; }
  };
})();
