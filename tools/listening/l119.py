# Source for library/listening/listening-119.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l119.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l119-ann-yperarithmi-ptisi", "title": "Υπεράριθμη πτήση: ζητούνται εθελοντές", "title_en": "An overbooked flight: volunteers wanted", "type": "announcement", "level": "B2",
 "context_el": "Περιμένετε στην πύλη αναχώρησης για μια πτήση προς τις Βρυξέλλες. Ακούτε μια ανακοίνωση.",
 "script": [
  L("Υπάλληλος", "f", "Κυρίες και κύριοι, καλησπέρα σας. Η πτήση για Βρυξέλλες είναι υπεράριθμη, δηλαδή έχουν πουληθεί περισσότερα εισιτήρια από τις διαθέσιμες θέσεις. Αναζητούμε τέσσερις επιβάτες που θα ήταν πρόθυμοι να ταξιδέψουν με την επόμενη πτήση, αύριο στις επτά το πρωί.", "Ladies and gentlemen, good evening. The flight to Brussels is overbooked, which means more tickets have been sold than there are seats available. We are looking for four passengers who would be willing to travel on the next flight, tomorrow at seven in the morning."),
  L("Υπάλληλος", "f", "Όσοι δεχτούν θα λάβουν αποζημίωση τριακοσίων ευρώ, καθώς και δωρεάν διανυκτέρευση σε ξενοδοχείο κοντά στο αεροδρόμιο, με δείπνο και πρωινό. Η μεταφορά από και προς το ξενοδοχείο είναι επίσης δωρεάν.", "Those who accept will receive compensation of three hundred euros, as well as a free overnight stay in a hotel near the airport, with dinner and breakfast. Transport to and from the hotel is also free."),
  L("Υπάλληλος", "f", "Οι αποσκευές σας θα παραμείνουν στο αεροδρόμιο και θα ταξιδέψουν μαζί σας αύριο, οπότε κρατήστε μαζί σας ό,τι χρειάζεστε για τη νύχτα. Αν ενδιαφέρεστε, ελάτε στο γκισέ της πύλης πριν ξεκινήσει η επιβίβαση.", "Your luggage will stay at the airport and travel with you tomorrow, so keep with you whatever you need for the night. If you are interested, come to the gate desk before boarding begins."),
 ],
 "questions": [
  Q("Γιατί ζητούν εθελοντές;", ["Γιατί η πτήση ακυρώθηκε", "Γιατί έχουν πουληθεί περισσότερα εισιτήρια από τις διαθέσιμες θέσεις", "Γιατί το αεροπλάνο έχει βλάβη", "Γιατί ο καιρός είναι κακός"], 1, "έχουν πουληθεί περισσότερα εισιτήρια από τις διαθέσιμες θέσεις"),
  Q("Τι θα πάρουν όσοι δεχτούν, εκτός από τα χρήματα;", ["Μια θέση στην πρώτη θέση", "Ένα δωρεάν εισιτήριο για άλλο ταξίδι", "Δωρεάν διανυκτέρευση σε ξενοδοχείο με δείπνο και πρωινό", "Ένα ταξί για το σπίτι τους"], 2, "δωρεάν διανυκτέρευση σε ξενοδοχείο κοντά στο αεροδρόμιο, με δείπνο και πρωινό"),
  Q("Τι θα γίνει με τις αποσκευές τους;", ["Θα παραμείνουν στο αεροδρόμιο και θα ταξιδέψουν μαζί τους αύριο", "Θα σταλούν απόψε στις Βρυξέλλες", "Θα τις πάρουν μαζί στο ξενοδοχείο", "Θα τις παραλάβουν στο σπίτι τους"], 0, "Οι αποσκευές σας θα παραμείνουν στο αεροδρόμιο και θα ταξιδέψουν μαζί σας αύριο"),
 ],
 "gloss": {"πύλη αναχώρησης": "πύλη αναχώρησης — departure gate", "υπεράριθμη": "υπεράριθμος — overbooked", "διαθέσιμες": "διαθέσιμος — available", "πρόθυμοι": "πρόθυμος — willing", "αποζημίωση": "αποζημίωση — compensation", "διανυκτέρευση": "διανυκτέρευση — overnight stay", "αποσκευές": "αποσκευή — (piece of) luggage", "γκισέ": "γκισέ — desk, counter", "επιβίβαση": "επιβίβαση — boarding"}
})

