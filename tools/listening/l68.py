# Source for library/listening/listening-68.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l68.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l68-ann-proastiakos", "title": "Αλλαγή αποβάθρας στον Προαστιακό", "title_en": "Platform change on the suburban railway", "type": "announcement", "level": "B2",
 "context_el": "Περιμένετε τον Προαστιακό σε έναν σταθμό της Αθήνας. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνήτρια", "f", "Προσοχή, παρακαλώ. Ο συρμός των δέκα και είκοσι προς το αεροδρόμιο δεν θα αναχωρήσει από την αποβάθρα δύο, όπως αναγράφεται στους πίνακες, αλλά από την αποβάθρα τέσσερα. Οι επιβάτες παρακαλούνται να χρησιμοποιήσουν την υπόγεια διάβαση.", "Attention, please. The ten-twenty train to the airport will not depart from platform two, as shown on the boards, but from platform four. Passengers are asked to use the underpass."),
  L("Εκφωνήτρια", "f", "Λόγω εργασιών στη γραμμή, ο συρμός θα έχει καθυστέρηση περίπου δέκα λεπτών. Οι κυλιόμενες σκάλες προς την αποβάθρα τέσσερα δεν λειτουργούν· επιβάτες με αμαξίδια ή βαριές αποσκευές μπορούν να χρησιμοποιήσουν τον ανελκυστήρα στην άκρη του διαδρόμου.", "Because of works on the line, the train will be about ten minutes late. The escalators to platform four are not working; passengers with wheelchairs or heavy luggage can use the lift at the end of the corridor."),
  L("Εκφωνήτρια", "f", "Υπενθυμίζουμε ότι το εισιτήριο για το αεροδρόμιο πρέπει να επικυρωθεί πριν από την επιβίβαση. Ζητούμε συγγνώμη για την ταλαιπωρία.", "We remind you that the airport ticket must be validated before boarding. We apologise for the inconvenience."),
 ],
 "questions": [
  Q("Από ποια αποβάθρα θα αναχωρήσει τελικά ο συρμός;", ["Από την αποβάθρα δύο", "Από την αποβάθρα τέσσερα", "Από την αποβάθρα ένα", "Δεν έχει αποφασιστεί ακόμη"], 1, "από την αποβάθρα τέσσερα"),
  Q("Γιατί θα έχει καθυστέρηση ο συρμός;", ["Λόγω απεργίας", "Λόγω βλάβης στον συρμό", "Λόγω εργασιών στη γραμμή", "Λόγω κακοκαιρίας"], 2, "Λόγω εργασιών στη γραμμή"),
  Q("Τι πρέπει να κάνουν όσοι έχουν βαριές αποσκευές;", ["Να χρησιμοποιήσουν τον ανελκυστήρα", "Να περιμένουν τον επόμενο συρμό", "Να ζητήσουν βοήθεια από το προσωπικό", "Να πάνε στην αποβάθρα δύο"], 0, "μπορούν να χρησιμοποιήσουν τον ανελκυστήρα"),
 ],
 "gloss": {"συρμός": "συρμός — train", "αποβάθρα": "αποβάθρα — platform", "αναγράφεται": "αναγράφομαι — to be shown, written", "υπόγεια διάβαση": "υπόγεια διάβαση — underpass", "κυλιόμενες σκάλες": "κυλιόμενη σκάλα — escalator", "αμαξίδια": "αμαξίδιο — wheelchair", "ανελκυστήρα": "ανελκυστήρας — lift, elevator", "επικυρωθεί": "επικυρώνομαι — to be validated", "επιβίβαση": "επιβίβαση — boarding"},
})

