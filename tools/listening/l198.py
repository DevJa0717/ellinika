# Source for library/listening/listening-198.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l198.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l198-ann-dendryllia", "title": "Δωρεάν δενδρύλλια από τον δήμο", "title_en": "Free saplings from the municipality", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση στον δημοτικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνητής", "m", "Ο δήμος ενημερώνει τους δημότες ότι την Κυριακή 30 Νοεμβρίου, από τις δέκα το πρωί ως τις δύο το μεσημέρι, θα μοιραστούν δωρεάν δενδρύλλια στο δημοτικό φυτώριο, δίπλα στο κολυμβητήριο. Θα διατεθούν συνολικά δύο χιλιάδες δενδρύλλια, κυρίως ελιές, λεμονιές, χαρουπιές και πλατάνια.", "The municipality informs residents that on Sunday 30 November, from ten in the morning until two in the afternoon, free saplings will be handed out at the municipal nursery, next to the swimming pool. A total of two thousand saplings will be available, mainly olive, lemon, carob and plane trees."),
  L("Εκφωνητής", "m", "Κάθε νοικοκυριό μπορεί να πάρει μέχρι τρία δενδρύλλια, δείχνοντας έναν λογαριασμό ρεύματος ή νερού με διεύθυνση μέσα στον δήμο. Σχολεία και σύλλογοι που θέλουν περισσότερα πρέπει να κάνουν αίτηση ως την Τετάρτη μέσω της ιστοσελίδας.", "Each household can take up to three saplings by showing an electricity or water bill with an address within the municipality. Schools and associations that want more must apply by Wednesday through the website."),
  L("Εκφωνητής", "m", "Γεωπόνοι του δήμου θα βρίσκονται στο φυτώριο για να δίνουν συμβουλές για το φύτεμα και το πότισμα. Παρακαλούνται οι πολίτες να φέρουν δικές τους σακούλες ή καφάσια.", "The municipality's agronomists will be at the nursery to give advice on planting and watering. Citizens are asked to bring their own bags or crates."),
 ],
 "questions": [
  Q("Πού θα μοιραστούν τα δενδρύλλια;", ["Στο δημαρχείο", "Στο δημοτικό φυτώριο", "Στα σχολεία", "Στη λαϊκή αγορά"], 1, "στο δημοτικό φυτώριο"),
  Q("Τι πρέπει να δείξει κάθε νοικοκυριό;", ["Την ταυτότητα", "Έναν λογαριασμό ρεύματος ή νερού", "Μια αίτηση", "Μια απόδειξη πληρωμής"], 1, "δείχνοντας έναν λογαριασμό ρεύματος ή νερού"),
  Q("Τι ζητείται από τους πολίτες;", ["Να έρθουν νωρίς", "Να φέρουν δικές τους σακούλες ή καφάσια", "Να κλείσουν ραντεβού", "Να πληρώσουν ένα μικρό ποσό"], 1, "να φέρουν δικές τους σακούλες ή καφάσια"),
 ],
 "gloss": {"δενδρύλλια": "δενδρύλλιο — sapling", "φυτώριο": "φυτώριο — plant nursery", "νοικοκυριό": "νοικοκυριό — household", "Γεωπόνοι": "γεωπόνος — agronomist", "καφάσια": "καφάσι — crate"},
})

