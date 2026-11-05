# Brief: classify frequent Greek corpus words that neither our lexicon nor Wiktionary could lemmatize

Do NOT call any mcp__hearthbot__ tools. Do not write anything under /mnt/project-files. Do not install packages. Do not run git. Write only the output file you are given. Do the linguistic work yourself (you are a fluent Greek lexicographer); a script may only write/validate JSON you composed.

Input: a JSON array of `{w, per_million}`: a lowercase, sometimes accentless word form from the wordfreq Greek list (news, Wikipedia, subtitles, web), in frequency order. Many are names (people, places, clubs, parties), abbreviations written without dots (κλπ, χλμ, εσπα, μκο), accentless spellings of known words (ελλαδα, θεσσαλονικη), old spellings (καμμία), loanwords (ρόστερ, σκόρερ, ασίστ, κομισιόν), and some real words that deserve an entry (προκήρυξη, μετέπειτα, συλλαλητήριο, εγχείρημα, ενσωμάτωση).
Known-lemma file (path given): JSON object {lemma: short gloss} of the words already in the lexicon. A second file (path given) lists the lemmas being added in this same extension; treat them as known too.

For each item output one object, same order, with "w" and a "type":
- "fragment": an ending, syllable, interjection noise (εεε, μμμ), typo, or a cut-off word. Nothing else.
- "abbr": an abbreviation or acronym. Add "lemma" in its usual written form (κλπ. / χλμ. / ΕΣΠΑ / ΜΚΟ) and "gloss": the expansion in Greek then English, e.g. "και λοιπά — etc., and so on" or "Εταιρικό Σύμφωνο για το Πλαίσιο Ανάπτυξης — NSRF (EU development funding programme)".
- "name": a proper name (person, place, club, party, company, programme). Add "lemma" (nominative, capitalised, accented) and "gloss" (short English: "Piraeus (port city of Athens)", "Mitsotakis (Greek surname; Kyriakos Mitsotakis, prime minister from 2019)", "Panathinaikos (Athens sports club)"). For an ethnic adjective/noun that is a common word (Γερμανός, ευρωπαϊκός), use "new" or "form" instead.
- "form": an inflected form, accentless spelling or old spelling of a word in the known lists or of a word you enter as "new" earlier in your batch. Add "lemma" exactly as that headword.
- "new": a real Modern Greek word (including established loanwords: ρόστερ, σκόρερ, ασίστ, φινάλε, στάνταρ) whose lemma is not known. Add "entry" in the format of brief_10k.md in the same folder (lemma, translit, pos, pos_raw, form_key, gloss, example, noun/verb/adjective object with model, cefr_est, themes if any; omit "i" and "forms" inside entry) and, next to it, "forms": every inflected written form (nouns all cases sg+pl; adjectives all genders/cases/numbers; verbs the full active and, if used, passive sets; indeclinables [lemma]). If several items share one new lemma, enter it on the first and mark the others "form".

Output: JSON array (UTF-8, ensure_ascii False) at the output path; validate it parses and has one object per input item, in order. Report in at most three lines: counts per type, and doubts.
