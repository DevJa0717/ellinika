# Source for library/listening/listening-136.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l136.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l136-ann-nychta-mouseion", "title": "Η Νύχτα των Μουσείων", "title_en": "Museum Night", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε στο ραδιόφωνο μια ανακοίνωση του δήμου για μια πολιτιστική εκδήλωση.",
 "script": [
  L("Εκφωνήτρια", "f", "Το Σάββατο η πόλη γιορτάζει τη Νύχτα των Μουσείων. Από τις επτά το απόγευμα έως τα μεσάνυχτα, έντεκα μουσεία και πινακοθήκες θα είναι ανοιχτά, με ελεύθερη είσοδο για όλους.", "On Saturday the city celebrates Museum Night. From seven in the evening until midnight, eleven museums and galleries will be open, with free admission for everyone."),
  L("Εκφωνήτρια", "f", "Σε κάθε μουσείο θα γίνονται ξεναγήσεις κάθε μισή ώρα, ενώ στην αυλή του Λαογραφικού Μουσείου θα δώσει συναυλία η δημοτική χορωδία. Για τα παιδιά υπάρχει ένα παιχνίδι θησαυρού: όσα συγκεντρώσουν σφραγίδες από πέντε μουσεία θα πάρουν ένα δώρο.", "Every museum will offer guided tours every half hour, while the municipal choir will give a concert in the courtyard of the Folklore Museum. For children there is a treasure hunt: those who collect stamps from five museums will get a present."),
  L("Εκφωνήτρια", "f", "Δωρεάν λεωφορεία θα συνδέουν τα μουσεία ανά δεκαπέντε λεπτά. Επειδή αναμένεται μεγάλη προσέλευση, ο δήμος συνιστά στους επισκέπτες να αφήσουν τα αυτοκίνητά τους στο σπίτι.", "Free buses will link the museums every fifteen minutes. Because a large turnout is expected, the municipality advises visitors to leave their cars at home."),
 ],
 "questions": [
  Q("Πόσο κοστίζει η είσοδος στα μουσεία εκείνη τη νύχτα;", ["Πέντε ευρώ", "Είναι δωρεάν", "Μισή τιμή", "Δωρεάν μόνο για παιδιά"], 1, "με ελεύθερη είσοδο για όλους"),
  Q("Τι θα πάρουν τα παιδιά που θα συγκεντρώσουν πέντε σφραγίδες;", ["Ένα δώρο", "Ένα εισιτήριο για συναυλία", "Μια ξενάγηση", "Ένα βιβλίο για το μουσείο"], 0, "όσα συγκεντρώσουν σφραγίδες από πέντε μουσεία θα πάρουν ένα δώρο"),
  Q("Τι συνιστά ο δήμος στους επισκέπτες;", ["Να κλείσουν θέση από πριν", "Να έρθουν νωρίς", "Να αφήσουν τα αυτοκίνητά τους στο σπίτι", "Να φέρουν την ταυτότητά τους"], 2, "συνιστά στους επισκέπτες να αφήσουν τα αυτοκίνητά τους στο σπίτι"),
 ],
 "gloss": {"πινακοθήκες": "πινακοθήκη — art gallery", "ελεύθερη είσοδο": "ελεύθερη είσοδος — free admission", "ξεναγήσεις": "ξενάγηση — guided tour", "Λαογραφικού": "λαογραφικός — folklore (adj.)", "χορωδία": "χορωδία — choir", "παιχνίδι θησαυρού": "παιχνίδι θησαυρού — treasure hunt", "σφραγίδες": "σφραγίδα — stamp", "αναμένεται": "αναμένομαι — to be expected", "προσέλευση": "προσέλευση — turnout, attendance", "συνιστά": "συνιστώ — to advise, recommend"}
})

