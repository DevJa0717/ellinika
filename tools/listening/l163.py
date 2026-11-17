# Source for library/listening/listening-163.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l163.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l163-ann-theofania", "title": "Ανακοίνωση για τη βουτιά των Θεοφανείων", "title_en": "An announcement about the Epiphany dive", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου από το μεγάφωνο του λιμανιού λίγες μέρες πριν από τα Θεοφάνεια.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος ενημερώνει ότι ανήμερα των Θεοφανείων, στις έξι Ιανουαρίου, θα γίνει όπως κάθε χρόνο ο αγιασμός των υδάτων στον κεντρικό μόλο. Η τελετή θα ξεκινήσει μετά τη θεία λειτουργία, γύρω στις έντεκα και μισή.", "The municipality announces that on Epiphany day, the sixth of January, the blessing of the waters will take place as every year at the central pier. The ceremony will begin after the Divine Liturgy, at around half past eleven."),
  L("Εκφωνήτρια", "f", "Όσοι θέλουν να βουτήξουν για τον σταυρό πρέπει να δηλώσουν συμμετοχή στο λιμεναρχείο ως τις τέσσερις Ιανουαρίου. Οι κολυμβητές πρέπει να είναι ενήλικοι και να φέρουν ιατρική βεβαίωση ότι μπορούν να κολυμπήσουν σε κρύο νερό. Δεν θα γίνει δεκτή καμία δήλωση την ίδια μέρα.", "Those who want to dive for the cross must register at the harbour office by the fourth of January. Swimmers must be adults and bring a medical certificate stating that they can swim in cold water. No registration will be accepted on the day itself."),
  L("Εκφωνήτρια", "f", "Για λόγους ασφαλείας, από τις δέκα το πρωί θα απαγορεύεται η στάθμευση σε όλη την παραλιακή οδό, και ένα σκάφος του λιμενικού θα βρίσκεται δίπλα στους κολυμβητές. Μετά την τελετή, ο πολιτιστικός σύλλογος θα προσφέρει ζεστό τσάι και λουκουμάδες στην πλατεία.", "For safety reasons, from ten in the morning parking will be prohibited along the whole seafront road, and a coastguard boat will be next to the swimmers. After the ceremony, the cultural association will offer hot tea and loukoumades in the square."),
 ],
 "questions": [
  Q("Πού πρέπει να δηλώσουν συμμετοχή όσοι θέλουν να βουτήξουν;", ["Στο δημαρχείο", "Στην εκκλησία", "Στο λιμεναρχείο", "Στον πολιτιστικό σύλλογο"], 2, "πρέπει να δηλώσουν συμμετοχή στο λιμεναρχείο ως τις τέσσερις Ιανουαρίου"),
  Q("Τι πρέπει να φέρουν οι κολυμβητές;", ["Ιατρική βεβαίωση ότι μπορούν να κολυμπήσουν σε κρύο νερό", "Στολή κατάδυσης", "Ταυτότητα και φωτογραφία", "Μια άδεια από τον ιερέα"], 0, "να φέρουν ιατρική βεβαίωση ότι μπορούν να κολυμπήσουν σε κρύο νερό"),
  Q("Τι θα απαγορεύεται από τις δέκα το πρωί;", ["Το ψάρεμα στον μόλο", "Η στάθμευση σε όλη την παραλιακή οδό", "Η κυκλοφορία των σκαφών", "Η είσοδος στην πλατεία"], 1, "θα απαγορεύεται η στάθμευση σε όλη την παραλιακή οδό"),
 ],
 "gloss": {"Θεοφανείων": "Θεοφάνεια — Epiphany (6 January)", "ανήμερα": "ανήμερα — on the day itself", "αγιασμός": "αγιασμός — blessing (with holy water)", "υδάτων": "ύδατα — waters (formal)", "μόλο": "μόλος — pier, jetty", "θεία λειτουργία": "θεία λειτουργία — the Divine Liturgy", "βουτήξουν": "βουτάω — to dive", "λιμεναρχείο": "λιμεναρχείο — harbour office, port authority", "κολυμβητές": "κολυμβητής — swimmer", "ενήλικοι": "ενήλικος — adult", "βεβαίωση": "βεβαίωση — certificate", "στάθμευση": "στάθμευση — parking", "παραλιακή": "παραλιακός — seafront (adj.)", "λιμενικού": "λιμενικό — coastguard", "λουκουμάδες": "λουκουμάς — loukoumas (honey doughnut)"},
})

