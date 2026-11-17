# Source for library/listening/listening-132.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l132.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l132-ann-diavatiria", "title": "Νέο ωράριο για τα διαβατήρια", "title_en": "New opening hours for passports", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε στο ραδιόφωνο μια ανακοίνωση της αστυνομίας για την έκδοση διαβατηρίων.",
 "script": [
  L("Εκφωνήτρια", "f", "Η Διεύθυνση Αστυνομίας ανακοινώνει ότι, λόγω του μεγάλου αριθμού αιτήσεων πριν από το καλοκαίρι, το γραφείο διαβατηρίων θα λειτουργεί από τη Δευτέρα και τα απογεύματα, από τις τέσσερις έως τις οχτώ, καθώς και το πρωί του Σαββάτου.", "The Police Directorate announces that, because of the large number of applications before the summer, from Monday the passport office will also be open in the afternoons, from four to eight, as well as on Saturday mornings."),
  L("Εκφωνήτρια", "f", "Οι πολίτες εξυπηρετούνται μόνο με ραντεβού, το οποίο κλείνεται ηλεκτρονικά. Πριν από το ραντεβού πρέπει να έχει πληρωθεί το παράβολο, και ο αιτών να έχει μαζί του την ταυτότητα και μία πρόσφατη φωτογραφία.", "Citizens are served by appointment only, which is booked online. Before the appointment the fee must have been paid, and the applicant must bring their identity card and one recent photograph."),
  L("Εκφωνήτρια", "f", "Για τα ανήλικα παιδιά είναι απαραίτητη η παρουσία και των δύο γονέων ή μια υπεύθυνη δήλωση του γονέα που απουσιάζει. Τα νέα διαβατήρια παραδίδονται συνήθως μέσα σε μία εβδομάδα.", "For minors the presence of both parents is necessary, or a signed declaration from the absent parent. New passports are usually delivered within one week."),
 ],
 "questions": [
  Q("Τι αλλάζει από τη Δευτέρα στο γραφείο διαβατηρίων;", ["Κλείνει για ανακαίνιση", "Θα λειτουργεί και απογεύματα και Σάββατο πρωί", "Μεταφέρεται σε άλλο κτίριο", "Καταργούνται τα ραντεβού"], 1, "θα λειτουργεί από τη Δευτέρα και τα απογεύματα"),
  Q("Τι πρέπει να έχει γίνει πριν από το ραντεβού;", ["Να έχει σταλεί η ταυτότητα", "Να έχει γίνει αίτηση στο δημαρχείο", "Να έχει πληρωθεί το παράβολο", "Να έχουν τραβηχτεί οι φωτογραφίες στο γραφείο"], 2, "πρέπει να έχει πληρωθεί το παράβολο"),
  Q("Τι χρειάζεται για ένα ανήλικο παιδί;", ["Η παρουσία και των δύο γονέων ή υπεύθυνη δήλωση του γονέα που απουσιάζει", "Μόνο το πιστοποιητικό γέννησης", "Μια βεβαίωση από το σχολείο", "Δύο φωτογραφίες αντί για μία"], 0, "είναι απαραίτητη η παρουσία και των δύο γονέων ή μια υπεύθυνη δήλωση του γονέα που απουσιάζει"),
 ],
 "gloss": {"διαβατηρίων": "διαβατήριο — passport", "έκδοση": "έκδοση — issue", "αιτήσεων": "αίτηση — application", "ραντεβού": "ραντεβού — appointment", "παράβολο": "παράβολο — (official) fee", "αιτών": "ο αιτών — the applicant", "ταυτότητα": "ταυτότητα — identity card", "ανήλικα": "ανήλικος — minor, under-age", "υπεύθυνη δήλωση": "υπεύθυνη δήλωση — signed (sworn) declaration", "απουσιάζει": "απουσιάζω — to be absent", "παραδίδονται": "παραδίδομαι — to be delivered"}
})