ITEMS.append({
 "id": "l136-int-keroplastis", "title": "Ο τελευταίος κεροπλάστης της πόλης", "title_en": "The town's last candle maker", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική εκπομπή για παλιά επαγγέλματα.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς φτιάχνεται ένα κερί με τον παραδοσιακό τρόπο;", "How is a candle made the traditional way?"),
  L("Κεροπλάστης", "m", "Λιώνουμε το κερί της μέλισσας σε ένα μεγάλο καζάνι και βουτάμε το φιτίλι ξανά και ξανά, ώσπου να αποκτήσει το πάχος που θέλουμε. Για μια μεγάλη λαμπάδα χρειάζονται πάνω από σαράντα βουτιές. Το αληθινό μελισσοκέρι μυρίζει μέλι και καίει αργά, χωρίς καπνό.", "We melt beeswax in a big cauldron and dip the wick again and again until it reaches the thickness we want. A large Easter candle needs more than forty dips. Real beeswax smells of honey and burns slowly, without smoke."),
  L("Δημοσιογράφος", "m", "Ποια είναι η πιο δύσκολη εποχή;", "Which is the busiest time of year?"),
  L("Κεροπλάστης", "m", "Το Πάσχα, χωρίς αμφιβολία. Από τον Φεβρουάριο δουλεύουμε όλη η οικογένεια, γιατί οι νονοί παραγγέλνουν στολισμένες λαμπάδες για τα βαφτιστήρια τους. Τον υπόλοιπο χρόνο φτιάχνουμε κεριά για τις εκκλησίες. Δυστυχώς, τα φτηνά κεριά από παραφίνη μάς έχουν πάρει πολλούς πελάτες, αλλά τελευταία έρχονται νέοι που ψάχνουν κάτι φυσικό.", "Easter, without a doubt. From February the whole family works, because godparents order decorated Easter candles for their godchildren. The rest of the year we make candles for the churches. Unfortunately, cheap paraffin candles have taken many of our customers, but lately young people come looking for something natural."),
 ],
 "questions": [
  Q("Πώς αποκτά το κερί το πάχος που θέλουν;", ["Το χύνουν σε καλούπι", "Βουτούν το φιτίλι ξανά και ξανά στο λιωμένο κερί", "Το κόβουν με μαχαίρι", "Το ζεσταίνουν στον ήλιο"], 1, "βουτάμε το φιτίλι ξανά και ξανά, ώσπου να αποκτήσει το πάχος που θέλουμε"),
  Q("Τι ισχύει για το αληθινό μελισσοκέρι;", ["Μυρίζει μέλι και καίει αργά, χωρίς καπνό", "Είναι φτηνότερο από την παραφίνη", "Καίει πολύ γρήγορα", "Δεν έχει μυρωδιά"], 0, "Το αληθινό μελισσοκέρι μυρίζει μέλι και καίει αργά, χωρίς καπνό"),
  Q("Γιατί το Πάσχα είναι η πιο δύσκολη εποχή;", ["Γιατί κλείνουν οι εκκλησίες", "Γιατί δεν βρίσκουν κερί", "Γιατί οι νονοί παραγγέλνουν στολισμένες λαμπάδες για τα βαφτιστήρια τους", "Γιατί φεύγουν για διακοπές"], 2, "οι νονοί παραγγέλνουν στολισμένες λαμπάδες για τα βαφτιστήρια τους"),
 ],
 "gloss": {"Λιώνουμε": "λιώνω — to melt", "καζάνι": "καζάνι — cauldron", "βουτάμε": "βουτάω — to dip", "φιτίλι": "φιτίλι — wick", "πάχος": "πάχος — thickness", "λαμπάδα": "λαμπάδα — (Easter) candle", "μελισσοκέρι": "μελισσοκέρι — beeswax", "νονοί": "νονός — godparent", "στολισμένες": "στολισμένος — decorated", "βαφτιστήρια": "βαφτιστήρι — godchild", "παραφίνη": "παραφίνη — paraffin"}
})

ITEMS.append({
 "id": "l136-dia-resital", "title": "Το πρώτο ρεσιτάλ στα σαράντα", "title_en": "A first recital at forty", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλους να συζητούν σε ένα καφέ.",
 "script": [
  L("Νίκος", "m", "Την Κυριακή έχω το πρώτο μου ρεσιτάλ στο ωδείο. Μετά από τρία χρόνια μαθήματα πιάνο, θα παίξω μπροστά σε κόσμο. Και τρέμω. Τα άλλα παιδιά είναι δέκα χρονών, κι εγώ σαράντα δύο.", "On Sunday I have my first recital at the conservatory. After three years of piano lessons, I'll play in front of people. And I'm shaking. The other kids are ten, and I'm forty-two."),
  L("Μαρίνα", "f", "Αυτό είναι υπέροχο! Κανείς δεν θα κοιτάζει την ηλικία σου. Θα δουν κάποιον που τόλμησε να μάθει κάτι καινούργιο. Τι θα παίξεις;", "That's wonderful! No one will be looking at your age. They'll see someone who dared to learn something new. What will you play?"),
  L("Νίκος", "m", "Ένα μικρό κομμάτι του Σοπέν. Στο σπίτι το παίζω χωρίς λάθη, αλλά μπροστά στη δασκάλα μου τα χέρια μου ιδρώνουν και ξεχνάω τις νότες.", "A short piece by Chopin. At home I play it without mistakes, but in front of my teacher my hands sweat and I forget the notes."),
  L("Μαρίνα", "f", "Κάνε κάτι που έκανα εγώ πριν από μια ομιλία: παίξ' το μπροστά σε λίγους φίλους πριν από την Κυριακή, για να συνηθίσεις να σε κοιτάζουν. Αν θες, ελάτε σπίτι μου το Σάββατο, έχω και το παλιό πιάνο της μητέρας μου.", "Do something I did before a speech: play it in front of a few friends before Sunday, so you get used to being watched. If you like, come over to mine on Saturday, I've got my mother's old piano too."),
 ],
 "questions": [
  Q("Γιατί αγχώνεται ο Νίκος;", ["Γιατί δεν έχει μελετήσει", "Γιατί θα παίξει μπροστά σε κόσμο για πρώτη φορά", "Γιατί η δασκάλα του είναι αυστηρή", "Γιατί το πιάνο είναι χαλασμένο"], 1, "θα παίξω μπροστά σε κόσμο. Και τρέμω"),
  Q("Τι του συμβαίνει μπροστά στη δασκάλα του;", ["Παίζει καλύτερα", "Γελάει", "Ιδρώνουν τα χέρια του και ξεχνάει τις νότες", "Παίζει πολύ γρήγορα"], 2, "τα χέρια μου ιδρώνουν και ξεχνάω τις νότες"),
  Q("Τι του προτείνει η Μαρίνα;", ["Να παίξει το κομμάτι μπροστά σε λίγους φίλους πριν από την Κυριακή", "Να ακυρώσει το ρεσιτάλ", "Να διαλέξει ένα πιο εύκολο κομμάτι", "Να πάρει ένα ηρεμιστικό"], 0, "παίξ' το μπροστά σε λίγους φίλους πριν από την Κυριακή"),
 ],
 "gloss": {"ρεσιτάλ": "ρεσιτάλ — recital", "ωδείο": "ωδείο — conservatory, music school", "τρέμω": "τρέμω — to tremble", "τόλμησε": "τολμώ — to dare", "κομμάτι": "κομμάτι — piece (of music)", "ιδρώνουν": "ιδρώνω — to sweat", "νότες": "νότα — note (music)", "ομιλία": "ομιλία — speech, talk", "συνηθίσεις": "συνηθίζω — to get used to"}
})