ITEMS.append({
 "id": "l68-vm-nero-pigadiou", "title": "Τα αποτελέσματα για το νερό του πηγαδιού", "title_en": "The results for the well water", "type": "voicemail", "level": "B2",
 "context_el": "Στείλατε ένα δείγμα από το νερό του πηγαδιού στο εξοχικό σας για ανάλυση. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Χημικός", "m", "Καλησπέρα σας, από το χημείο «Ανάλυσις» σας παίρνω, για το δείγμα νερού που μας φέρατε την Τρίτη. Βγήκαν τα αποτελέσματα. Μικρόβια δεν βρήκαμε, αλλά τα νιτρικά είναι πάνω από το επιτρεπτό όριο για πόσιμο νερό.", "Good evening, I'm calling from the Analysis laboratory about the water sample you brought us on Tuesday. The results are out. We didn't find any bacteria, but the nitrates are above the permitted limit for drinking water."),
  L("Χημικός", "m", "Αυτό συμβαίνει συχνά σε περιοχές με καλλιέργειες, λόγω των λιπασμάτων. Σας συμβουλεύω να μην το πίνετε και να μη μαγειρεύετε με αυτό. Για πότισμα, όμως, και για το πλύσιμο της αυλής μπορείτε να το χρησιμοποιείτε κανονικά.", "This often happens in areas with crops, because of fertilisers. I advise you not to drink it or cook with it. For watering, though, and for washing the yard you can use it as normal."),
  L("Χημικός", "m", "Αν θέλετε, μπορούμε να σας προτείνουμε ένα σύστημα φιλτραρίσματος. Τη γραπτή έκθεση θα σας τη στείλουμε με ηλεκτρονικό ταχυδρομείο μέχρι την Παρασκευή. Καλή συνέχεια.", "If you like, we can suggest a filtering system. We will send you the written report by email by Friday. Have a good evening."),
 ],
 "questions": [
  Q("Τι πρόβλημα βρέθηκε στο νερό;", ["Μικρόβια", "Πολύ αλάτι", "Νιτρικά πάνω από το επιτρεπτό όριο", "Σκουριά"], 2, "τα νιτρικά είναι πάνω από το επιτρεπτό όριο"),
  Q("Πού οφείλεται συνήθως το πρόβλημα αυτό;", ["Στα λιπάσματα των καλλιεργειών", "Στους παλιούς σωλήνες", "Στη θάλασσα", "Στην ξηρασία"], 0, "λόγω των λιπασμάτων"),
  Q("Για τι μπορεί να χρησιμοποιηθεί το νερό;", ["Για μαγείρεμα", "Για πότισμα", "Για πόσιμο", "Για τον καφέ"], 1, "Για πότισμα"),
 ],
 "gloss": {"πηγαδιού": "πηγάδι — well", "δείγμα": "δείγμα — sample", "χημείο": "χημείο — (chemical) laboratory", "Μικρόβια": "μικρόβιο — germ, bacterium", "νιτρικά": "νιτρικά — nitrates", "επιτρεπτό όριο": "επιτρεπτό όριο — permitted limit", "πόσιμο": "πόσιμος — drinkable", "λιπασμάτων": "λίπασμα — fertiliser", "πότισμα": "πότισμα — watering", "φιλτραρίσματος": "φιλτράρισμα — filtering", "έκθεση": "έκθεση — report"},
})

ITEMS.append({
 "id": "l68-dia-vapsimo-saloniou", "title": "Τι χρώμα θα βάψουμε το σαλόνι;", "title_en": "What colour shall we paint the living room?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι συζητά πώς θα βάψει το σαλόνι του.",
 "script": [
  L("Δέσποινα", "f", "Λοιπόν, πήρα δείγματα από το χρωματοπωλείο. Εμένα μου αρέσει πολύ αυτό το σκούρο πράσινο. Θα δώσει χαρακτήρα στο σαλόνι.", "So, I got samples from the paint shop. I really like this dark green. It will give the living room character."),
  L("Στέλιος", "m", "Είναι ωραίο, αλλά το σαλόνι μας βλέπει βόρεια και έχει λίγο φως. Με σκούρο χρώμα θα μοιάζει με σπηλιά. Τι λες για το σκούρο πράσινο μόνο στον τοίχο πίσω από τον καναπέ, και τους άλλους τρεις σε ένα ζεστό λευκό;", "It's nice, but our living room faces north and gets little light. With a dark colour it will look like a cave. What about the dark green only on the wall behind the sofa, and the other three in a warm white?"),
  L("Δέσποινα", "f", "Ναι, αυτό μου αρέσει. Και να το κάνουμε μόνοι μας. Ο μάστορας ζήτησε τετρακόσια ευρώ. Με αυτά τα λεφτά παίρνουμε και καινούργιες κουρτίνες.", "Yes, I like that. And let's do it ourselves. The decorator asked for four hundred euros. With that money we can buy new curtains too."),
  L("Στέλιος", "m", "Εντάξει, αλλά πρώτα πρέπει να στοκάρουμε τις ρωγμές πάνω από την πόρτα. Το Σάββατο σκεπάζουμε τα έπιπλα με νάιλον και ξεκινάμε.", "Fine, but first we need to fill the cracks above the door. On Saturday we cover the furniture with plastic sheeting and get started."),
 ],
 "questions": [
  Q("Γιατί ο Στέλιος δεν θέλει όλο το σαλόνι σκούρο πράσινο;", ["Γιατί δεν του αρέσει το πράσινο", "Γιατί το σαλόνι έχει λίγο φως", "Γιατί η μπογιά είναι ακριβή", "Γιατί δεν ταιριάζει με τον καναπέ"], 1, "έχει λίγο φως"),
  Q("Τι αποφασίζουν τελικά για τα χρώματα;", ["Όλους τους τοίχους λευκούς", "Όλους τους τοίχους πράσινους", "Έναν τοίχο πράσινο και τους άλλους λευκούς", "Να ρωτήσουν τον μάστορα"], 2, "τους άλλους τρεις σε ένα ζεστό λευκό"),
  Q("Τι πρέπει να κάνουν πριν βάψουν;", ["Να αγοράσουν κουρτίνες", "Να στοκάρουν τις ρωγμές", "Να μετακινήσουν τον καναπέ", "Να καλέσουν τον μάστορα"], 1, "πρέπει να στοκάρουμε τις ρωγμές"),
 ],
 "gloss": {"χρωματοπωλείο": "χρωματοπωλείο — paint shop", "βλέπει βόρεια": "βλέπω βόρεια — to face north", "σπηλιά": "σπηλιά — cave", "μάστορας": "μάστορας — tradesman, decorator", "στοκάρουμε": "στοκάρω — to fill (with filler)", "ρωγμές": "ρωγμή — crack", "σκεπάζουμε": "σκεπάζω — to cover", "νάιλον": "νάιλον — plastic sheeting"},
})

