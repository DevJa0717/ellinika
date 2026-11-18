# Source for library/listening/listening-174.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l174.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l174-ann-exetastiko-kentro", "title": "Ανακοίνωση σε εξεταστικό κέντρο των Πανελλαδικών", "title_en": "An announcement at a national exams centre", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός σχολείου, λίγα λεπτά πριν αρχίσουν οι Πανελλαδικές εξετάσεις.",
 "script": [
  L("Πρόεδρος της επιτροπής", "f", "Καλημέρα σε όλους. Οι υποψήφιοι παρακαλούνται να βρίσκονται στις αίθουσές τους μέχρι τις επτά και μισή. Μετά τις οχτώ δεν επιτρέπεται η είσοδος σε κανέναν.", "Good morning, everyone. Candidates are asked to be in their rooms by half past seven. After eight no one is allowed in."),
  L("Πρόεδρος της επιτροπής", "f", "Πάνω στο θρανίο θα έχετε μόνο την ταυτότητα ή το διαβατήριό σας, στυλό με μπλε μελάνι και ένα μπουκάλι νερό χωρίς ετικέτα. Τα κινητά τηλέφωνα και τα έξυπνα ρολόγια παραδίδονται κλειστά στους επιτηρητές, πριν μοιραστούν τα θέματα.", "On the desk you will have only your identity card or passport, pens with blue ink and a bottle of water without a label. Mobile phones and smartwatches are handed in switched off to the invigilators before the questions are handed out."),
  L("Πρόεδρος της επιτροπής", "f", "Κανείς δεν μπορεί να αποχωρήσει πριν περάσει μία ώρα από τη διανομή των θεμάτων. Οι γονείς παρακαλούνται να μην περιμένουν στην αυλή, αλλά έξω από την κεντρική πύλη. Καλή επιτυχία σε όλους!", "No one may leave before an hour has passed since the questions were handed out. Parents are asked not to wait in the courtyard, but outside the main gate. Good luck to everyone!"),
 ],
 "questions": [
  Q("Τι επιτρέπεται να έχουν οι υποψήφιοι πάνω στο θρανίο;", ["Το κινητό τους, κλειστό", "Ταυτότητα, μπλε στυλό και νερό χωρίς ετικέτα", "Ένα έξυπνο ρολόι", "Σημειώσεις και λεξικό"], 1, "μόνο την ταυτότητα ή το διαβατήριό σας, στυλό με μπλε μελάνι και ένα μπουκάλι νερό χωρίς ετικέτα"),
  Q("Πότε μπορεί να φύγει ένας υποψήφιος;", ["Όποτε θέλει", "Μετά τις οχτώ", "Αφού περάσει μία ώρα από τη διανομή των θεμάτων", "Μόνο στο τέλος της εξέτασης"], 2, "Κανείς δεν μπορεί να αποχωρήσει πριν περάσει μία ώρα"),
  Q("Πού πρέπει να περιμένουν οι γονείς;", ["Έξω από την κεντρική πύλη", "Στην αυλή", "Στον διάδρομο", "Στο γραφείο του διευθυντή"], 0, "έξω από την κεντρική πύλη"),
 ],
 "gloss": {"Πανελλαδικές εξετάσεις": "Πανελλαδικές εξετάσεις — Greek national university entrance exams", "υποψήφιοι": "υποψήφιος — candidate", "θρανίο": "θρανίο — school desk", "μελάνι": "μελάνι — ink", "ετικέτα": "ετικέτα — label", "επιτηρητές": "επιτηρητής — invigilator", "θέματα": "θέματα (εξετάσεων) — exam questions", "αποχωρήσει": "αποχωρώ — to leave", "διανομή": "διανομή — distribution, handing out", "πύλη": "πύλη — gate"},
})

