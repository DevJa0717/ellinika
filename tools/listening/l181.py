# Source for library/listening/listening-181.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l181.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l181-ann-xenagisi-zythopoieio", "title": "Πριν από την ξενάγηση στο ζυθοποιείο", "title_en": "Before the brewery tour", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα μικρό ζυθοποιείο και ακούτε μια ανακοίνωση λίγο πριν αρχίσει η ξενάγηση.",
 "script": [
  L("Ξεναγός", "f", "Καλησπέρα σας και καλώς ήρθατε! Η ξενάγηση θα διαρκέσει περίπου σαράντα πέντε λεπτά. Θα δούμε πρώτα την αποθήκη με τα σιτηρά και τον λυκίσκο, μετά τις δεξαμενές όπου βράζει και ζυμώνεται η μπίρα, και στο τέλος τη γραμμή εμφιάλωσης.", "Good evening and welcome! The tour will last about forty-five minutes. We'll first see the storeroom with the grain and the hops, then the tanks where the beer is boiled and fermented, and finally the bottling line."),
  L("Ξεναγός", "f", "Για λόγους ασφαλείας, παρακαλούμε να μένετε πίσω από την κίτρινη γραμμή στο πάτωμα, γιατί οι σωλήνες κοντά στις δεξαμενές είναι πολύ ζεστοί. Στον χώρο της εμφιάλωσης δεν επιτρέπονται οι φωτογραφίες με φλας, επειδή ενοχλούν τους αισθητήρες των μηχανημάτων.", "For safety reasons, please stay behind the yellow line on the floor, because the pipes near the tanks are very hot. In the bottling area flash photography is not allowed, because it disturbs the machines' sensors."),
  L("Ξεναγός", "f", "Η ξενάγηση τελειώνει με γευσιγνωσία τριών μπιρών, μόνο για ενήλικες, γι' αυτό ίσως σας ζητήσουμε την ταυτότητά σας. Όσοι οδηγούν μπορούν να δοκιμάσουν την μπίρα μας χωρίς αλκοόλ, δωρεάν. Με το εισιτήριό σας έχετε επίσης δέκα τοις εκατό έκπτωση στο κατάστημα στην έξοδο.", "The tour ends with a tasting of three beers, for adults only, so we may ask for your ID. Those who are driving can try our alcohol-free beer, free of charge. With your ticket you also get ten per cent off in the shop at the exit."),
 ],
 "questions": [
  Q("Γιατί πρέπει οι επισκέπτες να μένουν πίσω από την κίτρινη γραμμή;", ["Γιατί το πάτωμα γλιστράει", "Γιατί οι σωλήνες κοντά στις δεξαμενές είναι πολύ ζεστοί", "Γιατί εκεί δουλεύουν οι εργάτες", "Γιατί απαγορεύεται να αγγίζουν τα σιτηρά"], 1, "οι σωλήνες κοντά στις δεξαμενές είναι πολύ ζεστοί"),
  Q("Γιατί δεν επιτρέπεται το φλας στον χώρο της εμφιάλωσης;", ["Γιατί χαλάει τη γεύση της μπίρας", "Γιατί υπάρχουν πνευματικά δικαιώματα", "Γιατί ενοχλεί τους αισθητήρες των μηχανημάτων", "Γιατί ενοχλεί τους άλλους επισκέπτες"], 2, "επειδή ενοχλούν τους αισθητήρες των μηχανημάτων"),
  Q("Τι προσφέρεται σε όσους οδηγούν;", ["Μπίρα χωρίς αλκοόλ, δωρεάν", "Ένα δώρο από το κατάστημα", "Μεγαλύτερη έκπτωση", "Ένας καφές"], 0, "Όσοι οδηγούν μπορούν να δοκιμάσουν την μπίρα μας χωρίς αλκοόλ, δωρεάν"),
 ],
 "gloss": {"ζυθοποιείο": "ζυθοποιείο — brewery", "σιτηρά": "σιτηρά — grain, cereals", "λυκίσκο": "λυκίσκος — hops", "δεξαμενές": "δεξαμενή — tank", "ζυμώνεται": "ζυμώνομαι — to ferment", "εμφιάλωσης": "εμφιάλωση — bottling", "σωλήνες": "σωλήνας — pipe", "αισθητήρες": "αισθητήρας — sensor", "γευσιγνωσία": "γευσιγνωσία — tasting"},
})