ITEMS.append({
 "id": "l198-int-gamilies-tourtes", "title": "Η ζαχαροπλάστρια των γαμήλιων τούρτων", "title_en": "The wedding-cake maker", "type": "interview", "level": "B2",
 "context_el": "Συνέντευξη με μια ζαχαροπλάστρια που φτιάχνει γαμήλιες τούρτες στη Θεσσαλονίκη.",
 "script": [
  L("Δημοσιογράφος", "m", "Ποια είναι η πιο δύσκολη τούρτα που έχετε φτιάξει;", "What's the hardest cake you've ever made?"),
  L("Ζαχαροπλάστρια", "f", "Μια τούρτα πέντε ορόφων για έναν γάμο σε ένα νησί, τον Αύγουστο. Η τούρτα ταξίδεψε με το πλοίο σε ένα ψυγείο, και εγώ μαζί της. Όλο το ταξίδι κοίταζα το θερμόμετρο. Όταν φτάσαμε, τη συναρμολόγησα σε μια κουζίνα χωρίς κλιματισμό, με τριάντα οχτώ βαθμούς. Άντεξε, αλλά εγώ όχι και τόσο.", "A five-tier cake for a wedding on an island, in August. The cake travelled on the ferry in a fridge, and so did I. The whole journey I was watching the thermometer. When we arrived, I assembled it in a kitchen without air conditioning, at thirty-eight degrees. It held up, but I didn't quite."),
  L("Δημοσιογράφος", "m", "Τι ζητούν σήμερα τα ζευγάρια;", "What do couples ask for today?"),
  L("Ζαχαροπλάστρια", "f", "Πιο απλές τούρτες και λιγότερη ζάχαρη. Παλιά όλοι ήθελαν λευκή κρέμα και λουλούδια από ζαχαρόπαστα. Τώρα ζητούν φρέσκα φρούτα, ελληνικές γεύσεις, μαστίχα, σύκο, καρύδι. Πολλά ζευγάρια μάλιστα δεν θέλουν καν μεγάλη τούρτα· προτιμούν μια μικρή για τη φωτογραφία και γλυκά σε ατομικές μερίδες για τους καλεσμένους.", "Simpler cakes and less sugar. In the past everyone wanted white cream and sugar-paste flowers. Now they ask for fresh fruit, Greek flavours, mastic, fig, walnut. Many couples don't even want a big cake; they prefer a small one for the photo and individual desserts for the guests."),
  L("Δημοσιογράφος", "m", "Δοκιμάζετε κομμάτι από κάθε τούρτα;", "Do you taste a piece of every cake?"),
  L("Ζαχαροπλάστρια", "f", "Ποτέ στον γάμο. Τη δοκιμάζουμε μαζί με το ζευγάρι δύο μήνες πριν. Στον γάμο φεύγω πριν από την κοπή. Αν την έβλεπα να κόβεται, θα έκλαιγα περισσότερο από τη μητέρα της νύφης.", "Never at the wedding. We taste it together with the couple two months before. At the wedding I leave before the cutting. If I watched it being cut, I'd cry more than the bride's mother."),
 ],
 "questions": [
  Q("Πώς ταξίδεψε η τούρτα των πέντε ορόφων;", ["Με αεροπλάνο", "Με το πλοίο, μέσα σε ψυγείο", "Με φορτηγό", "Την έφτιαξε στο νησί από την αρχή"], 1, "Η τούρτα ταξίδεψε με το πλοίο σε ένα ψυγείο"),
  Q("Τι ζητούν σήμερα πολλά ζευγάρια;", ["Μεγαλύτερες τούρτες", "Λουλούδια από ζαχαρόπαστα", "Πιο απλές τούρτες με λιγότερη ζάχαρη", "Τούρτες σοκολάτας"], 2, "Πιο απλές τούρτες και λιγότερη ζάχαρη"),
  Q("Γιατί φεύγει από τον γάμο πριν από την κοπή;", ["Γιατί έχει κι άλλη δουλειά", "Γιατί θα έκλαιγε αν την έβλεπε να κόβεται", "Γιατί δεν είναι καλεσμένη", "Γιατί είναι κουρασμένη"], 1, "Αν την έβλεπα να κόβεται, θα έκλαιγα"),
 ],
 "gloss": {"γαμήλιες": "γαμήλιος — wedding (adj.)", "ορόφων": "όροφος — tier, floor", "συναρμολόγησα": "συναρμολογώ — to assemble", "ζαχαρόπαστα": "ζαχαρόπαστα — sugar paste, fondant", "μερίδες": "μερίδα — portion", "κοπή": "κοπή — cutting"},
})

ITEMS.append({
 "id": "l198-vm-antallagi-glosson", "title": "Μήνυμα από τη συνεργάτιδα ανταλλαγής γλωσσών", "title_en": "A message from a language-exchange partner", "type": "voicemail", "level": "B2",
 "context_el": "Κάνετε ανταλλαγή γλωσσών με μια Ισπανίδα που ζει στην Αθήνα. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Λουθία", "f", "Γεια σου, η Λουθία είμαι! Συγγνώμη, αλλά αύριο δεν μπορώ να έρθω στο καφέ στις έξι, γιατί μου άλλαξαν τη βάρδια στη δουλειά. Μπορούμε να το κάνουμε την Πέμπτη την ίδια ώρα; Αν δεν σε βολεύει, πες μου εσύ.", "Hi, it's Lucía! Sorry, but tomorrow I can't come to the café at six, because they changed my shift at work. Can we do it on Thursday at the same time? If that doesn't suit you, you tell me."),
  L("Λουθία", "f", "Και κάτι ακόμα: την προηγούμενη φορά μιλήσαμε σχεδόν μία ώρα ελληνικά και μόνο δέκα λεπτά ισπανικά. Είναι δικό μου λάθος, γιατί μου αρέσει πολύ να μιλάω! Αυτή τη φορά βάζω χρονόμετρο: μισή ώρα στη μία γλώσσα, μισή στην άλλη.", "And one more thing: last time we spoke Greek for almost an hour and Spanish for only ten minutes. It's my fault, because I really like talking! This time I'm setting a timer: half an hour in one language, half in the other."),
  L("Λουθία", "f", "Α, και φέρε μου, αν θυμηθείς, εκείνο το βιβλίο με τις παροιμίες που μου είπες. Θέλω να μάθω να λέω «κάθε εμπόδιο για καλό» χωρίς να γελάνε οι συνάδελφοί μου. Φιλιά!", "Oh, and bring me, if you remember, that book of proverbs you told me about. I want to learn to say 'every obstacle is for the best' without my colleagues laughing. Kisses!"),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί να έρθει αύριο η Λουθία;", ["Είναι άρρωστη", "Της άλλαξαν τη βάρδια στη δουλειά", "Θα ταξιδέψει", "Έχει μάθημα"], 1, "μου άλλαξαν τη βάρδια στη δουλειά"),
  Q("Τι πρόβλημα υπήρξε την προηγούμενη φορά;", ["Άργησαν και οι δύο", "Μίλησαν πολύ περισσότερο ελληνικά απ' ό,τι ισπανικά", "Το καφέ ήταν κλειστό", "Δεν είχαν θέμα συζήτησης"], 1, "μιλήσαμε σχεδόν μία ώρα ελληνικά και μόνο δέκα λεπτά ισπανικά"),
  Q("Τι της ζητάει να φέρει;", ["Ένα λεξικό", "Ένα βιβλίο με παροιμίες", "Ένα χρονόμετρο", "Τις σημειώσεις της"], 1, "εκείνο το βιβλίο με τις παροιμίες"),
 ],
 "gloss": {"ανταλλαγή": "ανταλλαγή — exchange", "βάρδια": "βάρδια — shift", "βολεύει": "βολεύω — to suit, be convenient", "χρονόμετρο": "χρονόμετρο — timer, stopwatch", "παροιμίες": "παροιμία — proverb"},
})

