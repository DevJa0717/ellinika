# Source for library/listening/listening-112.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l112.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l112-ann-delfinia-kolpos", "title": "Δελφίνια στον κόλπο: οδηγίες για τα σκάφη", "title_en": "Dolphins in the bay: instructions for boats", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του λιμεναρχείου στο τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνήτρια", "f", "Το λιμεναρχείο ενημερώνει ότι τις τελευταίες μέρες έχει εμφανιστεί στον κόλπο ένα κοπάδι δελφινιών, με αρκετά μικρά. Οι κυβερνήτες σκαφών και οι οδηγοί ταχύπλοων παρακαλούνται να μειώνουν ταχύτητα όταν τα βλέπουν και να κρατούν απόσταση.", "The port authority informs the public that in recent days a pod of dolphins, with several young, has appeared in the bay. Boat skippers and speedboat drivers are asked to reduce speed when they see them and keep their distance."),
  L("Εκφωνήτρια", "f", "Απαγορεύεται να ακολουθούν τα δελφίνια, να τα περικυκλώνουν ή να περνούν ανάμεσά τους. Οι κολυμβητές δεν πρέπει να προσπαθούν να τα αγγίξουν ή να τα ταΐσουν, γιατί αυτό μπορεί να τα αγχώσει και να τα απομακρύνει από την περιοχή.", "It is forbidden to follow the dolphins, surround them or pass between them. Swimmers should not try to touch or feed them, because this can stress them and drive them away from the area."),
  L("Εκφωνήτρια", "f", "Όποιος δει δελφίνι τραυματισμένο ή μπλεγμένο σε δίχτυα, να ειδοποιήσει αμέσως το λιμεναρχείο. Παρακαλούνται επίσης όσοι τραβούν βίντεο να μην πλησιάζουν περισσότερο για μια καλύτερη λήψη.", "Anyone who sees a dolphin that is injured or caught in nets should notify the port authority immediately. Those filming video are also asked not to approach closer for a better shot."),
 ],
 "questions": [
  Q("Τι ζητείται από τους οδηγούς σκαφών όταν βλέπουν δελφίνια;", ["Να σβήνουν τη μηχανή", "Να μειώνουν ταχύτητα και να κρατούν απόσταση", "Να επιστρέφουν στο λιμάνι", "Να τα φωτογραφίζουν"], 1, "να μειώνουν ταχύτητα όταν τα βλέπουν και να κρατούν απόσταση"),
  Q("Γιατί δεν πρέπει οι κολυμβητές να ταΐζουν τα δελφίνια;", ["Γιατί μπορεί να τους δαγκώσουν", "Γιατί η τροφή δεν τους κάνει καλό", "Γιατί μπορεί να τα αγχώσει και να τα απομακρύνει", "Γιατί υπάρχει πρόστιμο"], 2, "αυτό μπορεί να τα αγχώσει και να τα απομακρύνει από την περιοχή"),
  Q("Τι πρέπει να κάνει όποιος δει δελφίνι μπλεγμένο σε δίχτυα;", ["Να ειδοποιήσει αμέσως το λιμεναρχείο", "Να το ελευθερώσει μόνος του", "Να τραβήξει βίντεο", "Να ειδοποιήσει τους ψαράδες"], 0, "να ειδοποιήσει αμέσως το λιμεναρχείο"),
 ],
 "gloss": {"λιμεναρχείο": "λιμεναρχείο — port authority", "κοπάδι": "κοπάδι — pod, herd, flock", "κυβερνήτες": "κυβερνήτης — skipper, captain", "ταχύπλοων": "ταχύπλοο — speedboat", "περικυκλώνουν": "περικυκλώνω — to surround", "αγχώσει": "αγχώνω — to stress", "δίχτυα": "δίχτυ — (fishing) net", "λήψη": "λήψη — shot (photo, video)"}
})

