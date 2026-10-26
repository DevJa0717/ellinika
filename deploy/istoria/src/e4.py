# Era 4 · Κλασική εποχή (480–323 π.Χ.)
from common import P, S, G, T, Q, SRC

ERA = dict(id="classical", el="Η Κλασική εποχή", en="The Classical age", dates="480–323 π.Χ.", dates_en="480–323 BC", level="B2",
  intro_el="Από τη νίκη επί των Περσών ως τον θάνατο του Μεγάλου Αλεξάνδρου, η Αθήνα γίνεται το κέντρο του ελληνικού κόσμου. Είναι η εποχή της δημοκρατίας, του Παρθενώνα, του θεάτρου, της ιατρικής του Ιπποκράτη και της ιστορίας ως επιστήμης, αλλά και του καταστροφικού Πελοποννησιακού πολέμου.",
  intro_en="From the victory over Persia to the death of Alexander the Great, Athens becomes the centre of the Greek world, though never its master for long. This is the age of democracy, of the Parthenon, of tragedy and comedy, of Hippocratic medicine and of history as a discipline, and also of the ruinous Peloponnesian War (431–404 BC) between Athens and Sparta. The Greek remains B2 but now uses more learned vocabulary, abstract nouns and the passive participles typical of serious prose.")

CH = []

# 4.1 politics
CH.append(dict(id="e4-democracy", theme="politics", el="Η αθηναϊκή δημοκρατία στην πράξη", title="Athenian democracy in practice", dates="508–322 π.Χ.",
  image="democracy",
  summary_en="How direct democracy actually worked in fifth- and fourth-century Athens: the Assembly on the Pnyx, the Council chosen by lot, the popular courts, ostracism, pay for office, and who was left out.",
  sections=[
    S("context", "Μετά τον Μαραθώνα και τη Σαλαμίνα", "After Marathon and Salamis", [
      P("Στις αρχές του 5ου αιώνα π.Χ. η Περσική αυτοκρατορία, η μεγαλύτερη δύναμη του κόσμου, προσπάθησε δύο φορές να υποτάξει την Ελλάδα. Το 490 π.Χ. οι Αθηναίοι, μαζί με τους Πλαταιείς, νίκησαν τους Πέρσες στον Μαραθώνα. Δέκα χρόνια αργότερα, το 480 π.Χ., ο στόλος των ελληνικών πόλεων, με τους Αθηναίους να έχουν τα περισσότερα πλοία, νίκησε τον περσικό στόλο στη Σαλαμίνα. Η νίκη έδωσε στην Αθήνα τεράστιο κύρος και, ιδιαίτερα, έκανε σημαντικούς τους φτωχούς πολίτες που κωπηλατούσαν στις τριήρεις.",
        "At the beginning of the fifth century BC the Persian Empire, the greatest power in the world, twice tried to subjugate Greece. In 490 BC the Athenians, together with the Plataeans, defeated the Persians at Marathon. Ten years later, in 480 BC, after the Spartan stand at Thermopylae, the fleet of the allied Greek cities, in which Athens supplied the largest contingent, defeated the Persian fleet at Salamis, and in 479 BC the land army under Spartan command won at Plataea. The victory gave Athens enormous prestige and an empire, the Delian League. Above all, it made the poor citizens who rowed the triremes indispensable; Aristotle later linked the growth of democracy directly to the 'naval crowd' (Politics 1304a, Constitution of the Athenians 27).", [1, 2]),
    ]),
    S("assembly", "Η Εκκλησία του δήμου", "The Assembly of the people", [
      P("Η αθηναϊκή δημοκρατία ήταν άμεση: οι πολίτες δεν εξέλεγαν βουλευτές, αλλά αποφάσιζαν οι ίδιοι. Το κυρίαρχο σώμα ήταν η Εκκλησία του δήμου, δηλαδή η συνέλευση όλων των ενήλικων Αθηναίων πολιτών. Συνεδρίαζε περίπου σαράντα φορές τον χρόνο στον λόφο της Πνύκας, απέναντι από την Ακρόπολη. Εκεί ψήφιζαν για τον πόλεμο και την ειρήνη, για τους φόρους, για τις συμμαχίες και για τους νόμους. Οποιοσδήποτε πολίτης μπορούσε να ανέβει στο βήμα και να μιλήσει.",
        "Athenian democracy was direct: the citizens did not elect representatives but decided for themselves. The sovereign body was the Assembly (Ekklēsia) of the dēmos, the meeting of all adult male Athenian citizens. In the fourth century it met about forty times a year (four times in each of the ten 'prytanies' into which the year was divided) on the Pnyx hill, opposite the Acropolis; for some decisions, such as ostracism and grants of citizenship, a quorum of 6,000 was required. There they voted, usually by show of hands, on war and peace, taxes, alliances and laws. Any citizen could mount the speaker's platform (the bēma) and speak; the herald's opening question was 'Who wishes to speak?' (τίς ἀγορεύειν βούλεται;). The right of every citizen to speak, isēgoria, was as central to the Athenian idea of democracy as voting.", [3, 4]),
      P("Την ημερήσια διάταξη την ετοίμαζε η Βουλή των Πεντακοσίων. Τα μέλη της δεν εκλέγονταν, αλλά κληρώνονταν: πενήντα από κάθε φυλή, για έναν χρόνο, και κανείς δεν μπορούσε να γίνει βουλευτής περισσότερες από δύο φορές στη ζωή του. Με κλήρο επιλέγονταν και οι περισσότεροι άρχοντες και τα μέλη των λαϊκών δικαστηρίων. Οι Αθηναίοι πίστευαν ότι η κλήρωση είναι πιο δημοκρατική από την εκλογή, γιατί η εκλογή ευνοεί τους πλούσιους και τους διάσημους. Εκλέγονταν μόνο όσοι χρειάζονταν ειδικές γνώσεις, όπως οι δέκα στρατηγοί.",
        "The agenda was prepared by the Council (Boulē) of Five Hundred. Its members were not elected but chosen by lot: fifty from each tribe, for one year, and no one could serve more than twice in a lifetime, so a large share of citizens served at some point. Most magistrates and the jurors of the popular courts (dikastēria, with panels of 201, 501 or more) were also chosen by lot, using an allotment machine, the klērōtērion, with slots for citizens' bronze ID tickets. The Athenians believed that sortition is more democratic than election, because election favours the rich and famous; Aristotle states this plainly (Politics 1294b). Only those whose posts required special expertise, such as the ten generals (stratēgoi) and some financial officials, were elected, and could be re-elected: Pericles was general fifteen years in a row.", [3, 4]),
    ]),
    S("ostracism", "Όστρακα, μισθός και όρια", "Potsherds, pay and limits", [
      P("Μία φορά τον χρόνο ο δήμος μπορούσε να αποφασίσει να γίνει «οστρακισμός». Κάθε πολίτης χάραζε πάνω σε ένα κομμάτι σπασμένου αγγείου, ένα «όστρακο», το όνομα του πολιτικού που θεωρούσε επικίνδυνο για τη δημοκρατία. Αν μαζεύονταν τουλάχιστον έξι χιλιάδες όστρακα, εκείνος που είχε τους περισσότερους ψήφους έπρεπε να φύγει από την Αθήνα για δέκα χρόνια, χωρίς όμως να χάσει την περιουσία του. Οι αρχαιολόγοι έχουν βρει χιλιάδες όστρακα. Κάποια με το όνομα του Θεμιστοκλή είναι γραμμένα από λίγα μόνο χέρια, πράγμα που δείχνει ότι κάποιοι τα ετοίμαζαν από πριν για να τα μοιράσουν.",
        "Once a year the people could decide to hold an ostracism. Each citizen scratched on a piece of broken pottery, an ostrakon, the name of the politician he considered dangerous to the democracy. If at least six thousand ostraka were cast (or, on another ancient view, if one man received six thousand), the man with the most votes had to leave Athens for ten years, but without losing his property or citizenship. The first known ostracism was in 487 BC and the last around 416 BC. Archaeologists have found over ten thousand ostraka in the Agora and the Kerameikos. A batch of 190 with the name of Themistocles, found on the north slope of the Acropolis, is written in only a few hands, which shows that some people prepared them in advance to hand out, an early example of electoral organisation, or manipulation.", [5, 6]),
      P("Από την εποχή του Περικλή η πόλη πλήρωνε μισθό στους δικαστές, και από τις αρχές του 4ου αιώνα π.Χ. και σε όσους πήγαιναν στην Εκκλησία, για να μπορούν να συμμετέχουν και οι φτωχοί. Η δημοκρατία είχε όμως αυστηρά όρια. Πολίτες ήταν μόνο οι ενήλικοι άντρες με Αθηναίους γονείς, ίσως τριάντα με πενήντα χιλιάδες. Οι γυναίκες, οι μέτοικοι, δηλαδή οι ελεύθεροι ξένοι που ζούσαν στην Αθήνα, και οι πολυάριθμοι δούλοι δεν είχαν κανένα πολιτικό δικαίωμα.",
        "From the time of Pericles (c. 450s BC) the city paid jurors a daily wage, and from the early fourth century BC also those who attended the Assembly, so that the poor could take part. But democracy had strict limits. Citizens were only adult men with Athenian parents (after Pericles' citizenship law of 451/450 BC, both parents had to be Athenian), perhaps thirty to fifty thousand at the start of the Peloponnesian War. Women, metics (free foreigners living in Athens, who paid a special tax and served in the army), and the numerous slaves had no political rights; how many slaves there were is uncertain, with estimates from about 60,000 to over 100,000. In Thucydides' Funeral Oration, Pericles calls the system a democracy 'because it is run with a view to the many, not the few' (2.37); its critics, from the 'Old Oligarch' to Plato, called it the rule of the ignorant mob.", [4, 7]),
    ]),
  ],
  grammar=[
    G("B2", "The passive with an agent: από + accusative", "Παθητική φωνή και ποιητικό αίτιο",
      "When a passive verb names who did the action, Greek uses από + accusative: Η ημερήσια διάταξη ετοιμαζόταν από τη Βουλή. But Greek prefers the active with a fronted object in everyday style (Την ημερήσια διάταξη την ετοίμαζε η Βουλή), keeping the passive for processes without a clear agent: κληρώνονταν, εκλέγονταν.",
      [("Τα μέλη της δεν εκλέγονταν, αλλά κληρώνονταν.", "Its members were not elected but chosen by lot."),
       ("Ο Θεμιστοκλής εξοστρακίστηκε από τον δήμο.", "Themistocles was ostracised by the people.")]),
    G("B2", "όσοι, όποιος, οποιοσδήποτε: 'all who', 'whoever', 'anyone'", "Αναφορικές αντωνυμίες χωρίς προηγούμενο",
      "όσοι/όσες/όσα means 'all those who': εκλέγονταν μόνο όσοι χρειάζονταν ειδικές γνώσεις. όποιος 'whoever' introduces a clause; οποιοσδήποτε 'any(one) at all' is a pronoun or adjective: οποιοσδήποτε πολίτης.",
      [("Πλήρωνε και όσους πήγαιναν στην Εκκλησία.", "It also paid those who attended the Assembly."),
       ("Οποιοσδήποτε πολίτης μπορούσε να μιλήσει.", "Any citizen could speak.")]),
  ],
  terms=[
    T("η άμεση δημοκρατία", "direct democracy", "Πολίτευμα όπου οι πολίτες αποφασίζουν οι ίδιοι, χωρίς αντιπροσώπους.", "A system where citizens decide themselves, without representatives."),
    T("η Εκκλησία του δήμου", "the Assembly", "Η συνέλευση όλων των πολιτών στην αρχαία Αθήνα.", "The meeting of all citizens in ancient Athens."),
    T("η κλήρωση", "sortition, drawing lots", "Επιλογή προσώπων στην τύχη, με κλήρο.", "Choosing people at random, by lot."),
    T("ο οστρακισμός", "ostracism", "Δεκαετής εξορία πολιτικού με ψηφοφορία πάνω σε όστρακα.", "Ten-year exile of a politician by a vote on potsherds."),
    T("ο μέτοικος", "metic", "Ελεύθερος ξένος που ζούσε μόνιμα στην Αθήνα χωρίς πολιτικά δικαιώματα.", "A free foreign resident of Athens without political rights."),
    T("η τριήρης", "trireme", "Πολεμικό πλοίο με τρεις σειρές κουπιά.", "A warship with three banks of oars."),
    T("το κύρος", "prestige", "Η εκτίμηση και η επιρροή που έχει κάποιος.", "The respect and influence someone enjoys."),
    T("η ημερήσια διάταξη", "agenda", "Τα θέματα που θα συζητηθούν σε μια συνεδρίαση.", "The items to be discussed at a meeting."),
  ],
  questions=[
    Q("Γιατί η νίκη στη Σαλαμίνα ενίσχυσε τους φτωχούς πολίτες;", ["Γιατί αυτοί κωπηλατούσαν στις τριήρεις", "Γιατί πήραν χρήματα από τους Πέρσες", "Γιατί έγιναν όλοι στρατηγοί", "Γιατί έφυγαν οι πλούσιοι"], 0, "The 'naval crowd'."),
    Q("Πώς επιλέγονταν τα μέλη της Βουλής των Πεντακοσίων;", ["Με κλήρωση", "Με εκλογές", "Από τον βασιλιά", "Με κληρονομιά"], 0, "Fifty per tribe, by lot, for a year."),
    Q("Τι συνέβαινε σε όποιον εξοστρακιζόταν;", ["Έφευγε από την Αθήνα για δέκα χρόνια", "Εκτελούνταν", "Έχανε την περιουσία του", "Γινόταν δούλος"], 0, "He kept his property."),
    Q("Ποιοι δεν είχαν πολιτικά δικαιώματα;", ["Οι γυναίκες, οι μέτοικοι και οι δούλοι", "Οι φτωχοί πολίτες", "Οι στρατηγοί", "Οι κωπηλάτες"], 0, "Only adult male citizens voted."),
  ],
  vocab=["υποτάσσω", "νικώ", "κύρος", "κωπηλατώ", "άμεσος", "εκλέγω", "βουλευτής", "αποφασίζω", "κυρίαρχος", "συνέλευση", "ενήλικος", "συνεδριάζω", "ψηφίζω", "συμμαχία", "βήμα", "κληρώνω", "δικαστήριο", "ευνοώ", "γνώση", "στρατηγός", "επικίνδυνος", "ψήφος", "περιουσία", "μισθός", "συμμετέχω", "όριο", "πολυάριθμος", "δικαίωμα"],
  sources=[
    SRC("Herodotus, Histories 6.102–117 (Marathon) and 8.40–96 (Salamis)."),
    SRC("Aristotle, Constitution of the Athenians 27 and Politics 1304a (the naval crowd); Strauss, B. (2004). The Battle of Salamis. New York: Simon & Schuster."),
    SRC("Aristotle, Constitution of the Athenians 42–69 (the institutions of the 4th century)."),
    SRC("Hansen, M. H. (1991). The Athenian Democracy in the Age of Demosthenes. Oxford: Blackwell."),
    SRC("Plutarch, Life of Aristides 7 (the procedure of ostracism)."),
    SRC("Broneer, O. (1938). “Excavations on the north slope of the Acropolis, 1937”. Hesperia 7: 161–263 (the 190 Themistocles ostraka); Lang, M. (1990). Ostraka. The Athenian Agora vol. 25. Princeton: ASCSA."),
    SRC("Thucydides, History 2.35–46 (Pericles' Funeral Oration)."),
  ]))

