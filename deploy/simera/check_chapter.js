// Checks bilingual reader chapters (shared format, ledger 2026-10-25 20:40).
// Usage: node /mnt/project-files/deploy/simera/check_chapter.js /mnt/project-files/app/library/simera/<file>.json ...
// Reports: schema problems, cite numbers without a source, quiz answers not among options, final-ν slips,
// hunspell el_GR unknown words (needs `hunspell -d el_GR`), and words the app's tap lookup cannot resolve
// (MISS) or only stem-guesses (GUESS). Fix MISS/GUESS by adding entries to the chapter's "gloss" map:
// {"inflected form as written": "lemma — English gloss"}. Exit code 1 if anything blocking is found.
const fs = require("fs"), path = require("path"), cp = require("child_process");
const APP = "/mnt/project-files/app", D = "/mnt/project-files/data/";
const L = require(APP + "/lookup.js");
const lex = [], seen = new Set();
for (const f of fs.readdirSync(D + "lexicon").filter((f) => /^core-.*\.json$/.test(f)).sort()) {
  const d = JSON.parse(fs.readFileSync(D + "lexicon/" + f)); for (const e of Array.isArray(d) ? d : d.entries) if (!seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); }
}
for (const e of JSON.parse(fs.readFileSync(D + "colloquial/colloquial-lexicon.json"))) if (!seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); }
const irr = JSON.parse(fs.readFileSync(D + "grammar/verbs-holton.json"))["irregular_verbs_6.25"].verbs;
const J = (p) => fs.existsSync(p) ? JSON.parse(fs.readFileSync(p)) : {};
const extra = { ...J(APP + "/lessons/lookup-gloss.json"), ...J(APP + "/lessons/lookup-extra.json") };
const index = L.build(lex, { ...J(D + "lexicon/names.json"), ...J(D + "colloquial/colloquial-lookup.json"), ...extra }, irr, J(D + "lexicon/forms-index.json").forms || {});
const tok = (s) => String(s).match(/[Ͱ-Ͽἀ-῿]+(?:['’])?/g) || [];
let bad = 0;
const finalN = (s, where, out) => {
  // την/στην/τον/στον/ένα(ν)/δεν/μην before consonants: keep ν before vowels and κ π τ ξ ψ γκ μπ ντ τσ τζ
  const keep = /^([αεηιουωάέήίόύώϊϋΐΰ]|κ|π|τ|ξ|ψ|γκ|μπ|ντ|τσ|τζ)/i;
  const re = /(^|[\s«(“"])(τη|στη|την|στην|μη|μην)\s+([Ͱ-Ͽἀ-῿]+)/gi;
  let m; while ((m = re.exec(s))) {
    const art = m[2].toLowerCase(), w = m[3].toLowerCase().normalize("NFC");
    const hasN = art.endsWith("ν"), needs = keep.test(w);
    if (hasN && !needs && (art === "την" || art === "στην")) out.push(`${where}: "${m[2]} ${m[3]}" → drop ν`);
    if (!hasN && needs) out.push(`${where}: "${m[2]} ${m[3]}" → add ν`);
  }
};
for (const f of process.argv.slice(2)) {
  let c; try { c = JSON.parse(fs.readFileSync(f)); } catch (e) { console.log(`${f}: INVALID JSON ${e.message}`); bad++; continue; }
  const probs = [], warn = [];
  for (const k of ["id", "el", "title", "level", "summary_en", "sections", "grammar", "terms", "gloss", "questions", "vocab", "sources"]) if (!(k in c)) probs.push("missing key " + k);
  const srcN = new Set((c.sources || []).map((s) => s.n));
  for (const s of c.sources || []) if (!/^https?:\/\//.test(s.url || "")) probs.push(`source ${s.n} has no url`);
  const greek = [];
  (c.sections || []).forEach((s, i) => {
    if (!s.el || !s.en) probs.push(`section ${i} lacks el/en heading`);
    greek.push(s.el);
    (s.paras || []).forEach((p, j) => {
      if (!p.el || !p.en) probs.push(`section ${i} para ${j} lacks el/en`);
      if (!(p.cite || []).length) probs.push(`section ${i} para ${j} has no cite`);
      for (const n of p.cite || []) if (!srcN.has(n)) probs.push(`section ${i} para ${j} cites [${n}] with no source`);
      greek.push(p.el); finalN(p.el || "", `s${i}p${j}`, warn);
    });
  });
  (c.questions || []).forEach((q, i) => { greek.push(q.q, ...(q.options || [])); if (!(q.options || []).includes(q.answer)) probs.push(`question ${i}: answer not among options`); });
  (c.grammar || []).forEach((g) => (g.examples || []).forEach((x) => { greek.push(x.el); finalN(x.el || "", "grammar", warn); }));
  (c.terms || []).forEach((t) => greek.push(t.el, t.def_el));
  if (c.image) greek.push(c.image.caption);
  const ctx = c.gloss || {}, MISS = new Set(), GUESS = new Set(), words = new Set();
  for (const t of greek) for (const w of tok(t || "")) { words.add(w.replace(/['’]$/, "")); const r = L.lookup(index, w, ctx); if (!r) MISS.add(w); else if (r[0].how === "guess") GUESS.add(`${w}→${r[0].lemma}`); }
  let spell = [];
  try { spell = cp.execSync("hunspell -i UTF-8 -d el_GR -l", { input: [...words].join("\n"), env: { ...process.env, LANG: "C.UTF-8" } }).toString().split("\n").filter(Boolean); } catch (e) {}
  spell = spell.filter((w) => !(w in ctx) && !/^[Α-ΩΆ-Ώ]/.test(w)); // proper names are left to the gloss
  bad += probs.length + MISS.size;
  console.log(`${path.basename(f)}: ${probs.length} problems, ${MISS.size} lookup misses, ${GUESS.size} guesses, ${warn.length} final-ν, ${spell.length} unknown to hunspell`);
  for (const p of probs) console.log("  PROBLEM: " + p);
  if (MISS.size) console.log("  MISS: " + [...MISS].join(" "));
  if (GUESS.size) console.log("  GUESS: " + [...GUESS].join(" "));
  for (const w of warn) console.log("  FINAL-N: " + w);
  if (spell.length) console.log("  SPELL?: " + spell.join(" "));
}
process.exitCode = bad ? 1 : 0;
