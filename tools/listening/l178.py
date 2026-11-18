# Source for library/listening/listening-178.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l178.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l178-ann-imantas-aposkevon", "title": "Ανακοίνωση στην αίθουσα παραλαβής αποσκευών", "title_en": "An announcement in the baggage reclaim hall", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση στην αίθουσα παραλαβής αποσκευών ενός αεροδρομίου, αργά το βράδυ.",
 "script": [
  L("Εκφωνητής", "m", "Κυρίες και κύριοι, οι επιβάτες της πτήσης από τη Φρανκφούρτη παρακαλούνται να κατευθυνθούν στον ιμάντα αριθμός πέντε και όχι στον τρία, όπως αναγραφόταν αρχικά στις οθόνες. Λόγω βλάβης σε ένα όχημα μεταφοράς, οι αποσκευές θα αρχίσουν να έρχονται με καθυστέρηση περίπου είκοσι λεπτών.", "Ladies and gentlemen, passengers of the flight from Frankfurt are requested to go to belt number five and not number three, as originally shown on the screens. Because of a fault in a transport vehicle, the baggage will start arriving with a delay of about twenty minutes."),
  L("Εκφωνητής", "m", "Τα ογκώδη αντικείμενα, όπως καρότσια μωρών, ποδήλατα και εξοπλισμός σκι, δεν θα έρθουν στον ιμάντα. Θα τα παραλάβετε από το ειδικό γκισέ, στο τέλος της αίθουσας, δίπλα στο τελωνείο.", "Bulky items, such as prams, bicycles and ski equipment, will not come on the belt. You will collect them from the special counter, at the end of the hall, next to customs."),
  L("Εκφωνητής", "m", "Αν η αποσκευή σας δεν έχει φτάσει, μην βγείτε από την αίθουσα. Απευθυνθείτε στο γραφείο απολεσθέντων αποσκευών, κρατώντας την κάρτα επιβίβασης και το αυτοκόλλητο της βαλίτσας σας. Μόλις βγείτε από τις συρόμενες πόρτες, δεν θα μπορείτε να ξαναμπείτε. Σας ευχαριστούμε για την κατανόηση.", "If your baggage has not arrived, do not leave the hall. Go to the lost baggage office, keeping your boarding pass and your suitcase's tag. Once you go out through the sliding doors, you won't be able to come back in. Thank you for your understanding."),
 ],
 "questions": [
  Q("Πού πρέπει να πάνε οι επιβάτες της πτήσης από τη Φρανκφούρτη;", ["Στον ιμάντα τρία", "Στον ιμάντα πέντε", "Στο τελωνείο", "Στην έξοδο"], 1, "να κατευθυνθούν στον ιμάντα αριθμός πέντε"),
  Q("Πού θα παραλάβουν οι επιβάτες ένα ποδήλατο;", ["Στον ιμάντα πέντε", "Στο γραφείο απολεσθέντων", "Στο ειδικό γκισέ στο τέλος της αίθουσας", "Έξω από τις συρόμενες πόρτες"], 2, "Θα τα παραλάβετε από το ειδικό γκισέ, στο τέλος της αίθουσας"),
  Q("Γιατί δεν πρέπει να βγουν από την αίθουσα όσοι δεν βρήκαν τη βαλίτσα τους;", ["Γιατί δεν θα μπορούν να ξαναμπούν", "Γιατί θα χάσουν την πτήση τους", "Γιατί έξω δεν υπάρχει γραφείο πληροφοριών", "Γιατί θα πληρώσουν πρόστιμο"], 0, "δεν θα μπορείτε να ξαναμπείτε"),
 ],
 "gloss": {"αίθουσα παραλαβής αποσκευών": "αίθουσα παραλαβής αποσκευών — baggage reclaim hall", "ιμάντα": "ιμάντας — (conveyor) belt", "αναγραφόταν": "αναγράφομαι — to be shown, be written", "βλάβης": "βλάβη — fault, breakdown", "ογκώδη": "ογκώδης — bulky", "καρότσια μωρών": "καρότσι μωρού — pram", "γκισέ": "γκισέ — counter, window", "τελωνείο": "τελωνείο — customs", "απολεσθέντων αποσκευών": "απολεσθείσες αποσκευές — lost baggage (formal)", "κάρτα επιβίβασης": "κάρτα επιβίβασης — boarding pass", "συρόμενες πόρτες": "συρόμενη πόρτα — sliding door"},
})

