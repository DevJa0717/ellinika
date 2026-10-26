// Accuracy check for the syntax guide (library/syntax/*.json) and the grammar cards (library/cards/*.json).
// Adapted from tools/philosophers/check.js: mixed scripts, double or missing accents, words unknown to the LibreOffice
// el_GR list, final-ν slips (τη/την, δε/δεν, μη/μην) and words the tap lookup cannot resolve. Wrong options of
// multiple-choice exercises are skipped, since they are wrong on purpose.
// Usage: node tools/syntax-cards/check.js library/syntax/*.json library/cards/*.json
const fs = require("fs"), path = require("path"), cp = require("child_process");
const APP = path.resolve(__dirname, "../.."), D = APP + "/data/";
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
const strs = (o, out) => {
  if (typeof o === "string") out.push(o);
  else if (Array.isArray(o)) o.forEach((x) => strs(x, out));
  else if (o && typeof o === "object") {
    if (o.type === "choice") { out.push(o.q, o.answer, o.why || ""); return; }
    for (const [k, v] of Object.entries(o)) if (!["href", "id", "file", "kind", "level", "type", "group"].includes(k)) strs(v, out);
  }
};
const keep = /^([αεηιουωάέήίόύώϊϋΐΰ]|κ|π|τ|ξ|ψ|γκ|μπ|ντ|τσ|τζ)/i;
for (const f of process.argv.slice(2)) {
  if (/(index|gloss)\.json$/.test(f)) continue;
  const c = JSON.parse(fs.readFileSync(f)), greek = [], warn = [], probs = [];
  strs(c, greek);
  for (const s0 of greek) {
    const s = s0.replace(/\*+/g, "");
    const re = /(^|[\s«(“"])(τη|στη|μη|δε)\s+([Ͱ-Ͽἀ-῿]+)/gi; let m;
    while ((m = re.exec(s))) if (keep.test(m[3].toLowerCase().normalize("NFC"))) warn.push(`"${m[2]} ${m[3]}" → add ν`);
    const re2 = /(^|[\s«(“"])(την|στην)\s+([Ͱ-Ͽἀ-῿]+)/gi;
    while ((m = re2.exec(s))) if (!keep.test(m[3].toLowerCase().normalize("NFC"))) warn.push(`"${m[2]} ${m[3]}" → drop ν`);
  }
  const ctx = J(APP + "/library/syntax/gloss.json"), MISS = new Set(), GUESS = new Set(), spell = new Set(), acc = new Set();
  for (const t0 of greek) {
    const t = t0.replace(/\*+/g, "");
    if (/[A-Za-z][Ͱ-Ͽ]|[Ͱ-Ͽ][A-Za-z]/.test(t)) probs.push("mixed Latin/Greek letters: " + t.match(/\S*([A-Za-z][Ͱ-Ͽ]|[Ͱ-Ͽ][A-Za-z])\S*/)[0]);
    const toks = tok(t);
    toks.forEach((w0, i) => {
      const w = w0.replace(/['’]$/, "");
      if (/^-|-$/.test(w) || w.length < 2 && !/[Α-Ωα-ω]/.test(w)) return;
      const r = L.lookup(index, w, ctx);
      if (!r) MISS.add(w); else if (r[0].how === "guess") GUESS.add(`${w}→${r[0].lemma}`);
      const na = (w.match(ACC) || []).length, nv = (w.toLowerCase().match(VOW) || []).length;
      if (na > 1 && !(na === 2 && ENCL.has((toks[i + 1] || "").toLowerCase()))) acc.add(w + " (2 accents)");
      if (!na && nv > 1 && w === w.toLowerCase() && !/['’]$/.test(w0) && !words.has(w)) acc.add(w + " (no accent)");
      if (!words.has(w) && !words.has(w.toLowerCase()) && !/^[Α-ΩΆ-Ώ]/.test(w) && !/['’]$/.test(w0)) spell.add(w);
    });
  }
  bad += probs.length;
  console.log(`${path.basename(f)}: ${probs.length} problems, ${MISS.size} lookup misses, ${GUESS.size} guesses, ${warn.length} final-ν, ${acc.size} accent, ${spell.size} unknown to el_GR`);
  for (const p of probs) console.log("  PROBLEM: " + p);
  if (MISS.size) console.log("  MISS: " + [...MISS].join(" "));
  if (GUESS.size) console.log("  GUESS: " + [...GUESS].join(" "));
  if (warn.length) console.log("  NU: " + [...new Set(warn)].join(", "));
  if (acc.size) console.log("  ACCENT: " + [...acc].join(", "));
  if (spell.size) console.log("  SPELL?: " + [...spell].join(" "));
}
process.exitCode = bad ? 1 : 0;
