# Source for library/listening/listening-180.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l180.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l180-ann-eisodos-festival", "title": "Ανακοίνωση στην είσοδο ενός μουσικού φεστιβάλ", "title_en": "An announcement at the entrance to a music festival", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα στην είσοδο ενός καλοκαιρινού μουσικού φεστιβάλ.",
 "script": [
  L("Εκφωνητής", "m", "Καλησπέρα σας και καλώς ήρθατε στο φεστιβάλ! Για να μπείτε πιο γρήγορα, έχετε έτοιμο το εισιτήριό σας στο κινητό και ανοιχτή την τσάντα σας για τον έλεγχο. Στην είσοδο θα σας δοθεί ένα βραχιόλι, το οποίο πρέπει να φοράτε σε όλη τη διάρκεια του φεστιβάλ. Αν το χάσετε, δεν μπορεί να αντικατασταθεί.", "Good evening and welcome to the festival! To get in faster, have your ticket ready on your phone and your bag open for the check. At the entrance you'll be given a wristband, which you must wear throughout the festival. If you lose it, it cannot be replaced."),
  L("Εκφωνητής", "m", "Μέσα στον χώρο δεν γίνονται δεκτά μετρητά. Μπορείτε να φορτώσετε χρήματα στο βραχιόλι σας στα περίπτερα με την πράσινη σημαία, και ό,τι περισσέψει θα σας επιστραφεί μετά το φεστιβάλ μέσω της εφαρμογής. Δεν επιτρέπονται γυάλινα μπουκάλια· μπορείτε όμως να φέρετε άδειο παγούρι και να το γεμίσετε δωρεάν στις βρύσες.", "Inside the grounds cash is not accepted. You can load money onto your wristband at the kiosks with the green flag, and whatever is left over will be refunded to you after the festival through the app. Glass bottles are not allowed; you can, however, bring an empty water bottle and fill it for free at the taps."),
  L("Εκφωνητής", "m", "Οι γονείς με μικρά παιδιά μπορούν να προμηθευτούν δωρεάν ωτοασπίδες από το σημείο πληροφοριών, δίπλα στη σκηνή του σταθμού πρώτων βοηθειών. Καλή διασκέδαση!", "Parents with small children can get free ear defenders from the information point, next to the first-aid station tent. Have fun!"),
 ],
 "questions": [
  Q("Τι πρέπει να κάνει κανείς με το βραχιόλι;", ["Να το επιστρέψει στην έξοδο", "Να το φοράει σε όλη τη διάρκεια του φεστιβάλ", "Να το δείχνει μόνο στην είσοδο", "Να το αλλάζει κάθε μέρα"], 1, "πρέπει να φοράτε σε όλη τη διάρκεια του φεστιβάλ"),
  Q("Πώς πληρώνει κανείς μέσα στον χώρο του φεστιβάλ;", ["Με μετρητά", "Μόνο με πιστωτική κάρτα", "Με χρήματα φορτωμένα στο βραχιόλι", "Με κουπόνια από την είσοδο"], 2, "Μπορείτε να φορτώσετε χρήματα στο βραχιόλι σας"),
  Q("Τι μπορούν να προμηθευτούν δωρεάν οι γονείς με μικρά παιδιά;", ["Ωτοασπίδες", "Νερό", "Καπέλα", "Εισιτήρια για τα παιδιά"], 0, "δωρεάν ωτοασπίδες από το σημείο πληροφοριών"),
 ],
 "gloss": {"βραχιόλι": "βραχιόλι — wristband, bracelet", "αντικατασταθεί": "αντικαθίσταμαι — to be replaced", "δεν γίνονται δεκτά": "γίνομαι δεκτός — to be accepted", "μετρητά": "μετρητά — cash", "φορτώσετε": "φορτώνω — to load, top up", "περισσέψει": "περισσεύω — to be left over", "εφαρμογής": "εφαρμογή — app", "παγούρι": "παγούρι — water bottle, flask", "προμηθευτούν": "προμηθεύομαι — to get, obtain", "ωτοασπίδες": "ωτοασπίδα — ear defender, earplug", "πρώτων βοηθειών": "πρώτες βοήθειες — first aid"},
})

