# Source for library/listening/listening-184.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l184.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l184-ann-kleisimo-siraggas", "title": "Νυχτερινό κλείσιμο της σήραγγας για συντήρηση", "title_en": "Night closure of the tunnel for maintenance", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση της τροχαίας σε έναν τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνήτρια", "f", "Ανακοίνωση της Τροχαίας. Από τη Δευτέρα και για δύο εβδομάδες, η σήραγγα του Αγίου Νικολάου θα μένει κλειστή κάθε νύχτα από τις έντεκα το βράδυ ως τις πέντε το πρωί. Τα συνεργεία θα αλλάξουν τα φώτα, θα καθαρίσουν τους ανεμιστήρες εξαερισμού και θα ελέγξουν τα συστήματα πυρόσβεσης.", "An announcement from the traffic police. From Monday and for two weeks, the Agios Nikolaos tunnel will stay closed every night from eleven in the evening until five in the morning. The crews will change the lights, clean the ventilation fans and check the fire-fighting systems."),
  L("Εκφωνήτρια", "f", "Τις ώρες αυτές τα αυτοκίνητα θα εκτρέπονται στον παλιό επαρχιακό δρόμο, που περνά πάνω από το βουνό. Η διαδρομή είναι στενή και έχει πολλές στροφές, γι' αυτό τα φορτηγά πάνω από δώδεκα τόνους δεν θα μπορούν να τη χρησιμοποιήσουν· θα πρέπει να περιμένουν στον χώρο στάθμευσης πριν από την είσοδο της σήραγγας.", "During these hours cars will be diverted onto the old provincial road, which goes over the mountain. The route is narrow and has many bends, so lorries over twelve tonnes won't be able to use it; they will have to wait in the car park before the tunnel entrance."),
  L("Εκφωνήτρια", "f", "Τα ασθενοφόρα και τα οχήματα της πυροσβεστικής θα περνούν κανονικά από τη σήραγγα, με τη συνοδεία των συνεργείων. Η Τροχαία ζητά από τους οδηγούς να υπολογίζουν τουλάχιστον είκοσι λεπτά επιπλέον.", "Ambulances and fire-service vehicles will go through the tunnel as normal, escorted by the crews. The traffic police ask drivers to allow at least twenty extra minutes."),
 ],
 "questions": [
  Q("Τι θα κάνουν τα συνεργεία στη σήραγγα;", ["Θα τη διαπλατύνουν", "Θα αλλάξουν τα φώτα, θα καθαρίσουν τους ανεμιστήρες και θα ελέγξουν την πυρόσβεση", "Θα βάψουν τους τοίχους", "Θα στήσουν διόδια"], 1, "Τα συνεργεία θα αλλάξουν τα φώτα, θα καθαρίσουν τους ανεμιστήρες εξαερισμού και θα ελέγξουν τα συστήματα πυρόσβεσης"),
  Q("Τι θα κάνουν τα φορτηγά πάνω από δώδεκα τόνους;", ["Θα πάρουν τον παλιό επαρχιακό δρόμο", "Θα περάσουν από τη σήραγγα με συνοδεία", "Θα περιμένουν στον χώρο στάθμευσης πριν από την είσοδο", "Θα πάνε από την παραλιακή"], 2, "θα πρέπει να περιμένουν στον χώρο στάθμευσης πριν από την είσοδο της σήραγγας"),
  Q("Ποια οχήματα θα περνούν κανονικά από τη σήραγγα;", ["Τα λεωφορεία", "Τα ασθενοφόρα και τα οχήματα της πυροσβεστικής", "Τα ταξί", "Οι μοτοσικλέτες"], 1, "Τα ασθενοφόρα και τα οχήματα της πυροσβεστικής θα περνούν κανονικά από τη σήραγγα"),
 ],
 "gloss": {"σήραγγα": "σήραγγα — tunnel", "Τροχαίας": "Τροχαία — traffic police", "ανεμιστήρες εξαερισμού": "ανεμιστήρας εξαερισμού — ventilation fan", "πυρόσβεσης": "πυρόσβεση — fire-fighting", "εκτρέπονται": "εκτρέπομαι — to be diverted", "επαρχιακό δρόμο": "επαρχιακός δρόμος — provincial road", "στροφές": "στροφή — bend", "συνοδεία": "συνοδεία — escort"},
})

