# Source for library/listening/listening-166.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l166.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l166-ann-aftoexypiretisi-vivliothiki", "title": "Νέα μηχανήματα αυτοεξυπηρέτησης στη βιβλιοθήκη", "title_en": "New self-service machines at the library", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα της δημοτικής βιβλιοθήκης.",
 "script": [
  L("Υπάλληλος", "f", "Αγαπητοί επισκέπτες, από τη Δευτέρα θα λειτουργούν στο ισόγειο δύο μηχανήματα αυτοεξυπηρέτησης. Με αυτά μπορείτε να δανειστείτε και να επιστρέψετε βιβλία μόνοι σας, χωρίς να περιμένετε στην ουρά. Αρκεί να σκανάρετε την κάρτα μέλους σας και να ακουμπήσετε τα βιβλία πάνω στο μηχάνημα.", "Dear visitors, from Monday two self-service machines will be in operation on the ground floor. With them you can borrow and return books by yourselves, without waiting in the queue. All you have to do is scan your membership card and place the books on the machine."),
  L("Υπάλληλος", "f", "Επιπλέον, δίπλα στην κεντρική είσοδο τοποθετήθηκε ένα κουτί επιστροφής, που είναι διαθέσιμο είκοσι τέσσερις ώρες το εικοσιτετράωρο. Έτσι, μπορείτε να επιστρέφετε βιβλία ακόμη και όταν η βιβλιοθήκη είναι κλειστή. Παρακαλούμε να μη ρίχνετε στο κουτί επιτραπέζια παιχνίδια ή δίσκους, γιατί μπορεί να σπάσουν· αυτά επιστρέφονται μόνο στο γκισέ.", "In addition, a return box has been placed next to the main entrance, available twenty-four hours a day. So you can return books even when the library is closed. Please do not drop board games or records into the box, because they may break; these are returned only at the desk."),
  L("Υπάλληλος", "f", "Την πρώτη εβδομάδα, εθελοντές θα βρίσκονται δίπλα στα μηχανήματα για να βοηθούν όσους δυσκολεύονται. Το προσωπικό, φυσικά, παραμένει στη διάθεσή σας για προτάσεις βιβλίων και για κάθε άλλη πληροφορία.", "In the first week, volunteers will be next to the machines to help anyone who has difficulty. The staff, of course, remain at your disposal for book recommendations and any other information."),
 ],
 "questions": [
  Q("Τι πρέπει να κάνει κανείς για να δανειστεί ένα βιβλίο από το μηχάνημα;", ["Να πληρώσει με κάρτα", "Να σκανάρει την κάρτα μέλους και να ακουμπήσει τα βιβλία στο μηχάνημα", "Να γράψει τον τίτλο σε μια οθόνη", "Να ζητήσει έναν κωδικό από το γκισέ"], 1, "Αρκεί να σκανάρετε την κάρτα μέλους σας και να ακουμπήσετε τα βιβλία πάνω στο μηχάνημα"),
  Q("Τι δεν πρέπει να ρίχνει κανείς στο κουτί επιστροφής;", ["Βιβλία για παιδιά", "Περιοδικά", "Επιτραπέζια παιχνίδια ή δίσκους", "Βιβλία με σκληρό εξώφυλλο"], 2, "να μη ρίχνετε στο κουτί επιτραπέζια παιχνίδια ή δίσκους, γιατί μπορεί να σπάσουν"),
  Q("Ποιοι θα βοηθούν την πρώτη εβδομάδα;", ["Εθελοντές", "Οι τεχνικοί της εταιρείας", "Μαθητές του λυκείου", "Κανείς"], 0, "εθελοντές θα βρίσκονται δίπλα στα μηχανήματα"),
 ],
 "gloss": {"μεγάφωνα": "μεγάφωνο — loudspeaker", "αυτοεξυπηρέτησης": "αυτοεξυπηρέτηση — self-service", "ισόγειο": "ισόγειο — ground floor", "δανειστείτε": "δανείζομαι — to borrow", "σκανάρετε": "σκανάρω — to scan", "κάρτα μέλους": "κάρτα μέλους — membership card", "τοποθετήθηκε": "τοποθετούμαι — to be placed", "εικοσιτετράωρο": "εικοσιτετράωρο — twenty-four hours, day", "επιτραπέζια παιχνίδια": "επιτραπέζιο παιχνίδι — board game", "δίσκους": "δίσκος — record (music)", "γκισέ": "γκισέ — desk, counter", "προσωπικό": "προσωπικό — staff", "διάθεσή": "στη διάθεσή σας — at your disposal"},
})

