# Source for library/listening/listening-217.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l217.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l217-news-katoikidia-ploia", "title": "Καμπίνες για κατοικίδια στα πλοία της ακτοπλοΐας", "title_en": "Pet-friendly cabins on coastal ferries", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο ραδιόφωνο για τα ταξίδια με κατοικίδια στα πλοία.",
 "script": [
  L("Εκφωνήτρια", "f", "Από το ερχόμενο καλοκαίρι, δύο ακτοπλοϊκές εταιρείες θα διαθέτουν ειδικές καμπίνες, όπου οι επιβάτες θα μπορούν να ταξιδεύουν μαζί με τον σκύλο ή τη γάτα τους. Μέχρι σήμερα, στα περισσότερα πλοία τα ζώα έπρεπε να μένουν σε κλουβιά στο κατάστρωμα ή σε ειδικούς χώρους, συχνά μέσα στη ζέστη ή στον αέρα.", "From next summer, two ferry companies will offer special cabins where passengers can travel with their dog or cat. Until now, on most ships animals have had to stay in cages on deck or in special areas, often in the heat or the wind."),
  L("Εκφωνήτρια", "f", "Οι νέες καμπίνες θα έχουν δάπεδο που καθαρίζεται εύκολα, μπολ για νερό και φαγητό, και θα καθαρίζονται σχολαστικά μετά από κάθε ταξίδι, ώστε να μπορούν να τις χρησιμοποιούν αργότερα και επιβάτες με αλλεργίες. Οι ιδιοκτήτες θα πρέπει να έχουν μαζί το βιβλιάριο υγείας του ζώου και να το κρατούν με λουρί στους κοινόχρηστους χώρους.", "The new cabins will have easy-to-clean floors, bowls for water and food, and will be cleaned thoroughly after every trip, so that passengers with allergies can use them later too. Owners will need to carry the animal's health booklet and keep it on a lead in the common areas."),
  L("Εκφωνήτρια", "f", "Οι φιλοζωικές οργανώσεις χαιρετίζουν την απόφαση, τονίζοντας ότι κάθε καλοκαίρι πολλά ζώα εγκαταλείπονται επειδή οι ιδιοκτήτες τους δεν μπορούν να τα πάρουν μαζί στις διακοπές. Οι καμπίνες θα κοστίζουν όσο και οι κανονικές, συν ένα μικρό ποσό για τον καθαρισμό.", "Animal welfare groups welcome the decision, stressing that every summer many animals are abandoned because their owners can't take them on holiday. The cabins will cost the same as ordinary ones, plus a small cleaning fee."),
 ],
 "questions": [
  Q("Πού έμεναν μέχρι σήμερα τα ζώα στα περισσότερα πλοία;", ["Στις καμπίνες με τους ιδιοκτήτες", "Σε κλουβιά στο κατάστρωμα ή σε ειδικούς χώρους", "Στο εστιατόριο", "Στο γκαράζ με τα αυτοκίνητα"], 1, "τα ζώα έπρεπε να μένουν σε κλουβιά στο κατάστρωμα ή σε ειδικούς χώρους"),
  Q("Γιατί οι καμπίνες θα καθαρίζονται σχολαστικά μετά από κάθε ταξίδι;", ["Για να μη μυρίζουν", "Για να μπορούν να τις χρησιμοποιούν και επιβάτες με αλλεργίες", "Επειδή το απαιτούν οι κτηνίατροι", "Για να αλλάζουν τα έπιπλα"], 1, "ώστε να μπορούν να τις χρησιμοποιούν αργότερα και επιβάτες με αλλεργίες"),
  Q("Τι πρέπει να έχουν μαζί τους οι ιδιοκτήτες;", ["Ένα πιστοποιητικό εκπαίδευσης", "Το βιβλιάριο υγείας του ζώου", "Ένα κλουβί", "Φαγητό για όλο το ταξίδι"], 1, "θα πρέπει να έχουν μαζί το βιβλιάριο υγείας του ζώου"),
  Q("Γιατί χαιρετίζουν την απόφαση οι φιλοζωικές οργανώσεις;", ["Γιατί θα μειωθούν οι τιμές", "Γιατί κάθε καλοκαίρι πολλά ζώα εγκαταλείπονται", "Γιατί θα δημιουργηθούν νέες θέσεις εργασίας", "Γιατί τα πλοία θα γίνουν πιο γρήγορα"], 1, "κάθε καλοκαίρι πολλά ζώα εγκαταλείπονται επειδή οι ιδιοκτήτες τους δεν μπορούν να τα πάρουν μαζί"),
 ],
 "gloss": {"ακτοπλοϊκές": "ακτοπλοϊκός — coastal shipping (adj.)", "κατάστρωμα": "κατάστρωμα — deck", "σχολαστικά": "σχολαστικά — thoroughly", "βιβλιάριο υγείας": "βιβλιάριο υγείας — health booklet", "λουρί": "λουρί — lead, leash", "κοινόχρηστους": "κοινόχρηστος — common, shared", "φιλοζωικές": "φιλοζωικός — animal welfare (adj.)", "εγκαταλείπονται": "εγκαταλείπω — to abandon"},
})
ITEMS.append({
 "id": "l217-dia-pazari-pylotis", "title": "Ένα παζάρι ανταλλαγής στην πυλωτή", "title_en": "A swap bazaar under the building", "type": "dialogue", "level": "B2",
 "context_el": "Δύο γείτονισσες οργανώνουν ένα παζάρι ανταλλαγής στην πυλωτή της πολυκατοικίας τους.",
 "script": [
  L("Βάσω", "f", "Λοιπόν, Ρένα, ρώτησα όλους τους ενοίκους. Από τα δεκατέσσερα διαμερίσματα, τα έντεκα θέλουν να συμμετάσχουν στο παζάρι. Μόνο ο κύριος του πέμπτου είπε ότι δεν έχει τίποτα περιττό.", "So, Rena, I asked all the tenants. Of the fourteen flats, eleven want to take part in the bazaar. Only the man on the fifth floor said he has nothing he doesn't need."),
  L("Ρένα", "f", "Ο κύριος του πέμπτου; Έχει ένα ολόκληρο μπαλκόνι γεμάτο κούτες! Τέλος πάντων. Σκεφτόμουν να μην πουλάμε τίποτα. Ο καθένας να φέρνει πράγματα και να παίρνει ό,τι του χρειάζεται, χωρίς χρήματα.", "The man on the fifth floor? He's got a whole balcony full of boxes! Anyway. I was thinking we shouldn't sell anything. Everyone brings things and takes whatever they need, without money."),
  L("Βάσω", "f", "Μου αρέσει. Αλλά τι θα κάνουμε με όσα περισσέψουν; Δεν θέλω να μείνουν στην πυλωτή για εβδομάδες και να θυμώσει η διαχειρίστρια.", "I like it. But what do we do with whatever's left over? I don't want it to stay under the building for weeks and make the building manager angry."),
  L("Ρένα", "f", "Τα ρούχα θα τα πάμε στην ενορία, τα βιβλία στη δανειστική βιβλιοθήκη του δημοτικού σχολείου, και ό,τι είναι χαλασμένο θα πάει στην ανακύκλωση την ίδια μέρα. Ο γιος μου έχει ένα βανάκι και θα βοηθήσει.", "We'll take the clothes to the parish, the books to the primary school's lending library, and anything broken will go to recycling the same day. My son has a little van and will help."),
  L("Βάσω", "f", "Τέλεια. Να ορίσουμε ημερομηνία; Τι λες για την Κυριακή στις δεκαεννιά, από τις δέκα ως τη μία; Και να φτιάξω κι ένα κέικ για όσους κατέβουν.", "Perfect. Shall we set a date? How about Sunday the nineteenth, from ten to one? And I'll make a cake for whoever comes down."),
  L("Ρένα", "f", "Ναι! Και να γράψουμε στην αφίσα «Φέρτε και τον καφέ σας». Ίσως έτσι κατέβει και ο κύριος του πέμπτου με τις κούτες του.", "Yes! And let's write on the poster 'Bring your coffee too'. Maybe that way the man on the fifth floor will come down with his boxes."),
 ],
 "questions": [
  Q("Πόσα διαμερίσματα θέλουν να συμμετάσχουν στο παζάρι;", ["Δεκατέσσερα", "Έντεκα", "Πέντε", "Δεκαεννιά"], 1, "Από τα δεκατέσσερα διαμερίσματα, τα έντεκα θέλουν να συμμετάσχουν"),
  Q("Τι προτείνει η Ρένα για τη λειτουργία του παζαριού;", ["Να πουλάνε τα πράγματα φτηνά", "Να φέρνει ο καθένας πράγματα και να παίρνει ό,τι χρειάζεται, χωρίς χρήματα", "Να δοθούν τα έσοδα στη διαχείριση", "Να γίνει δημοπρασία"], 1, "Ο καθένας να φέρνει πράγματα και να παίρνει ό,τι του χρειάζεται, χωρίς χρήματα"),
  Q("Πού θα πάνε τα βιβλία που θα περισσέψουν;", ["Στην ενορία", "Στην ανακύκλωση", "Στη δανειστική βιβλιοθήκη του δημοτικού σχολείου", "Σε ένα παλαιοπωλείο"], 2, "τα βιβλία στη δανειστική βιβλιοθήκη του δημοτικού σχολείου"),
  Q("Τι θα φτιάξει η Βάσω για την ημέρα του παζαριού;", ["Καφέ", "Αφίσες", "Ένα κέικ", "Σάντουιτς"], 2, "να φτιάξω κι ένα κέικ για όσους κατέβουν"),
 ],
 "gloss": {"πυλωτή": "πυλωτή — open ground floor (pilotis) of a block of flats", "ενοίκους": "ένοικος — tenant, resident", "περιττό": "περιττός — unnecessary, superfluous", "κούτες": "κούτα — cardboard box", "περισσέψουν": "περισσεύω — to be left over", "διαχειρίστρια": "διαχειρίστρια — building manager (f.)", "ενορία": "ενορία — parish", "βανάκι": "βαν — van"},
})
ITEMS.append({
 "id": "l217-c1-mono-archaia-mousiki", "title": "Πώς ακουγόταν η αρχαία ελληνική μουσική;", "title_en": "What did ancient Greek music sound like?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια διάλεξη για την αρχαία ελληνική μουσική.",
 "script": [
  L("Ομιλήτρια", "f", "Για τους αρχαίους Έλληνες η μουσική δεν ήταν απλή διασκέδαση. Συνόδευε τη θρησκεία, το θέατρο, τους αθλητικούς αγώνες, ακόμα και την εκπαίδευση των παιδιών. Ο Πλάτων πίστευε ότι οι μουσικοί τρόποι επηρεάζουν τον χαρακτήρα των νέων. Κι όμως, για αιώνες δεν ξέραμε σχεδόν καθόλου πώς ακουγόταν αυτή η μουσική.", "For the ancient Greeks music was not mere entertainment. It accompanied religion, theatre, athletic contests, even the education of children. Plato believed that musical modes affect the character of the young. And yet, for centuries we knew almost nothing of how this music sounded."),
  L("Ομιλήτρια", "f", "Οι αρχαίοι Έλληνες είχαν σύστημα σημειογραφίας: έγραφαν σύμβολα, κυρίως γράμματα του αλφαβήτου, πάνω από τις συλλαβές του κειμένου. Έχουν σωθεί περίπου εξήντα αποσπάσματα, τα περισσότερα σε πάπυρους ή πάνω σε πέτρα. Το πιο διάσημο είναι ο λεγόμενος Επιτάφιος του Σεικίλου, χαραγμένος σε μια μαρμάρινη στήλη που βρέθηκε στη Μικρά Ασία τον 19ο αιώνα. Είναι το αρχαιότερο σωζόμενο ολοκληρωμένο μουσικό κομμάτι με κείμενο και μελωδία.", "The ancient Greeks had a system of notation: they wrote symbols, mainly letters of the alphabet, above the syllables of the text. About sixty fragments survive, most on papyri or on stone. The most famous is the so-called Epitaph of Seikilos, carved on a marble stele found in Asia Minor in the 19th century. It is the oldest surviving complete piece of music with both words and melody."),
  L("Ομιλήτρια", "f", "Η μελωδία είναι μόνο η μισή ιστορία. Για να ζωντανέψει η μουσική, χρειαζόμαστε και τα όργανα. Ο αυλός, για παράδειγμα, δεν ήταν φλογέρα, όπως συχνά μεταφράζεται, αλλά ένα διπλό πνευστό με γλωσσίδι, με ήχο δυνατό και διαπεραστικό. Ερευνητές έχουν κατασκευάσει αντίγραφα με βάση αυλούς που βρέθηκαν σε ανασκαφές, και οι μουσικοί μαθαίνουν ξανά να τους παίζουν.", "The melody is only half the story. To bring music to life, we also need the instruments. The aulos, for instance, was not a flute, as it is often translated, but a double reed wind instrument with a loud, piercing sound. Researchers have built replicas based on auloi found in excavations, and musicians are learning to play them again."),
  L("Ομιλήτρια", "f", "Βέβαια, δεν θα μάθουμε ποτέ με βεβαιότητα πώς τραγουδούσε ένας Αθηναίος τον 5ο αιώνα π.Χ. Ο ρυθμός, όμως, μας δίνει ένα σημαντικό στοιχείο: στα αρχαία ελληνικά οι συλλαβές είχαν μακρά και βραχεία διάρκεια, και αυτή η διάρκεια καθόριζε τον ρυθμό του τραγουδιού. Η γλώσσα δηλαδή ήταν ήδη, κατά κάποιον τρόπο, μουσική.", "Of course, we will never know with certainty how an Athenian sang in the 5th century BC. Rhythm, however, gives us an important clue: in ancient Greek, syllables were long or short, and this length determined the rhythm of the song. The language, in other words, was already, in a sense, music."),
 ],
 "questions": [
  Q("Τι πίστευε ο Πλάτων για τη μουσική;", ["Ότι ήταν μόνο διασκέδαση", "Ότι οι μουσικοί τρόποι επηρεάζουν τον χαρακτήρα των νέων", "Ότι έπρεπε να απαγορευτεί", "Ότι ήταν μόνο για τους θεούς"], 1, "Ο Πλάτων πίστευε ότι οι μουσικοί τρόποι επηρεάζουν τον χαρακτήρα των νέων"),
  Q("Γιατί είναι σημαντικός ο Επιτάφιος του Σεικίλου;", ["Είναι το πρώτο βιβλίο μουσικής", "Είναι το αρχαιότερο σωζόμενο ολοκληρωμένο μουσικό κομμάτι με κείμενο και μελωδία", "Γράφτηκε από τον Πλάτωνα", "Βρέθηκε στην Ακρόπολη"], 1, "Είναι το αρχαιότερο σωζόμενο ολοκληρωμένο μουσικό κομμάτι με κείμενο και μελωδία"),
  Q("Τι ήταν στην πραγματικότητα ο αυλός;", ["Ένα έγχορδο όργανο", "Ένα κρουστό", "Ένα διπλό πνευστό με γλωσσίδι, με δυνατό ήχο", "Μια απλή φλογέρα"], 2, "δεν ήταν φλογέρα ... αλλά ένα διπλό πνευστό με γλωσσίδι"),
  Q("Τι καθόριζε τον ρυθμό του τραγουδιού;", ["Ο τονισμός των λέξεων", "Η μακρά και βραχεία διάρκεια των συλλαβών", "Τα κρουστά όργανα", "Ο χορός"], 1, "οι συλλαβές είχαν μακρά και βραχεία διάρκεια, και αυτή η διάρκεια καθόριζε τον ρυθμό"),
 ],
 "gloss": {"Συνόδευε": "συνοδεύω — to accompany", "μουσικοί τρόποι": "μουσικός τρόπος — (musical) mode", "πάπυρους": "πάπυρος — papyrus", "στήλη": "στήλη — stele, column", "σωζόμενο": "σωζόμενος — surviving, extant", "πνευστό": "πνευστό — wind instrument", "γλωσσίδι": "γλωσσίδι — reed (of an instrument)", "διαπεραστικό": "διαπεραστικός — piercing", "ανασκαφές": "ανασκαφή — excavation"},
})
ITEMS.append({
 "id": "l217-c1-int-geloiografos", "title": "Ένα σκίτσο αξίζει όσο χίλιες λέξεις;", "title_en": "Is a cartoon worth a thousand words? A political cartoonist", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε ραδιοφωνική εκπομπή με μια γελοιογράφο που δημοσιεύει σκίτσα σε εφημερίδα.",
 "script": [
  L("Δημοσιογράφος", "m", "Κάθε πρωί χιλιάδες αναγνώστες ανοίγουν την εφημερίδα πρώτα στη δική σας σελίδα. Πώς γεννιέται ένα σκίτσο;", "Every morning thousands of readers open the paper first at your page. How is a cartoon born?"),
  L("Γελοιογράφος", "f", "Με πολύ διάβασμα και πολύ πέταμα. Διαβάζω τις ειδήσεις από νωρίς το πρωί και σημειώνω ιδέες. Τις περισσότερες τις πετάω, γιατί είναι είτε προβλέψιμες είτε άδικες. Ένα καλό σκίτσο πρέπει να πει κάτι που ο αναγνώστης νιώθει αλλά δεν έχει διατυπώσει. Αν χρειάζεται εξήγηση, έχει αποτύχει.", "With a lot of reading and a lot of throwing away. I read the news from early in the morning and jot down ideas. I throw most of them away, because they're either predictable or unfair. A good cartoon has to say something the reader feels but hasn't put into words. If it needs explaining, it has failed."),
  L("Δημοσιογράφος", "m", "Έχετε δεχτεί ποτέ πιέσεις για κάποιο σκίτσο;", "Have you ever come under pressure over a cartoon?"),
  L("Γελοιογράφος", "f", "Φυσικά. Κάποιοι πολιτικοί έχουν τηλεφωνήσει στην εφημερίδα, κάποιοι αναγνώστες μού στέλνουν θυμωμένα μηνύματα. Αυτό είναι μέρος της δουλειάς. Η σάτιρα υπάρχει από την εποχή του Αριστοφάνη για να ενοχλεί τους ισχυρούς. Έχω όμως έναν προσωπικό κανόνα: δεν κοροϊδεύω ποτέ κάποιον για κάτι που δεν διάλεξε, όπως την εμφάνιση ή την καταγωγή του. Γελάω με ό,τι κάνουμε, όχι με ό,τι είμαστε.", "Of course. Some politicians have rung the newspaper, some readers send me angry messages. That's part of the job. Satire has existed since the time of Aristophanes to annoy the powerful. But I have a personal rule: I never mock someone for something they didn't choose, such as their appearance or origin. I laugh at what we do, not at what we are."),
  L("Δημοσιογράφος", "m", "Τα μέσα κοινωνικής δικτύωσης έχουν αλλάξει τη δουλειά σας;", "Has social media changed your work?"),
  L("Γελοιογράφος", "f", "Πάρα πολύ. Ένα σκίτσο μπορεί να κάνει τον γύρο του κόσμου μέσα σε λίγες ώρες, συχνά χωρίς υπογραφή και χωρίς το πλαίσιο της εφημερίδας. Αυτό είναι και ευκαιρία και κίνδυνος, γιατί κάποιος σε άλλη χώρα μπορεί να το διαβάσει εντελώς διαφορετικά. Γι' αυτό σήμερα σκέφτομαι διπλά πριν τελειώσω ένα σκίτσο, όχι από φόβο, αλλά από σεβασμό στον αναγνώστη που δεν ξέρω.", "Enormously. A cartoon can go round the world in a few hours, often without a signature and without the context of the paper. That's both an opportunity and a risk, because someone in another country may read it completely differently. That's why today I think twice before finishing a cartoon, not out of fear, but out of respect for the reader I don't know."),
 ],
 "questions": [
  Q("Γιατί πετάει τις περισσότερες ιδέες της;", ["Γιατί δεν έχει χρόνο να τις σχεδιάσει", "Γιατί είναι προβλέψιμες ή άδικες", "Γιατί δεν αρέσουν στον διευθυντή", "Γιατί είναι πολύ πολιτικές"], 1, "είναι είτε προβλέψιμες είτε άδικες"),
  Q("Πότε θεωρεί ότι ένα σκίτσο έχει αποτύχει;", ["Όταν προκαλεί θυμό", "Όταν χρειάζεται εξήγηση", "Όταν δεν έχει χρώμα", "Όταν δεν το μοιράζονται στο διαδίκτυο"], 1, "Αν χρειάζεται εξήγηση, έχει αποτύχει"),
  Q("Ποιος είναι ο προσωπικός της κανόνας;", ["Να μη σχεδιάζει ποτέ πολιτικούς", "Να μην κοροϊδεύει κάποιον για κάτι που δεν διάλεξε", "Να μη δέχεται τηλεφωνήματα", "Να μην υπογράφει τα σκίτσα της"], 1, "δεν κοροϊδεύω ποτέ κάποιον για κάτι που δεν διάλεξε"),
  Q("Γιατί σκέφτεται σήμερα διπλά πριν τελειώσει ένα σκίτσο;", ["Από φόβο για τους πολιτικούς", "Από σεβασμό για αναγνώστες που μπορεί να το διαβάσουν αλλιώς", "Γιατί πληρώνεται λιγότερο", "Γιατί η εφημερίδα το απαιτεί"], 1, "όχι από φόβο, αλλά από σεβασμό στον αναγνώστη που δεν ξέρω"),
 ],
 "gloss": {"γελοιογράφο": "γελοιογράφος — cartoonist", "σκίτσο": "σκίτσο — sketch, cartoon", "προβλέψιμες": "προβλέψιμος — predictable", "διατυπώσει": "διατυπώνω — to put into words, formulate", "σάτιρα": "σάτιρα — satire", "κοροϊδεύω": "κοροϊδεύω — to mock, make fun of", "καταγωγή": "καταγωγή — origin, descent", "πλαίσιο": "πλαίσιο — context; frame"},
})
rnd = random.Random(217)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-217.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