ITEMS.append({
 "id": "l112-vm-petrelaio-thermansis", "title": "Μήνυμα από τη διαχειρίστρια για το πετρέλαιο θέρμανσης", "title_en": "A message from the building manager about heating oil", "type": "voicemail", "level": "B2",
 "context_el": "Μένετε σε πολυκατοικία. Ακούτε ένα μήνυμα από τη διαχειρίστρια στον τηλεφωνητή.",
 "script": [
  L("Διαχειρίστρια", "f", "Καλησπέρα, κύριε Λαμπράκη, η Σοφία είμαι, η διαχειρίστρια. Σας τηλεφωνώ για το πετρέλαιο θέρμανσης. Η δεξαμενή είναι σχεδόν άδεια, και το πετρέλαιο θα έρθει την Πέμπτη το πρωί. Για να το παραγγείλω, χρειάζομαι από κάθε διαμέρισμα την προκαταβολή μέχρι την Τρίτη.", "Good evening, Mr Lambrakis, it's Sofia, the building manager. I'm calling about the heating oil. The tank is almost empty, and the oil will arrive on Thursday morning. To order it, I need the advance payment from every flat by Tuesday."),
  L("Διαχειρίστρια", "f", "Για το δικό σας διαμέρισμα το ποσό είναι διακόσια σαράντα ευρώ, ανάλογα με τα τετραγωνικά. Μπορείτε να το καταθέσετε στον λογαριασμό της πολυκατοικίας ή να μου το αφήσετε σε φάκελο στο γραμματοκιβώτιο.", "For your flat the amount is two hundred and forty euros, according to the square metres. You can deposit it in the building's account or leave it for me in an envelope in the letterbox."),
  L("Διαχειρίστρια", "f", "Μια ακόμα παράκληση: την Πέμπτη το πρωί μην παρκάρετε μπροστά στην είσοδο, γιατί το βυτιοφόρο πρέπει να πλησιάσει. Αν όλα πάνε καλά, το καλοριφέρ θα ανάψει από το Σάββατο, τρεις ώρες το πρωί και τέσσερις το βράδυ.", "One more request: on Thursday morning don't park in front of the entrance, because the tanker needs to get close. If all goes well, the heating will come on from Saturday, three hours in the morning and four in the evening."),
 ],
 "questions": [
  Q("Τι χρειάζεται η διαχειρίστρια μέχρι την Τρίτη;", ["Τα κλειδιά της αποθήκης", "Την προκαταβολή από κάθε διαμέρισμα", "Μια υπογραφή για τη συνέλευση", "Τον αριθμό του λογαριασμού"], 1, "χρειάζομαι από κάθε διαμέρισμα την προκαταβολή μέχρι την Τρίτη"),
  Q("Από τι εξαρτάται το ποσό για κάθε διαμέρισμα;", ["Από τον όροφο", "Από τον αριθμό των ενοίκων", "Από τα τετραγωνικά", "Από την κατανάλωση της περσινής χρονιάς"], 2, "ανάλογα με τα τετραγωνικά"),
  Q("Γιατί δεν πρέπει να παρκάρει κανείς μπροστά στην είσοδο την Πέμπτη;", ["Γιατί το βυτιοφόρο πρέπει να πλησιάσει", "Γιατί θα βαφτεί η είσοδος", "Γιατί θα γίνει καθαρισμός του δρόμου", "Γιατί έρχεται ο τεχνικός του ανελκυστήρα"], 0, "το βυτιοφόρο πρέπει να πλησιάσει"),
 ],
 "gloss": {"διαχειρίστρια": "διαχειρίστρια — (female) building manager", "πετρέλαιο": "πετρέλαιο θέρμανσης — heating oil", "δεξαμενή": "δεξαμενή — tank", "προκαταβολή": "προκαταβολή — advance payment", "τετραγωνικά": "τετραγωνικά (μέτρα) — square metres", "καταθέσετε": "καταθέτω — to deposit", "βυτιοφόρο": "βυτιοφόρο — tanker (lorry)"}
})

ITEMS.append({
 "id": "l112-dia-antlia-thermotitas", "title": "Αντλία θερμότητας ή καινούργιος καυστήρας;", "title_en": "A heat pump or a new boiler?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά πώς θα ζεσταίνουν το σπίτι τους.",
 "script": [
  L("Άννα", "f", "Ο υδραυλικός είπε ότι ο καυστήρας μας είναι είκοσι πέντε χρονών και δεν αξίζει να τον επισκευάσουμε. Πρέπει να αποφασίσουμε: καινούργιο καυστήρα πετρελαίου ή αντλία θερμότητας;", "The plumber said our boiler is twenty-five years old and isn't worth repairing. We have to decide: a new oil boiler or a heat pump?"),
  L("Θοδωρής", "m", "Η αντλία κοστίζει σχεδόν τα διπλά. Από την άλλη, λειτουργεί με ρεύμα και, απ' ό,τι διάβασα, καταναλώνει πολύ λιγότερη ενέργεια. Αν βάλουμε και φωτοβολταϊκά στην ταράτσα, ο λογαριασμός θα πέσει ακόμα περισσότερο.", "The heat pump costs almost twice as much. On the other hand, it runs on electricity and, from what I've read, uses much less energy. If we also put solar panels on the roof, the bill will drop even further."),
  L("Άννα", "f", "Η ταράτσα όμως είναι κοινή με τους άλλους ενοίκους. Θα πρέπει να το συζητήσουμε στη συνέλευση. Και μην ξεχνάς ότι το σπίτι δεν έχει μόνωση· χωρίς μόνωση, ό,τι κι αν βάλουμε, η ζέστη θα φεύγει από τα παράθυρα.", "But the roof is shared with the other residents. We'll have to discuss it at the meeting. And don't forget the house has no insulation; without insulation, whatever we install, the heat will escape through the windows."),
  L("Θοδωρής", "m", "Σωστό. Ας ζητήσουμε πρώτα προσφορά για τα παράθυρα και ας ρωτήσουμε αν υπάρχει κάποιο πρόγραμμα επιδότησης. Μετά αποφασίζουμε για τη θέρμανση.", "Right. Let's first ask for a quote for the windows and find out if there's a subsidy scheme. Then we'll decide about the heating."),
 ],
 "questions": [
  Q("Γιατί πρέπει να αλλάξουν τον καυστήρα;", ["Γιατί καταναλώνει πολύ ρεύμα", "Γιατί είναι πολύ παλιός και δεν αξίζει επισκευή", "Γιατί το ζήτησαν οι ένοικοι", "Γιατί απαγορεύτηκε το πετρέλαιο"], 1, "δεν αξίζει να τον επισκευάσουμε"),
  Q("Γιατί η Άννα λέει ότι η ταράτσα είναι πρόβλημα;", ["Γιατί είναι πολύ μικρή", "Γιατί δεν έχει ήλιο", "Γιατί είναι κοινή και πρέπει να το συζητήσουν στη συνέλευση", "Γιατί χρειάζεται επισκευή"], 2, "Η ταράτσα όμως είναι κοινή με τους άλλους ενοίκους"),
  Q("Τι αποφασίζουν να κάνουν πρώτα;", ["Να ζητήσουν προσφορά για τα παράθυρα και να ρωτήσουν για επιδότηση", "Να αγοράσουν αντλία θερμότητας", "Να επισκευάσουν τον παλιό καυστήρα", "Να βάλουν φωτοβολταϊκά"], 0, "Ας ζητήσουμε πρώτα προσφορά για τα παράθυρα"),
 ],
 "gloss": {"καυστήρας": "καυστήρας — boiler", "αντλία": "αντλία θερμότητας — heat pump", "καταναλώνει": "καταναλώνω — to consume", "φωτοβολταϊκά": "φωτοβολταϊκά — solar (photovoltaic) panels", "μόνωση": "μόνωση — insulation", "προσφορά": "προσφορά — quote, offer", "επιδότησης": "επιδότηση — subsidy"}
})

