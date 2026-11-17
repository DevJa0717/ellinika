# Source for library/listening/listening-122.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l122.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l122-ann-tournoua-skakiou", "title": "Τουρνουά σκακιού στη δημοτική βιβλιοθήκη", "title_en": "A chess tournament at the municipal library", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε στη δημοτική βιβλιοθήκη της πόλης σας. Ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Υπάλληλος", "m", "Αγαπητοί επισκέπτες, σας ενημερώνουμε ότι την Κυριακή 30 Νοεμβρίου η βιβλιοθήκη μας διοργανώνει ανοιχτό τουρνουά σκακιού για όλες τις ηλικίες. Οι αγώνες θα γίνουν στην αίθουσα εκδηλώσεων του πρώτου ορόφου, από τις δέκα το πρωί.", "Dear visitors, we would like to inform you that on Sunday 30 November our library is organising an open chess tournament for all ages. The games will take place in the events room on the first floor, from ten in the morning."),
  L("Υπάλληλος", "m", "Οι συμμετοχές δηλώνονται στο γραφείο δανεισμού μέχρι την Πέμπτη. Η συμμετοχή είναι δωρεάν, αλλά οι θέσεις είναι περιορισμένες, γι' αυτό σας συνιστούμε να δηλώσετε έγκαιρα. Τα παιδιά κάτω των δώδεκα θα παίξουν σε ξεχωριστή κατηγορία.", "Entries are taken at the lending desk until Thursday. Taking part is free, but places are limited, so we recommend you sign up early. Children under twelve will play in a separate category."),
  L("Υπάλληλος", "m", "Όσοι έχετε δική σας σκακιέρα και ρολόι, παρακαλούμε να τα φέρετε μαζί σας. Για όσους δεν ξέρουν ακόμη να παίζουν, ένα μέλος του τοπικού σκακιστικού ομίλου θα κάνει μάθημα για αρχάριους στο αναγνωστήριο, κάθε μισή ώρα.", "Those of you who have your own chessboard and clock, please bring them with you. For those who don't yet know how to play, a member of the local chess club will give a beginners' lesson in the reading room every half hour."),
 ],
 "questions": [
  Q("Πού θα γίνουν οι αγώνες;", ["Στο αναγνωστήριο", "Στην αίθουσα εκδηλώσεων του πρώτου ορόφου", "Στην αυλή της βιβλιοθήκης", "Στα γραφεία του σκακιστικού ομίλου"], 1, "Οι αγώνες θα γίνουν στην αίθουσα εκδηλώσεων του πρώτου ορόφου"),
  Q("Γιατί συνιστούν να δηλώσουν οι ενδιαφερόμενοι έγκαιρα;", ["Γιατί η συμμετοχή κοστίζει ακριβότερα μετά την Πέμπτη", "Γιατί το τουρνουά μπορεί να αναβληθεί", "Γιατί οι θέσεις είναι περιορισμένες", "Γιατί χρειάζεται να αγοράσουν σκακιέρα"], 2, "οι θέσεις είναι περιορισμένες"),
  Q("Τι θα γίνεται για όσους δεν ξέρουν να παίζουν;", ["Μάθημα για αρχάριους στο αναγνωστήριο, κάθε μισή ώρα", "Προβολή ταινίας για το σκάκι", "Δωρεάν βιβλία σκακιού", "Ένας αγώνας επίδειξης στο τέλος"], 0, "θα κάνει μάθημα για αρχάριους στο αναγνωστήριο, κάθε μισή ώρα"),
 ],
 "gloss": {"διοργανώνει": "διοργανώνω — to organise", "τουρνουά": "τουρνουά — tournament", "αίθουσα εκδηλώσεων": "αίθουσα εκδηλώσεων — events room", "συμμετοχές": "συμμετοχή — entry, participation", "γραφείο δανεισμού": "γραφείο δανεισμού — lending desk", "έγκαιρα": "έγκαιρα — in good time", "σκακιέρα": "σκακιέρα — chessboard", "σκακιστικού ομίλου": "σκακιστικός όμιλος — chess club", "αρχάριους": "αρχάριος — beginner", "αναγνωστήριο": "αναγνωστήριο — reading room"}
})