ITEMS.append({
 "id": "l119-vm-vivliothiki-ergaleion", "title": "Μήνυμα από τη βιβλιοθήκη εργαλείων", "title_en": "A message from the tool library", "type": "voicemail", "level": "B2",
 "context_el": "Είστε μέλος μιας δημοτικής «βιβλιοθήκης εργαλείων», που δανείζει εργαλεία αντί για βιβλία. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα σας, ο Στράτος είμαι από τη βιβλιοθήκη εργαλείων του δήμου. Σας τηλεφωνώ για το κρουστικό δράπανο που δανειστήκατε. Έπρεπε να το επιστρέψετε χθες, και το έχει ήδη κλείσει άλλο μέλος για αύριο το πρωί.", "Good morning, this is Stratos from the municipal tool library. I'm calling about the hammer drill you borrowed. You were supposed to return it yesterday, and another member has already booked it for tomorrow morning."),
  L("Υπάλληλος", "m", "Μπορείτε να το φέρετε σήμερα ως τις οκτώ το βράδυ. Αν δεν προλαβαίνετε, υπάρχει και η θυρίδα επιστροφής δίπλα στην είσοδο, που είναι ανοιχτή όλο το εικοσιτετράωρο. Μην ξεχάσετε να βάλετε μέσα στη θήκη και τα τρυπάνια.", "You can bring it today until eight in the evening. If you can't make it, there is also the return box next to the entrance, which is open twenty-four hours a day. Don't forget to put the drill bits in the case too."),
  L("Υπάλληλος", "m", "Και κάτι ακόμα: από τον επόμενο μήνα θα οργανώνουμε κάθε Σάββατο ένα δωρεάν σεμινάριο για αρχάριους, για το πώς χρησιμοποιούμε με ασφάλεια τα ηλεκτρικά εργαλεία. Αν σας ενδιαφέρει, γραφτείτε στην ιστοσελίδα μας.", "And one more thing: from next month we'll be holding a free workshop for beginners every Saturday on how to use power tools safely. If you're interested, sign up on our website."),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί ο Στράτος;", ["Γιατί το δράπανο είναι χαλασμένο", "Γιατί η επιστροφή του δράπανου έχει καθυστερήσει και άλλο μέλος το έχει κλείσει", "Γιατί η βιβλιοθήκη θα κλείσει", "Γιατί η συνδρομή έχει λήξει"], 1, "Έπρεπε να το επιστρέψετε χθες, και το έχει ήδη κλείσει άλλο μέλος για αύριο το πρωί"),
  Q("Τι μπορεί να κάνει ο ακροατής αν δεν προλαβαίνει να το φέρει ως τις οκτώ;", ["Να το αφήσει σε έναν γείτονα", "Να το φέρει την επόμενη εβδομάδα", "Να το αφήσει στη θυρίδα επιστροφής δίπλα στην είσοδο", "Να ζητήσει να το πάρουν από το σπίτι του"], 2, "υπάρχει και η θυρίδα επιστροφής δίπλα στην είσοδο"),
  Q("Τι θα οργανώνει η βιβλιοθήκη από τον επόμενο μήνα;", ["Ένα δωρεάν σεμινάριο για την ασφαλή χρήση ηλεκτρικών εργαλείων", "Μια έκθεση με παλιά εργαλεία", "Πωλήσεις μεταχειρισμένων εργαλείων", "Επισκευές εργαλείων με χαμηλό κόστος"], 0, "ένα δωρεάν σεμινάριο για αρχάριους, για το πώς χρησιμοποιούμε με ασφάλεια τα ηλεκτρικά εργαλεία"),
 ],
 "gloss": {"εργαλείων": "εργαλείο — tool", "δανείζει": "δανείζω — to lend", "κρουστικό δράπανο": "κρουστικό δράπανο — hammer drill", "δανειστήκατε": "δανείζομαι — to borrow", "προλαβαίνετε": "προλαβαίνω — to manage (in time)", "θυρίδα επιστροφής": "θυρίδα επιστροφής — return box, drop slot", "εικοσιτετράωρο": "εικοσιτετράωρο — twenty-four hours", "θήκη": "θήκη — case", "τρυπάνια": "τρυπάνι — drill bit", "αρχάριους": "αρχάριος — beginner"}
})

ITEMS.append({
 "id": "l119-dial-ilektriko-podilato-patera", "title": "Ηλεκτρικό ποδήλατο για τον πατέρα;", "title_en": "An e-bike for Dad?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο αδέρφια, η Ελπίδα και ο Θοδωρής, συζητούν τι δώρο να κάνουν στον πατέρα τους, που κλείνει τα εβδομήντα.",
 "script": [
  L("Ελπίδα", "f", "Θοδωρή, σκέφτηκα για τα εβδομηντάχρονα του μπαμπά να του πάρουμε ένα ηλεκτρικό ποδήλατο. Από τότε που πούλησε το αυτοκίνητο, πηγαίνει παντού με τα πόδια και κουράζεται στην ανηφόρα του σπιτιού.", "Thodoris, I thought that for Dad's seventieth we could get him an e-bike. Ever since he sold the car, he walks everywhere and gets tired on the hill up to the house."),
  L("Θοδωρής", "m", "Δεν ξέρω, Ελπίδα. Ποδήλατο στα εβδομήντα; Κι αν πέσει; Τα ηλεκτρικά πιάνουν και μεγάλη ταχύτητα. Εμένα με ανησυχεί η κίνηση στον κεντρικό δρόμο.", "I don't know, Elpida. A bike at seventy? And what if he falls? E-bikes also reach high speeds. What worries me is the traffic on the main road."),
  L("Ελπίδα", "f", "Ο μπαμπάς ποδηλατούσε σε όλη του τη ζωή, μέχρι πριν από δέκα χρόνια. Και η υποβοήθηση σταματάει στα είκοσι πέντε χιλιόμετρα την ώρα. Υπάρχει άλλωστε ο ποδηλατόδρομος δίπλα στο ποτάμι, δεν χρειάζεται να μπει στον κεντρικό δρόμο.", "Dad cycled all his life, until ten years ago. And the assistance stops at twenty-five kilometres an hour. Besides, there's the cycle path by the river; he doesn't need to go onto the main road."),
  L("Θοδωρής", "m", "Καλά, με έπεισες μισά-μισά. Αλλά να του πάρουμε μαζί και ένα καλό κράνος, και να τον πάμε πρώτα σε ένα κατάστημα να το δοκιμάσει. Δεν θέλω να του κάνουμε ένα δώρο που θα μείνει στην αποθήκη.", "OK, you've half convinced me. But let's get him a good helmet too, and take him to a shop first to try it. I don't want to give him a present that will end up in the storeroom."),
 ],
 "questions": [
  Q("Γιατί η Ελπίδα θέλει να πάρουν ηλεκτρικό ποδήλατο στον πατέρα τους;", ["Γιατί του αρέσουν τα αθλήματα", "Γιατί πούλησε το αυτοκίνητο και κουράζεται στην ανηφόρα του σπιτιού", "Γιατί του το υποσχέθηκαν πέρυσι", "Γιατί ο γιατρός του είπε να γυμνάζεται"], 1, "Από τότε που πούλησε το αυτοκίνητο, πηγαίνει παντού με τα πόδια και κουράζεται στην ανηφόρα του σπιτιού"),
  Q("Τι ανησυχεί κυρίως τον Θοδωρή;", ["Η τιμή του ποδηλάτου", "Ότι ο πατέρας δεν ξέρει ποδήλατο", "Η κίνηση στον κεντρικό δρόμο", "Ότι η μπαταρία θα χαλάσει γρήγορα"], 2, "Εμένα με ανησυχεί η κίνηση στον κεντρικό δρόμο"),
  Q("Τι προτείνει ο Θοδωρής στο τέλος;", ["Να πάρουν και ένα κράνος και να τον πάνε πρώτα να το δοκιμάσει", "Να του πάρουν ένα απλό ποδήλατο", "Να του κάνουν άλλο δώρο", "Να ρωτήσουν πρώτα τη μητέρα τους"], 0, "να του πάρουμε μαζί και ένα καλό κράνος, και να τον πάμε πρώτα σε ένα κατάστημα να το δοκιμάσει"),
 ],
 "gloss": {"εβδομηντάχρονα": "εβδομηντάχρονα — seventieth birthday", "ανηφόρα": "ανηφόρα — uphill slope", "ταχύτητα": "ταχύτητα — speed", "ποδηλατούσε": "ποδηλατώ — to cycle", "υποβοήθηση": "υποβοήθηση — (motor) assistance", "ποδηλατόδρομος": "ποδηλατόδρομος — cycle path", "μισά-μισά": "μισά-μισά — half, partly", "κράνος": "κράνος — helmet", "αποθήκη": "αποθήκη — storeroom"}
})