ITEMS.append({
 "id": "l198-mono-imerologio-evgnomosynis", "title": "Το ημερολόγιο ευγνωμοσύνης μου", "title_en": "My gratitude diary", "type": "monologue", "level": "B2",
 "context_el": "Μια ακροάτρια μιλάει σε μια ραδιοφωνική εκπομπή για μια συνήθεια που απέκτησε.",
 "script": [
  L("Ευαγγελία", "f", "Πριν από δύο χρόνια περνούσα μια πολύ δύσκολη περίοδο. Είχα χάσει τη δουλειά μου και κάθε βράδυ, πριν κοιμηθώ, σκεφτόμουν μόνο τι πήγε στραβά. Μια φίλη μού έκανε δώρο ένα μικρό τετράδιο και μου είπε: «Γράφε κάθε βράδυ τρία πράγματα για τα οποία είσαι ευγνώμων. Μικρά, όχι μεγάλα.»", "Two years ago I was going through a very difficult period. I'd lost my job and every night, before sleeping, I only thought about what had gone wrong. A friend gave me a small notebook as a present and said: 'Every night write three things you're grateful for. Small ones, not big ones.'"),
  L("Ευαγγελία", "f", "Στην αρχή μού φαινόταν ανόητο. Τι να γράψω; Όμως άρχισα: «Ο φούρναρης μου κράτησε το τελευταίο κουλούρι». «Η γάτα κοιμήθηκε στα πόδια μου». «Βρήκα πάρκινγκ με την πρώτη». Μετά από μερικές εβδομάδες παρατήρησα κάτι παράξενο: μέσα στη μέρα άρχισα να προσέχω αυτά τα μικρά πράγματα, για να τα θυμηθώ το βράδυ.", "At first it seemed silly to me. What would I write? But I started: 'The baker kept the last bread ring for me.' 'The cat slept on my feet.' 'I found a parking space first time.' After a few weeks I noticed something strange: during the day I started paying attention to these little things, so I could remember them in the evening."),
  L("Ευαγγελία", "f", "Δεν λέω ότι ένα τετράδιο λύνει τα προβλήματα. Τη δουλειά τη βρήκα με πολύ ψάξιμο, όχι με το τετράδιο. Αλλά κοιμάμαι καλύτερα. Έχω γεμίσει ήδη τέσσερα τετράδια, και όταν έχω μια άσχημη μέρα, ανοίγω ένα στην τύχη και διαβάζω.", "I'm not saying a notebook solves problems. I found the job through a lot of searching, not with the notebook. But I sleep better. I've already filled four notebooks, and when I have a bad day, I open one at random and read."),
 ],
 "questions": [
  Q("Τι της πρότεινε η φίλη της;", ["Να βρει καινούργια δουλειά", "Να γράφει κάθε βράδυ τρία πράγματα για τα οποία είναι ευγνώμων", "Να πάει σε ψυχολόγο", "Να κάνει γυμναστική"], 1, "Γράφε κάθε βράδυ τρία πράγματα για τα οποία είσαι ευγνώμων"),
  Q("Τι παρατήρησε μετά από μερικές εβδομάδες;", ["Ότι βαριόταν να γράφει", "Ότι μέσα στη μέρα πρόσεχε τα μικρά πράγματα", "Ότι η φίλη της είχε άδικο", "Ότι κοιμόταν λιγότερο"], 1, "άρχισα να προσέχω αυτά τα μικρά πράγματα"),
  Q("Τι κάνει όταν έχει μια άσχημη μέρα;", ["Τηλεφωνεί στη φίλη της", "Ανοίγει ένα τετράδιο στην τύχη και διαβάζει", "Γράφει τι πήγε στραβά", "Βγαίνει βόλτα με τη γάτα"], 1, "ανοίγω ένα στην τύχη και διαβάζω"),
 ],
 "gloss": {"ευγνώμων": "ευγνώμων — grateful", "στραβά": "πάει στραβά — to go wrong", "ανόητο": "ανόητος — silly, foolish", "κουλούρι": "κουλούρι — sesame bread ring", "ψάξιμο": "ψάξιμο — searching"},
})

