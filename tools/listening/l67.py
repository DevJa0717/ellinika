# Source for library/listening/listening-67.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l67.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l67-ann-ekkinisi-10k", "title": "Λίγο πριν από την εκκίνηση", "title_en": "Just before the start", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε έναν αγώνα δρόμου δέκα χιλιομέτρων στην πόλη σας. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνητής", "m", "Καλημέρα σε όλους τους δρομείς! Η εκκίνηση του αγώνα των δέκα χιλιομέτρων θα δοθεί σε δεκαπέντε λεπτά. Παρακαλούμε να πάτε στη ζώνη εκκίνησης που αντιστοιχεί στο χρώμα του αριθμού σας: οι πράσινοι μπροστά, οι κίτρινοι στη μέση και οι κόκκινοι πίσω.", "Good morning to all runners! The start of the ten-kilometre race will be given in fifteen minutes. Please go to the starting zone that matches the colour of your bib number: green at the front, yellow in the middle and red at the back."),
  L("Εκφωνητής", "m", "Ο χρόνος σας καταγράφεται από το τσιπ που βρίσκεται στο πίσω μέρος του αριθμού, οπότε μην τον διπλώνετε. Σταθμοί νερού θα υπάρχουν στο τρίτο και στο έβδομο χιλιόμετρο.", "Your time is recorded by the chip on the back of your number, so don't fold it. There will be water stations at the third and the seventh kilometre."),
  L("Εκφωνητής", "m", "Όσοι δεν έχετε αφήσει ακόμη τις τσάντες σας, μπορείτε να τις αφήσετε στη σκηνή πίσω από την εξέδρα. Αν νιώσετε αδιαθεσία κατά τη διάρκεια του αγώνα, απευθυνθείτε στους εθελοντές με τα κίτρινα γιλέκα. Καλή επιτυχία!", "Those of you who haven't left your bags yet can leave them in the tent behind the stand. If you feel unwell during the race, go to the volunteers in yellow vests. Good luck!"),
 ],
 "questions": [
  Q("Πού πρέπει να σταθούν οι δρομείς με κόκκινο αριθμό;", ["Μπροστά", "Στη μέση", "Πίσω", "Δίπλα στην εξέδρα"], 2, "οι κόκκινοι πίσω"),
  Q("Γιατί δεν πρέπει να διπλώνουν τον αριθμό τους;", ["Γιατί θα σκιστεί", "Γιατί έχει το τσιπ που καταγράφει τον χρόνο", "Γιατί δεν θα φαίνεται το χρώμα", "Γιατί είναι απαγορευμένο από τον κανονισμό"], 1, "Ο χρόνος σας καταγράφεται από το τσιπ που βρίσκεται στο πίσω μέρος του αριθμού"),
  Q("Πού μπορούν να αφήσουν τις τσάντες τους;", ["Στους εθελοντές", "Στη σκηνή πίσω από την εξέδρα", "Στον σταθμό νερού", "Στο αυτοκίνητό τους"], 1, "στη σκηνή πίσω από την εξέδρα"),
 ],
 "gloss": {"δρομείς": "δρομέας — runner", "εκκίνηση": "εκκίνηση — start (of a race)", "ζώνη εκκίνησης": "ζώνη εκκίνησης — starting zone", "τσιπ": "τσιπ — chip", "διπλώνετε": "διπλώνω — to fold", "εξέδρα": "εξέδρα — stand, platform", "αδιαθεσία": "αδιαθεσία — feeling unwell", "γιλέκα": "γιλέκο — vest"},
})

