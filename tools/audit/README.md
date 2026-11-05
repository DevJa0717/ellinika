# Content audit tools

Run these before pushing new content. No installs needed (Node 22, curl). The el_GR word list downloads to /tmp on first run.

| Command | What it checks |
|---|---|
| `node tools/audit/audit.js <files or dirs>` | Greek text in any JSON: spelling (LibreOffice el_GR + the project word lists), accents, final ς/σ, final ν, mixed Latin/Greek letters, Latin `?` in Greek (use `;`), doubled function words, space before punctuation, unbalanced «», and words the tap lookup cannot resolve. Ends with a list of "typo candidates" (unknown words one letter away from a real word). Exit 1 on HARD findings. |
| `node tools/audit/links.js [--web] [paths]` | `#routes` in content resolve, image/file paths exist, quiz answers are among the options with no duplicate options, offline-files.json and the sw.js SHELL list exist, every library JSON is cached offline. `--web` also fetches every external URL (404/410/no answer = dead; 403/429 = unverifiable). |
| `node tools/audit/pdfs.js` | Every PDF in downloads/textbook: Greek-only cover (no Latin letters on page 1), page count, listed on downloads/textbook/index.html. |
| `node tools/audit/answers.js [paths]` | Every word in every drill answer key (answer/accept/correct/solution) is a real form in el_GR or the project word lists. A wrong form in a key teaches the error. |
| `python3 tools/audit/facts.py <files>` | Bilingual readers: every paragraph cites a source, every cited number exists, years/numbers in the Greek and English halves of a paragraph agree, quiz answers present. |

Options for audit.js: `--json out.json` (full findings), `--md out.md` (summary), `--quiet` (counts only), `--no-lookup` (faster).

Deliberate exceptions: dialect, ancient/Katharevousa, error-spotting and distractor material is not spell-checked (paths and keys are in `SKIP_SPELL` / `ERROR_KEYS` in audit.js). Add verified words the dictionary lacks to `tools/audit/allow.txt`.

Typical use for a new shelf: `node tools/audit/audit.js library/<shelf> && node tools/audit/links.js library/<shelf> && python3 tools/audit/facts.py library/<shelf>/*.json`.

Results of the 2026-11-05 full run and every correction made: `ledger/audit-2026-11-05-corrections.md`. Words the lookup cannot resolve, ranked by frequency (input for the vocabulary thread): `ledger/lookup-misses-2026-11-05.tsv`.