ITEMS.append({
 "id": "l132-vm-presveia-viza", "title": "Μήνυμα από την πρεσβεία για τη βίζα", "title_en": "A message from the embassy about the visa", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κάνει αίτηση για βίζα σε μια ξένη πρεσβεία. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα σας, σας καλούμε από το προξενικό τμήμα της πρεσβείας, σχετικά με την αίτησή σας για τουριστική βίζα. Η αίτησή σας είναι σχεδόν πλήρης, αλλά λείπει ένα δικαιολογητικό: η βεβαίωση από τον εργοδότη σας ότι έχετε πάρει άδεια για τις ημερομηνίες του ταξιδιού.", "Good morning, we're calling from the consular section of the embassy about your application for a tourist visa. Your application is almost complete, but one supporting document is missing: the certificate from your employer that you've been granted leave for the dates of the trip."),
  L("Υπάλληλος", "m", "Μπορείτε να τη στείλετε σκαναρισμένη στο ηλεκτρονικό ταχυδρομείο του τμήματος μέσα σε δέκα εργάσιμες ημέρες. Αν δεν τη λάβουμε έγκαιρα, η αίτηση θα απορριφθεί και θα χρειαστεί να πληρώσετε ξανά το τέλος.", "You can send it scanned to the section's email within ten working days. If we don't receive it in time, the application will be rejected and you'll need to pay the fee again."),
  L("Υπάλληλος", "m", "Το διαβατήριό σας παραμένει στην πρεσβεία. Θα σας ενημερώσουμε με γραπτό μήνυμα πότε μπορείτε να περάσετε να το παραλάβετε. Ευχαριστούμε.", "Your passport remains at the embassy. We'll inform you by text message when you can come and collect it. Thank you."),
 ],
 "questions": [
  Q("Τι λείπει από την αίτηση;", ["Μια φωτογραφία", "Η βεβαίωση του εργοδότη για την άδεια", "Το εισιτήριο του αεροπλάνου", "Η κράτηση του ξενοδοχείου"], 1, "λείπει ένα δικαιολογητικό: η βεβαίωση από τον εργοδότη σας"),
  Q("Τι θα συμβεί αν το δικαιολογητικό δεν σταλεί έγκαιρα;", ["Το ταξίδι θα καθυστερήσει μία εβδομάδα", "Θα χρειαστεί συνέντευξη στην πρεσβεία", "Η αίτηση θα απορριφθεί και θα πρέπει να πληρωθεί ξανά το τέλος", "Θα επιστραφούν τα χρήματα"], 2, "η αίτηση θα απορριφθεί και θα χρειαστεί να πληρώσετε ξανά το τέλος"),
  Q("Πώς θα μάθει ο αιτών πότε να παραλάβει το διαβατήριο;", ["Με γραπτό μήνυμα", "Με επιστολή", "Θα του τηλεφωνήσουν ξανά", "Θα το δει στην ιστοσελίδα"], 0, "Θα σας ενημερώσουμε με γραπτό μήνυμα"),
 ],
 "gloss": {"πρεσβεία": "πρεσβεία — embassy", "βίζα": "βίζα — visa", "προξενικό": "προξενικός — consular", "δικαιολογητικό": "δικαιολογητικό — supporting document", "βεβαίωση": "βεβαίωση — certificate", "εργοδότη": "εργοδότης — employer", "σκαναρισμένη": "σκαναρισμένος — scanned", "εργάσιμες": "εργάσιμος — working (day)", "απορριφθεί": "απορρίπτομαι — to be rejected", "τέλος": "τέλος — fee", "παραλάβετε": "παραλαμβάνω — to collect, receive"}
})

ITEMS.append({
 "id": "l132-dial-fotovoltaika", "title": "Να βάλουμε φωτοβολταϊκά στη στέγη;", "title_en": "Shall we put solar panels on the roof?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι συζητά αν θα βάλει φωτοβολταϊκά πάνελ στη στέγη του σπιτιού του.",
 "script": [
  L("Κώστας", "m", "Ο λογαριασμός του ρεύματος ήρθε πάλι διακόσια ευρώ. Σκέφτομαι σοβαρά να βάλουμε φωτοβολταϊκά στη στέγη. Ο γείτονας λέει ότι πληρώνει πια σχεδόν τα μισά.", "The electricity bill came to two hundred euros again. I'm seriously thinking of putting solar panels on the roof. The neighbour says he now pays almost half."),
  L("Ελπίδα", "f", "Ναι, αλλά πόσο κοστίζει η εγκατάσταση; Δεν θέλω να πάρουμε δάνειο για κάτι που θα αποσβεστεί σε δεκαπέντε χρόνια.", "Yes, but how much does the installation cost? I don't want to take out a loan for something that will pay for itself in fifteen years."),
  L("Κώστας", "m", "Ρώτησα σε μια εταιρεία. Για ένα σύστημα σαν το δικό μας, με την επιδότηση που δίνει τώρα το κράτος, η απόσβεση είναι περίπου έξι με επτά χρόνια.", "I asked a company. For a system like ours, with the subsidy the state gives now, the payback is about six or seven years."),
  L("Ελπίδα", "f", "Εντάξει, αυτό ακούγεται λογικό. Πρώτα όμως ας ελέγξει κάποιος αν αντέχει η στέγη το βάρος. Είναι παλιά, θυμάσαι τι έγινε με τα κεραμίδια πέρσι;", "OK, that sounds reasonable. But first let someone check whether the roof can take the weight. It's old; remember what happened with the tiles last year?"),
 ],
 "questions": [
  Q("Γιατί θέλει ο Κώστας να βάλουν φωτοβολταϊκά;", ["Γιατί το ζήτησε ο δήμος", "Γιατί ο λογαριασμός του ρεύματος είναι πολύ ακριβός", "Γιατί η στέγη χρειάζεται επισκευή", "Γιατί του έκαναν δώρο τα πάνελ"], 1, "Ο λογαριασμός του ρεύματος ήρθε πάλι διακόσια ευρώ"),
  Q("Σε πόσο χρόνο θα αποσβεστεί, σύμφωνα με την εταιρεία, η εγκατάσταση;", ["Σε δεκαπέντε χρόνια", "Σε δύο χρόνια", "Σε έξι με επτά χρόνια", "Σε έναν χρόνο"], 2, "η απόσβεση είναι περίπου έξι με επτά χρόνια"),
  Q("Τι θέλει να γίνει πρώτα η Ελπίδα;", ["Να ελεγχθεί αν η στέγη αντέχει το βάρος", "Να πάρουν δάνειο", "Να μιλήσουν με τον γείτονα", "Να αλλάξουν εταιρεία ρεύματος"], 0, "Πρώτα όμως ας ελέγξει κάποιος αν αντέχει η στέγη το βάρος"),
 ],
 "gloss": {"φωτοβολταϊκά": "φωτοβολταϊκά — solar (photovoltaic) panels", "πάνελ": "πάνελ — panel", "στέγη": "στέγη — roof", "λογαριασμός του ρεύματος": "λογαριασμός του ρεύματος — electricity bill", "εγκατάσταση": "εγκατάσταση — installation", "δάνειο": "δάνειο — loan", "αποσβεστεί": "αποσβένομαι — to pay for itself", "επιδότηση": "επιδότηση — subsidy", "απόσβεση": "απόσβεση — payback", "αντέχει": "αντέχω — to bear, withstand", "κεραμίδια": "κεραμίδι — roof tile"}
})