ITEMS.append({
 "id": "l119-int-xenagiseis-afis", "title": "Ξεναγήσεις αφής για τυφλούς επισκέπτες", "title_en": "Touch tours for blind visitors", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με τη Μυρτώ, αρχαιολόγο σε ένα περιφερειακό μουσείο, που οργανώνει ξεναγήσεις για τυφλούς και άτομα με προβλήματα όρασης.",
 "script": [
  L("Δημοσιογράφος", "m", "Μυρτώ, σε ένα μουσείο συνήθως ακούμε «μην αγγίζετε». Εσείς κάνετε το αντίθετο.", "Myrto, in a museum we usually hear \"do not touch\". You do the opposite."),
  L("Μυρτώ", "f", "Ναι, αλλά όχι με τα πρωτότυπα. Έχουμε φτιάξει πιστά αντίγραφα από γύψο και ρητίνη, στο ίδιο μέγεθος με τα αρχαία. Οι επισκέπτες τα ψηλαφούν με την ησυχία τους, ενώ εγώ περιγράφω τα χρώματα, το φως και τον χώρο όπου βρέθηκαν.", "Yes, but not with the originals. We've made faithful copies in plaster and resin, the same size as the ancient pieces. The visitors feel them at their own pace, while I describe the colours, the light and the place where they were found."),
  L("Δημοσιογράφος", "m", "Τι σας έχει εκπλήξει περισσότερο;", "What has surprised you most?"),
  L("Μυρτώ", "f", "Ότι οι τυφλοί επισκέπτες προσέχουν λεπτομέρειες που εμείς δεν βλέπουμε. Μια κυρία ανακάλυψε με τα δάχτυλά της ένα σημάδι από το εργαλείο του γλύπτη, που δεν το είχαμε προσέξει ποτέ. Από τότε, ζητάω κι από τους βλέποντες συναδέλφους μου να κλείνουν τα μάτια τους πού και πού.", "That blind visitors notice details we don't see. One lady discovered with her fingers a mark left by the sculptor's tool, which we had never noticed. Since then, I've been asking my sighted colleagues to close their eyes now and then too."),
  L("Δημοσιογράφος", "m", "Τι σχέδια έχετε;", "What plans do you have?"),
  L("Μυρτώ", "f", "Ετοιμάζουμε έναν οδηγό σε γραφή μπράιγ και ηχητικές περιγραφές που θα μπορεί κανείς να ακούει από το κινητό του. Θέλουμε ο τυφλός επισκέπτης να μπορεί να έρθει και μόνος του, χωρίς να εξαρτάται από ένα πρόγραμμα ξεναγήσεων.", "We're preparing a guide in Braille and audio descriptions that people will be able to listen to on their phones. We want blind visitors to be able to come on their own too, without depending on a tour schedule."),
 ],
 "questions": [
  Q("Τι αγγίζουν οι επισκέπτες στις ξεναγήσεις της Μυρτώς;", ["Τα πρωτότυπα αρχαία", "Πιστά αντίγραφα από γύψο και ρητίνη", "Μικρά μοντέλα από ξύλο", "Ζωγραφιές με ανάγλυφα χρώματα"], 1, "Έχουμε φτιάξει πιστά αντίγραφα από γύψο και ρητίνη"),
  Q("Τι ανακάλυψε μια τυφλή επισκέπτρια;", ["Ένα σπάσιμο στο άγαλμα", "Μια επιγραφή στη βάση", "Ένα σημάδι από το εργαλείο του γλύπτη", "Ότι το αντίγραφο ήταν μικρότερο"], 2, "ένα σημάδι από το εργαλείο του γλύπτη"),
  Q("Ποιος είναι ο στόχος του νέου οδηγού;", ["Να μπορεί ο τυφλός επισκέπτης να έρθει και μόνος του", "Να αυξηθούν τα έσοδα του μουσείου", "Να αντικαταστήσει τις ξεναγήσεις για όλους", "Να μεταφραστεί σε πολλές γλώσσες"], 0, "Θέλουμε ο τυφλός επισκέπτης να μπορεί να έρθει και μόνος του"),
 ],
 "gloss": {"περιφερειακό": "περιφερειακός — regional", "τυφλούς": "τυφλός — blind", "όρασης": "όραση — sight, vision", "αγγίζετε": "αγγίζω — to touch", "πρωτότυπα": "πρωτότυπο — original", "γύψο": "γύψος — plaster", "ρητίνη": "ρητίνη — resin", "ψηλαφούν": "ψηλαφώ — to feel, touch (to explore)", "γλύπτη": "γλύπτης — sculptor", "βλέποντες": "βλέπων — sighted (person)", "γραφή μπράιγ": "γραφή Μπράιγ — Braille"}
})