ITEMS.append({
 "id": "l67-vm-metafrasi-ptychiou", "title": "Η μετάφραση του πτυχίου είναι έτοιμη", "title_en": "Your degree translation is ready", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε δώσει το πτυχίο σας για επίσημη μετάφραση. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, από το γραφείο μεταφράσεων «Λόγος» σας τηλεφωνώ. Η επίσημη μετάφραση του πτυχίου σας στα αγγλικά είναι έτοιμη και μπορείτε να την παραλάβετε από αύριο.", "Good morning, I'm calling from the Logos translation office. The official English translation of your degree is ready and you can collect it from tomorrow."),
  L("Υπάλληλος", "f", "Το κόστος είναι σαράντα πέντε ευρώ, όπως είχαμε συμφωνήσει, και μπορείτε να πληρώσετε με κάρτα. Παρακαλούμε να φέρετε μαζί σας την ταυτότητά σας, γιατί η μετάφραση παραδίδεται μόνο στον ίδιο τον ενδιαφερόμενο ή σε κάποιον με εξουσιοδότηση.", "The cost is forty-five euros, as we agreed, and you can pay by card. Please bring your ID with you, because the translation is only handed over to the person concerned or to someone with written authorisation."),
  L("Υπάλληλος", "f", "Σας θυμίζω ότι η σφραγίδα της Χάγης δεν περιλαμβάνεται· αν τη χρειάζεστε, πρέπει να απευθυνθείτε στην Περιφέρεια. Είμαστε ανοιχτά καθημερινά μέχρι τις τρεις, εκτός Σαββάτου. Ευχαριστώ.", "Just a reminder that the Hague apostille is not included; if you need it, you must apply to the regional authority. We're open every day until three, except Saturdays. Thank you."),
 ],
 "questions": [
  Q("Πότε μπορεί να παραλάβει τη μετάφραση;", ["Σήμερα", "Από αύριο", "Το Σάββατο", "Σε μία εβδομάδα"], 1, "μπορείτε να την παραλάβετε από αύριο"),
  Q("Τι πρέπει να φέρει μαζί του;", ["Το πρωτότυπο πτυχίο", "Μετρητά", "Την ταυτότητά του", "Μια φωτογραφία"], 2, "να φέρετε μαζί σας την ταυτότητά σας"),
  Q("Τι δεν περιλαμβάνεται στην τιμή;", ["Η σφραγίδα της Χάγης", "Η μετάφραση στα αγγλικά", "Η πληρωμή με κάρτα", "Η παράδοση στο σπίτι"], 0, "η σφραγίδα της Χάγης δεν περιλαμβάνεται"),
 ],
 "gloss": {"πτυχίο": "πτυχίο — degree (certificate)", "επίσημη μετάφραση": "επίσημη μετάφραση — certified translation", "παραλάβετε": "παραλαμβάνω — to collect, receive", "ενδιαφερόμενο": "ενδιαφερόμενος — person concerned", "εξουσιοδότηση": "εξουσιοδότηση — authorisation", "σφραγίδα της Χάγης": "σφραγίδα της Χάγης — Hague apostille", "Περιφέρεια": "Περιφέρεια — regional authority"},
})

ITEMS.append({
 "id": "l67-dia-ekplixi-mamas", "title": "Έκπληξη για τα πενήντα της μαμάς", "title_en": "A surprise for Mum's fiftieth", "type": "dialogue", "level": "B2",
 "context_el": "Δύο αδέρφια οργανώνουν ένα πάρτι-έκπληξη για τη μητέρα τους.",
 "script": [
  L("Ηλέκτρα", "f", "Τα πενήντα της μαμάς είναι σε τρεις εβδομάδες. Λέω να κλείσουμε την πίσω αίθουσα στην ταβέρνα του κυρ-Γιάννη. Χωράει σαράντα άτομα.", "Mum's fiftieth is in three weeks. I'm thinking we book the back room at Mr Giannis's taverna. It holds forty people."),
  L("Λευτέρης", "m", "Ωραία ιδέα. Βρήκα στο ίντερνετ και τρεις συμμαθήτριές της από το λύκειο. Δεν τις έχει δει από τότε που τελείωσαν το σχολείο. Θα πάθει πλάκα!", "Great idea. I've also found three of her classmates from secondary school online. She hasn't seen them since they finished school. She'll be amazed!"),
  L("Ηλέκτρα", "f", "Τέλεια! Το δύσκολο είναι να μην καταλάβει τίποτα. Θα πούμε στον μπαμπά να της πει ότι θα πάνε οι δυο τους για φαγητό, για να γιορτάσουν μόνοι τους.", "Perfect! The hard part is making sure she doesn't suspect anything. We'll tell Dad to tell her the two of them are going out to eat, to celebrate on their own."),
  L("Λευτέρης", "m", "Και τη μουσική την αναλαμβάνω εγώ: θα φτιάξω μια λίστα με τα αγαπημένα της τραγούδια της Αλεξίου. Τα έξοδα τα μοιράζουμε στη μέση, εντάξει;", "And I'll take care of the music: I'll make a playlist of her favourite Alexiou songs. We split the costs down the middle, OK?"),
 ],
 "questions": [
  Q("Πόσα άτομα χωράει η αίθουσα της ταβέρνας;", ["Είκοσι", "Τριάντα", "Σαράντα", "Πενήντα"], 2, "Χωράει σαράντα άτομα"),
  Q("Ποιους βρήκε ο Λευτέρης στο ίντερνετ;", ["Παλιούς συναδέλφους της μαμάς", "Τρεις συμμαθήτριές της από το λύκειο", "Μακρινούς συγγενείς", "Μια τραγουδίστρια"], 1, "τρεις συμμαθήτριές της από το λύκειο"),
  Q("Πώς θα φέρουν τη μαμά στην ταβέρνα χωρίς να καταλάβει;", ["Θα της πουν ότι είναι γιορτή ενός φίλου", "Ο μπαμπάς θα της πει ότι θα πάνε οι δυο τους για φαγητό", "Θα της πουν ότι έχει ραντεβού με τον γιατρό", "Θα την πάρει η Ηλέκτρα για ψώνια"], 1, "θα πάνε οι δυο τους για φαγητό"),
 ],
 "gloss": {"κλείσουμε": "κλείνω (τραπέζι, αίθουσα) — to book", "αίθουσα": "αίθουσα — room, hall", "συμμαθήτριές": "συμμαθήτρια — classmate (female)", "πάθει πλάκα": "παθαίνω πλάκα — to be amazed (colloquial)", "αναλαμβάνω": "αναλαμβάνω — to take on, take charge of", "έξοδα": "έξοδα — expenses"},
})