ITEMS.append({
 "id": "l122-vm-ypotitlismos", "title": "Μια δουλειά υποτιτλισμού", "title_en": "A subtitling job", "type": "voicemail", "level": "B2",
 "context_el": "Εργάζεστε ως ελεύθερος επαγγελματίας μεταφραστής. Ακούτε ένα μήνυμα στον τηλεφωνητή σας από ένα γραφείο μεταφράσεων.",
 "script": [
  L("Συντονίστρια", "f", "Καλημέρα, η Αθηνά είμαι από το γραφείο μεταφράσεων. Έχουμε μια καινούργια δουλειά που νομίζω ότι σου ταιριάζει: υπότιτλους για μια γαλλική σειρά ντοκιμαντέρ, έξι επεισόδια των πενήντα λεπτών, για ένα κανάλι που ξεκινά τις προβολές τον Ιανουάριο.", "Good morning, it's Athina from the translation agency. We have a new job that I think suits you: subtitles for a French documentary series, six fifty-minute episodes, for a channel that starts broadcasting in January."),
  L("Συντονίστρια", "f", "Η προθεσμία είναι στενή: το πρώτο επεισόδιο το θέλουν σε δέκα μέρες, για να το ελέγξει ο πελάτης, και τα υπόλοιπα μέχρι τα μέσα Δεκεμβρίου. Το κανάλι έχει δικό του οδηγό ύφους, με κανόνες για το μήκος των γραμμών, και θα σου τον στείλω με email.", "The deadline is tight: they want the first episode in ten days, so the client can check it, and the rest by mid-December. The channel has its own style guide, with rules on line length, and I'll send it to you by email."),
  L("Συντονίστρια", "f", "Η αμοιβή είναι ανά λεπτό προγράμματος, λίγο καλύτερη από την προηγούμενη φορά. Πες μου μέχρι αύριο το μεσημέρι αν τη θέλεις, γιατί αλλιώς πρέπει να ψάξω κάποιον άλλον. Ευχαριστώ!", "The fee is per programme minute, a bit better than last time. Let me know by tomorrow midday if you want it, because otherwise I have to look for someone else. Thanks!"),
 ],
 "questions": [
  Q("Τι είδους δουλειά προτείνει η Αθηνά;", ["Διερμηνεία σε ένα συνέδριο", "Υπότιτλους για μια γαλλική σειρά ντοκιμαντέρ", "Μετάφραση ενός μυθιστορήματος", "Μεταγλώττιση παιδικών ταινιών"], 1, "υπότιτλους για μια γαλλική σειρά ντοκιμαντέρ"),
  Q("Γιατί θέλουν το πρώτο επεισόδιο σε δέκα μέρες;", ["Γιατί θα προβληθεί αμέσως", "Γιατί η Αθηνά φεύγει για διακοπές", "Για να το ελέγξει ο πελάτης", "Για να το δείξουν σε ένα φεστιβάλ"], 2, "για να το ελέγξει ο πελάτης"),
  Q("Μέχρι πότε πρέπει να απαντήσει ο ακροατής;", ["Μέχρι αύριο το μεσημέρι", "Μέχρι το τέλος της εβδομάδας", "Μέχρι τα μέσα Δεκεμβρίου", "Μέχρι τον Ιανουάριο"], 0, "Πες μου μέχρι αύριο το μεσημέρι αν τη θέλεις"),
 ],
 "gloss": {"ελεύθερος επαγγελματίας": "ελεύθερος επαγγελματίας — freelancer", "μεταφραστής": "μεταφραστής — translator", "υπότιτλους": "υπότιτλος — subtitle", "επεισόδια": "επεισόδιο — episode", "προβολές": "προβολή — screening, broadcast", "προθεσμία": "προθεσμία — deadline", "στενή": "στενός — tight, narrow", "οδηγό ύφους": "οδηγός ύφους — style guide", "αμοιβή": "αμοιβή — fee", "ανά λεπτό": "ανά λεπτό — per minute"}
})

ITEMS.append({
 "id": "l122-dial-agroktima", "title": "Σαββατοκύριακο σε ένα αγρόκτημα", "title_en": "A weekend on a farm", "type": "dialogue", "level": "B2",
 "context_el": "Η Ναταλία και ο Πέτρος, γονείς δύο μικρών παιδιών, σχεδιάζουν ένα Σαββατοκύριακο σε έναν αγροτουριστικό ξενώνα.",
 "script": [
  L("Ναταλία", "f", "Πέτρο, βρήκα έναν αγροτουριστικό ξενώνα στην ορεινή Κορινθία. Έχουν κατσίκες, κότες κι ένα μικρό τυροκομείο. Τα παιδιά μπορούν να βοηθήσουν στο άρμεγμα και να μάθουν πώς γίνεται το τυρί.", "Petros, I've found an agritourism guesthouse in the mountains of Corinthia. They have goats, hens and a small cheese dairy. The kids can help with the milking and learn how cheese is made."),
  L("Πέτρος", "m", "Ακούγεται ωραίο, αλλά ο μικρός φοβάται τα ζώα. Θυμάσαι τι έγινε με τον σκύλο της γειτόνισσας; Δεν θέλω να περάσει όλο το Σαββατοκύριακο κλαίγοντας.", "Sounds nice, but the little one is scared of animals. Remember what happened with the neighbour's dog? I don't want him to spend the whole weekend crying."),
  L("Ναταλία", "f", "Το σκέφτηκα. Έχουν κι άλλες δραστηριότητες: μάζεμα κάστανων, ζύμωμα ψωμιού στον ξυλόφουρνο, ακόμη και μάθημα για το πώς φυτεύουμε λαχανικά. Δεν είναι υποχρεωτικό να πλησιάσει τα ζώα.", "I thought about that. They have other activities too: gathering chestnuts, kneading bread for the wood oven, even a lesson on how to plant vegetables. He doesn't have to go near the animals."),
  L("Πέτρος", "m", "Εντάξει, τότε. Μόνο ρώτα αν έχουν θέρμανση στα δωμάτια, γιατί τον Νοέμβριο στα βουνά κάνει κρύο. Κι αν γίνεται, ας πάρουμε δωμάτιο στο ισόγειο, για να μην ανεβοκατεβαίνουμε σκάλες με το καρότσι.", "All right, then. Just ask if they have heating in the rooms, because in November it's cold in the mountains. And if possible, let's take a ground-floor room, so we're not going up and down stairs with the buggy."),
 ],
 "questions": [
  Q("Τι ενθουσιάζει τη Ναταλία στον ξενώνα;", ["Ότι έχει πισίνα", "Ότι τα παιδιά μπορούν να βοηθήσουν στο άρμεγμα και να μάθουν πώς γίνεται το τυρί", "Ότι είναι κοντά στη θάλασσα", "Ότι είναι πολύ φθηνός"], 1, "Τα παιδιά μπορούν να βοηθήσουν στο άρμεγμα και να μάθουν πώς γίνεται το τυρί"),
  Q("Ποια είναι η ανησυχία του Πέτρου;", ["Ότι ο δρόμος είναι επικίνδυνος", "Ότι το φαγητό δεν θα αρέσει στα παιδιά", "Ότι ο μικρός φοβάται τα ζώα", "Ότι θα βρέξει"], 2, "ο μικρός φοβάται τα ζώα"),
  Q("Γιατί θέλει ο Πέτρος δωμάτιο στο ισόγειο;", ["Για να μην ανεβοκατεβαίνουν σκάλες με το καρότσι", "Γιατί έχει καλύτερη θέα", "Γιατί είναι πιο ζεστό", "Γιατί είναι κοντά στο τυροκομείο"], 0, "για να μην ανεβοκατεβαίνουμε σκάλες με το καρότσι"),
 ],
 "gloss": {"αγροτουριστικό": "αγροτουριστικός — agritourism (adj.)", "ξενώνα": "ξενώνας — guesthouse", "τυροκομείο": "τυροκομείο — cheese dairy", "άρμεγμα": "άρμεγμα — milking", "μάζεμα": "μάζεμα — gathering, picking", "ζύμωμα": "ζύμωμα — kneading", "ξυλόφουρνο": "ξυλόφουρνος — wood-fired oven", "υποχρεωτικό": "υποχρεωτικός — compulsory", "θέρμανση": "θέρμανση — heating", "ανεβοκατεβαίνουμε": "ανεβοκατεβαίνω — to go up and down", "καρότσι": "καρότσι — pushchair, buggy"}
})

