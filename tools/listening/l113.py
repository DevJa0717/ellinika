# Source for library/listening/listening-113.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l113.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l113-ann-vatrachoi-dromos", "title": "Κλειστός δρόμος τις νύχτες για τους βατράχους", "title_en": "A road closed at night for the frogs", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου στο τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνητής", "m", "Ο δήμος ενημερώνει ότι από τη Δευτέρα και για τρεις εβδομάδες ο παραλίμνιος δρόμος θα κλείνει κάθε βράδυ από τις οκτώ μέχρι τις έξι το πρωί. Αυτή την εποχή χιλιάδες βάτραχοι και φρύνοι κατεβαίνουν από το δάσος προς τη λίμνη για να γεννήσουν, και πολλοί σκοτώνονται από τα αυτοκίνητα.", "The municipality announces that from Monday and for three weeks the lakeside road will close every evening from eight until six in the morning. At this time of year thousands of frogs and toads come down from the forest to the lake to spawn, and many are killed by cars."),
  L("Εκφωνητής", "m", "Οι κάτοικοι των σπιτιών κατά μήκος του δρόμου θα μπορούν να περνούν, αλλά παρακαλούνται να οδηγούν πολύ αργά και να προσέχουν. Τα λεωφορεία της γραμμής θα ακολουθούν τον δρόμο μέσα από το χωριό.", "Residents of the houses along the road will be able to pass, but are asked to drive very slowly and carefully. The buses on the route will take the road through the village."),
  L("Εκφωνητής", "m", "Ο δήμος αναζητά επίσης εθελοντές που θα μαζεύουν με κουβάδες τα ζώα από την άκρη του δρόμου και θα τα μεταφέρουν στην όχθη. Όσοι ενδιαφέρονται, να φέρουν φακό και γάντια και να έρθουν στο πάρκινγκ του αναψυκτηρίου στις οκτώ.", "The municipality is also looking for volunteers to collect the animals in buckets from the roadside and carry them to the shore. Those interested should bring a torch and gloves and come to the car park of the snack bar at eight."),
 ],
 "questions": [
  Q("Γιατί θα κλείνει ο δρόμος τις νύχτες;", ["Γιατί θα γίνουν έργα", "Γιατί οι βάτραχοι κατεβαίνουν στη λίμνη και σκοτώνονται από τα αυτοκίνητα", "Γιατί πλημμυρίζει από τη λίμνη", "Γιατί δεν έχει φωτισμό"], 1, "πολλοί σκοτώνονται από τα αυτοκίνητα"),
  Q("Τι θα κάνουν τα λεωφορεία;", ["Δεν θα κυκλοφορούν τα βράδια", "Θα περνούν πολύ αργά", "Θα ακολουθούν τον δρόμο μέσα από το χωριό", "Θα σταματούν στο αναψυκτήριο"], 2, "θα ακολουθούν τον δρόμο μέσα από το χωριό"),
  Q("Τι πρέπει να φέρουν οι εθελοντές;", ["Φακό και γάντια", "Κουβάδες και δίχτυα", "Γιλέκο και μπότες", "Φαγητό για τα ζώα"], 0, "να φέρουν φακό και γάντια"),
 ],
 "gloss": {"παραλίμνιος": "παραλίμνιος — lakeside", "βάτραχοι": "βάτραχος — frog", "φρύνοι": "φρύνος — toad", "γεννήσουν": "γεννώ — to lay eggs, spawn, give birth", "κατά μήκος": "κατά μήκος — along", "κουβάδες": "κουβάς — bucket", "όχθη": "όχθη — bank, shore", "φακό": "φακός — torch, flashlight", "αναψυκτηρίου": "αναψυκτήριο — snack bar, café"}
})

ITEMS.append({
 "id": "l113-vm-ktiniatros-emvolio", "title": "Μήνυμα από την κτηνιατρική κλινική", "title_en": "A message from the vet clinic", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε σκύλο. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Γραμματέας", "f", "Καλημέρα σας, από την κτηνιατρική κλινική «Άργος» σας καλούμε. Σας υπενθυμίζουμε ότι ο Μπρούνο έχει το ετήσιο εμβόλιο λύσσας μέσα στον μήνα. Η γιατρός προτείνει την ίδια μέρα να του κάνουμε και το τεστ για τη λεϊσμανίαση, αφού έχει περάσει ένας χρόνος από το προηγούμενο.", "Good morning, we're calling from the Argos veterinary clinic. We'd like to remind you that Bruno is due for his annual rabies vaccine this month. The vet suggests also doing his leishmaniasis test on the same day, since a year has passed since the last one."),
  L("Γραμματέας", "f", "Για το τεστ χρειάζεται λίγο αίμα, οπότε καλό θα ήταν να μην έχει φάει τίποτα τις τελευταίες οκτώ ώρες. Γι' αυτό σας προτείνουμε ραντεβού νωρίς το πρωί. Έχουμε διαθέσιμες ώρες την Τετάρτη και την Παρασκευή στις εννιά.", "The test needs a little blood, so it would be best if he hasn't eaten anything for the last eight hours. That's why we suggest an appointment early in the morning. We have slots available on Wednesday and Friday at nine."),
  L("Γραμματέας", "f", "Μην ξεχάσετε να φέρετε το βιβλιάριο υγείας του, για να περάσουμε το εμβόλιο. Αν θέλετε, μπορούμε να σας δώσουμε και το αντιπαρασιτικό χάπι για τους επόμενους τρεις μήνες. Για επιβεβαίωση, καλέστε μας ή στείλτε μήνυμα σε αυτόν τον αριθμό.", "Don't forget to bring his health booklet so we can record the vaccine. If you like, we can also give you the antiparasitic tablet for the next three months. To confirm, call us or send a message to this number."),
 ],
 "questions": [
  Q("Τι προτείνει η γιατρός να γίνει την ίδια μέρα με το εμβόλιο;", ["Ένα μπάνιο", "Το τεστ για τη λεϊσμανίαση", "Ένα τσιπάκι", "Μια ακτινογραφία"], 1, "την ίδια μέρα να του κάνουμε και το τεστ για τη λεϊσμανίαση"),
  Q("Γιατί προτείνουν ραντεβού νωρίς το πρωί;", ["Γιατί το απόγευμα η κλινική είναι κλειστή", "Γιατί ο σκύλος είναι πιο ήρεμος", "Γιατί ο σκύλος καλό είναι να μην έχει φάει πριν από το τεστ", "Γιατί έχει λιγότερη κίνηση"], 2, "καλό θα ήταν να μην έχει φάει τίποτα τις τελευταίες οκτώ ώρες"),
  Q("Τι πρέπει να φέρει ο ιδιοκτήτης;", ["Το βιβλιάριο υγείας του σκύλου", "Ένα δείγμα τροφής", "Το λουρί και το φίμωτρο", "Την απόδειξη της προηγούμενης επίσκεψης"], 0, "να φέρετε το βιβλιάριο υγείας του"),
 ],
 "gloss": {"κτηνιατρική": "κτηνιατρικός — veterinary", "υπενθυμίζουμε": "υπενθυμίζω — to remind", "λύσσας": "λύσσα — rabies", "λεϊσμανίαση": "λεϊσμανίαση — leishmaniasis (a parasitic disease spread by sandflies)", "διαθέσιμες": "διαθέσιμος — available", "βιβλιάριο": "βιβλιάριο υγείας — health booklet", "αντιπαρασιτικό": "αντιπαρασιτικός — antiparasitic", "επιβεβαίωση": "επιβεβαίωση — confirmation"}
})