ITEMS.append({
 "id": "l180-int-myrmigkologos", "title": "Η ερευνήτρια των μυρμηγκιών", "title_en": "The ant researcher", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια βιολόγο που μελετά τα μυρμήγκια.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι περισσότεροι άνθρωποι θέλουν να διώξουν τα μυρμήγκια από την κουζίνα τους. Εσείς γιατί αφιερώσατε τη ζωή σας σε αυτά;", "Most people want to get ants out of their kitchen. Why did you devote your life to them?"),
  L("Βιολόγος", "f", "Γιατί είναι ένας ολόκληρος κόσμος κάτω από τα πόδια μας. Μια φωλιά μπορεί να έχει εκατοντάδες χιλιάδες μέλη, και κανένα δεν δίνει εντολές. Η βασίλισσα δεν «βασιλεύει»· απλώς γεννά αυγά. Κι όμως, η φωλιά λειτουργεί σαν ένας οργανισμός: κάποια μυρμήγκια μαζεύουν τροφή, άλλα φροντίζουν τις προνύμφες, άλλα φυλάνε την είσοδο.", "Because they're a whole world beneath our feet. A nest can have hundreds of thousands of members, and none of them gives orders. The queen doesn't 'reign'; she just lays eggs. And yet, the nest works like one organism: some ants gather food, others look after the larvae, others guard the entrance."),
  L("Δημοσιογράφος", "m", "Πώς συνεννοούνται χωρίς αρχηγό;", "How do they coordinate without a leader?"),
  L("Βιολόγος", "f", "Κυρίως με χημικές ουσίες, τις φερομόνες. Όταν ένα μυρμήγκι βρει τροφή, γυρνώντας στη φωλιά αφήνει ένα ίχνος στο έδαφος. Τα άλλα το ακολουθούν και, αν βρουν κι αυτά τροφή, το ενισχύουν. Έτσι, ο πιο σύντομος δρόμος γίνεται σιγά σιγά ο πιο «μυρωδάτος». Μηχανικοί έχουν δανειστεί αυτή την ιδέα για να σχεδιάζουν δίκτυα και δρομολόγια.", "Mainly with chemical substances, pheromones. When an ant finds food, on its way back to the nest it leaves a trail on the ground. The others follow it and, if they find food too, they reinforce it. So the shortest route gradually becomes the most 'fragrant'. Engineers have borrowed this idea to design networks and routes."),
  L("Δημοσιογράφος", "m", "Και τι να κάνουμε με τα μυρμήγκια της κουζίνας;", "And what should we do about the ants in the kitchen?"),
  L("Βιολόγος", "f", "Να σκουπίσουμε τα ψίχουλα και να σβήσουμε το ίχνος με λίγο ξίδι. Χωρίς τροφή και χωρίς «χάρτη», θα πάνε να ψάξουν αλλού. Δεν χρειάζεται να τα σκοτώσουμε· στον κήπο κάνουν πολύτιμη δουλειά, αερίζουν το χώμα και μεταφέρουν σπόρους.", "Wipe up the crumbs and erase the trail with a little vinegar. With no food and no 'map', they'll go and look elsewhere. There's no need to kill them; in the garden they do valuable work, aerating the soil and carrying seeds."),
 ],
 "questions": [
  Q("Τι κάνει, κατά τη βιολόγο, η βασίλισσα;", ["Δίνει εντολές σε όλη τη φωλιά", "Απλώς γεννά αυγά", "Φυλάει την είσοδο", "Μαζεύει τροφή"], 1, "Η βασίλισσα δεν «βασιλεύει»· απλώς γεννά αυγά"),
  Q("Πώς γίνεται ο πιο σύντομος δρόμος ο πιο «μυρωδάτος»;", ["Τον σημαδεύει η βασίλισσα", "Τον βρίσκουν με την όραση", "Περισσότερα μυρμήγκια τον ακολουθούν και ενισχύουν το ίχνος", "Τον ανοίγουν τα φρουρά μυρμήγκια"], 2, "Τα άλλα το ακολουθούν και, αν βρουν κι αυτά τροφή, το ενισχύουν"),
  Q("Τι προτείνει για τα μυρμήγκια της κουζίνας;", ["Να σκουπίσουμε τα ψίχουλα και να σβήσουμε το ίχνος με ξίδι", "Να χρησιμοποιήσουμε εντομοκτόνο", "Να αφήσουμε ζάχαρη έξω από το σπίτι", "Να κλείσουμε όλα τα παράθυρα"], 0, "Να σκουπίσουμε τα ψίχουλα και να σβήσουμε το ίχνος με λίγο ξίδι"),
 ],
 "gloss": {"μυρμήγκια": "μυρμήγκι — ant", "αφιερώσατε": "αφιερώνω — to devote", "φωλιά": "φωλιά — nest", "βασίλισσα": "βασίλισσα — queen", "βασιλεύει": "βασιλεύω — to reign", "προνύμφες": "προνύμφη — larva", "συνεννοούνται": "συνεννοούμαι — to communicate, coordinate", "φερομόνες": "φερομόνη — pheromone", "ίχνος": "ίχνος — trail, trace", "ενισχύουν": "ενισχύω — to reinforce", "ψίχουλα": "ψίχουλο — crumb", "αερίζουν": "αερίζω — to aerate"},
})

ITEMS.append({
 "id": "l180-int-kataskevastis-podilaton", "title": "Ποδήλατα φτιαγμένα στο χέρι", "title_en": "Handmade bicycles", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν τεχνίτη που κατασκευάζει χειροποίητους σκελετούς ποδηλάτων σε ένα εργαστήριο στη Θεσσαλονίκη.",
 "script": [
  L("Δημοσιογράφος", "f", "Γιατί να πληρώσει κανείς για ένα ποδήλατο φτιαγμένο στο χέρι, όταν μπορεί να αγοράσει ένα έτοιμο;", "Why would anyone pay for a handmade bicycle when they can buy a ready-made one?"),
  L("Τεχνίτης", "m", "Γιατί κάθε σώμα είναι διαφορετικό. Τα έτοιμα ποδήλατα βγαίνουν σε πέντε-έξι μεγέθη. Εγώ παίρνω περίπου είκοσι μετρήσεις από τον πελάτη: το μήκος των ποδιών, των χεριών, τη γωνία της πλάτης του. Έρχονται σε μένα συχνά άνθρωποι που πονούσαν στη μέση ή στους καρπούς και νόμιζαν ότι φταίει η ηλικία τους. Τελικά έφταιγε το ποδήλατο.", "Because every body is different. Ready-made bikes come in five or six sizes. I take about twenty measurements from the customer: the length of the legs, the arms, the angle of the back. People often come to me who had pain in the lower back or wrists and thought their age was to blame. In the end it was the bike."),
  L("Δημοσιογράφος", "f", "Από τι υλικό φτιάχνετε τους σκελετούς;", "What material do you make the frames from?"),
  L("Τεχνίτης", "m", "Κυρίως από ατσάλι. Είναι πιο βαρύ από τα σύγχρονα υλικά, αλλά απορροφά καλύτερα τους κραδασμούς και επισκευάζεται εύκολα. Αν σπάσει ένα αλουμινένιο ή ένα καρμπόν, συνήθως πετιέται. Ένας ατσάλινος σκελετός, αν τον προσέχεις, μπορεί να κρατήσει μια ζωή. Κάθε σκελετός μού παίρνει περίπου δύο εβδομάδες.", "Mainly from steel. It's heavier than modern materials, but it absorbs vibrations better and is easily repaired. If an aluminium or carbon one breaks, it's usually thrown away. A steel frame, if you look after it, can last a lifetime. Each frame takes me about two weeks."),
  L("Δημοσιογράφος", "f", "Ποιος είναι ο πιο ασυνήθιστος πελάτης σας;", "Who is your most unusual customer?"),
  L("Τεχνίτης", "m", "Ένας κύριος ογδόντα δύο χρονών, που ήθελε ένα ποδήλατο για να πάει από τη Θεσσαλονίκη στο χωριό του στη Χαλκιδική, όπως έκανε όταν ήταν δεκαοχτώ. Το έκανε, σε τρεις μέρες. Μου έστειλε φωτογραφία από την πλατεία του χωριού.", "A gentleman of eighty-two, who wanted a bike to go from Thessaloniki to his village in Halkidiki, as he did when he was eighteen. He did it, in three days. He sent me a photo from the village square."),
 ],
 "questions": [
  Q("Γιατί, κατά τον τεχνίτη, χρειάζεται ένα ποδήλατο φτιαγμένο στο χέρι;", ["Γιατί είναι πιο ελαφρύ", "Γιατί κάθε σώμα είναι διαφορετικό", "Γιατί είναι φθηνότερο", "Γιατί είναι πιο γρήγορο"], 1, "Γιατί κάθε σώμα είναι διαφορετικό"),
  Q("Ποιο πλεονέκτημα του ατσαλιού αναφέρει;", ["Είναι το ελαφρύτερο υλικό", "Δεν σκουριάζει ποτέ", "Απορροφά καλύτερα τους κραδασμούς και επισκευάζεται εύκολα", "Είναι το φθηνότερο"], 2, "απορροφά καλύτερα τους κραδασμούς και επισκευάζεται εύκολα"),
  Q("Τι έκανε ο ογδοντάχρονος πελάτης;", ["Πήγε με το ποδήλατο στο χωριό του στη Χαλκιδική", "Έκανε τον γύρο της Ελλάδας", "Χάρισε το ποδήλατο στον εγγονό του", "Έλαβε μέρος σε αγώνα"], 0, "ήθελε ένα ποδήλατο για να πάει από τη Θεσσαλονίκη στο χωριό του στη Χαλκιδική"),
 ],
 "gloss": {"χειροποίητους": "χειροποίητος — handmade", "σκελετούς": "σκελετός — frame (of a bicycle)", "μετρήσεις": "μέτρηση — measurement", "γωνία": "γωνία — angle", "μέση": "μέση — lower back, waist", "καρπούς": "καρπός — wrist", "ατσάλι": "ατσάλι — steel", "απορροφά": "απορροφώ — to absorb", "κραδασμούς": "κραδασμός — vibration", "αλουμινένιο": "αλουμινένιος — aluminium (adj.)", "καρμπόν": "καρμπόν — carbon (fibre)", "ασυνήθιστος": "ασυνήθιστος — unusual"},
})

