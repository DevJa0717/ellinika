# Source for library/listening/listening-21.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l21.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l21-ann-revma", "title": "Προγραμματισμένη διακοπή ρεύματος", "title_en": "A planned power cut", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση σε έναν τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο διαχειριστής του δικτύου ηλεκτρικής ενέργειας ανακοινώνει ότι την Τετάρτη, από τις οχτώ το πρωί ως τις δύο το μεσημέρι, θα γίνει προγραμματισμένη διακοπή ρεύματος στις οδούς γύρω από την κεντρική πλατεία, λόγω εργασιών αναβάθμισης του δικτύου.", "The electricity network operator announces that on Wednesday, from eight in the morning until two in the afternoon, there will be a planned power cut in the streets around the central square, due to network upgrade works."),
  L("Εκφωνήτρια", "f", "Οι κάτοικοι παρακαλούνται να αποσυνδέσουν τις ευαίσθητες ηλεκτρικές συσκευές, όπως υπολογιστές και τηλεοράσεις, για να μην καταστραφούν όταν επανέλθει η τάση. Οι ανελκυστήρες των πολυκατοικιών δεν θα λειτουργούν.", "Residents are asked to unplug sensitive electrical appliances, such as computers and televisions, so that they are not damaged when the power comes back. The lifts in apartment buildings will not work."),
  L("Εκφωνήτρια", "f", "Όσοι χρησιμοποιούν ιατρικά μηχανήματα στο σπίτι, όπως συσκευές οξυγόνου, πρέπει να επικοινωνήσουν άμεσα με τον δήμο, ο οποίος θα διαθέσει γεννήτριες. Σε περίπτωση κακοκαιρίας, οι εργασίες θα μετατεθούν για την επόμενη εβδομάδα.", "Anyone who uses medical equipment at home, such as oxygen machines, should contact the council immediately, which will provide generators. In case of bad weather, the works will be postponed to the following week."),
 ],
 "questions": [
  Q("Γιατί θα γίνει η διακοπή ρεύματος;", ["Λόγω βλάβης", "Λόγω εργασιών αναβάθμισης του δικτύου", "Λόγω καύσωνα", "Λόγω απεργίας"], 1, "λόγω εργασιών αναβάθμισης του δικτύου"),
  Q("Τι ζητείται από τους κατοίκους;", ["Να μείνουν στο σπίτι", "Να αποσυνδέσουν τις ευαίσθητες συσκευές", "Να αγοράσουν γεννήτριες", "Να μη χρησιμοποιούν νερό"], 1, "να αποσυνδέσουν τις ευαίσθητες ηλεκτρικές συσκευές"),
  Q("Τι θα κάνει ο δήμος για όσους χρησιμοποιούν ιατρικά μηχανήματα;", ["Θα τους μεταφέρει στο νοσοκομείο", "Θα διαθέσει γεννήτριες", "Θα τους δώσει αποζημίωση", "Θα αναβάλει τις εργασίες"], 1, "ο οποίος θα διαθέσει γεννήτριες"),
 ],
 "gloss": {"διαχειριστής": "διαχειριστής — operator, manager", "δικτύου": "δίκτυο — network, grid", "διακοπή ρεύματος": "διακοπή ρεύματος — power cut", "αναβάθμισης": "αναβάθμιση — upgrade", "να αποσυνδέσουν": "αποσυνδέω — to disconnect, unplug", "συσκευές": "συσκευή — appliance, device", "επανέλθει": "επανέρχομαι — to return, come back", "τάση": "τάση — voltage", "γεννήτριες": "γεννήτρια — generator", "κακοκαιρίας": "κακοκαιρία — bad weather", "θα μετατεθούν": "μετατίθεμαι — to be postponed, moved"},
})

ITEMS.append({
 "id": "l21-vm-odigisi", "title": "Μήνυμα από τη σχολή οδηγών", "title_en": "A message from the driving school", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από μια σχολή οδηγών.",
 "script": [
  L("Εκπαιδευτής", "m", "Γεια σου, Χρυσάνθη, ο Παύλος είμαι από τη σχολή οδηγών. Σε παίρνω γιατί βγήκε η ημερομηνία της εξέτασης για το δίπλωμα: Πέμπτη δεκαεννιά του μήνα, στις εννιά το πρωί. Το θεωρητικό το έχεις ήδη περάσει, οπότε μένει μόνο η πρακτική.", "Hi Chrysanthi, it's Pavlos from the driving school. I'm calling because the date of your licence test has come out: Thursday the nineteenth, at nine in the morning. You've already passed the theory, so only the practical is left."),
  L("Εκπαιδευτής", "m", "Νομίζω ότι θα ήταν καλό να κάνουμε δύο επιπλέον μαθήματα πριν από την εξέταση. Οδηγείς πολύ καλά, αλλά το παρκάρισμα ανάμεσα σε δύο αυτοκίνητα σε αγχώνει ακόμη, και ο εξεταστής σίγουρα θα σου το ζητήσει.", "I think it would be good to do two extra lessons before the test. You drive very well, but parallel parking between two cars still makes you nervous, and the examiner will definitely ask you to do it."),
  L("Εκπαιδευτής", "m", "Μπορώ Δευτέρα και Τρίτη απόγευμα, μετά τις πέντε. Πες μου ποια ώρα σε βολεύει. Και μην ξεχάσεις να φέρεις την ταυτότητά σου την ημέρα της εξέτασης, αλλιώς δεν θα σε αφήσουν να δώσεις.", "I'm free Monday and Tuesday afternoon, after five. Tell me what time suits you. And don't forget to bring your ID on the day of the test, otherwise they won't let you take it."),
 ],
 "questions": [
  Q("Ποια εξέταση της μένει να δώσει;", ["Η θεωρητική", "Η πρακτική", "Και οι δύο", "Η ιατρική"], 1, "οπότε μένει μόνο η πρακτική"),
  Q("Γιατί προτείνει δύο επιπλέον μαθήματα;", ["Γιατί δεν οδηγεί καλά", "Γιατί το παρκάρισμα ανάμεσα σε δύο αυτοκίνητα την αγχώνει ακόμη", "Γιατί άλλαξαν οι κανόνες", "Γιατί η εξέταση είναι νυχτερινή"], 1, "το παρκάρισμα ανάμεσα σε δύο αυτοκίνητα σε αγχώνει ακόμη"),
  Q("Τι πρέπει να φέρει την ημέρα της εξέτασης;", ["Το βιβλίο του ΚΟΚ", "Την ταυτότητά της", "Ένα πιστοποιητικό υγείας", "Χρήματα για το παράβολο"], 1, "μην ξεχάσεις να φέρεις την ταυτότητά σου"),
 ],
 "gloss": {"σχολή οδηγών": "σχολή οδηγών — driving school", "τηλεφωνητή": "τηλεφωνητής — answering machine", "εξέτασης": "εξέταση — test, exam", "δίπλωμα": "δίπλωμα (οδήγησης) — driving licence", "θεωρητικό": "θεωρητικό — theory test", "πρακτική": "πρακτική — practical (test)", "παρκάρισμα": "παρκάρισμα — parking", "αγχώνει": "αγχώνω — to make anxious", "εξεταστής": "εξεταστής — examiner", "βολεύει": "βολεύω — to suit"},
})

