# Source for library/listening/listening-34.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l34.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l34-ann-anaklisi", "title": "Ανάκληση προϊόντος στο σούπερ μάρκετ", "title_en": "A product recall at the supermarket", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα ενός σούπερ μάρκετ.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί πελάτες, σας ενημερώνουμε ότι, ύστερα από οδηγία του Ενιαίου Φορέα Ελέγχου Τροφίμων, ανακαλείται μια παρτίδα ταχινιού ολικής άλεσης σε βάζο των τριακοσίων γραμμαρίων, με ημερομηνία λήξης τον Μάρτιο του επόμενου έτους. Σε δείγματα της παρτίδας βρέθηκε σαλμονέλα.", "Dear customers, we inform you that, following an instruction from the Hellenic Food Authority, a batch of wholegrain tahini in a three-hundred-gram jar, with an expiry date of March next year, is being recalled. Salmonella was found in samples of the batch."),
  L("Εκφωνήτρια", "f", "Όσοι έχετε αγοράσει το συγκεκριμένο προϊόν, παρακαλείστε να μην το καταναλώσετε. Μπορείτε να το επιστρέψετε σε οποιοδήποτε κατάστημά μας, ακόμη και ανοιγμένο και χωρίς απόδειξη, και θα σας επιστραφεί ολόκληρο το ποσό.", "Those of you who have bought this product are asked not to consume it. You can return it to any of our shops, even opened and without a receipt, and the whole amount will be refunded."),
  L("Εκφωνήτρια", "f", "Οι υπόλοιπες παρτίδες και τα άλλα προϊόντα της ίδιας εταιρείας είναι απολύτως ασφαλή. Για περισσότερες πληροφορίες, απευθυνθείτε στο κέντρο εξυπηρέτησης πελατών, δίπλα στα ταμεία. Σας ευχαριστούμε.", "The other batches and the company's other products are completely safe. For more information, please go to the customer service desk next to the tills. Thank you."),
 ],
 "questions": [
  Q("Γιατί ανακαλείται το ταχίνι;", ["Γιατί έληξε", "Γιατί βρέθηκε σαλμονέλα σε δείγματα", "Γιατί η ετικέτα ήταν λάθος", "Γιατί είχε σπασμένα βάζα"], 1, "Σε δείγματα της παρτίδας βρέθηκε σαλμονέλα"),
  Q("Τι ισχύει για την επιστροφή του προϊόντος;", ["Χρειάζεται απόδειξη", "Γίνεται δεκτό ακόμη και ανοιγμένο και χωρίς απόδειξη", "Μόνο στο κατάστημα όπου αγοράστηκε", "Δίνεται μόνο δωροεπιταγή"], 1, "ακόμη και ανοιγμένο και χωρίς απόδειξη"),
  Q("Τι λέει η ανακοίνωση για τα άλλα προϊόντα της εταιρείας;", ["Ανακαλούνται κι αυτά", "Είναι απολύτως ασφαλή", "Ελέγχονται ακόμη", "Πωλούνται με έκπτωση"], 1, "τα άλλα προϊόντα της ίδιας εταιρείας είναι απολύτως ασφαλή"),
 ],
 "gloss": {"ανακαλείται": "ανακαλούμαι — to be recalled", "παρτίδα": "παρτίδα — batch", "ταχινιού": "ταχίνι — tahini", "ολικής άλεσης": "ολικής άλεσης — wholegrain", "βάζο": "βάζο — jar", "ημερομηνία λήξης": "ημερομηνία λήξης — expiry date", "δείγματα": "δείγμα — sample", "σαλμονέλα": "σαλμονέλα — salmonella", "να μην το καταναλώσετε": "καταναλώνω — to consume", "απόδειξη": "απόδειξη — receipt", "απευθυνθείτε": "απευθύνομαι — to turn to, contact"},
})

ITEMS.append({
 "id": "l34-vm-odeio", "title": "Μήνυμα από το ωδείο", "title_en": "A message from the music school", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τη γραμματεία ενός ωδείου.",
 "script": [
  L("Γραμματέας", "f", "Καλησπέρα σας, σας τηλεφωνώ από το Ωδείο «Αρμονία» για τις εξετάσεις πιάνου του γιου σας. Η επιτροπή που θα έρθει από την Αθήνα δεν μπορεί την ημερομηνία που είχαμε ορίσει, γι' αυτό οι εξετάσεις μεταφέρονται μία εβδομάδα αργότερα, στις δεκαέξι Ιουνίου.", "Good evening, I'm calling from the «Harmonia» music school about your son's piano exams. The committee coming from Athens can't make the date we had set, so the exams are moving one week later, to the sixteenth of June."),
  L("Γραμματέας", "f", "Ο Άγγελος θα παίξει στις έντεκα και μισή, αλλά καλό είναι να έρθει μισή ώρα νωρίτερα, για να ζεσταθεί σε μια από τις αίθουσες μελέτης. Πρέπει να έχει μαζί του τις παρτιτούρες σε δύο αντίτυπα, ένα για τον ίδιο και ένα για την επιτροπή.", "Angelos will play at half past eleven, but it's best if he comes half an hour earlier to warm up in one of the practice rooms. He must bring his sheet music in two copies, one for himself and one for the committee."),
  L("Γραμματέας", "f", "Επίσης, θα σας παρακαλούσα να εξοφλήσετε τα εξέταστρα, εξήντα ευρώ, μέχρι το τέλος του μήνα. Μπορείτε να πληρώσετε στη γραμματεία ή με κατάθεση στον λογαριασμό του ωδείου. Ευχαριστώ πολύ.", "Also, I'd ask you to pay the exam fee, sixty euros, by the end of the month. You can pay at the office or by bank deposit into the school's account. Thank you very much."),
 ],
 "questions": [
  Q("Γιατί μεταφέρονται οι εξετάσεις;", ["Γιατί αρρώστησε ο δάσκαλος", "Γιατί η επιτροπή δεν μπορεί την αρχική ημερομηνία", "Γιατί η αίθουσα ανακαινίζεται", "Γιατί ο Άγγελος έχει σχολικές εξετάσεις"], 1, "Η επιτροπή που θα έρθει από την Αθήνα δεν μπορεί την ημερομηνία"),
  Q("Γιατί πρέπει ο Άγγελος να έρθει νωρίτερα;", ["Για να γνωρίσει την επιτροπή", "Για να ζεσταθεί σε μια αίθουσα μελέτης", "Για να πληρώσει τα εξέταστρα", "Για να κουρδίσει το πιάνο"], 1, "για να ζεσταθεί σε μια από τις αίθουσες μελέτης"),
  Q("Τι πρέπει να φέρει μαζί του;", ["Το βιβλίο θεωρίας", "Τις παρτιτούρες σε δύο αντίτυπα", "Μια βεβαίωση από το σχολείο", "Την απόδειξη πληρωμής"], 1, "τις παρτιτούρες σε δύο αντίτυπα"),
 ],
 "gloss": {"ωδείου": "ωδείο — conservatory, music school", "γραμματεία": "γραμματεία — office, secretariat", "επιτροπή": "επιτροπή — committee, panel", "είχαμε ορίσει": "ορίζω — to set, fix", "να ζεσταθεί": "ζεσταίνομαι — to warm up", "αίθουσες μελέτης": "αίθουσα μελέτης — practice room", "παρτιτούρες": "παρτιτούρα — sheet music, score", "αντίτυπα": "αντίτυπο — copy", "να εξοφλήσετε": "εξοφλώ — to pay off", "εξέταστρα": "εξέταστρα — exam fee", "κατάθεση": "κατάθεση — deposit"},
})

