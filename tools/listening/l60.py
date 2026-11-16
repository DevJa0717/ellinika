# Source for library/listening/listening-60.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l60.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l60-ann-diodia", "title": "Ηλεκτρονικά διόδια στον αυτοκινητόδρομο", "title_en": "Electronic tolls on the motorway", "type": "announcement", "level": "B2",
 "context_el": "Οδηγείτε σε έναν αυτοκινητόδρομο και ακούτε τον ραδιοφωνικό σταθμό της εταιρείας που τον διαχειρίζεται.",
 "script": [
  L("Ανακοίνωση", "m", "Αγαπητοί οδηγοί, σας ενημερώνουμε ότι από την πρώτη του επόμενου μήνα στους σταθμούς διοδίων της Ελευσίνας και της Κορίνθου θα λειτουργούν μόνο ηλεκτρονικές λωρίδες για τα αυτοκίνητα που διαθέτουν πομποδέκτη. Οι λωρίδες αυτές σημαίνονται με πράσινο χρώμα και το σύμβολο του πομποδέκτη.", "Dear drivers, we inform you that from the first of next month, at the Elefsina and Corinth toll stations, there will be electronic-only lanes for cars that have a transponder. These lanes are marked in green with the transponder symbol."),
  L("Ανακοίνωση", "m", "Όσοι δεν έχουν πομποδέκτη θα συνεχίσουν να πληρώνουν με μετρητά ή με κάρτα στις υπόλοιπες λωρίδες. Παρακαλούμε να επιλέγετε έγκαιρα τη σωστή λωρίδα και να μην αλλάζετε απότομα πορεία λίγο πριν από τον σταθμό.", "Those without a transponder will continue to pay in cash or by card in the other lanes. Please choose the right lane in good time and do not change course abruptly just before the station."),
  L("Ανακοίνωση", "m", "Για τον επόμενο μήνα, όσοι αποκτήσουν πομποδέκτη από τα σημεία εξυπηρέτησης της εταιρείας θα έχουν δέκα τοις εκατό έκπτωση σε όλες τις διελεύσεις. Καλό ταξίδι.", "For the next month, anyone who gets a transponder from the company's service points will have ten per cent off all passages. Have a good journey."),
 ],
 "questions": [
  Q("Ποιοι μπορούν να χρησιμοποιούν τις πράσινες λωρίδες;", ["Όλα τα αυτοκίνητα", "Μόνο τα αυτοκίνητα με πομποδέκτη", "Μόνο τα φορτηγά", "Όσοι πληρώνουν με κάρτα"], 1, "μόνο ηλεκτρονικές λωρίδες για τα αυτοκίνητα που διαθέτουν πομποδέκτη"),
  Q("Τι ζητούν από τους οδηγούς;", ["Να μειώσουν την ταχύτητα στο μισό", "Να επιλέγουν έγκαιρα τη σωστή λωρίδα", "Να έχουν μαζί τους μετρητά", "Να ανάβουν τα φώτα"], 1, "να επιλέγετε έγκαιρα τη σωστή λωρίδα και να μην αλλάζετε απότομα πορεία"),
  Q("Ποια προσφορά ανακοινώνεται;", ["Δωρεάν διελεύσεις για έναν μήνα", "Δέκα τοις εκατό έκπτωση για όσους αποκτήσουν πομποδέκτη", "Δωρεάν πομποδέκτης", "Έκπτωση για πληρωμές με μετρητά"], 1, "θα έχουν δέκα τοις εκατό έκπτωση σε όλες τις διελεύσεις"),
 ],
 "gloss": {"διοδίων": "διόδια — tolls", "λωρίδες": "λωρίδα — lane", "πομποδέκτη": "πομποδέκτης — transponder", "σημαίνονται": "σημαίνομαι — to be marked", "μετρητά": "μετρητά — cash", "έγκαιρα": "έγκαιρα — in good time", "πορεία": "πορεία — course, direction", "διελεύσεις": "διέλευση — passage"},
})

ITEMS.append({
 "id": "l60-vm-ktimatologio", "title": "Μήνυμα από το Κτηματολόγιο", "title_en": "A message from the Land Registry", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε δηλώσει ένα χωράφι που κληρονομήσατε στο Κτηματολόγιο. Θα ακούσετε ένα μήνυμα από μια υπάλληλο στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "f", "Καλησπέρα σας, κύριε Αργυρόπουλε, σας τηλεφωνώ από το γραφείο Κτηματολογίου της Τρίπολης, σχετικά με τη δήλωση που κάνατε για το χωράφι στη Βυτίνα. Ελέγξαμε τα έγγραφα και διαπιστώσαμε ότι λείπει το τοπογραφικό διάγραμμα, χωρίς το οποίο δεν μπορούμε να καταχωρίσουμε τα όρια του ακινήτου.", "Good afternoon, Mr Argyropoulos, I'm calling from the Land Registry office in Tripoli about the declaration you made for the field in Vytina. We checked the documents and found that the topographical plan is missing, without which we can't register the boundaries of the property."),
  L("Υπάλληλος", "f", "Επίσης, στο συμβόλαιο αποδοχής κληρονομιάς η έκταση αναγράφεται τέσσερα στρέμματα, ενώ στους χάρτες μας εμφανίζεται κάτι λιγότερο από τρία. Θα χρειαστεί να το διευκρινίσουμε, ίσως με τη βοήθεια ενός μηχανικού.", "Also, in the deed of acceptance of inheritance the area is given as four stremmata, while on our maps it appears as a little under three. We'll need to clarify this, perhaps with the help of an engineer."),
  L("Υπάλληλος", "f", "Μπορείτε να στείλετε το διάγραμμα ηλεκτρονικά, μέσα από την πλατφόρμα, μέχρι το τέλος του μήνα. Για ό,τι χρειαστείτε, είμαι στο γραφείο κάθε πρωί. Ευχαριστώ.", "You can send the plan electronically, through the platform, by the end of the month. For anything you need, I'm in the office every morning. Thank you."),
 ],
 "questions": [
  Q("Ποιο έγγραφο λείπει;", ["Η ταυτότητα", "Το τοπογραφικό διάγραμμα", "Το συμβόλαιο", "Η φορολογική δήλωση"], 1, "λείπει το τοπογραφικό διάγραμμα"),
  Q("Ποιο πρόβλημα υπάρχει με την έκταση του χωραφιού;", ["Ανήκει σε άλλον ιδιοκτήτη", "Στο συμβόλαιο αναγράφεται μεγαλύτερη έκταση από ό,τι στους χάρτες", "Δεν υπάρχει στους χάρτες", "Είναι δασική έκταση"], 1, "στο συμβόλαιο ... η έκταση αναγράφεται τέσσερα στρέμματα, ενώ στους χάρτες μας εμφανίζεται κάτι λιγότερο από τρία"),
  Q("Πώς μπορεί να στείλει το διάγραμμα;", ["Μόνο με το ταχυδρομείο", "Ηλεκτρονικά, μέσα από την πλατφόρμα", "Με φαξ", "Πρέπει να το φέρει αυτοπροσώπως"], 1, "Μπορείτε να στείλετε το διάγραμμα ηλεκτρονικά, μέσα από την πλατφόρμα"),
 ],
 "gloss": {"Κτηματολογίου": "Κτηματολόγιο — Land Registry", "χωράφι": "χωράφι — field", "τοπογραφικό διάγραμμα": "τοπογραφικό διάγραμμα — topographical plan", "καταχωρίσουμε": "καταχωρίζω — to register, enter", "όρια": "όριο — boundary", "ακινήτου": "ακίνητο — property", "αποδοχής κληρονομιάς": "αποδοχή κληρονομιάς — acceptance of an inheritance", "στρέμματα": "στρέμμα — stremma (1,000 m²)", "διευκρινίσουμε": "διευκρινίζω — to clarify"},
})