ITEMS.append({
 "id": "l132-int-anarrichitria", "title": "Μια αναρριχήτρια στα Μετέωρα", "title_en": "A rock climber at Meteora", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια ραδιοφωνική συνέντευξη με μια νέα γυναίκα που κάνει αναρρίχηση στους βράχους των Μετεώρων.",
 "script": [
  L("Δημοσιογράφος", "m", "Ιουλία, γιατί έρχονται αναρριχητές από όλο τον κόσμο στα Μετέωρα;", "Ioulia, why do climbers come from all over the world to Meteora?"),
  L("Αναρριχήτρια", "f", "Γιατί οι βράχοι εδώ δεν μοιάζουν με κανέναν άλλον. Είναι από ένα πέτρωμα σαν τσιμέντο με χαλίκια, οπότε σκαρφαλώνεις πιάνοντας στρογγυλές πέτρες. Και όταν φτάνεις στην κορυφή, βλέπεις απέναντι τα μοναστήρια. Είναι μαγικό.", "Because the rocks here are like no others. They're made of a rock like concrete with pebbles, so you climb by holding on to round stones. And when you reach the top, you see the monasteries opposite. It's magical."),
  L("Δημοσιογράφος", "m", "Επιτρέπεται να σκαρφαλώνει κανείς παντού;", "Is one allowed to climb everywhere?"),
  L("Αναρριχήτρια", "f", "Όχι. Υπάρχουν κανόνες, που τους σεβόμαστε. Δεν σκαρφαλώνουμε στους βράχους με τα μοναστήρια, και την άνοιξη αποφεύγουμε κάποιες διαδρομές, γιατί φωλιάζουν εκεί αρπακτικά πουλιά.", "No. There are rules, and we respect them. We don't climb the rocks with the monasteries, and in spring we avoid some routes, because birds of prey nest there."),
  L("Δημοσιογράφος", "m", "Δεν φοβάσαι;", "Aren't you afraid?"),
  L("Αναρριχήτρια", "f", "Φυσικά, και αυτό είναι καλό. Ο φόβος σε κάνει προσεκτική. Ελέγχω πάντα δύο φορές τα σχοινιά και τον εξοπλισμό, και δεν σκαρφαλώνω ποτέ μόνη μου.", "Of course, and that's good. Fear makes you careful. I always double-check the ropes and the equipment, and I never climb alone."),
 ],
 "questions": [
  Q("Τι κάνει ξεχωριστούς τους βράχους των Μετεώρων;", ["Είναι οι ψηλότεροι στην Ευρώπη", "Είναι από ένα πέτρωμα με στρογγυλές πέτρες, σαν τσιμέντο με χαλίκια", "Είναι πολύ λείοι", "Είναι από μάρμαρο"], 1, "Είναι από ένα πέτρωμα σαν τσιμέντο με χαλίκια"),
  Q("Γιατί αποφεύγουν την άνοιξη κάποιες διαδρομές;", ["Γιατί βρέχει πολύ", "Γιατί έρχονται πολλοί τουρίστες", "Γιατί φωλιάζουν εκεί αρπακτικά πουλιά", "Γιατί γίνονται εργασίες"], 2, "γιατί φωλιάζουν εκεί αρπακτικά πουλιά"),
  Q("Τι λέει η Ιουλία για τον φόβο;", ["Ότι είναι καλός, γιατί την κάνει προσεκτική", "Ότι δεν φοβάται ποτέ", "Ότι γι' αυτό σκαρφαλώνει μόνη", "Ότι τον ξεπέρασε με τα χρόνια"], 0, "Φυσικά, και αυτό είναι καλό. Ο φόβος σε κάνει προσεκτική"),
 ],
 "gloss": {"αναρρίχηση": "αναρρίχηση — rock climbing", "αναρριχητές": "αναρριχητής — climber", "πέτρωμα": "πέτρωμα — rock (type)", "τσιμέντο": "τσιμέντο — concrete, cement", "χαλίκια": "χαλίκι — pebble, gravel", "σκαρφαλώνεις": "σκαρφαλώνω — to climb", "σεβόμαστε": "σέβομαι — to respect", "διαδρομές": "διαδρομή — route", "αρπακτικά": "αρπακτικό — bird of prey", "σχοινιά": "σχοινί — rope", "εξοπλισμό": "εξοπλισμός — equipment"}
})

