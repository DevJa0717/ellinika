# Source for library/listening/listening-64.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l64.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l64-ann-allagi-oras", "title": "Υπενθύμιση για την αλλαγή ώρας", "title_en": "A reminder about the clocks going back", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε το ραδιόφωνο ένα Σάββατο του Οκτωβρίου. Θα ακούσετε μια ανακοίνωση.",
 "script": [
  L("Εκφωνητής", "m", "Υπενθυμίζουμε στους ακροατές μας ότι αυτή τη νύχτα, ξημερώματα Κυριακής, τελειώνει η θερινή ώρα. Στις τέσσερις τα ξημερώματα, οι δείκτες των ρολογιών θα γυρίσουν μία ώρα πίσω, δηλαδή στις τρεις. Έτσι, θα κερδίσουμε μία ώρα ύπνου.", "We remind our listeners that tonight, in the early hours of Sunday, summer time ends. At four in the morning, the hands of the clocks will go back one hour, to three. So we'll gain an hour's sleep."),
  L("Εκφωνητής", "m", "Τα κινητά τηλέφωνα και οι υπολογιστές αλλάζουν συνήθως αυτόματα την ώρα. Ελέγξτε, όμως, τα ρολόγια του φούρνου, του αυτοκινήτου και τα ξυπνητήρια, για να μην έχετε εκπλήξεις τη Δευτέρα το πρωί.", "Mobile phones and computers usually change the time automatically. But check the clocks on your oven and in your car, and your alarm clocks, so you don't get any surprises on Monday morning."),
  L("Εκφωνητής", "m", "Όσοι ταξιδεύετε τη νύχτα με πλοίο ή αεροπλάνο, να έχετε υπόψη ότι τα δρομολόγια ακολουθούν τη νέα ώρα. Καλό σαββατοκύριακο.", "Those of you travelling overnight by boat or plane should bear in mind that timetables follow the new time. Have a good weekend."),
 ],
 "questions": [
  Q("Τι θα γίνει στις τέσσερις τα ξημερώματα;", ["Τα ρολόγια θα πάνε μία ώρα μπροστά", "Τα ρολόγια θα γυρίσουν μία ώρα πίσω", "Θα σταματήσουν τα δρομολόγια", "Θα αρχίσει η θερινή ώρα"], 1, "οι δείκτες των ρολογιών θα γυρίσουν μία ώρα πίσω"),
  Q("Ποια ρολόγια συμβουλεύει ο εκφωνητής να ελέγξουμε;", ["Τα κινητά τηλέφωνα", "Τους υπολογιστές", "Τα ρολόγια του φούρνου, του αυτοκινήτου και τα ξυπνητήρια", "Τα ρολόγια των σταθμών"], 2, "Ελέγξτε, όμως, τα ρολόγια του φούρνου, του αυτοκινήτου και τα ξυπνητήρια"),
  Q("Τι πρέπει να έχουν υπόψη όσοι ταξιδεύουν τη νύχτα;", ["Ότι τα δρομολόγια ακολουθούν τη νέα ώρα", "Ότι τα πλοία δεν κινούνται", "Ότι πρέπει να είναι στο λιμάνι μία ώρα νωρίτερα", "Ότι τα εισιτήρια αλλάζουν τιμή"], 0, "τα δρομολόγια ακολουθούν τη νέα ώρα"),
 ],
 "gloss": {"ξημερώματα": "ξημερώματα — early hours (before dawn)", "θερινή ώρα": "θερινή ώρα — summer time, daylight saving time", "δείκτες": "δείκτης — hand (of a clock)", "αυτόματα": "αυτόματα — automatically", "ξυπνητήρια": "ξυπνητήρι — alarm clock", "εκπλήξεις": "έκπληξη — surprise", "να έχετε υπόψη": "έχω υπόψη — to bear in mind"},
})

