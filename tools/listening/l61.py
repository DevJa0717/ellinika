# Source for library/listening/listening-61.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l61.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l61-ann-ygra", "title": "Νέοι κανόνες για τα υγρά στη χειραποσκευή", "title_en": "New rules for liquids in hand luggage", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε στον χώρο ελέγχου ασφαλείας ενός αεροδρομίου. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Ανακοίνωση", "f", "Αγαπητοί επιβάτες, σας ενημερώνουμε ότι στο σημείο ελέγχου Β λειτουργούν πλέον νέοι αξονικοί σαρωτές. Οι επιβάτες που περνούν από αυτό το σημείο δεν χρειάζεται να βγάζουν από τη χειραποσκευή τους τα υγρά και τις ηλεκτρονικές συσκευές, όπως φορητούς υπολογιστές και ταμπλέτες.", "Dear passengers, we inform you that new CT scanners are now in operation at security checkpoint B. Passengers going through this checkpoint do not need to take liquids and electronic devices, such as laptops and tablets, out of their hand luggage."),
  L("Ανακοίνωση", "f", "Προσοχή, όμως: το όριο των εκατό χιλιοστόλιτρων ανά συσκευασία εξακολουθεί να ισχύει σε όλα τα σημεία ελέγχου, μέχρι νεωτέρας. Στο σημείο ελέγχου Α, οι παλιοί κανόνες παραμένουν σε ισχύ: τα υγρά τοποθετούνται σε διαφανές σακουλάκι, χωριστά από την τσάντα.", "Please note, however: the limit of one hundred millilitres per container still applies at all checkpoints, until further notice. At checkpoint A the old rules remain in force: liquids are placed in a transparent bag, separately from the bag."),
  L("Ανακοίνωση", "f", "Για τη γρηγορότερη εξυπηρέτησή σας, ακολουθήστε τις οδηγίες του προσωπικού και έχετε έτοιμη την κάρτα επιβίβασης. Σας ευχαριστούμε.", "For faster service, please follow the staff's instructions and have your boarding pass ready. Thank you."),
 ],
 "questions": [
  Q("Τι αλλάζει στο σημείο ελέγχου Β;", ["Δεν γίνεται πια έλεγχος", "Οι επιβάτες δεν χρειάζεται να βγάζουν υγρά και ηλεκτρονικές συσκευές από την τσάντα", "Επιτρέπονται μεγάλα μπουκάλια νερό", "Ελέγχονται μόνο οι βαλίτσες"], 1, "δεν χρειάζεται να βγάζουν από τη χειραποσκευή τους τα υγρά και τις ηλεκτρονικές συσκευές"),
  Q("Τι ισχύει ακόμη σε όλα τα σημεία ελέγχου;", ["Το όριο των εκατό χιλιοστόλιτρων ανά συσκευασία", "Η απαγόρευση των φορητών υπολογιστών", "Ο έλεγχος διαβατηρίων", "Η χρέωση για τα σακουλάκια"], 0, "το όριο των εκατό χιλιοστόλιτρων ανά συσκευασία εξακολουθεί να ισχύει σε όλα τα σημεία ελέγχου"),
  Q("Τι πρέπει να κάνουν οι επιβάτες στο σημείο ελέγχου Α;", ["Να περάσουν χωρίς έλεγχο", "Να βάλουν τα υγρά σε διαφανές σακουλάκι, χωριστά από την τσάντα", "Να αφήσουν τα υγρά στο γκισέ", "Να δείξουν το διαβατήριο"], 1, "τα υγρά τοποθετούνται σε διαφανές σακουλάκι, χωριστά από την τσάντα"),
 ],
 "gloss": {"χειραποσκευή": "χειραποσκευή — hand luggage", "σαρωτές": "σαρωτής — scanner", "φορητούς υπολογιστές": "φορητός υπολογιστής — laptop", "χιλιοστόλιτρων": "χιλιοστόλιτρο — millilitre", "συσκευασία": "συσκευασία — container, packaging", "μέχρι νεωτέρας": "μέχρι νεωτέρας — until further notice", "σε ισχύ": "σε ισχύ — in force", "διαφανές": "διαφανής — transparent", "κάρτα επιβίβασης": "κάρτα επιβίβασης — boarding pass"},
})

