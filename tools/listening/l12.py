# Source for library/listening/listening-12.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l12.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l12-ann-aimodosia", "title": "Εθελοντική αιμοδοσία", "title_en": "A blood donation drive", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα του δημαρχείου μιας μικρής πόλης.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο Δήμος, σε συνεργασία με το Γενικό Νοσοκομείο, διοργανώνει εθελοντική αιμοδοσία την Κυριακή είκοσι δύο Νοεμβρίου, από τις εννιά το πρωί έως τις δύο το μεσημέρι, στην αίθουσα εκδηλώσεων του δημαρχείου.", "The Municipality, in cooperation with the General Hospital, is organising a voluntary blood donation on Sunday the twenty-second of November, from nine in the morning until two in the afternoon, in the events hall of the town hall."),
  L("Εκφωνήτρια", "f", "Μπορούν να δώσουν αίμα όσοι είναι από δεκαοχτώ έως εξήντα πέντε ετών, ζυγίζουν τουλάχιστον πενήντα κιλά και είναι υγιείς. Συνιστάται να έχετε φάει ένα ελαφρύ πρωινό και να πιείτε άφθονο νερό. Μην ξεχάσετε την ταυτότητά σας.", "Those aged eighteen to sixty-five who weigh at least fifty kilos and are healthy can give blood. You are advised to have eaten a light breakfast and to drink plenty of water. Don't forget your identity card."),
  L("Εκφωνήτρια", "f", "Οι αιμοδότες θα εγγραφούν στην Τράπεζα Αίματος του Δήμου, η οποία καλύπτει δωρεάν τις ανάγκες των ίδιων και των οικογενειών τους. Μετά την αιμοδοσία θα προσφερθεί χυμός και γλυκό. Σας περιμένουμε· μία μονάδα αίματος μπορεί να σώσει έως και τρεις ζωές.", "Donors will be registered with the Municipality's Blood Bank, which covers the needs of the donors themselves and their families free of charge. After donating, juice and a sweet will be offered. We look forward to seeing you; one unit of blood can save up to three lives."),
 ],
 "questions": [
  Q("Πού θα γίνει η αιμοδοσία;", ["Στο Γενικό Νοσοκομείο", "Στην αίθουσα εκδηλώσεων του δημαρχείου", "Σε ένα κινητό συνεργείο στην πλατεία", "Στο κέντρο υγείας"], 1, "στην αίθουσα εκδηλώσεων του δημαρχείου"),
  Q("Τι συνιστάται στους αιμοδότες;", ["Να έρθουν νηστικοί", "Να φάνε κάτι ελαφρύ και να πιουν πολύ νερό", "Να φέρουν ιατρική βεβαίωση", "Να κλείσουν ραντεβού τηλεφωνικά"], 1, "Συνιστάται να έχετε φάει ένα ελαφρύ πρωινό και να πιείτε άφθονο νερό."),
  Q("Ποιο όφελος έχουν όσοι εγγραφούν στην Τράπεζα Αίματος;", ["Παίρνουν μια μέρα άδεια", "Καλύπτονται οι ανάγκες τους και των οικογενειών τους σε αίμα", "Κάνουν δωρεάν εξετάσεις κάθε χρόνο", "Παίρνουν έκπτωση στα δημοτικά τέλη"], 1, "καλύπτει δωρεάν τις ανάγκες των ίδιων και των οικογενειών τους"),
 ],
 "gloss": {"αιμοδοσία": "αιμοδοσία — blood donation", "διοργανώνει": "διοργανώνω — to organise", "αίθουσα εκδηλώσεων": "αίθουσα εκδηλώσεων — events hall", "ζυγίζουν": "ζυγίζω — to weigh", "Συνιστάται": "συνιστάται — it is recommended", "άφθονο": "άφθονος — plentiful", "αιμοδότες": "αιμοδότης — blood donor", "Τράπεζα Αίματος": "τράπεζα αίματος — blood bank", "μονάδα αίματος": "μονάδα αίματος — unit of blood"},
})

