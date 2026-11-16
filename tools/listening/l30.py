# Source for library/listening/listening-30.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l30.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l30-ann-leoforeia", "title": "Λεωφορεία αντί για τρένα", "title_en": "Buses instead of trains", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση σε έναν σιδηροδρομικό σταθμό.",
 "script": [
  L("Εκφωνήτρια", "f", "Ενημερώνουμε το επιβατικό κοινό ότι, λόγω εργασιών συντήρησης στη γραμμή, από τη Δευτέρα δεκαοκτώ έως την Παρασκευή είκοσι δύο του μήνα, τα δρομολόγια ανάμεσα στη Λάρισα και το Λιτόχωρο θα εκτελούνται με λεωφορεία.", "We inform passengers that, due to maintenance work on the line, from Monday the eighteenth to Friday the twenty-second of the month, services between Larissa and Litochoro will be operated by buses."),
  L("Εκφωνήτρια", "f", "Οι επιβάτες θα κατεβαίνουν από το τρένο στη Λάρισα και θα επιβιβάζονται στα λεωφορεία που θα περιμένουν μπροστά από την κεντρική είσοδο του σταθμού. Η διαδρομή με το λεωφορείο θα διαρκεί περίπου σαράντα λεπτά περισσότερο, γι' αυτό σας συνιστούμε να υπολογίσετε επιπλέον χρόνο, ιδίως αν έχετε ανταπόκριση.", "Passengers will get off the train in Larissa and board the buses waiting in front of the station's main entrance. The bus journey will take about forty minutes longer, so we advise you to allow extra time, especially if you have a connection."),
  L("Εκφωνήτρια", "f", "Τα εισιτήρια που έχουν ήδη εκδοθεί ισχύουν κανονικά και για τα λεωφορεία. Δυστυχώς, στα λεωφορεία δεν επιτρέπεται η μεταφορά ποδηλάτων. Για περισσότερες πληροφορίες, απευθυνθείτε στα εκδοτήρια.", "Tickets already issued are fully valid on the buses. Unfortunately, bicycles cannot be carried on the buses. For more information, please ask at the ticket offices."),
 ],
 "questions": [
  Q("Γιατί τα δρομολόγια θα γίνονται με λεωφορεία;", ["Λόγω απεργίας", "Λόγω εργασιών συντήρησης στη γραμμή", "Λόγω κακοκαιρίας", "Λόγω έλλειψης προσωπικού"], 1, "λόγω εργασιών συντήρησης στη γραμμή"),
  Q("Γιατί συνιστούν στους επιβάτες να υπολογίσουν επιπλέον χρόνο;", ["Γιατί τα λεωφορεία είναι λίγα", "Γιατί η διαδρομή με το λεωφορείο θα διαρκεί περίπου σαράντα λεπτά περισσότερο", "Γιατί θα κλείσουν τα εκδοτήρια", "Γιατί θα γίνεται έλεγχος εισιτηρίων"], 1, "Η διαδρομή με το λεωφορείο θα διαρκεί περίπου σαράντα λεπτά περισσότερο"),
  Q("Τι δεν επιτρέπεται στα λεωφορεία;", ["Οι μεγάλες βαλίτσες", "Η μεταφορά ποδηλάτων", "Τα κατοικίδια", "Τα παλιά εισιτήρια"], 1, "στα λεωφορεία δεν επιτρέπεται η μεταφορά ποδηλάτων"),
 ],
 "gloss": {"σιδηροδρομικό": "σιδηροδρομικός — railway (adj.)", "επιβατικό κοινό": "επιβατικό κοινό — passengers (formal)", "εργασιών συντήρησης": "εργασίες συντήρησης — maintenance work", "δρομολόγια": "δρομολόγιο — service, route", "θα εκτελούνται": "εκτελούμαι — to be operated, carried out", "θα επιβιβάζονται": "επιβιβάζομαι — to board", "ανταπόκριση": "ανταπόκριση — connection", "έχουν ήδη εκδοθεί": "εκδίδομαι — to be issued", "ισχύουν": "ισχύω — to be valid", "εκδοτήρια": "εκδοτήριο — ticket office"},
})

