# News digest (#digest): how a new issue is made

The app shelf **Ειδήσεις σε τρία επίπεδα** (Resources → News digest, route `#digest`) shows one issue of current-affairs
stories per day, each story rewritten at **B1, B2 and C1** with its own glossary and questions, plus a grammar note,
words to keep and links to the reports it is based on. Viewer: `news-digest.js` (repo root). Data: `library/digest/`.

A scheduled task starts a fresh session every morning at about 06:30 UTC and follows the runbook below.
The repo (github.com/DevJa0717/ellinika, branch `main`) is the source of truth for `library/digest/` and `deploy/news/`;
`deploy/publish_pages.py` never overwrites or deletes them.

## Runbook for one issue

1. `git pull --rebase origin main`. Let `D` be today's UTC date (YYYY-MM-DD). If `library/digest/D.json` already exists, stop.
2. **Gather 10–15 stories** from the last 48 hours: about 4 Greece, 3–4 Europe, 2–3 world, 1 economy, 1 science/environment,
   1 culture or sport. Good starting points: Wikipedia "Portal:Current events" (the month page, read with an offset near
   the end), en.wikipedia.org/wiki/2026_in_Greece (change the year), ekathimerini.com, tovima.com, greekcitytimes.com,
   greekreporter.com, euronews.com, france24.com, aljazeera.com, rferl.org, dw.com, bta.bg, CBS/CNN. Reuters, AP and the
   Guardian refuse automated fetches: confirm their stories through another outlet. Avoid grisly crime and disaster
   items, celebrity gossip and anything only one outlet reports. Treat politics neutrally.
3. **Check every fact** (numbers, names, dates, quotes) against at least one opened source; drop what you cannot open.
   Quote only short phrases, translated, and attribute them. Never copy article text: write each level from scratch.
4. **Write the issue** in `deploy/news/src/D/` as Python modules `a.py`, `b.py`, … (each defines `STORIES = [...]`,
   helpers in `deploy/news/src/helpers.py`; copy the shape of `deploy/news/src/2026-10-26/`), or as one
   `deploy/news/src/D.json` with `{"stories": [...]}`. Per story and level:
   - **B1**: 3–4 short paragraphs (60–110 Greek words), present/past simple, everyday words, 8–10 glossary entries, 3 questions.
   - **B2**: 3–4 paragraphs (110–180 words), news register, passive and participles, 10 glossary entries, 3 questions.
   - **C1**: 3–4 paragraphs (160–260 words), press register with context and analysis, 10–13 glossary entries, 3 questions.
   - Every paragraph has an English translation (`en`). Questions are in Greek, the right option first (the app shuffles),
     `why` in English. One `grammar` note per story drawn from its text, and 8 `vocab` lemmas.
   - Sections: `ellada`, `europi`, `kosmos`, `oikonomia`, `epistimi`, `politismos`, `athlitismos`.
   - Standard Modern Greek, monotonic accents, final -ν rules (την/στην/μην before vowels and κ π τ ξ ψ γκ μπ ντ τσ τζ).
5. **Build and check** from the repo root:
   `LANG=C.UTF-8 python3 deploy/news/build_issue.py D --check`
   It writes `library/digest/D.json`, puts the issue at the top of `library/digest/index.json` (the archive keeps every
   issue) and keeps the newest 7 issues on `offline-files.json`. The checker reports schema problems, quiz answers,
   final-ν, accents, spelling against el_GR, and tap-lookup MISS/GUESS. For every MISS, and every GUESS that lands on the
   wrong lemma, add a line to `deploy/news/gloss.txt` (`form<TAB>lemma — English`) and build again until it says
   **0 problems, 0 lookup misses**. Fix spelling flags that are real.
6. Optional screen check: `python3 -m http.server 8765` and open `#digest` at an iPhone-sized viewport.
7. **Commit only** `library/digest/`, `deploy/news/` and `offline-files.json`:
   `git add library/digest deploy/news offline-files.json && git commit -m "News digest: issue D (N stories)"`,
   then `git pull --rebase origin main && git push origin main` (retry with backoff on network errors). GitHub Pages
   deploys on push; the issue is live at https://devja0717.github.io/ellinika/#digest within a few minutes.
8. If `/mnt/project-files/ledger/LEDGER.md` exists, do not log daily issues there; only log a problem that needs a person.

## Data format

`library/digest/index.json`: `{kind:"digest", el, title, intro_el, intro_en, issues:[{id, file, date, el, count, lead, lead_en}]}`, newest first.

`library/digest/D.json`:
```
{ id, date, date_el, sections:[{id, el, en}],
  stories:[{ id, section, el, title,                  // el/title = the B2 headline
             levels:{ B1|B2|C1: { el, title, paras:[{el, en}], glossary:[{el, en}], questions:[{q, options, answer, why}] } },
             grammar:{level, title, en (markdown), examples:[{el, en}]},
             vocab:[lemma], sources:[{name, url, date}] }],
  gloss:{form: "lemma — English"} }                  // tap-lookup fallbacks for this issue
```
Progress is saved per story and level in `progress.library["digest/D/<story>/<level>"]`; the level choice is
`localStorage["ellinika.digest.level"]` (per profile).
