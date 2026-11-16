# Source for library/listening/listening-49.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l49.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l49-ann-parastasi", "title": "Καθυστέρηση της παράστασης", "title_en": "The performance is delayed", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα ανοιχτό θέατρο ένα καλοκαιρινό βράδυ. Θα ακούσετε μια ανακοίνωση πριν από την έναρξη της παράστασης.",
 "script": [
  L("Ανακοίνωση", "f", "Αγαπητοί θεατές, καλησπέρα σας. Λόγω της βροχής που έπεσε το απόγευμα, η σκηνή είναι ακόμα βρεγμένη και οι τεχνικοί μας χρειάζονται λίγο χρόνο για να τη στεγνώσουν. Η παράσταση θα αρχίσει με καθυστέρηση περίπου μισής ώρας, στις δέκα αντί για τις εννιάμισι.", "Dear audience, good evening. Because of the rain that fell this afternoon, the stage is still wet and our technicians need a little time to dry it. The performance will start about half an hour late, at ten instead of half past nine."),
  L("Ανακοίνωση", "f", "Σύμφωνα με την πρόγνωση, ο καιρός δεν θα χαλάσει ξανά απόψε. Αν, παρ' όλα αυτά, η παράσταση διακοπεί πριν από το διάλειμμα, τα εισιτήρια θα ισχύουν για την επαναληπτική παράσταση της Πέμπτης. Αν διακοπεί μετά το διάλειμμα, δυστυχώς δεν θα γίνει επιστροφή χρημάτων.", "According to the forecast, the weather will not turn bad again tonight. If, however, the performance is interrupted before the interval, tickets will be valid for the repeat performance on Thursday. If it is interrupted after the interval, unfortunately there will be no refund."),
  L("Ανακοίνωση", "f", "Στο μεταξύ, το κυλικείο μας προσφέρει δωρεάν νερό σε όλους τους θεατές. Όσοι κάθονται στις πρώτες σειρές μπορούν να πάρουν μαξιλαράκια από την είσοδο, γιατί τα σκαλιά είναι ακόμα υγρά. Σας ευχαριστούμε για την κατανόηση.", "Meanwhile, our snack bar is offering free water to all members of the audience. Those sitting in the front rows can take cushions from the entrance, because the steps are still damp. Thank you for your understanding."),
 ],
 "questions": [
  Q("Γιατί θα καθυστερήσει η παράσταση;", ["Επειδή αρρώστησε ένας ηθοποιός", "Επειδή η σκηνή είναι ακόμα βρεγμένη", "Επειδή χάλασαν τα φώτα", "Επειδή αργούν οι θεατές"], 1, "η σκηνή είναι ακόμα βρεγμένη και οι τεχνικοί μας χρειάζονται λίγο χρόνο"),
  Q("Τι θα γίνει αν η παράσταση διακοπεί πριν από το διάλειμμα;", ["Θα επιστραφούν τα χρήματα", "Τα εισιτήρια θα ισχύουν για την παράσταση της Πέμπτης", "Η παράσταση θα συνεχιστεί σε κλειστό χώρο", "Οι θεατές θα πάρουν δωρεάν νερό"], 1, "τα εισιτήρια θα ισχύουν για την επαναληπτική παράσταση της Πέμπτης"),
  Q("Γιατί μπορούν να πάρουν μαξιλαράκια όσοι κάθονται μπροστά;", ["Επειδή κάνει κρύο", "Επειδή τα σκαλιά είναι ακόμα υγρά", "Επειδή η παράσταση είναι μεγάλη", "Επειδή είναι δώρο του θεάτρου"], 1, "γιατί τα σκαλιά είναι ακόμα υγρά"),
 ],
 "gloss": {"θεατές": "θεατής — spectator, member of the audience", "βρεγμένη": "βρεγμένος — wet", "να τη στεγνώσουν": "στεγνώνω — to dry", "πρόγνωση": "πρόγνωση — forecast", "δεν θα χαλάσει": "χαλάει ο καιρός — the weather turns bad", "διακοπεί": "διακόπτομαι — to be interrupted", "διάλειμμα": "διάλειμμα — interval, break", "επαναληπτική παράσταση": "επαναληπτική παράσταση — repeat performance", "κυλικείο": "κυλικείο — snack bar, canteen", "μαξιλαράκια": "μαξιλαράκι — small cushion", "σκαλιά": "σκαλί — step", "υγρά": "υγρός — damp, wet", "κατανόηση": "κατανόηση — understanding"},
})