ITEMS.append({
 "id": "l113-dia-fovos-ptisis", "title": "Φοβάμαι να πετάξω", "title_en": "I'm afraid of flying", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλες που ετοιμάζουν ένα ταξίδι στη Λισαβόνα.",
 "script": [
  L("Δανάη", "f", "Βρήκα εισιτήρια για τη Λισαβόνα σε πολύ καλή τιμή. Να τα κλείσω; Λέμε για τον Μάρτιο, σωστά;", "I found tickets to Lisbon at a really good price. Shall I book them? We said March, right?"),
  L("Ρένα", "f", "Πρέπει να σου πω κάτι. Από τότε που είχαμε εκείνες τις αναταράξεις στην πτήση για τη Ρόδο, φοβάμαι να πετάξω. Την τελευταία φορά έτρεμα ολόκληρη και δεν μπορούσα να ανασάνω. Σκεφτόμουν μήπως πάμε με τρένο, έστω κι αν κάνουμε δύο μέρες.", "I have to tell you something. Ever since we had that turbulence on the flight to Rhodes, I'm afraid of flying. Last time I was shaking all over and couldn't breathe. I was wondering if we could go by train, even if it takes us two days."),
  L("Δανάη", "f", "Σε καταλαβαίνω, αλλά οι αναταράξεις είναι κάτι πολύ συνηθισμένο, τα αεροπλάνα είναι φτιαγμένα για να τις αντέχουν. Ξέρεις ότι κάποιες αεροπορικές οργανώνουν σεμινάρια για όσους φοβούνται να πετάξουν; Σου εξηγεί ένας πιλότος τι ακριβώς συμβαίνει και μαθαίνεις ασκήσεις αναπνοής.", "I understand, but turbulence is very common; planes are built to withstand it. Did you know some airlines run seminars for people who are afraid of flying? A pilot explains exactly what happens and you learn breathing exercises."),
  L("Ρένα", "f", "Δεν το ήξερα. Εντάξει, θα το ψάξω. Αν βρω κάποιο πριν από τον Μάρτιο, κλείνουμε. Αλλά θα κάτσω στον διάδρομο, όχι στο παράθυρο, και θα μου κρατάς το χέρι.", "I didn't know that. OK, I'll look into it. If I find one before March, we'll book. But I'm sitting on the aisle, not by the window, and you'll hold my hand."),
 ],
 "questions": [
  Q("Πότε άρχισε η Ρένα να φοβάται να πετάξει;", ["Όταν ήταν παιδί", "Μετά από αναταράξεις σε μια πτήση για τη Ρόδο", "Όταν είδε ένα ντοκιμαντέρ", "Όταν έχασε μια πτήση"], 1, "Από τότε που είχαμε εκείνες τις αναταράξεις στην πτήση για τη Ρόδο"),
  Q("Τι προτείνει η Δανάη;", ["Να πάνε με τρένο", "Να αναβάλουν το ταξίδι", "Ένα σεμινάριο για όσους φοβούνται να πετάξουν", "Να πάρει ένα ηρεμιστικό"], 2, "κάποιες αεροπορικές οργανώνουν σεμινάρια για όσους φοβούνται να πετάξουν"),
  Q("Τι ζητά η Ρένα για την πτήση;", ["Να κάτσει στον διάδρομο και να της κρατά η φίλη της το χέρι", "Να κάτσει στο παράθυρο", "Να πετάξουν πρωί", "Να πάρουν απευθείας πτήση"], 0, "θα κάτσω στον διάδρομο, όχι στο παράθυρο, και θα μου κρατάς το χέρι"),
 ],
 "gloss": {"αναταράξεις": "αναταράξεις — turbulence", "πτήση": "πτήση — flight", "έτρεμα": "τρέμω — to shake, tremble", "ανασάνω": "ανασαίνω — to breathe", "έστω κι αν": "έστω κι αν — even if", "αντέχουν": "αντέχω — to withstand, bear", "αεροπορικές": "αεροπορική (εταιρεία) — airline", "αναπνοής": "αναπνοή — breathing", "διάδρομο": "διάδρομος — aisle, corridor"}
})

