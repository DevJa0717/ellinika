# Source for library/listening/listening-144.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l144.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l144-vm-sxoleio-pyretos", "title": "Ο μικρός έχει πυρετό", "title_en": "Your son has a temperature", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα από το σχολείο του γιου σας στον τηλεφωνητή σας.",
 "script": [
  L("Γραμματέας", "f", "Καλημέρα σας, από το Τρίτο Δημοτικό Σχολείο σας τηλεφωνώ, για τον Άγγελο της Δ΄ τάξης. Μετά το δεύτερο διάλειμμα είπε στη δασκάλα του ότι πονάει το κεφάλι του, και η νοσηλεύτρια του σχολείου τού μέτρησε τριάντα οχτώ και τρία.", "Good morning, I'm calling from the Third Primary School, about Angelos in year four. After the second break he told his teacher that he had a headache, and the school nurse measured thirty-eight point three."),
  L("Γραμματέας", "f", "Τώρα ξαπλώνει στο ιατρείο και είναι ήρεμος, αλλά σύμφωνα με τον κανονισμό πρέπει να έρθει κάποιος να τον πάρει. Αν δεν μπορείτε εσείς, μπορεί να τον πάρει ένα από τα άτομα που έχετε δηλώσει στην αρχή της χρονιάς, αρκεί να έχει μαζί του ταυτότητα.", "He's lying down in the sick room now and he's calm, but according to the rules someone has to come and collect him. If you can't, one of the people you registered at the start of the year can collect him, as long as they bring ID."),
  L("Γραμματέας", "f", "Επίσης, για να επιστρέψει στο σχολείο, πρέπει να μην έχει πυρετό για τουλάχιστον είκοσι τέσσερις ώρες. Ευχαριστώ.", "Also, to return to school, he must have had no fever for at least twenty-four hours. Thank you."),
 ],
 "questions": [
  Q("Τι συνέβη στον Άγγελο;", ["Χτύπησε στο διάλειμμα", "Πονούσε το κεφάλι του και είχε πυρετό", "Τσακώθηκε με έναν συμμαθητή του", "Ξέχασε το φαγητό του"], 1, "είπε στη δασκάλα του ότι πονάει το κεφάλι του"),
  Q("Ποιος μπορεί να τον πάρει, αν δεν μπορείτε εσείς;", ["Οποιοσδήποτε ενήλικας", "Ένας συμμαθητής του", "Ένα από τα άτομα που έχετε δηλώσει, με ταυτότητα", "Κανείς άλλος"], 2, "μπορεί να τον πάρει ένα από τα άτομα που έχετε δηλώσει"),
  Q("Πότε μπορεί να επιστρέψει στο σχολείο;", ["Όταν δεν έχει πυρετό για τουλάχιστον είκοσι τέσσερις ώρες", "Αύριο το πρωί", "Μετά από μία εβδομάδα", "Μόνο με χαρτί από γιατρό"], 0, "πρέπει να μην έχει πυρετό για τουλάχιστον είκοσι τέσσερις ώρες"),
 ],
 "gloss": {"διάλειμμα": "διάλειμμα — break", "νοσηλεύτρια": "νοσηλεύτρια — nurse", "μέτρησε": "μετράω — to measure", "ξαπλώνει": "ξαπλώνω — to lie down", "ιατρείο": "ιατρείο — sick room, surgery", "κανονισμό": "κανονισμός — regulation", "δηλώσει": "δηλώνω — to register, declare", "ταυτότητα": "ταυτότητα — ID card", "πυρετό": "πυρετός — fever"}
})