ITEMS.append({
 "id": "l60-dia-ofthalmiatros", "title": "Στον οφθαλμίατρο", "title_en": "At the eye doctor's", "type": "dialogue", "level": "B2",
 "context_el": "Μια γυναίκα επισκέπτεται έναν οφθαλμίατρο γιατί δεν βλέπει καλά. Θα ακούσετε τη συζήτησή τους.",
 "script": [
  L("Ασθενής", "f", "Γιατρέ μου, τους τελευταίους μήνες δυσκολεύομαι να διαβάσω τα μικρά γράμματα, ιδίως το βράδυ. Κρατάω το κινητό όλο και πιο μακριά από τα μάτια μου.", "Doctor, in recent months I've had trouble reading small print, especially in the evening. I hold my phone further and further from my eyes."),
  L("Οφθαλμίατρος", "m", "Πόσων χρονών είστε, αν επιτρέπεται; Σαράντα πέντε; Τότε είναι μάλλον πρεσβυωπία, κάτι απολύτως φυσιολογικό σε αυτή την ηλικία. Ο φακός του ματιού χάνει σιγά σιγά την ελαστικότητά του και δυσκολεύεται να εστιάσει από κοντά. Ας κάνουμε όμως πρώτα έναν πλήρη έλεγχο.", "How old are you, if I may ask? Forty-five? Then it's probably presbyopia, something completely normal at this age. The lens of the eye gradually loses its elasticity and finds it hard to focus close up. But let's first do a full check-up."),
  L("Ασθενής", "f", "Δηλαδή θα χρειαστώ γυαλιά; Δεν έχω φορέσει ποτέ στη ζωή μου.", "So I'll need glasses? I've never worn any in my life."),
  L("Οφθαλμίατρος", "m", "Πιθανότατα γυαλιά για κοντινή απόσταση, μόνο για το διάβασμα. Θα σας βάλω και σταγόνες για να διαστείλω την κόρη, ώστε να εξετάσω τον βυθό του ματιού. Για δυο τρεις ώρες θα βλέπετε θολά και θα σας ενοχλεί το φως, οπότε μην οδηγήσετε μετά.", "Most likely glasses for close range, just for reading. I'll also put in drops to dilate the pupil, so I can examine the back of the eye. For two or three hours you'll see blurred and light will bother you, so don't drive afterwards."),
  L("Ασθενής", "f", "Ευτυχώς ήρθα με το μετρό. Και πρέπει να ξαναέρθω;", "Luckily I came by metro. And do I have to come back?"),
  L("Οφθαλμίατρος", "m", "Από εδώ και πέρα, ένας έλεγχος τον χρόνο είναι αρκετός. Μετά τα σαράντα, καλό είναι να μετράμε και την πίεση του ματιού, για να προλάβουμε το γλαύκωμα.", "From now on, one check-up a year is enough. After forty, it's good to measure the eye pressure too, to catch glaucoma early."),
 ],
 "questions": [
  Q("Τι πρόβλημα έχει η ασθενής;", ["Βλέπει θολά από μακριά", "Δυσκολεύεται να διαβάσει τα μικρά γράμματα", "Την πονάνε τα μάτια", "Βλέπει διπλά"], 1, "δυσκολεύομαι να διαβάσω τα μικρά γράμματα, ιδίως το βράδυ"),
  Q("Γιατί δεν πρέπει να οδηγήσει μετά την εξέταση;", ["Γιατί θα κουραστεί", "Γιατί οι σταγόνες θα την κάνουν να βλέπει θολά", "Γιατί θα φοράει καινούργια γυαλιά", "Γιατί θα πάρει φάρμακο"], 1, "θα βλέπετε θολά και θα σας ενοχλεί το φως, οπότε μην οδηγήσετε μετά"),
  Q("Γιατί είναι καλό να μετράει την πίεση του ματιού;", ["Για να προλάβει το γλαύκωμα", "Για να αλλάξει γυαλιά", "Για να μη χρειαστεί επέμβαση", "Για να κοιμάται καλύτερα"], 0, "για να προλάβουμε το γλαύκωμα"),
 ],
 "gloss": {"οφθαλμίατρο": "οφθαλμίατρος — eye doctor", "πρεσβυωπία": "πρεσβυωπία — presbyopia, long-sightedness with age", "ελαστικότητά": "ελαστικότητα — elasticity", "εστιάσει": "εστιάζω — to focus", "σταγόνες": "σταγόνα — drop", "διαστείλω": "διαστέλλω — to dilate", "κόρη": "κόρη (του ματιού) — pupil", "βυθό": "βυθός (του ματιού) — back of the eye", "θολά": "θολά — blurred", "γλαύκωμα": "γλαύκωμα — glaucoma"},
})