ITEMS.append({
 "id": "l64-vm-scholi-chorou", "title": "Μήνυμα από τη σχολή χορού", "title_en": "A message from the dance school", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε γραφτεί σε μαθήματα ταγκό. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Δασκάλα", "f", "Γεια σας, κύριε Πετρίδη, είμαι η Μυρτώ από τη σχολή χορού «Μιλόνγκα». Σας τηλεφωνώ γιατί το μάθημα ταγκό για αρχάριους μεταφέρεται από την Τρίτη στην Πέμπτη, ίδια ώρα, στις οκτώ και μισή. Η αίθουσα της Τρίτης θα ανακαινιστεί.", "Hello, Mr Petridis, this is Myrto from the Milonga dance school. I'm calling because the beginners' tango class is moving from Tuesday to Thursday, same time, half past eight. The Tuesday studio is being renovated."),
  L("Δασκάλα", "f", "Επίσης, μου είπατε ότι δεν έχετε παρτενέρ. Μην ανησυχείτε: μια κυρία που ξεκινά κι αυτή από την Πέμπτη ψάχνει ζευγάρι, οπότε μπορείτε να χορεύετε μαζί. Θυμηθείτε να φέρετε παπούτσια με λεία σόλα, όχι αθλητικά, γιατί κολλάνε στο πάτωμα.", "Also, you told me you don't have a partner. Don't worry: a lady who's also starting on Thursday is looking for a partner, so you can dance together. Remember to bring shoes with smooth soles, not trainers, because they stick to the floor."),
  L("Δασκάλα", "f", "Αν η Πέμπτη δεν σας βολεύει, πείτε μου, να σας επιστρέψουμε τα χρήματα του μήνα. Τα λέμε!", "If Thursday doesn't suit you, let me know and we'll refund this month's fee. See you!"),
 ],
 "questions": [
  Q("Γιατί μεταφέρεται το μάθημα;", ["Γιατί η δασκάλα είναι άρρωστη", "Γιατί η αίθουσα της Τρίτης θα ανακαινιστεί", "Γιατί δεν υπάρχουν αρκετοί μαθητές", "Γιατί η Τρίτη είναι αργία"], 1, "Η αίθουσα της Τρίτης θα ανακαινιστεί"),
  Q("Ποια λύση προτείνει η δασκάλα για τον παρτενέρ;", ["Να φέρει μια φίλη του", "Να χορεύει με τη δασκάλα", "Να χορεύει με μια κυρία που ξεκινά κι αυτή την Πέμπτη", "Να περιμένει το επόμενο τμήμα"], 2, "μια κυρία που ξεκινά κι αυτή από την Πέμπτη ψάχνει ζευγάρι"),
  Q("Γιατί δεν πρέπει να φέρει αθλητικά παπούτσια;", ["Γιατί χαλάνε το πάτωμα", "Γιατί κολλάνε στο πάτωμα", "Γιατί δεν επιτρέπονται στη σχολή", "Γιατί είναι βαριά"], 1, "όχι αθλητικά, γιατί κολλάνε στο πάτωμα"),
 ],
 "gloss": {"αρχάριους": "αρχάριος — beginner", "ανακαινιστεί": "ανακαινίζομαι — to be renovated", "παρτενέρ": "παρτενέρ — (dance) partner", "ζευγάρι": "ζευγάρι — partner, pair", "λεία σόλα": "λεία σόλα — smooth sole", "αθλητικά": "αθλητικά — trainers, sneakers", "κολλάνε": "κολλάω — to stick", "βολεύει": "βολεύω — to suit, be convenient"},
})

ITEMS.append({
 "id": "l64-dia-erasmus-domatio", "title": "Ένα δωμάτιο για έναν φοιτητή Erasmus", "title_en": "A room for an Erasmus student", "type": "dialogue", "level": "B2",
 "context_el": "Ένας φοιτητής από την Ισπανία, που θα σπουδάσει ένα εξάμηνο στη Θεσσαλονίκη, μιλά στο τηλέφωνο με μια ιδιοκτήτρια για ένα δωμάτιο.",
 "script": [
  L("Φοιτητής", "m", "Καλημέρα σας. Είδα την αγγελία σας για το δωμάτιο κοντά στο Αριστοτέλειο. Είναι ακόμη διαθέσιμο από τον Φεβρουάριο;", "Good morning. I saw your ad for the room near the Aristotle University. Is it still available from February?"),
  L("Ιδιοκτήτρια", "f", "Ναι, είναι. Είναι ένα δωμάτιο σε διαμέρισμα τριών υπνοδωματίων. Τα άλλα δύο τα νοικιάζουν μια Ελληνίδα φοιτήτρια και ένας Ιταλός. Το ενοίκιο είναι τριακόσια είκοσι ευρώ, με τα κοινόχρηστα, αλλά χωρίς το ρεύμα.", "Yes, it is. It's a room in a three-bedroom flat. The other two are rented by a Greek student and an Italian. The rent is three hundred and twenty euros, including the building charges, but not electricity."),
  L("Φοιτητής", "m", "Και για πόσο καιρό πρέπει να υπογράψω συμβόλαιο; Θα μείνω μόνο πέντε μήνες.", "And for how long do I have to sign a contract? I'll only be staying five months."),
  L("Ιδιοκτήτρια", "f", "Δεν υπάρχει πρόβλημα, νοικιάζω συχνά σε φοιτητές Erasmus. Θα σας ζητήσω, όμως, ένα ενοίκιο εγγύηση, που θα σας το επιστρέψω όταν φύγετε, αν όλα είναι εντάξει. Και αν θέλετε, μπορώ να σας δείξω το δωμάτιο με βιντεοκλήση πριν έρθετε.", "That's no problem, I often rent to Erasmus students. I will, however, ask you for one month's rent as a deposit, which I'll return when you leave, if everything is in order. And if you like, I can show you the room by video call before you come."),
 ],
 "questions": [
  Q("Τι περιλαμβάνει το ενοίκιο;", ["Το ρεύμα", "Τα κοινόχρηστα", "Το ίντερνετ και το ρεύμα", "Τίποτα"], 1, "με τα κοινόχρηστα, αλλά χωρίς το ρεύμα"),
  Q("Ποιος μένει ήδη στο διαμέρισμα;", ["Δύο Ιταλοί", "Μια Ελληνίδα φοιτήτρια και ένας Ιταλός", "Η ιδιοκτήτρια", "Ένας Ισπανός"], 1, "μια Ελληνίδα φοιτήτρια και ένας Ιταλός"),
  Q("Τι προτείνει η ιδιοκτήτρια πριν έρθει ο φοιτητής;", ["Να πληρώσει όλο το εξάμηνο", "Να του δείξει το δωμάτιο με βιντεοκλήση", "Να στείλει έναν φίλο του να δει το δωμάτιο", "Να υπογράψει για έναν χρόνο"], 1, "μπορώ να σας δείξω το δωμάτιο με βιντεοκλήση"),
 ],
 "gloss": {"αγγελία": "αγγελία — advertisement, listing", "διαθέσιμο": "διαθέσιμος — available", "υπνοδωματίων": "υπνοδωμάτιο — bedroom", "κοινόχρηστα": "κοινόχρηστα — shared building charges", "συμβόλαιο": "συμβόλαιο — contract, lease", "εγγύηση": "εγγύηση — deposit", "βιντεοκλήση": "βιντεοκλήση — video call"},
})