ITEMS.append({
 "id": "l21-dia-kanapes", "title": "Ένας καναπές για το σαλόνι", "title_en": "A sofa for the living room", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα κατάστημα επίπλων.",
 "script": [
  L("Πελάτης", "m", "Μας αρέσει πολύ αυτός ο γκρι καναπές, αλλά φοβάμαι ότι είναι λίγο μεγάλος για το σαλόνι μας. Έχουμε μετρήσει τον τοίχο: δύο μέτρα και είκοσι εκατοστά.", "We really like this grey sofa, but I'm afraid it's a bit big for our living room. We've measured the wall: two metres twenty centimetres."),
  L("Πωλήτρια", "f", "Αυτός είναι δύο μέτρα και σαράντα, οπότε δεν χωράει. Το ίδιο μοντέλο όμως υπάρχει και σε τριθέσια έκδοση, δύο μέτρα ακριβώς. Και το ύφασμα βγαίνει, πλένεται στο πλυντήριο· αν έχετε παιδιά ή κατοικίδια, είναι μεγάλο πλεονέκτημα.", "This one is two metres forty, so it won't fit. But the same model also comes as a three-seater, exactly two metres. And the fabric comes off and is machine-washable; if you have children or pets, that's a big advantage."),
  L("Πελάτης", "m", "Έχουμε μια γάτα που τα ξεσκίζει όλα, οπότε αυτό μας ενδιαφέρει. Σε πόσο καιρό μπορεί να παραδοθεί; Και η μεταφορά χρεώνεται;", "We have a cat that shreds everything, so that interests us. How soon can it be delivered? And is delivery charged?"),
  L("Πωλήτρια", "f", "Το τριθέσιο σε αυτό το χρώμα δεν το έχουμε στην αποθήκη· παραγγέλνεται από το εργοστάσιο και φτάνει σε τέσσερις με πέντε εβδομάδες. Η μεταφορά και η ανάβαση στον όροφο είναι δωρεάν, αρκεί να υπάρχει ασανσέρ ή η σκάλα να είναι αρκετά φαρδιά.", "We don't have the three-seater in this colour in the warehouse; it's ordered from the factory and arrives in four to five weeks. Delivery and carrying it up to your floor are free, as long as there's a lift or the staircase is wide enough."),
 ],
 "questions": [
  Q("Γιατί δεν μπορούν να πάρουν τον καναπέ που βλέπουν;", ["Γιατί είναι ακριβός", "Γιατί είναι πολύ μεγάλος για τον τοίχο τους", "Γιατί δεν τους αρέσει το χρώμα", "Γιατί έχει πουληθεί"], 1, "Αυτός είναι δύο μέτρα και σαράντα, οπότε δεν χωράει"),
  Q("Γιατί τους ενδιαφέρει το ύφασμα που πλένεται;", ["Γιατί έχουν μικρά παιδιά", "Γιατί έχουν μια γάτα που τα ξεσκίζει όλα", "Γιατί μένουν δίπλα στη θάλασσα", "Γιατί καπνίζουν"], 1, "Έχουμε μια γάτα που τα ξεσκίζει όλα"),
  Q("Τι ισχύει για την παράδοση;", ["Γίνεται αύριο", "Χρεώνεται ανάλογα με τον όροφο", "Ο καναπές φτάνει σε τέσσερις με πέντε εβδομάδες και η μεταφορά είναι δωρεάν", "Πρέπει να τον πάρουν οι ίδιοι από την αποθήκη"], 2, "φτάνει σε τέσσερις με πέντε εβδομάδες. Η μεταφορά και η ανάβαση στον όροφο είναι δωρεάν"),
 ],
 "gloss": {"επίπλων": "έπιπλο — piece of furniture", "καναπές": "καναπές — sofa", "σαλόνι": "σαλόνι — living room", "εκατοστά": "εκατοστό — centimetre", "χωράει": "χωράω — to fit", "τριθέσια": "τριθέσιος — three-seater", "κατοικίδια": "κατοικίδιο — pet", "πλεονέκτημα": "πλεονέκτημα — advantage", "ξεσκίζει": "ξεσκίζω — to shred, tear apart", "να παραδοθεί": "παραδίδομαι — to be delivered", "αποθήκη": "αποθήκη — warehouse", "εργοστάσιο": "εργοστάσιο — factory", "ανάβαση": "ανάβαση — carrying up, ascent"},
})