ITEMS.append({
 "id": "l178-int-dendrochirourgos", "title": "Η δενδροχειρουργός της πόλης", "title_en": "The city's tree surgeon", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια δενδροχειρουργό που φροντίζει τα γέρικα δέντρα στα πάρκα και στους δρόμους μιας μεγάλης πόλης.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι περισσότεροι δεν έχουν ακούσει ποτέ τη λέξη «δενδροχειρουργός». Τι κάνετε ακριβώς;", "Most people have never heard the word 'tree surgeon'. What exactly do you do?"),
  L("Δενδροχειρουργός", "f", "Εξετάζω τα δέντρα σαν ασθενείς. Ανεβαίνω με σχοινιά και ζώνη ασφαλείας στα κλαδιά, ελέγχω αν υπάρχουν σαπίσματα, κουφάλες ή μύκητες, και αποφασίζω αν ένα δέντρο χρειάζεται κλάδεμα, στήριξη με ειδικά συρματόσχοινα ή, στη χειρότερη περίπτωση, κοπή. Χρησιμοποιώ και ένα όργανο που στέλνει ηχητικά κύματα μέσα στον κορμό, για να δω αν είναι κούφιος χωρίς να τον τρυπήσω.", "I examine trees like patients. I climb into the branches with ropes and a safety harness, check whether there is rot, hollows or fungi, and decide whether a tree needs pruning, support with special steel cables or, in the worst case, felling. I also use an instrument that sends sound waves into the trunk, to see whether it's hollow without drilling into it."),
  L("Δημοσιογράφος", "m", "Οι πολίτες συχνά διαμαρτύρονται όταν βλέπουν δέντρα να κόβονται.", "Citizens often protest when they see trees being cut down."),
  L("Δενδροχειρουργός", "f", "Και καλά κάνουν να ρωτούν. Όμως το μεγαλύτερο πρόβλημα δεν είναι οι κοπές, είναι το κακό κλάδεμα. Όταν κόβεις ένα πλατάνι «κούτσουρο», όπως λέμε, αφήνοντας μόνο τον κορμό και τα χοντρά κλαδιά, οι πληγές είναι τόσο μεγάλες που το δέντρο δεν μπορεί να τις κλείσει. Μπαίνει νερό, σαπίζει από μέσα, και δέκα χρόνια αργότερα γίνεται επικίνδυνο. Τότε πια πρέπει να κοπεί, και όλοι λένε ότι φταίει ο δήμος που το έκοψε.", "And they're right to ask. But the biggest problem isn't the felling, it's bad pruning. When you cut a plane tree back to a 'stump', as we say, leaving only the trunk and the thick branches, the wounds are so big that the tree can't close them. Water gets in, it rots from the inside, and ten years later it becomes dangerous. By then it has to be cut down, and everyone says it's the council's fault for cutting it."),
  L("Δημοσιογράφος", "m", "Ποιο δέντρο σας έχει συγκινήσει περισσότερο;", "Which tree has moved you most?"),
  L("Δενδροχειρουργός", "f", "Μια γέρικη μουριά σε μια αυλή σχολείου. Είχε ανοίξει στα δύο μετά από μια καταιγίδα και όλοι έλεγαν να την κόψουμε. Τη δέσαμε με συρματόσχοινα και τη στηρίξαμε. Πέρσι τα παιδιά μού έστειλαν μια ζωγραφιά: η μουριά γεμάτη φύλλα, κι από κάτω γραμμένο «Ευχαριστούμε που δεν την κόψατε».", "An old mulberry tree in a school yard. It had split in two after a storm and everyone said to cut it down. We tied it with steel cables and propped it up. Last year the children sent me a drawing: the mulberry full of leaves, and underneath written 'Thank you for not cutting it down'."),
 ],
 "questions": [
  Q("Πώς ελέγχει αν ένας κορμός είναι κούφιος;", ["Τον τρυπάει με τρυπάνι", "Με ένα όργανο που στέλνει ηχητικά κύματα μέσα στον κορμό", "Τον χτυπάει με ένα σφυρί", "Κοιτάζει τα φύλλα"], 1, "ένα όργανο που στέλνει ηχητικά κύματα μέσα στον κορμό"),
  Q("Ποιο είναι κατά τη δενδροχειρουργό το μεγαλύτερο πρόβλημα;", ["Οι συχνές κοπές", "Η έλλειψη νερού", "Το κακό κλάδεμα", "Τα αυτοκίνητα που παρκάρουν κάτω από τα δέντρα"], 2, "το μεγαλύτερο πρόβλημα δεν είναι οι κοπές, είναι το κακό κλάδεμα"),
  Q("Τι έγινε με τη μουριά στην αυλή του σχολείου;", ["Τη στήριξαν με συρματόσχοινα και σώθηκε", "Την έκοψαν μετά την καταιγίδα", "Τη μετέφεραν σε ένα πάρκο", "Φύτεψαν μια καινούργια στη θέση της"], 0, "Τη δέσαμε με συρματόσχοινα και τη στηρίξαμε"),
 ],
 "gloss": {"δενδροχειρουργό": "δενδροχειρουργός — tree surgeon", "γέρικα": "γέρικος — old (of trees, animals)", "ζώνη ασφαλείας": "ζώνη ασφαλείας — safety harness (here)", "σαπίσματα": "σάπισμα — rot", "κουφάλες": "κουφάλα — hollow (in a tree)", "μύκητες": "μύκητας — fungus", "κλάδεμα": "κλάδεμα — pruning", "συρματόσχοινα": "συρματόσχοινο — steel cable", "κορμό": "κορμός — trunk", "κούφιος": "κούφιος — hollow", "διαμαρτύρονται": "διαμαρτύρομαι — to protest", "κούτσουρο": "κούτσουρο — stump, log", "μουριά": "μουριά — mulberry tree"},
})

ITEMS.append({
 "id": "l178-vm-kommotirio-skylon", "title": "Μήνυμα από το κομμωτήριο σκύλων", "title_en": "A message from the dog grooming salon", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από το κομμωτήριο όπου έχετε κλείσει ραντεβού για τον σκύλο σας.",
 "script": [
  L("Κομμώτρια", "f", "Καλησπέρα, η Σοφία είμαι, από το κομμωτήριο σκύλων «Χνούδι». Σας παίρνω για το ραντεβού του Μπρούνο την Πέμπτη στις έντεκα. Δυστυχώς, η συνάδελφός μου που κάνει τα μεγαλόσωμα σκυλιά θα λείπει εκείνη τη μέρα, οπότε σας προτείνω να το μεταφέρουμε για το Σάββατο στις δέκα, αν σας βολεύει.", "Good evening, it's Sofia, from the dog grooming salon 'Fluff'. I'm calling about Bruno's appointment on Thursday at eleven. Unfortunately, my colleague who does the large dogs will be away that day, so I suggest we move it to Saturday at ten, if that suits you."),
  L("Κομμώτρια", "f", "Θέλω να σας ρωτήσω και κάτι ακόμα. Την προηγούμενη φορά πρόσεξα ότι ο Μπρούνο ξυνόταν πολύ πίσω από τα αυτιά και είχε λίγο κοκκινίλα. Αν τον έχει δει ο κτηνίατρος και σας έδωσε κάποιο ειδικό σαμπουάν, φέρτε το μαζί σας, για να μη χρησιμοποιήσουμε το δικό μας και τον ερεθίσουμε.", "I also want to ask you something else. Last time I noticed that Bruno was scratching a lot behind his ears and had some redness. If the vet has seen him and gave you a special shampoo, bring it with you, so we don't use ours and irritate him."),
  L("Κομμώτρια", "f", "Και μην τον ταΐσετε πολύ το πρωί του ραντεβού· με το πιστολάκι και το μπάνιο κάποια σκυλιά αγχώνονται και ανακατεύεται το στομάχι τους. Στείλτε μου ένα μήνυμα για το Σάββατο. Ευχαριστώ!", "And don't feed him a lot on the morning of the appointment; with the hairdryer and the bath some dogs get anxious and their stomach gets upset. Send me a message about Saturday. Thanks!"),
 ],
 "questions": [
  Q("Γιατί προτείνει η Σοφία να αλλάξει το ραντεβού;", ["Γιατί το κομμωτήριο θα είναι κλειστό για ανακαίνιση", "Γιατί η συνάδελφος που κάνει τα μεγάλα σκυλιά θα λείπει", "Γιατί είναι άρρωστη η ίδια", "Γιατί έχει πολλά ραντεβού την Πέμπτη"], 1, "η συνάδελφός μου που κάνει τα μεγαλόσωμα σκυλιά θα λείπει"),
  Q("Τι ζητάει να φέρει ο ιδιοκτήτης;", ["Το βιβλιάριο υγείας του σκύλου", "Μια πετσέτα", "Το ειδικό σαμπουάν από τον κτηνίατρο, αν υπάρχει", "Το λουρί και το φίμωτρο"], 2, "Αν τον έχει δει ο κτηνίατρος και σας έδωσε κάποιο ειδικό σαμπουάν, φέρτε το μαζί σας"),
  Q("Γιατί δεν πρέπει να ταΐσει πολύ τον σκύλο το πρωί;", ["Γιατί με το άγχος ανακατεύεται το στομάχι κάποιων σκύλων", "Γιατί θα του δώσουν λιχουδιές στο κομμωτήριο", "Γιατί θα κάνει δίαιτα", "Γιατί το ζήτησε ο κτηνίατρος"], 0, "κάποια σκυλιά αγχώνονται και ανακατεύεται το στομάχι τους"),
 ],
 "gloss": {"κομμωτήριο": "κομμωτήριο — hair salon (here: grooming salon)", "τηλεφωνητή": "τηλεφωνητής — answering machine", "Χνούδι": "χνούδι — fluff, fuzz", "μεγαλόσωμα": "μεγαλόσωμος — large-bodied", "σας βολεύει": "με βολεύει — it suits me", "ξυνόταν": "ξύνομαι — to scratch oneself", "κοκκινίλα": "κοκκινίλα — redness", "ερεθίσουμε": "ερεθίζω — to irritate", "ταΐσετε": "ταΐζω — to feed", "πιστολάκι": "πιστολάκι — hairdryer", "ανακατεύεται το στομάχι": "ανακατεύεται το στομάχι μου — my stomach gets upset"},
})

