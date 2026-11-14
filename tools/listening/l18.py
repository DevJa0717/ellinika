# Source for library/listening/listening-18.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l18.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l18-ann-nosokomeio", "title": "Αλλαγές στα εξωτερικά ιατρεία", "title_en": "Changes at the outpatient clinics", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ηχογραφημένη ανακοίνωση στο τηλεφωνικό κέντρο ενός νοσοκομείου.",
 "script": [
  L("Εκφωνήτρια", "f", "Καλέσατε το Γενικό Νοσοκομείο. Σας ενημερώνουμε ότι από τη Δευτέρα τα ραντεβού για τα εξωτερικά ιατρεία κλείνονται μόνο ηλεκτρονικά ή στον αριθμό ένα τέσσερα πέντε τρία τρία, και όχι πια στο ταμείο του νοσοκομείου.", "You have called the General Hospital. We inform you that from Monday, appointments for the outpatient clinics can only be booked online or on 14533, and no longer at the hospital cashier's desk."),
  L("Εκφωνήτρια", "f", "Το καρδιολογικό ιατρείο μεταφέρεται προσωρινά στο ισόγειο του νέου κτιρίου, λόγω εργασιών ανακαίνισης. Οι ασθενείς που έχουν ήδη ραντεβού δεν χρειάζεται να κάνουν τίποτα· θα εξεταστούν κανονικά στη νέα θέση.", "The cardiology clinic is moving temporarily to the ground floor of the new building, due to renovation work. Patients who already have an appointment don't need to do anything; they will be examined as normal in the new location."),
  L("Εκφωνήτρια", "f", "Παρακαλούμε να προσέρχεστε δεκαπέντε λεπτά νωρίτερα, με την αστυνομική σας ταυτότητα και το παραπεμπτικό του γιατρού σας. Για επείγοντα περιστατικά, απευθυνθείτε απευθείας στο τμήμα επειγόντων.", "Please arrive fifteen minutes early, with your identity card and your doctor's referral. For emergencies, go directly to the emergency department."),
 ],
 "questions": [
  Q("Πώς κλείνονται τα ραντεβού από τη Δευτέρα;", ["Μόνο στο ταμείο", "Μόνο ηλεκτρονικά ή τηλεφωνικά", "Μόνο μέσω του οικογενειακού γιατρού", "Χωρίς ραντεβού"], 1, "κλείνονται μόνο ηλεκτρονικά ή στον αριθμό"),
  Q("Τι πρέπει να κάνουν όσοι έχουν ήδη ραντεβού στο καρδιολογικό;", ["Να κλείσουν νέο ραντεβού", "Τίποτα, θα εξεταστούν στη νέα θέση", "Να πάνε σε άλλο νοσοκομείο", "Να τηλεφωνήσουν για επιβεβαίωση"], 1, "δεν χρειάζεται να κάνουν τίποτα"),
  Q("Τι πρέπει να φέρουν οι ασθενείς;", ["Τις παλιές εξετάσεις τους", "Την ταυτότητα και το παραπεμπτικό", "Χρήματα σε μετρητά", "Το βιβλιάριο εμβολίων"], 1, "με την αστυνομική σας ταυτότητα και το παραπεμπτικό του γιατρού σας"),
 ],
 "gloss": {"τηλεφωνικό κέντρο": "τηλεφωνικό κέντρο — switchboard, call centre", "εξωτερικά ιατρεία": "εξωτερικά ιατρεία — outpatient clinics", "κλείνονται": "κλείνομαι — to be booked", "καρδιολογικό ιατρείο": "καρδιολογικό ιατρείο — cardiology clinic", "μεταφέρεται": "μεταφέρομαι — to be moved", "ισόγειο": "ισόγειο — ground floor", "θα εξεταστούν": "εξετάζομαι — to be examined", "να προσέρχεστε": "προσέρχομαι — to arrive, attend", "παραπεμπτικό": "παραπεμπτικό — (doctor's) referral", "επείγοντα περιστατικά": "επείγον περιστατικό — emergency case", "τμήμα επειγόντων": "τμήμα επειγόντων — emergency department"},
})