ITEMS.append({
 "id": "l132-rep-agrotourismos-kriti", "title": "Αγροτουρισμός σε ένα χωριό της Κρήτης", "title_en": "Agritourism in a Cretan village", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα χωριό της Κρήτης που υποδέχεται επισκέπτες στις αγροτικές του δουλειές.",
 "script": [
  L("Ρεπόρτερ", "f", "Σε ένα χωριό στους πρόποδες του Ψηλορείτη, μερικές οικογένειες αγροτών ένωσαν τις δυνάμεις τους και άνοιξαν τα σπίτια και τα χωράφια τους στους επισκέπτες. Εδώ δεν υπάρχουν μεγάλα ξενοδοχεία, μόνο παλιά πέτρινα σπίτια που ανακαινίστηκαν με προσοχή.", "In a village at the foot of Mount Psiloritis, some farming families joined forces and opened their homes and fields to visitors. There are no big hotels here, just old stone houses that were carefully renovated."),
  L("Ρεπόρτερ", "f", "Οι επισκέπτες μπορούν να βοηθήσουν στο άρμεγμα, να μάθουν να φτιάχνουν τυρί ή να μαζέψουν χόρτα με τις γυναίκες του χωριού. Το φθινόπωρο συμμετέχουν και στη συγκομιδή των ελιών και στο ελαιοτριβείο.", "Visitors can help with the milking, learn to make cheese or gather wild greens with the women of the village. In autumn they also take part in the olive harvest and at the olive press."),
  L("Ρεπόρτερ", "f", "Για τους κατοίκους, ο αγροτουρισμός είναι ένα δεύτερο εισόδημα που τους επιτρέπει να μείνουν στον τόπο τους. Και οι νέοι δεν φεύγουν πια όλοι για την πόλη: δύο ζευγάρια επέστρεψαν πέρσι από το Ηράκλειο για να δουλέψουν στο πρόγραμμα.", "For the residents, agritourism is a second income that allows them to stay in their homeland. And the young no longer all leave for the city: two couples came back from Heraklion last year to work in the scheme."),
 ],
 "questions": [
  Q("Πού μένουν οι επισκέπτες;", ["Σε ένα μεγάλο ξενοδοχείο", "Σε παλιά πέτρινα σπίτια που ανακαινίστηκαν", "Σε σκηνές", "Στο Ηράκλειο"], 1, "μόνο παλιά πέτρινα σπίτια που ανακαινίστηκαν με προσοχή"),
  Q("Τι μπορούν να κάνουν οι επισκέπτες το φθινόπωρο;", ["Να κάνουν μπάνιο στη θάλασσα", "Να τρυγήσουν σταφύλια", "Να συμμετάσχουν στη συγκομιδή των ελιών", "Να κάνουν σκι στον Ψηλορείτη"], 2, "Το φθινόπωρο συμμετέχουν και στη συγκομιδή των ελιών"),
  Q("Τι κέρδισε το χωριό από τον αγροτουρισμό;", ["Ένα δεύτερο εισόδημα και νέους που επέστρεψαν", "Ένα καινούργιο σχολείο", "Έναν καινούργιο δρόμο", "Περισσότερα ξενοδοχεία"], 0, "ο αγροτουρισμός είναι ένα δεύτερο εισόδημα"),
 ],
 "gloss": {"αγροτουρισμός": "αγροτουρισμός — agritourism", "πρόποδες": "πρόποδες — foot (of a mountain)", "αγροτών": "αγρότης — farmer", "ανακαινίστηκαν": "ανακαινίζομαι — to be renovated", "άρμεγμα": "άρμεγμα — milking", "χόρτα": "χόρτα — (wild) greens", "συγκομιδή": "συγκομιδή — harvest", "ελαιοτριβείο": "ελαιοτριβείο — olive press", "εισόδημα": "εισόδημα — income", "επέστρεψαν": "επιστρέφω — to return"}
})

ITEMS.append({
 "id": "l132-rep-seismografos-scholeio", "title": "Ένας σεισμογράφος στην αυλή του σχολείου", "title_en": "A seismograph in the schoolyard", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα γυμνάσιο που απέκτησε δικό του σεισμογράφο.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε ένα γυμνάσιο της Πάτρας, οι μαθητές παρακολουθούν τους σεισμούς της περιοχής μέσα από την τάξη τους. Ένας μικρός σεισμογράφος, που τοποθετήθηκε σε ένα υπόγειο του σχολείου, στέλνει κάθε δευτερόλεπτο δεδομένα σε έναν υπολογιστή.", "At a lower secondary school in Patras, pupils follow the region's earthquakes from their classroom. A small seismograph, installed in a basement of the school, sends data to a computer every second."),
  L("Ρεπόρτερ", "m", "Τα στοιχεία αυτά καταλήγουν και σε ένα δίκτυο σχολείων και πανεπιστημίων, το οποίο τα χρησιμοποιεί για εκπαιδευτικούς σκοπούς. «Όταν γίνεται ένας σεισμός, τα παιδιά τρέχουν να δουν τη γραμμή στην οθόνη», λέει η καθηγήτρια φυσικής.", "This information also goes to a network of schools and universities, which uses it for educational purposes. 'When there's an earthquake, the children run to see the line on the screen,' says the physics teacher."),
  L("Ρεπόρτερ", "m", "Το πρόγραμμα έχει και πρακτικό στόχο: οι μαθητές μαθαίνουν πώς να προστατεύονται σε έναν σεισμό και διδάσκουν οι ίδιοι στους μικρότερους μαθητές του δημοτικού της γειτονιάς τι πρέπει να κάνουν.", "The scheme also has a practical aim: the pupils learn how to protect themselves in an earthquake, and they themselves teach the younger pupils of the neighbourhood primary school what to do."),
 ],
 "questions": [
  Q("Πού τοποθετήθηκε ο σεισμογράφος;", ["Στην ταράτσα του σχολείου", "Σε ένα υπόγειο του σχολείου", "Στην αυλή του δημοτικού", "Στο γραφείο του διευθυντή"], 1, "που τοποθετήθηκε σε ένα υπόγειο του σχολείου"),
  Q("Πού καταλήγουν και τα στοιχεία του σεισμογράφου;", ["Στην αστυνομία", "Σε μια τηλεοπτική εκπομπή", "Σε ένα δίκτυο σχολείων και πανεπιστημίων", "Στο υπουργείο"], 2, "καταλήγουν και σε ένα δίκτυο σχολείων και πανεπιστημίων"),
  Q("Τι κάνουν οι μαθητές για τα μικρότερα παιδιά;", ["Τους διδάσκουν τι πρέπει να κάνουν σε έναν σεισμό", "Τους χαρίζουν σεισμογράφους", "Τους δείχνουν πειράματα φυσικής", "Τους διαβάζουν παραμύθια"], 0, "διδάσκουν οι ίδιοι στους μικρότερους μαθητές του δημοτικού της γειτονιάς τι πρέπει να κάνουν"),
 ],
 "gloss": {"σεισμογράφο": "σεισμογράφος — seismograph", "σεισμούς": "σεισμός — earthquake", "τοποθετήθηκε": "τοποθετούμαι — to be installed, placed", "υπόγειο": "υπόγειο — basement", "δεδομένα": "δεδομένα — data", "στοιχεία": "στοιχεία — data, information", "καταλήγουν": "καταλήγω — to end up", "δίκτυο": "δίκτυο — network", "εκπαιδευτικούς": "εκπαιδευτικός — educational", "προστατεύονται": "προστατεύομαι — to protect oneself"}
})