ITEMS.append({
 "id": "l68-dia-taxidi-gavdo", "title": "Πώς θα πάμε στη Γαύδο;", "title_en": "How shall we get to Gavdos?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο φίλοι οργανώνουν διακοπές στη Γαύδο, νότια της Κρήτης.",
 "script": [
  L("Φώτης", "m", "Κοίταξα τα δρομολόγια. Το καράβι για τη Γαύδο φεύγει από τη Χώρα Σφακίων, αλλά τον Ιούνιο δεν έχει κάθε μέρα. Αν φυσάει πολύ, ακυρώνεται κιόλας.", "I looked at the timetables. The boat to Gavdos leaves from Chora Sfakion, but in June it doesn't go every day. If it's very windy, it's even cancelled."),
  L("Μυρτώ", "f", "Τότε ας μην κλείσουμε πτήση επιστροφής την ίδια μέρα που φεύγουμε από το νησί. Αν κολλήσουμε εκεί, θα χάσουμε το αεροπλάνο. Καλύτερα να μείνουμε ένα βράδυ στα Χανιά πριν πετάξουμε.", "Then let's not book a return flight on the same day we leave the island. If we get stuck there, we'll miss the plane. Better to stay a night in Chania before we fly."),
  L("Φώτης", "m", "Σωστό. Και να πάρουμε μετρητά. Μου είπαν ότι στο νησί δεν υπάρχει ΑΤΜ και πολλά μαγαζιά δεν δέχονται κάρτες.", "Right. And let's take cash. I was told there's no cash machine on the island and many shops don't accept cards."),
  L("Μυρτώ", "f", "Και φακό! Το βράδυ στις παραλίες δεν έχει καθόλου φωτισμό. Γι’ αυτό, λένε, ο έναστρος ουρανός είναι απίστευτος.", "And a torch! At night there's no lighting at all on the beaches. That's why, they say, the starry sky is incredible."),
 ],
 "questions": [
  Q("Τι ισχύει για το καράβι προς τη Γαύδο τον Ιούνιο;", ["Φεύγει τρεις φορές τη μέρα", "Δεν φεύγει κάθε μέρα και μπορεί να ακυρωθεί λόγω αέρα", "Φεύγει από τα Χανιά", "Δεν υπάρχει καράβι τον Ιούνιο"], 1, "τον Ιούνιο δεν έχει κάθε μέρα. Αν φυσάει πολύ, ακυρώνεται κιόλας"),
  Q("Γιατί η Μυρτώ θέλει να μείνουν ένα βράδυ στα Χανιά;", ["Για να δουν την πόλη", "Για να μη χάσουν την πτήση, αν κολλήσουν στο νησί", "Γιατί το ξενοδοχείο είναι φθηνότερο", "Για να πάρουν μετρητά"], 1, "Αν κολλήσουμε εκεί, θα χάσουμε το αεροπλάνο"),
  Q("Γιατί πρέπει να πάρουν μετρητά;", ["Γιατί στο νησί δεν υπάρχει ΑΤΜ", "Γιατί το καράβι δέχεται μόνο μετρητά", "Γιατί είναι φθηνότερα", "Γιατί έχασαν τις κάρτες τους"], 0, "στο νησί δεν υπάρχει ΑΤΜ"),
 ],
 "gloss": {"δρομολόγια": "δρομολόγιο — timetable, route", "ακυρώνεται": "ακυρώνομαι — to be cancelled", "κολλήσουμε": "κολλάω — to get stuck", "μετρητά": "μετρητά — cash", "φακό": "φακός — torch, flashlight", "φωτισμό": "φωτισμός — lighting", "έναστρος": "έναστρος — starry"},
})