ITEMS.append({
 "id": "l49-vm-gyalia", "title": "Τα καινούργια γυαλιά", "title_en": "The new glasses", "type": "voicemail", "level": "B2",
 "context_el": "Πριν από μια εβδομάδα παραγγείλατε γυαλιά οράσεως από ένα κατάστημα οπτικών. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Οπτικός", "f", "Καλημέρα σας, κύριε Παπαδάκη, από το κατάστημα οπτικών «Ίρις» σας τηλεφωνώ. Τα γυαλιά σας είναι έτοιμα, αλλά υπάρχει ένα μικρό θέμα. Ο σκελετός που διαλέξατε, ο καφέ, δεν υπήρχε πια στο χρώμα αυτό, και η εταιρεία μάς έστειλε τον ίδιο σε σκούρο μπλε.", "Good morning, Mr Papadakis, I'm calling from the Iris optician's. Your glasses are ready, but there's a small issue. The frame you chose, the brown one, was no longer available in that colour, and the company sent us the same one in dark blue."),
  L("Οπτικός", "f", "Οι φακοί είναι ακριβώς αυτοί που έγραψε ο γιατρός σας, με την αντιανακλαστική επίστρωση. Αν σας αρέσει το μπλε, μπορείτε να περάσετε να τα πάρετε από σήμερα. Αν προτιμάτε να περιμένετε τον καφέ σκελετό, θα έρθει σε περίπου τρεις εβδομάδες, και τότε θα πρέπει να ξαναφτιάξουμε τους φακούς.", "The lenses are exactly the ones your doctor prescribed, with the anti-reflective coating. If you like the blue, you can come and pick them up from today. If you'd rather wait for the brown frame, it will arrive in about three weeks, and then we'll have to make the lenses again."),
  L("Οπτικός", "f", "Για την ταλαιπωρία, θα σας κάνουμε έκπτωση δέκα τοις εκατό σε όποια λύση διαλέξετε. Θυμίζω ότι είμαστε ανοιχτά μέχρι τις εννιά το βράδυ, εκτός από Τετάρτη και Σάββατο, που κλείνουμε στις τρεις. Ευχαριστώ, καλή σας μέρα.", "For the trouble, we'll give you a ten per cent discount on whichever option you choose. Just a reminder that we're open until nine in the evening, except Wednesday and Saturday, when we close at three. Thank you, have a nice day."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με τα γυαλιά;", ["Οι φακοί είναι λάθος", "Ο σκελετός ήρθε σε άλλο χρώμα", "Τα γυαλιά έσπασαν", "Η τιμή άλλαξε"], 1, "η εταιρεία μάς έστειλε τον ίδιο σε σκούρο μπλε"),
  Q("Τι θα συμβεί αν ο κύριος Παπαδάκης προτιμήσει τον καφέ σκελετό;", ["Θα πληρώσει περισσότερα", "Θα περιμένει περίπου τρεις εβδομάδες", "Θα πρέπει να ξαναπάει στον γιατρό", "Θα τον πάρει αύριο"], 1, "θα έρθει σε περίπου τρεις εβδομάδες"),
  Q("Πότε κλείνει το κατάστημα στις τρεις;", ["Δευτέρα και Πέμπτη", "Τετάρτη και Σάββατο", "Μόνο Σάββατο", "Κάθε μέρα"], 1, "εκτός από Τετάρτη και Σάββατο, που κλείνουμε στις τρεις"),
 ],
 "gloss": {"γυαλιά οράσεως": "γυαλιά οράσεως — prescription glasses", "οπτικών": "κατάστημα οπτικών — optician's", "σκελετός": "σκελετός — frame (of glasses); skeleton", "φακοί": "φακός — lens", "αντιανακλαστική επίστρωση": "αντιανακλαστική επίστρωση — anti-reflective coating", "να ξαναφτιάξουμε": "ξαναφτιάχνω — to make again", "ταλαιπωρία": "ταλαιπωρία — trouble, inconvenience", "έκπτωση": "έκπτωση — discount"},
})

ITEMS.append({
 "id": "l49-dia-glastres", "title": "Οι γλάστρες της γειτόνισσας", "title_en": "The neighbour's plant pots", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε δύο γειτόνισσες σε μια πολυκατοικία. Η μία φεύγει για διακοπές και ζητάει μια χάρη από την άλλη.",
 "script": [
  L("Κατερίνα", "f", "Κυρία Βούλα, μπορώ να σας ζητήσω μια χάρη; Φεύγω αύριο για δέκα μέρες στην Κρήτη, και ανησυχώ για τις γλάστρες μου στο μπαλκόνι. Με αυτή τη ζέστη, αν δεν τις ποτίζει κανείς, θα ξεραθούν.", "Mrs Voula, may I ask you a favour? I'm leaving tomorrow for ten days in Crete, and I'm worried about my plant pots on the balcony. In this heat, if nobody waters them, they'll dry out."),
  L("Βούλα", "f", "Ευχαρίστως, παιδί μου. Κι εγώ το ίδιο κάνω για τα λουλούδια μου, τα ποτίζω κάθε βράδυ. Πόσο συχνά θέλουν νερό τα δικά σου;", "Gladly, dear. I do the same for my flowers, I water them every evening. How often do yours need water?"),
  L("Κατερίνα", "f", "Τα περισσότερα μέρα παρά μέρα, κατά προτίμηση το βράδυ, όταν έχει πέσει ο ήλιος. Μόνο οι κάκτοι στη γωνία δεν θέλουν σχεδόν καθόλου, μια φορά την εβδομάδα φτάνει. Και ο βασιλικός θέλει κάθε μέρα, γιατί είναι στο πιο ζεστό σημείο.", "Most of them every other day, preferably in the evening, once the sun has gone down. Only the cacti in the corner hardly need any; once a week is enough. And the basil needs it every day, because it's in the hottest spot."),
  L("Βούλα", "f", "Εντάξει, θα τα γράψω για να μην τα μπερδέψω. Άφησέ μου ένα κλειδί, και να μου στείλεις καμιά φωτογραφία από την Κρήτη. Και μη μου φέρεις τίποτα, ακούς; Μια χαρά είναι να έχεις καλούς γείτονες.", "All right, I'll write it down so I don't mix them up. Leave me a key, and send me a photo or two from Crete. And don't bring me anything, you hear? It's a joy to have good neighbours."),
 ],
 "questions": [
  Q("Γιατί ανησυχεί η Κατερίνα;", ["Επειδή χάθηκαν τα κλειδιά της", "Επειδή οι γλάστρες της θα ξεραθούν χωρίς νερό", "Επειδή δεν έχει βρει εισιτήρια", "Επειδή η κυρία Βούλα φεύγει κι εκείνη"], 1, "αν δεν τις ποτίζει κανείς, θα ξεραθούν"),
  Q("Ποιο φυτό χρειάζεται νερό κάθε μέρα;", ["Οι κάκτοι", "Ο βασιλικός", "Όλα τα φυτά", "Κανένα"], 1, "ο βασιλικός θέλει κάθε μέρα, γιατί είναι στο πιο ζεστό σημείο"),
  Q("Τι ζητάει η κυρία Βούλα από την Κατερίνα;", ["Ένα δώρο από την Κρήτη", "Ένα κλειδί και καμιά φωτογραφία", "Να ποτίσει κι εκείνη τα δικά της λουλούδια", "Χρήματα για το νερό"], 1, "Άφησέ μου ένα κλειδί, και να μου στείλεις καμιά φωτογραφία"),
 ],
 "gloss": {"γειτόνισσες": "γειτόνισσα — (female) neighbour", "χάρη": "χάρη — favour", "γλάστρες": "γλάστρα — flowerpot", "ποτίζει": "ποτίζω — to water", "θα ξεραθούν": "ξεραίνομαι — to dry out, wither", "Ευχαρίστως": "ευχαρίστως — gladly", "μέρα παρά μέρα": "μέρα παρά μέρα — every other day", "κατά προτίμηση": "κατά προτίμηση — preferably", "κάκτοι": "κάκτος — cactus", "βασιλικός": "βασιλικός — basil", "να μην τα μπερδέψω": "μπερδεύω — to mix up"},
})