ITEMS.append({
 "id": "l12-vm-diplomaa", "title": "Η ημερομηνία της εξέτασης", "title_en": "The date of the driving test", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα από έναν δάσκαλο οδήγησης προς τη μαθήτριά του.",
 "script": [
  L("Δάσκαλος", "m", "Γεια σου, Δάφνη, ο Στέλιος είμαι από τη σχολή οδηγών. Έχω καλά νέα: βγήκε η ημερομηνία για την πρακτική σου εξέταση. Είναι την Τρίτη δεκαεπτά, στις οχτώ και μισή το πρωί, στο κέντρο εξετάσεων στη βιομηχανική περιοχή.", "Hi Dafni, it's Stelios from the driving school. I have good news: the date for your practical test has come through. It's on Tuesday the seventeenth, at half past eight in the morning, at the test centre in the industrial area."),
  L("Δάσκαλος", "m", "Πριν από την εξέταση θα ήθελα να κάνουμε άλλα δύο μαθήματα, κυρίως για το παρκάρισμα στην ανηφόρα, που σε δυσκολεύει ακόμα. Μπορώ τη Δευτέρα και την Πέμπτη μετά τις πέντε.", "Before the test I'd like us to do two more lessons, mainly for parking on a slope, which you still find hard. I can do Monday and Thursday after five."),
  L("Δάσκαλος", "m", "Το πρωί της εξέτασης έλα στη σχολή στις οχτώ παρά τέταρτο, να πάμε μαζί με το αυτοκίνητο της σχολής. Και φέρε οπωσδήποτε την ταυτότητα και τα γυαλιά σου, γιατί χωρίς γυαλιά δεν θα σε αφήσουν να οδηγήσεις. Πάρε με όταν μπορέσεις.", "On the morning of the test come to the school at a quarter to eight, so we can go together in the school car. And be sure to bring your identity card and your glasses, because without glasses they won't let you drive. Call me when you can."),
 ],
 "questions": [
  Q("Γιατί θέλει ο δάσκαλος να κάνουν κι άλλα μαθήματα;", ["Γιατί η Δάφνη δεν έχει οδηγήσει ποτέ στην πόλη", "Για να εξασκηθεί στο παρκάρισμα στην ανηφόρα", "Γιατί το απαιτεί ο νόμος", "Για να μάθει τη διαδρομή της εξέτασης"], 1, "κυρίως για το παρκάρισμα στην ανηφόρα, που σε δυσκολεύει ακόμα"),
  Q("Πού πρέπει να πάει η Δάφνη το πρωί της εξέτασης;", ["Κατευθείαν στο κέντρο εξετάσεων", "Στη σχολή οδηγών, στις οχτώ παρά τέταρτο", "Στο σπίτι του δασκάλου", "Στη στάση του λεωφορείου"], 1, "έλα στη σχολή στις οχτώ παρά τέταρτο"),
  Q("Γιατί πρέπει να φέρει τα γυαλιά της;", ["Γιατί θα έχει πολύ ήλιο", "Γιατί χωρίς αυτά δεν θα της επιτρέψουν να οδηγήσει", "Γιατί θα κάνει πρώτα εξέταση όρασης", "Γιατί θα διαβάσει ερωτήσεις θεωρίας"], 1, "χωρίς γυαλιά δεν θα σε αφήσουν να οδηγήσεις"),
 ],
 "gloss": {"σχολή οδηγών": "σχολή οδηγών — driving school", "βγήκε η ημερομηνία": "βγαίνει η ημερομηνία — the date is announced, comes through", "πρακτική σου εξέταση": "πρακτική εξέταση — practical test", "κέντρο εξετάσεων": "κέντρο εξετάσεων — test centre", "βιομηχανική περιοχή": "βιομηχανική περιοχή — industrial area", "παρκάρισμα": "παρκάρισμα — parking", "ανηφόρα": "ανηφόρα — uphill slope", "σε δυσκολεύει": "με δυσκολεύει κάτι — I find something hard", "οπωσδήποτε": "οπωσδήποτε — without fail, definitely"},
})

ITEMS.append({
 "id": "l12-dia-synkatoikoi", "title": "Οι λογαριασμοί του σπιτιού", "title_en": "The household bills", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση ανάμεσα σε δύο συγκάτοικους φοιτητές.",
 "script": [
  L("Νίκος", "m", "Άρη, ήρθε ο λογαριασμός του ρεύματος. Διακόσια δέκα ευρώ για δύο μήνες. Πρέπει να τα πούμε.", "Aris, the electricity bill has come. Two hundred and ten euros for two months. We need to talk."),
  L("Άρης", "m", "Διακόσια δέκα; Πώς γίνεται; Εγώ σχεδόν δεν είμαι σπίτι, όλη μέρα είμαι στη σχολή και μετά στη δουλειά.", "Two hundred and ten? How is that possible? I'm hardly ever at home, I'm at the university all day and then at work."),
  L("Νίκος", "m", "Ναι, αλλά το καλοριφέρ στο δωμάτιό σου είναι αναμμένο όλη νύχτα, και ο θερμοσίφωνας μένει ανοιχτός από το πρωί μέχρι το βράδυ. Το έχω δει.", "Yes, but the heater in your room is on all night, and the water heater stays on from morning till evening. I've seen it."),
  L("Άρης", "m", "Εντάξει, για τον θερμοσίφωνα έχεις δίκιο, φταίω. Τι λες να βάλουμε έναν χρονοδιακόπτη; Δεν κοστίζει πολύ και ανάβει μόνο μισή ώρα πριν από το μπάνιο.", "OK, you're right about the water heater, it's my fault. What do you say we install a timer? It doesn't cost much and it only switches on half an hour before a shower."),
  L("Νίκος", "m", "Καλή ιδέα. Κι αυτόν τον λογαριασμό; Μισά μισά, όπως πάντα;", "Good idea. And this bill? Half and half, as always?"),
  L("Άρης", "m", "Όχι, αυτή τη φορά πληρώνω εγώ τα εκατόν τριάντα. Είναι πιο δίκαιο. Και από τον επόμενο μήνα βλέπουμε πώς θα πάει με τον χρονοδιακόπτη.", "No, this time I'll pay the hundred and thirty. It's fairer. And from next month we'll see how it goes with the timer."),
 ],
 "questions": [
  Q("Γιατί ήταν τόσο μεγάλος ο λογαριασμός, κατά τον Νίκο;", ["Γιατί αυξήθηκε η τιμή του ρεύματος", "Γιατί ο Άρης αφήνει αναμμένα το καλοριφέρ και τον θερμοσίφωνα", "Γιατί ήρθε λογαριασμός τριών μηνών", "Γιατί χάλασε το ψυγείο"], 1, "το καλοριφέρ ... είναι αναμμένο όλη νύχτα, και ο θερμοσίφωνας μένει ανοιχτός"),
  Q("Τι προτείνει ο Άρης;", ["Να αλλάξουν πάροχο ρεύματος", "Να βάλουν χρονοδιακόπτη στον θερμοσίφωνα", "Να βρουν τρίτο συγκάτοικο", "Να κλείνουν το καλοριφέρ τη νύχτα"], 1, "Τι λες να βάλουμε έναν χρονοδιακόπτη;"),
  Q("Πώς θα μοιράσουν αυτόν τον λογαριασμό;", ["Μισά μισά", "Θα τον πληρώσει όλο ο Άρης", "Ο Άρης θα πληρώσει το μεγαλύτερο μέρος", "Θα τον πληρώσει ο ιδιοκτήτης"], 2, "αυτή τη φορά πληρώνω εγώ τα εκατόν τριάντα"),
 ],
 "gloss": {"συγκάτοικους": "συγκάτοικος — flatmate", "λογαριασμός του ρεύματος": "λογαριασμός ρεύματος — electricity bill", "Πρέπει να τα πούμε": "πρέπει να τα πούμε — we need to talk", "καλοριφέρ": "καλοριφέρ — radiator, heater", "αναμμένο": "αναμμένος — switched on, lit", "θερμοσίφωνας": "θερμοσίφωνας — electric water heater", "φταίω": "φταίω — to be to blame", "χρονοδιακόπτη": "χρονοδιακόπτης — timer switch", "Μισά μισά": "μισά μισά — half and half", "δίκαιο": "δίκαιος — fair"},
})

