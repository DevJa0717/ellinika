# Source for library/listening/listening-16.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l16.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l16-ann-ploio", "title": "Καλώς ήρθατε στο πλοίο", "title_en": "Welcome aboard the ferry", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα ενός πλοίου, λίγο μετά την αναχώρηση από τον Πειραιά.",
 "script": [
  L("Εκφωνήτρια", "f", "Κυρίες και κύριοι, ο πλοίαρχος και το πλήρωμα σας καλωσορίζουν στο πλοίο. Η άφιξή μας στη Νάξο προβλέπεται στις δύο και μισή το μεσημέρι, με ενδιάμεσους σταθμούς τη Σύρο και την Πάρο.", "Ladies and gentlemen, the captain and crew welcome you aboard. Our arrival in Naxos is expected at half past two in the afternoon, with intermediate stops at Syros and Paros."),
  L("Εκφωνήτρια", "f", "Λόγω των ισχυρών ανέμων, παρακαλούνται οι επιβάτες να μην παραμένουν στο ανοιχτό κατάστρωμα της πλώρης και να κρατούν τα παιδιά κοντά τους. Το εστιατόριο και το κυλικείο βρίσκονται στο πέμπτο κατάστρωμα και λειτουργούν σε όλη τη διάρκεια του ταξιδιού.", "Because of the strong winds, passengers are asked not to remain on the open bow deck and to keep children close to them. The restaurant and snack bar are on deck five and are open throughout the voyage."),
  L("Εκφωνήτρια", "f", "Οι επιβάτες με αυτοκίνητο παρακαλούνται να μην κατεβαίνουν στο γκαράζ πριν από την ανακοίνωση για την αποβίβαση. Οι κάτοχοι καμπίνας μπορούν να παραλάβουν το κλειδί τους από τη ρεσεψιόν, στο έκτο κατάστρωμα. Σας ευχόμαστε καλό ταξίδι.", "Passengers with cars are asked not to go down to the garage before the disembarkation announcement. Cabin holders can collect their key from reception, on deck six. We wish you a pleasant voyage."),
 ],
 "questions": [
  Q("Σε ποια νησιά θα σταματήσει το πλοίο πριν από τη Νάξο;", ["Στη Μύκονο και στην Τήνο", "Στη Σύρο και στην Πάρο", "Στην Πάρο και στην Αντίπαρο", "Πουθενά, πηγαίνει κατευθείαν"], 1, "με ενδιάμεσους σταθμούς τη Σύρο και την Πάρο"),
  Q("Γιατί δεν πρέπει να μένουν οι επιβάτες στο κατάστρωμα της πλώρης;", ["Γιατί γίνονται εργασίες", "Λόγω των ισχυρών ανέμων", "Γιατί είναι μόνο για το πλήρωμα", "Γιατί βρέχει"], 1, "Λόγω των ισχυρών ανέμων"),
  Q("Πού παραλαμβάνουν οι επιβάτες το κλειδί της καμπίνας;", ["Στο γκαράζ", "Στο κυλικείο", "Στη ρεσεψιόν, στο έκτο κατάστρωμα", "Από τον πλοίαρχο"], 2, "από τη ρεσεψιόν, στο έκτο κατάστρωμα"),
 ],
 "gloss": {"μεγάφωνα": "μεγάφωνο — loudspeaker", "αναχώρηση": "αναχώρηση — departure", "πλοίαρχος": "πλοίαρχος — captain", "πλήρωμα": "πλήρωμα — crew", "ενδιάμεσους σταθμούς": "ενδιάμεσος σταθμός — intermediate stop", "ισχυρών ανέμων": "ισχυρός άνεμος — strong wind", "κατάστρωμα": "κατάστρωμα — deck", "πλώρης": "πλώρη — bow (of a ship)", "κυλικείο": "κυλικείο — snack bar", "αποβίβαση": "αποβίβαση — disembarkation", "καμπίνας": "καμπίνα — cabin"},
})