ITEMS.append({
 "id": "l61-vm-orthodontikos", "title": "Μήνυμα από τον ορθοδοντικό", "title_en": "A message from the orthodontist", "type": "voicemail", "level": "B2",
 "context_el": "Η κόρη σας φοράει σιδεράκια. Θα ακούσετε ένα μήνυμα από το ιατρείο του ορθοδοντικού στον τηλεφωνητή σας.",
 "script": [
  L("Γραμματέας", "f", "Καλησπέρα σας, κυρία Λαμπροπούλου, σας τηλεφωνώ από το ορθοδοντικό ιατρείο του κυρίου Ζερβού. Το ραντεβού της Δάφνης την Πέμπτη στις πέντε πρέπει να μετακινηθεί, γιατί ο γιατρός θα είναι σε συνέδριο. Μπορούμε να σας προτείνουμε την Τρίτη στις τέσσερις ή την επόμενη Δευτέρα στις έξι.", "Good afternoon, Mrs Lambropoulou, I'm calling from Dr Zervos's orthodontic practice. Dafni's appointment on Thursday at five has to be moved, because the doctor will be at a conference. We can offer you Tuesday at four or the following Monday at six."),
  L("Γραμματέας", "f", "Ο γιατρός ζήτησε επίσης να σας υπενθυμίσω ότι η Δάφνη πρέπει να φοράει τα λαστιχάκια κάθε βράδυ, όπως της εξήγησε, και να αποφεύγει τις τραγανές και κολλώδεις τροφές, όπως καραμέλες και ξηρούς καρπούς, γιατί μπορεί να ξεκολλήσουν τα σιδεράκια.", "The doctor also asked me to remind you that Dafni must wear the elastics every night, as he explained to her, and avoid crunchy and sticky foods, such as sweets and nuts, because the braces may come unstuck."),
  L("Γραμματέας", "f", "Παρακαλώ καλέστε μας για να επιβεβαιώσετε το νέο ραντεβού. Καλό απόγευμα.", "Please call us to confirm the new appointment. Have a good afternoon."),
 ],
 "questions": [
  Q("Γιατί μετακινείται το ραντεβού;", ["Γιατί η Δάφνη είναι άρρωστη", "Γιατί ο γιατρός θα είναι σε συνέδριο", "Γιατί το ιατρείο κλείνει για ανακαίνιση", "Γιατί χάλασε ένα μηχάνημα"], 1, "γιατί ο γιατρός θα είναι σε συνέδριο"),
  Q("Τι πρέπει να κάνει η Δάφνη κάθε βράδυ;", ["Να πλένει τα δόντια με ειδική οδοντόκρεμα", "Να φοράει τα λαστιχάκια", "Να βγάζει τα σιδεράκια", "Να παίρνει ένα φάρμακο"], 1, "η Δάφνη πρέπει να φοράει τα λαστιχάκια κάθε βράδυ"),
  Q("Γιατί πρέπει να αποφεύγει τις καραμέλες και τους ξηρούς καρπούς;", ["Γιατί χαλάνε τα δόντια", "Γιατί μπορεί να ξεκολλήσουν τα σιδεράκια", "Γιατί έχει αλλεργία", "Γιατί παχαίνουν"], 1, "γιατί μπορεί να ξεκολλήσουν τα σιδεράκια"),
 ],
 "gloss": {"ορθοδοντικό": "ορθοδοντικός — orthodontic; orthodontist", "σιδεράκια": "σιδεράκια — braces", "μετακινηθεί": "μετακινούμαι — to be moved", "λαστιχάκια": "λαστιχάκι — little elastic band", "τραγανές": "τραγανός — crunchy", "κολλώδεις": "κολλώδης — sticky", "ξηρούς καρπούς": "ξηροί καρποί — nuts", "ξεκολλήσουν": "ξεκολλάω — to come unstuck", "επιβεβαιώσετε": "επιβεβαιώνω — to confirm"},
})

ITEMS.append({
 "id": "l61-dia-antallagi-spitiou", "title": "Ανταλλαγή σπιτιού για τις διακοπές", "title_en": "A house swap for the holidays", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι συζητά αν θα ανταλλάξει το σπίτι του με μια οικογένεια από το εξωτερικό για τις καλοκαιρινές διακοπές.",
 "script": [
  L("Αλέξης", "m", "Κοίτα αυτή την πρόταση που ήρθε στην πλατφόρμα: μια οικογένεια από τη Λυών θέλει να ανταλλάξουμε σπίτια για δύο εβδομάδες τον Ιούλιο. Εμείς στο δικό τους διαμέρισμα, εκείνοι στο δικό μας.", "Look at this offer that came on the platform: a family from Lyon want to swap houses with us for two weeks in July. Us in their flat, them in ours."),
  L("Μυρτώ", "f", "Ακούγεται ωραίο, αφού θα γλιτώσουμε το ξενοδοχείο. Αλλά δεν ξέρω αν μου αρέσει η ιδέα να μένουν άγνωστοι στο σπίτι μας. Και αν σπάσουν κάτι;", "It sounds nice, since we'll save on the hotel. But I don't know if I like the idea of strangers staying in our home. And what if they break something?"),
  L("Αλέξης", "m", "Η πλατφόρμα έχει σύστημα αξιολογήσεων. Αυτοί έχουν κάνει ήδη έξι ανταλλαγές και όλες οι κριτικές είναι εξαιρετικές. Υπάρχει και ασφάλεια για ζημιές. Μπορούμε επίσης να μιλήσουμε πρώτα μαζί τους με βιντεοκλήση, να τους γνωρίσουμε.", "The platform has a rating system. They've already done six swaps and all the reviews are excellent. There's also insurance for damage. We can also talk to them first by video call, to get to know them."),
  L("Μυρτώ", "f", "Αυτό με καθησυχάζει λίγο. Και η γάτα; Ποιος θα τη φροντίζει;", "That reassures me a bit. And the cat? Who'll look after her?"),
  L("Αλέξης", "m", "Γράφουν ότι λατρεύουν τα ζώα και ότι θα τη φροντίσουν ευχαρίστως. Εμείς, πάλι, θα ποτίζουμε τα φυτά τους. Και μας αφήνουν και το αυτοκίνητό τους, για να κάνουμε εκδρομές στην εξοχή.", "They write that they love animals and will gladly look after her. We, in turn, will water their plants. And they're leaving us their car too, so we can go on trips to the countryside."),
  L("Μυρτώ", "f", "Εντάξει, ας κάνουμε τη βιντεοκλήση. Αλλά πρώτα πρέπει να καθαρίσουμε την αποθήκη. Δεν θέλω να δουν αυτό το χάος!", "OK, let's do the video call. But first we have to clear out the storeroom. I don't want them to see that mess!"),
 ],
 "questions": [
  Q("Τι ανησυχεί αρχικά τη Μυρτώ;", ["Το κόστος", "Η ιδέα να μένουν άγνωστοι στο σπίτι τους", "Το ταξίδι με το αεροπλάνο", "Η γλώσσα"], 1, "δεν ξέρω αν μου αρέσει η ιδέα να μένουν άγνωστοι στο σπίτι μας"),
  Q("Τι λέει ο Αλέξης για να την καθησυχάσει;", ["Ότι η οικογένεια είναι φίλοι τους", "Ότι υπάρχουν εξαιρετικές κριτικές και ασφάλεια για ζημιές", "Ότι θα κλειδώσουν όλα τα δωμάτια", "Ότι θα μείνει η γιαγιά στο σπίτι"], 1, "όλες οι κριτικές είναι εξαιρετικές. Υπάρχει και ασφάλεια για ζημιές"),
  Q("Τι θα αφήσει η γαλλική οικογένεια στον Αλέξη και τη Μυρτώ;", ["Τη γάτα τους", "Το αυτοκίνητό τους", "Τα ποδήλατά τους", "Μια κάρτα για το μετρό"], 1, "μας αφήνουν και το αυτοκίνητό τους"),
 ],
 "gloss": {"ανταλλάξουμε": "ανταλλάσσω — to swap, exchange", "γλιτώσουμε": "γλιτώνω — to save, avoid", "αξιολογήσεων": "αξιολόγηση — rating", "κριτικές": "κριτική — review", "ασφάλεια": "ασφάλεια — insurance", "βιντεοκλήση": "βιντεοκλήση — video call", "καθησυχάζει": "καθησυχάζω — to reassure", "ευχαρίστως": "ευχαρίστως — gladly", "εξοχή": "εξοχή — countryside"},
})

