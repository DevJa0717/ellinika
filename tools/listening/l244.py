# Source for library/listening/listening-244.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l244.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l244-news-agalma-vrethike", "title": "Βρέθηκε το χάλκινο άγαλμα που είχε κλαπεί από το πάρκο", "title_en": "The bronze statue stolen from the park has been found", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός τοπικού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνητής", "m", "Βρέθηκε χθες το χάλκινο άγαλμα του μικρού ψαρά, που είχε κλαπεί πριν από δύο εβδομάδες από το δημοτικό πάρκο. Το άγαλμα εντοπίστηκε σε μια μάντρα παλιοσιδερικών έξω από την πόλη, λίγο πριν λιώσει.", "The bronze statue of the little fisherman, which was stolen two weeks ago from the municipal park, was found yesterday. The statue was located in a scrap-metal yard outside the town, shortly before it was melted down."),
  L("Εκφωνητής", "m", "Τον ιδιοκτήτη της μάντρας τον ειδοποίησε ένας υπάλληλός του, που αναγνώρισε το άγαλμα από φωτογραφίες στα μέσα κοινωνικής δικτύωσης. Οι δύο άνδρες που το είχαν πουλήσει ως παλιό μέταλλο, για περίπου διακόσια ευρώ, αναζητούνται από την αστυνομία.", "The owner of the yard was alerted by one of his employees, who recognised the statue from photographs on social media. The two men who had sold it as scrap metal, for about two hundred euros, are being sought by the police."),
  L("Εκφωνητής", "m", "Το άγαλμα έχει υποστεί ζημιές: λείπει το καλάμι που κρατούσε ο ψαράς, και η βάση του έχει κοπεί με τροχό. Ο γλύπτης που το είχε φτιάξει, πριν από σαράντα χρόνια, ζει ακόμη στην πόλη και προσφέρθηκε να το επισκευάσει δωρεάν.", "The statue has been damaged: the fishing rod the fisherman was holding is missing, and its base has been cut with an angle grinder. The sculptor who made it forty years ago still lives in the town and has offered to repair it free of charge."),
  L("Εκφωνητής", "m", "Ο δήμος ανακοίνωσε ότι το άγαλμα θα επιστρέψει στη θέση του την άνοιξη, αυτή τη φορά στερεωμένο σε τσιμεντένια βάση και κοντά σε κάμερα ασφαλείας.", "The municipality announced that the statue will return to its place in the spring, this time fixed to a concrete base and near a security camera."),
 ],
 "questions": [
  Q("Πού βρέθηκε το άγαλμα;", ["Σε ένα σπίτι στο κέντρο", "Σε μια μάντρα παλιοσιδερικών έξω από την πόλη", "Στο λιμάνι", "Σε ένα κατάστημα με αντίκες"], 1, "εντοπίστηκε σε μια μάντρα παλιοσιδερικών έξω από την πόλη"),
  Q("Πώς αναγνωρίστηκε το άγαλμα;", ["Από τον γλύπτη", "Ένας υπάλληλος το αναγνώρισε από φωτογραφίες στα μέσα κοινωνικής δικτύωσης", "Από την κάμερα του πάρκου", "Από έναν περαστικό"], 1, "αναγνώρισε το άγαλμα από φωτογραφίες στα μέσα κοινωνικής δικτύωσης"),
  Q("Ποια ζημιά έχει υποστεί το άγαλμα;", ["Έχει σπάσει το κεφάλι του", "Λείπει το καλάμι και η βάση έχει κοπεί", "Έχει βαφτεί με σπρέι", "Έχει λιώσει το μισό"], 1, "λείπει το καλάμι που κρατούσε ο ψαράς, και η βάση του έχει κοπεί με τροχό"),
  Q("Τι προσφέρθηκε να κάνει ο γλύπτης;", ["Να φτιάξει ένα καινούργιο άγαλμα", "Να επισκευάσει το άγαλμα δωρεάν", "Να το κρατήσει στο εργαστήριό του", "Να το πουλήσει σε μουσείο"], 1, "προσφέρθηκε να το επισκευάσει δωρεάν"),
 ],
 "gloss": {"χάλκινο": "χάλκινος — bronze, copper", "άγαλμα": "άγαλμα — statue", "κλαπεί": "κλέβομαι — to be stolen", "μάντρα": "μάντρα — yard (enclosed)", "παλιοσιδερικών": "παλιοσίδερα — scrap metal", "λιώσει": "λιώνω — to melt", "αναζητούνται": "αναζητούμαι — to be sought", "καλάμι": "καλάμι — fishing rod; reed", "τροχό": "τροχός — angle grinder; wheel", "γλύπτης": "γλύπτης — sculptor", "στερεωμένο": "στερεωμένος — fixed, secured", "τσιμεντένια": "τσιμεντένιος — concrete"},
})