ITEMS.append({
 "id": "l174-int-ektimitis-zimion", "title": "Ο εκτιμητής ζημιών", "title_en": "The loss adjuster", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν εκτιμητή ζημιών που δουλεύει για μια ασφαλιστική εταιρεία.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι ακριβώς κάνει ένας εκτιμητής ζημιών;", "What exactly does a loss adjuster do?"),
  L("Εκτιμητής", "m", "Όταν κάποιος έχει ασφαλίσει το σπίτι ή το μαγαζί του και πάθει ζημιά, από πλημμύρα, φωτιά ή κλοπή, πηγαίνω εγώ να δω τι έγινε. Φωτογραφίζω, μετράω, ρωτάω, και στο τέλος γράφω μια έκθεση για το πόσα χρήματα πρέπει να πάρει ο πελάτης.", "When someone has insured their house or shop and suffers damage, from a flood, a fire or a theft, I go to see what happened. I take photos, measure, ask questions, and at the end I write a report on how much money the customer should get."),
  L("Δημοσιογράφος", "f", "Οι πελάτες σάς βλέπουν σαν εχθρό;", "Do customers see you as an enemy?"),
  L("Εκτιμητής", "m", "Μερικές φορές, ναι. Φτάνω σε ένα σπίτι που μόλις πλημμύρισε, οι άνθρωποι έχουν χάσει πράγματα μιας ζωής, κι εγώ ρωτάω πόσων χρονών ήταν το ψυγείο. Έχω μάθει να ακούω πρώτα και να μετράω μετά. Πολλοί θέλουν απλώς κάποιον να τους πει ότι θα τα καταφέρουν.", "Sometimes, yes. I arrive at a house that has just flooded, people have lost the things of a lifetime, and I ask how old the fridge was. I have learnt to listen first and measure afterwards. Many just want someone to tell them they'll manage."),
  L("Δημοσιογράφος", "f", "Συναντάτε και απάτες;", "Do you also come across fraud?"),
  L("Εκτιμητής", "m", "Σπάνια, αλλά συμβαίνει. Κάποτε ένας πελάτης δήλωσε ότι του έκλεψαν μια ακριβή τηλεόραση. Στις φωτογραφίες από τα γενέθλια του γιου του, την προηγούμενη εβδομάδα, στη θέση της υπήρχε μια γλάστρα.", "Rarely, but it happens. Once a customer declared that an expensive television had been stolen from him. In the photos from his son's birthday the week before, there was a flowerpot in its place."),
 ],
 "questions": [
  Q("Τι κάνει ο εκτιμητής στο τέλος της επίσκεψης;", ["Πληρώνει τον πελάτη επιτόπου", "Γράφει μια έκθεση για το ποσό που πρέπει να πάρει ο πελάτης", "Επισκευάζει τη ζημιά", "Καλεί την αστυνομία"], 1, "γράφω μια έκθεση για το πόσα χρήματα πρέπει να πάρει ο πελάτης"),
  Q("Τι έχει μάθει από την εμπειρία του;", ["Να μετράει γρήγορα", "Να μη μιλάει με τους πελάτες", "Να ακούει πρώτα και να μετράει μετά", "Να μην πιστεύει κανέναν"], 2, "Έχω μάθει να ακούω πρώτα και να μετράω μετά"),
  Q("Πώς κατάλαβε την απάτη με την τηλεόραση;", ["Από φωτογραφίες όπου στη θέση της υπήρχε μια γλάστρα", "Από τον γείτονα", "Από την απόδειξη αγοράς", "Από τις κάμερες ασφαλείας"], 0, "στη θέση της υπήρχε μια γλάστρα"),
 ],
 "gloss": {"εκτιμητή ζημιών": "εκτιμητής ζημιών — loss adjuster", "ασφαλιστική εταιρεία": "ασφαλιστική εταιρεία — insurance company", "ασφαλίσει": "ασφαλίζω — to insure", "κλοπή": "κλοπή — theft", "έκθεση": "έκθεση — report", "εχθρό": "εχθρός — enemy", "πλημμύρισε": "πλημμυρίζω — to flood", "απάτες": "απάτη — fraud", "δήλωσε": "δηλώνω — to declare", "γλάστρα": "γλάστρα — flowerpot"},
})

ITEMS.append({
 "id": "l174-int-orykta-lavriou", "title": "Η συλλέκτρια ορυκτών του Λαυρίου", "title_en": "The mineral collector of Lavrio", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γυναίκα από το Λαύριο που συλλέγει ορυκτά εδώ και τριάντα χρόνια.",
 "script": [
  L("Δημοσιογράφος", "m", "Γιατί το Λαύριο είναι τόσο γνωστό στους συλλέκτες ορυκτών;", "Why is Lavrio so well known to mineral collectors?"),
  L("Συλλέκτρια", "f", "Γιατί εδώ υπάρχουν μεταλλεία από την αρχαιότητα. Οι αρχαίοι Αθηναίοι έβγαζαν από αυτή τη γη ασήμι. Τα παλιά υπολείμματα από τα μεταλλεία, οι σκουριές όπως τις λέμε, έμειναν για αιώνες κοντά στη θάλασσα, και το αλμυρό νερό δημιούργησε μέσα τους κρυστάλλους που δεν υπάρχουν πουθενά αλλού στον κόσμο.", "Because there have been mines here since antiquity. The ancient Athenians took silver out of this ground. The old residues from the mines, the slag as we call it, stayed for centuries near the sea, and the salt water created crystals in them that exist nowhere else in the world."),
  L("Δημοσιογράφος", "m", "Μπορεί ο καθένας να μαζέψει ορυκτά;", "Can anyone collect minerals?"),
  L("Συλλέκτρια", "f", "Όχι πια όπως παλιά. Πολλές περιοχές είναι προστατευόμενες, και σωστά. Εγώ πηγαίνω μόνο εκεί όπου επιτρέπεται, και τα πιο σπάνια κομμάτια τα δείχνω στο μουσείο. Οι πιο ωραίοι κρύσταλλοι είναι μικροσκοπικοί· τους βλέπεις μόνο με μεγεθυντικό φακό.", "Not like before. Many areas are protected, and rightly so. I only go where it is allowed, and I show the rarest pieces to the museum. The most beautiful crystals are tiny; you only see them with a magnifying glass."),
  L("Δημοσιογράφος", "m", "Τι σας αρέσει περισσότερο σε αυτό το χόμπι;", "What do you like most about this hobby?"),
  L("Συλλέκτρια", "f", "Η υπομονή που σου μαθαίνει. Μπορεί να ψάχνεις έναν ολόκληρο μήνα και να μη βρεις τίποτα. Και μετά, ένα πρωί, σπας μια πέτρα και μέσα λάμπει ένα πράσινο αστεράκι.", "The patience it teaches you. You might search for a whole month and find nothing. And then, one morning, you break a stone and inside a little green star shines."),
 ],
 "questions": [
  Q("Πώς δημιουργήθηκαν οι σπάνιοι κρύσταλλοι του Λαυρίου;", ["Από ηφαίστεια", "Από το αλμυρό νερό μέσα στις παλιές σκουριές των μεταλλείων", "Από τους αρχαίους τεχνίτες", "Από τους σεισμούς"], 1, "το αλμυρό νερό δημιούργησε μέσα τους κρυστάλλους"),
  Q("Τι κάνει με τα πιο σπάνια κομμάτια;", ["Τα πουλάει στο διαδίκτυο", "Τα χαρίζει στους φίλους της", "Τα δείχνει στο μουσείο", "Τα κρύβει στο σπίτι της"], 2, "τα πιο σπάνια κομμάτια τα δείχνω στο μουσείο"),
  Q("Τι της αρέσει περισσότερο στο χόμπι της;", ["Η υπομονή που της μαθαίνει", "Τα χρήματα που κερδίζει", "Τα ταξίδια σε άλλες χώρες", "Η παρέα με άλλους συλλέκτες"], 0, "Η υπομονή που σου μαθαίνει"),
 ],
 "gloss": {"συλλέγει": "συλλέγω — to collect", "ορυκτά": "ορυκτό — mineral", "μεταλλεία": "μεταλλείο — mine", "ασήμι": "ασήμι — silver", "υπολείμματα": "υπόλειμμα — residue", "σκουριές": "σκουριά — slag (here); rust", "κρυστάλλους": "κρύσταλλος — crystal", "προστατευόμενες": "προστατευόμενος — protected", "μικροσκοπικοί": "μικροσκοπικός — tiny", "μεγεθυντικό φακό": "μεγεθυντικός φακός — magnifying glass"},
})