ITEMS.append({
 "id": "l34-dia-kep", "title": "Στο ΚΕΠ για ένα πιστοποιητικό", "title_en": "At the citizens' service centre for a certificate", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα Κέντρο Εξυπηρέτησης Πολιτών (ΚΕΠ).",
 "script": [
  L("Πολίτισσα", "f", "Καλημέρα. Χρειάζομαι ένα πιστοποιητικό οικογενειακής κατάστασης για να το καταθέσω στο πανεπιστήμιο της κόρης μου, που θα κάνει αίτηση για φοιτητική εστία.", "Good morning. I need a family status certificate to submit to my daughter's university; she's going to apply for student housing."),
  L("Υπάλληλος", "m", "Μάλιστα. Ξέρετε ότι μπορείτε να το εκδώσετε και μόνη σας από το σπίτι, μέσα από την ψηφιακή πύλη του Δημοσίου, με τους κωδικούς του Taxisnet; Βγαίνει αμέσως και έχει την ίδια ισχύ.", "I see. Did you know you can also issue it yourself from home, through the government's digital portal, with your Taxisnet codes? It comes out immediately and has the same validity."),
  L("Πολίτισσα", "f", "Το δοκίμασα, αλλά μου βγάζει μήνυμα ότι λείπει η εγγραφή του γάμου μου. Παντρευτήκαμε στο εξωτερικό, στη Γερμανία.", "I tried, but it gives me a message that my marriage registration is missing. We got married abroad, in Germany."),
  L("Υπάλληλος", "m", "Α, τότε ο γάμος σας πρέπει πρώτα να καταχωριστεί στο Ειδικό Ληξιαρχείο Αθηνών. Θα σας κάνω την αίτηση από εδώ· χρειάζομαι την ταυτότητά σας και τη ληξιαρχική πράξη γάμου από τη Γερμανία, με επικύρωση και μετάφραση. Η διαδικασία κρατάει περίπου έναν μήνα, και μετά θα μπορείτε να βγάλετε το πιστοποιητικό κανονικά.", "Ah, then your marriage must first be registered at the Special Registry Office in Athens. I'll make the application for you from here; I need your ID card and the marriage certificate from Germany, with an apostille and translation. The process takes about a month, and afterwards you'll be able to get the certificate as normal."),
 ],
 "questions": [
  Q("Γιατί χρειάζεται η πολίτισσα το πιστοποιητικό;", ["Για να βγάλει διαβατήριο", "Για την αίτηση της κόρης της για φοιτητική εστία", "Για να παντρευτεί", "Για τη φορολογική της δήλωση"], 1, "για να το καταθέσω στο πανεπιστήμιο της κόρης μου"),
  Q("Γιατί δεν μπόρεσε να το εκδώσει από το σπίτι;", ["Γιατί δεν είχε κωδικούς", "Γιατί λείπει η εγγραφή του γάμου της, που έγινε στο εξωτερικό", "Γιατί η ιστοσελίδα δεν λειτουργούσε", "Γιατί δεν έχει υπολογιστή"], 1, "λείπει η εγγραφή του γάμου μου"),
  Q("Τι πρέπει να γίνει πρώτα;", ["Να ξαναπαντρευτούν στην Ελλάδα", "Να καταχωριστεί ο γάμος στο Ειδικό Ληξιαρχείο Αθηνών", "Να πάει η ίδια στη Γερμανία", "Να πληρώσει πρόστιμο"], 1, "ο γάμος σας πρέπει πρώτα να καταχωριστεί στο Ειδικό Ληξιαρχείο Αθηνών"),
 ],
 "gloss": {"πιστοποιητικό": "πιστοποιητικό — certificate", "οικογενειακής κατάστασης": "οικογενειακή κατάσταση — family status", "να το καταθέσω": "καταθέτω — to submit", "να το εκδώσετε": "εκδίδω — to issue", "ψηφιακή πύλη": "ψηφιακή πύλη — digital portal", "κωδικούς": "κωδικός — code, password", "ισχύ": "ισχύς — validity, force", "εγγραφή": "εγγραφή — registration", "να καταχωριστεί": "καταχωρίζομαι — to be registered", "Ληξιαρχείο": "ληξιαρχείο — registry office", "ληξιαρχική πράξη γάμου": "ληξιαρχική πράξη γάμου — marriage certificate", "επικύρωση": "επικύρωση — certification, apostille"},
})