ITEMS.append({
 "id": "l178-rep-alieftikos-tourismos", "title": "Μια μέρα στο καΐκι με τον ψαρά", "title_en": "A day on the boat with the fisherman", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ραδιοφωνικό ρεπορτάζ για τον αλιευτικό τουρισμό σε ένα νησί των Δωδεκανήσων.",
 "script": [
  L("Ρεπόρτερ", "m", "Είναι πέντε το πρωί και στο λιμάνι ακόμα δεν έχει φέξει. Ο καπετάν Μιχάλης ετοιμάζει τα δίχτυα του, ενώ τέσσερις τουρίστες από τη Γαλλία φορούν σωσίβια και κοιτάζουν με περιέργεια. Σήμερα δεν θα κάνουν απλώς μια βόλτα με βάρκα· θα δουλέψουν δίπλα του, όπως ένας πραγματικός ναύτης.", "It's five in the morning and in the harbour it hasn't got light yet. Captain Michalis is preparing his nets, while four tourists from France put on life jackets and look on with curiosity. Today they won't just take a boat ride; they'll work alongside him, like a real deckhand."),
  L("Ψαράς", "m", "Τα τελευταία χρόνια το ψάρι λιγοστεύει και τα έξοδα ανεβαίνουν. Με τον αλιευτικό τουρισμό βγάζω ένα συμπλήρωμα και ψαρεύω λιγότερο. Αλλά το σημαντικότερο είναι άλλο: οι επισκέπτες καταλαβαίνουν πόσος κόπος κρύβεται πίσω από ένα πιάτο μαρίδα. Κάποιοι, όταν γυρίζουν στο σπίτι τους, μου γράφουν ότι δεν ξαναγοράζουν ψάρι χωρίς να ρωτήσουν από πού είναι.", "In recent years the fish have been getting scarcer and expenses are rising. With fishing tourism I earn some extra and fish less. But the most important thing is something else: the visitors understand how much effort lies behind a plate of whitebait. Some, when they get back home, write to tell me they never buy fish again without asking where it's from."),
  L("Ρεπόρτερ", "m", "Το καΐκι μπορεί να πάρει μέχρι έξι επιβάτες και πρέπει να έχει ειδική άδεια και ασφάλιση. Γύρω στις δέκα, μετά το μάζεμα των διχτυών, ο καπετάνιος ψήνει μερικά από τα ψάρια πάνω στη βάρκα, σε μια κρυφή παραλία. Για πολλούς επισκέπτες, αυτή η στιγμή είναι η πιο αξέχαστη των διακοπών τους.", "The boat can take up to six passengers and must have a special licence and insurance. Around ten, after hauling in the nets, the captain grills some of the fish on board, at a hidden beach. For many visitors, this moment is the most unforgettable of their holiday."),
 ],
 "questions": [
  Q("Τι θα κάνουν οι τουρίστες στο καΐκι;", ["Μια απλή βόλτα με βάρκα", "Θα δουλέψουν δίπλα στον ψαρά σαν ναύτες", "Θα κάνουν καταδύσεις", "Θα παρακολουθήσουν δελφίνια"], 1, "θα δουλέψουν δίπλα του, όπως ένας πραγματικός ναύτης"),
  Q("Τι θεωρεί ο ψαράς το σημαντικότερο;", ["Τα χρήματα που κερδίζει", "Ότι μαθαίνει γαλλικά", "Ότι οι επισκέπτες καταλαβαίνουν πόσος κόπος κρύβεται πίσω από ένα πιάτο ψάρι", "Ότι ψαρεύει περισσότερο"], 2, "οι επισκέπτες καταλαβαίνουν πόσος κόπος κρύβεται πίσω από ένα πιάτο μαρίδα"),
  Q("Πόσους επιβάτες μπορεί να πάρει το καΐκι;", ["Μέχρι έξι", "Μέχρι τέσσερις", "Μέχρι δέκα", "Όσους χωράει"], 0, "Το καΐκι μπορεί να πάρει μέχρι έξι επιβάτες"),
 ],
 "gloss": {"αλιευτικό τουρισμό": "αλιευτικός τουρισμός — fishing tourism", "καΐκι": "καΐκι — caique, fishing boat", "έχει φέξει": "φέγγει — it gets light", "δίχτυα": "δίχτυ — (fishing) net", "σωσίβια": "σωσίβιο — life jacket", "ναύτης": "ναύτης — sailor, deckhand", "λιγοστεύει": "λιγοστεύω — to become scarce", "συμπλήρωμα": "συμπλήρωμα — supplement, extra income", "κόπος": "κόπος — effort, toil", "μαρίδα": "μαρίδα — whitebait (picarel)", "ασφάλιση": "ασφάλιση — insurance", "μάζεμα": "μάζεμα — gathering, hauling in"},
})