ITEMS.append({
 "id": "l49-dia-katadysi", "title": "Μαθήματα κατάδυσης", "title_en": "Diving lessons", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια τουρίστρια να ρωτάει σε μια σχολή καταδύσεων σε ένα νησί για τα μαθήματα για αρχάριους.",
 "script": [
  L("Ελπίδα", "f", "Γεια σας. Θα ήθελα να κάνω μια δοκιμαστική κατάδυση, αλλά δεν έχω κάνει ποτέ ξανά. Είναι εύκολο για κάποιον που απλώς ξέρει να κολυμπάει;", "Hello. I'd like to do a trial dive, but I've never done one before. Is it easy for someone who can just swim?"),
  L("Εκπαιδευτής", "m", "Βεβαίως. Η δοκιμαστική κατάδυση είναι ακριβώς για αρχάριους. Πρώτα κάνουμε μισή ώρα θεωρία στη σχολή, μετά μια μικρή εξάσκηση στα ρηχά, και στο τέλος κατεβαίνουμε μέχρι έξι μέτρα. Εγώ θα είμαι συνέχεια δίπλα σας. Πρέπει μόνο να συμπληρώσετε ένα ιατρικό ερωτηματολόγιο.", "Certainly. The trial dive is exactly for beginners. First we do half an hour of theory at the school, then a little practice in the shallows, and finally we go down to six metres. I'll be beside you the whole time. You just need to fill in a medical questionnaire."),
  L("Ελπίδα", "f", "Ιατρικό ερωτηματολόγιο; Έχω λίγο άσθμα, αλλά είναι ελαφρύ. Είναι πρόβλημα αυτό;", "A medical questionnaire? I have a little asthma, but it's mild. Is that a problem?"),
  L("Εκπαιδευτής", "m", "Σε αυτή την περίπτωση, χρειαζόμαστε μια βεβαίωση από γιατρό ότι μπορείτε να καταδυθείτε. Υπάρχει ένα ιατρείο στο λιμάνι που την εκδίδει την ίδια μέρα. Επίσης, να ξέρετε ότι δεν πρέπει να πετάξετε με αεροπλάνο για είκοσι τέσσερις ώρες μετά την κατάδυση. Πότε φεύγετε;", "In that case we need a certificate from a doctor saying you can dive. There's a surgery at the harbour that issues it the same day. Also, you should know that you mustn't fly for twenty-four hours after the dive. When are you leaving?"),
  L("Ελπίδα", "f", "Την Κυριακή το πρωί, με το πλοίο. Άρα δεν υπάρχει πρόβλημα. Θα περάσω από τον γιατρό αύριο και θα κλείσω για την Παρασκευή.", "On Sunday morning, by boat. So there's no problem. I'll go to the doctor tomorrow and book for Friday."),
 ],
 "questions": [
  Q("Μέχρι ποιο βάθος κατεβαίνουν στη δοκιμαστική κατάδυση;", ["Μέχρι δύο μέτρα", "Μέχρι έξι μέτρα", "Μέχρι δώδεκα μέτρα", "Μέχρι είκοσι μέτρα"], 1, "στο τέλος κατεβαίνουμε μέχρι έξι μέτρα"),
  Q("Τι χρειάζεται η Ελπίδα λόγω του άσθματός της;", ["Ειδικό εξοπλισμό", "Βεβαίωση από γιατρό", "Να κάνει μάθημα μόνη της", "Να μην κάνει θεωρία"], 1, "χρειαζόμαστε μια βεβαίωση από γιατρό ότι μπορείτε να καταδυθείτε"),
  Q("Γιατί δεν έχει πρόβλημα με την αναχώρησή της;", ["Επειδή μένει άλλη μια εβδομάδα", "Επειδή θα φύγει με πλοίο και όχι με αεροπλάνο", "Επειδή η κατάδυση είναι σύντομη", "Επειδή ο εκπαιδευτής θα τη συνοδεύσει"], 1, "Την Κυριακή το πρωί, με το πλοίο. Άρα δεν υπάρχει πρόβλημα"),
 ],
 "gloss": {"σχολή καταδύσεων": "σχολή καταδύσεων — diving school", "αρχάριους": "αρχάριος — beginner", "δοκιμαστική κατάδυση": "δοκιμαστική κατάδυση — trial dive", "εξάσκηση": "εξάσκηση — practice", "ρηχά": "τα ρηχά — the shallows", "ερωτηματολόγιο": "ερωτηματολόγιο — questionnaire", "άσθμα": "άσθμα — asthma", "ελαφρύ": "ελαφρύς — mild, light", "βεβαίωση": "βεβαίωση — certificate, written confirmation", "να καταδυθείτε": "καταδύομαι — to dive", "εκδίδει": "εκδίδω — to issue"},
})