ITEMS.append({
 "id": "l16-vm-paidikos", "title": "Θέση στον παιδικό σταθμό", "title_en": "A place at the nursery", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα από έναν δημοτικό παιδικό σταθμό προς έναν πατέρα.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα, κύριε Νικολάου, σας καλούμε από τον δεύτερο δημοτικό παιδικό σταθμό. Σας ενημερώνουμε ότι η αίτησή σας εγκρίθηκε και η κόρη σας, η Ελπίδα, μπορεί να ξεκινήσει από την πρώτη Δεκεμβρίου.", "Good morning, Mr Nikolaou, we're calling from the second municipal nursery. We're letting you know that your application has been approved and your daughter, Elpida, can start from the first of December."),
  L("Υπάλληλος", "f", "Για να ολοκληρωθεί η εγγραφή, θα πρέπει να μας φέρετε ως την Παρασκευή το βιβλιάριο υγείας της με τα εμβόλια και μια βεβαίωση από τον παιδίατρο ότι μπορεί να παρακολουθήσει ομαδικό χώρο. Χωρίς αυτά τα δύο, δυστυχώς, η θέση θα δοθεί στο επόμενο παιδί της λίστας.", "To complete the registration, you'll need to bring us by Friday her health booklet with her vaccinations and a certificate from the paediatrician that she can attend a group setting. Without these two, unfortunately, the place will go to the next child on the list."),
  L("Υπάλληλος", "f", "Τις πρώτες μέρες προτείνουμε η μικρή να μένει μόνο δύο ώρες, για να προσαρμοστεί σιγά σιγά. Αν έχετε απορίες, είμαστε εδώ καθημερινά από τις επτά το πρωί ως τις τέσσερις.", "For the first few days we suggest the little one stays only two hours, so she can adjust gradually. If you have any questions, we're here every day from seven in the morning until four."),
 ],
 "questions": [
  Q("Τι είναι το καλό νέο του μηνύματος;", ["Ότι η αίτηση εγκρίθηκε", "Ότι ο σταθμός θα είναι δωρεάν", "Ότι ο σταθμός μετακομίζει", "Ότι άλλαξε το ωράριο"], 0, "η αίτησή σας εγκρίθηκε"),
  Q("Τι θα συμβεί αν ο πατέρας δεν φέρει τα έγγραφα ως την Παρασκευή;", ["Θα πληρώσει πρόστιμο", "Η θέση θα δοθεί σε άλλο παιδί", "Η κόρη του θα ξεκινήσει αργότερα", "Θα πρέπει να κάνει νέα αίτηση τον Ιανουάριο"], 1, "η θέση θα δοθεί στο επόμενο παιδί της λίστας"),
  Q("Τι προτείνει ο σταθμός για τις πρώτες μέρες;", ["Να έρθει και ο πατέρας στην τάξη", "Να μένει το παιδί μόνο δύο ώρες", "Να φέρει το παιδί ένα παιχνίδι από το σπίτι", "Να μη φάει εκεί το μεσημεριανό"], 1, "η μικρή να μένει μόνο δύο ώρες"),
 ],
 "gloss": {"παιδικό σταθμό": "παιδικός σταθμός — nursery, day care", "εγκρίθηκε": "εγκρίνομαι — to be approved", "να ολοκληρωθεί": "ολοκληρώνομαι — to be completed", "εγγραφή": "εγγραφή — registration, enrolment", "βιβλιάριο υγείας": "βιβλιάριο υγείας — (child's) health booklet", "εμβόλια": "εμβόλιο — vaccine, vaccination", "παιδίατρο": "παιδίατρος — paediatrician", "ομαδικό χώρο": "ομαδικός χώρος — group setting", "να προσαρμοστεί": "προσαρμόζομαι — to adjust, settle in", "απορίες": "απορία — question, query"},
})

ITEMS.append({
 "id": "l16-dia-kommotirio", "title": "Στο κομμωτήριο", "title_en": "At the hairdresser's", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα κομμωτήριο ανάμεσα σε μια πελάτισσα και τον κομμωτή.",
 "script": [
  L("Κομμωτής", "m", "Καλώς την! Τι θα κάνουμε σήμερα; Το ίδιο κούρεμα με την προηγούμενη φορά;", "Welcome! What are we doing today? The same cut as last time?"),
  L("Ρούλα", "f", "Όχι, θέλω μια αλλαγή. Σκεφτόμουν να τα κόψω αρκετά κοντά, ως τον σβέρκο, και να κάνω και λίγες ανταύγειες, γιατί έχουν αρχίσει να φαίνονται τα άσπρα.", "No, I want a change. I was thinking of cutting it quite short, to the nape, and having some highlights too, because the grey hairs are starting to show."),
  L("Κομμωτής", "m", "Καλή ιδέα. Με το σχήμα του προσώπου σου, ένα κοντό κούρεμα θα σου πάει πολύ. Μόνο να ξέρεις ότι οι ανταύγειες θέλουν περίπου δύο ώρες, και θα χρειαστεί να τις ανανεώνεις κάθε δύο μήνες.", "Good idea. With the shape of your face, a short cut will really suit you. Just so you know, highlights take about two hours, and you'll need to touch them up every two months."),
  L("Ρούλα", "f", "Δύο ώρες; Στις έξι πρέπει να πάρω το παιδί από το φροντιστήριο. Ας κάνουμε σήμερα μόνο το κούρεμα, και κλείνουμε ραντεβού για τις ανταύγειες το Σάββατο το πρωί.", "Two hours? At six I have to pick up my child from the tutoring school. Let's just do the cut today, and we'll book an appointment for the highlights on Saturday morning."),
 ],
 "questions": [
  Q("Τι θέλει αρχικά η Ρούλα;", ["Το ίδιο κούρεμα με την προηγούμενη φορά", "Κοντό κούρεμα και ανταύγειες", "Μόνο χτένισμα", "Να βάψει όλα τα μαλλιά της μαύρα"], 1, "να τα κόψω αρκετά κοντά, ως τον σβέρκο, και να κάνω και λίγες ανταύγειες"),
  Q("Τι λέει ο κομμωτής για τις ανταύγειες;", ["Ότι δεν της ταιριάζουν", "Ότι θέλουν δύο ώρες και ανανέωση κάθε δύο μήνες", "Ότι είναι πολύ ακριβές", "Ότι πρέπει να τις κάνει πριν από το κούρεμα"], 1, "οι ανταύγειες θέλουν περίπου δύο ώρες"),
  Q("Γιατί αναβάλλει η Ρούλα τις ανταύγειες;", ["Γιατί δεν έχει χρήματα", "Γιατί πρέπει να πάρει το παιδί της στις έξι", "Γιατί ο κομμωτής δεν έχει χρόνο", "Γιατί άλλαξε γνώμη"], 1, "Στις έξι πρέπει να πάρω το παιδί από το φροντιστήριο"),
 ],
 "gloss": {"κομμωτήριο": "κομμωτήριο — hairdresser's", "κομμωτή": "κομμωτής — hairdresser", "κούρεμα": "κούρεμα — haircut", "σβέρκο": "σβέρκος — nape of the neck", "ανταύγειες": "ανταύγειες — highlights (hair)", "τα άσπρα": "τα άσπρα — grey (white) hairs", "σχήμα του προσώπου": "σχήμα του προσώπου — face shape", "θα σου πάει": "μου πάει — it suits me", "να τις ανανεώνεις": "ανανεώνω — to renew, touch up", "φροντιστήριο": "φροντιστήριο — tutoring school (after-school classes)"},
})