ITEMS.append({
 "id": "l30-vm-asfaleia", "title": "Μήνυμα από την ασφαλιστική εταιρεία", "title_en": "A message from the insurance company", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από την ασφαλιστική εταιρεία του αυτοκινήτου σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα σας, κύριε Δημητρίου, σας τηλεφωνούμε από την ασφαλιστική σας εταιρεία. Σας υπενθυμίζουμε ότι η ασφάλεια του αυτοκινήτου σας λήγει στις τριάντα του μήνα. Αν δεν ανανεωθεί έγκαιρα, δεν θα επιτρέπεται να κυκλοφορείτε με το όχημα, και σε περίπτωση ελέγχου υπάρχει πρόστιμο.", "Good morning, Mr Dimitriou, we're calling from your insurance company. We remind you that your car insurance expires on the thirtieth of the month. If it isn't renewed in time, you won't be allowed to drive the vehicle, and in case of a check there is a fine."),
  L("Υπάλληλος", "m", "Επειδή τα τελευταία πέντε χρόνια δεν έχετε δηλώσει κανένα ατύχημα, δικαιούστε έκπτωση δέκα τοις εκατό στο ασφάλιστρο. Επιπλέον, φέτος μπορείτε να προσθέσετε στο συμβόλαιό σας οδική βοήθεια σε όλη την Ευρώπη με μόλις είκοσι ευρώ τον χρόνο.", "Because you haven't reported any accident in the last five years, you're entitled to a ten per cent discount on the premium. In addition, this year you can add Europe-wide roadside assistance to your policy for only twenty euros a year."),
  L("Υπάλληλος", "m", "Μπορείτε να ανανεώσετε το συμβόλαιο ηλεκτρονικά, μέσα από την εφαρμογή μας, ή να μας καλέσετε για να σας στείλουμε τον κωδικό πληρωμής. Ευχαριστούμε που μας προτιμάτε.", "You can renew the policy online, through our app, or call us so that we can send you the payment code. Thank you for choosing us."),
 ],
 "questions": [
  Q("Τι θα συμβεί αν η ασφάλεια δεν ανανεωθεί έγκαιρα;", ["Θα αυξηθεί αυτόματα η τιμή", "Δεν θα επιτρέπεται να κυκλοφορεί με το αυτοκίνητο", "Θα χάσει το δίπλωμά του", "Θα ανανεωθεί για δύο χρόνια"], 1, "δεν θα επιτρέπεται να κυκλοφορείτε με το όχημα"),
  Q("Γιατί ο κύριος Δημητρίου δικαιούται έκπτωση;", ["Γιατί είναι νέος πελάτης", "Γιατί δεν έχει δηλώσει ατύχημα τα τελευταία πέντε χρόνια", "Γιατί πληρώνει ηλεκτρονικά", "Γιατί έχει δύο αυτοκίνητα"], 1, "τα τελευταία πέντε χρόνια δεν έχετε δηλώσει κανένα ατύχημα"),
  Q("Τι μπορεί να προσθέσει φέτος στο συμβόλαιο;", ["Ασφάλεια ζωής", "Οδική βοήθεια σε όλη την Ευρώπη", "Ασφάλεια για το σπίτι", "Δεύτερο οδηγό δωρεάν"], 1, "οδική βοήθεια σε όλη την Ευρώπη"),
 ],
 "gloss": {"ασφαλιστική": "ασφαλιστικός — insurance (adj.)", "λήγει": "λήγω — to expire", "ανανεωθεί": "ανανεώνομαι — to be renewed", "όχημα": "όχημα — vehicle", "πρόστιμο": "πρόστιμο — fine", "δηλώσει": "δηλώνω — to report, declare", "δικαιούστε": "δικαιούμαι — to be entitled", "ασφάλιστρο": "ασφάλιστρο — insurance premium", "συμβόλαιό": "συμβόλαιο — policy, contract", "οδική βοήθεια": "οδική βοήθεια — roadside assistance"},
})

ITEMS.append({
 "id": "l30-dia-enoikiasi", "title": "Ενοικίαση αυτοκινήτου στην Κρήτη", "title_en": "Renting a car in Crete", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα γραφείο ενοικίασης αυτοκινήτων στο αεροδρόμιο του Ηρακλείου.",
 "script": [
  L("Πελάτισσα", "f", "Καλησπέρα. Έχω κάνει κράτηση για ένα μικρό αυτοκίνητο για μία εβδομάδα, στο όνομα Κωνσταντίνου.", "Good evening. I've booked a small car for one week, in the name Konstantinou."),
  L("Υπάλληλος", "m", "Μάλιστα, σας βρήκα. Θα χρειαστώ το δίπλωμα οδήγησης και μια πιστωτική κάρτα για την εγγύηση. Θα δεσμεύσουμε τριακόσια ευρώ, τα οποία αποδεσμεύονται όταν επιστρέψετε το αυτοκίνητο χωρίς ζημιές.", "Right, I've found you. I'll need your driving licence and a credit card for the deposit. We'll hold three hundred euros, which is released when you return the car undamaged."),
  L("Πελάτισσα", "f", "Σκοπεύω να πάω και στις παραλίες του νότου, στη Λυβική θάλασσα. Υπάρχει πρόβλημα με τους χωματόδρομους;", "I'm planning to go to the beaches in the south too, on the Libyan Sea. Is there a problem with dirt roads?"),
  L("Υπάλληλος", "m", "Καλή ερώτηση. Η βασική ασφάλεια δεν καλύπτει ζημιές στο κάτω μέρος του αυτοκινήτου ή στα λάστιχα, που συμβαίνουν συχνά στους χωματόδρομους. Γι' αυτό σας προτείνω την πλήρη κάλυψη, με δώδεκα ευρώ την ημέρα· έτσι δεν θα χρειαστεί και εγγύηση. Και κάτι ακόμη: το αυτοκίνητο το παραλαμβάνετε με γεμάτο ρεζερβουάρ και πρέπει να το επιστρέψετε επίσης γεμάτο.", "Good question. The basic insurance doesn't cover damage to the underside of the car or the tyres, which often happens on dirt roads. That's why I suggest full cover, at twelve euros a day; that way you won't need a deposit either. And one more thing: you collect the car with a full tank and must return it full as well."),
  L("Πελάτισσα", "f", "Τότε θα πάρω την πλήρη κάλυψη. Προτιμώ να πληρώσω λίγο παραπάνω και να είμαι ήσυχη.", "Then I'll take full cover. I'd rather pay a bit more and have peace of mind."),
 ],
 "questions": [
  Q("Πότε αποδεσμεύονται τα τριακόσια ευρώ της εγγύησης;", ["Μετά από ένα μήνα", "Όταν επιστραφεί το αυτοκίνητο χωρίς ζημιές", "Την πρώτη μέρα της ενοικίασης", "Όταν πληρωθεί η βενζίνη"], 1, "αποδεσμεύονται όταν επιστρέψετε το αυτοκίνητο χωρίς ζημιές"),
  Q("Τι δεν καλύπτει η βασική ασφάλεια;", ["Την κλοπή", "Ζημιές στο κάτω μέρος του αυτοκινήτου ή στα λάστιχα", "Τα τζάμια", "Τους επιβάτες"], 1, "δεν καλύπτει ζημιές στο κάτω μέρος του αυτοκινήτου ή στα λάστιχα"),
  Q("Πώς πρέπει να επιστραφεί το αυτοκίνητο;", ["Καθαρό εσωτερικά", "Με γεμάτο ρεζερβουάρ", "Στο λιμάνι", "Πριν από τις δέκα το πρωί"], 1, "πρέπει να το επιστρέψετε επίσης γεμάτο"),
 ],
 "gloss": {"ενοικίασης": "ενοικίαση — rental", "κράτηση": "κράτηση — booking", "εγγύηση": "εγγύηση — deposit, guarantee", "Θα δεσμεύσουμε": "δεσμεύω — to hold, block (an amount)", "αποδεσμεύονται": "αποδεσμεύομαι — to be released", "ζημιές": "ζημιά — damage", "χωματόδρομους": "χωματόδρομος — dirt road", "λάστιχα": "λάστιχο — tyre", "πλήρη κάλυψη": "πλήρης κάλυψη — full cover", "παραλαμβάνετε": "παραλαμβάνω — to collect, receive", "ρεζερβουάρ": "ρεζερβουάρ — fuel tank"},
})

