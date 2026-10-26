# Era 2 · Μινωίτες και Μυκηναίοι (περ. 2000–1100 π.Χ.)
from common import P, S, G, T, Q, SRC

ERA = dict(id="bronze-age", el="Μινωίτες και Μυκηναίοι", en="Minoans and Mycenaeans", dates="περ. 2000–1100 π.Χ.", dates_en="c. 2000–1100 BC", level="B1+",
  intro_el="Στη Μέση και στην Ύστερη Εποχή του Χαλκού εμφανίζονται στο Αιγαίο τα πρώτα ανάκτορα, η πρώτη γραφή και, για πρώτη φορά, γραπτά ελληνικά. Πρώτα στην Κρήτη των Μινωιτών και ύστερα στις Μυκήνες, την Πύλο και την Τίρυνθα, γεννιέται ένας κόσμος που οι μεταγενέστεροι Έλληνες θα θυμούνται ως την εποχή των ηρώων.",
  intro_en="In the Middle and Late Bronze Age the Aegean sees its first palaces, its first writing and, for the first time, written Greek. First in Minoan Crete and then at Mycenae, Pylos and Tiryns, a world arises that later Greeks remembered, through Homer, as the age of heroes. The chapters cover the scripts of Crete and their decipherment, the frescoes of Thera, the Mycenaean palace states, Bronze Age engineering and Minoan religion. The Greek stays around B1+, with more subordinate clauses; the grammar notes add the perfect, the gerund and result clauses.")

CH = []

