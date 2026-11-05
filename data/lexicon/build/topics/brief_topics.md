# Brief: B2/C1 topic vocabulary list for the Greek Certificate of Attainment (Πιστοποίηση Ελληνομάθειας)

Do NOT call any mcp__hearthbot__ tools. Do not install packages. Do not run git. Write only the output file you are given. Do the linguistic work yourself (you are an experienced examiner and teacher of Modern Greek); a script may only write/validate JSON you composed.

Task: list the Modern Greek words a learner needs to read, listen to, write and speak about the given topic at B2 and C1 level, as tested in the Certificate of Attainment in Greek (Κέντρο Ελληνικής Γλώσσας) and found in Greek news, opinion pieces, public notices and everyday talk on that topic.
- Aim for about 450 lemmas: nouns, verbs, adjectives, adverbs; include the common, frequent words of the topic (an examiner would expect them) and the more precise B2/C1 words (argumentation, abstract nouns, formal verbs used in texts, e.g. επιβαρύνω, εφαρμογή, βιωσιμότητα).
- Dictionary form only: verbs present 1sg (or -μαι), nouns nominative singular (plural only if plural-only), adjectives masculine nominative singular. Correct monotonic accents. Single words only, no phrases. No proper names, no abbreviations.
- Only real, standard, attested words. Never invent compounds or derivatives. If unsure whether a word exists, leave it out.
- Tag each with the level you judge (B1, B2 or C1); skip A1–A2 basics.

Output: JSON array of {"lemma": "...", "pos": "noun|verb|adjective|adverb", "level": "B2"}. Validate it parses. Report in one line: count by level.
