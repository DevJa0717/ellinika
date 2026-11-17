# Source for library/listening/listening-111.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l111.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l111-ann-vradia-asteriwn", "title": "Βραδιά παρατήρησης του ουρανού στο κάστρο", "title_en": "A stargazing night at the castle", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση ενός συλλόγου ερασιτεχνών αστρονόμων στο τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνητής", "m", "Ο σύλλογος ερασιτεχνών αστρονόμων της πόλης σας προσκαλεί σε μια βραδιά παρατήρησης του ουρανού, την Παρασκευή στις εννιά το βράδυ, στον προαύλιο χώρο του κάστρου. Θα στηθούν έξι τηλεσκόπια, και τα μέλη του συλλόγου θα εξηγούν τι βλέπουμε.", "The town's amateur astronomers' club invites you to a sky-watching evening on Friday at nine in the evening, in the castle forecourt. Six telescopes will be set up, and club members will explain what we are seeing."),
  L("Εκφωνητής", "m", "Αν ο καιρός το επιτρέψει, θα μπορέσουμε να δούμε τους κρατήρες της Σελήνης, τους δακτυλίους του Κρόνου και μερικούς από τους δορυφόρους του Δία. Σε περίπτωση συννεφιάς, η εκδήλωση θα μεταφερθεί στην επόμενη Παρασκευή.", "If the weather allows, we will be able to see the craters of the Moon, the rings of Saturn and some of Jupiter's moons. In case of cloud, the event will be moved to the following Friday."),
  L("Εκφωνητής", "m", "Η είσοδος είναι ελεύθερη. Παρακαλούνται οι επισκέπτες να έχουν μαζί τους ζεστά ρούχα και, αν θέλουν να φωτίζουν τον δρόμο τους, φακό με κόκκινο φως, γιατί το λευκό φως δυσκολεύει την παρατήρηση.", "Admission is free. Visitors are asked to bring warm clothes and, if they want to light their way, a torch with red light, because white light makes observation difficult."),
 ],
 "questions": [
  Q("Πού θα γίνει η εκδήλωση;", ["Στο πλανητάριο", "Στον προαύλιο χώρο του κάστρου", "Στην παραλία", "Στο δημαρχείο"], 1, "στον προαύλιο χώρο του κάστρου"),
  Q("Τι θα γίνει αν έχει συννεφιά;", ["Θα ακυρωθεί οριστικά", "Θα γίνει μια διάλεξη σε αίθουσα", "Θα μεταφερθεί στην επόμενη Παρασκευή", "Θα γίνει κανονικά"], 2, "η εκδήλωση θα μεταφερθεί στην επόμενη Παρασκευή"),
  Q("Γιατί πρέπει ο φακός να έχει κόκκινο φως;", ["Γιατί το λευκό φως δυσκολεύει την παρατήρηση", "Γιατί το ζητά ο δήμος", "Γιατί φαίνεται από μακριά", "Γιατί δεν ενοχλεί τα ζώα"], 0, "το λευκό φως δυσκολεύει την παρατήρηση"),
 ],
 "gloss": {"ερασιτεχνών": "ερασιτέχνης — amateur", "αστρονόμων": "αστρονόμος — astronomer", "προαύλιο": "προαύλιος χώρος — forecourt", "τηλεσκόπια": "τηλεσκόπιο — telescope", "κρατήρες": "κρατήρας — crater", "δακτυλίους": "δακτύλιος — ring", "δορυφόρους": "δορυφόρος — moon, satellite", "συννεφιάς": "συννεφιά — cloudy weather"}
})

