# Ελληνικά

Personal Modern Greek course (static site, no build step), served by GitHub Pages from `main` at
**https://devja0717.github.io/ellinika/**. GitHub Pages is the only host.

This repo is the complete copy of the project folder:

| Repo path | What it is |
|---|---|
| `/` (index.html, *.js, *.css, lessons/, library/, img/, icons/, audio/) | the app itself |
| `data/` | lexicon, grammar, C1 and colloquial data, including build intermediates and exam papers |
| `downloads/` | companion textbook PDFs (A1–C1, parts of speech, reader) and the single-file `Ellinika.html` |
| `deploy/` | `publish_pages.py` (mirrors the project folder into this repo) and the textbook builders |
| `tools/` | dialect-recording helpers; `tools/app/` holds the app's build helpers |
| `ledger/`, `plan/`, `screens/`, `.notes/` | project ledger, B2 study plan, screenshots, notes on uploaded sources |

Republish from the project folder:

```
python3 /mnt/project-files/deploy/publish_pages.py <clone of this repo>
cd <clone> && git add -A && git commit -m "..." && git push origin main
```

`.github/workflows/pages.yml` deploys every push to `main`.
