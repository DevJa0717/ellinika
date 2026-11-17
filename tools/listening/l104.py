# Source for library/listening/listening-104.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l104.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l104-ann-tiganelaio", "title": "Συλλογή χρησιμοποιημένου λαδιού", "title_en": "Collecting used cooking oil", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου στο τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος ενημερώνει τους κατοίκους ότι από την πρώτη Δεκεμβρίου ξεκινά πρόγραμμα συλλογής χρησιμοποιημένου λαδιού τηγανίσματος. Σε όλα τα σχολεία και σε δώδεκα σούπερ μάρκετ της πόλης θα τοποθετηθούν ειδικοί πορτοκαλί κάδοι.", "The municipality informs residents that from the first of December a programme for collecting used frying oil is starting. Special orange bins will be placed at all schools and at twelve supermarkets in the town."),
  L("Εκφωνήτρια", "f", "Οι κάτοικοι παρακαλούνται να αφήνουν το λάδι να κρυώσει, να το βάζουν σε πλαστικά μπουκάλια με καπάκι και να τα ρίχνουν κλειστά στους κάδους. Το λάδι δεν πρέπει να χύνεται στον νεροχύτη, γιατί φράζει τις αποχετεύσεις και ρυπαίνει τη θάλασσα.", "Residents are asked to let the oil cool, put it in plastic bottles with a cap and drop them, closed, into the bins. Oil must not be poured down the sink, because it blocks the drains and pollutes the sea."),
  L("Εκφωνήτρια", "f", "Το λάδι που θα συγκεντρωθεί θα μετατραπεί σε βιοντίζελ. Τα σχολεία που θα μαζέψουν τη μεγαλύτερη ποσότητα ως το τέλος της σχολικής χρονιάς θα κερδίσουν εκπαιδευτικό υλικό. Ο κατάλογος με τα σημεία συλλογής υπάρχει στην ιστοσελίδα του δήμου.", "The oil collected will be turned into biodiesel. The schools that collect the largest amount by the end of the school year will win educational materials. The list of collection points is on the municipality's website."),
 ],
 "questions": [
  Q("Πού θα τοποθετηθούν οι κάδοι;", ["Σε κάθε πολυκατοικία", "Μόνο στο δημαρχείο", "Σε όλα τα σχολεία και σε δώδεκα σούπερ μάρκετ", "Στα λιμάνια της πόλης"], 2, "Σε όλα τα σχολεία και σε δώδεκα σούπερ μάρκετ της πόλης"),
  Q("Γιατί δεν πρέπει να χύνεται το λάδι στον νεροχύτη;", ["Γιατί φράζει τις αποχετεύσεις και ρυπαίνει τη θάλασσα", "Γιατί είναι εύφλεκτο", "Γιατί χαλάει τις βρύσες", "Γιατί μυρίζει άσχημα"], 0, "φράζει τις αποχετεύσεις και ρυπαίνει τη θάλασσα"),
  Q("Τι θα κερδίσουν τα σχολεία που θα μαζέψουν τη μεγαλύτερη ποσότητα;", ["Μια εκδρομή", "Υπολογιστές", "Χρήματα για τη θέρμανση", "Εκπαιδευτικό υλικό"], 3, "θα κερδίσουν εκπαιδευτικό υλικό"),
 ],
 "gloss": {"τηγανίσματος": "τηγάνισμα — frying", "κάδοι": "κάδος — bin", "νεροχύτη": "νεροχύτης — sink", "φράζει": "φράζω — to block", "αποχετεύσεις": "αποχέτευση — drain, sewer", "ρυπαίνει": "ρυπαίνω — to pollute", "βιοντίζελ": "βιοντίζελ — biodiesel"}
})