ITEMS.append({
 "id": "l111-vm-grafeio-metafraseon", "title": "Μήνυμα από το γραφείο μεταφράσεων", "title_en": "A message from the translation office", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε δώσει το πτυχίο σας για μετάφραση. Ακούτε ένα μήνυμα από το γραφείο μεταφράσεων στον τηλεφωνητή.",
 "script": [
  L("Υπάλληλος", "f", "Καλησπέρα, κυρία Ιωάννου, από το γραφείο μεταφράσεων σας καλώ, για τη μετάφραση του πτυχίου σας στα αγγλικά. Τη μετάφραση την έχουμε σχεδόν έτοιμη, αλλά από τη φωτοτυπία που μας αφήσατε δεν διαβάζεται καθαρά η σφραγίδα του πανεπιστημίου.", "Good afternoon, Ms Ioannou, I'm calling from the translation office about the translation of your degree into English. We have the translation almost ready, but on the photocopy you left us the university's stamp can't be read clearly."),
  L("Υπάλληλος", "f", "Θα χρειαστεί να μας φέρετε το πρωτότυπο, μόνο για να το δούμε· θα σας το επιστρέψουμε αμέσως. Είμαστε ανοιχτά καθημερινά από τις εννιά ως τις πέντε και το Σάββατο ως τις δύο.", "You'll need to bring us the original, just so we can see it; we'll give it back to you straight away. We're open on weekdays from nine to five and on Saturday until two."),
  L("Υπάλληλος", "f", "Αν το φέρετε μέχρι την Τετάρτη, η μετάφραση θα είναι έτοιμη την Παρασκευή, όπως είχαμε συμφωνήσει. Η τιμή παραμένει η ίδια· αν θέλετε όμως και δεύτερο επικυρωμένο αντίγραφο, υπάρχει μια μικρή επιπλέον χρέωση.", "If you bring it by Wednesday, the translation will be ready on Friday, as we agreed. The price stays the same; but if you also want a second certified copy, there is a small extra charge."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με τη φωτοτυπία;", ["Λείπει μια σελίδα", "Δεν διαβάζεται καθαρά η σφραγίδα του πανεπιστημίου", "Είναι σε λάθος γλώσσα", "Χάθηκε"], 1, "δεν διαβάζεται καθαρά η σφραγίδα του πανεπιστημίου"),
  Q("Τι πρέπει να κάνει η κυρία Ιωάννου;", ["Να στείλει μια νέα φωτοτυπία με email", "Να πληρώσει προκαταβολή", "Να φέρει το πρωτότυπο, που θα της επιστραφεί αμέσως", "Να πάει στο πανεπιστήμιο"], 2, "Θα χρειαστεί να μας φέρετε το πρωτότυπο"),
  Q("Πότε θα είναι έτοιμη η μετάφραση, αν φέρει το πρωτότυπο μέχρι την Τετάρτη;", ["Την Παρασκευή", "Την Πέμπτη", "Το Σάββατο", "Την επόμενη εβδομάδα"], 0, "η μετάφραση θα είναι έτοιμη την Παρασκευή"),
 ],
 "gloss": {"μεταφράσεων": "μετάφραση — translation", "πτυχίου": "πτυχίο — degree (certificate)", "φωτοτυπία": "φωτοτυπία — photocopy", "σφραγίδα": "σφραγίδα — stamp, seal", "πρωτότυπο": "πρωτότυπο — the original (document)", "επικυρωμένο": "επικυρωμένος — certified", "χρέωση": "χρέωση — charge"}
})

ITEMS.append({
 "id": "l111-dia-koino-aftokinito", "title": "Ένα αυτοκίνητο για δύο οικογένειες;", "title_en": "One car for two families?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά μια πρόταση των γειτόνων τους.",
 "script": [
  L("Στέλλα", "f", "Η Μαρίνα από τον τρίτο μου πρότεινε κάτι περίεργο. Θέλουν να πουλήσουν το αυτοκίνητό τους, και μας ρώτησαν αν θα θέλαμε να μοιραζόμαστε το δικό μας. Θα πλήρωναν τα μισά έξοδα: ασφάλεια, σέρβις, τέλη κυκλοφορίας.", "Marina from the third floor suggested something odd to me. They want to sell their car, and they asked us if we'd like to share ours. They'd pay half the costs: insurance, servicing, road tax."),
  L("Γιώργος", "m", "Τα μισά έξοδα δεν είναι λίγα. Εμείς το παίρνουμε μόνο τα Σαββατοκύριακα, για το χωριό. Το πρόβλημα είναι αν το χρειαζόμαστε την ίδια μέρα. Και τι γίνεται αν κάποιος το τρακάρει;", "Half the costs is no small amount. We only take it at weekends, for the village. The problem is if we need it on the same day. And what happens if someone crashes it?"),
  L("Στέλλα", "f", "Λένε να φτιάξουμε ένα κοινό ημερολόγιο στο κινητό, όπου ο καθένας θα κλείνει τις μέρες του. Για τις ζημιές, όποιος οδηγεί πληρώνει. Αν θες, να το δοκιμάσουμε για τρεις μήνες και μετά βλέπουμε.", "They suggest setting up a shared calendar on the phone, where each of us books our days. For damage, whoever is driving pays. If you like, let's try it for three months and then we'll see."),
  L("Γιώργος", "m", "Εντάξει, αλλά να τα γράψουμε όλα σε ένα χαρτί και να το υπογράψουμε. Καλοί οι γείτονες, αλλά δεν θέλω να χαλάσουμε τις σχέσεις μας για ένα αυτοκίνητο.", "OK, but let's write it all down on a piece of paper and sign it. The neighbours are nice, but I don't want us to ruin our relationship over a car."),
 ],
 "questions": [
  Q("Τι προτείνουν οι γείτονες;", ["Να αγοράσουν μαζί καινούργιο αυτοκίνητο", "Να μοιράζονται το αυτοκίνητο της Στέλλας και του Γιώργου και να πληρώνουν τα μισά έξοδα", "Να πηγαίνουν μαζί στο χωριό", "Να νοικιάζουν αυτοκίνητο"], 1, "μας ρώτησαν αν θα θέλαμε να μοιραζόμαστε το δικό μας"),
  Q("Πώς θα λύνουν το πρόβλημα αν το χρειάζονται την ίδια μέρα;", ["Με κλήρωση", "Θα το παίρνει πάντα ο Γιώργος", "Με ένα κοινό ημερολόγιο στο κινητό", "Θα παίρνουν ταξί"], 2, "ένα κοινό ημερολόγιο στο κινητό"),
  Q("Τι θέλει ο Γιώργος πριν δεχτεί;", ["Να γράψουν τη συμφωνία σε χαρτί και να την υπογράψουν", "Να πληρώσουν οι γείτονες περισσότερα", "Να ρωτήσουν τον ασφαλιστή", "Να το σκεφτεί έναν μήνα"], 0, "να τα γράψουμε όλα σε ένα χαρτί και να το υπογράψουμε"),
 ],
 "gloss": {"μοιραζόμαστε": "μοιράζομαι — to share", "ασφάλεια": "ασφάλεια — insurance", "σέρβις": "σέρβις — servicing", "τέλη": "τέλη κυκλοφορίας — road tax", "τρακάρει": "τρακάρω — to crash (a car)", "ζημιές": "ζημιά — damage", "υπογράψουμε": "υπογράφω — to sign"}
})

ITEMS.append({
 "id": "l111-int-kloouns-nosokomeio", "title": "Κλόουν σε νοσοκομείο παίδων", "title_en": "A clown in a children's hospital", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γυναίκα που δουλεύει ως κλόουν σε νοσοκομείο.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αθανασίου, πώς βρεθήκατε να δουλεύετε ως κλόουν σε νοσοκομείο;", "Ms Athanasiou, how did you come to work as a clown in a hospital?"),
  L("Αθανασίου", "f", "Είμαι ηθοποιός. Πριν από οκτώ χρόνια ο γιος μιας φίλης νοσηλεύτηκε για μήνες, και πήγαινα να τον επισκεφτώ με μια κόκκινη μύτη. Οι νοσηλεύτριες είδαν ότι τα παιδιά γελούσαν και έτρωγαν καλύτερα, και μου ζήτησαν να έρχομαι τακτικά.", "I'm an actress. Eight years ago a friend's son was in hospital for months, and I used to visit him with a red nose. The nurses saw that the children laughed and ate better, and they asked me to come regularly."),
  L("Δημοσιογράφος", "m", "Δεν είναι δύσκολο να βλέπετε άρρωστα παιδιά;", "Isn't it hard to see sick children?"),
  L("Αθανασίου", "f", "Είναι. Γι' αυτό η πρώτη μας δουλειά είναι να ακούμε. Πριν μπούμε σε ένα δωμάτιο, ρωτάμε τις νοσηλεύτριες πώς είναι το παιδί. Και πάντα χτυπάμε την πόρτα: στο νοσοκομείο τα παιδιά δεν μπορούν να αποφασίσουν σχεδόν τίποτα, έτσι τουλάχιστον μπορούν να μας πουν «όχι».", "It is. That's why our first job is to listen. Before we go into a room, we ask the nurses how the child is. And we always knock on the door: in hospital children can decide almost nothing, so at least they can tell us 'no'."),
  L("Δημοσιογράφος", "m", "Και οι γονείς;", "And the parents?"),
  L("Αθανασίου", "f", "Συχνά γελούν περισσότερο από τα παιδιά. Μια μητέρα μού είπε κάποτε ότι ήταν η πρώτη φορά μετά από δύο εβδομάδες που ξέχασε για λίγα λεπτά πού βρισκόταν. Αυτό για μένα είναι η μεγαλύτερη αμοιβή.", "They often laugh more than the children. A mother once told me it was the first time in two weeks that she forgot for a few minutes where she was. For me, that's the greatest reward."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε η κυρία Αθανασίου;", ["Σπούδασε ειδικά για κλόουν σε νοσοκομεία", "Επισκεπτόταν τον γιο μιας φίλης με μια κόκκινη μύτη", "Την προσέλαβε το υπουργείο Υγείας", "Δούλευε σε τσίρκο"], 1, "πήγαινα να τον επισκεφτώ με μια κόκκινη μύτη"),
  Q("Γιατί χτυπούν πάντα την πόρτα;", ["Για να μην ξυπνήσουν τα παιδιά", "Επειδή το ζητούν οι γιατροί", "Για να μπορούν τα παιδιά να τους πουν «όχι»", "Για να ακούσουν οι γονείς"], 2, "έτσι τουλάχιστον μπορούν να μας πουν «όχι»"),
  Q("Τι θεωρεί η ίδια τη μεγαλύτερη αμοιβή;", ["Όταν οι γονείς ξεχνούν για λίγα λεπτά πού βρίσκονται", "Τον μισθό της", "Τα δώρα των παιδιών", "Τα βραβεία"], 0, "ξέχασε για λίγα λεπτά πού βρισκόταν"),
 ],
 "gloss": {"κλόουν": "κλόουν — clown", "νοσηλεύτηκε": "νοσηλεύομαι — to be in hospital, be treated as an in-patient", "νοσηλεύτριες": "νοσηλεύτρια — (female) nurse", "τακτικά": "τακτικά — regularly", "αμοιβή": "αμοιβή — reward, pay", "ηθοποιός": "ηθοποιός — actor, actress"}
})

ITEMS.append({
 "id": "l111-rep-sxoliki-avli-savvatokyriako", "title": "Η σχολική αυλή ανοίγει τα Σαββατοκύριακα", "title_en": "The school playground opens at weekends", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στο ραδιόφωνο για μια απόφαση ενός δήμου.",
 "script": [
  L("Ρεπόρτερ", "f", "Σε μια πυκνοκατοικημένη γειτονιά της Θεσσαλονίκης, όπου δεν υπάρχει ούτε ένα πάρκο σε απόσταση δέκα λεπτών, ο δήμος αποφάσισε να ανοίγει την αυλή του δημοτικού σχολείου τα Σάββατα και τις Κυριακές, από τις δέκα ως τις οκτώ το βράδυ.", "In a densely populated neighbourhood of Thessaloniki, where there isn't a single park within ten minutes, the municipality has decided to open the primary school playground on Saturdays and Sundays, from ten until eight in the evening."),
  L("Ρεπόρτερ", "f", "Την αυλή την προσέχουν εθελοντές γονείς, που κάνουν βάρδιες των τεσσάρων ωρών. Ανοίγουν και κλειδώνουν την πόρτα, και φροντίζουν να μη μένουν σκουπίδια. Οι τουαλέτες του σχολείου, πάντως, μένουν κλειστές.", "The playground is looked after by volunteer parents, who do four-hour shifts. They open and lock the gate, and make sure no rubbish is left behind. The school toilets, however, stay closed."),
  L("Ρεπόρτερ", "f", "Τις πρώτες εβδομάδες η αυλή γέμιζε κυρίως με παιδιά που έπαιζαν μπάλα. Τώρα έρχονται και ηλικιωμένοι, που κάθονται στα παγκάκια, ενώ μια ομάδα κοριτσιών οργάνωσε μόνη της ένα τουρνουά βόλεϊ.", "In the first weeks the playground filled mainly with children playing football. Now older people come too and sit on the benches, while a group of girls has organised a volleyball tournament on their own."),
 ],
 "questions": [
  Q("Γιατί άνοιξε η σχολική αυλή;", ["Επειδή το σχολείο ανακαινίστηκε", "Επειδή στη γειτονιά δεν υπάρχει πάρκο κοντά", "Επειδή το ζήτησαν οι δάσκαλοι", "Για ένα φεστιβάλ"], 1, "όπου δεν υπάρχει ούτε ένα πάρκο σε απόσταση δέκα λεπτών"),
  Q("Ποιοι προσέχουν την αυλή;", ["Φύλακες του δήμου", "Οι δάσκαλοι", "Εθελοντές γονείς", "Η αστυνομία"], 2, "Την αυλή την προσέχουν εθελοντές γονείς"),
  Q("Τι οργάνωσε μια ομάδα κοριτσιών;", ["Ένα τουρνουά βόλεϊ", "Μια γιορτή για τους ηλικιωμένους", "Ένα παζάρι", "Μαθήματα χορού"], 0, "μια ομάδα κοριτσιών οργάνωσε μόνη της ένα τουρνουά βόλεϊ"),
 ],
 "gloss": {"πυκνοκατοικημένη": "πυκνοκατοικημένος — densely populated", "αυλή": "αυλή — (school) playground, yard", "βάρδιες": "βάρδια — shift", "κλειδώνουν": "κλειδώνω — to lock", "παγκάκια": "παγκάκι — bench", "τουρνουά": "τουρνουά — tournament"}
})

ITEMS.append({
 "id": "l111-rep-koureio-vivlia", "title": "Ένα κουρείο που ακούει τα παιδιά να διαβάζουν", "title_en": "A barbershop that listens to children read", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή με ιστορίες από τις γειτονιές.",
 "script": [
  L("Ρεπόρτερ", "m", "Στο κουρείο του κυρίου Αντώνη, στον Βόλο, υπάρχει ένα ράφι με παιδικά βιβλία. Κάθε παιδί που διαβάζει δυνατά μια ιστορία όσο κουρεύεται, παίρνει έκπτωση δύο ευρώ. Η ιδέα, όπως λέει ο ίδιος, του ήρθε όταν είδε ένα παρόμοιο πρόγραμμα σε ένα ντοκιμαντέρ.", "In Mr Antonis's barbershop, in Volos, there is a shelf of children's books. Every child who reads a story aloud while having their hair cut gets a two-euro discount. The idea, as he says himself, came to him when he saw a similar scheme in a documentary."),
  L("Ρεπόρτερ", "m", "Τα βιβλία τα έχουν χαρίσει κυρίως πελάτες, και η δημοτική βιβλιοθήκη στέλνει κάθε μήνα καινούργια. Ο κύριος Αντώνης δεν διορθώνει τα λάθη των παιδιών· κάνει μόνο ερωτήσεις για την ιστορία, για να δει αν την κατάλαβαν.", "The books have mostly been donated by customers, and the municipal library sends new ones every month. Mr Antonis doesn't correct the children's mistakes; he only asks questions about the story, to see if they understood it."),
  L("Ρεπόρτερ", "m", "Μια μητέρα μάς είπε ότι ο γιος της, που δεν ήθελε να ανοίξει βιβλίο, ζητά πια να κουρευτεί κάθε δύο εβδομάδες. «Τα μαλλιά του δεν μακραίνουν τόσο γρήγορα», είπε γελώντας, «αλλά η ιστορία δεν μπορεί να περιμένει.»", "A mother told us that her son, who didn't want to open a book, now asks to have his hair cut every two weeks. 'His hair doesn't grow that fast,' she said laughing, 'but the story can't wait.'"),
 ],
 "questions": [
  Q("Τι παίρνει ένα παιδί που διαβάζει δυνατά μια ιστορία;", ["Ένα βιβλίο δώρο", "Έκπτωση δύο ευρώ", "Ένα γλυκό", "Δωρεάν κούρεμα"], 1, "παίρνει έκπτωση δύο ευρώ"),
  Q("Τι κάνει ο κύριος Αντώνης όσο διαβάζουν τα παιδιά;", ["Διορθώνει τα λάθη τους", "Βάζει μουσική", "Κάνει ερωτήσεις για την ιστορία", "Βαθμολογεί την ανάγνωση"], 2, "κάνει μόνο ερωτήσεις για την ιστορία"),
  Q("Τι άλλαξε για τον γιο της μητέρας;", ["Ζητά πια να κουρεύεται κάθε δύο εβδομάδες", "Άρχισε να γράφει ιστορίες", "Έγινε μέλος της βιβλιοθήκης", "Θέλει να γίνει κουρέας"], 0, "ζητά πια να κουρευτεί κάθε δύο εβδομάδες"),
 ],
 "gloss": {"κουρείο": "κουρείο — barbershop", "κουρεύεται": "κουρεύομαι — to have one's hair cut", "έκπτωση": "έκπτωση — discount", "ντοκιμαντέρ": "ντοκιμαντέρ — documentary", "χαρίσει": "χαρίζω — to give, donate", "διορθώνει": "διορθώνω — to correct", "μακραίνουν": "μακραίνω — to grow longer"}
})

ITEMS.append({
 "id": "l111-mono-proinos-typos", "title": "Πώς έγινα πρωινός τύπος", "title_en": "How I became a morning person", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλά σε ένα podcast για τις συνήθειές της.",
 "script": [
  L("Ειρήνη", "f", "Για χρόνια ήμουν κουκουβάγια. Κοιμόμουν στις δύο, ξυπνούσα με τρία ξυπνητήρια και έφτανα στη δουλειά χωρίς να έχω φάει τίποτα. Τα πρωινά τα μισούσα.", "For years I was a night owl. I went to sleep at two, woke up with three alarm clocks and got to work without having eaten anything. I hated mornings."),
  L("Ειρήνη", "f", "Όλα άλλαξαν όταν υιοθέτησα έναν σκύλο, που ήθελε βόλτα στις επτά. Τις πρώτες εβδομάδες ήμουν σαν ζόμπι. Σιγά σιγά, όμως, άρχισα να νυστάζω νωρίτερα το βράδυ, και μέσα σε δύο μήνες κοιμόμουν πριν από τις έντεκα.", "Everything changed when I adopted a dog who wanted a walk at seven. The first weeks I was like a zombie. Little by little, though, I started to feel sleepy earlier in the evening, and within two months I was asleep before eleven."),
  L("Ειρήνη", "f", "Σήμερα η ώρα που αγαπώ περισσότερο είναι η βόλτα της αυγής, όταν η πόλη είναι ακόμα άδεια. Δεν λέω ότι όλοι πρέπει να ξυπνούν νωρίς. Λέω μόνο ότι αυτό που νόμιζα πως ήταν ο χαρακτήρας μου, ήταν τελικά μια συνήθεια.", "Today the time I love most is the dawn walk, when the city is still empty. I'm not saying everyone should get up early. I'm only saying that what I thought was my character turned out to be a habit."),
 ],
 "questions": [
  Q("Πώς ήταν η Ειρήνη παλιά;", ["Ξυπνούσε πολύ νωρίς", "Κοιμόταν αργά και μισούσε τα πρωινά", "Δούλευε νυχτερινή βάρδια", "Έτρωγε πάντα μεγάλο πρωινό"], 1, "Τα πρωινά τα μισούσα"),
  Q("Τι την έκανε να αλλάξει;", ["Μια συμβουλή του γιατρού της", "Μια νέα δουλειά", "Ένας σκύλος που ήθελε βόλτα στις επτά", "Ένα βιβλίο"], 2, "υιοθέτησα έναν σκύλο, που ήθελε βόλτα στις επτά"),
  Q("Ποιο είναι το συμπέρασμά της;", ["Αυτό που νόμιζε χαρακτήρα της ήταν τελικά μια συνήθεια", "Όλοι πρέπει να ξυπνούν νωρίς", "Οι σκύλοι είναι καλύτεροι από τα ξυπνητήρια", "Το πρωί είναι πιο παραγωγικό"], 0, "αυτό που νόμιζα πως ήταν ο χαρακτήρας μου, ήταν τελικά μια συνήθεια"),
 ],
 "gloss": {"κουκουβάγια": "κουκουβάγια — owl; (figuratively) night owl", "ξυπνητήρια": "ξυπνητήρι — alarm clock", "μισούσα": "μισώ — to hate", "υιοθέτησα": "υιοθετώ — to adopt", "νυστάζω": "νυστάζω — to feel sleepy", "αυγής": "αυγή — dawn"}
})

ITEMS.append({
 "id": "l111-mono-mageirevo-sta-35", "title": "Έμαθα να μαγειρεύω στα τριάντα πέντε", "title_en": "I learned to cook at thirty-five", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλά σε μια ραδιοφωνική εκπομπή για τη μαγειρική.",
 "script": [
  L("Λευτέρης", "m", "Ως τα τριάντα πέντε μου δεν ήξερα να βράσω ούτε ένα αυγό. Έμενα με τους γονείς μου, μετά έτρωγα έξω ή παράγγελνα. Όταν η γιατρός μού είπε ότι πρέπει να προσέξω τη διατροφή μου, κατάλαβα ότι έπρεπε να μάθω.", "Until I was thirty-five I couldn't even boil an egg. I lived with my parents, then I ate out or ordered in. When the doctor told me I had to watch my diet, I realised I had to learn."),
  L("Λευτέρης", "m", "Ζήτησα από τη μητέρα μου να με μάθει τρία φαγητά: φακές, μπριάμ και κοτόπουλο λεμονάτο. Τα πρώτα μου πιάτα ήταν καταστροφή· τις φακές τις έκαψα δύο φορές. Η μητέρα μου όμως είχε υπομονή και μου έλεγε να μη βιάζομαι.", "I asked my mother to teach me three dishes: lentils, briam and lemon chicken. My first dishes were a disaster; I burned the lentils twice. But my mother was patient and told me not to rush."),
  L("Λευτέρης", "m", "Σήμερα μαγειρεύω σχεδόν κάθε μέρα και ξοδεύω πολύ λιγότερα. Το πιο ωραίο όμως είναι ότι κάθε Κυριακή καλώ φίλους για φαγητό. Πριν από λίγο καιρό η μητέρα μου ήρθε και είπε ότι το μπριάμ μου είναι καλύτερο από το δικό της. Δεν ξέρω αν το εννοούσε.", "Today I cook almost every day and spend much less. But the nicest thing is that every Sunday I invite friends for a meal. Not long ago my mother came and said that my briam is better than hers. I don't know if she meant it."),
 ],
 "questions": [
  Q("Γιατί αποφάσισε ο Λευτέρης να μάθει να μαγειρεύει;", ["Παντρεύτηκε", "Η γιατρός τού είπε να προσέξει τη διατροφή του", "Έχασε τη δουλειά του", "Μετακόμισε στο εξωτερικό"], 1, "πρέπει να προσέξω τη διατροφή μου"),
  Q("Τι συνέβη με τις φακές;", ["Τις έκαψε δύο φορές", "Βγήκαν τέλειες από την πρώτη φορά", "Δεν του άρεσαν", "Τις μαγείρεψε η μητέρα του"], 0, "τις φακές τις έκαψα δύο φορές"),
  Q("Τι του είπε πρόσφατα η μητέρα του;", ["Ότι πρέπει να μάθει κι άλλα φαγητά", "Ότι μαγειρεύει πολύ αλμυρά", "Ότι το μπριάμ του είναι καλύτερο από το δικό της", "Ότι ξοδεύει πολλά"], 2, "το μπριάμ μου είναι καλύτερο από το δικό της"),
 ],
 "gloss": {"βράσω": "βράζω — to boil", "παράγγελνα": "παραγγέλνω — to order (food)", "διατροφή": "διατροφή — diet", "μπριάμ": "μπριάμ — briam (baked mixed vegetables)", "λεμονάτο": "λεμονάτος — cooked with lemon", "υπομονή": "υπομονή — patience", "εννοούσε": "εννοώ — to mean"}
})

ITEMS.append({
 "id": "l111-c1-pos-pethainei-mia-glossa", "title": "Πώς πεθαίνει μια γλώσσα", "title_en": "How a language dies", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια γλωσσολόγο να μιλά σε μια διάλεξη για τις γλώσσες που κινδυνεύουν.",
 "script": [
  L("Γλωσσολόγος", "f", "Στον κόσμο μιλιούνται σήμερα περίπου επτά χιλιάδες γλώσσες. Οι μισές περίπου, σύμφωνα με τις εκτιμήσεις πολλών γλωσσολόγων, κινδυνεύουν να χαθούν μέσα σε αυτόν τον αιώνα. Οι αριθμοί αυτοί είναι αναγκαστικά προσεγγιστικοί, γιατί δεν υπάρχει κοινά αποδεκτός ορισμός για το πού τελειώνει μια διάλεκτος και πού αρχίζει μια γλώσσα.", "Around seven thousand languages are spoken in the world today. About half of them, according to the estimates of many linguists, are at risk of disappearing within this century. These figures are necessarily approximate, because there is no commonly accepted definition of where a dialect ends and a language begins."),
  L("Γλωσσολόγος", "f", "Μια γλώσσα σπάνια πεθαίνει απότομα. Συνήθως η διαδικασία κρατά τρεις γενιές. Οι παππούδες μιλούν μόνο την τοπική γλώσσα. Οι γονείς τη μιλούν, αλλά θεωρούν ότι η κυρίαρχη γλώσσα θα ανοίξει στα παιδιά τους περισσότερες πόρτες, και σταματούν να τη χρησιμοποιούν μαζί τους. Τα εγγόνια την καταλαβαίνουν, αλλά δεν τη μιλούν.", "A language rarely dies suddenly. Usually the process takes three generations. The grandparents speak only the local language. The parents speak it, but they believe that the dominant language will open more doors for their children, and stop using it with them. The grandchildren understand it, but don't speak it."),
  L("Γλωσσολόγος", "f", "Το κρίσιμο σημείο, λοιπόν, δεν είναι πόσοι μιλούν μια γλώσσα, αλλά αν τη μαθαίνουν ακόμη τα παιδιά. Μια γλώσσα με εκατό χιλιάδες ομιλητές, όλους ηλικιωμένους, κινδυνεύει περισσότερο από μια γλώσσα με πέντε χιλιάδες ομιλητές που τη μεταδίδουν στα παιδιά τους.", "So the critical point isn't how many people speak a language, but whether children are still learning it. A language with a hundred thousand speakers, all of them elderly, is in greater danger than a language with five thousand speakers who pass it on to their children."),
  L("Γλωσσολόγος", "f", "Και στην Ελλάδα έχουμε τέτοια παραδείγματα. Τα τσακώνικα, που μιλιούνται σε λίγα χωριά της Αρκαδίας, θεωρούνται σήμερα σοβαρά απειλούμενα. Τα τελευταία χρόνια, πάντως, διδάσκονται σε ορισμένα σχολεία της περιοχής. Το αν αυτό αρκεί, θα το δείξει η επόμενη γενιά.", "We have such examples in Greece too. Tsakonian, spoken in a few villages in Arcadia, is today considered seriously endangered. In recent years, however, it has been taught in some schools in the area. Whether that is enough, the next generation will show."),
 ],
 "questions": [
  Q("Γιατί οι αριθμοί για τις γλώσσες του κόσμου είναι προσεγγιστικοί;", ["Γιατί δεν έχουν καταγραφεί όλες οι χώρες", "Γιατί δεν υπάρχει κοινά αποδεκτός ορισμός για το όριο ανάμεσα σε διάλεκτο και γλώσσα", "Γιατί οι γλώσσες αλλάζουν κάθε χρόνο", "Γιατί οι κυβερνήσεις δεν δίνουν στοιχεία"], 1, "δεν υπάρχει κοινά αποδεκτός ορισμός για το πού τελειώνει μια διάλεκτος και πού αρχίζει μια γλώσσα"),
  Q("Γιατί σταματούν οι γονείς να μιλούν την τοπική γλώσσα στα παιδιά τους;", ["Γιατί την έχουν ξεχάσει", "Γιατί το απαγορεύει το σχολείο", "Γιατί πιστεύουν ότι η κυρίαρχη γλώσσα θα τους ανοίξει περισσότερες πόρτες", "Γιατί τα παιδιά δεν την καταλαβαίνουν"], 2, "θεωρούν ότι η κυρίαρχη γλώσσα θα ανοίξει στα παιδιά τους περισσότερες πόρτες"),
  Q("Ποιο είναι, κατά την ομιλήτρια, το κρίσιμο σημείο για την επιβίωση μιας γλώσσας;", ["Αν τη μαθαίνουν ακόμη τα παιδιά", "Ο αριθμός των ομιλητών της", "Αν έχει γραπτή μορφή", "Αν διδάσκεται στο πανεπιστήμιο"], 0, "αν τη μαθαίνουν ακόμη τα παιδιά"),
  Q("Τι λέει για τα τσακώνικα;", ["Έχουν ήδη χαθεί", "Μιλιούνται σε όλη την Πελοπόννησο", "Θεωρούνται σοβαρά απειλούμενα, αλλά διδάσκονται σε ορισμένα σχολεία", "Είναι διάλεκτος της κρητικής"], 2, "θεωρούνται σήμερα σοβαρά απειλούμενα"),
 ],
 "gloss": {"προσεγγιστικοί": "προσεγγιστικός — approximate", "αποδεκτός": "αποδεκτός — accepted", "διάλεκτος": "διάλεκτος — dialect", "κυρίαρχη": "κυρίαρχος — dominant", "κρίσιμο": "κρίσιμος — critical", "μεταδίδουν": "μεταδίδω — to pass on, transmit", "τσακώνικα": "τσακώνικα — Tsakonian (language of eastern Arcadia)", "απειλούμενα": "απειλούμενος — endangered, threatened"}
})

ITEMS.append({
 "id": "l111-c1-xronos-trexei", "title": "Γιατί τα χρόνια περνούν πιο γρήγορα όσο μεγαλώνουμε;", "title_en": "Why do the years pass faster as we get older?", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια γνωστική ψυχολόγο σε μια εκπομπή για την επιστήμη.",
 "script": [
  L("Δημοσιογράφος", "m", "Σχεδόν όλοι λέμε ότι, όσο μεγαλώνουμε, ο χρόνος κυλά πιο γρήγορα. Ισχύει ή είναι απλώς μια εντύπωση;", "Almost all of us say that, as we get older, time flows faster. Is it true or just an impression?"),
  L("Ψυχολόγος", "f", "Είναι εντύπωση, αλλά πολύ συστηματική. Ενδιαφέρον έχει ότι αφορά κυρίως τα μεγάλα διαστήματα. Όταν ζητάμε από ανθρώπους να εκτιμήσουν πόσο κράτησαν μερικά δευτερόλεπτα ή λεπτά, οι διαφορές ανάμεσα σε νέους και ηλικιωμένους είναι μικρές. Η αίσθηση της επιτάχυνσης εμφανίζεται όταν κοιτάμε πίσω: «πού πήγε η χρονιά;»", "It is an impression, but a very systematic one. Interestingly, it mainly concerns long periods. When we ask people to estimate how long a few seconds or minutes lasted, the differences between young and old people are small. The sense of acceleration appears when we look back: 'where did the year go?'"),
  L("Δημοσιογράφος", "m", "Και πώς εξηγείται;", "And how is it explained?"),
  L("Ψυχολόγος", "f", "Υπάρχουν δύο βασικές εξηγήσεις, που δεν αποκλείουν η μία την άλλη. Η πρώτη είναι αναλογική: για ένα παιδί πέντε χρονών, ένας χρόνος είναι το ένα πέμπτο της ζωής του· για έναν πενηντάρη, είναι το ένα πεντηκοστό. Η δεύτερη έχει να κάνει με τη μνήμη. Κρίνουμε πόσο μεγάλο ήταν ένα διάστημα από το πόσες ξεχωριστές αναμνήσεις μάς άφησε. Στην παιδική ηλικία σχεδόν όλα είναι καινούργια· αργότερα, οι μέρες μοιάζουν μεταξύ τους και συγχωνεύονται στη μνήμη.", "There are two main explanations, which don't exclude each other. The first is proportional: for a five-year-old child, a year is one fifth of their life; for a fifty-year-old, it is one fiftieth. The second has to do with memory. We judge how long a period was by how many distinct memories it left us. In childhood almost everything is new; later, the days resemble each other and merge in memory."),
  L("Δημοσιογράφος", "m", "Μπορούμε να κάνουμε κάτι γι' αυτό;", "Can we do anything about it?"),
  L("Ψυχολόγος", "f", "Αν δεχτούμε τη δεύτερη εξήγηση, ναι. Οι καινούργιες εμπειρίες, ένα ταξίδι, ένα χόμπι, μια γλώσσα, γεμίζουν τη μνήμη με ορόσημα. Υπάρχει μάλιστα ένα παράδοξο: μια εβδομάδα διακοπών σε ένα άγνωστο μέρος μοιάζει να περνά γρήγορα όσο τη ζούμε, αλλά όταν τη θυμόμαστε, μας φαίνεται μεγάλη, ακριβώς επειδή είναι γεμάτη αναμνήσεις.", "If we accept the second explanation, yes. New experiences, a trip, a hobby, a language, fill our memory with landmarks. There is even a paradox: a week's holiday in an unknown place seems to pass quickly while we live it, but when we remember it, it seems long, precisely because it is full of memories."),
 ],
 "questions": [
  Q("Σε ποια διαστήματα αφορά κυρίως η αίσθηση ότι ο χρόνος επιταχύνεται;", ["Στα λίγα δευτερόλεπτα", "Στα μεγάλα διαστήματα, όταν κοιτάμε πίσω", "Στις ώρες της δουλειάς", "Στις νύχτες"], 1, "Η αίσθηση της επιτάχυνσης εμφανίζεται όταν κοιτάμε πίσω"),
  Q("Τι λέει η «αναλογική» εξήγηση;", ["Ότι ο εγκέφαλος γερνά", "Ότι οι ηλικιωμένοι κοιμούνται λιγότερο", "Ότι ένας χρόνος αποτελεί όλο και μικρότερο μέρος της ζωής μας", "Ότι οι μέρες έχουν λιγότερες ώρες"], 2, "για έναν πενηντάρη, είναι το ένα πεντηκοστό"),
  Q("Σύμφωνα με τη δεύτερη εξήγηση, από τι κρίνουμε τη διάρκεια ενός διαστήματος;", ["Από το πόσες ξεχωριστές αναμνήσεις μάς άφησε", "Από το πόσο κουραστήκαμε", "Από το ημερολόγιο", "Από το πόσο διασκεδάσαμε"], 0, "Κρίνουμε πόσο μεγάλο ήταν ένα διάστημα από το πόσες ξεχωριστές αναμνήσεις μάς άφησε"),
  Q("Ποιο είναι το «παράδοξο» των διακοπών;", ["Οι διακοπές μάς κουράζουν περισσότερο από τη δουλειά", "Περνούν γρήγορα όσο τις ζούμε, αλλά στη μνήμη μοιάζουν μεγάλες", "Τις θυμόμαστε λιγότερο από τις εργάσιμες μέρες", "Μοιάζουν ατελείωτες όσο τις ζούμε"], 1, "μοιάζει να περνά γρήγορα όσο τη ζούμε, αλλά όταν τη θυμόμαστε, μας φαίνεται μεγάλη"),
 ],
 "gloss": {"κυλά": "κυλώ — to flow, roll (of time)", "εντύπωση": "εντύπωση — impression", "εκτιμήσουν": "εκτιμώ — to estimate", "επιτάχυνσης": "επιτάχυνση — acceleration", "αποκλείουν": "αποκλείω — to exclude, rule out", "συγχωνεύονται": "συγχωνεύομαι — to merge", "ορόσημα": "ορόσημο — landmark, milestone", "παράδοξο": "παράδοξο — paradox"}
})

rnd = random.Random(111)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-111.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