ITEMS.append({
 "id": "l18-vm-anelkystiras", "title": "Ο ανελκυστήρας της πολυκατοικίας", "title_en": "The building's lift", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα από τη διαχειρίστρια μιας πολυκατοικίας προς έναν ένοικο.",
 "script": [
  L("Διαχειρίστρια", "f", "Γεια σας, κύριε Ανδρέου, η Βούλα είμαι, η διαχειρίστρια. Σας τηλεφωνώ για τον ανελκυστήρα. Ο τεχνικός ήρθε σήμερα και είπε ότι το μοτέρ είναι πολύ παλιό και πρέπει να αλλαχτεί, αλλιώς δεν θα περάσει τον ετήσιο έλεγχο ασφαλείας.", "Hello, Mr Andreou, it's Voula, the building manager. I'm calling about the lift. The technician came today and said the motor is very old and must be replaced, otherwise it won't pass the annual safety inspection."),
  L("Διαχειρίστρια", "f", "Η δαπάνη είναι περίπου τέσσερις χιλιάδες ευρώ, και θα μοιραστεί στα διαμερίσματα ανάλογα με τα χιλιοστά. Για εσάς, στον τέταρτο όροφο, βγαίνει γύρω στα τριακόσια πενήντα ευρώ. Αν θέλετε, μπορείτε να το πληρώσετε σε τρεις δόσεις.", "The cost is about four thousand euros, and it will be split among the flats according to their shares. For you, on the fourth floor, it comes to around three hundred and fifty euros. If you like, you can pay in three instalments."),
  L("Διαχειρίστρια", "f", "Θα κάνουμε γενική συνέλευση την Τετάρτη στις οχτώ το βράδυ, στην είσοδο, για να το εγκρίνουμε. Αν δεν μπορείτε να έρθετε, μπορείτε να δώσετε εξουσιοδότηση σε κάποιον γείτονα. Καλό βράδυ!", "We'll hold a general meeting on Wednesday at eight in the evening, in the entrance hall, to approve it. If you can't come, you can authorise a neighbour to vote for you. Good evening!"),
 ],
 "questions": [
  Q("Γιατί πρέπει να αλλαχτεί το μοτέρ;", ["Γιατί κάνει θόρυβο", "Γιατί είναι παλιό και δεν θα περάσει τον έλεγχο ασφαλείας", "Γιατί χάλασε χθες", "Γιατί το ζήτησαν οι ένοικοι"], 1, "δεν θα περάσει τον ετήσιο έλεγχο ασφαλείας"),
  Q("Πώς θα μοιραστεί η δαπάνη;", ["Εξίσου σε όλους", "Ανάλογα με τα χιλιοστά κάθε διαμερίσματος", "Μόνο στους πάνω ορόφους", "Θα την πληρώσει ο ιδιοκτήτης"], 1, "θα μοιραστεί στα διαμερίσματα ανάλογα με τα χιλιοστά"),
  Q("Τι μπορεί να κάνει ο κύριος Ανδρέου αν δεν έρθει στη συνέλευση;", ["Να στείλει email", "Να δώσει εξουσιοδότηση σε έναν γείτονα", "Να ψηφίσει τηλεφωνικά", "Τίποτα"], 1, "μπορείτε να δώσετε εξουσιοδότηση σε κάποιον γείτονα"),
 ],
 "gloss": {"διαχειρίστρια": "διαχειρίστρια — (female) building manager", "ένοικο": "ένοικος — tenant, resident", "ανελκυστήρα": "ανελκυστήρας — lift, elevator", "μοτέρ": "μοτέρ — motor", "να αλλαχτεί": "αλλάζομαι — to be replaced", "ετήσιο έλεγχο ασφαλείας": "ετήσιος έλεγχος ασφαλείας — annual safety inspection", "δαπάνη": "δαπάνη — cost, expense", "χιλιοστά": "χιλιοστά — shares (each flat's portion of building costs)", "δόσεις": "δόση — instalment", "γενική συνέλευση": "γενική συνέλευση — general meeting", "εξουσιοδότηση": "εξουσιοδότηση — authorisation, proxy"},
})

ITEMS.append({
 "id": "l18-dia-kreopoleio", "title": "Στον χασάπη", "title_en": "At the butcher's", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα κρεοπωλείο λίγες μέρες πριν από το Πάσχα.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα, κυρ Θανάση. Θέλω να παραγγείλω αρνί για το Πάσχα. Θα είμαστε δεκαπέντε άτομα και θα το ψήσουμε στη σούβλα, στο χωριό.", "Good morning, Mr Thanasis. I'd like to order lamb for Easter. We'll be fifteen people and we'll roast it on the spit, in the village."),
  L("Χασάπης", "m", "Για δεκαπέντε άτομα, με τα συνοδευτικά, ένα αρνί δεκατεσσάρων με δεκαπέντε κιλά φτάνει. Είναι ντόπιο, από βοσκό της περιοχής. Θέλετε να σας κρατήσω και τα εντόσθια για τη μαγειρίτσα;", "For fifteen people, with side dishes, a lamb of fourteen to fifteen kilos is enough. It's local, from a shepherd in the area. Do you want me to keep the offal for you for the magiritsa?"),
  L("Πελάτισσα", "f", "Ναι, βέβαια, τη μαγειρίτσα τη φτιάχνει η πεθερά μου το Μεγάλο Σάββατο. Και θα ήθελα κι ένα κοκορέτσι έτοιμο, αν γίνεται.", "Yes, of course, my mother-in-law makes the magiritsa on Holy Saturday. And I'd also like a ready kokoretsi, if possible."),
  L("Χασάπης", "m", "Γίνεται. Περάστε να τα πάρετε τη Μεγάλη Πέμπτη μετά τις πέντε, γιατί το Σάββατο θα έχει πολύ κόσμο. Θα χρειαστώ μια προκαταβολή πενήντα ευρώ για να κλείσει η παραγγελία.", "That's fine. Come and pick them up on Holy Thursday after five, because on Saturday it'll be very busy. I'll need a fifty-euro deposit to confirm the order."),
 ],
 "questions": [
  Q("Πώς θα μαγειρέψει η οικογένεια το αρνί;", ["Στον φούρνο", "Στη σούβλα", "Στη σχάρα", "Στην κατσαρόλα"], 1, "θα το ψήσουμε στη σούβλα"),
  Q("Ποιος φτιάχνει τη μαγειρίτσα;", ["Ο χασάπης", "Η πελάτισσα", "Η πεθερά της πελάτισσας", "Η μητέρα της"], 2, "τη μαγειρίτσα τη φτιάχνει η πεθερά μου"),
  Q("Γιατί προτείνει ο χασάπης να περάσει την Πέμπτη;", ["Γιατί το Σάββατο θα είναι κλειστά", "Γιατί το Σάββατο θα έχει πολύ κόσμο", "Γιατί το αρνί θα είναι πιο φρέσκο", "Γιατί η Πέμπτη είναι φθηνότερη"], 1, "γιατί το Σάββατο θα έχει πολύ κόσμο"),
 ],
 "gloss": {"κρεοπωλείο": "κρεοπωλείο — butcher's shop", "να παραγγείλω": "παραγγέλνω — to order", "σούβλα": "σούβλα — spit", "συνοδευτικά": "συνοδευτικό — side dish", "ντόπιο": "ντόπιος — local", "εντόσθια": "εντόσθια — offal", "μαγειρίτσα": "μαγειρίτσα — magiritsa (Easter soup)", "πεθερά": "πεθερά — mother-in-law", "Μεγάλο Σάββατο": "Μεγάλο Σάββατο — Holy Saturday", "κοκορέτσι": "κοκορέτσι — kokoretsi (spit-roasted offal)", "Μεγάλη Πέμπτη": "Μεγάλη Πέμπτη — Holy Thursday", "παραγγελία": "παραγγελία — order"},
})

