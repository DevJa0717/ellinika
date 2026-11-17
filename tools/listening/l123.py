# Source for library/listening/listening-123.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l123.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l123-ann-palios-stathmos", "title": "Εγκαίνια στον παλιό σιδηροδρομικό σταθμό", "title_en": "Opening at the old railway station", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου σε έναν τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος σάς προσκαλεί στα εγκαίνια του νέου πολιτιστικού κέντρου, που στεγάζεται στο κτίριο του παλιού σιδηροδρομικού σταθμού. Ο σταθμός είχε κλείσει πριν από είκοσι χρόνια, όταν σταμάτησε να λειτουργεί η γραμμή, και αναπαλαιώθηκε με ευρωπαϊκά κονδύλια.", "The municipality invites you to the opening of the new cultural centre, housed in the building of the old railway station. The station had closed twenty years ago, when the line stopped operating, and was restored with European funds."),
  L("Εκφωνήτρια", "f", "Τα εγκαίνια θα γίνουν το Σάββατο στις έξι το απόγευμα. Στην παλιά αίθουσα αναμονής θα εγκαινιαστεί μια έκθεση φωτογραφίας με θέμα την ιστορία της γραμμής, ενώ στις αποβάθρες θα παίξει η φιλαρμονική του δήμου.", "The opening will take place on Saturday at six in the evening. In the old waiting room an exhibition of photographs on the history of the line will open, while the municipal band will play on the platforms."),
  L("Εκφωνήτρια", "f", "Όσοι έχετε παλιές φωτογραφίες ή αντικείμενα από τον σταθμό, μπορείτε να τα δανείσετε στο κέντρο για μια δεύτερη έκθεση τον χειμώνα. Πληροφορίες στο δημαρχείο, στο γραφείο πολιτισμού. Η είσοδος στα εγκαίνια είναι ελεύθερη.", "Those of you who have old photographs or objects from the station can lend them to the centre for a second exhibition in winter. Information at the town hall, at the culture office. Admission to the opening is free."),
 ],
 "questions": [
  Q("Πώς αναπαλαιώθηκε ο σταθμός;", ["Με δωρεές των κατοίκων", "Με ευρωπαϊκά κονδύλια", "Με χρήματα του σιδηροδρόμου", "Από εθελοντές"], 1, "αναπαλαιώθηκε με ευρωπαϊκά κονδύλια"),
  Q("Τι θα γίνει στην παλιά αίθουσα αναμονής;", ["Μια συναυλία", "Ένα πάρτι για παιδιά", "Μια έκθεση φωτογραφίας για την ιστορία της γραμμής", "Μια διάλεξη"], 2, "θα εγκαινιαστεί μια έκθεση φωτογραφίας με θέμα την ιστορία της γραμμής"),
  Q("Τι ζητά ο δήμος από τους κατοίκους;", ["Να δανείσουν παλιές φωτογραφίες ή αντικείμενα από τον σταθμό", "Να γίνουν εθελοντές στα εγκαίνια", "Να αγοράσουν εισιτήρια", "Να ψηφίσουν για το όνομα του κέντρου"], 0, "μπορείτε να τα δανείσετε στο κέντρο"),
 ],
 "gloss": {"εγκαίνια": "εγκαίνια — opening, inauguration", "στεγάζεται": "στεγάζομαι — to be housed", "σιδηροδρομικού": "σιδηροδρομικός — railway (adj.)", "αναπαλαιώθηκε": "αναπαλαιώνω — to restore (an old building)", "κονδύλια": "κονδύλι — fund, budget item", "αίθουσα αναμονής": "αίθουσα αναμονής — waiting room", "αποβάθρες": "αποβάθρα — platform", "φιλαρμονική": "φιλαρμονική — (brass) band", "δανείσετε": "δανείζω — to lend", "ελεύθερη": "ελεύθερη είσοδος — free admission"}
})