ITEMS.append({
 "id": "l49-int-agiografos", "title": "Η αγιογράφος", "title_en": "The icon painter", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια νέα αγιογράφο που ζει και δουλεύει στη Θεσσαλονίκη.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Χατζή, πώς αποφασίσατε να γίνετε αγιογράφος; Δεν είναι συνηθισμένο επάγγελμα για μια γυναίκα τριάντα χρονών.", "Ms Chatzi, how did you decide to become an icon painter? It's not a usual profession for a thirty-year-old woman."),
  L("Δανάη", "f", "Σπούδασα γραφιστική και δούλευα σε μια διαφημιστική εταιρεία. Ένα καλοκαίρι πήγα σε ένα σεμινάριο αγιογραφίας στο Άγιον Όρος... όχι μέσα, βέβαια, σε μια σχολή έξω από αυτό. Ενθουσιάστηκα με την τεχνική. Μετά από δύο χρόνια μαθητείας δίπλα σε έναν παλιό αγιογράφο, άνοιξα το δικό μου εργαστήριο.", "I studied graphic design and worked at an advertising agency. One summer I went to an icon-painting seminar near Mount Athos... not inside, of course, at a school outside it. I was thrilled by the technique. After two years of apprenticeship with an old icon painter, I opened my own workshop."),
  L("Δημοσιογράφος", "m", "Τι κάνει τη βυζαντινή αγιογραφία τόσο ιδιαίτερη;", "What makes Byzantine icon painting so special?"),
  L("Δανάη", "f", "Είναι μια τέχνη με πολύ αυστηρούς κανόνες. Χρησιμοποιούμε φυσικά χρώματα, που τα αναμειγνύουμε με κρόκο αυγού, και φύλλα χρυσού για το φόντο. Μια εικόνα μπορεί να μου πάρει από δύο εβδομάδες μέχρι δύο μήνες. Η μεγαλύτερη πρόκληση δεν είναι να είσαι πρωτότυπος, αλλά να μένεις πιστός στην παράδοση και ταυτόχρονα να δίνεις ζωή στο πρόσωπο.", "It's an art with very strict rules. We use natural pigments, which we mix with egg yolk, and gold leaf for the background. An icon can take me anything from two weeks to two months. The biggest challenge isn't being original, but staying faithful to tradition while giving life to the face."),
  L("Δημοσιογράφος", "m", "Ποιοι είναι οι πελάτες σας;", "Who are your clients?"),
  L("Δανάη", "f", "Κυρίως εκκλησίες και ιδιώτες, αλλά τελευταία έχω πολλές παραγγελίες από το εξωτερικό, από Έλληνες της διασποράς. Κάνω επίσης μαθήματα τα Σάββατα, και οι περισσότεροι μαθητές μου, παραδόξως, είναι νέοι κάτω των τριάντα.", "Mainly churches and private individuals, but lately I have a lot of orders from abroad, from Greeks of the diaspora. I also teach classes on Saturdays, and most of my students, surprisingly, are young people under thirty."),
 ],
 "questions": [
  Q("Τι δουλειά έκανε πριν η Δανάη;", ["Ήταν δασκάλα ζωγραφικής", "Δούλευε σε διαφημιστική εταιρεία", "Ήταν συντηρήτρια σε μουσείο", "Δούλευε σε εκκλησία"], 1, "Σπούδασα γραφιστική και δούλευα σε μια διαφημιστική εταιρεία"),
  Q("Με τι αναμειγνύονται τα χρώματα;", ["Με λάδι", "Με κρόκο αυγού", "Με νερό και αλάτι", "Με κερί"], 1, "Χρησιμοποιούμε φυσικά χρώματα, που τα αναμειγνύουμε με κρόκο αυγού"),
  Q("Τι λέει για τους μαθητές της;", ["Είναι κυρίως συνταξιούχοι", "Οι περισσότεροι είναι νέοι κάτω των τριάντα", "Είναι όλοι ξένοι", "Είναι κυρίως ιερείς"], 1, "οι περισσότεροι μαθητές μου, παραδόξως, είναι νέοι κάτω των τριάντα"),
 ],
 "gloss": {"αγιογράφο": "αγιογράφος — icon painter", "αγιογράφος": "αγιογράφος — icon painter", "γραφιστική": "γραφιστική — graphic design", "διαφημιστική εταιρεία": "διαφημιστική εταιρεία — advertising agency", "αγιογραφίας": "αγιογραφία — icon painting", "Ενθουσιάστηκα": "ενθουσιάζομαι — to be thrilled", "μαθητείας": "μαθητεία — apprenticeship", "εργαστήριο": "εργαστήριο — workshop", "αναμειγνύουμε": "αναμειγνύω — to mix", "κρόκο αυγού": "κρόκος αυγού — egg yolk", "φύλλα χρυσού": "φύλλο χρυσού — gold leaf", "φόντο": "φόντο — background", "πρόκληση": "πρόκληση — challenge", "πιστός": "πιστός — faithful", "διασποράς": "διασπορά — diaspora", "παραδόξως": "παραδόξως — surprisingly, paradoxically"},
})