ITEMS.append({
 "id": "l12-dia-logistis", "title": "Στον λογιστή", "title_en": "At the accountant's", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση ανάμεσα σε μια ελεύθερη επαγγελματία και τον λογιστή της.",
 "script": [
  L("Λογιστής", "m", "Λοιπόν, κυρία Μανωλάκη, ήρθε η ώρα για τη φορολογική σας δήλωση. Μου φέρατε τις αποδείξεις από τις αγορές σας με κάρτα;", "So, Ms Manolaki, it's time for your tax return. Did you bring me the receipts for your card purchases?"),
  L("Μανωλάκη", "f", "Δεν τις κράτησα όλες. Είναι απαραίτητο;", "I didn't keep them all. Is it necessary?"),
  L("Λογιστής", "m", "Δεν χρειάζεται να τις έχετε σε χαρτί, οι ηλεκτρονικές πληρωμές καταγράφονται αυτόματα. Το σημαντικό είναι να έχετε ξοδέψει με κάρτα ένα ορισμένο ποσοστό του εισοδήματός σας. Αλλιώς πληρώνετε επιπλέον φόρο στη διαφορά.", "You don't need to have them on paper, electronic payments are recorded automatically. What matters is that you have spent a certain percentage of your income by card. Otherwise you pay extra tax on the difference."),
  L("Μανωλάκη", "f", "Νομίζω ότι είμαι εντάξει, πληρώνω σχεδόν τα πάντα με κάρτα. Τι άλλο χρειάζεστε;", "I think I'm fine, I pay for almost everything by card. What else do you need?"),
  L("Λογιστής", "m", "Τα τιμολόγια που κόψατε φέτος, το συμβόλαιο του γραφείου που νοικιάζετε και τις αποδείξεις του ασφαλιστικού ταμείου. Το γραφείο, αφού το χρησιμοποιείτε για τη δουλειά, μπορούμε να το εκπέσουμε ως επαγγελματική δαπάνη.", "The invoices you issued this year, the contract for the office you rent and the receipts from your social insurance fund. Since you use the office for work, we can deduct it as a business expense."),
  L("Μανωλάκη", "f", "Τέλεια. Θα σας τα στείλω όλα με email μέχρι την Παρασκευή.", "Perfect. I'll email you everything by Friday."),
 ],
 "questions": [
  Q("Γιατί δεν χρειάζονται οι χάρτινες αποδείξεις;", ["Γιατί η κυρία Μανωλάκη δεν πληρώνει φόρο", "Γιατί οι πληρωμές με κάρτα καταγράφονται αυτόματα", "Γιατί ο λογιστής τις έχει ήδη", "Γιατί καταργήθηκε η δήλωση"], 1, "οι ηλεκτρονικές πληρωμές καταγράφονται αυτόματα"),
  Q("Τι συμβαίνει αν κάποιος δεν ξοδέψει αρκετά με κάρτα;", ["Χάνει τη σύνταξή του", "Πληρώνει επιπλέον φόρο", "Παίρνει πρόστιμο από την τράπεζα", "Δεν μπορεί να κάνει δήλωση"], 1, "Αλλιώς πληρώνετε επιπλέον φόρο στη διαφορά."),
  Q("Γιατί ζητάει ο λογιστής το συμβόλαιο του γραφείου;", ["Για να το εκπέσει ως επαγγελματική δαπάνη", "Για να το νοικιάσει ο ίδιος", "Γιατί λήγει φέτος", "Για να ελέγξει τον ιδιοκτήτη"], 0, "μπορούμε να το εκπέσουμε ως επαγγελματική δαπάνη"),
 ],
 "gloss": {"ελεύθερη επαγγελματία": "ελεύθερος επαγγελματίας — self-employed person, freelancer", "λογιστή": "λογιστής — accountant", "φορολογική σας δήλωση": "φορολογική δήλωση — tax return", "αποδείξεις": "απόδειξη — receipt", "καταγράφονται": "καταγράφομαι — to be recorded", "ποσοστό": "ποσοστό — percentage", "εισοδήματός": "εισόδημα — income", "τιμολόγια": "τιμολόγιο — invoice", "κόψατε": "κόβω τιμολόγιο — to issue an invoice", "ασφαλιστικού ταμείου": "ασφαλιστικό ταμείο — social insurance fund", "εκπέσουμε": "εκπίπτω — to deduct (tax)", "επαγγελματική δαπάνη": "επαγγελματική δαπάνη — business expense"},
})