ITEMS.append({
 "id": "l122-int-varelas", "title": "Βαρέλια φτιαγμένα στο χέρι", "title_en": "Barrels made by hand", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε μια ραδιοφωνική εκπομπή για τα παλιά επαγγέλματα. Μιλά ένας βαρελάς από ένα χωριό της Νεμέας.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Σταύρο, πόσα χρόνια φτιάχνετε βαρέλια;", "Mr Stavros, how many years have you been making barrels?"),
  L("Βαρελάς", "m", "Από δεκατεσσάρων χρονών. Το εργαστήρι το άνοιξε ο παππούς μου, και τότε κάθε οικογένεια στο χωριό είχε το δικό της κρασί και χρειαζόταν βαρέλια. Σήμερα οι πελάτες μου είναι κυρίως μικρά οινοποιεία.", "Since I was fourteen. My grandfather opened the workshop, and back then every family in the village had its own wine and needed barrels. Today my customers are mainly small wineries."),
  L("Δημοσιογράφος", "f", "Ποιο ξύλο χρησιμοποιείτε;", "Which wood do you use?"),
  L("Βαρελάς", "m", "Κυρίως δρυ, γιατί δίνει στο κρασί άρωμα και αντέχει πολλά χρόνια. Παλιότερα έφτιαχναν βαρέλια και από καστανιά, που ήταν φθηνότερη. Το πιο δύσκολο είναι να λυγίσεις τις σανίδες. Τις ζεσταίνουμε πάνω σε φωτιά και τις βρέχουμε, ώσπου να πάρουν το σχήμα τους.", "Mainly oak, because it gives the wine aroma and lasts many years. In the past they also made barrels from chestnut, which was cheaper. The hardest thing is bending the staves. We heat them over a fire and wet them until they take their shape."),
  L("Δημοσιογράφος", "f", "Θα συνεχίσει κάποιος τη δουλειά σας;", "Will someone carry on your work?"),
  L("Βαρελάς", "m", "Ο ανιψιός μου έρχεται κάθε Σάββατο και μαθαίνει. Δεν είναι εύκολο, θέλει χρόνια για να αποκτήσεις το μάτι. Αλλά τελευταία βλέπω ότι οι νέοι οινοποιοί ζητούν ξανά χειροποίητα βαρέλια, κι αυτό μου δίνει ελπίδα.", "My nephew comes every Saturday and learns. It isn't easy, it takes years to develop an eye for it. But lately I see that young winemakers are asking for handmade barrels again, and that gives me hope."),
 ],
 "questions": [
  Q("Ποιοι είναι σήμερα οι πελάτες του βαρελά;", ["Οι οικογένειες του χωριού", "Κυρίως μικρά οινοποιεία", "Ξένοι τουρίστες", "Εστιατόρια της Αθήνας"], 1, "Σήμερα οι πελάτες μου είναι κυρίως μικρά οινοποιεία"),
  Q("Πώς λυγίζουν τις σανίδες;", ["Τις αφήνουν στον ήλιο", "Τις χτυπούν με σφυρί", "Τις ζεσταίνουν πάνω σε φωτιά και τις βρέχουν", "Τις βάζουν σε καλούπι για μήνες"], 2, "Τις ζεσταίνουμε πάνω σε φωτιά και τις βρέχουμε"),
  Q("Τι δίνει ελπίδα στον βαρελά;", ["Ότι οι νέοι οινοποιοί ζητούν ξανά χειροποίητα βαρέλια", "Ότι ο δήμος του έδωσε επιδότηση", "Ότι το ξύλο έγινε φθηνότερο", "Ότι άνοιξε μια σχολή βαρελάδων"], 0, "οι νέοι οινοποιοί ζητούν ξανά χειροποίητα βαρέλια"),
 ],
 "gloss": {"βαρελάς": "βαρελάς — cooper, barrel maker", "εργαστήρι": "εργαστήρι — workshop", "οινοποιεία": "οινοποιείο — winery", "δρυ": "δρυς — oak", "άρωμα": "άρωμα — aroma", "λυγίσεις": "λυγίζω — to bend", "σανίδες": "σανίδα — plank, stave", "ώσπου": "ώσπου — until", "ανιψιός": "ανιψιός — nephew", "αποκτήσεις το μάτι": "αποκτώ το μάτι — to develop an eye (for something)", "χειροποίητα": "χειροποίητος — handmade"}
})