ITEMS.append({
 "id": "l184-int-grafomichanes", "title": "Ο άνθρωπος που επισκευάζει γραφομηχανές", "title_en": "The man who repairs typewriters", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν τεχνίτη που επισκευάζει παλιές γραφομηχανές.",
 "script": [
  L("Δημοσιογράφος", "f", "Ποιος φέρνει σήμερα γραφομηχανή για επισκευή;", "Who brings a typewriter in for repair these days?"),
  L("Τεχνίτης", "m", "Περισσότεροι απ' ό,τι φαντάζεστε. Συγγραφείς που θέλουν να γράφουν χωρίς ειδοποιήσεις και ίντερνετ, νέοι που τη βρήκαν στο πατάρι του παππού, και συλλέκτες. Τα τελευταία χρόνια μάλιστα έχω περισσότερη δουλειά από ποτέ.", "More than you'd imagine. Writers who want to write without notifications and the internet, young people who found one in their grandfather's loft, and collectors. In the last few years I've actually had more work than ever."),
  L("Δημοσιογράφος", "f", "Ποια είναι η πιο συνηθισμένη βλάβη;", "What's the most common fault?"),
  L("Τεχνίτης", "m", "Ο κύλινδρος, το λάστιχο πάνω στο οποίο χτυπούν τα γράμματα. Με τα χρόνια σκληραίνει σαν πέτρα και τα γράμματα βγαίνουν αχνά. Τον ξαναντύνω με καινούργιο λάστιχο. Μετά έρχονται τα πλήκτρα που κολλάνε, συνήθως από σκόνη και παλιό λάδι.", "The platen, the rubber roller the letters strike. Over the years it hardens like stone and the letters come out faint. I re-cover it with new rubber. After that come keys that stick, usually from dust and old oil."),
  L("Δημοσιογράφος", "f", "Και οι μελανοταινίες; Βρίσκονται ακόμα;", "And ribbons? Can you still find them?"),
  L("Τεχνίτης", "m", "Βρίσκονται, αλλά όχι για όλα τα μοντέλα. Γι' αυτό κρατάω τα παλιά καρούλια και τα γεμίζω με καινούργια ταινία. Το πιο δύσκολο πάντως δεν είναι τα ανταλλακτικά. Είναι να πείσω τον πελάτη να μη βάλει λάδι μόνος του.", "Yes, but not for every model. That's why I keep the old spools and fill them with new ribbon. The hardest thing, though, isn't spare parts. It's persuading the customer not to oil it himself."),
 ],
 "questions": [
  Q("Ποιοι φέρνουν σήμερα γραφομηχανές για επισκευή, σύμφωνα με τον τεχνίτη;", ["Μόνο συλλέκτες", "Κυρίως δημόσιες υπηρεσίες", "Συγγραφείς, νέοι που τη βρήκαν στο σπίτι του παππού και συλλέκτες", "Σχεδόν κανείς"], 2, "Συγγραφείς που θέλουν να γράφουν χωρίς ειδοποιήσεις και ίντερνετ"),
  Q("Τι παθαίνει με τα χρόνια ο κύλινδρος;", ["Σκληραίνει και τα γράμματα βγαίνουν αχνά", "Σκουριάζει", "Σπάει στη μέση", "Χάνει το χρώμα του"], 0, "Με τα χρόνια σκληραίνει σαν πέτρα και τα γράμματα βγαίνουν αχνά"),
  Q("Ποιο είναι, κατά τον τεχνίτη, το πιο δύσκολο στη δουλειά του;", ["Να βρει ανταλλακτικά", "Να πείσει τον πελάτη να μη βάλει λάδι μόνος του", "Να γεμίσει τα καρούλια", "Να βρει πελάτες"], 1, "Είναι να πείσω τον πελάτη να μη βάλει λάδι μόνος του"),
 ],
 "gloss": {"γραφομηχανές": "γραφομηχανή — typewriter", "ειδοποιήσεις": "ειδοποίηση — notification", "πατάρι": "πατάρι — loft", "συλλέκτες": "συλλέκτης — collector", "κύλινδρος": "κύλινδρος — platen, roller", "σκληραίνει": "σκληραίνω — to harden", "αχνά": "αχνός — faint", "ξαναντύνω": "ξαναντύνω — to re-cover", "μελανοταινίες": "μελανοταινία — typewriter ribbon", "καρούλια": "καρούλι — spool", "ανταλλακτικά": "ανταλλακτικό — spare part"},
})