ITEMS.append({
 "id": "l104-vm-logistria", "title": "Μήνυμα από τη λογίστρια για τη φορολογική δήλωση", "title_en": "A message from the accountant about the tax return", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα από τη λογίστριά σας στον τηλεφωνητή.",
 "script": [
  L("Λογίστρια", "f", "Καλημέρα, κύριε Σταθόπουλε, η Ρένα Μαυρίδη είμαι, από το λογιστικό γραφείο. Ετοιμάζω τη φορολογική σας δήλωση και μου λείπουν ακόμα δύο πράγματα.", "Good morning, Mr Stathopoulos, it's Rena Mavridi, from the accounting office. I'm preparing your tax return and I'm still missing two things."),
  L("Λογίστρια", "f", "Πρώτον, τη βεβαίωση από την τράπεζα για τους τόκους του στεγαστικού δανείου. Τη βρίσκετε στο e-banking, στην ενότητα «Βεβαιώσεις». Δεύτερον, τις αποδείξεις από τον φυσικοθεραπευτή, γιατί οι ιατρικές δαπάνες μειώνουν τον φόρο. Αν έχετε πληρώσει με κάρτα, δεν χρειάζονται χαρτιά· μου αρκεί να μου πείτε το ποσό.", "First, the certificate from the bank for the interest on your mortgage. You'll find it in e-banking, under 'Certificates'. Second, the receipts from the physiotherapist, because medical expenses reduce the tax. If you paid by card, no papers are needed; it's enough to tell me the amount."),
  L("Λογίστρια", "f", "Η προθεσμία λήγει σε δέκα μέρες, αλλά αν υποβάλουμε τη δήλωση μέσα στην εβδομάδα, έχετε έκπτωση τέσσερα τοις εκατό, αν πληρώσετε τον φόρο εφάπαξ. Στείλτε μου τα, σας παρακαλώ, με email ως την Πέμπτη.", "The deadline expires in ten days, but if we submit the return this week, you get a four per cent discount if you pay the tax in a lump sum. Please send them to me by email by Thursday."),
 ],
 "questions": [
  Q("Πού μπορεί να βρει ο κύριος Σταθόπουλος τη βεβαίωση για τους τόκους;", ["Στο ταχυδρομείο", "Στο e-banking, στην ενότητα «Βεβαιώσεις»", "Στο λογιστικό γραφείο", "Στην εφορία"], 1, "Τη βρίσκετε στο e-banking, στην ενότητα «Βεβαιώσεις»"),
  Q("Τι ισχύει αν πλήρωσε τον φυσικοθεραπευτή με κάρτα;", ["Πρέπει να ζητήσει νέες αποδείξεις", "Δεν μπορεί να μειώσει τον φόρο", "Πρέπει να πάει ο ίδιος στην τράπεζα", "Αρκεί να πει το ποσό στη λογίστρια"], 3, "μου αρκεί να μου πείτε το ποσό"),
  Q("Πότε έχει έκπτωση τέσσερα τοις εκατό;", ["Αν η δήλωση υποβληθεί μέσα στην εβδομάδα και πληρώσει τον φόρο εφάπαξ", "Αν πληρώσει σε δόσεις", "Αν στείλει τα χαρτιά ταχυδρομικώς", "Σε κάθε περίπτωση"], 0, "αν υποβάλουμε τη δήλωση μέσα στην εβδομάδα, έχετε έκπτωση τέσσερα τοις εκατό, αν πληρώσετε τον φόρο εφάπαξ"),
 ],
 "gloss": {"φορολογική": "φορολογική δήλωση — tax return", "τόκους": "τόκος — interest", "στεγαστικού": "στεγαστικό δάνειο — mortgage", "αποδείξεις": "απόδειξη — receipt", "δαπάνες": "δαπάνη — expense", "προθεσμία": "προθεσμία — deadline", "υποβάλουμε": "υποβάλλω — to submit", "εφάπαξ": "εφάπαξ — in a lump sum"}
})

ITEMS.append({
 "id": "l104-dia-protochronia", "title": "Πού θα κάνουμε Πρωτοχρονιά;", "title_en": "Where shall we spend New Year's Day?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι συζητά πού θα περάσει την Πρωτοχρονιά.",
 "script": [
  L("Νίκος", "m", "Η μητέρα μου ρώτησε πάλι αν θα πάμε για Πρωτοχρονιά στη Λάρισα. Τι να της πω;", "My mother asked again whether we'll go to Larissa for New Year's Day. What shall I tell her?"),
  L("Έλενα", "f", "Πέρσι πήγαμε στους δικούς σου, Νίκο. Οι γονείς μου μάς περιμένουν φέτος. Ο πατέρας μου έχει ήδη παραγγείλει γουρουνόπουλο.", "Last year we went to your parents, Nikos. My parents are expecting us this year. My father has already ordered a suckling pig."),
  L("Νίκος", "m", "Το ξέρω, έχεις δίκιο. Μόνο που η γιαγιά μου είναι ενενήντα δύο και δεν ξέρω πόσες Πρωτοχρονιές ακόμα θα κόψουμε μαζί τη βασιλόπιτα.", "I know, you're right. It's just that my grandmother is ninety-two and I don't know how many more New Year's Days we'll cut the vasilopita together."),
  L("Έλενα", "f", "Τότε γιατί δεν τους καλούμε όλους εδώ; Το σαλόνι μας χωράει δώδεκα άτομα αν βάλουμε και το πτυσσόμενο τραπέζι.", "Then why don't we invite them all here? Our living room fits twelve people if we add the folding table."),
  L("Νίκος", "m", "Όλους; Και τους δικούς σου και τους δικούς μου; Η γιαγιά δεν ταξιδεύει πια με το λεωφορείο.", "All of them? Both your family and mine? Grandma doesn't travel by coach any more."),
  L("Έλενα", "f", "Θα τη φέρει ο ξάδερφός σου με το αυτοκίνητο, αφού έρχεται κι αυτός στην Αθήνα τα Χριστούγεννα. Κι εγώ θα φτιάξω τη βασιλόπιτα με τη συνταγή της, αν μου τη δώσει.", "Your cousin will bring her by car, since he's coming to Athens for Christmas too. And I'll make the vasilopita with her recipe, if she gives it to me."),
  L("Νίκος", "m", "Αυτό θα της αρέσει πολύ. Πάρε τη μαμά σου να της το πεις, κι εγώ θα μιλήσω με τη δική μου απόψε.", "She'll love that. Call your mum and tell her, and I'll talk to mine tonight."),
 ],
 "questions": [
  Q("Πού πέρασαν την περσινή Πρωτοχρονιά;", ["Στο σπίτι τους", "Στους γονείς του Νίκου", "Στους γονείς της Έλενας", "Σε ξενοδοχείο"], 1, "Πέρσι πήγαμε στους δικούς σου"),
  Q("Τι προτείνει η Έλενα;", ["Να πάνε φέτος στη Λάρισα", "Να μείνουν μόνοι τους", "Να καλέσουν όλους στο σπίτι τους", "Να πάνε σε εστιατόριο"], 2, "γιατί δεν τους καλούμε όλους εδώ;"),
  Q("Πώς θα έρθει η γιαγιά στην Αθήνα;", ["Με το λεωφορείο", "Με το τρένο", "Θα την πάρει ο Νίκος", "Θα τη φέρει ο ξάδερφος του Νίκου με το αυτοκίνητο"], 3, "Θα τη φέρει ο ξάδερφός σου με το αυτοκίνητο"),
 ],
 "gloss": {"γουρουνόπουλο": "γουρουνόπουλο — suckling pig", "βασιλόπιτα": "βασιλόπιτα — New Year's cake", "πτυσσόμενο": "πτυσσόμενος — folding", "χωράει": "χωράω — to fit, hold"}
})