ITEMS.append({
 "id": "l132-mono-epistrofi-germania", "title": "Γύρισα μετά από δέκα χρόνια στη Γερμανία", "title_en": "I came back after ten years in Germany", "type": "monologue", "level": "B2",
 "context_el": "Ένας μηχανικός μιλά για την επιστροφή του στην Ελλάδα μετά από δέκα χρόνια στο εξωτερικό.",
 "script": [
  L("Παναγιώτης", "m", "Έφυγα για τη Γερμανία το 2014, όταν η κρίση ήταν στο χειρότερο σημείο της. Είχα ένα πτυχίο μηχανικού και καμία δουλειά. Στο Μόναχο βρήκα δουλειά σε μια μεγάλη εταιρεία μέσα σε δύο μήνες.", "I left for Germany in 2014, when the crisis was at its worst. I had an engineering degree and no job. In Munich I found work at a big company within two months."),
  L("Παναγιώτης", "m", "Τα χρόνια εκεί ήταν καλά: καλός μισθός, οργάνωση, σεβασμός. Μου έλειπαν όμως πράγματα που δεν μπορούσα να εξηγήσω στους Γερμανούς φίλους μου: ο καφές που κρατάει τρεις ώρες, η γιαγιά μου, το φως του Οκτωβρίου.", "The years there were good: a good salary, organisation, respect. But I missed things I couldn't explain to my German friends: coffee that lasts three hours, my grandmother, the October light."),
  L("Παναγιώτης", "m", "Πέρσι η εταιρεία μου μού πρότεινε να δουλεύω από απόσταση, και γύρισα στη Θεσσαλονίκη. Ο μισθός είναι ο ίδιος, αλλά τα πράγματα δεν είναι εύκολα: τα ενοίκια έχουν ανέβει πολύ. Δεν μετανιώνω πάντως. Νιώθω ότι επιτέλους ζω στο σπίτι μου.", "Last year my company offered me remote work, and I came back to Thessaloniki. The salary is the same, but things aren't easy: rents have gone up a lot. I don't regret it, though. I feel that at last I'm living at home."),
 ],
 "questions": [
  Q("Γιατί έφυγε ο Παναγιώτης για τη Γερμανία;", ["Για να σπουδάσει", "Γιατί δεν έβρισκε δουλειά στην Ελλάδα λόγω της κρίσης", "Γιατί παντρεύτηκε μια Γερμανίδα", "Γιατί τον μετέθεσε η εταιρεία του"], 1, "Είχα ένα πτυχίο μηχανικού και καμία δουλειά"),
  Q("Τι του έλειπε στη Γερμανία;", ["Ο καλός μισθός", "Η οργάνωση", "Ο καφές που κρατάει ώρες, η γιαγιά του, το φως του Οκτωβρίου", "Οι Γερμανοί φίλοι του"], 2, "ο καφές που κρατάει τρεις ώρες, η γιαγιά μου, το φως του Οκτωβρίου"),
  Q("Ποιο πρόβλημα αντιμετωπίζει τώρα στη Θεσσαλονίκη;", ["Τα ενοίκια έχουν ανέβει πολύ", "Ο μισθός του μειώθηκε", "Δεν βρίσκει φίλους", "Έχασε τη δουλειά του"], 0, "τα ενοίκια έχουν ανέβει πολύ"),
 ],
 "gloss": {"μηχανικός": "μηχανικός — engineer", "εξωτερικό": "εξωτερικό — abroad", "κρίση": "κρίση — crisis", "πτυχίο": "πτυχίο — degree", "μισθός": "μισθός — salary", "οργάνωση": "οργάνωση — organisation", "σεβασμός": "σεβασμός — respect", "από απόσταση": "από απόσταση — remotely", "ενοίκια": "ενοίκιο — rent", "μετανιώνω": "μετανιώνω — to regret"}
})

