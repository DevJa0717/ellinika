/* Word lookup for Greek text: surface form -> lemma + gloss.
   Matching is accent-insensitive, so generated forms need only the right letters, not the right stress.
   Works in the page (window.EllinikaLookup) and in node (module.exports) for the coverage checker. */
(function (root) {
  "use strict";
  const strip = (s) => String(s).normalize("NFD").replace(/[̀-ͯ]/g, "").normalize("NFC").toLowerCase().replace(/ς/g, "σ");
  const GREEK = /[Ͱ-Ͽἀ-῿]/;

  // Ending sets by lemma ending (accent-stripped, final ς written σ). Over-generation is harmless: rank decides.
  const NOUN = [
    ["ματα", ["ματα", "ματων"]], ["μα", ["μα", "ματοσ", "ματα", "ματων"]],
    ["ιμο", ["ιμο", "ιματοσ", "ιματα", "ιματων"]],
    ["ον", ["ον", "οντοσ", "οντα", "οντων"]],
    ["οσ", ["οσ", "ο", "ου", "ε", "οι", "ουσ", "ων", "η", "εα"]],
    ["ασ", ["ασ", "α", "εσ", "ων", "αδεσ", "αδων", "ατοσ", "ατα", "ατων"]],
    ["ησ", ["ησ", "η", "εσ", "ων", "ηδεσ", "ηδων", "εισ", "ουσ", "εων"]],
    ["εσ", ["εσ", "ε", "εδεσ", "εδων"]],
    ["ουσ", ["ουσ", "ου", "ουδεσ", "ουδων"]],
    ["α", ["α", "ασ", "εσ", "ων", "αδεσ", "αδων", "ατα", "ατων", "ατοσ"]],
    ["η", ["η", "ησ", "εσ", "ων", "εισ", "εων"]],
    ["ι", ["ι", "ιου", "ια", "ιων", "ιου"]],
    ["ο", ["ο", "ου", "α", "ων"]],
    ["ου", ["ου", "ουσ", "ουδεσ", "ουδων"]],
    ["υ", ["υ", "υου", "ια", "υα", "υων"]],
  ];
  const ADJ = [
    ["οσ", ["οσ", "ο", "ου", "ε", "οι", "ουσ", "ων", "η", "ησ", "εσ", "α", "ια", "ιασ", "ιεσ"]],
    ["ησ", ["ησ", "η", "ουσ", "εισ", "ων", "εσ", "ικο", "ικη", "ικοσ", "ικα", "ικεσ", "ικοι", "ικου", "ικουσ", "ικων", "ιδεσ", "ια", "ιασ", "ιεσ"]],
    ["υσ", ["υσ", "υ", "ιου", "ιοι", "ιουσ", "ιων", "ια", "ιασ", "ιεσ", "εοσ", "εια", "ειασ", "ειεσ", "εων", "εισ", "εα"]],
    ["ων", ["ων", "οντα", "οντοσ", "οντεσ", "οντων", "ουσα", "ουσασ", "ουσεσ", "ουσων", "ον"]],
  ];
  const V_ACT = ["ω", "εισ", "ει", "ουμε", "ετε", "ουν", "ουνε", "ε", "τε", "οντασ", "α", "εσ", "αμε", "ατε", "αν", "ανε", "ομαι", "εσαι", "εται", "ομαστε", "εστε", "ονται", "ομουν", "οσουν", "οταν", "ομασταν", "οσασταν", "ονταν", "ομουνα", "οσουνα", "οτανε", "ονταν", "οντανε", "μενοσ", "μενη", "μενο", "μενοι", "μενεσ", "μενα", "μενου", "μενων", "μενουσ"];
  const V_CONT = ["ω", "αω", "ασ", "αει", "α", "αμε", "ουμε", "ατε", "ανε", "ουν", "ουνε", "αν", "εισ", "ει", "ειτε", "ουσα", "ουσεσ", "ουσε", "ουσαμε", "ουσατε", "ουσαν", "ουσανε", "αγα", "αγεσ", "αγε", "αγαμε", "αγατε", "αγαν", "ωντασ", "α", "ατε", "ιεμαι", "ιεσαι", "ιεται", "ιομαστε", "ιεστε", "ιουνται", "ιοταν", "ιομουν", "αμαι", "ασαι", "αται", "ομαστε", "αστε", "ουνται", "ομουν", "οταν"];
  const V_AOR = ["α", "εσ", "ε", "αμε", "ατε", "αν", "ανε", "ω", "εισ", "ει", "ουμε", "ετε", "ουν", "ουνε", "ε", "τε", "ετε", "ει"];
  const V_PASS = ["ηκα", "ηκεσ", "ηκε", "ηκαμε", "ηκατε", "ηκαν", "ηκανε", "ω", "εισ", "ει", "ουμε", "ειτε", "ουν", "ειτε", "ου"];

  const ENDINGS = new Set([...NOUN, ...ADJ].flatMap(([, f]) => f).concat(V_ACT, V_CONT, V_AOR, V_PASS, ["σ", "ουσ"]));

  function build(entries, extra, irregular, forms) {
    const idx = new Map();         // stripped form -> [{e, how, note}]
    const stems = new Map();       // stripped stem -> [e] for guesses
    const add = (form, e, how, note) => {
      if (!form || /\s/.test(form)) return;
      const k = strip(form);
      if (k.length < 1) return;
      const list = idx.get(k) || idx.set(k, []).get(k);
      if (!list.some((x) => x.e === e)) list.push({ e, how, note });
    };
    const addStem = (stem, e) => { if (stem.length >= 3) { const l = stems.get(stem) || stems.set(stem, []).get(stem); if (!l.includes(e)) l.push(e); } };
    const expand = (lemmaS, table, e) => {
      for (const [end, forms] of table) if (lemmaS.endsWith(end)) { const st = lemmaS.slice(0, -end.length); for (const f of forms) add(st + f, e, "form"); addStem(st, e); return st; }
      return null;
    };
    const firstForm = (s) => String(s || "").replace(/\(.*?\)/g, "").split(/[\/,;]/)[0].trim();
    for (const e of entries) {
      const L = e.lemma; if (!L) continue;
      for (const alt of String(L).split(/\s*[\/,]\s*/)) add(alt, e, "lemma");
      const s = strip(firstForm(L));
      if (e.pos === "noun") { expand(s, NOUN, e); if (e.noun?.gen_sg) add(firstForm(e.noun.gen_sg), e, "form", "genitive"); }
      else if (e.pos === "adjective") { expand(s, ADJ, e); for (const g of ["m", "f", "n"]) if (e.adjective?.[g]) for (const f of String(e.adjective[g]).split(/[\/,]/)) { add(f.trim(), e, "form"); expand(strip(f.trim()), ADJ, e); } }
      else if (e.pos === "verb") {
        let st = null;
        if (/(ιεμαι|αμαι)$/.test(s)) { st = s.replace(/(ιεμαι|αμαι)$/, ""); for (const f of V_CONT) add(st + f, e, "form"); }
        else if (/ομαι$/.test(s)) { st = s.slice(0, -4); for (const f of V_ACT) add(st + f, e, "form"); }
        else if (/[αοε]ω$/.test(s) && /ώ$|άω$/.test(firstForm(L)) || /ω$/.test(s) && /ώ$/.test(firstForm(L))) { st = s.replace(/α?ω$/, ""); for (const f of V_CONT) add(st + f, e, "form"); }
        else if (/ω$/.test(s)) { st = s.slice(0, -1); for (const f of V_ACT) { add(st + f, e, "form"); if (/^(α|ε|η|ε|ω|εσ|ετε|αν|ανε|αμε|ατε)$/.test(f)) add("ε" + st + f, e, "form"); } }
        if (st) addStem(st, e);
        const aor = firstForm(e.verb?.aorist_1sg);
        if (aor && /α$/.test(strip(aor))) {
          const a = strip(aor).slice(0, -1);
          for (const f of V_AOR) add(a + f, e, "form", "past");
          if (/^[εη]/.test(a) && !/^[εη]/.test(s)) for (const f of V_AOR) add(a.slice(1) + f, e, "form");
        }
      } else if (e.pos === "adverb" && /α$/.test(s)) { /* nothing */ }
      else expand(s, NOUN, e);
    }
    // Holton's irregular verb table (present, past, dependent, passive forms) mapped to the lexicon entry.
    const byLemma = new Map(entries.map((e) => [e.lemma, e]));
    for (const v of irregular || []) {
      const pres = firstForm(v.present);
      const e = byLemma.get(pres) || { lemma: pres, gloss: v.meaning, pos: "verb", irregularOnly: true };
      add(pres, e, "lemma");
      for (const [field, ends] of [["active_simple_past", V_AOR], ["passive_simple_past", V_PASS], ["dependent", V_AOR], ["passive_dependent", V_PASS]]) {
        for (const raw of String(v[field] || "").split("/")) {
          const f = strip(raw.replace(/\(.*?\)/g, "").replace(/^θα\s+/, "").trim()); if (!f || /\s/.test(f)) continue;
          add(f, e, "form", field.includes("passive") ? "passive" : "past");
          const st = f.replace(/(ηκα|ω|α)$/, ""); if (st !== f) for (const x of ends) add(st + x, e, "form");
          if (/ηκα$/.test(f)) for (const x of V_PASS.slice(7)) add(f.replace(/ηκα$/, "") + x, e, "form");
          if (/^[εη]/.test(st) && field === "active_simple_past") for (const x of V_AOR) add(st.slice(1) + x, e, "form");
        }
      }
      if (v.passive_perfect_participle) expand(strip(firstForm(v.passive_perfect_participle)), ADJ, e);
    }
    // Inflected forms written per lexicon entry (data/lexicon/forms-index.json): {form: [lemma, ...]}.
    for (const [form, lemmas] of Object.entries(forms || {})) for (const l of [].concat(lemmas)) { const e = byLemma.get(l); if (e) add(form, e, "form"); }
    // Hand-written forms (function words, clitics, irregular forms): {form: "lemma|gloss|note"}.
    for (const [form, val] of Object.entries(extra || {})) {
      const [lemma, gloss, note] = String(val).split("|");
      const e = byLemma.get(lemma) || { lemma, gloss, pos: "" };
      const list = idx.get(strip(form)) || idx.set(strip(form), []).get(strip(form));
      list.unshift({ e: gloss && e.gloss !== gloss ? { ...e, gloss } : e, how: "extra", note });
    }
    return { idx, stems };
  }

  const rank = (h) => (h.how === "extra" ? -1e6 : 0) + (h.how === "lemma" ? -1e5 : 0) + (h.e.rank || 9e4);
  // ctx: {form: "lemma — meaning"} glosses written into a lesson (reading texts, subtitles).
  function lookup(index, word, ctx) {
    const w = String(word).replace(/^[«"'(]+|[»"'.,;:!?·)…]+$/g, "");
    if (!w || !GREEK.test(w)) return null;
    const k = strip(w);
    const out = [];
    if (ctx) for (const [f, g] of Object.entries(ctx)) if (strip(f) === k) { const [lemma, ...rest] = String(g).split(/\s+[—–-]\s+/); out.push({ lemma: rest.length ? lemma : w, gloss: rest.length ? rest.join(" — ") : g, how: "gloss" }); break; }
    const hits = (index.idx.get(k) || []).slice().sort((a, b) => rank(a) - rank(b));
    for (const h of hits) if (!out.some((o) => o.lemma === h.e.lemma)) out.push({ lemma: h.e.lemma, gloss: h.e.gloss, pos: h.e.pos, entry: h.e.irregularOnly ? null : h.e, how: h.how, note: h.note });
    if (!out.length) {
      // Guess: longest known stem that the word starts with (at most 5 letters of ending).
      for (let n = k.length - 1; n >= Math.max(3, k.length - 5) && !out.length; n--) {
        if (!ENDINGS.has(k.slice(n))) continue;
        const l = index.stems.get(k.slice(0, n));
        if (l) for (const e of l.slice().sort((a, b) => (a.rank || 9e4) - (b.rank || 9e4)).slice(0, 2)) out.push({ lemma: e.lemma, gloss: e.gloss, pos: e.pos, entry: e, how: "guess" });
      }
    }
    return out.length ? out.slice(0, out[0].how === "gloss" || out[0].how === "extra" ? 2 : 3) : null;
  }

  const api = { build, lookup, strip, GREEK };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.EllinikaLookup = api;
})(typeof window !== "undefined" ? window : globalThis);
