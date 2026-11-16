# Source for library/listening/listening-72.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l72.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l72-ann-prin-tin-parastasi", "title": "Λίγο πριν από την παράσταση", "title_en": "Just before the performance", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα αρχαίο θέατρο για μια καλοκαιρινή παράσταση. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνητής", "m", "Κυρίες και κύριοι, καλησπέρα σας. Η παράσταση θα αρχίσει σε δέκα λεπτά. Παρακαλούμε όσους βρίσκονται ακόμη στα σκαλιά να πάρουν τις θέσεις τους, για να μην ενοχλούνται οι υπόλοιποι θεατές μετά την έναρξη.", "Ladies and gentlemen, good evening. The performance will begin in ten minutes. We ask those who are still on the steps to take their seats, so that the other spectators are not disturbed after the start."),
  L("Εκφωνητής", "m", "Σας υπενθυμίζουμε ότι απαγορεύεται η φωτογράφιση και η βιντεοσκόπηση κατά τη διάρκεια της παράστασης. Τα κινητά τηλέφωνα πρέπει να είναι απενεργοποιημένα, γιατί ακόμη και το φως της οθόνης φαίνεται από τη σκηνή.", "We remind you that photography and video recording are prohibited during the performance. Mobile phones must be switched off, because even the light of the screen can be seen from the stage."),
  L("Εκφωνητής", "m", "Η παράσταση διαρκεί περίπου δύο ώρες, χωρίς διάλειμμα. Μετά το τέλος, τα λεωφορεία για το Ναύπλιο θα αναχωρούν από τον κάτω χώρο στάθμευσης. Σας ευχόμαστε καλή διασκέδαση.", "The performance lasts about two hours, without an interval. After the end, buses to Nafplio will leave from the lower car park. We wish you an enjoyable evening."),
 ],
 "questions": [
  Q("Τι ζητείται από όσους είναι ακόμη στα σκαλιά;", ["Να βγουν από το θέατρο", "Να πάρουν τις θέσεις τους", "Να αγοράσουν εισιτήριο", "Να περιμένουν το διάλειμμα"], 1, "να πάρουν τις θέσεις τους"),
  Q("Γιατί πρέπει να είναι απενεργοποιημένα τα κινητά;", ["Γιατί χαλάνε τον ήχο", "Γιατί το φως της οθόνης φαίνεται από τη σκηνή", "Γιατί δεν υπάρχει σήμα", "Γιατί το ζητάει ο σκηνοθέτης"], 1, "ακόμη και το φως της οθόνης φαίνεται από τη σκηνή"),
  Q("Από πού θα αναχωρούν τα λεωφορεία;", ["Από την είσοδο του θεάτρου", "Από τον κάτω χώρο στάθμευσης", "Από το Ναύπλιο", "Από το εκδοτήριο"], 1, "θα αναχωρούν από τον κάτω χώρο στάθμευσης"),
 ],
 "gloss": {"παράσταση": "παράσταση — performance", "σκαλιά": "σκαλί — step (here: tiers of the theatre)", "έναρξη": "έναρξη — start", "φωτογράφιση": "φωτογράφιση — photography", "βιντεοσκόπηση": "βιντεοσκόπηση — video recording", "απενεργοποιημένα": "απενεργοποιημένος — switched off", "διάλειμμα": "διάλειμμα — interval", "χώρο στάθμευσης": "χώρος στάθμευσης — car park"},
})

ITEMS.append({
 "id": "l72-vm-ergolavos-taratsa", "title": "Η μόνωση της ταράτσας", "title_en": "Insulating the roof terrace", "type": "voicemail", "level": "B2",
 "context_el": "Είστε διαχειριστής σε μια πολυκατοικία. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τον εργολάβο που θα κάνει τη μόνωση της ταράτσας.",
 "script": [
  L("Εργολάβος", "m", "Καλημέρα σας, ο Παπαδάκης είμαι, για τη μόνωση της ταράτσας. Ανέβηκα χθες με τον συνεργάτη μου και είδαμε ότι η παλιά μεμβράνη έχει φουσκώσει σε πολλά σημεία. Δεν αρκεί να βάλουμε νέα από πάνω· πρέπει πρώτα να ξηλωθεί η παλιά.", "Good morning, it's Papadakis, about the roof insulation. I went up yesterday with my colleague and we saw that the old membrane has blistered in many places. It's not enough to lay a new one on top; the old one has to be stripped off first."),
  L("Εργολάβος", "m", "Αυτό σημαίνει δύο μέρες δουλειά παραπάνω και ένα επιπλέον κόστος, περίπου τετρακόσια ευρώ. Θα σας στείλω τη νέα προσφορά με ηλεκτρονικό ταχυδρομείο, για να τη δείξετε στους ενοίκους στη γενική συνέλευση.", "That means two more days of work and an extra cost of about four hundred euros. I'll send you the new quote by email so you can show it to the residents at the general meeting."),
  L("Εργολάβος", "m", "Το σημαντικό είναι να τελειώσουμε πριν από τις πρώτες βροχές. Αν πάρετε απόφαση μέσα στην εβδομάδα, ξεκινάμε τη Δευτέρα. Παρακαλώ, ενημερώστε τους ενοίκους να μην απλώνουν ρούχα στην ταράτσα όσο δουλεύουμε.", "The important thing is to finish before the first rains. If you make a decision within the week, we start on Monday. Please let the residents know not to hang washing on the roof while we're working."),
 ],
 "questions": [
  Q("Τι διαπίστωσε ο εργολάβος στην ταράτσα;", ["Ότι η μόνωση είναι σε καλή κατάσταση", "Ότι η παλιά μεμβράνη έχει φουσκώσει σε πολλά σημεία", "Ότι λείπουν τα κάγκελα", "Ότι η ταράτσα είναι πολύ μικρή"], 1, "η παλιά μεμβράνη έχει φουσκώσει σε πολλά σημεία"),
  Q("Γιατί θα στείλει νέα προσφορά;", ["Για να τη δουν οι ένοικοι στη γενική συνέλευση", "Γιατί έχασε την παλιά", "Για να πληρωθεί αμέσως", "Γιατί άλλαξε ο ΦΠΑ"], 0, "για να τη δείξετε στους ενοίκους στη γενική συνέλευση"),
  Q("Τι πρέπει να αποφύγουν οι ένοικοι όσο κρατούν οι εργασίες;", ["Να χρησιμοποιούν το ασανσέρ", "Να απλώνουν ρούχα στην ταράτσα", "Να παρκάρουν μπροστά στην είσοδο", "Να ανοίγουν τα παράθυρα"], 1, "να μην απλώνουν ρούχα στην ταράτσα όσο δουλεύουμε"),
 ],
 "gloss": {"διαχειριστής": "διαχειριστής — building manager (of a block of flats)", "εργολάβο": "εργολάβος — contractor", "μόνωση": "μόνωση — insulation", "μεμβράνη": "μεμβράνη — (waterproof) membrane", "φουσκώσει": "φουσκώνω — to swell, blister", "ξηλωθεί": "ξηλώνω — to strip off, tear out", "προσφορά": "προσφορά — quote", "ενοίκους": "ένοικος — resident", "γενική συνέλευση": "γενική συνέλευση — general meeting", "απλώνουν": "απλώνω — to hang out (washing)"},
})