ITEMS.append({
 "id": "l104-int-metaglottisi", "title": "Μια ηθοποιός της μεταγλώττισης", "title_en": "A dubbing actress", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε μια ραδιοφωνική εκπομπή για τα επαγγέλματα.",
 "script": [
  L("Δημοσιογράφος", "m", "Η καλεσμένη μας σήμερα δεν την έχετε δει ποτέ, αλλά σίγουρα την έχετε ακούσει. Πόσους χαρακτήρες έχετε μεταγλωττίσει;", "You have never seen our guest today, but you have certainly heard her. How many characters have you dubbed?"),
  L("Ηθοποιός", "f", "Έχω χάσει το μέτρημα. Πάνω από διακόσιους, νομίζω: πριγκίπισσες, μάγισσες, ένα σκαντζόχοιρο, μια φορά κι ένα ψυγείο που μιλούσε. Στην Ελλάδα μεταγλωττίζονται κυρίως ταινίες κινουμένων σχεδίων και παιδικές σειρές· οι ταινίες για ενήλικες συνήθως προβάλλονται με υπότιτλους.", "I've lost count. More than two hundred, I think: princesses, witches, a hedgehog, and once a talking fridge. In Greece it is mainly animated films and children's series that are dubbed; films for adults are usually shown with subtitles."),
  L("Δημοσιογράφος", "m", "Πώς δουλεύετε στο στούντιο;", "How do you work in the studio?"),
  L("Ηθοποιός", "f", "Βλέπουμε τη σκηνή στην οθόνη και ακούμε το πρωτότυπο στα ακουστικά. Ο μεγαλύτερος κόπος είναι ο συγχρονισμός: τα λόγια πρέπει να ταιριάζουν με το στόμα του χαρακτήρα. Γι' αυτό ο μεταφραστής συχνά αλλάζει τις φράσεις ώστε να έχουν το ίδιο μήκος. Συνήθως ηχογραφούμε μόνοι μας, όχι όλοι μαζί, οπότε συχνά απαντώ σε έναν συνάδελφο που δεν έχω γνωρίσει ποτέ.", "We watch the scene on the screen and listen to the original in the headphones. The hardest part is synchronisation: the words have to match the character's mouth. That's why the translator often changes the phrases so that they have the same length. We usually record on our own, not all together, so I often answer a colleague I have never met."),
  L("Δημοσιογράφος", "m", "Τι είναι το πιο ωραίο στη δουλειά σας;", "What's the best thing about your job?"),
  L("Ηθοποιός", "f", "Όταν ένα παιδί στο σούπερ μάρκετ γυρίζει απότομα, επειδή αναγνώρισε τη φωνή μου, και δεν καταλαβαίνει γιατί η μαμά του μιλάει με μια άγνωστη κυρία.", "When a child in the supermarket turns round suddenly, because they recognised my voice, and can't understand why their mum is talking to a strange lady."),
 ],
 "questions": [
  Q("Τι μεταγλωττίζεται κυρίως στην Ελλάδα, σύμφωνα με την ηθοποιό;", ["Ταινίες κινουμένων σχεδίων και παιδικές σειρές", "Όλες οι ξένες ταινίες", "Μόνο τα ντοκιμαντέρ", "Οι ειδήσεις"], 0, "μεταγλωττίζονται κυρίως ταινίες κινουμένων σχεδίων και παιδικές σειρές"),
  Q("Ποιος είναι ο μεγαλύτερος κόπος στη δουλειά της;", ["Η απομνημόνευση του κειμένου", "Οι πολλές ώρες στο στούντιο", "Ο συγχρονισμός των λόγων με το στόμα του χαρακτήρα", "Η μετάφραση"], 2, "Ο μεγαλύτερος κόπος είναι ο συγχρονισμός"),
  Q("Πώς ηχογραφούν συνήθως οι ηθοποιοί;", ["Όλοι μαζί στην ίδια αίθουσα", "Μόνοι τους", "Από το σπίτι τους", "Μπροστά σε κοινό"], 1, "Συνήθως ηχογραφούμε μόνοι μας"),
 ],
 "gloss": {"μεταγλωττίσει": "μεταγλωττίζω — to dub", "κινουμένων": "κινούμενα σχέδια — cartoons, animation", "υπότιτλους": "υπότιτλος — subtitle", "ακουστικά": "ακουστικά — headphones", "συγχρονισμός": "συγχρονισμός — synchronisation", "ηχογραφούμε": "ηχογραφώ — to record"}
})