ITEMS.append({
 "id": "l68-int-archeionomos", "title": "Μια αρχειονόμος", "title_en": "An archivist", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια αρχειονόμο που εργάζεται στα Γενικά Αρχεία του Κράτους.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς κάνει ένας αρχειονόμος;", "What exactly does an archivist do?"),
  L("Αρχειονόμος", "f", "Φροντίζουμε έγγραφα που έχουν ιστορική αξία: τα ταξινομούμε, τα συντηρούμε και τα κάνουμε διαθέσιμα στο κοινό. Τα τελευταία χρόνια ψηφιοποιούμε πολλά από αυτά, γιατί το χαρτί είναι εύθραυστο και κάθε φορά που κάποιος το πιάνει, φθείρεται λίγο.", "We look after documents of historical value: we classify them, conserve them and make them available to the public. In recent years we've been digitising many of them, because paper is fragile and every time someone handles it, it wears a little."),
  L("Δημοσιογράφος", "m", "Ποιοι έρχονται στα Αρχεία;", "Who comes to the Archives?"),
  L("Αρχειονόμος", "f", "Ιστορικοί και φοιτητές, φυσικά. Όμως όλο και περισσότεροι είναι απλοί πολίτες που ψάχνουν την ιστορία της οικογένειάς τους: ένα μητρώο του στρατού με το όνομα του προπάππου τους, ένα συμβόλαιο για το πατρικό σπίτι. Κάποιοι συγκινούνται τόσο, που κλαίνε μπροστά μου.", "Historians and students, of course. But more and more are ordinary citizens looking into their family history: an army register with their great-grandfather's name, a contract for the family home. Some are so moved that they cry in front of me."),
 ],
 "questions": [
  Q("Γιατί ψηφιοποιούν τα έγγραφα;", ["Για να τα πουλήσουν", "Γιατί το χαρτί είναι εύθραυστο και φθείρεται", "Γιατί δεν έχουν χώρο", "Γιατί το ζήτησε η κυβέρνηση"], 1, "γιατί το χαρτί είναι εύθραυστο"),
  Q("Ποιοι έρχονται όλο και συχνότερα στα Αρχεία;", ["Τουρίστες", "Δημοσιογράφοι", "Απλοί πολίτες που ψάχνουν την ιστορία της οικογένειάς τους", "Δικηγόροι"], 2, "απλοί πολίτες που ψάχνουν την ιστορία της οικογένειάς τους"),
  Q("Τι συμβαίνει μερικές φορές με τους επισκέπτες;", ["Θυμώνουν", "Συγκινούνται και κλαίνε", "Φεύγουν απογοητευμένοι", "Χάνουν τα έγγραφα"], 1, "Κάποιοι συγκινούνται τόσο, που κλαίνε μπροστά μου"),
 ],
 "gloss": {"αρχειονόμος": "αρχειονόμος — archivist", "έγγραφα": "έγγραφο — document", "ταξινομούμε": "ταξινομώ — to classify, sort", "συντηρούμε": "συντηρώ — to conserve, maintain", "ψηφιοποιούμε": "ψηφιοποιώ — to digitise", "εύθραυστο": "εύθραυστος — fragile", "φθείρεται": "φθείρομαι — to wear, deteriorate", "μητρώο": "μητρώο — register", "προπάππου": "προπάππους — great-grandfather", "συμβόλαιο": "συμβόλαιο — contract"},
})

ITEMS.append({
 "id": "l68-rep-elia-vouvon", "title": "Η ελιά των Βουβών", "title_en": "The olive tree of Vouves", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από ένα χωριό των Χανίων στην Κρήτη.",
 "script": [
  L("Ρεπόρτερ", "f", "Βρίσκομαι στις Άνω Βούβες, ένα μικρό χωριό κοντά στα Χανιά, μπροστά σε μια ελιά που θεωρείται από τις αρχαιότερες στον κόσμο. Οι επιστήμονες δεν συμφωνούν για την ακριβή ηλικία της· οι εκτιμήσεις φτάνουν τις τρεις χιλιάδες χρόνια και ακόμη περισσότερο.", "I'm in Ano Vouves, a small village near Chania, in front of an olive tree that is considered one of the oldest in the world. Scientists don't agree on its exact age; estimates reach three thousand years and even more."),
  L("Ρεπόρτερ", "f", "Ο κορμός της είναι τόσο φαρδύς, που χρειάζονται αρκετοί άνθρωποι πιασμένοι χέρι χέρι για να τον αγκαλιάσουν. Κι όμως, το δέντρο δίνει ακόμη ελιές. Το 1997 ανακηρύχθηκε διατηρητέο μνημείο της φύσης.", "Its trunk is so wide that it takes several people holding hands to encircle it. And yet the tree still bears olives. In 1997 it was declared a protected natural monument."),
  L("Ρεπόρτερ", "f", "Το 2004, κλαδιά από αυτή την ελιά χρησιμοποιήθηκαν για τα στεφάνια των νικητών του μαραθωνίου στους Ολυμπιακούς Αγώνες της Αθήνας. Δίπλα στο δέντρο λειτουργεί σήμερα ένα μικρό μουσείο της ελιάς, που δέχεται χιλιάδες επισκέπτες κάθε χρόνο.", "In 2004, branches from this olive tree were used for the wreaths of the marathon winners at the Athens Olympic Games. Next to the tree there is now a small olive museum, which receives thousands of visitors every year."),
 ],
 "questions": [
  Q("Τι ισχύει για την ηλικία της ελιάς;", ["Είναι ακριβώς δύο χιλιάδων ετών", "Οι επιστήμονες δεν συμφωνούν για την ακριβή ηλικία της", "Φυτεύτηκε τον 19ο αιώνα", "Είναι η αρχαιότερη ελιά της Ευρώπης σίγουρα"], 1, "Οι επιστήμονες δεν συμφωνούν για την ακριβή ηλικία της"),
  Q("Τι ισχύει για το δέντρο σήμερα;", ["Έχει ξεραθεί", "Δίνει ακόμη ελιές", "Μεταφέρθηκε σε μουσείο", "Κόπηκε μετά το 2004"], 1, "το δέντρο δίνει ακόμη ελιές"),
  Q("Για τι χρησιμοποιήθηκαν κλαδιά του το 2004;", ["Για τη φλόγα των Αγώνων", "Για τα στεφάνια των νικητών του μαραθωνίου", "Για τη διακόσμηση του σταδίου", "Για ένα γραμματόσημο"], 1, "για τα στεφάνια των νικητών του μαραθωνίου"),
 ],
 "gloss": {"αρχαιότερες": "αρχαιότερος — oldest", "εκτιμήσεις": "εκτίμηση — estimate", "κορμός": "κορμός — trunk", "φαρδύς": "φαρδύς — wide", "αγκαλιάσουν": "αγκαλιάζω — to embrace, encircle", "ανακηρύχθηκε": "ανακηρύσσομαι — to be declared", "διατηρητέο μνημείο": "διατηρητέο μνημείο — protected monument", "κλαδιά": "κλαδί — branch", "στεφάνια": "στεφάνι — wreath"},
})