ITEMS.append({
 "id": "l67-dia-kodikos-kleidothike", "title": "Ο κωδικός μου κλειδώθηκε", "title_en": "My password got locked", "type": "dialogue", "level": "B2",
 "context_el": "Μια πελάτισσα τηλεφωνεί στην εξυπηρέτηση πελατών της τράπεζάς της.",
 "script": [
  L("Πελάτισσα", "f", "Καλησπέρα. Προσπάθησα να μπω στην εφαρμογή της τράπεζας και, αφού έβαλα τρεις φορές λάθος κωδικό, μου βγήκε μήνυμα ότι ο λογαριασμός μου κλειδώθηκε.", "Good evening. I tried to log into the bank's app and, after I entered the wrong password three times, I got a message that my account was locked."),
  L("Υπάλληλος", "m", "Μην ανησυχείτε, συμβαίνει συχνά. Για λόγους ασφαλείας, θα σας κάνω πρώτα μερικές ερωτήσεις: ποια είναι η ημερομηνία γέννησής σας και τα τέσσερα τελευταία ψηφία της κάρτας σας;", "Don't worry, it happens often. For security reasons, I'll first ask you a few questions: what is your date of birth and the last four digits of your card?"),
  L("Πελάτισσα", "f", "Δώδεκα Μαρτίου 1985, και τα ψηφία είναι 4417.", "The twelfth of March 1985, and the digits are 4417."),
  L("Υπάλληλος", "m", "Ευχαριστώ. Ξεκλείδωσα τον λογαριασμό και σας έστειλα με SMS έναν προσωρινό κωδικό, που ισχύει για μία ώρα. Μόλις μπείτε, θα σας ζητηθεί να ορίσετε καινούργιο. Και κάτι ακόμη: η τράπεζα δεν θα σας ζητήσει ποτέ τους κωδικούς σας με email ή μήνυμα. Αν λάβετε κάτι τέτοιο, μην απαντήσετε.", "Thank you. I've unlocked the account and sent you a temporary password by SMS, which is valid for one hour. As soon as you log in, you'll be asked to set a new one. And one more thing: the bank will never ask you for your passwords by email or message. If you receive something like that, don't reply."),
 ],
 "questions": [
  Q("Γιατί κλειδώθηκε ο λογαριασμός;", ["Γιατί έληξε η κάρτα", "Γιατί έβαλε τρεις φορές λάθος κωδικό", "Γιατί άλλαξε κινητό", "Γιατί δεν πλήρωσε έναν λογαριασμό"], 1, "αφού έβαλα τρεις φορές λάθος κωδικό"),
  Q("Πόσο ισχύει ο προσωρινός κωδικός;", ["Μία μέρα", "Μία ώρα", "Δέκα λεπτά", "Μία εβδομάδα"], 1, "που ισχύει για μία ώρα"),
  Q("Τι δεν θα κάνει ποτέ η τράπεζα;", ["Να στείλει SMS", "Να ζητήσει τους κωδικούς με email ή μήνυμα", "Να κάνει ερωτήσεις ασφαλείας", "Να ξεκλειδώσει λογαριασμούς"], 1, "η τράπεζα δεν θα σας ζητήσει ποτέ τους κωδικούς σας με email ή μήνυμα"),
 ],
 "gloss": {"εφαρμογή": "εφαρμογή — app", "κωδικό": "κωδικός — password, code", "κλειδώθηκε": "κλειδώνομαι — to be locked", "ψηφία": "ψηφίο — digit", "Ξεκλείδωσα": "ξεκλειδώνω — to unlock", "προσωρινό": "προσωρινός — temporary", "ορίσετε": "ορίζω — to set, define"},
})