ITEMS.append({
 "id": "l30-dia-podilato", "title": "Στο κατάστημα ποδηλάτων", "title_en": "At the bike shop", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα κατάστημα που επισκευάζει ποδήλατα.",
 "script": [
  L("Πελάτης", "m", "Γεια σας. Το ποδήλατό μου κάνει έναν περίεργο θόρυβο όταν αλλάζω ταχύτητες, και τα φρένα δεν πιάνουν καλά, ειδικά όταν βρέχει.", "Hello. My bike makes a strange noise when I change gear, and the brakes don't grip well, especially when it rains."),
  L("Τεχνίτρια", "f", "Για να δούμε... Η αλυσίδα είναι πολύ φθαρμένη, και γι' αυτό πηδάει στα γρανάζια. Τα τακάκια των φρένων έχουν επίσης λιώσει. Πόσο συχνά το χρησιμοποιείτε;", "Let's see... The chain is very worn, and that's why it jumps on the gears. The brake pads are also worn down. How often do you use it?"),
  L("Πελάτης", "m", "Κάθε μέρα, για να πηγαίνω στη δουλειά. Περίπου δεκαπέντε χιλιόμετρα τη μέρα.", "Every day, to go to work. About fifteen kilometres a day."),
  L("Τεχνίτρια", "f", "Τότε είναι λογικό. Με τόσα χιλιόμετρα, η αλυσίδα θέλει αλλαγή περίπου κάθε χρόνο, και πρέπει να καθαρίζεται και να λαδώνεται κάθε μήνα. Η αλλαγή αλυσίδας και τακακιών, μαζί με ένα γενικό σέρβις, κοστίζει εξήντα ευρώ. Θα είναι έτοιμο αύριο το απόγευμα.", "Then it makes sense. With so many kilometres, the chain needs changing about once a year, and it should be cleaned and oiled every month. Changing the chain and pads, together with a general service, costs sixty euros. It'll be ready tomorrow afternoon."),
  L("Πελάτης", "m", "Αύριο; Και πώς θα πάω στη δουλειά;", "Tomorrow? And how will I get to work?"),
  L("Τεχνίτρια", "f", "Μπορώ να σας δανείσω ένα από τα δικά μας ποδήλατα μέχρι αύριο, χωρίς χρέωση. Το κάνουμε για όλους τους σταθερούς πελάτες.", "I can lend you one of our own bikes until tomorrow, free of charge. We do that for all our regular customers."),
 ],
 "questions": [
  Q("Γιατί πηδάει η αλυσίδα στα γρανάζια;", ["Γιατί είναι πολύ σφιχτή", "Γιατί είναι πολύ φθαρμένη", "Γιατί λείπει μια βίδα", "Γιατί βράχηκε"], 1, "Η αλυσίδα είναι πολύ φθαρμένη, και γι' αυτό πηδάει στα γρανάζια"),
  Q("Κάθε πότε πρέπει να καθαρίζεται και να λαδώνεται η αλυσίδα;", ["Κάθε εβδομάδα", "Κάθε μήνα", "Κάθε χρόνο", "Μόνο όταν βρέχει"], 1, "πρέπει να καθαρίζεται και να λαδώνεται κάθε μήνα"),
  Q("Πώς λύνει η τεχνίτρια το πρόβλημα του πελάτη για τη μετακίνησή του;", ["Του προτείνει να πάρει ταξί", "Του δανείζει δωρεάν ένα ποδήλατο μέχρι αύριο", "Επισκευάζει το ποδήλατο αμέσως", "Του δίνει έκπτωση"], 1, "Μπορώ να σας δανείσω ένα από τα δικά μας ποδήλατα μέχρι αύριο, χωρίς χρέωση"),
 ],
 "gloss": {"ταχύτητες": "ταχύτητα — gear (on a bike or car)", "φρένα": "φρένο — brake", "δεν πιάνουν": "πιάνω — (of brakes) to grip", "αλυσίδα": "αλυσίδα — chain", "φθαρμένη": "φθαρμένος — worn", "πηδάει": "πηδάω — to jump, skip", "γρανάζια": "γρανάζι — gear wheel, cog", "τακάκια": "τακάκι — brake pad", "έχουν επίσης λιώσει": "λιώνω — to wear down, melt", "να λαδώνεται": "λαδώνω — to oil", "χρέωση": "χρέωση — charge"},
})

