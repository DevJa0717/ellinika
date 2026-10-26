/* Ελληνικά Library: reference tables, readings and worksheets that sit beside the course.
   Registers routes in window.EllinikaAddons; app.js calls them for #library, #ref and the other library pages.
   Content is data: app/library/index.json lists the shelves, and each shelf reads its own JSON files,
   so new material is added by dropping a file in and listing it there. */
(function () {
  "use strict";
  const A = () => window.Ellinika;
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});

  /* ---------- generic paradigm renderer ---------- */
  // Any nested object of forms becomes a grid: the case/person/number key in each path is the row,
  // everything else in the path is the column. Objects too wide for one grid split by their top key.
  const ROWS = ["nom", "acc", "gen", "voc", "nom_acc", "1sg", "2sg", "3sg", "1pl", "2pl", "3pl", "sg", "pl"];
  const LABEL = {
    nom: "Nominative", acc: "Accusative", gen: "Genitive", voc: "Vocative", nom_acc: "Nom. / Acc.",
    "1sg": "1 sg", "2sg": "2 sg", "3sg": "3 sg", "1pl": "1 pl", "2pl": "2 pl", "3pl": "3 pl",
    sg: "Singular", pl: "Plural", m: "masc.", f: "fem.", n: "neut.", "m/f": "masc./fem.",
    active: "active", passive: "passive", present: "present", imperfect: "imperfect", simple_past: "simple past",
    dependent: "dependent", past: "past", imperfective_imperative: "imperative (continuous)", perfective_imperative: "imperative (perfective)",
  };
  const PERS = ["1sg", "2sg", "3sg", "1pl", "2pl", "3pl"], GORD = { m: 1, f: 2, n: 3 };
  const HIDE = new Set(["section", "pdf_pages", "pdf_page", "source", "variety", "related_files", "stopped_at", "id", "holton"]);
  const lab = (k) => LABEL[k] || String(k).replace(/_/g, " ");
  const cap = (k) => { const l = lab(k); return l.charAt(0).toUpperCase() + l.slice(1); };
  const GR = /[Ͱ-Ͽἀ-῿]/;
  const greek = (s) => `<span lang="el">${A().esc(s)}</span>`;
  // Book section references are source metadata, not teaching text, so they stay out of the page.
  const noRef = (s) => String(s).replace(/\s*\((?:see |cf\. )?§[^)]*\)/g, "").replace(/;?\s*see §[\d.]+(?:[-–,]\s*§?[\d.]+)*/g, "");
  const txt = (s) => A().md(noRef(s));

  function leaves(o, path = [], out = []) {
    if (o == null) return out;
    if (typeof o === "string" || typeof o === "number") out.push([path, String(o)]);
    else if (!Array.isArray(o) && typeof o === "object") for (const [k, v] of Object.entries(o)) if (!HIDE.has(k)) leaves(v, path.concat(k), out);
    return out;
  }
  function gridHTML(ls) {
    const rows = [], cols = [], cell = {};
    for (const [p, v] of ls) {
      // Row key: person first, then case, then number. A person row also takes its gender (3 sg masc.).
      let ri = p.findIndex((k) => PERS.includes(k));
      if (ri < 0) ri = p.findIndex((k) => ROWS.includes(k) && k !== "sg" && k !== "pl");
      if (ri < 0) ri = p.findIndex((k) => ROWS.includes(k));
      const gi = PERS.includes(p[ri]) ? p.findIndex((k) => k in GORD) : -1;
      const r = gi >= 0 ? p[ri] + "|" + p[gi] : p[ri], c = p.filter((_, i) => i !== ri && i !== gi).map(lab).join(" · ") || " ";
      if (!rows.includes(r)) rows.push(r);
      if (!cols.includes(c)) cols.push(c);
      cell[r + "|" + c] = v;
    }
    const ord = (r) => { const [x, g] = r.split("|"); return ROWS.indexOf(x) * 10 + (g ? GORD[g] : 0); };
    rows.sort((a, b) => ord(a) - ord(b));
    const showHead = cols.length > 1 || cols[0] !== " ";
    return `<div class="tbl-wrap"><table class="pdg">${showHead ? `<thead><tr><th></th>${cols.map((c) => `<th>${A().esc(c)}</th>`).join("")}</tr></thead>` : ""}
      <tbody>${rows.map((r) => `<tr><th scope="row">${r.split("|").map(lab).join(" ")}</th>${cols.map((c) => `<td lang="el">${A().esc(cell[r + "|" + c] ?? "–")}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
  }
  function gridable(o) {
    const ls = leaves(o);
    if (!ls.length || !ls.every(([p]) => p.some((k) => ROWS.includes(k)))) return null;
    const cols = new Set(ls.map(([p]) => p.filter((k) => !ROWS.includes(k)).join("|")));
    return cols.size <= 4 ? ls : null;
  }
  // Any form value as plain text: "a / b" strings stay, lists join, {form, en} keeps its gloss, {gen: …} keeps its label.
  const SHORT = { nom: "nom.", acc: "acc.", gen: "gen.", voc: "voc.", nom_acc: "nom./acc.", sg: "sg.", pl: "pl." };
  function fv(v) {
    if (v == null) return "";
    if (typeof v !== "object") return String(v);
    if (Array.isArray(v)) return v.map(fv).filter(Boolean).join(", ");
    if (v.form || v.el) return fv(v.form || v.el) + (v.en || v.gloss ? ` (${fv(v.en || v.gloss)})` : "");
    return Object.entries(v).filter(([k, x]) => !HIDE.has(k) && x != null).map(([k, x]) => `${SHORT[k] || lab(k)} ${fv(x)}`).join(", ");
  }
  // Singular → plural entries: irregular neuters ({lemma, sg: {gen}, pl: {nom, gen}}) and gender-changing plurals ({sg, pl: [{form, en}]}).
  function sgPl(x) {
    const head = x.lemma || (typeof x.sg === "string" ? x.sg : "");
    const sg = typeof x.sg === "object" && x.sg ? Object.entries(x.sg).filter(([, v]) => v != null).map(([k, v]) => `${SHORT[k] || lab(k)} sg. ${fv(v)}`).join(", ") : "";
    const pls = [].concat(x.pl ?? []).filter((p) => p != null);
    const plEl = pls.map((p) => typeof p === "object" && !p.form && !p.el
      ? Object.entries(p).filter(([, v]) => v != null).map(([k, v]) => `${SHORT[k] || lab(k)} pl. ${fv(v)}`).join(", ")
      : fv(p.form || p.el || p)).join(" · ");
    const glosses = pls.filter((p) => p && (p.en || p.gloss)).map((p) => pls.length > 1 ? `${fv(p.form || p.el)}: ${fv(p.en || p.gloss)}` : fv(p.en || p.gloss));
    const forms = [sg, plEl ? (x.lemma ? plEl : `→ ${plEl}`) : x.lemma ? "no plural" : ""].filter(Boolean).join(" · ");
    return `<li><span class="ex-el" lang="el">${A().esc(head)}${forms ? (x.lemma ? " · " : " ") + A().esc(forms) : ""}</span>${glosses.length ? `<span class="ex-en">${A().esc(glosses.join(" · "))}</span>` : ""}</li>`;
  }
  // Render anything: grids for form tables, lists for examples, prose for rules.
  function block(o, depth = 0) {
    if (o == null) return "";
    if (typeof o === "string" || typeof o === "number") return `<p>${txt(String(o))}</p>`;
    if (Array.isArray(o)) {
      if (!o.length) return "";
      if (o.every((x) => typeof x === "string")) return o.length > 6 && o.every((x) => GR.test(x) && x.length < 40)
        ? `<p class="word-cloud" lang="el">${o.map((x) => A().esc(x)).join(" · ")}</p>`
        : `<ul class="ref-notes">${o.map((x) => `<li>${txt(x)}</li>`).join("")}</ul>`;
      if (o.every((x) => x && typeof x === "object" && (x.el || x.form || x.sg))) return `<ul class="ex-list">${o.map((x) => x.el || x.form
        ? `<li><span class="ex-el" lang="el">${A().esc(fv(x.el || x.form))}</span>${x.en || x.gloss ? `<span class="ex-en">${A().esc(fv(x.en || x.gloss))}</span>` : ""}</li>`
        : sgPl(x)).join("")}</ul>`;
      return o.map((x) => `<div class="ref-sub">${block(x, depth + 1)}</div>`).join("");
    }
    const g = gridable(o);
    if (g) return gridHTML(g);
    let html = "";
    // Sibling form tables that fit side by side (present beside imperfect) merge into one grid.
    const formKids = Object.entries(o).filter(([k, v]) => !HIDE.has(k) && v && typeof v === "object" && !Array.isArray(v) && gridable(v));
    const merged = formKids.length > 1 && gridable(Object.fromEntries(formKids));
    if (merged) html += gridHTML(merged);
    for (const [k, v] of Object.entries(o)) {
      if (HIDE.has(k) || v == null) continue;
      if (merged && formKids.some(([fk]) => fk === k)) continue;
      if (typeof v === "string") { html += k === "rule" || k === "note" ? `<p>${txt(v)}</p>` : `<p><span class="ref-k">${A().esc(lab(k))}</span> ${txt(v)}</p>`; continue; }
      const inner = block(v, depth + 1);
      if (!inner) continue;
      html += ["rule", "rules", "notes", "examples"].includes(k) ? inner : `<h${Math.min(6, 4 + depth)} class="ref-h">${A().esc(lab(k))}</h${Math.min(6, 4 + depth)}>${inner}`;
    }
    return html;
  }

  /* ---------- grammar tables ---------- */
  const GEN = { m: "masculine", f: "feminine", n: "neuter" };
  async function refData() {
    const r = A().resolve;
    const [nouns, adj, pro, verbs, nums] = await Promise.all(["grammar/nouns-full.json", "grammar/adjectives.json", "grammar/pronouns-holton.json", "grammar/verbs-holton.json", "grammar/numerals.json"].map((f) => r(f).catch(() => ({}))));
    return { nouns, adj, pro, verbs, nums };
  }
  const card = (title, sub, body, attrs = "") => `<article class="card ref-card"${attrs}><div class="ref-title">${title}${sub ? ` <span class="ex-en">${sub}</span>` : ""}</div>${body}</article>`;

  function nounCard(p) {
    const forms = { sg: { ...p.sg, ...(p.voc_sg ? { voc: p.voc_sg } : {}) }, pl: { ...p.pl, ...(p.voc_pl ? { voc: p.voc_pl } : {}) } };
    return card(`${greek(p.model)}`, `${A().esc(p.gloss || "")} · ${GEN[p.gender] || p.gender || ""}`, gridHTML(leaves(forms)) +
      (p.stress ? `<p class="ref-note">${txt(p.stress)}</p>` : "") +
      (p.examples?.length ? `<p class="word-cloud" lang="el">${p.examples.map((x) => A().esc(x)).join(" · ")}</p>` : ""), ` data-words="${A().esc([p.model, ...(p.examples || [])].join(" "))}"`);
  }
  function adjCard(p) {
    return card(greek(p.model), A().esc([p.gloss, p.applies].filter(Boolean).join(" · ")),
      `<h5 class="ref-h">Singular</h5>${gridHTML(leaves(p.sg))}<h5 class="ref-h">Plural</h5>${gridHTML(leaves(p.pl))}` +
      (p.examples?.length ? `<p class="word-cloud" lang="el">${p.examples.map((x) => A().esc(x)).join(" · ")}</p>` : ""), ` data-words="${A().esc([p.model, ...(p.examples || [])].join(" "))}"`);
  }

  const TABS = [
    ["articles", "Articles", (d) => card("Definite article", "ο, η, το", `<h5 class="ref-h">Singular</h5>${gridHTML(leaves(d.nouns.articles?.definite?.sg))}<h5 class="ref-h">Plural</h5>${gridHTML(leaves(d.nouns.articles?.definite?.pl))}<p class="ref-note">${txt(d.nouns.articles?.final_n_rule || "")}</p>`)
      + card("Indefinite article", "ένας, μία, ένα", block({ m: d.nouns.articles?.indefinite?.m, f: d.nouns.articles?.indefinite?.f, n: d.nouns.articles?.indefinite?.n }) + block(d.nouns.articles?.indefinite?.notes))
      + card("σε + article", "στον, στη, στο…", block(d.nouns.articles?.se_contraction))],
    ["nouns", "Nouns", (d) => `<div class="ref-find"><input id="ref-q" type="search" lang="el" placeholder="Find a noun's pattern, e.g. πρόσφυγας" autocomplete="off"><span class="ex-en" id="ref-hit"></span></div>`
      + ["m", "f", "n"].map((g) => `<h3 class="ref-group">${GEN[g]}</h3>` + (d.nouns.paradigms || []).filter((p) => p.gender === g).map(nounCard).join("")).join("")
      + card("Irregular neuters", "", block(d.nouns.irregular_neuters)) + card("Nouns that change gender in the plural", "", block(d.nouns.gender_change_in_plural))
      + card("Common gender", "", block(d.nouns.common_gender)) + card("Indeclinable nouns", "", block(d.nouns.indeclinable)) + card("Vocative", "", block(d.nouns.vocative_notes))],
    ["adjectives", "Adjectives", (d) => `<div class="ref-find"><input id="ref-q" type="search" lang="el" placeholder="Find an adjective's pattern, e.g. βαθύς" autocomplete="off"><span class="ex-en" id="ref-hit"></span></div>`
      + (d.adj.paradigms || []).map(adjCard).join("") + card("Comparison", "πιο, -τερος, -τατος", block(d.adj.comparison)) + card("Indeclinable adjectives", "", block(d.adj.indeclinable))],
    ["pronouns", "Pronouns", (d) => Object.entries(d.pro).filter(([k, v]) => v && typeof v === "object" && !HIDE.has(k)).map(([k, v]) => card(A().esc(cap(k)), "", block(v))).join("")],
    ["verbs", "Verbs", (d) => (d.verbs.sections || []).filter((s) => Object.keys(s).some((k) => k.startsWith("paradigm"))).map((s) => {
      const p = s.paradigm || s.paradigm_έχω, model = s.model_verb || (s.paradigm_έχω ? "έχω" : s.section === "6.7" ? "είμαι" : "");
      const extra = Object.fromEntries(Object.entries(s).filter(([k]) => k.startsWith("verbs") && Array.isArray(s[k])));
      return card(greek(model), A().esc([p?.gloss, s.title].filter(Boolean).join(" · ")), block(p) + (Object.keys(extra).length ? block(extra) : "") + (s.non_finite_forms ? `<h5 class="ref-h">Non-finite forms</h5>${block(s.non_finite_forms)}` : ""));
    }).join("")],
    ["irregular", "Irregular verbs", (d) => {
      const vs = d.verbs["irregular_verbs_6.25"]?.verbs || [];
      const cols = [["present", "Present"], ["meaning", "Meaning"], ["active_simple_past", "Simple past"], ["dependent", "Dependent"], ["perfective_imperative", "Imperative"], ["imperfect", "Imperfect"], ["passive_simple_past", "Passive past"], ["passive_dependent", "Passive dep."], ["passive_perfect_participle", "Participle"]];
      return `<div class="ref-find"><input id="irr-q" type="search" lang="el" placeholder="Filter ${vs.length} verbs, Greek or English" autocomplete="off"></div>
        <div class="tbl-wrap"><table class="pdg irr"><thead><tr>${cols.map(([, l]) => `<th>${l}</th>`).join("")}</tr></thead><tbody>
        ${vs.map((v) => `<tr data-s="${A().esc((Object.values(v).join(" ")).toLowerCase())}">${cols.map(([k]) => `<td${k === "meaning" ? "" : ' lang="el"'}>${A().esc(k === "present" && v.conjugation_type ? `${v.present} (${v.conjugation_type})` : v[k] ?? "")}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
    }],
    ["numerals", "Numerals", (d) => Object.entries(d.nums).filter(([k, v]) => v && typeof v === "object" && !HIDE.has(k)).map(([k, v]) => card(A().esc(v.title || cap(k)), "", block(v))).join("")],
  ];

  const strip = (s) => String(s).normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().replace(/ς/g, "σ");
  function wireFind(scope) {
    const q = scope.querySelector("#ref-q"), hit = scope.querySelector("#ref-hit");
    if (q) q.oninput = () => {
      const w = strip(q.value.trim());
      const cards = [...scope.querySelectorAll(".ref-card[data-words]")];
      cards.forEach((c) => c.classList.remove("found"));
      if (!w) { hit.textContent = ""; return; }
      // Exact word in a pattern's list first, then the longest shared ending among the models.
      let best = cards.find((c) => c.dataset.words.split(" ").some((x) => strip(x) === w));
      if (!best) {
        let bl = 0;
        for (const c of cards) { const m = strip(c.dataset.words.split(" ")[0]); let n = 0; while (n < Math.min(m.length, w.length) && m[m.length - 1 - n] === w[w.length - 1 - n]) n++; if (n > bl) { bl = n; best = c; } }
        if (bl < 2) best = null;
      }
      hit.textContent = best ? `Declines like ${best.dataset.words.split(" ")[0]}` : "No pattern found";
      if (best) { best.classList.add("found"); best.scrollIntoView({ block: "center", behavior: "smooth" }); }
    };
    const iq = scope.querySelector("#irr-q");
    if (iq) iq.oninput = () => { const w = strip(iq.value.trim()); scope.querySelectorAll("tr[data-s]").forEach((tr) => (tr.hidden = !!w && !strip(tr.dataset.s).includes(w))); };
  }

  // #ref.<tab>~<word> opens a tab with its search filled in (the lookup popup's "Table" link).
  routes.ref = async (arg) => {
    const [tab, w] = String(arg || "").split("~"), word = w ? decodeURIComponent(w) : "";
    const E = A(), t = TABS.find(([k]) => k === tab) || TABS[0];
    document.title = `${t[1]} · Grammar tables`;
    E.$("#bar-meta").textContent = "Grammar tables";
    E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Grammar tables</h2>
      <nav class="unit-tabs ref-tabs" aria-label="Tables">${TABS.map(([k, l]) => `<a href="#ref.${k}"${k === t[0] ? ' aria-current="true"' : ""}>${l}</a>`).join("")}</nav>
      <div id="ref-body" class="ref-body"><p class="loading">Φόρτωση…</p></div>`;
    const body = E.$("#ref-body");
    try { body.innerHTML = t[2](await refData()); } catch (e) { body.innerHTML = `<p>The tables could not load: ${E.esc(e.message)}</p>`; }
    // The irregular table is long; skip word wrapping there so filtering stays fast.
    if (t[0] !== "irregular") E.wrapGreek(body);
    wireFind(body);
    window.scrollTo(0, 0);
    const q = body.querySelector("#ref-q, #irr-q");
    if (word && q) {
      q.value = word; q.oninput();
      // A regular verb is not in the irregular table: show the model conjugations instead.
      if (t[0] === "irregular" && !body.querySelector("tr[data-s]:not([hidden])")) location.replace("#ref.verbs");
    }
  };

  /* ---------- reading shelves (stories, classics, news) ---------- */
  // library/<shelf>/index.json: {items: [{id, file, el, title, level}]}. Each item file:
  // {el, title, level, paras: [{el, en}], gloss: {form: "lemma — meaning"}, notes: [..], questions: [{q, options, answer, why}], vocab: [lemma]}
  const LEVELS = ["A2", "B1", "B2", "C1"];
  // Opinion pieces: paragraphs may carry {role, role_en, moves: [connectors as written]}; moves are highlighted in the text.
  function markMoves(E, p) {
    let h = E.esc(p.el);
    for (const m of (p.moves || []).slice().sort((a, b) => b.length - a.length)) {
      const em = E.esc(m), lo = h.toLowerCase(), L = /\p{L}/u; let i = -1;
      // First whole-phrase match (ενώ must not hit Παρθενώνα), outside an earlier mark.
      for (let j = lo.indexOf(em.toLowerCase()); j >= 0; j = lo.indexOf(em.toLowerCase(), j + 1))
        if (!L.test(h[j - 1] || "") && !L.test(h[j + em.length] || "") && h.slice(0, j).split("<mark").length === h.slice(0, j).split("</mark>").length) { i = j; break; }
      if (i < 0) continue;
      h = h.slice(0, i) + `<mark class="op-move">` + h.slice(i, i + em.length) + "</mark>" + h.slice(i + em.length);
    }
    return h;
  }
  const SUM_TASK = "Γράψτε μια περίληψη του άρθρου σε 60–80 λέξεις. Αποδώστε τη θέση του αρθρογράφου και τα βασικά του επιχειρήματα με δικά σας λόγια, χωρίς παραδείγματα και χωρίς δικά σας σχόλια.";
  // A reply draft under a text (progress.library.drafts[key]) with optional examiner feedback.
  function replyBox(E, key, st, o = { pre: "op", lo: 250, hi: 300, task: st.writing, kind: "reply" }) {
    const p = E.progress; p.library = p.library || {}; const drafts = (p.library.drafts = p.library.drafts || {});
    const ta = E.$(`#${o.pre}-draft`), cnt = E.$(`#${o.pre}-count`); let saveT;
    const upd = () => { const n = wcount(ta.value); cnt.textContent = `${n} / ${o.lo}–${o.hi} words`; cnt.className = "sub" + (n > o.hi * 1.1 ? " over" : n >= o.lo * 0.9 ? " ok" : ""); };
    ta.value = drafts[key] || ""; upd();
    ta.oninput = () => { upd(); clearTimeout(saveT); saveT = setTimeout(() => { drafts[key] = ta.value; if (!ta.value) delete drafts[key]; E.saveProgress(); }, 600); };
    aiSample().then((sample) => {
      const btn = E.$(`#${o.pre}-fb`); if (!sample || !btn) return; btn.hidden = false;
      btn.onclick = async () => {
        const text = ta.value.trim(), out = E.$(`#${o.pre}-fbout`);
        if (wcount(text) < 20) { out.innerHTML = `<p class="sub">Write at least a few sentences first.</p>`; return; }
        btn.disabled = true; out.innerHTML = `<p class="loading">Thinking…</p>`;
        const prompt = `You are an examiner for the Greek B2 certificate (Πιστοποίηση Ελληνομάθειας). A learner (strong in grammar patterns, weaker in vocabulary, declension endings are a known weak spot) read an opinion article titled "${st.el}" and wrote a ${o.kind} for this task:\n${o.task}\n\nThe article's argument: ${st.structure || ""}${o.kind === "summary" ? "\n\nTHE ARTICLE:\n" + st.paras.map((x) => x.el).join("\n") : ""}\n\nLEARNER'S TEXT:\n${text}\n\nReply in English, in Markdown, with exactly these sections:\n**Score**: a mark out of 15 each for task, organisation and register, vocabulary and grammar, and an overall verdict (pass/borderline/fail at B2).\n**${o.kind === "summary" ? "Content" : "Argument"}**: ${o.kind === "summary" ? "which of the article\'s main points the summary keeps, misses or distorts, and whether it copies whole phrases" : "two sentences on how well the reply builds and connects its argument"}.\n**Corrected text**: the learner's text in Greek with every error fixed, keeping their content and style.\n**Errors**: a numbered list, each "wrong → right: short reason", case and agreement errors first.\n**Better connectors**: 3 to 5 connectors or phrases from the article or the C1 repertoire that would raise the mark, in Greek with English.`;
        try { await sample(prompt, { onText: ({ text: tx }) => { out.innerHTML = `<div class="card ws-fb">${E.paras(tx)}</div>`; } }); E.wrapGreek(out); }
        catch (e) { out.innerHTML = `<p class="sub">${e?.code === "not_granted" ? "Feedback needs your permission to use Claude." : e?.code === "rate_limited" ? "Too many requests just now; try again in a minute." : "Feedback could not be fetched."}</p>`; if (e?.code === "not_granted") btn.hidden = true; }
        finally { btn.disabled = false; }
      };
    });
  }
  function shelfRoute(shelf, heading) {
    return async (id) => {
      const E = A(), base = `library/${shelf}/`;
      let idx = { items: [] };
      try { idx = await E.getJSON(base + "index.json"); } catch (e) { /* empty shelf */ }
      E.$("#bar-meta").textContent = heading;
      const done = (E.progress.library || {});
      if (!id) {
        document.title = heading + " · Ελληνικά";
        // A shelf with idx.sections (the Reader) is grouped by section, each row carrying its level.
        const row = (x, lvl) => `
            <li><a class="lesson-row" href="#${shelf}.${E.esc(x.id)}"><span class="lr-num">${idx.items.indexOf(x) + 1}</span>
            <span class="lr-main"><span class="lr-title" lang="el">${E.esc(x.el)}</span><span class="lr-en">${E.esc(x.title)}</span></span>
            ${lvl ? `<span class="chip">${E.esc(x.level)}</span>` : ""}${done[shelf + "/" + x.id] != null ? `<span class="chip done">${Math.round(done[shelf + "/" + x.id] * 100)}%</span>` : ""}</a></li>`;
        if (idx.sections) {
          E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>${E.esc(heading)}</h2>
            <nav class="rdr-toc">${idx.sections.map((s) => `<a class="chip" href="#${shelf}" data-sec="${s.id}" lang="el">${E.esc(s.el)}</a>`).join("")}</nav>
            ${idx.sections.map((s) => `<h3 class="ref-group" id="sec-${s.id}"><span lang="el">${E.esc(s.el)}</span> <span class="sub">· ${E.esc(s.title)}</span></h3><ul class="lessons">${idx.items.filter((x) => x.section === s.id).map((x) => row(x, true)).join("")}</ul>`).join("")}`;
          E.view.querySelectorAll(".rdr-toc a").forEach((a) => (a.onclick = (e) => { e.preventDefault(); E.$("#sec-" + a.dataset.sec).scrollIntoView({ behavior: "smooth" }); }));
          return window.scrollTo(0, 0);
        }
        E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>${E.esc(heading)}</h2>
          ${LEVELS.filter((lv) => idx.items.some((x) => x.level === lv)).map((lv) => `<h3 class="ref-group">${lv}</h3><ul class="lessons">${idx.items.filter((x) => x.level === lv).map((x) => row(x)).join("")}</ul>`).join("")}`;
        return window.scrollTo(0, 0);
      }
      const meta = idx.items.find((x) => x.id === id);
      if (!meta) { location.hash = shelf; return; }
      const st = await E.getJSON(base + meta.file), roles = st.paras.some((p) => p.role);
      document.title = st.el + " · " + heading;
      E.setGloss(st.gloss);
      const pos = idx.items.indexOf(meta), next = idx.items[pos + 1];
      E.view.innerHTML = `<p class="crumbs"><a href="#${shelf}">← ${E.esc(heading)}</a></p>
        <div class="story-head"><span class="chip">${E.esc(st.level || meta.level)}</span><h2 lang="el">${E.esc(st.el)}</h2><span class="ex-en">${E.esc(st.title)}${st.author ? " · " + E.esc(st.author) : ""}</span></div>
        ${st.image ? `<figure class="rdr-fig"><img src="${E.esc(st.image.file)}" alt="${E.esc(st.image.caption || "")}" loading="lazy"><figcaption><span lang="el">${E.esc(st.image.caption || "")}</span>${st.image.credit ? ` <span class="sub">· ${E.esc(st.image.credit.split(" · ").pop())}${st.image.license ? ", " + E.esc(st.image.license) : ""}</span>` : ""}</figcaption></figure>` : ""}
        ${roles ? `<div class="sheet-bar op-bar"><label><input type="checkbox" id="op-show" checked> Show argument structure</label><a class="btn small ghost" href="#expr.connectors~practice">Practise connectors</a></div>` : ""}
        <div class="rd-text story${roles ? " op-on" : ""}${st.form === "poem" ? " poem" : ""}">${st.paras.map((p) => `${p.role ? `<div class="op-role no-look"><span lang="el">${E.esc(p.role)}</span> · ${E.esc(p.role_en || "")}</div>` : ""}<p>${roles ? markMoves(E, p) : E.esc(p.el)}</p>`).join("")}</div>
        ${st.paras.some((p) => p.en) ? `<details class="rd-en"><summary>English translation</summary>${st.paras.map((p) => `<p>${E.esc(p.en || "")}</p>`).join("")}</details>` : ""}
        ${st.structure ? `<section class="card op-struct"><h3>How the argument is built</h3><p>${E.esc(st.structure)}</p>${roles ? `<ol class="op-outline">${st.paras.map((p) => `<li><b>${E.esc(p.role_en || p.role || "")}</b>${(p.moves || []).length ? ` · <span lang="el">${p.moves.map((m) => E.esc(m)).join(", ")}</span>` : ""}</li>`).join("")}</ol>` : ""}</section>` : ""}
        ${st.notes?.length ? `<section class="culture"><h3>Notes</h3><ul class="ref-notes">${st.notes.map((n) => `<li>${E.md(n)}</li>`).join("")}</ul></section>` : ""}
        ${st.source ? `<p class="sub rdr-src no-look" lang="el">${E.esc(st.source)}</p>` : ""}
        ${st.questions?.length ? `<section class="card story-q"><h3>Questions</h3>${st.questions.map((q, i) => `<div class="sq" data-i="${i}"><p class="q-prompt">${E.esc(q.q)}</p><div class="options">${q.options.map((o) => `<button class="opt">${E.esc(o)}</button>`).join("")}</div><p class="ex-en sq-why" hidden></p></div>`).join("")}<p class="sub" id="sq-score"></p></section>` : ""}
        ${st.vocab?.length ? `<section class="card"><h3>Words from this text</h3><p class="word-cloud" lang="el">${st.vocab.map((v) => E.esc(v)).join(" · ")}</p><button class="btn small" id="sv-add">Add all to my words</button></section>` : ""}
        ${roles ? `<section class="card"><h3>Summary</h3><div class="ws-prompt" lang="el"><p>${SUM_TASK}</p></div><textarea id="sm-draft" class="ws-draft" lang="el" rows="5" spellcheck="false" placeholder="Το άρθρο υποστηρίζει ότι…"></textarea><div class="sheet-bar"><span id="sm-count" class="sub"></span><button class="btn small ghost" id="sm-fb" hidden>Writing feedback</button></div><div id="sm-fbout"></div></section>` : ""}
        ${st.writing ? `<section class="card"><h3>Your reply</h3><div class="ws-prompt" lang="el">${E.paras(st.writing)}</div><textarea id="op-draft" class="ws-draft" lang="el" rows="12" spellcheck="false" placeholder="Γράψτε εδώ…"></textarea><div class="sheet-bar"><span id="op-count" class="sub"></span><button class="btn small ghost" id="op-fb" hidden>Writing feedback</button></div><div id="op-fbout"></div></section>` : ""}
        ${next ? `<p><a class="btn" href="#${shelf}.${E.esc(next.id)}">Next: <span lang="el">${E.esc(next.el)}</span></a></p>` : ""}`;
      E.wrapGreek(E.view.querySelector(".story")); E.wrapGreek(E.view.querySelector(".culture"));
      if (roles) { E.$("#op-show").onchange = (e) => E.view.querySelector(".story").classList.toggle("op-on", e.target.checked); E.wrapGreek(E.view.querySelector(".op-struct")); }
      if (st.writing) replyBox(E, shelf + "/" + id, st);
      if (roles) replyBox(E, shelf + "/" + id + "~sum", st, { pre: "sm", lo: 60, hi: 80, kind: "summary", task: SUM_TASK });
      // Questions: first answer counts; score saved per item when all are answered.
      let right = 0, answered = 0;
      E.view.querySelectorAll(".sq").forEach((box) => {
        const q = st.questions[box.dataset.i];
        box.querySelectorAll(".opt").forEach((b) => (b.onclick = () => {
          box.querySelectorAll(".opt").forEach((x) => { x.disabled = true; if (x.textContent === q.answer) x.classList.add("right"); });
          if (b.textContent === q.answer) right++; else b.classList.add("wrong");
          if (q.why) { const w = box.querySelector(".sq-why"); w.textContent = q.why; w.hidden = false; }
          if (++answered === st.questions.length) {
            const p = E.progress, key = shelf + "/" + id, sc = right / answered;
            p.library = p.library || {}; p.library[key] = Math.max(p.library[key] || 0, sc); E.saveProgress();
            E.$("#sq-score").textContent = `${right} of ${answered} right`;
          }
        }));
      });
      const add = E.$("#sv-add");
      if (add) add.onclick = () => {
        const p = E.progress, v = p.vocab || (p.vocab = {}), now = Date.now(); let n = 0;
        for (const l of st.vocab) if (!v[l]) { v[l] = { ivl: 0, reps: 0, lapses: 0, rec: 1, seen: now, due: now }; n++; }
        E.saveProgress(); add.outerHTML = `<span class="lk-state">${n} added · they come up in your next word recall</span>`;
      };
      window.scrollTo(0, 0);
    };
  }
  routes.stories = shelfRoute("stories", "Graded short stories");
  routes.classics = shelfRoute("classics", "Classic Greek stories");
  routes.news = shelfRoute("news", "News reader");
  routes.opinion = shelfRoute("opinion", "Opinion articles");
  routes.reader = shelfRoute("reader", "Greek reader");

  /* ---------- exercise sheets: printable, self-checking grids built from the grammar data ---------- */
  // Each sheet type builds cards of {title, sub, rows:[{label, answers:[...]}]}; answers[0] is shown in the key.
  const CASES = [["nom", "Nom."], ["acc", "Acc."], ["gen", "Gen."]];
  const DEF = { sg: { m: { nom: "ο", acc: "τον", gen: "του" }, f: { nom: "η", acc: "τη(ν)", gen: "της" }, n: { nom: "το", acc: "το", gen: "του" } }, pl: { m: { nom: "οι", acc: "τους", gen: "των" }, f: { nom: "οι", acc: "τις", gen: "των" }, n: { nom: "τα", acc: "τα", gen: "των" } } };
  const keepN = (w) => /^([αεηιουωάέήίόύώκπτξψ]|γκ|μπ|ντ|τσ|τζ)/.test(w);
  const art = (a, w) => (a.includes("(") ? (keepN(w) ? a.replace(/[()]/g, "") : a.replace(/\(.*\)/, "")) : a);
  const simple = (w) => typeof w === "string" && /^[α-ωάέήίόύώϊϋΐΰς]+$/.test(w);
  const sampleN = (a, n) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a.slice(0, n); };
  const alts = (f) => String(f).split("/").flatMap((x) => { const m = x.trim().match(/^(.*)\(([^)]+)\)(.*)$/); return m ? [m[1] + m[3], m[1] + m[2] + m[3]] : [x.trim()]; }).filter(Boolean);
  const pool = (lex) => lex.filter((e) => (e.rank || 9e9) <= 3000 && !e.needs_review);

  // Past-tense persons from the 1sg (έγραψα, αγαπήθηκα): sg and 3pl keep its stress; 1pl/2pl stress the
  // antepenult and drop a stressed syllabic augment (έγραψα → γράψαμε) unless the present itself starts with ε.
  const ACC = { "α": "ά", "ε": "έ", "η": "ή", "ι": "ί", "ο": "ό", "υ": "ύ", "ω": "ώ" };
  const unacc = (w) => w.normalize("NFD").replace(/́/g, "").normalize("NFC");
  const nuclei = (w) => { const out = []; const re = /(αι|ει|οι|ου|αυ|ευ|υι)(?![̈])|[αεηιουωϊϋ]/g; let m; while ((m = re.exec(w))) out.push([m.index, m[0].length]); return out; };
  const stressAt = (w, k) => { // k = syllable from the end, 1 = last
    const n = nuclei(w); if (n.length < k) return null;
    const [i, len] = n[n.length - k], j = i + len - 1, c = w[j];
    return ACC[c] ? w.slice(0, j) + ACC[c] + w.slice(j + 1) : null;
  };
  function pastRows(a1, present) {
    if (!/α$/.test(a1) || !/[άέήίόύώ]/.test(a1) || /[ϊϋ]/.test(present)) return null;
    // Internal augment (διέκρινα, παρέμεινα): the plural drops it, which the analogy cannot see, so skip.
    const ai = a1.search(/έ/);
    if (ai > 0 && !/ηκα$/.test(a1) && unacc(present)[ai] !== "ε") return null;
    const hi = a1.search(/ή/); // εισήγαγα (εισάγω) → εισαγάγαμε
    if (hi > 0 && unacc(present)[hi] === "α") return null;
    const st = a1.slice(0, -1);
    // Synizesis (ήπια = ή-πια) keeps the stress where it is: ήπιαμε.
    const pl = (end) => (/[^αεηιουωάέήίόύώ]ι$/.test(st) ? st + end : stressAt(unacc(st) + end, 3));
    const aug = /^έ/.test(a1) && !/^[εέ]/.test(present) && nuclei(unacc(a1)).length >= 3;
    const strip = (w) => (aug && w && /^ε/.test(w) ? w.slice(1) : w);
    const p1 = strip(pl("αμε")), p2 = strip(pl("ατε")), p3b = strip(pl("ανε"));
    if (!p1 || !p2) return null;
    const PRO = ["εγώ", "εσύ", "αυτός", "εμείς", "εσείς", "αυτοί"];
    const f = [[a1], [st + "ες"], [st + "ε"], [p1], [p2], [st + "αν", p3b].filter(Boolean)];
    return f.map((answers, i) => ({ label: PRO[i], answers }));
  }

  // Perfective (θα / να) forms from the past: έγραψα → γράψω (σ/ξ/ψ aorists only; irregulars like είπα → πω are left out),
  // αγαπήθηκα → αγαπηθώ. Augment rules as in pastRows.
  function depRows(a1, present) {
    if (!pastRows(a1, present)) return null;
    const PRO = ["εγώ", "εσύ", "αυτός", "εμείς", "εσείς", "αυτοί"].map((x) => "θα (" + x + ")");
    if (/[θτ]ηκα$/.test(a1)) {
      const st = unacc(a1.slice(0, -3));
      return ["ώ", "είς", "εί", "ούμε", "είτε", "ούν/ούνε"].map((en, i) => ({ label: PRO[i], answers: en.split("/").map((x) => st + x) }));
    }
    if (!/[σξψ]α$/.test(a1) || /^[ήη]/.test(a1)) return null;
    let st = a1.slice(0, -1);
    if (/^έ/.test(a1) && !/^[εέ]/.test(present) && nuclei(unacc(a1)).length >= 3) st = st.slice(1);
    const d1 = stressAt(unacc(st) + "ω", 2); if (!d1) return null;
    const s0 = d1.slice(0, -1);
    return ["ω", "εις", "ει", "ουμε", "ετε", "ουν/ουνε"].map((en, i) => ({ label: PRO[i], answers: en.split("/").map((x) => s0 + x) }));
  }

  const SHEETS = [
    { id: "nouns", el: "Κλίση ουσιαστικών", title: "Noun declension grids", async make() {
      const [lex, nouns] = await Promise.all([A().lexicon(), A().resolve("grammar/nouns-full.json")]);
      const P = Object.fromEntries(nouns.paradigms.map((p) => [p.id, p]));
      const derive = window.__ellinika?.derive;
      const cards = [];
      for (const e of sampleN(pool(lex).filter((e) => e.pos === "noun" && simple(e.lemma) && P[e.noun?.model]), 60)) {
        const p = P[e.noun.model], g = e.noun.gender, rows = [];
        for (const num of ["sg", "pl"]) for (const [c, cl] of CASES) {
          const f = c === "nom" && num === "sg" ? e.lemma : derive(p.model, alts(p[num][c])[0], e.lemma);
          if (!f) { rows.length = 0; break; }
          rows.push({ label: `${cl} ${num}`, pre: art(DEF[num][g][c], f), answers: [f] });
        }
        if (rows.length === 6) { rows[0].given = true; cards.push({ title: e.lemma, sub: `${e.gloss} · like ${p.model}`, rows }); }
        if (cards.length === 8) break;
      }
      return cards;
    } },
    { id: "phrases", el: "Άρθρο, επίθετο, ουσιαστικό", title: "Noun phrases in every case", async make() {
      const [lex, nouns, adjs] = await Promise.all([A().lexicon(), A().resolve("grammar/nouns-full.json"), A().resolve("grammar/adjectives.json")]);
      const P = Object.fromEntries(nouns.paradigms.map((p) => [p.id, p])), Q = Object.fromEntries(adjs.paradigms.map((p) => [p.id, p]));
      const derive = window.__ellinika?.derive, L = pool(lex);
      const ns = sampleN(L.filter((e) => e.pos === "noun" && simple(e.lemma) && P[e.noun?.model]), 80);
      // Only adjectives whose stress matches their model can be derived safely (ψηλός models only end-stressed -ος).
      const as = sampleN(L.filter((e) => e.pos === "adjective" && (e.rank || 9e9) <= 1500 && Q[e.adjective?.model] && ["m", "f", "n"].every((g) => simple(e.adjective[g]))
        && ["m", "f", "n"].every((g) => derive(alts(Q[e.adjective.model].sg.nom[g])[0], alts(Q[e.adjective.model].pl.gen[g])[0], e.adjective[g]))), 80);
      const cards = [];
      for (const [i, n] of ns.entries()) {
        if (!as.length) break;
        const a = as[i % as.length], p = P[n.noun.model], q = Q[a.adjective.model], g = n.noun.gender;
        const rows = [];
        for (const num of ["sg", "pl"]) for (const [c, cl] of CASES) {
          const nf = c === "nom" && num === "sg" ? n.lemma : derive(p.model, alts(p[num][c])[0], n.lemma);
          const af = c === "nom" && num === "sg" ? a.adjective[g] : derive(alts(q.sg.nom[g])[0], alts(q[num][c][g])[0], a.adjective[g]);
          if (!nf || !af) { rows.length = 0; break; }
          const t = art(DEF[num][g][c], af);
          rows.push({ label: `${cl} ${num}`, answers: [`${t} ${af} ${nf}`] });
        }
        if (rows.length === 6) { rows[0].given = true; cards.push({ title: `${rows[0].answers[0]}`, sub: `${a.gloss.split(";")[0]} ${n.gloss.split(";")[0]}`, rows }); }
        if (cards.length === 6) break;
      }
      return cards;
    } },
    { id: "present", el: "Ενεστώτας", title: "Present tense conjugation", async make() {
      const lex = await A().lexicon();
      const PRO = ["εγώ", "εσύ", "αυτός", "εμείς", "εσείς", "αυτοί"];
      const END = { A: ["ω", "εις", "ει", "ουμε", "ετε", "ουν/ουνε"], B1: ["ώ/άω", "άς", "άει/ά", "άμε/ούμε", "άτε", "ούν/άνε/ούνε"], B2: ["ώ", "είς", "εί", "ούμε", "είτε", "ούν/ούνε"] };
      const ok = (e) => { const g = e.verb?.conj_group, w = e.lemma; if (!END[g] || !simple(w)) return false;
        if (g === "A") return /[^αεηιουωάέήίόύώ]ω$/.test(w) && /[άέήίόύώ]/.test(w);
        return /ώ$/.test(w) && w.length > 3; };
      return sampleN(pool(lex).filter((e) => e.pos === "verb" && ok(e)), 8).map((e) => {
        const g = e.verb.conj_group, stem = e.lemma.slice(0, -1);
        const rows = END[g].map((en, i) => ({ label: PRO[i], answers: en.split("/").map((x) => stem + x) }));
        rows[0].given = true;
        return { title: e.lemma, sub: e.gloss.split(";")[0], rows };
      });
    } },
    { id: "irregular", el: "Ανώμαλα ρήματα", title: "Irregular verbs: principal parts", async make() {
      const [vs, lex] = await Promise.all([A().resolve("grammar/verbs-holton.json"), A().lexicon()]);
      // Verbs in the 3000-word list first, so the sheet drills verbs worth knowing.
      const known = new Set(pool(lex).map((e) => e.lemma)), v = (vs["irregular_verbs_6.25"]?.verbs || []).filter((x) => alts(x.present).some((p) => known.has(p)));
      const F = [["active_simple_past", "simple past (I …)"], ["dependent", "dependent (να …)"], ["perfective_imperative", "imperative (sg/pl)"], ["passive_simple_past", "passive past"], ["passive_perfect_participle", "participle"]];
      return sampleN(v.filter((x) => x.active_simple_past), 10).map((x) => ({ title: x.present, sub: x.meaning,
        rows: F.filter(([k]) => x[k]).map(([k, l]) => ({ label: l, answers: alts(String(x[k]).replace(/^θα\s+/, "")).concat(String(x[k]).includes("/") ? [String(x[k])] : []) })) }));
    } },
    { id: "aorist", el: "Αόριστος", title: "Simple past (aorist) conjugation", async make() {
      const lex = await A().lexicon();
      return sampleN(pool(lex).filter((e) => e.pos === "verb" && simple(e.lemma) && /α$/.test(e.verb?.aorist_1sg || "") && simple(e.verb.aorist_1sg)), 40)
        .map((e) => ({ e, rows: pastRows(e.verb.aorist_1sg, e.lemma) })).filter((x) => x.rows).slice(0, 8)
        .map(({ e, rows }) => ({ title: e.lemma, sub: e.gloss.split(";")[0] + " · past", rows }));
    } },
    { id: "future", el: "Στιγμιαίος μέλλοντας (θα / να)", title: "Simple future and να forms", async make() {
      const lex = await A().lexicon();
      const cand = sampleN(pool(lex).filter((e) => e.pos === "verb" && simple(e.lemma)), 200);
      const act = cand.filter((e) => simple(e.verb?.aorist_1sg || "") && /[σξψ]α$/.test(e.verb.aorist_1sg)).map((e) => ({ e, rows: depRows(e.verb.aorist_1sg, e.lemma) })).filter((x) => x.rows).slice(0, 6);
      const pas = cand.filter((e) => /(ομαι|άμαι|ούμαι)$/.test(e.lemma) && /[θτ]ηκα$/.test(e.verb?.aorist_1sg || "") && simple(e.verb.aorist_1sg)).map((e) => ({ e, rows: depRows(e.verb.aorist_1sg, e.lemma) })).filter((x) => x.rows).slice(0, 2);
      return act.concat(pas).map(({ e, rows }) => ({ title: e.lemma, sub: e.gloss.split(";")[0] + " · past " + e.verb.aorist_1sg, rows }));
    } },
    { id: "context", el: "Λέξεις στο κείμενο", title: "Words in context (from the readings)", async make() {
      // Gaps a vocab word in a real sentence from the stories and news; the hint gives the dictionary form, the answer is the inflected form.
      const shelves = ["stories", "news", "opinion", "reader"], texts = [];
      for (const sh of shelves) { try { const ix = await A().getJSON(`library/${sh}/index.json`); for (const it of ix.items) texts.push(`library/${sh}/${it.file}`); } catch (e) { /* shelf missing */ } }
      const cards = [];
      for (const f of sampleN(texts, texts.length)) {
        const t = await A().getJSON(f).catch(() => null); if (!t) continue;
        const sents = t.paras.flatMap((p) => p.el.match(/[^.;!?]+[.;!?»]*/g) || []).map((x) => x.trim()).filter((x) => { const n = x.split(/\s+/).length; return n >= 6 && n <= 32; });
        const forms = Object.entries(t.gloss || {}).filter(([k, v]) => /^[α-ωάέήίόύώϊϋΐΰς]+$/.test(k) && (t.vocab || []).some((l) => v.startsWith(l + " —")));
        for (const l of t.vocab || []) if (/^[α-ωάέήίόύώς]+$/.test(l) && !forms.some(([k]) => k === l)) forms.push([l, t.gloss?.[l] || l]);
        const rows = [], used = new Set();
        for (const [form, g] of sampleN(forms, forms.length)) {
          const re = new RegExp(`(^|[^\\p{L}])${form}(?=$|[^\\p{L}])`, "u");
          const sent = sents.find((x) => re.test(x) && !used.has(x)); if (!sent) continue;
          used.add(sent);
          const lemma = g.split(" — ")[0], mean = (g.split(" — ")[1] || "").split(/[;(]/)[0].trim();
          rows.push({ label: sent.replace(re, "$1_____"), hint: `${lemma}${mean ? " · " + mean : ""}`, answers: [form] });
          if (rows.length === 6) break;
        }
        if (rows.length >= 4) cards.push({ title: t.el, sub: `${t.level || ""} · fill in the right form`, wide: true, rows });
        if (cards.length === 4) break;
      }
      return cards;
    } },
    { id: "passive-past", el: "Παθητικός αόριστος", title: "Passive simple past conjugation", async make() {
      const lex = await A().lexicon();
      const pick = (e) => e.verb?.aorist_passive_1sg || (/(ομαι|άμαι|ούμαι)$/.test(e.lemma) && /ηκα$/.test(e.verb?.aorist_1sg || "") ? e.verb.aorist_1sg : "");
      return sampleN(pool(lex).filter((e) => e.pos === "verb" && simple(e.lemma) && /ηκα$/.test(pick(e)) && simple(pick(e))), 40)
        .map((e) => ({ e, rows: pastRows(pick(e), e.lemma) })).filter((x) => x.rows).slice(0, 8)
        .map(({ e, rows }) => ({ title: e.lemma, sub: e.gloss.split(";")[0] + " · passive past", rows }));
    } },
  ];

  const norm = (s) => String(s).normalize("NFC").trim().toLowerCase().replace(/\s+/g, " ").replace(/σ(?=$|\s)/g, "ς");
  const bare = (s) => norm(s).normalize("NFD").replace(/[̀-ͯ]/g, "");
  routes.sheets = async (id) => {
    const E = A();
    E.$("#bar-meta").textContent = "Exercise sheets";
    const sh = SHEETS.find((x) => x.id === id);
    if (!sh) {
      document.title = "Exercise sheets · Ελληνικά";
      const done = E.progress.library || {};
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Exercise sheets</h2>
        <ul class="lessons">${SHEETS.map((x, i) => `<li><a class="lesson-row" href="#sheets.${x.id}"><span class="lr-num">${i + 1}</span>
          <span class="lr-main"><span class="lr-title" lang="el">${x.el}</span><span class="lr-en">${x.title}</span></span>
          ${done["sheets/" + x.id] != null ? `<span class="chip done">${Math.round(done["sheets/" + x.id] * 100)}%</span>` : ""}</a></li>`).join("")}</ul>`;
      return window.scrollTo(0, 0);
    }
    document.title = sh.title + " · Ελληνικά";
    E.view.innerHTML = `<p class="crumbs"><a href="#sheets">← Exercise sheets</a></p><h2>${sh.title}</h2><p class="sub" lang="el">${sh.el}</p>
      <div class="sheet-bar"><button class="btn small" id="sh-check">Check</button><button class="btn small ghost" id="sh-key">Show answers</button><button class="btn small ghost" id="sh-new">New sheet</button><button class="btn small ghost" id="sh-print">Print</button><span class="sub" id="sh-score"></span></div>
      <div class="sheet" id="sheet"><p class="loading">Φόρτωση…</p></div>`;
    let cards = [];
    try { cards = await sh.make(); } catch (e) { E.$("#sheet").innerHTML = `<p>The sheet could not be built: ${E.esc(e.message)}</p>`; return; }
    E.$("#sheet").innerHTML = cards.map((c, ci) => `<article class="card sheet-card"><div class="ref-title"><span lang="el">${E.esc(c.title)}</span> <span class="ex-en">${E.esc(c.sub || "")}</span></div>
      <div class="grid-fill${c.wide ? " grid-wide" : ""}">${c.rows.map((r, ri) => `<label${c.wide ? ' lang="el"' : ""}>${E.esc(r.label)}${r.hint ? `<span class="sh-hint">${E.esc(r.hint)}</span>` : ""}</label><div class="sh-cell">${r.pre ? `<span class="sh-pre" lang="el">${E.esc(r.pre)}</span>` : ""}${r.given
        ? `<span class="sh-given" lang="el">${E.esc(r.answers[0])}</span>`
        : `<input lang="el" autocomplete="off" autocapitalize="off" spellcheck="false" data-c="${ci}" data-r="${ri}"><span class="sh-ans" lang="el" hidden>${E.esc(r.answers[0])}</span>`}</div>`).join("")}</div></article>`).join("");
    const inputs = [...E.view.querySelectorAll(".sheet input")];
    E.$("#sh-check").onclick = () => {
      let right = 0;
      for (const inp of inputs) {
        const ans = cards[inp.dataset.c].rows[inp.dataset.r].answers, v = inp.value;
        const st = !v.trim() ? "" : ans.some((a) => norm(a) === norm(v)) ? "right" : ans.some((a) => bare(a) === bare(v)) ? "almost" : "wrong";
        inp.className = st; if (st === "right") right++;
        inp.nextElementSibling.hidden = !(st === "wrong" || st === "almost");
        if (st === "wrong" || st === "almost") { const c = cards[inp.dataset.c], r = c.rows[inp.dataset.r]; mistake("Sheet", `${c.title} · ${r.label}${r.pre ? " · " + r.pre + " …" : ""}${r.hint ? " (" + r.hint + ")" : ""}`, v, ans, "#sheets." + sh.id); }
      }
      const sc = inputs.length ? right / inputs.length : 0;
      E.$("#sh-score").textContent = `${right} of ${inputs.length} right`;
      const p = E.progress; p.library = p.library || {}; p.library["sheets/" + sh.id] = Math.max(p.library["sheets/" + sh.id] || 0, sc); E.saveProgress();
    };
    E.$("#sh-key").onclick = () => E.view.querySelectorAll(".sh-ans").forEach((x) => (x.hidden = false));
    E.$("#sh-new").onclick = () => routes.sheets(id);
    E.$("#sh-print").onclick = () => window.print();
    window.scrollTo(0, 0);
  };

  /* ---------- paradigm drill: write a whole table from memory ---------- */
  async function drillItems() {
    const [nouns, adjs, verbs] = await Promise.all(["grammar/nouns-full.json", "grammar/adjectives.json", "grammar/verbs-holton.json"].map((f) => A().resolve(f).catch(() => ({}))));
    const items = [];
    for (const p of nouns.paradigms || []) items.push({ id: "n-" + p.id, group: "Nouns · " + (GEN[p.gender] || "common gender"), word: p.model, gloss: p.gloss, forms: { sg: p.sg, pl: p.pl }, model: p, examples: p.examples || [] });
    for (const p of adjs.paradigms || []) items.push({ id: "a-" + p.id, group: "Adjectives", word: p.model, gloss: p.gloss, forms: { sg: p.sg, pl: p.pl } });
    for (const s of verbs.sections || []) {
      const pd = s.paradigm || s.paradigm_έχω; if (!pd) continue;
      const model = s.model_verb || (s.paradigm_έχω ? "έχω" : "είμαι");
      // Glosses and notes sit beside the forms; drop them so the tense is a pure form table.
      const formsOnly = (o) => Object.fromEntries(Object.entries(o).filter(([, x]) => x && typeof x === "object"));
      for (const [t, v0] of Object.entries(pd)) { const v = v0 && typeof v0 === "object" ? formsOnly(v0) : null; if (v && Object.keys(v).length && gridable(v)) items.push({ id: `v-${model}-${t}`, group: "Verbs", word: model, gloss: `${lab(t)}${pd.gloss ? " · " + pd.gloss : ""}`, forms: v }); }
    }
    return items;
  }
  function drillGrid(ls) {
    const rows = [], cols = [], cell = {};
    for (const [p, v] of ls) {
      let ri = p.findIndex((k) => PERS.includes(k)); if (ri < 0) ri = p.findIndex((k) => ROWS.includes(k) && k !== "sg" && k !== "pl"); if (ri < 0) ri = p.findIndex((k) => ROWS.includes(k));
      const r = p[ri], c = p.filter((_, i) => i !== ri).map(lab).join(" · ") || " ";
      if (!rows.includes(r)) rows.push(r); if (!cols.includes(c)) cols.push(c); cell[r + "|" + c] = v;
    }
    rows.sort((a, b) => ROWS.indexOf(a) - ROWS.indexOf(b));
    return `<div class="tbl-wrap"><table class="pdg drill"><thead><tr><th></th>${cols.map((c) => `<th>${A().esc(c)}</th>`).join("")}</tr></thead><tbody>${rows.map((r) => `<tr><th scope="row">${lab(r)}</th>${cols.map((c) => { const v = cell[r + "|" + c];
      return `<td>${v == null ? "–" : `<input lang="el" autocomplete="off" autocapitalize="off" spellcheck="false" data-a="${A().esc(v)}" data-l="${A().esc(lab(r) + (c.trim() ? " · " + c : ""))}"><span class="sh-ans" lang="el" hidden>${A().esc(v)}</span>`}</td>`; }).join("")}</tr>`).join("")}</tbody></table></div>`;
  }
  routes.drill = async (arg) => {
    const E = A(), [id, w] = decodeURIComponent(String(arg || "")).split("~");
    E.$("#bar-meta").textContent = "Paradigm drill";
    const items = await drillItems(), done = E.progress.library || {};
    const it = items.find((x) => x.id === id);
    if (!it) {
      document.title = "Paradigm drill · Ελληνικά";
      const groups = [...new Set(items.map((x) => x.group))];
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Paradigm drill</h2>
        <p><button class="btn small" id="dr-rand">Random table</button></p>
        ${groups.map((g) => `<h3 class="ref-group">${E.esc(g)}</h3><div class="drill-chips">${items.filter((x) => x.group === g).map((x) => `<a class="drill-chip${done["drill/" + x.id] >= 0.9 ? " done" : ""}" href="#drill.${E.esc(x.id)}"><span lang="el">${E.esc(x.word)}</span>${x.group === "Verbs" ? ` <small>${E.esc(x.gloss.split(" · ")[0])}</small>` : ""}</a>`).join("")}</div>`).join("")}`;
      E.$("#dr-rand").onclick = () => { location.hash = "drill." + items[Math.floor(Math.random() * items.length)].id; };
      return window.scrollTo(0, 0);
    }
    // ~word: the same pattern on another word, forms built by analogy (skipped when the analogy is unsafe).
    let word = it.word, forms = it.forms;
    const derive = window.__ellinika?.derive;
    if (w && it.model && derive) {
      const ww = w, f = JSON.parse(JSON.stringify(forms)); let ok = true;
      for (const num of ["sg", "pl"]) for (const c of Object.keys(f[num] || {})) { const d = derive(it.model.model, alts(f[num][c])[0], ww); if (d) f[num][c] = d; else ok = false; }
      if (ok) { word = ww; forms = f; }
    }
    const fits = (x) => derive && it.model && ["sg", "pl"].every((num) => Object.values(it.forms[num] || {}).every((f) => derive(it.model.model, alts(f)[0], x)));
    const others = (it.examples || []).filter((x) => simple(x) && x !== word && fits(x));
    document.title = word + " · Paradigm drill";
    E.view.innerHTML = `<p class="crumbs"><a href="#drill">← Paradigm drill</a></p>
      <div class="story-head"><span class="chip">${E.esc(it.group)}</span><h2 lang="el">${E.esc(word)}</h2><span class="ex-en">${E.esc(it.gloss || "")}${word !== it.word ? ` · like ${E.esc(it.word)}` : ""}</span></div>
      <div class="sheet-bar"><button class="btn small" id="dr-check">Check</button><button class="btn small ghost" id="dr-key">Show answers</button>${others.length ? `<button class="btn small ghost" id="dr-other">Another word, same pattern</button>` : ""}<a class="btn small ghost" href="#ref">Tables</a><span class="sub" id="dr-score"></span></div>
      <article class="card">${drillGrid(leaves(forms))}</article>`;
    const inputs = [...E.view.querySelectorAll("table.drill input")];
    inputs[0]?.focus();
    E.$("#dr-check").onclick = () => {
      let right = 0;
      for (const inp of inputs) {
        const ans = alts(inp.dataset.a), v = inp.value;
        const st = !v.trim() ? "wrong" : ans.some((a) => norm(a) === norm(v)) ? "right" : ans.some((a) => bare(a) === bare(v)) ? "almost" : "wrong";
        inp.className = st; if (st === "right") right++;
        inp.nextElementSibling.hidden = st === "right";
        if (st !== "right" && v.trim()) mistake("Drill", `${word} · ${inp.dataset.l || ""}`, v, ans, location.hash);
      }
      E.$("#dr-score").textContent = `${right} of ${inputs.length} right`;
      const p = E.progress; p.library = p.library || {}; p.library["drill/" + it.id] = Math.max(p.library["drill/" + it.id] || 0, right / inputs.length); E.saveProgress();
    };
    E.$("#dr-key").onclick = () => E.view.querySelectorAll(".sh-ans").forEach((x) => (x.hidden = false));
    if (others.length) E.$("#dr-other").onclick = () => { location.hash = `drill.${it.id}~${encodeURIComponent(others[Math.floor(Math.random() * others.length)])}`; };
    window.scrollTo(0, 0);
  };

  /* ---------- exam practice: official sample tasks (data/c1/syllabus/reading-tasks.json), timed and scored ---------- */
  const EXAM_FILES = ["b2-tasks.json", "b2-tasks-2.json", "b2-tasks-3.json", "b2-tasks-4.json", "c1-tasks.json"], LISTEN_FILES = ["listening.json", "listening-2.json", "listening-3.json", "listening-4.json", "listening-5.json"];
  const SERIES = [["b2-s", "Β2 · Επίσημο δείγμα"], ["b2-p1", "Β2 · Πρακτική 1"], ["b2-p2", "Β2 · Πρακτική 2"], ["b2-p3", "Β2 · Πρακτική 3"], ["b2-p4", "Β2 · Πρακτική 4"], ["b2-p5", "Β2 · Πρακτική 5"], ["b2-p6", "Β2 · Πρακτική 6"], ["b2-p7", "Β2 · Πρακτική 7"], ["b2-p8", "Β2 · Πρακτική 8"], ["b2-p9", "Β2 · Πρακτική 9"], ["b2-p10", "Β2 · Πρακτική 10"], ["b2-p11", "Β2 · Πρακτική 11"], ["b2-p12", "Β2 · Πρακτική 12"], ["b2-p", "Β2 · Πρακτική"],
    ["c1-s1", "Γ1 · Δείγμα 1"], ["c1-s2", "Γ1 · Δείγμα 2"], ["c1-guide", "Γ1 · Οδηγός 2022"], ["c1-p1", "Γ1 · Πρακτική 1"], ["c1-p2", "Γ1 · Πρακτική 2"], ["c1-p3", "Γ1 · Πρακτική 3"]];
  const optLetter = (o) => (o.match(/^([α-δΑ-Δ])\s/) || [])[1];
  const mcRight = (o, ans) => o === ans || (ans && optLetter(o) && optLetter(o).toLowerCase() === String(ans).trim().toLowerCase());
  routes.exam = async (id) => {
    const E = A();
    E.$("#bar-meta").textContent = "Exam practice";
    let data;
    try { data = await E.resolve("c1/syllabus/reading-tasks.json"); } catch (e) { E.view.innerHTML = `<p>The exam tasks could not load.</p>`; return; }
    // B2 tasks (official sample + practice sets) live with the library and come first.
    for (const f of EXAM_FILES.slice().reverse()) {
      try { const b2 = await E.getJSON("library/exam/" + f); data = { ...data, tasks: [...(b2.tasks || []), ...(data.tasks || [])] }; } catch (e) { /* not built yet */ }
    }
    const tasks = (data.tasks || []).filter((t) => t.questions?.some((q) => q.answer));
    E.setGloss(await E.getJSON("library/exam/gloss.json").catch(() => ({}))); // names and rarer words in the B2 practice texts
    const t = tasks.find((x) => x.id === id), done = E.progress.library || {};
    if (!t) {
      document.title = "Exam practice · Ελληνικά";
      const kind = (t) => (/-use-/.test(t.id) ? "Χρήση γλώσσας" : "Κατανόηση γραπτού λόγου");
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Exam practice</h2>
        <p class="sub">B2 tasks first (the official sample and practice sets in the same format), then the Γ1 sample papers one step above. Timed and marked.</p>
        ${SERIES.map(([k, l], si) => { const inS = (id, k0) => id.startsWith(/\d$/.test(k0) ? k0 + "-" : k0), ts = tasks.filter((x) => inS(x.id, k) && !SERIES.slice(0, si).some(([k0]) => inS(x.id, k0))); return ts.length ? `<h3 class="ref-group">${l}</h3><ul class="lessons">${ts.map((x) => `<li><a class="lesson-row" href="#exam.${x.id}"><span class="lr-num">${tasks.indexOf(x) + 1}</span>
          <span class="lr-main"><span class="lr-title" lang="el">${E.esc(x.title || x.id)}</span><span class="lr-en">${kind(x)} · ${E.esc(x.task_type.split(" (")[0].split(" — ")[0])}</span></span>
          ${done["exam/" + x.id] != null ? `<span class="chip done">${Math.round(done["exam/" + x.id] * 100)}%</span>` : ""}</a></li>`).join("")}</ul>` : ""; }).join("")}`;
      return window.scrollTo(0, 0);
    }
    document.title = (t.title || t.id) + " · Exam practice";
    const rel = t.related_text_id ? tasks.find((x) => x.id === t.related_text_id) || (data.tasks || []).find((x) => x.id === t.related_text_id) : null;
    const isEx = (q) => /ΠΑΡΑΔΕΙΓΜΑ/.test(q.prompt);
    const qs = t.questions.filter((q) => q.answer && !isEx(q)), exQ = t.questions.find(isEx);
    const exHTML = t.example ? `<p class="ex-en">Example: ${E.esc(Object.values(t.example).join(" → "))}</p>`
      : exQ ? `<p class="ex-en" lang="el">Example: ${E.esc(exQ.prompt.replace(/\s*\(ΠΑΡΑΔΕΙΓΜΑ\)/, ""))} → ${E.esc((exQ.options || []).find((o) => mcRight(o, exQ.answer)) || exQ.answer || "")}</p>` : "";
    E.view.innerHTML = `<p class="crumbs"><a href="#exam">← Exam practice</a></p>
      <div class="story-head"><span class="chip">${/-use-/.test(t.id) ? "Χρήση γλώσσας" : "Κατανόηση"}</span><h2 lang="el">${E.esc(t.title || "")}</h2><span class="ex-en">${E.esc(t.task_type)}</span></div>
      <div class="sheet-bar"><span class="chip" id="ex-time">0:00</span><button class="btn small" id="ex-submit">Submit</button><span class="sub" id="ex-score"></span></div>
      <section class="card"><p lang="el">${E.esc(t.instructions_el || "")}</p>${exHTML}</section>
      ${t.text_el ? `<div class="rd-text story exam-text">${E.paras(t.text_el.replace(/\n/g, "\n\n"))}</div>` : ""}
      ${rel && rel.text_el ? `<details class="rd-en"><summary>Show the text this summary is based on</summary><div class="rd-text story">${E.paras(rel.text_el.replace(/\n/g, "\n\n"))}</div></details>` : ""}
      <section class="card exam-q">${qs.map((q, i) => {
        const opts = (q.options || []).filter(Boolean);
        const ctl = !opts.length ? `<input lang="el" autocomplete="off" spellcheck="false" data-i="${i}">`
          : opts.every((o) => o.length <= 45) ? `<select data-i="${i}"><option value="">–</option>${(opts.some(optLetter) ? opts : opts.slice().sort((x, y) => x.localeCompare(y, "el"))).map((o) => `<option>${E.esc(o)}</option>`).join("")}</select>`
          : `<div class="ex-radios">${opts.map((o) => `<label><input type="radio" name="q${i}" value="${E.esc(o)}" data-i="${i}"> <span lang="el">${E.esc(o)}</span></label>`).join("")}</div>`;
        return `<div class="sq" data-i="${i}"><p class="q-prompt" lang="el">${E.esc(q.prompt)}</p>${ctl}<p class="ex-en sq-why" hidden></p></div>`; }).join("")}</section>
      <p class="src">${/^(b2|c1)-p/.test(t.id) ? `Original practice task in the official ${t.id.startsWith("c1") ? "C1 (Γ1)" : "B2"} format.` : `© Κέντρο Ελληνικής Γλώσσας sample papers, texts adapted from ${E.esc(t.text_source || "credited publications")}; for personal study.`}</p>`;
    E.wrapGreek(E.view.querySelector(".exam-text"));
    const t0 = Date.now(), tick = setInterval(() => { const el = E.$("#ex-time"); if (!el) return clearInterval(tick); const s = Math.floor((Date.now() - t0) / 1000); el.textContent = `${Math.floor(s / 60)}:${String(s % 60).padStart(2, "0")}`; }, 1000);
    E.$("#ex-submit").onclick = () => {
      clearInterval(tick);
      let right = 0;
      qs.forEach((q, i) => {
        const box = E.view.querySelector(`.sq[data-i="${i}"]`), opts = (q.options || []).filter(Boolean);
        let v = "";
        const sel = box.querySelector("select, input:not([type=radio])"), rad = box.querySelector("input[type=radio]:checked");
        v = rad ? rad.value : sel ? sel.value : "";
        const ok = opts.length ? mcRight(v, q.answer) : String(q.answer).split(/\s*\/\s*/).some((a) => norm(a) === norm(v) || bare(a) === bare(v));
        if (ok) right++;
        box.classList.add(ok ? "ok" : "bad");
        if (!ok && v) mistake("Exam", `${t.title || t.id} · ${q.prompt}`, v, opts.length ? [(opts.find((o) => mcRight(o, q.answer)) || q.answer)] : String(q.answer).split(/\s*\/\s*/), "#exam." + t.id, !!opts.length);
        const why = box.querySelector(".sq-why");
        const key = opts.length ? (opts.find((o) => mcRight(o, q.answer)) || q.answer) : q.answer;
        why.textContent = (ok ? "✓ " : "✗ Answer: ") + key + (q.suggested_correction ? ` → ${q.suggested_correction}` : "") + (q.answer_note ? ` · ${q.answer_note}` : "");
        why.hidden = false;
      });
      const sc = right / qs.length;
      E.$("#ex-score").textContent = `${right} of ${qs.length} · ${E.$("#ex-time").textContent}`;
      if (t.answer_note && !E.$("#ex-note")) E.view.querySelector(".exam-q").insertAdjacentHTML("beforeend", `<p class="ex-en" id="ex-note">${E.esc(t.answer_note)}</p>`);
      const p = E.progress; p.library = p.library || {}; p.library["exam/" + t.id] = Math.max(p.library["exam/" + t.id] || 0, sc); E.saveProgress();
    };
    window.scrollTo(0, 0);
  };

  /* ---------- conversation phrasebook with English→Greek recall ---------- */
  // Phrase recall keeps its own schedule in progress.library.phr: {phrase: {ivl days, due ms}}; interval ×2.5 per hit.
  const REG = { formal: "formal", informal: "informal", neutral: "" };
  const pnorm = (s) => bare(String(s).replace(/[.,;!?·«»"'’…—–-]/g, " ").replace(/\s+/g, " "));
  routes.phrases = async (arg) => {
    const E = A(), data = await E.getJSON("library/phrases/phrases.json");
    E.$("#bar-meta").textContent = "Phrasebook";
    E.setGloss(data.gloss);
    const st = () => { const p = E.progress; p.library = p.library || {}; return (p.library.phr = p.library.phr || {}); };
    if (!arg) {
      document.title = "Phrasebook · Ελληνικά";
      const s0 = st(), now = Date.now(), all = data.groups.flatMap((g) => g.items);
      const due = all.filter((x) => s0[x.el] && s0[x.el].due <= now).length, learnt = all.filter((x) => s0[x.el]?.ivl >= 21).length;
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Conversation phrasebook</h2>
        <div class="sheet-bar"><a class="btn small" href="#phrases.practice">Practise (${due} due)</a><span class="sub">${learnt} of ${all.length} phrases solid</span></div>
        ${data.groups.map((g) => `<section class="card ref-card"><div class="ref-title"><span lang="el">${E.esc(g.el)}</span> <span class="ex-en">${E.esc(g.en)}</span></div>
          <ul class="ex-list phr">${g.items.map((x) => `<li><span class="ex-el" lang="el">${E.esc(x.el)}${REG[x.reg] ? ` <span class="lk-pos">${REG[x.reg]}</span>` : ""}</span><span class="ex-en">${E.esc(x.en)}</span>${x.ex ? `<span class="phr-ex" lang="el">${E.esc(x.ex)}</span>` : ""}</li>`).join("")}</ul>
          <a class="btn small ghost" href="#phrases.practice~${g.id}">Practise this group</a></section>`).join("")}`;
      E.wrapGreek(E.view);
      return window.scrollTo(0, 0);
    }
    // Practice: due phrases first, then new ones, up to 12.
    const gid = decodeURIComponent(arg).split("~")[1], s0 = st(), now = Date.now();
    const pool = data.groups.filter((g) => !gid || g.id === gid).flatMap((g) => g.items.map((x) => ({ ...x, g: g.en })));
    const queue = [...pool.filter((x) => s0[x.el] && s0[x.el].due <= now).sort((a, b) => s0[a.el].due - s0[b.el].due), ...sampleN(pool.filter((x) => !s0[x.el]), 12)].slice(0, 12);
    let i = 0, right = 0;
    document.title = "Phrase practice · Ελληνικά";
    const show = () => {
      if (i >= queue.length) {
        E.view.innerHTML = `<p class="crumbs"><a href="#phrases">← Phrasebook</a></p><section class="card result"><div class="score">${right}/${queue.length}</div><p>${queue.length ? "Session done." : "Nothing due in this group right now."}</p><a class="btn" href="#phrases">Back to the phrasebook</a></section>`;
        return;
      }
      const x = queue[i];
      E.view.innerHTML = `<p class="crumbs"><a href="#phrases">← Phrasebook</a></p><div class="pmeta"><span>${E.esc(x.g)}</span><span>${i + 1} / ${queue.length}</span></div>
        <section class="card"><span class="q-kind">Say it in Greek${REG[x.reg] ? " · " + REG[x.reg] : ""}</span><p class="q-prompt">${E.esc(x.en)}</p>
        <div class="answer-row"><input id="ph-in" lang="el" autocomplete="off" autocapitalize="off" spellcheck="false"><button class="btn" id="ph-go">Check</button></div><div id="ph-fb"></div></section>`;
      const inp = E.$("#ph-in"); inp.focus();
      const go = () => {
        if (E.$("#ph-next")) return E.$("#ph-next").click();
        const ok = pnorm(inp.value) === pnorm(x.el), close = !ok && pnorm(inp.value).replace(/ /g, "") === pnorm(x.el).replace(/ /g, "");
        const res = ok || close ? "right" : "wrong";
        inp.className = res; if (res === "right") right++;
        if (res === "wrong" && inp.value.trim()) mistake("Phrase", x.en, inp.value, [x.el], "#phrases");
        const v = s0[x.el] || (s0[x.el] = { ivl: 0 });
        if (res === "right") { v.ivl = v.ivl ? Math.round(v.ivl * 2.5) : 1; v.due = Date.now() + v.ivl * 864e5; } else { v.ivl = 0; v.due = Date.now() + 10 * 6e4; }
        E.saveProgress();
        E.$("#ph-fb").innerHTML = `<div class="feedback ${res}"><strong lang="el">${E.esc(x.el)}</strong>${x.ex ? `<span class="why" lang="el">${E.esc(x.ex)}</span>` : ""}</div><p><button class="btn" id="ph-next">Next</button></p>`;
        E.wrapGreek(E.$("#ph-fb"));
        E.$("#ph-next").onclick = () => { i++; show(); };
      };
      E.$("#ph-go").onclick = go;
      inp.onkeydown = (e) => { if (e.key === "Enter") { e.preventDefault(); go(); } };
    };
    show();
    window.scrollTo(0, 0);
  };

  /* ---------- writing and speaking workshop ---------- */
  const aiSample = () => (window.claude?.use ? window.claude.use("sample").catch(() => null) : Promise.resolve(null));
  // Drafts live in progress.library.drafts[taskId] so Backup carries them; finished tasks in progress.library["writing/<id>"].
  const wcount = (s) => (String(s).match(/[\p{L}\p{N}]+/gu) || []).length;
  const phraseList = (E, ph) => (ph || []).length ? `<ul class="ex-list phr">${ph.map((x) => `<li><span class="ex-el" lang="el">${E.esc(x.el)}</span><span class="ex-en">${E.esc(x.en)}</span></li>`).join("")}</ul>` : "";
  const modelBlock = (E, el, en, label) => el ? `<details class="card ws-model"><summary>${label}</summary><div class="story" lang="el">${E.paras(el)}</div>${en ? `<details class="ws-tr"><summary>Translation</summary>${E.paras(en)}</details>` : ""}</details>` : "";
  routes.writing = async (arg) => {
    const E = A(), data = await E.getJSON("library/writing/workshop.json");
    E.$("#bar-meta").textContent = "Workshop";
    E.setGloss(data.gloss);
    const p = E.progress; p.library = p.library || {}; const drafts = (p.library.drafts = p.library.drafts || {});
    const id = arg ? decodeURIComponent(arg) : "";
    if (!id) {
      document.title = "Writing and speaking · Ελληνικά";
      const card = (t, kind) => {
        const done = p.library["writing/" + t.id], d = drafts[t.id];
        const sub = kind === "w" ? `${E.esc(t.genre || "")}${t.register ? " · " + E.esc(t.register) : ""}${t.words ? ` · ${t.words} words` : ""}` : `Part ${t.part}`;
        return `<a class="card shelf ws-task" href="#writing.${encodeURIComponent(t.id)}"><span class="shelf-el" lang="el">${E.esc((t.prompt_el || "").split("\n")[0].slice(0, 110))}${(t.prompt_el || "").length > 110 ? "…" : ""}</span>
          <span class="shelf-en">${E.esc(t.level)}${t.official ? " · official sample" : ""} · ${sub}</span>${done ? `<span class="chip done">done</span>` : d ? `<span class="chip">${wcount(d)} words drafted</span>` : ""}</a>`;
      };
      const lv = (lev) => data.writing.filter((t) => t.level === lev);
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Writing and speaking workshop</h2>
        <h3>Writing · B2</h3><div class="shelves">${lv("B2").map((t) => card(t, "w")).join("")}</div>
        ${lv("Γ1").length ? `<h3>Writing · C1 (Γ1) stretch tasks</h3><div class="shelves">${lv("Γ1").map((t) => card(t, "w")).join("")}</div>` : ""}
        <h3>Speaking · B2</h3>${[1, 2, 3].map((n) => { const its = data.speaking.filter((t) => t.part === n); return its.length ? `<h4>Part ${n}${n === 1 ? ": about you" : n === 2 ? ": discussion questions" : ": role-card debate"}</h4><div class="shelves">${its.map((t) => card(t, "s")).join("")}</div>` : ""; }).join("")}`;
      E.wrapGreek(E.view);
      return window.scrollTo(0, 0);
    }
    const w = data.writing.find((t) => t.id === id), sp = !w && data.speaking.find((t) => t.id === id), t = w || sp;
    if (!t) { location.hash = "writing"; return; }
    document.title = (w ? "Writing" : "Speaking") + " task · Ελληνικά";
    const head = `<p class="crumbs"><a href="#writing">← Workshop</a></p>
      <div class="pmeta"><span>${E.esc(t.level)}${t.official ? " · official sample" : ""}${w ? ` · ${E.esc(t.genre || "")}${t.register ? " · " + E.esc(t.register) : ""}` : ` · speaking part ${t.part}`}</span><span id="ws-time">0:00</span></div>
      <section class="card"><div class="ws-prompt" lang="el">${E.paras(t.prompt_el)}</div>${t.prompt_en ? `<details class="ws-tr"><summary>Prompt in English</summary>${E.paras(t.prompt_en)}</details>` : ""}</section>`;
    // Timer: B2 writing allows about 30 min per task; speaking turns about 2–3 min.
    let sec = 0; clearInterval(routes._wsTimer);
    routes._wsTimer = setInterval(() => { const el = E.$("#ws-time"); if (!el) return clearInterval(routes._wsTimer); sec++; el.textContent = `${Math.floor(sec / 60)}:${String(sec % 60).padStart(2, "0")}`; }, 1000);
    if (w) {
      const target = t.words || 0;
      E.view.innerHTML = `${head}
        ${(t.plan || []).length ? `<section class="card"><div class="ref-title">Plan</div><ol class="ws-plan">${t.plan.map((x) => `<li>${E.esc(x)}</li>`).join("")}</ol></section>` : ""}
        ${(t.phrases || []).length ? `<details class="card" open><summary>Phrase bank</summary>${phraseList(E, t.phrases)}</details>` : ""}
        <section class="card"><textarea id="ws-draft" class="ws-draft" lang="el" rows="14" spellcheck="false" placeholder="${E.esc(t.opening || "Γράψτε εδώ…")}"></textarea>
          <div class="sheet-bar"><span id="ws-count" class="sub"></span><button class="btn small ghost" id="ws-open">Insert opening</button><button class="btn small" id="ws-done">Mark done</button><button class="btn small ghost" id="ws-fb" hidden>Writing feedback</button></div><div id="ws-fbout"></div></section>
        ${(data.rubric || []).length ? `<section class="card"><div class="ref-title">Check your text</div><ul class="ws-rubric">${data.rubric.map((r, i) => `<li><label><input type="checkbox" data-r="${i}"> <span lang="el">${E.esc(r.el)}</span> <span class="ex-en">${E.esc(r.en)}</span></label></li>`).join("")}</ul></section>` : ""}
        ${(t.notes || []).length ? `<section class="card"><div class="ref-title">Watch out for</div><ul>${t.notes.map((x) => `<li>${E.esc(x)}</li>`).join("")}</ul></section>` : ""}
        ${modelBlock(E, t.model_el, t.model_en, "Model answer (write yours first)")}`;
      const ta = E.$("#ws-draft"), cnt = E.$("#ws-count");
      ta.value = drafts[t.id] || "";
      let saveT;
      const upd = () => {
        const n = wcount(ta.value);
        cnt.textContent = target ? `${n} / ${target} words` : `${n} words`;
        cnt.className = "sub" + (target && n > target * 1.1 ? " over" : target && n >= target * 0.9 ? " ok" : "");
      };
      ta.oninput = () => { upd(); clearTimeout(saveT); saveT = setTimeout(() => { drafts[t.id] = ta.value; if (!ta.value) delete drafts[t.id]; E.saveProgress(); }, 600); };
      upd();
      E.$("#ws-open").hidden = !t.opening;
      E.$("#ws-open").onclick = () => { ta.value = t.opening + "\n\n" + ta.value; ta.oninput(); ta.focus(); };
      const markDone = () => { p.library["writing/" + t.id] = { words: wcount(ta.value), at: Date.now() }; drafts[t.id] = ta.value; E.saveProgress(); E.$("#ws-done").textContent = "Done ✓"; };
      E.$("#ws-done").onclick = markDone;
      // Examiner feedback through the page's sample capability (the viewer's own Claude); hidden where unavailable.
      aiSample().then((sample) => {
        const btn = E.$("#ws-fb"); if (!sample || !btn) return; btn.hidden = false;
        btn.onclick = async () => {
          const text = ta.value.trim(), out = E.$("#ws-fbout");
          if (wcount(text) < 20) { out.innerHTML = `<p class="sub">Write at least a few sentences first.</p>`; return; }
          btn.disabled = true; out.innerHTML = `<p class="loading">Thinking…</p>`;
          const prompt = `You are an examiner for the Greek B2 certificate (Πιστοποίηση Ελληνομάθειας, Κέντρο Ελληνικής Γλώσσας). A learner (strong in grammar patterns, weaker in vocabulary, declension endings are a known weak spot) wrote the text below for this task.\n\nTASK (${t.genre || ""}, ${t.register || ""}, about ${target} words):\n${t.prompt_el}\n\nCRITERIA:\n${(data.rubric || []).map((r) => "- " + r.en).join("\n")}\n\nLEARNER'S TEXT:\n${text}\n\nReply in English, in Markdown, with exactly these sections:\n**Score**: a mark out of 15 for each criterion group (task, organisation and register, vocabulary and grammar) and an overall verdict (pass/borderline/fail at B2).\n**Corrected text**: the learner's text in Greek with every error fixed, keeping their content and style.\n**Errors**: a numbered list, each "wrong → right: short reason", case and agreement errors first.\n**Better phrasing**: 3 to 5 B2-level phrases that would raise the mark, in Greek with English.\n**Next step**: one sentence on what to practise.`;
          try {
            await sample(prompt, { onText: ({ text: tx }) => { out.innerHTML = `<div class="card ws-fb">${E.md ? E.paras(tx) : E.esc(tx)}</div>`; } });
            E.wrapGreek(out);
          } catch (e) { out.innerHTML = `<p class="sub">${e?.code === "not_granted" ? "Feedback needs your permission to use Claude." : e?.code === "rate_limited" ? "Too many requests just now; try again in a minute." : "Feedback could not be fetched."}</p>`; if (e?.code === "not_granted") btn.hidden = true; }
          finally { btn.disabled = false; }
        };
      });
      if (p.library["writing/" + t.id]) E.$("#ws-done").textContent = "Done ✓";
    } else {
      E.view.innerHTML = `${head}
        ${(t.roles || []).length ? `<div class="ws-roles">${t.roles.map((r) => `<section class="card ws-role"><span class="q-kind">Role ${E.esc(r.label)}</span><div lang="el">${E.paras(r.el)}</div>${r.en ? `<p class="ex-en">${E.esc(r.en)}</p>` : ""}</section>`).join("")}</div>` : ""}
        ${(t.phrases || []).length ? `<details class="card" open><summary>Phrase bank</summary>${phraseList(E, t.phrases)}</details>` : ""}
        <section class="card"><p class="sub">Answer aloud for two to three minutes without notes, using at least three phrases from the bank. Record yourself if you can, then compare with the model.</p>
          <div class="sheet-bar"><button class="btn small" id="ws-done">Mark done</button><button class="btn small ghost" id="ws-chat-go" hidden>Conversation practice</button></div><div id="ws-chat"></div></section>
        ${modelBlock(E, t.model_el, t.model_en, "Model answer")}`;
      E.$("#ws-done").onclick = () => { p.library["writing/" + t.id] = { at: Date.now() }; E.saveProgress(); E.$("#ws-done").textContent = "Done ✓"; };
      // A typed conversation with Claude playing the examiner or the other role; the page keeps the turns.
      aiSample().then((sample) => {
        const go = E.$("#ws-chat-go"); if (!sample || !go) return; go.hidden = false;
        go.onclick = () => {
          go.hidden = true;
          const box = E.$("#ws-chat"), turns = [];
          const role = (t.roles || []).find((r) => r.label === "Β");
          const frame = `You are playing the ${role ? "other speaker in a Greek B2 oral exam debate (role Β): " + role.el : "examiner in a Greek B2 oral exam, part " + t.part + ". The topic: " + t.prompt_el}. Speak only Greek, natural spoken B2 level, 2 to 4 sentences per turn, and keep the conversation going with a question or a counter-argument. If the learner makes a case or agreement error, add one line at the end starting with "✎" giving the correction in Greek. Learner's first message follows.`;
          box.innerHTML = `<div class="ws-turns"></div><div class="answer-row"><textarea id="ws-say" lang="el" rows="2" placeholder="Γράψτε την απάντησή σας…"></textarea><button class="btn" id="ws-send">Send</button></div>`;
          const list = box.querySelector(".ws-turns"), say = E.$("#ws-say");
          const render = (extra) => { list.innerHTML = turns.map((x) => `<p class="ws-turn ${x.role}"><span lang="el">${E.esc(x.content.replace(frame + "\n\n", ""))}</span></p>`).join("") + (extra || ""); E.wrapGreek(list); };
          E.$("#ws-send").onclick = async () => {
            const v = say.value.trim(); if (!v) return;
            turns.push({ role: "user", content: turns.length ? v : frame + "\n\n" + v }); say.value = ""; render(`<p class="loading">…</p>`);
            try { const { text } = await sample(turns.slice(-12), { cache: false, modelTier: "quick" }); turns.push({ role: "assistant", content: text }); render(); }
            catch (e) { turns.pop(); render(`<p class="sub">${e?.code === "not_granted" ? "Practice needs your permission to use Claude." : "No answer just now; try again."}</p>`); }
          };
        };
      });
      if (p.library["writing/" + t.id]) E.$("#ws-done").textContent = "Done ✓";
    }
    E.wrapGreek(E.view);
    window.scrollTo(0, 0);
  };

  /* ---------- listening: scripts read by the browser's Greek voice, with questions, transcript and dictation ---------- */
  // Scores in progress.library["listening/<id>"]; dictation best in progress.library["dict/<id>"].
  const greekVoices = () => new Promise((res) => {
    const ss = window.speechSynthesis; if (!ss) return res([]);
    const pick = () => ss.getVoices().filter((v) => /^el(-|_|$)/i.test(v.lang));
    const v = pick(); if (v.length) return res(v);
    let done = false; const fin = () => { if (!done) { done = true; res(pick()); } };
    ss.addEventListener?.("voiceschanged", fin, { once: true }); setTimeout(fin, 1500);
  });
  function speaker(voices) {
    // With two Greek voices, f and m get one each; with one, pitch tells them apart.
    const ss = window.speechSynthesis, fem = voices.find((v) => /melina|female|γυν/i.test(v.name)) || voices[0], mal = voices.find((v) => v !== fem) || voices[0];
    let rate = 0.95;
    return {
      setRate: (r) => (rate = r),
      stop: () => ss && ss.cancel(),
      say: (lines, onLine) => new Promise((res) => {
        if (!ss || !voices.length) return res();
        ss.cancel();
        lines.forEach((l, i) => {
          const u = new SpeechSynthesisUtterance(l.el);
          u.lang = "el-GR"; u.voice = l.voice === "m" ? mal : fem; u.rate = rate;
          u.pitch = mal === fem ? (l.voice === "m" ? 0.75 : 1.15) : 1;
          u.onstart = () => onLine && onLine(i);
          if (i === lines.length - 1) { u.onend = () => res(); u.onerror = () => res(); }
          ss.speak(u);
        });
      }),
    };
  }
  routes.listening = async (arg) => {
    const E = A(), data = await E.getJSON("library/listening/listening.json"), done = (E.progress.library || {});
    for (const f of LISTEN_FILES.slice(1)) { try { data.items = data.items.concat((await E.getJSON("library/listening/" + f)).items || []); } catch (e) { /* set not built yet */ } }
    E.$("#bar-meta").textContent = "Listening";
    const TYPE = { announcement: "Ανακοίνωση", dialogue: "Διάλογος", interview: "Συνέντευξη", report: "Ρεπορτάζ", voicemail: "Φωνητικό μήνυμα", monologue: "Μονόλογος" };
    const [id, mode] = decodeURIComponent(arg || "").split("~");
    const it = data.items.find((x) => x.id === id);
    window.speechSynthesis?.cancel();
    if (!it) {
      document.title = "Listening · Ελληνικά";
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Listening practice</h2>
        <p class="sub">B2-style recordings read by your device's Greek voice. Listen first, answer, then read the transcript or try the dictation.</p>
        <ul class="lessons">${data.items.map((x, i) => `<li><a class="lesson-row" href="#listening.${encodeURIComponent(x.id)}"><span class="lr-num">${i + 1}</span>
          <span class="lr-main"><span class="lr-title" lang="el">${E.esc(x.title)}</span><span class="lr-en">${TYPE[x.type] || x.type} · ${E.esc(x.title_en || "")}</span></span>
          ${done["listening/" + x.id] != null ? `<span class="chip done">${Math.round(done["listening/" + x.id] * 100)}%</span>` : ""}</a></li>`).join("")}</ul>`;
      return window.scrollTo(0, 0);
    }
    document.title = it.title + " · Listening";
    E.setGloss(it.gloss);
    const voices = await greekVoices(), sp = speaker(voices), noVoice = !voices.length;
    const bar = `<div class="sheet-bar"><button class="btn small" id="ls-play"${noVoice ? " disabled" : ""}>▶ Play</button><button class="btn small ghost" id="ls-stop"${noVoice ? " disabled" : ""}>■ Stop</button>
      <label class="sub">Speed <select id="ls-rate"><option value="0.75">slow</option><option value="0.95" selected>normal</option><option value="1.1">fast</option></select></label><span class="sub" id="ls-plays"></span></div>
      ${noVoice ? `<p class="sub">This browser has no Greek voice, so the recording cannot play. Read the transcript instead, or install a Greek voice in your device's speech settings.</p>` : ""}`;
    const lineHTML = (l, i) => `<div class="ls-line" data-i="${i}"><button class="ls-say" data-i="${i}" title="Play this line"${noVoice ? " disabled" : ""}>▶</button><div><span class="ls-who">${E.esc(l.speaker || "")}</span> <span lang="el">${E.esc(l.el)}</span><span class="ex-en ls-en">${E.esc(l.en || "")}</span></div></div>`;
    const wire = () => {
      E.$("#ls-rate").onchange = (e) => sp.setRate(+e.target.value);
      E.$("#ls-stop").onclick = () => sp.stop();
      E.view.querySelectorAll(".ls-say").forEach((b) => (b.onclick = () => sp.say([it.script[+b.dataset.i]])));
    };
    if (mode === "dict") {
      // Dictation: each line is played, typed, and marked word by word.
      E.view.innerHTML = `<p class="crumbs"><a href="#listening.${encodeURIComponent(it.id)}">← ${E.esc(it.title)}</a></p><h2>Dictation</h2>${bar}
        <section class="card">${it.script.map((l, i) => `<div class="ls-dict" data-i="${i}"><button class="btn small ghost ls-say" data-i="${i}"${noVoice ? " disabled" : ""}>▶ ${i + 1}</button>
          <textarea lang="el" rows="2" spellcheck="false" autocapitalize="off"></textarea><p class="ls-mark" lang="el" hidden></p></div>`).join("")}
          <div class="sheet-bar"><button class="btn" id="ls-dcheck">Check</button><span class="sub" id="ls-dscore"></span></div></section>`;
      wire();
      E.$("#ls-play").onclick = () => sp.say(it.script);
      E.$("#ls-dcheck").onclick = () => {
        let ok = 0, all = 0;
        E.view.querySelectorAll(".ls-dict").forEach((d) => {
          const target = it.script[+d.dataset.i].el.split(/\s+/), typed = d.querySelector("textarea").value.split(/\s+/).map((w) => bare(w.replace(/[.,;!?·«»"…]/g, "")));
          // Longest common subsequence: correct words in the wrong order no longer get full credit.
          const ordered = window.EllinikaDictation.compare(target, typed);
          all += ordered.total; ok += ordered.correct;
          const matched = new Set(ordered.matched);
          const marks = target.map((w, i) => `<span class="${matched.has(i) ? "ok" : "miss"}">${E.esc(w)}</span>`);
          const m = d.querySelector(".ls-mark"); m.innerHTML = marks.join(" "); m.hidden = false;
        });
        const sc = all ? ok / all : 0; E.$("#ls-dscore").textContent = `${ok} of ${all} words`;
        const p = E.progress; p.library = p.library || {}; p.library["dict/" + it.id] = Math.max(p.library["dict/" + it.id] || 0, sc); E.saveProgress();
      };
      return window.scrollTo(0, 0);
    }
    let plays = 0;
    E.view.innerHTML = `<p class="crumbs"><a href="#listening">← Listening</a></p>
      <div class="story-head"><span class="chip">${TYPE[it.type] || it.type}</span><h2 lang="el">${E.esc(it.title)}</h2><span class="ex-en">${E.esc(it.title_en || "")}</span></div>
      <section class="card"><p lang="el">${E.esc(it.context_el || "")}</p>${bar}<p class="ls-now sub" id="ls-now"></p></section>
      <section class="card exam-q">${it.questions.map((q, i) => `<div class="sq" data-i="${i}"><p class="q-prompt" lang="el">${i + 1}. ${E.esc(q.q)}</p>
        <div class="ex-radios">${q.options.map((o) => `<label><input type="radio" name="lq${i}" value="${E.esc(o)}"> <span lang="el">${E.esc(o)}</span></label>`).join("")}</div><p class="ex-en sq-why" lang="el" hidden></p></div>`).join("")}
        <div class="sheet-bar"><button class="btn" id="ls-check">Check answers</button><span class="sub" id="ls-score"></span></div></section>
      <details class="card" id="ls-tr"><summary>Transcript and translation</summary><div class="ls-script">${it.script.map(lineHTML).join("")}</div></details>
      <div class="actions"><a class="btn ghost" href="#listening.${encodeURIComponent(it.id)}~dict">Dictation</a>${it.vocab?.length ? `<button class="btn ghost" id="ls-add">Add ${it.vocab.length} words to my recall</button>` : ""}</div>`;
    wire();
    E.$("#ls-play").onclick = async () => {
      plays++; E.$("#ls-plays").textContent = `played ${plays}×`;
      await sp.say(it.script, (i) => { E.$("#ls-now") && (E.$("#ls-now").textContent = `${i + 1} / ${it.script.length} · ${it.script[i].speaker || ""}`); });
      E.$("#ls-now") && (E.$("#ls-now").textContent = "");
    };
    E.$("#ls-check").onclick = () => {
      let right = 0;
      it.questions.forEach((q, i) => {
        const box = E.view.querySelector(`.sq[data-i="${i}"]`), v = box.querySelector("input:checked")?.value || "", ok = v === q.answer;
        if (ok) right++;
        box.classList.toggle("ok", ok); box.classList.toggle("bad", !ok);
        if (!ok && v) mistake("Listening", `${it.title} · ${q.q}`, v, [q.answer], "#listening." + encodeURIComponent(it.id), true);
        const w = box.querySelector(".sq-why"); w.textContent = (ok ? "✓ " : "✗ " + q.answer + " · ") + (q.why || ""); w.hidden = false;
      });
      E.$("#ls-score").textContent = `${right} of ${it.questions.length}`;
      const p = E.progress; p.library = p.library || {}; p.library["listening/" + it.id] = Math.max(p.library["listening/" + it.id] || 0, right / it.questions.length); E.saveProgress();
    };
    const add = E.$("#ls-add");
    if (add) add.onclick = () => {
      const p = E.progress, v = p.vocab || (p.vocab = {}), now = Date.now(); let n = 0;
      for (const l of it.vocab) if (!v[l]) { v[l] = { ivl: 0, reps: 0, lapses: 0, rec: 1, seen: now, due: now }; n++; }
      E.saveProgress(); add.outerHTML = `<span class="lk-state">${n} added · they come up in your next word recall</span>`;
    };
    E.wrapGreek(E.$("#ls-tr")); E.wrapGreek(E.view.querySelector(".exam-q"));
    window.scrollTo(0, 0);
  };

  /* ---------- expression trainer: connectors, collocations, idioms, learned phrases (data/c1/phrases) ---------- */
  // Spaced recall in progress.library.expr: {"deck/el": {ivl days, due ms}}; same schedule as the phrasebook.
  const DECKS = [["connectors", "Συνδετικές λέξεις", "Connectors", "function"], ["collocations", "Συνάψεις λέξεων", "Collocations", "pattern"], ["idioms", "Ιδιωματισμοί", "Idioms", "register"], ["learned-phrases", "Λόγιες φράσεις", "Learned phrases", "type"]];
  const gapRe = (ph) => new RegExp(`(^|[^\\p{L}])(${ph.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")})(?=$|[^\\p{L}])`, "iu");
  routes.expr = async (arg) => {
    const E = A(); E.$("#bar-meta").textContent = "Expressions";
    const p = E.progress; p.library = p.library || {}; const st = (p.library.expr = p.library.expr || {});
    const [deck, mode] = decodeURIComponent(arg || "").split("~");
    const D = DECKS.find((d) => d[0] === deck), now = Date.now();
    if (!D) {
      document.title = "Expressions · Ελληνικά";
      const counts = await Promise.all(DECKS.map(async ([id]) => { const xs = await E.resolve(`c1/phrases/${id}.json`).catch(() => []); return { n: xs.length, due: xs.filter((x) => st[id + "/" + x.el]?.due <= now).length, solid: xs.filter((x) => st[id + "/" + x.el]?.ivl >= 21).length }; }));
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Expression trainer</h2>
        <p class="sub">The words that make B2 and C1 writing sound native: connectors, collocations, idioms and learned phrases, each with an example. Practise them English → Greek on a spaced schedule.</p>
        <ul class="lessons">${DECKS.map(([id, el, en], i) => `<li><a class="lesson-row" href="#expr.${id}"><span class="lr-num">${i + 1}</span><span class="lr-main"><span class="lr-title" lang="el">${el}</span><span class="lr-en">${en} · ${counts[i].n} items · ${counts[i].solid} solid${counts[i].due ? ` · ${counts[i].due} due` : ""}</span></span></a></li>`).join("")}</ul>`;
      return window.scrollTo(0, 0);
    }
    const [id, el, en, tag] = D, xs = await E.resolve(`c1/phrases/${id}.json`);
    document.title = en + " · Ελληνικά";
    if (mode !== "practice") {
      E.view.innerHTML = `<p class="crumbs"><a href="#expr">← Expressions</a></p><h2>${en}</h2><p class="sub" lang="el">${el}</p>
        <div class="sheet-bar"><a class="btn small" href="#expr.${id}~practice">Practise ${xs.filter((x) => st[id + "/" + x.el]?.due <= now).length || 12}</a><input id="ex-filter" placeholder="Filter (Greek or English)" autocomplete="off"></div>
        <ul class="ex-list phr" id="ex-items">${xs.map((x, i) => `<li data-i="${i}"><span class="ex-el" lang="el">${E.esc(x.el)}${x[tag] ? ` <span class="lk-pos">${E.esc(x[tag])}</span>` : ""}${st[id + "/" + x.el]?.ivl >= 21 ? ` <span class="chip done">solid</span>` : ""}</span><span class="ex-en">${E.esc(x.meaning_en)}</span>${x.example_el ? `<span class="phr-ex" lang="el">${E.esc(x.example_el)}</span>` : ""}${x.grammar_note || x.origin_note ? `<span class="ex-en">${E.esc(x.grammar_note || x.origin_note)}</span>` : ""}</li>`).join("")}</ul>`;
      const hay = xs.map((x) => bare(`${x.el} ${x.meaning_en} ${x.example_el || ""}`));
      E.$("#ex-filter").oninput = (e) => { const q = bare(e.target.value); E.view.querySelectorAll("#ex-items li").forEach((li) => (li.hidden = !!q && !hay[+li.dataset.i].includes(q))); };
      E.wrapGreek(E.$("#ex-items"));
      return window.scrollTo(0, 0);
    }
    const queue = [...xs.filter((x) => st[id + "/" + x.el]?.due <= now).sort((a, b) => st[id + "/" + a.el].due - st[id + "/" + b.el].due), ...sampleN(xs.filter((x) => !st[id + "/" + x.el]), 12)].slice(0, 12);
    let i = 0, right = 0;
    const show = () => {
      if (i >= queue.length) { E.view.innerHTML = `<p class="crumbs"><a href="#expr.${id}">← ${en}</a></p><section class="card result"><div class="score">${right}/${queue.length}</div><p>${queue.length ? "Session done." : "Nothing due right now."}</p><a class="btn" href="#expr.${id}~practice">Another round</a></section>`; return; }
      const x = queue[i], re = gapRe(x.el), cloze = x.example_el && re.test(x.example_el) ? E.esc(x.example_el).replace(gapRe(E.esc(x.el)), "$1<span class=\"gap\">_____</span>") : "";
      E.view.innerHTML = `<p class="crumbs"><a href="#expr.${id}">← ${en}</a></p><div class="pmeta"><span>${en}</span><span>${i + 1} / ${queue.length}</span></div>
        <section class="card"><span class="q-kind">Say it in Greek${x.register && x.register !== "neutral" ? " · " + E.esc(x.register) : ""}</span><p class="q-prompt">${E.esc(x.meaning_en)}</p>
        ${cloze ? `<p lang="el" class="ex-cloze">${cloze}</p>` : x.example_en ? `<p class="ex-en">${E.esc(x.example_en)}</p>` : ""}
        <div class="answer-row"><input id="xp-in" lang="el" autocomplete="off" autocapitalize="off" spellcheck="false"><button class="btn" id="xp-go">Check</button></div><div id="xp-fb"></div></section>`;
      const inp = E.$("#xp-in"); inp.focus();
      const go = () => {
        if (E.$("#xp-next")) return E.$("#xp-next").click();
        const a = pnorm(inp.value), b = pnorm(x.el), ok = a === b || a.replace(/ /g, "") === b.replace(/ /g, "");
        inp.className = ok ? "right" : "wrong"; if (ok) right++;
        const v = st[id + "/" + x.el] || (st[id + "/" + x.el] = { ivl: 0 });
        if (ok) { v.ivl = v.ivl ? Math.round(v.ivl * 2.5) : 1; v.due = Date.now() + v.ivl * 864e5; } else { v.ivl = 0; v.due = Date.now() + 10 * 6e4; if (inp.value.trim()) mistake("Expression", x.meaning_en, inp.value, [x.el], "#expr." + id); }
        E.saveProgress();
        E.$("#xp-fb").innerHTML = `<div class="feedback ${ok ? "right" : "wrong"}"><strong lang="el">${E.esc(x.el)}</strong>${x.example_el ? `<span class="why" lang="el">${E.esc(x.example_el)}</span>` : ""}${x.grammar_note || x.origin_note ? `<span class="why">${E.esc(x.grammar_note || x.origin_note)}</span>` : ""}</div><p><button class="btn" id="xp-next">Next</button></p>`;
        E.wrapGreek(E.$("#xp-fb"));
        E.$("#xp-next").onclick = () => { i++; show(); };
      };
      E.$("#xp-go").onclick = go;
      inp.onkeydown = (e) => { if (e.key === "Enter") { e.preventDefault(); go(); } };
    };
    show();
    window.scrollTo(0, 0);
  };

  /* ---------- backup: progress to and from a JSON file ---------- */
  routes.backup = () => {
    const E = A();
    document.title = "Backup · Ελληνικά"; E.$("#bar-meta").textContent = "Backup";
    const p = E.progress, words = Object.keys(p.vocab || {}).length, lessons = Object.keys(p).filter((k) => p[k]?.best != null).length;
    E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Backup</h2>
      <section class="card"><p>${lessons} lessons and ${words} words in recall are saved in this browser.</p>
      <div class="actions"><button class="btn" id="bk-save">Save backup file</button><label class="btn ghost">Restore from file<input type="file" id="bk-load" accept="application/json,.json" hidden></label></div>
      <p class="sub" id="bk-msg"></p></section>`;
    E.$("#bk-save").onclick = async () => {
      const data = JSON.stringify({ app: "ellinika", saved: new Date().toISOString(), progress: E.progress }, null, 1);
      const filename = `ellinika-progress-${new Date().toISOString().slice(0, 10)}.json`, msg = E.$("#bk-msg");
      // In the claude.ai preview files go through the downloads capability; opened from a folder, a plain link works.
      const dl = window.claude?.use ? await window.claude.use("downloads").catch(() => null) : null;
      if (dl) {
        try { await dl.save({ filename, data }); msg.textContent = "Backup file saved."; }
        catch (err) { msg.textContent = err?.code === "declined" ? "Not saved." : "Could not save: " + (err?.message || err); }
        return;
      }
      const a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([data], { type: "application/json" })); a.download = filename;
      document.body.append(a); a.click(); a.remove(); setTimeout(() => URL.revokeObjectURL(a.href), 2000);
      msg.textContent = "Backup file saved.";
    };
    E.$("#bk-load").onchange = async (e) => {
      const f = e.target.files[0]; if (!f) return;
      try {
        const d = JSON.parse(await f.text());
        if (d.app !== "ellinika" || typeof d.progress !== "object") throw new Error("not an Ελληνικά backup");
        if (!confirm(`Replace the progress in this browser with the backup from ${String(d.saved).slice(0, 10)}?`)) return;
        localStorage.setItem("ellinika.progress.v1", JSON.stringify(d.progress));
        location.hash = ""; location.reload();
      } catch (err) { E.$("#bk-msg").textContent = "Could not restore: " + err.message; }
    };
    window.scrollTo(0, 0);
  };

  /* ---------- mock exam: one B2 paper assembled from the exam, listening and workshop shelves ---------- */
  // progress.library.mock[set] = {start, parts:{listening:[ids], writing:id}, history:[{at, total, mins, parts}]}. Parts are done on their own pages; scores come from progress.
  const MOCK_SETS = [["b2-s1", "Official sample"], ["b2-p1", "Practice 1"], ["b2-p2", "Practice 2"], ["b2-p3", "Practice 3"], ["b2-p4", "Practice 4"], ["b2-p5", "Practice 5"], ["b2-p6", "Practice 6"], ["b2-p7", "Practice 7"], ["b2-p8", "Practice 8"], ["b2-p9", "Practice 9"], ["b2-p10", "Practice 10"], ["b2-p11", "Practice 11"], ["b2-p12", "Practice 12"]];
  routes.mock = async (arg) => {
    const E = A(), p = E.progress; p.library = p.library || {}; const mk = (p.library.mock = p.library.mock || {});
    document.title = "Mock exam · Ελληνικά"; E.$("#bar-meta").textContent = "Mock exam";
    let tasks = [];
    for (const f of EXAM_FILES) tasks = tasks.concat((await E.getJSON("library/exam/" + f).catch(() => ({ tasks: [] }))).tasks || []);
    const [set] = decodeURIComponent(arg || "").split("~");
    const sets = MOCK_SETS.filter(([k]) => tasks.some((t) => t.id.startsWith(k + "-")));
    if (!sets.find(([k]) => k === set)) {
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Mock exam</h2>
        <p class="sub">A full B2 paper: reading, use of language, two listening items and one writing task, against the clock. Work through the parts in order; each opens in its own page and your scores are collected here.</p>
        <ul class="lessons">${sets.map(([k, l], i) => { const h = mk[k]?.history || [], best = h.length ? Math.max(...h.map((x) => x.total)) : null;
          return `<li><a class="lesson-row" href="#mock.${k}"><span class="lr-num">${i + 1}</span><span class="lr-main"><span class="lr-title">${l}</span><span class="lr-en">${mk[k]?.start && !mk[k].done ? "in progress" : h.length ? `${h.length} attempt${h.length > 1 ? "s" : ""}` : "not tried"}</span></span>${best != null ? `<span class="chip done">${Math.round(best * 100)}%</span>` : ""}</a></li>`; }).join("")}</ul>`;
      return window.scrollTo(0, 0);
    }
    const st = (mk[set] = mk[set] || {});
    const L = [];
    for (const f of LISTEN_FILES) L.push(...((await E.getJSON("library/listening/" + f).catch(() => ({ items: [] }))).items || []).filter((x) => x.level !== "C1"));
    const W = (await E.getJSON("library/writing/workshop.json").catch(() => ({ writing: [] }))).writing.filter((t) => t.level === "B2");
    const start = () => {
      st.start = Date.now(); st.done = false;
      st.parts = { listening: sampleN(L.filter((x) => ["dialogue", "interview", "report", "monologue"].includes(x.type)), 1).concat(sampleN(L.filter((x) => ["announcement", "voicemail"].includes(x.type)), 1)).map((x) => x.id), writing: sampleN(W, 1)[0]?.id };
      // Clear earlier scores for these parts so the paper counts only this attempt.
      for (const t of tasks.filter((t) => t.id.startsWith(set + "-"))) delete p.library["exam/" + t.id];
      for (const id of st.parts.listening) delete p.library["listening/" + id];
      if (st.parts.writing) delete p.library["writing/" + st.parts.writing];
      st.rubric = 0; E.saveProgress(); routes.mock(set);
    };
    const label = MOCK_SETS.find(([k]) => k === set)[1];
    if (!st.start || st.done) {
      const h = st.history || [];
      E.view.innerHTML = `<p class="crumbs"><a href="#mock">← Mock exam</a></p><h2>${label}</h2>
        <section class="card"><p>About two hours: reading and use of language (about 90 minutes in the real exam), two listening items, one writing task. The clock starts when you press Start; earlier scores for these tasks are cleared so the paper counts only this attempt.</p><p><button class="btn" id="mk-start">Start the paper</button></p></section>
        ${h.length ? `<section class="card"><div class="ref-title">Earlier attempts</div><ul>${h.map((x) => `<li>${new Date(x.at).toLocaleDateString()} · <strong>${Math.round(x.total * 100)}%</strong> · ${x.mins} min · reading ${Math.round(x.parts.reading * 100)}%, use ${Math.round(x.parts.use * 100)}%, listening ${Math.round(x.parts.listening * 100)}%, writing ${Math.round(x.parts.writing * 100)}%</li>`).join("")}</ul></section>` : ""}`;
      E.$("#mk-start").onclick = start;
      return window.scrollTo(0, 0);
    }
    const lib = p.library, ts = tasks.filter((t) => t.id.startsWith(set + "-"));
    const avg = (xs) => (xs.length ? xs.reduce((a, b) => a + (b ?? 0), 0) / xs.length : 0);
    const read = ts.filter((t) => /-reading-/.test(t.id)), use = ts.filter((t) => /-use-/.test(t.id));
    const li = st.parts.listening.map((id) => L.find((x) => x.id === id)).filter(Boolean), wt = W.find((t) => t.id === st.parts.writing);
    const row = (href, title, sc) => `<li><a class="lesson-row" href="${href}"><span class="lr-main"><span class="lr-title" lang="el">${E.esc(title)}</span></span>${sc != null ? `<span class="chip done">${Math.round(sc * 100)}%</span>` : `<span class="chip">to do</span>`}</a></li>`;
    const mins = Math.round((Date.now() - st.start) / 6e4);
    const R = (data) => (data && data.rubric) || [];
    const rubric = R(await E.getJSON("library/writing/workshop.json").catch(() => null));
    E.view.innerHTML = `<p class="crumbs"><a href="#mock">← Mock exam</a></p><h2>${label}</h2><div class="sheet-bar"><span class="chip">${mins} min so far</span><span class="sub">Open each part, finish it, then come back here.</span></div>
      <h3 class="ref-group" lang="el">1 · Κατανόηση γραπτού λόγου</h3><ul class="lessons">${read.map((t) => row("#exam." + t.id, t.title || t.id, lib["exam/" + t.id])).join("")}</ul>
      <h3 class="ref-group" lang="el">2 · Χρήση γλώσσας</h3><ul class="lessons">${use.map((t) => row("#exam." + t.id, t.title || t.id, lib["exam/" + t.id])).join("")}</ul>
      <h3 class="ref-group" lang="el">3 · Κατανόηση προφορικού λόγου</h3><ul class="lessons">${li.map((x) => row("#listening." + encodeURIComponent(x.id), x.title, lib["listening/" + x.id])).join("")}</ul>
      <h3 class="ref-group" lang="el">4 · Παραγωγή γραπτού λόγου</h3><ul class="lessons">${wt ? row("#writing." + encodeURIComponent(wt.id), (wt.prompt_el || "").split("\n")[0].slice(0, 90) + "…", lib["writing/" + wt.id] ? 1 : null) : ""}</ul>
      ${rubric.length ? `<section class="card"><div class="ref-title">After writing, tick what your text does</div><ul class="ws-rubric">${rubric.map((r, i) => `<li><label><input type="checkbox" class="mk-r" ${st.rubric & (1 << i) ? "checked" : ""} data-i="${i}"> <span lang="el">${E.esc(r.el)}</span> <span class="ex-en">${E.esc(r.en)}</span></label></li>`).join("")}</ul></section>` : ""}
      <div class="actions"><button class="btn" id="mk-finish">Finish and score the paper</button><button class="btn ghost" id="mk-abandon">Abandon</button></div><div id="mk-res"></div>`;
    E.view.querySelectorAll(".mk-r").forEach((c) => (c.onchange = () => { st.rubric = c.checked ? st.rubric | (1 << +c.dataset.i) : st.rubric & ~(1 << +c.dataset.i); E.saveProgress(); }));
    E.$("#mk-abandon").onclick = () => { if (confirm("Abandon this attempt?")) { st.start = 0; E.saveProgress(); routes.mock(set); } };
    E.$("#mk-finish").onclick = () => {
      const ticks = rubric.filter((_, i) => st.rubric & (1 << i)).length;
      const parts = { reading: avg(read.map((t) => lib["exam/" + t.id])), use: avg(use.map((t) => lib["exam/" + t.id])), listening: avg(li.map((x) => lib["listening/" + x.id])), writing: wt && lib["writing/" + wt.id] && rubric.length ? ticks / rubric.length : 0 };
      const total = (parts.reading + parts.use + parts.listening + parts.writing) / 4;
      (st.history = st.history || []).unshift({ at: Date.now(), total, mins: Math.round((Date.now() - st.start) / 6e4), parts });
      st.done = true; E.saveProgress();
      E.$("#mk-res").innerHTML = `<section class="card result"><div class="score">${Math.round(total * 100)}%</div><p>${[["Reading", parts.reading], ["Use of language", parts.use], ["Listening", parts.listening], ["Writing (self-check)", parts.writing]].map(([n, v]) => `${n} ${Math.round(v * 100)}% ${v >= 0.6 ? "✓" : "✗"}`).join(" · ")}</p><p class="sub">${Object.values(parts).every((v) => v >= 0.6) ? "Every skill is at 60% or more, the pass mark the real exam sets for each skill." : "The real exam needs 60% in every skill; one skill below that fails the whole certificate."} Speaking is not in this paper; practise it in the workshop. Wrong answers are waiting in the <a href="#mistakes">mistakes notebook</a>.</p></section>`;
      E.$("#mk-finish").disabled = true;
    };
    window.scrollTo(0, 0);
  };

  /* ---------- mistakes notebook: every wrong typed or chosen answer, reviewed until right ---------- */
  // progress.library.mistakes: [{k kind, p prompt, g given, a answers[], h link, mc multiple-choice, t time, n times missed}], newest first, max 400.
  function mistake(kind, prompt, given, answers, href, mc) {
    const E = A(), p = E.progress; p.library = p.library || {};
    const list = (p.library.mistakes = p.library.mistakes || []), ex = list.findIndex((m) => m.p === prompt && m.k === kind);
    const m = ex >= 0 ? list.splice(ex, 1)[0] : { k: kind, p: prompt, a: answers, h: href, mc: !!mc, n: 0 };
    m.g = given; m.t = Date.now(); m.n++; list.unshift(m); list.length = Math.min(list.length, 400);
    E.saveProgress();
  }
  /* ---------- rebuild the argument: put an opinion article's shuffled paragraphs back in order ---------- */
  // Score in progress.library["argue/<id>"] (share of paragraphs in the right place, best kept).
  routes.argue = async (arg) => {
    const E = A(); E.$("#bar-meta").textContent = "Rebuild the argument";
    const p = E.progress; p.library = p.library || {};
    let idx = { items: [] }; try { idx = await E.getJSON("library/opinion/index.json"); } catch (e) { /* no articles */ }
    const id = arg ? decodeURIComponent(arg) : "", meta = idx.items.find((x) => x.id === id);
    if (!meta) {
      document.title = "Rebuild the argument · Ελληνικά";
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Rebuild the argument</h2>
        <p class="sub">The paragraphs of an opinion article are shuffled. Tap them in the order the writer used, guided by the connectors and the logic of thesis, counter-argument and conclusion. Then read the article with its structure shown.</p>
        <ul class="lessons">${idx.items.map((x, i) => `<li><a class="lesson-row" href="#argue.${E.esc(x.id)}"><span class="lr-num">${i + 1}</span><span class="lr-main"><span class="lr-title" lang="el">${E.esc(x.el)}</span><span class="lr-en">${E.esc(x.level)} · ${E.esc(x.title)}</span></span>${p.library["argue/" + x.id] != null ? `<span class="chip done">${Math.round(p.library["argue/" + x.id] * 100)}%</span>` : ""}</a></li>`).join("")}</ul>`;
      return window.scrollTo(0, 0);
    }
    const st = await E.getJSON("library/opinion/" + meta.file);
    document.title = st.el + " · Rebuild the argument";
    E.setGloss(st.gloss);
    const n = st.paras.length, order = sampleN([...Array(n).keys()], n), picked = [];
    E.view.innerHTML = `<p class="crumbs"><a href="#argue">← Rebuild the argument</a></p>
      <div class="story-head"><span class="chip">${E.esc(st.level)}</span><h2 lang="el">${E.esc(st.el)}</h2><span class="ex-en">${E.esc(st.title)}</span></div>
      <p class="sub">Tap the paragraphs in order, first to last. Tap a placed paragraph to send it back.</p>
      <ol class="ag-done story" id="ag-done"></ol>
      <div class="ag-pool story" id="ag-pool"></div>
      <div class="sheet-bar"><span class="sub" id="ag-score"></span><button class="btn small" id="ag-check" disabled>Check</button><a class="btn small ghost" href="#opinion.${E.esc(id)}">Read with structure</a></div>`;
    const card = (i) => `<button class="ag-card" data-i="${i}"><span class="ag-role" hidden></span><span lang="el">${E.esc(st.paras[i].el)}</span></button>`;
    const draw = () => {
      E.$("#ag-done").innerHTML = picked.map((i) => `<li>${card(i)}</li>`).join("");
      E.$("#ag-pool").innerHTML = order.filter((i) => !picked.includes(i)).map(card).join("");
      E.$("#ag-check").disabled = picked.length !== n;
      E.view.querySelectorAll(".ag-card").forEach((b) => (b.onclick = () => { const i = +b.dataset.i, k = picked.indexOf(i); if (k >= 0) picked.splice(k, 1); else picked.push(i); draw(); }));
    };
    draw();
    E.$("#ag-check").onclick = () => {
      let right = 0;
      E.$("#ag-done").querySelectorAll(".ag-card").forEach((b, k) => {
        const i = +b.dataset.i, ok = i === k; if (ok) right++;
        b.classList.add(ok ? "ok" : "bad"); b.disabled = true;
        const r = b.querySelector(".ag-role"); r.hidden = false; r.textContent = `${ok ? "✓" : "✗ belongs at " + (i + 1)} · ${st.paras[i].role_en || ""}`;
      });
      const sc = right / n, key = "argue/" + id; p.library[key] = Math.max(p.library[key] || 0, sc); E.saveProgress();
      E.$("#ag-score").textContent = `${right} of ${n} in place`;
      E.$("#ag-check").style.display = "none";
    };
    window.scrollTo(0, 0);
  };

  /* ---------- register converter: rewrite a message in the other register ---------- */
  // library/register/register.json {items: [{id, level, situation, from, el_from, el_to, en, changes: [{from, to, why}]}], gloss}.
  // Draft in progress.library.drafts["register/<id>"]; self-check in progress.library["register/<id>"] (1 or 0).
  routes.register = async (arg) => {
    const E = A(); E.$("#bar-meta").textContent = "Register converter";
    const data = await E.getJSON("library/register/register.json"); E.setGloss(data.gloss);
    const p = E.progress; p.library = p.library || {}; const drafts = (p.library.drafts = p.library.drafts || {});
    const reg = (f) => (f === "informal" ? ["Φιλικό", "informal"] : ["Επίσημο", "formal"]);
    const id = arg ? decodeURIComponent(arg) : "", i = data.items.findIndex((x) => x.id === id), t = data.items[i];
    if (!t) {
      document.title = "Register converter · Ελληνικά";
      const row = (x) => { const sc = p.library["register/" + x.id]; return `<li><a class="lesson-row" href="#register.${E.esc(x.id)}"><span class="lr-num">${E.esc(x.level)}</span><span class="lr-main"><span class="lr-title">${E.esc(x.situation)}</span><span class="lr-en">${reg(x.from)[1]} → ${reg(x.from === "informal" ? "formal" : "informal")[1]}</span></span>${sc != null ? `<span class="chip ${sc ? "done" : ""}">${sc ? "✓" : "again"}</span>` : drafts["register/" + x.id] ? `<span class="chip">draft</span>` : ""}</a></li>`; };
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Register converter</h2>
        <p class="sub">The B2 writing paper marks register: a note to a friend and a letter to the municipality say the same thing differently. Rewrite each message in the other register, then compare with the model and the list of changes.</p>
        <h3>Make it formal</h3><ul class="lessons">${data.items.filter((x) => x.from === "informal").map(row).join("")}</ul>
        <h3>Make it informal</h3><ul class="lessons">${data.items.filter((x) => x.from !== "informal").map(row).join("")}</ul>`;
      return window.scrollTo(0, 0);
    }
    const [fromEl, fromEn] = reg(t.from), [toEl, toEn] = reg(t.from === "informal" ? "formal" : "informal"), key = "register/" + t.id, next = data.items[i + 1];
    document.title = "Register converter · Ελληνικά";
    E.view.innerHTML = `<p class="crumbs"><a href="#register">← Register converter</a></p>
      <div class="pmeta"><span>${E.esc(t.level)} · ${fromEn} → ${toEn}</span></div>
      <section class="card"><p class="sub">${E.esc(t.situation)}</p><div class="ref-title"><span lang="el">${fromEl}</span> · ${fromEn}</div><div class="story" lang="el">${E.paras(t.el_from)}</div><details class="ws-tr"><summary>English</summary><p>${E.esc(t.en)}</p></details></section>
      <section class="card"><div class="ref-title">Rewrite it: <span lang="el">${toEl}</span> · ${toEn}</div><textarea id="rg-draft" class="ws-draft" lang="el" rows="7" spellcheck="false"></textarea>
        <div class="sheet-bar"><span id="rg-count" class="sub"></span><button class="btn small" id="rg-show">Compare with the model</button><button class="btn small ghost" id="rg-fb" hidden>Writing feedback</button></div><div id="rg-fbout"></div></section>
      <section class="card" id="rg-model" hidden><div class="ref-title">Model</div><div class="story" lang="el">${E.paras(t.el_to)}</div>
        <ul class="ex-list phr">${(t.changes || []).map((c) => `<li><span class="ex-el" lang="el">${E.esc(c.from)} → ${E.esc(c.to)}</span><span class="ex-en">${E.esc(c.why)}</span></li>`).join("")}</ul>
        <div class="sheet-bar"><span class="sub">Did your version get the register right?</span><button class="btn small" data-ok="1">Yes</button><button class="btn small ghost" data-ok="0">Not yet</button></div></section>
      ${next ? `<p><a class="btn" href="#register.${E.esc(next.id)}">Next message</a></p>` : ""}`;
    E.wrapGreek(E.view.querySelector(".story"));
    const ta = E.$("#rg-draft"), cnt = E.$("#rg-count"); let saveT;
    const upd = () => (cnt.textContent = `${wcount(ta.value)} words`);
    ta.value = drafts[key] || ""; upd();
    ta.oninput = () => { upd(); clearTimeout(saveT); saveT = setTimeout(() => { drafts[key] = ta.value; if (!ta.value) delete drafts[key]; E.saveProgress(); }, 600); };
    E.$("#rg-show").onclick = () => { const m = E.$("#rg-model"); m.hidden = false; E.wrapGreek(m); m.scrollIntoView({ behavior: "smooth", block: "start" }); };
    E.view.querySelectorAll("[data-ok]").forEach((b) => (b.onclick = () => {
      p.library[key] = +b.dataset.ok; E.saveProgress();
      b.parentElement.innerHTML = `<span class="lk-state">${+b.dataset.ok ? "Noted ✓" : "Marked to try again; it shows in the list"}</span>`;
    }));
    aiSample().then((sample) => {
      const btn = E.$("#rg-fb"); if (!sample || !btn) return; btn.hidden = false;
      btn.onclick = async () => {
        const text = ta.value.trim(), out = E.$("#rg-fbout");
        if (wcount(text) < 15) { out.innerHTML = `<p class="sub">Write your version first.</p>`; return; }
        btn.disabled = true; out.innerHTML = `<p class="loading">Thinking…</p>`;
        const prompt = `You are a Greek writing tutor preparing a learner for the Greek B2 certificate (Πιστοποίηση Ελληνομάθειας). Situation: ${t.situation}. The learner had to rewrite this ${fromEn} Greek message in a ${toEn} register, keeping the content:\n${t.el_from}\n\nA model answer (one of many good ones):\n${t.el_to}\n\nLEARNER'S VERSION:\n${text}\n\nReply in English, in Markdown, with exactly these sections:\n**Register**: is it consistently ${toEn}? Name any phrases that slip into the wrong register.\n**Corrected text**: the learner's version in Greek with every error fixed, keeping their wording where it works.\n**Errors**: a numbered list, each "wrong → right: short reason", case and agreement errors first.\n**Phrases to keep**: 3 ${toEn} Greek phrases worth memorising for this kind of message, with English.`;
        try { await sample(prompt, { onText: ({ text: tx }) => { out.innerHTML = `<div class="card ws-fb">${E.paras(tx)}</div>`; } }); E.wrapGreek(out); }
        catch (e) { out.innerHTML = `<p class="sub">${e?.code === "not_granted" ? "Feedback needs your permission to use Claude." : e?.code === "rate_limited" ? "Too many requests just now; try again in a minute." : "Feedback could not be fetched."}</p>`; if (e?.code === "not_granted") btn.hidden = true; }
        finally { btn.disabled = false; }
      };
    });
    window.scrollTo(0, 0);
  };

  /* ---------- today's study session: one item from each exam skill, rotating through what is not done yet ---------- */
  // The plan is fixed for the day (seeded by date); ticks live in progress.library.today = {day, done: [href]}.
  routes.today = async () => {
    const E = A(); E.$("#bar-meta").textContent = "Today's session"; document.title = "Today's session · Ελληνικά";
    const p = E.progress; p.library = p.library || {}; const lib = p.library;
    const day = new Date().toISOString().slice(0, 10), seed = [...day].reduce((a, c) => (a * 31 + c.charCodeAt(0)) >>> 0, 7);
    if (lib.today?.day !== day) lib.today = { day, done: [] };
    const pick = (xs, key) => { if (!xs.length) return null; const fresh = xs.filter((x) => lib[key(x)] == null), pool = fresh.length ? fresh : xs; return pool[seed % pool.length]; };
    const get = (f, k) => E.getJSON(f).then((d) => d[k] || []).catch(() => []);
    const [exs, lss, ws, op, rg, mk] = await Promise.all([Promise.all(EXAM_FILES.map((f) => get("library/exam/" + f, "tasks"))), Promise.all(LISTEN_FILES.map((f) => get("library/listening/" + f, "items"))), E.getJSON("library/writing/workshop.json").catch(() => ({})), get("library/opinion/index.json", "items"), get("library/register/register.json", "items"), Promise.resolve(lib.mistakes || [])]);
    const ex = exs.flat(), now = Date.now();
    const due = await Promise.all(DECKS.map(async ([id]) => ((await E.resolve(`c1/phrases/${id}.json`).catch(() => [])).filter((x) => lib.expr?.[id + "/" + x.el]?.due <= now).length)));
    const dk = due.indexOf(Math.max(...due)), plan = [];
    plan.push({ min: 10, skill: "Expressions", href: `#expr.${DECKS[dk][0]}~practice`, el: DECKS[dk][1], en: due[dk] ? `${due[dk]} due in ${DECKS[dk][2].toLowerCase()}` : `12 new ${DECKS[dk][2].toLowerCase()}` });
    const rd = pick(ex.filter((t) => t.id.startsWith("b2-") && t.id.includes("reading")), (t) => "exam/" + t.id); if (rd) plan.push({ min: 20, skill: "Reading", href: "#exam." + rd.id, el: rd.title || rd.id, en: "B2 reading task", key: "exam/" + rd.id });
    const us = pick(ex.filter((t) => t.id.startsWith("b2-") && t.id.includes("use")), (t) => "exam/" + t.id); if (us) plan.push({ min: 10, skill: "Language use", href: "#exam." + us.id, el: us.title || us.id, en: "B2 grammar and vocabulary task", key: "exam/" + us.id });
    const ls = pick(lss.flat().filter((x) => x.level !== "C1"), (x) => "listening/" + x.id); if (ls) plan.push({ min: 15, skill: "Listening", href: "#listening." + encodeURIComponent(ls.id), el: ls.title, en: `${ls.title_en || ""}: questions, then the dictation`, key: "listening/" + ls.id });
    const o = pick(op, (x) => "opinion/" + x.id); if (o) plan.push({ min: 15, skill: "Reading for argument", href: "#opinion." + o.id, el: o.el, en: `${o.level} opinion article: questions and a 60–80 word summary`, key: "opinion/" + o.id });
    const w = (ws.writing || []).filter((t) => t.level === "B2"), r = rg.filter((x) => x.level !== "B1");
    if (seed % 3 === 2 && r.length) { const x = pick(r, (x) => "register/" + x.id); plan.push({ min: 15, skill: "Writing", href: "#register." + x.id, el: x.situation, en: "register rewrite", key: "register/" + x.id }); }
    else { const x = pick(w, (t) => "writing/" + t.id); if (x) plan.push({ min: 25, skill: "Writing", href: "#writing." + encodeURIComponent(x.id), el: (x.prompt_el || "").split("\n")[0].slice(0, 120), en: `${x.genre || "B2 task"}${x.words ? ", " + x.words + " words" : ""}`, key: "writing/" + x.id }); }
    const sp = pick(ws.speaking || [], (t) => "writing/" + t.id); if (sp) plan.push({ min: 5, skill: "Speaking", href: "#writing." + encodeURIComponent(sp.id), el: (sp.prompt_el || "").split("\n")[0].slice(0, 120), en: `speaking part ${sp.part}, aloud`, key: "writing/" + sp.id });
    if (mk.length) plan.push({ min: 5, skill: "Mistakes", href: "#mistakes", el: "Επανάληψη λαθών", en: `${mk.length} saved mistakes` });
    const total = plan.reduce((a, x) => a + x.min, 0);
    const draw = () => {
      const n = plan.filter((x) => lib.today.done.includes(x.href)).length;
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Today's session</h2>
        <p class="sub">About ${total} minutes covering every part of the B2 exam. The plan stays the same all day and moves on to new material tomorrow. ${n} of ${plan.length} done.</p>
        <ul class="lessons td-plan">${plan.map((x, i) => { const d = lib.today.done.includes(x.href); return `<li class="${d ? "td-done" : ""}"><a class="lesson-row" href="${x.href}" data-i="${i}"><span class="lr-num">${x.min}′</span><span class="lr-main"><span class="lr-en">${E.esc(x.skill)}</span><span class="lr-title" lang="el">${E.esc(x.el)}</span><span class="lr-en">${E.esc(x.en)}</span></span>${x.key && lib[x.key] != null ? `<span class="chip done">${typeof lib[x.key] === "number" ? Math.round(lib[x.key] * 100) + "%" : "done"}</span>` : ""}</a><label class="td-tick"><input type="checkbox" data-h="${E.esc(x.href)}"${d ? " checked" : ""}> done</label></li>`; }).join("")}</ul>`;
      E.view.querySelectorAll(".td-tick input").forEach((c) => (c.onchange = () => { const h = c.dataset.h, L = lib.today.done; if (c.checked) { if (!L.includes(h)) L.push(h); } else L.splice(L.indexOf(h), 1); E.saveProgress(); draw(); }));
      E.view.querySelectorAll("a[data-i]").forEach((a) => (a.onclick = () => { const h = a.getAttribute("href"); if (!lib.today.done.includes(h)) { lib.today.done.push(h); E.saveProgress(); } }));
    };
    draw(); window.scrollTo(0, 0);
  };

  /* ---------- where to focus: per-skill averages from saved scores, mistake counts, and what to redo next ---------- */
  routes.focus = async () => {
    const E = A(); E.$("#bar-meta").textContent = "Where to focus"; document.title = "Where to focus · Ελληνικά";
    const lib = E.progress.library || {}, now = Date.now();
    const SK = [["Reading", (k) => /^exam\/b2-.*reading/.test(k)], ["Language use", (k) => /^exam\/b2-.*use/.test(k)], ["Listening", (k) => k.startsWith("listening/")], ["Grammar sheets", (k) => k.startsWith("sheets/")], ["Paradigm drill", (k) => k.startsWith("drill/")], ["Reading for meaning", (k) => /^(stories|news|classics|opinion)\//.test(k)], ["C1 tasks", (k) => k.startsWith("exam/c1-")]];
    const nums = Object.entries(lib).filter(([, v]) => typeof v === "number" && v >= 0 && v <= 1);
    const rows = SK.map(([l, f]) => { const xs = nums.filter(([k]) => f(k)); return { l, n: xs.length, avg: xs.length ? xs.reduce((a, [, v]) => a + v, 0) / xs.length : null }; });
    const mk = lib.mistakes || [], recent = mk.filter((m) => now - m.t < 30 * 864e5), kinds = {};
    for (const m of recent) kinds[m.k] = (kinds[m.k] || 0) + 1;
    const exp = lib.expr || {}, ex = Object.values(exp), solid = ex.filter((x) => x.ivl >= 21).length;
    // Redo: the lowest saved scores under 60%, linked back to where they were earned.
    const href = (k) => { const [a, ...b] = k.split("/"), id = b.join("/"); return a === "exam" ? "#exam." + id : a === "sheets" ? "#sheets." + id : a === "drill" ? "#drill." + id : "#" + a + "." + id; };
    const redo = nums.filter(([k, v]) => v < 0.6 && /^(exam|listening|sheets|drill|stories|news|classics|opinion)\//.test(k)).sort((a, b) => a[1] - b[1]).slice(0, 6);
    const untried = rows.filter((r) => !r.n && r.l !== "C1 tasks").map((r) => r.l);
    const HOME = { Reading: "#exam", "Language use": "#exam", Listening: "#listening", "Grammar sheets": "#sheets", "Paradigm drill": "#drill", "Reading for meaning": "#opinion" };
    const bar = (r) => `<li class="fc-row"><span class="fc-l">${r.l}</span><span class="fc-bar"><span style="width:${Math.round((r.avg || 0) * 100)}%" class="${r.avg == null ? "" : r.avg < 0.6 ? "bad" : "ok"}"></span></span><span class="fc-n">${r.avg == null ? "not tried" : Math.round(r.avg * 100) + "% · " + r.n}</span></li>`;
    E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Where to focus</h2>
      <p class="sub">Averages of your saved scores in each skill. The exam needs 60% in every paper, so anything red is where practice pays most.</p>
      <ul class="fc-list">${rows.map(bar).join("")}</ul>
      <p class="sub">Expressions: ${ex.length} practised, ${solid} solid (21+ days).</p>
      ${recent.length ? `<section class="card"><h3>Mistakes in the last 30 days</h3><p>${Object.entries(kinds).sort((a, b) => b[1] - a[1]).map(([k, n]) => `${E.esc(k)} <b>${n}</b>`).join(" · ")}</p><a class="btn small" href="#mistakes">Review them</a></section>` : ""}
      <section class="card"><h3>Do next</h3>${redo.length || untried.length ? `<ul class="lessons">${redo.map(([k, v]) => `<li><a class="lesson-row" href="${href(k)}"><span class="lr-num">${Math.round(v * 100)}%</span><span class="lr-main"><span class="lr-title">Redo ${E.esc(k.split("/").slice(1).join("/").replace(/^op-/, "").replace(/-/g, " "))}</span><span class="lr-en">${E.esc({ exam: "exam task", sheets: "exercise sheet", drill: "paradigm drill", listening: "listening", stories: "story", news: "news", classics: "classic", opinion: "opinion article" }[k.split("/")[0]] || "")}</span></span></a></li>`).join("")}${untried.map((l) => `<li><a class="lesson-row" href="${HOME[l]}"><span class="lr-num">new</span><span class="lr-main"><span class="lr-title">Start ${l.toLowerCase()}</span><span class="lr-en">nothing scored here yet</span></span></a></li>`).join("")}</ul>` : `<p class="sub">Everything you have scored is at 60% or above. Keep going with <a href="#today">today's session</a>.</p>`}</section>`;
    window.scrollTo(0, 0);
  };

  routes.mistakes = (arg) => {
    const E = A(), p = E.progress; p.library = p.library || {}; const list = (p.library.mistakes = p.library.mistakes || []);
    document.title = "Mistakes · Ελληνικά"; E.$("#bar-meta").textContent = "Mistakes";
    if (arg !== "review") {
      E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Mistakes notebook</h2>
        <p class="sub">Every wrong answer from sheets, drills, exams, listening and phrase practice lands here. Review them until they're right; a right answer clears the entry.</p>
        ${list.length ? `<div class="sheet-bar"><a class="btn small" href="#mistakes.review">Review ${Math.min(list.length, 20)}</a><button class="btn small ghost" id="mk-clear">Clear all</button><span class="sub">${list.length} open</span></div>
        <ul class="sr-list">${list.slice(0, 200).map((m) => `<li><a href="${m.h || "#mistakes"}"><span class="chip">${E.esc(m.k)}</span> <span lang="el">${E.esc(m.p)}</span>${m.n > 1 ? ` <span class="sub">×${m.n}</span>` : ""}</a>
          <p class="sr-snip"><span class="mk-bad" lang="el">${E.esc(m.g)}</span> → <span class="mk-ok" lang="el">${E.esc(m.a[0])}</span></p></li>`).join("")}</ul>` : `<section class="card"><p>No open mistakes. Wrong answers from sheets, drills, exams, listening and phrase practice will collect here.</p></section>`}`;
      if (E.$("#mk-clear")) E.$("#mk-clear").onclick = () => { if (confirm("Clear the whole mistakes notebook?")) { p.library.mistakes = []; E.saveProgress(); routes.mistakes(); } };
      return window.scrollTo(0, 0);
    }
    // Review: the 20 most-missed recent entries; type the answer (for multiple choice, the right option's text).
    const queue = list.slice().sort((a, b) => b.n - a.n || b.t - a.t).slice(0, 20);
    let i = 0, right = 0;
    const show = () => {
      if (i >= queue.length) { E.view.innerHTML = `<p class="crumbs"><a href="#mistakes">← Mistakes</a></p><section class="card result"><div class="score">${right}/${queue.length}</div><p>${list.length} still open.</p><a class="btn" href="#mistakes">Back to the notebook</a></section>`; return; }
      const m = queue[i];
      E.view.innerHTML = `<p class="crumbs"><a href="#mistakes">← Mistakes</a></p><div class="pmeta"><span>${E.esc(m.k)}</span><span>${i + 1} / ${queue.length}</span></div>
        <section class="card"><p class="q-prompt" lang="el">${E.esc(m.p)}</p><p class="sub">Last time you wrote <span class="mk-bad" lang="el">${E.esc(m.g)}</span>.</p>
        ${m.mc ? `<div class="ex-radios">${sampleN([m.a[0], m.g], 2).map((o) => `<label><input type="radio" name="mk" value="${E.esc(o)}"> <span lang="el">${E.esc(o)}</span></label>`).join("")}</div><p><button class="btn" id="mk-go">Check</button></p>`
          : `<div class="answer-row"><input id="mk-in" lang="el" autocomplete="off" autocapitalize="off" spellcheck="false"><button class="btn" id="mk-go">Check</button></div>`}<div id="mk-fb"></div></section>`;
      const inp = E.$("#mk-in"); inp?.focus();
      const go = () => {
        if (E.$("#mk-next")) return E.$("#mk-next").click();
        const v = m.mc ? E.view.querySelector("input[name=mk]:checked")?.value || "" : inp.value;
        const ok = m.a.some((a) => norm(a) === norm(v) || (!m.mc && bare(a) === bare(v)));
        if (ok) { right++; const j = list.indexOf(m); if (j >= 0) list.splice(j, 1); } else { m.n++; m.t = Date.now(); }
        E.saveProgress();
        E.$("#mk-fb").innerHTML = `<div class="feedback ${ok ? "right" : "wrong"}"><strong lang="el">${E.esc(m.a[0])}</strong>${m.h ? ` <a class="sub" href="${m.h}">open the exercise</a>` : ""}</div><p><button class="btn" id="mk-next">Next</button></p>`;
        E.$("#mk-next").onclick = () => { i++; show(); };
      };
      E.$("#mk-go").onclick = go;
      if (inp) inp.onkeydown = (e) => { if (e.key === "Enter") { e.preventDefault(); go(); } };
    };
    show();
    window.scrollTo(0, 0);
  };

  /* ---------- search across lessons, readings, workshop and phrasebook ---------- */
  // The index is built on the first search and kept for the session; matching ignores case and accents.
  let searchIdx = null;
  async function buildSearch() {
    const E = A(), docs = [];
    const flat = (o) => (typeof o === "string" ? o : Array.isArray(o) ? o.map(flat).join(" ") : o && typeof o === "object" ? Object.values(o).map(flat).join(" ") : "");
    const course = await E.getJSON("lessons/course.json").catch(() => ({ units: [] }));
    const lessons = course.units.flatMap((u) => (u.lessons || []).map((l) => ({ ...l, unit: u.title })));
    await Promise.all(lessons.map(async (l) => {
      const j = await E.getJSON(`lessons/${l.file}`).catch(() => null); if (!j) return;
      docs.push({ kind: "Lesson", href: "#" + l.id, title: `${l.el || j.el || ""} · ${l.title || j.title || ""}`, text: flat([j.blocks, j.practice, j.vocab]) });
    }));
    for (const [sh, label] of [["stories", "Story"], ["news", "News"], ["classics", "Classic"], ["opinion", "Opinion"], ["reader", "Reader"]]) {
      const ix = await E.getJSON(`library/${sh}/index.json`).catch(() => ({ items: [] }));
      await Promise.all(ix.items.map(async (it) => {
        const j = await E.getJSON(`library/${sh}/${it.file}`).catch(() => null); if (!j) return;
        docs.push({ kind: label, href: `#${sh}.${it.id}`, title: `${j.el} · ${j.title}`, text: flat([j.paras, j.notes]) });
      }));
    }
    const ws = await E.getJSON("library/writing/workshop.json").catch(() => null);
    if (ws) for (const t of [...ws.writing, ...ws.speaking]) docs.push({ kind: "Workshop", href: `#writing.${encodeURIComponent(t.id)}`, title: (t.prompt_el || "").split("\n")[0].slice(0, 80), text: flat([t.prompt_el, t.prompt_en, t.phrases, t.model_el, t.model_en, t.notes]) });
    const ph = await E.getJSON("library/phrases/phrases.json").catch(() => null);
    if (ph) for (const g of ph.groups) docs.push({ kind: "Phrasebook", href: "#phrases", title: `${g.el} · ${g.en}`, text: flat(g.items) });
    for (const f of LISTEN_FILES) {
      const L = await E.getJSON("library/listening/" + f).catch(() => null);
      if (L) for (const it of L.items) docs.push({ kind: "Listening", href: `#listening.${encodeURIComponent(it.id)}`, title: `${it.title} · ${it.title_en || ""}`, text: flat(it.script) });
    }
    const pos = await E.getJSON("library/pos/index.json").catch(() => ({ items: [] }));
    await Promise.all(pos.items.map(async (it) => {
      const j = await E.getJSON(`library/pos/${it.file}`).catch(() => null); if (!j) return;
      j.sections.forEach((s, i) => docs.push({ kind: "Grammar", href: `#pos.${it.id}~${i}`, title: `${s.el} · ${s.title}`, text: flat(s.body) }));
    }));
    // Word families and false friends (word-families.js): one result per family and per confusable set.
    for (const [sh, label] of [["families", "Word family"], ["confusables", "False friends"]]) {
      const ix = await E.getJSON(`library/${sh}/index.json`).catch(() => ({ items: [] }));
      await Promise.all(ix.items.map(async (it) => {
        const j = await E.getJSON(`library/${sh}/${it.file}`).catch(() => null); if (!j) return;
        if (j.groups) for (const g of j.groups) docs.push({ kind: label, href: `#${sh}.${it.id}`, title: `${g.key} · ${g.meaning}`, text: flat([g.members, g.note, g.ex]) });
        if (j.pairs) for (const p of j.pairs) docs.push({ kind: label, href: `#${sh}.${it.id}`, title: p.words.map((w) => w.el).join(" / "), text: flat([p.trap, p.words, p.note, p.ex]) });
      }));
    }
    for (const d of docs) { d.text = d.text.replace(/\*\*|__|`/g, "").replace(/\s+/g, " "); d.bare = bare(d.text); }
    return docs;
  }
  routes.search = async (arg) => {
    const E = A(), q = decodeURIComponent(arg || "").trim();
    document.title = "Search · Ελληνικά"; E.$("#bar-meta").textContent = "Search";
    E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Search</h2>
      <form class="answer-row" id="sr-form"><input id="sr-q" lang="el" placeholder="e.g. aorist, γενική, ο οποίος, rent" value="${E.esc(q)}" autocomplete="off"><button class="btn">Search</button></form>
      <div id="sr-out">${q ? `<p class="loading">Searching…</p>` : `<p class="sub">Searches every lesson, story, news text, classic, workshop task, listening script, grammar guide, word family, false friend and the phrasebook, in Greek or English, ignoring accents.</p>`}</div>`;
    E.$("#sr-form").onsubmit = (e) => { e.preventDefault(); const v = E.$("#sr-q").value.trim(); if (v) location.hash = "search." + encodeURIComponent(v); };
    if (!q) return E.$("#sr-q").focus();
    searchIdx = searchIdx || (await buildSearch());
    const bq = bare(q), hits = [];
    for (const d of searchIdx) {
      const i = d.bare.indexOf(bq); if (i < 0) continue;
      let n = 0, j = i; while (j >= 0) { n++; j = d.bare.indexOf(bq, j + bq.length); }
      const a = Math.max(0, i - 70), b = Math.min(d.text.length, i + bq.length + 90);
      hits.push({ d, n, snip: (a ? "…" : "") + E.esc(d.text.slice(a, i)) + "<mark>" + E.esc(d.text.slice(i, i + bq.length)) + "</mark>" + E.esc(d.text.slice(i + bq.length, b)) + (b < d.text.length ? "…" : "") });
    }
    hits.sort((x, y) => (bare(y.d.title).includes(bq) - bare(x.d.title).includes(bq)) || y.n - x.n);
    E.$("#sr-out").innerHTML = hits.length ? `<p class="sub">${hits.length} places</p><ul class="sr-list">${hits.slice(0, 60).map((h) => `<li><a href="${h.d.href}"><span class="chip">${h.d.kind}</span> <span class="sr-title" lang="el">${E.esc(h.d.title)}</span>${h.n > 1 ? ` <span class="sub">×${h.n}</span>` : ""}</a><p class="sr-snip">${h.snip}</p></li>`).join("")}</ul>`
      : `<p class="sub">Nothing found for “${E.esc(q)}”.</p>`;
    window.scrollTo(0, 0);
  };

  /* ---------- library hub ---------- */
  routes.library = async () => {
    const E = A();
    document.title = "Resources · Ελληνικά";
    E.$("#bar-meta").textContent = "Resources";
    let idx = { shelves: [] };
    try { idx = await E.getJSON("library/index.json"); } catch (e) { /* no manifest yet */ }
    E.view.innerHTML = `<p class="crumbs"><a href="#">← Course</a></p><h2>Resources</h2>
      <form class="answer-row" id="lib-search"><input id="lib-q" lang="el" placeholder="Search lessons and readings" autocomplete="off"><button class="btn">Search</button></form>
      <div class="shelves">${idx.shelves.map((s) => s.ready
        ? `<a class="card shelf" href="#${E.esc(s.route)}"><span class="shelf-el" lang="el">${E.esc(s.el)}</span><span class="shelf-en">${E.esc(s.title)}</span></a>`
        : `<div class="card shelf planned"><span class="shelf-el" lang="el">${E.esc(s.el)}</span><span class="shelf-en">${E.esc(s.title)}</span><span class="chip new">coming</span></div>`).join("")}</div>`;
    E.$("#lib-search").onsubmit = (e) => { e.preventDefault(); const v = E.$("#lib-q").value.trim(); if (v) location.hash = "search." + encodeURIComponent(v); };
    window.scrollTo(0, 0);
  };
})();