ITEMS.append({
 "id": "l21-dia-ktiniatros", "title": "Στον κτηνίατρο", "title_en": "At the vet's", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα κτηνιατρείο.",
 "script": [
  L("Κτηνίατρος", "f", "Λοιπόν, τι συμβαίνει με τον Φίλιππο;", "So, what's the matter with Filippos?"),
  L("Ιδιοκτήτρια", "f", "Από χθες δεν τρώει σχεδόν τίποτα και κρύβεται κάτω από το κρεβάτι. Συνήθως είναι πολύ λαίμαργος, γι' αυτό ανησύχησα. Νομίζω ότι μπορεί να έφαγε κάποιο φυτό από το μπαλκόνι.", "Since yesterday he's hardly eaten anything and he's been hiding under the bed. He's usually very greedy, that's why I got worried. I think he may have eaten some plant from the balcony."),
  L("Κτηνίατρος", "f", "Τι φυτά έχετε; Μερικά, όπως οι κρίνοι, είναι πολύ τοξικά για τις γάτες. Θα του κάνω μια εξέταση αίματος για να δούμε πώς λειτουργούν τα νεφρά του. Μέχρι να βγουν τα αποτελέσματα, θα του δώσουμε ορό για να μην αφυδατωθεί.", "What plants do you have? Some, like lilies, are very toxic for cats. I'll do a blood test to see how his kidneys are working. Until the results come out, we'll give him a drip so he doesn't get dehydrated."),
  L("Ιδιοκτήτρια", "f", "Έχω βασιλικό, λεβάντα και... ναι, μια γλάστρα με κρίνους που μου έκαναν δώρο την περασμένη εβδομάδα.", "I have basil, lavender and... yes, a pot of lilies that someone gave me as a present last week."),
  L("Κτηνίατρος", "f", "Τότε καλά κάνατε που ήρθατε αμέσως. Σε τέτοιες περιπτώσεις ο χρόνος μετράει πολύ. Θα τον κρατήσουμε εδώ απόψε, και τους κρίνους καλύτερα να τους χαρίσετε σε κάποιον που δεν έχει γάτα.", "Then you did well to come straight away. In cases like this time counts a lot. We'll keep him here tonight, and you'd better give the lilies to someone who doesn't have a cat."),
 ],
 "questions": [
  Q("Γιατί ανησύχησε η ιδιοκτήτρια;", ["Γιατί ο γάτος έχει πυρετό", "Γιατί δεν τρώει σχεδόν τίποτα και κρύβεται", "Γιατί χτύπησε στο πόδι", "Γιατί έπεσε από το μπαλκόνι"], 1, "Από χθες δεν τρώει σχεδόν τίποτα και κρύβεται κάτω από το κρεβάτι"),
  Q("Γιατί θα κάνει η κτηνίατρος εξέταση αίματος;", ["Για να δει πώς λειτουργούν τα νεφρά του", "Για να βρει την ηλικία του", "Για να του κάνει εμβόλιο", "Για να δει αν είναι αφυδατωμένος"], 0, "για να δούμε πώς λειτουργούν τα νεφρά του"),
  Q("Ποιο φυτό είναι πιθανότατα η αιτία;", ["Ο βασιλικός", "Η λεβάντα", "Οι κρίνοι", "Το γιασεμί"], 2, "μια γλάστρα με κρίνους"),
 ],
 "gloss": {"κτηνιατρείο": "κτηνιατρείο — vet's surgery", "λαίμαργος": "λαίμαργος — greedy (for food)", "κρίνοι": "κρίνος — lily", "τοξικά": "τοξικός — toxic", "εξέταση αίματος": "εξέταση αίματος — blood test", "νεφρά": "νεφρό — kidney", "ορό": "ορός — drip, saline", "αφυδατωθεί": "αφυδατώνομαι — to become dehydrated", "βασιλικό": "βασιλικός — basil", "λεβάντα": "λεβάντα — lavender", "γλάστρα": "γλάστρα — flowerpot", "να τους χαρίσετε": "χαρίζω — to give away"},
})

