# Source for library/listening/listening-62.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l62.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l62-ann-paidi-paralia", "title": "Χαμένο παιδί στην παραλία", "title_en": "A lost child on the beach", "type": "announcement", "level": "B2",
 "context_el": "Κάνετε μπάνιο σε μια οργανωμένη παραλία. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα του ναυαγοσωστικού πύργου.",
 "script": [
  L("Ναυαγοσώστης", "m", "Προσοχή, παρακαλώ. Στον ναυαγοσωστικό πύργο βρίσκεται ένα κοριτσάκι περίπου πέντε χρονών, με το όνομα Αλεξάνδρα. Φοράει κίτρινο μαγιό και ένα ροζ καπέλο με λουλούδια. Οι γονείς της παρακαλούνται να έρθουν αμέσως στον πύργο, δίπλα στο μπαρ της παραλίας.", "Attention, please. A little girl of about five, named Alexandra, is at the lifeguard tower. She is wearing a yellow swimsuit and a pink hat with flowers. Her parents are asked to come to the tower, next to the beach bar, immediately."),
  L("Ναυαγοσώστης", "m", "Η μικρή είναι καλά και περιμένει με τη συνάδελφό μου. Υπενθυμίζουμε σε όλους τους γονείς ότι στο περίπτερο πληροφοριών διατίθενται δωρεάν βραχιολάκια, όπου μπορείτε να γράψετε το τηλέφωνό σας. Έτσι, αν το παιδί σας χαθεί, θα μπορούμε να σας ειδοποιήσουμε αμέσως.", "The little one is fine and is waiting with my colleague. We remind all parents that free wristbands are available at the information kiosk, on which you can write your phone number. That way, if your child gets lost, we can contact you straight away."),
  L("Ναυαγοσώστης", "m", "Σας ευχαριστούμε και σας ευχόμαστε καλό μπάνιο.", "Thank you, and enjoy your swim."),
 ],
 "questions": [
  Q("Τι φοράει το κοριτσάκι;", ["Ένα κόκκινο μαγιό και γυαλιά ηλίου", "Ένα κίτρινο μαγιό και ένα ροζ καπέλο με λουλούδια", "Ένα μπλε φόρεμα", "Ένα ροζ μαγιό και σαγιονάρες"], 1, "Φοράει κίτρινο μαγιό και ένα ροζ καπέλο με λουλούδια"),
  Q("Πού πρέπει να πάνε οι γονείς;", ["Στο πάρκινγκ", "Στο περίπτερο πληροφοριών", "Στον ναυαγοσωστικό πύργο, δίπλα στο μπαρ", "Στην είσοδο της παραλίας"], 2, "να έρθουν αμέσως στον πύργο, δίπλα στο μπαρ της παραλίας"),
  Q("Τι προσφέρεται δωρεάν στο περίπτερο πληροφοριών;", ["Αντηλιακό", "Βραχιολάκια για να γράψουν οι γονείς το τηλέφωνό τους", "Καπέλα για τα παιδιά", "Νερό"], 1, "διατίθενται δωρεάν βραχιολάκια, όπου μπορείτε να γράψετε το τηλέφωνό σας"),
 ],
 "gloss": {"ναυαγοσωστικό πύργο": "ναυαγοσωστικός πύργος — lifeguard tower", "μαγιό": "μαγιό — swimsuit", "παρακαλούνται": "παρακαλούμαι — to be requested", "συνάδελφό": "συνάδελφος — colleague", "περίπτερο πληροφοριών": "περίπτερο πληροφοριών — information kiosk", "διατίθενται": "διατίθεμαι — to be available", "βραχιολάκια": "βραχιολάκι — wristband", "ειδοποιήσουμε": "ειδοποιώ — to notify, alert"},
})