ITEMS.append({
 "id": "l119-rep-fanaria-ilikiomenoi", "title": "Περισσότερος χρόνος στα φανάρια για τους ηλικιωμένους", "title_en": "More time at the lights for older pedestrians", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε τοπικό ραδιόφωνο για μια αλλαγή στα φανάρια των πεζών μιας πόλης.",
 "script": [
  L("Ρεπόρτερ", "f", "Πόσος χρόνος χρειάζεται για να διασχίσει κανείς έναν μεγάλο δρόμο; Για έναν νέο άνθρωπο, λίγα δευτερόλεπτα. Για έναν ηλικιωμένο με μπαστούνι, συχνά περισσότερος από όσο δίνει το πράσινο φανάρι. Ο δήμος αποφάσισε να αλλάξει αυτή την κατάσταση σε δέκα διαβάσεις κοντά σε νοσοκομεία, κέντρα υγείας και πλατείες.", "How much time does it take to cross a big road? For a young person, a few seconds. For an older person with a walking stick, often more than the green light allows. The municipality has decided to change this at ten crossings near hospitals, health centres and squares."),
  L("Ρεπόρτερ", "f", "Στις διαβάσεις αυτές τοποθετήθηκαν αισθητήρες που αντιλαμβάνονται αν κάποιος πεζός βρίσκεται ακόμα στη μέση του δρόμου. Σε αυτή την περίπτωση, το πράσινο για τους πεζούς παρατείνεται για λίγα δευτερόλεπτα, ώσπου να φτάσει με ασφάλεια απέναντι.", "Sensors were installed at these crossings that detect whether a pedestrian is still in the middle of the road. In that case, the green for pedestrians is extended by a few seconds until they reach the other side safely."),
  L("Ρεπόρτερ", "f", "Οι οδηγοί αρχικά διαμαρτυρήθηκαν για τις καθυστερήσεις, όμως οι μετρήσεις του πρώτου μήνα έδειξαν ότι ο χρόνος αναμονής για τα αυτοκίνητα αυξήθηκε ελάχιστα. Αν τα αποτελέσματα είναι καλά, ο δήμος σκοπεύει να επεκτείνει το σύστημα σε όλη την πόλη μέσα στα επόμενα δύο χρόνια.", "Drivers initially complained about delays, but measurements from the first month showed that waiting time for cars increased only slightly. If the results are good, the municipality plans to extend the system to the whole city within the next two years."),
 ],
 "questions": [
  Q("Πού έγινε η αλλαγή;", ["Σε όλους τους δρόμους της πόλης", "Σε δέκα διαβάσεις κοντά σε νοσοκομεία, κέντρα υγείας και πλατείες", "Μόνο έξω από σχολεία", "Στον περιφερειακό δρόμο"], 1, "σε δέκα διαβάσεις κοντά σε νοσοκομεία, κέντρα υγείας και πλατείες"),
  Q("Τι κάνουν οι αισθητήρες;", ["Μετρούν πόσα αυτοκίνητα περνούν", "Ειδοποιούν την αστυνομία", "Παρατείνουν το πράσινο αν κάποιος πεζός βρίσκεται ακόμα στη μέση του δρόμου", "Ανάβουν φώτα στο οδόστρωμα"], 2, "το πράσινο για τους πεζούς παρατείνεται για λίγα δευτερόλεπτα"),
  Q("Τι έδειξαν οι μετρήσεις του πρώτου μήνα;", ["Ότι ο χρόνος αναμονής για τα αυτοκίνητα αυξήθηκε ελάχιστα", "Ότι τα ατυχήματα μειώθηκαν στο μισό", "Ότι οι οδηγοί περιμένουν πολύ περισσότερο", "Ότι οι πεζοί δεν χρησιμοποιούν τις διαβάσεις"], 0, "ο χρόνος αναμονής για τα αυτοκίνητα αυξήθηκε ελάχιστα"),
 ],
 "gloss": {"φανάρια": "φανάρι — traffic light", "πεζών": "πεζός — pedestrian", "διασχίσει": "διασχίζω — to cross", "μπαστούνι": "μπαστούνι — walking stick", "διαβάσεις": "διάβαση — (pedestrian) crossing", "αισθητήρες": "αισθητήρας — sensor", "αντιλαμβάνονται": "αντιλαμβάνομαι — to detect, perceive", "παρατείνεται": "παρατείνομαι — to be extended", "διαμαρτυρήθηκαν": "διαμαρτύρομαι — to complain, protest", "επεκτείνει": "επεκτείνω — to extend"}
})