ITEMS.append({
 "id": "l180-vm-politikos-gamos", "title": "Μήνυμα από το δημαρχείο για τον γάμο", "title_en": "A message from the town hall about the wedding", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από την υπάλληλο του δημαρχείου που ετοιμάζει τον πολιτικό σας γάμο.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, από το γραφείο πολιτικών γάμων του δημαρχείου σας παίρνω, η κυρία Ζαχαρίου. Είδα ότι μας στείλατε τα δικαιολογητικά, αλλά λείπει ακόμα η άδεια γάμου, ή όπως αλλιώς τη λέμε, η βεβαίωση ότι δεν υπάρχει κώλυμα. Χωρίς αυτήν δεν μπορούμε να κλειδώσουμε την ημερομηνία.", "Good morning, I'm calling from the civil weddings office at the town hall, it's Mrs Zachariou. I saw that you sent us the documents, but the marriage licence is still missing, or as we also call it, the certificate that there is no impediment. Without it we can't lock in the date."),
  L("Υπάλληλος", "f", "Για την ημερομηνία που ζητήσατε, το Σάββατο δώδεκα Ιουνίου, υπάρχει ακόμα διαθέσιμη ώρα στις έντεκα ή στις δώδεκα και μισή. Η αίθουσα τελετών χωράει μέχρι πενήντα άτομα όρθια· αν θα είστε περισσότεροι, μπορούμε να κάνουμε την τελετή στον κήπο του δημαρχείου, αλλά τότε υπάρχει μια μικρή επιπλέον χρέωση.", "For the date you asked for, Saturday the twelfth of June, there is still a free slot at eleven or at half past twelve. The ceremony room holds up to fifty people standing; if there will be more of you, we can hold the ceremony in the town hall garden, but then there is a small extra charge."),
  L("Υπάλληλος", "f", "Να σας θυμίσω ότι χρειάζονται δύο μάρτυρες, ενήλικες, με την αστυνομική τους ταυτότητα. Και οι βέρες δεν είναι υποχρεωτικές, αν και τις φέρνουν σχεδόν όλοι. Πάρτε με όταν μπορείτε για να μου πείτε ποια ώρα προτιμάτε. Και συγχαρητήρια!", "Let me remind you that you need two witnesses, adults, with their identity cards. And wedding rings aren't compulsory, although almost everyone brings them. Call me when you can to tell me which time you prefer. And congratulations!"),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί ακόμα να οριστεί η ημερομηνία του γάμου;", ["Γιατί η αίθουσα είναι κλειστή τον Ιούνιο", "Γιατί λείπει η άδεια γάμου", "Γιατί δεν έχει πληρωθεί το παράβολο", "Γιατί οι μάρτυρες δεν έχουν ταυτότητα"], 1, "λείπει ακόμα η άδεια γάμου"),
  Q("Τι συμβαίνει αν οι καλεσμένοι είναι πάνω από πενήντα;", ["Η τελετή γίνεται σε άλλη μέρα", "Πρέπει να μείνουν κάποιοι έξω", "Η τελετή μπορεί να γίνει στον κήπο με μικρή επιπλέον χρέωση", "Χρειάζεται δεύτερος δήμαρχος"], 2, "μπορούμε να κάνουμε την τελετή στον κήπο του δημαρχείου, αλλά τότε υπάρχει μια μικρή επιπλέον χρέωση"),
  Q("Τι ισχύει για τις βέρες, σύμφωνα με την υπάλληλο;", ["Δεν είναι υποχρεωτικές, αλλά τις φέρνουν σχεδόν όλοι", "Πρέπει να τις κρατούν οι μάρτυρες", "Τις παρέχει το δημαρχείο", "Απαγορεύονται στην αίθουσα"], 0, "οι βέρες δεν είναι υποχρεωτικές, αν και τις φέρνουν σχεδόν όλοι"),
 ],
 "gloss": {"πολιτικών γάμων": "πολιτικός γάμος — civil wedding", "δικαιολογητικά": "δικαιολογητικά — supporting documents", "άδεια γάμου": "άδεια γάμου — marriage licence", "κώλυμα": "κώλυμα — impediment, obstacle", "κλειδώσουμε": "κλειδώνω — to lock (in)", "αίθουσα τελετών": "αίθουσα τελετών — ceremony room", "επιπλέον χρέωση": "επιπλέον χρέωση — extra charge", "μάρτυρες": "μάρτυρας — witness", "ενήλικες": "ενήλικας — adult", "βέρες": "βέρα — wedding ring", "υποχρεωτικές": "υποχρεωτικός — compulsory"},
})