ITEMS.append({
 "id": "l112-int-thalassino-gyali", "title": "Κοσμήματα από θαλασσινό γυαλί", "title_en": "Jewellery from sea glass", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γυναίκα που φτιάχνει κοσμήματα σε ένα νησί.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Βλάχου, τι ακριβώς είναι το θαλασσινό γυαλί;", "Ms Vlachou, what exactly is sea glass?"),
  L("Βλάχου", "f", "Είναι κομμάτια από σπασμένα μπουκάλια και βάζα, που η θάλασσα τα γυρίζει πάνω στην άμμο και στα βότσαλα για χρόνια, ώσπου οι αιχμηρές άκρες τους στρογγυλεύουν και η επιφάνεια γίνεται θαμπή, σαν παγωμένη. Ουσιαστικά είναι σκουπίδι που η θάλασσα έκανε στολίδι.", "They're pieces of broken bottles and jars that the sea tumbles over the sand and pebbles for years, until their sharp edges become rounded and the surface turns matt, as if frosted. Essentially it's rubbish that the sea has turned into an ornament."),
  L("Δημοσιογράφος", "m", "Πού τα βρίσκετε;", "Where do you find them?"),
  L("Βλάχου", "f", "Περπατώ κάθε πρωί σε δύο παραλίες, κυρίως μετά από φουρτούνα. Τα πράσινα και τα καφέ είναι τα πιο συνηθισμένα, από μπουκάλια μπίρας και κρασιού. Τα μπλε και τα κόκκινα είναι σπάνια· ένα κόκκινο κομμάτι το βρίσκω ίσως μία φορά τον χρόνο.", "I walk on two beaches every morning, mainly after a storm. Green and brown ones are the most common, from beer and wine bottles. Blue and red ones are rare; I find a red piece maybe once a year."),
  L("Δημοσιογράφος", "m", "Και τι κάνετε με αυτά;", "And what do you do with them?"),
  L("Βλάχου", "f", "Τα τρυπώ με ένα λεπτό τρυπάνι και τα δένω με ασημένιο σύρμα για σκουλαρίκια και μενταγιόν. Δεν τα γυαλίζω ποτέ· η ομορφιά τους είναι ακριβώς ότι τα έφτιαξε ο χρόνος. Και κάθε φορά που κατεβαίνω στην παραλία, μαζεύω και τα πλαστικά που βρίσκω.", "I drill them with a thin drill and bind them with silver wire for earrings and pendants. I never polish them; their beauty is precisely that time made them. And every time I go down to the beach, I also pick up the plastic I find."),
 ],
 "questions": [
  Q("Τι είναι, σύμφωνα με την κ. Βλάχου, το θαλασσινό γυαλί;", ["Ένα είδος πέτρας", "Σπασμένα γυαλιά που η θάλασσα στρογγύλεψε με τα χρόνια", "Γυαλί από ναυάγια", "Ένα υλικό που φτιάχνεται σε εργαστήριο"], 1, "Είναι κομμάτια από σπασμένα μπουκάλια και βάζα"),
  Q("Ποια χρώματα είναι τα πιο σπάνια;", ["Τα πράσινα", "Τα καφέ", "Τα μπλε και τα κόκκινα", "Τα λευκά"], 2, "Τα μπλε και τα κόκκινα είναι σπάνια"),
  Q("Γιατί δεν γυαλίζει ποτέ τα κομμάτια;", ["Γιατί η ομορφιά τους είναι ότι τα έφτιαξε ο χρόνος", "Γιατί δεν έχει τα κατάλληλα εργαλεία", "Γιατί σπάνε εύκολα", "Γιατί οι πελάτες δεν το θέλουν"], 0, "η ομορφιά τους είναι ακριβώς ότι τα έφτιαξε ο χρόνος"),
 ],
 "gloss": {"βότσαλα": "βότσαλο — pebble", "αιχμηρές": "αιχμηρός — sharp", "στρογγυλεύουν": "στρογγυλεύω — to become round", "θαμπή": "θαμπός — matt, dull", "στολίδι": "στολίδι — ornament", "φουρτούνα": "φουρτούνα — storm (at sea)", "τρυπάνι": "τρυπάνι — drill", "μενταγιόν": "μενταγιόν — pendant"}
})