ITEMS.append({
 "id": "l21-mon-nea-douleia", "title": "Η πρώτη μέρα στη νέα δουλειά", "title_en": "The first day at a new job", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν νέο άντρα να μιλά σε ένα podcast για την πρώτη του μέρα σε μια καινούργια δουλειά.",
 "script": [
  L("Θοδωρής", "m", "Μετά από οκτώ μήνες ανεργίας και δεκάδες αιτήσεις, με πήραν επιτέλους σε μια εταιρεία λογισμικού στη Θεσσαλονίκη. Το προηγούμενο βράδυ δεν έκλεισα μάτι. Είχα σιδερώσει τρία πουκάμισα και δεν μπορούσα να αποφασίσω ποιο θα φορέσω.", "After eight months of unemployment and dozens of applications, I was finally hired by a software company in Thessaloniki. The night before, I didn't sleep a wink. I had ironed three shirts and couldn't decide which one to wear."),
  L("Θοδωρής", "m", "Όταν έφτασα, ανακάλυψα ότι όλοι φορούσαν τζιν και φούτερ. Η προϊσταμένη μου γέλασε και μου είπε ότι το μόνο ντύσιμο που απαγορεύεται εκεί είναι η γραβάτα. Μου έδωσαν έναν φορητό υπολογιστή, μου έδειξαν πού είναι η κουζίνα και μου σύστησαν έναν συνάδελφο, τον Άρη, που θα ήταν ο «μέντοράς» μου τους πρώτους μήνες.", "When I arrived, I discovered everyone was wearing jeans and hoodies. My manager laughed and told me the only clothing forbidden there is a tie. They gave me a laptop, showed me where the kitchen is and introduced me to a colleague, Aris, who would be my 'mentor' for the first few months."),
  L("Θοδωρής", "m", "Το πιο σημαντικό, όμως, έγινε το μεσημέρι. Ο Άρης μού είπε: «Εδώ κανείς δεν περιμένει να τα ξέρεις όλα. Περιμένουμε να ρωτάς.» Μου πήρε χρόνια να καταλάβω πόσο σοφή ήταν αυτή η φράση.", "The most important thing, though, happened at midday. Aris told me: 'Nobody here expects you to know everything. We expect you to ask.' It took me years to understand how wise that phrase was."),
 ],
 "questions": [
  Q("Πώς ένιωθε ο Θοδωρής το προηγούμενο βράδυ;", ["Ήρεμος", "Τόσο αγχωμένος που δεν κοιμήθηκε", "Κουρασμένος από τη μετακόμιση", "Απογοητευμένος"], 1, "Το προηγούμενο βράδυ δεν έκλεισα μάτι"),
  Q("Τι ανακάλυψε όταν έφτασε στη δουλειά;", ["Ότι όλοι φορούσαν κοστούμια", "Ότι όλοι φορούσαν τζιν και φούτερ", "Ότι είχε αργήσει", "Ότι δεν τον περίμεναν"], 1, "ανακάλυψα ότι όλοι φορούσαν τζιν και φούτερ"),
  Q("Ποια συμβουλή του έδωσε ο Άρης;", ["Να δουλεύει μέχρι αργά", "Να μη μιλάει πολύ στις συσκέψεις", "Να ρωτάει, γιατί κανείς δεν περιμένει να τα ξέρει όλα", "Να φοράει πάντα γραβάτα"], 2, "Εδώ κανείς δεν περιμένει να τα ξέρεις όλα. Περιμένουμε να ρωτάς"),
 ],
 "gloss": {"ανεργίας": "ανεργία — unemployment", "αιτήσεις": "αίτηση — application", "λογισμικού": "λογισμικό — software", "δεν έκλεισα μάτι": "δεν κλείνω μάτι — not to sleep a wink", "σιδερώσει": "σιδερώνω — to iron", "φούτερ": "φούτερ — sweatshirt, hoodie", "προϊσταμένη": "προϊσταμένη — (female) manager", "ντύσιμο": "ντύσιμο — way of dressing, clothes", "γραβάτα": "γραβάτα — tie", "φορητό υπολογιστή": "φορητός υπολογιστής — laptop", "σύστησαν": "συστήνω — to introduce", "σοφή": "σοφός — wise"},
})

ITEMS.append({
 "id": "l21-rep-plastira", "title": "Η λίμνη Πλαστήρα", "title_en": "Lake Plastiras", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από τη λίμνη Πλαστήρα, στον νομό Καρδίτσας.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε υψόμετρο περίπου οκτακοσίων μέτρων, ανάμεσα σε έλατα και καστανιές, απλώνεται μια λίμνη που μοιάζει να βγήκε από καρτ ποστάλ της Ελβετίας. Κι όμως, η λίμνη Πλαστήρα είναι τεχνητή: δημιουργήθηκε στα τέλη της δεκαετίας του 1950, όταν χτίστηκε ένα φράγμα στον ποταμό Ταυρωπό.", "At an altitude of about eight hundred metres, among firs and chestnut trees, lies a lake that looks as if it came off a Swiss postcard. And yet Lake Plastiras is artificial: it was created at the end of the 1950s, when a dam was built on the river Tavropos."),
  L("Ρεπόρτερ", "m", "Πήρε το όνομά της από τον στρατηγό και πρωθυπουργό Νικόλαο Πλαστήρα, ο οποίος είχε οραματιστεί το έργο ήδη από τη δεκαετία του 1920, για να δοθεί νερό στον θεσσαλικό κάμπο και ηλεκτρικό ρεύμα στην περιοχή.", "It took its name from the general and prime minister Nikolaos Plastiras, who had envisioned the project as early as the 1920s, to provide water for the Thessalian plain and electricity for the area."),
  L("Ρεπόρτερ", "m", "Σήμερα η λίμνη έχει γίνει δημοφιλής προορισμός όλο τον χρόνο. Τον χειμώνα οι επισκέπτες έρχονται για τα τζάκια και τα χιονισμένα τοπία, το καλοκαίρι για κανό, ιππασία και ποδήλατο. Οι κάτοικοι των γύρω χωριών, που κάποτε ζούσαν μόνο από την κτηνοτροφία, ανοίγουν ξενώνες και ταβέρνες. Ανησυχούν όμως για τις χρονιές λειψυδρίας, όταν η στάθμη του νερού πέφτει επικίνδυνα.", "Today the lake has become a popular destination all year round. In winter visitors come for the fireplaces and snowy landscapes, in summer for canoeing, horse riding and cycling. The residents of the surrounding villages, who once lived only from livestock farming, are opening guesthouses and tavernas. But they worry about years of drought, when the water level falls dangerously."),
 ],
 "questions": [
  Q("Πώς δημιουργήθηκε η λίμνη;", ["Από έναν σεισμό", "Με ένα φράγμα στον ποταμό Ταυρωπό", "Από το λιώσιμο των χιονιών", "Από μια πηγή"], 1, "όταν χτίστηκε ένα φράγμα στον ποταμό Ταυρωπό"),
  Q("Για ποιους λόγους είχε οραματιστεί ο Πλαστήρας το έργο;", ["Για τον τουρισμό", "Για νερό στον κάμπο και ηλεκτρικό ρεύμα", "Για την αλιεία", "Για την άμυνα της χώρας"], 1, "για να δοθεί νερό στον θεσσαλικό κάμπο και ηλεκτρικό ρεύμα στην περιοχή"),
  Q("Τι ανησυχεί τους κατοίκους;", ["Οι πολλοί τουρίστες", "Η πτώση της στάθμης του νερού στις χρονιές λειψυδρίας", "Οι πλημμύρες", "Η έλλειψη δρόμων"], 1, "Ανησυχούν όμως για τις χρονιές λειψυδρίας"),
 ],
 "gloss": {"υψόμετρο": "υψόμετρο — altitude", "έλατα": "έλατο — fir tree", "καστανιές": "καστανιά — chestnut tree", "τεχνητή": "τεχνητός — artificial", "φράγμα": "φράγμα — dam", "πρωθυπουργό": "πρωθυπουργός — prime minister", "είχε οραματιστεί": "οραματίζομαι — to envision", "κάμπο": "κάμπος — plain", "τζάκια": "τζάκι — fireplace", "ιππασία": "ιππασία — horse riding", "κτηνοτροφία": "κτηνοτροφία — livestock farming", "ξενώνες": "ξενώνας — guesthouse", "λειψυδρίας": "λειψυδρία — water shortage, drought", "στάθμη": "στάθμη — level"},
})