# 2.1 language
CH.append(dict(id="e2-linear-b", theme="language", el="Γραμμική Α και Γραμμική Β: τα πρώτα γραπτά ελληνικά", title="Linear A and Linear B: the first written Greek", dates="περ. 1800–1200 π.Χ.",
  image="linear-b",
  summary_en="Crete's undeciphered Linear A, the Mycenaean Linear B, and how an architect, Michael Ventris, showed in 1952 that Linear B was Greek, pushing written Greek back some five hundred years.",
  sections=[
    S("scripts", "Οι γραφές της Κρήτης", "The scripts of Crete", [
      P("Η πρώτη γραφή του Αιγαίου εμφανίστηκε στην Κρήτη. Οι Μινωίτες χρησιμοποίησαν πρώτα ένα σύστημα με εικονογραφικά σημεία, τα λεγόμενα «κρητικά ιερογλυφικά», και αργότερα μια απλούστερη γραφή, τη Γραμμική Α. Τη Γραμμική Α τη διαβάζουμε περίπου, γιατί πολλά σημεία της μοιάζουν με σημεία της Γραμμικής Β. Δεν την καταλαβαίνουμε όμως, γιατί η γλώσσα που αποδίδει δεν είναι ελληνική και δεν μοιάζει με καμία γνωστή γλώσσα.",
        "The first writing in the Aegean appeared in Crete. The Minoans first used a system of pictorial signs, so-called 'Cretan hieroglyphic', and later, from around 1800 BC, a simpler script, Linear A, found on clay tablets, stone offering tables and vessels across Crete and the islands. We can roughly 'read' Linear A, in the sense of pronouncing it, because many of its signs resemble Linear B signs whose values we know. But we do not understand it, because the language it records is not Greek and does not resemble any known language; with only a few thousand signs surviving, mostly lists and short religious formulas, there is too little text to crack it. The Phaistos Disc, a stamped clay disc of about 1700 BC, uses yet another script and remains a mystery.", [1, 2]),
      P("Η Γραμμική Β είναι μια προσαρμογή της Γραμμικής Α για τα ελληνικά. Τη χρησιμοποίησαν οι Μυκηναίοι από τον 15ο ως τον 13ο αιώνα π.Χ., στην Κνωσό και στα ανάκτορα της ηπειρωτικής Ελλάδας: στην Πύλο, στις Μυκήνες, στη Θήβα, στην Τίρυνθα. Έχει περίπου 90 συλλαβογράμματα, δηλαδή σημεία που αποδίδουν μια συλλαβή, και πολλά ιδεογράμματα, μικρές εικόνες για πράγματα όπως άλογα, άρματα, κρασί και λάδι.",
        "Linear B is an adaptation of Linear A for Greek. The Mycenaeans used it from the fifteenth to the thirteenth century BC, at Knossos and in the palaces of the mainland: Pylos, Mycenae, Thebes, Tiryns, and also at Chania in western Crete. It has about 90 syllabic signs (syllabograms), each standing for a syllable such as da, pu or ri, and many ideograms (logograms), small pictures for things like horses, chariots, wine and oil, plus a decimal number system. Because a syllabic script fits Greek badly, spellings are approximate: final consonants are left out and clusters split, so the word for 'tripod', τρίπους, is written ti-ri-po.", [1, 3]),
    ]),
    S("ventris", "Ο αρχιτέκτονας που διάβασε τη Γραμμική Β", "The architect who read Linear B", [
      P("Τις πρώτες πινακίδες της Γραμμικής Β τις βρήκε στην Κνωσό ο Βρετανός Άρθουρ Έβανς, το 1900. Το 1939 ο Αμερικανός Καρλ Μπλέγκεν βρήκε στην Πύλο ένα ολόκληρο αρχείο. Για πολλά χρόνια κανείς δεν μπορούσε να τις διαβάσει. Ο ίδιος ο Έβανς ήταν βέβαιος ότι η γλώσσα τους δεν ήταν ελληνική. Η λύση ήρθε από έναν Άγγλο αρχιτέκτονα, τον Μάικλ Βέντρις, που είχε ενθουσιαστεί με τις μινωικές γραφές από δεκατεσσάρων χρονών.",
        "The first Linear B tablets were found at Knossos by the Briton Arthur Evans in 1900. In 1939 the American Carl Blegen found a whole archive at Pylos, on the very first day of digging the 'Palace of Nestor'. For decades no one could read them, and Evans himself was certain that their language was not Greek. The American classicist Alice Kober (1906–1950) laid crucial groundwork by showing that the language was inflected: groups of signs changed their endings in regular patterns ('Kober's triplets'). The solution came from an English architect, Michael Ventris (1922–1956), who had been fascinated by the Minoan scripts since he heard Evans lecture when he was fourteen.", [3, 4]),
      P("Ο Βέντρις οργάνωσε τα σημεία σε έναν πίνακα, σύμφωνα με το ποια σημεία μοιράζονταν πιθανώς το ίδιο σύμφωνο ή το ίδιο φωνήεν. Όταν δοκίμασε να διαβάσει μερικά ονόματα τόπων της Κρήτης, όπως ko-no-so (Κνωσός) και a-mi-ni-so (Αμνισός), κατάλαβε ότι η γλώσσα ήταν μια πολύ αρχαία μορφή της ελληνικής. Ανακοίνωσε την ανακάλυψή του στο ραδιόφωνο του BBC την 1η Ιουλίου 1952. Το 1953, μαζί με τον γλωσσολόγο Τζον Τσάντγουικ, δημοσίευσε την απόδειξη.",
        "Ventris arranged the signs in a grid, according to which signs probably shared the same consonant or the same vowel, without assuming any language. When he tried reading some Cretan place names into the grid, such as ko-no-so (Knossos) and a-mi-ni-so (Amnisos, the harbour of Knossos), he realised, to his own surprise, that the language was a very archaic form of Greek. He announced the discovery on BBC radio on 1 July 1952. In 1953, with the Cambridge philologist John Chadwick, he published the proof in the article 'Evidence for Greek dialect in the Mycenaean archives'. That same year a tablet from Pylos, found by Blegen just before, showed pictures of tripods and jars next to words that, read with Ventris's values, said exactly 'tripod' and 'jar with four handles', a striking confirmation. Ventris was killed in a car accident in 1956, aged 34.", [3, 4, 5]),
    ]),
    S("words", "Τι μας λένε οι πινακίδες", "What the tablets tell us", [
      P("Οι πινακίδες δεν είναι λογοτεχνία. Είναι λογαριασμοί και κατάλογοι: πόσα πρόβατα έχει ένας βοσκός, πόσο λάδι πήγε σε έναν θεό, πόσοι εργάτες πήραν μερίδες σιτάρι. Είναι όμως πολύτιμες, γιατί είναι τα πρώτα ελληνικά που έχουν γραφτεί ποτέ, περίπου πεντακόσια χρόνια πριν από τον Όμηρο. Σε αυτές εμφανίζονται λέξεις που αναγνωρίζουμε αμέσως: e-ra-wo (έλαιον, δηλαδή λάδι), wa-na-ka (άναξ, ο βασιλιάς), pa-te (πατέρας).",
        "The tablets are not literature. They are accounts and inventories: how many sheep a shepherd has, how much oil went to a god, how many workers received rations of wheat. They were written on unbaked clay and meant to be thrown away; they survive only because the fires that destroyed the palaces baked them hard. Yet they are precious, because they are the earliest Greek ever written, some five hundred years before Homer. In them appear words we recognise at once: e-ra-wo (elaion, 'olive oil'; modern λάδι comes from a related form), wa-na-ka (wanax, later ἄναξ, 'king, lord'), pa-te (patēr, 'father'), and qa-si-re-u, the ancestor of βασιλεύς, which then meant only a local chief.", [3, 6]),
      P("Εμφανίζονται επίσης θεοί που ξέρουμε από την κλασική εποχή: ο Δίας (di-wo), η Ήρα (e-ra), ο Ποσειδώνας (po-se-da-o), ακόμα και ο Διόνυσος (di-wo-nu-so), που παλαιότερα οι ερευνητές θεωρούσαν «νέο» θεό. Η αποκρυπτογράφηση της Γραμμικής Β έδειξε λοιπόν ότι η ελληνική γλώσσα και μέρος της ελληνικής θρησκείας υπήρχαν ήδη στην Εποχή του Χαλκού. Η Γραμμική Α, αντίθετα, δεν έχει αποκρυπτογραφηθεί μέχρι σήμερα.",
        "Gods familiar from the classical age also appear: Zeus (di-wo, in the genitive), Hera (e-ra), Poseidon (po-se-da-o), who at Pylos seems to have been the chief god, and even Dionysus (di-wo-nu-so, on tablets from Pylos and Chania), whom scholars used to consider a 'new' god imported late from Thrace or Phrygia. The decipherment of Linear B therefore showed that the Greek language and part of Greek religion already existed in the Bronze Age, and that the Mycenaeans of the epics were Greek speakers. Linear A, by contrast, has still not been deciphered, and the language of the Minoans remains unknown.", [3, 6]),
    ]),
  ],
  grammar=[
    G("B1", "The perfect: έχω + aorist form", "Παρακείμενος (ενεργητικός και παθητικός)",
      "The perfect links a past action to the present: έχουν βρεθεί 'have been found', δεν έχει αποκρυπτογραφηθεί 'has not been deciphered'. It is formed with έχω + the invariable form: active -ει (έχω γράψει), passive -εί (έχει γραφτεί). Greek uses it less than English: for a dated event use the aorist (βρέθηκαν το 1939).",
      [("Η Γραμμική Α δεν έχει αποκρυπτογραφηθεί μέχρι σήμερα.", "Linear A has not been deciphered to this day."),
       ("τα πρώτα ελληνικά που έχουν γραφτεί ποτέ", "the first Greek that has ever been written")]),
    G("B1", "Fronted object with a clitic, again: names of discoverers", "«Τις πινακίδες τις βρήκε ο Έβανς»",
      "Greek prefers to start with the known topic and end with the new information. To say 'the tablets were found by Evans', it often keeps the verb active and fronts the object, repeating it with a clitic pronoun: Τις πρώτες πινακίδες τις βρήκε ο Έβανς. The new information, ο Έβανς, comes last, where the stress falls.",
      [("Τις πρώτες πινακίδες τις βρήκε στην Κνωσό ο Άρθουρ Έβανς.", "The first tablets were found at Knossos by Arthur Evans."),
       ("Τη Γραμμική Α τη διαβάζουμε περίπου.", "Linear A we can roughly read.")]),
  ],
  terms=[
    T("η γραφή", "script, writing system", "Σύστημα σημείων για να αποδίδεται μια γλώσσα στο γραπτό.", "A system of signs for writing a language."),
    T("το συλλαβόγραμμα", "syllabic sign", "Σημείο γραφής που αποδίδει μια ολόκληρη συλλαβή, π.χ. da, ko.", "A written sign standing for a whole syllable."),
    T("το ιδεόγραμμα", "ideogram", "Σημείο που αποδίδει ένα πράγμα ή μια έννοια με εικόνα.", "A sign that stands for a thing or idea by a picture."),
    T("η αποκρυπτογράφηση", "decipherment", "Το να βρει κανείς πώς διαβάζεται και τι σημαίνει μια άγνωστη γραφή.", "Working out how an unknown script is read and what it means."),
    T("το αρχείο", "archive", "Σύνολο εγγράφων που φυλάγονται μαζί.", "A collection of documents kept together."),
    T("ο άναξ", "wanax, king", "Ο ανώτατος άρχοντας ενός μυκηναϊκού ανακτόρου.", "The supreme ruler of a Mycenaean palace state."),
    T("ο κατάλογος", "list, inventory", "Σειρά από ονόματα ή πράγματα, το ένα κάτω από το άλλο.", "A series of names or items one under another."),
  ],
  questions=[
    Q("Γιατί δεν καταλαβαίνουμε τη Γραμμική Α;", ["Γιατί η γλώσσα της δεν είναι ελληνική και δεν μοιάζει με γνωστή γλώσσα", "Γιατί δεν βρέθηκαν πινακίδες", "Γιατί είναι πολύ μεγάλη", "Γιατί γράφτηκε στην Αίγυπτο"], 0, "We can pronounce many signs but not understand the language."),
    Q("Ποιος αποκρυπτογράφησε τη Γραμμική Β;", ["Ο Μάικλ Βέντρις", "Ο Άρθουρ Έβανς", "Ο Όμηρος", "Ο Καρλ Μπλέγκεν"], 0, "Ventris, with John Chadwick, 1952–53."),
    Q("Πώς σώθηκαν οι πήλινες πινακίδες;", ["Ψήθηκαν στις φωτιές που κατέστρεψαν τα ανάκτορα", "Τις έκρυψαν σε σπηλιές", "Ήταν από μάρμαρο", "Τις αντέγραψαν οι Ρωμαίοι"], 0, "Unbaked clay survived only when the palaces burned."),
    Q("Ποιος θεός εμφανίζεται στις πινακίδες, ενώ τον θεωρούσαν «νέο»;", ["Ο Διόνυσος", "Ο Ερμής ως πρώτος", "Ο Δίας", "Ο Απόλλωνας"], 0, "di-wo-nu-so at Pylos and Chania."),
  ],
  vocab=["γραφή", "σημείο", "απλός", "αποδίδω", "προσαρμογή", "συλλαβή", "άρμα", "κρασί", "λάδι", "βέβαιος", "ενθουσιάζομαι", "οργανώνω", "σύμφωνο", "φωνήεν", "δοκιμάζω", "ανακοινώνω", "ανακάλυψη", "δημοσιεύω", "απόδειξη", "λογαριασμός", "βοσκός", "μερίδα", "πολύτιμος", "αναγνωρίζω", "αντίθετα"],
  sources=[
    SRC("“Linear A”, Wikipedia (date range, corpus, undeciphered status).", "https://en.wikipedia.org/wiki/Linear_A"),
    SRC("Godart, L. (1995). Il disco di Festo: l'enigma di una scrittura. Turin: Einaudi."),
    SRC("Chadwick, J. (1958). The Decipherment of Linear B. Cambridge University Press (repr. 2014)."),
    SRC("Faculty of Classics, University of Cambridge, “Michael Ventris, 1922–1956: Architect and Decipherer of Linear B”.", "https://www.classics.cam.ac.uk/research/projects/mycep/decipherment/ventris"),
    SRC("Ventris, M. & Chadwick, J. (1953). “Evidence for Greek dialect in the Mycenaean archives”. Journal of Hellenic Studies 73: 84–103."),
    SRC("Ventris, M. & Chadwick, J. (1973). Documents in Mycenaean Greek. 2nd ed. Cambridge University Press."),
  ]))