ITEMS.append({
 "id": "l112-rep-orchistra-syntaxiouchon", "title": "Μια ορχήστρα συνταξιούχων", "title_en": "An orchestra of pensioners", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στο ραδιόφωνο για ένα πολιτιστικό πρόγραμμα.",
 "script": [
  L("Ρεπόρτερ", "f", "Κάθε Τετάρτη απόγευμα, στο πολιτιστικό κέντρο του δήμου, σαράντα συνταξιούχοι κουρδίζουν τα όργανά τους. Η ορχήστρα δημιουργήθηκε πριν από τέσσερα χρόνια, και τα περισσότερα μέλη της δεν είχαν παίξει μουσική από τα νεανικά τους χρόνια.", "Every Wednesday afternoon, at the municipal cultural centre, forty pensioners tune their instruments. The orchestra was created four years ago, and most of its members had not played music since their youth."),
  L("Ρεπόρτερ", "f", "Ο μαέστρος, καθηγητής σε ωδείο, διαλέγει κομμάτια που ταιριάζουν στο επίπεδο κάθε ομάδας. Όσοι δεν ήξεραν καθόλου μουσική ξεκίνησαν με κρουστά, ενώ ένας πρώην ναυτικός έμαθε τσέλο στα εβδομήντα δύο του.", "The conductor, a teacher at a conservatory, chooses pieces that suit the level of each group. Those who didn't know any music started with percussion, while a former sailor learned the cello at seventy-two."),
  L("Ρεπόρτερ", "f", "Η ορχήστρα δίνει δύο συναυλίες τον χρόνο, τα Χριστούγεννα και τον Ιούνιο. Τα έσοδα από τα εισιτήρια πηγαίνουν σε μουσικά όργανα για τα σχολεία της περιοχής, ώστε, όπως λένε, να μη χρειαστεί τα σημερινά παιδιά να περιμένουν τη σύνταξη για να παίξουν μουσική.", "The orchestra gives two concerts a year, at Christmas and in June. The ticket income goes on musical instruments for the area's schools, so that, as they say, today's children won't have to wait for retirement to play music."),
 ],
 "questions": [
  Q("Τι ισχύει για τα περισσότερα μέλη της ορχήστρας;", ["Ήταν επαγγελματίες μουσικοί", "Δεν είχαν παίξει μουσική από τα νεανικά τους χρόνια", "Ήταν δάσκαλοι μουσικής", "Δεν έχουν ξαναπαίξει μπροστά σε κοινό"], 1, "τα περισσότερα μέλη της δεν είχαν παίξει μουσική από τα νεανικά τους χρόνια"),
  Q("Με τι ξεκίνησαν όσοι δεν ήξεραν καθόλου μουσική;", ["Με πιάνο", "Με τραγούδι", "Με κρουστά", "Με κιθάρα"], 2, "Όσοι δεν ήξεραν καθόλου μουσική ξεκίνησαν με κρουστά"),
  Q("Πού πηγαίνουν τα έσοδα από τα εισιτήρια;", ["Σε μουσικά όργανα για τα σχολεία της περιοχής", "Στον μισθό του μαέστρου", "Σε ταξίδια της ορχήστρας", "Στο πολιτιστικό κέντρο"], 0, "Τα έσοδα από τα εισιτήρια πηγαίνουν σε μουσικά όργανα για τα σχολεία της περιοχής"),
 ],
 "gloss": {"συνταξιούχοι": "συνταξιούχος — pensioner", "κουρδίζουν": "κουρδίζω — to tune (an instrument)", "μαέστρος": "μαέστρος — conductor", "ωδείο": "ωδείο — conservatory, music school", "κρουστά": "κρουστά — percussion instruments", "τσέλο": "τσέλο — cello", "έσοδα": "έσοδα — income, proceeds"}
})