ITEMS.append({
 "id": "l181-int-psaradissa", "title": "Μια ψαράδισσα στη Λέρο", "title_en": "A fisherwoman on Leros", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γυναίκα που ψαρεύει επαγγελματικά με το δικό της καΐκι.",
 "script": [
  L("Δημοσιογράφος", "m", "Δεν είναι συνηθισμένο να βλέπει κανείς γυναίκα στο τιμόνι ενός ψαροκάικου. Πώς ξεκινήσατε;", "It's not common to see a woman at the helm of a fishing boat. How did you start?"),
  L("Ψαράδισσα", "f", "Όταν ήμουν είκοσι πέντε, ο πατέρας μου αρρώστησε και δεν μπορούσε πια να βγαίνει στη θάλασσα. Το καΐκι θα το πουλούσαμε. Είπα «δώστε μου έναν χρόνο». Αυτός ο χρόνος κράτησε δεκαοχτώ χρόνια. Στην αρχή οι άλλοι ψαράδες γελούσαν· σήμερα με ρωτούν πού έριξα τα δίχτυα.", "When I was twenty-five, my father fell ill and could no longer go out to sea. We were going to sell the boat. I said 'give me a year'. That year lasted eighteen years. At first the other fishermen laughed; today they ask me where I cast my nets."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το μεγαλύτερο πρόβλημα σήμερα;", "What is the biggest problem today?"),
  L("Ψαράδισσα", "f", "Τα ψάρια είναι πολύ λιγότερα απ' ό,τι όταν ξεκίνησα. Και κάθε μέρα βγάζω με τα δίχτυα πλαστικά, σακούλες, μπουκάλια. Τα φέρνω όλα στο λιμάνι, σε έναν ειδικό κάδο, γιατί αν τα ξαναρίξω στη θάλασσα, αύριο θα τα ξαναβρώ.", "There are far fewer fish than when I started. And every day I pull up plastics with the nets, bags, bottles. I bring them all to the harbour, to a special bin, because if I throw them back into the sea, I'll find them again tomorrow."),
  L("Δημοσιογράφος", "m", "Πού πουλάτε τα ψάρια σας;", "Where do you sell your fish?"),
  L("Ψαράδισσα", "f", "Κατευθείαν σε τρεις ταβέρνες του νησιού, χωρίς μεσάζοντες. Μου τηλεφωνούν το πρωί και τους λέω τι έπιασα. Έτσι κερδίζω λίγο περισσότερα, κι εκείνοι ξέρουν ότι το ψάρι είναι της ημέρας.", "Directly to three tavernas on the island, without middlemen. They phone me in the morning and I tell them what I've caught. That way I earn a little more, and they know the fish is the catch of the day."),
 ],
 "questions": [
  Q("Γιατί άρχισε να ψαρεύει;", ["Ήθελε να γίνει ανεξάρτητη από μικρή", "Ο πατέρας της αρρώστησε και θα πουλούσαν το καΐκι", "Έχασε τη δουλειά της στην πόλη", "Το καΐκι το κέρδισε σε λαχείο"], 1, "ο πατέρας μου αρρώστησε και δεν μπορούσε πια να βγαίνει στη θάλασσα. Το καΐκι θα το πουλούσαμε"),
  Q("Τι κάνει με τα πλαστικά που βγάζει με τα δίχτυα;", ["Τα ξαναρίχνει στη θάλασσα", "Τα πουλάει για ανακύκλωση", "Τα φέρνει σε έναν ειδικό κάδο στο λιμάνι", "Τα αφήνει στην παραλία"], 2, "Τα φέρνω όλα στο λιμάνι, σε έναν ειδικό κάδο"),
  Q("Πώς πουλάει τα ψάρια της;", ["Κατευθείαν σε ταβέρνες, χωρίς μεσάζοντες", "Στην ψαραγορά του Πειραιά", "Σε ένα σούπερ μάρκετ", "Σε τουρίστες στο λιμάνι"], 0, "Κατευθείαν σε τρεις ταβέρνες του νησιού, χωρίς μεσάζοντες"),
 ],
 "gloss": {"τιμόνι": "τιμόνι — helm, wheel", "ψαροκάικου": "ψαροκάικο — fishing boat", "αρρώστησε": "αρρωσταίνω — to fall ill", "δίχτυα": "δίχτυ — net", "κάδο": "κάδος — bin", "μεσάζοντες": "μεσάζων — middleman", "της ημέρας": "της ημέρας — fresh, of the day"},
})

ITEMS.append({
 "id": "l181-int-kampanopoios", "title": "Ο τεχνίτης που φτιάχνει καμπάνες", "title_en": "The craftsman who makes bells", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν τεχνίτη που κατασκευάζει καμπάνες για εκκλησίες.",
 "script": [
  L("Δημοσιογράφος", "f", "Είστε η τρίτη γενιά της οικογένειάς σας που φτιάχνει καμπάνες. Από τι υλικό γίνεται μια καμπάνα;", "You are the third generation of your family to make bells. What material is a bell made of?"),
  L("Τεχνίτης", "m", "Από μπρούντζο, δηλαδή ένα κράμα χαλκού και κασσίτερου, περίπου τέσσερα μέρη χαλκό σε ένα μέρος κασσίτερο. Αν βάλεις περισσότερο κασσίτερο, ο ήχος γίνεται πιο καθαρός, αλλά η καμπάνα σπάει πιο εύκολα. Όλη η τέχνη είναι στην ισορροπία.", "From bronze, that is an alloy of copper and tin, roughly four parts copper to one part tin. If you add more tin, the sound becomes clearer, but the bell breaks more easily. The whole art is in the balance."),
  L("Δημοσιογράφος", "f", "Πώς πετυχαίνετε τη σωστή νότα;", "How do you get the right note?"),
  L("Τεχνίτης", "m", "Το καλούπι το φτιάχνουμε από πηλό, με το σχήμα που θα δώσει περίπου τη νότα που θέλουμε. Μετά το χύσιμο, κουρδίζουμε την καμπάνα σε έναν τόρνο: αφαιρούμε λίγο λίγο μέταλλο από το εσωτερικό της, και ακούμε. Αν αφαιρέσεις πολύ, δεν γυρίζεις πίσω.", "We make the mould from clay, with the shape that will give roughly the note we want. After the casting, we tune the bell on a lathe: we remove metal little by little from its inside, and we listen. If you take off too much, there's no going back."),
  L("Δημοσιογράφος", "f", "Ποιο είναι το πιο δύσκολο κομμάτι της δουλειάς;", "What is the hardest part of the job?"),
  L("Τεχνίτης", "m", "Η αναμονή. Μια μεγάλη καμπάνα πρέπει να κρυώσει μέσα στο καλούπι για αρκετές μέρες. Αν βιαστείς να τη βγάλεις, μπορεί να ραγίσει. Ο παππούς μου έλεγε ότι η καμπάνα θέλει υπομονή πριν μιλήσει.", "The waiting. A large bell has to cool inside the mould for several days. If you hurry to take it out, it may crack. My grandfather used to say that a bell needs patience before it speaks."),
 ],
 "questions": [
  Q("Τι συμβαίνει, κατά τον τεχνίτη, αν βάλεις περισσότερο κασσίτερο;", ["Η καμπάνα γίνεται πιο ελαφριά", "Ο ήχος γίνεται πιο καθαρός, αλλά η καμπάνα σπάει πιο εύκολα", "Η καμπάνα αλλάζει χρώμα", "Ο ήχος γίνεται πιο χαμηλός"], 1, "Αν βάλεις περισσότερο κασσίτερο, ο ήχος γίνεται πιο καθαρός, αλλά η καμπάνα σπάει πιο εύκολα"),
  Q("Πώς κουρδίζεται η καμπάνα;", ["Προσθέτουν μέταλλο στο εξωτερικό της", "Αλλάζουν το σχοινί της", "Αφαιρούν λίγο λίγο μέταλλο από το εσωτερικό της σε έναν τόρνο", "Τη ζεσταίνουν ξανά"], 2, "αφαιρούμε λίγο λίγο μέταλλο από το εσωτερικό της, και ακούμε"),
  Q("Γιατί η αναμονή είναι το πιο δύσκολο κομμάτι;", ["Γιατί αν βγάλεις την καμπάνα νωρίς, μπορεί να ραγίσει", "Γιατί οι πελάτες βιάζονται", "Γιατί ο πηλός αργεί να βρεθεί", "Γιατί ο τόρνος είναι πολύ αργός"], 0, "Αν βιαστείς να τη βγάλεις, μπορεί να ραγίσει"),
 ],
 "gloss": {"καμπάνες": "καμπάνα — bell", "μπρούντζο": "μπρούντζος — bronze", "κράμα": "κράμα — alloy", "χαλκού": "χαλκός — copper", "κασσίτερου": "κασσίτερος — tin", "καλούπι": "καλούπι — mould", "πηλό": "πηλός — clay", "χύσιμο": "χύσιμο — casting", "τόρνο": "τόρνος — lathe", "ραγίσει": "ραγίζω — to crack"},
})

ITEMS.append({
 "id": "l181-vm-apokriatiki-stoli", "title": "Μήνυμα για την αποκριάτικη στολή", "title_en": "A message about the carnival costume", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από ένα κατάστημα που νοικιάζει αποκριάτικες στολές.",
 "script": [
  L("Υπάλληλος", "m", "Καλησπέρα σας, από το κατάστημα «Μασκαράδα» σας παίρνω, για τη στολή του πειρατή που κλείσατε για τον γιο σας, νούμερο οχτώ. Δυστυχώς, όταν μας την επέστρεψε ο προηγούμενος πελάτης, έλειπε το καπέλο, και δεν θα έχουμε καινούργιο πριν από το Σάββατο.", "Good evening, I'm calling from the 'Maskarada' shop about the pirate costume you reserved for your son, size eight. Unfortunately, when the previous customer returned it, the hat was missing, and we won't have a new one before Saturday."),
  L("Υπάλληλος", "m", "Σας προτείνω δύο λύσεις: ή να πάρετε τη στολή χωρίς καπέλο με έκπτωση πέντε ευρώ, ή να την αλλάξετε με τη στολή του σωματοφύλακα, στο ίδιο νούμερο και στην ίδια τιμή, η οποία είναι πλήρης, με καπέλο και σπαθί από αφρώδες υλικό.", "I suggest two solutions: either you take the costume without the hat at five euros off, or you swap it for the musketeer costume, in the same size and at the same price, which is complete, with a hat and a sword made of foam."),
  L("Υπάλληλος", "m", "Θυμίζω ότι η εγγύηση είναι είκοσι ευρώ και επιστρέφεται όταν φέρετε πίσω τη στολή, το αργότερο την Τετάρτη μετά την Καθαρά Δευτέρα. Πείτε μου τι προτιμάτε ως αύριο το μεσημέρι, γιατί αυτές τις μέρες οι στολές φεύγουν πολύ γρήγορα. Ευχαριστώ!", "A reminder that the deposit is twenty euros and is returned when you bring the costume back, by the Wednesday after Clean Monday at the latest. Tell me what you prefer by tomorrow noon, because these days the costumes go very fast. Thank you!"),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με τη στολή του πειρατή;", ["Είναι σε λάθος νούμερο", "Λείπει το καπέλο", "Είναι σκισμένη", "Την πήρε άλλος πελάτης"], 1, "έλειπε το καπέλο, και δεν θα έχουμε καινούργιο πριν από το Σάββατο"),
  Q("Τι ισχύει για τη στολή του σωματοφύλακα;", ["Κοστίζει περισσότερο", "Υπάρχει μόνο σε μεγαλύτερο νούμερο", "Είναι πλήρης, στο ίδιο νούμερο και στην ίδια τιμή", "Δεν έχει σπαθί"], 2, "στο ίδιο νούμερο και στην ίδια τιμή, η οποία είναι πλήρης, με καπέλο και σπαθί"),
  Q("Πότε επιστρέφεται η εγγύηση;", ["Όταν επιστραφεί η στολή, ως την Τετάρτη μετά την Καθαρά Δευτέρα", "Το Σάββατο", "Δεν επιστρέφεται", "Αμέσως, μόλις πάρετε τη στολή"], 0, "η εγγύηση είναι είκοσι ευρώ και επιστρέφεται όταν φέρετε πίσω τη στολή, το αργότερο την Τετάρτη μετά την Καθαρά Δευτέρα"),
 ],
 "gloss": {"αποκριάτικες στολές": "αποκριάτικη στολή — carnival costume", "πειρατή": "πειρατής — pirate", "κλείσατε": "κλείνω — to book, reserve", "νούμερο": "νούμερο — size", "σωματοφύλακα": "σωματοφύλακας — musketeer", "αφρώδες υλικό": "αφρώδες υλικό — foam", "εγγύηση": "εγγύηση — deposit", "Καθαρά Δευτέρα": "Καθαρά Δευτέρα — Clean Monday (start of Lent)"},
})

ITEMS.append({
 "id": "l181-mon-roloi-cheiros", "title": "Γιατί φοράω ακόμα ρολόι", "title_en": "Why I still wear a watch", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να εξηγεί σε ένα podcast γιατί φοράει ακόμα ένα παλιό μηχανικό ρολόι χειρός.",
 "script": [
  L("Στέλιος", "m", "Οι φίλοι μου γελάνε: «Τι το θες το ρολόι, αφού έχεις κινητό;» Το ρολόι μου ήταν του παππού μου. Είναι μηχανικό, δεν έχει μπαταρία, και κάθε πρωί πρέπει να το κουρδίσω, γυρίζοντας για λίγα δευτερόλεπτα την κορόνα. Για μένα αυτό έγινε μια μικρή τελετουργία, σαν τον πρώτο καφέ.", "My friends laugh: 'What do you need a watch for, since you have a phone?' My watch was my grandfather's. It's mechanical, it has no battery, and every morning I have to wind it, turning the crown for a few seconds. For me that has become a little ritual, like the first coffee."),
  L("Στέλιος", "m", "Παρατήρησα όμως και κάτι άλλο. Όταν κοιτούσα την ώρα στο κινητό, έβλεπα και τις ειδοποιήσεις, και πριν το καταλάβω είχαν περάσει δέκα λεπτά. Τώρα κοιτάζω τον καρπό μου, βλέπω την ώρα, και τίποτα άλλο. Υπολόγισα ότι πιάνω το κινητό μου σχεδόν τις μισές φορές απ' ό,τι πριν.", "But I noticed something else too. When I checked the time on my phone, I also saw the notifications, and before I knew it ten minutes had passed. Now I look at my wrist, I see the time, and nothing else. I worked out that I pick up my phone almost half as often as before."),
  L("Στέλιος", "m", "Το ρολόι δεν είναι ακριβές· χάνει περίπου ένα λεπτό την εβδομάδα, και κάθε Κυριακή το διορθώνω. Δεν με πειράζει. Μου θυμίζει ότι ο χρόνος δεν χρειάζεται να μετριέται πάντα στο δευτερόλεπτο. Κι όταν το κοιτάζω, θυμάμαι τον παππού μου να μου λέει: «Μη βιάζεσαι, δεν θα σου φύγει η ζωή».", "The watch isn't accurate; it loses about a minute a week, and every Sunday I correct it. I don't mind. It reminds me that time doesn't always need to be measured to the second. And when I look at it, I remember my grandfather telling me: 'Don't rush, life won't run away from you.'"),
 ],
 "questions": [
  Q("Τι πρέπει να κάνει ο Στέλιος κάθε πρωί;", ["Να αλλάξει την μπαταρία του ρολογιού", "Να κουρδίσει το ρολόι γυρίζοντας την κορόνα", "Να ρυθμίσει την ώρα με το κινητό", "Να καθαρίσει το ρολόι"], 1, "κάθε πρωί πρέπει να το κουρδίσω, γυρίζοντας για λίγα δευτερόλεπτα την κορόνα"),
  Q("Τι άλλαξε από τότε που κοιτάζει την ώρα στο ρολόι;", ["Αργεί λιγότερο στα ραντεβού του", "Κοιμάται καλύτερα", "Πιάνει το κινητό του σχεδόν τις μισές φορές απ' ό,τι πριν", "Δεν χρησιμοποιεί πια κινητό"], 2, "πιάνω το κινητό μου σχεδόν τις μισές φορές απ' ό,τι πριν"),
  Q("Πώς αντιμετωπίζει το ότι το ρολόι χάνει ένα λεπτό την εβδομάδα;", ["Δεν τον πειράζει, το διορθώνει κάθε Κυριακή", "Θέλει να το πάει στον ωρολογοποιό", "Σκέφτεται να αγοράσει καινούργιο", "Το φοράει μόνο τις Κυριακές"], 0, "κάθε Κυριακή το διορθώνω. Δεν με πειράζει"),
 ],
 "gloss": {"μηχανικό": "μηχανικός — mechanical", "ρολόι χειρός": "ρολόι χειρός — wristwatch", "κουρδίσω": "κουρδίζω — to wind (up)", "κορόνα": "κορόνα — crown (of a watch)", "τελετουργία": "τελετουργία — ritual", "ειδοποιήσεις": "ειδοποίηση — notification", "καρπό": "καρπός — wrist", "ακριβές": "ακριβής — accurate", "δεν θα σου φύγει η ζωή": "δεν θα σου φύγει η ζωή — life won't run away from you"},
})

ITEMS.append({
 "id": "l181-dia-aftokinito-tou-pappou", "title": "Το αυτοκίνητο του παππού", "title_en": "Grandad's car", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο αδέλφια να συζητούν τι θα κάνουν με το παλιό αυτοκίνητο του παππού τους.",
 "script": [
  L("Ελπίδα", "f", "Μάρκο, ο θείος λέει ότι πρέπει να αδειάσουμε το γκαράζ ως τον Μάρτιο. Τι θα κάνουμε με το αυτοκίνητο του παππού; Είναι εκεί μέσα από το 1978 και δεν έχει πάρει μπρος εδώ και δέκα χρόνια.", "Markos, our uncle says we have to empty the garage by March. What are we going to do with grandad's car? It's been in there since 1978 and it hasn't started for ten years."),
  L("Μάρκος", "m", "Ένας συλλέκτης από τη Θεσσαλονίκη προσφέρθηκε να το αγοράσει, όπως είναι. Τα λεφτά δεν είναι πολλά, αλλά τουλάχιστον θα το φροντίσει κάποιος που ξέρει.", "A collector from Thessaloniki has offered to buy it, as it is. The money isn't much, but at least someone who knows will look after it."),
  L("Ελπίδα", "f", "Δεν μπορώ να το φανταστώ σε ξένα χέρια. Σε αυτό το αυτοκίνητο μας πήγαινε για μπάνιο κάθε καλοκαίρι. Γιατί να μην το επισκευάσουμε εμείς;", "I can't imagine it in someone else's hands. He used to take us swimming in that car every summer. Why don't we repair it ourselves?"),
  L("Μάρκος", "m", "Γιατί η επισκευή μπορεί να κοστίσει όσο ένα καινούργιο αυτοκίνητο. Ας κάνουμε το εξής: να το δει πρώτα ο μηχανικός της γειτονιάς και να μας δώσει μια εκτίμηση. Αν είναι λογικό ποσό, το φτιάχνουμε· αλλιώς, το δίνουμε στον συλλέκτη και του ζητάμε να μας το δείχνει πού και πού.", "Because the repair could cost as much as a new car. Let's do this: first let the neighbourhood mechanic look at it and give us an estimate. If it's a reasonable amount, we fix it; otherwise, we give it to the collector and ask him to show it to us now and then."),
  L("Ελπίδα", "f", "Εντάξει, αλλά αν το φτιάξουμε, με αυτό θα πάω στην εκκλησία την ημέρα του γάμου μου.", "All right, but if we fix it, I'm going to the church in it on my wedding day."),
 ],
 "questions": [
  Q("Γιατί πρέπει να αποφασίσουν τώρα;", ["Γιατί το αυτοκίνητο χάλασε πρόσφατα", "Γιατί πρέπει να αδειάσει το γκαράζ ως τον Μάρτιο", "Γιατί ο συλλέκτης φεύγει στο εξωτερικό", "Γιατί η Ελπίδα παντρεύεται τον Μάρτιο"], 1, "πρέπει να αδειάσουμε το γκαράζ ως τον Μάρτιο"),
  Q("Γιατί η Ελπίδα δεν θέλει να πουλήσουν το αυτοκίνητο;", ["Γιατί θέλει να το οδηγεί κάθε μέρα", "Γιατί ο συλλέκτης δίνει λίγα χρήματα", "Γιατί της θυμίζει τα καλοκαίρια με τον παππού", "Γιατί είναι πολύ σπάνιο"], 2, "Σε αυτό το αυτοκίνητο μας πήγαινε για μπάνιο κάθε καλοκαίρι"),
  Q("Τι προτείνει ο Μάρκος;", ["Να ζητήσουν πρώτα εκτίμηση από τον μηχανικό", "Να το πουλήσουν αμέσως", "Να το αφήσουν στο γκαράζ", "Να το επισκευάσουν μόνοι τους"], 0, "να το δει πρώτα ο μηχανικός της γειτονιάς και να μας δώσει μια εκτίμηση"),
 ],
 "gloss": {"γκαράζ": "γκαράζ — garage", "δεν έχει πάρει μπρος": "παίρνω μπρος — (of an engine) to start", "συλλέκτης": "συλλέκτης — collector", "όπως είναι": "όπως είναι — as it is", "σε ξένα χέρια": "σε ξένα χέρια — in someone else's hands", "επισκευή": "επισκευή — repair", "εκτίμηση": "εκτίμηση — estimate", "πού και πού": "πού και πού — now and then"},
})

ITEMS.append({
 "id": "l181-news-iliaka-pagkakia", "title": "Παγκάκια που φορτίζουν κινητά", "title_en": "Benches that charge phones", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση από ένα τοπικό δελτίο ειδήσεων.",
 "script": [
  L("Παρουσιάστρια", "f", "Είκοσι «έξυπνα» παγκάκια τοποθετήθηκαν αυτή την εβδομάδα σε πλατείες και πάρκα της πόλης. Έχουν ενσωματωμένο ηλιακό πάνελ και επιτρέπουν στους περαστικούς να φορτίζουν δωρεάν το κινητό τους, ενώ το βράδυ φωτίζονται με χαμηλό φως.", "Twenty 'smart' benches were installed this week in squares and parks around the town. They have a built-in solar panel and let passers-by charge their phones for free, while at night they light up with a low light."),
  L("Παρουσιάστρια", "f", "Τα παγκάκια διαθέτουν επίσης αισθητήρες που μετρούν τη θερμοκρασία και την ποιότητα του αέρα. Τα στοιχεία θα δημοσιεύονται σε μια ιστοσελίδα του δήμου, ώστε οι κάτοικοι να ξέρουν, για παράδειγμα, πότε η ατμοσφαιρική ρύπανση ξεπερνά τα όρια.", "The benches also have sensors that measure temperature and air quality. The data will be published on a municipal website, so that residents know, for example, when air pollution exceeds the limits."),
  L("Παρουσιάστρια", "f", "Δεν έλειψαν όμως και οι αντιδράσεις. Ένας σύλλογος κατοίκων υποστηρίζει ότι τα χρήματα θα έπρεπε να είχαν δοθεί για δέντρα, αφού πολλά από τα νέα παγκάκια βρίσκονται σε σημεία χωρίς καμία σκιά. Ο δήμαρχος απάντησε ότι μέσα στον χειμώνα θα φυτευτούν πάνω από εκατό δέντρα στα ίδια σημεία.", "There were, however, some objections. A residents' association argues that the money should have gone on trees, since many of the new benches are in spots with no shade at all. The mayor replied that over the winter more than a hundred trees will be planted in the same spots."),
 ],
 "questions": [
  Q("Τι μπορούν να κάνουν οι περαστικοί στα νέα παγκάκια;", ["Να πληρώνουν τη στάθμευση", "Να φορτίζουν δωρεάν το κινητό τους", "Να αγοράζουν εισιτήρια λεωφορείου", "Να δανείζονται βιβλία"], 1, "επιτρέπουν στους περαστικούς να φορτίζουν δωρεάν το κινητό τους"),
  Q("Γιατί θα δημοσιεύονται τα στοιχεία των αισθητήρων;", ["Για να ελέγχεται η κατανάλωση ρεύματος", "Για να μετρηθεί πόσοι κάθονται στα παγκάκια", "Για να ξέρουν οι κάτοικοι πότε η ρύπανση ξεπερνά τα όρια", "Για να βελτιωθεί το διαδίκτυο"], 2, "ώστε οι κάτοικοι να ξέρουν, για παράδειγμα, πότε η ατμοσφαιρική ρύπανση ξεπερνά τα όρια"),
  Q("Τι υποστηρίζει ο σύλλογος κατοίκων;", ["Ότι τα χρήματα θα έπρεπε να είχαν δοθεί για δέντρα", "Ότι τα παγκάκια είναι άβολα", "Ότι το φως τη νύχτα ενοχλεί", "Ότι χρειάζονται περισσότερα παγκάκια"], 0, "τα χρήματα θα έπρεπε να είχαν δοθεί για δέντρα"),
 ],
 "gloss": {"ενσωματωμένο": "ενσωματωμένος — built-in", "ηλιακό πάνελ": "ηλιακό πάνελ — solar panel", "περαστικούς": "περαστικός — passer-by", "φορτίζουν": "φορτίζω — to charge", "αισθητήρες": "αισθητήρας — sensor", "ατμοσφαιρική ρύπανση": "ατμοσφαιρική ρύπανση — air pollution", "όρια": "όριο — limit", "αντιδράσεις": "αντίδραση — objection, reaction"},
})

ITEMS.append({
 "id": "l181-rep-kastanies", "title": "Ένα χωριό ξαναφυτεύει τις καστανιές του", "title_en": "A village replants its chestnut trees", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από ένα ορεινό χωριό που προσπαθεί να σώσει τον καστανεώνα του.",
 "script": [
  L("Ρεπόρτερ", "m", "Για γενιές, τα κάστανα ήταν το κύριο εισόδημα αυτού του ορεινού χωριού. Τα τελευταία χρόνια όμως, μια ασθένεια που προκαλεί ένας μύκητας, το έλκος της καστανιάς, ξεραίνει τα δέντρα το ένα μετά το άλλο. Στις πλαγιές γύρω από το χωριό φαίνονται πλέον δεκάδες γυμνοί κορμοί.", "For generations, chestnuts were the main income of this mountain village. In recent years, however, a disease caused by a fungus, chestnut blight, has been drying out the trees one after another. On the slopes around the village dozens of bare trunks can now be seen."),
  L("Γεωπόνος", "f", "Κόβουμε τα άρρωστα κλαδιά και καίμε τα κομμάτια, για να μην εξαπλωθεί ο μύκητας. Δοκιμάζουμε επίσης μια βιολογική μέθοδο: εισάγουμε στις πληγές των δέντρων μια πιο αδύναμη μορφή του ίδιου μύκητα, που κάνει την ασθένεια λιγότερο επικίνδυνη. Τα πρώτα αποτελέσματα είναι ενθαρρυντικά.", "We cut the diseased branches and burn the pieces, so that the fungus doesn't spread. We are also trying a biological method: we introduce into the trees' wounds a weaker form of the same fungus, which makes the disease less dangerous. The first results are encouraging."),
  L("Ρεπόρτερ", "m", "Παράλληλα, κάθε φθινόπωρο οι μαθητές του σχολείου φυτεύουν νέα δενδρύλλια μαζί με τους παππούδες τους. Φέτος φυτεύτηκαν διακόσια. Οι πρώτοι καρποί θα αργήσουν αρκετά χρόνια, αλλά, όπως μας είπε ένας ηλικιωμένος, «δεν φυτεύουμε για εμάς· φυτεύουμε για τα εγγόνια μας».", "At the same time, every autumn the pupils of the school plant new saplings together with their grandparents. This year two hundred were planted. The first nuts will take quite a few years, but, as an elderly man told us, 'we don't plant for ourselves; we plant for our grandchildren'."),
 ],
 "questions": [
  Q("Τι προκαλεί το έλκος της καστανιάς;", ["Ένα έντομο", "Ένας μύκητας", "Η ξηρασία", "Η ρύπανση του αέρα"], 1, "μια ασθένεια που προκαλεί ένας μύκητας, το έλκος της καστανιάς"),
  Q("Σε τι συνίσταται η βιολογική μέθοδος που δοκιμάζουν;", ["Ψεκάζουν τα δέντρα με φάρμακο", "Φυτεύουν άλλο είδος δέντρων", "Εισάγουν στις πληγές μια πιο αδύναμη μορφή του μύκητα", "Κόβουν όλα τα δέντρα"], 2, "εισάγουμε στις πληγές των δέντρων μια πιο αδύναμη μορφή του ίδιου μύκητα"),
  Q("Ποιοι φυτεύουν τα νέα δενδρύλλια;", ["Οι μαθητές μαζί με τους παππούδες τους", "Μια εταιρεία από την πόλη", "Οι γεωπόνοι μόνοι τους", "Εθελοντές από το εξωτερικό"], 0, "οι μαθητές του σχολείου φυτεύουν νέα δενδρύλλια μαζί με τους παππούδες τους"),
 ],
 "gloss": {"καστανεώνα": "καστανεώνας — chestnut grove", "κάστανα": "κάστανο — chestnut", "εισόδημα": "εισόδημα — income", "μύκητας": "μύκητας — fungus", "έλκος της καστανιάς": "έλκος της καστανιάς — chestnut blight", "ξεραίνει": "ξεραίνω — to dry out, wither", "κορμοί": "κορμός — trunk", "εξαπλωθεί": "εξαπλώνομαι — to spread", "πληγές": "πληγή — wound", "δενδρύλλια": "δενδρύλλιο — sapling"},
})

ITEMS.append({
 "id": "l181-c1-giati-kokkinizoun-ta-fylla", "title": "Γιατί αλλάζουν χρώμα τα φύλλα το φθινόπωρο", "title_en": "Why leaves change colour in autumn", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια βοτανολόγο να εξηγεί σε μια ραδιοφωνική εκπομπή γιατί τα φύλλα κιτρινίζουν και κοκκινίζουν το φθινόπωρο.",
 "script": [
  L("Βοτανολόγος", "f", "Το πράσινο χρώμα των φύλλων οφείλεται στη χλωροφύλλη, την ουσία με την οποία τα φυτά αξιοποιούν το φως του ήλιου. Η χλωροφύλλη όμως διασπάται συνεχώς και πρέπει να ανανεώνεται. Όταν οι μέρες μικραίνουν και κάνει κρύο, το δέντρο σταματά να την παράγει, και το πράσινο σβήνει σιγά σιγά.", "The green colour of leaves is due to chlorophyll, the substance with which plants make use of sunlight. Chlorophyll, however, breaks down constantly and must be renewed. When the days get shorter and it gets cold, the tree stops producing it, and the green fades little by little."),
  L("Βοτανολόγος", "f", "Τότε αποκαλύπτονται τα κίτρινα και πορτοκαλί καροτενοειδή, που υπήρχαν στο φύλλο όλο το καλοκαίρι, κρυμμένα κάτω από το πράσινο. Το κόκκινο είναι άλλη υπόθεση: οι ανθοκυανίνες, που το δίνουν, δεν υπήρχαν πριν· πολλά δέντρα τις παράγουν από την αρχή το φθινόπωρο, κυρίως όταν οι μέρες είναι ηλιόλουστες και οι νύχτες δροσερές.", "Then the yellow and orange carotenoids are revealed, which were in the leaf all summer, hidden under the green. Red is another matter: the anthocyanins that produce it weren't there before; many trees produce them from scratch in autumn, mainly when the days are sunny and the nights cool."),
  L("Βοτανολόγος", "f", "Γιατί όμως να ξοδέψει ένα δέντρο ενέργεια για ένα φύλλο που σε λίγο θα πέσει; Η επικρατέστερη εξήγηση είναι ότι οι ανθοκυανίνες λειτουργούν σαν αντηλιακό: προστατεύουν το φύλλο όσο το δέντρο «μαζεύει» από αυτό τα πολύτιμα θρεπτικά συστατικά, πριν το αφήσει να πέσει. Υπάρχουν και άλλες υποθέσεις, πιο αμφιλεγόμενες, ότι το κόκκινο είναι ένα μήνυμα προς τα έντομα, μια προειδοποίηση ότι το δέντρο είναι υγιές και ικανό να αμυνθεί.", "But why would a tree spend energy on a leaf that will soon fall? The prevailing explanation is that anthocyanins act like a sunscreen: they protect the leaf while the tree 'collects' the precious nutrients from it, before letting it fall. There are other, more controversial hypotheses, that red is a message to insects, a warning that the tree is healthy and able to defend itself."),
 ],
 "questions": [
  Q("Γιατί σβήνει το πράσινο χρώμα το φθινόπωρο;", ["Γιατί η χλωροφύλλη παγώνει", "Γιατί το δέντρο σταματά να παράγει χλωροφύλλη, που διασπάται συνεχώς", "Γιατί τα φύλλα δέχονται λιγότερο νερό", "Γιατί τα έντομα τρώνε τη χλωροφύλλη"], 1, "Η χλωροφύλλη όμως διασπάται συνεχώς και πρέπει να ανανεώνεται"),
  Q("Σε τι διαφέρουν οι ανθοκυανίνες από τα καροτενοειδή;", ["Είναι κίτρινες και όχι κόκκινες", "Βρίσκονται μόνο στις ρίζες", "Δεν υπήρχαν πριν· πολλά δέντρα τις παράγουν από την αρχή το φθινόπωρο", "Υπάρχουν μόνο σε δέντρα της ερήμου"], 2, "οι ανθοκυανίνες, που το δίνουν, δεν υπήρχαν πριν"),
  Q("Ποια είναι η επικρατέστερη εξήγηση για το κόκκινο χρώμα;", ["Λειτουργεί σαν αντηλιακό όσο το δέντρο παίρνει πίσω τα θρεπτικά συστατικά", "Προσελκύει πουλιά", "Ζεσταίνει το φύλλο τη νύχτα", "Είναι απλώς ένα τυχαίο αποτέλεσμα"], 0, "οι ανθοκυανίνες λειτουργούν σαν αντηλιακό"),
 ],
 "gloss": {"κιτρινίζουν": "κιτρινίζω — to turn yellow", "χλωροφύλλη": "χλωροφύλλη — chlorophyll", "αξιοποιούν": "αξιοποιώ — to make use of", "διασπάται": "διασπώμαι — to break down", "καροτενοειδή": "καροτενοειδή — carotenoids", "ανθοκυανίνες": "ανθοκυανίνη — anthocyanin", "ηλιόλουστες": "ηλιόλουστος — sunny", "επικρατέστερη": "επικρατέστερος — prevailing", "αντηλιακό": "αντηλιακό — sunscreen", "θρεπτικά συστατικά": "θρεπτικά συστατικά — nutrients", "αμφιλεγόμενες": "αμφιλεγόμενος — controversial"},
})

ITEMS.append({
 "id": "l181-c1-giati-den-gargalame-ton-eafto-mas", "title": "Γιατί δεν μπορούμε να γαργαλήσουμε τον εαυτό μας", "title_en": "Why we can't tickle ourselves", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια νευροεπιστήμονα σε μια εκπομπή για την επιστήμη.",
 "script": [
  L("Παρουσιαστής", "m", "Όλοι το έχουμε δοκιμάσει: όσο κι αν προσπαθήσουμε, δεν μπορούμε να γαργαλήσουμε τον εαυτό μας. Γιατί;", "We've all tried it: however hard we try, we can't tickle ourselves. Why?"),
  L("Νευροεπιστήμονας", "f", "Γιατί ο εγκέφαλός μας προβλέπει τις συνέπειες των δικών μας κινήσεων. Κάθε φορά που κινούμαστε, στέλνει ένα αντίγραφο της εντολής σε περιοχές όπως η παρεγκεφαλίδα, οι οποίες υπολογίζουν τι θα νιώσουμε. Όταν η αίσθηση έρθει, είναι ήδη «αναμενόμενη», και ο εγκέφαλος τη μειώνει.", "Because our brain predicts the consequences of our own movements. Every time we move, it sends a copy of the command to areas such as the cerebellum, which calculate what we will feel. When the sensation arrives, it is already 'expected', and the brain turns it down."),
  L("Παρουσιαστής", "m", "Πώς το απέδειξαν αυτό οι ερευνητές;", "How did researchers prove this?"),
  L("Νευροεπιστήμονας", "f", "Σε ένα γνωστό πείραμα, οι συμμετέχοντες κινούσαν έναν μοχλό, και ένα ρομπότ μετέφερε την κίνηση σε ένα μαλακό εργαλείο που άγγιζε την παλάμη τους. Όταν το ρομπότ πρόσθετε μια μικρή καθυστέρηση, λίγων δεκάτων του δευτερολέπτου, ή άλλαζε την κατεύθυνση της κίνησης, το άγγιγμα γινόταν πιο γαργαλιστικό. Η πρόβλεψη δεν ταίριαζε πια με την πραγματικότητα.", "In a well-known experiment, participants moved a lever, and a robot transferred the movement to a soft tool that touched their palm. When the robot added a small delay, of a few tenths of a second, or changed the direction of the movement, the touch became more ticklish. The prediction no longer matched reality."),
  L("Παρουσιαστής", "m", "Και τι μας λέει αυτό για τον εγκέφαλο;", "And what does this tell us about the brain?"),
  L("Νευροεπιστήμονας", "f", "Ότι δεν καταγράφει απλώς τον κόσμο· τον προβλέπει συνεχώς και δίνει προσοχή κυρίως σε ό,τι δεν περίμενε. Είναι πολύ χρήσιμο: έτσι ξεχωρίζουμε το χέρι μας που ακουμπά το μπράτσο μας από ένα έντομο που περπατά πάνω του.", "That it doesn't simply record the world; it constantly predicts it and pays attention mainly to what it didn't expect. It's very useful: that's how we tell apart our own hand touching our arm from an insect walking on it."),
 ],
 "questions": [
  Q("Τι κάνει ο εγκέφαλος με μια αίσθηση που προκαλούμε μόνοι μας;", ["Την ενισχύει", "Τη μειώνει, γιατί είναι ήδη αναμενόμενη", "Την αγνοεί εντελώς", "Τη στέλνει στην παρεγκεφαλίδα για να την αποθηκεύσει"], 1, "Όταν η αίσθηση έρθει, είναι ήδη «αναμενόμενη», και ο εγκέφαλος τη μειώνει"),
  Q("Πότε το άγγιγμα γινόταν πιο γαργαλιστικό στο πείραμα;", ["Όταν οι συμμετέχοντες έκλειναν τα μάτια", "Όταν το εργαλείο ήταν πιο σκληρό", "Όταν το ρομπότ πρόσθετε μια μικρή καθυστέρηση ή άλλαζε την κατεύθυνση", "Όταν το πείραμα γινόταν σε ζευγάρια"], 2, "Όταν το ρομπότ πρόσθετε μια μικρή καθυστέρηση, λίγων δεκάτων του δευτερολέπτου, ή άλλαζε την κατεύθυνση της κίνησης"),
  Q("Γιατί είναι χρήσιμη αυτή η λειτουργία του εγκεφάλου;", ["Μας βοηθά να ξεχωρίζουμε τις δικές μας κινήσεις από κάτι εξωτερικό, όπως ένα έντομο", "Μας κάνει να γελάμε πιο εύκολα", "Μας βοηθά να κοιμόμαστε", "Βελτιώνει τη μνήμη μας"], 0, "έτσι ξεχωρίζουμε το χέρι μας που ακουμπά το μπράτσο μας από ένα έντομο που περπατά πάνω του"),
 ],
 "gloss": {"γαργαλήσουμε": "γαργαλώ — to tickle", "νευροεπιστήμονα": "νευροεπιστήμονας — neuroscientist", "συνέπειες": "συνέπεια — consequence", "αντίγραφο": "αντίγραφο — copy", "παρεγκεφαλίδα": "παρεγκεφαλίδα — cerebellum", "αναμενόμενη": "αναμενόμενος — expected", "μοχλό": "μοχλός — lever", "καθυστέρηση": "καθυστέρηση — delay", "γαργαλιστικό": "γαργαλιστικός — ticklish", "μπράτσο": "μπράτσο — (upper) arm"},
})

rnd = random.Random(181)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-181.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
