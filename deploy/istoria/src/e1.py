# Era 1 · Προϊστορία (περ. 300.000–2000 π.Χ.)
from common import P, S, G, T, Q, SRC

ERA = dict(id="prehistory", el="Προϊστορία", en="Prehistory", dates="περ. 300.000–2000 π.Χ.", dates_en="c. 300,000–2000 BC", level="B1+",
  intro_el="Πριν από τη γραφή, πριν από τις πόλεις και τους βασιλιάδες, ο ελλαδικός χώρος είχε ήδη μια ιστορία εκατοντάδων χιλιάδων χρόνων. Σε αυτή την ενότητα γνωρίζουμε τους πρώτους ανθρώπους, τα πρώτα χωριά και την πρώτη μεγάλη τέχνη του Αιγαίου.",
  intro_en="Before writing, before cities and kings, the land that is now Greece already had a history hundreds of thousands of years long. This part follows the first humans in the region, the first farming villages of Thessaly, the lake dwellers of Macedonia, the marble figures of the Cyclades and the traces that the earliest languages of the Aegean left in Greek. The Greek here is the simplest in the reader (around B1+), with the grammar notes covering the past tenses and dates you need for everything that follows.")

CH = []

# 1.1 politics / society
CH.append(dict(id="e1-villages", theme="politics", el="Τα πρώτα χωριά: Σέσκλο και Διμήνι", title="The first villages: Sesklo and Dimini", dates="περ. 7000–4000 π.Χ.",
  image="neolithic-sherd",
  summary_en="How farming reached Greece around 7000–6500 BC and how the villages of Thessaly, above all Sesklo and Dimini, organised their life without kings or palaces.",
  sections=[
    S("from-caves", "Από τις σπηλιές στα χωριά", "From caves to villages", [
      P("Για εκατοντάδες χιλιάδες χρόνια οι άνθρωποι στον ελλαδικό χώρο ζούσαν ως κυνηγοί και τροφοσυλλέκτες. Μετακινούνταν μαζί με τα ζώα που κυνηγούσαν και έβρισκαν καταφύγιο σε σπηλιές. Γύρω στο 7000 π.Χ. όμως έγινε μια από τις μεγαλύτερες αλλαγές στην ιστορία της ανθρωπότητας: οι άνθρωποι άρχισαν να καλλιεργούν σιτάρι και κριθάρι και να εκτρέφουν πρόβατα και κατσίκες. Αυτή η αλλαγή ονομάζεται «νεολιθική επανάσταση».",
        "For hundreds of thousands of years the people of the region that is now Greece lived as hunters and gatherers. They moved with the animals they hunted and sheltered in caves. Around 7000 BC (most scholars give a range of 7000–6500 BC) one of the greatest changes in human history took place: people began to grow wheat and barley and to raise sheep and goats. None of these plants or animals was native to Greece in domesticated form; they had been domesticated earlier in the Near East and arrived from Anatolia, across the Aegean islands or along the coasts. Ancient DNA shows that Greece's first farmers were closely related to the early farmers of north-western Anatolia, and that the farmers who later spread across Europe descend from Aegean populations like them. The phrase 'Neolithic Revolution' was made famous by the archaeologist V. Gordon Childe in the 1930s.", [1, 2]),
      P("Η γεωργία έκανε τους ανθρώπους να μείνουν σε ένα μέρος. Έχτισαν σπίτια, στην αρχή από ξύλα και λάσπη και αργότερα με πέτρινα θεμέλια και τοίχους από πλίνθους, δηλαδή από τούβλα λάσπης που ξεραίνονταν στον ήλιο. Η εύφορη πεδιάδα της Θεσσαλίας ήταν ιδανική για τις καλλιέργειες, και γι' αυτό εκεί έχουν βρεθεί εκατοντάδες νεολιθικοί οικισμοί. Στη Θεσσαλία τους λένε «μαγούλες», γιατί με τον καιρό τα ερείπια των σπιτιών, το ένα πάνω στο άλλο, σχημάτισαν χαμηλούς λόφους.",
        "Farming made people stay in one place. They built houses, at first of wood and mud and later with stone foundations and walls of mudbrick, that is, bricks of mud dried in the sun. The fertile plain of Thessaly was ideal for crops, which is why hundreds of Neolithic settlements have been found there. In Thessaly they are called magoules (singular magoula), because over time the ruins of houses, one built on top of another, formed low mounds. Archaeologists elsewhere call such mounds 'tells', from the Arabic word for a hill; each layer of a tell is a snapshot of one phase of the village, which is why they are so valuable for dating.", [1, 4]),
    ]),
    S("sesklo", "Σέσκλο: ένα από τα παλαιότερα χωριά της Ευρώπης", "Sesklo: one of Europe's oldest villages", [
      P("Το Σέσκλο, κοντά στον σημερινό Βόλο, είναι ένας από τους πιο γνωστούς νεολιθικούς οικισμούς της Ευρώπης. Οι πρώτοι αγρότες εγκαταστάθηκαν εκεί γύρω στο 6500 π.Χ. Στην εποχή της μεγαλύτερης ακμής του ο οικισμός είχε πιθανότατα μερικές χιλιάδες κατοίκους. Τον ανέσκαψε για πρώτη φορά ο αρχαιολόγος Χρήστος Τσούντας, στις αρχές του 20ού αιώνα, και αργότερα, από το 1956, ο Δημήτριος Θεοχάρης.",
        "Sesklo, near the modern city of Volos, is one of the best-known Neolithic settlements in Europe. The first farmers settled there around 6500 BC (some pottery may be older still). At its height, in the Middle Neolithic of the late sixth millennium BC, the settlement probably had a few thousand inhabitants, which made it unusually large for its time. It was first excavated by the archaeologist Christos Tsountas in 1901–1902, and later, from 1956 onward, by Dimitrios Theocharis, who gave his name to the 'Sesklo culture', the Middle Neolithic culture of Thessaly.", [3, 4]),
      P("Οι κάτοικοι του Σέσκλου ήταν ικανοί τεχνίτες. Έφτιαχναν λεπτά πήλινα αγγεία, ζωγραφισμένα με κόκκινα γεωμετρικά σχέδια πάνω σε ανοιχτόχρωμο φόντο, και μικρά ειδώλια από πηλό. Στο ψηλότερο σημείο του οικισμού, την «ακρόπολη», υπήρχε ένα μεγάλο κτίριο με προθάλαμο και κύρια αίθουσα. Μερικοί αρχαιολόγοι το θεωρούν πρόγονο του «μεγάρου», του κτιρίου που χιλιάδες χρόνια αργότερα θα βρισκόταν στο κέντρο των μυκηναϊκών ανακτόρων.",
        "The people of Sesklo were skilled craftspeople. They made thin clay pots painted with red geometric patterns on a light background, and small clay figurines. On the highest point of the settlement, the 'acropolis', stood a large building with a porch and a main hall. Some archaeologists see it as an ancestor of the megaron, the hall-and-porch building that thousands of years later stood at the centre of the Mycenaean palaces; others think the resemblance is a coincidence of simple design, since a rectangular room with a porch is an obvious way to build. Either way, the building shows that the community could plan and build something larger than a family home.", [3, 4]),
    ]),
    S("dimini", "Διμήνι: τείχη και κοινωνία", "Dimini: walls and society", [
      P("Λίγα χιλιόμετρα πιο πέρα βρίσκεται το Διμήνι, όπου οι άνθρωποι εγκαταστάθηκαν γύρω στο 4800 π.Χ. Ο οικισμός περιβαλλόταν από αρκετούς ομόκεντρους πέτρινους περιβόλους. Παλαιότερα οι ερευνητές πίστευαν ότι ήταν τείχη για την άμυνα. Σήμερα πολλοί θεωρούν ότι οι περίβολοι μάλλον χώριζαν τις γειτονιές και τους χώρους εργασίας, αφού ήταν χαμηλοί και είχαν πολλά ανοίγματα.",
        "A few kilometres away lies Dimini, where people settled around 4800 BC, according to thermoluminescence dates on its pottery; for a while the two villages seem to have existed side by side. The settlement was surrounded by several concentric stone enclosure walls. Researchers used to think these were defensive walls, and the old textbook story had the 'Dimini people' conquering Sesklo. Today many think the enclosures more probably divided neighbourhoods and work areas, since they were low and had many openings; the excavator of the later seasons, Giorgos Hourmouziadis, argued strongly for this social reading.", [5, 6]),
      P("Αυτοί οι οικισμοί δεν είχαν βασιλιάδες ούτε ανάκτορα. Οι αρχαιολόγοι πιστεύουν ότι ήταν κοινότητες σχετικά ισότιμες, όπου οι οικογένειες μοιράζονταν τη γη και τη δουλειά. Οι επαφές με άλλους τόπους όμως ήταν ήδη πολλές: στο Διμήνι υπήρχε εργαστήριο για κοσμήματα από ένα θαλασσινό όστρακο, τον σπόνδυλο, και στη Θεσσαλία έχει βρεθεί οψιανός από τη Μήλο. Αυτό σημαίνει ότι τα αγαθά ταξίδευαν σε μεγάλες αποστάσεις.",
        "These settlements had no kings and no palaces. Archaeologists believe they were relatively egalitarian communities in which families shared land and labour, although some households may have stored more than others. Contacts with other places, however, were already many: Dimini had a workshop making ornaments from a marine shell, Spondylus, and ornaments of this kind travelled as far as central Europe; Melian obsidian has also been found in Thessaly. This means that goods, and with them ideas, travelled over long distances thousands of years before the first written records.", [6, 7]),
    ]),
  ],
  grammar=[
    G("B1", "The imperfect for habits and background", "Παρατατικός: συνήθεια και διάρκεια",
      "Greek uses the imperfect (παρατατικός) for repeated or ongoing actions in the past: what people used to do, or what was going on. Active verbs take -α endings on the present stem (ζούσαν, έφτιαχναν, κυνηγούσαν); passive and deponent verbs take -όμουν/-όταν/-ονταν (μετακινούνταν, ξεραίνονταν, περιβαλλόταν). A single completed event goes in the aorist instead: εγκαταστάθηκαν, έχτισαν.",
      [("Οι άνθρωποι ζούσαν ως κυνηγοί και τροφοσυλλέκτες.", "People lived (used to live) as hunters and gatherers."),
       ("Μετακινούνταν μαζί με τα ζώα.", "They moved (kept moving) with the animals."),
       ("Οι πρώτοι αγρότες εγκαταστάθηκαν εκεί γύρω στο 6500 π.Χ.", "The first farmers settled there around 6500 BC (one event: aorist).")]),
    G("B1", "Dates, centuries and 'around'", "Χρονολογίες και αιώνες",
      "π.Χ. (προ Χριστού) = BC, μ.Χ. (μετά Χριστόν) = AD. A year takes the neuter article because έτος is understood: το 6500 π.Χ., στο 4800 π.Χ. 'Around' is γύρω στο or περίπου. A century is an ordinal with αιώνας, usually written with a numeral and the ending: ο 20ός αιώνας, στις αρχές του 20ού αιώνα (genitive), τον 5ο αιώνα π.Χ. (accusative of time: 'in the 5th century').",
      [("Γύρω στο 7000 π.Χ. έγινε μια μεγάλη αλλαγή.", "Around 7000 BC a great change happened."),
       ("στις αρχές του 20ού αιώνα", "at the beginning of the 20th century"),
       ("από το 1956", "from 1956 on")]),
  ],
  terms=[
    T("η νεολιθική επανάσταση", "the Neolithic Revolution", "Η μεγάλη αλλαγή από το κυνήγι στη γεωργία και την κτηνοτροφία.", "The shift from hunting and gathering to farming and herding."),
    T("ο τροφοσυλλέκτης", "gatherer, forager", "Άνθρωπος που ζει μαζεύοντας φυτά και καρπούς, όχι καλλιεργώντας.", "Someone who lives by collecting wild plants rather than growing them."),
    T("ο οικισμός", "settlement", "Τόπος όπου μένουν μαζί πολλές οικογένειες· χωριό ή μικρή πόλη.", "A place where many families live together; a village or small town."),
    T("η πλίνθος", "mudbrick", "Τούβλο από λάσπη και άχυρο που ξεραίνεται στον ήλιο.", "A brick of mud and straw dried in the sun."),
    T("η μαγούλα", "tell, settlement mound", "Χαμηλός λόφος από ερείπια σπιτιών χτισμένων το ένα πάνω στο άλλο.", "A low mound formed by the ruins of houses built one on top of another."),
    T("η ακρόπολη", "acropolis, citadel", "Το ψηλότερο σημείο ενός οικισμού ή μιας πόλης.", "The highest, often fortified, point of a settlement or city."),
    T("ο περίβολος", "enclosure wall", "Τοίχος που περικλείνει έναν χώρο.", "A wall that encloses an area."),
    T("ο οψιανός", "obsidian", "Μαύρο ηφαιστειακό γυαλί· στο Αιγαίο βγαίνει κυρίως στη Μήλο.", "Black volcanic glass; in the Aegean it comes mainly from Melos."),
  ],
  questions=[
    Q("Τι άρχισαν να κάνουν οι άνθρωποι γύρω στο 7000 π.Χ.;", ["Να καλλιεργούν και να εκτρέφουν ζώα", "Να ζουν σε σπηλιές", "Να γράφουν", "Να χτίζουν ανάκτορα"], 0, "The Neolithic Revolution: wheat, barley, sheep and goats."),
    Q("Γιατί λέγονται «μαγούλες» οι θεσσαλικοί οικισμοί;", ["Γιατί τα ερείπια σχημάτισαν χαμηλούς λόφους", "Γιατί ήταν κοντά στη θάλασσα", "Γιατί είχαν μεγάλα τείχη", "Γιατί ήταν σε σπηλιές"], 0, "Layers of houses built on top of each other formed mounds."),
    Q("Ποια είναι η σημερινή εξήγηση για τους περιβόλους του Διμηνίου;", ["Μάλλον χώριζαν γειτονιές και χώρους εργασίας", "Ήταν σίγουρα τείχη για πόλεμο", "Ήταν τάφοι", "Ήταν κανάλια για νερό"], 0, "They were low and had many openings."),
    Q("Τι δείχνει ο οψιανός από τη Μήλο στη Θεσσαλία;", ["Ότι τα αγαθά ταξίδευαν μακριά", "Ότι στη Θεσσαλία υπήρχαν ηφαίστεια", "Ότι οι κάτοικοι ήταν βασιλιάδες", "Ότι υπήρχε γραφή"], 0, "Obsidian only comes from a few volcanic sources, so it proves exchange."),
  ],
  vocab=["καλλιεργώ", "εκτρέφω", "κυνηγός", "καταφύγιο", "αλλαγή", "θεμέλιο", "εύφορος", "πεδιάδα", "ερείπιο", "εγκαθίσταμαι", "ακμή", "τεχνίτης", "αγγείο", "πρόγονος", "περιβάλλω", "άμυνα", "ισότιμος", "μοιράζομαι", "αγαθό", "απόσταση"],
  sources=[
    SRC("“Neolithic Greece”, Wikipedia (overview of dates and sites).", "https://en.wikipedia.org/wiki/Neolithic_Greece"),
    SRC("Hofmanová, Z. et al. (2016). “Early farmers from across Europe directly descended from Neolithic Aegeans”. PNAS 113 (25): 6886–6891.", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4922144"),
    SRC("“Sesklo”, Wikipedia (excavation history: Tsountas 1901–02, Theocharis from 1956).", "https://en.wikipedia.org/wiki/Sesklo"),
    SRC("Perlès, C. (2001). The Early Neolithic in Greece: The First Farming Communities in Europe. Cambridge University Press."),
    SRC("“Dimini”, Wikipedia (thermoluminescence dates by Liritzis, coexistence with Sesklo).", "https://en.wikipedia.org/wiki/Dimini"),
    SRC("Hourmouziadis, G. (1979). Το νεολιθικό Διμήνι. Βόλος: Εταιρεία Θεσσαλικών Ερευνών."),
    SRC("Halstead, P. (1993). “Spondylus shell ornaments from late Neolithic Dimini, Greece: specialized manufacture or unequal accumulation?”. Antiquity 67: 603–609."),
  ]))

# 1.2 science / technology
CH.append(dict(id="e1-stone-age", theme="science", el="Οψιανός και πλοία: η τεχνολογία της Λίθινης Εποχής", title="Obsidian and boats: Stone Age technology", dates="περ. 210.000–6000 π.Χ.",
  image="obsidian",
  summary_en="The oldest human remains in Greece, a wall built in the last Ice Age, and the obsidian that proves people were sailing the Aegean thousands of years before farming.",
  sections=[
    S("first-humans", "Οι πρώτοι άνθρωποι", "The first humans", [
      P("Οι άνθρωποι ζουν στον ελλαδικό χώρο εδώ και πολύ περισσότερο απ' όσο φανταζόμαστε. Στο σπήλαιο Απήδημα της Μάνης βρέθηκαν, τη δεκαετία του 1970, δύο κρανία. Το 2019 μια ομάδα επιστημόνων με επικεφαλής την Ελληνίδα παλαιοανθρωπολόγο Κατερίνα Χαρβάτη ανακοίνωσε ότι το ένα είναι περίπου 210.000 ετών και ανήκει σε Homo sapiens, δηλαδή στο δικό μας είδος. Αν η χρονολόγηση είναι σωστή, πρόκειται για τον αρχαιότερο γνωστό σύγχρονο άνθρωπο έξω από την Αφρική.",
        "Humans have lived in the region far longer than we tend to imagine. In the Apidima cave in the Mani, two skulls were found in the 1970s. In 2019 a team led by the Greek palaeoanthropologist Katerina Harvati (University of Tübingen) announced that one of them, Apidima 1, is about 210,000 years old and belongs to Homo sapiens, our own species, while the other, Apidima 2, about 170,000 years old, has Neanderthal features. If the dating and identification are right, Apidima 1 is the oldest known modern human outside Africa, and its population was later replaced by Neanderthals. Not all specialists accept the identification, because the skull is only partly preserved and had to be reconstructed digitally.", [1]),
      P("Στο σπήλαιο της Θεόπετρας, κοντά στα Μετέωρα, οι αρχαιολόγοι βρήκαν έναν πέτρινο τοίχο που έκλεινε μεγάλο μέρος της εισόδου. Η χρονολόγηση έδειξε ότι χτίστηκε πριν από περίπου 23.000 χρόνια, στην πιο κρύα φάση της τελευταίας εποχής των παγετώνων. Μάλλον τον έχτισαν για να προστατευτούν από τον παγωμένο αέρα. Είναι μία από τις παλαιότερες γνωστές ανθρώπινες κατασκευές στον κόσμο.",
        "In Theopetra cave near Meteora, where excavations led by Nina Kyparissi-Apostolika began in 1987, archaeologists found a stone wall that closed off a large part of the entrance. Optically stimulated luminescence dating showed that it was built about 23,000 years ago, during the Last Glacial Maximum, the coldest phase of the last Ice Age. It was probably built as protection against the freezing wind. It is often called the oldest human-built structure in Greece and one of the oldest known in the world; the stronger claim, 'the oldest in the world', is repeated in the press but cannot be proved. Theopetra was used almost continuously from the Middle Palaeolithic to the Neolithic.", [2, 3]),
    ]),
    S("obsidian", "Ο οψιανός της Μήλου και τα πρώτα ταξίδια", "Melian obsidian and the first voyages", [
      P("Πριν από τα μέταλλα, το πιο κοφτερό υλικό που είχαν οι άνθρωποι ήταν ο οψιανός, ένα μαύρο ηφαιστειακό γυαλί. Όταν τον χτυπούσαν με τέχνη, έβγαιναν λεπίδες κοφτερές σαν ξυράφι. Στο Αιγαίο ο οψιανός βρίσκεται κυρίως στη Μήλο. Και όμως, κομμάτια οψιανού της Μήλου βρέθηκαν στο σπήλαιο Φράγχθι στην Αργολίδα, σε στρώματα που είναι παλαιότερα από 11.000 π.Χ.",
        "Before metals, the sharpest material people had was obsidian, a black volcanic glass. When it was struck skilfully ('knapped'), it produced blades as sharp as a razor; obsidian edges are in fact sharper than steel scalpels. In the Aegean, obsidian is found mainly on Melos (there is a minor source on Giali near Nisyros). And yet pieces of Melian obsidian were found in Franchthi Cave in the Argolid, in layers of the end of the Upper Palaeolithic and the Mesolithic. Studies of the obsidian itself, including hydration dating, place the earliest of it more than 13,000 years ago. Franchthi was used by humans for more than 30,000 years, from the Upper Palaeolithic down to about 3000 BC.", [4, 5]),
      P("Η Μήλος ήταν νησί και τότε. Επομένως, για να φέρουν τον οψιανό στην Πελοπόννησο, οι άνθρωποι έπρεπε να ταξιδέψουν στη θάλασσα, πιθανώς με βάρκες από καλάμια ή κορμούς δέντρων. Αυτά είναι από τα αρχαιότερα στοιχεία για ναυσιπλοΐα στη Μεσόγειο. Οι κάτοικοι του Φράγχθι ψάρευαν επίσης μεγάλα ψάρια, όπως τόνους, κάτι που δείχνει ότι γνώριζαν καλά τη θάλασσα.",
        "Melos was an island then too, even though the sea level was much lower than today. So to bring obsidian to the Peloponnese people had to cross open water, probably in boats of reeds or hollowed logs; no boat of this age survives, so their form is a guess. This is among the earliest evidence for seafaring in the Mediterranean. In the Mesolithic layers at Franchthi, around 8000 BC, the bones of large fish such as tuna also appear, which suggests that the inhabitants knew the sea and its seasons well.", [4, 5]),
      P("Στο Φράγχθι φαίνεται και η μεγάλη αλλαγή της νεολιθικής εποχής. Στα πρώτα μισά της 7ης χιλιετίας π.Χ. εμφανίζονται εκεί σπόροι από σιτάρι και κριθάρι που δεν φύτρωναν άγρια στην περιοχή. Λίγο αργότερα εμφανίζονται και τα πρώτα πήλινα αγγεία. Η τεχνολογία της γεωργίας, όπως και ο οψιανός, ήρθε από τη θάλασσα.",
        "Franchthi also records the great change of the Neolithic. In the first half of the seventh millennium BC, seeds of wheat and barley appear there, of species that did not grow wild in the area, and AMS radiocarbon dates on the seeds themselves support this early date. A little later the first pottery appears. The excavator Catherine Perlès argued that these crops came by sea, with colonists sailing along the islands, rather than only overland around the northern Aegean. Farming, like obsidian, arrived by water.", [5, 6]),
    ]),
  ],
  grammar=[
    G("B1", "The passive aorist in -θηκα / -τηκα", "Παθητικός αόριστος σε -θηκα",
      "History writing is full of passive aorists: what was found, built, dated. The ending is -θηκα (-θηκες, -θηκε, -θήκαμε, -θήκατε, -θηκαν), sometimes -τηκα or -χτηκα after certain stems. Learn them with the active: βρίσκω → βρέθηκε, χτίζω → χτίστηκε, χρονολογώ → χρονολογήθηκε, ανακοινώνω → ανακοινώθηκε.",
      [("Δύο κρανία βρέθηκαν τη δεκαετία του 1970.", "Two skulls were found in the 1970s."),
       ("Ο τοίχος χτίστηκε πριν από 23.000 χρόνια.", "The wall was built 23,000 years ago."),
       ("για να προστατευτούν από τον αέρα", "to protect themselves from the wind (passive subjunctive: να + προστατευτούν)")]),
    G("B1", "Time ago: πριν από and εδώ και", "«Πριν από» και «εδώ και»",
      "πριν από + accusative means 'before' or, with a length of time, 'ago': πριν από 23.000 χρόνια. εδώ και + time means 'for (up to now)' and goes with the present: ζουν εδώ και 200.000 χρόνια 'they have been living here for 200,000 years'. English uses a perfect; Greek uses a present.",
      [("πριν από περίπου 23.000 χρόνια", "about 23,000 years ago"),
       ("Οι άνθρωποι ζουν στον ελλαδικό χώρο εδώ και πολύ καιρό.", "People have been living in the region for a long time.")]),
  ],
  terms=[
    T("ο παλαιοανθρωπολόγος", "palaeoanthropologist", "Επιστήμονας που μελετά τα απολιθώματα των πρώτων ανθρώπων.", "A scientist who studies fossils of early humans."),
    T("η εποχή των παγετώνων", "Ice Age", "Μεγάλη περίοδος πολύ ψυχρού κλίματος, με πάγους σε μεγάλο μέρος της Γης.", "A long period of very cold climate with ice sheets over much of the Earth."),
    T("η χρονολόγηση", "dating", "Η μέθοδος με την οποία βρίσκουμε πόσο παλιό είναι κάτι.", "Finding out how old something is."),
    T("η λεπίδα", "blade", "Το κοφτερό μέρος ενός εργαλείου· εδώ, μακρόστενο κομμάτι πέτρας.", "The cutting edge of a tool; here, a long narrow flake of stone."),
    T("η ναυσιπλοΐα", "seafaring, navigation", "Τα ταξίδια με πλοία στη θάλασσα.", "Travelling by boat on the sea."),
    T("η χιλιετία", "millennium", "Περίοδος χιλίων ετών.", "A period of a thousand years."),
    T("το στρώμα", "layer, stratum", "Ένα επίπεδο χώματος σε μια ανασκαφή· όσο πιο βαθιά, τόσο πιο παλιό.", "A level of earth in an excavation; the deeper, the older."),
  ],
  questions=[
    Q("Τι ανακοινώθηκε το 2019 για το κρανίο από το Απήδημα;", ["Ότι είναι περίπου 210.000 ετών και ανήκει σε Homo sapiens", "Ότι είναι νεολιθικό", "Ότι ανήκει σε βασιλιά", "Ότι βρέθηκε στη Μήλο"], 0, "Harvati et al., Nature 2019."),
    Q("Γιατί έχτισαν πιθανότατα τον τοίχο της Θεόπετρας;", ["Για να προστατευτούν από τον κρύο αέρα", "Για να κρατήσουν νερό", "Για να κρύψουν θησαυρούς", "Για έναν ναό"], 0, "It dates to the coldest phase of the last Ice Age."),
    Q("Τι αποδεικνύει ο οψιανός της Μήλου στο σπήλαιο Φράγχθι;", ["Ότι οι άνθρωποι ταξίδευαν στη θάλασσα", "Ότι η Μήλος ήταν ενωμένη με την Πελοπόννησο", "Ότι υπήρχε γεωργία", "Ότι υπήρχε μέταλλο"], 0, "Melos was an island, so the obsidian came by boat."),
    Q("Πώς ήρθε πιθανότατα η γεωργία στο Φράγχθι;", ["Από τη θάλασσα", "Από τη Βόρεια Ευρώπη", "Από την Αίγυπτο με καμήλες", "Δεν ήρθε ποτέ"], 0, "Perlès argued for colonists arriving by sea."),
  ],
  vocab=["κρανίο", "ανήκω", "είδος", "αρχαιότερος", "εποχή", "παγωμένος", "κατασκευή", "κοφτερός", "ξυράφι", "ηφαιστειακός", "ταξιδεύω", "βάρκα", "στοιχείο", "ψαρεύω", "σπόρος", "φυτρώνω", "άγριος", "εμφανίζομαι"],
  sources=[
    SRC("Harvati, K. et al. (2019). “Apidima Cave fossils provide earliest evidence of Homo sapiens in Eurasia”. Nature 571: 500–504; University of Tübingen press release, 10 July 2019.", "https://uni-tuebingen.de/en/university/news-and-publications/press-releases/archive/archivfullview-press-releases/article/earliest-known-homo-sapiens-in-eurasia-found-in-greece"),
    SRC("Kyparissi-Apostolika, N. (ed.) (2000). Theopetra Cave: Twelve Years of Excavation and Research 1987–1998. Athens: Institute for Aegean Prehistory."),
    SRC("“Theopetra Cave”, Wikipedia (OSL date of the wall, c. 23,000 years).", "https://en.wikipedia.org/wiki/Theopetra_Cave"),
    SRC("“Franchthi Cave”, Wikipedia (occupation sequence, Melian obsidian, tuna bones).", "https://en.wikipedia.org/wiki/Franchthi_Cave"),
    SRC("Laskaris, N. et al. (2011). “Late Pleistocene/Early Holocene seafaring in the Aegean: new obsidian hydration dates with the SIMS-SS method”. Journal of Archaeological Science 38: 2475–2479."),
    SRC("Perlès, C., Quiles, A. & Valladas, H. (2013). “Early seventh-millennium AMS dates from domestic seeds in the Initial Neolithic at Franchthi Cave (Argolid, Greece)”. Antiquity 87: 1001–1015.", "https://hal.parisnanterre.fr/hal-01529120/file/early_seventhmillennium_ams_dates_perles_Catherine.pdf"),
  ]))

# 1.3 art
CH.append(dict(id="e1-cycladic", theme="art", el="Τα κυκλαδικά ειδώλια", title="The Cycladic figurines", dates="περ. 3200–2000 π.Χ.",
  image="cycladic-figure",
  summary_en="The marble figures of the Early Bronze Age Cyclades: how they were made, what they may have meant, why so many have lost their findspot, and how they shaped modern sculpture.",
  sections=[
    S("marble", "Μάρμαρο από τα νησιά", "Marble from the islands", [
      P("Γύρω στο 3200 π.Χ. αρχίζει στο Αιγαίο η Εποχή του Χαλκού. Στις Κυκλάδες, τα νησιά που σχηματίζουν έναν κύκλο γύρω από τη Δήλο, αναπτύχθηκε τότε ένας ξεχωριστός πολιτισμός, ο κυκλαδικός. Οι κάτοικοί τους ήταν αγρότες, ψαράδες και θαλασσινοί. Είναι όμως γνωστοί σε όλο τον κόσμο για κάτι άλλο: για τα μαρμάρινα ειδώλια τους, που μοιάζουν εκπληκτικά μοντέρνα.",
        "Around 3200 BC the Bronze Age begins in the Aegean, as copper and later bronze tools spread. In the Cyclades, the islands that form a circle (κύκλος) around Delos, a distinctive culture developed, the Early Cycladic, which lasted until about 2000 BC. Its people were farmers, fishermen and seafarers, travelling in long oared boats of the kind shown on clay 'frying pans' from Syros. But they are known all over the world for something else: their marble figurines, which look astonishingly modern.", [1, 2]),
      P("Τα περισσότερα ειδώλια είναι γυναικείες μορφές, όρθιες, με τα χέρια διπλωμένα κάτω από το στήθος. Οι αρχαιολόγοι ονομάζουν αυτόν τον τύπο «κανονικό». Το μέγεθός τους ποικίλλει: τα περισσότερα έχουν ύψος λίγων εκατοστών, αλλά το μεγαλύτερο που σώζεται ολόκληρο, από την Αμοργό, φτάνει σχεδόν το ενάμισι μέτρο. Τα έφτιαχναν από το λευκό μάρμαρο της Νάξου και της Πάρου, το έτριβαν με σμύριδα και το γυάλιζαν με πέτρες.",
        "Most of the figurines are female figures, standing, with their arms folded beneath the breasts, the right arm usually below the left. Archaeologists call this the 'canonical' or folded-arm type, and divide it into varieties named after cemeteries (Spedos, Dokathismata and others). Their size varies: most are a few centimetres to a few tens of centimetres high, but fewer than a dozen are thought to have stood over a metre, and the largest that survives complete, from Amorgos and now in the National Archaeological Museum in Athens, is nearly one and a half metres tall. They were made from the white marble of Naxos and Paros, shaped with emery (also from Naxos) and polished with stones such as pumice; metal tools were rare.", [1, 3]),
    ]),
    S("colour", "Ειδώλια με χρώματα", "Figurines in colour", [
      P("Σήμερα τα ειδώλια μάς φαίνονται λευκά και λιτά. Στην αρχή όμως ήταν ζωγραφισμένα. Πάνω στο μάρμαρο έχουν βρεθεί ίχνη από κόκκινο, μπλε και μαύρο χρώμα, που έδειχναν τα μάτια, τα μαλλιά, κοσμήματα ή σχέδια στο πρόσωπο και στο σώμα. Τα περισσότερα έχουν μόνο τη μύτη σκαλισμένη· τα υπόλοιπα χαρακτηριστικά τα ζωγράφιζαν.",
        "Today the figurines look white and austere to us. Originally, though, they were painted. Traces of red, blue and black pigment have been found on the marble, as well as 'ghosts' where paint protected the surface from weathering; they marked eyes, hair, jewellery, or patterns of dots and stripes on the face and body. Most have only the nose carved in relief; the other features were painted. Scientific analysis has identified pigments such as cinnabar and iron oxides for red and azurite for blue. The 'pure white' look that inspired modern artists is therefore partly an accident of survival.", [2, 3]),
      P("Τι σήμαιναν; Δεν ξέρουμε με βεβαιότητα. Πολλά βρέθηκαν σε τάφους, άλλα σε σπίτια. Στο νησάκι Κέρος βρέθηκαν χιλιάδες κομμάτια ειδωλίων που είχαν σπάσει σκόπιμα σε άλλο μέρος και είχαν μεταφερθεί εκεί. Γι' αυτό πολλοί αρχαιολόγοι πιστεύουν ότι η Κέρος ήταν ένα ιερό, ίσως το πρώτο κοινό ιερό των Κυκλάδων.",
        "What did they mean? We do not know for sure: goddesses, ancestors, servants for the dead, or images of the dead person have all been suggested. Many were found in graves, others in settlements. On the islet of Keros, between Naxos and Amorgos, excavations led by Colin Renfrew found thousands of fragments of figurines and marble vessels that had been deliberately broken elsewhere and brought there. For that reason many archaeologists believe that Keros was a sanctuary, perhaps the earliest shared sanctuary of the Cyclades, where islanders brought broken objects as part of a ritual.", [4, 5]),
    ]),
    S("modern", "Από τους τάφους στα μουσεία", "From graves to museums", [
      P("Τον 20ό αιώνα τα κυκλαδικά ειδώλια έγιναν πολύ δημοφιλή. Γλύπτες όπως ο Κωνσταντίν Μπρανκούζι, ο Αμεντέο Μοντιλιάνι και ο Χένρι Μουρ εμπνεύστηκαν από τις απλές τους γραμμές. Η επιτυχία είχε όμως και σκοτεινή πλευρά: λαθρανασκαφείς λεηλάτησαν πολλούς τάφους για να πουλήσουν ειδώλια σε συλλέκτες. Έτσι, για τα περισσότερα από αυτά δεν ξέρουμε πού ακριβώς βρέθηκαν, και ένα μέρος από όσα κυκλοφορούν στην αγορά είναι πλαστά.",
        "In the twentieth century the Cycladic figurines became extremely popular. Sculptors such as Constantin Brâncuși, Amedeo Modigliani and Henry Moore drew inspiration from their simple lines, and the figures came to be seen as precursors of modernism. But success had a dark side: looters plundered many graves to sell figurines to collectors. As a result, for most of them (by some counts only about 40% have a known origin) we do not know exactly where they were found, which destroys much of their value as evidence, and some of those on the market are forgeries. The archaeologists David Gill and Christopher Chippindale called this the 'material and intellectual consequences' of esteem for Cycladic figures.", [3, 6]),
    ]),
  ],
  grammar=[
    G("B1", "The passive present for general statements", "Παθητικός ενεστώτας: «λέγεται», «θεωρείται»",
      "Greek often uses a passive present in -εται / -ονται where English says 'is called', 'is considered', 'are found': ονομάζεται, θεωρείται, βρίσκεται. It states general facts without naming who does the action. The active third person plural does the same job informally: τους λένε «μαγούλες» = they are called magoules.",
      [("Ο τύπος ονομάζεται «κανονικός».", "The type is called 'canonical'."),
       ("Στο Αιγαίο ο οψιανός βρίσκεται κυρίως στη Μήλο.", "In the Aegean obsidian is found mainly on Melos.")]),
    G("B1", "Pluperfect: είχε + aorist form", "Υπερσυντέλικος",
      "For an action completed before another past action, Greek uses είχα/είχες/είχε... + the invariable aorist form (-ει for active, -εί for passive): είχαν σπάσει 'they had broken', είχαν μεταφερθεί 'they had been carried'.",
      [("κομμάτια που είχαν σπάσει σκόπιμα σε άλλο μέρος", "pieces that had been broken (lit. had broken) deliberately elsewhere"),
       ("και είχαν μεταφερθεί εκεί", "and had been carried there")]),
  ],
  terms=[
    T("η Εποχή του Χαλκού", "the Bronze Age", "Η περίοδος που τα εργαλεία γίνονταν κυρίως από χαλκό και κράματά του· στο Αιγαίο περ. 3200–1100 π.Χ.", "The period when tools were made mainly of copper and bronze; in the Aegean c. 3200–1100 BC."),
    T("το ειδώλιο", "figurine", "Μικρό άγαλμα ανθρώπου ή ζώου.", "A small statue of a human or animal."),
    T("η σμύριδα", "emery", "Σκληρή πέτρα της Νάξου που χρησιμοποιείται για τρίψιμο και γυάλισμα.", "A hard rock from Naxos used for grinding and polishing."),
    T("το ιερό", "sanctuary", "Τόπος λατρείας, αφιερωμένος σε θεό ή θεότητα.", "A place of worship."),
    T("ο λαθρανασκαφέας", "looter, illicit digger", "Άνθρωπος που σκάβει παράνομα για να βρει και να πουλήσει αρχαία.", "Someone who digs illegally to find and sell antiquities."),
    T("πλαστός", "forged, fake", "Ψεύτικος, φτιαγμένος για να ξεγελάσει.", "False, made to deceive."),
  ],
  questions=[
    Q("Πώς είναι τα χέρια στον «κανονικό» τύπο ειδωλίου;", ["Διπλωμένα κάτω από το στήθος", "Σηκωμένα ψηλά", "Ανοιχτά στο πλάι", "Πίσω από την πλάτη"], 0, "The folded-arm type."),
    Q("Ήταν τα ειδώλια πάντα λευκά;", ["Όχι, ήταν ζωγραφισμένα", "Ναι, πάντα", "Ήταν από χρυσό", "Ήταν από ξύλο"], 0, "Pigment traces show red, blue and black paint."),
    Q("Γιατί πιστεύουν ότι η Κέρος ήταν ιερό;", ["Γιατί εκεί μεταφέρθηκαν χιλιάδες σπασμένα ειδώλια", "Γιατί είχε ναό με κίονες", "Γιατί το λέει ο Όμηρος", "Γιατί είχε ανάκτορο"], 0, "The fragments were broken elsewhere and brought there."),
    Q("Ποια ήταν η σκοτεινή πλευρά της δημοτικότητας των ειδωλίων;", ["Οι λεηλασίες τάφων και τα πλαστά", "Οι πόλεμοι στις Κυκλάδες", "Η καταστροφή του μαρμάρου", "Τίποτα"], 0, "Looting destroyed their archaeological context."),
  ],
  vocab=["μάρμαρο", "σχηματίζω", "αναπτύσσομαι", "ξεχωριστός", "πολιτισμός", "εκπληκτικός", "διπλώνω", "ποικίλλω", "ύψος", "σώζομαι", "γυαλίζω", "λιτός", "ίχνος", "βεβαιότητα", "σκόπιμα", "μεταφέρω", "εμπνέομαι", "λεηλατώ", "συλλέκτης"],
  sources=[
    SRC("The Metropolitan Museum of Art, “Marble female figure, Early Cycladic I–II, ca. 3200–2700 BCE” (object record).", "https://www.metmuseum.org/art/collection/search/254526"),
    SRC("“Cycladic culture”, Wikipedia (periods, figurine types, pigments).", "https://en.wikipedia.org/wiki/Cycladic_culture"),
    SRC("Renfrew, C. (1991). The Cycladic Spirit: Masterpieces from the Nicholas P. Goulandris Collection. London: Thames & Hudson."),
    SRC("“Keros”, Wikipedia (the Keros deposits and the Cambridge–Greek excavations 2006–2018).", "https://en.wikipedia.org/wiki/Keros"),
    SRC("Renfrew, C., Boyd, M. & Bronk Ramsey, C. (2012). “The oldest maritime sanctuary? Dating the sanctuary at Keros and the Cycladic Early Bronze Age”. Antiquity 86: 144–160."),
    SRC("Gill, D. W. J. & Chippindale, C. (1993). “Material and intellectual consequences of esteem for Cycladic figures”. American Journal of Archaeology 97: 601–659."),
  ]))

# 1.4 culture
CH.append(dict(id="e1-dispilio", theme="culture", el="Ζωή δίπλα στη λίμνη: το Δισπηλιό", title="Life on the lake: Dispilio", dates="περ. 6000–3000 π.Χ.",
  image="neolithic-figure",
  summary_en="A Neolithic village built on wooden piles on Lake Orestiada near Kastoria, its famous inscribed tablet, and what figurines may tell us about Neolithic beliefs.",
  sections=[
    S("lake", "Ένα χωριό πάνω σε πασσάλους", "A village on piles", [
      P("Το 1932 η στάθμη της λίμνης Ορεστιάδας, κοντά στην Καστοριά, κατέβηκε πολύ, και από το νερό φάνηκαν ξύλινοι πάσσαλοι. Ήταν τα υπολείμματα ενός νεολιθικού οικισμού, του Δισπηλιού. Συστηματικές ανασκαφές ξεκίνησαν το 1992 από το Αριστοτέλειο Πανεπιστήμιο Θεσσαλονίκης, με επικεφαλής τον καθηγητή Γιώργο Χουρμουζιάδη. Ο οικισμός κατοικήθηκε για πολλούς αιώνες, κυρίως στη Μέση και στην Ύστερη Νεολιθική.",
        "In 1932 the level of Lake Orestiada near Kastoria fell sharply, and wooden piles appeared above the water. They were the remains of a Neolithic settlement, Dispilio, noted at the time by the archaeologist Antonios Keramopoulos. Systematic excavations began in 1992 under Professor Giorgos Hourmouziadis of the Aristotle University of Thessaloniki, the same scholar who reinterpreted Dimini. The settlement was inhabited for many centuries, above all in the Middle and Late Neolithic, from the sixth into the fourth millennium BC. Because the waterlogged mud preserved organic material, Dispilio has yielded wood, seeds and other finds that rarely survive on dry sites.", [1, 2]),
      P("Τα σπίτια ήταν χτισμένα πάνω σε πασσάλους, στην όχθη ή μέσα στα ρηχά νερά της λίμνης. Οι κάτοικοι καλλιεργούσαν σιτάρι και όσπρια, μάζευαν καρπούς από το δάσος, ψάρευαν και κυνηγούσαν. Έφτιαχναν εργαλεία από πέτρα, κόκαλο και κέρατο ελαφιού, και αγγεία από πηλό. Σήμερα κοντά στο αρχαιολογικό εύρημα υπάρχει μια ανασύσταση του οικισμού, με καλύβες από ξύλο και καλάμια, που μπορεί να την επισκεφτεί κανείς.",
        "The houses were built on piles, on the shore or in the shallow water of the lake, which gave protection and kept floors dry as the water level changed. The inhabitants grew wheat and pulses, gathered nuts and fruit from the forest, fished and hunted. They made tools of stone, bone and deer antler, and pots of clay. Today, next to the excavation, there is an open-air reconstruction of the settlement, with huts of wood and reeds, which visitors can walk around; it is one of the very few reconstructed Neolithic lake villages in south-eastern Europe.", [1, 3]),
    ]),
    S("tablet", "Η πινακίδα του Δισπηλιού", "The Dispilio tablet", [
      P("Το πιο διάσημο εύρημα του Δισπηλιού είναι μια ξύλινη πινακίδα που βρέθηκε το 1993. Πάνω της είναι χαραγμένα σημάδια σε σειρές. Η χρονολόγηση με τη μέθοδο του ραδιενεργού άνθρακα έδωσε ημερομηνία περίπου στο 5200 π.Χ. Μερικοί είδαν σε αυτά τα σημάδια την αρχαιότερη γραφή του κόσμου. Οι περισσότεροι ειδικοί όμως είναι πιο προσεκτικοί: τα σημάδια μπορεί να είναι διακοσμήσεις ή σύμβολα, αλλά δεν ξέρουμε αν αποδίδουν μια γλώσσα.",
        "The most famous find from Dispilio is a wooden tablet found in 1993, with marks incised in rows. Radiocarbon dating of the wood, published in 2014 by Yorgos Facorellis and colleagues, gave a calibrated range of about 5324–5079 BC; popular sources often round this to 'about 5200 BC' or quote older figures such as 5260 BC. Some have seen these marks as the oldest writing in the world, and the tablet is often presented online as 'proof' of Neolithic Greek writing. Most specialists are more careful: the signs may be decorations, owner's marks or symbols, but nothing shows that they record a language, let alone Greek, which did not yet exist. Real writing, in the sense of signs for the sounds or words of a language, appears in the Aegean only with the Cretan scripts of the Bronze Age.", [4, 5]),
    ]),
    S("beliefs", "Πίστεψαν σε μια «Μεγάλη Μητέρα»;", "Did they believe in a 'Great Mother'?", [
      P("Σε πολλούς νεολιθικούς οικισμούς της Ελλάδας, από τη Θεσσαλία μέχρι την Κρήτη, βρέθηκαν μικρά ειδώλια, πολλά από τα οποία παριστάνουν γυναίκες με τονισμένους γοφούς και κοιλιά. Παλαιότερα οι ερευνητές πίστευαν ότι όλα αυτά απεικόνιζαν μια μεγάλη θεά της γονιμότητας, τη «Μεγάλη Μητέρα». Σήμερα οι περισσότεροι αρχαιολόγοι αμφιβάλλουν για μια τόσο απλή εξήγηση.",
        "In many Neolithic settlements of Greece, from Thessaly to Crete, small figurines have been found, many of which show women with emphasised hips and belly, like the Late Neolithic marble figure in the picture. Researchers used to believe that all of these depicted one great fertility goddess, the 'Great Mother'; the archaeologist Marija Gimbutas built a whole theory of a peaceful, goddess-worshipping 'Old Europe' on such figures. Today most archaeologists doubt so simple an explanation.", [6, 7]),
      P("Τα ειδώλια είναι πολύ διαφορετικά μεταξύ τους: υπάρχουν γυναίκες, άντρες, ζώα και μορφές που δεν μπορούμε να πούμε τι φύλο έχουν. Βρέθηκαν σε σπίτια, σε σωρούς από σκουπίδια, σπάνια σε τάφους. Ίσως χρησιμοποιούνταν σε τελετές, ίσως ήταν παιχνίδια ή αναθήματα. Η απάντηση είναι πιθανότατα ότι είχαν πολλές χρήσεις. Μας θυμίζουν πόσο δύσκολο είναι να καταλάβουμε τις ιδέες ανθρώπων που δεν άφησαν γραπτά κείμενα.",
        "The figurines are very varied: there are women, men, animals and figures whose sex cannot be determined. They were found in houses and in rubbish deposits, rarely in graves; many were deliberately broken. They may have been used in rituals, may have been toys, teaching aids, votive offerings or tokens in exchanges. The answer is probably that they had many uses, which changed over the three thousand years of the Neolithic. They remind us how hard it is to understand the ideas of people who left no written texts: archaeology can tell us what people did with objects, much less what they believed.", [6, 7]),
    ]),
  ],
  grammar=[
    G("B1", "The relative ο οποίος / η οποία / το οποίο", "Η αναφορική αντωνυμία «ο οποίος»",
      "που is the everyday relative 'who/which/that'. In more careful writing, and after a preposition or a word like πολλά/μερικά, Greek uses ο οποίος, which agrees with the noun in gender and number and takes the case of its own clause: πολλά από τα οποία 'many of which', η μέθοδος με την οποία 'the method by which'.",
      [("μικρά ειδώλια, πολλά από τα οποία παριστάνουν γυναίκες", "small figurines, many of which depict women"),
       ("η μέθοδος με την οποία βρίσκουμε την ηλικία", "the method by which we find the age")]),
    G("B1", "Impersonal κανείς 'one, anyone'", "Το απρόσωπο «κανείς»",
      "In a positive sentence, κανείς (or κάποιος) can mean 'one, a person' in general: μπορεί να την επισκεφτεί κανείς 'one can visit it'. In a negative sentence it means 'nobody': δεν ξέρει κανείς 'nobody knows'.",
      [("μια ανασύσταση που μπορεί να την επισκεφτεί κανείς", "a reconstruction that one can visit"),
       ("Δεν ξέρει κανείς τι σήμαιναν.", "Nobody knows what they meant.")]),
  ],
  terms=[
    T("ο πάσσαλος", "pile, stake", "Χοντρό ξύλο καρφωμένο στο έδαφος για να στηρίξει κάτι.", "A thick post driven into the ground to support something."),
    T("η στάθμη", "level (of water)", "Το ύψος της επιφάνειας του νερού.", "The height of a water surface."),
    T("η ανασκαφή", "excavation", "Η συστηματική έρευνα του εδάφους για αρχαία ευρήματα.", "Systematic digging for archaeological finds."),
    T("η ανασύσταση", "reconstruction", "Αντίγραφο που δείχνει πώς ήταν κάτι στο παρελθόν.", "A model showing how something once looked."),
    T("η πινακίδα", "tablet", "Επίπεδο κομμάτι ξύλου ή πηλού για να γράφει κανείς πάνω του.", "A flat piece of wood or clay for writing on."),
    T("ο ραδιενεργός άνθρακας", "radiocarbon", "Ο άνθρακας-14, που χρησιμοποιείται για τη χρονολόγηση οργανικών υλικών.", "Carbon-14, used to date organic materials."),
    T("η γονιμότητα", "fertility", "Η ικανότητα να γεννάει κανείς ή να παράγει καρπούς.", "The ability to bear children or produce crops."),
    T("το ανάθημα", "votive offering", "Αντικείμενο που προσφέρεται σε θεό.", "An object offered to a god."),
  ],
  questions=[
    Q("Πότε φάνηκαν για πρώτη φορά οι πάσσαλοι του Δισπηλιού;", ["Το 1932", "Το 1992", "Το 5200 π.Χ.", "Το 1993"], 0, "The lake level dropped in 1932; excavation began in 1992."),
    Q("Τι πιστεύουν οι περισσότεροι ειδικοί για την πινακίδα;", ["Ότι δεν ξέρουμε αν τα σημάδια αποδίδουν γλώσσα", "Ότι είναι ελληνική γραφή", "Ότι είναι ψεύτικη", "Ότι είναι χάρτης"], 0, "Marks are not necessarily writing."),
    Q("Πού βρέθηκαν κυρίως τα νεολιθικά ειδώλια;", ["Σε σπίτια και σωρούς σκουπιδιών", "Μόνο σε ναούς", "Μόνο σε τάφους", "Στη θάλασσα"], 0, "Rarely in graves."),
    Q("Γιατί είναι δύσκολο να καταλάβουμε τα ειδώλια;", ["Γιατί οι άνθρωποι εκείνοι δεν άφησαν κείμενα", "Γιατί είναι πολύ μεγάλα", "Γιατί χάθηκαν όλα", "Γιατί είναι από χρυσό"], 0, "No written sources explain them."),
  ],
  vocab=["λίμνη", "υπόλειμμα", "συστηματικός", "κατοικώ", "όχθη", "ρηχός", "όσπριο", "κόκαλο", "ελάφι", "καλύβα", "εύρημα", "χαράζω", "σημάδι", "προσεκτικός", "διακόσμηση", "παριστάνω", "απεικονίζω", "αμφιβάλλω", "τελετή", "φύλο"],
  sources=[
    SRC("“Dispilio”, Wikipedia (discovery in 1932, excavations from 1992).", "https://en.wikipedia.org/wiki/Dispilio"),
    SRC("Hourmouziadis, G. H. (ed.) (2002). Δισπηλιό: 7500 χρόνια μετά. Θεσσαλονίκη: University Studio Press."),
    SRC("Visit Greece (Greek National Tourism Organisation), “Dispilio of Kastoria”.", "https://www.visitgreece.gr/en/experiences/nature/culture/dispilio-of-kastoria"),
    SRC("Facorellis, Y., Sofronidou, M. & Hourmouziadis, G. (2014). “Radiocarbon dating of the Neolithic lakeside settlement of Dispilio, Kastoria, northern Greece”. Radiocarbon 56 (2): 511–528.", "https://www.cambridge.org/core/journals/radiocarbon/article/radiocarbon-dating-of-the-neolithic-lakeside-settlement-of-dispilio-kastoria-northern-greece/759AA29502776E142883F1971293BEB1"),
    SRC("“Dispilio Tablet”, Wikipedia (find in 1993; status of the signs).", "https://en.wikipedia.org/wiki/Dispilio_Tablet"),
    SRC("The Metropolitan Museum of Art, “Marble female figure, Late Neolithic, 4500–4000 BCE” (object record).", "https://www.metmuseum.org/art/collection/search/255417"),
    SRC("Talalay, L. E. (1993). Deities, Dolls, and Devices: Neolithic Figurines from Franchthi Cave, Greece. Bloomington: Indiana University Press."),
  ]))

# 1.5 language
CH.append(dict(id="e1-pregreek", theme="language", el="Πριν από τα ελληνικά: λέξεις από μια χαμένη γλώσσα", title="Before Greek: words from a lost language", dates="πριν από το 2000 π.Χ.",
  image="double-axe",
  summary_en="Greek was not the first language of Greece. Place names in -nthos and -ssos, and everyday words such as ρεβίθι and κυπαρίσσι, are traces of the 'Pre-Greek' languages spoken before the Greeks arrived.",
  sections=[
    S("arrival", "Πότε ήρθαν τα ελληνικά;", "When did Greek arrive?", [
      P("Η ελληνική ανήκει στη μεγάλη οικογένεια των ινδοευρωπαϊκών γλωσσών, μαζί με τα λατινικά, τα σανσκριτικά, τα περσικά, τις γερμανικές και τις σλαβικές γλώσσες. Οι γλωσσολόγοι πιστεύουν ότι οι πρόγονοι αυτών των γλωσσών μιλιόνταν κάποτε σε μια περιοχή μακριά από την Ελλάδα, πιθανώς στις στέπες βόρεια της Μαύρης Θάλασσας ή στην Ανατολία. Αυτό σημαίνει ότι η γλώσσα που έγινε τα ελληνικά ήρθε στον ελλαδικό χώρο από αλλού.",
        "Greek belongs to the large family of Indo-European languages, along with Latin, Sanskrit, Persian and the Germanic and Slavic languages; compare πατήρ, Latin pater, Sanskrit pitár, English father. Linguists believe that the ancestor of these languages, Proto-Indo-European, was once spoken in a region far from Greece, most probably the steppes north of the Black Sea (the view now supported by most geneticists), or, on an older rival theory, in Anatolia. This means that the language that became Greek came into the region from elsewhere, carried by people who mixed with the farmers already living there.", [1, 2]),
      P("Πότε ακριβώς έγινε αυτό, δεν το ξέρουμε. Πολλοί ερευνητές το τοποθετούν γύρω στο 2000 π.Χ. ή λίγο νωρίτερα, όταν στην ηπειρωτική Ελλάδα παρατηρούνται καταστροφές οικισμών και νέοι τρόποι ζωής. Σίγουρο είναι μόνο ότι γύρω στο 1400 π.Χ. οι Μυκηναίοι έγραφαν ήδη ελληνικά. Πριν από τους Έλληνες όμως, στο Αιγαίο μιλούσαν άλλες γλώσσες, που χάθηκαν. Τις ονομάζουμε συμβατικά «προελληνικές».",
        "Exactly when this happened we do not know. Many researchers place it around 2000 BC or somewhat earlier, at the transition from the Early to the Middle Bronze Age (about 2200–1900 BC), when destructions of settlements and new ways of life are observed on the mainland; others argue for an earlier or a more gradual arrival, and archaeology alone cannot show which language people spoke. The only certainty is that by around 1400 BC the Mycenaeans were already writing Greek in Linear B. Before the Greeks, other languages were spoken in the Aegean, and they disappeared. We call them by convention 'Pre-Greek', which may cover more than one language; the Minoans' language, written in Linear A, was one of them.", [2, 3]),
    ]),
    S("names", "Κόρινθος, Παρνασσός, Κνωσός", "Corinth, Parnassus, Knossos", [
      P("Οι χαμένες γλώσσες άφησαν όμως ίχνη, κυρίως σε ονόματα τόπων. Πολλά τοπωνύμια τελειώνουν σε -νθος, όπως η Κόρινθος, η Τίρυνθα (αρχαία Τίρυνς, Τίρυνθος), η Ζάκυνθος και η Πρόβαλινθος, ή σε -σσος, όπως ο Παρνασσός, η Αλικαρνασσός και η Κνωσός, που στην αρχαιότητα γραφόταν Κνωσσός. Αυτές οι καταλήξεις δεν μπορούν να εξηγηθούν από την ελληνική ούτε από άλλες ινδοευρωπαϊκές γλώσσες.",
        "The lost languages did leave traces, above all in place names. Many place names end in -nthos, such as Corinth (Κόρινθος), Tiryns (gen. Τίρυνθος, modern Τίρυνθα), Zakynthos and Probalinthos in Attica, or in -ssos (-ttos in Attic), such as Parnassos, Halicarnassus and Knossos, which in antiquity was spelt Κνωσσός, and Hymettos. These endings cannot be explained from Greek or, in most cases, from other Indo-European languages. The observation goes back to the German scholar Paul Kretschmer in 1896. Some scholars connect -ssos with the Luwian language of Anatolia (Parnassos has been read as Luwian parna- 'house' with a possessive suffix), so 'Pre-Greek' may itself hide several different layers.", [3, 4]),
    ]),
    S("words", "Προελληνικές λέξεις στα σημερινά ελληνικά", "Pre-Greek words in Greek today", [
      P("Ίχνη υπάρχουν και σε λέξεις που χρησιμοποιούμε ακόμα. Ο «ερέβινθος» των αρχαίων έγινε το σημερινό «ρεβίθι». Το «κυπαρίσσι» έρχεται από το αρχαίο «κυπάρισσος», ο «υάκινθος» είναι λουλούδι και όνομα, και ο «λαβύρινθος» έχει την ίδια κατάληξη. Πολλές λέξεις για φυτά, ζώα, εργαλεία και τη θάλασσα θεωρούνται προελληνικές. Ακόμα και η «θάλασσα» ίσως είναι μία από αυτές, αν και γι' αυτήν οι γλωσσολόγοι διαφωνούν.",
        "Traces also survive in words we still use. Ancient ἐρέβινθος 'chickpea' became today's ρεβίθι. κυπαρίσσι comes from ancient κυπάρισσος 'cypress'; υάκινθος 'hyacinth' is a flower and a name; and λαβύρινθος 'labyrinth' has the same ending. Many words for plants, animals, tools and the sea are considered Pre-Greek: Robert Beekes's etymological dictionary marks hundreds of words as such. Even θάλασσα 'sea' may be one of them, although linguists disagree, since an Indo-European etymology has also been proposed. This pattern is typical: when newcomers settle in a land, they borrow local words for the local landscape, plants and places.", [4, 5]),
      P("Ο λαβύρινθος έχει και μια γοητευτική ιστορία. Ο Πλούταρχος γράφει ότι στη γλώσσα των Λυδών της Μικράς Ασίας «λάβρυς» λεγόταν ο διπλός πέλεκυς. Ο διπλός πέλεκυς ήταν το πιο σημαντικό θρησκευτικό σύμβολο της μινωικής Κρήτης. Έτσι, πολλοί υπέθεσαν ότι «λαβύρινθος» σήμαινε «το σπίτι του διπλού πέλεκυ», δηλαδή το ανάκτορο της Κνωσού. Η ερμηνεία είναι ελκυστική, αλλά δεν είναι αποδεδειγμένη.",
        "The labyrinth also has a fascinating story. Plutarch (Greek Questions 45) writes that in the language of the Lydians of Asia Minor labrys meant the double axe. The double axe, like the bronze one in the picture, was one of the most important religious symbols of Minoan Crete, carved on the stones of the palace of Knossos. So many scholars, starting with Arthur Evans, supposed that labyrinthos meant 'the house of the double axe', that is, the palace of Knossos, whose maze of rooms would then lie behind the myth of the Minotaur. A Linear B tablet from Knossos does mention a 'da-pu-ri-to-jo' (labyrinthos) with an offering to 'the Mistress of the Labyrinth'. The interpretation is attractive, but the link with labrys is not proven, and some linguists reject it.", [5, 6]),
    ]),
  ],
  grammar=[
    G("B1", "Passive imperfect: μιλιόνταν, γραφόταν, λεγόταν", "Παθητικός παρατατικός",
      "The passive imperfect describes what used to be said, written or done. Endings: -όμουν, -όσουν, -όταν, -όμασταν, -όσασταν, -ονταν (with stress on -ό-). For contracted verbs like μιλάω the 3rd plural is μιλιόνταν; λέγεται → λεγόταν; γράφεται → γραφόταν.",
      [("η Κνωσός, που στην αρχαιότητα γραφόταν Κνωσσός", "Knossos, which in antiquity was spelt Knossos with double s"),
       ("«λάβρυς» λεγόταν ο διπλός πέλεκυς", "the double axe was called labrys"),
       ("γλώσσες που μιλιόνταν κάποτε", "languages that were once spoken")]),
    G("B1", "Fronting the object with a pronoun", "Προτακτικό αντικείμενο: «Πότε ακριβώς έγινε, δεν το ξέρουμε»",
      "When an object or a whole clause is put first for emphasis, Greek repeats it with a weak pronoun before the verb: Πότε ακριβώς έγινε αυτό, δεν το ξέρουμε. Τις ονομάζουμε «προελληνικές». This doubling is normal and natural, not redundant.",
      [("Πότε ακριβώς έγινε αυτό, δεν το ξέρουμε.", "When exactly this happened, we don't know."),
       ("Το Σέσκλο τον ανέσκαψε ο Τσούντας.", "Sesklo was excavated by Tsountas (lit. Sesklo, Tsountas excavated it).")]),
  ],
  terms=[
    T("ινδοευρωπαϊκός", "Indo-European", "Που ανήκει στη μεγάλη οικογένεια γλωσσών από την Ινδία ως την Ευρώπη.", "Belonging to the language family stretching from India to Europe."),
    T("ο γλωσσολόγος", "linguist", "Επιστήμονας που μελετά τις γλώσσες.", "A scientist who studies languages."),
    T("προελληνικός", "Pre-Greek", "Που υπήρχε στο Αιγαίο πριν από την ελληνική γλώσσα.", "Existing in the Aegean before the Greek language."),
    T("το τοπωνύμιο", "place name", "Το όνομα ενός τόπου: πόλης, βουνού, νησιού.", "The name of a place: a town, mountain or island."),
    T("η κατάληξη", "ending, suffix", "Το τελευταίο μέρος μιας λέξης.", "The final part of a word."),
    T("ο διπλός πέλεκυς", "double axe", "Τσεκούρι με δύο λεπίδες· ιερό σύμβολο της μινωικής Κρήτης.", "An axe with two blades; a sacred symbol of Minoan Crete."),
    T("η ετυμολογία", "etymology", "Η προέλευση και η ιστορία μιας λέξης.", "The origin and history of a word."),
  ],
  questions=[
    Q("Σε ποια οικογένεια γλωσσών ανήκει η ελληνική;", ["Στην ινδοευρωπαϊκή", "Στη σημιτική", "Στην ουραλική", "Σε καμία"], 0, "With Latin, Sanskrit, Persian, Germanic, Slavic."),
    Q("Ποια κατάληξη τοπωνυμίων θεωρείται προελληνική;", ["-νθος", "-πολη", "-ούπολη", "-άκι"], 0, "Κόρινθος, Ζάκυνθος; also -σσος."),
    Q("Από ποια αρχαία λέξη προέρχεται το «ρεβίθι»;", ["Ερέβινθος", "Ρέω", "Ρόδον", "Έρεβος"], 0, "ἐρέβινθος 'chickpea'."),
    Q("Τι σήμαινε «λάβρυς» στη γλώσσα των Λυδών, κατά τον Πλούταρχο;", ["Διπλός πέλεκυς", "Σπίτι", "Βασιλιάς", "Ταύρος"], 0, "Plutarch, Greek Questions 45."),
  ],
  vocab=["οικογένεια", "στέπα", "τοποθετώ", "ηπειρωτικός", "παρατηρώ", "καταστροφή", "συμβατικά", "χάνομαι", "εξηγώ", "αρχαιότητα", "ρεβίθι", "κυπαρίσσι", "λουλούδι", "διαφωνώ", "γοητευτικός", "πέλεκυς", "σύμβολο", "υποθέτω", "ερμηνεία", "ελκυστικός"],
  sources=[
    SRC("Horrocks, G. (2010). Greek: A History of the Language and its Speakers. 2nd ed. Chichester: Wiley-Blackwell, ch. 1."),
    SRC("Anthony, D. W. (2007). The Horse, the Wheel, and Language. Princeton University Press (the steppe hypothesis)."),
    SRC("“Pre-Greek substrate”, Wikipedia (the -nthos/-ssos names, Kretschmer, Luwian hypothesis).", "https://en.wikipedia.org/wiki/Pre-Greek_substrate"),
    SRC("Beekes, R. S. P. (2014). Pre-Greek: Phonology, Morphology, Lexicon. Leiden: Brill; and Beekes (2010), Etymological Dictionary of Greek. Leiden: Brill."),
    SRC("Plutarch, Greek Questions (Αἴτια Ἑλληνικά) 45, on labrys as the Lydian word for axe."),
    SRC("The Metropolitan Museum of Art, “Bronze double axe, Minoan, ca. 1700–1450 BCE” (object record).", "https://www.metmuseum.org/art/collection/search/253596"),
  ]))