ITEMS.append({
 "id": "l144-ann-monastiri", "title": "Πριν μπούμε στο μοναστήρι", "title_en": "Before we enter the monastery", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα πούλμαν με μια ομάδα τουριστών. Ακούτε τη συνοδό να κάνει μια ανακοίνωση.",
 "script": [
  L("Συνοδός", "f", "Σε πέντε λεπτά φτάνουμε στο μοναστήρι. Πριν κατεβείτε, λίγες πληροφορίες. Το μοναστήρι είναι ανοιχτό για επισκέπτες μέχρι τη μία το μεσημέρι, οπότε θα έχουμε στη διάθεσή μας περίπου μία ώρα.", "In five minutes we arrive at the monastery. Before you get off, some information. The monastery is open to visitors until one in the afternoon, so we'll have about an hour."),
  L("Συνοδός", "f", "Οι κυρίες πρέπει να φορούν φούστα κάτω από το γόνατο και να έχουν καλυμμένους τους ώμους, και οι κύριοι μακρύ παντελόνι. Όσοι φοράτε σορτς μην ανησυχείτε: στην είσοδο δανείζουν δωρεάν φούστες και μαντίλια.", "Ladies must wear a skirt below the knee and have their shoulders covered, and gentlemen long trousers. Those of you in shorts, don't worry: at the entrance they lend skirts and shawls free of charge."),
  L("Συνοδός", "f", "Μέσα στο καθολικό απαγορεύονται οι φωτογραφίες, και σας παρακαλώ να μιλάτε χαμηλόφωνα, γιατί οι μοναχοί ζουν εκεί. Στη μία και τέταρτο ακριβώς θα σας περιμένω εδώ, στο πούλμαν.", "Inside the main church photographs are forbidden, and please speak quietly, because the monks live there. At a quarter past one exactly I'll be waiting for you here, at the coach."),
 ],
 "questions": [
  Q("Πόσο χρόνο θα έχουν στο μοναστήρι;", ["Περίπου μία ώρα", "Δύο ώρες", "Μισή ώρα", "Όλο το απόγευμα"], 0, "θα έχουμε στη διάθεσή μας περίπου μία ώρα"),
  Q("Τι γίνεται με όσους φορούν σορτς;", ["Δεν μπορούν να μπουν", "Πρέπει να αγοράσουν ρούχα", "Μπορούν να δανειστούν δωρεάν φούστες και μαντίλια στην είσοδο", "Μένουν στο πούλμαν"], 2, "στην είσοδο δανείζουν δωρεάν φούστες και μαντίλια"),
  Q("Τι απαγορεύεται μέσα στο καθολικό;", ["Να ανάβουν κεριά", "Οι φωτογραφίες", "Να μπαίνουν παιδιά", "Να κάθονται"], 1, "Μέσα στο καθολικό απαγορεύονται οι φωτογραφίες"),
 ],
 "gloss": {"πούλμαν": "πούλμαν — coach", "συνοδό": "συνοδός — tour guide, escort", "στη διάθεσή μας": "στη διάθεσή μας — at our disposal", "καλυμμένους": "καλυμμένος — covered", "ώμους": "ώμος — shoulder", "μαντίλια": "μαντίλι — shawl, headscarf", "καθολικό": "καθολικό — main church of a monastery", "χαμηλόφωνα": "χαμηλόφωνα — quietly", "μοναχοί": "μοναχός — monk"}
})

ITEMS.append({
 "id": "l144-dia-ektypotis", "title": "Ο εκτυπωτής χάλασε ξανά", "title_en": "The printer broke again", "type": "dialogue", "level": "B2",
 "context_el": "Δύο συνάδελφοι συζητούν στο γραφείο.",
 "script": [
  L("Στέλλα", "f", "Ο εκτυπωτής πάλι μπλοκάρει το χαρτί. Τρίτη φορά αυτή την εβδομάδα! Και πρέπει να τυπώσω τις προσφορές για τη συνάντηση των δέκα.", "The printer's jamming the paper again. Third time this week! And I have to print the quotes for the ten o'clock meeting."),
  L("Νίκος", "m", "Τον έχουμε οχτώ χρόνια, είναι πια για πέταμα. Είπα στον διευθυντή να πάρουμε καινούργιο, αλλά θέλει πρώτα τρεις προσφορές από διαφορετικά καταστήματα.", "We've had it eight years, it's ready for the bin now. I told the manager we should get a new one, but he first wants three quotes from different shops."),
  L("Στέλλα", "f", "Θα τις βρω εγώ σήμερα το απόγευμα. Αλλά για τώρα τι κάνουμε;", "I'll find them this afternoon. But what do we do for now?"),
  L("Νίκος", "m", "Το λογιστήριο στον δεύτερο όροφο έχει έναν που δουλεύει μια χαρά. Στείλ' τους το αρχείο με email και ανέβα να το πάρεις. Μόνο μην ξεχάσεις να πάρεις μαζί σου και δικό μας χαρτί, γιατί την προηγούμενη φορά μάς παραπονέθηκαν.", "Accounts on the second floor have one that works fine. Email them the file and go up and get it. Just don't forget to take some of our paper with you, because last time they complained to us."),
 ],
 "questions": [
  Q("Τι πρόβλημα έχει ο εκτυπωτής;", ["Δεν έχει μελάνι", "Μπλοκάρει το χαρτί", "Δεν συνδέεται στο δίκτυο", "Τυπώνει πολύ αργά"], 1, "Ο εκτυπωτής πάλι μπλοκάρει το χαρτί"),
  Q("Τι θέλει ο διευθυντής πριν αγοράσει καινούργιο εκτυπωτή;", ["Να τον επισκευάσουν πρώτα", "Να περιμένουν μέχρι τον Ιανουάριο", "Τρεις προσφορές από διαφορετικά καταστήματα", "Να τον αγοράσουν μαζί με το λογιστήριο"], 2, "θέλει πρώτα τρεις προσφορές από διαφορετικά καταστήματα"),
  Q("Τι πρέπει να μην ξεχάσει η Στέλλα;", ["Να πάρει μαζί της δικό τους χαρτί", "Να ενημερώσει τον διευθυντή", "Να κλείσει τον εκτυπωτή", "Να τυπώσει δύο αντίγραφα"], 0, "μην ξεχάσεις να πάρεις μαζί σου και δικό μας χαρτί"),
 ],
 "gloss": {"εκτυπωτής": "εκτυπωτής — printer", "μπλοκάρει": "μπλοκάρω — to jam", "τυπώσω": "τυπώνω — to print", "προσφορές": "προσφορά — quote, offer", "για πέταμα": "για πέταμα — fit for the bin", "λογιστήριο": "λογιστήριο — accounts department", "αρχείο": "αρχείο — file", "παραπονέθηκαν": "παραπονιέμαι — to complain"}
})

