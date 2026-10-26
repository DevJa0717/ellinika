# Era 3 · Γεωμετρική και Αρχαϊκή εποχή (περ. 1100–480 π.Χ.)
from common import P, S, G, T, Q, SRC

ERA = dict(id="archaic", el="Από τους «σκοτεινούς αιώνες» στην Αρχαϊκή εποχή", en="From the 'Dark Ages' to the Archaic period", dates="περ. 1100–480 π.Χ.", dates_en="c. 1100–480 BC", level="B2",
  intro_el="Μετά την πτώση των ανακτόρων, ο ελληνικός κόσμος ξαναφτιάχνεται από την αρχή. Τον 8ο αιώνα π.Χ. εμφανίζονται το αλφάβητο, τα ομηρικά έπη, οι πρώτοι Ολυμπιακοί αγώνες και η πόλη-κράτος. Ως τους Περσικούς πολέμους οι Έλληνες ιδρύουν αποικίες από τη Μαύρη Θάλασσα ως την Ισπανία και θέτουν τα θεμέλια της φιλοσοφίας, της τέχνης και της πολιτικής.",
  intro_en="After the fall of the palaces the Greek world rebuilt itself almost from scratch. The four centuries once called the 'Dark Ages' were poorer and less literate, but they were not empty, and in the eighth century BC the alphabet, the Homeric epics, the first Olympic games and the city-state all appear within a few generations. By the Persian Wars, Greeks had founded colonies from the Black Sea to Spain and laid the foundations of philosophy, monumental sculpture and political reform. From this part on the Greek is a steady B2, with longer sentences, more abstract vocabulary and the conditional and result clauses typical of history writing.")

CH = []