ITEMS.append({
 "id": "l198-dia-gataki", "title": "Θα κρατήσουμε το γατάκι που βρήκαμε;", "title_en": "Shall we keep the kitten we found?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι συζητάει για ένα γατάκι που βρήκε έξω από την πολυκατοικία.",
 "script": [
  L("Στέλιος", "m", "Το βρήκα κάτω από ένα αυτοκίνητο, βρεγμένο και να νιαουρίζει. Δεν μπορούσα να το αφήσω εκεί. Του έδωσα λίγο γάλα.", "I found it under a car, wet and meowing. I couldn't leave it there. I gave it some milk."),
  L("Χαρά", "f", "Γάλα όχι, Στέλιο, κάνει κακό στις γάτες. Του δίνουμε νερό και λίγη τροφή για γατάκια. Αλλά πες μου ειλικρινά: σκέφτεσαι να το κρατήσουμε; Ταξιδεύουμε κάθε δεύτερο Σαββατοκύριακο, και ο ιδιοκτήτης έχει γράψει στο συμβόλαιο ότι δεν θέλει ζώα.", "Not milk, Stelios, it's bad for cats. We give it water and a little kitten food. But tell me honestly: are you thinking of keeping it? We travel every other weekend, and the landlord has written in the contract that he doesn't want animals."),
  L("Στέλιος", "m", "Το ξέρω. Ας το πάμε πρώτα στον κτηνίατρο να δούμε αν έχει τσιπάκι. Μπορεί να είναι κάποιου. Αν όχι, ρωτάμε την κυρία Φωφώ στον τρίτο. Έχει ήδη δύο γάτες και πάντα λέει ότι της λείπει μια τρίτη.", "I know. Let's take it to the vet first to see if it has a microchip. It might belong to someone. If not, we ask Mrs Fofo on the third floor. She already has two cats and always says she misses a third."),
  L("Χαρά", "f", "Καλή ιδέα. Και αν δεν το θέλει ούτε εκείνη, το κρατάμε μέχρι να του βρούμε σπίτι. Μόνο μην του δώσεις όνομα, γιατί τότε δεν θα το αποχωριστούμε ποτέ.", "Good idea. And if she doesn't want it either, we keep it until we find it a home. Just don't give it a name, because then we'll never part with it."),
  L("Στέλιος", "m", "Εεε... ήδη το λέω Μπισκότο.", "Erm... I'm already calling it Biscuit."),
 ],
 "questions": [
  Q("Τι λέει η Χαρά για το γάλα;", ["Ότι είναι καλό για τα γατάκια", "Ότι κάνει κακό στις γάτες", "Ότι πρέπει να είναι ζεστό", "Ότι δεν έχουν στο σπίτι"], 1, "Γάλα όχι, Στέλιο, κάνει κακό στις γάτες"),
  Q("Γιατί δυσκολεύονται να κρατήσουν το γατάκι;", ["Γιατί είναι αλλεργικοί", "Γιατί ταξιδεύουν συχνά και ο ιδιοκτήτης δεν θέλει ζώα", "Γιατί έχουν ήδη σκύλο", "Γιατί το σπίτι είναι μικρό"], 1, "ο ιδιοκτήτης έχει γράψει στο συμβόλαιο ότι δεν θέλει ζώα"),
  Q("Γιατί η Χαρά δεν θέλει να δώσουν όνομα στο γατάκι;", ["Γιατί δεν τους ανήκει", "Γιατί τότε δεν θα το αποχωριστούν ποτέ", "Γιατί θα το ονομάσει η κυρία Φωφώ", "Γιατί είναι πολύ μικρό"], 1, "γιατί τότε δεν θα το αποχωριστούμε ποτέ"),
 ],
 "gloss": {"νιαουρίζει": "νιαουρίζω — to meow", "συμβόλαιο": "συμβόλαιο — (rental) contract", "τσιπάκι": "τσιπάκι — microchip", "αποχωριστούμε": "αποχωρίζομαι — to part with"},
})

