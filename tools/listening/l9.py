# Source for library/listening/listening-9.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l9.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l9-ann-apagoreftiko", "title": "Απαγορευτικό απόπλου", "title_en": "Ferries kept in port", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση στο λιμάνι του Πειραιά.",
 "script": [
  L("Εκφωνητής", "m", "Ανακοίνωση προς το επιβατικό κοινό. Λόγω των ισχυρών ανέμων, που στο Αιγαίο φτάνουν τα εννιά μποφόρ, το Λιμενικό έχει εκδώσει απαγορευτικό απόπλου για όλα τα πλοία με προορισμό τις Κυκλάδες. Τα δρομολόγια της πρωινής ζώνης δεν θα πραγματοποιηθούν.", "Announcement to passengers. Owing to strong winds, reaching force nine in the Aegean, the coastguard has banned all ships bound for the Cyclades from sailing. The morning sailings will not take place."),
  L("Εκφωνητής", "m", "Οι επιβάτες παρακαλούνται να μην εγκαταλείψουν τον χώρο του λιμανιού και να παρακολουθούν τις ανακοινώσεις, καθώς, σύμφωνα με την πρόγνωση, οι άνεμοι αναμένεται να εξασθενήσουν μετά το μεσημέρι. Αν η απαγόρευση αρθεί, τα πλοία θα αναχωρήσουν με τη σειρά των αρχικών δρομολογίων.", "Passengers are requested not to leave the port area and to follow the announcements, as, according to the forecast, the winds are expected to weaken after midday. If the ban is lifted, the ships will depart in the order of the original sailings."),
  L("Εκφωνητής", "m", "Τα εισιτήρια ισχύουν για οποιοδήποτε δρομολόγιο της ίδιας εταιρείας τις επόμενες επτά ημέρες. Όσοι επιθυμούν επιστροφή χρημάτων μπορούν να απευθυνθούν στα εκδοτήρια της Πύλης Ε7, χωρίς καμία χρέωση.", "Tickets are valid for any sailing of the same company over the next seven days. Those who wish to have a refund can go to the ticket offices at Gate E7, free of charge."),
 ],
 "questions": [
  Q("Γιατί δεν αναχωρούν τα πλοία;", ["Λόγω απεργίας των ναυτικών", "Λόγω ισχυρών ανέμων", "Λόγω βλάβης στο λιμάνι", "Λόγω ομίχλης"], 1, "Λόγω των ισχυρών ανέμων ... το Λιμενικό έχει εκδώσει απαγορευτικό απόπλου"),
  Q("Τι ζητείται από τους επιβάτες;", ["Να γυρίσουν στα σπίτια τους", "Να μείνουν στο λιμάνι και να προσέχουν τις ανακοινώσεις", "Να αγοράσουν νέα εισιτήρια", "Να πάνε στο αεροδρόμιο"], 1, "παρακαλούνται να μην εγκαταλείψουν τον χώρο του λιμανιού και να παρακολουθούν τις ανακοινώσεις"),
  Q("Τι ισχύει για τα εισιτήρια;", ["Χάνονται", "Ισχύουν μόνο για το απογευματινό δρομολόγιο", "Ισχύουν για μια εβδομάδα ή επιστρέφονται τα χρήματα χωρίς χρέωση", "Επιστρέφεται το μισό ποσό"], 2, "Τα εισιτήρια ισχύουν για οποιοδήποτε δρομολόγιο ... τις επόμενες επτά ημέρες ... επιστροφή χρημάτων ... χωρίς καμία χρέωση"),
 ],
 "gloss": {"απόπλου": "απόπλους — sailing, departure (of a ship)", "επιβατικό κοινό": "επιβατικό κοινό — passengers (the travelling public)", "μποφόρ": "μποφόρ — (degree on the) Beaufort scale", "Λιμενικό": "Λιμενικό — coastguard", "εκδώσει": "εκδίδω — to issue", "δρομολόγια": "δρομολόγιο — (scheduled) sailing, route", "εξασθενήσουν": "εξασθενώ — to weaken", "αρθεί": "αίρομαι — to be lifted", "εκδοτήρια": "εκδοτήριο — ticket office", "χρέωση": "χρέωση — charge"},
})

ITEMS.append({
 "id": "l9-vm-ekdromi", "title": "Η σχολική εκδρομή", "title_en": "The school trip", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα από την υπεύθυνη καθηγήτρια ενός γυμνασίου προς τους γονείς της τρίτης τάξης.",
 "script": [
  L("Καθηγήτρια", "f", "Καλησπέρα σας, είμαι η κυρία Μαυρίδου, υπεύθυνη για την εκδρομή της Γ΄ Γυμνασίου. Σας τηλεφωνώ γιατί υπάρχει μια αλλαγή: λόγω του καιρού, η τριήμερη εκδρομή στο Ναύπλιο μεταφέρεται μία εβδομάδα αργότερα, από Πέμπτη δεκαέξι έως Σάββατο δεκαοκτώ του μήνα.", "Good evening, this is Mrs Mavridou, in charge of the year-nine school trip. I'm calling because there is a change: because of the weather, the three-day trip to Nafplio is moved a week later, from Thursday the sixteenth to Saturday the eighteenth of the month."),
  L("Καθηγήτρια", "f", "Το κόστος παραμένει το ίδιο, εκατόν σαράντα ευρώ, και περιλαμβάνει το λεωφορείο, δύο διανυκτερεύσεις με πρωινό και τις εισόδους στους αρχαιολογικούς χώρους της Επιδαύρου και των Μυκηνών. Τα γεύματα δεν περιλαμβάνονται.", "The cost stays the same, a hundred and forty euros, and includes the coach, two nights with breakfast and admission to the archaeological sites of Epidaurus and Mycenae. Meals are not included."),
  L("Καθηγήτρια", "f", "Όσοι δεν έχετε επιστρέψει ακόμη την υπεύθυνη δήλωση με την υπογραφή σας, παρακαλώ να τη στείλετε με το παιδί μέχρι την Τρίτη. Χωρίς αυτήν, δυστυχώς, ο μαθητής δεν μπορεί να συμμετάσχει. Αν το παιδί σας έχει κάποια αλλεργία ή παίρνει φάρμακα, γράψτε το στο πίσω μέρος της δήλωσης. Ευχαριστώ πολύ.", "Those of you who have not yet returned the signed declaration, please send it with your child by Tuesday. Without it, unfortunately, the pupil cannot take part. If your child has an allergy or takes medication, write it on the back of the form. Thank you very much."),
 ],
 "questions": [
  Q("Τι αλλάζει στην εκδρομή;", ["Ο προορισμός", "Η ημερομηνία", "Το κόστος", "Η διάρκεια"], 1, "η τριήμερη εκδρομή στο Ναύπλιο μεταφέρεται μία εβδομάδα αργότερα"),
  Q("Τι ΔΕΝ περιλαμβάνεται στο κόστος;", ["Το λεωφορείο", "Το πρωινό", "Οι είσοδοι στους αρχαιολογικούς χώρους", "Το μεσημεριανό και το βραδινό φαγητό"], 3, "Τα γεύματα δεν περιλαμβάνονται."),
  Q("Τι πρέπει να κάνουν οι γονείς μέχρι την Τρίτη;", ["Να πληρώσουν το υπόλοιπο ποσό", "Να επιστρέψουν υπογεγραμμένη την υπεύθυνη δήλωση", "Να τηλεφωνήσουν στο σχολείο", "Να στείλουν τα φάρμακα των παιδιών"], 1, "παρακαλώ να τη στείλετε με το παιδί μέχρι την Τρίτη"),
 ],
 "gloss": {"υπεύθυνη": "υπεύθυνος — in charge, responsible", "μεταφέρεται": "μεταφέρομαι — to be moved, transferred", "διανυκτερεύσεις": "διανυκτέρευση — overnight stay", "αρχαιολογικούς χώρους": "αρχαιολογικός χώρος — archaeological site", "γεύματα": "γεύμα — meal", "υπεύθυνη δήλωση": "υπεύθυνη δήλωση — signed declaration (formal statement)", "υπογραφή": "υπογραφή — signature", "να συμμετάσχει": "συμμετέχω — to take part", "αλλεργία": "αλλεργία — allergy"},
})