ITEMS.append({
 "id": "l64-dia-periagogi", "title": "Μια απρόσμενη χρέωση", "title_en": "An unexpected charge", "type": "dialogue", "level": "B2",
 "context_el": "Μια πελάτισσα τηλεφωνεί στην εξυπηρέτηση πελατών της εταιρείας κινητής τηλεφωνίας της, γιατί ο λογαριασμός της είναι πολύ υψηλότερος από ό,τι συνήθως.",
 "script": [
  L("Πελάτισσα", "f", "Καλησπέρα. Ο λογαριασμός μου αυτόν τον μήνα είναι ενενήντα ευρώ, ενώ συνήθως πληρώνω είκοσι. Δεν καταλαβαίνω τι έγινε.", "Good afternoon. My bill this month is ninety euros, when I usually pay twenty. I don't understand what happened."),
  L("Υπάλληλος", "m", "Μια στιγμή να δω. Βλέπω χρήση δεδομένων στις είκοσι Σεπτεμβρίου, από την Τουρκία. Ταξιδέψατε στην Κωνσταντινούπολη;", "One moment, let me look. I see data usage on the twentieth of September, from Turkey. Did you travel to Istanbul?"),
  L("Πελάτισσα", "f", "Ναι, για ένα τριήμερο. Νόμιζα, όμως, ότι η περιαγωγή είναι πια δωρεάν στο εξωτερικό.", "Yes, for a long weekend. But I thought roaming was free abroad now."),
  L("Υπάλληλος", "m", "Είναι δωρεάν μόνο μέσα στην Ευρωπαϊκή Ένωση. Η Τουρκία δεν είναι μέλος, γι’ αυτό χρεωθήκατε με το τιμολόγιο εκτός Ένωσης. Επειδή, όμως, είστε πελάτισσα πολλά χρόνια, μπορώ να σας κάνω έκπτωση πενήντα τοις εκατό σε αυτή τη χρέωση. Και την επόμενη φορά, ενεργοποιήστε ένα πακέτο ταξιδιού πριν φύγετε· κοστίζει μόνο δέκα ευρώ την εβδομάδα.", "It's free only within the European Union. Turkey isn't a member, so you were charged at the non-EU rate. But since you've been a customer for many years, I can give you a fifty per cent discount on this charge. And next time, activate a travel package before you leave; it costs only ten euros a week."),
 ],
 "questions": [
  Q("Πόσο πληρώνει συνήθως η πελάτισσα;", ["Ενενήντα ευρώ", "Είκοσι ευρώ", "Δέκα ευρώ", "Πενήντα ευρώ"], 1, "συνήθως πληρώνω είκοσι"),
  Q("Γιατί χρεώθηκε η πελάτισσα;", ["Γιατί έκανε πολλά τηλεφωνήματα στην Ελλάδα", "Γιατί χρησιμοποίησε δεδομένα σε χώρα εκτός Ευρωπαϊκής Ένωσης", "Γιατί άλλαξε πρόγραμμα", "Γιατί έχασε το κινητό της"], 1, "Η Τουρκία δεν είναι μέλος, γι’ αυτό χρεωθήκατε με το τιμολόγιο εκτός Ένωσης"),
  Q("Τι της προσφέρει ο υπάλληλος;", ["Να ακυρώσει όλη τη χρέωση", "Έκπτωση πενήντα τοις εκατό σε αυτή τη χρέωση", "Ένα δωρεάν πακέτο ταξιδιού", "Ένα καινούργιο κινητό"], 1, "μπορώ να σας κάνω έκπτωση πενήντα τοις εκατό σε αυτή τη χρέωση"),
 ],
 "gloss": {"εξυπηρέτηση πελατών": "εξυπηρέτηση πελατών — customer service", "κινητής τηλεφωνίας": "κινητή τηλεφωνία — mobile telephony", "χρήση δεδομένων": "χρήση δεδομένων — data usage", "τριήμερο": "τριήμερο — three-day break, long weekend", "περιαγωγή": "περιαγωγή — roaming", "χρεωθήκατε": "χρεώνομαι — to be charged", "τιμολόγιο": "τιμολόγιο — tariff, rate", "ενεργοποιήστε": "ενεργοποιώ — to activate"},
})