ITEMS.append({
 "id": "l178-mon-akoustiko-varikoias", "title": "Το πρώτο μου ακουστικό βαρηκοΐας", "title_en": "My first hearing aid", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν συνταξιούχο δάσκαλο να μιλάει για την εμπειρία του όταν άρχισε να φοράει ακουστικό βαρηκοΐας.",
 "script": [
  L("Συνταξιούχος", "m", "Για χρόνια έλεγα ότι οι άλλοι μουρμουρίζουν. Η γυναίκα μου με παρακαλούσε να χαμηλώσω την τηλεόραση, και τα εγγόνια μου γελούσαν όταν απαντούσα σε ερωτήσεις που δεν μου είχαν κάνει. Στα τραπέζια με πολύ κόσμο απλώς χαμογελούσα και κουνούσα το κεφάλι. Δεν ήθελα να παραδεχτώ ότι δεν άκουγα.", "For years I said other people mumbled. My wife told me to turn the TV down, and my grandchildren laughed when I answered questions they hadn't asked me. At crowded tables I just smiled and nodded. I didn't want to admit I couldn't hear."),
  L("Συνταξιούχος", "m", "Όταν τελικά πήγα στον ωτορινολαρυγγολόγο, το ακουόγραμμα έδειξε ότι είχα χάσει μεγάλο μέρος της ακοής στις υψηλές συχνότητες. Μου είπε κάτι που με ξάφνιασε: ότι όσο περισσότερο καθυστερεί κανείς, τόσο πιο δύσκολα συνηθίζει ο εγκέφαλος ξανά τους ήχους.", "When I finally went to the ear, nose and throat specialist, the audiogram showed I had lost a large part of my hearing in the high frequencies. He told me something that surprised me: that the longer you put it off, the harder it is for the brain to get used to sounds again."),
  L("Συνταξιούχος", "m", "Τις πρώτες μέρες όλα μου φαίνονταν εκκωφαντικά: το ψυγείο, τα βήματά μου, το χαρτί που τσαλάκωνα. Μετά από δύο εβδομάδες ο εγκέφαλος έμαθε να τα αγνοεί. Και ένα πρωί, στο μπαλκόνι, άκουσα ξανά τα σπουργίτια. Δεν είχα καταλάβει καν ότι τα είχα χάσει. Αν έχετε κάποιον που λέει ότι όλοι μουρμουρίζουν, στείλτε τον να εξεταστεί.", "In the first days everything seemed deafening: the fridge, my footsteps, the paper I crumpled. After two weeks my brain learned to ignore them. And one morning, on the balcony, I heard the sparrows again. I hadn't even realised I'd lost them. If you have someone who says everyone mumbles, send them to get tested."),
 ],
 "questions": [
  Q("Τι έκανε ο ομιλητής στα τραπέζια με πολύ κόσμο;", ["Έφευγε νωρίς", "Χαμογελούσε και κουνούσε το κεφάλι", "Ζητούσε από όλους να μιλούν πιο δυνατά", "Καθόταν δίπλα στη γυναίκα του"], 1, "απλώς χαμογελούσα και κουνούσα το κεφάλι"),
  Q("Τι τον ξάφνιασε από όσα του είπε ο γιατρός;", ["Ότι η βαρηκοΐα του ήταν κληρονομική", "Ότι θα χρειαζόταν χειρουργείο", "Ότι όσο καθυστερεί κανείς, τόσο πιο δύσκολα συνηθίζει ο εγκέφαλος τους ήχους", "Ότι το ακουστικό θα το φορούσε μόνο το βράδυ"], 2, "όσο περισσότερο καθυστερεί κανείς, τόσο πιο δύσκολα συνηθίζει ο εγκέφαλος ξανά τους ήχους"),
  Q("Τι του συνέβη ένα πρωί στο μπαλκόνι;", ["Άκουσε ξανά τα σπουργίτια", "Έχασε το ακουστικό του", "Τον ενόχλησε ο θόρυβος του δρόμου", "Μίλησε με έναν γείτονα"], 0, "άκουσα ξανά τα σπουργίτια"),
 ],
 "gloss": {"ακουστικό βαρηκοΐας": "ακουστικό βαρηκοΐας — hearing aid", "μουρμουρίζουν": "μουρμουρίζω — to mumble", "παραδεχτώ": "παραδέχομαι — to admit", "ωτορινολαρυγγολόγο": "ωτορινολαρυγγολόγος — ear, nose and throat specialist", "ακουόγραμμα": "ακουόγραμμα — audiogram", "ακοής": "ακοή — hearing", "συχνότητες": "συχνότητα — frequency", "ξάφνιασε": "ξαφνιάζω — to surprise", "εκκωφαντικά": "εκκωφαντικός — deafening", "τσαλάκωνα": "τσαλακώνω — to crumple", "σπουργίτια": "σπουργίτι — sparrow"},
})