# 4.2 art
CH.append(dict(id="e4-parthenon", theme="art", el="Ο Παρθενώνας: η τελειότητα που δεν είναι ευθεία", title="The Parthenon: a perfection without straight lines", dates="447–432 π.Χ.",
  image="parthenon",
  summary_en="Why Pericles rebuilt the Acropolis, how Iktinos, Kallikrates and Phidias built the Parthenon with almost no straight lines, and what happened to it over 2,400 years, from church and mosque to explosion and the Elgin Marbles.",
  sections=[
    S("pericles", "Το σχέδιο του Περικλή", "Pericles' programme", [
      P("Μετά την καταστροφή του 480 π.Χ., οι ναοί της Ακρόπολης έμειναν ερειπωμένοι για περίπου τριάντα χρόνια. Το 447 π.Χ., με πρόταση του Περικλή, οι Αθηναίοι άρχισαν ένα τεράστιο οικοδομικό πρόγραμμα. Τα έξοδα καλύφθηκαν εν μέρει από τα χρήματα της Δηλιακής Συμμαχίας, που οι σύμμαχοι της Αθήνας πλήρωναν για την κοινή άμυνα κατά των Περσών. Οι πολιτικοί αντίπαλοι του Περικλή τον κατηγόρησαν ότι στόλιζε την πόλη «σαν ματαιόδοξη γυναίκα» με τα χρήματα των άλλων.",
        "After the destruction of 480 BC, the temples of the Acropolis stood in ruins for about thirty years; according to a debated tradition, the Greeks had sworn not to rebuild the shrines the Persians had burned, as a memorial. In 447 BC, on Pericles' proposal, the Athenians began an enormous building programme: the Parthenon, then the Propylaia, the temple of Athena Nike and later the Erechtheion. The costs were met partly from the funds of the Delian League, which Athens' allies paid for common defence against Persia and whose treasury had been moved from Delos to Athens in 454 BC. Pericles' political opponents accused him of decking out the city 'like a vain woman' with other people's money; Pericles replied that as long as Athens protected the allies, it owed them no account (Plutarch, Pericles 12). The programme also provided work and wages for thousands of craftsmen.", [1, 2]),
      P("Τον Παρθενώνα τον σχεδίασαν οι αρχιτέκτονες Ικτίνος και Καλλικράτης, ενώ την επίβλεψη όλου του έργου είχε ο γλύπτης Φειδίας, φίλος του Περικλή. Ο ναός είναι δωρικός, με οκτώ κίονες στις στενές πλευρές και δεκαεπτά στις μακριές, όλος από πεντελικό μάρμαρο. Ο κυρίως ναός τελείωσε το 438 π.Χ. και τα γλυπτά το 432 π.Χ., μόλις ένα χρόνο πριν από την αρχή του Πελοποννησιακού πολέμου.",
        "The Parthenon was designed by the architects Iktinos and Kallikrates, while the supervision of the whole project lay with the sculptor Phidias, Pericles' friend. The temple is Doric, with eight columns on the short sides and seventeen on the long ones, built entirely of marble from Mount Pentelikon, some 16 km away; about 100,000 tonnes of marble have been estimated for the Periclean buildings as a whole. The main temple was finished, and the cult statue dedicated, in 438 BC, and the sculptures in 432 BC, just one year before the start of the Peloponnesian War. Inside stood Phidias' Athena Parthenos, about 11–12 m tall, made of gold and ivory over a wooden core; its gold plates, about 40 talents' weight, could be removed and counted as the city's reserve (Thucydides 2.13).", [2, 3]),
    ]),
    S("curves", "Καμπύλες που φαίνονται ευθείες", "Curves that look straight", [
      P("Ο Παρθενώνας φαίνεται απόλυτα κανονικός, αλλά σχεδόν καμία γραμμή του δεν είναι ευθεία. Η βάση του είναι ελαφρά κυρτή, ψηλότερη στο κέντρο κατά μερικά εκατοστά. Οι κίονες έχουν μια ελαφριά διόγκωση στο μέσο τους, την «ένταση», και γέρνουν λίγο προς τα μέσα. Οι γωνιακοί κίονες είναι λίγο χοντρότεροι από τους υπόλοιπους. Οι μελετητές πιστεύουν ότι αυτές οι «εκλεπτύνσεις» διορθώνουν τις οπτικές ψευδαισθήσεις και κάνουν το κτίριο να φαίνεται πιο ζωντανό και πιο σταθερό.",
        "The Parthenon looks perfectly regular, yet almost none of its lines is straight. Its base (the stylobate) is slightly convex, higher in the middle by about 6 cm on the short sides and 11 cm on the long sides. The columns swell slightly in the middle (entasis) and lean slightly inwards; it has been calculated that their axes, extended, would meet more than 2 km above the temple. The corner columns are a little thicker than the rest and the spacing between them is narrower. Scholars believe these 'refinements' correct optical illusions (a long straight line seen against the sky appears to sag, a column outlined against light looks thinner) and make the building look more alive and more stable; the Roman architect Vitruvius already explains them in this way (On Architecture 3.3–4). Because no two blocks are exactly alike, every stone had to be cut for its own place, which makes the current restoration so slow.", [3, 4]),
      P("Η γλυπτική διακόσμηση ήταν πλουσιότερη από κάθε άλλου ναού. Στα αετώματα παριστάνονταν η γέννηση της Αθηνάς και η διαμάχη της με τον Ποσειδώνα για την Αττική. Στις μετόπες υπήρχαν μάχες, ανάμεσά τους των Λαπιθών με τους Κενταύρους. Γύρω από τον κυρίως ναό έτρεχε μια ζωφόρος μήκους 160 μέτρων, που δείχνει μια πομπή με ιππείς, άρματα, μουσικούς και ζώα για θυσία, πιθανότατα την πομπή των Παναθηναίων.",
        "The sculptural decoration was richer than that of any other Greek temple. The pediments showed the birth of Athena from the head of Zeus and her contest with Poseidon for Attica. The 92 metopes showed battles, among them the Lapiths against the Centaurs, Greeks against Amazons and gods against giants, all understood as images of order against chaos and, implicitly, of Greeks against Persians. Around the inner building ran a continuous Ionic frieze 160 m long, showing a procession of horsemen, chariots, musicians and animals for sacrifice, most probably the Panathenaic procession in honour of Athena; its subject, mortals on a temple, was unprecedented, and its exact meaning is still debated.", [3, 5]),
    ]),
    S("history", "Ναός, εκκλησία, τζαμί, ερείπιο", "Temple, church, mosque, ruin", [
      P("Ο Παρθενώνας έζησε πολλές ζωές. Τον 6ο αιώνα μ.Χ. έγινε χριστιανική εκκλησία της Παναγίας, και μετά την οθωμανική κατάκτηση της Αθήνας, το 1458, τζαμί. Το 1687, κατά τη διάρκεια μιας πολιορκίας των Βενετών, οι Οθωμανοί είχαν αποθηκεύσει πυρίτιδα μέσα στον ναό. Μια βενετική οβίδα έπεσε πάνω της και η έκρηξη κατέστρεψε το κέντρο του κτιρίου. Ανάμεσα στο 1801 και το 1812, με άδεια των οθωμανικών αρχών που αμφισβητείται, ο Βρετανός πρέσβης λόρδος Έλγιν αφαίρεσε μεγάλο μέρος των γλυπτών, που βρίσκονται σήμερα στο Βρετανικό Μουσείο.",
        "The Parthenon has lived many lives. In the sixth century AD (the exact date is uncertain) it became a Christian church of the Virgin Mary (Panagia Atheniotissa), and after the Ottoman conquest of Athens in 1458 a mosque, with a minaret. On 26 September 1687, during a Venetian siege led by Francesco Morosini, the Ottomans had stored gunpowder inside the temple; a Venetian mortar shell struck it, and the explosion destroyed the centre of the building and killed some 300 people. Between 1801 and 1812, with a permission from the Ottoman authorities whose existence and scope are disputed (the surviving document is an Italian translation of a firman), the British ambassador Lord Elgin removed about half of the surviving sculptures, which he sold to the British Museum in 1816. Greece has requested their return since 1983, when the actress and minister Melina Merkouri launched the campaign.", [6, 7]),
      P("Από το 1975 μια ειδική επιτροπή επιστημόνων εργάζεται για την αναστήλωση των μνημείων της Ακρόπολης. Αφαιρούν τα σιδερένια στηρίγματα παλαιότερων επεμβάσεων, που σκούριαζαν και έσπαγαν το μάρμαρο, και τα αντικαθιστούν με τιτάνιο. Από το 2009 τα πρωτότυπα γλυπτά που έμειναν στην Αθήνα εκτίθενται στο νέο Μουσείο της Ακρόπολης, όπου ένας χώρος περιμένει ακόμα τα κομμάτια του Λονδίνου.",
        "Since 1975 a special committee of scientists (the Committee for the Conservation of the Acropolis Monuments, ESMA) has been working on the restoration of the Acropolis monuments. They remove the iron clamps of earlier interventions (mainly by Nikolaos Balanos, 1898–1939), which rusted, expanded and cracked the marble, and replace them with titanium; missing pieces are filled with new Pentelic marble, deliberately left lighter so that it can be distinguished. Since 2009 the original sculptures that remained in Athens have been displayed in the new Acropolis Museum, whose top-floor gallery, aligned with the temple itself, shows the frieze in its original order, with white plaster casts marking the pieces still in London.", [6, 8]),
    ]),
  ],
  grammar=[
    G("B2", "Learned adverbial phrases: εν μέρει, κατά τη διάρκεια", "Λόγιες εκφράσεις στον ιστορικό λόγο",
      "Formal Greek keeps many fixed phrases from older Greek: εν μέρει 'partly', εν τούτοις 'nevertheless', κατά τη διάρκεια + gen. 'during', κατά κύριο λόγο 'mainly', ως επί το πλείστον 'for the most part'. They are normal in history writing and journalism; learn them as whole units.",
      [("Τα έξοδα καλύφθηκαν εν μέρει από τα χρήματα της Συμμαχίας.", "The costs were met partly from the League's funds."),
       ("κατά τη διάρκεια μιας πολιορκίας", "during a siege")]),
    G("B2", "Comparatives in -ότερος and with πιο; κατά + amount", "Παραθετικά και διαφορά μεγέθους",
      "Comparatives are formed with πιο + adjective or with -ότερος/-ύτερος: πιο ζωντανό / ζωντανότερο, χοντρότεροι, πλουσιότερη. 'Than' is από + accusative or απ' ό,τι + clause. The size of a difference is given with κατά: ψηλότερη κατά μερικά εκατοστά 'higher by a few centimetres'.",
      [("Οι γωνιακοί κίονες είναι λίγο χοντρότεροι από τους υπόλοιπους.", "The corner columns are slightly thicker than the rest."),
       ("Η βάση είναι ψηλότερη στο κέντρο κατά μερικά εκατοστά.", "The base is higher in the centre by a few centimetres.")]),
  ],
  terms=[
    T("δωρικός", "Doric", "Ο απλούστερος από τους αρχαίους ρυθμούς αρχιτεκτονικής, με λιτά κιονόκρανα.", "The plainest ancient architectural order, with simple capitals."),
    T("το αέτωμα", "pediment", "Το τριγωνικό μέρος στην πρόσοψη ενός ναού, κάτω από τη στέγη.", "The triangular gable on the front of a temple."),
    T("η μετόπη", "metope", "Τετράγωνη πλάκα με ανάγλυφο ανάμεσα στα τρίγλυφα ενός δωρικού ναού.", "A square relief panel between the triglyphs of a Doric temple."),
    T("η ένταση", "entasis; tension; intensity", "Στην αρχιτεκτονική, η ελαφριά διόγκωση στη μέση του κίονα.", "In architecture, the slight swelling of a column's shaft."),
    T("η εκλέπτυνση", "refinement", "Μικρή, σκόπιμη απόκλιση από την ευθεία γραμμή σε ένα κτίριο.", "A small deliberate deviation from straight lines in a building."),
    T("η ψευδαίσθηση", "illusion", "Κάτι που φαίνεται αλλιώς απ' ό,τι είναι.", "Something that appears different from what it is."),
    T("η αναστήλωση", "restoration (of a monument)", "Η επανατοποθέτηση των κομματιών ενός μνημείου στη θέση τους.", "Putting a monument's pieces back in place."),
    T("η πυρίτιδα", "gunpowder", "Εκρηκτική σκόνη· λέγεται και μπαρούτι.", "Explosive powder (colloquially μπαρούτι)."),
  ],
  questions=[
    Q("Από πού προήλθαν εν μέρει τα χρήματα για τον Παρθενώνα;", ["Από τη Δηλιακή Συμμαχία", "Από την Περσία", "Από τη Σπάρτη", "Από την Αίγυπτο"], 0, "Allied contributions; Plutarch, Pericles 12."),
    Q("Ποιος είχε την επίβλεψη όλου του έργου;", ["Ο Φειδίας", "Ο Ικτίνος", "Ο Θεμιστοκλής", "Ο Έλγιν"], 0, "The architects were Iktinos and Kallikrates."),
    Q("Τι είναι η «ένταση» στους κίονες;", ["Μια ελαφριά διόγκωση στη μέση τους", "Ένα χρώμα", "Μια ρωγμή", "Ένα άγαλμα"], 0, "One of the optical refinements."),
    Q("Τι κατέστρεψε το κέντρο του Παρθενώνα το 1687;", ["Η έκρηξη πυρίτιδας από βενετική οβίδα", "Ένας σεισμός", "Μια φωτιά από κεραυνό", "Ο λόρδος Έλγιν"], 0, "During Morosini's siege."),
  ],
  vocab=["ερειπωμένος", "πρόταση", "οικοδομικός", "έξοδα", "καλύπτω", "σύμμαχος", "αντίπαλος", "κατηγορώ", "στολίζω", "ματαιόδοξος", "επίβλεψη", "πλευρά", "απόλυτα", "κανονικός", "ευθύς", "κυρτός", "γέρνω", "γωνιακός", "χοντρός", "μελετητής", "διορθώνω", "σταθερός", "διαμάχη", "πομπή", "ιππέας", "κατάκτηση", "αποθηκεύω", "οβίδα", "πρέσβης", "αφαιρώ", "στήριγμα", "σκουριάζω", "αντικαθιστώ", "εκτίθεμαι"],
  sources=[
    SRC("Plutarch, Life of Pericles 12–13 (the building programme and the opposition)."),
    SRC("Hurwit, J. M. (2004). The Acropolis in the Age of Pericles. Cambridge University Press."),
    SRC("Neils, J. (ed.) (2005). The Parthenon: From Antiquity to the Present. Cambridge University Press."),
    SRC("Vitruvius, On Architecture 3.3.13 and 3.4.5; Korres, M. (1994). “The architecture of the Parthenon”, in P. Tournikiotis (ed.), The Parthenon and its Impact in Modern Times. Athens: Melissa."),
    SRC("Jenkins, I. (1994). The Parthenon Frieze. London: British Museum Press."),
    SRC("Beard, M. (2002). The Parthenon. London: Profile Books."),
    SRC("St Clair, W. (1998). Lord Elgin and the Marbles. 3rd ed. Oxford University Press."),
    SRC("Acropolis Restoration Service (YSMA), “The restoration of the Acropolis monuments” (Hellenic Ministry of Culture).", "https://www.ysma.gr/en/"),
  ]))