ITEMS.append({
 "id": "l174-dia-klironomisame-ena-chorafi", "title": "Κληρονομήσαμε ένα χωράφι", "title_en": "We inherited a field", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο αδέρφια να συζητούν τι θα κάνουν με ένα χωράφι που τους άφησε η γιαγιά τους.",
 "script": [
  L("Θοδωρής", "m", "Μίλησα με τον συμβολαιογράφο. Για να γίνει το χωράφι δικό μας, πρέπει πρώτα να πληρώσουμε φόρο κληρονομιάς και να το περάσουμε στο κτηματολόγιο. Θα μας κοστίσει περίπου χίλια ευρώ.", "I spoke to the notary. For the field to become ours, we first have to pay inheritance tax and register it in the land registry. It will cost us about a thousand euros."),
  L("Ελένη", "f", "Και μετά; Εσύ ζεις στην Πάτρα, εγώ στη Θεσσαλονίκη. Ποιος θα το καλλιεργεί; Ένας γείτονας ήδη ρώτησε αν το πουλάμε.", "And then? You live in Patras, I live in Thessaloniki. Who's going to farm it? A neighbour has already asked if we're selling it."),
  L("Θοδωρής", "m", "Έχει σαράντα ελιές που φύτεψε ο παππούς. Δεν μπορώ να τις δώσω έτσι. Τι λες να το νοικιάσουμε στον γείτονα; Εκείνος θα το φροντίζει, κι εμείς θα παίρνουμε μερικά κιλά λάδι κάθε χρόνο.", "It has forty olive trees our grandfather planted. I can't just give them away. What do you say we rent it to the neighbour? He'll look after it, and we'll get a few kilos of oil every year."),
  L("Ελένη", "f", "Μου αρέσει αυτό. Έτσι δεν χάνουμε το χωράφι, και τα παιδιά μας θα έχουν κάπου να έρχονται τον Νοέμβριο για το μάζεμα. Αλλά να το γράψουμε σε χαρτί, όχι με μια χειραψία.", "I like that. That way we don't lose the field, and our children will have somewhere to come in November for the harvest. But let's put it on paper, not just a handshake."),
 ],
 "questions": [
  Q("Τι πρέπει να κάνουν πρώτα για να γίνει το χωράφι δικό τους;", ["Να το πουλήσουν", "Να πληρώσουν φόρο κληρονομιάς και να το περάσουν στο κτηματολόγιο", "Να φυτέψουν ελιές", "Να μετακομίσουν στο χωριό"], 1, "να πληρώσουμε φόρο κληρονομιάς και να το περάσουμε στο κτηματολόγιο"),
  Q("Γιατί ο Θοδωρής δεν θέλει να πουλήσει το χωράφι;", ["Γιατί η τιμή είναι χαμηλή", "Γιατί θέλει να μείνει εκεί", "Γιατί έχει τις ελιές που φύτεψε ο παππούς τους", "Γιατί δεν του αρέσει ο γείτονας"], 2, "Έχει σαράντα ελιές που φύτεψε ο παππούς"),
  Q("Τι ζητάει η Ελένη;", ["Να γράψουν τη συμφωνία σε χαρτί", "Να πουλήσουν το λάδι", "Να έρθει ο γείτονας στη Θεσσαλονίκη", "Να μοιράσουν το χωράφι στα δύο"], 0, "να το γράψουμε σε χαρτί, όχι με μια χειραψία"),
 ],
 "gloss": {"συμβολαιογράφο": "συμβολαιογράφος — notary", "φόρο κληρονομιάς": "φόρος κληρονομιάς — inheritance tax", "κτηματολόγιο": "κτηματολόγιο — land registry", "καλλιεργεί": "καλλιεργώ — to farm, cultivate", "νοικιάσουμε": "νοικιάζω — to rent (out)", "μάζεμα": "μάζεμα — harvest, picking", "χειραψία": "χειραψία — handshake"},
})