ITEMS.append({
 "id": "l16-dia-eisitirio", "title": "Εισιτήριο με αυτοκίνητο", "title_en": "A ferry ticket with a car", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα πρακτορείο ακτοπλοϊκών εισιτηρίων.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Θα ήθελα δύο εισιτήρια για Χανιά, για την Παρασκευή το βράδυ, με αυτοκίνητο. Υπάρχει διαθεσιμότητα σε καμπίνα;", "Good morning. I'd like two tickets to Chania, for Friday night, with a car. Is there availability in a cabin?"),
  L("Υπάλληλος", "f", "Για την Παρασκευή οι δίκλινες καμπίνες έχουν τελειώσει, γιατί είναι τριήμερο. Μου έχουν μείνει μόνο τετράκλινες, που είναι αρκετά ακριβότερες, ή αεροπορικά καθίσματα. Αν μπορείτε να φύγετε την Πέμπτη, υπάρχουν ακόμη δίκλινες.", "For Friday the twin cabins are sold out, because it's a long weekend. I only have four-berth cabins left, which are quite a bit more expensive, or airline-style seats. If you can leave on Thursday, there are still twin cabins."),
  L("Πελάτης", "m", "Την Πέμπτη δεν γίνεται, δουλεύουμε και οι δύο. Πόσο κοστίζει η τετράκλινη; Και το αυτοκίνητο χρεώνεται ανάλογα με το μήκος;", "Thursday's not possible, we both work. How much is the four-berth cabin? And is the car charged according to its length?"),
  L("Υπάλληλος", "f", "Ναι, μέχρι τέσσερα και πέντε μέτρα είναι η κανονική τιμή. Η τετράκλινη για δύο άτομα βγαίνει περίπου εκατό ευρώ πιο ακριβά από τη δίκλινη. Αν κλείσετε και την επιστροφή τώρα, έχετε έκπτωση είκοσι τοις εκατό στο αυτοκίνητο.", "Yes, up to four and a half metres it's the standard price. The four-berth cabin for two people comes to about a hundred euros more than the twin. If you book the return now as well, you get twenty per cent off the car."),
 ],
 "questions": [
  Q("Γιατί δεν υπάρχουν δίκλινες καμπίνες την Παρασκευή;", ["Γιατί το πλοίο είναι μικρό", "Γιατί είναι τριήμερο", "Γιατί υπάρχει απεργία", "Γιατί το πλοίο δεν έχει καμπίνες"], 1, "γιατί είναι τριήμερο"),
  Q("Γιατί δεν μπορεί ο πελάτης να ταξιδέψει την Πέμπτη;", ["Γιατί δεν υπάρχουν εισιτήρια", "Γιατί δουλεύουν και οι δύο", "Γιατί το αυτοκίνητο είναι στο συνεργείο", "Γιατί είναι ακριβότερα"], 1, "δουλεύουμε και οι δύο"),
  Q("Πώς μπορεί να πάρει έκπτωση;", ["Αν πληρώσει μετρητά", "Αν κλείσει και την επιστροφή τώρα", "Αν ταξιδέψει χωρίς αυτοκίνητο", "Αν είναι φοιτητής"], 1, "Αν κλείσετε και την επιστροφή τώρα, έχετε έκπτωση"),
 ],
 "gloss": {"πρακτορείο": "πρακτορείο — (travel) agency", "ακτοπλοϊκών": "ακτοπλοϊκός — ferry (coastal shipping)", "διαθεσιμότητα": "διαθεσιμότητα — availability", "δίκλινες": "δίκλινος — twin, two-berth", "τριήμερο": "τριήμερο — long (three-day) weekend", "τετράκλινες": "τετράκλινος — four-berth", "αεροπορικά καθίσματα": "αεροπορικό κάθισμα — airline-style seat (on a ferry)", "χρεώνεται": "χρεώνομαι — to be charged", "μήκος": "μήκος — length", "επιστροφή": "επιστροφή — return (trip)"},
})