ITEMS.append({
 "id": "l61-dia-valitsa", "title": "Η βαλίτσα που δεν έφτασε", "title_en": "The suitcase that didn't arrive", "type": "dialogue", "level": "B2",
 "context_el": "Μια επιβάτισσα δεν βρίσκει τη βαλίτσα της μετά από μια πτήση. Θα ακούσετε τη συζήτησή της με τον υπάλληλο στο γραφείο αποσκευών.",
 "script": [
  L("Επιβάτισσα", "f", "Καλησπέρα. Ήρθα με την πτήση από τη Φρανκφούρτη και η βαλίτσα μου δεν εμφανίστηκε στον ιμάντα. Περίμενα μισή ώρα.", "Good evening. I came on the flight from Frankfurt and my suitcase didn't appear on the belt. I waited half an hour."),
  L("Υπάλληλος", "m", "Λυπάμαι πολύ. Μπορώ να δω την κάρτα επιβίβασης και το απόκομμα της αποσκευής; Ναι… Βλέπω στο σύστημα ότι η βαλίτσα σας δεν φορτώθηκε στη Φρανκφούρτη, γιατί η ανταπόκριση ήταν πολύ σύντομη. Θα έρθει με την επόμενη πτήση, αύριο το πρωί.", "I'm very sorry. May I see your boarding pass and the baggage tag? Yes… I see in the system that your suitcase wasn't loaded in Frankfurt, because the connection was very short. It will come on the next flight, tomorrow morning."),
  L("Επιβάτισσα", "f", "Αύριο; Μα όλα μου τα πράγματα είναι μέσα, ακόμη και τα φάρμακά μου. Και αύριο το μεσημέρι έχω μια σημαντική συνάντηση.", "Tomorrow? But all my things are inside, even my medicines. And tomorrow at midday I have an important meeting."),
  L("Υπάλληλος", "m", "Καταλαβαίνω. Θα συμπληρώσουμε τώρα μια δήλωση, και θα σας τη φέρουμε στο ξενοδοχείο σας με κούριερ, χωρίς χρέωση. Στο μεταξύ, η εταιρεία καλύπτει τα απαραίτητα έξοδα, όπως είδη προσωπικής υγιεινής ή μια αλλαξιά ρούχα. Κρατήστε μόνο τις αποδείξεις.", "I understand. We'll fill in a report now, and we'll bring it to your hotel by courier, free of charge. In the meantime, the airline covers essential expenses, such as toiletries or a change of clothes. Just keep the receipts."),
  L("Επιβάτισσα", "f", "Και για τα φάρμακα;", "And the medicines?"),
  L("Υπάλληλος", "m", "Αν είναι επείγον, υπάρχει φαρμακείο στο επίπεδο των αφίξεων. Με τη συνταγή του γιατρού σας, το κόστος θα σας επιστραφεί κι αυτό. Ορίστε ο αριθμός της δήλωσης, για να παρακολουθείτε τη βαλίτσα σας ηλεκτρονικά.", "If it's urgent, there's a pharmacy on the arrivals level. With your doctor's prescription, the cost will be refunded to you as well. Here is the report number, so you can track your suitcase online."),
 ],
 "questions": [
  Q("Γιατί δεν έφτασε η βαλίτσα;", ["Γιατί χάθηκε στο αεροδρόμιο", "Γιατί δεν φορτώθηκε στη Φρανκφούρτη λόγω σύντομης ανταπόκρισης", "Γιατί ήταν πολύ βαριά", "Γιατί στάλθηκε σε άλλη πόλη"], 1, "η βαλίτσα σας δεν φορτώθηκε στη Φρανκφούρτη, γιατί η ανταπόκριση ήταν πολύ σύντομη"),
  Q("Πώς θα πάρει τη βαλίτσα της;", ["Θα περάσει η ίδια από το αεροδρόμιο", "Θα της τη φέρουν στο ξενοδοχείο με κούριερ", "Θα τη στείλουν ταχυδρομικώς", "Θα πρέπει να πληρώσει μεταφορά"], 1, "θα σας τη φέρουμε στο ξενοδοχείο σας με κούριερ, χωρίς χρέωση"),
  Q("Τι πρέπει να κρατήσει για να της επιστραφούν τα έξοδα;", ["Την κάρτα επιβίβασης", "Τις αποδείξεις", "Το εισιτήριο", "Το διαβατήριο"], 1, "Κρατήστε μόνο τις αποδείξεις"),
 ],
 "gloss": {"ιμάντα": "ιμάντας — (baggage) belt", "απόκομμα": "απόκομμα — tag, stub", "αποσκευής": "αποσκευή — luggage", "φορτώθηκε": "φορτώνομαι — to be loaded", "ανταπόκριση": "ανταπόκριση — connection (flight)", "δήλωση": "δήλωση — report, declaration", "είδη προσωπικής υγιεινής": "είδη προσωπικής υγιεινής — toiletries", "αλλαξιά": "αλλαξιά — change (of clothes)", "αποδείξεις": "απόδειξη — receipt", "συνταγή": "συνταγή — prescription"},
})