ITEMS.append({
 "id": "l136-vm-enoikiasi", "title": "Μια γρατζουνιά στο νοικιασμένο αυτοκίνητο", "title_en": "A scratch on the rental car", "type": "voicemail", "level": "B2",
 "context_el": "Επιστρέψατε χθες ένα αυτοκίνητο που είχατε νοικιάσει στις διακοπές. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα σας, σας καλώ από το γραφείο ενοικίασης αυτοκινήτων στο αεροδρόμιο. Κατά τον έλεγχο του αυτοκινήτου που επιστρέψατε χθες, ο συνάδελφός μου βρήκε μια γρατζουνιά στην πίσω δεξιά πόρτα, η οποία δεν αναφέρεται στο έντυπο παραλαβής.", "Good morning, I'm calling from the car rental office at the airport. During the inspection of the car you returned yesterday, my colleague found a scratch on the rear right door that isn't mentioned on the pick-up form."),
  L("Υπάλληλος", "m", "Αν έχετε φωτογραφίες από τη μέρα που παραλάβατε το αυτοκίνητο, θα σας παρακαλούσα να μας τις στείλετε με ηλεκτρονικό ταχυδρομείο, για να δούμε αν η γρατζουνιά υπήρχε ήδη.", "If you have photos from the day you picked up the car, I'd ask you to send them to us by email, so we can see whether the scratch was already there."),
  L("Υπάλληλος", "m", "Σε κάθε περίπτωση, επειδή είχατε πάρει πλήρη ασφάλεια, δεν θα χρειαστεί να πληρώσετε τίποτα για την επισκευή. Απλώς πρέπει να κλείσουμε τον φάκελο. Ευχαριστώ, και καλή συνέχεια.", "In any case, because you took out full insurance, you won't have to pay anything for the repair. We just need to close the file. Thank you, and all the best."),
 ],
 "questions": [
  Q("Τι βρήκε ο υπάλληλος στο αυτοκίνητο;", ["Ένα σπασμένο φανάρι", "Μια γρατζουνιά στην πίσω δεξιά πόρτα", "Ένα σκισμένο κάθισμα", "Ένα ξεφούσκωτο λάστιχο"], 1, "βρήκε μια γρατζουνιά στην πίσω δεξιά πόρτα"),
  Q("Τι σας ζητά να στείλετε;", ["Φωτογραφίες από τη μέρα της παραλαβής", "Το δίπλωμα οδήγησης", "Την απόδειξη πληρωμής", "Τα κλειδιά του αυτοκινήτου"], 0, "Αν έχετε φωτογραφίες από τη μέρα που παραλάβατε το αυτοκίνητο"),
  Q("Θα χρειαστεί να πληρώσετε για την επισκευή;", ["Ναι, το μισό κόστος", "Ναι, όλο το κόστος", "Όχι, γιατί είχατε πάρει πλήρη ασφάλεια", "Μόνο αν δεν στείλετε φωτογραφίες"], 2, "επειδή είχατε πάρει πλήρη ασφάλεια, δεν θα χρειαστεί να πληρώσετε τίποτα"),
 ],
 "gloss": {"ενοικίασης": "ενοικίαση — rental", "γρατζουνιά": "γρατζουνιά — scratch", "έντυπο παραλαβής": "έντυπο παραλαβής — pick-up form", "παραλάβατε": "παραλαμβάνω — to collect, take delivery of", "ηλεκτρονικό ταχυδρομείο": "ηλεκτρονικό ταχυδρομείο — email", "πλήρη ασφάλεια": "πλήρης ασφάλεια — full insurance", "επισκευή": "επισκευή — repair", "φάκελο": "φάκελος — file"}
})