ITEMS.append({
 "id": "l12-mon-nosileftria", "title": "Νυχτερινή βάρδια", "title_en": "Night shift", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια νοσηλεύτρια να μιλά για τον πρώτο χρόνο της σε ένα δημόσιο νοσοκομείο.",
 "script": [
  L("Ελένη", "f", "Τον πρώτο μου χρόνο στο νοσοκομείο δεν θα τον ξεχάσω ποτέ. Με έβαλαν σχεδόν αμέσως σε νυχτερινές βάρδιες, στην παθολογική κλινική. Μία νοσηλεύτρια και μία βοηθός για τριάντα ασθενείς. Στη σχολή δεν σου μαθαίνουν πώς να τρέχεις ταυτόχρονα σε τρία δωμάτια.", "I will never forget my first year at the hospital. They put me on night shifts almost straight away, in the internal medicine ward. One nurse and one assistant for thirty patients. At nursing school they don't teach you how to run to three rooms at once."),
  L("Ελένη", "f", "Το πιο δύσκολο δεν ήταν η κούραση, αλλά οι στιγμές που ένιωθα ότι δεν προλαβαίνω να σταθώ δίπλα στους ανθρώπους όπως θα ήθελα. Μια γιαγιά μού κρατούσε το χέρι και μου έλεγε «κάτσε λίγο, κορίτσι μου», κι εγώ έπρεπε να φύγω γιατί χτυπούσε το κουδούνι αλλού.", "The hardest thing wasn't the tiredness, but the moments when I felt I didn't have time to be there for people as I would have liked. An old lady held my hand and said \"stay a little, my girl\", and I had to leave because a bell was ringing somewhere else."),
  L("Ελένη", "f", "Πολλοί συμφοιτητές μου έφυγαν για τη Γερμανία ή την Αγγλία, όπου οι μισθοί είναι διπλάσιοι. Το σκέφτηκα κι εγώ. Έμεινα, γιατί εδώ είναι η οικογένειά μου, και γιατί πιστεύω ότι το δημόσιο σύστημα υγείας αξίζει να το υπερασπιστούμε. Αλλά καταλαβαίνω απόλυτα όσους έφυγαν.", "Many of my fellow students left for Germany or England, where salaries are double. I thought about it too. I stayed, because my family is here, and because I believe the public health system is worth defending. But I completely understand those who left."),
 ],
 "questions": [
  Q("Τι ήταν το πιο δύσκολο για την Ελένη;", ["Η σωματική κούραση", "Ότι δεν είχε χρόνο να σταθεί δίπλα στους ασθενείς όπως ήθελε", "Οι σχέσεις με τους γιατρούς", "Ο χαμηλός μισθός"], 1, "οι στιγμές που ένιωθα ότι δεν προλαβαίνω να σταθώ δίπλα στους ανθρώπους"),
  Q("Πόσο προσωπικό είχε η κλινική τη νύχτα;", ["Δύο νοσηλεύτριες", "Μία νοσηλεύτρια και μία βοηθός", "Μία νοσηλεύτρια και έναν γιατρό", "Τρεις νοσηλεύτριες"], 1, "Μία νοσηλεύτρια και μία βοηθός για τριάντα ασθενείς."),
  Q("Γιατί δεν έφυγε στο εξωτερικό;", ["Γιατί δεν ήξερε γλώσσες", "Για την οικογένειά της και γιατί πιστεύει στο δημόσιο σύστημα υγείας", "Γιατί της πρόσφεραν προαγωγή", "Γιατί δεν της άρεσε το κλίμα"], 1, "Έμεινα, γιατί εδώ είναι η οικογένειά μου, και γιατί πιστεύω ότι το δημόσιο σύστημα υγείας αξίζει να το υπερασπιστούμε."),
 ],
 "gloss": {"νοσηλεύτρια": "νοσηλεύτρια — nurse (f.)", "νυχτερινές βάρδιες": "νυχτερινή βάρδια — night shift", "παθολογική κλινική": "παθολογική κλινική — internal medicine ward", "ασθενείς": "ασθενής — patient", "κούραση": "κούραση — tiredness", "προλαβαίνω": "προλαβαίνω — to have time (to), manage", "να σταθώ δίπλα": "στέκομαι δίπλα σε κάποιον — to stand by, support someone", "κάτσε λίγο": "κάτσε — sit, stay (imperative of κάθομαι)", "συμφοιτητές": "συμφοιτητής — fellow student", "διπλάσιοι": "διπλάσιος — double", "να το υπερασπιστούμε": "υπερασπίζομαι — to defend"},
})