ITEMS.append({
 "id": "l9-dia-synelefsi", "title": "Η συνέλευση της πολυκατοικίας", "title_en": "The residents' meeting", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση στη γενική συνέλευση μιας πολυκατοικίας ανάμεσα στον διαχειριστή, τον κύριο Ζαχαρίου, και την ένοικο του τρίτου ορόφου, την κυρία Ηλιοπούλου.",
 "script": [
  L("Κύριος Ζαχαρίου", "m", "Λοιπόν, το πρώτο θέμα είναι το καλοριφέρ. Ο λέβητας είναι είκοσι πέντε χρονών, φέτος χάλασε δύο φορές, και ο τεχνικός λέει ότι δεν αξίζει να τον επισκευάσουμε ξανά. Προτείνω να περάσουμε σε φυσικό αέριο.", "Right, the first item is the central heating. The boiler is twenty-five years old, it broke down twice this year, and the technician says it isn't worth repairing again. I propose we switch to natural gas."),
  L("Κυρία Ηλιοπούλου", "f", "Συμφωνώ ότι κάτι πρέπει να γίνει, αλλά πόσο θα κοστίσει; Πολλοί εδώ είμαστε συνταξιούχοι.", "I agree something must be done, but how much will it cost? Many of us here are pensioners."),
  L("Κύριος Ζαχαρίου", "m", "Η προσφορά που πήραμε είναι γύρω στις δώδεκα χιλιάδες ευρώ για όλη την πολυκατοικία. Μοιράζεται με βάση τα χιλιοστά του καθενός. Για ένα διαμέρισμα σαν το δικό σας, αυτό σημαίνει περίπου οκτακόσια ευρώ, που μπορούν να πληρωθούν σε δέκα δόσεις μαζί με τα κοινόχρηστα.", "The quote we got is around twelve thousand euros for the whole building. It is divided according to each owner's share. For a flat like yours, that means about eight hundred euros, which can be paid in ten instalments with the service charges."),
  L("Κυρία Ηλιοπούλου", "f", "Σε δόσεις είναι πιο λογικό. Και το πετρέλαιο που αγοράσαμε τον Οκτώβριο; Έχει μείνει σχεδόν μισή δεξαμενή.", "In instalments it's more reasonable. And the heating oil we bought in October? There's almost half a tank left."),
  L("Κύριος Ζαχαρίου", "m", "Καλή ερώτηση. Η εγκατάσταση θα γίνει το καλοκαίρι, οπότε το πετρέλαιο θα το κάψουμε μέχρι τον Απρίλιο. Αν περισσέψει κάτι, ο προμηθευτής δέχεται να το αγοράσει πίσω.", "Good question. The installation will be done in the summer, so we'll burn the oil until April. If any is left, the supplier agrees to buy it back."),
  L("Κυρία Ηλιοπούλου", "f", "Τότε εγώ ψηφίζω υπέρ. Αλλά θα ήθελα να δούμε και μια δεύτερη προσφορά, για σύγκριση.", "Then I vote in favour. But I'd like us to see a second quote as well, for comparison."),
 ],
 "questions": [
  Q("Γιατί ο διαχειριστής προτείνει αλλαγή;", ["Γιατί το πετρέλαιο τελείωσε", "Γιατί ο λέβητας είναι παλιός και χαλάει συχνά", "Γιατί το ζήτησαν οι ένοικοι", "Γιατί το επιβάλλει ο νόμος"], 1, "Ο λέβητας είναι είκοσι πέντε χρονών, φέτος χάλασε δύο φορές"),
  Q("Πώς μοιράζεται το κόστος;", ["Ίσα σε όλα τα διαμερίσματα", "Με βάση τα χιλιοστά κάθε ιδιοκτησίας", "Το πληρώνει ο διαχειριστής", "Ανάλογα με τον αριθμό των ενοίκων"], 1, "Μοιράζεται με βάση τα χιλιοστά του καθενός."),
  Q("Τι θα γίνει με το πετρέλαιο που έχει μείνει;", ["Θα πεταχτεί", "Θα πουληθεί αμέσως", "Θα χρησιμοποιηθεί μέχρι τον Απρίλιο και ό,τι περισσέψει θα το αγοράσει ο προμηθευτής", "Θα μοιραστεί στους ενοίκους"], 2, "το πετρέλαιο θα το κάψουμε μέχρι τον Απρίλιο. Αν περισσέψει κάτι, ο προμηθευτής δέχεται να το αγοράσει πίσω."),
  Q("Ποια είναι η τελική θέση της κυρίας Ηλιοπούλου;", ["Είναι αντίθετη", "Ψηφίζει υπέρ αλλά θέλει και δεύτερη προσφορά", "Δεν ψηφίζει", "Θέλει να επισκευαστεί ο παλιός λέβητας"], 1, "εγώ ψηφίζω υπέρ. Αλλά θα ήθελα να δούμε και μια δεύτερη προσφορά"),
 ],
 "gloss": {"συνέλευση": "συνέλευση — meeting, assembly", "διαχειριστή": "διαχειριστής — building manager", "ένοικο": "ένοικος — resident, tenant", "καλοριφέρ": "καλοριφέρ — central heating, radiator", "λέβητας": "λέβητας — boiler", "φυσικό αέριο": "φυσικό αέριο — natural gas", "προσφορά": "προσφορά — quote, offer", "χιλιοστά": "χιλιοστά — share of common charges (per mille of the building)", "δόσεις": "δόση — instalment", "κοινόχρηστα": "κοινόχρηστα — service charges (shared building costs)", "δεξαμενή": "δεξαμενή — tank", "περισσέψει": "περισσεύω — to be left over", "προμηθευτής": "προμηθευτής — supplier", "ψηφίζω υπέρ": "ψηφίζω υπέρ — to vote in favour"},
})