ITEMS.append({
 "id": "l136-ann-aerodromio", "title": "Στάση εργασίας στο αεροδρόμιο", "title_en": "Work stoppage at the airport", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε στο αεροδρόμιο και ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνητής", "m", "Παρακαλούνται οι επιβάτες να προσέξουν: λόγω στάσης εργασίας των ελεγκτών εναέριας κυκλοφορίας από τις δώδεκα έως τις τέσσερις το απόγευμα, όλες οι πτήσεις αυτού του διαστήματος θα αναχωρήσουν με καθυστέρηση.", "Passengers are kindly asked to note: due to a work stoppage by air traffic controllers from twelve to four in the afternoon, all flights in this period will depart late."),
  L("Εκφωνητής", "m", "Οι πτήσεις προς Ρόδο και Ηράκλειο έχουν ακυρωθεί. Οι επιβάτες των πτήσεων αυτών μπορούν να απευθυνθούν στα γκισέ της εταιρείας τους, για να κλείσουν θέση στην επόμενη διαθέσιμη πτήση χωρίς επιπλέον χρέωση.", "The flights to Rhodes and Heraklion have been cancelled. Passengers on these flights can go to their airline's desks to book a seat on the next available flight at no extra charge."),
  L("Εκφωνητής", "m", "Οι αεροπορικές εταιρείες θα διανέμουν κουπόνια για φαγητό και νερό στους επιβάτες που περιμένουν περισσότερο από τρεις ώρες. Παρακαλούμε να παρακολουθείτε τις οθόνες για τις νέες ώρες αναχώρησης. Ευχαριστούμε για την κατανόησή σας.", "The airlines will hand out vouchers for food and water to passengers waiting more than three hours. Please follow the screens for the new departure times. Thank you for your understanding."),
 ],
 "questions": [
  Q("Γιατί θα καθυστερήσουν οι πτήσεις;", ["Λόγω κακοκαιρίας", "Λόγω στάσης εργασίας των ελεγκτών εναέριας κυκλοφορίας", "Λόγω βλάβης στον διάδρομο", "Λόγω απεργίας των πιλότων"], 1, "λόγω στάσης εργασίας των ελεγκτών εναέριας κυκλοφορίας"),
  Q("Τι μπορούν να κάνουν οι επιβάτες των ακυρωμένων πτήσεων;", ["Να πάρουν πίσω μόνο τα μισά χρήματα", "Να περιμένουν μέχρι αύριο", "Να ταξιδέψουν με πλοίο", "Να κλείσουν θέση στην επόμενη διαθέσιμη πτήση χωρίς επιπλέον χρέωση"], 3, "για να κλείσουν θέση στην επόμενη διαθέσιμη πτήση χωρίς επιπλέον χρέωση"),
  Q("Ποιοι θα πάρουν κουπόνια για φαγητό και νερό;", ["Οι επιβάτες που περιμένουν περισσότερο από τρεις ώρες", "Όλοι οι επιβάτες", "Μόνο οι οικογένειες με παιδιά", "Οι επιβάτες για Ρόδο"], 0, "στους επιβάτες που περιμένουν περισσότερο από τρεις ώρες"),
 ],
 "gloss": {"μεγάφωνα": "μεγάφωνο — loudspeaker", "στάσης εργασίας": "στάση εργασίας — work stoppage", "ελεγκτών εναέριας κυκλοφορίας": "ελεγκτής εναέριας κυκλοφορίας — air traffic controller", "διαστήματος": "διάστημα — period of time", "ακυρωθεί": "ακυρώνομαι — to be cancelled", "απευθυνθούν": "απευθύνομαι — to apply to, contact", "γκισέ": "γκισέ — desk, counter", "χρέωση": "χρέωση — charge", "διανέμουν": "διανέμω — to hand out", "κουπόνια": "κουπόνι — voucher"}
})

ITEMS.append({
 "id": "l136-int-pagopoieio", "title": "Το τελευταίο παγοποιείο", "title_en": "The last ice factory", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από ρεπορτάζ σε μια παραθαλάσσια πόλη.",
 "script": [
  L("Δημοσιογράφος", "f", "Ποιος αγοράζει ακόμη πάγο σε κολόνες;", "Who still buys ice in blocks?"),
  L("Ιδιοκτήτης", "m", "Περισσότεροι απ' όσους νομίζετε. Τα ψαροκάικα, πριν βγουν τη νύχτα, φορτώνουν πάγο για να κρατήσουν φρέσκα τα ψάρια. Οι ψαροταβέρνες τον θέλουν για τη βιτρίνα τους. Και τα καλοκαίρια, σε γάμους και πανηγύρια, τα ποτά κρυώνουν σε βαρέλια με πάγο.", "More than you think. The fishing boats load ice before they go out at night, to keep the fish fresh. The fish tavernas want it for their display counters. And in summer, at weddings and village festivals, drinks are chilled in barrels of ice."),
  L("Δημοσιογράφος", "f", "Πώς ξεκίνησε το παγοποιείο;", "How did the ice factory start?"),
  L("Ιδιοκτήτης", "m", "Το έστησε ο παππούς μου το 1952, όταν τα σπίτια δεν είχαν ψυγεία. Τότε ο πάγος πήγαινε πόρτα πόρτα με ένα κάρο. Όταν ήρθαν τα ψυγεία, έκλεισαν σχεδόν όλα τα παγοποιεία της περιοχής. Εμείς αντέξαμε, γιατί αλλάξαμε πελάτες. Τώρα ο γιος μου θέλει να φτιάχνει και διάφανο πάγο για τα κοκτέιλ των μπαρ.", "My grandfather set it up in 1952, when homes had no fridges. Back then ice went door to door on a cart. When fridges came, almost all the ice factories in the area closed. We survived because we changed customers. Now my son wants to make clear ice for bar cocktails too."),
 ],
 "questions": [
  Q("Γιατί αγοράζουν πάγο τα ψαροκάικα;", ["Για να κρατήσουν φρέσκα τα ψάρια", "Για να κρυώσουν τα ποτά των ψαράδων", "Για να πουλήσουν πάγο στα νησιά", "Για να καθαρίσουν τα αμπάρια"], 0, "φορτώνουν πάγο για να κρατήσουν φρέσκα τα ψάρια"),
  Q("Πώς έφτανε ο πάγος στα σπίτια παλιότερα;", ["Με φορτηγό ψυγείο", "Τον έπαιρναν οι ίδιοι από το λιμάνι", "Πόρτα πόρτα με ένα κάρο", "Με το τρένο"], 2, "ο πάγος πήγαινε πόρτα πόρτα με ένα κάρο"),
  Q("Γιατί το παγοποιείο άντεξε, όταν έκλεισαν τα άλλα;", ["Γιατί πήρε επιδότηση", "Γιατί άλλαξε πελάτες", "Γιατί μείωσε τις τιμές", "Γιατί άνοιξε και ψαροταβέρνα"], 1, "Εμείς αντέξαμε, γιατί αλλάξαμε πελάτες"),
 ],
 "gloss": {"παγοποιείο": "παγοποιείο — ice factory", "παραθαλάσσια": "παραθαλάσσιος — seaside (adj.)", "κολόνες": "κολόνα — block (of ice), column", "ψαροκάικα": "ψαροκάικο — fishing boat", "φορτώνουν": "φορτώνω — to load", "ψαροταβέρνες": "ψαροταβέρνα — fish taverna", "βιτρίνα": "βιτρίνα — display counter", "πανηγύρια": "πανηγύρι — village festival", "βαρέλια": "βαρέλι — barrel", "κάρο": "κάρο — cart", "διάφανο": "διάφανος — clear, transparent"}
})