ITEMS.append({
 "id": "l163-int-laxanagora", "title": "Νύχτες στη λαχαναγορά", "title_en": "Nights at the wholesale produce market", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν έμπορο που δουλεύει στην κεντρική λαχαναγορά μιας μεγάλης πόλης.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι ώρα ξεκινάει η μέρα σας;", "What time does your day start?"),
  L("Έμπορος", "m", "Η δική μου μέρα ξεκινάει όταν οι περισσότεροι πάνε για ύπνο. Τα φορτηγά από τους παραγωγούς φτάνουν γύρω στα μεσάνυχτα, και ως τις τρεις πρέπει να έχουμε ξεφορτώσει και να έχουμε στήσει τα κιβώτια. Τότε αρχίζουν να έρχονται οι μανάβηδες και οι μάγειροι των εστιατορίων.", "My day starts when most people are going to bed. The lorries from the growers arrive around midnight, and by three we must have unloaded and set out the crates. That's when the greengrocers and the restaurant cooks start coming."),
  L("Δημοσιογράφος", "f", "Πώς ορίζεται η τιμή;", "How is the price set?"),
  L("Έμπορος", "m", "Καθαρά από την προσφορά και τη ζήτηση. Αν μια βροχή στον κάμπο έχει χαλάσει τις ντομάτες, η τιμή ανεβαίνει μέσα σε μια νύχτα. Αν φτάσουν διπλάσια πορτοκάλια απ' όσα χρειάζεται η αγορά, στις έξι το πρωί τα δίνω σχεδόν όσο τα πήρα, γιατί αύριο θα είναι χειρότερα.", "Purely from supply and demand. If rain on the plain has spoiled the tomatoes, the price goes up within one night. If twice as many oranges arrive as the market needs, at six in the morning I give them away for almost what I paid, because tomorrow they'll be worse."),
  L("Δημοσιογράφος", "f", "Δεν σας κουράζει αυτό το πρόγραμμα;", "Doesn't this schedule tire you?"),
  L("Έμπορος", "m", "Το σώμα συνηθίζει, η οικογένεια λιγότερο. Βλέπω τα παιδιά μου μόνο το μεσημέρι, όταν γυρίζουν από το σχολείο. Αλλά αυτή η δουλειά έχει κάτι που δεν βρίσκεις αλλού: τα συμφωνούμε όλα με μια χειραψία, χωρίς χαρτιά, και ο λόγος σου είναι το μόνο σου κεφάλαιο.", "The body gets used to it, the family less so. I see my children only at midday, when they come back from school. But this job has something you don't find elsewhere: we agree everything with a handshake, without papers, and your word is your only capital."),
 ],
 "questions": [
  Q("Πότε φτάνουν τα φορτηγά από τους παραγωγούς;", ["Γύρω στα μεσάνυχτα", "Στις τρεις το πρωί", "Στις έξι το πρωί", "Το μεσημέρι"], 0, "Τα φορτηγά από τους παραγωγούς φτάνουν γύρω στα μεσάνυχτα"),
  Q("Γιατί πουλάει φθηνά τα πορτοκάλια όταν φτάνουν πάρα πολλά;", ["Γιατί είναι χαλασμένα", "Γιατί αύριο θα είναι χειρότερα", "Γιατί το ζητάει ο νόμος", "Γιατί οι μανάβηδες δεν τα θέλουν"], 1, "γιατί αύριο θα είναι χειρότερα"),
  Q("Τι εκτιμά περισσότερο στη δουλειά του;", ["Τον καλό μισθό", "Τις ελεύθερες ώρες του απογεύματος", "Ότι όλα συμφωνούνται με μια χειραψία και ο λόγος του μετράει", "Ότι δουλεύει μόνος του"], 2, "τα συμφωνούμε όλα με μια χειραψία, χωρίς χαρτιά"),
 ],
 "gloss": {"λαχαναγορά": "λαχαναγορά — wholesale fruit and vegetable market", "έμπορο": "έμπορος — trader, merchant", "παραγωγούς": "παραγωγός — producer, grower", "ξεφορτώσει": "ξεφορτώνω — to unload", "κιβώτια": "κιβώτιο — crate", "μανάβηδες": "μανάβης — greengrocer", "προσφορά": "προσφορά — supply", "ζήτηση": "ζήτηση — demand", "κάμπο": "κάμπος — plain", "διπλάσια": "διπλάσιος — double, twice as many", "χειραψία": "χειραψία — handshake", "κεφάλαιο": "κεφάλαιο — capital"},
})

ITEMS.append({
 "id": "l163-int-delivery", "title": "Στη σέλα του ντελίβερι", "title_en": "In the delivery rider's saddle", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια διανομέα που μεταφέρει φαγητό με μηχανάκι για μια εφαρμογή.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσες παραγγελίες κάνετε σε μια βάρδια;", "How many orders do you do in a shift?"),
  L("Διανομέας", "f", "Ένα συνηθισμένο βράδυ γύρω στις είκοσι. Αν βρέχει, πολύ περισσότερες, γιατί κανείς δεν θέλει να βγει από το σπίτι. Είναι παράξενο: οι χειρότερες συνθήκες για μένα είναι οι καλύτερες για τα κέρδη μου.", "On an ordinary evening around twenty. If it's raining, many more, because nobody wants to leave the house. It's strange: the worst conditions for me are the best for my earnings."),
  L("Δημοσιογράφος", "m", "Τι σας δυσκολεύει περισσότερο;", "What do you find hardest?"),
  L("Διανομέας", "f", "Η πίεση του χρόνου. Η εφαρμογή δείχνει στον πελάτη πού βρίσκομαι κάθε δευτερόλεπτο, και αν αργήσω, μπορεί να μου βάλει κακή βαθμολογία. Με χαμηλή βαθμολογία παίρνεις λιγότερες παραγγελίες. Έτσι, ενώ κανείς δεν σου λέει να τρέχεις, το σύστημα σε σπρώχνει να τρέχεις.", "Time pressure. The app shows the customer where I am every second, and if I'm late, they may give me a bad rating. With a low rating you get fewer orders. So, while nobody tells you to rush, the system pushes you to rush."),
  L("Δημοσιογράφος", "m", "Τι θα αλλάζατε, αν μπορούσατε;", "What would you change, if you could?"),
  L("Διανομέας", "f", "Πρώτα την ασφάλιση. Το μηχανάκι είναι δικό μου, η βενζίνη δική μου, και αν πέσω, η ζημιά είναι επίσης δική μου. Και κάτι μικρό: οι πολυκατοικίες χωρίς νούμερα και ονόματα στα κουδούνια. Χάνω πέντε λεπτά ψάχνοντας, και ο πελάτης νομίζει ότι έκανα βόλτα.", "First, the insurance. The motorbike is mine, the petrol mine, and if I fall, the damage is mine too. And something small: blocks of flats without numbers and names on the doorbells. I lose five minutes searching, and the customer thinks I went for a ride."),
 ],
 "questions": [
  Q("Τι συμβαίνει με τις παραγγελίες όταν βρέχει;", ["Μειώνονται", "Αυξάνονται πολύ", "Σταματούν εντελώς", "Μένουν ίδιες"], 1, "Αν βρέχει, πολύ περισσότερες"),
  Q("Γιατί, κατά τη διανομέα, οι διανομείς τρέχουν;", ["Γιατί τους το ζητάει ο προϊστάμενος", "Γιατί πληρώνονται με την ώρα", "Γιατί η κακή βαθμολογία φέρνει λιγότερες παραγγελίες", "Γιατί το φαγητό κρυώνει"], 2, "Με χαμηλή βαθμολογία παίρνεις λιγότερες παραγγελίες"),
  Q("Ποιο μικρό πρόβλημα αναφέρει στο τέλος;", ["Τις πολυκατοικίες χωρίς νούμερα και ονόματα στα κουδούνια", "Τα σκυλιά στις αυλές", "Τους πελάτες που δεν δίνουν φιλοδώρημα", "Τα ασανσέρ που δεν λειτουργούν"], 0, "οι πολυκατοικίες χωρίς νούμερα και ονόματα στα κουδούνια"),
 ],
 "gloss": {"διανομέα": "διανομέας — delivery person", "εφαρμογή": "εφαρμογή — app", "παραγγελίες": "παραγγελία — order", "βάρδια": "βάρδια — shift", "κέρδη": "κέρδος — earnings, profit", "βαθμολογία": "βαθμολογία — rating", "σπρώχνει": "σπρώχνω — to push", "ασφάλιση": "ασφάλιση — insurance", "κουδούνια": "κουδούνι — doorbell"},
})