ITEMS.append({
 "id": "l30-mon-douleia", "title": "Η πρώτη μου δουλειά", "title_en": "My first job", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν άντρα να θυμάται την πρώτη του δουλειά σε ένα podcast για την εργασία.",
 "script": [
  L("Παύλος", "m", "Την πρώτη μου δουλειά την έπιασα στα δεκαέξι, ένα καλοκαίρι στη Χαλκιδική. Ήμουν βοηθός σερβιτόρου σε μια ταβέρνα δίπλα στη θάλασσα. Δούλευα δώδεκα ώρες τη μέρα, έξι μέρες την εβδομάδα, και στο τέλος της πρώτης μέρας δεν ένιωθα τα πόδια μου.", "I got my first job at sixteen, one summer in Halkidiki. I was a waiter's assistant in a taverna by the sea. I worked twelve hours a day, six days a week, and at the end of the first day I couldn't feel my legs."),
  L("Παύλος", "m", "Το αφεντικό, ο κυρ-Στέλιος, ήταν αυστηρός αλλά δίκαιος. Τη δεύτερη εβδομάδα έσπασα μια ολόκληρη στοίβα με πιάτα μπροστά σε όλους τους πελάτες. Περίμενα ότι θα με απολύσει. Αντί γι' αυτό, μου έδωσε μια σκούπα και μου είπε: «Όποιος δεν σπάει πιάτα, δεν δουλεύει.»", "The boss, Mr Stelios, was strict but fair. In the second week I broke a whole stack of plates in front of all the customers. I expected him to fire me. Instead, he gave me a broom and said: 'Whoever doesn't break plates isn't working.'"),
  L("Παύλος", "m", "Από εκείνο το καλοκαίρι έμαθα πράγματα που δεν διδάσκονται σε κανένα πανεπιστήμιο: να μιλάω με αγνώστους, να μένω ήρεμος όταν όλα πάνε στραβά, να σέβομαι κάθε δουλειά. Σήμερα έχω δική μου εταιρεία, και όταν ένας νέος υπάλληλος κάνει το πρώτο του λάθος, του λέω την ίδια φράση.", "From that summer I learned things that aren't taught at any university: how to talk to strangers, how to stay calm when everything goes wrong, how to respect every job. Today I have my own company, and when a new employee makes his first mistake, I tell him the same phrase."),
 ],
 "questions": [
  Q("Τι δουλειά έκανε ο Παύλος στα δεκαέξι;", ["Μάγειρας σε ξενοδοχείο", "Βοηθός σερβιτόρου σε ταβέρνα", "Ναυαγοσώστης", "Πωλητής σε κατάστημα"], 1, "Ήμουν βοηθός σερβιτόρου σε μια ταβέρνα δίπλα στη θάλασσα"),
  Q("Πώς αντέδρασε ο κυρ-Στέλιος όταν ο Παύλος έσπασε τα πιάτα;", ["Τον απέλυσε", "Του έδωσε μια σκούπα και του είπε μια ενθαρρυντική φράση", "Του έκοψε τα πιάτα από τον μισθό", "Του φώναξε μπροστά στους πελάτες"], 1, "μου έδωσε μια σκούπα και μου είπε: «Όποιος δεν σπάει πιάτα, δεν δουλεύει.»"),
  Q("Τι κάνει σήμερα ο Παύλος όταν ένας νέος υπάλληλος κάνει λάθος;", ["Τον απολύει", "Του λέει την ίδια φράση", "Τον στέλνει σε σεμινάριο", "Του κόβει τον μισθό"], 1, "του λέω την ίδια φράση"),
 ],
 "gloss": {"την έπιασα": "πιάνω δουλειά — to start a job", "βοηθός σερβιτόρου": "βοηθός σερβιτόρου — waiter's assistant", "αφεντικό": "αφεντικό — boss", "αυστηρός": "αυστηρός — strict", "δίκαιος": "δίκαιος — fair", "στοίβα": "στοίβα — stack", "θα με απολύσει": "απολύω — to fire, dismiss", "σκούπα": "σκούπα — broom", "αγνώστους": "άγνωστος — stranger", "πάνε στραβά": "πάω στραβά — to go wrong", "να σέβομαι": "σέβομαι — to respect"},
})

ITEMS.append({
 "id": "l30-rep-trenaki", "title": "Το τρενάκι του Πηλίου", "title_en": "The little train of Pelion", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για το ιστορικό τρενάκι του Πηλίου.",
 "script": [
  L("Ρεπόρτερ", "f", "Σφυρίζει δυνατά και ξεκινά αργά από τον σταθμό των Άνω Λεχωνίων. Το τρενάκι του Πηλίου, ο «Μουτζούρης», όπως το λένε οι ντόπιοι λόγω του καπνού του, ταξιδεύει ανάμεσα σε ελαιώνες, καστανιές και πλατάνια, με θέα τον Παγασητικό κόλπο.", "It whistles loudly and slowly sets off from the station at Ano Lechonia. The little train of Pelion, the 'Moutzouris', as locals call it because of its smoke, travels among olive groves, chestnut trees and plane trees, with a view of the Pagasetic Gulf."),
  L("Ρεπόρτερ", "f", "Η γραμμή κατασκευάστηκε στα τέλη του δέκατου ένατου και στις αρχές του εικοστού αιώνα, για να συνδέσει τον Βόλο με τα χωριά του βουνού. Το πλάτος της είναι μόλις εξήντα εκατοστά, και ο μηχανικός που τη σχεδίασε ήταν ο Ιταλός Εβαρίστο ντε Κίρικο, πατέρας του διάσημου ζωγράφου Τζόρτζιο ντε Κίρικο, που γεννήθηκε στον Βόλο.", "The line was built in the late nineteenth and early twentieth centuries to link Volos with the mountain villages. Its gauge is just sixty centimetres, and the engineer who designed it was the Italian Evaristo de Chirico, father of the famous painter Giorgio de Chirico, who was born in Volos."),
  L("Ρεπόρτερ", "f", "Η διαδρομή μέχρι τις Μηλιές κρατά περίπου μιάμιση ώρα, και το πιο εντυπωσιακό σημείο είναι η σιδερένια γέφυρα στους Ταξιάρχες, που κρέμεται πάνω από μια χαράδρα. Στις Μηλιές το τρενάκι κάνει στάση μιάμισης ώρας, αρκετή για έναν καφέ στην πλατεία του χωριού. Τον χειμώνα, το τρενάκι λειτουργεί μόνο τα Σαββατοκύριακα και τις αργίες.", "The journey to Milies takes about an hour and a half, and the most impressive point is the iron bridge at Taxiarches, which hangs over a ravine. In Milies the train stops for an hour and a half, enough for a coffee in the village square. In winter, the little train runs only at weekends and on holidays."),
 ],
 "questions": [
  Q("Γιατί οι ντόπιοι λένε το τρενάκι «Μουτζούρη»;", ["Λόγω του χρώματός του", "Λόγω του καπνού του", "Λόγω του ονόματος του μηχανικού", "Γιατί είναι πολύ αργό"], 1, "όπως το λένε οι ντόπιοι λόγω του καπνού του"),
  Q("Ποιος σχεδίασε τη γραμμή;", ["Ο ζωγράφος Τζόρτζιο ντε Κίρικο", "Ο Ιταλός μηχανικός Εβαρίστο ντε Κίρικο", "Ένας Γάλλος αρχιτέκτονας", "Οι κάτοικοι των χωριών"], 1, "ο μηχανικός που τη σχεδίασε ήταν ο Ιταλός Εβαρίστο ντε Κίρικο"),
  Q("Ποιο είναι το πιο εντυπωσιακό σημείο της διαδρομής;", ["Ο σταθμός του Βόλου", "Η σιδερένια γέφυρα στους Ταξιάρχες", "Η πλατεία στις Μηλιές", "Μια σήραγγα κάτω από το βουνό"], 1, "το πιο εντυπωσιακό σημείο είναι η σιδερένια γέφυρα στους Ταξιάρχες"),
 ],
 "gloss": {"Σφυρίζει": "σφυρίζω — to whistle", "ντόπιοι": "ντόπιος — local", "καπνού": "καπνός — smoke", "ελαιώνες": "ελαιώνας — olive grove", "καστανιές": "καστανιά — chestnut tree", "πλατάνια": "πλάτανος — plane tree", "κόλπο": "κόλπος — gulf", "πλάτος": "πλάτος — width, gauge", "σιδερένια": "σιδερένιος — iron (adj.)", "χαράδρα": "χαράδρα — ravine", "αργίες": "αργία — public holiday"},
})