# 2.2 art
CH.append(dict(id="e2-frescoes", theme="art", el="Οι τοιχογραφίες της Θήρας", title="The frescoes of Thera", dates="17ος αιώνας π.Χ.",
  image="spring-fresco",
  summary_en="Akrotiri on Santorini, buried by one of the largest volcanic eruptions of the last ten thousand years, preserved the finest wall paintings of the Aegean Bronze Age.",
  sections=[
    S("pompeii", "Η «Πομπηία του Αιγαίου»", "The 'Pompeii of the Aegean'", [
      P("Στη νότια ακτή της Σαντορίνης, της αρχαίας Θήρας, βρίσκεται ο οικισμός του Ακρωτηρίου. Τον 17ο αιώνα π.Χ. ήταν ένα πλούσιο λιμάνι, με διώροφα και τριώροφα σπίτια, πλακόστρωτους δρόμους και αποχετεύσεις. Ήταν στενά δεμένο με τη μινωική Κρήτη, που βρίσκεται μόλις 110 χιλιόμετρα νοτιότερα. Ξαφνικά όμως ήρθε η καταστροφή: το ηφαίστειο του νησιού εξερράγη και σκέπασε την πόλη με μέτρα ηφαιστειακής στάχτης.",
        "On the south coast of Santorini, ancient Thera, lies the settlement of Akrotiri. In the seventeenth century BC it was a wealthy port with two- and three-storey houses, paved streets and drains. It was closely tied to Minoan Crete, only about 110 km to the south, whose pottery, weights and writing (Linear A) it used. Then disaster came: the island's volcano erupted, in one of the largest eruptions anywhere in the last ten thousand years, and buried the town under metres of pumice and ash. The date is disputed: radiocarbon points to roughly 1620–1600 BC, while traditional archaeological and Egyptian synchronisms suggest a date around 1530–1500 BC.", [1, 2]),
      P("Το Ακρωτήρι ανέσκαψε από το 1967 ο Έλληνας αρχαιολόγος Σπυρίδων Μαρινάτος, ο οποίος πέθανε το 1974 μέσα στον χώρο της ανασκαφής και θάφτηκε εκεί. Τη δουλειά του συνέχισε ο Χρίστος Ντούμας. Σε αντίθεση με την Πομπηία, στο Ακρωτήρι δεν βρέθηκαν σκελετοί ούτε πολλά πολύτιμα αντικείμενα. Φαίνεται ότι οι σεισμοί πριν από την έκρηξη προειδοποίησαν τους κατοίκους, οι οποίοι πρόλαβαν να φύγουν.",
        "Akrotiri was excavated from 1967 by the Greek archaeologist Spyridon Marinatos, who had argued since 1939 that the Thera eruption helped destroy Minoan civilisation; he died at the site in 1974, after a fall, and was buried there. His work was continued by Christos Doumas, who has directed it ever since. Unlike Pompeii, no skeletons and few valuables were found at Akrotiri. It seems that earthquakes before the eruption warned the inhabitants, who managed to leave; there are even signs that some had started clearing rubble and repairing houses before the final eruption. Where they went, and whether they survived, is unknown.", [1, 2]),
    ]),
    S("paintings", "Χελιδόνια, ψαράδες και πλοία", "Swallows, fishermen and ships", [
      P("Ο μεγαλύτερος θησαυρός του Ακρωτηρίου είναι οι τοιχογραφίες του. Η πιο γνωστή, η «Τοιχογραφία της Άνοιξης», δείχνει κόκκινα κρίνα πάνω σε βράχους και χελιδόνια που πετούν σε ζευγάρια, σαν να φλερτάρουν. Είναι η μόνη που βρέθηκε στη θέση της, στους τοίχους ενός δωματίου, ενώ οι άλλες είχαν πέσει και σπάσει. Άλλες τοιχογραφίες δείχνουν δύο αγόρια που κάνουν πυγμαχία, έναν νεαρό ψαρά με δύο ματσάκια ψάρια και γυναίκες που μαζεύουν κρόκο.",
        "Akrotiri's greatest treasure is its wall paintings. The best known, the Spring Fresco, shows red lilies growing on volcanic rocks and swallows flying in pairs, as if courting; it covered three walls of a small room and is the only one found in place on the walls, while the others had fallen and broken and had to be pieced together from thousands of fragments. Other paintings show two boys boxing, each wearing a single glove; a young fisherman carrying two strings of fish; and girls gathering crocus (saffron) flowers, which was probably both a ritual and an economic activity. The paintings are now in the National Archaeological Museum in Athens and the Museum of Prehistoric Thera in Fira.", [1, 3]),
      P("Η πιο εντυπωσιακή σύνθεση είναι η «Μικρογραφική ζωφόρος» από την «Οικία του Δυτικού». Πάνω από ένα παράθυρο ο ζωγράφος παρέστησε έναν ολόκληρο στόλο που ταξιδεύει από πόλη σε πόλη, με δελφίνια γύρω από τα πλοία και ανθρώπους που τον παρακολουθούν από τις στέγες. Είναι μια από τις παλαιότερες αναπαραστάσεις τοπίου και θάλασσας στην ευρωπαϊκή τέχνη, και ένα πολύτιμο ντοκουμέντο για τα πλοία της εποχής.",
        "The most impressive composition is the 'Miniature Frieze' from the so-called West House. Above a window the painter depicted an entire fleet sailing from one town to another, with dolphins around the ships and people watching from the rooftops; scholars still debate whether it shows a festival, a military expedition or a myth. It is one of the oldest depictions of landscape and seascape in European art, and a precious document for the ships of the period, which are shown with oars, sails, cabins for captains and decorated hulls.", [1, 3]),
    ]),
    S("technique", "Πώς ζωγράφιζαν", "How they painted", [
      P("Οι ζωγράφοι δούλευαν πάνω σε ασβεστοκονίαμα, που ήταν συχνά ακόμα υγρό. Έτσι τα χρώματα απορροφούνταν και γίνονταν μέρος του τοίχου, γι' αυτό διατηρήθηκαν τόσο φωτεινά. Χρησιμοποιούσαν λίγα χρώματα, από ορυκτά: κόκκινο και κίτρινο από γαίες, μπλε από ένα ειδικό ορυκτό, και μαύρο. Τα πρόσωπα των αντρών τα ζωγράφιζαν κοκκινωπά και των γυναικών λευκά, όπως και στην Αίγυπτο.",
        "The painters worked on lime plaster that was often still wet, so that the pigments were absorbed and became part of the wall (true fresco, buon fresco), which is why they have kept such bright colours; details were sometimes added on dry plaster. They used a small palette of mineral pigments: red and yellow from ochres, blue from a special pigment (Egyptian blue or glaucophane, a blue mineral), and black from carbon or manganese. By convention men's skin is painted reddish-brown and women's white, as in Egypt, a convention that says more about ideals of indoor and outdoor life than about real skin colour.", [3, 4]),
    ]),
  ],
  grammar=[
    G("B1", "The gerund in -οντας / -ώντας", "Η μετοχή σε -οντας/-ώντας",
      "The active participle (gerund) never changes form. It shows an action happening at the same time as the main verb, or the way something is done: ταξιδεύοντας 'travelling', κοιτάζοντας 'looking', ζωγραφίζοντας 'by painting'. Verbs in -ώ/-άω take -ώντας: πετώντας, οδηγώντας. Its subject is normally the subject of the main verb.",
      [("Οι ζωγράφοι δούλευαν βάζοντας τα χρώματα στον υγρό τοίχο.", "The painters worked by putting the colours on the wet wall."),
       ("Τα χελιδόνια πετούν σε ζευγάρια, φλερτάροντας.", "The swallows fly in pairs, flirting.")]),
    G("B1", "σε αντίθεση με, ενώ: contrast", "Αντίθεση: «σε αντίθεση με» και «ενώ»",
      "σε αντίθεση με + accusative contrasts two things: σε αντίθεση με την Πομπηία 'unlike Pompeii'. ενώ 'while, whereas' joins two clauses that contrast: Είναι η μόνη που βρέθηκε στη θέση της, ενώ οι άλλες είχαν πέσει.",
      [("Σε αντίθεση με την Πομπηία, δεν βρέθηκαν σκελετοί.", "Unlike Pompeii, no skeletons were found."),
       ("Των αντρών τα πρόσωπα είναι κοκκινωπά, ενώ των γυναικών λευκά.", "Men's faces are reddish, whereas women's are white.")]),
  ],
  terms=[
    T("η τοιχογραφία", "wall painting, fresco", "Ζωγραφική πάνω σε τοίχο.", "A painting on a wall."),
    T("η έκρηξη", "eruption, explosion", "Το απότομο ξέσπασμα ενός ηφαιστείου.", "The sudden outburst of a volcano."),
    T("η κίσσηρη", "pumice", "Ελαφριά, πορώδης ηφαιστειακή πέτρα· λέγεται και ελαφρόπετρα.", "Light, porous volcanic rock (also ελαφρόπετρα)."),
    T("η ζωφόρος", "frieze", "Μακριά οριζόντια ζώνη με παραστάσεις σε τοίχο ή ναό.", "A long horizontal band of images on a wall or temple."),
    T("το ασβεστοκονίαμα", "lime plaster", "Μείγμα από ασβέστη, άμμο και νερό για να καλύπτονται οι τοίχοι.", "A mix of lime, sand and water used to coat walls."),
    T("η αναπαράσταση", "depiction, representation", "Το να δείχνει κανείς κάτι με εικόνα.", "Showing something in an image."),
  ],
  questions=[
    Q("Γιατί λένε το Ακρωτήρι «Πομπηία του Αιγαίου»;", ["Γιατί το σκέπασε ηφαιστειακή στάχτη", "Γιατί το έχτισαν οι Ρωμαίοι", "Γιατί βρέθηκαν εκεί πολλοί σκελετοί", "Γιατί είναι στην Ιταλία"], 0, "Like Pompeii, it was buried by an eruption."),
    Q("Γιατί δεν βρέθηκαν σκελετοί στο Ακρωτήρι;", ["Οι κάτοικοι προειδοποιήθηκαν από σεισμούς και έφυγαν", "Τους πήραν οι αρχαιολόγοι", "Δεν υπήρχαν κάτοικοι", "Ήταν όλοι στη θάλασσα"], 0, "Earthquakes gave warning."),
    Q("Τι δείχνει η «Τοιχογραφία της Άνοιξης»;", ["Κρίνα και χελιδόνια", "Δύο αγόρια που πυγμαχούν", "Έναν στόλο", "Γυναίκες που μαζεύουν κρόκο"], 0, "Red lilies and swallows in pairs."),
    Q("Γιατί τα χρώματα των τοιχογραφιών έμειναν φωτεινά;", ["Γιατί μπήκαν σε υγρό ασβεστοκονίαμα και έγιναν μέρος του τοίχου", "Γιατί ξαναβάφτηκαν το 1967", "Γιατί ήταν από χρυσό", "Γιατί ήταν κάτω από το νερό"], 0, "Buon fresco technique."),
  ],
  vocab=["ακτή", "λιμάνι", "πλακόστρωτος", "δεμένος", "ηφαίστειο", "εκρήγνυμαι", "σκεπάζω", "στάχτη", "σκελετός", "προειδοποιώ", "προλαβαίνω", "θησαυρός", "κρίνο", "χελιδόνι", "πυγμαχία", "εντυπωσιακός", "στόλος", "παρακολουθώ", "στέγη", "τοπίο", "απορροφώ", "διατηρούμαι", "φωτεινός", "ορυκτό"],
  sources=[
    SRC("“Akrotiri (prehistoric city)”, Wikipedia (excavation, absence of remains, eruption date debate).", "https://en.wikipedia.org/wiki/Akrotiri_(prehistoric_city)"),
    SRC("Manning, S. W. et al. (2014). “Dating the Thera (Santorini) eruption: archaeological and scientific evidence supporting a high chronology”. Antiquity 88: 1164–1179."),
    SRC("Doumas, C. (1992). The Wall-Paintings of Thera. Athens: Thera Foundation."),
    SRC("Brysbaert, A. (2008). The Power of Technology in the Bronze Age Eastern Mediterranean: The Case of the Painted Plaster. London: Equinox."),
  ]))