ITEMS.append({
 "id": "l198-rep-scholeio-xenonas", "title": "Το κλειστό σχολείο του χωριού γίνεται ξενώνας για πεζοπόρους", "title_en": "The village's closed school becomes a hikers' hostel", "type": "report", "level": "B2",
 "context_el": "Ρεπορτάζ από μια ραδιοφωνική εκπομπή για την ύπαιθρο.",
 "script": [
  L("Ρεπόρτερ", "m", "Το δημοτικό σχολείο του χωριού έκλεισε πριν από δεκαπέντε χρόνια, όταν έμειναν μόνο δύο μαθητές. Από τότε το πέτρινο κτίριο ήταν άδειο, με σπασμένα παράθυρα και έναν πίνακα που έγραφε ακόμα την τελευταία ημερομηνία μαθήματος.", "The village primary school closed fifteen years ago, when only two pupils were left. Since then the stone building had been empty, with broken windows and a blackboard still showing the date of the last lesson."),
  L("Ρεπόρτερ", "m", "Πέρσι ο πολιτιστικός σύλλογος του χωριού ζήτησε από τον δήμο να του παραχωρήσει το κτίριο. Με χρήματα από ένα ευρωπαϊκό πρόγραμμα και πολλή εθελοντική δουλειά, οι δύο αίθουσες έγιναν κοιτώνες με είκοσι κρεβάτια, και το γραφείο του δασκάλου μια μικρή κοινόχρηστη κουζίνα.", "Last year the village cultural association asked the municipality to grant it the building. With money from a European programme and a lot of volunteer work, the two classrooms became dormitories with twenty beds, and the teacher's office a small shared kitchen."),
  L("Ρεπόρτερ", "m", "Ο ξενώνας βρίσκεται πάνω σε ένα παλιό μονοπάτι που ενώνει τρία χωριά, και ήδη το πρώτο καλοκαίρι φιλοξένησε πάνω από τετρακόσιους πεζοπόρους. Τον πίνακα τον κράτησαν στη θέση του. Οι επισκέπτες γράφουν πάνω του με κιμωλία από πού ήρθαν, και οι παλιοί μαθητές του σχολείου έρχονται να διαβάσουν.", "The hostel lies on an old path linking three villages, and already in its first summer it hosted over four hundred hikers. They kept the blackboard in its place. Visitors write on it in chalk where they came from, and the school's former pupils come to read."),
 ],
 "questions": [
  Q("Γιατί έκλεισε το σχολείο;", ["Γιατί χάλασε το κτίριο", "Γιατί έμειναν μόνο δύο μαθητές", "Γιατί έφυγε ο δάσκαλος", "Γιατί έγινε καινούργιο σχολείο"], 1, "όταν έμειναν μόνο δύο μαθητές"),
  Q("Σε τι μετατράπηκαν οι δύο αίθουσες;", ["Σε μουσείο", "Σε κοιτώνες με είκοσι κρεβάτια", "Σε καφενείο", "Σε κουζίνα"], 1, "οι δύο αίθουσες έγιναν κοιτώνες με είκοσι κρεβάτια"),
  Q("Τι γράφουν οι επισκέπτες στον πίνακα;", ["Τα ονόματα των παλιών μαθητών", "Από πού ήρθαν", "Τη διαδρομή του μονοπατιού", "Τις τιμές του ξενώνα"], 1, "γράφουν πάνω του με κιμωλία από πού ήρθαν"),
 ],
 "gloss": {"ξενώνας": "ξενώνας — hostel, guesthouse", "πεζοπόρους": "πεζοπόρος — hiker", "παραχωρήσει": "παραχωρώ — to grant, hand over", "κοιτώνες": "κοιτώνας — dormitory", "κοινόχρηστη": "κοινόχρηστος — shared, communal", "κιμωλία": "κιμωλία — chalk"},
})

ITEMS.append({
 "id": "l198-int-cheiristis-geranou", "title": "Ο χειριστής γερανού", "title_en": "The crane operator", "type": "interview", "level": "B2",
 "context_el": "Συνέντευξη με έναν χειριστή γερανού σε ένα μεγάλο εργοτάξιο.",
 "script": [
  L("Δημοσιογράφος", "f", "Πόσο ψηλά δουλεύετε;", "How high up do you work?"),
  L("Χειριστής", "m", "Η καμπίνα μου είναι στα πενήντα πέντε μέτρα. Ανεβαίνω με μια σκάλα, κάθε πρωί, περίπου είκοσι λεπτά. Γι' αυτό παίρνω μαζί μου νερό, φαγητό και ό,τι άλλο χρειάζομαι για όλη τη μέρα. Αν ξεχάσω κάτι κάτω, ξεχνάω και το διάλειμμα.", "My cab is at fifty-five metres. I climb up a ladder every morning, about twenty minutes. That's why I take water, food and whatever else I need for the whole day. If I forget something down below, I forget my break too."),
  L("Δημοσιογράφος", "f", "Πώς ξέρετε πού να αφήσετε το φορτίο, αφού δεν βλέπετε πάντα κάτω;", "How do you know where to put the load down, since you can't always see below?"),
  L("Χειριστής", "m", "Έχω πάντα έναν συνεργάτη στο έδαφος, τον σημαιωτή. Μιλάμε με ασύρματο και, όταν δεν ακούγεται, με σήματα με τα χέρια. Είναι σαν χορός για δύο: αν δεν εμπιστεύεσαι τον άλλον, δεν γίνεται. Με τον Βαγγέλη δουλεύουμε μαζί δώδεκα χρόνια και καταλαβαινόμαστε με μια ματιά, ακόμα κι από πενήντα μέτρα.", "I always have a partner on the ground, the banksman. We talk by radio and, when it can't be heard, with hand signals. It's like a dance for two: if you don't trust the other person, it doesn't work. Vangelis and I have worked together for twelve years and we understand each other at a glance, even from fifty metres."),
  L("Δημοσιογράφος", "f", "Πότε σταματάτε τη δουλειά;", "When do you stop work?"),
  L("Χειριστής", "m", "Όταν φυσάει πολύ. Ο γερανός έχει ανεμόμετρο, και πάνω από ένα όριο απαγορεύεται να σηκώσουμε φορτίο. Τότε κάθομαι και κοιτάζω την πόλη από ψηλά. Έχω τη θέα που πληρώνουν άλλοι για να τη δουν από τα ρετιρέ.", "When it's very windy. The crane has an anemometer, and above a limit we're not allowed to lift a load. Then I sit and look at the city from above. I have the view that others pay to see from penthouses."),
 ],
 "questions": [
  Q("Γιατί παίρνει μαζί του ό,τι χρειάζεται για όλη τη μέρα;", ["Γιατί δεν υπάρχει κουζίνα στο εργοτάξιο", "Γιατί η ανάβαση στην καμπίνα κρατάει πολύ", "Γιατί δουλεύει τη νύχτα", "Γιατί του το ζητάει ο προϊστάμενος"], 1, "Ανεβαίνω με μια σκάλα, κάθε πρωί, περίπου είκοσι λεπτά"),
  Q("Πώς επικοινωνεί με τον συνεργάτη του όταν δεν ακούγεται ο ασύρματος;", ["Με το κινητό", "Με σήματα με τα χέρια", "Με φωτεινά σήματα", "Φωνάζοντας"], 1, "με σήματα με τα χέρια"),
  Q("Πότε απαγορεύεται να σηκώσουν φορτίο;", ["Όταν βρέχει", "Όταν ο άνεμος ξεπερνά ένα όριο", "Τη νύχτα", "Τα Σαββατοκύριακα"], 1, "πάνω από ένα όριο απαγορεύεται να σηκώσουμε φορτίο"),
 ],
 "gloss": {"γερανού": "γερανός — crane", "εργοτάξιο": "εργοτάξιο — construction site", "φορτίο": "φορτίο — load", "σημαιωτή": "σημαιωτής — banksman, signaller", "ασύρματο": "ασύρματος — two-way radio", "ανεμόμετρο": "ανεμόμετρο — anemometer"},
})

