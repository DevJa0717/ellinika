/* Ελληνικά learning tools. No server, accounts, API keys, or third-party dependencies. */
(function () {
  "use strict";
  const routes = (window.EllinikaAddons = window.EllinikaAddons || {});
  const E = () => window.Ellinika;
  const esc = (value) => E().esc(value == null ? "" : value);
  const $ = (s) => document.querySelector(s);
  const now = () => new Date().toISOString();
  const count = (s) => (String(s).match(/[\p{L}\p{N}]+/gu) || []).length;
  const sample = (array) => array.slice().sort(() => Math.random() - 0.5);
  const diagnostic = [
    { level: "A1", skill: "Greetings", q: "Which expression means ‘good morning’?", options: ["Καλημέρα", "Καληνύχτα", "Αντίο", "Ευχαριστώ"], answer: 0, why: "Καλημέρα is a greeting used in the morning." },
    { level: "A1", skill: "Articles", q: "Complete: ___ σπίτι είναι μεγάλο.", options: ["Ο", "Η", "Το", "Τον"], answer: 2, why: "Σπίτι is a neuter noun: το σπίτι." },
    { level: "A1", skill: "Present tense", q: "Complete: Εγώ ___ φοιτητής.", options: ["είναι", "είμαστε", "είμαι", "είσαι"], answer: 2, why: "The first-person singular of είμαι is είμαι." },
    { level: "A1", skill: "Plural nouns", q: "What is the nominative plural of το παιδί?", options: ["οι παιδί", "τα παιδιά", "τα παιδί", "των παιδιών"], answer: 1, why: "το παιδί → τα παιδιά." },
    { level: "A1", skill: "Questions", q: "Which question asks ‘Where are you from?’", options: ["Πόσο χρονών είσαι;", "Τι ώρα είναι;", "Από πού είσαι;", "Πώς σε λένε;"], answer: 2, why: "Από πού είσαι; asks about origin." },
    { level: "A2", skill: "Simple past", q: "Complete: Χθες ___ στο σχολείο.", options: ["πηγαίνω", "πήγα", "θα πάω", "πηγαίνεις"], answer: 1, why: "Χθες calls for a past event: πήγα." },
    { level: "A2", skill: "Genitive", q: "Complete: Αυτά είναι τα βιβλία ___ παιδιών.", options: ["των", "τα", "τους", "οι"], answer: 0, why: "The genitive plural article is των." },
    { level: "A2", skill: "Future", q: "Complete: Αύριο ___ διαβάσω το βιβλίο.", options: ["θα", "να", "μη", "που"], answer: 0, why: "θα + dependent verb form expresses the future." },
    { level: "A2", skill: "Pronouns", q: "Choose ‘I see her’.", options: ["Τη βλέπω.", "Της βλέπω.", "Το βλέπω.", "Τον βλέπω."], answer: 0, why: "The feminine accusative weak pronoun is τη(ν); the final ν drops before β." },
    { level: "A2", skill: "Imperfect", q: "Complete: Όταν ήμουν μικρός, ___ κάθε μέρα στο πάρκο.", options: ["θα πάω", "πήγα", "πήγαινα", "πηγαίνω"], answer: 2, why: "Πήγαινα describes a repeated past activity." },
    { level: "B1", skill: "Subjunctive", q: "Complete: Θέλω ___ μάθω ελληνικά.", options: ["θα", "να", "όταν", "πως"], answer: 1, why: "Θέλω να μάθω expresses a desire followed by να." },
    { level: "B1", skill: "Conditionals", q: "Complete: Αν βρέξει, ___ στο σπίτι.", options: ["έμεινα", "μένουμε χθες", "θα μείνουμε", "μέναμε"], answer: 2, why: "Αν βρέξει, θα μείνουμε is a real future conditional." },
    { level: "B1", skill: "Passive", q: "Complete: Το γράμμα ___ χθες.", options: ["γράφεται αύριο", "γράψαμε", "γράφει", "γράφτηκε"], answer: 3, why: "Γράφτηκε is a past passive form agreeing with το γράμμα." },
    { level: "B1", skill: "Relative clauses", q: "Complete: Ο φίλος ___ μένει δίπλα μου είναι γιατρός.", options: ["που", "πού", "πώς", "ότι"], answer: 0, why: "The relative particle is unaccented που." },
    { level: "B1", skill: "Purpose", q: "Complete: Διαβάζω περισσότερο ___ περάσω την εξέταση.", options: ["επειδή", "για να", "ενώ", "μόλις"], answer: 1, why: "Για να introduces a purpose." },
    { level: "B2", skill: "Unreal conditional", q: "Complete: Αν το ήξερα, ___ νωρίτερα.", options: ["έρχομαι", "θα έρθω", "θα ερχόμουν", "ήρθα αύριο"], answer: 2, why: "An unreal present/general conditional can use αν + imperfect and θα + imperfect." },
    { level: "B2", skill: "Concession", q: "Complete: Παρόλο ___ έβρεχε, βγήκαμε.", options: ["που", "να", "αν", "για"], answer: 0, why: "Παρόλο που introduces a concessive clause." },
    { level: "B2", skill: "Relative pronouns", q: "Complete: Το βιβλίο ___ μου μίλησες είναι εδώ.", options: ["ο οποίος", "για το οποίο", "της οποίας", "στον οποίο"], answer: 1, why: "Μιλάω για something; βιβλίο is neuter: για το οποίο." },
    { level: "B2", skill: "Past counterfactual", q: "Complete: Αν είχα προλάβει, θα ___ το τρένο.", options: ["πάρω", "είχα πάρει", "παίρνω", "πάρω χθες"], answer: 1, why: "A past counterfactual pairs αν + pluperfect with θα + pluperfect." },
    { level: "B2", skill: "Nominal style", q: "Which phrase most naturally means ‘due to the rain’?", options: ["λόγω της βροχής", "λόγω την βροχή", "λόγω στη βροχή", "λόγω βρέχει"], answer: 0, why: "The preposition λόγω takes the genitive: της βροχής." },
    { level: "C1", skill: "Argument connectors", q: "Complete: ___ εκ τούτου, η πρόταση απορρίφθηκε.", options: ["Έως", "Ως", "Από", "Δίχως"], answer: 1, why: "Ως εκ τούτου means ‘consequently’." },
    { level: "C1", skill: "Formal register", q: "Which is the most formal equivalent of ‘βγάζω απόφαση’?", options: ["παίρνω μια απόφαση", "σκέφτομαι μια απόφαση", "εκδίδω απόφαση", "βγάζω έξω την απόφαση"], answer: 2, why: "Εκδίδω απόφαση is a conventional formal collocation." },
    { level: "C1", skill: "Concession", q: "Complete: ___ και αν προσπαθήσει, δεν θα τα καταφέρει.", options: ["Όσο", "Όποτε", "Όπου", "Επειδή"], answer: 0, why: "Όσο και αν / όσο κι αν means ‘however much’." },
    { level: "C1", skill: "Learned expressions", q: "Complete: Η τροπολογία τέθηκε ___ ισχύ.", options: ["από", "σε", "με", "για"], answer: 1, why: "The conventional phrase is τίθεται σε ισχύ." },
    { level: "C1", skill: "Nuanced stance", q: "What does ‘Δεν αποκλείεται να εγκριθεί’ mean?", options: ["It has definitely been approved", "It is impossible to approve", "It may be approved", "It must not be approved"], answer: 2, why: "Δεν αποκλείεται να expresses possibility, not certainty." }
  ];

  routes.diagnostic = function () {
    const app = E(), holder = app.view, groups = ["A1", "A2", "B1", "B2", "C1"];
    app.$("#bar-meta").textContent = "Diagnostic";
    document.title = "Placement diagnostic · Ελληνικά";
    let i = 0, answers = [];
    const previous = app.progress.library?.diagnostic;
    function screen() {
      if (i >= diagnostic.length) return finish();
      const q = diagnostic[i];
      holder.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Placement diagnostic</h2><p class="sub">Informal, non-certified baseline. 25 independent questions across A1–C1; not a speaking or writing assessment.</p>
      <div class="pmeta"><span>${i + 1} / ${diagnostic.length} · ${q.level}</span><span>${esc(q.skill)}</span></div>
      <div class="progress"><i style="width:${Math.round(100*i/diagnostic.length)}%"></i></div>
      <section class="card"><h3>${esc(q.q)}</h3><div class="options" id="dg-answers">${q.options.map((a,j)=>`<button class="opt" data-i="${j}">${esc(a)}</button>`).join("")}</div><p class="sub" id="dg-explain" hidden></p><button class="btn" id="dg-next" hidden>Next</button></section>`;
      holder.querySelectorAll("#dg-answers button").forEach(btn => btn.onclick = () => {
        if (answers[i] != null) return;
        const chosen = Number(btn.dataset.i); answers[i] = chosen;
        holder.querySelectorAll("#dg-answers button").forEach((b,j) => { b.disabled = true; b.classList.toggle("right",j === q.answer); if (j===chosen && j!==q.answer) b.classList.add("wrong"); });
        const ex = $("#dg-explain"); ex.hidden = false; ex.textContent = q.why;
        $("#dg-next").hidden = false;
      });
      $("#dg-next").onclick = () => { i++; screen(); };
    }
    function finish() {
      const byLevel = groups.map(level => {
        const ix = diagnostic.map((q,j)=>q.level===level?j:-1).filter(j=>j>=0);
        const right = ix.filter(j=>answers[j]===diagnostic[j].answer).length;
        return { level, right, total: ix.length, fraction: right/ix.length };
      });
      let startingPoint = "A1";
      for (const item of byLevel) { if (item.fraction >= 0.8) startingPoint = item.level; else break; }
      const result = { at:now(), score:byLevel.reduce((s,x)=>s+x.right,0), total:diagnostic.length, byLevel, suggested_start:startingPoint };
      app.progress.library = app.progress.library || {};
      app.progress.library.diagnostic = result; app.saveProgress();
      holder.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Diagnostic results</h2><p class="sub">${result.score} / ${result.total} correct. Suggested course starting point: <strong>${startingPoint}</strong> (provisional).</p>
      <section class="card"><h3>Per-level accuracy</h3><ul class="ex-list">${byLevel.map(x=>`<li>${x.level}: ${x.right}/${x.total} · ${Math.round(x.fraction*100)}%</li>`).join("")}</ul><p class="sub">Only five questions per level. This cannot certify a CEFR level; speaking, writing and authentic listening remain unassessed. A low score may reflect unfamiliar vocabulary or the test format rather than overall ability.</p></section>
      <div class="actions"><button class="btn" id="dg-repeat">Retake</button><a class="btn ghost" href="#library">Resources</a></div>`;
      $("#dg-repeat").onclick = () => { i=0; answers=[]; screen(); };
    }
    if (previous) {
      holder.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Placement diagnostic</h2><section class="card"><p>Previous assessment: ${new Date(previous.at).toLocaleDateString()} · ${previous.score}/${previous.total} correct</p><p class="sub">This self-check does not certify a CEFR level.</p><button class="btn" id="dg-go">Take assessment</button></section>`;
      $("#dg-go").onclick = screen;
    } else screen();
  };

  const speech = (text) => {
    if (!window.speechSynthesis || !window.SpeechSynthesisUtterance) return false;
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text); u.lang = "el-GR"; u.rate = 0.93;
    window.speechSynthesis.speak(u); return true;
  };
  const audioUrl = (url) => {
    if (typeof url !== "string" || !url || url.startsWith("/") || url.includes("..") || /:\/\//.test(url) || url.startsWith("data:")) return null;
    if (!/^audio\/[\w/-]+\.(mp3|m4a|ogg|wav)$/i.test(url)) return null;
    return url;
  };
  routes.speakinglab = async function () {
    const app = E(), view = app.view;
    app.$("#bar-meta").textContent = "Speaking studio";
    document.title = "Speaking studio · Ελληνικά";
    let data, manifest;
    try { [data, manifest] = await Promise.all([app.getJSON("library/writing/workshop.json"),app.getJSON("audio/manifest.json").catch(()=>({speaking:{}}))]); }
    catch (e) { view.innerHTML = `<p>Speaking tasks could not load. ${esc(e.message)}</p>`; return; }
    const tasks = data.speaking || [];
    let stream = null, recorder = null, audioBlobUrl = null;
    let recordedChunks = [];
    const cleanup = () => { if (recorder && recorder.state !== "inactive") recorder.stop(); stream?.getTracks().forEach(t=>t.stop()); stream=null; if (audioBlobUrl) URL.revokeObjectURL(audioBlobUrl); audioBlobUrl=null; };
    const selected = decodeURIComponent((location.hash.split(".")[1] || ""));
    const task = tasks.find(t=>t.id===selected);
    if (!task) {
      view.innerHTML = `<p class="crumbs"><a href="#library">← Resources</a></p><h2>Speaking studio</h2><p class="sub">Record your response locally, replay it, and compare it to a model when available. No audio is uploaded or automatically saved.</p>
        <ul class="lessons">${tasks.map((t,k)=>`<li><a class="lesson-row" href="#speakinglab.${encodeURIComponent(t.id)}"><span class="lr-num">${k+1}</span><span class="lr-main"><span class="lr-title" lang="el">${esc((t.prompt_el||"").split("\n")[0])}</span><span class="lr-en">${esc(t.level)} · oral exam part ${esc(t.part)}</span></span></a></li>`).join("")}</ul>`;
      return;
    }
    view.innerHTML = `<p class="crumbs"><a href="#speakinglab">← Speaking studio</a></p><h2>Speaking studio · ${esc(task.level)}</h2><section class="card"><div class="ws-prompt" lang="el">${app.paras(task.prompt_el)}</div>
      <div class="sheet-bar"><button class="btn small ghost" id="sl-listen">▶ Hear prompt</button><span id="sl-source" class="sub"></span></div>
      <div id="sl-asset"></div></section><section class="card"><h3>Your response</h3><p class="sub">Microphone permission is requested only when you press Record. Recording remains on this device unless you export it.</p>
      <div class="sheet-bar"><button class="btn" id="sl-start">Record</button><button class="btn ghost" id="sl-stop" disabled>Stop</button><span id="sl-status" role="status"></span></div><div id="sl-play"></div></section>
      ${(task.phrases||[]).length?`<details class="card"><summary>Useful phrases</summary><ul class="ex-list">${task.phrases.map(p=>`<li><span lang="el">${esc(p.el)}</span><span class="ex-en">${esc(p.en)}</span></li>`).join("")}</ul></details>`:""}
      ${task.model_el?`<details class="card"><summary>Model answer</summary><div lang="el">${app.paras(task.model_el)}</div></details>`:""}<section class="card"><h3>Reflect</h3><p>Were your case endings, verb aspect, and word order correct? Did you speak in complete sentences and link ideas naturally?</p><textarea id="sl-notes" rows="4" placeholder="Notes about what to practise next…"></textarea><button class="btn small" id="sl-notes-save">Save notes</button></section>`;
    const key="speaking-notes/"+task.id; const existing = app.progress.library?.[key];
    $("#sl-notes").value=existing?.text||"";
    $("#sl-notes-save").onclick=()=>{app.progress.library=app.progress.library||{};app.progress.library[key]={text:$("#sl-notes").value,at:now()};app.saveProgress();$("#sl-notes-save").textContent="Saved";};
    const asset=audioUrl(manifest.speaking?.[task.id]);
    if(asset){ $("#sl-asset").innerHTML=`<audio id="sl-recorded-prompt" controls preload="none" src="${esc(asset)}"></audio>`;$("#sl-source").textContent="Recorded audio available"; }
    else $("#sl-source").textContent="Device-generated voice (fallback)";
    $("#sl-listen").onclick=()=>{if(asset){$("#sl-recorded-prompt").play().catch(()=>{$("#sl-source").textContent="Playback blocked. Tap the audio player below.";});}else if(!speech(task.prompt_el)) $("#sl-source").textContent="No Greek voice is available on this device.";};
    const begin=$("#sl-start"), stop=$("#sl-stop"), status=$("#sl-status");
    if(!navigator.mediaDevices?.getUserMedia || typeof window.MediaRecorder === "undefined") {begin.disabled=true; status.textContent="Microphone recording is not supported in this browser.";return;}
    begin.onclick=async()=>{
      try {if(audioBlobUrl){URL.revokeObjectURL(audioBlobUrl);audioBlobUrl=null;}stream=await navigator.mediaDevices.getUserMedia({audio:true});
        recordedChunks=[];const types=["audio/webm;codecs=opus","audio/mp4","audio/webm","audio/ogg"];const mime=types.find(t=>MediaRecorder.isTypeSupported(t));
        recorder=new MediaRecorder(stream,mime?{mimeType:mime}:undefined);
        recorder.ondataavailable=e=>{if(e.data?.size)recordedChunks.push(e.data);};
        recorder.onstop=()=>{stream?.getTracks().forEach(t=>t.stop());stream=null;
          if(!view.contains(begin)) return;
          begin.disabled=false;stop.disabled=true;
          if(!recordedChunks.length){status.textContent="No recording was captured.";return;}
          const type=recorder.mimeType||recordedChunks[0].type||"audio/webm",blob=new Blob(recordedChunks,{type});audioBlobUrl=URL.createObjectURL(blob);
          const ext=type.includes("mp4")?"m4a":type.includes("ogg")?"ogg":"webm";const name=`ellinika-${task.id}.${ext}`;
          $("#sl-play").innerHTML=`<p><audio controls id="sl-response" src="${esc(audioBlobUrl)}"></audio></p><p><a class="btn small ghost" id="sl-download" download="${esc(name)}" href="${esc(audioBlobUrl)}">Export my recording</a></p>`;
          status.textContent="Recorded locally. Listen to yourself and compare with the model.";
        };
        recorder.start();begin.disabled=true;stop.disabled=false;status.textContent="Recording…";
      } catch(err){stream?.getTracks().forEach(t=>t.stop());stream=null;status.textContent="Microphone permission denied or unavailable: "+(err.message||err);}
    };
    stop.onclick=()=>{if(recorder?.state==="recording")recorder.stop();};
    // Stop using the microphone if the user navigates away.
    const observer=new MutationObserver(()=>{if(!view.contains(begin)){cleanup();observer.disconnect();}});
    observer.observe(view,{childList:true});
  };

  const connectorRe = /(?<![\p{L}])(ωστόσο|επιπλέον|επομένως|συνεπώς|παράλληλα|αρχικά|τελικά|συμπερασματικά|δηλαδή|επίσης|αφενός|αφετέρου|καταρχάς|για παράδειγμα|από την άλλη πλευρά)(?![\p{L}])/giu;
  routes.writingcoach = async function () {
    const app=E();app.$("#bar-meta").textContent="Writing coach";document.title="Writing coach · Ελληνικά";
    let data;try{data=await app.getJSON("library/writing/workshop.json");}catch(e){app.view.textContent="Writing tasks could not load.";return;}
    const tasks=data.writing||[],selected=decodeURIComponent(location.hash.split(".")[1]||"");
    const task=tasks.find(t=>t.id===selected);
    if(!task){app.view.innerHTML=`<p class="crumbs"><a href="#library">← Resources</a></p><h2>Writing coach</h2><p class="sub">Offline structural checks, revision prompts and a saved draft. This is not automated grammatical correction.</p><ul class="lessons">${tasks.map((t,k)=>`<li><a class="lesson-row" href="#writingcoach.${encodeURIComponent(t.id)}"><span class="lr-num">${k+1}</span><span class="lr-main"><span class="lr-title" lang="el">${esc((t.prompt_el||"").split("\n")[0])}</span><span class="lr-en">${esc(t.level)} · ${esc(t.genre||"writing")}</span></span></a></li>`).join("")}</ul>`;return;}
    const key=task.id, lib=app.progress.library||(app.progress.library={}),drafts=lib.drafts||(lib.drafts={});
    app.view.innerHTML=`<p class="crumbs"><a href="#writingcoach">← Writing coach</a></p><h2>Writing coach · ${esc(task.level)}</h2><section class="card"><div lang="el">${app.paras(task.prompt_el)}</div>${task.prompt_en?`<details><summary>English instructions</summary><p>${esc(task.prompt_en)}</p></details>`:""}</section><section class="card"><textarea id="wc-text" lang="el" rows="16" spellcheck="true" autocomplete="off" placeholder="Γράψτε εδώ…"></textarea><div class="sheet-bar"><span id="wc-count" class="sub"></span><button class="btn" id="wc-check">Review structure</button><button class="btn ghost" id="wc-export">Export draft (.txt)</button></div><div id="wc-feedback" aria-live="polite"></div></section>
      ${(task.phrases||[]).length?`<details class="card"><summary>Suggested expressions</summary><ul class="ex-list">${task.phrases.map(p=>`<li lang="el">${esc(p.el)}</li>`).join("")}</ul></details>`:""}
      ${task.model_el?`<details class="card"><summary>Model answer (open after revising)</summary><div lang="el">${app.paras(task.model_el)}</div></details>`:""}<p class="sub">The structural checks do not inspect noun case, verb agreement, or idiomatic correctness. Use the regular writing workshop for an AI-reviewed draft where that service is available.</p>`;
    const ta=$("#wc-text"), counter=$("#wc-count");ta.value=drafts[key]||"";let timer;
    const sync=()=>{counter.textContent=`${count(ta.value)} words${task.words?` / target ${task.words}`:""}`;clearTimeout(timer);timer=setTimeout(()=>{drafts[key]=ta.value;app.saveProgress();},450);};
    ta.oninput=sync;sync();
    $("#wc-check").onclick=()=>{
      const txt=ta.value.trim(),n=count(txt),paragraphs=txt.split(/\n\s*\n/).filter(x=>x.trim()),connectors=[...txt.matchAll(connectorRe)].map(x=>x[0]);
      const targets=[];
      if(n<20)targets.push("Write at least a short paragraph before reviewing.");
      if(task.words && n<task.words*0.85)targets.push(`Text is below the suggested length of ${task.words} words.`);
      if(task.words && n>task.words*1.15)targets.push(`Text exceeds the suggested length of ${task.words} words.`);
      if(n>=80 && paragraphs.length<2)targets.push("Consider separating the introduction, development and conclusion into paragraphs.");
      if(n>=100 && connectors.length<2)targets.push("Consider linking your main ideas explicitly (e.g. ωστόσο, επιπλέον, επομένως). Use each connector only where its meaning fits.");
      const out=[];out.push(`<li>Length: <strong>${n}</strong> words</li>`);out.push(`<li>Paragraphs: <strong>${paragraphs.length}</strong></li>`);out.push(`<li>Discourse connectors detected: <strong>${connectors.length}</strong></li>`);
      $("#wc-feedback").innerHTML=`<section class="card"><h3>Structural review</h3><ul>${out.join("")}</ul>${targets.length?`<h4>Consider revising</h4><ul>${targets.map(s=>`<li>${esc(s)}</li>`).join("")}</ul>`:"<p>No obvious structural flags were triggered. This does not mean the Greek is grammatically correct.</p>"}<p><strong>Self-check:</strong> Are noun cases and adjective endings correct? Does each verb have the intended aspect? Are register and task requirements appropriate?</p></section>`;
    };
    $("#wc-export").onclick=()=>{const blob=new Blob([ta.value],{type:"text/plain;charset=utf-8"}),url=URL.createObjectURL(blob),a=document.createElement("a");a.href=url;a.download="ellinika-writing-"+key+".txt";a.click();setTimeout(()=>URL.revokeObjectURL(url),4000);};
  };
})();