ITEMS.append({
 "id": "l180-mon-egnatia-me-ta-podia", "title": "Περπατώντας την Εγνατία Οδό", "title_en": "Walking the Via Egnatia", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια εκπαιδευτικό να μιλάει σε μια ραδιοφωνική εκπομπή για τις τρεις εβδομάδες που περπάτησε κατά μήκος της αρχαίας Εγνατίας Οδού.",
 "script": [
  L("Εκπαιδευτικός", "f", "Οι περισσότεροι, όταν ακούνε «Εγνατία», σκέφτονται τον σύγχρονο αυτοκινητόδρομο. Εγώ σκεφτόμουν τον αρχαίο δρόμο που έφτιαξαν οι Ρωμαίοι τον δεύτερο αιώνα π.Χ., για να ενώσουν την Αδριατική με το Βυζάντιο. Από αυτόν περνούσαν στρατιώτες, έμποροι, προσκυνητές. Πέρσι το καλοκαίρι αποφάσισα να περπατήσω ένα κομμάτι του, από τη Φλώρινα ως την Καβάλα.", "When most people hear 'Egnatia', they think of the modern motorway. I was thinking of the ancient road the Romans built in the second century BC, to connect the Adriatic with Byzantium. Soldiers, merchants and pilgrims passed along it. Last summer I decided to walk a section of it, from Florina to Kavala."),
  L("Εκπαιδευτικός", "f", "Σε λίγα σημεία σώζονται ακόμα οι μεγάλες πλάκες του αρχαίου δρόμου, με αυλάκια από τις ρόδες των αμαξών. Τις περισσότερες φορές όμως περπατούσα σε χωματόδρομους και σε μονοπάτια, ακολουθώντας έναν χάρτη και πολλές φορές τις οδηγίες των ντόπιων. Κοιμόμουν σε μικρά ξενοδοχεία και, δύο φορές, σε σπίτια ανθρώπων που με είδαν κουρασμένη και μου πρόσφεραν ένα κρεβάτι.", "In a few places the large slabs of the ancient road still survive, with grooves from the wheels of carts. Most of the time, though, I walked on dirt roads and paths, following a map and often the directions of locals. I slept in small hotels and, twice, in the homes of people who saw I was tired and offered me a bed."),
  L("Εκπαιδευτικός", "f", "Αυτό που θα θυμάμαι δεν είναι οι αρχαιότητες, αλλά ο ρυθμός. Με το αυτοκίνητο, η απόσταση από τη Θεσσαλονίκη ως την Καβάλα είναι δυόμισι ώρες. Με τα πόδια μού πήρε έξι μέρες. Μέσα σε αυτές τις μέρες κατάλαβα πόσο μεγάλη είναι στην πραγματικότητα η χώρα μας.", "What I'll remember isn't the antiquities, but the rhythm. By car, the distance from Thessaloniki to Kavala is two and a half hours. On foot it took me six days. During those days I understood how big our country really is."),
 ],
 "questions": [
  Q("Γιατί έφτιαξαν οι Ρωμαίοι την Εγνατία Οδό;", ["Για να ενώσουν την Αθήνα με τη Θεσσαλονίκη", "Για να ενώσουν την Αδριατική με το Βυζάντιο", "Για τους προσκυνητές του Αγίου Όρους", "Για να μεταφέρουν μάρμαρα"], 1, "για να ενώσουν την Αδριατική με το Βυζάντιο"),
  Q("Τι σώζεται σε λίγα σημεία του αρχαίου δρόμου;", ["Ρωμαϊκά ορόσημα", "Παλιά πανδοχεία", "Μεγάλες πλάκες με αυλάκια από τις ρόδες των αμαξών", "Γέφυρες"], 2, "σώζονται ακόμα οι μεγάλες πλάκες του αρχαίου δρόμου, με αυλάκια από τις ρόδες των αμαξών"),
  Q("Τι θα θυμάται περισσότερο η εκπαιδευτικός;", ["Τον ρυθμό του περπατήματος", "Τις αρχαιότητες", "Τα ξενοδοχεία", "Το φαγητό"], 0, "Αυτό που θα θυμάμαι δεν είναι οι αρχαιότητες, αλλά ο ρυθμός"),
 ],
 "gloss": {"κατά μήκος": "κατά μήκος — along", "αυτοκινητόδρομο": "αυτοκινητόδρομος — motorway", "Αδριατική": "Αδριατική — the Adriatic", "προσκυνητές": "προσκυνητής — pilgrim", "πλάκες": "πλάκα — slab", "ρόδες": "ρόδα — wheel", "αμαξών": "άμαξα — cart, carriage", "χωματόδρομους": "χωματόδρομος — dirt road", "ντόπιων": "ντόπιος — local", "αρχαιότητες": "αρχαιότητα — antiquity, ancient monument", "ρυθμός": "ρυθμός — rhythm, pace"},
})