ITEMS.append({
 "id": "l122-rep-mikri-alieia", "title": "Λιγότερα καΐκια στα λιμάνια", "title_en": "Fewer fishing boats in the harbours", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στις ειδήσεις του ραδιοφώνου για την παράκτια αλιεία.",
 "script": [
  L("Ρεπόρτερ", "m", "Στο λιμανάκι της Κάτω Ζάκρου, όπως και σε πολλά νησιά, τα ξύλινα καΐκια λιγοστεύουν χρόνο με τον χρόνο. Οι ψαράδες λένε ότι το ψάρι έχει μειωθεί, ενώ τα καύσιμα και τα δίχτυα έχουν ακριβύνει πολύ.", "In the little harbour of Kato Zakros, as on many islands, the wooden fishing boats are getting fewer year by year. The fishermen say the fish have declined, while fuel and nets have become much more expensive."),
  L("Ψαράς", "m", "Ο πατέρας μου έβγαζε ένα καλάθι γεμάτο κάθε πρωί. Εγώ κάποιες μέρες γυρίζω με δυο τρία ψάρια. Τα παιδιά μου δεν θέλουν να συνεχίσουν, και δεν τους κατηγορώ.", "My father would bring in a full basket every morning. Some days I come back with two or three fish. My children don't want to carry on, and I don't blame them."),
  L("Ρεπόρτερ", "m", "Ορισμένοι ψαράδες βρίσκουν διέξοδο στον αλιευτικό τουρισμό: παίρνουν επισκέπτες μαζί τους στη θάλασσα, τους δείχνουν πώς ρίχνονται τα δίχτυα και στο τέλος μαγειρεύουν μαζί την ψαριά. Οι επιστήμονες, από την πλευρά τους, ζητούν περισσότερες θαλάσσιες προστατευόμενες περιοχές, όπου τα ψάρια θα μπορούν να αναπαράγονται.", "Some fishermen find a way out in fishing tourism: they take visitors out to sea with them, show them how the nets are cast and at the end cook the catch together. Scientists, for their part, are calling for more marine protected areas, where fish will be able to reproduce."),
 ],
 "questions": [
  Q("Ποια προβλήματα αναφέρουν οι ψαράδες;", ["Τους αυστηρούς ελέγχους", "Ότι το ψάρι έχει μειωθεί και τα καύσιμα και τα δίχτυα ακρίβυναν", "Την έλλειψη λιμανιών", "Τον ανταγωνισμό από τα σούπερ μάρκετ"], 1, "το ψάρι έχει μειωθεί, ενώ τα καύσιμα και τα δίχτυα έχουν ακριβύνει πολύ"),
  Q("Τι γίνεται στον αλιευτικό τουρισμό;", ["Οι τουρίστες αγοράζουν ψάρια στο λιμάνι", "Οι ψαράδες νοικιάζουν τα καΐκια τους", "Οι ψαράδες παίρνουν επισκέπτες στη θάλασσα και μαγειρεύουν μαζί την ψαριά", "Οι επισκέπτες ψαρεύουν μόνοι τους"], 2, "παίρνουν επισκέπτες μαζί τους στη θάλασσα"),
  Q("Τι ζητούν οι επιστήμονες;", ["Περισσότερες θαλάσσιες προστατευόμενες περιοχές", "Απαγόρευση του αλιευτικού τουρισμού", "Μεγαλύτερα αλιευτικά σκάφη", "Χαμηλότερη τιμή στα καύσιμα"], 0, "ζητούν περισσότερες θαλάσσιες προστατευόμενες περιοχές"),
 ],
 "gloss": {"παράκτια": "παράκτιος — coastal, inshore", "αλιεία": "αλιεία — fishing, fisheries", "καΐκια": "καΐκι — caique, small fishing boat", "λιγοστεύουν": "λιγοστεύω — to dwindle", "καύσιμα": "καύσιμα — fuel", "δίχτυα": "δίχτυ — net", "διέξοδο": "διέξοδος — way out", "αλιευτικό": "αλιευτικός — fishing (adj.)", "ψαριά": "ψαριά — catch (of fish)", "προστατευόμενες": "προστατευόμενος — protected", "αναπαράγονται": "αναπαράγομαι — to reproduce, breed"}
})