ITEMS.append({
 "id": "l112-rep-nychta-mouseio-efivoi", "title": "Μια νύχτα στο μουσείο για εφήβους", "title_en": "A night at the museum for teenagers", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για τον πολιτισμό.",
 "script": [
  L("Ρεπόρτερ", "m", "Ένα αρχαιολογικό μουσείο στη Βόρεια Ελλάδα δοκίμασε κάτι ασυνήθιστο: άνοιξε τις αίθουσές του μια Παρασκευή βράδυ μόνο για εφήβους, από τις οχτώ ως τα μεσάνυχτα. Οι εκατόν πενήντα θέσεις γέμισαν μέσα σε δύο μέρες.", "An archaeological museum in northern Greece tried something unusual: it opened its galleries one Friday evening just for teenagers, from eight until midnight. The hundred and fifty places filled up in two days."),
  L("Ρεπόρτερ", "m", "Αντί για ξενάγηση, οι έφηβοι έπαιξαν ένα παιχνίδι μυστηρίου: έπρεπε να βρουν, με βάση γρίφους, ποιο αντικείμενο είχε «κλαπεί» από μια βιτρίνα. Αρχαιολόγοι του μουσείου βοηθούσαν με στοιχεία, χωρίς να δίνουν έτοιμες απαντήσεις.", "Instead of a guided tour, the teenagers played a mystery game: they had to find out, from riddles, which object had been 'stolen' from a display case. The museum's archaeologists helped with clues, without giving ready answers."),
  L("Ρεπόρτερ", "m", "Η βραδιά έκλεισε με συναυλία ενός τοπικού συγκροτήματος στην αυλή. Πολλοί έφηβοι είπαν ότι ήταν η πρώτη φορά που πήγαιναν σε μουσείο χωρίς το σχολείο τους, και το μουσείο σχεδιάζει να επαναλάβει την εκδήλωση κάθε δύο μήνες.", "The evening ended with a concert by a local band in the courtyard. Many teenagers said it was the first time they had been to a museum without their school, and the museum plans to repeat the event every two months."),
 ],
 "questions": [
  Q("Πόσο γρήγορα γέμισαν οι θέσεις;", ["Μέσα σε μία ώρα", "Μέσα σε δύο μέρες", "Μέσα σε μία εβδομάδα", "Δεν γέμισαν όλες"], 1, "Οι εκατόν πενήντα θέσεις γέμισαν μέσα σε δύο μέρες"),
  Q("Τι έκαναν οι έφηβοι αντί για ξενάγηση;", ["Παρακολούθησαν μια ταινία", "Ζωγράφισαν αρχαία αγγεία", "Έπαιξαν ένα παιχνίδι μυστηρίου με γρίφους", "Άκουσαν μια διάλεξη"], 2, "οι έφηβοι έπαιξαν ένα παιχνίδι μυστηρίου"),
  Q("Τι σχεδιάζει το μουσείο;", ["Να επαναλάβει την εκδήλωση κάθε δύο μήνες", "Να ανοίγει κάθε βράδυ", "Να οργανώσει μια συναυλία τον χειμώνα", "Να ανεβάσει την τιμή του εισιτηρίου"], 0, "το μουσείο σχεδιάζει να επαναλάβει την εκδήλωση κάθε δύο μήνες"),
 ],
 "gloss": {"εφήβους": "έφηβος — teenager", "αίθουσές": "αίθουσα — hall, gallery", "ξενάγηση": "ξενάγηση — guided tour", "γρίφους": "γρίφος — riddle", "βιτρίνα": "βιτρίνα — display case", "στοιχεία": "στοιχείο — clue; piece of evidence", "συγκροτήματος": "συγκρότημα — (music) band"}
})

ITEMS.append({
 "id": "l112-mono-poulisa-ta-misa", "title": "Πούλησα τα μισά μου πράγματα", "title_en": "I sold half my things", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλά σε ένα podcast για τον τρόπο ζωής.",
 "script": [
  L("Παύλος", "m", "Πριν από δύο χρόνια μετακόμισα από ένα διαμέρισμα ενενήντα τετραγωνικών σε ένα σαράντα πέντε. Δεν χωρούσαν τα μισά μου πράγματα, οπότε αναγκάστηκα να αποφασίσω τι θα κρατήσω.", "Two years ago I moved from a ninety-square-metre flat to a forty-five. Half my things wouldn't fit, so I was forced to decide what to keep."),
  L("Παύλος", "m", "Ο κανόνας μου ήταν απλός: ό,τι δεν είχα χρησιμοποιήσει τον τελευταίο χρόνο, έφευγε. Πούλησα έπιπλα και ηλεκτρικές συσκευές στο διαδίκτυο, χάρισα ρούχα και έδωσα στη βιβλιοθήκη της γειτονιάς δύο κούτες βιβλία. Το πιο δύσκολο ήταν τα δώρα· ένιωθα ότι πρόδιδα αυτούς που μου τα είχαν κάνει.", "My rule was simple: anything I hadn't used in the last year went. I sold furniture and electrical appliances online, gave away clothes and gave two boxes of books to the neighbourhood library. The hardest part was the gifts; I felt I was betraying the people who had given them to me."),
  L("Παύλος", "m", "Δεν έγινα κανένας ασκητής. Αγοράζω ακόμα πράγματα, αλλά πριν από κάθε αγορά αναρωτιέμαι πού θα το βάλω. Συνήθως η απάντηση είναι «πουθενά», και έτσι γλιτώνω και χρήματα. Το σπίτι καθαρίζεται σε μία ώρα, και δεν έχει τύχει να μου λείψει κάτι από όσα έδωσα.", "I haven't become some kind of ascetic. I still buy things, but before every purchase I ask myself where I'll put it. Usually the answer is 'nowhere', and so I save money too. The flat gets cleaned in an hour, and I haven't once missed anything I gave away."),
 ],
 "questions": [
  Q("Γιατί ο Παύλος αναγκάστηκε να ξεφορτωθεί πράγματα;", ["Γιατί ήθελε χρήματα για ένα ταξίδι", "Γιατί μετακόμισε σε πολύ μικρότερο διαμέρισμα", "Γιατί του το πρότεινε ένας φίλος", "Γιατί χώρισε"], 1, "Δεν χωρούσαν τα μισά μου πράγματα"),
  Q("Τι ήταν το πιο δύσκολο να δώσει;", ["Τα βιβλία", "Τα έπιπλα", "Τα δώρα", "Τα ρούχα"], 2, "Το πιο δύσκολο ήταν τα δώρα"),
  Q("Τι αναρωτιέται σήμερα πριν από κάθε αγορά;", ["Πού θα το βάλει", "Αν είναι σε προσφορά", "Αν θα το χρησιμοποιήσει καθημερινά", "Αν θα αρέσει στους φίλους του"], 0, "αναρωτιέμαι πού θα το βάλω"),
 ],
 "gloss": {"αναγκάστηκα": "αναγκάζομαι — to be forced", "συσκευές": "συσκευή — appliance, device", "χάρισα": "χαρίζω — to give away", "κούτες": "κούτα — (cardboard) box", "πρόδιδα": "προδίδω — to betray", "ασκητής": "ασκητής — ascetic, hermit", "γλιτώνω": "γλιτώνω — to save; escape"}
})

