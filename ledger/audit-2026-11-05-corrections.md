# Content audit corrections, 2026-11-05

Thread "Validate all content end to end". Scope: everything added since the 2026-10-25 audit (15+ bilingual readers, cookbook, drill books, writing and error workbooks, syntax guide and cards, word families and false friends, news digest, #theoria) plus a re-run over all older content. Tools: tools/audit/ (see its README). Each line: files changed, old → new (reason). Generator sources were fixed together with the built JSON so rebuilds keep the correction.

## Corrections
- `library/pos/adjective.json`, `library/pos/src/03-adjective.txt`: μερακλήδικο/μερακλήδικος → μερακλίδικο/μερακλίδικος (standard spelling, ΛΚΝ)
- `library/athlitismos/athina2004.json`: περίπου 10.500 αθλητές → περίπου 10.600 αθλητές (matches the English side and the IOC figure, 10,625)
- `library/simera/soc-crisis.json`: unsourced claim "το 2026 το υψηλότερο μηνιαίο ποσοστό … τον Μάρτιο" → "τα μηνιαία στοιχεία δείχνουν ότι αυξάνεται τον χειμώνα και στις αρχές της άνοιξης και πέφτει το καλοκαίρι" (the English side and its source say only this)
- `downloads/textbook/Ellinika-Music.pdf`, `Ellinika-Orthodox-year.pdf`, `Ellinika-Theatre-cinema.pdf`: cover page carried an English footer ("mousiki companion textbook") → rebuilt with the footer-free Greek cover; `deploy/textbook/build_bilingual.py` now always swaps in a footer-free cover and `render_pdf.js` prints only page numbers for non-level volumes
- `library/dialects/central.json`: "label": "Wikipedia: Heptanesean dialect; Peloponnesian dialect",
   "url": "https://en.wikipedia.org/wiki/Heptanesean_dialect" → "label": "Wikipedia: Modern Greek dialects (Heptanesian and Peloponnesian)",
   "url": "https://en.wikipedia.org/wiki/Modern_Greek_dialects" (cited Wikipedia page does not exist)
- `library/diaspora/chiotes.json`: “Chiot diaspora”",
   "url": "https://en.wikipedia.org/wiki/Chiot_diaspora" → “Chian diaspora”",
   "url": "https://en.wikipedia.org/wiki/Chian_diaspora" (cited page title wrong (404))
- `library/diaspora/afstralia.json`: “Greeks in Melbourne”",
   "url": "https://en.wikipedia.org/wiki/Greeks_in_Melbourne" → “Greeks of Melbourne”",
   "url": "https://en.wikipedia.org/wiki/Greeks_of_Melbourne" (cited page title wrong (404))
- `library/diaspora/vienni.json`: “Greek community of Vienna”",
   "url": "https://en.wikipedia.org/wiki/Greek_community_of_Vienna" → “Greeks in Austria”",
   "url": "https://en.wikipedia.org/wiki/Greeks_in_Austria" (cited page does not exist (404))
- `library/diaspora/vienni.json`: “Greeks in Trieste”",
   "url": "https://en.wikipedia.org/wiki/Greeks_in_Trieste" → “Greeks in Italy”",
   "url": "https://en.wikipedia.org/wiki/Greeks_in_Italy" (cited page does not exist (404))
- `library/diaspora/odessos.json`: “Greeks in Odesa”",
   "url": "https://en.wikipedia.org/wiki/Greeks_in_Odesa" → “Greeks in Ukraine”",
   "url": "https://en.wikipedia.org/wiki/Greeks_in_Ukraine" (cited page does not exist (404))
- `library/athlitismos/kerkida.json`: "Wikipedia, “Football hooliganism in Greece”",
   "url": "https://en.wikipedia.org/wiki/Football_hooliganism_in_Greece" → "Wikipedia, “Football hooliganism”",
   "url": "https://en.wikipedia.org/wiki/Football_hooliganism" (cited page does not exist (404))
- `library/athlitismos/kerkida.json`, `tools/themed-readers/athlitismos/sources.py`: source [5] "Football hooliganism in Greece" (page does not exist) → "Murder of Michalis Katsouris" (the 2023 events the paragraph cites)
- `library/exam/b2-tasks.json`: μη μπορούν → μην μπορούν (final ν before μπ)
- `library/exam/b2-tasks-3.json`: με την λίγη υπομονή → με λίγη υπομονή (no article with λίγη here)
- `library/exam/c1-tasks.json`: με τη ψηφιακή → με την ψηφιακή (final ν before ψ)
- `library/skini/angelopoulos.json`, `tools/arts/skini/part3.py`: παίζοντας τη «Γκόλφω» → την «Γκόλφω», quiz option/answer Τη Γκόλφω → Την Γκόλφω (final ν before γκ; the quoted source sentence left as printed)

## Follow-up: external links not fixed (2026-11-05)
Found by `node tools/audit/links.js --web`. Wikipedia dead links were all repointed above. These remain:
- No answer (timeouts or bot blocks, probably alive): olympics.com, uefa.com, Biblioteca Marciana, Istituto Ellenico (Venice), imthira, elsyn, espa.gr, 70.coe.int, opennieuwsbank.
- 404 (need a new URL or a replacement source): DAI Olympia page, Tsakonian archives, Landesmuseum, PECOB, National Archaeological Museum (Antikythera page), IPCC fact sheet, Dumbarton Oaks, Shaw Prize 2011, Cleveland Museum of Art 1959.82.
Run `node tools/audit/links.js --web | grep -E " 404| 410"` to list the files that cite them.

## Re-checks of new content (2026-11-05)
- Lexicon ranks 9,100–10,950 (ba9d3a6, 1,057 new lemmas): all 3,595 added lemmas checked against el_GR; the 78 it lacks are genuine loanwords, neologisms and colloquialisms (φωτό, κορονοϊός, τσουνάμι, χατ τρικ, φραπές…). Clean.
- Drill books re-extract (341890f): answers.js 0 unknown words in answer keys.
- Theoria ch. 45 and the 7 "Towards B2" cards (f7f9f5b): clean.
- links.js: a `file` with an online `url` fallback is no longer reported missing (the 35 MB C1 listening mp3 is deliberately not in the repo).
- `lessons/videos-c1.json`, `data/c1/videos/videos-c1.json`: στο Τέξας ; → στο Τέξας; (space before ; in subtitles)
- `lessons/videos-c1.json`, `data/c1/videos/videos-c1.json`: στο Κολούμπια ; → στο Κολούμπια; (space before ; in subtitles)
- `library/families/prefix-5.json`, `tools/wordfamilies/fam_b.py`: αυτός, ολος. → αυτός, όλος. (missing accent)
- `library/athlitismos/athina-1896.json`, `tools/themed-readers/athlitismos/sources.py`: https://www.olympics.com/en/olympic-games/athens-1896 → https://web.archive.org/web/20260825054755/https://www.olympics.com/en/olympic-games/athens-1896 (dead link; Wayback Machine copy)
- `library/athlitismos/athina2004.json`, `tools/themed-readers/athlitismos/sources.py`: https://www.olympics.com/en/olympic-games/athens-2004 → https://web.archive.org/web/20260508141424/https://www.olympics.com/en/olympic-games/athens-2004 (dead link; Wayback Machine copy)
- `library/simera/cul-sport.json`, `library/athlitismos/euro2004.json`, `tools/themed-readers/athlitismos/sources.py`: https://www.uefa.com/uefaeuro/history/seasons/2004/ → https://web.archive.org/web/20261022090334/https://www.uefa.com/uefaeuro/history/seasons/2004/ (dead link; Wayback Machine copy)
- `library/athlitismos/olympia.json`, `tools/themed-readers/athlitismos/sources.py`: https://www.olympics.com/ioc/ancient-olympic-games → https://web.archive.org/web/20260128224915/https://www.olympics.com/ioc/ancient-olympic-games (dead link; Wayback Machine copy)
- `library/dialects/tsakonian.json`: https://www.tsakonianarchives.gr/sintomi_grammatiki_tsakonikis_dialektou/ → https://web.archive.org/web/20240807161800/https://www.tsakonianarchives.gr/sintomi_grammatiki_tsakonikis_dialektou/ (dead link; Wayback Machine copy)
- `library/diaspora/politikoi-prosfyges.json`, `tools/diaspora/common.py`: https://pecob.net/Socialist-camp-USSR-Greek-Political-Refugees-unsettled-historical-issue → https://web.archive.org/web/20241104144201/https://www.pecob.net/Socialist-camp-USSR-Greek-Political-Refugees-unsettled-historical-issue (dead link; Wayback Machine copy)
- `library/diaspora/venetia.json`, `tools/diaspora/common.py`: https://marciana.venezia.sbn.it/ → https://web.archive.org/web/20210813052522/https://marciana.venezia.sbn.it/ (dead link; Wayback Machine copy)
- `library/diaspora/venetia.json`, `tools/diaspora/common.py`: https://www.istitutoellenico.org/ → https://web.archive.org/web/20260423080301/https://istitutoellenico.org/ (dead link; Wayback Machine copy)
- `library/mathiatriki/neoteroi.json`, `tools/themed-readers/mathiatriki/sources.py`: https://www.shawprize.org/laureates/2011-mathematical-sciences/ → https://web.archive.org/web/20250823002315/https://www.shawprize.org/laureates/2011-mathematical-sciences/ (dead link; Wayback Machine copy)
- `library/politeia/dikastiria.json`, `tools/politeia/common.py`: https://www.elsyn.gr/ → https://web.archive.org/web/20261017144257/http://www.elsyn.gr/ (dead link; Wayback Machine copy)
- `library/politeia/europi.json`, `tools/politeia/common.py`: https://www.espa.gr/ → https://web.archive.org/web/20221102142227/https://espa.gr/ (dead link; Wayback Machine copy)
- `library/reader/poem-karyotakis.json`: https://clevelandart.org/art/1959.82 → https://web.archive.org/web/20260314132329/https://www.clevelandart.org/art/1959.82 (dead link; Wayback Machine copy)
- `library/simera/cul-sport.json`: https://www.uefa.com/uefaconferenceleague/history/seasons/2024/ → https://web.archive.org/web/20260410171736/https://www.uefa.com/uefaconferenceleague/history/seasons/2024/ (dead link; Wayback Machine copy)
- `data/c1/syllabus/reading-tasks.json`, `data/c1/syllabus/sample-papers/1._c1_katanohsi_grapta.txt`: http://www.tovima.gr/health-fitness/article/?aid=436055 → https://web.archive.org/web/20130529191947/http://www.tovima.gr:80/health-fitness/article/?aid=436055 (dead link; Wayback Machine copy)
- `library/simera/hr-framework.json`: https://70.coe.int/1974-greece-re-joins-en.html → https://web.archive.org/web/20260122220822/https://70.coe.int/1974-greece-re-joins-en.html (site unreachable; Wayback Machine copy)
- `library/athlitismos/floga.json`, `tools/themed-readers/athlitismos/sources.py`: https://www.olympics.com/ioc/olympic-flame → https://en.wikipedia.org/wiki/Olympic_flame (dead link; equivalent source)
- `library/athlitismos/floga.json`, `tools/themed-readers/athlitismos/sources.py`: International Olympic Committee, “The Olympic flame and torch relay”, olympics.com → “Olympic flame” (history of the flame and the torch relay), Wikipedia (source replaced)
- `library/athlitismos/zappas.json`, `tools/themed-readers/athlitismos/sources.py`: https://www.olympics.com/ioc/history/founders-of-modern-olympic-games → https://en.wikipedia.org/wiki/Olympic_Congress (dead link; equivalent source)
- `library/athlitismos/zappas.json`, `tools/themed-readers/athlitismos/sources.py`: International Olympic Committee, “Founding of the IOC: the Sorbonne Congress, 23 June 1894”, olympics.com → “Olympic Congress” (the founding Sorbonne Congress, 23 June 1894), Wikipedia (source replaced)
- `library/athlitismos/telos.json`, `tools/themed-readers/athlitismos/sources.py`: https://www.dainst.org/en/projects/olympia → https://www.dainst.org/en/ (project page removed; institute site)
- `library/diaspora/apoikies.json`, `tools/diaspora/images.json`: http://katalog.landesmuseum.de/object/464B5B04C4D14A0C8E507149BC7C132C → https://www.landesmuseum.de/ (old catalogue offline; museum site)
- `library/digest/2026-10-26.json`, `deploy/news/src/2026-10-26/c.py`: https://www.infrastructure.gov.au/department/media/news/western-sydney-airport-set-open → https://en.wikipedia.org/wiki/Western_Sydney_International_Airport (dead link; equivalent source)
- `library/epistimi/antikythira.json`, `tools/themed-readers/epistimi/sources.py`: https://www.namuseum.gr/en/collection/antikythera/ → https://www.namuseum.gr/en/collection/ (page moved; museum collection)
- `library/epistimi/klima.json`, `tools/themed-readers/epistimi/sources.py`: https://www.ipcc.ch/report/ar6/wg1/downloads/factsheets/IPCC_AR6_WGI_Regional_Fact_Sheet_Mediterranean.pdf → https://web.archive.org/web/20240106014001/https://www.ipcc.ch/report/ar6/wg1/resources/factsheets/ (PDF removed; archived fact-sheet index that links it)
- `library/mathiatriki/vyzantini-iatriki.json`, `library/istoria/e7-science.json`, `tools/themed-readers/mathiatriki/sources.py`, `deploy/istoria/src/e7.py`: https://www.doaks.org/resources/publications/books/byzantine-monastic-foundation-documents → https://en.wikipedia.org/wiki/Pantokrator_Monastery (dead link; book citation kept, link to the monastery)
- `library/nisia/amorgos-mikra.json`, `tools/nisia/common.py`: https://www.imthira.gr/ → https://en.wikipedia.org/wiki/Amorgos (site unreachable; equivalent source)

## External links replaced (2026-11-05, second pass; supersedes the "not fixed" list above)
All 24 dead or unreachable outside sources were replaced (`git show` this commit for the full list): 16 now point to Wayback Machine copies (olympics.com ×3, uefa.com ×2, Tsakonian archives, PECOB, Marciana, Istituto Ellenico, Shaw Prize 2011, elsyn, espa, Cleveland Museum 1959.82, 70.coe.int, To Vima 2013, IPCC AR6 fact-sheet index); 8 had no snapshot and point to equivalent sources (Olympic flame → Wikipedia "Olympic flame"; IOC founders → Wikipedia "Olympic Congress"; DAI Olympia → dainst.org/en; Landesmuseum catalogue → landesmuseum.de; Western Sydney airport → Wikipedia; NAM Antikythera → namuseum.gr/en/collection; Dumbarton Oaks BMFD → Wikipedia "Pantokrator Monastery", book citation kept; imthira.gr → Wikipedia "Amorgos"). Generator sources updated too. `links.js --web` now verifies Wayback links through the archive.org availability API (web.archive.org itself is blocked from the sandbox) and reports 0 dead of 3,830.
- `library/theoria` (src/39-connecting.txt, connecting.json, drills.json): drill "Ήρθε ___ έφυγε" offered both και and κι, and και is also correct; the distractor is now είτε.
- `library/theoria` (learned-syntax src, json, drills.json): "Απεργία ___ όρων" (άνευ όρων does not collocate with απεργία) → "Παράδοση ___ όρων" (unconditional surrender).

## Re-check of the 11:00–14:00 UTC landings (2026-11-05)
- New readers #kathimerini (Everyday life, 14 ch) and #ygeia (Health, 10 ch): audit.js 0 hard findings (flags were interjections, ordinals, enclitic accents); facts.py clean; sample paragraphs read, natural and correct (helpline 1018 and ΕΚΑΒ 166 verified). Four dead citations fixed: ATH.ENA Card → Wikipedia "Public transport in Athens", EU VAT e-commerce → Your Europe "VAT rules for e-commerce", "Ferry transport in Greece" → "Transport in Greece" (these three now match tools/themata/kathimerini/sources.py, the JSON was older than the generator), el "Οριζόντια ιδιοκτησία" → el "Πολυκατοικία".
- Theoria mixed-practice sections (e96fb7b, 26fdc7b): audit.js and answers.js clean (flags are deliberate spelling drills, ό,τι, surnames, elisions).
- Drill books (761414d): answers.js 0 unknown words.
- links.js: 0 internal problems in 1,047 files.

## Final re-check, 2026-11-05 ~19:20 UTC
New since 84b0465: readers #douleia (9 ch), #scheseis (8), #nomos (6), #eleftheros (5), #eidiseis (7), 9 added chapters in #kathimerini/#ygeia, theoria learned prefixes/suffixes, drill-book irregular tables, lexicon to 14,261 entries. audit.js: 0 hard findings (flags are enclitic accents such as κίνδυνός τους, φιλότιμό σου, τηλεφωνήματός μας, which are correct, plus καρέτα καρέτα, ordinals, glosses). facts.py: 47 chapters, 0 real mismatches. answers.js: only names, ό,τι, ordinals and deliberate drills. links.js: 0 internal problems in 1,096 files; --web 0 dead of 4,126 (the one timeout, dovaluegreece.gr, answers 200 on retry). pdfs.js: all 37 PDFs have Greek-only covers and are listed. No fixes needed.