ITEMS.append({
 "id": "l123-vm-synedrio", "title": "Μήνυμα από τη διοργανώτρια ενός συνεδρίου", "title_en": "A message from a conference organiser", "type": "voicemail", "level": "B2",
 "context_el": "Θα μιλήσετε σε ένα επιστημονικό συνέδριο. Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη διοργανώτρια.",
 "script": [
  L("Διοργανώτρια", "f", "Καλησπέρα σας, η Ελένη Μαργαρίτη είμαι, από την οργανωτική επιτροπή του συνεδρίου. Σας τηλεφωνώ γιατί έγινε μια μικρή αλλαγή στο πρόγραμμα: η ομιλία σας μεταφέρεται από την Παρασκευή το πρωί στην Πέμπτη το απόγευμα, στις πέντε, γιατί ένας ομιλητής ακύρωσε.", "Good evening, it's Eleni Margariti, from the conference organising committee. I'm calling because there's been a small change to the programme: your talk is moving from Friday morning to Thursday afternoon, at five, because a speaker has cancelled."),
  L("Διοργανώτρια", "f", "Θα έχετε στη διάθεσή σας είκοσι λεπτά για την ομιλία και δέκα για ερωτήσεις. Σας παρακαλώ να μας στείλετε την παρουσίασή σας μέχρι την Τρίτη, για να τη φορτώσουμε από πριν στον υπολογιστή της αίθουσας και να μη χαθεί χρόνος.", "You will have twenty minutes for your talk and ten for questions. Please send us your presentation by Tuesday, so we can load it in advance onto the room's computer and no time is lost."),
  L("Διοργανώτρια", "f", "Αν η αλλαγή σάς δημιουργεί πρόβλημα με το ξενοδοχείο, μην ανησυχείτε: έχουμε κανονίσει να μείνετε μία νύχτα επιπλέον χωρίς χρέωση. Πείτε μου μόνο αν θα το χρειαστείτε. Ευχαριστώ πολύ!", "If the change causes you a problem with the hotel, don't worry: we have arranged for you to stay one extra night free of charge. Just tell me if you'll need it. Thank you very much!"),
 ],
 "questions": [
  Q("Γιατί μεταφέρεται η ομιλία;", ["Γιατί η αίθουσα δεν είναι διαθέσιμη", "Γιατί ένας ομιλητής ακύρωσε", "Γιατί το συνέδριο τελειώνει νωρίτερα", "Γιατί το ζήτησε ο ακροατής"], 1, "γιατί ένας ομιλητής ακύρωσε"),
  Q("Γιατί πρέπει να σταλεί η παρουσίαση μέχρι την Τρίτη;", ["Για να μεταφραστεί", "Για να τυπωθεί στο πρόγραμμα", "Για να φορτωθεί από πριν στον υπολογιστή της αίθουσας", "Για να την εγκρίνει η επιτροπή"], 2, "για να τη φορτώσουμε από πριν στον υπολογιστή της αίθουσας"),
  Q("Τι έχει κανονίσει η επιτροπή για το ξενοδοχείο;", ["Μία νύχτα επιπλέον χωρίς χρέωση", "Ένα δωμάτιο σε άλλο ξενοδοχείο", "Έκπτωση στο εστιατόριο", "Ταξί από το αεροδρόμιο"], 0, "έχουμε κανονίσει να μείνετε μία νύχτα επιπλέον χωρίς χρέωση"),
 ],
 "gloss": {"συνέδριο": "συνέδριο — conference", "διοργανώτρια": "διοργανώτρια — (female) organiser", "οργανωτική επιτροπή": "οργανωτική επιτροπή — organising committee", "ομιλία": "ομιλία — talk, lecture", "ομιλητής": "ομιλητής — speaker", "ακύρωσε": "ακυρώνω — to cancel", "στη διάθεσή σας": "στη διάθεσή σας — at your disposal", "παρουσίασή": "παρουσίαση — presentation", "φορτώσουμε": "φορτώνω — to load (a file)", "χρέωση": "χρέωση — charge"}
})

ITEMS.append({
 "id": "l123-dial-kolymbi-sta-saranta", "title": "Ποτέ δεν είναι αργά για κολύμπι", "title_en": "It's never too late to swim", "type": "dialogue", "level": "B2",
 "context_el": "Η Βάσω, σαράντα δύο χρονών, λέει στον φίλο της τον Άλκη ότι γράφτηκε σε μαθήματα κολύμβησης.",
 "script": [
  L("Βάσω", "f", "Άλκη, θα γελάσεις, αλλά γράφτηκα σε μαθήματα κολύμβησης για ενήλικες. Μεγάλωσα σε ορεινό χωριό και δεν έμαθα ποτέ. Κάθε καλοκαίρι κάθομαι στην άκρη και βλέπω τους άλλους να βουτάνε.", "Alkis, you'll laugh, but I've signed up for adult swimming lessons. I grew up in a mountain village and never learned. Every summer I sit on the edge and watch the others dive in."),
  L("Άλκης", "m", "Γιατί να γελάσω; Μπράβο σου! Η θεία μου έμαθε στα εξήντα και τώρα κολυμπά κάθε πρωί ως τη σημαδούρα. Πώς είναι τα μαθήματα;", "Why would I laugh? Good for you! My aunt learned at sixty and now she swims to the buoy every morning. What are the lessons like?"),
  L("Βάσω", "f", "Είμαστε οκτώ στην ομάδα, όλοι πάνω από τριάντα πέντε. Το πρώτο μάθημα δεν μπήκαμε καν στο νερό· μιλήσαμε για τον φόβο. Ο προπονητής λέει ότι οι ενήλικες δεν δυσκολεύονται με την τεχνική, αλλά με τον πανικό.", "There are eight of us in the group, all over thirty-five. In the first lesson we didn't even get into the water; we talked about fear. The coach says adults don't struggle with the technique, but with panic."),
  L("Άλκης", "m", "Λογικό. Ξέρεις τι; Αν θέλεις, ερχόμαστε μαζί στην πισίνα την Κυριακή, να κάνεις εξάσκηση εκεί που πατώνεις. Και το καλοκαίρι πάμε στη θάλασσα να με πας εσύ ως τη σημαδούρα!", "Makes sense. You know what? If you like, we can go to the pool together on Sunday, so you can practise where you can touch the bottom. And in the summer we'll go to the sea and you can take me out to the buoy!"),
 ],
 "questions": [
  Q("Γιατί η Βάσω δεν έμαθε ποτέ κολύμπι;", ["Γιατί φοβόταν το νερό από παιδί", "Γιατί μεγάλωσε σε ορεινό χωριό", "Γιατί δεν είχε χρόνο", "Γιατί ήταν άρρωστη"], 1, "Μεγάλωσα σε ορεινό χωριό και δεν έμαθα ποτέ"),
  Q("Με τι δυσκολεύονται οι ενήλικες, σύμφωνα με τον προπονητή;", ["Με την τεχνική", "Με την αναπνοή", "Με τον πανικό", "Με το κρύο νερό"], 2, "οι ενήλικες δεν δυσκολεύονται με την τεχνική, αλλά με τον πανικό"),
  Q("Τι προτείνει ο Άλκης;", ["Να πάνε μαζί στην πισίνα την Κυριακή για εξάσκηση", "Να πάρει ιδιαίτερα μαθήματα", "Να γνωρίσει τη θεία του", "Να αγοράσει μπρατσάκια"], 0, "ερχόμαστε μαζί στην πισίνα την Κυριακή"),
 ],
 "gloss": {"κολύμβησης": "κολύμβηση — swimming", "ενήλικες": "ενήλικας — adult", "βουτάνε": "βουτάω — to dive in", "σημαδούρα": "σημαδούρα — buoy", "προπονητής": "προπονητής — coach", "τεχνική": "τεχνική — technique", "πανικό": "πανικός — panic", "εξάσκηση": "εξάσκηση — practice", "πατώνεις": "πατώνω — to touch the bottom (in water)"}
})