ITEMS.append({
 "id": "l104-rep-energeiaki-koinotita", "title": "Ένα χωριό που παράγει το δικό του ρεύμα", "title_en": "A village that produces its own electricity", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια περιφερειακή εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "f", "Στις στέγες του χωριού, ανάμεσα στα κεραμίδια και στις καμινάδες, γυαλίζουν φωτοβολταϊκά πάνελ. Πριν από τρία χρόνια, εξήντα οικογένειες και ο τοπικός σύλλογος ίδρυσαν μια ενεργειακή κοινότητα: έναν συνεταιρισμό που εγκατέστησε ένα μικρό φωτοβολταϊκό πάρκο σε ένα χωράφι έξω από το χωριό.", "On the roofs of the village, among the tiles and the chimneys, photovoltaic panels shine. Three years ago, sixty families and the local association founded an energy community: a cooperative that installed a small solar park in a field outside the village."),
  L("Πρόεδρος", "m", "Ο καθένας έβαλε όσα μπορούσε, από διακόσια μέχρι δύο χιλιάδες ευρώ, και πήραμε κι ένα μικρό δάνειο. Η ενέργεια που παράγουμε συμψηφίζεται με την κατανάλωση των μελών, έτσι οι λογαριασμοί του ρεύματος έχουν πέσει αισθητά.", "Everyone put in what they could, from two hundred to two thousand euros, and we also took out a small loan. The energy we produce is offset against the members' consumption, so the electricity bills have fallen noticeably."),
  L("Ρεπόρτερ", "f", "Η κοινότητα δεν σκέφτεται μόνο τα μέλη της. Ένα μέρος της ενέργειας καλύπτει δωρεάν τις ανάγκες του σχολείου και του αγροτικού ιατρείου, ενώ δύο ηλικιωμένες χήρες που ζουν με μικρή σύνταξη δεν πληρώνουν συνδρομή. Το επόμενο σχέδιο είναι ένας φορτιστής για ηλεκτρικά αυτοκίνητα στην πλατεία.", "The community doesn't think only of its members. Part of the energy covers the needs of the school and the rural clinic free of charge, while two elderly widows who live on a small pension pay no subscription. The next plan is a charger for electric cars in the square."),
 ],
 "questions": [
  Q("Τι ίδρυσαν οι κάτοικοι πριν από τρία χρόνια;", ["Ένα αιολικό πάρκο", "Μια ενεργειακή κοινότητα", "Μια εταιρεία πετρελαίου", "Ένα σχολείο"], 1, "ίδρυσαν μια ενεργειακή κοινότητα"),
  Q("Τι έγινε με τους λογαριασμούς του ρεύματος;", ["Έχουν πέσει αισθητά", "Έχουν διπλασιαστεί", "Έμειναν ίδιοι", "Καταργήθηκαν"], 0, "οι λογαριασμοί του ρεύματος έχουν πέσει αισθητά"),
  Q("Ποιο είναι το επόμενο σχέδιο της κοινότητας;", ["Ένα δεύτερο φωτοβολταϊκό πάρκο", "Ένα νέο ιατρείο", "Ανακαίνιση της πλατείας", "Ένας φορτιστής για ηλεκτρικά αυτοκίνητα στην πλατεία"], 3, "Το επόμενο σχέδιο είναι ένας φορτιστής για ηλεκτρικά αυτοκίνητα στην πλατεία"),
 ],
 "gloss": {"φωτοβολταϊκά": "φωτοβολταϊκός — photovoltaic, solar", "ενεργειακή": "ενεργειακή κοινότητα — energy community", "συνεταιρισμό": "συνεταιρισμός — cooperative", "συμψηφίζεται": "συμψηφίζω — to offset", "αισθητά": "αισθητά — noticeably", "σύνταξη": "σύνταξη — pension", "φορτιστής": "φορτιστής — charger"}
})

ITEMS.append({
 "id": "l104-rep-mpotsia", "title": "Μπότσια: ένα άθλημα για όλους", "title_en": "Boccia: a sport for everyone", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια αθλητική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "m", "Στο κλειστό γυμναστήριο της γειτονιάς επικρατεί απόλυτη ησυχία. Μια αθλήτρια σε αναπηρικό αμαξίδιο σκύβει, στοχεύει και ρίχνει μια κόκκινη δερμάτινη μπάλα, που σταματά λίγα εκατοστά από τη μικρή άσπρη. Το άθλημα λέγεται μπότσια και είναι παραολυμπιακό.", "In the neighbourhood's indoor gym there is total silence. An athlete in a wheelchair leans forward, aims and throws a red leather ball, which stops a few centimetres from the small white one. The sport is called boccia and it is Paralympic."),
  L("Προπονήτρια", "f", "Ο στόχος είναι να φέρεις τις μπάλες σου όσο πιο κοντά γίνεται στη λευκή, τον «στόχο». Το παίζουν κυρίως άνθρωποι με σοβαρές κινητικές αναπηρίες. Όσοι δεν μπορούν να ρίξουν με το χέρι χρησιμοποιούν μια ράμπα, και ένας βοηθός τη στρέφει όπως του λέει ο αθλητής, χωρίς να κοιτάζει το γήπεδο.", "The aim is to bring your balls as close as possible to the white one, the 'jack'. It's played mainly by people with severe physical disabilities. Those who can't throw by hand use a ramp, and an assistant turns it as the athlete tells them, without looking at the court."),
  L("Ρεπόρτερ", "m", "Ο σύλλογος ξεκίνησε με τρία μέλη και σήμερα έχει δεκαοχτώ. Τις Κυριακές οι αθλητές παίζουν και με φίλους και συγγενείς χωρίς αναπηρία, που συνήθως χάνουν. Η προπονήτρια ζητά από τον δήμο ένα μικρό λεωφορείο με ράμπα, γιατί η μετακίνηση προς το γυμναστήριο είναι για πολλούς το πιο δύσκολο κομμάτι της προπόνησης.", "The club started with three members and today it has eighteen. On Sundays the athletes also play with friends and relatives without disabilities, who usually lose. The coach is asking the municipality for a small bus with a ramp, because getting to the gym is, for many, the hardest part of training."),
 ],
 "questions": [
  Q("Ποιος είναι ο στόχος στο μπότσια;", ["Να ρίξεις την μπάλα όσο πιο μακριά γίνεται", "Να φέρεις τις μπάλες σου όσο πιο κοντά γίνεται στη λευκή", "Να χτυπήσεις τις μπάλες του αντιπάλου έξω από το γήπεδο", "Να βάλεις την μπάλα σε μια τρύπα"], 1, "να φέρεις τις μπάλες σου όσο πιο κοντά γίνεται στη λευκή"),
  Q("Τι κάνει ο βοηθός όταν ο αθλητής χρησιμοποιεί ράμπα;", ["Ρίχνει ο ίδιος την μπάλα", "Μετράει τους πόντους", "Δείχνει στον αθλητή πού να στοχεύσει", "Στρέφει τη ράμπα όπως του λέει ο αθλητής, χωρίς να κοιτάζει το γήπεδο"], 3, "ένας βοηθός τη στρέφει όπως του λέει ο αθλητής, χωρίς να κοιτάζει το γήπεδο"),
  Q("Τι ζητά η προπονήτρια από τον δήμο;", ["Ένα μικρό λεωφορείο με ράμπα", "Ένα καινούργιο γυμναστήριο", "Χρήματα για μπάλες", "Περισσότερους προπονητές"], 0, "Η προπονήτρια ζητά από τον δήμο ένα μικρό λεωφορείο με ράμπα"),
 ],
 "gloss": {"αμαξίδιο": "αναπηρικό αμαξίδιο — wheelchair", "στοχεύει": "στοχεύω — to aim", "παραολυμπιακό": "παραολυμπιακός — Paralympic", "κινητικές": "κινητική αναπηρία — physical disability", "ράμπα": "ράμπα — ramp", "στρέφει": "στρέφω — to turn", "μετακίνηση": "μετακίνηση — getting around, travel"}
})