ITEMS.append({
 "id": "l180-dia-kynigi-thisavrou-me-gps", "title": "Κυνήγι θησαυρού με το κινητό", "title_en": "A treasure hunt with a phone", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλους να συζητούν για ένα παιχνίδι στο οποίο ψάχνει κανείς μικρά κρυμμένα κουτιά με τη βοήθεια του GPS.",
 "script": [
  L("Λευτέρης", "m", "Τι κάνεις εκεί σκυμμένη πίσω από το παγκάκι; Έχασες κάτι;", "What are you doing bent down behind the bench? Did you lose something?"),
  L("Ρένα", "f", "Όχι, ψάχνω κάτι! Είναι ένα παιχνίδι. Άνθρωποι σε όλο τον κόσμο κρύβουν μικρά κουτάκια και ανεβάζουν τις συντεταγμένες σε μια εφαρμογή. Εσύ πηγαίνεις στο σημείο και ψάχνεις. Μέσα υπάρχει ένα μικρό τετράδιο, όπου γράφεις το όνομά σου και την ημερομηνία.", "No, I'm looking for something! It's a game. People all over the world hide little boxes and upload the coordinates to an app. You go to the spot and search. Inside there's a little notebook, where you write your name and the date."),
  L("Λευτέρης", "m", "Και τι κερδίζεις; Υπάρχει κάτι πολύτιμο μέσα;", "And what do you win? Is there something valuable inside?"),
  L("Ρένα", "f", "Τίποτα πολύτιμο. Κάποιες φορές μικρά μπιχλιμπίδια: ένα μπρελόκ, ένα κοχύλι. Ο κανόνας είναι, αν πάρεις κάτι, να αφήσεις κάτι ίσης αξίας. Το ωραίο είναι ότι σε πάει σε μέρη που αλλιώς δεν θα πήγαινες ποτέ. Χάρη σε αυτό ανακάλυψα ένα βυζαντινό εκκλησάκι πέντε λεπτά από το σπίτι μου.", "Nothing valuable. Sometimes little trinkets: a keyring, a shell. The rule is, if you take something, you leave something of equal value. The nice thing is that it takes you to places you'd never otherwise go. Thanks to it I discovered a Byzantine chapel five minutes from my house."),
  L("Λευτέρης", "m", "Και δεν σε κοιτάζουν περίεργα οι περαστικοί;", "And don't passers-by look at you strangely?"),
  L("Ρένα", "f", "Αυτό είναι το πιο δύσκολο! Πρέπει να ψάχνεις χωρίς να σε προσέχουν, για να μη βρει το κουτί κάποιος που δεν ξέρει το παιχνίδι και το πετάξει. Γι' αυτό, αν σε ρωτήσει κανείς, εγώ απλώς δένω το κορδόνι μου. Έλα, βοήθα με. Η εφαρμογή λέει ότι είναι μαγνητικό. Ψάξε κάτω από τα μεταλλικά πόδια.", "That's the hardest part! You have to search without being noticed, so that someone who doesn't know the game doesn't find the box and throw it away. So, if anyone asks you, I'm just tying my shoelace. Come on, help me. The app says it's magnetic. Look under the metal legs."),
 ],
 "questions": [
  Q("Τι βρίσκει κανείς πάντα μέσα στο κουτάκι;", ["Χρήματα", "Ένα μικρό τετράδιο", "Έναν χάρτη", "Ένα κλειδί"], 1, "Μέσα υπάρχει ένα μικρό τετράδιο"),
  Q("Ποιος είναι ο κανόνας για τα μπιχλιμπίδια;", ["Τα παίρνεις όλα", "Δεν τα αγγίζεις ποτέ", "Αν πάρεις κάτι, αφήνεις κάτι ίσης αξίας", "Τα στέλνεις σε αυτόν που έκρυψε το κουτί"], 2, "αν πάρεις κάτι, να αφήσεις κάτι ίσης αξίας"),
  Q("Γιατί πρέπει να ψάχνει κανείς χωρίς να τον προσέχουν;", ["Για να μη βρει το κουτί κάποιος που δεν ξέρει το παιχνίδι και το πετάξει", "Γιατί απαγορεύεται από τον δήμο", "Για να μην τον ακολουθήσουν άλλοι παίκτες", "Γιατί ντρέπεται"], 0, "για να μη βρει το κουτί κάποιος που δεν ξέρει το παιχνίδι και το πετάξει"),
 ],
 "gloss": {"σκυμμένη": "σκυμμένος — bent down", "κουτάκια": "κουτάκι — little box", "συντεταγμένες": "συντεταγμένη — coordinate", "εφαρμογή": "εφαρμογή — app", "μπιχλιμπίδια": "μπιχλιμπίδι — trinket", "μπρελόκ": "μπρελόκ — keyring", "κοχύλι": "κοχύλι — shell", "ίσης αξίας": "ίσης αξίας — of equal value", "εκκλησάκι": "εκκλησάκι — small church, chapel", "περαστικοί": "περαστικός — passer-by", "κορδόνι": "κορδόνι — shoelace", "μαγνητικό": "μαγνητικός — magnetic"},
})

