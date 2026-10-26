// node render_syntax.js <build dir> <out dir>  — prints Syntax.html and "Grammar cards.html"; shrinks any card taller than one page first
const { chromium } = require("/opt/node22/lib/node_modules/playwright");
const path = require("path"), fs = require("fs");
const BOOKS = [["Syntax", "Ellinika-Syntax.pdf", "Σύνταξη και λόγος"], ["Grammar cards", "Ellinika-Grammar-cards.pdf", "Κάρτες γραμματικής"]];
(async () => {
  const [build, out] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium" });
  for (const [name, file, label] of BOOKS) {
    const page = await browser.newPage();
    await page.goto("file://" + path.resolve(build, name + ".html"), { waitUntil: "load", timeout: 0 });
    await page.evaluate(() => document.fonts.ready);
    await page.emulateMedia({ media: "print" });
    // printable height: 297mm minus 36mm margins, less a little for safety; 1mm = 96/25.4 px
    const shrunk = await page.evaluate(() => {
      const max = (297 - 36 - 4) * 96 / 25.4, out = [];
      for (const c of document.querySelectorAll(".card")) {
        let pt = 10;
        while (c.scrollHeight > max && pt > 6.5) { pt -= 0.25; c.style.fontSize = pt + "pt"; c.querySelectorAll("table").forEach((t) => t.style.fontSize = (pt - 0.7) + "pt"); }
        if (pt < 10) out.push(c.id + " " + pt + "pt" + (c.scrollHeight > max ? " STILL TOO TALL" : ""));
      }
      return out;
    });
    if (shrunk.length) console.log(name, "shrunk:", shrunk.join(", "));
    const dst = path.join(out, file);
    await page.pdf({ path: dst, format: "A4", printBackground: true, outline: true, tagged: true, preferCSSPageSize: true, timeout: 0,
      displayHeaderFooter: true, headerTemplate: "<span></span>",
      footerTemplate: `<div style="font-family:sans-serif;font-size:7.5pt;color:#7a8396;width:100%;padding:0 16mm;display:flex;justify-content:space-between"><span>Ελληνικά · ${label}</span><span class="pageNumber"></span></div>` });
    console.log(name, (fs.statSync(dst).size / 1048576).toFixed(1) + " MB");
    await page.close();
  }
  await browser.close();
})();