ITEMS.append({
 "id": "l174-dia-votsala-sti-valitsa", "title": "Βότσαλα στη βαλίτσα;", "title_en": "Pebbles in the suitcase?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε μια μητέρα και τη δεκάχρονη κόρη της την τελευταία μέρα των διακοπών τους σε ένα νησί.",
 "script": [
  L("Κόρη", "f", "Μαμά, κοίτα! Μάζεψα είκοσι βότσαλα, όλα άσπρα και στρογγυλά. Θα τα βάλω στη βαλίτσα για να φτιάξω ένα κάδρο στο δωμάτιό μου.", "Mum, look! I've collected twenty pebbles, all white and round. I'll put them in the suitcase to make a picture frame in my room."),
  L("Μητέρα", "f", "Είναι πανέμορφα, αλλά δεν μπορούμε να τα πάρουμε. Απαγορεύεται να παίρνουμε άμμο και βότσαλα από τις παραλίες, και μπορεί να πληρώσουμε και πρόστιμο.", "They're beautiful, but we can't take them. It's forbidden to take sand and pebbles from beaches, and we might even have to pay a fine."),
  L("Κόρη", "f", "Μα είναι μόνο είκοσι! Η παραλία έχει εκατομμύρια.", "But it's only twenty! The beach has millions."),
  L("Μητέρα", "f", "Αν το σκεφτεί έτσι κάθε επισκέπτης, σε λίγα χρόνια η παραλία θα είναι γυμνή. Ξέρεις τι κάνουμε; Τα φωτογραφίζουμε όλα μαζί πάνω στην άμμο, και στο σπίτι τυπώνουμε τη φωτογραφία για το κάδρο σου.", "If every visitor thinks like that, in a few years the beach will be bare. You know what we'll do? We'll photograph them all together on the sand, and at home we'll print the photo for your frame."),
  L("Κόρη", "f", "Εντάξει... Αλλά να τα βάλω σε σχήμα καρδιάς πρώτα!", "OK... But let me put them in the shape of a heart first!"),
 ],
 "questions": [
  Q("Τι θέλει να κάνει η κόρη με τα βότσαλα;", ["Να τα χαρίσει στη γιαγιά της", "Να φτιάξει ένα κάδρο στο δωμάτιό της", "Να τα πουλήσει", "Να τα ρίξει στη θάλασσα"], 1, "για να φτιάξω ένα κάδρο στο δωμάτιό μου"),
  Q("Γιατί η μητέρα λέει όχι;", ["Γιατί η βαλίτσα είναι γεμάτη", "Γιατί τα βότσαλα είναι βαριά", "Γιατί απαγορεύεται και μπορεί να πληρώσουν πρόστιμο", "Γιατί δεν της αρέσουν"], 2, "Απαγορεύεται να παίρνουμε άμμο και βότσαλα"),
  Q("Ποια λύση προτείνει η μητέρα;", ["Να φωτογραφίσουν τα βότσαλα και να τυπώσουν τη φωτογραφία", "Να πάρουν μόνο ένα βότσαλο", "Να αγοράσουν βότσαλα από ένα μαγαζί", "Να γυρίσουν του χρόνου"], 0, "Τα φωτογραφίζουμε όλα μαζί πάνω στην άμμο"),
 ],
 "gloss": {"βότσαλα": "βότσαλο — pebble", "στρογγυλά": "στρογγυλός — round", "κάδρο": "κάδρο — picture frame", "πρόστιμο": "πρόστιμο — fine", "γυμνή": "γυμνός — bare, naked", "τυπώνουμε": "τυπώνω — to print", "σχήμα καρδιάς": "σε σχήμα καρδιάς — heart-shaped"},
})