# 3.1 language
CH.append(dict(id="e3-alphabet", theme="language", el="Το αλφάβητο: ένα δάνειο που άλλαξε τον κόσμο", title="The alphabet: a loan that changed the world", dates="8ος–5ος αιώνας π.Χ.",
  image="nearchos",
  summary_en="How the Greeks borrowed the Phoenician consonant script, invented letters for vowels, used dozens of local alphabets, and passed their own on to the Etruscans and Romans.",
  sections=[
    S("loan", "Τα «φοινικήια γράμματα»", "The 'Phoenician letters'", [
      P("Ύστερα από τέσσερις αιώνες χωρίς γραφή, οι Έλληνες άρχισαν ξανά να γράφουν τον 8ο αιώνα π.Χ. Αυτή τη φορά όμως δεν ξαναβρήκαν τη Γραμμική Β, που είχε ξεχαστεί εντελώς. Δανείστηκαν τη γραφή των Φοινίκων, ενός λαού εμπόρων από τις ακτές του σημερινού Λιβάνου, με τους οποίους συναντιόνταν στα λιμάνια της ανατολικής Μεσογείου. Ο Ηρόδοτος, τον 5ο αιώνα π.Χ., ονομάζει ακόμα τα γράμματα «φοινικήια», και τα ονόματα των γραμμάτων προδίδουν την προέλευσή τους: το άλφα, το βήτα και το γάμμα αντιστοιχούν στα φοινικικά άλεφ, μπεθ και γκίμελ.",
        "After four centuries without writing, the Greeks began to write again in the eighth century BC (a few scholars argue for the ninth). This time, however, they did not rediscover Linear B, which had been completely forgotten. They borrowed the script of the Phoenicians, a trading people from the coast of modern Lebanon, whom they met in the ports of the eastern Mediterranean, perhaps at places like Al Mina in Syria or in Cyprus and Crete. Herodotus, in the fifth century BC, still calls the letters phoinikēia (5.58) and tells the legend that Cadmus brought them to Thebes. The names of the letters betray their origin: alpha, beta and gamma correspond to Phoenician aleph ('ox'), beth ('house') and gimel, names that mean something in Phoenician but nothing in Greek.", [1, 2]),
      P("Η φοινικική γραφή είχε όμως ένα μειονέκτημα: έγραφε μόνο σύμφωνα. Για μια σημιτική γλώσσα αυτό ήταν αρκετό, γιατί ο αναγνώστης μπορούσε να μαντέψει τα φωνήεντα από τα συμφραζόμενα. Για τα ελληνικά, όπου μια λέξη μπορεί να αρχίζει ή να τελειώνει σε φωνήεν, ήταν ανεπαρκής. Έτσι οι Έλληνες χρησιμοποίησαν μερικά φοινικικά σύμφωνα που δεν χρειάζονταν, για να γράψουν φωνήεντα: από το άλεφ έγινε το Α, από το χε το Ε, από το γιοντ το Ι και από το άγιν το Ο. Πρόσθεσαν αργότερα και νέα γράμματα, όπως το Φ, το Χ, το Ψ και το Ω.",
        "The Phoenician script had one drawback, though: it wrote only consonants. For a Semitic language that was enough, because the reader could guess the vowels from the context and from the consonantal root. For Greek, where a word can begin or end in a vowel and vowels distinguish grammatical forms, it was inadequate. So the Greeks used a few Phoenician consonant signs they did not need to write vowels: aleph (a glottal stop) became A, he became E, yod became I, and ayin (a throat sound) became O; waw gave both the early letter digamma (Ϝ, for the sound w) and, in another form, Υ. Later they added new letters such as Φ, Χ, Ψ and Ω (Ω, 'big O', first in Ionia). Whether this was a single deliberate invention or a gradual process is debated, but the result was the first full alphabet, with signs for both consonants and vowels.", [1, 3]),
    ]),
    S("first", "Οι πρώτες επιγραφές", "The first inscriptions", [
      P("Οι παλαιότερες ελληνικές επιγραφές με το αλφάβητο είναι από τα μέσα του 8ου αιώνα π.Χ. και, παραδόξως, δεν είναι διοικητικά κείμενα, όπως οι πινακίδες της Γραμμικής Β, αλλά στίχοι. Σε μια οινοχόη από την Αθήνα, γύρω στο 740 π.Χ., κάποιος χάραξε έναν εξάμετρο στίχο: ότι το δοχείο θα το πάρει ο χορευτής που χορεύει πιο ζωηρά από όλους. Σε ένα κύπελλο από την Πιθηκούσσα, το σημερινό Ίσκια, κοντά στη Νάπολη, μια επιγραφή αστειεύεται ότι όποιος πιει από αυτό θα κυριευτεί από τον πόθο της Αφροδίτης, και το παρομοιάζει με το περίφημο ποτήρι του Νέστορα στην «Ιλιάδα».",
        "The oldest Greek alphabetic inscriptions date from the mid-eighth century BC and, surprisingly, they are not administrative texts like the Linear B tablets, but verse. On a wine jug (oinochoe) from the Dipylon cemetery in Athens, around 740 BC, someone scratched a hexameter line: that the jug will go to the dancer who dances most friskily of all. On a cup from Pithekoussai, modern Ischia near Naples, the earliest Greek settlement in Italy, an inscription of about 740–720 BC jokes that it is 'Nestor's cup, good to drink from', and that whoever drinks from it will be seized by desire for fair-crowned Aphrodite, a playful allusion to the famous cup of Nestor in the Iliad (11.632–637). Some scholars have even suggested that the alphabet was adapted precisely to record poetry with its metre, though this remains a hypothesis.", [3, 4]),
      P("Στην αρχή δεν υπήρχε ένα αλφάβητο για όλους τους Έλληνες. Κάθε περιοχή είχε τη δική της παραλλαγή, με διαφορετικά σχήματα και αξίες για μερικά γράμματα. Οι επιγραφές γράφονταν άλλοτε από τα δεξιά προς τα αριστερά, όπως η φοινικική, και άλλοτε «βουστροφηδόν», δηλαδή μια σειρά προς τα δεξιά και την επόμενη προς τα αριστερά, όπως οργώνει ένα βόδι το χωράφι. Οι αγγειογράφοι, όπως ο Νέαρχος, άρχισαν να υπογράφουν τα έργα τους, και πάνω στα αγγεία γράφονταν τα ονόματα των μορφών.",
        "At first there was no single alphabet for all Greeks. Each region had its own variant ('epichoric' alphabets), with different shapes and values for some letters; in Euboea and the west, for example, Χ stood for the sound ks, while in Ionia it stood for kh. Inscriptions were written sometimes from right to left, like Phoenician, and sometimes boustrophedon, 'as the ox turns', one line to the right and the next to the left, the way an ox ploughs a field; left-to-right became the norm only in the course of the sixth and fifth centuries. Vase painters such as Nearchos, whose aryballos is in the picture, began to sign their works ('Nearchos made me'), and the names of the figures were written on the vases, which makes Attic pottery a rich source for early spelling.", [3, 5]),
    ]),
    S("legacy", "Από την Κύμη στη Ρώμη", "From Cumae to Rome", [
      P("Το αλφάβητο ταξίδεψε μαζί με τους Έλληνες αποίκους. Η παραλλαγή της Εύβοιας, που χρησιμοποιούσαν οι άποικοι της Κύμης στην Ιταλία, πέρασε στους Ετρούσκους και από αυτούς στους Ρωμαίους. Γι' αυτό το λατινικό αλφάβητο, και επομένως αυτό που χρησιμοποιεί σήμερα η μισή ανθρωπότητα, κατάγεται τελικά από ένα ελληνικό. Πολύ αργότερα, τον 9ο αιώνα μ.Χ., από το ελληνικό αλφάβητο θα γεννηθούν και οι γραφές των Σλάβων.",
        "The alphabet travelled with the Greek colonists. The Euboean variant used by the colonists of Cumae in Italy (founded from Pithekoussai) passed to the Etruscans, and from them to the Romans. That is why the Latin alphabet, and therefore the one used today by about half of humanity, ultimately descends from a Greek one; it also explains why Latin X has the Euboean value ks and why Latin C and G go back to Greek gamma. Much later, in the ninth century AD, the scripts of the Slavs, Glagolitic and then Cyrillic, would also be born from the Greek alphabet, as a later chapter shows.", [2, 3]),
      P("Η Αθήνα κράτησε για πολύ καιρό το δικό της, παλιό αλφάβητο. Μόλις το 403/402 π.Χ. η πόλη αποφάσισε επίσημα να χρησιμοποιεί το ιωνικό αλφάβητο της Μιλήτου, με 24 γράμματα, το ίδιο που διδάσκεται σήμερα στα ελληνικά σχολεία. Από τότε το ιωνικό αλφάβητο επικράτησε σε όλο τον ελληνικό κόσμο. Τα πεζά γράμματα, οι τόνοι και τα πνεύματα ήρθαν πολύ αργότερα.",
        "Athens kept its own old alphabet for a long time; in it, for example, Ε stood for both short e and long ē, and Η was still the sign for the h sound. Only in 403/402 BC, in the archonship of Eukleides, after the restoration of democracy, did the city officially decide to use the Ionic alphabet of Miletus, with 24 letters, the same one taught in Greek schools today. From then on the Ionic alphabet prevailed throughout the Greek world, and the other local alphabets died out within a century. Lower-case letters (minuscule, from the ninth century AD), accents and breathings (from about 200 BC, as the chapter on the Hellenistic Koine explains) came much later.", [3, 6]),
    ]),
  ],
  grammar=[
    G("B2", "Learned prepositions with the genitive: κατά, μετά, υπέρ", "«Κατά» με αιτιατική και γενική",
      "κατά has two uses. With the accusative it means 'during, around, according to': κατά τον Ηρόδοτο 'according to Herodotus', κατά τον 8ο αιώνα 'during the 8th century'. With the genitive (learned) it means 'against': κατά των Περσών 'against the Persians'. Fixed phrases keep old forms: κατ' αρχάς 'at first', κατ' εξοχήν 'par excellence'.",
      [("Κατά τον Ηρόδοτο, ο Κάδμος έφερε τα γράμματα στη Θήβα.", "According to Herodotus, Cadmus brought the letters to Thebes."),
       ("ένας πόλεμος κατά των Περσών", "a war against the Persians")]),
    G("B2", "Causal clauses: γιατί, επειδή, αφού, καθώς", "Αιτιολογικές προτάσεις",
      "γιατί and επειδή give a reason (επειδή can come first in the sentence, γιατί normally not). αφού 'since' presents the reason as already known; καθώς 'as, since' is more formal. Remember αφού also means 'after' with a past tense in narrative.",
      [("Για τα ελληνικά ήταν ανεπαρκής, αφού μια λέξη μπορεί να αρχίζει σε φωνήεν.", "For Greek it was inadequate, since a word can begin with a vowel."),
       ("Επειδή έγραφε μόνο σύμφωνα, οι Έλληνες πρόσθεσαν φωνήεντα.", "Because it wrote only consonants, the Greeks added vowels.")]),
  ],
  terms=[
    T("το αλφάβητο", "alphabet", "Γραφή με ξεχωριστά γράμματα για σύμφωνα και φωνήεντα.", "A script with separate letters for consonants and vowels."),
    T("η επιγραφή", "inscription", "Κείμενο χαραγμένο σε πέτρα, μέταλλο ή πηλό.", "A text cut into stone, metal or clay."),
    T("τα συμφραζόμενα", "context", "Οι λέξεις γύρω από μια λέξη, που βοηθούν να την καταλάβουμε.", "The surrounding words that help us understand one."),
    T("ο εξάμετρος", "hexameter", "Ο στίχος των επών, με έξι μέτρα.", "The six-foot verse line of epic poetry."),
    T("βουστροφηδόν", "boustrophedon", "Γραφή όπου κάθε σειρά αλλάζει κατεύθυνση, όπως οργώνει το βόδι.", "Writing in which each line changes direction, as an ox ploughs."),
    T("ο άποικος", "colonist, settler", "Αυτός που φεύγει από την πόλη του για να ιδρύσει νέα πόλη αλλού.", "One who leaves home to found a new city elsewhere."),
    T("επιχώριος", "local (epichoric)", "Που ανήκει σε έναν συγκεκριμένο τόπο.", "Belonging to one particular place."),
  ],
  questions=[
    Q("Από ποιον λαό δανείστηκαν οι Έλληνες τη γραφή τους;", ["Από τους Φοίνικες", "Από τους Αιγυπτίους", "Από τους Μινωίτες", "Από τους Ρωμαίους"], 0, "Herodotus calls the letters 'Phoenician'."),
    Q("Ποια ήταν η μεγάλη καινοτομία των Ελλήνων;", ["Τα γράμματα για τα φωνήεντα", "Η γραφή από δεξιά προς τα αριστερά", "Τα ιδεογράμματα", "Οι αριθμοί"], 0, "Phoenician wrote only consonants."),
    Q("Τι είναι οι πρώτες ελληνικές επιγραφές;", ["Κυρίως στίχοι", "Λογαριασμοί ανακτόρων", "Νόμοι", "Χάρτες"], 0, "The Dipylon jug and Nestor's cup."),
    Q("Πώς έφτασε το ελληνικό αλφάβητο στους Ρωμαίους;", ["Μέσω των Ετρούσκων, από την Κύμη", "Μέσω των Φοινίκων", "Μέσω της Αιγύπτου", "Απευθείας από την Αθήνα"], 0, "The Euboean variant of Cumae."),
  ],
  vocab=["δανείζομαι", "έμπορος", "συναντιέμαι", "προδίδω", "προέλευση", "αντιστοιχώ", "μειονέκτημα", "μαντεύω", "ανεπαρκής", "προσθέτω", "παραδόξως", "διοικητικός", "στίχος", "χαράζω", "δοχείο", "χορευτής", "ζωηρός", "κύπελλο", "αστειεύομαι", "πόθος", "παρομοιάζω", "παραλλαγή", "οργώνω", "χωράφι", "υπογράφω", "κατάγομαι", "επικρατώ"],
  sources=[
    SRC("Herodotus, Histories 5.58 (the Phoenician letters and Cadmus)."),
    SRC("Powell, B. B. (1991). Homer and the Origin of the Greek Alphabet. Cambridge University Press."),
    SRC("Jeffery, L. H. (1990). The Local Scripts of Archaic Greece. Rev. ed. with supplement by A. W. Johnston. Oxford: Clarendon Press."),
    SRC("“Nestor's Cup (Pithekoussai)” and “Dipylon inscription”, Wikipedia.", "https://en.wikipedia.org/wiki/Nestor%27s_Cup_(Pithekoussai)"),
    SRC("The Metropolitan Museum of Art, “Terracotta aryballos (oil flask), signed by Nearchos, ca. 570 BCE” (object record).", "https://www.metmuseum.org/art/collection/search/252451"),
    SRC("Threatte, L. (1980). The Grammar of Attic Inscriptions, vol. 1: Phonology. Berlin: de Gruyter (the Eukleidean reform of 403/2 BC)."),
  ]))

