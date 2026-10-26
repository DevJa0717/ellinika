// node deploy/textbook/render_drills.js <build dir> <out dir> — prints the two drill books to PDF and packs them with compress.py
const { chromium } = require("playwright");
const path = require("path"), fs = require("fs"), { execFileSync } = require("child_process");
(async () => {
  const [build, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  for (const [html, pdf, label] of [["Declension drills.html", "Ellinika-Declension-drills.pdf", "Κλίση ονομάτων"], ["Conjugation drills.html", "Ellinika-Conjugation-drills.pdf", "Συζυγία ρημάτων"]]) {
    const page = await browser.newPage();
    await page.goto("file://" + path.resolve(build, html), { waitUntil: "load", timeout: 0 });
    await page.evaluate(() => document.fonts.ready);
    const raw = path.join(build, pdf);
    await page.pdf({ path: raw, format: "A4", printBackground: true, outline: true, tagged: true, preferCSSPageSize: true, timeout: 0,
      displayHeaderFooter: true, headerTemplate: "<span></span>",
      footerTemplate: `<div style="font-family:sans-serif;font-size:7.5pt;color:#7a8396;width:100%;padding:0 16mm;display:flex;justify-content:space-between"><span>Ελληνικά · ${label}</span><span class="pageNumber"></span></div>` });
    execFileSync("python3", [path.join(__dirname, "compress.py"), raw, path.join(out, pdf), "Ελληνικά · " + label]);
    console.log(pdf, (fs.statSync(path.join(out, pdf)).size / 1048576).toFixed(1) + " MB");
    await page.close();
  }
  await browser.close();
})();