ITEMS.append({
 "id": "l72-dia-koinos-logariasmos", "title": "Κοινός λογαριασμός ή χωριστά;", "title_en": "Joint account or separate?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι που μόλις άρχισε να μένει μαζί συζητά πώς θα χειρίζεται τα χρήματα.",
 "script": [
  L("Ιάσονας", "m", "Σκεφτόμουν να ανοίξουμε έναν κοινό λογαριασμό. Να βάζουμε εκεί και οι δύο τον μισθό μας και να πληρώνουμε απ' αυτόν τα πάντα. Έτσι δεν θα κρατάμε λογαριασμό ποιος πλήρωσε τι.", "I was thinking we should open a joint account. We'd both put our salaries there and pay for everything from it. That way we won't keep track of who paid what."),
  L("Δανάη", "f", "Ναι, αλλά εσύ βγάζεις σχεδόν τα διπλά από μένα. Δεν θέλω να νιώθω ότι ζω με τα δικά σου λεφτά. Και, για να είμαι ειλικρινής, μου αρέσει να έχω και κάτι δικό μου, να αγοράζω ένα δώρο χωρίς να το βλέπεις στην κίνηση του λογαριασμού.", "Yes, but you earn almost twice as much as I do. I don't want to feel I'm living on your money. And, to be honest, I like having something of my own too, to buy a present without you seeing it in the account statement."),
  L("Ιάσονας", "m", "Δίκιο έχεις. Τι λες για κάτι ενδιάμεσο; Ένας κοινός λογαριασμός για το ενοίκιο, το σούπερ μάρκετ και τους λογαριασμούς, και ο καθένας κρατάει τον δικό του για τα υπόλοιπα.", "You're right. What about something in between? A joint account for the rent, the supermarket and the bills, and each of us keeps our own for everything else."),
  L("Δανάη", "f", "Μου αρέσει. Και να μη βάζουμε το ίδιο ποσό, αλλά το ίδιο ποσοστό του μισθού μας, ας πούμε το εξήντα τοις εκατό. Έτσι είναι πιο δίκαιο και για τους δύο.", "I like it. And let's not put in the same amount, but the same percentage of our salaries, say sixty per cent. That way it's fairer for both of us."),
 ],
 "questions": [
  Q("Τι προτείνει αρχικά ο Ιάσονας;", ["Να μην έχουν καθόλου κοινά έξοδα", "Να βάζουν όλο τον μισθό τους σε έναν κοινό λογαριασμό", "Να πληρώνει εκείνος τα πάντα", "Να ανοίξουν λογαριασμό ταμιευτηρίου"], 1, "Να βάζουμε εκεί και οι δύο τον μισθό μας"),
  Q("Γιατί διστάζει η Δανάη;", ["Γιατί δεν εμπιστεύεται τις τράπεζες", "Γιατί εκείνος κερδίζει πολύ περισσότερα και θέλει κάτι δικό της", "Γιατί έχει χρέη", "Γιατί θέλει να μείνει μόνη"], 1, "εσύ βγάζεις σχεδόν τα διπλά από μένα"),
  Q("Πώς θα μοιράζονται τελικά τα κοινά έξοδα;", ["Ο καθένας θα βάζει το ίδιο ποσό", "Ο καθένας θα βάζει το ίδιο ποσοστό του μισθού του", "Θα πληρώνει μόνο ο Ιάσονας", "Θα πληρώνουν εκ περιτροπής"], 1, "το ίδιο ποσοστό του μισθού μας"),
 ],
 "gloss": {"χειρίζεται": "χειρίζομαι — to handle, manage", "κοινό λογαριασμό": "κοινός λογαριασμός — joint (bank) account", "μισθό": "μισθός — salary", "βγάζεις": "βγάζω — to earn (colloquial)", "κίνηση του λογαριασμού": "κίνηση λογαριασμού — account statement, transactions", "ενδιάμεσο": "ενδιάμεσος — intermediate, in between", "ποσό": "ποσό — amount", "ποσοστό": "ποσοστό — percentage"},
})