ITEMS.append({
 "id": "l18-dia-ergasia", "title": "Συνέντευξη για πρακτική άσκηση", "title_en": "An internship interview", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη για πρακτική άσκηση σε ένα γραφείο αρχιτεκτόνων.",
 "script": [
  L("Αρχιτέκτονας", "f", "Λοιπόν, Μάρκο, είδα το πορτφόλιό σου και μου άρεσαν πολύ οι μακέτες σου. Γιατί θέλεις να κάνεις την πρακτική σου σε ένα μικρό γραφείο σαν το δικό μας;", "So, Markos, I saw your portfolio and I really liked your models. Why do you want to do your internship at a small office like ours?"),
  L("Μάρκος", "m", "Γιατί σε ένα μεγάλο γραφείο ο ασκούμενος συνήθως κάνει μόνο σχέδια στον υπολογιστή. Εδώ πιστεύω ότι θα μπορώ να δω ένα έργο από την αρχή ως το τέλος, να πηγαίνω στα εργοτάξια και να μάθω πώς μιλάμε με τους πελάτες.", "Because in a big office the intern usually only does drawings on the computer. Here I believe I'll be able to see a project from start to finish, go to building sites and learn how we talk to clients."),
  L("Αρχιτέκτονας", "f", "Σωστά. Να ξέρεις όμως ότι ασχολούμαστε κυρίως με αναπαλαιώσεις παλιών σπιτιών, που έχουν πολλές απρόβλεπτες δυσκολίες. Η πρακτική διαρκεί έξι μήνες, πέντε μέρες την εβδομάδα, με αμοιβή που καλύπτει το πρόγραμμα του πανεπιστημίου.", "Right. But you should know that we mainly work on restorations of old houses, which have many unexpected difficulties. The internship lasts six months, five days a week, with pay covered by the university's programme."),
  L("Μάρκος", "m", "Αυτό ακριβώς με ενδιαφέρει. Η διπλωματική μου εργασία είναι για τα παραδοσιακά σπίτια του Πηλίου, οπότε θα ήταν μεγάλη ευκαιρία για μένα.", "That's exactly what interests me. My thesis is on the traditional houses of Pelion, so it would be a great opportunity for me."),
 ],
 "questions": [
  Q("Γιατί προτιμά ο Μάρκος ένα μικρό γραφείο;", ["Γιατί πληρώνει καλύτερα", "Γιατί θα μπορεί να δει ένα έργο από την αρχή ως το τέλος", "Γιατί είναι κοντά στο σπίτι του", "Γιατί δεν δουλεύει με υπολογιστές"], 1, "θα μπορώ να δω ένα έργο από την αρχή ως το τέλος"),
  Q("Με τι ασχολείται κυρίως το γραφείο;", ["Με νέες πολυκατοικίες", "Με αναπαλαιώσεις παλιών σπιτιών", "Με εσωτερική διακόσμηση", "Με δημόσια κτίρια"], 1, "ασχολούμαστε κυρίως με αναπαλαιώσεις παλιών σπιτιών"),
  Q("Για ποιο θέμα είναι η διπλωματική του Μάρκου;", ["Για τα παραδοσιακά σπίτια του Πηλίου", "Για τις μακέτες", "Για τα εργοτάξια", "Για τους ουρανοξύστες"], 0, "Η διπλωματική μου εργασία είναι για τα παραδοσιακά σπίτια του Πηλίου"),
 ],
 "gloss": {"πρακτική άσκηση": "πρακτική άσκηση — internship, work placement", "πορτφόλιό": "πορτφόλιο — portfolio", "μακέτες": "μακέτα — (architectural) model", "ασκούμενος": "ασκούμενος — intern, trainee", "εργοτάξια": "εργοτάξιο — building site", "αναπαλαιώσεις": "αναπαλαίωση — restoration (of old buildings)", "απρόβλεπτες": "απρόβλεπτος — unexpected", "διαρκεί": "διαρκώ — to last", "αμοιβή": "αμοιβή — pay, fee", "διπλωματική μου εργασία": "διπλωματική εργασία — (degree) thesis"},
})

