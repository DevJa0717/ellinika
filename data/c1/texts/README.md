# C1 Modern Greek reading corpus (texts/)

Collected 2026-10-18 for Devon's personal, non-commercial Greek study app (C1 level, intellectual adult learner).

**49 texts, ~26,000 words in total.**

| kind | count | what |
|---|---|---|
| wiki | 17 | Greek Wikipedia (CC BY-SA 4.0) via the MediaWiki API: lead + 1-3 sections, 517-890 words. Philosophy, politics/society, science/tech, Greek history and culture, the language question. |
| literature | 12 | Public-domain literature from Greek Wikisource: Cavafy (5 poems), Papadiamantis (2 excerpts), Vizyinos, Solomos (*Διάλογος*), Karyotakis (*Πρέβεζα*), Psycharis (2 excerpts from *Το ταξίδι μου*). |
| official | 7 | Greek Constitution (3 texts: arts 1-5; 16 + 120; 24), EU Charter of Fundamental Rights in Greek (2 texts, EUR-Lex), a European Parliament press release (8 Oct 2026), a Ministry of Education press release (18 Oct 2026). |
| opinion | 10 | Recent (Oct 2026) opinion/analysis pieces from tovima.gr, ertnews.gr, lifo.gr and efsyn.gr. Each is a single excerpt of 400 words or fewer, with attribution and link. |
| speech | 3 | Kolokotronis on the Pnyx (1838); G. Papandreou, *Ο λόγος της απελευθερώσεως* (18 Oct 1944); Aris Velouchiotis, *Λόγος στη Λαμία* (29 Oct 1944). The last two are a deliberate pair contrasting katharevousa and demotic. |

## Files

- `<id>.json`: one text each. Fields: `id, kind, title, author, date, url, license, register, topic, words, text, notes`, plus `retrieved` (2026-10-18) and `orthography` (`monotonic` or `polytonic (as in source)`). Polytonic texts also carry **`text_monotonic`**, a machine conversion that may contain small accent errors. Paragraphs in `text` are separated by `\n\n`. In poems, lines are separated by `\n` and stanzas by `\n\n`. Section headings from Wikipedia and article headings from legal texts are kept as short standalone paragraphs.
- `index.json`: `{count, texts:[{id, kind, title, topic, words, register, author, orthography, has_monotonic_version, file}]}`.
- `sources.json`: `{items:[{id,title,author,url,license,retrieved,file,notes}], skipped:[...]}`. `skipped` lists the sources I tried and left out, with the reason.

ID prefixes: `w` = wiki, `l` = literature, `o` = official, `j` = journalism/opinion, `s` = speech.

## Things to know

- **Length:** the 250-900 word target applies to prose. Some texts are shorter by nature: the Cavafy and Karyotakis poems (81-245 words) are complete poems, and the two efsyn pieces (j09, j10, about 160 words) are short op-eds cut back so they stay excerpts and never the full article. The Solomos *Διάλογος* (436 words) is all of the Wikisource transcription, which is incomplete.
- **Orthography:** Greek is NFC. Latin look-alike letters inside Greek words (common in the Wikisource Constitution, e.g. Latin K/O/H) were mapped to Greek. Polytonic is kept where the source is genuinely polytonic: Cavafy's *Η πόλις*, *Απολείπειν*, *Θερμοπύλες*; *Η Φόνισσα*; Vizyinos; Solomos; the Psycharis preface; Papandreou. In those files `text_monotonic` is the monotonic version. *Όνειρο στο κύμα* came from Wikisource half polytonic and half monotonic, so it was converted entirely to monotonic (noted in the file). Cavafy's and Psycharis' own spellings (σκέψις, Εβρώπη, αφτό, είταν) are left untouched.
- **Register labels:** `katharevousa-mixed` covers Papadiamantis, Vizyinos, Kolokotronis and Papandreou. Velouchiotis' plain spoken oratory is labelled `neutral`.
- **Copyright:**
  - Wikipedia texts are CC BY-SA 4.0. Credit "Greek Wikipedia contributors" and link the article; the revision id is in `date`.
  - Literature and Kolokotronis/Velouchiotis are public domain (authors died before 1956).
  - The Constitution, the ministry release and the EU texts are official texts, reusable with acknowledgement of the source.
  - **Opinion pieces are copyrighted:** short excerpts for personal study only, not to be redistributed.
  - **Papandreou (died 1968) is not yet public domain by term:** personal use only.