ITEMS.append({
 "id": "l62-vm-vivliothiki", "title": "Το βιβλίο σας σάς περιμένει", "title_en": "Your book is waiting for you", "type": "voicemail", "level": "B2",
 "context_el": "Είχατε κάνει κράτηση για ένα βιβλίο στη δημοτική βιβλιοθήκη. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Βιβλιοθηκονόμος", "m", "Καλημέρα σας, κύριε Αθανασίου, σας τηλεφωνώ από τη Δημοτική Βιβλιοθήκη. Το βιβλίο που είχατε κρατήσει, «Η ζωή εν τάφω» του Μυριβήλη, επιστράφηκε χθες και σας περιμένει στο γκισέ των δανεισμών. Θα το κρατήσουμε για εσάς μέχρι την Παρασκευή.", "Good morning, Mr Athanasiou, I'm calling from the Municipal Library. The book you had reserved, Myrivilis's 'Life in the Tomb', was returned yesterday and is waiting for you at the loans desk. We'll keep it for you until Friday."),
  L("Βιβλιοθηκονόμος", "m", "Επίσης, σας υπενθυμίζω ότι έχετε ακόμη στα χέρια σας δύο βιβλία, των οποίων η προθεσμία επιστροφής έληξε την περασμένη εβδομάδα. Αν θέλετε, μπορείτε να ανανεώσετε τον δανεισμό τους μέσα από την ιστοσελίδα μας, με τον αριθμό της κάρτας μέλους σας.", "I'd also like to remind you that you still have two books whose return deadline expired last week. If you wish, you can renew the loan through our website, using your membership card number."),
  L("Βιβλιοθηκονόμος", "m", "Να σας πω, τέλος, ότι από τον επόμενο μήνα η βιβλιοθήκη θα είναι ανοιχτή και τα Σάββατα, από τις δέκα ως τις δύο. Καλή σας μέρα.", "Finally, from next month the library will also be open on Saturdays, from ten to two. Have a good day."),
 ],
 "questions": [
  Q("Μέχρι πότε θα κρατήσει η βιβλιοθήκη το βιβλίο;", ["Μέχρι αύριο", "Μέχρι την Παρασκευή", "Μέχρι το Σάββατο", "Για έναν μήνα"], 1, "Θα το κρατήσουμε για εσάς μέχρι την Παρασκευή"),
  Q("Ποιο πρόβλημα υπάρχει με δύο άλλα βιβλία;", ["Έχουν χαθεί", "Έχουν καταστραφεί", "Η προθεσμία επιστροφής τους έληξε", "Δεν έχουν ακόμη επιστραφεί από άλλον αναγνώστη"], 2, "δύο βιβλία, των οποίων η προθεσμία επιστροφής έληξε την περασμένη εβδομάδα"),
  Q("Τι αλλάζει από τον επόμενο μήνα;", ["Η βιβλιοθήκη θα ανοίγει και τα Σάββατα", "Η βιβλιοθήκη θα κλείνει νωρίτερα", "Οι κάρτες μέλους θα πληρώνονται", "Οι κρατήσεις θα γίνονται μόνο τηλεφωνικά"], 0, "η βιβλιοθήκη θα είναι ανοιχτή και τα Σάββατα"),
 ],
 "gloss": {"κρατήσει": "κρατώ — to reserve, keep", "επιστράφηκε": "επιστρέφομαι — to be returned", "γκισέ των δανεισμών": "γκισέ δανεισμών — loans desk", "προθεσμία επιστροφής": "προθεσμία επιστροφής — return deadline", "έληξε": "λήγω — to expire", "ανανεώσετε": "ανανεώνω — to renew", "κάρτας μέλους": "κάρτα μέλους — membership card"},
})

ITEMS.append({
 "id": "l62-dia-laouto", "title": "Ένα λαούτο για αρχάριους", "title_en": "A laouto for a beginner", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα κατάστημα μουσικών οργάνων. Μια πελάτισσα θέλει να αγοράσει λαούτο.",
 "script": [
  L("Πελάτισσα", "f", "Καλησπέρα. Θέλω να αρχίσω μαθήματα λαούτου και ψάχνω ένα όργανο για αρχάριους. Δεν ξέρω, όμως, τίποτα από λαούτα.", "Good evening. I want to start laouto lessons and I'm looking for an instrument for beginners. But I know nothing about laoutos."),
  L("Πωλητής", "m", "Κανένα πρόβλημα. Για αρχή, σας προτείνω αυτό εδώ, με σκάφη από καρυδιά. Είναι ελαφρύ, έχει καλό ήχο και κοστίζει τριακόσια ογδόντα ευρώ. Τα χειροποίητα ξεκινούν από οκτακόσια, αλλά για τα πρώτα χρόνια δεν χρειάζεστε κάτι τόσο ακριβό.", "No problem. To start with, I suggest this one here, with a walnut body. It's light, sounds good and costs three hundred and eighty euros. The handmade ones start at eight hundred, but for the first few years you don't need anything that expensive."),
  L("Πελάτισσα", "f", "Τι άλλο θα χρειαστώ;", "What else will I need?"),
  L("Πωλητής", "m", "Μια θήκη, για να το προστατεύετε από την υγρασία και τα χτυπήματα, και μια πένα. Αν το αγοράσετε σήμερα, η θήκη σάς την κάνουμε δώρο. Και κάτι ακόμη: τις πρώτες εβδομάδες οι χορδές ξεκουρδίζονται συχνά. Είναι φυσιολογικό, μην ανησυχήσετε.", "A case, to protect it from damp and knocks, and a plectrum. If you buy it today, we'll give you the case for free. And one more thing: in the first few weeks the strings go out of tune often. It's normal, don't worry."),
 ],
 "questions": [
  Q("Πόσο κοστίζει το λαούτο που προτείνει ο πωλητής;", ["Τριακόσια ευρώ", "Τριακόσια ογδόντα ευρώ", "Οκτακόσια ευρώ", "Εκατόν ογδόντα ευρώ"], 1, "κοστίζει τριακόσια ογδόντα ευρώ"),
  Q("Τι θα πάρει δώρο η πελάτισσα, αν το αγοράσει σήμερα;", ["Ένα μάθημα", "Τη θήκη", "Μια πένα", "Ένα σετ χορδές"], 1, "η θήκη σάς την κάνουμε δώρο"),
  Q("Τι είναι φυσιολογικό τις πρώτες εβδομάδες, σύμφωνα με τον πωλητή;", ["Να πονάνε τα δάχτυλα", "Να ξεκουρδίζονται συχνά οι χορδές", "Να ραγίζει το ξύλο", "Να αλλάζει ο ήχος από την υγρασία"], 1, "τις πρώτες εβδομάδες οι χορδές ξεκουρδίζονται συχνά. Είναι φυσιολογικό"),
 ],
 "gloss": {"λαούτου": "λαούτο — laouto (Greek long-necked lute)", "σκάφη": "σκάφη — body (of a lute)", "καρυδιά": "καρυδιά — walnut (wood)", "χειροποίητα": "χειροποίητος — handmade", "θήκη": "θήκη — case", "υγρασία": "υγρασία — damp, humidity", "πένα": "πένα — plectrum", "χορδές": "χορδή — string", "ξεκουρδίζονται": "ξεκουρδίζομαι — to go out of tune"},
})