ITEMS.append({
 "id": "l9-dia-taftotita", "title": "Η νέα ταυτότητα", "title_en": "The new identity card", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα αστυνομικό τμήμα ανάμεσα σε έναν πολίτη και μια υπάλληλο του γραφείου ταυτοτήτων.",
 "script": [
  L("Πολίτης", "m", "Καλημέρα. Έχω ραντεβού στις δέκα για έκδοση νέας ταυτότητας. Η παλιά μου είναι από το 1998 και η φωτογραφία δεν μου μοιάζει καθόλου πια.", "Good morning. I have an appointment at ten to get a new identity card. My old one is from 1998 and the photo doesn't look like me at all any more."),
  L("Υπάλληλος", "f", "Καλημέρα σας. Φέρατε τη φωτογραφία; Πρέπει να είναι πρόσφατη, έγχρωμη, με λευκό φόντο και χωρίς γυαλιά.", "Good morning. Did you bring the photo? It must be recent, in colour, with a white background and without glasses."),
  L("Πολίτης", "m", "Ναι, εδώ είναι. Φοράω όμως γυαλιά όλη την ώρα. Δεν πειράζει που στη φωτογραφία δεν τα έχω;", "Yes, here it is. But I wear glasses all the time. Doesn't it matter that I don't have them in the photo?"),
  L("Υπάλληλος", "f", "Όχι, έτσι πρέπει. Οι νέες ταυτότητες έχουν τσιπ με βιομετρικά στοιχεία, και η αναγνώριση γίνεται χωρίς γυαλιά. Τώρα θα πάρουμε και τα δακτυλικά σας αποτυπώματα. Έχετε πληρώσει το παράβολο;", "No, that's how it should be. The new cards have a chip with biometric data, and recognition is done without glasses. Now we'll also take your fingerprints. Have you paid the fee?"),
  L("Πολίτης", "m", "Το πλήρωσα ηλεκτρονικά χθες. Έχω την απόδειξη στο κινητό. Πότε θα είναι έτοιμη;", "I paid it online yesterday. I have the receipt on my phone. When will it be ready?"),
  L("Υπάλληλος", "f", "Σε δύο με τρεις εβδομάδες. Θα σας έρθει μήνυμα για να την παραλάβετε από εδώ, αυτοπροσώπως. Την παλιά σας ταυτότητα την κρατάτε μέχρι τότε· θα την παραδώσετε όταν παραλάβετε τη νέα.", "In two to three weeks. You'll get a message to collect it from here in person. You keep your old card until then; you'll hand it in when you collect the new one."),
 ],
 "questions": [
  Q("Γιατί ο πολίτης θέλει νέα ταυτότητα;", ["Γιατί έχασε την παλιά", "Γιατί η παλιά είναι πολύ παλιά και η φωτογραφία δεν του μοιάζει", "Γιατί άλλαξε όνομα", "Γιατί η παλιά χάλασε"], 1, "Η παλιά μου είναι από το 1998 και η φωτογραφία δεν μου μοιάζει καθόλου πια."),
  Q("Γιατί η φωτογραφία πρέπει να είναι χωρίς γυαλιά;", ["Για λόγους αισθητικής", "Γιατί η βιομετρική αναγνώριση γίνεται χωρίς γυαλιά", "Γιατί τα γυαλιά αντανακλούν το φως", "Γιατί έτσι ήταν πάντα"], 1, "Οι νέες ταυτότητες έχουν τσιπ με βιομετρικά στοιχεία, και η αναγνώριση γίνεται χωρίς γυαλιά."),
  Q("Τι θα γίνει με την παλιά ταυτότητα;", ["Θα την παραδώσει σήμερα", "Θα την κρατήσει για πάντα", "Θα την κρατήσει μέχρι να παραλάβει τη νέα", "Θα την καταστρέψει ο ίδιος"], 2, "Την παλιά σας ταυτότητα την κρατάτε μέχρι τότε· θα την παραδώσετε όταν παραλάβετε τη νέα."),
 ],
 "gloss": {"έκδοση": "έκδοση — issue (of a document)", "έγχρωμη": "έγχρωμος — in colour", "φόντο": "φόντο — background", "τσιπ": "τσιπ — chip", "βιομετρικά στοιχεία": "βιομετρικά στοιχεία — biometric data", "δακτυλικά σας αποτυπώματα": "δακτυλικά αποτυπώματα — fingerprints", "παράβολο": "παράβολο — (official) fee", "απόδειξη": "απόδειξη — receipt", "να την παραλάβετε": "παραλαμβάνω — to collect, receive", "αυτοπροσώπως": "αυτοπροσώπως — in person", "θα την παραδώσετε": "παραδίδω — to hand in"},
})