ITEMS.append({
 "id": "l68-mono-scholikos-trochonomos", "title": "Σχολικός τροχονόμος στα εβδομήντα", "title_en": "A school crossing volunteer at seventy", "type": "monologue", "level": "B2",
 "context_el": "Ένας συνταξιούχος μιλά για την εθελοντική του δουλειά ως σχολικός τροχονόμος έξω από ένα δημοτικό σχολείο.",
 "script": [
  L("Θανάσης", "m", "Όταν βγήκα στη σύνταξη, τα πρώτα μου πρωινά ήταν άδεια. Ένας φίλος μού είπε ότι ο δήμος ζητούσε εθελοντές για να βοηθούν τα παιδιά να περνούν τον δρόμο έξω από τα σχολεία. Έκανα μια σύντομη εκπαίδευση, μου έδωσαν ένα πορτοκαλί γιλέκο και μια πινακίδα «Στοπ», και ξεκίνησα.", "When I retired, my first mornings were empty. A friend told me the municipality was looking for volunteers to help children cross the road outside schools. I did a short training course, they gave me an orange vest and a 'Stop' sign, and I started."),
  L("Θανάσης", "m", "Κάθε πρωί από τις οχτώ παρά τέταρτο μέχρι τις οχτώ και τέταρτο στέκομαι στη διάβαση. Οι περισσότεροι οδηγοί σταματούν πρόθυμα, αλλά υπάρχουν και κάποιοι βιαστικοί που κορνάρουν. Δεν θυμώνω· τους χαμογελάω και περιμένω να περάσει και το τελευταίο παιδί.", "Every morning from a quarter to eight until a quarter past eight I stand at the crossing. Most drivers stop willingly, but there are also some people in a hurry who honk. I don't get angry; I smile at them and wait for the last child to cross."),
  L("Θανάσης", "m", "Τα παιδιά με λένε «κύριο Στοπ». Τα Χριστούγεννα μού έφεραν μια κάρτα με εκατό υπογραφές. Την έχω κορνιζάρει. Δεν πληρώνομαι, αλλά δεν έχω κάνει πιο ικανοποιητική δουλειά στη ζωή μου.", "The children call me 'Mr Stop'. At Christmas they brought me a card with a hundred signatures. I've had it framed. I don't get paid, but I've never done a more satisfying job in my life."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε ο Θανάσης αυτή τη δουλειά;", ["Τον προσέλαβε το σχολείο", "Ένας φίλος του είπε ότι ο δήμος ζητούσε εθελοντές", "Ήταν παλιός τροχονόμος", "Το εγγόνι του τον παρακάλεσε"], 1, "Ένας φίλος μού είπε ότι ο δήμος ζητούσε εθελοντές"),
  Q("Πώς αντιδρά στους οδηγούς που κορνάρουν;", ["Τους φωνάζει", "Γράφει τον αριθμό τους", "Τους χαμογελάει και περιμένει", "Καλεί την αστυνομία"], 2, "τους χαμογελάω και περιμένω"),
  Q("Τι του έφεραν τα παιδιά τα Χριστούγεννα;", ["Ένα γιλέκο", "Μια κάρτα με εκατό υπογραφές", "Ένα κουτί γλυκά", "Μια καινούργια πινακίδα"], 1, "μια κάρτα με εκατό υπογραφές"),
 ],
 "gloss": {"τροχονόμος": "τροχονόμος — traffic warden", "σύνταξη": "σύνταξη — pension, retirement", "εθελοντές": "εθελοντής — volunteer", "γιλέκο": "γιλέκο — vest", "πινακίδα": "πινακίδα — sign", "διάβαση": "διάβαση — (pedestrian) crossing", "πρόθυμα": "πρόθυμα — willingly", "κορνάρουν": "κορνάρω — to honk", "κορνιζάρει": "κορνιζάρω — to frame", "ικανοποιητική": "ικανοποιητικός — satisfying"},
})

ITEMS.append({
 "id": "l68-mono-stathero-tilefono", "title": "Γιατί κράτησα το σταθερό τηλέφωνο", "title_en": "Why I kept my landline", "type": "monologue", "level": "B2",
 "context_el": "Μια γυναίκα εξηγεί γιατί δεν κατάργησε το σταθερό της τηλέφωνο.",
 "script": [
  L("Αλεξάνδρα", "f", "Όλοι οι φίλοι μου έχουν καταργήσει το σταθερό. «Τι το θες;» με ρωτούν. «Πληρώνεις άδικα.» Κι όμως, εγώ το κράτησα, και δεν είναι από νοσταλγία.", "All my friends have got rid of their landlines. 'What do you need it for?' they ask me. 'You're paying for nothing.' And yet I kept it, and it's not out of nostalgia."),
  L("Αλεξάνδρα", "f", "Πρώτα απ’ όλα, ο αριθμός είναι ο ίδιος εδώ και τριάντα χρόνια. Τον ξέρουν απέξω η μητέρα μου, οι θείες μου, ο γιατρός μου. Όταν έχασα το κινητό μου πέρσι, ήταν ο μόνος τρόπος να με βρουν. Επιπλέον, στο σπίτι το κινητό μου πιάνει άσχημα, ενώ με το σταθερό ακούω καθαρά.", "First of all, the number has been the same for thirty years. My mother, my aunts and my doctor know it by heart. When I lost my mobile last year, it was the only way they could reach me. Besides, my mobile gets poor reception at home, while on the landline I hear clearly."),
  L("Αλεξάνδρα", "f", "Αλλά ο πιο σημαντικός λόγος είναι άλλος: όταν μιλάω στο σταθερό, κάθομαι στην πολυθρόνα και δεν κάνω τίποτε άλλο. Δεν κοιτάζω μηνύματα, δεν ανοίγω εφαρμογές. Απλώς ακούω. Οι φίλοι μου λένε ότι στο σταθερό είμαι πιο καλή ακροάτρια.", "But the most important reason is another: when I talk on the landline, I sit in the armchair and do nothing else. I don't look at messages, I don't open apps. I just listen. My friends say I'm a better listener on the landline."),
 ],
 "questions": [
  Q("Τι λένε οι φίλοι της για το σταθερό;", ["Ότι είναι πιο φθηνό", "Ότι πληρώνει άδικα", "Ότι θέλουν κι αυτοί ένα", "Ότι είναι πιο ασφαλές"], 1, "Πληρώνεις άδικα"),
  Q("Τι έγινε πέρσι;", ["Έχασε το κινητό της", "Άλλαξε αριθμό", "Μετακόμισε", "Χάλασε το σταθερό"], 0, "Όταν έχασα το κινητό μου πέρσι"),
  Q("Ποιος είναι ο πιο σημαντικός λόγος για την Αλεξάνδρα;", ["Η νοσταλγία", "Το χαμηλό κόστος", "Ότι στο σταθερό συγκεντρώνεται και απλώς ακούει", "Ότι η μητέρα της δεν έχει κινητό"], 2, "Απλώς ακούω"),
 ],
 "gloss": {"σταθερό": "σταθερό (τηλέφωνο) — landline", "καταργήσει": "καταργώ — to abolish, get rid of", "άδικα": "άδικα — for nothing, in vain", "νοσταλγία": "νοσταλγία — nostalgia", "απέξω": "απέξω — by heart", "πιάνει άσχημα": "πιάνω άσχημα — to get poor reception", "πολυθρόνα": "πολυθρόνα — armchair", "ακροάτρια": "ακροάτρια — listener (f.)"},
})

ITEMS.append({
 "id": "l68-c1-thermikes-nisides", "title": "Οι πόλεις που ψήνονται", "title_en": "Cities that bake", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια πολεοδόμο για το φαινόμενο της θερμικής νησίδας στις πόλεις.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι είναι αυτό που οι επιστήμονες ονομάζουν «αστική θερμική νησίδα»;", "What is it that scientists call an 'urban heat island'?"),
  L("Πολεοδόμος", "f", "Είναι το φαινόμενο κατά το οποίο το κέντρο μιας πόλης είναι αισθητά θερμότερο από τις γύρω περιοχές, κυρίως τη νύχτα. Η άσφαλτος και το σκυρόδεμα απορροφούν τη θερμότητα όλη μέρα και την αποδίδουν σιγά σιγά μετά τη δύση του ηλίου. Προσθέστε τα κλιματιστικά, που αποβάλλουν ζεστό αέρα στον δρόμο, και την έλλειψη πρασίνου, και έχετε μια πόλη που δεν δροσίζει ποτέ.", "It's the phenomenon whereby the centre of a city is noticeably hotter than the surrounding areas, mainly at night. Asphalt and concrete absorb heat all day and release it slowly after sunset. Add the air conditioners, which expel hot air into the street, and the lack of greenery, and you have a city that never cools down."),
  L("Δημοσιογράφος", "m", "Και ποιες είναι οι συνέπειες;", "And what are the consequences?"),
  L("Πολεοδόμος", "f", "Οι νύχτες χωρίς δροσιά είναι επικίνδυνες, ιδίως για τους ηλικιωμένους, γιατί ο οργανισμός δεν προλαβαίνει να ανακάμψει. Γι’ αυτό η Αθήνα ήταν το 2021 η πρώτη ευρωπαϊκή πόλη που όρισε υπεύθυνη για τη διαχείριση του καύσωνα. Οι λύσεις υπάρχουν: δέντρα, που σκιάζουν και δροσίζουν με την εξάτμιση, πράσινες ταράτσες, ανοιχτόχρωμα υλικά που αντανακλούν το φως αντί να το απορροφούν. Το δύσκολο δεν είναι η τεχνολογία, αλλά η βούληση και ο χρόνος, γιατί ένα δέντρο θέλει χρόνια για να μεγαλώσει.", "Nights without cool air are dangerous, especially for the elderly, because the body doesn't have time to recover. That's why in 2021 Athens became the first European city to appoint an officer responsible for managing heatwaves. The solutions exist: trees, which give shade and cool through evaporation, green roofs, light-coloured materials that reflect light instead of absorbing it. The hard part isn't the technology but the will and the time, because a tree takes years to grow."),
 ],
 "questions": [
  Q("Πότε είναι πιο έντονη η διαφορά θερμοκρασίας;", ["Το μεσημέρι", "Κυρίως τη νύχτα", "Τον χειμώνα", "Το πρωί"], 1, "κυρίως τη νύχτα"),
  Q("Τι κάνουν η άσφαλτος και το σκυρόδεμα;", ["Αντανακλούν τη θερμότητα", "Απορροφούν τη θερμότητα και την αποδίδουν μετά τη δύση του ηλίου", "Δροσίζουν τον αέρα", "Εμποδίζουν τον αέρα"], 1, "απορροφούν τη θερμότητα όλη μέρα και την αποδίδουν σιγά σιγά μετά τη δύση του ηλίου"),
  Q("Τι έκανε η Αθήνα το 2021;", ["Φύτεψε ένα εκατομμύριο δέντρα", "Απαγόρευσε τα κλιματιστικά", "Όρισε υπεύθυνη για τη διαχείριση του καύσωνα", "Έβαψε όλους τους δρόμους λευκούς"], 2, "όρισε υπεύθυνη για τη διαχείριση του καύσωνα"),
  Q("Ποιο είναι, κατά την πολεοδόμο, το δυσκολότερο;", ["Η τεχνολογία", "Το κόστος των υλικών", "Η βούληση και ο χρόνος", "Η αντίδραση των κατοίκων"], 2, "Το δύσκολο δεν είναι η τεχνολογία, αλλά η βούληση και ο χρόνος"),
 ],
 "gloss": {"πολεοδόμο": "πολεοδόμος — urban planner", "θερμικής νησίδας": "θερμική νησίδα — heat island", "αισθητά": "αισθητά — noticeably", "σκυρόδεμα": "σκυρόδεμα — concrete", "αποδίδουν": "αποδίδω — to give back, release", "αποβάλλουν": "αποβάλλω — to expel", "ανακάμψει": "ανακάμπτω — to recover", "καύσωνα": "καύσωνας — heatwave", "εξάτμιση": "εξάτμιση — evaporation", "αντανακλούν": "αντανακλώ — to reflect", "βούληση": "βούληση — will"},
})