# 2.3 politics
CH.append(dict(id="e2-palaces", theme="politics", el="Τα μυκηναϊκά ανάκτορα και ο άναξ", title="The Mycenaean palaces and the wanax", dates="περ. 1600–1100 π.Χ.",
  image="chariot-krater",
  summary_en="How the Mycenaean kingdoms were run, as revealed by Schliemann's spade and the Linear B tablets, and how the palace system collapsed around 1200 BC.",
  sections=[
    S("schliemann", "Ο Σλήμαν και ο «χρυσός των Μυκηνών»", "Schliemann and the 'gold of Mycenae'", [
      P("Το 1876 ο Γερμανός επιχειρηματίας Ερρίκος Σλήμαν, που είχε ήδη σκάψει στην Τροία, άρχισε ανασκαφή στις Μυκήνες. Μέσα στον λεγόμενο «Ταφικό Κύκλο Α» βρήκε τάφους γεμάτους χρυσά κοσμήματα, όπλα και πέντε χρυσές προσωπίδες. Όταν είδε την πιο εντυπωσιακή, πίστεψε ότι είχε βρει το πρόσωπο του Αγαμέμνονα, του βασιλιά που κατά τον Όμηρο οδήγησε τους Έλληνες στην Τροία.",
        "In 1876 the German businessman Heinrich Schliemann, who had already dug at Troy, began excavating at Mycenae, using Pausanias's description of the royal graves as his guide. Inside the so-called Grave Circle A he found shaft graves full of gold jewellery, weapons and five gold funerary masks. When he saw the most impressive one, he believed he had found the face of Agamemnon, the king who, according to Homer, led the Greeks to Troy. The story that he cabled the King of Greece 'I have gazed upon the face of Agamemnon' is probably a later embellishment.", [1, 2]),
      P("Σήμερα ξέρουμε ότι η «μάσκα του Αγαμέμνονα» είναι από το 1550–1500 π.Χ. περίπου, δηλαδή τρεις αιώνες πριν από τον Τρωικό πόλεμο, αν αυτός έγινε ποτέ. Η ανακάλυψη του Σλήμαν όμως ήταν τεράστια: έδειξε ότι πίσω από τα έπη υπήρχε ένας πραγματικός, πλούσιος πολιτισμός. Από το όνομα των Μυκηνών τον ονομάζουμε «μυκηναϊκό».",
        "Today we know that the 'Mask of Agamemnon' dates to about 1550–1500 BC, some three centuries before the traditional date of the Trojan War, if it ever took place; a minority of scholars have even questioned whether Schliemann embellished the mask itself, though most accept it as genuine. Schliemann's discovery was nonetheless enormous: it showed that behind the epics lay a real, wealthy civilisation, with contacts reaching Egypt, Anatolia and the Baltic (amber). From the name of Mycenae we call it 'Mycenaean', although Mycenae was only one of several centres.", [1, 2]),
    ]),
    S("state", "Ένα κράτος με γραφειοκρατία", "A state with a bureaucracy", [
      P("Τον 14ο και τον 13ο αιώνα π.Χ. η ηπειρωτική Ελλάδα ήταν χωρισμένη σε μικρά βασίλεια, με κέντρο ένα ανάκτορο: στις Μυκήνες, στην Τίρυνθα, στην Πύλο, στη Θήβα. Στην κορυφή βρισκόταν ο άναξ. Κάτω από αυτόν υπήρχε ο λαβαγέτας, πιθανώς ο αρχηγός του στρατού, και πολλοί αξιωματούχοι. Στα χωριά υπήρχαν τοπικοί άρχοντες, οι «βασιλείς», μια λέξη που αργότερα θα σημαίνει «βασιλιάς».",
        "In the fourteenth and thirteenth centuries BC mainland Greece was divided into small kingdoms, each centred on a palace: Mycenae, Tiryns, Pylos, Thebes, perhaps also Athens and Iolkos. At the top stood the wanax (wa-na-ka). Below him was the lawagetas (ra-wa-ke-ta), probably the leader of the army or 'of the people', and many officials whose titles we can read but whose duties we can only guess. In the villages there were local leaders called qa-si-re-u (basileus), a word that later came to mean 'king'; when the palaces fell, these local chiefs survived, which is one reason the word rose in status.", [3, 4]),
      P("Οι πινακίδες της Γραμμικής Β δείχνουν ότι το ανάκτορο έλεγχε μεγάλο μέρος της οικονομίας. Μάζευε φόρους σε προϊόντα, όπως σιτάρι, λάδι, μαλλί και μέλι, οργάνωνε εργαστήρια και μοίραζε μερίδες φαγητού στους εργάτες. Στην Πύλο, για παράδειγμα, οι πινακίδες αναφέρουν εκατοντάδες γυναίκες υφάντριες με τα παιδιά τους. Είναι μια εικόνα πολύ διαφορετική από τους ήρωες του Ομήρου: ένα κράτος με γραφειοκρατία.",
        "The Linear B tablets show that the palace controlled a large part of the economy. It collected taxes in kind, such as wheat, oil, wool and honey, organised workshops (perfumed oil, bronze, chariots, textiles) and distributed food rations to workers. At Pylos, for example, the tablets list several hundred women textile workers with their children, many of them apparently of foreign origin, some possibly captives from the Anatolian coast. It is a picture very different from Homer's heroes: a state with a bureaucracy, scribes and inventories, rather like the palace economies of the Near East.", [3, 4]),
    ]),
    S("collapse", "Η κατάρρευση γύρω στο 1200 π.Χ.", "The collapse around 1200 BC", [
      P("Γύρω στο 1200 π.Χ. τα περισσότερα μυκηναϊκά ανάκτορα καταστράφηκαν από φωτιά. Η αιτία δεν είναι σαφής. Οι ερευνητές μιλούν για σεισμούς, ξηρασία, εξεγέρσεις, εισβολές, ή για έναν συνδυασμό όλων αυτών. Την ίδια εποχή καταρρέουν και άλλα κράτη της ανατολικής Μεσογείου, όπως η αυτοκρατορία των Χετταίων, ενώ η Αίγυπτος πολεμά με τους λεγόμενους «Λαούς της Θάλασσας».",
        "Around 1200 BC most of the Mycenaean palaces were destroyed by fire. The cause is not clear. Researchers speak of earthquakes, drought, revolts, invasions or a combination of all of these ('systems collapse'); the later Greek legend of the 'return of the Heracleidae' and the old theory of a 'Dorian invasion' have little archaeological support. At the same time other states of the eastern Mediterranean were collapsing too, such as the Hittite empire and the city of Ugarit in Syria, while Egypt was fighting the so-called 'Sea Peoples', as Ramesses III recorded on the walls of his temple at Medinet Habu. Some Mycenaean sites lived on into the twelfth century BC, but by about 1100 BC the palace world was gone.", [5, 6]),
      P("Με τα ανάκτορα χάθηκε και η γραφή. Για περίπου τέσσερις αιώνες οι Έλληνες δεν έγραφαν. Ο πληθυσμός μειώθηκε, το εμπόριο περιορίστηκε και οι άνθρωποι ζούσαν σε μικρότερες κοινότητες. Η ανάμνηση όμως των παλιών βασιλείων δεν χάθηκε: πέρασε στους μύθους και στα έπη, που οι αοιδοί τραγουδούσαν από γενιά σε γενιά.",
        "With the palaces, writing disappeared too: for about four centuries the Greeks did not write, since Linear B had been a tool of palace administration, not of everyday life. The population fell, trade shrank and people lived in smaller communities. But the memory of the old kingdoms did not disappear: it passed into myths and epics, which bards (aoidoi) sang from generation to generation. The Homeric Catalogue of Ships still lists places that mattered in the Bronze Age, and Homeric words such as ἄναξ and objects like the boar's-tusk helmet are Mycenaean survivals.", [5, 6]),
    ]),
  ],
  grammar=[
    G("B1", "Neuter plurals and big numbers", "Εκατοντάδες, χιλιάδες, εκατομμύρια",
      "εκατοντάδα 'a hundred (approx.)', χιλιάδα 'a thousand', εκατομμύριο 'a million' are nouns: εκατοντάδες γυναίκες 'hundreds of women', χιλιάδες κομμάτια 'thousands of pieces', with the noun in the same case, not a genitive. Exact hundreds agree in gender: τριακόσιοι άντρες, τριακόσιες γυναίκες, τριακόσια πλοία.",
      [("Οι πινακίδες αναφέρουν εκατοντάδες γυναίκες υφάντριες.", "The tablets mention hundreds of women weavers."),
       ("τρεις αιώνες πριν από τον Τρωικό πόλεμο", "three centuries before the Trojan War")]),
    G("B1", "θα + imperfect: 'would' and future in the past", "«Θα» με παρατατικό: το μέλλον στο παρελθόν",
      "θα + imperfect can describe what was going to happen later, seen from a past point: μια λέξη που αργότερα θα σήμαινε «βασιλιάς» 'a word that would later mean king'. The same form also expresses conditional 'would' and probability: θα ήταν 'it must have been / it would be'.",
      [("μια λέξη που αργότερα θα σήμαινε «βασιλιάς»", "a word that would later mean 'king'"),
       ("Ο λαβαγέτας θα ήταν μάλλον ο αρχηγός του στρατού.", "The lawagetas was probably the army leader.")]),
  ],
  terms=[
    T("η προσωπίδα", "(funerary) mask", "Μάσκα που κάλυπτε το πρόσωπο του νεκρού.", "A mask covering the face of the dead."),
    T("ο ταφικός κύκλος", "grave circle", "Κυκλικός περίβολος με βασιλικούς τάφους στις Μυκήνες.", "A circular enclosure of royal graves at Mycenae."),
    T("το έπος", "epic poem", "Μεγάλο αφηγηματικό ποίημα για ήρωες, όπως η «Ιλιάδα».", "A long narrative poem about heroes, like the Iliad."),
    T("ο αξιωματούχος", "official", "Πρόσωπο με δημόσια θέση και εξουσία.", "A person holding public office."),
    T("ο φόρος", "tax", "Χρήματα ή προϊόντα που πληρώνει κανείς στο κράτος.", "Money or goods paid to the state."),
    T("η γραφειοκρατία", "bureaucracy", "Διοίκηση με γραφείς, έγγραφα και κανόνες.", "Administration by scribes, documents and rules."),
    T("ο αοιδός", "bard", "Ποιητής που τραγουδούσε έπη απ' έξω.", "A poet who sang epics from memory."),
  ],
  questions=[
    Q("Τι πίστεψε ο Σλήμαν όταν βρήκε τη χρυσή προσωπίδα;", ["Ότι ήταν το πρόσωπο του Αγαμέμνονα", "Ότι ήταν αιγυπτιακή", "Ότι ήταν ψεύτικη", "Ότι ήταν του Οδυσσέα"], 0, "It is in fact three centuries older."),
    Q("Ποιος ήταν στην κορυφή ενός μυκηναϊκού βασιλείου;", ["Ο άναξ", "Ο βασιλεύς", "Ο λαβαγέτας", "Ο γραφέας"], 0, "wa-na-ka in Linear B."),
    Q("Τι έκανε το ανάκτορο, σύμφωνα με τις πινακίδες;", ["Μάζευε φόρους και μοίραζε μερίδες", "Δεν είχε καμία σχέση με την οικονομία", "Έγραφε ποιήματα", "Έκοβε νομίσματα"], 0, "Coinage did not exist yet."),
    Q("Τι έγινε με τη γραφή μετά την κατάρρευση;", ["Χάθηκε για περίπου τέσσερις αιώνες", "Έγινε πιο διαδεδομένη", "Αντικαταστάθηκε από τα λατινικά", "Τη χρησιμοποιούσαν μόνο τα παιδιά"], 0, "Writing returns with the alphabet in the 8th century BC."),
  ],
  vocab=["επιχειρηματίας", "σκάβω", "τάφος", "όπλο", "οδηγώ", "τεράστιος", "πραγματικός", "χωρισμένος", "βασίλειο", "κορυφή", "αρχηγός", "στρατός", "άρχοντας", "οικονομία", "προϊόν", "μαλλί", "μέλι", "εργαστήριο", "μοιράζω", "σαφής", "ξηρασία", "εξέγερση", "εισβολή", "αυτοκρατορία", "πληθυσμός", "μειώνομαι", "εμπόριο", "ανάμνηση", "γενιά"],
  sources=[
    SRC("Schliemann, H. (1878). Mycenae: A Narrative of Researches and Discoveries at Mycenae and Tiryns. London: John Murray."),
    SRC("“Mask of Agamemnon”, Wikipedia (date c. 1550–1500 BC, authenticity debate).", "https://en.wikipedia.org/wiki/Mask_of_Agamemnon"),
    SRC("Chadwick, J. (1976). The Mycenaean World. Cambridge University Press."),
    SRC("Shelmerdine, C. W. (ed.) (2008). The Cambridge Companion to the Aegean Bronze Age. Cambridge University Press, ch. 6 and 12."),
    SRC("Cline, E. H. (2014). 1177 B.C.: The Year Civilization Collapsed. Princeton University Press."),
    SRC("Dickinson, O. (2006). The Aegean from Bronze Age to Iron Age. London: Routledge."),
  ]))