ITEMS.append({
 "id": "l166-int-stenografos", "title": "Στενογράφος στη Βουλή", "title_en": "A stenographer in parliament", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια στενογράφο που καταγράφει τις συνεδριάσεις της Βουλής.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς κάνει ένας στενογράφος της Βουλής;", "What exactly does a parliamentary stenographer do?"),
  L("Στενογράφος", "f", "Καταγράφουμε όλα όσα λέγονται στην αίθουσα, λέξη προς λέξη, για τα πρακτικά. Τα πρακτικά είναι το επίσημο αρχείο της Βουλής. Αν σε πενήντα χρόνια κάποιος θέλει να μάθει τι είπε ένας βουλευτής, θα διαβάσει αυτό που γράψαμε εμείς.", "We record everything that is said in the chamber, word for word, for the official record. The record is parliament's official archive. If in fifty years someone wants to know what an MP said, they will read what we wrote."),
  L("Δημοσιογράφος", "m", "Δεν υπάρχει πια ηχογράφηση; Γιατί χρειάζονται άνθρωποι;", "Isn't there recording now? Why are people needed?"),
  L("Στενογράφος", "f", "Υπάρχει, και μας βοηθάει πολύ. Όμως το μικρόφωνο δεν πιάνει τις φωνές από τα έδρανα, όταν όλοι μιλούν μαζί. Εμείς είμαστε μέσα στην αίθουσα και βλέπουμε ποιος διέκοψε ποιον. Γι' αυτό δουλεύουμε με τη σειρά, λίγα λεπτά ο καθένας, και μετά πηγαίνουμε στο γραφείο να καθαρογράψουμε το κομμάτι μας.", "There is, and it helps us a lot. But the microphone doesn't pick up the voices from the benches when everyone talks at once. We are in the chamber and we see who interrupted whom. That's why we work in turns, a few minutes each, and then we go to the office to write up our section in full."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το πιο δύσκολο;", "What is the hardest part?"),
  L("Στενογράφος", "f", "Να μένεις ουδέτερη. Μπορεί να διαφωνώ ριζικά με κάποιον, αλλά οφείλω να γράψω τα λόγια του με την ίδια προσοχή. Και να μη διορθώνω τα λάθη τους, εκτός αν είναι προφανής παραδρομή, όπως μια λάθος ημερομηνία.", "Staying neutral. I may disagree completely with someone, but I am obliged to write his words with the same care. And not to correct their mistakes, unless it's an obvious slip, like a wrong date."),
 ],
 "questions": [
  Q("Τι είναι τα πρακτικά;", ["Οι σημειώσεις των βουλευτών", "Το επίσημο αρχείο της Βουλής", "Ένα βιβλίο με νόμους", "Οι ειδήσεις της ημέρας"], 1, "Τα πρακτικά είναι το επίσημο αρχείο της Βουλής"),
  Q("Γιατί δεν αρκεί η ηχογράφηση;", ["Γιατί χαλάει συχνά", "Γιατί απαγορεύεται", "Γιατί το μικρόφωνο δεν πιάνει τις φωνές από τα έδρανα όταν όλοι μιλούν μαζί", "Γιατί κοστίζει πολύ"], 2, "το μικρόφωνο δεν πιάνει τις φωνές από τα έδρανα, όταν όλοι μιλούν μαζί"),
  Q("Πότε διορθώνει τα λάθη των ομιλητών;", ["Πάντα", "Μόνο όταν είναι προφανής παραδρομή, όπως μια λάθος ημερομηνία", "Όταν της το ζητούν", "Ποτέ, ούτε τις ημερομηνίες"], 1, "εκτός αν είναι προφανής παραδρομή, όπως μια λάθος ημερομηνία"),
 ],
 "gloss": {"στενογράφο": "στενογράφος — stenographer", "στενογράφος": "στενογράφος — stenographer", "συνεδριάσεις": "συνεδρίαση — session, sitting", "Βουλής": "Βουλή — parliament", "πρακτικά": "πρακτικά — minutes, official record", "βουλευτής": "βουλευτής — member of parliament", "ηχογράφηση": "ηχογράφηση — recording", "έδρανα": "έδρανο — bench (in parliament)", "διέκοψε": "διακόπτω — to interrupt", "καθαρογράψουμε": "καθαρογράφω — to write up a clean copy", "ουδέτερη": "ουδέτερος — neutral", "ριζικά": "ριζικά — radically, completely", "παραδρομή": "παραδρομή — slip, oversight"},
})

ITEMS.append({
 "id": "l166-int-skyloi-xionostivades", "title": "Σκύλοι που βρίσκουν ανθρώπους στο χιόνι", "title_en": "Dogs that find people under avalanche snow", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν εθελοντή μιας ομάδας διάσωσης, που εκπαιδεύει σκύλους για χιονοστιβάδες.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς βρίσκει ένας σκύλος έναν άνθρωπο κάτω από το χιόνι;", "How does a dog find a person under the snow?"),
  L("Εθελοντής", "m", "Με τη μύτη του, φυσικά. Η μυρωδιά του ανθρώπου ανεβαίνει μέσα από το χιόνι, ακόμη και από βάθος αρκετών μέτρων. Ένας εκπαιδευμένος σκύλος μπορεί να ψάξει μια περιοχή σε λίγα λεπτά, ενώ μια ομάδα ανθρώπων με κοντάρια θα χρειαζόταν ώρες.", "With its nose, of course. A person's scent rises through the snow, even from a depth of several metres. A trained dog can search an area in a few minutes, while a team of people with probes would need hours."),
  L("Δημοσιογράφος", "f", "Γιατί είναι τόσο σημαντική η ταχύτητα;", "Why is speed so important?"),
  L("Εθελοντής", "m", "Γιατί κάτω από το χιόνι ο χρόνος τελειώνει γρήγορα. Οι περισσότεροι επιζούν αν τους βγάλουμε μέσα στο πρώτο τέταρτο της ώρας. Μετά, οι πιθανότητες πέφτουν απότομα, κυρίως επειδή λείπει ο αέρας.", "Because under the snow time runs out quickly. Most people survive if we get them out within the first quarter of an hour. After that, the chances drop sharply, mainly because of the lack of air."),
  L("Δημοσιογράφος", "f", "Πώς εκπαιδεύετε τους σκύλους;", "How do you train the dogs?"),
  L("Εθελοντής", "m", "Σαν παιχνίδι κρυφτού. Στην αρχή κρύβεται ο ιδιοκτήτης πίσω από ένα δέντρο, μετά σε μια μικρή τρύπα στο χιόνι, και σιγά σιγά πιο βαθιά. Όταν ο σκύλος τον βρει, παίρνει το αγαπημένο του παιχνίδι. Για εκείνον δεν είναι δουλειά· είναι το πιο ωραίο παιχνίδι του κόσμου.", "Like a game of hide-and-seek. At first the owner hides behind a tree, then in a small hole in the snow, and gradually deeper. When the dog finds him, it gets its favourite toy. For the dog it isn't work; it's the best game in the world."),
 ],
 "questions": [
  Q("Γιατί ο σκύλος είναι πιο γρήγορος από μια ομάδα ανθρώπων;", ["Γιατί τρέχει πιο γρήγορα στο χιόνι", "Γιατί μυρίζει τον άνθρωπο μέσα από το χιόνι και ψάχνει μια περιοχή σε λίγα λεπτά", "Γιατί ακούει τις φωνές", "Γιατί βλέπει καλύτερα στο σκοτάδι"], 1, "Ένας εκπαιδευμένος σκύλος μπορεί να ψάξει μια περιοχή σε λίγα λεπτά"),
  Q("Γιατί είναι τόσο σημαντική η ταχύτητα;", ["Γιατί οι περισσότεροι επιζούν μόνο αν βγουν μέσα στο πρώτο τέταρτο", "Γιατί ο σκύλος κουράζεται", "Γιατί νυχτώνει", "Γιατί το χιόνι λιώνει"], 0, "Οι περισσότεροι επιζούν αν τους βγάλουμε μέσα στο πρώτο τέταρτο της ώρας"),
  Q("Πώς εκπαιδεύονται οι σκύλοι;", ["Με τιμωρίες", "Με βίντεο", "Σαν παιχνίδι κρυφτού, με επιβράβευση το αγαπημένο τους παιχνίδι", "Με πολλές ώρες τρέξιμο"], 2, "Σαν παιχνίδι κρυφτού"),
 ],
 "gloss": {"εθελοντή": "εθελοντής — volunteer", "διάσωσης": "διάσωση — rescue", "εκπαιδεύει": "εκπαιδεύω — to train", "χιονοστιβάδες": "χιονοστιβάδα — avalanche", "μυρωδιά": "μυρωδιά — smell, scent", "βάθος": "βάθος — depth", "κοντάρια": "κοντάρι — pole, probe", "επιζούν": "επιζώ — to survive", "πιθανότητες": "πιθανότητα — chance, probability", "απότομα": "απότομα — sharply, abruptly", "κρυφτού": "κρυφτό — hide-and-seek", "ιδιοκτήτης": "ιδιοκτήτης — owner"},
})