ITEMS.append({
 "id": "l244-vm-synadelfos-autokinito", "title": "Μήνυμα από μια συνάδελφο: «Να πηγαίνουμε μαζί στη δουλειά;»", "title_en": "A message from a colleague: 'Shall we drive to work together?'", "type": "voicemail", "level": "B2",
 "context_el": "Πριν από λίγες μέρες μετακομίσατε σε μια νέα γειτονιά. Ακούτε ένα μήνυμα που σας άφησε μια συνάδελφός σας στον τηλεφωνητή.",
 "script": [
  L("Συνάδελφος", "f", "Γεια σου, η Κατερίνα είμαι, από το λογιστήριο. Έμαθα από τη Ρένα ότι μετακόμισες στο Μαρούσι, δύο δρόμους από το σπίτι μου! Σκέφτηκα λοιπόν να πηγαίνουμε μαζί στη δουλειά με ένα αυτοκίνητο, αντί να παίρνουμε το καθένας το δικό του.", "Hi, it's Katerina, from accounts. I heard from Rena that you've moved to Marousi, two streets from my house! So I thought we could go to work together in one car, instead of each of us taking our own."),
  L("Συνάδελφος", "f", "Η ιδέα μου είναι να οδηγούμε εναλλάξ, μία εβδομάδα εγώ και μία εσύ, και να μοιραζόμαστε τα διόδια όταν παίρνουμε την Αττική Οδό. Εγώ ξεκινάω κατά τις επτά και είκοσι, για να βρίσκω θέση στο πάρκινγκ της εταιρείας.", "My idea is that we drive in turns, one week me and one week you, and share the tolls when we take the Attiki Odos. I set off at about twenty past seven, so that I find a space in the company car park."),
  L("Συνάδελφος", "f", "Μόνο να ξέρεις ότι τις Τετάρτες φεύγω νωρίτερα, στις τέσσερις, γιατί παίρνω την κόρη μου από το κολυμβητήριο. Εκείνες τις μέρες θα πρέπει να γυρίζεις με το μετρό, ή να πάρεις εσύ το αυτοκίνητό σου.", "Just so you know, on Wednesdays I leave earlier, at four, because I pick my daughter up from the swimming pool. On those days you'd have to come back by metro, or take your own car."),
  L("Συνάδελφος", "f", "Αν σου αρέσει η ιδέα, θα μπορούσαμε να το δοκιμάσουμε από τη Δευτέρα. Πες μου μόνο αν σε πειράζει το ραδιόφωνο το πρωί, γιατί εγώ ακούω ειδήσεις σε όλη τη διαδρομή. Τα λέμε αύριο στο γραφείο.", "If you like the idea, we could try it from Monday. Just tell me if you mind the radio in the morning, because I listen to the news the whole way. See you tomorrow at the office."),
 ],
 "questions": [
  Q("Τι προτείνει η Κατερίνα;", ["Να παίρνουν μαζί το μετρό", "Να πηγαίνουν μαζί στη δουλειά με ένα αυτοκίνητο", "Να μετακομίσουν στο ίδιο κτίριο", "Να αγοράσουν μαζί ένα αυτοκίνητο"], 1, "να πηγαίνουμε μαζί στη δουλειά με ένα αυτοκίνητο"),
  Q("Πώς θα μοιράζονται την οδήγηση;", ["Θα οδηγεί πάντα η Κατερίνα", "Θα οδηγούν εναλλάξ, μία εβδομάδα ο καθένας", "Θα οδηγεί ο/η ακροατής/τρια το πρωί και εκείνη το απόγευμα", "Θα αλλάζουν κάθε μέρα"], 1, "να οδηγούμε εναλλάξ, μία εβδομάδα εγώ και μία εσύ"),
  Q("Γιατί ξεκινά η Κατερίνα στις επτά και είκοσι;", ["Για να αποφεύγει την κίνηση", "Για να βρίσκει θέση στο πάρκινγκ της εταιρείας", "Για να πάει την κόρη της στο σχολείο", "Γιατί αρχίζει νωρίς η βάρδια της"], 1, "για να βρίσκω θέση στο πάρκινγκ της εταιρείας"),
  Q("Τι γίνεται τις Τετάρτες;", ["Δεν πηγαίνει στη δουλειά", "Φεύγει στις τέσσερις για να πάρει την κόρη της από το κολυμβητήριο", "Δουλεύει από το σπίτι", "Οδηγεί πάντα ο/η ακροατής/τρια"], 1, "τις Τετάρτες φεύγω νωρίτερα, στις τέσσερις, γιατί παίρνω την κόρη μου από το κολυμβητήριο"),
 ],
 "gloss": {"λογιστήριο": "λογιστήριο — accounts department", "μετακόμισες": "μετακομίζω — to move house", "εναλλάξ": "εναλλάξ — in turns, alternately", "μοιραζόμαστε": "μοιράζομαι — to share", "διόδια": "διόδια — tolls", "πάρκινγκ": "πάρκινγκ — car park", "κολυμβητήριο": "κολυμβητήριο — swimming pool (sports)", "σε πειράζει": "με πειράζει — to mind, bother", "διαδρομή": "διαδρομή — route, journey"},
})