ITEMS.append({
 "id": "l72-dia-allagi-epaggelmatos", "title": "Αλλαγή επαγγέλματος στα σαράντα", "title_en": "A career change at forty", "type": "dialogue", "level": "B2",
 "context_el": "Δύο παλιές συμμαθήτριες συναντιούνται σε ένα καφέ και η μία λέει στην άλλη για ένα μεγάλο σχέδιο.",
 "script": [
  L("Στέλλα", "f", "Λοιπόν, ποιο είναι το μεγάλο νέο που μου έλεγες στο τηλέφωνο;", "So, what's the big news you were telling me about on the phone?"),
  L("Κατερίνα", "f", "Παραιτούμαι από την τράπεζα. Δεκαοχτώ χρόνια πίσω από ένα γκισέ, Στέλλα. Γράφτηκα σε σχολή αρτοποιίας και από τον Σεπτέμβριο κάνω πρακτική σε έναν φούρνο στο Παγκράτι.", "I'm resigning from the bank. Eighteen years behind a counter, Stella. I've enrolled in a baking school and from September I'm doing an internship at a bakery in Pangrati."),
  L("Στέλλα", "f", "Φούρνο; Μα εσύ σιχαινόσουν να ξυπνάς νωρίς! Οι φούρναρηδες σηκώνονται στις τρεις. Και τα λεφτά; Θα πάρεις πολύ λιγότερα στην αρχή.", "A bakery? But you hated getting up early! Bakers get up at three. And the money? You'll earn much less at first."),
  L("Κατερίνα", "f", "Το ξέρω, και το σκέφτηκα πολύ. Έχω κάνει οικονομίες για δύο χρόνια, και ο Μάρκος με στηρίζει. Όσο για το ξύπνημα, προτιμώ να σηκώνομαι στις τρεις για κάτι που αγαπώ, παρά στις επτά για κάτι που με αρρωσταίνει. Αν δεν το κάνω τώρα, δεν θα το κάνω ποτέ.", "I know, and I thought about it a lot. I've saved for two years, and Markos supports me. As for getting up, I'd rather get up at three for something I love than at seven for something that makes me ill. If I don't do it now, I'll never do it."),
 ],
 "questions": [
  Q("Πού θα κάνει πρακτική η Κατερίνα;", ["Σε μια τράπεζα", "Σε έναν φούρνο στο Παγκράτι", "Σε ένα ζαχαροπλαστείο", "Σε μια σχολή μαγειρικής"], 1, "κάνω πρακτική σε έναν φούρνο στο Παγκράτι"),
  Q("Τι ανησυχεί τη Στέλλα;", ["Ότι η Κατερίνα δεν ξέρει να ψήνει", "Το πρωινό ξύπνημα και τα λιγότερα χρήματα", "Ότι ο φούρνος είναι μακριά", "Ότι η σχολή είναι ακριβή"], 1, "Θα πάρεις πολύ λιγότερα στην αρχή"),
  Q("Πώς έχει προετοιμαστεί η Κατερίνα;", ["Έχει πάρει δάνειο", "Έχει κάνει οικονομίες για δύο χρόνια", "Έχει βρει δεύτερη δουλειά", "Δεν έχει προετοιμαστεί καθόλου"], 1, "Έχω κάνει οικονομίες για δύο χρόνια"),
 ],
 "gloss": {"Παραιτούμαι": "παραιτούμαι — to resign", "γκισέ": "γκισέ — counter (in a bank, post office)", "αρτοποιίας": "αρτοποιία — bread-making, baking", "πρακτική": "πρακτική — internship", "σιχαινόσουν": "σιχαίνομαι — to loathe", "φούρναρηδες": "φούρναρης — baker", "οικονομίες": "οικονομίες — savings", "στηρίζει": "στηρίζω — to support"},
})