ITEMS.append({
 "id": "l123-int-marionetes", "title": "Μια κατασκευάστρια μαριονετών", "title_en": "A marionette maker", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε μια ραδιοφωνική εκπομπή για την τέχνη. Μιλά μια γυναίκα που φτιάχνει μαριονέτες.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αλεξίου, πώς ξεκινήσατε να φτιάχνετε μαριονέτες;", "Ms Alexiou, how did you start making marionettes?"),
  L("Κατασκευάστρια", "f", "Σπούδαζα σκηνογραφία και σε ένα ταξίδι στην Πράγα είδα μια παράσταση με μαριονέτες. Ενθουσιάστηκα. Έμεινα εκεί έναν χρόνο και δούλεψα σε ένα εργαστήρι, όπου έμαθα να σκαλίζω ξύλο και να δένω τα σχοινιά.", "I was studying stage design and on a trip to Prague I saw a marionette show. I was thrilled. I stayed there a year and worked in a workshop, where I learned to carve wood and tie the strings."),
  L("Δημοσιογράφος", "m", "Πόσο χρόνο θέλει μια μαριονέτα;", "How long does a marionette take?"),
  L("Κατασκευάστρια", "f", "Μια απλή, περίπου δύο εβδομάδες. Το κεφάλι και τα χέρια τα σκαλίζω από φλαμουριά, που είναι μαλακό ξύλο. Το πιο δύσκολο όμως δεν είναι το σκάλισμα αλλά η ισορροπία. Αν τα σχοινιά δεν είναι σωστά δεμένα, η κούκλα περπατά σαν μεθυσμένη.", "A simple one, about two weeks. I carve the head and hands from lime wood, which is a soft wood. But the hardest thing isn't the carving, it's the balance. If the strings aren't tied correctly, the puppet walks as if it's drunk."),
  L("Δημοσιογράφος", "m", "Ποιοι αγοράζουν σήμερα μαριονέτες;", "Who buys marionettes today?"),
  L("Κατασκευάστρια", "f", "Κυρίως θέατρα και συλλέκτες. Τα τελευταία χρόνια όμως κάνω και εργαστήρια για παιδιά. Φτιάχνουν μια απλή κούκλα από χαρτόνι και στο τέλος παίζουν μια μικρή παράσταση. Βλέπω ότι τα παιδιά, που ζουν μέσα στις οθόνες, μαγεύονται ακόμη από ένα κομμάτι ξύλο που κινείται.", "Mainly theatres and collectors. In recent years, though, I also run workshops for children. They make a simple puppet out of cardboard and at the end they put on a little show. I see that children, who live surrounded by screens, are still enchanted by a piece of wood that moves."),
 ],
 "questions": [
  Q("Πού έμαθε να φτιάχνει μαριονέτες;", ["Σε μια σχολή στην Αθήνα", "Σε ένα εργαστήρι στην Πράγα", "Από τον παππού της", "Από βιβλία"], 1, "Έμεινα εκεί έναν χρόνο και δούλεψα σε ένα εργαστήρι"),
  Q("Ποιο είναι το πιο δύσκολο, σύμφωνα με την ίδια;", ["Το σκάλισμα του κεφαλιού", "Το βάψιμο", "Η ισορροπία", "Τα ρούχα της κούκλας"], 2, "Το πιο δύσκολο όμως δεν είναι το σκάλισμα αλλά η ισορροπία"),
  Q("Τι κάνουν τα παιδιά στα εργαστήριά της;", ["Φτιάχνουν μια απλή κούκλα από χαρτόνι και παίζουν μια μικρή παράσταση", "Βλέπουν ταινίες για το κουκλοθέατρο", "Σκαλίζουν ξύλο", "Ράβουν κοστούμια"], 0, "Φτιάχνουν μια απλή κούκλα από χαρτόνι και στο τέλος παίζουν μια μικρή παράσταση"),
 ],
 "gloss": {"μαριονέτες": "μαριονέτα — marionette, string puppet", "σκηνογραφία": "σκηνογραφία — stage design", "Ενθουσιάστηκα": "ενθουσιάζομαι — to be thrilled", "σκαλίζω": "σκαλίζω — to carve", "σχοινιά": "σχοινί — string, rope", "φλαμουριά": "φλαμουριά — lime (linden) tree", "ισορροπία": "ισορροπία — balance", "συλλέκτες": "συλλέκτης — collector", "χαρτόνι": "χαρτόνι — cardboard", "μαγεύονται": "μαγεύομαι — to be enchanted"}
})