ITEMS.append({
 "id": "l104-mono-zacharoplasteio", "title": "Η πρώτη μου δουλειά σε ένα ζαχαροπλαστείο", "title_en": "My first job in a patisserie", "type": "monologue", "level": "B2",
 "context_el": "Μια νέα γυναίκα μιλά σε ένα podcast για την πρώτη της δουλειά.",
 "script": [
  L("Δανάη", "f", "Ήμουν δεκαεπτά όταν έπιασα δουλειά για το καλοκαίρι σε ένα ζαχαροπλαστείο της γειτονιάς. Φανταζόμουν ότι θα έφτιαχνα τούρτες. Την πρώτη εβδομάδα, όμως, το μόνο που έκανα ήταν να πλένω ταψιά και να διπλώνω κουτιά.", "I was seventeen when I got a summer job at a patisserie in the neighbourhood. I imagined I'd be making cakes. The first week, though, all I did was wash baking trays and fold boxes."),
  L("Δανάη", "f", "Ο κύριος Στέλιος, ο ιδιοκτήτης, μιλούσε ελάχιστα. Τη δεύτερη εβδομάδα με έβαλε στο ταμείο. Εκεί έμαθα το πιο σημαντικό μάθημα: ότι οι άνθρωποι δεν αγοράζουν γλυκά, αγοράζουν γιορτές. Ο κύριος που έπαιρνε κάθε Κυριακή έξι κορμούς σοκολάτας για τα εγγόνια του, η κοπέλα που ήθελε μια τούρτα με τη φράση «Συγγνώμη»…", "Mr Stelios, the owner, spoke very little. In the second week he put me on the till. There I learnt the most important lesson: people don't buy sweets, they buy celebrations. The gentleman who bought six chocolate logs every Sunday for his grandchildren, the girl who wanted a cake with the word 'Sorry'…"),
  L("Δανάη", "f", "Τον Αύγουστο, την τελευταία μου μέρα, ο κύριος Στέλιος με φώναξε στο εργαστήριο και μου έδειξε πώς φτιάχνει τη σαντιγί του. «Μην το πεις σε κανέναν», μου είπε. Δεν έγινα ζαχαροπλάστρια, σπουδάζω νοσηλευτική, αλλά τη συνταγή την κρατάω ακόμα σε ένα χαρτάκι στο πορτοφόλι μου.", "In August, on my last day, Mr Stelios called me into the workshop and showed me how he makes his whipped cream. 'Don't tell anyone,' he said. I didn't become a pastry chef, I'm studying nursing, but I still keep the recipe on a scrap of paper in my wallet."),
 ],
 "questions": [
  Q("Τι έκανε η Δανάη την πρώτη εβδομάδα;", ["Έφτιαχνε τούρτες", "Έπλενε ταψιά και δίπλωνε κουτιά", "Δούλευε στο ταμείο", "Μοίραζε γλυκά στα σπίτια"], 1, "το μόνο που έκανα ήταν να πλένω ταψιά και να διπλώνω κουτιά"),
  Q("Ποιο ήταν το πιο σημαντικό μάθημα που έμαθε στο ταμείο;", ["Ότι οι άνθρωποι αγοράζουν γιορτές, όχι γλυκά", "Ότι πρέπει να μετράς σωστά τα ρέστα", "Ότι οι πελάτες είναι πάντα βιαστικοί", "Ότι η σοκολάτα πουλάει περισσότερο"], 0, "οι άνθρωποι δεν αγοράζουν γλυκά, αγοράζουν γιορτές"),
  Q("Τι κάνει σήμερα η Δανάη;", ["Είναι ζαχαροπλάστρια", "Δουλεύει ακόμα στο ζαχαροπλαστείο", "Σπουδάζει νοσηλευτική", "Έχει δικό της μαγαζί"], 2, "σπουδάζω νοσηλευτική"),
 ],
 "gloss": {"ζαχαροπλαστείο": "ζαχαροπλαστείο — patisserie", "ταψιά": "ταψί — baking tray", "ταμείο": "ταμείο — till, cash desk", "κορμούς": "κορμός σοκολάτας — chocolate log", "σαντιγί": "σαντιγί — whipped cream", "νοσηλευτική": "νοσηλευτική — nursing"}
})