ITEMS.append({
 "id": "l113-int-xyloglyptis-templa", "title": "Ένας ξυλογλύπτης τέμπλων", "title_en": "A carver of church screens", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν ξυλογλύπτη σε ραδιοφωνική εκπομπή για τις τέχνες.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Ζαφείρη, εσείς φτιάχνετε ξυλόγλυπτα τέμπλα για εκκλησίες. Πώς ξεκινήσατε;", "Mr Zafeiris, you make carved wooden screens for churches. How did you start?"),
  L("Ξυλογλύπτης", "m", "Ο πατέρας μου ήταν ξυλουργός και από μικρός περνούσα τα απογεύματα στο εργαστήριο. Στα δεκαέξι ένας γέρος ξυλογλύπτης με πήρε μαθητευόμενο. Τα πρώτα δύο χρόνια μόνο ακόνιζα τα σκαρπέλα και σκάλιζα φύλλα σε κομμάτια που πετούσαμε.", "My father was a carpenter, and from a young age I spent my afternoons in the workshop. At sixteen an old woodcarver took me on as an apprentice. For the first two years I only sharpened the chisels and carved leaves on pieces we threw away."),
  L("Δημοσιογράφος", "f", "Πόσο καιρό χρειάζεται ένα τέμπλο;", "How long does a screen take?"),
  L("Ξυλογλύπτης", "m", "Για μια μικρή εκκλησία, γύρω στους οκτώ μήνες. Δουλεύω κυρίως καρυδιά, που είναι σκληρή αλλά σκαλίζεται όμορφα. Τα σχέδια είναι παραδοσιακά: κλήματα, σταφύλια, πουλιά, καμιά φορά ο δικέφαλος αετός. Τίποτα δεν γίνεται με μηχάνημα· όλα με το χέρι.", "For a small church, about eight months. I mainly work walnut, which is hard but carves beautifully. The designs are traditional: vines, grapes, birds, sometimes the double-headed eagle. Nothing is done by machine; everything by hand."),
  L("Δημοσιογράφος", "f", "Υπάρχουν νέοι που θέλουν να μάθουν την τέχνη;", "Are there young people who want to learn the craft?"),
  L("Ξυλογλύπτης", "m", "Λίγοι, αλλά υπάρχουν. Έχω δύο μαθήτριες αυτή τη στιγμή. Το δύσκολο δεν είναι η τεχνική, είναι η υπομονή. Ένα λάθος στο ξύλο δεν σβήνεται· πρέπει να το κάνεις κομμάτι του σχεδίου.", "Few, but they exist. I have two apprentices right now. The hard part isn't the technique, it's the patience. A mistake in wood can't be erased; you have to make it part of the design."),
 ],
 "questions": [
  Q("Τι έκανε τα πρώτα χρόνια ως μαθητευόμενος;", ["Έφτιαχνε μικρά τέμπλα", "Ακόνιζε τα σκαρπέλα και σκάλιζε φύλλα σε κομμάτια που πετούσαν", "Μάζευε ξύλα από το δάσος", "Έβαφε τα έργα του δασκάλου του"], 1, "μόνο ακόνιζα τα σκαρπέλα και σκάλιζα φύλλα σε κομμάτια που πετούσαμε"),
  Q("Γιατί προτιμά την καρυδιά;", ["Γιατί είναι φτηνή", "Γιατί είναι ελαφριά", "Γιατί είναι σκληρή αλλά σκαλίζεται όμορφα", "Γιατί δεν τη χαλάνε τα έντομα"], 2, "είναι σκληρή αλλά σκαλίζεται όμορφα"),
  Q("Ποιο είναι κατά τη γνώμη του το πιο δύσκολο στην τέχνη του;", ["Η υπομονή", "Η τεχνική", "Η εύρεση πελατών", "Το κόστος του ξύλου"], 0, "Το δύσκολο δεν είναι η τεχνική, είναι η υπομονή"),
 ],
 "gloss": {"ξυλογλύπτη": "ξυλογλύπτης — woodcarver", "τέμπλα": "τέμπλο — iconostasis, carved screen in an Orthodox church", "μαθητευόμενο": "μαθητευόμενος — apprentice", "ακόνιζα": "ακονίζω — to sharpen", "σκαρπέλα": "σκαρπέλο — chisel", "σκάλιζα": "σκαλίζω — to carve", "καρυδιά": "καρυδιά — walnut (tree, wood)", "κλήματα": "κλήμα — vine", "δικέφαλος": "δικέφαλος αετός — double-headed eagle", "υπομονή": "υπομονή — patience"}
})

