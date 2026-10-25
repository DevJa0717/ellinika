import sys; sys.path.insert(0, '/tmp/claude-0/-home-user/0382d7bb-6b8c-530a-8ab0-98d2dee28f52/scratchpad/lit-src')
from util import *

def poem(i, fixes=()):
    d, ps = src(i)
    return fix("\n\n".join(ps), list(fixes))

ithaki = poem('l01', [("βρείς", "βρεις"), ("πρωϊά", "πρωιά"), ("\nΑλλο δεν", "\nΆλλο δεν"), ("\nΕτσι σοφός", "\nΈτσι σοφός")])
barb = poem('l02', [("μιά τέτοια", "μια τέτοια"), ("μιά κάποια", "μια κάποια"), ("οι δυό μας", "οι δυο μας")])
poli = poem('l03', [("εδώ,\nπού τόσα", "εδώ,\nπου τόσα"), ("Έτσι πού τη", "Έτσι που τη")])
therm = poem('l05', [("πώς ο Εφιάλτης", "πως ο Εφιάλτης")])
antonios = poem('l04', [("σου πού ενδίδει", "σου που ενδίδει"), ("σου\nπού απέτυχαν", "σου\nπου απέτυχαν"), ("σου\nπού βγήκαν", "σου\nπου βγήκαν"),
                        ("Αλεξάνδρεια πού φεύγει", "Αλεξάνδρεια που φεύγει"), ("μην πεις πώς ήταν", "μην πεις πως ήταν"), ("όνειρο, πώς απατήθηκεν", "όνειρο, πως απατήθηκεν"),
                        ("σαν πού ταιριάζει σε πού αξιώθηκες", "σαν που ταιριάζει σε που αξιώθηκες"), ("Αλεξάνδρεια πού χάνεις", "Αλεξάνδρεια που χάνεις")])
for t in (poli, antonios, therm): assert "πού" not in t.replace("πούνε", ""), t

_, poli_poly = src('l03', mono=False)