ITEMS.append({
 "id": "l9-mon-fournos", "title": "Η νύχτα του φούρνου", "title_en": "Night at the bakery", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε τη Βασιλική, που έχει έναν οικογενειακό φούρνο στην Καλαμάτα, να μιλάει για τη δουλειά της.",
 "script": [
  L("Βασιλική", "f", "Όταν οι περισσότεροι πάνε για ύπνο, εγώ ξεκινάω. Στις έντεκα το βράδυ ανοίγω τον φούρνο, ανάβω τα φώτα και ζυμώνω τα πρώτα ψωμιά. Ο φούρνος ήταν του πατέρα μου, και πριν από αυτόν του παππού μου, που έψηνε με ξύλα. Εμείς τώρα έχουμε ηλεκτρικούς φούρνους, αλλά το προζύμι είναι ακόμη το ίδιο, το κρατάμε ζωντανό εδώ και πενήντα χρόνια.", "When most people go to bed, I begin. At eleven at night I open the bakery, turn on the lights and knead the first loaves. The bakery was my father's, and before him my grandfather's, who baked with wood. Now we have electric ovens, but the sourdough starter is still the same: we've kept it alive for fifty years."),
  L("Βασιλική", "f", "Ο κόσμος νομίζει ότι το ψωμί είναι απλό: αλεύρι, νερό, αλάτι. Στην πραγματικότητα, κάθε νύχτα είναι διαφορετική. Αν έχει υγρασία, η ζύμη φουσκώνει αλλιώς· αν κάνει κρύο, θέλει περισσότερο χρόνο. Αυτά δεν τα μαθαίνεις από βιβλία, τα μαθαίνεις με τα χέρια.", "People think bread is simple: flour, water, salt. In reality every night is different. If it's humid, the dough rises differently; if it's cold, it needs more time. You don't learn that from books, you learn it with your hands."),
  L("Βασιλική", "f", "Το δύσκολο δεν είναι η κούραση, είναι ότι ζεις ανάποδα από τους άλλους. Χάνεις γάμους, γιορτές, τα απογεύματα των παιδιών σου. Και όμως, όταν στις έξι ανοίγει η πόρτα και ο πρώτος πελάτης, πάντα ο ίδιος συνταξιούχος, μου λέει «μοσχοβολάει όλος ο δρόμος», ξέρω γιατί το κάνω.", "The hard part isn't the tiredness, it's that you live the opposite way round from everyone else. You miss weddings, celebrations, your children's afternoons. And yet, when at six the door opens and the first customer, always the same pensioner, tells me 'the whole street smells wonderful', I know why I do it."),
 ],
 "questions": [
  Q("Τι έχει μείνει ίδιο από την εποχή του παππού της;", ["Οι φούρνοι με ξύλα", "Το προζύμι", "Το ωράριο", "Το κτίριο"], 1, "το προζύμι είναι ακόμη το ίδιο, το κρατάμε ζωντανό εδώ και πενήντα χρόνια"),
  Q("Τι εννοεί η Βασιλική όταν λέει ότι «κάθε νύχτα είναι διαφορετική»;", ["Ότι κάθε βράδυ φτιάχνει άλλο είδος ψωμιού", "Ότι ο καιρός επηρεάζει τη ζύμη", "Ότι έχει διαφορετικούς υπαλλήλους", "Ότι αλλάζουν οι πελάτες"], 1, "Αν έχει υγρασία, η ζύμη φουσκώνει αλλιώς· αν κάνει κρύο, θέλει περισσότερο χρόνο."),
  Q("Ποιο είναι για εκείνη το πιο δύσκολο κομμάτι της δουλειάς;", ["Η σωματική κούραση", "Τα χαμηλά κέρδη", "Ότι ζει σε διαφορετικό ρυθμό από τους άλλους και χάνει κοινωνικές στιγμές", "Οι απαιτητικοί πελάτες"], 2, "Το δύσκολο δεν είναι η κούραση, είναι ότι ζεις ανάποδα από τους άλλους."),
 ],
 "gloss": {"ζυμώνω": "ζυμώνω — to knead", "έψηνε": "ψήνω — to bake, roast", "ξύλα": "ξύλο — wood, firewood", "προζύμι": "προζύμι — sourdough starter", "αλεύρι": "αλεύρι — flour", "υγρασία": "υγρασία — humidity, damp", "ζύμη": "ζύμη — dough", "φουσκώνει": "φουσκώνω — to rise, swell", "κούραση": "κούραση — tiredness", "ανάποδα": "ανάποδα — the other way round", "μοσχοβολάει": "μοσχοβολάω — to smell wonderful"},
})

ITEMS.append({
 "id": "l9-rep-metro", "title": "Τα αρχαία του μετρό", "title_en": "The metro's antiquities", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τα αρχαία που βρέθηκαν κατά την κατασκευή του μετρό της Θεσσαλονίκης.",
 "script": [
  L("Ρεπόρτερ", "f", "Όποιος κατεβαίνει στον σταθμό Βενιζέλου του μετρό της Θεσσαλονίκης δεν βλέπει μόνο τρένα. Πίσω από γυάλινα τοιχώματα απλώνεται ένα κομμάτι από τον κεντρικό δρόμο της βυζαντινής πόλης, με τις πλάκες του, τα ερείπια καταστημάτων και ένα σταυροδρόμι που χρησιμοποιούνταν για αιώνες.", "Anyone going down into Venizelou station on the Thessaloniki metro doesn't see only trains. Behind glass walls stretches a section of the main street of the Byzantine city, with its paving slabs, the ruins of shops and a crossroads that was used for centuries."),
  L("Ρεπόρτερ", "f", "Τα ευρήματα ήρθαν στο φως στις ανασκαφές που έγιναν πριν από την κατασκευή των σταθμών. Για χρόνια, αρχαιολόγοι, μηχανικοί και πολιτικοί διαφωνούσαν: έπρεπε τα αρχαία να μεταφερθούν αλλού, για να προχωρήσει το έργο, ή να παραμείνουν στη θέση τους; Η διαμάχη καθυστέρησε το μετρό, που περίμενε η πόλη για δεκαετίες.", "The finds came to light in the excavations carried out before the stations were built. For years archaeologists, engineers and politicians disagreed: should the antiquities be moved elsewhere so the project could proceed, or stay where they were? The dispute delayed the metro, which the city had been waiting for for decades."),
  L("Ρεπόρτερ", "f", "Τελικά επιλέχθηκε μια λύση που κράτησε τα περισσότερα ευρήματα στη θέση τους, και το μετρό άνοιξε στο τέλος του 2024. Σήμερα πολλοί επιβάτες λένε ότι δεν θα φανταζόντουσαν να πηγαίνουν στη δουλειά τους περνώντας κάθε πρωί μέσα από χίλια χρόνια ιστορίας.", "In the end a solution was chosen that kept most of the finds in place, and the metro opened at the end of 2024. Today many passengers say they would never have imagined going to work passing through a thousand years of history every morning."),
 ],
 "questions": [
  Q("Τι μπορεί να δει κανείς στον σταθμό Βενιζέλου;", ["Ένα μουσείο με αγάλματα", "Τμήμα του κεντρικού βυζαντινού δρόμου της πόλης", "Ένα αρχαίο θέατρο", "Φωτογραφίες από τις ανασκαφές"], 1, "Πίσω από γυάλινα τοιχώματα απλώνεται ένα κομμάτι από τον κεντρικό δρόμο της βυζαντινής πόλης"),
  Q("Ποιο ήταν το αντικείμενο της διαμάχης;", ["Το κόστος του μετρό", "Το όνομα του σταθμού", "Αν τα αρχαία θα μετακινηθούν ή θα μείνουν στη θέση τους", "Ποιος θα κατασκευάσει το μετρό"], 2, "έπρεπε τα αρχαία να μεταφερθούν αλλού ... ή να παραμείνουν στη θέση τους;"),
  Q("Ποια ήταν η συνέπεια της διαμάχης;", ["Ακυρώθηκε το έργο", "Καθυστέρησε το μετρό", "Καταστράφηκαν αρχαία", "Άλλαξε η διαδρομή του μετρό"], 1, "Η διαμάχη καθυστέρησε το μετρό"),
 ],
 "gloss": {"τοιχώματα": "τοίχωμα — wall, partition", "πλάκες": "πλάκα — slab, paving stone", "ερείπια": "ερείπιο — ruin", "σταυροδρόμι": "σταυροδρόμι — crossroads", "ευρήματα": "εύρημα — find", "ήρθαν στο φως": "έρχομαι στο φως — to come to light", "ανασκαφές": "ανασκαφή — excavation", "διαμάχη": "διαμάχη — dispute"},
})