ITEMS.append({
 "id": "l174-mon-allergia-sta-fistikia", "title": "Ζω με αλλεργία στα φιστίκια", "title_en": "Living with a peanut allergy", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια φοιτήτρια να μιλάει σε ένα ραδιοφωνικό πρόγραμμα για τη σοβαρή αλλεργία της.",
 "script": [
  L("Φοιτήτρια", "f", "Είμαι αλλεργική στα αράπικα φιστίκια από τότε που θυμάμαι τον εαυτό μου. Δεν είναι απλώς μια φαγούρα· αν φάω έστω και ένα μικρό κομμάτι, μπορεί να πάθω σοκ και να μην μπορώ να αναπνεύσω. Γι' αυτό έχω πάντα στην τσάντα μου δύο ενέσεις αδρεναλίνης.", "I've been allergic to peanuts for as long as I can remember. It isn't just an itch; if I eat even a small piece, I can go into shock and be unable to breathe. That's why I always have two adrenaline injections in my bag."),
  L("Φοιτήτρια", "f", "Το πιο δύσκολο είναι τα εστιατόρια. Πρέπει να εξηγώ κάθε φορά ότι δεν φτάνει να βγάλουν τα φιστίκια από το πιάτο· ούτε το μαχαίρι ούτε το λάδι πρέπει να έχουν αγγίξει φιστίκι. Μερικοί σερβιτόροι με κοιτάζουν σαν να είμαι ιδιότροπη.", "The hardest thing is restaurants. I have to explain every time that it isn't enough to take the peanuts off the plate; neither the knife nor the oil must have touched a peanut. Some waiters look at me as if I were fussy."),
  L("Φοιτήτρια", "f", "Από την άλλη, έχω φίλους που ξέρουν ακριβώς τι να κάνουν αν πάθω κρίση. Τους έδειξα πώς να μου κάνουν την ένεση στο πόδι, ακόμα και πάνω από το τζιν. Και οι συγκάτοικοί μου έχουν σταματήσει να φέρνουν φιστικοβούτυρο στο σπίτι. Αυτό, για μένα, είναι αληθινή φιλία.", "On the other hand, I have friends who know exactly what to do if I have an attack. I showed them how to give me the injection in the leg, even through jeans. And my flatmates have stopped bringing peanut butter into the flat. That, for me, is true friendship."),
 ],
 "questions": [
  Q("Τι έχει πάντα στην τσάντα της;", ["Ένα σνακ χωρίς φιστίκια", "Δύο ενέσεις αδρεναλίνης", "Ένα σημείωμα από τον γιατρό", "Χάπια για τη φαγούρα"], 1, "έχω πάντα στην τσάντα μου δύο ενέσεις αδρεναλίνης"),
  Q("Τι πρέπει να εξηγεί στα εστιατόρια;", ["Ότι δεν τρώει κρέας", "Ότι θέλει μικρότερη μερίδα", "Ότι ούτε τα σκεύη ούτε το λάδι πρέπει να έχουν αγγίξει φιστίκι", "Ότι προτιμά τραπέζι έξω"], 2, "ούτε το μαχαίρι ούτε το λάδι πρέπει να έχουν αγγίξει φιστίκι"),
  Q("Τι θεωρεί αληθινή φιλία;", ["Ότι οι φίλοι και οι συγκάτοικοί της προσέχουν και ξέρουν τι να κάνουν", "Ότι οι φίλοι της πληρώνουν στο εστιατόριο", "Ότι τη συνοδεύουν στον γιατρό", "Ότι μαγειρεύουν για εκείνη"], 0, "έχω φίλους που ξέρουν ακριβώς τι να κάνουν"),
 ],
 "gloss": {"αλλεργία": "αλλεργία — allergy", "αλλεργική": "αλλεργικός — allergic", "αράπικα φιστίκια": "αράπικο φιστίκι — peanut", "φαγούρα": "φαγούρα — itch", "σοκ": "σοκ (αναφυλακτικό) — (anaphylactic) shock", "ενέσεις αδρεναλίνης": "ένεση αδρεναλίνης — adrenaline injection", "ιδιότροπη": "ιδιότροπος — fussy, awkward", "κρίση": "κρίση — attack (medical)", "συγκάτοικοί": "συγκάτοικος — flatmate", "φιστικοβούτυρο": "φιστικοβούτυρο — peanut butter"},
})

ITEMS.append({
 "id": "l174-vm-ypografi-kidemona", "title": "Μήνυμα από το σχολείο για την υπογραφή του κηδεμόνα", "title_en": "A message from the school about the guardian's signature", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα που άφησε η γραμματέας ενός γυμνασίου στον τηλεφωνητή ενός πατέρα.",
 "script": [
  L("Γραμματέας", "f", "Καλησπέρα σας, κύριε Αλεξίου, σας τηλεφωνώ από τη γραμματεία του Δεύτερου Γυμνασίου. Η Δανάη δεν έχει φέρει ακόμα την υπεύθυνη δήλωση για την τριήμερη εκδρομή στα Ιωάννινα. Χωρίς την υπογραφή του κηδεμόνα δυστυχώς δεν μπορεί να συμμετάσχει.", "Good afternoon, Mr Alexiou, I'm calling from the office of the Second Lower Secondary School. Danai hasn't yet brought the signed declaration for the three-day trip to Ioannina. Without the guardian's signature, unfortunately, she cannot take part."),
  L("Γραμματέας", "f", "Η τελευταία προθεσμία είναι την Παρασκευή στις δώδεκα. Μπορείτε να υπογράψετε το έντυπο που έχει η Δανάη στην τσάντα της ή να περάσετε από τη γραμματεία, που είναι ανοιχτή καθημερινά από τις οχτώ ως τις δύο. Μην ξεχάσετε να συμπληρώσετε και το τηλέφωνο για ώρα ανάγκης.", "The final deadline is Friday at twelve. You can sign the form Danai has in her bag or come by the office, which is open every weekday from eight to two. Don't forget to fill in the emergency phone number too."),
  L("Γραμματέας", "f", "Αν η Δανάη έχει κάποια αλλεργία ή παίρνει φάρμακα, γράψτε το στο πίσω μέρος. Ευχαριστώ πολύ.", "If Danai has an allergy or takes medication, write it on the back. Thank you very much."),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί η γραμματέας;", ["Γιατί η Δανάη έλειψε από το σχολείο", "Γιατί λείπει η υπογραφή του κηδεμόνα για την εκδρομή", "Γιατί η εκδρομή ακυρώθηκε", "Γιατί η Δανάη αρρώστησε"], 1, "Χωρίς την υπογραφή του κηδεμόνα δυστυχώς δεν μπορεί να συμμετάσχει"),
  Q("Μέχρι πότε πρέπει να παραδοθεί η δήλωση;", ["Μέχρι τη Δευτέρα", "Μέχρι αύριο το πρωί", "Μέχρι την Παρασκευή στις δώδεκα", "Μέχρι την ημέρα της εκδρομής"], 2, "Η τελευταία προθεσμία είναι την Παρασκευή στις δώδεκα"),
  Q("Τι πρέπει να γραφτεί στο πίσω μέρος του εντύπου;", ["Αλλεργίες ή φάρμακα της Δανάης", "Το ποσό που πληρώθηκε", "Η διεύθυνση του σπιτιού", "Το όνομα του καθηγητή"], 0, "Αν η Δανάη έχει κάποια αλλεργία ή παίρνει φάρμακα, γράψτε το στο πίσω μέρος"),
 ],
 "gloss": {"γραμματέας": "γραμματέας — secretary", "γυμνασίου": "γυμνάσιο — lower secondary school", "τηλεφωνητή": "τηλεφωνητής — answering machine, voicemail", "γραμματεία": "γραμματεία — school office", "υπεύθυνη δήλωση": "υπεύθυνη δήλωση — signed declaration", "κηδεμόνα": "κηδεμόνας — (legal) guardian", "συμμετάσχει": "συμμετέχω — to take part", "προθεσμία": "προθεσμία — deadline", "έντυπο": "έντυπο — form", "ώρα ανάγκης": "ώρα ανάγκης — emergency"},
})