ITEMS.append({
 "id": "l34-dia-ano-poli", "title": "Ψάχνοντας τον δρόμο στην Άνω Πόλη", "title_en": "Looking for the way in the Upper Town", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο ανάμεσα σε μια τουρίστρια και έναν κάτοικο της Θεσσαλονίκης.",
 "script": [
  L("Τουρίστρια", "f", "Συγγνώμη, μήπως ξέρετε πώς θα πάω στα Κάστρα; Ο χάρτης στο κινητό μου με πηγαίνει σε κύκλους και έχω χαθεί εντελώς σε αυτά τα στενά.", "Excuse me, do you know how I get to the Castles? The map on my phone keeps taking me round in circles, and I'm completely lost in these narrow streets."),
  L("Κάτοικος", "m", "Δεν φταίτε εσείς, η Άνω Πόλη μπερδεύει ακόμη κι εμάς. Ακούστε: ανεβείτε αυτό το σοκάκι μέχρι τη μικρή εκκλησία με τον κήπο. Εκεί στρίψτε δεξιά και συνεχίστε την ανηφόρα, ώσπου να δείτε τα τείχη. Θα σας πάρει δέκα λεπτά, αλλά είναι αρκετά απότομο.", "It's not your fault; the Upper Town confuses even us. Listen: go up this alley as far as the little church with the garden. There turn right and keep going uphill until you see the walls. It'll take you ten minutes, but it's quite steep."),
  L("Τουρίστρια", "f", "Υπάρχει και λεωφορείο; Δεν ξέρω αν θα αντέξω κι άλλη ανηφόρα με αυτή τη ζέστη.", "Is there a bus too? I don't know if I can manage another climb in this heat."),
  L("Κάτοικος", "m", "Υπάρχει, το εικοσιτρία, αλλά περνάει κάθε μισή ώρα από τον κεντρικό δρόμο. Αν θέλετε τη γνώμη μου, πηγαίνετε με τα πόδια και σταματήστε στο Βλατάδων Μοναστήρι, που είναι στον δρόμο σας. Έχει την πιο ωραία θέα της πόλης, και σκιά.", "There is, the 23, but it only comes every half hour along the main road. If you want my opinion, go on foot and stop at the Vlatadon Monastery, which is on your way. It has the best view of the city, and shade."),
 ],
 "questions": [
  Q("Γιατί έχει χαθεί η τουρίστρια;", ["Γιατί δεν έχει χάρτη", "Γιατί ο χάρτης του κινητού την πηγαίνει σε κύκλους", "Γιατί πήρε λάθος λεωφορείο", "Γιατί δεν μιλάει ελληνικά"], 1, "Ο χάρτης στο κινητό μου με πηγαίνει σε κύκλους"),
  Q("Τι πρέπει να κάνει στη μικρή εκκλησία;", ["Να στρίψει αριστερά", "Να στρίψει δεξιά", "Να περιμένει το λεωφορείο", "Να κατέβει τη σκάλα"], 1, "Εκεί στρίψτε δεξιά"),
  Q("Τι της προτείνει τελικά ο κάτοικος;", ["Να πάρει ταξί", "Να πάει με τα πόδια και να σταματήσει στη Μονή Βλατάδων", "Να περιμένει το εικοσιτρία", "Να γυρίσει το απόγευμα"], 1, "πηγαίνετε με τα πόδια και σταματήστε στο Βλατάδων Μοναστήρι"),
 ],
 "gloss": {"Κάστρα": "Κάστρα — the Castles (upper walls of Thessaloniki)", "σε κύκλους": "σε κύκλους — round in circles", "στενά": "στενό — narrow street", "σοκάκι": "σοκάκι — alley", "στρίψτε": "στρίβω — to turn", "ανηφόρα": "ανηφόρα — uphill slope", "τείχη": "τείχος — (city) wall", "απότομο": "απότομος — steep", "θα αντέξω": "αντέχω — to bear, manage", "θέα": "θέα — view", "σκιά": "σκιά — shade"},
})