ITEMS.append({
 "id": "l178-dia-pyranichneftis", "title": "Ο πυρανιχνευτής που σφυρίζει τη νύχτα", "title_en": "The smoke alarm that beeps at night", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο συγκάτοικους να συζητούν στην κουζίνα, νωρίς το πρωί, μετά από μια νύχτα χωρίς ύπνο.",
 "script": [
  L("Σταύρος", "m", "Το άκουσες κι εσύ; Κάθε ένα λεπτό, ένα «μπιπ». Από τις τρεις τα ξημερώματα. Νόμιζα ότι θα τρελαθώ.", "Did you hear it too? Every minute, a 'beep'. Since three in the morning. I thought I'd go mad."),
  L("Ιωάννα", "f", "Πώς να μην το ακούσω; Είναι ο πυρανιχνευτής στον διάδρομο. Όταν σφυρίζει έτσι, ένα σύντομο «μπιπ» κάθε λίγο, σημαίνει ότι η μπαταρία του τελειώνει. Δεν υπάρχει φωτιά.", "How could I not hear it? It's the smoke alarm in the hallway. When it beeps like that, one at a time, it means its battery is running out. There's no fire."),
  L("Σταύρος", "m", "Και γιατί αποφάσισε να μας το πει στις τρεις τα ξημερώματα; Πάντως εγώ τον βγάζω από το ταβάνι και τελείωσε. Ποτέ δεν μαγειρεύουμε κάτι επικίνδυνο.", "And why did it decide to tell us at three in the morning? Anyway, I'm taking it off the ceiling and that's that. We never cook anything dangerous."),
  L("Ιωάννα", "f", "Ούτε να το σκέφτεσαι. Θυμάσαι τον Ιανουάριο, που ξέχασες το μπρίκι στο μάτι και έλιωσε η λαβή; Αυτό το πράγμα σφύριξε πριν μυρίσουμε τίποτα. Αλλάζουμε την μπαταρία, δεν τον βγάζουμε.", "Don't even think about it. Remember in January, when you forgot the coffee pot on the hob and the handle melted? That thing went off before we smelled anything. We change the battery, we don't take it off."),
  L("Σταύρος", "m", "Καλά, καλά. Τι μπαταρία θέλει;", "OK, OK. What battery does it need?"),
  L("Ιωάννα", "f", "Μια τετράγωνη, εννιά βολτ. Θα πάρω από το περίπτερο το μεσημέρι. Και επειδή απ' ό,τι φαίνεται στο κουτί είναι πάνω από δέκα χρονών, θα στείλω και μήνυμα στον ιδιοκτήτη. Μετά από δέκα χρόνια οι αισθητήρες χάνουν την ευαισθησία τους και πρέπει να αλλάζει ολόκληρος.", "A square one, nine volts. I'll get one from the kiosk at midday. And since, from what it says on the box, it's over ten years old, I'll also send a message to the landlord. After ten years the sensors lose their sensitivity and the whole thing needs replacing."),
 ],
 "questions": [
  Q("Τι σημαίνει το σφύριγμα κάθε ένα λεπτό;", ["Ότι υπάρχει καπνός", "Ότι τελειώνει η μπαταρία", "Ότι ο πυρανιχνευτής έπαθε βλάβη", "Ότι κάποιος άνοιξε την πόρτα"], 1, "σημαίνει ότι η μπαταρία του τελειώνει"),
  Q("Γιατί η Ιωάννα δεν θέλει να βγάλουν τον πυρανιχνευτή;", ["Γιατί το απαγορεύει ο ιδιοκτήτης", "Γιατί είναι καινούργιος", "Γιατί τον Ιανουάριο σφύριξε πριν μυρίσουν τίποτα", "Γιατί είναι δύσκολο να τον ξεβιδώσουν"], 2, "Αυτό το πράγμα σφύριξε πριν μυρίσουμε τίποτα"),
  Q("Γιατί θα στείλει μήνυμα στον ιδιοκτήτη;", ["Γιατί ο πυρανιχνευτής είναι πάνω από δέκα χρονών και πρέπει να αλλάξει", "Για να της επιστρέψει τα χρήματα της μπαταρίας", "Για να παραπονεθεί για τον θόρυβο", "Για να του ζητήσει άδεια να τον βγάλουν"], 0, "είναι πάνω από δέκα χρονών"),
 ],
 "gloss": {"συγκάτοικους": "συγκάτοικος — flatmate", "ξημερώματα": "ξημερώματα — small hours", "τρελαθώ": "τρελαίνομαι — to go mad", "πυρανιχνευτής": "πυρανιχνευτής — smoke alarm", "σφυρίζει": "σφυρίζω — to whistle, beep", "ταβάνι": "ταβάνι — ceiling", "μπρίκι": "μπρίκι — small pot for Greek coffee", "μάτι": "μάτι (κουζίνας) — hob, burner", "λαβή": "λαβή — handle", "περίπτερο": "περίπτερο — kiosk", "αισθητήρες": "αισθητήρας — sensor", "ευαισθησία": "ευαισθησία — sensitivity"},
})

ITEMS.append({
 "id": "l178-news-kiniti-odontiatriki-monada", "title": "Κινητή οδοντιατρική μονάδα στα ορεινά χωριά", "title_en": "A mobile dental unit in the mountain villages", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση σε έναν περιφερειακό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνήτρια", "f", "Από την ερχόμενη εβδομάδα, μια κινητή οδοντιατρική μονάδα θα επισκέπτεται τα ορεινά χωριά του νομού, όπου δεν υπάρχει κανένας οδοντίατρος. Πρόκειται για ένα ειδικά διαμορφωμένο φορτηγάκι, με οδοντιατρική πολυθρόνα, μηχάνημα ακτινογραφιών και αποστειρωτή.", "From next week, a mobile dental unit will visit the mountain villages of the prefecture, where there is no dentist at all. It is a specially fitted van, with a dental chair, an X-ray machine and a steriliser."),
  L("Εκφωνήτρια", "f", "Η μονάδα θα μένει δύο μέρες σε κάθε χωριό και θα επιστρέφει κάθε τρεις μήνες. Οι εξετάσεις και οι καθαρισμοί θα είναι δωρεάν για παιδιά και για κατοίκους άνω των εξήντα πέντε. Για πιο σύνθετες θεραπείες, όπως εμφυτεύματα ή γέφυρες, οι ασθενείς θα παραπέμπονται στο κέντρο υγείας της πόλης.", "The unit will stay two days in each village and will return every three months. Check-ups and cleanings will be free for children and for residents over sixty-five. For more complex treatments, such as implants or bridges, patients will be referred to the town's health centre."),
  L("Εκφωνήτρια", "f", "Τα ραντεβού κλείνονται μέσω των κοινοτικών γραφείων. Σύμφωνα με τον υπεύθυνο του προγράμματος, πολλοί ηλικιωμένοι κάτοικοι έχουν να δουν οδοντίατρο πάνω από δέκα χρόνια, επειδή η διαδρομή ως την πόλη και πίσω τούς παίρνει όλη τη μέρα.", "Appointments are booked through the community offices. According to the head of the programme, many elderly residents haven't seen a dentist for over ten years, because the journey to town and back takes them the whole day."),
 ],
 "questions": [
  Q("Κάθε πότε θα επιστρέφει η μονάδα σε κάθε χωριό;", ["Κάθε εβδομάδα", "Κάθε τρεις μήνες", "Κάθε χρόνο", "Μόνο το καλοκαίρι"], 1, "θα επιστρέφει κάθε τρεις μήνες"),
  Q("Τι θα γίνεται με ένα εμφύτευμα;", ["Θα γίνεται δωρεάν στο φορτηγάκι", "Θα γίνεται μόνο σε παιδιά", "Ο ασθενής θα παραπέμπεται στο κέντρο υγείας της πόλης", "Δεν θα καλύπτεται καθόλου"], 2, "οι ασθενείς θα παραπέμπονται στο κέντρο υγείας της πόλης"),
  Q("Γιατί πολλοί ηλικιωμένοι δεν έχουν δει οδοντίατρο για χρόνια;", ["Γιατί η διαδρομή ως την πόλη και πίσω τούς παίρνει όλη τη μέρα", "Γιατί φοβούνται τον οδοντίατρο", "Γιατί δεν έχουν ασφάλεια", "Γιατί ο οδοντίατρος της πόλης έκλεισε"], 0, "η διαδρομή ως την πόλη και πίσω τούς παίρνει όλη τη μέρα"),
 ],
 "gloss": {"κινητή οδοντιατρική μονάδα": "κινητή μονάδα — mobile unit", "περιφερειακό": "περιφερειακός — regional", "ειδικά διαμορφωμένο": "ειδικά διαμορφωμένος — specially fitted", "φορτηγάκι": "φορτηγάκι — van, small truck", "πολυθρόνα": "πολυθρόνα — armchair (here: dental chair)", "ακτινογραφιών": "ακτινογραφία — X-ray", "αποστειρωτή": "αποστειρωτής — steriliser", "εμφυτεύματα": "εμφύτευμα — implant", "παραπέμπονται": "παραπέμπω — to refer", "κοινοτικών γραφείων": "κοινοτικό γραφείο — community office"},
})