ITEMS.append({
 "id": "l62-dia-logariasmos-tavernas", "title": "Πώς θα μοιράσουμε τον λογαριασμό;", "title_en": "How shall we split the bill?", "type": "dialogue", "level": "B2",
 "context_el": "Μια παρέα φίλων τελειώνει το φαγητό σε μια ταβέρνα. Θα ακούσετε δύο από αυτούς να συζητούν για τον λογαριασμό.",
 "script": [
  L("Στέλιος", "m", "Ήρθε ο λογαριασμός: εκατόν σαράντα τέσσερα ευρώ. Είμαστε έξι, άρα εικοσιτέσσερα ο καθένας. Απλό.", "The bill's here: a hundred and forty-four euros. There are six of us, so twenty-four each. Simple."),
  L("Μυρτώ", "f", "Περίμενε λίγο. Η Ζωή και ο Άρης ήπιαν μόνο νερό και δεν πήραν από τα θαλασσινά. Εμείς παραγγείλαμε δύο μπουκάλια κρασί και τις γαρίδες. Δεν είναι δίκαιο να πληρώσουν το ίδιο.", "Hang on. Zoi and Aris only drank water and didn't have any of the seafood. We ordered two bottles of wine and the prawns. It isn't fair for them to pay the same."),
  L("Στέλιος", "m", "Καλά λες. Τότε ας πληρώσουν εκείνοι από δεκαπέντε, και τα υπόλοιπα τα μοιράζουμε εμείς οι τέσσερις. Πόσο βγαίνει;", "You're right. Then let them pay fifteen each, and the four of us split the rest. How much is that?"),
  L("Μυρτώ", "f", "Εκατόν δεκατέσσερα διά τέσσερα… είκοσι οκτώ και κάτι. Ας βάλουμε τριάντα ο καθένας, και τα ρέστα να μείνουν φιλοδώρημα. Ο σερβιτόρος ήταν πολύ εξυπηρετικός. Α, και πες τους ότι δέχονται κάρτα, γιατί η Ζωή δεν έχει μετρητά.", "A hundred and fourteen divided by four… twenty-eight and a bit. Let's put in thirty each, and leave the change as a tip. The waiter was very helpful. Oh, and tell them they take cards, because Zoi has no cash."),
 ],
 "questions": [
  Q("Γιατί διαφωνεί η Μυρτώ με τη μοιρασιά σε ίσα μέρη;", ["Γιατί ο λογαριασμός είναι λάθος", "Γιατί δύο φίλοι ήπιαν μόνο νερό και δεν έφαγαν θαλασσινά", "Γιατί θέλει να κεράσει τους φίλους της", "Γιατί η ίδια δεν έφαγε σχεδόν τίποτα"], 1, "Η Ζωή και ο Άρης ήπιαν μόνο νερό και δεν πήραν από τα θαλασσινά"),
  Q("Πόσα θα πληρώσει τελικά καθένας από τους τέσσερις;", ["Είκοσι τέσσερα ευρώ", "Δεκαπέντε ευρώ", "Είκοσι οκτώ ευρώ", "Τριάντα ευρώ"], 3, "Ας βάλουμε τριάντα ο καθένας"),
  Q("Τι θα γίνουν τα ρέστα;", ["Θα τα πάρει η Ζωή", "Θα μείνουν φιλοδώρημα για τον σερβιτόρο", "Θα πληρώσουν το επόμενο τραπέζι", "Θα τα επιστρέψουν στον Άρη"], 1, "τα ρέστα να μείνουν φιλοδώρημα"),
 ],
 "gloss": {"λογαριασμός": "λογαριασμός — bill", "θαλασσινά": "θαλασσινά — seafood", "γαρίδες": "γαρίδα — prawn", "δίκαιο": "δίκαιος — fair", "διά": "διά — divided by", "ρέστα": "ρέστα — change (money)", "φιλοδώρημα": "φιλοδώρημα — tip", "εξυπηρετικός": "εξυπηρετικός — helpful", "μετρητά": "μετρητά — cash"},
})