ITEMS.append({
 "id": "l60-dia-forema", "title": "Ένα φόρεμα για τον γάμο", "title_en": "A dress for the wedding", "type": "dialogue", "level": "B2",
 "context_el": "Μια νεαρή γυναίκα θέλει να νοικιάσει ένα φόρεμα για έναν γάμο. Θα ακούσετε τη συζήτησή της με την υπάλληλο ενός καταστήματος ενοικίασης ρούχων.",
 "script": [
  L("Ιφιγένεια", "f", "Καλημέρα. Είμαι καλεσμένη σε έναν γάμο τον άλλο μήνα και δεν θέλω να αγοράσω ακριβό φόρεμα που θα φορέσω μία φορά. Μια φίλη μου είπε ότι εδώ νοικιάζετε.", "Good morning. I'm invited to a wedding next month and I don't want to buy an expensive dress I'll wear once. A friend told me you rent here."),
  L("Υπάλληλος", "f", "Ακριβώς. Έχουμε φορέματα σχεδιαστών σε ένα μικρό κλάσμα της τιμής τους. Η ενοικίαση κρατάει τέσσερις μέρες και περιλαμβάνει το στεγνό καθάρισμα. Ο γάμος είναι πρωινός ή βραδινός;", "Exactly. We have designer dresses at a small fraction of their price. The rental lasts four days and includes dry cleaning. Is the wedding in the morning or the evening?"),
  L("Ιφιγένεια", "f", "Βραδινός, σε ένα κτήμα έξω από τη Θεσσαλονίκη. Και η νύφη μάς παρακάλεσε να μη φορέσουμε λευκό ούτε μαύρο.", "Evening, at an estate outside Thessaloniki. And the bride asked us not to wear white or black."),
  L("Υπάλληλος", "f", "Τότε σας προτείνω αυτό το σμαραγδί μακρύ, ή το μπορντό με την ανοιχτή πλάτη. Αν χρειαστεί μικρή μεταποίηση, π.χ. στο μήκος, την κάνουμε εμείς χωρίς επιβάρυνση.", "Then I'd suggest this long emerald one, or the burgundy with the open back. If a small alteration is needed, for example to the length, we do it ourselves at no extra charge."),
  L("Ιφιγένεια", "f", "Το σμαραγδί μού αρέσει πολύ. Τι γίνεται αν πάθει κάποια ζημιά; Αν χυθεί κρασί, ας πούμε;", "I really like the emerald one. What happens if it gets damaged? If wine is spilled, say?"),
  L("Υπάλληλος", "f", "Οι μικροί λεκέδες καλύπτονται από την ασφάλεια που περιλαμβάνεται στην τιμή. Για σκισίματα ή μεγάλες ζημιές, κρατάμε μέρος της εγγύησης. Μπορείτε να το δοκιμάσετε τώρα και να το κλείσουμε για τις ημερομηνίες σας.", "Small stains are covered by the insurance included in the price. For tears or major damage, we keep part of the deposit. You can try it on now and we'll book it for your dates."),
 ],
 "questions": [
  Q("Γιατί θέλει η Ιφιγένεια να νοικιάσει φόρεμα;", ["Γιατί δεν βρίσκει το νούμερό της", "Γιατί δεν θέλει να αγοράσει ακριβό φόρεμα για μία φορά", "Γιατί της το ζήτησε η νύφη", "Γιατί είναι της μόδας"], 1, "δεν θέλω να αγοράσω ακριβό φόρεμα που θα φορέσω μία φορά"),
  Q("Τι ζήτησε η νύφη από τις καλεσμένες;", ["Να φορέσουν μακριά φορέματα", "Να μη φορέσουν λευκό ούτε μαύρο", "Να φορέσουν πράσινο", "Να έρθουν νωρίς"], 1, "η νύφη μάς παρακάλεσε να μη φορέσουμε λευκό ούτε μαύρο"),
  Q("Τι γίνεται αν το φόρεμα λερωθεί λίγο;", ["Πληρώνει ολόκληρη την τιμή", "Οι μικροί λεκέδες καλύπτονται από την ασφάλεια", "Πρέπει να το καθαρίσει η ίδια", "Χάνει όλη την εγγύηση"], 1, "καλύπτονται από την ασφάλεια που περιλαμβάνεται στην τιμή"),
 ],
 "gloss": {"καλεσμένη": "καλεσμένος — invited, guest", "σχεδιαστών": "σχεδιαστής — designer", "κλάσμα": "κλάσμα — fraction", "στεγνό καθάρισμα": "στεγνό καθάρισμα — dry cleaning", "κτήμα": "κτήμα — estate", "σμαραγδί": "σμαραγδί — emerald green", "μπορντό": "μπορντό — burgundy", "μεταποίηση": "μεταποίηση — alteration", "επιβάρυνση": "επιβάρυνση — extra charge", "σκισίματα": "σκίσιμο — tear"},
})