ITEMS.append({
 "id": "l123-rep-xanazontanevei-xorio", "title": "Ένα ορεινό χωριό ξαναγεμίζει με κατοίκους", "title_en": "A mountain village fills up again", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στις ειδήσεις για ένα ορεινό χωριό που είχε σχεδόν ερημώσει.",
 "script": [
  L("Ρεπόρτερ", "f", "Πριν από δέκα χρόνια, στο χωριό ζούσαν μόνιμα δεκαπέντε ηλικιωμένοι και το σχολείο είχε κλείσει. Σήμερα οι μόνιμοι κάτοικοι είναι πάνω από εκατό, και φέτος το σχολείο ξανάνοιξε με έντεκα μαθητές.", "Ten years ago, fifteen elderly people lived permanently in the village and the school had closed. Today the permanent residents number over a hundred, and this year the school reopened with eleven pupils."),
  L("Πρόεδρος", "m", "Το κλειδί ήταν το ίντερνετ. Όταν φέραμε γρήγορη σύνδεση, ήρθαν οικογένειες που μπορούν να δουλεύουν από απόσταση. Ο δήμος τούς έδωσε επίσης εγκαταλελειμμένα σπίτια με χαμηλό ενοίκιο, με την υποχρέωση να τα επισκευάσουν.", "The key was the internet. When we brought in a fast connection, families who can work remotely came. The municipality also gave them abandoned houses at a low rent, on condition that they repair them."),
  L("Ρεπόρτερ", "f", "Η επιστροφή δεν είναι πάντα εύκολη. Οι νέοι κάτοικοι παραπονιούνται ότι το πλησιέστερο νοσοκομείο απέχει μιάμιση ώρα και ότι τον χειμώνα ο δρόμος κλείνει συχνά από το χιόνι. Κι όμως, οι περισσότεροι λένε ότι δεν σκέφτονται να γυρίσουν στην πόλη.", "The return isn't always easy. The new residents complain that the nearest hospital is an hour and a half away and that in winter the road often closes because of snow. And yet most say they have no thought of going back to the city."),
 ],
 "questions": [
  Q("Τι συνέβη φέτος στο σχολείο του χωριού;", ["Έκλεισε οριστικά", "Ξανάνοιξε με έντεκα μαθητές", "Έγινε μουσείο", "Ενώθηκε με το σχολείο της πόλης"], 1, "φέτος το σχολείο ξανάνοιξε με έντεκα μαθητές"),
  Q("Ποιο ήταν το κλειδί για την επιστροφή, σύμφωνα με τον πρόεδρο;", ["Ένας καινούργιος δρόμος", "Οι θέσεις εργασίας στο χωριό", "Το ίντερνετ", "Ένα νέο νοσοκομείο"], 2, "Το κλειδί ήταν το ίντερνετ"),
  Q("Για τι παραπονιούνται οι νέοι κάτοικοι;", ["Για την απόσταση από το νοσοκομείο και τον δρόμο που κλείνει από το χιόνι", "Για το υψηλό ενοίκιο", "Για τους παλιούς κατοίκους", "Για τον θόρυβο"], 0, "το πλησιέστερο νοσοκομείο απέχει μιάμιση ώρα"),
 ],
 "gloss": {"ερημώσει": "ερημώνω — to become deserted", "μόνιμα": "μόνιμα — permanently", "ηλικιωμένοι": "ηλικιωμένος — elderly person", "σύνδεση": "σύνδεση — connection", "από απόσταση": "από απόσταση — remotely", "εγκαταλελειμμένα": "εγκαταλελειμμένος — abandoned", "υποχρέωση": "υποχρέωση — obligation", "επισκευάσουν": "επισκευάζω — to repair", "παραπονιούνται": "παραπονιέμαι — to complain", "πλησιέστερο": "πλησιέστερος — nearest", "απέχει": "απέχω — to be (a distance) away"}
})

ITEMS.append({
 "id": "l123-rep-apofagia-kotes", "title": "Τα αποφάγια πάνε στις κότες", "title_en": "Leftovers go to the hens", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε τοπικό ραδιόφωνο για ένα πρόγραμμα ενός δήμου που μοιράζει κότες στους κατοίκους.",
 "script": [
  L("Ρεπόρτερ", "m", "Ένας μικρός δήμος της Κρήτης δοκιμάζει έναν ασυνήθιστο τρόπο για να μειώσει τα σκουπίδια: μοιράζει δωρεάν δύο κότες σε κάθε νοικοκυριό που έχει αυλή. Οι κότες τρώνε τα περισσότερα αποφάγια της κουζίνας, και σε αντάλλαγμα δίνουν αυγά.", "A small municipality in Crete is trying an unusual way to cut rubbish: it is giving two hens free to every household that has a yard. The hens eat most of the kitchen leftovers, and in return they give eggs."),
  L("Κάτοικος", "f", "Στην αρχή δεν ήμουν σίγουρη, γιατί δεν είχα ζώα ποτέ. Τώρα τα παιδιά τρέχουν κάθε πρωί να μαζέψουν τα αυγά. Και ο κάδος μας γεμίζει πολύ πιο αργά, γιατί ό,τι περισσεύει από το τραπέζι πηγαίνει στο κοτέτσι.", "At first I wasn't sure, because I'd never had animals. Now the children run every morning to collect the eggs. And our bin fills up much more slowly, because whatever is left over from the table goes to the henhouse."),
  L("Ρεπόρτερ", "m", "Ο δήμος δίνει στους συμμετέχοντες και ένα μικρό εγχειρίδιο: οι κότες δεν πρέπει να τρώνε αλμυρά φαγητά, κρέας ή μουχλιασμένο ψωμί. Αν το πρόγραμμα πετύχει, θα επεκταθεί του χρόνου και στα γειτονικά χωριά.", "The municipality also gives participants a small handbook: the hens should not eat salty food, meat or mouldy bread. If the programme succeeds, it will be extended to the neighbouring villages next year."),
 ],
 "questions": [
  Q("Τι μοιράζει ο δήμος;", ["Κάδους κομποστοποίησης", "Δύο κότες σε κάθε νοικοκυριό με αυλή", "Σπόρους για λαχανόκηπους", "Σακούλες ανακύκλωσης"], 1, "μοιράζει δωρεάν δύο κότες σε κάθε νοικοκυριό που έχει αυλή"),
  Q("Τι άλλαξε για την κάτοικο που μιλά;", ["Αγοράζει περισσότερο φαγητό", "Τα παιδιά φοβούνται τις κότες", "Ο κάδος της γεμίζει πολύ πιο αργά", "Πουλάει αυγά στη λαϊκή"], 2, "ο κάδος μας γεμίζει πολύ πιο αργά"),
  Q("Τι δεν πρέπει να τρώνε οι κότες, σύμφωνα με το εγχειρίδιο;", ["Αλμυρά φαγητά, κρέας ή μουχλιασμένο ψωμί", "Λαχανικά και φρούτα", "Ρύζι και ζυμαρικά", "Σπόρους"], 0, "οι κότες δεν πρέπει να τρώνε αλμυρά φαγητά, κρέας ή μουχλιασμένο ψωμί"),
 ],
 "gloss": {"αποφάγια": "αποφάγια — leftovers, scraps", "ασυνήθιστο": "ασυνήθιστος — unusual", "νοικοκυριό": "νοικοκυριό — household", "σε αντάλλαγμα": "σε αντάλλαγμα — in return", "περισσεύει": "περισσεύω — to be left over", "κοτέτσι": "κοτέτσι — henhouse", "εγχειρίδιο": "εγχειρίδιο — handbook", "μουχλιασμένο": "μουχλιασμένος — mouldy", "επεκταθεί": "επεκτείνομαι — to be extended"}
})

