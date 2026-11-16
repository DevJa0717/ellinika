# Source for library/listening/listening-83.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l83.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l83-ann-kokkini-simaia", "title": "Κόκκινη σημαία στην παραλία", "title_en": "Red flag on the beach", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε μια οργανωμένη παραλία. Από τα μεγάφωνα του πύργου ναυαγοσωστών ακούτε μια ανακοίνωση.",
 "script": [
  L("Ναυαγοσώστης", "m", "Προσοχή, παρακαλώ. Λόγω των ισχυρών βοριάδων, από αυτή τη στιγμή στον πύργο έχει υψωθεί κόκκινη σημαία. Αυτό σημαίνει ότι το κολύμπι απαγορεύεται σε όλη την παραλία. Παρακαλούνται όλοι οι λουόμενοι να βγουν αμέσως από το νερό.", "Attention, please. Because of the strong northerly winds, a red flag has now been raised on the tower. This means swimming is forbidden along the whole beach. All bathers are asked to leave the water immediately."),
  L("Ναυαγοσώστης", "m", "Υπάρχουν επικίνδυνα ρεύματα κοντά στους βράχους, στο δεξί άκρο της παραλίας. Ακόμη και οι έμπειροι κολυμβητές δεν πρέπει να μπουν στη θάλασσα. Επίσης, απαγορεύονται τα φουσκωτά στρώματα και τα κανό μέχρι νεωτέρας.", "There are dangerous currents near the rocks, at the right-hand end of the beach. Even experienced swimmers must not go into the sea. Inflatable mattresses and canoes are also forbidden until further notice."),
  L("Ναυαγοσώστης", "m", "Τέλος, ένα μικρό αγόρι, περίπου έξι χρονών, με κίτρινο μαγιό, βρίσκεται μαζί μας στον πύργο. Λέγεται Στέλιος. Οι γονείς του παρακαλούνται να έρθουν να τον παραλάβουν. Ευχαριστούμε.", "Finally, a little boy, about six years old, in yellow swimming trunks, is with us at the tower. His name is Stelios. His parents are asked to come and collect him. Thank you."),
 ],
 "questions": [
  Q("Γιατί υψώθηκε κόκκινη σημαία;", ["Λόγω μεδουσών", "Λόγω ισχυρών βοριάδων", "Λόγω ρύπανσης", "Λόγω ενός ατυχήματος"], 1, "Λόγω των ισχυρών βοριάδων"),
  Q("Πού υπάρχουν επικίνδυνα ρεύματα;", ["Στη μέση της παραλίας", "Κοντά στο λιμανάκι", "Κοντά στους βράχους, στο δεξί άκρο", "Πίσω από τις σημαδούρες"], 2, "κοντά στους βράχους, στο δεξί άκρο της παραλίας"),
  Q("Τι ζητείται από τους γονείς του Στέλιου;", ["Να τον φωνάξουν από τη θάλασσα", "Να έρθουν να τον παραλάβουν από τον πύργο", "Να του φέρουν ένα μαγιό", "Να τηλεφωνήσουν στην αστυνομία"], 1, "Οι γονείς του παρακαλούνται να έρθουν να τον παραλάβουν"),
 ],
 "gloss": {"ναυαγοσωστών": "ναυαγοσώστης — lifeguard", "βοριάδων": "βοριάς — north wind", "υψωθεί": "υψώνομαι — to be raised", "λουόμενοι": "λουόμενος — bather", "ρεύματα": "ρεύμα — current", "φουσκωτά στρώματα": "φουσκωτό στρώμα — inflatable mattress", "μέχρι νεωτέρας": "μέχρι νεωτέρας — until further notice", "μαγιό": "μαγιό — swimsuit, swimming trunks", "παραλάβουν": "παραλαμβάνω — to collect, pick up"},
})
ITEMS.append({
 "id": "l83-vm-kataskinosi", "title": "Μήνυμα από την κατασκήνωση", "title_en": "Voicemail from the summer camp", "type": "voicemail", "level": "B2",
 "context_el": "Η κόρη σας θα πάει σε μια παιδική κατασκήνωση. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Βάσω", "f", "Καλημέρα σας, είμαι η Βάσω, η υπεύθυνη της κατασκήνωσης «Τα Έλατα». Σας τηλεφωνώ για τη Μυρτώ, που ξεκινάει την πρώτη περίοδο. Το πούλμαν θα φύγει την Κυριακή στις οχτώ το πρωί από τον σταθμό Λαρίσης. Η επιβίβαση αρχίζει στις εφτάμισι.", "Good morning, this is Vaso, the director of the 'Fir Trees' camp. I'm calling about Myrto, who starts in the first session. The coach will leave on Sunday at eight in the morning from Larissis station. Boarding starts at half past seven."),
  L("Βάσω", "f", "Στη λίστα με τα πράγματα που σας στείλαμε ξεχάσαμε να γράψουμε έναν φακό και ένα ζευγάρι κλειστά παπούτσια για την πεζοπορία. Σας θυμίζω επίσης ότι τα κινητά τηλέφωνα δεν επιτρέπονται· τα παιδιά μπορούν να σας τηλεφωνούν από το γραφείο κάθε Τετάρτη και Σάββατο το απόγευμα.", "On the list of things we sent you we forgot to include a torch and a pair of closed shoes for the hike. I also remind you that mobile phones are not allowed; the children can phone you from the office every Wednesday and Saturday afternoon."),
  L("Βάσω", "f", "Τέλος, δεν έχουμε λάβει ακόμα τη βεβαίωση του παιδιάτρου. Χωρίς αυτήν δεν μπορούμε να δεχτούμε τη Μυρτώ, οπότε στείλτε τη μας με email μέχρι την Παρασκευή. Ευχαριστώ, καλή σας μέρα.", "Finally, we haven't yet received the paediatrician's certificate. Without it we can't accept Myrto, so please email it to us by Friday. Thank you, have a nice day."),
 ],
 "questions": [
  Q("Τι ώρα αρχίζει η επιβίβαση στο πούλμαν;", ["Στις εφτά", "Στις εφτάμισι", "Στις οχτώ", "Στις οχτώμισι"], 1, "Η επιβίβαση αρχίζει στις εφτάμισι"),
  Q("Τι ξέχασαν να γράψουν στη λίστα;", ["Ένα μαγιό και μια πετσέτα", "Έναν φακό και κλειστά παπούτσια", "Ένα αντηλιακό και ένα καπέλο", "Έναν υπνόσακο"], 1, "έναν φακό και ένα ζευγάρι κλειστά παπούτσια"),
  Q("Τι πρέπει να στείλουν οι γονείς μέχρι την Παρασκευή;", ["Την πληρωμή", "Μια φωτογραφία", "Τη βεβαίωση του παιδιάτρου", "Τον αριθμό του κινητού τους"], 2, "δεν έχουμε λάβει ακόμα τη βεβαίωση του παιδιάτρου"),
 ],
 "gloss": {"κατασκήνωση": "κατασκήνωση — summer camp", "υπεύθυνη": "υπεύθυνος — person in charge, director", "περίοδο": "περίοδος — session, period", "πούλμαν": "πούλμαν — coach", "επιβίβαση": "επιβίβαση — boarding", "φακό": "φακός — torch, flashlight", "πεζοπορία": "πεζοπορία — hike", "βεβαίωση": "βεβαίωση — certificate", "παιδιάτρου": "παιδίατρος — paediatrician"},
})
ITEMS.append({
 "id": "l83-dia-kranos", "title": "Ένα κράνος για το πατίνι", "title_en": "A helmet for the scooter", "type": "dialogue", "level": "B2",
 "context_el": "Σε ένα κατάστημα αθλητικών ειδών, ένας πελάτης ζητάει ένα κράνος.",
 "script": [
  L("Πελάτης", "m", "Καλησπέρα. Ψάχνω ένα κράνος για ηλεκτρικό πατίνι. Το χρησιμοποιώ κάθε μέρα για να πηγαίνω στη δουλειά.", "Good evening. I'm looking for a helmet for an electric scooter. I use it every day to get to work."),
  L("Πωλήτρια", "f", "Μάλιστα. Αν πηγαίνετε στη δουλειά, σας προτείνω αυτό εδώ. Έχει ενσωματωμένο φως στο πίσω μέρος, ώστε να σας βλέπουν τα αυτοκίνητα το βράδυ, και είναι πιστοποιημένο και για ηλεκτρικά πατίνια, όχι μόνο για ποδήλατα.", "Right. If you're commuting, I'd suggest this one. It has a built-in light at the back, so cars can see you at night, and it's certified for electric scooters too, not only for bicycles."),
  L("Πελάτης", "m", "Ωραίο. Πόσο κάνει;", "Nice. How much is it?"),
  L("Πωλήτρια", "f", "Ογδόντα πέντε ευρώ. Υπάρχει κι ένα φθηνότερο, στα σαράντα, αλλά δεν έχει φως και είναι πιο βαρύ. Πρώτα όμως πρέπει να βρούμε το σωστό μέγεθος. Επιτρέψτε μου να μετρήσω την περίμετρο του κεφαλιού σας.", "Eighty-five euros. There's also a cheaper one, at forty, but it has no light and it's heavier. But first we need to find the right size. Let me measure the circumference of your head."),
  L("Πελάτης", "m", "Βεβαίως. Και αν πέσω κάποια στιγμή; Μπορώ να το συνεχίσω να το φοράω;", "Of course. And if I fall at some point? Can I keep wearing it?"),
  L("Πωλήτρια", "f", "Όχι. Μετά από ένα χτύπημα, ακόμα κι αν δεν φαίνεται καμία ζημιά, το κράνος πρέπει να αντικατασταθεί. Το εσωτερικό του έχει ήδη κάνει τη δουλειά του. Πάντως, με αυτό το μοντέλο, αν το φέρετε μέσα σε δύο χρόνια, έχετε έκπτωση τριάντα τοις εκατό στο καινούργιο.", "No. After an impact, even if no damage is visible, the helmet must be replaced. The inside has already done its job. Still, with this model, if you bring it back within two years, you get thirty per cent off a new one."),
 ],
 "questions": [
  Q("Γιατί η πωλήτρια προτείνει το ακριβότερο κράνος;", ["Γιατί είναι πιο ελαφρύ και πιο όμορφο", "Γιατί έχει φως και είναι πιστοποιημένο για πατίνια", "Γιατί είναι σε προσφορά", "Γιατί είναι το μόνο στο μέγεθός του"], 1, "Έχει ενσωματωμένο φως στο πίσω μέρος"),
  Q("Τι κάνει η πωλήτρια πριν από την αγορά;", ["Ζητάει την ταυτότητά του", "Μετράει την περίμετρο του κεφαλιού του", "Του δίνει να δοκιμάσει ένα πατίνι", "Ελέγχει το πατίνι του"], 1, "Επιτρέψτε μου να μετρήσω την περίμετρο του κεφαλιού σας"),
  Q("Τι πρέπει να γίνει μετά από ένα χτύπημα;", ["Τίποτα, αν δεν φαίνεται ζημιά", "Το κράνος πρέπει να αντικατασταθεί", "Πρέπει να το ελέγξει το κατάστημα", "Πρέπει να αλλάξει μόνο το φως"], 1, "το κράνος πρέπει να αντικατασταθεί"),
 ],
 "gloss": {"κράνος": "κράνος — helmet", "πατίνι": "πατίνι — scooter", "ενσωματωμένο": "ενσωματωμένος — built-in", "πιστοποιημένο": "πιστοποιημένος — certified", "περίμετρο": "περίμετρος — circumference", "χτύπημα": "χτύπημα — impact, blow", "αντικατασταθεί": "αντικαθίσταμαι — to be replaced", "έκπτωση": "έκπτωση — discount"},
})
ITEMS.append({
 "id": "l83-int-texnikos-anelkystiron", "title": "Ένας τεχνικός ανελκυστήρων", "title_en": "A lift engineer", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή για τα επαγγέλματα, η δημοσιογράφος μιλά με έναν τεχνικό ανελκυστήρων.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Σαββίδη, πόσο καιρό κάνετε αυτή τη δουλειά;", "Mr Savvidis, how long have you been doing this job?"),
  L("Γιώργος", "m", "Εικοσιπέντε χρόνια. Ξεκίνησα ως βοηθός του πατέρα μου, που είχε ένα μικρό συνεργείο στη Θεσσαλονίκη. Σήμερα συντηρώ περίπου εκατόν πενήντα ανελκυστήρες, κυρίως σε πολυκατοικίες. Ο νόμος προβλέπει ότι κάθε ανελκυστήρας πρέπει να ελέγχεται από τεχνικό μία φορά τον μήνα.", "Twenty-five years. I started as my father's assistant; he had a small workshop in Thessaloniki. Today I maintain about a hundred and fifty lifts, mostly in apartment blocks. The law says every lift must be checked by a technician once a month."),
  L("Δημοσιογράφος", "f", "Ποια είναι η πιο συνηθισμένη βλάβη;", "What's the most common fault?"),
  L("Γιώργος", "m", "Οι πόρτες. Τα παιδιά τις κρατάνε ανοιχτές, οι ένοικοι μεταφέρουν έπιπλα και τις χτυπάνε. Ο ανελκυστήρας είναι φτιαγμένος να μην κινείται αν μια πόρτα δεν έχει κλείσει σωστά, οπότε ο κόσμος νομίζει ότι χάλασε, ενώ στην πραγματικότητα απλώς προστατεύει τους επιβάτες.", "The doors. Children hold them open, tenants move furniture and bang them. The lift is made not to move if a door hasn't closed properly, so people think it has broken down, when in fact it's just protecting the passengers."),
  L("Δημοσιογράφος", "f", "Έχετε απεγκλωβίσει πολλούς ανθρώπους;", "Have you freed many people who were trapped?"),
  L("Γιώργος", "m", "Αμέτρητους. Το πιο σημαντικό είναι να μένει κανείς ήρεμος. Ο ανελκυστήρας δεν πέφτει, όσο κι αν το βλέπουμε στις ταινίες. Το καλύτερο είναι να πατήσετε το κουμπί του συναγερμού και να περιμένετε. Μια φορά απεγκλώβισα μια νύφη που πήγαινε στην εκκλησία. Έφτασε με μισή ώρα καθυστέρηση, αλλά μου έστειλε κουφέτα.", "Countless. The most important thing is to stay calm. A lift doesn't fall, however often we see it in films. The best thing is to press the alarm button and wait. Once I freed a bride on her way to church. She arrived half an hour late, but she sent me sugared almonds."),
 ],
 "questions": [
  Q("Κάθε πότε πρέπει να ελέγχεται ένας ανελκυστήρας σύμφωνα με τον νόμο;", ["Μία φορά την εβδομάδα", "Μία φορά τον μήνα", "Μία φορά τον χρόνο", "Μόνο όταν χαλάσει"], 1, "κάθε ανελκυστήρας πρέπει να ελέγχεται από τεχνικό μία φορά τον μήνα"),
  Q("Γιατί ο κόσμος νομίζει συχνά ότι ο ανελκυστήρας χάλασε;", ["Γιατί τα φώτα σβήνουν", "Γιατί κάνει θόρυβο", "Γιατί δεν κινείται όταν μια πόρτα δεν έχει κλείσει σωστά", "Γιατί είναι πολύ αργός"], 2, "Ο ανελκυστήρας είναι φτιαγμένος να μην κινείται αν μια πόρτα δεν έχει κλείσει σωστά"),
  Q("Τι συμβουλεύει όποιον εγκλωβιστεί;", ["Να προσπαθήσει να ανοίξει την πόρτα", "Να πατήσει το κουμπί του συναγερμού και να περιμένει", "Να πηδήξει για να ξεκολλήσει ο θάλαμος", "Να τηλεφωνήσει στους γείτονες"], 1, "Το καλύτερο είναι να πατήσετε το κουμπί του συναγερμού και να περιμένετε"),
 ],
 "gloss": {"ανελκυστήρων": "ανελκυστήρας — lift, elevator", "συνεργείο": "συνεργείο — workshop", "συντηρώ": "συντηρώ — to maintain, service", "βλάβη": "βλάβη — fault, breakdown", "ένοικοι": "ένοικος — tenant, resident", "απεγκλωβίσει": "απεγκλωβίζω — to free (someone trapped)", "Αμέτρητους": "αμέτρητος — countless", "συναγερμού": "συναγερμός — alarm", "κουφέτα": "κουφέτο — sugared almond (wedding favour)"},
})
ITEMS.append({
 "id": "l83-rep-tzoumerka", "title": "Τα Τζουμέρκα", "title_en": "The Tzoumerka mountains", "type": "report", "level": "B2",
 "context_el": "Σε μια ταξιδιωτική εκπομπή, ένας δημοσιογράφος παρουσιάζει τα Τζουμέρκα, στην Ήπειρο.",
 "script": [
  L("Δημοσιογράφος", "m", "Τα Τζουμέρκα είναι μια από τις πιο άγριες και λιγότερο γνωστές οροσειρές της Ελλάδας. Απλώνονται ανάμεσα στους νομούς Ιωαννίνων και Άρτας, με κορυφές που ξεπερνούν τα δύο χιλιάδες μέτρα και χωριά χτισμένα από πέτρα, όπως τα Πράμαντα και οι Καλαρρύτες.", "Tzoumerka is one of the wildest and least known mountain ranges in Greece. It stretches between the prefectures of Ioannina and Arta, with peaks over two thousand metres and stone-built villages such as Pramanta and Kalarrytes."),
  L("Δημοσιογράφος", "m", "Το πιο διάσημο μνημείο της περιοχής είναι το γεφύρι της Πλάκας, πάνω από τον ποταμό Άραχθο. Ήταν το μεγαλύτερο μονότοξο πέτρινο γεφύρι των Βαλκανίων. Το 2015 μια μεγάλη πλημμύρα το γκρέμισε, και πολλοί πίστεψαν ότι χάθηκε για πάντα. Ύστερα από μια προσεκτική αναστήλωση, όμως, ξαναστάθηκε όρθιο το 2020.", "The most famous monument in the area is the Plaka bridge, over the river Arachthos. It was the largest single-arch stone bridge in the Balkans. In 2015 a great flood brought it down, and many believed it was lost for ever. After careful restoration, however, it stood again in 2020."),
  L("Δημοσιογράφος", "m", "Ο Άραχθος είναι επίσης ιδανικός για ράφτινγκ, ενώ λίγο πιο πάνω, κοντά στους Καλαρρύτες, η μονή της Κηπίνας κρέμεται κυριολεκτικά από έναν βράχο. Για να φτάσει κανείς εκεί, περνάει μια μικρή ξύλινη γέφυρα. Παλιότερα, η γέφυρα αυτή σηκωνόταν τη νύχτα, για να προστατεύει τους μοναχούς από τους ληστές.", "The Arachthos is also ideal for rafting, while a little further up, near Kalarrytes, the monastery of Kipina literally hangs from a rock. To get there you cross a small wooden bridge. In the past this bridge was raised at night, to protect the monks from bandits."),
 ],
 "questions": [
  Q("Ανάμεσα σε ποιους νομούς απλώνονται τα Τζουμέρκα;", ["Ιωαννίνων και Πρέβεζας", "Ιωαννίνων και Άρτας", "Άρτας και Τρικάλων", "Θεσπρωτίας και Άρτας"], 1, "Απλώνονται ανάμεσα στους νομούς Ιωαννίνων και Άρτας"),
  Q("Τι έγινε με το γεφύρι της Πλάκας;", ["Γκρεμίστηκε το 2015 και ξαναστήθηκε το 2020", "Χτίστηκε το 2015", "Γκρεμίστηκε σε σεισμό και δεν ξαναχτίστηκε", "Μεταφέρθηκε σε μουσείο"], 0, "Το 2015 μια μεγάλη πλημμύρα το γκρέμισε"),
  Q("Γιατί σηκωνόταν τη νύχτα η ξύλινη γέφυρα της μονής;", ["Για να περνούν τα καράβια", "Για να μην τη χαλάσει η βροχή", "Για να προστατεύει τους μοναχούς από τους ληστές", "Για να μην πέφτουν οι επισκέπτες"], 2, "για να προστατεύει τους μοναχούς από τους ληστές"),
 ],
 "gloss": {"οροσειρές": "οροσειρά — mountain range", "κορυφές": "κορυφή — peak", "γεφύρι": "γεφύρι — (stone) bridge", "μονότοξο": "μονότοξος — single-arched", "γκρέμισε": "γκρεμίζω — to bring down, demolish", "αναστήλωση": "αναστήλωση — restoration", "ράφτινγκ": "ράφτινγκ — rafting", "κυριολεκτικά": "κυριολεκτικά — literally", "μοναχούς": "μοναχός — monk", "ληστές": "ληστής — bandit"},
})
ITEMS.append({
 "id": "l83-rep-porto-lagos", "title": "Το Πόρτο Λάγος και η Βιστωνίδα", "title_en": "Porto Lagos and Lake Vistonida", "type": "report", "level": "B2",
 "context_el": "Σε μια εκπομπή για τη φύση, μια δημοσιογράφος μιλά από την ακτή της Θράκης.",
 "script": [
  L("Δημοσιογράφος", "f", "Βρίσκομαι στο Πόρτο Λάγος, ένα μικρό λιμάνι στη Θράκη, εκεί όπου η λίμνη Βιστωνίδα συναντά τη θάλασσα. Η λίμνη έχει γλυφό νερό, δηλαδή μείγμα από γλυκό και αλμυρό, και γι’ αυτό φιλοξενεί ένα σπάνιο πλήθος από ψάρια και πουλιά.", "I'm in Porto Lagos, a small harbour in Thrace, where Lake Vistonida meets the sea. The lake has brackish water, that is a mixture of fresh and salt water, and so it is home to a rare abundance of fish and birds."),
  L("Δημοσιογράφος", "f", "Τον χειμώνα, εδώ έρχονται χιλιάδες φλαμίνγκο, αλλά και πελεκάνοι, ερωδιοί και αγριόπαπιες. Η περιοχή προστατεύεται από τη Σύμβαση Ραμσάρ για τους υγροτόπους, και οι επισκέπτες καλούνται να παρατηρούν τα πουλιά από απόσταση, χωρίς να τα ενοχλούν.", "In winter thousands of flamingos come here, as well as pelicans, herons and wild ducks. The area is protected by the Ramsar Convention on wetlands, and visitors are asked to watch the birds from a distance, without disturbing them."),
  L("Δημοσιογράφος", "f", "Το πιο φωτογραφημένο σημείο είναι το μοναστήρι του Αγίου Νικολάου, χτισμένο πάνω σε δύο νησάκια μέσα στη λίμνη. Ενώνεται με την ακτή με μια μακριά ξύλινη γέφυρα. Το ηλιοβασίλεμα από εκεί, με τα φλαμίνγκο στο βάθος, είναι από τα πιο όμορφα θεάματα της βόρειας Ελλάδας.", "The most photographed spot is the monastery of Saint Nicholas, built on two islets in the lake. It is joined to the shore by a long wooden bridge. The sunset from there, with the flamingos in the distance, is one of the most beautiful sights in northern Greece."),
 ],
 "questions": [
  Q("Τι νερό έχει η λίμνη Βιστωνίδα;", ["Μόνο γλυκό", "Μόνο αλμυρό", "Γλυφό, μείγμα από γλυκό και αλμυρό", "Θερμό"], 2, "Η λίμνη έχει γλυφό νερό, δηλαδή μείγμα από γλυκό και αλμυρό"),
  Q("Τι ζητείται από τους επισκέπτες;", ["Να ταΐζουν τα πουλιά", "Να παρατηρούν τα πουλιά από απόσταση", "Να μην βγάζουν φωτογραφίες", "Να έρχονται μόνο το καλοκαίρι"], 1, "οι επισκέπτες καλούνται να παρατηρούν τα πουλιά από απόσταση"),
  Q("Πού είναι χτισμένο το μοναστήρι του Αγίου Νικολάου;", ["Σε έναν λόφο πάνω από το λιμάνι", "Σε δύο νησάκια μέσα στη λίμνη", "Στην άκρη της παραλίας", "Μέσα στο χωριό"], 1, "χτισμένο πάνω σε δύο νησάκια μέσα στη λίμνη"),
 ],
 "gloss": {"γλυφό": "γλυφός — brackish", "μείγμα": "μείγμα — mixture", "φλαμίνγκο": "φλαμίνγκο — flamingo", "πελεκάνοι": "πελεκάνος — pelican", "ερωδιοί": "ερωδιός — heron", "αγριόπαπιες": "αγριόπαπια — wild duck", "υγροτόπους": "υγρότοπος — wetland", "νησάκια": "νησάκι — islet", "ηλιοβασίλεμα": "ηλιοβασίλεμα — sunset", "θεάματα": "θέαμα — sight, spectacle"},
})
ITEMS.append({
 "id": "l83-mono-adeia-patrotitas", "title": "Τέσσερις μήνες άδεια πατρότητας", "title_en": "Four months of paternity leave", "type": "monologue", "level": "B2",
 "context_el": "Σε ένα podcast για τη γονεϊκότητα, ένας πατέρας μιλά για την εμπειρία του.",
 "script": [
  L("Θοδωρής", "m", "Όταν γεννήθηκε η κόρη μας, αποφασίσαμε με τη γυναίκα μου να μοιραστούμε τη γονική άδεια. Εκείνη έμεινε στο σπίτι τους πρώτους έξι μήνες, και μετά εγώ πήρα τέσσερις μήνες, όταν εκείνη γύρισε στη δουλειά. Στο γραφείο μου ήμουν ο πρώτος άντρας που το έκανε, και κάποιοι συνάδελφοι αστειεύονταν ότι πάω διακοπές.", "When our daughter was born, my wife and I decided to share parental leave. She stayed home for the first six months, and then I took four months, when she went back to work. At my office I was the first man to do it, and some colleagues joked that I was going on holiday."),
  L("Θοδωρής", "m", "Διακοπές δεν ήταν καθόλου. Την πρώτη εβδομάδα ήμουν εξαντλημένος. Δεν ήξερα πότε πεινάει, πότε νυστάζει, γιατί κλαίει. Σιγά σιγά, όμως, μάθαμε ο ένας τον άλλον. Ανακάλυψα ότι ηρεμούσε μόνο όταν της τραγουδούσα παλιά ρεμπέτικα, κάτι που η μητέρα της δεν το πίστευε.", "It was no holiday at all. The first week I was exhausted. I didn't know when she was hungry, when she was sleepy, why she was crying. Little by little, though, we got to know each other. I discovered that she only calmed down when I sang her old rebetika, which her mother couldn't believe."),
  L("Θοδωρής", "m", "Το πιο σημαντικό που κέρδισα είναι ότι τώρα δεν είμαι ο «βοηθός» της μαμάς. Ξέρω τον παιδίατρο, ξέρω τα ρούχα της, ξέρω τι τρώει. Και η γυναίκα μου λέει ότι για πρώτη φορά ένιωσε ότι η ευθύνη μοιράζεται πραγματικά στα δύο.", "The most important thing I gained is that now I'm not mum's 'helper'. I know the paediatrician, I know her clothes, I know what she eats. And my wife says that for the first time she felt the responsibility was really shared between the two of us."),
 ],
 "questions": [
  Q("Πόσους μήνες άδεια πήρε ο Θοδωρής;", ["Δύο", "Τέσσερις", "Έξι", "Δέκα"], 1, "μετά εγώ πήρα τέσσερις μήνες"),
  Q("Πώς ηρεμούσε η κόρη του;", ["Με βόλτες με το αυτοκίνητο", "Όταν της τραγουδούσε παλιά ρεμπέτικα", "Με μουσική από το ραδιόφωνο", "Όταν την κρατούσε η γιαγιά"], 1, "ηρεμούσε μόνο όταν της τραγουδούσα παλιά ρεμπέτικα"),
  Q("Τι λέει η γυναίκα του για την εμπειρία;", ["Ότι ήταν δύσκολη για εκείνη", "Ότι η ευθύνη μοιράζεται πραγματικά στα δύο", "Ότι θα ήθελε περισσότερη άδεια", "Ότι ο Θοδωρής έπρεπε να γυρίσει νωρίτερα στη δουλειά"], 1, "η ευθύνη μοιράζεται πραγματικά στα δύο"),
 ],
 "gloss": {"γονεϊκότητα": "γονεϊκότητα — parenthood", "γονική άδεια": "γονική άδεια — parental leave", "συνάδελφοι": "συνάδελφος — colleague", "αστειεύονταν": "αστειεύομαι — to joke", "εξαντλημένος": "εξαντλημένος — exhausted", "νυστάζει": "νυστάζω — to be sleepy", "ρεμπέτικα": "ρεμπέτικο — rebetiko song", "ευθύνη": "ευθύνη — responsibility"},
})
ITEMS.append({
 "id": "l83-mono-xypnao-stis-pente", "title": "Γιατί ξυπνάω στις πέντε", "title_en": "Why I get up at five", "type": "monologue", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή, μια ακροάτρια εξηγεί γιατί ξυπνάει πολύ νωρίς κάθε πρωί.",
 "script": [
  L("Ζωή", "f", "Εδώ και τρία χρόνια ξυπνάω κάθε πρωί στις πέντε, ακόμα και τα Σαββατοκύριακα. Δεν το έκανα επειδή διάβασα κάποιο βιβλίο για επιτυχημένους ανθρώπους. Το έκανα από ανάγκη: έχω δύο παιδιά και μια απαιτητική δουλειά, και δεν είχα ούτε μισή ώρα για τον εαυτό μου.", "For three years I've been getting up at five every morning, even at weekends. I didn't do it because I read some book about successful people. I did it out of necessity: I have two children and a demanding job, and I didn't have even half an hour for myself."),
  L("Ζωή", "f", "Τις δύο πρώτες εβδομάδες ήταν μαρτύριο. Το μυστικό, τελικά, δεν ήταν το ξυπνητήρι αλλά το βράδυ: έπρεπε να πέφτω για ύπνο στις δέκα. Αυτό σήμαινε λιγότερες σειρές στην τηλεόραση και λιγότερο κινητό στο κρεβάτι.", "The first two weeks were torture. The secret, in the end, wasn't the alarm clock but the evening: I had to go to bed at ten. That meant fewer series on TV and less phone in bed."),
  L("Ζωή", "f", "Τώρα αυτή η ώρα είναι η πιο πολύτιμη της μέρας μου. Το σπίτι είναι σιωπηλό, πίνω τον καφέ μου στο μπαλκόνι, διαβάζω ή απλώς κοιτάζω τον ουρανό να φωτίζει. Δεν το προτείνω σε όλους, όμως. Ο σύντροφός μου το δοκίμασε μία εβδομάδα και είπε ότι προτιμά να είναι ζωντανός παρά ξύπνιος.", "Now this hour is the most precious of my day. The house is silent, I drink my coffee on the balcony, read or just watch the sky grow light. I don't recommend it to everyone, though. My partner tried it for a week and said he'd rather be alive than awake."),
 ],
 "questions": [
  Q("Γιατί άρχισε η Ζωή να ξυπνάει στις πέντε;", ["Γιατί το διάβασε σε ένα βιβλίο", "Γιατί δεν είχε καθόλου χρόνο για τον εαυτό της", "Γιατί η δουλειά της αρχίζει νωρίς", "Γιατί δεν μπορούσε να κοιμηθεί"], 1, "δεν είχα ούτε μισή ώρα για τον εαυτό μου"),
  Q("Ποιο ήταν, τελικά, το μυστικό;", ["Ένα δυνατό ξυπνητήρι", "Ο πολύς καφές", "Να πέφτει για ύπνο στις δέκα", "Να κοιμάται το μεσημέρι"], 2, "έπρεπε να πέφτω για ύπνο στις δέκα"),
  Q("Τι είπε ο σύντροφός της όταν το δοκίμασε;", ["Ότι του άρεσε πολύ", "Ότι θα το συνεχίσει", "Ότι προτιμά να είναι ζωντανός παρά ξύπνιος", "Ότι ξυπνάει ήδη νωρίς"], 2, "προτιμά να είναι ζωντανός παρά ξύπνιος"),
 ],
 "gloss": {"ακροάτρια": "ακροάτρια — (female) listener", "απαιτητική": "απαιτητικός — demanding", "μαρτύριο": "μαρτύριο — torture, ordeal", "ξυπνητήρι": "ξυπνητήρι — alarm clock", "πέφτω για ύπνο": "πέφτω για ύπνο — to go to bed", "σειρές": "σειρά — (TV) series", "πολύτιμη": "πολύτιμος — precious", "φωτίζει": "φωτίζω — to grow light, light up", "ξύπνιος": "ξύπνιος — awake"},
})
ITEMS.append({
 "id": "l83-c1-fainomeno-ikea", "title": "Το «φαινόμενο IKEA»: γιατί αγαπάμε ό,τι φτιάχνουμε", "title_en": "The 'IKEA effect': why we love what we make", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την οικονομία της καθημερινότητας, ένας δημοσιογράφος συζητά με μια ερευνήτρια της συμπεριφορικής οικονομίας.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αλεξίου, τι είναι αυτό που οι ερευνητές ονομάζουν «φαινόμενο IKEA»;", "Ms Alexiou, what is it that researchers call the 'IKEA effect'?"),
  L("Ερευνήτρια", "f", "Είναι η τάση μας να αποδίδουμε μεγαλύτερη αξία σε αντικείμενα που έχουμε φτιάξει, έστω και εν μέρει, με τα χέρια μας. Σε μια γνωστή σειρά πειραμάτων, οι συμμετέχοντες συναρμολογούσαν απλά κουτιά αποθήκευσης ή έφτιαχναν ζώα από χαρτί, τα γνωστά οριγκάμι. Όταν τους ζητήθηκε να πουν πόσα χρήματα θα έδιναν για αυτά, πρόσφεραν σημαντικά περισσότερα απ’ ό,τι για ίδια αντικείμενα, έτοιμα από το εργοστάσιο.", "It's our tendency to attribute greater value to objects we have made, even partly, with our own hands. In a well-known series of experiments, participants assembled simple storage boxes or made paper animals, the familiar origami. When asked how much money they would pay for them, they offered considerably more than for identical, factory-made objects."),
  L("Δημοσιογράφος", "m", "Ακόμα κι αν το αποτέλεσμα ήταν άσχημο;", "Even if the result was ugly?"),
  L("Ερευνήτρια", "f", "Ακριβώς. Τα οριγκάμι των ερασιτεχνών ήταν συχνά τσαλακωμένα και στραβά, κι όμως οι δημιουργοί τους τα εκτιμούσαν σχεδόν όσο και τα έργα ειδικών. Υπάρχει όμως μια σημαντική προϋπόθεση: η εργασία πρέπει να ολοκληρωθεί. Όταν οι συμμετέχοντες άφηναν το έργο στη μέση ή το κατέστρεφαν, το φαινόμενο εξαφανιζόταν.", "Exactly. The amateurs' origami were often crumpled and crooked, yet their makers valued them almost as highly as the work of experts. There is, however, an important condition: the task has to be completed. When participants left the work half-done or it was destroyed, the effect disappeared."),
  L("Δημοσιογράφος", "m", "Πώς το εκμεταλλεύονται οι εταιρείες;", "How do companies exploit it?"),
  L("Ερευνήτρια", "f", "Με πολλούς τρόπους. Το κλασικό παράδειγμα είναι τα έτοιμα μείγματα για κέικ στις Ηνωμένες Πολιτείες τη δεκαετία του 1950. Λέγεται ότι οι πωλήσεις τους ανέβηκαν όταν η συνταγή άλλαξε και οι νοικοκυρές έπρεπε να προσθέτουν ένα φρέσκο αυγό, αν και η ιστορία αυτή είναι μάλλον μύθος. Το βέβαιο είναι ότι λίγη προσπάθεια μάς κάνει να νιώθουμε ικανοί. Και αυτό το αίσθημα, όπως αποδεικνύεται, έχει τιμή.", "In many ways. The classic example is cake mixes in the United States in the 1950s. It is said that their sales rose when the recipe changed and housewives had to add a fresh egg, although this story is probably a myth. What is certain is that a little effort makes us feel competent. And that feeling, as it turns out, has a price."),
 ],
 "questions": [
  Q("Τι έδειξαν τα πειράματα;", ["Ότι προτιμάμε τα έτοιμα προϊόντα", "Ότι πληρώνουμε περισσότερα για ό,τι έχουμε φτιάξει οι ίδιοι", "Ότι τα οριγκάμι είναι δύσκολα", "Ότι οι ειδικοί κάνουν πάντα καλύτερη δουλειά"], 1, "πρόσφεραν σημαντικά περισσότερα απ’ ό,τι για ίδια αντικείμενα, έτοιμα από το εργοστάσιο"),
  Q("Ποια προϋπόθεση πρέπει να ισχύει για να εμφανιστεί το φαινόμενο;", ["Το αντικείμενο πρέπει να είναι όμορφο", "Η εργασία πρέπει να ολοκληρωθεί", "Ο συμμετέχων πρέπει να είναι ειδικός", "Το αντικείμενο πρέπει να είναι ακριβό"], 1, "η εργασία πρέπει να ολοκληρωθεί"),
  Q("Τι λέει η ερευνήτρια για την ιστορία με τα μείγματα για κέικ;", ["Ότι είναι αποδεδειγμένη", "Ότι συνέβη στην Ευρώπη", "Ότι είναι μάλλον μύθος", "Ότι αφορούσε τα ψωμιά"], 2, "αν και η ιστορία αυτή είναι μάλλον μύθος"),
 ],
 "gloss": {"συμπεριφορικής οικονομίας": "συμπεριφορική οικονομία — behavioural economics", "αποδίδουμε": "αποδίδω — to attribute", "εν μέρει": "εν μέρει — partly", "συναρμολογούσαν": "συναρμολογώ — to assemble", "οριγκάμι": "οριγκάμι — origami", "ερασιτεχνών": "ερασιτέχνης — amateur", "τσαλακωμένα": "τσαλακωμένος — crumpled", "προϋπόθεση": "προϋπόθεση — precondition", "εκμεταλλεύονται": "εκμεταλλεύομαι — to exploit", "μείγματα": "μείγμα — mix"},
})
ITEMS.append({
 "id": "l83-c1-paratiritis", "title": "Γιατί δεν βοηθάμε όταν είμαστε πολλοί;", "title_en": "Why don't we help when there are many of us?", "type": "monologue", "level": "C1",
 "context_el": "Σε μια διάλεξη ψυχολογίας για το ευρύ κοινό, μια καθηγήτρια μιλά για το «φαινόμενο του παρατηρητή».",
 "script": [
  L("Καθηγήτρια", "f", "Το 1964, στη Νέα Υόρκη, μια νεαρή γυναίκα, η Κίτι Τζενοβέζε, δολοφονήθηκε έξω από το σπίτι της. Οι εφημερίδες έγραψαν τότε ότι τριάντα οχτώ γείτονες άκουσαν ή είδαν την επίθεση χωρίς να κάνουν τίποτα. Σήμερα ξέρουμε ότι η εικόνα αυτή ήταν υπερβολική, ωστόσο η υπόθεση έγινε αφετηρία για μια ολόκληρη σειρά ερευνών.", "In 1964, in New York, a young woman, Kitty Genovese, was murdered outside her home. The newspapers wrote at the time that thirty-eight neighbours heard or saw the attack without doing anything. Today we know that this picture was exaggerated, yet the case became the starting point for a whole series of studies."),
  L("Καθηγήτρια", "f", "Οι ψυχολόγοι Ντάρλεϊ και Λατανέ έστησαν πειράματα όπου ένας φοιτητής, μέσα από ένα σύστημα ενδοεπικοινωνίας, άκουγε κάποιον να παθαίνει κρίση επιληψίας. Όταν ο φοιτητής πίστευε ότι ήταν ο μόνος που άκουγε, έτρεχε να βοηθήσει στη συντριπτική πλειονότητα των περιπτώσεων. Όταν πίστευε ότι τον άκουγαν και άλλοι τέσσερις, το ποσοστό έπεφτε δραματικά. Το ονόμασαν «διάχυση της ευθύνης»: όσο περισσότεροι είμαστε, τόσο λιγότερο νιώθει ο καθένας ότι η βοήθεια εξαρτάται από τον ίδιο.", "The psychologists Darley and Latané set up experiments in which a student, through an intercom system, heard someone having an epileptic seizure. When the student believed he was the only one listening, he rushed to help in the overwhelming majority of cases. When he believed four others could hear too, the rate dropped dramatically. They called it 'diffusion of responsibility': the more of us there are, the less each one feels that help depends on him."),
  L("Καθηγήτρια", "f", "Υπάρχει όμως και μια πιο αισιόδοξη πλευρά. Μια πρόσφατη μελέτη, που ανέλυσε εκατοντάδες πραγματικές συγκρούσεις καταγεγραμμένες από κάμερες ασφαλείας σε διάφορες χώρες, βρήκε ότι στις εννιά από τις δέκα περιπτώσεις τουλάχιστον ένας περαστικός παρενέβη. Και το συμβουλευτικό μήνυμα είναι απλό: αν χρειαστείτε βοήθεια μέσα σε πλήθος, μην απευθύνεστε σε όλους. Κοιτάξτε έναν άνθρωπο στα μάτια και πείτε του: «Εσείς, με το μπλε μπουφάν, καλέστε το εκατόν δώδεκα».", "But there is also a more optimistic side. A recent study, which analysed hundreds of real conflicts recorded by security cameras in various countries, found that in nine out of ten cases at least one passer-by intervened. And the practical advice is simple: if you need help in a crowd, don't address everyone. Look one person in the eye and say: 'You, in the blue jacket, call one-one-two.'"),
 ],
 "questions": [
  Q("Τι λέει η καθηγήτρια για όσα έγραψαν οι εφημερίδες το 1964;", ["Ότι ήταν απολύτως ακριβή", "Ότι η εικόνα ήταν υπερβολική", "Ότι δεν έγινε ποτέ έγκλημα", "Ότι οι γείτονες κάλεσαν αμέσως την αστυνομία"], 1, "Σήμερα ξέρουμε ότι η εικόνα αυτή ήταν υπερβολική"),
  Q("Τι είναι η «διάχυση της ευθύνης»;", ["Η τάση να κατηγορούμε τους άλλους", "Το ότι, όσο περισσότεροι είμαστε, τόσο λιγότερο νιώθει ο καθένας ότι η βοήθεια εξαρτάται από τον ίδιο", "Η υποχρέωση να καλούμε την αστυνομία", "Η τάση να βοηθάμε μόνο τους γνωστούς μας"], 1, "όσο περισσότεροι είμαστε, τόσο λιγότερο νιώθει ο καθένας ότι η βοήθεια εξαρτάται από τον ίδιο"),
  Q("Τι συμβουλεύει η καθηγήτρια όποιον χρειάζεται βοήθεια μέσα σε πλήθος;", ["Να φωνάξει όσο πιο δυνατά μπορεί", "Να απευθυνθεί σε όλους μαζί", "Να κοιτάξει έναν άνθρωπο στα μάτια και να του ζητήσει κάτι συγκεκριμένο", "Να περιμένει την αστυνομία"], 2, "Κοιτάξτε έναν άνθρωπο στα μάτια"),
 ],
 "gloss": {"παρατηρητή": "παρατηρητής — bystander, observer", "αφετηρία": "αφετηρία — starting point", "ενδοεπικοινωνίας": "ενδοεπικοινωνία — intercom", "κρίση επιληψίας": "κρίση επιληψίας — epileptic seizure", "συντριπτική πλειονότητα": "συντριπτική πλειονότητα — overwhelming majority", "διάχυση": "διάχυση — diffusion", "καταγεγραμμένες": "καταγεγραμμένος — recorded", "περαστικός": "περαστικός — passer-by", "παρενέβη": "παρεμβαίνω — to intervene", "απευθύνεστε": "απευθύνομαι — to address, turn to"},
})

rnd = random.Random(83)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-83.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