ITEMS.append({
 "id": "l18-mon-kolymvisi", "title": "Κολύμπι τον χειμώνα", "title_en": "Winter swimming", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν άντρα να μιλάει για τη συνήθειά του να κολυμπά στη θάλασσα όλο τον χρόνο.",
 "script": [
  L("Παύλος", "m", "Κολυμπώ στη θάλασσα κάθε πρωί, χειμώνα καλοκαίρι, εδώ και δεκαπέντε χρόνια. Οι φίλοι μου νομίζουν ότι είμαι τρελός, αλλά στην παραλία της γειτονιάς μας είμαστε μια ολόκληρη παρέα, οι λεγόμενοι «χειμερινοί κολυμβητές».", "I swim in the sea every morning, winter and summer, and have done for fifteen years. My friends think I'm mad, but at our local beach we're a whole group, the so-called 'winter swimmers'."),
  L("Παύλος", "m", "Τον Ιανουάριο το νερό πέφτει στους δεκατέσσερις βαθμούς. Τα πρώτα δευτερόλεπτα είναι σοκ, η ανάσα σου κόβεται. Γι' αυτό μπαίνουμε σιγά σιγά, δεν βουτάμε απότομα, και δεν μένουμε μέσα περισσότερο από δέκα λεπτά. Και ποτέ μόνοι.", "In January the water drops to fourteen degrees. The first seconds are a shock, your breath catches. That's why we go in slowly, we don't dive in abruptly, and we don't stay in for more than ten minutes. And never alone."),
  L("Παύλος", "m", "Όταν βγαίνεις, νιώθεις μια ενέργεια που δεν περιγράφεται. Από τότε που ξεκίνησα, σχεδόν δεν αρρωσταίνω, αν και ο γιατρός μου λέει ότι αυτό δεν έχει αποδειχθεί επιστημονικά. Το σίγουρο είναι ότι μετά από ένα τέτοιο πρωινό, κανένα πρόβλημα της δουλειάς δεν μου φαίνεται μεγάλο.", "When you come out, you feel an energy that can't be described. Since I started, I hardly ever get ill, although my doctor says this hasn't been scientifically proven. What's certain is that after a morning like that, no problem at work seems big to me."),
 ],
 "questions": [
  Q("Ποιοι είναι οι «χειμερινοί κολυμβητές»;", ["Επαγγελματίες αθλητές", "Μια παρέα που κολυμπά στη θάλασσα όλο τον χρόνο", "Ναυαγοσώστες", "Μια ομάδα που κολυμπά σε πισίνα"], 1, "είμαστε μια ολόκληρη παρέα, οι λεγόμενοι «χειμερινοί κολυμβητές»"),
  Q("Ποιον κανόνα ακολουθούν;", ["Βουτούν απότομα", "Μένουν μέσα μία ώρα", "Δεν κολυμπούν ποτέ μόνοι", "Κολυμπούν μόνο το καλοκαίρι"], 2, "Και ποτέ μόνοι"),
  Q("Τι λέει ο γιατρός του Παύλου;", ["Ότι πρέπει να σταματήσει", "Ότι το όφελος για την υγεία δεν έχει αποδειχθεί επιστημονικά", "Ότι κολυμπά πολύ λίγο", "Ότι είναι τρελός"], 1, "αυτό δεν έχει αποδειχθεί επιστημονικά"),
 ],
 "gloss": {"χειμερινοί κολυμβητές": "χειμερινός κολυμβητής — winter swimmer", "δευτερόλεπτα": "δευτερόλεπτο — second", "η ανάσα σου κόβεται": "μου κόβεται η ανάσα — to lose one's breath", "βουτάμε": "βουτάω — to dive, plunge", "απότομα": "απότομα — abruptly", "δεν περιγράφεται": "δεν περιγράφεται — is indescribable", "αρρωσταίνω": "αρρωσταίνω — to fall ill", "έχει αποδειχθεί": "αποδεικνύομαι — to be proven"},
})