blocks = [
 {"type": "text", "text":
  "Konstantinos Kavafis (C. P. Cavafy, 1863–1933) is the Greek poet the world reads, and the one Greeks quote in arguments. His language is a deliberate blend: a **demotic base** with **katharevousa forms** dropped in where they add irony, distance or an official, Byzantine-Alexandrian tone. Watch for: -ις nouns (*σκέψις, συγκίνησις, λύσις, πόλις*), learned verbs and participles (*σηκώθη, κινούντες, ομιλούντες*), the old accusative plural of 3rd-declension nouns (*τους Λαιστρυγόνας, λιμένας*), the Constantinopolitan *σε* for *σου* as indirect object (*να σε δώσει*), *τες* for *τις*, and the poet's own spellings (*καλλίτερα, θάβρεις, νάναι*).\n\n"
  "Five poems, each complete. Read each aloud once before looking at the gloss: Cavafy's rhythm is close to prose, and the meaning often hides in a single unexpected word (*μια **κάποια** λύσις*, *πάλ' εις **μικρόν** γενναίοι*). Line breaks are part of the poem; stanzas are separated by a blank line. Poems published polytonically are given in monotonic, with Cavafy's spellings kept and *ποῦ* (= *που*) and *πῶς* (= *πως*) normalised.\n\n"
  "*Πηγή: Κωνσταντίνος Π. Καβάφης, Ιθάκη (1911), Περιμένοντας τους βαρβάρους (1904), Η πόλις (1910), Θερμοπύλες (1903), Απολείπειν ο θεός Αντώνιον (1911); public domain, Greek Wikisource.*"},
 {"type": "reading", "title": "Ιθάκη", "text": ithaki,
  "en": "As you set out on the journey to Ithaca,\npray that the road be long,\nfull of adventures, full of knowledge.\nThe Laestrygonians and the Cyclopes,\nangry Poseidon, do not fear them:\nyou will never find such things on your way\nif your thought stays lofty, if a rare\nemotion touches your spirit and your body.\nThe Laestrygonians and the Cyclopes,\nfierce Poseidon, you will not meet\nunless you carry them within your soul,\nunless your soul raises them up before you.\n\n"
        "Pray that the road be long.\nMay there be many summer mornings\nwhen, with what pleasure, what joy,\nyou enter harbours seen for the first time;\nmay you stop at Phoenician trading posts\nand buy fine wares,\nmother-of-pearl and coral, amber and ebony,\nand sensual perfumes of every kind,\nas many sensual perfumes as you can;\nmay you go to many Egyptian cities\nto learn and learn again from the learned.\n\n"
        "Always keep Ithaca in your mind.\nTo arrive there is your destination.\nBut do not hurry the journey at all.\nBetter that it last many years,\nand that you anchor at the island old at last,\nrich with all you have gained on the way,\nnot expecting Ithaca to give you riches.\n\n"
        "Ithaca gave you the beautiful journey.\nWithout her you would not have set out.\nShe has nothing more to give you.\n\n"
        "And if you find her poor, Ithaca has not deceived you.\nWise as you have become, with so much experience,\nyou will have understood by now what Ithacas mean.",
  "gloss": {"πηγαιμό": "πηγαιμός — the going, outward journey", "Λαιστρυγόνας": "Λαιστρυγόνες — Laestrygonians, cannibal giants of the Odyssey (old acc. pl.)", "Κύκλωπας": "Κύκλωπες — Cyclopes (old acc. pl.)", "σκέψις": "σκέψη — thought (learned -ις form)", "εκλεκτή": "εκλεκτός — choice, rare, refined", "συγκίνησις": "συγκίνηση — emotion", "κουβανείς": "κουβαλάς — you carry (popular form)", "πρωιά": "πρωινό — morning (pl.)", "λιμένας": "λιμάνι — harbour (acc. pl. of learned λιμήν)", "πρωτοειδωμένους": "πρωτοειδωμένος — seen for the first time", "εμπορεία": "εμπορείο — trading post", "πραγμάτειες": "πραμάτεια — wares, merchandise", "σεντέφια": "σεντέφι — mother-of-pearl", "κεχριμπάρια": "κεχριμπάρι — amber", "ηδονικά": "ηδονικός — sensual", "φθάσιμον": "φτάσιμο — arriving, arrival (learned -ον)", "αράξεις": "αράζω — to anchor, moor", "προσδοκώντας": "προσδοκώ — expecting (learned verb)", "πτωχική": "φτωχικός — poor, humble", "γέλασε": "γελώ — (+ acc.) to deceive"},
  "questions": [
   q("Πότε, κατά το ποίημα, δεν θα συναντήσεις Λαιστρυγόνες και Κύκλωπες;", "Αν δεν τους κουβαλάς μέσα στην ψυχή σου", ["Αν ταξιδέψεις γρήγορα", "Αν αποφύγεις τις Αιγυπτιακές πόλεις", "Αν προσευχηθείς στον Ποσειδώνα"], "«αν δεν τους κουβανείς μες στην ψυχή σου»: the monsters are inner fears."),
   q("Ποιο είναι το πραγματικό δώρο της Ιθάκης;", "Το ίδιο το ταξίδι", ["Τα πλούτη που σε περιμένουν εκεί", "Η επιστροφή στην πατρίδα", "Η φήμη του ταξιδιώτη"], "«Η Ιθάκη σ' έδωσε το ωραίο ταξίδι»."),
   q("Τι δείχνει ο πληθυντικός «οι Ιθάκες» στον τελευταίο στίχο;", "Ότι η Ιθάκη είναι σύμβολο για κάθε μεγάλο στόχο ζωής", ["Ότι υπάρχουν πολλά νησιά με αυτό το όνομα", "Ότι ο ταξιδιώτης έχασε τον δρόμο του", "Ότι ο Οδυσσέας επέστρεψε πολλές φορές"], "The plural turns a place into a concept."),
  ]},
 {"type": "reading", "title": "Περιμένοντας τους βαρβάρους", "text": barb,
  "en": "— What are we waiting for, assembled in the marketplace?\nThe barbarians are due to arrive today.\n\n— Why such inaction in the Senate?\nWhy do the senators sit there without making laws?\n\n— Because the barbarians will arrive today.\nWhat laws should the senators make now?\nWhen the barbarians come they will make the laws.\n\n"
        "— Why did our emperor get up so early,\nand sit at the city's greatest gate\non the throne, in state, wearing the crown?\n\n— Because the barbarians will arrive today.\nAnd the emperor is waiting to receive\ntheir leader. He has even prepared\na parchment to give him. On it\nhe has written him many titles and names.\n\n"
        "— Why did our two consuls and the praetors go out\ntoday in their red, embroidered togas;\nwhy did they put on bracelets with so many amethysts,\nand rings with brilliant, glittering emeralds;\nwhy are they carrying precious canes today,\nsuperbly worked in silver and gold?\n\nBecause the barbarians will arrive today;\nand such things dazzle the barbarians.\n\n"
        "— Why don't our worthy orators come as always\nto deliver their speeches, to have their say?\n\nBecause the barbarians will arrive today;\nand they are bored by eloquence and public speeches.\n\n"
        "— Why this sudden restlessness\nand confusion? (How serious the faces have become.)\nWhy are the streets and squares emptying so fast,\nand everyone going home deep in thought?\n\nBecause night has fallen and the barbarians have not come.\nAnd some people have arrived from the border\nand said there are no barbarians any more.\n\nAnd now what will become of us without barbarians?\nThose people were a kind of solution.",
  "gloss": {"συναθροισμένοι": "συναθροίζομαι — assembled, gathered", "Σύγκλητο": "Σύγκλητος — the Senate", "απραξία": "απραξία — inaction", "Συγκλητικοί": "συγκλητικός — senator", "νομοθετούνε": "νομοθετώ — to legislate", "αυτοκράτωρ": "αυτοκράτορας — emperor (learned nom.)", "σηκώθη": "σηκώθηκε — got up (learned aorist)", "πόλεως": "πόλη — city (learned gen.)", "περγαμηνή": "περγαμηνή — parchment", "ύπατοι": "ύπατος — consul", "πραίτορες": "πραίτορας — praetor", "σμαράγδια": "σμαράγδι — emerald", "μαλάματα": "μάλαμα — gold (popular, poetic)", "έκτακτα": "έκτακτα — exceptionally, superbly", "θαμπόνουν": "θαμπώνω — to dazzle", "ευφράδειες": "ευφράδεια — eloquence", "δημηγορίες": "δημηγορία — public speech, harangue", "σύγχυσις": "σύγχυση — confusion", "γένουμε": "γίνουμε — become (θα γένουμε = what will become of us)", "λύσις": "λύση — solution"},
  "questions": [
   q("Γιατί η Σύγκλητος δεν νομοθετεί;", "Επειδή θα νομοθετήσουν οι βάρβαροι όταν έρθουν", ["Επειδή ο αυτοκράτορας το απαγόρευσε", "Επειδή οι συγκλητικοί είναι άρρωστοι", "Επειδή δεν υπάρχουν πια νόμοι για ψήφιση"], "«Οι βάρβαροι σαν έλθουν θα νομοθετήσουν»."),
   q("Γιατί τελικά οι πολίτες απογοητεύονται που δεν ήρθαν οι βάρβαροι;", "Η αναμονή τους έδινε σκοπό και δικαιολογία για την αδράνεια", ["Ήθελαν να τους νικήσουν στη μάχη", "Είχαν πληρώσει για τα δώρα του αρχηγού τους", "Οι βάρβαροι θα έφερναν εμπόριο και πλούτο"], "«Οι άνθρωποι αυτοί ήσαν μια κάποια λύσις»: the enemy as an excuse."),
   q("Γιατί δεν έρχονται οι ρήτορες;", "Επειδή οι βάρβαροι βαριούνται τους λόγους", ["Επειδή φοβούνται τους βαρβάρους", "Επειδή δεν τους κάλεσε ο αυτοκράτορας", "Επειδή έχασαν τη φωνή τους"], "«κι αυτοί βαριούντ' ευφράδειες και δημηγορίες»."),
  ]},
 {"type": "reading", "title": "Η πόλις", "text": poli,
  "en": "You said: 'I'll go to another land, I'll go to another sea.\nAnother city will be found, better than this one.\nEvery effort of mine is a condemnation written in advance;\nand my heart is, like a corpse, buried.\nHow long will my mind stay in this decay?\nWherever I turn my eye, wherever I look,\nI see the black ruins of my life here,\nwhere I spent so many years, and wasted and ruined them.'\n\n"
        "You will not find new places, you will not find other seas.\nThe city will follow you. You will walk the same\nstreets. And in the same neighbourhoods you will grow old;\nand in these same houses you will turn grey.\nYou will always arrive in this city. For elsewhere (do not hope)\nthere is no ship for you, there is no road.\nJust as you have wasted your life here\nin this small corner, you have ruined it in the whole world.",
  "gloss": {"πάγω": "πηγαίνω — I go (old popular form = πάω)", "γη": "γη — land, earth", "πόλις": "πόλη — city (learned form)", "καλλίτερη": "καλύτερη — better (Cavafy's spelling)", "καταδίκη": "καταδίκη — condemnation, sentence", "γραφτή": "γραφτός — written; destined", "θαμένη": "θαμμένος — buried", "μαρασμόν": "μαρασμός — decay, withering", "ερείπια": "ερείπιο — ruin", "ρήμαξα": "ρημάζω — to lay waste, ruin", "χάλασα": "χαλώ — to spoil, ruin", "θάβρεις": "θα βρεις — you will find", "γερνάς": "γερνώ — to grow old", "ασπρίζεις": "ασπρίζω — to turn white, go grey", "πόλι": "πόλη — city (acc., Cavafy's spelling)", "αλλού": "τα αλλού — 'the elsewheres', other places", "οδό": "οδός — road, way (learned)", "κώχη": "κόχη — corner, nook"},
  "questions": [
   q("Τι απαντά η δεύτερη φωνή στο σχέδιο φυγής;", "Ότι το πρόβλημα είναι μέσα του και θα τον ακολουθεί παντού", ["Ότι η καινούργια πόλη θα είναι πράγματι καλύτερη", "Ότι πρέπει να φύγει με πλοίο το συντομότερο", "Ότι η πόλη θα αλλάξει αν περιμένει"], "«Η πόλις θα σε ακολουθεί… σ' όλην την γη την χάλασες»."),
   q("Ποιο ρήμα δείχνει ότι ο ίδιος κατέστρεψε τη ζωή του;", "ρήμαξα", ["βρεθεί", "ακολουθεί", "ελπίζεις"], "«πέρασα και ρήμαξα και χάλασα»: he is the agent."),
  ]},
 {"type": "reading", "title": "Θερμοπύλες", "text": therm,
  "en": "Honour to those who in their lives\nhave taken up and guard their Thermopylae.\nNever stirring from duty;\njust and upright in all their deeds,\nbut with pity, too, and compassion;\ngenerous whenever they are rich, and when\nthey are poor, still generous in small things,\nstill helping as much as they can;\nalways speaking the truth,\nyet without hatred for those who lie.\n\n"
        "And even greater honour is their due\nwhen they foresee (and many do foresee)\nthat Ephialtes will appear in the end,\nand the Medes will get through after all.",
  "gloss": {"όπου": "όπου — who (Cavafy's relative = που)", "ζωή": "στην ζωή των — in their lives (των = τους)", "ώρισαν": "ορίζω — to define; to take up (a post) (old spelling)", "φυλάγουν": "φυλάγω — to guard", "χρέος": "χρέος — duty (also: debt)", "κινούντες": "κινώ — stirring, moving (learned participle = κινώντας)", "ίσιοι": "ίσιος — straight, upright", "ευσπλαχνία": "ευσπλαχνία — compassion, mercy", "οσάκις": "οσάκις — whenever (learned = όποτε)", "πτωχοί": "φτωχός — poor (learned spelling)", "μικρόν": "εις μικρόν — in a small way", "συντρέχοντες": "συντρέχω — helping, coming to the aid (participle)", "ομιλούντες": "ομιλώ — speaking (learned participle = μιλώντας)", "πλην": "πλην — but, except", "ψευδομένους": "ψεύδομαι — those who lie (participle)", "Εφιάλτης": "Εφιάλτης — Ephialtes, the traitor of 480 BC; also 'nightmare'", "Μήδοι": "Μήδοι — Medes = the Persians", "διαβούνε": "διαβαίνω — to pass through"},
  "questions": [
   q("Γιατί αξίζει σε αυτούς «περισσότερη τιμή»;", "Κάνουν το χρέος τους ενώ ξέρουν ότι στο τέλος θα προδοθούν", ["Επειδή στο τέλος πάντα νικούν", "Επειδή είναι πλούσιοι και γενναιόδωροι", "Επειδή δεν ξέρουν τι θα συμβεί"], "«όταν προβλέπουν… πως ο Εφιάλτης θα φανεί στο τέλος»: duty without illusions."),
   q("Πώς είναι γενναιόδωροι όταν είναι φτωχοί;", "Στο μέτρο των δυνάμεών τους, σε μικρά πράγματα", ["Καθόλου, γιατί δεν έχουν", "Δανείζονται για να δώσουν", "Δίνουν μόνο στους φίλους τους"], "«πάλ' εις μικρόν γενναίοι, πάλι συντρέχοντες όσο μπορούνε»."),
  ]},
 {"type": "reading", "title": "Απολείπειν ο θεός Αντώνιον", "text": antonios,
  "en": "When suddenly, at midnight, there is heard\nan invisible troupe passing by\nwith exquisite music, with voices,\ndo not mourn uselessly your fortune that is giving way now,\nyour works that failed, the plans of your life\nthat all turned out to be illusions.\nAs one long prepared, as one courageous,\nsay goodbye to her, to Alexandria who is leaving.\nAbove all do not fool yourself, do not say it was\na dream, that your ears deceived you;\ndo not stoop to such vain hopes.\nAs one long prepared, as one courageous,\nas befits you, who were granted such a city,\ngo firmly to the window\nand listen with emotion, but not\nwith the pleading and complaints of cowards,\nas a last delight, to the sounds,\nthe exquisite instruments of the mystic troupe,\nand say goodbye to her, to Alexandria whom you are losing.",
  "gloss": {"ακουσθεί": "ακούγομαι — to be heard (learned aor. subj. = ακουστεί)", "αόρατος": "αόρατος — invisible", "θίασος": "θίασος — troupe; Dionysus' procession", "εξαίσιες": "εξαίσιος — exquisite", "ενδίδει": "ενδίδω — to give way, yield", "απέτυχαν": "αποτυγχάνω — to fail", "πλάνες": "πλάνη — illusion, delusion", "ανοφέλετα": "ανώφελα — uselessly", "θρηνήσεις": "θρηνώ — to mourn, lament", "θαρραλέος": "θαρραλέος — courageous", "αποχαιρέτα": "αποχαιρετώ — say goodbye (imperative)", "γελασθείς": "γελιέμαι — to be fooled (learned = γελαστείς)", "απατήθηκεν": "απατώμαι — to be deceived", "ακοή": "ακοή — hearing", "μάταιες": "μάταιος — vain, futile", "καταδεχθείς": "καταδέχομαι — to stoop to, deign (= καταδεχτείς)", "αξιώθηκες": "αξιώνομαι — to be granted, deemed worthy", "δειλών": "δειλός — coward", "παρακάλια": "παρακάλια — pleading", "απόλαυσι": "απόλαυση — delight, enjoyment"},
  "questions": [
   q("Τι ζητά ο ποιητής από τον Αντώνιο;", "Να αποχαιρετήσει την Αλεξάνδρεια με αξιοπρέπεια, χωρίς αυταπάτες", ["Να πολεμήσει για να κρατήσει την πόλη", "Να ακολουθήσει τον θίασο έξω από την πόλη", "Να κλείσει το παράθυρο και να κοιμηθεί"], "«Σαν έτοιμος από καιρό, σα θαρραλέος, αποχαιρέτα την»."),
   q("Ποια «μάταιη ελπίδα» πρέπει να αποφύγει;", "Να πει ότι όλα ήταν ένα όνειρο", ["Να ελπίζει ότι θα γυρίσει ο θίασος", "Να πιστέψει ότι η μουσική είναι ωραία", "Να ζητήσει βοήθεια από τους φίλους του"], "«μην πεις πως ήταν ένα όνειρο, πως απατήθηκεν η ακοή σου»."),
  ]},
 {"type": "table", "title": "Cavafy's learned and poetic forms → standard Greek",
  "head": ["In the poems", "Standard modern", "What it is"],
  "rows": [
   ["σκέψις, συγκίνησις, λύσις, σύγχυσις", "σκέψη, συγκίνηση, λύση, σύγχυση", "learned -ις nouns"],
   ["πόλις / της πόλεως / την πόλι", "πόλη / της πόλης / την πόλη", "learned noun and genitive; Cavafy's -ι accusative"],
   ["ευχαρίστησι, απόλαυσι, συγκίνησιν", "ευχαρίστηση, απόλαυση, συγκίνηση", "-ι(ν) accusative of -ις nouns"],
   ["ο αυτοκράτωρ", "ο αυτοκράτορας", "learned nominative in -ωρ"],
   ["τους Λαιστρυγόνας, τους Κύκλωπας, λιμένας", "τους Λαιστρυγόνες, τους Κύκλωπες, λιμάνια", "ancient accusative plural -ας"],
   ["σηκώθη", "σηκώθηκε", "short learned aorist passive"],
   ["έλθουν, ήλθαν", "έρθουν, ήρθαν", "learned stem of έρχομαι"],
   ["ακουσθεί, γελασθείς, καταδεχθείς", "ακουστεί, γελαστείς, καταδεχτείς", "-σθ-/-χθ- passive stems"],
   ["κινούντες, ομιλούντες, συντρέχοντες", "κινώντας, μιλώντας, βοηθώντας", "declinable active participles"],
   ["ψευδομένους", "αυτούς που λένε ψέματα", "middle participle as noun"],
   ["οσάκις", "όποτε", "learned conjunction"],
   ["πλην", "αλλά, εκτός από", "learned conjunction / preposition"],
   ["όπου (Τιμή σ' εκείνους όπου…)", "που", "older relative"],
   ["στην ζωή των, σ' όλες των τες πράξεις", "στη ζωή τους, σε όλες τους τις πράξεις", "των = τους; τες = τις"],
   ["να σε δώσει, σ' έδωσε", "να σου δώσει, σου έδωσε", "Constantinopolitan accusative for the indirect object"],
   ["θα γένουμε", "θα γίνουμε", "popular variant"],
   ["πάγω", "πάω, πηγαίνω", "older popular form"],
   ["φθάνω, πτωχός, πτωχική", "φτάνω, φτωχός, φτωχική", "learned consonant clusters"],
   ["φθάσιμον", "φτάσιμο", "neuter with learned -ν"],
   ["καλλίτερα", "καλύτερα", "Cavafy's spelling (from κάλλος)"],
   ["νάναι, θάβγαινες, θάβρεις", "να 'ναι, θα 'βγαινες, θα βρεις", "elision written as one word"],
   ["μέν', βαριούντ', πάλ', μεσάνυχτ'", "μένει, βαριούνται, πάλι, μεσάνυχτα", "elided final vowel"],
   ["εις μικρόν", "σε μικρό βαθμό", "εις + accusative"],
   ["Απολείπειν ο θεός Αντώνιον", "Ο θεός εγκαταλείπει τον Αντώνιο", "Ancient Greek infinitive (Plutarch)"],
  ]},
 {"type": "culture", "title": "Ο Αλεξανδρινός",
  "text": "Cavafy spent almost his whole life in Alexandria, working as a clerk in the Irrigation Office and printing his poems on loose sheets for friends; the first real collection appeared only after his death. He divided his work into **philosophical, historical and sensual** poems, and the historical ones are mostly set not in classical Athens but in the Hellenistic and late-Roman world: diasporas, provincial courts, the end of empires.\n\n"
          "**Απολείπειν ο θεός Αντώνιον** comes from Plutarch's *Life of Antony*: the night before Alexandria fell to Octavian, people heard a Dionysian procession leaving the city, and took it as Antony's god abandoning him. **Θερμοπύλες** gave Greek the phrase *ο καθένας έχει τις Θερμοπύλες του* and made *Εφιάλτης* a byword for the traitor. **Περιμένοντας τους βαρβάρους** is the most quoted Greek poem in political commentary (*μια κάποια λύσις* = a convenient enemy or excuse) and gave J. M. Coetzee the title of a novel. **Ιθάκη** was read at Jacqueline Kennedy Onassis' funeral, and *η Ιθάκη μας* is everyday Greek for one's life goal.\n\n"
          "When Greeks discuss Cavafy they talk about his **ειρωνεία**, his **πεζολογία** (prosaic diction) and his **γλωσσική μίξη**. Critics long argued over whether this mixture was a flaw or a stroke of genius; today it reads like the voice of a Greek diaspora that has vanished."},
]