ITEMS.append({
 "id": "l144-int-tsopanoskyla", "title": "Ο εκπαιδευτής των τσοπανόσκυλων", "title_en": "The sheepdog trainer", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από μια ραδιοφωνική εκπομπή για την ύπαιθρο.",
 "script": [
  L("Δημοσιογράφος", "f", "Εκπαιδεύετε σκυλιά που προστατεύουν τα κοπάδια από τους λύκους και τις αρκούδες. Πώς ξεκινά αυτή η εκπαίδευση;", "You train dogs that protect flocks from wolves and bears. How does this training begin?"),
  L("Εκπαιδευτής", "m", "Ξεκινά πολύ νωρίς, όταν το κουτάβι είναι έξι με οχτώ εβδομάδων. Το βάζουμε να μεγαλώσει μέσα στο κοπάδι, ανάμεσα στα πρόβατα, όχι στο σπίτι. Έτσι θεωρεί τα πρόβατα οικογένειά του και τα υπερασπίζεται σαν να ήταν αδέλφια του.", "It starts very early, when the puppy is six to eight weeks old. We let it grow up inside the flock, among the sheep, not in the house. That way it considers the sheep its family and defends them as if they were its siblings."),
  L("Δημοσιογράφος", "f", "Και επιτίθεται στον λύκο;", "And does it attack the wolf?"),
  L("Εκπαιδευτής", "m", "Σπάνια. Ένα καλό τσοπανόσκυλο γαβγίζει και στέκεται ανάμεσα στον λύκο και στο κοπάδι. Τις περισσότερες φορές αυτό αρκεί. Το πρόβλημα είναι ότι οι πεζοπόροι δεν το ξέρουν και πλησιάζουν τα πρόβατα. Η συμβουλή μου είναι απλή: σταματήστε, μην τρέξετε, μην κοιτάτε τον σκύλο στα μάτια, και απομακρυνθείτε αργά από το κοπάδι. Ο σκύλος κάνει απλώς τη δουλειά του.", "Rarely. A good sheepdog barks and stands between the wolf and the flock. Most of the time that's enough. The problem is that hikers don't know this and approach the sheep. My advice is simple: stop, don't run, don't look the dog in the eye, and move slowly away from the flock. The dog is simply doing its job."),
 ],
 "questions": [
  Q("Πού μεγαλώνει το κουτάβι;", ["Στο σπίτι του βοσκού", "Μέσα στο κοπάδι, ανάμεσα στα πρόβατα", "Σε ένα ειδικό κέντρο", "Με άλλα σκυλιά"], 1, "Το βάζουμε να μεγαλώσει μέσα στο κοπάδι, ανάμεσα στα πρόβατα"),
  Q("Τι κάνει συνήθως ένα καλό τσοπανόσκυλο όταν έρθει λύκος;", ["Επιτίθεται αμέσως", "Τρέχει να ειδοποιήσει τον βοσκό", "Κρύβεται", "Γαβγίζει και στέκεται ανάμεσα στον λύκο και στο κοπάδι"], 3, "γαβγίζει και στέκεται ανάμεσα στον λύκο και στο κοπάδι"),
  Q("Τι συμβουλεύει τους πεζοπόρους;", ["Να τρέξουν μακριά", "Να δώσουν φαγητό στον σκύλο", "Να σταματήσουν και να απομακρυνθούν αργά από το κοπάδι", "Να φωνάξουν δυνατά"], 2, "απομακρυνθείτε αργά από το κοπάδι"),
 ],
 "gloss": {"τσοπανόσκυλο": "τσοπανόσκυλο — sheepdog", "κοπάδια": "κοπάδι — flock", "λύκους": "λύκος — wolf", "αρκούδες": "αρκούδα — bear", "κουτάβι": "κουτάβι — puppy", "πρόβατα": "πρόβατο — sheep", "υπερασπίζεται": "υπερασπίζομαι — to defend", "γαβγίζει": "γαβγίζω — to bark", "πεζοπόροι": "πεζοπόρος — hiker", "απομακρυνθείτε": "απομακρύνομαι — to move away"}
})