ITEMS.append({
 "id": "l62-int-chartaetoi", "title": "Ο κατασκευαστής χαρταετών", "title_en": "The kite maker", "type": "interview", "level": "B2",
 "context_el": "Λίγες μέρες πριν από την Καθαρά Δευτέρα, μια δημοσιογράφος μιλά με έναν ηλικιωμένο κατασκευαστή χαρταετών.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Μανώλη, πόσα χρόνια φτιάχνετε χαρταετούς;", "Mr Manolis, how many years have you been making kites?"),
  L("Κατασκευαστής", "m", "Από δώδεκα χρονών. Με έμαθε ο πατέρας μου, στην αυλή μας στην Κοκκινιά. Τότε δεν υπήρχαν έτοιμοι αετοί από πλαστικό· τους φτιάχναμε μόνοι μας με καλάμια, χρωματιστό χαρτί, σπάγκο και αλευρόκολλα. Σήμερα φτιάχνω γύρω στους τριακόσιους κάθε χρόνο, όλους στο χέρι.", "Since I was twelve. My father taught me, in our yard in Kokkinia. Back then there were no ready-made plastic kites; we made them ourselves with reeds, coloured paper, string and flour paste. Today I make around three hundred every year, all by hand."),
  L("Δημοσιογράφος", "f", "Ποιο είναι το μυστικό ενός καλού χαρταετού;", "What's the secret of a good kite?"),
  L("Κατασκευαστής", "m", "Η ισορροπία. Ο σκελετός πρέπει να είναι απόλυτα συμμετρικός, αλλιώς ο αετός γέρνει και πέφτει. Και η ουρά να έχει το σωστό μάκρος: ούτε πολύ κοντή ούτε πολύ μακριά. Το πιο σημαντικό, όμως, το λέω πάντα στα παιδιά: ποτέ αετό κοντά σε καλώδια της ΔΕΗ. Έχουν γίνει πολλά ατυχήματα.", "Balance. The frame must be perfectly symmetrical, otherwise the kite tilts and falls. And the tail must be the right length: neither too short nor too long. But the most important thing, I always tell the children: never fly a kite near power lines. There have been many accidents."),
 ],
 "questions": [
  Q("Με τι έφτιαχναν παλιά τους χαρταετούς;", ["Με πλαστικό και ξύλο", "Με καλάμια, χρωματιστό χαρτί, σπάγκο και αλευρόκολλα", "Με ύφασμα και σύρμα", "Τους αγόραζαν έτοιμους"], 1, "τους φτιάχναμε μόνοι μας με καλάμια, χρωματιστό χαρτί, σπάγκο και αλευρόκολλα"),
  Q("Γιατί πρέπει ο σκελετός να είναι συμμετρικός;", ["Για να είναι πιο όμορφος", "Γιατί αλλιώς ο αετός γέρνει και πέφτει", "Για να αντέχει τη βροχή", "Για να είναι πιο ελαφρύς"], 1, "αλλιώς ο αετός γέρνει και πέφτει"),
  Q("Ποια συμβουλή δίνει πάντα στα παιδιά;", ["Να πετούν τον αετό μόνο με τους γονείς τους", "Να μην πετούν ποτέ αετό κοντά σε καλώδια ρεύματος", "Να φτιάχνουν μόνοι τους τον αετό", "Να μην τον πετούν όταν φυσάει πολύ"], 1, "ποτέ αετό κοντά σε καλώδια της ΔΕΗ"),
 ],
 "gloss": {"Καθαρά Δευτέρα": "Καθαρά Δευτέρα — Clean Monday (start of Lent, kite-flying day)", "χαρταετούς": "χαρταετός — kite", "καλάμια": "καλάμι — reed, cane", "σπάγκο": "σπάγκος — string", "αλευρόκολλα": "αλευρόκολλα — flour paste (glue)", "ισορροπία": "ισορροπία — balance", "σκελετός": "σκελετός — frame", "γέρνει": "γέρνω — to tilt, lean", "καλώδια της ΔΕΗ": "καλώδια της ΔΕΗ — power lines (ΔΕΗ: the Public Power Corporation)"},
})

