# Source for library/listening/listening-226.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l226.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l226-news-foitites-se-xenodocheia", "title": "Φοιτητές σε ξενοδοχεία τον χειμώνα", "title_en": "Students in hotels over the winter", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο ραδιόφωνο για μια λύση στο πρόβλημα της στέγασης των φοιτητών.",
 "script": [
  L("Εκφωνήτρια", "f", "Σε μια πόλη με πανεπιστήμιο και πολλά ξενοδοχεία που μένουν κλειστά τον χειμώνα, ο δήμος βρήκε έναν τρόπο να συνδυάσει τα δύο προβλήματα. Από τον Οκτώβριο ως τον Μάιο, δεκαπέντε ξενοδοχεία θα νοικιάζουν δωμάτια σε φοιτητές σε χαμηλές τιμές.", "In a city with a university and many hotels that stay closed in winter, the municipality has found a way to combine the two problems. From October to May, fifteen hotels will rent rooms to students at low prices."),
  L("Εκφωνήτρια", "f", "Το ενοίκιο θα περιλαμβάνει ρεύμα, θέρμανση και ίντερνετ, ενώ σε κάποια ξενοδοχεία οι φοιτητές θα μπορούν να χρησιμοποιούν και την κουζίνα. Οι ιδιοκτήτες κερδίζουν ένα σταθερό εισόδημα τους μήνες που αλλιώς θα είχαν μόνο έξοδα.", "The rent will include electricity, heating and internet, while in some hotels students will also be able to use the kitchen. The owners gain a steady income in the months when they would otherwise have only expenses."),
  L("Εκφωνήτρια", "f", "Το μεγάλο μειονέκτημα είναι ότι τον Ιούνιο οι φοιτητές πρέπει να αδειάσουν τα δωμάτια για τους τουρίστες, ακριβώς την περίοδο των εξετάσεων. Ο φοιτητικός σύλλογος ζητά από το πανεπιστήμιο να προσφέρει θέσεις στις εστίες για αυτές τις λίγες εβδομάδες.", "The big drawback is that in June students must vacate the rooms for tourists, exactly during the exam period. The students' union is asking the university to offer places in the halls of residence for those few weeks."),
 ],
 "questions": [
  Q("Ποια δύο προβλήματα συνδυάζει η λύση του δήμου;", ["Την κίνηση και τη ρύπανση", "Τα κλειστά ξενοδοχεία τον χειμώνα και τη στέγαση των φοιτητών", "Την ανεργία και τον τουρισμό", "Τις εξετάσεις και τις διακοπές"], 1, "πολλά ξενοδοχεία που μένουν κλειστά τον χειμώνα ... νοικιάζουν δωμάτια σε φοιτητές"),
  Q("Τι περιλαμβάνει το ενοίκιο;", ["Μόνο το δωμάτιο", "Ρεύμα, θέρμανση και ίντερνετ", "Πρωινό και δείπνο", "Καθαριότητα κάθε μέρα"], 1, "Το ενοίκιο θα περιλαμβάνει ρεύμα, θέρμανση και ίντερνετ"),
  Q("Τι κερδίζουν οι ιδιοκτήτες;", ["Νέους πελάτες για το καλοκαίρι", "Μια επιδότηση από το κράτος", "Ένα σταθερό εισόδημα τους μήνες χωρίς τουρίστες", "Δωρεάν ανακαίνιση"], 2, "Οι ιδιοκτήτες κερδίζουν ένα σταθερό εισόδημα"),
  Q("Ποιο είναι το μεγάλο μειονέκτημα;", ["Τα δωμάτια είναι μακριά από το πανεπιστήμιο", "Οι φοιτητές πρέπει να φύγουν τον Ιούνιο, την περίοδο των εξετάσεων", "Δεν επιτρέπονται επισκέπτες", "Τα δωμάτια δεν έχουν θέρμανση"], 1, "τον Ιούνιο οι φοιτητές πρέπει να αδειάσουν τα δωμάτια ... ακριβώς την περίοδο των εξετάσεων"),
 ],
 "gloss": {"στέγασης": "στέγαση — housing", "συνδυάσει": "συνδυάζω — to combine", "ενοίκιο": "ενοίκιο — rent", "θέρμανση": "θέρμανση — heating", "εισόδημα": "εισόδημα — income", "μειονέκτημα": "μειονέκτημα — drawback, disadvantage", "αδειάσουν": "αδειάζω — to empty, vacate", "εστίες": "εστία — hall of residence; hearth"},
})
ITEMS.append({
 "id": "l226-vm-zacharoplasteio-tourta", "title": "Μήνυμα από το ζαχαροπλαστείο για την τούρτα", "title_en": "Message from the patisserie about the cake", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από το ζαχαροπλαστείο όπου παραγγείλατε μια τούρτα για την επέτειο γάμου των γονιών σας.",
 "script": [
  L("Ζαχαροπλάστης", "m", "Καλησπέρα, κυρία Νικολάου, από το ζαχαροπλαστείο «Η Γλυκιά Γωνιά» σας παίρνω, για την τούρτα που παραγγείλατε για τα σαράντα χρόνια γάμου των γονιών σας, την Κυριακή.", "Good afternoon, Ms Nikolaou, I'm calling from 'The Sweet Corner' patisserie about the cake you ordered for your parents' fortieth wedding anniversary on Sunday."),
  L("Ζαχαροπλάστης", "m", "Δυστυχώς, η εποχή των σύκων τελείωσε και δεν βρίσκουμε πια φρέσκα σύκα σε καλή ποιότητα. Σας προτείνω δύο λύσεις: είτε να τη φτιάξουμε με αχλάδια καραμελωμένα, που τα έχουμε από έναν παραγωγό της περιοχής, είτε με μαρμελάδα σύκου που φτιάξαμε εμείς το καλοκαίρι. Η γεύση και στις δύο περιπτώσεις είναι πολύ καλή.", "Unfortunately, the fig season is over and we can no longer find fresh figs of good quality. I suggest two solutions: either we make it with caramelised pears, which we get from a local producer, or with fig jam that we made ourselves in the summer. The taste is very good in both cases."),
  L("Ζαχαροπλάστης", "m", "Επίσης, μου είπατε ότι θα είστε πενήντα άτομα. Η διώροφη τούρτα που διαλέξατε βγάζει περίπου σαράντα κομμάτια, οπότε ίσως θα ήταν καλύτερα να προσθέσουμε και έναν δίσκο με μικρά γλυκά· κοστίζει τριάντα ευρώ. Και για την επιγραφή πάνω στην τούρτα, θέλουμε να ξέρουμε αν προτιμάτε «Καλή επέτειο» ή τα ονόματα των γονιών σας.", "Also, you told me there will be fifty of you. The two-tier cake you chose gives about forty slices, so it might be better to add a tray of small pastries as well; it costs thirty euros. And for the inscription on the cake, we'd like to know whether you prefer 'Happy anniversary' or your parents' names."),
  L("Ζαχαροπλάστης", "m", "Χρειαζόμαστε την απάντησή σας ως αύριο το μεσημέρι, για να προλάβουμε. Η παραλαβή μένει κανονικά την Κυριακή στις έντεκα. Ευχαριστούμε!", "We need your answer by tomorrow midday, so that we have time. Collection stays as planned on Sunday at eleven. Thank you!"),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με την τούρτα;", ["Ο φούρνος χάλασε", "Δεν βρίσκουν πια φρέσκα σύκα καλής ποιότητας", "Η παραγγελία χάθηκε", "Η σοκολάτα τελείωσε"], 1, "δεν βρίσκουμε πια φρέσκα σύκα σε καλή ποιότητα"),
  Q("Ποια λύση προτείνει ο ζαχαροπλάστης;", ["Να ακυρωθεί η παραγγελία", "Καραμελωμένα αχλάδια ή μαρμελάδα σύκου", "Μια τούρτα σοκολάτας", "Να αλλάξει η μέρα"], 1, "είτε να τη φτιάξουμε με αχλάδια καραμελωμένα ... είτε με μαρμελάδα σύκου"),
  Q("Γιατί προτείνει έναν δίσκο με μικρά γλυκά;", ["Γιατί είναι δώρο", "Γιατί η τούρτα δεν φτάνει για όλους τους καλεσμένους", "Γιατί η τούρτα θα αργήσει", "Γιατί οι γονείς δεν τρώνε τούρτα"], 1, "θα είστε πενήντα άτομα. Η διώροφη τούρτα ... βγάζει περίπου σαράντα κομμάτια"),
  Q("Τι θέλει να μάθει για την επιγραφή;", ["Αν θα γραφτεί με σοκολάτα", "Αν θα γράφει «Καλή επέτειο» ή τα ονόματα των γονιών", "Σε ποια γλώσσα θα γραφτεί", "Αν θα μπει και η ημερομηνία του γάμου"], 1, "αν προτιμάτε «Καλή επέτειο» ή τα ονόματα των γονιών σας"),
 ],
 "gloss": {"ζαχαροπλαστείο": "ζαχαροπλαστείο — patisserie, cake shop", "τούρτα": "τούρτα — (layer) cake, gateau", "παραγγείλατε": "παραγγέλνω — to order", "επέτειο": "επέτειος — anniversary", "καραμελωμένα": "καραμελωμένος — caramelised", "διώροφη": "διώροφος — two-storey; (cake) two-tier", "επιγραφή": "επιγραφή — inscription", "προλάβουμε": "προλαβαίνω — to have time, make it", "παραλαβή": "παραλαβή — collection, pick-up"},
})
ITEMS.append({
 "id": "l226-c1-mono-deiktes-rologiou", "title": "Γιατί οι δείκτες του ρολογιού γυρίζουν προς τα δεξιά", "title_en": "Why clock hands turn to the right", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ραδιοφωνική εκπομπή για την ιστορία των καθημερινών αντικειμένων.",
 "script": [
  L("Ομιλητής", "m", "Λέμε «δεξιόστροφα» και «αριστερόστροφα» χωρίς να το σκεφτούμε, σαν να ήταν η φορά του ρολογιού ένας φυσικός νόμος. Δεν είναι. Είναι μια σύμβαση, που όμως έχει μια πολύ λογική προέλευση: το ηλιακό ρολόι.", "We say 'clockwise' and 'anticlockwise' without thinking, as if the direction of the clock were a law of nature. It isn't. It is a convention, but one with a very logical origin: the sundial."),
  L("Ομιλητής", "m", "Στο βόρειο ημισφαίριο, ο ήλιος ανατέλλει στα ανατολικά, περνά από τον νότο και δύει στα δυτικά. Η σκιά του γνώμονα πάνω σε ένα οριζόντιο ηλιακό ρολόι κινείται έτσι από τα αριστερά προς τα δεξιά, γύρω από ένα κέντρο. Όταν, στον Μεσαίωνα, κατασκευάστηκαν στην Ευρώπη τα πρώτα μηχανικά ρολόγια, οι τεχνίτες μιμήθηκαν απλώς την κίνηση που όλοι γνώριζαν.", "In the northern hemisphere, the sun rises in the east, passes through the south and sets in the west. The shadow of the gnomon on a horizontal sundial thus moves from left to right, around a centre. When the first mechanical clocks were built in Europe in the Middle Ages, the craftsmen simply imitated the movement everyone knew."),
  L("Ομιλητής", "m", "Αν τα πρώτα ρολόγια είχαν κατασκευαστεί στο νότιο ημισφαίριο, όπου η σκιά κινείται αντίστροφα, ίσως σήμερα να λέγαμε «δεξιόστροφα» για την αντίθετη κίνηση. Και υπήρξαν εξαιρέσεις: στον καθεδρικό ναό της Φλωρεντίας, για παράδειγμα, ένα ρολόι του 15ου αιώνα, που διακόσμησε ο ζωγράφος Πάολο Ουτσέλο, γυρίζει αντίθετα από τα σημερινά.", "If the first clocks had been built in the southern hemisphere, where the shadow moves the other way, perhaps today we would say 'clockwise' for the opposite movement. And there were exceptions: in Florence Cathedral, for example, a fifteenth-century clock decorated by the painter Paolo Uccello turns the opposite way to today's clocks."),
  L("Ομιλητής", "m", "Από τη στιγμή που μια σύμβαση επικρατήσει, γίνεται σχεδόν αδύνατο να αλλάξει. Τα βιδώματα, τα καπάκια των βάζων, οι βρύσες: όλα κουβαλούν, με τον τρόπο τους, την ίδια σιωπηλή συμφωνία. Και κάθε φορά που κοιτάμε το ρολόι μας, χωρίς να το ξέρουμε, ακολουθούμε τη σκιά ενός ραβδιού στον ήλιο.", "Once a convention prevails, it becomes almost impossible to change. Screw threads, jar lids, taps: all carry, in their own way, the same silent agreement. And every time we look at our watch, without knowing it, we are following the shadow of a stick in the sun."),
 ],
 "questions": [
  Q("Πώς χαρακτηρίζει ο ομιλητής τη φορά του ρολογιού;", ["Ως φυσικό νόμο", "Ως σύμβαση με λογική προέλευση", "Ως τυχαία επιλογή ενός βασιλιά", "Ως εφεύρεση του 20ού αιώνα"], 1, "Είναι μια σύμβαση, που όμως έχει μια πολύ λογική προέλευση"),
  Q("Από πού πήραν οι πρώτοι κατασκευαστές την κίνηση των δεικτών;", ["Από την κίνηση των πλανητών", "Από τη σκιά στα ηλιακά ρολόγια του βόρειου ημισφαιρίου", "Από τη φορά της γραφής", "Από τους ανεμόμυλους"], 1, "Η σκιά του γνώμονα ... κινείται έτσι από τα αριστερά προς τα δεξιά ... οι τεχνίτες μιμήθηκαν απλώς την κίνηση"),
  Q("Τι ιδιαίτερο έχει το ρολόι στον καθεδρικό της Φλωρεντίας;", ["Δεν έχει δείκτες", "Είναι το παλαιότερο του κόσμου", "Γυρίζει αντίθετα από τα σημερινά ρολόγια", "Δείχνει μόνο τις ώρες της προσευχής"], 2, "γυρίζει αντίθετα από τα σημερινά"),
  Q("Τι λέει στο τέλος για τις συμβάσεις;", ["Ότι αλλάζουν εύκολα", "Ότι, όταν επικρατήσουν, αλλάζουν πολύ δύσκολα", "Ότι διαφέρουν σε κάθε χώρα", "Ότι πρέπει να καταργηθούν"], 1, "Από τη στιγμή που μια σύμβαση επικρατήσει, γίνεται σχεδόν αδύνατο να αλλάξει"),
 ],
 "gloss": {"δεξιόστροφα": "δεξιόστροφα — clockwise", "αριστερόστροφα": "αριστερόστροφα — anticlockwise", "φορά": "φορά — direction; time, occasion", "σύμβαση": "σύμβαση — convention; contract", "ημισφαίριο": "ημισφαίριο — hemisphere", "ανατέλλει": "ανατέλλω — to rise (sun)", "γνώμονα": "γνώμονας — gnomon (of a sundial)", "μιμήθηκαν": "μιμούμαι — to imitate", "επικρατήσει": "επικρατώ — to prevail", "βιδώματα": "βίδωμα — screwing; screw thread"},
})
ITEMS.append({
 "id": "l226-c1-int-kryptografos", "title": "Μια κρυπτογράφος μιλά για τα μυστικά μας", "title_en": "A cryptographer on our secrets", "type": "interview", "level": "C1",
 "context_el": "Μια ερευνήτρια της κρυπτογραφίας μιλά σε μια ραδιοφωνική εκπομπή για την ασφάλεια των δεδομένων.",
 "script": [
  L("Δημοσιογράφος", "m", "Όταν ακούμε «κρυπτογραφία», οι περισσότεροι σκεφτόμαστε κατασκόπους και μυστικά μηνύματα στον πόλεμο. Πόσο παρούσα είναι στην καθημερινή μας ζωή;", "When we hear 'cryptography', most of us think of spies and secret wartime messages. How present is it in our everyday lives?"),
  L("Κρυπτογράφος", "f", "Πολύ περισσότερο απ’ όσο φαντάζεστε. Κάθε φορά που πληρώνετε με κάρτα, που στέλνετε ένα μήνυμα ή που ανοίγετε μια ιστοσελίδα με το λουκετάκι στη γραμμή διευθύνσεων, η κρυπτογραφία δουλεύει στο παρασκήνιο. Είναι τα μαθηματικά που εξασφαλίζουν ότι ό,τι στέλνετε θα το διαβάσει μόνο αυτός για τον οποίο προορίζεται.", "Much more than you imagine. Every time you pay by card, send a message or open a web page with the little padlock in the address bar, cryptography is working in the background. It is the mathematics that ensures that whatever you send will be read only by the person it is meant for."),
  L("Δημοσιογράφος", "m", "Και πού βρίσκεται συνήθως το αδύναμο σημείο;", "And where is the weak point usually?"),
  L("Κρυπτογράφος", "f", "Σχεδόν ποτέ στα μαθηματικά. Οι σύγχρονοι αλγόριθμοι, αν εφαρμοστούν σωστά, είναι εξαιρετικά δύσκολο να «σπάσουν». Το αδύναμο σημείο είναι ο άνθρωπος: οι εύκολοι κωδικοί, ο ίδιος κωδικός παντού, το μήνυμα που μας ζητά να «επιβεβαιώσουμε τα στοιχεία μας». Οι επιτιθέμενοι δεν χρειάζεται να λύσουν εξισώσεις, αν μπορούν απλώς να μας ξεγελάσουν.", "Almost never in the mathematics. Modern algorithms, if implemented correctly, are extremely hard to 'break'. The weak point is the human being: easy passwords, the same password everywhere, the message asking us to 'confirm our details'. Attackers don't need to solve equations if they can simply trick us."),
  L("Δημοσιογράφος", "m", "Ακούμε συχνά ότι οι κβαντικοί υπολογιστές θα τα αλλάξουν όλα. Πρέπει να ανησυχούμε;", "We often hear that quantum computers will change everything. Should we be worried?"),
  L("Κρυπτογράφος", "f", "Να ανησυχούμε όχι, να προετοιμαζόμαστε ναι. Ένας αρκετά ισχυρός κβαντικός υπολογιστής θα μπορούσε, θεωρητικά, να σπάσει ορισμένα από τα συστήματα που χρησιμοποιούμε σήμερα. Γι’ αυτό η κοινότητα δουλεύει εδώ και χρόνια σε νέους αλγόριθμους, που θεωρούνται ανθεκτικοί και σε τέτοιες επιθέσεις. Το ενδιαφέρον είναι ότι η αλλαγή πρέπει να γίνει πριν από την απειλή, γιατί κάποια δεδομένα που κλέβονται σήμερα θα μπορούσαν να αποκρυπτογραφηθούν αύριο.", "Worried, no; preparing, yes. A sufficiently powerful quantum computer could, in theory, break some of the systems we use today. That's why the community has been working for years on new algorithms, which are considered resistant to such attacks too. The interesting thing is that the change must happen before the threat, because some data stolen today could be decrypted tomorrow."),
 ],
 "questions": [
  Q("Πού συναντάμε την κρυπτογραφία στην καθημερινή ζωή, σύμφωνα με την ίδια;", ["Μόνο στις τράπεζες", "Στις πληρωμές με κάρτα, στα μηνύματα και στις ασφαλείς ιστοσελίδες", "Μόνο στον στρατό", "Μόνο στα ηλεκτρονικά παιχνίδια"], 1, "Κάθε φορά που πληρώνετε με κάρτα, που στέλνετε ένα μήνυμα ή που ανοίγετε μια ιστοσελίδα με το λουκετάκι"),
  Q("Πού βρίσκεται συνήθως το αδύναμο σημείο;", ["Στους αλγόριθμους", "Στους υπολογιστές", "Στον άνθρωπο", "Στα καλώδια"], 2, "Το αδύναμο σημείο είναι ο άνθρωπος"),
  Q("Τι στάση προτείνει απέναντι στους κβαντικούς υπολογιστές;", ["Πανικό", "Αδιαφορία", "Όχι ανησυχία, αλλά προετοιμασία", "Απαγόρευσή τους"], 2, "Να ανησυχούμε όχι, να προετοιμαζόμαστε ναι"),
  Q("Γιατί πρέπει η αλλαγή να γίνει πριν από την απειλή;", ["Γιατί οι νέοι αλγόριθμοι είναι φθηνότεροι", "Γιατί δεδομένα που κλέβονται σήμερα μπορεί να αποκρυπτογραφηθούν αργότερα", "Γιατί το απαιτεί ο νόμος", "Γιατί οι κβαντικοί υπολογιστές υπάρχουν ήδη παντού"], 1, "κάποια δεδομένα που κλέβονται σήμερα θα μπορούσαν να αποκρυπτογραφηθούν αύριο"),
 ],
 "gloss": {"κρυπτογραφία": "κρυπτογραφία — cryptography", "κατασκόπους": "κατάσκοπος — spy", "παρασκήνιο": "παρασκήνιο — background, behind the scenes", "προορίζεται": "προορίζομαι — to be intended, meant", "αλγόριθμοι": "αλγόριθμος — algorithm", "επιτιθέμενοι": "επιτιθέμενος — attacker", "ξεγελάσουν": "ξεγελώ — to trick, fool", "κβαντικοί": "κβαντικός — quantum", "ανθεκτικοί": "ανθεκτικός — resistant, durable", "αποκρυπτογραφηθούν": "αποκρυπτογραφώ — to decrypt"},
})
rnd = random.Random(226)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-226.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