ITEMS.append({
 "id": "l49-rep-pantopoleio", "title": "Το παντοπωλείο του χωριού ξανανοίγει", "title_en": "The village shop reopens", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από ένα ραδιοφωνικό δελτίο ειδήσεων για ένα ορεινό χωριό της Αρκαδίας.",
 "script": [
  L("Ρεπόρτερ", "f", "Για πέντε χρόνια, οι διακόσιοι κάτοικοι ενός ορεινού χωριού της Αρκαδίας έπρεπε να οδηγούν σαράντα λεπτά για να αγοράσουν ψωμί και γάλα. Το μοναδικό παντοπωλείο είχε κλείσει όταν ο ιδιοκτήτης του βγήκε στη σύνταξη, και κανείς δεν ήθελε να το αναλάβει.", "For five years, the two hundred residents of a mountain village in Arcadia had to drive forty minutes to buy bread and milk. The only grocery shop had closed when its owner retired, and nobody wanted to take it over."),
  L("Ρεπόρτερ", "f", "Φέτος, όμως, οι κάτοικοι βρήκαν τη λύση μόνοι τους. Ίδρυσαν έναν συνεταιρισμό: εκατόν είκοσι οικογένειες έβαλαν από πενήντα ευρώ η καθεμία, και με τα χρήματα αυτά ανακαίνισαν το παλιό μαγαζί. Το προσωπικό είναι εθελοντές, κυρίως συνταξιούχοι, που δουλεύουν με βάρδιες τρεις ώρες την εβδομάδα.", "This year, however, the residents found the solution themselves. They founded a cooperative: a hundred and twenty families put in fifty euros each, and with this money they renovated the old shop. The staff are volunteers, mostly pensioners, who work shifts of three hours a week."),
  L("Ρεπόρτερ", "f", "Το παντοπωλείο πουλάει κυρίως τοπικά προϊόντα, όπως τυρί, μέλι και χόρτα από τους παραγωγούς της περιοχής. Τα κέρδη δεν μοιράζονται, αλλά επενδύονται σε έργα για το χωριό. Το επόμενο σχέδιο είναι να ανοίξει, δίπλα στο μαγαζί, ένα μικρό καφενείο για τους τουρίστες που περνούν το καλοκαίρι.", "The shop sells mainly local products, such as cheese, honey and greens from the area's producers. The profits are not shared out but invested in projects for the village. The next plan is to open a small café next to the shop for the tourists who pass through in summer."),
 ],
 "questions": [
  Q("Γιατί είχε κλείσει το παντοπωλείο;", ["Επειδή δεν είχε πελάτες", "Επειδή ο ιδιοκτήτης βγήκε στη σύνταξη", "Επειδή καταστράφηκε από φωτιά", "Επειδή ήταν πολύ ακριβό"], 1, "είχε κλείσει όταν ο ιδιοκτήτης του βγήκε στη σύνταξη"),
  Q("Ποιοι δουλεύουν στο παντοπωλείο;", ["Ένας νέος ιδιοκτήτης", "Εθελοντές, κυρίως συνταξιούχοι", "Φοιτητές το καλοκαίρι", "Υπάλληλοι του δήμου"], 1, "Το προσωπικό είναι εθελοντές, κυρίως συνταξιούχοι"),
  Q("Τι γίνεται με τα κέρδη;", ["Μοιράζονται στις οικογένειες", "Επενδύονται σε έργα για το χωριό", "Δίνονται στους παραγωγούς", "Πάνε στον δήμο"], 1, "Τα κέρδη δεν μοιράζονται, αλλά επενδύονται σε έργα για το χωριό"),
 ],
 "gloss": {"παντοπωλείο": "παντοπωλείο — grocery shop", "να το αναλάβει": "αναλαμβάνω — to take over, take on", "Ίδρυσαν": "ιδρύω — to found", "συνεταιρισμό": "συνεταιρισμός — cooperative", "ανακαίνισαν": "ανακαινίζω — to renovate", "εθελοντές": "εθελοντής — volunteer", "βάρδιες": "βάρδια — shift", "χόρτα": "χόρτα — (wild) greens", "παραγωγούς": "παραγωγός — producer", "κέρδη": "κέρδος — profit", "επενδύονται": "επενδύομαι — to be invested"},
})

ITEMS.append({
 "id": "l49-dia-psarema", "title": "Ψάρεμα με τον παππού", "title_en": "Fishing with Grandpa", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν παππού και τον εγγονό του να κανονίζουν μια πρωινή έξοδο για ψάρεμα με τη βάρκα.",
 "script": [
  L("Παππούς", "m", "Λοιπόν, Αλέξη, αύριο θα σε πάρω μαζί μου για ψάρεμα. Αλλά να ξέρεις, ξεκινάμε στις πέντε και μισή, πριν βγει ο ήλιος. Τα ψάρια τρώνε νωρίς το πρωί.", "Right then, Alexis, tomorrow I'll take you fishing with me. But you should know, we set off at half past five, before the sun comes up. Fish feed early in the morning."),
  L("Αλέξης", "m", "Στις πέντε και μισή; Παππού, είναι καλοκαίρι, έχω διακοπές! Δεν μπορούμε να πάμε στις οχτώ;", "At half past five? Grandpa, it's summer, I'm on holiday! Can't we go at eight?"),
  L("Παππούς", "m", "Στις οχτώ φυσάει ο μαΐστρος και η θάλασσα αγριεύει. Με μια μικρή βάρκα σαν τη δική μου, δεν είναι ασφαλές. Θα γυρίσουμε μέχρι τις δέκα, και μετά κοιμάσαι όσο θέλεις. Θα σου μάθω και πώς να βάζεις το δόλωμα στο αγκίστρι.", "At eight the mistral blows and the sea gets rough. With a small boat like mine, it's not safe. We'll be back by ten, and then you can sleep as much as you like. I'll also teach you how to put the bait on the hook."),
  L("Αλέξης", "m", "Καλά, εντάξει. Να πάρω κάτι μαζί μου;", "Fine, okay. Should I bring anything?"),
  L("Παππούς", "m", "Ένα καπέλο και αντηλιακό, γιατί στη θάλασσα καίγεσαι χωρίς να το καταλάβεις. Και το σωσίβιο το φοράς από τη στιγμή που μπαίνεις στη βάρκα, χωρίς συζήτηση. Κολατσιό θα ετοιμάσει η γιαγιά σου.", "A hat and sunscreen, because at sea you get burnt without realising. And you wear the life jacket from the moment you get into the boat, no discussion. Your grandmother will prepare a snack."),
 ],
 "questions": [
  Q("Γιατί δεν μπορούν να ξεκινήσουν στις οχτώ;", ["Επειδή ο παππούς έχει δουλειά", "Επειδή φυσάει ο μαΐστρος και η θάλασσα αγριεύει", "Επειδή τα ψάρια φεύγουν", "Επειδή η βάρκα χρειάζεται επισκευή"], 1, "Στις οχτώ φυσάει ο μαΐστρος και η θάλασσα αγριεύει"),
  Q("Τι θα μάθει ο Αλέξης από τον παππού;", ["Να οδηγεί τη βάρκα", "Να βάζει το δόλωμα στο αγκίστρι", "Να καθαρίζει τα ψάρια", "Να κολυμπάει"], 1, "Θα σου μάθω και πώς να βάζεις το δόλωμα στο αγκίστρι"),
  Q("Ποιος είναι ο κανόνας του παππού για το σωσίβιο;", ["Το φοράει μόνο αν έχει κύμα", "Το φοράει από τη στιγμή που μπαίνει στη βάρκα", "Το έχει δίπλα του στη βάρκα", "Δεν χρειάζεται"], 1, "το σωσίβιο το φοράς από τη στιγμή που μπαίνεις στη βάρκα"),
 ],
 "gloss": {"ψάρεμα": "ψάρεμα — fishing", "βάρκα": "βάρκα — small boat", "μαΐστρος": "μαΐστρος — mistral (north-west wind)", "αγριεύει": "αγριεύω — to get rough (of the sea)", "δόλωμα": "δόλωμα — bait", "αγκίστρι": "αγκίστρι — fish hook", "αντηλιακό": "αντηλιακό — sunscreen", "καίγεσαι": "καίγομαι — to get burnt", "σωσίβιο": "σωσίβιο — life jacket", "Κολατσιό": "κολατσιό — snack, mid-morning bite"},
})