ITEMS.append({
 "id": "l12-rep-sfoungarades", "title": "Οι σφουγγαράδες της Καλύμνου", "title_en": "The sponge divers of Kalymnos", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από την Κάλυμνο για την παράδοση της σπογγαλιείας.",
 "script": [
  L("Δημοσιογράφος", "m", "Για πάνω από έναν αιώνα, η Κάλυμνος ζούσε από τα σφουγγάρια. Κάθε άνοιξη, μετά το Πάσχα, τα καΐκια έφευγαν για τις ακτές της Βόρειας Αφρικής και γύριζαν το φθινόπωρο. Στο λιμάνι, οι γυναίκες αποχαιρετούσαν τους άντρες χωρίς να ξέρουν αν θα τους ξαναδούν.", "For over a century, Kalymnos lived from sponges. Every spring, after Easter, the boats left for the coasts of North Africa and returned in the autumn. At the harbour, the women said goodbye to the men without knowing whether they would see them again."),
  L("Δημοσιογράφος", "m", "Η δουλειά ήταν εξαιρετικά επικίνδυνη. Με τη χρήση του σκαφάνδρου, οι δύτες κατέβαιναν πολύ βαθιά, και πολλοί έμειναν παράλυτοι ή πέθαναν από τη νόσο των δυτών, που τότε κανείς δεν καταλάβαινε. Στο νησί υπάρχουν ακόμα ηλικιωμένοι που περπατούν με δυσκολία εξαιτίας της.", "The work was extremely dangerous. With the diving suit, divers went down very deep, and many were left paralysed or died from decompression sickness, which nobody understood at the time. On the island there are still old men who walk with difficulty because of it."),
  L("Δημοσιογράφος", "m", "Σήμερα έχουν μείνει ελάχιστοι σφουγγαράδες. Ασθένειες των θαλάσσιων σπόγγων και τα συνθετικά σφουγγάρια μείωσαν δραματικά τη ζήτηση. Η παράδοση όμως ζει στο Ναυτικό Μουσείο, στα εργαστήρια επεξεργασίας που επισκέπτονται οι τουρίστες, και στη γιορτή που διοργανώνει κάθε χρόνο το νησί.", "Today very few sponge divers remain. Diseases of marine sponges and synthetic sponges reduced demand dramatically. But the tradition lives on in the Maritime Museum, in the processing workshops that tourists visit, and in the festival the island organises every year."),
 ],
 "questions": [
  Q("Πότε έφευγαν τα καΐκια των σφουγγαράδων;", ["Το φθινόπωρο", "Την άνοιξη, μετά το Πάσχα", "Τον χειμώνα", "Όλο τον χρόνο"], 1, "Κάθε άνοιξη, μετά το Πάσχα, τα καΐκια έφευγαν"),
  Q("Ποιος ήταν ο μεγαλύτερος κίνδυνος της δουλειάς;", ["Οι καρχαρίες", "Οι καταιγίδες", "Η νόσος των δυτών από τις βαθιές καταδύσεις", "Οι πειρατές"], 2, "πολλοί έμειναν παράλυτοι ή πέθαναν από τη νόσο των δυτών"),
  Q("Γιατί μειώθηκε η σπογγαλιεία;", ["Γιατί απαγορεύτηκε από τον νόμο", "Λόγω ασθενειών των σπόγγων και των συνθετικών σφουγγαριών", "Γιατί οι νέοι έφυγαν στην Αμερική", "Λόγω του τουρισμού"], 1, "Ασθένειες των θαλάσσιων σπόγγων και τα συνθετικά σφουγγάρια μείωσαν δραματικά τη ζήτηση."),
 ],
 "gloss": {"σφουγγαράδες": "σφουγγαράς — sponge diver", "σπογγαλιείας": "σπογγαλιεία — sponge fishing", "σφουγγάρια": "σφουγγάρι — sponge", "αποχαιρετούσαν": "αποχαιρετώ — to say goodbye", "σκαφάνδρου": "σκάφανδρο — diving suit (with helmet)", "δύτες": "δύτης — diver", "παράλυτοι": "παράλυτος — paralysed", "νόσο των δυτών": "νόσος των δυτών — decompression sickness, the bends", "σπόγγων": "σπόγγος — sponge (scientific)", "συνθετικά": "συνθετικός — synthetic", "εργαστήρια επεξεργασίας": "εργαστήριο επεξεργασίας — processing workshop"},
})

ITEMS.append({
 "id": "l12-rep-karla", "title": "Η λίμνη που ξαναγεννήθηκε", "title_en": "The lake that was reborn", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τη λίμνη Κάρλα στη Θεσσαλία.",
 "script": [
  L("Δημοσιογράφος", "f", "Η Κάρλα ήταν κάποτε μια μεγάλη λίμνη ανάμεσα στη Λάρισα και τον Βόλο. Οι ψαράδες των γύρω χωριών ζούσαν από αυτήν, με τις ξύλινες βάρκες τους και τις καλαμένιες καλύβες στις όχθες. Το 1962 όμως η λίμνη αποξηράνθηκε, για να δοθούν περισσότερα χωράφια στους αγρότες.", "Karla was once a large lake between Larissa and Volos. The fishermen of the surrounding villages lived from it, with their wooden boats and reed huts on the shores. In 1962, however, the lake was drained to give farmers more fields."),
  L("Δημοσιογράφος", "f", "Το αποτέλεσμα δεν ήταν αυτό που περίμεναν. Το έδαφος αποδείχθηκε αλμυρό και λιγότερο γόνιμο, οι υπόγειοι υδροφορείς άρχισαν να αδειάζουν και ο Βόλος αντιμετώπιζε συχνά πλημμύρες. Χρειάστηκαν δεκαετίες για να παραδεχτεί η πολιτεία ότι η αποξήρανση ήταν λάθος.", "The result was not what they expected. The soil turned out to be salty and less fertile, the underground aquifers began to empty and Volos often faced floods. It took decades for the state to admit that the draining was a mistake."),
  L("Δημοσιογράφος", "f", "Με ένα μεγάλο έργο αποκατάστασης, ένα μέρος της λίμνης γέμισε ξανά νερό. Σήμερα στις όχθες της ξαναβλέπει κανείς φλαμίνγκο, ερωδιούς και πελεκάνους. Δεν είναι πια η παλιά Κάρλα, αλλά για τους ηλικιωμένους των χωριών είναι κάτι σαν επιστροφή ενός χαμένου φίλου.", "With a large restoration project, part of the lake filled with water again. Today on its shores you can again see flamingos, herons and pelicans. It is no longer the old Karla, but for the old people of the villages it is something like the return of a lost friend."),
 ],
 "questions": [
  Q("Γιατί αποξηράνθηκε η λίμνη;", ["Λόγω ξηρασίας", "Για να αποκτήσουν οι αγρότες περισσότερα χωράφια", "Για να χτιστεί αεροδρόμιο", "Εξαιτίας μιας επιδημίας"], 1, "για να δοθούν περισσότερα χωράφια στους αγρότες"),
  Q("Ποιο ήταν ένα από τα αρνητικά αποτελέσματα της αποξήρανσης;", ["Το έδαφος ήταν αλμυρό και λιγότερο γόνιμο", "Αυξήθηκαν τα ψάρια", "Οι αγρότες έγιναν πλούσιοι", "Ο Βόλος έμεινε χωρίς πλημμύρες"], 0, "Το έδαφος αποδείχθηκε αλμυρό και λιγότερο γόνιμο"),
  Q("Πώς είναι η λίμνη σήμερα;", ["Ακριβώς όπως πριν από το 1962", "Ένα μέρος της ξαναγέμισε και επέστρεψαν τα πουλιά", "Είναι εντελώς ξερή", "Έχει γίνει τεχνητή παραλία"], 1, "ένα μέρος της λίμνης γέμισε ξανά νερό ... φλαμίνγκο, ερωδιούς και πελεκάνους"),
 ],
 "gloss": {"καλαμένιες καλύβες": "καλαμένιος — made of reeds; καλύβα — hut", "όχθες": "όχθη — bank, shore (of a lake or river)", "αποξηράνθηκε": "αποξηραίνω — to drain (land, a lake)", "γόνιμο": "γόνιμος — fertile", "υδροφορείς": "υδροφορέας — aquifer", "παραδεχτεί": "παραδέχομαι — to admit", "πολιτεία": "πολιτεία — the state", "αποξήρανση": "αποξήρανση — drainage, draining", "έργο αποκατάστασης": "έργο αποκατάστασης — restoration project", "ερωδιούς": "ερωδιός — heron", "πελεκάνους": "πελεκάνος — pelican"},
})