ITEMS.append({
 "id": "l9-int-greeklish", "title": "Γράφοντας ελληνικά με λατινικούς χαρακτήρες", "title_en": "Writing Greek in Latin letters", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια γλωσσολόγο για τα «greeklish» και τη γραφή στον ψηφιακό κόσμο.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αντωνίου, στις αρχές του 2000 πολλοί προειδοποιούσαν ότι τα greeklish, δηλαδή τα ελληνικά γραμμένα με λατινικούς χαρακτήρες, θα κατέστρεφαν την ελληνική γλώσσα. Τι έγινε τελικά;", "Ms Antoniou, in the early 2000s many people warned that Greeklish, that is Greek written in Latin characters, would destroy the Greek language. What happened in the end?"),
  L("Γλωσσολόγος", "f", "Τίποτα από όσα φοβόντουσαν. Τα greeklish δεν ήταν επιλογή, ήταν ανάγκη: τα πρώτα κινητά και πολλά προγράμματα στον υπολογιστή δεν υποστήριζαν ελληνικούς χαρακτήρες. Μόλις η τεχνολογία το επέτρεψε, η συντριπτική πλειονότητα γύρισε στο ελληνικό αλφάβητο.", "None of what they feared. Greeklish wasn't a choice, it was a necessity: early mobile phones and many computer programs didn't support Greek characters. As soon as the technology allowed it, the overwhelming majority went back to the Greek alphabet."),
  L("Δημοσιογράφος", "m", "Δεν άφησαν όμως κανένα ίχνος;", "But didn't they leave any trace?"),
  L("Γλωσσολόγος", "f", "Άφησαν κάτι ενδιαφέρον: ανέδειξαν πόσο συμβατική είναι η ορθογραφία. Όταν γράφεις «i» για το ι, το η, το υ, το ει και το οι, συνειδητοποιείς ότι πέντε γραφές αντιστοιχούν σε έναν ήχο. Κάποιοι έγραφαν φωνητικά, άλλοι «οπτικά», μιμούμενοι το σχήμα των γραμμάτων, για παράδειγμα «8» για το θήτα. Ήταν, χωρίς να το ξέρουν, ένα μάθημα ιστορίας της γραφής.", "They left something interesting: they showed how conventional spelling is. When you write 'i' for ι, η, υ, ει and οι, you realise that five spellings correspond to one sound. Some wrote phonetically, others 'visually', imitating the shape of the letters, for example '8' for theta. It was, without their knowing it, a lesson in the history of writing."),
  L("Δημοσιογράφος", "m", "Και σήμερα; Ποιο είναι το νέο φόβητρο;", "And today? What is the new bogeyman?"),
  L("Γλωσσολόγος", "f", "Σήμερα ανησυχούμε ότι οι νέοι δεν βάζουν τόνους στα μηνύματα ή ότι γεμίζουν τα κείμενα με αγγλικές λέξεις. Η γλώσσα όμως πάντα δανειζόταν και πάντα προσαρμοζόταν. Αυτό που μετράει δεν είναι να απαγορεύουμε, αλλά να μαθαίνουμε στα παιδιά να αλλάζουν ύφος ανάλογα με την περίσταση: άλλο ένα μήνυμα σε έναν φίλο, άλλο μια αίτηση σε μια δημόσια υπηρεσία.", "Today we worry that young people don't put accents in their messages or that they fill their texts with English words. But language has always borrowed and always adapted. What matters is not to forbid, but to teach children to change register according to the situation: a message to a friend is one thing, an application to a public service another."),
 ],
 "questions": [
  Q("Γιατί, σύμφωνα με τη γλωσσολόγο, εμφανίστηκαν τα greeklish;", ["Επειδή οι νέοι ήθελαν να ξεχωρίσουν", "Επειδή η τεχνολογία δεν υποστήριζε ελληνικούς χαρακτήρες", "Επειδή ήταν πιο γρήγορα στη γραφή", "Επειδή τα δίδασκαν στα σχολεία"], 1, "τα πρώτα κινητά και πολλά προγράμματα στον υπολογιστή δεν υποστήριζαν ελληνικούς χαρακτήρες"),
  Q("Τι «μάθημα» πρόσφεραν, κατά τη γνώμη της, τα greeklish;", ["Έδειξαν ότι η ορθογραφία βασίζεται σε συμβάσεις, αφού πολλές γραφές αποδίδουν τον ίδιο ήχο", "Έμαθαν στους Έλληνες αγγλικά", "Έδειξαν ότι το ελληνικό αλφάβητο είναι ξεπερασμένο", "Βελτίωσαν την ορθογραφία των νέων"], 0, "ανέδειξαν πόσο συμβατική είναι η ορθογραφία ... πέντε γραφές αντιστοιχούν σε έναν ήχο"),
  Q("Τι σημαίνει η «οπτική» γραφή που αναφέρει;", ["Η γραφή με κεφαλαία", "Η αντικατάσταση γραμμάτων με σύμβολα που τους μοιάζουν στο σχήμα", "Η γραφή χωρίς τόνους", "Η χρήση εικονιδίων"], 1, "μιμούμενοι το σχήμα των γραμμάτων, για παράδειγμα «8» για το θήτα"),
  Q("Ποια είναι η θέση της για τις σημερινές ανησυχίες;", ["Ότι πρέπει να απαγορευτούν οι αγγλικές λέξεις", "Ότι οι τόνοι πρέπει να καταργηθούν", "Ότι το ζητούμενο είναι να μάθουν τα παιδιά να προσαρμόζουν το ύφος τους στην περίσταση", "Ότι η γλώσσα κινδυνεύει σοβαρά"], 2, "να μαθαίνουμε στα παιδιά να αλλάζουν ύφος ανάλογα με την περίσταση"),
 ],
 "gloss": {"λατινικούς χαρακτήρες": "λατινικοί χαρακτήρες — Latin characters", "προειδοποιούσαν": "προειδοποιώ — to warn", "υποστήριζαν": "υποστηρίζω — to support", "συντριπτική πλειονότητα": "συντριπτική πλειονότητα — overwhelming majority", "ίχνος": "ίχνος — trace", "ανέδειξαν": "αναδεικνύω — to bring out, highlight", "συμβατική": "συμβατικός — conventional", "συνειδητοποιείς": "συνειδητοποιώ — to realise", "μιμούμενοι": "μιμούμαι — to imitate", "φόβητρο": "φόβητρο — bogeyman, scare", "τόνους": "τόνος — (written) accent", "ύφος": "ύφος — style, register", "περίσταση": "περίσταση — occasion, situation"},
})