ITEMS.append({
 "id": "l72-int-skyloi-odigoi", "title": "Η εκπαιδεύτρια σκύλων-οδηγών", "title_en": "The guide-dog trainer", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη σε ραδιοφωνική εκπομπή με μια γυναίκα που εκπαιδεύει σκύλους-οδηγούς για τυφλούς.",
 "script": [
  L("Δημοσιογράφος", "f", "Κυρία Σαββίδου, πόσος χρόνος χρειάζεται για να γίνει ένα κουτάβι σκύλος-οδηγός;", "Ms Savvidou, how long does it take for a puppy to become a guide dog?"),
  L("Ευανθία", "f", "Σχεδόν δύο χρόνια. Τον πρώτο χρόνο το κουτάβι ζει με μια εθελοντική οικογένεια, που του μαθαίνει να κυκλοφορεί σε λεωφορεία, σε καταστήματα, σε δρόμους με θόρυβο. Μετά έρχεται σε εμάς για την κανονική εκπαίδευση, που κρατάει περίπου έξι μήνες.", "Almost two years. In the first year the puppy lives with a volunteer family, who teach it to get around on buses, in shops, on noisy streets. Then it comes to us for the proper training, which lasts about six months."),
  L("Δημοσιογράφος", "f", "Τι είναι το πιο δύσκολο να μάθει ένας σκύλος;", "What's the hardest thing for a dog to learn?"),
  L("Ευανθία", "f", "Η «έξυπνη ανυπακοή». Ο σκύλος πρέπει να αρνηθεί μια εντολή, αν είναι επικίνδυνη. Αν ο άνθρωπος του πει «εμπρός» και έρχεται αυτοκίνητο, ο σκύλος μένει ακίνητος. Δεν το κάνουν όλοι· περίπου ένας στους δύο σκύλους δεν ολοκληρώνει την εκπαίδευση.", "'Intelligent disobedience'. The dog must refuse a command if it is dangerous. If its person says 'forward' and a car is coming, the dog stays still. Not all of them manage it; about one in two dogs doesn't complete the training."),
  L("Δημοσιογράφος", "f", "Τι θέλετε να ξέρουν οι ακροατές μας;", "What would you like our listeners to know?"),
  L("Ευανθία", "f", "Δύο πράγματα. Πρώτον, όταν ένας σκύλος φοράει το λουρί εργασίας, δεν τον χαϊδεύουμε και δεν του δίνουμε φαγητό· δουλεύει. Δεύτερον, ο νόμος επιτρέπει στους σκύλους-οδηγούς να μπαίνουν παντού, σε ταξί, εστιατόρια, νοσοκομεία. Κι όμως, πολλοί τυφλοί ακόμη ακούνε «απαγορεύονται τα ζώα».", "Two things. First, when a dog is wearing its working harness, we don't stroke it and we don't give it food; it's working. Second, the law allows guide dogs to go everywhere, in taxis, restaurants, hospitals. And yet many blind people still hear 'no animals allowed'."),
 ],
 "questions": [
  Q("Τι κάνει το κουτάβι τον πρώτο χρόνο;", ["Εκπαιδεύεται σε ειδική σχολή", "Ζει με μια εθελοντική οικογένεια", "Ζει με τον τυφλό ιδιοκτήτη του", "Μένει σε κτηνιατρείο"], 1, "Τον πρώτο χρόνο το κουτάβι ζει με μια εθελοντική οικογένεια"),
  Q("Τι είναι η «έξυπνη ανυπακοή»;", ["Να μην υπακούει ποτέ ο σκύλος", "Να αρνείται ο σκύλος μια εντολή, αν είναι επικίνδυνη", "Να μαθαίνει μόνος του δρομολόγια", "Να γαβγίζει στα αυτοκίνητα"], 1, "Ο σκύλος πρέπει να αρνηθεί μια εντολή, αν είναι επικίνδυνη"),
  Q("Τι δεν πρέπει να κάνουμε όταν ο σκύλος φοράει το λουρί εργασίας;", ["Να του μιλάμε στον τυφλό", "Να τον χαϊδεύουμε και να του δίνουμε φαγητό", "Να περπατάμε δίπλα του", "Να τον κοιτάζουμε"], 1, "δεν τον χαϊδεύουμε και δεν του δίνουμε φαγητό"),
 ],
 "gloss": {"σκύλους-οδηγούς": "σκύλος-οδηγός — guide dog", "τυφλούς": "τυφλός — blind (person)", "κουτάβι": "κουτάβι — puppy", "εθελοντική": "εθελοντικός — volunteer", "ανυπακοή": "ανυπακοή — disobedience", "εντολή": "εντολή — command", "ακίνητος": "ακίνητος — motionless", "λουρί εργασίας": "λουρί εργασίας — working harness", "χαϊδεύουμε": "χαϊδεύω — to stroke, pet"},
})

ITEMS.append({
 "id": "l72-rep-karla", "title": "Η λίμνη Κάρλα ξαναζωντανεύει", "title_en": "Lake Karla comes back to life", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από ραδιοφωνική εκπομπή για το περιβάλλον.",
 "script": [
  L("Ρεπόρτερ", "m", "Η Κάρλα ήταν κάποτε μια από τις μεγαλύτερες λίμνες της Θεσσαλίας. Οι ψαράδες των γύρω χωριών ζούσαν από αυτήν για αιώνες. Το 1962, όμως, η λίμνη αποξηράνθηκε, για να κερδίσουν οι αγρότες καλλιεργήσιμη γη και να σταματήσουν οι πλημμύρες.", "Karla was once one of the largest lakes in Thessaly. The fishermen of the surrounding villages lived from it for centuries. In 1962, however, the lake was drained, so that farmers could gain arable land and the floods would stop."),
  L("Ρεπόρτερ", "m", "Το αποτέλεσμα δεν ήταν αυτό που περίμεναν. Τα χωράφια συχνά πλημμύριζαν, τα υπόγεια νερά λιγόστεψαν και η περιοχή έχασε τα πουλιά και τους ψαράδες της. Γι' αυτό, τις τελευταίες δεκαετίες, ένα μεγάλο έργο αποκατάστασης έφερε ξανά νερό σε ένα μέρος της παλιάς λίμνης.", "The result was not what they expected. The fields often flooded, groundwater dwindled, and the area lost its birds and its fishermen. That's why, in recent decades, a large restoration project brought water back to part of the old lake."),
  L("Ρεπόρτερ", "m", "Σήμερα στους υγροτόπους της Κάρλας ξεχειμωνιάζουν χιλιάδες πουλιά, ανάμεσά τους φλαμίνγκο και πελεκάνοι. Οι παλιοί ψαράδες λένε ότι δεν περίμεναν να ξαναδούν τέτοια εικόνα. Οι επιστήμονες, ωστόσο, προειδοποιούν ότι η λίμνη χρειάζεται καθαρό νερό και προσεκτική διαχείριση, για να μην επαναληφθούν τα λάθη του παρελθόντος.", "Today thousands of birds winter in the wetlands of Karla, among them flamingos and pelicans. The old fishermen say they did not expect to see such a sight again. Scientists, however, warn that the lake needs clean water and careful management, so that the mistakes of the past are not repeated."),
 ],
 "questions": [
  Q("Γιατί αποξηράνθηκε η λίμνη το 1962;", ["Για να χτιστεί αεροδρόμιο", "Για να κερδίσουν οι αγρότες γη και να σταματήσουν οι πλημμύρες", "Γιατί είχε μολυνθεί", "Για να φτιαχτεί δρόμος"], 1, "για να κερδίσουν οι αγρότες καλλιεργήσιμη γη και να σταματήσουν οι πλημμύρες"),
  Q("Ποιο ήταν το αποτέλεσμα της αποξήρανσης;", ["Οι πλημμύρες σταμάτησαν οριστικά", "Τα υπόγεια νερά λιγόστεψαν και χάθηκαν τα πουλιά", "Η περιοχή γέμισε τουρίστες", "Οι ψαράδες έγιναν πλούσιοι"], 1, "τα υπόγεια νερά λιγόστεψαν και η περιοχή έχασε τα πουλιά"),
  Q("Τι λένε οι επιστήμονες σήμερα;", ["Ότι η λίμνη δεν θα επιβιώσει", "Ότι χρειάζεται καθαρό νερό και προσεκτική διαχείριση", "Ότι πρέπει να ξαναποξηρανθεί", "Ότι τα πουλιά είναι πολλά"], 1, "η λίμνη χρειάζεται καθαρό νερό και προσεκτική διαχείριση"),
 ],
 "gloss": {"αποξηράνθηκε": "αποξηραίνω — to drain (a lake, marsh)", "καλλιεργήσιμη": "καλλιεργήσιμος — arable", "πλημμύρες": "πλημμύρα — flood", "υπόγεια νερά": "υπόγεια νερά — groundwater", "λιγόστεψαν": "λιγοστεύω — to dwindle", "αποκατάστασης": "αποκατάσταση — restoration", "υγροτόπους": "υγρότοπος — wetland", "ξεχειμωνιάζουν": "ξεχειμωνιάζω — to spend the winter", "πελεκάνοι": "πελεκάνος — pelican", "διαχείριση": "διαχείριση — management"},
})

