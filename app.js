/* Ελληνικά course engine.
   Lessons are JSON in lessons/; grammar and vocabulary come from the shared data/ folder.
   Lesson "blocks" render the Learn tab; "practice" specs are expanded by GENERATORS into exercise items. */
(function () {
  "use strict";

  const $ = (sel, el = document) => el.querySelector(sel);
  // Sticky tabs and toolbars sit just under the header, whose height varies with the safe area and wrapping.
  const bar = document.querySelector(".bar");
  if (bar && window.ResizeObserver) new ResizeObserver(() => document.documentElement.style.setProperty("--bar-h", bar.offsetHeight + "px")).observe(bar);
  const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const shuffle = (a) => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const pick = (a) => a[Math.floor(Math.random() * a.length)];
  const sample = (a, n) => shuffle(a).slice(0, n);
  const uniq = (a) => [...new Set(a)];

  // Minimal inline markup for lesson prose: **bold**, *italic*, and paragraphs.
  const md = (s) => esc(s).replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>").replace(/\*(.+?)\*/g, "<em>$1</em>");
  const paras = (s) => String(s).split(/\n\n+/).map((p) => `<p>${md(p)}</p>`).join("");

  /* ---------- storage (per-device progress) ---------- */
  const STORE_KEY = "ellinika.progress.v1";
  function loadProgress() { try { return JSON.parse(localStorage.getItem(STORE_KEY)) || {}; } catch (e) { return {}; } }
  function saveProgress(p) { try { localStorage.setItem(STORE_KEY, JSON.stringify(p)); } catch (e) { /* storage unavailable */ } }
  let progress = loadProgress();

  /* ---------- data loading ---------- */
  // The app looks for data/ beside itself (published preview) and falls back to ../data/ (project folder layout).
  let DATA_ROOT = null;
  const cache = {};
  async function getJSON(url) {
    if (!cache[url]) cache[url] = fetch(url).then((r) => { if (!r.ok) throw new Error(url + " " + r.status); return r.json(); });
    return cache[url];
  }
  async function dataRoot() {
    if (DATA_ROOT) return DATA_ROOT;
    for (const root of ["data/", "../data/"]) {
      try { const r = await fetch(root + "grammar/glossary.json", { method: "GET" }); if (r.ok) { DATA_ROOT = root; return root; } } catch (e) { /* try next */ }
    }
    throw new Error("Could not find the data folder");
  }
  // Source refs look like "grammar/nouns-full.json#paradigms[id=m-ος-fixed].sg"
  async function resolve(ref) {
    const [file, path] = ref.split("#");
    let obj = await getJSON((await dataRoot()) + file);
    if (!path) return obj;
    for (const part of path.match(/[^.\[\]]+(\[[^\]]+\])?/g)) {
      const m = part.match(/^([^\[]+)(?:\[([^=\]]+)=([^\]]+)\])?$/);
      obj = obj?.[m[1]];
      if (m[2]) obj = (obj || []).find((x) => String(x[m[2]]) === m[3]);
    }
    return obj;
  }

  // Vocabulary: every core list present, merged by lemma.
  let lexPromise = null;
  function lexicon() {
    if (!lexPromise) lexPromise = (async () => {
      const root = await dataRoot();
      // core-3000.json holds only ranks 1001+, so merge it onto core-1000 (keyed by lemma).
      const out = [], seen = new Set();
      for (const f of ["lexicon/core-1000.json", "lexicon/core-3000.json", "colloquial/colloquial-lexicon.json"]) {
        try { const r = await fetch(root + f); if (r.ok) { const d = await r.json(); for (const e of (Array.isArray(d) ? d : d.entries)) if (!seen.has(e.lemma)) { seen.add(e.lemma); out.push(e); } } } catch (e) { /* missing file */ }
      }
      return out;
    })();
    return lexPromise;
  }

  /* ---------- Greek text helpers ---------- */
  const ACC = { "ά": "α", "έ": "ε", "ή": "η", "ί": "ι", "ό": "ο", "ύ": "υ", "ώ": "ω", "ΐ": "ϊ", "ΰ": "ϋ", "Ά": "Α", "Έ": "Ε", "Ή": "Η", "Ί": "Ι", "Ό": "Ο", "Ύ": "Υ", "Ώ": "Ω" };
  const ADD_ACC = Object.fromEntries(Object.entries(ACC).map(([a, b]) => [b, a]));
  const stripAccents = (s) => s.replace(/[άέήίόύώΐΰΆΈΉΊΌΎΏ]/g, (c) => ACC[c]);
  function norm(s) {
    return String(s).normalize("NFC").trim().toLowerCase().replace(/[’‘`]/g, "'").replace(/[,«»"]/g, "").replace(/\s+/g, " ")
      .replace(/σ(?=$|[\s.,;!?·])/g, "ς").replace(/[.;!?·]+$/, "").replace(/;/g, ";");
  }
  // "χάνουν(ε)" -> ["χάνουν","χάνουνε"]; "είστε/είσαστε" -> both
  function variants(form) {
    const out = [];
    for (const alt of String(form).split("/")) {
      const a = alt.trim();
      const m = a.match(/^(.*)\(([^)]+)\)(.*)$/);
      if (m) { out.push(m[1] + m[3], m[1] + m[2] + m[3]); } else out.push(a);
    }
    return uniq(out.map((x) => x.trim()).filter(Boolean));
  }
  // Compare a typed answer with the accepted forms: "right", "almost" (accent only), or "wrong".
  function grade(input, forms) {
    const n = norm(input);
    if (!n) return "wrong";
    const accepted = forms.flatMap(variants).map(norm);
    if (accepted.includes(n)) return "right";
    if (accepted.map(stripAccents).includes(stripAccents(n))) return "almost";
    return "wrong";
  }
  // Syllable nuclei for stress questions. Returns null when glides make the count ambiguous.
  const VOWELS = "αεηιουωάέήίόύώϊϋΐΰ";
  function syllables(word) {
    const w = word.toLowerCase();
    // Skip words where ι/υ (alone or in ει, οι, αι) meets a following vowel: often a glide (άδειος, δουλειά).
    if (/[ιυ][αεηιοω]/.test(stripAccents(w).replace(/[αεη]υ/g, "·v").replace(/ου/g, "·u"))) return null;
    const nuclei = [];
    for (let i = 0; i < w.length; i++) {
      const c = w[i];
      if (!VOWELS.includes(c)) continue;
      const prev = w[i - 1], pair = (prev || "") + stripAccents(c);
      const isSecond = prev && "αεοηυ".includes(prev) && ["αι", "ει", "οι", "υι", "ου", "αυ", "ευ", "ηυ"].includes(pair) && !"ϊϋΐΰ".includes(c);
      if (isSecond) nuclei[nuclei.length - 1] += c; else nuclei.push(c);
    }
    return nuclei;
  }
  function stressFromEnd(word) {
    const n = syllables(word);
    if (!n || n.length < 2) return null;
    const idx = n.findIndex((s) => /[άέήίόύώΐΰ]/.test(s));
    if (idx < 0) return null;
    return n.length - idx; // 1 = last syllable
  }
  // Vowel nuclei with their positions. An unaccented ι/υ before another vowel counts as a glide (παιδιού, κλειδιά).
  function spansG(word) {
    const w = word.toLowerCase(), spans = [];
    for (let i = 0; i < w.length; i++) {
      const c = w[i];
      if (!VOWELS.includes(c)) continue;
      const prev = w[i - 1], pair = (prev || "") + stripAccents(c);
      if (prev && "αεοηυ".includes(prev) && ["αι", "ει", "οι", "υι", "ου", "αυ", "ευ", "ηυ"].includes(pair) && !"ϊϋΐΰ".includes(c)) { spans[spans.length - 1][1] = i; continue; }
      if ((c === "ι" || c === "υ") && w[i + 1] && VOWELS.includes(w[i + 1]) && !(c === "υ" && "αεη".includes(prev))) {
        const nxt = w[i + 1] + (w[i + 2] || "");
        if (!["ου", "ού"].includes(nxt) || true) continue;
      }
      spans.push([i, i]);
    }
    return spans;
  }
  const accentFromEnd = (w) => { const sp = spansG(w); const k = sp.findIndex(([a, b]) => /[άέήίόύώΐΰ]/.test(w.slice(a, b + 1))); return k < 0 ? 0 : sp.length - k; };
  function placeAccent(bare, fromEnd) {
    const spans = spansG(bare);
    if (spans.length < fromEnd) return null;
    if (spans.length === 1 || !fromEnd) return bare;
    const i = spans[spans.length - fromEnd][1];
    return bare.slice(0, i) + (ADD_ACC[bare[i]] || bare[i]) + bare.slice(i + 1);
  }
  // Build a form of word `wNom` by analogy with a model: model nominative + model form.
  // Copies the ending change and the stress position counted from the end. Returns null when unsafe.
  function derive(mNom, mForm, wNom) {
    if (!mForm || /[\s\/()]/.test(mForm)) return null;
    const a = stripAccents(mNom), b = stripAccents(wNom), f = stripAccents(mForm);
    let k = 0; while (k < Math.min(a.length, b.length) - 1 && a[a.length - 1 - k] === b[b.length - 1 - k]) k++;
    if (!k) return null;
    const stemM = a.slice(0, a.length - k), stemW = b.slice(0, b.length - k);
    if (!f.startsWith(stemM)) return null;
    if (accentFromEnd(mNom) !== accentFromEnd(wNom) || spansG(wNom).length < 2) return null;
    let bare = stemW + f.slice(stemM.length);
    bare = bare.replace(/ς(?=.)/g, "σ").replace(/σ$/, "ς");
    // A stressed ί/ύ before a vowel (περίοδος) is a full syllable, not a glide: keep it one in the bare form.
    const h = wNom.search(/[ίύ](?=[αεηιουω])/);
    if (h >= 0 && h < stemW.length) bare = bare.slice(0, h) + (bare[h] === "ι" ? "ϊ" : "ϋ") + bare.slice(h + 1);
    const out = placeAccent(bare, accentFromEnd(mForm));
    if (!out || h < 0 || h >= stemW.length) return out;
    return out.slice(0, h) + ({ "ΐ": "ί", "ΰ": "ύ", "ϊ": "ι", "ϋ": "υ" }[out[h]] || out[h]) + out.slice(h + 1);
  }
  // τη(ν), το(ν): keep the ν before a vowel or κ π τ ξ ψ γκ μπ ντ τσ τζ.
  const artFit = (a, word) => { const vs = variants(a); if (vs.length < 2) return vs[0]; const keep = /^([αεηιουωάέήίόύώκπτξψ]|γκ|μπ|ντ|τσ|τζ)/.test(word); return vs.find((v) => v.endsWith("ν") === keep) || vs[0]; };
  const simpleWord = (w) => typeof w === "string" && /^[α-ωάέήίόύώϊϋΐΰς]+$/.test(w);

  if (typeof window !== "undefined") window.__ellinika = { derive, syllables, stressFromEnd };

  /* ---------- exercise generators ---------- */
  // Each returns an array of items: {kind, prompt, big?, options?, answer, accept?, why?}
  const PERSONS = [["1sg", "εγώ"], ["2sg", "εσύ"], ["3sg", "αυτός / αυτή"], ["1pl", "εμείς"], ["2pl", "εσείς"], ["3pl", "αυτοί / αυτές"]];
  const CASE_EN = { nom: "nominative", acc: "accusative", gen: "genitive", voc: "vocative" };
  const NUM_EN = { sg: "singular", pl: "plural" };
  const GEN_EN = { m: "masculine", f: "feminine", n: "neuter" };

  const VOCAB_POS = new Set(["noun", "verb", "adjective", "adverb", "conjunction", "preposition"]);
  const simplePhrase = (w) => typeof w === "string" && /^[α-ωάέήίόύώϊϋΐΰςΑ-ΩΆΈΉΊΌΎΏ /()-]+$/.test(w);
  const vstore = () => progress.vocab || (progress.vocab = {});
  // Production interval grows ×2.5 per correct recall (×1.5 if only the accent was off); a miss starts over.
  // A word counts as known once its interval reaches KNOWN_DAYS.
  function vocabGrade(lemma, result, mode) {
    const vs = vstore(), now = Date.now();
    const v = vs[lemma] || (vs[lemma] = { ivl: 0, reps: 0, lapses: 0, rec: 0, seen: now });
    if (mode === "rec") { if (result === "right") v.rec++; if (!v.due) v.due = now + 10 * 6e4; }
    else if (result === "wrong") { v.lapses++; v.ivl = 0; v.due = now + 10 * 6e4; }
    else { v.reps++; v.ivl = v.ivl ? Math.round(v.ivl * (result === "almost" ? 1.5 : 2.5)) : 1; v.due = now + v.ivl * 864e5 - 4 * 36e5; v.last = now; }
    saveProgress(progress);
  }

  function mc(prompt, answer, distractors, extra = {}) {
    const opts = shuffle(uniq([answer, ...shuffle(distractors.filter((d) => d !== answer)).slice(0, (extra.nOpts || 4) - 1)]));
    return { kind: "Choose", prompt, options: opts, answer, ...extra };
  }

  const GENERATORS = {
    async "letter-sound"(spec) {
      const abc = await resolve("grammar/alphabet-phonology.json#alphabet");
      return sample(abc, spec.n).map((l) => mc("What sound does this letter make?", l.sound, abc.map((x) => x.sound),
        { big: `${l.upper} ${l.lower}`, why: `${l.upper} ${l.lower} is called ${l.name} [${l.name_ipa}].` }));
    },
    async "letter-name"(spec) {
      const abc = await resolve("grammar/alphabet-phonology.json#alphabet");
      return sample(abc, spec.n).map((l) => mc("What is this letter called?", l.name, abc.map((x) => x.name),
        { big: `${l.upper} ${l.lower}`, why: `${l.name} [${l.name_ipa}], sound: ${l.sound}.` }));
    },
    async "name-letter"(spec) {
      const abc = await resolve("grammar/alphabet-phonology.json#alphabet");
      return sample(abc, spec.n).map((l) => ({ kind: "Type", prompt: `Type the lower-case letter called **${l.name}**.`, answer: l.lower,
        accept: l.lower === "σ" ? ["σ", "ς"] : [l.lower], why: `${l.name} = ${l.upper} ${l.lower}` }));
    },
    async "digraph-sound"(spec) {
      const d = await resolve("grammar/alphabet-phonology.json#digraphs");
      const all = [...d.vowel, ...d.consonant].map((x) => ({ s: x.spelling, snd: x.sound }));
      return sample(all, spec.n).map((x) => mc("How is this letter pair pronounced?", x.snd, all.map((y) => y.snd), { big: x.s, why: `${x.s} = [${x.snd}]` }));
    },
    async "av-ev"(spec) {
      const lex = await lexicon();
      const d = await resolve("grammar/alphabet-phonology.json#digraphs");
      const voiceless = d.voiceless_triggers;
      const words = lex.filter((e) => simpleWord(e.lemma) && /(α|ε)(υ|ύ)/.test(e.lemma));
      return sample(words, spec.n).map((e) => {
        const m = e.lemma.match(/(α|ε)(υ|ύ)(.?)/);
        const base = m[1] === "α" ? "a" : "e";
        const next = m[3];
        const f = !next || voiceless.includes(next);
        const ans = `[${base}${f ? "f" : "v"}]`;
        return mc(`How is ${m[1]}υ pronounced in this word? (${e.gloss})`, ans, [`[${base}f]`, `[${base}v]`, `[${base}u]`],
          { big: e.lemma, nOpts: 3, why: next ? `It is followed by ${next}, which is ${f ? "voiceless, so υ = [f]" : "a vowel or voiced consonant, so υ = [v]"}. Whole word: ${e.translit}.` : `At the end of a word υ = [f].` });
      });
    },
    async "read-word"(spec) {
      const lex = await lexicon();
      const pool = lex.filter((e) => simpleWord(e.lemma) && e.translit && e.lemma.length >= 3 && e.rank <= (spec.maxRank || 1000));
      return sample(pool, spec.n).map((e) => {
        const near = pool.filter((x) => x !== e && Math.abs(x.translit.length - e.translit.length) <= 2 && x.translit[0] === e.translit[0]);
        const dist = (near.length >= 3 ? near : pool).map((x) => x.translit);
        return mc("Which reading is right?", e.translit, dist, { big: e.lemma, why: `${e.lemma} (${e.translit}): ${e.gloss}` });
      });
    },
    async "stress-syllable"(spec) {
      const lex = await lexicon();
      const names = { 1: "last syllable", 2: "second from last", 3: "third from last" };
      const pool = lex.filter((e) => simpleWord(e.lemma) && stressFromEnd(e.lemma));
      return sample(pool, spec.n).map((e) => {
        const k = stressFromEnd(e.lemma), syl = syllables(e.lemma);
        return mc("Which syllable carries the stress?", names[k], Object.values(names), { big: e.lemma, nOpts: 3,
          why: `${syl.length} vowel sounds (${syl.join(" · ")}); the accent sits on the ${names[k]}. ${e.translit}: ${e.gloss}.` });
      });
    },
    async "article-gender"(spec) {
      const lex = await lexicon();
      const art = { m: "ο", f: "η", n: "το" };
      const pool = lex.filter((e) => e.pos === "noun" && art[e.noun?.gender] && simpleWord(e.lemma) && !e.needs_review);
      return sample(pool, spec.n).map((e) => {
        const g = e.noun.gender, bare = stripAccents(e.lemma);
        const end = ["μα", "ος", "ας", "ης", "ες", "α", "η", "ο", "ι", "ς", "ν"].find((x) => bare.endsWith(x)) || bare.slice(-1);
        return mc(`Which article goes with this noun? (${e.gloss})`, art[g], ["ο", "η", "το"],
          { big: `___ ${e.lemma}`, nOpts: 3, why: `${art[g]} ${e.lemma}: ${GEN_EN[g]}, ending -${end}. ${e.example?.el ? "e.g. " + e.example.el : ""}` });
      });
    },
    async "article-form"(spec) {
      const def = await resolve("grammar/nouns-full.json#articles.definite");
      const items = [];
      for (const num of ["sg", "pl"]) for (const g of ["m", "f", "n"]) for (const c of ["nom", "acc", "gen"]) items.push({ num, g, c, form: def[num][g][c] });
      const forms = uniq(items.map((x) => x.form));
      return sample(items, spec.n).map((x) => {
        const same = items.filter((y) => y.form === x.form && y !== x).map((y) => `${GEN_EN[y.g]} ${CASE_EN[y.c]} ${NUM_EN[y.num]}`);
        return mc(`“the”: ${GEN_EN[x.g]} ${CASE_EN[x.c]} ${NUM_EN[x.num]}`, x.form, forms,
          { why: `${x.form}` + (same.length ? `, the same form as the ${same.slice(0, 3).join(", ")}.` : ".") });
      });
    },
    async "case-function"(spec) {
      const fns = (await resolve("grammar/noun-phrase.json#functions")).filter((f) => CASE_EN[f.case]);
      return sample(fns, spec.n).map((f) => mc(`Which case does Greek use for the **${f.function}**?`, CASE_EN[f.case], Object.values(CASE_EN),
        { why: `${f.el} (${f.en})${f.note ? " " + f.note : ""}` }));
    },
    async "paradigm-cell"(spec) {
      // spec.src points at a noun paradigm {sg:{nom..}, pl:{..}} or a verb tense {1sg..3pl}
      const p = await resolve(spec.src);
      const cells = [];
      if (p.sg) for (const num of ["sg", "pl"]) for (const c of spec.cases || ["nom", "acc", "gen"]) cells.push({ label: `${CASE_EN[c]} ${NUM_EN[num]}`, form: p[num][c] });
      else for (const [k, pro] of PERSONS) if (p[k]) cells.push({ label: `${pro} (${k})`, form: p[k] });
      return sample(cells, spec.n).map((c) => ({ kind: "Type", prompt: `**${spec.lemma}**: ${c.label}`, answer: c.form, accept: [c.form], why: `${c.label}: ${c.form}` }));
    },
    async "paradigm-fill"(spec) {
      const p = await resolve(spec.src);
      const rows = [];
      if (p.sg) for (const num of ["sg", "pl"]) for (const c of spec.cases || ["nom", "acc", "gen"]) rows.push({ label: `${c} ${num}`, form: p[num][c] });
      else for (const [k, pro] of PERSONS) if (p[k]) rows.push({ label: pro, form: p[k] });
      const given = spec.given ?? 1;
      return [{ kind: "Fill the table", prompt: spec.prompt || `Write out **${spec.lemma}**.`, fill: rows.map((r, i) => ({ ...r, given: i < given })), answer: rows.map((r) => r.form).join(", "), why: spec.why }];
    },
    async "decline-like"(spec) {
      // Regular -ος masculines with fixed stress, built from the model's endings.
      const p = await resolve(spec.src);
      const end = { sg: { nom: "ος", acc: "ο", gen: "ου", voc: "ε" }, pl: { nom: "οι", acc: "ους", gen: "ων", voc: "οι" } };
      const words = (p.examples || []).map((w) => w.split("/")[0].trim()).filter((w) => simpleWord(w) && /(ος|ός)$/.test(w) && stressFromEnd(w) <= 2);
      const out = [];
      for (const w of sample(words, spec.n)) {
        const finalStress = w.endsWith("ός");
        const stem = w.slice(0, -2);
        const num = pick(["sg", "pl"]), c = pick(spec.cases || ["acc", "gen"]);
        let e = end[num][c];
        if (finalStress) e = e.replace(/^(ο|ε)(υ|ι)?/, (m0, v, d) => (d ? v + ADD_ACC[d] : ADD_ACC[v]));
        const form = stem + e;
        out.push({ kind: "Type", prompt: `Decline like **${p.model}**: ${w}, ${CASE_EN[c]} ${NUM_EN[num]}`, answer: form, accept: [form],
          why: `${w} → ${form}. The stress ${finalStress ? "stays on the ending" : "stays on the same syllable"}, as in ${p.model} → ${p[num][c]}.` });
      }
      return out;
    },
    async "conjugate-present"(spec) {
      // First-conjugation verbs: consonant stem + -ω, stress on the stem.
      const lex = await lexicon();
      const ends = { "1sg": "ω", "2sg": "εις", "3sg": "ει", "1pl": "ουμε", "2pl": "ετε", "3pl": "ουν" };
      const skip = new Set(spec.skip || []);
      const pool = lex.filter((e) => e.pos === "verb" && e.verb?.conj_group === "A" && /^[α-ωάέήίόύώ]+[^αεηιουωάέήίόύώ]ω$/.test(e.lemma) && /[άέήίόύώ]/.test(e.lemma) && !skip.has(e.lemma));
      return sample(pool, spec.n).map((e) => {
        const [k, pro] = pick(PERSONS);
        const stem = e.lemma.slice(0, -1), form = stem + ends[k];
        return { kind: "Type", prompt: `**${e.lemma}** (${e.gloss.replace(/^to /, "")}): ${pro} ___`, answer: form, accept: k === "3pl" ? [form, form + "ε"] : [form],
          why: `Stem ${stem}- + -${ends[k]} → ${form}${k === "3pl" ? " (or " + form + "ε in speech)" : ""}.` };
      });
    },
    async "decline"(spec) {
      // Nouns by analogy with Holton's model paradigms; see derive().
      const ps = (await resolve("grammar/nouns-full.json#paradigms")).filter((p) => !spec.ids || spec.ids.includes(p.id));
      const def = await resolve("grammar/nouns-full.json#articles.definite");
      const cells = (spec.cells || ["sg.acc", "sg.gen", "pl.nom", "pl.acc", "pl.gen"]).map((c) => c.split("."));
      const pool = [];
      for (const p of ps) {
        const g = { m: "m", f: "f", n: "n", "m/f": "m" }[p.gender];
        if (!g) continue;
        const words = uniq([p.model, ...(p.examples || []).map((w) => String(w).split(/[\/ (]/)[0])]).filter((w) => /^[α-ωάέήίόύώϊϋΐΰς]+$/.test(w));
        for (const w of words) {
          const forms = cells.map(([num, c]) => [num, c, derive(p.model, p[num]?.[c], w)]);
          if (forms.every((f) => f[2])) pool.push({ p, g, w, forms });
        }
      }
      const out = [];
      for (const e of sample(pool, spec.n)) {
        const [num, c, form] = pick(e.forms);
        const art = artFit(def[num][e.g][c], form), nomArt = variants(def.sg[e.g].nom)[0];
        out.push({ kind: "Decline", prompt: `**${nomArt} ${e.w}** (like ${e.p.model}): ${CASE_EN[c]} ${NUM_EN[num]}`, answer: `${art} ${form}`,
          accept: [form, ...variants(def[num][e.g][c]).map((a) => `${a} ${form}`)], why: `${e.p.model} → ${e.p[num][c]}, so ${e.w} → ${form}.${e.p.stress ? " " + e.p.stress : ""}`, tag: "decl" });
      }
      return out;
    },
    async "adj-agree"(spec) {
      // Adjectives keep the stress on the same syllable; endings follow the model.
      const ps = (await resolve("grammar/adjectives.json#paradigms")).filter((p) => !spec.ids || spec.ids.includes(p.model));
      const nouns = { m: ["ο άντρας", "τον φίλο", "του δρόμου", "οι μαθητές", "τους φίλους", "των δρόμων"], f: ["η πόλη", "τη γυναίκα", "της χώρας", "οι πόλεις", "τις γυναίκες", "των χωρών"], n: ["το σπίτι", "το παιδί", "του σπιτιού", "τα σπίτια", "τα παιδιά", "των σπιτιών"] };
      const slots = [["sg", "nom"], ["sg", "acc"], ["sg", "gen"], ["pl", "nom"], ["pl", "acc"], ["pl", "gen"]];
      const pool = [];
      for (const p of ps) {
        const words = uniq([p.model, ...(p.examples || []).map((w) => String(w).split(/[\/ (]/)[0])]).filter((w) => /^[α-ωάέήίόύώϊϋΐΰς]+$/.test(w));
        for (const w of words) if (!(spec.exclude || []).includes(w)) pool.push({ p, w });
      }
      const out = [];
      for (const e of sample(pool, spec.n * 2)) {
        if (out.length >= spec.n) break;
        const g = pick(["m", "f", "n"]), k = Math.floor(Math.random() * 6), [num, c] = slots[k];
        const mForm = e.p[num]?.[c]?.[g] ?? (g !== "n" ? e.p[num]?.[c]?.mf : undefined);
        if (!mForm || /[\/( ]/.test(mForm)) continue;
        const sIdx = (w) => spansG(w).findIndex(([x, y]) => /[άέήίόύώ]/.test(w.slice(x, y + 1)));
        if (sIdx(mForm) !== sIdx(e.p.model)) {
          // Stress moves in this cell (σύνηθες, επειγόντων): copy the position from the end, as for nouns.
          const form = derive(e.p.model, mForm, e.w);
          if (!form) continue;
          const [art, ...rest] = nouns[g][k].split(" ");
          out.push({ kind: "Agree", prompt: `Make **${e.w}** agree: ${art} ___ ${rest.join(" ")}`, answer: form, accept: [form],
            why: `${GEN_EN[g]} ${CASE_EN[c]} ${NUM_EN[num]}: ${art} ${form} ${rest.join(" ")} (model ${e.p.model} → ${mForm}; the stress moves here).`, tag: "decl" });
          continue;
        }
        const a = stripAccents(e.p.model), b = stripAccents(e.w);
        let kk = 0; while (kk < Math.min(a.length, b.length) - 1 && a[a.length - 1 - kk] === b[b.length - 1 - kk]) kk++;
        const stemM = a.slice(0, a.length - kk), f = stripAccents(mForm);
        if (!kk || !f.startsWith(stemM)) continue;
        let bare = b.slice(0, b.length - kk) + f.slice(stemM.length);
        bare = bare.replace(/ς(?=.)/g, "σ").replace(/σ$/, "ς");
        const sp = spansG(e.w), idx = sp.findIndex(([x, y]) => /[άέήίόύώ]/.test(e.w.slice(x, y + 1)));
        const spB = spansG(bare);
        if (idx < 0 || spB.length <= idx) continue;
        const i = spB[idx][1], form = bare.slice(0, i) + (ADD_ACC[bare[i]] || bare[i]) + bare.slice(i + 1);
        const [art, ...rest] = nouns[g][k].split(" ");
        out.push({ kind: "Agree", prompt: `Make **${e.w}** agree: ${art} ___ ${rest.join(" ")}`, answer: form, accept: [form],
          why: `${GEN_EN[g]} ${CASE_EN[c]} ${NUM_EN[num]}: ${art} ${form} ${rest.join(" ")} (model ${e.p.model} → ${mForm}). Adjectives keep the stress on the same syllable.`, tag: "decl" });
      }
      return out;
    },
    async "conjugate-2"(spec) {
      // Second-conjugation present: type A (αγαπώ) or B (θεωρώ).
      const sec = await resolve(`grammar/verbs-holton.json#sections[section=${spec.type === "B" ? "6.10" : "6.9"}]`);
      const list = (spec.type === "B" ? sec.verbs_type_B : sec.verbs_type_A).map((x) => { const m = x.match(/^(\S+)\s+'(.+)'$/); return m && { lemma: m[1], gloss: m[2] }; }).filter((x) => x && x.lemma.endsWith("ώ") && x.lemma.length > 2);
      const ends = spec.type === "B" ? { "1sg": "ώ", "2sg": "είς", "3sg": "εί", "1pl": "ούμε", "2pl": "είτε", "3pl": "ούν(ε)" } : { "1sg": "ώ/άω", "2sg": "άς", "3sg": "άει/ά", "1pl": "άμε/ούμε", "2pl": "άτε", "3pl": "ούν(ε)/άνε" };
      return sample(list, spec.n).map((v) => {
        const [k, pro] = pick(PERSONS), stem = v.lemma.slice(0, -1);
        const forms = ends[k].split("/").map((e) => stem + e);
        return { kind: "Type", prompt: `**${v.lemma}** (${v.gloss.replace(/^I /, "")}): ${pro} ___`, answer: forms.join(" / "), accept: forms,
          why: `Type ${spec.type || "A"}: ${stem}- + ${ends[k].split("/").map((e) => "-" + e).join(" or ")}. Stress always on the ending.` };
      });
    },
    async "review"(spec) {
      // Spaced review of earlier misses (stored per device).
      const now = Date.now(), due = (progress.review || []).filter((r) => r.due <= now && (!spec.tag || r.tag === spec.tag));
      return due.slice(0, spec.n).map((r) => ({ ...r.item, kind: "Review", reviewId: r.id }));
    },
    async "number-words"(spec) {
      // Numbers 1-9999 in words, counting (neuter) form or agreeing with a noun.
      const U = { n: ["", "ένα", "δύο|δυο", "τρία", "τέσσερα", "πέντε", "έξι", "επτά|εφτά", "οκτώ|οχτώ", "εννέα|εννιά"], m: ["", "ένας", "δύο|δυο", "τρεις", "τέσσερις"], f: ["", "μία|μια", "δύο|δυο", "τρεις", "τέσσερις"] };
      const TEEN = { n: ["δέκα", "έντεκα|ένδεκα", "δώδεκα", "δεκατρία", "δεκατέσσερα", "δεκαπέντε", "δεκαέξι|δεκάξι", "δεκαεπτά|δεκαεφτά", "δεκαοκτώ|δεκαοχτώ", "δεκαεννέα|δεκαεννιά"] };
      TEEN.m = TEEN.n.slice(); TEEN.m[3] = "δεκατρείς"; TEEN.m[4] = "δεκατέσσερις"; TEEN.f = TEEN.m;
      const TENS = ["", "", "είκοσι", "τριάντα", "σαράντα", "πενήντα", "εξήντα", "εβδομήντα", "ογδόντα", "ενενήντα"];
      const HUN = ["", "", "διακόσι", "τριακόσι|τρακόσι", "τετρακόσι", "πεντακόσι", "εξακόσι", "επτακόσι|εφτακόσι", "οκτακόσι|οχτακόσι", "εννιακόσι|εννεακόσι"];
      const HEND = { n: "α", m: "οι", f: "ες" };
      const unit = (d, g) => (U[g][d] || U.n[d]);
      function words(x, g) {
        const parts = [];
        const th = Math.floor(x / 1000), h = Math.floor((x % 1000) / 100), r = x % 100;
        if (th === 1) parts.push("χίλι" + HEND[g]); else if (th > 1) parts.push(...words(th, "f"), "χιλιάδες");
        if (h === 1) parts.push(r ? "εκατόν|εκατό" : "εκατό"); else if (h > 1) parts.push(HUN[h].split("|").map((s) => s + HEND[g]).join("|"));
        if (r >= 10 && r < 20) parts.push(TEEN[g][r - 10]);
        else { if (r >= 20) parts.push(TENS[Math.floor(r / 10)]); if (r % 10) parts.push(unit(r % 10, g)); }
        return parts;
      }
      const expand = (parts) => parts.reduce((acc, p) => acc.flatMap((a) => p.split("|").map((v) => (a ? a + " " : "") + v)), [""]);
      const nouns = { n: ["", "παιδιά", "σπίτια", "βιβλία"], m: ["άνθρωποι", "δρόμοι", "φίλοι"], f: ["γυναίκες", "μέρες", "σελίδες", "ώρες"] };
      const out = [];
      for (let i = 0; i < spec.n; i++) {
        const max = pick(spec.max || [20, 100, 1000, 10000]);
        const x = 1 + Math.floor(Math.random() * (max - 1)) + (max > 20 && Math.random() < 0.5 ? 0 : 0);
        const g = spec.genders ? pick(spec.genders) : "n";
        const noun = g === "n" ? pick(nouns.n) : pick(nouns[g]);
        if (x % 10 === 1 && x !== 11 && noun && g !== "n") continue;
        const forms = expand(words(x, g));
        out.push({ kind: "Type", prompt: noun ? `Write in words: **${x}** ${noun}` : `Write in words (counting form): **${x}**`, answer: forms[0], accept: forms,
          why: `${x} = ${forms[0]}${forms.length > 1 ? ` (also ${forms.slice(1, 3).join(", ")})` : ""}.${g !== "n" ? ` 1, 3, 4 and the hundreds agree with a ${GEN_EN[g]} noun.` : ""}` });
      }
      return out;
    },
    async "prep-blank"(spec) {
      // Example sentences from Holton §8.2 with the preposition blanked out.
      const preps = await resolve("grammar/prepositions.json#sections[section=8.2].prepositions");
      const main = preps.filter((p) => !spec.only || spec.only.includes(p.preposition.split(" ")[0]));
      const names = main.map((p) => p.preposition.split(" ")[0]);
      const pool = [];
      for (const p of main) {
        const w = p.preposition.split(" ")[0];
        for (const u of p.uses) for (const ex of u.examples || []) {
          const forms = w === "σε" ? ["στον", "στην", "στη", "στο", "στους", "στις", "στα", "σε"] : w === "από" ? ["από", "απ'"] : [w];
          const re = new RegExp(`(^|[\\s(])(${forms.join("|")})(?=[\\s,.;!])`, "i");
          const m = ex.el.match(re);
          if (m) pool.push({ p: w, gloss: u.meaning, el: ex.el.replace(re, `$1___`), full: ex.el, en: ex.en, hit: m[2] });
        }
      }
      return sample(pool, spec.n).map((x) => mc(`${x.el} · *${x.en}*`, x.p === "σε" ? x.hit.toLowerCase() : x.p, x.p === "σε" ? [...names.filter((n) => n !== "σε"), "σε", "στο", "στη", "στον"] : names, { why: `${x.full}: ${x.p} = ${x.gloss}.${x.p === "σε" && x.hit !== "σε" ? ` σε fuses with the article: ${x.hit}.` : ""}` }));
    },
    async "principal-parts"(spec) {
      // Present → simple past or future (dependent) from Poulopoulou's 99 verbs or Holton's irregular table.
      let rows;
      if (spec.source === "irregular") rows = (await resolve("grammar/verbs-holton.json"))["irregular_verbs_6.25"].verbs.filter((v) => v.active_simple_past).map((v) => ({ present: v.present, gloss: v.meaning, aorist: v.active_simple_past, future: v.dependent }));
      else rows = (await resolve("grammar/verbs-past-future.json#principal_parts")).map((v) => ({ present: v.present, gloss: v.gloss, aorist: v.aorist_1sg, future: v.future_1sg, group: v.past_group }));
      const part = spec.part || "aorist";
      rows = rows.filter((r) => r[part] && !/only|impers/.test(r[part]) && (!spec.irregularOnly || r.group));
      return sample(rows, spec.n).map((r) => {
        const accept = r[part].split(/\s*\/\s*/).flatMap((x) => [x.replace(/\s*\(.*?\)\s*/g, "").trim(), (x.match(/\((.*?)\)/) || [])[1]]).filter(Boolean);
        return { kind: "Type", prompt: `**${r.present}** (${r.gloss.replace(/^to /, "")}): ${part === "aorist" ? "εγώ ___ (simple past)" : "εγώ θα ___ (perfective)"}`, answer: r[part], accept: accept.map((a) => a.replace(/^θα\s+/, "")),
          why: `${r.present} → ${part === "aorist" ? r.aorist : "θα " + r.future}${/irregular/.test(r.group || "") ? " (irregular: learn it as a pair)" : ""}.` , tag: "verb" };
      });
    },
    async "aorist-person"(spec) {
      const rows = (await resolve("grammar/verbs-past-future.json#principal_parts")).filter((v) => /^[α-ωάέήίόύώ]+α$/.test(v.aorist_1sg || ""));
      const ends = { "1sg": "α", "2sg": "ες", "3sg": "ε", "1pl": "αμε", "2pl": "ατε", "3pl": "αν" };
      const out = [];
      for (const v of sample(rows, spec.n)) {
        const [k, pro] = pick(PERSONS), aor = v.aorist_1sg, pres = stripAccents(v.present.split(/[ /]/)[0]);
        const stem = stripAccents(aor).slice(0, -1), fixed = v.past_group === "irregular_1";
        const aug = /^ε/.test(stem) && !/^ε/.test(pres) && !fixed;
        const sp = spansG(aor), idx = sp.findIndex(([a, b]) => /[άέήίόύώ]/.test(aor.slice(a, b + 1)));
        const atIndex = (bare, i) => { const s2 = spansG(bare); const j = s2[i][1]; return bare.slice(0, j) + (ADD_ACC[bare[j]] || bare[j]) + bare.slice(j + 1); };
        let form;
        if (fixed) form = atIndex(stem + ends[k], idx);
        else if (k === "1pl" || k === "2pl") form = placeAccent((aug ? stem.slice(1) : stem) + ends[k], 3);
        else form = atIndex(stem + ends[k], idx);
        const accept = [form];
        if (k === "3pl" && !fixed) accept.push(placeAccent((aug ? stem.slice(1) : stem) + "ανε", 3));
        if (k === "3pl" && fixed) accept.push(atIndex(stem + "ανε", idx));
        out.push({ kind: "Type", prompt: `**${v.present}** → ${aor}: ${pro} ___ (simple past)`, answer: form, accept,
          why: fixed ? `${aor} keeps its stress throughout: ${form}.` : `Stress on the third syllable from the end${aug ? "; the augment ε- appears only when it is needed to carry the stress" : ""}: ${form}.`, tag: "verb" });
      }
      return out;
    },
    async "imperfect"(spec) {
      const out = [];
      const ends = { "1sg": "α", "2sg": "ες", "3sg": "ε", "1pl": "αμε", "2pl": "ατε", "3pl": "αν" };
      if (spec.conj === 2) {
        const secA = await resolve("grammar/verbs-holton.json#sections[section=6.9]"), secB = await resolve("grammar/verbs-holton.json#sections[section=6.10]");
        const list = [...secA.verbs_type_A, ...secB.verbs_type_B].map((x) => x.match(/^(\S+)\s+'(.+)'$/)).filter((m) => m && m[1].endsWith("ώ") && m[1].length > 2);
        for (const m of sample(list, spec.n)) {
          const [k, pro] = pick(PERSONS), stem = m[1].slice(0, -1);
          const form = stem + { "1sg": "ούσα", "2sg": "ούσες", "3sg": "ούσε", "1pl": "ούσαμε", "2pl": "ούσατε", "3pl": "ούσαν" }[k];
          out.push({ kind: "Type", prompt: `**${m[1]}** (${m[2].replace(/^I /, "")}): ${pro} ___ (imperfect)`, answer: form, accept: k === "3pl" ? [form, form + "ε"] : [form], why: `Second conjugation: stem + stressed -ούσ- + past endings: ${form}.`, tag: "verb" });
        }
        return out;
      }
      const lex = await lexicon();
      const pool = lex.filter((e) => e.pos === "verb" && e.verb?.conj_group === "A" && /^[α-ωάέήίόύώ]+[^αεηιουωάέήίόύώ]ω$/.test(e.lemma) && !/^[αεηιουωάέήίόύώ]/.test(e.lemma) && !/imperf/.test(e.verb?.aorist_1sg || "") && !["έχω", "είμαι"].includes(e.lemma));
      for (const e of sample(pool, spec.n)) {
        const [k, pro] = pick(PERSONS), stem = stripAccents(e.lemma).slice(0, -1);
        const short = spansG(stem + "α").length < 3;
        const long = k === "1pl" || k === "2pl";
        let form = long ? placeAccent(stem + ends[k], 3) : placeAccent((short ? "ε" : "") + stem + ends[k], 3);
        if (!form) continue;
        const accept = [form];
        if (k === "3pl") accept.push(placeAccent(stem + "ανε", 3));
        out.push({ kind: "Type", prompt: `**${e.lemma}** (${e.gloss.replace(/^to /, "")}): ${pro} ___ (imperfect)`, answer: form, accept,
          why: `Present stem + past endings, stress on the third syllable from the end${short && !long ? "; the form is too short, so it takes the augment έ-" : ""}: ${form}.`, tag: "verb" });
      }
      return out;
    },
    async "future-person"(spec) {
      const rows = (await resolve("grammar/verbs-past-future.json#principal_parts")).map((v) => ({ ...v, fut: (v.future_1sg || "").split(/\s*\/\s*/)[0].replace(/\s*\(.*\)/, "") })).filter((v) => /^[α-ωάέήίόύώ]+ω$/.test(v.fut));
      const out = [];
      const particle = spec.particle || "θα";
      for (const v of sample(rows, spec.n)) {
        const [k, pro] = pick(PERSONS), f = v.fut, bare = stripAccents(f);
        let forms;
        if (bare.endsWith("αω")) { const st = bare.slice(0, -2); forms = { "1sg": [f], "2sg": [st + "ας"], "3sg": [placeAccent(st + "αει", 2)], "1pl": [placeAccent(st + "αμε", 2)], "2pl": [placeAccent(st + "ατε", 2)], "3pl": [placeAccent(st + "ανε", 2)] }; if (spansG(st + "ας").length > 1) forms["2sg"] = [placeAccent(st + "ας", 1)]; }
        else if (spansG(f).length === 1) { const st = bare.slice(0, -1); forms = { "1sg": [f], "2sg": [st + "εις"], "3sg": [st + "ει"], "1pl": [placeAccent(st + "ουμε", 2)], "2pl": [placeAccent(st + "ειτε", 2)], "3pl": [st + "ουν", placeAccent(st + "ουνε", 2)] }; }
        else if (/ώ$/.test(f)) { const st = bare.slice(0, -1); forms = { "1sg": [f], "2sg": [placeAccent(st + "εις", 1)], "3sg": [placeAccent(st + "ει", 1)], "1pl": [placeAccent(st + "ουμε", 2)], "2pl": [placeAccent(st + "ειτε", 2)], "3pl": [placeAccent(st + "ουν", 1), placeAccent(st + "ουνε", 2)] }; }
        else {
          const st = bare.slice(0, -1), sp = spansG(f), idx = sp.findIndex(([a, b]) => /[άέήίόύώ]/.test(f.slice(a, b + 1)));
          const at = (b) => { const s2 = spansG(b); const j = s2[idx][1]; return b.slice(0, j) + (ADD_ACC[b[j]] || b[j]) + b.slice(j + 1); };
          forms = { "1sg": [f], "2sg": [at(st + "εις")], "3sg": [at(st + "ει")], "1pl": [at(st + "ουμε")], "2pl": [at(st + "ετε")], "3pl": [at(st + "ουν"), at(st + "ουνε")] };
        }
        const list = forms[k];
        if (!list.every(Boolean)) continue;
        out.push({ kind: "Type", prompt: `**${v.present}** (${v.gloss.replace(/^to /, "")}): ${pro} ${particle} ___ (perfective)`, answer: list[0], accept: list.flatMap((x) => [x, `${particle} ${x}`]),
          why: `Perfective stem ${v.fut} + present endings: ${particle} ${list[0]}.`, tag: "verb" });
      }
      return out;
    },
    async "word-blank"(spec) {
      // Holton example sentences with one connective (from spec.words) blanked out.
      const lists = await Promise.all(spec.src.map(resolve));
      const pool = [];
      const words = spec.words.slice().sort((a, b) => b.length - a.length);
      for (const ex of lists.flat().filter((x) => x && x.el)) {
        for (const w of words) {
          const re = new RegExp(`(^|[\\s,(«])(${w.replace(/\s+/g, "\\s+")})(?=[\\s,.;!»])`, "i");
          const m = ex.el.match(re);
          if (m) { pool.push({ w, el: ex.el.replace(re, "$1___"), full: ex.el, en: ex.en }); break; }
        }
      }
      return sample(pool, spec.n).map((x) => mc(`${x.el} · *${x.en}*`, x.w, spec.distractors || spec.words, { why: x.full }));
    },
    async "passive-present"(spec) {
      const lex = await lexicon();
      const pool = lex.filter((e) => e.pos === "verb" && /^[α-ωάέήίόύώ]+ομαι$/.test(e.lemma) && /[άέήίόύώ]/.test(e.lemma.slice(0, -4)));
      const ends = { "1sg": "ομαι", "2sg": "εσαι", "3sg": "εται", "1pl": "ομαστε", "2pl": "εστε", "3pl": "ονται" };
      return sample(pool, spec.n).map((e) => {
        const [k, pro] = pick(PERSONS), stem = stripAccents(e.lemma).slice(0, -4);
        const sp = spansG(e.lemma), idx = sp.findIndex(([a, b]) => /[άέήίόύώ]/.test(e.lemma.slice(a, b + 1)));
        const at = (b) => { const s2 = spansG(b); const j = s2[idx][1]; return b.slice(0, j) + (ADD_ACC[b[j]] || b[j]) + b.slice(j + 1); };
        const form = k === "1pl" ? placeAccent(stem + ends[k], 3) : at(stem + ends[k]);
        const accept = k === "2pl" ? [form, placeAccent(stem + "οσαστε", 3)] : [form];
        return { kind: "Type", prompt: `**${e.lemma}** (${e.gloss.replace(/^to /, "")}): ${pro} ___`, answer: form, accept,
          why: `-ομαι, -εσαι, -εται, -όμαστε, -εστε (-όσαστε), -ονται${k === "1pl" ? "; the 1st plural moves the stress forward one syllable" : ""}: ${form}.`, tag: "verb" };
      });
    },
    async "passive-aorist"(spec) {
      const known = new Set((await lexicon()).map((e) => e.lemma));
      const rows = (await resolve("grammar/verbs-holton.json"))["irregular_verbs_6.25"].verbs.filter((v) => /^[α-ωάέήίόύώ]+ηκα$/.test(v.passive_simple_past || "") && (!spec.common || known.has(v.present)));
      const ends = { "1sg": "ηκα", "2sg": "ηκες", "3sg": "ηκε", "1pl": "ηκαμε", "2pl": "ηκατε", "3pl": "ηκαν" };
      return sample(rows, spec.n).map((v) => {
        const [k, pro] = pick(PERSONS), stem = stripAccents(v.passive_simple_past).slice(0, -3);
        const form = placeAccent(stem + ends[k], 3);
        return { kind: "Type", prompt: `**${v.present}** (${v.meaning}) → passive past ${v.passive_simple_past}: ${pro} ___`, answer: form, accept: k === "3pl" ? [form, placeAccent(stem + "ηκανε", 3)] : [form],
          why: `Passive stem + -ηκ- + past endings, stress on the third syllable from the end: ${form}.`, tag: "verb" };
      });
    },
    async "perfect"(spec) {
      const rows = (await resolve("grammar/verbs-past-future.json#principal_parts")).map((v) => ({ ...v, fut: (v.future_1sg || "").split(/\s*\/\s*/)[0].replace(/\s*\(.*\)/, "") })).filter((v) => /^[α-ωάέήίόύώ]+ω$/.test(v.fut) && !["έχω", "ξέρω", "θέλω"].includes(v.fut));
      const AUX = { perfect: ["έχω", "έχεις", "έχει", "έχουμε", "έχετε", "έχουν"], pluperfect: ["είχα", "είχες", "είχε", "είχαμε", "είχατε", "είχαν"] };
      const out = [];
      for (const v of sample(rows, spec.n)) {
        const f = v.fut, bare = stripAccents(f), st = bare.slice(0, -1);
        let nf;
        if (bare.endsWith("αω")) nf = placeAccent(bare.slice(0, -2) + "αει", 2);
        else if (spansG(f).length === 1) nf = st + "ει";
        else if (/ώ$/.test(f)) nf = placeAccent(st + "ει", 1);
        else { const sp = spansG(f), idx = sp.findIndex(([a, b]) => /[άέήίόύώ]/.test(f.slice(a, b + 1))); const s2 = spansG(st + "ει"); const j = s2[idx][1]; nf = (st + "ει").slice(0, j) + ADD_ACC[(st + "ει")[j]] + (st + "ει").slice(j + 1); }
        const tense = pick(spec.tenses || ["perfect", "pluperfect"]), i = Math.floor(Math.random() * 6);
        const form = `${AUX[tense][i]} ${nf}`;
        out.push({ kind: "Type", prompt: `**${v.present}** (${v.gloss.replace(/^to /, "")}): ${PERSONS[i][1]} ___ (${tense})`, answer: form, accept: [form],
          why: `${tense === "perfect" ? "έχω" : "είχα"} + the non-finite form (= 3sg of the perfective: θα ${nf}): ${form}.`, tag: "verb" });
      }
      return out;
    },
    async "irregular-part"(spec) {
      // Any column of Holton's irregular table (6.25): passive_simple_past, passive_dependent, passive_perfect_participle…
      const LABEL = { passive_simple_past: "passive simple past (εγώ)", passive_dependent: "passive dependent: θα ___", passive_perfect_participle: "participle in -μένος", active_simple_past: "simple past (εγώ)" };
      const known = new Set((await lexicon()).map((e) => e.lemma));
      const expand = (x) => { const m = x.match(/^(.*?)\((.*?)\)(.*)$/); return m ? [m[1] + m[3], m[1] + m[2] + m[3]] : [x]; };
      let rows = (await resolve("grammar/verbs-holton.json"))["irregular_verbs_6.25"].verbs.filter((v) => { const f = v[spec.field]; return f && !/^\(|\s/.test(f); });
      if (spec.common) rows = rows.filter((v) => known.has(v.present.split(/[\/ ]/)[0]) || (spec.also || []).includes(v.present));
      if (spec.only) rows = rows.filter((v) => spec.only.includes(v.present));
      return sample(rows, spec.n).map((v) => {
        const accept = v[spec.field].split("/").flatMap(expand);
        return { kind: "Type", prompt: `**${v.present}** (${v.meaning}): ${LABEL[spec.field] || spec.field}`, answer: v[spec.field], accept,
          why: `${v.present} → ${v[spec.field]}${v.passive_simple_past && spec.field !== "passive_simple_past" ? ` (passive past ${v.passive_simple_past})` : ""}.`, tag: "verb" };
      });
    },
    async "participle-agree"(spec) {
      // -μένος participles decline like ψηλός; the stress never leaves -μέ-.
      const END = { m: { "sg.nom": "ος", "sg.acc": "ο", "sg.gen": "ου", "pl.nom": "οι", "pl.acc": "ους", "pl.gen": "ων" }, f: { "sg.nom": "η", "sg.acc": "η", "sg.gen": "ης", "pl.nom": "ες", "pl.acc": "ες", "pl.gen": "ων" }, n: { "sg.nom": "ο", "sg.acc": "ο", "sg.gen": "ου", "pl.nom": "α", "pl.acc": "α", "pl.gen": "ων" } };
      const NOUN = { m: { "sg.nom": "ο φάκελος", "sg.acc": "τον φάκελο", "sg.gen": "του φακέλου", "pl.nom": "οι φάκελοι", "pl.acc": "τους φακέλους", "pl.gen": "των φακέλων" }, f: { "sg.nom": "η πόρτα", "sg.acc": "την πόρτα", "sg.gen": "της πόρτας", "pl.nom": "οι πόρτες", "pl.acc": "τις πόρτες", "pl.gen": "των πορτών" }, n: { "sg.nom": "το γράμμα", "sg.acc": "το γράμμα", "sg.gen": "του γράμματος", "pl.nom": "τα γράμματα", "pl.acc": "τα γράμματα", "pl.gen": "των γραμμάτων" } };
      const words = spec.words.map((w) => { const m = w.match(/^(\S+)\s*(?:'(.+)')?/); return { w: m[1], en: m[2] || "" }; });
      return sample(words, spec.n).map(({ w, en }) => {
        const g = pick(["m", "f", "n"]), slot = pick(Object.keys(END.m)), form = w.slice(0, -2) + END[g][slot];
        const [art, ...rest] = NOUN[g][slot].split(" ");
        const [num, c] = slot.split(".");
        return { kind: "Agree", prompt: `Make **${w}**${en ? ` (${en})` : ""} agree: ${art} ___ ${rest.join(" ")}`, answer: form, accept: [form],
          why: `${GEN_EN[g]} ${CASE_EN[c]} ${NUM_EN[num]}: ${art} ${form} ${rest.join(" ")}. -μένος, -μένη, -μένο decline like ψηλός and the stress stays on -μέ-.`, tag: "decl" };
      });
    },
    async "gerund"(spec) {
      // 1st conjugation -οντας (stress on the syllable before), 2nd conjugation -ώντας.
      const IRR = { "λέω": "λέγοντας", "τρώω": "τρώγοντας", "πάω": "πηγαίνοντας", "ακούω": "ακούγοντας", "κλαίω": "κλαίγοντας", "φταίω": "φταίγοντας", "καίω": "καίγοντας", "έχω": "έχοντας", "είμαι": "όντας", "ζω": "ζώντας", "βγαίνω": "βγαίνοντας", "επενδύω": "επενδύοντας" };
      const lex = (await lexicon()).filter((e) => e.pos === "verb" && /^[α-ωάέήίόύώ]+[ωώ]$/.test(e.lemma) && !/άω$/.test(e.lemma) && !["αρέσω", "συμβαίνω", "ανήκω", "χρησιμεύω", "πρόκειται"].includes(e.lemma));
      return sample(lex, spec.n).map((e) => {
        const v = e.lemma, bare = stripAccents(v);
        let form = IRR[v];
        if (!form) form = /ώ$/.test(v) ? bare.slice(0, -1) + "ώντας" : placeAccent(bare.slice(0, -1) + "οντας", 3);
        return { kind: "Type", prompt: `Gerund of **${v}** (${e.gloss.split(";")[0].replace(/^to /, "")})`, answer: form, accept: [form],
          why: IRR[v] ? `${v} → ${form} (irregular).` : /ώ$/.test(v) ? `Stressed -ώ verbs take -ώντας: ${form}.` : `-ω verbs take -οντας with the stress just before it: ${form}.`, tag: "verb" };
      });
    },
    async "vocab-recall"(spec) {
      // Spaced English → Greek recall. New words are met once as a recognition question, then produced.
      const lex = (await lexicon()).filter((e) => VOCAB_POS.has(e.pos) && e.gloss && simplePhrase(e.lemma));
      const byL = new Map(lex.map((e) => [e.lemma, e]));
      const vs = vstore(), now = Date.now();
      const due = Object.entries(vs).filter(([l, v]) => v.due && v.due <= now && byL.has(l)).sort((a, b) => a[1].due - b[1].due).map(([l]) => byL.get(l)).slice(0, spec.n ?? 8);
      const ordered = lex.slice().sort((a, b) => (a.rank || 1e5) - (b.rank || 1e5)).map((e) => e.lemma);
      const fresh = uniq([...(spec.words || []), ...ordered]).filter((l) => byL.has(l) && !vs[l]).slice(0, spec.new ?? 4).map((l) => byL.get(l));
      const ART = { m: "ο", f: "η", n: "το" };
      const withArt = (e) => (e.pos === "noun" && ART[e.noun?.gender] ? `${ART[e.noun.gender]} ${e.lemma}` : e.lemma);
      const ex = (e) => (e.example?.el ? `${e.example.el} · *${e.example.en || ""}*` : "");
      const rec = fresh.map((e) => mc("What does it mean?", e.gloss, lex.filter((x) => x.pos === e.pos && x !== e).map((x) => x.gloss), { kind: "New word", big: withArt(e), why: ex(e), vocab: { lemma: e.lemma, mode: "rec" } }));
      const prod = [...due, ...fresh].map((e) => {
        const same = lex.filter((x) => x.gloss === e.gloss).map((x) => x.lemma);
        const accept = uniq([e.lemma, withArt(e), ...same, ...String(e.lemma).split(/\s*\/\s*/)]);
        const hint = { noun: "noun", verb: "verb", adjective: "adjective", adverb: "adverb", conjunction: "conjunction", preposition: "preposition" }[e.pos];
        return { kind: "Say it in Greek", prompt: `**${e.gloss}** (${hint})`, answer: withArt(e), accept, why: ex(e), vocab: { lemma: e.lemma, mode: "prod" } };
      });
      // "Use it": words already in recall come back inside a common collocation; the learner writes the words around the headword.
      const col = await collocs();
      const use = [];
      for (const l of sample(Object.keys(vs).filter((l) => vs[l].ivl > 0 && col[l]), 12)) {
        if (use.length >= (spec.use ?? 2)) break;
        const c = sample((col[l].collocations || []).filter((x) => x.el.startsWith(l + " ") && !/[\/+()…]|\.\.\./.test(x.el)), 1)[0];
        if (!c) continue;
        const rest = c.el.slice(l.length + 1);
        use.push({ kind: "Use it", prompt: `**${c.en}**`, big: `${l} ___`, answer: rest, accept: [rest], why: c.el });
      }
      return [...rec, ...prod, ...use];
    },
    async "reading-q"(spec) {
      return spec.questions.map((q) => mc(q.prompt, q.answer, q.options, { kind: "Comprehension", why: q.why, nOpts: q.options.length, comp: true }));
    },
    async "mc"(spec) {
      return (spec.n ? sample(spec.items, spec.n) : spec.items).map((q) => mc(q.prompt, q.answer, q.options, { big: q.big, why: q.why, nOpts: q.options.length }));
    },
    async "type"(spec) {
      return (spec.n ? sample(spec.items, spec.n) : spec.items).map((q) => ({ kind: "Type", prompt: q.prompt, big: q.big, answer: q.answer, accept: q.accept || [q.answer], why: q.why }));
    },
  };

  if (typeof window !== "undefined") window.__ellinika.GENERATORS = GENERATORS;

  /* ---------- Learn-tab block renderers ---------- */
  const BLOCKS = {
    async text(b) { return `${b.title ? `<h3>${esc(b.title)}</h3>` : ""}${paras(b.text)}`; },
    async callout(b) { return `<div class="callout">${paras(b.text)}</div>`; },
    async culture(b) { return `<div class="culture"><span class="eyebrow">ΠΟΛΙΤΙΣΜΟΣ · culture</span>${b.title ? `<h3>${esc(b.title)}</h3>` : ""}${paras(b.text)}</div>`; },
    async reading(b) {
      Object.assign(lookCtx, b.gloss || {});
      return `<div class="reading"><span class="eyebrow">ΑΝΑΓΝΩΣΗ · reading</span><h3 lang="el">${esc(b.title)}</h3><div class="rd-text" lang="el">${paras(b.text)}</div>${b.en ? `<details class="rd-en no-look"><summary>English</summary>${paras(b.en)}</details>` : ""}</div>`;
    },
    async video(b) { Object.assign(lookCtx, b.gloss || {}); return videoHTML(b); },
    async rules(b) {
      let list = b.items || (await resolve(b.src));
      if (typeof list === "string") list = [list];
      if (b.pick) list = b.pick.map((i) => list[i]).filter(Boolean);
      return `${b.title ? `<h3>${esc(b.title)}</h3>` : ""}<ul>${list.map((r) => `<li>${ruleItem(r)}</li>`).join("")}</ul>${srcNote(b)}`;
    },
    async examples(b) {
      let list = b.items || (await resolve(b.src));
      if (b.limit) list = list.slice(0, b.limit);
      return `${b.title ? `<h3>${esc(b.title)}</h3>` : ""}<ul class="ex-list">${list.map((x) => `<li><span class="ex-el" lang="el">${esc(x.el)}${x.ipa ? ` <span class="ipa">[${esc(x.ipa)}]</span>` : ""}</span><span class="ex-en">${esc(x.en || x.use || x.function || "")}</span></li>`).join("")}</ul>${srcNote(b)}`;
    },
    async table(b) {
      return `${b.title ? `<h3>${esc(b.title)}</h3>` : ""}<div class="tbl-wrap"><table${b.head.length >= 3 ? ' class="stack"' : ""}><thead><tr>${b.head.map((h) => `<th>${esc(h)}</th>`).join("")}</tr></thead><tbody>${b.rows.map((r) => `<tr>${r.map((c, i) => `<td${i === 0 && b.bigFirst ? ' class="big"' : ""} data-h="${esc(b.head[i] || "")}">${md(c)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>${srcNote(b)}`;
    },
    async alphabet(b) {
      const abc = await resolve("grammar/alphabet-phonology.json#alphabet");
      return `<div class="tbl-wrap"><table><thead><tr><th>Letter</th><th>Name</th><th>Sound</th></tr></thead><tbody>${abc.map((l) => `<tr><td class="big" lang="el">${l.upper} ${l.lower}</td><td lang="el">${l.name} <span class="ipa">[${esc(l.name_ipa)}]</span></td><td>${esc(l.sound)}</td></tr>`).join("")}</tbody></table></div>${srcNote({ src: "Holton §1.1" })}`;
    },
    async digraphs(b) {
      const d = await resolve("grammar/alphabet-phonology.json#digraphs");
      const rows = [...d.vowel.map((x) => [x.spelling, x.sound, ""]), ...d.consonant.map((x) => [x.spelling, x.sound, x.word_internal ? `inside a word: ${x.word_internal}` : (x.examples || []).map((e) => e.el).join(", ")])];
      const vu = d.vowel_plus_upsilon.map((x) => [x.spelling, `${x.before_vowel_or_voiced} / ${x.before_voiceless_or_final}`, (x.examples || []).map((e) => `${e.el} [${e.ipa}]`).join(", ") || x.note || ""]);
      return `<div class="tbl-wrap"><table><thead><tr><th>Spelling</th><th>Sound</th><th>Notes</th></tr></thead><tbody>${[...rows, ...vu].map((r) => `<tr><td class="big" lang="el">${esc(r[0])}</td><td>[${esc(r[1])}]</td><td>${esc(r[2])}</td></tr>`).join("")}</tbody></table></div><p class="sub">${esc(d.double_consonants)}</p>`;
    },
    async article(b) {
      const a = await resolve(b.src || "grammar/nouns-full.json#articles.definite");
      const cases = b.cases || ["nom", "acc", "gen"];
      const rows = [];
      for (const num of ["sg", "pl"]) for (const c of cases) rows.push([`${c} ${num}`, a[num].m[c], a[num].f[c], a[num].n[c]]);
      return `${b.title ? `<h3>${esc(b.title)}</h3>` : ""}<div class="tbl-wrap"><table><thead><tr><th></th><th>masc.</th><th>fem.</th><th>neut.</th></tr></thead><tbody>${rows.map((r) => `<tr><th>${r[0]}</th>${r.slice(1).map((c) => `<td class="big" lang="el">${esc(c)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>${srcNote(b)}`;
    },
    async "noun-paradigm"(b) {
      const ps = await Promise.all(b.src.map(resolve));
      const cases = b.cases || ["nom", "acc", "gen", "voc"];
      const rows = [];
      for (const num of ["sg", "pl"]) for (const c of cases) rows.push([`${c} ${num}`, ...ps.map((p) => p[num][c])]);
      return `${b.title ? `<h3>${esc(b.title)}</h3>` : ""}<div class="tbl-wrap"><table><thead><tr><th></th>${ps.map((p) => `<th lang="el">${esc(p.model)}<br><span class="ipa">${esc(p.gloss)}</span></th>`).join("")}</tr></thead><tbody>${rows.map((r) => `<tr><th>${r[0]}</th>${r.slice(1).map((c) => `<td class="big" lang="el">${esc(c)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>${ps.map((p) => p.stress ? `<p class="sub"><strong lang="el">${esc(p.model)}</strong>: ${esc(p.stress)}</p>` : "").join("")}${srcNote(b)}`;
    },
    async "verb-paradigm"(b) {
      const cols = await Promise.all(b.columns.map((c) => resolve(c.src)));
      return `${b.title ? `<h3>${esc(b.title)}</h3>` : ""}<div class="tbl-wrap"><table><thead><tr><th></th>${b.columns.map((c) => `<th>${esc(c.label)}</th>`).join("")}</tr></thead><tbody>${PERSONS.map(([k, pro]) => `<tr><th lang="el">${pro}</th>${cols.map((p) => `<td class="big" lang="el">${esc(p[k])}</td>`).join("")}</tr>`).join("")}</tbody></table></div>${srcNote(b)}`;
    },
    async uses(b) {
      const list = (await resolve(b.src)).slice(0, b.limit || 10);
      return `${b.title ? `<h3>${esc(b.title)}</h3>` : ""}<ul class="ex-list">${list.map((u) => `<li><span class="ex-en"><strong>${esc(u.use || u.meaning || "")}</strong></span>${(u.examples || (u.el ? [u] : [])).slice(0, b.per || 2).map((x) => `<span class="ex-el" lang="el">${esc(x.el)}</span><span class="ex-en">${esc(x.en)}</span>`).join("")}</li>`).join("")}</ul>${srcNote(b)}`;
    },
    async prep(b) {
      const preps = await resolve("grammar/prepositions.json#sections[section=8.2].prepositions");
      const list = preps.filter((p) => b.only.includes(p.preposition.split(" ")[0]));
      return list.map((p) => `<h3 lang="el">${esc(p.preposition)} <span class="ipa">+ ${esc(p.case)}</span></h3><p class="sub">${esc(p.gloss)}${p.colloquial_form ? ` · ${esc(p.colloquial_form)}` : ""}</p><ul class="ex-list">${p.uses.slice(0, b.limit || 8).map((u) => `<li><span class="ex-en"><strong>${esc(u.meaning)}</strong></span>${(u.examples || []).slice(0, 2).map((x) => `<span class="ex-el" lang="el">${esc(x.el)}</span><span class="ex-en">${esc(x.en)}</span>`).join("")}</li>`).join("")}</ul>`).join("");
    },
    async vocab(b) {
      const lex = await lexicon();
      let list;
      if (b.words) list = b.words.map((w) => lex.find((e) => e.lemma === w)).filter(Boolean);
      else list = lex.filter((e) => new RegExp(b.match).test(e.lemma) && (!b.pos || e.pos === b.pos) && (!b.gender || e.noun?.gender === b.gender)).slice(0, b.limit || 24);
      return `${b.title ? `<h3>${esc(b.title)}</h3>` : ""}<div class="vocab">${list.map((e) => `<div><span class="ex-el" lang="el">${b.article && e.noun ? { m: "ο ", f: "η ", n: "το " }[e.noun.gender] || "" : ""}${esc(e.lemma)}</span><span class="ex-en">${esc(e.gloss)}</span></div>`).join("")}</div>`;
    },
  };
  const srcNote = () => ""; // source citations are kept in the lesson JSON (cite) but not shown

  /* ---------- horizontal pages ---------- */
  const pagerNav = () => `<div class="pager-nav"><button class="btn ghost small" data-dir="-1" aria-label="Previous page">‹ Back</button><div class="dots"></div><button class="btn ghost small" data-dir="1" aria-label="Next page">Next ›</button></div>`;
  function pager(wrap, onChange) {
    const track = wrap.querySelector(".pager"), pages = [...track.children];
    const dots = wrap.querySelector(".dots"), prev = wrap.querySelector('[data-dir="-1"]'), next = wrap.querySelector('[data-dir="1"]');
    dots.innerHTML = pages.map((_, i) => `<button aria-label="Page ${i + 1}"></button>`).join("");
    let cur = -1;
    const set = (i) => {
      if (i === cur) return; cur = i;
      [...dots.children].forEach((d, k) => d.setAttribute("aria-current", k === i));
      prev.disabled = i === 0; next.disabled = i === pages.length - 1;
      onChange && onChange(i);
    };
    const go = (i, instant) => {
      i = Math.max(0, Math.min(pages.length - 1, i));
      track.scrollTo({ left: pages[i].offsetLeft - track.offsetLeft, behavior: instant ? "auto" : "smooth" });
      set(i);
      const top = wrap.getBoundingClientRect().top;
      if (!instant && top < 0) window.scrollBy({ top: top - 70, behavior: "smooth" });
    };
    let t;
    track.addEventListener("scroll", () => { clearTimeout(t); t = setTimeout(() => set(Math.round(track.scrollLeft / track.clientWidth)), 60); });
    prev.onclick = () => go(cur - 1); next.onclick = () => go(cur + 1);
    [...dots.children].forEach((d, k) => (d.onclick = () => go(k)));
    set(0);
    return { go };
  }

  /* ---------- photos (img/manifest.json, optional) ---------- */
  let photos = [];
  const hashStr = (s) => [...String(s)].reduce((a, c) => (a * 31 + c.codePointAt(0)) >>> 0, 7);
  function photoFor(i) {
    if (!photos.length) return "";
    const p = photos[i % photos.length];
    return `<figure class="photo"><img src="img/${esc(p.file)}" alt="${esc(p.caption)}" loading="lazy"><figcaption>${esc(p.caption)} </figcaption></figure>`;
  }

  /* ---------- spaced review of misses ---------- */
  const STEPS = [1, 3, 7, 21, 60, 120]; // days
  function schedule(item, right) {
    if (item.fill) return;
    const list = progress.review || (progress.review = []);
    const id = item.reviewId || norm(item.prompt + "|" + item.answer).slice(0, 160);
    let r = list.find((x) => x.id === id);
    if (!r && right) return;
    if (!r) { r = { id, tag: item.tag || "", step: -1, item: { prompt: item.prompt, big: item.big, answer: item.answer, accept: item.accept, options: item.options, why: item.why, tag: item.tag } }; list.push(r); }
    r.step = right ? r.step + 1 : 0;
    if (r.step >= STEPS.length) { list.splice(list.indexOf(r), 1); }
    else r.due = Date.now() + STEPS[Math.max(0, r.step)] * 864e5 - 4 * 36e5;
    saveProgress(progress);
  }

  /* ---------- word lookup (tap, or hover with a mouse) ---------- */
  let lookIdx = null, lookCtx = {};
  function lookupIndex() {
    if (!lookIdx) lookIdx = (async () => {
      const [lex, extra, more, verbs, names, forms, colloq] = await Promise.all([lexicon(), getJSON("lessons/lookup-extra.json").catch(() => ({})), getJSON("lessons/lookup-gloss.json").catch(() => ({})), resolve("grammar/verbs-holton.json").catch(() => ({})), resolve("lexicon/names.json").catch(() => ({})), resolve("lexicon/forms-index.json").catch(() => ({})), resolve("colloquial/colloquial-lookup.json").catch(() => ({}))]);
      return window.EllinikaLookup.build(lex, { ...names, ...colloq, ...more, ...extra }, verbs["irregular_verbs_6.25"]?.verbs || [], forms.forms || {});
    })();
    return lookIdx;
  }
  const GREEK_RUN = /[Ͱ-Ͽἀ-῿]+(?:['’](?=[\s,.;!?»]|$))?/g;
  function wrapGreek(root) {
    if (!root) return;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, { acceptNode: (n) => n.parentElement.closest("button, input, textarea, summary, .w, .no-look, .eyebrow, .lk-pop, script, style, .q-big") ? NodeFilter.FILTER_REJECT : /[Ͱ-Ͽἀ-῿]/.test(n.nodeValue) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP });
    const nodes = []; while (walker.nextNode()) nodes.push(walker.currentNode);
    for (const n of nodes) {
      const s = n.nodeValue, frag = document.createDocumentFragment(); let last = 0;
      for (const m of s.matchAll(GREEK_RUN)) {
        if (m.index > last) frag.append(s.slice(last, m.index));
        const sp = document.createElement("span"); sp.className = "w"; sp.textContent = m[0]; frag.append(sp);
        last = m.index + m[0].length;
      }
      if (last < s.length) frag.append(s.slice(last));
      n.replaceWith(frag);
    }
  }
  const pop = document.createElement("div");
  pop.className = "lk-pop"; pop.hidden = true; pop.setAttribute("role", "dialog");
  document.body.append(pop);
  let popFor = null, hoverT = null;
  const POS_EL = { noun: "noun", verb: "verb", adjective: "adj.", adverb: "adv.", pronoun: "pron.", preposition: "prep.", conjunction: "conj.", article: "article", numeral: "num.", particle: "particle" };
  function vocabState(lemma) {
    const v = progress.vocab?.[lemma];
    if (!v) return `<button class="lk-add" data-lemma="${esc(lemma)}">+ Add to my words</button>`;
    if (v.ivl >= KNOWN_DAYS) return `<span class="lk-state known">Known</span>`;
    const d = Math.round((v.due - Date.now()) / 864e5);
    return `<span class="lk-state">In recall · ${d <= 0 ? "due now" : `next in ${d} day${d > 1 ? "s" : ""}`}</span>`;
  }
  const REF_TAB = { noun: "nouns", adjective: "adjectives", verb: "irregular" }; // Library grammar tables (library.js)
  // Collocations, synonyms and word family for the 2,000 most frequent content words (data/lexicon/collocations.json), loaded on first lookup.
  let collocP;
  const collocs = () => (collocP = collocP || resolve("lexicon/collocations.json").then((d) => d.entries || {}).catch(() => ({})));
  const collocBlock = (c) => !c ? "" : `${(c.collocations || []).length ? `<ul class="lk-col">${c.collocations.slice(0, 3).map((x) => `<li><span lang="el">${esc(x.el)}</span> <span class="lk-col-en">${esc(x.en)}</span></li>`).join("")}</ul>` : ""}${(c.synonyms || []).length ? `<div class="lk-rel"><span class="lk-pos">≈</span> <span lang="el">${esc(c.synonyms.slice(0, 3).join(", "))}</span></div>` : ""}${(c.family || []).length ? `<div class="lk-rel"><span class="lk-pos">family</span> <span lang="el">${esc(c.family.slice(0, 4).join(", "))}</span></div>` : ""}`;
  // When the tapped word is an inflected form, say so: «φωτός» is the genitive singular of «φως».
  function formNote(word, h) {
    const w = word.replace(/['’]$/, "").toLowerCase();
    if (!h.lemma || w === h.lemma.toLowerCase()) return "";
    const what = h.entry?.noun?.gen_sg === w ? "genitive singular of" : "a form of";
    return `<div class="lk-form"><span lang="el">${esc(word)}</span> is ${what} <span lang="el">${esc(h.lemma)}</span></div>`;
  }
  async function showLookup(el) {
    popFor = el;
    const word = el.textContent;
    const [index, col] = await Promise.all([lookupIndex(), collocs()]);
    const hits = window.EllinikaLookup.lookup(index, word, lookCtx);
    if (popFor !== el) return;
    const wik = (w) => `<a class="lk-ext" href="https://en.wiktionary.org/wiki/${encodeURIComponent(w.replace(/['’]$/, ""))}#Greek" target="_blank" rel="noopener">Wiktionary ↗</a>`;
    pop.innerHTML = `<div class="lk-word" lang="el">${esc(word)}</div>` + (hits ? hits.map((h, i) => `<div class="lk-hit">
        <div><span class="lk-lemma" lang="el">${esc(h.lemma)}</span>${POS_EL[h.pos] ? ` <span class="lk-pos">${POS_EL[h.pos]}</span>` : ""}${h.how === "guess" ? ` <span class="lk-pos">best guess</span>` : ""}</div>
        ${formNote(word, h)}
        <div class="lk-gloss">${esc(h.gloss)}</div>
        ${h.entry?.example?.el ? `<div class="lk-ex" lang="el">${esc(h.entry.example.el)}</div>` : ""}
        ${i === 0 ? collocBlock(col[h.lemma]) : ""}
        ${h.entry && VOCAB_POS.has(h.entry.pos) ? vocabState(h.entry.lemma) : ""}
        ${REF_TAB[h.pos] ? `<a class="lk-ext lk-tbl" href="#ref.${REF_TAB[h.pos]}~${encodeURIComponent(h.lemma)}">Table ↗</a>` : ""}
      </div>`).join("") + wik(hits[0].lemma) : `<div class="lk-gloss">Not in the word list yet.</div>${wik(word)}`);
    pop.hidden = false;
    const r = el.getBoundingClientRect(), pw = Math.min(300, window.innerWidth - 24);
    pop.style.width = pw + "px";
    pop.style.left = Math.max(12, Math.min(window.innerWidth - pw - 12, r.left + r.width / 2 - pw / 2)) + "px";
    const below = r.bottom + 8, h = pop.offsetHeight;
    pop.style.top = (below + h > window.innerHeight - 8 && r.top - h - 8 > 8 ? r.top - h - 8 : below) + "px";
    document.querySelectorAll(".w.on").forEach((x) => x.classList.remove("on")); el.classList.add("on");
  }
  function hideLookup() { pop.hidden = true; popFor = null; document.querySelectorAll(".w.on").forEach((x) => x.classList.remove("on")); }
  document.addEventListener("click", (e) => {
    const add = e.target.closest(".lk-add");
    if (add) { const v = vstore(); v[add.dataset.lemma] = { ivl: 0, reps: 0, lapses: 0, rec: 1, seen: Date.now(), due: Date.now() }; saveProgress(progress); add.outerHTML = `<span class="lk-state">Added · comes up in your next practice</span>`; return; }
    const w = e.target.closest(".w");
    if (w) { e.preventDefault(); if (popFor === w && !pop.hidden) hideLookup(); else { w.closest(".video")?.__pause?.(); showLookup(w); } return; }
    if (!e.target.closest(".lk-pop")) hideLookup();
  });
  document.addEventListener("pointerover", (e) => {
    if (e.pointerType !== "mouse") return;
    const w = e.target.closest(".w");
    clearTimeout(hoverT);
    if (w) hoverT = setTimeout(() => showLookup(w), 280);
    else if (!e.target.closest(".lk-pop") && popFor && !popFor.dataset.pinned) hoverT = setTimeout(hideLookup, 450);
  });
  window.addEventListener("scroll", () => { if (!pop.hidden) hideLookup(); }, { passive: true });

  /* ---------- videos (embedded from their host, subtitles from lessons/videos.json) ---------- */
  const mmss = (t) => `${Math.floor(t / 60)}:${String(Math.floor(t % 60)).padStart(2, "0")}`;
  function videoHTML(v) {
    const start = Math.floor(v.start || 0), end = Math.ceil(v.end || 0);
    const player = v.embed.kind === "youtube"
      ? `<iframe src="https://www.youtube-nocookie.com/embed/${encodeURIComponent(v.embed.src)}?enablejsapi=1&playsinline=1&rel=0&start=${start}${end ? `&end=${end}` : ""}" title="${esc(v.title)}" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>`
      : `<video controls playsinline preload="metadata" crossorigin="anonymous" src="${esc(v.embed.src)}#t=${start}${end ? "," + end : ""}"></video>`;
    return `<div class="video" data-vid="${esc(v.id)}">
      <span class="eyebrow">ΒΙΝΤΕΟ · ${esc(v.level || "")}</span><h3 lang="el">${esc(v.title)}</h3>
      <div class="vframe">${player}</div>
      <div class="subs"><div class="sub-el" lang="el">&nbsp;</div><div class="sub-en no-look" hidden></div></div>
      <div class="vctl"><button class="btn ghost small" data-act="en">English line</button><button class="btn ghost small" data-act="list">Transcript</button></div>
      <ol class="transcript" hidden>${(v.cues || []).map((c, i) => `<li data-i="${i}"><button class="tc-time" data-i="${i}">${mmss(c.t)}</button><span lang="el">${esc(c.el)}</span></li>`).join("")}</ol>
      <p class="src"><a href="${esc(v.source || "#")}" target="_blank" rel="noopener">${esc(v.credit || "source")}${v.license ? ", " + esc(v.license) : ""}</a></p>
    </div>`;
  }
  function wireVideo(el, v) {
    if (!v) return;
    const cues = v.cues || [], subEl = el.querySelector(".sub-el"), subEn = el.querySelector(".sub-en");
    const media = el.querySelector("video"), frame = el.querySelector("iframe");
    let ytTime = 0, cur = -2;
    const yt = (func, args = []) => frame?.contentWindow?.postMessage(JSON.stringify({ event: "command", func, args }), "*");
    const now = () => (media ? media.currentTime : ytTime);
    el.__pause = () => (media ? media.pause() : yt("pauseVideo"));
    const seek = (t) => { if (media) { media.currentTime = t; media.play(); } else { yt("seekTo", [t, true]); yt("playVideo"); } };
    const tick = () => {
      const t = now(), i = cues.findIndex((c) => t >= c.t && t < c.d);
      if (i === cur) return; cur = i;
      subEl.textContent = i >= 0 ? cues[i].el : " "; wrapGreek(subEl);
      subEn.textContent = i >= 0 ? cues[i].en || "" : "";
      el.querySelectorAll(".transcript li").forEach((li) => li.classList.toggle("on", +li.dataset.i === i));
    };
    if (media) { media.addEventListener("timeupdate", tick); media.addEventListener("seeked", tick); if (v.end) media.addEventListener("timeupdate", () => { if (media.currentTime > v.end) media.pause(); }); }
    if (frame) {
      // YouTube's embed reports its time by postMessage once told we are listening.
      const listen = () => frame.contentWindow?.postMessage(JSON.stringify({ event: "listening", id: v.id, channel: "widget" }), "*");
      frame.addEventListener("load", () => { listen(); setTimeout(listen, 800); });
      const onMsg = (e) => {
        if (e.source !== frame.contentWindow) return;
        try { const d = typeof e.data === "string" ? JSON.parse(e.data) : e.data; if (d?.info?.currentTime != null) { ytTime = d.info.currentTime; tick(); } } catch (err) { /* not ours */ }
      };
      window.addEventListener("message", onMsg);
      const iv = setInterval(() => { if (!document.body.contains(el)) { clearInterval(iv); window.removeEventListener("message", onMsg); } }, 2000);
    }
    el.querySelector('[data-act="en"]').onclick = (e) => { subEn.hidden = !subEn.hidden; e.target.classList.toggle("on", !subEn.hidden); };
    el.querySelector('[data-act="list"]').onclick = (e) => { const ol = el.querySelector(".transcript"); ol.hidden = !ol.hidden; e.target.classList.toggle("on", !ol.hidden); };
    el.querySelectorAll(".tc-time").forEach((b) => (b.onclick = () => seek(cues[+b.dataset.i].t)));
  }

  // All subtitled videos on one page, by level; "#videos.<id>" plays one.
  const allVideos = () => Promise.all(["lessons/videos.json", "lessons/videos-c1.json"].map((f) => getJSON(f).then((d) => d.videos || []).catch(() => []))).then((a) => a.flat());
  async function renderVideos(id) {
    hideLookup();
    const vids = await allVideos(), lessonTitle = (lid) => course.units.flatMap((u) => u.lessons).find((l) => l.id === lid && l.file);
    const v = id && vids.find((x) => x.id === id);
    if (v) {
      document.title = `${v.title} · Videos`;
      lookCtx = { ...(v.gloss || {}) };
      const rel = (v.lessons || []).map(lessonTitle).filter(Boolean);
      view.innerHTML = `<p class="crumbs"><a href="#videos">← All videos</a></p><section class="block">${videoHTML(v)}</section>
        ${rel.length ? `<section class="block"><h3>Lessons with this video</h3><ul class="vid-rel">${rel.map((l) => `<li><a href="#${l.id}"><span lang="el">${esc(l.el)}</span> · ${esc(l.title)}</a></li>`).join("")}</ul></section>` : ""}`;
      wrapGreek(view);
      wireVideo(view.querySelector(".video"), v);
      return window.scrollTo(0, 0);
    }
    document.title = "Videos · Ελληνικά";
    const levels = [...new Set(vids.map((x) => x.level || "Other"))];
    view.innerHTML = `<p class="crumbs"><a href="#">← Back to the course</a></p>
      <section class="intro"><h1>Videos</h1><p class="sub">${vids.length} videos with synced Greek subtitles. Tap any word in the subtitles to look it up.</p></section>
      ${levels.map((lv) => `<section class="block"><h2>${esc(lv)}</h2><ul class="lessons">${vids.filter((x) => (x.level || "Other") === lv).map((x) => `
        <li><a class="lesson-row" href="#videos.${esc(x.id)}"><span class="lr-num">▶</span>
          <span class="lr-main"><span class="lr-title" lang="el">${esc(x.title)}</span><span class="lr-en">${esc(x.title_en || x.credit || "")}${x.cues?.length ? ` · ${mmss((x.end || x.cues[x.cues.length - 1].d || 0) - (x.start || 0))}` : ""}</span></span></a></li>`).join("")}</ul></section>`).join("")}`;
    window.scrollTo(0, 0);
  }

  /* ---------- views ---------- */
  let course = null;
  const view = $("#view");

  function lessonStatus(id) {
    const p = progress[id];
    if (!p) return `<span class="chip new">new</span>`;
    const pct = Math.round(p.best * 100);
    return `<span class="chip${pct >= 85 ? " done" : ""}">${pct}%</span>`;
  }

  // Road to B2: grammar = lessons mastered (85%+), vocabulary = words produced and still recalled 90+ days on, comprehension = readings passed.
  const VOCAB_TARGET = 4000, KNOWN_DAYS = 90;
  function vocabCounts() {
    const vs = Object.values(progress.vocab || {});
    return { known: vs.filter((v) => v.ivl >= KNOWN_DAYS).length, producing: vs.filter((v) => v.reps > 0 && v.ivl > 0).length, seen: vs.length };
  }
  function tracker() {
    const levels = {};
    for (const u of course.units) {
      if (u.daily) continue;
      const lv = u.colloquial ? "Slang" : u.label.split(" ")[0];
      levels[lv] = levels[lv] || { total: 0, done: 0 };
      for (const l of u.lessons) { levels[lv].total++; if (progress[l.id]?.best >= 0.85) levels[lv].done++; }
    }
    const EXTRA_LV = ["C1", "Slang"];
    const all = Object.entries(levels).filter(([lv]) => !EXTRA_LV.includes(lv)).map(([, x]) => x).reduce((a, b) => ({ total: a.total + b.total, done: a.done + b.done }), { total: 0, done: 0 });
    const vc = vocabCounts();
    const reads = course.units.filter((u) => !u.colloquial && !EXTRA_LV.includes(u.label.split(" ")[0])).flatMap((u) => u.lessons).filter((l) => l.reading);
    const readDone = reads.filter((l) => progress.comp?.[l.id]?.best >= 0.75).length;
    const overall = 0.4 * (vc.known / VOCAB_TARGET) + 0.4 * (all.total ? all.done / all.total : 0) + 0.2 * (reads.length ? readDone / reads.length : 0);
    const syl = course.b2_syllabus || { areas: {}, themes: [] };
    const exam = Object.entries(syl.areas).map(([k, label]) => {
      const ls = course.units.flatMap((u) => u.lessons).filter((l) => l.b2 === k);
      return [label, ls.filter((l) => progress[l.id]?.best >= 0.85).length, ls.length];
    });
    if (syl.themes.length) exam.push(["B2 vocabulary themes", syl.themes.filter((t) => progress["theme-" + t.id]?.best >= 0.85).length, syl.themes.length]);
    const bar = (label, done, total, extra) => `<div class="level"><span class="lv">${label}</span><div class="progress"><i style="width:${total ? (done / total) * 100 : 0}%"></i></div><span class="sub">${done}/${total}${extra || ""}</span></div>`;
    return `<section class="tracker" aria-label="Road to B2">
      <div class="unit-head"><h2>Road to B2</h2><span class="sub">${Math.round(overall * 100)}%</span></div>
      <div class="levels">${Object.entries(levels).map(([lv, x]) => bar(lv, x.done, x.total)).join("")}${levels.C1 ? "" : `<div class="level planned"><span class="lv">C1</span><div class="progress"></div><span class="sub">later</span></div>`}</div>
      <div class="levels exam">${bar("Words known", vc.known, VOCAB_TARGET)}${bar("Words in recall", vc.producing, VOCAB_TARGET)}${bar("Reading", readDone, reads.length)}</div>
      <h3>B2 exam syllabus</h3>
      <div class="levels exam">${exam.map((r) => bar(...r)).join("")}</div>
    </section>`;
  }

  function renderHome() {
    document.title = "Ελληνικά Course";
    const all = course.units.flatMap((u) => u.lessons).filter((l) => l.file);
    const done = all.filter((l) => progress[l.id]?.best >= 0.85).length;
    $("#bar-meta").textContent = `${done} of ${all.length} ready lessons mastered`;
    let n = 0;
    view.innerHTML = `
      <section class="intro hero"${photos.length ? ` style="background-image:url('img/${esc(photos[new Date().getDate() % photos.length].file)}')"` : ""}>
        <div class="hero-in"><span class="hero-el" lang="el">Ελληνικά</span><h1>${esc(course.title)}</h1>
        <div class="meander" aria-hidden="true"></div>
        <div class="hero-stats"><span><b>${vocabCounts().known}</b> words known</span><span><b>${done}</b>/${all.length} lessons</span><a class="btn small" href="#daily-words">Word recall</a><a class="btn small" href="#videos">Videos</a><a class="btn small" href="#library">Resources</a></div></div>
      </section>
      ${tracker()}
      <div class="unit-tabs" role="tablist" aria-label="Units">${course.units.map((u, i) => `<button data-i="${i}">${esc(u.label.replace(" · ", " "))}</button>`).join("")}</div>
      <div class="pager-wrap" id="units">
        <div class="pager">${course.units.map((u, ui) => `
        <section class="unit page">
          ${photoFor(ui)}
          <div class="unit-head"><span class="eyebrow">${esc(u.label)}</span><h2>${esc(u.title)}</h2></div>
          <ul class="lessons">${u.lessons.map((l) => { n++; return l.file ? `
            <li><a class="lesson-row" href="#${l.id}">
              <span class="lr-num">${n}</span>
              <span class="lr-main"><span class="lr-title" lang="el">${esc(l.el)}</span><span class="lr-en">${esc(l.title)}</span></span>
              ${lessonStatus(l.id)}
            </a></li>` : `
            <li><div class="lesson-row planned">
              <span class="lr-num">${n}</span>
              <span class="lr-main"><span class="lr-title" lang="el">${esc(l.el)}</span><span class="lr-en">${esc(l.title)}${l.holton ? ` · Holton §${esc(l.holton)}` : ""}</span></span>
              <span class="chip new">coming</span>
            </div></li>`; }).join("")}</ul>
        </section>`).join("")}</div>
        ${pagerNav()}
      </div>
      <p class="src"><a href="#videos">Videos</a> · <a href="#library">Resources</a> · <a href="#credits">Credits</a></p>`;
    // Open on the unit holding the first lesson not yet mastered.
    const firstOpen = course.units.findIndex((u) => u.lessons.some((l) => l.file && !(progress[l.id]?.best >= 0.85)));
    const tabs = [...view.querySelectorAll(".unit-tabs button")];
    const pg = pager($("#units"), (i) => tabs.forEach((t, k) => { t.setAttribute("aria-current", k === i); if (k === i) t.scrollIntoView({ inline: "nearest", block: "nearest" }); }));
    tabs.forEach((t, k) => (t.onclick = () => pg.go(k)));
    pg.go(Math.max(0, firstOpen), true);
    window.scrollTo(0, 0);
  }

  async function renderLesson(id, tab) {
    const meta = course.units.flatMap((u) => u.lessons).find((l) => l.id === id && l.file);
    if (!meta) return renderHome();
    const lesson = await getJSON(`lessons/${meta.file}`);
    document.title = `${lesson.el} · Ελληνικά`;
    const all = course.units.flatMap((u) => u.lessons).filter((l) => l.file);
    const idx = all.indexOf(meta);
    $("#bar-meta").textContent = `Lesson ${idx + 1} of ${all.length}`;
    view.innerHTML = `
      <div class="lesson-head">
        <h1 lang="el">${esc(lesson.el)}</h1>
        <p class="sub">${esc(lesson.title)}</p>
      </div>
      <div class="tabs" role="tablist">
        <button class="tab" role="tab" id="tab-learn" aria-selected="${tab !== "practice"}">Learn</button>
        <button class="tab" role="tab" id="tab-practice" aria-selected="${tab === "practice"}">Practice</button>
      </div>
      <div id="pane"></div>`;
    lesson.id = id;
    if (!lesson.blocks?.length) { lesson.blocks = []; $("#tab-learn").hidden = true; tab = "practice"; }
    $("#tab-learn").onclick = () => showLearn(lesson, all, idx);
    $("#tab-practice").onclick = () => showPractice(lesson, meta, all, idx);
    if (tab === "practice") showPractice(lesson, meta, all, idx); else showLearn(lesson, all, idx);
    window.scrollTo(0, 0);
  }

  function selectTab(name) {
    $("#tab-learn").setAttribute("aria-selected", name === "learn");
    $("#tab-practice").setAttribute("aria-selected", name === "practice");
  }

  async function showLearn(lesson) {
    selectTab("learn");
    const pane = $("#pane");
    pane.innerHTML = `<p class="loading">Loading…</p>`;
    const html = [];
    lookCtx = {};
    const vids = (await Promise.all(["lessons/videos.json", "lessons/videos-c1.json"].map((f) => getJSON(f).then((d) => d.videos || []).catch(() => [])))).flat().filter((v) => (v.lessons || []).includes(lesson.id));
    for (const b of [...lesson.blocks, ...vids.map((v) => ({ ...v, type: "video" }))]) {
      try { html.push(`<section class="block">${await BLOCKS[b.type](b)}</section>`); }
      catch (e) { html.push(`<section class="block"><p class="sub">This part could not load (${esc(e.message)}).</p></section>`); }
    }
    const pages = html.map((h, i) => `<div class="page">${i === 0 ? photoFor(lesson.photo ?? hashStr(lesson.el)) : ""}${h}${i === html.length - 1 ? `<div class="next-cta"><button class="btn" id="go-practice">Start practice</button></div>` : ""}</div>`);
    pane.innerHTML = `<div class="learn pager-wrap" id="learn"><div class="pager">${pages.join("")}</div>${pagerNav()}</div>`;
    pager($("#learn"));
    wrapGreek(pane);
    pane.querySelectorAll(".video").forEach((el) => wireVideo(el, vids.find((v) => v.id === el.dataset.vid)));
    $("#go-practice").onclick = () => { $("#tab-practice").click(); window.scrollTo(0, 0); };
  }

  /* ---------- practice session ---------- */
  async function buildItems(lesson) {
    const items = [];
    for (const spec of lesson.practice) {
      try { items.push(...(await GENERATORS[spec.gen](spec)).map((it) => ({ ...it, why: it.why || spec.why }))); }
      catch (e) { console.warn("generator failed", spec.gen, e); }
    }
    const tail = [];
    for (const b of lesson.blocks) if (b.type === "reading" && b.questions) tail.push(...(await GENERATORS["reading-q"](b)));
    if (!lesson.practice.some((p) => p.gen === "vocab-recall")) {
      try { tail.push(...(await GENERATORS["vocab-recall"]({ n: 6, new: 4, words: lesson.vocab }))); } catch (e) { console.warn("vocab failed", e); }
    }
    const main = items.filter((it) => !it.vocab), voc = items.filter((it) => it.vocab);
    return [...(lesson.shuffle === false ? main : shuffle(main)), ...tail, ...voc];
  }

  async function showPractice(lesson, meta, all, idx) {
    selectTab("practice");
    const pane = $("#pane");
    pane.innerHTML = `<p class="loading">Building exercises…</p>`;
    const queue = await buildItems(lesson);
    const total = queue.length;
    const graded = queue.filter((it) => !it.vocab && !it.comp).length;
    const state = { i: 0, right: 0, missed: [], retry: [], vRight: 0, vTotal: queue.filter((it) => it.vocab).length, cRight: 0, cTotal: queue.filter((it) => it.comp).length };

    function next() {
      if (state.i >= queue.length) return finish();
      const item = queue[state.i];
      const firstPass = state.i < total;
      const done = Math.min(state.i, total);
      pane.innerHTML = `
        <div class="practice">
          <div class="pmeta"><span>${firstPass ? `${state.i + 1} / ${total}` : "Again"}</span><span>${state.right + state.vRight + state.cRight} right</span></div>
          <div class="progress"><i style="width:${(done / total) * 100}%"></i></div>
          <div class="card" id="card">
            <span class="q-kind">${esc(item.kind)}</span>
            <div class="q-prompt">${md(item.prompt)}</div>
            ${item.big ? `<div class="q-big${item.big.length > 8 ? " mid" : ""}" lang="el">${esc(item.big)}</div>` : ""}
            <div id="answer-area"></div>
            <div id="fb"></div>
            <div class="actions" id="acts"></div>
          </div>
        </div>`;
      const area = $("#answer-area"), fb = $("#fb"), acts = $("#acts");
      if (!item.vocab) wrapGreek($("#card .q-prompt"));
      const record = (result, shown) => {
        let snap = null;
        if (firstPass && item.vocab) {
          snap = JSON.stringify(vstore()[item.vocab.lemma] || null);
          vocabGrade(item.vocab.lemma, result, item.vocab.mode);
          if (result !== "wrong") state.vRight++;
          else if (item.vocab.mode === "prod") { state.missed.push({ item, given: shown }); queue.push(item); }
        } else if (firstPass && item.comp) {
          if (result === "right") state.cRight++;
        } else if (firstPass) {
          schedule(item, result === "right");
          if (result === "right") state.right++;
          else { state.missed.push({ item, given: shown }); queue.push(item); }
        }
        const label = { right: "Σωστά! Correct.", almost: "Almost: check the accent.", wrong: "Not quite." }[result];
        fb.innerHTML = `<div class="feedback ${result}"><strong>${label}</strong>${result !== "right" ? `<span>Answer: <span lang="el">${esc(item.answer)}</span></span>` : ""}${item.why ? `<span class="why">${md(item.why)}</span>` : ""}</div>`;
        wrapGreek(fb);
        acts.innerHTML = `${snap && result === "wrong" && item.vocab.mode === "prod" ? `<button class="kbd-toggle" id="override">I was right</button>` : "<span></span>"}<button class="btn" id="next">${state.i + 1 >= queue.length ? "See results" : "Next"}</button>`;
        const ov = $("#override");
        if (ov) ov.onclick = () => {
          // A synonym or variant the list does not know: undo the miss and count it as recalled.
          const vs = vstore(), prevV = JSON.parse(snap); if (prevV) vs[item.vocab.lemma] = prevV; else delete vs[item.vocab.lemma];
          vocabGrade(item.vocab.lemma, "right", "prod");
          state.vRight++; state.missed.pop(); queue.pop();
          ov.remove(); fb.querySelector(".feedback").className = "feedback right";
        };
        const nb = $("#next"); nb.focus({ preventScroll: true }); nb.onclick = () => { state.i++; next(); };
        fb.scrollIntoView({ block: "nearest", behavior: "smooth" });
      };

      if (item.options) {
        area.innerHTML = `<div class="options">${item.options.map((o, k) => `<button class="opt" data-k="${k}" lang="el">${esc(o)}</button>`).join("")}</div>`;
        area.querySelectorAll(".opt").forEach((btn) => btn.onclick = () => {
          const chosen = item.options[+btn.dataset.k];
          area.querySelectorAll(".opt").forEach((b) => { b.disabled = true; if (item.options[+b.dataset.k] === item.answer) b.classList.add("right"); });
          if (chosen !== item.answer) btn.classList.add("wrong");
          record(chosen === item.answer ? "right" : "wrong", chosen);
        });
        hideKeypad();
      } else if (item.fill) {
        area.innerHTML = `<div class="grid-fill">${item.fill.map((r, k) => `<label for="f${k}" lang="el">${esc(r.label)}</label><input id="f${k}" lang="el" autocomplete="off" autocapitalize="off" spellcheck="false" ${r.given ? `value="${esc(variants(r.form)[0])}" readonly` : ""}>`).join("")}</div>`;
        acts.innerHTML = `<button class="kbd-toggle" id="kbd">Greek keyboard</button><button class="btn" id="check">Check</button>`;
        $("#kbd").onclick = toggleKeypad;
        $("#check").onclick = () => {
          let worst = "right";
          item.fill.forEach((r, k) => {
            const inp = $("#f" + k); if (r.given) return;
            const g = grade(inp.value, [r.form]);
            inp.classList.add(g); inp.readOnly = true;
            if (g !== "right") { inp.insertAdjacentHTML("afterend", `<span class="fix" lang="el">${esc(r.form)}</span>`); }
            if (g === "wrong" || (g === "almost" && worst === "right")) worst = g;
          });
          hideKeypad();
          record(worst, "");
        };
        const first = item.fill.findIndex((r) => !r.given); if (first >= 0) $("#f" + first).focus({ preventScroll: true });
      } else {
        area.innerHTML = `<div class="answer-row"><input id="ans" lang="el" autocomplete="off" autocapitalize="off" spellcheck="false" placeholder="Type in Greek" enterkeyhint="done"><button class="btn" id="check">Check</button></div>`;
        acts.innerHTML = `<button class="kbd-toggle" id="kbd">Greek keyboard</button><span></span>`;
        $("#kbd").onclick = toggleKeypad;
        const inp = $("#ans");
        const check = () => {
          if (inp.readOnly) return;
          const g = grade(inp.value, item.accept || [item.answer]);
          inp.classList.add(g); inp.readOnly = true; $("#check").disabled = true;
          hideKeypad();
          record(g, inp.value);
        };
        $("#check").onclick = check;
        inp.addEventListener("keydown", (e) => { if (e.key === "Enter") { e.preventDefault(); if (inp.readOnly) $("#next")?.click(); else check(); } });
        inp.focus({ preventScroll: true });
      }
    }

    function finish() {
      hideKeypad();
      const score = graded ? state.right / graded : 0;
      const prev = progress[meta.id];
      if (graded) progress[meta.id] = { best: Math.max(score, prev?.best || 0), last: score, at: new Date().toISOString(), runs: (prev?.runs || 0) + 1 };
      if (state.cTotal) { const c = state.cRight / state.cTotal, pc = (progress.comp || (progress.comp = {}))[meta.id]; progress.comp[meta.id] = { best: Math.max(c, pc?.best || 0), last: c }; }
      saveProgress(progress);
      const nextL = all[idx + 1];
      pane.innerHTML = `
        <div class="card result">
          <span class="q-kind">Result</span>
          ${graded ? `<div class="score">${Math.round(score * 100)}%</div>
          <p class="sub">Grammar ${state.right}/${graded}${score >= 0.85 ? " · mastered" : " · 85% to master"}</p>` : ""}
          ${state.cTotal ? `<p class="sub">Reading ${state.cRight}/${state.cTotal}</p>` : ""}
          ${state.vTotal ? `<p class="sub">Words ${state.vRight}/${state.vTotal} · ${vocabCounts().known} known, ${vocabCounts().producing} in recall</p>` : ""}
          ${state.missed.length ? `<div class="missed"><h3>To review</h3><ul class="ex-list">${state.missed.map((m) => `<li><span class="ex-el">${md(m.item.prompt)} ${m.item.big ? `<span lang="el">${esc(m.item.big)}</span>` : ""}</span><span class="ex-en">Answer: <span lang="el">${esc(m.item.answer)}</span>${m.given ? ` · you wrote ${esc(m.given)}` : ""}</span></li>`).join("")}</ul></div>` : ""}
          <div class="actions" style="width:100%">
            <button class="btn ghost" id="again">Practise again</button>
            <button class="btn ghost" id="quit">Save &amp; quit</button>
            ${nextL ? `<a class="btn" href="#${nextL.id}">Next lesson</a>` : `<a class="btn" href="#">Course map</a>`}
          </div>
        </div>`;
      $("#again").onclick = () => showPractice(lesson, meta, all, idx);
      // Quit writes the save file to the chosen destination (profiles.js), then returns to the course map.
      $("#quit").onclick = async (e) => { e.target.disabled = true; e.target.textContent = "Saving…"; await window.EllinikaProfiles?.saveNow?.(); location.hash = ""; };
    }
    next();
  }

  /* ---------- on-screen Greek keypad ---------- */
  const keypad = $("#keypad");
  const ROWS = ["ςερτυθιοπ", "ασδφγηξκλ", "ζχψωβνμ"];
  function buildKeypad() {
    keypad.innerHTML = ROWS.map((r, i) => `<div class="krow">${i === 2 ? `<button class="wide" data-k="acc" aria-label="add accent">´ τόνος</button>` : ""}${[...r].map((c) => `<button data-k="${c}">${c}</button>`).join("")}${i === 2 ? `<button class="wide" data-k="bs" aria-label="delete">⌫</button>` : ""}</div>`).join("")
      + `<div class="krow"><button class="wide" data-k="dia">¨</button><button class="wide" data-k=" " style="max-width:12rem">space</button><button class="wide" data-k="hide">done</button></div>`;
    keypad.addEventListener("pointerdown", (e) => e.preventDefault());
    keypad.addEventListener("click", (e) => {
      const k = e.target.closest("button")?.dataset.k; if (!k) return;
      const inp = document.activeElement?.tagName === "INPUT" ? document.activeElement : (lastInput && !lastInput.readOnly ? lastInput : null);
      if (k === "hide") return hideKeypad();
      if (!inp || inp.readOnly) return;
      const v = inp.value;
      if (k === "bs") inp.value = v.slice(0, -1);
      else if (k === "acc") { const m = v.match(/^(.*)([αεηιουω])([^αεηιουω]*)$/); if (m) inp.value = m[1] + ADD_ACC[m[2]] + m[3]; }
      else if (k === "dia") inp.value = v.replace(/[ιυί ύ]$/, (c) => ({ "ι": "ϊ", "υ": "ϋ", "ί": "ΐ", "ύ": "ΰ" }[c] || c));
      else inp.value = v + k;
      inp.focus({ preventScroll: true });
    });
  }
  let lastInput = null;
  document.addEventListener("focusin", (e) => { if (e.target.tagName === "INPUT") lastInput = e.target; });
  function toggleKeypad() { if (!keypad.innerHTML) buildKeypad(); keypad.hidden = !keypad.hidden; document.body.style.paddingBottom = keypad.hidden ? "" : "220px"; }
  function hideKeypad() { keypad.hidden = true; document.body.style.paddingBottom = ""; }

  function renderCredits() {
    view.innerHTML = `<h2>Credits</h2>
      <p class="sub">Grammar from Holton, Mackridge &amp; Philippaki-Warburton, <em>Greek: An Essential Grammar</em> (2nd ed.) and Poulopoulou, <em>Modern Greek: Grammar Notes for Absolute Beginners</em> (Kallipos, CC BY-NC-SA 3.0 GR). Word frequencies from the OpenSubtitles 2018 list (hermitdave/FrequencyWords, CC BY-SA 4.0). Progress is saved on this device.</p>
      <h3>Photos</h3><p class="sub">Wikimedia Commons, cropped and resized; CC BY-SA photos stay under their license.</p>
      <ul class="ex-list">${photos.map((p) => `<li><span class="ex-el" lang="el">${esc(p.caption)}</span><span class="ex-en">${esc(p.credit)} · <a href="${esc(p.source)}" target="_blank" rel="noopener">${esc(p.license)}, source</a></span></li>`).join("")}</ul>
      <p><a href="#">← Back to the course</a></p>`;
    window.scrollTo(0, 0);
  }

  // A rule item may be a string or an object ({rule, examples: [{el, en}]}); objects show their text and examples.
  function ruleItem(r) {
    if (r == null) return "";
    if (typeof r !== "object") return md(String(r));
    const text = r.rule || r.text || r.note || r.description || r.en || "";
    const ex = [].concat(r.examples || r.example || []).map((x) => typeof x === "object" && x
      ? `<span lang="el">${esc(x.el || x.form || "")}</span>${x.ipa ? ` [${esc(x.ipa)}]` : ""}${x.en || x.gloss ? ` <span class="ex-en">${esc(x.en || x.gloss)}</span>` : ""}`
      : `<span lang="el">${esc(x)}</span>`);
    const head = text ? md(String(text)) : r.el ? `<span lang="el">${esc(r.el)}</span>${r.en ? ` <span class="ex-en">${esc(r.en)}</span>` : ""}` : "";
    return head + (ex.length ? `<br>${ex.join(" · ")}` : "");
  }

  /* ---------- add-on hook: library.js and later modules register routes in window.EllinikaAddons ---------- */
  window.Ellinika = { $, esc, md, paras, getJSON, resolve, dataRoot, lexicon, wrapGreek, hideLookup, view, setGloss: (g) => { lookCtx = g || {}; }, get progress() { return progress; }, saveProgress: () => saveProgress(progress) };

  /* ---------- routing ---------- */
  function route() {
    hideKeypad();
    const h = location.hash.replace(/^#/, "");
    if (!h) return renderHome();
    if (h === "credits") return renderCredits();
    if (h === "videos" || h.startsWith("videos.")) return renderVideos(h.split(".")[1]);
    const [id, tab] = h.split(".");
    const addon = (window.EllinikaAddons || {})[id];
    if (addon) { hideLookup(); return addon(tab); }
    renderLesson(id, tab);
  }
  $("#brand").onclick = (e) => { e.preventDefault(); if (location.hash) location.hash = ""; else renderHome(); };
  window.addEventListener("hashchange", route);

  getJSON("img/manifest.json").then((m) => { photos = m.photos || []; }).catch(() => {})
    .then(() => getJSON("lessons/course.json")).then((c) => { course = c; route(); })
    .catch((e) => { view.innerHTML = `<p>The course could not load: ${esc(e.message)}. Open the app from its folder over http (for example <code>python3 -m http.server</code> in the project folder) so it can read the lesson files.</p>`; });
})();