# 4.3 science
CH.append(dict(id="e4-hippocrates", theme="science", el="Ο Ιπποκράτης και η γέννηση της ιατρικής", title="Hippocrates and the birth of medicine", dates="περ. 460–370 π.Χ.",
  image="hippocrates",
  summary_en="What we know (very little) about Hippocrates of Kos, what the sixty-odd books of the 'Hippocratic Corpus' actually say about disease, observation and ethics, and how the plague of Athens tested them.",
  sections=[
    S("man", "Ο άνθρωπος και η «Συλλογή»", "The man and the 'Corpus'", [
      P("Για τη ζωή του Ιπποκράτη ξέρουμε ελάχιστα. Γεννήθηκε στην Κω γύρω στο 460 π.Χ., σε μια οικογένεια γιατρών, ταξίδεψε σε πολλά μέρη της Ελλάδας και πέθανε, σύμφωνα με την παράδοση, στη Λάρισα σε μεγάλη ηλικία. Ήδη στην εποχή του ήταν διάσημος: ο Πλάτωνας τον αναφέρει ως το παράδειγμα του γιατρού. Με το όνομά του έχουν σωθεί περίπου εξήντα ιατρικά συγγράμματα, η λεγόμενη «Ιπποκρατική Συλλογή». Δεν τα έγραψε όλα ο ίδιος: είναι έργα διαφορετικών γιατρών, από τα τέλη του 5ου ως τον 4ο αιώνα π.Χ. και αργότερα.",
        "We know very little about Hippocrates' life. He was born on Kos around 460 BC into a family of physicians, the Asclepiads, who claimed descent from the healing god Asclepius; he travelled widely in Greece and died, according to tradition, at Larissa in Thessaly at a great age. Already in his lifetime he was famous: Plato mentions him as the very type of the physician who teaches for a fee (Protagoras 311b) and attributes to him the view that the body cannot be understood without understanding the whole (Phaedrus 270c). About sixty medical treatises have survived under his name, the so-called 'Hippocratic Corpus'. He did not write them all himself: they are works by different physicians, from the late fifth into the fourth century BC and later, written in Ionic Greek, and they sometimes contradict one another. Which, if any, are by Hippocrates himself is unknown.", [1, 2]),
    ]),
    S("nature", "Οι αρρώστιες έχουν φυσικές αιτίες", "Diseases have natural causes", [
      P("Η μεγάλη καινοτομία των ιπποκρατικών γιατρών ήταν η πεποίθηση ότι οι αρρώστιες έχουν φυσικές αιτίες, και όχι θεϊκές. Στο σύγγραμμα «Περί ιερής νούσου», για την επιληψία, ο συγγραφέας γράφει ότι η αρρώστια αυτή δεν είναι καθόλου πιο θεϊκή ή πιο ιερή από τις άλλες. Οι άνθρωποι τη λένε ιερή, εξηγεί, μόνο επειδή δεν την καταλαβαίνουν. Όσοι προσφέρουν μαγικές θεραπείες, προσθέτει με ειρωνεία, κρύβουν πίσω από τους θεούς τη δική τους άγνοια.",
        "The great innovation of the Hippocratic physicians was the conviction that diseases have natural causes, not divine ones. In the treatise On the Sacred Disease (Περὶ ἱερῆς νούσου), about epilepsy, the author writes that this disease is not in the least more divine or more sacred than others, but has a nature and a cause like other diseases; people call it sacred only because they do not understand it. Those who offer magical cures, purifications and spells, he adds ironically, hide their own ignorance behind the gods. He locates the cause in the brain, which he calls the organ of thought and feeling, a striking claim at a time when many placed thought in the heart or the diaphragm.", [3, 4]),
      P("Οι ιπποκρατικοί γιατροί έδιναν μεγάλη σημασία στην παρατήρηση. Στα βιβλία των «Επιδημιών» περιγράφουν δεκάδες ασθενείς, μέρα με τη μέρα: τον πυρετό, τον σφυγμό, τα ούρα, τον ύπνο, την έκβαση της αρρώστιας, ακόμα και όταν ο ασθενής πέθαινε. Στο έργο «Περί αέρων, υδάτων, τόπων» εξετάζουν πώς το κλίμα, το νερό και ο τρόπος ζωής επηρεάζουν την υγεία. Πολλοί πίστευαν ότι η υγεία είναι η ισορροπία τεσσάρων «χυμών» του σώματος: του αίματος, του φλέγματος, της κίτρινης και της μαύρης χολής. Η θεωρία ήταν λανθασμένη, αλλά θα κυριαρχήσει στην ευρωπαϊκή ιατρική για δύο χιλιάδες χρόνια.",
        "The Hippocratic physicians attached great importance to observation. In the books of the Epidemics they describe dozens of patients day by day: fever, pulse, urine, sleep and the outcome of the illness, even when the patient died, as roughly 60% of the recorded cases did, an honesty rare in medical writing before modern times. They put prognosis, foreseeing the course of a disease, at the centre of the physician's art. The work Airs, Waters, Places examines how climate, water and way of life affect health, and is the first text of environmental medicine (and, less happily, of climatic theories of national character). Many believed that health is the balance of four 'humours' of the body, blood, phlegm, yellow bile and black bile; the classic statement is in On the Nature of Man, attributed in antiquity to Hippocrates' son-in-law Polybus. The theory was wrong, but through Galen it would dominate European and Islamic medicine for two thousand years, and survives in words like 'melancholy' (μέλαινα χολή, black bile) and 'phlegmatic'.", [4, 5]),
    ]),
    S("ethics", "Ο όρκος και το «μη βλάπτειν»", "The oath and 'do no harm'", [
      P("Το πιο γνωστό κείμενο της Συλλογής είναι ο «Όρκος». Ο γιατρός ορκίζεται στους θεούς της ιατρικής ότι θα χρησιμοποιεί τη θεραπεία για το καλό των ασθενών, ότι δεν θα δώσει σε κανέναν θανατηφόρο φάρμακο, ακόμα κι αν του το ζητήσουν, και ότι θα κρατά μυστικό ό,τι δει ή ακούσει για τη ζωή τους. Η γνωστή φράση «πρώτα να μη βλάψεις» δεν βρίσκεται αυτούσια στον Όρκο, αλλά στις «Επιδημίες»: ο γιατρός πρέπει «να ωφελεί ή τουλάχιστον να μη βλάπτει».",
        "The best-known text in the Corpus is the Oath. The physician swears by Apollo the healer, Asclepius, Hygieia and Panacea that he will use treatment for the benefit of the sick, that he will give no one a deadly drug even if asked, nor a woman a pessary to cause abortion, that he will not cut for the stone but leave that to specialists, and that he will keep secret whatever he sees or hears about patients' lives. The Oath may reflect the views of a particular group rather than all Greek doctors, and its date is uncertain. The famous phrase 'first, do no harm' (primum non nocere) is not in the Oath at all; the closest ancient wording is in the Epidemics (1.11): the physician must 'help, or at least not harm' (ὠφελέειν ἢ μὴ βλάπτειν). Modern versions of the Oath, such as the World Medical Association's Declaration of Geneva (1948), are still sworn by medical graduates.", [6, 7]),
      P("Το 430 π.Χ., στη διάρκεια του Πελοποννησιακού πολέμου, ένας τρομερός λοιμός χτύπησε την Αθήνα, που ήταν γεμάτη πρόσφυγες από την ύπαιθρο. Πέθανε ίσως το ένα τέταρτο του πληθυσμού, ανάμεσά τους και ο Περικλής. Ο ιστορικός Θουκυδίδης, που αρρώστησε και ο ίδιος, περιέγραψε τα συμπτώματα με ιπποκρατική ακρίβεια, «για να μπορεί να τα αναγνωρίσει κανείς, αν ξαναπέσει». Παρατήρησε επίσης ότι όσοι γιατρεύονταν δεν αρρώσταιναν δεύτερη φορά, μια από τις πρώτες περιγραφές της ανοσίας.",
        "In 430 BC, during the Peloponnesian War, a terrible epidemic (λοιμός, 'plague') struck Athens, which was crowded with refugees from the countryside behind the Long Walls. Perhaps a quarter to a third of the population died, among them Pericles in 429 BC. The historian Thucydides, who fell ill himself and recovered, described the symptoms with Hippocratic precision, 'so that anyone may recognise it if it ever breaks out again' (2.48), and noted that the physicians died in greatest numbers because they were most in contact with the sick. He also observed that those who recovered did not catch it a second time, at least not fatally (2.51), one of the earliest descriptions of acquired immunity. What the disease was is still debated; ancient DNA from a mass grave in the Kerameikos has been read as pointing to typhoid fever, but measles, smallpox and others have been proposed.", [8, 9]),
    ]),
  ],
  grammar=[
    G("B2", "Indefinite relatives: ό,τι, όποιος, όσος + subjunctive", "«Ό,τι δει ή ακούσει»",
      "Relatives referring to something not yet known take the subjunctive: ό,τι δει 'whatever he may see', όποιος έρθει 'whoever comes'. Note the comma in ό,τι 'whatever', which distinguishes it from ότι 'that'.",
      [("θα κρατά μυστικό ό,τι δει ή ακούσει", "he will keep secret whatever he sees or hears"),
       ("Δεν θα δώσει θανατηφόρο φάρμακο, ακόμα κι αν του το ζητήσουν.", "He will give no deadly drug, even if they ask him for it.")]),
    G("B2", "θα + present vs θα + aorist", "Εξακολουθητικός και στιγμιαίος μέλλοντας",
      "θα + present stem describes a continuing or repeated future (θα χρησιμοποιεί 'will (always) use', θα κρατά 'will keep'), θα + aorist stem a single complete event (θα δώσει 'will give', θα κυριαρχήσει 'will come to dominate'). Oaths and promises about lasting conduct naturally use the continuous form.",
      [("Ο γιατρός ορκίζεται ότι θα χρησιμοποιεί τη θεραπεία για το καλό των ασθενών.", "The physician swears he will (always) use treatment for the patients' good."),
       ("Η θεωρία θα κυριαρχήσει για δύο χιλιάδες χρόνια.", "The theory will come to dominate for two thousand years.")]),
  ],
  terms=[
    T("το σύγγραμμα", "treatise, written work", "Επιστημονικό ή φιλοσοφικό βιβλίο.", "A scholarly or scientific written work."),
    T("η επιληψία", "epilepsy", "Νευρολογική πάθηση με κρίσεις σπασμών.", "A neurological condition with seizures."),
    T("η πρόγνωση", "prognosis", "Η πρόβλεψη της πορείας μιας αρρώστιας.", "Predicting the course of an illness."),
    T("ο χυμός", "humour; juice", "Στην αρχαία ιατρική, ένα από τα τέσσερα υγρά του σώματος.", "In ancient medicine, one of the four bodily fluids."),
    T("η χολή", "bile", "Υγρό που παράγει το συκώτι· «μαύρη χολή» = μελαγχολία.", "A fluid made by the liver; 'black bile' = melancholy."),
    T("ο λοιμός", "plague, epidemic", "Μεγάλη, θανατηφόρα επιδημία.", "A great deadly epidemic."),
    T("η ανοσία", "immunity", "Η αντίσταση του οργανισμού σε μια αρρώστια.", "The body's resistance to a disease."),
    T("θανατηφόρος", "deadly, lethal", "Που προκαλεί θάνατο.", "Causing death."),
  ],
  questions=[
    Q("Ποιος έγραψε την «Ιπποκρατική Συλλογή»;", ["Διάφοροι γιατροί σε διάφορες εποχές", "Μόνο ο Ιπποκράτης", "Ο Πλάτωνας", "Ο Γαληνός"], 0, "About sixty treatises by different authors."),
    Q("Τι υποστηρίζει το «Περί ιερής νούσου»;", ["Ότι η επιληψία έχει φυσική αιτία", "Ότι η επιληψία στέλνεται από τους θεούς", "Ότι η επιληψία θεραπεύεται με μαγεία", "Ότι η επιληψία δεν υπάρχει"], 0, "It is no more divine than other diseases."),
    Q("Πού βρίσκεται η φράση «να ωφελεί ή να μη βλάπτει»;", ["Στις «Επιδημίες»", "Στον «Όρκο»", "Στον Θουκυδίδη", "Στον Όμηρο"], 0, "Epidemics 1.11, not the Oath."),
    Q("Τι παρατήρησε ο Θουκυδίδης για όσους γιατρεύτηκαν από τον λοιμό;", ["Ότι δεν αρρώσταιναν δεύτερη φορά", "Ότι πέθαιναν αργότερα", "Ότι έγιναν γιατροί", "Ότι έφυγαν από την Αθήνα"], 0, "An early description of immunity (2.51)."),
  ],
  vocab=["ελάχιστα", "γιατρός", "ηλικία", "διάσημος", "αναφέρω", "καινοτομία", "πεποίθηση", "αρρώστια", "θεϊκός", "ιερός", "θεραπεία", "ειρωνεία", "άγνοια", "σημασία", "ασθενής", "πυρετός", "σφυγμός", "κλίμα", "επηρεάζω", "υγεία", "ισορροπία", "λανθασμένος", "ορκίζομαι", "φάρμακο", "μυστικός", "βλάπτω", "ωφελώ", "πρόσφυγας", "σύμπτωμα", "γιατρεύομαι"],
  sources=[
    SRC("Plato, Protagoras 311b–c and Phaedrus 270c (Hippocrates)."),
    SRC("Jouanna, J. (1999). Hippocrates. Trans. M. B. DeBevoise. Baltimore: Johns Hopkins University Press."),
    SRC("Hippocrates, On the Sacred Disease 1–2 and 17 (the brain as organ of thought)."),
    SRC("Nutton, V. (2013). Ancient Medicine. 2nd ed. London: Routledge."),
    SRC("Hippocrates, Epidemics 1 and 3 (case histories); Airs, Waters, Places; On the Nature of Man 4 (the four humours)."),
    SRC("The Hippocratic Oath, trans. L. Edelstein (1943). The Hippocratic Oath: Text, Translation and Interpretation. Baltimore: Johns Hopkins Press."),
    SRC("Hippocrates, Epidemics 1.11 (“to help, or at least not to harm”)."),
    SRC("Thucydides, History 2.47–54 (the plague of Athens)."),
    SRC("Papagrigorakis, M. J. et al. (2006). “DNA examination of ancient dental pulp incriminates typhoid fever as a probable cause of the Plague of Athens”. International Journal of Infectious Diseases 10: 206–214."),
  ]))

