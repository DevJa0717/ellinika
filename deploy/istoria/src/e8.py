# Era 8 · Τουρκοκρατία και Βενετοκρατία (1453–1821)
from common import P, S, G, T, Q, SRC

ERA = dict(id="ottoman", el="Τουρκοκρατία και Βενετοκρατία", en="Ottoman and Venetian rule", dates="1453–1821", dates_en="1453–1821", level="C1",
  intro_el="Μετά την Άλωση οι Έλληνες έζησαν σχεδόν τέσσερις αιώνες χωρίς δικό τους κράτος, μοιρασμένοι ανάμεσα στην Οθωμανική αυτοκρατορία και στις κτήσεις της Βενετίας. Η εποχή αυτή, που συχνά παρουσιάζεται ως «σκοτεινή», γέννησε ωστόσο την Κρητική Αναγέννηση, τον Γκρέκο, τα δημοτικά τραγούδια και τον Νεοελληνικό Διαφωτισμό, που προετοίμασε την Επανάσταση του 1821. Το τελευταίο μέρος του βιβλίου είναι σε επίπεδο C1: πυκνότερος λόγος, λόγιες δομές και αποσπάσματα σε παλαιότερες μορφές της γλώσσας.",
  intro_en="After the Fall the Greeks lived for almost four centuries without a state of their own, divided between the Ottoman Empire and the possessions of Venice. This period, often presented as a 'dark age', nevertheless produced the Cretan Renaissance, El Greco, the folk songs and the Modern Greek Enlightenment, which prepared the Revolution of 1821. The last part of the book is at C1: denser prose, learned structures, and excerpts in older forms of the language, which the translation unpacks.")

CH = []

# 8.1 politics
CH.append(dict(id="e8-rule", theme="politics", el="Πατριάρχης, μιλλέτ και Φαναριώτες: οι Έλληνες στην Οθωμανική αυτοκρατορία", title="Patriarch, millet and Phanariots: Greeks in the Ottoman Empire", dates="1454–1821",
  image="gennadios",
  summary_en="How the Ottoman state governed its Orthodox subjects through the Patriarchate, what the devshirme and the poll tax meant, how the Phanariot families rose to power, and why Venetian Crete and the Ionian Islands followed a different path.",
  sections=[
    S("patriarch", "Ο σουλτάνος και ο πατριάρχης", "The sultan and the patriarch", [
      P("Λίγους μήνες μετά την Άλωση, τον Ιανουάριο του 1454, ο Μωάμεθ Β΄ ανέδειξε πατριάρχη τον μοναχό Γεννάδιο Σχολάριο, έναν λόγιο γνωστό για την αντίθεσή του στην ένωση με την Καθολική Εκκλησία. Η επιλογή δεν ήταν τυχαία: ένας αντιδυτικός πατριάρχης εξασφάλιζε ότι οι ορθόδοξοι υπήκοοι δεν θα στρέφονταν προς τη Ρώμη ή τη Βενετία. Ο πατριάρχης έγινε έτσι όχι μόνο θρησκευτικός ηγέτης, αλλά και ο ανώτατος υπεύθυνος απέναντι στην Πύλη για όλους τους ορθόδοξους της αυτοκρατορίας, ανεξάρτητα από τη γλώσσα τους.",
        "A few months after the Fall, in January 1454, Mehmed II had the monk Gennadios Scholarios installed as patriarch, a scholar known for his opposition to union with the Catholic Church. The choice was not accidental: an anti-western patriarch ensured that the Orthodox subjects would not turn towards Rome or Venice. The patriarch thus became not only a religious leader but also the chief person answerable to the Porte for all the empire's Orthodox, whatever their language: Greeks, Bulgarians, Serbs, Romanians, Albanians and Arabs alike.", [1, 2]),
      P("Οι ιστορικοί περιέγραφαν παλαιότερα αυτή τη ρύθμιση ως «σύστημα των μιλλέτ», δηλαδή των θρησκευτικών κοινοτήτων με δική τους αυτοδιοίκηση. Σήμερα πολλοί υποστηρίζουν ότι ένα τόσο οργανωμένο σύστημα διαμορφώθηκε μόλις τον 18ο και τον 19ο αιώνα, και ότι η αφήγηση για τα προνόμια που παραχώρησε ο ίδιος ο Μωάμεθ είναι εν μέρει μεταγενέστερος μύθος. Αδιαμφισβήτητο είναι πάντως ότι οι χριστιανοί, ως «ραγιάδες», πλήρωναν ειδικό κεφαλικό φόρο, το χαράτσι, δεν μπορούσαν να φέρουν όπλα και, σε ορισμένες περιοχές, υπέφεραν από το παιδομάζωμα, τη στρατολόγηση αγοριών για τους γενίτσαρους.",
        "Historians used to describe this arrangement as the 'millet system', the religious communities with their own self-government. Today many argue that such an organised system took shape only in the eighteenth and nineteenth centuries, and that the story of privileges granted by Mehmed himself is partly a later myth. What is beyond dispute is that Christians, as re'aya ('flock', subjects), paid a special poll tax, the cizye or haraç, could not bear arms, and in some regions suffered the devshirme (παιδομάζωμα), the levy of boys for the Janissary corps, which declined in the seventeenth century.", [2, 3, 4]),
    ]),
    S("phanariots", "Οι Φαναριώτες", "The Phanariots", [
      P("Από τα τέλη του 17ου αιώνα μια ολιγάριθμη αλλά ισχυρή ελίτ, οι Φαναριώτες, που πήραν το όνομά τους από τη συνοικία του Φαναρίου όπου βρίσκεται το Πατριαρχείο, απέκτησε πρωτοφανή επιρροή. Χάρη στη γλωσσομάθεια και στη μόρφωσή τους, συχνά από πανεπιστήμια της Ιταλίας, έγιναν διερμηνείς της Πύλης και του στόλου, δηλαδή ουσιαστικά οι διπλωμάτες της αυτοκρατορίας. Από το 1711 και το 1716 ως το 1821 ο σουλτάνος διόριζε Φαναριώτες ηγεμόνες στη Μολδαβία και στη Βλαχία, στη σημερινή Ρουμανία, όπου οι αυλές τους έγιναν εστίες ελληνικής παιδείας.",
        "From the late seventeenth century a small but powerful elite, the Phanariots, named after the Phanar quarter where the Patriarchate stands, gained unprecedented influence. Thanks to their command of languages and their education, often at Italian universities (Alexandros Mavrokordatos studied medicine at Padua and Bologna), they became the Dragomans (interpreters) of the Porte and of the fleet, in effect the empire's diplomats. From 1711 and 1716 until 1821 the sultan appointed Phanariots as princes (hospodars) of Moldavia and Wallachia, in today's Romania, where their courts became centres of Greek learning.", [5, 6]),
    ]),
    S("venice", "Η άλλη Ελλάδα: Κρήτη και Επτάνησα", "The other Greece: Crete and the Ionian Islands", [
      P("Δεν έζησαν όλοι οι Έλληνες υπό οθωμανική κυριαρχία. Η Κρήτη ήταν βενετική κτήση από το 1211 ως το 1669, όταν, ύστερα από μια πολιορκία του Χάνδακα που κράτησε είκοσι ένα χρόνια, μία από τις μακρύτερες της ιστορίας, το νησί παραδόθηκε στους Οθωμανούς. Τα Επτάνησα, με εξαίρεση τη Λευκάδα για ένα διάστημα, δεν γνώρισαν ποτέ την τουρκική κατάκτηση· έμειναν βενετικά ως το 1797. Γι' αυτό η Κέρκυρα, η Ζάκυνθος και η Κεφαλονιά έχουν ως σήμερα έντονα ιταλικά στοιχεία στην αρχιτεκτονική, στη μουσική και στο λεξιλόγιό τους.",
        "Not all Greeks lived under Ottoman rule. Crete was a Venetian possession from 1211 to 1669, when, after a siege of Candia (Chandax, today's Heraklion) that lasted twenty-one years (1648–1669), one of the longest in history, the island surrendered to the Ottomans. The Ionian Islands, except Lefkada for a period (1479–1684), never experienced Turkish conquest; they remained Venetian until 1797. That is why Corfu, Zakynthos and Kefalonia still have strong Italian elements in their architecture, music and vocabulary.", [7, 8]),
    ]),
  ],
  grammar=[
    G("C1", "Learned active participles in -ων, -ούσα, -ον", "Μετοχές ενεργητικού ενεστώτα της λόγιας παράδοσης",
      "Formal Greek keeps ancient active participles as adjectives and nouns: ο κυβερνών 'the ruler', οι ενδιαφερόμενοι (passive), τα ισχύοντα 'the rules in force', η επικρατούσα άποψη 'the prevailing view', ο ανώτατος υπεύθυνος. Learn them as vocabulary: επικρατών/επικρατούσα/επικρατούν, ισχύων/ισχύουσα/ισχύον, υπάρχων/υπάρχουσα/υπάρχον (τα υπάρχοντα 'belongings').",
      [("Η επικρατούσα άποψη σήμερα είναι διαφορετική.", "The prevailing view today is different."),
       ("Σύμφωνα με τα ισχύοντα, οι χριστιανοί δεν έφεραν όπλα.", "Under the rules in force, Christians did not bear arms.")]),
    G("C1", "Learned set phrases with the ancient dative", "Λόγιες στερεότυπες φράσεις με δοτική",
      "The dative case is dead, but survives in fixed expressions common in formal prose: εν μέρει 'partly', εν λόγω 'in question', εν τω μεταξύ 'meanwhile', εν τέλει 'in the end', εν ονόματι 'in the name of', τοις μετρητοίς 'in cash; at face value', δόξα τω Θεώ 'thank God', εν πάση περιπτώσει 'in any case'.",
      [("Η αφήγηση είναι εν μέρει μεταγενέστερος μύθος.", "The story is partly a later myth."),
       ("Δεν πρέπει να παίρνουμε τις πηγές τοις μετρητοίς.", "We should not take the sources at face value.")]),
  ],
  terms=[
    T("η Πύλη", "the (Sublime) Porte", "Η οθωμανική κυβέρνηση στην Κωνσταντινούπολη.", "The Ottoman government in Constantinople."),
    T("ο υπήκοος", "subject (of a state)", "Πρόσωπο που ζει υπό την εξουσία ενός κράτους ή ηγεμόνα.", "A person under the authority of a state or ruler."),
    T("ο ραγιάς", "raya, (non-Muslim) subject", "Ο μη μουσουλμάνος υπήκοος της Οθωμανικής αυτοκρατορίας· σήμερα μεταφορικά ο δουλοπρεπής.", "A non-Muslim Ottoman subject; today figuratively a servile person."),
    T("το χαράτσι", "poll tax; (colloquial) a heavy charge", "Ο κεφαλικός φόρος των χριστιανών· σήμερα κάθε άδικος φόρος.", "The Christians' poll tax; today any unfair tax."),
    T("το παιδομάζωμα", "devshirme", "Η βίαιη στρατολόγηση χριστιανόπαιδων για τον οθωμανικό στρατό και τη διοίκηση.", "The forced levy of Christian boys for the Ottoman army and administration."),
    T("ο διερμηνέας", "interpreter, dragoman", "Αυτός που μεταφράζει προφορικά από μια γλώσσα σε άλλη.", "One who translates orally between languages."),
    T("πρωτοφανής", "unprecedented", "Που δεν έχει ξανασυμβεί ή ξαναϋπάρξει.", "Never seen or happened before."),
    T("αδιαμφισβήτητος", "indisputable", "Που δεν μπορεί να αμφισβητηθεί.", "Beyond dispute."),
  ],
  questions=[
    Q("Γιατί ο Μωάμεθ Β΄ προτίμησε τον Γεννάδιο ως πατριάρχη;", ["Γιατί ήταν αντίθετος στην ένωση με την Καθολική Εκκλησία", "Γιατί ήταν συγγενής του σουλτάνου", "Γιατί ήταν Βενετός", "Γιατί είχε πολεμήσει στα τείχη"], 0, "An anti-western patriarch."),
    Q("Τι αμφισβητούν σήμερα πολλοί ιστορικοί για το «σύστημα των μιλλέτ»;", ["Ότι υπήρχε ως οργανωμένο σύστημα ήδη από το 1454", "Ότι υπήρχαν χριστιανοί στην αυτοκρατορία", "Ότι υπήρχε πατριάρχης", "Ότι υπήρχε φόρος"], 0, "Probably later than often claimed."),
    Q("Σε τι όφειλαν οι Φαναριώτες την επιρροή τους;", ["Στη γλωσσομάθεια και στη μόρφωσή τους", "Στον στρατό τους", "Στα πλοία τους", "Στη συμμαχία τους με τη Βενετία"], 0, "Dragomans of the Porte."),
    Q("Ποια περιοχή δεν γνώρισε ποτέ, σχεδόν, οθωμανική κυριαρχία;", ["Τα Επτάνησα", "Η Κρήτη", "Η Πελοπόννησος", "Η Μακεδονία"], 0, "Venetian until 1797."),
  ],
  vocab=["αναδεικνύω", "αντίθεση", "τυχαίος", "εξασφαλίζω", "υπήκοος", "υπεύθυνος", "ανεξάρτητα", "ρύθμιση", "αυτοδιοίκηση", "διαμορφώνομαι", "προνόμιο", "παραχωρώ", "αδιαμφισβήτητος", "υποφέρω", "στρατολόγηση", "ολιγάριθμος", "πρωτοφανής", "γλωσσομάθεια", "διερμηνέας", "ουσιαστικά", "διορίζω", "εστία", "κυριαρχία", "παραδίνομαι"],
  sources=[
    SRC("Kritoboulos, History of Mehmed the Conqueror 2.1–2; Sphrantzes, Chronicon minus 35; Runciman, S. (1968). The Great Church in Captivity. Cambridge University Press, ch. 7."),
    SRC("Braude, B. (1982). Foundation myths of the millet system. In Braude, B., & Lewis, B. (eds), Christians and Jews in the Ottoman Empire, vol. 1. New York: Holmes & Meier, 69–88."),
    SRC("Clogg, R. (2013). A Concise History of Greece. 3rd ed. Cambridge University Press, ch. 1."),
    SRC("Inalcik, H. (1973). The Ottoman Empire: The Classical Age 1300–1600. London: Weidenfeld & Nicolson, 78–80 (devshirme)."),
    SRC("Philliou, C. M. (2011). Biography of an Empire: Governing Ottomans in an Age of Revolution. Berkeley: University of California Press."),
    SRC("Camariano-Cioran, A. (1974). Les académies princières de Bucarest et de Jassy et leurs professeurs. Thessaloniki: Institute for Balkan Studies."),
    SRC("Greene, M. (2000). A Shared World: Christians and Muslims in the Early Modern Mediterranean. Princeton University Press (Crete, 1645–1669)."),
    SRC("Παναγιωτόπουλος, Β. (επιμ.) (2003). Ιστορία του Νέου Ελληνισμού 1770–2000, τ. 1. Αθήνα: Ελληνικά Γράμματα; Hirst, A., & Sammon, P. (eds) (2014). The Ionian Islands: Aspects of their History and Culture. Newcastle: Cambridge Scholars."),
  ]))

