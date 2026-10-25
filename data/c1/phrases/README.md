# C1 phrase datasets (Modern Greek)

Personal, non-commercial study material for C1-level Greek: idioms, learned/katharevousa survivals, formal collocations, and discourse connectors. Retrieved/compiled 2026-10-18.

## Files

| File | Items | Content |
|---|---|---|
| `idioms.json` | 406 | Everyday and literary idioms, proverbs and similes, roughly ranked by usefulness (`rank` 1 = most frequent in conversation/press). Fields: `rank, el, literal_en, meaning_en, register (colloquial/neutral/formal), example_el, example_en, source_url`. Register mix: mostly colloquial/neutral, ~40 formal (mythological/learned idioms such as δαμόκλειος σπάθη, κρούω τον κώδωνα του κινδύνου). |
| `learned-phrases.json` | 335 | Katharevousa and ancient survivals in current use. `type`: fixed-dative 76 (εν τω μεταξύ, τοις μετρητοίς, εν ευθέτω χρόνω, αγαθή τη πίστει…), preposition-phrase 129 (εκ των υστέρων, επί τάπητος, προ των πυλών, εις βάρος, υπό την αιγίδα…), saying 50 (μηδέν άγαν, γνώθι σαυτόν, η αρχή άνδρα δείκνυσι, NT quotations…), formula 30 (ειρήσθω εν παρόδω, θέτω υπό αμφισβήτηση, λαμβάνω χώρα…), other 50 (τρόπον τινά, πόσω μάλλον, κεκλεισμένων των θυρών…). Fields add `origin_note`. |
| `collocations.json` | 359 | Formal/academic collocations: verb+noun 266 (λαμβάνω μέτρα, ασκώ κριτική, καταβάλλω προσπάθεια, εγείρω ερωτήματα, χρήζω διερεύνησης…), adj+noun 83 (ευρεία απήχηση, οξεία κριτική, επιτακτική ανάγκη, ακανθώδες ζήτημα…), other 10. Each has `colloquial_equiv`, the everyday way to say it. |
| `connectors.json` | 175 | Discourse connectors and stance/hedging expressions, by `function` (hedging 24, emphasis 18, sequencing 18, contrast 14, concession 14, result 14, addition 13, reformulation 13, summary 13, condition 12, cause 12, exemplification 10), with `register` and a `grammar_note` (mood, case, position). Polysemous items such as ενώ appear once per function. Has a `source_url` too. |
| `sources.json` | | Sources with licence notes. |

## Method and caveats
- Candidate phrases were taken from el.wiktionary categories (Εκφράσεις (νέα ελληνικά) with 1,595 pages, Πολυλεκτικοί όροι with 2,466, Εκφράσεις (καθαρεύουσα), Επιρρηματικές εκφράσεις, Παροιμίες), plus the curator's knowledge of current press and spoken usage. Obsolete, dialectal, very vulgar or purely nautical items were left out. A few mildly vulgar but very common ones are kept and marked colloquial, for example τα σκατώνω and μου την έσπασε.
- The MediaWiki API returned HTTP 429 (shared IP), so the category listings were scraped from the normal HTML category pages instead (politely, about 1.5 s between requests).
- `source_url` = the el.wiktionary entry when one exists (403 items in all). Otherwise it is a lemma search in the Τριανταφυλλίδης *Λεξικό της κοινής νεοελληνικής* (greek-language.gr) for the phrase's key word. That dictionary lists set phrases under ΦΡ inside the headword entry and marks register (λόγ., προφ., μτφ.). For ancient-only forms (for example σαυτόν) that search can come back empty. Some Triantafyllidis entries were spot-checked and agree with this data: χυλόπιτα, σφοντύλι, μαντάρα, τάπητας (λόγ.), ευήκοος.
- Collocations are mostly not separate dictionary entries, so their `source_url` points to the noun's dictionary entry.
- All examples, translations, register labels and colloquial equivalents are original. No example sentences were copied. Wiktionary content is CC BY-SA 4.0. Triantafyllidis is © ΚΕΓ and is only linked.
- Spelling: everything is monotonic and NFC-normalised. The only polytonic text is a few ancient forms quoted in `origin_note`. Learned phrases are given in their usual modern monotonic spelling, e.g. τοις μετρητοίς, εν πάση περιπτώσει.
- Register is the curator's judgment for typical use. Ancient sayings are labelled formal even when they are used jokingly in conversation.