ITEMS.append({
 "id": "l30-rep-pozar", "title": "Τα Λουτρά Πόζαρ", "title_en": "The Pozar thermal baths", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από τα Λουτρά Πόζαρ, στον νομό Πέλλας.",
 "script": [
  L("Ρεπόρτερ", "m", "Έξω η θερμοκρασία είναι δύο βαθμοί, και οι πλαγιές του Καϊμακτσαλάν είναι σκεπασμένες με χιόνι. Κι όμως, δεκάδες άνθρωποι κολυμπούν χαμογελαστοί σε ένα ποτάμι από το οποίο βγαίνουν ατμοί. Βρισκόμαστε στα Λουτρά Πόζαρ, κοντά στην Αριδαία.", "Outside the temperature is two degrees, and the slopes of Kaimaktsalan are covered in snow. And yet dozens of people are swimming, smiling, in a river that is giving off steam. We are at the Pozar baths, near Aridaia."),
  L("Ρεπόρτερ", "m", "Το νερό αναβλύζει από τα βάθη της γης με θερμοκρασία γύρω στους τριάντα επτά βαθμούς όλο τον χρόνο. Σχηματίζει μικρούς καταρράκτες και φυσικές λιμνούλες, όπου οι επισκέπτες κάθονται για ώρες. Οι κάτοικοι λένε ότι τα ιαματικά νερά βοηθούν σε προβλήματα των αρθρώσεων και του δέρματος, και η χρήση τους είναι γνωστή από την αρχαιότητα.", "The water gushes up from deep in the earth at around thirty-seven degrees all year round. It forms small waterfalls and natural pools, where visitors sit for hours. Locals say the healing waters help with joint and skin problems, and their use has been known since antiquity."),
  L("Ρεπόρτερ", "m", "Τον χειμώνα πολλοί επισκέπτες συνδυάζουν το μπάνιο με σκι στο χιονοδρομικό κέντρο του βουνού, που απέχει λίγο πιο πάνω. Συμβουλή: φέρτε παντόφλες για τα βράχια και μην ξεχάσετε μια ζεστή πετσέτα, γιατί το πιο δύσκολο δεν είναι να μπείτε στο νερό, αλλά να βγείτε!", "In winter many visitors combine bathing with skiing at the mountain's ski centre, a little higher up. A tip: bring slippers for the rocks and don't forget a warm towel, because the hardest part isn't getting into the water, it's getting out!"),
 ],
 "questions": [
  Q("Τι θερμοκρασία έχει το νερό στα Λουτρά Πόζαρ;", ["Δύο βαθμούς", "Γύρω στους τριάντα επτά βαθμούς", "Γύρω στους πενήντα βαθμούς", "Αλλάζει ανάλογα με την εποχή"], 1, "με θερμοκρασία γύρω στους τριάντα επτά βαθμούς όλο τον χρόνο"),
  Q("Σε τι λένε οι κάτοικοι ότι βοηθούν τα ιαματικά νερά;", ["Στην πέψη", "Σε προβλήματα των αρθρώσεων και του δέρματος", "Στον ύπνο", "Στην όραση"], 1, "βοηθούν σε προβλήματα των αρθρώσεων και του δέρματος"),
  Q("Ποιο είναι, κατά τον ρεπόρτερ, το πιο δύσκολο;", ["Να βρεις θέση", "Να βγεις από το νερό", "Να μπεις στο νερό", "Να φτάσεις στο μέρος"], 1, "το πιο δύσκολο δεν είναι να μπείτε στο νερό, αλλά να βγείτε"),
 ],
 "gloss": {"Λουτρά": "λουτρά — (thermal) baths", "πλαγιές": "πλαγιά — slope", "ατμοί": "ατμός — steam", "αναβλύζει": "αναβλύζω — to gush up, spring", "καταρράκτες": "καταρράκτης — waterfall", "λιμνούλες": "λιμνούλα — pool, small lake", "ιαματικά": "ιαματικός — healing, medicinal", "αρθρώσεων": "άρθρωση — joint", "χιονοδρομικό κέντρο": "χιονοδρομικό κέντρο — ski centre", "παντόφλες": "παντόφλα — slipper", "πετσέτα": "πετσέτα — towel"},
})