ITEMS.append({
 "id": "l60-int-koudounas", "title": "Ο τεχνίτης των κουδουνιών", "title_en": "The bell maker", "type": "interview", "level": "B2",
 "context_el": "Σε μια εκπομπή για τα παραδοσιακά επαγγέλματα, η δημοσιογράφος μιλά με έναν τεχνίτη που φτιάχνει κουδούνια για ζώα σε ένα χωριό της Ηπείρου.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Βαγγέλη, για ποιον φτιάχνετε σήμερα κουδούνια;", "Mr Vangelis, who do you make bells for today?"),
  L("Τεχνίτης", "m", "Κυρίως για κτηνοτρόφους, που τα κρεμάνε στα πρόβατα και στις κατσίκες. Ο βοσκός αναγνωρίζει από τον ήχο πού βρίσκεται το κοπάδι του, ακόμη κι όταν δεν το βλέπει μέσα στην ομίχλη. Κάθε κουδούνι έχει τη δική του φωνή, και ένα καλό κοπάδι ακούγεται σαν ορχήστρα.", "Mainly for herders, who hang them on sheep and goats. The shepherd recognises from the sound where his flock is, even when he can't see it in the fog. Every bell has its own voice, and a good flock sounds like an orchestra."),
  L("Δημοσιογράφος", "f", "Και πώς δίνετε σε κάθε κουδούνι τη φωνή του;", "And how do you give each bell its voice?"),
  L("Τεχνίτης", "m", "Με το σφυρί και με το αυτί. Κόβω τη λαμαρίνα, τη διπλώνω, και μετά τη χτυπάω ξανά και ξανά, ώσπου να βγάλει τον ήχο που θέλω. Στο τέλος τη βάφω με μπρούντζο και την ψήνω στο καμίνι. Αυτό το μυστικό μού το έμαθε ο πατέρας μου, κι εκείνος από τον δικό του.", "With the hammer and with the ear. I cut the sheet metal, fold it, and then strike it again and again until it gives the sound I want. At the end I coat it with brass and fire it in the kiln. My father taught me that secret, and he learned it from his."),
  L("Δημοσιογράφος", "f", "Έχει μέλλον αυτή η τέχνη;", "Does this craft have a future?"),
  L("Τεχνίτης", "m", "Τα κοπάδια λιγοστεύουν, αλλά τώρα με βρίσκουν και άλλοι πελάτες: μουσικοί, που βάζουν τα κουδούνια στα έργα τους, και οι ομάδες που ντύνονται κουδουνάτοι στα καρναβάλια. Όσο υπάρχουν αυτοί, η φωνή του βουνού δεν θα σβήσει.", "Flocks are dwindling, but now other customers find me too: musicians, who put the bells in their works, and the groups who dress up as bell-wearers at carnivals. As long as they exist, the voice of the mountain won't die out."),
 ],
 "questions": [
  Q("Γιατί χρειάζονται τα κουδούνια οι βοσκοί;", ["Για να διώχνουν τους λύκους", "Για να αναγνωρίζουν από τον ήχο πού βρίσκεται το κοπάδι", "Για διακόσμηση", "Για να ξυπνούν το πρωί"], 1, "Ο βοσκός αναγνωρίζει από τον ήχο πού βρίσκεται το κοπάδι του"),
  Q("Πώς δίνει ο τεχνίτης τον ήχο σε κάθε κουδούνι;", ["Με ένα μηχάνημα", "Χτυπώντας το με το σφυρί ώσπου να βγάλει τον ήχο που θέλει", "Αλλάζοντας το μέγεθός του", "Βάφοντάς το"], 1, "τη χτυπάω ξανά και ξανά, ώσπου να βγάλει τον ήχο που θέλω"),
  Q("Ποιοι νέοι πελάτες τον βρίσκουν;", ["Ξενοδοχεία", "Μουσικοί και ομάδες κουδουνάτων στα καρναβάλια", "Σχολεία", "Τουρίστες από το εξωτερικό"], 1, "μουσικοί ... και οι ομάδες που ντύνονται κουδουνάτοι στα καρναβάλια"),
 ],
 "gloss": {"κουδούνια": "κουδούνι — bell", "κτηνοτρόφους": "κτηνοτρόφος — livestock farmer, herder", "κοπάδι": "κοπάδι — flock", "ομίχλη": "ομίχλη — fog", "σφυρί": "σφυρί — hammer", "λαμαρίνα": "λαμαρίνα — sheet metal", "καμίνι": "καμίνι — kiln, furnace", "λιγοστεύουν": "λιγοστεύω — to dwindle", "κουδουνάτοι": "κουδουνάτος — carnival bell-wearer"},
})

ITEMS.append({
 "id": "l60-rep-tatoi", "title": "Το κτήμα του Τατοΐου", "title_en": "The Tatoi estate", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από ένα ιστορικό κτήμα στις παρυφές της Αθήνας.",
 "script": [
  L("Ρεπόρτερ", "m", "Βρισκόμαστε στο Τατόι, στους πρόποδες της Πάρνηθας, μόλις είκοσι πέντε χιλιόμετρα από το κέντρο της Αθήνας. Εδώ, για σχεδόν έναν αιώνα, βρισκόταν η θερινή κατοικία της βασιλικής οικογένειας. Το κτήμα, με τα δάση, τα ανάκτορα, τους στάβλους και το βασιλικό κοιμητήριο, περιήλθε οριστικά στο ελληνικό δημόσιο στις αρχές της δεκαετίας του 2000.", "We're at Tatoi, at the foot of Mount Parnitha, just twenty-five kilometres from the centre of Athens. Here, for almost a century, was the summer residence of the royal family. The estate, with its forests, palace, stables and royal cemetery, passed definitively to the Greek state in the early 2000s."),
  L("Ρεπόρτερ", "m", "Για χρόνια το κτήμα έμεινε εγκαταλειμμένο. Τα κτίρια ερήμωσαν, και πολλά αντικείμενα κινδύνευαν από την υγρασία. Τα τελευταία χρόνια, όμως, ξεκίνησε ένα μεγάλο πρόγραμμα αποκατάστασης. Ορισμένα κτίρια έχουν ήδη αναπαλαιωθεί, και χιλιάδες αντικείμενα, από έπιπλα μέχρι άμαξες, καταγράφονται και συντηρούνται.", "For years the estate was left abandoned. The buildings fell into ruin and many objects were at risk from damp. In recent years, however, a large restoration programme has begun. Some buildings have already been restored, and thousands of objects, from furniture to carriages, are being catalogued and conserved."),
  L("Ρεπόρτερ", "m", "Το πάρκο είναι ήδη ανοιχτό στο κοινό, και τα Σαββατοκύριακα γεμίζει οικογένειες που κάνουν περίπατο ή ποδήλατο ανάμεσα στα πεύκα. Ο στόχος είναι, όταν ολοκληρωθούν οι εργασίες, να λειτουργήσουν εδώ μουσεία και πολιτιστικοί χώροι, ώστε το Τατόι να γίνει ένας ζωντανός τόπος ιστορίας και πρασίνου.", "The park is already open to the public, and at weekends it fills with families walking or cycling among the pines. The aim is that, when the work is finished, museums and cultural spaces will operate here, so that Tatoi becomes a living place of history and greenery."),
 ],
 "questions": [
  Q("Τι ήταν το Τατόι για σχεδόν έναν αιώνα;", ["Στρατιωτική βάση", "Η θερινή κατοικία της βασιλικής οικογένειας", "Ένα μοναστήρι", "Ένα αγρόκτημα του δήμου"], 1, "βρισκόταν η θερινή κατοικία της βασιλικής οικογένειας"),
  Q("Τι γίνεται τα τελευταία χρόνια στο κτήμα;", ["Πουλήθηκε σε ιδιώτες", "Ξεκίνησε ένα μεγάλο πρόγραμμα αποκατάστασης", "Χτίστηκε ξενοδοχείο", "Έκλεισε για το κοινό"], 1, "ξεκίνησε ένα μεγάλο πρόγραμμα αποκατάστασης"),
  Q("Ποιος είναι ο στόχος όταν ολοκληρωθούν οι εργασίες;", ["Να γίνει κατοικία του προέδρου", "Να λειτουργήσουν μουσεία και πολιτιστικοί χώροι", "Να κοπούν τα πεύκα", "Να γίνει γήπεδο γκολφ"], 1, "να λειτουργήσουν εδώ μουσεία και πολιτιστικοί χώροι"),
 ],
 "gloss": {"κτήμα": "κτήμα — estate", "παρυφές": "παρυφές — outskirts", "θερινή": "θερινός — summer", "ανάκτορα": "ανάκτορο — palace", "κοιμητήριο": "κοιμητήριο — cemetery", "περιήλθε": "περιέρχομαι — to pass (to someone)", "ερήμωσαν": "ερημώνω — to become deserted, fall into ruin", "αναπαλαιωθεί": "αναπαλαιώνω — to restore (an old building)", "άμαξες": "άμαξα — carriage"},
})