ITEMS.append({
 "id": "l174-vm-exantlimeno-vivlio", "title": "Μήνυμα από το παλαιοβιβλιοπωλείο", "title_en": "A message from the second-hand bookshop", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα που άφησε ο ιδιοκτήτης ενός παλαιοβιβλιοπωλείου σε μια πελάτισσα.",
 "script": [
  L("Βιβλιοπώλης", "m", "Καλημέρα, κυρία Σταυροπούλου, ο Μιχάλης είμαι από το παλαιοβιβλιοπωλείο στην Ασκληπιού. Έχω καλά νέα: βρήκα το βιβλίο που ψάχνατε, τη συλλογή διηγημάτων του πατέρα σας. Είναι εξαντλημένο εδώ και σαράντα χρόνια, αλλά ένας συνάδελφος από τη Θεσσαλονίκη είχε ένα αντίτυπο.", "Good morning, Mrs Stavropoulou, it's Michalis from the second-hand bookshop on Asklipiou Street. I have good news: I found the book you were looking for, your father's short-story collection. It has been out of print for forty years, but a colleague from Thessaloniki had a copy."),
  L("Βιβλιοπώλης", "m", "Είναι σε καλή κατάσταση, μόνο το εξώφυλλο είναι λίγο ξεθωριασμένο. Και κάτι που ίσως σας συγκινήσει: στην πρώτη σελίδα υπάρχει αφιέρωση με το χέρι του συγγραφέα σε κάποιον φίλο του. Η τιμή είναι τριάντα πέντε ευρώ.", "It's in good condition, only the cover is a little faded. And something that may move you: on the first page there is a dedication in the author's own hand to a friend of his. The price is thirty-five euros."),
  L("Βιβλιοπώλης", "m", "Θα το κρατήσω για σας ως το Σάββατο. Αν δεν μπορείτε να περάσετε, μπορώ να σας το στείλω με αντικαταβολή. Πείτε μου τι προτιμάτε.", "I'll keep it for you until Saturday. If you can't come by, I can send it to you cash on delivery. Let me know which you prefer."),
 ],
 "questions": [
  Q("Ποιο βιβλίο βρήκε ο βιβλιοπώλης;", ["Ένα μυθιστόρημα που ζήτησε η κόρη της πελάτισσας", "Τη συλλογή διηγημάτων του πατέρα της πελάτισσας", "Ένα παλιό λεξικό", "Ένα βιβλίο μαγειρικής"], 1, "τη συλλογή διηγημάτων του πατέρα σας"),
  Q("Τι ιδιαίτερο έχει το αντίτυπο;", ["Είναι καινούργιο", "Έχει εικόνες", "Έχει χειρόγραφη αφιέρωση του συγγραφέα", "Είναι μεταφρασμένο"], 2, "υπάρχει αφιέρωση με το χέρι του συγγραφέα"),
  Q("Τι προτείνει ο βιβλιοπώλης αν η πελάτισσα δεν μπορεί να περάσει;", ["Να της το στείλει με αντικαταβολή", "Να το κρατήσει για έναν μήνα", "Να το φέρει ο ίδιος στο σπίτι της", "Να το πουλήσει σε άλλον"], 0, "μπορώ να σας το στείλω με αντικαταβολή"),
 ],
 "gloss": {"παλαιοβιβλιοπωλείου": "παλαιοβιβλιοπωλείο — second-hand bookshop", "πελάτισσα": "πελάτισσα — (female) customer", "διηγημάτων": "διήγημα — short story", "εξαντλημένο": "εξαντλημένος — out of print; exhausted", "συνάδελφος": "συνάδελφος — colleague", "αντίτυπο": "αντίτυπο — copy (of a book)", "εξώφυλλο": "εξώφυλλο — cover", "ξεθωριασμένο": "ξεθωριασμένος — faded", "αφιέρωση": "αφιέρωση — dedication", "αντικαταβολή": "αντικαταβολή — cash on delivery"},
})

