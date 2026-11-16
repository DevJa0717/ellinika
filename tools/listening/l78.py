# Source for library/listening/listening-78.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l78.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l78-ann-lixiarxeio", "title": "Ανακοίνωση στο ληξιαρχείο", "title_en": "Announcement at the registry office", "type": "announcement", "level": "B2",
 "context_el": "Περιμένετε στο ληξιαρχείο του δήμου σας για να πάρετε ένα πιστοποιητικό. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Υπάλληλος", "f", "Αγαπητοί δημότες, σας παρακαλούμε να πάρετε αριθμό προτεραιότητας από το μηχάνημα δίπλα στην είσοδο. Το γκισέ ένα εξυπηρετεί δηλώσεις γέννησης και θανάτου, το γκισέ δύο δηλώσεις γάμου και συμφώνου συμβίωσης, και το γκισέ τρία όλα τα υπόλοιπα.", "Dear residents, please take a queue number from the machine next to the entrance. Counter one handles birth and death registrations, counter two marriage and civil partnership registrations, and counter three everything else."),
  L("Υπάλληλος", "f", "Σας υπενθυμίζουμε ότι τα πιστοποιητικά γέννησης και οικογενειακής κατάστασης εκδίδονται πλέον και ηλεκτρονικά, μέσα σε λίγα λεπτά, από την ψηφιακή πύλη του Δημοσίου. Αν χρειάζεστε μόνο ένα τέτοιο πιστοποιητικό, δεν είναι απαραίτητο να περιμένετε στην ουρά.", "We remind you that birth and family-status certificates are now also issued electronically, within a few minutes, through the government's digital portal. If you only need such a certificate, there's no need to wait in the queue."),
  L("Υπάλληλος", "f", "Για τη δήλωση γέννησης, παρακαλούμε να έχετε μαζί σας τη βεβαίωση του μαιευτηρίου και τις ταυτότητες και των δύο γονέων. Η υπηρεσία κλείνει στις δύο και μισή, και αριθμοί δίνονται μέχρι τις δύο.", "For a birth registration, please bring the certificate from the maternity hospital and the identity cards of both parents. The office closes at half past two, and numbers are given out until two."),
 ],
 "questions": [
  Q("Τι εξυπηρετεί το γκισέ δύο;", ["Δηλώσεις γέννησης και θανάτου", "Δηλώσεις γάμου και συμφώνου συμβίωσης", "Όλα τα υπόλοιπα", "Μόνο πιστοποιητικά"], 1, "το γκισέ δύο δηλώσεις γάμου και συμφώνου συμβίωσης"),
  Q("Ποιοι δεν χρειάζεται να περιμένουν στην ουρά;", ["Οι ηλικιωμένοι", "Όσοι χρειάζονται μόνο ένα πιστοποιητικό γέννησης ή οικογενειακής κατάστασης", "Οι γονείς με μωρά", "Όσοι έχουν ραντεβού"], 1, "Αν χρειάζεστε μόνο ένα τέτοιο πιστοποιητικό, δεν είναι απαραίτητο να περιμένετε στην ουρά"),
  Q("Μέχρι πότε δίνονται αριθμοί;", ["Μέχρι τις δύο και μισή", "Μέχρι τις δύο", "Μέχρι τη μία", "Όλη μέρα"], 1, "αριθμοί δίνονται μέχρι τις δύο"),
 ],
 "gloss": {"ληξιαρχείο": "ληξιαρχείο — registry office", "πιστοποιητικό": "πιστοποιητικό — certificate", "δημότες": "δημότης — resident (of a municipality)", "αριθμό προτεραιότητας": "αριθμός προτεραιότητας — queue number", "γκισέ": "γκισέ — counter", "συμφώνου συμβίωσης": "σύμφωνο συμβίωσης — civil partnership", "οικογενειακής κατάστασης": "οικογενειακή κατάσταση — family status", "εκδίδονται": "εκδίδομαι — to be issued", "πύλη": "πύλη — portal", "μαιευτηρίου": "μαιευτήριο — maternity hospital"},
})