ITEMS.append({
 "id": "l61-int-vitro", "title": "Η τεχνίτρια του βιτρό", "title_en": "The stained-glass maker", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή για τις τέχνες, ο δημοσιογράφος μιλά με μια γυναίκα που φτιάχνει βιτρό σε ένα εργαστήρι της Θεσσαλονίκης.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αγλαΐα, πώς ξεκινήσατε με το βιτρό;", "Ms Aglaia, how did you start with stained glass?"),
  L("Τεχνίτρια", "f", "Ήμουν φοιτήτρια στην Καλών Τεχνών και ζωγράφιζα. Ένα καλοκαίρι, στη Γαλλία, μπήκα σε έναν γοτθικό καθεδρικό ναό, και το φως που περνούσε από τα παράθυρα με συγκλόνισε. Ήταν σαν να ζωγράφιζε κανείς με το ίδιο το φως. Τότε αποφάσισα να μάθω την τέχνη, και μαθήτευσα δύο χρόνια σε ένα εργαστήρι στη Σαρτρ.", "I was a student at the School of Fine Arts and I painted. One summer, in France, I went into a Gothic cathedral and the light coming through the windows overwhelmed me. It was as if someone were painting with light itself. Then I decided to learn the craft, and I apprenticed for two years in a workshop in Chartres."),
  L("Δημοσιογράφος", "m", "Πώς φτιάχνεται ένα βιτρό;", "How is a stained-glass window made?"),
  L("Τεχνίτρια", "f", "Πρώτα σχεδιάζω το έργο σε φυσικό μέγεθος. Μετά κόβω τα κομμάτια του γυαλιού ένα ένα, με ειδικό κόφτη. Κάποιες λεπτομέρειες, όπως τα πρόσωπα, τις ζωγραφίζω με ειδικά χρώματα και τις ψήνω στο καμίνι. Στο τέλος ενώνω τα κομμάτια με λωρίδες μολυβιού και τα κολλάω. Ένα μεσαίο παράθυρο μπορεί να μου πάρει δύο μήνες.", "First I draw the work at full size. Then I cut the pieces of glass one by one with a special cutter. Some details, such as faces, I paint with special colours and fire in the kiln. Finally I join the pieces with strips of lead and solder them. A medium-sized window can take me two months."),
  L("Δημοσιογράφος", "m", "Ποιοι είναι οι πελάτες σας;", "Who are your customers?"),
  L("Τεχνίτρια", "f", "Παλιότερα κυρίως εκκλησίες. Σήμερα όλο και περισσότεροι ιδιώτες θέλουν ένα βιτρό στην είσοδο ή στο κλιμακοστάσιο του σπιτιού τους. Κάνω επίσης αποκαταστάσεις σε παλιά αρχοντικά, όπου συχνά βρίσκω γυαλιά εκατό και πλέον ετών. Το να τα σώζεις είναι σαν να μιλάς με τους τεχνίτες που σε προηγήθηκαν.", "In the past mainly churches. Today more and more private individuals want a stained-glass window in the entrance or stairwell of their home. I also do restorations in old mansions, where I often find glass more than a hundred years old. Saving it is like talking to the craftsmen who came before you."),
 ],
 "questions": [
  Q("Τι την έκανε να ασχοληθεί με το βιτρό;", ["Μια έκθεση στη Θεσσαλονίκη", "Το φως στα παράθυρα ενός γοτθικού καθεδρικού ναού", "Ένα μάθημα στο πανεπιστήμιο", "Η οικογενειακή παράδοση"], 1, "μπήκα σε έναν γοτθικό καθεδρικό ναό, και το φως που περνούσε από τα παράθυρα με συγκλόνισε"),
  Q("Με τι ενώνει τα κομμάτια του γυαλιού;", ["Με κόλλα", "Με λωρίδες μολυβιού", "Με ξύλινα πλαίσια", "Με σύρμα"], 1, "ενώνω τα κομμάτια με λωρίδες μολυβιού"),
  Q("Ποιοι ζητούν σήμερα όλο και περισσότερο βιτρό;", ["Οι εκκλησίες", "Οι ιδιώτες για τα σπίτια τους", "Τα μουσεία", "Τα ξενοδοχεία"], 1, "όλο και περισσότεροι ιδιώτες θέλουν ένα βιτρό στην είσοδο ή στο κλιμακοστάσιο του σπιτιού τους"),
 ],
 "gloss": {"βιτρό": "βιτρό — stained glass", "καθεδρικό ναό": "καθεδρικός ναός — cathedral", "συγκλόνισε": "συγκλονίζω — to overwhelm, move deeply", "μαθήτευσα": "μαθητεύω — to apprentice", "κόφτη": "κόφτης — cutter", "καμίνι": "καμίνι — kiln", "μολυβιού": "μόλυβδος/μολύβι — lead", "κλιμακοστάσιο": "κλιμακοστάσιο — stairwell", "προηγήθηκαν": "προηγούμαι — to come before"},
})