ITEMS.append({
 "id": "l184-int-maketes-ploion", "title": "Η κατασκευάστρια μακετών πλοίων", "title_en": "The ship-model maker", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γυναίκα που φτιάχνει μακέτες πλοίων σε ένα εργαστήρι στον Πειραιά.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς ξεκινά μια μακέτα;", "How does a model begin?"),
  L("Κατασκευάστρια", "f", "Από τα σχέδια του πλοίου. Αν το πλοίο υπάρχει ακόμα, ζητάω από την εταιρεία τα αρχικά σχέδια του ναυπηγείου. Αν έχει χαθεί, ψάχνω σε αρχεία και σε παλιές φωτογραφίες. Μετά αποφασίζουμε την κλίμακα. Οι περισσότερες μακέτες μου είναι ένα προς εκατό, δηλαδή ένα εκατοστό για κάθε μέτρο του πλοίου.", "From the ship's plans. If the ship still exists, I ask the company for the shipyard's original plans. If it's been lost, I search archives and old photographs. Then we decide on the scale. Most of my models are one to a hundred, that is one centimetre for every metre of the ship."),
  L("Δημοσιογράφος", "m", "Ποιοι είναι οι πελάτες σας;", "Who are your customers?"),
  L("Κατασκευάστρια", "f", "Ναυτιλιακές εταιρείες που θέλουν το πλοίο τους στη ρεσεψιόν, μουσεία, αλλά και οικογένειες. Πέρυσι μια κυρία μού ζήτησε το καΐκι του πατέρα της, που είχε βουλιάξει πριν από σαράντα χρόνια. Είχε μόνο δύο θολές φωτογραφίες και τις αναμνήσεις της. Όταν της το παρέδωσα, έκλαψε.", "Shipping companies who want their ship in reception, museums, but families too. Last year a lady asked me for her father's caique, which had sunk forty years ago. She had only two blurry photographs and her memories. When I handed it over, she cried."),
  L("Δημοσιογράφος", "m", "Πόσο χρόνο χρειάζεται μια μακέτα;", "How long does a model take?"),
  L("Κατασκευάστρια", "f", "Από δύο μήνες ως έναν χρόνο. Το πιο χρονοβόρο είναι οι μικρές λεπτομέρειες: τα σκοινιά, οι σωσίβιες λέμβοι, τα παραθυράκια. Κάποιες φορές δουλεύω με μεγεθυντικό φακό όλη μέρα.", "From two months to a year. The most time-consuming part is the small details: the ropes, the lifeboats, the little portholes. Sometimes I work with a magnifying glass all day."),
 ],
 "questions": [
  Q("Τι κάνει αν το πλοίο έχει χαθεί;", ["Αρνείται την παραγγελία", "Ψάχνει σε αρχεία και σε παλιές φωτογραφίες", "Ζητά σχέδια από το ναυπηγείο", "Το σχεδιάζει από φαντασία"], 1, "Αν έχει χαθεί, ψάχνω σε αρχεία και σε παλιές φωτογραφίες"),
  Q("Τι σημαίνει κλίμακα «ένα προς εκατό»;", ["Ένα εκατοστό για κάθε μέτρο του πλοίου", "Ένα μέτρο για κάθε εκατό μέτρα", "Εκατό κομμάτια για κάθε μακέτα", "Ένα εκατοστό για κάθε δέκα μέτρα"], 0, "ένα εκατοστό για κάθε μέτρο του πλοίου"),
  Q("Τι είχε η κυρία για το καΐκι του πατέρα της;", ["Τα σχέδια του ναυπηγείου", "Ένα κομμάτι από το καΐκι", "Δύο θολές φωτογραφίες και τις αναμνήσεις της", "Ένα βίντεο"], 2, "Είχε μόνο δύο θολές φωτογραφίες και τις αναμνήσεις της"),
 ],
 "gloss": {"μακέτες": "μακέτα — scale model", "ναυπηγείου": "ναυπηγείο — shipyard", "κλίμακα": "κλίμακα — scale", "Ναυτιλιακές εταιρείες": "ναυτιλιακή εταιρεία — shipping company", "καΐκι": "καΐκι — caique, wooden boat", "βουλιάξει": "βουλιάζω — to sink", "θολές": "θολός — blurry", "χρονοβόρο": "χρονοβόρος — time-consuming", "σωσίβιες λέμβοι": "σωσίβια λέμβος — lifeboat", "μεγεθυντικό φακό": "μεγεθυντικός φακός — magnifying glass"},
})

ITEMS.append({
 "id": "l184-vm-narthikas-vrouxismou", "title": "Μήνυμα για τον νάρθηκα της νύχτας", "title_en": "A message about the night guard", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα από τη γραμματεία ενός οδοντιατρείου στον τηλεφωνητή σας.",
 "script": [
  L("Γραμματέας", "f", "Καλημέρα, κύριε Παπαδάκη, σας τηλεφωνώ από το οδοντιατρείο της κυρίας Ζαφειρίου. Ο νάρθηκας που σας έφτιαξαν για το τρίξιμο των δοντιών ήρθε από το εργαστήριο. Θα πρέπει να περάσετε για δοκιμή, γιατί η γιατρός θέλει να ελέγξει ότι εφαρμόζει σωστά πριν τον πάρετε σπίτι.", "Good morning, Mr Papadakis, I'm calling from Dr Zafeiriou's dental practice. The guard they made you for grinding your teeth has arrived from the lab. You'll need to come in for a fitting, because the doctor wants to check that it fits properly before you take it home."),
  L("Γραμματέας", "f", "Η γιατρός είπε επίσης να μου θυμίσω να σας πω ότι τις πρώτες νύχτες μπορεί να σας φαίνεται άβολος και να τρέχει περισσότερο σάλιο. Είναι φυσιολογικό και περνάει σε μία με δύο εβδομάδες. Τον πλένετε κάθε πρωί με κρύο νερό, όχι ζεστό, γιατί παραμορφώνεται.", "The doctor also asked me to remind you that for the first few nights it may feel uncomfortable and you may produce more saliva. That's normal and passes in one to two weeks. You wash it every morning with cold water, not hot, because it loses its shape."),
  L("Γραμματέας", "f", "Έχουμε ελεύθερο ραντεβού την Τετάρτη στις έξι ή την Παρασκευή στις δέκα το πρωί. Καλέστε μας στο 210 6427 381 να μας πείτε ποιο σας βολεύει.", "We have a free appointment on Wednesday at six or on Friday at ten in the morning. Call us on 210 6427 381 to tell us which suits you."),
 ],
 "questions": [
  Q("Γιατί πρέπει ο κύριος Παπαδάκης να περάσει από το οδοντιατρείο;", ["Για να πληρώσει", "Για να ελέγξει η γιατρός ότι ο νάρθηκας εφαρμόζει σωστά", "Για καθαρισμό δοντιών", "Για ακτινογραφία"], 1, "η γιατρός θέλει να ελέγξει ότι εφαρμόζει σωστά πριν τον πάρετε σπίτι"),
  Q("Τι μπορεί να συμβεί τις πρώτες νύχτες;", ["Να πονάνε τα δόντια", "Να σπάσει ο νάρθηκας", "Να φαίνεται άβολος και να τρέχει περισσότερο σάλιο", "Να μην μπορεί να κοιμηθεί καθόλου"], 2, "τις πρώτες νύχτες μπορεί να σας φαίνεται άβολος και να τρέχει περισσότερο σάλιο"),
  Q("Γιατί πρέπει ο νάρθηκας να πλένεται με κρύο νερό;", ["Γιατί με ζεστό νερό παραμορφώνεται", "Γιατί το ζεστό νερό τον λερώνει", "Για να μη μυρίζει", "Γιατί το λέει ο κατασκευαστής"], 0, "Τον πλένετε κάθε πρωί με κρύο νερό, όχι ζεστό, γιατί παραμορφώνεται"),
 ],
 "gloss": {"οδοντιατρείου": "οδοντιατρείο — dental practice", "νάρθηκας": "νάρθηκας — (dental) guard, splint", "τρίξιμο των δοντιών": "τρίξιμο των δοντιών — teeth grinding", "εργαστήριο": "εργαστήριο — laboratory", "εφαρμόζει": "εφαρμόζω — to fit", "άβολος": "άβολος — uncomfortable", "σάλιο": "σάλιο — saliva", "παραμορφώνεται": "παραμορφώνομαι — to lose its shape, warp"},
})