ITEMS.append({
 "id": "l163-dia-coworking", "title": "Ένα γραφείο που το μοιράζεσαι", "title_en": "An office you share", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλους που δουλεύουν από το σπίτι να συζητούν αν θα νοικιάσουν θέση σε έναν συνεργατικό χώρο εργασίας.",
 "script": [
  L("Νεφέλη", "f", "Άκου, δεν αντέχω άλλο να μεταφράζω στο τραπέζι της κουζίνας. Βρήκα έναν συνεργατικό χώρο δύο στάσεις με το μετρό. Σταθερό γραφείο εκατόν πενήντα ευρώ τον μήνα, ή ενενήντα αν κάθεσαι όπου βρεις ελεύθερη θέση.", "Listen, I can't stand translating at the kitchen table any longer. I found a co-working space two stops away by metro. A fixed desk is a hundred and fifty euros a month, or ninety if you sit wherever you find a free seat."),
  L("Στάθης", "m", "Ενενήντα για μια καρέκλα που δεν είναι καν δική σου; Εγώ στο σπίτι δεν πληρώνω τίποτα.", "Ninety for a chair that isn't even yours? At home I pay nothing."),
  L("Νεφέλη", "f", "Πληρώνεις όμως ρεύμα και θέρμανση όλη μέρα. Και πόσες φορές μου έχεις πει ότι μιλάς μόνο με τη γάτα από τη Δευτέρα ως την Παρασκευή; Εκεί έχει κόσμο, καφέ, αίθουσα για συναντήσεις με πελάτες.", "But you pay for electricity and heating all day. And how many times have you told me that you talk only to the cat from Monday to Friday? There are people there, coffee, a room for meetings with clients."),
  L("Στάθης", "m", "Εντάξει, αυτό με τους πελάτες με ενδιαφέρει. Τα σχέδιά μου δεν τα δείχνω με χαρά δίπλα στο άπλυτο πιάτο. Αλλά φοβάμαι τον θόρυβο. Εγώ θέλω ησυχία για να συγκεντρωθώ.", "OK, that bit about clients interests me. I don't enjoy showing my designs next to an unwashed plate. But I'm afraid of the noise. I need quiet to concentrate."),
  L("Νεφέλη", "f", "Έχει και κλειστά δωμάτια σιωπής. Ας πάμε την Πέμπτη: η πρώτη μέρα είναι δωρεάν, να δοκιμάσουμε πριν δεσμευτούμε.", "It also has closed silent rooms. Let's go on Thursday: the first day is free, so we can try before we commit."),
  L("Στάθης", "m", "Μια δωρεάν μέρα δεν τη λέω όχι. Αλλά αν με ενοχλήσει κανείς με τηλεφωνήματα στο διπλανό γραφείο, γυρίζω στη γάτα μου.", "I won't say no to a free day. But if anyone bothers me with phone calls at the next desk, I'm going back to my cat."),
 ],
 "questions": [
  Q("Πόσο κοστίζει ένα σταθερό γραφείο τον μήνα;", ["Ενενήντα ευρώ", "Εκατό ευρώ", "Εκατόν πενήντα ευρώ", "Διακόσια ευρώ"], 2, "Σταθερό γραφείο εκατόν πενήντα ευρώ τον μήνα"),
  Q("Τι ενδιαφέρει τον Στάθη στον συνεργατικό χώρο;", ["Ο φθηνός καφές", "Η αίθουσα για συναντήσεις με πελάτες", "Η κοντινή απόσταση", "Οι νέες γνωριμίες"], 1, "αυτό με τους πελάτες με ενδιαφέρει"),
  Q("Τι αποφασίζουν στο τέλος;", ["Να νοικιάσουν αμέσως δύο γραφεία", "Να μείνουν στο σπίτι", "Να πάνε την Πέμπτη για μια δωρεάν δοκιμαστική μέρα", "Να ψάξουν άλλον χώρο"], 2, "η πρώτη μέρα είναι δωρεάν, να δοκιμάσουμε πριν δεσμευτούμε"),
 ],
 "gloss": {"συνεργατικό χώρο": "συνεργατικός χώρος — co-working space", "νοικιάσουν": "νοικιάζω — to rent", "μεταφράζω": "μεταφράζω — to translate", "Σταθερό": "σταθερός — fixed", "θέρμανση": "θέρμανση — heating", "αίθουσα": "αίθουσα — room, hall", "σχέδιά": "σχέδιο — design, drawing", "άπλυτο": "άπλυτος — unwashed", "συγκεντρωθώ": "συγκεντρώνομαι — to concentrate", "σιωπής": "σιωπή — silence", "δεσμευτούμε": "δεσμεύομαι — to commit oneself", "ενοχλήσει": "ενοχλώ — to bother"},
})