ITEMS.append({
 "id": "l78-vm-kommotria", "title": "Μήνυμα από την κομμώτρια", "title_en": "Message from the hairdresser", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κλείσει ραντεβού για βαφή μαλλιών σε ένα κομμωτήριο. Θα ακούσετε ένα μήνυμα από την κομμώτρια.",
 "script": [
  L("Κομμώτρια", "f", "Γεια σου, Ελπίδα, η Ρούλα είμαι από το κομμωτήριο. Σε παίρνω για το ραντεβού του Σαββάτου. Αφού θα βάψεις πρώτη φορά με αυτή τη βαφή, πρέπει να κάνουμε πρώτα ένα τεστ αλλεργίας, τουλάχιστον σαράντα οκτώ ώρες πριν.", "Hi Elpida, it's Roula from the hair salon. I'm calling about Saturday's appointment. Since you'll be using this dye for the first time, we need to do an allergy test first, at least forty-eight hours before."),
  L("Κομμώτρια", "f", "Είναι πολύ απλό: βάζουμε λίγη βαφή πίσω από το αυτί και, αν σε δύο μέρες δεν έχεις κοκκινίλα ή φαγούρα, προχωράμε κανονικά. Μπορείς να περάσεις την Πέμπτη, οποιαδήποτε ώρα, κρατάει πέντε λεπτά.", "It's very simple: we put a little dye behind your ear and, if in two days you have no redness or itching, we go ahead as normal. You can drop by on Thursday, any time, it takes five minutes."),
  L("Κομμώτρια", "f", "Και κάτι ακόμα: μη λούσεις τα μαλλιά σου την ίδια μέρα της βαφής, γιατί το χρώμα πιάνει καλύτερα. Αν δεν μπορείς την Πέμπτη, πες μου να μεταθέσουμε το ραντεβού. Φιλιά!", "And one more thing: don't wash your hair on the day of the colouring, because the colour takes better. If you can't make Thursday, tell me and we'll move the appointment. Love!"),
 ],
 "questions": [
  Q("Γιατί χρειάζεται τεστ αλλεργίας;", ["Γιατί η Ελπίδα έχει αλλεργίες", "Γιατί θα βάψει πρώτη φορά με αυτή τη βαφή", "Γιατί το απαιτεί ο νόμος για όλους", "Γιατί άλλαξε κομμωτήριο"], 1, "Αφού θα βάψεις πρώτη φορά με αυτή τη βαφή"),
  Q("Πότε μπορεί να περάσει για το τεστ;", ["Το Σάββατο το πρωί", "Την Πέμπτη, οποιαδήποτε ώρα", "Την Παρασκευή το απόγευμα", "Μόνο με ραντεβού τη Δευτέρα"], 1, "Μπορείς να περάσεις την Πέμπτη, οποιαδήποτε ώρα"),
  Q("Τι δεν πρέπει να κάνει την ημέρα της βαφής;", ["Να φάει", "Να λούσει τα μαλλιά της", "Να βγει στον ήλιο", "Να κολυμπήσει"], 1, "μη λούσεις τα μαλλιά σου την ίδια μέρα της βαφής"),
 ],
 "gloss": {"κομμώτρια": "κομμώτρια — hairdresser (woman)", "βαφή": "βαφή — dye, colouring", "κομμωτήριο": "κομμωτήριο — hair salon", "αλλεργίας": "αλλεργία — allergy", "κοκκινίλα": "κοκκινίλα — redness", "φαγούρα": "φαγούρα — itching", "λούσεις": "λούζω — to wash (hair)", "πιάνει": "πιάνω — (of colour) to take", "μεταθέσουμε": "μεταθέτω — to move, postpone"},
})

ITEMS.append({
 "id": "l78-dia-agios-vasilis", "title": "Θα πούμε την αλήθεια για τον Άγιο Βασίλη;", "title_en": "Shall we tell the truth about Father Christmas?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο γονείς συζητούν αν πρέπει να πουν στην οκτάχρονη κόρη τους την αλήθεια για τον Άγιο Βασίλη.",
 "script": [
  L("Θοδωρής", "m", "Η Μυρτώ με ρώτησε σήμερα ευθέως αν ο Άγιος Βασίλης υπάρχει. Ένα παιδί στο σχολείο τής είπε ότι τα δώρα τα αγοράζουν οι γονείς. Δεν ήξερα τι να απαντήσω και άλλαξα θέμα.", "Myrto asked me straight out today whether Father Christmas exists. A child at school told her that the parents buy the presents. I didn't know what to answer and changed the subject."),
  L("Κατερίνα", "f", "Είναι οχτώ χρονών, Θοδωρή. Αν ρωτάει τόσο ευθέως, μάλλον ήδη υποψιάζεται. Δεν θέλω να της πούμε ψέματα κατάμουτρα· θα νιώσει ότι την κοροϊδεύαμε.", "She's eight, Thodoris. If she's asking so directly, she probably already suspects. I don't want us to lie to her face; she'll feel we were making fun of her."),
  L("Θοδωρής", "m", "Ναι, αλλά έχει και έναν μικρό αδερφό. Αν το μάθει, θα το πει αμέσως στον Άρη, και αυτός είναι μόλις τεσσάρων.", "Yes, but she also has a little brother. If she finds out, she'll tell Aris straight away, and he's only four."),
  L("Κατερίνα", "f", "Γι’ αυτό λέω να της το πούμε σαν μυστικό των μεγάλων. Ότι ο Άγιος Βασίλης είναι μια ιστορία που κρατάμε ζωντανή για να χαίρονται οι μικροί, και ότι από φέτος μπορεί να γίνει κι εκείνη βοηθός του. Να διαλέξει μαζί μας το δώρο του Άρη.", "That's why I say we tell her as a grown-ups' secret. That Father Christmas is a story we keep alive so the little ones can enjoy it, and that from this year she can become one of his helpers too. She can choose Aris's present with us."),
  L("Θοδωρής", "m", "Μου αρέσει. Έτσι δεν χάνει τη μαγεία, απλώς αλλάζει ρόλο.", "I like it. That way she doesn't lose the magic, she just changes role."),
 ],
 "questions": [
  Q("Γιατί η Μυρτώ ρώτησε για τον Άγιο Βασίλη;", ["Το είδε σε μια ταινία", "Ένα παιδί στο σχολείο τής είπε ότι τα δώρα τα αγοράζουν οι γονείς", "Βρήκε τα δώρα κρυμμένα", "Ο αδερφός της τής το είπε"], 1, "Ένα παιδί στο σχολείο τής είπε ότι τα δώρα τα αγοράζουν οι γονείς"),
  Q("Τι ανησυχεί τον Θοδωρή;", ["Ότι η Μυρτώ θα κλάψει", "Ότι η Μυρτώ θα το πει στον μικρό της αδερφό", "Ότι θα θυμώσει η γιαγιά", "Ότι δεν θα θέλει πια δώρα"], 1, "θα το πει αμέσως στον Άρη"),
  Q("Τι προτείνει η Κατερίνα;", ["Να συνεχίσουν να λένε ψέματα", "Να της το πουν σαν μυστικό των μεγάλων και να γίνει βοηθός", "Να μη γιορτάσουν φέτος τα Χριστούγεννα", "Να ρωτήσουν τη δασκάλα"], 1, "να της το πούμε σαν μυστικό των μεγάλων"),
 ],
 "gloss": {"Άγιο Βασίλη": "Άγιος Βασίλης — Saint Basil (the Greek Father Christmas, who comes on New Year's Day)", "ευθέως": "ευθέως — directly, straight out", "υποψιάζεται": "υποψιάζομαι — to suspect", "κατάμουτρα": "κατάμουτρα — to someone's face", "κοροϊδεύαμε": "κοροϊδεύω — to make fun of, deceive", "μυστικό": "μυστικό — secret", "βοηθός": "βοηθός — helper", "μαγεία": "μαγεία — magic", "ρόλο": "ρόλος — role"},
})