ITEMS.append({
 "id": "l113-rep-chalazi-ampelia", "title": "Χαλάζι στα αμπέλια λίγο πριν από τον τρύγο", "title_en": "Hail on the vineyards just before the harvest", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στις τοπικές ειδήσεις.",
 "script": [
  L("Ρεπόρτερ", "f", "Μια καταιγίδα που κράτησε μόλις είκοσι λεπτά ήταν αρκετή για να καταστρέψει τη χρονιά πολλών αμπελουργών. Το χαλάζι, σε μέγεθος καρυδιού σε ορισμένα σημεία, έπεσε χθες το απόγευμα στα χωριά της περιοχής, μόλις δέκα μέρες πριν από τον τρύγο.", "A storm that lasted just twenty minutes was enough to ruin the year for many winegrowers. The hail, the size of a walnut in some places, fell yesterday afternoon on the villages of the area, just ten days before the harvest."),
  L("Ρεπόρτερ", "f", "«Σε μερικά κτήματα δεν έμεινε ούτε ένα τσαμπί», λέει ο πρόεδρος του αγροτικού συνεταιρισμού. «Όπου τα σταφύλια σώθηκαν, έχουν χτυπήματα και θα πρέπει να τα μαζέψουμε αμέσως, πριν σαπίσουν. Το κρασί φέτος θα είναι πολύ λιγότερο.»", "\"In some vineyards not a single bunch was left,\" says the president of the farmers' cooperative. \"Where the grapes survived, they're bruised and we'll have to pick them immediately, before they rot. There will be much less wine this year.\""),
  L("Ρεπόρτερ", "f", "Οι αμπελουργοί καλούνται να δηλώσουν τις ζημιές στον ΕΛΓΑ μέσα σε λίγες μέρες, ώστε να έρθουν οι εκτιμητές πριν από τη συγκομιδή. Ο συνεταιρισμός ζητά επίσης από τους κατοίκους εθελοντική βοήθεια στον τρύγο αυτό το Σαββατοκύριακο.", "Winegrowers are asked to report the damage to ELGA, the agricultural insurance body, within a few days, so that the assessors can come before the harvest. The cooperative is also asking residents for volunteer help with the grape harvest this weekend."),
 ],
 "questions": [
  Q("Πόσο κράτησε η καταιγίδα;", ["Μια ολόκληρη νύχτα", "Μόλις είκοσι λεπτά", "Δύο ώρες", "Δέκα μέρες"], 1, "Μια καταιγίδα που κράτησε μόλις είκοσι λεπτά"),
  Q("Τι πρέπει να γίνει με τα σταφύλια που σώθηκαν;", ["Να μείνουν να ωριμάσουν", "Να πουληθούν για φαγητό", "Να μαζευτούν αμέσως, πριν σαπίσουν", "Να ψεκαστούν"], 2, "θα πρέπει να τα μαζέψουμε αμέσως, πριν σαπίσουν"),
  Q("Γιατί πρέπει οι αμπελουργοί να δηλώσουν γρήγορα τις ζημιές;", ["Για να έρθουν οι εκτιμητές πριν από τη συγκομιδή", "Για να πάρουν δάνειο", "Για να κλείσει ο δρόμος", "Για να βρουν εργάτες"], 0, "ώστε να έρθουν οι εκτιμητές πριν από τη συγκομιδή"),
 ],
 "gloss": {"καταιγίδα": "καταιγίδα — storm", "αμπελουργών": "αμπελουργός — winegrower", "χαλάζι": "χαλάζι — hail", "τρύγο": "τρύγος — grape harvest", "κτήματα": "κτήμα — estate, vineyard, plot", "τσαμπί": "τσαμπί — bunch (of grapes)", "συνεταιρισμού": "συνεταιρισμός — cooperative", "σαπίσουν": "σαπίζω — to rot", "ΕΛΓΑ": "ΕΛΓΑ — Hellenic Agricultural Insurance Organisation", "εκτιμητές": "εκτιμητής — (insurance) assessor", "συγκομιδή": "συγκομιδή — harvest"}
})

ITEMS.append({
 "id": "l113-rep-palia-dichtya", "title": "Τα παλιά δίχτυα γίνονται νήμα", "title_en": "Old fishing nets become yarn", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε εκπομπή για το περιβάλλον.",
 "script": [
  L("Ρεπόρτερ", "m", "Στο λιμάνι του νησιού έχει στηθεί ένα μεγάλο κοντέινερ με μια απλή επιγραφή: «Παλιά δίχτυα εδώ». Μέχρι πέρσι, οι ψαράδες δεν ήξεραν τι να κάνουν τα σκισμένα δίχτυα τους. Άλλα τα έκαιγαν, άλλα τα άφηναν στις αποθήκες, και κάποια, δυστυχώς, κατέληγαν στη θάλασσα.", "At the island's harbour a large container has been set up with a simple sign: \"Old nets here\". Until last year, fishermen didn't know what to do with their torn nets. Some burned them, some left them in storerooms, and some, unfortunately, ended up in the sea."),
  L("Ρεπόρτερ", "m", "Τα δίχτυα που χάνονται στη θάλασσα συνεχίζουν να πιάνουν ψάρια, χελώνες και δελφίνια για χρόνια. Γι' αυτό μια περιβαλλοντική οργάνωση, μαζί με τον σύλλογο ψαράδων, ξεκίνησε το πρόγραμμα. Τα δίχτυα πλένονται, συσκευάζονται και στέλνονται σε εργοστάσιο στο εξωτερικό, όπου το νάιλον γίνεται καινούργιο νήμα για μαγιό και κάλτσες.", "Nets lost at sea go on catching fish, turtles and dolphins for years. That's why an environmental organisation, together with the fishermen's association, started the programme. The nets are washed, packed and sent to a factory abroad, where the nylon becomes new yarn for swimsuits and socks."),
  L("Ρεπόρτερ", "m", "Μέσα σε έναν χρόνο μαζεύτηκαν σχεδόν δεκαπέντε τόνοι. Οι ψαράδες δεν πληρώνονται για τα δίχτυα, αλλά, όπως λέει ένας από αυτούς, «τουλάχιστον ξέρω ότι δεν θα σκοτώσουν τίποτα όταν πάψω να τα χρησιμοποιώ».", "Within a year almost fifteen tonnes were collected. The fishermen aren't paid for the nets, but, as one of them says, \"at least I know they won't kill anything once I stop using them\"."),
 ],
 "questions": [
  Q("Τι έκαναν πριν οι ψαράδες με τα σκισμένα δίχτυα;", ["Τα πουλούσαν", "Άλλοι τα έκαιγαν, άλλοι τα άφηναν στις αποθήκες", "Τα επισκεύαζαν πάντα", "Τα έδιναν στον δήμο"], 1, "Άλλα τα έκαιγαν, άλλα τα άφηναν στις αποθήκες"),
  Q("Γιατί είναι επικίνδυνα τα δίχτυα που χάνονται στη θάλασσα;", ["Γιατί μπλέκονται στις προπέλες", "Γιατί λερώνουν τις παραλίες", "Γιατί συνεχίζουν να πιάνουν ζώα για χρόνια", "Γιατί βουλιάζουν τα σκάφη"], 2, "συνεχίζουν να πιάνουν ψάρια, χελώνες και δελφίνια για χρόνια"),
  Q("Τι γίνεται το νάιλον των διχτυών;", ["Νήμα για μαγιό και κάλτσες", "Καύσιμο", "Υλικό για σακούλες", "Καινούργια δίχτυα"], 0, "το νάιλον γίνεται καινούργιο νήμα για μαγιό και κάλτσες"),
 ],
 "gloss": {"δίχτυα": "δίχτυ — (fishing) net", "νήμα": "νήμα — yarn, thread", "επιγραφή": "επιγραφή — sign, inscription", "σκισμένα": "σκισμένος — torn", "κατέληγαν": "καταλήγω — to end up", "συσκευάζονται": "συσκευάζω — to pack", "μαγιό": "μαγιό — swimsuit", "τόνοι": "τόνος — tonne", "πάψω": "παύω — to stop, cease"}
})

