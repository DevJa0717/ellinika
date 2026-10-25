// node render_pdf.js <build dir> <out dir> A1 A2 ...  — prints <build>/<L>.html to <out>/Ellinika-<L>-textbook.pdf
const { chromium } = require("/opt/node22/lib/node_modules/playwright");
const path = require("path"), fs = require("fs");
(async () => {
  const [build, out, ...levels] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium" });
  for (const L of levels) {
    const page = await browser.newPage();
    await page.goto("file://" + path.resolve(build, L + ".html"), { waitUntil: "load", timeout: 0 });
    await page.evaluate(() => document.fonts.ready);
    const file = path.join(out, `Ellinika-${L}-textbook.pdf`);
    await page.pdf({ path: file, format: "A4", printBackground: true, outline: true, tagged: true, preferCSSPageSize: true, timeout: 0,
      displayHeaderFooter: true, headerTemplate: "<span></span>",
      footerTemplate: `<div style="font-family:sans-serif;font-size:7.5pt;color:#7a8396;width:100%;padding:0 16mm;display:flex;justify-content:space-between"><span>Ελληνικά · ${L} companion textbook</span><span class="pageNumber"></span></div>` });
    console.log(L, (fs.statSync(file).size / 1048576).toFixed(1) + " MB");
    await page.close();
  }
  await browser.close();
})();