ITEMS.append({
 "id": "l62-rep-koroni", "title": "Το κάστρο της Κορώνης", "title_en": "The castle of Koroni", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ταξιδιωτικό ρεπορτάζ από τη Μεσσηνία.",
 "script": [
  L("Ρεπόρτερ", "f", "Η Κορώνη απλώνεται αμφιθεατρικά στη νοτιοδυτική άκρη της Πελοποννήσου, κάτω από το κάστρο της. Οι Ενετοί, που το κατείχαν για περίπου τρεις αιώνες, ονόμαζαν την Κορώνη και τη γειτονική Μεθώνη «τα μάτια της Γαληνοτάτης», γιατί από εκεί έλεγχαν τα πλοία που ταξίδευαν προς την Ανατολή.", "Koroni spreads like an amphitheatre at the south-western tip of the Peloponnese, below its castle. The Venetians, who held it for about three centuries, called Koroni and neighbouring Methoni 'the eyes of the Most Serene Republic', because from there they controlled the ships sailing to the East."),
  L("Ρεπόρτερ", "f", "Το ιδιαίτερο με αυτό το κάστρο είναι ότι παραμένει ζωντανό. Μέσα στα τείχη του ζουν ακόμη μερικές οικογένειες, και λειτουργεί ένα γυναικείο μοναστήρι, του οποίου οι μοναχές καλλιεργούν λουλούδια και κηπευτικά ανάμεσα στα ερείπια.", "What is special about this castle is that it is still alive. A few families still live inside its walls, and there is a convent whose nuns grow flowers and vegetables among the ruins."),
  L("Ρεπόρτερ", "f", "Από τις επάλξεις, η θέα στον Μεσσηνιακό κόλπο κόβει την ανάσα. Και ακριβώς κάτω από το κάστρο βρίσκεται η Ζάγκα, μια μεγάλη αμμουδιά με καθαρά νερά, ιδανική για ένα μπάνιο μετά τη βόλτα.", "From the battlements, the view over the Messenian Gulf is breathtaking. And right below the castle lies Zaga, a long sandy beach with clear water, ideal for a swim after the walk."),
 ],
 "questions": [
  Q("Γιατί οι Ενετοί ονόμαζαν την Κορώνη και τη Μεθώνη «μάτια»;", ["Γιατί είχαν όμορφους φάρους", "Γιατί από εκεί έλεγχαν τα πλοία προς την Ανατολή", "Γιατί είχαν σχήμα ματιού", "Γιατί ήταν οι πλουσιότερες πόλεις τους"], 1, "από εκεί έλεγχαν τα πλοία που ταξίδευαν προς την Ανατολή"),
  Q("Τι κάνει το κάστρο «ζωντανό»;", ["Οι συναυλίες που γίνονται εκεί", "Το ότι ζουν ακόμη οικογένειες μέσα στα τείχη και λειτουργεί μοναστήρι", "Οι αρχαιολογικές ανασκαφές", "Οι πολλοί τουρίστες"], 1, "Μέσα στα τείχη του ζουν ακόμη μερικές οικογένειες, και λειτουργεί ένα γυναικείο μοναστήρι"),
  Q("Τι είναι η Ζάγκα;", ["Ένα χωριό στο βουνό", "Μια μεγάλη αμμουδιά κάτω από το κάστρο", "Ένα ενετικό λιμάνι", "Το μοναστήρι του κάστρου"], 1, "η Ζάγκα, μια μεγάλη αμμουδιά με καθαρά νερά"),
 ],
 "gloss": {"αμφιθεατρικά": "αμφιθεατρικά — like an amphitheatre (in tiers)", "Ενετοί": "Ενετός — Venetian", "κατείχαν": "κατέχω — to hold, occupy", "Γαληνοτάτης": "Γαληνοτάτη — the Most Serene Republic (Venice)", "τείχη": "τείχος — (city) wall", "μοναχές": "μοναχή — nun", "κηπευτικά": "κηπευτικά — vegetables", "ερείπια": "ερείπιο — ruin", "επάλξεις": "έπαλξη — battlement", "αμμουδιά": "αμμουδιά — sandy beach"},
})

ITEMS.append({
 "id": "l62-dia-myelos", "title": "Εγγραφή δότη μυελού των οστών", "title_en": "Registering as a bone marrow donor", "type": "dialogue", "level": "B2",
 "context_el": "Σε ένα περίπτερο ενημέρωσης στην πανεπιστημιούπολη, ένας φοιτητής μιλά με μια εθελόντρια για τη δωρεά μυελού των οστών.",
 "script": [
  L("Φοιτητής", "m", "Καλημέρα. Είδα την αφίσα σας. Τι ακριβώς χρειάζεται για να γραφτώ ως δότης μυελού;", "Good morning. I saw your poster. What exactly do I need to do to register as a marrow donor?"),
  L("Εθελόντρια", "f", "Είναι πολύ απλό. Συμπληρώνετε ένα έντυπο, και μετά παίρνουμε δείγμα από το εσωτερικό του μάγουλου με μια μπατονέτα. Δεν πονάει καθόλου. Το δείγμα αναλύεται και τα στοιχεία σας μπαίνουν στο μητρώο δοτών.", "It's very simple. You fill in a form, and then we take a sample from the inside of your cheek with a swab. It doesn't hurt at all. The sample is analysed and your details go into the donor registry."),
  L("Φοιτητής", "m", "Και αν βρεθεί κάποιος ασθενής που ταιριάζει μαζί μου; Φοβάμαι λίγο τις βελόνες, να σας πω την αλήθεια.", "And if a patient who matches me is found? I'm a bit afraid of needles, to tell you the truth."),
  L("Εθελόντρια", "f", "Η πιθανότητα να σας καλέσουν είναι μικρή, αλλά αν συμβεί, στις περισσότερες περιπτώσεις τα κύτταρα συλλέγονται από το αίμα, με μια διαδικασία που μοιάζει με αιμοδοσία. Μπορείτε να γραφτείτε από τα δεκαοκτώ σας, και φυσικά μπορείτε να αποσυρθείτε από το μητρώο όποτε θέλετε.", "The chance of being called is small, but if it happens, in most cases the cells are collected from the blood, in a procedure similar to giving blood. You can register from the age of eighteen, and of course you can withdraw from the registry whenever you like."),
 ],
 "questions": [
  Q("Πώς παίρνεται το δείγμα κατά την εγγραφή;", ["Με εξέταση αίματος", "Με μπατονέτα από το εσωτερικό του μάγουλου", "Με μια μικρή ένεση", "Από ένα τρίχωμα"], 1, "παίρνουμε δείγμα από το εσωτερικό του μάγουλου με μια μπατονέτα"),
  Q("Τι φοβάται λίγο ο φοιτητής;", ["Τα νοσοκομεία", "Τις βελόνες", "Το αίμα", "Τις παρενέργειες"], 1, "Φοβάμαι λίγο τις βελόνες"),
  Q("Τι ισχύει, αν κάποιος αλλάξει γνώμη μετά την εγγραφή;", ["Πρέπει να πληρώσει πρόστιμο", "Μπορεί να αποσυρθεί από το μητρώο όποτε θέλει", "Δεν μπορεί να αποσυρθεί για πέντε χρόνια", "Πρέπει να το δηλώσει στον γιατρό του"], 1, "μπορείτε να αποσυρθείτε από το μητρώο όποτε θέλετε"),
 ],
 "gloss": {"μυελού των οστών": "μυελός των οστών — bone marrow", "δότης": "δότης — donor", "έντυπο": "έντυπο — form", "μάγουλου": "μάγουλο — cheek", "μπατονέτα": "μπατονέτα — cotton swab", "μητρώο δοτών": "μητρώο δοτών — donor registry", "κύτταρα": "κύτταρο — cell", "συλλέγονται": "συλλέγομαι — to be collected", "αποσυρθείτε": "αποσύρομαι — to withdraw"},
})