ITEMS.append({
 "id": "l166-dia-proto-taxidi-xoris-goneis", "title": "Το πρώτο ταξίδι χωρίς τους γονείς", "title_en": "The first trip without the parents", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο ανάμεσα σε μια μητέρα και τη δεκαεφτάχρονη κόρη της, που θέλει να πάει κάμπινγκ με φίλους.",
 "script": [
  L("Κόρη", "f", "Μαμά, τελειώσαμε τις εξετάσεις και θέλουμε να πάμε με την Ιφιγένεια και τη Ράνια για κάμπινγκ στη Χαλκιδική. Πέντε μέρες μόνο.", "Mum, we've finished our exams and we want to go camping in Halkidiki with Ifigeneia and Rania. Only five days."),
  L("Μητέρα", "f", "Τρία κορίτσια μόνα σας σε κάμπινγκ; Δεν ξέρω, Δανάη. Πού θα μένετε ακριβώς;", "Three girls on your own at a campsite? I don't know, Danai. Where exactly will you stay?"),
  L("Κόρη", "f", "Σε ένα οργανωμένο κάμπινγκ, με ρεσεψιόν και φύλακα όλη τη νύχτα. Η μητέρα της Ράνιας το ξέρει, πήγαινε εκεί κάθε καλοκαίρι. Και θα παίρνουμε τηλέφωνο κάθε βράδυ, το υπόσχομαι.", "At an organised campsite, with a reception and a guard all night. Rania's mother knows it, she used to go there every summer. And we'll phone every evening, I promise."),
  L("Μητέρα", "f", "Και τα χρήματα; Έχεις υπολογίσει πόσο θα κοστίσει;", "And the money? Have you worked out how much it will cost?"),
  L("Κόρη", "f", "Ναι, έχω κάνει λογαριασμό. Με το ΚΤΕΛ, τη σκηνή και το φαγητό βγαίνει γύρω στα εκατόν πενήντα ευρώ. Τα εκατό τα έχω μαζέψει από τα ιδιαίτερα που έκανα στον μικρό του τρίτου ορόφου.", "Yes, I've done the maths. With the coach, the tent and food it comes to about a hundred and fifty euros. I've saved a hundred from the private lessons I gave the little boy on the third floor."),
  L("Μητέρα", "f", "Βλέπω ότι τα έχεις σκεφτεί όλα. Εντάξει, αλλά με έναν όρο: θα μου στείλεις το τηλέφωνο του κάμπινγκ και των γονιών των κοριτσιών, και τα υπόλοιπα πενήντα θα τα βάλω εγώ.", "I see you've thought of everything. All right, but on one condition: you'll send me the phone number of the campsite and of the girls' parents, and I'll put in the remaining fifty."),
 ],
 "questions": [
  Q("Γιατί η κόρη πιστεύει ότι το κάμπινγκ είναι ασφαλές;", ["Γιατί θα πάει και ο πατέρας της", "Γιατί είναι οργανωμένο, με ρεσεψιόν και φύλακα όλη τη νύχτα", "Γιατί είναι μέσα στην πόλη", "Γιατί θα μείνουν σε ξενοδοχείο"], 1, "Σε ένα οργανωμένο κάμπινγκ, με ρεσεψιόν και φύλακα όλη τη νύχτα"),
  Q("Από πού έχει μαζέψει χρήματα η κόρη;", ["Από ιδιαίτερα μαθήματα σε ένα παιδί της πολυκατοικίας", "Από το χαρτζιλίκι της γιαγιάς", "Από δουλειά σε καφετέρια", "Από ένα βραβείο"], 0, "Τα εκατό τα έχω μαζέψει από τα ιδιαίτερα που έκανα στον μικρό του τρίτου ορόφου"),
  Q("Με ποιον όρο συμφωνεί η μητέρα;", ["Να γυρίσουν σε τρεις μέρες", "Να πάει και η ίδια", "Να της στείλει τα τηλέφωνα του κάμπινγκ και των γονιών των κοριτσιών", "Να πληρώσει η κόρη όλα τα έξοδα"], 2, "θα μου στείλεις το τηλέφωνο του κάμπινγκ και των γονιών των κοριτσιών"),
 ],
 "gloss": {"δεκαεφτάχρονη": "δεκαεφτάχρονος — seventeen-year-old", "κάμπινγκ": "κάμπινγκ — campsite, camping", "οργανωμένο": "οργανωμένος — organised", "ρεσεψιόν": "ρεσεψιόν — reception", "φύλακα": "φύλακας — guard", "υπόσχομαι": "υπόσχομαι — to promise", "υπολογίσει": "υπολογίζω — to calculate", "λογαριασμό": "κάνω λογαριασμό — to do the sums", "ΚΤΕΛ": "ΚΤΕΛ — intercity coach service", "σκηνή": "σκηνή — tent", "ιδιαίτερα": "ιδιαίτερα — private lessons", "όρο": "όρος — condition, term"},
})