ITEMS.append({
 "id": "l112-mono-protos-xeimonas-sti-thessaloniki", "title": "Ο πρώτος μου χειμώνας στην Ελλάδα", "title_en": "My first winter in Greece", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια Σουηδή που ζει στη Θεσσαλονίκη να μιλά σε μια ραδιοφωνική εκπομπή.",
 "script": [
  L("Κάριν", "f", "Όταν μετακόμισα από τη Στοκχόλμη στη Θεσσαλονίκη, οι φίλοι μου στη Σουηδία με ζήλευαν. «Τέλος το κρύο», μου έλεγαν. Κανείς δεν μου είχε πει ότι τον πρώτο μου χειμώνα εδώ θα κρύωνα περισσότερο από ποτέ.", "When I moved from Stockholm to Thessaloniki, my friends in Sweden envied me. 'No more cold,' they told me. Nobody had told me that in my first winter here I'd be colder than ever."),
  L("Κάριν", "f", "Το πρόβλημα δεν ήταν η θερμοκρασία έξω, αλλά μέσα στα σπίτια. Στη Σουηδία τα σπίτια έχουν χοντρούς τοίχους, τριπλά τζάμια και θέρμανση όλη μέρα. Εδώ, στο πρώτο μου διαμέρισμα, το καλοριφέρ άναβε μόνο λίγες ώρες, και τα πλακάκια στο πάτωμα ήταν παγωμένα.", "The problem wasn't the temperature outside, but inside the houses. In Sweden houses have thick walls, triple glazing and heating all day. Here, in my first flat, the radiator came on for only a few hours, and the floor tiles were freezing."),
  L("Κάριν", "f", "Έμαθα γρήγορα τα ελληνικά κόλπα: παντόφλες και ζακέτα μέσα στο σπίτι και μια κουβέρτα πάντα στον καναπέ. Και κατάλαβα γιατί πολλοί Έλληνες λένε ότι στη Σουηδία δεν κρύωσαν ποτέ: εκεί, απλώς, το κρύο μένει έξω από την πόρτα.", "I quickly learned the Greek tricks: slippers and a cardigan indoors and a blanket always on the sofa. And I understood why many Greeks say they were never cold in Sweden: there, the cold simply stays outside the door."),
 ],
 "questions": [
  Q("Τι της έλεγαν οι φίλοι της στη Σουηδία;", ["Ότι θα της λείψει το χιόνι", "«Τέλος το κρύο»", "Ότι η Θεσσαλονίκη έχει πολλή υγρασία", "Ότι θα γυρίσει σύντομα"], 1, "«Τέλος το κρύο», μου έλεγαν"),
  Q("Πού ήταν, κατά την Κάριν, το πρόβλημα;", ["Στον αέρα του Βαρδάρη", "Στη βροχή", "Μέσα στα σπίτια", "Στα μέσα μεταφοράς"], 2, "Το πρόβλημα δεν ήταν η θερμοκρασία έξω, αλλά μέσα στα σπίτια"),
  Q("Τι έμαθε να κάνει;", ["Να φοράει παντόφλες και ζακέτα μέσα στο σπίτι", "Να αφήνει το καλοριφέρ αναμμένο όλη μέρα", "Να αγοράσει θερμάστρα", "Να περνά τον χειμώνα στη Σουηδία"], 0, "παντόφλες και ζακέτα μέσα στο σπίτι"),
 ],
 "gloss": {"ζήλευαν": "ζηλεύω — to envy", "τζάμια": "τζάμι — (window) pane, glass", "πλακάκια": "πλακάκι — tile", "παγωμένα": "παγωμένος — frozen, freezing", "κόλπα": "κόλπο — trick", "παντόφλες": "παντόφλα — slipper", "ζακέτα": "ζακέτα — cardigan"}
})

