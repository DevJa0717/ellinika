// Accuracy checks for the error-correction workbook (corrected texts only, from corrected.txt written by build.py).
// Usage: node library/errors/src/check.js   (run from the repo root or anywhere)
// Reports: words unknown to the LibreOffice el_GR list and to the app lexicon, final-ν slips (same rule as the
// 2026-10-25 audit), words stressed on the third-last syllable before a clitic without a second accent,
// one-syllable words with an accent (except ή, πού, πώς), double accents, and words the tap lookup cannot resolve.
const fs = require("fs"), path = require("path"), cp = require("child_process");
const ROOT = path.resolve(__dirname, "../../.."), D = ROOT + "/data/";
const L = require(ROOT + "/lookup.js");
const lex = [], seen = new Set();
for (const f of fs.readdirSync(D + "lexicon").filter((f) => /^core-.*\.json$/.test(f)).sort()) {
  const d = JSON.parse(fs.readFileSync(D + "lexicon/" + f)); for (const e of Array.isArray(d) ? d : d.entries) if (!seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); }
}
for (const e of JSON.parse(fs.readFileSync(D + "colloquial/colloquial-lexicon.json"))) if (!seen.has(e.lemma)) { seen.add(e.lemma); lex.push(e); }
const irr = JSON.parse(fs.readFileSync(D + "grammar/verbs-holton.json"))["irregular_verbs_6.25"].verbs;
const J = (p) => fs.existsSync(p) ? JSON.parse(fs.readFileSync(p)) : {};
const forms = J(D + "lexicon/forms-index.json").forms || {};
const gloss = J(path.join(ROOT, "library/errors/gloss.json"));
const index = L.build(lex, { ...J(D + "lexicon/names.json"), ...J(D + "colloquial/colloquial-lookup.json"), ...J(ROOT + "/lessons/lookup-gloss.json"), ...J(ROOT + "/lessons/lookup-extra.json") }, irr, forms);
const DIC = "/tmp/el_GR.dic";
if (!fs.existsSync(DIC)) cp.execSync(`curl -sSfL -o ${DIC} https://raw.githubusercontent.com/LibreOffice/dictionaries/master/el_GR/el_GR.dic`);
const words = new Set(new TextDecoder("iso-8859-7").decode(fs.readFileSync(DIC)).split("\n").slice(1).map((l) => l.split("/")[0].trim()));
const ACC = /[άέήίόύώΐΰΆΈΉΊΌΎΏ]/g, VOW = /[αεηιουωάέήίόύώϊϋΐΰ]/gi;
const CL = new Set(["μου", "σου", "του", "της", "μας", "σας", "τους", "τον", "την", "τη", "το", "τα", "τις"]);
const MONO_OK = new Set(["ή", "πού", "πώς", "μάς", "σάς", "τόν"]);
const syl = (w) => (w.toLowerCase().replace(/(αι|ει|οι|ου|υι|αυ|ευ)(?![ΐΰϊϋ])/g, "V").replace(/[ιυ](?=[αεηοωάέήόώ])/g, "").match(/[αεηιουωάέήίόύώϊϋΐΰV]/gi) || []).length;
const lines = fs.readFileSync(__dirname + "/corrected.txt", "utf8").trim().split("\n");
const out = { spell: new Map(), nu: [], acc2: [], mono: [], dbl: [], miss: new Map() };
for (const line of lines) {
  const [id, text] = line.split("\t");
  const toks = text.match(/[Ͱ-Ͽἀ-῿]+/g) || [];
  // final ν
  const re = /(^|[\s«(“"])(τη|στη|την|στην|μη|μην|δε)\s+([Ͱ-Ͽ]+)/gi; let m;
  const keep = /^([αεηιουωάέήίόύώϊϋΐΰ]|κ|π|τ|ξ|ψ|γκ|μπ|ντ|τσ|τζ)/i;
  while ((m = re.exec(text))) {
    const a = m[2].toLowerCase(), w = m[3].toLowerCase(), needs = keep.test(w);
    if (["την", "στην", "μην"].includes(a) && !needs) out.nu.push(`${id}: ${m[2]} ${m[3]}`);
    if (["τη", "στη", "μη", "δε"].includes(a) && needs) out.nu.push(`${id}: ${m[2]} ${m[3]}`);
  }
  if (/\bτο\s+(Νίκο|γάτο|φίλο)\b/.test(text)) out.nu.push(`${id}: masculine το`);
  toks.forEach((t, i) => {
    const n = (t.match(ACC) || []).length, s = syl(t);
    if (n > 1 && !(n === 2 && toks[i + 1] && CL.has(toks[i + 1].toLowerCase()))) out.dbl.push(`${id}: ${t}`);
    if (s === 1 && n === 1 && !MONO_OK.has(t.toLowerCase())) out.mono.push(`${id}: ${t}`);
    if (s >= 2 && n === 0 && !/^[ΑΕΗΙΟΥΩ]+$/.test(t) && !CL.has(t.toLowerCase())) out.mono.push(`${id}: no accent ${t}`);
    // third-last stress before a clitic: is the accented vowel 3rd from end?
    const next = toks[i + 1];
    if (next && CL.has(next.toLowerCase()) && n === 1) {
      const idx = text.indexOf(t + " " + next);
      const vs = [...t.toLowerCase().replace(/(αι|ει|οι|ου|αυ|ευ)/g, (x) => /[άέήίόύώ]/.test(x) ? x : "V")].filter((c) => /[αεηιουωάέήίόύώϊϋΐΰV]/.test(c));
      const pos = vs.findIndex((c) => /[άέήίόύώΐΰ]/.test(c));
      if (pos >= 0 && vs.length - pos === 3 && idx >= 0) out.acc2.push(`${id}: ${t} ${next}`);
    }
    const lw = t.toLowerCase();
    if (!words.has(t) && !words.has(lw) && !forms[lw] && !forms[t]) out.spell.set(t, (out.spell.get(t) || []).concat(id));
    const r = L.lookup(index, t, gloss);
    if (!r) out.miss.set(t, (out.miss.get(t) || []).concat(id));
    else if (r[0].how === "guess") out.miss.set(t + " (guess " + r[0].lemma + ")", (out.miss.get(t) || []).concat(id));
  });
}
console.log(`texts: ${lines.length}`);
console.log(`final ν: ${out.nu.length}`); out.nu.forEach((x) => console.log("  " + x));
console.log(`double accents: ${out.dbl.length}`); out.dbl.forEach((x) => console.log("  " + x));
console.log(`accent on one-syllable / no accent: ${out.mono.length}`); out.mono.forEach((x) => console.log("  " + x));
console.log(`third-last stress before clitic (check: needs a 2nd accent unless the clitic belongs to the next word): ${out.acc2.length}`); out.acc2.forEach((x) => console.log("  " + x));
console.log(`unknown to el_GR and lexicon: ${out.spell.size}`); for (const [k, v] of out.spell) console.log(`  ${k} (${v.slice(0, 3).join(", ")})`);
console.log(`lookup misses: ${out.miss.size}`); for (const [k, v] of out.miss) console.log(`  ${k} (${v.slice(0, 3).join(", ")})`);