ITEMS.append({
 "id": "l166-dia-onomatodosia", "title": "Βάφτιση ή δήλωση στο ληξιαρχείο;", "title_en": "Christening or registering the name?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο ανάμεσα σε ένα ζευγάρι που συζητά πώς θα δώσει όνομα στο μωρό του.",
 "script": [
  L("Άντρας", "m", "Η μητέρα μου ρώτησε πάλι πότε θα κάνουμε τη βάφτιση. Ήδη ψάχνει κέντρο για το τραπέζι.", "My mother asked again when we're having the christening. She's already looking for a venue for the meal."),
  L("Γυναίκα", "f", "Το ξέρω. Αλλά εμείς δεν έχουμε αποφασίσει ακόμα. Μπορούμε απλώς να δηλώσουμε το όνομα στο ληξιαρχείο, χωρίς βάφτιση. Το έκαναν και η Νεφέλη με τον Άρη.", "I know. But we haven't decided yet. We can simply register the name at the registry office, without a christening. Nefeli and Aris did that too."),
  L("Άντρας", "m", "Κι αν η μικρή θέλει αργότερα να βαφτιστεί; Δεν θέλω να νιώσει ότι της πήραμε την επιλογή.", "And what if the little one wants to be christened later? I don't want her to feel we took the choice away from her."),
  L("Γυναίκα", "f", "Μα αυτό ακριβώς λέω. Αν δηλώσουμε τώρα το όνομα, μπορεί να βαφτιστεί όποτε θέλει, και στα δεκαοχτώ της. Ενώ αν τη βαφτίσουμε τώρα, αποφασίζουμε εμείς για εκείνη.", "But that's exactly what I'm saying. If we register the name now, she can be christened whenever she wants, even at eighteen. Whereas if we christen her now, we decide for her."),
  L("Άντρας", "m", "Έχεις δίκιο σε αυτό. Το πρόβλημα είναι η γιαγιά. Και η νονά, που την έχουμε ήδη ρωτήσει.", "You're right about that. The problem is grandma. And the godmother, whom we've already asked."),
  L("Γυναίκα", "f", "Ας κάνουμε μια γιορτή για το όνομα, με όλη την οικογένεια και τη νονά δίπλα μας. Θα έχει τραπέζι, μουσική και μπομπονιέρες, για να είναι όλοι ευχαριστημένοι. Μόνο που δεν θα γίνει σε εκκλησία.", "Let's have a celebration for the name, with the whole family and the godmother beside us. There will be a meal, music and favours, so everyone is happy. Only it won't take place in a church."),
 ],
 "questions": [
  Q("Τι προτείνει η γυναίκα για το όνομα;", ["Να το διαλέξει η γιαγιά", "Να δηλωθεί στο ληξιαρχείο χωρίς βάφτιση", "Να περιμένουν έναν χρόνο", "Να γίνει η βάφτιση στο εξωτερικό"], 1, "Μπορούμε απλώς να δηλώσουμε το όνομα στο ληξιαρχείο, χωρίς βάφτιση"),
  Q("Ποιο είναι το επιχείρημά της;", ["Ότι η βάφτιση κοστίζει πολύ", "Ότι έτσι το παιδί θα μπορεί να αποφασίσει μόνο του αργότερα", "Ότι δεν βρίσκουν νονά", "Ότι η εκκλησία είναι μακριά"], 1, "μπορεί να βαφτιστεί όποτε θέλει, και στα δεκαοχτώ της"),
  Q("Τι προτείνει τελικά η γυναίκα για να είναι όλοι ευχαριστημένοι;", ["Μια γιορτή για το όνομα με την οικογένεια και τη νονά", "Να κάνουν βάφτιση μόνο για τη γιαγιά", "Να μην καλέσουν κανέναν", "Να ρωτήσουν τον παπά"], 0, "Ας κάνουμε μια γιορτή για το όνομα"),
 ],
 "gloss": {"βάφτιση": "βάφτιση — christening", "κέντρο": "κέντρο — reception venue", "δηλώσουμε": "δηλώνω — to declare, to register", "ληξιαρχείο": "ληξιαρχείο — registry office", "βαφτιστεί": "βαφτίζομαι — to be christened", "επιλογή": "επιλογή — choice", "νονά": "νονά — godmother", "μπομπονιέρες": "μπομπονιέρα — wedding/christening favour", "εκκλησία": "εκκλησία — church"},
})