ITEMS.append({
 "id": "l9-mon-yperturismos", "title": "Όταν ο τουρισμός γίνεται βάρος", "title_en": "When tourism becomes a burden", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα σχόλιο σε ραδιοφωνική εκπομπή για τον υπερτουρισμό στα ελληνικά νησιά.",
 "script": [
  L("Σχολιαστής", "m", "Κάθε καλοκαίρι οι ίδιες εικόνες: στα στενά της Οίας, χιλιάδες επισκέπτες από κρουαζιερόπλοια περιμένουν με τα κινητά υψωμένα το ίδιο ηλιοβασίλεμα, ενώ οι κάτοικοι δυσκολεύονται να περάσουν για να πάνε στη δουλειά τους. Ο τουρισμός, που για δεκαετίες στήριξε την ελληνική οικονομία, σε ορισμένα μέρη αρχίζει να υπονομεύει τα ίδια τα θεμέλιά του.", "Every summer the same pictures: in the alleys of Oia, thousands of visitors from cruise ships wait, phones held high, for the same sunset, while residents struggle to get through on their way to work. Tourism, which for decades has supported the Greek economy, is in some places starting to undermine its own foundations."),
  L("Σχολιαστής", "m", "Το πρόβλημα δεν είναι οι τουρίστες καθαυτοί, αλλά η συγκέντρωσή τους στον ίδιο τόπο και την ίδια εποχή. Τα νησιά δεν έχουν σχεδιαστεί για να δέχονται σε μια μέρα πολλαπλάσιους ανθρώπους από τον μόνιμο πληθυσμό τους. Το νερό λιγοστεύει, τα σκουπίδια συσσωρεύονται, και τα σπίτια μετατρέπονται σε καταλύματα βραχυχρόνιας μίσθωσης, με αποτέλεσμα ο γιατρός ή ο δάσκαλος που διορίζεται εκεί να μη βρίσκει πού να μείνει.", "The problem is not tourists as such, but their concentration in the same place at the same time. The islands were not designed to receive in one day many times more people than their permanent population. Water runs short, rubbish piles up, and houses are turned into short-term rentals, so that the doctor or teacher posted there can't find anywhere to live."),
  L("Σχολιαστής", "m", "Έχουν ληφθεί κάποια μέτρα, όπως ένα τέλος για τους επιβάτες κρουαζιέρας τους καλοκαιρινούς μήνες. Αλλά κανένα τέλος δεν αρκεί, αν δεν αλλάξουμε τρόπο σκέψης: από το «όσο περισσότεροι, τόσο καλύτερα» στο «τι αντέχει αυτός ο τόπος». Διαφορετικά, κινδυνεύουμε να πουλάμε μια εικόνα που οι ίδιοι έχουμε καταστρέψει.", "Some measures have been taken, such as a fee for cruise passengers in the summer months. But no fee is enough unless we change our way of thinking: from 'the more the better' to 'what can this place bear'. Otherwise we risk selling an image that we ourselves have destroyed."),
 ],
 "questions": [
  Q("Τι υποστηρίζει ο σχολιαστής για τον τουρισμό σε ορισμένα μέρη;", ["Ότι πρέπει να σταματήσει εντελώς", "Ότι αρχίζει να βλάπτει τις ίδιες τις βάσεις του", "Ότι δεν έχει πια οικονομική σημασία", "Ότι είναι η μόνη λύση για τα νησιά"], 1, "σε ορισμένα μέρη αρχίζει να υπονομεύει τα ίδια τα θεμέλιά του"),
  Q("Ποιο είναι, κατά τον σχολιαστή, το πραγματικό πρόβλημα;", ["Η συμπεριφορά των τουριστών", "Οι χαμηλές τιμές", "Η συγκέντρωση πολλών επισκεπτών στον ίδιο τόπο την ίδια εποχή", "Η έλλειψη ξενοδοχείων"], 2, "Το πρόβλημα δεν είναι οι τουρίστες καθαυτοί, αλλά η συγκέντρωσή τους στον ίδιο τόπο και την ίδια εποχή."),
  Q("Ποια συνέπεια της βραχυχρόνιας μίσθωσης αναφέρει;", ["Ότι ακριβαίνουν τα εστιατόρια", "Ότι οι δημόσιοι υπάλληλοι που διορίζονται στα νησιά δεν βρίσκουν σπίτι", "Ότι κλείνουν τα ξενοδοχεία", "Ότι αυξάνονται τα έσοδα των δήμων"], 1, "ο γιατρός ή ο δάσκαλος που διορίζεται εκεί να μη βρίσκει πού να μείνει"),
  Q("Τι προτείνει στο τέλος;", ["Να αυξηθεί το τέλος κρουαζιέρας", "Να απαγορευτούν τα κρουαζιερόπλοια", "Να γίνει πιο ελκυστικός ο χειμερινός τουρισμός", "Μια αλλαγή νοοτροπίας, με γνώμονα το τι αντέχει κάθε τόπος"], 3, "από το «όσο περισσότεροι, τόσο καλύτερα» στο «τι αντέχει αυτός ο τόπος»"),
 ],
 "gloss": {"υπερτουρισμό": "υπερτουρισμός — overtourism", "στενά": "στενό — alley, narrow street", "κρουαζιερόπλοια": "κρουαζιερόπλοιο — cruise ship", "υψωμένα": "υψωμένος — raised, held up", "να υπονομεύει": "υπονομεύω — to undermine", "θεμέλιά": "θεμέλιο — foundation", "καθαυτοί": "καθαυτός — as such, per se", "πολλαπλάσιους": "πολλαπλάσιος — many times more", "συσσωρεύονται": "συσσωρεύομαι — to pile up", "καταλύματα": "κατάλυμα — accommodation, lodging", "βραχυχρόνιας μίσθωσης": "βραχυχρόνια μίσθωση — short-term rental", "διορίζεται": "διορίζομαι — to be appointed, posted", "ληφθεί": "λαμβάνομαι — to be taken (measures)"},
})