# 3.2 art
CH.append(dict(id="e3-kouroi", theme="art", el="Κούροι και κόρες: η γέννηση της μνημειακής γλυπτικής", title="Kouroi and korai: the birth of monumental sculpture", dates="περ. 650–480 π.Χ.",
  image="kouros",
  summary_en="The life-size marble youths and maidens of the Archaic period, their debt to Egypt, their famous smile, their lost colours, and how they were rediscovered under the Acropolis.",
  sections=[
    S("egypt", "Ένα μάθημα από την Αίγυπτο", "A lesson from Egypt", [
      P("Γύρω στα μέσα του 7ου αιώνα π.Χ. Έλληνες μισθοφόροι και έμποροι εγκαταστάθηκαν στην Αίγυπτο, όπου ο φαραώ τούς επέτρεψε να ιδρύσουν την πόλη Ναύκρατη στο Δέλτα του Νείλου. Εκεί είδαν για πρώτη φορά τεράστια πέτρινα αγάλματα και ναούς. Λίγο αργότερα εμφανίζονται στην Ελλάδα τα πρώτα μεγάλα μαρμάρινα αγάλματα: οι κούροι, γυμνοί νέοι άντρες σε όρθια στάση, με το αριστερό πόδι λίγο μπροστά, και οι κόρες, ντυμένες νέες γυναίκες.",
        "Around the middle of the seventh century BC Greek mercenaries and traders settled in Egypt, where the pharaoh Psammetichus I and his successors employed them; under Amasis they were allowed to base themselves at Naukratis in the Nile Delta. There they saw huge stone statues and temples, and learned how to quarry and carve hard stone on a large scale. Soon afterwards the first large marble statues appear in Greece: the kouroi, naked young men standing upright with the left foot slightly forward, and the korai, clothed young women. The pose of the kouros is clearly modelled on Egyptian standing statues, and the historian Diodorus even tells (1.98) that the Samian sculptors Telekles and Theodoros worked with an Egyptian system of proportions.", [1, 2]),
      P("Οι Έλληνες όμως δεν αντέγραψαν απλώς. Οι αιγυπτιακοί άντρες στέκονται ντυμένοι και στηρίζονται σε μια πέτρινη πλάκα πίσω τους. Οι ελληνικοί κούροι είναι γυμνοί και στέκονται ελεύθεροι. Ο κούρος της εικόνας, από την Αττική, γύρω στο 590–580 π.Χ., είναι ένα από τα παλαιότερα μαρμάρινα αγάλματα της Αθήνας και βρίσκεται σήμερα στη Νέα Υόρκη. Η στάση του είναι ακόμα άκαμπτη και το σώμα του είναι σχεδόν γεωμετρικό, αλλά μέσα σε έναν αιώνα οι γλύπτες θα μάθουν να αποδίδουν τους μυς, το βάρος και την κίνηση με εκπληκτική ακρίβεια.",
        "But the Greeks did not simply copy. Egyptian men stand clothed (at least in a kilt) and are supported by a stone back slab; the Greek kouroi are naked and stand free, an expression of a culture that celebrated the athletic male body. The kouros in the picture, from Attica, of about 590–580 BC, is one of the earliest marble statues from Athens and is now in the Metropolitan Museum in New York; its proportions follow a grid close to the Egyptian canon. Its stance is still rigid and its body almost geometric, with the kneecaps and ribcage drawn like patterns, but within a century sculptors would learn to render muscles, weight and movement with astonishing accuracy, as in the Kroisos kouros from Anavyssos (c. 530 BC) and the 'Kritios Boy' (c. 480 BC), which finally shifts its weight onto one leg.", [2, 3]),
    ]),
    S("smile", "Το «αρχαϊκό χαμόγελο» και τα χαμένα χρώματα", "The 'Archaic smile' and the lost colours", [
      P("Πολλά αρχαϊκά αγάλματα έχουν ένα παράξενο, ελαφρύ χαμόγελο, που οι ιστορικοί τέχνης ονομάζουν «αρχαϊκό χαμόγελο». Δεν σημαίνει απαραίτητα χαρά: χαμογελούν ακόμα και πολεμιστές που πεθαίνουν. Ίσως ήταν ένας τρόπος να δείξουν ότι η μορφή είναι ζωντανή, ή απλώς μια τεχνική λύση για να δοθεί σχήμα στο στόμα. Οι κούροι στέκονταν συχνά πάνω σε τάφους, ως μνημεία νεκρών, ή σε ιερά, ως αναθήματα στους θεούς.",
        "Many Archaic statues have a strange, slight smile, which art historians call the 'Archaic smile'. It does not necessarily mean joy: even dying warriors smile, as on the pediments of the temple of Aphaia on Aegina. Perhaps it was a way of showing that the figure is alive and in the favour of the gods, or simply a technical solution for giving shape to the mouth on a block-like head. Kouroi often stood on graves, as memorials to the dead, or in sanctuaries, as offerings to the gods. The base of the Kroisos kouros carries the epitaph: 'Stand and mourn at the monument of dead Kroisos, whom raging Ares destroyed one day as he fought in the front ranks.'", [3, 4]),
      P("Τα αγάλματα που βλέπουμε σήμερα λευκά ήταν κάποτε ζωγραφισμένα με έντονα χρώματα. Τα μαλλιά ήταν κόκκινα ή καφέ, τα μάτια είχαν χρώμα, και τα ρούχα των κορών είχαν πολύχρωμα σχέδια. Αυτό το ξέρουμε από τα ίχνη που σώζονται και από σύγχρονες επιστημονικές μεθόδους. Η εικόνα της «λευκής» αρχαίας τέχνης, που λάτρεψαν οι Ευρωπαίοι του 18ου και του 19ου αιώνα, είναι στην πραγματικότητα ένα λάθος.",
        "The statues we see as white today were once painted in strong colours. Hair was red or brown, eyes were coloured, and the korai's garments had multicoloured patterns of meanders, rosettes and animals. We know this from surviving traces and from modern scientific methods such as ultraviolet light, raking light and X-ray fluorescence; the reconstructions of Vinzenz Brinkmann's 'Gods in Color' exhibitions made this vivid to the public. The image of 'white' ancient art, adored by eighteenth- and nineteenth-century Europeans from Winckelmann onwards and built into Neoclassical architecture, is in fact a mistake, though how bright and how complete the painting was is still debated.", [4, 5]),
    ]),
    S("persians", "Οι κόρες κάτω από το χώμα της Ακρόπολης", "The korai under the soil of the Acropolis", [
      P("Το 480 π.Χ. οι Πέρσες κατέλαβαν την Αθήνα και κατέστρεψαν τα ιερά της Ακρόπολης. Όταν οι Αθηναίοι επέστρεψαν, έθαψαν τα σπασμένα αγάλματα μέσα σε λάκκους, για να ισοπεδώσουν τον βράχο και να χτίσουν από την αρχή. Η καταστροφή αυτή έσωσε, χωρίς να το θέλει κανείς, πολλά αριστουργήματα. Όταν τα έφεραν στο φως οι αρχαιολόγοι το 1886, πολλές κόρες είχαν ακόμα τα χρώματά τους.",
        "In 480 BC the Persians took Athens and destroyed the sanctuaries of the Acropolis (Herodotus 8.53). When the Athenians returned, they buried the broken statues in pits as fill to level the rock and build anew; archaeologists call this layer the 'Persian debris' (Perserschutt). This destruction unintentionally saved many masterpieces from later reuse and weathering. When archaeologists brought them to light in 1886, during the excavations of Panagiotis Kavvadias, many korai still had their colours. Today they stand in the Acropolis Museum. Because the burial gives a firm end date of 480 BC, the 'Persian debris' is also a key fixed point for dating Archaic Greek art.", [3, 6]),
    ]),
  ],
  grammar=[
    G("B2", "χωρίς να + subjunctive", "«Χωρίς να»: τρόπος και αντίθεση",
      "χωρίς να + subjunctive means 'without doing': χωρίς να το θέλει κανείς 'without anyone wanting it'. It is a whole clause, so it has its own verb and can have its own subject. With a noun use χωρίς + accusative: χωρίς γραφή 'without writing'.",
      [("Η καταστροφή έσωσε τα αγάλματα, χωρίς να το θέλει κανείς.", "The destruction saved the statues, without anyone intending it."),
       ("Οι Έλληνες δεν αντέγραψαν χωρίς να αλλάξουν τίποτα.", "The Greeks did not copy without changing anything.")]),
    G("B2", "Passive with να: για να δοθεί, για να χτιστεί", "Παθητική υποτακτική αορίστου",
      "The passive aorist subjunctive is formed from the passive aorist stem with -ώ endings: δόθηκε → να δοθεί, χτίστηκε → να χτιστεί, θάφτηκε → να θαφτεί. It is common after για να, πριν να/πριν, ώστε να.",
      [("μια τεχνική λύση για να δοθεί σχήμα στο στόμα", "a technical solution for giving shape to the mouth (lit. for shape to be given)"),
       ("για να χτιστεί ο νέος ναός", "for the new temple to be built")]),
  ],
  terms=[
    T("ο κούρος", "kouros", "Αρχαϊκό άγαλμα γυμνού νέου άντρα σε όρθια στάση.", "Archaic statue of a naked young man standing."),
    T("η κόρη", "kore", "Αρχαϊκό άγαλμα ντυμένης νέας γυναίκας.", "Archaic statue of a clothed young woman."),
    T("ο μισθοφόρος", "mercenary", "Στρατιώτης που πολεμά για χρήματα σε ξένο στρατό.", "A soldier who fights for pay in a foreign army."),
    T("άκαμπτος", "rigid", "Που δεν λυγίζει· σκληρός, χωρίς κίνηση.", "That does not bend; stiff."),
    T("η πολυχρωμία", "polychromy", "Η χρήση πολλών χρωμάτων σε γλυπτά και κτίρια.", "The use of many colours on sculpture and buildings."),
    T("το αριστούργημα", "masterpiece", "Έργο τέχνης εξαιρετικής ποιότητας.", "A work of art of outstanding quality."),
    T("το επιτύμβιο", "epitaph", "Κείμενο ή μνημείο πάνω σε τάφο.", "A text or monument on a grave."),
  ],
  questions=[
    Q("Από πού πήραν οι Έλληνες την ιδέα για τα μεγάλα πέτρινα αγάλματα;", ["Από την Αίγυπτο", "Από την Περσία", "Από τη Ρώμη", "Από τη Γαλλία"], 0, "Via Naukratis and Greek mercenaries."),
    Q("Ποια είναι η μεγάλη διαφορά των κούρων από τα αιγυπτιακά αγάλματα;", ["Είναι γυμνοί και στέκονται ελεύθεροι", "Είναι καθιστοί", "Είναι από ξύλο", "Είναι πολύ μικροί"], 0, "No back slab, no clothes."),
    Q("Τι σημαίνει το «αρχαϊκό χαμόγελο»;", ["Δεν σημαίνει απαραίτητα χαρά", "Ότι ο γλύπτης αστειευόταν", "Ότι ο νεκρός ήταν ευτυχισμένος", "Ότι το άγαλμα είναι αιγυπτιακό"], 0, "Even dying warriors smile."),
    Q("Γιατί σώθηκαν τα χρώματα πολλών κορών της Ακρόπολης;", ["Γιατί θάφτηκαν μετά την περσική καταστροφή", "Γιατί τις έκρυψαν οι Πέρσες", "Γιατί ξαναβάφτηκαν", "Γιατί ήταν μέσα σε ναό"], 0, "The 'Persian debris' of 480 BC."),
  ],
  vocab=["εγκαθίσταμαι", "επιτρέπω", "ιδρύω", "τεράστιος", "άγαλμα", "γυμνός", "όρθιος", "στάση", "ντυμένος", "αντιγράφω", "στηρίζομαι", "πλάκα", "ελεύθερος", "αποδίδω", "μυς", "κίνηση", "ακρίβεια", "χαμόγελο", "απαραίτητα", "πολεμιστής", "ζωντανός", "μνημείο", "έντονος", "πολύχρωμος", "καταλαμβάνω", "λάκκος", "ισοπεδώνω", "βράχος", "φέρνω στο φως"],
  sources=[
    SRC("Herodotus, Histories 2.154 and 2.178 (Greek mercenaries in Egypt; Naukratis)."),
    SRC("Diodorus Siculus, Library of History 1.98 (Telekles and Theodoros and the Egyptian canon); Guralnick, E. (1978). “The proportions of kouroi”. American Journal of Archaeology 82: 461–472."),
    SRC("The Metropolitan Museum of Art, “Marble statue of a kouros (youth), ca. 590–580 BCE” (object record).", "https://www.metmuseum.org/art/collection/search/253370"),
    SRC("Boardman, J. (1991). Greek Sculpture: The Archaic Period. London: Thames & Hudson."),
    SRC("Brinkmann, V. & Wünsche, R. (eds.) (2007). Gods in Color: Painted Sculpture of Classical Antiquity. Munich: Stiftung Archäologie."),
    SRC("Herodotus, Histories 8.53 (the Persian sack of the Acropolis); Hurwit, J. M. (1999). The Athenian Acropolis. Cambridge University Press."),
  ]))