ITEMS.append({
 "id": "l123-mon-pazl", "title": "Το πάθος μου για τα παζλ", "title_en": "My passion for jigsaw puzzles", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άνδρα να μιλά σε ένα podcast για το χόμπι του.",
 "script": [
  L("Ομιλητής", "m", "Τα παζλ τα ανακάλυψα την εποχή του εγκλεισμού, όταν δεν ήξερα τι να κάνω τα βράδια. Η κόρη μου μού χάρισε ένα παζλ χιλίων κομματιών με ένα λιμάνι της Ύδρας. Μου πήρε τρεις εβδομάδες, αλλά όταν έβαλα το τελευταίο κομμάτι, ένιωσα σαν να είχα ανεβεί σε βουνό.", "I discovered jigsaw puzzles during the lockdown, when I didn't know what to do in the evenings. My daughter gave me a thousand-piece puzzle of a harbour on Hydra. It took me three weeks, but when I put in the last piece, I felt as if I'd climbed a mountain."),
  L("Ομιλητής", "m", "Σήμερα κάνω παζλ των τριών και τεσσάρων χιλιάδων κομματιών. Έχω μάθει και κόλπα: πρώτα ξεχωρίζω τις άκρες, μετά ομαδοποιώ τα κομμάτια ανά χρώμα. Το πιο δύσκολο είναι ο ουρανός, γιατί όλα τα κομμάτια μοιάζουν ίδια.", "Today I do puzzles of three and four thousand pieces. I've learned tricks too: first I pick out the edges, then I group the pieces by colour. The hardest part is the sky, because all the pieces look the same."),
  L("Ομιλητής", "m", "Για μένα το παζλ είναι κάτι σαν διαλογισμός. Για δύο ώρες δεν σκέφτομαι τη δουλειά, τους λογαριασμούς, τίποτα. Και όταν το τελειώσω, δεν το κολλάω· το χαλάω και το χαρίζω σε κάποιον φίλο. Η χαρά είναι στη διαδρομή, όχι στο αποτέλεσμα.", "For me a puzzle is something like meditation. For two hours I don't think about work, bills, anything. And when I finish it, I don't glue it; I break it up and give it to a friend. The joy is in the journey, not in the result."),
 ],
 "questions": [
  Q("Πότε ανακάλυψε τα παζλ ο ομιλητής;", ["Όταν ήταν παιδί", "Την εποχή του εγκλεισμού", "Όταν βγήκε στη σύνταξη", "Σε ένα ταξίδι στην Ύδρα"], 1, "Τα παζλ τα ανακάλυψα την εποχή του εγκλεισμού"),
  Q("Ποιο είναι το πιο δύσκολο κομμάτι ενός παζλ γι' αυτόν;", ["Οι άκρες", "Τα κτίρια", "Ο ουρανός", "Η θάλασσα"], 2, "Το πιο δύσκολο είναι ο ουρανός"),
  Q("Τι κάνει όταν τελειώσει ένα παζλ;", ["Το χαλάει και το χαρίζει σε κάποιον φίλο", "Το κολλάει και το κρεμάει στον τοίχο", "Το πουλάει", "Το φυλάει σε ένα ντουλάπι"], 0, "το χαλάω και το χαρίζω σε κάποιον φίλο"),
 ],
 "gloss": {"παζλ": "παζλ — jigsaw puzzle", "εγκλεισμού": "εγκλεισμός — lockdown", "χάρισε": "χαρίζω — to give (as a gift)", "κομματιών": "κομμάτι — piece", "ξεχωρίζω": "ξεχωρίζω — to pick out, separate", "άκρες": "άκρη — edge", "ομαδοποιώ": "ομαδοποιώ — to group", "διαλογισμός": "διαλογισμός — meditation", "κολλάω": "κολλάω — to glue", "διαδρομή": "διαδρομή — journey, route"}
})