ITEMS.append({
 "id": "l67-int-petalotis", "title": "Ο πεταλωτής", "title_en": "The farrier", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή για παλιά επαγγέλματα, μια δημοσιογράφος μιλά με έναν πεταλωτή.",
 "script": [
  L("Δημοσιογράφος", "f", "Πολλοί πιστεύουν ότι το επάγγελμα του πεταλωτή έχει εξαφανιστεί. Έχετε ακόμη δουλειά;", "Many people think the farrier's trade has disappeared. Do you still have work?"),
  L("Πεταλωτής", "m", "Και παραπάνω! Τα άλογα δεν δουλεύουν πια στα χωράφια, αλλά υπάρχουν σχολές ιππασίας, ιπποδρομίες και πολλοί που έχουν άλογα για χόμπι. Η οπλή του αλόγου μεγαλώνει συνεχώς, όπως τα νύχια μας, γι’ αυτό τα πέταλα πρέπει να αλλάζουν κάθε έξι με οκτώ εβδομάδες.", "More than enough! Horses don't work in the fields any more, but there are riding schools, horse races and lots of people who keep horses as a hobby. A horse's hoof grows all the time, like our nails, so the shoes need changing every six to eight weeks."),
  L("Δημοσιογράφος", "f", "Δεν πονάει το άλογο, όταν καρφώνετε το πέταλο;", "Doesn't it hurt the horse when you nail on the shoe?"),
  L("Πεταλωτής", "m", "Όχι, αν γίνει σωστά. Το εξωτερικό τοίχωμα της οπλής δεν έχει νεύρα. Το πιο σημαντικό είναι να ηρεμήσεις το ζώο. Ένα φοβισμένο άλογο ζυγίζει μισό τόνο, και μια κλοτσιά μπορεί να σου σπάσει τα πλευρά. Γι’ αυτό, πριν πιάσω το σφυρί, του μιλάω και το χαϊδεύω.", "No, if it's done properly. The outer wall of the hoof has no nerves. The most important thing is to calm the animal. A frightened horse weighs half a tonne, and a kick can break your ribs. That's why, before I pick up the hammer, I talk to it and stroke it."),
 ],
 "questions": [
  Q("Ποιοι χρειάζονται σήμερα τον πεταλωτή;", ["Μόνο οι αγρότες", "Σχολές ιππασίας, ιπποδρομίες και ιδιοκτήτες αλόγων για χόμπι", "Μόνο ο στρατός", "Κανείς"], 1, "υπάρχουν σχολές ιππασίας, ιπποδρομίες και πολλοί που έχουν άλογα για χόμπι"),
  Q("Κάθε πότε πρέπει να αλλάζουν τα πέταλα;", ["Κάθε χρόνο", "Κάθε έξι με οκτώ εβδομάδες", "Κάθε μήνα", "Μόνο όταν σπάσουν"], 1, "κάθε έξι με οκτώ εβδομάδες"),
  Q("Γιατί δεν πονάει το άλογο;", ["Γιατί του δίνουν φάρμακο", "Γιατί κοιμάται", "Γιατί το εξωτερικό τοίχωμα της οπλής δεν έχει νεύρα", "Γιατί τα πέταλα είναι πλαστικά"], 2, "Το εξωτερικό τοίχωμα της οπλής δεν έχει νεύρα"),
 ],
 "gloss": {"πεταλωτή": "πεταλωτής — farrier", "ιππασίας": "ιππασία — horse riding", "ιπποδρομίες": "ιπποδρομία — horse race", "οπλή": "οπλή — hoof", "πέταλα": "πέταλο — horseshoe", "καρφώνετε": "καρφώνω — to nail", "τοίχωμα": "τοίχωμα — wall (of an organ, a hoof)", "κλοτσιά": "κλοτσιά — kick", "πλευρά": "πλευρό — rib"},
})

ITEMS.append({
 "id": "l67-rep-kastellorizo", "title": "Καστελλόριζο, το ανατολικότερο νησί", "title_en": "Kastellorizo, the easternmost island", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από μια ταξιδιωτική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "f", "Το Καστελλόριζο είναι το ανατολικότερο κατοικημένο νησί της Ελλάδας. Από το λιμάνι του, οι ακτές της Τουρκίας φαίνονται τόσο κοντά, που μοιάζει να μπορείς να τις φτάσεις κολυμπώντας. Οι κάτοικοι είναι μόλις λίγες εκατοντάδες.", "Kastellorizo is the easternmost inhabited island of Greece. From its harbour, the Turkish coast looks so close that it seems you could swim to it. The inhabitants number only a few hundred."),
  L("Ρεπόρτερ", "f", "Στις αρχές του εικοστού αιώνα, όμως, το νησί είχε χιλιάδες κατοίκους και ένα από τα πιο πολυσύχναστα λιμάνια της περιοχής. Οι πόλεμοι και η οικονομική παρακμή οδήγησαν πολλούς στη μετανάστευση, κυρίως στην Αυστραλία, όπου ζει σήμερα μια μεγάλη κοινότητα Καστελλοριζιών.", "In the early twentieth century, however, the island had thousands of inhabitants and one of the busiest harbours in the region. Wars and economic decline led many to emigrate, mainly to Australia, where a large community of people from Kastellorizo lives today."),
  L("Ρεπόρτερ", "f", "Τα πολύχρωμα σπίτια γύρω από το λιμάνι έγιναν γνωστά σε όλο τον κόσμο το 1991, χάρη στην ιταλική ταινία «Μεντιτερράνεο», που κέρδισε το Όσκαρ. Ένα από τα αξιοθέατα που δεν πρέπει να χάσετε είναι η Γαλάζια Σπηλιά, όπου το φως του ήλιου βάφει το νερό σε ένα απίστευτο μπλε.", "The colourful houses around the harbour became known worldwide in 1991 thanks to the Italian film Mediterraneo, which won the Oscar. One of the sights you shouldn't miss is the Blue Cave, where the sunlight paints the water an incredible blue."),
 ],
 "questions": [
  Q("Τι ξεχωρίζει το Καστελλόριζο;", ["Είναι το μεγαλύτερο νησί της Δωδεκανήσου", "Είναι το ανατολικότερο κατοικημένο νησί της Ελλάδας", "Δεν έχει λιμάνι", "Έχει χιλιάδες κατοίκους σήμερα"], 1, "το ανατολικότερο κατοικημένο νησί της Ελλάδας"),
  Q("Πού μετανάστευσαν κυρίως οι κάτοικοι;", ["Στην Αμερική", "Στην Αυστραλία", "Στη Γερμανία", "Στην Αθήνα"], 1, "κυρίως στην Αυστραλία"),
  Q("Πώς έγινε γνωστό το νησί σε όλο τον κόσμο;", ["Από ένα βιβλίο", "Από την ταινία «Μεντιτερράνεο»", "Από έναν αρχαιολογικό χώρο", "Από ένα φεστιβάλ μουσικής"], 1, "χάρη στην ιταλική ταινία «Μεντιτερράνεο»"),
 ],
 "gloss": {"ανατολικότερο": "ανατολικότερος — easternmost", "κατοικημένο": "κατοικημένος — inhabited", "πολυσύχναστα": "πολυσύχναστος — busy, crowded", "παρακμή": "παρακμή — decline", "μετανάστευση": "μετανάστευση — emigration", "αξιοθέατα": "αξιοθέατο — sight, attraction", "Γαλάζια Σπηλιά": "Γαλάζια Σπηλιά — the Blue Cave"},
})

