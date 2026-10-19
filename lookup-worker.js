/* Builds the word-lookup index off the main thread, so the first tap on a word never freezes scrolling.
   app.js sends the file list ({lex, extra, verbs, forms}) and then one {word, ctx} per tap. */
importScripts("lookup.js");
let ready = null;
const getJSON = (u) => fetch(u).then((r) => (r.ok ? r.json() : {})).catch(() => ({}));
async function build({ lex, extra, verbs, forms }) {
  const [lists, extras, v, f] = await Promise.all([Promise.all(lex.map(getJSON)), Promise.all(extra.map(getJSON)), getJSON(verbs), getJSON(forms)]);
  const out = [], seen = new Set();
  for (const d of lists) for (const e of (Array.isArray(d) ? d : d.entries || [])) if (!seen.has(e.lemma)) { seen.add(e.lemma); out.push(e); }
  return self.EllinikaLookup.build(out, Object.assign({}, ...extras), v["irregular_verbs_6.25"]?.verbs || [], f.forms || {});
}
onmessage = async (e) => {
  const m = e.data;
  try {
    if (m.files) { ready = ready || build(m.files); await ready; postMessage({ id: m.id, ok: true }); }
    else postMessage({ id: m.id, hits: self.EllinikaLookup.lookup(await ready, m.word, m.ctx) });
  } catch (err) { postMessage({ id: m.id, error: String(err && err.message || err) }); }
};