ITEMS.append({
 "id": "l132-mono-anadochi-mitera", "title": "Γιατί έγινα ανάδοχη μητέρα", "title_en": "Why I became a foster mother", "type": "monologue", "level": "B2",
 "context_el": "Μια γυναίκα μιλά σε μια εκδήλωση για την εμπειρία της ως ανάδοχης μητέρας.",
 "script": [
  L("Σταυρούλα", "f", "Πριν από τρία χρόνια διάβασα ένα άρθρο για παιδιά που μεγαλώνουν σε ιδρύματα, επειδή οι γονείς τους δεν μπορούν, για διάφορους λόγους, να τα φροντίσουν. Με τον άντρα μου είχαμε ήδη μια κόρη, αλλά αποφασίσαμε να γίνουμε ανάδοχη οικογένεια.", "Three years ago I read an article about children who grow up in institutions because their parents can't, for various reasons, look after them. My husband and I already had a daughter, but we decided to become a foster family."),
  L("Σταυρούλα", "f", "Η διαδικασία κράτησε σχεδόν έναν χρόνο: συνεντεύξεις με κοινωνικούς λειτουργούς, σεμινάρια, έλεγχοι στο σπίτι. Ύστερα ήρθε σε εμάς ο Λευτέρης, ένα αγοράκι πέντε χρονών που δεν μιλούσε σχεδόν καθόλου.", "The process took almost a year: interviews with social workers, seminars, home checks. Then Lefteris came to us, a little boy of five who hardly spoke at all."),
  L("Σταυρούλα", "f", "Η αναδοχή δεν είναι υιοθεσία. Ο Λευτέρης βλέπει τακτικά τη μητέρα του, και ίσως κάποτε επιστρέψει κοντά της. Αυτό είναι το πιο δύσκολο για εμάς. Όμως σήμερα γελάει, πηγαίνει σχολείο και δεν σταματά να μιλάει. Αυτό μας φτάνει.", "Fostering is not adoption. Lefteris sees his mother regularly, and perhaps one day he'll go back to her. That's the hardest thing for us. But today he laughs, goes to school and never stops talking. That's enough for us."),
 ],
 "questions": [
  Q("Τι έκανε τη Σταυρούλα να σκεφτεί την αναδοχή;", ["Μια φίλη της που ήταν ανάδοχη μητέρα", "Ένα άρθρο για παιδιά που μεγαλώνουν σε ιδρύματα", "Μια τηλεοπτική εκπομπή", "Η κόρη της"], 1, "διάβασα ένα άρθρο για παιδιά που μεγαλώνουν σε ιδρύματα"),
  Q("Πώς ήταν ο Λευτέρης όταν ήρθε στην οικογένεια;", ["Πολύ ζωηρός", "Άρρωστος", "Δεν μιλούσε σχεδόν καθόλου", "Δεν ήθελε να πάει σχολείο"], 2, "ένα αγοράκι πέντε χρονών που δεν μιλούσε σχεδόν καθόλου"),
  Q("Ποιο είναι το πιο δύσκολο για την οικογένεια;", ["Ότι ο Λευτέρης ίσως κάποτε επιστρέψει στη μητέρα του", "Ότι η διαδικασία κράτησε πολύ", "Ότι ο Λευτέρης δεν τα πάει καλά με την κόρη τους", "Ότι δεν έχουν αρκετό χώρο στο σπίτι"], 0, "ίσως κάποτε επιστρέψει κοντά της. Αυτό είναι το πιο δύσκολο για εμάς"),
 ],
 "gloss": {"ανάδοχη": "ανάδοχος — foster (parent)", "ιδρύματα": "ίδρυμα — institution, (children's) home", "φροντίσουν": "φροντίζω — to look after", "διαδικασία": "διαδικασία — process", "κοινωνικούς λειτουργούς": "κοινωνικός λειτουργός — social worker", "σεμινάρια": "σεμινάριο — seminar, course", "αναδοχή": "αναδοχή — fostering", "υιοθεσία": "υιοθεσία — adoption", "τακτικά": "τακτικά — regularly"}
})