ITEMS.append({
 "id": "l244-c1-mono-paramana", "title": "Ένα κομμάτι σύρμα για ένα χρέος: η ιστορία της παραμάνας", "title_en": "A piece of wire for a debt: the history of the safety pin", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν ιστορικό σε μια ραδιοφωνική εκπομπή για τα αντικείμενα της καθημερινής ζωής.",
 "script": [
  L("Ιστορικός", "m", "Η παραμάνα μοιάζει τόσο απλή, που δύσκολα φανταζόμαστε ότι κάποιος χρειάστηκε να την εφεύρει. Κι όμως, οι πρόγονοί της είναι πολύ παλιοί. Ήδη στην Εποχή του Χαλκού οι άνθρωποι στερέωναν τα ρούχα τους με πόρπες, μεταλλικές καρφίτσες που λύγιζαν σε σχήμα τόξου.", "The safety pin seems so simple that we can hardly imagine anyone needed to invent it. And yet its ancestors are very old. Already in the Bronze Age people fastened their clothes with brooches, metal pins bent into the shape of a bow."),
  L("Ιστορικός", "m", "Η παραμάνα που ξέρουμε σήμερα γεννήθηκε το 1849, στη Νέα Υόρκη. Ένας εφευρέτης, ο Γουόλτερ Χαντ, χρωστούσε δεκαπέντε δολάρια σε έναν φίλο του. Σύμφωνα με τη γνωστή ιστορία, κάθισε και έστριβε ένα κομμάτι σύρμα για λίγες ώρες, ώσπου κατέληξε σε ένα σχέδιο με ελατήριο στη μία άκρη και ένα μικρό κάλυμμα στην άλλη, που έκρυβε τη μύτη.", "The safety pin we know today was born in 1849, in New York. An inventor, Walter Hunt, owed fifteen dollars to a friend. According to the well-known story, he sat twisting a piece of wire for a few hours, until he arrived at a design with a spring at one end and a small cover at the other, which hid the point."),
  L("Ιστορικός", "m", "Πήρε δίπλωμα ευρεσιτεχνίας και το πούλησε αμέσως για τετρακόσια δολάρια. Ξεπλήρωσε το χρέος του, αλλά δεν είδε ποτέ τα κέρδη από ένα αντικείμενο που θα πουλιόταν σε δισεκατομμύρια κομμάτια. Ο Χαντ, παρεμπιπτόντως, είχε σχεδιάσει και μια ραπτομηχανή, αλλά δεν την κατοχύρωσε.", "He took out a patent and sold it immediately for four hundred dollars. He paid off his debt, but never saw the profits from an object that would sell in billions. Hunt, incidentally, had also designed a sewing machine, but did not patent it."),
  L("Ιστορικός", "m", "Και το ελληνικό όνομα; Η λέξη «παραμάνα» σήμαινε αρχικά τη γυναίκα που θήλαζε και μεγάλωνε τα παιδιά άλλων. Η πιο διαδεδομένη εξήγηση είναι ότι η καρφίτσα πήρε το όνομά της επειδή τη χρησιμοποιούσαν οι παραμάνες για τις πάνες των μωρών, αν και αυτό δεν είναι απολύτως βέβαιο.", "And the Greek name? The word 'paramana' originally meant the woman who breastfed and raised other people's children. The most widespread explanation is that the pin took its name because wet nurses used it for babies' nappies, although this is not entirely certain."),
 ],
 "questions": [
  Q("Τι ήταν οι πόρπες της Εποχής του Χαλκού;", ["Κουμπιά από κόκαλο", "Μεταλλικές καρφίτσες σε σχήμα τόξου για τα ρούχα", "Δερμάτινες ζώνες", "Κοσμήματα για τα μαλλιά"], 1, "στερέωναν τα ρούχα τους με πόρπες, μεταλλικές καρφίτσες που λύγιζαν σε σχήμα τόξου"),
  Q("Γιατί, σύμφωνα με την ιστορία, έφτιαξε ο Χαντ την παραμάνα;", ["Για να τη χαρίσει στη γυναίκα του", "Για να ξεπληρώσει ένα χρέος δεκαπέντε δολαρίων", "Για έναν διαγωνισμό", "Για να βοηθήσει τις παραμάνες"], 1, "χρωστούσε δεκαπέντε δολάρια σε έναν φίλο του"),
  Q("Τι έκανε με το δίπλωμα ευρεσιτεχνίας;", ["Το κράτησε μέχρι τον θάνατό του", "Το πούλησε αμέσως για τετρακόσια δολάρια", "Το χάρισε σε έναν φίλο του", "Το έχασε σε μια δίκη"], 1, "Πήρε δίπλωμα ευρεσιτεχνίας και το πούλησε αμέσως για τετρακόσια δολάρια"),
  Q("Πόσο βέβαιη είναι η εξήγηση για το ελληνικό όνομα «παραμάνα»;", ["Είναι απολύτως αποδεδειγμένη", "Είναι η πιο διαδεδομένη, αλλά όχι απολύτως βέβαιη", "Είναι σίγουρα λάθος", "Ο ιστορικός δεν δίνει καμία εξήγηση"], 1, "Η πιο διαδεδομένη εξήγηση … αν και αυτό δεν είναι απολύτως βέβαιο"),
 ],
 "gloss": {"παραμάνα": "παραμάνα — safety pin; wet nurse", "σύρμα": "σύρμα — wire", "χρέος": "χρέος — debt", "στερέωναν": "στερεώνω — to fasten, fix", "πόρπες": "πόρπη — brooch, clasp (ancient fibula)", "τόξου": "τόξο — bow, arc", "ελατήριο": "ελατήριο — spring", "δίπλωμα ευρεσιτεχνίας": "δίπλωμα ευρεσιτεχνίας — patent", "Ξεπλήρωσε": "ξεπληρώνω — to pay off", "κατοχύρωσε": "κατοχυρώνω — to patent, secure legally", "θήλαζε": "θηλάζω — to breastfeed", "πάνες": "πάνα — nappy, diaper"},
})

