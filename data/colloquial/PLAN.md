# Colloquial Greek units: plan (thread "Colloquial Greek units", 2026-10-18)

Status (2026-10-18 14:40): all 13 lessons written and validated; see ledger.

## Format notes (checked against app.js and theme-work.json)
- Lesson file: `{el, title, vocab:[lemmas], blocks:[...], practice:[...]}` in app/lessons/.
- Blocks: text{title,text}, table{title,head,rows (md **bold**)}, examples{title,items:[{el,en}]}, callout{text}, culture{title,text}, reading{title,text,en,gloss:{form:"lemma — gloss"},questions:[{prompt,answer,options}]}, rules{title,items}.
- Practice: `type` {items:[{prompt,answer,accept,why}]}, `mc` {items:[{prompt,answer,options,why}]}. vocab-recall runs automatically on `vocab` lemmas, which must exist in lexicon().
- Lexicon entry shape = data/lexicon/core-3000.json (rank, lemma, translit, pos, gloss, example{el,en}, noun/verb/adjective sub-objects, cefr_est). Add colloquial fields: `register` (colloquial|slang|vulgar|offensive), `strength` (0-5), `region`.
- Lookup: app.js lexicon() reads lexicon/core-1000, core-3000, core-4000 only. The app thread must add `colloquial/colloquial-lexicon.json` there (or the lookup index) for slang lookup and vocab-recall to work. Multi-word lemmas are not indexed by lookup.js (whitespace forms skipped); surface forms can also go in a `colloquial-lookup.json` in lookup-extra format `{"form":"lemma|gloss"}`.

## Units (unit "Colloquial Greek", files app/lessons/slang-*.json)
1. slang-discourse: ρε, μωρέ, βρε, έλα, άντε, άσε, καλά, πω πω, μπα, ωχ, τέλος πάντων
2. slang-everyday: people, money, going out, mood (φάση, πλάκα, κολλητός, τύπος, φράγκα, τζάμπα, την κάνω, μου τη σπάει)
3. slang-idioms: colloquial set phrases (τα έκανα θάλασσα, τρώω πόρτα, ψήνομαι, μου ήρθε κεραμίδα)
4. slang-morphology: diminutives/augmentatives, θεο-/κατα-/ψιλο-/παλιο-/κωλο-, -άρω loans
5. slang-youth: youth, internet, texting, Greeklish, abbreviations
6. slang-swearing: γαμώ family, μαλάκας scale, σκατά, κώλος, αρχίδια, blasphemy, euphemisms, strength scale
7. slang-insults: insults by type, κατάρες, μούντζα, how to respond or defuse
8. slang-nightlife: drinking, partying, romance, sex, drugs (adult, frank)
9. slang-athens-thessaloniki: north/south (σε λέω, σουβλάκι/καλαμάκι, παχύ λ)
10. slang-crete: Cretan (τσαι, ίντα, γιάντα, κοπέλι, θωρώ, γροικώ)
11. slang-cyprus: Cypriot (τζαι, εν, ίνταλως, δαμαί, ποτζεί, augment kept)
12. slang-regions: Pontic, Ionian, Peloponnese/Mani, Epirus, rebetiko μάγκικα
13. slang-dialogues: capstone scenes, register switching formal <-> colloquial
Each lesson: register + strength notes, typical responses, example dialogues, pronunciation notes, culture note, a reading, type+mc practice. Sources go in data/colloquial/SOURCES.md, not in lessons.