ITEMS.append({
 "id": "l132-c1-ringelmann", "title": "Γιατί η ομάδα τραβάει λιγότερο", "title_en": "Why a team pulls less", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη για την ψυχολογία της ομαδικής εργασίας.",
 "script": [
  L("Ομιλήτρια", "f", "Στις αρχές του 20ού αιώνα, ένας Γάλλος γεωπόνος, ο Μαξιμιλιέν Ρινγκελμάν, ήθελε να μάθει πόσο αποδοτικά δουλεύουν οι άνθρωποι και τα ζώα στις αγροτικές εργασίες. Ζήτησε λοιπόν από εθελοντές να τραβήξουν ένα σχοινί, πρώτα μόνοι τους και ύστερα σε ομάδες, και μέτρησε τη δύναμη που ασκούσαν.", "At the beginning of the twentieth century, a French agricultural engineer, Maximilien Ringelmann, wanted to find out how efficiently people and animals work in farm tasks. So he asked volunteers to pull a rope, first alone and then in groups, and measured the force they exerted."),
  L("Ομιλήτρια", "f", "Το αποτέλεσμα ήταν απρόσμενο. Η ομάδα, φυσικά, τραβούσε περισσότερο από τον καθένα χωριστά, όχι όμως όσο το άθροισμα των ατομικών δυνάμεων. Όσο μεγάλωνε η ομάδα, τόσο μειωνόταν η προσπάθεια του καθενός· σε ομάδες των οχτώ ατόμων, σύμφωνα με τις μετρήσεις του, έφτανε περίπου στο μισό.", "The result was unexpected. The group, of course, pulled more than each person separately, but not as much as the sum of the individual forces. The larger the group grew, the more each person's effort declined; in groups of eight, according to his measurements, it fell to about half."),
  L("Ομιλήτρια", "f", "Δύο εξηγήσεις έχουν προταθεί. Η πρώτη είναι πρακτική: σε μια ομάδα οι κινήσεις δεν συντονίζονται τέλεια, και ένα μέρος της δύναμης χάνεται. Η δεύτερη είναι ψυχολογική, και οι ψυχολόγοι την ονόμασαν αργότερα «κοινωνική οκνηρία»: όταν η συμβολή μας χάνεται μέσα στο σύνολο, χαλαρώνουμε, συχνά χωρίς να το καταλαβαίνουμε.", "Two explanations have been proposed. The first is practical: in a group, movements aren't perfectly coordinated, and part of the force is lost. The second is psychological, and psychologists later called it 'social loafing': when our contribution is lost within the whole, we slack off, often without realising it."),
  L("Ομιλήτρια", "f", "Τι σημαίνει αυτό για έναν χώρο εργασίας; Οι έρευνες δείχνουν ότι το φαινόμενο περιορίζεται όταν η συμβολή του καθενός είναι ορατή και αναγνωρίζεται, όταν οι ομάδες είναι μικρές και όταν οι συμμετέχοντες πιστεύουν πραγματικά στον στόχο. Με άλλα λόγια, δεν φταίει η ομάδα· φταίει η αφάνεια.", "What does this mean for a workplace? Research shows that the effect is reduced when each person's contribution is visible and recognised, when teams are small and when participants really believe in the goal. In other words, it's not the team that's to blame; it's invisibility."),
 ],
 "questions": [
  Q("Τι ήθελε να μάθει αρχικά ο Ρινγκελμάν;", ["Πόσο δυνατοί είναι οι αθλητές", "Πόσο αποδοτικά δουλεύουν άνθρωποι και ζώα στις αγροτικές εργασίες", "Γιατί οι άνθρωποι προτιμούν να δουλεύουν μόνοι", "Πώς επηρεάζει η κούραση την απόδοση"], 1, "ήθελε να μάθει πόσο αποδοτικά δουλεύουν οι άνθρωποι και τα ζώα στις αγροτικές εργασίες"),
  Q("Τι διαπίστωσε όσο μεγάλωνε η ομάδα;", ["Η ομάδα τραβούσε λιγότερο από ένα άτομο", "Η δύναμη της ομάδας ήταν ίση με το άθροισμα των ατομικών δυνάμεων", "Μειωνόταν η προσπάθεια του καθενός", "Οι εθελοντές κουράζονταν γρηγορότερα"], 2, "Όσο μεγάλωνε η ομάδα, τόσο μειωνόταν η προσπάθεια του καθενός"),
  Q("Ποια είναι η ψυχολογική εξήγηση του φαινομένου;", ["Όταν η συμβολή μας χάνεται μέσα στο σύνολο, χαλαρώνουμε", "Οι άνθρωποι δεν εμπιστεύονται τους άλλους", "Οι κινήσεις δεν συντονίζονται τέλεια", "Οι εθελοντές δεν πληρώνονταν"], 0, "όταν η συμβολή μας χάνεται μέσα στο σύνολο, χαλαρώνουμε"),
  Q("Τι συμπεραίνει η ομιλήτρια;", ["Ότι η ομαδική εργασία πρέπει να καταργηθεί", "Ότι οι μεγάλες ομάδες είναι πιο αποδοτικές", "Ότι το πρόβλημα λύνεται μόνο με χρήματα", "Ότι φταίει η αφάνεια της ατομικής συμβολής, όχι η ομάδα"], 3, "δεν φταίει η ομάδα· φταίει η αφάνεια"),
 ],
 "gloss": {"γεωπόνος": "γεωπόνος — agricultural engineer, agronomist", "αποδοτικά": "αποδοτικά — efficiently", "ασκούσαν": "ασκώ — to exert", "απρόσμενο": "απρόσμενος — unexpected", "άθροισμα": "άθροισμα — sum", "ατομικών": "ατομικός — individual", "συντονίζονται": "συντονίζομαι — to be coordinated", "οκνηρία": "οκνηρία — idleness, loafing", "συμβολή": "συμβολή — contribution", "σύνολο": "σύνολο — whole", "χαλαρώνουμε": "χαλαρώνω — to relax, slack off", "ορατή": "ορατός — visible", "αφάνεια": "αφάνεια — obscurity, invisibility"}
})