ITEMS.append({
 "id": "l16-mon-prosfyges", "title": "Μαθήματα ελληνικών για πρόσφυγες", "title_en": "Greek lessons for refugees", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια εθελόντρια να μιλάει για τα μαθήματα ελληνικών που κάνει σε πρόσφυγες.",
 "script": [
  L("Ευαγγελία", "f", "Εδώ και τρία χρόνια διδάσκω εθελοντικά ελληνικά σε ενήλικες πρόσφυγες, σε μια μη κυβερνητική οργάνωση στο κέντρο της Αθήνας. Οι μαθητές μου έρχονται από το Αφγανιστάν, τη Συρία, το Κονγκό, και μιλούν πολύ διαφορετικές γλώσσες.", "For three years I've been teaching Greek as a volunteer to adult refugees, at a non-governmental organisation in the centre of Athens. My students come from Afghanistan, Syria, the Congo, and speak very different languages."),
  L("Ευαγγελία", "f", "Το πιο δύσκολο στην αρχή είναι το αλφάβητο. Κάποιοι δεν έχουν πάει ποτέ σχολείο, ούτε στη δική τους γλώσσα, οπότε μαθαίνουν να γράφουν για πρώτη φορά. Άλλοι είναι μηχανικοί ή δάσκαλοι και προχωρούν πολύ γρήγορα. Γι' αυτό χωρίζουμε την τάξη σε μικρές ομάδες.", "The hardest thing at first is the alphabet. Some have never been to school, not even in their own language, so they are learning to write for the first time. Others are engineers or teachers and progress very quickly. That's why we split the class into small groups."),
  L("Ευαγγελία", "f", "Δεν διδάσκουμε μόνο γραμματική. Μαθαίνουμε πώς να κλείνουν ραντεβού στο νοσοκομείο, πώς να μιλούν στον εργοδότη, πώς να διαβάζουν έναν λογαριασμό. Η μεγαλύτερη χαρά μου ήταν όταν μια μαθήτρια, που στην αρχή δεν ήξερε ούτε να γράψει το όνομά της, μου έστειλε ένα μήνυμα στα ελληνικά για να μου πει ότι βρήκε δουλειά.", "We don't only teach grammar. We learn how to book appointments at the hospital, how to talk to an employer, how to read a bill. My greatest joy was when a student, who at first couldn't even write her name, sent me a message in Greek to tell me she had found a job."),
 ],
 "questions": [
  Q("Πού διδάσκει η Ευαγγελία;", ["Σε ένα δημόσιο σχολείο", "Σε μια μη κυβερνητική οργάνωση", "Στο πανεπιστήμιο", "Στο σπίτι της"], 1, "σε μια μη κυβερνητική οργάνωση στο κέντρο της Αθήνας"),
  Q("Γιατί χωρίζουν την τάξη σε μικρές ομάδες;", ["Γιατί η αίθουσα είναι μικρή", "Γιατί οι μαθητές έχουν πολύ διαφορετικό επίπεδο", "Γιατί μιλούν διαφορετικές γλώσσες", "Γιατί έρχονται σε διαφορετικές ώρες"], 1, "Γι' αυτό χωρίζουμε την τάξη σε μικρές ομάδες"),
  Q("Ποια ήταν η μεγαλύτερη χαρά της Ευαγγελίας;", ["Όταν πήρε μισθό", "Όταν μια μαθήτρια της έγραψε στα ελληνικά ότι βρήκε δουλειά", "Όταν οι μαθητές πέρασαν τις εξετάσεις", "Όταν η οργάνωση πήρε βραβείο"], 1, "μου έστειλε ένα μήνυμα στα ελληνικά για να μου πει ότι βρήκε δουλειά"),
 ],
 "gloss": {"εθελόντρια": "εθελόντρια — (female) volunteer", "πρόσφυγες": "πρόσφυγας — refugee", "εθελοντικά": "εθελοντικά — as a volunteer", "μη κυβερνητική οργάνωση": "μη κυβερνητική οργάνωση — non-governmental organisation (NGO)", "αλφάβητο": "αλφάβητο — alphabet", "μηχανικοί": "μηχανικός — engineer", "προχωρούν": "προχωρώ — to progress, move on", "χωρίζουμε": "χωρίζω — to split, divide", "εργοδότη": "εργοδότης — employer", "λογαριασμό": "λογαριασμός — bill"},
})

