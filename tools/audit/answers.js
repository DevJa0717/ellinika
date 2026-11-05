#!/usr/bin/env node
// Answer-key check (2026-11-05): every word inside an "answer"/"accept"/"correct"/"solution" value of any drill
// must be a real Greek form (LibreOffice el_GR list ∪ the project's forms index and word lists ∪ tools/audit/allow.txt),
// unless it is in the item's own gloss. A wrong form in an answer key teaches the error, so these are listed one by one.
// Usage: node tools/audit/answers.js [paths]   (default: library lessons)
const fs = require("fs"), path = require("path"), cp = require("child_process");
const ROOT = path.resolve(__dirname, "../..");
const DIC = process.env.EL_DIC || "/tmp/el_GR.dic";
if (!fs.existsSync(DIC)) cp.execSync(`curl -sSfL -o ${DIC} https://raw.githubusercontent.com/LibreOffice/dictionaries/master/el_GR/el_GR.dic`);
const dict = new Set(new TextDecoder("iso-8859-7").decode(fs.readFileSync(DIC)).split("\n").slice(1).map((l) => l.split("/")[0].trim()));
const J = (p) => { try { return JSON.parse(fs.readFileSync(p)); } catch { return {}; } };
for (const k of Object.keys(J(ROOT + "/data/lexicon/forms-index.json").forms || {})) dict.add(k);
for (const f of fs.readdirSync(ROOT + "/data/lexicon").filter((f) => /^core-.*\.json$/.test(f))) { const d = J(ROOT + "/data/lexicon/" + f); for (const e of Array.isArray(d) ? d : d.entries || []) dict.add(e.lemma); }
const allowF = path.join(__dirname, "allow.txt");
if (fs.existsSync(allowF)) for (const l of fs.readFileSync(allowF, "utf8").split("\n")) { const w = l.replace(/#.*/, "").trim(); if (w) dict.add(w); }
const args = process.argv.slice(2); const targets = args.length ? args : ["library", "lessons"];
const files = []; const visit = (p) => { const st = fs.statSync(p); if (st.isDirectory()) { for (const f of fs.readdirSync(p).sort()) if (f !== "src") visit(path.join(p, f)); } else if (p.endsWith(".json")) files.push(p); };
for (const t of targets) visit(path.resolve(ROOT, t));
const SKIP = /dialects|slang|colloquial|classics|videos|errors\/|c1-language-question|c1-read-prose|c1-ancient/;
let n = 0;
for (const f of files) {
  const rel = path.relative(ROOT, f); if (SKIP.test(rel)) continue;
  const o = J(f); const out = [];
  const walk = (x, ctx) => {
    if (Array.isArray(x)) return x.forEach((y) => walk(y, ctx));
    if (!x || typeof x !== "object") return;
    const g = { ...ctx, ...(x.gloss && typeof x.gloss === "object" ? x.gloss : {}) };
    for (const [k, v] of Object.entries(x)) {
      if (/^(answer|answers|accept|correct|solution|a|fix|right)$/i.test(k)) for (const s of [].concat(v)) if (typeof s === "string")
        for (const m of s.replace(/\*+/g, "").matchAll(/[Ͱ-Ͽ]+(?:['’])?/g)) {
          const w = m[0]; if (/['’]$/.test(w) || /^[Α-ΩΆ-Ώ]/.test(w) && s.indexOf(w) > 0) continue;
          const lw = w.toLowerCase(), b = s.replace(/\*+/g, "")[m.index - 1] || "", a = s.replace(/\*+/g, "")[m.index + w.length] || "";
          if (/[-‐_]/.test(b) || /[-‐_]/.test(a)) continue;
          if (!dict.has(w) && !dict.has(lw) && !(w in g) && !(lw in g)) out.push(`${w}  ← ${k}: ${s.slice(0, 90)}`);
        }
      walk(v, g);
    }
  };
  walk(o, o.gloss && typeof o.gloss === "object" ? o.gloss : {});
  if (out.length) { n += out.length; console.log(`${rel}: ${out.length}`); for (const l of [...new Set(out)]) console.log("   " + l); }
}
console.log(`${n} answer-key words not found in any word list`);
process.exitCode = n ? 1 : 0;