ITEMS.append({
 "id": "l184-mon-zo-me-emvoes", "title": "Ζω με ένα βουητό στα αυτιά", "title_en": "Living with a ringing in my ears", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλά σε μια εκπομπή υγείας για τις εμβοές που έχει εδώ και χρόνια.",
 "script": [
  L("Αντώνης", "m", "Όλα ξεκίνησαν μετά από μια συναυλία, πριν από δώδεκα χρόνια. Βγήκα έξω και άκουγα ένα σφύριγμα. Σκέφτηκα ότι θα περάσει ως το πρωί. Δεν πέρασε ποτέ. Ο ωτορινολαρυγγολόγος μου εξήγησε ότι λέγεται εμβοές και ότι συχνά συνδέεται με βλάβη της ακοής από τον θόρυβο.", "It all started after a concert, twelve years ago. I came out and could hear a whistling. I thought it would pass by morning. It never did. The ear, nose and throat doctor explained that it's called tinnitus and that it's often linked to hearing damage from noise."),
  L("Αντώνης", "m", "Τους πρώτους μήνες δεν μπορούσα να κοιμηθώ. Μέσα στην ησυχία της νύχτας το σφύριγμα γινόταν τεράστιο. Αυτό που με βοήθησε δεν ήταν κάποιο χάπι, γιατί θεραπεία που να το σταματά δεν υπάρχει. Ήταν ένα μικρό ηχείο δίπλα στο κρεβάτι, που παίζει ήχο βροχής. Ο εγκέφαλος έχει κάτι άλλο να ακούει.", "For the first few months I couldn't sleep. In the quiet of the night the whistling became enormous. What helped me wasn't some pill, because there's no treatment that stops it. It was a small speaker next to the bed that plays the sound of rain. The brain has something else to listen to."),
  L("Αντώνης", "m", "Σήμερα το ακούω μόνο όταν το σκέφτομαι, όπως τώρα που σας μιλάω. Και πάντα έχω στην τσέπη ωτοασπίδες. Στις συναυλίες τις φοράω, ακόμα κι αν οι φίλοι μου γελάνε.", "Today I only hear it when I think about it, like now while I'm talking to you. And I always have earplugs in my pocket. At concerts I wear them, even if my friends laugh."),
 ],
 "questions": [
  Q("Πότε ξεκίνησαν οι εμβοές του Αντώνη;", ["Μετά από ένα κρυολόγημα", "Μετά από μια συναυλία", "Όταν άρχισε να δουλεύει σε εργοτάξιο", "Μετά από ένα ταξίδι με αεροπλάνο"], 1, "Όλα ξεκίνησαν μετά από μια συναυλία"),
  Q("Τι τον βοήθησε να κοιμάται;", ["Ένα χάπι", "Ένα ηχείο που παίζει ήχο βροχής", "Οι ωτοασπίδες", "Μια επέμβαση"], 1, "Ήταν ένα μικρό ηχείο δίπλα στο κρεβάτι, που παίζει ήχο βροχής"),
  Q("Τι κάνει σήμερα στις συναυλίες;", ["Δεν πηγαίνει πια", "Κάθεται μακριά από τα ηχεία", "Φοράει ωτοασπίδες", "Φεύγει νωρίς"], 2, "Στις συναυλίες τις φοράω"),
 ],
 "gloss": {"εμβοές": "εμβοές — tinnitus", "σφύριγμα": "σφύριγμα — whistling", "ωτορινολαρυγγολόγος": "ωτορινολαρυγγολόγος — ear, nose and throat doctor", "βλάβη της ακοής": "βλάβη της ακοής — hearing damage", "ηχείο": "ηχείο — speaker", "ωτοασπίδες": "ωτοασπίδα — earplug"},
})