ITEMS.append({
 "id": "l136-vm-vivliopoleio", "title": "Ήρθε το βιβλίο σας, αλλά…", "title_en": "Your book has arrived, but…", "type": "voicemail", "level": "B2",
 "context_el": "Είχατε παραγγείλει ένα βιβλίο σε ένα βιβλιοπωλείο της γειτονιάς σας. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Βιβλιοπώλης", "m", "Καλησπέρα, από το βιβλιοπωλείο «Ο Ναυτίλος». Το βιβλίο που παραγγείλατε έφτασε σήμερα, αλλά υπάρχει ένα μικρό θέμα. Ο εκδότης μάς έστειλε τη νέα έκδοση, με εξώφυλλο από χαρτόνι, και όχι τη δερματόδετη που είχατε ζητήσει, γιατί εκείνη έχει εξαντληθεί.", "Good evening, from the Nautilus bookshop. The book you ordered arrived today, but there's a small issue. The publisher sent us the new edition, with a paperback cover, and not the leather-bound one you asked for, because that one is out of print."),
  L("Βιβλιοπώλης", "m", "Το περιεχόμενο είναι ακριβώς το ίδιο, και μάλιστα η νέα έκδοση έχει και έναν πρόλογο του μεταφραστή. Είναι επίσης έξι ευρώ φθηνότερη, οπότε, αν την κρατήσετε, θα σας επιστρέψουμε τη διαφορά.", "The content is exactly the same, and in fact the new edition also has a translator's preface. It's also six euros cheaper, so if you keep it, we'll refund you the difference."),
  L("Βιβλιοπώλης", "m", "Αν πάλι προτιμάτε τη δερματόδετη, μπορώ να ψάξω σε παλαιοβιβλιοπωλεία, αλλά μπορεί να αργήσει. Πείτε μου τι θέλετε να κάνουμε. Καλό βράδυ.", "If, on the other hand, you prefer the leather-bound one, I can look in second-hand bookshops, but it may take a while. Let me know what you'd like us to do. Good evening."),
 ],
 "questions": [
  Q("Ποιο είναι το «μικρό θέμα»;", ["Το βιβλίο έφτασε σκισμένο", "Ήρθε η νέα έκδοση και όχι η δερματόδετη", "Ήρθε λάθος βιβλίο", "Το βιβλίο θα αργήσει ένα μήνα"], 1, "Ο εκδότης μάς έστειλε τη νέα έκδοση, με εξώφυλλο από χαρτόνι, και όχι τη δερματόδετη"),
  Q("Τι έχει επιπλέον η νέα έκδοση;", ["Φωτογραφίες", "Έναν χάρτη", "Έναν πρόλογο του μεταφραστή", "Ένα CD"], 2, "η νέα έκδοση έχει και έναν πρόλογο του μεταφραστή"),
  Q("Τι θα γίνει αν κρατήσετε τη νέα έκδοση;", ["Θα σας επιστρέψουν τη διαφορά", "Θα πληρώσετε έξι ευρώ παραπάνω", "Θα πάρετε ένα δεύτερο βιβλίο δώρο", "Θα σας τη στείλουν στο σπίτι"], 0, "αν την κρατήσετε, θα σας επιστρέψουμε τη διαφορά"),
 ],
 "gloss": {"παραγγείλει": "παραγγέλνω — to order", "εκδότης": "εκδότης — publisher", "έκδοση": "έκδοση — edition", "εξώφυλλο": "εξώφυλλο — cover", "χαρτόνι": "χαρτόνι — cardboard", "δερματόδετη": "δερματόδετος — leather-bound", "εξαντληθεί": "εξαντλούμαι — to be sold out, out of print", "περιεχόμενο": "περιεχόμενο — content", "πρόλογο": "πρόλογος — preface", "μεταφραστή": "μεταφραστής — translator", "παλαιοβιβλιοπωλεία": "παλαιοβιβλιοπωλείο — second-hand bookshop"}
})