ITEMS.append({
 "id": "l21-rep-olympos", "title": "Όλυμπος Καρπάθου", "title_en": "Olympos, Karpathos", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από την Όλυμπο, ένα ορεινό χωριό της Καρπάθου.",
 "script": [
  L("Ρεπόρτερ", "f", "Το χωριό είναι χτισμένο στην κορυφή ενός βουνού, με τα χρωματιστά του σπίτια να κατεβαίνουν σαν σκαλοπάτια προς τη θάλασσα. Για αιώνες ήταν σχεδόν απομονωμένο, και ο δρόμος που το ενώνει με την υπόλοιπη Κάρπαθο είναι σχετικά πρόσφατος.", "The village is built on the top of a mountain, with its coloured houses going down like steps towards the sea. For centuries it was almost isolated, and the road that connects it to the rest of Karpathos is relatively recent."),
  L("Ρεπόρτερ", "f", "Ίσως γι' αυτό η Όλυμπος έχει διατηρήσει έθιμα που αλλού έχουν χαθεί. Αρκετές ηλικιωμένες γυναίκες φορούν ακόμη καθημερινά την παραδοσιακή φορεσιά, με κεντημένα μαντίλια και δερμάτινες μπότες. Η τοπική διάλεκτος έχει λέξεις και προφορές που ενθουσιάζουν τους γλωσσολόγους.", "Perhaps that's why Olympos has kept customs that have been lost elsewhere. Several elderly women still wear the traditional costume every day, with embroidered headscarves and leather boots. The local dialect has words and pronunciations that delight linguists."),
  L("Ρεπόρτερ", "f", "Στα πανηγύρια, οι άντρες τραγουδούν «μαντινάδες», στίχους που αυτοσχεδιάζουν επί τόπου, συνοδεία λύρας και τσαμπούνας. Ο τουρισμός έφερε χρήματα, αλλά και ένα δίλημμα: πώς θα μείνει ζωντανή η παράδοση χωρίς να μετατραπεί σε θέαμα για τους επισκέπτες;", "At festivals, the men sing 'mantinades', verses they improvise on the spot, accompanied by the lyra and the tsambouna. Tourism has brought money, but also a dilemma: how can the tradition stay alive without turning into a show for visitors?"),
 ],
 "questions": [
  Q("Γιατί, σύμφωνα με τη ρεπόρτερ, η Όλυμπος διατήρησε τα έθιμά της;", ["Γιατί έχει πολλούς κατοίκους", "Γιατί για αιώνες ήταν σχεδόν απομονωμένη", "Γιατί το απαγόρευσε ο δήμος", "Γιατί δεν έχει θάλασσα"], 1, "Για αιώνες ήταν σχεδόν απομονωμένο"),
  Q("Τι φορούν ακόμη καθημερινά αρκετές ηλικιωμένες γυναίκες;", ["Μαύρα ρούχα", "Την παραδοσιακή φορεσιά", "Ρούχα από την Αθήνα", "Στολές χορού"], 1, "φορούν ακόμη καθημερινά την παραδοσιακή φορεσιά"),
  Q("Ποιο δίλημμα έφερε ο τουρισμός;", ["Πώς θα χτιστούν περισσότερα ξενοδοχεία", "Πώς θα μείνει ζωντανή η παράδοση χωρίς να γίνει θέαμα", "Αν πρέπει να κλείσει ο δρόμος", "Αν πρέπει να διδάσκεται η διάλεκτος"], 1, "πώς θα μείνει ζωντανή η παράδοση χωρίς να μετατραπεί σε θέαμα για τους επισκέπτες"),
 ],
 "gloss": {"χρωματιστά": "χρωματιστός — coloured", "απομονωμένο": "απομονωμένος — isolated", "έθιμα": "έθιμο — custom", "φορεσιά": "φορεσιά — costume, dress", "κεντημένα": "κεντημένος — embroidered", "μαντίλια": "μαντίλι — headscarf", "διάλεκτος": "διάλεκτος — dialect", "γλωσσολόγους": "γλωσσολόγος — linguist", "πανηγύρια": "πανηγύρι — village festival", "αυτοσχεδιάζουν": "αυτοσχεδιάζω — to improvise", "επί τόπου": "επί τόπου — on the spot", "τσαμπούνας": "τσαμπούνα — tsambouna (island bagpipe)", "δίλημμα": "δίλημμα — dilemma", "θέαμα": "θέαμα — spectacle, show"},
})