ITEMS.append({
 "id": "l78-dia-agriochoiroi", "title": "Αγριογούρουνα στον κήπο", "title_en": "Wild boar in the garden", "type": "dialogue", "level": "B2",
 "context_el": "Δύο γείτονες σε ένα προάστιο κοντά στο βουνό συζητούν για τα αγριογούρουνα που κατεβαίνουν τη νύχτα στους κήπους.",
 "script": [
  L("Στράτος", "m", "Είδες τι έγινε απόψε; Μου όργωσαν ολόκληρο το γκαζόν και έφαγαν όλες τις πατάτες που είχα φυτέψει. Ήταν τουλάχιστον πέντε, μια μάνα με τα μικρά της.", "Did you see what happened last night? They dug up my whole lawn and ate all the potatoes I'd planted. There were at least five, a mother with her young."),
  L("Λίνα", "f", "Κι εμένα μου αναποδογύρισαν τους κάδους. Από την πυρκαγιά και μετά κατεβαίνουν όλο και πιο συχνά· στο βουνό δεν έχουν πια αρκετή τροφή, και εδώ βρίσκουν σκουπίδια και ποτισμένους κήπους.", "They knocked over my bins too. Since the fire they've been coming down more and more often; on the mountain there isn't enough food any more, and here they find rubbish and watered gardens."),
  L("Στράτος", "m", "Εγώ λέω να καλέσουμε τους κυνηγούς. Αν συνεχιστεί, κάποιος θα τραυματιστεί. Χθες το βράδυ ένα αυτοκίνητο παραλίγο να πέσει πάνω τους στη στροφή.", "I say we call the hunters. If this goes on, someone will get hurt. Last night a car nearly hit them on the bend."),
  L("Λίνα", "f", "Μέσα στον οικισμό απαγορεύεται το κυνήγι, και δικαίως. Το δασαρχείο λέει ότι το πιο αποτελεσματικό είναι να κλείνουμε καλά τους κάδους και να μην αφήνουμε φαγητό για τις γάτες έξω τη νύχτα. Και να βάλουμε περίφραξη με ηλεκτρικό σύρμα χαμηλής τάσης, που δεν τα βλάπτει, απλώς τα διώχνει.", "Hunting is banned inside the settlement, and rightly so. The forestry office says the most effective thing is to close the bins properly and not leave food out for the cats at night. And to put up fencing with low-voltage electric wire, which doesn't harm them, it just drives them away."),
 ],
 "questions": [
  Q("Τι έπαθε ο κήπος του Στράτου;", ["Κάηκε", "Τα αγριογούρουνα όργωσαν το γκαζόν και έφαγαν τις πατάτες", "Πλημμύρισε", "Τον κατέστρεψαν οι γάτες"], 1, "Μου όργωσαν ολόκληρο το γκαζόν και έφαγαν όλες τις πατάτες"),
  Q("Γιατί, κατά τη Λίνα, κατεβαίνουν πιο συχνά τα ζώα;", ["Γιατί είναι πάρα πολλά", "Γιατί μετά την πυρκαγιά δεν έχουν αρκετή τροφή στο βουνό", "Γιατί τα ταΐζουν οι κάτοικοι", "Γιατί φοβούνται τους κυνηγούς"], 1, "στο βουνό δεν έχουν πια αρκετή τροφή"),
  Q("Τι προτείνει το δασαρχείο;", ["Να έρθουν κυνηγοί", "Να κλείνουν καλά τους κάδους και να βάλουν περίφραξη χαμηλής τάσης", "Να μετακομίσουν οι κάτοικοι", "Να ταΐζουν τα ζώα στο βουνό"], 1, "να κλείνουμε καλά τους κάδους"),
 ],
 "gloss": {"αγριογούρουνα": "αγριογούρουνο — wild boar", "προάστιο": "προάστιο — suburb", "όργωσαν": "οργώνω — to plough, dig up", "γκαζόν": "γκαζόν — lawn", "αναποδογύρισαν": "αναποδογυρίζω — to knock over, overturn", "πυρκαγιά": "πυρκαγιά — (wild)fire", "τραυματιστεί": "τραυματίζομαι — to be injured", "οικισμό": "οικισμός — settlement", "δασαρχείο": "δασαρχείο — forestry office", "περίφραξη": "περίφραξη — fencing", "τάσης": "τάση — voltage"},
})