ITEMS.append({
 "id": "l104-mono-monopati-kritis", "title": "Επτά μέρες με τα πόδια στα βουνά της Κρήτης", "title_en": "Seven days on foot in the mountains of Crete", "type": "monologue", "level": "B2",
 "context_el": "Ένας άντρας μιλά σε μια εκπομπή για ταξίδια.",
 "script": [
  L("Μάρκος", "m", "Πέρσι τον Μάιο περπάτησα επτά μέρες σε ένα κομμάτι του ευρωπαϊκού μονοπατιού Ε4 στην Κρήτη, από χωριό σε χωριό, με ένα σακίδιο οχτώ κιλών. Δεν ήμουν ποτέ αθλητικός τύπος· ήθελα απλώς να δω αν μπορώ.", "Last May I walked for seven days on a section of the European E4 path in Crete, from village to village, with an eight-kilo rucksack. I was never the sporty type; I just wanted to see if I could."),
  L("Μάρκος", "m", "Η τρίτη μέρα ήταν η χειρότερη. Είχα φουσκάλες και στα δύο πόδια, έβρεχε, και χάθηκα για δύο ώρες επειδή δεν πρόσεξα ένα σημάδι στον βράχο. Όταν έφτασα επιτέλους στο χωριό, μια γυναίκα που με είδε μούσκεμα με έβαλε στο σπίτι της, μου έδωσε στεγνές κάλτσες και δεν με άφησε να φύγω πριν φάω.", "The third day was the worst. I had blisters on both feet, it was raining, and I got lost for two hours because I didn't notice a mark on the rock. When I finally reached the village, a woman who saw me soaking wet took me into her house, gave me dry socks and wouldn't let me leave before I'd eaten."),
  L("Μάρκος", "m", "Από εκεί και πέρα κάτι άλλαξε. Δεν μετρούσα πια τα χιλιόμετρα· κοίταζα τα αγριολούλουδα και μιλούσα με τους βοσκούς. Αν με ρωτήσετε τι έμαθα, θα σας πω ότι χρειάζομαι πολύ λιγότερα πράγματα απ' όσα νόμιζα. Και ότι πρέπει πάντα να έχεις ένα ζευγάρι στεγνές κάλτσες.", "From then on something changed. I no longer counted the kilometres; I looked at the wild flowers and talked to the shepherds. If you ask me what I learnt, I'll tell you that I need far fewer things than I thought. And that you should always have a pair of dry socks."),
 ],
 "questions": [
  Q("Γιατί έκανε ο Μάρκος αυτή την πεζοπορία;", ["Γιατί ήταν έμπειρος ορειβάτης", "Γιατί του το πρότεινε ένας φίλος", "Γιατί ήθελε να δει αν μπορεί", "Γιατί έγραφε έναν οδηγό"], 2, "ήθελα απλώς να δω αν μπορώ"),
  Q("Γιατί χάθηκε την τρίτη μέρα;", ["Γιατί δεν πρόσεξε ένα σημάδι στον βράχο", "Γιατί έπεσε ομίχλη", "Γιατί χάλασε το κινητό του", "Γιατί ακολούθησε έναν βοσκό"], 0, "δεν πρόσεξα ένα σημάδι στον βράχο"),
  Q("Τι έμαθε, σύμφωνα με τον ίδιο;", ["Ότι πρέπει να ταξιδεύει πάντα με παρέα", "Ότι η Κρήτη είναι πολύ ακριβή", "Ότι πρέπει να προπονηθεί περισσότερο", "Ότι χρειάζεται πολύ λιγότερα πράγματα απ' όσα νόμιζε"], 3, "χρειάζομαι πολύ λιγότερα πράγματα απ' όσα νόμιζα"),
 ],
 "gloss": {"μονοπατιού": "μονοπάτι — path, trail", "σακίδιο": "σακίδιο — rucksack", "φουσκάλες": "φουσκάλα — blister", "μούσκεμα": "μούσκεμα — soaking wet", "αγριολούλουδα": "αγριολούλουδο — wild flower", "βοσκούς": "βοσκός — shepherd"}
})