ITEMS.append({
 "id": "l21-int-ekav", "title": "Οδηγός ασθενοφόρου", "title_en": "An ambulance driver", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια διασώστρια που οδηγεί ασθενοφόρο σε μια μεγάλη πόλη.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσα χρόνια κάνετε αυτή τη δουλειά;", "How many years have you been doing this job?"),
  L("Διασώστρια", "f", "Δεκαπέντε. Ξεκίνησα στα είκοσι πέντε, και ακόμη θυμάμαι το πρώτο μου περιστατικό: ένας ηλικιωμένος με έμφραγμα σε έναν πέμπτο όροφο χωρίς ασανσέρ. Τον κατεβάσαμε με το φορείο από τις σκάλες. Επέζησε, και μας έστειλε ένα κουτί γλυκά στον σταθμό.", "Fifteen. I started at twenty-five, and I still remember my first call-out: an elderly man with a heart attack on a fifth floor without a lift. We carried him down the stairs on the stretcher. He survived, and sent us a box of sweets at the station."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το μεγαλύτερο πρόβλημα στη δουλειά σας;", "What's the biggest problem in your job?"),
  L("Διασώστρια", "f", "Η κίνηση και οι οδηγοί που δεν κάνουν χώρο. Πολλοί πανικοβάλλονται όταν ακούν τη σειρήνα και σταματούν στη μέση του δρόμου. Το σωστό είναι να πηγαίνετε δεξιά και να επιβραδύνετε. Κάθε λεπτό που χάνουμε μπορεί να κοστίσει μια ζωή.", "Traffic, and drivers who don't make room. Many panic when they hear the siren and stop in the middle of the road. The right thing is to move to the right and slow down. Every minute we lose can cost a life."),
  L("Διασώστρια", "f", "Και κάτι ακόμα: δεν είμαστε ήρωες. Είμαστε άνθρωποι που κουράζονται και φοβούνται, αλλά κάνουν αυτό που πρέπει. Το χειρότερο δεν είναι οι νυχτερινές βάρδιες· είναι οι περιπτώσεις που, όσο κι αν προσπαθήσεις, φτάνεις αργά.", "And one more thing: we're not heroes. We're people who get tired and afraid but do what has to be done. The worst thing isn't the night shifts; it's the cases where, however hard you try, you arrive too late."),
 ],
 "questions": [
  Q("Τι θυμάται από το πρώτο της περιστατικό;", ["Ότι ο ασθενής δεν επέζησε", "Ότι κατέβασαν τον ασθενή με το φορείο από τις σκάλες και εκείνος επέζησε", "Ότι το ασθενοφόρο χάλασε", "Ότι ήταν ένα τροχαίο"], 1, "Τον κατεβάσαμε με το φορείο από τις σκάλες. Επέζησε"),
  Q("Τι πρέπει να κάνουν οι οδηγοί όταν ακούν τη σειρήνα;", ["Να σταματούν στη μέση του δρόμου", "Να πηγαίνουν δεξιά και να επιβραδύνουν", "Να αυξάνουν ταχύτητα", "Να ανάβουν τα φώτα"], 1, "Το σωστό είναι να πηγαίνετε δεξιά και να επιβραδύνετε"),
  Q("Τι θεωρεί το χειρότερο στη δουλειά της;", ["Τις νυχτερινές βάρδιες", "Τον χαμηλό μισθό", "Τις περιπτώσεις που φτάνει αργά", "Τους θυμωμένους συγγενείς"], 2, "είναι οι περιπτώσεις που, όσο κι αν προσπαθήσεις, φτάνεις αργά"),
 ],
 "gloss": {"διασώστρια": "διασώστρια — (female) paramedic", "ασθενοφόρο": "ασθενοφόρο — ambulance", "περιστατικό": "περιστατικό — case, call-out", "έμφραγμα": "έμφραγμα — heart attack", "φορείο": "φορείο — stretcher", "Επέζησε": "επιζώ — to survive", "πανικοβάλλονται": "πανικοβάλλομαι — to panic", "σειρήνα": "σειρήνα — siren", "να επιβραδύνετε": "επιβραδύνω — to slow down", "ήρωες": "ήρωας — hero", "βάρδιες": "βάρδια — shift"},
})