ITEMS.append({
 "id": "l78-int-odontotechnitria", "title": "Η οδοντοτεχνίτρια", "title_en": "The dental technician", "type": "interview", "level": "B2",
 "context_el": "Σε μια εκπομπή για τα λιγότερο γνωστά επαγγέλματα μιλά μια οδοντοτεχνίτρια.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι περισσότεροι δεν έχουμε ιδέα τι κάνει ένας οδοντοτεχνίτης. Μας εξηγείτε;", "Most of us have no idea what a dental technician does. Can you explain?"),
  L("Οδοντοτεχνίτρια", "f", "Φτιάχνουμε όλα όσα μπαίνουν στο στόμα και δεν είναι φυσικά δόντια: στεφάνες, γέφυρες, οδοντοστοιχίες. Δεν βλέπουμε σχεδόν ποτέ τον ασθενή. Ο οδοντίατρος μάς στέλνει ένα αποτύπωμα ή, όλο και πιο συχνά, μια ψηφιακή σάρωση, και εμείς δουλεύουμε στο εργαστήριο.", "We make everything that goes in the mouth and isn't natural teeth: crowns, bridges, dentures. We almost never see the patient. The dentist sends us an impression or, more and more often, a digital scan, and we work in the laboratory."),
  L("Δημοσιογράφος", "m", "Η τεχνολογία έχει αλλάξει πολύ τη δουλειά σας;", "Has technology changed your work a lot?"),
  L("Οδοντοτεχνίτρια", "f", "Τεράστια. Πολλές στεφάνες σχεδιάζονται πια στον υπολογιστή και κόβονται από μηχανήματα. Αλλά το πιο δύσκολο κομμάτι παραμένει χειροποίητο: το χρώμα. Κανένα δόντι δεν είναι απλώς άσπρο. Έχει αποχρώσεις, διαφάνειες, μικρές ατέλειες. Αν ένα ψεύτικο δόντι είναι τέλειο, φαίνεται αμέσως ψεύτικο.", "Enormously. Many crowns are now designed on the computer and cut by machines. But the hardest part is still done by hand: the colour. No tooth is simply white. It has shades, translucencies, small imperfections. If a false tooth is perfect, it immediately looks false."),
 ],
 "questions": [
  Q("Τι φτιάχνει ένας οδοντοτεχνίτης;", ["Οδοντόβουρτσες", "Στεφάνες, γέφυρες και οδοντοστοιχίες", "Φάρμακα για τα δόντια", "Εργαλεία για οδοντιάτρους"], 1, "στεφάνες, γέφυρες, οδοντοστοιχίες"),
  Q("Πώς δουλεύει με τον ασθενή;", ["Τον βλέπει κάθε εβδομάδα", "Σχεδόν ποτέ δεν τον βλέπει· δουλεύει με αποτύπωμα ή ψηφιακή σάρωση", "Τον εξετάζει μαζί με τον οδοντίατρο", "Του τηλεφωνεί για οδηγίες"], 1, "Δεν βλέπουμε σχεδόν ποτέ τον ασθενή"),
  Q("Γιατί ένα «τέλειο» ψεύτικο δόντι δεν είναι καλό;", ["Γιατί σπάει εύκολα", "Γιατί φαίνεται αμέσως ψεύτικο", "Γιατί κοστίζει πολύ", "Γιατί πονάει"], 1, "Αν ένα ψεύτικο δόντι είναι τέλειο, φαίνεται αμέσως ψεύτικο"),
 ],
 "gloss": {"οδοντοτεχνίτρια": "οδοντοτεχνίτρια — dental technician (woman)", "στεφάνες": "στεφάνη — (dental) crown", "γέφυρες": "γέφυρα — bridge", "οδοντοστοιχίες": "οδοντοστοιχία — denture", "αποτύπωμα": "αποτύπωμα — impression, mould", "σάρωση": "σάρωση — scan", "χειροποίητο": "χειροποίητος — handmade", "αποχρώσεις": "απόχρωση — shade", "διαφάνειες": "διαφάνεια — translucency", "ατέλειες": "ατέλεια — imperfection"},
})