ITEMS.append({
 "id": "l122-rep-perifrourisi-dason", "title": "Εθελοντές φρουροί του δάσους", "title_en": "Volunteer forest watchers", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε τοπικό ραδιόφωνο για μια ομάδα εθελοντών που προστατεύει ένα δάσος από τις πυρκαγιές.",
 "script": [
  L("Ρεπόρτερ", "f", "Κάθε καλοκαίρι, από τον Ιούνιο ως τον Σεπτέμβριο, πενήντα εθελοντές από τα γύρω χωριά περιπολούν στο πευκοδάσος πάνω από την πόλη. Κινούνται σε βάρδιες, μέρα και νύχτα, με δύο αγροτικά οχήματα και έναν μικρό πυροσβεστικό σταθμό που φτιάχτηκε με δωρεές.", "Every summer, from June to September, fifty volunteers from the surrounding villages patrol the pine forest above the town. They work in shifts, day and night, with two pick-up trucks and a small fire station that was built with donations."),
  L("Εθελοντής", "m", "Η δουλειά μας είναι κυρίως να βλέπουμε και να ειδοποιούμε. Αν εντοπίσουμε καπνό, καλούμε αμέσως την Πυροσβεστική και δίνουμε ακριβείς συντεταγμένες. Τα πρώτα δέκα λεπτά μπορούμε να κάνουμε κάτι κι εμείς, με το νερό που κουβαλάμε, μέχρι να έρθουν οι επαγγελματίες.", "Our job is mainly to watch and to alert. If we spot smoke, we immediately call the Fire Service and give exact coordinates. In the first ten minutes we can do something ourselves too, with the water we carry, until the professionals arrive."),
  L("Ρεπόρτερ", "f", "Η ομάδα κάνει και πρόληψη: τον χειμώνα καθαρίζει τα μονοπάτια από τα ξερά κλαδιά και μιλά στα σχολεία. Φέτος, χάρη σε έγκαιρη ειδοποίηση, δύο μικρές φωτιές σβήστηκαν πριν εξαπλωθούν.", "The group also does prevention: in winter it clears the paths of dry branches and talks in schools. This year, thanks to a timely alert, two small fires were put out before they spread."),
 ],
 "questions": [
  Q("Πώς φτιάχτηκε ο μικρός πυροσβεστικός σταθμός;", ["Με χρήματα του κράτους", "Με δωρεές", "Με ένα ευρωπαϊκό πρόγραμμα", "Από την Πυροσβεστική"], 1, "έναν μικρό πυροσβεστικό σταθμό που φτιάχτηκε με δωρεές"),
  Q("Τι κάνουν οι εθελοντές όταν εντοπίσουν καπνό;", ["Προσπαθούν μόνοι τους να σβήσουν τη φωτιά", "Ειδοποιούν τα χωριά να φύγουν", "Καλούν αμέσως την Πυροσβεστική και δίνουν ακριβείς συντεταγμένες", "Ανεβαίνουν σε έναν πύργο παρατήρησης"], 2, "καλούμε αμέσως την Πυροσβεστική και δίνουμε ακριβείς συντεταγμένες"),
  Q("Τι κάνει η ομάδα τον χειμώνα;", ["Καθαρίζει τα μονοπάτια από τα ξερά κλαδιά και μιλά στα σχολεία", "Φυτεύει καινούργια πεύκα", "Δεν έχει καμία δραστηριότητα", "Εκπαιδεύεται στο εξωτερικό"], 0, "τον χειμώνα καθαρίζει τα μονοπάτια από τα ξερά κλαδιά και μιλά στα σχολεία"),
 ],
 "gloss": {"πυρκαγιές": "πυρκαγιά — wildfire", "περιπολούν": "περιπολώ — to patrol", "πευκοδάσος": "πευκοδάσος — pine forest", "βάρδιες": "βάρδια — shift", "δωρεές": "δωρεά — donation", "ειδοποιούμε": "ειδοποιώ — to alert, notify", "εντοπίσουμε": "εντοπίζω — to spot, locate", "συντεταγμένες": "συντεταγμένες — coordinates", "πρόληψη": "πρόληψη — prevention", "εξαπλωθούν": "εξαπλώνομαι — to spread"}
})

ITEMS.append({
 "id": "l122-mon-aristeroheiras", "title": "Μεγαλώνοντας αριστερόχειρας", "title_en": "Growing up left-handed", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλά σε ένα podcast για το πώς ήταν να μεγαλώνει ως αριστερόχειρας.",
 "script": [
  L("Ομιλήτρια", "f", "Γεννήθηκα αριστερόχειρας, όπως περίπου ένας στους δέκα ανθρώπους. Στο δημοτικό, η δασκάλα μου προσπαθούσε να με κάνει να γράφω με το δεξί. Μου έλεγε ότι έτσι είναι «το σωστό». Για έναν χρόνο έγραφα αργά και άσχημα, και ένιωθα ότι κάτι δεν πάει καλά με μένα.", "I was born left-handed, like about one in ten people. At primary school, my teacher tried to make me write with my right hand. She told me that was 'the proper way'. For a year I wrote slowly and badly, and I felt that something was wrong with me."),
  L("Ομιλήτρια", "f", "Η μητέρα μου πήγε στο σχολείο και ζήτησε να με αφήσουν ήσυχη. Από τότε γράφω με το αριστερό και δεν είχα ποτέ ξανά πρόβλημα. Βέβαια, ο κόσμος είναι φτιαγμένος για δεξιόχειρες: τα ψαλίδια, τα ανοιχτήρια, ακόμη και τα θρανία με το μικρό τραπεζάκι στη δεξιά πλευρά.", "My mother went to the school and asked them to leave me alone. Since then I write with my left hand and I've never had a problem again. Of course, the world is made for right-handers: scissors, can openers, even desks with the little writing surface on the right side."),
  L("Ομιλήτρια", "f", "Σήμερα έχω δικό μου ψαλίδι για αριστερόχειρες και γελάω όταν μου λένε ότι γράφω «ανάποδα». Το μόνο που ζητώ είναι κανένα παιδί να μη νιώσει πια ότι το χέρι του είναι λάθος.", "Today I have my own left-handed scissors and I laugh when people tell me I write 'backwards'. All I ask is that no child should ever again feel that their hand is wrong."),
 ],
 "questions": [
  Q("Τι προσπαθούσε να κάνει η δασκάλα της;", ["Να της μάθει να γράφει και με τα δύο χέρια", "Να την κάνει να γράφει με το δεξί", "Να τη βάλει να καθίσει μπροστά", "Να τη στείλει σε ειδικό"], 1, "η δασκάλα μου προσπαθούσε να με κάνει να γράφω με το δεξί"),
  Q("Τι έκανε η μητέρα της;", ["Της αγόρασε ειδικά τετράδια", "Την άλλαξε σχολείο", "Πήγε στο σχολείο και ζήτησε να την αφήσουν ήσυχη", "Της έκανε μαθήματα στο σπίτι"], 2, "Η μητέρα μου πήγε στο σχολείο και ζήτησε να με αφήσουν ήσυχη"),
  Q("Ποια είναι η επιθυμία της ομιλήτριας;", ["Κανένα παιδί να μη νιώσει πια ότι το χέρι του είναι λάθος", "Να φτιαχτούν περισσότερα ψαλίδια για αριστερόχειρες", "Να γράψει ένα βιβλίο για την παιδική της ηλικία", "Να γίνει δασκάλα"], 0, "κανένα παιδί να μη νιώσει πια ότι το χέρι του είναι λάθος"),
 ],
 "gloss": {"αριστερόχειρας": "αριστερόχειρας — left-handed person", "δεξιόχειρες": "δεξιόχειρας — right-handed person", "ψαλίδια": "ψαλίδι — scissors", "ανοιχτήρια": "ανοιχτήρι — opener", "θρανία": "θρανίο — school desk", "ανάποδα": "ανάποδα — backwards, the wrong way round", "ήσυχη": "αφήνω κάποιον ήσυχο — to leave someone alone"}
})