ITEMS.append({
 "id": "l60-dia-katoikidio", "title": "Ένας σκύλος στο διαμέρισμα", "title_en": "A dog in the flat", "type": "dialogue", "level": "B2",
 "context_el": "Ένας νεαρός ενοικιαστής μιλά με τη διαχειρίστρια της πολυκατοικίας του, γιατί θέλει να υιοθετήσει έναν σκύλο. Θα ακούσετε τη συζήτησή τους.",
 "script": [
  L("Στέφανος", "m", "Κυρία Λένα, καλημέρα. Θα ήθελα να σας ρωτήσω κάτι. Σκέφτομαι να υιοθετήσω ένα σκυλάκι από ένα φιλοζωικό σωματείο. Υπάρχει κάποιο πρόβλημα με τον κανονισμό της πολυκατοικίας;", "Mrs Lena, good morning. I'd like to ask you something. I'm thinking of adopting a little dog from an animal welfare society. Is there any problem with the building's rules?"),
  L("Διαχειρίστρια", "f", "Καλημέρα, Στέφανε. Ο νόμος δεν επιτρέπει πια στον κανονισμό να απαγορεύει τα κατοικίδια στα διαμερίσματα, οπότε δεν μπορεί κανείς να σας εμποδίσει. Υπάρχουν όμως κάποιοι κανόνες καλής γειτονίας.", "Good morning, Stefanos. The law no longer allows building rules to ban pets in flats, so nobody can stop you. But there are some rules of good neighbourliness."),
  L("Στέφανος", "m", "Φυσικά. Τι πρέπει να προσέξω;", "Of course. What should I be careful about?"),
  L("Διαχειρίστρια", "f", "Πρώτον, στους κοινόχρηστους χώρους, στην είσοδο και στο ασανσέρ, ο σκύλος πρέπει να είναι πάντα με λουρί. Δεύτερον, το γάβγισμα. Ο κύριος Σπύρος στον δεύτερο δουλεύει νύχτα και κοιμάται τα πρωινά. Αν το σκυλάκι μένει μόνο του όλη μέρα και γαβγίζει, θα έχουμε παράπονα.", "First, in the common areas, the entrance and the lift, the dog must always be on a lead. Second, barking. Mr Spyros on the second floor works nights and sleeps in the mornings. If the dog stays alone all day and barks, we'll have complaints."),
  L("Στέφανος", "m", "Δουλεύω από το σπίτι τις περισσότερες μέρες, οπότε δεν θα μένει πολύ μόνο του. Και θα το βγάζω βόλτα τρεις φορές τη μέρα.", "I work from home most days, so it won't be alone much. And I'll take it for a walk three times a day."),
  L("Διαχειρίστρια", "f", "Τότε δεν βλέπω κανένα πρόβλημα. Α, και να μαζεύετε πάντα τις ακαθαρσίες στον δρόμο. Η κυρία Ρούλα στο ισόγειο έχει κάνει θέμα τα λουλούδια της!", "Then I don't see any problem. Oh, and always pick up the mess in the street. Mrs Roula on the ground floor has made an issue of her flowers!"),
 ],
 "questions": [
  Q("Μπορεί ο κανονισμός της πολυκατοικίας να απαγορεύσει τον σκύλο;", ["Ναι, αν το αποφασίσουν οι ένοικοι", "Όχι, ο νόμος δεν το επιτρέπει πια", "Ναι, μόνο για μεγάλους σκύλους", "Μόνο αν το ζητήσει η διαχειρίστρια"], 1, "Ο νόμος δεν επιτρέπει πια στον κανονισμό να απαγορεύει τα κατοικίδια στα διαμερίσματα"),
  Q("Γιατί ανησυχεί η διαχειρίστρια για το γάβγισμα;", ["Γιατί υπάρχουν μωρά στην πολυκατοικία", "Γιατί ο κύριος Σπύρος δουλεύει νύχτα και κοιμάται τα πρωινά", "Γιατί η κυρία Ρούλα φοβάται τα σκυλιά", "Γιατί οι τοίχοι είναι λεπτοί"], 1, "Ο κύριος Σπύρος στον δεύτερο δουλεύει νύχτα και κοιμάται τα πρωινά"),
  Q("Γιατί ο Στέφανος πιστεύει ότι ο σκύλος δεν θα γαβγίζει πολύ;", ["Γιατί θα πάρει ήσυχη ράτσα", "Γιατί δουλεύει από το σπίτι τις περισσότερες μέρες", "Γιατί θα τον εκπαιδεύσει", "Γιατί θα μένει στο μπαλκόνι"], 1, "Δουλεύω από το σπίτι τις περισσότερες μέρες"),
 ],
 "gloss": {"υιοθετήσω": "υιοθετώ — to adopt", "φιλοζωικό σωματείο": "φιλοζωικό σωματείο — animal welfare society", "κανονισμό": "κανονισμός — rules, regulations", "κατοικίδια": "κατοικίδιο — pet", "κοινόχρηστους χώρους": "κοινόχρηστοι χώροι — common areas", "λουρί": "λουρί — lead, leash", "γάβγισμα": "γάβγισμα — barking", "ακαθαρσίες": "ακαθαρσίες — mess, droppings"},
})