- **Skipped:**
  - Kathimerini: every candidate was behind the paywall.
  - presidency.gr, primeminister.gr and the Parliament site: blocked by bot protection, so the President's and PM's speeches could not be fetched.
  - European Parliament verbatim reports: blocked by bot protection.
  - Nobel lectures by Seferis and Elytis: no Greek text online, and still in copyright.
  - A volunteer Greek translation of Obama's 2016 Athens speech: too many grammar errors to use as a model.
- Every file's `notes` field flags learned forms, idioms and difficulty points to use for glossing.

## Contents

| id | kind | title | author | words | register | orth. |
|---|---|---|---|---|---|---|
| w01 | wiki | Σωκράτης | Wikipedia contributors | 740 | neutral | monotonic |
| w02 | wiki | Στωικισμός | Wikipedia contributors | 517 | neutral | monotonic |
| w03 | wiki | Διαφωτισμός | Wikipedia contributors | 761 | neutral | monotonic |
| w04 | wiki | Δημοκρατία | Wikipedia contributors | 673 | neutral | monotonic |
| w05 | wiki | Μεταπολίτευση | Wikipedia contributors | 655 | neutral | monotonic |
| w06 | wiki | Ευρωπαϊκή Ένωση | Wikipedia contributors | 705 | neutral | monotonic |
| w07 | wiki | Ελληνική οικονομική κρίση χρέους (2009-2018) | Wikipedia contributors | 890 | neutral | monotonic |
| w08 | wiki | Κλιματική αλλαγή | Wikipedia contributors | 554 | neutral | monotonic |
| w09 | wiki | Τεχνητή νοημοσύνη | Wikipedia contributors | 753 | neutral | monotonic |
| w10 | wiki | Εξέλιξη | Wikipedia contributors | 787 | neutral | monotonic |
| w11 | wiki | Γλωσσικό ζήτημα | Wikipedia contributors | 872 | neutral | monotonic |
| w12 | wiki | Καθαρεύουσα | Wikipedia contributors | 659 | neutral | monotonic |
| w13 | wiki | Δημοτική γλώσσα | Wikipedia contributors | 715 | neutral | monotonic |
| w14 | wiki | Ρεμπέτικο τραγούδι | Wikipedia contributors | 734 | neutral | monotonic |
| w15 | wiki | Ελληνική Επανάσταση του 1821 | Wikipedia contributors | 687 | neutral | monotonic |
| w16 | wiki | Μικρασιατική Καταστροφή | Wikipedia contributors | 716 | neutral | monotonic |
| w17 | wiki | Νέα ελληνική γλώσσα | Wikipedia contributors | 667 | neutral | monotonic |
| l01 | literature | Ιθάκη | Κωνσταντίνος Π. Καβάφης | 237 | literary | monotonic |
| l02 | literature | Περιμένοντας τους βαρβάρους | Κωνσταντίνος Π. Καβάφης | 245 | literary | monotonic |
| l03 | literature | Η πόλις | Κωνσταντίνος Π. Καβάφης | 141 | literary | polytonic |
| l04 | literature | Απολείπειν ο θεός Αντώνιον | Κωνσταντίνος Π. Καβάφης | 121 | literary | polytonic |
| l05 | literature | Θερμοπύλες | Κωνσταντίνος Π. Καβάφης | 81 | literary | polytonic |
| l06 | literature | Όνειρο στο κύμα (αρχή) | Αλέξανδρος Παπαδιαμάντης | 672 | katharevousa-mixed | monotonic |
| l07 | literature | Η Φόνισσα, Κεφάλαιο Α΄ (αρχή) | Αλέξανδρος Παπαδιαμάντης | 627 | katharevousa-mixed | polytonic |
| l08 | literature | Το μόνον της ζωής του ταξείδιον (αρχή) | Γεώργιος Βιζυηνός | 616 | katharevousa-mixed | polytonic |
| l09 | literature | Διάλογος (οριστικό κείμενο) | Διονύσιος Σολωμός | 436 | literary | polytonic |
| l10 | literature | Πρέβεζα | Κώστας Καρυωτάκης | 125 | literary | monotonic |
| l11 | literature | Το ταξίδι μου — Θ΄. Cabinet de lecture (απόσπασμα) | Γιάννης Ψυχάρης | 441 | literary | monotonic |
| l12 | literature | Το ταξίδι μου — Πρόλογος της δεύτερης έκδοσης (απόσπασμα) | Γιάννης Ψυχάρης | 467 | literary | polytonic |
| o01 | official | Σύνταγμα της Ελλάδας — Άρθρα 1–5 (Βασικές διατάξεις, ισότητα, ελευθερία) | Ελληνική Πολιτεία | 748 | formal | monotonic |
| o02 | official | Σύνταγμα της Ελλάδας — Άρθρα 16 και 120 (Παιδεία· τελική διάταξη) | Ελληνική Πολιτεία | 604 | formal | monotonic |
| o03 | official | Σύνταγμα της Ελλάδας — Άρθρο 24 (Προστασία του περιβάλλοντος, χωροταξία) | Ελληνική Πολιτεία | 417 | formal | monotonic |
| o04 | official | Χάρτης των Θεμελιωδών Δικαιωμάτων της ΕΕ — Προοίμιο και Τίτλος Ι (Αξιοπρέπεια) | Ευρωπαϊκό Κοινοβούλιο, Συμβούλιο, Επιτροπή | 547 | formal | monotonic |
| o05 | official | Χάρτης των Θεμελιωδών Δικαιωμάτων της ΕΕ — Επιλεγμένα άρθρα (Ελευθερίες, Ισότητα) | Ευρωπαϊκό Κοινοβούλιο, Συμβούλιο, Επιτροπή | 541 | formal | monotonic |
| o06 | official | Οι προτεραιότητες του ΕΚ για την πρώτη στρατηγική κατά της διαφθοράς | Ευρωπαϊκό Κοινοβούλιο — Γραφείο Τύπου | 662 | formal | monotonic |
| o07 | official | Σοφία Ζαχαράκη από το Δουβλίνο: Η ελληνική εκπαιδευτική ατζέντα στον ευρωπαϊκό διάλογο, με το βλέμμα στην Προεδρία του 2027 | Υπουργείο Παιδείας, Θρησκευμάτων και Αθλητισμού — Γραφείο Τύπου | 694 | formal | monotonic |
| j01 | opinion | Ο μεταφραστής που δεν μιλάει δύο γλώσσες | Κωστής Κατσανέβας | 378 | journalistic | monotonic |
| j02 | opinion | Τεχνητή νοημοσύνη, υπεραξία της εργασίας και το μέλλον της | Ιωάννης Παπαγιάννης | 391 | journalistic | monotonic |
| j03 | opinion | Ο φόβος ως ψυχολογικός ρυθμιστής ηττημένων προσδοκιών | Γιώργος Πανταγιάς | 395 | journalistic | monotonic |
| j04 | opinion | AI agents: Όταν οι ιστότοποι τούς κλείνουν την πόρτα | Βάλια Καϊμάκη | 380 | journalistic | monotonic |
| j05 | opinion | Η σοβαρή πλευρά της Αναγεννητικής Ιατρικής και των επιστημονικών μεθόδων Μακροβιότητας | Πολυδεύκης Παπαδόπουλος | 361 | journalistic | monotonic |
| j06 | opinion | Γκομενάκια και κολοκυθάκια με συνταγή από ΑΙ | Ερωφίλη Κόκκαλη | 398 | journalistic | monotonic |
| j07 | opinion | Η μαγκιά της Σάλι Ρούνεϊ | Δημήτρης Πολιτάκης | 351 | journalistic | monotonic |
| j08 | opinion | Σπουδές φύλου στο «Γεώργιος Καραϊσκάκης» | Δημήτρης Πολιτάκης | 342 | journalistic | monotonic |
| j09 | opinion | Ο Καρτερός, ο Φουκώ «οι λέξεις και τα πράγματα» | Βάσω Μουρελά | 164 | journalistic | monotonic |
| j10 | opinion | Τα κέρδη τους ή οι ανάγκες των παιδιών μας; | Κυριάκος Ιωαννίδης | 160 | journalistic | monotonic |
| s01 | speech | Ομιλία του Θεόδωρου Κολοκοτρώνη στην Πνύκα (απόσπασμα) | Θεόδωρος Κολοκοτρώνης | 736 | katharevousa-mixed | monotonic |
| s02 | speech | Ο λόγος της απελευθερώσεως (απόσπασμα) | Γεώργιος Παπανδρέου | 660 | katharevousa-mixed | polytonic |
| s03 | speech | Λόγος στη Λαμία (απόσπασμα) | Άρης Βελουχιώτης | 777 | neutral | monotonic |
