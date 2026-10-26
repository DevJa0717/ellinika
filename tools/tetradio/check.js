// Checks the writing workbook (library/tetradio/*.json). Adapted from tools/philosophers/check.js:
// final-ν slips, double or missing accents, Latin letters inside Greek words, words unknown to the LibreOffice el_GR list
// (proper names and glossed forms excepted), words the tap lookup cannot resolve (MISS) or only stem-guesses (GUESS),
// and drill answers that are not among the options. Usage: node tools/tetradio/check.js [library/tetradio/*.json]
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
const DIC = "/tmp/el_GR.dic";
if (!fs.existsSync(DIC)) cp.execSync(`curl -sSfL -o ${DIC} https://raw.githubusercontent.com/LibreOffice/dictionaries/master/el_GR/el_GR.dic`);
const words = new Set(new TextDecoder("iso-8859-7").decode(fs.readFileSync(DIC)).split("\n").slice(1).map((l) => l.split("/")[0].trim()));
const tok = (s) => String(s).match(/[Ͱ-Ͽἀ-῿]+(?:['’])?/g) || [];
const ACC = /[άέήίόύώΐΰΆΈΉΊΌΎΏ]/g, VOW = /[αεηιουωάέήίόύώϊϋΐΰ]/gi;
const ENCL = new Set(["με", "σε", "μου", "σου", "του", "της", "μας", "σας", "τους", "τον", "την", "το", "τα", "τις", "τη"]);
const files = process.argv.slice(2).length ? process.argv.slice(2) : fs.readdirSync(ROOT + "/library/tetradio").filter((f) => f.endsWith(".json") && f !== "index.json").map((f) => ROOT + "/library/tetradio/" + f);
let bad = 0;
for (const f of files) {
  const c = JSON.parse(fs.readFileSync(f)), probs = [], warn = [], strs = [];
  const walk = (v, k) => { if (typeof v === "string") { if (k !== "gloss") strs.push(v); } else if (Array.isArray(v)) v.forEach((x) => walk(x, k)); else if (v && typeof v === "object") for (const [kk, vv] of Object.entries(v)) if (kk !== "gloss" && kk !== "wrong") walk(vv, kk); };
  walk(c, "");
  for (const d of c.drills || []) if (!d.options.includes(d.answer)) probs.push("drill answer not among options: " + d.q);
  const finalN = (s) => {
    const keep = /^([αεηιουωάέήίόύώϊϋΐΰ]|κ|π|τ|ξ|ψ|γκ|μπ|ντ|τσ|τζ)/i;
    const re = /(^|[\s«(“"])(τη|στη|την|στην|μη|μην|δε|δεν|αυτή|αυτήν|καμιά|καμιάν)\s+([Ͱ-Ͽἀ-῿]+)/gi; let m;
    while ((m = re.exec(s))) {
      const a = m[2].toLowerCase(), w = m[3].toLowerCase().normalize("NFC"), hasN = a.endsWith("ν"), needs = keep.test(w);
      if (["την", "στην"].includes(a) && hasN && !needs) warn.push(`"${m[2]} ${m[3]}" → drop ν`);
      if (a === "μην" && !needs) warn.push(`"${m[2]} ${m[3]}" → μη`);
      if (["τη", "στη", "μη"].includes(a) && needs) warn.push(`"${m[2]} ${m[3]}" → add ν`);
    }
  };
  const ctx = c.gloss || {}, MISS = new Set(), GUESS = new Set(), spell = new Set(), acc = new Set();
  for (const t of strs) {
    finalN(t);
    if (/[A-Za-z][Ͱ-Ͽ]|[Ͱ-Ͽ][A-Za-z]/.test(t)) probs.push("mixed Latin/Greek letters: " + t.match(/\S*([A-Za-z][Ͱ-Ͽ]|[Ͱ-Ͽ][A-Za-z])\S*/)[0]);
    const toks = tok(t);
    toks.forEach((w0, i) => {
      const w = w0.replace(/['’]$/, ""), r = L.lookup(index, w, ctx);
      if (!r) MISS.add(w); else if (r[0].how === "guess") GUESS.add(`${w}→${r[0].lemma}`);
      const na = (w.match(ACC) || []).length, nv = (w.toLowerCase().match(VOW) || []).length;
      if (na > 1 && !(na === 2 && ENCL.has((toks[i + 1] || "").toLowerCase()))) acc.add(w + " (2 accents)");
      if (!na && nv > 1 && w === w.toLowerCase() && !/['’]$/.test(w0) && !words.has(w)) acc.add(w + " (no accent)");
      const w1 = na === 2 && ENCL.has((toks[i + 1] || "").toLowerCase()) ? w.replace(/([άέήίόύώ])(?!.*[άέήίόύώ])/, (x) => "αεηιουω"["άέήίόύώ".indexOf(x)]) : w;
      if (!words.has(w1) && !words.has(w1.toLowerCase()) && !(w in ctx) && !/^[Α-ΩΆ-Ώ]/.test(w) && !/['’]$/.test(w0)) spell.add(w);
    });
  }
  bad += probs.length + MISS.size;
  console.log(`${path.basename(f)}: ${probs.length} problems, ${MISS.size} misses, ${GUESS.size} guesses, ${warn.length} ν-warnings, ${acc.size} accent, ${spell.size} unknown to el_GR`);
  for (const p of probs) console.log("  PROBLEM: " + p);
  if (MISS.size) console.log("  MISS: " + [...MISS].join(" "));
  if (GUESS.size) console.log("  GUESS: " + [...GUESS].join(" "));
  for (const w of new Set(warn)) console.log("  WARN: " + w);
  if (acc.size) console.log("  ACCENT: " + [...acc].join(", "));
  if (spell.size) console.log("  SPELL?: " + [...spell].join(" "));
}
process.exitCode = bad ? 1 : 0;