ITEMS.append({
 "id": "l34-mono-syros", "title": "Ένας χειμώνας στη Σύρο", "title_en": "A winter on Syros", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να μιλάει για τον χειμώνα που πέρασε σε ένα νησί.",
 "script": [
  L("Ιφιγένεια", "f", "Δουλεύω ως προγραμματίστρια για μια εταιρεία στο Άμστερνταμ, και από την πανδημία δουλεύω από το σπίτι. Πέρσι αποφάσισα ότι το σπίτι αυτό δεν χρειάζεται να είναι στην Αθήνα. Νοίκιασα ένα διαμέρισμα στην Ερμούπολη, στη Σύρο, από τον Οκτώβριο μέχρι τον Απρίλιο, με το μισό ενοίκιο απ' ό,τι πλήρωνα στο Παγκράτι.", "I work as a programmer for a company in Amsterdam, and since the pandemic I've worked from home. Last year I decided that this home didn't have to be in Athens. I rented a flat in Ermoupoli, on Syros, from October to April, for half the rent I was paying in Pangrati."),
  L("Ιφιγένεια", "f", "Η Σύρος είναι ιδανική για κάτι τέτοιο, γιατί δεν είναι ένα νησί που πεθαίνει τον χειμώνα. Είναι πρωτεύουσα των Κυκλάδων, έχει νοσοκομείο, πανεπιστημιακά τμήματα, θέατρο, και ζωντανή αγορά όλο τον χρόνο. Το ίντερνετ ήταν καλύτερο απ' ό,τι φοβόμουν, και το πλοίο για τον Πειραιά πήγαινε σχεδόν κάθε μέρα, εκτός από τις μέρες με μποφόρ.", "Syros is ideal for something like this, because it isn't an island that dies in winter. It's the capital of the Cyclades, it has a hospital, university departments, a theatre and a lively market all year round. The internet was better than I'd feared, and the ferry to Piraeus went almost every day, except on windy days."),
  L("Ιφιγένεια", "f", "Δεν ήταν όλα ειδυλλιακά. Τον Ιανουάριο φυσούσε τόσο που δεν έβγαινα από το σπίτι για μέρες, και μου έλειψαν οι φίλοι μου. Όμως έμαθα να ζω πιο αργά, να ψωνίζω από τους ίδιους ανθρώπους κάθε μέρα και να με χαιρετούν με το όνομά μου. Φέτος ξαναπάω, αυτή τη φορά για όλο τον χρόνο.", "Not everything was idyllic. In January it was so windy that I didn't leave the house for days, and I missed my friends. But I learned to live more slowly, to shop from the same people every day and to be greeted by name. This year I'm going back, this time for the whole year."),
 ],
 "questions": [
  Q("Γιατί μπόρεσε η Ιφιγένεια να μετακομίσει στη Σύρο;", ["Γιατί βρήκε δουλειά εκεί", "Γιατί δουλεύει από το σπίτι για μια εταιρεία στο εξωτερικό", "Γιατί σπουδάζει εκεί", "Γιατί έχει συγγενείς στο νησί"], 1, "από την πανδημία δουλεύω από το σπίτι"),
  Q("Γιατί η Σύρος είναι ιδανική τον χειμώνα, κατά την ίδια;", ["Γιατί έχει ζέστη", "Γιατί δεν πεθαίνει τον χειμώνα και έχει υπηρεσίες όλο τον χρόνο", "Γιατί είναι κοντά στο Άμστερνταμ", "Γιατί δεν έχει τουρίστες"], 1, "δεν είναι ένα νησί που πεθαίνει τον χειμώνα"),
  Q("Τι θα κάνει φέτος;", ["Θα γυρίσει στην Αθήνα", "Θα ξαναπάει, αυτή τη φορά για όλο τον χρόνο", "Θα μετακομίσει στο Άμστερνταμ", "Θα πάει σε άλλο νησί"], 1, "Φέτος ξαναπάω, αυτή τη φορά για όλο τον χρόνο"),
 ],
 "gloss": {"προγραμματίστρια": "προγραμματίστρια — programmer (f.)", "Νοίκιασα": "νοικιάζω — to rent", "ενοίκιο": "ενοίκιο — rent", "ιδανική": "ιδανικός — ideal", "πρωτεύουσα": "πρωτεύουσα — capital", "μποφόρ": "μποφόρ — Beaufort (strong wind)", "ειδυλλιακά": "ειδυλλιακός — idyllic", "φυσούσε": "φυσάει — it is windy", "μου έλειψαν": "λείπω (μου λείπει) — to be missed", "χαιρετούν": "χαιρετώ — to greet"},
})

ITEMS.append({
 "id": "l34-rep-vouliagmeni", "title": "Η λίμνη της Βουλιαγμένης", "title_en": "Lake Vouliagmeni", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ για τη λίμνη της Βουλιαγμένης.",
 "script": [
  L("Ρεπόρτερ", "f", "Μόλις είκοσι χιλιόμετρα από το κέντρο της Αθήνας, κάτω από έναν απότομο βράχο, βρίσκεται μια λίμνη με γαλαζοπράσινα νερά. Η λίμνη της Βουλιαγμένης σχηματίστηκε πριν από χιλιάδες χρόνια, όταν κατέρρευσε η οροφή ενός μεγάλου σπηλαίου.", "Just twenty kilometres from the centre of Athens, beneath a steep rock face, lies a lake with blue-green waters. Lake Vouliagmeni formed thousands of years ago, when the roof of a large cave collapsed."),
  L("Ρεπόρτερ", "f", "Το νερό της είναι υφάλμυρο, δηλαδή μείγμα θαλασσινού και γλυκού νερού, και ανανεώνεται συνεχώς από υπόγειες πηγές. Χάρη σε αυτές, η θερμοκρασία του μένει γύρω στους είκοσι δύο βαθμούς όλο τον χρόνο, και γι' αυτό πολλοί Αθηναίοι κολυμπούν εδώ ακόμη και τον χειμώνα. Οι επισκέπτες γνωρίζουν και τα μικρά ψαράκια της λίμνης, που τσιμπούν απαλά τα πόδια όσων μπαίνουν στο νερό.", "Its water is brackish, that is, a mixture of sea water and fresh water, and is constantly renewed by underground springs. Thanks to them, its temperature stays around twenty-two degrees all year, which is why many Athenians swim here even in winter. Visitors also get to know the lake's little fish, which gently nibble the feet of anyone who goes into the water."),
  L("Ρεπόρτερ", "f", "Κάτω από την επιφάνεια κρύβεται ένα από τα μεγαλύτερα υποθαλάσσια σπηλαιοσυστήματα του κόσμου, με στοές μήκους αρκετών χιλιομέτρων. Η εξερεύνησή του επιτρέπεται μόνο σε έμπειρους επιστημονικούς δύτες, γιατί στο παρελθόν έχουν χάσει τη ζωή τους εκεί άνθρωποι που μπήκαν χωρίς άδεια.", "Beneath the surface lies one of the largest underwater cave systems in the world, with tunnels several kilometres long. Exploring it is allowed only to experienced scientific divers, because in the past people who went in without permission have lost their lives there."),
 ],
 "questions": [
  Q("Πώς σχηματίστηκε η λίμνη;", ["Από ένα ποτάμι", "Όταν κατέρρευσε η οροφή ενός σπηλαίου", "Από έναν σεισμό τον 20ό αιώνα", "Την έφτιαξαν άνθρωποι"], 1, "όταν κατέρρευσε η οροφή ενός μεγάλου σπηλαίου"),
  Q("Γιατί πολλοί κολυμπούν εκεί και τον χειμώνα;", ["Γιατί είναι δωρεάν", "Γιατί η θερμοκρασία μένει γύρω στους είκοσι δύο βαθμούς", "Γιατί είναι κοντά στο σπίτι τους", "Γιατί το συνιστούν οι γιατροί"], 1, "η θερμοκρασία του μένει γύρω στους είκοσι δύο βαθμούς όλο τον χρόνο"),
  Q("Ποιοι επιτρέπεται να εξερευνήσουν το σπήλαιο;", ["Όλοι οι επισκέπτες", "Μόνο έμπειροι επιστημονικοί δύτες", "Μόνο οι κάτοικοι της περιοχής", "Κανείς"], 1, "Η εξερεύνησή του επιτρέπεται μόνο σε έμπειρους επιστημονικούς δύτες"),
 ],
 "gloss": {"γαλαζοπράσινα": "γαλαζοπράσινος — blue-green", "σχηματίστηκε": "σχηματίζομαι — to form", "κατέρρευσε": "καταρρέω — to collapse", "οροφή": "οροφή — roof, ceiling", "υφάλμυρο": "υφάλμυρος — brackish", "μείγμα": "μείγμα — mixture", "ανανεώνεται": "ανανεώνομαι — to be renewed", "υπόγειες πηγές": "υπόγεια πηγή — underground spring", "τσιμπούν": "τσιμπάω — to nibble, pinch", "στοές": "στοά — tunnel, gallery", "εξερεύνησή": "εξερεύνηση — exploration", "δύτες": "δύτης — diver"},
})