ITEMS.append({
 "id": "l9-rep-seismoi", "title": "Ζώντας με τους σεισμούς", "title_en": "Living with earthquakes", "type": "report", "level": "C1",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τη σεισμικότητα της Ελλάδας και την προετοιμασία των πολιτών.",
 "script": [
  L("Ρεπόρτερ", "f", "Η Ελλάδα είναι η πιο σεισμογενής χώρα της Ευρώπης. Κάθε χρόνο καταγράφονται χιλιάδες σεισμικές δονήσεις, οι περισσότερες τόσο μικρές, που δεν τις αντιλαμβάνεται κανείς. Ο λόγος βρίσκεται βαθιά κάτω από τη θάλασσα, εκεί όπου η αφρικανική λιθοσφαιρική πλάκα βυθίζεται κάτω από την ευρασιατική.", "Greece is the most earthquake-prone country in Europe. Every year thousands of tremors are recorded, most of them so small that no one notices them. The reason lies deep under the sea, where the African lithospheric plate sinks beneath the Eurasian one."),
  L("Ρεπόρτερ", "f", "Παρά τη συχνότητα των σεισμών, οι απώλειες σε ανθρώπινες ζωές τις τελευταίες δεκαετίες είναι σχετικά περιορισμένες. Οι σεισμολόγοι το αποδίδουν σε μεγάλο βαθμό στον αντισεισμικό κανονισμό, που αναθεωρήθηκε αυστηρότερα μετά τους μεγάλους σεισμούς της Καλαμάτας το 1986 και της Αθήνας το 1999. Τα κτίρια που χτίστηκαν από τότε έχουν αποδειχθεί πολύ πιο ανθεκτικά.", "Despite the frequency of earthquakes, loss of life in recent decades has been relatively limited. Seismologists attribute this largely to the building code for earthquake resistance, which was made stricter after the major earthquakes in Kalamata in 1986 and Athens in 1999. Buildings constructed since then have proved much more resilient."),
  L("Ρεπόρτερ", "f", "Το αδύναμο σημείο παραμένουν τα παλιά κτίρια και η ελλιπής προετοιμασία των πολιτών. Οι ειδικοί επιμένουν σε απλά πράγματα: να στερεώνουμε τις βιβλιοθήκες στον τοίχο, να έχουμε έτοιμο ένα σακίδιο με νερό, φακό και φάρμακα, και να ξέρουμε ότι κατά τη διάρκεια της δόνησης δεν τρέχουμε στις σκάλες, αλλά καλυπτόμαστε κάτω από ένα γερό τραπέζι. Όπως λένε, τον σεισμό δεν μπορούμε να τον προβλέψουμε, μπορούμε όμως να τον περιμένουμε προετοιμασμένοι.", "The weak point remains old buildings and citizens' inadequate preparation. Experts insist on simple things: fixing bookcases to the wall, keeping a bag ready with water, a torch and medicines, and knowing that during the shaking we don't run to the stairs but take cover under a sturdy table. As they say, we can't predict an earthquake, but we can await it prepared."),
 ],
 "questions": [
  Q("Πού οφείλεται η έντονη σεισμικότητα της Ελλάδας;", ["Στα ηφαίστεια των Κυκλάδων", "Στη βύθιση της αφρικανικής πλάκας κάτω από την ευρασιατική", "Στις γεωτρήσεις", "Στη θερμοκρασία της θάλασσας"], 1, "η αφρικανική λιθοσφαιρική πλάκα βυθίζεται κάτω από την ευρασιατική"),
  Q("Σε τι αποδίδουν οι σεισμολόγοι τις σχετικά λίγες απώλειες;", ["Στην τύχη", "Στο ότι οι σεισμοί γίνονται κυρίως στη θάλασσα", "Στον αυστηρότερο αντισεισμικό κανονισμό", "Στην πρόβλεψη των σεισμών"], 2, "το αποδίδουν σε μεγάλο βαθμό στον αντισεισμικό κανονισμό"),
  Q("Τι συστήνουν οι ειδικοί να κάνουμε κατά τη διάρκεια της δόνησης;", ["Να τρέξουμε έξω από τις σκάλες", "Να καλυφθούμε κάτω από ένα γερό τραπέζι", "Να σταθούμε δίπλα στο παράθυρο", "Να μπούμε στο ασανσέρ"], 1, "δεν τρέχουμε στις σκάλες, αλλά καλυπτόμαστε κάτω από ένα γερό τραπέζι"),
 ],
 "gloss": {"σεισμικότητα": "σεισμικότητα — seismicity", "σεισμογενής": "σεισμογενής — earthquake-prone", "δονήσεις": "δόνηση — tremor, shaking", "αντιλαμβάνεται": "αντιλαμβάνομαι — to perceive, notice", "λιθοσφαιρική πλάκα": "λιθοσφαιρική πλάκα — lithospheric (tectonic) plate", "βυθίζεται": "βυθίζομαι — to sink", "απώλειες": "απώλεια — loss", "το αποδίδουν": "αποδίδω — to attribute", "αντισεισμικό κανονισμό": "αντισεισμικός κανονισμός — seismic building code", "αναθεωρήθηκε": "αναθεωρώ — to revise", "ελλιπής": "ελλιπής — inadequate, incomplete", "στερεώνουμε": "στερεώνω — to fix, secure", "σακίδιο": "σακίδιο — backpack", "φακό": "φακός — torch, flashlight", "γερό": "γερός — sturdy, strong"},
})

