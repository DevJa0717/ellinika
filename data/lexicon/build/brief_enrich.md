# Brief: check and enrich existing Modern Greek lexicon entries

Do NOT call any mcp__hearthbot__ tools. Do not write anything under /mnt/project-files. Do not install packages. Write only the output file you are given.

Input: a JSON array of existing lexicon entries. Read /tmp/claude-0/-home-user/6eb9e19e-d304-5a76-afab-f5a8079856a1/scratchpad/b/brief_new.md for the target entry format and field rules (ignore its candidate/skip steps).

For EVERY input entry, output the complete corrected entry (same order), so that it meets the brief_new.md format:
- Keep rank, source, freq_count, _file and lemma exactly as given (if the lemma itself is wrong, keep it and put the correct one in "lemma_fix").
- Check every Greek form, gloss, translit and the example for errors and fix them. Keep the existing example if it is correct and natural; replace it only if it is wrong, unnatural or a fragment ending in "...".
- Add what is missing: cefr_est (A1-C1) on every entry; themes where they clearly apply; noun.model for every noun (and fix gen_sg/gender/declension); adjective.model for every adjective (and add the adjective object if missing); for verbs add aorist_passive_1sg and participle where commonly used, and set conj_group to A / B1 / B2 / deponent / irregular (the old value "B" must become B1 or B2; null must become a real value). Keep any existing "note".
- needs_review: remove it when you resolved the doubt; keep it (true) only if a form is still uncertain.
- Articles, pronouns, numerals with forms: keep their existing form_key; add nothing that does not fit.

Output: write the JSON array (UTF-8, ensure_ascii False) to the output path, validate it parses and has the same number of entries as the input, and report in at most four lines: entries, how many corrected (forms/glosses/examples), how many still needs_review.