ITEMS.append({
 "id": "l16-rep-monemvasia", "title": "Μονεμβασιά, η πόλη στον βράχο", "title_en": "Monemvasia, the town on the rock", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ταξιδιωτικό ρεπορτάζ από τη Μονεμβασιά, στη Λακωνία.",
 "script": [
  L("Δημοσιογράφος", "f", "Από τη στεριά βλέπεις μόνο έναν τεράστιο βράχο μέσα στη θάλασσα. Η καστροπολιτεία κρύβεται στη νότια πλευρά του, και τη φτάνεις περνώντας μια στενή λωρίδα γης και μια μικρή γέφυρα. Από αυτή τη μοναδική είσοδο πήρε και το όνομά της: «μόνη εμβασία», δηλαδή μία μόνο είσοδος.", "From the mainland you see only a huge rock in the sea. The castle town is hidden on its southern side, and you reach it by crossing a narrow strip of land and a small bridge. It got its name from this single entrance: 'moni emvasia', meaning a single way in."),
  L("Δημοσιογράφος", "f", "Στα βυζαντινά χρόνια η Μονεμβασιά ήταν ένα από τα σημαντικότερα λιμάνια του Μοριά και εξήγαγε σε όλη την Ευρώπη ένα γλυκό κρασί, τη μαλβαζία. Μέσα στα τείχη δεν κυκλοφορούν αυτοκίνητα· τα υλικά για τις επισκευές μεταφέρονται ακόμη με γαϊδουράκια μέσα από τα λιθόστρωτα σοκάκια.", "In Byzantine times Monemvasia was one of the most important ports of the Morea and exported a sweet wine, malmsey, all over Europe. No cars circulate within the walls; materials for repairs are still carried by donkeys through the cobbled alleys."),
  L("Δημοσιογράφος", "f", "Στη Μονεμβασιά γεννήθηκε το 1909 ο ποιητής Γιάννης Ρίτσος, και το σπίτι του βρίσκεται στην είσοδο της παλιάς πόλης. Οι κάτοικοι λένε ότι τον χειμώνα, όταν φεύγουν οι τουρίστες, μένουν μέσα στα τείχη λιγότερα από είκοσι άτομα.", "The poet Yannis Ritsos was born in Monemvasia in 1909, and his house is at the entrance to the old town. Residents say that in winter, when the tourists leave, fewer than twenty people stay within the walls."),
 ],
 "questions": [
  Q("Από πού πήρε το όνομά της η Μονεμβασιά;", ["Από έναν βυζαντινό αυτοκράτορα", "Από τη μοναδική της είσοδο", "Από το κρασί της", "Από έναν άγιο"], 1, "Από αυτή τη μοναδική είσοδο πήρε και το όνομά της"),
  Q("Πώς μεταφέρονται τα υλικά για τις επισκευές μέσα στα τείχη;", ["Με μικρά φορτηγά", "Με βάρκες", "Με γαϊδουράκια", "Με ελικόπτερο"], 2, "μεταφέρονται ακόμη με γαϊδουράκια"),
  Q("Τι ισχύει τον χειμώνα, σύμφωνα με τους κατοίκους;", ["Η πόλη κλείνει εντελώς", "Μένουν μέσα στα τείχη λιγότερα από είκοσι άτομα", "Έρχονται περισσότεροι τουρίστες", "Γίνεται φεστιβάλ ποίησης"], 1, "μένουν μέσα στα τείχη λιγότερα από είκοσι άτομα"),
 ],
 "gloss": {"στεριά": "στεριά — mainland, dry land", "βράχο": "βράχος — rock", "καστροπολιτεία": "καστροπολιτεία — fortified (castle) town", "λωρίδα γης": "λωρίδα γης — strip of land", "εμβασία": "εμβασία — (old) entrance, way in", "Μοριά": "Μοριάς — the Morea (Peloponnese)", "εξήγαγε": "εξάγω — to export", "μαλβαζία": "μαλβαζία — malmsey (sweet wine)", "τείχη": "τείχος — (city) wall", "επισκευές": "επισκευή — repair", "γαϊδουράκια": "γαϊδουράκι — little donkey", "λιθόστρωτα σοκάκια": "λιθόστρωτο σοκάκι — cobbled alley"},
})

ITEMS.append({
 "id": "l16-rep-anadasosi", "title": "Μετά τη φωτιά", "title_en": "After the fire", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για μια εθελοντική δράση σε ένα δάσος που κάηκε.",
 "script": [
  L("Δημοσιογράφος", "m", "Δύο χρόνια μετά την πυρκαγιά, η πλαγιά είναι ακόμη γεμάτη μαυρισμένους κορμούς. Σήμερα το πρωί, όμως, περισσότεροι από εκατό εθελοντές, ανάμεσά τους πολλές οικογένειες με παιδιά, ήρθαν να βοηθήσουν τη δασική υπηρεσία.", "Two years after the fire, the slope is still full of blackened trunks. This morning, however, more than a hundred volunteers, among them many families with children, came to help the forest service."),
  L("Δασολόγος", "f", "Δεν φυτεύουμε όπου να 'ναι. Σε πολλά σημεία το δάσος αναγεννιέται μόνο του, γιατί τα κουκουνάρια της χαλεπίου πεύκης ανοίγουν με τη ζέστη και ρίχνουν σπόρους. Εκεί η καλύτερη βοήθεια είναι να προστατέψουμε την περιοχή από τη βόσκηση και την οικοδόμηση.", "We don't plant just anywhere. In many places the forest regenerates by itself, because the cones of the Aleppo pine open with the heat and drop seeds. There the best help is to protect the area from grazing and building."),
  L("Δημοσιογράφος", "m", "Οι εθελοντές φύτεψαν σήμερα βελανιδιές, κουμαριές και χαρουπιές, είδη που αντέχουν στην ξηρασία και καίγονται δυσκολότερα. Η δασική υπηρεσία θα ποτίζει τα δενδρύλλια όλο το πρώτο καλοκαίρι, την πιο κρίσιμη περίοδο για την επιβίωσή τους.", "Today the volunteers planted oaks, strawberry trees and carob trees, species that withstand drought and burn less easily. The forest service will water the saplings throughout the first summer, the most critical period for their survival."),
 ],
 "questions": [
  Q("Ποιοι ήρθαν να βοηθήσουν τη δασική υπηρεσία;", ["Μόνο στρατιώτες", "Πάνω από εκατό εθελοντές, ανάμεσά τους οικογένειες", "Μαθητές ενός σχολείου", "Οι πυροσβέστες της περιοχής"], 1, "περισσότεροι από εκατό εθελοντές, ανάμεσά τους πολλές οικογένειες με παιδιά"),
  Q("Γιατί σε πολλά σημεία δεν χρειάζεται φύτευση;", ["Γιατί το έδαφος είναι άγονο", "Γιατί το δάσος αναγεννιέται μόνο του", "Γιατί θα χτιστούν σπίτια", "Γιατί δεν υπάρχει νερό"], 1, "Σε πολλά σημεία το δάσος αναγεννιέται μόνο του"),
  Q("Γιατί διάλεξαν βελανιδιές, κουμαριές και χαρουπιές;", ["Γιατί μεγαλώνουν πολύ γρήγορα", "Γιατί αντέχουν στην ξηρασία και καίγονται δυσκολότερα", "Γιατί είναι φθηνές", "Γιατί δίνουν φρούτα"], 1, "είδη που αντέχουν στην ξηρασία και καίγονται δυσκολότερα"),
 ],
 "gloss": {"εθελοντική δράση": "εθελοντική δράση — volunteer action", "πλαγιά": "πλαγιά — slope, hillside", "μαυρισμένους": "μαυρισμένος — blackened", "δασική υπηρεσία": "δασική υπηρεσία — forest service", "όπου να 'ναι": "όπου να 'ναι — just anywhere", "αναγεννιέται": "αναγεννιέμαι — to regenerate", "κουκουνάρια": "κουκουνάρι — pine cone", "χαλεπίου πεύκης": "χαλέπιος πεύκη — Aleppo pine", "βόσκηση": "βόσκηση — grazing", "οικοδόμηση": "οικοδόμηση — building, construction", "βελανιδιές": "βελανιδιά — oak", "κουμαριές": "κουμαριά — strawberry tree", "χαρουπιές": "χαρουπιά — carob tree", "ξηρασία": "ξηρασία — drought", "δενδρύλλια": "δενδρύλλιο — sapling", "επιβίωσή": "επιβίωση — survival"},
})

