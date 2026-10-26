// Cookbook check: runs tools/philosophers/check.js on a copy of each chapter whose recipe and tables are folded into
// checked fields (recipe lines become paragraphs, table Greek cells become vocab), so every Greek word is checked.
// Usage: node /mnt/project-files/tools/kouzina/check.js <chapter.json>…
const fs = require("fs"), os = require("os"), path = require("path"), cp = require("child_process");
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "kz-"));
const files = process.argv.slice(2).filter((f) => !f.endsWith("index.json")).map((f) => {
  const c = JSON.parse(fs.readFileSync(f)), extra = [];
  for (const s of c.sections || []) for (const t of s.tables || []) {
    extra.push(t.el || "");
    t.rows.forEach((r) => r.forEach((v, i) => { if (t.cols[i].lang === "el") extra.push(v); }));
  }
  if (c.recipe) {
    const r = c.recipe, cite = c.sections[0].paras[0].cite;
    const paras = [...r.groups.flatMap((g) => [{ el: g.el, en: g.en || "-", cite }, ...g.items.map((x) => ({ el: x.el, en: x.en || "-", cite }))]),
      ...r.steps.map((x) => ({ ...x, cite })), ...r.tips.map((x) => ({ ...x, cite })), { el: r.serves_el + " " + r.time_el, en: "-", cite }];
    c.sections.push({ id: "recipe", el: "Συνταγή", en: "Recipe", paras });
  }
  c.vocab = [...(c.vocab || []), ...extra];
  const out = path.join(tmp, path.basename(f)); fs.writeFileSync(out, JSON.stringify(c)); return out;
});
const r = cp.spawnSync("node", ["/mnt/project-files/tools/philosophers/check.js", ...files], { stdio: "inherit" });
process.exitCode = r.status;