ITEMS.append({
 "id": "l18-rep-vikos", "title": "Το φαράγγι του Βίκου", "title_en": "The Vikos Gorge", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ταξιδιωτικό ρεπορτάζ από το Ζαγόρι, στην Ήπειρο.",
 "script": [
  L("Δημοσιογράφος", "f", "Βρισκόμαστε στο Ζαγόρι, μια περιοχή με σαράντα έξι πέτρινα χωριά στις πλαγιές της Πίνδου. Το 2023 το πολιτιστικό τοπίο του Ζαγορίου ανακηρύχθηκε μνημείο παγκόσμιας κληρονομιάς της UNESCO.", "We are in Zagori, an area with forty-six stone villages on the slopes of the Pindus. In 2023 the cultural landscape of Zagori was declared a UNESCO World Heritage Site."),
  L("Δημοσιογράφος", "f", "Το πιο γνωστό του αξιοθέατο είναι το φαράγγι του Βίκου, με απόκρημνα τοιχώματα που σε ορισμένα σημεία ξεπερνούν τα εννιακόσια μέτρα. Η διάσχισή του, από το Μονοδένδρι ως το Βίκο, διαρκεί περίπου έξι ώρες και απαιτεί καλή φυσική κατάσταση.", "Its best-known attraction is the Vikos Gorge, with sheer walls that in places exceed nine hundred metres. Crossing it, from Monodendri to Vikos, takes about six hours and requires good fitness."),
  L("Δημοσιογράφος", "f", "Τα χωριά συνδέονται με λιθόστρωτα μονοπάτια και τοξωτά πέτρινα γεφύρια, που χτίστηκαν κυρίως τον δέκατο όγδοο και τον δέκατο ένατο αιώνα με χρήματα ντόπιων εμπόρων. Οι κάτοικοι λένε ότι ο καλύτερος τρόπος για να γνωρίσεις το Ζαγόρι είναι με τα πόδια.", "The villages are linked by cobbled paths and arched stone bridges, built mainly in the eighteenth and nineteenth centuries with money from local merchants. Residents say the best way to get to know Zagori is on foot."),
 ],
 "questions": [
  Q("Τι έγινε το 2023;", ["Άνοιξε νέος δρόμος", "Το Ζαγόρι ανακηρύχθηκε μνημείο παγκόσμιας κληρονομιάς", "Χτίστηκε νέο γεφύρι", "Έκλεισε το φαράγγι"], 1, "ανακηρύχθηκε μνημείο παγκόσμιας κληρονομιάς της UNESCO"),
  Q("Πόσο διαρκεί η διάσχιση του φαραγγιού;", ["Μία ώρα", "Περίπου έξι ώρες", "Δύο μέρες", "Μισή μέρα με αυτοκίνητο"], 1, "διαρκεί περίπου έξι ώρες"),
  Q("Με τι χρήματα χτίστηκαν τα πέτρινα γεφύρια;", ["Με χρήματα του κράτους", "Με χρήματα ντόπιων εμπόρων", "Με ευρωπαϊκά προγράμματα", "Με χρήματα της εκκλησίας"], 1, "με χρήματα ντόπιων εμπόρων"),
 ],
 "gloss": {"πέτρινα": "πέτρινος — (made of) stone", "πλαγιές": "πλαγιά — slope", "πολιτιστικό τοπίο": "πολιτιστικό τοπίο — cultural landscape", "ανακηρύχθηκε": "ανακηρύσσομαι — to be declared", "αξιοθέατο": "αξιοθέατο — sight, attraction", "απόκρημνα": "απόκρημνος — sheer, precipitous", "τοιχώματα": "τοίχωμα — wall (of a gorge)", "διάσχισή": "διάσχιση — crossing", "λιθόστρωτα": "λιθόστρωτος — cobbled", "τοξωτά": "τοξωτός — arched", "γεφύρια": "γεφύρι — (stone) bridge", "εμπόρων": "έμπορος — merchant"},
})

ITEMS.append({
 "id": "l18-rep-trena", "title": "Το τρενάκι του Πηλίου", "title_en": "The little train of Pelion", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για ένα ιστορικό τρένο στο Πήλιο.",
 "script": [
  L("Δημοσιογράφος", "m", "Κάθε Σαββατοκύριακο, από την άνοιξη ως το φθινόπωρο, ένα μικρό ατμοκίνητο τρένο ξεκινά από τις Άνω Λεχώνιες και ανεβαίνει αργά ως τις Μηλιές, μέσα από ελαιώνες και πυκνά δάση από πλατάνια.", "Every weekend, from spring to autumn, a small steam train sets off from Ano Lechonia and climbs slowly to Milies, through olive groves and dense plane-tree forests."),
  L("Δημοσιογράφος", "m", "Η γραμμή έχει πλάτος μόλις εξήντα εκατοστά και κατασκευάστηκε στις αρχές του εικοστού αιώνα. Στη διαδρομή το τρένο περνά πάνω από μια περίφημη πέτρινη γέφυρα, που σχεδίασε, σύμφωνα με την παράδοση, ο Ιταλός μηχανικός Εβαρίστο ντε Κίρικο, πατέρας του ζωγράφου Τζόρτζιο ντε Κίρικο.", "The track is only sixty centimetres wide and was built at the beginning of the twentieth century. Along the way the train crosses a famous stone bridge designed, according to tradition, by the Italian engineer Evaristo de Chirico, father of the painter Giorgio de Chirico."),
  L("Δημοσιογράφος", "m", "Η διαδρομή κρατά περίπου μιάμιση ώρα, με μια στάση στο χωριό Άνω Γατζέα για νερό. Τα εισιτήρια εξαντλούνται συχνά, γι' αυτό καλό είναι να κλείνετε θέση από πριν, ιδίως τον Αύγουστο.", "The journey takes about an hour and a half, with a stop at the village of Ano Gatzea for water. Tickets often sell out, so it's a good idea to book a seat in advance, especially in August."),
 ],
 "questions": [
  Q("Πότε λειτουργεί το τρενάκι;", ["Κάθε μέρα όλο τον χρόνο", "Τα Σαββατοκύριακα από την άνοιξη ως το φθινόπωρο", "Μόνο τον χειμώνα", "Μόνο τον Αύγουστο"], 1, "Κάθε Σαββατοκύριακο, από την άνοιξη ως το φθινόπωρο"),
  Q("Ποιος σχεδίασε, σύμφωνα με την παράδοση, την πέτρινη γέφυρα;", ["Ο ζωγράφος Τζόρτζιο ντε Κίρικο", "Ο πατέρας του, Εβαρίστο ντε Κίρικο", "Ένας ντόπιος μάστορας", "Ένας Γάλλος αρχιτέκτονας"], 1, "ο Ιταλός μηχανικός Εβαρίστο ντε Κίρικο, πατέρας του ζωγράφου"),
  Q("Τι συμβουλεύει ο δημοσιογράφος;", ["Να πάτε μόνο τον Αύγουστο", "Να κλείνετε θέση από πριν", "Να αγοράσετε εισιτήριο στο τρένο", "Να πάτε με αυτοκίνητο"], 1, "καλό είναι να κλείνετε θέση από πριν"),
 ],
 "gloss": {"ατμοκίνητο": "ατμοκίνητος — steam-powered", "ελαιώνες": "ελαιώνας — olive grove", "πυκνά": "πυκνός — dense", "πλατάνια": "πλάτανος — plane tree", "γραμμή": "γραμμή — (railway) track, line", "πλάτος": "πλάτος — width", "κατασκευάστηκε": "κατασκευάζομαι — to be built", "περίφημη": "περίφημος — famous", "εξαντλούνται": "εξαντλούμαι — to sell out, run out"},
})