ITEMS.append({
 "id": "l184-dia-paidia-stin-kideia", "title": "Θα πάρουμε τα παιδιά στην κηδεία;", "title_en": "Shall we take the children to the funeral?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά αν τα παιδιά τους πρέπει να πάνε στην κηδεία του προπάππου τους.",
 "script": [
  L("Ελένη", "f", "Η μάνα μου λέει να μην πάρουμε τα παιδιά αύριο στην κηδεία. Λέει ότι είναι μικρά και θα τρομάξουν.", "My mother says we shouldn't take the children to the funeral tomorrow. She says they're little and they'll be frightened."),
  L("Θοδωρής", "m", "Η Μυρτώ είναι δέκα χρονών, δεν είναι πια μωρό. Και ήταν πολύ δεμένη με τον παππού. Αν δεν την πάμε, φοβάμαι ότι θα νιώσει ότι της κρύψαμε κάτι.", "Myrto's ten, she's not a baby any more. And she was very close to Grandad. If we don't take her, I'm afraid she'll feel we hid something from her."),
  L("Ελένη", "f", "Για τη Μυρτώ συμφωνώ. Ο Στέλιος όμως είναι πέντε. Δεν θα καταλάβει τι γίνεται και θα κουραστεί στην εκκλησία.", "I agree about Myrto. But Stelios is five. He won't understand what's going on and he'll get tired in church."),
  L("Θοδωρής", "m", "Τότε ας τη ρωτήσουμε τη Μυρτώ αν θέλει να έρθει, και να της εξηγήσουμε από πριν τι θα δει. Τον Στέλιο μπορεί να τον κρατήσει η αδερφή μου, και να έρθει μόνο στο σπίτι μετά, που θα μαζευτεί όλη η οικογένεια.", "Then let's ask Myrto if she wants to come, and explain beforehand what she'll see. My sister can look after Stelios, and he can come just to the house afterwards, when the whole family gets together."),
  L("Ελένη", "f", "Καλή ιδέα. Έτσι θα δει κι αυτός ότι ο παππούς είχε τόσους ανθρώπους που τον αγαπούσαν.", "Good idea. That way he'll also see that Grandad had so many people who loved him."),
 ],
 "questions": [
  Q("Γιατί ο Θοδωρής θέλει να πάει η Μυρτώ στην κηδεία;", ["Γιατί το θέλει η γιαγιά", "Γιατί φοβάται ότι θα νιώσει ότι της έκρυψαν κάτι", "Γιατί δεν έχουν πού να την αφήσουν", "Γιατί έχει ξαναπάει σε κηδεία"], 1, "Αν δεν την πάμε, φοβάμαι ότι θα νιώσει ότι της κρύψαμε κάτι"),
  Q("Τι ανησυχεί την Ελένη για τον Στέλιο;", ["Ότι θα κλαίει", "Ότι θα αρρωστήσει", "Ότι δεν θα καταλάβει τι γίνεται και θα κουραστεί", "Ότι θα κάνει φασαρία στο σπίτι"], 2, "Δεν θα καταλάβει τι γίνεται και θα κουραστεί στην εκκλησία"),
  Q("Τι αποφασίζουν τελικά για τον Στέλιο;", ["Θα έρθει μόνο στο σπίτι μετά την κηδεία", "Θα πάει κανονικά στην εκκλησία", "Θα μείνει με τη γιαγιά όλη μέρα", "Δεν θα του πουν τίποτα"], 0, "να έρθει μόνο στο σπίτι μετά"),
 ],
 "gloss": {"κηδεία": "κηδεία — funeral", "προπάππου": "προπάππους — great-grandfather", "τρομάξουν": "τρομάζω — to be frightened", "δεμένη": "δεμένος — close (emotionally), attached", "κρύψαμε": "κρύβω — to hide", "μαζευτεί": "μαζεύομαι — to gather"},
})