ITEMS.append({
 "id": "l64-int-ornithologos", "title": "Ο ορνιθολόγος της Καλλονής", "title_en": "The ornithologist of Kalloni", "type": "interview", "level": "B2",
 "context_el": "Σε μια εκπομπή για τη φύση, μια δημοσιογράφος μιλά με έναν ορνιθολόγο από τη Λέσβο.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Βαλιαννάτε, γιατί έρχονται κάθε άνοιξη στη Λέσβο εκατοντάδες παρατηρητές πουλιών από όλη την Ευρώπη;", "Mr Valiannatos, why do hundreds of birdwatchers from all over Europe come to Lesvos every spring?"),
  L("Ορνιθολόγος", "m", "Γιατί η Λέσβος βρίσκεται πάνω σε μια από τις μεγάλες διαδρομές μετανάστευσης ανάμεσα στην Αφρική και στη βόρεια Ευρώπη. Τον Απρίλιο και τον Μάιο, χιλιάδες πουλιά σταματούν εδώ για να ξεκουραστούν και να τραφούν, κυρίως στους υγροτόπους και στις αλυκές του κόλπου της Καλλονής.", "Because Lesvos lies on one of the great migration routes between Africa and northern Europe. In April and May, thousands of birds stop here to rest and feed, mainly in the wetlands and salt pans of the Gulf of Kalloni."),
  L("Δημοσιογράφος", "f", "Ποιο είναι το πιο εντυπωσιακό θέαμα;", "What is the most impressive sight?"),
  L("Ορνιθολόγος", "m", "Για τους περισσότερους, τα φλαμίνγκο, που γεμίζουν τις αλυκές με ροζ. Εμένα, όμως, με συγκινούν τα μικρά πουλιά, που ζυγίζουν λιγότερο από δέκα γραμμάρια και έχουν διασχίσει τη Σαχάρα. Για τους επισκέπτες έχω μια συμβουλή: κιάλια, υπομονή και ησυχία. Και, παρακαλώ, όχι κοντά στις φωλιές.", "For most people, the flamingos, which fill the salt pans with pink. But what moves me are the little birds that weigh less than ten grams and have crossed the Sahara. I have one piece of advice for visitors: binoculars, patience and quiet. And please, not near the nests."),
 ],
 "questions": [
  Q("Γιατί έρχονται τόσα πουλιά στη Λέσβο;", ["Γιατί έχει ζεστό κλίμα όλο τον χρόνο", "Γιατί βρίσκεται πάνω σε μια μεγάλη διαδρομή μετανάστευσης", "Γιατί υπάρχουν πολλά δάση", "Γιατί οι κάτοικοι τα ταΐζουν"], 1, "η Λέσβος βρίσκεται πάνω σε μια από τις μεγάλες διαδρομές μετανάστευσης"),
  Q("Τι συγκινεί περισσότερο τον ορνιθολόγο;", ["Τα φλαμίνγκο", "Τα μικρά πουλιά που έχουν διασχίσει τη Σαχάρα", "Οι αετοί", "Οι γλάροι του λιμανιού"], 1, "με συγκινούν τα μικρά πουλιά, που ζυγίζουν λιγότερο από δέκα γραμμάρια και έχουν διασχίσει τη Σαχάρα"),
  Q("Ποια συμβουλή δίνει στους επισκέπτες;", ["Να έρχονται μόνο το καλοκαίρι", "Κιάλια, υπομονή και ησυχία, και όχι κοντά στις φωλιές", "Να φέρνουν τροφή για τα πουλιά", "Να φωτογραφίζουν με φλας"], 1, "κιάλια, υπομονή και ησυχία. Και, παρακαλώ, όχι κοντά στις φωλιές"),
 ],
 "gloss": {"ορνιθολόγο": "ορνιθολόγος — ornithologist", "παρατηρητές πουλιών": "παρατηρητής πουλιών — birdwatcher", "μετανάστευσης": "μετανάστευση — migration", "τραφούν": "τρέφομαι — to feed", "υγροτόπους": "υγρότοπος — wetland", "αλυκές": "αλυκή — salt pan", "θέαμα": "θέαμα — sight, spectacle", "διασχίσει": "διασχίζω — to cross", "κιάλια": "κιάλια — binoculars", "φωλιές": "φωλιά — nest"},
})