ITEMS.append({
 "id": "l166-mon-teleftaio-ploio", "title": "Η νύχτα που έχασα το τελευταίο πλοίο", "title_en": "The night I missed the last boat", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια νεαρή γυναίκα να διηγείται σε ένα ραδιοφωνικό πρόγραμμα μια περιπέτεια από τις διακοπές της.",
 "script": [
  L("Γυναίκα", "f", "Πριν από δύο χρόνια έμενα στη Νάξο και πήγα για μια μέρα στην Πάρο να δω μια φίλη. Το τελευταίο πλοίο της επιστροφής έφευγε στις επτά. Καθόμασταν σε ένα καφενείο στο λιμάνι και κοιτούσα το ρολόι, αλλά το κινητό μου είχε μείνει από μπαταρία και το ρολόι του καφενείου, όπως αποδείχτηκε, πήγαινε πίσω.", "Two years ago I was staying on Naxos and went for a day to Paros to see a friend. The last boat back left at seven. We were sitting in a café at the harbour and I kept looking at the clock, but my phone had run out of battery and the café clock, as it turned out, was slow."),
  L("Γυναίκα", "f", "Όταν φτάσαμε στην προβλήτα, το πλοίο είχε ήδη σηκώσει τον καταπέλτη. Η φίλη μου έμενε σε ένα δωμάτιο με τη μητέρα της, οπότε δεν μπορούσα να κοιμηθώ εκεί, και όλα τα ξενοδοχεία ήταν γεμάτα, γιατί ήταν δεκαπενταύγουστος.", "When we reached the pier, the boat had already raised its ramp. My friend was staying in a room with her mother, so I couldn't sleep there, and all the hotels were full, because it was the fifteenth of August."),
  L("Γυναίκα", "f", "Τότε ένας ψαράς που μας άκουσε μου είπε ότι έβγαινε για ψάρεμα κοντά στη Νάξο στις τέσσερις τα ξημερώματα. Πέρασα τη νύχτα σε ένα παγκάκι με τη φίλη μου, κουβεντιάζοντας, και ξημερώματα μπήκα σε ένα καΐκι που μύριζε πετρέλαιο και ψάρια. Είδα την ανατολή από τη μέση της θάλασσας. Τελικά, ήταν το καλύτερο λάθος που έχω κάνει.", "Then a fisherman who overheard us told me he was going out fishing near Naxos at four in the morning. I spent the night on a bench with my friend, chatting, and at dawn I got into a boat that smelled of diesel and fish. I saw the sunrise from the middle of the sea. In the end, it was the best mistake I've ever made."),
 ],
 "questions": [
  Q("Γιατί έχασε το πλοίο;", ["Γιατί ξύπνησε αργά", "Γιατί το κινητό της είχε κλείσει και το ρολόι του καφενείου πήγαινε πίσω", "Γιατί το πλοίο έφυγε νωρίτερα από το πρόγραμμα", "Γιατί δεν βρήκε ταξί"], 1, "το κινητό μου είχε μείνει από μπαταρία και το ρολόι του καφενείου, όπως αποδείχτηκε, πήγαινε πίσω"),
  Q("Γιατί δεν βρήκε ξενοδοχείο;", ["Γιατί ήταν ακριβά", "Γιατί ήταν δεκαπενταύγουστος και όλα ήταν γεμάτα", "Γιατί δεν είχε χρήματα", "Γιατί ήταν κλειστά"], 1, "όλα τα ξενοδοχεία ήταν γεμάτα, γιατί ήταν δεκαπενταύγουστος"),
  Q("Πώς γύρισε τελικά στη Νάξο;", ["Με το πρώτο πλοίο του πρωινού", "Με ένα ιδιωτικό σκάφος φίλων", "Με το καΐκι ενός ψαρά στις τέσσερις τα ξημερώματα", "Με αεροπλάνο"], 2, "ξημερώματα μπήκα σε ένα καΐκι"),
 ],
 "gloss": {"διηγείται": "διηγούμαι — to narrate, tell", "περιπέτεια": "περιπέτεια — adventure", "μπαταρία": "μένω από μπαταρία — to run out of battery", "αποδείχτηκε": "αποδεικνύομαι — to turn out", "πήγαινε πίσω": "πηγαίνω πίσω — (of a clock) to be slow", "προβλήτα": "προβλήτα — pier, jetty", "καταπέλτη": "καταπέλτης — ramp (of a ferry)", "δεκαπενταύγουστος": "δεκαπενταύγουστος — 15 August (Assumption holiday)", "ψαράς": "ψαράς — fisherman", "ξημερώματα": "ξημερώματα — at dawn, early morning", "καΐκι": "καΐκι — caique, small boat", "πετρέλαιο": "πετρέλαιο — diesel", "ανατολή": "ανατολή — sunrise"},
})

ITEMS.append({
 "id": "l166-vm-podilatadiko", "title": "Μήνυμα από το ποδηλατάδικο", "title_en": "A message from the bike shop", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από το κατάστημα όπου αφήσατε το ποδήλατό σας για σέρβις.",
 "script": [
  L("Τεχνικός", "m", "Καλησπέρα σας, ο Παύλος από το ποδηλατάδικο στην Αγίου Δημητρίου. Τελειώσαμε το σέρβις στο ποδήλατό σας. Αλλάξαμε τα τακάκια στα φρένα, όπως είχαμε πει, και ρυθμίσαμε τις ταχύτητες.", "Good evening, it's Pavlos from the bike shop on Agiou Dimitriou. We've finished the service on your bike. We changed the brake pads, as we'd agreed, and adjusted the gears."),
  L("Τεχνικός", "m", "Βρήκαμε όμως και κάτι που δεν είχαμε δει την πρώτη φορά: η αλυσίδα έχει τεντωθεί αρκετά και φθείρει τα γρανάζια. Σας προτείνω να την αλλάξουμε τώρα, γιατί αν περιμένετε, μετά θα χρειαστεί να αλλάξετε και τα γρανάζια, που κοστίζουν πολύ περισσότερο. Η αλυσίδα είναι γύρω στα είκοσι πέντε ευρώ με την εργασία.", "But we also found something we hadn't seen the first time: the chain has stretched quite a lot and is wearing the sprockets. I suggest we change it now, because if you wait, you'll later need to change the sprockets as well, which cost much more. The chain is about twenty-five euros including labour."),
  L("Τεχνικός", "m", "Δεν την αλλάζουμε αν δεν μας πείτε εσείς. Πάρτε με τηλέφωνο ως αύριο το μεσημέρι, για να είναι έτοιμο το ποδήλατο το απόγευμα. Κλείνουμε στις οχτώ, και το Σάββατο στις δύο.", "We won't change it unless you tell us. Call me by tomorrow at noon, so the bike is ready in the afternoon. We close at eight, and on Saturday at two."),
 ],
 "questions": [
  Q("Τι έκαναν ήδη στο ποδήλατο;", ["Άλλαξαν τα λάστιχα", "Άλλαξαν τα τακάκια και ρύθμισαν τις ταχύτητες", "Έβαψαν τον σκελετό", "Άλλαξαν τη σέλα"], 1, "Αλλάξαμε τα τακάκια στα φρένα, όπως είχαμε πει, και ρυθμίσαμε τις ταχύτητες"),
  Q("Γιατί προτείνει να αλλάξουν τώρα την αλυσίδα;", ["Γιατί έχει σπάσει", "Γιατί είναι σε προσφορά", "Γιατί αλλιώς αργότερα θα χρειαστεί να αλλάξουν και τα ακριβότερα γρανάζια", "Γιατί κάνει θόρυβο"], 2, "αν περιμένετε, μετά θα χρειαστεί να αλλάξετε και τα γρανάζια"),
  Q("Ως πότε πρέπει να του τηλεφωνήσετε;", ["Ως αύριο το μεσημέρι", "Ως απόψε στις οχτώ", "Ως το Σάββατο", "Ως τη Δευτέρα"], 0, "Πάρτε με τηλέφωνο ως αύριο το μεσημέρι"),
 ],
 "gloss": {"σέρβις": "σέρβις — service", "ποδηλατάδικο": "ποδηλατάδικο — bike shop", "τακάκια": "τακάκι — brake pad", "φρένα": "φρένο — brake", "ρυθμίσαμε": "ρυθμίζω — to adjust", "ταχύτητες": "ταχύτητα — gear", "αλυσίδα": "αλυσίδα — chain", "τεντωθεί": "τεντώνομαι — to stretch", "φθείρει": "φθείρω — to wear out", "γρανάζια": "γρανάζι — sprocket, gear wheel", "εργασία": "εργασία — labour"},
})