# 2.4 science / engineering
CH.append(dict(id="e2-engineering", theme="science", el="Κυκλώπεια τείχη, θόλοι και γέφυρες", title="Cyclopean walls, tholos tombs and bridges", dates="περ. 1900–1200 π.Χ.",
  image="atreus",
  summary_en="Bronze Age engineering in Greece: Minoan plumbing at Knossos, Mycenaean walls so large that later Greeks credited them to giants, the dome of the 'Treasury of Atreus', roads, bridges and the draining of Lake Kopais.",
  sections=[
    S("knossos", "Νερό και φως στην Κνωσό", "Water and light at Knossos", [
      P("Οι Μινωίτες ήταν εξαιρετικοί μηχανικοί. Το ανάκτορο της Κνωσού, που χτίστηκε γύρω στο 1900 π.Χ. και ξαναχτίστηκε μετά από σεισμούς, είχε πολλούς ορόφους, μεγάλες σκάλες και ένα σύστημα με πήλινους σωλήνες για το νερό. Οι σωλήνες ήταν κωνικοί και έμπαιναν ο ένας μέσα στον άλλο, έτσι ώστε το νερό να τρέχει με πίεση και να μη μαζεύονται άλατα. Χωριστά κανάλια μάζευαν τα νερά της βροχής και τα λύματα.",
        "The Minoans were excellent engineers. The palace of Knossos, first built around 1900 BC and rebuilt after earthquakes, had several storeys, monumental staircases and a system of clay pipes for water. The pipe sections were tapered and fitted into one another, so that the water ran with some pressure and sediment was flushed out instead of settling. Separate stone channels collected rainwater and waste water, and some rooms had what looks like a flushing latrine. Much of what visitors see today, however, including the red columns, is Arthur Evans's reinforced-concrete reconstruction of the 1920s and 1930s, which archaeologists now regard with mixed feelings.", [1, 2]),
      P("Τα ανάκτορα είχαν επίσης «φωταγωγούς», δηλαδή ανοιχτά φρεάτια στο κέντρο του κτιρίου, που έφερναν φως και αέρα στους κάτω ορόφους. Έτσι τα δωμάτια έμεναν δροσερά το καλοκαίρι. Πολλές από αυτές τις λύσεις τις ξαναβρήκε η ευρωπαϊκή αρχιτεκτονική πολλούς αιώνες αργότερα.",
        "The palaces also had light wells, open shafts in the middle of the building that brought light and air down to the lower floors and kept the rooms cool in summer. Columns of cypress wood, wider at the top than at the bottom, supported the roofs. Several of these solutions, such as light wells and planned drainage, were reinvented by European architecture many centuries later, though there is no direct line of influence.", [1, 2]),
    ]),
    S("cyclopean", "Τείχη για γίγαντες", "Walls for giants", [
      P("Οι Μυκηναίοι έχτισαν γύρω από τις ακροπόλεις τους τείχη από τεράστιες πέτρες, μερικές από τις οποίες ζυγίζουν πολλούς τόνους. Οι μεταγενέστεροι Έλληνες δεν μπορούσαν να φανταστούν πώς τις σήκωσαν άνθρωποι. Γι' αυτό πίστευαν ότι τα τείχη τα είχαν χτίσει οι Κύκλωπες, οι μυθικοί γίγαντες με το ένα μάτι. Από τότε τα λέμε «κυκλώπεια». Ο περιηγητής Παυσανίας, τον 2ο αιώνα μ.Χ., γράφει ότι ούτε δύο μουλάρια δεν θα μπορούσαν να κουνήσουν ούτε τη μικρότερη πέτρα στα τείχη της Τίρυνθας.",
        "The Mycenaeans built walls of huge stones around their citadels, some of which weigh several tonnes; at Tiryns the walls are up to about 8 m thick in places and contain galleries roofed with corbelled stone. Later Greeks could not imagine how human beings had lifted them, so they believed the walls had been built by the Cyclopes, the mythical one-eyed giants; that is why we still call this kind of masonry 'Cyclopean'. The traveller Pausanias, in the second century AD, writes of the walls of Tiryns that not even a pair of mules could move the smallest of their stones, and he ranks them with the pyramids of Egypt as a wonder (Description of Greece 2.25.8, 9.36.5).", [3, 4]),
      P("Η πιο διάσημη είσοδος είναι η Πύλη των Λεόντων στις Μυκήνες, από το 1250 π.Χ. περίπου. Πάνω από το υπέρθυρο υπάρχει ένα τριγωνικό ανάγλυφο με δύο λιοντάρια ή γρύπες, που στέκονται αντικριστά δίπλα σε μια κολόνα. Είναι το παλαιότερο μνημειακό γλυπτό της Ευρώπης που βρίσκεται ακόμα στη θέση του. Το τρίγωνο έχει και πρακτικό ρόλο: παίρνει το βάρος από το υπέρθυρο, για να μη σπάσει.",
        "The most famous entrance is the Lion Gate at Mycenae, from about 1250 BC. Above the lintel is a triangular relief of two lions (or lionesses; their heads, made separately, are lost) standing face to face on either side of a column. It is often described as the oldest monumental sculpture in Europe still in its original position. The triangle also has a practical role: it is a 'relieving triangle' that takes the weight of the wall off the lintel so that the lintel does not crack.", [3, 5]),
    ]),
    S("tholos", "Ο θόλος και οι γέφυρες", "The dome and the bridges", [
      P("Οι Μυκηναίοι έθαβαν τους βασιλιάδες τους σε θολωτούς τάφους. Ο μεγαλύτερος είναι ο λεγόμενος «Θησαυρός του Ατρέα» στις Μυκήνες, από τον 13ο αιώνα π.Χ. Ο θόλος του έχει διάμετρο σχεδόν 15 μέτρα και ύψος πάνω από 13 μέτρα. Δεν είναι πραγματικός θόλος, αλλά «ψευδοθόλος»: κάθε σειρά από πέτρες προεξέχει λίγο από την προηγούμενη, μέχρι να κλείσει η κορυφή. Για περισσότερα από χίλια χρόνια ήταν ο μεγαλύτερος θόλος του κόσμου, μέχρι να χτιστεί το Πάνθεον στη Ρώμη.",
        "The Mycenaeans buried their kings in tholos (beehive) tombs. The largest is the so-called Treasury of Atreus at Mycenae, from the thirteenth century BC (the name is a later legend: it was neither a treasury nor demonstrably Atreus's). Its dome is nearly 15 m across (about 14.5 m) and over 13 m high. It is not a true dome but a corbelled one: each course of stones projects slightly beyond the one below until the top closes. The lintel over the door is a single block about 8 m long, estimated at around 120 tonnes. For well over a thousand years it was the widest dome in the world, until the Romans built domes with concrete; the Pantheon in Rome (c. AD 125) is usually named as the one that surpassed it.", [5, 6]),
      P("Οι Μυκηναίοι έφτιαξαν επίσης δρόμους για άρματα και πέτρινες γέφυρες. Μία από αυτές, η γέφυρα του Αρκαδικού, κοντά στο Ναύπλιο, χτίστηκε γύρω στο 1300–1190 π.Χ. και χρησιμοποιείται ακόμα από τους ντόπιους. Στη Βοιωτία οι Μυκηναίοι αποξήραναν μεγάλο μέρος της λίμνης Κωπαΐδας με κανάλια και φράγματα, για να κερδίσουν γη για καλλιέργεια. Όταν τα έργα εγκαταλείφθηκαν, η λίμνη ξαναγέμισε, και αποξηράνθηκε ξανά μόνο τον 19ο αιώνα.",
        "The Mycenaeans also built roads for chariots and stone bridges. One of them, the Arkadiko bridge near Nafplio, a corbel-arch bridge 22 m long on the old road between Tiryns and Epidaurus, was built around 1300–1190 BC and is still used by locals as a track, which makes it one of the oldest bridges in use anywhere. In Boeotia, in the thirteenth century BC, the Mycenaeans drained much of Lake Kopais with canals, dykes and the great fortress of Gla to guard them, in order to win land for farming. When the works were abandoned, the lake filled again; it was drained once more only in the late nineteenth century (1880s), by a British company.", [7, 8]),
    ]),
  ],
  grammar=[
    G("B1+", "Purpose and result: για να, ώστε να, έτσι ώστε", "Σκοπός και αποτέλεσμα",
      "για να + subjunctive gives the purpose ('in order to'): για να κερδίσουν γη. ώστε να / έτσι ώστε να stress the intended result of a design: οι σωλήνες ήταν κωνικοί, έτσι ώστε το νερό να τρέχει. The negative is μη(ν): για να μη σπάσει.",
      [("Αποξήραναν τη λίμνη για να κερδίσουν γη.", "They drained the lake to win land."),
       ("Το τρίγωνο παίρνει το βάρος, για να μη σπάσει το υπέρθυρο.", "The triangle takes the weight so that the lintel does not break.")]),
    G("B1+", "μέχρι να: 'until' with the subjunctive", "«Μέχρι να» + υποτακτική",
      "For 'until' something happens (or happened), Greek uses μέχρι να / ώσπου να + subjunctive, even about the past: μέχρι να χτιστεί το Πάνθεον 'until the Pantheon was built'; κάθε σειρά προεξέχει μέχρι να κλείσει η κορυφή.",
      [("Ήταν ο μεγαλύτερος θόλος, μέχρι να χτιστεί το Πάνθεον.", "It was the largest dome until the Pantheon was built."),
       ("κάθε σειρά προεξέχει, μέχρι να κλείσει η κορυφή", "each course projects until the top closes")]),
  ],
  terms=[
    T("ο μηχανικός", "engineer", "Αυτός που σχεδιάζει και κατασκευάζει κτίρια, δρόμους, μηχανές.", "Someone who designs and builds structures or machines."),
    T("ο φωταγωγός", "light well", "Ανοιχτό φρεάτιο μέσα σε κτίριο για φως και αέρα.", "An open shaft inside a building for light and air."),
    T("κυκλώπειος", "Cyclopean", "Χτισμένος με τεράστιες ακατέργαστες πέτρες.", "Built of huge, roughly shaped stones."),
    T("το υπέρθυρο", "lintel", "Η οριζόντια πέτρα ή δοκός πάνω από μια πόρτα.", "The horizontal beam or stone above a door."),
    T("το ανάγλυφο", "relief", "Γλυπτό που προεξέχει από μια επίπεδη επιφάνεια.", "A sculpture projecting from a flat surface."),
    T("ο θολωτός τάφος", "tholos tomb", "Υπόγειος κυκλικός τάφος με θόλο.", "An underground circular tomb with a domed roof."),
    T("αποξηραίνω", "to drain (land, a lake)", "Βγάζω το νερό από μια λίμνη ή έλος για να γίνει ξηρά.", "To remove water from a lake or marsh to make dry land."),
  ],
  questions=[
    Q("Γιατί οι σωλήνες της Κνωσού ήταν κωνικοί;", ["Για να τρέχει το νερό με πίεση και να μη μαζεύονται άλατα", "Για ομορφιά", "Γιατί δεν ήξεραν άλλο σχήμα", "Για να κρατούν κρασί"], 0, "Tapered sections fitted together."),
    Q("Γιατί λέγονται «κυκλώπεια» τα τείχη;", ["Γιατί πίστευαν ότι τα έχτισαν οι Κύκλωπες", "Γιατί είναι κυκλικά", "Γιατί είναι στις Κυκλάδες", "Γιατί τα έχτισε ο Κύκλωπας Πολύφημος για τον Οδυσσέα"], 0, "Pausanias reports the belief."),
    Q("Τι είναι ο «ψευδοθόλος»;", ["Θόλος όπου κάθε σειρά πέτρας προεξέχει λίγο από την προηγούμενη", "Θόλος από μπετόν", "Θόλος από ξύλο", "Ζωγραφισμένος θόλος"], 0, "A corbelled dome."),
    Q("Τι έκαναν οι Μυκηναίοι στη λίμνη Κωπαΐδα;", ["Την αποξήραναν για καλλιέργεια", "Έχτισαν πόλη μέσα της", "Την έκαναν λιμάνι", "Έφτιαξαν γέφυρα πάνω της"], 0, "With canals, dykes and the fortress of Gla."),
  ],
  vocab=["εξαιρετικός", "όροφος", "σκάλα", "σωλήνας", "πίεση", "άλας", "κανάλι", "βροχή", "λύματα", "δροσερός", "λύση", "ζυγίζω", "φαντάζομαι", "σηκώνω", "μυθικός", "γίγαντας", "κουνώ", "είσοδος", "λιοντάρι", "κολόνα", "βάρος", "θάβω", "διάμετρος", "προεξέχω", "γέφυρα", "ντόπιος", "φράγμα", "εγκαταλείπω"],
  sources=[
    SRC("Angelakis, A. N. et al. (2005). “Urban wastewater and stormwater technologies in ancient Greece”. Water Research 39: 210–220."),
    SRC("MacGillivray, J. A. (2000). Minotaur: Sir Arthur Evans and the Archaeology of the Minoan Myth. London: Jonathan Cape."),
    SRC("Pausanias, Description of Greece 2.16.5, 2.25.8 and 9.36.5 (Cyclopean walls of Mycenae and Tiryns)."),
    SRC("Loader, N. C. (1998). Building in Cyclopean Masonry. Jonsered: Paul Åströms Förlag."),
    SRC("Wace, A. J. B. (1949). Mycenae: An Archaeological History and Guide. Princeton University Press."),
    SRC("Cavanagh, W. & Laxton, R. (1981). “The structural mechanics of the Mycenaean tholos tomb”. Annual of the British School at Athens 76: 109–140."),
    SRC("“Arkadiko Bridge”, Wikipedia (date 1300–1190 BC, corbel arch, still in use).", "https://en.wikipedia.org/wiki/Arkadiko_Bridge"),
    SRC("Knauss, J. (1987). Die Melioration des Kopaisbeckens durch die Minyer im 2. Jt. v. Chr. Munich: Technische Universität."),
  ]))