ITEMS.append({
 "id": "l136-news-glaroi", "title": "Πρόστιμο για όσους ταΐζουν τους γλάρους", "title_en": "A fine for feeding the gulls", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στις τοπικές ειδήσεις.",
 "script": [
  L("Ρεπόρτερ", "f", "Ο δήμος αποφάσισε να επιβάλει πρόστιμο πενήντα ευρώ σε όσους ταΐζουν τους γλάρους στην παραλιακή λεωφόρο και στο λιμάνι.", "The municipality has decided to impose a fifty-euro fine on anyone who feeds the gulls on the seafront avenue and in the harbour."),
  L("Ρεπόρτερ", "f", "Τα τελευταία χρόνια οι γλάροι έχουν γίνει πολύ πιο τολμηροί. Κατεβαίνουν στα τραπέζια των καφετεριών και αρπάζουν φαγητό ακόμη και από τα χέρια των παιδιών. Σύμφωνα με τον δήμο, ο κύριος λόγος είναι ότι πολλοί περαστικοί και τουρίστες τους δίνουν ψωμί και υπολείμματα.", "In recent years the gulls have become much bolder. They swoop onto café tables and snatch food even from children's hands. According to the municipality, the main reason is that many passers-by and tourists give them bread and scraps."),
  L("Ρεπόρτερ", "f", "Οι ορνιθολόγοι συμφωνούν με το μέτρο, αλλά τονίζουν ότι χρειάζονται και κάδοι με καπάκι, γιατί οι γλάροι βρίσκουν τροφή και στα ανοιχτά σκουπίδια. Ο δήμος υπόσχεται να τοποθετήσει εκατό νέους κάδους μέχρι το καλοκαίρι.", "Ornithologists agree with the measure but stress that bins with lids are also needed, because gulls also find food in open rubbish. The municipality promises to install a hundred new bins by summer."),
 ],
 "questions": [
  Q("Τι αποφάσισε ο δήμος;", ["Να απαγορεύσει τα ψάρια στο λιμάνι", "Να επιβάλει πρόστιμο σε όσους ταΐζουν τους γλάρους", "Να μετακινήσει τους γλάρους", "Να κλείσει τις καφετέριες νωρίτερα"], 1, "επιβάλει πρόστιμο πενήντα ευρώ σε όσους ταΐζουν τους γλάρους"),
  Q("Ποιος είναι, σύμφωνα με τον δήμο, ο κύριος λόγος που οι γλάροι έγιναν τολμηροί;", ["Η έλλειψη ψαριών στη θάλασσα", "Ο καιρός", "Ότι πολλοί περαστικοί και τουρίστες τους δίνουν ψωμί και υπολείμματα", "Ότι οι καφετέριες έβγαλαν τραπέζια στον δρόμο"], 2, "ο κύριος λόγος είναι ότι πολλοί περαστικοί και τουρίστες τους δίνουν ψωμί και υπολείμματα"),
  Q("Τι λένε οι ορνιθολόγοι ότι χρειάζεται επιπλέον;", ["Κάδοι με καπάκι", "Περισσότεροι αστυνομικοί", "Δίχτυα στο λιμάνι", "Ειδικές ταΐστρες"], 0, "χρειάζονται και κάδοι με καπάκι"),
 ],
 "gloss": {"πρόστιμο": "πρόστιμο — fine", "γλάρους": "γλάρος — gull", "επιβάλει": "επιβάλλω — to impose", "παραλιακή": "παραλιακός — seafront (adj.)", "τολμηροί": "τολμηρός — bold", "αρπάζουν": "αρπάζω — to snatch", "περαστικοί": "περαστικός — passer-by", "υπολείμματα": "υπόλειμμα — leftover, scrap", "ορνιθολόγοι": "ορνιθολόγος — ornithologist", "τονίζουν": "τονίζω — to stress", "κάδοι": "κάδος — bin", "καπάκι": "καπάκι — lid"}
})