ITEMS.append({
 "id": "l180-news-vivliothiki-se-stathmo-metro", "title": "Μια βιβλιοθήκη μέσα σε σταθμό του μετρό", "title_en": "A library inside a metro station", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση σε έναν ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνήτρια", "f", "Σε έναν από τους πιο πολυσύχναστους σταθμούς του μετρό της πόλης άνοιξε χθες μια μικρή δανειστική βιβλιοθήκη. Βρίσκεται στον χώρο πριν από τις ακυρωτικές μηχανές, σε ένα παλιό κατάστημα που έμενε κλειστό για χρόνια, και θα λειτουργεί καθημερινά από τις επτά το πρωί ως τις δέκα το βράδυ.", "In one of the busiest stations of the city's metro a small lending library opened yesterday. It is located in the area before the ticket validators, in an old shop that had been closed for years, and will operate daily from seven in the morning to ten at night."),
  L("Εκφωνήτρια", "f", "Οι επιβάτες μπορούν να δανειστούν έως δύο βιβλία με την κάρτα απεριορίστων διαδρομών τους, χωρίς άλλη εγγραφή, και να τα επιστρέψουν σε οποιονδήποτε από τους πέντε σταθμούς που θα αποκτήσουν παρόμοιο σημείο μέσα στη χρονιά. Τα περισσότερα βιβλία είναι σύντομα μυθιστορήματα, διηγήματα και ποίηση, επιλεγμένα ώστε να διαβάζονται σε λίγες διαδρομές.", "Passengers can borrow up to two books with their unlimited travel card, without further registration, and return them at any of the five stations that will get a similar point during the year. Most of the books are short novels, short stories and poetry, chosen so that they can be read in a few journeys."),
  L("Εκφωνήτρια", "f", "Τα βιβλία προέρχονται από δωρεές εκδοτών και πολιτών. Σύμφωνα με τους υπεύθυνους, μόνο την πρώτη μέρα δανείστηκαν πάνω από τριακόσια βιβλία, ενώ αρκετοί επιβάτες άφησαν και δικά τους βιβλία στο ειδικό ράφι δωρεών.", "The books come from donations by publishers and citizens. According to those in charge, on the first day alone over three hundred books were borrowed, while several passengers also left their own books on the special donations shelf."),
 ],
 "questions": [
  Q("Πού ακριβώς βρίσκεται η βιβλιοθήκη;", ["Μέσα σε ένα βαγόνι", "Σε ένα παλιό κατάστημα πριν από τις ακυρωτικές μηχανές", "Στην αποβάθρα", "Έξω από τον σταθμό"], 1, "στον χώρο πριν από τις ακυρωτικές μηχανές, σε ένα παλιό κατάστημα"),
  Q("Τι χρειάζεται για να δανειστεί κανείς βιβλία;", ["Κάρτα δημοτικής βιβλιοθήκης", "Ταυτότητα", "Την κάρτα απεριορίστων διαδρομών του", "Ένα μικρό αντίτιμο"], 2, "με την κάρτα απεριορίστων διαδρομών τους, χωρίς άλλη εγγραφή"),
  Q("Από πού προέρχονται τα βιβλία;", ["Από δωρεές εκδοτών και πολιτών", "Από τη δημοτική βιβλιοθήκη", "Από αγορές του δήμου", "Από σχολεία"], 0, "Τα βιβλία προέρχονται από δωρεές εκδοτών και πολιτών"),
 ],
 "gloss": {"πολυσύχναστους": "πολυσύχναστος — busy, crowded", "δανειστική βιβλιοθήκη": "δανειστική βιβλιοθήκη — lending library", "ακυρωτικές μηχανές": "ακυρωτικό μηχάνημα — ticket validator", "δανειστούν": "δανείζομαι — to borrow", "κάρτα απεριορίστων διαδρομών": "κάρτα απεριορίστων διαδρομών — unlimited travel card", "εγγραφή": "εγγραφή — registration", "οποιονδήποτε": "οποιοσδήποτε — any", "διηγήματα": "διήγημα — short story", "διαδρομές": "διαδρομή — journey, route", "δωρεές": "δωρεά — donation", "εκδοτών": "εκδότης — publisher"},
})

ITEMS.append({
 "id": "l180-rep-giagiades-sto-diadiktyo", "title": "Οι γιαγιάδες που μαγειρεύουν στο διαδίκτυο", "title_en": "The grandmothers who cook online", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ραδιοφωνικό ρεπορτάζ για ένα κανάλι μαγειρικής στο διαδίκτυο με πρωταγωνίστριες τρεις γιαγιάδες από ένα χωριό της Ηπείρου.",
 "script": [
  L("Ρεπόρτερ", "m", "Στην κουζίνα ενός πέτρινου σπιτιού, τρεις γυναίκες ανοίγουν φύλλο για πίτα, ενώ ένα κινητό, στερεωμένο πάνω σε μια στοίβα από πιάτα, τις βιντεοσκοπεί. Η κυρία Σοφία είναι ογδόντα ενός, η κυρία Μαρίκα εβδομήντα εννιά και η κυρία Φρόσω ογδόντα τεσσάρων. Το κανάλι τους έχει σήμερα πάνω από διακόσιες χιλιάδες συνδρομητές.", "In the kitchen of a stone house, three women are rolling out pastry for a pie, while a phone, propped up on a stack of plates, films them. Mrs Sofia is eighty-one, Mrs Marika seventy-nine and Mrs Froso eighty-four. Their channel today has over two hundred thousand subscribers."),
  L("Εγγονή", "f", "Την ιδέα την είχα εγώ, στην καραντίνα, όταν δεν μπορούσα να πάω στο χωριό. Ήθελα να μάθω τη συνταγή της γιαγιάς για την κασιόπιτα και της ζήτησα να με πάρει βιντεοκλήση. Οι φίλες της ήρθαν να βοηθήσουν, άρχισαν να μαλώνουν για το πόσο βούτυρο θέλει, και το βίντεο έγινε απίστευτα αστείο. Το ανέβασα, και μέσα σε μια εβδομάδα το είχαν δει εκατό χιλιάδες άνθρωποι.", "The idea was mine, during the lockdown, when I couldn't go to the village. I wanted to learn grandma's recipe for cheese pie and asked her to video-call me. Her friends came to help, started arguing about how much butter it needs, and the video became incredibly funny. I uploaded it, and within a week a hundred thousand people had seen it."),
  L("Ρεπόρτερ", "m", "Οι γιαγιάδες δεν μετράνε τίποτα με ζυγαριά· «όσο πάρει», λένε, και οι συνδρομητές γράφουν στα σχόλια προσπαθώντας να μαντέψουν τις ποσότητες. Πολλά μηνύματα έρχονται από Έλληνες του εξωτερικού, που λένε ότι μαγειρεύοντας μαζί τους νιώθουν πάλι στο σπίτι της δικής τους γιαγιάς.", "The grandmothers don't measure anything with scales; 'as much as it takes', they say, and the subscribers write in the comments trying to guess the quantities. Many messages come from Greeks abroad, who say that cooking along with them they feel back at their own grandmother's house."),
 ],
 "questions": [
  Q("Πόσους συνδρομητές έχει σήμερα το κανάλι;", ["Εκατό χιλιάδες", "Πάνω από διακόσιες χιλιάδες", "Τρεις χιλιάδες", "Ένα εκατομμύριο"], 1, "Το κανάλι τους έχει σήμερα πάνω από διακόσιες χιλιάδες συνδρομητές"),
  Q("Γιατί έγινε τόσο αστείο το πρώτο βίντεο;", ["Γιατί κάηκε η πίτα", "Γιατί η γιαγιά δεν ήξερε να χρησιμοποιεί το κινητό", "Γιατί οι φίλες της γιαγιάς άρχισαν να μαλώνουν για το βούτυρο", "Γιατί μπήκε η γάτα στην κουζίνα"], 2, "άρχισαν να μαλώνουν για το πόσο βούτυρο θέλει"),
  Q("Τι λένε πολλοί Έλληνες του εξωτερικού;", ["Ότι νιώθουν πάλι στο σπίτι της γιαγιάς τους", "Ότι θέλουν να επισκεφτούν το χωριό", "Ότι δεν βρίσκουν τα υλικά", "Ότι οι συνταγές είναι δύσκολες"], 0, "νιώθουν πάλι στο σπίτι της δικής τους γιαγιάς"),
 ],
 "gloss": {"κανάλι": "κανάλι — channel", "πρωταγωνίστριες": "πρωταγωνίστρια — star, protagonist (f.)", "ανοίγουν φύλλο": "ανοίγω φύλλο — to roll out pastry", "στερεωμένο": "στερεωμένος — propped up, fixed", "στοίβα": "στοίβα — stack, pile", "βιντεοσκοπεί": "βιντεοσκοπώ — to film", "συνδρομητές": "συνδρομητής — subscriber", "καραντίνα": "καραντίνα — quarantine, lockdown", "κασιόπιτα": "κασιόπιτα — cheese pie (Epirus)", "βιντεοκλήση": "βιντεοκλήση — video call", "όσο πάρει": "όσο πάρει — as much as it takes", "μαντέψουν": "μαντεύω — to guess"},
})