ITEMS.append({
 "id": "l122-mon-imerologio-oneiron", "title": "Το ημερολόγιο των ονείρων μου", "title_en": "My dream diary", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν νεαρό άνδρα να μιλά σε μια ραδιοφωνική εκπομπή για τη συνήθειά του να καταγράφει τα όνειρά του.",
 "script": [
  L("Ομιλητής", "m", "Πριν από δύο χρόνια ένας φίλος μού είπε ότι κρατά ημερολόγιο ονείρων. Στην αρχή γέλασα, γιατί εγώ νόμιζα ότι δεν ονειρεύομαι σχεδόν ποτέ. Δοκίμασα όμως: έβαλα ένα τετράδιο δίπλα στο κρεβάτι και κάθε πρωί έγραφα ό,τι θυμόμουν, πριν καν σηκωθώ.", "Two years ago a friend told me he keeps a dream diary. At first I laughed, because I thought I almost never dream. But I tried: I put a notebook next to the bed and every morning I wrote down whatever I remembered, before I even got up."),
  L("Ομιλητής", "m", "Τις πρώτες μέρες έγραφα μόνο μια δυο λέξεις. Μετά από μερικές εβδομάδες όμως θυμόμουν ολόκληρες ιστορίες, με πρόσωπα, χρώματα και διαλόγους. Φαίνεται ότι όσο περισσότερο προσέχεις τα όνειρά σου, τόσο περισσότερα θυμάσαι.", "In the first days I only wrote a word or two. After a few weeks, though, I was remembering whole stories, with faces, colours and dialogue. It seems that the more attention you pay to your dreams, the more you remember."),
  L("Ομιλητής", "m", "Δεν πιστεύω ότι τα όνειρα προβλέπουν το μέλλον. Όταν όμως ξαναδιαβάζω το τετράδιο, καταλαβαίνω τι με απασχολούσε κάθε περίοδο: τις εξετάσεις, έναν χωρισμό, τη μετακόμιση. Είναι σαν ένα δεύτερο ημερολόγιο της ζωής μου, γραμμένο από κάποιον άλλο.", "I don't believe dreams predict the future. But when I reread the notebook, I understand what was on my mind in each period: the exams, a break-up, the move. It's like a second diary of my life, written by someone else."),
 ],
 "questions": [
  Q("Γιατί γέλασε στην αρχή ο ομιλητής;", ["Γιατί ο φίλος του έλεγε αστεία όνειρα", "Γιατί νόμιζε ότι δεν ονειρεύεται σχεδόν ποτέ", "Γιατί δεν του αρέσει να γράφει", "Γιατί πίστευε ότι τα όνειρα είναι προλήψεις"], 1, "εγώ νόμιζα ότι δεν ονειρεύομαι σχεδόν ποτέ"),
  Q("Τι διαπίστωσε μετά από μερικές εβδομάδες;", ["Ότι ονειρευόταν πάντα το ίδιο πράγμα", "Ότι κοιμόταν καλύτερα", "Ότι θυμόταν ολόκληρες ιστορίες, με πρόσωπα, χρώματα και διαλόγους", "Ότι τα όνειρά του έγιναν εφιάλτες"], 2, "θυμόμουν ολόκληρες ιστορίες, με πρόσωπα, χρώματα και διαλόγους"),
  Q("Τι του δείχνει το τετράδιο όταν το ξαναδιαβάζει;", ["Τι τον απασχολούσε κάθε περίοδο", "Τι θα συμβεί στο μέλλον", "Ποια όνειρα είναι κοινά σε όλους", "Πόσες ώρες κοιμόταν"], 0, "καταλαβαίνω τι με απασχολούσε κάθε περίοδο"),
 ],
 "gloss": {"καταγράφει": "καταγράφω — to record, write down", "ημερολόγιο": "ημερολόγιο — diary", "ονειρεύομαι": "ονειρεύομαι — to dream", "τετράδιο": "τετράδιο — notebook", "προσέχεις": "προσέχω — to pay attention", "προβλέπουν": "προβλέπω — to predict", "απασχολούσε": "απασχολώ — to occupy (someone's mind)", "χωρισμό": "χωρισμός — break-up, separation", "μετακόμιση": "μετακόμιση — move (house)"}
})