ITEMS.append({
 "id": "l163-dia-apothiki", "title": "Πού θα μείνουν τα πράγματα;", "title_en": "Where will the things stay?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο αδέλφια να συζητούν τι θα κάνει η αδελφή με τα πράγματά της όσο θα δουλεύει έναν χρόνο στο εξωτερικό.",
 "script": [
  L("Μυρτώ", "f", "Το συμβόλαιο στη Ρότερνταμ είναι για δώδεκα μήνες, και το σπίτι πρέπει να το αδειάσω ως το τέλος του μήνα. Σκέφτομαι να νοικιάσω μια μικρή αποθήκη. Βρήκα μία με τρία τετραγωνικά για σαράντα ευρώ τον μήνα.", "The contract in Rotterdam is for twelve months, and I have to empty the flat by the end of the month. I'm thinking of renting a small storage unit. I found one of three square metres for forty euros a month."),
  L("Άρης", "m", "Σαράντα επί δώδεκα κάνει τετρακόσια ογδόντα. Με αυτά τα λεφτά αγοράζεις καινούργια τα μισά από αυτά που θα φυλάξεις. Γιατί δεν τα φέρνεις στο υπόγειό μας;", "Forty times twelve makes four hundred and eighty. With that money you could buy new half of what you'll store. Why don't you bring them to our basement?"),
  L("Μυρτώ", "f", "Γιατί το υπόγειό σας πλημμύρισε πέρσι, θυμάσαι; Τα βιβλία μου δεν θα επιζούσαν από δεύτερη πλημμύρα. Η αποθήκη έχει σταθερή θερμοκρασία και κάμερες.", "Because your basement flooded last year, remember? My books wouldn't survive a second flood. The storage unit has a constant temperature and cameras."),
  L("Άρης", "m", "Τότε κάνε ένα ξεσκαρτάρισμα πρώτα. Τον καναπέ τον έχεις δέκα χρόνια και η ταπετσαρία του έχει σκιστεί. Τα έπιπλα που δεν θα ξαναχρησιμοποιήσεις, πούλησέ τα ή χάρισέ τα.", "Then do a clear-out first. You've had the sofa for ten years and its upholstery is torn. The furniture you won't use again, sell it or give it away."),
  L("Μυρτώ", "f", "Λογικό. Αν κρατήσω μόνο τα βιβλία, τα ρούχα του χειμώνα και το ποδήλατο, μου φτάνει η αποθήκη του ενός τετραγωνικού, που κοστίζει τα μισά.", "Makes sense. If I keep only the books, the winter clothes and the bicycle, the one-square-metre unit is enough for me, and it costs half."),
  L("Άρης", "m", "Και το ποδήλατο άφησέ το σε μένα. Θα το προσέχω σαν να ήταν δικό μου.", "And leave the bicycle with me. I'll look after it as if it were mine."),
 ],
 "questions": [
  Q("Γιατί η Μυρτώ δεν θέλει να βάλει τα πράγματά της στο υπόγειο του Άρη;", ["Γιατί είναι πολύ μακριά", "Γιατί το υπόγειο πλημμύρισε πέρσι", "Γιατί δεν έχει χώρο", "Γιατί δεν έχει κάμερες"], 1, "Γιατί το υπόγειό σας πλημμύρισε πέρσι"),
  Q("Τι της προτείνει ο Άρης για τα έπιπλα που δεν θα ξαναχρησιμοποιήσει;", ["Να τα πουλήσει ή να τα χαρίσει", "Να τα πάρει μαζί της", "Να τα αφήσει στο σπίτι", "Να τα επισκευάσει"], 0, "πούλησέ τα ή χάρισέ τα"),
  Q("Τι θα κάνει τελικά με το ποδήλατο;", ["Θα το βάλει στην αποθήκη", "Θα το πουλήσει", "Θα το πάρει στη Ρότερνταμ", "Θα το αφήσει στον Άρη"], 3, "Και το ποδήλατο άφησέ το σε μένα"),
 ],
 "gloss": {"συμβόλαιο": "συμβόλαιο — contract", "Ρότερνταμ": "Ρότερνταμ — Rotterdam", "αδειάσω": "αδειάζω — to empty", "αποθήκη": "αποθήκη — storage unit, storeroom", "τετραγωνικά": "τετραγωνικό — square metre", "φυλάξεις": "φυλάω — to keep, to store", "υπόγειό": "υπόγειο — basement", "πλημμύρισε": "πλημμυρίζω — to flood", "επιζούσαν": "επιζώ — to survive", "ξεσκαρτάρισμα": "ξεσκαρτάρισμα — clear-out", "ταπετσαρία": "ταπετσαρία — upholstery", "σκιστεί": "σκίζομαι — to get torn", "χάρισέ": "χαρίζω — to give away"},
})