ITEMS.append({
 "id": "l72-mono-imikranies", "title": "Ζώντας με τις ημικρανίες", "title_en": "Living with migraines", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να μιλά σε ένα podcast για την υγεία.",
 "script": [
  L("Αλίκη", "f", "Έχω ημικρανίες από τα δεκατέσσερά μου. Πολλοί νομίζουν ότι η ημικρανία είναι ένας δυνατός πονοκέφαλος. Δεν είναι. Μια κρίση μπορεί να κρατήσει δύο μέρες: δεν αντέχω το φως, ούτε τον παραμικρό θόρυβο, και συχνά κάνω εμετό. Μένω στο σκοτάδι και περιμένω να περάσει.", "I've had migraines since I was fourteen. Many people think a migraine is a bad headache. It isn't. An attack can last two days: I can't stand light, or the slightest noise, and I'm often sick. I stay in the dark and wait for it to pass."),
  L("Αλίκη", "f", "Για χρόνια ντρεπόμουν να το πω στη δουλειά. Φοβόμουν ότι θα με θεωρήσουν τεμπέλα. Ένας νευρολόγος με βοήθησε πολύ: μου είπε να κρατάω ημερολόγιο, για να βρω τι προκαλεί τις κρίσεις. Ανακάλυψα ότι για μένα φταίνε η έλλειψη ύπνου, το κρασί και οι μέρες που δεν τρώω στην ώρα μου.", "For years I was embarrassed to say it at work. I was afraid they'd think I was lazy. A neurologist helped me a lot: he told me to keep a diary to find out what triggers the attacks. I discovered that for me the culprits are lack of sleep, wine and the days when I don't eat on time."),
  L("Αλίκη", "f", "Σήμερα έχω πολύ λιγότερες κρίσεις, χάρη σε μια προληπτική θεραπεία και σε ένα πιο σταθερό πρόγραμμα. Αυτό που θέλω να πω σε όσους έχουν ημικρανίες είναι: μη ζητάτε συγγνώμη. Είναι μια πραγματική ασθένεια, όχι μια δικαιολογία.", "Today I have far fewer attacks, thanks to a preventive treatment and a more regular routine. What I want to say to people with migraines is: don't apologise. It's a real illness, not an excuse."),
 ],
 "questions": [
  Q("Πώς περιγράφει η Αλίκη μια κρίση ημικρανίας;", ["Ως έναν απλό πονοκέφαλο", "Μπορεί να κρατήσει δύο μέρες και δεν αντέχει φως και θόρυβο", "Κρατάει λίγα λεπτά", "Περνάει με έναν καφέ"], 1, "Μια κρίση μπορεί να κρατήσει δύο μέρες"),
  Q("Γιατί κρατούσε ημερολόγιο;", ["Για να το δείξει στη δουλειά", "Για να βρει τι προκαλεί τις κρίσεις", "Για να γράψει ένα βιβλίο", "Για να θυμάται τα φάρμακα"], 1, "για να βρω τι προκαλεί τις κρίσεις"),
  Q("Τι θέλει να πει σε όσους έχουν ημικρανίες;", ["Να αλλάξουν δουλειά", "Να μη ζητούν συγγνώμη, γιατί είναι πραγματική ασθένεια", "Να μην παίρνουν φάρμακα", "Να κρύβουν το πρόβλημά τους"], 1, "μη ζητάτε συγγνώμη"),
 ],
 "gloss": {"ημικρανίες": "ημικρανία — migraine", "κρίση": "κρίση — attack", "παραμικρό": "παραμικρός — slightest", "εμετό": "εμετός — vomiting", "τεμπέλα": "τεμπέλης, τεμπέλα — lazy", "νευρολόγος": "νευρολόγος — neurologist", "προληπτική": "προληπτικός — preventive", "δικαιολογία": "δικαιολογία — excuse"},
})

