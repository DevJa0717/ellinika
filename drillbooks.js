/* Ελληνικά drill books (#klisi): typed production drills for declension and conjugation.
   Every item is a real word from the word list with its paradigm in library/drills/*.json (built by tools/drills/build.py).
   Books: articles and pronouns, nouns (with article), adjectives, noun phrases, verbs (active), verbs (passive and deponent),
   sentences (forms in context) and a mixed weak-spots book. Instant feedback names the form you wrote if it is another cell
   of the same paradigm and shows the table. Misses come back by spaced repetition (1, 3, 7, 21, 60 days).
   Progress is per profile in localStorage "ellinika.drillbooks.v1". Registers #klisi and #klisi.<book>. */
(function () {
  "use strict";
  const A = () => window.Ellinika;
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});
  const KEY = "ellinika.drillbooks.v1";
  const BASE = "library/drills/";
  const HEAD = "Drill books";
  const LV = ["A1", "A2", "B1", "B2", "C1"];
  const GAPS = [0, 1, 3, 7, 21, 60]; // days until a missed item comes back, by box
  const PDF_DECL = "downloads/textbook/Ellinika-Declension-drills.pdf";
  const PDF_CONJ = "downloads/textbook/Ellinika-Conjugation-drills.pdf";

  const CSS = `
.kl-hero h2 { margin: 0; font: 400 2rem/1.15 var(--f-display); }
.kl-hero p { margin: 6px 0 0; }
.kl-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; margin: 14px 0; }
.kl-stat { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 10px; text-align: center; }
.kl-stat b { display: block; font: 400 1.6rem/1.1 var(--f-display); font-variant-numeric: tabular-nums; }
.kl-stat span { font: 500 .75rem/1.2 var(--f-ui); color: var(--muted); }
.kl-books { display: grid; gap: 10px; grid-template-columns: repeat(auto-fill, minmax(min(100%, 260px), 1fr)); margin: 12px 0 20px; }
.kl-book { display: grid; gap: 4px; text-decoration: none; color: var(--ink); background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 14px 14px 12px; }
.kl-book .el { font: 400 1.3rem/1.2 var(--f-display); }
.kl-book .en { font: 500 .85rem/1.3 var(--f-ui); color: var(--muted); }
.kl-book .meta { display: flex; justify-content: space-between; gap: 8px; align-items: center; font: 500 .78rem/1.2 var(--f-ui); color: var(--muted); margin-top: 6px; }
.kl-meter { height: 6px; border-radius: 3px; background: var(--paper); overflow: hidden; }
.kl-meter i { display: block; height: 100%; background: var(--good); }
.kl-weak { width: 100%; border-collapse: collapse; font: 500 .88rem/1.3 var(--f-ui); }
.kl-weak td { padding: 6px 4px; border-bottom: 1px solid var(--line); }
.kl-weak td:last-child { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }
.kl-weak td.bad { color: var(--bad); } .kl-weak td.ok { color: var(--good); }
.kl-set { display: grid; gap: 14px; }
.kl-set h3 { margin: 0 0 6px; font: 600 .78rem/1.2 var(--f-ui); letter-spacing: .08em; text-transform: uppercase; color: var(--terra); }
.kl-chips { display: flex; flex-wrap: wrap; gap: 6px; }
.kl-chips button { border: 1px solid var(--line); background: transparent; color: var(--ink); border-radius: 999px; padding: 8px 12px; min-height: 36px; font: 500 .85rem/1 var(--f-ui); cursor: pointer; }
.kl-chips button[aria-pressed="true"] { background: var(--ink); color: var(--paper); border-color: var(--ink); }
.kl-card { gap: 12px; }
.kl-top { display: flex; justify-content: space-between; align-items: center; gap: 8px; font: 500 .8rem/1.2 var(--f-ui); color: var(--muted); }
.kl-bar { height: 4px; background: var(--paper); border-radius: 2px; overflow: hidden; }
.kl-bar i { display: block; height: 100%; background: var(--terra); transition: width .2s; }
.kl-task { font: 600 .8rem/1.3 var(--f-ui); letter-spacing: .06em; text-transform: uppercase; color: var(--terra); }
.kl-task .el { text-transform: none; letter-spacing: 0; font-weight: 500; color: var(--muted); margin-left: 6px; }
.kl-word { font: 400 2.1rem/1.15 var(--f-display); overflow-wrap: anywhere; }
.kl-word small { display: block; font: 500 .9rem/1.3 var(--f-ui); color: var(--muted); margin-top: 4px; }
.kl-sent { font-size: 1.2rem; line-height: 1.5; }
.kl-sent .gap { color: var(--terra); font-weight: 600; }
.kl-who { font: 500 1.05rem/1.2 var(--f-ui); }
.kl-pre { font-size: 1.15rem; color: var(--muted); align-self: center; }
.kl-card .answer-row input { font-size: 1.2rem; }
.kl-tbl { border-collapse: collapse; width: 100%; font-size: .98rem; }
.kl-tbl th, .kl-tbl td { padding: 5px 6px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }
.kl-tbl th { font: 600 .72rem/1.2 var(--f-ui); color: var(--muted); text-transform: uppercase; letter-spacing: .05em; }
.kl-tbl td.hit { background: var(--warn-soft); color: var(--warn); font-weight: 600; border-radius: 4px; }
.kl-tbl td.you { box-shadow: inset 0 0 0 1px var(--bad); border-radius: 4px; }
.kl-note { font-size: .9rem; color: var(--muted); margin: 0; }
.kl-due { display: flex; gap: 10px; align-items: center; justify-content: space-between; flex-wrap: wrap; }
.kl-print { display: grid; gap: 8px; }
.kl-print a { display: flex; justify-content: space-between; gap: 10px; }
@media (max-width: 420px) { .kl-word { font-size: 1.8rem; } .kl-tbl { font-size: .9rem; } }
`;
  function style() { if (document.getElementById("kl-css")) return; const s = document.createElement("style"); s.id = "kl-css"; s.textContent = CSS; document.head.appendChild(s); }

  /* ---------- labels ---------- */
  const CASE = [["nom", "Nominative", "ονομαστική"], ["gen", "Genitive", "γενική"], ["acc", "Accusative", "αιτιατική"], ["voc", "Vocative", "κλητική"]];
  const NUM = [["sg", "singular", "ενικός"], ["pl", "plural", "πληθυντικός"]];
  const GEN = [["m", "masculine", "αρσενικό"], ["f", "feminine", "θηλυκό"], ["n", "neuter", "ουδέτερο"]];
  const PERS = ["εγώ", "εσύ", "αυτός / αυτή", "εμείς", "εσείς", "αυτοί / αυτές"];
  const PERS_EN = ["1st sg", "2nd sg", "3rd sg", "1st pl", "2nd pl", "3rd pl"];
  const TENSES = {
    pres: ["Present", "ενεστώτας"], impf: ["Imperfect (past continuous)", "παρατατικός"], aor: ["Aorist (simple past)", "αόριστος"],
    fut: ["Simple future", "στιγμιαίος μέλλοντας"], perf: ["Present perfect", "παρακείμενος"], plup: ["Pluperfect", "υπερσυντέλικος"],
    impP: ["Imperative, one-off (perfective)", "στιγμιαία προστακτική"], impI: ["Imperative, ongoing (imperfective)", "εξακολουθητική προστακτική"],
  };
  const ECHO = ["έχω", "έχεις", "έχει", "έχουμε", "έχετε", "έχουν"], EICHA = ["είχα", "είχες", "είχε", "είχαμε", "είχατε", "είχαν"];
  const ART = { // [nom, gen, acc] by gender, singular then plural
    m: [["ο", "του", "τον"], ["οι", "των", "τους"]], f: [["η", "της", "τη|την"], ["οι", "των", "τις"]], n: [["το", "του", "το"], ["τα", "των", "τα"]],
  };
  // Final -ν of την: kept before a vowel and κ π τ ξ ψ (and μπ ντ γκ τσ τζ), dropped elsewhere.
  const tin = (next) => (/^[αεηιουωάέήίόύώκπτξψ]/.test(next || "") ? "την" : "τη");
  const showArt = (a, next) => (a === "τη|την" ? tin(next) : first(a));
  const art = (g, num, ci) => (ci === 3 ? "" : ART[g === "c" ? "m" : g][num][ci]);
  const cellLabel = (ci, num) => `${CASE[ci][1]} ${NUM[num][1]}`;
  const cellLabelEl = (ci, num) => `${CASE[ci][2]} ${NUM[num][2].replace("ός", "ού")}`;

  /* ---------- text ---------- */
  const ACC = { "ά": "α", "έ": "ε", "ή": "η", "ί": "ι", "ό": "ο", "ύ": "υ", "ώ": "ω", "ΐ": "ϊ", "ΰ": "ϋ" };
  const plain = (s) => s.replace(/[άέήίόύώΐΰ]/g, (c) => ACC[c]);
  // Latin look-alikes typed on a non-Greek keyboard are mapped to Greek; final σ becomes ς.
  const LAT = { a: "α", b: "β", e: "ε", h: "η", i: "ι", k: "κ", m: "μ", n: "ν", o: "ο", p: "ρ", t: "τ", u: "υ", x: "χ", y: "υ", z: "ζ" };
  function norm(s) {
    return String(s || "").normalize("NFC").toLowerCase().replace(/[’‘`΄']/g, "'").replace(/[.,;!?·«»"]/g, " ").trim().replace(/\s+/g, " ")
      .replace(/[a-z]/g, (c) => LAT[c] || c).replace(/σ(?=$|\s)/g, "ς");
  }
  const alts = (cell) => (cell ? cell.split("|") : []);
  const first = (cell) => alts(cell)[0] || "";
  // τη/την, το/τον: both spellings of the article are accepted.
  function withArt(a, forms) {
    const out = [];
    for (const x of alts(a)) for (const f of forms) out.push(x ? x + " " + f : f);
    if (a === "τη|την") for (const f of forms) out.push("τη " + f, "την " + f);
    return [...new Set(out)];
  }

  /* ---------- storage ---------- */
  const today = () => Math.floor((Date.now() - new Date().getTimezoneOffset() * 60000) / 864e5);
  function load() {
    let s = null; try { s = JSON.parse(localStorage.getItem(KEY)); } catch (e) { /* none */ }
    if (!s || s.v !== 1) s = { v: 1, it: {}, cat: {}, bk: {}, day: {} };
    return s;
  }
  let ST = load();
  function save() { try { localStorage.setItem(KEY, JSON.stringify(ST)); } catch (e) { /* storage full or blocked */ } }
  // it[id] = [box, due day or -1, right, wrong]; cat[key] = [right, total]; bk[book] = [right, total]
  function record(item, ok) {
    const r = ST.it[item.id] || [0, -1, 0, 0];
    if (ok) {
      r[2]++;
      if (r[3] > 0) { r[0] = Math.min(r[0] + 1, GAPS.length); r[1] = r[0] >= GAPS.length ? -1 : today() + GAPS[r[0]]; }
    } else { r[3]++; r[0] = 0; r[1] = today() + 1; }
    ST.it[item.id] = r;
    const c = (ST.cat[item.cat] = ST.cat[item.cat] || [0, 0]); c[0] += ok ? 1 : 0; c[1]++;
    const b = (ST.bk[item.book] = ST.bk[item.book] || [0, 0]); b[0] += ok ? 1 : 0; b[1]++;
    const d = today(); ST.day[d] = (ST.day[d] || 0) + 1;
    const keys = Object.keys(ST.day); if (keys.length > 60) delete ST.day[keys.sort()[0]];
    save();
    const E = A(), p = E.progress; p.library = p.library || {};
    p.library["klisi/" + item.book] = b[1] ? b[0] / b[1] : 0; E.saveProgress();
  }
  const dueIds = () => Object.entries(ST.it).filter(([, r]) => r[1] >= 0 && r[1] <= today()).map(([k]) => k);

  /* ---------- data ---------- */
  const cache = {};
  async function data(name) {
    if (!cache[name]) cache[name] = A().getJSON(BASE + name + ".json").catch((e) => { delete cache[name]; throw e; });
    return cache[name];
  }

  /* ---------- books: each turns an item id into a full question ---------- */
  // Item ids: n|lemma|cell  a|lemma|cell  p|adj noun|cell  r|table|cell  v|lemma|voice.tense.person  c|index
  const BOOKS = [
    { id: "pron", el: "Άρθρα και αντωνυμίες", en: "Articles and pronouns: ο/η/το, ένας, personal, demonstrative, relative and the rest", files: ["pronouns"], pdf: PDF_DECL },
    { id: "nouns", el: "Ουσιαστικά", en: "Nouns with their article, every case and number, by declension type", files: ["nouns"], pdf: PDF_DECL },
    { id: "adjs", el: "Επίθετα", en: "Adjectives in all three genders, every case and number", files: ["adjectives"], pdf: PDF_DECL },
    { id: "phr", el: "Άρθρο, επίθετο, ουσιαστικό", en: "Whole noun phrases: ο καλός φίλος → των καλών φίλων", files: ["pronouns", "nouns", "adjectives"], pdf: PDF_DECL },
    { id: "verbs", el: "Ρήματα: ενεργητική φωνή", en: "Verbs, active voice: present, imperfect, aorist, future, perfect, pluperfect, imperative", files: ["verbs"], pdf: PDF_CONJ },
    { id: "pass", el: "Ρήματα: παθητική φωνή και αποθετικά", en: "Passive voice and deponent verbs (έρχομαι, θυμάμαι …)", files: ["verbs"], pdf: PDF_CONJ },
    { id: "ctx", el: "Μέσα στη φράση", en: "Forms in context: the right form for a gap in a real sentence", files: ["context", "nouns", "adjectives", "verbs"], pdf: PDF_DECL },
    { id: "mix", el: "Τα αδύνατά μου σημεία", en: "Weak spots: a mixed set weighted toward the forms you miss most", files: ["pronouns", "nouns", "adjectives", "verbs"] },
  ];
  const bookById = (id) => BOOKS.find((b) => b.id === id);

  const FOCUS = {
    pron: [["all", "Everything"], ["art", "Articles"], ["pers", "Personal pronouns"], ["dem", "αυτός, εκείνος"], ["rel", "ο οποίος, ποιος"], ["oth", "Other pronouns"]],
    nouns: [["all", "All forms"], ["gen", "Genitive"], ["acc", "Accusative"], ["pl", "Plural"], ["voc", "Vocative"]],
    adjs: [["all", "All forms"], ["f", "Feminine"], ["n", "Neuter"], ["gen", "Genitive"], ["pl", "Plural"]],
    phr: [["all", "All cases"], ["gen", "Genitive"], ["acc", "Accusative"], ["pl", "Plural"]],
    ctx: [["all", "All"], ["n", "Nouns"], ["a", "Adjectives"], ["v", "Verbs"]],
  };
  const TYPES = [["all", "All types"], ["m-ος", "masc. -ος"], ["m-ας", "masc. -ας"], ["m-ης", "masc. -ής/-ης"], ["m-imp", "masc. -άς/-ές/-ούς (καφέδες)"], ["f-α", "fem. -α"], ["f-η-ες", "fem. -η (φωνές)"], ["f-η-εις", "fem. -η (πόλεις)"], ["f-ος", "fem. -ος"], ["n-ο", "neut. -ο"], ["n-ι", "neut. -ι"], ["n-μα", "neut. -μα"], ["n-ος", "neut. -ος"], ["oth", "other"]];
  const typeOf = (m) => (m.startsWith("m-imparisyllabic") ? "m-imp" : m.startsWith("m-ος") ? "m-ος" : m.startsWith("m-ας") ? "m-ας" : m === "m-ης" ? "m-ης" : m.startsWith("f-α") ? "f-α" : m === "f-η-ες" ? "f-η-ες" : m === "f-η-εις" ? "f-η-εις" : m === "f-ος" ? "f-ος" : m.startsWith("n-ο-") ? "n-ο" : m === "n-ι" || m === "n-ί" ? "n-ι" : m === "n-μα" || m === "n-ιμο" ? "n-μα" : m.startsWith("n-ος") ? "n-ος" : "oth");
  const VT_A = ["pres", "impf", "aor", "fut", "perf", "plup", "impP", "impI"], VT_P = ["pres", "impf", "aor", "fut", "perf", "impP"];

  // Builds the list of candidate ids for a book under the chosen settings.
  async function pool(book, opt) {
    const lvMax = LV.indexOf(opt.lv), okLv = (lv) => opt.lv === "all" || LV.indexOf(lv) <= lvMax || (lv === "C2" && lvMax >= 4);
    const out = [];
    if (book === "pron" || book === "mix") {
      const P = await data("pronouns");
      for (const t of P.tables) {
        const grp = t.id.startsWith("art") ? "art" : t.id === "pers" ? "pers" : /αυτός|εκείνος/.test(t.id) ? "dem" : /οποίος|ποιος$/.test(t.id) && t.id !== "pr-κάποιος" ? "rel" : "oth";
        if (book === "pron" && opt.focus !== "all" && opt.focus !== grp) continue;
        if (!okLv(t.lv)) continue;
        if (t.kind === "pers") t.rows.forEach((r, ri) => [1, 2, 3, 4].forEach((ci) => { if (r[ci]) out.push(`r|${t.id}|${ri}.${ci}`); }));
        else t.f.forEach((c, i) => { if (c) out.push(`r|${t.id}|${i}`); });
      }
    }
    if (book === "nouns" || book === "mix") {
      const N = await data("nouns");
      N.words.forEach((w) => {
        if (!okLv(w.lv)) return;
        if (book === "nouns" && opt.type !== "all" && typeOf(w.m) !== opt.type) return;
        w.f.forEach((c, i) => {
          if (!c) return;
          const num = i >> 2, ci = i & 3;
          if (ci === 3 && (num === 1 || w.g !== "m" && w.g !== "c" || first(c) === first(w.f[0]))) return; // vocative = nominative: nothing to drill
          if (book === "nouns") { const f = opt.focus; if (f === "gen" && ci !== 1 || f === "acc" && ci !== 2 || f === "pl" && num !== 1 || f === "voc" && ci !== 3) return; }
          out.push(`n|${w.l}|${i}`);
        });
      });
    }
    if (book === "adjs" || book === "mix") {
      const D = await data("adjectives");
      D.words.forEach((w) => {
        if (!okLv(w.lv)) return;
        w.f.forEach((c, i) => {
          if (!c) return;
          const num = Math.floor(i / 12), ci = Math.floor(i / 3) % 4, g = i % 3;
          if (ci === 3 && !(num === 0 && g === 0)) return;
          if (i === 0) return; // the dictionary form itself
          if (book === "adjs") { const f = opt.focus; if (f === "f" && g !== 1 || f === "n" && g !== 2 || f === "gen" && ci !== 1 || f === "pl" && num !== 1) return; }
          out.push(`a|${w.l}|${i}`);
        });
      });
    }
    if (book === "phr") {
      const [P, N, D] = await Promise.all([data("pronouns"), data("nouns"), data("adjectives")]);
      P.phrases.forEach((p) => {
        if (!okLv(p.lv)) return;
        const no = N.words.find((x) => x.l === p.n), ad = D.words.find((x) => x.l === p.a); if (!no || !ad) return;
        for (let i = 0; i < 8; i++) { const num = i >> 2, ci = i & 3; if (ci === 3 || i === 0) continue;
          if (!no.f[i] || !ad.f[num * 12 + ci * 3 + "mfn".indexOf(no.g)]) continue; const f = opt.focus; if (f === "gen" && ci !== 1 || f === "acc" && ci !== 2 || f === "pl" && num !== 1) continue; out.push(`p|${p.a} ${p.n}|${i}`); }
      });
    }
    if (book === "verbs" || book === "pass" || book === "mix") {
      const V = await data("verbs");
      const want = book === "mix" ? null : new Set(opt.tenses);
      V.words.forEach((w) => {
        if (!okLv(w.lv)) return;
        const voices = [];
        if (book !== "pass" && !w.dep) voices.push(["A", w.A, VT_A]);
        if (book !== "verbs") { if (w.dep) voices.push(["D", w.A, VT_P]); if (w.P) voices.push(["P", w.P, VT_P]); }
        for (const [vk, V2, tenses] of voices) for (const t of tenses) {
          if (want && !want.has(t)) continue;
          if (t === "aor" && V2.one_past) continue;
          if (t === "impP" || t === "impI") { V2[t].forEach((c, i) => { if (c) out.push(`v|${w.l}|${vk}.${t}.${i ? 4 : 1}`); }); continue; }
          const src = t === "fut" ? V2.dep : t === "perf" || t === "plup" ? null : V2[t];
          for (let p = 0; p < 6; p++) {
            if (src && !src[p]) continue;
            if ((t === "perf" || t === "plup") && !V2.inf) continue;
            if ((t === "perf" || t === "plup") && p % 2) continue; // half the persons: the participle part is the same
            if (t === "pres" && p === 0 && vk !== "P") continue; // the dictionary form itself
            out.push(`v|${w.l}|${vk}.${t}.${p}`);
          }
        }
      });
    }
    if (book === "ctx") {
      const C = await data("context");
      C.items.forEach((x, i) => { if (okLv(x.lv) && (opt.focus === "all" || opt.focus === x.k)) out.push(`c|${i}`); });
    }
    return out;
  }

  // Turns an id into a question: {id, book, cat, task, taskEl, word, gloss, who, pre, sent, en, answers[], show, table(), others[]}
  async function make(id, book) {
    const [k, a, b] = id.split("|");
    if (k === "n") {
      const N = await data("nouns"), w = N.words.find((x) => x.l === a); if (!w) return null;
      const i = +b, num = i >> 2, ci = i & 3, forms = alts(w.f[i]);
      const ar = art(w.g, num, ci), lemmaArt = w.g === "c" ? "ο/η" : ART[w.g][0][0];
      let answers = ci === 3 ? forms : withArt(ar, forms);
      if (w.g === "c" && ci !== 3) answers = [...answers, ...withArt(ART.f[num][ci], forms)];
      const others = [];
      w.f.forEach((c, j) => { if (j !== i && c) for (const f of alts(c)) others.push([f, cellLabel(j & 3, j >> 2)]); });
      return { id, book: book || "nouns", cat: `n.${CASE[ci][0]}.${NUM[num][0]}`, task: cellLabel(ci, num), taskEl: cellLabelEl(ci, num),
        word: `${lemmaArt} ${w.l}`, gloss: w.en, pre: "", ph: ci === 3 ? "vocative form" : "article + noun", answers, show: (ci === 3 ? "" : showArt(ar, forms[0]) + " ") + forms[0], strip: true,
        note: N.notes[w.m] || "", table: () => nounTable(w, i), others };
    }
    if (k === "a") {
      const D = await data("adjectives"), w = D.words.find((x) => x.l === a); if (!w) return null;
      const i = +b, num = Math.floor(i / 12), ci = Math.floor(i / 3) % 4, g = i % 3, forms = alts(w.f[i]);
      const others = []; w.f.forEach((c, j) => { if (j !== i && c) for (const f of alts(c)) others.push([f, `${GEN[j % 3][1]} ${cellLabel(Math.floor(j / 3) % 4, Math.floor(j / 12))}`]); });
      const ar = ci === 3 ? "" : showArt(ART["mfn"[g]][num][ci], forms[0]);
      return { id, book: book || "adjs", cat: `a.${CASE[ci][0]}.${NUM[num][0]}`, task: `${GEN[g][1]} ${cellLabel(ci, num)}`, taskEl: `${GEN[g][2]}, ${cellLabelEl(ci, num)}`,
        word: w.l, gloss: w.en, pre: ar, answers: [...forms, ...forms.flatMap((f) => withArt(ART["mfn"[g]][num][ci], [f]))], show: forms[0], note: D.notes[w.m] || "", table: () => adjTable(w, i), others };
    }
    if (k === "p") {
      const [N, D, P] = await Promise.all([data("nouns"), data("adjectives"), data("pronouns")]);
      const [aw, nw] = a.split(" "), ad = D.words.find((x) => x.l === aw), no = N.words.find((x) => x.l === nw), ph = P.phrases.find((x) => x.a === aw && x.n === nw);
      if (!ad || !no) return null;
      const i = +b, num = i >> 2, ci = i & 3, gi = "mfn".indexOf(no.g);
      const af = alts(ad.f[num * 12 + ci * 3 + gi]), nf = alts(no.f[i]);
      const combos = []; for (const x of af) for (const y of nf) combos.push(x + " " + y);
      return { id, book: "phr", cat: `p.${CASE[ci][0]}.${NUM[num][0]}`, task: cellLabel(ci, num), taskEl: cellLabelEl(ci, num),
        word: `${ART[no.g][0][0]} ${aw} ${nw}`, gloss: ph ? ph.en : "", ph: "article + adjective + noun", answers: withArt(art(no.g, num, ci), combos), show: `${showArt(art(no.g, num, ci), af[0])} ${af[0]} ${nf[0]}`,
        note: "Article, adjective and noun agree in gender, number and case. " + (N.notes[no.m] || ""), table: () => phraseTable(ad, no, i), others: [] };
    }
    if (k === "r") {
      const P = await data("pronouns"), t = P.tables.find((x) => x.id === a); if (!t) return null;
      if (t.kind === "pers") {
        const [ri, ci] = b.split(".").map(Number), cols = ["nominative", "genitive, strong", "genitive, weak", "accusative, strong", "accusative, weak"];
        const colsEl = ["ονομαστική", "γενική, δυνατός τύπος", "γενική, αδύνατος τύπος", "αιτιατική, δυνατός τύπος", "αιτιατική, αδύνατος τύπος"];
        const forms = alts(t.rows[ri][ci]);
        const others = []; t.rows[ri].forEach((c, j) => { if (j !== ci) for (const f of alts(c)) others.push([f, cols[j]]); });
        return { id, book: "pron", cat: `r.pers.${ci}`, task: cols[ci], taskEl: colsEl[ci], word: t.rows[ri][0], gloss: "personal pronoun", answers: forms, show: forms[0], note: t.note, table: () => persTable(t, ri, ci), others };
      }
      const i = +b, num = Math.floor(i / 9), ci = Math.floor(i / 3) % 3, g = i % 3, forms = alts(t.f[i]);
      const others = []; t.f.forEach((c, j) => { if (j !== i && c) for (const f of alts(c)) others.push([f, `${GEN[j % 3][1]} ${cellLabel(Math.floor(j / 3) % 3, Math.floor(j / 9))}`]); });
      const rel = t.id === "pr-οποίος";
      const ans = rel ? forms.flatMap((f) => withArt(ART["mfn"[g]][num][ci], [f])) : forms;
      return { id, book: "pron", cat: t.id.startsWith("art") ? `r.art.${CASE[ci][0]}` : `r.${CASE[ci][0]}.${NUM[num][0]}`, task: `${GEN[g][1]} ${cellLabel(ci, num)}`, taskEl: `${GEN[g][2]}, ${cellLabelEl(ci, num)}`,
        word: t.l, gloss: t.en, answers: ans, show: rel ? showArt(ART["mfn"[g]][num][ci], forms[0]) + " " + forms[0] : forms[0], note: t.note, table: () => g3Table(t, i), others };
    }
    if (k === "v") {
      const V = await data("verbs"), w = V.words.find((x) => x.l === a); if (!w) return null;
      const [vk, t, ps] = b.split("."), p = +ps, src = vk === "P" ? w.P : w.A; if (!src) return null;
      let forms, pre = "", who = PERS[p];
      if (t === "fut") { forms = alts(src.dep[p]); pre = "θα"; }
      else if (t === "perf") forms = [ECHO[p] + " " + src.inf];
      else if (t === "plup") forms = [EICHA[p] + " " + src.inf];
      else if (t === "impP" || t === "impI") { forms = alts(src[t][p === 1 ? 0 : 1]); who = p === 1 ? "εσύ" : "εσείς"; }
      else forms = alts(src[t][p]);
      if (!forms.length || !forms[0]) return null;
      const answers = pre ? [...forms, ...forms.map((f) => pre + " " + f)] : forms;
      const others = [];
      for (const tt of ["pres", "impf", "aor", "dep"]) (src[tt] || []).forEach((c, j) => { if (!(tt === t && j === p)) for (const f of alts(c)) others.push([f, `${tt === "dep" ? "dependent (θα/να)" : TENSES[tt][0].toLowerCase()}, ${PERS_EN[j]}`]); });
      const voice = vk === "P" ? "passive" : vk === "D" ? "deponent" : "active";
      const lemma = vk === "P" ? first(w.P.pres[0]) : w.l;
      return { id, book: vk === "A" ? "verbs" : "pass", cat: `v.${vk === "A" ? "A" : "P"}.${t}`, task: TENSES[t][0] + (vk === "P" ? ", passive" : ""), taskEl: TENSES[t][1],
        word: lemma, gloss: vk === "P" ? `passive of ${w.l} (${w.en})` : w.en, who, pre, answers, show: forms[0],
        note: verbNote(w, src, t, voice), table: () => verbTable(w, src, t, p, pre), others };
    }
    if (k === "c") {
      const C = await data("context"), x = C.items[+a]; if (!x) return null;
      const label = await ctxLabel(x);
      const parts = x.s.split("___");
      return { id, book: "ctx", cat: `c.${x.k}`, task: "Fill the gap", taskEl: "συμπλήρωσε το κενό", sent: [parts[0], parts.slice(1).join("___")], en: x.en,
        word: x.l, gloss: label, answers: [x.a.toLowerCase()], show: x.a, note: "", table: () => "", others: [] };
    }
    return null;
  }

  async function ctxLabel(x) {
    const labs = [];
    for (const c of x.c) {
      if (x.k === "n") labs.push(cellLabel(c & 3, c >> 2));
      else if (x.k === "a") labs.push(`${GEN[c % 3][1]} ${cellLabel(Math.floor(c / 3) % 4, Math.floor(c / 12))}`);
      else { const [vk, t, p] = String(c).split("."); labs.push(`${t === "dep" ? "θα/να form" : TENSES[t][0].toLowerCase()}${vk === "P" ? " passive" : ""}, ${PERS_EN[+p]}`); }
    }
    const u = [...new Set(labs.map((x) => x.toLowerCase()))];
    return u.length > 2 ? u.slice(0, 2).join(" or ") + " …" : u.join(" or ");
  }

  /* ---------- tables shown with the feedback ---------- */
  const E_ = (s) => A().esc(s);
  const td = (txt, hit) => `<td lang="el"${hit ? ' class="hit"' : ""}>${E_(txt)}</td>`;
  function nounTable(w, hit) {
    const rows = CASE.map(([, en, el], ci) => {
      const cells = [0, 1].map((num) => { const i = num * 4 + ci, f = w.f[i]; return td(f ? (art(w.g, num, ci) ? showArt(art(w.g, num, ci), first(f)) + " " : "") + alts(f).join(" / ") : "—", i === hit); });
      return `<tr><th scope="row">${en.slice(0, 3)}.</th>${cells.join("")}</tr>`;
    });
    return `<table class="kl-tbl"><thead><tr><th></th><th>singular</th><th>plural</th></tr></thead><tbody>${rows.join("")}</tbody></table>`;
  }
  function adjTable(w, hit) {
    const num = Math.floor(hit / 12);
    const rows = CASE.map(([, en], ci) => `<tr><th scope="row">${en.slice(0, 3)}.</th>${[0, 1, 2].map((g) => { const i = num * 12 + ci * 3 + g; return td(alts(w.f[i]).join(" / ") || "—", i === hit); }).join("")}</tr>`);
    return `<table class="kl-tbl"><thead><tr><th>${NUM[num][1]}</th><th>masc.</th><th>fem.</th><th>neut.</th></tr></thead><tbody>${rows.join("")}</tbody></table>`;
  }
  function phraseTable(ad, no, hit) {
    const gi = "mfn".indexOf(no.g);
    const rows = [0, 1, 2].map((ci) => `<tr><th scope="row">${CASE[ci][1].slice(0, 3)}.</th>${[0, 1].map((num) => { const i = num * 4 + ci; return td(`${showArt(art(no.g, num, ci), first(ad.f[num * 12 + ci * 3 + gi]))} ${first(ad.f[num * 12 + ci * 3 + gi])} ${first(no.f[i])}`, i === hit); }).join("")}</tr>`);
    return `<table class="kl-tbl"><thead><tr><th></th><th>singular</th><th>plural</th></tr></thead><tbody>${rows.join("")}</tbody></table>`;
  }
  function g3Table(t, hit) {
    const num = Math.floor(hit / 9);
    const rows = [0, 1, 2].map((ci) => `<tr><th scope="row">${CASE[ci][1].slice(0, 3)}.</th>${[0, 1, 2].map((g) => { const i = num * 9 + ci * 3 + g; return td(alts(t.f[i]).join(" / ") || "—", i === hit); }).join("")}</tr>`);
    return `<table class="kl-tbl"><thead><tr><th>${NUM[num][1]}</th><th>masc.</th><th>fem.</th><th>neut.</th></tr></thead><tbody>${rows.join("")}</tbody></table>`;
  }
  function persTable(t, ri, ci) {
    const rows = t.rows.map((r, i) => `<tr>${r.map((c, j) => td(alts(c).join(" / "), i === ri && j === ci)).join("")}</tr>`);
    return `<div class="tbl-wrap"><table class="kl-tbl"><thead><tr><th>nom.</th><th>gen.</th><th>gen. weak</th><th>acc.</th><th>acc. weak</th></tr></thead><tbody>${rows.join("")}</tbody></table></div>`;
  }
  function verbTable(w, src, t, p, pre) {
    let row;
    if (t === "perf") row = ECHO.map((x) => x + " " + src.inf);
    else if (t === "plup") row = EICHA.map((x) => x + " " + src.inf);
    else if (t === "fut") row = src.dep.map((c) => (c ? "θα " + first(c) : "—"));
    else if (t === "impP" || t === "impI") return `<table class="kl-tbl"><tbody>${["εσύ", "εσείς"].map((x, i) => `<tr><th scope="row">${x}</th>${td(alts(src[t][i]).join(" / ") || "—", (p === 1 ? 0 : 1) === i)}</tr>`).join("")}</tbody></table>`;
    else row = src[t].map((c) => alts(c).join(" / ") || "—");
    return `<table class="kl-tbl"><tbody>${row.map((x, i) => `<tr><th scope="row">${PERS[i]}</th>${td(x, i === p)}</tr>`).join("")}</tbody></table>`;
  }
  function verbNote(w, src, t, voice) {
    const s = [];
    const a1 = first(src.aor[0]), d1 = first(src.dep[0]), p1 = first(src.pres[0]);
    if (t === "aor" || t === "fut" || t === "perf" || t === "plup" || t === "impP") s.push(`Principal parts: ${p1} · ${a1}${d1 && d1 !== p1 ? " · (θα) " + d1 : ""}${src.inf ? " · έχω " + src.inf : ""}.`);
    if (t === "aor" && voice === "active") s.push("The past tenses add the augment έ- when the stress would otherwise fall before the stem (έγραψα but γράψαμε).");
    if (t === "impf" && voice !== "active") s.push("Passive imperfect endings: -όμουν, -όσουν, -όταν, -όμασταν, -όσασταν, -ονταν.");
    if (t === "aor" && voice !== "active") s.push("Passive aorist: perfective stem + -θηκα / -τηκα, stress on the third syllable from the end (-θηκα, -θήκαμε).");
    if (t === "fut") s.push("θα + the perfective (dependent) form, the same form that follows να.");
    if (t === "perf" || t === "plup") s.push(`έχω/είχα + the invariable form ${src.inf} (the 3rd singular of the dependent).`);
    if (w.A.one_past && t === "impf") s.push("This verb has one past tense only, so the imperfect also does the aorist's job.");
    return s.join(" ");
  }

  /* ---------- feedback ---------- */
  function judge(q, given) {
    const g = norm(given), ok = q.answers.map(norm);
    if (!g) return { st: "wrong", msg: "No answer." };
    if (ok.includes(g)) return { st: "right" };
    if (ok.map(plain).includes(plain(g))) return { st: "almost", msg: "Right letters, wrong accent." };
    const bare = g.split(" ").pop();
    if (q.strip && ok.some((x) => x.split(" ").pop() === bare)) return { st: "almost", msg: "The noun is right; check the article." };
    const hit = q.others.find(([f]) => norm(f) === bare || norm(f) === g);
    if (hit) return { st: "wrong", msg: `That is the ${hit[1]} form.` };
    return { st: "wrong" };
  }

  /* ---------- screens ---------- */
  function settings(book) {
    let s = {}; try { s = JSON.parse(localStorage.getItem(KEY + ".set")) || {}; } catch (e) { /* none */ }
    const b = s[book] || {};
    return { lv: b.lv || "B2", focus: b.focus || "all", type: b.type || "all", n: b.n || 20, tenses: b.tenses || (book === "pass" ? VT_P.slice(0, 4) : ["pres", "impf", "aor", "fut"]) };
  }
  function saveSettings(book, o) {
    let s = {}; try { s = JSON.parse(localStorage.getItem(KEY + ".set")) || {}; } catch (e) { /* none */ }
    s[book] = o; try { localStorage.setItem(KEY + ".set", JSON.stringify(s)); } catch (e) { /* ignore */ }
  }
  const pct = (r) => (r && r[1] ? Math.round((r[0] / r[1]) * 100) : null);

  const CATNAME = (c) => {
    const [k, x, y] = c.split(".");
    const cs = { nom: "nominative", gen: "genitive", acc: "accusative", voc: "vocative" }, nm = { sg: "singular", pl: "plural" };
    if (k === "n") return `Nouns · ${cs[x]} ${nm[y]}`;
    if (k === "a") return `Adjectives · ${cs[x]} ${nm[y]}`;
    if (k === "p") return `Noun phrases · ${cs[x]} ${nm[y]}`;
    if (k === "v") return `Verbs · ${x === "P" ? "passive " : ""}${TENSES[y] ? TENSES[y][0].toLowerCase() : y}`;
    if (k === "r") return x === "art" ? `Article · ${cs[y]}` : x === "pers" ? "Personal pronouns" : `Pronouns · ${cs[x]} ${nm[y]}`;
    if (k === "c") return `In context · ${{ n: "nouns", a: "adjectives", v: "verbs" }[x]}`;
    return c;
  };

  async function hub() {
    const E = A(); style();
    E.$("#bar-meta").textContent = HEAD; document.title = HEAD + " · Ελληνικά";
    ST = load();
    const due = dueIds().length, seen = Object.keys(ST.it).length, tot = Object.values(ST.bk).reduce((a, b) => [a[0] + b[0], a[1] + b[1]], [0, 0]);
    const weak = Object.entries(ST.cat).filter(([, r]) => r[1] >= 5).map(([c, r]) => [c, r[0] / r[1], r[1]]).sort((a, b) => a[1] - b[1]).slice(0, 8);
    E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p>
      <div class="kl-hero"><h2 lang="el">Τετράδια κλίσης</h2><p class="sub">Declension and conjugation drill books: type the form, get instant feedback with the full table, and see your misses again after 1, 3, 7, 21 and 60 days until they stick. Every item is a real word from the word list with its real paradigm.</p></div>
      <div class="kl-stats"><div class="kl-stat"><b>${seen}</b><span>items practised</span></div><div class="kl-stat"><b>${tot[1] ? Math.round((tot[0] / tot[1]) * 100) + "%" : "–"}</b><span>right first time</span></div><div class="kl-stat"><b>${due}</b><span>misses due today</span></div></div>
      ${due ? `<section class="card kl-due"><span><b>${due}</b> missed ${due === 1 ? "form is" : "forms are"} due for review.</span><a class="btn small" href="#klisi.review">Review now</a></section>` : ""}
      <div class="kl-books">${BOOKS.map((b) => { const r = ST.bk[b.id], p = pct(r); return `<a class="kl-book" href="#klisi.${b.id}"><span class="el" lang="el">${E.esc(b.el)}</span><span class="en">${E.esc(b.en)}</span>
        <span class="meta"><span>${r ? `${r[1]} answered` : "not started"}</span><span>${p != null ? p + "%" : ""}</span></span>${p != null ? `<span class="kl-meter"><i style="width:${p}%"></i></span>` : ""}</a>`; }).join("")}</div>
      ${weak.length ? `<section class="card"><h3>Where you miss most</h3><table class="kl-weak"><tbody>${weak.map(([c, v, n]) => `<tr><td>${E.esc(CATNAME(c))}</td><td class="${v < 0.7 ? "bad" : "ok"}">${Math.round(v * 100)}% of ${n}</td></tr>`).join("")}</tbody></table><p><a class="btn small ghost" href="#klisi.mix">Practise the weak spots</a></p></section>` : ""}
      <section class="card kl-print"><h3>Printable drill books</h3><p class="sub">The same items on paper, grouped by declension type and tense, with answer keys at the back.</p>
        <a class="btn ghost" href="${PDF_DECL}" target="_blank" rel="noopener"><span lang="el">Κλίση ονομάτων</span><small>nouns, adjectives, articles, pronouns · PDF</small></a>
        <a class="btn ghost" href="${PDF_CONJ}" target="_blank" rel="noopener"><span lang="el">Συζυγία ρημάτων</span><small>verbs, all tenses and voices · PDF</small></a></section>
      <p class="kl-note">Paradigms come from Wiktionary's inflection tables (CC BY-SA 4.0) and are kept only where they agree with the app's word list; regular words without a Wiktionary table were generated by rule and kept only where every form matches the word list's own forms index.</p>`;
    window.scrollTo(0, 0);
  }

  async function setup(bk) {
    const E = A(); style();
    const B = bookById(bk), o = settings(bk);
    E.$("#bar-meta").textContent = HEAD; document.title = B.el + " · " + HEAD;
    const chips = (name, list, cur, multi) => `<div class="kl-chips" data-name="${name}">${list.map(([v, l]) => `<button type="button" data-v="${E.esc(v)}" aria-pressed="${multi ? cur.includes(v) : cur === v}"${l.match(/[α-ω]/) ? ' lang="el"' : ""}>${E.esc(l)}</button>`).join("")}</div>`;
    const tenses = bk === "verbs" ? VT_A : VT_P;
    E.view.innerHTML = `<p class="crumbs"><a href="#klisi">← Drill books</a></p>
      <div class="kl-hero"><h2 lang="el">${E.esc(B.el)}</h2><p class="sub">${E.esc(B.en)}</p></div>
      <section class="card kl-set">
        <div><h3>Words up to level</h3>${chips("lv", [...LV.map((l) => [l, l]), ["all", "All"]], o.lv)}</div>
        ${FOCUS[bk] ? `<div><h3>Focus</h3>${chips("focus", FOCUS[bk], o.focus)}</div>` : ""}
        ${bk === "nouns" ? `<div><h3>Declension type</h3>${chips("type", TYPES, o.type)}</div>` : ""}
        ${bk === "verbs" || bk === "pass" ? `<div><h3>Tenses</h3>${chips("tenses", tenses.map((t) => [t, TENSES[t][0].replace(/ \(.*\)/, "")]), o.tenses, true)}</div>` : ""}
        <div><h3>Questions per round</h3>${chips("n", [[10, "10"], [20, "20"], [40, "40"], [80, "80"]].map(([a, b]) => [String(a), b]), String(o.n))}</div>
        <p id="kl-count" class="sub">Counting items…</p>
        <p><button class="btn" id="kl-go">Start</button></p>
      </section>`;
    const upd = async () => { const ids = await pool(bk, o); E.$("#kl-count").textContent = ids.length ? `${ids.length.toLocaleString("en")} items in this selection.` : "No items match; widen the selection."; E.$("#kl-go").disabled = !ids.length; };
    E.view.querySelectorAll(".kl-chips").forEach((box) => box.addEventListener("click", (ev) => {
      const btn = ev.target.closest("button"); if (!btn) return;
      const name = box.dataset.name, v = btn.dataset.v;
      if (name === "tenses") { const s = new Set(o.tenses); s.has(v) ? s.delete(v) : s.add(v); if (!s.size) return; o.tenses = tenses.filter((t) => s.has(t)); btn.setAttribute("aria-pressed", s.has(v)); }
      else { o[name] = name === "n" ? +v : v; box.querySelectorAll("button").forEach((x) => x.setAttribute("aria-pressed", x === btn)); }
      saveSettings(bk, o); upd();
    }));
    E.$("#kl-go").onclick = () => run(bk, o);
    upd();
    window.scrollTo(0, 0);
  }

  // Picks a round: due misses first, then unseen items, weighted toward weak categories; seen-and-right items last.
  async function pick(bk, o) {
    const due = new Set(dueIds());
    const n = o.n || 20;
    if (bk === "review") return shuffle([...due]).slice(0, Math.max(n, 40)); // every book, sentences and phrases included
    const ids = await pool(bk, bk === "mix" ? { lv: "all", focus: "all", type: "all", tenses: VT_A } : o);
    let chosen = ids.filter((id) => due.has(id));
    chosen = shuffle(chosen).slice(0, Math.ceil(n / 2));
    const fresh = ids.filter((id) => !ST.it[id] && !due.has(id)), seenOk = ids.filter((id) => ST.it[id] && !due.has(id));
    const catOf = (id) => id.split("|")[0];
    const weight = (id) => {
      if (bk !== "mix") return 1;
      const q = ST.cat; let w = 1;
      for (const [c, r] of Object.entries(q)) if (c[0] === catOf(id) && r[1] >= 5) w = Math.max(w, 1 + 3 * (1 - r[0] / r[1]));
      return w;
    };
    const want = n - chosen.length;
    // Sample fresh items: earlier (more frequent, lower level) words are likelier, but the whole range appears.
    const take = [];
    const src = fresh.length ? fresh : seenOk;
    for (let tries = 0; take.length < want && tries < want * 30 && src.length; tries++) {
      const r = Math.random(), i = Math.floor(Math.pow(r, 1.6) * src.length), id = src[i];
      if (take.includes(id) || chosen.includes(id)) continue;
      if (Math.random() * 4 > weight(id) && bk === "mix" && tries < want * 10) continue;
      take.push(id);
    }
    return shuffle([...chosen, ...take]).slice(0, n);
  }
  function shuffle(a) { for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }

  async function run(bk, o) {
    const E = A(); style();
    E.view.innerHTML = `<p class="sub">Preparing the round…</p>`;
    let ids;
    try { ids = await pick(bk, o); } catch (e) { E.view.innerHTML = `<p>The drill data could not load: ${E.esc(e.message)}</p>`; return; }
    if (!ids.length) { E.view.innerHTML = `<p class="crumbs"><a href="#klisi">← Drill books</a></p><section class="card"><p>Nothing due right now. Pick a book to practise.</p></section>`; return; }
    const queue = ids.slice(), done = [], again = new Set();
    let right = 0, total = 0;
    const B = bookById(bk) || { el: "Επανάληψη", en: "Review of misses" };
    const next = async () => {
      if (!queue.length) return finish();
      const id = queue.shift();
      const q = await make(id, bk === "mix" || bk === "review" ? null : bk);
      if (!q) return next();
      show(q);
    };
    const show = (q) => {
      const n = done.length + 1, all = done.length + queue.length + 1;
      E.view.innerHTML = `<p class="crumbs"><a href="#klisi${bk === "review" ? "" : "." + bk}">← ${E.esc(B.el)}</a></p>
        <article class="card kl-card">
          <div class="kl-top"><span>${n} / ${all}</span><span>${total ? Math.round((right / total) * 100) + "% right" : ""}</span></div>
          <div class="kl-bar"><i style="width:${Math.round(((n - 1) / all) * 100)}%"></i></div>
          <div class="kl-task">${E.esc(q.task)}<span class="el" lang="el">${E.esc(q.taskEl)}</span></div>
          ${q.sent ? `<p class="kl-sent" lang="el">${E.esc(q.sent[0])}<span class="gap">_____</span>${E.esc(q.sent[1])}</p><p class="sub">${E.esc(q.en)}</p><p class="kl-word" style="font-size:1.4rem" lang="el">${E.esc(q.word)}<small>${E.esc(q.gloss)}</small></p>`
            : `<p class="kl-word" lang="el">${E.esc(q.word)}<small>${E.esc(q.gloss)}</small></p>`}
          ${q.who ? `<p class="kl-who" lang="el">${E.esc(q.who)}</p>` : ""}
          <form class="answer-row" id="kl-f" autocomplete="off">${q.pre ? `<span class="kl-pre" lang="el">${E.esc(q.pre)}</span>` : ""}<input id="kl-in" lang="el" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="go" aria-label="Your answer"${q.ph ? ` placeholder="${E.esc(q.ph)}"` : ""}><button class="btn" id="kl-ok">Check</button></form>
          <div id="kl-fb"></div>
        </article>`;
      const inp = E.$("#kl-in"); inp.focus({ preventScroll: true });
      let answered = false;
      E.$("#kl-f").onsubmit = (ev) => {
        ev.preventDefault();
        if (answered) return next();
        const v = inp.value; if (!v.trim()) return;
        answered = true;
        const j = judge(q, v), ok = j.st === "right";
        total++; if (ok) right++;
        if (!again.has(q.id)) record(q, ok);
        done.push([q, v, ok]);
        if (!ok && !again.has(q.id)) { again.add(q.id); queue.splice(Math.min(queue.length, 3 + Math.floor(Math.random() * 3)), 0, q.id); }
        inp.classList.add(ok ? "right" : j.st); inp.readOnly = true;
        E.$("#kl-ok").textContent = "Next";
        E.$("#kl-fb").innerHTML = `<div class="feedback ${j.st}"><b>${ok ? "Right." : j.msg ? E.esc(j.msg) : "Not quite."}</b>${ok && q.answers.length > 1 && norm(v) !== norm(q.show) ? `<span class="why">Main form: <span lang="el">${E.esc(q.show)}</span></span>` : ""}${!ok ? `<span class="why">Answer: <b lang="el">${q.pre ? E.esc(q.pre) + " " : ""}${E.esc(q.show)}</b></span>` : ""}</div>
          ${ok ? "" : `<div class="tbl-wrap">${q.table()}</div>${q.note ? `<p class="kl-note">${E.esc(q.note)}</p>` : ""}`}`;
        E.$("#kl-ok").focus({ preventScroll: true });
        if (!ok) E.$("#kl-fb").scrollIntoView({ block: "nearest", behavior: "smooth" });
      };
    };
    const finish = () => {
      const miss = done.filter(([, , ok]) => !ok);
      E.view.innerHTML = `<p class="crumbs"><a href="#klisi">← Drill books</a></p>
        <section class="card result"><div class="score">${total ? Math.round((right / total) * 100) : 0}%</div><p>${right} of ${total} right${miss.length ? `; ${miss.length} ${miss.length === 1 ? "miss comes" : "misses come"} back tomorrow, then after 3, 7, 21 and 60 days` : ""}.</p>
        <div class="actions"><button class="btn" id="kl-again">Another round</button><a class="btn ghost" href="#klisi">All books</a></div></section>
        ${miss.length ? `<section class="card"><h3>To remember</h3><ul class="ex-list">${miss.map(([q, v]) => `<li><span class="ex-el" lang="el">${E.esc(q.word)} → <b>${q.pre ? E.esc(q.pre) + " " : ""}${E.esc(q.show)}</b></span><span class="ex-en">${E.esc(q.task)}${q.who ? " · " + E.esc(q.who) : ""} · you wrote <span lang="el">${E.esc(v)}</span></span></li>`).join("")}</ul></section>` : ""}`;
      E.$("#kl-again").onclick = () => run(bk, o);
      window.scrollTo(0, 0);
    };
    next();
  }

  routes.klisi = async (arg) => {
    const E = A(); style();
    try {
      if (!arg) return await hub();
      if (arg === "review") return await run("review", { n: 40 });
      if (arg === "mix") return await run("mix", { n: 30 });
      if (bookById(arg)) return await setup(arg);
      return await hub();
    } catch (e) { E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><p>Drill books could not load: ${E.esc(e.message)}</p>`; }
  };
  // for the printable books and tests
  window.EllinikaDrills = { norm, plain, judge, make, pool };
})();