# 8.2 art
CH.append(dict(id="e8-el-greco", theme="art", el="Από την Κρητική Σχολή στον Γκρέκο", title="From the Cretan School to El Greco", dates="περ. 1450–1614",
  image="toledo",
  summary_en="Candia's icon workshops, where Byzantine tradition met Venetian painting; Theophanes the Cretan on Mount Athos; and Domenikos Theotokopoulos, who trained as an icon painter in Crete and became, in Toledo, one of the great painters of Europe.",
  sections=[
    S("school", "Τα εργαστήρια του Χάνδακα", "The workshops of Candia", [
      P("Μετά την Άλωση πολλοί ζωγράφοι από την Κωνσταντινούπολη βρήκαν καταφύγιο στη βενετοκρατούμενη Κρήτη, και ο Χάνδακας εξελίχθηκε στο σημαντικότερο κέντρο αγιογραφίας του ελληνικού κόσμου. Αρχειακά έγγραφα αναφέρουν περισσότερους από εκατό ζωγράφους που εργάστηκαν εκεί τον 15ο και τον 16ο αιώνα. Τα εργαστήριά τους λειτουργούσαν σχεδόν βιομηχανικά: ένα συμβόλαιο του 1499 προβλέπει την παράδοση επτακοσίων εικόνων της Παναγίας μέσα σε σαράντα πέντε μέρες, για εμπόρους που θα τις πουλούσαν στη Δύση.",
        "After the Fall many painters from Constantinople found refuge in Venetian-ruled Crete, and Candia developed into the most important centre of icon painting in the Greek world. Archival documents name more than a hundred painters working there in the fifteenth and sixteenth centuries. Their workshops ran almost industrially: a contract of 1499 provides for the delivery of seven hundred icons of the Virgin within forty-five days, for merchants who would sell them in the West.", [1, 2]),
      P("Η ιδιαιτερότητα της «Κρητικής Σχολής» είναι ότι οι ζωγράφοι της δούλευαν, ανάλογα με την παραγγελία, είτε «alla greca», στον παραδοσιακό βυζαντινό τρόπο, είτε «alla latina», με στοιχεία της ιταλικής τέχνης, και συχνά συνδύαζαν τους δύο τρόπους στο ίδιο έργο. Κορυφαίοι εκπρόσωποί της ήταν ο Ανδρέας Ρίτζος, ο Μιχαήλ Δαμασκηνός και ο Θεοφάνης ο Κρης, που διακόσμησε με τοιχογραφίες μονές του Αγίου Όρους τη δεκαετία του 1530 και επηρέασε την ορθόδοξη ζωγραφική για αιώνες.",
        "The distinctive feature of the 'Cretan School' is that its painters worked, depending on the commission, either alla greca, in the traditional Byzantine manner, or alla latina, with elements of Italian art, and often combined the two in the same work. Its leading figures were Andreas Ritzos, Michael Damaskinos and Theophanes the Cretan, who decorated monasteries on Mount Athos with frescoes in the 1530s (the Great Lavra in 1535, Stavronikita in 1545–46) and influenced Orthodox painting for centuries.", [1, 3]),
    ]),
    S("greco", "Δομήνικος Θεοτοκόπουλος", "Domenikos Theotokopoulos", [
      P("Μέσα σε αυτό το περιβάλλον γεννήθηκε το 1541 ο Δομήνικος Θεοτοκόπουλος. Το 1563 αναφέρεται ήδη σε έγγραφο ως «μαΐστρος», δηλαδή ανεξάρτητος αγιογράφος με δικό του εργαστήριο. Γύρω στο 1567 εγκατέλειψε την Κρήτη για τη Βενετία, όπου μελέτησε τον Τιτσιάνο και τον Τιντορέτο, και το 1570 πήγε στη Ρώμη. Εκεί λέγεται ότι, όταν συζητήθηκε η κάλυψη των γυμνών μορφών της Καπέλα Σιστίνα, προσφέρθηκε να ξαναζωγραφίσει ολόκληρη την «Τελευταία Κρίση» του Μιχαήλ Άγγελου «με σεμνότητα και ευπρέπεια, και όχι κατώτερη σε ποιότητα», μια πρόταση που, όπως είναι αναμενόμενο, δεν τον έκανε δημοφιλή.",
        "Into this world Domenikos Theotokopoulos was born in 1541. By 1563 a document already calls him maistro, an independent icon painter with his own workshop. Around 1567 he left Crete for Venice, where he studied Titian and Tintoretto, and in 1570 he went to Rome. There, according to Giulio Mancini, when the covering of the nudes in the Sistine Chapel was being discussed, he offered to repaint Michelangelo's entire Last Judgement 'with modesty and decency, and no less well painted', a proposal which, predictably, did not make him popular.", [4, 5]),
      P("Το 1577 εγκαταστάθηκε στο Τολέδο της Ισπανίας, όπου έμεινε ως τον θάνατό του, το 1614. Οι Ισπανοί τον ονόμαζαν «El Greco», «ο Έλληνας», αλλά ο ίδιος υπέγραφε σχεδόν πάντα τα έργα του με ελληνικά γράμματα: «Δομήνικος Θεοτοκόπουλος ἐποίει», προσθέτοντας μερικές φορές «Κρής». Οι επιμηκυμένες μορφές του, τα ψυχρά, ηλεκτρικά χρώματα και ο ταραγμένος ουρανός, όπως στην «Άποψη του Τολέδου», φάνηκαν παράξενα στους επόμενους αιώνες. Ξαναανακαλύφθηκαν μόλις στις αρχές του 20ού αιώνα, όταν οι εξπρεσιονιστές και ο Πικάσο είδαν σε αυτόν έναν πρόδρομο της μοντέρνας τέχνης.",
        "In 1577 he settled in Toledo in Spain, where he stayed until his death in 1614. The Spaniards called him El Greco, 'the Greek', but he signed his works almost always in Greek letters: Δομήνικος Θεοτοκόπουλος ἐποίει, 'Domenikos Theotokopoulos made (this)', sometimes adding Κρής, 'Cretan'. His elongated figures, cold, electric colours and turbulent skies, as in the View of Toledo now in the Metropolitan Museum, seemed strange to later centuries. He was rediscovered only in the early twentieth century, when the Expressionists and Picasso saw him as a forerunner of modern art.", [5, 6, 7]),
    ]),
    S("debate", "Βυζαντινός ή Δυτικός;", "Byzantine or Western?", [
      P("Το ερώτημα πόσο «βυζαντινός» έμεινε ο Γκρέκο απασχόλησε έντονα την ελληνική και τη διεθνή έρευνα. Η ανακάλυψη, το 1983, μιας υπογεγραμμένης εικόνας της «Κοίμησης της Θεοτόκου» στη Σύρο έδειξε ότι πριν φύγει από την Κρήτη ήταν ήδη ώριμος αγιογράφος, που πειραματιζόταν με ιταλικά πρότυπα. Οι περισσότεροι μελετητές σήμερα απορρίπτουν τόσο την εθνικιστική ανάγνωση ενός «καθαρά βυζαντινού» Γκρέκο όσο και την αντίθετη, ενός καλλιτέχνη που απαρνήθηκε ολοκληρωτικά την καταγωγή του. Το έργο του μοιάζει μάλλον με μια προσωπική σύνθεση, αδιανόητη χωρίς τη διπλή του παιδεία.",
        "The question of how 'Byzantine' El Greco remained has occupied Greek and international scholarship intensely. The discovery in 1983 of a signed icon of the Dormition of the Virgin on Syros showed that before leaving Crete he was already a mature icon painter experimenting with Italian models. Most scholars today reject both the nationalist reading of a 'purely Byzantine' El Greco and the opposite one, of an artist who wholly renounced his origins. His work looks rather like a personal synthesis, unthinkable without his double training.", [6, 8]),
    ]),
  ],
  grammar=[
    G("C1", "Either/or with ανάλογα με and είτε ... είτε in complex sentences", "«Ανάλογα με την παραγγελία, είτε ... είτε»",
      "In C1 prose, alternative constructions are often embedded: ανάλογα με + noun introduces the condition, είτε ... είτε lists the options, and συχνά/ενίοτε adds a qualification. Keep parallel structure: είτε «alla greca», στον βυζαντινό τρόπο, είτε «alla latina», με ιταλικά στοιχεία. Commas mark the inserted explanation.",
      [("Δούλευαν, ανάλογα με την παραγγελία, είτε «alla greca» είτε «alla latina».", "They worked, depending on the commission, either alla greca or alla latina."),
       ("Απορρίπτουν τόσο τη μία ανάγνωση όσο και την αντίθετη.", "They reject both the one reading and the opposite.")]),
    G("C1", "Adjectives of impossibility and necessity in -τος: αδιανόητος, αναμενόμενος", "Ρηματικά επίθετα σε -τος και μετοχές σε -όμενος",
      "Verbal adjectives in -τος with the negative α- express impossibility: αδιανόητος 'unthinkable', ανεπανάληπτος 'unrepeatable', αναπόφευκτος 'unavoidable', ακατανόητος 'incomprehensible'. Participles in -όμενος can mean 'to be expected': αναμενόμενος 'expected', όπως είναι αναμενόμενο 'as is to be expected'.",
      [("Μια σύνθεση αδιανόητη χωρίς τη διπλή του παιδεία.", "A synthesis unthinkable without his double training."),
       ("Όπως ήταν αναμενόμενο, η πρόταση δεν τον έκανε δημοφιλή.", "As was to be expected, the proposal did not make him popular.")]),
  ],
  terms=[
    T("η αγιογραφία", "icon painting", "Η ζωγραφική εικόνων με θρησκευτικά θέματα.", "The painting of religious icons."),
    T("η παραγγελία", "commission, order", "Αίτημα να κατασκευαστεί ή να σταλεί κάτι, συνήθως με πληρωμή.", "A request, usually paid, to make or supply something."),
    T("ο εκπρόσωπος", "representative, exponent", "Αυτός που εκφράζει ή αντιπροσωπεύει μια ομάδα ή ένα ρεύμα.", "One who embodies or represents a group or movement."),
    T("ο αγιογράφος", "icon painter", "Ζωγράφος που φτιάχνει θρησκευτικές εικόνες και τοιχογραφίες.", "A painter of religious icons and murals."),
    T("επιμηκυμένος", "elongated", "Που έχει γίνει πιο μακρύς από το κανονικό.", "Made longer than normal."),
    T("η ευπρέπεια", "decency, propriety", "Η σεμνή και κόσμια συμπεριφορά ή εμφάνιση.", "Modest, proper behaviour or appearance."),
    T("απαρνιέμαι", "to renounce, disown", "Αρνούμαι κάτι που μου ανήκε ή στο οποίο πίστευα.", "To reject something one belonged to or believed in."),
    T("αδιανόητος", "unthinkable, inconceivable", "Που δεν μπορεί κανείς να τον φανταστεί.", "Impossible to imagine."),
  ],
  questions=[
    Q("Τι δείχνει το συμβόλαιο του 1499 για τα εργαστήρια του Χάνδακα;", ["Ότι παρήγαγαν εικόνες σε μεγάλες ποσότητες για εξαγωγή", "Ότι ζωγράφιζαν μόνο για τις εκκλησίες της Κρήτης", "Ότι δεν πληρώνονταν", "Ότι ήταν όλοι Ιταλοί"], 0, "700 icons in 45 days."),
    Q("Τι σημαίνει ότι ένας Κρητικός ζωγράφος δούλευε «alla latina»;", ["Με στοιχεία της ιταλικής τέχνης", "Στον βυζαντινό τρόπο", "Σε λατινικό χειρόγραφο", "Μόνο για καθολικούς"], 0, "As opposed to alla greca."),
    Q("Πώς υπέγραφε ο Γκρέκο τα έργα του;", ["Με ελληνικά γράμματα, με το πλήρες όνομά του", "«El Greco»", "Με λατινικά γράμματα", "Δεν υπέγραφε"], 0, "Δομήνικος Θεοτοκόπουλος ἐποίει."),
    Q("Τι έδειξε η εικόνα που βρέθηκε στη Σύρο το 1983;", ["Ότι ήταν ήδη ώριμος αγιογράφος πριν φύγει από την Κρήτη", "Ότι δεν είχε ζήσει ποτέ στην Κρήτη", "Ότι ήταν μαθητής του Πικάσο", "Ότι γεννήθηκε στη Σύρο"], 0, "The Dormition of the Virgin."),
  ],
  vocab=["καταφύγιο", "εξελίσσομαι", "αρχειακός", "έγγραφο", "βιομηχανικά", "συμβόλαιο", "προβλέπω", "ιδιαιτερότητα", "παραγγελία", "συνδυάζω", "εκπρόσωπος", "διακοσμώ", "εγκαταλείπω", "κάλυψη", "σεμνότητα", "κατώτερος", "δημοφιλής", "υπογράφω", "επιμηκυμένος", "ταραγμένος", "πρόδρομος", "ώριμος", "πειραματίζομαι", "απαρνιέμαι"],
  sources=[
    SRC("Χατζηδάκης, Μ. (1987). Έλληνες ζωγράφοι μετά την Άλωση (1450–1830), τ. 1. Αθήνα: Κέντρο Νεοελληνικών Ερευνών Ε.Ι.Ε."),
    SRC("Cattapan, M. (1972). Nuovi elenchi e documenti dei pittori in Creta dal 1300 al 1500. Θησαυρίσματα 9: 202–235 (the 1499 contract for 700 icons)."),
    SRC("Chatzidakis, M. (1986). Ο κρητικός ζωγράφος Θεοφάνης: Η τελευταία φάση της τέχνης του στις τοιχογραφίες της Ιεράς Μονής Σταυρονικήτα. Άγιον Όρος."),
    SRC("Mancini, G. (c. 1620). Considerazioni sulla pittura, ed. Marucchi, A. (1956). Rome: Accademia dei Lincei, vol. 1, 230; Κωνσταντουδάκη-Κιτρομηλίδου, Μ. (1975). Ο Δομήνικος Θεοτοκόπουλος (El Greco) από το Χάνδακα στη Βενετία. Θησαυρίσματα 12: 292–308."),
    SRC("Davies, D. (ed.) (2003). El Greco. London: National Gallery Company."),
    SRC("Brown, J. (ed.) (1982). El Greco of Toledo. Boston: Little, Brown; Μουσείο Μπενάκη (1990). Ο Γκρέκο στην Ελλάδα (catalogue)."),
    SRC("The Metropolitan Museum of Art, El Greco, View of Toledo (29.100.6).", "https://www.metmuseum.org/art/collection/search/436575"),
    SRC("Κωνσταντουδάκη-Κιτρομηλίδου, Μ. (1990). Ο Δομήνικος Θεοτοκόπουλος και η Κοίμηση της Σύρου. In Ο Γκρέκο στην Ελλάδα. Αθήνα: Μουσείο Μπενάκη; Hadjinicolaou, N. (ed.) (1995). El Greco of Crete. Iraklion: Municipality of Iraklion."),
  ]))