ITEMS.append({
 "id": "l72-mono-mitriko-gala", "title": "Δότρια μητρικού γάλακτος", "title_en": "A breast-milk donor", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια νέα μητέρα να μιλά σε μια εκδήλωση για τη μητρότητα.",
 "script": [
  L("Ναταλία", "f", "Όταν γεννήθηκε η κόρη μου, είχα τόσο πολύ γάλα, που δεν ήξερα τι να το κάνω. Μια μαία στο μαιευτήριο μού μίλησε για την τράπεζα μητρικού γάλακτος. Δεν ήξερα καν ότι υπάρχει κάτι τέτοιο.", "When my daughter was born, I had so much milk that I didn't know what to do with it. A midwife at the maternity hospital told me about the human milk bank. I didn't even know such a thing existed."),
  L("Ναταλία", "f", "Το γάλα αυτό το χρειάζονται κυρίως πρόωρα μωρά, που ζυγίζουν μερικές φορές λιγότερο από ένα κιλό. Οι μητέρες τους, από το άγχος ή από τον τοκετό, συχνά δεν έχουν ακόμη γάλα. Για αυτά τα μωρά το μητρικό γάλα είναι σχεδόν φάρμακο.", "This milk is needed mainly by premature babies, who sometimes weigh less than a kilo. Their mothers, because of stress or the birth itself, often don't have milk yet. For these babies breast milk is almost a medicine."),
  L("Ναταλία", "f", "Πριν γίνω δότρια, έκανα αιματολογικές εξετάσεις και συμπλήρωσα ένα ερωτηματολόγιο. Μετά, κάθε μέρα έβγαζα γάλα, το έβαζα στην κατάψυξη, και μια φορά την εβδομάδα ένας οδηγός του νοσοκομείου περνούσε να το πάρει. Σε έξι μήνες έδωσα πάνω από ογδόντα λίτρα. Δεν θα γνωρίσω ποτέ αυτά τα μωρά, αλλά σκέφτομαι συχνά ότι κάπου μεγαλώνουν.", "Before becoming a donor, I had blood tests and filled in a questionnaire. Then every day I expressed milk, put it in the freezer, and once a week a hospital driver came by to collect it. In six months I gave over eighty litres. I'll never meet those babies, but I often think that somewhere they are growing up."),
 ],
 "questions": [
  Q("Ποιος της μίλησε για την τράπεζα μητρικού γάλακτος;", ["Η μητέρα της", "Μια μαία στο μαιευτήριο", "Μια φίλη της", "Ο παιδίατρος"], 1, "Μια μαία στο μαιευτήριο μού μίλησε για την τράπεζα μητρικού γάλακτος"),
  Q("Ποια μωρά χρειάζονται κυρίως αυτό το γάλα;", ["Τα πρόωρα μωρά", "Τα μωρά με αλλεργίες", "Όλα τα νεογέννητα", "Τα δίδυμα"], 0, "Το γάλα αυτό το χρειάζονται κυρίως πρόωρα μωρά"),
  Q("Πώς έφτανε το γάλα στο νοσοκομείο;", ["Το πήγαινε η ίδια κάθε μέρα", "Ένας οδηγός του νοσοκομείου περνούσε μια φορά την εβδομάδα", "Το έστελνε με το ταχυδρομείο", "Το έπαιρνε ο άντρας της"], 1, "μια φορά την εβδομάδα ένας οδηγός του νοσοκομείου περνούσε να το πάρει"),
 ],
 "gloss": {"δότρια": "δότρια — donor (female)", "μητρικού γάλακτος": "μητρικό γάλα — breast milk", "μητρότητα": "μητρότητα — motherhood", "μαία": "μαία — midwife", "μαιευτήριο": "μαιευτήριο — maternity hospital", "πρόωρα": "πρόωρος — premature", "τοκετό": "τοκετός — childbirth", "αιματολογικές εξετάσεις": "αιματολογικές εξετάσεις — blood tests", "ερωτηματολόγιο": "ερωτηματολόγιο — questionnaire", "κατάψυξη": "κατάψυξη — freezer"},
})