ITEMS.append({
 "id": "l123-mon-vradia-komodias", "title": "Η πρώτη μου βραδιά κωμωδίας", "title_en": "My first comedy night", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια νεαρή γυναίκα να διηγείται σε μια ραδιοφωνική εκπομπή την πρώτη φορά που ανέβηκε στη σκηνή για stand-up κωμωδία.",
 "script": [
  L("Ομιλήτρια", "f", "Δουλεύω λογίστρια, και οι φίλοι μου πάντα έλεγαν ότι είμαι αστεία. Πέρσι δήλωσα συμμετοχή σε μια ανοιχτή βραδιά κωμωδίας σε ένα μπαρ των Εξαρχείων. Είχα πέντε λεπτά. Έγραψα το κείμενό μου για έναν μήνα και το έλεγα στον καθρέφτη κάθε βράδυ.", "I work as an accountant, and my friends always said I'm funny. Last year I signed up for an open comedy night at a bar in Exarchia. I had five minutes. I wrote my material over a month and said it to the mirror every evening."),
  L("Ομιλήτρια", "f", "Όταν ανέβηκα, τα χέρια μου έτρεμαν και ξέχασα το πρώτο αστείο. Για μερικά δευτερόλεπτα επικράτησε απόλυτη σιωπή. Τότε είπα την αλήθεια: «Συγγνώμη, είμαι λογίστρια, συνήθως μετράω, δεν μιλάω». Και ο κόσμος γέλασε.", "When I went up, my hands were shaking and I forgot the first joke. For a few seconds there was total silence. Then I told the truth: 'Sorry, I'm an accountant, I usually count, I don't talk.' And people laughed."),
  L("Ομιλήτρια", "f", "Από εκεί και πέρα όλα κύλησαν καλύτερα. Δεν ήμουν τέλεια, αλλά έμαθα κάτι σημαντικό: το κοινό συγχωρεί τα λάθη, αν είσαι ειλικρινής. Από τότε ανεβαίνω στη σκηνή μία φορά τον μήνα, και κρατάω πάντα ένα χαρτάκι στην τσέπη, για παν ενδεχόμενο.", "From then on everything went better. I wasn't perfect, but I learned something important: the audience forgives mistakes if you're honest. Since then I go on stage once a month, and I always keep a slip of paper in my pocket, just in case."),
 ],
 "questions": [
  Q("Πώς προετοιμάστηκε η ομιλήτρια;", ["Πήρε μαθήματα υποκριτικής", "Έγραψε το κείμενό της για έναν μήνα και το έλεγε στον καθρέφτη", "Το έλεγε στους συναδέλφους της", "Δεν προετοιμάστηκε καθόλου"], 1, "Έγραψα το κείμενό μου για έναν μήνα και το έλεγα στον καθρέφτη κάθε βράδυ"),
  Q("Τι συνέβη όταν ανέβηκε στη σκηνή;", ["Ο κόσμος άρχισε να φεύγει", "Έπεσε το μικρόφωνο", "Ξέχασε το πρώτο αστείο", "Γέλασαν όλοι αμέσως"], 2, "ξέχασα το πρώτο αστείο"),
  Q("Τι έμαθε από την εμπειρία;", ["Ότι το κοινό συγχωρεί τα λάθη, αν είσαι ειλικρινής", "Ότι δεν είναι φτιαγμένη για τη σκηνή", "Ότι πρέπει να μάθει το κείμενο απέξω", "Ότι οι λογιστές δεν είναι αστείοι"], 0, "το κοινό συγχωρεί τα λάθη, αν είσαι ειλικρινής"),
 ],
 "gloss": {"κωμωδίας": "κωμωδία — comedy", "λογίστρια": "λογίστρια — (female) accountant", "δήλωσα συμμετοχή": "δηλώνω συμμετοχή — to sign up", "καθρέφτη": "καθρέφτης — mirror", "έτρεμαν": "τρέμω — to shake, tremble", "επικράτησε": "επικρατώ — to prevail", "σιωπή": "σιωπή — silence", "κύλησαν": "κυλάω — to go (smoothly), roll", "συγχωρεί": "συγχωρώ — to forgive", "ειλικρινής": "ειλικρινής — honest", "για παν ενδεχόμενο": "για παν ενδεχόμενο — just in case"}
})