ITEMS.append({
 "id": "l166-vm-emfanisi-film", "title": "Μήνυμα από το εργαστήριο για τα φιλμ του παππού", "title_en": "A message from the photo lab about grandad's films", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από ένα φωτογραφικό εργαστήριο, όπου πήγατε τρία παλιά φιλμ που βρήκατε σε μια μηχανή του παππού σας.",
 "script": [
  L("Φωτογράφος", "f", "Γεια σας, η Χαρά από το φωτογραφικό εργαστήριο. Σας παίρνω για τα τρία φιλμ που μας φέρατε. Τα δύο εμφανίστηκαν κανονικά, και οι φωτογραφίες βγήκαν πολύ καλύτερες από ό,τι περίμενα για φιλμ που έμειναν τόσα χρόνια μέσα σε μια μηχανή. Είναι κυρίως οικογενειακές φωτογραφίες σε μια παραλία και σε ένα πανηγύρι.", "Hello, it's Chara from the photo lab. I'm calling about the three films you brought us. Two developed normally, and the photos came out much better than I expected for films that stayed so many years inside a camera. They're mostly family photos on a beach and at a village festival."),
  L("Φωτογράφος", "f", "Το τρίτο, δυστυχώς, ήταν άγραφο. Μάλλον ο παππούς σας το είχε βάλει στη μηχανή αλλά δεν πρόλαβε να τραβήξει. Δεν θα σας χρεώσουμε γι' αυτό.", "The third, unfortunately, was blank. Your grandad probably put it in the camera but didn't get the chance to take any pictures. We won't charge you for it."),
  L("Φωτογράφος", "f", "Τις φωτογραφίες τις σκανάραμε και σε υψηλή ανάλυση, όπως ζητήσατε, και σας τις στείλαμε με email. Τα αρνητικά και τις εκτυπώσεις μπορείτε να τα παραλάβετε από αύριο. Σας συμβουλεύω να κρατάτε τα αρνητικά σε δροσερό και σκοτεινό μέρος, γιατί είναι το πιο πολύτιμο κομμάτι.", "We also scanned the photos in high resolution, as you asked, and sent them to you by email. You can collect the negatives and the prints from tomorrow. I advise you to keep the negatives in a cool, dark place, because they are the most valuable part."),
 ],
 "questions": [
  Q("Τι δείχνουν κυρίως οι φωτογραφίες;", ["Τοπία από το βουνό", "Οικογενειακές στιγμές σε μια παραλία και σε ένα πανηγύρι", "Έναν γάμο", "Παλιά κτίρια της πόλης"], 1, "Είναι κυρίως οικογενειακές φωτογραφίες σε μια παραλία και σε ένα πανηγύρι"),
  Q("Τι συνέβη με το τρίτο φιλμ;", ["Ήταν κατεστραμμένο από τον ήλιο", "Χάθηκε", "Ήταν άγραφο, χωρίς φωτογραφίες", "Χρειάζεται ειδική εμφάνιση"], 2, "Το τρίτο, δυστυχώς, ήταν άγραφο"),
  Q("Πού συμβουλεύει να φυλάτε τα αρνητικά;", ["Σε δροσερό και σκοτεινό μέρος", "Σε ένα συρτάρι στην κουζίνα", "Δίπλα στο παράθυρο", "Στο ψυγείο"], 0, "κρατάτε τα αρνητικά σε δροσερό και σκοτεινό μέρος"),
 ],
 "gloss": {"φωτογραφικό εργαστήριο": "φωτογραφικό εργαστήριο — photo lab", "φιλμ": "φιλμ — film (roll)", "μηχανή": "μηχανή — camera", "εμφανίστηκαν": "εμφανίζομαι — (of film) to be developed", "πανηγύρι": "πανηγύρι — village festival", "άγραφο": "άγραφος — blank, unexposed", "χρεώσουμε": "χρεώνω — to charge", "ανάλυση": "ανάλυση — resolution", "αρνητικά": "αρνητικό — negative (photo)", "εκτυπώσεις": "εκτύπωση — print", "πολύτιμο": "πολύτιμος — valuable"},
})