# 8.3 language
CH.append(dict(id="e8-erotokritos", theme="language", el="Ο Ερωτόκριτος και η Κρητική Αναγέννηση", title="Erotokritos and the Cretan Renaissance", dates="περ. 1590–1713",
  image="erotokritos",
  summary_en="The literature of Venetian Crete, written in the island's dialect: Chortatzis's tragedy Erofili, the religious drama The Sacrifice of Abraham, and Kornaros's Erotokritos, 10,012 rhyming lines that Greek villagers learned by heart.",
  sections=[
    S("renaissance", "Μια λογοτεχνία στη γλώσσα του λαού", "A literature in the people's language", [
      P("Στα τέλη του 16ου και στις αρχές του 17ου αιώνα, στην ειρηνική και σχετικά ευημερούσα Κρήτη, συντελέστηκε κάτι πρωτόγνωρο: μορφωμένοι Κρητικοί, που γνώριζαν άριστα την ιταλική λογοτεχνία, άρχισαν να γράφουν θέατρο και ποίηση όχι στη λόγια γλώσσα, αλλά στη ζωντανή κρητική διάλεκτο. Ο Γεώργιος Χορτάτσης έγραψε γύρω στο 1600 την «Ερωφίλη», μια τραγωδία με πρότυπο ένα ιταλικό έργο, ενώ η «Θυσία του Αβραάμ», ένα θρησκευτικό δράμα, συγκινεί ακόμα με την απλότητά της.",
        "In the late sixteenth and early seventeenth centuries, in a peaceful and relatively prosperous Crete, something unprecedented happened: educated Cretans with a thorough knowledge of Italian literature began to write drama and poetry not in the learned language but in the living Cretan dialect. Georgios Chortatzis wrote Erofili around 1600, a tragedy modelled on Giraldi's Orbecche, while The Sacrifice of Abraham, a religious drama, still moves readers with its simplicity.", [1, 2]),
    ]),
    S("poem", "Δέκα χιλιάδες στίχοι", "Ten thousand lines", [
      P("Το κορυφαίο έργο της εποχής είναι ο «Ερωτόκριτος» του Βιτσέντζου Κορνάρου, ένα έμμετρο μυθιστόρημα 10.012 δεκαπεντασύλλαβων στίχων με ζευγαρωτή ομοιοκαταληξία. Αφηγείται τον έρωτα του Ερωτόκριτου, γιου ενός συμβούλου του βασιλιά της Αθήνας, για την πριγκίπισσα Αρετούσα. Ο βασιλιάς εξορίζει τον νέο, φυλακίζει την κόρη του που αρνείται κάθε άλλο γαμπρό, και η ιστορία λύνεται μόνο όταν ο Ερωτόκριτος, μεταμφιεσμένος, σώζει το βασίλειο σε πόλεμο. Το έργο ξεκινά με τους περίφημους στίχους:",
        "The masterpiece of the age is Erotokritos by Vitsentzos (Vincenzo) Kornaros, a verse romance of 10,012 fifteen-syllable lines in rhyming couplets. It tells of the love of Erotokritos, son of a counsellor of the king of Athens, for the princess Aretousa. The king exiles the young man and imprisons his daughter, who refuses every other suitor, and the story is resolved only when Erotokritos, in disguise, saves the kingdom in war. The work opens with the famous lines:", [3, 4]),
      P("«Του κύκλου τα γυρίσματα, που ανεβοκατεβαίνουν, / και του τροχού, που ώρες ψηλά κι ώρες στα βάθη πηαίνουν, / με του καιρού τα πάθη του, που αναπαημό δεν έχουν, / μα στο καλό κι εις το κακό περιπατούν και τρέχουν». Η εικόνα του τροχού της τύχης, που ανεβάζει και κατεβάζει τους ανθρώπους, είναι μεσαιωνική και ευρωπαϊκή, αλλά η γλώσσα, με τύπους όπως «πηαίνουν» αντί για «πηγαίνουν» και «αναπαημός» αντί για «ανάπαυση», είναι καθαρά κρητική.",
        "'The turns of the circle, which go up and down, / and of the wheel, which now high and now into the depths goes, / with the changes of time, which know no rest, / but towards good and towards bad they walk and run.' The image of the wheel of fortune, raising and lowering people, is medieval and European, but the language, with forms such as πηαίνουν for πηγαίνουν 'they go' and αναπαημός for ανάπαυση 'rest', is purely Cretan.", [4, 5]),
    ]),
    S("memory", "Από το τυπογραφείο στο στόμα του λαού", "From the press to the people's lips", [
      P("Μετά την κατάληψη της Κρήτης από τους Οθωμανούς το 1669, πολλοί Κρητικοί κατέφυγαν στα Επτάνησα και στη Βενετία, παίρνοντας μαζί τους τα χειρόγραφα. Ο «Ερωτόκριτος» τυπώθηκε για πρώτη φορά στη Βενετία το 1713 και από τότε επανεκδόθηκε δεκάδες φορές σε φτηνές λαϊκές εκδόσεις. Οι στίχοι του διαδόθηκαν σε όλο τον ελληνόφωνο κόσμο, και ως τον 20ό αιώνα αγράμματοι χωρικοί και βοσκοί ήξεραν απέξω χιλιάδες από αυτούς, τους οποίους τραγουδούσαν με τη λύρα.",
        "After the Ottoman conquest of Crete in 1669, many Cretans fled to the Ionian Islands and to Venice, taking the manuscripts with them. Erotokritos was first printed in Venice in 1713 (by Antonio Bortoli) and was reprinted dozens of times in cheap popular editions. Its lines spread throughout the Greek-speaking world, and until the twentieth century illiterate villagers and shepherds knew thousands of them by heart and sang them to the lyra.", [3, 6]),
      P("Ο Γιώργος Σεφέρης, σε ένα γνωστό δοκίμιό του, έγραψε ότι ο «Ερωτόκριτος» είναι ίσως το μόνο έργο της νεοελληνικής λογοτεχνίας που αγκάλιασε πραγματικά ολόκληρο τον λαό. Για τη γλώσσα το έργο έχει κι άλλη σημασία: απέδειξε, αιώνες πριν από τη νίκη της δημοτικής, ότι η ομιλούμενη γλώσσα μπορεί να σηκώσει το βάρος μιας μεγάλης λογοτεχνίας. Οι Επτανήσιοι ποιητές του 19ου αιώνα, όπως ο Διονύσιος Σολωμός, θεώρησαν την κρητική ποίηση πρόγονό τους.",
        "Giorgos Seferis, in a well-known essay (1946), wrote that Erotokritos is perhaps the only work of Modern Greek literature that truly embraced the whole people. For the language it has a further significance: it proved, centuries before the victory of dimotiki, that the spoken language could carry the weight of a great literature. The Ionian poets of the nineteenth century, such as Dionysios Solomos, considered Cretan poetry their ancestor.", [7, 8]),
    ]),
  ],
  grammar=[
    G("C1", "Reading older and dialect forms", "Παλαιότεροι και διαλεκτικοί τύποι",
      "Early modern and dialect texts use forms you can decode by analogy: loss of intervocalic γ (πηαίνουν = πηγαίνουν, λέω < λέγω), εις for σε (εις το κακό), κι for και before vowels, final -ν kept (πολλήν), -ουσι/-ασι for -ουν/-αν (λέγουσι), and older vocabulary (αναπαημός 'rest', ώρες ... ώρες 'sometimes ... sometimes'). Read aloud: the metre helps.",
      [("που ώρες ψηλά κι ώρες στα βάθη πηαίνουν", "which now go high, now into the depths"),
       ("μα στο καλό κι εις το κακό περιπατούν και τρέχουν", "but towards good and towards bad they walk and run")]),
    G("C1", "Learned passive aorists in formal narrative: συντελέστηκε, επανεκδόθηκε", "Λόγιοι παθητικοί αόριστοι",
      "Formal narrative favours learned verbs with passive aorists: συντελούμαι → συντελέστηκε 'took place, was accomplished', επανεκδίδομαι → επανεκδόθηκε 'was reissued', διαδίδομαι → διαδόθηκε 'spread', αποδεικνύομαι → αποδείχτηκε. The augment of εκδίδω-type verbs stays inside the prefix only in the active (εξέδωσε) and disappears in the passive (εκδόθηκε).",
      [("Στην Κρήτη συντελέστηκε κάτι πρωτόγνωρο.", "Something unprecedented happened in Crete."),
       ("Το έργο επανεκδόθηκε δεκάδες φορές.", "The work was reissued dozens of times.")]),
  ],
  terms=[
    T("πρωτόγνωρος", "unprecedented, unheard-of", "Που συμβαίνει ή γίνεται γνωστός για πρώτη φορά.", "Happening or known for the first time."),
    T("έμμετρος", "in verse, metrical", "Γραμμένος σε στίχους με μέτρο.", "Written in metrical lines."),
    T("η ομοιοκαταληξία", "rhyme", "Η ομοιότητα στον ήχο του τέλους δύο ή περισσότερων στίχων.", "Sound-likeness at the end of two or more lines."),
    T("ζευγαρωτός", "in pairs, paired (of rhyme: couplets)", "Που πηγαίνει ανά δύο.", "Going in twos."),
    T("μεταμφιεσμένος", "disguised", "Που έχει αλλάξει την εμφάνισή του για να μην αναγνωριστεί.", "Having changed one's appearance to avoid recognition."),
    T("ο τροχός της τύχης", "wheel of fortune", "Εικόνα για την αστάθεια της ανθρώπινης τύχης.", "An image of the instability of human fortune."),
    T("απέξω", "by heart; from outside", "Από μνήμης, χωρίς να διαβάζει κανείς.", "From memory, without reading."),
    T("η λύρα", "lyra (Cretan bowed fiddle); lyre", "Έγχορδο όργανο με δοξάρι, χαρακτηριστικό της Κρήτης.", "A bowed string instrument typical of Crete."),
  ],
  questions=[
    Q("Ποια ήταν η καινοτομία των Κρητικών συγγραφέων;", ["Έγραψαν στη ζωντανή κρητική διάλεκτο", "Έγραψαν στα λατινικά", "Έγραψαν μόνο θρησκευτικά κείμενα", "Έγραψαν στα αρχαία ελληνικά"], 0, "Not in the learned language."),
    Q("Σε τι μέτρο είναι γραμμένος ο «Ερωτόκριτος»;", ["Σε δεκαπεντασύλλαβους στίχους με ζευγαρωτή ομοιοκαταληξία", "Σε ελεύθερο στίχο", "Σε πεζό λόγο", "Σε δακτυλικό εξάμετρο"], 0, "10,012 lines."),
    Q("Τι σημαίνει «πηαίνουν» στον Ερωτόκριτο;", ["Πηγαίνουν", "Πίνουν", "Πεινάνε", "Παίζουν"], 0, "Loss of intervocalic γ."),
    Q("Τι απέδειξε, κατά το κείμενο, ο «Ερωτόκριτος» για τη γλώσσα;", ["Ότι η ομιλούμενη γλώσσα μπορεί να στηρίξει μεγάλη λογοτεχνία", "Ότι η κρητική διάλεκτος είναι ακατανόητη", "Ότι η καθαρεύουσα είναι ανώτερη", "Ότι η ποίηση πρέπει να γράφεται στα ιταλικά"], 0, "Long before dimotiki won."),
  ],
  vocab=["ευημερώ", "συντελούμαι", "πρωτόγνωρος", "άριστα", "πρότυπο", "συγκινώ", "απλότητα", "έμμετρος", "ομοιοκαταληξία", "αφηγούμαι", "σύμβουλος", "φυλακίζω", "γαμπρός", "μεταμφιεσμένος", "τροχός", "τύχη", "τυπώνω", "επανεκδίδω", "χωρικός", "βοσκός", "απέξω", "αγκαλιάζω", "ομιλούμενος", "βάρος"],
  sources=[
    SRC("Holton, D. (ed.) (1991). Literature and Society in Renaissance Crete. Cambridge University Press."),
    SRC("Χορτάτσης, Γ. Ερωφίλη, έκδ. Αλεξίου, Σ., & Αποσκίτη, Μ. (1988). Αθήνα: Στιγμή; Η Θυσία του Αβραάμ, έκδ. Μέγας, Γ. Α. (1954). Αθήνα: Ίκαρος."),
    SRC("Κορνάρος, Β. Ερωτόκριτος, κριτική έκδοση Αλεξίου, Σ. (1980). Αθήνα: Ερμής."),
    SRC("Holton, D. (1991). Erotokritos. Bristol: Bristol Classical Press."),
    SRC("Ερωτόκριτος Α΄ 1–4 (Αλεξίου 1980); Κριαράς, Ε. Λεξικό της μεσαιωνικής ελληνικής δημώδους γραμματείας 1100–1669, λ. αναπαημός.", "https://www.greek-language.gr/greekLang/medieval_greek/kriaras/"),
    SRC("Πολίτης, Λ. (1978). Ιστορία της νεοελληνικής λογοτεχνίας. Αθήνα: ΜΙΕΤ, κεφ. 5; Βενετία, Antonio Bortoli, 1713 (editio princeps)."),
    SRC("Σεφέρης, Γ. (1946). Ερωτόκριτος. In Δοκιμές, τ. 1. Αθήνα: Ίκαρος."),
    SRC("Beaton, R. (1999). An Introduction to Modern Greek Literature. 2nd ed. Oxford: Clarendon Press, ch. 1."),
  ]))