ITEMS.append({
 "id": "l178-int-zografos-tampelon", "title": "Ο ζωγράφος των ταμπελών", "title_en": "The sign painter", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν από τους τελευταίους τεχνίτες στην Αθήνα που ζωγραφίζουν με το χέρι ταμπέλες για μαγαζιά.",
 "script": [
  L("Δημοσιογράφος", "f", "Σήμερα μια ταμπέλα τυπώνεται σε μια ώρα. Γιατί να ζωγραφίσει κανείς μία με το χέρι;", "Today a sign gets printed in an hour. Why would anyone paint one by hand?"),
  L("Τεχνίτης", "m", "Γιατί η τυπωμένη είναι ίδια με χιλιάδες άλλες. Τα γράμματα με το πινέλο έχουν μια μικρή ανωμαλία, μια ζωντάνια, που το μάτι την καταλαβαίνει ακόμα κι αν δεν ξέρει να την εξηγήσει. Πελάτες μου είναι συνήθως παλιά καφενεία, κουρεία και ζαχαροπλαστεία που θέλουν να κρατήσουν τον χαρακτήρα τους, αλλά και νέα μαγαζιά που θέλουν να δείχνουν παλιά.", "Because a printed one is the same as thousands of others. Letters done with a brush have a slight irregularity, a liveliness, that the eye notices even if it can't explain it. My customers are usually old cafés, barber shops and patisseries that want to keep their character, but also new shops that want to look old."),
  L("Δημοσιογράφος", "f", "Πώς μάθατε την τέχνη;", "How did you learn the craft?"),
  L("Τεχνίτης", "m", "Από έναν ηλικιωμένο μάστορα στο Μεταξουργείο, στα τέλη της δεκαετίας του ογδόντα. Τον πρώτο χρόνο δεν με άφηνε να ακουμπήσω ταμπέλα. Γέμιζα σελίδες ολόκληρες με το ίδιο γράμμα, το άλφα, ξανά και ξανά, ώσπου να βγαίνει ίσιο χωρίς χάρακα. Τα ελληνικά κεφαλαία είναι δύσκολα· το σίγμα και το ωμέγα θέλουν μεγάλη ισορροπία.", "From an elderly master in Metaxourgeio, at the end of the eighties. The first year he wouldn't let me touch a sign. I filled whole pages with the same letter, alpha, again and again, until it came out straight without a ruler. Greek capitals are hard; sigma and omega need great balance."),
  L("Δημοσιογράφος", "f", "Βλέπετε μέλλον στη δουλειά σας;", "Do you see a future in your work?"),
  L("Τεχνίτης", "m", "Περισσότερο απ' ό,τι πριν από δέκα χρόνια. Τώρα έρχονται νέοι γραφίστες και μου ζητούν να τους μάθω. Μεγάλωσαν μπροστά σε μια οθόνη και θέλουν να νιώσουν το πινέλο στο χέρι τους.", "More than ten years ago. Now young graphic designers come and ask me to teach them. They grew up in front of a screen and want to feel the brush in their hand."),
 ],
 "questions": [
  Q("Τι έχουν κατά τον τεχνίτη τα γράμματα με το πινέλο;", ["Πιο έντονα χρώματα", "Μια μικρή ανωμαλία, μια ζωντάνια", "Μεγαλύτερη αντοχή στη βροχή", "Χαμηλότερο κόστος"], 1, "Τα γράμματα με το πινέλο έχουν μια μικρή ανωμαλία, μια ζωντάνια"),
  Q("Τι έκανε τον πρώτο χρόνο της μαθητείας του;", ["Ζωγράφιζε μικρές ταμπέλες", "Καθάριζε τα πινέλα", "Γέμιζε σελίδες με το ίδιο γράμμα, ξανά και ξανά", "Έβαφε τοίχους"], 2, "Γέμιζα σελίδες ολόκληρες με το ίδιο γράμμα, το άλφα, ξανά και ξανά"),
  Q("Ποιοι του ζητούν σήμερα να τους μάθει την τέχνη;", ["Νέοι γραφίστες που μεγάλωσαν μπροστά σε μια οθόνη", "Συνταξιούχοι", "Φοιτητές αρχιτεκτονικής", "Ιδιοκτήτες καφενείων"], 0, "έρχονται νέοι γραφίστες και μου ζητούν να τους μάθω"),
 ],
 "gloss": {"ταμπέλες": "ταμπέλα — sign", "πινέλο": "πινέλο — (paint)brush", "ανωμαλία": "ανωμαλία — irregularity", "ζωντάνια": "ζωντάνια — liveliness", "κουρεία": "κουρείο — barber shop", "ζαχαροπλαστεία": "ζαχαροπλαστείο — patisserie", "μάστορα": "μάστορας — master craftsman", "ακουμπήσω": "ακουμπάω — to touch", "χάρακα": "χάρακας — ruler", "κεφαλαία": "κεφαλαίο (γράμμα) — capital letter", "γραφίστες": "γραφίστας — graphic designer"},
})