ITEMS.append({
 "id": "l60-mono-rouxa", "title": "Ένας χρόνος χωρίς καινούργια ρούχα", "title_en": "A year without new clothes", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν άντρα να μιλά σε μια εκδήλωση για την κατανάλωση για ένα πείραμα που έκανε.",
 "script": [
  L("Ομιλητής", "m", "Πριν από δύο χρόνια άνοιξα την ντουλάπα μου και μέτρησα τριάντα δύο μπλουζάκια. Τα μισά δεν τα είχα φορέσει ούτε μία φορά τον τελευταίο χρόνο. Τότε αποφάσισα να περάσω έναν ολόκληρο χρόνο χωρίς να αγοράσω κανένα καινούργιο ρούχο, εκτός από εσώρουχα και κάλτσες.", "Two years ago I opened my wardrobe and counted thirty-two T-shirts. Half of them I hadn't worn even once in the past year. Then I decided to spend a whole year without buying any new clothes, except underwear and socks."),
  L("Ομιλητής", "m", "Οι πρώτοι μήνες ήταν οι πιο δύσκολοι. Συνειδητοποίησα πόσο συχνά αγόραζα από βαρεμάρα ή για να φτιάξω τη διάθεσή μου. Όταν κάτι χαλούσε, έμαθα να το επιδιορθώνω: έραψα κουμπιά, μπάλωσα ένα τζιν, και πήγα για πρώτη φορά σε τσαγκάρη για να αλλάξω σόλες.", "The first months were the hardest. I realised how often I bought out of boredom or to cheer myself up. When something broke, I learned to repair it: I sewed buttons, patched a pair of jeans and went to a cobbler for the first time to have soles replaced."),
  L("Ομιλητής", "m", "Στο τέλος του χρόνου είχα εξοικονομήσει περίπου οχτακόσια ευρώ, αλλά το σημαντικότερο ήταν άλλο: σταμάτησα να ορίζω τον εαυτό μου από το τι φοράω. Κανείς, παρεμπιπτόντως, δεν πρόσεξε ότι φορούσα τα ίδια ρούχα. Οι άλλοι, τελικά, μας κοιτάζουν πολύ λιγότερο απ’ όσο νομίζουμε.", "At the end of the year I had saved about eight hundred euros, but the most important thing was something else: I stopped defining myself by what I wear. Nobody, incidentally, noticed that I wore the same clothes. Other people, in the end, look at us much less than we think."),
 ],
 "questions": [
  Q("Τι τον έκανε να ξεκινήσει το πείραμα;", ["Μια συμβουλή φίλου", "Ότι τα μισά μπλουζάκια του δεν τα είχε φορέσει τον τελευταίο χρόνο", "Ένα ντοκιμαντέρ", "Οικονομικά προβλήματα"], 1, "Τα μισά δεν τα είχα φορέσει ούτε μία φορά τον τελευταίο χρόνο"),
  Q("Τι συνειδητοποίησε τους πρώτους μήνες;", ["Ότι δεν του άρεσαν τα ρούχα του", "Ότι αγόραζε συχνά από βαρεμάρα ή για να φτιάξει τη διάθεσή του", "Ότι χρειαζόταν περισσότερα ρούχα", "Ότι τα ρούχα του ήταν παλιά"], 1, "πόσο συχνά αγόραζα από βαρεμάρα ή για να φτιάξω τη διάθεσή μου"),
  Q("Ποιο ήταν, κατά τον ομιλητή, το σημαντικότερο αποτέλεσμα;", ["Τα χρήματα που εξοικονόμησε", "Ότι σταμάτησε να ορίζει τον εαυτό του από τα ρούχα του", "Ότι έμαθε να ράβει", "Ότι οι φίλοι του τον θαύμασαν"], 1, "σταμάτησα να ορίζω τον εαυτό μου από το τι φοράω"),
 ],
 "gloss": {"ντουλάπα": "ντουλάπα — wardrobe", "μπλουζάκια": "μπλουζάκι — T-shirt", "βαρεμάρα": "βαρεμάρα — boredom", "επιδιορθώνω": "επιδιορθώνω — to repair", "μπάλωσα": "μπαλώνω — to patch", "τσαγκάρη": "τσαγκάρης — cobbler", "σόλες": "σόλα — sole", "ορίζω": "ορίζω — to define", "παρεμπιπτόντως": "παρεμπιπτόντως — incidentally"},
})