ITEMS.append({
 "id": "l136-c1-gresham", "title": "Ο νόμος του Γκρέσαμ", "title_en": "Gresham's law", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη οικονομικής ιστορίας.",
 "script": [
  L("Ομιλητής", "m", "Το 405 π.Χ., στους «Βατράχους» του Αριστοφάνη, ο χορός παραπονιέται ότι η Αθήνα φέρεται στους καλύτερους πολίτες της όπως στα παλιά, καθαρά ασημένια νομίσματά της: τα έχει παραμερίσει και χρησιμοποιεί, αντί γι' αυτά, κακής ποιότητας χάλκινα νομίσματα. Είναι ίσως η αρχαιότερη περιγραφή ενός φαινομένου που αργότερα ονομάστηκε «νόμος του Γκρέσαμ».", "In 405 BC, in Aristophanes' 'Frogs', the chorus complains that Athens treats its best citizens like its old, pure silver coins: it has put them aside and uses poor-quality bronze coins instead. It is perhaps the oldest description of a phenomenon that was later called 'Gresham's law'."),
  L("Ομιλητής", "m", "Ο Τόμας Γκρέσαμ ήταν οικονομικός σύμβουλος της βασίλισσας Ελισάβετ της Α΄ τον 16ο αιώνα. Το όνομά του όμως το έδωσε στον νόμο ένας Σκωτσέζος οικονομολόγος, ο Χένρι Μακλάουντ, το 1858, παρόλο που την ίδια ιδέα είχαν διατυπώσει νωρίτερα και άλλοι, ανάμεσά τους ο Νικόλαος Κοπέρνικος.", "Thomas Gresham was a financial adviser to Queen Elizabeth I in the 16th century. However, his name was given to the law by a Scottish economist, Henry Macleod, in 1858, even though others had formulated the same idea earlier, among them Nicolaus Copernicus."),
  L("Ομιλητής", "m", "Η διατύπωση είναι απλή: το κακό χρήμα διώχνει το καλό. Αν κυκλοφορούν δύο νομίσματα με την ίδια ονομαστική αξία, αλλά το ένα περιέχει περισσότερο πολύτιμο μέταλλο, οι άνθρωποι ξοδεύουν το φτωχότερο και κρατούν, ή λιώνουν, το καλύτερο. Έτσι, σιγά σιγά, στην αγορά μένει μόνο το κακό νόμισμα.", "The formulation is simple: bad money drives out good. If two coins circulate with the same face value, but one contains more precious metal, people spend the poorer one and keep, or melt down, the better one. So, little by little, only the bad coin remains on the market."),
  L("Ομιλητής", "m", "Προσοχή όμως: ο νόμος ισχύει μόνο όταν ο νόμος του κράτους υποχρεώνει τους πολίτες να δέχονται και τα δύο νομίσματα στην ίδια αξία. Σήμερα η φράση χρησιμοποιείται και μεταφορικά, για παράδειγμα όταν λέμε ότι η πρόχειρη πληροφορία διώχνει την προσεκτική.", "But careful: the law only applies when state law obliges citizens to accept both coins at the same value. Today the phrase is also used metaphorically, for example when we say that sloppy information drives out careful information."),
 ],
 "questions": [
  Q("Με τι συγκρίνει ο χορός στους «Βατράχους» τους καλύτερους πολίτες της Αθήνας;", ["Με τα χάλκινα νομίσματα", "Με τα παλιά, καθαρά ασημένια νομίσματα που η πόλη έχει παραμερίσει", "Με τα χρυσά κοσμήματα", "Με τα ξένα νομίσματα"], 1, "η Αθήνα φέρεται στους καλύτερους πολίτες της όπως στα παλιά, καθαρά ασημένια νομίσματά της"),
  Q("Ποιος έδωσε στον νόμο το όνομα του Γκρέσαμ;", ["Η βασίλισσα Ελισάβετ", "Ο Κοπέρνικος", "Ένας Σκωτσέζος οικονομολόγος, ο Χένρι Μακλάουντ", "Ο ίδιος ο Γκρέσαμ"], 2, "ένας Σκωτσέζος οικονομολόγος, ο Χένρι Μακλάουντ, το 1858"),
  Q("Τι κάνουν οι άνθρωποι, σύμφωνα με τον νόμο, όταν κυκλοφορούν δύο νομίσματα με την ίδια ονομαστική αξία;", ["Ξοδεύουν το φτωχότερο και κρατούν ή λιώνουν το καλύτερο", "Ξοδεύουν πρώτα το καλύτερο", "Τα ανταλλάσσουν με ξένα νομίσματα", "Τα καταθέτουν στην τράπεζα"], 0, "οι άνθρωποι ξοδεύουν το φτωχότερο και κρατούν, ή λιώνουν, το καλύτερο"),
  Q("Πότε ισχύει ο νόμος, σύμφωνα με τον ομιλητή;", ["Μόνο σε καιρό πολέμου", "Πάντα, χωρίς εξαιρέσεις", "Μόνο για τα ασημένια νομίσματα", "Μόνο όταν το κράτος υποχρεώνει τους πολίτες να δέχονται και τα δύο νομίσματα στην ίδια αξία"], 3, "ο νόμος ισχύει μόνο όταν ο νόμος του κράτους υποχρεώνει τους πολίτες να δέχονται και τα δύο νομίσματα στην ίδια αξία"),
 ],
 "gloss": {"χορός": "χορός — chorus (in ancient drama)", "παραπονιέται": "παραπονιέμαι — to complain", "ασημένια": "ασημένιος — silver (adj.)", "νομίσματα": "νόμισμα — coin, currency", "παραμερίσει": "παραμερίζω — to set aside", "χάλκινα": "χάλκινος — bronze, copper (adj.)", "σύμβουλος": "σύμβουλος — adviser", "διατυπώσει": "διατυπώνω — to formulate", "ονομαστική αξία": "ονομαστική αξία — face value", "πολύτιμο": "πολύτιμος — precious", "λιώνουν": "λιώνω — to melt down", "μεταφορικά": "μεταφορικά — metaphorically", "πρόχειρη": "πρόχειρος — sloppy, makeshift"}
})