ITEMS.append({
 "id": "l113-mono-giati-chasmouriomaste", "title": "Το μυστήριο του χασμουρητού", "title_en": "The mystery of yawning", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε ένα μικρό επιστημονικό ένθετο σε ραδιοφωνική εκπομπή.",
 "script": [
  L("Παρουσιαστής", "m", "Αν χασμουρηθείτε ενώ ακούτε αυτή την εκπομπή, μην ανησυχείτε· δεν σημαίνει ότι βαριέστε. Το χασμουρητό είναι μια από τις πιο κοινές και ταυτόχρονα πιο μυστηριώδεις κινήσεις του σώματος. Το κάνουν σχεδόν όλα τα σπονδυλωτά, ακόμα και τα έμβρυα μέσα στη μήτρα.", "If you yawn while listening to this programme, don't worry; it doesn't mean you're bored. Yawning is one of the most common and at the same time most mysterious movements of the body. Almost all vertebrates do it, even foetuses in the womb."),
  L("Παρουσιαστής", "m", "Παλιότερα πιστεύαμε ότι χασμουριόμαστε επειδή χρειαζόμαστε περισσότερο οξυγόνο, όμως τα πειράματα δεν το επιβεβαίωσαν. Μια νεότερη θεωρία λέει ότι το χασμουρητό δροσίζει τον εγκέφαλο: η βαθιά εισπνοή και το τέντωμα του σαγονιού φέρνουν πιο δροσερό αίμα στο κεφάλι.", "We used to believe we yawn because we need more oxygen, but experiments didn't confirm it. A newer theory says yawning cools the brain: the deep breath in and the stretching of the jaw bring cooler blood to the head."),
  L("Παρουσιαστής", "m", "Το πιο περίεργο όμως είναι ότι το χασμουρητό είναι μεταδοτικό. Αρκεί να δούμε, να ακούσουμε ή ακόμα και να διαβάσουμε για κάποιον που χασμουριέται. Οι ερευνητές παρατηρούν ότι αυτό συμβαίνει πιο συχνά ανάμεσα σε ανθρώπους που γνωρίζονται καλά, γι' αυτό κάποιοι το συνδέουν με την ενσυναίσθηση.", "But the strangest thing is that yawning is contagious. It's enough to see, hear or even read about someone yawning. Researchers observe that it happens more often between people who know each other well, which is why some link it to empathy."),
 ],
 "questions": [
  Q("Τι λέει ο παρουσιαστής για τα έμβρυα;", ["Δεν χασμουριούνται ποτέ", "Χασμουριούνται κι αυτά μέσα στη μήτρα", "Χασμουριούνται μόνο τον τελευταίο μήνα", "Δεν έχει μελετηθεί"], 1, "ακόμα και τα έμβρυα μέσα στη μήτρα"),
  Q("Τι λέει η νεότερη θεωρία;", ["Ότι χρειαζόμαστε περισσότερο οξυγόνο", "Ότι χασμουριόμαστε από βαρεμάρα", "Ότι το χασμουρητό δροσίζει τον εγκέφαλο", "Ότι ξεκουράζει τα μάτια"], 2, "το χασμουρητό δροσίζει τον εγκέφαλο"),
  Q("Πότε είναι πιο συχνό το μεταδοτικό χασμουρητό;", ["Ανάμεσα σε ανθρώπους που γνωρίζονται καλά", "Ανάμεσα σε αγνώστους", "Το πρωί", "Όταν κάνει ζέστη"], 0, "πιο συχνά ανάμεσα σε ανθρώπους που γνωρίζονται καλά"),
 ],
 "gloss": {"χασμουρηθείτε": "χασμουριέμαι — to yawn", "βαριέστε": "βαριέμαι — to be bored", "χασμουρητό": "χασμουρητό — yawn, yawning", "σπονδυλωτά": "σπονδυλωτά — vertebrates", "έμβρυα": "έμβρυο — foetus, embryo", "μήτρα": "μήτρα — womb", "εισπνοή": "εισπνοή — inhalation", "σαγονιού": "σαγόνι — jaw", "μεταδοτικό": "μεταδοτικός — contagious", "ενσυναίσθηση": "ενσυναίσθηση — empathy"}
})