ITEMS.append({
 "id": "l112-c1-onomata-anemon", "title": "Τα ονόματα των ανέμων", "title_en": "The names of the winds", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ιστορικό να μιλά σε μια διάλεξη για τη ναυτική παράδοση.",
 "script": [
  L("Ιστορικός", "f", "Για έναν λαό ναυτικών, ο άνεμος δεν ήταν ποτέ απλώς «αέρας». Ήταν σύμμαχος ή εχθρός, και κάθε κατεύθυνσή του είχε το δικό της όνομα. Ήδη οι αρχαίοι Έλληνες μιλούσαν για τον Βορέα, τον Νότο, τον Ζέφυρο και τον Εύρο, και στην Αθήνα σώζεται ακόμη το Ωρολόγιο του Ανδρόνικου Κυρρήστου, οι γνωστοί «Αέρηδες», με οκτώ ανάγλυφες μορφές ανέμων.", "For a people of sailors, the wind was never just 'air'. It was an ally or an enemy, and each direction had its own name. The ancient Greeks already spoke of Boreas, Notos, Zephyros and Euros, and in Athens the Horologion of Andronikos of Kyrrhos still survives, the well-known 'Aerides', with eight carved figures of winds."),
  L("Ιστορικός", "f", "Οι ονομασίες όμως που χρησιμοποιούν μέχρι σήμερα οι Έλληνες ναυτικοί είναι, ως επί το πλείστον, άλλης προέλευσης. Η τραμουντάνα, ο γρέγος, ο λεβάντες, ο σιρόκος, ο πουνέντες και ο μαΐστρος έχουν έρθει από τα ιταλικά, σε μεγάλο βαθμό μέσω των Βενετών, που κυριάρχησαν για αιώνες σε πολλά νησιά. Ο γαρμπής, ο νοτιοδυτικός άνεμος, έχει κατά πάσα πιθανότητα αραβική ρίζα.", "But the names that Greek sailors use to this day are, for the most part, of other origin. Tramontana, gregos, levantes, sirocco, ponente and maistros have come from Italian, largely through the Venetians, who dominated many islands for centuries. Garbis, the south-west wind, most probably has an Arabic root."),
  L("Ιστορικός", "f", "Ο πιο γνωστός άνεμος του Αιγαίου είναι, βέβαια, το μελτέμι: ένας βοριάς ξηρός και συχνά δυνατός, που φυσά κυρίως τους καλοκαιρινούς μήνες. Οι αρχαίοι τον ονόμαζαν «ετησίες», επειδή επέστρεφε κάθε χρόνο την ίδια εποχή. Για τους ναυτικούς ήταν ευλογία, αν ταξίδευαν προς τον νότο, και κατάρα, αν ήθελαν να πάνε βόρεια.", "The best-known wind of the Aegean is, of course, the meltemi: a dry and often strong northerly that blows mainly in the summer months. The ancients called it the 'etesians', because it returned every year at the same season. For sailors it was a blessing if they were travelling south, and a curse if they wanted to go north."),
  L("Ιστορικός", "f", "Τα ονόματα αυτά δεν είναι απλώς απομεινάρια. Δείχνουν πόσο ανοιχτή ήταν πάντα η ελληνική θάλασσα σε άλλους λαούς και γλώσσες. Ένας ψαράς που λέει σήμερα «πιάνει μαΐστρος» μιλά, χωρίς να το ξέρει, μια γλώσσα που διαμορφώθηκε από Βενετούς καπετάνιους, Άραβες εμπόρους και Έλληνες ναυτικούς μαζί.", "These names are not mere relics. They show how open the Greek sea has always been to other peoples and languages. A fisherman who says today 'the maistros is picking up' speaks, without knowing it, a language shaped by Venetian captains, Arab merchants and Greek sailors together."),
 ],
 "questions": [
  Q("Τι απεικονίζει το Ωρολόγιο του Ανδρόνικου Κυρρήστου στην Αθήνα;", ["Τους δώδεκα θεούς", "Οκτώ ανάγλυφες μορφές ανέμων", "Τα ζώδια", "Μια ναυμαχία"], 1, "με οκτώ ανάγλυφες μορφές ανέμων"),
  Q("Από πού προέρχονται οι περισσότερες ονομασίες που χρησιμοποιούν σήμερα οι ναυτικοί;", ["Από τα αρχαία ελληνικά", "Από τα τουρκικά", "Από τα ιταλικά, σε μεγάλο βαθμό μέσω των Βενετών", "Από τα αγγλικά"], 2, "έχουν έρθει από τα ιταλικά, σε μεγάλο βαθμό μέσω των Βενετών"),
  Q("Γιατί οι αρχαίοι ονόμαζαν το μελτέμι «ετησίες»;", ["Επειδή επέστρεφε κάθε χρόνο την ίδια εποχή", "Επειδή φυσούσε όλο τον χρόνο", "Επειδή ήταν πολύ δυνατό", "Επειδή ερχόταν από την Ασία"], 0, "επειδή επέστρεφε κάθε χρόνο την ίδια εποχή"),
  Q("Τι δείχνουν, κατά την ομιλήτρια, τα ονόματα των ανέμων;", ["Ότι οι Έλληνες ναυτικοί δεν είχαν δικές τους λέξεις", "Πόσο ανοιχτή ήταν η ελληνική θάλασσα σε άλλους λαούς και γλώσσες", "Ότι οι Βενετοί ήταν καλύτεροι ναυτικοί", "Ότι οι λέξεις αυτές θα χαθούν σύντομα"], 1, "Δείχνουν πόσο ανοιχτή ήταν πάντα η ελληνική θάλασσα σε άλλους λαούς και γλώσσες"),
 ],
 "gloss": {"σύμμαχος": "σύμμαχος — ally", "ανάγλυφες": "ανάγλυφος — carved in relief", "προέλευσης": "προέλευση — origin", "κυριάρχησαν": "κυριαρχώ — to dominate, rule", "βοριάς": "βοριάς — north wind", "ευλογία": "ευλογία — blessing", "κατάρα": "κατάρα — curse", "απομεινάρια": "απομεινάρι — relic, remnant"}
})