ITEMS.append({
 "id": "l122-c1-loxygkas", "title": "Ο λόξυγκας, ένα αινιγματικό αντανακλαστικό", "title_en": "Hiccups, a puzzling reflex", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια γιατρό να μιλά σε μια εκπομπή εκλαΐκευσης της επιστήμης για τον λόξυγκα.",
 "script": [
  L("Γιατρός", "f", "Ο λόξυγκας είναι μια ακούσια, απότομη σύσπαση του διαφράγματος, του μυός που χωρίζει τον θώρακα από την κοιλιά. Μόλις ο αέρας αρχίσει να μπαίνει ορμητικά στους πνεύμονες, η γλωττίδα κλείνει σχεδόν αμέσως, και από αυτό το απότομο κλείσιμο βγαίνει ο χαρακτηριστικός ήχος.", "Hiccups are an involuntary, sudden contraction of the diaphragm, the muscle that separates the chest from the abdomen. As soon as air starts rushing into the lungs, the glottis closes almost immediately, and that sudden closure produces the characteristic sound."),
  L("Γιατρός", "f", "Συνήθως τον προκαλούν πράγματα καθημερινά: ένα γεύμα που φάγαμε βιαστικά, τα ανθρακούχα ποτά, μια ξαφνική αλλαγή θερμοκρασίας. Στις περισσότερες περιπτώσεις σταματά μόνος του σε λίγα λεπτά. Αν όμως διαρκεί περισσότερο από δύο μέρες, καλό είναι να εξεταστεί κανείς από γιατρό, γιατί μπορεί να κρύβει κάποιο άλλο πρόβλημα.", "It is usually caused by everyday things: a meal eaten in a hurry, fizzy drinks, a sudden change in temperature. In most cases it stops by itself within a few minutes. But if it lasts more than two days, it is wise to be examined by a doctor, because it may be hiding some other problem."),
  L("Γιατρός", "f", "Το πιο αινιγματικό είναι γιατί υπάρχει. Ο λόξυγκας δεν φαίνεται να έχει κάποια χρησιμότητα στους ενήλικες. Ξέρουμε όμως ότι τα έμβρυα έχουν λόξυγκα μέσα στη μήτρα, πολύ πριν αρχίσουν να αναπνέουν. Μια υπόθεση είναι ότι πρόκειται για κατάλοιπο της εξέλιξης, από την εποχή που οι πρόγονοί μας ανέπνεαν στο νερό. Μια άλλη υποστηρίζει ότι βοηθά τα βρέφη να βγάζουν τον αέρα που καταπίνουν όταν θηλάζουν. Καμία δεν έχει αποδειχθεί.", "The most puzzling thing is why it exists. Hiccups don't seem to have any use in adults. We know, however, that foetuses hiccup in the womb, long before they start breathing. One hypothesis is that it is a remnant of evolution, from the time when our ancestors breathed in water. Another holds that it helps babies get rid of the air they swallow while feeding. Neither has been proven."),
  L("Γιατρός", "f", "Όσο για τα γνωστά κόλπα, να κρατήσουμε την αναπνοή μας, να πιούμε νερό ανάποδα ή να μας τρομάξει κάποιος, η επιστημονική τεκμηρίωση είναι ελάχιστη. Ίσως δουλεύουν απλώς επειδή, μέχρι να τα δοκιμάσουμε, ο λόξυγκας έχει ήδη περάσει μόνος του.", "As for the well-known tricks, holding our breath, drinking water upside down or having someone scare us, the scientific evidence is minimal. Perhaps they work simply because, by the time we try them, the hiccups have already passed on their own."),
 ],
 "questions": [
  Q("Από πού προέρχεται ο χαρακτηριστικός ήχος του λόξυγκα;", ["Από τη σύσπαση του στομάχου", "Από το απότομο κλείσιμο της γλωττίδας", "Από τον αέρα που βγαίνει από τη μύτη", "Από τους παλμούς της καρδιάς"], 1, "από αυτό το απότομο κλείσιμο βγαίνει ο χαρακτηριστικός ήχος"),
  Q("Πότε συνιστά η γιατρός να εξεταστεί κανείς;", ["Αν ο λόξυγκας εμφανιστεί μετά το φαγητό", "Αν ο λόξυγκας είναι πολύ δυνατός", "Αν διαρκεί περισσότερο από δύο μέρες", "Αν τον έχει ένα παιδί"], 2, "Αν όμως διαρκεί περισσότερο από δύο μέρες, καλό είναι να εξεταστεί κανείς από γιατρό"),
  Q("Τι γνωρίζουμε για τον λόξυγκα στα έμβρυα;", ["Ότι τον έχουν μέσα στη μήτρα, πολύ πριν αρχίσουν να αναπνέουν", "Ότι δεν τον έχουν ποτέ", "Ότι είναι σημάδι προβλήματος", "Ότι σταματά τον τρίτο μήνα"], 0, "τα έμβρυα έχουν λόξυγκα μέσα στη μήτρα, πολύ πριν αρχίσουν να αναπνέουν"),
  Q("Τι λέει η γιατρός για τα γνωστά κόλπα κατά του λόξυγκα;", ["Ότι είναι επικίνδυνα", "Ότι δουλεύουν μόνο στα παιδιά", "Ότι έχουν αποδειχθεί επιστημονικά", "Ότι η επιστημονική τεκμηρίωση είναι ελάχιστη"], 3, "η επιστημονική τεκμηρίωση είναι ελάχιστη"),
 ],
 "gloss": {"λόξυγκα": "λόξυγκας — hiccups", "εκλαΐκευσης": "εκλαΐκευση — popularisation", "ακούσια": "ακούσιος — involuntary", "σύσπαση": "σύσπαση — contraction", "διαφράγματος": "διάφραγμα — diaphragm", "θώρακα": "θώρακας — chest, thorax", "γλωττίδα": "γλωττίδα — glottis", "ανθρακούχα": "ανθρακούχος — fizzy, carbonated", "έμβρυα": "έμβρυο — foetus, embryo", "μήτρα": "μήτρα — womb", "κατάλοιπο": "κατάλοιπο — remnant", "θηλάζουν": "θηλάζω — to breastfeed, suckle", "τεκμηρίωση": "τεκμηρίωση — evidence, documentation"}
})