ITEMS.append({
 "id": "l104-c1-zeigarnik", "title": "Γιατί δεν ξεχνάμε όσα αφήσαμε στη μέση;", "title_en": "Why don't we forget what we left half-done?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ψυχολόγο σε μια εκπομπή εκλαΐκευσης της επιστήμης.",
 "script": [
  L("Ψυχολόγος", "f", "Σύμφωνα με μια ιστορία που επαναλαμβάνεται συχνά, όλα ξεκίνησαν σε ένα καφέ του Βερολίνου τη δεκαετία του 1920. Μια νεαρή ψυχολόγος, η Μπλούμα Ζεϊγκάρνικ, παρατήρησε ότι ο σερβιτόρος θυμόταν με ακρίβεια τις παραγγελίες που δεν είχαν ακόμα πληρωθεί, αλλά τις ξεχνούσε σχεδόν αμέσως μόλις ο λογαριασμός εξοφλούνταν. Είτε η ιστορία είναι ακριβής είτε όχι, η Ζεϊγκάρνικ αποφάσισε να ελέγξει την παρατήρηση στο εργαστήριο.", "According to a story that is often repeated, it all began in a Berlin café in the 1920s. A young psychologist, Bluma Zeigarnik, noticed that the waiter remembered precisely the orders that had not yet been paid, but forgot them almost immediately once the bill was settled. Whether or not the story is accurate, Zeigarnik decided to test the observation in the laboratory."),
  L("Ψυχολόγος", "f", "Έδωσε στους συμμετέχοντες απλές εργασίες, όπως παζλ και αριθμητικές ασκήσεις, και διέκοπτε ορισμένες πριν ολοκληρωθούν. Αργότερα, όταν τους ζητούσε να θυμηθούν τις εργασίες, εκείνες που είχαν διακοπεί ανακαλούνταν συχνότερα από όσες είχαν τελειώσει. Η εξήγηση που προτάθηκε ήταν ότι ένας ανολοκλήρωτος στόχος διατηρεί μια εσωτερική ένταση, η οποία κρατά την πληροφορία ενεργή, ώσπου ο στόχος να ικανοποιηθεί.", "She gave participants simple tasks, such as puzzles and arithmetic exercises, and interrupted some of them before they were completed. Later, when she asked them to recall the tasks, the interrupted ones were remembered more often than those that had been finished. The explanation proposed was that an unfinished goal maintains an inner tension, which keeps the information active until the goal is satisfied."),
  L("Ψυχολόγος", "f", "Οφείλω να πω ότι οι μεταγενέστερες προσπάθειες επανάληψης του πειράματος έδωσαν ανάμεικτα αποτελέσματα. Η ιδέα, πάντως, έχει γίνει ιδιαίτερα δημοφιλής: οι σεναριογράφοι τελειώνουν τα επεισόδια με μια ανοιχτή απορία, ακριβώς για να μην μπορούμε να σταματήσουμε. Υπάρχει και μια πιο πρακτική εφαρμογή. Όταν κάποιος δεν μπορεί να κοιμηθεί επειδή σκέφτεται εκκρεμότητες, μερικές έρευνες δείχνουν ότι βοηθά να γράψει ένα συγκεκριμένο σχέδιο για το πότε θα τις τακτοποιήσει. Είναι σαν να λέμε στον εγκέφαλο: «Το έχω σημειώσει, μπορείς να ησυχάσεις».", "I must say that later attempts to replicate the experiment gave mixed results. The idea, in any case, has become very popular: screenwriters end episodes with an open question precisely so that we can't stop. There is also a more practical application. When someone can't sleep because they are thinking about unfinished business, some studies show that it helps to write down a specific plan for when they will deal with it. It is as if we were telling the brain: 'I've noted it down, you can rest.'"),
 ],
 "questions": [
  Q("Τι παρατήρησε, σύμφωνα με την ιστορία, η Ζεϊγκάρνικ στο καφέ;", ["Ότι ο σερβιτόρος θυμόταν τις απλήρωτες παραγγελίες και ξεχνούσε τις πληρωμένες", "Ότι οι πελάτες ξεχνούσαν να πληρώσουν", "Ότι ο σερβιτόρος σημείωνε όλες τις παραγγελίες", "Ότι οι πελάτες θυμούνταν τι είχαν παραγγείλει"], 0, "θυμόταν με ακρίβεια τις παραγγελίες που δεν είχαν ακόμα πληρωθεί, αλλά τις ξεχνούσε σχεδόν αμέσως μόλις ο λογαριασμός εξοφλούνταν"),
  Q("Ποιες εργασίες θυμούνταν συχνότερα οι συμμετέχοντες;", ["Τις πιο δύσκολες", "Εκείνες που είχαν διακοπεί", "Εκείνες που είχαν τελειώσει", "Τις πρώτες που έκαναν"], 1, "εκείνες που είχαν διακοπεί ανακαλούνταν συχνότερα από όσες είχαν τελειώσει"),
  Q("Τι λέει η ψυχολόγος για τις μεταγενέστερες επαναλήψεις του πειράματος;", ["Ότι επιβεβαίωσαν πλήρως το αποτέλεσμα", "Ότι δεν έγιναν ποτέ", "Ότι έδωσαν ανάμεικτα αποτελέσματα", "Ότι απέδειξαν ότι η ιστορία ήταν ψέμα"], 2, "έδωσαν ανάμεικτα αποτελέσματα"),
  Q("Τι μπορεί να βοηθήσει κάποιον που δεν κοιμάται εξαιτίας των εκκρεμοτήτων, σύμφωνα με μερικές έρευνες;", ["Να βλέπει ένα επεισόδιο σειράς", "Να σηκωθεί και να τις τελειώσει αμέσως", "Να προσπαθήσει να μην τις σκέφτεται", "Να γράψει ένα συγκεκριμένο σχέδιο για το πότε θα τις τακτοποιήσει"], 3, "βοηθά να γράψει ένα συγκεκριμένο σχέδιο για το πότε θα τις τακτοποιήσει"),
 ],
 "gloss": {"εξοφλούνταν": "εξοφλώ — to settle, pay off", "διέκοπτε": "διακόπτω — to interrupt", "ανακαλούνταν": "ανακαλώ — to recall", "ανολοκλήρωτος": "ανολοκλήρωτος — unfinished", "μεταγενέστερες": "μεταγενέστερος — later, subsequent", "ανάμεικτα": "ανάμεικτος — mixed", "εκκρεμότητες": "εκκρεμότητα — pending matter", "σεναριογράφοι": "σεναριογράφος — screenwriter"}
})