# 4.4 culture
CH.append(dict(id="e4-theatre", theme="culture", el="Το θέατρο: τραγωδία, κωμωδία και πόλη", title="Theatre: tragedy, comedy and the city", dates="534–322 π.Χ.",
  image="comic-mask",
  summary_en="How Athenian drama grew out of the festival of Dionysus, how plays were funded and judged, what Aeschylus, Sophocles, Euripides and Aristophanes put on stage, and why the theatre of Epidaurus still carries a whisper to the back row.",
  sections=[
    S("dionysia", "Μια γιορτή για τον Διόνυσο", "A festival for Dionysus", [
      P("Το θέατρο γεννήθηκε στην Αθήνα μέσα από τη λατρεία του Διονύσου, του θεού του κρασιού και της έκστασης. Κάθε άνοιξη, στα Μεγάλα Διονύσια, η πόλη οργάνωνε θεατρικούς αγώνες. Σύμφωνα με την παράδοση, ο πρώτος νικητής, γύρω στο 534 π.Χ., ήταν ο Θέσπις, ο οποίος ξεχώρισε από τον χορό έναν ηθοποιό που μιλούσε μαζί του. Από το όνομά του λέμε ακόμα σήμερα «το άρμα του Θέσπιδος» για έναν περιοδεύοντα θίασο, και τα αγγλικά ονομάζουν τους ηθοποιούς thespians. Αργότερα ο Αισχύλος πρόσθεσε δεύτερο ηθοποιό και ο Σοφοκλής τρίτο.",
        "Theatre was born in Athens out of the worship of Dionysus, god of wine, ecstasy and transformation. Every spring, at the City (Great) Dionysia, the city held dramatic competitions in the theatre of Dionysus on the south slope of the Acropolis. According to tradition, the first victor, around 534 BC, was Thespis, who set one actor apart from the chorus to speak with it; Aristotle's Poetics (1449a) is our main source for the early stages, though much of it is reconstruction. From his name Greek still speaks of 'the cart of Thespis' for a touring company, and English calls actors 'thespians'. Later Aeschylus added a second actor and Sophocles a third; all roles, including women's, were played by men in masks, which allowed three actors to play many parts.", [1, 2]),
      P("Τα έξοδα της παράστασης τα πλήρωνε ένας πλούσιος πολίτης, ο «χορηγός», ως ένα είδος φόρου προς την πόλη. Ήταν μεγάλη τιμή: ο νεαρός Περικλής, για παράδειγμα, ήταν χορηγός των «Περσών» του Αισχύλου, το 472 π.Χ. Στους αγώνες συμμετείχαν τρεις τραγικοί ποιητές, με τέσσερα έργα ο καθένας, και κριτές που κληρώνονταν έβγαζαν τον νικητή. Αργότερα η πόλη έδινε στους φτωχούς πολίτες και χρήματα για το εισιτήριο, τα «θεωρικά».",
        "The cost of a production was paid by a wealthy citizen, the chorēgos, as a kind of tax to the city (a 'liturgy'); the word survives in modern Greek χορηγός 'sponsor'. It was a great honour: the young Pericles, for example, was chorēgos for Aeschylus' Persians in 472 BC, the oldest surviving Greek play, which shows the Persian court learning of the defeat at Salamis. Three tragic poets competed each year, each with four plays (three tragedies and a satyr play), and judges chosen by lot, one from each tribe, decided the winner. Later the city also gave poor citizens money for their seat, the theōrika, which Demosthenes called 'the glue of the democracy' (according to a later source).", [2, 3]),
    ]),
    S("tragedy", "Τρεις τραγικοί και ένας κωμικός", "Three tragedians and one comic poet", [
      P("Από τις εκατοντάδες τραγωδίες που γράφτηκαν, σώζονται ολόκληρες μόνο τριάντα δύο περίπου, όλες από τρεις ποιητές. Ο Αισχύλος, που είχε πολεμήσει στον Μαραθώνα, έγραψε την «Ορέστεια», όπου η εκδίκηση αντικαθίσταται στο τέλος από ένα δικαστήριο. Ο Σοφοκλής, στον «Οιδίποδα Τύραννο» και στην «Αντιγόνη», έδειξε ανθρώπους που συγκρούονται με τη μοίρα, τους νόμους και τη συνείδησή τους. Ο Ευριπίδης, στη «Μήδεια» και στις «Τρωάδες», έδωσε φωνή σε γυναίκες, σκλάβους και θύματα του πολέμου.",
        "Of the hundreds of tragedies written, only about thirty-two survive complete, all by three poets (seven by Aeschylus, seven by Sophocles and seventeen or eighteen under Euripides' name, plus the disputed Rhesus). Aeschylus, who had fought at Marathon and mentioned only that on his epitaph, wrote the Oresteia (458 BC), the only surviving trilogy, in which the cycle of blood revenge is replaced at the end by a court, the Areopagus, founded by Athena. Sophocles, in Oedipus the King and Antigone, showed people in conflict with fate, with the laws of the state and with their own conscience. Euripides, in Medea and The Trojan Women (415 BC, the year after Athens massacred the men of Melos), gave voice to women, slaves and the victims of war, and was often thought shocking; he won only four or five victories in his lifetime but became the most read tragedian after his death.", [4, 5]),
      P("Η κωμωδία ήταν πιο ελεύθερη. Ο Αριστοφάνης σατίριζε τους πολιτικούς της εποχής με το όνομά τους, ακόμα και τον ισχυρό Κλέωνα, και κορόιδευε τον Σωκράτη και τον Ευριπίδη. Στη «Λυσιστράτη», το 411 π.Χ., οι γυναίκες της Αθήνας και της Σπάρτης κάνουν απεργία από τον έρωτα, για να αναγκάσουν τους άντρες να σταματήσουν τον πόλεμο. Το ότι μια πόλη σε πόλεμο επέτρεπε τέτοια έργα δείχνει πόση ελευθερία λόγου, η «παρρησία», υπήρχε στην Αθήνα.",
        "Comedy was freer. Aristophanes satirised the politicians of the day by name, even the powerful Cleon, who apparently prosecuted him for it, and mocked Socrates in the Clouds (423 BC) and Euripides in the Frogs (405 BC). In Lysistrata (411 BC), the women of Athens and Sparta go on a sex strike to force the men to stop the war. That a city at war allowed such plays shows how much freedom of speech, parrhēsia, existed in Athens, though it had limits, and attempts were made at times to restrict mockery by name. Plato later suggested that the caricature in the Clouds helped create the prejudice that led to Socrates' trial (Apology 18d, 19c).", [5, 6]),
    ]),
    S("epidaurus", "Το θέατρο της Επιδαύρου", "The theatre of Epidaurus", [
      P("Τα πρώτα θέατρα ήταν απλές πλαγιές λόφων με ξύλινα καθίσματα. Τον 4ο αιώνα π.Χ. άρχισαν να χτίζονται πέτρινα θέατρα. Το πιο φημισμένο είναι της Επιδαύρου, στο ιερό του θεού της ιατρικής Ασκληπιού. Χωρά περίπου δεκατρείς με δεκατέσσερις χιλιάδες θεατές, και η ακουστική του είναι τόσο καλή, ώστε από τις πιο ψηλές σειρές ακούγεται ένα σπίρτο που ανάβει στην ορχήστρα. Ερευνητές έχουν δείξει ότι τα σκαλοπάτια λειτουργούν σαν φίλτρο: απορροφούν τους χαμηλούς θορύβους και αντανακλούν τις φωνές.",
        "The first theatres were simple hillsides with wooden seats; the theatre of Dionysus in Athens was rebuilt in stone only in the 330s BC under Lycurgus. Stone theatres spread in the fourth century BC. The most famous is that of Epidaurus, in the sanctuary of the healing god Asclepius, attributed by Pausanias to Polykleitos (the Younger) and admired by him above all others for its harmony and beauty (2.27.5). It seats about thirteen to fourteen thousand spectators, and its acoustics are so good that a match struck in the orchestra is said to be heard in the highest rows. Researchers at the Georgia Institute of Technology (2007) showed that the rows of limestone seats act as an acoustic filter, damping low-frequency background noise such as the murmur of the audience while reflecting the higher frequencies of the actors' voices. Since 1955 the Epidaurus Festival has staged ancient drama there every summer.", [7, 8]),
    ]),
  ],
  grammar=[
    G("B2", "Nominalised clauses: το ότι, το να", "Ονοματοποιημένες προτάσεις",
      "A whole clause can become the subject or object of a sentence when preceded by the neuter article: Το ότι μια πόλη σε πόλεμο επέτρεπε τέτοια έργα δείχνει... 'The fact that a city at war allowed such plays shows...'. το να + verb names an activity: Το να γράφεις κωμωδίες ήταν επικίνδυνο 'Writing comedies was dangerous'.",
      [("Το ότι επέτρεπε τέτοια έργα δείχνει πόση ελευθερία υπήρχε.", "The fact that it allowed such plays shows how much freedom there was."),
       ("Το να σατιρίζεις τον Κλέωνα ήθελε θάρρος.", "Satirising Cleon took courage.")]),
    G("B2", "The passive present participle in -όμενος", "Μετοχή παθητικού ενεστώτα",
      "Learned and formal Greek uses present passive participles in -όμενος, -ούμενος, -ώμενος as adjectives: ο λεγόμενος 'the so-called', τα παριστανόμενα έργα 'the plays performed', τα σωζόμενα κείμενα 'the surviving texts'. In everyday speech a relative clause is more usual: τα κείμενα που σώζονται.",
      [("τα σωζόμενα έργα του Αισχύλου", "the surviving works of Aeschylus"),
       ("ο λεγόμενος «χορηγός»", "the so-called chorēgos")]),
  ],
  terms=[
    T("η τραγωδία", "tragedy", "Θεατρικό έργο με σοβαρό θέμα και συνήθως τραγικό τέλος.", "A serious play, usually ending in catastrophe."),
    T("η κωμωδία", "comedy", "Θεατρικό έργο που προκαλεί γέλιο και σατιρίζει.", "A play that makes people laugh and satirises."),
    T("ο χορός", "chorus; dance", "Στο αρχαίο θέατρο, η ομάδα που τραγουδούσε και χόρευε.", "In ancient theatre, the group that sang and danced."),
    T("ο χορηγός", "chorēgos; sponsor", "Ο πλούσιος που πλήρωνε μια παράσταση· σήμερα ο χρηματοδότης.", "The wealthy citizen who funded a play; today a sponsor."),
    T("η παρρησία", "freedom of speech, frankness", "Το δικαίωμα και το θάρρος να λέει κανείς ελεύθερα τη γνώμη του.", "The right and courage to speak one's mind."),
    T("η ακουστική", "acoustics", "Ο τρόπος που ακούγεται ο ήχος σε έναν χώρο.", "How sound carries in a space."),
    T("η ορχήστρα", "orchestra (theatre floor)", "Ο κυκλικός χώρος μπροστά στη σκηνή, όπου χόρευε ο χορός.", "The circular dancing floor in front of the stage."),
    T("σατιρίζω", "to satirise", "Κοροϊδεύω κάποιον για να δείξω τα ελαττώματά του.", "To mock in order to expose faults."),
  ],
  questions=[
    Q("Από ποια γιορτή γεννήθηκε το θέατρο;", ["Από τα Μεγάλα Διονύσια", "Από τους Ολυμπιακούς αγώνες", "Από τα Παναθήναια", "Από τα Χριστούγεννα"], 0, "The festival of Dionysus."),
    Q("Ποιος πλήρωνε τα έξοδα μιας παράστασης;", ["Ο χορηγός", "Ο ποιητής", "Οι θεατές", "Ο βασιλιάς"], 0, "A wealthy citizen, as a liturgy."),
    Q("Τι κάνουν οι γυναίκες στη «Λυσιστράτη»;", ["Απεργία από τον έρωτα για να σταματήσει ο πόλεμος", "Πολεμούν στη Σπάρτη", "Γράφουν τραγωδίες", "Ψηφίζουν στην Εκκλησία"], 0, "Aristophanes, 411 BC."),
    Q("Γιατί ακούγονται τόσο καλά οι φωνές στην Επίδαυρο;", ["Τα σκαλοπάτια απορροφούν τους χαμηλούς θορύβους και αντανακλούν τις φωνές", "Υπάρχουν μεγάφωνα", "Οι ηθοποιοί φώναζαν πολύ", "Το θέατρο είναι πολύ μικρό"], 0, "Georgia Tech study, 2007."),
  ],
  vocab=["λατρεία", "έκσταση", "θεατρικός", "αγώνας", "ξεχωρίζω", "ηθοποιός", "παράσταση", "τιμή", "κριτής", "εισιτήριο", "σώζομαι", "ολόκληρος", "εκδίκηση", "συγκρούομαι", "μοίρα", "συνείδηση", "φωνή", "θύμα", "κοροϊδεύω", "απεργία", "αναγκάζω", "ελευθερία", "κάθισμα", "φημισμένος", "χωρώ", "σπίρτο", "σκαλοπάτι", "θόρυβος", "αντανακλώ"],
  sources=[
    SRC("Aristotle, Poetics 1449a (the origins of tragedy and the number of actors)."),
    SRC("Csapo, E. & Slater, W. J. (1995). The Context of Ancient Drama. Ann Arbor: University of Michigan Press."),
    SRC("Plutarch, Life of Pericles 9 and Life of Nicias 3 (the theōrika); IG II² 2318 (the didascalic record: Pericles chorēgos in 472 BC)."),
    SRC("Easterling, P. E. (ed.) (1997). The Cambridge Companion to Greek Tragedy. Cambridge University Press."),
    SRC("Taplin, O. (1978). Greek Tragedy in Action. London: Methuen; Aristophanes, Lysistrata, Clouds, Frogs."),
    SRC("Plato, Apology 18d and 19c (the Clouds and the prejudice against Socrates)."),
    SRC("Pausanias, Description of Greece 2.27.5 (the theatre of Epidaurus)."),
    SRC("Declercq, N. F. & Dekeyser, C. S. A. (2007). “Acoustic diffraction effects at the Hellenistic amphitheater of Epidaurus: seat rows responsible for the marvelous acoustics”. Journal of the Acoustical Society of America 121: 2011–2022."),
  ]))