ITEMS.append({
 "id": "l119-rep-tragoudia-chorioy", "title": "Ηχογραφώντας τα παλιά τραγούδια του χωριού", "title_en": "Recording the village's old songs", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα πρόγραμμα σε ένα ορεινό χωριό της Ηπείρου.",
 "script": [
  L("Ρεπόρτερ", "m", "Στο καφενείο του χωριού, ο ογδοντάχρονος κυρ Λευτέρης τραγουδάει ένα μοιρολόι που έμαθε από τη γιαγιά του. Απέναντί του, μια φοιτήτρια μουσικολογίας κρατά ένα μικρόφωνο. Είναι μία από τους έξι νέους που γυρίζουν φέτος τα χωριά της περιοχής για να ηχογραφήσουν τα τραγούδια των ηλικιωμένων πριν χαθούν.", "In the village café, eighty-year-old Lefteris is singing a lament he learned from his grandmother. Opposite him, a musicology student holds a microphone. She is one of six young people going round the villages of the area this year to record the old people's songs before they are lost."),
  L("Ρεπόρτερ", "m", "Πολλά από αυτά τα τραγούδια δεν έχουν γραφτεί ποτέ. Περνούσαν από γενιά σε γενιά προφορικά, στους γάμους, στα πανηγύρια και στις δουλειές του χωραφιού. Οι φοιτητές καταγράφουν και τους στίχους, αλλά και τις ιστορίες που λένε οι τραγουδιστές για το πότε και γιατί τραγουδιόταν κάθε τραγούδι.", "Many of these songs have never been written down. They passed from generation to generation orally, at weddings, at festivals and during work in the fields. The students record the lyrics too, as well as the stories the singers tell about when and why each song was sung."),
  L("Ρεπόρτερ", "m", "Οι ηχογραφήσεις θα είναι ελεύθερα διαθέσιμες σε ένα ψηφιακό αρχείο. Η μεγαλύτερη χαρά όμως, λένε οι φοιτητές, είναι ότι τα παιδιά του χωριού άρχισαν να ζητούν από τους παππούδες τους να τους μάθουν τα τραγούδια.", "The recordings will be freely available in a digital archive. The greatest joy, however, the students say, is that the village children have started asking their grandparents to teach them the songs."),
 ],
 "questions": [
  Q("Τι κάνουν οι έξι νέοι;", ["Δίνουν συναυλίες στα χωριά", "Ηχογραφούν τα τραγούδια των ηλικιωμένων πριν χαθούν", "Διδάσκουν μουσική στα σχολεία", "Γράφουν καινούργια τραγούδια"], 1, "για να ηχογραφήσουν τα τραγούδια των ηλικιωμένων πριν χαθούν"),
  Q("Πώς περνούσαν τα τραγούδια από γενιά σε γενιά;", ["Μέσα από βιβλία", "Μέσα από το ραδιόφωνο", "Προφορικά, στους γάμους, στα πανηγύρια και στις δουλειές", "Στο σχολείο του χωριού"], 2, "Περνούσαν από γενιά σε γενιά προφορικά"),
  Q("Ποια είναι η μεγαλύτερη χαρά των φοιτητών;", ["Ότι τα παιδιά του χωριού ζητούν από τους παππούδες να τους μάθουν τα τραγούδια", "Ότι θα βγάλουν δίσκο", "Ότι το πρόγραμμα θα χρηματοδοτηθεί ξανά", "Ότι έγιναν γνωστοί στην τηλεόραση"], 0, "τα παιδιά του χωριού άρχισαν να ζητούν από τους παππούδες τους να τους μάθουν τα τραγούδια"),
 ],
 "gloss": {"ορεινό": "ορεινός — mountain (adj.)", "μοιρολόι": "μοιρολόι — lament (for the dead)", "μουσικολογίας": "μουσικολογία — musicology", "ηχογραφήσουν": "ηχογραφώ — to record (sound)", "προφορικά": "προφορικά — orally", "πανηγύρια": "πανηγύρι — village festival", "χωραφιού": "χωράφι — field", "στίχους": "στίχος — line (of a song), lyric", "τραγουδιόταν": "τραγουδιέμαι — to be sung", "αρχείο": "αρχείο — archive"}
})

ITEMS.append({
 "id": "l119-mon-alexiptoto-plagias", "title": "Πέταξα με αλεξίπτωτο πλαγιάς", "title_en": "I went paragliding", "type": "monologue", "level": "B2",
 "context_el": "Ο Γιάννης, ένας λογιστής σαράντα πέντε χρονών, διηγείται την πρώτη του πτήση με αλεξίπτωτο πλαγιάς.",
 "script": [
  L("Γιάννης", "m", "Φοβάμαι τα ύψη από παιδί. Γι’ αυτό, όταν η γυναίκα μου μού χάρισε μια πτήση με αλεξίπτωτο πλαγιάς για τα γενέθλιά μου, νόμισα ότι αστειευόταν. Δεν αστειευόταν. Ήταν μια διπλή πτήση, δηλαδή θα πετούσα δεμένος μπροστά από έναν έμπειρο πιλότο.", "I've been afraid of heights since I was a child. So when my wife gave me a paragliding flight for my birthday, I thought she was joking. She wasn't. It was a tandem flight, meaning I'd fly strapped in front of an experienced pilot."),
  L("Γιάννης", "m", "Το χειρότερο ήταν η απογείωση. Ο πιλότος μού είπε να τρέξω προς τον γκρεμό και να μη σταματήσω για κανέναν λόγο. Τα πόδια μου έτρεμαν, αλλά έτρεξα. Και ξαφνικά η γη χάθηκε κάτω από τα πόδια μου και επικράτησε μια απίστευτη ησυχία.", "The worst part was the take-off. The pilot told me to run towards the cliff and not to stop for any reason. My legs were shaking, but I ran. And suddenly the ground disappeared from under my feet and an incredible silence fell."),
  L("Γιάννης", "m", "Πετάξαμε είκοσι λεπτά πάνω από τη θάλασσα. Το περίεργο είναι ότι δεν ένιωσα καθόλου ίλιγγο, ίσως γιατί δεν πατούσα πουθενά. Όταν προσγειωθήκαμε στην παραλία, γέλαγα σαν παιδί. Δεν έγινα ριψοκίνδυνος, αλλά έμαθα ότι ο φόβος δεν είναι πάντα καλός σύμβουλος.", "We flew for twenty minutes over the sea. The strange thing is that I didn't feel dizzy at all, perhaps because I wasn't standing on anything. When we landed on the beach, I was laughing like a child. I didn't become a daredevil, but I learned that fear isn't always a good adviser."),
 ],
 "questions": [
  Q("Τι είδους πτήση ήταν;", ["Μια πτήση μόνος του μετά από μαθήματα", "Μια διπλή πτήση, δεμένος μπροστά από έναν έμπειρο πιλότο", "Μια πτήση με μικρό αεροπλάνο", "Μια πτήση με αερόστατο"], 1, "Ήταν μια διπλή πτήση, δηλαδή θα πετούσα δεμένος μπροστά από έναν έμπειρο πιλότο"),
  Q("Ποιο ήταν για τον Γιάννη το χειρότερο κομμάτι;", ["Η προσγείωση", "Η διαδρομή με το αυτοκίνητο ως το βουνό", "Η απογείωση", "Η αναμονή για καλό καιρό"], 2, "Το χειρότερο ήταν η απογείωση"),
  Q("Τι έμαθε ο Γιάννης από την εμπειρία;", ["Ότι ο φόβος δεν είναι πάντα καλός σύμβουλος", "Ότι θέλει να γίνει πιλότος", "Ότι δεν φοβάται πια τίποτα", "Ότι η γυναίκα του αστειεύεται συχνά"], 0, "έμαθα ότι ο φόβος δεν είναι πάντα καλός σύμβουλος"),
 ],
 "gloss": {"λογιστής": "λογιστής — accountant", "αλεξίπτωτο πλαγιάς": "αλεξίπτωτο πλαγιάς — paraglider", "ύψη": "ύψος — height", "αστειευόταν": "αστειεύομαι — to joke", "δεμένος": "δεμένος — strapped in, tied", "απογείωση": "απογείωση — take-off", "γκρεμό": "γκρεμός — cliff", "έτρεμαν": "τρέμω — to shake, tremble", "ίλιγγο": "ίλιγγος — vertigo, dizziness", "προσγειωθήκαμε": "προσγειώνομαι — to land", "ριψοκίνδυνος": "ριψοκίνδυνος — daredevil, risk-taker"}
})