# 3.3 politics
CH.append(dict(id="e3-polis", theme="politics", el="Η πόλη-κράτος, οι αποικίες και οι πρώτοι νομοθέτες", title="The city-state, the colonies and the first lawgivers", dates="περ. 800–500 π.Χ.",
  image="owl",
  summary_en="The rise of the polis, the great wave of colonisation from Marseille to the Crimea, and the Athenian reforms of Draco, Solon and Cleisthenes that led towards democracy.",
  sections=[
    S("polis", "Τι ήταν η πόλη-κράτος", "What the city-state was", [
      P("Η «πόλις» των αρχαίων Ελλήνων δεν ήταν απλώς μια πόλη. Ήταν μια ανεξάρτητη κοινότητα πολιτών, με δικούς της νόμους, θεούς, στρατό και, από τον 6ο αιώνα π.Χ., δικά της νομίσματα. Συνήθως περιλάμβανε ένα αστικό κέντρο με ακρόπολη και αγορά, και γύρω του την ύπαιθρο με τα χωριά. Οι περισσότερες πόλεις ήταν μικρές, με λίγες χιλιάδες κατοίκους, και υπήρχαν περισσότερες από χίλιες.",
        "The ancient Greek polis was not simply a town. It was an independent community of citizens, with its own laws, gods, army and, from the sixth century BC, its own coinage (coins were invented in Lydia around 600 BC and quickly adopted by Greek cities; the Athenian 'owls' in the picture became the most trusted silver coin of the Aegean). It usually included an urban centre with an acropolis and an agora, and around it the countryside with its villages: Athens included all of Attica. Most poleis were small, with a few thousand inhabitants, and there were more than a thousand of them; the Copenhagen Polis Centre's inventory lists 1,035 known poleis of the Archaic and Classical periods. What made the citizens equals was, increasingly, that they fought side by side as hoplites, heavily armed infantrymen in a close formation, the phalanx.", [1, 2]),
      P("Η λέξη «πόλις» μάς έδωσε πολλές λέξεις: «πολίτης», «πολιτική», «πολιτισμός». Ο Αριστοτέλης θα γράψει τον 4ο αιώνα π.Χ. ότι ο άνθρωπος είναι «φύσει πολιτικόν ζῷον», δηλαδή ένα ον που από τη φύση του ζει μέσα σε πόλη. Όποιος μπορεί να ζήσει μόνος του, προσθέτει, είναι είτε θηρίο είτε θεός.",
        "The word polis has given us many words: πολίτης 'citizen', πολιτική 'politics', πολιτισμός 'civilisation', and through Latin and English 'police' and 'policy'. Aristotle would write in the fourth century BC that man is 'by nature a political animal' (φύσει πολιτικὸν ζῷον), a being who by nature lives in a polis, and that anyone who can live alone, outside the polis, is either a beast or a god (Politics 1253a). For Aristotle the polis was not a convenience but the condition for a fully human, good life.", [3]),
    ]),
    S("colonies", "«Σαν βάτραχοι γύρω από μια λίμνη»", "'Like frogs around a pond'", [
      P("Από τον 8ο ως τον 6ο αιώνα π.Χ. οι Έλληνες ίδρυσαν εκατοντάδες αποικίες σε όλη τη Μεσόγειο και τη Μαύρη Θάλασσα. Οι λόγοι ήταν πολλοί: η έλλειψη γης, οι πολιτικές συγκρούσεις, το εμπόριο. Μια πόλη, η «μητρόπολη», έστελνε μια ομάδα αποίκων με αρχηγό τον «οικιστή», συνήθως αφού ζητούσε τη γνώμη του μαντείου των Δελφών. Η νέα πόλη ήταν ανεξάρτητη, αλλά κρατούσε δεσμούς με τη μητρόπολη.",
        "From the eighth to the sixth century BC the Greeks founded hundreds of colonies all around the Mediterranean and the Black Sea. The reasons were many: shortage of farmland, political conflict, trade, adventure. A city, the 'mother city' (metropolis), sent out a group of colonists led by a founder (oikistēs), usually after consulting the oracle of Delphi. The new city was independent, but kept religious and sentimental ties with its metropolis. Among the most famous foundations are Syracuse (traditionally 733 BC, from Corinth), Byzantion (traditionally in the 660s BC, from Megara), Cyrene in Libya (c. 631 BC, from Thera, a foundation described in detail by Herodotus 4.150–159) and Massalia, modern Marseille (c. 600 BC, from Phocaea).", [4, 5]),
      P("Έτσι οι Έλληνες απλώθηκαν από τη Μασσαλία ως την Κριμαία και από την Κυρήνη ως την Τραπεζούντα. Ο Πλάτωνας βάζει τον Σωκράτη να λέει ότι οι Έλληνες κατοικούν γύρω από τη θάλασσα «σαν μυρμήγκια ή βάτραχοι γύρω από μια λίμνη». Πολλές από αυτές τις πόλεις, όπως η Νάπολη (Νεάπολις, «νέα πόλη»), η Μασσαλία και η Κωνσταντινούπολη, το αρχαίο Βυζάντιο, υπάρχουν μέχρι σήμερα.",
        "In this way the Greeks spread from Marseille to the Crimea and from Cyrene to Trebizond. Southern Italy and Sicily became so Greek that the Romans called the region Magna Graecia, 'Great Greece'. Plato has Socrates say that the Greeks live around the sea 'like ants or frogs around a pond' (Phaedo 109b). Many of these cities, such as Naples (Neapolis, 'new city'), Marseille and Istanbul, ancient Byzantion, still exist today, and Greek was spoken in parts of southern Italy without a break into modern times, in the Griko and Grecanico dialects.", [4, 6]),
    ]),
    S("lawgivers", "Δράκων, Σόλων, Κλεισθένης", "Draco, Solon, Cleisthenes", [
      P("Στην Αθήνα, όπως και σε άλλες πόλεις, η εξουσία ανήκε αρχικά σε λίγες αριστοκρατικές οικογένειες. Γύρω στο 621 π.Χ. ο Δράκων κατέγραψε για πρώτη φορά τους νόμους. Ήταν τόσο αυστηροί, ώστε, όπως έλεγαν αργότερα, ήταν γραμμένοι «με αίμα και όχι με μελάνι». Γι' αυτό λέμε ακόμα σήμερα «δρακόντεια μέτρα». Το πιο σημαντικό όμως ήταν ότι οι νόμοι ήταν πλέον γραμμένοι και ίδιοι για όλους.",
        "In Athens, as in other cities, power at first belonged to a few aristocratic families, who interpreted unwritten custom as they pleased. Around 621 BC Draco recorded the laws in writing for the first time. They were so harsh that, as later Athenians said, they were written 'in blood, not ink' (Plutarch, Solon 17, quoting the orator Demades): even stealing vegetables was said to be punishable by death. That is why we still say 'draconian measures'. But the most important thing was that the laws were now written down and the same for everyone; his homicide law, which distinguished intentional from unintentional killing, remained in force for centuries.", [7, 8]),
      P("Το 594 π.Χ. οι Αθηναίοι έδωσαν στον Σόλωνα, έναν αριστοκράτη και ποιητή, την εξουσία να λύσει μια βαθιά κρίση. Πολλοί φτωχοί αγρότες είχαν χρεωθεί τόσο, που είχαν γίνει δούλοι των πλουσίων. Ο Σόλων ακύρωσε τα χρέη, με τη λεγόμενη «σεισάχθεια», και απαγόρευσε να γίνεται κάποιος δούλος για χρέη. Το 508/507 π.Χ. ο Κλεισθένης αναδιοργάνωσε τους πολίτες σε δέκα φυλές με βάση τον τόπο κατοικίας και όχι την καταγωγή, και έτσι άνοιξε τον δρόμο για τη δημοκρατία.",
        "In 594 BC the Athenians gave Solon, an aristocrat and poet, the power to resolve a deep crisis. Many poor farmers had fallen so far into debt that they had become serfs or even slaves of the rich, some sold abroad. Solon cancelled the debts with the so-called seisachtheia, 'shaking off of burdens', and banned enslavement for debt; in his own poems he boasts that he freed the black earth by pulling up the boundary stones of mortgage. He also divided citizens into four classes by agricultural income, opening offices to wealth rather than birth. After a period of tyranny under Peisistratos and his sons, in 508/507 BC Cleisthenes reorganised the citizens into ten tribes based on place of residence (the demes) rather than descent, mixing coast, city and inland in each tribe, and created a Council of 500. In this way he opened the road to democracy; Herodotus says he 'took the people into his faction' (5.66).", [7, 8]),
    ]),
  ],
  grammar=[
    G("B2", "Result clauses: τόσο ... ώστε / που", "Συμπερασματικές προτάσεις",
      "'So ... that' is τόσο (+ adjective/adverb) ... ώστε or, more colloquially, που: Ήταν τόσο αυστηροί, ώστε... ; είχαν χρεωθεί τόσο, που είχαν γίνει δούλοι. With a noun use τόσος/τόση/τόσο (agreeing): τόσα χρέη, που...",
      [("Ήταν τόσο αυστηροί, ώστε ήταν γραμμένοι «με αίμα».", "They were so harsh that they were written 'in blood'."),
       ("Είχαν χρεωθεί τόσο, που είχαν γίνει δούλοι.", "They had fallen so deep into debt that they had become slaves.")]),
    G("B2", "είτε ... είτε, ούτε ... ούτε", "Διαζευκτικοί και αρνητικοί σύνδεσμοι",
      "είτε ... είτε 'either ... or' offers two possibilities: είτε θηρίο είτε θεός. ούτε ... ούτε 'neither ... nor' goes with δεν before the verb: δεν ήταν ούτε δίκαιοι ούτε γραμμένοι.",
      [("Όποιος ζει μόνος του είναι είτε θηρίο είτε θεός.", "Whoever lives alone is either a beast or a god."),
       ("Οι νόμοι δεν ήταν ούτε γραμμένοι ούτε ίδιοι για όλους.", "The laws were neither written nor the same for all.")]),
  ],
  terms=[
    T("η πόλη-κράτος", "city-state, polis", "Ανεξάρτητη πόλη με τη γύρω περιοχή, δικούς της νόμους και στρατό.", "An independent city with its territory, laws and army."),
    T("η αποικία", "colony", "Πόλη που ιδρύθηκε από αποίκους άλλης πόλης.", "A city founded by settlers from another city."),
    T("η μητρόπολη", "mother city; metropolis", "Η πόλη που ίδρυσε μια αποικία· σήμερα και μεγάλη πόλη ή έδρα μητροπολίτη.", "The city that founded a colony; today also a big city or a bishop's see."),
    T("ο οπλίτης", "hoplite", "Βαριά οπλισμένος πεζός στρατιώτης.", "A heavily armed foot soldier."),
    T("ο νομοθέτης", "lawgiver", "Αυτός που γράφει ή θεσπίζει νόμους.", "One who writes or lays down laws."),
    T("δρακόντειος", "draconian", "Πάρα πολύ αυστηρός.", "Extremely harsh."),
    T("η σεισάχθεια", "seisachtheia, cancellation of debts", "Η ακύρωση των χρεών από τον Σόλωνα το 594 π.Χ.", "Solon's cancellation of debts in 594 BC."),
    T("η φυλή", "tribe", "Μία από τις υποδιαιρέσεις των πολιτών μιας πόλης.", "One of the divisions of a city's citizens."),
  ],
  questions=[
    Q("Τι ήταν η «πόλις» για τους αρχαίους;", ["Ανεξάρτητη κοινότητα πολιτών με δικούς της νόμους", "Μια πρωτεύουσα αυτοκρατορίας", "Ένα χωριό χωρίς στρατό", "Ένας ναός"], 0, "With laws, gods, army and coins."),
    Q("Ποια από αυτές τις πόλεις ήταν αρχικά ελληνική αποικία;", ["Η Μασσαλία", "Η Ρώμη", "Η Βαβυλώνα", "Η Μέμφιδα"], 0, "Founded c. 600 BC from Phocaea."),
    Q("Γιατί λέμε «δρακόντεια μέτρα»;", ["Από τους πολύ αυστηρούς νόμους του Δράκοντα", "Από τους δράκους των μύθων", "Από έναν βασιλιά της Σπάρτης", "Από τον Σόλωνα"], 0, "Written 'in blood, not ink'."),
    Q("Τι έκανε ο Σόλων με τη «σεισάχθεια»;", ["Ακύρωσε τα χρέη", "Έχτισε τείχη", "Ίδρυσε αποικίες", "Κατάργησε τη θρησκεία"], 0, "And banned slavery for debt."),
  ],
  vocab=["ανεξάρτητος", "κοινότητα", "πολίτης", "νόμος", "νόμισμα", "περιλαμβάνω", "αστικός", "αγορά", "ύπαιθρος", "θηρίο", "έλλειψη", "σύγκρουση", "μαντείο", "δεσμός", "απλώνομαι", "μυρμήγκι", "βάτραχος", "αριστοκρατικός", "καταγράφω", "αυστηρός", "αίμα", "μελάνι", "κρίση", "χρέος", "δούλος", "ακυρώνω", "απαγορεύω", "αναδιοργανώνω", "καταγωγή"],
  sources=[
    SRC("Hansen, M. H. & Nielsen, T. H. (eds.) (2004). An Inventory of Archaic and Classical Poleis. Oxford University Press."),
    SRC("The Metropolitan Museum of Art, “Silver tetradrachm, Athens, ca. 440–404 BC” (object record).", "https://www.metmuseum.org/art/collection/search/330160"),
    SRC("Aristotle, Politics 1.2, 1253a1–29 (the political animal)."),
    SRC("Boardman, J. (1999). The Greeks Overseas: Their Early Colonies and Trade. 4th ed. London: Thames & Hudson."),
    SRC("Herodotus, Histories 4.150–159 (the foundation of Cyrene)."),
    SRC("Plato, Phaedo 109b (frogs around a pond)."),
    SRC("Aristotle, Constitution of the Athenians (Ἀθηναίων Πολιτεία) 4–12 and 20–22; Plutarch, Life of Solon 15–17."),
    SRC("Herodotus, Histories 5.66–69 (Cleisthenes' reforms); Osborne, R. (2009). Greece in the Making, 1200–479 BC. 2nd ed. London: Routledge."),
  ]))