ITEMS.append({
 "id": "l184-news-relanti-sxoleia", "title": "Πρόστιμα για τις μηχανές που μένουν αναμμένες έξω από τα σχολεία", "title_en": "Fines for engines left running outside schools", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα δελτίο ειδήσεων σε τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνητής", "m", "Από τον επόμενο μήνα, όσοι οδηγοί περιμένουν έξω από τα σχολεία της πόλης με τη μηχανή αναμμένη θα κινδυνεύουν με πρόστιμο. Το δημοτικό συμβούλιο ενέκρινε χθες την απόφαση, μετά από μετρήσεις που έκαναν μαθητές του δεύτερου γυμνασίου με φορητούς αισθητήρες.", "From next month, drivers who wait outside the town's schools with the engine running will risk a fine. The town council approved the decision yesterday, after measurements made by pupils of the second secondary school with portable sensors."),
  L("Εκφωνητής", "m", "Οι μαθητές κατέγραψαν για έναν μήνα την ποιότητα του αέρα στην πύλη του σχολείου. Βρήκαν ότι τα αιωρούμενα σωματίδια σχεδόν διπλασιάζονταν το μεσημέρι, την ώρα που οι γονείς περίμεναν στο ρελαντί, συχνά με το κλιματιστικό ανοιχτό. Τις ώρες των μαθημάτων οι τιμές έπεφταν ξανά.", "The pupils recorded the air quality at the school gate for a month. They found that particulate matter almost doubled at midday, when parents were waiting with the engine idling, often with the air conditioning on. During lesson hours the values fell again."),
  L("Εκφωνητής", "m", "Τις πρώτες δύο εβδομάδες οι δημοτικοί αστυνομικοί θα κάνουν μόνο συστάσεις. Μετά, το πρόστιμο θα είναι σαράντα ευρώ. Εξαιρούνται τα ταξί που μεταφέρουν μαθητές με αναπηρία και τα οχήματα έκτακτης ανάγκης.", "For the first two weeks the municipal police will only give warnings. After that, the fine will be forty euros. Taxis carrying pupils with disabilities and emergency vehicles are exempt."),
 ],
 "questions": [
  Q("Ποιος έκανε τις μετρήσεις που οδήγησαν στην απόφαση;", ["Το υπουργείο Περιβάλλοντος", "Μαθητές ενός γυμνασίου με φορητούς αισθητήρες", "Οι δημοτικοί αστυνομικοί", "Ένα πανεπιστήμιο"], 1, "μετρήσεις που έκαναν μαθητές του δεύτερου γυμνασίου με φορητούς αισθητήρες"),
  Q("Πότε ήταν χειρότερη η ποιότητα του αέρα στην πύλη;", ["Νωρίς το πρωί", "Τις ώρες των μαθημάτων", "Το μεσημέρι, όταν οι γονείς περίμεναν με τη μηχανή αναμμένη", "Το βράδυ"], 2, "τα αιωρούμενα σωματίδια σχεδόν διπλασιάζονταν το μεσημέρι"),
  Q("Τι θα γίνεται τις πρώτες δύο εβδομάδες;", ["Οι αστυνομικοί θα κάνουν μόνο συστάσεις", "Το πρόστιμο θα είναι διπλό", "Θα κλείσει ο δρόμος", "Θα μοιράζονται φυλλάδια στα παιδιά"], 0, "Τις πρώτες δύο εβδομάδες οι δημοτικοί αστυνομικοί θα κάνουν μόνο συστάσεις"),
 ],
 "gloss": {"πρόστιμο": "πρόστιμο — fine", "ενέκρινε": "εγκρίνω — to approve", "φορητούς αισθητήρες": "φορητός αισθητήρας — portable sensor", "πύλη": "πύλη — gate", "αιωρούμενα σωματίδια": "αιωρούμενα σωματίδια — particulate matter", "ρελαντί": "ρελαντί — idling", "συστάσεις": "σύσταση — warning, recommendation", "Εξαιρούνται": "εξαιρούμαι — to be exempt", "έκτακτης ανάγκης": "έκτακτη ανάγκη — emergency"},
})

ITEMS.append({
 "id": "l184-rep-daneistiki-iatrikon", "title": "Δανείζουμε πατερίτσες και αναπηρικά αμαξίδια", "title_en": "We lend crutches and wheelchairs", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για μια ενορία που δανείζει ιατρικά βοηθήματα.",
 "script": [
  L("Ρεπόρτερ", "f", "Στο υπόγειο της ενορίας, ανάμεσα σε κούτες με ρούχα, υπάρχουν στοιχισμένα δεκάδες αναπηρικά αμαξίδια, πατερίτσες, περιπατητήρες και δύο ηλεκτρικά κρεβάτια. Όλα είναι δωρεές από οικογένειες που δεν τα χρειάζονταν πια, και όλα δανείζονται δωρεάν σε όποιον τα έχει ανάγκη.", "In the parish basement, among boxes of clothes, dozens of wheelchairs, crutches, walking frames and two electric beds stand in rows. All are donations from families who no longer needed them, and all are lent free of charge to anyone who needs them."),
  L("Ρεπόρτερ", "f", "Η ιδέα ήταν μιας συνταξιούχου νοσηλεύτριας, της κυρίας Ευτέρπης. «Έβλεπα ηλικιωμένους που έσπαγαν το πόδι τους και έπρεπε να αγοράσουν περιπατητήρα για έξι εβδομάδες», μας λέει. «Και σε σπίτια όπου είχε πεθάνει κάποιος, τα αμαξίδια κατέληγαν στα σκουπίδια.»", "The idea came from a retired nurse, Mrs Efterpi. 'I saw elderly people who broke their leg and had to buy a walking frame for six weeks,' she tells us. 'And in homes where someone had died, the wheelchairs ended up in the rubbish.'"),
  L("Ρεπόρτερ", "f", "Πριν δοθεί ξανά, κάθε αντικείμενο καθαρίζεται, απολυμαίνεται και ελέγχεται από έναν εθελοντή μηχανικό. Ο δανειζόμενος υπογράφει μόνο ένα χαρτί ότι θα το επιστρέψει όταν δεν το χρειάζεται πια. Μέσα σε δύο χρόνια έχουν γίνει πάνω από τετρακόσιοι δανεισμοί.", "Before it's given out again, every item is cleaned, disinfected and checked by a volunteer engineer. The borrower only signs a paper saying they'll return it when they no longer need it. Within two years there have been over four hundred loans."),
 ],
 "questions": [
  Q("Από πού προέρχονται τα βοηθήματα;", ["Από το νοσοκομείο", "Από δωρεές οικογενειών που δεν τα χρειάζονταν πια", "Από τον δήμο", "Από μια εταιρεία"], 1, "Όλα είναι δωρεές από οικογένειες που δεν τα χρειάζονταν πια"),
  Q("Τι έβλεπε η κυρία Ευτέρπη πριν ξεκινήσει;", ["Ότι τα νοσοκομεία δεν είχαν αμαξίδια", "Ότι οι ηλικιωμένοι δεν έβγαιναν από το σπίτι", "Ηλικιωμένους που αγόραζαν περιπατητήρα για λίγες εβδομάδες και αμαξίδια στα σκουπίδια", "Ότι τα αμαξίδια ήταν πολύ ακριβά για τα νοσοκομεία"], 2, "έπρεπε να αγοράσουν περιπατητήρα για έξι εβδομάδες"),
  Q("Τι πρέπει να κάνει όποιος δανείζεται κάτι;", ["Να υπογράψει ότι θα το επιστρέψει", "Να πληρώσει εγγύηση", "Να φέρει συνταγή γιατρού", "Να γίνει μέλος της ενορίας"], 0, "Ο δανειζόμενος υπογράφει μόνο ένα χαρτί ότι θα το επιστρέψει"),
 ],
 "gloss": {"ενορίας": "ενορία — parish", "στοιχισμένα": "στοιχισμένος — lined up", "αναπηρικά αμαξίδια": "αναπηρικό αμαξίδιο — wheelchair", "πατερίτσες": "πατερίτσα — crutch", "περιπατητήρες": "περιπατητήρας — walking frame", "δωρεές": "δωρεά — donation", "συνταξιούχου": "συνταξιούχος — retired person, pensioner", "απολυμαίνεται": "απολυμαίνω — to disinfect", "δανειζόμενος": "δανειζόμενος — borrower", "δανεισμοί": "δανεισμός — loan"},
})