ITEMS.append({
 "id": "l78-rep-tzitzikia", "title": "Τα τζιτζίκια του καλοκαιριού", "title_en": "The cicadas of summer", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από μια ραδιοφωνική εκπομπή για τη φύση.",
 "script": [
  L("Ρεπόρτερ", "m", "Για τους περισσότερους Έλληνες, ο ήχος του καλοκαιριού είναι το τζιτζίκι. Λίγοι όμως ξέρουν ότι τραγουδούν μόνο τα αρσενικά. Ο ήχος δεν βγαίνει από το στόμα, αλλά από δύο μεμβράνες στην κοιλιά τους, που δονούνται εκατοντάδες φορές το δευτερόλεπτο. Σκοπός τους είναι να προσελκύσουν τα θηλυκά.", "For most Greeks, the sound of summer is the cicada. But few know that only the males sing. The sound doesn't come from the mouth, but from two membranes on their abdomen, which vibrate hundreds of times a second. Their aim is to attract the females."),
  L("Ρεπόρτερ", "m", "Το πιο εντυπωσιακό, ωστόσο, είναι ο κύκλος ζωής τους. Το τζιτζίκι που ακούμε στο πεύκο έχει περάσει τα περισσότερα χρόνια της ζωής του κάτω από τη γη, ως νύμφη, πίνοντας τον χυμό από τις ρίζες των δέντρων. Βγαίνει στην επιφάνεια μόνο για λίγες εβδομάδες, για να ζευγαρώσει και να πεθάνει.", "The most impressive thing, however, is their life cycle. The cicada we hear in the pine tree has spent most of its life underground, as a nymph, drinking sap from the roots of trees. It comes up to the surface only for a few weeks, to mate and die."),
  L("Ρεπόρτερ", "m", "Ο Αίσωπος, στον γνωστό μύθο, έκανε το τζιτζίκι σύμβολο της τεμπελιάς απέναντι στο εργατικό μυρμήγκι. Οι αρχαίοι Αθηναίοι, όμως, το αγαπούσαν· το θεωρούσαν σύμβολο της μουσικής, και κάποιοι φορούσαν χρυσά τζιτζίκια στα μαλλιά τους.", "Aesop, in the well-known fable, made the cicada a symbol of laziness compared to the hard-working ant. The ancient Athenians, however, loved it; they considered it a symbol of music, and some wore golden cicadas in their hair."),
 ],
 "questions": [
  Q("Ποια τζιτζίκια τραγουδούν;", ["Μόνο τα θηλυκά", "Μόνο τα αρσενικά", "Όλα", "Μόνο τα νεαρά"], 1, "τραγουδούν μόνο τα αρσενικά"),
  Q("Πού περνά το τζιτζίκι τα περισσότερα χρόνια της ζωής του;", ["Στα κλαδιά των πεύκων", "Κάτω από τη γη, ως νύμφη", "Μέσα στο νερό", "Σε άλλες χώρες"], 1, "κάτω από τη γη, ως νύμφη"),
  Q("Πώς έβλεπαν το τζιτζίκι οι αρχαίοι Αθηναίοι;", ["Ως σύμβολο της τεμπελιάς", "Ως σύμβολο της μουσικής", "Ως κακό οιωνό", "Ως φαγητό"], 1, "το θεωρούσαν σύμβολο της μουσικής"),
 ],
 "gloss": {"τζιτζίκι": "τζιτζίκι — cicada", "αρσενικά": "αρσενικός — male", "μεμβράνες": "μεμβράνη — membrane", "δονούνται": "δονούμαι — to vibrate", "προσελκύσουν": "προσελκύω — to attract", "νύμφη": "νύμφη — nymph (insect stage)", "χυμό": "χυμός — sap, juice", "ζευγαρώσει": "ζευγαρώνω — to mate", "τεμπελιάς": "τεμπελιά — laziness", "μυρμήγκι": "μυρμήγκι — ant"},
})

ITEMS.append({
 "id": "l78-rep-alonia", "title": "Τα αλώνια των Κυκλάδων", "title_en": "The threshing floors of the Cyclades", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τα παλιά αλώνια σε ένα νησί των Κυκλάδων.",
 "script": [
  L("Ρεπόρτερ", "f", "Περπατώντας στα μονοπάτια της Σίφνου, ο επισκέπτης συναντά συχνά μεγάλους πέτρινους κύκλους, στρωμένους με πλάκες, πάνω σε λόφους ή στις άκρες των χωραφιών. Είναι τα αλώνια, όπου μέχρι τη δεκαετία του εξήντα οι αγρότες χώριζαν το σιτάρι από το άχυρο.", "Walking the paths of Sifnos, visitors often come across large stone circles, paved with slabs, on hills or at the edges of fields. These are the threshing floors, where until the sixties farmers separated the wheat from the straw."),
  L("Ρεπόρτερ", "f", "Τον Ιούλιο άπλωναν τα στάχυα στο αλώνι, και ζώα, συνήθως άλογα ή γαϊδούρια, γύριζαν γύρω γύρω πάνω τους για ώρες. Μετά οι αγρότες περίμεναν τον αέρα: πετούσαν το μείγμα ψηλά με ξύλινα δικράνια, το ελαφρύ άχυρο το έπαιρνε ο αέρας και ο βαρύς καρπός έπεφτε κάτω. Γι’ αυτό τα αλώνια χτίζονταν σε ανεμοδαρμένα σημεία.", "In July they spread the ears of wheat on the threshing floor, and animals, usually horses or donkeys, walked round and round on them for hours. Then the farmers waited for the wind: they tossed the mixture high with wooden pitchforks, the light straw was carried off by the wind and the heavy grain fell down. That's why threshing floors were built in windswept spots."),
  L("Ρεπόρτερ", "f", "Σήμερα τα περισσότερα είναι εγκαταλειμμένα, αλλά ένας τοπικός σύλλογος έχει αρχίσει να τα καθαρίζει και να τα σημαδεύει σε χάρτες πεζοπορίας. Κάθε καλοκαίρι, σε ένα από αυτά, οργανώνεται μια γιορτή όπου οι παλιότεροι δείχνουν στα παιδιά πώς γινόταν το αλώνισμα.", "Today most are abandoned, but a local association has begun clearing them and marking them on hiking maps. Every summer, on one of them, a festival is held where older people show the children how threshing was done."),
 ],
 "questions": [
  Q("Σε τι χρησίμευαν τα αλώνια;", ["Για χορούς", "Για να χωρίζουν το σιτάρι από το άχυρο", "Για να μαζεύουν νερό", "Για να βόσκουν τα ζώα"], 1, "οι αγρότες χώριζαν το σιτάρι από το άχυρο"),
  Q("Γιατί τα αλώνια χτίζονταν σε ανεμοδαρμένα σημεία;", ["Για να έχουν θέα", "Γιατί χρειαζόταν αέρας για να φύγει το ελαφρύ άχυρο", "Για να είναι μακριά από τα σπίτια", "Γιατί εκεί υπήρχαν πέτρες"], 1, "το ελαφρύ άχυρο το έπαιρνε ο αέρας"),
  Q("Τι κάνει σήμερα ένας τοπικός σύλλογος;", ["Τα πουλάει σε ξένους", "Τα καθαρίζει και τα σημαδεύει σε χάρτες πεζοπορίας", "Χτίζει καινούργια", "Καλλιεργεί σιτάρι σε όλα"], 1, "έχει αρχίσει να τα καθαρίζει και να τα σημαδεύει σε χάρτες πεζοπορίας"),
 ],
 "gloss": {"αλώνια": "αλώνι — threshing floor", "πλάκες": "πλάκα — (stone) slab", "σιτάρι": "σιτάρι — wheat", "άχυρο": "άχυρο — straw", "στάχυα": "στάχυ — ear (of wheat)", "δικράνια": "δικράνι — wooden (two-pronged) pitchfork", "καρπός": "καρπός — grain", "ανεμοδαρμένα": "ανεμοδαρμένος — windswept", "πεζοπορίας": "πεζοπορία — hiking", "αλώνισμα": "αλώνισμα — threshing"},
})

