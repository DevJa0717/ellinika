// Tap-lookup coverage for the history reader: prints Greek words with no lookup hit, per chapter (chapter gloss counts).
const fs = require("fs"), path = require("path");
const APP = "/mnt/project-files/app/", D = "/mnt/project-files/data/";
const L = require(APP + "lookup.js");
const lex = [], seen = new Set();
for (const f of fs.readdirSync(D + "lexicon").filter((f) => /^core-.*\.json$/.test(f)).sort()) { const d = JSON.parse(fs.readFileSync(D + "lexicon/" + f)); for (const e of Array.isArray(d) ? d : d.entries) if (!seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); } }
for (const e of JSON.parse(fs.readFileSync(D + "colloquial/colloquial-lexicon.json"))) if (!seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); }
const irr = JSON.parse(fs.readFileSync(D + "grammar/verbs-holton.json"))["irregular_verbs_6.25"].verbs;
const opt = (p) => (fs.existsSync(p) ? JSON.parse(fs.readFileSync(p)) : {});
const extra = { ...opt(APP + "lessons/lookup-gloss.json"), ...opt(APP + "lessons/lookup-extra.json") };
const index = L.build(lex, { ...opt(D + "lexicon/names.json"), ...opt(D + "colloquial/colloquial-lookup.json"), ...extra }, irr, opt(D + "lexicon/forms-index.json").forms || {});
const skip = new Set(["en", "def_en", "title", "summary_en", "why", "text", "url", "file", "credit", "license", "source", "caption_en", "gloss"]);
let total = 0;
const files = process.argv.slice(2).length ? process.argv.slice(2) : fs.readdirSync(APP + "library/istoria").filter((f) => /^e\d/.test(f)).map((f) => APP + "library/istoria/" + f);
for (const f of files) {
  const ch = JSON.parse(fs.readFileSync(f)), texts = [];
  const walk = (o, k) => { if (typeof o === "string") { if (!skip.has(k)) texts.push(o); } else if (Array.isArray(o)) o.forEach((x) => walk(x, k)); else if (o && typeof o === "object") for (const [kk, v] of Object.entries(o)) if (!skip.has(kk)) walk(v, kk); };
  walk(ch);
  const miss = new Set(), guess = new Set();
  for (const t of texts) for (const w of t.match(/[Ͱ-Ͽἀ-῿]+/g) || []) { const r = L.lookup(index, w, ch.gloss || {}); if (!r) miss.add(w); else if (r[0].how === "guess") guess.add(w + "→" + r[0].lemma); }
  total += miss.size;
  console.log(path.basename(f) + ": " + miss.size + " missing" + (miss.size ? "\n  MISS: " + [...miss].join(" ") : "") + (guess.size ? "\n  GUESS: " + [...guess].join(" ") : ""));
}
console.log("missing total:", total);