ITEMS.append({
 "id": "l184-c1-giati-mpagiatevei-to-psomi", "title": "Γιατί μπαγιατεύει το ψωμί", "title_en": "Why bread goes stale", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν χημικό τροφίμων σε μια εκπομπή για τη διατροφή.",
 "script": [
  L("Παρουσιάστρια", "f", "Όλοι νομίζουμε ότι το ψωμί μπαγιατεύει επειδή ξεραίνεται. Ισχύει;", "We all think bread goes stale because it dries out. Is that true?"),
  L("Χημικός", "m", "Μόνο εν μέρει. Η κύρια αιτία βρίσκεται στο άμυλο. Στο ψήσιμο, οι κόκκοι του αμύλου απορροφούν νερό, φουσκώνουν και τα μόριά τους χάνουν την τακτική τους διάταξη· γι' αυτό το φρέσκο ψωμί είναι μαλακό. Καθώς κρυώνει και περνούν οι ώρες, τα μόρια σιγά σιγά ξαναοργανώνονται σε κρυσταλλικές δομές και διώχνουν το νερό από μέσα τους. Το φαινόμενο λέγεται ανασχηματισμός του αμύλου. Η ψίχα σκληραίνει, ακόμα κι αν η συνολική υγρασία δεν έχει αλλάξει πολύ.", "Only partly. The main cause lies in the starch. During baking, the starch granules absorb water, swell, and their molecules lose their orderly arrangement; that's why fresh bread is soft. As it cools and the hours go by, the molecules slowly reorganise into crystalline structures and push the water out of themselves. The phenomenon is called starch retrogradation. The crumb hardens, even if the overall moisture hasn't changed much."),
  L("Παρουσιάστρια", "f", "Άρα το ψυγείο βοηθάει;", "So does the fridge help?"),
  L("Χημικός", "m", "Το αντίθετο. Στις θερμοκρασίες του ψυγείου ο ανασχηματισμός επιταχύνεται, οπότε το ψωμί μπαγιατεύει πιο γρήγορα απ' ό,τι στον πάγκο. Η κατάψυξη, αντίθετα, σχεδόν τον σταματά. Κι αν ζεστάνετε ένα μπαγιάτικο ψωμί στον φούρνο, οι κρύσταλλοι λιώνουν προσωρινά και ξαναμαλακώνει, αρκεί να το φάτε αμέσως.", "The opposite. At fridge temperatures retrogradation speeds up, so bread goes stale faster than on the counter. Freezing, on the other hand, almost stops it. And if you warm a stale loaf in the oven, the crystals melt temporarily and it softens again, as long as you eat it straight away."),
 ],
 "questions": [
  Q("Ποια είναι, κατά τον χημικό, η κύρια αιτία που μπαγιατεύει το ψωμί;", ["Το ότι χάνει όλη του την υγρασία", "Ο ανασχηματισμός του αμύλου σε κρυσταλλικές δομές", "Η δράση της μαγιάς", "Η επαφή με τον αέρα"], 1, "Το φαινόμενο λέγεται ανασχηματισμός του αμύλου"),
  Q("Τι συμβαίνει στο ψωμί μέσα στο ψυγείο;", ["Μπαγιατεύει πιο γρήγορα", "Διατηρείται φρέσκο περισσότερο", "Δεν αλλάζει τίποτα", "Μουχλιάζει αμέσως"], 0, "το ψωμί μπαγιατεύει πιο γρήγορα απ' ό,τι στον πάγκο"),
  Q("Γιατί ξαναμαλακώνει ένα μπαγιάτικο ψωμί στον φούρνο;", ["Γιατί απορροφά υγρασία από τον αέρα", "Γιατί οι κρύσταλλοι λιώνουν προσωρινά", "Γιατί ξαναφουσκώνει η μαγιά", "Γιατί καίγεται η κόρα"], 1, "οι κρύσταλλοι λιώνουν προσωρινά και ξαναμαλακώνει"),
 ],
 "gloss": {"μπαγιατεύει": "μπαγιατεύω — to go stale", "ξεραίνεται": "ξεραίνομαι — to dry out", "άμυλο": "άμυλο — starch", "κόκκοι": "κόκκος — granule", "διάταξη": "διάταξη — arrangement", "κρυσταλλικές δομές": "κρυσταλλική δομή — crystalline structure", "ανασχηματισμός": "ανασχηματισμός — (here) retrogradation, re-formation", "ψίχα": "ψίχα — crumb (inside of bread)", "επιταχύνεται": "επιταχύνομαι — to speed up", "κατάψυξη": "κατάψυξη — freezing, freezer", "μπαγιάτικο": "μπαγιάτικος — stale"},
})