ITEMS.append({
 "id": "l12-int-vivliopoleio", "title": "Ένα βιβλιοπωλείο στο νησί", "title_en": "A bookshop on the island", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με τον ιδιοκτήτη ενός μικρού βιβλιοπωλείου σε ένα νησί των Κυκλάδων.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς αποφασίσατε να ανοίξετε βιβλιοπωλείο σε ένα νησί με δύο χιλιάδες κατοίκους;", "How did you decide to open a bookshop on an island with two thousand inhabitants?"),
  L("Μάρκος", "m", "Ήταν λίγο τρέλα, το παραδέχομαι. Δούλευα σε έναν μεγάλο εκδοτικό οίκο στην Αθήνα και είχα κουραστεί. Ήρθα εδώ για διακοπές, είδα ένα παλιό μαγαζί κλειστό στο λιμάνι και σκέφτηκα: γιατί όχι;", "It was a bit mad, I admit. I was working at a big publishing house in Athens and I was tired. I came here on holiday, saw an old shop closed at the harbour and thought: why not?"),
  L("Δημοσιογράφος", "f", "Και τον χειμώνα, όταν φεύγουν οι τουρίστες;", "And in winter, when the tourists leave?"),
  L("Μάρκος", "m", "Τον χειμώνα το βιβλιοπωλείο γίνεται κάτι σαν στέκι. Κάνουμε λέσχη ανάγνωσης κάθε Πέμπτη, οργανώνουμε παρουσιάσεις με συγγραφείς μέσω βίντεο, και τα παιδιά του σχολείου έρχονται για την ώρα του παραμυθιού. Τα κέρδη τα βγάζω το καλοκαίρι· τον χειμώνα βγάζω φίλους.", "In winter the bookshop becomes something like a hangout. We hold a reading club every Thursday, organise book presentations with authors by video, and the schoolchildren come for story time. I make my profits in summer; in winter I make friends."),
  L("Δημοσιογράφος", "f", "Δεν σας φοβίζουν οι ηλεκτρονικές πωλήσεις;", "Aren't you afraid of online sales?"),
  L("Μάρκος", "m", "Ένας αλγόριθμος μπορεί να σου προτείνει ένα βιβλίο, αλλά δεν μπορεί να σε κοιτάξει και να καταλάβει ότι σήμερα χρειάζεσαι κάτι αστείο. Αυτό είναι το πλεονέκτημά μας.", "An algorithm can recommend you a book, but it can't look at you and understand that today you need something funny. That is our advantage."),
 ],
 "questions": [
  Q("Τι έκανε ο Μάρκος πριν ανοίξει το βιβλιοπωλείο;", ["Ήταν δάσκαλος στο νησί", "Δούλευε σε εκδοτικό οίκο στην Αθήνα", "Είχε ταβέρνα στο λιμάνι", "Ήταν συγγραφέας"], 1, "Δούλευα σε έναν μεγάλο εκδοτικό οίκο στην Αθήνα"),
  Q("Τι γίνεται στο βιβλιοπωλείο τον χειμώνα;", ["Κλείνει", "Γίνεται χώρος συνάντησης με λέσχη ανάγνωσης και δραστηριότητες", "Πουλάει μόνο σχολικά βιβλία", "Νοικιάζεται σε τουρίστες"], 1, "το βιβλιοπωλείο γίνεται κάτι σαν στέκι. Κάνουμε λέσχη ανάγνωσης"),
  Q("Ποιο θεωρεί πλεονέκτημα του βιβλιοπωλείου απέναντι στις ηλεκτρονικές πωλήσεις;", ["Τις χαμηλότερες τιμές", "Την προσωπική επαφή και την κατανόηση του πελάτη", "Τη γρήγορη παράδοση", "Τη μεγαλύτερη ποικιλία"], 1, "δεν μπορεί να σε κοιτάξει και να καταλάβει ότι σήμερα χρειάζεσαι κάτι αστείο"),
 ],
 "gloss": {"βιβλιοπωλείο": "βιβλιοπωλείο — bookshop", "τρέλα": "τρέλα — madness", "το παραδέχομαι": "παραδέχομαι — to admit", "εκδοτικό οίκο": "εκδοτικός οίκος — publishing house", "στέκι": "στέκι — hangout, regular meeting place", "λέσχη ανάγνωσης": "λέσχη ανάγνωσης — book club", "παρουσιάσεις": "παρουσίαση (βιβλίου) — book launch, presentation", "την ώρα του παραμυθιού": "ώρα του παραμυθιού — story time", "κέρδη": "κέρδος — profit", "αλγόριθμος": "αλγόριθμος — algorithm", "πλεονέκτημά": "πλεονέκτημα — advantage"},
})