ITEMS.append({
 "id": "l198-news-pezoporos-taygetos", "title": "Βρέθηκε σώος ο πεζοπόρος που αγνοούνταν στον Ταΰγετο", "title_en": "Missing hiker found safe on Taygetos", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων του ραδιοφώνου.",
 "script": [
  L("Εκφωνήτρια", "f", "Σώος βρέθηκε σήμερα το πρωί ο σαραντάχρονος πεζοπόρος που αγνοούνταν από το Σάββατο στον Ταΰγετο. Τον εντόπισε ομάδα της ΕΜΑΚ με τη βοήθεια ενός σκύλου έρευνας, σε μια χαράδρα περίπου δύο χιλιόμετρα μακριά από το μονοπάτι.", "The forty-year-old hiker who had been missing on Taygetos since Saturday was found safe this morning. He was located by a team from the special disaster response unit with the help of a search dog, in a ravine about two kilometres from the path."),
  L("Εκφωνήτρια", "f", "Ο άντρας είχε χάσει τον δρόμο του όταν έπεσε πυκνή ομίχλη, και στη συνέχεια τραυματίστηκε ελαφρά στο πόδι. Πέρασε δύο νύχτες σε μια σπηλιά, όπου, όπως είπε στους διασώστες, επιβίωσε με ένα σακουλάκι ξηρούς καρπούς και το νερό ενός ρυακιού.", "The man had lost his way when thick fog fell, and then slightly injured his leg. He spent two nights in a cave, where, as he told the rescuers, he survived on a bag of nuts and water from a stream."),
  L("Εκφωνήτρια", "f", "Η Πυροσβεστική υπενθυμίζει στους πεζοπόρους να ενημερώνουν πάντα κάποιον για τη διαδρομή τους και να έχουν μαζί τους φορτισμένο κινητό, φακό και ζεστά ρούχα, ακόμα και για σύντομες πεζοπορίες.", "The Fire Service reminds hikers always to tell someone about their route and to carry a charged phone, a torch and warm clothes, even for short hikes."),
 ],
 "questions": [
  Q("Ποιος βοήθησε να εντοπιστεί ο πεζοπόρος;", ["Ένα ελικόπτερο", "Ένας σκύλος έρευνας", "Ένας βοσκός", "Ένας άλλος πεζοπόρος"], 1, "με τη βοήθεια ενός σκύλου έρευνας"),
  Q("Γιατί έχασε τον δρόμο του;", ["Γιατί νύχτωσε", "Γιατί έπεσε πυκνή ομίχλη", "Γιατί χάλασε το κινητό του", "Γιατί χιόνιζε"], 1, "όταν έπεσε πυκνή ομίχλη"),
  Q("Τι συμβουλεύει η Πυροσβεστική;", ["Να μην πηγαίνουν μόνοι", "Να ενημερώνουν κάποιον για τη διαδρομή και να έχουν μαζί τους κινητό, φακό και ζεστά ρούχα", "Να πεζοπορούν μόνο το καλοκαίρι", "Να μένουν πάντα στο μονοπάτι"], 1, "να ενημερώνουν πάντα κάποιον για τη διαδρομή τους"),
 ],
 "gloss": {"Σώος": "σώος — safe and sound", "αγνοούνταν": "αγνοούμαι — to be missing", "χαράδρα": "χαράδρα — ravine", "διασώστες": "διασώστης — rescuer", "ρυακιού": "ρυάκι — stream", "φακό": "φακός — torch, flashlight"},
})