ITEMS.append({
 "id": "l64-rep-moni-arkadiou", "title": "Η Μονή Αρκαδίου", "title_en": "Arkadi Monastery", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από την Κρήτη, λίγες μέρες πριν από την επέτειο της 8ης Νοεμβρίου.",
 "script": [
  L("Ρεπόρτερ", "m", "Βρισκόμαστε στη Μονή Αρκαδίου, περίπου είκοσι χιλιόμετρα από το Ρέθυμνο. Η εκκλησία, με την περίτεχνη πρόσοψη, είναι ένα από τα πιο φωτογραφημένα μνημεία της Κρήτης. Για τους Κρητικούς, όμως, ο τόπος αυτός είναι πάνω απ’ όλα σύμβολο θυσίας.", "We are at Arkadi Monastery, about twenty kilometres from Rethymno. The church, with its ornate facade, is one of the most photographed monuments in Crete. For Cretans, however, this place is above all a symbol of sacrifice."),
  L("Ρεπόρτερ", "m", "Τον Νοέμβριο του 1866, κατά τη διάρκεια της κρητικής επανάστασης, εκατοντάδες επαναστάτες, γυναίκες και παιδιά είχαν καταφύγει στο μοναστήρι, που το πολιορκούσε ο οθωμανικός στρατός. Όταν οι πολιορκητές μπήκαν στην αυλή, οι υπερασπιστές ανατίναξαν την πυριτιδαποθήκη, προτιμώντας τον θάνατο από την παράδοση.", "In November 1866, during the Cretan revolt, hundreds of rebels, women and children had taken refuge in the monastery, which was besieged by the Ottoman army. When the besiegers entered the courtyard, the defenders blew up the powder magazine, preferring death to surrender."),
  L("Ρεπόρτερ", "m", "Η είδηση συγκλόνισε την Ευρώπη, και πολλοί διανοούμενοι στήριξαν από τότε τον αγώνα των Κρητικών. Σήμερα, στο μικρό μουσείο της μονής, ο επισκέπτης μπορεί να δει προσωπικά αντικείμενα των υπερασπιστών, ενώ η πυριτιδαποθήκη, χωρίς στέγη, έχει διατηρηθεί όπως ήταν.", "The news shook Europe, and many intellectuals supported the Cretans' struggle from then on. Today, in the monastery's small museum, visitors can see personal belongings of the defenders, while the roofless powder magazine has been preserved as it was."),
 ],
 "questions": [
  Q("Πού βρίσκεται η Μονή Αρκαδίου;", ["Στο κέντρο του Ηρακλείου", "Περίπου είκοσι χιλιόμετρα από το Ρέθυμνο", "Στα Χανιά", "Σε ένα νησάκι κοντά στην Κρήτη"], 1, "περίπου είκοσι χιλιόμετρα από το Ρέθυμνο"),
  Q("Τι έκαναν οι υπερασπιστές, όταν οι πολιορκητές μπήκαν στην αυλή;", ["Παραδόθηκαν", "Ανατίναξαν την πυριτιδαποθήκη", "Έφυγαν από μια μυστική πόρτα", "Ζήτησαν βοήθεια από την Ευρώπη"], 1, "οι υπερασπιστές ανατίναξαν την πυριτιδαποθήκη"),
  Q("Πώς αντέδρασε η Ευρώπη;", ["Αδιαφόρησε", "Η είδηση τη συγκλόνισε και πολλοί διανοούμενοι στήριξαν τους Κρητικούς", "Έστειλε στρατό", "Δεν έμαθε ποτέ το γεγονός"], 1, "Η είδηση συγκλόνισε την Ευρώπη, και πολλοί διανοούμενοι στήριξαν από τότε τον αγώνα των Κρητικών"),
 ],
 "gloss": {"επέτειο": "επέτειος — anniversary", "περίτεχνη": "περίτεχνος — ornate", "πρόσοψη": "πρόσοψη — facade", "θυσίας": "θυσία — sacrifice", "καταφύγει": "καταφεύγω — to take refuge", "πολιορκούσε": "πολιορκώ — to besiege", "υπερασπιστές": "υπερασπιστής — defender", "πυριτιδαποθήκη": "πυριτιδαποθήκη — powder magazine", "παράδοση": "παράδοση — surrender (here)", "διανοούμενοι": "διανοούμενος — intellectual"},
})

ITEMS.append({
 "id": "l64-dia-taxidi-lisavona", "title": "Ταξίδι στη Λισαβόνα με τους γονείς", "title_en": "A trip to Lisbon with our parents", "type": "dialogue", "level": "B2",
 "context_el": "Δύο αδέλφια οργανώνουν ένα ταξίδι για την επέτειο γάμου των γονιών τους.",
 "script": [
  L("Ιάσονας", "m", "Λοιπόν, τα σαράντα χρόνια γάμου των γονιών είναι τον Μάιο. Σκεφτόμουν να τους κάνουμε δώρο ένα ταξίδι στη Λισαβόνα. Η μαμά λέει πάντα ότι θέλει να ακούσει φάδο από κοντά.", "So, our parents' fortieth wedding anniversary is in May. I was thinking we could give them a trip to Lisbon. Mum always says she wants to hear fado live."),
  L("Δανάη", "f", "Ωραία ιδέα, αλλά ο μπαμπάς δεν περπατάει πολύ μετά την εγχείρηση στο γόνατο, και η Λισαβόνα έχει πολλές ανηφόρες. Πρέπει να βρούμε ξενοδοχείο στο κέντρο, κοντά σε στάση του τραμ.", "Nice idea, but Dad doesn't walk much since his knee operation, and Lisbon has lots of hills. We need to find a hotel in the centre, near a tram stop."),
  L("Ιάσονας", "m", "Σωστά. Και να κλείσουμε την πτήση από τώρα, γιατί τον Μάιο οι τιμές ανεβαίνουν. Υπάρχει απευθείας πτήση από την Αθήνα δύο φορές την εβδομάδα.", "Right. And we should book the flight now, because prices go up in May. There's a direct flight from Athens twice a week."),
  L("Δανάη", "f", "Τέλεια. Εγώ θα αναλάβω το ξενοδοχείο και μια βραδιά με φάδο σε ένα ταβερνάκι. Εσύ κλείσε τα εισιτήρια. Και μην πεις τίποτα στη γιαγιά· δεν κρατάει μυστικό ούτε πέντε λεπτά!", "Perfect. I'll take care of the hotel and an evening of fado in a little tavern. You book the tickets. And don't say anything to Grandma; she can't keep a secret for even five minutes!"),
 ],
 "questions": [
  Q("Γιατί σκέφτονται τη Λισαβόνα;", ["Γιατί είναι φθηνή", "Γιατί η μητέρα τους θέλει να ακούσει φάδο από κοντά", "Γιατί εκεί πέρασαν τον μήνα του μέλιτος", "Γιατί έχουν συγγενείς εκεί"], 1, "Η μαμά λέει πάντα ότι θέλει να ακούσει φάδο από κοντά"),
  Q("Γιατί πρέπει το ξενοδοχείο να είναι κοντά σε στάση του τραμ;", ["Γιατί δεν θα νοικιάσουν αυτοκίνητο", "Γιατί ο πατέρας δεν περπατάει πολύ μετά την εγχείρηση", "Γιατί το τραμ είναι δωρεάν", "Γιατί είναι πιο φθηνό"], 1, "ο μπαμπάς δεν περπατάει πολύ μετά την εγχείρηση στο γόνατο"),
  Q("Γιατί δεν πρέπει να μάθει τίποτα η γιαγιά;", ["Γιατί θα θυμώσει", "Γιατί δεν κρατάει μυστικό", "Γιατί θέλει κι εκείνη να πάει", "Γιατί δεν της αρέσουν τα ταξίδια"], 1, "δεν κρατάει μυστικό ούτε πέντε λεπτά"),
 ],
 "gloss": {"επέτειο γάμου": "επέτειος γάμου — wedding anniversary", "φάδο": "φάδο — fado (Portuguese song)", "εγχείρηση": "εγχείρηση — operation, surgery", "γόνατο": "γόνατο — knee", "ανηφόρες": "ανηφόρα — uphill slope", "απευθείας πτήση": "απευθείας πτήση — direct flight", "αναλάβω": "αναλαμβάνω — to take on, take care of", "ταβερνάκι": "ταβερνάκι — little tavern"},
})

