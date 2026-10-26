// Checks bilingual reader chapters (shared format). Based on deploy/simera/check_chapter.js, with a built-in
// spelling check against the LibreOffice el_GR word list (no hunspell binary needed; downloaded to /tmp on first run).
// Usage: node /mnt/project-files/tools/philosophers/check.js /mnt/project-files/app/library/philosophers/<id>.json ...
// Reports schema problems, cites without a source, quiz answers not among options, final-ν slips, double or missing
// accents, Latin letters inside Greek words, words unknown to el_GR (proper names and glossed forms excepted),
// and words the tap lookup cannot resolve (MISS) or only stem-guesses (GUESS). Exit code 1 on problems or misses.
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
const DIC = "/tmp/el_GR.dic";
if (!fs.existsSync(DIC)) cp.execSync(`curl -sSfL -o ${DIC} https://raw.githubusercontent.com/LibreOffice/dictionaries/master/el_GR/el_GR.dic`);
const words = new Set(new TextDecoder("iso-8859-7").decode(fs.readFileSync(DIC)).split("\n").slice(1).map((l) => l.split("/")[0].trim()));
const tok = (s) => String(s).match(/[Ͱ-Ͽἀ-῿]+(?:['’])?/g) || [];
const ACC = /[άέήίόύώΐΰΆΈΉΊΌΎΏ]/g, VOW = /[αεηιουωάέήίόύώϊϋΐΰ]/gi;
const ENCL = new Set(["με", "σε", "μου", "σου", "του", "της", "μας", "σας", "τους", "τον", "την", "το", "τα", "τις", "τη"]);
let bad = 0;
for (const f of process.argv.slice(2)) {
  let c; try { c = JSON.parse(fs.readFileSync(f)); } catch (e) { console.log(`${f}: INVALID JSON ${e.message}`); bad++; continue; }
  const probs = [], warn = [];
  for (const k of ["id", "el", "title", "level", "summary_en", "sections", "grammar", "terms", "gloss", "questions", "vocab", "sources"]) if (!(k in c)) probs.push("missing key " + k);
  const srcN = new Set((c.sources || []).map((s) => s.n)), used = new Set();
  for (const s of c.sources || []) if (!/^https?:\/\//.test(s.url || "")) probs.push(`source ${s.n} has no url`);
  const greek = [];
  const finalN = (s, where) => {
    const keep = /^([αεηιουωάέήίόύώϊϋΐΰ]|κ|π|τ|ξ|ψ|γκ|μπ|ντ|τσ|τζ)/i;
    const re = /(^|[\s«(“"])(τη|στη|την|στην|μη|μην|δε|δεν|αυτή|αυτήν|καμιά|καμιάν)\s+([Ͱ-Ͽἀ-῿]+)/gi; let m;
    while ((m = re.exec(s))) {
      const a = m[2].toLowerCase(), w = m[3].toLowerCase().normalize("NFC"), hasN = a.endsWith("ν"), needs = keep.test(w);
      if (["την", "στην", "μην", "δεν"].includes(a) && hasN && !needs && !["δεν", "μην"].includes(a)) warn.push(`${where}: "${m[2]} ${m[3]}" → drop ν`);
      if (["τη", "στη", "μη", "δε"].includes(a) && needs && !(a === "δε" && /^(ουκ|ουχ|ου$)/.test(w)) && !(a.toLowerCase() === "μη" && /^(ον|όν|όντα|όντος|ανθρώπιν|αντίφασ|είναι)/i.test(m[3]))) warn.push(`${where}: "${m[2]} ${m[3]}" → add ν`);
    }
  };
  (c.sections || []).forEach((s, i) => {
    if (!s.el || !s.en) probs.push(`section ${i} lacks el/en heading`);
    greek.push(s.el);
    (s.paras || []).forEach((p, j) => {
      if (!p.el || !p.en) probs.push(`section ${i} para ${j} lacks el/en`);
      if (!(p.cite || []).length) probs.push(`section ${i} para ${j} has no cite`);
      for (const n of p.cite || []) { used.add(n); if (!srcN.has(n)) probs.push(`section ${i} para ${j} cites [${n}] with no source`); }
      greek.push(p.el); finalN(p.el || "", `${s.id}#${j}`);
    });
  });
  for (const n of srcN) if (!used.has(n)) warn.push(`source [${n}] is never cited`);
  (c.questions || []).forEach((q, i) => { greek.push(q.q, ...(q.options || [])); if (!(q.options || []).includes(q.answer)) probs.push(`question ${i}: answer not among options`); });
  (c.grammar || []).forEach((g) => { greek.push(g.el || ""); (g.examples || []).forEach((x) => { greek.push(x.el); finalN(x.el || "", "grammar"); }); });
  (c.terms || []).forEach((t) => { greek.push(t.el, t.def_el); finalN(t.def_el || "", "term"); });
  greek.push(...(c.vocab || []));
  if (c.image) greek.push(c.image.caption);
  const ctx = c.gloss || {}, MISS = new Set(), GUESS = new Set(), spell = new Set(), acc = new Set();
  for (const t of greek) {
    if (/[A-Za-z][Ͱ-Ͽ]|[Ͱ-Ͽ][A-Za-z]/.test(t || "")) probs.push("mixed Latin/Greek letters: " + t.match(/\S*([A-Za-z][Ͱ-Ͽ]|[Ͱ-Ͽ][A-Za-z])\S*/)[0]);
    const toks = tok(t || "");
    toks.forEach((w0, i) => {
      const w = w0.replace(/['’]$/, ""), r = L.lookup(index, w, ctx);
      if (!r) MISS.add(w); else if (r[0].how === "guess") GUESS.add(`${w}→${r[0].lemma}`);
      const na = (w.match(ACC) || []).length, nv = (w.toLowerCase().match(VOW) || []).length;
      if (na > 1 && !(na === 2 && ENCL.has((toks[i + 1] || "").toLowerCase()))) acc.add(w + " (2 accents)");
      if (!na && nv > 1 && w === w.toLowerCase() && !/['’]$/.test(w0) && !words.has(w)) acc.add(w + " (no accent)");
      if (!words.has(w) && !words.has(w.toLowerCase()) && !(w in ctx) && !/^[Α-ΩΆ-Ώ]/.test(w) && !/['’]$/.test(w0)) spell.add(w);
    });
  }
  bad += probs.length + MISS.size;
  console.log(`${path.basename(f)}: ${probs.length} problems, ${MISS.size} lookup misses, ${GUESS.size} guesses, ${warn.length} warnings, ${acc.size} accent, ${spell.size} unknown to el_GR`);
  for (const p of probs) console.log("  PROBLEM: " + p);
  if (MISS.size) console.log("  MISS: " + [...MISS].join(" "));
  if (GUESS.size) console.log("  GUESS: " + [...GUESS].join(" "));
  for (const w of warn) console.log("  WARN: " + w);
  if (acc.size) console.log("  ACCENT: " + [...acc].join(", "));
  if (spell.size) console.log("  SPELL?: " + [...spell].join(" "));
}
process.exitCode = bad ? 1 : 0;