# 3.4 science
CH.append(dict(id="e3-ionians", theme="science", el="Οι Ίωνες φυσικοί: από τον μύθο στον λόγο", title="The Ionian thinkers: from myth to reason", dates="περ. 600–500 π.Χ.",
  image="milesian",
  summary_en="In sixth-century Miletus, Thales, Anaximander and Anaximenes began to explain nature without gods; Xenophanes mocked human-shaped deities and noticed fossils; Pythagoras found numbers in music.",
  sections=[
    S("miletus", "Η Μίλητος, μια πόλη στο σταυροδρόμι", "Miletus, a city at the crossroads", [
      P("Τον 6ο αιώνα π.Χ. η πιο λαμπρή πόλη του ελληνικού κόσμου δεν ήταν η Αθήνα, αλλά η Μίλητος, στην ακτή της Μικράς Ασίας. Ήταν ένα μεγάλο λιμάνι, με αποικίες στη Μαύρη Θάλασσα και επαφές με τη Λυδία, τη Βαβυλώνα και την Αίγυπτο. Εκεί, για πρώτη φορά απ' όσο ξέρουμε, κάποιοι άνθρωποι προσπάθησαν να εξηγήσουν τον κόσμο χωρίς να επικαλούνται τους θεούς. Τους ονομάζουμε «Ίωνες φυσικούς» ή «προσωκρατικούς».",
        "In the sixth century BC the most brilliant city of the Greek world was not Athens but Miletus, on the coast of Asia Minor in the region called Ionia. It was a great port, with dozens of colonies in the Black Sea and contacts with Lydia, Babylon and Egypt, from which it could learn astronomical records and practical geometry. There, for the first time as far as we know, some people tried to explain the world without invoking the gods, by looking for a natural principle (archē) behind all things. We call them the 'Ionian natural philosophers' (physikoi, from physis 'nature') or 'Presocratics'. Their books are lost: we know them through quotations and summaries in later writers, above all Aristotle, his pupil Theophrastus and much later Diogenes Laertius.", [1, 2]),
    ]),
    S("thales", "Θαλής και Αναξίμανδρος", "Thales and Anaximander", [
      P("Ο πρώτος από αυτούς ήταν ο Θαλής. Σύμφωνα με τον Ηρόδοτο, είχε προβλέψει μια έκλειψη ηλίου, που έγινε στη διάρκεια μιας μάχης ανάμεσα στους Λυδούς και στους Μήδους. Οι στρατιώτες τρόμαξαν τόσο, που σταμάτησαν να πολεμούν και έκαναν ειρήνη. Οι αστρονόμοι υπολογίζουν ότι πρόκειται για την έκλειψη της 28ης Μαΐου του 585 π.Χ. Ο Θαλής δίδασκε ότι η αρχή των πάντων είναι το νερό. Η απάντηση ήταν λάθος, αλλά η ερώτηση ήταν καινούρια: από τι είναι φτιαγμένος ο κόσμος;",
        "The first of them was Thales. According to Herodotus (1.74), he had foretold an eclipse of the sun that took place during a battle between the Lydians and the Medes; the soldiers were so frightened that they stopped fighting and made peace. Astronomers calculate that this was the eclipse of 28 May 585 BC, which is why that date is often given as the 'birthday' of Greek philosophy; how Thales could have predicted it, perhaps from Babylonian eclipse cycles, and how precisely, is doubted by historians of astronomy. Thales taught that the first principle of all things is water. The answer was wrong, but the question was new: what is the world made of? Later tradition credits him with measuring the height of the pyramids from their shadows and with several geometrical theorems.", [1, 3]),
      P("Ο μαθητής του, ο Αναξίμανδρος, πήγε ακόμα πιο μακριά. Υποστήριξε ότι η αρχή δεν είναι κάποιο από τα γνωστά υλικά, αλλά κάτι αόριστο και χωρίς όρια, το «άπειρον». Φαντάστηκε τη Γη σαν έναν κύλινδρο που αιωρείται στο κέντρο του κόσμου χωρίς να στηρίζεται πουθενά, επειδή δεν έχει λόγο να πέσει προς καμία κατεύθυνση. Λέγεται ότι σχεδίασε τον πρώτο χάρτη του γνωστού κόσμου. Πρότεινε μάλιστα ότι οι άνθρωποι προέρχονται από άλλα ζώα, που ζούσαν αρχικά στο νερό.",
        "His pupil Anaximander (c. 610–546 BC) went even further. He argued that the first principle is not one of the known materials but something indefinite and boundless, the apeiron. He imagined the Earth as a drum-shaped cylinder that hangs at the centre of the cosmos without resting on anything, because it has no reason to fall in any direction rather than another, an argument from symmetry that impressed Aristotle (On the Heavens 295b). He is said to have drawn the first map of the known world (Strabo 1.1.11) and to have introduced the gnomon, the shadow-stick sundial, to Greece. He even suggested that humans came from other animals that at first lived in water, since a human baby is too helpless to have survived on its own. His follower Anaximenes made air the first principle, changing into other things by thickening and thinning, which was the first attempt to explain qualities by quantities.", [2, 4]),
    ]),
    S("xenophanes", "Ξενοφάνης και Πυθαγόρας", "Xenophanes and Pythagoras", [
      P("Ο ποιητής Ξενοφάνης από την Κολοφώνα έκανε μια τολμηρή παρατήρηση για τους θεούς. Οι Αιθίοπες, έγραψε, λένε ότι οι θεοί τους είναι μαύροι και με πλατιές μύτες, ενώ οι Θράκες ότι έχουν γαλανά μάτια και κόκκινα μαλλιά. Και αν τα βόδια και τα άλογα είχαν χέρια, θα ζωγράφιζαν θεούς που μοιάζουν με βόδια και άλογα. Ο Ξενοφάνης παρατήρησε επίσης κοχύλια και αποτυπώματα ψαριών πάνω στα βουνά και συμπέρανε ότι κάποτε η θάλασσα σκέπαζε τη στεριά.",
        "The poet Xenophanes of Colophon (c. 570–475 BC) made a bold observation about the gods. The Ethiopians, he wrote, say their gods are black and snub-nosed, while the Thracians say theirs have blue eyes and red hair (fragment 16); and if oxen and horses had hands, they would draw gods that look like oxen and horses (fragment 15). His target was the human-shaped, quarrelsome gods of Homer and Hesiod, whom he accused of every human vice. Xenophanes also noticed shells and the impressions of fish in rocks on mountains and in quarries (at Syracuse, Paros and Malta) and concluded that the sea had once covered the land, one of the earliest known interpretations of fossils (reported by Hippolytus, Refutation 1.14).", [2, 5]),
      P("Ο Πυθαγόρας από τη Σάμο εγκαταστάθηκε γύρω στο 530 π.Χ. στον Κρότωνα της νότιας Ιταλίας, όπου ίδρυσε μια κοινότητα με αυστηρούς κανόνες ζωής. Οι πυθαγόρειοι πίστευαν ότι η ουσία των πραγμάτων είναι οι αριθμοί. Ανακάλυψαν ότι οι αρμονικές μουσικές συγχορδίες αντιστοιχούν σε απλές αναλογίες μήκους των χορδών, όπως 2:1 για την οκτάβα. Το περίφημο «Πυθαγόρειο θεώρημα» ήταν όμως γνωστό στους Βαβυλώνιους πολύ πριν από αυτόν.",
        "Pythagoras of Samos settled around 530 BC at Croton in southern Italy, where he founded a community with strict rules of life (including, famously, restrictions on eating beans) and a belief in the transmigration of souls. The Pythagoreans believed that the essence of things is number. They discovered that harmonious musical intervals correspond to simple ratios of string length, such as 2:1 for the octave, 3:2 for the fifth and 4:3 for the fourth, perhaps the first mathematical law of nature ever found. The famous 'Pythagorean theorem', however, was known to the Babylonians more than a thousand years earlier (as the tablet Plimpton 322 and other Old Babylonian texts show), and it is not certain that Pythagoras himself proved it; he wrote nothing, and his followers attributed their discoveries to him.", [2, 6]),
    ]),
  ],
  grammar=[
    G("B2", "Unreal conditions in the present: αν + imperfect, θα + imperfect", "Υποθετικοί λόγοι του αντίθετου",
      "To talk about something that is not true (if oxen had hands), Greek uses αν + imperfect in the 'if' clause and θα + imperfect in the main clause: Αν τα βόδια είχαν χέρια, θα ζωγράφιζαν θεούς. The same forms can refer to the past ('if they had had... they would have painted'), though a pluperfect is clearer for the past.",
      [("Αν τα βόδια είχαν χέρια, θα ζωγράφιζαν θεούς σαν βόδια.", "If oxen had hands, they would paint gods like oxen."),
       ("Αν η Γη στηριζόταν κάπου, θα έπεφτε.", "If the Earth rested on something, it would fall.")]),
    G("B2", "Reporting what someone taught: ότι + indicative", "Πλάγιος λόγος με «ότι»",
      "After verbs of saying and thinking (λέω, γράφω, διδάσκω, υποστηρίζω, πιστεύω) Greek uses ότι or πως + indicative, keeping the tense the speaker used: Ο Θαλής δίδασκε ότι η αρχή είναι το νερό ('taught that the principle is water'). English often shifts to 'was'; Greek does not have to.",
      [("Υποστήριξε ότι η αρχή δεν είναι κάποιο γνωστό υλικό.", "He argued that the principle is not a known material."),
       ("Συμπέρανε ότι κάποτε η θάλασσα σκέπαζε τη στεριά.", "He concluded that the sea had once covered the land.")]),
  ],
  terms=[
    T("ο προσωκρατικός", "Presocratic", "Φιλόσοφος που έζησε πριν από τον Σωκράτη ή στην εποχή του.", "A philosopher before or contemporary with Socrates."),
    T("η αρχή", "first principle; beginning; authority", "Για τους φυσικούς, η βασική ουσία από την οποία γίνονται όλα.", "For the physikoi, the basic stuff from which everything comes."),
    T("η έκλειψη", "eclipse", "Όταν η Σελήνη κρύβει τον Ήλιο ή η Γη τη Σελήνη.", "When the Moon hides the Sun or the Earth the Moon."),
    T("το άπειρον", "the boundless (apeiron)", "Κατά τον Αναξίμανδρο, η αόριστη αρχή του κόσμου.", "For Anaximander, the indefinite origin of the world."),
    T("αιωρούμαι", "to hang, float in the air", "Βρίσκομαι στον αέρα χωρίς να στηρίζομαι.", "To be suspended without support."),
    T("το απολίθωμα", "fossil", "Λείψανο ή αποτύπωμα φυτού ή ζώου μέσα σε πέτρα.", "The remains or imprint of a plant or animal in rock."),
    T("η αναλογία", "ratio, proportion", "Η σχέση ανάμεσα σε δύο μεγέθη, π.χ. 2 προς 1.", "The relation between two quantities, e.g. 2 to 1."),
  ],
  questions=[
    Q("Ποια έκλειψη πιστεύεται ότι προέβλεψε ο Θαλής;", ["Της 28ης Μαΐου 585 π.Χ.", "Του 1453", "Της πτώσης της Τροίας", "Του 776 π.Χ."], 0, "Herodotus 1.74; Lydians and Medes made peace."),
    Q("Γιατί, κατά τον Αναξίμανδρο, η Γη δεν πέφτει;", ["Γιατί δεν έχει λόγο να πέσει προς καμία κατεύθυνση", "Γιατί τη στηρίζει ο Άτλας", "Γιατί επιπλέει στο νερό", "Γιατί είναι πολύ ελαφριά"], 0, "An argument from symmetry."),
    Q("Τι παρατήρησε ο Ξενοφάνης για τους θεούς;", ["Ότι κάθε λαός τους φαντάζεται σαν τον εαυτό του", "Ότι δεν υπάρχουν βουνά", "Ότι οι θεοί είναι αριθμοί", "Ότι οι θεοί ζουν στη Μίλητο"], 0, "Fragments 15–16."),
    Q("Τι ανακάλυψαν οι πυθαγόρειοι για τη μουσική;", ["Ότι οι συγχορδίες αντιστοιχούν σε απλές αναλογίες", "Ότι η μουσική είναι επικίνδυνη", "Ότι η λύρα ήρθε από την Αίγυπτο", "Τίποτα"], 0, "2:1 octave, 3:2 fifth, 4:3 fourth."),
  ],
  vocab=["λαμπρός", "επαφή", "εξηγώ", "επικαλούμαι", "προβλέπω", "μάχη", "τρομάζω", "ειρήνη", "υπολογίζω", "καινούριος", "φτιαγμένος", "υποστηρίζω", "αόριστος", "όριο", "κατεύθυνση", "σχεδιάζω", "χάρτης", "προέρχομαι", "τολμηρός", "παρατήρηση", "κοχύλι", "αποτύπωμα", "συμπεραίνω", "στεριά", "ουσία", "αριθμός", "ανακαλύπτω", "μήκος", "χορδή", "θεώρημα"],
  sources=[
    SRC("Herodotus, Histories 1.74 (Thales and the eclipse); Stephenson, F. R. & Fatoohi, L. J. (1997). “Thales's prediction of a solar eclipse”. Journal for the History of Astronomy 28: 279–282."),
    SRC("Kirk, G. S., Raven, J. E. & Schofield, M. (1983). The Presocratic Philosophers. 2nd ed. Cambridge University Press."),
    SRC("Aristotle, Metaphysics 983b (Thales and water)."),
    SRC("Aristotle, On the Heavens 295b10–16; Strabo, Geography 1.1.11; Couprie, D. L. (2011). Heaven and Earth in Ancient Greek Cosmology. New York: Springer."),
    SRC("Xenophanes, fragments DK 21 B15, B16; Hippolytus, Refutation of All Heresies 1.14."),
    SRC("Burkert, W. (1972). Lore and Science in Ancient Pythagoreanism. Cambridge, MA: Harvard University Press; Robson, E. (2001). “Neither Sherlock Holmes nor Babylon: a reassessment of Plimpton 322”. Historia Mathematica 28: 167–206."),
  ]))