ITEMS.append({
 "id": "l18-int-gelioto", "title": "Η γελωτοποιός του νοσοκομείου", "title_en": "The hospital clown", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια γυναίκα που επισκέπτεται παιδιά στο νοσοκομείο ως κλόουν. Η ίδια αυτοαποκαλείται «γελωτοποιός».",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Λιάπη, τι κάνει ένας κλόουν σε ένα παιδιατρικό νοσοκομείο;", "Ms Liapi, what does a clown do in a children's hospital?"),
  L("Κλόουν", "f", "Πάνω απ' όλα, δίνει στο παιδί την αίσθηση ότι έχει ξανά τον έλεγχο. Στο νοσοκομείο όλοι του λένε τι να κάνει: να πάρει το φάρμακο, να ξαπλώσει, να μην κουνηθεί. Εμείς ρωτάμε: «Θέλεις να μπω;» Αν πει όχι, φεύγουμε. Αυτό από μόνο του είναι θεραπευτικό.", "Above all, it gives the child the feeling of being in control again. In hospital everyone tells them what to do: take the medicine, lie down, don't move. We ask: 'Do you want me to come in?' If they say no, we leave. That in itself is therapeutic."),
  L("Δημοσιογράφος", "m", "Χρειάζεται ειδική εκπαίδευση;", "Is special training needed?"),
  L("Κλόουν", "f", "Βέβαια. Δεν αρκεί να είσαι αστείος. Μαθαίνουμε αυτοσχεδιασμό, αλλά και κανόνες υγιεινής, και συνεργαζόμαστε στενά με τις νοσηλεύτριες, που μας λένε ποιο παιδί έχει μια δύσκολη μέρα. Μερικές φορές το πιο σημαντικό που κάνουμε δεν είναι να κάνουμε το παιδί να γελάσει, αλλά να κάνουμε τους γονείς να χαμογελάσουν για λίγα λεπτά.", "Of course. It's not enough to be funny. We learn improvisation, but also hygiene rules, and we work closely with the nurses, who tell us which child is having a hard day. Sometimes the most important thing we do isn't making the child laugh, but making the parents smile for a few minutes."),
 ],
 "questions": [
  Q("Τι δίνει ο κλόουν στο παιδί, πάνω απ' όλα;", ["Δώρα", "Την αίσθηση ότι έχει ξανά τον έλεγχο", "Φάρμακα", "Πληροφορίες για την αρρώστια του"], 1, "δίνει στο παιδί την αίσθηση ότι έχει ξανά τον έλεγχο"),
  Q("Τι κάνουν οι κλόουν αν το παιδί δεν θέλει να μπουν;", ["Μπαίνουν έτσι κι αλλιώς", "Φεύγουν", "Ρωτούν τους γονείς", "Περιμένουν έξω από την πόρτα"], 1, "Αν πει όχι, φεύγουμε"),
  Q("Με ποιους συνεργάζονται στενά;", ["Με τους γιατρούς μόνο", "Με τις νοσηλεύτριες", "Με τους δασκάλους", "Με άλλους ηθοποιούς"], 1, "συνεργαζόμαστε στενά με τις νοσηλεύτριες"),
 ],
 "gloss": {"γελωτοποιός": "γελωτοποιός — clown, jester", "παιδιατρικό νοσοκομείο": "παιδιατρικό νοσοκομείο — children's hospital", "αίσθηση": "αίσθηση — feeling, sense", "να μην κουνηθεί": "κουνιέμαι — to move", "θεραπευτικό": "θεραπευτικός — therapeutic", "εκπαίδευση": "εκπαίδευση — training", "αυτοσχεδιασμό": "αυτοσχεδιασμός — improvisation", "κανόνες υγιεινής": "κανόνες υγιεινής — hygiene rules", "νοσηλεύτριες": "νοσηλεύτρια — (female) nurse"},
})