ITEMS.append({
 "id": "l12-mon-diarroi", "title": "Η διαρροή εγκεφάλων", "title_en": "The brain drain", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια κοινωνιολόγο να μιλά σε μια ημερίδα για τη διαρροή εγκεφάλων, δηλαδή τη μετανάστευση νέων Ελλήνων με υψηλή μόρφωση κατά την οικονομική κρίση.",
 "script": [
  L("Κοινωνιολόγος", "f", "Κατά τη διάρκεια της οικονομικής κρίσης, εκτιμάται ότι εκατοντάδες χιλιάδες Έλληνες, στη συντριπτική τους πλειονότητα νέοι, εγκατέλειψαν τη χώρα. Το ιδιαίτερο χαρακτηριστικό αυτού του κύματος, σε σύγκριση με τη μετανάστευση της δεκαετίας του '60, είναι το υψηλό μορφωτικό του επίπεδο: γιατροί, μηχανικοί, ερευνητές, πτυχιούχοι με μεταπτυχιακούς τίτλους.", "During the economic crisis, it is estimated that hundreds of thousands of Greeks, the overwhelming majority of them young, left the country. The distinctive feature of this wave, compared with the emigration of the 1960s, is its high level of education: doctors, engineers, researchers, graduates with postgraduate degrees."),
  L("Κοινωνιολόγος", "f", "Το κόστος για τη χώρα είναι διπλό. Αφενός, η Ελλάδα επένδυσε στη δωρεάν εκπαίδευση αυτών των ανθρώπων και τώρα τα οφέλη τα καρπώνονται άλλες οικονομίες. Αφετέρου, η αποχώρησή τους επιδεινώνει το δημογραφικό πρόβλημα, αφού πρόκειται για ανθρώπους σε ηλικία που θα έκαναν οικογένεια.", "The cost for the country is twofold. On the one hand, Greece invested in the free education of these people and now other economies reap the benefits. On the other hand, their departure worsens the demographic problem, since these are people at the age when they would start families."),
  L("Κοινωνιολόγος", "f", "Τα τελευταία χρόνια παρατηρείται μια σταδιακή επιστροφή, την οποία ενθαρρύνουν και φορολογικά κίνητρα. Οι έρευνές μας δείχνουν όμως ότι ο μισθός δεν είναι ο μόνος παράγοντας. Όσοι επιστρέφουν αναφέρουν την οικογένεια και την ποιότητα ζωής· όσοι διστάζουν, μιλούν για την αναξιοκρατία και τη γραφειοκρατία.", "In recent years a gradual return has been observed, which tax incentives also encourage. Our research shows, however, that salary is not the only factor. Those who return mention family and quality of life; those who hesitate speak of the lack of meritocracy and of bureaucracy."),
  L("Κοινωνιολόγος", "f", "Θα ήθελα, τέλος, να προτείνω μια αλλαγή οπτικής. Οι Έλληνες του εξωτερικού δεν είναι απλώς μια απώλεια· αποτελούν ένα δίκτυο γνώσεων και επαφών που, αν το αξιοποιήσουμε, μπορεί να ωφελήσει τη χώρα ακόμη κι αν οι περισσότεροι δεν επιστρέψουν ποτέ.", "Finally, I would like to propose a change of perspective. Greeks abroad are not simply a loss; they form a network of knowledge and contacts which, if we make use of it, can benefit the country even if most of them never return."),
 ],
 "questions": [
  Q("Σε τι διαφέρει το μεταναστευτικό κύμα της κρίσης από εκείνο της δεκαετίας του '60;", ["Στον αριθμό των ανθρώπων", "Στο υψηλό μορφωτικό επίπεδο των μεταναστών", "Στις χώρες προορισμού", "Στο ότι έφυγαν κυρίως ηλικιωμένοι"], 1, "το υψηλό μορφωτικό του επίπεδο"),
  Q("Ποιο είναι το «διπλό κόστος» για τη χώρα;", ["Η απώλεια της επένδυσης στην εκπαίδευση και η επιδείνωση του δημογραφικού", "Η μείωση των φόρων και η ανεργία", "Η αύξηση των μισθών και ο πληθωρισμός", "Η απώλεια τουριστών και επενδυτών"], 0, "Αφενός ... δωρεάν εκπαίδευση ... Αφετέρου ... επιδεινώνει το δημογραφικό πρόβλημα"),
  Q("Τι αναφέρουν όσοι διστάζουν να επιστρέψουν;", ["Τους χαμηλούς μισθούς μόνο", "Την αναξιοκρατία και τη γραφειοκρατία", "Το κλίμα", "Την έλλειψη σχολείων"], 1, "όσοι διστάζουν, μιλούν για την αναξιοκρατία και τη γραφειοκρατία"),
  Q("Ποια αλλαγή οπτικής προτείνει η ομιλήτρια;", ["Να απαγορευτεί η μετανάστευση", "Να θεωρηθούν οι απόδημοι δίκτυο που μπορεί να ωφελήσει τη χώρα", "Να αυξηθούν οι φόροι για όσους έφυγαν", "Να σταματήσουν τα κίνητρα επιστροφής"], 1, "αποτελούν ένα δίκτυο γνώσεων και επαφών που, αν το αξιοποιήσουμε, μπορεί να ωφελήσει τη χώρα"),
 ],
 "gloss": {"διαρροή εγκεφάλων": "διαρροή εγκεφάλων — brain drain", "ημερίδα": "ημερίδα — one-day conference", "συντριπτική τους πλειονότητα": "συντριπτική πλειονότητα — overwhelming majority", "εγκατέλειψαν": "εγκαταλείπω — to leave, abandon", "μορφωτικό του επίπεδο": "μορφωτικό επίπεδο — level of education", "μεταπτυχιακούς τίτλους": "μεταπτυχιακός τίτλος — postgraduate degree", "Αφενός": "αφενός … αφετέρου — on the one hand … on the other", "καρπώνονται": "καρπώνομαι — to reap (benefits)", "επιδεινώνει": "επιδεινώνω — to worsen", "δημογραφικό πρόβλημα": "δημογραφικό (πρόβλημα) — falling birth rate and ageing population", "φορολογικά κίνητρα": "φορολογικό κίνητρο — tax incentive", "αναξιοκρατία": "αναξιοκρατία — lack of meritocracy", "γραφειοκρατία": "γραφειοκρατία — bureaucracy", "οπτικής": "οπτική — perspective", "αξιοποιήσουμε": "αξιοποιώ — to make good use of"},
})

