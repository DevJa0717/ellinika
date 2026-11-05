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
