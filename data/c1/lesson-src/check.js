// Usage: node check.js id1 id2 ...  (server on :8765 serving site/)
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' in {} ? undefined : undefined });
  const p = await b.newPage();
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error'||m.type()==='warning') errs.push(m.text()); });
  for (const id of process.argv.slice(2)) {
    errs.length = 0;
    await p.goto(`http://localhost:8765/app/index.html#${id}`); await p.waitForTimeout(1500);
    const bad = await p.$$eval('.block', bs => bs.filter(x => /could not load/.test(x.textContent)).map(x => x.textContent.slice(0,150)));
    const nblocks = await p.$$eval('.block', bs => bs.length);
    await p.goto(`http://localhost:8765/app/index.html#${id}.practice`); await p.waitForTimeout(1500);
    const txt = (await p.textContent('#pane')||'').slice(0,200).replace(/\s+/g,' ');
    console.log(`${id}: blocks=${nblocks} bad=${JSON.stringify(bad)} errs=${JSON.stringify(errs)} practice="${txt}"`);
  }
  await b.close();
})();