ITEMS.append({
 "id": "l34-rep-ethnikos-kipos", "title": "Ο Εθνικός Κήπος", "title_en": "The National Garden", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τον Εθνικό Κήπο της Αθήνας.",
 "script": [
  L("Ρεπόρτερ", "m", "Δίπλα στη Βουλή, στην καρδιά της Αθήνας, απλώνεται ο Εθνικός Κήπος, μια όαση πρασίνου που πολλοί Αθηναίοι διασχίζουν καθημερινά χωρίς να γνωρίζουν την ιστορία του. Τον δημιούργησε η βασίλισσα Αμαλία γύρω στο 1840 ως ιδιωτικό κήπο των ανακτόρων, και για πολλά χρόνια το κοινό έμπαινε μόνο σε ορισμένες ώρες.", "Next to Parliament, in the heart of Athens, lies the National Garden, an oasis of greenery that many Athenians cross every day without knowing its history. Queen Amalia created it around 1840 as the private garden of the palace, and for many years the public could enter only at certain hours."),
  L("Ρεπόρτερ", "m", "Η βασίλισσα έφερε φυτά από όλο τον κόσμο, που μεταφέρθηκαν με πλοία και φυτεύτηκαν με μεγάλο κόπο σε ένα έδαφος ξερό και πετρώδες. Για το πότισμα χρησιμοποιήθηκε, μεταξύ άλλων, ένα αρχαίο υδραγωγείο. Το 1927 ο κήπος άνοιξε ελεύθερα στο κοινό και πήρε το σημερινό του όνομα.", "The queen brought plants from all over the world, which were transported by ship and planted with great effort in dry, stony ground. For watering, an ancient aqueduct was used, among other things. In 1927 the garden opened freely to the public and took its present name."),
  L("Ρεπόρτερ", "m", "Σήμερα ο κήπος φιλοξενεί εκατοντάδες είδη φυτών, πάπιες και χελώνες, μια παιδική βιβλιοθήκη και ένα μικρό βοτανικό μουσείο. Το καλοκαίρι, όταν η θερμοκρασία στους γύρω δρόμους ξεπερνά τους σαράντα βαθμούς, κάτω από τα δέντρα του είναι αισθητά πιο δροσερά. Γι' αυτό οι ειδικοί λένε ότι η Αθήνα χρειάζεται πολλούς ακόμη τέτοιους κήπους.", "Today the garden is home to hundreds of plant species, ducks and turtles, a children's library and a small botanical museum. In summer, when the temperature in the surrounding streets exceeds forty degrees, it is noticeably cooler under its trees. That's why experts say Athens needs many more gardens like it."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε ο Εθνικός Κήπος;", ["Ως δημοτικό πάρκο", "Ως ιδιωτικός κήπος των ανακτόρων", "Ως αρχαίο ιερό", "Ως βοτανικός κήπος του πανεπιστημίου"], 1, "ως ιδιωτικό κήπο των ανακτόρων"),
  Q("Τι έγινε το 1927;", ["Καταστράφηκε από πυρκαγιά", "Άνοιξε ελεύθερα στο κοινό και πήρε το σημερινό του όνομα", "Φυτεύτηκαν τα πρώτα δέντρα", "Χτίστηκε η Βουλή"], 1, "Το 1927 ο κήπος άνοιξε ελεύθερα στο κοινό"),
  Q("Γιατί οι ειδικοί λένε ότι η Αθήνα χρειάζεται περισσότερους κήπους;", ["Για τους τουρίστες", "Γιατί κάτω από τα δέντρα είναι αισθητά πιο δροσερά", "Για να ζουν περισσότερα ζώα", "Για να έχουν τα παιδιά βιβλιοθήκες"], 1, "κάτω από τα δέντρα του είναι αισθητά πιο δροσερά"),
 ],
 "gloss": {"απλώνεται": "απλώνομαι — to spread out", "όαση": "όαση — oasis", "πρασίνου": "πράσινο — greenery", "ανακτόρων": "ανάκτορα — palace", "κόπο": "κόπος — effort, toil", "πετρώδες": "πετρώδης — stony", "πότισμα": "πότισμα — watering", "υδραγωγείο": "υδραγωγείο — aqueduct", "πάπιες": "πάπια — duck", "χελώνες": "χελώνα — turtle, tortoise", "βοτανικό": "βοτανικός — botanical", "αισθητά": "αισθητά — noticeably"},
})

ITEMS.append({
 "id": "l34-int-navagosostis", "title": "Ένας ναυαγοσώστης", "title_en": "A lifeguard", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν ναυαγοσώστη σε μια πολυσύχναστη παραλία της Χαλκιδικής.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς είναι μια συνηθισμένη μέρα για έναν ναυαγοσώστη;", "What's an ordinary day like for a lifeguard?"),
  L("Στέφανος", "m", "Ξεκινάω στις δέκα και τελειώνω στις έξι, και όλο αυτό το διάστημα δεν παίρνω τα μάτια μου από το νερό. Ο κόσμος νομίζει ότι κάθομαι και κάνω ηλιοθεραπεία, αλλά η συγκέντρωση είναι εξαντλητική. Ένας άνθρωπος που πνίγεται συνήθως δεν φωνάζει, όπως στις ταινίες· βυθίζεται σιωπηλά μέσα σε λίγα δευτερόλεπτα.", "I start at ten and finish at six, and all that time I don't take my eyes off the water. People think I sit and sunbathe, but the concentration is exhausting. A person who is drowning usually doesn't shout, as in films; they sink silently within a few seconds."),
  L("Δημοσιογράφος", "f", "Ποια είναι τα πιο συνηθισμένα περιστατικά;", "What are the most common incidents?"),
  L("Στέφανος", "m", "Τα περισσότερα είναι μικρά: τσιμπήματα από μέδουσες, παιδιά που χάνονται από τους γονείς τους, κάποιος που ζαλίστηκε από τη ζέστη. Οι πιο επικίνδυνες στιγμές είναι όταν φυσάει και δημιουργούνται ρεύματα που τραβούν τον κόσμο στα βαθιά. Τότε βάζουμε κόκκινη σημαία, αλλά πολλοί δεν τη σέβονται.", "Most are minor: jellyfish stings, children who get separated from their parents, someone who felt dizzy from the heat. The most dangerous moments are when it's windy and currents form that pull people out into deep water. Then we put up a red flag, but many people don't respect it."),
  L("Δημοσιογράφος", "f", "Τι θα συμβουλεύατε τους λουόμενους;", "What would you advise swimmers?"),
  L("Στέφανος", "m", "Να μην κολυμπούν μόνοι τους μακριά από την ακτή, να μην μπαίνουν στο νερό αμέσως μετά από βαρύ φαγητό ή αλκοόλ και, κυρίως, να προσέχουν τα παιδιά τους συνεχώς, όχι από την οθόνη του κινητού. Αν σας πάρει το ρεύμα, μην κολυμπάτε κόντρα του· κολυμπήστε παράλληλα με την ακτή, μέχρι να βγείτε από αυτό.", "Not to swim alone far from the shore, not to go into the water right after a heavy meal or alcohol and, above all, to watch their children constantly, not from a phone screen. If a current takes you, don't swim against it; swim parallel to the shore until you get out of it."),
 ],
 "questions": [
  Q("Τι λέει ο Στέφανος για έναν άνθρωπο που πνίγεται;", ["Φωνάζει δυνατά για βοήθεια", "Συνήθως βυθίζεται σιωπηλά μέσα σε λίγα δευτερόλεπτα", "Κουνάει τα χέρια του", "Κολυμπάει προς την ακτή"], 1, "βυθίζεται σιωπηλά μέσα σε λίγα δευτερόλεπτα"),
  Q("Πότε είναι οι πιο επικίνδυνες στιγμές;", ["Όταν έχει πολύ κόσμο", "Όταν φυσάει και δημιουργούνται ρεύματα", "Το μεσημέρι", "Όταν έχει μέδουσες"], 1, "όταν φυσάει και δημιουργούνται ρεύματα"),
  Q("Τι πρέπει να κάνει κανείς αν τον πάρει το ρεύμα;", ["Να κολυμπήσει κόντρα στο ρεύμα", "Να κολυμπήσει παράλληλα με την ακτή", "Να μείνει ακίνητος", "Να βουτήξει στον βυθό"], 1, "κολυμπήστε παράλληλα με την ακτή"),
 ],
 "gloss": {"ναυαγοσώστη": "ναυαγοσώστης — lifeguard", "ηλιοθεραπεία": "ηλιοθεραπεία — sunbathing", "εξαντλητική": "εξαντλητικός — exhausting", "πνίγεται": "πνίγομαι — to drown", "βυθίζεται": "βυθίζομαι — to sink", "περιστατικά": "περιστατικό — incident", "μέδουσες": "μέδουσα — jellyfish", "ζαλίστηκε": "ζαλίζομαι — to feel dizzy", "ρεύματα": "ρεύμα — current", "λουόμενους": "λουόμενος — bather, swimmer", "κόντρα": "κόντρα σε — against"},
})

