# Source for library/listening/listening-81.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l81.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l81-ann-katastroma", "title": "Ανακοίνωση για τα καταστρώματα του πλοίου", "title_en": "Announcement about the ship's decks", "type": "announcement", "level": "B2",
 "context_el": "Ταξιδεύετε με ένα πλοίο της γραμμής προς τις Κυκλάδες. Λίγο μετά την αναχώρηση ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Αξιωματικός", "m", "Κυρίες και κύριοι, καλησπέρα σας. Σας ενημερώνουμε ότι λόγω των ισχυρών ανέμων στο Αιγαίο, τα εξωτερικά καταστρώματα θα παραμείνουν κλειστά για όλη τη διάρκεια του ταξιδιού. Παρακαλούμε τους επιβάτες να παραμείνουν στους εσωτερικούς χώρους του πλοίου.", "Ladies and gentlemen, good evening. We inform you that because of the strong winds in the Aegean, the outside decks will remain closed for the whole voyage. Passengers are asked to remain in the indoor areas of the ship."),
  L("Αξιωματικός", "m", "Υπενθυμίζουμε ότι κατά τη διάρκεια του ταξιδιού δεν επιτρέπεται η πρόσβαση στα γκαράζ. Αν χρειάζεστε κάτι από το αυτοκίνητό σας, θα πρέπει να περιμένετε μέχρι την άφιξη. Όσοι αισθάνονται ναυτία μπορούν να ζητήσουν βοήθεια από το πλήρωμα στη ρεσεψιόν, στο κατάστρωμα επτά.", "We remind you that access to the car decks is not permitted during the voyage. If you need something from your car, you will have to wait until arrival. Anyone feeling seasick can ask the crew for help at reception, on deck seven."),
  L("Αξιωματικός", "m", "Λόγω του κυματισμού, η άφιξή μας στη Νάξο αναμένεται με καθυστέρηση περίπου σαράντα λεπτών. Ζητούμε την κατανόησή σας και σας ευχόμαστε καλό ταξίδι.", "Because of the swell, our arrival in Naxos is expected about forty minutes late. We ask for your understanding and wish you a pleasant voyage."),
 ],
 "questions": [
  Q("Γιατί θα μείνουν κλειστά τα εξωτερικά καταστρώματα;", ["Λόγω καθαρισμού", "Λόγω των ισχυρών ανέμων", "Λόγω βροχής", "Γιατί είναι νύχτα"], 1, "λόγω των ισχυρών ανέμων στο Αιγαίο, τα εξωτερικά καταστρώματα θα παραμείνουν κλειστά"),
  Q("Τι πρέπει να κάνει όποιος χρειάζεται κάτι από το αυτοκίνητό του;", ["Να ζητήσει άδεια από τον καπετάνιο", "Να περιμένει μέχρι την άφιξη", "Να πάει στη ρεσεψιόν", "Να κατέβει με έναν ναύτη"], 1, "θα πρέπει να περιμένετε μέχρι την άφιξη"),
  Q("Πόση καθυστέρηση αναμένεται;", ["Δέκα λεπτά", "Περίπου σαράντα λεπτά", "Μία ώρα", "Δύο ώρες"], 1, "καθυστέρηση περίπου σαράντα λεπτών"),
 ],
 "gloss": {"καταστρώματα": "κατάστρωμα — deck", "ισχυρών ανέμων": "ισχυροί άνεμοι — strong winds", "εσωτερικούς χώρους": "εσωτερικοί χώροι — indoor areas", "πρόσβαση": "πρόσβαση — access", "γκαράζ": "γκαράζ — garage, car deck", "ναυτία": "ναυτία — seasickness, nausea", "πλήρωμα": "πλήρωμα — crew", "κυματισμού": "κυματισμός — swell, rough sea", "κατανόησή": "κατανόηση — understanding"},
})
ITEMS.append({
 "id": "l81-vm-kommotirio-skylon", "title": "Μήνυμα από το κομμωτήριο σκύλων", "title_en": "Voicemail from the dog groomer", "type": "voicemail", "level": "B2",
 "context_el": "Αφήσατε τον σκύλο σας σε ένα κομμωτήριο σκύλων. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Μυρτώ", "f", "Γεια σας, είμαι η Μυρτώ από το κομμωτήριο σκύλων «Χνούδι». Ο Ρόκι είναι έτοιμος νωρίτερα απ’ ό,τι υπολογίζαμε: τον λούσαμε, του κόψαμε το τρίχωμα και τα νύχια, και ήταν πολύ ήσυχος, σαν άγγελος.", "Hello, this is Myrto from the 'Fluff' dog grooming salon. Rocky is ready earlier than we expected: we washed him, trimmed his coat and his nails, and he was very calm, like an angel."),
  L("Μυρτώ", "f", "Θέλω μόνο να σας πω ότι, ενώ τον βουρτσίζαμε, βρήκαμε ένα τσιμπούρι πίσω από το αριστερό του αυτί. Το αφαιρέσαμε προσεκτικά, αλλά καλό θα ήταν να τον δει και ο κτηνίατρός σας τις επόμενες μέρες και να του βάλετε αντιπαρασιτικό.", "I just want to tell you that, while we were brushing him, we found a tick behind his left ear. We removed it carefully, but it would be a good idea for your vet to see him in the next few days and for you to give him an anti-parasite treatment."),
  L("Μυρτώ", "f", "Μπορείτε να περάσετε να τον πάρετε όποτε θέλετε μέχρι τις επτά. Πληρώνετε στο μαγαζί, και δεχόμαστε και κάρτα. Τα λέμε!", "You can come and pick him up whenever you like until seven. You pay at the shop, and we take cards too. See you!"),
 ],
 "questions": [
  Q("Τι έκαναν στον Ρόκι;", ["Μόνο μπάνιο", "Τον έλουσαν και του έκοψαν το τρίχωμα και τα νύχια", "Του έκαναν εμβόλιο", "Τον εκπαίδευσαν"], 1, "τον λούσαμε, του κόψαμε το τρίχωμα και τα νύχια"),
  Q("Τι βρήκαν ενώ τον βούρτσιζαν;", ["Μια πληγή", "Ένα τσιμπούρι", "Ψύλλους", "Ένα τσιπάκι"], 1, "βρήκαμε ένα τσιμπούρι πίσω από το αριστερό του αυτί"),
  Q("Τι συμβουλεύει η Μυρτώ;", ["Να τον λούζουν πιο συχνά", "Να τον δει ο κτηνίατρος και να του βάλουν αντιπαρασιτικό", "Να μην τον βγάζουν στο πάρκο", "Να του κόβουν πιο κοντά το τρίχωμα"], 1, "καλό θα ήταν να τον δει και ο κτηνίατρός σας τις επόμενες μέρες και να του βάλετε αντιπαρασιτικό"),
 ],
 "gloss": {"κομμωτήριο σκύλων": "κομμωτήριο σκύλων — dog grooming salon", "Χνούδι": "χνούδι — fluff, down", "λούσαμε": "λούζω — to wash (hair, a pet)", "τρίχωμα": "τρίχωμα — coat, fur", "νύχια": "νύχι — nail, claw", "βουρτσίζαμε": "βουρτσίζω — to brush", "τσιμπούρι": "τσιμπούρι — tick", "αφαιρέσαμε": "αφαιρώ — to remove", "αντιπαρασιτικό": "αντιπαρασιτικό — anti-parasite treatment"},
})
ITEMS.append({
 "id": "l81-dia-krevati-skala", "title": "Το κρεβάτι δεν χωράει στη σκάλα", "title_en": "The bed won't fit up the stairs", "type": "dialogue", "level": "B2",
 "context_el": "Οι μεταφορείς ενός καταστήματος επίπλων δεν μπόρεσαν να ανεβάσουν ένα κρεβάτι στο διαμέρισμα ενός πελάτη. Ο πελάτης τηλεφωνεί στο κατάστημα.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Οι μεταφορείς σας ήρθαν σήμερα το πρωί με το κρεβάτι που παρήγγειλα, αλλά δεν χωρούσε στη σκάλα της πολυκατοικίας και το πήραν πίσω. Τώρα τι κάνουμε;", "Good morning. Your delivery men came this morning with the bed I ordered, but it didn't fit up the building's staircase and they took it back. What do we do now?"),
  L("Υπάλληλος", "f", "Λυπάμαι για την ταλαιπωρία. Υπάρχουν δύο λύσεις. Η πρώτη είναι να το ανεβάσουμε από το μπαλκόνι με ανυψωτικό μηχάνημα. Αυτό όμως κοστίζει ογδόντα ευρώ επιπλέον και χρειάζεται άδεια από τον δήμο για να κλείσει για λίγο ο δρόμος.", "I'm sorry for the inconvenience. There are two solutions. The first is to bring it up through the balcony with a lift. That costs eighty euros extra, though, and it needs a permit from the municipality to close the road for a while."),
  L("Πελάτης", "m", "Και η δεύτερη;", "And the second?"),
  L("Υπάλληλος", "f", "Η δεύτερη είναι να ξεβιδώσουμε το κεφαλάρι, που είναι το πιο μεγάλο κομμάτι, και να το συναρμολογήσουμε ξανά μέσα στο σπίτι. Αυτή γίνεται δωρεάν, απλώς θα κρατήσει περίπου μία ώρα παραπάνω.", "The second is to unscrew the headboard, which is the biggest piece, and assemble it again inside the flat. That's free of charge; it will just take about an hour longer."),
  L("Πελάτης", "m", "Τότε προτιμώ τη δεύτερη. Πότε μπορείτε να έρθετε;", "Then I prefer the second. When can you come?"),
  L("Υπάλληλος", "f", "Την Πέμπτη, ανάμεσα στις δέκα και τη μία. Θα σας στείλουμε μήνυμα μισή ώρα πριν φτάσουν οι μεταφορείς.", "On Thursday, between ten and one. We'll send you a message half an hour before the delivery men arrive."),
 ],
 "questions": [
  Q("Γιατί οι μεταφορείς πήραν πίσω το κρεβάτι;", ["Ήταν λάθος μοντέλο", "Δεν χωρούσε στη σκάλα", "Ήταν σπασμένο", "Ο πελάτης δεν ήταν σπίτι"], 1, "δεν χωρούσε στη σκάλα της πολυκατοικίας"),
  Q("Τι χρειάζεται η πρώτη λύση, εκτός από τα ογδόντα ευρώ;", ["Την υπογραφή του διαχειριστή", "Άδεια από τον δήμο για να κλείσει ο δρόμος", "Έναν δεύτερο μεταφορέα", "Ένα μεγαλύτερο φορτηγό"], 1, "χρειάζεται άδεια από τον δήμο για να κλείσει για λίγο ο δρόμος"),
  Q("Ποιο είναι το μειονέκτημα της δεύτερης λύσης;", ["Κοστίζει περισσότερο", "Θα κρατήσει περίπου μία ώρα παραπάνω", "Το κρεβάτι θα χάσει την εγγύηση", "Θα γίνει τον επόμενο μήνα"], 1, "θα κρατήσει περίπου μία ώρα παραπάνω"),
 ],
 "gloss": {"μεταφορείς": "μεταφορέας — delivery man", "επίπλων": "έπιπλο — piece of furniture", "χωρούσε": "χωράω — to fit", "ταλαιπωρία": "ταλαιπωρία — inconvenience, hassle", "ανυψωτικό μηχάνημα": "ανυψωτικό μηχάνημα — (furniture) lift, hoist", "άδεια": "άδεια — permit", "ξεβιδώσουμε": "ξεβιδώνω — to unscrew", "κεφαλάρι": "κεφαλάρι — headboard", "συναρμολογήσουμε": "συναρμολογώ — to assemble"},
})
ITEMS.append({
 "id": "l81-int-radioerasitechnis", "title": "Ένας ραδιοερασιτέχνης", "title_en": "A radio amateur", "type": "interview", "level": "B2",
 "context_el": "Σε μια τοπική ραδιοφωνική εκπομπή, η δημοσιογράφος μιλά με τον κύριο Ηλία, που είναι ραδιοερασιτέχνης εδώ και σαράντα χρόνια.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Ηλία, τι ακριβώς κάνει ένας ραδιοερασιτέχνης στην εποχή του ίντερνετ;", "Mr Ilias, what exactly does a radio amateur do in the age of the internet?"),
  L("Ηλίας", "m", "Μιλάμε με ανθρώπους σε όλο τον κόσμο μέσω ασυρμάτου, χωρίς καμία εταιρεία στη μέση. Από το δωμάτιό μου στη Λάρισα έχω μιλήσει με ψαράδες στη Νορβηγία, με έναν δάσκαλο στη Βραζιλία, ακόμα και με αστροναύτες στον Διεθνή Διαστημικό Σταθμό. Αλλά για να εκπέμπεις, χρειάζεσαι άδεια, και για την άδεια πρέπει να περάσεις εξετάσεις.", "We talk to people all over the world by radio, without any company in the middle. From my room in Larissa I've talked with fishermen in Norway, a teacher in Brazil, even astronauts on the International Space Station. But to transmit you need a licence, and for the licence you have to pass exams."),
  L("Δημοσιογράφος", "f", "Είναι μόνο χόμπι;", "Is it just a hobby?"),
  L("Ηλίας", "m", "Όχι μόνο. Όταν μετά από έναν σεισμό ή μια πλημμύρα πέφτουν τα δίκτυα κινητής τηλεφωνίας, ο ασύρματος συνεχίζει να λειτουργεί, αρκεί να υπάρχει μια μπαταρία. Πολλές φορές οι ραδιοερασιτέχνες ήταν οι πρώτοι που μετέφεραν μηνύματα από αποκλεισμένα χωριά στις αρχές.", "Not only. When the mobile networks go down after an earthquake or a flood, the radio keeps working, as long as there's a battery. Many times radio amateurs have been the first to carry messages from cut-off villages to the authorities."),
  L("Δημοσιογράφος", "f", "Χρησιμοποιείτε ακόμα τον κώδικα Μορς;", "Do you still use Morse code?"),
  L("Ηλίας", "m", "Και βέβαια. Δεν είναι πια υποχρεωτικός για την άδεια, αλλά εγώ τον αγαπώ. Είναι σαν μια μουσική που την καταλαβαίνουν οι ραδιοερασιτέχνες όλου του κόσμου, ό,τι γλώσσα κι αν μιλούν.", "Of course. It's no longer compulsory for the licence, but I love it. It's like a music understood by radio amateurs all over the world, whatever language they speak."),
 ],
 "questions": [
  Q("Τι χρειάζεται κάποιος για να εκπέμπει;", ["Μια συνδρομή στο ίντερνετ", "Άδεια, για την οποία πρέπει να περάσει εξετάσεις", "Μια σύσταση από έναν άλλο ραδιοερασιτέχνη", "Ένα πτυχίο ηλεκτρολόγου"], 1, "για να εκπέμπεις, χρειάζεσαι άδεια, και για την άδεια πρέπει να περάσεις εξετάσεις"),
  Q("Γιατί είναι χρήσιμος ο ασύρματος μετά από μια καταστροφή;", ["Γιατί είναι φθηνότερος", "Γιατί συνεχίζει να λειτουργεί όταν πέφτουν τα δίκτυα κινητής", "Γιατί τον χρησιμοποιεί ο στρατός", "Γιατί έχει καλύτερο ήχο"], 1, "ο ασύρματος συνεχίζει να λειτουργεί, αρκεί να υπάρχει μια μπαταρία"),
  Q("Τι λέει ο κύριος Ηλίας για τον κώδικα Μορς;", ["Δεν τον χρησιμοποιεί κανείς πια", "Δεν είναι πια υποχρεωτικός, αλλά τον αγαπά", "Είναι υποχρεωτικός για την άδεια", "Τον έμαθε πρόσφατα"], 1, "Δεν είναι πια υποχρεωτικός για την άδεια, αλλά εγώ τον αγαπώ"),
 ],
 "gloss": {"ραδιοερασιτέχνης": "ραδιοερασιτέχνης — radio amateur, ham", "ασυρμάτου": "ασύρματος — radio (transmitter)", "αστροναύτες": "αστροναύτης — astronaut", "Διεθνή Διαστημικό Σταθμό": "Διεθνής Διαστημικός Σταθμός — International Space Station", "εκπέμπεις": "εκπέμπω — to transmit, broadcast", "άδεια": "άδεια — licence", "δίκτυα κινητής τηλεφωνίας": "δίκτυα κινητής τηλεφωνίας — mobile networks", "αποκλεισμένα": "αποκλεισμένος — cut off", "αρχές": "αρχές — the authorities", "κώδικα Μορς": "κώδικας Μορς — Morse code"},
})
ITEMS.append({
 "id": "l81-rep-parko-tritsi", "title": "Το Πάρκο Τρίτση", "title_en": "Tritsis Park", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα μεγάλο πάρκο στα δυτικά της Αθήνας.",
 "script": [
  L("Ρεπόρτερ", "f", "Λίγοι Αθηναίοι το γνωρίζουν, όμως στα δυτικά της πόλης, στο Ίλιον, βρίσκεται ένα από τα μεγαλύτερα πάρκα της Αττικής, το Πάρκο Αντώνη Τρίτση. Με λίμνες, καλαμιώνες και ελαιώνες, μοιάζει περισσότερο με κομμάτι εξοχής παρά με αστικό πάρκο.", "Few Athenians know it, but in the west of the city, in Ilion, lies one of the largest parks in Attica, Antonis Tritsis Park. With lakes, reed beds and olive groves, it looks more like a piece of countryside than an urban park."),
  L("Ρεπόρτερ", "f", "Οι λίμνες του προσελκύουν δεκάδες είδη πουλιών, από πάπιες και νερόκοτες μέχρι ερωδιούς, που σταματούν εδώ κατά τη μετανάστευσή τους. Κάθε Σαββατοκύριακο, ομάδες παρατηρητών με κιάλια περπατούν σιωπηλά στα μονοπάτια, και τα σχολεία της περιοχής φέρνουν εδώ τους μαθητές για μαθήματα περιβαλλοντικής εκπαίδευσης.", "Its lakes attract dozens of bird species, from ducks and moorhens to herons, which stop here during their migration. Every weekend, groups of birdwatchers with binoculars walk silently along the paths, and the schools of the area bring their pupils here for environmental education lessons."),
  L("Ρεπόρτερ", "f", "Το πάρκο, όμως, αντιμετωπίζει προβλήματα. Οι εθελοντές λένε ότι η συντήρηση δεν είναι πάντα επαρκής και ότι ορισμένοι επισκέπτες αφήνουν τα σκυλιά τους ελεύθερα, ενοχλώντας τα πουλιά. Ζητούν περισσότερους φύλακες και καλύτερη σήμανση στις εισόδους.", "The park, however, faces problems. Volunteers say that maintenance is not always adequate and that some visitors let their dogs run free, disturbing the birds. They are asking for more wardens and better signs at the entrances."),
 ],
 "questions": [
  Q("Με τι μοιάζει το πάρκο, σύμφωνα με τη ρεπόρτερ;", ["Με έναν βοτανικό κήπο", "Με κομμάτι εξοχής", "Με παιδική χαρά", "Με γήπεδο"], 1, "μοιάζει περισσότερο με κομμάτι εξοχής παρά με αστικό πάρκο"),
  Q("Γιατί έρχονται εδώ τα σχολεία;", ["Για αθλητικούς αγώνες", "Για μαθήματα περιβαλλοντικής εκπαίδευσης", "Για εκδρομές με ποδήλατα", "Για να φυτέψουν δέντρα"], 1, "για μαθήματα περιβαλλοντικής εκπαίδευσης"),
  Q("Τι ζητούν οι εθελοντές;", ["Να κλείσει το πάρκο τα Σαββατοκύριακα", "Περισσότερους φύλακες και καλύτερη σήμανση", "Να απαγορευτούν τα σχολεία", "Νέες λίμνες"], 1, "Ζητούν περισσότερους φύλακες και καλύτερη σήμανση στις εισόδους"),
 ],
 "gloss": {"καλαμιώνες": "καλαμιώνας — reed bed", "ελαιώνες": "ελαιώνας — olive grove", "εξοχής": "εξοχή — countryside", "νερόκοτες": "νερόκοτα — moorhen", "ερωδιούς": "ερωδιός — heron", "μετανάστευσή": "μετανάστευση — migration", "παρατηρητών": "παρατηρητής — (bird)watcher, observer", "κιάλια": "κιάλια — binoculars", "συντήρηση": "συντήρηση — maintenance", "επαρκής": "επαρκής — adequate", "φύλακες": "φύλακας — warden, guard", "σήμανση": "σήμανση — signage"},
})
ITEMS.append({
 "id": "l81-rep-styga", "title": "Τα νερά της Στύγας", "title_en": "The waters of the Styx", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ταξιδιωτικό ρεπορτάζ από τον Χελμό, στη βόρεια Πελοπόννησο.",
 "script": [
  L("Ρεπόρτερ", "m", "Στις απόκρημνες πλαγιές του Χελμού, ένας καταρράκτης πέφτει από ύψος περίπου διακοσίων μέτρων πάνω σε σκουρόχρωμα βράχια. Οι ντόπιοι τον λένε Μαυρονέρι, από το χρώμα των βράχων. Από την αρχαιότητα, όμως, πολλοί τον ταυτίζουν με τη Στύγα, τον ποταμό του Κάτω Κόσμου στη μυθολογία.", "On the steep slopes of Mount Chelmos, a waterfall drops about two hundred metres onto dark rocks. The locals call it Mavroneri, 'black water', from the colour of the rocks. Since antiquity, though, many have identified it with the Styx, the river of the Underworld in mythology."),
  L("Ρεπόρτερ", "m", "Σύμφωνα με τον μύθο, οι θεοί ορκίζονταν στο νερό της Στύγας, και όποιος παρέβαινε τον όρκο έχανε για χρόνια τη θεϊκή του δύναμη. Εδώ, λέει η παράδοση, η Θέτιδα βούτηξε τον μικρό Αχιλλέα για να γίνει άτρωτος, κρατώντας τον από τη φτέρνα.", "According to myth, the gods swore oaths on the water of the Styx, and whoever broke the oath lost their divine power for years. Here, tradition says, Thetis dipped the infant Achilles to make him invulnerable, holding him by the heel."),
  L("Ρεπόρτερ", "m", "Η διαδρομή μέχρι τη βάση του καταρράκτη ξεκινά από το χωριό Περιστέρα και διαρκεί περίπου τρεις ώρες. Είναι απαιτητική και δεν συνιστάται τον χειμώνα, όταν τα μονοπάτια καλύπτονται από χιόνι. Οι οδηγοί βουνού συμβουλεύουν να ξεκινάτε νωρίς και να έχετε μαζί σας αρκετό νερό, γιατί στη διαδρομή δεν υπάρχει πηγή.", "The route to the foot of the waterfall starts from the village of Peristera and takes about three hours. It is demanding and not recommended in winter, when the paths are covered with snow. Mountain guides advise setting off early and taking enough water with you, because there is no spring along the way."),
 ],
 "questions": [
  Q("Γιατί οι ντόπιοι λένε τον καταρράκτη Μαυρονέρι;", ["Γιατί το νερό είναι βρόμικο", "Από το χρώμα των βράχων", "Γιατί πέφτει τη νύχτα", "Από ένα παλιό χωριό"], 1, "Οι ντόπιοι τον λένε Μαυρονέρι, από το χρώμα των βράχων"),
  Q("Τι έπαθε, κατά τον μύθο, ο θεός που παρέβαινε τον όρκο;", ["Πέθαινε", "Έχανε για χρόνια τη θεϊκή του δύναμη", "Γινόταν άνθρωπος για πάντα", "Εξοριζόταν στη Στύγα"], 1, "όποιος παρέβαινε τον όρκο έχανε για χρόνια τη θεϊκή του δύναμη"),
  Q("Γιατί πρέπει να έχουν μαζί τους αρκετό νερό οι πεζοπόροι;", ["Γιατί κάνει πολλή ζέστη", "Γιατί στη διαδρομή δεν υπάρχει πηγή", "Γιατί το νερό του καταρράκτη είναι δηλητηριώδες", "Γιατί η διαδρομή κρατάει δύο μέρες"], 1, "στη διαδρομή δεν υπάρχει πηγή"),
 ],
 "gloss": {"απόκρημνες": "απόκρημνος — steep, sheer", "καταρράκτης": "καταρράκτης — waterfall", "σκουρόχρωμα": "σκουρόχρωμος — dark-coloured", "ταυτίζουν": "ταυτίζω — to identify (with)", "Κάτω Κόσμου": "Κάτω Κόσμος — the Underworld", "ορκίζονταν": "ορκίζομαι — to swear (an oath)", "παρέβαινε": "παραβαίνω — to break, violate", "άτρωτος": "άτρωτος — invulnerable", "φτέρνα": "φτέρνα — heel", "απαιτητική": "απαιτητικός — demanding", "συνιστάται": "συνιστώμαι — to be recommended"},
})
ITEMS.append({
 "id": "l81-mono-tselo", "title": "Τσέλο στα σαράντα πέντε", "title_en": "Cello at forty-five", "type": "monologue", "level": "B2",
 "context_el": "Σε μια εκπομπή για ενήλικες που μαθαίνουν κάτι καινούργιο, η Ζωή μιλά για τα μαθήματα τσέλου που ξεκίνησε στα σαράντα πέντε της.",
 "script": [
  L("Ζωή", "f", "Από παιδί ήθελα να παίζω τσέλο, αλλά οι γονείς μου έλεγαν ότι είναι ακριβό και ογκώδες, και με έστειλαν σε μαθήματα αγγλικών. Στα σαράντα πέντε, όταν τα παιδιά μου έφυγαν για σπουδές, νοίκιασα ένα τσέλο από ένα ωδείο και έκλεισα το πρώτο μου μάθημα.", "Since I was a child I wanted to play the cello, but my parents said it was expensive and bulky, and sent me to English lessons. At forty-five, when my children left to study, I rented a cello from a music school and booked my first lesson."),
  L("Ζωή", "f", "Οι πρώτοι μήνες ήταν απογοητευτικοί. Το δοξάρι γλιστρούσε, οι νότες έβγαιναν φάλτσες και ο σκύλος μου έφευγε από το δωμάτιο μόλις άνοιγα τη θήκη. Ο δάσκαλός μου, όμως, μου είπε κάτι που με βοήθησε: «Τα παιδιά μαθαίνουν πιο γρήγορα, αλλά οι ενήλικες ξέρουν γιατί μαθαίνουν.»", "The first months were disheartening. The bow slipped, the notes came out out of tune, and my dog left the room as soon as I opened the case. My teacher, though, told me something that helped: 'Children learn faster, but adults know why they are learning.'"),
  L("Ζωή", "f", "Σήμερα, τρία χρόνια μετά, παίζω σε μια ερασιτεχνική ορχήστρα της γειτονιάς. Είμαι η μεγαλύτερη στα τσέλα, και η πιο αργή, αλλά κανείς δεν με κοιτάζει περίεργα. Και ο σκύλος, πλέον, ξαπλώνει δίπλα μου όταν κάνω εξάσκηση.", "Today, three years later, I play in an amateur neighbourhood orchestra. I'm the oldest in the cello section, and the slowest, but nobody looks at me strangely. And the dog now lies down next to me when I practise."),
 ],
 "questions": [
  Q("Γιατί δεν έμαθε τσέλο ως παιδί;", ["Γιατί δεν της άρεσε η μουσική", "Γιατί οι γονείς της έλεγαν ότι είναι ακριβό και ογκώδες", "Γιατί δεν υπήρχε δάσκαλος", "Γιατί προτιμούσε το πιάνο"], 1, "οι γονείς μου έλεγαν ότι είναι ακριβό και ογκώδες"),
  Q("Τι της είπε ο δάσκαλός της;", ["Ότι είναι πολύ αργά για να μάθει", "Ότι οι ενήλικες ξέρουν γιατί μαθαίνουν", "Ότι πρέπει να αγοράσει δικό της τσέλο", "Ότι τα παιδιά δεν μαθαίνουν τσέλο"], 1, "οι ενήλικες ξέρουν γιατί μαθαίνουν"),
  Q("Πώς έχει αλλάξει η στάση του σκύλου της;", ["Γαβγίζει όταν παίζει", "Ξαπλώνει δίπλα της όταν κάνει εξάσκηση", "Φεύγει ακόμα από το δωμάτιο", "Κοιμάται στη θήκη του τσέλου"], 1, "ο σκύλος, πλέον, ξαπλώνει δίπλα μου όταν κάνω εξάσκηση"),
 ],
 "gloss": {"τσέλο": "τσέλο — cello", "ογκώδες": "ογκώδης — bulky", "ωδείο": "ωδείο — music school, conservatory", "απογοητευτικοί": "απογοητευτικός — disheartening", "δοξάρι": "δοξάρι — bow (of a string instrument)", "φάλτσες": "φάλτσος — out of tune", "θήκη": "θήκη — case", "ερασιτεχνική ορχήστρα": "ερασιτεχνική ορχήστρα — amateur orchestra", "εξάσκηση": "εξάσκηση — practice"},
})
ITEMS.append({
 "id": "l81-mono-grammata-kratoumeno", "title": "Γράμματα σε έναν κρατούμενο", "title_en": "Letters to a prisoner", "type": "monologue", "level": "B2",
 "context_el": "Σε μια εκπομπή για τον εθελοντισμό, ο Νίκος μιλά για την αλληλογραφία του με έναν κρατούμενο, μέσα από ένα πρόγραμμα μιας μη κυβερνητικής οργάνωσης.",
 "script": [
  L("Νίκος", "m", "Πριν από δύο χρόνια είδα μια ανακοίνωση από μια οργάνωση που έψαχνε εθελοντές για να γράφουν γράμματα σε κρατούμενους που δεν έχουν κανέναν να τους επισκέπτεται. Δίστασα πολύ. Αναρωτιόμουν τι θα μπορούσα να πω σε έναν άγνωστο που βρίσκεται στη φυλακή.", "Two years ago I saw a notice from an organisation looking for volunteers to write letters to prisoners who have no one to visit them. I hesitated a lot. I wondered what I could say to a stranger who is in prison."),
  L("Νίκος", "m", "Η οργάνωση μάς έδωσε κάποιους κανόνες: δεν ρωτάμε ποτέ για το αδίκημα, δεν δίνουμε τη διεύθυνση του σπιτιού μας, και τα γράμματα περνούν πρώτα από τα γραφεία της. Στο πρώτο μου γράμμα έγραψα για τον καιρό, για ένα βιβλίο που διάβαζα και για τη γάτα μου. Ήταν αμήχανο.", "The organisation gave us some rules: we never ask about the offence, we don't give our home address, and the letters go through its offices first. In my first letter I wrote about the weather, a book I was reading and my cat. It was awkward."),
  L("Νίκος", "m", "Η απάντηση ήρθε μετά από τρεις εβδομάδες, τέσσερις σελίδες με προσεγμένα γράμματα. Ο Θανάσης, έτσι λέγεται, μου έγραψε ότι ήταν το πρώτο γράμμα που έπαιρνε εδώ και έξι χρόνια. Από τότε γράφουμε ο ένας στον άλλον κάθε μήνα. Έχει αρχίσει να τελειώνει το λύκειο μέσα στη φυλακή, και μου στέλνει τις εκθέσεις του να τις διαβάσω.", "The reply came three weeks later: four pages in careful handwriting. Thanasis, that's his name, wrote that it was the first letter he had received in six years. Since then we've written to each other every month. He has started finishing secondary school in prison, and he sends me his essays to read."),
 ],
 "questions": [
  Q("Τι ψάχνει η οργάνωση;", ["Δικηγόρους για κρατούμενους", "Εθελοντές για να γράφουν γράμματα σε κρατούμενους", "Δασκάλους για τη φυλακή", "Δωρεές βιβλίων"], 1, "έψαχνε εθελοντές για να γράφουν γράμματα σε κρατούμενους"),
  Q("Ποιος από τους παρακάτω είναι κανόνας της οργάνωσης;", ["Να γράφουν κάθε εβδομάδα", "Να μη ρωτούν ποτέ για το αδίκημα", "Να επισκέπτονται τον κρατούμενο", "Να γράφουν μόνο στα αγγλικά"], 1, "δεν ρωτάμε ποτέ για το αδίκημα"),
  Q("Τι έγραψε ο Θανάσης στην πρώτη του απάντηση;", ["Ότι θα αποφυλακιστεί σύντομα", "Ότι ήταν το πρώτο γράμμα που έπαιρνε εδώ και έξι χρόνια", "Ότι δεν ήθελε να ξαναγράψει", "Ότι του αρέσουν οι γάτες"], 1, "ήταν το πρώτο γράμμα που έπαιρνε εδώ και έξι χρόνια"),
 ],
 "gloss": {"κρατούμενο": "κρατούμενος — prisoner, inmate", "αλληλογραφία": "αλληλογραφία — correspondence", "μη κυβερνητικής οργάνωσης": "μη κυβερνητική οργάνωση — NGO", "Δίστασα": "διστάζω — to hesitate", "φυλακή": "φυλακή — prison", "αδίκημα": "αδίκημα — offence, crime", "αμήχανο": "αμήχανος — awkward", "προσεγμένα": "προσεγμένος — careful, neat", "λύκειο": "λύκειο — upper secondary school", "εκθέσεις": "έκθεση — essay"},
})
ITEMS.append({
 "id": "l81-c1-fagito-aeroplano", "title": "Γιατί το φαγητό στο αεροπλάνο είναι άνοστο;", "title_en": "Why does airline food taste bland?", "type": "interview", "level": "C1",
 "context_el": "Σε μια επιστημονική εκπομπή, η δημοσιογράφος συζητά με έναν ερευνητή της επιστήμης των τροφίμων για τη γεύση στα αεροπλάνα και για το γιατί το φαγητό εκεί μοιάζει άνοστο.",
 "script": [
  L("Δημοσιογράφος", "f", "Όλοι γκρινιάζουμε για το φαγητό στο αεροπλάνο. Είναι πράγματι χειρότερο ή είναι ιδέα μας;", "We all grumble about airline food. Is it really worse, or is it just us?"),
  L("Ερευνητής", "m", "Και τα δύο, θα έλεγα. Στην καμπίνα, η πίεση είναι χαμηλότερη και ο αέρας εξαιρετικά ξηρός, πιο ξηρός από τον αέρα της ερήμου. Η μύτη στεγνώνει, και, επειδή ένα μεγάλο μέρος αυτού που λέμε γεύση είναι στην πραγματικότητα όσφρηση, η αντίληψη του αλμυρού και του γλυκού μειώνεται αισθητά, σύμφωνα με ορισμένες μετρήσεις κατά περίπου ένα τρίτο.", "Both, I would say. In the cabin, the pressure is lower and the air is extremely dry, drier than desert air. The nose dries out, and because a large part of what we call taste is actually smell, the perception of salty and sweet drops noticeably, according to some measurements by about a third."),
  L("Δημοσιογράφος", "f", "Και ο θόρυβος;", "And the noise?"),
  L("Ερευνητής", "m", "Παίζει κι αυτός ρόλο. Πειράματα έχουν δείξει ότι ο συνεχής θόρυβος των κινητήρων αμβλύνει την αίσθηση του γλυκού. Παραδόξως, η γεύση ουμάμι, αυτή που βρίσκουμε στην ντομάτα ή στην παρμεζάνα, φαίνεται να επηρεάζεται πολύ λιγότερο ή και να ενισχύεται. Ίσως γι’ αυτό τόσοι επιβάτες παραγγέλνουν χυμό ντομάτας στο αεροπλάνο, ενώ στο έδαφος δεν θα τον άγγιζαν ποτέ.", "It plays a part too. Experiments have shown that the constant noise of the engines dulls the sense of sweetness. Paradoxically, the umami taste, the one we find in tomato or parmesan, seems to be affected much less, or even enhanced. Perhaps that's why so many passengers order tomato juice on a plane when on the ground they'd never touch it."),
  L("Δημοσιογράφος", "f", "Τι κάνουν οι αεροπορικές εταιρείες γι’ αυτό;", "What do airlines do about it?"),
  L("Ερευνητής", "m", "Οι σεφ που σχεδιάζουν τα μενού προσθέτουν περισσότερο αλάτι και μπαχαρικά, προτιμούν σάλτσες που κρατούν την υγρασία, και επιλέγουν υλικά πλούσια σε ουμάμι, όπως τα μανιτάρια. Δοκιμάζουν μάλιστα τα πιάτα σε ειδικούς θαλάμους που αναπαράγουν τις συνθήκες της πτήσης. Το φαγητό που σε ένα εστιατόριο θα σας φαινόταν υπερβολικά αλμυρό, στα δέκα χιλιάδες μέτρα μπορεί να είναι σωστό.", "The chefs who design the menus add more salt and spices, prefer sauces that retain moisture, and choose ingredients rich in umami, such as mushrooms. They even test the dishes in special chambers that reproduce flight conditions. Food that would seem too salty to you in a restaurant may be just right at ten thousand metres."),
 ],
 "questions": [
  Q("Γιατί μειώνεται η αντίληψη του αλμυρού και του γλυκού στην καμπίνα;", ["Γιατί το φαγητό είναι κατεψυγμένο", "Γιατί η χαμηλή πίεση και ο ξηρός αέρας στεγνώνουν τη μύτη", "Γιατί οι επιβάτες είναι κουρασμένοι", "Γιατί η καμπίνα είναι κρύα"], 1, "Η μύτη στεγνώνει"),
  Q("Ποια γεύση φαίνεται να επηρεάζεται λιγότερο;", ["Το γλυκό", "Το ουμάμι", "Το αλμυρό", "Το ξινό"], 1, "η γεύση ουμάμι, αυτή που βρίσκουμε στην ντομάτα ή στην παρμεζάνα, φαίνεται να επηρεάζεται πολύ λιγότερο"),
  Q("Πού δοκιμάζουν τα πιάτα οι σεφ;", ["Σε κανονικές πτήσεις", "Σε ειδικούς θαλάμους που αναπαράγουν τις συνθήκες της πτήσης", "Σε εστιατόρια του αεροδρομίου", "Σε ομάδες επιβατών"], 1, "Δοκιμάζουν μάλιστα τα πιάτα σε ειδικούς θαλάμους που αναπαράγουν τις συνθήκες της πτήσης"),
 ],
 "gloss": {"άνοστο": "άνοστος — bland, tasteless", "γκρινιάζουμε": "γκρινιάζω — to grumble", "πίεση": "πίεση — pressure", "ξηρός": "ξηρός — dry", "ερήμου": "έρημος — desert", "όσφρηση": "όσφρηση — sense of smell", "αισθητά": "αισθητά — noticeably", "κινητήρων": "κινητήρας — engine", "αμβλύνει": "αμβλύνω — to dull, blunt", "ουμάμι": "ουμάμι — umami", "μπαχαρικά": "μπαχαρικό — spice", "θαλάμους": "θάλαμος — chamber", "αναπαράγουν": "αναπαράγω — to reproduce"},
})
ITEMS.append({
 "id": "l81-c1-filodorima", "title": "Το φιλοδώρημα: ευγένεια ή υποχρέωση;", "title_en": "Tipping: courtesy or obligation?", "type": "monologue", "level": "C1",
 "context_el": "Σε μια ραδιοφωνική εκπομπή για την καθημερινή ζωή, μια κοινωνιολόγος μιλά για το φιλοδώρημα.",
 "script": [
  L("Κοινωνιολόγος", "f", "Στην Ελλάδα, το φιλοδώρημα ήταν για δεκαετίες μια διακριτική υπόθεση. Αφήναμε τα ψιλά στο πιατάκι ή λέγαμε στον σερβιτόρο «κρατήστε τα ρέστα», χωρίς να υπολογίζουμε ποσοστά. Ήταν μια χειρονομία ευγένειας, όχι ένα ποσό που όφειλες.", "In Greece, tipping was for decades a discreet affair. We left the small change on the saucer or told the waiter 'keep the change', without calculating percentages. It was a gesture of courtesy, not an amount you owed."),
  L("Κοινωνιολόγος", "f", "Τα τελευταία χρόνια, με την εξάπλωση των πληρωμών με κάρτα, αυτό αλλάζει. Τα τερματικά σε πολλά καταστήματα προτείνουν πλέον έτοιμα ποσοστά, δέκα, δεκαπέντε, είκοσι τοις εκατό, και ο πελάτης νιώθει ότι πρέπει να διαλέξει μπροστά στο βλέμμα του υπαλλήλου. Αυτή η κοινωνική πίεση μοιάζει περισσότερο με το αμερικανικό μοντέλο, όπου το φιλοδώρημα αποτελεί στην ουσία μέρος του μισθού.", "In recent years, with the spread of card payments, this is changing. In many shops the terminals now suggest ready-made percentages, ten, fifteen, twenty per cent, and the customer feels he has to choose under the employee's gaze. This social pressure looks more like the American model, where the tip is essentially part of the wage."),
  L("Κοινωνιολόγος", "f", "Το ερώτημα, λοιπόν, δεν είναι μόνο πόσα αφήνουμε, αλλά ποιος πληρώνει τελικά τον εργαζόμενο. Όταν ο μισθός βασίζεται στη γενναιοδωρία του πελάτη, η αβεβαιότητα μεταφέρεται από τον εργοδότη στον σερβιτόρο. Ίσως η πιο ευγενική χειρονομία να μην είναι ένα μεγαλύτερο φιλοδώρημα, αλλά ένας δίκαιος μισθός που θα το κάνει ξανά προαιρετικό.", "The question, then, is not only how much we leave, but who ultimately pays the worker. When the wage depends on the customer's generosity, the uncertainty is shifted from the employer to the waiter. Perhaps the most courteous gesture is not a bigger tip, but a fair wage that would make it optional again."),
 ],
 "questions": [
  Q("Πώς περιγράφει η κοινωνιολόγος το παραδοσιακό φιλοδώρημα στην Ελλάδα;", ["Ως υποχρεωτικό ποσοστό", "Ως διακριτική χειρονομία ευγένειας", "Ως μέρος του μισθού", "Ως κάτι που δεν υπήρχε"], 1, "Ήταν μια χειρονομία ευγένειας, όχι ένα ποσό που όφειλες"),
  Q("Τι αλλάζει με τις πληρωμές με κάρτα;", ["Τα φιλοδωρήματα καταργούνται", "Τα τερματικά προτείνουν έτοιμα ποσοστά και ο πελάτης νιώθει πίεση", "Οι σερβιτόροι παίρνουν μεγαλύτερο μισθό", "Οι πελάτες δίνουν λιγότερα"], 1, "Τα τερματικά σε πολλά καταστήματα προτείνουν πλέον έτοιμα ποσοστά"),
  Q("Ποιο είναι το συμπέρασμα της ομιλήτριας;", ["Πρέπει να αφήνουμε πάντα είκοσι τοις εκατό", "Ένας δίκαιος μισθός θα έκανε το φιλοδώρημα ξανά προαιρετικό", "Το αμερικανικό μοντέλο είναι το καλύτερο", "Το φιλοδώρημα πρέπει να απαγορευτεί"], 1, "ένας δίκαιος μισθός που θα το κάνει ξανά προαιρετικό"),
 ],
 "gloss": {"φιλοδώρημα": "φιλοδώρημα — tip, gratuity", "διακριτική": "διακριτικός — discreet", "ψιλά": "ψιλά — small change", "ρέστα": "ρέστα — change (money)", "ποσοστά": "ποσοστό — percentage", "χειρονομία": "χειρονομία — gesture", "όφειλες": "οφείλω — to owe", "εξάπλωση": "εξάπλωση — spread", "τερματικά": "τερματικό — (card) terminal", "γενναιοδωρία": "γενναιοδωρία — generosity", "εργοδότη": "εργοδότης — employer", "προαιρετικό": "προαιρετικός — optional"},
})

rnd = random.Random(81)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-81.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