ITEMS.append({
 "id": "l174-c1-giati-yparchoun-palirroies", "title": "Γιατί η Μεσόγειος έχει τόσο μικρές παλίρροιες", "title_en": "Why the Mediterranean has such small tides", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν ωκεανογράφο για τις παλίρροιες.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι προκαλεί τις παλίρροιες;", "What causes tides?"),
  L("Ωκεανογράφος", "m", "Κυρίως η βαρύτητα της Σελήνης και, σε μικρότερο βαθμό, του Ήλιου. Η Σελήνη έλκει περισσότερο τα νερά που βρίσκονται πιο κοντά της, κι έτσι σχηματίζεται ένα «φούσκωμα» του ωκεανού προς την πλευρά της. Ένα δεύτερο φούσκωμα σχηματίζεται στην αντίθετη πλευρά της Γης. Καθώς η Γη περιστρέφεται, οι περισσότερες ακτές περνούν από δύο πλημμυρίδες και δύο αμπώτιδες περίπου κάθε μέρα.", "Mainly the gravity of the Moon and, to a lesser degree, of the Sun. The Moon pulls more strongly on the waters closest to it, and so a 'bulge' of the ocean forms on its side. A second bulge forms on the opposite side of the Earth. As the Earth rotates, most coasts go through two high tides and two low tides roughly every day."),
  L("Δημοσιογράφος", "f", "Γιατί όμως στην Ελλάδα σχεδόν δεν τις καταλαβαίνουμε;", "But why do we hardly notice them in Greece?"),
  L("Ωκεανογράφος", "m", "Γιατί η Μεσόγειος είναι μια σχεδόν κλειστή θάλασσα, που επικοινωνεί με τον Ατλαντικό μόνο από το στενό του Γιβραλτάρ. Το παλιρροιακό κύμα του ωκεανού δεν μπορεί να μπει ολόκληρο, και η ίδια η Μεσόγειος είναι πολύ μικρή για να σχηματίσει δικές της μεγάλες παλίρροιες. Έτσι, στις περισσότερες ελληνικές ακτές η διαφορά στάθμης είναι μόλις μερικές δεκάδες εκατοστά, ενώ σε ορισμένες ακτές του Ατλαντικού ξεπερνά τα δέκα μέτρα.", "Because the Mediterranean is an almost closed sea, which connects with the Atlantic only through the Strait of Gibraltar. The ocean's tidal wave can't get in fully, and the Mediterranean itself is too small to form big tides of its own. So on most Greek coasts the difference in level is only a few tens of centimetres, whereas on some Atlantic coasts it exceeds ten metres."),
  L("Δημοσιογράφος", "f", "Υπάρχει κάποια εξαίρεση;", "Is there an exception?"),
  L("Ωκεανογράφος", "m", "Ο Εύριπος, στη Χαλκίδα. Εκεί το νερό αλλάζει κατεύθυνση αρκετές φορές την ημέρα, άλλοτε κανονικά και άλλοτε με τρόπο που μοιάζει ακανόνιστος. Δεν οφείλεται σε μεγάλες παλίρροιες, αλλά στη μικρή διαφορά στάθμης ανάμεσα στον βόρειο και στον νότιο Ευβοϊκό, που σπρώχνει το νερό μέσα από ένα πολύ στενό πέρασμα. Το φαινόμενο απασχολούσε ήδη τους αρχαίους.", "The Euripus, at Chalkida. There the water changes direction several times a day, sometimes regularly and sometimes in a way that looks irregular. It isn't due to big tides, but to the small difference in level between the northern and the southern Euboean Gulf, which pushes the water through a very narrow passage. The phenomenon already occupied the ancients."),
 ],
 "questions": [
  Q("Τι προκαλεί κυρίως τις παλίρροιες;", ["Ο άνεμος", "Η βαρύτητα της Σελήνης και, λιγότερο, του Ήλιου", "Οι σεισμοί στον βυθό", "Τα ποτάμια που χύνονται στη θάλασσα"], 1, "Κυρίως η βαρύτητα της Σελήνης"),
  Q("Γιατί οι παλίρροιες στη Μεσόγειο είναι μικρές;", ["Γιατί το νερό της είναι πιο αλμυρό", "Γιατί είναι πολύ ζεστή", "Γιατί είναι σχεδόν κλειστή και πολύ μικρή για δικές της μεγάλες παλίρροιες", "Γιατί η Σελήνη δεν φαίνεται από εκεί"], 2, "η Μεσόγειος είναι μια σχεδόν κλειστή θάλασσα"),
  Q("Σε τι οφείλονται τα ρεύματα του Ευρίπου, σύμφωνα με τον ωκεανογράφο;", ["Στη μικρή διαφορά στάθμης ανάμεσα στον βόρειο και στον νότιο Ευβοϊκό", "Σε μεγάλες παλίρροιες", "Στα πλοία που περνούν", "Σε υπόγειες πηγές"], 0, "στη μικρή διαφορά στάθμης ανάμεσα στον βόρειο και στον νότιο Ευβοϊκό"),
 ],
 "gloss": {"ωκεανογράφο": "ωκεανογράφος — oceanographer", "παλίρροιες": "παλίρροια — tide", "βαρύτητα": "βαρύτητα — gravity", "έλκει": "έλκω — to attract, pull", "φούσκωμα": "φούσκωμα — bulge, swelling", "περιστρέφεται": "περιστρέφομαι — to rotate", "πλημμυρίδες": "πλημμυρίδα — high tide", "αμπώτιδες": "άμπωτη — low tide, ebb", "παλιρροιακό κύμα": "παλιρροιακό κύμα — tidal wave (of the tide)", "στάθμης": "στάθμη — level", "ακανόνιστος": "ακανόνιστος — irregular", "πέρασμα": "πέρασμα — passage"},
})