ITEMS.append({
 "id": "l132-c1-kairis", "title": "Θεόφιλος Καΐρης, ο δάσκαλος της Άνδρου", "title_en": "Theofilos Kairis, the teacher of Andros", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με έναν ιστορικό για τον λόγιο και κληρικό Θεόφιλο Καΐρη.",
 "script": [
  L("Δημοσιογράφος", "f", "Ποιος ήταν ο Θεόφιλος Καΐρης;", "Who was Theofilos Kairis?"),
  L("Ιστορικός", "m", "Ήταν ένας από τους σημαντικότερους λόγιους του Νεοελληνικού Διαφωτισμού. Γεννήθηκε στην Άνδρο το 1784, σπούδασε στην Ακαδημία των Κυδωνιών και αργότερα στην Ιταλία και στη Γαλλία, όπου μελέτησε φιλοσοφία και θετικές επιστήμες. Γύρισε για να διδάξει στις Κυδωνίες, όπου, σύμφωνα με τις πηγές, οι παραδόσεις του είχαν πολλούς ακροατές.", "He was one of the most important scholars of the Modern Greek Enlightenment. He was born on Andros in 1784, studied at the Academy of Kydonies and later in Italy and France, where he studied philosophy and the natural sciences. He came back to teach at Kydonies, where, according to the sources, his lectures drew many listeners."),
  L("Δημοσιογράφος", "f", "Και στην Επανάσταση;", "And in the Revolution?"),
  L("Ιστορικός", "m", "Το 1821, αν και κληρικός, ύψωσε τη σημαία της Επανάστασης στην Άνδρο και πολέμησε ο ίδιος σε μάχες, όπου και τραυματίστηκε. Μετά την απελευθέρωση, όμως, αφιερώθηκε σε αυτό που θεωρούσε την πραγματική του αποστολή: ίδρυσε στην Άνδρο ένα ορφανοτροφείο-σχολείο για τα παιδιά των αγωνιστών, με προχωρημένες για την εποχή μεθόδους διδασκαλίας.", "In 1821, although a cleric, he raised the flag of the Revolution on Andros and fought in battles himself, where he was also wounded. After liberation, however, he devoted himself to what he considered his true mission: he founded on Andros an orphanage-school for the children of the fighters, with teaching methods advanced for the time."),
  L("Δημοσιογράφος", "f", "Γιατί όμως συγκρούστηκε με την Εκκλησία;", "But why did he clash with the Church?"),
  L("Ιστορικός", "m", "Διότι ανέπτυξε μια δική του θρησκευτική και φιλοσοφική διδασκαλία, τη «Θεοσέβεια», που απομακρυνόταν από την ορθόδοξη παράδοση. Η Εκκλησία τον καταδίκασε, έκλεισε το σχολείο του, και ο ίδιος διώχθηκε. Πέθανε το 1853 στη φυλακή της Σύρου. Σήμερα πολλοί τον θυμούνται κυρίως ως έναν από τους πρωτοπόρους της ελευθερίας της σκέψης στην Ελλάδα.", "Because he developed a religious and philosophical teaching of his own, 'Theosebeia', which departed from the Orthodox tradition. The Church condemned him, his school was closed, and he himself was persecuted. He died in 1853 in the prison of Syros. Today many remember him chiefly as one of the pioneers of freedom of thought in Greece."),
 ],
 "questions": [
  Q("Πού σπούδασε ο Καΐρης, εκτός από τις Κυδωνίες;", ["Στη Ρωσία και στην Αυστρία", "Στην Ιταλία και στη Γαλλία", "Στην Αθήνα", "Στην Κωνσταντινούπολη"], 1, "αργότερα στην Ιταλία και στη Γαλλία"),
  Q("Τι έκανε το 1821;", ["Έφυγε στο εξωτερικό", "Έγραψε τον πρώτο νόμο του κράτους", "Ύψωσε τη σημαία της Επανάστασης στην Άνδρο και πολέμησε", "Έγινε επίσκοπος της Άνδρου"], 2, "ύψωσε τη σημαία της Επανάστασης στην Άνδρο και πολέμησε ο ίδιος σε μάχες"),
  Q("Τι ίδρυσε μετά την απελευθέρωση;", ["Ένα ορφανοτροφείο-σχολείο για τα παιδιά των αγωνιστών", "Ένα πανεπιστήμιο στη Σύρο", "Μια εφημερίδα", "Ένα μοναστήρι"], 0, "ίδρυσε στην Άνδρο ένα ορφανοτροφείο-σχολείο για τα παιδιά των αγωνιστών"),
  Q("Γιατί συγκρούστηκε με την Εκκλησία;", ["Γιατί έκλεισε τις εκκλησίες της Άνδρου", "Γιατί αρνήθηκε να πολεμήσει", "Γιατί υποστήριξε τους Οθωμανούς", "Γιατί ανέπτυξε μια διδασκαλία που απομακρυνόταν από την ορθόδοξη παράδοση"], 3, "που απομακρυνόταν από την ορθόδοξη παράδοση"),
 ],
 "gloss": {"λόγιο": "λόγιος — scholar", "κληρικό": "κληρικός — cleric, clergyman", "Διαφωτισμού": "Διαφωτισμός — the Enlightenment", "θετικές επιστήμες": "θετικές επιστήμες — natural sciences", "παραδόσεις": "παράδοση — lecture; tradition", "ακροατές": "ακροατής — listener", "ύψωσε": "υψώνω — to raise", "τραυματίστηκε": "τραυματίζομαι — to be wounded", "αποστολή": "αποστολή — mission", "ορφανοτροφείο": "ορφανοτροφείο — orphanage", "αγωνιστών": "αγωνιστής — fighter (of 1821)", "καταδίκασε": "καταδικάζω — to condemn", "διώχθηκε": "διώκομαι — to be persecuted", "πρωτοπόρους": "πρωτοπόρος — pioneer"}
})

rnd = random.Random(132)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-132.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