ITEMS.append({
 "id": "l78-mono-paidikos-filos", "title": "Ξαναβρήκα τον παιδικό μου φίλο", "title_en": "I found my childhood friend again", "type": "monologue", "level": "B2",
 "context_el": "Ένας άντρας διηγείται σε ένα podcast πώς ξαναβρήκε έναν φίλο από το δημοτικό.",
 "script": [
  L("Βαγγέλης", "m", "Με τον Τάσο ήμασταν αχώριστοι από την πρώτη δημοτικού. Καθόμασταν στο ίδιο θρανίο, παίζαμε μπάλα στην ίδια αλάνα, και τα καλοκαίρια χανόμασταν μαζί στο ποτάμι. Στην πέμπτη τάξη ο πατέρας του πήρε μετάθεση στη Θράκη, και μια μέρα απλώς δεν ήρθε στο σχολείο.", "Tasos and I were inseparable from the first year of primary school. We sat at the same desk, played football on the same patch of waste ground, and in summer we disappeared together down by the river. In fifth grade his father was transferred to Thrace, and one day he simply didn't come to school."),
  L("Βαγγέλης", "m", "Για χρόνια σκεφτόμουν να τον ψάξω, αλλά δεν θυμόμουν ούτε το επώνυμό του σωστά. Πέρσι η κόρη μου ανέβασε σε μια ομάδα του χωριού μια παλιά σχολική φωτογραφία. Μέσα σε δύο ώρες κάποιος έγραψε στα σχόλια: «Ο δεύτερος από αριστερά είναι ο θείος μου ο Τάσος!»", "For years I thought about looking for him, but I couldn't even remember his surname correctly. Last year my daughter posted an old school photo in a village group. Within two hours someone wrote in the comments: 'The second from the left is my uncle Tasos!'"),
  L("Βαγγέλης", "m", "Συναντηθήκαμε σε ένα καφενείο στη Λάρισα, στη μέση της απόστασης. Φοβόμουν ότι δεν θα είχαμε τι να πούμε, μετά από σαράντα χρόνια. Καθίσαμε πέντε ώρες. Στο τέλος μού έδωσε ένα κουτάκι: μέσα ήταν μια γυάλινη μπίλια που του είχα χαρίσει το τελευταίο μας καλοκαίρι.", "We met in a café in Larissa, halfway between us. I was afraid we'd have nothing to say after forty years. We sat for five hours. At the end he gave me a little box: inside was a glass marble I'd given him our last summer."),
 ],
 "questions": [
  Q("Γιατί έφυγε ο Τάσος από το σχολείο;", ["Άλλαξε σχολείο για να παίζει μπάλα", "Ο πατέρας του πήρε μετάθεση στη Θράκη", "Αρρώστησε", "Μάλωσαν οι οικογένειες"], 1, "ο πατέρας του πήρε μετάθεση στη Θράκη"),
  Q("Πώς τον ξαναβρήκε ο Βαγγέλης;", ["Από τον τηλεφωνικό κατάλογο", "Μέσα από μια παλιά σχολική φωτογραφία σε μια ομάδα του χωριού", "Τον συνάντησε τυχαία", "Μέσα από το σχολείο"], 1, "η κόρη μου ανέβασε σε μια ομάδα του χωριού μια παλιά σχολική φωτογραφία"),
  Q("Τι του έδωσε ο Τάσος στο τέλος της συνάντησης;", ["Μια φωτογραφία", "Μια γυάλινη μπίλια που του είχε χαρίσει ο Βαγγέλης", "Ένα γράμμα", "Μια μπάλα"], 1, "μια γυάλινη μπίλια που του είχα χαρίσει το τελευταίο μας καλοκαίρι"),
 ],
 "gloss": {"αχώριστοι": "αχώριστος — inseparable", "θρανίο": "θρανίο — school desk", "αλάνα": "αλάνα — patch of waste ground (where children play)", "μετάθεση": "μετάθεση — (job) transfer", "επώνυμό": "επώνυμο — surname", "ανέβασε": "ανεβάζω — to post, upload", "σχόλια": "σχόλιο — comment", "καφενείο": "καφενείο — (traditional) café", "μπίλια": "μπίλια — marble (toy)", "χαρίσει": "χαρίζω — to give (as a gift)"},
})