ITEMS.append({
 "id": "l64-mono-dialogismos", "title": "Δέκα λεπτά σιωπής", "title_en": "Ten minutes of silence", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να μιλά σε ένα podcast για το πώς ξεκίνησε τον διαλογισμό.",
 "script": [
  L("Ειρήνη", "f", "Πριν από δύο χρόνια ήμουν διαρκώς αγχωμένη. Δούλευα σε μια διαφημιστική εταιρεία, κοιμόμουν άσχημα και θύμωνα για το παραμικρό. Μια φίλη μού πρότεινε να δοκιμάσω τον διαλογισμό. Στην αρχή γέλασα· μου φαινόταν κάτι για ανθρώπους με πολύ ελεύθερο χρόνο.", "Two years ago I was constantly stressed. I worked at an advertising agency, slept badly and got angry over the slightest thing. A friend suggested I try meditation. At first I laughed; it seemed like something for people with lots of free time."),
  L("Ειρήνη", "f", "Τελικά δοκίμασα, με μια εφαρμογή στο κινητό: δέκα λεπτά κάθε πρωί, πριν ξυπνήσουν τα παιδιά. Τις πρώτες μέρες το μυαλό μου έτρεχε παντού: στη λίστα με τα ψώνια, στα email, σε μια παλιά κουβέντα. Η δασκάλα στην εφαρμογή έλεγε ότι αυτό είναι φυσιολογικό και ότι απλώς επιστρέφουμε, ξανά και ξανά, στην αναπνοή.", "In the end I gave it a try, with an app on my phone: ten minutes every morning, before the children woke up. For the first few days my mind wandered everywhere: to the shopping list, to emails, to an old conversation. The teacher in the app said this is normal and that we simply come back, again and again, to the breath."),
  L("Ειρήνη", "f", "Δεν έγινα ξαφνικά άλλος άνθρωπος. Αλλά τώρα, όταν κάτι με εκνευρίζει, καταλαβαίνω τι νιώθω πριν αντιδράσω. Και αυτά τα λίγα δευτερόλεπτα κάνουν τεράστια διαφορά.", "I didn't suddenly become a different person. But now, when something annoys me, I notice what I'm feeling before I react. And those few seconds make a huge difference."),
 ],
 "questions": [
  Q("Πώς αντέδρασε αρχικά στην πρόταση της φίλης της;", ["Ενθουσιάστηκε", "Γέλασε, γιατί της φαινόταν κάτι για ανθρώπους με πολύ ελεύθερο χρόνο", "Θύμωσε", "Ζήτησε να πάνε μαζί σε μάθημα"], 1, "Στην αρχή γέλασα· μου φαινόταν κάτι για ανθρώπους με πολύ ελεύθερο χρόνο"),
  Q("Πότε κάνει διαλογισμό;", ["Το βράδυ πριν κοιμηθεί", "Στο μεσημεριανό διάλειμμα", "Δέκα λεπτά κάθε πρωί, πριν ξυπνήσουν τα παιδιά", "Μία φορά την εβδομάδα"], 2, "δέκα λεπτά κάθε πρωί, πριν ξυπνήσουν τα παιδιά"),
  Q("Ποια αλλαγή περιγράφει στο τέλος;", ["Ότι δεν θυμώνει ποτέ πια", "Ότι καταλαβαίνει τι νιώθει πριν αντιδράσει", "Ότι άλλαξε δουλειά", "Ότι κοιμάται δέκα ώρες"], 1, "καταλαβαίνω τι νιώθω πριν αντιδράσω"),
 ],
 "gloss": {"διαλογισμό": "διαλογισμός — meditation", "αγχωμένη": "αγχωμένος — stressed", "για το παραμικρό": "για το παραμικρό — over the slightest thing", "εφαρμογή": "εφαρμογή — app", "φυσιολογικό": "φυσιολογικός — normal", "αναπνοή": "αναπνοή — breath, breathing", "εκνευρίζει": "εκνευρίζω — to annoy", "αντιδράσω": "αντιδρώ — to react"},
})