ITEMS.append({
 "id": "l198-c1-mono-peina-kai-thymos", "title": "Γιατί η πείνα μάς κάνει νευρικούς;", "title_en": "Why does hunger make us irritable?", "type": "monologue", "level": "C1",
 "context_el": "Απόσπασμα από podcast εκλαΐκευσης της επιστήμης.",
 "script": [
  L("Παρουσιαστής", "m", "Οι αγγλόφωνοι έχουν μια λέξη γι' αυτό: «hangry», από το hungry και το angry, πεινασμένος και θυμωμένος. Η λέξη έχει μπει πια και σε μεγάλα λεξικά, αλλά το φαινόμενο το ξέρουμε όλοι: πλησιάζει η ώρα του φαγητού και ξαφνικά ο συνάδελφος που μασάει τσίχλα γίνεται ανυπόφορος.", "English speakers have a word for it: 'hangry', from hungry and angry. The word has even made it into major dictionaries, but we all know the phenomenon: mealtime approaches and suddenly the colleague chewing gum becomes unbearable."),
  L("Παρουσιαστής", "m", "Μια εξήγηση έχει να κάνει με τη γλυκόζη. Όταν η στάθμη της στο αίμα πέφτει, ο οργανισμός εκκρίνει ορμόνες του στρες, όπως η αδρεναλίνη και η κορτιζόλη, για να την ανεβάσει. Οι ίδιες ορμόνες όμως μας κάνουν πιο ευερέθιστους. Επιπλέον, ο εγκέφαλος καταναλώνει πολλή ενέργεια, και ο αυτοέλεγχος, η ικανότητα να καταπίνουμε μια απότομη απάντηση, φαίνεται να είναι από τα πρώτα πράγματα που υποφέρουν όταν τα αποθέματα λιγοστεύουν.", "One explanation has to do with glucose. When its level in the blood drops, the body releases stress hormones, such as adrenaline and cortisol, to raise it. But the same hormones make us more irritable. Moreover, the brain consumes a lot of energy, and self-control, the ability to swallow a sharp reply, seems to be among the first things to suffer when reserves run low."),
  L("Παρουσιαστής", "m", "Μια ευρωπαϊκή μελέτη, που παρακολούθησε εθελοντές στην καθημερινή τους ζωή για αρκετές εβδομάδες, βρήκε ότι όσο πιο πεινασμένοι δήλωναν, τόσο περισσότερο θυμό και εκνευρισμό ανέφεραν. Οι ερευνητές προσθέτουν όμως κάτι παρήγορο: όταν αναγνωρίζουμε ότι η κακή μας διάθεση οφείλεται στην πείνα, το αποτέλεσμα μειώνεται. Με άλλα λόγια, πριν από μια δύσκολη συζήτηση, ένα μήλο ίσως είναι το καλύτερο επιχείρημα.", "A European study, which followed volunteers in their daily lives for several weeks, found that the hungrier they said they were, the more anger and irritation they reported. But the researchers add something comforting: when we recognise that our bad mood is due to hunger, the effect diminishes. In other words, before a difficult conversation, an apple may be the best argument."),
 ],
 "questions": [
  Q("Τι κάνει ο οργανισμός όταν πέφτει η γλυκόζη στο αίμα;", ["Σταματά να καταναλώνει ενέργεια", "Εκκρίνει ορμόνες του στρες για να την ανεβάσει", "Μας κάνει να κοιμόμαστε", "Αυξάνει τον αυτοέλεγχο"], 1, "ο οργανισμός εκκρίνει ορμόνες του στρες"),
  Q("Ποια ικανότητα φαίνεται να υποφέρει από τις πρώτες όταν πεινάμε;", ["Η μνήμη", "Ο αυτοέλεγχος", "Η όραση", "Η ομιλία"], 1, "ο αυτοέλεγχος, η ικανότητα να καταπίνουμε μια απότομη απάντηση"),
  Q("Τι βρήκε η ευρωπαϊκή μελέτη;", ["Ότι η πείνα δεν επηρεάζει τη διάθεση", "Ότι όσο πιο πεινασμένοι δήλωναν, τόσο περισσότερο θυμό ανέφεραν", "Ότι οι άντρες θυμώνουν περισσότερο", "Ότι το μήλο δεν βοηθάει"], 1, "όσο πιο πεινασμένοι δήλωναν, τόσο περισσότερο θυμό και εκνευρισμό ανέφεραν"),
  Q("Τι μειώνει το αποτέλεσμα, σύμφωνα με τους ερευνητές;", ["Η γυμναστική", "Το να αναγνωρίζουμε ότι η κακή διάθεση οφείλεται στην πείνα", "Ο καφές", "Η τσίχλα"], 1, "όταν αναγνωρίζουμε ότι η κακή μας διάθεση οφείλεται στην πείνα"),
 ],
 "gloss": {"ανυπόφορος": "ανυπόφορος — unbearable", "στάθμη": "στάθμη — level", "εκκρίνει": "εκκρίνω — to secrete, release", "ευερέθιστους": "ευερέθιστος — irritable", "αυτοέλεγχος": "αυτοέλεγχος — self-control", "λιγοστεύουν": "λιγοστεύω — to run low, dwindle", "εκνευρισμό": "εκνευρισμός — irritation"},
})