ITEMS.append({
 "id": "l163-mon-limenarxeio", "title": "Μια χρονιά σε ένα μικρό λιμεναρχείο", "title_en": "A year at a small harbour office", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια υπαξιωματικό του λιμενικού να μιλάει για την πρώτη της χρονιά σε ένα μικρό νησί.",
 "script": [
  L("Λιμενικός", "f", "Όταν πήρα τη μετάθεση για ένα νησί με τριακόσιους κατοίκους, νόμιζα ότι θα βαριόμουν. Το λιμεναρχείο ήταν ένα δωμάτιο με δύο γραφεία, έναν ασύρματο και μια φωτογραφία του παλιού λιμανιού στον τοίχο. Ήμασταν τρεις, και τον χειμώνα το πλοίο ερχόταν δύο φορές την εβδομάδα.", "When I got the transfer to an island with three hundred inhabitants, I thought I'd be bored. The harbour office was one room with two desks, a radio and a photo of the old harbour on the wall. There were three of us, and in winter the ship came twice a week."),
  L("Λιμενικός", "f", "Γρήγορα κατάλαβα ότι εδώ το λιμενικό δεν είναι μόνο ελέγχοι και πρόστιμα. Όταν ο καιρός κλείνει τη θάλασσα, εμείς είμαστε αυτοί που λέμε στον κόσμο ότι το πλοίο δεν θα έρθει, και ότι τα φάρμακα ή το ψωμί θα αργήσουν. Οι άνθρωποι θυμώνουν, αλλά θυμώνουν με τον καιρό, όχι με εμάς.", "I soon understood that here the coastguard isn't only checks and fines. When the weather closes the sea, we're the ones who tell people that the ship won't come, and that the medicines or the bread will be late. People get angry, but they're angry with the weather, not with us."),
  L("Λιμενικός", "f", "Η πιο δύσκολη νύχτα ήταν τον Φεβρουάριο, όταν ένας ηλικιωμένος έπαθε εγκεφαλικό. Με οκτώ μποφόρ κανένα σκάφος δεν μπορούσε να βγει, και περιμέναμε το ελικόπτερο τρεις ώρες στο γήπεδο του χωριού, με τους ψαράδες να φωτίζουν το έδαφος με τα αυτοκίνητά τους. Σήμερα εκείνος ο κύριος μου φέρνει κάθε Κυριακή φρέσκα αυγά. Δεν βαρέθηκα ούτε μία μέρα.", "The hardest night was in February, when an elderly man had a stroke. With eight on the Beaufort scale no boat could go out, and we waited three hours for the helicopter at the village football pitch, with the fishermen lighting the ground with their cars. Today that gentleman brings me fresh eggs every Sunday. I haven't been bored for a single day."),
 ],
 "questions": [
  Q("Τι περίμενε η λιμενικός όταν πήρε τη μετάθεση;", ["Ότι θα είχε πολλή δουλειά", "Ότι θα βαριόταν", "Ότι θα έμενε λίγους μήνες", "Ότι θα έβρισκε φίλους"], 1, "νόμιζα ότι θα βαριόμουν"),
  Q("Με ποιον θυμώνουν οι κάτοικοι όταν δεν έρχεται το πλοίο, σύμφωνα με εκείνη;", ["Με τον καιρό", "Με το λιμενικό", "Με την εταιρεία του πλοίου", "Με τον δήμαρχο"], 0, "θυμώνουν με τον καιρό, όχι με εμάς"),
  Q("Πώς βοήθησαν οι ψαράδες τη νύχτα του Φεβρουαρίου;", ["Μετέφεραν τον ασθενή με τη βάρκα τους", "Κάλεσαν το ελικόπτερο", "Φώτισαν το έδαφος με τα αυτοκίνητά τους", "Έφεραν έναν γιατρό από το διπλανό νησί"], 2, "με τους ψαράδες να φωτίζουν το έδαφος με τα αυτοκίνητά τους"),
 ],
 "gloss": {"υπαξιωματικό": "υπαξιωματικός — petty officer, NCO", "λιμενικού": "λιμενικό — coastguard", "μετάθεση": "μετάθεση — (job) transfer", "λιμεναρχείο": "λιμεναρχείο — harbour office", "ασύρματο": "ασύρματος — radio (transmitter)", "ελέγχοι": "έλεγχος — check, inspection", "πρόστιμα": "πρόστιμο — fine", "εγκεφαλικό": "εγκεφαλικό — stroke", "μποφόρ": "μποφόρ — Beaufort (wind force)", "ελικόπτερο": "ελικόπτερο — helicopter", "γήπεδο": "γήπεδο — (football) pitch", "φωτίζουν": "φωτίζω — to light up"},
})

ITEMS.append({
 "id": "l163-vm-katataktirio", "title": "Μήνυμα από τη σχολή για το κατατακτήριο τεστ", "title_en": "A message from the school about the placement test", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη γραμματεία μιας σχολής ξένων γλωσσών.",
 "script": [
  L("Γραμματεία", "f", "Καλησπέρα σας, εδώ Δήμητρα από τη γραμματεία της σχολής. Σας καλώ για το κατατακτήριο τεστ στα γερμανικά που είχατε κλείσει για την Τρίτη στις έξι. Δυστυχώς η καθηγήτρια που το διορθώνει θα λείπει, οπότε το μεταφέρουμε για την Πέμπτη στην ίδια ώρα.", "Good evening, this is Dimitra from the school office. I'm calling about the German placement test you had booked for Tuesday at six. Unfortunately the teacher who marks it will be away, so we're moving it to Thursday at the same time."),
  L("Γραμματεία", "f", "Το τεστ έχει ένα γραπτό μέρος, περίπου σαράντα λεπτά, και μια σύντομη προφορική συζήτηση. Δεν χρειάζεται να διαβάσετε τίποτα· ο σκοπός είναι μόνο να σας βάλουμε στο σωστό τμήμα. Φέρτε μόνο ένα στυλό και την ταυτότητά σας.", "The test has a written part, about forty minutes, and a short oral conversation. You don't need to study anything; the aim is only to put you in the right class. Just bring a pen and your ID card."),
  L("Γραμματεία", "f", "Αν η Πέμπτη δεν σας βολεύει, στείλτε μου ένα μήνυμα μέχρι αύριο το μεσημέρι, για να σας βρω άλλη ώρα πριν αρχίσουν τα μαθήματα στις δεκαπέντε του μήνα. Ευχαριστώ, καλό σας βράδυ.", "If Thursday doesn't suit you, send me a message by tomorrow midday, so I can find you another time before classes start on the fifteenth of the month. Thank you, have a good evening."),
 ],
 "questions": [
  Q("Γιατί μεταφέρεται το τεστ;", ["Γιατί η σχολή θα είναι κλειστή", "Γιατί η καθηγήτρια που το διορθώνει θα λείπει", "Γιατί δεν υπάρχουν αρκετοί υποψήφιοι", "Γιατί άλλαξε το πρόγραμμα των μαθημάτων"], 1, "η καθηγήτρια που το διορθώνει θα λείπει"),
  Q("Ποιος είναι ο σκοπός του τεστ;", ["Να πάρετε πιστοποιητικό", "Να σας βάλουν στο σωστό τμήμα", "Να κερδίσετε υποτροφία", "Να δείτε αν περάσατε τον προηγούμενο κύκλο"], 1, "ο σκοπός είναι μόνο να σας βάλουμε στο σωστό τμήμα"),
  Q("Τι πρέπει να κάνετε αν δεν σας βολεύει η Πέμπτη;", ["Να έρθετε την Τρίτη όπως ήταν", "Να πάτε απευθείας στο πρώτο μάθημα", "Να στείλετε μήνυμα ως αύριο το μεσημέρι", "Να τηλεφωνήσετε στην καθηγήτρια"], 2, "στείλτε μου ένα μήνυμα μέχρι αύριο το μεσημέρι"),
 ],
 "gloss": {"κατατακτήριο": "κατατακτήριος — placement (test)", "γραμματεία": "γραμματεία — (school) office, secretariat", "κλείσει": "κλείνω — to book", "διορθώνει": "διορθώνω — to mark, to correct", "μεταφέρουμε": "μεταφέρω — to move, to reschedule", "γραπτό": "γραπτός — written", "προφορική": "προφορικός — oral", "τμήμα": "τμήμα — class, group", "ταυτότητά": "ταυτότητα — ID card", "βολεύει": "βολεύω — to suit"},
})