# 4.5 language
CH.append(dict(id="e4-historians", theme="language", el="Ηρόδοτος και Θουκυδίδης: πώς γεννήθηκε η ιστορία", title="Herodotus and Thucydides: how history was born", dates="περ. 440–400 π.Χ.",
  image="historians",
  summary_en="Two writers, two dialects, two methods: Herodotus' Ionic 'inquiry' into the Persian Wars and Thucydides' austere Attic analysis of the Peloponnesian War, and how the word ἱστορία came to mean 'history'.",
  sections=[
    S("herodotus", "Ο Ηρόδοτος και η «ιστορίη»", "Herodotus and the 'inquiry'", [
      P("Ο Ηρόδοτος γεννήθηκε στην Αλικαρνασσό της Μικράς Ασίας, γύρω στο 484 π.Χ. Το έργο του αρχίζει με μια πρόταση που έγινε διάσημη: παρουσιάζει την «ιστορίη» του, για να μην ξεχαστούν με τον καιρό όσα έκαναν οι άνθρωποι, και για να μη χάσουν τη φήμη τους τα μεγάλα έργα Ελλήνων και βαρβάρων, και κυρίως για ποιον λόγο πολέμησαν μεταξύ τους. Η λέξη «ιστορίη» σήμαινε τότε «έρευνα», «αυτό που μαθαίνει κανείς ρωτώντας». Χάρη στον Ηρόδοτο απέκτησε τη σημασία που έχει σήμερα.",
        "Herodotus was born in Halicarnassus (modern Bodrum) in Asia Minor around 484 BC, a Greek city under Persian rule, and he lived for a time in Athens and died, probably, at Thurii in southern Italy. His work begins with a sentence that became famous: he presents his historiē 'so that what people have done may not be erased by time, and that great and marvellous deeds, some shown by Greeks and some by barbarians, may not lose their fame, and above all for what reason they fought each other'. The word historiē then meant 'inquiry', 'what one learns by asking' (from ἵστωρ, 'one who knows, a witness'). Thanks to Herodotus it acquired the meaning it has today; Cicero called him 'the father of history' (On the Laws 1.5).", [1, 2]),
      P("Ο Ηρόδοτος ταξίδεψε στην Αίγυπτο, στη Βαβυλώνα, στη Σκυθία, και ρωτούσε ιερείς, ναυτικούς και απλούς ανθρώπους. Καταγράφει ήθη και έθιμα, μύθους και ανέκδοτα, και συχνά δίνει πολλές εκδοχές για το ίδιο γεγονός, αφήνοντας τον αναγνώστη να κρίνει. «Εγώ οφείλω να λέω όσα λέγονται», γράφει, «αλλά δεν είμαι υποχρεωμένος να τα πιστεύω όλα.» Έγραψε στην ιωνική διάλεκτο, και τα κείμενά του διαβάζονταν δημόσια, σαν μια μεγάλη αφήγηση.",
        "Herodotus travelled to Egypt, Babylon and Scythia (or claims to have done), and questioned priests, sailors and ordinary people. He records customs and manners, myths and anecdotes, and often gives several versions of the same event, leaving the reader to judge. 'I am obliged to report what is said,' he writes, 'but I am not at all obliged to believe it all, and let this saying hold for my whole account' (7.152). He was long mocked as the 'father of lies', and some of his stories are certainly wrong, but archaeology and Near Eastern records have often vindicated him, and his curiosity about other peoples makes him also the first ethnographer. He wrote in the Ionic dialect, the language of early prose and science, and his work was, according to later tradition, read aloud in public, like a great story.", [2, 3]),
    ]),
    S("thucydides", "Ο Θουκυδίδης και το «κτήμα ες αιεί»", "Thucydides and the 'possession for ever'", [
      P("Ο Θουκυδίδης, Αθηναίος, ήταν στρατηγός στον Πελοποννησιακό πόλεμο. Όταν το 424 π.Χ. δεν κατάφερε να σώσει την Αμφίπολη από τους Σπαρτιάτες, οι Αθηναίοι τον εξόρισαν. Τα είκοσι χρόνια της εξορίας τα αφιέρωσε στη συγγραφή της ιστορίας του πολέμου, που άρχισε, όπως λέει, αμέσως μόλις ξέσπασε, γιατί κατάλαβε ότι θα είναι ο πιο σημαντικός πόλεμος που έγινε ποτέ. Το έργο του σταματά απότομα στο 411 π.Χ., χωρίς να έχει ολοκληρωθεί.",
        "Thucydides, an Athenian, was a general in the Peloponnesian War. When in 424 BC he failed to save Amphipolis from the Spartan Brasidas, the Athenians exiled him. He devoted the twenty years of exile to writing the history of the war, which he began, he says, as soon as it broke out, because he realised it would be the greatest war there had ever been (1.1). Exile, he notes, allowed him to talk to both sides (5.26). His work breaks off abruptly in 411 BC, in mid-sentence, unfinished; Xenophon's Hellenica picks up the story where he stops.", [4, 5]),
      P("Η μέθοδός του ήταν πολύ πιο αυστηρή από του Ηροδότου. Απορρίπτει τους θεούς ως αιτία των γεγονότων και τους μύθους ως πηγή. Ελέγχει τις μαρτυρίες, γιατί, όπως παρατηρεί, οι αυτόπτες μάρτυρες δεν λένε τα ίδια για τα ίδια γεγονότα, αλλά ο καθένας ανάλογα με τη συμπάθειά του ή τη μνήμη του. Ξεχωρίζει τις πραγματικές αιτίες του πολέμου, τον φόβο της Σπάρτης για τη δύναμη της Αθήνας, από τις αφορμές. Γράφει, λέει, όχι για να ευχαριστήσει το κοινό της στιγμής, αλλά για να αφήσει ένα «κτῆμα ἐς αἰεί», ένα απόκτημα για πάντα.",
        "His method was much stricter than Herodotus'. He rejects the gods as causes of events and myths as evidence. He checks testimony because, as he observes, eyewitnesses do not say the same things about the same events, but each according to his sympathy or his memory (1.22). He distinguishes the 'truest cause' of the war, Sparta's fear of the growth of Athenian power, from the stated grievances and pretexts (1.23), a distinction historians and political scientists still use; the modern phrase 'Thucydides trap' borrows it. He writes, he says, not to please the audience of the moment but to leave 'a possession for all time' (κτῆμα ἐς αἰεί, 1.22), because human nature being what it is, similar things will happen again. The speeches in his work, he admits, are not verbatim: he wrote what each speaker would most likely have said, keeping as close as possible to the general sense.", [4, 6]),
    ]),
    S("attic", "Η αττική πεζογραφία", "Attic prose", [
      P("Ο Θουκυδίδης έγραψε στην αττική διάλεκτο, σε ένα ύφος πυκνό και δύσκολο, γεμάτο αφηρημένες έννοιες και αντιθέσεις. Ακόμα και οι αρχαίοι αναγνώστες τον έβρισκαν δυσνόητο. Τον 4ο αιώνα π.Χ. η αττική διάλεκτος έγινε, με τους ρήτορες, όπως ο Λυσίας και ο Δημοσθένης, και με φιλοσόφους, όπως ο Πλάτωνας, η γλώσσα της ελληνικής πεζογραφίας. Πάνω της θα στηριχτεί αργότερα η «κοινή», η γλώσσα όλου του ελληνιστικού κόσμου.",
        "Thucydides wrote in the Attic dialect, in a dense, difficult style, full of abstract nouns and antitheses, and with an early Attic flavour (he still writes -σσ- where later Attic has -ττ-, e.g. θάλασσα rather than θάλαττα). Even ancient readers found him hard: Dionysius of Halicarnassus complained that some passages needed a commentary. In the fourth century BC, with orators such as Lysias, Isocrates and Demosthenes, and philosophers such as Plato, Attic became the language of Greek prose, and its influence was helped by rhetoric, the art of persuasion brought to Athens by Gorgias of Leontini in 427 BC. On it the Koine, the language of the whole Hellenistic world, would later be based, and many words of modern Greek, in their form, are Attic rather than Ionic: compare Attic θάλαττα with modern θάλασσα, however, a reminder that the Koine also kept Ionic features.", [6, 7]),
    ]),
  ],
  grammar=[
    G("B2", "Negative purpose: για να μη(ν)", "Αρνητικός σκοπός",
      "A negative purpose uses μη(ν), not δεν: για να μην ξεχαστούν 'so that they may not be forgotten', για να μη χάσουν. The same μη is used with all subjunctives: να μη φύγεις, ας μη μιλήσει. μην keeps ν before vowels and κ, π, τ, μπ, ντ, γκ, ξ, ψ, τσ, τζ.",
      [("για να μην ξεχαστούν με τον καιρό όσα έκαναν οι άνθρωποι", "so that what people did may not be forgotten in time"),
       ("για να μη χάσουν τη φήμη τους τα μεγάλα έργα", "so that great deeds may not lose their fame")]),
    G("B2", "ανάλογα με, χάρη σε, εξαιτίας: prepositional phrases", "Εμπρόθετοι προσδιορισμοί αιτίας και τρόπου",
      "ανάλογα με + acc. 'depending on, according to': ανάλογα με τη συμπάθειά του. χάρη σε + acc. 'thanks to' (positive cause): χάρη στον Ηρόδοτο. εξαιτίας + gen. 'because of' (often negative): εξαιτίας της ήττας.",
      [("ο καθένας ανάλογα με τη συμπάθειά του", "each according to his sympathy"),
       ("Χάρη στον Ηρόδοτο η λέξη απέκτησε τη σημερινή της σημασία.", "Thanks to Herodotus the word acquired its present meaning.")]),
  ],
  terms=[
    T("η ιστορία", "history; story", "Αρχικά «έρευνα»· σήμερα η μελέτη του παρελθόντος.", "Originally 'inquiry'; now the study of the past."),
    T("ο βάρβαρος", "barbarian, non-Greek", "Για τους αρχαίους, όποιος δεν μιλούσε ελληνικά· σήμερα «άγριος, απολίτιστος».", "For the ancients, anyone not speaking Greek; today 'savage'."),
    T("η εκδοχή", "version", "Ένας από τους τρόπους να διηγηθεί ή να ερμηνεύσει κανείς κάτι.", "One way of telling or interpreting something."),
    T("ο αυτόπτης μάρτυρας", "eyewitness", "Αυτός που είδε ο ίδιος ένα γεγονός.", "Someone who saw an event personally."),
    T("η αφορμή", "pretext, occasion", "Το γεγονός που προκαλεί κάτι, χωρίς να είναι η βαθύτερη αιτία του.", "The trigger of something, as opposed to its deeper cause."),
    T("η εξορία", "exile", "Η υποχρεωτική απομάκρυνση από την πατρίδα.", "Forced removal from one's homeland."),
    T("η πεζογραφία", "prose", "Λόγος γραμμένος χωρίς μέτρο, σε αντίθεση με την ποίηση.", "Writing without metre, as opposed to poetry."),
    T("ο ρήτορας", "orator", "Αυτός που μιλά με τέχνη δημόσια για να πείσει.", "One who speaks skilfully in public to persuade."),
  ],
  questions=[
    Q("Τι σήμαινε αρχικά η λέξη «ιστορίη»;", ["Έρευνα", "Παραμύθι", "Πόλεμος", "Βιβλίο"], 0, "What one learns by asking."),
    Q("Τι έκανε ο Ηρόδοτος όταν υπήρχαν πολλές εκδοχές;", ["Τις κατέγραφε και άφηνε τον αναγνώστη να κρίνει", "Διάλεγε πάντα τη μία", "Τις έκρυβε", "Ρωτούσε το μαντείο"], 0, "Herodotus 7.152."),
    Q("Γιατί εξορίστηκε ο Θουκυδίδης;", ["Γιατί δεν έσωσε την Αμφίπολη", "Γιατί έγραψε κωμωδίες", "Γιατί ήταν Σπαρτιάτης", "Γιατί εξοστρακίστηκε"], 0, "In 424 BC."),
    Q("Ποια είναι, κατά τον Θουκυδίδη, η πραγματική αιτία του πολέμου;", ["Ο φόβος της Σπάρτης για τη δύναμη της Αθήνας", "Η Ωραία Ελένη", "Οι θεοί", "Ένας σεισμός"], 0, "Thucydides 1.23."),
  ],
  vocab=["πρόταση", "παρουσιάζω", "ξεχνιέμαι", "φήμη", "κυρίως", "έρευνα", "χάρη σε", "αποκτώ", "ναυτικός", "έθιμο", "ανέκδοτο", "γεγονός", "κρίνω", "οφείλω", "υποχρεωμένος", "διάλεκτος", "αφήγηση", "καταφέρνω", "εξορίζω", "αφιερώνω", "ξεσπώ", "απότομα", "ολοκληρώνω", "απορρίπτω", "μαρτυρία", "συμπάθεια", "ευχαριστώ", "πυκνός", "αφηρημένος", "δυσνόητος"],
  sources=[
    SRC("Herodotus, Histories, proem (1.0)."),
    SRC("Cicero, On the Laws 1.5 (pater historiae); Herodotus 7.152; Thomas, R. (2000). Herodotus in Context. Cambridge University Press."),
    SRC("Romm, J. (1998). Herodotus. New Haven: Yale University Press."),
    SRC("Thucydides, History 1.1, 4.104–107 and 5.26 (the war, Amphipolis, the exile)."),
    SRC("Xenophon, Hellenica 1.1.1 (continuing Thucydides)."),
    SRC("Thucydides, History 1.20–23 (method, the 'possession for ever', the truest cause); Hornblower, S. (1987). Thucydides. London: Duckworth."),
    SRC("Horrocks, G. (2010). Greek: A History of the Language and its Speakers. 2nd ed., ch. 2–3; Dionysius of Halicarnassus, On Thucydides 51."),
  ]))