ITEMS.append({
 "id": "l49-mono-manitaria", "title": "Βόλτα για μανιτάρια", "title_en": "A mushroom walk", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια οδηγό να δίνει οδηγίες σε μια ομάδα πριν από μια φθινοπωρινή βόλτα για μανιτάρια σε ένα δάσος των Γρεβενών.",
 "script": [
  L("Οδηγός", "f", "Καλώς ήρθατε όλοι. Πριν μπούμε στο δάσος, μερικοί σημαντικοί κανόνες. Ο πρώτος και πιο σημαντικός: κανείς δεν τρώει μανιτάρι που δεν το έχω δει εγώ. Στην Ελλάδα υπάρχουν πάνω από δύο χιλιάδες είδη, και μερικά από τα πιο δηλητηριώδη μοιάζουν πολύ με τα φαγώσιμα.", "Welcome, everyone. Before we go into the forest, a few important rules. The first and most important: nobody eats a mushroom I haven't seen. In Greece there are over two thousand species, and some of the most poisonous look very like the edible ones."),
  L("Οδηγός", "f", "Δεύτερον, τα μανιτάρια δεν τα ξεριζώνουμε. Τα κόβουμε προσεκτικά με το μαχαιράκι που σας έδωσα, ώστε να μείνει το υπόγειο μέρος και να ξαναβγούν του χρόνου. Και τα βάζουμε στο καλάθι, όχι σε πλαστική σακούλα, γιατί εκεί ιδρώνουν και χαλάνε γρήγορα.", "Second, we don't pull mushrooms up by the roots. We cut them carefully with the little knife I gave you, so that the underground part stays and they come up again next year. And we put them in the basket, not in a plastic bag, because there they sweat and spoil quickly."),
  L("Οδηγός", "f", "Θα περπατήσουμε περίπου τρεις ώρες, με ένα διάλειμμα στο ξωκλήσι. Μείνετε κοντά στην ομάδα, γιατί στο δάσος χάνεται κανείς εύκολα και δεν έχει σήμα το κινητό. Στο τέλος θα μαγειρέψουμε μαζί όσα μαζέψουμε, στο σπίτι του χωριού, με λίγο λάδι και θυμάρι.", "We'll walk for about three hours, with a break at the little chapel. Stay close to the group, because it's easy to get lost in the forest and there's no mobile signal. At the end we'll cook together whatever we gather, at the village house, with a little oil and thyme."),
 ],
 "questions": [
  Q("Ποιος είναι ο πιο σημαντικός κανόνας;", ["Να μη μαζέψουν πάνω από ένα κιλό", "Να μη φάνε κανένα μανιτάρι που δεν έχει δει η οδηγός", "Να μην περπατούν μόνοι τους", "Να μην κόβουν κλαδιά"], 1, "κανείς δεν τρώει μανιτάρι που δεν το έχω δει εγώ"),
  Q("Γιατί δεν βάζουν τα μανιτάρια σε πλαστική σακούλα;", ["Επειδή απαγορεύεται στο δάσος", "Επειδή ιδρώνουν και χαλάνε γρήγορα", "Επειδή σπάνε", "Επειδή χάνουν τη μυρωδιά τους"], 1, "εκεί ιδρώνουν και χαλάνε γρήγορα"),
  Q("Γιατί πρέπει να μείνουν κοντά στην ομάδα;", ["Επειδή υπάρχουν άγρια ζώα", "Επειδή χάνεται κανείς εύκολα και δεν έχει σήμα", "Επειδή θα βραδιάσει", "Επειδή η οδηγός θα μιλάει συνέχεια"], 1, "στο δάσος χάνεται κανείς εύκολα και δεν έχει σήμα το κινητό"),
 ],
 "gloss": {"δάσος": "δάσος — forest", "είδη": "είδος — species, kind", "δηλητηριώδη": "δηλητηριώδης — poisonous", "φαγώσιμα": "φαγώσιμος — edible", "ξεριζώνουμε": "ξεριζώνω — to uproot", "υπόγειο": "υπόγειος — underground", "ιδρώνουν": "ιδρώνω — to sweat", "χαλάνε": "χαλάω — to spoil, go off", "ξωκλήσι": "ξωκλήσι — country chapel", "σήμα": "σήμα — signal", "θυμάρι": "θυμάρι — thyme"},
})