ITEMS.append({
 "id": "l113-mono-teleftaio-treno", "title": "Η νύχτα που έχασα το τελευταίο τρένο", "title_en": "The night I missed the last train", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να διηγείται μια ιστορία σε ραδιοφωνική εκπομπή με ιστορίες ακροατών.",
 "script": [
  L("Αφηγήτρια", "f", "Ήταν Νοέμβριος και γύριζα από μια συνέντευξη για δουλειά σε μια μικρή πόλη. Η συνέντευξη κράτησε περισσότερο απ' όσο περίμενα, και όταν έφτασα τρέχοντας στον σταθμό, είδα τα φώτα του τελευταίου τρένου να απομακρύνονται. Το επόμενο ήταν στις έξι το πρωί.", "It was November and I was coming back from a job interview in a small town. The interview lasted longer than I expected, and when I reached the station running, I saw the lights of the last train moving away. The next one was at six in the morning."),
  L("Αφηγήτρια", "f", "Ταξί δεν υπήρχε, το κινητό μου είχε σχεδόν αδειάσει και το μοναδικό ξενοδοχείο ήταν κλειστό για τον χειμώνα. Κάθισα στο παγκάκι κι έκλαψα, για να είμαι ειλικρινής. Τότε βγήκε ο σταθμάρχης, ένας ηλικιωμένος κύριος, και μου είπε να μπω μέσα να ζεσταθώ.", "There was no taxi, my phone was almost dead and the only hotel was closed for the winter. I sat on the bench and cried, to be honest. Then the stationmaster came out, an elderly gentleman, and told me to come inside and warm up."),
  L("Αφηγήτρια", "f", "Μου έφτιαξε τσάι, μου δάνεισε τον φορτιστή του και μου έδειξε έναν καναπέ στο γραφείο. Μιλήσαμε μέχρι τις δύο για τα τρένα που περνούσαν από εκεί όταν ήταν νέος. Τη δουλειά τελικά την πήρα, και κάθε φορά που περνάω από εκείνον τον σταθμό, του αφήνω ένα κουτί κουλουράκια.", "He made me tea, lent me his charger and showed me a sofa in the office. We talked until two about the trains that passed through there when he was young. I did get the job in the end, and every time I pass through that station, I leave him a box of biscuits."),
 ],
 "questions": [
  Q("Γιατί έχασε το τελευταίο τρένο;", ["Γιατί μπερδεύτηκε στην ώρα", "Γιατί η συνέντευξη κράτησε περισσότερο απ' όσο περίμενε", "Γιατί δεν βρήκε ταξί", "Γιατί το τρένο έφυγε νωρίτερα"], 1, "Η συνέντευξη κράτησε περισσότερο απ' όσο περίμενα"),
  Q("Γιατί δεν μπορούσε να μείνει σε ξενοδοχείο;", ["Γιατί ήταν πολύ ακριβό", "Γιατί ήταν γεμάτο", "Γιατί ήταν κλειστό για τον χειμώνα", "Γιατί ήταν μακριά από τον σταθμό"], 2, "το μοναδικό ξενοδοχείο ήταν κλειστό για τον χειμώνα"),
  Q("Τι κάνει η αφηγήτρια κάθε φορά που περνά από τον σταθμό;", ["Αφήνει στον σταθμάρχη ένα κουτί κουλουράκια", "Του τηλεφωνεί", "Κατεβαίνει για καφέ", "Του φέρνει ένα βιβλίο"], 0, "του αφήνω ένα κουτί κουλουράκια"),
 ],
 "gloss": {"απομακρύνονται": "απομακρύνομαι — to move away", "αδειάσει": "αδειάζω — to empty; (of a battery) to run down", "παγκάκι": "παγκάκι — bench", "ειλικρινής": "ειλικρινής — honest, sincere", "σταθμάρχης": "σταθμάρχης — stationmaster", "ζεσταθώ": "ζεσταίνομαι — to warm up", "φορτιστή": "φορτιστής — charger", "κουλουράκια": "κουλουράκι — biscuit, butter cookie"}
})