ITEMS.append({
 "id": "l144-news-ptyxio", "title": "Πτυχίο στα ογδόντα οχτώ", "title_en": "A degree at eighty-eight", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων.",
 "script": [
  L("Εκφωνητής", "m", "Με χειροκροτήματα που κράτησαν πάνω από ένα λεπτό ολοκληρώθηκε χθες η τελετή ορκωμοσίας στο Τμήμα Ιστορίας ενός πανεπιστημίου της βόρειας Ελλάδας. Ο λόγος: ανάμεσα στους απόφοιτους ήταν και μια γιαγιά ογδόντα οχτώ ετών.", "Applause that lasted more than a minute ended yesterday's graduation ceremony at the History Department of a university in northern Greece. The reason: among the graduates was an eighty-eight-year-old grandmother."),
  L("Εκφωνητής", "m", "Η κυρία Ευτέρπη αναγκάστηκε να σταματήσει το σχολείο στα δεκατρία της, για να δουλέψει στα χωράφια. Τελείωσε το λύκειο σε ένα σχολείο για ενήλικες στα εβδομήντα εννιά της και πέρασε στο πανεπιστήμιο με ειδικές εξετάσεις. Τα τελευταία χρόνια ο εγγονός της την πήγαινε με το αυτοκίνητο στις παραδόσεις.", "Mrs Efterpi was forced to leave school at thirteen to work in the fields. She finished secondary school at an adult school at seventy-nine and got into university through special exams. In recent years her grandson drove her to lectures."),
  L("Εκφωνητής", "m", "«Δεν το έκανα για το χαρτί», είπε στους δημοσιογράφους. «Το έκανα για να καταλάβω επιτέλους την ιστορία που έζησα.» Τώρα σκέφτεται να γράψει τις αναμνήσεις της από τον πόλεμο.", "'I didn't do it for the certificate,' she told reporters. 'I did it to finally understand the history I lived through.' Now she is thinking of writing her memories of the war."),
 ],
 "questions": [
  Q("Γιατί σταμάτησε το σχολείο στα δεκατρία της;", ["Για να δουλέψει στα χωράφια", "Γιατί παντρεύτηκε", "Γιατί μετακόμισαν", "Γιατί αρρώστησε"], 0, "για να δουλέψει στα χωράφια"),
  Q("Πώς πήγαινε στις παραδόσεις τα τελευταία χρόνια;", ["Με το λεωφορείο", "Την πήγαινε ο εγγονός της με το αυτοκίνητο", "Με ταξί", "Τις παρακολουθούσε από το διαδίκτυο"], 1, "ο εγγονός της την πήγαινε με το αυτοκίνητο στις παραδόσεις"),
  Q("Γιατί, όπως είπε, σπούδασε;", ["Για να βρει δουλειά", "Για να κάνει χαρά στην οικογένειά της", "Για να καταλάβει την ιστορία που έζησε", "Για να γίνει δασκάλα"], 2, "για να καταλάβω επιτέλους την ιστορία που έζησα"),
 ],
 "gloss": {"χειροκροτήματα": "χειροκρότημα — applause", "τελετή ορκωμοσίας": "τελετή ορκωμοσίας — graduation ceremony", "απόφοιτους": "απόφοιτος — graduate", "αναγκάστηκε": "αναγκάζομαι — to be forced", "χωράφια": "χωράφι — field", "λύκειο": "λύκειο — upper secondary school", "ενήλικες": "ενήλικας — adult", "παραδόσεις": "παράδοση — lecture", "αναμνήσεις": "ανάμνηση — memory"}
})

ITEMS.append({
 "id": "l144-mon-mikrofilm", "title": "Πώς ψάχνουμε σε παλιές εφημερίδες", "title_en": "How to search old newspapers", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια υπάλληλο σε μια βιβλιοθήκη να μιλά σε μια ομάδα φοιτητών.",
 "script": [
  L("Βιβλιοθηκονόμος", "f", "Καλώς ήρθατε στο τμήμα εφημερίδων. Εδώ έχουμε όλες τις μεγάλες εφημερίδες της Αθήνας από το 1900 και μετά. Τα πρωτότυπα φύλλα είναι πολύ εύθραυστα, γι' αυτό δεν τα δίνουμε στο κοινό. Τα περισσότερα έχουν φωτογραφηθεί σε μικροφίλμ.", "Welcome to the newspaper section. Here we have all the major Athens newspapers from 1900 onwards. The original issues are very fragile, so we don't give them to the public. Most have been photographed on microfilm."),
  L("Βιβλιοθηκονόμος", "f", "Για να βρείτε αυτό που ψάχνετε, πρέπει να ξέρετε τουλάχιστον τον μήνα και τη χρονιά. Συμπληρώνετε ένα δελτίο με την εφημερίδα και την ημερομηνία, και σε δέκα λεπτά περίπου σας φέρνουμε το καρούλι. Οι συσκευές ανάγνωσης είναι εκεί, δίπλα στο παράθυρο.", "To find what you're looking for, you need to know at least the month and the year. You fill in a slip with the newspaper and the date, and in about ten minutes we bring you the reel. The readers are over there, by the window."),
  L("Βιβλιοθηκονόμος", "f", "Μπορείτε να τυπώσετε σελίδες με δέκα λεπτά τη σελίδα, ή να τις αποθηκεύσετε σε στικάκι δωρεάν. Τις εφημερίδες μέχρι το 1950 θα τις βρείτε και ψηφιοποιημένες στην ιστοσελίδα μας, οπότε μπορείτε να τις διαβάζετε και από το σπίτι.", "You can print pages for ten cents a page, or save them to a USB stick for free. Newspapers up to 1950 you'll also find digitised on our website, so you can read them from home too."),
 ],
 "questions": [
  Q("Γιατί δεν δίνουν τα πρωτότυπα φύλλα στο κοινό;", ["Γιατί είναι πολύ εύθραυστα", "Γιατί είναι πολύ ακριβά", "Γιατί λείπουν πολλά", "Γιατί είναι σε άλλο κτίριο"], 0, "Τα πρωτότυπα φύλλα είναι πολύ εύθραυστα"),
  Q("Τι πρέπει να ξέρει κανείς για να βρει ένα άρθρο;", ["Τον τίτλο του άρθρου", "Τουλάχιστον τον μήνα και τη χρονιά", "Το όνομα του δημοσιογράφου", "Τη σελίδα"], 1, "πρέπει να ξέρετε τουλάχιστον τον μήνα και τη χρονιά"),
  Q("Τι ισχύει για τις εφημερίδες μέχρι το 1950;", ["Δεν υπάρχουν πια", "Μπορούν να δανειστούν", "Υπάρχουν ψηφιοποιημένες στην ιστοσελίδα της βιβλιοθήκης", "Υπάρχουν μόνο σε πρωτότυπο"], 2, "Τις εφημερίδες μέχρι το 1950 θα τις βρείτε και ψηφιοποιημένες στην ιστοσελίδα μας"),
 ],
 "gloss": {"πρωτότυπα": "πρωτότυπος — original", "φύλλα": "φύλλο — issue (of a newspaper)", "εύθραυστα": "εύθραυστος — fragile", "μικροφίλμ": "μικροφίλμ — microfilm", "δελτίο": "δελτίο — slip, form", "καρούλι": "καρούλι — reel", "συσκευές ανάγνωσης": "συσκευή ανάγνωσης — (microfilm) reader", "αποθηκεύσετε": "αποθηκεύω — to save", "στικάκι": "στικάκι — USB stick", "ψηφιοποιημένες": "ψηφιοποιημένος — digitised"}
})