ITEMS.append({
 "id": "l12-int-texniti", "title": "Η τεχνητή νοημοσύνη και η δουλειά μας", "title_en": "Artificial intelligence and our jobs", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια καθηγήτρια πληροφορικής για τις επιπτώσεις της τεχνητής νοημοσύνης στην εργασία.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί ακροατές μας ανησυχούν ότι η τεχνητή νοημοσύνη θα τους πάρει τη δουλειά. Είναι βάσιμος αυτός ο φόβος;", "Many of our listeners worry that artificial intelligence will take their jobs. Is this fear well founded?"),
  L("Καθηγήτρια", "f", "Είναι κατανοητός, αλλά χρειάζεται μια διευκρίνιση. Τα συστήματα αυτά σπάνια αντικαθιστούν ολόκληρα επαγγέλματα· αυτοματοποιούν κυρίως συγκεκριμένες εργασίες μέσα σε ένα επάγγελμα. Ένας μεταφραστής, για παράδειγμα, μπορεί να χρησιμοποιεί ένα πρώτο αυτόματο προσχέδιο, αλλά η ευθύνη για την ακρίβεια και το ύφος παραμένει δική του.", "It is understandable, but it needs a clarification. These systems rarely replace entire professions; they mainly automate specific tasks within a profession. A translator, for example, may use an automatic first draft, but responsibility for accuracy and style remains theirs."),
  L("Δημοσιογράφος", "m", "Δηλαδή δεν θα χαθούν θέσεις εργασίας;", "So no jobs will be lost?"),
  L("Καθηγήτρια", "f", "Δεν είπα αυτό. Ορισμένες θέσεις, ιδίως σε επαναλαμβανόμενες γραφειακές εργασίες, θα μειωθούν, και η μετάβαση θα είναι επώδυνη για όσους δεν έχουν πρόσβαση σε επανεκπαίδευση. Η ιστορία της τεχνολογίας δείχνει ότι δημιουργούνται και νέα επαγγέλματα, αλλά όχι απαραίτητα για τους ίδιους ανθρώπους ούτε στον ίδιο τόπο.", "I didn't say that. Some positions, especially in repetitive office tasks, will decrease, and the transition will be painful for those who have no access to retraining. The history of technology shows that new professions are also created, but not necessarily for the same people or in the same place."),
  L("Δημοσιογράφος", "m", "Τι θα συμβουλεύατε έναν νέο που διαλέγει σήμερα σπουδές;", "What would you advise a young person choosing what to study today?"),
  L("Καθηγήτρια", "f", "Να μη διαλέξει με βάση το ποιο επάγγελμα θα «επιβιώσει», γιατί κανείς δεν το ξέρει με βεβαιότητα. Να καλλιεργήσει δεξιότητες που δύσκολα αυτοματοποιούνται: κριτική σκέψη, συνεργασία, την ικανότητα να διατυπώνει σωστά ένα πρόβλημα. Και να είναι έτοιμος να μαθαίνει σε όλη του τη ζωή.", "Not to choose on the basis of which profession will \"survive\", because nobody knows that for certain. To cultivate skills that are hard to automate: critical thinking, collaboration, the ability to formulate a problem properly. And to be ready to keep learning throughout life."),
 ],
 "questions": [
  Q("Σύμφωνα με την καθηγήτρια, τι κάνουν κυρίως τα συστήματα τεχνητής νοημοσύνης;", ["Αντικαθιστούν ολόκληρα επαγγέλματα", "Αυτοματοποιούν συγκεκριμένες εργασίες μέσα σε ένα επάγγελμα", "Δημιουργούν μόνο νέες θέσεις εργασίας", "Δεν επηρεάζουν καθόλου την εργασία"], 1, "αυτοματοποιούν κυρίως συγκεκριμένες εργασίες μέσα σε ένα επάγγελμα"),
  Q("Για ποιους θα είναι επώδυνη η μετάβαση;", ["Για τους καθηγητές πληροφορικής", "Για όσους δεν έχουν πρόσβαση σε επανεκπαίδευση", "Για τους μεταφραστές μόνο", "Για τους εργοδότες"], 1, "η μετάβαση θα είναι επώδυνη για όσους δεν έχουν πρόσβαση σε επανεκπαίδευση"),
  Q("Τι συμβουλεύει τους νέους;", ["Να σπουδάσουν οπωσδήποτε πληροφορική", "Να διαλέξουν το επάγγελμα που θα επιβιώσει", "Να καλλιεργήσουν δεξιότητες που δύσκολα αυτοματοποιούνται και να μαθαίνουν διαρκώς", "Να αποφύγουν τις γραφειακές δουλειές"], 2, "Να καλλιεργήσει δεξιότητες που δύσκολα αυτοματοποιούνται ... Και να είναι έτοιμος να μαθαίνει σε όλη του τη ζωή."),
 ],
 "gloss": {"τεχνητή νοημοσύνη": "τεχνητή νοημοσύνη — artificial intelligence", "βάσιμος": "βάσιμος — well-founded", "κατανοητός": "κατανοητός — understandable", "διευκρίνιση": "διευκρίνιση — clarification", "αυτοματοποιούν": "αυτοματοποιώ — to automate", "προσχέδιο": "προσχέδιο — draft", "ύφος": "ύφος — style", "επαναλαμβανόμενες": "επαναλαμβανόμενος — repetitive", "γραφειακές εργασίες": "γραφειακή εργασία — office work", "μετάβαση": "μετάβαση — transition", "επώδυνη": "επώδυνος — painful", "επανεκπαίδευση": "επανεκπαίδευση — retraining", "δεξιότητες": "δεξιότητα — skill", "κριτική σκέψη": "κριτική σκέψη — critical thinking", "να διατυπώνει": "διατυπώνω — to formulate, put into words"},
})
rnd = random.Random(12)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-12.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