ITEMS.append({
 "id": "l122-c1-exodos-mesolongiou", "title": "Η Έξοδος του Μεσολογγίου", "title_en": "The Exodus of Missolonghi", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια ιστορικό σε μια εκπομπή για την Ελληνική Επανάσταση.",
 "script": [
  L("Δημοσιογράφος", "m", "Το Μεσολόγγι έχει μια ξεχωριστή θέση στη μνήμη της Επανάστασης. Γιατί ήταν τόσο σημαντικό;", "Missolonghi has a special place in the memory of the Revolution. Why was it so important?"),
  L("Ιστορικός", "f", "Ήταν το σημαντικότερο οχυρό των επαναστατών στη δυτική Ελλάδα. Είχε ήδη αποκρούσει μια πολιορκία στα τέλη του 1822, και εκεί πέθανε ο λόρδος Βύρων το 1824, κάτι που έκανε την πόλη γνωστή σε όλη την Ευρώπη. Η τελευταία πολιορκία άρχισε την άνοιξη του 1825 και κράτησε περίπου έναν χρόνο.", "It was the most important stronghold of the revolutionaries in western Greece. It had already repelled a siege in 1822, and Lord Byron died there in 1824, which made the town known throughout Europe. The last siege began in the spring of 1825 and lasted about a year."),
  L("Δημοσιογράφος", "m", "Τι οδήγησε στην απόφαση για την Έξοδο;", "What led to the decision for the Exodus?"),
  L("Ιστορικός", "f", "Η πείνα. Όταν στα οθωμανικά στρατεύματα προστέθηκε ο αιγυπτιακός στρατός του Ιμπραήμ, η πόλη αποκλείστηκε εντελώς και από τη θάλασσα. Οι πολιορκημένοι έτρωγαν πια ποντίκια και φύκια. Τη νύχτα της 10ης Απριλίου του 1826, με το παλιό ημερολόγιο, επιχείρησαν να διασπάσουν τις γραμμές του εχθρού, μαζί με γυναίκες και παιδιά.", "Hunger. When Ibrahim's Egyptian army was added to the Ottoman forces, the town was completely cut off from the sea as well. The besieged were by then eating rats and seaweed. On the night of 10 April 1826, by the old calendar, they attempted to break through the enemy lines, together with women and children."),
  L("Δημοσιογράφος", "m", "Πόσοι σώθηκαν;", "How many were saved?"),
  L("Ιστορικός", "f", "Οι αριθμοί διαφέρουν από πηγή σε πηγή, αλλά όλοι συμφωνούν ότι μόνο ένα μικρό μέρος κατάφερε να φτάσει σε ασφαλές μέρος. Στρατιωτικά ήταν ήττα. Ηθικά όμως η Έξοδος συγκλόνισε την Ευρώπη. Ο Ντελακρουά ζωγράφισε την Ελλάδα πάνω στα ερείπια του Μεσολογγίου, και το φιλελληνικό κίνημα δυνάμωσε. Λέγεται συχνά ότι το Μεσολόγγι κέρδισε, χάνοντας, τη συμπάθεια που αργότερα οδήγησε στην επέμβαση των Δυνάμεων.", "The numbers differ from source to source, but all agree that only a small part managed to reach safety. Militarily it was a defeat. Morally, however, the Exodus shook Europe. Delacroix painted Greece on the ruins of Missolonghi, and the philhellenic movement grew stronger. It is often said that Missolonghi, by losing, won the sympathy that later led to the intervention of the Powers."),
 ],
 "questions": [
  Q("Τι έκανε το Μεσολόγγι γνωστό σε όλη την Ευρώπη, σύμφωνα με την ιστορικό;", ["Η πρώτη πολιορκία του 1822", "Ο θάνατος του λόρδου Βύρωνα εκεί το 1824", "Η ναυμαχία του Ναβαρίνου", "Το εμπόριο του λιμανιού του"], 1, "εκεί πέθανε ο λόρδος Βύρων το 1824, κάτι που έκανε την πόλη γνωστή σε όλη την Ευρώπη"),
  Q("Γιατί αποφασίστηκε η Έξοδος;", ["Γιατί έφτασε ελληνικός στόλος", "Γιατί οι Οθωμανοί πρότειναν συνθηκολόγηση", "Λόγω της πείνας, όταν η πόλη αποκλείστηκε εντελώς", "Γιατί ξέσπασε επιδημία"], 2, "Η πείνα"),
  Q("Τι λέει η ιστορικός για τον αριθμό όσων σώθηκαν;", ["Ότι οι αριθμοί διαφέρουν, αλλά σώθηκε μόνο ένα μικρό μέρος", "Ότι σώθηκαν σχεδόν όλοι", "Ότι δεν σώθηκε κανείς", "Ότι σώθηκαν μόνο οι στρατιώτες"], 0, "Οι αριθμοί διαφέρουν από πηγή σε πηγή"),
  Q("Ποια ήταν, κατά την ιστορικό, η σημασία της Εξόδου;", ["Ήταν μια μεγάλη στρατιωτική νίκη", "Οδήγησε στο τέλος της Επανάστασης", "Δεν είχε καμία απήχηση στο εξωτερικό", "Ήταν ήττα, αλλά κέρδισε τη συμπάθεια της Ευρώπης"], 3, "Ηθικά όμως η Έξοδος συγκλόνισε την Ευρώπη"),
 ],
 "gloss": {"Επανάστασης": "Επανάσταση — (Greek) Revolution (1821)", "οχυρό": "οχυρό — stronghold", "αποκρούσει": "αποκρούω — to repel", "πολιορκία": "πολιορκία — siege", "στρατεύματα": "στράτευμα — troops", "αποκλείστηκε": "αποκλείομαι — to be cut off, blockaded", "πολιορκημένοι": "πολιορκημένος — besieged", "φύκια": "φύκι — seaweed", "διασπάσουν": "διασπώ — to break through", "συγκλόνισε": "συγκλονίζω — to shake, move deeply", "ερείπια": "ερείπιο — ruin", "φιλελληνικό": "φιλελληνικός — philhellenic", "επέμβαση": "επέμβαση — intervention"}
})

rnd = random.Random(122)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-122.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