ITEMS.append({
 "id": "l119-mon-proti-opera-exinta", "title": "Η πρώτη μου όπερα στα εξήντα", "title_en": "My first opera at sixty", "type": "monologue", "level": "B2",
 "context_el": "Η κυρία Σταυρούλα, συνταξιούχος δασκάλα, μιλάει σε μια εκπομπή για την πρώτη φορά που πήγε στην όπερα.",
 "script": [
  L("Σταυρούλα", "f", "Πίστευα πάντα ότι η όπερα είναι για λίγους, για ανθρώπους με γούνες και κιάλια. Η εγγονή μου, που σπουδάζει τραγούδι, επέμενε να με πάει σε μια παράσταση της «Τραβιάτα». Δέχτηκα για να μην τη στενοχωρήσω.", "I always believed that opera was for the few, for people with furs and opera glasses. My granddaughter, who is studying singing, insisted on taking me to a performance of La Traviata. I accepted so as not to upset her."),
  L("Σταυρούλα", "f", "Φοβόμουν ότι δεν θα καταλαβαίνω τίποτα, αφού τραγουδούσαν στα ιταλικά. Όμως πάνω από τη σκηνή υπήρχαν υπότιτλοι στα ελληνικά, και πριν από την παράσταση η εγγονή μου μού είχε διηγηθεί την υπόθεση. Στη δεύτερη πράξη έκλαιγα σαν μικρό παιδί.", "I was afraid I wouldn't understand anything, since they were singing in Italian. But above the stage there were surtitles in Greek, and before the performance my granddaughter had told me the plot. In the second act I was crying like a little child."),
  L("Σταυρούλα", "f", "Από τότε έχω πάει άλλες τέσσερις φορές. Βρήκα και φθηνά εισιτήρια για τις γενικές δοκιμές, που είναι ανοιχτές για συνταξιούχους. Αυτό που κατάλαβα είναι ότι δεν χρειάζεται να ξέρεις από μουσική για να συγκινηθείς. Αρκεί να αφεθείς.", "Since then I've been four more times. I also found cheap tickets for the dress rehearsals, which are open to pensioners. What I realised is that you don't need to know about music to be moved. You just have to let yourself go."),
 ],
 "questions": [
  Q("Γιατί δέχτηκε η κυρία Σταυρούλα να πάει στην όπερα;", ["Γιατί της άρεσε πάντα η όπερα", "Για να μη στενοχωρήσει την εγγονή της", "Γιατί κέρδισε δωρεάν εισιτήρια", "Γιατί το πρότεινε ο γιατρός της"], 1, "Δέχτηκα για να μην τη στενοχωρήσω"),
  Q("Τι τη βοήθησε να καταλάβει την παράσταση;", ["Ένα βιβλίο που διάβασε", "Ότι ξέρει ιταλικά", "Οι υπότιτλοι στα ελληνικά και η υπόθεση που της διηγήθηκε η εγγονή της", "Ένας ξεναγός στο θέατρο"], 2, "πάνω από τη σκηνή υπήρχαν υπότιτλοι στα ελληνικά"),
  Q("Τι κατάλαβε η κυρία Σταυρούλα;", ["Ότι δεν χρειάζεται να ξέρεις από μουσική για να συγκινηθείς", "Ότι η όπερα είναι πολύ ακριβή", "Ότι προτιμά το θέατρο", "Ότι πρέπει να μάθει ιταλικά"], 0, "δεν χρειάζεται να ξέρεις από μουσική για να συγκινηθείς"),
 ],
 "gloss": {"συνταξιούχος": "συνταξιούχος — pensioner, retired", "γούνες": "γούνα — fur (coat)", "κιάλια": "κιάλια — binoculars, opera glasses", "επέμενε": "επιμένω — to insist", "στενοχωρήσω": "στενοχωρώ — to upset", "υπότιτλοι": "υπότιτλος — subtitle, surtitle", "υπόθεση": "υπόθεση — plot", "πράξη": "πράξη — act (of a play)", "γενικές δοκιμές": "γενική δοκιμή — dress rehearsal", "συγκινηθείς": "συγκινούμαι — to be moved", "αφεθείς": "αφήνομαι — to let oneself go"}
})

