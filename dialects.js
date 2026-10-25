/* Ελληνικά Dialects: one document per Modern Greek dialect, with a map, feature tables, sample texts, recordings and sources.
   Registers #dialects (the shelf, with the map) and #dialects.<id> in window.EllinikaAddons.
   Content is data: library/dialects/index.json lists the documents, the dialect groups and the map markers;
   library/dialects/map.json holds the coastline paths; each document is library/dialects/<id>.json. */
(function () {
  "use strict";
  const A = () => window.Ellinika;
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});
  const BASE = "library/dialects/";

  const css = `
.dl-map { position: relative; margin: 0; }
.dl-map svg { display: block; width: 100%; height: auto; border-radius: 10px; background: var(--aegean-soft); border: 1px solid var(--line); }
.dl-map .land { fill: var(--card); stroke: var(--line); stroke-width: .6; }
.dl-map .greek { fill: var(--paper); stroke: var(--line); stroke-width: .6; opacity: .55; }
.dl-map .mk circle { stroke: var(--card); stroke-width: 1.6; }
.dl-map .mk.dim { opacity: .28; }
.dl-map .mk text { font: 600 12px/1 var(--f-ui); fill: var(--ink); paint-order: stroke; stroke: var(--card); stroke-width: 3px; stroke-linejoin: round; }
.dl-map a.mk:focus-visible circle { stroke: var(--terra); stroke-width: 3; }
.dl-legend { display: flex; flex-wrap: wrap; gap: 6px 14px; margin: 10px 0 0; padding: 0; list-style: none; font: 500 .8rem/1.3 var(--f-ui); color: var(--muted); }
.dl-legend i { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 6px; vertical-align: -1px; }
.dl-cap { font: 400 .8rem/1.4 var(--f-ui); color: var(--muted); margin: 6px 0 0; }
.dl-group { margin: 22px 0 8px; font: 600 .78rem/1.2 var(--f-ui); letter-spacing: .06em; text-transform: uppercase; color: var(--muted); display: flex; align-items: center; gap: 8px; }
.dl-group i { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
.dl-head { display: grid; gap: 6px; margin: 4px 0 14px; }
.dl-head h2 { margin: 0; font: 400 2rem/1.15 var(--f-display); }
.dl-chips { display: flex; flex-wrap: wrap; gap: 6px; }
.dl-lead { font-size: 1.05rem; }
.dl-facts { display: grid; grid-template-columns: max-content minmax(0, 1fr); gap: 6px 14px; margin: 0; font-size: .95rem; }
.dl-facts dt { font: 600 .78rem/1.6 var(--f-ui); color: var(--muted); text-transform: uppercase; letter-spacing: .04em; }
.dl-facts dd { margin: 0; }
@media (max-width: 420px) { .dl-facts { grid-template-columns: minmax(0, 1fr); gap: 2px; } .dl-facts dd { margin-bottom: 8px; } }
.dl-sec { margin: 26px 0 0; }
.dl-sec > h3 { margin: 0 0 8px; font: 600 1.15rem/1.3 var(--f-ui); }
.dl-sec > h3 .el { display: block; font: 400 .95rem/1.3 var(--f-body); color: var(--muted); }
.dl-sec p { margin: 0 0 10px; }
.dl-tl { list-style: none; margin: 0; padding: 0 0 0 14px; border-left: 2px solid var(--line); display: grid; gap: 10px; }
.dl-tl li { position: relative; }
.dl-tl li::before { content: ""; position: absolute; left: -20px; top: .45em; width: 10px; height: 10px; border-radius: 50%; background: var(--terra); }
.dl-tl b { font: 600 .85rem/1.3 var(--f-ui); color: var(--terra); display: block; }
.dl-tbl { border-collapse: collapse; width: 100%; font-size: .92rem; }
.dl-tbl th, .dl-tbl td { text-align: left; vertical-align: top; padding: 7px 8px; border-bottom: 1px solid var(--line); }
.dl-tbl th { font: 600 .75rem/1.3 var(--f-ui); color: var(--muted); text-transform: uppercase; letter-spacing: .04em; }
.dl-tbl:not(.stack) td:first-child { white-space: nowrap; }
.dl-tbl.wrap td:first-child { white-space: normal; }
@media (max-width: 620px) {
  .dl-tbl.stack, .dl-tbl.stack tbody, .dl-tbl.stack tr, .dl-tbl.stack td { display: block; width: 100%; }
  .dl-tbl.stack thead { display: none; }
  .dl-tbl.stack tr { padding: 9px 0; border-bottom: 1px solid var(--line); }
  .dl-tbl.stack td { border: 0; padding: 2px 0; white-space: normal; }
  .dl-tbl.stack td.nil { display: none; }
  .dl-tbl.stack td:first-child { font-weight: 600; }
  .dl-tbl.stack td + td::before { content: attr(data-h); display: block; font: 600 .68rem/1.4 var(--f-ui); color: var(--muted); text-transform: uppercase; letter-spacing: .04em; }
}
.dl-ex { list-style: none; margin: 0; padding: 0; display: grid; gap: 10px; }
.dl-ex li { border-left: 3px solid var(--terra); padding: 2px 0 2px 12px; }
.dl-ex .d { font-size: 1.05rem; }
.dl-ex .s, .dl-ex .e { display: block; font-size: .9rem; color: var(--muted); }
.dl-ex .s::before { content: "Standard: "; font: 600 .72rem/1 var(--f-ui); text-transform: uppercase; letter-spacing: .04em; }
.dl-sample .ln { margin: 0; }
.dl-sample .ln + .ln { margin-top: 2px; }
.dl-sample .en { color: var(--muted); font-size: .92rem; margin-top: 10px; }
.dl-src { font-size: .88rem; }
.dl-src li { margin-bottom: 4px; }
.dl-yes { color: var(--good); font-weight: 600; }
.dl-part { color: var(--warn); font-weight: 600; }
.dl-no { color: var(--muted); }
.dl-nav { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 24px; }
.dl-clip { display: grid; gap: 10px; padding-top: 14px; }
.dl-clip + .dl-clip { border-top: 1px solid var(--line); margin-top: 14px; }
.dl-clip h4 { margin: 0; font-size: 1.05rem; }
.dl-clip .who { margin: 0; font-size: .92rem; color: var(--muted); }
.dl-clip .sub-tr { font: 400 .9rem/1.4 var(--f-body); color: var(--muted); }
.dl-clip .vctl { display: flex; flex-wrap: wrap; gap: 6px; }
.dl-clip .transcript li { align-items: start; }
.dl-clip .transcript .tr { display: block; font: 400 .84rem/1.35 var(--f-body); color: var(--muted); }
.dl-clip .src { margin: 0; font-size: .8rem; color: var(--muted); }
.dl-clip .lf { margin: 0; font-size: .9rem; }`;
  function style() { if (!document.getElementById("dl-css")) { const s = document.createElement("style"); s.id = "dl-css"; s.textContent = css; document.head.append(s); } }

  let idxP = null, mapP = null;
  const index = () => (idxP = idxP || A().getJSON(BASE + "index.json").catch((e) => { idxP = null; throw e; }));
  const mapData = () => (mapP = mapP || A().getJSON(BASE + "map.json").catch((e) => { mapP = null; throw e; }));

  // Map: equirectangular projection centred on 40.5° N, the same one map.json was drawn with.
  function mapSVG(m, idx, focus) {
    const E = A(), col = Object.fromEntries(idx.groups.map((g) => [g.id, g.color]));
    const xy = (lon, lat) => [(lon - m.W) * m.K * m.SC, (m.N - lat) * m.SC];
    const marks = idx.markers.map((k) => {
      const [x, y] = xy(k.lon, k.lat), on = !focus || focus.includes(k.id), big = focus && on;
      const dx = k.dx ?? 9, anchor = dx < 0 ? "end" : "start";
      const body = `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${big ? 7.5 : 5.5}" fill="${col[k.group] || "#888"}"/>`
        + (k.label && (!focus || on) ? `<text x="${(x + dx).toFixed(1)}" y="${(y + (k.dy ?? 4)).toFixed(1)}" text-anchor="${anchor}">${E.esc(k.label)}</text>` : "");
      return k.doc && (!focus || !on)
        ? `<a class="mk${on ? "" : " dim"}" href="#dialects.${E.esc(k.doc)}" aria-label="${E.esc(k.name || k.label)}"><title>${E.esc(k.name || k.label)}</title>${body}</a>`
        : `<g class="mk${on ? "" : " dim"}"><title>${E.esc(k.name || k.label)}</title>${body}</g>`;
    }).join("");
    return `<figure class="dl-map no-look"><svg viewBox="0 0 ${m.w} ${m.h}" role="img" aria-label="Map of the Greek dialect areas around 1900">
      <path class="land" d="${m.land}"/><path class="greek" d="${m.greek}"/>${marks}</svg></figure>`;
  }
  const legend = (idx) => `<ul class="dl-legend no-look">${idx.groups.map((g) => `<li><i style="background:${g.color}"></i>${A().esc(g.en)}</li>`).join("")}</ul>`;

  // A cell marked ✓, ~ or – becomes a coloured symbol (feature tables).
  const SYM = new Set(["✓", "~", "–"]);
  function cell(E, c) {
    const s = String(c ?? "");
    if (s === "✓") return `<span class="dl-yes" aria-label="yes">✓</span>`;
    if (s === "~") return `<span class="dl-part" aria-label="partly">~</span>`;
    if (s === "–") return `<span class="dl-no" aria-label="no">–</span>`;
    return E.md(s);
  }
  function section(E, s) {
    let h = `<section class="dl-sec">${s.h ? `<h3>${E.esc(s.h)}${s.el ? `<span class="el" lang="el">${E.esc(s.el)}</span>` : ""}</h3>` : ""}`;
    if (s.text) h += E.paras ? E.paras(s.text) : `<p>${E.md(s.text)}</p>`;
    if (s.timeline) h += `<ol class="dl-tl">${s.timeline.map((t) => `<li><b>${E.esc(t.when)}</b>${E.md(t.text)}</li>`).join("")}</ol>`;
    if (s.table) {
      // Tick grids stay as grids; word tables stack into cards on a phone (each cell labelled by its column head).
      const grid = s.table.rows.some((r) => r.some((c) => SYM.has(String(c).trim())));
      h += `<div class="tbl-wrap"><table class="dl-tbl${s.table.wrap ? " wrap" : ""}${grid ? "" : " stack"}"><thead><tr>${s.table.head.map((c) => `<th>${E.esc(c)}</th>`).join("")}</tr></thead>
      <tbody>${s.table.rows.map((r) => `<tr>${r.map((c, i) => String(c).trim() ? `<td data-h="${E.esc(s.table.head[i] || "")}">${cell(E, c)}</td>` : "<td class=\"nil\"></td>").join("")}</tr>`).join("")}</tbody></table></div>`;
    }
    if (s.examples) h += `<ul class="dl-ex">${s.examples.map((x) => `<li><span class="d" lang="el">${E.esc(x.el)}</span>${x.std ? `<span class="s" lang="el">${E.esc(x.std)}</span>` : ""}${x.en ? `<span class="e">${E.esc(x.en)}</span>` : ""}</li>`).join("")}</ul>`;
    if (s.notes) h += `<ul class="ref-notes">${s.notes.map((n) => `<li>${E.md(n)}</li>`).join("")}</ul>`;
    if (s.after) h += `<p>${E.md(s.after)}</p>`;
    return h + "</section>";
  }

  async function shelf() {
    const E = A();
    document.title = "Dialects of Greek · Ελληνικά";
    E.$("#bar-meta").textContent = "Dialects";
    E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><p class="loading">Φόρτωση…</p>`;
    const [idx, m] = await Promise.all([index(), mapData().catch(() => null)]);
    const done = E.progress.library || {};
    E.view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p>
      <div class="dl-head"><h2 lang="el">Οι διάλεκτοι της ελληνικής</h2><span class="ex-en">Dialects of Modern Greek: where they are spoken, how they sound, and where their differences come from</span></div>
      <p class="dl-lead">${E.md(idx.intro || "")}</p>
      ${m ? mapSVG(m, idx) + legend(idx) + `<p class="dl-cap">${E.md(idx.mapCaption || "")}</p>` : ""}
      ${idx.groups.map((g) => { const its = idx.items.filter((x) => x.group === g.id); return its.length ? `<h3 class="dl-group"><i style="background:${g.color}"></i>${E.esc(g.en)}</h3>
        <ul class="lessons">${its.map((x) => `<li><a class="lesson-row" href="#dialects.${E.esc(x.id)}"><span class="lr-num">${idx.items.indexOf(x) + 1}</span>
          <span class="lr-main"><span class="lr-title" lang="el">${E.esc(x.el)}</span><span class="lr-en">${E.esc(x.title)}</span></span>
          ${done["dialects/" + x.id] != null ? `<span class="chip done">${Math.round(done["dialects/" + x.id] * 100)}%</span>` : ""}</a></li>`).join("")}</ul>` : ""; }).join("")}`;
    E.wrapGreek(E.view.querySelector(".dl-lead"));
    window.scrollTo(0, 0);
  }

  // Listen: dialect recordings played from YouTube (nothing stored), with subtitles synced by the embed's postMessage time.
  // Each subtitle shows the Greek-script line (tappable), and on request VLACH's phonetic transcription and English.
  const mmss = (t) => `${Math.floor(t / 60)}:${String(Math.floor(t % 60)).padStart(2, "0")}`;
  function clipHTML(E, c) {
    const cues = c.cues || [], start = Math.floor(cues[0]?.t || 0);
    return `<div class="dl-clip" data-clip="${E.esc(c.id)}">
      <h4>${c.el ? `<span lang="el">${E.esc(c.el)}</span> · ` : ""}<span class="no-look">${E.esc(c.title)}</span></h4>
      ${c.who ? `<p class="who">${E.md(c.who)}</p>` : ""}
      <div class="vframe"><iframe src="https://www.youtube-nocookie.com/embed/${encodeURIComponent(c.yt)}?enablejsapi=1&playsinline=1&rel=0${start ? `&start=${Math.max(0, start - 2)}` : ""}" title="${E.esc(c.title)}" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen loading="lazy"></iframe></div>
      ${cues.length ? `<div class="subs"><div class="sub-el" lang="el">&nbsp;</div><div class="sub-tr no-look" hidden></div><div class="sub-en no-look" hidden></div></div>
      <div class="vctl"><button class="btn ghost small" data-act="en">English line</button><button class="btn ghost small" data-act="tr">VLACH transcription</button><button class="btn ghost small" data-act="list">Transcript</button></div>
      <ol class="transcript" hidden>${cues.map((q, i) => `<li data-i="${i}"><button class="tc-time" data-i="${i}">${mmss(q.t)}</button><span><span lang="el">${E.esc(q.el)}</span><span class="tr no-look">${E.esc(q.tr || "")}</span><span class="tr no-look">${E.esc(q.en || "")}</span></span></li>`).join("")}</ol>` : ""}
      ${c.listenFor ? `<p class="lf"><b>Listen for:</b> ${E.md(c.listenFor)}</p>` : ""}
      ${c.note ? `<p class="who">${E.md(c.note)}</p>` : ""}
      <p class="src no-look"><a href="https://www.youtube.com/watch?v=${encodeURIComponent(c.yt)}" target="_blank" rel="noopener">${E.esc(c.cite)}</a></p>
    </div>`;
  }
  function wireClip(E, el, c) {
    const cues = c.cues || [], frame = el.querySelector("iframe");
    if (!cues.length || !frame) return;
    const subEl = el.querySelector(".sub-el"), subTr = el.querySelector(".sub-tr"), subEn = el.querySelector(".sub-en");
    let cur = -2;
    const yt = (func, args = []) => frame.contentWindow?.postMessage(JSON.stringify({ event: "command", func, args }), "*");
    const tick = (t) => {
      const i = cues.findIndex((q) => t >= q.t && t < q.d);
      if (i === cur) return; cur = i;
      subEl.textContent = i >= 0 ? cues[i].el : " "; E.wrapGreek(subEl);
      subTr.textContent = i >= 0 ? cues[i].tr || "" : "";
      subEn.textContent = i >= 0 ? cues[i].en || "" : "";
      el.querySelectorAll(".transcript li").forEach((li) => li.classList.toggle("on", +li.dataset.i === i));
    };
    const listen = () => frame.contentWindow?.postMessage(JSON.stringify({ event: "listening", id: c.id, channel: "widget" }), "*");
    frame.addEventListener("load", () => { listen(); setTimeout(listen, 800); });
    const onMsg = (e) => {
      if (e.source !== frame.contentWindow) return;
      try { const d = typeof e.data === "string" ? JSON.parse(e.data) : e.data; if (d?.info?.currentTime != null) tick(d.info.currentTime); } catch (err) { /* not ours */ }
    };
    window.addEventListener("message", onMsg);
    const iv = setInterval(() => { if (!document.body.contains(el)) { clearInterval(iv); window.removeEventListener("message", onMsg); } }, 2000);
    const toggle = (sel) => (e) => { const x = el.querySelector(sel); x.hidden = !x.hidden; e.target.classList.toggle("on", !x.hidden); };
    el.querySelector('[data-act="en"]').onclick = toggle(".sub-en");
    el.querySelector('[data-act="tr"]').onclick = toggle(".sub-tr");
    el.querySelector('[data-act="list"]').onclick = toggle(".transcript");
    el.querySelectorAll(".tc-time").forEach((b) => (b.onclick = () => { yt("seekTo", [cues[+b.dataset.i].t, true]); yt("playVideo"); }));
  }

  async function doc(id) {
    const E = A();
    const idx = await index(), meta = idx.items.find((x) => x.id === id);
    if (!meta) { location.hash = "dialects"; return; }
    E.view.innerHTML = `<p class="crumbs"><a href="#dialects">← Dialects</a></p><p class="loading">Φόρτωση…</p>`;
    const [d, m] = await Promise.all([E.getJSON(BASE + meta.file), mapData().catch(() => null)]);
    if (location.hash !== "#dialects." + id) return;
    document.title = d.el + " · Dialects";
    E.$("#bar-meta").textContent = "Dialects";
    E.setGloss(Object.assign({}, ...(d.listen?.clips || []).map((c) => c.gloss || {}), d.gloss));
    const g = idx.groups.find((x) => x.id === meta.group), pos = idx.items.indexOf(meta), prev = idx.items[pos - 1], next = idx.items[pos + 1];
    E.view.innerHTML = `<p class="crumbs"><a href="#dialects">← Dialects</a></p>
      <div class="dl-head"><div class="dl-chips">${g ? `<span class="chip" style="background:${g.color};color:#10283e">${E.esc(g.en)}</span>` : ""}${d.status ? `<span class="chip">${E.esc(d.status)}</span>` : ""}</div>
        <h2 lang="el">${E.esc(d.el)}</h2><span class="ex-en">${E.esc(d.title)}</span></div>
      <div class="dl-body">
      ${d.lead ? `<p class="dl-lead">${E.md(d.lead)}</p>` : ""}
      ${d.facts?.length ? `<section class="card"><dl class="dl-facts">${d.facts.map(([k, v]) => `<dt>${E.esc(k)}</dt><dd>${E.md(v)}</dd>`).join("")}</dl></section>` : ""}
      ${m && d.markers?.length ? `<div class="dl-sec">${mapSVG(m, idx, d.markers)}</div>` : ""}
      ${(d.sections || []).map((s) => section(E, s)).join("")}
      ${d.sample ? `<section class="dl-sec card dl-sample"><h3>${E.esc(d.sample.h || "Sample text")}</h3>${d.sample.intro ? `<p class="sub">${E.md(d.sample.intro)}</p>` : ""}
        <div lang="el">${d.sample.lines.map((l) => `<p class="ln">${E.esc(l)}</p>`).join("")}</div>
        ${d.sample.en ? `<details class="rd-en"><summary>English translation</summary>${d.sample.en.map((l) => `<p class="ln">${E.esc(l)}</p>`).join("")}</details>` : ""}
        ${d.sample.notes ? `<ul class="ref-notes">${d.sample.notes.map((n) => `<li>${E.md(n)}</li>`).join("")}</ul>` : ""}
        ${d.sample.source ? `<p class="sub">${E.md(d.sample.source)}</p>` : ""}</section>` : ""}
      ${d.listen?.clips?.length ? `<section class="dl-sec card dl-listen"><h3>${E.esc(d.listen.h || "Listen")}</h3>${d.listen.intro ? `<p class="sub">${E.md(d.listen.intro)}</p>` : ""}
        ${d.listen.clips.map((c) => clipHTML(E, c)).join("")}
        ${d.listen.render && d.listen.clips.some((c) => c.cues?.length) ? `<p class="sub no-look">${E.md(d.listen.render)}</p>` : ""}</section>` : ""}
      ${d.culture ? `<section class="dl-sec culture"><h3>${E.esc(d.culture.h || "Culture")}</h3>${E.paras ? E.paras(d.culture.text) : E.md(d.culture.text)}</section>` : ""}
      </div>
      ${d.questions?.length ? `<section class="dl-sec card story-q"><h3>Check your understanding</h3>${d.questions.map((q, i) => `<div class="sq" data-i="${i}"><p class="q-prompt">${E.md(q.q)}</p><div class="options">${q.options.map((o) => `<button class="opt">${E.esc(o)}</button>`).join("")}</div><p class="ex-en sq-why" hidden></p></div>`).join("")}<p class="sub" id="sq-score"></p></section>` : ""}
      ${d.related?.length ? `<section class="dl-sec"><h3>In the course</h3><ul class="ref-notes">${d.related.map((r) => `<li><a href="${E.esc(r.href)}">${E.esc(r.label)}</a></li>`).join("")}</ul></section>` : ""}
      ${d.sources?.length ? `<section class="dl-sec dl-src no-look"><h3>Sources</h3><ol>${d.sources.map((s) => `<li>${s.url ? `<a href="${E.esc(s.url)}" target="_blank" rel="noopener">${E.esc(s.label)}</a>` : E.esc(s.label)}${s.note ? ` · ${E.esc(s.note)}` : ""}</li>`).join("")}</ol></section>` : ""}
      <div class="dl-nav">${prev ? `<a class="btn ghost" href="#dialects.${E.esc(prev.id)}">← <span lang="el">${E.esc(prev.el)}</span></a>` : ""}${next ? `<a class="btn" href="#dialects.${E.esc(next.id)}">Next: <span lang="el">${E.esc(next.el)}</span></a>` : ""}</div>`;
    E.wrapGreek(E.view.querySelector(".dl-body"));
    E.wrapGreek(E.view.querySelector(".dl-head h2"));
    E.view.querySelectorAll(".dl-clip").forEach((el) => wireClip(E, el, d.listen.clips.find((c) => c.id === el.dataset.clip)));
    // Questions: the first answer counts; the score is saved once all are answered.
    let right = 0, answered = 0;
    E.view.querySelectorAll(".sq").forEach((box) => {
      const q = d.questions[box.dataset.i];
      box.querySelectorAll(".opt").forEach((b) => (b.onclick = () => {
        box.querySelectorAll(".opt").forEach((x) => { x.disabled = true; if (x.textContent === q.answer) x.classList.add("right"); });
        if (b.textContent === q.answer) right++; else b.classList.add("wrong");
        if (q.why) { const w = box.querySelector(".sq-why"); w.textContent = q.why; w.hidden = false; }
        if (++answered === d.questions.length) {
          const p = E.progress, key = "dialects/" + id;
          p.library = p.library || {}; p.library[key] = Math.max(p.library[key] || 0, right / answered); E.saveProgress();
          E.$("#sq-score").textContent = `${right} of ${answered} right`;
        }
      }));
    });
    window.scrollTo(0, 0);
  }

  routes.dialects = async (id) => {
    style();
    try { await (id ? doc(id) : shelf()); }
    catch (e) { A().view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><p>The dialect pages could not load: ${A().esc(e.message)}</p>`; }
  };
})();