ITEMS.append({
 "id": "l163-vm-diaitologos", "title": "Μήνυμα από τη διαιτολόγο", "title_en": "A message from the dietitian", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη διαιτολόγο που επισκεφθήκατε την προηγούμενη εβδομάδα.",
 "script": [
  L("Διαιτολόγος", "f", "Καλημέρα, η Αλεξάνδρα Πετρίδου είμαι, η διαιτολόγος. Πήρα τα αποτελέσματα από τις εξετάσεις αίματος που μου στείλατε. Τα περισσότερα είναι μια χαρά, αλλά ο σίδηρος είναι λίγο χαμηλός, πράγμα που εξηγεί την κούραση που μου περιγράψατε.", "Good morning, it's Alexandra Petridou, the dietitian. I've got the results of the blood tests you sent me. Most of them are fine, but your iron is a little low, which explains the tiredness you described to me."),
  L("Διαιτολόγος", "f", "Δεν χρειάζεται να αλλάξουμε όλο το πρόγραμμα. Προσθέστε φακές ή ρεβίθια δύο φορές την εβδομάδα και σπανάκι στις σαλάτες, και πίνετε έναν χυμό πορτοκάλι μαζί με το φαγητό, γιατί η βιταμίνη C βοηθά τον οργανισμό να απορροφά τον σίδηρο. Αντίθετα, τον καφέ και το τσάι καλό είναι να τα πίνετε μία ώρα μετά το γεύμα, όχι μαζί.", "We don't need to change the whole plan. Add lentils or chickpeas twice a week and spinach to your salads, and drink an orange juice with your meal, because vitamin C helps the body absorb iron. On the other hand, it's best to drink coffee and tea an hour after the meal, not with it."),
  L("Διαιτολόγος", "f", "Συμπληρώματα δεν σας προτείνω ακόμη· αυτό θα το αποφασίσει ο γιατρός σας αν οι τιμές δεν βελτιωθούν. Ας ξανακάνουμε εξετάσεις σε τρεις μήνες. Αν έχετε απορίες, με βρίσκετε στο γραφείο κάθε απόγευμα εκτός Τετάρτης.", "I'm not recommending supplements yet; your doctor will decide that if the values don't improve. Let's repeat the tests in three months. If you have any questions, you can find me at the office every afternoon except Wednesday."),
 ],
 "questions": [
  Q("Τι έδειξαν οι εξετάσεις αίματος;", ["Ότι η χοληστερίνη είναι υψηλή", "Ότι ο σίδηρος είναι λίγο χαμηλός", "Ότι όλα είναι τέλεια", "Ότι το σάκχαρο είναι χαμηλό"], 1, "ο σίδηρος είναι λίγο χαμηλός"),
  Q("Γιατί προτείνει χυμό πορτοκάλι με το φαγητό;", ["Γιατί η βιταμίνη C βοηθά τον οργανισμό να απορροφά τον σίδηρο", "Γιατί αντικαθιστά τα φρούτα", "Γιατί κόβει την όρεξη", "Γιατί βοηθά τον ύπνο"], 0, "η βιταμίνη C βοηθά τον οργανισμό να απορροφά τον σίδηρο"),
  Q("Τι λέει για τα συμπληρώματα;", ["Να αρχίσετε αμέσως", "Να τα αγοράσετε από το γραφείο της", "Θα τα αποφασίσει ο γιατρός αν οι τιμές δεν βελτιωθούν", "Δεν βοηθούν ποτέ"], 2, "αυτό θα το αποφασίσει ο γιατρός σας αν οι τιμές δεν βελτιωθούν"),
 ],
 "gloss": {"διαιτολόγο": "διαιτολόγος — dietitian", "εξετάσεις αίματος": "εξετάσεις αίματος — blood tests", "σίδηρος": "σίδηρος — iron", "κούραση": "κούραση — tiredness", "φακές": "φακή — lentil", "ρεβίθια": "ρεβίθι — chickpea", "σπανάκι": "σπανάκι — spinach", "απορροφά": "απορροφώ — to absorb", "γεύμα": "γεύμα — meal", "Συμπληρώματα": "συμπλήρωμα — (dietary) supplement", "βελτιωθούν": "βελτιώνομαι — to improve", "απορίες": "απορία — question, query"},
})