ITEMS.append({
 "id": "l123-c1-iera-dasi", "title": "Τα ιερά δάση της Ηπείρου", "title_en": "The sacred forests of Epirus", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια δασολόγο να μιλά σε μια εκπομπή για τη σχέση των ανθρώπων με τη φύση στα χωριά της Ηπείρου.",
 "script": [
  L("Δασολόγος", "f", "Σε πολλά χωριά της Ηπείρου, κυρίως στο Ζαγόρι και στην Κόνιτσα, υπάρχουν μικρά δάση που για αιώνες κανείς δεν τολμούσε να κόψει. Ονομάζονται ιερά ή αφιερωμένα δάση, γιατί η κοινότητα τα είχε αφιερώσει σε έναν άγιο, και ο ιερέας είχε απειλήσει με αφορισμό όποιον έκοβε έστω κι ένα κλαδί.", "In many villages of Epirus, mainly in Zagori and Konitsa, there are small forests that for centuries nobody dared to cut. They are called sacred or dedicated forests, because the community had dedicated them to a saint, and the priest had threatened with excommunication anyone who cut even a single branch."),
  L("Δασολόγος", "f", "Πίσω από τη θρησκευτική απαγόρευση κρυβόταν συχνά μια πολύ πρακτική λογική. Τα δάση αυτά βρίσκονταν συνήθως πάνω από το χωριό και το προστάτευαν από κατολισθήσεις και χιονοστιβάδες. Άλλα λειτουργούσαν ως αποθεματικό ξυλείας, που η κοινότητα μπορούσε να χρησιμοποιήσει μόνο σε μεγάλη ανάγκη, για παράδειγμα για να ξαναχτίσει την εκκλησία.", "Behind the religious ban there was often a very practical logic. These forests were usually above the village and protected it from landslides and avalanches. Others served as a timber reserve, which the community could use only in great need, for example to rebuild the church."),
  L("Δασολόγος", "f", "Σήμερα οι επιστήμονες τα μελετούν με μεγάλο ενδιαφέρον. Επειδή έμειναν ανέγγιχτα τόσο πολύ καιρό, έχουν πολύ γέρικα δέντρα και μεγάλη ποικιλία από μύκητες, έντομα και πουλιά. Κατά κάποιον τρόπο, είναι προστατευόμενες περιοχές πολύ πριν εφευρεθεί η έννοια.", "Today scientists study them with great interest. Because they remained untouched for so long, they have very old trees and a great variety of fungi, insects and birds. In a way, they are protected areas from long before the concept was invented."),
  L("Δασολόγος", "f", "Το ερώτημα είναι τι θα γίνει τώρα που τα χωριά αδειάζουν και ο φόβος του αφορισμού δεν πείθει πια κανέναν. Ορισμένες κοινότητες προσπαθούν να τα κατοχυρώσουν θεσμικά. Νομίζω ότι μας θυμίζουν κάτι που ξεχάσαμε: ότι η προστασία της φύσης δεν ξεκίνησε από τα γραφεία, αλλά από τις ίδιες τις τοπικές κοινωνίες.", "The question is what will happen now that the villages are emptying and the fear of excommunication no longer convinces anyone. Some communities are trying to secure them institutionally. I think they remind us of something we forgot: that nature protection didn't start in offices, but in local communities themselves."),
 ],
 "questions": [
  Q("Γιατί κανείς δεν τολμούσε να κόψει τα δάση αυτά;", ["Γιατί ανήκαν σε έναν πλούσιο γαιοκτήμονα", "Γιατί ο ιερέας είχε απειλήσει με αφορισμό όποιον έκοβε κλαδί", "Γιατί τα φύλαγαν στρατιώτες", "Γιατί το ξύλο τους ήταν άχρηστο"], 1, "ο ιερέας είχε απειλήσει με αφορισμό όποιον έκοβε έστω κι ένα κλαδί"),
  Q("Ποια πρακτική λογική κρυβόταν πίσω από την απαγόρευση;", ["Η προστασία του νερού του χωριού", "Η διατήρηση του κυνηγιού", "Η προστασία από κατολισθήσεις και χιονοστιβάδες και ένα αποθεματικό ξυλείας", "Η παραγωγή μελιού"], 2, "το προστάτευαν από κατολισθήσεις και χιονοστιβάδες"),
  Q("Γιατί ενδιαφέρουν σήμερα τους επιστήμονες;", ["Γιατί έχουν πολύ γέρικα δέντρα και μεγάλη ποικιλία ζωής", "Γιατί είναι τα μεγαλύτερα δάση της Ελλάδας", "Γιατί εκεί ζουν αρκούδες", "Γιατί έχουν σπάνια φαρμακευτικά φυτά"], 0, "έχουν πολύ γέρικα δέντρα και μεγάλη ποικιλία από μύκητες, έντομα και πουλιά"),
  Q("Τι μας θυμίζουν τα ιερά δάση, κατά τη δασολόγο;", ["Ότι η θρησκεία είναι πιο δυνατή από τον νόμο", "Ότι τα χωριά πρέπει να ξαναγεμίσουν", "Ότι τα δάση πρέπει να κόβονται με μέτρο", "Ότι η προστασία της φύσης ξεκίνησε από τις τοπικές κοινωνίες"], 3, "η προστασία της φύσης δεν ξεκίνησε από τα γραφεία, αλλά από τις ίδιες τις τοπικές κοινωνίες"),
 ],
 "gloss": {"δασολόγο": "δασολόγος — forester, forest scientist", "τολμούσε": "τολμώ — to dare", "αφιερωμένα": "αφιερωμένος — dedicated", "αφορισμό": "αφορισμός — excommunication", "απαγόρευση": "απαγόρευση — ban", "κατολισθήσεις": "κατολίσθηση — landslide", "χιονοστιβάδες": "χιονοστιβάδα — avalanche", "αποθεματικό": "αποθεματικό — reserve", "ξυλείας": "ξυλεία — timber", "ανέγγιχτα": "ανέγγιχτος — untouched", "γέρικα": "γέρικος — old, aged", "κατοχυρώσουν": "κατοχυρώνω — to secure (legally)", "θεσμικά": "θεσμικά — institutionally"}
})