ITEMS.append({
 "id": "l21-mon-filiki", "title": "Η Φιλική Εταιρεία", "title_en": "The Filiki Etaireia (Society of Friends)", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη ιστορίας για την προετοιμασία της Επανάστασης του 1821.",
 "script": [
  L("Ιστορικός", "m", "Το 1814, στην Οδησσό, τρεις άγνωστοι έμποροι, ο Νικόλαος Σκουφάς, ο Αθανάσιος Τσακάλωφ και ο Εμμανουήλ Ξάνθος, ίδρυσαν μια μυστική οργάνωση με στόχο την απελευθέρωση των Ελλήνων. Την ονόμασαν Φιλική Εταιρεία. Κανείς τους δεν ήταν πλούσιος ή διάσημος· αυτό ακριβώς τους επέτρεψε να δρουν χωρίς να προκαλούν υποψίες.", "In 1814, in Odessa, three unknown merchants, Nikolaos Skoufas, Athanasios Tsakalof and Emmanouil Xanthos, founded a secret organisation aimed at the liberation of the Greeks. They called it the Filiki Etaireia. None of them was rich or famous; precisely this allowed them to act without arousing suspicion."),
  L("Ιστορικός", "m", "Η οργάνωση είχε αυστηρή ιεραρχία και τελετουργίες μύησης, εμπνευσμένες εν μέρει από τους τεκτονικούς κύκλους της εποχής. Τα νέα μέλη ορκίζονταν μυστικότητα και συχνά δεν ήξεραν ποιος βρισκόταν στην κορυφή. Οι ιδρυτές καλλιέργησαν σκόπιμα τη φήμη ότι πίσω από την Εταιρεία βρισκόταν η Ρωσία, κάτι που έπειθε πολλούς διστακτικούς να προσχωρήσουν.", "The organisation had a strict hierarchy and initiation rituals, partly inspired by the Masonic circles of the time. New members swore secrecy and often didn't know who was at the top. The founders deliberately cultivated the rumour that Russia was behind the Society, which persuaded many hesitant people to join."),
  L("Ιστορικός", "m", "Μέσα σε λίγα χρόνια, η Εταιρεία απλώθηκε από τη Μολδοβλαχία ως την Πελοπόννησο και τα νησιά, και μύησε προκρίτους, κληρικούς, εμπόρους και οπλαρχηγούς. Το 1820 την ηγεσία ανέλαβε ο Αλέξανδρος Υψηλάντης, αξιωματικός του ρωσικού στρατού, και τον Φεβρουάριο του 1821 πέρασε τον Προύθο ποταμό, ξεκινώντας την Επανάσταση.", "Within a few years the Society spread from the Danubian Principalities to the Peloponnese and the islands, and initiated notables, clergy, merchants and armed chieftains. In 1820 the leadership was taken over by Alexandros Ypsilantis, an officer in the Russian army, and in February 1821 he crossed the river Prut, starting the Revolution."),
  L("Ιστορικός", "m", "Αυτό που μου φαίνεται αξιοσημείωτο είναι ότι μια επανάσταση που άλλαξε τον χάρτη της Ευρώπης ξεκίνησε όχι από στρατηγούς ή βασιλιάδες, αλλά από τρεις μικρέμπορους σε ένα λιμάνι της Μαύρης Θάλασσας.", "What strikes me as remarkable is that a revolution which changed the map of Europe was started not by generals or kings, but by three small traders in a Black Sea port."),
 ],
 "questions": [
  Q("Γιατί, κατά τον ιστορικό, βοήθησε το ότι οι ιδρυτές ήταν άγνωστοι;", ["Γιατί είχαν περισσότερο χρόνο", "Γιατί μπορούσαν να δρουν χωρίς να προκαλούν υποψίες", "Γιατί δεν είχαν οικογένειες", "Γιατί δεν πλήρωναν φόρους"], 1, "αυτό ακριβώς τους επέτρεψε να δρουν χωρίς να προκαλούν υποψίες"),
  Q("Ποια φήμη καλλιέργησαν σκόπιμα οι ιδρυτές;", ["Ότι η Εταιρεία είχε τεράστια περιουσία", "Ότι πίσω από την Εταιρεία βρισκόταν η Ρωσία", "Ότι ο αρχηγός ήταν ο πατριάρχης", "Ότι η Αγγλία θα έστελνε στόλο"], 1, "πίσω από την Εταιρεία βρισκόταν η Ρωσία"),
  Q("Ποιοι μυήθηκαν στην Εταιρεία;", ["Μόνο έμποροι της Οδησσού", "Πρόκριτοι, κληρικοί, έμποροι και οπλαρχηγοί", "Μόνο αξιωματικοί του ρωσικού στρατού", "Μόνο φοιτητές"], 1, "μύησε προκρίτους, κληρικούς, εμπόρους και οπλαρχηγούς"),
  Q("Τι θεωρεί αξιοσημείωτο ο ιστορικός;", ["Ότι η Επανάσταση ξεκίνησε στην Πελοπόννησο", "Ότι η Επανάσταση ξεκίνησε από τρεις μικρέμπορους", "Ότι η Ρωσία βοήθησε την Επανάσταση", "Ότι η Εταιρεία διαλύθηκε γρήγορα"], 1, "ξεκίνησε όχι από στρατηγούς ή βασιλιάδες, αλλά από τρεις μικρέμπορους"),
 ],
 "gloss": {"μυστική": "μυστικός — secret", "απελευθέρωση": "απελευθέρωση — liberation", "υποψίες": "υποψία — suspicion", "ιεραρχία": "ιεραρχία — hierarchy", "τελετουργίες μύησης": "τελετουργία μύησης — initiation ritual", "τεκτονικούς": "τεκτονικός — Masonic", "ορκίζονταν": "ορκίζομαι — to swear (an oath)", "καλλιέργησαν": "καλλιεργώ — to cultivate, foster", "διστακτικούς": "διστακτικός — hesitant", "να προσχωρήσουν": "προσχωρώ — to join", "προκρίτους": "πρόκριτος — local notable", "κληρικούς": "κληρικός — cleric", "οπλαρχηγούς": "οπλαρχηγός — armed chieftain", "αξιοσημείωτο": "αξιοσημείωτος — remarkable", "μικρέμπορους": "μικρέμπορος — small trader"},
})