ITEMS.append({
 "id": "l144-rep-diplomata", "title": "Λιγότεροι νέοι στο τιμόνι", "title_en": "Fewer young people behind the wheel", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια ενημερωτική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "m", "Πριν από είκοσι χρόνια, σχεδόν κάθε δεκαοχτάχρονος στην Ελλάδα έσπευδε να βγάλει δίπλωμα οδήγησης. Σήμερα, σύμφωνα με στοιχεία των σχολών οδηγών, οι νέοι που δίνουν εξετάσεις πριν από τα είκοσι πέντε είναι σχεδόν οι μισοί.", "Twenty years ago, almost every eighteen-year-old in Greece rushed to get a driving licence. Today, according to figures from driving schools, the young people who take the test before twenty-five are almost half as many."),
  L("Ρεπόρτερ", "m", "Ο πρώτος λόγος είναι το κόστος: τα μαθήματα και τα παράβολα ξεπερνούν συχνά τα οχτακόσια ευρώ, για να μην πούμε για την αγορά και την ασφάλιση ενός αυτοκινήτου. Πολλοί νέοι όμως λένε ότι απλώς δεν το χρειάζονται, αφού στις μεγάλες πόλεις μετακινούνται με το μετρό, με ποδήλατο ή με εφαρμογές για ταξί.", "The first reason is cost: lessons and fees often exceed eight hundred euros, not to mention buying and insuring a car. But many young people say they simply don't need it, since in big cities they get around by metro, by bike or with taxi apps."),
  L("Ρεπόρτερ", "m", "Στην επαρχία η εικόνα είναι διαφορετική. Εκεί, χωρίς αυτοκίνητο, η δουλειά και η διασκέδαση γίνονται δύσκολες, και το δίπλωμα παραμένει, όπως λένε, «το πρώτο διαβατήριο για την ανεξαρτησία».", "In the provinces the picture is different. There, without a car, work and going out become difficult, and the licence remains, as they say, 'the first passport to independence'."),
 ],
 "questions": [
  Q("Τι έχει αλλάξει σε σχέση με πριν από είκοσι χρόνια;", ["Οι νέοι βγάζουν δίπλωμα νωρίτερα", "Οι νέοι που δίνουν εξετάσεις πριν από τα είκοσι πέντε είναι σχεδόν οι μισοί", "Οι εξετάσεις έγιναν πιο εύκολες", "Οι σχολές οδηγών έκλεισαν"], 1, "οι νέοι που δίνουν εξετάσεις πριν από τα είκοσι πέντε είναι σχεδόν οι μισοί"),
  Q("Ποιον δεύτερο λόγο αναφέρουν πολλοί νέοι;", ["Ότι φοβούνται να οδηγήσουν", "Ότι οι εξετάσεις είναι δύσκολες", "Ότι απλώς δεν το χρειάζονται", "Ότι δεν τους αρέσουν τα αυτοκίνητα"], 2, "Πολλοί νέοι όμως λένε ότι απλώς δεν το χρειάζονται"),
  Q("Τι ισχύει στην επαρχία;", ["Το δίπλωμα παραμένει πολύ σημαντικό", "Οι νέοι προτιμούν το ποδήλατο", "Υπάρχουν πολλές συγκοινωνίες", "Τα μαθήματα είναι φτηνότερα"], 0, "το δίπλωμα παραμένει"),
 ],
 "gloss": {"έσπευδε": "σπεύδω — to hasten, rush", "δίπλωμα οδήγησης": "δίπλωμα οδήγησης — driving licence", "στοιχεία": "στοιχεία — figures, data", "παράβολα": "παράβολο — (official) fee", "ασφάλιση": "ασφάλιση — insurance", "μετακινούνται": "μετακινούμαι — to get around", "επαρχία": "επαρχία — the provinces", "ανεξαρτησία": "ανεξαρτησία — independence"}
})