# 8.4 science
CH.append(dict(id="e8-enlightenment", theme="science", el="Ο Νεοελληνικός Διαφωτισμός: φυσική, γλώσσα και ελευθερία", title="The Modern Greek Enlightenment: physics, language and freedom", dates="περ. 1750–1821",
  image="rigas-physics",
  summary_en="How Greek merchants, teachers and printers brought Newtonian science and the ideas of the French Revolution to the Greek world: the new schools, Rigas Velestinlis and his execution in 1798, Adamantios Korais's 'middle way' in language, and the journal Hermes o Logios.",
  sections=[
    S("schools", "Έμποροι, σχολεία και τυπογραφεία", "Merchants, schools and printing presses", [
      P("Τον 18ο αιώνα μια δυναμική τάξη Ελλήνων εμπόρων, εγκατεστημένων στη Βιέννη, στην Τεργέστη, στη Βενετία, στην Οδησσό και στο Λιβόρνο, απέκτησε πλούτο, επαφές και, κυρίως, πρόσβαση στις ιδέες της Ευρώπης. Με τα χρήματά τους χρηματοδοτήθηκαν σχολεία και βιβλία, που τυπώνονταν σχεδόν όλα έξω από την οθωμανική επικράτεια. Στις Κυδωνίες της Μικράς Ασίας, στη Χίο, στα Ιωάννινα και στη Σμύρνη λειτούργησαν σχολές με εργαστήρια φυσικής και χημείας, όπου διδάσκονταν ο Νεύτωνας και η πειραματική μέθοδος.",
        "In the eighteenth century a dynamic class of Greek merchants, settled in Vienna, Trieste, Venice, Odessa and Livorno, acquired wealth, contacts and, above all, access to the ideas of Europe. Their money funded schools and books, nearly all printed outside Ottoman territory. At Kydonies (Ayvalık) in Asia Minor, on Chios, in Ioannina and Smyrna there were schools with physics and chemistry laboratories, where Newton and the experimental method were taught.", [1, 2]),
      P("Το κίνημα αυτό, που ο ιστορικός Κ. Θ. Δημαράς ονόμασε «Νεοελληνικό Διαφωτισμό», δεν περιορίστηκε στις θετικές επιστήμες. Οι λόγιοί του, όπως ο Ευγένιος Βούλγαρης και ο Νικηφόρος Θεοτόκης, μετέφρασαν και συνέγραψαν εγχειρίδια λογικής, γεωγραφίας και αστρονομίας, ενώ οι νεότεροι, επηρεασμένοι από τη Γαλλική Επανάσταση, συνέδεσαν τη γνώση με την ιδέα της πολιτικής ελευθερίας. Η σύγκρουση με τους συντηρητικούς κύκλους του Πατριαρχείου, που έβλεπαν στις νέες ιδέες απειλή για την πίστη, ήταν αναπόφευκτη.",
        "This movement, which the historian K. Th. Dimaras named the 'Modern Greek Enlightenment', was not confined to the natural sciences. Its scholars, such as Eugenios Voulgaris and Nikiforos Theotokis, translated and wrote textbooks of logic, geography and astronomy, while the younger generation, influenced by the French Revolution, linked knowledge to the idea of political freedom. Conflict with the conservative circles of the Patriarchate, who saw the new ideas as a threat to the faith, was inevitable; a patriarchal encyclical of 1819 condemned the teaching of the sciences.", [1, 3]),
    ]),
    S("rigas", "Ρήγας Βελεστινλής", "Rigas Velestinlis", [
      P("Ο Ρήγας, που γεννήθηκε στο Βελεστίνο της Θεσσαλίας το 1757, υπηρέτησε ως γραμματέας Φαναριωτών ηγεμόνων στη Βλαχία, πριν εγκατασταθεί στη Βιέννη. Το 1790 εξέδωσε το «Φυσικής απάνθισμα», μια ανθολογία φυσικών γνώσεων «διά τους αγχίνους και φιλομαθείς Έλληνας», όπως γράφει στον τίτλο. Το 1797 τύπωσε τη μεγάλη «Χάρτα» της Ελλάδας και ένα σχέδιο συντάγματος για μια δημοκρατία όπου όλοι οι λαοί των Βαλκανίων, χριστιανοί και μουσουλμάνοι, θα ήταν ίσοι πολίτες.",
        "Rigas, born at Velestino in Thessaly in 1757, served as secretary to Phanariot princes in Wallachia before settling in Vienna. In 1790 he published the Anthology of Physics (Φυσικής απάνθισμα), 'for the quick-witted and learning-loving Greeks', as the title says. In 1797 he printed his great Charta (map) of Greece and a draft constitution for a republic in which all the peoples of the Balkans, Christians and Muslims, would be equal citizens.", [4, 5]),
      P("Ο «Θούριός» του, ένα επαναστατικό τραγούδι, έγινε σύνθημα μιας ολόκληρης γενιάς: «Ως πότε, παλικάρια, θα ζούμε στα στενά, / μονάχοι σαν λιοντάρια, στες ράχες, στα βουνά;» και, λίγο πιο κάτω, «Καλύτερα μιας ώρας ελεύθερη ζωή, / παρά σαράντα χρόνια σκλαβιά και φυλακή». Τον Δεκέμβριο του 1797 οι αυστριακές αρχές τον συνέλαβαν στην Τεργέστη και τον παρέδωσαν στους Οθωμανούς. Τον Ιούνιο του 1798 στραγγαλίστηκε με τους συντρόφους του στο Βελιγράδι.",
        "His Thourios ('war song'), a revolutionary hymn, became the watchword of a whole generation: 'How long, brave lads, shall we live in the narrow passes, / alone like lions, on the ridges, on the mountains?' and, a little further on, 'Better one hour of free life / than forty years of slavery and prison.' In December 1797 the Austrian authorities arrested him in Trieste and handed him over to the Ottomans. In June 1798 he was strangled with his companions in Belgrade.", [5, 6]),
    ]),
    S("korais", "Ο Κοραής και η «μέση οδός»", "Korais and the 'middle way'", [
      P("Ο Αδαμάντιος Κοραής (1748–1833), γιατρός από τη Σμύρνη που έζησε στο Παρίσι από το 1788, είδε με τα μάτια του τη Γαλλική Επανάσταση και αφιέρωσε τη ζωή του στην «παιδεία του γένους». Στην «Ελληνική Βιβλιοθήκη» του εξέδωσε αρχαίους συγγραφείς με εκτενείς προλόγους στη νέα γλώσσα, πεπεισμένος ότι η γνώση της αρχαιότητας θα αφύπνιζε τους υπόδουλους Έλληνες. Για τη γλώσσα πρότεινε μια «μέση οδό»: να μην υιοθετηθεί ούτε η αρχαΐζουσα γλώσσα των λογίων ούτε η «χυδαία» ομιλουμένη ως είχε, αλλά η ομιλουμένη, «διορθωμένη» με βάση την αρχαία. Από αυτή την πρόταση γεννήθηκε τελικά η καθαρεύουσα.",
        "Adamantios Korais (1748–1833), a physician from Smyrna who lived in Paris from 1788, witnessed the French Revolution and devoted his life to the 'education of the nation'. In his Hellenic Library he edited ancient authors with long prefaces in the modern language, convinced that knowledge of antiquity would awaken the enslaved Greeks. For the language he proposed a 'middle way': to adopt neither the archaising language of the scholars nor the 'vulgar' spoken tongue as it was, but the spoken language 'corrected' on the basis of the ancient. From this proposal katharevousa was eventually born.", [7, 8]),
      P("Το 1811 άρχισε να κυκλοφορεί στη Βιέννη ο «Ερμής ο Λόγιος», το πρώτο σημαντικό ελληνικό φιλολογικό και επιστημονικό περιοδικό, με άρθρα για τη φυσική, τη χημεία, τη γλώσσα και την παιδεία. Κυκλοφόρησε ως το 1821. Μέσα σε δύο γενιές, η ιδέα ότι οι Έλληνες ήταν ένα έθνος με δικαίωμα σε δικό του κράτος είχε περάσει από τα βιβλία των λογίων στη συνείδηση πολλών.",
        "In 1811 Hermes o Logios ('Hermes the Learned') began to appear in Vienna, the first important Greek literary and scientific periodical, with articles on physics, chemistry, language and education. It ran until 1821. Within two generations the idea that the Greeks were a nation with a right to their own state had passed from the scholars' books into the consciousness of many.", [9]),
    ]),
  ],
  grammar=[
    G("C1", "Katharevousa endings you will meet in older titles", "Τύποι της καθαρεύουσας σε τίτλους και αποσπάσματα",
      "Older texts and titles use ancient forms: διά + acc. 'for', accusative plural -ας for masculines (τους Έλληνας = τους Έλληνες), genitive -εως (της πόλεως = της πόλης), infinitives (το γράφειν), participles in -ων/-ούσα. In Φυσικής απάνθισμα the genitive comes first, as in ancient Greek: 'Anthology of Physics'. Recognise them; you do not need to produce them.",
      [("διά τους αγχίνους και φιλομαθείς Έλληνας", "for the quick-witted and learning-loving Greeks"),
       ("η παιδεία του γένους", "the education of the nation")]),
    G("C1", "Neither ... nor ... but: ούτε ... ούτε ..., αλλά", "Σύνθετη άρνηση με διόρθωση",
      "A C1 argument often rejects two options and proposes a third: να μην υιοθετηθεί ούτε το Α ούτε το Β, αλλά το Γ. After a negative main verb (δεν/μην), ούτε ... ούτε needs no further negation. Compare όχι μόνο ... αλλά και 'not only ... but also' and μάλλον 'rather' to soften the alternative.",
      [("Να μην υιοθετηθεί ούτε η αρχαΐζουσα ούτε η χυδαία, αλλά η ομιλουμένη διορθωμένη.", "Adopt neither the archaising nor the vulgar, but the spoken language corrected."),
       ("Δεν ήταν μόνο επιστήμη, αλλά και πολιτική.", "It was not only science, but also politics.")]),
  ],
  terms=[
    T("ο Διαφωτισμός", "the Enlightenment", "Το πνευματικό κίνημα του 18ου αιώνα που πίστευε στη λογική και στην επιστήμη.", "The 18th-century movement that trusted reason and science."),
    T("η επικράτεια", "territory (of a state)", "Η περιοχή στην οποία ασκεί εξουσία ένα κράτος.", "The area over which a state rules."),
    T("οι θετικές επιστήμες", "the (natural) sciences", "Τα μαθηματικά, η φυσική, η χημεία και οι συγγενείς επιστήμες.", "Mathematics, physics, chemistry and related sciences."),
    T("το εγχειρίδιο", "textbook, manual", "Βιβλίο που παρουσιάζει συστηματικά τις βασικές γνώσεις ενός θέματος.", "A book presenting the basics of a subject systematically."),
    T("αναπόφευκτος", "inevitable", "Που δεν μπορεί να αποφευχθεί.", "Impossible to avoid."),
    T("ο θούριος", "war song, martial hymn", "Επαναστατικό ή πολεμικό τραγούδι που εμψυχώνει.", "A rousing revolutionary or martial song."),
    T("υπόδουλος", "enslaved, subjugated", "Που ζει κάτω από ξένη κυριαρχία, χωρίς ελευθερία.", "Living under foreign rule, without freedom."),
    T("η καθαρεύουσα", "katharevousa", "Η λόγια μορφή της νέας ελληνικής, «καθαρισμένη» με αρχαία στοιχεία.", "The learned form of Modern Greek, 'purified' with ancient elements."),
  ],
  questions=[
    Q("Ποιος ήταν ο ρόλος των Ελλήνων εμπόρων της διασποράς;", ["Χρηματοδότησαν σχολεία και βιβλία", "Έγραψαν τα εγχειρίδια φυσικής", "Κυβέρνησαν τη Βλαχία", "Απαγόρευσαν τις νέες ιδέες"], 0, "Money and contacts."),
    Q("Γιατί συγκρούστηκε ο Διαφωτισμός με κύκλους του Πατριαρχείου;", ["Γιατί έβλεπαν τις νέες ιδέες ως απειλή για την πίστη", "Γιατί το Πατριαρχείο ήθελε περισσότερη επιστήμη", "Γιατί οι λόγιοι ήταν Οθωμανοί", "Γιατί δεν υπήρχαν σχολεία"], 0, "The encyclical of 1819."),
    Q("Τι προέβλεπε το σχέδιο συντάγματος του Ρήγα;", ["Ίσα δικαιώματα για όλους τους λαούς των Βαλκανίων", "Μια μοναρχία μόνο για Έλληνες", "Την επιστροφή του Βυζαντίου", "Την ένωση με την Αυστρία"], 0, "Christians and Muslims as equal citizens."),
    Q("Τι πρότεινε ο Κοραής για τη γλώσσα;", ["Την ομιλουμένη, διορθωμένη με βάση την αρχαία", "Την αρχαία ελληνική", "Τη γαλλική", "Την ομιλουμένη χωρίς καμία αλλαγή"], 0, "The 'middle way'."),
  ],
  vocab=["δυναμικός", "εγκατεστημένος", "πρόσβαση", "χρηματοδοτώ", "επικράτεια", "πειραματικός", "περιορίζομαι", "συγγράφω", "εγχειρίδιο", "συνδέω", "σύγκρουση", "συντηρητικός", "απειλή", "αναπόφευκτος", "υπηρετώ", "ανθολογία", "σύνταγμα", "σύνθημα", "συλλαμβάνω", "στραγγαλίζω", "εκτενής", "πεπεισμένος", "αφυπνίζω", "συνείδηση"],
  sources=[
    SRC("Δημαράς, Κ. Θ. (1977). Νεοελληνικός Διαφωτισμός. Αθήνα: Ερμής."),
    SRC("Kitromilides, P. M. (2013). Enlightenment and Revolution: The Making of Modern Greece. Cambridge, MA: Harvard University Press."),
    SRC("Patriarchal encyclical of 1819 against the sciences, in Κιτρομηλίδης, Π. Μ. (1996). Νεοελληνικός Διαφωτισμός: Οι πολιτικές και κοινωνικές ιδέες. Αθήνα: ΜΙΕΤ."),
    SRC("Ρήγας Βελεστινλής (1790). Φυσικής απάνθισμα διά τους αγχίνους και φιλομαθείς Έλληνας. Βιέννη; Βουλή των Ελλήνων (2000). Ρήγας Βελεστινλής: Άπαντα τα σωζόμενα, τ. 1–5."),
    SRC("Woodhouse, C. M. (1995). Rhigas Velestinlis: The Proto-Martyr of the Greek Revolution. Limni: Denise Harvey."),
    SRC("Ρήγας, Θούριος, στ. 1–2, 9–10 (Βιέννη, 1797); Βρανούσης, Λ. (1968). Ρήγας Βελεστινλής. Αθήνα: Βασική Βιβλιοθήκη."),
    SRC("Korais, A. (1803). Mémoire sur l'état actuel de la civilisation dans la Grèce. Paris; Κοραής, Α. Ελληνική Βιβλιοθήκη (1805–1826), Παρίσι."),
    SRC("Mackridge, P. (2009). Language and National Identity in Greece, 1766–1976. Oxford University Press, ch. 4."),
    SRC("Ερμής ο Λόγιος (1811–1821), Βιέννη; Σκοπετέα, Έ. (1988). Το «πρότυπο βασίλειο» και η Μεγάλη Ιδέα. Αθήνα: Πολύτυπο."),
  ]))

