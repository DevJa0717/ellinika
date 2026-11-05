/* Ελληνικά grammar outline (#theoria): a Schaum's-style guide. Every chapter gives concise theory with everyday examples,
   solved problems with worked answers, then drills. Every drill you answer joins a spaced-repetition schedule
   (Leitner boxes: 1, 3, 7, 14, 30, 60, 120 days); a miss comes back the same day and climbs again from the bottom.
   Content is data: library/theoria/<id>.json, index.json, drills.json and references.json, built from
   library/theoria/src/*.txt by build.py. Progress is per profile in localStorage "ellinika.theoria.v1".
   Routes: #theoria (contents and review), #theoria.<chapter>[~section], #theoria.review, #theoria.drill~<chapter>,
   #theoria.weak, #theoria.refs, #theoria.path (graded cumulative review) and #theoria.path~<stage>. The interface switches between English and Greek (button at the top). */
(function () {
  "use strict";
  const A = () => window.Ellinika;
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});
  const KEY = "ellinika.theoria.v1";
  const BASE = "library/theoria/";
  const PDF = "downloads/textbook/Ellinika-Grammar-outline.pdf";
  const GAPS = [0, 1, 3, 7, 14, 30, 60, 120]; // days until the next review, by box; box 5 and up counts as mastered
  const MASTER = 5;

  /* ---------- interface language ---------- */
  const T = {
    en: {
      head: "Grammar outline", res: "← Resources", sub: "A Schaum's-style grammar of Modern Greek: each chapter gives the rule in a few lines, everyday examples, solved problems with the working shown, then drills. Every drill you answer joins your spaced-repetition schedule, so what you miss comes back until it sticks.",
      chapters: "chapters", solved: "solved problems", drills: "drills", practised: "drills practised", due: "due today", mastered: "mastered",
      review: "Review due drills", reviewN: (n) => `${n} drill${n === 1 ? " is" : "s are"} due for review.`, nothingDue: "Nothing due right now.",
      weak: "Practise weak spots", refs: "References and validation", pdf: "PDF (theory, problems and answer key)",
      contents: "Contents", parts: "parts", practise: "Practise this chapter", next: "Next", all: "All chapters",
      solvedH: "Solved problems", drillsH: "Drills", solution: "Solution", choose: "Choose", order: "Put the words in order", write: "Write",
      check: "Check", undo: "Undo", answer: "Answer", nearly: "Nearly: check the accents or the final -ν. ", greek: "Greek",
      score: (r, a, t) => `Drills: ${r} of ${a} right${a < t ? `, ${t - a} to go` : ""}. Every answer is now in your review schedule.`,
      sessionDone: "Session complete", right: "right", again: "Misses come back today and then climb again: 1, 3, 7, 14, 30 days.",
      cont: "Continue", back: "Back to the outline", of: "of", from: "From", newItems: "new", dueItems: "due", inBox: "next review",
      days: (n) => n === 0 ? "today" : n === 1 ? "tomorrow" : `in ${n} days`, deeper: "Go deeper in the app", lang: "Ελληνικά",
      problem: "Problem", sessionEmpty: "No drills to practise here yet.", reset: "Reset this chapter's progress", resetQ: "Forget your answers for this chapter? Its drills will start again as new.",
      progress: (s, n) => `${s} of ${n} drills practised`, weakEmpty: "No weak spots yet: answer some drills first.",
      path: "Graded review path", pathSub: "Short mixed tests that follow the outline from chapter 1 to the end. Each stage tests a few chapters and brings back earlier ones, so what you learned first is not forgotten. Score 80% to open the next stage; every answer also joins your review schedule.",
      stage: "Stage", checkpoint: "Checkpoint", final: "Final review", chs: "Chapters", plusEarlier: "with earlier chapters", best: "best", start: "Start", retry: "Try again", locked: "Pass the stage before to open this one.",
      passed: (p) => `Passed with ${p}%. The next stage is open.`, notYet: (p) => `${p}%. 80% opens the next stage: the misses are in your review schedule, so try again after a look at their chapters.`,
      nextStage: "Next stage", pathProg: (a, n) => `${a} of ${n} stages passed`, pathAll: "Back to the path",
    },
    el: {
      head: "Γραμματική σε θεωρία και ασκήσεις", res: "← Βοηθήματα", sub: "Μια γραμματική της νέας ελληνικής σε στιλ Schaum: κάθε κεφάλαιο δίνει τον κανόνα σε λίγες γραμμές, καθημερινά παραδείγματα, λυμένες ασκήσεις με τη λύση τους και μετά ασκήσεις εξάσκησης. Κάθε άσκηση που απαντάτε μπαίνει στο πρόγραμμα επαναλήψεων, έτσι ό,τι χάνετε επιστρέφει ώσπου να το μάθετε.",
      chapters: "κεφάλαια", solved: "λυμένες ασκήσεις", drills: "ασκήσεις", practised: "ασκήσεις που κάνατε", due: "για σήμερα", mastered: "κατακτημένες",
      review: "Επανάληψη", reviewN: (n) => n === 1 ? "1 άσκηση περιμένει επανάληψη." : `${n} ασκήσεις περιμένουν επανάληψη.`, nothingDue: "Δεν υπάρχει τίποτα για επανάληψη τώρα.",
      weak: "Τα αδύνατα σημεία μου", refs: "Βιβλιογραφία και έλεγχος", pdf: "PDF (θεωρία, ασκήσεις και λύσεις)",
      contents: "Περιεχόμενα", parts: "ενότητες", practise: "Εξάσκηση στο κεφάλαιο", next: "Επόμενο", all: "Όλα τα κεφάλαια",
      solvedH: "Λυμένες ασκήσεις", drillsH: "Ασκήσεις", solution: "Λύση", choose: "Διαλέξτε", order: "Βάλτε τις λέξεις στη σειρά", write: "Γράψτε",
      check: "Έλεγχος", undo: "Αναίρεση", answer: "Απάντηση", nearly: "Σχεδόν: κοιτάξτε τους τόνους ή το τελικό -ν. ", greek: "Ελληνικά",
      score: (r, a, t) => `Ασκήσεις: ${r} σωστές από ${a}${a < t ? `, απομένουν ${t - a}` : ""}. Όλες οι απαντήσεις μπήκαν στο πρόγραμμα επαναλήψεων.`,
      sessionDone: "Τέλος", right: "σωστές", again: "Τα λάθη επιστρέφουν σήμερα και μετά ανεβαίνουν ξανά: 1, 3, 7, 14, 30 μέρες.",
      cont: "Συνέχεια", back: "Πίσω στον οδηγό", of: "από", from: "Από", newItems: "νέες", dueItems: "για επανάληψη", inBox: "επόμενη επανάληψη",
      days: (n) => n === 0 ? "σήμερα" : n === 1 ? "αύριο" : `σε ${n} μέρες`, deeper: "Περισσότερα στην εφαρμογή", lang: "English",
      problem: "Άσκηση", sessionEmpty: "Δεν υπάρχουν ακόμα ασκήσεις εδώ.", reset: "Μηδενισμός προόδου κεφαλαίου", resetQ: "Να ξεχαστούν οι απαντήσεις σας σε αυτό το κεφάλαιο; Οι ασκήσεις του θα ξεκινήσουν πάλι ως νέες.",
      progress: (s, n) => `${s} από ${n} ασκήσεις`, weakEmpty: "Δεν υπάρχουν ακόμα αδύνατα σημεία: κάντε πρώτα μερικές ασκήσεις.",
      path: "Διαβαθμισμένη πορεία επανάληψης", pathSub: "Σύντομα μικτά τεστ που ακολουθούν τον οδηγό από το πρώτο κεφάλαιο ως το τέλος. Κάθε στάδιο εξετάζει λίγα κεφάλαια και φέρνει πίσω και προηγούμενα, για να μην ξεχνιούνται όσα μάθατε πρώτα. Με 80% ανοίγει το επόμενο στάδιο· κάθε απάντηση μπαίνει και στο πρόγραμμα επαναλήψεων.",
      stage: "Στάδιο", checkpoint: "Έλεγχος ενότητας", final: "Τελική επανάληψη", chs: "Κεφάλαια", plusEarlier: "και προηγούμενα κεφάλαια", best: "καλύτερο", start: "Έναρξη", retry: "Ξανά", locked: "Περάστε πρώτα το προηγούμενο στάδιο.",
      passed: (p) => `Περάσατε με ${p}%. Το επόμενο στάδιο άνοιξε.`, notYet: (p) => `${p}%. Με 80% ανοίγει το επόμενο στάδιο: τα λάθη μπήκαν στο πρόγραμμα επαναλήψεων, δείτε τα κεφάλαιά τους και δοκιμάστε ξανά.`,
      nextStage: "Επόμενο στάδιο", pathProg: (a, n) => `${a} από ${n} στάδια`, pathAll: "Πίσω στην πορεία",
    },
  };

  /* ---------- state (per profile) ---------- */
  // it[id] = [box, due day, right, wrong]
  let ST = null;
  function load() {
    if (ST) return ST;
    let s = null; try { s = JSON.parse(localStorage.getItem(KEY)); } catch (e) { /* none */ }
    ST = s && s.it ? s : { it: {}, ui: "en" };
    return ST;
  }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(ST)); } catch (e) { /* storage full or blocked */ } }
  window.addEventListener("ellinika:profile", () => { ST = null; });
  const t = () => T[load().ui === "el" ? "el" : "en"];
  const today = () => { const d = new Date(); return Math.floor((d.getTime() - d.getTimezoneOffset() * 6e4 - 4 * 36e5) / 864e5); };
  function schedule(id, ok) {
    const s = load(), r = s.it[id] || [0, -1, 0, 0];
    const fresh = !s.it[id];
    if (ok) { r[0] = fresh ? 2 : Math.min(r[0] + 1, GAPS.length - 1); r[2]++; }
    else { r[0] = 1; r[3]++; }
    r[1] = today() + (ok ? GAPS[r[0]] : 0);
    s.it[id] = r; save();
    return r;
  }
  const isDue = (r) => r && r[1] <= today();

  /* ---------- styles ---------- */
  const CSS = `
.th-hero h2 { margin: 0; font: 400 2rem/1.15 var(--f-display); }
.th-hero .ex-en { display: block; margin-top: 2px; }
.th-top { display: flex; justify-content: space-between; align-items: center; gap: 8px; flex-wrap: wrap; }
.th-lang { min-height: 36px; }
.th-pathcard { display: flex; justify-content: space-between; align-items: center; gap: 12px; }
.th-pathcard b { display: block; font: 600 1rem/1.3 var(--f-ui); }
.th-path { list-style: none; padding: 0; margin: 14px 0; display: grid; gap: 8px; }
.th-ppart { font: 600 .8rem/1.3 var(--f-ui); color: var(--muted); margin-top: 10px; text-transform: none; }
.th-stg { display: grid; grid-template-columns: 2.2rem 1fr auto; gap: 10px; align-items: center; background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 10px 12px; }
.th-stg.lock { opacity: .55; }
.th-stg .th-sn { font: 400 1.3rem/1 var(--f-display); color: var(--terra); text-align: center; font-variant-numeric: tabular-nums; }
.th-stg.ok .th-sn { color: var(--olive, #5a7d3a); }
.th-stg .th-sb { min-width: 0; }
.th-stg .th-sb b { font: 600 .95rem/1.3 var(--f-ui); margin-right: 6px; }
.th-stg .ex-en { display: block; }
.th-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; margin: 14px 0; }
.th-stat { background: var(--card); border: 1px solid var(--line); border-radius: 10px; padding: 10px 6px; text-align: center; }
.th-stat b { display: block; font: 400 1.6rem/1.1 var(--f-display); font-variant-numeric: tabular-nums; }
.th-stat span { font: 500 .75rem/1.2 var(--f-ui); color: var(--muted); }
.th-due { display: flex; gap: 10px; align-items: center; justify-content: space-between; flex-wrap: wrap; }
.th-acts { display: flex; gap: 8px; flex-wrap: wrap; margin: 10px 0 18px; }
.th-part { margin: 22px 0 8px; display: grid; gap: 2px; }
.th-part .th-pn { font: 600 .72rem/1.2 var(--f-ui); letter-spacing: .12em; text-transform: uppercase; color: var(--terra); }
.th-part h3 { margin: 0; font: 400 1.35rem/1.2 var(--f-display); }
.th-list { list-style: none; margin: 0; padding: 0; display: grid; gap: 8px; }
.th-ch { display: grid; grid-template-columns: 2.4rem 1fr; gap: 10px; align-items: start; text-decoration: none; color: var(--ink); background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 12px; }
.th-ch:hover { border-color: var(--terra); }
.th-ch .n { font: 400 1.5rem/1 var(--f-display); color: var(--terra); text-align: center; padding-top: 2px; font-variant-numeric: tabular-nums; }
.th-ch .el { font: 400 1.15rem/1.25 var(--f-display); display: block; }
.th-ch .en { font: 500 .82rem/1.3 var(--f-ui); color: var(--muted); display: block; }
.th-ch .meta { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; margin-top: 6px; font: 500 .75rem/1.2 var(--f-ui); color: var(--muted); }
.th-meter { height: 5px; border-radius: 3px; background: var(--paper); overflow: hidden; margin-top: 6px; }
.th-meter i { display: block; height: 100%; background: var(--good); }
.th-doc { display: grid; gap: 14px; }
.th-doc .card { gap: 12px; }
.th-doc p { margin: 0; }
.th-sec { scroll-margin-top: 80px; }
.th-sec h3 { display: grid; gap: 2px; margin: 0; font: 400 1.45rem/1.2 var(--f-display); }
.th-sec h3 .ex-en { font-size: .85rem; }
.th-head { display: flex; justify-content: space-between; align-items: center; gap: 8px; }
.th-num { font: 600 .8rem/1 var(--f-ui); color: var(--muted); font-variant-numeric: tabular-nums; }
.th-tip { border-left-color: var(--terra); background: rgba(242, 193, 78, .07); border-radius: 0 8px 8px 0; padding: 10px 12px 10px 14px; }
.th-ex { border-left: 2px solid var(--line); padding-left: 12px; }
table.th-tbl td { font-size: 1rem; }
table.th-tbl th[scope="row"] { text-transform: none; letter-spacing: 0; font-size: .85rem; }
.th-toc summary { cursor: pointer; font: 600 .9rem/1.3 var(--f-ui); }
.th-toc ol { margin: 0; padding-left: 0; list-style: none; display: grid; gap: 2px; }
.th-jump { all: unset; cursor: pointer; display: block; padding: 7px 4px; border-radius: 6px; line-height: 1.35; }
.th-jump:hover, .th-jump:focus-visible { background: rgba(127, 127, 127, .12); }
.th-h { font: 600 .72rem/1.2 var(--f-ui); letter-spacing: .12em; text-transform: uppercase; color: var(--terra); }
.th-solved { display: grid; gap: 10px; background: rgba(127, 127, 127, .05); border-radius: 10px; padding: 12px; }
.th-sp { display: grid; gap: 4px; }
.th-sp .pq { font-weight: 500; }
.th-sp .pq b.pn { font: 600 .78rem/1 var(--f-ui); color: var(--muted); margin-right: 6px; font-variant-numeric: tabular-nums; }
.th-sp .pa { padding-left: 12px; border-left: 2px solid var(--good); }
.th-sp .pa .lbl { font: 600 .7rem/1 var(--f-ui); letter-spacing: .08em; text-transform: uppercase; color: var(--good); margin-right: 6px; }
.th-sp .pw { font-size: .9rem; color: var(--muted); padding-left: 14px; }
.th-check { display: grid; gap: 18px; border-top: 1px dashed var(--line); padding-top: 12px; }
.th-q .q-prompt { margin: 0 0 8px; }
.th-kind { font: 600 .68rem/1 var(--f-ui); letter-spacing: .06em; text-transform: uppercase; color: var(--muted); margin-bottom: 4px; display: flex; gap: 8px; justify-content: space-between; }
.th-kind .th-box { text-transform: none; letter-spacing: 0; font-weight: 500; }
.th-built { min-height: 2.9rem; display: flex; flex-wrap: wrap; gap: 6px; align-items: center; padding: 8px; border: 1px dashed var(--line); border-radius: 8px; }
.th-built.right { border-style: solid; border-color: var(--good); background: var(--good-soft); }
.th-built.wrong { border-style: solid; border-color: var(--bad); background: var(--bad-soft); }
.th-tiles { display: flex; flex-wrap: wrap; gap: 6px; margin: 8px 0; }
.th-tile { padding: 8px 11px; border: 1px solid var(--line); border-radius: 8px; background: var(--paper); color: var(--ink); font-size: 1.05rem; cursor: pointer; }
.th-tile:disabled { opacity: .3; cursor: default; }
.th-btns { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 4px; }
.th-why, .th-ans { margin-top: 8px !important; }
.th-links { display: grid; gap: 6px; }
.th-links ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 6px; }
.th-links a { display: inline-flex; gap: 6px; align-items: baseline; padding: 6px 10px; border: 1px solid var(--line); border-radius: 999px; text-decoration: none; color: inherit; font-size: .9rem; line-height: 1.3; }
.th-links a:hover { border-color: var(--terra); }
.th-links .lk-k { font: 600 .62rem/1 var(--f-ui); letter-spacing: .06em; text-transform: uppercase; color: var(--terra); }
.th-nav { display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap; }
.th-sess { gap: 12px; }
.th-sess .th-from { font: 500 .8rem/1.3 var(--f-ui); color: var(--muted); }
.th-sess .th-from a { color: inherit; }
.th-bar { height: 4px; background: var(--paper); border-radius: 2px; overflow: hidden; }
.th-bar i { display: block; height: 100%; background: var(--terra); transition: width .2s; }
.th-sess .q-prompt { font-size: 1.15rem; line-height: 1.5; }
.th-sess .answer-row input { font-size: 1.15rem; }
.th-refs li { margin: 6px 0; line-height: 1.45; }
@media print {
  .ell-nav, .bar, .crumbs, .th-acts, .th-nav, .th-check, .th-links, .th-toc, .th-lang, .lk-pop, #keypad { display: none !important; }
}
`;
  if (!document.getElementById("th-css")) { const st = document.createElement("style"); st.id = "th-css"; st.textContent = CSS; document.head.appendChild(st); }

  /* ---------- data ---------- */
  let idxP, bankP, glossP;
  const index = (E) => (idxP = idxP || E.getJSON(BASE + "index.json").catch(() => { idxP = null; return { items: [] }; }));
  const bank = (E) => (bankP = bankP || E.getJSON(BASE + "drills.json").catch(() => { bankP = null; return {}; }));
  const gloss = (E) => (glossP = glossP || Promise.all([E.getJSON(BASE + "gloss.json").catch(() => ({})), E.getJSON("library/syntax/gloss.json").catch(() => ({}))]).then(([a, b]) => ({ ...b, ...a })));

  /* ---------- grading (shared with the syntax guide): case, punctuation and spacing never count; accents and final -ν are "nearly" ---------- */
  const ACC = { "ά": "α", "έ": "ε", "ή": "η", "ί": "ι", "ό": "ο", "ύ": "υ", "ώ": "ω", "ΐ": "ϊ", "ΰ": "ϋ" };
  const norm = (s) => String(s).normalize("NFC").toLowerCase().replace(/\*+/g, "").replace(/[’‘`΄]/g, "'").replace(/ό,\s?τι/g, "ό|τι")
    .replace(/[.,;;!?·«»"“”()…\-–—]/g, " ").replace(/σ(?=\s|$)/g, "ς").replace(/\s+/g, " ").trim();
  const loose = (s) => norm(s).replace(/[άέήίόύώΐΰ]/g, (c) => ACC[c]).replace(/(^|\s)(σ?τη|αυτη|δε|μη|καμια)ν(?=\s|$)/g, "$1$2");
  const grade = (input, forms) => forms.some((f) => norm(f) === norm(input)) ? "right" : forms.some((f) => loose(f) === loose(input)) ? "almost" : "wrong";
  const words = (s) => String(s).replace(/[.;;!?·]+$/, "").split(/\s+/).filter(Boolean);
  const shuffle = (a, seed) => { const r = a.slice(); let x = seed || 7; for (let i = r.length - 1; i > 0; i--) { x = (x * 9301 + 49297) % 233280; const j = Math.floor((x / 233280) * (i + 1)); [r[i], r[j]] = [r[j], r[i]]; } return r; };
  const rshuffle = (a) => { const r = a.slice(); for (let i = r.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [r[i], r[j]] = [r[j], r[i]]; } return r; };
  const hash = (s) => { let h = 7; for (const c of s) h = (h * 31 + c.charCodeAt(0)) % 100003; return h; };

  /* ---------- graded review path: stages of up to three chapters in book order, a checkpoint at the end of every part,
     then a final review. Each test mixes the stage's chapters (14 drills) with earlier chapters (6), favouring what is
     new or was missed. 80% opens the next stage; the best score per stage is kept in state.path. ---------- */
  const PASS = 0.8;
  function stages(idx) {
    const parts = [];
    idx.items.forEach((x) => { if (x.part || !parts.length) parts.push({ part: x.part, chs: [] }); parts[parts.length - 1].chs.push(x); });
    const out = [];
    parts.forEach((pt) => {
      const n = Math.ceil(pt.chs.length / 3);
      for (let i = 0; i < n; i++) {
        const lo = Math.round((i * pt.chs.length) / n), hi = Math.round(((i + 1) * pt.chs.length) / n);
        out.push({ kind: "stage", chs: pt.chs.slice(lo, hi), part: pt.part });
      }
      if (n > 1) out.push({ kind: "check", chs: pt.chs, part: pt.part });
    });
    out.push({ kind: "final", chs: idx.items, part: null });
    out.forEach((st, i) => {
      st.key = st.kind + ":" + st.chs.map((c) => c.id).join(",");
      st.n = i + 1;
      const first = idx.items.indexOf(st.chs[0]);
      st.earlier = st.kind === "final" ? [] : idx.items.slice(0, first);
      const lv = st.chs.map((c) => c.span || "").join(" ").match(/[ABC][12]/g) || [];
      st.span = lv.length ? (lv.sort()[0] === lv.sort()[lv.length - 1] ? lv[0] : lv.sort()[0] + "–" + lv.sort()[lv.length - 1]) : "";
    });
    return out;
  }
  function pick(ids, n, s) {
    // new and missed first, then the weakest boxes; random within each group
    const w = (id) => { const r = s.it[id]; return !r ? 0 : r[3] > r[2] ? 1 : 2 + r[0]; };
    const groups = {};
    rshuffle(ids).forEach((id) => (groups[w(id)] = groups[w(id)] || []).push(id));
    return Object.keys(groups).sort((a, b) => a - b).flatMap((k) => groups[k]).slice(0, n);
  }
  function stageIds(st, B, s) {
    const per = (chs, n) => {
      // spread over the chapters: an even share from each, the rest from the pool
      const pools = chs.map((c) => c.ids.filter((id) => B[id]));
      const share = Math.max(1, Math.floor(n / Math.max(1, chs.length)));
      let got = pools.flatMap((p) => pick(p, share, s));
      if (got.length > n) got = rshuffle(got).slice(0, n);
      if (got.length < n) got = got.concat(pick(pools.flat().filter((id) => !got.includes(id)), n - got.length, s));
      return got;
    };
    if (st.kind === "final") return rshuffle(per(st.chs, 30));
    const own = per(st.chs, 14), old = st.earlier.length ? pick(st.earlier.flatMap((c) => c.ids.filter((id) => B[id])), 6, s) : [];
    return rshuffle(own.concat(old));
  }
  const stageOpen = (all, i, s) => i === 0 || all.slice(0, i).every((x) => (s.path || {})[x.key] >= PASS * 100);
  const stageName = (L, st) => st.kind === "check" ? `${L.checkpoint}: ${st.part ? st.part[1] : ""}` : st.kind === "final" ? L.final : `${L.stage} ${st.n}`;

  /* ---------- rendering ---------- */
  const linksHTML = (E, b) => !b.links.length ? "" : `<nav class="th-links"><span class="th-h">${t().deeper}</span><ul>${b.links.map((l) =>
    `<li><a href="${E.esc(l.href)}"><span class="lk-k">${E.esc(l.kind)}</span><span lang="el">${E.esc(l.el)}</span></a></li>`).join("")}</ul></nav>`;

  function boxNote(id) {
    const r = load().it[id]; if (!r) return "";
    return `${t().inBox}: ${t().days(Math.max(0, r[1] - today()))}`;
  }

  function qHTML(E, q, n) {
    const L = t();
    const kind = { choice: L.choose, order: L.order, write: L.write }[q.type];
    const head = `<span class="th-kind"><span>${kind}</span><span class="th-box">${boxNote(q.id)}</span></span><p class="q-prompt">${E.md(q.q)}</p>`;
    const tail = `<p class="ex-en th-ans" hidden></p><p class="ex-en th-why" hidden></p>`;
    if (q.type === "choice") {
      const opts = shuffle(q.options, hash(q.id || q.q));
      return `<div class="th-q" data-n="${n}" data-o="${E.esc(JSON.stringify(opts))}">${head}<div class="options">${opts.map((o) => `<button class="opt" lang="el">${E.md(o)}</button>`).join("")}</div>${tail}</div>`;
    }
    if (q.type === "order") return `<div class="th-q" data-n="${n}">${head}<div class="th-built" lang="el" aria-live="polite"></div><div class="th-tiles"></div>
      <div class="th-btns"><button class="btn small th-cb">${L.check}</button><button class="btn small ghost th-undo">${L.undo}</button></div>${tail}</div>`;
    return `<div class="th-q" data-n="${n}">${head}<form class="answer-row"><input lang="el" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" placeholder="${L.greek}"><button class="btn">${L.check}</button></form>${tail}</div>`;
  }

  // Wires one rendered question box; onAnswer(ok) runs once.
  function wireQ(E, box, q, onAnswer) {
    const L = t();
    const finish = (ok, shown) => {
      const r = q.id ? schedule(q.id, ok) : null;
      const ans = box.querySelector(".th-ans");
      if (shown) { ans.innerHTML = shown; ans.hidden = false; }
      if (q.why) { const w = box.querySelector(".th-why"); w.innerHTML = E.md(q.why); w.hidden = false; E.wrapGreek(w); }
      E.wrapGreek(ans);
      if (r) box.querySelector(".th-box").textContent = `${L.inBox}: ${L.days(Math.max(0, r[1] - today()))}`;
      onAnswer(ok);
    };
    const answerLine = () => `${L.answer}: <span lang="el">${E.md([q.answer, ...(q.accept || [])].join(" · "))}</span>`;
    if (q.type === "choice") {
      const opts = JSON.parse(box.dataset.o);
      box.querySelectorAll(".opt").forEach((b, k) => (b.onclick = () => {
        box.querySelectorAll(".opt").forEach((x, j) => { x.disabled = true; if (opts[j] === q.answer) x.classList.add("right"); });
        const ok = opts[k] === q.answer; if (!ok) b.classList.add("wrong");
        finish(ok, "");
      }));
    } else if (q.type === "order") {
      const ws = words(q.answer), end = (q.answer.match(/[.;;!?·]+$/) || [""])[0];
      const tiles = shuffle(ws.map((w, i) => ({ w: i === 0 && !q.keepCase ? w.charAt(0).toLowerCase() + w.slice(1) : w, i })), hash(q.id || q.q) + ws.length);
      const built = box.querySelector(".th-built"), tl = box.querySelector(".th-tiles"), picked = [];
      tl.innerHTML = tiles.map((x, k) => `<button class="th-tile" data-k="${k}" lang="el">${E.esc(x.w)}</button>`).join("");
      const draw = () => { built.textContent = picked.map((k) => tiles[k].w).join(" "); };
      tl.querySelectorAll(".th-tile").forEach((b) => (b.onclick = () => { picked.push(+b.dataset.k); b.disabled = true; draw(); }));
      box.querySelector(".th-undo").onclick = () => { const k = picked.pop(); if (k != null) tl.querySelector(`[data-k="${k}"]`).disabled = false; draw(); };
      box.querySelector(".th-cb").onclick = (ev) => {
        if (picked.length < tiles.length) { built.classList.add("wrong"); setTimeout(() => built.classList.remove("wrong"), 600); return; }
        const said = picked.map((k) => tiles[k].w).join(" ") + end;
        const ok = [q.answer, ...(q.accept || [])].some((f) => norm(f) === norm(said));
        built.classList.add(ok ? "right" : "wrong");
        tl.querySelectorAll("button").forEach((b) => (b.disabled = true)); ev.target.disabled = true; box.querySelector(".th-undo").disabled = true;
        finish(ok, ok ? "" : answerLine());
      };
    } else {
      const form = box.querySelector("form"), inp = form.querySelector("input");
      form.onsubmit = (ev) => {
        ev.preventDefault(); if (!inp.value.trim()) return;
        const g = grade(inp.value, [q.answer, ...(q.accept || [])]);
        inp.classList.add(g); inp.readOnly = true; form.querySelector("button").disabled = true;
        finish(g !== "wrong", g === "right" ? "" : (g === "almost" ? L.nearly : "") + answerLine());
      };
    }
  }

  function block(E, b, ctx) {
    if (b.p != null) return `<p>${E.md(b.p)}</p>`;
    if (b.tip != null) return `<div class="callout th-tip"><p>${E.md(b.tip)}</p></div>`;
    if (b.list) return `<ul class="ref-notes">${b.list.map((x) => `<li>${E.md(x)}</li>`).join("")}</ul>`;
    if (b.ex) return `<ul class="ex-list th-ex">${b.ex.map((x) => `<li><span class="ex-el" lang="el">${E.md(x.el)}</span>${x.en ? `<span class="ex-en">${E.md(x.en)}</span>` : ""}</li>`).join("")}</ul>`;
    if (b.links) return linksHTML(E, b);
    if (b.table) {
      const tb = b.table, blank = tb.head.every((h) => !h);
      return `<div class="tbl-wrap"><table class="th-tbl">${blank ? "" : `<thead><tr>${tb.head.map((h) => `<th scope="col">${E.md(h)}</th>`).join("")}</tr></thead>`}
        <tbody>${tb.rows.map((r) => `<tr>${r.map((c, i) => i === 0 && !blank ? `<th scope="row">${E.md(c)}</th>` : `<td>${E.md(c)}</td>`).join("")}</tr>`).join("")}</tbody></table></div>`;
    }
    if (b.solved) return `<div class="th-solved"><span class="th-h">${t().solvedH}</span>${b.solved.map((p) => {
      ctx.p++;
      return `<div class="th-sp"><p class="pq"><b class="pn">${ctx.num}.${ctx.p}</b>${E.md(p.q)}</p><p class="pa"><span class="lbl">${t().solution}</span>${E.md(p.a)}</p>${p.why ? `<p class="pw">${E.md(p.why)}</p>` : ""}</div>`;
    }).join("")}</div>`;
    if (b.check) return `<div class="th-check"><span class="th-h">${t().drillsH}</span>${b.check.map((q) => { ctx.qs.push(q); return qHTML(E, q, ctx.qs.length - 1); }).join("")}</div>`;
    return "";
  }

  const langBtn = () => `<button class="btn small ghost th-lang" id="th-lang" lang="${load().ui === "el" ? "en" : "el"}">${t().lang}</button>`;
  function wireLang(rerender) {
    const b = document.getElementById("th-lang"); if (!b) return;
    b.onclick = () => { const s = load(); s.ui = s.ui === "el" ? "en" : "el"; save(); rerender(); };
  }

  /* ---------- #theoria ---------- */
  async function home(E) {
    const L = t(), idx = await index(E), s = load();
    document.title = L.head + " · Ελληνικά";
    const allIds = idx.items.flatMap((x) => x.ids);
    const seen = allIds.filter((id) => s.it[id]).length, due = allIds.filter((id) => isDue(s.it[id])).length;
    const mast = allIds.filter((id) => s.it[id] && s.it[id][0] >= MASTER).length;
    const tot = idx.items.reduce((a, x) => [a[0] + x.solved, a[1] + x.questions], [0, 0]);
    let html = `<div class="th-top"><p class="crumbs"><a href="#library">${L.res}</a></p>${langBtn()}</div>
      <div class="th-hero"><h2 lang="el">Γραμματική σε θεωρία και ασκήσεις</h2><span class="ex-en">Grammar outline · Schaum's-style · A1–C1</span></div>
      <p class="sub">${L.sub} ${idx.items.length} ${L.chapters} · ${tot[0]} ${L.solved} · ${tot[1]} ${L.drills}.</p>
      <div class="th-stats"><div class="th-stat"><b>${seen}</b><span>${L.practised}</span></div><div class="th-stat"><b>${due}</b><span>${L.due}</span></div><div class="th-stat"><b>${mast}</b><span>${L.mastered}</span></div></div>
      ${due ? `<section class="card th-due"><span>${L.reviewN(due)}</span><a class="btn small" href="#theoria.review">${L.review}</a></section>` : ""}
      <section class="card th-pathcard"><div><b>${L.path}</b><span class="ex-en">${L.pathProg(stages(idx).filter((x) => (s.path || {})[x.key] >= PASS * 100).length, stages(idx).length)}</span></div><a class="btn small" href="#theoria.path">${L.start}</a></section>
      <div class="th-acts">${seen ? `<a class="btn ghost small" href="#theoria.weak">${L.weak}</a>` : ""}<a class="btn ghost small" href="#theoria.refs">${L.refs}</a><a class="btn ghost small" href="${PDF}" target="_blank" rel="noopener">${L.pdf}</a></div>`;
    let open = false;
    idx.items.forEach((x) => {
      if (x.part) {
        if (open) html += `</ul>`;
        html += `<div class="th-part"><span class="th-pn">${E.esc(x.part[0])}</span><h3><span lang="el">${E.esc(x.part[1])}</span> <span class="ex-en">${E.esc(x.part[2] || "")}</span></h3></div><ul class="th-list">`;
        open = true;
      } else if (!open) { html += `<ul class="th-list">`; open = true; }
      const done = x.ids.filter((id) => s.it[id]).length, d = x.ids.filter((id) => isDue(s.it[id])).length;
      html += `<li><a class="th-ch" href="#theoria.${E.esc(x.id)}"><span class="n">${x.num}</span><span>
        <span class="el" lang="el">${E.esc(x.el)}</span><span class="en">${E.esc(x.title)}</span>
        <span class="meta"><span class="chip">${E.esc(x.span)}</span><span>${x.solved} ${L.solved} · ${x.questions} ${L.drills}</span>${d ? `<span class="chip new">${d} ${L.dueItems}</span>` : ""}</span>
        ${done ? `<span class="th-meter" title="${L.progress(done, x.questions)}"><i style="width:${Math.round((done / x.questions) * 100)}%"></i></span>` : ""}</span></a></li>`;
    });
    if (open) html += `</ul>`;
    E.view.innerHTML = html;
    E.wrapGreek(E.view.querySelector(".sub"));
    wireLang(() => home(E));
    window.scrollTo(0, 0);
  }

  async function chapter(E, id, sec) {
    const L = t(), idx = await index(E);
    const meta = idx.items.find((x) => x.id === id);
    if (!meta) { location.hash = "theoria"; return; }
    const d = await E.getJSON(BASE + meta.file);
    document.title = d.el + " · " + L.head;
    E.setGloss(await gloss(E));
    const pos = idx.items.indexOf(meta), prev = idx.items[pos - 1], next = idx.items[pos + 1];
    const ctx = { num: meta.num, p: 0, qs: [] };
    const body = d.sections.map((s, i) => `<section class="card th-sec" id="th-s${i}">
        <div class="th-head"><span class="chip">${E.esc(s.level)}</span><span class="th-num">${meta.num}.${i + 1}</span></div>
        <h3><span lang="el">${E.esc(s.el)}</span><span class="ex-en">${E.esc(s.title)}</span></h3>
        ${s.body.map((b) => block(E, b, ctx)).join("")}</section>`).join("");
    const intro = d.intro.map((b) => block(E, b, ctx)).join("");
    E.view.innerHTML = `<div class="th-top"><p class="crumbs"><a href="#theoria">← ${L.head}</a></p>${langBtn()}</div>
      <div class="story-head"><span class="chip">${E.esc(d.span || "")}</span><h2 lang="el">${meta.num}. ${E.esc(d.el)}</h2><span class="ex-en">${E.esc(d.title)}</span></div>
      <div class="th-doc">
      ${intro ? `<section class="card">${intro}</section>` : ""}
      <details class="card th-toc" open><summary>${L.contents} · ${d.sections.length} ${L.parts} · ${meta.solved} ${L.solved} · ${ctx.qs.length} ${L.drills}</summary>
        <ol>${d.sections.map((s, i) => `<li><button class="th-jump" data-i="${i}"><span class="chip">${E.esc(s.level)}</span> ${meta.num}.${i + 1} <span lang="el">${E.esc(s.el)}</span> <span class="ex-en">${E.esc(s.title)}</span></button></li>`).join("")}</ol></details>
      <div class="th-acts"><a class="btn small" href="#theoria.drill~${E.esc(id)}">${L.practise}</a></div>
      ${body}
      <p class="sub" id="th-score"></p>
      <nav class="th-nav">${prev ? `<a class="btn ghost" href="#theoria.${E.esc(prev.id)}">← <span lang="el">${E.esc(prev.el)}</span></a>` : "<span></span>"}
        ${next ? `<a class="btn" href="#theoria.${E.esc(next.id)}">${L.next}: <span lang="el">${E.esc(next.el)}</span></a>` : `<a class="btn" href="#theoria">${L.all}</a>`}</nav>
      <p><button class="linkish" id="th-reset">${L.reset}</button></p>
      </div>`;
    E.wrapGreek(E.view.querySelector(".th-doc"));
    E.view.querySelectorAll(".th-jump").forEach((b) => (b.onclick = () => E.$("#th-s" + b.dataset.i).scrollIntoView({ behavior: "smooth", block: "start" })));
    let right = 0, answered = 0;
    E.view.querySelectorAll(".th-q").forEach((box) => wireQ(E, box, ctx.qs[+box.dataset.n], (ok) => {
      answered++; if (ok) right++;
      E.$("#th-score").textContent = L.score(right, answered, ctx.qs.length);
    }));
    wireLang(() => chapter(E, id, sec));
    E.$("#th-reset").onclick = () => { if (confirm(L.resetQ)) { const s = load(); meta.ids.forEach((k) => delete s.it[k]); save(); chapter(E, id); } };
    if (sec && E.$("#th-s" + sec)) E.$("#th-s" + sec).scrollIntoView({ block: "start" });
    else window.scrollTo(0, 0);
  }

  /* ---------- sessions: one drill at a time ---------- */
  async function session(E, mode, chId) {
    const L = t(), idx = await index(E), B = await bank(E), s = load();
    E.setGloss(await gloss(E));
    const title = (c) => (idx.items.find((x) => x.id === c) || {});
    let ids;
    let st = null;
    if (mode === "path") {
      const all = stages(idx), i = all.findIndex((x) => String(x.n) === String(chId));
      st = all[i];
      if (!st || !stageOpen(all, i, s)) { location.hash = "theoria.path"; return; }
      ids = stageIds(st, B, s);
    } else if (mode === "review") ids = rshuffle(Object.keys(s.it).filter((id) => B[id] && isDue(s.it[id]))).slice(0, 40);
    else if (mode === "weak") {
      ids = Object.keys(s.it).filter((id) => B[id] && s.it[id][3] > 0).sort((a, b) => (s.it[b][3] - s.it[b][2] / 2) - (s.it[a][3] - s.it[a][2] / 2)).slice(0, 25);
      ids = rshuffle(ids);
    } else {
      const meta = title(chId); if (!meta.ids) { location.hash = "theoria"; return; }
      const all = meta.ids.filter((id) => B[id]);
      const due = all.filter((id) => isDue(s.it[id])), fresh = all.filter((id) => !s.it[id]);
      const rest = all.filter((id) => s.it[id] && !isDue(s.it[id])).sort((a, b) => s.it[a][0] - s.it[b][0]);
      ids = [...rshuffle(due), ...fresh, ...rest].slice(0, 15);
    }
    const back = mode === "drill" ? `#theoria.${chId}` : mode === "path" ? "#theoria.path" : "#theoria";
    const head = mode === "path" ? stageName(L, st) : mode === "review" ? L.review : mode === "weak" ? L.weak : `${title(chId).num}. ${title(chId).el}`;
    document.title = head + " · " + L.head;
    if (!ids.length) {
      E.view.innerHTML = `<p class="crumbs"><a href="${back}">← ${L.back}</a></p><section class="card"><p>${mode === "review" ? L.nothingDue : mode === "weak" ? L.weakEmpty : L.sessionEmpty}</p><p><a class="btn small" href="#theoria">${L.all}</a></p></section>`;
      return window.scrollTo(0, 0);
    }
    const queue = ids.slice(), retried = new Set();
    let k = 0, right = 0, firstTotal = ids.length;
    const draw = () => {
      if (k >= queue.length && mode === "path") {
        const pct = Math.round((right / firstTotal) * 100), sv = load();
        sv.path = sv.path || {}; sv.path[st.key] = Math.max(sv.path[st.key] || 0, pct); save();
        const ok = pct >= PASS * 100, all = stages(idx), nx = all[st.n];
        E.view.innerHTML = `<p class="crumbs"><a href="${back}">← ${L.pathAll}</a></p>
          <section class="card th-sess"><h3>${E.esc(stageName(L, st))}</h3><p><b>${right}</b> ${L.of} ${firstTotal} ${L.right}.</p><p class="sub">${ok ? L.passed(pct) : L.notYet(pct)}</p>
          <div class="th-btns">${ok && nx ? `<a class="btn" href="#theoria.path~${nx.n}">${L.nextStage}</a>` : `<button class="btn" id="th-more">${L.retry}</button>`}<a class="btn ghost" href="${back}">${L.pathAll}</a></div></section>`;
        const m = E.$("#th-more"); if (m) m.onclick = () => session(E, mode, chId);
        return window.scrollTo(0, 0);
      }
      if (k >= queue.length) {
        E.view.innerHTML = `<p class="crumbs"><a href="${back}">← ${L.back}</a></p>
          <section class="card th-sess"><h3 lang="${load().ui === "el" ? "el" : "en"}">${L.sessionDone}</h3><p><b>${right}</b> ${L.of} ${firstTotal} ${L.right}.</p><p class="sub">${L.again}</p>
          <div class="th-btns"><a class="btn" href="${back}">${L.back}</a>${mode === "drill" ? `<button class="btn ghost" id="th-more">${L.cont}</button>` : ""}</div></section>`;
        const m = E.$("#th-more"); if (m) m.onclick = () => session(E, mode, chId);
        return window.scrollTo(0, 0);
      }
      const id = queue[k], q = { ...B[id], id }, c = title(q.c);
      E.view.innerHTML = `<div class="th-top"><p class="crumbs"><a href="${back}">← ${L.back}</a></p><span class="th-num">${Math.min(k + 1, queue.length)} / ${queue.length}</span></div>
        <div class="th-bar"><i style="width:${Math.round((k / queue.length) * 100)}%"></i></div>
        <section class="card th-sess"><span class="th-from">${L.from}: <a href="#theoria.${E.esc(q.c)}~${q.s}">${c.num}. <span lang="el">${E.esc(c.el || "")}</span></a></span>
        ${qHTML(E, q, 0)}<div class="th-btns"><button class="btn" id="th-next" style="display:none">${L.next} →</button></div></section>`;
      const box = E.view.querySelector(".th-q");
      E.wrapGreek(box.querySelector(".q-prompt"));
      wireQ(E, box, q, (ok) => {
        if (ok && !retried.has(id)) right++;
        if (!ok && !retried.has(id)) { retried.add(id); queue.push(id); }
        const nb = E.$("#th-next"); nb.style.display = ""; nb.focus({ preventScroll: true });
        nb.onclick = () => { k++; draw(); };
      });
      const inp = box.querySelector("input"); if (inp) inp.focus({ preventScroll: true });
      window.scrollTo(0, 0);
    };
    draw();
  }

  async function pathPage(E) {
    const L = t(), idx = await index(E), s = load(), all = stages(idx);
    document.title = L.path + " · " + L.head;
    const done = all.filter((x) => (s.path || {})[x.key] >= PASS * 100).length;
    let html = `<div class="th-top"><p class="crumbs"><a href="#theoria">← ${L.head}</a></p>${langBtn()}</div>
      <div class="story-head"><h2>${L.path}</h2><span class="ex-en">${L.pathProg(done, all.length)}</span></div>
      <p class="sub">${L.pathSub}</p><div class="th-bar"><i style="width:${Math.round((done / all.length) * 100)}%"></i></div><ol class="th-path">`;
    let lastPart = null;
    all.forEach((st, i) => {
      if (st.part && st.part !== lastPart && st.kind === "stage") { html += `<li class="th-ppart"><span class="th-pn">${E.esc(st.part[0])}</span> <span lang="el">${E.esc(st.part[1])}</span></li>`; lastPart = st.part; }
      const best = (s.path || {})[st.key], open = stageOpen(all, i, s), ok = best >= PASS * 100;
      const chs = st.kind === "stage" ? st.chs.map((c) => `${c.num}. <span lang="el">${E.esc(c.el)}</span>`).join(" · ")
        : `${L.chs} ${st.chs[0].num}–${st.chs[st.chs.length - 1].num}`;
      html += `<li class="th-stg${ok ? " ok" : ""}${open ? "" : " lock"}"><span class="th-sn">${ok ? "✓" : st.n}</span><span class="th-sb">
        <b>${E.esc(stageName(L, st))}</b> ${st.span ? `<span class="chip">${E.esc(st.span)}</span>` : ""}
        <span class="ex-en">${chs}${st.earlier.length ? ` · ${L.plusEarlier}` : ""}</span>
        ${best != null ? `<span class="ex-en">${L.best}: ${best}%</span>` : ""}</span>
        ${open ? `<a class="btn small${ok ? " ghost" : ""}" href="#theoria.path~${st.n}">${best != null ? L.retry : L.start}</a>` : `<span class="th-lock" title="${E.esc(L.locked)}">🔒</span>`}</li>`;
    });
    html += `</ol>`;
    E.view.innerHTML = html;
    wireLang(() => pathPage(E));
    window.scrollTo(0, 0);
  }

  async function refs(E) {
    const L = t();
    document.title = L.refs + " · " + L.head;
    let d;
    try { d = await E.getJSON(BASE + "references.json"); } catch (e) { E.view.innerHTML = `<p class="crumbs"><a href="#theoria">← ${L.head}</a></p><p>—</p>`; return; }
    const ctx = { num: 0, p: 0, qs: [] };
    E.view.innerHTML = `<div class="th-top"><p class="crumbs"><a href="#theoria">← ${L.head}</a></p>${langBtn()}</div>
      <div class="story-head"><h2 lang="el">${E.esc(d.el)}</h2><span class="ex-en">${E.esc(d.title)}</span></div>
      <div class="th-doc th-refs">${d.intro.length ? `<section class="card">${d.intro.map((b) => block(E, b, ctx)).join("")}</section>` : ""}
      ${d.sections.map((s) => `<section class="card th-sec"><h3><span lang="el">${E.esc(s.el)}</span><span class="ex-en">${E.esc(s.title)}</span></h3>${s.body.map((b) => block(E, b, ctx)).join("")}</section>`).join("")}</div>`;
    wireLang(() => refs(E));
    window.scrollTo(0, 0);
  }

  routes.theoria = async (sub) => {
    const E = A();
    E.$("#bar-meta").textContent = t().head;
    load();
    if (!sub) return home(E);
    if (sub === "review") return session(E, "review");
    if (sub === "weak") return session(E, "weak");
    if (sub === "refs") return refs(E);
    if (sub === "path") return pathPage(E);
    if (sub.startsWith("path~")) return session(E, "path", sub.slice(5));
    if (sub.startsWith("drill~")) return session(E, "drill", sub.slice(6));
    const [id, sec] = sub.split("~");
    return chapter(E, id, sec);
  };

  // Due count for other screens (Today, Resources) that want to show it.
  window.EllinikaTheoria = { due: async () => { const B = await bank(A()), s = load(); return Object.keys(s.it).filter((id) => B[id] && isDue(s.it[id])).length; } };
})();