ITEMS.append({
 "id": "l72-c1-pseudeis-anamniseis", "title": "Θυμόμαστε πράγματα που δεν έγιναν ποτέ;", "title_en": "Do we remember things that never happened?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν γνωστικό ψυχολόγο σε εκπομπή του ραδιοφώνου για την επιστήμη.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Λαμπρόπουλε, οι περισσότεροι πιστεύουμε ότι η μνήμη λειτουργεί σαν βιντεοκάμερα. Έχουμε άδικο;", "Mr Lampropoulos, most of us believe that memory works like a video camera. Are we wrong?"),
  L("Ψυχολόγος", "m", "Απολύτως. Η μνήμη δεν αποθηκεύει μια πιστή εγγραφή. Κάθε φορά που ανακαλούμε ένα γεγονός, ουσιαστικά το ανασυνθέτουμε, και στην ανασύνθεση αυτή παρεισφρέουν στοιχεία που ακούσαμε αργότερα, που φανταστήκαμε ή που μας υπέβαλαν άλλοι. Η ανάμνηση αλλάζει λίγο κάθε φορά που τη θυμόμαστε.", "Absolutely. Memory doesn't store a faithful recording. Every time we recall an event we essentially reconstruct it, and into that reconstruction creep elements that we heard later, that we imagined or that others suggested to us. The memory changes a little every time we remember it."),
  L("Δημοσιογράφος", "f", "Μπορεί κανείς να «θυμάται» κάτι που δεν συνέβη ποτέ;", "Can someone 'remember' something that never happened?"),
  L("Ψυχολόγος", "m", "Ναι, και αυτό έχει αποδειχθεί πειραματικά. Σε γνωστές μελέτες, οι ερευνητές περιέγραφαν στους συμμετέχοντες μερικά πραγματικά περιστατικά από την παιδική τους ηλικία, μαζί με ένα επινοημένο, για παράδειγμα ότι χάθηκαν σε ένα εμπορικό κέντρο. Ένα σημαντικό ποσοστό όχι μόνο αποδεχόταν το ψεύτικο περιστατικό, αλλά πρόσθετε και λεπτομέρειες: τι φορούσε, ποιος το βρήκε.", "Yes, and it has been shown experimentally. In well-known studies, researchers described to participants a few real incidents from their childhood together with an invented one, for example that they got lost in a shopping centre. A significant proportion not only accepted the false incident but also added details: what they were wearing, who found them."),
  L("Δημοσιογράφος", "f", "Αυτό έχει πρακτικές συνέπειες;", "Does this have practical consequences?"),
  L("Ψυχολόγος", "m", "Τεράστιες, κυρίως στη δικαιοσύνη. Πολλές δικαστικές πλάνες βασίστηκαν σε καταθέσεις αυτοπτών μαρτύρων, οι οποίοι ήταν απολύτως ειλικρινείς και απολύτως λανθασμένοι. Γι' αυτό σήμερα οι ειδικοί επιμένουν ότι οι ανακρίσεις πρέπει να γίνονται χωρίς καθοδηγητικές ερωτήσεις. Το δίδαγμα δεν είναι ότι η μνήμη είναι άχρηστη, αλλά ότι η βεβαιότητα δεν αποτελεί απόδειξη ακρίβειας.", "Enormous, mainly in the justice system. Many miscarriages of justice were based on the testimony of eyewitnesses who were completely sincere and completely wrong. That's why experts today insist that interrogations must be conducted without leading questions. The lesson is not that memory is useless, but that certainty is not proof of accuracy."),
 ],
 "questions": [
  Q("Πώς λειτουργεί η μνήμη, κατά τον ψυχολόγο;", ["Σαν βιντεοκάμερα", "Ανασυνθέτει το γεγονός κάθε φορά που το ανακαλούμε", "Αποθηκεύει μόνο εικόνες", "Δεν αλλάζει ποτέ"], 1, "Κάθε φορά που ανακαλούμε ένα γεγονός, ουσιαστικά το ανασυνθέτουμε"),
  Q("Τι έκαναν οι ερευνητές στις μελέτες που αναφέρει;", ["Έδειχναν στους συμμετέχοντες ταινίες", "Περιέγραφαν πραγματικά περιστατικά μαζί με ένα επινοημένο", "Ρωτούσαν τους γονείς τους", "Τους υπνώτιζαν"], 1, "μερικά πραγματικά περιστατικά από την παιδική τους ηλικία, μαζί με ένα επινοημένο"),
  Q("Τι έκαναν πολλοί συμμετέχοντες;", ["Αρνούνταν το ψεύτικο περιστατικό", "Αποδέχονταν το ψεύτικο περιστατικό και πρόσθεταν λεπτομέρειες", "Θυμούνταν μόνο το ψεύτικο", "Δεν θυμούνταν τίποτα"], 1, "όχι μόνο αποδεχόταν το ψεύτικο περιστατικό, αλλά πρόσθετε και λεπτομέρειες"),
  Q("Ποιο είναι το δίδαγμα, κατά τον ψυχολόγο;", ["Ότι η μνήμη είναι άχρηστη", "Ότι η βεβαιότητα δεν αποτελεί απόδειξη ακρίβειας", "Ότι οι μάρτυρες λένε ψέματα", "Ότι πρέπει να καταργηθούν οι καταθέσεις"], 1, "η βεβαιότητα δεν αποτελεί απόδειξη ακρίβειας"),
 ],
 "gloss": {"γνωστικό": "γνωστικός — cognitive", "πιστή": "πιστός — faithful", "ανακαλούμε": "ανακαλώ — to recall", "ανασυνθέτουμε": "ανασυνθέτω — to reconstruct", "παρεισφρέουν": "παρεισφρέω — to creep in, intrude", "υπέβαλαν": "υποβάλλω — to suggest (an idea)", "επινοημένο": "επινοημένος — invented", "δικαστικές πλάνες": "δικαστική πλάνη — miscarriage of justice", "καταθέσεις": "κατάθεση — testimony", "αυτοπτών μαρτύρων": "αυτόπτης μάρτυρας — eyewitness", "καθοδηγητικές": "καθοδηγητικός — leading (question)", "δίδαγμα": "δίδαγμα — lesson"},
})

