#!/usr/bin/env node
// Content audit for the whole app (2026-11-05, "Validate all content end to end").
// Format-agnostic: walks every string of every JSON file given (files or directories), keeps the Greek ones, and checks
//   spelling against the LibreOffice el_GR list (828k full forms) + the project's own vetted forms,
//   accents (two accents outside proparoxytone+enclitic, polysyllables without an accent, accented clitics),
//   final sigma (ς inside a word, σ at the end), mixed Latin/Greek letters, final-ν (την/στην/τη/στη/δεν/μην),
//   a Latin "?" in Greek text (Greek uses ";"), doubled words ("και και"), space before punctuation,
//   unbalanced «» and (), and words the tap lookup cannot resolve.
// Usage: node tools/audit/audit.js [--json out.json] [--md out.md] [--quiet] [--no-lookup] <file|dir> ...
//        (no paths = every content folder: library lessons data/c1 data/colloquial data/grammar)
// Exit code 1 when any HARD finding is left (mixed script, final sigma, doubled word, "?" in Greek, invalid JSON).
// Words a file defines in a "gloss" object, capitalised words (names) and dialect/ancient material (paths in SKIP_SPELL)
// are not spell-checked. Allow-list: tools/audit/allow.txt (one word per line, # comments).
const fs = require("fs"), path = require("path"), cp = require("child_process");
const ROOT = path.resolve(__dirname, "../..");
const D = ROOT + "/data/";
const args = process.argv.slice(2);
const opt = (k) => { const i = args.indexOf(k); if (i < 0) return null; const v = args[i + 1]; args.splice(i, 2); return v; };
const flag = (k) => { const i = args.indexOf(k); if (i < 0) return false; args.splice(i, 1); return true; };
const JSON_OUT = opt("--json"), MD_OUT = opt("--md"), QUIET = flag("--quiet"), NOLOOK = flag("--no-lookup");
const targets = args.length ? args : ["library", "lessons", "data/c1", "data/colloquial", "data/grammar"];