ITEMS.append({
 "id": "l68-c1-glossiko-zitima", "title": "Το γλωσσικό ζήτημα", "title_en": "The Greek language question", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από διάλεξη γλωσσολόγου για τη διαμάχη ανάμεσα στην καθαρεύουσα και τη δημοτική.",
 "script": [
  L("Γλωσσολόγος", "m", "Για σχεδόν δύο αιώνες, οι Έλληνες διαφωνούσαν έντονα για το ποια μορφή της γλώσσας τους έπρεπε να γράφουν. Από τη μία πλευρά ήταν η καθαρεύουσα, μια λόγια γλώσσα που προσπαθούσε να πλησιάσει τα αρχαία ελληνικά· από την άλλη η δημοτική, η γλώσσα που μιλούσε ο λαός. Ήδη στις αρχές του 19ου αιώνα ο Αδαμάντιος Κοραής είχε προτείνει μια «μέση οδό»: να «διορθωθεί» η ομιλούμενη γλώσσα, χωρίς να επιβληθεί η αρχαία.", "For almost two centuries, Greeks argued fiercely about which form of their language they should write. On one side was katharevousa, a learned language that tried to come close to ancient Greek; on the other demotic, the language the people spoke. Already at the beginning of the 19th century Adamantios Korais had proposed a 'middle way': to 'correct' the spoken language without imposing the ancient one."),
  L("Γλωσσολόγος", "m", "Το 1888 ο Γιάννης Ψυχάρης δημοσίευσε «Το ταξίδι μου», ένα βιβλίο γραμμένο σε δημοτική, που έγινε το μανιφέστο του δημοτικισμού. Η διαμάχη όμως δεν έμεινε στα βιβλία. Το 1901 η μετάφραση των Ευαγγελίων στη δημοτική προκάλεσε αιματηρές ταραχές στην Αθήνα, τα λεγόμενα «Ευαγγελικά». Η γλώσσα είχε γίνει ζήτημα πολιτικό και ιδεολογικό.", "In 1888 Yannis Psycharis published 'My Journey', a book written in demotic which became the manifesto of demoticism. But the dispute did not stay in books. In 1901 the translation of the Gospels into demotic caused bloody riots in Athens, the so-called 'Gospel riots'. Language had become a political and ideological issue."),
  L("Γλωσσολόγος", "m", "Το ζήτημα έκλεισε επίσημα μόλις το 1976, όταν η δημοτική καθιερώθηκε ως γλώσσα της εκπαίδευσης και της διοίκησης. Λίγα χρόνια αργότερα, το 1982, ήρθε και το μονοτονικό σύστημα. Η σημερινή κοινή νεοελληνική, ωστόσο, δεν είναι η «καθαρή» δημοτική του Ψυχάρη· έχει κρατήσει πλήθος λόγιων λέξεων και εκφράσεων. Θα μπορούσε κανείς να πει ότι, κατά κάποιον τρόπο, επικράτησε η μέση οδός.", "The question was officially closed only in 1976, when demotic was established as the language of education and administration. A few years later, in 1982, came the monotonic system. Today's standard Modern Greek, however, is not Psycharis's 'pure' demotic; it has kept a host of learned words and expressions. One could say that, in a way, the middle way prevailed."),
 ],
 "questions": [
  Q("Τι πρότεινε ο Κοραής;", ["Να επιστρέψουν στα αρχαία ελληνικά", "Μια «μέση οδό» ανάμεσα στην ομιλούμενη και την αρχαία γλώσσα", "Να γράφουν μόνο στη δημοτική", "Να υιοθετηθεί το λατινικό αλφάβητο"], 1, "Αδαμάντιος Κοραής είχε προτείνει μια «μέση οδό»"),
  Q("Τι ήταν «Το ταξίδι μου» του Ψυχάρη;", ["Έναν ταξιδιωτικό οδηγό", "Το μανιφέστο του δημοτικισμού", "Μια μετάφραση των Ευαγγελίων", "Ένα βιβλίο γραμματικής της καθαρεύουσας"], 1, "έγινε το μανιφέστο του δημοτικισμού"),
  Q("Τι προκάλεσε τα «Ευαγγελικά» το 1901;", ["Η μετάφραση των Ευαγγελίων στη δημοτική", "Ένας νέος νόμος για την εκπαίδευση", "Η καθιέρωση του μονοτονικού", "Μια διάλεξη του Κοραή"], 0, "η μετάφραση των Ευαγγελίων στη δημοτική προκάλεσε αιματηρές ταραχές"),
  Q("Πώς χαρακτηρίζει ο ομιλητής τη σημερινή κοινή νεοελληνική;", ["Ως την «καθαρή» δημοτική του Ψυχάρη", "Ως μια μορφή καθαρεύουσας", "Ως γλώσσα που έχει κρατήσει πλήθος λόγιων λέξεων, σαν να επικράτησε η μέση οδός", "Ως γλώσσα που δεν έχει αλλάξει από τον 19ο αιώνα"], 2, "έχει κρατήσει πλήθος λόγιων λέξεων και εκφράσεων"),
 ],
 "gloss": {"καθαρεύουσα": "καθαρεύουσα — katharevousa (learned Greek)", "δημοτική": "δημοτική — demotic Greek", "λόγια": "λόγιος — learned, scholarly", "μέση οδό": "μέση οδός — middle way", "επιβληθεί": "επιβάλλομαι — to be imposed", "μανιφέστο": "μανιφέστο — manifesto", "δημοτικισμού": "δημοτικισμός — demoticism", "αιματηρές": "αιματηρός — bloody", "ταραχές": "ταραχή — riot, unrest", "καθιερώθηκε": "καθιερώνομαι — to be established", "μονοτονικό": "μονοτονικό σύστημα — monotonic accent system", "επικράτησε": "επικρατώ — to prevail"},
})

rnd = random.Random(68)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-68.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