ITEMS.append({
 "id": "l112-c1-anatrichila-mousiki", "title": "Γιατί μας ανατριχιάζει ένα τραγούδι;", "title_en": "Why does a song give us chills?", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν νευροεπιστήμονα σε μια εκπομπή για την επιστήμη.",
 "script": [
  L("Δημοσιογράφος", "f", "Σε πολλούς συμβαίνει να ανατριχιάζουν ακούγοντας ένα συγκεκριμένο σημείο ενός τραγουδιού. Τι γίνεται εκείνη τη στιγμή στον εγκέφαλο;", "Many people get chills when they hear a particular moment in a song. What happens in the brain at that moment?"),
  L("Νευροεπιστήμονας", "m", "Σε μια γνωστή μελέτη του 2011, ερευνητές στον Καναδά ζήτησαν από τους συμμετέχοντες να φέρουν τη μουσική που τους προκαλούσε ανατριχίλα και κατέγραψαν τη δραστηριότητα του εγκεφάλου τους. Διαπίστωσαν ότι στις στιγμές της έντονης συγκίνησης απελευθερωνόταν ντοπαμίνη, η ίδια ουσία που εμπλέκεται στην ευχαρίστηση από το φαγητό ή από άλλες ανταμοιβές.", "In a well-known 2011 study, researchers in Canada asked participants to bring music that gave them chills and recorded their brain activity. They found that at moments of intense emotion dopamine was released, the same substance involved in the pleasure of food or other rewards."),
  L("Δημοσιογράφος", "f", "Δηλαδή η μουσική λειτουργεί σαν μια ανταμοιβή;", "So music works like a reward?"),
  L("Νευροεπιστήμονας", "m", "Κατά κάποιον τρόπο. Το πιο ενδιαφέρον εύρημα ήταν ότι η ντοπαμίνη απελευθερωνόταν και λίγο πριν από την κορύφωση, όσο ο ακροατής την περίμενε. Ο εγκέφαλος προβλέπει συνεχώς τι θα ακολουθήσει. Οι συνθέτες το εκμεταλλεύονται: χτίζουν μια προσδοκία, την καθυστερούν και, τη σωστή στιγμή, την ικανοποιούν ή μας ξαφνιάζουν.", "In a way. The most interesting finding was that dopamine was also released just before the climax, while the listener was anticipating it. The brain constantly predicts what will come next. Composers exploit this: they build up an expectation, delay it and, at the right moment, fulfil it or surprise us."),
  L("Δημοσιογράφος", "f", "Ανατριχιάζουν όλοι με τη μουσική;", "Does everyone get chills from music?"),
  L("Νευροεπιστήμονας", "m", "Όχι. Ένα σημαντικό ποσοστό των ανθρώπων το βιώνει τακτικά, άλλοι σπάνια ή ποτέ, και οι λόγοι δεν είναι ακόμη απολύτως σαφείς. Αυτό δεν σημαίνει ότι οι δεύτεροι απολαμβάνουν λιγότερο τη μουσική. Και κάτι ακόμη: το ίδιο τραγούδι, αν το ακούμε συνέχεια, χάνει σιγά σιγά αυτή τη δύναμη, ακριβώς επειδή δεν μας εκπλήσσει πια.", "No. A significant proportion of people experience it regularly, others rarely or never, and the reasons are not yet entirely clear. That doesn't mean the latter enjoy music less. And one more thing: the same song, if we listen to it all the time, gradually loses this power, precisely because it no longer surprises us."),
 ],
 "questions": [
  Q("Τι διαπίστωσε η μελέτη του 2011;", ["Ότι η μουσική μειώνει τη ντοπαμίνη", "Ότι στις στιγμές έντονης συγκίνησης απελευθερωνόταν ντοπαμίνη", "Ότι μόνο η κλασική μουσική προκαλεί ανατριχίλα", "Ότι η ανατριχίλα είναι αντίδραση στο κρύο"], 1, "στις στιγμές της έντονης συγκίνησης απελευθερωνόταν ντοπαμίνη"),
  Q("Ποιο ήταν το πιο ενδιαφέρον εύρημα, κατά τον νευροεπιστήμονα;", ["Ότι η ντοπαμίνη απελευθερωνόταν μόνο μετά το τραγούδι", "Ότι οι μουσικοί έχουν περισσότερη ντοπαμίνη", "Ότι η ντοπαμίνη απελευθερωνόταν και λίγο πριν από την κορύφωση", "Ότι οι γυναίκες ανατριχιάζουν συχνότερα"], 2, "η ντοπαμίνη απελευθερωνόταν και λίγο πριν από την κορύφωση"),
  Q("Πώς εκμεταλλεύονται οι συνθέτες τη λειτουργία του εγκεφάλου;", ["Χτίζουν μια προσδοκία, την καθυστερούν και την ικανοποιούν ή μας ξαφνιάζουν", "Γράφουν πάντα πολύ γρήγορους ρυθμούς", "Επαναλαμβάνουν την ίδια μελωδία χωρίς αλλαγές", "Χρησιμοποιούν μόνο χαμηλές νότες"], 0, "χτίζουν μια προσδοκία, την καθυστερούν"),
  Q("Γιατί ένα τραγούδι που ακούμε συνέχεια χάνει τη δύναμή του;", ["Γιατί κουράζονται τα αυτιά μας", "Γιατί δεν μας εκπλήσσει πια", "Γιατί αλλάζει η διάθεσή μας", "Γιατί ξεχνάμε τους στίχους"], 1, "ακριβώς επειδή δεν μας εκπλήσσει πια"),
 ],
 "gloss": {"ανατριχιάζουν": "ανατριχιάζω — to get goosebumps, shiver", "ανατριχίλα": "ανατριχίλα — chills, goosebumps", "απελευθερωνόταν": "απελευθερώνομαι — to be released", "εμπλέκεται": "εμπλέκομαι — to be involved", "κορύφωση": "κορύφωση — climax", "προσδοκία": "προσδοκία — expectation", "εκπλήσσει": "εκπλήσσω — to surprise", "βιώνει": "βιώνω — to experience"}
})

rnd = random.Random(112)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-112.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
