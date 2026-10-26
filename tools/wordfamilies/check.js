// Accuracy checks for the word-family and confusables shelves (library/families, library/confusables).
// Based on tools/philosophers/check.js: el_GR spelling (LibreOffice word list), final-ν, double/missing accents,
// Latin letters inside Greek words, and words the tap lookup cannot resolve (MISS) or only stem-guesses (GUESS).
// Usage: node tools/wordfamilies/check.js library/families/*.json library/confusables/*.json
// Gap-fill distractors in the homophones chapter are deliberate misspellings and are not spell-checked.
const fs = require("fs"), path = require("path"), cp = require("child_process");
const APP = path.resolve(__dirname, "..", ".."), D = APP + "/data/";
const L = require(APP + "/lookup.js");
const lex = [], seen = new Set();
for (const f of ["core-1000.json", "core-3000.json"]) for (const e of JSON.parse(fs.readFileSync(D + "lexicon/" + f))) if (!seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); }
for (const e of JSON.parse(fs.readFileSync(D + "colloquial/colloquial-lexicon.json"))) if (!seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); }
const irr = JSON.parse(fs.readFileSync(D + "grammar/verbs-holton.json"))["irregular_verbs_6.25"].verbs;
const J = (p) => fs.existsSync(p) ? JSON.parse(fs.readFileSync(p)) : {};
const index = L.build(lex, { ...J(D + "lexicon/names.json"), ...J(D + "colloquial/colloquial-lookup.json"), ...J(APP + "/lessons/lookup-gloss.json"), ...J(APP + "/lessons/lookup-extra.json") }, irr, J(D + "lexicon/forms-index.json").forms || {});
const DIC = "/tmp/el_GR.dic";
if (!fs.existsSync(DIC)) cp.execSync(`curl -sSfL -o ${DIC} https://raw.githubusercontent.com/LibreOffice/dictionaries/master/el_GR/el_GR.dic`);
const words = new Set(new TextDecoder("iso-8859-7").decode(fs.readFileSync(DIC)).split("\n").slice(1).map((l) => l.split("/")[0].trim()));
const tok = (s) => String(s).match(/[Ͱ-Ͽἀ-῿]+(?:['’])?/g) || [];
const ACC = /[άέήίόύώΐΰΆΈΉΊΌΎΏ]/g, VOW = /[αεηιουωάέήίόύώϊϋΐΰ]/gi;
const ENCL = new Set(["με", "σε", "μου", "σου", "του", "της", "μας", "σας", "τους", "τον", "την", "το", "τα", "τις", "τη"]);
let bad = 0;
function strings(o, out, skipKeys) {
  if (typeof o === "string") out.push(o);
  else if (Array.isArray(o)) o.forEach((x) => strings(x, out, skipKeys));
  else if (o && typeof o === "object") for (const [k, v] of Object.entries(o)) if (!skipKeys.has(k)) strings(v, out, skipKeys);
  return out;
}
for (const f of process.argv.slice(2)) {
  if (f.endsWith("index.json")) continue;
  const c = JSON.parse(fs.readFileSync(f)), warn = [];
  const skip = new Set(["gloss", "id", "file", ...(c.id === "homophones" || c.id === "small-words" ? ["o"] : [])]);
  const greek = strings(c, [], skip);
  for (const s of greek) {
    const re = /(^|[\s«(“"*])(τη|στη|την|στην|μη|μην|δε|δεν|αυτή|αυτήν)\s+([Ͱ-Ͽἀ-῿]+)/gi; let m;
    while ((m = re.exec(s))) {
      const a = m[2].toLowerCase(), w = m[3].toLowerCase(), needs = /^([αεηιουωάέήίόύώϊϋΐΰ]|κ|π|τ|ξ|ψ|γκ|μπ|ντ|τσ|τζ)/i.test(w);
      if (["την", "στην"].includes(a) && !needs) warn.push(`"${m[2]} ${m[3]}" → drop ν`);
      if (["τη", "στη", "μη", "δε"].includes(a) && needs) warn.push(`"${m[2]} ${m[3]}" → add ν`);
    }
  }
  const ctx = c.gloss || {}, MISS = new Set(), GUESS = new Set(), spell = new Set(), acc = new Set(), probs = [];
  for (const t of greek) {
    if (/[A-Za-z][Ͱ-Ͽ]|[Ͱ-Ͽ][A-Za-z]/.test(t)) probs.push("mixed Latin/Greek letters: " + t.match(/\S*([A-Za-z][Ͱ-Ͽ]|[Ͱ-Ͽ][A-Za-z])\S*/)[0]);
    const toks = tok(t);
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
  console.log(`${path.basename(f)}: ${probs.length} problems, ${MISS.size} lookup misses, ${GUESS.size} guesses, ${warn.length} final-ν, ${acc.size} accent, ${spell.size} unknown to el_GR`);
  for (const p of probs) console.log("  PROBLEM: " + p);
  if (MISS.size) console.log("  MISS: " + [...MISS].join(" "));
  if (GUESS.size) console.log("  GUESS: " + [...GUESS].join(" "));
  for (const w of warn) console.log("  ν: " + w);
  if (acc.size) console.log("  ACCENT: " + [...acc].join(", "));
  if (spell.size) console.log("  SPELL?: " + [...spell].join(" "));
}
process.exitCode = bad ? 1 : 0;