ITEMS.append({
 "id": "l21-int-poli15", "title": "Η πόλη των δεκαπέντε λεπτών", "title_en": "The fifteen-minute city", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια πολεοδόμο για την ιδέα της «πόλης των δεκαπέντε λεπτών».",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς σημαίνει «πόλη των δεκαπέντε λεπτών»;", "What exactly does 'fifteen-minute city' mean?"),
  L("Πολεοδόμος", "f", "Είναι μια ιδέα σύμφωνα με την οποία κάθε κάτοικος πρέπει να μπορεί να φτάσει με τα πόδια ή με το ποδήλατο, μέσα σε ένα τέταρτο, σε ό,τι χρειάζεται καθημερινά: σχολείο, φαρμακείο, σούπερ μάρκετ, πάρκο, ίσως και τη δουλειά του. Δεν είναι κάτι εντελώς καινούργιο· έτσι λειτουργούσαν οι παραδοσιακές γειτονιές πριν το αυτοκίνητο κυριαρχήσει.", "It's an idea according to which every resident should be able to reach by foot or by bike, within a quarter of an hour, everything they need every day: school, pharmacy, supermarket, park, perhaps even their work. It's not something entirely new; that's how traditional neighbourhoods worked before the car took over."),
  L("Δημοσιογράφος", "m", "Υπάρχουν όμως και αντιδράσεις. Κάποιοι τη βλέπουν ως περιορισμό της ελευθερίας τους.", "But there are also objections. Some see it as a restriction of their freedom."),
  L("Πολεοδόμος", "f", "Κατανοώ την ανησυχία, αλλά πρόκειται για παρεξήγηση. Κανείς δεν απαγορεύει σε κανέναν να πάει όπου θέλει. Ο στόχος είναι να μη χρειάζεται να μπεις στο αυτοκίνητο για να αγοράσεις ψωμί. Το πραγματικό ζήτημα είναι άλλο: αν οι υπηρεσίες συγκεντρωθούν μόνο στις ευκατάστατες γειτονιές, η ιδέα μπορεί να βαθύνει τις ανισότητες αντί να τις μειώσει.", "I understand the concern, but it's a misunderstanding. Nobody forbids anyone to go wherever they want. The aim is that you shouldn't need to get into a car to buy bread. The real issue is a different one: if services are concentrated only in well-off neighbourhoods, the idea may deepen inequalities instead of reducing them."),
  L("Πολεοδόμος", "f", "Για την Αθήνα, με τις πυκνές της γειτονιές και τα μικρά καταστήματα στο ισόγειο των πολυκατοικιών, έχουμε ήδη ένα μεγάλο πλεονέκτημα. Αυτό που λείπει είναι οι ασφαλείς διαδρομές για πεζούς και οι χώροι πρασίνου.", "For Athens, with its dense neighbourhoods and small shops on the ground floor of apartment buildings, we already have a big advantage. What's missing is safe routes for pedestrians and green spaces."),
 ],
 "questions": [
  Q("Τι σημαίνει, σύμφωνα με την πολεοδόμο, η «πόλη των δεκαπέντε λεπτών»;", ["Ότι οι συγκοινωνίες περνούν κάθε δεκαπέντε λεπτά", "Ότι κάθε κάτοικος φτάνει με τα πόδια ή με ποδήλατο σε ό,τι χρειάζεται μέσα σε ένα τέταρτο", "Ότι απαγορεύεται το αυτοκίνητο", "Ότι η διαδρομή για τη δουλειά πρέπει να είναι σύντομη"], 1, "κάθε κάτοικος πρέπει να μπορεί να φτάσει με τα πόδια ή με το ποδήλατο, μέσα σε ένα τέταρτο"),
  Q("Πώς απαντά στην κριτική ότι η ιδέα περιορίζει την ελευθερία;", ["Συμφωνεί με την κριτική", "Λέει ότι είναι παρεξήγηση, γιατί κανείς δεν απαγορεύει τίποτα", "Λέει ότι η ελευθερία δεν είναι σημαντική", "Δεν απαντά"], 1, "πρόκειται για παρεξήγηση. Κανείς δεν απαγορεύει σε κανέναν να πάει όπου θέλει"),
  Q("Ποιο είναι, κατά τη γνώμη της, το πραγματικό ζήτημα;", ["Το κόστος των έργων", "Ότι οι υπηρεσίες μπορεί να συγκεντρωθούν στις ευκατάστατες γειτονιές και να βαθύνουν τις ανισότητες", "Η αντίδραση των οδηγών ταξί", "Η έλλειψη ποδηλάτων"], 1, "η ιδέα μπορεί να βαθύνει τις ανισότητες αντί να τις μειώσει"),
  Q("Τι λείπει από την Αθήνα;", ["Τα μικρά καταστήματα", "Οι πυκνές γειτονιές", "Οι ασφαλείς διαδρομές για πεζούς και οι χώροι πρασίνου", "Τα σχολεία"], 2, "Αυτό που λείπει είναι οι ασφαλείς διαδρομές για πεζούς και οι χώροι πρασίνου"),
 ],
 "gloss": {"πολεοδόμο": "πολεοδόμος — urban planner", "τέταρτο": "τέταρτο — quarter (of an hour)", "κυριαρχήσει": "κυριαρχώ — to dominate", "αντιδράσεις": "αντίδραση — reaction, objection", "περιορισμό": "περιορισμός — restriction", "παρεξήγηση": "παρεξήγηση — misunderstanding", "συγκεντρωθούν": "συγκεντρώνομαι — to be concentrated", "ευκατάστατες": "ευκατάστατος — well-off", "να βαθύνει": "βαθαίνω — to deepen", "ανισότητες": "ανισότητα — inequality", "πυκνές": "πυκνός — dense", "πεζούς": "πεζός — pedestrian", "χώροι πρασίνου": "χώρος πρασίνου — green space"},
})

rnd = random.Random(21)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-21.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