ITEMS.append({
 "id": "l30-int-elegktis", "title": "Ελεγκτής εναέριας κυκλοφορίας", "title_en": "An air traffic controller", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια ελέγκτρια εναέριας κυκλοφορίας.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί λένε ότι η δουλειά σας είναι από τις πιο αγχωτικές στον κόσμο. Ισχύει;", "Many say your job is one of the most stressful in the world. Is that true?"),
  L("Ελέγκτρια", "f", "Είναι απαιτητική, σίγουρα. Τις ώρες αιχμής το καλοκαίρι μπορεί να έχω στην οθόνη μου δεκαπέντε αεροπλάνα ταυτόχρονα, και πρέπει να ξέρω ανά πάσα στιγμή πού βρίσκεται το καθένα, σε ποιο ύψος και με ποια ταχύτητα. Ένα λάθος δεν συγχωρείται. Γι' αυτό δεν δουλεύουμε ποτέ περισσότερο από δύο ώρες χωρίς διάλειμμα.", "It's demanding, certainly. At peak hours in summer I can have fifteen planes on my screen at once, and I have to know at every moment where each one is, at what altitude and at what speed. A mistake isn't forgiven. That's why we never work more than two hours without a break."),
  L("Δημοσιογράφος", "m", "Σε ποια γλώσσα μιλάτε με τους πιλότους;", "What language do you speak to the pilots in?"),
  L("Ελέγκτρια", "f", "Στα αγγλικά, με μια πολύ συγκεκριμένη φρασεολογία. Κάθε εντολή επαναλαμβάνεται από τον πιλότο, για να είμαστε σίγουροι ότι δεν υπάρχει παρεξήγηση. Με τους Έλληνες πιλότους μπορούμε να μιλάμε και ελληνικά, αλλά συνήθως προτιμάμε τα αγγλικά, για να καταλαβαίνουν και οι άλλοι πιλότοι στη συχνότητα τι συμβαίνει.", "In English, with very specific phraseology. Every instruction is repeated back by the pilot, so we're sure there's no misunderstanding. With Greek pilots we can also speak Greek, but we usually prefer English, so that the other pilots on the frequency also understand what's happening."),
  L("Ελέγκτρια", "f", "Το πιο όμορφο στη δουλειά μου; Όταν τελειώνει μια δύσκολη βάρδια και ξέρω ότι χιλιάδες άνθρωποι έφτασαν με ασφάλεια, χωρίς να μάθουν ποτέ ότι υπήρξα.", "The best thing about my job? When a difficult shift ends and I know that thousands of people arrived safely, without ever knowing I existed."),
 ],
 "questions": [
  Q("Γιατί οι ελεγκτές δεν δουλεύουν πάνω από δύο ώρες χωρίς διάλειμμα;", ["Γιατί το ορίζει το συνδικάτο τους", "Γιατί η δουλειά απαιτεί συνεχή προσοχή και ένα λάθος δεν συγχωρείται", "Γιατί οι πτήσεις σταματούν κάθε δύο ώρες", "Γιατί κουράζονται τα μάτια από την οθόνη"], 1, "Ένα λάθος δεν συγχωρείται. Γι' αυτό δεν δουλεύουμε ποτέ περισσότερο από δύο ώρες χωρίς διάλειμμα"),
  Q("Γιατί ο πιλότος επαναλαμβάνει κάθε εντολή;", ["Για να εξασκηθεί στα αγγλικά", "Για να μην υπάρχει παρεξήγηση", "Γιατί η σύνδεση είναι κακή", "Για να ηχογραφηθεί"], 1, "για να είμαστε σίγουροι ότι δεν υπάρχει παρεξήγηση"),
  Q("Γιατί προτιμούν τα αγγλικά και με τους Έλληνες πιλότους;", ["Γιατί τα ελληνικά απαγορεύονται", "Για να καταλαβαίνουν και οι άλλοι πιλότοι στη συχνότητα", "Γιατί είναι πιο σύντομα", "Γιατί το ζητούν οι επιβάτες"], 1, "για να καταλαβαίνουν και οι άλλοι πιλότοι στη συχνότητα τι συμβαίνει"),
 ],
 "gloss": {"ελέγκτρια": "ελέγκτρια — (female) controller", "εναέριας κυκλοφορίας": "εναέρια κυκλοφορία — air traffic", "αγχωτικές": "αγχωτικός — stressful", "απαιτητική": "απαιτητικός — demanding", "ώρες αιχμής": "ώρες αιχμής — peak hours", "ανά πάσα στιγμή": "ανά πάσα στιγμή — at every moment", "ύψος": "ύψος — altitude, height", "δεν συγχωρείται": "συγχωρούμαι — to be forgiven", "φρασεολογία": "φρασεολογία — phraseology", "εντολή": "εντολή — instruction, command", "παρεξήγηση": "παρεξήγηση — misunderstanding", "συχνότητα": "συχνότητα — frequency", "βάρδια": "βάρδια — shift"},
})