ITEMS.append({
 "id": "l64-c1-giransi", "title": "Μια χώρα που γερνάει", "title_en": "A country growing old", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή λόγου, ένας δημοσιογράφος συζητά με μια δημογράφο για τη γήρανση του πληθυσμού στην Ελλάδα.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι δημογράφοι μιλούν εδώ και χρόνια για «δημογραφική βόμβα». Είναι υπερβολή ή πραγματικός κίνδυνος;", "Demographers have been talking about a 'demographic time bomb' for years. Is it an exaggeration or a real danger?"),
  L("Δημογράφος", "f", "Η έκφραση είναι δραματική, αλλά τα στοιχεία είναι σαφή. Η Ελλάδα έχει έναν από τους χαμηλότερους δείκτες γονιμότητας στην Ευρώπη και, ταυτόχρονα, ένα από τα υψηλότερα ποσοστά ατόμων άνω των εξήντα πέντε. Σε αυτό προστέθηκε, κατά την οικονομική κρίση, η μετανάστευση χιλιάδων νέων, πολλοί από τους οποίους ήταν άνθρωποι σε ηλικία να κάνουν οικογένεια.", "The expression is dramatic, but the figures are clear. Greece has one of the lowest fertility rates in Europe and, at the same time, one of the highest proportions of people over sixty-five. Added to this, during the economic crisis, was the emigration of thousands of young people, many of whom were of an age to start a family."),
  L("Δημοσιογράφος", "m", "Ποιες είναι οι συνέπειες στην καθημερινή ζωή;", "What are the consequences for everyday life?"),
  L("Δημογράφος", "f", "Τις βλέπουμε ήδη: σχολεία που κλείνουν σε ορεινά χωριά, ελλείψεις εργατικού δυναμικού σε τομείς όπως ο τουρισμός και η γεωργία, πιέσεις στο ασφαλιστικό σύστημα και στις υπηρεσίες υγείας. Δεν υπάρχει μία μαγική λύση. Τα επιδόματα γέννησης βοηθούν λίγο· πολύ περισσότερο μετρούν η σταθερή εργασία, η προσιτή στέγη και οι δομές φροντίδας για τα μικρά παιδιά. Και, βέβαια, μια ρεαλιστική πολιτική για τη μετανάστευση, που θα βλέπει τους νεοφερμένους όχι μόνο ως πρόβλημα, αλλά και ως μέρος της λύσης.", "We already see them: schools closing in mountain villages, labour shortages in sectors like tourism and agriculture, pressure on the social insurance system and health services. There is no single magic solution. Birth allowances help a little; far more important are stable employment, affordable housing and childcare facilities for young children. And, of course, a realistic migration policy, one that sees newcomers not only as a problem but also as part of the solution."),
 ],
 "questions": [
  Q("Πώς κρίνει η δημογράφος την έκφραση «δημογραφική βόμβα»;", ["Ως εντελώς λανθασμένη", "Ως δραματική, αλλά τα στοιχεία είναι σαφή", "Ως πολύ ήπια", "Ως πολιτικό σύνθημα χωρίς βάση"], 1, "Η έκφραση είναι δραματική, αλλά τα στοιχεία είναι σαφή"),
  Q("Τι επιβάρυνε την κατάσταση κατά την οικονομική κρίση;", ["Η άφιξη πολλών συνταξιούχων από το εξωτερικό", "Η μετανάστευση χιλιάδων νέων", "Η αύξηση των γεννήσεων", "Το κλείσιμο των νοσοκομείων"], 1, "η μετανάστευση χιλιάδων νέων"),
  Q("Τι θεωρεί πιο σημαντικό από τα επιδόματα γέννησης;", ["Τη μείωση των φόρων για τους συνταξιούχους", "Τη σταθερή εργασία, την προσιτή στέγη και τις δομές φροντίδας παιδιών", "Την κατασκευή νέων σχολείων", "Την αύξηση των ορίων συνταξιοδότησης"], 1, "πολύ περισσότερο μετρούν η σταθερή εργασία, η προσιτή στέγη και οι δομές φροντίδας για τα μικρά παιδιά"),
  Q("Πώς πρέπει, κατά τη γνώμη της, να βλέπει η πολιτική τους νεοφερμένους;", ["Μόνο ως πρόβλημα", "Και ως μέρος της λύσης", "Ως προσωρινούς επισκέπτες", "Ως ευθύνη άλλων χωρών"], 1, "όχι μόνο ως πρόβλημα, αλλά και ως μέρος της λύσης"),
 ],
 "gloss": {"δημογράφο": "δημογράφος — demographer", "γήρανση": "γήρανση — ageing", "δείκτες γονιμότητας": "δείκτης γονιμότητας — fertility rate", "ποσοστά": "ποσοστό — proportion, rate", "εργατικού δυναμικού": "εργατικό δυναμικό — workforce", "ασφαλιστικό σύστημα": "ασφαλιστικό σύστημα — social insurance (pension) system", "επιδόματα γέννησης": "επίδομα γέννησης — birth allowance", "προσιτή στέγη": "προσιτή στέγη — affordable housing", "δομές φροντίδας": "δομή φροντίδας — care facility", "νεοφερμένους": "νεοφερμένος — newcomer"},
})