ITEMS.append({
 "id": "l61-rep-doxa", "title": "Η λίμνη Δόξα", "title_en": "Lake Doxa", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από μια ορεινή λίμνη της Πελοποννήσου.",
 "script": [
  L("Ρεπόρτερ", "f", "Βρισκόμαστε στη λίμνη Δόξα, στα ορεινά της Κορινθίας, σε υψόμετρο περίπου εννιακοσίων μέτρων. Η λίμνη είναι τεχνητή: δημιουργήθηκε στις αρχές της δεκαετίας του 2000 με ένα φράγμα, για να συγκεντρώνει νερό για την άρδευση. Γρήγορα, όμως, έγινε ένας από τους πιο αγαπημένους προορισμούς για εκδρομές στην Πελοπόννησο.", "We're at Lake Doxa, in the mountains of Corinthia, at an altitude of about nine hundred metres. The lake is artificial: it was created in the early 2000s with a dam, to collect water for irrigation. Quickly, however, it became one of the most popular destinations for day trips in the Peloponnese."),
  L("Ρεπόρτερ", "f", "Το πιο φωτογραφημένο σημείο είναι το μικρό εκκλησάκι του Αγίου Φανουρίου, χτισμένο σε μια χερσόνησο μέσα στη λίμνη. Γύρω γύρω απλώνονται πυκνά δάση από έλατα και πεύκα, που καθρεφτίζονται στο νερό. Το φθινόπωρο, τα χρώματα των φύλλων κάνουν το τοπίο ακόμη πιο εντυπωσιακό.", "The most photographed spot is the little chapel of Agios Fanourios, built on a peninsula in the lake. All around stretch dense forests of firs and pines, reflected in the water. In autumn, the colours of the leaves make the landscape even more impressive."),
  L("Ρεπόρτερ", "f", "Υπάρχει ένα μονοπάτι που κάνει τον γύρο της λίμνης, περίπου πέντε χιλιόμετρα, κατάλληλο και για οικογένειες. Το κολύμπι απαγορεύεται, γιατί πρόκειται για ταμιευτήρα νερού. Οι επισκέπτες καλούνται επίσης να μην αφήνουν σκουπίδια και να μην ανάβουν φωτιές, ιδίως το καλοκαίρι.", "There's a path that goes round the lake, about five kilometres, suitable for families too. Swimming is forbidden, because it's a water reservoir. Visitors are also asked not to leave rubbish and not to light fires, especially in summer."),
 ],
 "questions": [
  Q("Γιατί δημιουργήθηκε η λίμνη Δόξα;", ["Για να παράγει ρεύμα", "Για να συγκεντρώνει νερό για την άρδευση", "Για τον τουρισμό", "Για την ύδρευση της Αθήνας"], 1, "για να συγκεντρώνει νερό για την άρδευση"),
  Q("Ποιο είναι το πιο φωτογραφημένο σημείο;", ["Το φράγμα", "Το εκκλησάκι του Αγίου Φανουρίου", "Ένα παλιό χωριό", "Ένας καταρράκτης"], 1, "Το πιο φωτογραφημένο σημείο είναι το μικρό εκκλησάκι του Αγίου Φανουρίου"),
  Q("Γιατί απαγορεύεται το κολύμπι;", ["Γιατί το νερό είναι πολύ κρύο", "Γιατί πρόκειται για ταμιευτήρα νερού", "Γιατί η λίμνη είναι πολύ βαθιά", "Γιατί υπάρχουν φίδια"], 1, "Το κολύμπι απαγορεύεται, γιατί πρόκειται για ταμιευτήρα νερού"),
 ],
 "gloss": {"υψόμετρο": "υψόμετρο — altitude", "τεχνητή": "τεχνητός — artificial", "φράγμα": "φράγμα — dam", "άρδευση": "άρδευση — irrigation", "χερσόνησο": "χερσόνησος — peninsula", "έλατα": "έλατο — fir", "καθρεφτίζονται": "καθρεφτίζομαι — to be reflected", "ταμιευτήρα": "ταμιευτήρας — reservoir"},
})

ITEMS.append({
 "id": "l61-dia-istioploia", "title": "Μαθήματα ιστιοπλοΐας", "title_en": "Sailing lessons", "type": "dialogue", "level": "B2",
 "context_el": "Μια μητέρα ζητά πληροφορίες για μαθήματα ιστιοπλοΐας για τον γιο της σε έναν ναυτικό όμιλο. Θα ακούσετε τη συζήτησή της με τον προπονητή.",
 "script": [
  L("Μητέρα", "f", "Καλημέρα. Ο γιος μου είναι δέκα χρονών και θέλει πολύ να μάθει ιστιοπλοΐα. Από ποια ηλικία δέχεστε παιδιά;", "Good morning. My son is ten and really wants to learn sailing. From what age do you accept children?"),
  L("Προπονητής", "m", "Από οκτώ χρονών, αρκεί να ξέρουν κολύμπι. Τα παιδιά ξεκινούν με το «Οπτιμιστ», ένα μικρό, ασφαλές σκάφος για έναν άνθρωπο. Είναι το ιδανικό σκάφος για να μάθουν να διαβάζουν τον αέρα και να παίρνουν αποφάσεις μόνα τους.", "From eight, as long as they can swim. Children start with the Optimist, a small, safe single-handed boat. It's the ideal boat for learning to read the wind and make decisions on their own."),
  L("Μητέρα", "f", "Μόνα τους; Δεν είναι επικίνδυνο;", "On their own? Isn't it dangerous?"),
  L("Προπονητής", "m", "Καθόλου. Τα παιδιά φορούν πάντα σωσίβιο, και ένα φουσκωτό με προπονητή τα ακολουθεί σε όλη τη διάρκεια του μαθήματος. Επίσης, την πρώτη μέρα μαθαίνουν τι να κάνουν αν αναποδογυρίσει το σκάφος. Συμβαίνει συχνά, και στην αρχή τα παιδιά το διασκεδάζουν!", "Not at all. The children always wear a life jacket, and an inflatable with a coach follows them throughout the lesson. Also, on the first day they learn what to do if the boat capsizes. It happens often, and at first the children find it fun!"),
  L("Μητέρα", "f", "Πότε γίνονται τα μαθήματα;", "When are the lessons?"),
  L("Προπονητής", "m", "Τρεις φορές την εβδομάδα, απογεύματα, και τα Σάββατα το πρωί. Αν ο καιρός είναι πολύ άσχημος, κάνουμε θεωρία στην αίθουσα: κόμβους, κανόνες, μετεωρολογία. Η ιστιοπλοΐα δεν είναι μόνο άθλημα, είναι και σχολείο υπευθυνότητας.", "Three times a week, in the afternoons, and on Saturday mornings. If the weather is very bad, we do theory in the classroom: knots, rules, meteorology. Sailing isn't just a sport; it's also a school of responsibility."),
 ],
 "questions": [
  Q("Ποια προϋπόθεση υπάρχει για να ξεκινήσει ένα παιδί;", ["Να είναι πάνω από δώδεκα χρονών", "Να ξέρει κολύμπι", "Να έχει δικό του σκάφος", "Να έχει κάνει άλλο άθλημα"], 1, "Από οκτώ χρονών, αρκεί να ξέρουν κολύμπι"),
  Q("Πώς εξασφαλίζεται η ασφάλεια των παιδιών;", ["Δεν βγαίνουν ποτέ από το λιμάνι", "Φορούν σωσίβιο και τα ακολουθεί φουσκωτό με προπονητή", "Πλέουν πάντα δύο μαζί", "Πλέουν μόνο όταν δεν φυσάει"], 1, "Τα παιδιά φορούν πάντα σωσίβιο, και ένα φουσκωτό με προπονητή τα ακολουθεί"),
  Q("Τι κάνουν όταν ο καιρός είναι πολύ άσχημος;", ["Ακυρώνουν το μάθημα", "Κάνουν θεωρία στην αίθουσα", "Κολυμπούν στην πισίνα", "Βλέπουν ταινίες"], 1, "κάνουμε θεωρία στην αίθουσα: κόμβους, κανόνες, μετεωρολογία"),
 ],
 "gloss": {"ιστιοπλοΐα": "ιστιοπλοΐα — sailing", "ναυτικό όμιλο": "ναυτικός όμιλος — sailing club", "σωσίβιο": "σωσίβιο — life jacket", "αναποδογυρίσει": "αναποδογυρίζω — to capsize, overturn", "κόμβους": "κόμβος — knot", "μετεωρολογία": "μετεωρολογία — meteorology", "υπευθυνότητας": "υπευθυνότητα — responsibility"},
})