ITEMS.append({
 "id": "l144-dia-stroma", "title": "Ένα καινούργιο στρώμα", "title_en": "A new mattress", "type": "dialogue", "level": "B2",
 "context_el": "Μια πελάτισσα βρίσκεται σε ένα κατάστημα με στρώματα.",
 "script": [
  L("Πελάτισσα", "f", "Καλησπέρα. Ψάχνω ένα διπλό στρώμα. Ξυπνάω κάθε πρωί με πόνο στη μέση, και ο γιατρός μου είπε ότι το δικό μου είναι πολύ μαλακό.", "Good evening. I'm looking for a double mattress. I wake up every morning with back pain, and my doctor told me mine is too soft."),
  L("Πωλητής", "m", "Τότε σας προτείνω ένα από αυτά τα ορθοπεδικά, με ανεξάρτητα ελατήρια. Είναι πιο σκληρά, αλλά προσαρμόζονται στο σώμα. Ξαπλώστε πρώτα για πέντε λεπτά, στο πλάι, όπως κοιμάστε. Δεν αποφασίζει κανείς για ένα στρώμα σε δέκα δευτερόλεπτα.", "Then I suggest one of these orthopaedic ones, with independent springs. They're firmer, but they adapt to the body. Lie down first for five minutes, on your side, the way you sleep. Nobody decides on a mattress in ten seconds."),
  L("Πελάτισσα", "f", "Είναι πολύ άνετο. Αν όμως το πάρω και δεν μου κάνει;", "It's very comfortable. But what if I buy it and it doesn't suit me?"),
  L("Πωλητής", "m", "Έχετε εκατό νύχτες δοκιμή. Αν δεν είστε ευχαριστημένη, το αλλάζετε με άλλο, χωρίς χρέωση. Τη μεταφορά και την παραλαβή του παλιού σας στρώματος τις κάνουμε δωρεάν, αλλά για την ανακύκλωσή του υπάρχει μια μικρή χρέωση, δεκαπέντε ευρώ.", "You have a hundred nights' trial. If you're not satisfied, you exchange it for another one at no charge. Delivery and collection of your old mattress we do free, but there's a small charge for recycling it, fifteen euros."),
 ],
 "questions": [
  Q("Γιατί θέλει καινούργιο στρώμα;", ["Γιατί μετακομίζει", "Γιατί ξυπνά με πόνο στη μέση και το δικό της είναι πολύ μαλακό", "Γιατί το παλιό χάλασε", "Γιατί παντρεύεται"], 1, "Ξυπνάω κάθε πρωί με πόνο στη μέση"),
  Q("Τι της προτείνει να κάνει ο πωλητής;", ["Να ξαπλώσει για πέντε λεπτά, στο πλάι, όπως κοιμάται", "Να το πάρει αμέσως", "Να ρωτήσει πρώτα τον γιατρό", "Να επιστρέψει άλλη μέρα"], 0, "Ξαπλώστε πρώτα για πέντε λεπτά, στο πλάι, όπως κοιμάστε"),
  Q("Για ποιο πράγμα υπάρχει χρέωση;", ["Για τη μεταφορά", "Για την αλλαγή του στρώματος", "Για την παραλαβή του παλιού στρώματος", "Για την ανακύκλωση του παλιού στρώματος"], 3, "για την ανακύκλωσή του υπάρχει μια μικρή χρέωση"),
 ],
 "gloss": {"στρώμα": "στρώμα — mattress", "μέση": "μέση — lower back", "μαλακό": "μαλακός — soft", "ορθοπεδικά": "ορθοπεδικός — orthopaedic", "ελατήρια": "ελατήριο — spring", "προσαρμόζονται": "προσαρμόζομαι — to adapt", "άνετο": "άνετος — comfortable", "δοκιμή": "δοκιμή — trial", "παραλαβή": "παραλαβή — collection", "ανακύκλωσή": "ανακύκλωση — recycling"}
})