ITEMS.append({
 "id": "l49-c1-panellinies", "title": "Πανελλήνιες: ένα σύστημα υπό συζήτηση", "title_en": "The national university entrance exams under debate", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συζήτηση με μια εκπαιδευτικό για το σύστημα εισαγωγής στα ελληνικά πανεπιστήμια.",
 "script": [
  L("Δημοσιογράφος", "m", "Κάθε Ιούνιο, δεκάδες χιλιάδες μαθητές δίνουν Πανελλήνιες εξετάσεις. Κυρία Λαμπροπούλου, γιατί το σύστημα αυτό προκαλεί τόσες αντιδράσεις, ενώ ταυτόχρονα κανείς δεν τολμά να το καταργήσει;", "Every June, tens of thousands of pupils sit the national exams. Ms Lambropoulou, why does this system provoke so many reactions, while at the same time nobody dares abolish it?"),
  L("Εκπαιδευτικός", "f", "Γιατί έχει ένα ισχυρό πλεονέκτημα: θεωρείται αδιάβλητο. Τα γραπτά είναι ανώνυμα, βαθμολογούνται από δύο διαφορετικούς βαθμολογητές, και ο γιος του υπουργού κρίνεται με τον ίδιο τρόπο όπως το παιδί του αγρότη. Σε μια χώρα με χαμηλή εμπιστοσύνη στους θεσμούς, αυτό δεν είναι λίγο.", "Because it has one strong advantage: it is considered incorruptible. The scripts are anonymous, they are marked by two different examiners, and the minister's son is judged in the same way as the farmer's child. In a country with low trust in institutions, that's no small thing."),
  L("Δημοσιογράφος", "m", "Και τα μειονεκτήματα;", "And the disadvantages?"),
  L("Εκπαιδευτικός", "f", "Το κόστος, πρώτα απ' όλα. Η αξιοκρατία είναι, σε μεγάλο βαθμό, φαινομενική, αφού οι περισσότερες οικογένειες πληρώνουν φροντιστήρια για δύο ή τρία χρόνια. Ένα παιδί από φτωχή οικογένεια σε ένα απομακρυσμένο χωριό δεν ξεκινά από την ίδια αφετηρία. Έπειτα, η τελευταία τάξη του λυκείου έχει ουσιαστικά μετατραπεί σε προετοιμασία για τις εξετάσεις. Ό,τι δεν εξετάζεται, απλώς παραμελείται.", "Cost, first of all. The meritocracy is, to a large extent, only apparent, since most families pay for cramming schools for two or three years. A child from a poor family in a remote village doesn't start from the same starting point. Then, the final year of upper secondary school has essentially turned into exam preparation. Whatever isn't examined is simply neglected."),
  L("Δημοσιογράφος", "m", "Υπάρχει εναλλακτική;", "Is there an alternative?"),
  L("Εκπαιδευτικός", "f", "Οι προτάσεις δεν λείπουν: να μετράει ο βαθμός του απολυτηρίου, να γίνεται εθνικό απολυτήριο σε όλες τις τάξεις του λυκείου, να επιλέγουν τα ίδια τα πανεπιστήμια. Το πρόβλημα είναι ότι κάθε τέτοια πρόταση προσκρούει στον φόβο της αναξιοκρατίας. Πιστεύω ότι η αλλαγή θα έρθει μόνο σταδιακά, και μόνο αν πρώτα ενισχυθεί το δημόσιο σχολείο, ώστε να μην είναι το φροντιστήριο ο πραγματικός δάσκαλος.", "There's no shortage of proposals: count the school-leaving grade, introduce a national certificate across all years of upper secondary, let the universities choose for themselves. The problem is that every such proposal runs up against the fear of favouritism. I believe change will only come gradually, and only if the state school is strengthened first, so that the cramming school isn't the real teacher."),
 ],
 "questions": [
  Q("Ποιο είναι, κατά την εκπαιδευτικό, το μεγάλο πλεονέκτημα των Πανελληνίων;", ["Ότι είναι εύκολες", "Ότι θεωρούνται αδιάβλητες", "Ότι κοστίζουν λίγο στο κράτος", "Ότι εξετάζουν όλα τα μαθήματα"], 1, "Γιατί έχει ένα ισχυρό πλεονέκτημα: θεωρείται αδιάβλητο"),
  Q("Γιατί λέει ότι η αξιοκρατία είναι «φαινομενική»;", ["Επειδή οι βαθμολογητές κάνουν λάθη", "Επειδή οι περισσότερες οικογένειες πληρώνουν φροντιστήρια", "Επειδή τα θέματα διαρρέουν", "Επειδή τα πανεπιστήμια δεν δέχονται όλους"], 1, "αφού οι περισσότερες οικογένειες πληρώνουν φροντιστήρια για δύο ή τρία χρόνια"),
  Q("Τι έχει συμβεί, κατά την ίδια, στην τελευταία τάξη του λυκείου;", ["Έχει καταργηθεί", "Έχει μετατραπεί σε προετοιμασία για τις εξετάσεις", "Έχει γίνει πιο εύκολη", "Έχει αποκτήσει περισσότερα μαθήματα"], 1, "η τελευταία τάξη του λυκείου έχει ουσιαστικά μετατραπεί σε προετοιμασία για τις εξετάσεις"),
  Q("Υπό ποια προϋπόθεση πιστεύει ότι μπορεί να έρθει η αλλαγή;", ["Αν καταργηθούν αμέσως οι εξετάσεις", "Αν πρώτα ενισχυθεί το δημόσιο σχολείο", "Αν τα φροντιστήρια γίνουν δωρεάν", "Αν αποφασίσουν οι μαθητές"], 1, "μόνο αν πρώτα ενισχυθεί το δημόσιο σχολείο"),
 ],
 "gloss": {"εισαγωγής": "εισαγωγή — admission, entry", "προκαλεί": "προκαλώ — to provoke, cause", "να το καταργήσει": "καταργώ — to abolish", "πλεονέκτημα": "πλεονέκτημα — advantage", "αδιάβλητο": "αδιάβλητος — incorruptible, above suspicion", "γραπτά": "γραπτό — exam script", "βαθμολογητές": "βαθμολογητής — examiner, marker", "θεσμούς": "θεσμός — institution", "αξιοκρατία": "αξιοκρατία — meritocracy", "φαινομενική": "φαινομενικός — apparent, seeming", "φροντιστήρια": "φροντιστήριο — cramming school, private tutoring school", "αφετηρία": "αφετηρία — starting point", "παραμελείται": "παραμελούμαι — to be neglected", "απολυτηρίου": "απολυτήριο — school-leaving certificate", "προσκρούει": "προσκρούω σε — to run up against", "αναξιοκρατίας": "αναξιοκρατία — favouritism, lack of meritocracy", "σταδιακά": "σταδιακά — gradually"},
})