ITEMS.append({
 "id": "l61-mono-kapnisma", "title": "Πώς έκοψα το κάπνισμα", "title_en": "How I gave up smoking", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν άντρα να μιλά σε μια ομάδα υποστήριξης για το πώς σταμάτησε το κάπνισμα.",
 "script": [
  L("Ομιλητής", "m", "Κάπνιζα είκοσι πέντε χρόνια, ένα πακέτο τη μέρα. Είχα προσπαθήσει να το κόψω τουλάχιστον πέντε φορές, αλλά πάντα ξανάρχιζα μετά από λίγες εβδομάδες, συνήθως σε κάποια στιγμή άγχους στη δουλειά ή σε μια βραδιά με φίλους.", "I smoked for twenty-five years, a pack a day. I had tried to quit at least five times, but I always started again after a few weeks, usually at some stressful moment at work or on a night out with friends."),
  L("Ομιλητής", "m", "Αυτή τη φορά άλλαξα τακτική. Πήγα σε ένα ιατρείο διακοπής καπνίσματος σε δημόσιο νοσοκομείο, όπου μου έδωσαν και φαρμακευτική βοήθεια. Αλλά το πιο σημαντικό ήταν ότι έμαθα να αναγνωρίζω τις στιγμές που με «καλούσε» το τσιγάρο: τον πρώτο καφέ, το διάλειμμα στη δουλειά, μετά το φαγητό. Σε εκείνες τις στιγμές έκανα κάτι άλλο: έπινα νερό, έκανα μια βόλτα, έπαιρνα τηλέφωνο έναν φίλο.", "This time I changed tactics. I went to a smoking cessation clinic at a public hospital, where they also gave me medication. But the most important thing was that I learned to recognise the moments when cigarettes 'called' me: the first coffee, the break at work, after a meal. At those moments I did something else: drank water, went for a walk, phoned a friend."),
  L("Ομιλητής", "m", "Έχουν περάσει δύο χρόνια. Ξανάβρα τη γεύση και τη μυρωδιά, ανεβαίνω τις σκάλες χωρίς να λαχανιάζω, και με τα χρήματα που γλίτωσα κάναμε με τη γυναίκα μου ένα ταξίδι στη Σκωτία. Αν μπόρεσα εγώ, μπορεί ο καθένας.", "Two years have passed. I've got back my sense of taste and smell, I climb stairs without getting out of breath, and with the money I saved my wife and I took a trip to Scotland. If I could do it, anyone can."),
 ],
 "questions": [
  Q("Πότε ξανάρχιζε συνήθως το κάπνισμα;", ["Τα Σαββατοκύριακα", "Σε στιγμές άγχους ή σε βραδιές με φίλους", "Όταν ταξίδευε", "Όταν έπινε αλκοόλ"], 1, "συνήθως σε κάποια στιγμή άγχους στη δουλειά ή σε μια βραδιά με φίλους"),
  Q("Ποιο ήταν, κατά τον ομιλητή, το πιο σημαντικό αυτή τη φορά;", ["Τα φάρμακα", "Ότι έμαθε να αναγνωρίζει τις στιγμές που τον «καλούσε» το τσιγάρο", "Ότι η γυναίκα του τον πίεσε", "Ότι ακρίβυναν τα τσιγάρα"], 1, "το πιο σημαντικό ήταν ότι έμαθα να αναγνωρίζω τις στιγμές που με «καλούσε» το τσιγάρο"),
  Q("Τι έκαναν με τα χρήματα που γλίτωσε;", ["Αγόρασαν αυτοκίνητο", "Έκαναν ένα ταξίδι στη Σκωτία", "Τα έδωσαν σε φιλανθρωπία", "Ανακαίνισαν το σπίτι"], 1, "με τα χρήματα που γλίτωσα κάναμε με τη γυναίκα μου ένα ταξίδι στη Σκωτία"),
 ],
 "gloss": {"κόψω": "κόβω (το κάπνισμα) — to quit (smoking)", "ξανάρχιζα": "ξαναρχίζω — to start again", "τακτική": "τακτική — tactics", "διακοπής καπνίσματος": "διακοπή καπνίσματος — smoking cessation", "φαρμακευτική": "φαρμακευτικός — medicinal, pharmaceutical", "Ξανάβρα": "ξαναβρίσκω — to find again", "λαχανιάζω": "λαχανιάζω — to get out of breath", "γλίτωσα": "γλιτώνω — to save"},
})

