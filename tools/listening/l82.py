# Source for library/listening/listening-82.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l82.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l82-ann-kep-rantevou", "title": "Νέο σύστημα ραντεβού στο ΚΕΠ", "title_en": "New appointment system at the citizens' service centre", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε στην αίθουσα αναμονής ενός Κέντρου Εξυπηρέτησης Πολιτών (ΚΕΠ). Θα ακούσετε μια ανακοίνωση.",
 "script": [
  L("Υπάλληλος", "f", "Αγαπητοί πολίτες, σας ενημερώνουμε ότι από την πρώτη του επόμενου μήνα η εξυπηρέτηση στο ΚΕΠ θα γίνεται μόνο με ραντεβού. Το ραντεβού κλείνεται ηλεκτρονικά, μέσω της ιστοσελίδας του δήμου, ή τηλεφωνικά, τις εργάσιμες μέρες από τις οχτώ μέχρι τις δύο.", "Dear citizens, we inform you that from the first of next month service at the citizens' service centre will be by appointment only. Appointments are booked online, through the municipality's website, or by phone, on working days from eight to two."),
  L("Υπάλληλος", "f", "Εξαιρούνται τα άτομα με αναπηρία και οι πολίτες άνω των εβδομήντα πέντε ετών, οι οποίοι θα εξυπηρετούνται κατά προτεραιότητα και χωρίς ραντεβού. Παρακαλούμε να έρχεστε δέκα λεπτά πριν από την ώρα σας, με την αστυνομική σας ταυτότητα και όλα τα απαραίτητα δικαιολογητικά.", "People with disabilities and citizens over seventy-five are exempt; they will be served as a priority and without an appointment. Please come ten minutes before your time, with your identity card and all the necessary documents."),
  L("Υπάλληλος", "f", "Αν δεν μπορείτε να έρθετε, ακυρώστε το ραντεβού σας τουλάχιστον μία μέρα νωρίτερα, ώστε να εξυπηρετηθεί κάποιος άλλος συμπολίτης. Ευχαριστούμε για τη συνεργασία.", "If you cannot come, please cancel your appointment at least one day in advance, so that another fellow citizen can be served. Thank you for your cooperation."),
 ],
 "questions": [
  Q("Πώς μπορεί κανείς να κλείσει ραντεβού;", ["Μόνο αυτοπροσώπως", "Ηλεκτρονικά ή τηλεφωνικά", "Μόνο με email", "Μέσω ταχυδρομείου"], 1, "Το ραντεβού κλείνεται ηλεκτρονικά, μέσω της ιστοσελίδας του δήμου, ή τηλεφωνικά"),
  Q("Ποιοι εξυπηρετούνται χωρίς ραντεβού;", ["Οι φοιτητές", "Τα άτομα με αναπηρία και οι πολίτες άνω των εβδομήντα πέντε", "Οι δημοτικοί υπάλληλοι", "Όσοι έρχονται πριν από τις οχτώ"], 1, "Εξαιρούνται τα άτομα με αναπηρία και οι πολίτες άνω των εβδομήντα πέντε ετών"),
  Q("Γιατί πρέπει να ακυρώνει κανείς το ραντεβού του μία μέρα νωρίτερα;", ["Για να μην πληρώσει πρόστιμο", "Για να εξυπηρετηθεί κάποιος άλλος", "Για να κλείσει καινούργιο", "Για να ενημερωθεί ο δήμαρχος"], 1, "ώστε να εξυπηρετηθεί κάποιος άλλος συμπολίτης"),
 ],
 "gloss": {"Κέντρου Εξυπηρέτησης Πολιτών": "Κέντρο Εξυπηρέτησης Πολιτών (ΚΕΠ) — citizens' service centre", "εξυπηρέτηση": "εξυπηρέτηση — service", "ραντεβού": "ραντεβού — appointment", "εργάσιμες": "εργάσιμος — working (day)", "Εξαιρούνται": "εξαιρούμαι — to be exempt", "αναπηρία": "αναπηρία — disability", "κατά προτεραιότητα": "κατά προτεραιότητα — as a priority", "αστυνομική σας ταυτότητα": "αστυνομική ταυτότητα — identity card", "δικαιολογητικά": "δικαιολογητικά — supporting documents", "συμπολίτης": "συμπολίτης — fellow citizen"},
})
ITEMS.append({
 "id": "l82-vm-xenagos-dilos", "title": "Μήνυμα από τον ξεναγό για την εκδρομή στη Δήλο", "title_en": "Voicemail from the guide about the Delos trip", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κλείσει μια εκδρομή στη Δήλο από τη Μύκονο. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Άρης", "m", "Καλησπέρα, είμαι ο Άρης, ο ξεναγός σας για την αυριανή εκδρομή στη Δήλο. Το καραβάκι φεύγει από το παλιό λιμάνι της Μυκόνου στις εννιά ακριβώς, οπότε σας παρακαλώ να είστε στην προβλήτα στις οχτώ και μισή. Αν αργήσετε, δεν μπορούμε να σας περιμένουμε, γιατί το νησί κλείνει νωρίς.", "Good evening, this is Aris, your guide for tomorrow's trip to Delos. The boat leaves the old port of Mykonos at nine sharp, so please be at the pier at half past eight. If you're late we can't wait for you, because the island closes early."),
  L("Άρης", "m", "Στη Δήλο δεν υπάρχει σχεδόν καθόλου σκιά, και ο αρχαιολογικός χώρος είναι μεγάλος. Φέρτε καπέλο, αντηλιακό και τουλάχιστον ένα λίτρο νερό ο καθένας. Φορέστε κλειστά, άνετα παπούτσια, γιατί θα περπατήσουμε πάνω σε πέτρες.", "There is almost no shade on Delos, and the archaeological site is large. Bring a hat, sunscreen and at least a litre of water each. Wear closed, comfortable shoes, because we'll be walking on stones."),
  L("Άρης", "m", "Σας θυμίζω ότι στο νησί δεν επιτρέπεται να μείνει κανείς τη νύχτα, και ότι απαγορεύεται αυστηρά να πάρετε μαζί σας πέτρες ή όστρακα από τον χώρο. Αν έχετε ερωτήσεις, καλέστε με σε αυτό τον αριθμό. Τα λέμε αύριο!", "I remind you that nobody is allowed to stay on the island overnight, and that it is strictly forbidden to take stones or potsherds from the site. If you have any questions, call me on this number. See you tomorrow!"),
 ],
 "questions": [
  Q("Τι ώρα πρέπει να είναι οι επισκέπτες στην προβλήτα;", ["Στις οχτώ", "Στις οχτώ και μισή", "Στις εννιά", "Στις εννιά και μισή"], 1, "σας παρακαλώ να είστε στην προβλήτα στις οχτώ και μισή"),
  Q("Γιατί πρέπει να φέρουν καπέλο και νερό;", ["Γιατί η εκδρομή κρατάει όλη μέρα", "Γιατί στη Δήλο δεν υπάρχει σχεδόν καθόλου σκιά", "Γιατί δεν υπάρχει καντίνα στο καραβάκι", "Γιατί θα κολυμπήσουν"], 1, "Στη Δήλο δεν υπάρχει σχεδόν καθόλου σκιά"),
  Q("Τι απαγορεύεται αυστηρά;", ["Να βγάζουν φωτογραφίες", "Να παίρνουν πέτρες ή όστρακα από τον χώρο", "Να τρώνε στο νησί", "Να μιλούν δυνατά"], 1, "απαγορεύεται αυστηρά να πάρετε μαζί σας πέτρες ή όστρακα από τον χώρο"),
 ],
 "gloss": {"ξεναγός": "ξεναγός — tour guide", "καραβάκι": "καραβάκι — small boat", "προβλήτα": "προβλήτα — pier, jetty", "σκιά": "σκιά — shade", "αρχαιολογικός χώρος": "αρχαιολογικός χώρος — archaeological site", "αντηλιακό": "αντηλιακό — sunscreen", "αυστηρά": "αυστηρά — strictly", "όστρακα": "όστρακο — potsherd, shell"},
})
ITEMS.append({
 "id": "l82-dia-episkevi-kinitou", "title": "Επισκευή ή καινούργιο κινητό;", "title_en": "Repair the phone or buy a new one?", "type": "dialogue", "level": "B2",
 "context_el": "Ένας πελάτης πηγαίνει σε ένα μικρό κατάστημα επισκευής κινητών με το τηλέφωνό του. Θα ακούσετε τη συνομιλία του με την τεχνικό.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Μου έπεσε το κινητό στο πεζοδρόμιο και ράγισε η οθόνη. Λειτουργεί ακόμα, αλλά η αφή δεν δουλεύει σε μια γωνία.", "Good morning. I dropped my phone on the pavement and the screen cracked. It still works, but the touch doesn't work in one corner."),
  L("Τεχνικός", "f", "Ας το δω. Ναι, πρέπει να αλλάξει όλη η οθόνη. Με γνήσιο ανταλλακτικό κοστίζει εκατόν σαράντα ευρώ, με συμβατό περίπου ογδόντα. Το συμβατό είναι λίγο λιγότερο φωτεινό, αλλά για καθημερινή χρήση δεν θα δείτε μεγάλη διαφορά.", "Let me see. Yes, the whole screen needs replacing. With an original part it costs a hundred and forty euros, with a compatible one about eighty. The compatible one is a little less bright, but for everyday use you won't see much difference."),
  L("Πελάτης", "m", "Εκατόν σαράντα; Με λίγα χρήματα παραπάνω παίρνω καινούργιο.", "A hundred and forty? For a bit more money I can get a new one."),
  L("Τεχνικός", "f", "Μπορείτε, βέβαια. Αλλά το δικό σας είναι μόλις δύο χρονών και η μπαταρία του είναι σε πολύ καλή κατάσταση. Ένα καινούργιο της ίδιας κατηγορίας θα σας κοστίσει πάνω από τετρακόσια. Και κάθε κινητό που πετάμε είναι κι ένα κομμάτι ηλεκτρονικά απόβλητα.", "You can, of course. But yours is only two years old and its battery is in very good condition. A new one in the same class will cost you over four hundred. And every phone we throw away is also a piece of electronic waste."),
  L("Πελάτης", "m", "Εντάξει, με πείσατε. Το συμβατό. Πόσο θα πάρει;", "All right, you've convinced me. The compatible one. How long will it take?"),
  L("Τεχνικός", "f", "Αν το αφήσετε τώρα, θα είναι έτοιμο σε δύο ώρες. Σας δίνουμε και εγγύηση έξι μηνών για την οθόνη. Καλό θα ήταν, πάντως, να βάλετε και μια θήκη.", "If you leave it now, it'll be ready in two hours. We also give you a six-month guarantee on the screen. It would be a good idea, though, to get a case as well."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με το κινητό;", ["Δεν ανάβει καθόλου", "Η οθόνη ράγισε και η αφή δεν δουλεύει σε μια γωνία", "Η μπαταρία τελειώνει γρήγορα", "Δεν ακούγεται ο ήχος"], 1, "ράγισε η οθόνη. Λειτουργεί ακόμα, αλλά η αφή δεν δουλεύει σε μια γωνία"),
  Q("Ποια επιχειρήματα χρησιμοποιεί η τεχνικός για να τον πείσει να το επισκευάσει;", ["Ότι τα καινούργια κινητά είναι χειρότερα", "Ότι το κινητό είναι μόνο δύο χρονών, η μπαταρία είναι καλή και ένα καινούργιο κοστίζει πολύ περισσότερο", "Ότι δεν έχει καινούργια κινητά στο κατάστημα", "Ότι η επισκευή είναι δωρεάν"], 1, "το δικό σας είναι μόλις δύο χρονών και η μπαταρία του είναι σε πολύ καλή κατάσταση"),
  Q("Τι εγγύηση δίνει το κατάστημα;", ["Δεν δίνει εγγύηση", "Έξι μηνών για την οθόνη", "Ενός χρόνου για όλο το κινητό", "Δύο χρόνων"], 1, "Σας δίνουμε και εγγύηση έξι μηνών για την οθόνη"),
 ],
 "gloss": {"επισκευής": "επισκευή — repair", "ράγισε": "ραγίζω — to crack", "αφή": "αφή — touch (screen)", "γνήσιο ανταλλακτικό": "γνήσιο ανταλλακτικό — original spare part", "συμβατό": "συμβατός — compatible", "φωτεινό": "φωτεινός — bright", "κατηγορίας": "κατηγορία — class, category", "ηλεκτρονικά απόβλητα": "ηλεκτρονικά απόβλητα — electronic waste", "εγγύηση": "εγγύηση — guarantee", "θήκη": "θήκη — (phone) case"},
})
ITEMS.append({
 "id": "l82-int-syntiritria-vivlion", "title": "Μια συντηρήτρια παλιών βιβλίων", "title_en": "A conservator of old books", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή για τα επαγγέλματα του πολιτισμού, η δημοσιογράφος μιλά με την Ευτυχία, που συντηρεί παλιά βιβλία και χειρόγραφα σε μια δημόσια βιβλιοθήκη.",
 "script": [
  L("Δημοσιογράφος", "m", "Ευτυχία, τι ακριβώς σημαίνει «συντήρηση» ενός βιβλίου;", "Eftychia, what exactly does the 'conservation' of a book mean?"),
  L("Ευτυχία", "f", "Σημαίνει να σταματήσουμε τη φθορά και να το κάνουμε ξανά ασφαλές για χρήση, χωρίς να αλλάξουμε τον χαρακτήρα του. Δεν το κάνουμε να μοιάζει καινούργιο. Αν ένα βιβλίο του δέκατου όγδοου αιώνα έχει σημειώσεις στο περιθώριο ή λεκέδες από κερί, αυτά είναι μέρος της ιστορίας του.", "It means stopping the deterioration and making it safe to use again, without changing its character. We don't make it look new. If an eighteenth-century book has notes in the margin or wax stains, those are part of its history."),
  L("Δημοσιογράφος", "m", "Ποιοι είναι οι μεγαλύτεροι εχθροί των βιβλίων;", "What are books' greatest enemies?"),
  L("Ευτυχία", "f", "Η υγρασία, πρώτα απ’ όλα, γιατί φέρνει μύκητες. Μετά, το φως και τα έντομα. Αλλά ο πιο ύπουλος εχθρός είναι συχνά το ίδιο το χαρτί. Το φθηνό χαρτί που χρησιμοποιήθηκε από τα μέσα του δέκατου ένατου αιώνα περιέχει οξέα και κιτρινίζει και θρυμματίζεται με τα χρόνια, ενώ το παλαιότερο χαρτί από κουρέλια αντέχει αιώνες.", "Damp, first of all, because it brings mould. Then light and insects. But the most insidious enemy is often the paper itself. The cheap paper used from the mid-nineteenth century contains acids and yellows and crumbles over the years, while older rag paper lasts for centuries."),
  L("Δημοσιογράφος", "m", "Τι συμβουλή θα δίνατε σε όσους έχουν παλιά βιβλία στο σπίτι;", "What advice would you give people who have old books at home?"),
  L("Ευτυχία", "f", "Να τα κρατούν μακριά από το υπόγειο και τη σοφίτα, όπου η θερμοκρασία αλλάζει απότομα. Να μην τα στοιβάζουν ούτε να τα δένουν με λαστιχάκια. Και, πάνω απ’ όλα, να μην τα «επισκευάζουν» με σελοτέιπ. Το σελοτέιπ είναι ο εφιάλτης κάθε συντηρητή.", "To keep them away from the basement and the attic, where the temperature changes abruptly. Not to stack them or tie them up with rubber bands. And above all, not to 'repair' them with sticky tape. Sticky tape is every conservator's nightmare."),
 ],
 "questions": [
  Q("Τι σημαίνει, για την Ευτυχία, η συντήρηση ενός βιβλίου;", ["Να το κάνει να μοιάζει καινούργιο", "Να σταματήσει τη φθορά χωρίς να αλλάξει τον χαρακτήρα του", "Να αντιγράψει το κείμενο", "Να αλλάξει το εξώφυλλο"], 1, "Σημαίνει να σταματήσουμε τη φθορά και να το κάνουμε ξανά ασφαλές για χρήση, χωρίς να αλλάξουμε τον χαρακτήρα του"),
  Q("Γιατί είναι συχνά πρόβλημα το χαρτί από τα μέσα του δέκατου ένατου αιώνα;", ["Γιατί είναι πολύ χοντρό", "Γιατί περιέχει οξέα και θρυμματίζεται με τα χρόνια", "Γιατί είναι από κουρέλια", "Γιατί το τρώνε τα ποντίκια"], 1, "περιέχει οξέα και κιτρινίζει και θρυμματίζεται με τα χρόνια"),
  Q("Τι συμβουλεύει να μην κάνουμε;", ["Να διαβάζουμε τα παλιά βιβλία", "Να τα επισκευάζουμε με σελοτέιπ", "Να τα κρατάμε στο σαλόνι", "Να τα δανείζουμε"], 1, "να μην τα «επισκευάζουν» με σελοτέιπ"),
 ],
 "gloss": {"συντηρεί": "συντηρώ — to conserve, preserve", "χειρόγραφα": "χειρόγραφο — manuscript", "φθορά": "φθορά — deterioration, wear", "περιθώριο": "περιθώριο — margin", "λεκέδες": "λεκές — stain", "μύκητες": "μύκητας — fungus, mould", "ύπουλος": "ύπουλος — insidious, treacherous", "οξέα": "οξύ — acid", "θρυμματίζεται": "θρυμματίζομαι — to crumble", "κουρέλια": "κουρέλι — rag", "στοιβάζουν": "στοιβάζω — to stack, pile up", "σελοτέιπ": "σελοτέιπ — sticky tape", "εφιάλτης": "εφιάλτης — nightmare"},
})
ITEMS.append({
 "id": "l82-rep-edessa", "title": "Οι καταρράκτες της Έδεσσας", "title_en": "The waterfalls of Edessa", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ταξιδιωτικό ρεπορτάζ από την Έδεσσα, στην κεντρική Μακεδονία.",
 "script": [
  L("Ρεπόρτερ", "f", "Η Έδεσσα είναι γνωστή ως η «πόλη των νερών», και δεν είναι δύσκολο να καταλάβει κανείς γιατί. Ποτάμια και ρυάκια διασχίζουν την πόλη, και στην άκρη της, εκεί όπου το οροπέδιο τελειώνει απότομα, τα νερά πέφτουν από ψηλά σχηματίζοντας μια σειρά από καταρράκτες. Ο μεγαλύτερος, ο Κάρανος, έχει ύψος περίπου εβδομήντα μέτρων.", "Edessa is known as the 'city of waters', and it isn't hard to see why. Rivers and streams cross the town, and at its edge, where the plateau ends abruptly, the waters fall from a height, forming a series of waterfalls. The largest, Karanos, is about seventy metres high."),
  L("Ρεπόρτερ", "f", "Ένα στενό μονοπάτι οδηγεί πίσω από τον καταρράκτη, σε μια μικρή σπηλιά, από όπου ο επισκέπτης βλέπει το νερό να πέφτει μπροστά του σαν κουρτίνα. Το έδαφος είναι υγρό και γλιστερό, γι’ αυτό χρειάζονται παπούτσια με καλό πάτο.", "A narrow path leads behind the waterfall to a small cave, from where the visitor sees the water falling in front of him like a curtain. The ground is wet and slippery, so shoes with a good sole are needed."),
  L("Ρεπόρτερ", "f", "Τα νερά δεν ήταν πάντα μόνο αξιοθέατο. Για αιώνες κινούσαν νερόμυλους, και αργότερα υφαντουργεία και κανναβουργεία, που έκαναν την Έδεσσα σημαντικό βιομηχανικό κέντρο. Σήμερα, σε ένα από τα παλιά κτίρια λειτουργεί ένα υπαίθριο μουσείο του νερού, όπου οι επισκέπτες μαθαίνουν πώς το νερό έγινε ενέργεια.", "The waters were not always just a sight. For centuries they drove watermills, and later textile mills and hemp factories, which made Edessa an important industrial centre. Today, in one of the old buildings, there is an open-air water museum, where visitors learn how water became energy."),
 ],
 "questions": [
  Q("Πόσο ύψος έχει ο μεγαλύτερος καταρράκτης;", ["Περίπου τριάντα μέτρα", "Περίπου εβδομήντα μέτρα", "Περίπου διακόσια μέτρα", "Περίπου δέκα μέτρα"], 1, "Ο μεγαλύτερος, ο Κάρανος, έχει ύψος περίπου εβδομήντα μέτρων"),
  Q("Γιατί χρειάζονται παπούτσια με καλό πάτο;", ["Γιατί το μονοπάτι είναι μακρύ", "Γιατί το έδαφος είναι υγρό και γλιστερό", "Γιατί υπάρχουν πολλές πέτρες", "Γιατί κάνει κρύο"], 1, "Το έδαφος είναι υγρό και γλιστερό"),
  Q("Τι κινούσαν παλιότερα τα νερά της Έδεσσας;", ["Μόνο βάρκες", "Νερόμυλους, υφαντουργεία και κανναβουργεία", "Ηλεκτρικά τρένα", "Αντλίες για τα χωράφια"], 1, "Για αιώνες κινούσαν νερόμυλους, και αργότερα υφαντουργεία και κανναβουργεία"),
 ],
 "gloss": {"ρυάκια": "ρυάκι — stream, brook", "διασχίζουν": "διασχίζω — to cross", "οροπέδιο": "οροπέδιο — plateau", "καταρράκτες": "καταρράκτης — waterfall", "σπηλιά": "σπηλιά — cave", "γλιστερό": "γλιστερός — slippery", "πάτο": "πάτος — sole (of a shoe), bottom", "αξιοθέατο": "αξιοθέατο — sight, attraction", "νερόμυλους": "νερόμυλος — watermill", "υφαντουργεία": "υφαντουργείο — textile mill", "κανναβουργεία": "κανναβουργείο — hemp factory", "υπαίθριο": "υπαίθριος — open-air"},
})
ITEMS.append({
 "id": "l82-rep-vinsanto", "title": "Το Βινσάντο της Σαντορίνης", "title_en": "Vinsanto of Santorini", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα γλυκό κρασί της Σαντορίνης, σε μια εκπομπή για τα τοπικά προϊόντα.",
 "script": [
  L("Ρεπόρτερ", "m", "Στη Σαντορίνη τα αμπέλια δεν μοιάζουν με εκείνα που ξέρουμε. Τα κλήματα πλέκονται χαμηλά, σε σχήμα καλαθιού, για να προστατεύουν τα σταφύλια από τους δυνατούς ανέμους και τον ήλιο. Και επειδή το ηφαιστειακό έδαφος δεν ευνοεί τη φυλλοξήρα, τα αμπέλια του νησιού γλίτωσαν από την ασθένεια που κατέστρεψε στα τέλη του δέκατου ένατου αιώνα τα περισσότερα αμπέλια της Ευρώπης.", "On Santorini the vineyards don't look like the ones we know. The vines are woven low, in the shape of a basket, to protect the grapes from the strong winds and the sun. And because the volcanic soil doesn't favour phylloxera, the island's vineyards escaped the disease that destroyed most of Europe's vineyards at the end of the nineteenth century."),
  L("Ρεπόρτερ", "m", "Από αυτά τα αμπέλια βγαίνει και το Βινσάντο, ένα γλυκό κρασί με μεγάλη ιστορία. Μετά τον τρύγο, τα σταφύλια απλώνονται στον ήλιο για περίπου δύο εβδομάδες, ώσπου να ζαρώσουν και να συγκεντρώσουν τη ζάχαρή τους. Έτσι, από πολλά κιλά σταφύλια βγαίνει πολύ λίγος χυμός, πηχτός σαν μέλι.", "From these vineyards also comes Vinsanto, a sweet wine with a long history. After the harvest, the grapes are spread out in the sun for about two weeks, until they shrivel and concentrate their sugar. So from many kilos of grapes comes very little juice, thick as honey."),
  L("Ρεπόρτερ", "m", "Το κρασί ωριμάζει για τουλάχιστον δύο χρόνια σε βαρέλια, και αρκετοί οινοποιοί το αφήνουν πολύ περισσότερο. Οι ντόπιοι το έπιναν παραδοσιακά σε γιορτές και το χρησιμοποιούσαν ως κρασί της Θείας Κοινωνίας. Σήμερα, τα παλιά οινοποιεία, οι λεγόμενες κάναβες, δέχονται επισκέπτες για γευσιγνωσία.", "The wine matures for at least two years in barrels, and many winemakers leave it much longer. Locals traditionally drank it at festivals and used it as communion wine. Today, the old wineries, the so-called kanaves, welcome visitors for tastings."),
 ],
 "questions": [
  Q("Γιατί τα κλήματα στη Σαντορίνη πλέκονται χαμηλά σε σχήμα καλαθιού;", ["Για να μαζεύονται πιο εύκολα", "Για να προστατεύουν τα σταφύλια από τον άνεμο και τον ήλιο", "Για να φαίνονται όμορφα στους τουρίστες", "Γιατί έτσι ποτίζονται καλύτερα"], 1, "για να προστατεύουν τα σταφύλια από τους δυνατούς ανέμους και τον ήλιο"),
  Q("Τι γίνεται με τα σταφύλια μετά τον τρύγο;", ["Πατιούνται αμέσως", "Απλώνονται στον ήλιο για περίπου δύο εβδομάδες", "Μπαίνουν στο ψυγείο", "Πωλούνται στην αγορά"], 1, "τα σταφύλια απλώνονται στον ήλιο για περίπου δύο εβδομάδες"),
  Q("Πόσο ωριμάζει τουλάχιστον το κρασί;", ["Έξι μήνες", "Δύο χρόνια", "Δέκα χρόνια", "Έναν μήνα"], 1, "Το κρασί ωριμάζει για τουλάχιστον δύο χρόνια σε βαρέλια"),
 ],
 "gloss": {"κλήματα": "κλήμα — vine", "πλέκονται": "πλέκομαι — to be woven, twined", "ηφαιστειακό": "ηφαιστειακός — volcanic", "ευνοεί": "ευνοώ — to favour", "φυλλοξήρα": "φυλλοξήρα — phylloxera (vine pest)", "τρύγο": "τρύγος — grape harvest", "ζαρώσουν": "ζαρώνω — to shrivel, wrinkle", "πηχτός": "πηχτός — thick", "βαρέλια": "βαρέλι — barrel", "οινοποιοί": "οινοποιός — winemaker", "Θείας Κοινωνίας": "Θεία Κοινωνία — Holy Communion", "κάναβες": "κάναβα — traditional winery (Santorini)", "γευσιγνωσία": "γευσιγνωσία — tasting"},
})
ITEMS.append({
 "id": "l82-mono-monothesio", "title": "Δασκάλα σε μονοθέσιο σχολείο", "title_en": "Teacher in a one-teacher school", "type": "monologue", "level": "B2",
 "context_el": "Σε μια εκπομπή για την εκπαίδευση, η Δήμητρα μιλά για τη χρονιά που δίδαξε σε ένα μονοθέσιο δημοτικό σχολείο σε ένα ορεινό χωριό.",
 "script": [
  L("Δήμητρα", "f", "Όταν πήρα τον διορισμό μου, άνοιξα τον χάρτη για να βρω πού είναι το χωριό. Ήταν ψηλά στα Άγραφα, δύο ώρες από την πιο κοντινή πόλη, με δρόμο που τον χειμώνα έκλεινε συχνά από το χιόνι. Το σχολείο είχε μία αίθουσα, μία δασκάλα, εμένα, και έξι μαθητές, από την πρώτη ως την έκτη τάξη.", "When I got my appointment, I opened the map to find where the village was. It was high up in the Agrafa mountains, two hours from the nearest town, with a road that was often closed by snow in winter. The school had one classroom, one teacher, me, and six pupils, from first to sixth grade."),
  L("Δήμητρα", "f", "Στην αρχή δεν ήξερα πώς να διδάξω έξι τάξεις ταυτόχρονα. Σιγά σιγά βρήκα τον τρόπο: όσο εγώ δούλευα με τους μικρούς, οι μεγάλοι έλυναν ασκήσεις, και μετά οι μεγάλοι βοηθούσαν τους μικρούς να διαβάσουν. Ανακάλυψα ότι τα παιδιά μαθαίνουν πολλά όταν εξηγούν κάτι σε κάποιον άλλον.", "At first I didn't know how to teach six grades at once. Little by little I found a way: while I worked with the little ones, the older ones did exercises, and then the older ones helped the little ones to read. I discovered that children learn a lot when they explain something to someone else."),
  L("Δήμητρα", "f", "Το σχολείο ήταν η καρδιά του χωριού. Εκεί γιορτάζαμε την εθνική επέτειο, εκεί έρχονταν οι γιαγιάδες να πουν παραμύθια. Όταν τελείωσε η χρονιά, ήξερα ότι, αν κάποτε κλείσει το σχολείο, το χωριό θα αδειάσει. Δυστυχώς, δύο χρόνια μετά, αυτό ακριβώς συνέβη.", "The school was the heart of the village. That's where we celebrated the national holiday, that's where grandmothers came to tell fairy tales. When the year ended, I knew that if the school ever closed, the village would empty. Unfortunately, two years later, that's exactly what happened."),
 ],
 "questions": [
  Q("Πόσους μαθητές είχε το σχολείο;", ["Δύο", "Έξι", "Δώδεκα", "Είκοσι"], 1, "έξι μαθητές, από την πρώτη ως την έκτη τάξη"),
  Q("Τι ανακάλυψε η Δήμητρα για τη μάθηση;", ["Ότι τα παιδιά μαθαίνουν καλύτερα μόνα τους", "Ότι τα παιδιά μαθαίνουν πολλά όταν εξηγούν κάτι σε κάποιον άλλον", "Ότι οι μικροί μαθαίνουν πιο γρήγορα από τους μεγάλους", "Ότι χρειάζονται περισσότεροι δάσκαλοι"], 1, "τα παιδιά μαθαίνουν πολλά όταν εξηγούν κάτι σε κάποιον άλλον"),
  Q("Τι συνέβη δύο χρόνια μετά;", ["Το σχολείο απέκτησε δεύτερη δασκάλα", "Το σχολείο έκλεισε", "Χτίστηκε καινούργιος δρόμος", "Ήρθαν περισσότεροι μαθητές"], 1, "δύο χρόνια μετά, αυτό ακριβώς συνέβη"),
 ],
 "gloss": {"μονοθέσιο": "μονοθέσιο σχολείο — one-teacher school", "διορισμό": "διορισμός — (teaching) appointment", "Άγραφα": "Άγραφα — the Agrafa mountains", "αίθουσα": "αίθουσα — classroom", "ταυτόχρονα": "ταυτόχρονα — at the same time", "έλυναν": "λύνω — to solve", "εθνική επέτειο": "εθνική επέτειος — national holiday", "αδειάσει": "αδειάζω — to empty"},
})
ITEMS.append({
 "id": "l82-mono-votana", "title": "Ο κήπος με τα βότανα", "title_en": "The herb garden", "type": "monologue", "level": "B2",
 "context_el": "Σε μια εκπομπή για τον κήπο και το μπαλκόνι, ο Λευτέρης μιλά για τα βότανα που καλλιεργεί.",
 "script": [
  L("Λευτέρης", "m", "Η γιαγιά μου στην Κρήτη είχε ένα βότανο για κάθε πρόβλημα: δίκταμο για το στομάχι, φασκόμηλο για τον λαιμό, χαμομήλι για τον ύπνο. Όταν ήμουν μικρός, νόμιζα ότι ήταν μάγισσα. Τώρα, στα πενήντα μου, έχω φτιάξει κι εγώ έναν μικρό κήπο με βότανα σε μια ταράτσα στον Πειραιά.", "My grandmother in Crete had a herb for every problem: dittany for the stomach, sage for the throat, chamomile for sleep. When I was little, I thought she was a witch. Now, at fifty, I've made a small herb garden myself on a roof terrace in Piraeus."),
  L("Λευτέρης", "m", "Τα περισσότερα βότανα είναι εύκολα, γιατί είναι φυτά της Μεσογείου. Θέλουν πολύ ήλιο, λίγο νερό και φτωχό χώμα. Το μεγαλύτερο λάθος που κάνουν οι αρχάριοι είναι ότι τα ποτίζουν υπερβολικά. Ο δυόσμος είναι η εξαίρεση: αγαπάει την υγρασία και, αν δεν τον βάλεις σε δική του γλάστρα, θα πνίξει όλα τα άλλα.", "Most herbs are easy, because they are Mediterranean plants. They want lots of sun, little water and poor soil. The biggest mistake beginners make is overwatering them. Mint is the exception: it loves moisture and, if you don't put it in its own pot, it will smother all the others."),
  L("Λευτέρης", "m", "Να πω, πάντως, ότι δεν είμαι γιατρός. Ένα τσάι από φασκόμηλο σε ζεσταίνει τον χειμώνα, αλλά δεν αντικαθιστά τα φάρμακα. Για μένα τα βότανα είναι κυρίως μυρωδιές και αναμνήσεις. Όταν τρίβω ένα φύλλο ρίγανης ανάμεσα στα δάχτυλα, ξαναβρίσκομαι στην αυλή της γιαγιάς μου.", "I should say, though, that I'm not a doctor. A sage tea warms you in winter, but it doesn't replace medicine. For me herbs are mainly smells and memories. When I rub an oregano leaf between my fingers, I'm back in my grandmother's yard."),
 ],
 "questions": [
  Q("Πού έχει φτιάξει ο Λευτέρης τον κήπο του;", ["Στην αυλή της γιαγιάς του", "Σε μια ταράτσα στον Πειραιά", "Σε ένα χωράφι στην Κρήτη", "Σε ένα δημοτικό πάρκο"], 1, "έχω φτιάξει κι εγώ έναν μικρό κήπο με βότανα σε μια ταράτσα στον Πειραιά"),
  Q("Ποιο είναι το μεγαλύτερο λάθος των αρχαρίων;", ["Τα βάζουν στη σκιά", "Τα ποτίζουν υπερβολικά", "Τα φυτεύουν τον χειμώνα", "Χρησιμοποιούν πολύ λίπασμα"], 1, "Το μεγαλύτερο λάθος που κάνουν οι αρχάριοι είναι ότι τα ποτίζουν υπερβολικά"),
  Q("Γιατί πρέπει ο δυόσμος να μπαίνει σε δική του γλάστρα;", ["Γιατί χρειάζεται πολύ ήλιο", "Γιατί αλλιώς θα πνίξει τα άλλα φυτά", "Γιατί μυρίζει πολύ έντονα", "Γιατί είναι πολύ ευαίσθητος"], 1, "αν δεν τον βάλεις σε δική του γλάστρα, θα πνίξει όλα τα άλλα"),
 ],
 "gloss": {"βότανα": "βότανο — herb", "δίκταμο": "δίκταμο — (Cretan) dittany", "φασκόμηλο": "φασκόμηλο — (Greek) sage", "χαμομήλι": "χαμομήλι — chamomile", "μάγισσα": "μάγισσα — witch", "ταράτσα": "ταράτσα — roof terrace", "ποτίζουν": "ποτίζω — to water", "δυόσμος": "δυόσμος — mint", "γλάστρα": "γλάστρα — flowerpot", "πνίξει": "πνίγω — to choke, smother", "ρίγανης": "ρίγανη — oregano"},
})
ITEMS.append({
 "id": "l82-c1-ypomoni", "title": "Το πείραμα με το ζαχαρωτό: τι μετράει πραγματικά;", "title_en": "The marshmallow experiment: what does it really measure?", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την ψυχολογία, ο δημοσιογράφος συζητά με μια αναπτυξιακή ψυχολόγο για ένα διάσημο πείραμα αυτοελέγχου.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί έχουμε ακούσει για το «πείραμα με το ζαχαρωτό». Τι ακριβώς έγινε;", "Many of us have heard of the 'marshmallow experiment'. What exactly happened?"),
  L("Ψυχολόγος", "f", "Στις δεκαετίες του εξήντα και του εβδομήντα, ερευνητές στο Στάνφορντ έβαζαν παιδιά προσχολικής ηλικίας μπροστά σε ένα γλυκό και τους έλεγαν: «Αν περιμένεις μέχρι να γυρίσω, θα πάρεις δύο.» Χρόνια αργότερα, οι ίδιοι ερευνητές διαπίστωσαν ότι τα παιδιά που είχαν περιμένει περισσότερο είχαν κατά μέσο όρο καλύτερες σχολικές επιδόσεις. Έτσι γεννήθηκε η ιδέα ότι ο αυτοέλεγχος στα τέσσερα χρόνια προβλέπει την επιτυχία στη ζωή.", "In the sixties and seventies, researchers at Stanford would put preschool children in front of a sweet and tell them: 'If you wait until I come back, you'll get two.' Years later, the same researchers found that the children who had waited longer had, on average, better school results. That's how the idea was born that self-control at age four predicts success in life."),
  L("Δημοσιογράφος", "m", "Και ισχύει;", "And is it true?"),
  L("Ψυχολόγος", "f", "Είναι πιο περίπλοκο. Μια μεγάλη επανάληψη του πειράματος, το 2018, με πολύ περισσότερα και πιο διαφορετικά παιδιά, βρήκε ότι η σχέση είναι πολύ πιο αδύναμη, και ότι εξασθενεί ακόμα περισσότερο όταν λάβουμε υπόψη το οικογενειακό περιβάλλον και το εισόδημα. Ένα παιδί που μεγαλώνει με λίγα, όπου το φαγητό δεν είναι πάντα σίγουρο, έχει λογικούς λόγους να μην περιμένει.", "It's more complicated. A large replication of the experiment, in 2018, with many more and more diverse children, found that the relationship is much weaker, and that it weakens even further when we take family background and income into account. A child growing up with little, where food isn't always certain, has rational reasons not to wait."),
  L("Δημοσιογράφος", "m", "Δηλαδή η αναμονή εξαρτάται και από την εμπιστοσύνη;", "So waiting also depends on trust?"),
  L("Ψυχολόγος", "f", "Ακριβώς. Σε ένα άλλο πείραμα, πριν από τη δοκιμασία, ένας ερευνητής υποσχέθηκε στα παιδιά καινούργιες κηρομπογιές. Για τα μισά παιδιά κράτησε την υπόσχεσή του, για τα άλλα μισά όχι. Τα παιδιά που είχαν δει τον ενήλικα να τηρεί τον λόγο του περίμεναν πολύ περισσότερο. Ο αυτοέλεγχος, λοιπόν, δεν είναι μόνο χαρακτηριστικό του παιδιού. Είναι και μια λογική απάντηση στον κόσμο που το περιβάλλει.", "Exactly. In another experiment, before the test, a researcher promised the children new crayons. For half the children he kept his promise, for the other half he didn't. The children who had seen the adult keep his word waited much longer. Self-control, then, is not only a trait of the child. It is also a rational response to the world around it."),
 ],
 "questions": [
  Q("Τι διαπίστωσαν αρχικά οι ερευνητές του Στάνφορντ;", ["Ότι κανένα παιδί δεν περίμενε", "Ότι τα παιδιά που περίμεναν περισσότερο είχαν κατά μέσο όρο καλύτερες σχολικές επιδόσεις", "Ότι τα κορίτσια περίμεναν περισσότερο", "Ότι η ζάχαρη βλάπτει τη μνήμη"], 1, "τα παιδιά που είχαν περιμένει περισσότερο είχαν κατά μέσο όρο καλύτερες σχολικές επιδόσεις"),
  Q("Τι βρήκε η επανάληψη του 2018;", ["Ότι η σχέση είναι πολύ πιο αδύναμη, ιδίως αν ληφθεί υπόψη το οικογενειακό περιβάλλον", "Ότι τα αρχικά αποτελέσματα ήταν ακριβή", "Ότι η σχέση είναι ακόμα πιο ισχυρή", "Ότι το πείραμα δεν μπορεί να επαναληφθεί"], 0, "η σχέση είναι πολύ πιο αδύναμη"),
  Q("Τι έδειξε το πείραμα με τις κηρομπογιές;", ["Ότι τα παιδιά προτιμούν τις κηρομπογιές από τα γλυκά", "Ότι τα παιδιά περιμένουν περισσότερο όταν έχουν δει τον ενήλικα να κρατά τον λόγο του", "Ότι οι υποσχέσεις δεν έχουν σημασία", "Ότι τα μεγαλύτερα παιδιά περιμένουν λιγότερο"], 1, "Τα παιδιά που είχαν δει τον ενήλικα να τηρεί τον λόγο του περίμεναν πολύ περισσότερο"),
 ],
 "gloss": {"ζαχαρωτό": "ζαχαρωτό — marshmallow, sweet", "αναπτυξιακή ψυχολόγο": "αναπτυξιακή ψυχολόγος — developmental psychologist", "αυτοελέγχου": "αυτοέλεγχος — self-control", "προσχολικής ηλικίας": "προσχολική ηλικία — preschool age", "επιδόσεις": "επίδοση — performance, results", "προβλέπει": "προβλέπω — to predict", "επανάληψη": "επανάληψη — replication, repetition", "εξασθενεί": "εξασθενώ — to weaken", "λάβουμε υπόψη": "λαμβάνω υπόψη — to take into account", "κηρομπογιές": "κηρομπογιά — crayon", "τηρεί τον λόγο του": "τηρώ τον λόγο μου — to keep one's word"},
})
ITEMS.append({
 "id": "l82-c1-listes", "title": "Γιατί αγαπάμε τις λίστες;", "title_en": "Why do we love lists?", "type": "monologue", "level": "C1",
 "context_el": "Σε ένα πολιτιστικό podcast, ένας δοκιμιογράφος μιλά για τη σχέση μας με τις λίστες.",
 "script": [
  L("Δοκιμιογράφος", "m", "Λίστες για τα ψώνια, λίστες με «δέκα πράγματα που πρέπει να κάνεις πριν από τα τριάντα», λίστες με τα καλύτερα βιβλία της χρονιάς. Ζούμε περικυκλωμένοι από λίστες, και δεν είναι τυχαίο. Η λίστα υπόσχεται κάτι που η ζωή σπάνια προσφέρει: τάξη. Μετατρέπει το χάος σε σειρά, το άπειρο σε πεπερασμένο.", "Shopping lists, lists of 'ten things to do before you're thirty', lists of the year's best books. We live surrounded by lists, and it's no accident. The list promises something life rarely offers: order. It turns chaos into sequence, the infinite into the finite."),
  L("Δοκιμιογράφος", "m", "Οι ψυχολόγοι έχουν παρατηρήσει ότι οι ανολοκλήρωτες εργασίες μάς απασχολούν περισσότερο από τις ολοκληρωμένες· επιστρέφουν στο μυαλό μας και μας ενοχλούν. Όταν γράφουμε μια εκκρεμότητα σε μια λίστα, το μυαλό ησυχάζει, σαν να έχει κάνει ήδη ένα πρώτο βήμα. Και η χαρά του να διαγράφεις κάτι με μια γραμμή είναι, ας το παραδεχτούμε, σχεδόν σωματική.", "Psychologists have observed that unfinished tasks occupy us more than finished ones; they come back to mind and bother us. When we write a pending task on a list, the mind settles, as if it had already taken a first step. And the pleasure of crossing something off with a line is, let's admit it, almost physical."),
  L("Δοκιμιογράφος", "m", "Υπάρχει, όμως, και μια σκοτεινή πλευρά. Οι λίστες του διαδικτύου μάς δίνουν την ψευδαίσθηση ότι κάθε εμπειρία μπορεί να μετρηθεί και να «ολοκληρωθεί». Ένα ταξίδι γίνεται σημάδι σε έναν κατάλογο, ένα βιβλίο αριθμός σε μια ετήσια πρόκληση. Ίσως η πιο ελεύθερη στιγμή να είναι εκείνη που δεν ανήκει σε καμία λίστα.", "There is, however, a dark side too. Internet lists give us the illusion that every experience can be measured and 'completed'. A journey becomes a tick on a checklist, a book a number in a yearly challenge. Perhaps the freest moment is the one that belongs to no list."),
 ],
 "questions": [
  Q("Τι υπόσχεται η λίστα, σύμφωνα με τον ομιλητή;", ["Επιτυχία", "Τάξη", "Πλούτο", "Ελεύθερο χρόνο"], 1, "Η λίστα υπόσχεται κάτι που η ζωή σπάνια προσφέρει: τάξη"),
  Q("Τι συμβαίνει όταν γράφουμε μια εκκρεμότητα σε μια λίστα;", ["Την ξεχνάμε αμέσως", "Το μυαλό ησυχάζει, σαν να έχει κάνει ένα πρώτο βήμα", "Νιώθουμε περισσότερο άγχος", "Την ολοκληρώνουμε πιο γρήγορα"], 1, "το μυαλό ησυχάζει, σαν να έχει κάνει ήδη ένα πρώτο βήμα"),
  Q("Ποια είναι η «σκοτεινή πλευρά» των λιστών;", ["Ότι χάνονται εύκολα", "Ότι δίνουν την ψευδαίσθηση ότι κάθε εμπειρία μπορεί να μετρηθεί και να ολοκληρωθεί", "Ότι παίρνουν πολύ χρόνο", "Ότι είναι πάντα λάθος"], 1, "Οι λίστες του διαδικτύου μάς δίνουν την ψευδαίσθηση ότι κάθε εμπειρία μπορεί να μετρηθεί"),
 ],
 "gloss": {"δοκιμιογράφος": "δοκιμιογράφος — essayist", "περικυκλωμένοι": "περικυκλωμένος — surrounded", "χάος": "χάος — chaos", "πεπερασμένο": "πεπερασμένος — finite", "ανολοκλήρωτες": "ανολοκλήρωτος — unfinished", "εκκρεμότητα": "εκκρεμότητα — pending matter", "ησυχάζει": "ησυχάζω — to settle, calm down", "διαγράφεις": "διαγράφω — to cross out", "ψευδαίσθηση": "ψευδαίσθηση — illusion", "πρόκληση": "πρόκληση — challenge"},
})

rnd = random.Random(82)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-82.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