ITEMS.append({
 "id": "l67-mono-ilektriko-amaxi", "title": "Ένας χρόνος με ηλεκτρικό αυτοκίνητο", "title_en": "A year with an electric car", "type": "monologue", "level": "B2",
 "context_el": "Σε ένα podcast για την καθημερινότητα, ένας άντρας μιλά για την εμπειρία του με ένα ηλεκτρικό αυτοκίνητο.",
 "script": [
  L("Στράτος", "m", "Πέρσι τέτοια εποχή αγόρασα ηλεκτρικό αυτοκίνητο, και πολλοί φίλοι μού λένε ότι τρελάθηκα. Η αλήθεια είναι ότι για την πόλη είναι ιδανικό. Το φορτίζω στο γκαράζ το βράδυ, όσο κοιμάμαι, και το πρωί έχω αυτονομία περίπου τριακόσια πενήντα χιλιόμετρα.", "This time last year I bought an electric car, and many friends tell me I've gone mad. The truth is that for the city it's ideal. I charge it in the garage at night while I sleep, and in the morning I have a range of about three hundred and fifty kilometres."),
  L("Στράτος", "m", "Το κόστος ανά χιλιόμετρο είναι πολύ μικρότερο απ’ ό,τι με τη βενζίνη. Στο ταξίδι από την Αθήνα στη Θεσσαλονίκη σταμάτησα μία φορά, για μισή ώρα, σε έναν ταχυφορτιστή, όσο έπινα καφέ.", "The cost per kilometre is much lower than with petrol. On the trip from Athens to Thessaloniki I stopped once, for half an hour, at a fast charger while I had a coffee."),
  L("Στράτος", "m", "Υπάρχουν, βέβαια, και δυσκολίες. Σε ορισμένα νησιά και ορεινές περιοχές οι φορτιστές είναι ακόμη λίγοι, οπότε χρειάζεται προγραμματισμός. Και τον χειμώνα, με το κρύο, η αυτονομία μειώνεται αισθητά.", "There are, of course, difficulties too. On some islands and in mountain areas there are still few chargers, so you need to plan ahead. And in winter, with the cold, the range drops noticeably."),
 ],
 "questions": [
  Q("Πού φορτίζει συνήθως ο Στράτος το αυτοκίνητο;", ["Σε ταχυφορτιστές", "Στο γκαράζ το βράδυ", "Στη δουλειά του", "Σε βενζινάδικο"], 1, "Το φορτίζω στο γκαράζ το βράδυ, όσο κοιμάμαι"),
  Q("Τι έκανε στο ταξίδι προς τη Θεσσαλονίκη;", ["Δεν σταμάτησε καθόλου", "Σταμάτησε μία φορά για μισή ώρα σε ταχυφορτιστή", "Σταμάτησε τρεις φορές", "Πήρε το τρένο"], 1, "σταμάτησα μία φορά, για μισή ώρα, σε έναν ταχυφορτιστή"),
  Q("Τι συμβαίνει τον χειμώνα;", ["Η αυτονομία αυξάνεται", "Το αυτοκίνητο δεν ξεκινά", "Η αυτονομία μειώνεται αισθητά", "Το ρεύμα γίνεται ακριβότερο"], 2, "η αυτονομία μειώνεται αισθητά"),
 ],
 "gloss": {"φορτίζω": "φορτίζω — to charge", "αυτονομία": "αυτονομία — range (of a vehicle)", "ανά χιλιόμετρο": "ανά χιλιόμετρο — per kilometre", "ταχυφορτιστή": "ταχυφορτιστής — fast charger", "φορτιστές": "φορτιστής — charger", "προγραμματισμός": "προγραμματισμός — planning", "αισθητά": "αισθητά — noticeably"},
})