ITEMS.append({
 "id": "l18-mon-dimokratia", "title": "Η κλήρωση στην αρχαία Αθήνα", "title_en": "Selection by lot in ancient Athens", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη για τον θεσμό της κλήρωσης στην αθηναϊκή δημοκρατία.",
 "script": [
  L("Ιστορικός", "m", "Όταν σκεφτόμαστε τη δημοκρατία, σκεφτόμαστε εκλογές. Οι αρχαίοι Αθηναίοι, όμως, θεωρούσαν τις εκλογές μάλλον αριστοκρατικό θεσμό, γιατί ευνοούν όσους είναι γνωστοί, πλούσιοι ή καλοί ρήτορες. Το κατεξοχήν δημοκρατικό εργαλείο ήταν η κλήρωση.", "When we think of democracy, we think of elections. The ancient Athenians, however, considered elections a rather aristocratic institution, because they favour those who are well known, wealthy or good speakers. The quintessentially democratic tool was selection by lot."),
  L("Ιστορικός", "m", "Με κλήρωση επιλέγονταν τα περισσότερα αξιώματα, τα μέλη της Βουλής των Πεντακοσίων και οι δικαστές των λαϊκών δικαστηρίων. Για τον σκοπό αυτό χρησιμοποιούσαν μια ειδική πέτρινη μηχανή, το κληρωτήριο, όπου τοποθετούσαν τα ονόματα των πολιτών και τα ανακάτευαν με λευκούς και μαύρους κύβους. Η θητεία ήταν συνήθως ετήσια, και τα περισσότερα αξιώματα δεν μπορούσε κανείς να τα κατέχει δεύτερη φορά.", "Most offices, the members of the Council of Five Hundred and the jurors of the popular courts were chosen by lot. For this purpose they used a special stone machine, the kleroterion, where they placed the citizens' names and mixed them with white and black cubes. Terms were usually annual, and most offices could not be held a second time."),
  L("Ιστορικός", "m", "Υπήρχαν, βέβαια, εξαιρέσεις: οι στρατηγοί, για παράδειγμα, εκλέγονταν, γιατί για τον πόλεμο χρειαζόταν ικανότητα και όχι τύχη. Και δεν πρέπει να ξεχνάμε ότι «πολίτες» ήταν μόνο οι ενήλικοι άντρες· οι γυναίκες, οι δούλοι και οι μέτοικοι ήταν αποκλεισμένοι. Παρ' όλα αυτά, η ιδέα ότι κάθε πολίτης είναι ικανός να κυβερνήσει επανέρχεται σήμερα, με τις λεγόμενες «συνελεύσεις πολιτών» που επιλέγονται με κλήρωση.", "There were, of course, exceptions: generals, for example, were elected, because war required ability and not luck. And we mustn't forget that 'citizens' were only adult men; women, slaves and resident foreigners were excluded. Nevertheless, the idea that every citizen is capable of governing is returning today, with the so-called 'citizens' assemblies' chosen by lot."),
 ],
 "questions": [
  Q("Γιατί οι Αθηναίοι θεωρούσαν τις εκλογές μάλλον αριστοκρατικό θεσμό;", ["Γιατί ήταν ακριβές", "Γιατί ευνοούν τους γνωστούς, τους πλούσιους και τους καλούς ρήτορες", "Γιατί τις είχαν εφεύρει οι Σπαρτιάτες", "Γιατί ψήφιζαν μόνο οι γυναίκες"], 1, "γιατί ευνοούν όσους είναι γνωστοί, πλούσιοι ή καλοί ρήτορες"),
  Q("Γιατί οι στρατηγοί εκλέγονταν και δεν κληρώνονταν;", ["Γιατί ήταν λίγοι", "Γιατί για τον πόλεμο χρειαζόταν ικανότητα και όχι τύχη", "Γιατί ήταν πλούσιοι", "Γιατί το ζητούσαν οι θεοί"], 1, "για τον πόλεμο χρειαζόταν ικανότητα και όχι τύχη"),
  Q("Πού επανέρχεται σήμερα η ιδέα της κλήρωσης;", ["Στις εθνικές εκλογές", "Στις συνελεύσεις πολιτών", "Στα δικαστήρια", "Στον στρατό"], 1, "με τις λεγόμενες «συνελεύσεις πολιτών» που επιλέγονται με κλήρωση"),
 ],
 "gloss": {"θεσμό": "θεσμός — institution", "κλήρωσης": "κλήρωση — selection by lot, draw", "αριστοκρατικό": "αριστοκρατικός — aristocratic", "ευνοούν": "ευνοώ — to favour", "ρήτορες": "ρήτορας — orator", "κατεξοχήν": "κατεξοχήν — par excellence", "αξιώματα": "αξίωμα — office, post", "Βουλής των Πεντακοσίων": "Βουλή των Πεντακοσίων — Council of Five Hundred", "λαϊκών δικαστηρίων": "λαϊκό δικαστήριο — popular court", "κληρωτήριο": "κληρωτήριο — kleroterion (allotment machine)", "θητεία": "θητεία — term of office", "να τα κατέχει": "κατέχω — to hold", "στρατηγοί": "στρατηγός — general", "μέτοικοι": "μέτοικος — resident foreigner (metic)", "αποκλεισμένοι": "αποκλεισμένος — excluded", "επανέρχεται": "επανέρχομαι — to return, come back"},
})