ITEMS.append({
 "id": "l163-c1-lagrange", "title": "Σημεία ισορροπίας στο διάστημα", "title_en": "Points of balance in space", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια αστροφυσικό για τα λεγόμενα σημεία Λαγκράνζ και για το διαστημικό τηλεσκόπιο Τζέιμς Γουέμπ.",
 "script": [
  L("Δημοσιογράφος", "m", "Το τηλεσκόπιο Τζέιμς Γουέμπ δεν βρίσκεται σε τροχιά γύρω από τη Γη, όπως το Χαμπλ. Πού ακριβώς βρίσκεται;", "The James Webb telescope isn't in orbit around the Earth, like Hubble. Where exactly is it?"),
  L("Αστροφυσικός", "f", "Σε ένα σημείο που ονομάζουμε L2, περίπου ενάμισι εκατομμύριο χιλιόμετρα από τη Γη, στην αντίθετη πλευρά από τον Ήλιο. Είναι ένα από τα πέντε σημεία που περιέγραψε τον δέκατο όγδοο αιώνα ο μαθηματικός Ζοζέφ-Λουί Λαγκράνζ. Σε αυτά, η έλξη του Ήλιου και της Γης συνδυάζονται έτσι ώστε ένα μικρό σώμα να μπορεί να περιφέρεται γύρω από τον Ήλιο ακολουθώντας τη Γη, χωρίς να μένει πίσω ούτε να προπορεύεται.", "At a point we call L2, about one and a half million kilometres from the Earth, on the side opposite the Sun. It is one of the five points described in the eighteenth century by the mathematician Joseph-Louis Lagrange. At them, the pull of the Sun and the Earth combine in such a way that a small body can orbit the Sun keeping pace with the Earth, neither falling behind nor getting ahead."),
  L("Δημοσιογράφος", "m", "Και γιατί επιλέχθηκε αυτό το σημείο;", "And why was this point chosen?"),
  L("Αστροφυσικός", "f", "Το Γουέμπ παρατηρεί κυρίως στο υπέρυθρο, δηλαδή καταγράφει θερμότητα. Για να μη «θαμπώνεται» από τη δική του θερμότητα, πρέπει να είναι εξαιρετικά ψυχρό. Από το L2, ο Ήλιος, η Γη και η Σελήνη βρίσκονται πάντα περίπου προς την ίδια κατεύθυνση, οπότε μια μόνο ηλιοπροστασία, μεγέθους γηπέδου τένις, αρκεί για να τα κρύβει όλα ταυτόχρονα.", "Webb observes mainly in the infrared, that is, it records heat. So as not to be 'dazzled' by its own heat, it must be extremely cold. From L2, the Sun, the Earth and the Moon are always roughly in the same direction, so a single sunshield, the size of a tennis court, is enough to hide them all at once."),
  L("Δημοσιογράφος", "m", "Δηλαδή το τηλεσκόπιο απλώς «κάθεται» εκεί;", "So the telescope simply 'sits' there?"),
  L("Αστροφυσικός", "f", "Όχι ακριβώς. Το L2 είναι ασταθές σημείο ισορροπίας, όπως μια μπίλια στην κορυφή ενός λόφου: η παραμικρή απόκλιση μεγαλώνει με τον καιρό. Γι' αυτό το Γουέμπ κάνει μια μεγάλη τροχιά γύρω από το σημείο και ανάβει περιοδικά τους κινητήρες του για μικρές διορθώσεις. Αντίθετα, τα σημεία L4 και L5 είναι ευσταθή· στα αντίστοιχα σημεία του Ήλιου και του Δία έχουν συσσωρευτεί χιλιάδες αστεροειδείς, οι λεγόμενοι Τρώες.", "Not exactly. L2 is an unstable equilibrium point, like a marble on the top of a hill: the slightest deviation grows over time. That's why Webb makes a large orbit around the point and periodically fires its thrusters for small corrections. By contrast, points L4 and L5 are stable; at the corresponding points of the Sun and Jupiter thousands of asteroids have accumulated, the so-called Trojans."),
 ],
 "questions": [
  Q("Τι ισχύει για ένα μικρό σώμα σε ένα σημείο Λαγκράνζ;", ["Περιφέρεται γύρω από τη Γη πιο γρήγορα από τη Σελήνη", "Μπορεί να περιφέρεται γύρω από τον Ήλιο ακολουθώντας τη Γη", "Δεν δέχεται καμία βαρυτική έλξη", "Πλησιάζει σιγά σιγά τον Ήλιο"], 1, "ένα μικρό σώμα να μπορεί να περιφέρεται γύρω από τον Ήλιο ακολουθώντας τη Γη"),
  Q("Γιατί το L2 είναι κατάλληλο για το Γουέμπ;", ["Γιατί εκεί δεν υπάρχει ηλιακό φως", "Γιατί είναι το πιο κοντινό σημείο στη Γη", "Γιατί Ήλιος, Γη και Σελήνη βρίσκονται προς την ίδια κατεύθυνση και μια ηλιοπροστασία τα κρύβει όλα", "Γιατί εκεί το τηλεσκόπιο δεν χρειάζεται καύσιμα"], 2, "μια μόνο ηλιοπροστασία, μεγέθους γηπέδου τένις, αρκεί για να τα κρύβει όλα ταυτόχρονα"),
  Q("Με τι παρομοιάζει η αστροφυσικός το L2;", ["Με μια μπίλια στην κορυφή ενός λόφου", "Με μια μπίλια στον πάτο ενός μπολ", "Με ένα εκκρεμές", "Με μια σβούρα"], 0, "όπως μια μπίλια στην κορυφή ενός λόφου"),
  Q("Τι βρίσκεται στα σημεία L4 και L5 του συστήματος Ήλιου–Δία;", ["Δορυφόροι επικοινωνιών", "Το τηλεσκόπιο Χαμπλ", "Αστεροειδή που ονομάζονται Τρώες", "Κομήτες από το εξωτερικό ηλιακό σύστημα"], 2, "έχουν συσσωρευτεί χιλιάδες αστεροειδείς, οι λεγόμενοι Τρώες"),
 ],
 "gloss": {"αστροφυσικό": "αστροφυσικός — astrophysicist", "ισορροπίας": "ισορροπία — balance, equilibrium", "τροχιά": "τροχιά — orbit", "Λαγκράνζ": "Λαγκράνζ — Lagrange", "έλξη": "έλξη — pull, attraction", "περιφέρεται": "περιφέρομαι — to revolve, to orbit", "προπορεύεται": "προπορεύομαι — to go ahead", "υπέρυθρο": "υπέρυθρο — infrared", "θαμπώνεται": "θαμπώνομαι — to be dazzled, blurred", "ψυχρό": "ψυχρός — cold", "ηλιοπροστασία": "ηλιοπροστασία — sunshield", "ασταθές": "ασταθής — unstable", "μπίλια": "μπίλια — marble", "απόκλιση": "απόκλιση — deviation", "κινητήρες": "κινητήρας — engine, thruster", "ευσταθή": "ευσταθής — stable", "συσσωρευτεί": "συσσωρεύομαι — to accumulate", "αστεροειδείς": "αστεροειδής — asteroid", "Τρώες": "Τρώας — Trojan"},
})