ITEMS.append({
 "id": "l64-c1-eok", "title": "Η ένταξη στην ΕΟΚ", "title_en": "Joining the EEC", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από διάλεξη ιστορικού για την ένταξη της Ελλάδας στην Ευρωπαϊκή Οικονομική Κοινότητα.",
 "script": [
  L("Ιστορικός", "m", "Η Ελλάδα είχε συνάψει συμφωνία σύνδεσης με την Ευρωπαϊκή Οικονομική Κοινότητα ήδη από το 1961, αλλά η δικτατορία του 1967 πάγωσε τη διαδικασία. Μετά την αποκατάσταση της δημοκρατίας το 1974, ο Κωνσταντίνος Καραμανλής έθεσε την πλήρη ένταξη ως εθνική προτεραιότητα.", "Greece had concluded an association agreement with the European Economic Community as early as 1961, but the 1967 dictatorship froze the process. After the restoration of democracy in 1974, Konstantinos Karamanlis made full membership a national priority."),
  L("Ιστορικός", "m", "Για τον Καραμανλή, το διακύβευμα δεν ήταν μόνο οικονομικό. Η ένταξη θα στερέωνε τους νεαρούς δημοκρατικούς θεσμούς και θα έδενε τη χώρα με τη Δύση, σε μια εποχή έντασης με την Τουρκία. Η συνθήκη προσχώρησης υπογράφηκε στο Ζάππειο τον Μάιο του 1979, και η Ελλάδα έγινε το δέκατο μέλος της Κοινότητας την 1η Ιανουαρίου 1981.", "For Karamanlis, the stakes were not only economic. Membership would consolidate the young democratic institutions and tie the country to the West, at a time of tension with Turkey. The treaty of accession was signed at the Zappeion in May 1979, and Greece became the tenth member of the Community on 1 January 1981."),
  L("Ιστορικός", "m", "Η απόφαση δεν ήταν ομόφωνη. Μέρος της αντιπολίτευσης φοβόταν ότι η ελληνική γεωργία και βιομηχανία δεν θα άντεχαν τον ανταγωνισμό. Τις επόμενες δεκαετίες, τα κοινοτικά κονδύλια άλλαξαν την όψη της υπαίθρου, με δρόμους, αρδευτικά έργα και επιδοτήσεις. Το αν η χώρα αξιοποίησε σωστά αυτούς τους πόρους παραμένει, ωστόσο, αντικείμενο έντονης συζήτησης.", "The decision was not unanimous. Part of the opposition feared that Greek agriculture and industry would not withstand the competition. In the following decades, Community funds changed the face of the countryside, with roads, irrigation works and subsidies. Whether the country made good use of these resources, however, remains the subject of heated debate."),
 ],
 "questions": [
  Q("Γιατί πάγωσε η διαδικασία σύνδεσης;", ["Λόγω οικονομικής κρίσης", "Λόγω της δικτατορίας του 1967", "Γιατί η ΕΟΚ απέρριψε την Ελλάδα", "Λόγω πολέμου με την Τουρκία"], 1, "η δικτατορία του 1967 πάγωσε τη διαδικασία"),
  Q("Ποιο ήταν, για τον Καραμανλή, το διακύβευμα πέρα από την οικονομία;", ["Η ενίσχυση της δημοκρατίας και η πρόσδεση της χώρας στη Δύση", "Η κατάργηση των συνόρων", "Η υιοθέτηση νέου νομίσματος", "Η μείωση του στρατού"], 0, "Η ένταξη θα στερέωνε τους νεαρούς δημοκρατικούς θεσμούς και θα έδενε τη χώρα με τη Δύση"),
  Q("Πότε έγινε η Ελλάδα μέλος της Κοινότητας;", ["Τον Μάιο του 1979", "Το 1974", "Την 1η Ιανουαρίου 1981", "Το 1961"], 2, "η Ελλάδα έγινε το δέκατο μέλος της Κοινότητας την 1η Ιανουαρίου 1981"),
  Q("Τι φοβόταν μέρος της αντιπολίτευσης;", ["Ότι θα χανόταν η γλώσσα", "Ότι η γεωργία και η βιομηχανία δεν θα άντεχαν τον ανταγωνισμό", "Ότι θα αυξανόταν η μετανάστευση", "Ότι η χώρα θα έχανε νησιά"], 1, "η ελληνική γεωργία και βιομηχανία δεν θα άντεχαν τον ανταγωνισμό"),
 ],
 "gloss": {"συνάψει": "συνάπτω — to conclude (an agreement)", "συμφωνία σύνδεσης": "συμφωνία σύνδεσης — association agreement", "πάγωσε": "παγώνω — to freeze", "αποκατάσταση": "αποκατάσταση — restoration", "διακύβευμα": "διακύβευμα — what is at stake", "στερέωνε": "στερεώνω — to consolidate", "συνθήκη προσχώρησης": "συνθήκη προσχώρησης — treaty of accession", "ομόφωνη": "ομόφωνος — unanimous", "κονδύλια": "κονδύλι — fund, budget item", "αρδευτικά έργα": "αρδευτικά έργα — irrigation works", "αξιοποίησε": "αξιοποιώ — to make use of"},
})

rnd = random.Random(64)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-64.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
