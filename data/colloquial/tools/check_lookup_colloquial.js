// Colloquial variant: also loads data/colloquial/colloquial-lexicon.json. Usage: node check_lookup_colloquial.js [--all] <lesson files>
// Coverage check for the word lookup. Usage (from app/): node tools/check_lookup.js [--all] lessons/a2-x.json ...
// Default checks reading texts and video subtitles (blocks of type reading/video); --all checks every Greek string in the file.
// Prints words with no lookup hit ("MISS") and words matched only by a stem guess ("GUESS").
const fs = require("fs"), path = require("path");
const L = require("/mnt/project-files/app/lookup.js");
const D = "/mnt/project-files/data/";
const lex = [];
const seen = new Set();
for (const f of fs.readdirSync(D + "lexicon").filter((f) => /^core-.*\.json$/.test(f)).sort()) {
  const d = JSON.parse(fs.readFileSync(D + "lexicon/" + f)); for (const e of Array.isArray(d) ? d : d.entries) if (!seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); }
}
{ const c = JSON.parse(fs.readFileSync(D + "colloquial/colloquial-lexicon.json")); for (const e of c) if (!seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); } }
const irr = JSON.parse(fs.readFileSync(D + "grammar/verbs-holton.json"))["irregular_verbs_6.25"].verbs;
const more = fs.existsSync(path.join("/mnt/project-files/app/lessons/lookup-gloss.json")) ? JSON.parse(fs.readFileSync(path.join("/mnt/project-files/app/lessons/lookup-gloss.json"))) : {};
const extra = { ...more, ...JSON.parse(fs.readFileSync(path.join("/mnt/project-files/app/lessons/lookup-extra.json"))) };
const opt = (f) => { const p = path.join(D + "lexicon", f); return fs.existsSync(p) ? JSON.parse(fs.readFileSync(p)) : {}; };
const cl = JSON.parse(fs.readFileSync(D + "colloquial/colloquial-lookup.json"));
const index = L.build(lex, { ...opt("names.json"), ...cl, ...extra }, irr, opt("forms-index.json").forms || {});
const all = process.argv.includes("--all");
const tok = (s) => String(s).match(/[Ͱ-Ͽἀ-῿]+(?:['’])?/g) || [];
let miss = 0, guess = 0;
for (const f of process.argv.slice(2).filter((a) => !a.startsWith("--"))) {
  let lesson = JSON.parse(fs.readFileSync(f));
  if (lesson.videos) lesson = { blocks: lesson.videos.map((v) => ({ ...v, type: "video" })) };
  const ctx = {}; const texts = [];
  const walk = (o) => { if (typeof o === "string") texts.push(o); else if (Array.isArray(o)) o.forEach(walk); else if (o && typeof o === "object") for (const [k, v] of Object.entries(o)) if (k !== "gloss" && k !== "en") walk(v); };
  for (const b of lesson.blocks || []) {
    if (b.gloss) Object.assign(ctx, b.gloss);
    if (b.type === "reading") texts.push(b.text, ...(b.questions || []).flatMap((q) => [q.prompt, ...(q.options || [])]));
    if (b.type === "video") texts.push(...(b.cues || []).map((c) => c.el));
  }
  if (all) walk(lesson);
  const out = { MISS: new Set(), GUESS: new Set() };
  for (const t of texts) for (const w of tok(t)) { const r = L.lookup(index, w, ctx); if (!r) out.MISS.add(w); else if (r[0].how === "guess") out.GUESS.add(`${w}→${r[0].lemma}`); }
  miss += out.MISS.size; guess += out.GUESS.size;
  console.log(`${f}: ${out.MISS.size} missing, ${out.GUESS.size} guessed`);
  if (out.MISS.size) console.log("  MISS: " + [...out.MISS].join(" "));
  if (out.GUESS.size) console.log("  GUESS: " + [...out.GUESS].join(" "));
}
process.exitCode = miss ? 1 : 0;