# 3.5 culture
CH.append(dict(id="e3-delphi", theme="culture", el="Δελφοί και Ολυμπία: τα κοινά ιερά των Ελλήνων", title="Delphi and Olympia: the shared sanctuaries of the Greeks", dates="8ος–6ος αιώνας π.Χ.",
  image="pythia",
  summary_en="How rival cities came to share a common Greek identity at the Panhellenic sanctuaries: the oracle of Apollo at Delphi, its riddling answers, and the games at Olympia under the sacred truce.",
  sections=[
    S("panhellenic", "Χωρισμένοι αλλά Έλληνες", "Divided, yet Greek", [
      P("Οι Έλληνες δεν είχαν ποτέ στην αρχαιότητα ένα ενιαίο κράτος. Οι πόλεις τους ήταν ανεξάρτητες και συχνά πολεμούσαν μεταξύ τους. Παρ' όλα αυτά, ένιωθαν ότι ανήκαν σε έναν κοινό κόσμο. Ο Ηρόδοτος γράφει ότι αυτό που ένωνε τους Έλληνες ήταν το κοινό αίμα, η κοινή γλώσσα, τα κοινά ιερά και οι θυσίες, και τα κοινά ήθη. Τα σημαντικότερα σημεία συνάντησης ήταν τα «πανελλήνια» ιερά, κυρίως η Ολυμπία και οι Δελφοί.",
        "In antiquity the Greeks never had a single state. Their cities were independent and often fought each other. Nevertheless they felt they belonged to a common world. Herodotus has the Athenians declare that what united the Greeks (to Hellēnikon) was shared blood, a shared language, shared sanctuaries and sacrifices to the gods, and shared customs (8.144), one of the earliest definitions of a national identity. The most important meeting points were the 'Panhellenic' sanctuaries, open to all Greeks, above all Olympia and Delphi; with the sanctuaries of Poseidon at the Isthmus and of Zeus at Nemea they hosted the four great 'crown games' of the periodos, the athletic circuit.", [1, 2]),
    ]),
    S("olympia", "Οι Ολυμπιακοί αγώνες και η εκεχειρία", "The Olympic games and the truce", [
      P("Σύμφωνα με την παράδοση, οι πρώτοι Ολυμπιακοί αγώνες έγιναν το 776 π.Χ., στο ιερό του Δία στην Ολυμπία. Αρχικά υπήρχε μόνο ένα αγώνισμα, ο δρόμος του σταδίου, περίπου 192 μέτρα. Με τον καιρό προστέθηκαν η πάλη, η πυγμαχία, το πένταθλο και οι αρματοδρομίες. Οι νικητές δεν έπαιρναν χρήματα στην Ολυμπία, αλλά ένα στεφάνι από κλαδί αγριελιάς. Στις πόλεις τους όμως τους υποδέχονταν σαν ήρωες και τους έδιναν μεγάλες τιμές.",
        "According to tradition, the first Olympic games took place in 776 BC at the sanctuary of Zeus at Olympia; the date comes from victor lists compiled centuries later by the sophist Hippias of Elis, and archaeology suggests that the cult and some athletic activity are older, while the expansion of the festival belongs rather to the late eighth and seventh centuries. At first there was only one event, the stadion sprint of about 192 m (the Olympic stadium's length). In time wrestling, boxing, the pentathlon, chariot races and the brutal pankration were added. Victors received no money at Olympia, only a wreath of wild olive (kotinos); but their home cities welcomed them as heroes and gave them great honours, free meals for life in Athens, statues and odes by poets like Pindar. Only free Greek men could compete; married women were barred from even watching, although women could win the chariot race as owners, as the Spartan princess Kyniska did in 396 BC.", [3, 4]),
      P("Κατά τη διάρκεια των αγώνων κηρυσσόταν «εκεχειρία», μια ιερή ανακωχή. Οι αθλητές και οι θεατές μπορούσαν να ταξιδέψουν στην Ολυμπία με ασφάλεια, ακόμα και μέσα από πόλεις που βρίσκονταν σε πόλεμο. Η εκεχειρία δεν σταματούσε τους πολέμους, όπως πιστεύεται συχνά σήμερα, αλλά προστάτευε το ταξίδι και την ίδια την Ολυμπία. Όποιος την παραβίαζε πλήρωνε πρόστιμο, όπως έπαθαν οι Σπαρτιάτες το 420 π.Χ.",
        "During the games a sacred truce, the ekecheiria, was proclaimed by heralds sent out from Elis. Athletes and spectators could travel to Olympia in safety, even through cities at war. The truce did not stop wars in general, as is often believed today, but it protected the journey and Olympia itself. Whoever violated it paid a fine and could be excluded: this happened to the Spartans in 420 BC, who were barred from the games and fined 2,000 minas for attacking a fort during the truce (Thucydides 5.49–50). The modern 'Olympic Truce', revived by the United Nations in 1993, is inspired by this custom.", [4, 5]),
    ]),
    S("delphi", "Το μαντείο των Δελφών", "The oracle of Delphi", [
      P("Οι Δελφοί, στις πλαγιές του Παρνασσού, θεωρούνταν ο «ομφαλός», δηλαδή το κέντρο της Γης. Εκεί, στον ναό του Απόλλωνα, η ιέρεια Πυθία καθόταν σε έναν τρίποδα και έδινε χρησμούς σε όσους ρωτούσαν τον θεό. Οι ιερείς μετέφεραν τα λόγια της, συχνά σε στίχους. Ζητούσαν τη γνώμη της απλοί άνθρωποι, αλλά και βασιλιάδες και πόλεις, πριν από έναν πόλεμο ή πριν από την ίδρυση μιας αποικίας. Στον ναό ήταν γραμμένα δύο από τα πιο γνωστά ελληνικά ρητά: «Γνῶθι σαυτόν» και «Μηδὲν ἄγαν».",
        "Delphi, on the slopes of Parnassus, was considered the omphalos, the 'navel', the centre of the Earth: Zeus, the myth said, released two eagles from the ends of the world and they met there. In the temple of Apollo the priestess Pythia sat on a tripod and gave oracles to those who questioned the god. Priests passed on her words, often in hexameter verse. Ordinary people consulted her, but so did kings and cities, before a war or before founding a colony; consultations were limited to certain days, and enquirers paid a fee and sacrificed a goat. Two of the best-known Greek maxims were inscribed at the temple: 'Know thyself' (Γνῶθι σαυτόν) and 'Nothing in excess' (Μηδὲν ἄγαν). The ancient claim that the Pythia was intoxicated by vapours from a chasm has been both doubted and, after geological studies of faults under the temple, partly revived; it remains disputed.", [6, 7]),
      P("Οι χρησμοί ήταν συχνά διφορούμενοι. Ο πιο γνωστός δόθηκε, κατά τον Ηρόδοτο, στον Κροίσο, τον πλούσιο βασιλιά της Λυδίας. Ο Κροίσος ρώτησε αν πρέπει να εκστρατεύσει κατά των Περσών. Η Πυθία απάντησε ότι, αν το κάνει, θα καταστρέψει μια μεγάλη αυτοκρατορία. Ο Κροίσος επιτέθηκε, νικήθηκε, και η μεγάλη αυτοκρατορία που καταστράφηκε ήταν η δική του. Από τότε μια απάντηση που μπορεί να ερμηνευτεί με δύο τρόπους λέγεται «πυθικός χρησμός», και για όποιον μιλά έτσι λέμε ότι «μιλάει σαν την Πυθία».",
        "The oracles were often ambiguous. The most famous was given, according to Herodotus (1.53, 1.91), to Croesus, the wealthy king of Lydia. Croesus asked whether he should march against the Persians. The Pythia answered that if he did, he would destroy a great empire. Croesus attacked, was defeated by Cyrus in 547/546 BC, and the great empire that was destroyed was his own; when he complained, the god replied that he should have asked which empire was meant. Ever since, an answer that can be interpreted in two ways is called a 'Pythian oracle' (πυθικός χρησμός), and modern Greeks say of someone who answers evasively, often a politician, that he 'speaks like the Pythia'. The sanctuary was also a showcase of rivalry: cities built 'treasuries' along the Sacred Way to display their offerings and victories.", [6, 8]),
    ]),
  ],
  grammar=[
    G("B2", "Future conditions: αν + aorist subjunctive, θα + subjunctive", "Υποθετικός λόγος για το μέλλον",
      "A real possibility in the future takes αν + subjunctive (usually aorist) and θα + subjunctive or future: αν το κάνει, θα καταστρέψει μια μεγάλη αυτοκρατορία 'if he does it, he will destroy a great empire'. In reported speech after a past verb the same forms stay: η Πυθία απάντησε ότι, αν το κάνει, θα καταστρέψει...",
      [("Αν εκστρατεύσεις κατά των Περσών, θα καταστρέψεις μια μεγάλη αυτοκρατορία.", "If you march against the Persians, you will destroy a great empire."),
       ("Όποιος την παραβιάσει, θα πληρώσει πρόστιμο.", "Whoever violates it will pay a fine.")]),
    G("B2", "Concession: παρ' όλα αυτά, αν και, μολονότι", "Εναντιωματικές εκφράσεις",
      "παρ' όλα αυτά / παρόλα αυτά 'nevertheless' starts a sentence that goes against what came before. αν και and (more formally) μολονότι + indicative mean 'although'. Do not confuse παρ' όλα αυτά with παρόλο που 'even though', which introduces a clause.",
      [("Οι πόλεις πολεμούσαν. Παρ' όλα αυτά, ένιωθαν Έλληνες.", "The cities fought. Nevertheless, they felt Greek."),
       ("Αν και δεν είχαν ενιαίο κράτος, είχαν κοινά ιερά.", "Although they had no single state, they had shared sanctuaries.")]),
  ],
  terms=[
    T("πανελλήνιος", "Panhellenic", "Που αφορά ή ανήκει σε όλους τους Έλληνες.", "Concerning or belonging to all Greeks."),
    T("το αγώνισμα", "(athletic) event", "Κάθε ξεχωριστός αγώνας μέσα σε μια διοργάνωση.", "Each separate contest within a competition."),
    T("η εκεχειρία", "truce", "Προσωρινή παύση των εχθροπραξιών· στην Ολυμπία, ιερή ανακωχή.", "A temporary stop to hostilities; at Olympia, a sacred truce."),
    T("το μαντείο", "oracle (place)", "Ιερό όπου οι άνθρωποι ρωτούσαν τους θεούς για το μέλλον.", "A sanctuary where people asked the gods about the future."),
    T("ο χρησμός", "oracle (response)", "Η απάντηση που έδινε ο θεός μέσω της ιέρειας.", "The answer the god gave through the priestess."),
    T("ο ομφαλός", "navel; centre", "Το κέντρο· οι Δελφοί θεωρούνταν ο ομφαλός της Γης.", "The centre; Delphi was the navel of the Earth."),
    T("διφορούμενος", "ambiguous", "Που μπορεί να ερμηνευτεί με δύο τρόπους.", "Open to two interpretations."),
    T("το ρητό", "maxim, saying", "Σύντομη φράση με γενική αλήθεια ή συμβουλή.", "A short phrase expressing a general truth or advice."),
  ],
  questions=[
    Q("Τι ένωνε τους Έλληνες, κατά τον Ηρόδοτο;", ["Το αίμα, η γλώσσα, τα ιερά και τα ήθη", "Ένας βασιλιάς", "Ένας κοινός στρατός", "Ένα κοινό νόμισμα"], 0, "Herodotus 8.144."),
    Q("Τι έπαιρναν οι νικητές στην Ολυμπία;", ["Στεφάνι από αγριελιά", "Χρυσό μετάλλιο", "Πολλά χρήματα", "Ένα άλογο"], 0, "The kotinos; rewards came later at home."),
    Q("Τι προστάτευε η ολυμπιακή εκεχειρία;", ["Το ταξίδι προς την Ολυμπία και το ίδιο το ιερό", "Όλους τους πολέμους", "Μόνο τους Σπαρτιάτες", "Τα σύνορα της Περσίας"], 0, "It did not stop wars in general."),
    Q("Ποια αυτοκρατορία κατέστρεψε ο Κροίσος;", ["Τη δική του", "Των Περσών", "Των Αιγυπτίων", "Των Αθηναίων"], 0, "Herodotus 1.53 and 1.91."),
  ],
  vocab=["ενιαίος", "μεταξύ", "νιώθω", "ενώνω", "θυσία", "ήθη", "συνάντηση", "παράδοση", "στάδιο", "πάλη", "νικητής", "στεφάνι", "κλαδί", "αγριελιά", "υποδέχομαι", "τιμή", "κηρύσσω", "ανακωχή", "θεατής", "ασφάλεια", "παραβιάζω", "πρόστιμο", "πλαγιά", "ιέρεια", "τρίποδας", "ίδρυση", "εκστρατεύω", "επιτίθεμαι", "ερμηνεύω"],
  sources=[
    SRC("Herodotus, Histories 8.144 (to Hellenikon)."),
    SRC("Hall, J. M. (2002). Hellenicity: Between Ethnicity and Culture. University of Chicago Press."),
    SRC("Pausanias, Description of Greece 5.8.6 (the first Olympiad, the stadion); Christesen, P. (2007). Olympic Victor Lists and Ancient Greek History. Cambridge University Press."),
    SRC("Miller, S. G. (2004). Ancient Greek Athletics. New Haven: Yale University Press."),
    SRC("Thucydides, History 5.49–50 (the Spartans excluded from the games of 420 BC)."),
    SRC("Scott, M. (2014). Delphi: A History of the Center of the Ancient World. Princeton University Press."),
    SRC("de Boer, J. Z., Hale, J. R. & Chanton, J. (2001). “New evidence for the geological origins of the ancient Delphic oracle (Greece)”. Geology 29: 707–710."),
    SRC("Herodotus, Histories 1.46–56 and 1.91 (Croesus and the oracle)."),
  ]))