# 2.5 culture / religion
CH.append(dict(id="e2-minoans", theme="culture", el="Ταύροι, θεές και θάλασσα: ο κόσμος των Μινωιτών", title="Bulls, goddesses and the sea: the Minoan world", dates="περ. 2000–1450 π.Χ.",
  image="larnax",
  summary_en="Minoan Crete as later Greeks remembered it and as archaeology shows it: palaces without walls, bull-leaping, sanctuaries on mountain peaks, and the Mycenaean takeover of Knossos.",
  sections=[
    S("minos", "Ο βασιλιάς Μίνωας και η θαλασσοκρατορία", "King Minos and the thalassocracy", [
      P("Όταν ο Άρθουρ Έβανς άρχισε να σκάβει στην Κνωσό το 1900, έδωσε στον πολιτισμό που βρήκε το όνομα του μυθικού βασιλιά Μίνωα. Οι ίδιοι οι «Μινωίτες» δεν ξέρουμε πώς έλεγαν τον εαυτό τους. Οι αρχαίοι Έλληνες όμως θυμούνταν ότι η Κρήτη ήταν κάποτε μεγάλη δύναμη. Ο ιστορικός Θουκυδίδης γράφει ότι ο Μίνωας ήταν ο πρώτος που απέκτησε στόλο και κυριάρχησε στη θάλασσα.",
        "When Arthur Evans began digging at Knossos in 1900, he named the civilisation he found after the mythical King Minos. What the 'Minoans' called themselves we do not know; Egyptian texts call Crete Keftiu, and Near Eastern texts Kaptara. But the ancient Greeks remembered that Crete had once been a great power. The historian Thucydides writes that Minos was the first known ruler to acquire a navy and to rule the sea, clearing it of pirates and planting colonies in the Cyclades (1.4). Modern scholars call this the 'Minoan thalassocracy', though how far Crete actually ruled other islands, rather than trading with and influencing them, is debated.", [1, 2]),
      P("Τα μινωικά ανάκτορα, στην Κνωσό, στη Φαιστό, στα Μάλια και στη Ζάκρο, έχουν κάτι παράξενο: δεν έχουν ισχυρά τείχη. Παλαιότερα αυτό οδήγησε σε μια ρομαντική εικόνα των Μινωιτών ως ειρηνικού λαού. Σήμερα οι ερευνητές είναι πιο επιφυλακτικοί, γιατί υπάρχουν όπλα, φυλάκια και κάποιες ενδείξεις βίας. Πιθανότατα όμως ο στόλος ήταν η κύρια άμυνα του νησιού.",
        "The Minoan palaces, at Knossos, Phaistos, Malia and Zakros, have something strange about them: they lack strong fortification walls. In the past this led to a romantic picture of the Minoans as a peaceful, nature-loving and even 'matriarchal' people, a picture that owes much to the early twentieth century. Today researchers are more cautious, since there are weapons, guard posts along roads and some signs of violence, including a possible human sacrifice at Anemospilia near Archanes. Still, the fleet was probably the island's main defence. The palaces were less 'palaces' in our sense than centres of ritual, storage and administration, built around a large central court.", [2, 3]),
    ]),
    S("religion", "Ιερά στις κορυφές και παιχνίδια με ταύρους", "Peak sanctuaries and games with bulls", [
      P("Οι Μινωίτες λάτρευαν τους θεούς τους σε σπηλιές, σε ιερά πάνω σε κορυφές βουνών και μέσα στα ανάκτορα. Τα σύμβολά τους ήταν ο διπλός πέλεκυς και τα «κέρατα καθοσιώσεως», ένα σχήμα σαν κέρατα ταύρου. Στην τέχνη τους κυριαρχούν οι γυναικείες μορφές. Τα περίφημα πήλινα ειδώλια από φαγεντιανή της Κνωσού, γύρω στο 1600 π.Χ., δείχνουν γυναίκες που κρατούν φίδια, και ο Έβανς τα ονόμασε «θεές των φιδιών».",
        "The Minoans worshipped their gods in caves, in sanctuaries on mountain peaks and inside the palaces. Their symbols were the double axe and the so-called 'horns of consecration', a shape like a bull's horns. Female figures dominate their art, and many scholars think a goddess or goddesses held the central place in their religion. The famous faience figurines from Knossos, of about 1600 BC, found by Evans in 1903 in the stone-lined 'Temple Repositories', show women holding snakes, and Evans named them 'snake goddesses'. Both are incomplete and were heavily restored; whether they are goddesses or priestesses is uncertain. Several ivory 'snake goddesses' in foreign museums, which appeared on the art market after Evans's finds, are suspected or known to be modern forgeries.", [3, 4]),
      P("Το πιο γνωστό μινωικό θέαμα είναι τα ταυροκαθάψια. Σε τοιχογραφίες, σφραγίδες και αγαλματίδια βλέπουμε νέους και νέες να πιάνουν έναν ταύρο από τα κέρατα και να κάνουν τούμπα πάνω από την πλάτη του. Δεν ξέρουμε αν ήταν άθλημα, θρησκευτική τελετή ή και τα δύο. Πολλοί πιστεύουν ότι η ανάμνηση αυτών των παιχνιδιών, μαζί με τους λαβύρινθους διαδρόμους της Κνωσού, γέννησε τον μύθο του Μινώταυρου.",
        "The best-known Minoan spectacle is bull-leaping. In frescoes, seals and figurines we see young men and women seize a bull by the horns and somersault over its back; the 'Toreador Fresco' from Knossos shows three figures around one charging bull. We do not know whether it was a sport, a religious ritual or both, and modern bullfighting experts have doubted whether the leap as shown is even possible. Many believe that the memory of these games, together with the maze-like corridors of Knossos, gave rise to the myth of the Minotaur, the bull-man kept in the Labyrinth and fed with Athenian youths until Theseus killed him.", [3, 5]),
    ]),
    S("end", "Το τέλος της μινωικής Κρήτης", "The end of Minoan Crete", [
      P("Γύρω στο 1450 π.Χ. τα περισσότερα μινωικά κέντρα καταστράφηκαν. Μόνο η Κνωσός συνέχισε να λειτουργεί, αλλά τώρα οι πινακίδες της είναι γραμμένες στα ελληνικά, σε Γραμμική Β. Αυτό δείχνει ότι Έλληνες από την ηπειρωτική χώρα είχαν πάρει την εξουσία. Η έκρηξη της Θήρας, που έγινε πολύ νωρίτερα, μάλλον αποδυνάμωσε την Κρήτη, αλλά δεν ήταν η μόνη αιτία της παρακμής. Οι νέοι άρχοντες κράτησαν πολλά από τη μινωική κουλτούρα: την τέχνη, τη γραφή και ίσως μέρος της θρησκείας.",
        "Around 1450 BC most Minoan centres were destroyed. Only Knossos went on functioning, but now its tablets are written in Greek, in Linear B. This shows that Greeks from the mainland had taken power, whether by conquest or by dynastic takeover. The Thera eruption, which happened considerably earlier, probably weakened Crete (through tsunamis, ash fall and damage to its fleet and trade), but it was not the sole cause of decline, as Marinatos had argued. The new rulers kept much of Minoan culture: its art, its script adapted for Greek, and perhaps part of its religion. Burial customs changed too, and painted clay coffins (larnakes) like the one in the picture became common in Late Minoan Crete.", [2, 6]),
    ]),
  ],
  grammar=[
    G("B1+", "λέγεται ότι, φαίνεται ότι: reporting and inferring", "Απρόσωπες εκφράσεις: «φαίνεται ότι», «πιστεύεται ότι»",
      "When the evidence is uncertain, history writing distances itself with impersonal verbs: φαίνεται ότι 'it seems that', λέγεται ότι 'it is said that', πιστεύεται ότι 'it is believed that', θεωρείται 'is considered'. With πιθανότατα / μάλλον the writer gives a personal estimate.",
      [("Φαίνεται ότι οι σεισμοί προειδοποίησαν τους κατοίκους.", "It seems that the earthquakes warned the inhabitants."),
       ("Πιθανότατα ο στόλος ήταν η κύρια άμυνα.", "The fleet was most probably the main defence.")]),
    G("B1+", "να after verbs of perception and ability", "«Να» μετά από ρήματα αντίληψης",
      "After βλέπω, ακούω, συνεχίζω, αρχίζω, μπορώ, Greek uses να + verb where English uses an -ing form or an infinitive: βλέπουμε νέους να πιάνουν έναν ταύρο 'we see young men seizing a bull'; συνέχισε να λειτουργεί 'it continued to function'.",
      [("Βλέπουμε νέους και νέες να πιάνουν έναν ταύρο από τα κέρατα.", "We see young men and women grabbing a bull by the horns."),
       ("Μόνο η Κνωσός συνέχισε να λειτουργεί.", "Only Knossos continued to function.")]),
  ],
  terms=[
    T("η θαλασσοκρατορία", "thalassocracy, sea power", "Κυριαρχία ενός κράτους στη θάλασσα με τον στόλο του.", "Rule of the sea by a state's fleet."),
    T("τα κέρατα καθοσιώσεως", "horns of consecration", "Μινωικό ιερό σύμβολο σε σχήμα κεράτων ταύρου.", "A Minoan sacred symbol shaped like bull's horns."),
    T("η φαγεντιανή", "faience", "Υλικό από αλεσμένο χαλαζία με γυαλιστερή επιφάνεια.", "A glazed material of ground quartz."),
    T("τα ταυροκαθάψια", "bull-leaping", "Μινωικό θέαμα με άλματα πάνω από ταύρους.", "A Minoan spectacle of leaping over bulls."),
    T("η σφραγίδα", "seal", "Μικρή χαραγμένη πέτρα για να αφήνει αποτύπωμα σε πηλό.", "A small engraved stone for making impressions in clay."),
    T("η λάρνακα", "larnax, clay coffin", "Πήλινο φέρετρο σε σχήμα κιβωτίου ή μπανιέρας.", "A clay coffin shaped like a chest or bathtub."),
    T("η παρακμή", "decline", "Η σταδιακή πτώση μιας κοινωνίας ή ενός πολιτισμού.", "The gradual decline of a society or culture."),
  ],
  questions=[
    Q("Ποιος έδωσε το όνομα «μινωικός» στον πολιτισμό της Κρήτης;", ["Ο Άρθουρ Έβανς", "Ο Θουκυδίδης", "Ο Όμηρος", "Οι ίδιοι οι Μινωίτες"], 0, "After the mythical king Minos."),
    Q("Τι λείπει από τα μινωικά ανάκτορα;", ["Ισχυρά τείχη", "Αυλές", "Αποθήκες", "Σκάλες"], 0, "The fleet was probably the main defence."),
    Q("Τι πιστεύουν πολλοί για τον μύθο του Μινώταυρου;", ["Ότι γεννήθηκε από τα ταυροκαθάψια και τους διαδρόμους της Κνωσού", "Ότι είναι αιγυπτιακός", "Ότι τον επινόησε ο Έβανς", "Ότι είναι ιστορικό γεγονός"], 0, "Bull games plus a maze-like palace."),
    Q("Τι δείχνουν οι πινακίδες της Κνωσού μετά το 1450 π.Χ.;", ["Ότι την εξουσία είχαν πάρει Έλληνες", "Ότι η Κνωσός εγκαταλείφθηκε", "Ότι ήρθαν Αιγύπτιοι", "Ότι επέστρεψε η Γραμμική Α"], 0, "They are in Greek, in Linear B."),
  ],
  vocab=["δίνω", "μυθικός", "δύναμη", "αποκτώ", "κυριαρχώ", "παράξενος", "ισχυρός", "ρομαντικός", "ειρηνικός", "επιφυλακτικός", "ένδειξη", "βία", "λατρεύω", "κορυφή", "κυριαρχία", "φίδι", "θέαμα", "κέρατο", "πλάτη", "άθλημα", "διάδρομος", "λειτουργώ", "εξουσία", "αποδυναμώνω", "αιτία"],
  sources=[
    SRC("Thucydides, History of the Peloponnesian War 1.4 (Minos and the first navy)."),
    SRC("Fitton, J. L. (2002). Minoans. London: British Museum Press."),
    SRC("Marinatos, N. (1993). Minoan Religion: Ritual, Image, and Symbol. Columbia: University of South Carolina Press."),
    SRC("Lapatin, K. (2002). Mysteries of the Snake Goddess: Art, Desire, and the Forging of History. Boston: Houghton Mifflin."),
    SRC("Younger, J. G. (1995). “Bronze Age representations of Aegean bull-games, III”. Aegaeum 12: 507–545."),
    SRC("Driessen, J. & Macdonald, C. F. (1997). The Troubled Island: Minoan Crete before and after the Santorini Eruption. Aegaeum 17. Liège."),
  ]))