ITEMS.append({
 "id": "l78-c1-gaidouria-santorinis", "title": "Τα γαϊδουράκια της Σαντορίνης και η ηθική των ζώων εργασίας", "title_en": "The donkeys of Santorini and the ethics of working animals", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε απόσπασμα από μια ομιλία μιας κτηνιάτρου σε ένα συνέδριο για την ευζωία των ζώων.",
 "script": [
  L("Κτηνίατρος", "f", "Η εικόνα του γαϊδουριού που ανεβάζει τουρίστες από το παλιό λιμάνι στα Φηρά, περίπου εξακόσια σκαλοπάτια, έχει γίνει σχεδόν σύμβολο της Σαντορίνης. Τα τελευταία χρόνια, όμως, έχει γίνει και σύμβολο κάτι άλλου: της έντασης ανάμεσα στην παράδοση και την ευζωία των ζώων. Φωτογραφίες με εξαντλημένα ζώα και πληγές από τα σαμάρια έκαναν τον γύρο του κόσμου.", "The image of the donkey carrying tourists up from the old port to Fira, about six hundred steps, has become almost a symbol of Santorini. In recent years, though, it has also become a symbol of something else: the tension between tradition and animal welfare. Photos of exhausted animals with sores from their saddles went round the world."),
  L("Κτηνίατρος", "f", "Η πολιτεία αντέδρασε με μια εγκύκλιο που απαγορεύει να μεταφέρουν άτομα πάνω από εκατό κιλά και ορίζει ώρες ξεκούρασης και σκιά. Είναι ένα βήμα. Δεν πιστεύω, ωστόσο, ότι η απλή απαγόρευση είναι πανάκεια. Για πολλές οικογένειες του νησιού, τα ζώα αυτά είναι κομμάτι μιας κληρονομιάς αιώνων, και η επιβίωσή τους εξαρτάται από το εισόδημα που φέρνουν.", "The state responded with a circular that bans them from carrying people over one hundred kilos and sets rest hours and shade. It is a step. I do not believe, however, that a simple ban is a panacea. For many families on the island, these animals are part of a centuries-old heritage, and their survival depends on the income they bring."),
  L("Κτηνίατρος", "f", "Το ερώτημα, λοιπόν, δεν είναι αν τα ζώα πρέπει να δουλεύουν, αλλά υπό ποιους όρους. Ένα ζώο που τρέφεται σωστά, εξετάζεται τακτικά και δεν υπερφορτώνεται μπορεί να ζήσει μια αξιοπρεπή ζωή εργασίας. Και, παραδόξως, ο πιο αποτελεσματικός μοχλός πίεσης δεν είναι ο νόμος, αλλά ο ίδιος ο επισκέπτης: αν αρνηθεί να ανέβει σε ένα ζώο που φαίνεται ταλαιπωρημένο, ο ιδιοκτήτης θα καταλάβει γρήγορα το μήνυμα.", "The question, then, is not whether animals should work, but under what conditions. An animal that is properly fed, regularly examined and not overloaded can live a dignified working life. And, paradoxically, the most effective lever of pressure is not the law, but the visitor himself: if he refuses to get on an animal that looks ill-treated, the owner will quickly get the message."),
 ],
 "questions": [
  Q("Τι έκανε το θέμα γνωστό διεθνώς;", ["Ένα ντοκιμαντέρ για το νησί", "Φωτογραφίες με εξαντλημένα ζώα και πληγές από τα σαμάρια", "Μια απεργία των ιδιοκτητών", "Ένας νέος νόμος της Ευρωπαϊκής Ένωσης"], 1, "Φωτογραφίες με εξαντλημένα ζώα και πληγές από τα σαμάρια έκαναν τον γύρο του κόσμου"),
  Q("Γιατί η κτηνίατρος δεν θεωρεί την απαγόρευση πανάκεια;", ["Γιατί δεν εφαρμόζεται ποτέ", "Γιατί τα ζώα είναι κομμάτι μιας κληρονομιάς και πηγή εισοδήματος για πολλές οικογένειες", "Γιατί τα ζώα δεν κουράζονται", "Γιατί οι τουρίστες δεν την ξέρουν"], 1, "η επιβίωσή τους εξαρτάται από το εισόδημα που φέρνουν"),
  Q("Ποιος είναι, κατά την ομιλήτρια, ο πιο αποτελεσματικός μοχλός πίεσης;", ["Ο νόμος", "Ο ίδιος ο επισκέπτης", "Οι κτηνίατροι", "Ο δήμος"], 1, "ο πιο αποτελεσματικός μοχλός πίεσης δεν είναι ο νόμος, αλλά ο ίδιος ο επισκέπτης"),
 ],
 "gloss": {"γαϊδουριού": "γαϊδούρι — donkey", "ευζωία": "ευζωία — welfare, well-being", "εξαντλημένα": "εξαντλημένος — exhausted", "πληγές": "πληγή — sore, wound", "σαμάρια": "σαμάρι — packsaddle", "εγκύκλιο": "εγκύκλιος — (official) circular", "πανάκεια": "πανάκεια — panacea", "υπερφορτώνεται": "υπερφορτώνω — to overload", "αξιοπρεπή": "αξιοπρεπής — dignified", "μοχλός πίεσης": "μοχλός πίεσης — lever of pressure", "ταλαιπωρημένο": "ταλαιπωρημένος — ill-treated, worn out"},
})