ITEMS.append({
 "id": "l62-mono-eparchia", "title": "Από την Αθήνα στην επαρχία", "title_en": "From Athens to the provinces", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να μιλά σε ένα podcast για τη μετακόμισή της από την Αθήνα σε μια μικρή πόλη.",
 "script": [
  L("Αφροδίτη", "f", "Πριν από τρία χρόνια, με τον άντρα μου και τα δύο παιδιά μας, αφήσαμε την Αθήνα και μετακομίσαμε στην Καλαμπάκα, από όπου κατάγεται η μητέρα μου. Ο λόγος ήταν απλός: περνούσαμε σχεδόν δύο ώρες κάθε μέρα στην κίνηση και δεν βλέπαμε τα παιδιά μας.", "Three years ago, my husband, our two children and I left Athens and moved to Kalambaka, where my mother comes from. The reason was simple: we spent almost two hours a day in traffic and never saw our children."),
  L("Αφροδίτη", "f", "Εγώ δουλεύω πλέον εξ αποστάσεως για την ίδια εταιρεία, ενώ ο άντρας μου άνοιξε ένα μικρό εργαστήριο επίπλων. Τα παιδιά πάνε με τα πόδια στο σχολείο, και το απόγευμα παίζουν έξω χωρίς να ανησυχούμε.", "I now work remotely for the same company, while my husband opened a small furniture workshop. The children walk to school, and in the afternoon they play outside without us worrying."),
  L("Αφροδίτη", "f", "Δεν είναι όλα ρόδινα, βέβαια. Μου λείπουν τα θέατρα και οι φίλοι μου, και για κάθε ειδικό γιατρό πρέπει να πάμε στη Λάρισα ή στα Τρίκαλα. Αλλά όταν ανοίγω το παράθυρο το πρωί και βλέπω τα Μετέωρα, ξέρω ότι πήραμε τη σωστή απόφαση.", "Not everything is rosy, of course. I miss the theatres and my friends, and for any specialist doctor we have to go to Larissa or Trikala. But when I open the window in the morning and see the Meteora, I know we made the right decision."),
 ],
 "questions": [
  Q("Γιατί αποφάσισαν να φύγουν από την Αθήνα;", ["Γιατί έχασαν τις δουλειές τους", "Γιατί περνούσαν πολλές ώρες στην κίνηση και δεν έβλεπαν τα παιδιά τους", "Γιατί τα ενοίκια ήταν ακριβά", "Γιατί αρρώστησε η μητέρα της"], 1, "περνούσαμε σχεδόν δύο ώρες κάθε μέρα στην κίνηση και δεν βλέπαμε τα παιδιά μας"),
  Q("Τι κάνει σήμερα ο άντρας της;", ["Δουλεύει εξ αποστάσεως", "Έχει ένα μικρό εργαστήριο επίπλων", "Είναι δάσκαλος", "Δουλεύει στα Τρίκαλα"], 1, "ο άντρας μου άνοιξε ένα μικρό εργαστήριο επίπλων"),
  Q("Ποιο μειονέκτημα αναφέρει;", ["Το κρύο του χειμώνα", "Ότι για ειδικό γιατρό πρέπει να πάνε σε άλλη πόλη", "Το κακό ίντερνετ", "Τους λίγους συμμαθητές των παιδιών"], 1, "για κάθε ειδικό γιατρό πρέπει να πάμε στη Λάρισα ή στα Τρίκαλα"),
 ],
 "gloss": {"κατάγεται": "κατάγομαι — to come from, originate", "κίνηση": "κίνηση — traffic", "εξ αποστάσεως": "εξ αποστάσεως — remotely", "εργαστήριο επίπλων": "εργαστήριο επίπλων — furniture workshop", "ρόδινα": "ρόδινος — rosy", "ειδικό γιατρό": "ειδικός γιατρός — specialist doctor"},
})