ITEMS.append({
 "id": "l60-c1-kalodia", "title": "Τα υποβρύχια καλώδια του διαδικτύου", "title_en": "The internet's undersea cables", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την τεχνολογία, η δημοσιογράφος συζητά με έναν μηχανικό τηλεπικοινωνιών για την υποδομή του διαδικτύου.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Σαρρή, οι περισσότεροι φανταζόμαστε ότι το διαδίκτυο ταξιδεύει μέσω δορυφόρων. Ισχύει;", "Mr Sarris, most of us imagine that the internet travels via satellites. Is that true?"),
  L("Μηχανικός", "m", "Είναι μια πολύ διαδεδομένη παρανόηση. Στην πραγματικότητα, πάνω από το ενενήντα πέντε τοις εκατό της διηπειρωτικής κίνησης δεδομένων περνά από καλώδια οπτικών ινών, απλωμένα στον βυθό των ωκεανών. Πρόκειται για καλώδια όχι πολύ χοντρότερα από έναν σωλήνα ποτίσματος, που όμως μεταφέρουν τεράστιο όγκο πληροφορίας με την ταχύτητα του φωτός. Οι δορυφόροι είναι χρήσιμοι για απομακρυσμένες περιοχές, αλλά δεν μπορούν να ανταγωνιστούν τη χωρητικότητα των καλωδίων.", "It's a very widespread misconception. In reality, over ninety-five per cent of intercontinental data traffic passes through fibre-optic cables laid on the ocean floor. They are cables not much thicker than a garden hose, which nevertheless carry a huge volume of information at the speed of light. Satellites are useful for remote areas, but they can't compete with the capacity of cables."),
  L("Δημοσιογράφος", "f", "Και η Ελλάδα; Τι ρόλο παίζει σε αυτό το δίκτυο;", "And Greece? What role does it play in this network?"),
  L("Μηχανικός", "m", "Όλο και πιο σημαντικό. Η γεωγραφική της θέση, ανάμεσα στην Ευρώπη, την Ασία και την Αφρική, την καθιστά φυσικό κόμβο. Αρκετά νέα καλώδια που συνδέουν την Ευρώπη με τη Μέση Ανατολή και την Ινδία προσγειώνονται ή σχεδιάζεται να προσγειωθούν σε ελληνικές ακτές, κυρίως στην Κρήτη. Αυτό σημαίνει επενδύσεις σε κέντρα δεδομένων, αλλά και μια νέα γεωπολιτική βαρύτητα.", "Increasingly important. Its geographical position, between Europe, Asia and Africa, makes it a natural hub. Several new cables linking Europe with the Middle East and India land, or are planned to land, on Greek shores, mainly in Crete. That means investment in data centres, but also a new geopolitical weight."),
  L("Δημοσιογράφος", "f", "Είναι ευάλωτα αυτά τα καλώδια;", "Are these cables vulnerable?"),
  L("Μηχανικός", "m", "Περισσότερο απ’ όσο θα θέλαμε. Οι περισσότερες βλάβες οφείλονται σε άγκυρες πλοίων και σε αλιευτικά εργαλεία, όχι σε δολιοφθορές. Ωστόσο, τα τελευταία χρόνια έχουν καταγραφεί περιστατικά που προκαλούν ανησυχία, και γι’ αυτό η προστασία των καλωδίων έχει γίνει ζήτημα εθνικής ασφάλειας. Η επισκευή, πάντως, είναι εντυπωσιακή: ειδικά πλοία ανασύρουν το καλώδιο από βάθος χιλιάδων μέτρων, το επιδιορθώνουν στο κατάστρωμα και το ξαναβυθίζουν.", "More than we'd like. Most faults are caused by ships' anchors and fishing gear, not sabotage. However, in recent years there have been incidents that cause concern, which is why protecting cables has become a matter of national security. Repair, though, is impressive: special ships haul the cable up from a depth of thousands of metres, mend it on deck and sink it again."),
 ],
 "questions": [
  Q("Ποια «παρανόηση» διορθώνει ο μηχανικός;", ["Ότι το διαδίκτυο είναι δωρεάν", "Ότι το διαδίκτυο ταξιδεύει κυρίως μέσω δορυφόρων", "Ότι τα καλώδια είναι πολύ χοντρά", "Ότι οι δορυφόροι είναι άχρηστοι"], 1, "οι περισσότεροι φανταζόμαστε ότι το διαδίκτυο ταξιδεύει μέσω δορυφόρων ... Είναι μια πολύ διαδεδομένη παρανόηση"),
  Q("Γιατί η Ελλάδα αποτελεί φυσικό κόμβο;", ["Λόγω του μεγάλου πληθυσμού της", "Λόγω της γεωγραφικής της θέσης ανάμεσα σε τρεις ηπείρους", "Γιατί έχει πολλούς δορυφόρους", "Γιατί κατασκευάζει καλώδια"], 1, "Η γεωγραφική της θέση, ανάμεσα στην Ευρώπη, την Ασία και την Αφρική, την καθιστά φυσικό κόμβο"),
  Q("Πού οφείλονται οι περισσότερες βλάβες στα καλώδια;", ["Σε δολιοφθορές", "Σε άγκυρες πλοίων και αλιευτικά εργαλεία", "Σε σεισμούς", "Σε καρχαρίες"], 1, "Οι περισσότερες βλάβες οφείλονται σε άγκυρες πλοίων και σε αλιευτικά εργαλεία"),
  Q("Πώς επισκευάζεται ένα υποβρύχιο καλώδιο;", ["Με δύτες στον βυθό", "Το ανασύρουν ειδικά πλοία, το επιδιορθώνουν στο κατάστρωμα και το ξαναβυθίζουν", "Αντικαθίσταται ολόκληρο", "Με ρομπότ που μένουν μόνιμα στον βυθό"], 1, "ειδικά πλοία ανασύρουν το καλώδιο ... το επιδιορθώνουν στο κατάστρωμα και το ξαναβυθίζουν"),
 ],
 "gloss": {"παρανόηση": "παρανόηση — misconception", "διηπειρωτικής": "διηπειρωτικός — intercontinental", "οπτικών ινών": "οπτική ίνα — optical fibre", "χωρητικότητα": "χωρητικότητα — capacity", "κόμβο": "κόμβος — hub, node", "κέντρα δεδομένων": "κέντρο δεδομένων — data centre", "άγκυρες": "άγκυρα — anchor", "δολιοφθορές": "δολιοφθορά — sabotage", "ανασύρουν": "ανασύρω — to haul up", "κατάστρωμα": "κατάστρωμα — deck"},
})