ITEMS.append({
 "id": "l244-c1-int-palynologos", "title": "Μια παλυνολόγος για τη γύρη, το αρχείο που κρύβεται στις λίμνες", "title_en": "A palynologist on pollen, the archive hidden in lakes", "type": "interview", "level": "C1",
 "context_el": "Μια παλυνολόγος, δηλαδή μια επιστήμονας που μελετά τους κόκκους γύρης, μιλά σε μια ραδιοφωνική εκπομπή για την επιστήμη.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι περισσότεροι ακροατές μας σκέφτονται τη γύρη μόνο την άνοιξη, όταν φτερνίζονται. Τι βλέπετε εσείς σε αυτή;", "Most of our listeners think about pollen only in spring, when they sneeze. What do you see in it?"),
  L("Παλυνολόγος", "f", "Ένα αρχείο. Κάθε φυτό παράγει κόκκους γύρης με το δικό του σχήμα, και στο μικροσκόπιο μπορώ να ξεχωρίσω μια βελανιδιά από ένα πεύκο ή μια ελιά. Το εξωτερικό τοίχωμα του κόκκου είναι από τα πιο ανθεκτικά υλικά της φύσης. Αν πέσει στον πάτο μιας λίμνης, όπου δεν υπάρχει οξυγόνο, μπορεί να διατηρηθεί για χιλιάδες χρόνια.", "An archive. Every plant produces pollen grains with their own shape, and under the microscope I can tell an oak from a pine or an olive. The outer wall of the grain is one of the most resistant materials in nature. If it falls to the bottom of a lake, where there is no oxygen, it can be preserved for thousands of years."),
  L("Δημοσιογράφος", "m", "Και πώς διαβάζετε αυτό το αρχείο;", "And how do you read this archive?"),
  L("Παλυνολόγος", "f", "Βγάζουμε από τον πυθμένα μακριούς σωλήνες με ιζήματα, που περιέχουν χιλιάδες λεπτά στρώματα, και μετράμε τη γύρη σε κάθε στρώμα. Έτσι βλέπουμε πότε τα δάση υποχωρούσαν και πότε επέστρεφαν, πότε άλλαζε το κλίμα, ακόμη και πότε οι άνθρωποι άρχισαν να καλλιεργούν. Όταν ξαφνικά πληθαίνει η γύρη της ελιάς και των σιτηρών, ξέρουμε ότι κάπου κοντά εμφανίστηκαν αγρότες.", "We extract long tubes of sediment from the bottom, containing thousands of thin layers, and count the pollen in each layer. That way we see when the forests retreated and when they returned, when the climate changed, even when people began to farm. When the pollen of olives and cereals suddenly increases, we know that farmers appeared somewhere nearby."),
  L("Δημοσιογράφος", "m", "Χρησιμεύει η δουλειά σας και στο παρόν;", "Is your work useful in the present too?"),
  L("Παλυνολόγος", "f", "Βεβαίως. Σε κάποιες πόλεις υπάρχουν παγίδες γύρης στις ταράτσες, και οι μετρήσεις τους βοηθούν τους αλλεργικούς να ξέρουν πότε να προσέχουν. Η γύρη χρησιμοποιείται καμιά φορά και στην εγκληματολογία: η λάσπη σε ένα παπούτσι μπορεί να δείξει από ποια περιοχή πέρασε κάποιος.", "Of course. In some cities there are pollen traps on the roofs, and their measurements help people with allergies know when to be careful. Pollen is sometimes used in forensics too: the mud on a shoe can show which area someone passed through."),
 ],
 "questions": [
  Q("Γιατί μπορεί η παλυνολόγος να ξεχωρίσει τα φυτά από τη γύρη τους;", ["Γιατί η γύρη έχει διαφορετική μυρωδιά", "Γιατί κάθε φυτό παράγει κόκκους με το δικό του σχήμα", "Γιατί η γύρη έχει διαφορετικό χρώμα", "Γιατί κάθε φυτό ανθίζει άλλη εποχή"], 1, "Κάθε φυτό παράγει κόκκους γύρης με το δικό του σχήμα"),
  Q("Γιατί διατηρείται η γύρη στον πάτο των λιμνών;", ["Γιατί το νερό είναι κρύο", "Γιατί εκεί δεν υπάρχει οξυγόνο και το τοίχωμά της είναι πολύ ανθεκτικό", "Γιατί την τρώνε τα ψάρια", "Γιατί σκεπάζεται με αλάτι"], 1, "Αν πέσει στον πάτο μιας λίμνης, όπου δεν υπάρχει οξυγόνο, μπορεί να διατηρηθεί"),
  Q("Τι δείχνει μια ξαφνική αύξηση της γύρης της ελιάς και των σιτηρών;", ["Ότι το κλίμα έγινε πιο κρύο", "Ότι κάπου κοντά εμφανίστηκαν αγρότες", "Ότι κάηκε ένα δάσος", "Ότι η λίμνη στέρεψε"], 1, "ξέρουμε ότι κάπου κοντά εμφανίστηκαν αγρότες"),
  Q("Πώς χρησιμοποιείται η γύρη στην εγκληματολογία;", ["Για να βρεθούν δακτυλικά αποτυπώματα", "Η λάσπη σε ένα παπούτσι μπορεί να δείξει από πού πέρασε κάποιος", "Για να χρονολογηθούν τα όπλα", "Για να αναγνωριστεί η φωνή ενός υπόπτου"], 1, "η λάσπη σε ένα παπούτσι μπορεί να δείξει από ποια περιοχή πέρασε κάποιος"),
 ],
 "gloss": {"παλυνολόγος": "παλυνολόγος — palynologist (pollen scientist)", "γύρη": "γύρη — pollen", "κόκκους": "κόκκος — grain", "φτερνίζονται": "φτερνίζομαι — to sneeze", "βελανιδιά": "βελανιδιά — oak", "τοίχωμα": "τοίχωμα — wall (of a cell, vessel)", "ανθεκτικά": "ανθεκτικός — resistant, durable", "πυθμένα": "πυθμένας — bottom (of sea, lake)", "ιζήματα": "ίζημα — sediment", "υποχωρούσαν": "υποχωρώ — to retreat", "πληθαίνει": "πληθαίνω — to increase in number", "σιτηρών": "σιτηρά — cereals, grain", "παγίδες": "παγίδα — trap", "εγκληματολογία": "εγκληματολογία — criminology, forensics", "λάσπη": "λάσπη — mud"},
})
rnd = random.Random(244)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-244.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
