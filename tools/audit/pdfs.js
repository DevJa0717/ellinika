#!/usr/bin/env node
// PDF check (2026-11-05): every downloads/textbook/*.pdf has a Greek-only cover (no Latin letters on page 1, cover
// rule of 2026-10-26), a Greek "Έκδοση <date>" line, and is listed on downloads/textbook/index.html. Needs pdftotext/pdfinfo.
// Usage: node tools/audit/pdfs.js
const fs = require("fs"), path = require("path"), cp = require("child_process");
const DIR = path.resolve(__dirname, "../../downloads/textbook");
const index = fs.readFileSync(path.join(DIR, "index.html"), "utf8");
let bad = 0;
for (const f of fs.readdirSync(DIR).filter((f) => f.endsWith(".pdf")).sort()) {
  const p = path.join(DIR, f);
  const cover = cp.execFileSync("pdftotext", ["-f", "1", "-l", "1", p, "-"]).toString();
  const pages = (cp.execFileSync("pdfinfo", [p]).toString().match(/Pages:\s+(\d+)/) || [])[1];
  const probs = [];
  const latin = cover.match(/[A-Za-z]{2,}/g); if (latin) probs.push("Latin on cover: " + [...new Set(latin)].join(" "));
  if (!/Έκδοση/.test(cover)) probs.push("no «Έκδοση …» line on cover");
  if (!index.includes(`href="${f}"`)) probs.push("not listed on index.html");
  bad += probs.length;
  console.log(`${probs.length ? "✗" : "✓"} ${f} (${pages} pp)${probs.length ? ": " + probs.join("; ") : ""}`);
}
process.exitCode = bad ? 1 : 0;