ITEMS.append({
 "id": "l113-c1-psevdaisthisi-sychnotitas", "title": "Γιατί μια καινούργια λέξη εμφανίζεται ξαφνικά παντού", "title_en": "Why a new word suddenly appears everywhere", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ομιλία σε κύκλο διαλέξεων για τη γλώσσα και τον νου.",
 "script": [
  L("Ομιλήτρια", "f", "Σίγουρα σας έχει συμβεί: μαθαίνετε μια λέξη που δεν είχατε ξανακούσει ποτέ, και μέσα σε λίγες μέρες τη συναντάτε στην εφημερίδα, σε μια σειρά, στη συζήτηση δύο αγνώστων στο λεωφορείο. Η πρώτη σκέψη είναι ότι η λέξη έγινε ξαφνικά της μόδας. Η αλήθεια, κατά κανόνα, είναι πολύ πιο πεζή: η λέξη ήταν πάντα εκεί· απλώς τώρα την προσέχετε.", "It has surely happened to you: you learn a word you had never heard before, and within a few days you come across it in the newspaper, in a series, in the conversation of two strangers on the bus. The first thought is that the word has suddenly become fashionable. The truth, as a rule, is much more prosaic: the word was always there; you just notice it now."),
  L("Ομιλήτρια", "f", "Ο Αμερικανός γλωσσολόγος Άρνολντ Ζουίκι ονόμασε το φαινόμενο «ψευδαίσθηση της συχνότητας». Κατά την περιγραφή του, συνδυάζονται δύο μηχανισμοί. Ο πρώτος είναι η επιλεκτική προσοχή: ο εγκέφαλος φιλτράρει συνεχώς τον τεράστιο όγκο πληροφοριών που δεχόμαστε, και ό,τι μόλις αποκτήσαμε λόγο να προσέχουμε περνά πιο εύκολα το φίλτρο. Ο δεύτερος είναι η μεροληψία επιβεβαίωσης: κάθε νέα συνάντηση με τη λέξη την καταγράφουμε ως απόδειξη, ενώ τις μέρες που δεν την ακούμε απλώς δεν τις μετράμε.", "The American linguist Arnold Zwicky named the phenomenon the \"frequency illusion\". In his description, two mechanisms combine. The first is selective attention: the brain constantly filters the enormous volume of information we receive, and whatever we have just acquired a reason to notice gets through the filter more easily. The second is confirmation bias: we record every new encounter with the word as evidence, while the days we don't hear it we simply don't count."),
  L("Ομιλήτρια", "f", "Ο ίδιος ερευνητής περιέγραψε και μια συγγενική πλάνη, την «ψευδαίσθηση της πρόσφατης εμφάνισης»: την πεποίθηση ότι μια έκφραση που μόλις προσέξαμε είναι καινούργια, ενώ συχνά τη χρησιμοποιούν εδώ και αιώνες. Από αυτήν πηγάζουν πολλά από τα παράπονα για τη «διάβρωση» της γλώσσας από τη νέα γενιά.", "The same researcher also described a related fallacy, the \"recency illusion\": the belief that an expression we have just noticed is new, when often it has been in use for centuries. Many of the complaints about the \"erosion\" of the language by the younger generation stem from it."),
  L("Ομιλήτρια", "f", "Για όσους μαθαίνουν ξένες γλώσσες, πάντως, η ψευδαίσθηση αυτή είναι μάλλον ευλογία. Κάθε φορά που μια λέξη «εμφανίζεται» ξανά, έχουμε μια ακόμα ευκαιρία να την ακούσουμε στο φυσικό της περιβάλλον, και η μνήμη μας την εδραιώνει. Με άλλα λόγια, η αυταπάτη δουλεύει υπέρ μας.", "For those learning foreign languages, though, this illusion is rather a blessing. Every time a word \"appears\" again, we get another chance to hear it in its natural setting, and our memory consolidates it. In other words, the self-deception works in our favour."),
 ],
 "questions": [
  Q("Ποια είναι, κατά την ομιλήτρια, η συνήθης εξήγηση όταν μια νέα λέξη εμφανίζεται παντού;", ["Ότι η λέξη έγινε της μόδας", "Ότι η λέξη υπήρχε πάντα αλλά τώρα την προσέχουμε", "Ότι τα μέσα ενημέρωσης την επαναλαμβάνουν σκόπιμα", "Ότι τη θυμόμαστε λανθασμένα"], 1, "η λέξη ήταν πάντα εκεί· απλώς τώρα την προσέχετε"),
  Q("Πώς λειτουργεί η μεροληψία επιβεβαίωσης στο φαινόμενο αυτό;", ["Ξεχνάμε τη λέξη όταν δεν την ακούμε", "Επιλέγουμε να διαβάζουμε κείμενα με τη λέξη", "Μετράμε κάθε συνάντηση με τη λέξη ως απόδειξη, αλλά όχι τις μέρες που δεν την ακούμε", "Ρωτάμε άλλους αν έχουν ακούσει τη λέξη"], 2, "κάθε νέα συνάντηση με τη λέξη την καταγράφουμε ως απόδειξη, ενώ τις μέρες που δεν την ακούμε απλώς δεν τις μετράμε"),
  Q("Τι είναι η «ψευδαίσθηση της πρόσφατης εμφάνισης»;", ["Η πεποίθηση ότι μια έκφραση είναι καινούργια ενώ υπάρχει εδώ και αιώνες", "Η τάση να ξεχνάμε γρήγορα τις νέες λέξεις", "Η αίσθηση ότι ο χρόνος περνά πιο γρήγορα", "Η προτίμηση για παλιές εκφράσεις"], 0, "την πεποίθηση ότι μια έκφραση που μόλις προσέξαμε είναι καινούργια"),
  Q("Γιατί η ομιλήτρια θεωρεί το φαινόμενο ευλογία για όσους μαθαίνουν γλώσσες;", ["Γιατί τους κάνει πιο σίγουρους", "Γιατί κάθε νέα συνάντηση με τη λέξη βοηθά τη μνήμη να την εδραιώσει", "Γιατί μειώνει τα λάθη στην προφορά", "Γιατί τους βοηθά να μαντεύουν τη σημασία"], 1, "η μνήμη μας την εδραιώνει"),
 ],
 "gloss": {"πεζή": "πεζός — prosaic, mundane", "ψευδαίσθηση": "ψευδαίσθηση — illusion", "επιλεκτική": "επιλεκτικός — selective", "φιλτράρει": "φιλτράρω — to filter", "μεροληψία": "μεροληψία επιβεβαίωσης — confirmation bias", "συγγενική": "συγγενικός — related, kindred", "πλάνη": "πλάνη — fallacy, delusion", "πηγάζουν": "πηγάζω — to stem, spring from", "διάβρωση": "διάβρωση — erosion", "ευλογία": "ευλογία — blessing", "εδραιώνει": "εδραιώνω — to consolidate", "αυταπάτη": "αυταπάτη — self-deception"}
})