// ---------- dictionary ----------
const DIC = process.env.EL_DIC || "/tmp/el_GR.dic";
if (!fs.existsSync(DIC)) cp.execSync(`curl -sSfL -o ${DIC} https://raw.githubusercontent.com/LibreOffice/dictionaries/master/el_GR/el_GR.dic`);
const dict = new Set(new TextDecoder("iso-8859-7").decode(fs.readFileSync(DIC)).split("\n").slice(1).map((l) => l.split("/")[0].trim()));
const J = (p) => { try { return JSON.parse(fs.readFileSync(p)); } catch { return {}; } };
const proj = new Set();                       // vetted project forms (word lists were read entry by entry on 2026-10-25)
const lex = [], seen = new Set();
for (const f of fs.readdirSync(D + "lexicon").filter((f) => /^core-.*\.json$/.test(f)).sort()) {
  const d = J(D + "lexicon/" + f); for (const e of Array.isArray(d) ? d : d.entries || []) if (!seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); proj.add(e.lemma); }
}
for (const e of [].concat(J(D + "colloquial/colloquial-lexicon.json"))) if (e && e.lemma && !seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); }
const forms = J(D + "lexicon/forms-index.json").forms || {};
for (const k of Object.keys(forms)) proj.add(k);
const allowFile = path.join(__dirname, "allow.txt");
const allow = new Set(fs.existsSync(allowFile) ? fs.readFileSync(allowFile, "utf8").split("\n").map((l) => l.replace(/#.*/, "").trim()).filter(Boolean) : []);
const known = (w) => dict.has(w) || dict.has(w.toLowerCase()) || proj.has(w) || proj.has(w.toLowerCase()) || allow.has(w) || allow.has(w.toLowerCase());

// ---------- lookup ----------
let L = null, index = null;
if (!NOLOOK) {
  L = require(ROOT + "/lookup.js");
  const irr = J(D + "grammar/verbs-holton.json")["irregular_verbs_6.25"].verbs;
  const extra = { ...J(ROOT + "/lessons/lookup-gloss.json"), ...J(ROOT + "/lessons/lookup-extra.json") };
  index = L.build(lex, { ...J(D + "lexicon/names.json"), ...J(D + "colloquial/colloquial-lookup.json"), ...extra }, irr, forms);
}

// ---------- helpers ----------
const GR = /[Ͱ-Ͽἀ-῿]/, POLY = /[ἀ-῿]/;
const tok = (s) => s.match(/[Ͱ-Ͽἀ-῿]+(?:['’])?/g) || [];
const ACC = /[άέήίόύώΐΰΆΈΉΊΌΎΏ]/g, VOW = /[αεηιουω]/gi;
const strip = (w) => w.normalize("NFD").replace(/[̀-ͯ]/g, "").normalize("NFC");
// vowels counted as syllable nuclei (diphthongs αι ει οι ου υι αυ ευ count once)
const syll = (w) => { const s = strip(w.toLowerCase()).replace(/αι|ει|οι|ου|υι|αυ|ευ|ηυ/g, "a"); return (s.match(/[αεηιουωa]/g) || []).length; };
const ENCL = new Set(["με", "σε", "μου", "σου", "του", "της", "μας", "σας", "τους", "τον", "την", "το", "τα", "τις", "τη", "τες"]);
// never accented in monotonic (μού/μάς/σού… are left alone: the distinctive accent, Ο διευθυντής μού τηλεφώνησε, is correct)
const CLITIC_ACC = new Set(["τό", "τά", "τόν", "τίς", "μέ", "σέ", "νά", "θά", "καί", "γιά", "δέν", "μήν"]);
const SKIP_KEYS = new Set(["en", "url", "href", "credit", "license", "licence", "source", "file", "img", "src", "id", "slug", "audio", "video", "youtube", "author_en", "title_en", "summary_en", "note_en", "def_en", "why_en", "license_url", "listen"]);
const skipKey = (k) => SKIP_KEYS.has(k) || /_en$|^en_|url$/i.test(k);
// dialect, ancient, Katharevousa and deliberate-error material: no spelling/accent/final-ν verdicts, only hard checks
const SKIP_SPELL = [/library\/dialects\//, /library\/errors\//, /library\/classics\//, /data\/c1\/texts\//, /data\/c1\/videos\//, /lessons\/videos/, /dialect/, /slang/, /colloquial/, /library\/confusables\//, /data\/grammar\/.*holton/];
const ERROR_KEYS = /^(wrong|bad|error|incorrect|distractor|mistake|err|options|choices|before)$/i;

const HARD_DOUBLE = new Set(["το", "τα", "η", "ο", "οι", "και", "να", "θα", "σε", "από", "για", "την", "τον", "των", "τις", "στο", "στη", "στην", "στον", "με", "δεν", "που"]);
const findings = [];   // {file, path, kind, hard, text, word}
const unknown = new Map(); // word -> {n, files:Set, ex}
const add = (f, p, kind, hard, word, text) => findings.push({ file: f, path: p, kind, hard, word, text: (text || "").slice(0, 160) });

function checkString(file, jp, s0, ctx, lenient) {
  if (!GR.test(s0)) return;
  const s = s0.replace(/\*+/g, "");   // markdown emphasis inside words (**β**ράδυ, γράφ**ουν**)
  const greekShare = (s.match(/[Ͱ-Ͽἀ-῿]/g) || []).length / Math.max(1, (s.match(/[A-Za-zͰ-Ͽἀ-῿]/g) || []).length);
  const polytonic = POLY.test(s);
  // mixed script inside a word
  for (const m of s.matchAll(/\S*(?:[A-Za-z][Ͱ-Ͽἀ-῿]|[Ͱ-Ͽἀ-῿][A-Za-z])\S*/g)) {
    const w = m[0];
    if (/^(https?:|[a-z]+\.[a-z])/.test(w) || /[=<>{}]/.test(w)) continue;
    const ipa = /^\[|\]\W*$/.test(w) || /ipa|pronounc|translit|cluster/i.test(jp) || /^[a-zéə]/.test(w) && /[a-zé]/.test(w.replace(/[Ͱ-Ͽ]/g, "").slice(0, 3));
    add(file, jp, "mixed-script", !lenient && !ipa, w, s);
  }
  if (greekShare > 0.6) {
    for (const m of s.matchAll(/([^.!;:\n"“”()?]*)\?/g)) if (GR.test(m[1]) && !/[A-Za-z]/.test(m[1]) && !/https?:/.test(s)) { add(file, jp, "latin-question-mark", !lenient, m[1].trim().slice(-40) + "?", s); break; }
    for (const m of s.matchAll(/(^|[\s«(])([Ͱ-Ͽἀ-῿]{2,})\s+\2(?=[\s.,;!·»)]|$)/g)) if (!["πολύ", "σιγά", "λίγο", "κάτω", "πάνω", "ένα", "δυο", "γρήγορα", "όλο", "μέρα", "μόνο", "ναι", "όχι", "ώρα", "τώρα", "έλα", "αργά", "χέρι", "πότε", "άλλο", "ένας", "μια", "κοντά", "στάλα", "πέρα", "σπίτι", "πόρτα", "λέξη", "κομμάτι", "βήμα"].includes(m[2].toLowerCase())) add(file, jp, "doubled-word", !lenient && HARD_DOUBLE.has(m[2].toLowerCase()), m[2], s);
    if (/[Ͱ-Ͽἀ-῿] [,.;:!·](?![.\d])/.test(s) && !/ \.\.\./.test(s)) add(file, jp, "space-before-punct", false, "", s);
    const op = (s.match(/«/g) || []).length, cl = (s.match(/»/g) || []).length;
    if (op !== cl && s.length < 2000) add(file, jp, "unbalanced-quotes", false, `«${op} »${cl}`, s);
  }
  const toks = []; for (const m of s.matchAll(/[Ͱ-Ͽἀ-῿][Ͱ-Ͽἀ-῿\u0300-\u036f]*(?:['’])?/g)) toks.push({ w: m[0], at: m.index });
  toks.forEach(({ w: w0, at }, i) => {
    const apos = /['’]$/.test(w0), w = w0.replace(/['’]$/, "");
    if (/[\u0300-\u036f]/.test(w)) return; // phonetic/dialect spellings with combining marks (τσ̌ερί)
    const before = s[at - 1] || "", after = s[at + w0.length] || "";
    if (/[-‐‑–/]/.test(before) || /[-‐‑–]/.test(after) || before === "*" && after === "*" && w.length < 4) return; // stems, endings, syllables (αυ-το-κί-νη-το, -ησα)
    if (/ς./.test(w)) add(file, jp, "final-sigma", !lenient, w, s);
    if (/σ$/.test(w) && !apos && w.length > 1 && !/[.*_]/.test(after) && !/^(.)\1+$/i.test(w.toLowerCase().replace(/ς/g, "σ")) && !/^[τπ]?[τπσ]σ$|^τσ$/.test(w)) add(file, jp, "final-sigma", !lenient, w, s);
    if (polytonic || lenient) return;
    const na = (w.match(ACC) || []).length, ns = syll(w);
    const next = ((toks[i + 1] || {}).w || "").replace(/['’]$/, "").toLowerCase();
    if (na > 1 && !(na === 2 && (ENCL.has(next) || /^_+$/.test(s.slice(at + w0.length).trim().split(/\s/)[0] || "") || /answer|accept/.test(jp)))) add(file, jp, "two-accents", false, w, s);
    if (CLITIC_ACC.has(w) && !(w === "τί" || w === "πού")) add(file, jp, "accented-monosyllable", false, w, s);
    if (!na && ns > 1 && w === w.toLowerCase() && !apos && !known(w) && !(w in ctx)) add(file, jp, "no-accent", false, w, s);
    if (!known(w) && !(w in ctx) && !(w.toLowerCase() in ctx) && !/^[Α-ΩΆ-Ώ]/.test(w) && !apos && w.length > 1) {
      const u = unknown.get(w) || { n: 0, files: new Set(), ex: s.slice(0, 140), path: jp };
      u.n++; u.files.add(file); unknown.set(w, u);
    }
    if (index && !/(^|\.)(gloss|lookup|glossary)(\.|$)/i.test(jp) && !(after === "." && w.length <= 5)) { const r = L.lookup(index, w, ctx); if (!r) add(file, jp, "lookup-miss", false, w, s); }
  });
  if (!polytonic && !lenient) finalN(file, jp, s);
}

function finalN(file, jp, s) {
  const keep = /^([αεηιουωάέήίόύώϊϋΐΰ]|κ|π|τ|ξ|ψ|γκ|μπ|ντ|τσ|τζ)/i;
  const re = /(^|[\s«(“"])(τη|στη|την|στην|μη|μην|δε|δεν)\s+([Ͱ-Ͽ]+)/gi; let m;
  while ((m = re.exec(s))) {
    const a = m[2].toLowerCase(), w = m[3].toLowerCase(), hasN = a.endsWith("ν"), needs = keep.test(w);
    if ((a === "την" || a === "στην") && !needs) add(file, jp, "final-n", false, `${m[2]} ${m[3]} → drop ν`, s);
    if ((a === "τη" || a === "στη") && needs) add(file, jp, "final-n", false, `${m[2]} ${m[3]} → add ν`, s);
    if (a === "μη" && needs && /(εις|ει|ω|ώ|ουμε|ούμε|ετε|είτε|ουν|ούν|άς|άτε|σεις|ξεις|ψεις|ήσεις)$/.test(w) && !/^(ον|όν|όντα)/.test(w)) add(file, jp, "final-n", false, `${m[2]} ${m[3]} → add ν`, s);
    if (a === "δε" && needs && !/^(ουκ|ουχ)/.test(w)) add(file, jp, "final-n", false, `${m[2]} ${m[3]} → δεν`, s);
    void hasN;
  }
}

function collectGloss(o, ctx) {
  if (Array.isArray(o)) o.forEach((x) => collectGloss(x, ctx));
  else if (o && typeof o === "object") for (const [k, v] of Object.entries(o)) {
    if (/gloss|lookup|glossary|vocab/i.test(k) && v && typeof v === "object" && !Array.isArray(v)) for (const g of Object.keys(v)) ctx[g] = v[g];
    if (/gloss|glossary|vocab|terms/i.test(k) && Array.isArray(v)) for (const g of v) if (g && typeof g === "object") for (const kk of ["el", "lemma", "word", "gr"]) if (typeof g[kk] === "string") for (const t of tok(g[kk])) ctx[t.replace(/['’]$/, "")] = 1;
    collectGloss(v, ctx);
  }
}

function walk(file, o, jp, ctx, lenient) {
  if (typeof o === "string") return checkString(file, jp, o, ctx, lenient);
  if (Array.isArray(o)) return o.forEach((x, i) => walk(file, x, `${jp}[${i}]`, ctx, lenient));
  if (o && typeof o === "object") for (const [k, v] of Object.entries(o)) {
    if (skipKey(k)) continue;
    walk(file, v, jp ? `${jp}.${k}` : k, ctx, lenient || ERROR_KEYS.test(k));
  }
}

const files = [];
const SKIP_FILES = /forms-index|names\.json|lookup-(gloss|extra)|colloquial-lookup|offline|manifest|\/drills\/|lexicon\/build|wiktionary/;
const visit = (p) => { const st = fs.statSync(p); if (st.isDirectory()) for (const f of fs.readdirSync(p).sort()) visit(path.join(p, f)); else if (p.endsWith(".json") && !SKIP_FILES.test(p)) files.push(p); };
for (const t of targets) visit(path.resolve(ROOT, t));
let invalid = 0;
for (const f of files) {
  const rel = path.relative(ROOT, f);
  let o; try { o = JSON.parse(fs.readFileSync(f, "utf8")); } catch (e) { add(rel, "", "invalid-json", true, "", e.message); invalid++; continue; }
  const ctx = {}; collectGloss(o, ctx);
  walk(rel, o, "", ctx, SKIP_SPELL.some((r) => r.test(rel)));
}

// typo candidates: unknown words one edit away from a dictionary word
const near = (w) => {
  const a = "αβγδεζηθικλμνξοπρστυφχψωάέήίόύώϊϋΐΰς";
  for (let i = 0; i <= w.length; i++) {
    for (const c of a) { const x = w.slice(0, i) + c + w.slice(i); if (dict.has(x)) return x; if (i < w.length) { const y = w.slice(0, i) + c + w.slice(i + 1); if (y !== w && dict.has(y)) return y; } }
    if (i < w.length) { const d = w.slice(0, i) + w.slice(i + 1); if (dict.has(d)) return d; }
    if (i < w.length - 1) { const t = w.slice(0, i) + w[i + 1] + w[i] + w.slice(i + 2); if (dict.has(t)) return t; }
  }
  return null;
};
const unk = [...unknown.entries()].map(([w, u]) => ({ word: w, n: u.n, files: [...u.files], ex: u.ex, near: u.n <= 3 ? near(w) : null })).sort((a, b) => (b.near ? 1 : 0) - (a.near ? 1 : 0) || a.n - b.n);

// ---------- report ----------
const byKind = {}; for (const x of findings) byKind[x.kind] = (byKind[x.kind] || 0) + 1;
const hard = findings.filter((x) => x.hard);
console.log(`audited ${files.length} files: ${findings.length} findings (${hard.length} hard), ${unk.length} words unknown to el_GR (${unk.filter((u) => u.near).length} look like typos)`);
console.log("by kind: " + Object.entries(byKind).sort((a, b) => b[1] - a[1]).map(([k, n]) => `${k} ${n}`).join(", "));
if (!QUIET) {
  for (const x of findings.filter((x) => x.kind !== "lookup-miss")) console.log(`  ${x.hard ? "HARD" : "warn"} ${x.kind}: ${x.file} ${x.path} ${x.word ? "«" + x.word + "»" : ""} | ${x.text}`);
  const tc = unk.filter((u) => u.near); if (tc.length) console.log("typo candidates (word → nearest el_GR word, count, file):"); for (const u of tc) console.log(`  ${u.word} → ${u.near}  ×${u.n}  ${u.files[0]}  | ${u.ex}`);
}
if (JSON_OUT) fs.writeFileSync(JSON_OUT, JSON.stringify({ files: files.length, byKind, findings, unknown: unk }, null, 1));
if (MD_OUT) {
  const lines = [`# Audit report`, ``, `${files.length} files, ${findings.length} findings (${hard.length} hard).`, ``, ...Object.entries(byKind).map(([k, n]) => `- ${k}: ${n}`), ``, `## Typo candidates`, ``, ...unk.filter((u) => u.near).map((u) => `- ${u.word} → ${u.near} (×${u.n}, ${u.files[0]})`)];
  fs.writeFileSync(MD_OUT, lines.join("\n") + "\n");
}
process.exitCode = hard.length ? 1 : 0;