ITEMS.append({
 "id": "l60-c1-lozani", "title": "Η Συνθήκη της Λωζάνης", "title_en": "The Treaty of Lausanne", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από διάλεξη ιστορικού για μια συνθήκη που διαμόρφωσε τα σύνορα της σύγχρονης Ελλάδας.",
 "script": [
  L("Ιστορικός", "m", "Μετά τη Μικρασιατική Καταστροφή του 1922, η Ελλάδα προσήλθε στις διαπραγματεύσεις της Λωζάνης ηττημένη και εξαντλημένη, με ένα κύμα προσφύγων να κατακλύζει τις πόλεις της. Επικεφαλής της ελληνικής αντιπροσωπείας ήταν ο Ελευθέριος Βενιζέλος, που, αν και εκτός κυβέρνησης, θεωρήθηκε ο μόνος ικανός να υπερασπιστεί τα ελληνικά συμφέροντα.", "After the Asia Minor Catastrophe of 1922, Greece came to the Lausanne negotiations defeated and exhausted, with a wave of refugees flooding its cities. The head of the Greek delegation was Eleftherios Venizelos, who, although out of government, was considered the only person able to defend Greek interests."),
  L("Ιστορικός", "m", "Η συνθήκη, που υπογράφηκε τον Ιούλιο του 1923, καθόρισε τα σύνορα ανάμεσα στην Ελλάδα και την Τουρκία, τα οποία, με εξαίρεση τα Δωδεκάνησα, ισχύουν μέχρι σήμερα. Η Ανατολική Θράκη, η Ίμβρος και η Τένεδος έμειναν στην Τουρκία. Ήδη από τον Ιανουάριο είχε υπογραφεί η σύμβαση για την υποχρεωτική ανταλλαγή των πληθυσμών, την πρώτη τέτοιας κλίμακας στη σύγχρονη ιστορία. Εξαιρέθηκαν οι Έλληνες της Κωνσταντινούπολης και οι μουσουλμάνοι της Δυτικής Θράκης.", "The treaty, signed in July 1923, fixed the borders between Greece and Turkey, which, with the exception of the Dodecanese, remain in force to this day. Eastern Thrace, Imbros and Tenedos remained with Turkey. Already in January the convention on the compulsory exchange of populations had been signed, the first of such a scale in modern history. The Greeks of Constantinople and the Muslims of Western Thrace were exempted."),
  L("Ιστορικός", "m", "Η αποτίμηση της Λωζάνης παραμένει αμφιλεγόμενη. Για πολλούς πρόσφυγες ήταν η οριστική απώλεια των πατρογονικών εστιών. Από την άλλη πλευρά, η συνθήκη έκλεισε έναν κύκλο δεκαετιών πολέμων και επέτρεψε στην Ελλάδα να αφιερωθεί στο τεράστιο έργο της αποκατάστασης των προσφύγων, που, παρά τις δυσκολίες, μεταμόρφωσε την οικονομία, την κοινωνία και τον πολιτισμό της χώρας.", "The assessment of Lausanne remains controversial. For many refugees it was the definitive loss of their ancestral homes. On the other hand, the treaty closed a cycle of decades of wars and allowed Greece to devote itself to the enormous task of resettling the refugees, which, despite the difficulties, transformed the country's economy, society and culture."),
 ],
 "questions": [
  Q("Σε τι κατάσταση βρισκόταν η Ελλάδα στις διαπραγματεύσεις;", ["Νικήτρια και ισχυρή", "Ηττημένη και εξαντλημένη", "Ουδέτερη", "Σε εμφύλιο πόλεμο"], 1, "η Ελλάδα προσήλθε στις διαπραγματεύσεις της Λωζάνης ηττημένη και εξαντλημένη"),
  Q("Γιατί ο Βενιζέλος ηγήθηκε της αντιπροσωπείας, αν και ήταν εκτός κυβέρνησης;", ["Γιατί ζούσε στη Λωζάνη", "Γιατί θεωρήθηκε ο μόνος ικανός να υπερασπιστεί τα ελληνικά συμφέροντα", "Γιατί το ζήτησαν οι Μεγάλες Δυνάμεις", "Γιατί ήταν ο νέος βασιλιάς"], 1, "θεωρήθηκε ο μόνος ικανός να υπερασπιστεί τα ελληνικά συμφέροντα"),
  Q("Ποιοι εξαιρέθηκαν από την ανταλλαγή των πληθυσμών;", ["Οι κάτοικοι της Κρήτης", "Οι Έλληνες της Κωνσταντινούπολης και οι μουσουλμάνοι της Δυτικής Θράκης", "Οι κάτοικοι των Δωδεκανήσων", "Όλοι οι κάτοικοι της Θράκης"], 1, "Εξαιρέθηκαν οι Έλληνες της Κωνσταντινούπολης και οι μουσουλμάνοι της Δυτικής Θράκης"),
  Q("Ποια θετική συνέπεια της συνθήκης αναφέρει ο ομιλητής;", ["Η Ελλάδα κέρδισε τη Σμύρνη", "Έκλεισε έναν κύκλο πολέμων και η χώρα αφιερώθηκε στην αποκατάσταση των προσφύγων", "Οι πρόσφυγες επέστρεψαν στα σπίτια τους", "Η Τουρκία πλήρωσε αποζημιώσεις"], 1, "η συνθήκη έκλεισε έναν κύκλο δεκαετιών πολέμων και επέτρεψε στην Ελλάδα να αφιερωθεί στο τεράστιο έργο της αποκατάστασης των προσφύγων"),
 ],
 "gloss": {"προσήλθε": "προσέρχομαι — to come, attend", "διαπραγματεύσεις": "διαπραγμάτευση — negotiation", "κατακλύζει": "κατακλύζω — to flood", "αντιπροσωπείας": "αντιπροσωπεία — delegation", "σύμβαση": "σύμβαση — convention, agreement", "ανταλλαγή των πληθυσμών": "ανταλλαγή πληθυσμών — population exchange", "Εξαιρέθηκαν": "εξαιρούμαι — to be exempted", "αποτίμηση": "αποτίμηση — assessment", "αμφιλεγόμενη": "αμφιλεγόμενος — controversial", "πατρογονικών εστιών": "πατρογονικές εστίες — ancestral homes"},
})

rnd = random.Random(60)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-60.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