ITEMS.append({
 "id": "l178-c1-giati-gourgourizoun-oi-gates", "title": "Γιατί γουργουρίζουν οι γάτες", "title_en": "Why cats purr", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια κτηνίατρο να απαντά σε ερωτήσεις ακροατών σε μια ραδιοφωνική εκπομπή για το γουργούρισμα των γατών.",
 "script": [
  L("Παρουσιαστής", "m", "Μια ακροάτρια ρωτάει: όταν η γάτα της γουργουρίζει, σημαίνει πάντα ότι είναι ευχαριστημένη;", "A listener asks: when her cat purrs, does it always mean it's content?"),
  L("Κτηνίατρος", "f", "Όχι πάντα, και αυτό εκπλήσσει πολλούς. Οι γάτες γουργουρίζουν όταν τις χαϊδεύουμε, αλλά και όταν είναι πονεμένες, αγχωμένες ή ακόμα και λίγο πριν πεθάνουν. Η μητέρα γουργουρίζει όταν γεννάει, και τα γατάκια, που γεννιούνται τυφλά και κουφά, νιώθουν τη δόνηση και βρίσκουν έτσι τον δρόμο προς το στήθος της. Γι' αυτό πολλοί ερευνητές πιστεύουν ότι το γουργούρισμα δεν εκφράζει τόσο ευχαρίστηση όσο ένα αίτημα: «μείνε κοντά μου» ή «φρόντισέ με».", "Not always, and that surprises many people. Cats purr when we stroke them, but also when they're in pain, stressed or even shortly before they die. The mother purrs when giving birth, and the kittens, which are born blind and deaf, feel the vibration and so find their way to her belly. That's why many researchers believe purring expresses not so much pleasure as a request: 'stay close to me' or 'look after me'."),
  L("Παρουσιαστής", "m", "Και πώς παράγεται αυτός ο ήχος;", "And how is that sound produced?"),
  L("Κτηνίατρος", "f", "Για δεκαετίες η επικρατέστερη εξήγηση ήταν ότι οι μύες του λάρυγγα συσπώνται ρυθμικά και κάνουν τις φωνητικές χορδές να πάλλονται, τόσο στην εισπνοή όσο και στην εκπνοή. Πιο πρόσφατες μελέτες όμως έδειξαν ότι οι φωνητικές χορδές της γάτας έχουν ένα μικρό στρώμα ιστού που τους επιτρέπει να δονούνται σε πολύ χαμηλές συχνότητες, ακόμα και χωρίς συνεχή εντολή από τον εγκέφαλο. Το ζήτημα, με άλλα λόγια, δεν έχει κλείσει.", "For decades the prevailing explanation was that the muscles of the larynx contract rhythmically and make the vocal folds vibrate, both on breathing in and breathing out. More recent studies, however, have shown that a cat's vocal folds have a small layer of tissue that lets them vibrate at very low frequencies, even without continuous commands from the brain. The question, in other words, isn't closed."),
  L("Κτηνίατρος", "f", "Θα ακούσετε επίσης ότι η συχνότητα του γουργουρίσματος βοηθά να γιατρεύονται τα κόκαλα. Είναι μια γοητευτική υπόθεση, αλλά προς το παρόν δεν υπάρχουν αρκετά στοιχεία που να την αποδεικνύουν. Καλό είναι να την ακούμε με επιφύλαξη.", "You'll also hear that the frequency of purring helps bones heal. It's a fascinating hypothesis, but for now there isn't enough evidence to prove it. It's best to treat it with caution."),
 ],
 "questions": [
  Q("Σε ποια περίπτωση ΔΕΝ αναφέρει η κτηνίατρος ότι γουργουρίζουν οι γάτες;", ["Όταν τις χαϊδεύουμε", "Όταν κυνηγούν", "Όταν είναι πονεμένες", "Όταν η μητέρα γεννάει"], 1, "Οι γάτες γουργουρίζουν όταν τις χαϊδεύουμε, αλλά και όταν είναι πονεμένες"),
  Q("Τι έδειξαν οι πιο πρόσφατες μελέτες;", ["Ότι ο ήχος βγαίνει από τη μύτη", "Ότι μόνο οι θηλυκές γάτες γουργουρίζουν", "Ότι οι φωνητικές χορδές μπορούν να δονούνται χαμηλά ακόμα και χωρίς συνεχή εντολή από τον εγκέφαλο", "Ότι το γουργούρισμα γίνεται μόνο στην εκπνοή"], 2, "να δονούνται σε πολύ χαμηλές συχνότητες, ακόμα και χωρίς συνεχή εντολή από τον εγκέφαλο"),
  Q("Πώς κρίνει η κτηνίατρος την ιδέα ότι το γουργούρισμα γιατρεύει τα κόκαλα;", ["Ως γοητευτική υπόθεση χωρίς αρκετά στοιχεία ακόμα", "Ως αποδεδειγμένο γεγονός", "Ως εντελώς λανθασμένη", "Δεν την αναφέρει"], 0, "Είναι μια γοητευτική υπόθεση, αλλά προς το παρόν δεν υπάρχουν αρκετά στοιχεία"),
 ],
 "gloss": {"γουργούρισμα": "γουργούρισμα — purring", "γουργουρίζει": "γουργουρίζω — to purr", "εκπλήσσει": "εκπλήσσω — to surprise", "πονεμένες": "πονεμένος — in pain", "δόνηση": "δόνηση — vibration", "επικρατέστερη": "επικρατέστερος — prevailing", "λάρυγγα": "λάρυγγας — larynx", "συσπώνται": "συσπώμαι — to contract", "φωνητικές χορδές": "φωνητική χορδή — vocal fold, vocal cord", "πάλλονται": "πάλλομαι — to vibrate", "ιστού": "ιστός — tissue", "με επιφύλαξη": "με επιφύλαξη — with reservation, cautiously"},
})