ITEMS.append({
 "id": "l104-c1-esoteriki-foni", "title": "Ακούμε όλοι μια φωνή μέσα μας;", "title_en": "Do we all hear a voice inside us?", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν γνωστικό επιστήμονα σε μια ραδιοφωνική εκπομπή.",
 "script": [
  L("Δημοσιογράφος", "f", "Πολλοί από εμάς σκεφτόμαστε με λέξεις, σαν να μιλάμε σιωπηλά στον εαυτό μας. Ισχύει αυτό για όλους;", "Many of us think in words, as if we were speaking silently to ourselves. Is that true for everyone?"),
  L("Επιστήμονας", "m", "Όχι, και αυτό είναι ίσως το πιο απρόσμενο εύρημα των τελευταίων χρόνων. Όταν οι ερευνητές ζητούν από ανθρώπους να καταγράφουν τι περνάει από το μυαλό τους σε τυχαίες στιγμές της ημέρας, διαπιστώνουν τεράστιες διαφορές. Κάποιοι αναφέρουν έναν σχεδόν αδιάκοπο εσωτερικό μονόλογο, ενώ άλλοι λένε ότι σπάνια ή και ποτέ δεν «ακούνε» λέξεις στο κεφάλι τους· σκέφτονται με εικόνες, με αισθήσεις ή με κάτι που δυσκολεύονται να περιγράψουν.", "No, and that is perhaps the most unexpected finding of recent years. When researchers ask people to record what is going through their minds at random moments of the day, they find huge differences. Some report an almost constant inner monologue, while others say they rarely or never 'hear' words in their heads; they think in images, in sensations or in something they find hard to describe."),
  L("Δημοσιογράφος", "f", "Και αυτό επηρεάζει την καθημερινότητά τους;", "And does that affect their daily lives?"),
  L("Επιστήμονας", "m", "Λιγότερο απ' όσο θα περίμενε κανείς. Οι άνθρωποι με ελάχιστο εσωτερικό λόγο ζουν, δουλεύουν και συζητούν κανονικά. Σε ορισμένες πρόσφατες μελέτες τα πήγαν κάπως χειρότερα σε δοκιμασίες όπου έπρεπε να συγκρατήσουν μια σειρά λέξεων ή να κρίνουν αν δύο λέξεις ομοιοκαταληκτούν, πιθανώς επειδή δεν «επαναλάμβαναν» τις λέξεις μέσα τους. Όμως πρόκειται για μικρά δείγματα και τα συμπεράσματα είναι προσωρινά.", "Less than one would expect. People with very little inner speech live, work and converse normally. In some recent studies they did somewhat worse on tests where they had to hold a series of words in memory or judge whether two words rhyme, probably because they weren't 'repeating' the words to themselves. But these are small samples and the conclusions are provisional."),
  L("Δημοσιογράφος", "f", "Γιατί αργήσαμε τόσο να το ανακαλύψουμε;", "Why did it take us so long to discover this?"),
  L("Επιστήμονας", "m", "Επειδή ο καθένας θεωρεί αυτονόητο ότι οι άλλοι σκέφτονται όπως εκείνος. Δεν έχουμε πρόσβαση στο μυαλό του διπλανού μας, και σπάνια ρωτάμε. Πολλοί συμμετέχοντες μάς λένε ότι έμειναν άφωνοι όταν συνειδητοποίησαν ότι η δική τους εμπειρία δεν είναι η μόνη.", "Because everyone takes it for granted that others think as they do. We don't have access to the mind of the person next to us, and we rarely ask. Many participants tell us they were speechless when they realised that their own experience is not the only one."),
 ],
 "questions": [
  Q("Τι διαπιστώνουν οι ερευνητές όταν οι άνθρωποι καταγράφουν τις σκέψεις τους;", ["Ότι όλοι σκέφτονται με λέξεις", "Ότι υπάρχουν τεράστιες διαφορές από άνθρωπο σε άνθρωπο", "Ότι κανείς δεν σκέφτεται με εικόνες", "Ότι οι σκέψεις είναι ίδιες το πρωί και το βράδυ"], 1, "διαπιστώνουν τεράστιες διαφορές"),
  Q("Πώς επηρεάζει την καθημερινότητα ο ελάχιστος εσωτερικός λόγος;", ["Λιγότερο απ' όσο θα περίμενε κανείς", "Τους εμποδίζει να συζητούν", "Τους κάνει πιο δημιουργικούς", "Τους δυσκολεύει να βρουν δουλειά"], 0, "Λιγότερο απ' όσο θα περίμενε κανείς"),
  Q("Σε τι τα πήγαν κάπως χειρότερα σε ορισμένες μελέτες;", ["Στην ανάγνωση", "Στα μαθηματικά", "Στη συγκράτηση μιας σειράς λέξεων και στην κρίση της ομοιοκαταληξίας", "Στην αναγνώριση προσώπων"], 2, "έπρεπε να συγκρατήσουν μια σειρά λέξεων ή να κρίνουν αν δύο λέξεις ομοιοκαταληκτούν"),
  Q("Γιατί αργήσαμε να το ανακαλύψουμε, σύμφωνα με τον επιστήμονα;", ["Γιατί δεν υπήρχαν οι κατάλληλες μηχανές", "Γιατί οι άνθρωποι ντρέπονταν να μιλήσουν", "Γιατί οι ψυχολόγοι δεν ενδιαφέρονταν", "Γιατί ο καθένας θεωρεί αυτονόητο ότι οι άλλοι σκέφτονται όπως εκείνος"], 3, "ο καθένας θεωρεί αυτονόητο ότι οι άλλοι σκέφτονται όπως εκείνος"),
 ],
 "gloss": {"απρόσμενο": "απρόσμενος — unexpected", "εύρημα": "εύρημα — finding", "αδιάκοπο": "αδιάκοπος — constant, incessant", "συγκρατήσουν": "συγκρατώ — to retain, hold", "ομοιοκαταληκτούν": "ομοιοκαταληκτώ — to rhyme", "δείγματα": "δείγμα — sample", "αυτονόητο": "αυτονόητος — self-evident", "άφωνοι": "άφωνος — speechless"}
})

rnd = random.Random(104)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-104.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