ITEMS.append({
 "id": "l67-mono-proti-mera-nosileftis", "title": "Η πρώτη μέρα ως νοσηλευτής", "title_en": "My first day as a nurse", "type": "monologue", "level": "B2",
 "context_el": "Σε μια εκπομπή για νέους επαγγελματίες, ένας νεαρός νοσηλευτής μιλά για την πρώτη του μέρα στη δουλειά.",
 "script": [
  L("Παύλος", "m", "Την πρώτη μου μέρα στο νοσοκομείο δεν θα την ξεχάσω ποτέ. Με έβαλαν στην παθολογική κλινική, με τριάντα κρεβάτια και μόνο τρεις νοσηλευτές στη βάρδια. Στις επτά το πρωί ήμουν ήδη μούσκεμα στον ιδρώτα.", "I'll never forget my first day at the hospital. They put me on the internal medicine ward, with thirty beds and only three nurses on the shift. By seven in the morning I was already drenched in sweat."),
  L("Παύλος", "m", "Η προϊσταμένη, μια αυστηρή κυρία με είκοσι πέντε χρόνια προϋπηρεσία, μου είπε: «Ό,τι δεν ξέρεις, ρωτάς. Ποτέ μην κάνεις κάτι για το οποίο δεν είσαι σίγουρος.» Τη ρώτησα τουλάχιστον πενήντα φορές εκείνη τη μέρα.", "The head nurse, a strict lady with twenty-five years' experience, told me: 'Whatever you don't know, ask. Never do something you're not sure about.' I asked her at least fifty times that day."),
  L("Παύλος", "m", "Το πιο συγκινητικό ήταν ένας ηλικιωμένος ασθενής, που στο τέλος της βάρδιας μού κράτησε το χέρι και μου είπε «Θα γίνεις καλός, παιδί μου». Εκείνη τη στιγμή κατάλαβα ότι διάλεξα το σωστό επάγγελμα.", "The most moving thing was an elderly patient who, at the end of the shift, held my hand and said, 'You'll be good at this, my boy.' At that moment I understood that I'd chosen the right profession."),
 ],
 "questions": [
  Q("Πόσοι νοσηλευτές ήταν στη βάρδια;", ["Τρεις", "Τριάντα", "Πέντε", "Ένας"], 0, "μόνο τρεις νοσηλευτές στη βάρδια"),
  Q("Ποια συμβουλή του έδωσε η προϊσταμένη;", ["Να δουλεύει γρήγορα", "Να ρωτάει ό,τι δεν ξέρει", "Να μη μιλάει στους ασθενείς", "Να φεύγει νωρίς"], 1, "Ό,τι δεν ξέρεις, ρωτάς"),
  Q("Τι τον έκανε να καταλάβει ότι διάλεξε το σωστό επάγγελμα;", ["Ο μισθός", "Τα λόγια ενός ηλικιωμένου ασθενούς", "Ένας έπαινος από τον διευθυντή", "Η προαγωγή του"], 1, "μου είπε «Θα γίνεις καλός, παιδί μου»"),
 ],
 "gloss": {"νοσηλευτής": "νοσηλευτής — nurse (male)", "παθολογική κλινική": "παθολογική κλινική — internal medicine ward", "βάρδια": "βάρδια — shift", "μούσκεμα στον ιδρώτα": "μούσκεμα στον ιδρώτα — drenched in sweat", "προϊσταμένη": "προϊσταμένη — head nurse, supervisor", "προϋπηρεσία": "προϋπηρεσία — previous work experience", "συγκινητικό": "συγκινητικός — moving, touching"},
})