ITEMS.append({
 "id": "l166-c1-galazios-ouranos", "title": "Γιατί ο ουρανός είναι γαλάζιος και το ηλιοβασίλεμα κόκκινο", "title_en": "Why the sky is blue and the sunset red", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια φυσικό της ατμόσφαιρας σε μια εκπομπή εκλαΐκευσης της επιστήμης.",
 "script": [
  L("Δημοσιογράφος", "m", "Μια ερώτηση που κάνουν όλα τα παιδιά: γιατί ο ουρανός είναι γαλάζιος;", "A question all children ask: why is the sky blue?"),
  L("Φυσικός", "f", "Το φως του ήλιου μοιάζει λευκό, αλλά περιέχει όλα τα χρώματα. Όταν περνά μέσα από την ατμόσφαιρα, συναντά τα μόρια του αέρα, που είναι πολύ μικρότερα από το μήκος κύματος του φωτός. Αυτά τα μόρια σκεδάζουν, δηλαδή σκορπίζουν προς όλες τις κατευθύνσεις, το μπλε φως πολύ περισσότερο από το κόκκινο, γιατί το μπλε έχει μικρότερο μήκος κύματος. Το φαινόμενο λέγεται σκέδαση Ρέιλι, από τον Βρετανό φυσικό που το εξήγησε τον 19ο αιώνα. Έτσι, όπου κι αν κοιτάξουμε, μας έρχεται σκορπισμένο μπλε φως.", "Sunlight looks white, but it contains all colours. When it passes through the atmosphere, it meets the molecules of the air, which are much smaller than the wavelength of light. These molecules scatter, that is, spread in all directions, blue light much more than red, because blue has a shorter wavelength. The phenomenon is called Rayleigh scattering, after the British physicist who explained it in the 19th century. So, wherever we look, scattered blue light reaches us."),
  L("Δημοσιογράφος", "m", "Τότε γιατί όχι μωβ; Το ιώδες έχει ακόμη μικρότερο μήκος κύματος.", "Then why not purple? Violet has an even shorter wavelength."),
  L("Φυσικός", "f", "Πολύ σωστή παρατήρηση. Ο ήλιος εκπέμπει λιγότερο ιώδες φως, ένα μέρος του απορροφάται ψηλά στην ατμόσφαιρα, και κυρίως το μάτι μας είναι λιγότερο ευαίσθητο σε αυτό. Ο εγκέφαλος συνθέτει όλα αυτά και βλέπει γαλάζιο.", "A very good observation. The sun emits less violet light, part of it is absorbed high in the atmosphere, and above all our eye is less sensitive to it. The brain combines all this and sees light blue."),
  L("Δημοσιογράφος", "m", "Και το κόκκινο ηλιοβασίλεμα;", "And the red sunset?"),
  L("Φυσικός", "f", "Όταν ο ήλιος είναι χαμηλά, το φως διανύει πολύ μεγαλύτερη απόσταση μέσα στην ατμόσφαιρα για να φτάσει σε εμάς. Στη διαδρομή, το μπλε έχει σκορπιστεί σχεδόν όλο, και αυτό που απομένει είναι το πορτοκαλί και το κόκκινο. Τα σύννεφα, αντίθετα, είναι λευκά επειδή οι σταγόνες τους είναι μεγάλες και σκεδάζουν όλα τα χρώματα περίπου εξίσου.", "When the sun is low, the light travels a much greater distance through the atmosphere to reach us. Along the way, the blue has been almost entirely scattered, and what remains is orange and red. Clouds, by contrast, are white because their droplets are large and scatter all colours roughly equally."),
 ],
 "questions": [
  Q("Γιατί τα μόρια του αέρα σκεδάζουν περισσότερο το μπλε φως;", ["Γιατί το μπλε έχει μεγαλύτερη ενέργεια από τον ήλιο", "Γιατί το μπλε έχει μικρότερο μήκος κύματος", "Γιατί ο αέρας είναι μπλε", "Γιατί η θάλασσα αντανακλά το μπλε"], 1, "γιατί το μπλε έχει μικρότερο μήκος κύματος"),
  Q("Ποιος από τους λόγους που αναφέρει είναι ο κυριότερος για τον οποίο δεν βλέπουμε τον ουρανό μωβ;", ["Ότι το μάτι μας είναι λιγότερο ευαίσθητο στο ιώδες", "Ότι ο ήλιος δεν εκπέμπει καθόλου ιώδες", "Ότι το ιώδες δεν σκεδάζεται", "Ότι τα σύννεφα το κρύβουν"], 0, "κυρίως το μάτι μας είναι λιγότερο ευαίσθητο σε αυτό"),
  Q("Γιατί τα σύννεφα είναι λευκά;", ["Γιατί είναι πιο κοντά στον ήλιο", "Γιατί περιέχουν πάγο", "Γιατί οι σταγόνες τους είναι μεγάλες και σκεδάζουν όλα τα χρώματα περίπου εξίσου", "Γιατί απορροφούν το μπλε"], 2, "οι σταγόνες τους είναι μεγάλες και σκεδάζουν όλα τα χρώματα περίπου εξίσου"),
 ],
 "gloss": {"φυσικό": "φυσικός — physicist", "ατμόσφαιρας": "ατμόσφαιρα — atmosphere", "εκλαΐκευσης": "εκλαΐκευση — popularisation", "μόρια": "μόριο — molecule", "μήκος κύματος": "μήκος κύματος — wavelength", "σκεδάζουν": "σκεδάζω — to scatter (light)", "σκορπίζουν": "σκορπίζω — to scatter, spread", "κατευθύνσεις": "κατεύθυνση — direction", "σκέδαση": "σκέδαση — scattering", "ιώδες": "ιώδης — violet", "εκπέμπει": "εκπέμπω — to emit", "απορροφάται": "απορροφώμαι — to be absorbed", "ευαίσθητο": "ευαίσθητος — sensitive", "συνθέτει": "συνθέτω — to combine, compose", "διανύει": "διανύω — to travel, cover (a distance)", "σταγόνες": "σταγόνα — droplet", "εξίσου": "εξίσου — equally"},
})