# 8.5 culture
CH.append(dict(id="e8-klephts", theme="culture", el="Κλέφτες, δημοτικά τραγούδια και Φιλική Εταιρεία", title="Klephts, folk songs and the Society of Friends", dates="περ. 1600–1821",
  image="olympus-lear",
  summary_en="The klephts and armatoles of the mountains, the folk songs that told their story and later shaped Greek poetry, the first collections by Fauriel, and the secret Society of Friends whose revolt began in 1821.",
  sections=[
    S("klephts", "Οι κλέφτες και οι αρματολοί", "Klephts and armatoles", [
      P("Στα βουνά της ηπειρωτικής Ελλάδας, όπου η οθωμανική εξουσία ήταν πάντα πιο αδύναμη, δρούσαν ένοπλες ομάδες που ο λαός ονόμαζε «κλέφτες». Ήταν, στην πραγματικότητα, ένα μείγμα ληστών και ανταρτών: λήστευαν εμπόρους και γαιοκτήμονες, χριστιανούς και μουσουλμάνους, αλλά ήταν και οι μόνοι που αντιστέκονταν ανοιχτά στις αρχές. Για να τους περιορίσουν, οι Οθωμανοί προσέλαβαν άλλους ενόπλους χριστιανούς, τους «αρματολούς», ως τοπική πολιτοφυλακή. Τα όρια ανάμεσα στις δύο ομάδες ήταν ρευστά: ο χθεσινός κλέφτης γινόταν αύριο αρματολός, και αντίστροφα.",
        "In the mountains of mainland Greece, where Ottoman authority was always weaker, armed bands operated that the people called klephts ('thieves'). They were in fact a mixture of brigands and rebels: they robbed merchants and landowners, Christians and Muslims, but were also the only ones openly resisting the authorities. To contain them the Ottomans hired other armed Christians, the armatoles, as a local militia. The boundary between the two was fluid: yesterday's klepht became tomorrow's armatole, and vice versa.", [1, 2]),
    ]),
    S("songs", "Τα κλέφτικα τραγούδια", "The klephtic songs", [
      P("Τη ζωή, τις μάχες και τον θάνατο των κλεφτών τα τραγούδησαν τα «κλέφτικα» δημοτικά τραγούδια, γραμμένα συνήθως σε δεκαπεντασύλλαβο, χωρίς ομοιοκαταληξία, με λιτή γλώσσα και τολμηρές εικόνες. Σε ένα από τα πιο γνωστά, ο Όλυμπος και ο Κίσαβος, τα δύο βουνά της Θεσσαλίας, μαλώνουν. Ο Όλυμπος καυχιέται: «Μη με μαλώνεις, Κίσαβε, κονιαροπατημένε, / εγώ είμ' ο γέρος Όλυμπος, στον κόσμο ξακουσμένος· / έχω σαράντα δυο κορφές κι εξήντα δυο βρυσούλες, / κάθε κορφή και φλάμπουρο, κάθε κλαρί και κλέφτης».",
        "The life, battles and death of the klephts were sung in the 'klephtic' folk songs, usually in fifteen-syllable lines without rhyme, in spare language and with bold images. In one of the best known, Olympus and Kissavos (Ossa), the two mountains of Thessaly, quarrel. Olympus boasts: 'Do not scold me, Kissavos, you who are trampled by Turks (konyar), / I am old Olympus, famous throughout the world; / I have forty-two peaks and sixty-two little springs, / on every peak a banner, on every branch a klepht.'", [3, 4]),
      P("Το 1824–1825 ο Γάλλος λόγιος Κλοντ Φοριέλ δημοσίευσε στο Παρίσι τα «Τραγούδια του σύγχρονου ελληνικού λαού», την πρώτη μεγάλη συλλογή, με γαλλική μετάφραση. Μέσα στον ενθουσιασμό του φιλελληνισμού, η έκδοση έκανε γνωστή την ελληνική λαϊκή ποίηση σε όλη την Ευρώπη, και ο Γκαίτε μετέφρασε ορισμένα τραγούδια στα γερμανικά. Για τους Έλληνες ποιητές του 19ου και του 20ού αιώνα, από τον Σολωμό ως τον Σεφέρη και τον Ελύτη, τα δημοτικά τραγούδια έγιναν το μέτρο της αυθεντικής ελληνικής έκφρασης.",
        "In 1824–1825 the French scholar Claude Fauriel published in Paris his Chants populaires de la Grèce moderne, the first large collection, with a French translation. Amid the enthusiasm of philhellenism, the edition made Greek folk poetry known across Europe, and Goethe translated some of the songs into German. For Greek poets of the nineteenth and twentieth centuries, from Solomos to Seferis and Elytis, the folk songs became the measure of authentic Greek expression.", [4, 5]),
    ]),
    S("etaireia", "Η Φιλική Εταιρεία", "The Society of Friends", [
      P("Το 1814 τρεις Έλληνες έμποροι της Οδησσού, ο Νικόλαος Σκουφάς, ο Εμμανουήλ Ξάνθος και ο Αθανάσιος Τσακάλωφ, ίδρυσαν μια μυστική οργάνωση, τη Φιλική Εταιρεία, με σκοπό την απελευθέρωση του γένους. Η οργάνωση, με όρκους, συνθηματικά ονόματα και αυστηρή ιεραρχία στα πρότυπα των μασονικών στοών, απλώθηκε γρήγορα σε όλο τον ελληνικό κόσμο. Η επιτυχία της στηρίχτηκε εν μέρει σε μια σκόπιμη ασάφεια: πολλοί μυούμενοι πίστευαν ότι πίσω από την «Αρχή» της Εταιρείας κρυβόταν η Ρωσία.",
        "In 1814 three Greek merchants of Odessa, Nikolaos Skoufas, Emmanouil Xanthos and Athanasios Tsakaloff, founded a secret organisation, the Philiki Etaireia (Society of Friends), with the aim of liberating the nation. With oaths, code names and a strict hierarchy modelled on Masonic lodges, it spread rapidly across the Greek world. Its success rested partly on a deliberate ambiguity: many initiates believed that behind the Society's secret 'Authority' stood Russia itself.", [6, 7]),
      P("Τον Φεβρουάριο του 1821 ο αρχηγός της, ο Αλέξανδρος Υψηλάντης, αξιωματικός του ρωσικού στρατού, πέρασε τον ποταμό Προύθο στη Μολδαβία και κήρυξε την επανάσταση. Το κίνημα στις παραδουνάβιες ηγεμονίες απέτυχε, αλλά λίγες εβδομάδες αργότερα ξεσηκώθηκε η Πελοπόννησος, και το 1821 έγινε η αρχή του νέου ελληνικού κράτους. Η επέτειος γιορτάζεται στις 25 Μαρτίου, γιορτή του Ευαγγελισμού, μια ημερομηνία που επικράτησε περισσότερο για τον συμβολισμό της παρά επειδή εκείνη την ημέρα άρχισε πράγματι ο αγώνας. Εδώ τελειώνει αυτό το βιβλίο, και αρχίζει η ιστορία της σύγχρονης Ελλάδας.",
        "In February 1821 its leader, Alexandros Ypsilantis, an officer in the Russian army, crossed the river Prut into Moldavia and proclaimed the revolution (22 February, Old Style). The rising in the Danubian Principalities failed, but a few weeks later the Peloponnese rose, and 1821 became the beginning of the modern Greek state. The anniversary is celebrated on 25 March, the feast of the Annunciation, a date that prevailed more for its symbolism than because the struggle actually began on that day. Here this book ends, and the history of modern Greece begins.", [7, 8]),
    ]),
  ],
  grammar=[
    G("C1", "Compound epithets and augmentatives in folk poetry", "Σύνθετα επίθετα και υποκοριστικά στο δημοτικό τραγούδι",
      "Folk songs build vivid compounds: κονιαροπατημένος 'trodden by Turks' (Κονιάρος, a Turk from Konya + πατημένος), μαυρομάτα 'black-eyed girl', λιγνόκορμος 'slender', ασπροπρόσωπος 'honourable'. Older or poetic elisions are common: είμ' ο = είμαι ο. Diminutives in -ούλα/-ούλι add tenderness or smallness (βρυσούλα 'little spring', πουλάκι). In your own writing use them sparingly; in reading, split them into their parts.",
      [("Μη με μαλώνεις, Κίσαβε, κονιαροπατημένε.", "Do not scold me, Kissavos, you trodden by Turks."),
       ("Έχω σαράντα δυο κορφές κι εξήντα δυο βρυσούλες.", "I have forty-two peaks and sixty-two little springs.")]),
    G("C1", "Comparing reasons: περισσότερο για ... παρά επειδή", "Σύγκριση αιτιών",
      "To weigh two explanations: περισσότερο για + noun/για να ... παρά επειδή/γιατί ... 'more for ... than because ...'. Variants: όχι τόσο επειδή ... όσο επειδή 'not so much because ... as because', λιγότερο ... και περισσότερο. Typical of academic and journalistic C1 prose.",
      [("Η ημερομηνία επικράτησε περισσότερο για τον συμβολισμό της παρά επειδή άρχισε τότε ο αγώνας.", "The date prevailed more for its symbolism than because the struggle began then."),
       ("Πέτυχε όχι τόσο επειδή ήταν ισχυρή όσο επειδή φαινόταν ισχυρή.", "It succeeded not so much because it was strong as because it seemed strong.")]),
  ],
  terms=[
    T("ο κλέφτης", "klepht (rebel-brigand); thief", "Ένοπλος αντάρτης των βουνών επί Τουρκοκρατίας· σήμερα όποιος κλέβει.", "An armed mountain rebel under Ottoman rule; today a thief."),
    T("ο αρματολός", "armatole", "Χριστιανός ένοπλος στην υπηρεσία των Οθωμανών για την τήρηση της τάξης.", "An armed Christian in Ottoman service to keep order."),
    T("ο αντάρτης", "rebel, guerrilla", "Αυτός που πολεμά ένοπλα κατά της εξουσίας, συνήθως στα βουνά.", "One who fights authority with arms, usually in the mountains."),
    T("ρευστός", "fluid", "Που δεν έχει σταθερή μορφή ή σαφή όρια.", "Without fixed form or clear limits."),
    T("καυχιέμαι", "to boast", "Μιλώ με υπερηφάνεια για τα προσόντα μου.", "To talk proudly about one's own merits."),
    T("ο φιλελληνισμός", "philhellenism", "Το κίνημα συμπάθειας και στήριξης προς τον αγώνα των Ελλήνων τον 19ο αιώνα.", "The 19th-century movement supporting the Greek cause."),
    T("μυούμαι", "to be initiated", "Γίνομαι μέλος μιας μυστικής ομάδας με τελετή ή όρκο.", "To become a member of a secret group by ritual or oath."),
    T("η επέτειος", "anniversary", "Η μέρα που θυμόμαστε κάθε χρόνο ένα σημαντικό γεγονός.", "The day each year we remember an important event."),
  ],
  questions=[
    Q("Τι ήταν στην πραγματικότητα οι κλέφτες;", ["Ένα μείγμα ληστών και ανταρτών", "Οθωμανοί στρατιώτες", "Έμποροι της Οδησσού", "Μοναχοί του Αγίου Όρους"], 0, "Brigands and rebels."),
    Q("Γιατί ήταν ρευστά τα όρια ανάμεσα σε κλέφτες και αρματολούς;", ["Γιατί ο ίδιος άνθρωπος μπορούσε να περάσει από τη μία ομάδα στην άλλη", "Γιατί φορούσαν ίδια ρούχα", "Γιατί ζούσαν σε διαφορετικά βουνά", "Γιατί ήταν όλοι μουσουλμάνοι"], 0, "Yesterday's klepht, tomorrow's armatole."),
    Q("Ποια ήταν η σημασία της συλλογής του Φοριέλ;", ["Έκανε γνωστά τα ελληνικά δημοτικά τραγούδια στην Ευρώπη", "Ήταν η πρώτη έκδοση του Ερωτόκριτου", "Ήταν ένα σχέδιο συντάγματος", "Ήταν μια γραμματική της κρητικής διαλέκτου"], 0, "Paris, 1824–25."),
    Q("Γιατί επικράτησε η 25η Μαρτίου ως εθνική επέτειος;", ["Κυρίως για τον συμβολισμό της, τη γιορτή του Ευαγγελισμού", "Γιατί τότε πέρασε ο Υψηλάντης τον Προύθο", "Γιατί τότε ιδρύθηκε η Φιλική Εταιρεία", "Γιατί τότε πέθανε ο Ρήγας"], 0, "More symbol than precise date."),
  ],
  vocab=["ηπειρωτικός", "δρω", "ένοπλος", "μείγμα", "ληστής", "αντάρτης", "ληστεύω", "γαιοκτήμονας", "προσλαμβάνω", "πολιτοφυλακή", "ρευστός", "αντίστροφα", "τολμηρός", "μαλώνω", "καυχιέμαι", "ξακουσμένος", "κορφή", "ενθουσιασμός", "αυθεντικός", "απελευθέρωση", "ιεραρχία", "σκόπιμος", "ασάφεια", "επέτειος"],
  sources=[
    SRC("Koliopoulos, J. S. (1987). Brigands with a Cause: Brigandage and Irredentism in Modern Greece, 1821–1912. Oxford: Clarendon Press."),
    SRC("Βακαλόπουλος, Α. Ε. (1964–1980). Ιστορία του νέου ελληνισμού, τ. Β΄–Δ΄. Θεσσαλονίκη; Clogg, R. (2013). A Concise History of Greece. 3rd ed., ch. 1."),
    SRC("Πολίτης, Ν. Γ. (1914). Εκλογαί από τα τραγούδια του ελληνικού λαού. Αθήνα: Εστία, no. 1 («Ο Όλυμπος και ο Κίσαβος»)."),
    SRC("Fauriel, C. (1824–1825). Chants populaires de la Grèce moderne. 2 vols. Paris: Dondey-Dupré; Beaton, R. (1980). Folk Poetry of Modern Greece. Cambridge University Press."),
    SRC("Goethe, J. W. von (1825). Neugriechische Liebe-Skolien and Neugriechisch-epirotische Heldenlieder, in Über Kunst und Altertum 5.2; Mackridge, P. (2009). Language and National Identity in Greece, ch. 6."),
    SRC("Ξάνθος, Ε. (1845). Απομνημονεύματα περί της Φιλικής Εταιρίας. Αθήνα; Φράγκος, Γ. Δ. (1975). Η Φιλική Εταιρεία. In Ιστορία του Ελληνικού Έθνους, τ. ΙΑ΄. Αθήνα: Εκδοτική Αθηνών."),
    SRC("Mazower, M. (2021). The Greek Revolution: 1821 and the Making of Modern Europe. London: Allen Lane, ch. 1–4."),
    SRC("Royal Decree of 15 March 1838 establishing 25 March as the national holiday; Ξάνθος (1845) and Mazower (2021), ch. 3, on the actual beginnings of the revolt in March 1821."),
  ]))
