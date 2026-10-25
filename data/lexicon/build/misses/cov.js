const fs=require("fs"),path=require("path");
const A="/mnt/project-files/app/", D="/mnt/project-files/data/";
const L=require(A+"lookup.js");
const lex=[],seen=new Set();
for(const f of fs.readdirSync(D+"lexicon").filter(f=>/^core-.*\.json$/.test(f)).sort()) for(const e of JSON.parse(fs.readFileSync(D+"lexicon/"+f))) if(!seen.has(e.lemma)){seen.add(e.lemma);lex.push(e);}
const CL=D+"colloquial/colloquial-lexicon.json"; if(fs.existsSync(CL)) for(const e of JSON.parse(fs.readFileSync(CL))) if(!seen.has(e.lemma)){seen.add(e.lemma);lex.push(e);}
const irr=JSON.parse(fs.readFileSync(D+"grammar/verbs-holton.json"))["irregular_verbs_6.25"].verbs;
const extra={...JSON.parse(fs.readFileSync(A+"lessons/lookup-gloss.json")),...JSON.parse(fs.readFileSync(A+"lessons/lookup-extra.json"))};
const opt=(p)=>fs.existsSync(p)?JSON.parse(fs.readFileSync(p)):{};
// same sources as the app (app.js lookupIndex / tools/check_lookup.js)
const idx=L.build(lex,{...opt(D+"lexicon/names.json"),...opt(D+"colloquial/colloquial-lookup.json"),...extra},irr,opt(D+"lexicon/forms-index.json").forms||{});
const FI=JSON.parse(fs.readFileSync(D+"lexicon/forms-index.json")).forms; const fi=new Map();
for(const [k,v] of Object.entries(FI)) fi.set(L.strip(k),v);
const files=[]; const rd=(d)=>{for(const f of fs.readdirSync(d,{withFileTypes:true})){const p=path.join(d,f.name); if(f.isDirectory())rd(p); else if(p.endsWith(".json")&&!/lookup-|course\.json|index\.json|manifest/.test(p)) files.push(p);}};
rd(A+"lessons"); if(fs.existsSync(A+"library")) rd(A+"library");
const tok=(s)=>String(s).match(/[Ͱ-Ͽἀ-῿]+/g)||[];
const res={}; let n=0,miss=0,guess=0,fiHit=0;
for(const f of files){ let j; try{j=JSON.parse(fs.readFileSync(f));}catch{continue}
  const ctx={}; const texts=[];
  const walk=(o,k)=>{ if(typeof o==="string"){ if(k!=="en"&&k!=="gloss_en") texts.push(o);} else if(Array.isArray(o)) o.forEach(x=>walk(x,k)); else if(o&&typeof o==="object") for(const [kk,v] of Object.entries(o)){ if(kk==="gloss"&&v&&typeof v==="object"&&!Array.isArray(v)){Object.assign(ctx,v);continue;} walk(v,kk);} };
  walk(j);
  for(const t of texts) for(const w of tok(t)){ if(w.length<2) continue; n++;
    const h=L.lookup(idx,w,ctx); const how=!h?"miss":h[0].how==="guess"?"guess":"hit";
    if(how==="hit") continue; const k=L.strip(w); const inFI=fi.has(k);
    if(how==="miss")miss++; else guess++; if(inFI) fiHit++;
    const r=res[w.toLowerCase()]||(res[w.toLowerCase()]={n:0,how,fi:inFI?fi.get(k):null,files:new Set(),cap:0});
    r.n++; r.files.add(path.relative(A,f)); if(w[0]!==w[0].toLowerCase()) r.cap++;
  }}
const out=Object.entries(res).map(([w,r])=>({w,n:r.n,how:r.how,fi:r.fi,cap:r.cap,files:[...r.files].slice(0,4)})).sort((a,b)=>b.n-a.n);
fs.writeFileSync("misses.json",JSON.stringify(out,null,0));
console.log({tokens:n,miss,guess,files:files.length,distinct:out.length,coveredByFormsIndex:out.filter(x=>x.fi).length, tokensCoveredByFI:fiHit});
console.log(out.filter(x=>!x.fi&&x.cap<x.n).slice(0,60).map(x=>x.w+":"+x.n+":"+x.how).join(" "));