ITEMS.append({
 "id": "l9-int-metafrastria", "title": "Οι λέξεις που δεν μεταφράζονται", "title_en": "Words that won't translate", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια μεταφράστρια λογοτεχνίας από τα ελληνικά στα αγγλικά.",
 "script": [
  L("Δημοσιογράφος", "m", "Συχνά ακούμε ότι η ελληνική έχει λέξεις που δεν μεταφράζονται, όπως «φιλότιμο» ή «μεράκι». Ισχύει;", "We often hear that Greek has words that can't be translated, like 'filotimo' or 'meraki'. Is that true?"),
  L("Μεταφράστρια", "f", "Ισχύει και δεν ισχύει. Κάθε γλώσσα έχει λέξεις που δεν έχουν ακριβές αντίστοιχο σε μία λέξη σε άλλη γλώσσα. Αυτό δεν σημαίνει ότι το νόημά τους δεν μπορεί να αποδοθεί. Απλώς ο μεταφραστής πρέπει να επιλέξει: θα κρατήσει την ελληνική λέξη και θα την εξηγήσει, ή θα αναζητήσει μια περίφραση που να λειτουργεί μέσα στη συγκεκριμένη πρόταση;", "It is and it isn't. Every language has words with no exact one-word equivalent in another language. That doesn't mean their meaning can't be conveyed. The translator simply has to choose: keep the Greek word and explain it, or look for a paraphrase that works within that particular sentence?"),
  L("Δημοσιογράφος", "m", "Εσείς τι προτιμάτε;", "What do you prefer?"),
  L("Μεταφράστρια", "f", "Εξαρτάται από το κείμενο. Σε ένα μυθιστόρημα, οι υποσημειώσεις κουράζουν τον αναγνώστη και σπάνε τον ρυθμό. Αν ένας ήρωας λέει ότι κάποιος «δεν έχει φιλότιμο», θα αναρωτηθώ τι ακριβώς τον πληγώνει σε εκείνη τη σκηνή: η αχαριστία; η έλλειψη ντροπής; η αδιαφορία για την οικογένεια; Η ίδια λέξη μπορεί να γίνει τρεις διαφορετικές εκφράσεις σε τρία διαφορετικά σημεία του βιβλίου.", "It depends on the text. In a novel, footnotes tire the reader and break the rhythm. If a character says someone 'has no filotimo', I'll ask myself what exactly hurts him in that scene: ingratitude? lack of shame? indifference towards family? The same word may become three different expressions in three different places in the book."),
  L("Δημοσιογράφος", "m", "Δηλαδή, το δύσκολο δεν είναι οι «αμετάφραστες» λέξεις;", "So the difficult part isn't the 'untranslatable' words?"),
  L("Μεταφράστρια", "f", "Καθόλου. Το πραγματικά δύσκολο είναι το χιούμορ, η ειρωνεία, οι διάλεκτοι και ο ρυθμός της προφορικής γλώσσας. Ένα αστείο που στηρίζεται σε ένα λογοπαίγνιο ή σε ένα τοπικό ιδίωμα μπορεί να μου πάρει μέρες. Εκεί η μετάφραση γίνεται πραγματικά ξαναγράψιμο.", "Not at all. What is really difficult is humour, irony, dialects and the rhythm of spoken language. A joke that rests on a pun or a local idiom can take me days. That's where translation really becomes rewriting."),
 ],
 "questions": [
  Q("Τι πιστεύει η μεταφράστρια για τις «αμετάφραστες» λέξεις;", ["Ότι το νόημά τους δεν αποδίδεται ποτέ", "Ότι δεν έχουν αντίστοιχο σε μία λέξη, αλλά το νόημά τους μπορεί να αποδοθεί", "Ότι υπάρχουν μόνο στα ελληνικά", "Ότι πρέπει πάντα να μένουν αμετάφραστες"], 1, "Αυτό δεν σημαίνει ότι το νόημά τους δεν μπορεί να αποδοθεί."),
  Q("Γιατί αποφεύγει τις υποσημειώσεις στα μυθιστορήματα;", ["Γιατί δεν τις επιτρέπει ο εκδότης", "Γιατί κουράζουν τον αναγνώστη και διακόπτουν τον ρυθμό", "Γιατί κοστίζουν ακριβά", "Γιατί οι αναγνώστες ξέρουν ήδη τις λέξεις"], 1, "οι υποσημειώσεις κουράζουν τον αναγνώστη και σπάνε τον ρυθμό"),
  Q("Πώς χειρίζεται τη λέξη «φιλότιμο» σε ένα μυθιστόρημα;", ["Την αφήνει πάντα στα ελληνικά", "Τη μεταφράζει πάντα με την ίδια αγγλική λέξη", "Την αποδίδει διαφορετικά ανάλογα με το τι σημαίνει σε κάθε σκηνή", "Την παραλείπει"], 2, "Η ίδια λέξη μπορεί να γίνει τρεις διαφορετικές εκφράσεις σε τρία διαφορετικά σημεία του βιβλίου."),
  Q("Τι θεωρεί πραγματικά δύσκολο στη μετάφραση;", ["Τους τεχνικούς όρους", "Τα ονόματα", "Το χιούμορ, την ειρωνεία, τις διαλέκτους και τον ρυθμό του προφορικού λόγου", "Τη γραμματική"], 2, "Το πραγματικά δύσκολο είναι το χιούμορ, η ειρωνεία, οι διάλεκτοι και ο ρυθμός της προφορικής γλώσσας."),
 ],
 "gloss": {"μεταφράστρια": "μεταφράστρια — translator (f)", "φιλότιμο": "φιλότιμο — sense of honour and duty, decency", "μεράκι": "μεράκι — love and care put into one's work", "αντίστοιχο": "αντίστοιχος — corresponding, equivalent", "να αποδοθεί": "αποδίδομαι — to be rendered, conveyed", "περίφραση": "περίφραση — paraphrase", "υποσημειώσεις": "υποσημείωση — footnote", "θα αναρωτηθώ": "αναρωτιέμαι — to wonder, ask oneself", "πληγώνει": "πληγώνω — to hurt", "αχαριστία": "αχαριστία — ingratitude", "αδιαφορία": "αδιαφορία — indifference", "ειρωνεία": "ειρωνεία — irony", "λογοπαίγνιο": "λογοπαίγνιο — pun", "ιδίωμα": "ιδίωμα — idiom, local dialect"},
})
rnd = random.Random(9)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-9.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