ITEMS.append({
 "id": "l198-c1-int-akri-tis-glossas", "title": "Το φαινόμενο «στην άκρη της γλώσσας»", "title_en": "The tip-of-the-tongue phenomenon", "type": "interview", "level": "C1",
 "context_el": "Συνέντευξη με έναν ψυχογλωσσολόγο σε μια εκπομπή για τη γλώσσα.",
 "script": [
  L("Δημοσιογράφος", "f", "Όλοι το έχουμε ζήσει: ξέρουμε ότι ξέρουμε μια λέξη, αλλά δεν βγαίνει. Τι συμβαίνει εκείνη τη στιγμή;", "We've all experienced it: we know that we know a word, but it won't come out. What's happening at that moment?"),
  L("Ψυχογλωσσολόγος", "m", "Για να πούμε μια λέξη, ο εγκέφαλος κάνει δύο βήματα: πρώτα ανακαλεί τη σημασία και μετά τον ήχο, τη φωνολογική μορφή. Στο φαινόμενο «στην άκρη της γλώσσας» το πρώτο βήμα έχει πετύχει, ξέρουμε ακριβώς τι θέλουμε να πούμε, αλλά η σύνδεση με τον ήχο είναι προσωρινά αδύναμη. Γι' αυτό συχνά θυμόμαστε κομμάτια: το πρώτο γράμμα, πόσες συλλαβές έχει, πού τονίζεται.", "To say a word, the brain takes two steps: first it retrieves the meaning and then the sound, the phonological form. In the tip-of-the-tongue phenomenon the first step has succeeded, we know exactly what we want to say, but the link to the sound is temporarily weak. That's why we often remember fragments: the first letter, how many syllables it has, where the stress falls."),
  L("Δημοσιογράφος", "f", "Είναι σημάδι ότι η μνήμη μας χειροτερεύει;", "Is it a sign that our memory is getting worse?"),
  L("Ψυχογλωσσολόγος", "m", "Όχι απαραίτητα. Συμβαίνει σε όλες τις ηλικίες, σε πολλούς νέους ανθρώπους περίπου μία φορά την εβδομάδα. Είναι αλήθεια ότι γίνεται συχνότερο όσο μεγαλώνουμε, κυρίως με κύρια ονόματα, που έχουν λίγες συνδέσεις με άλλες λέξεις. Το «Βασίλης» δεν μας λέει τίποτα για το πρόσωπο. Το «αρτοποιός», αντίθετα, έχει μέσα του το «άρτος» και το «ποιώ», κι έτσι υπάρχουν περισσότεροι δρόμοι για να το βρούμε.", "Not necessarily. It happens at all ages, for many young people about once a week. It's true that it becomes more frequent as we get older, mainly with proper names, which have few links to other words. 'Vasilis' tells us nothing about the person. 'Baker', on the other hand, contains 'bread' and 'make', so there are more paths to find it."),
  L("Δημοσιογράφος", "f", "Και τι κάνουμε όταν μας συμβαίνει;", "And what do we do when it happens to us?"),
  L("Ψυχογλωσσολόγος", "m", "Το παράδοξο είναι ότι όσο περισσότερο προσπαθούμε, τόσο χειρότερα. Συχνά μια λάθος λέξη που μοιάζει «κολλάει» και μπλοκάρει τη σωστή. Η καλύτερη στρατηγική είναι να ασχοληθούμε με κάτι άλλο. Η λέξη τις περισσότερες φορές εμφανίζεται μόνη της, συνήθως τη στιγμή που δεν τη χρειαζόμαστε πια.", "The paradox is that the harder we try, the worse it gets. Often a wrong word that sounds similar 'sticks' and blocks the right one. The best strategy is to busy ourselves with something else. Most of the time the word turns up on its own, usually at the moment we no longer need it."),
 ],
 "questions": [
  Q("Ποιο βήμα έχει πετύχει όταν έχουμε μια λέξη «στην άκρη της γλώσσας»;", ["Η ανάκληση του ήχου", "Η ανάκληση της σημασίας", "Η προφορά", "Η γραφή"], 1, "το πρώτο βήμα έχει πετύχει, ξέρουμε ακριβώς τι θέλουμε να πούμε"),
  Q("Τι θυμόμαστε συχνά από τη λέξη;", ["Μόνο τη σημασία της στα αγγλικά", "Κομμάτια, όπως το πρώτο γράμμα ή τον αριθμό των συλλαβών", "Ολόκληρη τη λέξη αλλά όχι τη σημασία", "Τίποτα"], 1, "θυμόμαστε κομμάτια: το πρώτο γράμμα, πόσες συλλαβές έχει"),
  Q("Γιατί τα κύρια ονόματα ξεχνιούνται πιο εύκολα;", ["Γιατί είναι μακριά", "Γιατί έχουν λίγες συνδέσεις με άλλες λέξεις", "Γιατί τα ακούμε σπάνια", "Γιατί είναι ξένα"], 1, "κυρίως με κύρια ονόματα, που έχουν λίγες συνδέσεις με άλλες λέξεις"),
  Q("Ποια είναι η καλύτερη στρατηγική, κατά τον ψυχογλωσσολόγο;", ["Να προσπαθήσουμε πιο έντονα", "Να ψάξουμε στο λεξικό", "Να ασχοληθούμε με κάτι άλλο", "Να πούμε τη λέξη που μοιάζει"], 2, "Η καλύτερη στρατηγική είναι να ασχοληθούμε με κάτι άλλο"),
 ],
 "gloss": {"ψυχογλωσσολόγο": "ψυχογλωσσολόγος — psycholinguist", "ανακαλεί": "ανακαλώ — to retrieve, recall", "φωνολογική": "φωνολογικός — phonological", "συλλαβές": "συλλαβή — syllable", "τονίζεται": "τονίζομαι — to be stressed (of a syllable)", "παράδοξο": "παράδοξο — paradox", "μπλοκάρει": "μπλοκάρω — to block"},
})

rnd = random.Random(198)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-198.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
