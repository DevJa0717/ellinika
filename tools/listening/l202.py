# Source for library/listening/listening-202.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l202.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l202-ann-thyrides-dematon", "title": "Οι αυτόματες θυρίδες δεμάτων μετακομίζουν", "title_en": "The parcel lockers are moving", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός εμπορικού κέντρου.",
 "script": [
  L("Εκφωνητής", "m", "Αγαπητοί επισκέπτες, σας ενημερώνουμε ότι από τη Δευτέρα οι αυτόματες θυρίδες παραλαβής δεμάτων μεταφέρονται από την είσοδο του ισογείου στο πρώτο υπόγειο, δίπλα στο πάρκινγκ. Η μεταφορά θα γίνει το Σαββατοκύριακο, οπότε το Σάββατο και την Κυριακή οι θυρίδες δεν θα λειτουργούν.", "Dear visitors, we inform you that from Monday the automatic parcel lockers are moving from the ground-floor entrance to the first basement level, next to the car park. The move will take place at the weekend, so on Saturday and Sunday the lockers will not be working."),
  L("Εκφωνητής", "m", "Όσοι περιμένετε δέμα αυτές τις μέρες, μην ανησυχείτε: τα δέματα που δεν θα παραληφθούν θα φυλάσσονται με ασφάλεια και θα σας περιμένουν στη νέα θέση. Ο κωδικός παραλαβής που λάβατε με μήνυμα στο κινητό σας παραμένει ο ίδιος, και η προθεσμία παραλαβής παρατείνεται κατά δύο ημέρες.", "Those of you expecting a parcel in these days, don't worry: parcels that aren't collected will be kept safely and will be waiting for you in the new location. The collection code you received by text message stays the same, and the collection deadline is extended by two days."),
  L("Εκφωνητής", "m", "Για άτομα με κινητικές δυσκολίες, το προσωπικό του γραφείου πληροφοριών μπορεί να σας φέρει το δέμα σας στο ισόγειο. Ευχαριστούμε για την κατανόηση.", "For people with mobility difficulties, the information desk staff can bring your parcel to you on the ground floor. Thank you for your understanding."),
 ],
 "questions": [
  Q("Πού θα βρίσκονται οι θυρίδες από τη Δευτέρα;", ["Στην είσοδο του ισογείου", "Στο πρώτο υπόγειο, δίπλα στο πάρκινγκ", "Στον δεύτερο όροφο", "Στο γραφείο πληροφοριών"], 1, "στο πρώτο υπόγειο, δίπλα στο πάρκινγκ"),
  Q("Τι ισχύει για τον κωδικό παραλαβής;", ["Θα σταλεί νέος", "Παραμένει ο ίδιος", "Ισχύει μόνο το Σάββατο", "Πρέπει να ζητηθεί στο γραφείο"], 1, "παραμένει ο ίδιος"),
  Q("Τι μπορεί να κάνει το προσωπικό για άτομα με κινητικές δυσκολίες;", ["Να στείλει το δέμα στο σπίτι", "Να φέρει το δέμα στο ισόγειο", "Να επιστρέψει τα χρήματα", "Να κρατήσει θέση στο πάρκινγκ"], 1, "μπορεί να σας φέρει το δέμα σας στο ισόγειο"),
 ],
 "gloss": {"θυρίδες": "θυρίδα — locker, compartment", "δεμάτων": "δέμα — parcel", "υπόγειο": "υπόγειο — basement", "προθεσμία": "προθεσμία — deadline", "παρατείνεται": "παρατείνομαι — to be extended", "κινητικές": "κινητικός — mobility (adj.), motor"},
})
ITEMS.append({
 "id": "l202-rep-rhtinosyllektes", "title": "Οι τελευταίοι ρητινοσυλλέκτες", "title_en": "The last resin tappers in the pine forest", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ραδιοφωνικό ρεπορτάζ από ένα πευκοδάσος.",
 "script": [
  L("Ρεπόρτερ", "f", "Είναι επτά το πρωί και ο κύριος Στέλιος περπατάει ανάμεσα στα πεύκα με ένα μικρό κοφτερό εργαλείο στο χέρι. Σε κάθε δέντρο ανανεώνει μια επιμήκη τομή στον κορμό, και από κάτω κρέμεται ένα μικρό δοχείο, όπου στάζει αργά το ρετσίνι. Η δουλειά του λέγεται ρητινοσυλλογή, και είναι μια από τις παλιότερες ασχολίες της ελληνικής υπαίθρου.", "It is seven in the morning and Mr Stelios is walking among the pines with a small sharp tool in his hand. On each tree he renews an elongated cut in the trunk, and below it hangs a small container into which the resin slowly drips. His work is called resin tapping, and it is one of the oldest occupations of the Greek countryside."),
  L("Ρεπόρτερ", "f", "Το ρετσίνι χρησιμοποιείται στη ρετσίνα, αλλά και για την παραγωγή νέφτι, βερνικιών και άλλων προϊόντων. Πριν από μερικές δεκαετίες η Ελλάδα ήταν από τους σημαντικούς παραγωγούς στην Ευρώπη, όμως σήμερα οι ρητινοσυλλέκτες είναι λίγοι. Η δουλειά είναι κουραστική, πληρώνεται με το κιλό, και η τιμή επηρεάζεται από το φτηνότερο ρετσίνι που εισάγεται από άλλες χώρες.", "Resin is used in retsina, but also to produce turpentine, varnishes and other products. A few decades ago Greece was among the significant producers in Europe, but today resin tappers are few. The work is tiring, it is paid by the kilo, and the price is affected by cheaper resin imported from other countries."),
  L("Ρεπόρτερ", "f", "Ο κύριος Στέλιος λέει ότι οι ρητινοσυλλέκτες είναι και φύλακες του δάσους: περνούν κάθε μέρα από τα ίδια μονοπάτια, καθαρίζουν τα ξερά κλαδιά και είναι συχνά οι πρώτοι που θα δουν καπνό. «Όταν φύγουμε εμείς», μου λέει, «το δάσος θα μείνει πιο μόνο του.»", "Mr Stelios says that resin tappers are also guardians of the forest: they walk the same paths every day, clear away dry branches and are often the first to see smoke. 'When we're gone,' he tells me, 'the forest will be more alone.'"),
 ],
 "questions": [
  Q("Τι κάνει ο κύριος Στέλιος σε κάθε δέντρο;", ["Το κλαδεύει", "Ανανεώνει μια τομή στον κορμό", "Το ποτίζει", "Το μετράει"], 1, "ανανεώνει μια επιμήκη τομή στον κορμό"),
  Q("Γιατί είναι χαμηλή η τιμή του ρετσινιού;", ["Γιατί δεν το χρειάζεται κανείς", "Λόγω του φτηνότερου ρετσινιού που εισάγεται", "Γιατί είναι κακής ποιότητας", "Γιατί το κράτος ορίζει την τιμή"], 1, "η τιμή επηρεάζεται από το φτηνότερο ρετσίνι που εισάγεται από άλλες χώρες"),
  Q("Γιατί οι ρητινοσυλλέκτες λέγονται «φύλακες του δάσους»;", ["Γιατί είναι δασοφύλακες", "Γιατί περνούν κάθε μέρα και συχνά βλέπουν πρώτοι καπνό", "Γιατί φυτεύουν δέντρα", "Γιατί κυνηγούν λαθροκυνηγούς"], 1, "είναι συχνά οι πρώτοι που θα δουν καπνό"),
 ],
 "gloss": {"πευκοδάσος": "πευκοδάσος — pine forest", "επιμήκη": "επιμήκης — elongated", "τομή": "τομή — cut, incision", "κορμό": "κορμός — trunk", "στάζει": "στάζω — to drip", "ρετσίνι": "ρετσίνι — resin", "νέφτι": "νέφτι — turpentine", "βερνικιών": "βερνίκι — varnish", "φύλακες": "φύλακας — guardian, keeper"},
})
ITEMS.append({
 "id": "l202-dia-menou-qr", "title": "Ο κατάλογος με τον κωδικό QR", "title_en": "The menu that is only a QR code", "type": "dialogue", "level": "B2",
 "context_el": "Ένας πατέρας και η κόρη του κάθονται σε ένα καινούργιο εστιατόριο.",
 "script": [
  L("Πατέρας", "m", "Πού είναι ο κατάλογος; Ο σερβιτόρος μάς έφερε μόνο νερό κι αυτό το χαρτάκι με το τετράγωνο σχέδιο.", "Where's the menu? The waiter brought us only water and this little card with the square pattern."),
  L("Κόρη", "f", "Αυτός είναι ο κατάλογος, μπαμπά. Είναι κωδικός QR. Τον σκανάρεις με την κάμερα του κινητού και ανοίγει σε μια σελίδα με όλα τα πιάτα.", "That is the menu, Dad. It's a QR code. You scan it with your phone camera and it opens a page with all the dishes."),
  L("Πατέρας", "m", "Δοκίμασα, αλλά τα γράμματα είναι μικροσκοπικά και τα γυαλιά μου τα άφησα στο αυτοκίνητο. Και η μπαταρία μου είναι στο οκτώ τοις εκατό. Δεν θέλω να διαβάζω το φαγητό μου σε μια οθόνη.", "I tried, but the letters are tiny and I left my glasses in the car. And my battery is at eight per cent. I don't want to read my food off a screen."),
  L("Κόρη", "f", "Έχεις δίκιο, δεν είναι βολικό για όλους. Ας ρωτήσουμε αν έχουν και έντυπο. Πολλά μαγαζιά κρατάνε μερικούς καταλόγους σε χαρτί ακριβώς γι' αυτόν τον λόγο.", "You're right, it isn't convenient for everyone. Let's ask if they have a printed one too. Many places keep a few paper menus for exactly that reason."),
  L("Πατέρας", "m", "Κι αν δεν έχουν, θα μου τα διαβάσεις εσύ, όπως σου διάβαζα εγώ παραμύθια όταν ήσουν μικρή.", "And if they don't, you'll read them out to me, the way I used to read you fairy tales when you were little."),
 ],
 "questions": [
  Q("Γιατί δυσκολεύεται ο πατέρας να διαβάσει τον κατάλογο;", ["Γιατί είναι σε ξένη γλώσσα", "Γιατί τα γράμματα είναι μικροσκοπικά και δεν έχει τα γυαλιά του", "Γιατί το εστιατόριο είναι σκοτεινό", "Γιατί δεν ξέρει να διαβάζει"], 1, "τα γράμματα είναι μικροσκοπικά και τα γυαλιά μου τα άφησα στο αυτοκίνητο"),
  Q("Τι προτείνει η κόρη;", ["Να φύγουν", "Να ρωτήσουν αν υπάρχει έντυπος κατάλογος", "Να φορτίσουν το κινητό", "Να παραγγείλουν ό,τι και οι διπλανοί"], 1, "Ας ρωτήσουμε αν έχουν και έντυπο"),
  Q("Τι θα κάνει η κόρη αν δεν υπάρχει χάρτινος κατάλογος;", ["Θα παραγγείλει για εκείνον", "Θα του διαβάσει τα πιάτα", "Θα φέρει τα γυαλιά του", "Θα παραπονεθεί"], 1, "θα μου τα διαβάσεις εσύ"),
 ],
 "gloss": {"κατάλογος": "κατάλογος — menu", "σκανάρεις": "σκανάρω — to scan", "μικροσκοπικά": "μικροσκοπικός — tiny", "βολικό": "βολικός — convenient", "έντυπο": "έντυπος — printed", "παραμύθια": "παραμύθι — fairy tale"},
})
ITEMS.append({
 "id": "l202-vm-pagetos-lemonies", "title": "Μήνυμα για τον παγετό απόψε", "title_en": "A neighbour's warning about frost tonight", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον γείτονά σας στο χωριό.",
 "script": [
  L("Γείτονας", "m", "Γεια σου, Μαρίνα, ο Θανάσης είμαι, από το διπλανό κτήμα. Άκουσα στο δελτίο ότι απόψε η θερμοκρασία θα πέσει κάτω από το μηδέν, και ξέρω ότι φύτεψες φέτος τις καινούργιες λεμονιές. Οι νεαρές λεμονιές δεν αντέχουν καθόλου τον παγετό, μπορεί να καούν τα φύλλα τους μέσα σε μία νύχτα.", "Hi, Marina, it's Thanasis, from the next-door field. I heard on the forecast that tonight the temperature will drop below zero, and I know you planted the new lemon trees this year. Young lemon trees can't stand frost at all; their leaves can get burnt in a single night."),
  L("Γείτονας", "m", "Αν δεν προλαβαίνεις να έρθεις, μπορώ να τις σκεπάσω εγώ με το ειδικό ύφασμα που έχω στην αποθήκη. Μη χρησιμοποιήσεις νάιλον, γιατί ακουμπάει στα φύλλα και κάνει περισσότερο κακό. Και πότισέ τες λίγο το απόγευμα, γιατί το υγρό χώμα κρατάει καλύτερα τη ζέστη από το ξερό.", "If you can't make it here in time, I can cover them myself with the special fabric I have in the shed. Don't use plastic sheeting, because it touches the leaves and does more harm. And water them a little in the afternoon, because moist soil holds heat better than dry soil."),
  L("Γείτονας", "m", "Πάρε με μέχρι τις έξι να μου πεις τι θέλεις να κάνω. Γεια.", "Call me by six to tell me what you'd like me to do. Bye."),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί ο Θανάσης;", ["Για να ζητήσει λεμόνια", "Γιατί απόψε θα έχει παγετό και κινδυνεύουν οι λεμονιές", "Γιατί χάλασε η αποθήκη", "Για να πουλήσει το κτήμα"], 1, "απόψε η θερμοκρασία θα πέσει κάτω από το μηδέν"),
  Q("Γιατί δεν πρέπει να χρησιμοποιήσει νάιλον;", ["Γιατί είναι ακριβό", "Γιατί ακουμπάει στα φύλλα και κάνει περισσότερο κακό", "Γιατί το παίρνει ο αέρας", "Γιατί απαγορεύεται"], 1, "ακουμπάει στα φύλλα και κάνει περισσότερο κακό"),
  Q("Γιατί προτείνει πότισμα το απόγευμα;", ["Γιατί δεν έβρεξε", "Γιατί το υγρό χώμα κρατάει καλύτερα τη ζέστη", "Για να μεγαλώσουν τα λεμόνια", "Για να μη μπουν έντομα"], 1, "το υγρό χώμα κρατάει καλύτερα τη ζέστη από το ξερό"),
 ],
 "gloss": {"κτήμα": "κτήμα — field, estate", "λεμονιές": "λεμονιά — lemon tree", "παγετό": "παγετός — frost", "σκεπάσω": "σκεπάζω — to cover", "ύφασμα": "ύφασμα — fabric", "νάιλον": "νάιλον — plastic sheeting, nylon", "χώμα": "χώμα — soil"},
})
ITEMS.append({
 "id": "l202-news-katavothra", "title": "Καταβόθρα άνοιξε σε κεντρικό δρόμο", "title_en": "A sinkhole opens in a main street", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση από τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνήτρια", "f", "Μια καταβόθρα διαμέτρου περίπου τριών μέτρων άνοιξε τα ξημερώματα σε κεντρικό δρόμο της πόλης, μετά τις έντονες βροχοπτώσεις των τελευταίων ημερών. Ένα σταθμευμένο αυτοκίνητο έγειρε, καθώς ο μπροστινός του τροχός βούλιαξε στο άνοιγμα. Ευτυχώς δεν υπήρξαν τραυματισμοί, αφού εκείνη την ώρα ο δρόμος ήταν σχεδόν άδειος.", "A sinkhole about three metres in diameter opened in the early hours in a main street of the town, after the heavy rainfall of the last few days. A parked car tilted as its front wheel sank into the opening. Fortunately there were no injuries, since the street was almost empty at that hour."),
  L("Εκφωνήτρια", "f", "Σύμφωνα με τους πρώτους ελέγχους των τεχνικών υπηρεσιών του δήμου, η αιτία φαίνεται να είναι ένας παλιός αγωγός ομβρίων που έσπασε και παρέσυρε σιγά σιγά το χώμα κάτω από την άσφαλτο. Ο δρόμος παραμένει κλειστός και η κυκλοφορία έχει εκτραπεί σε παράλληλες οδούς.", "According to the first checks by the municipality's technical services, the cause appears to be an old storm-water pipe that broke and gradually washed away the soil beneath the asphalt. The street remains closed and traffic has been diverted to parallel roads."),
  L("Εκφωνήτρια", "f", "Ο δήμος ανακοίνωσε ότι θα ελέγξει με κάμερα όλο το δίκτυο της περιοχής, για να διαπιστωθεί αν υπάρχουν κι άλλα σημεία με παρόμοιο πρόβλημα.", "The municipality announced that it will inspect the whole network in the area with a camera, to establish whether there are other spots with a similar problem."),
 ],
 "questions": [
  Q("Τι έπαθε το σταθμευμένο αυτοκίνητο;", ["Κάηκε", "Έγειρε, γιατί ο τροχός του βούλιαξε", "Παρασύρθηκε από το νερό", "Τίποτα"], 1, "ο μπροστινός του τροχός βούλιαξε στο άνοιγμα"),
  Q("Ποια φαίνεται να είναι η αιτία;", ["Ένας σεισμός", "Ένας παλιός αγωγός ομβρίων που έσπασε", "Έργα του μετρό", "Ένα βαρύ φορτηγό"], 1, "ένας παλιός αγωγός ομβρίων που έσπασε"),
  Q("Τι θα κάνει ο δήμος;", ["Θα κλείσει τον δρόμο για έναν χρόνο", "Θα ελέγξει με κάμερα όλο το δίκτυο της περιοχής", "Θα αποζημιώσει τους οδηγούς", "Θα φυτέψει δέντρα"], 1, "θα ελέγξει με κάμερα όλο το δίκτυο της περιοχής"),
 ],
 "gloss": {"καταβόθρα": "καταβόθρα — sinkhole", "διαμέτρου": "διάμετρος — diameter", "έγειρε": "γέρνω — to tilt, lean", "βούλιαξε": "βουλιάζω — to sink", "αγωγός": "αγωγός — pipe, conduit", "ομβρίων": "όμβρια — rainwater, storm water", "εκτραπεί": "εκτρέπω — to divert"},
})
ITEMS.append({
 "id": "l202-int-fysito-gyali", "title": "Η τεχνίτρια του φυσητού γυαλιού", "title_en": "A glassblower at her furnace", "type": "interview", "level": "B2",
 "context_el": "Συνέντευξη με μια τεχνίτρια που φτιάχνει αντικείμενα από φυσητό γυαλί στο εργαστήριό της.",
 "script": [
  L("Δημοσιογράφος", "m", "Εδώ μέσα κάνει πολλή ζέστη. Πόσο ζεστός είναι ο φούρνος σας;", "It's very hot in here. How hot is your furnace?"),
  L("Τεχνίτρια", "f", "Πάνω από χίλιους βαθμούς. Το γυαλί εκεί μέσα γίνεται σαν παχύ μέλι. Με ένα μακρύ μεταλλικό σωλήνα παίρνω μια μπάλα λιωμένο γυαλί, φυσάω από την άλλη άκρη και σχηματίζεται μια φούσκα. Μετά τη γυρίζω συνεχώς και τη διαμορφώνω με ξύλινα εργαλεία και βρεγμένες εφημερίδες.", "Over a thousand degrees. The glass in there becomes like thick honey. With a long metal pipe I gather a ball of molten glass, blow from the other end and a bubble forms. Then I keep turning it and shape it with wooden tools and wet newspapers."),
  L("Δημοσιογράφος", "m", "Εφημερίδες; Δεν καίγονται;", "Newspapers? Don't they burn?"),
  L("Τεχνίτρια", "f", "Αν είναι καλά βρεγμένες, όχι αμέσως. Δημιουργούν ένα στρώμα ατμού ανάμεσα στο χέρι μου και στο γυαλί. Το πιο δύσκολο όμως δεν είναι το φύσημα, είναι η υπομονή. Όταν τελειώσει ένα κομμάτι, το βάζω σε έναν δεύτερο φούρνο, όπου κρυώνει πολύ αργά, μέσα σε μια ολόκληρη νύχτα. Αν κρυώσει απότομα, ραγίζει, ακόμα και μέρες αργότερα.", "If they're well soaked, not straight away. They create a layer of steam between my hand and the glass. The hardest part, though, isn't the blowing, it's the patience. When a piece is finished, I put it in a second oven, where it cools very slowly, over a whole night. If it cools suddenly, it cracks, even days later."),
  L("Δημοσιογράφος", "m", "Σας έχει τύχει να σπάσει κάτι που αγαπούσατε;", "Has something you loved ever broken on you?"),
  L("Τεχνίτρια", "f", "Πολλές φορές. Στην αρχή έκλαιγα. Τώρα κρατάω τα κομμάτια και τα ξαναλιώνω. Το γυαλί σού δίνει πάντα δεύτερη ευκαιρία.", "Many times. At first I used to cry. Now I keep the pieces and melt them down again. Glass always gives you a second chance."),
 ],
 "questions": [
  Q("Σε τι μοιάζει το γυαλί μέσα στον φούρνο;", ["Σε νερό", "Σε παχύ μέλι", "Σε άμμο", "Σε πηλό"], 1, "Το γυαλί εκεί μέσα γίνεται σαν παχύ μέλι"),
  Q("Γιατί χρησιμοποιεί βρεγμένες εφημερίδες;", ["Για να καθαρίσει το γυαλί", "Γιατί δημιουργούν στρώμα ατμού ανάμεσα στο χέρι και στο γυαλί", "Για να τυλίξει τα κομμάτια", "Για να ανάψει τον φούρνο"], 1, "Δημιουργούν ένα στρώμα ατμού ανάμεσα στο χέρι μου και στο γυαλί"),
  Q("Τι γίνεται αν ένα κομμάτι κρυώσει απότομα;", ["Γίνεται πιο ανθεκτικό", "Αλλάζει χρώμα", "Ραγίζει, ακόμα και μέρες αργότερα", "Τίποτα"], 2, "Αν κρυώσει απότομα, ραγίζει, ακόμα και μέρες αργότερα"),
 ],
 "gloss": {"φυσητό": "φυσητός — blown (glass)", "λιωμένο": "λιωμένος — molten, melted", "φούσκα": "φούσκα — bubble", "διαμορφώνω": "διαμορφώνω — to shape", "ατμού": "ατμός — steam", "ραγίζει": "ραγίζω — to crack", "ξαναλιώνω": "ξαναλιώνω — to melt down again"},
})
ITEMS.append({
 "id": "l202-mono-donti-sti-stegi", "title": "Το δόντι στα κεραμίδια", "title_en": "Throwing the baby tooth onto the roof", "type": "monologue", "level": "B2",
 "context_el": "Μια μητέρα μιλάει σε ένα podcast για γονείς.",
 "script": [
  L("Μητέρα", "f", "Χθες βράδυ ο γιος μου έχασε το πρώτο του δόντι. Είχε ακούσει από ένα αμερικανικό κινούμενο σχέδιο για τη νεράιδα των δοντιών, που παίρνει το δόντι κάτω από το μαξιλάρι και αφήνει ένα κέρμα. Ήθελε οπωσδήποτε να το βάλει κάτω από το μαξιλάρι του.", "Last night my son lost his first tooth. He had heard from an American cartoon about the tooth fairy, who takes the tooth from under the pillow and leaves a coin. He absolutely wanted to put it under his pillow."),
  L("Μητέρα", "f", "Εγώ όμως μεγάλωσα αλλιώς. Η γιαγιά μου μάς έβαζε να πετάμε το δόντι πάνω στα κεραμίδια και να λέμε κάτι σαν «Κοράκι, κοράκι, πάρε το δόντι μου και δώσ' μου ένα σιδερένιο». Σε κάθε περιοχή η φράση αλλάζει λίγο, αλλά η ιδέα είναι η ίδια: δίνεις το παλιό δόντι σε ένα πουλί για να σου φέρει ένα γερό.", "But I grew up differently. My grandmother used to have us throw the tooth onto the roof tiles and say something like 'Crow, crow, take my tooth and give me an iron one'. The phrase varies a little from region to region, but the idea is the same: you give the old tooth to a bird so it will bring you a strong one."),
  L("Μητέρα", "f", "Τελικά κάναμε και τα δύο. Πετάξαμε το δόντι στη σκεπή της αποθήκης, είπαμε το ποιηματάκι, και το πρωί βρήκε ένα κέρμα κάτω από το μαξιλάρι. Μου είπε ότι το κοράκι μάλλον το έφερε. Ίσως έτσι γεννιούνται οι νέες παραδόσεις.", "In the end we did both. We threw the tooth onto the roof of the shed, said the little rhyme, and in the morning he found a coin under his pillow. He told me the crow had probably brought it. Perhaps that's how new traditions are born."),
 ],
 "questions": [
  Q("Πού ήθελε ο γιος να βάλει το δόντι του;", ["Σε ένα κουτί", "Κάτω από το μαξιλάρι του", "Στα κεραμίδια", "Στον κήπο"], 1, "Ήθελε οπωσδήποτε να το βάλει κάτω από το μαξιλάρι του"),
  Q("Ποια είναι η ιδέα του εθίμου της γιαγιάς;", ["Να θάβεις το δόντι", "Να δίνεις το παλιό δόντι σε ένα πουλί για να σου φέρει ένα γερό", "Να κρατάς το δόντι για τύχη", "Να το δίνεις στον οδοντίατρο"], 1, "δίνεις το παλιό δόντι σε ένα πουλί για να σου φέρει ένα γερό"),
  Q("Τι έκαναν τελικά;", ["Μόνο το αμερικανικό έθιμο", "Μόνο το έθιμο της γιαγιάς", "Και τα δύο", "Τίποτα από τα δύο"], 2, "Τελικά κάναμε και τα δύο"),
 ],
 "gloss": {"νεράιδα": "νεράιδα — fairy", "μαξιλάρι": "μαξιλάρι — pillow", "κέρμα": "κέρμα — coin", "κεραμίδια": "κεραμίδι — roof tile", "κοράκι": "κοράκι — crow", "σιδερένιο": "σιδερένιος — iron (adj.)", "σκεπή": "σκεπή — roof"},
})
ITEMS.append({
 "id": "l202-rep-meteorologika-mpalonia", "title": "Τα μπαλόνια των μετεωρολόγων", "title_en": "Weather balloons launched twice a day", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από έναν μετεωρολογικό σταθμό.",
 "script": [
  L("Ρεπόρτερ", "m", "Λίγο πριν από τις δύο το μεσημέρι, ώρα Ελλάδας, ένας μετεωρολόγος βγαίνει στην αυλή του σταθμού κρατώντας ένα μεγάλο λευκό μπαλόνι γεμάτο αέριο. Από κάτω κρέμεται ένα μικρό κουτί, όχι μεγαλύτερο από ένα πακέτο γάλα. Είναι μια ραδιοβολίδα, ένα όργανο που μετράει τη θερμοκρασία, την υγρασία και την πίεση καθώς ανεβαίνει.", "Shortly before two in the afternoon, Greek time, a meteorologist steps out into the station's yard holding a large white balloon filled with gas. Below it hangs a small box, no bigger than a carton of milk. It is a radiosonde, an instrument that measures temperature, humidity and pressure as it rises."),
  L("Ρεπόρτερ", "m", "Τέτοιες εκτοξεύσεις γίνονται σε εκατοντάδες σταθμούς σε όλο τον κόσμο, συνήθως δύο φορές την ημέρα και στις ίδιες ώρες παντού, ώστε τα δεδομένα να μπορούν να συγκριθούν. Το όργανο στέλνει τις μετρήσεις του με ραδιοκύματα, και από τη θέση του, που παρακολουθείται με GPS, υπολογίζεται και η ταχύτητα του ανέμου σε κάθε ύψος.", "Such launches take place at hundreds of stations around the world, usually twice a day and at the same times everywhere, so that the data can be compared. The instrument sends its measurements by radio waves, and from its position, tracked by GPS, the wind speed at each altitude is also calculated."),
  L("Ρεπόρτερ", "m", "Όσο ανεβαίνει, η πίεση γύρω του πέφτει και το μπαλόνι φουσκώνει, ώσπου, συχνά πάνω από τα είκοσι χιλιόμετρα, σκάει. Το κουτί πέφτει με ένα μικρό αλεξίπτωτο και σπάνια βρίσκεται. Οι μετρήσεις του όμως έχουν ήδη μπει στα μοντέλα που προβλέπουν τον καιρό της επόμενης εβδομάδας.", "As it rises, the pressure around it falls and the balloon expands, until, often above twenty kilometres, it bursts. The box falls with a small parachute and is rarely found. But its measurements have already gone into the models that forecast the coming week's weather."),
 ],
 "questions": [
  Q("Τι μετράει η ραδιοβολίδα;", ["Μόνο τη βροχή", "Θερμοκρασία, υγρασία και πίεση", "Τη ρύπανση", "Τους σεισμούς"], 1, "μετράει τη θερμοκρασία, την υγρασία και την πίεση"),
  Q("Γιατί οι εκτοξεύσεις γίνονται στις ίδιες ώρες παντού;", ["Για λόγους ασφάλειας", "Για να μπορούν να συγκριθούν τα δεδομένα", "Γιατί τότε φυσάει λιγότερο", "Για να τις βλέπει το κοινό"], 1, "ώστε τα δεδομένα να μπορούν να συγκριθούν"),
  Q("Γιατί σκάει τελικά το μπαλόνι;", ["Γιατί το χτυπάει κεραυνός", "Γιατί η πίεση πέφτει και φουσκώνει υπερβολικά", "Γιατί το τρυπούν πουλιά", "Γιατί το σκάνε επίτηδες"], 1, "η πίεση γύρω του πέφτει και το μπαλόνι φουσκώνει"),
 ],
 "gloss": {"ραδιοβολίδα": "ραδιοβολίδα — radiosonde", "υγρασία": "υγρασία — humidity", "εκτοξεύσεις": "εκτόξευση — launch", "ραδιοκύματα": "ραδιοκύμα — radio wave", "φουσκώνει": "φουσκώνω — to inflate, expand", "αλεξίπτωτο": "αλεξίπτωτο — parachute"},
})
ITEMS.append({
 "id": "l202-c1-mono-katara-tis-gnosis", "title": "Η κατάρα της γνώσης", "title_en": "The curse of knowledge", "type": "monologue", "level": "C1",
 "context_el": "Μια ψυχολόγος μιλάει σε ένα σεμινάριο για καθηγητές και εκπαιδευτές.",
 "script": [
  L("Ψυχολόγος", "f", "Στα τέλη της δεκαετίας του ογδόντα, μια φοιτήτρια ψυχολογίας στο Στάνφορντ, η Ελίζαμπεθ Νιούτον, έκανε ένα απλό πείραμα. Χώρισε τους συμμετέχοντες σε «χτυπητές» και «ακροατές». Οι χτυπητές διάλεγαν ένα πολύ γνωστό τραγούδι, όπως το «Χρόνια πολλά», και χτυπούσαν τον ρυθμό του πάνω στο τραπέζι. Οι ακροατές έπρεπε να μαντέψουν ποιο ήταν.", "In the late eighties, a psychology student at Stanford, Elizabeth Newton, carried out a simple experiment. She divided the participants into 'tappers' and 'listeners'. The tappers chose a very well-known song, such as 'Happy Birthday', and tapped out its rhythm on the table. The listeners had to guess which it was."),
  L("Ψυχολόγος", "f", "Πριν ξεκινήσουν, οι χτυπητές εκτίμησαν ότι οι ακροατές θα βρίσκουν περίπου το μισό των τραγουδιών. Στην πραγματικότητα, όπως συνήθως αναφέρεται, βρήκαν σωστά μόνο τρία στα εκατόν είκοσι. Η εξήγηση είναι απλή και αμείλικτη: ο χτυπητής ακούει τη μελωδία μέσα στο κεφάλι του και δεν μπορεί να φανταστεί πώς ακούγεται το ίδιο τραγούδι χωρίς αυτήν, ως μια σειρά από ξερά χτυπήματα.", "Before they started, the tappers estimated that the listeners would identify about half of the songs. In reality, as it is usually reported, they correctly identified only three out of a hundred and twenty. The explanation is simple and merciless: the tapper hears the melody in his head and cannot imagine what the same song sounds like without it, as a series of dry knocks."),
  L("Ψυχολόγος", "f", "Αυτό το φαινόμενο ονομάζεται «κατάρα της γνώσης»: μόλις μάθουμε κάτι, μας είναι σχεδόν αδύνατο να θυμηθούμε πώς ήταν να μην το ξέρουμε. Γι' αυτό οι ειδικοί συχνά είναι κακοί δάσκαλοι αρχαρίων. Παραλείπουν βήματα που τους φαίνονται αυτονόητα και χρησιμοποιούν όρους που για τους ίδιους έχουν πάψει να είναι όροι.", "This phenomenon is called the 'curse of knowledge': once we learn something, it is almost impossible for us to remember what it was like not to know it. That is why experts are often poor teachers of beginners. They skip steps that seem self-evident to them and use terms that, for them, have stopped being terms."),
  L("Ψυχολόγος", "f", "Η καλή είδηση είναι ότι η κατάρα αυτή αντιμετωπίζεται, όχι με περισσότερη γνώση αλλά με περισσότερη επαφή με τον αρχάριο: δοκιμάστε την εξήγησή σας σε κάποιον που δεν ξέρει τίποτα και παρατηρήστε σε ποιο σημείο χάνεται. Εκεί βρίσκεται το βήμα που εσείς έχετε ξεχάσει ότι υπάρχει.", "The good news is that this curse can be countered, not with more knowledge but with more contact with the beginner: try your explanation on someone who knows nothing and watch where they get lost. That is where the step lies that you have forgotten exists."),
 ],
 "questions": [
  Q("Τι έκαναν οι «χτυπητές» στο πείραμα;", ["Τραγουδούσαν δυνατά", "Χτυπούσαν τον ρυθμό ενός γνωστού τραγουδιού στο τραπέζι", "Έπαιζαν πιάνο", "Μάντευαν τραγούδια"], 1, "χτυπούσαν τον ρυθμό του πάνω στο τραπέζι"),
  Q("Πόσο απείχε η εκτίμηση των χτυπητών από το αποτέλεσμα;", ["Ήταν σχεδόν ακριβής", "Περίμεναν περίπου το μισό, ενώ βρέθηκαν μόνο τρία στα εκατόν είκοσι", "Υποτίμησαν τους ακροατές", "Δεν έκαναν καμία εκτίμηση"], 1, "βρήκαν σωστά μόνο τρία στα εκατόν είκοσι"),
  Q("Γιατί, σύμφωνα με την ομιλήτρια, οι ειδικοί είναι συχνά κακοί δάσκαλοι αρχαρίων;", ["Γιατί βαριούνται", "Γιατί παραλείπουν βήματα που τους φαίνονται αυτονόητα", "Γιατί δεν ξέρουν αρκετά", "Γιατί μιλούν πολύ αργά"], 1, "Παραλείπουν βήματα που τους φαίνονται αυτονόητα"),
  Q("Πώς αντιμετωπίζεται η «κατάρα της γνώσης»;", ["Με περισσότερο διάβασμα", "Δοκιμάζοντας την εξήγηση σε έναν αρχάριο και βλέποντας πού χάνεται", "Με απλούστερα βιβλία", "Αποφεύγοντας τους όρους εντελώς"], 1, "δοκιμάστε την εξήγησή σας σε κάποιον που δεν ξέρει τίποτα"),
 ],
 "gloss": {"κατάρα": "κατάρα — curse", "συμμετέχοντες": "συμμετέχων — participant", "μαντέψουν": "μαντεύω — to guess", "εκτίμησαν": "εκτιμώ — to estimate", "αμείλικτη": "αμείλικτος — merciless, relentless", "αρχαρίων": "αρχάριος — beginner", "αυτονόητα": "αυτονόητος — self-evident"},
})
ITEMS.append({
 "id": "l202-c1-int-soroban", "title": "Αριθμητική με τον άβακα στο μυαλό", "title_en": "Mental arithmetic with an imaginary abacus", "type": "interview", "level": "C1",
 "context_el": "Συνέντευξη με μια εκπαιδευτικό που διδάσκει νοερή αριθμητική με τον ιαπωνικό άβακα σοροβάν.",
 "script": [
  L("Δημοσιογράφος", "m", "Είδα ένα παιδί δέκα χρονών να προσθέτει δεκαπέντε τριψήφιους αριθμούς σε λίγα δευτερόλεπτα, κουνώντας τα δάχτυλά του στον αέρα. Τι ακριβώς έκανε;", "I saw a ten-year-old add fifteen three-digit numbers in a few seconds, moving his fingers in the air. What exactly was he doing?"),
  L("Εκπαιδευτικός", "f", "Χειριζόταν έναν άβακα που υπάρχει μόνο στο μυαλό του. Τα παιδιά μαθαίνουν πρώτα στο σοροβάν, τον ιαπωνικό άβακα, που έχει σε κάθε στύλο μία χάντρα πάνω, που αξίζει πέντε, και τέσσερις κάτω, που αξίζουν από μία. Μετά από μήνες εξάσκησης, αρκετά από αυτά αρχίζουν να «βλέπουν» τον άβακα με κλειστά μάτια και να μετακινούν νοερά τις χάντρες. Τα δάχτυλα που κουνιούνται είναι το κατάλοιπο της αληθινής κίνησης.", "He was operating an abacus that exists only in his mind. The children first learn on the soroban, the Japanese abacus, which has on each rod one bead above, worth five, and four below, worth one each. After months of practice, quite a few of them begin to 'see' the abacus with their eyes closed and to move the beads mentally. The moving fingers are what remains of the real movement."),
  L("Δημοσιογράφος", "m", "Δηλαδή δεν υπολογίζουν όπως εμείς, με αριθμούς και κρατούμενα;", "So they don't calculate like we do, with numbers and carrying?"),
  L("Εκπαιδευτικός", "f", "Όχι ακριβώς. Είναι μια οπτική και κινητική διαδικασία περισσότερο παρά γλωσσική. Γι' αυτό, παραδόξως, μερικά παιδιά μπορούν να υπολογίζουν και να μιλάνε ταυτόχρονα. Οφείλω όμως να είμαι ειλικρινής: το αν αυτή η δεξιότητα βελτιώνει γενικότερα τα μαθηματικά ή τη συγκέντρωση είναι κάτι που η έρευνα δεν έχει αποδείξει πειστικά. Υπάρχουν ενθαρρυντικές μελέτες, αλλά και πολλές υπερβολές στη διαφήμιση.", "Not exactly. It's a visual and motor process more than a linguistic one. That's why, paradoxically, some children can calculate and talk at the same time. But I must be honest: whether this skill improves mathematics or concentration more generally is something research hasn't convincingly proven. There are encouraging studies, but also a lot of exaggeration in the advertising."),
  L("Δημοσιογράφος", "m", "Τότε γιατί αξίζει;", "Then why is it worth it?"),
  L("Εκπαιδευτικός", "f", "Γιατί τα παιδιά νιώθουν ότι οι αριθμοί γίνονται κάτι απτό, σχεδόν παιχνίδι. Ένα παιδί που φοβόταν τα μαθηματικά και ξαφνικά τα απολαμβάνει έχει κερδίσει κάτι που δεν μετριέται εύκολα σε τεστ.", "Because the children feel that numbers become something tangible, almost a game. A child who was afraid of mathematics and suddenly enjoys it has gained something that isn't easily measured in tests."),
 ],
 "questions": [
  Q("Τι έκανε το παιδί με τα δάχτυλα στον αέρα;", ["Μετρούσε με τα δάχτυλα", "Χειριζόταν έναν άβακα που υπάρχει μόνο στο μυαλό του", "Έγραφε τους αριθμούς", "Χαιρετούσε"], 1, "Χειριζόταν έναν άβακα που υπάρχει μόνο στο μυαλό του"),
  Q("Πόσο αξίζει η πάνω χάντρα σε κάθε στύλο του σοροβάν;", ["Ένα", "Δέκα", "Πέντε", "Τέσσερα"], 2, "μία χάντρα πάνω, που αξίζει πέντε"),
  Q("Γιατί μερικά παιδιά μπορούν να υπολογίζουν και να μιλάνε ταυτόχρονα;", ["Γιατί είναι ιδιοφυΐες", "Γιατί η διαδικασία είναι κυρίως οπτική και κινητική, όχι γλωσσική", "Γιατί μαθαίνουν απέξω τα αποτελέσματα", "Γιατί χρησιμοποιούν αριθμομηχανή"], 1, "Είναι μια οπτική και κινητική διαδικασία περισσότερο παρά γλωσσική"),
  Q("Τι λέει η εκπαιδευτικός για την έρευνα;", ["Ότι αποδεικνύει μεγάλα οφέλη", "Ότι δεν έχει αποδείξει πειστικά γενικότερα οφέλη", "Ότι δείχνει βλάβες", "Ότι δεν υπάρχει καμία μελέτη"], 1, "η έρευνα δεν έχει αποδείξει πειστικά"),
 ],
 "gloss": {"νοερή": "νοερός — mental", "άβακα": "άβακας — abacus", "τριψήφιους": "τριψήφιος — three-digit", "χάντρα": "χάντρα — bead", "στύλο": "στύλος — rod, pillar", "κατάλοιπο": "κατάλοιπο — remnant, residue", "κρατούμενα": "κρατούμενο — carried digit", "απτό": "απτός — tangible"},
})

rnd = random.Random(202)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-202.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