ITEMS.append({
 "id": "l163-c1-magnus", "title": "Γιατί στρίβει η μπάλα", "title_en": "Why the ball curves", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν καθηγητή φυσικής σε μια εκλαϊκευτική διάλεξη για το φαινόμενο Μάγκνους.",
 "script": [
  L("Καθηγητής", "m", "Όσοι παρακολουθείτε ποδόσφαιρο έχετε δει ελεύθερα χτυπήματα όπου η μπάλα ξεκινά προς τα έξω και την τελευταία στιγμή στρίβει προς το δοκάρι. Δεν πρόκειται για οφθαλμαπάτη ούτε για τύχη. Πρόκειται για το λεγόμενο φαινόμενο Μάγκνους, που πήρε το όνομά του από τον Γερμανό φυσικό Χάινριχ Γκούσταβ Μάγκνους, ο οποίος το μελέτησε τον δέκατο ένατο αιώνα.", "Those of you who watch football have seen free kicks where the ball sets off outwards and at the last moment curves towards the goal. It is neither an optical illusion nor luck. It is the so-called Magnus effect, named after the German physicist Heinrich Gustav Magnus, who studied it in the nineteenth century."),
  L("Καθηγητής", "m", "Όταν η μπάλα περιστρέφεται καθώς κινείται, παρασύρει μαζί της ένα λεπτό στρώμα αέρα. Από τη μία πλευρά, η επιφάνεια της μπάλας κινείται προς την ίδια κατεύθυνση με τη ροή του αέρα· από την άλλη, αντίθετα. Το αποτέλεσμα είναι ότι η μπάλα εκτρέπει τον αέρα προς τη μία πλευρά, και σύμφωνα με τον τρίτο νόμο του Νεύτωνα δέχεται ίση και αντίθετη ώθηση. Έτσι στρίβει προς την πλευρά όπου η επιφάνειά της κινείται μαζί με τον αέρα.", "When the ball spins as it moves, it drags a thin layer of air along with it. On one side, the surface of the ball moves in the same direction as the airflow; on the other, against it. The result is that the ball deflects the air to one side, and according to Newton's third law it receives an equal and opposite push. So it curves towards the side where its surface moves with the air."),
  L("Καθηγητής", "m", "Το ίδιο φαινόμενο εξηγεί το κόψιμο στο τένις και το «φάλτσο» στο πινγκ πονγκ. Λιγότερο γνωστό είναι ότι στη δεκαετία του 1920 κατασκευάστηκαν πλοία με τεράστιους περιστρεφόμενους κυλίνδρους αντί για πανιά, που κινούνταν με τον ίδιο τρόπο. Η ιδέα ξεχάστηκε όταν τα καύσιμα έγιναν φθηνά, αλλά τα τελευταία χρόνια ορισμένα φορτηγά πλοία έχουν ξαναβάλει τέτοιους κυλίνδρους για να μειώσουν την κατανάλωση. Είναι ένα καλό παράδειγμα για το πώς μια ιδέα που μοιάζει παρωχημένη μπορεί να επιστρέψει όταν αλλάξουν οι οικονομικές συνθήκες.", "The same effect explains topspin and slice in tennis and 'spin' in table tennis. Less well known is that in the 1920s ships were built with huge rotating cylinders instead of sails, which moved in the same way. The idea was forgotten when fuel became cheap, but in recent years some cargo ships have fitted such cylinders again to reduce consumption. It's a good example of how an idea that seems outdated can return when economic conditions change."),
 ],
 "questions": [
  Q("Τι προκαλεί το στρίψιμο της μπάλας, κατά τον καθηγητή;", ["Ο άνεμος στο γήπεδο", "Η περιστροφή της, που εκτρέπει τον αέρα προς τη μία πλευρά", "Το βάρος της μπάλας", "Η υγρασία του αέρα"], 1, "η μπάλα εκτρέπει τον αέρα προς τη μία πλευρά"),
  Q("Προς ποια πλευρά στρίβει η μπάλα;", ["Προς την πλευρά όπου η επιφάνειά της κινείται μαζί με τον αέρα", "Προς την πλευρά όπου η επιφάνειά της κινείται αντίθετα στον αέρα", "Πάντα προς τα δεξιά", "Προς την πλευρά του ποδιού που την κλώτσησε"], 0, "στρίβει προς την πλευρά όπου η επιφάνειά της κινείται μαζί με τον αέρα"),
  Q("Γιατί ξεχάστηκαν τα πλοία με τους περιστρεφόμενους κυλίνδρους;", ["Γιατί βυθίζονταν εύκολα", "Γιατί ήταν πολύ αργά", "Γιατί τα καύσιμα έγιναν φθηνά", "Γιατί απαγορεύτηκαν"], 2, "Η ιδέα ξεχάστηκε όταν τα καύσιμα έγιναν φθηνά"),
  Q("Ποιο γενικότερο συμπέρασμα βγάζει ο καθηγητής;", ["Ότι οι παλιές τεχνολογίες είναι πάντα καλύτερες", "Ότι μια ιδέα που μοιάζει παρωχημένη μπορεί να επιστρέψει όταν αλλάξουν οι οικονομικές συνθήκες", "Ότι το ποδόσφαιρο βοηθά την επιστήμη", "Ότι οι φυσικοί του 19ου αιώνα είχαν προβλέψει τα πάντα"], 1, "μια ιδέα που μοιάζει παρωχημένη μπορεί να επιστρέψει όταν αλλάξουν οι οικονομικές συνθήκες"),
 ],
 "gloss": {"εκλαϊκευτική": "εκλαϊκευτικός — popular-science", "φαινόμενο": "φαινόμενο — effect, phenomenon", "Μάγκνους": "Μάγκνους — Magnus", "ελεύθερα χτυπήματα": "ελεύθερο χτύπημα — free kick", "δοκάρι": "δοκάρι — goalpost", "οφθαλμαπάτη": "οφθαλμαπάτη — optical illusion", "περιστρέφεται": "περιστρέφομαι — to spin, to rotate", "παρασύρει": "παρασύρω — to drag along", "στρώμα": "στρώμα — layer", "ροή": "ροή — flow", "εκτρέπει": "εκτρέπω — to deflect", "ώθηση": "ώθηση — push, thrust", "κόψιμο": "κόψιμο — slice, cut (in tennis)", "φάλτσο": "φάλτσο — spin, swerve (on a ball)", "κυλίνδρους": "κύλινδρος — cylinder", "πανιά": "πανί — sail", "κατανάλωση": "κατανάλωση — consumption", "παρωχημένη": "παρωχημένος — outdated"},
})

rnd = random.Random(163)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-163.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