ITEMS.append({
 "id": "l144-c1-brooks", "title": "Ο νόμος του Μπρουκς", "title_en": "Brooks's law", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια ομιλία σε ένα συνέδριο για τη διοίκηση έργων.",
 "script": [
  L("Ομιλητής", "m", "Το 1975 ο Αμερικανός μηχανικός λογισμικού Φρεντ Μπρουκς, που είχε διευθύνει στην IBM την ανάπτυξη ενός από τα μεγαλύτερα λειτουργικά συστήματα της εποχής, δημοσίευσε ένα βιβλίο με τίτλο «Ο μυθικός ανθρωπομήνας». Εκεί διατύπωσε μια φράση που έμεινε γνωστή ως νόμος του Μπρουκς: αν προσθέσεις ανθρώπους σε ένα έργο λογισμικού που έχει ήδη καθυστερήσει, θα καθυστερήσει ακόμα περισσότερο.", "In 1975 the American software engineer Fred Brooks, who had led the development at IBM of one of the largest operating systems of the time, published a book titled 'The Mythical Man-Month'. There he formulated a sentence that became known as Brooks's law: adding people to a software project that is already late will make it later."),
  L("Ομιλητής", "m", "Οι λόγοι είναι δύο. Ο πρώτος είναι ότι οι νεοφερμένοι χρειάζονται χρόνο για να μάθουν το έργο, και αυτόν τον χρόνο τον αφαιρούν από τους έμπειρους, που πρέπει να τους εκπαιδεύσουν. Ο δεύτερος είναι πιο ύπουλος: κάθε νέο μέλος πολλαπλασιάζει τους διαύλους επικοινωνίας. Σε μια ομάδα πέντε ατόμων υπάρχουν δέκα πιθανά ζευγάρια που πρέπει να συνεννοηθούν· σε μια ομάδα είκοσι, εκατόν ενενήντα.", "There are two reasons. The first is that newcomers need time to learn the project, and they take that time from the experienced people, who have to train them. The second is more insidious: every new member multiplies the channels of communication. In a team of five there are ten possible pairs who have to coordinate; in a team of twenty, a hundred and ninety."),
  L("Ομιλητής", "m", "Ο ίδιος ο Μπρουκς παραδεχόταν ότι ο νόμος του είναι μια «εξωφρενική απλούστευση». Αν η προσθήκη γίνει νωρίς, ή αν οι εργασίες μπορούν να μοιραστούν εύκολα, οι νέοι άνθρωποι βοηθούν. Το βασικό του μάθημα όμως παραμένει επίκαιρο: ο ανθρωπομήνας είναι μύθος, γιατί οι άνθρωποι και οι μήνες δεν είναι ανταλλάξιμοι. Όπως έγραφε χαρακτηριστικά, εννιά γυναίκες δεν μπορούν να φέρουν στον κόσμο ένα παιδί σε έναν μήνα.", "Brooks himself admitted that his law is an 'outrageous oversimplification'. If people are added early, or if the tasks can be divided easily, the new people help. But his basic lesson remains relevant: the man-month is a myth, because people and months are not interchangeable. As he memorably wrote, nine women cannot bring a child into the world in one month."),
 ],
 "questions": [
  Q("Τι λέει ο νόμος του Μπρουκς;", ["Ότι τα μεγάλα έργα αποτυγχάνουν πάντα", "Ότι αν προσθέσεις ανθρώπους σε ένα έργο που έχει καθυστερήσει, θα καθυστερήσει ακόμα περισσότερο", "Ότι οι μικρές ομάδες δεν τελειώνουν ποτέ", "Ότι το λογισμικό πρέπει να γράφεται από έναν άνθρωπο"], 1, "θα καθυστερήσει ακόμα περισσότερο"),
  Q("Ποιος είναι ο πρώτος λόγος;", ["Οι νεοφερμένοι χρειάζονται χρόνο για να μάθουν το έργο, και τον αφαιρούν από τους έμπειρους", "Οι νεοφερμένοι είναι λιγότερο ικανοί", "Οι υπολογιστές δεν φτάνουν", "Οι μισθοί αυξάνονται"], 0, "οι νεοφερμένοι χρειάζονται χρόνο για να μάθουν το έργο"),
  Q("Τι συμβαίνει με τους διαύλους επικοινωνίας όταν μεγαλώνει η ομάδα;", ["Μειώνονται", "Μένουν ίδιοι", "Πολλαπλασιάζονται", "Γίνονται πιο απλοί"], 2, "κάθε νέο μέλος πολλαπλασιάζει τους διαύλους επικοινωνίας"),
  Q("Τι θέλει να δείξει το παράδειγμα με τις εννιά γυναίκες;", ["Ότι οι γυναίκες δουλεύουν καλύτερα σε ομάδες", "Ότι τα έργα πρέπει να διαρκούν εννιά μήνες", "Ότι η ομάδα πρέπει να έχει εννιά μέλη", "Ότι οι άνθρωποι και οι μήνες δεν είναι ανταλλάξιμοι"], 3, "οι άνθρωποι και οι μήνες δεν είναι ανταλλάξιμοι"),
 ],
 "gloss": {"διοίκηση έργων": "διοίκηση έργων — project management", "λογισμικού": "λογισμικό — software", "λειτουργικά συστήματα": "λειτουργικό σύστημα — operating system", "ανθρωπομήνας": "ανθρωπομήνας — man-month", "νεοφερμένοι": "νεοφερμένος — newcomer", "ύπουλος": "ύπουλος — insidious", "διαύλους": "δίαυλος — channel", "συνεννοηθούν": "συνεννοούμαι — to coordinate, communicate", "εξωφρενική": "εξωφρενικός — outrageous", "απλούστευση": "απλούστευση — oversimplification", "ανταλλάξιμοι": "ανταλλάξιμος — interchangeable"}
})