ITEMS.append({
 "id": "l119-c1-semasiologikos-koresmos", "title": "Όταν μια λέξη χάνει το νόημά της", "title_en": "When a word loses its meaning", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια γλωσσολόγο σε μια ραδιοφωνική εκπομπή για τη γλώσσα και τον εγκέφαλο.",
 "script": [
  L("Γλωσσολόγος", "f", "Κάντε ένα μικρό πείραμα: επαναλάβετε φωναχτά τη λέξη «πορτοκάλι» τριάντα φορές, γρήγορα. Κάπου στη μέση, θα συμβεί κάτι παράξενο. Η λέξη θα αρχίσει να ακούγεται σαν μια σειρά από ήχους χωρίς νόημα, σαν να την ακούτε για πρώτη φορά σε μια ξένη γλώσσα.", "Try a small experiment: repeat the word \"orange\" out loud thirty times, quickly. Somewhere in the middle, something strange will happen. The word will begin to sound like a string of meaningless sounds, as if you were hearing it for the first time in a foreign language."),
  L("Γλωσσολόγος", "f", "Το φαινόμενο ονομάζεται «σημασιολογικός κορεσμός». Τον όρο τον χρησιμοποίησε ο ψυχολόγος Λίον Τζακομπόβιτς Τζέιμς στη διδακτορική του διατριβή, στις αρχές της δεκαετίας του 1960. Η πιο συνηθισμένη εξήγηση είναι ότι, όταν ένα ερέθισμα επαναλαμβάνεται συνεχώς, οι νευρώνες που αντιδρούν σε αυτό «κουράζονται» και ανταποκρίνονται όλο και πιο αδύναμα. Η σύνδεση ανάμεσα στον ήχο και στη σημασία χαλαρώνει προσωρινά.", "The phenomenon is called \"semantic satiation\". The term was used by the psychologist Leon Jakobovits James in his doctoral thesis, in the early 1960s. The most common explanation is that when a stimulus is repeated continuously, the neurons that respond to it get \"tired\" and respond more and more weakly. The connection between the sound and the meaning loosens temporarily."),
  L("Γλωσσολόγος", "f", "Δεν είναι μόνο περιέργεια. Έχει προταθεί ότι η ίδια διαδικασία μπορεί να βοηθήσει ανθρώπους που φοβούνται να προφέρουν ορισμένες λέξεις, για παράδειγμα σε περιπτώσεις τραυλισμού, αφού η επανάληψη αφαιρεί από τη λέξη μέρος του συναισθηματικού της φορτίου. Τα ερευνητικά δεδομένα, πάντως, είναι ακόμη περιορισμένα.", "It isn't just a curiosity. It has been suggested that the same process may help people who are afraid of pronouncing certain words, for example in cases of stuttering, since repetition strips the word of part of its emotional charge. The research evidence, however, is still limited."),
  L("Γλωσσολόγος", "f", "Το φαινόμενο μάς θυμίζει και κάτι βαθύτερο: ότι η σχέση ανάμεσα στη λέξη και στο πράγμα είναι, στην ουσία, αυθαίρετη. Δεν υπάρχει τίποτα «πορτοκαλί» στον ήχο «πορτοκάλι». Το νόημα δεν βρίσκεται μέσα στη λέξη, αλλά μέσα σε εμάς, και γι’ αυτό μπορεί, έστω για λίγα δευτερόλεπτα, να εξαφανιστεί.", "The phenomenon also reminds us of something deeper: that the relationship between the word and the thing is, essentially, arbitrary. There is nothing \"orange\" in the sound \"orange\". Meaning isn't inside the word but inside us, and that's why it can disappear, even if only for a few seconds."),
 ],
 "questions": [
  Q("Τι συμβαίνει όταν επαναλαμβάνουμε μια λέξη πολλές φορές γρήγορα;", ["Τη θυμόμαστε καλύτερα", "Αρχίζει να ακούγεται σαν μια σειρά από ήχους χωρίς νόημα", "Την προφέρουμε πιο σωστά", "Αλλάζει η σημασία της για πάντα"], 1, "Η λέξη θα αρχίσει να ακούγεται σαν μια σειρά από ήχους χωρίς νόημα"),
  Q("Ποια είναι η πιο συνηθισμένη εξήγηση του φαινομένου;", ["Ότι ξεχνάμε τη λέξη", "Ότι η φωνή μας κουράζεται", "Ότι οι νευρώνες που αντιδρούν στο ερέθισμα «κουράζονται» και ανταποκρίνονται πιο αδύναμα", "Ότι ο εγκέφαλος τη μεταφράζει σε άλλη γλώσσα"], 2, "οι νευρώνες που αντιδρούν σε αυτό «κουράζονται» και ανταποκρίνονται όλο και πιο αδύναμα"),
  Q("Πώς παρουσιάζει η γλωσσολόγος τη χρήση του φαινομένου στον τραυλισμό;", ["Ως μια πρόταση με περιορισμένα ακόμη ερευνητικά δεδομένα", "Ως αποδεδειγμένη θεραπεία", "Ως επικίνδυνη πρακτική", "Ως κάτι που χρησιμοποιείται σε όλα τα σχολεία"], 0, "Τα ερευνητικά δεδομένα, πάντως, είναι ακόμη περιορισμένα"),
  Q("Τι δείχνει το φαινόμενο, κατά τη γλωσσολόγο;", ["Ότι οι ξένες γλώσσες είναι δύσκολες", "Ότι πρέπει να αποφεύγουμε την επανάληψη", "Ότι κάποιες λέξεις είναι πιο όμορφες από άλλες", "Ότι η σχέση ανάμεσα στη λέξη και στο πράγμα είναι στην ουσία αυθαίρετη"], 3, "η σχέση ανάμεσα στη λέξη και στο πράγμα είναι, στην ουσία, αυθαίρετη"),
 ],
 "gloss": {"γλωσσολόγο": "γλωσσολόγος — linguist", "σημασιολογικός κορεσμός": "σημασιολογικός κορεσμός — semantic satiation", "διδακτορική": "διδακτορικός — doctoral", "διατριβή": "διατριβή — thesis, dissertation", "ερέθισμα": "ερέθισμα — stimulus", "νευρώνες": "νευρώνας — neuron", "ανταποκρίνονται": "ανταποκρίνομαι — to respond", "χαλαρώνει": "χαλαρώνω — to loosen", "τραυλισμού": "τραυλισμός — stuttering", "φορτίου": "φορτίο — charge, load", "αυθαίρετη": "αυθαίρετος — arbitrary"}
})