ITEMS.append({
 "id": "l174-c1-apo-pou-erchetai-i-ammos", "title": "Από πού έρχεται η άμμος", "title_en": "Where sand comes from", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια γεωλόγο σε μια ομιλία για την άμμο των παραλιών.",
 "script": [
  L("Γεωλόγος", "f", "Κάθε κόκκος άμμου είναι ένα μικρό κομμάτι από κάποιον βράχο που διαβρώθηκε. Η βροχή, ο παγετός, τα ποτάμια και τα κύματα σπάνε τα πετρώματα σε όλο και μικρότερα κομμάτια, μια διαδικασία που μπορεί να κρατήσει χιλιάδες ή και εκατομμύρια χρόνια. Στις περισσότερες ακτές του κόσμου η άμμος αποτελείται κυρίως από χαλαζία, ένα ορυκτό εξαιρετικά ανθεκτικό.", "Every grain of sand is a small piece of some rock that has eroded. Rain, frost, rivers and waves break rocks into ever smaller pieces, a process that can take thousands or even millions of years. On most coasts of the world, sand consists mainly of quartz, an extremely durable mineral."),
  L("Γεωλόγος", "f", "Το χρώμα της άμμου μάς λέει την ιστορία της. Στις τροπικές θάλασσες η κάτασπρη άμμος προέρχεται συχνά από θραύσματα κοραλλιών και κοχυλιών. Στη Σαντορίνη, αντίθετα, οι μαύρες παραλίες οφείλουν το χρώμα τους στα ηφαιστειακά πετρώματα του νησιού.", "The colour of sand tells us its history. In tropical seas the snow-white sand often comes from fragments of corals and shells. On Santorini, by contrast, the black beaches owe their colour to the island's volcanic rocks."),
  L("Γεωλόγος", "f", "Ίσως σας εκπλήξει, αλλά η άμμος είναι από τα υλικά που καταναλώνουμε περισσότερο, κυρίως για το σκυρόδεμα. Και η άμμος της ερήμου δεν μας βοηθά πολύ: οι κόκκοι της έχουν στρογγυλέψει τόσο από τον άνεμο, που δεν δένουν καλά μεταξύ τους. Γι' αυτό σε πολλά μέρη του κόσμου αφαιρείται άμμος από ποτάμια και ακτές, συχνά παράνομα, με σοβαρές συνέπειες για το περιβάλλον.", "It may surprise you, but sand is one of the materials we consume most, mainly for concrete. And desert sand doesn't help us much: its grains have been rounded so much by the wind that they don't bind well together. That's why in many parts of the world sand is removed from rivers and coasts, often illegally, with serious consequences for the environment."),
 ],
 "questions": [
  Q("Από τι αποτελείται κυρίως η άμμος στις περισσότερες ακτές;", ["Από κοράλλια", "Από χαλαζία", "Από ηφαιστειακή στάχτη", "Από αλάτι"], 1, "η άμμος αποτελείται κυρίως από χαλαζία"),
  Q("Γιατί είναι μαύρες οι παραλίες της Σαντορίνης;", ["Από τη ρύπανση", "Από τα φύκια", "Από τα ηφαιστειακά πετρώματα του νησιού", "Από τα κοχύλια"], 2, "οφείλουν το χρώμα τους στα ηφαιστειακά πετρώματα"),
  Q("Γιατί η άμμος της ερήμου δεν είναι κατάλληλη για το σκυρόδεμα;", ["Οι κόκκοι της είναι πολύ στρογγυλεμένοι και δεν δένουν καλά", "Είναι πολύ αλμυρή", "Είναι πολύ βαριά", "Είναι πολύ ακριβή"], 0, "οι κόκκοι της έχουν στρογγυλέψει τόσο από τον άνεμο, που δεν δένουν καλά"),
 ],
 "gloss": {"γεωλόγο": "γεωλόγος — geologist", "κόκκος": "κόκκος — grain", "διαβρώθηκε": "διαβρώνομαι — to erode", "παγετός": "παγετός — frost", "πετρώματα": "πέτρωμα — rock", "χαλαζία": "χαλαζίας — quartz", "ανθεκτικό": "ανθεκτικός — durable", "θραύσματα": "θραύσμα — fragment", "κοραλλιών": "κοράλλι — coral", "κοχυλιών": "κοχύλι — shell", "ηφαιστειακά": "ηφαιστειακός — volcanic", "σκυρόδεμα": "σκυρόδεμα — concrete", "στρογγυλέψει": "στρογγυλεύω — to become round"},
})

rnd = random.Random(174)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-174.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