ITEMS.append({
 "id": "l34-mono-loimos", "title": "Ο Θουκυδίδης και ο λοιμός της Αθήνας", "title_en": "Thucydides and the plague of Athens", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια ιστορικό να μιλάει σε μια διάλεξη για τον λοιμό της Αθήνας.",
 "script": [
  L("Ιστορικός", "f", "Το καλοκαίρι του 430 π.Χ., τον δεύτερο χρόνο του Πελοποννησιακού Πολέμου, μια άγνωστη αρρώστια ξέσπασε στην Αθήνα. Η πόλη ήταν τότε ασφυκτικά γεμάτη, γιατί ο Περικλής είχε διατάξει τους κατοίκους της υπαίθρου να καταφύγουν πίσω από τα Μακρά Τείχη, για να προστατευτούν από τους Σπαρτιάτες.", "In the summer of 430 BC, in the second year of the Peloponnesian War, an unknown disease broke out in Athens. The city was then suffocatingly crowded, because Pericles had ordered the inhabitants of the countryside to take refuge behind the Long Walls, to protect themselves from the Spartans."),
  L("Ιστορικός", "f", "Γνωρίζουμε τόσα πολλά για τον λοιμό χάρη στον Θουκυδίδη, ο οποίος αρρώστησε ο ίδιος και επέζησε. Περιγράφει τα συμπτώματα με μια ακρίβεια σχεδόν ιατρική: τον υψηλό πυρετό, την αφόρητη δίψα, τις πληγές στο δέρμα. Δηλώνει μάλιστα ότι τα καταγράφει για να μπορούν οι μελλοντικές γενιές να αναγνωρίσουν την αρρώστια, αν ποτέ ξαναεμφανιστεί.", "We know so much about the plague thanks to Thucydides, who fell ill himself and survived. He describes the symptoms with almost medical precision: the high fever, the unbearable thirst, the sores on the skin. He even declares that he records them so that future generations may recognise the disease if it ever reappears."),
  L("Ιστορικός", "f", "Το πιο διεισδυτικό μέρος της περιγραφής του, όμως, δεν είναι ιατρικό αλλά κοινωνικό. Ο Θουκυδίδης δείχνει πώς ο φόβος του θανάτου διέλυσε τους θεσμούς και τις αξίες: οι άνθρωποι εγκατέλειπαν τους αρρώστους, οι νεκροί έμεναν άταφοι, και όσοι δεν περίμεναν να ζήσουν αρκετά για να τιμωρηθούν δεν σέβονταν ούτε νόμους ούτε θεούς.", "The most penetrating part of his description, however, is not medical but social. Thucydides shows how the fear of death dissolved institutions and values: people abandoned the sick, the dead were left unburied, and those who didn't expect to live long enough to be punished respected neither laws nor gods."),
  L("Ιστορικός", "f", "Ο λοιμός σκότωσε, κατά τις εκτιμήσεις, ένα μεγάλο μέρος του πληθυσμού, ανάμεσά τους και τον ίδιο τον Περικλή. Ποια ακριβώς ήταν η ασθένεια παραμένει ανοιχτό ερώτημα, παρά τις σύγχρονες αναλύσεις. Αυτό που δεν αμφισβητείται είναι ότι το κείμενο του Θουκυδίδη, γραμμένο πριν από είκοσι πέντε αιώνες, διαβάστηκε με νέα μάτια σε κάθε επιδημία που ακολούθησε, και πιο πρόσφατα στη δική μας.", "The plague killed, by estimates, a large part of the population, among them Pericles himself. What exactly the disease was remains an open question, despite modern analyses. What is not disputed is that Thucydides' text, written twenty-five centuries ago, has been read with new eyes in every epidemic that followed, and most recently in our own."),
 ],
 "questions": [
  Q("Γιατί η Αθήνα ήταν ασφυκτικά γεμάτη το 430 π.Χ.;", ["Λόγω μιας γιορτής", "Γιατί οι κάτοικοι της υπαίθρου είχαν καταφύγει πίσω από τα Μακρά Τείχη", "Γιατί είχαν έρθει πρόσφυγες από τη Σπάρτη", "Λόγω των Ολυμπιακών Αγώνων"], 1, "ο Περικλής είχε διατάξει τους κατοίκους της υπαίθρου να καταφύγουν πίσω από τα Μακρά Τείχη"),
  Q("Γιατί, σύμφωνα με τον ίδιο, ο Θουκυδίδης κατέγραψε τα συμπτώματα;", ["Για να βρεθεί θεραπεία", "Για να αναγνωρίσουν οι μελλοντικές γενιές την αρρώστια", "Για να κατηγορήσει τον Περικλή", "Γιατί του το ζήτησαν οι γιατροί"], 1, "για να μπορούν οι μελλοντικές γενιές να αναγνωρίσουν την αρρώστια"),
  Q("Ποιο θεωρεί η ομιλήτρια το πιο διεισδυτικό μέρος της περιγραφής;", ["Την ιατρική ανάλυση", "Την περιγραφή της κοινωνικής διάλυσης", "Τις στρατιωτικές λεπτομέρειες", "Τον αριθμό των νεκρών"], 1, "Το πιο διεισδυτικό μέρος της περιγραφής του, όμως, δεν είναι ιατρικό αλλά κοινωνικό"),
  Q("Τι ισχύει για την ταυτότητα της ασθένειας;", ["Έχει αποδειχθεί ότι ήταν πανούκλα", "Παραμένει ανοιχτό ερώτημα", "Ήταν γρίπη", "Την ονόμασε ο Θουκυδίδης"], 1, "παραμένει ανοιχτό ερώτημα"),
 ],
 "gloss": {"λοιμός": "λοιμός — plague, pestilence", "ξέσπασε": "ξεσπάω — to break out", "ασφυκτικά": "ασφυκτικά — suffocatingly", "είχε διατάξει": "διατάζω — to order", "υπαίθρου": "ύπαιθρος — countryside", "να καταφύγουν": "καταφεύγω — to take refuge", "συμπτώματα": "σύμπτωμα — symptom", "αφόρητη": "αφόρητος — unbearable", "διεισδυτικό": "διεισδυτικός — penetrating, incisive", "θεσμούς": "θεσμός — institution", "άταφοι": "άταφος — unburied", "εκτιμήσεις": "εκτίμηση — estimate", "δεν αμφισβητείται": "αμφισβητούμαι — to be disputed"},
})