ITEMS.append({
 "id": "l61-c1-diagnosi", "title": "Η τεχνητή νοημοσύνη στη διάγνωση", "title_en": "Artificial intelligence in diagnosis", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την υγεία, η δημοσιογράφος συζητά με έναν ακτινολόγο για τη χρήση της τεχνητής νοημοσύνης στην ιατρική.",
 "script": [
  L("Δημοσιογράφος", "f", "Γιατρέ, θα αντικαταστήσει η τεχνητή νοημοσύνη τους ακτινολόγους;", "Doctor, will artificial intelligence replace radiologists?"),
  L("Ακτινολόγος", "m", "Το ερώτημα αυτό ακούγεται εδώ και χρόνια, και μέχρι στιγμής η απάντηση είναι όχι. Τα αλγοριθμικά συστήματα είναι πράγματι εντυπωσιακά σε συγκεκριμένες εργασίες: εντοπίζουν μικρά οζίδια στους πνεύμονες ή ύποπτες αλλοιώσεις σε μια μαστογραφία με ακρίβεια που συχνά συγκρίνεται με εκείνη έμπειρων γιατρών. Ωστόσο, η διάγνωση δεν είναι μόνο αναγνώριση εικόνων. Προϋποθέτει να συνδυάσεις το εύρημα με το ιστορικό του ασθενούς, με τα συμπτώματα, με πληροφορίες που δεν φαίνονται στην οθόνη.", "This question has been heard for years, and so far the answer is no. Algorithmic systems are indeed impressive at specific tasks: they detect small nodules in the lungs or suspicious lesions on a mammogram with an accuracy often comparable to that of experienced doctors. However, diagnosis isn't just image recognition. It requires combining the finding with the patient's history, symptoms, information not visible on the screen."),
  L("Δημοσιογράφος", "f", "Πώς χρησιμοποιείτε εσείς αυτά τα εργαλεία στην πράξη;", "How do you use these tools in practice?"),
  L("Ακτινολόγος", "m", "Ως «δεύτερο ζευγάρι μάτια». Το σύστημα επισημαίνει περιοχές που ίσως χρειάζονται προσοχή, κι εγώ αποφασίζω. Αυτό μειώνει τις παραλείψεις, ιδίως στο τέλος μιας κουραστικής βάρδιας, όταν η προσοχή του ανθρώπου πέφτει. Υπάρχει όμως και ο αντίθετος κίνδυνος: να εμπιστευτεί κανείς τυφλά τη μηχανή και να πάψει να σκέφτεται κριτικά. Το φαινόμενο αυτό έχει όνομα, ονομάζεται «προκατάληψη του αυτοματισμού».", "As a 'second pair of eyes'. The system flags areas that may need attention, and I decide. This reduces omissions, especially at the end of a tiring shift, when human attention drops. But there's also the opposite danger: trusting the machine blindly and ceasing to think critically. This phenomenon has a name: it's called 'automation bias'."),
  L("Δημοσιογράφος", "f", "Και ποιος ευθύνεται, αν το σύστημα κάνει λάθος;", "And who is responsible if the system makes a mistake?"),
  L("Ακτινολόγος", "m", "Αυτό είναι ίσως το πιο ανοιχτό ζήτημα. Προς το παρόν, την τελική ευθύνη τη φέρει ο γιατρός που υπογράφει τη γνωμάτευση. Γι’ αυτό είναι κρίσιμο τα συστήματα να είναι διαφανή, να μπορούμε δηλαδή να καταλάβουμε γιατί κατέληξαν σε ένα συμπέρασμα. Ένα «μαύρο κουτί», όσο ακριβές κι αν είναι, δύσκολα θα κερδίσει την εμπιστοσύνη γιατρών και ασθενών.", "That is perhaps the most open question. For now, final responsibility rests with the doctor who signs the report. That's why it's crucial for systems to be transparent, meaning we can understand why they reached a conclusion. A 'black box', however accurate, will hardly win the trust of doctors and patients."),
 ],
 "questions": [
  Q("Σε τι είναι εντυπωσιακά τα αλγοριθμικά συστήματα, σύμφωνα με τον ακτινολόγο;", ["Στη συζήτηση με τους ασθενείς", "Στον εντοπισμό μικρών αλλοιώσεων σε εικόνες", "Στη σύνταξη του ιστορικού", "Στη θεραπεία"], 1, "εντοπίζουν μικρά οζίδια στους πνεύμονες ή ύποπτες αλλοιώσεις σε μια μαστογραφία"),
  Q("Γιατί η διάγνωση δεν είναι μόνο αναγνώριση εικόνων;", ["Γιατί οι εικόνες είναι συχνά θολές", "Γιατί απαιτεί συνδυασμό του ευρήματος με το ιστορικό και τα συμπτώματα", "Γιατί οι ασθενείς δεν εμπιστεύονται τις μηχανές", "Γιατί ο νόμος το απαγορεύει"], 1, "Προϋποθέτει να συνδυάσεις το εύρημα με το ιστορικό του ασθενούς, με τα συμπτώματα"),
  Q("Τι είναι η «προκατάληψη του αυτοματισμού»;", ["Η δυσπιστία των γιατρών απέναντι στις μηχανές", "Η τυφλή εμπιστοσύνη στη μηχανή που οδηγεί σε έλλειψη κριτικής σκέψης", "Η αποτυχία των μηχανών σε δύσκολες περιπτώσεις", "Η κούραση στο τέλος της βάρδιας"], 1, "να εμπιστευτεί κανείς τυφλά τη μηχανή και να πάψει να σκέφτεται κριτικά"),
  Q("Γιατί είναι κρίσιμο τα συστήματα να είναι διαφανή;", ["Για να κοστίζουν λιγότερο", "Για να μπορούμε να καταλάβουμε πώς κατέληξαν σε ένα συμπέρασμα και να κερδίσουν εμπιστοσύνη", "Για να μη χρειάζονται γιατρούς", "Για να είναι πιο γρήγορα"], 1, "να μπορούμε δηλαδή να καταλάβουμε γιατί κατέληξαν σε ένα συμπέρασμα"),
 ],
 "gloss": {"ακτινολόγους": "ακτινολόγος — radiologist", "οζίδια": "οζίδιο — nodule", "αλλοιώσεις": "αλλοίωση — lesion", "μαστογραφία": "μαστογραφία — mammogram", "ιστορικό": "ιστορικό — (medical) history", "επισημαίνει": "επισημαίνω — to flag, point out", "παραλείψεις": "παράλειψη — omission", "προκατάληψη": "προκατάληψη — bias", "γνωμάτευση": "γνωμάτευση — (medical) report", "διαφανή": "διαφανής — transparent"},
})