ITEMS.append({
 "id": "l16-int-karavomarangos", "title": "Η καραβομαραγκός", "title_en": "The boat builder", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια νέα γυναίκα που φτιάχνει ξύλινα καΐκια σε ένα καρνάγιο.",
 "script": [
  L("Δημοσιογράφος", "m", "Δεν είναι συνηθισμένο να βλέπει κανείς μια γυναίκα σε καρνάγιο. Πώς έφτασες εδώ;", "It's not usual to see a woman in a boatyard. How did you end up here?"),
  L("Ιωάννα", "f", "Ο πατέρας μου ήταν καραβομαραγκός, όπως και ο παππούς μου. Μικρή περνούσα τα απογεύματα στο καρνάγιο, μάζευα πριονίδια και τον έβλεπα να δουλεύει. Όταν τελείωσα τη σχολή καλών τεχνών, κατάλαβα ότι αυτό που ήθελα να φτιάχνω δεν ήταν γλυπτά, αλλά καΐκια.", "My father was a boat builder, like my grandfather. As a child I spent afternoons at the boatyard, collecting sawdust and watching him work. When I finished art school, I realised that what I wanted to make wasn't sculptures, but caiques."),
  L("Δημοσιογράφος", "m", "Λένε ότι η τέχνη αυτή πεθαίνει.", "They say this craft is dying."),
  L("Ιωάννα", "f", "Κινδυνεύει, αυτό είναι αλήθεια. Για χρόνια οι ψαράδες έπαιρναν επιδότηση για να διαλύσουν τα ξύλινα σκάφη τους, και χάθηκαν χιλιάδες καΐκια. Σήμερα, όμως, υπάρχει ξανά ενδιαφέρον, κυρίως για επισκευές παλιών σκαφών. Κάθε καΐκι έχει τη δική του ιστορία, και όταν το ξαναρίχνουμε στη θάλασσα, νιώθω ότι σώζουμε ένα κομμάτι της μνήμης του νησιού.", "It's in danger, that's true. For years fishermen received subsidies to break up their wooden boats, and thousands of caiques were lost. Today, though, there is interest again, mainly in repairing old boats. Every caique has its own story, and when we put it back in the sea, I feel we're saving a piece of the island's memory."),
 ],
 "questions": [
  Q("Πώς γνώρισε η Ιωάννα τη δουλειά του καραβομαραγκού;", ["Από ένα βιβλίο", "Από τον πατέρα της, στο καρνάγιο", "Σε μια σχολή ναυπηγικής", "Από ένα ντοκιμαντέρ"], 1, "Ο πατέρας μου ήταν καραβομαραγκός"),
  Q("Τι σπούδασε η Ιωάννα;", ["Ναυπηγική", "Καλές τέχνες", "Αρχιτεκτονική", "Ιστορία"], 1, "Όταν τελείωσα τη σχολή καλών τεχνών"),
  Q("Γιατί χάθηκαν χιλιάδες καΐκια;", ["Από πυρκαγιές", "Γιατί οι ψαράδες έπαιρναν επιδότηση για να τα διαλύσουν", "Γιατί πουλήθηκαν στο εξωτερικό", "Από μια μεγάλη καταιγίδα"], 1, "οι ψαράδες έπαιρναν επιδότηση για να διαλύσουν τα ξύλινα σκάφη τους"),
 ],
 "gloss": {"καΐκια": "καΐκι — caique (traditional wooden boat)", "καρνάγιο": "καρνάγιο — boatyard", "καραβομαραγκός": "καραβομαραγκός — boat builder, shipwright", "πριονίδια": "πριονίδι — sawdust", "σχολή καλών τεχνών": "σχολή καλών τεχνών — art school", "γλυπτά": "γλυπτό — sculpture", "Κινδυνεύει": "κινδυνεύω — to be in danger", "επιδότηση": "επιδότηση — subsidy", "να διαλύσουν": "διαλύω — to break up, dismantle", "σκάφη": "σκάφος — boat, vessel", "το ξαναρίχνουμε στη θάλασσα": "ρίχνω στη θάλασσα — to launch (a boat)"},
})

