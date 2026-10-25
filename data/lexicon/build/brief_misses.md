# Brief: resolve Greek words from the lessons that the word lookup cannot find

Do NOT call any mcp__hearthbot__ tools. Do not install packages. Write only the output file you are given. Do the linguistic work yourself (you are a fluent Greek lexicographer); a script may only write/validate JSON you composed.

Input: a JSON array of {w, n, capitalised, files}: a lowercase word token found in the app's lesson/reading files (n = occurrences, files = where), which the lookup could not match. Also read the known-lemma list (path given): accent-stripped lemmas and principal parts already in the lexicon. To see context, you may grep the listed files under /mnt/project-files/app/ (read-only).

For each item output one object, same order, with "w" and a "type":
- "fragment": an ending, stem or piece shown in a grammar table (ος, ούμαι, κυβερν, μενος), an abbreviation, a letter, or a typo. Nothing else needed.
- "name": a proper name or place (Αθήνα, Ελένη, Ερμού). Add "lemma" (nominative, capitalised) and "gloss" (short English, e.g. "Athens (capital of Greece)" or "Eleni (woman's name)").
- "form": an inflected form or variant spelling of a word whose lemma IS in the known list (μεγαλύτερη → μεγάλος, οκτώ → οχτώ, φουρνάρηδες → φούρναρης). Add "lemma" exactly as the dictionary headword.
- "new": a real Modern Greek word whose lemma is NOT in the known list (εκφοβισμός, λειψυδρία, ενδέχεται → ενδέχεται/ενδέχομαι as appropriate, εναπόκειται, μάθηση). Add "entry": a full entry in the format of /mnt/project-files/data/lexicon/build/brief_new.md (lemma, translit, pos, pos_raw, form_key, gloss, example, noun/verb/adjective object with model, cefr_est, themes if any; no cand_i), and "forms": every inflected form per /mnt/project-files/data/lexicon/build/brief_forms.md section 1. If several items share one new lemma, write the entry once (on the first) and mark the others "form" with that lemma. Fixed learned phrases (εν κατακλείδι, βίου in δια βίου μάθηση, ζην) may be entered as pos "other" with the whole phrase as lemma; then the item word is a "form" of it on later items.
- "other": anything else; add a short "note".

Output: JSON array (UTF-8, ensure_ascii False) at the output path; validate it parses and has one object per input item. Report in at most three lines: counts per type, and any doubts.