ITEMS.append({
 "id": "l61-c1-valkanikoi", "title": "Οι Βαλκανικοί Πόλεμοι", "title_en": "The Balkan Wars", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από διάλεξη ιστορικού για τους πολέμους που διπλασίασαν σχεδόν το ελληνικό κράτος.",
 "script": [
  L("Ιστορικός", "f", "Το φθινόπωρο του 1912, η Ελλάδα, η Σερβία, η Βουλγαρία και το Μαυροβούνιο, ενωμένες στη Βαλκανική Συμμαχία, κήρυξαν τον πόλεμο στην Οθωμανική Αυτοκρατορία. Ήταν μια συμμαχία συμφέροντος και όχι εμπιστοσύνης: κάθε χώρα είχε τις δικές της βλέψεις στα ίδια εδάφη, και κυρίως στη Μακεδονία.", "In the autumn of 1912, Greece, Serbia, Bulgaria and Montenegro, united in the Balkan League, declared war on the Ottoman Empire. It was an alliance of interest, not of trust: each country had its own designs on the same territories, above all on Macedonia."),
  L("Ιστορικός", "f", "Ο ελληνικός στρατός προέλασε γρήγορα και στις 26 Οκτωβρίου μπήκε στη Θεσσαλονίκη, λίγες ώρες πριν φτάσουν οι Βούλγαροι. Τους επόμενους μήνες απελευθερώθηκαν τα Ιωάννινα και τα νησιά του βορειοανατολικού Αιγαίου, ενώ ο στόλος εξασφάλισε τον έλεγχο της θάλασσας. Η ήττα των Οθωμανών ήταν ταχύτερη από ό,τι περίμενε οποιοσδήποτε.", "The Greek army advanced rapidly and on 26 October entered Thessaloniki, a few hours before the Bulgarians arrived. In the following months Ioannina and the islands of the north-east Aegean were liberated, while the fleet secured control of the sea. The Ottoman defeat was faster than anyone had expected."),
  L("Ιστορικός", "f", "Η μοιρασιά των λαφύρων, όμως, οδήγησε σε νέο πόλεμο. Το καλοκαίρι του 1913 η Βουλγαρία επιτέθηκε στους πρώην συμμάχους της και ηττήθηκε. Με τη Συνθήκη του Βουκουρεστίου, η Ελλάδα σχεδόν διπλασίασε την έκτασή της και τον πληθυσμό της. Η επιτυχία, ωστόσο, είχε και τη σκοτεινή της πλευρά: ενσωμάτωσε πληθυσμούς με διαφορετικές γλώσσες και ταυτότητες και άφησε ανοιχτές πληγές που θα ταλάνιζαν τα Βαλκάνια για δεκαετίες.", "The division of the spoils, however, led to a new war. In the summer of 1913 Bulgaria attacked its former allies and was defeated. With the Treaty of Bucharest, Greece almost doubled its territory and its population. Success, however, also had its dark side: it incorporated populations with different languages and identities and left open wounds that would plague the Balkans for decades."),
 ],
 "questions": [
  Q("Πώς χαρακτηρίζει η ομιλήτρια τη Βαλκανική Συμμαχία;", ["Ως συμμαχία φιλίας", "Ως συμμαχία συμφέροντος και όχι εμπιστοσύνης", "Ως αμυντική συμμαχία", "Ως συμμαχία με τις Μεγάλες Δυνάμεις"], 1, "Ήταν μια συμμαχία συμφέροντος και όχι εμπιστοσύνης"),
  Q("Τι συνέβη στις 26 Οκτωβρίου 1912;", ["Υπογράφηκε η ειρήνη", "Ο ελληνικός στρατός μπήκε στη Θεσσαλονίκη", "Απελευθερώθηκαν τα Ιωάννινα", "Η Βουλγαρία επιτέθηκε στην Ελλάδα"], 1, "στις 26 Οκτωβρίου μπήκε στη Θεσσαλονίκη"),
  Q("Τι προκάλεσε τον δεύτερο πόλεμο;", ["Μια νέα οθωμανική επίθεση", "Η μοιρασιά των εδαφών ανάμεσα στους συμμάχους", "Η παρέμβαση της Ρωσίας", "Μια επανάσταση στη Σερβία"], 1, "Η μοιρασιά των λαφύρων, όμως, οδήγησε σε νέο πόλεμο"),
  Q("Ποια «σκοτεινή πλευρά» της επιτυχίας αναφέρει η ομιλήτρια;", ["Τις οικονομικές δυσκολίες", "Την ενσωμάτωση πληθυσμών με διαφορετικές ταυτότητες και τις ανοιχτές πληγές", "Την απώλεια της Κρήτης", "Τον εμφύλιο πόλεμο"], 1, "ενσωμάτωσε πληθυσμούς με διαφορετικές γλώσσες και ταυτότητες και άφησε ανοιχτές πληγές"),
 ],
 "gloss": {"βλέψεις": "βλέψεις — designs, ambitions", "εδάφη": "έδαφος — territory", "προέλασε": "προελαύνω — to advance", "εξασφάλισε": "εξασφαλίζω — to secure", "μοιρασιά": "μοιρασιά — division, sharing out", "λαφύρων": "λάφυρο — spoils", "ενσωμάτωσε": "ενσωματώνω — to incorporate", "ταλάνιζαν": "ταλανίζω — to plague, torment"},
})

rnd = random.Random(61)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-61.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
