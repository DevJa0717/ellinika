// Checks a news digest issue (library/digest/<date>.json). Adapted from tools/philosophers/check.js and the
// 2026-10-25 audit checks: schema, quiz answers among options, sources with URLs, final-ν slips, double/missing accents,
// Latin letters inside Greek words, words unknown to the LibreOffice el_GR list (proper names and glossed forms
// excepted), and words the tap lookup cannot resolve (MISS) or only stem-guesses (GUESS).
// Paths are relative to the repo, so it runs in any clone: node deploy/news/check_issue.js library/digest/2026-10-26.json
// --misses prints only the missing forms, one per line (build_issue.py uses it to list what still needs a gloss).
// Exit code 1 on problems or misses.
const fs = require("fs"), path = require("path"), cp = require("child_process");
const ROOT = path.resolve(__dirname, "../.."), D = ROOT + "/data/";
const L = require(ROOT + "/lookup.js");
const lex = [], seen = new Set();
for (const f of fs.readdirSync(D + "lexicon").filter((f) => /^core-.*\.json$/.test(f)).sort()) {
  const d = JSON.parse(fs.readFileSync(D + "lexicon/" + f)); for (const e of Array.isArray(d) ? d : d.entries) if (!seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); }
}
for (const e of JSON.parse(fs.readFileSync(D + "colloquial/colloquial-lexicon.json"))) if (!seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); }
const irr = JSON.parse(fs.readFileSync(D + "grammar/verbs-holton.json"))["irregular_verbs_6.25"].verbs;
const J = (p) => fs.existsSync(p) ? JSON.parse(fs.readFileSync(p)) : {};
const extra = { ...J(ROOT + "/lessons/lookup-gloss.json"), ...J(ROOT + "/lessons/lookup-extra.json") };
const index = L.build(lex, { ...J(D + "lexicon/names.json"), ...J(D + "colloquial/colloquial-lookup.json"), ...extra }, irr, J(D + "lexicon/forms-index.json").forms || {});
const DIC = process.env.EL_DIC || "/tmp/el_GR.dic";
let words = null;
try {
  if (!fs.existsSync(DIC)) cp.execSync(`curl -sSfL -o ${DIC} https://raw.githubusercontent.com/LibreOffice/dictionaries/master/el_GR/el_GR.dic`, { stdio: "ignore" });
  words = new Set(new TextDecoder("iso-8859-7").decode(fs.readFileSync(DIC)).split("\n").slice(1).map((l) => l.split("/")[0].trim()));
} catch (e) { console.log("(el_GR word list not available: spelling check skipped)"); }
const tok = (s) => String(s).match(/[Ͱ-Ͽἀ-῿]+(?:['’])?/g) || [];
const ACC = /[άέήίόύώΐΰΆΈΉΊΌΎΏ]/g, VOW = /[αεηιουωάέήίόύώϊϋΐΰ]/gi;
const ENCL = new Set(["με", "σε", "μου", "σου", "του", "της", "μας", "σας", "τους", "τον", "την", "το", "τα", "τις", "τη"]);
const LEVELS = ["B1", "B2", "C1"], SECTIONS = new Set(["ellada", "europi", "kosmos", "oikonomia", "epistimi", "politismos", "athlitismos"]);
const finalN = (s, where, warn) => {
  const keep = /^([αεηιουωάέήίόύώϊϋΐΰ]|κ|π|τ|ξ|ψ|γκ|μπ|ντ|τσ|τζ)/i;
  const re = /(^|[\s«(“"])(τη|στη|την|στην|μη|μην|δε|αυτή|αυτήν|καμιά|καμιάν)\s+([Ͱ-Ͽἀ-῿]+)/gi; let m;
  while ((m = re.exec(s))) {
    const a = m[2].toLowerCase(), w = m[3].toLowerCase().normalize("NFC"), hasN = a.endsWith("ν"), needs = keep.test(w);
    if (["την", "στην", "αυτήν", "καμιάν"].includes(a) && hasN && !needs) warn.push(`${where}: "${m[2]} ${m[3]}" → drop ν`);
    if (["τη", "στη", "μη"].includes(a) && needs && !(a === "μη" && /^(όντα|ον$)/.test(w))) warn.push(`${where}: "${m[2]} ${m[3]}" → add ν`);
  }
};
const onlyMisses = process.argv.includes("--misses");
let bad = 0; const allMiss = new Set();
for (const f of process.argv.slice(2).filter((a) => !a.startsWith("--"))) {
  let iss; try { iss = JSON.parse(fs.readFileSync(f)); } catch (e) { console.log(`${f}: INVALID JSON ${e.message}`); bad++; continue; }
  const probs = [], warn = [], greek = [], ctx = iss.gloss || {}, ids = new Set();
  for (const k of ["id", "date", "date_el", "stories", "gloss"]) if (!(k in iss)) probs.push("missing key " + k);
  for (const s of iss.stories || []) {
    const W = s.id || "?";
    if (ids.has(s.id)) probs.push(`${W}: duplicate id`); ids.add(s.id);
    if (!/^[a-z0-9-]+$/.test(s.id || "")) probs.push(`${W}: id must be lowercase a-z, 0-9 and -`);
    if (!SECTIONS.has(s.section)) probs.push(`${W}: unknown section ${s.section}`);
    if (!(s.sources || []).length) probs.push(`${W}: no sources`);
    for (const src of s.sources || []) if (!/^https?:\/\//.test(src.url || "") || !src.name) probs.push(`${W}: source without name or url`);
    for (const lv of LEVELS) {
      const v = (s.levels || {})[lv];
      if (!v) { probs.push(`${W}: missing level ${lv}`); continue; }
      if (!v.el || !v.title) probs.push(`${W} ${lv}: headline el/title missing`);
      greek.push(v.el); finalN(v.el || "", `${W} ${lv} headline`, warn);
      if ((v.paras || []).length < 2) probs.push(`${W} ${lv}: fewer than 2 paragraphs`);
      (v.paras || []).forEach((p, j) => { if (!p.el || !p.en) probs.push(`${W} ${lv} para ${j}: el/en missing`); greek.push(p.el); finalN(p.el || "", `${W} ${lv} #${j}`, warn); });
      if ((v.glossary || []).length < 5) probs.push(`${W} ${lv}: glossary has fewer than 5 entries`);
      (v.glossary || []).forEach((g) => { if (!g.el || !g.en) probs.push(`${W} ${lv}: glossary entry without el/en`); greek.push(g.el); });
      if ((v.questions || []).length < 2) probs.push(`${W} ${lv}: fewer than 2 questions`);
      (v.questions || []).forEach((q, i) => {
        greek.push(q.q, ...(q.options || []));
        if (!(q.options || []).includes(q.answer)) probs.push(`${W} ${lv} question ${i}: answer not among options`);
        if (new Set(q.options).size !== (q.options || []).length) probs.push(`${W} ${lv} question ${i}: duplicate options`);
      });
      const words = (v.paras || []).map((p) => p.el).join(" ").split(/\s+/).length;
      const min = { B1: 50, B2: 100, C1: 150 }[lv];
      if (words < min) warn.push(`${W} ${lv}: only ${words} Greek words (aim for ${min}+)`);
    }
    if (s.grammar) (s.grammar.examples || []).forEach((x) => { greek.push(x.el); finalN(x.el || "", `${W} grammar`, warn); });
    greek.push(...(s.vocab || []));
  }
  const MISS = new Set(), GUESS = new Set(), spell = new Set(), acc = new Set();
  for (const t of greek) {
    if (/[A-Za-z][Ͱ-Ͽ]|[Ͱ-Ͽ][A-Za-z]/.test(t || "")) probs.push("mixed Latin/Greek letters: " + t.match(/\S*([A-Za-z][Ͱ-Ͽ]|[Ͱ-Ͽ][A-Za-z])\S*/)[0]);
    const toks = tok(t || "");
    toks.forEach((w0, i) => {
      const w = w0.replace(/['’]$/, ""), r = L.lookup(index, w, ctx);
      if (!r) MISS.add(w); else if (r[0].how === "guess") GUESS.add(`${w}→${r[0].lemma}`);
      const na = (w.match(ACC) || []).length, nv = (w.toLowerCase().match(VOW) || []).length;
      if (na > 1 && !(na === 2 && ENCL.has((toks[i + 1] || "").toLowerCase()))) acc.add(w + " (2 accents)");
      if (words && !na && nv > 1 && w === w.toLowerCase() && !/['’]$/.test(w0) && !words.has(w)) acc.add(w + " (no accent)");
      if (words && !words.has(w) && !words.has(w.toLowerCase()) && !(w in ctx) && !/^[Α-ΩΆ-Ώ]/.test(w) && !/['’]$/.test(w0)) spell.add(w);
    });
  }
  MISS.forEach((m) => allMiss.add(m));
  bad += probs.length + MISS.size;
  if (onlyMisses) continue;
  console.log(`${path.basename(f)}: ${(iss.stories || []).length} stories, ${probs.length} problems, ${MISS.size} lookup misses, ${GUESS.size} guesses, ${warn.length} warnings, ${acc.size} accent, ${spell.size} unknown to el_GR`);
  for (const p of probs) console.log("  PROBLEM: " + p);
  if (MISS.size) console.log("  MISS: " + [...MISS].join(" "));
  if (GUESS.size) console.log("  GUESS: " + [...GUESS].join(" "));
  for (const w of warn) console.log("  WARN: " + w);
  if (acc.size) console.log("  ACCENT: " + [...acc].join(", "));
  if (spell.size) console.log("  SPELL?: " + [...spell].join(" "));
}
if (onlyMisses) console.log([...allMiss].join("\n"));
process.exitCode = bad ? 1 : 0;