ITEMS.append({
 "id": "l78-c1-psifiaki-klironomia", "title": "Η ψηφιακή μας κληρονομιά", "title_en": "Our digital inheritance", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για το δίκαιο και την τεχνολογία, μια δικηγόρος μιλά για την ψηφιακή κληρονομιά: τι γίνεται με τους λογαριασμούς μας μετά τον θάνατο.",
 "script": [
  L("Δημοσιογράφος", "m", "Όταν πεθαίνει κάποιος, οι συγγενείς ξέρουν τι να κάνουν με το σπίτι ή τον τραπεζικό λογαριασμό. Τι γίνεται όμως με τις φωτογραφίες στο νέφος, το ηλεκτρονικό ταχυδρομείο, τα μέσα κοινωνικής δικτύωσης;", "When someone dies, relatives know what to do with the house or the bank account. But what happens with the photos in the cloud, the email, the social media?"),
  L("Δικηγόρος", "f", "Εδώ βρισκόμαστε σε μια γκρίζα ζώνη. Το κληρονομικό δίκαιο γράφτηκε για πράγματα που μπορείς να αγγίξεις. Οι ψηφιακοί λογαριασμοί, αντίθετα, διέπονται συνήθως από τους όρους χρήσης της κάθε εταιρείας, τους οποίους κανείς μας δεν διαβάζει. Έτσι, ένας γονιός μπορεί να μην έχει πρόσβαση στις φωτογραφίες του παιδιού του, ακόμα κι αν είναι ο μοναδικός κληρονόμος.", "Here we are in a grey zone. Inheritance law was written for things you can touch. Digital accounts, by contrast, are usually governed by each company's terms of use, which none of us reads. So a parent may not have access to their child's photos, even if they are the sole heir."),
  L("Δημοσιογράφος", "m", "Και τι προτείνετε στους ακροατές μας;", "And what do you suggest to our listeners?"),
  L("Δικηγόρος", "f", "Κάτι απλό, που όμως σχεδόν κανείς δεν κάνει: να συντάξουν μια ψηφιακή διαθήκη. Δεν χρειάζεται να είναι επίσημο έγγραφο· αρκεί ένας κατάλογος με τους λογαριασμούς και τι θέλουν να γίνει με τον καθένα: να διαγραφεί, να μετατραπεί σε λογαριασμό μνήμης, να παραδοθεί σε κάποιον. Πολλές πλατφόρμες, εξάλλου, επιτρέπουν ήδη να ορίσεις έναν «διάδοχο». Το κρίσιμο είναι να το σκεφτούμε όσο ζούμε, γιατί μετά οι αγαπημένοι μας θα βρεθούν αντιμέτωποι με έναν γραφειοκρατικό λαβύρινθο σε μια στιγμή πένθους.", "Something simple, which almost nobody does, though: draw up a digital will. It doesn't need to be an official document; a list of accounts and what they want to happen to each one is enough: to be deleted, turned into a memorial account, handed over to someone. Many platforms, moreover, already let you name a 'successor'. The crucial thing is to think about it while we're alive, because afterwards our loved ones will face a bureaucratic labyrinth at a moment of grief."),
 ],
 "questions": [
  Q("Γιατί η δικηγόρος μιλά για «γκρίζα ζώνη»;", ["Γιατί οι λογαριασμοί είναι παράνομοι", "Γιατί το κληρονομικό δίκαιο γράφτηκε για υλικά πράγματα και οι λογαριασμοί διέπονται από τους όρους των εταιρειών", "Γιατί οι εταιρείες κλείνουν συχνά", "Γιατί οι φωτογραφίες χάνονται"], 1, "Το κληρονομικό δίκαιο γράφτηκε για πράγματα που μπορείς να αγγίξεις"),
  Q("Τι μπορεί να συμβεί σε έναν γονιό, σύμφωνα με τη δικηγόρο;", ["Να χρεωθεί για τους λογαριασμούς", "Να μην έχει πρόσβαση στις φωτογραφίες του παιδιού του, ακόμα κι αν είναι ο μοναδικός κληρονόμος", "Να χάσει το σπίτι", "Να πρέπει να πληρώσει φόρο"], 1, "ένας γονιός μπορεί να μην έχει πρόσβαση στις φωτογραφίες του παιδιού του"),
  Q("Τι είναι, κατά τη δικηγόρο, μια «ψηφιακή διαθήκη»;", ["Ένα επίσημο έγγραφο από συμβολαιογράφο", "Ένας κατάλογος με τους λογαριασμούς και τι θέλουμε να γίνει με τον καθένα", "Μια εφαρμογή που διαγράφει τα πάντα", "Ένας κωδικός για την τράπεζα"], 1, "αρκεί ένας κατάλογος με τους λογαριασμούς και τι θέλουν να γίνει με τον καθένα"),
 ],
 "gloss": {"κληρονομιά": "κληρονομιά — inheritance, legacy", "νέφος": "νέφος — cloud (computing)", "γκρίζα ζώνη": "γκρίζα ζώνη — grey area", "κληρονομικό δίκαιο": "κληρονομικό δίκαιο — inheritance law", "διέπονται": "διέπομαι — to be governed (by rules)", "όρους χρήσης": "όροι χρήσης — terms of use", "κληρονόμος": "κληρονόμος — heir", "διαθήκη": "διαθήκη — will", "διάδοχο": "διάδοχος — successor", "λαβύρινθο": "λαβύρινθος — labyrinth", "πένθους": "πένθος — grief, mourning"},
})

rnd = random.Random(78)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-78.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