ITEMS.append({
 "id": "l67-c1-anglika-daneia", "title": "Αγγλικές λέξεις στα ελληνικά", "title_en": "English words in Greek", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή λόγου, ένας δημοσιογράφος συζητά με μια γλωσσολόγο για τις αγγλικές λέξεις που μπαίνουν στα ελληνικά.",
 "script": [
  L("Δημοσιογράφος", "m", "Μίτινγκ, ντεντλάιν, μπρέινστορμινγκ: σε πολλά γραφεία μιλάμε πια μια γλώσσα μισή ελληνική και μισή αγγλική. Κινδυνεύουν τα ελληνικά;", "Meeting, deadline, brainstorming: in many offices we now speak a language that's half Greek and half English. Is Greek in danger?"),
  L("Γλωσσολόγος", "f", "Η ανησυχία είναι κατανοητή, αλλά η ιστορία μάς διδάσκει ψυχραιμία. Τα ελληνικά δανείστηκαν λέξεις από τα λατινικά, τα ιταλικά, τα τουρκικά και τα γαλλικά, χωρίς να χάσουν την ταυτότητά τους. Ταυτόχρονα, έχουν δώσει στις άλλες γλώσσες χιλιάδες λέξεις, από τη «δημοκρατία» μέχρι το «τηλέφωνο», που είναι, μάλιστα, νεότερο σύνθετο από ελληνικά στοιχεία.", "The concern is understandable, but history teaches us to keep calm. Greek borrowed words from Latin, Italian, Turkish and French without losing its identity. At the same time, it has given other languages thousands of words, from 'democracy' to 'telephone', which is in fact a modern compound made from Greek elements."),
  L("Δημοσιογράφος", "m", "Υπάρχει, όμως, κάποια διαφορά σήμερα;", "Is there any difference today, though?"),
  L("Γλωσσολόγος", "f", "Η ταχύτητα. Το διαδίκτυο φέρνει νέες λέξεις καθημερινά. Αυτό που με εντυπωσιάζει, πάντως, είναι η δημιουργικότητα των ομιλητών: τα αγγλικά ρήματα αποκτούν ελληνικές καταλήξεις, όπως το «τσεκάρω» ή το «γκουγκλάρω», ενώ τα ουσιαστικά γίνονται συνήθως άκλιτα ουδέτερα: «το λάπτοπ», «τα λάπτοπ». Η γραμματική, δηλαδή, μένει ελληνική. Το πραγματικό ζητούμενο δεν είναι να διώξουμε τα δάνεια, αλλά να μην ξεχάσουμε τις ελληνικές λέξεις που ήδη έχουμε.", "Speed. The internet brings new words every day. What impresses me, though, is speakers' creativity: English verbs acquire Greek endings, like 'tsekaro' or 'gouglaro', while nouns usually become indeclinable neuters: 'to laptop', 'ta laptop'. In other words, the grammar stays Greek. The real issue is not to drive the loanwords out, but not to forget the Greek words we already have."),
 ],
 "questions": [
  Q("Τι μας διδάσκει η ιστορία, σύμφωνα με τη γλωσσολόγο;", ["Ότι τα ελληνικά θα εξαφανιστούν", "Ψυχραιμία, γιατί τα ελληνικά δανείστηκαν λέξεις χωρίς να χάσουν την ταυτότητά τους", "Ότι πρέπει να απαγορευτούν οι ξένες λέξεις", "Ότι τα αγγλικά είναι ανώτερη γλώσσα"], 1, "η ιστορία μάς διδάσκει ψυχραιμία"),
  Q("Τι λέει για τη λέξη «τηλέφωνο»;", ["Ότι είναι αγγλική λέξη", "Ότι είναι νεότερο σύνθετο από ελληνικά στοιχεία", "Ότι είναι αρχαία λέξη", "Ότι προέρχεται από τα ιταλικά"], 1, "είναι, μάλιστα, νεότερο σύνθετο από ελληνικά στοιχεία"),
  Q("Τι συμβαίνει συνήθως με τα αγγλικά ουσιαστικά;", ["Παίρνουν αρσενικό γένος", "Γίνονται άκλιτα ουδέτερα", "Μεταφράζονται πάντα", "Παίρνουν ελληνικές καταλήξεις πληθυντικού"], 1, "τα ουσιαστικά γίνονται συνήθως άκλιτα ουδέτερα"),
  Q("Ποιο είναι, κατά τη γνώμη της, το πραγματικό ζητούμενο;", ["Να διώξουμε όλα τα δάνεια", "Να μιλάμε μόνο αγγλικά στη δουλειά", "Να μην ξεχάσουμε τις ελληνικές λέξεις που ήδη έχουμε", "Να γράφουμε τις ξένες λέξεις με λατινικούς χαρακτήρες"], 2, "να μην ξεχάσουμε τις ελληνικές λέξεις που ήδη έχουμε"),
 ],
 "gloss": {"γλωσσολόγο": "γλωσσολόγος — linguist", "ψυχραιμία": "ψυχραιμία — composure, calm", "δανείστηκαν": "δανείζομαι — to borrow", "σύνθετο": "σύνθετο — compound (word)", "δημιουργικότητα": "δημιουργικότητα — creativity", "καταλήξεις": "κατάληξη — ending (grammar)", "άκλιτα": "άκλιτος — indeclinable", "δάνεια": "δάνειο — loan, loanword"},
})