ITEMS.append({
 "id": "l49-c1-theofilos", "title": "Θεόφιλος, ο ζωγράφος των πανηγυριών", "title_en": "Theophilos, the painter of village fairs", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη σε ένα μουσείο για τον λαϊκό ζωγράφο Θεόφιλο Χατζημιχαήλ.",
 "script": [
  L("Ομιλήτρια", "f", "Ο Θεόφιλος Χατζημιχαήλ γεννήθηκε στη Βαρειά της Λέσβου, πιθανότατα στις αρχές της δεκαετίας του 1870. Δεν σπούδασε ποτέ ζωγραφική. Πέρασε μεγάλο μέρος της ζωής του στη Σμύρνη και στο Πήλιο, όπου ζωγράφιζε τοιχογραφίες σε σπίτια, καφενεία και μαγαζιά, συχνά με αντάλλαγμα ένα πιάτο φαγητό ή ένα κρεβάτι για τη νύχτα.", "Theophilos Hatzimichail was born in Vareia on Lesbos, most probably in the early 1870s. He never studied painting. He spent much of his life in Smyrna and on Pelion, where he painted murals in houses, coffee houses and shops, often in exchange for a plate of food or a bed for the night."),
  L("Ομιλήτρια", "f", "Ήταν μια μορφή που προκαλούσε τον χλευασμό των συγχρόνων του. Κυκλοφορούσε ντυμένος με φουστανέλα, σαν αγωνιστής του Εικοσιένα, και συχνά γινόταν αντικείμενο πειραγμάτων στους δρόμους. Τα θέματά του ήταν οι ήρωες της Επανάστασης, σκηνές από τη μυθολογία, αλλά και η καθημερινή ζωή: ψαράδες, βοσκοί, γλέντια και πανηγύρια.", "He was a figure who drew the ridicule of his contemporaries. He went about dressed in a fustanella, like a fighter of 1821, and was often the target of teasing in the streets. His subjects were the heroes of the Revolution, scenes from mythology, but also everyday life: fishermen, shepherds, feasts and village fairs."),
  L("Ομιλήτρια", "f", "Η αναγνώριση ήρθε σχεδόν στο τέλος της ζωής του. Στα τέλη της δεκαετίας του 1920, ο κριτικός και εκδότης Στρατής Ελευθεριάδης, γνωστός στο Παρίσι ως Teriade, ανακάλυψε το έργο του και του παρήγγειλε σειρά πινάκων, εξασφαλίζοντάς του τα προς το ζην. Ο Θεόφιλος πέθανε το 1934 στη Μυτιλήνη, χωρίς να προλάβει να δει την καταξίωσή του.", "Recognition came almost at the end of his life. In the late 1920s, the critic and publisher Stratis Eleftheriadis, known in Paris as Tériade, discovered his work and commissioned a series of paintings from him, securing him a livelihood. Theophilos died in 1934 in Mytilene, without living to see his acclaim."),
  L("Ομιλήτρια", "f", "Σήμερα θεωρείται ένας από τους σημαντικότερους Έλληνες ζωγράφους του εικοστού αιώνα. Η ζωγραφική του, με την επίπεδη προοπτική και τα έντονα χρώματα, εντυπωσίασε την ελληνική πρωτοπορία, που έβλεπε σε αυτόν μια αυθεντική έκφραση της λαϊκής παράδοσης. Το μουσείο που φέρει το όνομά του στη Βαρειά ιδρύθηκε με πρωτοβουλία του ίδιου του Teriade.", "Today he is regarded as one of the most important Greek painters of the twentieth century. His painting, with its flat perspective and vivid colours, impressed the Greek avant-garde, who saw in him an authentic expression of folk tradition. The museum bearing his name in Vareia was founded on the initiative of Tériade himself."),
 ],
 "questions": [
  Q("Πώς πληρωνόταν συχνά ο Θεόφιλος για τις τοιχογραφίες του;", ["Με χρυσά νομίσματα", "Με ένα πιάτο φαγητό ή ένα κρεβάτι για τη νύχτα", "Με πίνακες άλλων ζωγράφων", "Δεν πληρωνόταν ποτέ"], 1, "συχνά με αντάλλαγμα ένα πιάτο φαγητό ή ένα κρεβάτι για τη νύχτα"),
  Q("Πώς τον αντιμετώπιζαν οι σύγχρονοί του;", ["Με θαυμασμό", "Τον κορόιδευαν συχνά", "Τον αγνοούσαν εντελώς", "Τον φοβούνταν"], 1, "προκαλούσε τον χλευασμό των συγχρόνων του ... συχνά γινόταν αντικείμενο πειραγμάτων"),
  Q("Τι έκανε για εκείνον ο Teriade;", ["Του δίδαξε ζωγραφική στο Παρίσι", "Του παρήγγειλε πίνακες και του εξασφάλισε τα προς το ζην", "Του αγόρασε ένα σπίτι στη Σμύρνη", "Έγραψε τη βιογραφία του"], 1, "του παρήγγειλε σειρά πινάκων, εξασφαλίζοντάς του τα προς το ζην"),
  Q("Γιατί εντυπωσίασε η ζωγραφική του την ελληνική πρωτοπορία;", ["Επειδή μιμούνταν τους Ευρωπαίους", "Επειδή έβλεπαν σε αυτήν αυθεντική έκφραση της λαϊκής παράδοσης", "Επειδή ήταν πολύ ρεαλιστική", "Επειδή πουλιόταν ακριβά"], 1, "έβλεπε σε αυτόν μια αυθεντική έκφραση της λαϊκής παράδοσης"),
 ],
 "gloss": {"λαϊκό ζωγράφο": "λαϊκός ζωγράφος — folk painter", "τοιχογραφίες": "τοιχογραφία — mural, wall painting", "αντάλλαγμα": "αντάλλαγμα — something in exchange", "χλευασμό": "χλευασμός — ridicule, mockery", "φουστανέλα": "φουστανέλα — fustanella (pleated kilt of the traditional costume)", "αγωνιστής του Εικοσιένα": "αγωνιστής του Εικοσιένα — fighter in the 1821 War of Independence", "πειραγμάτων": "πείραγμα — teasing", "πανηγύρια": "πανηγύρι — village fair, saint's-day festival", "αναγνώριση": "αναγνώριση — recognition", "εκδότης": "εκδότης — publisher", "τα προς το ζην": "τα προς το ζην — the means of living, livelihood", "καταξίωσή": "καταξίωση — acclaim, recognition of worth", "επίπεδη προοπτική": "επίπεδη προοπτική — flat perspective", "πρωτοπορία": "πρωτοπορία — avant-garde", "πρωτοβουλία": "πρωτοβουλία — initiative"},
})

rnd = random.Random(49)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-49.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