ITEMS.append({
 "id": "l113-c1-karagkiozis", "title": "Ο Καραγκιόζης και το θέατρο σκιών", "title_en": "Karagiozis and the shadow theatre", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια θεατρολόγο σε πολιτιστική εκπομπή.",
 "script": [
  L("Δημοσιογράφος", "m", "Ο Καραγκιόζης θεωρείται σήμερα κάτι απολύτως ελληνικό. Ισχύει αυτό;", "Karagiozis is considered something entirely Greek today. Is that true?"),
  L("Θεατρολόγος", "f", "Ναι και όχι. Το θέατρο σκιών ήρθε στον ελληνικό χώρο μέσα από την οθωμανική παράδοση, όπου ο κεντρικός ήρωας λεγόταν Καραγκιόζ. Τον δέκατο ένατο αιώνα όμως οι Έλληνες καραγκιοζοπαίχτες τον μεταμόρφωσαν ριζικά. Σημαντικό ρόλο αποδίδεται στον Δημήτριο Σαρδούνη, γνωστό ως Μίμαρο, που στην Πάτρα, προς τα τέλη του αιώνα, απομάκρυνε τα χοντροκομμένα αστεία και πρόσθεσε ήρωες και θέματα από την ελληνική ζωή και ιστορία.", "Yes and no. Shadow theatre came to the Greek lands through the Ottoman tradition, where the central hero was called Karagöz. But in the nineteenth century Greek puppeteers transformed him radically. An important role is attributed to Dimitrios Sardounis, known as Mimaros, who in Patras, towards the end of the century, removed the coarse jokes and added characters and themes from Greek life and history."),
  L("Δημοσιογράφος", "m", "Ποιοι είναι αυτοί οι ήρωες;", "Who are these characters?"),
  L("Θεατρολόγος", "f", "Γύρω από τον φτωχό, πονηρό και πάντα πεινασμένο Καραγκιόζη υπάρχει ένα ολόκληρο κοινωνικό πανόραμα: ο Χατζηαβάτης, ο δουλοπρεπής γείτονας· ο Μπαρμπαγιώργος, ο βουνίσιος θείος· ο Μορφονιός, ο ματαιόδοξος· ο Σταύρακας, ο μάγκας· και φυσικά ο Πασάς και η Βεζυροπούλα. Κάθε φιγούρα είναι και μια καρικατούρα ενός κοινωνικού τύπου, και το κοινό τις αναγνώριζε αμέσως, συχνά από την προφορά τους.", "Around the poor, crafty and ever-hungry Karagiozis there is a whole social panorama: Hatziavatis, the obsequious neighbour; Barba-Giorgos, the mountain uncle; Morfonios, the vain one; Stavrakas, the tough guy; and of course the Pasha and the Vizier's daughter. Each figure is also a caricature of a social type, and the audience recognised them immediately, often by their accent."),
  L("Δημοσιογράφος", "m", "Και τεχνικά; Πώς φτιάχνονταν οι φιγούρες;", "And technically? How were the figures made?"),
  L("Θεατρολόγος", "f", "Οι παλιότερες ήταν από δέρμα ζώων, επεξεργασμένο ώστε να γίνει ημιδιάφανο και να αφήνει το χρώμα να περνά στον μπερντέ, το άσπρο πανί. Αργότερα επικράτησε το χαρτόνι, που ήταν φτηνότερο, και οι σκιές έγιναν μαύρες. Πίσω από τον μπερντέ, ένας μόνο άνθρωπος δίνει φωνή σε όλους τους ήρωες. Όποιος θέλει να δει φιγούρες μεγάλων καραγκιοζοπαιχτών μπορεί να επισκεφθεί το Σπαθάρειο Μουσείο στο Μαρούσι.", "The older ones were of animal hide, treated so that it became translucent and let the colour pass onto the berntes, the white cloth. Later cardboard prevailed, as it was cheaper, and the shadows became black. Behind the screen, a single person gives voice to all the characters. Anyone who wants to see figures by great shadow-puppeteers can visit the Spathario Museum in Marousi."),
 ],
 "questions": [
  Q("Από πού ήρθε στον ελληνικό χώρο το θέατρο σκιών, σύμφωνα με τη θεατρολόγο;", ["Από την αρχαία Αθήνα", "Από την οθωμανική παράδοση", "Από την Ιταλία", "Από την Κίνα απευθείας"], 1, "μέσα από την οθωμανική παράδοση"),
  Q("Ποια συμβολή αποδίδεται στον Μίμαρο;", ["Ίδρυσε το πρώτο μουσείο", "Έφτιαξε τις πρώτες χάρτινες φιγούρες", "Απομάκρυνε τα χοντροκομμένα αστεία και πρόσθεσε ήρωες από την ελληνική ζωή", "Μετέφερε το θέατρο στην Αθήνα"], 2, "απομάκρυνε τα χοντροκομμένα αστεία και πρόσθεσε ήρωες και θέματα από την ελληνική ζωή και ιστορία"),
  Q("Πώς αναγνώριζε συχνά το κοινό τις φιγούρες;", ["Από την προφορά τους", "Από το χρώμα τους", "Από το μέγεθός τους", "Από τη μουσική που τις συνόδευε"], 0, "συχνά από την προφορά τους"),
  Q("Τι άλλαξε όταν επικράτησε το χαρτόνι;", ["Οι φιγούρες έγιναν μεγαλύτερες", "Οι σκιές έγιναν μαύρες", "Χρειάζονταν περισσότεροι παίχτες", "Ο μπερντές έγινε χρωματιστός"], 1, "οι σκιές έγιναν μαύρες"),
 ],
 "gloss": {"θεατρολόγο": "θεατρολόγος — theatre scholar", "καραγκιοζοπαίχτες": "καραγκιοζοπαίχτης — shadow-puppet performer", "μεταμόρφωσαν": "μεταμορφώνω — to transform", "αποδίδεται": "αποδίδομαι — to be attributed", "χοντροκομμένα": "χοντροκομμένος — coarse, crude", "πονηρό": "πονηρός — crafty, cunning", "δουλοπρεπής": "δουλοπρεπής — obsequious, servile", "βουνίσιος": "βουνίσιος — from the mountains", "ματαιόδοξος": "ματαιόδοξος — vain", "καρικατούρα": "καρικατούρα — caricature", "ημιδιάφανο": "ημιδιάφανος — translucent", "μπερντέ": "μπερντές — the white screen of the shadow theatre", "επικράτησε": "επικρατώ — to prevail"}
})

rnd = random.Random(113)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-113.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