ITEMS.append({
 "id": "l166-c1-ichitiko-fragma", "title": "Το ηχητικό φράγμα και ο υπερηχητικός κρότος", "title_en": "The sound barrier and the sonic boom", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν μηχανικό αεροναυπηγικής να μιλά σε μια διάλεξη για το κοινό σχετικά με το ηχητικό φράγμα.",
 "script": [
  L("Μηχανικός", "m", "Ο ήχος ταξιδεύει στον αέρα με περίπου χίλια διακόσια χιλιόμετρα την ώρα κοντά στο έδαφος, και λίγο πιο αργά σε μεγάλο ύψος, όπου ο αέρας είναι κρύος. Όταν ένα αεροπλάνο πλησιάζει αυτή την ταχύτητα, τα ηχητικά κύματα που δημιουργεί δεν προλαβαίνουν να απομακρυνθούν μπροστά του και συσσωρεύονται. Γι' αυτό οι πρώτοι πιλότοι μιλούσαν για ένα «φράγμα», σαν να υπήρχε ένας αόρατος τοίχος. Το 1947 ένας Αμερικανός πιλότος, ο Τσακ Γέιγκερ, έγινε ο πρώτος που το ξεπέρασε επίσημα, με ένα πειραματικό αεροσκάφος.", "Sound travels through air at about one thousand two hundred kilometres an hour near the ground, and a little more slowly at high altitude, where the air is cold. When an aircraft approaches this speed, the sound waves it creates can't get away ahead of it and pile up. That's why the first pilots spoke of a 'barrier', as if there were an invisible wall. In 1947 an American pilot, Chuck Yeager, became the first officially to break it, in an experimental aircraft."),
  L("Μηχανικός", "m", "Υπάρχει μια διαδεδομένη παρανόηση για τον υπερηχητικό κρότο. Πολλοί πιστεύουν ότι ακούγεται μία φορά, τη στιγμή που το αεροπλάνο «σπάει» το φράγμα. Στην πραγματικότητα, όσο πετά πιο γρήγορα από τον ήχο, σέρνει πίσω του έναν κώνο από κρουστικά κύματα. Όποιος βρίσκεται στο έδαφος ακούει τον κρότο τη στιγμή που ο κώνος περνά από πάνω του, σε όποιο σημείο της διαδρομής κι αν βρίσκεται.", "There is a widespread misconception about the sonic boom. Many people believe it is heard once, at the moment the aircraft 'breaks' the barrier. In reality, as long as it flies faster than sound, it drags behind it a cone of shock waves. Anyone on the ground hears the boom at the moment the cone passes over them, at whatever point of the route they are."),
  L("Μηχανικός", "m", "Αυτός ήταν και ένας από τους λόγους που το Κονκόρντ πετούσε με υπερηχητική ταχύτητα κυρίως πάνω από τον ωκεανό: πάνω από κατοικημένες περιοχές οι πτήσεις αυτές απαγορεύονταν. Κι ένα μικρό παράδειγμα από την καθημερινή ζωή: σύμφωνα με την πιο διαδεδομένη εξήγηση, το κροτάλισμα ενός μαστιγίου είναι ένας μικροσκοπικός υπερηχητικός κρότος, γιατί η άκρη του κινείται πιο γρήγορα από τον ήχο.", "That was also one of the reasons Concorde flew at supersonic speed mainly over the ocean: over inhabited areas such flights were prohibited. And a small example from everyday life: according to the most widespread explanation, the crack of a whip is a tiny sonic boom, because its tip moves faster than sound."),
 ],
 "questions": [
  Q("Γιατί οι πρώτοι πιλότοι μιλούσαν για «φράγμα»;", ["Γιατί υπήρχε πραγματικά ένας τοίχος αέρα", "Γιατί τα ηχητικά κύματα συσσωρεύονταν μπροστά στο αεροπλάνο, σαν αόρατος τοίχος", "Γιατί οι κινητήρες σταματούσαν", "Γιατί απαγορευόταν να πετάξουν πιο γρήγορα"], 1, "τα ηχητικά κύματα που δημιουργεί δεν προλαβαίνουν να απομακρυνθούν μπροστά του και συσσωρεύονται"),
  Q("Ποια είναι η παρανόηση για τον υπερηχητικό κρότο;", ["Ότι είναι επικίνδυνος για την υγεία", "Ότι τον ακούνε μόνο οι πιλότοι", "Ότι ακούγεται μόνο μία φορά, τη στιγμή που το αεροπλάνο ξεπερνά το φράγμα", "Ότι προκαλείται από τους κινητήρες"], 2, "Πολλοί πιστεύουν ότι ακούγεται μία φορά"),
  Q("Γιατί το Κονκόρντ πετούσε υπερηχητικά κυρίως πάνω από τον ωκεανό;", ["Γιατί πάνω από κατοικημένες περιοχές οι υπερηχητικές πτήσεις απαγορεύονταν", "Γιατί εκεί ο αέρας είναι πιο ζεστός", "Γιατί έκαιγε λιγότερα καύσιμα", "Γιατί οι επιβάτες το προτιμούσαν"], 0, "πάνω από κατοικημένες περιοχές οι πτήσεις αυτές απαγορεύονταν"),
 ],
 "gloss": {"αεροναυπηγικής": "αεροναυπηγική — aeronautical engineering", "διάλεξη": "διάλεξη — lecture", "ηχητικό φράγμα": "ηχητικό φράγμα — sound barrier", "έδαφος": "έδαφος — ground", "ύψος": "ύψος — altitude", "συσσωρεύονται": "συσσωρεύομαι — to pile up, accumulate", "αόρατος": "αόρατος — invisible", "πειραματικό": "πειραματικός — experimental", "αεροσκάφος": "αεροσκάφος — aircraft", "παρανόηση": "παρανόηση — misconception", "υπερηχητικό": "υπερηχητικός — supersonic", "κρότο": "κρότος — bang, boom", "σέρνει": "σέρνω — to drag", "κώνο": "κώνος — cone", "κρουστικά κύματα": "κρουστικό κύμα — shock wave", "κατοικημένες": "κατοικημένος — inhabited", "κροτάλισμα": "κροτάλισμα — crack, rattle", "μαστιγίου": "μαστίγιο — whip", "μικροσκοπικός": "μικροσκοπικός — tiny"},
})

rnd = random.Random(166)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-166.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