ITEMS.append({
 "id": "l67-c1-gorgopotamos", "title": "Η ανατίναξη της γέφυρας του Γοργοπόταμου", "title_en": "Blowing up the Gorgopotamos bridge", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από διάλεξη ιστορικού για μια από τις πιο γνωστές πράξεις της Εθνικής Αντίστασης.",
 "script": [
  L("Ιστορικός", "f", "Το φθινόπωρο του 1942 οι Βρετανοί αναζητούσαν τρόπο να διακόψουν τον ανεφοδιασμό των γερμανικών και ιταλικών δυνάμεων στη Βόρεια Αφρική. Μεγάλο μέρος των εφοδίων περνούσε από τη σιδηροδρομική γραμμή Θεσσαλονίκης–Αθήνας, με προορισμό τα λιμάνια της νότιας Ελλάδας. Έτσι γεννήθηκε το σχέδιο να ανατιναχτεί η γέφυρα του Γοργοπόταμου, κοντά στη Λαμία.", "In the autumn of 1942 the British were looking for a way to cut the supply of German and Italian forces in North Africa. A large part of the supplies went along the Thessaloniki–Athens railway line, bound for the ports of southern Greece. That is how the plan to blow up the Gorgopotamos bridge, near Lamia, was born."),
  L("Ιστορικός", "f", "Μια μικρή ομάδα Βρετανών αλεξιπτωτιστών συνεργάστηκε με τις δύο μεγαλύτερες αντιστασιακές οργανώσεις, τον ΕΛΑΣ, με επικεφαλής τον Άρη Βελουχιώτη, και τον ΕΔΕΣ του Ναπολέοντα Ζέρβα. Τη νύχτα της 25ης Νοεμβρίου, οι αντάρτες εξουδετέρωσαν την ιταλική φρουρά, και οι σαμποτέρ τοποθέτησαν τα εκρηκτικά. Δύο από τα μεταλλικά ανοίγματα της γέφυρας κατέρρευσαν.", "A small team of British parachutists worked with the two largest resistance organisations, ELAS, led by Aris Velouchiotis, and Napoleon Zervas's EDES. On the night of 25 November the partisans overcame the Italian garrison, and the saboteurs laid the explosives. Two of the bridge's metal spans collapsed."),
  L("Ιστορικός", "f", "Η επιχείρηση θεωρείται μία από τις σημαντικότερες δολιοφθορές στην κατεχόμενη Ευρώπη και ανέβασε το ηθικό των Ελλήνων. Είχε, όμως, και έναν πικρό συμβολισμό: ήταν μία από τις ελάχιστες φορές που οι δύο οργανώσεις πολέμησαν μαζί. Λίγο αργότερα, οι μεταξύ τους αντιπαραθέσεις θα οδηγούσαν σε ένοπλες συγκρούσεις, προάγγελο του Εμφυλίου.", "The operation is considered one of the most important acts of sabotage in occupied Europe and raised Greek morale. But it also carried a bitter symbolism: it was one of the very few times the two organisations fought together. Soon afterwards, the disputes between them would lead to armed clashes, a harbinger of the Civil War."),
 ],
 "questions": [
  Q("Ποιος ήταν ο στόχος των Βρετανών;", ["Να καταλάβουν τη Λαμία", "Να διακόψουν τον ανεφοδιασμό των δυνάμεων του Άξονα στη Βόρεια Αφρική", "Να απελευθερώσουν την Αθήνα", "Να καταστρέψουν τα λιμάνια"], 1, "να διακόψουν τον ανεφοδιασμό των γερμανικών και ιταλικών δυνάμεων στη Βόρεια Αφρική"),
  Q("Ποιοι συνεργάστηκαν στην επιχείρηση;", ["Μόνο ο ΕΛΑΣ", "Βρετανοί αλεξιπτωτιστές, ο ΕΛΑΣ και ο ΕΔΕΣ", "Ο ελληνικός στρατός και οι Αμερικανοί", "Μόνο Βρετανοί κομάντος"], 1, "Μια μικρή ομάδα Βρετανών αλεξιπτωτιστών συνεργάστηκε με τις δύο μεγαλύτερες αντιστασιακές οργανώσεις"),
  Q("Τι έγινε με τη γέφυρα;", ["Έμεινε άθικτη", "Κατέρρευσαν δύο από τα μεταλλικά ανοίγματά της", "Καταστράφηκε ολόκληρη", "Την κατέλαβαν οι Ιταλοί"], 1, "Δύο από τα μεταλλικά ανοίγματα της γέφυρας κατέρρευσαν"),
  Q("Ποιος ήταν ο «πικρός συμβολισμός» της επιχείρησης;", ["Ότι σκοτώθηκαν πολλοί άμαχοι", "Ότι ήταν μία από τις ελάχιστες φορές που οι δύο οργανώσεις πολέμησαν μαζί", "Ότι απέτυχε", "Ότι οι Βρετανοί δεν βοήθησαν"], 1, "ήταν μία από τις ελάχιστες φορές που οι δύο οργανώσεις πολέμησαν μαζί"),
 ],
 "gloss": {"ανεφοδιασμό": "ανεφοδιασμός — supply, resupply", "εφοδίων": "εφόδια — supplies", "ανατιναχτεί": "ανατινάζομαι — to be blown up", "αλεξιπτωτιστών": "αλεξιπτωτιστής — parachutist", "αντάρτες": "αντάρτης — partisan, guerrilla", "εξουδετέρωσαν": "εξουδετερώνω — to neutralise, overcome", "φρουρά": "φρουρά — garrison, guard", "δολιοφθορές": "δολιοφθορά — sabotage", "αντιπαραθέσεις": "αντιπαράθεση — dispute, confrontation", "προάγγελο": "προάγγελος — harbinger"},
})

rnd = random.Random(67)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-67.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