ITEMS.append({
 "id": "l34-int-thermiki-nisida", "title": "Η πόλη που ζεσταίνεται", "title_en": "The city that heats up", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια πολεοδόμο για το φαινόμενο της «αστικής θερμικής νησίδας».",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς είναι η «αστική θερμική νησίδα»;", "What exactly is the «urban heat island»?"),
  L("Πολεοδόμος", "f", "Είναι το φαινόμενο κατά το οποίο οι πόλεις είναι αισθητά θερμότερες από την ύπαιθρο γύρω τους. Η άσφαλτος και το τσιμέντο απορροφούν τη θερμότητα της ημέρας και την αποδίδουν τη νύχτα, ενώ τα κλιματιστικά και τα αυτοκίνητα προσθέτουν κι άλλη. Σε μια καλοκαιρινή νύχτα, η διαφορά ανάμεσα στο κέντρο της Αθήνας και σε ένα προάστιο με πράσινο μπορεί να φτάσει αρκετούς βαθμούς.", "It's the phenomenon whereby cities are noticeably hotter than the countryside around them. Asphalt and concrete absorb the day's heat and give it off at night, while air conditioners and cars add even more. On a summer night, the difference between central Athens and a green suburb can reach several degrees."),
  L("Δημοσιογράφος", "m", "Γιατί μας ανησυχούν ιδιαίτερα οι νύχτες;", "Why are the nights especially worrying?"),
  L("Πολεοδόμος", "f", "Γιατί ο οργανισμός χρειάζεται να δροσιστεί για να αναρρώσει από τη ζέστη της ημέρας. Όταν η θερμοκρασία δεν πέφτει ούτε τη νύχτα, οι ηλικιωμένοι και όσοι έχουν χρόνια νοσήματα κινδυνεύουν σοβαρά. Οι περισσότεροι θάνατοι στους καύσωνες δεν οφείλονται τόσο στη μέγιστη θερμοκρασία όσο στη συσσώρευση πολλών ζεστών ημερών και νυχτών.", "Because the body needs to cool down in order to recover from the heat of the day. When the temperature doesn't drop even at night, the elderly and people with chronic illnesses are at serious risk. Most deaths in heatwaves are due not so much to the maximum temperature as to the accumulation of many hot days and nights."),
  L("Δημοσιογράφος", "m", "Τι μπορεί να γίνει σε μια πόλη τόσο πυκνοδομημένη όσο η Αθήνα;", "What can be done in a city as densely built as Athens?"),
  L("Πολεοδόμος", "f", "Περισσότερα απ' όσα νομίζουμε. Δέντρα σε κάθε δρόμο όπου χωράνε, ανοιχτόχρωμα υλικά σε ταράτσες και πεζοδρόμια, που αντανακλούν τον ήλιο, πράσινες στέγες, μικρά πάρκα τσέπης σε άδεια οικόπεδα. Υπάρχει και ένα πολύ ενδιαφέρον σχέδιο να αξιοποιηθεί ξανά το Αδριάνειο Υδραγωγείο, που μεταφέρει νερό εδώ και σχεδόν δύο χιλιάδες χρόνια, για το πότισμα του πρασίνου. Κανένα από αυτά δεν αρκεί μόνο του· όλα μαζί, όμως, μπορούν να κάνουν τη διαφορά.", "More than we think. Trees on every street where they fit, light-coloured materials on rooftops and pavements, which reflect the sun, green roofs, small pocket parks on empty plots. There's also a very interesting plan to reuse Hadrian's Aqueduct, which has carried water for almost two thousand years, for watering greenery. None of these is enough on its own; together, though, they can make the difference."),
 ],
 "questions": [
  Q("Γιατί οι πόλεις είναι θερμότερες από την ύπαιθρο;", ["Γιατί βρίσκονται πιο νότια", "Γιατί η άσφαλτος και το τσιμέντο απορροφούν θερμότητα και την αποδίδουν τη νύχτα", "Γιατί έχουν λιγότερο αέρα", "Γιατί βρέχει λιγότερο"], 1, "Η άσφαλτος και το τσιμέντο απορροφούν τη θερμότητα της ημέρας και την αποδίδουν τη νύχτα"),
  Q("Γιατί οι ζεστές νύχτες είναι επικίνδυνες;", ["Γιατί δεν μπορούμε να κοιμηθούμε με κλιματιστικό", "Γιατί ο οργανισμός δεν μπορεί να δροσιστεί και να αναρρώσει", "Γιατί αυξάνεται η ρύπανση", "Γιατί κλείνουν τα νοσοκομεία"], 1, "ο οργανισμός χρειάζεται να δροσιστεί για να αναρρώσει"),
  Q("Σε τι οφείλονται κυρίως οι θάνατοι στους καύσωνες;", ["Στη μέγιστη θερμοκρασία μιας μέρας", "Στη συσσώρευση πολλών ζεστών ημερών και νυχτών", "Στην υγρασία", "Στις πυρκαγιές"], 1, "στη συσσώρευση πολλών ζεστών ημερών και νυχτών"),
  Q("Ποια είναι η άποψη της πολεοδόμου για τις λύσεις;", ["Μία λύση αρκεί, τα δέντρα", "Καμία δεν αρκεί μόνη της, όλες μαζί μπορούν να κάνουν τη διαφορά", "Δεν υπάρχουν λύσεις για την Αθήνα", "Το μόνο που χρειάζεται είναι περισσότερα κλιματιστικά"], 1, "Κανένα από αυτά δεν αρκεί μόνο του· όλα μαζί, όμως, μπορούν να κάνουν τη διαφορά"),
 ],
 "gloss": {"πολεοδόμο": "πολεοδόμος — urban planner", "θερμικής νησίδας": "θερμική νησίδα — heat island", "θερμότερες": "θερμός — hotter (comparative)", "απορροφούν": "απορροφώ — to absorb", "αποδίδουν": "αποδίδω — to give off, return", "προάστιο": "προάστιο — suburb", "να αναρρώσει": "αναρρώνω — to recover", "χρόνια νοσήματα": "χρόνιο νόσημα — chronic illness", "συσσώρευση": "συσσώρευση — accumulation", "πυκνοδομημένη": "πυκνοδομημένος — densely built", "αντανακλούν": "αντανακλώ — to reflect", "οικόπεδα": "οικόπεδο — plot (of land)", "Υδραγωγείο": "υδραγωγείο — aqueduct"},
})

rnd = random.Random(34)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-34.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