ITEMS.append({
 "id": "l136-c1-galanos", "title": "Δημήτριος Γαλανός, ο Έλληνας της Βαρανάσι", "title_en": "Dimitrios Galanos, the Greek of Varanasi", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια ιστορικό για τον Δημήτριο Γαλανό.",
 "script": [
  L("Δημοσιογράφος", "m", "Ποιος ήταν ο Δημήτριος Γαλανός;", "Who was Dimitrios Galanos?"),
  L("Ιστορικός", "f", "Ήταν ένας Αθηναίος λόγιος, γεννημένος το 1760, που θεωρείται ο πρώτος Έλληνας ινδολόγος. Νέος ακόμα, γύρω στο 1786, ταξίδεψε στην Ινδία, στην Καλκούτα, για να διδάξει τα παιδιά των Ελλήνων εμπόρων που ζούσαν εκεί.", "He was a scholar from Athens, born in 1760, who is considered the first Greek Indologist. While still young, around 1786, he travelled to India, to Calcutta, to teach the children of the Greek merchants living there."),
  L("Δημοσιογράφος", "m", "Και δεν γύρισε ποτέ;", "And he never came back?"),
  L("Ιστορικός", "f", "Όχι. Μετά από μερικά χρόνια εγκαταστάθηκε στη Βαρανάσι, την ιερή πόλη στις όχθες του Γάγγη, όπου έζησε σχεδόν σαράντα χρόνια. Εκεί έμαθε σανσκριτικά από Ινδούς σοφούς και, σύμφωνα με τις πηγές, ζούσε λιτά, σαν ασκητής, και ντυνόταν με τα ρούχα του τόπου.", "No. After a few years he settled in Varanasi, the holy city on the banks of the Ganges, where he lived for almost forty years. There he learned Sanskrit from Indian sages and, according to the sources, lived frugally, like an ascetic, and dressed in local clothes."),
  L("Δημοσιογράφος", "m", "Τι άφησε πίσω του;", "What did he leave behind?"),
  L("Ιστορικός", "f", "Μετέφρασε στα ελληνικά σημαντικά ινδικά κείμενα, ανάμεσά τους τη «Μπαγκαβάτ Γκίτα», και συνέταξε ένα σανσκριτικό λεξικό. Πέθανε στη Βαρανάσι το 1833. Οι μεταφράσεις του εκδόθηκαν στην Αθήνα μετά τον θάνατό του. Για πολλούς είναι ένα σπάνιο παράδειγμα λόγιου που πήγε να μάθει από έναν άλλο πολιτισμό, και όχι να τον διδάξει.", "He translated important Indian texts into Greek, among them the 'Bhagavad Gita', and compiled a Sanskrit dictionary. He died in Varanasi in 1833. His translations were published in Athens after his death. For many he is a rare example of a scholar who went to learn from another civilisation, not to teach it."),
 ],
 "questions": [
  Q("Γιατί πήγε αρχικά στην Ινδία;", ["Για να κάνει εμπόριο", "Για να διδάξει τα παιδιά των Ελλήνων εμπόρων στην Καλκούτα", "Για να μελετήσει τη βουδιστική φιλοσοφία", "Ως διπλωμάτης"], 1, "για να διδάξει τα παιδιά των Ελλήνων εμπόρων που ζούσαν εκεί"),
  Q("Πώς ζούσε στη Βαρανάσι, σύμφωνα με τις πηγές;", ["Σε ένα παλάτι", "Ως πλούσιος έμπορος", "Λιτά, σαν ασκητής, με τα ρούχα του τόπου", "Με την οικογένειά του"], 2, "ζούσε λιτά, σαν ασκητής, και ντυνόταν με τα ρούχα του τόπου"),
  Q("Τι συνέταξε, εκτός από τις μεταφράσεις;", ["Ένα σανσκριτικό λεξικό", "Μια ιστορία της Ινδίας", "Μια γραμματική της αρχαίας ελληνικής", "Ένα ταξιδιωτικό ημερολόγιο"], 0, "συνέταξε ένα σανσκριτικό λεξικό"),
  Q("Γιατί τον θεωρούν πολλοί σπάνιο παράδειγμα;", ["Γιατί έγραψε στα αγγλικά", "Γιατί έγινε πλούσιος", "Γιατί γύρισε στην Αθήνα και ίδρυσε σχολείο", "Γιατί πήγε να μάθει από έναν άλλο πολιτισμό και όχι να τον διδάξει"], 3, "λόγιου που πήγε να μάθει από έναν άλλο πολιτισμό, και όχι να τον διδάξει"),
 ],
 "gloss": {"λόγιος": "λόγιος — scholar", "ινδολόγος": "ινδολόγος — Indologist", "εμπόρων": "έμπορος — merchant", "εγκαταστάθηκε": "εγκαθίσταμαι — to settle", "όχθες": "όχθη — bank (of a river)", "σανσκριτικά": "σανσκριτικά — Sanskrit", "σοφούς": "σοφός — sage", "λιτά": "λιτά — frugally", "ασκητής": "ασκητής — ascetic", "συνέταξε": "συντάσσω — to compile", "εκδόθηκαν": "εκδίδομαι — to be published", "πολιτισμό": "πολιτισμός — civilisation"}
})

rnd = random.Random(136)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-136.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