ITEMS.append({
 "id": "l184-c1-giati-glistraei-o-pagos", "title": "Γιατί γλιστράει ο πάγος;", "title_en": "Why is ice slippery?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια φυσικό να μιλά σε μια ραδιοφωνική εκπομπή για την επιστήμη της καθημερινότητας.",
 "script": [
  L("Φυσικός", "f", "Η ερώτηση μοιάζει παιδική, αλλά οι φυσικοί διαφωνούν γι' αυτήν εδώ και πάνω από έναν αιώνα. Η εξήγηση που μάθαμε οι περισσότεροι στο σχολείο είναι ότι η πίεση της λεπίδας του παγοπέδιλου λιώνει τον πάγο από κάτω. Οι υπολογισμοί όμως δείχνουν ότι η πίεση αυτή δεν φτάνει για να λιώσει πάγο σε χαμηλές θερμοκρασίες, και ο πάγος γλιστράει ακόμα και όταν κάνει πολύ κρύο.", "The question sounds childish, but physicists have disagreed about it for over a century. The explanation most of us learned at school is that the pressure of the skate blade melts the ice underneath. But calculations show that this pressure isn't enough to melt ice at low temperatures, and ice is slippery even when it's very cold."),
  L("Φυσικός", "f", "Μια δεύτερη ιδέα είναι ότι η τριβή παράγει θερμότητα, που λιώνει ένα πολύ λεπτό στρώμα νερού κάτω από το παπούτσι ή τη λεπίδα. Αυτό μάλλον παίζει ρόλο όταν κινούμαστε γρήγορα, αλλά δεν εξηγεί γιατί γλιστράμε και όταν απλώς στεκόμαστε.", "A second idea is that friction produces heat, which melts a very thin layer of water under the shoe or the blade. That probably plays a role when we move fast, but it doesn't explain why we slip even when we're just standing."),
  L("Φυσικός", "f", "Γι' αυτό πολλοί ερευνητές σήμερα δίνουν βάρος στην ίδια την επιφάνεια του πάγου. Τα μόρια στην εξωτερική στρώση δεν είναι δεμένα τόσο σφιχτά όσο στο εσωτερικό, και συμπεριφέρονται σαν ένα στρώμα σχεδόν υγρό, πάχους λίγων μορίων. Το πιθανότερο είναι ότι και οι τρεις μηχανισμοί συμβάλλουν, ο καθένας σε διαφορετικές συνθήκες. Η συζήτηση πάντως δεν έχει κλείσει.", "That's why many researchers today put weight on the surface of the ice itself. The molecules in the outer layer aren't bound as tightly as in the interior, and they behave like an almost liquid layer a few molecules thick. Most likely all three mechanisms contribute, each in different conditions. The debate, however, isn't closed."),
 ],
 "questions": [
  Q("Γιατί η εξήγηση με την πίεση της λεπίδας δεν αρκεί;", ["Γιατί η πίεση δεν φτάνει για να λιώσει πάγο σε χαμηλές θερμοκρασίες", "Γιατί τα παγοπέδιλα είναι πολύ ελαφριά", "Γιατί ο πάγος δεν λιώνει ποτέ", "Γιατί δεν έχει μετρηθεί ποτέ"], 0, "η πίεση αυτή δεν φτάνει για να λιώσει πάγο σε χαμηλές θερμοκρασίες"),
  Q("Τι δεν εξηγεί η θεωρία της τριβής;", ["Γιατί γλιστράμε πιο πολύ όταν τρέχουμε", "Γιατί γλιστράμε και όταν απλώς στεκόμαστε", "Γιατί ο πάγος είναι διάφανος", "Γιατί λιώνει ο πάγος στον ήλιο"], 1, "δεν εξηγεί γιατί γλιστράμε και όταν απλώς στεκόμαστε"),
  Q("Ποιο είναι το συμπέρασμα της φυσικού;", ["Ότι η εξήγηση του σχολείου είναι σωστή", "Ότι μόνο η επιφάνεια του πάγου μετράει", "Ότι πιθανότατα συμβάλλουν και οι τρεις μηχανισμοί και η συζήτηση δεν έχει κλείσει", "Ότι το ζήτημα λύθηκε οριστικά"], 2, "Το πιθανότερο είναι ότι και οι τρεις μηχανισμοί συμβάλλουν"),
 ],
 "gloss": {"γλιστράει": "γλιστράω — to be slippery, slip", "λεπίδας": "λεπίδα — blade", "παγοπέδιλου": "παγοπέδιλο — ice skate", "τριβή": "τριβή — friction", "στρώμα": "στρώμα — layer", "επιφάνεια": "επιφάνεια — surface", "στρώση": "στρώση — layer, coat", "σφιχτά": "σφιχτά — tightly", "μηχανισμοί": "μηχανισμός — mechanism", "συμβάλλουν": "συμβάλλω — to contribute"},
})

rnd = random.Random(184)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-184.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