ITEMS.append({
 "id": "l62-c1-afalatosi", "title": "Αφαλάτωση: πόσιμο νερό από τη θάλασσα", "title_en": "Desalination: drinking water from the sea", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για το περιβάλλον, ένας δημοσιογράφος συζητά με μια μηχανικό για τις μονάδες αφαλάτωσης στα νησιά.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλά νησιά μας στηρίζονται πλέον στην αφαλάτωση για να καλύψουν τις ανάγκες τους σε νερό, ιδίως το καλοκαίρι. Πώς λειτουργεί, με απλά λόγια, μια τέτοια μονάδα;", "Many of our islands now rely on desalination to cover their water needs, especially in summer. How does such a plant work, in simple terms?"),
  L("Μηχανικός", "f", "Η πιο διαδεδομένη μέθοδος είναι η αντίστροφη όσμωση. Το θαλασσινό νερό, αφού φιλτραριστεί, πιέζεται με μεγάλη δύναμη μέσα από ειδικές μεμβράνες, οι οποίες αφήνουν να περάσουν τα μόρια του νερού αλλά συγκρατούν το αλάτι. Το αποτέλεσμα είναι νερό κατάλληλο για πόση, αφού προστεθούν και κάποια μεταλλικά στοιχεία.", "The most widespread method is reverse osmosis. Seawater, after being filtered, is pushed with great force through special membranes, which let water molecules pass but hold back the salt. The result is water fit to drink, once certain minerals have also been added."),
  L("Δημοσιογράφος", "m", "Ακούγεται σαν η ιδανική λύση. Πού βρίσκεται το πρόβλημα;", "It sounds like the ideal solution. Where's the catch?"),
  L("Μηχανικός", "f", "Σε δύο σημεία. Πρώτον, η διαδικασία καταναλώνει πολλή ενέργεια, που στα περισσότερα νησιά παράγεται ακόμη από πετρέλαιο. Δεύτερον, το υπόλειμμα, η λεγόμενη άλμη, είναι πολύ πιο αλμυρό από τη θάλασσα, και αν απορρίπτεται χωρίς σχεδιασμό, μπορεί να βλάψει τη θαλάσσια ζωή κοντά στις ακτές. Η αφαλάτωση, λοιπόν, είναι πολύτιμη, εφόσον συνδυάζεται με ανανεώσιμες πηγές ενέργειας και, κυρίως, με τη μείωση των απωλειών στα δίκτυα ύδρευσης, που σε ορισμένους δήμους ξεπερνούν το ένα τρίτο του νερού.", "In two places. First, the process consumes a lot of energy, which on most islands is still produced from oil. Second, the residue, the so-called brine, is much saltier than the sea, and if it is discharged without planning it can harm marine life near the coast. So desalination is valuable, provided it is combined with renewable energy and, above all, with reducing losses in the water networks, which in some municipalities exceed a third of the water."),
 ],
 "questions": [
  Q("Τι κάνουν οι μεμβράνες στην αντίστροφη όσμωση;", ["Ζεσταίνουν το νερό", "Αφήνουν να περάσει το νερό αλλά συγκρατούν το αλάτι", "Προσθέτουν μεταλλικά στοιχεία", "Σκοτώνουν τα μικρόβια"], 1, "αφήνουν να περάσουν τα μόρια του νερού αλλά συγκρατούν το αλάτι"),
  Q("Ποιο είναι το πρώτο πρόβλημα που αναφέρει η μηχανικός;", ["Το υψηλό κόστος των μεμβρανών", "Η μεγάλη κατανάλωση ενέργειας, που συχνά παράγεται από πετρέλαιο", "Η κακή γεύση του νερού", "Η έλλειψη ειδικευμένου προσωπικού"], 1, "η διαδικασία καταναλώνει πολλή ενέργεια, που στα περισσότερα νησιά παράγεται ακόμη από πετρέλαιο"),
  Q("Τι είναι η άλμη;", ["Το φιλτραρισμένο θαλασσινό νερό", "Το πολύ αλμυρό υπόλειμμα της διαδικασίας", "Ένα είδος μεμβράνης", "Το πόσιμο νερό πριν προστεθούν μέταλλα"], 1, "το υπόλειμμα, η λεγόμενη άλμη, είναι πολύ πιο αλμυρό από τη θάλασσα"),
  Q("Υπό ποιες προϋποθέσεις θεωρεί η μηχανικός την αφαλάτωση πολύτιμη;", ["Αν χρησιμοποιείται μόνο τον χειμώνα", "Αν συνδυάζεται με ανανεώσιμες πηγές και με μείωση των απωλειών στα δίκτυα", "Αν τη χρηματοδοτεί η Ευρωπαϊκή Ένωση", "Αν οι μονάδες χτίζονται μακριά από τα νησιά"], 1, "εφόσον συνδυάζεται με ανανεώσιμες πηγές ενέργειας και, κυρίως, με τη μείωση των απωλειών στα δίκτυα ύδρευσης"),
 ],
 "gloss": {"αφαλάτωση": "αφαλάτωση — desalination", "αντίστροφη όσμωση": "αντίστροφη όσμωση — reverse osmosis", "μεμβράνες": "μεμβράνη — membrane", "μόρια": "μόριο — molecule", "πόση": "πόση — drinking", "μεταλλικά στοιχεία": "μεταλλικά στοιχεία — minerals", "υπόλειμμα": "υπόλειμμα — residue", "άλμη": "άλμη — brine", "απορρίπτεται": "απορρίπτομαι — to be discharged, dumped", "απωλειών": "απώλεια — loss", "δίκτυα ύδρευσης": "δίκτυο ύδρευσης — water supply network"},
})