practice = [
 {"gen": "type", "items": [
  {"prompt": "Say in Greek: **destination**", "answer": "προορισμός", "accept": ["προορισμός", "ο προορισμός"]},
  {"prompt": "Say in Greek: **to anchor, moor**", "answer": "αράζω", "accept": ["αράζω"]},
  {"prompt": "Say in Greek: **inaction, idleness** (noun)", "answer": "απραξία", "accept": ["απραξία", "η απραξία", "αδράνεια"]},
  {"prompt": "Say in Greek: **to dazzle**", "answer": "θαμπώνω", "accept": ["θαμπώνω"]},
  {"prompt": "Say in Greek: **eloquence**", "answer": "ευφράδεια", "accept": ["ευφράδεια", "η ευφράδεια"]},
  {"prompt": "Say in Greek: **confusion**", "answer": "σύγχυση", "accept": ["σύγχυση", "η σύγχυση", "σύγχυσις"]},
  {"prompt": "Say in Greek: **decay, withering**", "answer": "μαρασμός", "accept": ["μαρασμός", "ο μαρασμός"]},
  {"prompt": "Say in Greek: **ruins**", "answer": "ερείπια", "accept": ["ερείπια", "τα ερείπια"]},
  {"prompt": "Say in Greek: **to lay waste, ruin**", "answer": "ρημάζω", "accept": ["ρημάζω"]},
  {"prompt": "Say in Greek: **duty** (Cavafy's word)", "answer": "χρέος", "accept": ["χρέος", "το χρέος"]},
  {"prompt": "Say in Greek: **compassion, mercy**", "answer": "ευσπλαχνία", "accept": ["ευσπλαχνία", "η ευσπλαχνία"]},
  {"prompt": "Say in Greek: **to give way, yield**", "answer": "ενδίδω", "accept": ["ενδίδω", "υποχωρώ"]},
  {"prompt": "Say in Greek: **illusion, delusion** (Cavafy's word)", "answer": "πλάνη", "accept": ["πλάνη", "η πλάνη"]},
  {"prompt": "Say in Greek: **courageous**", "answer": "θαρραλέος", "accept": ["θαρραλέος"]},
  {"prompt": "Say in Greek: **invisible**", "answer": "αόρατος", "accept": ["αόρατος"]},
 ]},
 {"gen": "mc", "items": [
  mc("Ένας αρθρογράφος γράφει ότι για την κυβέρνηση η κρίση ήταν «μια κάποια λύσις». Εννοεί ότι:", "η κρίση τής πρόσφερε βολική δικαιολογία", ["η κρίση λύθηκε οριστικά", "η κυβέρνηση βρήκε τεχνική λύση", "η κρίση ήταν μικρή και ασήμαντη"], "The barbarians' 'solution': a convenient enemy or excuse."),
  mc("«Κράτησε τις Θερμοπύλες του μέχρι τέλους.» Σημαίνει ότι:", "έμεινε πιστός στο καθήκον του ξέροντας ότι θα χάσει", ["κέρδισε μια δύσκολη μάχη", "πρόδωσε τους συντρόφους του", "έφυγε την τελευταία στιγμή"], "From Cavafy's Θερμοπύλες."),
  mc("Ο «Εφιάλτης» στα ελληνικά, εκτός από κακό όνειρο, σημαίνει και:", "τον προδότη", ["τον ήρωα", "τον βασιλιά των Περσών", "τον ποιητή"], "Ephialtes showed the Persians the path round Thermopylae."),
  mc("«Γενναίοι οσάκις είναι πλούσιοι.» Το «οσάκις» =", "όποτε", ["όσο", "όπως", "όπου"], "οσάκις (learned) = κάθε φορά που, όποτε."),
  mc("«Πλην χωρίς μίσος.» Το «πλην» εδώ =", "αλλά", ["επειδή", "επιπλέον", "ακόμη και"], "πλην = but (also 'except': πλην εμού = except me)."),
  mc("«Η Ιθάκη σ' έδωσε το ωραίο ταξίδι.» Στην κοινή νεοελληνική:", "Η Ιθάκη σού έδωσε το ωραίο ταξίδι.", ["Η Ιθάκη σε έδωσε στο ωραίο ταξίδι.", "Η Ιθάκη σε πήγε στο ωραίο ταξίδι.", "Η Ιθάκη σε έδωσε το ωραίο ταξίδι."], "Cavafy's accusative σε for the indirect object is Constantinopolitan; standard uses σου."),
  mc("Ο τίτλος «Απολείπειν ο θεός Αντώνιον» σημαίνει:", "Ο θεός εγκαταλείπει τον Αντώνιο", ["Ο Αντώνιος εγκαταλείπει τον θεό", "Ο θεός προστατεύει τον Αντώνιο", "Ο Αντώνιος λατρεύει τον θεό"], "απολείπω 'abandon'; Αντώνιον is the accusative object."),
  mc("«Δεν θα συναντήσεις… αν δεν τους κουβανείς μες στην ψυχή σου.» Το νόημα:", "Οι εχθροί που φοβάσαι είναι κυρίως μέσα σου", ["Πρέπει να αποφεύγεις τα επικίνδυνα ταξίδια", "Η ψυχή σου είναι αρκετά δυνατή για κάθε μάχη", "Οι μύθοι του Ομήρου δεν είναι αληθινοί"], "The Laestrygonians are inner fears."),
 ]},
]

d = {"el": "Καβάφης: πέντε ποιήματα", "title": "Reading Cavafy: Ithaca, the Barbarians, the City, Thermopylae, Antony", "section": "C1 · reading",
     "goal": "Read five of Cavafy's best-known poems in full, decode his mixed register, and use his famous lines the way Greeks do.",
     "blocks": blocks, "practice": practice}
write('c1-read-cavafy', d)