ITEMS.append({
 "id": "l18-int-ypnos-psifiaki", "title": "Η ψηφιακή αποτοξίνωση", "title_en": "Digital detox", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με έναν ψυχολόγο για τη σχέση μας με τα κινητά τηλέφωνα.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Καραλής, μιλάμε πολύ για «εθισμό» στο κινητό. Είναι σωστός ο όρος;", "Mr Karalis, we talk a lot about 'addiction' to the mobile phone. Is the term correct?"),
  L("Ψυχολόγος", "m", "Πρέπει να είμαστε προσεκτικοί. Οι περισσότεροι άνθρωποι δεν έχουν εθισμό με την κλινική έννοια· έχουν όμως μια συνήθεια που έχει σχεδιαστεί σκόπιμα για να είναι δύσκολο να την κόψουν. Οι ειδοποιήσεις, η ατελείωτη κύλιση, τα «μου αρέσει» λειτουργούν σαν μικρές ανταμοιβές που μας κάνουν να επιστρέφουμε ξανά και ξανά.", "We must be careful. Most people don't have an addiction in the clinical sense; they do, however, have a habit that has been deliberately designed to be hard to break. Notifications, endless scrolling, 'likes' work like small rewards that make us come back again and again."),
  L("Δημοσιογράφος", "f", "Τι συμβουλεύετε, λοιπόν; Να πετάξουμε τα κινητά;", "What do you advise, then? Should we throw our phones away?"),
  L("Ψυχολόγος", "m", "Όχι, αυτό δεν είναι ούτε ρεαλιστικό ούτε επιθυμητό. Προτείνω μικρές, συγκεκριμένες αλλαγές: να απενεργοποιήσουμε τις ειδοποιήσεις που δεν είναι απαραίτητες, να μην έχουμε το κινητό στο υπνοδωμάτιο, να ορίσουμε ώρες χωρίς οθόνη, για παράδειγμα στο οικογενειακό τραπέζι. Η λεγόμενη «ψηφιακή αποτοξίνωση» για ένα Σαββατοκύριακο είναι ευχάριστη, αλλά αν μετά επιστρέψουμε στις ίδιες συνήθειες, δεν αλλάζει τίποτα. Το ζητούμενο είναι η μόνιμη, ήπια αλλαγή.", "No, that's neither realistic nor desirable. I suggest small, specific changes: turning off notifications that aren't necessary, not keeping the phone in the bedroom, setting screen-free times, for example at the family table. A so-called 'digital detox' for a weekend is pleasant, but if afterwards we return to the same habits, nothing changes. What we're after is permanent, gentle change."),
 ],
 "questions": [
  Q("Τι λέει ο ψυχολόγος για τον όρο «εθισμός»;", ["Ότι ισχύει για όλους", "Ότι οι περισσότεροι έχουν μια συνήθεια σχεδιασμένη να είναι δύσκολο να κοπεί, όχι κλινικό εθισμό", "Ότι είναι ιατρικός όρος για τα παιδιά", "Ότι δεν υπάρχει πρόβλημα"], 1, "Οι περισσότεροι άνθρωποι δεν έχουν εθισμό με την κλινική έννοια"),
  Q("Με τι παρομοιάζει τις ειδοποιήσεις και τα «μου αρέσει»;", ["Με μικρές ανταμοιβές", "Με τιμωρίες", "Με φάρμακα", "Με παιχνίδια"], 0, "λειτουργούν σαν μικρές ανταμοιβές"),
  Q("Ποια είναι η άποψή του για την «ψηφιακή αποτοξίνωση» ενός Σαββατοκύριακου;", ["Ότι λύνει το πρόβλημα", "Ότι είναι ευχάριστη, αλλά δεν αλλάζει τίποτα αν επιστρέψουμε στις ίδιες συνήθειες", "Ότι είναι επικίνδυνη", "Ότι πρέπει να κρατά έναν μήνα"], 1, "αν μετά επιστρέψουμε στις ίδιες συνήθειες, δεν αλλάζει τίποτα"),
 ],
 "gloss": {"ψυχολόγο": "ψυχολόγος — psychologist", "εθισμό": "εθισμός — addiction", "όρος": "όρος — term", "κλινική έννοια": "κλινική έννοια — clinical sense", "σκόπιμα": "σκόπιμα — deliberately", "να την κόψουν": "κόβω (μια συνήθεια) — to break (a habit)", "ειδοποιήσεις": "ειδοποίηση — notification", "ατελείωτη κύλιση": "ατελείωτη κύλιση — endless scrolling", "ανταμοιβές": "ανταμοιβή — reward", "επιθυμητό": "επιθυμητός — desirable", "να απενεργοποιήσουμε": "απενεργοποιώ — to turn off, disable", "υπνοδωμάτιο": "υπνοδωμάτιο — bedroom", "ψηφιακή αποτοξίνωση": "ψηφιακή αποτοξίνωση — digital detox", "ήπια": "ήπιος — gentle, mild"},
})

rnd = random.Random(18)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-18.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