ITEMS.append({
 "id": "l30-mon-theodora", "title": "Θεοδώρα, η αυτοκράτειρα", "title_en": "Theodora, the empress", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη για την αυτοκράτειρα Θεοδώρα, σύζυγο του Ιουστινιανού.",
 "script": [
  L("Ιστορικός", "m", "Λίγες γυναίκες του Βυζαντίου έχουν προκαλέσει τόσο έντονες αντιδράσεις όσο η Θεοδώρα. Γεννήθηκε στις αρχές του έκτου αιώνα, κόρη ενός θηριοδαμαστή του Ιπποδρόμου, και στα νιάτα της εμφανιζόταν στη σκηνή ως ηθοποιός, ένα επάγγελμα που τότε θεωρούνταν ανάξιο. Για να την παντρευτεί ο Ιουστινιανός, χρειάστηκε να αλλάξει ο νόμος που απαγόρευε τον γάμο ανώτερων αξιωματούχων με ηθοποιούς.", "Few women of Byzantium have provoked such strong reactions as Theodora. She was born at the beginning of the sixth century, the daughter of an animal-keeper at the Hippodrome, and in her youth she appeared on stage as an actress, a profession then considered disreputable. For Justinian to marry her, the law forbidding high officials to marry actresses had to be changed."),
  L("Ιστορικός", "m", "Η πιο γνωστή στιγμή της είναι η Στάση του Νίκα, το 532. Η πόλη φλεγόταν, οι στασιαστές είχαν ανακηρύξει νέο αυτοκράτορα, και ο Ιουστινιανός σκεφτόταν να εγκαταλείψει την πρωτεύουσα. Σύμφωνα με τον ιστορικό Προκόπιο, η Θεοδώρα τότε μίλησε στο συμβούλιο και είπε ότι δεν θα έφευγε, γιατί «η βασιλεία είναι καλό σάβανο». Ο Ιουστινιανός έμεινε, και η στάση καταπνίγηκε με αιματηρό τρόπο.", "Her best-known moment is the Nika riot, in 532. The city was burning, the rioters had proclaimed a new emperor, and Justinian was thinking of abandoning the capital. According to the historian Procopius, Theodora then spoke to the council and said she would not leave, because 'royalty is a good burial shroud'. Justinian stayed, and the riot was crushed in a bloody way."),
  L("Ιστορικός", "m", "Πρέπει όμως να είμαστε προσεκτικοί με τις πηγές μας. Ο ίδιος Προκόπιος, που στα επίσημα έργα του την επαινεί, έγραψε και τα «Απόκρυφα», ένα κείμενο γεμάτο μίσος, όπου την παρουσιάζει ως διεφθαρμένη και σκληρή. Πολλά από όσα «ξέρουμε» για τη Θεοδώρα προέρχονται από αυτό το εμπαθές κείμενο.", "We must, however, be careful with our sources. The same Procopius who praises her in his official works also wrote the 'Secret History', a text full of hatred, in which he presents her as depraved and cruel. Much of what we 'know' about Theodora comes from this biased text."),
  L("Ιστορικός", "m", "Αυτό που μπορούμε να πούμε με κάποια βεβαιότητα είναι ότι άσκησε πραγματική πολιτική επιρροή και ότι συνδέθηκε με νόμους που βελτίωσαν τη θέση των γυναικών, για παράδειγμα στα κληρονομικά δικαιώματα και στην προστασία από την εκμετάλλευση. Για μια γυναίκα που ξεκίνησε από το περιθώριο, η διαδρομή της παραμένει εντυπωσιακή.", "What we can say with some certainty is that she exercised real political influence and that she was associated with laws that improved the position of women, for example in inheritance rights and protection from exploitation. For a woman who started out on the margins, her path remains remarkable."),
 ],
 "questions": [
  Q("Γιατί χρειάστηκε να αλλάξει ένας νόμος για τον γάμο της Θεοδώρας;", ["Γιατί ήταν ξένη", "Γιατί ο νόμος απαγόρευε τον γάμο ανώτερων αξιωματούχων με ηθοποιούς", "Γιατί ήταν πολύ νέα", "Γιατί ο Ιουστινιανός ήταν ήδη παντρεμένος"], 1, "χρειάστηκε να αλλάξει ο νόμος που απαγόρευε τον γάμο ανώτερων αξιωματούχων με ηθοποιούς"),
  Q("Τι έκανε η Θεοδώρα κατά τη Στάση του Νίκα, σύμφωνα με τον Προκόπιο;", ["Έφυγε κρυφά από την πόλη", "Αρνήθηκε να φύγει και έπεισε τον Ιουστινιανό να μείνει", "Διαπραγματεύτηκε με τους στασιαστές", "Ανακήρυξε τον εαυτό της αυτοκράτειρα"], 1, "είπε ότι δεν θα έφευγε, γιατί «η βασιλεία είναι καλό σάβανο». Ο Ιουστινιανός έμεινε"),
  Q("Γιατί ο ομιλητής ζητά προσοχή με τις πηγές;", ["Γιατί δεν σώζεται κανένα κείμενο της εποχής", "Γιατί πολλά από όσα ξέρουμε προέρχονται από ένα εμπαθές κείμενο του Προκόπιου", "Γιατί οι πηγές είναι γραμμένες στα λατινικά", "Γιατί η Θεοδώρα κατέστρεψε τα αρχεία"], 1, "Πολλά από όσα «ξέρουμε» για τη Θεοδώρα προέρχονται από αυτό το εμπαθές κείμενο"),
  Q("Τι μπορούμε να πούμε με κάποια βεβαιότητα για τη Θεοδώρα;", ["Ότι δεν είχε καμία πολιτική επιρροή", "Ότι άσκησε πολιτική επιρροή και συνδέθηκε με νόμους υπέρ των γυναικών", "Ότι ήταν η πρώτη γυναίκα αυτοκράτωρ που κυβέρνησε μόνη", "Ότι έγραψε η ίδια τα «Απόκρυφα»"], 1, "άσκησε πραγματική πολιτική επιρροή και ότι συνδέθηκε με νόμους που βελτίωσαν τη θέση των γυναικών"),
 ],
 "gloss": {"αυτοκράτειρα": "αυτοκράτειρα — empress", "θηριοδαμαστή": "θηριοδαμαστής — animal-keeper, tamer", "ανάξιο": "ανάξιος — unworthy, disreputable", "αξιωματούχων": "αξιωματούχος — official", "Στάση": "στάση — riot, uprising", "φλεγόταν": "φλέγομαι — to be ablaze", "στασιαστές": "στασιαστής — rioter, rebel", "είχαν ανακηρύξει": "ανακηρύσσω — to proclaim", "σάβανο": "σάβανο — burial shroud", "καταπνίγηκε": "καταπνίγομαι — to be crushed, suppressed", "Απόκρυφα": "«Απόκρυφα» — Procopius's Secret History", "διεφθαρμένη": "διεφθαρμένος — corrupt, depraved", "εμπαθές": "εμπαθής — biased, spiteful", "κληρονομικά": "κληρονομικός — hereditary, of inheritance", "εκμετάλλευση": "εκμετάλλευση — exploitation", "περιθώριο": "περιθώριο — margins (of society)"},
})

