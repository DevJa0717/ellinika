// node render_cover.js <cover.html> <out.pdf> — prints a cover page with no header or footer (Greek-only covers).
const { chromium } = require("/opt/node22/lib/node_modules/playwright");
const path = require("path");
(async () => {
  const [src, out] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium" });
  const page = await browser.newPage();
  await page.goto("file://" + path.resolve(src), { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: out, format: "A4", printBackground: true, preferCSSPageSize: true, pageRanges: "1" });
  await browser.close();
})();