ITEMS.append({
 "id": "l119-c1-smyrni-prin-1922", "title": "Η Σμύρνη πριν από το 1922", "title_en": "Smyrna before 1922", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν ιστορικό σε εκπομπή για τον ελληνισμό της Μικράς Ασίας.",
 "script": [
  L("Δημοσιογράφος", "f", "Η Σμύρνη συνδέεται στη μνήμη μας κυρίως με την καταστροφή του 1922. Εσείς επιμένετε να μιλάτε για τη ζωή της πριν από αυτήν.", "Smyrna is linked in our memory mainly with the catastrophe of 1922. You insist on talking about its life before that."),
  L("Ιστορικός", "m", "Γιατί αλλιώς δεν καταλαβαίνουμε τι χάθηκε. Τον 19ο αιώνα η Σμύρνη ήταν ένα από τα μεγαλύτερα λιμάνια της ανατολικής Μεσογείου. Ζούσαν εκεί Έλληνες, Τούρκοι, Αρμένιοι, Εβραίοι και Ευρωπαίοι έμποροι, οι λεγόμενοι Λεβαντίνοι. Η ελληνική κοινότητα ήταν πολυάριθμη και πλούσια, με σχολεία, νοσοκομεία και εφημερίδες. Η πιο γνωστή ίσως ήταν η Ευαγγελική Σχολή, με σημαντική βιβλιοθήκη και μουσείο.", "Because otherwise we don't understand what was lost. In the 19th century Smyrna was one of the largest ports of the eastern Mediterranean. Greeks, Turks, Armenians, Jews and European merchants, the so-called Levantines, lived there. The Greek community was numerous and wealthy, with schools, hospitals and newspapers. Perhaps the best known was the Evangelical School, with an important library and museum."),
  L("Δημοσιογράφος", "f", "Πώς έμοιαζε η καθημερινή ζωή;", "What was daily life like?"),
  L("Ιστορικός", "m", "Η προκυμαία, που χτίστηκε στο δεύτερο μισό του 19ου αιώνα, ήταν γεμάτη καφενεία, θέατρα και ζαχαροπλαστεία. Ένα τραμ που το έσερναν άλογα διέσχιζε την παραλία. Και βέβαια υπήρχε η μουσική: οι κομπανίες με το σαντούρι και το βιολί έπαιζαν τα σμυρναίικα, που αργότερα, με τους πρόσφυγες, επηρέασαν βαθιά το ρεμπέτικο.", "The quay, built in the second half of the 19th century, was full of cafés, theatres and patisseries. A horse-drawn tram ran along the seafront. And of course there was the music: the bands with the santouri and the violin played the Smyrna songs, which later, with the refugees, deeply influenced rebetiko."),
  L("Δημοσιογράφος", "f", "Και τον Σεπτέμβριο του 1922;", "And in September 1922?"),
  L("Ιστορικός", "m", "Μετά την κατάρρευση του μετώπου, ο τουρκικός στρατός μπήκε στην πόλη και λίγες μέρες αργότερα ξέσπασε μια τεράστια πυρκαγιά, που κατέστρεψε κυρίως τις ελληνικές και τις αρμενικές συνοικίες. Χιλιάδες άνθρωποι στριμώχτηκαν στην προκυμαία για να σωθούν. Οι επιζώντες έφεραν μαζί τους στην Ελλάδα τη μουσική, την κουζίνα, ακόμη και ονόματα: η Νέα Σμύρνη στην Αθήνα είναι μια τέτοια ανάμνηση. Η πόλη χάθηκε, αλλά ένα κομμάτι της ζει ακόμη ανάμεσά μας.", "After the collapse of the front, the Turkish army entered the city and a few days later a huge fire broke out, which destroyed mainly the Greek and Armenian quarters. Thousands of people crowded onto the quay to save themselves. The survivors brought with them to Greece their music, their cuisine, even names: Nea Smyrni in Athens is one such memory. The city was lost, but a piece of it still lives among us."),
 ],
 "questions": [
  Q("Γιατί ο ιστορικός επιμένει να μιλά για τη ζωή της Σμύρνης πριν από το 1922;", ["Γιατί η καταστροφή δεν έχει μελετηθεί", "Γιατί αλλιώς δεν καταλαβαίνουμε τι χάθηκε", "Γιατί η πόλη δεν άλλαξε μετά το 1922", "Γιατί γεννήθηκε εκεί"], 1, "Γιατί αλλιώς δεν καταλαβαίνουμε τι χάθηκε"),
  Q("Ποιοι ήταν οι Λεβαντίνοι;", ["Τούρκοι αξιωματούχοι", "Αρμένιοι τεχνίτες", "Ευρωπαίοι έμποροι που ζούσαν στη Σμύρνη", "Μουσικοί από τη Συρία"], 2, "Ευρωπαίοι έμποροι, οι λεγόμενοι Λεβαντίνοι"),
  Q("Τι λέει ο ιστορικός για τα σμυρναίικα;", ["Ότι με τους πρόσφυγες επηρέασαν βαθιά το ρεμπέτικο", "Ότι χάθηκαν μαζί με την πόλη", "Ότι τα έπαιζαν μόνο στις εκκλησίες", "Ότι τα έφεραν στη Σμύρνη οι Ευρωπαίοι"], 0, "επηρέασαν βαθιά το ρεμπέτικο"),
  Q("Ποιο παράδειγμα δίνει για τη μνήμη της πόλης στην Ελλάδα;", ["Ένα μουσείο στη Θεσσαλονίκη", "Τη βιβλιοθήκη της Ευαγγελικής Σχολής", "Ένα τραμ στην Αθήνα", "Το όνομα της Νέας Σμύρνης στην Αθήνα"], 3, "η Νέα Σμύρνη στην Αθήνα είναι μια τέτοια ανάμνηση"),
 ],
 "gloss": {"καταστροφή": "καταστροφή — catastrophe", "λιμάνια": "λιμάνι — port", "Λεβαντίνοι": "Λεβαντίνος — Levantine (European resident of the Ottoman East)", "πολυάριθμη": "πολυάριθμος — numerous", "προκυμαία": "προκυμαία — quay, waterfront", "έσερναν": "σέρνω — to pull, draw", "κομπανίες": "κομπανία — (small) band", "σαντούρι": "σαντούρι — santouri (hammered dulcimer)", "κατάρρευση": "κατάρρευση — collapse", "μετώπου": "μέτωπο — front (military)", "συνοικίες": "συνοικία — quarter, district", "στριμώχτηκαν": "στριμώχνομαι — to crowd, be squeezed", "επιζώντες": "επιζών — survivor"}
})

rnd = random.Random(119)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-119.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