ITEMS.append({
 "id": "l16-mon-kavafis", "title": "Ο Καβάφης και η Αλεξάνδρεια", "title_en": "Cavafy and Alexandria", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια ραδιοφωνική εκπομπή για τον ποιητή Κωνσταντίνο Καβάφη.",
 "script": [
  L("Παρουσιαστής", "m", "Ο Κωνσταντίνος Καβάφης γεννήθηκε το 1863 στην Αλεξάνδρεια, σε μια ακμάζουσα ελληνική παροικία, και πέθανε εκεί το 1933, ανήμερα των γενεθλίων του. Για περίπου τριάντα χρόνια εργάστηκε ως υπάλληλος στην Υπηρεσία Αρδεύσεων, μια δουλειά που, όπως έλεγε ο ίδιος, του άφηνε χρόνο για την ποίηση.", "Constantine Cavafy was born in 1863 in Alexandria, in a thriving Greek community, and died there in 1933, on his birthday. For about thirty years he worked as a clerk at the Irrigation Service, a job which, as he himself said, left him time for poetry."),
  L("Παρουσιαστής", "m", "Παράξενο για έναν ποιητή που σήμερα μεταφράζεται σε όλο τον κόσμο: ο Καβάφης δεν εξέδωσε ποτέ βιβλίο με τα ποιήματά του στο εμπόριο. Τα τύπωνε σε φυλλάδια και τα μοίραζε σε φίλους, διορθώνοντάς τα ξανά και ξανά. Ο «κανόνας» του, όπως τον ονομάζουμε, περιλαμβάνει εκατόν πενήντα τέσσερα ποιήματα.", "Strange for a poet who is now translated all over the world: Cavafy never published a book of his poems commercially. He printed them in leaflets and handed them out to friends, correcting them again and again. His 'canon', as we call it, comprises one hundred and fifty-four poems."),
  L("Παρουσιαστής", "m", "Η Αλεξάνδρεια είναι παρούσα σχεδόν σε όλο του το έργο, όχι όμως η σύγχρονη πόλη, αλλά η ελληνιστική πρωτεύουσα των Πτολεμαίων. Ο Καβάφης δεν τη γράφει με νοσταλγία· βλέπει τους ήρωές του με ειρωνεία και συμπόνια, την ώρα που χάνουν, που κάνουν λάθη, που συμβιβάζονται. Ίσως γι' αυτό μας μοιάζει τόσο σύγχρονος.", "Alexandria is present in almost all his work, not the modern city, however, but the Hellenistic capital of the Ptolemies. Cavafy doesn't write it with nostalgia; he sees his heroes with irony and compassion, at the moment they lose, make mistakes, compromise. Perhaps that is why he seems so modern to us."),
 ],
 "questions": [
  Q("Τι λέει ο παρουσιαστής για τη δουλειά του Καβάφη στην Υπηρεσία Αρδεύσεων;", ["Ότι τη μισούσε", "Ότι του άφηνε χρόνο για την ποίηση", "Ότι τον έκανε πλούσιο", "Ότι την άφησε γρήγορα"], 1, "μια δουλειά που, όπως έλεγε ο ίδιος, του άφηνε χρόνο για την ποίηση"),
  Q("Πώς κυκλοφορούσαν τα ποιήματα του Καβάφη όσο ζούσε;", ["Σε βιβλία στα βιβλιοπωλεία", "Σε εφημερίδες της Αθήνας", "Σε φυλλάδια που μοίραζε σε φίλους", "Μόνο σε μεταφράσεις"], 2, "Τα τύπωνε σε φυλλάδια και τα μοίραζε σε φίλους"),
  Q("Πώς βλέπει ο Καβάφης τους ήρωές του, σύμφωνα με τον ομιλητή;", ["Με θαυμασμό για τις νίκες τους", "Με ειρωνεία και συμπόνια", "Με νοσταλγία", "Με αδιαφορία"], 1, "βλέπει τους ήρωές του με ειρωνεία και συμπόνια"),
 ],
 "gloss": {"ακμάζουσα": "ακμάζων — thriving, flourishing", "παροικία": "παροικία — (expatriate) community", "ανήμερα": "ανήμερα — on the very day", "Υπηρεσία Αρδεύσεων": "Υπηρεσία Αρδεύσεων — Irrigation Service", "μεταφράζεται": "μεταφράζομαι — to be translated", "εξέδωσε": "εκδίδω — to publish", "στο εμπόριο": "στο εμπόριο — commercially, on sale", "φυλλάδια": "φυλλάδιο — leaflet, pamphlet", "κανόνας": "κανόνας — canon (of works); rule", "ελληνιστική": "ελληνιστικός — Hellenistic", "Πτολεμαίων": "Πτολεμαίοι — the Ptolemies", "νοσταλγία": "νοσταλγία — nostalgia", "ειρωνεία": "ειρωνεία — irony", "συμπόνια": "συμπόνια — compassion", "συμβιβάζονται": "συμβιβάζομαι — to compromise"},
})