ITEMS.append({
 "id": "l123-c1-ellines-aigyptou", "title": "Οι Έλληνες της Αιγύπτου", "title_en": "The Greeks of Egypt", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν ιστορικό σε μια εκπομπή για τον ελληνισμό της διασποράς.",
 "script": [
  L("Δημοσιογράφος", "f", "Για πολλούς η Αλεξάνδρεια είναι συνδεδεμένη με τον Καβάφη. Πόσο μεγάλη ήταν όμως η ελληνική παρουσία στην Αίγυπτο;", "For many people Alexandria is linked with Cavafy. But how large was the Greek presence in Egypt?"),
  L("Ιστορικός", "m", "Πολύ μεγάλη. Από τα μέσα του 19ου αιώνα, Έλληνες έμποροι εγκαταστάθηκαν στην Αλεξάνδρεια, στο Κάιρο και σε μικρότερες πόλεις. Στην ακμή της, τον 20ό αιώνα, η παροικία αριθμούσε, σύμφωνα με ορισμένες εκτιμήσεις, πάνω από εκατό χιλιάδες ανθρώπους, με δικά της σχολεία, νοσοκομεία, εφημερίδες και συλλόγους.", "Very large. From the mid-19th century, Greek merchants settled in Alexandria, Cairo and smaller towns. At its peak, in the 20th century, the community numbered, according to some estimates, over a hundred thousand people, with its own schools, hospitals, newspapers and associations."),
  L("Δημοσιογράφος", "f", "Από τι ζούσαν;", "What did they live on?"),
  L("Ιστορικός", "m", "Πολλοί από το βαμβάκι, που ήταν το μεγάλο εξαγωγικό προϊόν της χώρας. Οικογένειες όπως οι Μπενάκη έκαναν τεράστιες περιουσίες. Ένα μέρος αυτού του πλούτου επέστρεψε στην Ελλάδα: ο Γεώργιος Αβέρωφ χρηματοδότησε την αναστήλωση του Παναθηναϊκού Σταδίου για τους Ολυμπιακούς Αγώνες του 1896, και ο Αντώνης Μπενάκης ίδρυσε στην Αθήνα το μουσείο που φέρει το όνομά του.", "Many from cotton, which was the country's great export. Families such as the Benakis made huge fortunes. Part of that wealth returned to Greece: Georgios Averoff financed the restoration of the Panathenaic Stadium for the 1896 Olympic Games, and Antonis Benakis founded in Athens the museum that bears his name."),
  L("Δημοσιογράφος", "f", "Γιατί η παροικία σχεδόν εξαφανίστηκε;", "Why did the community almost disappear?"),
  L("Ιστορικός", "m", "Μετά την επανάσταση του 1952 και κυρίως με τις εθνικοποιήσεις του Νάσερ, από το 1956 και ύστερα, πολλές επιχειρήσεις πέρασαν στο κράτος και οι ξένοι έχασαν τη θέση τους στην οικονομία. Οι περισσότεροι Έλληνες έφυγαν μέσα σε λίγα χρόνια. Πολλοί ένιωσαν ότι έχαναν όχι μια ξένη χώρα, αλλά την πατρίδα τους. Σήμερα μένουν λίγες χιλιάδες, αλλά οι αναμνήσεις τους ζουν στη λογοτεχνία, από τον Καβάφη ως τον Τσίρκα.", "After the 1952 revolution and above all with Nasser's nationalisations, from 1956 onwards, many businesses passed to the state and foreigners lost their place in the economy. Most Greeks left within a few years. Many felt they were losing not a foreign country, but their homeland. Today a few thousand remain, but their memories live on in literature, from Cavafy to Tsirkas."),
 ],
 "questions": [
  Q("Πόσο μεγάλη ήταν η παροικία στην ακμή της, σύμφωνα με ορισμένες εκτιμήσεις;", ["Λίγες χιλιάδες", "Πάνω από εκατό χιλιάδες άνθρωποι", "Ένα εκατομμύριο", "Περίπου δέκα χιλιάδες"], 1, "πάνω από εκατό χιλιάδες ανθρώπους"),
  Q("Από τι ζούσαν πολλοί Έλληνες της Αιγύπτου;", ["Από τον τουρισμό", "Από το ψάρεμα στον Νείλο", "Από το βαμβάκι", "Από τα ορυχεία"], 2, "Πολλοί από το βαμβάκι"),
  Q("Τι χρηματοδότησε ο Γεώργιος Αβέρωφ;", ["Την αναστήλωση του Παναθηναϊκού Σταδίου", "Το Μουσείο Μπενάκη", "Ένα σχολείο στην Αλεξάνδρεια", "Την έκδοση των ποιημάτων του Καβάφη"], 0, "ο Γεώργιος Αβέρωφ χρηματοδότησε την αναστήλωση του Παναθηναϊκού Σταδίου"),
  Q("Γιατί έφυγαν οι περισσότεροι Έλληνες;", ["Λόγω ενός μεγάλου σεισμού", "Γιατί τους κάλεσε πίσω η ελληνική κυβέρνηση", "Λόγω μιας επιδημίας", "Λόγω των εθνικοποιήσεων, που τους στέρησαν τη θέση τους στην οικονομία"], 3, "με τις εθνικοποιήσεις του Νάσερ"),
 ],
 "gloss": {"διασποράς": "διασπορά — diaspora", "παρουσία": "παρουσία — presence", "εγκαταστάθηκαν": "εγκαθίσταμαι — to settle", "ακμή": "ακμή — peak, heyday", "παροικία": "παροικία — (expatriate) community", "αριθμούσε": "αριθμώ — to number", "βαμβάκι": "βαμβάκι — cotton", "εξαγωγικό": "εξαγωγικός — export (adj.)", "περιουσίες": "περιουσία — fortune", "αναστήλωση": "αναστήλωση — restoration", "εθνικοποιήσεις": "εθνικοποίηση — nationalisation", "επιχειρήσεις": "επιχείρηση — business"}
})

rnd = random.Random(123)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-123.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