ITEMS.append({
 "id": "l72-c1-limos-katochis", "title": "Ο μεγάλος λιμός της Κατοχής", "title_en": "The great famine of the Occupation", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε απόσπασμα από μια διάλεξη ιστορίας για την Ελλάδα της Κατοχής, στη διάρκεια του Δεύτερου Παγκοσμίου Πολέμου.",
 "script": [
  L("Ιστορικός", "f", "Ο χειμώνας του 1941–1942 έμεινε στη συλλογική μνήμη ως «ο χειμώνας της πείνας». Λίγους μήνες μετά την είσοδο των γερμανικών στρατευμάτων στην Αθήνα, η πρωτεύουσα και ο Πειραιάς βυθίστηκαν σε έναν λιμό χωρίς προηγούμενο στη νεότερη ευρωπαϊκή ιστορία εκτός πολέμου στο μέτωπο.", "The winter of 1941–1942 has remained in collective memory as 'the winter of hunger'. A few months after German troops entered Athens, the capital and Piraeus sank into a famine without precedent in modern European history away from the front line."),
  L("Ιστορικός", "f", "Τα αίτια ήταν πολλά και αλληλένδετα. Οι δυνάμεις κατοχής επίταξαν τρόφιμα και μεταφορικά μέσα· η χώρα ήταν χωρισμένη σε ζώνες, και το σιτάρι της Μακεδονίας δεν έφτανε στο νότο· ο βρετανικός ναυτικός αποκλεισμός σταμάτησε τις εισαγωγές, από τις οποίες η Ελλάδα εξαρτιόταν για ένα μεγάλο μέρος του ψωμιού της. Η μαύρη αγορά έκανε τα υπόλοιπα.", "The causes were many and interconnected. The occupying forces requisitioned food and means of transport; the country was divided into zones, and the wheat of Macedonia did not reach the south; the British naval blockade stopped the imports on which Greece depended for a large part of its bread. The black market did the rest."),
  L("Ιστορικός", "f", "Οι αριθμοί παραμένουν αντικείμενο συζήτησης, αλλά εκτιμάται ότι μόνο στην περιοχή Αθήνας και Πειραιά πέθαναν δεκάδες χιλιάδες άνθρωποι εκείνον τον χειμώνα. Οι φωτογραφίες με τα κάρα του δήμου που μάζευαν τους νεκρούς από τα πεζοδρόμια συγκλόνισαν την παγκόσμια κοινή γνώμη.", "The figures remain a matter of debate, but it is estimated that in the Athens and Piraeus area alone tens of thousands of people died that winter. The photographs of municipal carts collecting the dead from the pavements shocked world public opinion."),
  L("Ιστορικός", "f", "Η πίεση αυτή οδήγησε, το 1942, σε μια σπάνια εξαίρεση: ο αποκλεισμός χαλάρωσε, ώστε να φτάνει σιτάρι με πλοία υπό την εποπτεία του Ερυθρού Σταυρού. Ο λιμός δεν ήταν, επομένως, φυσική καταστροφή· ήταν αποτέλεσμα πολιτικών αποφάσεων. Και αυτό ακριβώς είναι το πιο ανησυχητικό του δίδαγμα.", "This pressure led, in 1942, to a rare exception: the blockade was relaxed so that wheat could arrive on ships under the supervision of the Red Cross. The famine was not, therefore, a natural disaster; it was the result of political decisions. And that is precisely its most disturbing lesson."),
 ],
 "questions": [
  Q("Πώς έμεινε στη μνήμη ο χειμώνας του 1941–1942;", ["Ως ο πιο κρύος χειμώνας του αιώνα", "Ως «ο χειμώνας της πείνας»", "Ως ο χειμώνας της απελευθέρωσης", "Ως ο χειμώνας των σεισμών"], 1, "«ο χειμώνας της πείνας»"),
  Q("Γιατί δεν έφτανε το σιτάρι της Μακεδονίας στο νότο;", ["Γιατί η σοδειά καταστράφηκε", "Γιατί η χώρα ήταν χωρισμένη σε ζώνες", "Γιατί το πουλούσαν στο εξωτερικό", "Γιατί δεν υπήρχαν λιμάνια"], 1, "η χώρα ήταν χωρισμένη σε ζώνες"),
  Q("Τι συνέβη το 1942;", ["Τελείωσε ο πόλεμος", "Ο αποκλεισμός χαλάρωσε για πλοία με σιτάρι υπό την εποπτεία του Ερυθρού Σταυρού", "Οι Γερμανοί έφυγαν από την Αθήνα", "Καταργήθηκε η μαύρη αγορά"], 1, "ο αποκλεισμός χαλάρωσε, ώστε να φτάνει σιτάρι με πλοία υπό την εποπτεία του Ερυθρού Σταυρού"),
  Q("Ποιο είναι, κατά την ιστορικό, το πιο ανησυχητικό δίδαγμα του λιμού;", ["Ότι ήταν φυσική καταστροφή", "Ότι ήταν αποτέλεσμα πολιτικών αποφάσεων", "Ότι δεν θα επαναληφθεί ποτέ", "Ότι οι αριθμοί είναι υπερβολικοί"], 1, "ήταν αποτέλεσμα πολιτικών αποφάσεων"),
 ],
 "gloss": {"λιμός": "λιμός — famine", "Κατοχής": "Κατοχή — the (Axis) Occupation of Greece, 1941–44", "στρατευμάτων": "στράτευμα — troops", "αλληλένδετα": "αλληλένδετος — interconnected", "επίταξαν": "επιτάσσω — to requisition", "αποκλεισμός": "αποκλεισμός — blockade", "εισαγωγές": "εισαγωγή — import", "μαύρη αγορά": "μαύρη αγορά — black market", "κάρα": "κάρο — cart", "συγκλόνισαν": "συγκλονίζω — to shock deeply", "εποπτεία": "εποπτεία — supervision"},
})

rnd = random.Random(72)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-72.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