ITEMS.append({
 "id": "l16-int-anglismoi", "title": "Αγγλικές λέξεις στα ελληνικά", "title_en": "English words in Greek", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με έναν γλωσσολόγο για τις αγγλικές λέξεις στην ελληνική γλώσσα.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Μαργαρίτη, πολλοί ανησυχούν ότι τα ελληνικά «γεμίζουν» αγγλικές λέξεις: μίτινγκ, ντεντλάιν, φιντμπάκ. Κινδυνεύει η γλώσσα μας;", "Mr Margaritis, many people worry that Greek is 'filling up' with English words: meeting, deadline, feedback. Is our language in danger?"),
  L("Γλωσσολόγος", "m", "Όχι, και θα σας πω γιατί. Ο δανεισμός λέξεων είναι φυσιολογικό φαινόμενο σε όλες τις γλώσσες. Τα ελληνικά έχουν δανειστεί από τα λατινικά, τα ιταλικά, τα τουρκικά, τα γαλλικά, και παρέμειναν ελληνικά. Οι περισσότερες αγγλικές λέξεις, εξάλλου, χρησιμοποιούνται σε συγκεκριμένα περιβάλλοντα, όπως οι εταιρείες ή η τεχνολογία, και πολλές εξαφανίζονται μέσα σε λίγα χρόνια.", "No, and I'll tell you why. Borrowing words is a normal phenomenon in all languages. Greek has borrowed from Latin, Italian, Turkish, French, and has remained Greek. Most English words, moreover, are used in specific settings, such as companies or technology, and many disappear within a few years."),
  L("Δημοσιογράφος", "f", "Δηλαδή δεν πρέπει να κάνουμε τίποτα;", "So we shouldn't do anything?"),
  L("Γλωσσολόγος", "m", "Δεν είπα αυτό. Το πρόβλημα δεν είναι οι δάνειες λέξεις, αλλά όταν τις χρησιμοποιούμε επειδή ακούγονται πιο «σοβαρές», ενώ υπάρχει απλή ελληνική λέξη που όλοι καταλαβαίνουν. Ένα ανακοινωθέν που μιλάει για «τάργκετ γκρουπ» αποκλείει όσους δεν ξέρουν αγγλικά. Και να θυμόμαστε ότι ο δανεισμός πάει και αντίστροφα: τα αγγλικά είναι γεμάτα ελληνικές λέξεις, από τη δημοκρατία ως την τηλεφωνία.", "I didn't say that. The problem isn't loanwords, but when we use them because they sound more 'serious', while there is a simple Greek word everyone understands. A press release that talks about a 'target group' excludes those who don't know English. And let's remember that borrowing goes the other way too: English is full of Greek words, from democracy to telephony."),
 ],
 "questions": [
  Q("Γιατί πιστεύει ο γλωσσολόγος ότι τα ελληνικά δεν κινδυνεύουν;", ["Γιατί οι Έλληνες δεν μιλούν αγγλικά", "Γιατί ο δανεισμός είναι φυσιολογικός και η γλώσσα έχει δανειστεί και στο παρελθόν", "Γιατί ο νόμος απαγορεύει τις ξένες λέξεις", "Γιατί οι αγγλικές λέξεις είναι λίγες"], 1, "Ο δανεισμός λέξεων είναι φυσιολογικό φαινόμενο σε όλες τις γλώσσες"),
  Q("Ποιο είναι, κατά τον γλωσσολόγο, το πραγματικό πρόβλημα;", ["Οι δάνειες λέξεις γενικά", "Η χρήση ξένων λέξεων για να ακουστεί κάτι πιο «σοβαρό», ενώ υπάρχει απλή ελληνική λέξη", "Η τεχνολογία", "Η διδασκαλία των αγγλικών στα σχολεία"], 1, "όταν τις χρησιμοποιούμε επειδή ακούγονται πιο «σοβαρές»"),
  Q("Τι θέλει να δείξει με το παράδειγμα της δημοκρατίας και της τηλεφωνίας;", ["Ότι ο δανεισμός πάει και αντίστροφα", "Ότι τα αγγλικά είναι δύσκολη γλώσσα", "Ότι οι λέξεις αυτές είναι αγγλικές", "Ότι η πολιτική επηρεάζει τη γλώσσα"], 0, "ο δανεισμός πάει και αντίστροφα"),
 ],
 "gloss": {"γλωσσολόγο": "γλωσσολόγος — linguist", "δανεισμός": "δανεισμός — borrowing", "φυσιολογικό φαινόμενο": "φυσιολογικό φαινόμενο — normal phenomenon", "έχουν δανειστεί": "δανείζομαι — to borrow", "παρέμειναν": "παραμένω — to remain", "περιβάλλοντα": "περιβάλλον — setting, environment", "εξαφανίζονται": "εξαφανίζομαι — to disappear", "δάνειες λέξεις": "δάνεια λέξη — loanword", "ανακοινωθέν": "ανακοινωθέν — press release, communiqué", "αποκλείει": "αποκλείω — to exclude", "αντίστροφα": "αντίστροφα — the other way round"},
})

rnd = random.Random(16)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-16.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