ITEMS.append({
 "id": "l30-int-placebo", "title": "Η δύναμη του εικονικού φαρμάκου", "title_en": "The power of the placebo", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια ερευνήτρια για το φαινόμενο του εικονικού φαρμάκου.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς είναι το φαινόμενο του εικονικού φαρμάκου;", "What exactly is the placebo effect?"),
  L("Ερευνήτρια", "f", "Είναι η βελτίωση που νιώθει ένας ασθενής όταν παίρνει μια θεραπεία χωρίς δραστική ουσία, για παράδειγμα ένα χάπι ζάχαρης, πιστεύοντας ότι είναι πραγματικό φάρμακο. Δεν πρόκειται για φαντασία: σε ορισμένες περιπτώσεις μπορούμε να μετρήσουμε αλλαγές στον εγκέφαλο, όπως την απελευθέρωση ουσιών που μειώνουν τον πόνο. Γι' αυτό κάθε νέο φάρμακο πρέπει να αποδείξει ότι είναι αποτελεσματικότερο από ένα εικονικό.", "It's the improvement a patient feels when taking a treatment with no active substance, for example a sugar pill, believing it to be a real medicine. It isn't imagination: in some cases we can measure changes in the brain, such as the release of substances that reduce pain. That's why every new drug has to prove it's more effective than a placebo."),
  L("Δημοσιογράφος", "m", "Λειτουργεί για όλες τις παθήσεις;", "Does it work for all conditions?"),
  L("Ερευνήτρια", "f", "Όχι. Δεν θεραπεύει λοιμώξεις ούτε μικραίνει όγκους. Είναι ισχυρότερο σε συμπτώματα που επηρεάζονται από τον εγκέφαλο, όπως ο πόνος, η ναυτία ή η κόπωση. Και ενδιαφέρον έχει ότι το τελετουργικό μετράει: οι ενέσεις λειτουργούν συχνά καλύτερα από τα χάπια, και τα ακριβά χάπια καλύτερα από τα φθηνά.", "No. It doesn't cure infections or shrink tumours. It's stronger for symptoms influenced by the brain, such as pain, nausea or fatigue. And, interestingly, the ritual matters: injections often work better than pills, and expensive pills better than cheap ones."),
  L("Ερευνήτρια", "f", "Το πιο παράδοξο εύρημα των τελευταίων χρόνων είναι ότι το φαινόμενο εμφανίζεται, σε κάποιο βαθμό, ακόμη και όταν οι ασθενείς ξέρουν ότι παίρνουν εικονικό φάρμακο. Υπάρχει όμως και η σκοτεινή πλευρά, το λεγόμενο φαινόμενο nocebo: όταν περιμένουμε παρενέργειες, συχνά τις νιώθουμε, ακόμη κι αν το χάπι δεν περιέχει τίποτα.", "The most paradoxical finding of recent years is that the effect appears, to some extent, even when patients know they're taking a placebo. But there's also a dark side, the so-called nocebo effect: when we expect side effects, we often feel them, even if the pill contains nothing."),
 ],
 "questions": [
  Q("Γιατί, κατά την ερευνήτρια, το φαινόμενο δεν είναι απλή φαντασία;", ["Γιατί το πιστεύουν οι γιατροί", "Γιατί μερικές φορές μετριούνται αλλαγές στον εγκέφαλο", "Γιατί τα χάπια ζάχαρης έχουν θρεπτική αξία", "Γιατί εμφανίζεται μόνο σε παιδιά"], 1, "σε ορισμένες περιπτώσεις μπορούμε να μετρήσουμε αλλαγές στον εγκέφαλο"),
  Q("Σε ποια συμπτώματα είναι ισχυρότερο το φαινόμενο;", ["Στις λοιμώξεις", "Στον πόνο, τη ναυτία και την κόπωση", "Στους όγκους", "Στα κατάγματα"], 1, "Είναι ισχυρότερο σε συμπτώματα που επηρεάζονται από τον εγκέφαλο, όπως ο πόνος, η ναυτία ή η κόπωση"),
  Q("Τι δείχνει το παράδειγμα των ενέσεων και των ακριβών χαπιών;", ["Ότι τα ακριβά φάρμακα είναι πάντα καλύτερα", "Ότι το τελετουργικό της θεραπείας επηρεάζει το αποτέλεσμα", "Ότι οι ασθενείς προτιμούν τις ενέσεις", "Ότι τα φθηνά χάπια είναι επικίνδυνα"], 1, "το τελετουργικό μετράει"),
  Q("Τι είναι το φαινόμενο nocebo;", ["Η θεραπεία χωρίς φάρμακα", "Όταν περιμένουμε παρενέργειες και τις νιώθουμε, ακόμη κι αν το χάπι δεν περιέχει τίποτα", "Όταν ένα φάρμακο δεν δουλεύει καθόλου", "Όταν ο ασθενής ξέρει ότι παίρνει εικονικό φάρμακο"], 1, "όταν περιμένουμε παρενέργειες, συχνά τις νιώθουμε, ακόμη κι αν το χάπι δεν περιέχει τίποτα"),
 ],
 "gloss": {"εικονικού φαρμάκου": "εικονικό φάρμακο — placebo", "ερευνήτρια": "ερευνήτρια — (female) researcher", "δραστική ουσία": "δραστική ουσία — active substance", "χάπι": "χάπι — pill", "απελευθέρωση": "απελευθέρωση — release", "αποτελεσματικότερο": "αποτελεσματικός — effective", "λοιμώξεις": "λοίμωξη — infection", "όγκους": "όγκος — tumour", "ναυτία": "ναυτία — nausea", "κόπωση": "κόπωση — fatigue", "τελετουργικό": "τελετουργικό — ritual", "ενέσεις": "ένεση — injection", "εύρημα": "εύρημα — finding", "παρενέργειες": "παρενέργεια — side effect"},
})
rnd = random.Random(30)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-30.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