ITEMS.append({
 "id": "l180-c1-giati-den-piannoume-tis-myges", "title": "Γιατί είναι τόσο δύσκολο να πιάσεις μια μύγα", "title_en": "Why it's so hard to swat a fly", "type": "interview", "level": "C1",
 "context_el": "Ακούτε έναν εντομολόγο να εξηγεί σε μια εκπομπή γιατί οι μύγες ξεφεύγουν σχεδόν πάντα από τις μυγοσκοτώστρες μας.",
 "script": [
  L("Παρουσιαστής", "m", "Όλοι το έχουμε ζήσει: σηκώνεις την εφημερίδα, χτυπάς με όλη σου τη δύναμη, και η μύγα έχει ήδη φύγει. Πώς το καταφέρνει;", "We've all experienced it: you raise the newspaper, strike with all your strength, and the fly has already gone. How does it manage?"),
  L("Εντομολόγος", "m", "Το μυστικό είναι ότι η μύγα ζει, ας πούμε, σε αργή κίνηση σε σύγκριση με εμάς. Τα μάτια της επεξεργάζονται πολύ περισσότερες εικόνες το δευτερόλεπτο από τα δικά μας. Εκεί όπου εμείς βλέπουμε μια συνεχή, γρήγορη κίνηση, εκείνη βλέπει κάτι σαν μια σειρά από διαδοχικά καρέ. Το χέρι μας της φαίνεται να πλησιάζει αργά, σχεδόν βαριεστημένα.", "The secret is that the fly lives, let's say, in slow motion compared with us. Its eyes process far more images per second than ours do. Where we see a continuous, fast movement, it sees something like a series of successive frames. Our hand seems to it to approach slowly, almost lazily."),
  L("Παρουσιαστής", "m", "Και πώς αποφασίζει προς τα πού να πετάξει;", "And how does it decide which way to fly?"),
  L("Εντομολόγος", "m", "Εδώ είναι το πιο εντυπωσιακό. Πειράματα με κάμερες υψηλής ταχύτητας έδειξαν ότι, μέσα σε λιγότερο από ένα δέκατο του δευτερολέπτου, η μύγα υπολογίζει από πού έρχεται η απειλή και μετακινεί τα πόδια της, ώστε να απογειωθεί προς την αντίθετη κατεύθυνση. Και όλα αυτά με έναν εγκέφαλο που δεν έχει ούτε ένα εκατομμύριο νευρώνες.", "Here's the most impressive part. Experiments with high-speed cameras showed that, in less than a tenth of a second, the fly calculates where the threat is coming from and repositions its legs, so as to take off in the opposite direction. And all that with a brain that doesn't have even a million neurons."),
  L("Εντομολόγος", "m", "Αν θέλετε μια πρακτική συμβουλή που προκύπτει από αυτές τις έρευνες: μη στοχεύετε εκεί όπου βρίσκεται η μύγα, αλλά λίγο μπροστά της, εκεί όπου πιθανότατα θα πεταχτεί. Ή, ακόμα καλύτερα, ανοίξτε το παράθυρο.", "If you want a practical tip that follows from this research: don't aim where the fly is, but a little in front of it, where it will most likely jump to. Or, even better, open the window."),
 ],
 "questions": [
  Q("Γιατί η μύγα βλέπει τις κινήσεις μας σαν σε αργή κίνηση;", ["Γιατί έχει πολλά μάτια", "Γιατί τα μάτια της επεξεργάζονται πολύ περισσότερες εικόνες το δευτερόλεπτο", "Γιατί ακούει τον αέρα που κινείται", "Γιατί βλέπει μόνο ασπρόμαυρα"], 1, "Τα μάτια της επεξεργάζονται πολύ περισσότερες εικόνες το δευτερόλεπτο από τα δικά μας"),
  Q("Τι έδειξαν οι κάμερες υψηλής ταχύτητας;", ["Ότι η μύγα πετά τυχαία", "Ότι η μύγα κλείνει τα μάτια της", "Ότι η μύγα μετακινεί τα πόδια της για να απογειωθεί αντίθετα από την απειλή", "Ότι η μύγα δεν αντιδρά πριν από το χτύπημα"], 2, "μετακινεί τα πόδια της, ώστε να απογειωθεί προς την αντίθετη κατεύθυνση"),
  Q("Ποια πρακτική συμβουλή δίνει ο εντομολόγος;", ["Να στοχεύουμε λίγο μπροστά από τη μύγα", "Να χτυπάμε πιο δυνατά", "Να χρησιμοποιούμε εντομοκτόνο", "Να περιμένουμε να κάτσει στον τοίχο"], 0, "μη στοχεύετε εκεί όπου βρίσκεται η μύγα, αλλά λίγο μπροστά της"),
 ],
 "gloss": {"ξεφεύγουν": "ξεφεύγω — to escape", "μυγοσκοτώστρες": "μυγοσκοτώστρα — fly swatter", "αργή κίνηση": "αργή κίνηση — slow motion", "επεξεργάζονται": "επεξεργάζομαι — to process", "διαδοχικά καρέ": "καρέ — frame (of a film)", "βαριεστημένα": "βαριεστημένα — lazily, wearily", "υψηλής ταχύτητας": "υψηλής ταχύτητας — high-speed", "απειλή": "απειλή — threat", "απογειωθεί": "απογειώνομαι — to take off", "νευρώνες": "νευρώνας — neuron", "στοχεύετε": "στοχεύω — to aim", "πεταχτεί": "πετάγομαι — to dart, jump"},
})

