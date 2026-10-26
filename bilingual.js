/* Ελληνικά bilingual readers: long chapters with Greek text and a fuller English parallel, new-term definitions,
   graded grammar notes, numbered sources, a quiz and words to keep.
   Registers one route per shelf in SHELVES (#<shelf> and #<shelf>.<chapter>) in window.EllinikaAddons.
   Content is data: library/<shelf>/index.json lists parts (and optional themes) and chapters; each chapter is library/<shelf>/<file>.
   The reading mode (Greek only / Greek with English / English only) is kept in localStorage "ellinika.bilingual.mode", so it is per profile. */
(function () {
  "use strict";
  const A = () => window.Ellinika;
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});
  const SHELVES = { philosophers: "Philosophers", istoria: "History of the Greeks", simera: "Greece today", politeia: "The Greek polity", kouzina: "The Greek kitchen", mousiki: "Greek music", skini: "Theatre and cinema", eortes: "The Orthodox year", athlitismos: "Greek sport", mathiatriki: "Maths and medicine", epistimi: "Science and technology", nisia: "The Greek islands", diaspora: "The Greek diaspora" };
  const MODE_KEY = "ellinika.bilingual.mode";
  const MODES = [["el", "Ελληνικά"], ["both", "Δίγλωσσο"], ["en", "English"]];

  const css = `
.bl-hero { margin: 4px 0 18px; }
.bl-hero h2 { margin: 0 0 4px; font: 400 2rem/1.15 var(--f-display); }
.bl-hero .bl-intro { margin: 10px 0 0; }
.bl-intro p { margin: 0 0 8px; }
.bl-intro .en { color: var(--muted); font-size: .95rem; }
.bl-see { margin: 0 0 14px; line-height: 1.7; }
.bl-toc { display: flex; flex-wrap: wrap; gap: 6px; margin: 12px 0 0; }
.bl-part { margin: 26px 0 8px; }
.bl-part h3 { margin: 0; font: 600 1.1rem/1.3 var(--f-ui); }
.bl-part h3 .el { display: block; font: 400 1.35rem/1.25 var(--f-display); }
.bl-part .bl-dates { font: 500 .8rem/1.3 var(--f-ui); color: var(--terra); letter-spacing: .03em; }
.bl-part .bl-intro { margin: 8px 0 0; font-size: .95rem; }
.lesson-row .lr-dates { display: block; font: 400 .78rem/1.3 var(--f-ui); color: var(--muted); }
.bl-row-chips { display: flex; flex-wrap: wrap; gap: 4px; justify-content: flex-end; }
.chip.bl-theme { background: var(--aegean-soft); color: var(--ink); }
.bl-head { display: grid; gap: 6px; margin: 4px 0 14px; }
.bl-head h2 { margin: 0; font: 400 2rem/1.15 var(--f-display); }
.bl-head .bl-en { font: 500 1rem/1.3 var(--f-ui); color: var(--muted); }
.bl-chips { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; }
.bl-fig { margin: 0 0 16px; }
.bl-fig img { display: block; width: 100%; max-height: 62vh; object-fit: contain; background: var(--paper); border-radius: 10px; border: 1px solid var(--line); }
.bl-fig figcaption { font: 400 .8rem/1.4 var(--f-ui); color: var(--muted); margin: 6px 0 0; }
.bl-bar { position: sticky; top: var(--bar-h, calc(env(safe-area-inset-top, 0px) + 49px)); z-index: 4; display: flex; gap: 8px; flex-wrap: wrap; align-items: center; padding: 8px 0; background: var(--paper); border-bottom: 1px solid var(--line); margin: 0 0 12px; }
.bl-seg { display: inline-flex; border: 1px solid var(--line); border-radius: 999px; overflow: hidden; }
.bl-seg button { border: 0; background: transparent; color: var(--ink); font: 500 .82rem/1 var(--f-ui); padding: 8px 12px; min-height: 36px; cursor: pointer; }
.bl-seg button[aria-pressed="true"] { background: var(--aegean, #0a2747); color: #fff; }
.bl-jump { flex: 1 1 140px; min-width: 0; max-width: 100%; font: 500 .85rem/1.2 var(--f-ui); padding: 7px 8px; border-radius: 8px; border: 1px solid var(--line); background: var(--card); color: var(--ink); }
.bl-brief { margin: 0 0 18px; }
.bl-brief p { margin: 0; }
.bl-sec { margin: 26px 0 0; scroll-margin-top: 110px; }
.bl-sec > h3 { margin: 0 0 10px; font: 600 1.15rem/1.3 var(--f-ui); }
.bl-sec > h3 .el { display: block; font: 400 1.3rem/1.3 var(--f-display); }
.bl-p { margin: 0 0 16px; }
.bl-p .el { margin: 0; font-size: 1.06rem; line-height: 1.65; }
.bl-p .en { margin: 6px 0 0; padding: 0 0 0 12px; border-left: 3px solid var(--line); color: var(--muted); font-size: .95rem; line-height: 1.6; }
.bl-text[data-mode="el"] .en, .bl-text[data-mode="el"] .bl-sec > h3 .en-h { display: none; }
.bl-text[data-mode="en"] .el { display: none; }
.bl-text[data-mode="en"] .en { border-left: 0; padding: 0; color: var(--ink); font-size: 1rem; }
.bl-cite { font: 600 .7rem/1 var(--f-ui); vertical-align: super; margin-left: 2px; text-decoration: none; color: var(--terra); }
.bl-text[data-mode="el"] .el .bl-cite-el { display: inline; }
.bl-cite-el { display: none; }
.bl-terms { display: grid; gap: 10px; margin: 0; }
.bl-terms dt { font: 600 1.02rem/1.3 var(--f-body); }
.bl-terms dt .sub { font: 400 .85rem/1.3 var(--f-ui); }
.bl-terms dd { margin: 2px 0 0; font-size: .95rem; }
.bl-terms dd .en { display: block; color: var(--muted); font-size: .9rem; }
.bl-gram { border-top: 1px solid var(--line); padding: 12px 0 0; margin: 12px 0 0; }
.bl-gram:first-of-type { border-top: 0; margin-top: 0; padding-top: 0; }
.bl-gram h4 { margin: 0 0 6px; font: 600 1rem/1.3 var(--f-ui); display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
.bl-gram p { margin: 0 0 6px; }
.bl-gram ul { margin: 6px 0 0; padding-left: 18px; }
.bl-gram li { margin: 0 0 4px; }
.bl-gram li .ex-en { display: block; }
.bl-listen ul { margin: 0; padding-left: 20px; } .bl-listen li { margin: 0 0 8px; overflow-wrap: anywhere; } .bl-listen .ex-en { display: block; }
.bl-src ol { margin: 0; padding-left: 22px; font-size: .9rem; }
.bl-src li { margin: 0 0 6px; overflow-wrap: anywhere; scroll-margin-top: 110px; }
.bl-src li:target { background: var(--aegean-soft); border-radius: 6px; }
.bl-recipe .bl-rmeta { display: flex; flex-wrap: wrap; gap: 6px 14px; margin: 0 0 10px; font: 500 .85rem/1.3 var(--f-ui); color: var(--muted); }
.bl-recipe h4 { margin: 14px 0 6px; font: 600 1rem/1.3 var(--f-ui); color: var(--terra); }
.bl-ing { margin: 0; padding-left: 20px; }
.bl-ing li { margin: 0 0 6px; }
.bl-ing .el, .bl-steps .el { margin: 0; }
.bl-ing .en { display: block; color: var(--muted); font-size: .88rem; }
.bl-steps { margin: 0; padding-left: 24px; }
.bl-steps li { margin: 0 0 12px; }
.bl-steps .el { font-size: 1.04rem; line-height: 1.6; }
.bl-steps .en { margin: 4px 0 0; color: var(--muted); font-size: .93rem; line-height: 1.55; }
.bl-tip { margin: 12px 0 0; padding: 10px 12px; border-radius: 8px; background: var(--aegean-soft); }
.bl-tip p { margin: 0; } .bl-tip .en { margin-top: 4px; color: var(--muted); font-size: .92rem; }
.bl-text[data-mode="en"] .bl-ing .en, .bl-text[data-mode="en"] .bl-steps .en, .bl-text[data-mode="en"] .bl-tip .en { color: var(--ink); font-size: 1rem; }
.bl-tblwrap { overflow-x: auto; margin: 4px 0 16px; -webkit-overflow-scrolling: touch; }
.bl-tblcap { font: 600 .92rem/1.3 var(--f-ui); margin: 8px 0 6px; }
.bl-tbl { border-collapse: collapse; width: 100%; font-size: .93rem; }
.bl-tbl th, .bl-tbl td { text-align: left; vertical-align: top; padding: 6px 8px; border-bottom: 1px solid var(--line); }
.bl-tbl th { font: 600 .8rem/1.3 var(--f-ui); color: var(--muted); }
.bl-tbl td[lang="el"] { font-weight: 500; }
.bl-nav { display: flex; gap: 8px; flex-wrap: wrap; margin: 20px 0 0; }
.bl-nav .btn { max-width: 100%; white-space: normal; text-align: left; }
`;
  function style() {
    if (document.getElementById("bl-style")) return;
    const s = document.createElement("style"); s.id = "bl-style"; s.textContent = css; document.head.append(s);
  }
  const mode = () => { try { const m = localStorage.getItem(MODE_KEY); return MODES.some((x) => x[0] === m) ? m : "both"; } catch (e) { return "both"; } };
  const setMode = (m) => { try { localStorage.setItem(MODE_KEY, m); } catch (e) { /* private mode */ } };
  const intro = (E, o) => (o.intro_el || o.intro_en ? `<div class="bl-intro">${o.intro_el ? `<p lang="el" class="el">${E.esc(o.intro_el)}</p>` : ""}${o.intro_en ? `<p class="en">${E.esc(o.intro_en)}</p>` : ""}</div>` : "");

  // Optional blocks (cookbook shelf): section.tables = [{el, en, cols: [{h, lang}], rows: [[cell…]]}] and
  // chapter.recipe = {serves_el, serves_en, time_el, time_en, groups: [{el, en, items: [{el, en}]}], steps: [{el, en}], tips: [{el, en}]}.
  function table(E, t) {
    const cols = t.cols || [];
    return `${t.el || t.en ? `<p class="bl-tblcap"><span lang="el">${E.esc(t.el || "")}</span>${t.en ? ` <span class="no-look">· ${E.esc(t.en)}</span>` : ""}</p>` : ""}<div class="bl-tblwrap"><table class="bl-tbl">
      <thead><tr>${cols.map((c) => `<th>${E.esc(c.h)}</th>`).join("")}</tr></thead>
      <tbody>${(t.rows || []).map((r) => `<tr>${r.map((v, i) => `<td${cols[i]?.lang === "el" ? ' lang="el"' : ' class="no-look"'}>${E.esc(v)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
  }
  function recipe(E, r, m) {
    const pair = (x, tag) => `<${tag} class="el" lang="el">${E.esc(x.el)}</${tag}>${x.en ? `<${tag} class="en">${E.esc(x.en)}</${tag}>` : ""}`;
    const meta = [[r.serves_el, r.serves_en], [r.time_el, r.time_en]].filter((x) => x[0] || x[1]);
    return `<section class="card bl-sec bl-recipe" id="bl-recipe"><h3><span class="el" lang="el">Η συνταγή</span>The recipe</h3>
      ${meta.length ? `<p class="bl-rmeta">${meta.map(([g, e]) => `<span><span lang="el">${E.esc(g || "")}</span>${e ? ` <span class="no-look">· ${E.esc(e)}</span>` : ""}</span>`).join("")}</p>` : ""}
      <div class="bl-text" data-mode="${m}">${(r.groups || []).map((g) => `<h4><span lang="el">${E.esc(g.el || "Υλικά")}</span>${g.en ? ` <span class="no-look">· ${E.esc(g.en)}</span>` : ""}</h4>
        <ul class="bl-ing">${g.items.map((x) => `<li>${pair(x, "span")}</li>`).join("")}</ul>`).join("")}
      <h4><span lang="el">Εκτέλεση</span> <span class="no-look">· Method</span></h4>
      <ol class="bl-steps">${(r.steps || []).map((x) => `<li>${pair(x, "p")}</li>`).join("")}</ol>
      ${(r.tips || []).map((x) => `<div class="bl-tip">${pair(x, "p")}</div>`).join("")}</div></section>`;
  }

  async function shelf(sh, heading) {
    const E = A(), idx = await E.getJSON(`library/${sh}/index.json`), done = E.progress.library || {};
    const themes = Object.fromEntries((idx.themes || []).map((t) => [t.id, t]));
    document.title = (idx.el || heading) + " · Ελληνικά";
    E.$("#bar-meta").textContent = idx.title || heading;
    const row = (x) => {
      const th = x.theme && themes[x.theme], key = sh + "/" + x.id;
      return `<li><a class="lesson-row" href="#${sh}.${E.esc(x.id)}"><span class="lr-num">${idx.items.indexOf(x) + 1}</span>
        <span class="lr-main"><span class="lr-title" lang="el">${E.esc(x.el)}</span><span class="lr-en">${E.esc(x.title)}</span>${x.dates ? `<span class="lr-dates">${E.esc(x.dates)}</span>` : ""}</span>
        <span class="bl-row-chips">${th ? `<span class="chip bl-theme" lang="el">${E.esc(th.el)}</span>` : ""}${x.level ? `<span class="chip">${E.esc(x.level)}</span>` : ""}${done[key] != null ? `<span class="chip done">${Math.round(done[key] * 100)}%</span>` : ""}</span></a></li>`;
    };
    const parts = idx.parts?.length ? idx.parts : [{ id: "", el: "", en: "" }];
    E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p>
      <div class="bl-hero"><h2 lang="el">${E.esc(idx.el || heading)}</h2><span class="ex-en">${E.esc(idx.title || "")}</span>${intro(E, idx)}
      ${idx.parts?.length > 1 ? `<nav class="bl-toc">${parts.map((p) => `<a class="chip" href="#${sh}" data-part="${E.esc(p.id)}" lang="el">${E.esc(p.el)}</a>`).join("")}</nav>` : ""}</div>
      ${parts.map((p) => {
        const items = idx.items.filter((x) => !p.id || x.part === p.id);
        return `${p.el || p.en ? `<div class="bl-part" id="part-${E.esc(p.id)}"><h3><span class="el" lang="el">${E.esc(p.el)}</span>${E.esc(p.en || "")}</h3>${p.dates ? `<span class="bl-dates">${E.esc(p.dates)}</span>` : ""}${intro(E, p)}</div>` : ""}
          <ul class="lessons">${items.map(row).join("")}</ul>`;
      }).join("")}`;
    E.view.querySelectorAll(".bl-toc a").forEach((a) => (a.onclick = (e) => { e.preventDefault(); E.$("#part-" + a.dataset.part)?.scrollIntoView({ behavior: "smooth" }); }));
    E.wrapGreek(E.view.querySelector(".bl-hero .bl-intro"));
    window.scrollTo(0, 0);
  }

  async function chapter(sh, heading, id) {
    const E = A(), idx = await E.getJSON(`library/${sh}/index.json`);
    const meta = idx.items.find((x) => x.id === id);
    if (!meta) { location.hash = sh; return; }
    const ch = await E.getJSON(`library/${sh}/${meta.file}`), key = sh + "/" + id;
    const th = (idx.themes || []).find((t) => t.id === (ch.theme || meta.theme));
    const pos = idx.items.indexOf(meta), prev = idx.items[pos - 1], next = idx.items[pos + 1];
    document.title = ch.el + " · " + (idx.el || heading);
    E.$("#bar-meta").textContent = idx.el || heading;
    E.setGloss(ch.gloss);
    const srcIds = new Set((ch.sources || []).map((s) => s.n));
    const cites = (p) => (p.cite || []).filter((n) => srcIds.has(n)).map((n) => `<a class="bl-cite" href="#${sh}.${E.esc(id)}" data-src="${n}" aria-label="Source ${n}">[${n}]</a>`).join("");
    const m = mode(), img = ch.image;
    E.view.innerHTML = `<p class="crumbs"><a href="#${sh}">← ${E.esc(idx.el || heading)}</a></p>
      <div class="bl-head"><div class="bl-chips"><span class="chip">${E.esc(ch.level || meta.level || "")}</span>${th ? `<span class="chip bl-theme" lang="el">${E.esc(th.el)}</span>` : ""}${ch.dates || meta.dates ? `<span class="sub">${E.esc(ch.dates || meta.dates)}</span>` : ""}</div>
        <h2 lang="el">${E.esc(ch.el)}</h2><span class="bl-en">${E.esc(ch.title)}</span></div>
      ${img ? `<figure class="bl-fig"><img src="${E.esc(img.file)}" alt="${E.esc(img.caption_en || img.caption || "")}" loading="lazy"><figcaption><span lang="el">${E.esc(img.caption || "")}</span>${img.caption_en ? ` <span class="no-look">· ${E.esc(img.caption_en)}</span>` : ""}<br><span class="no-look">${E.esc(img.credit || "")}${img.license ? " · " + E.esc(img.license) : ""}${img.source ? ` · <a href="${E.esc(img.source)}" target="_blank" rel="noopener">source</a>` : ""}</span></figcaption></figure>` : ""}
      ${ch.summary_en ? `<section class="card bl-brief"><h3>In brief</h3><p>${E.md(ch.summary_en)}</p></section>` : ""}
      ${ch.see?.length ? `<p class="bl-see sub"><span lang="el">Δείτε επίσης</span> · See also: ${ch.see.map((x) => `<a href="${E.esc(x.href)}"><span lang="el">${E.esc(x.el)}</span></a>`).join(" · ")}</p>` : ""}
      <div class="bl-bar"><div class="bl-seg" role="group" aria-label="Reading mode">${MODES.map(([k, l]) => `<button type="button" data-mode="${k}" aria-pressed="${k === m}">${l}</button>`).join("")}</div>
        <select class="bl-jump" aria-label="Go to section"><option value="">Sections…</option>${(ch.sections || []).map((s) => `<option value="${E.esc(s.id)}">${E.esc(s.el)} · ${E.esc(s.en)}</option>`).join("")}${ch.recipe ? `<option value="recipe">Η συνταγή · The recipe</option>` : ""}${ch.terms?.length ? `<option value="terms">Νέοι όροι · New terms</option>` : ""}${ch.grammar?.length ? `<option value="grammar">Γραμματική · Grammar notes</option>` : ""}${ch.questions?.length ? `<option value="quiz">Ερωτήσεις · Questions</option>` : ""}${ch.sources?.length ? `<option value="sources">Πηγές · Sources</option>` : ""}</select></div>
      ${ch.terms?.length ? `<section class="card bl-sec" id="bl-terms"><h3><span class="el" lang="el">Νέοι όροι</span>New terms in this chapter</h3><dl class="bl-terms">${ch.terms.map((t) => `<div><dt lang="el">${E.esc(t.el)} <span class="sub no-look">· ${E.esc(t.en)}</span></dt><dd>${t.def_el ? `<span lang="el">${E.esc(t.def_el)}</span>` : ""}${t.def_en ? `<span class="en">${E.esc(t.def_en)}</span>` : ""}</dd></div>`).join("")}</dl></section>` : ""}
      <div class="bl-text" data-mode="${m}">${(ch.sections || []).map((s) => `<section class="bl-sec" id="bl-${E.esc(s.id)}"><h3><span class="el" lang="el">${E.esc(s.el)}</span><span class="en-h">${E.esc(s.en)}</span></h3>
        ${s.paras.map((p) => `<div class="bl-p"><p class="el" lang="el">${E.esc(p.el)}<span class="bl-cite-el no-look">${cites(p)}</span></p>${p.en ? `<p class="en">${E.esc(p.en)}${cites(p)}</p>` : ""}</div>`).join("")}${(s.tables || []).map((t) => table(E, t)).join("")}</section>`).join("")}</div>
      ${ch.recipe ? recipe(E, ch.recipe, m) : ""}
      ${ch.grammar?.length ? `<section class="card bl-sec" id="bl-grammar"><h3><span class="el" lang="el">Γραμματική</span>Grammar notes</h3>${ch.grammar.map((g) => `<div class="bl-gram"><h4>${g.level ? `<span class="chip">${E.esc(g.level)}</span>` : ""}<span>${E.esc(g.title)}</span></h4>${g.el ? `<p lang="el">${E.esc(g.el)}</p>` : ""}${g.en ? `<p>${E.md(g.en)}</p>` : ""}${g.examples?.length ? `<ul>${g.examples.map((x) => `<li><span lang="el">${E.esc(x.el)}</span><span class="ex-en">${E.esc(x.en || "")}</span></li>`).join("")}</ul>` : ""}</div>`).join("")}</section>` : ""}
      ${ch.questions?.length ? `<section class="card story-q bl-sec" id="bl-quiz"><h3>Questions</h3>${ch.questions.map((q, i) => `<div class="sq" data-i="${i}"><p class="q-prompt" lang="el">${E.esc(q.q)}</p><div class="options">${q.options.map((o) => `<button class="opt" lang="el">${E.esc(o)}</button>`).join("")}</div><p class="ex-en sq-why" hidden></p></div>`).join("")}<p class="sub" id="sq-score"></p></section>` : ""}
      ${ch.vocab?.length ? `<section class="card bl-sec"><h3>Words to keep</h3><p class="word-cloud" lang="el">${ch.vocab.map((v) => E.esc(v)).join(" · ")}</p><button class="btn small" id="bl-add">Add all to my words</button></section>` : ""}
      ${ch.listen?.length ? `<section class="card bl-sec bl-listen no-look" id="bl-listen"><h3><span class="el" lang="el">Ακούστε και δείτε</span>Listen and watch</h3><ul>${ch.listen.map((l) => `<li><a href="${E.esc(l.url)}" target="_blank" rel="noopener">${E.esc(l.title)}</a>${l.note ? `<span class="ex-en">${E.esc(l.note)}</span>` : ""}</li>`).join("")}</ul></section>` : ""}
      ${ch.sources?.length ? `<section class="bl-sec bl-src" id="bl-sources"><h3><span class="el" lang="el">Πηγές</span>Sources</h3><ol>${ch.sources.map((s) => `<li id="bl-src-${s.n}" value="${s.n}">${E.esc(s.text)}${s.url ? ` <a href="${E.esc(s.url)}" target="_blank" rel="noopener">${E.esc(s.url.replace(/^https?:\/\/(www\.)?/, "").replace(/\/$/, ""))}</a>` : ""}</li>`).join("")}</ol></section>` : ""}
      <div class="bl-nav">${prev ? `<a class="btn ghost" href="#${sh}.${E.esc(prev.id)}">← <span lang="el">${E.esc(prev.el)}</span></a>` : ""}${next ? `<a class="btn" href="#${sh}.${E.esc(next.id)}">Next: <span lang="el">${E.esc(next.el)}</span></a>` : ""}</div>`;
    const texts = E.view.querySelectorAll(".bl-text");
    E.view.querySelectorAll(".bl-seg button").forEach((b) => (b.onclick = () => {
      setMode(b.dataset.mode); texts.forEach((t) => (t.dataset.mode = b.dataset.mode));
      E.view.querySelectorAll(".bl-seg button").forEach((x) => x.setAttribute("aria-pressed", String(x === b)));
    }));
    E.view.querySelector(".bl-jump").onchange = (e) => { const t = E.$("#bl-" + e.target.value); if (t) t.scrollIntoView({ behavior: "smooth" }); e.target.value = ""; };
    E.view.querySelectorAll(".bl-cite").forEach((a) => (a.onclick = (e) => { e.preventDefault(); const li = E.$("#bl-src-" + a.dataset.src); if (!li) return; li.scrollIntoView({ behavior: "smooth", block: "center" }); E.view.querySelectorAll(".bl-src li").forEach((x) => x.style.background = ""); li.style.background = "var(--aegean-soft)"; }));
    E.view.querySelectorAll(".bl-text .el, .bl-tbl [lang=el], .bl-recipe h4 [lang=el], .bl-terms dt, .bl-terms dd > span[lang], .bl-gram [lang=el], .bl-fig figcaption > span[lang], .story-q").forEach((n) => E.wrapGreek(n));
    let right = 0, answered = 0;
    E.view.querySelectorAll(".sq").forEach((box) => {
      const q = ch.questions[box.dataset.i];
      box.querySelectorAll(".opt").forEach((b) => (b.onclick = () => {
        box.querySelectorAll(".opt").forEach((x) => { x.disabled = true; if (x.textContent === q.answer) x.classList.add("right"); });
        if (b.textContent === q.answer) right++; else b.classList.add("wrong");
        if (q.why) { const w = box.querySelector(".sq-why"); w.textContent = q.why; w.hidden = false; }
        if (++answered === ch.questions.length) {
          const p = E.progress; p.library = p.library || {}; p.library[key] = Math.max(p.library[key] || 0, right / answered); E.saveProgress();
          E.$("#sq-score").textContent = `${right} of ${answered} right`;
        }
      }));
    });
    const add = E.$("#bl-add");
    if (add) add.onclick = () => {
      const p = E.progress, v = p.vocab || (p.vocab = {}), now = Date.now(); let n = 0;
      for (const l of ch.vocab) if (!v[l]) { v[l] = { ivl: 0, reps: 0, lapses: 0, rec: 1, seen: now, due: now }; n++; }
      E.saveProgress(); add.outerHTML = `<span class="lk-state">${n} added · they come up in your next word recall</span>`;
    };
    window.scrollTo(0, 0);
  }

  for (const [sh, heading] of Object.entries(SHELVES)) {
    routes[sh] = async (id) => {
      style();
      try { await (id ? chapter(sh, heading, id) : shelf(sh, heading)); }
      catch (e) { A().view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><p>This reader could not load: ${A().esc(e.message)}</p>`; }
    };
  }
})();