ITEMS.append({
 "id": "l62-c1-eptanisa", "title": "Η ένωση των Επτανήσων", "title_en": "The union of the Ionian Islands", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από διάλεξη ιστορικού για την ένωση των Ιονίων νησιών με την Ελλάδα το 1864.",
 "script": [
  L("Ιστορικός", "m", "Όταν ιδρύθηκε το ελληνικό κράτος, τα Επτάνησα δεν συμπεριλήφθηκαν σε αυτό. Από το 1815 αποτελούσαν ένα κράτος υπό βρετανική προστασία, το λεγόμενο Ηνωμένο Κράτος των Ιονίων Νήσων, με δική του Βουλή αλλά με τον πραγματικό έλεγχο στα χέρια ενός Βρετανού Αρμοστή.", "When the Greek state was founded, the Ionian Islands were not included in it. From 1815 they formed a state under British protection, the so-called United States of the Ionian Islands, with its own parliament but with real control in the hands of a British Lord High Commissioner."),
  L("Ιστορικός", "m", "Στα μέσα του αιώνα, το κίνημα των Ριζοσπαστών έθεσε ανοιχτά το αίτημα της ένωσης με την Ελλάδα, και η Ιόνιος Βουλή το υιοθέτησε επανειλημμένα, παρά τις διώξεις. Η ευκαιρία ήρθε το 1863, όταν η Βρετανία, θέλοντας να στηρίξει τον νέο βασιλιά Γεώργιο Α΄, δέχτηκε να παραχωρήσει τα νησιά ως ένα είδος «δώρου» για την ενθρόνισή του.", "In the middle of the century, the Radical movement openly raised the demand for union with Greece, and the Ionian Parliament adopted it repeatedly, despite persecution. The opportunity came in 1863, when Britain, wishing to support the new King George I, agreed to cede the islands as a kind of 'gift' for his accession."),
  L("Ιστορικός", "m", "Το δώρο, όμως, είχε όρους. Η Κέρκυρα και οι Παξοί κηρύχθηκαν ουδέτερες, και οι Βρετανοί, πριν αποχωρήσουν, ανατίναξαν μεγάλο μέρος των οχυρώσεων της Κέρκυρας. Παρ’ όλα αυτά, στις 21 Μαΐου 1864 η ένωση έγινε πραγματικότητα. Ήταν η πρώτη ειρηνική επέκταση του ελληνικού κράτους, και έφερε στην Αθήνα μια παράδοση παιδείας, μουσικής και λογοτεχνίας που θα σφράγιζε τον νεοελληνικό πολιτισμό.", "But the gift came with conditions. Corfu and Paxoi were declared neutral, and the British, before leaving, blew up a large part of Corfu's fortifications. Nevertheless, on 21 May 1864 the union became a reality. It was the first peaceful expansion of the Greek state, and it brought to Athens a tradition of education, music and literature that would leave its mark on modern Greek culture."),
 ],
 "questions": [
  Q("Ποιο ήταν το καθεστώς των Επτανήσων από το 1815;", ["Ήταν μέρος της Οθωμανικής Αυτοκρατορίας", "Ήταν κράτος υπό βρετανική προστασία", "Ανήκαν στη Βενετία", "Ήταν ανεξάρτητο κράτος χωρίς ξένο έλεγχο"], 1, "αποτελούσαν ένα κράτος υπό βρετανική προστασία"),
  Q("Ποιο κίνημα έθεσε ανοιχτά το αίτημα της ένωσης;", ["Οι Φιλικοί", "Οι Ριζοσπάστες", "Οι Διαφωτιστές", "Οι Βενιζελικοί"], 1, "το κίνημα των Ριζοσπαστών έθεσε ανοιχτά το αίτημα της ένωσης"),
  Q("Γιατί δέχτηκε η Βρετανία να παραχωρήσει τα νησιά;", ["Γιατί έχασε έναν πόλεμο", "Για να στηρίξει τον νέο βασιλιά Γεώργιο Α΄", "Γιατί τα νησιά ήταν φτωχά", "Γιατί το ζήτησε η Γαλλία"], 1, "θέλοντας να στηρίξει τον νέο βασιλιά Γεώργιο Α΄"),
  Q("Ποιον όρο αναφέρει ο ομιλητής;", ["Η Κέρκυρα και οι Παξοί κηρύχθηκαν ουδέτερες", "Οι Βρετανοί κράτησαν τη Ζάκυνθο", "Τα νησιά θα πλήρωναν φόρο στη Βρετανία", "Η Ιόνιος Βουλή θα συνέχιζε να λειτουργεί"], 0, "Η Κέρκυρα και οι Παξοί κηρύχθηκαν ουδέτερες"),
 ],
 "gloss": {"συμπεριλήφθηκαν": "συμπεριλαμβάνομαι — to be included", "Αρμοστή": "Αρμοστής — (Lord High) Commissioner", "Ριζοσπαστών": "Ριζοσπάστης — Radical (Ionian unionist party)", "επανειλημμένα": "επανειλημμένα — repeatedly", "διώξεις": "δίωξη — persecution", "παραχωρήσει": "παραχωρώ — to cede", "ενθρόνισή": "ενθρόνιση — accession, enthronement", "ουδέτερες": "ουδέτερος — neutral", "ανατίναξαν": "ανατινάζω — to blow up", "οχυρώσεων": "οχύρωση — fortification"},
})

rnd = random.Random(62)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-62.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