ITEMS.append({
 "id": "l144-c1-mandela", "title": "Το «φαινόμενο Μαντέλα»", "title_en": "The Mandela effect", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκπομπή για την ψυχολογία.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι είναι αυτό που στο διαδίκτυο ονομάζουν «φαινόμενο Μαντέλα»;", "What is the thing they call the 'Mandela effect' online?"),
  L("Ψυχολόγος", "m", "Ο όρος επινοήθηκε γύρω στο 2010 από μια Αμερικανίδα συγγραφέα, η οποία ανακάλυψε ότι πολλοί άνθρωποι, όπως κι εκείνη, «θυμούνταν» ότι ο Νέλσον Μαντέλα είχε πεθάνει στη φυλακή τη δεκαετία του 1980. Στην πραγματικότητα ο Μαντέλα αποφυλακίστηκε το 1990, έγινε πρόεδρος της Νότιας Αφρικής και πέθανε το 2013. Από τότε ο όρος χρησιμοποιείται για κάθε ψευδή ανάμνηση που μοιράζονται πολλοί άνθρωποι ταυτόχρονα.", "The term was coined around 2010 by an American writer, who discovered that many people, like her, 'remembered' that Nelson Mandela had died in prison in the 1980s. In reality Mandela was released from prison in 1990, became president of South Africa and died in 2013. Since then the term has been used for any false memory shared by many people at the same time."),
  L("Δημοσιογράφος", "f", "Κάποιοι στο διαδίκτυο το εξηγούν με παράλληλα σύμπαντα...", "Some people online explain it with parallel universes..."),
  L("Ψυχολόγος", "m", "Ναι, αλλά δεν χρειάζεται να καταφύγουμε τόσο μακριά. Η μνήμη δεν λειτουργεί σαν βιντεοκάμερα· κάθε φορά που ανακαλούμε κάτι, το ξαναχτίζουμε, και μαζί μπαίνουν υποθέσεις, πράγματα που διαβάσαμε αργότερα, πράγματα που μας είπαν άλλοι. Όταν πολλοί άνθρωποι κάνουν την ίδια λογική υπόθεση, καταλήγουν στην ίδια λάθος ανάμνηση. Το διαδίκτυο απλώς τους φέρνει σε επαφή, και η συμφωνία των άλλων κάνει το λάθος να μοιάζει ακόμα πιο βέβαιο. Μια πρόσφατη μελέτη έδειξε, μάλιστα, ότι οι άνθρωποι νιώθουν πολύ σίγουροι ακριβώς για τις αναμνήσεις που είναι λανθασμένες. Η σιγουριά, με άλλα λόγια, δεν αποδεικνύει τίποτα.", "Yes, but we don't need to go that far. Memory doesn't work like a video camera; every time we recall something, we rebuild it, and assumptions, things we read later, things others told us get mixed in. When many people make the same logical assumption, they end up with the same false memory. The internet simply puts them in touch, and the agreement of others makes the error seem even more certain. A recent study even showed that people feel very sure precisely about the memories that are wrong. Certainty, in other words, proves nothing."),
 ],
 "questions": [
  Q("Τι «θυμούνταν» πολλοί άνθρωποι για τον Μαντέλα;", ["Ότι δεν έγινε ποτέ πρόεδρος", "Ότι είχε πεθάνει στη φυλακή τη δεκαετία του 1980", "Ότι είχε ζήσει στην Αμερική", "Ότι είχε γράψει ένα βιβλίο"], 1, "είχε πεθάνει στη φυλακή τη δεκαετία του 1980"),
  Q("Τι συνέβη στην πραγματικότητα;", ["Αποφυλακίστηκε το 1990, έγινε πρόεδρος και πέθανε το 2013", "Πέθανε στη φυλακή το 1990", "Έφυγε από τη Νότια Αφρική", "Δεν φυλακίστηκε ποτέ"], 0, "ο Μαντέλα αποφυλακίστηκε το 1990"),
  Q("Πώς λειτουργεί η μνήμη, κατά τον ψυχολόγο;", ["Σαν βιντεοκάμερα", "Κρατά μόνο τα σημαντικά γεγονότα", "Κάθε φορά που ανακαλούμε κάτι, το ξαναχτίζουμε", "Δεν αλλάζει ποτέ"], 2, "κάθε φορά που ανακαλούμε κάτι, το ξαναχτίζουμε"),
  Q("Ποιο είναι το συμπέρασμα του ψυχολόγου;", ["Ότι τα παράλληλα σύμπαντα ίσως υπάρχουν", "Ότι το διαδίκτυο δημιουργεί ψευδείς ειδήσεις", "Ότι η κοινή γνώμη έχει πάντα δίκιο", "Ότι η σιγουριά δεν αποδεικνύει τίποτα"], 3, "Η σιγουριά, με άλλα λόγια, δεν αποδεικνύει τίποτα"),
 ],
 "gloss": {"επινοήθηκε": "επινοούμαι — to be coined, invented", "φυλακή": "φυλακή — prison", "αποφυλακίστηκε": "αποφυλακίζομαι — to be released from prison", "ψευδή": "ψευδής — false", "ανάμνηση": "ανάμνηση — memory", "ταυτόχρονα": "ταυτόχρονα — at the same time", "παράλληλα σύμπαντα": "παράλληλο σύμπαν — parallel universe", "καταφύγουμε": "καταφεύγω — to resort to", "ανακαλούμε": "ανακαλώ — to recall", "υποθέσεις": "υπόθεση — assumption", "λανθασμένες": "λανθασμένος — wrong, mistaken", "σιγουριά": "σιγουριά — certainty"}
})

rnd = random.Random(144)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-144.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