ITEMS.append({
 "id": "l180-c1-giati-zaronoun-ta-daktyla", "title": "Γιατί ζαρώνουν τα δάχτυλα στο νερό", "title_en": "Why fingers wrinkle in water", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια φυσιολόγο να εξηγεί σε μια επιστημονική εκπομπή γιατί ζαρώνουν τα δάχτυλά μας όταν μένουμε πολλή ώρα στο νερό.",
 "script": [
  L("Φυσιολόγος", "f", "Για πολλά χρόνια η εξήγηση φαινόταν προφανής: το δέρμα απορροφά νερό, φουσκώνει και ζαρώνει, όπως ένα σφουγγάρι. Υπάρχει όμως μια λεπτομέρεια που δεν ταιριάζει με αυτή την ιδέα. Ήδη από τη δεκαετία του τριάντα, γιατροί είχαν παρατηρήσει ότι σε ανθρώπους με βλάβη σε ορισμένα νεύρα των χεριών, τα δάχτυλα δεν ζαρώνουν καθόλου στο νερό.", "For many years the explanation seemed obvious: the skin absorbs water, swells and wrinkles, like a sponge. There is, however, a detail that doesn't fit this idea. As early as the 1930s, doctors had noticed that in people with damage to certain nerves of the hand, the fingers don't wrinkle at all in water."),
  L("Φυσιολόγος", "f", "Αυτό σημαίνει ότι το ζάρωμα δεν είναι απλώς ένα φυσικό φαινόμενο, αλλά μια ενεργή αντίδραση του νευρικού συστήματος. Όταν τα δάχτυλα μένουν στο νερό, τα αιμοφόρα αγγεία κάτω από το δέρμα συστέλλονται, ο όγκος του ιστού μειώνεται, και η επιφάνεια ζαρώνει. Και αφού ο οργανισμός ξοδεύει ενέργεια γι' αυτό, είναι λογικό να υποθέσουμε ότι εξυπηρετεί κάποιον σκοπό.", "This means that the wrinkling isn't simply a physical phenomenon, but an active response of the nervous system. When the fingers stay in water, the blood vessels under the skin constrict, the volume of the tissue decreases, and the surface wrinkles. And since the body spends energy on this, it's reasonable to assume that it serves some purpose."),
  L("Φυσιολόγος", "f", "Μια δημοφιλής υπόθεση είναι ότι οι ζάρες λειτουργούν σαν τα αυλάκια στα λάστιχα ενός αυτοκινήτου, που απομακρύνουν το νερό και βελτιώνουν το κράτημα. Σε ένα πείραμα, οι συμμετέχοντες με ζαρωμένα δάχτυλα μετέφεραν βρεγμένα βότσαλα από ένα δοχείο σε άλλο πιο γρήγορα. Άλλες μελέτες, όμως, δεν βρήκαν καμία διαφορά. Το ζήτημα, λοιπόν, παραμένει ανοιχτό· και το ωραίο είναι ότι ο καθένας μπορεί να κάνει το πείραμα στην μπανιέρα του.", "A popular hypothesis is that the wrinkles work like the grooves in a car's tyres, which channel away water and improve grip. In one experiment, participants with wrinkled fingers moved wet pebbles from one container to another faster. Other studies, however, found no difference. The question, then, remains open; and the nice thing is that anyone can do the experiment in their bathtub."),
 ],
 "questions": [
  Q("Ποια παρατήρηση δεν ταίριαζε με την παλιά εξήγηση;", ["Ότι τα δάχτυλα ζαρώνουν και στο αλμυρό νερό", "Ότι σε ανθρώπους με βλάβη σε ορισμένα νεύρα τα δάχτυλα δεν ζαρώνουν", "Ότι τα παιδιά δεν ζαρώνουν", "Ότι ζαρώνουν μόνο τα πόδια"], 1, "σε ανθρώπους με βλάβη σε ορισμένα νεύρα των χεριών, τα δάχτυλα δεν ζαρώνουν καθόλου στο νερό"),
  Q("Τι συμβαίνει κάτω από το δέρμα όταν ζαρώνουν τα δάχτυλα;", ["Το δέρμα γεμίζει νερό", "Τα νεύρα σταματούν να λειτουργούν", "Τα αιμοφόρα αγγεία συστέλλονται και ο όγκος του ιστού μειώνεται", "Η θερμοκρασία ανεβαίνει"], 2, "τα αιμοφόρα αγγεία κάτω από το δέρμα συστέλλονται, ο όγκος του ιστού μειώνεται"),
  Q("Τι λέει η φυσιολόγος για την υπόθεση του καλύτερου κρατήματος;", ["Ότι ορισμένα πειράματα τη στηρίζουν και άλλα όχι", "Ότι έχει αποδειχθεί οριστικά", "Ότι έχει απορριφθεί", "Ότι δεν έχει ελεγχθεί ποτέ"], 0, "Άλλες μελέτες, όμως, δεν βρήκαν καμία διαφορά"),
 ],
 "gloss": {"ζαρώνουν": "ζαρώνω — to wrinkle", "φυσιολόγο": "φυσιολόγος — physiologist", "προφανής": "προφανής — obvious", "φουσκώνει": "φουσκώνω — to swell", "σφουγγάρι": "σφουγγάρι — sponge", "βλάβη": "βλάβη — damage", "ζάρωμα": "ζάρωμα — wrinkling", "ενεργή": "ενεργός — active", "συστέλλονται": "συστέλλομαι — to constrict", "εξυπηρετεί": "εξυπηρετώ — to serve (a purpose)", "λάστιχα": "λάστιχο — tyre", "κράτημα": "κράτημα — grip", "βότσαλα": "βότσαλο — pebble", "μπανιέρα": "μπανιέρα — bathtub"},
})

rnd = random.Random(180)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-180.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