ITEMS.append({
 "id": "l178-c1-giati-kanoun-krak-ta-daktyla", "title": "Γιατί «κάνουν κρακ» τα δάχτυλα", "title_en": "Why knuckles crack", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν ρευματολόγο να εξηγεί σε ένα επιστημονικό ραδιόφωνο τι συμβαίνει όταν «σπάμε» τα δάχτυλά μας.",
 "script": [
  L("Ρευματολόγος", "m", "Οι αρθρώσεις των δαχτύλων περιβάλλονται από μια κάψα γεμάτη με ένα παχύρρευστο υγρό, το αρθρικό υγρό, που λειτουργεί σαν λιπαντικό. Όταν τραβάμε ή λυγίζουμε απότομα ένα δάχτυλο, οι επιφάνειες της άρθρωσης απομακρύνονται, η πίεση μέσα στην κάψα πέφτει και τα αέρια που είναι διαλυμένα στο υγρό σχηματίζουν μια φυσαλίδα. Αυτό το φαινόμενο λέγεται σπηλαίωση.", "The finger joints are surrounded by a capsule filled with a thick fluid, synovial fluid, which acts as a lubricant. When we pull or sharply bend a finger, the surfaces of the joint move apart, the pressure inside the capsule drops, and the gases dissolved in the fluid form a bubble. This phenomenon is called cavitation."),
  L("Ρευματολόγος", "m", "Για χρόνια οι επιστήμονες διαφωνούσαν αν ο ήχος προέρχεται από τη στιγμή που σχηματίζεται η φυσαλίδα ή από τη στιγμή που σκάει. Μια μελέτη του 2015, που κατέγραψε την άρθρωση με μαγνητική τομογραφία σε πραγματικό χρόνο, έδειξε ότι ο ήχος συμπίπτει με τον σχηματισμό της κοιλότητας. Γι' αυτό, παρεμπιπτόντως, δεν μπορείτε να ξανακάνετε κρακ το ίδιο δάχτυλο αμέσως: χρειάζονται περίπου είκοσι λεπτά μέχρι να διαλυθούν ξανά τα αέρια.", "For years scientists disagreed about whether the sound comes from the moment the bubble forms or from the moment it bursts. A 2015 study, which filmed the joint with real-time magnetic resonance imaging, showed that the sound coincides with the formation of the cavity. That's why, incidentally, you can't crack the same finger again right away: it takes about twenty minutes for the gases to dissolve again."),
  L("Ρευματολόγος", "m", "Και η μεγάλη ερώτηση: προκαλεί αρθρίτιδα; Όλα τα στοιχεία που έχουμε λένε όχι. Ένας Αμερικανός γιατρός έσπαγε επί εξήντα χρόνια τα δάχτυλα μόνο του ενός χεριού, για να το ελέγξει ο ίδιος, και στο τέλος δεν βρήκε καμία διαφορά ανάμεσα στα δύο. Ένα πείραμα με έναν μόνο συμμετέχοντα δεν αποδεικνύει βέβαια τίποτα, όμως και οι μεγαλύτερες μελέτες καταλήγουν στο ίδιο. Αν πάντως υπάρχει πόνος ή πρήξιμο, αυτό είναι άλλη ιστορία και χρειάζεται εξέταση.", "And the big question: does it cause arthritis? All the evidence we have says no. An American doctor cracked the knuckles of only one hand for sixty years, to test it himself, and in the end found no difference between the two. An experiment with a single participant proves nothing, of course, but larger studies come to the same conclusion. If there is pain or swelling, though, that's another story and needs to be examined."),
 ],
 "questions": [
  Q("Τι προκαλεί τον σχηματισμό της φυσαλίδας;", ["Ο αέρας που μπαίνει από το δέρμα", "Η πτώση της πίεσης μέσα στην κάψα της άρθρωσης", "Η τριβή των οστών", "Ένα σπάσιμο του χόνδρου"], 1, "η πίεση μέσα στην κάψα πέφτει και τα αέρια που είναι διαλυμένα στο υγρό σχηματίζουν μια φυσαλίδα"),
  Q("Γιατί δεν μπορούμε να ξανακάνουμε κρακ το ίδιο δάχτυλο αμέσως;", ["Γιατί η άρθρωση πονάει", "Γιατί το υγρό έχει χυθεί", "Γιατί χρειάζονται περίπου είκοσι λεπτά μέχρι να διαλυθούν ξανά τα αέρια", "Γιατί οι μύες κουράζονται"], 2, "χρειάζονται περίπου είκοσι λεπτά μέχρι να διαλυθούν ξανά τα αέρια"),
  Q("Πώς σχολιάζει ο ρευματολόγος το πείραμα του Αμερικανού γιατρού;", ["Μόνο του δεν αποδεικνύει τίποτα, αλλά οι μεγαλύτερες μελέτες καταλήγουν στο ίδιο", "Το θεωρεί την απόλυτη απόδειξη", "Λέει ότι τα αποτελέσματά του ήταν λανθασμένα", "Λέει ότι έδειξε αρθρίτιδα στο ένα χέρι"], 0, "Ένα πείραμα με έναν μόνο συμμετέχοντα δεν αποδεικνύει βέβαια τίποτα, όμως και οι μεγαλύτερες μελέτες καταλήγουν στο ίδιο"),
 ],
 "gloss": {"ρευματολόγο": "ρευματολόγος — rheumatologist", "αρθρώσεις": "άρθρωση — joint", "κάψα": "κάψα — capsule", "παχύρρευστο": "παχύρρευστος — thick, viscous", "αρθρικό υγρό": "αρθρικό υγρό — synovial fluid", "λιπαντικό": "λιπαντικό — lubricant", "λυγίζουμε": "λυγίζω — to bend", "διαλυμένα": "διαλυμένος — dissolved", "φυσαλίδα": "φυσαλίδα — bubble", "σπηλαίωση": "σπηλαίωση — cavitation", "μαγνητική τομογραφία": "μαγνητική τομογραφία — MRI", "συμπίπτει": "συμπίπτω — to coincide", "κοιλότητας": "κοιλότητα — cavity", "παρεμπιπτόντως": "παρεμπιπτόντως — incidentally", "αρθρίτιδα": "αρθρίτιδα — arthritis", "πρήξιμο": "πρήξιμο — swelling"},
})

rnd = random.Random(178)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-178.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
