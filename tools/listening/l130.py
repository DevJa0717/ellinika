# Source for library/listening/listening-130.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l130.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l130-ann-panselinos", "title": "Βραδιά της Πανσελήνου στον αρχαιολογικό χώρο", "title_en": "Full-moon evening at the archaeological site", "type": "announcement", "level": "B2",
 "context_el": "Είναι Αύγουστος. Ακούτε στο ραδιόφωνο μια ανακοίνωση του δήμου για τη βραδιά της Πανσελήνου.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος μας ανακοινώνει ότι, όπως κάθε χρόνο, την Παρασκευή που έρχεται, βράδυ της αυγουστιάτικης Πανσελήνου, ο αρχαιολογικός χώρος θα μείνει ανοιχτός από τις οχτώ το βράδυ μέχρι τη μία μετά τα μεσάνυχτα. Η είσοδος θα είναι ελεύθερη για όλους.", "Our municipality announces that, as every year, this coming Friday, the night of the August full moon, the archaeological site will stay open from eight in the evening until one after midnight. Entry will be free for everyone."),
  L("Εκφωνήτρια", "f", "Στις εννιά και μισή, στο αρχαίο θέατρο, η δημοτική χορωδία θα παρουσιάσει τραγούδια εμπνευσμένα από το φεγγάρι. Οι θέσεις στο θέατρο είναι περιορισμένες, γι' αυτό συνιστάται να έρθετε νωρίς. Δεν χρειάζεται κράτηση.", "At half past nine, in the ancient theatre, the municipal choir will present songs inspired by the moon. Seats in the theatre are limited, so you are advised to come early. No booking is needed."),
  L("Εκφωνήτρια", "f", "Υπενθυμίζουμε ότι στον χώρο απαγορεύονται τα τρόφιμα, το αλκοόλ και τα τακούνια, που προκαλούν φθορές στα αρχαία. Επιτρέπεται μόνο νερό. Συνιστάται να έχετε μαζί σας φακό, γιατί κάποια μονοπάτια δεν φωτίζονται.", "We remind you that food, alcohol and high heels, which damage the antiquities, are not allowed on the site. Only water is permitted. You are advised to bring a torch, because some paths are not lit."),
 ],
 "questions": [
  Q("Τι ισχύει για την είσοδο τη βραδιά της Πανσελήνου;", ["Κοστίζει όσο και τη μέρα", "Είναι ελεύθερη για όλους", "Είναι δωρεάν μόνο για τους δημότες", "Χρειάζεται εισιτήριο από πριν"], 1, "Η είσοδος θα είναι ελεύθερη για όλους"),
  Q("Γιατί συνιστάται να έρθει κανείς νωρίς στη συναυλία;", ["Επειδή οι θέσεις είναι περιορισμένες", "Επειδή η χορωδία ξεκινά στις οχτώ", "Επειδή χρειάζεται να κλείσει θέση", "Επειδή ο χώρος κλείνει νωρίς"], 0, "Οι θέσεις στο θέατρο είναι περιορισμένες, γι' αυτό συνιστάται να έρθετε νωρίς"),
  Q("Τι συνιστάται να φέρουν οι επισκέπτες;", ["Ένα μαξιλάρι για το θέατρο", "Κάτι να φάνε", "Έναν φακό", "Άνετα παπούτσια με τακούνι"], 2, "Συνιστάται να έχετε μαζί σας φακό"),
 ],
 "gloss": {"Πανσελήνου": "Πανσέληνος — full moon", "αυγουστιάτικης": "αυγουστιάτικος — of August", "αρχαιολογικός χώρος": "αρχαιολογικός χώρος — archaeological site", "μεσάνυχτα": "μεσάνυχτα — midnight", "χορωδία": "χορωδία — choir", "εμπνευσμένα": "εμπνευσμένος — inspired", "περιορισμένες": "περιορισμένος — limited", "συνιστάται": "συνιστάται — it is advised", "κράτηση": "κράτηση — booking", "τακούνια": "τακούνι — (high) heel", "φθορές": "φθορά — damage, wear", "φακό": "φακός — torch, flashlight", "μονοπάτια": "μονοπάτι — path"}
})

ITEMS.append({
 "id": "l130-vm-ktiniatros-emvolia", "title": "Μήνυμα από την κτηνίατρο για τα εμβόλια", "title_en": "A message from the vet about vaccinations", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε έναν σκύλο. Ακούτε ένα μήνυμα από την κτηνίατρο στον τηλεφωνητή σας.",
 "script": [
  L("Κτηνίατρος", "f", "Καλημέρα σας, η Μυρτώ είμαι από το κτηνιατρείο. Σας παίρνω για να σας θυμίσω ότι ο Ρεξ πρέπει να κάνει την ετήσια αναμνηστική δόση του εμβολίου μέχρι το τέλος του μήνα. Είδα στο βιβλιάριό του ότι η προηγούμενη έγινε τον Νοέμβριο της περασμένης χρονιάς.", "Good morning, it's Myrto from the veterinary clinic. I'm calling to remind you that Rex needs his annual booster vaccination by the end of the month. I saw in his health book that the previous one was done last November."),
  L("Κτηνίατρος", "f", "Αν θέλετε, την ίδια μέρα μπορούμε να κάνουμε και το τεστ για τη λεϊσμανίαση, που το συστήνουμε κάθε χρόνο, γιατί η ασθένεια είναι συχνή στην Ελλάδα. Για το τεστ ο σκύλος δεν χρειάζεται να είναι νηστικός.", "If you like, the same day we can also do the leishmaniasis test, which we recommend every year because the disease is common in Greece. The dog doesn't need to have fasted for the test."),
  L("Κτηνίατρος", "f", "Το κτηνιατρείο είναι ανοιχτό καθημερινά από τις εννιά ως τις δύο και από τις πέντε ως τις εννιά. Φέρτε μαζί σας και το βιβλιάριο υγείας, για να το ενημερώσουμε. Ευχαριστώ, καλή σας μέρα!", "The clinic is open daily from nine to two and from five to nine. Please also bring the health book so we can update it. Thank you, have a good day!"),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί η κτηνίατρος;", ["Γιατί ο Ρεξ είναι άρρωστος", "Για να θυμίσει την ετήσια αναμνηστική δόση του εμβολίου", "Για να αλλάξει ένα ραντεβού", "Για να ζητήσει πληρωμή"], 1, "πρέπει να κάνει την ετήσια αναμνηστική δόση του εμβολίου"),
  Q("Τι άλλο προτείνει να γίνει την ίδια μέρα;", ["Κούρεμα", "Καθαρισμός δοντιών", "Τεστ για τη λεϊσμανίαση", "Στείρωση"], 2, "μπορούμε να κάνουμε και το τεστ για τη λεϊσμανίαση"),
  Q("Τι πρέπει να φέρει ο ιδιοκτήτης;", ["Το βιβλιάριο υγείας του σκύλου", "Ένα δείγμα τροφής", "Τη συνταγή του γιατρού", "Μετρητά μόνο"], 0, "Φέρτε μαζί σας και το βιβλιάριο υγείας"),
 ],
 "gloss": {"κτηνίατρο": "κτηνίατρος — vet", "κτηνιατρείο": "κτηνιατρείο — veterinary clinic", "ετήσια": "ετήσιος — annual", "αναμνηστική δόση": "αναμνηστική δόση — booster dose", "βιβλιάριό": "βιβλιάριο υγείας — health book (record)", "λεϊσμανίαση": "λεϊσμανίαση — leishmaniasis", "συστήνουμε": "συστήνω — to recommend", "ασθένεια": "ασθένεια — disease", "νηστικός": "νηστικός — having not eaten, fasting", "ενημερώσουμε": "ενημερώνω — to update, inform"}
})

ITEMS.append({
 "id": "l130-dial-piano-kithara", "title": "Πιάνο ή κιθάρα για τη μικρή;", "title_en": "Piano or guitar for our daughter?", "type": "dialogue", "level": "B2",
 "context_el": "Η Νεφέλη και ο Αντρέας συζητούν σε ποιο μουσικό όργανο να γράψουν την κόρη τους, την Άννα, που είναι εννιά χρονών.",
 "script": [
  L("Νεφέλη", "f", "Αντρέα, η Άννα μού είπε πάλι ότι θέλει να μάθει μουσική. Σκέφτομαι το πιάνο. Λένε ότι είναι το καλύτερο όργανο για να μάθει κανείς τις βάσεις, να διαβάζει νότες, να καταλαβαίνει την αρμονία.", "Andreas, Anna told me again she wants to learn music. I'm thinking piano. They say it's the best instrument for learning the basics, reading music, understanding harmony."),
  L("Αντρέας", "m", "Μπορεί, αλλά πού θα το βάλουμε; Το σαλόνι είναι γεμάτο, και ένα καλό πιάνο κοστίζει μια περιουσία. Και τα ηλεκτρικά δεν είναι το ίδιο. Η κιθάρα είναι φθηνότερη και την παίρνει μαζί της όπου θέλει, στις κατασκηνώσεις, στις εκδρομές.", "Maybe, but where will we put it? The living room is full, and a good piano costs a fortune. And digital ones aren't the same. A guitar is cheaper and she can take it wherever she wants, to camp, on trips."),
  L("Νεφέλη", "f", "Η καθηγήτρια του ωδείου πάντως μου είπε ότι στην αρχή μπορεί να κάνει μάθημα σε ένα ηλεκτρικό πιάνο, που το νοικιάζει το ίδιο το ωδείο. Αν δούμε ότι επιμένει, αγοράζουμε αργότερα κανονικό.", "Anyway, the teacher at the music school told me that at first she can learn on a digital piano, which the school itself rents out. If we see she sticks with it, we buy a real one later."),
  L("Αντρέας", "m", "Τότε ας ρωτήσουμε την ίδια την Άννα. Ας την πάμε το Σάββατο στη δοκιμαστική μέρα του ωδείου, να δοκιμάσει και τα δύο όργανα, και να διαλέξει μόνη της.", "Then let's ask Anna herself. Let's take her on Saturday to the music school's taster day, so she can try both instruments and choose for herself."),
 ],
 "questions": [
  Q("Γιατί προτιμά η Νεφέλη το πιάνο;", ["Γιατί το παίζει η ίδια", "Γιατί είναι το καλύτερο όργανο για να μάθει κανείς τις βάσεις", "Γιατί το πρότεινε η Άννα", "Γιατί είναι φθηνό"], 1, "είναι το καλύτερο όργανο για να μάθει κανείς τις βάσεις"),
  Q("Ποια λύση πρότεινε η καθηγήτρια του ωδείου;", ["Να αγοράσουν αμέσως ένα πιάνο", "Να ξεκινήσει με κιθάρα", "Να κάνει μάθημα σε ηλεκτρικό πιάνο που νοικιάζει το ωδείο", "Να περιμένουν έναν χρόνο"], 2, "μπορεί να κάνει μάθημα σε ένα ηλεκτρικό πιάνο, που το νοικιάζει το ίδιο το ωδείο"),
  Q("Τι αποφασίζουν στο τέλος;", ["Να πάνε την Άννα στη δοκιμαστική μέρα για να διαλέξει μόνη της", "Να αγοράσουν κιθάρα", "Να αγοράσουν πιάνο", "Να αναβάλουν το θέμα"], 0, "Ας την πάμε το Σάββατο στη δοκιμαστική μέρα του ωδείου"),
 ],
 "gloss": {"όργανο": "μουσικό όργανο — musical instrument", "βάσεις": "βάση — basis; τις βάσεις = the basics", "νότες": "νότα — (musical) note", "αρμονία": "αρμονία — harmony", "περιουσία": "περιουσία — fortune", "κατασκηνώσεις": "κατασκήνωση — (summer) camp", "ωδείου": "ωδείο — music school, conservatory", "επιμένει": "επιμένω — to persist, stick with", "δοκιμαστική": "δοκιμαστικός — trial, taster (adj.)"}
})

ITEMS.append({
 "id": "l130-int-anemogennitries", "title": "Στην κορυφή μιας ανεμογεννήτριας", "title_en": "At the top of a wind turbine", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια ραδιοφωνική συνέντευξη με μια τεχνικό που συντηρεί ανεμογεννήτριες στην Εύβοια.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Δημάκη, πώς είναι μια μέρα δουλειάς πάνω σε μια ανεμογεννήτρια;", "Ms Dimaki, what's a working day like on a wind turbine?"),
  L("Τεχνικός", "f", "Ξεκινάμε πάντα με τον έλεγχο του καιρού. Αν ο άνεμος είναι πάνω από ένα όριο, δεν ανεβαίνουμε. Μετά φοράμε τον εξοπλισμό ασφαλείας και ανεβαίνουμε ογδόντα μέτρα, άλλοτε με ανελκυστήρα και άλλοτε με σκάλα. Δουλεύουμε πάντα σε ζευγάρια, ποτέ μόνοι.", "We always start by checking the weather. If the wind is above a limit, we don't go up. Then we put on the safety gear and climb eighty metres, sometimes by lift and sometimes by ladder. We always work in pairs, never alone."),
  L("Δημοσιογράφος", "m", "Φοβάστε το ύψος;", "Are you afraid of heights?"),
  L("Τεχνικός", "f", "Στην αρχή λίγο, ειδικά όταν φυσάει και ο πύργος κουνιέται ελαφρά. Με τον καιρό όμως το συνηθίζεις. Το πιο κουραστικό δεν είναι το ύψος αλλά ο στενός χώρος μέσα στο κέλυφος, όπου πρέπει να δουλέψεις σκυμμένος για ώρες.", "A little at first, especially when it's windy and the tower sways slightly. But you get used to it over time. The most tiring thing isn't the height but the cramped space inside the housing, where you have to work bent over for hours."),
  L("Δημοσιογράφος", "m", "Και τι σας αρέσει περισσότερο;", "And what do you like most?"),
  L("Τεχνικός", "f", "Η θέα, φυσικά! Τις καθαρές μέρες βλέπω από τη μία πλευρά το Αιγαίο και από την άλλη τα βουνά της Στερεάς. Και νιώθω ότι κάνω κάτι χρήσιμο για το περιβάλλον.", "The view, of course! On clear days I can see the Aegean on one side and the mountains of Central Greece on the other. And I feel I'm doing something useful for the environment."),
 ],
 "questions": [
  Q("Με τι ξεκινά πάντα η δουλειά;", ["Με μια σύσκεψη στο γραφείο", "Με τον έλεγχο του καιρού", "Με ένα πρωινό με τους συναδέλφους", "Με καθαρισμό του πύργου"], 1, "Ξεκινάμε πάντα με τον έλεγχο του καιρού"),
  Q("Τι είναι, κατά την τεχνικό, το πιο κουραστικό;", ["Το ύψος", "Το κρύο", "Ο στενός χώρος μέσα στο κέλυφος", "Τα μεγάλα ταξίδια"], 2, "ο στενός χώρος μέσα στο κέλυφος"),
  Q("Τι της αρέσει περισσότερο;", ["Η θέα και ότι κάνει κάτι χρήσιμο για το περιβάλλον", "Ο μισθός", "Το ωράριο", "Τα ταξίδια στο εξωτερικό"], 0, "Η θέα, φυσικά!"),
 ],
 "gloss": {"ανεμογεννήτρια": "ανεμογεννήτρια — wind turbine", "συντηρεί": "συντηρώ — to maintain", "όριο": "όριο — limit", "εξοπλισμό ασφαλείας": "εξοπλισμός ασφαλείας — safety equipment", "ανελκυστήρα": "ανελκυστήρας — lift", "ύψος": "ύψος — height", "πύργος": "πύργος — tower", "κουνιέται": "κουνιέμαι — to sway, move", "κέλυφος": "κέλυφος — shell, housing", "σκυμμένος": "σκυμμένος — bent over", "θέα": "θέα — view"}
})

ITEMS.append({
 "id": "l130-rep-paralies-xoris-tsigaro", "title": "Παραλίες χωρίς αποτσίγαρα", "title_en": "Beaches free of cigarette butts", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για μια πρωτοβουλία σε ένα νησί των Δωδεκανήσων.",
 "script": [
  L("Ρεπόρτερ", "f", "Σε δέκα παραλίες του νησιού το κάπνισμα απαγορεύεται φέτος για πρώτη φορά. Η απόφαση πάρθηκε από τον δήμο μετά από μια εθελοντική καθαριότητα, κατά την οποία μαζεύτηκαν μέσα σε μία μόνο μέρα πάνω από είκοσι χιλιάδες αποτσίγαρα.", "Smoking is banned on ten of the island's beaches for the first time this year. The council took the decision after a volunteer clean-up during which more than twenty thousand cigarette butts were collected in a single day."),
  L("Περιβαλλοντολόγος", "m", "Πολλοί νομίζουν ότι το αποτσίγαρο είναι χαρτί και λιώνει. Στην πραγματικότητα το φίλτρο είναι από ένα είδος πλαστικού που χρειάζεται χρόνια για να διαλυθεί, και στο μεταξύ απελευθερώνει τοξικές ουσίες στην άμμο και στο νερό.", "Many people think a cigarette butt is paper and dissolves. In reality the filter is made of a kind of plastic that takes years to break down, and meanwhile it releases toxic substances into the sand and water."),
  L("Ρεπόρτερ", "f", "Στις παραλίες έχουν τοποθετηθεί πινακίδες και οι ναυαγοσώστες ενημερώνουν τους λουόμενους. Για τους καπνιστές υπάρχουν ειδικοί χώροι λίγα μέτρα πιο πέρα, με σταχτοδοχεία. Οι περισσότεροι επισκέπτες, όπως μας είπαν, δέχτηκαν το μέτρο με ικανοποίηση.", "Signs have been put up on the beaches and lifeguards inform bathers. For smokers there are special areas a few metres away, with ashtrays. Most visitors, they told us, welcomed the measure."),
 ],
 "questions": [
  Q("Τι οδήγησε τον δήμο στην απόφαση;", ["Παράπονα από ξενοδόχους", "Μια εθελοντική καθαριότητα όπου μαζεύτηκαν πάνω από είκοσι χιλιάδες αποτσίγαρα", "Ένας νέος νόμος της Ευρωπαϊκής Ένωσης", "Μια πυρκαγιά σε παραλία"], 1, "μετά από μια εθελοντική καθαριότητα"),
  Q("Τι εξηγεί ο περιβαλλοντολόγος για το φίλτρο του τσιγάρου;", ["Ότι είναι από χαρτί και λιώνει γρήγορα", "Ότι είναι ακίνδυνο", "Ότι είναι από ένα είδος πλαστικού και απελευθερώνει τοξικές ουσίες", "Ότι το τρώνε τα ψάρια χωρίς πρόβλημα"], 2, "το φίλτρο είναι από ένα είδος πλαστικού"),
  Q("Τι υπάρχει για τους καπνιστές;", ["Ειδικοί χώροι λίγα μέτρα πιο πέρα, με σταχτοδοχεία", "Τίποτα, πρέπει να φύγουν από την παραλία", "Πρόστιμο μόνο", "Ειδικές ξαπλώστρες"], 0, "Για τους καπνιστές υπάρχουν ειδικοί χώροι λίγα μέτρα πιο πέρα"),
 ],
 "gloss": {"πρωτοβουλία": "πρωτοβουλία — initiative", "κάπνισμα": "κάπνισμα — smoking", "καθαριότητα": "καθαριότητα — clean-up, cleaning", "αποτσίγαρα": "αποτσίγαρο — cigarette butt", "λιώνει": "λιώνω — to melt, dissolve", "φίλτρο": "φίλτρο — filter", "διαλυθεί": "διαλύομαι — to break down", "τοξικές ουσίες": "τοξική ουσία — toxic substance", "πινακίδες": "πινακίδα — sign", "λουόμενους": "λουόμενος — bather", "καπνιστές": "καπνιστής — smoker", "σταχτοδοχεία": "σταχτοδοχείο — ashtray"}
})

ITEMS.append({
 "id": "l130-rep-koinotikos-fournos", "title": "Ο κοινοτικός φούρνος ξανανάβει", "title_en": "The village oven is lit again", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα χωριό της Ηπείρου όπου ξαναλειτουργεί ο παλιός κοινοτικός φούρνος.",
 "script": [
  L("Ρεπόρτερ", "m", "Στην πλατεία του χωριού υπάρχει ένας πέτρινος φούρνος, που χτίστηκε πριν από περίπου εκατό χρόνια. Παλιά οι νοικοκυρές έφερναν εκεί το ζυμάρι τους και έψηναν με τη σειρά το ψωμί της εβδομάδας. Τα τελευταία σαράντα χρόνια ο φούρνος έμενε σβηστός.", "In the village square there's a stone oven, built about a hundred years ago. In the old days housewives brought their dough there and baked the week's bread in turn. For the last forty years the oven had stood cold."),
  L("Κάτοικος", "f", "Πέρσι ο πολιτιστικός σύλλογος τον επισκεύασε, με τη βοήθεια ενός μάστορα από τα Γιάννενα. Τώρα κάθε Σάββατο τον ανάβουμε από τις έξι το πρωί. Όποιος θέλει φέρνει το ταψί του, πίτες, φαγητά, ψωμί, και τα ψήνουμε όλα μαζί.", "Last year the cultural association repaired it, with the help of a builder from Ioannina. Now every Saturday we light it from six in the morning. Anyone who wants brings their baking tray, pies, dishes, bread, and we bake everything together."),
  L("Ρεπόρτερ", "m", "Το Σάββατο έχει γίνει πια μια μικρή γιορτή. Έρχονται κάτοικοι από τα γύρω χωριά, ακόμη και επισκέπτες από την πόλη. Οι ηλικιωμένες μαθαίνουν στις νεότερες τα μυστικά του προζυμιού, και ο σύλλογος σκέφτεται να οργανώσει και μαθήματα για σχολεία.", "Saturday has now become a small festival. People come from the surrounding villages, even visitors from the town. The older women teach the younger ones the secrets of sourdough, and the association is thinking of organising lessons for schools too."),
 ],
 "questions": [
  Q("Τι έκαναν παλιά οι νοικοκυρές στον φούρνο;", ["Πουλούσαν ψωμί", "Έψηναν με τη σειρά το ψωμί της εβδομάδας", "Μαγείρευαν για τις γιορτές μόνο", "Έψηναν κάστανα"], 1, "έψηναν με τη σειρά το ψωμί της εβδομάδας"),
  Q("Ποιος επισκεύασε τον φούρνο;", ["Ο δήμος", "Ένας φούρναρης", "Ο πολιτιστικός σύλλογος με τη βοήθεια ενός μάστορα", "Οι μαθητές του σχολείου"], 2, "ο πολιτιστικός σύλλογος τον επισκεύασε"),
  Q("Τι μαθαίνουν οι νεότερες από τις ηλικιωμένες;", ["Τα μυστικά του προζυμιού", "Παραδοσιακούς χορούς", "Πώς να χτίζουν φούρνους", "Τραγούδια του χωριού"], 0, "Οι ηλικιωμένες μαθαίνουν στις νεότερες τα μυστικά του προζυμιού"),
 ],
 "gloss": {"κοινοτικός": "κοινοτικός — communal, village (adj.)", "ξαναλειτουργεί": "ξαναλειτουργώ — to work again", "πέτρινος": "πέτρινος — stone (adj.)", "νοικοκυρές": "νοικοκυρά — housewife", "ζυμάρι": "ζυμάρι — dough", "σβηστός": "σβηστός — unlit, out", "μάστορα": "μάστορας — craftsman, builder", "ταψί": "ταψί — baking tray", "προζυμιού": "προζύμι — sourdough starter"}
})

ITEMS.append({
 "id": "l130-mono-syntaxiouxos", "title": "Η πρώτη μου εβδομάδα ως συνταξιούχος", "title_en": "My first week as a pensioner", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλά σε μια ραδιοφωνική εκπομπή για τη ζωή μετά τη σύνταξη.",
 "script": [
  L("Γιάννης", "m", "Δούλεψα τριάντα πέντε χρόνια σε τράπεζα. Όλοι μου έλεγαν: «Τι ωραία, θα ξεκουραστείς!» Την πρώτη Δευτέρα όμως ξύπνησα στις έξι και μισή, όπως πάντα, φόρεσα σχεδόν το κοστούμι μου και μετά κάθισα στην κουζίνα και δεν ήξερα τι να κάνω.", "I worked thirty-five years in a bank. Everyone told me: 'How nice, you'll get some rest!' But the first Monday I woke up at half past six as always, almost put on my suit, and then sat in the kitchen not knowing what to do."),
  L("Γιάννης", "m", "Τις πρώτες μέρες τριγύριζα στο σπίτι και η γυναίκα μου άρχισε να εκνευρίζεται, γιατί της έλεγα πώς να τακτοποιεί τα ντουλάπια. Στο τέλος μου είπε, με χιούμορ αλλά σοβαρά: «Γιάννη, βρες κάτι να κάνεις έξω από το σπίτι.»", "For the first few days I wandered around the house, and my wife started getting irritated because I was telling her how to arrange the cupboards. In the end she told me, with humour but seriously: 'Yiannis, find something to do outside the house.'"),
  L("Γιάννης", "m", "Έτσι γράφτηκα εθελοντής σε μια οργάνωση που βοηθά μικρές επιχειρήσεις με τα οικονομικά τους. Πηγαίνω δύο πρωινά την εβδομάδα, και νιώθω πάλι χρήσιμος. Τα απογεύματα κάνω μαθήματα ιστορίας στο Ανοιχτό Πανεπιστήμιο του δήμου. Η σύνταξη, τελικά, δεν είναι το τέλος· είναι μια άλλη αρχή.", "So I signed up as a volunteer with an organisation that helps small businesses with their finances. I go two mornings a week and feel useful again. In the afternoons I take history classes at the council's Open University. Retirement, in the end, isn't the end; it's another beginning."),
 ],
 "questions": [
  Q("Τι έγινε την πρώτη Δευτέρα της σύνταξης;", ["Έφυγε για ταξίδι", "Ξύπνησε νωρίς όπως πάντα και δεν ήξερε τι να κάνει", "Κοιμήθηκε μέχρι το μεσημέρι", "Πήγε στην τράπεζα"], 1, "κάθισα στην κουζίνα και δεν ήξερα τι να κάνω"),
  Q("Γιατί εκνευρίστηκε η γυναίκα του;", ["Γιατί δεν τη βοηθούσε", "Γιατί έβλεπε συνέχεια τηλεόραση", "Γιατί της έλεγε πώς να τακτοποιεί τα ντουλάπια", "Γιατί ξόδευε πολλά χρήματα"], 2, "της έλεγα πώς να τακτοποιεί τα ντουλάπια"),
  Q("Τι κάνει σήμερα ο Γιάννης;", ["Είναι εθελοντής και κάνει μαθήματα ιστορίας", "Δουλεύει πάλι στην τράπεζα", "Έχει ανοίξει δική του επιχείρηση", "Ασχολείται μόνο με τον κήπο"], 0, "γράφτηκα εθελοντής σε μια οργάνωση"),
 ],
 "gloss": {"σύνταξη": "σύνταξη — pension, retirement", "ξεκουραστείς": "ξεκουράζομαι — to rest", "κοστούμι": "κοστούμι — suit", "τριγύριζα": "τριγυρίζω — to wander around", "εκνευρίζεται": "εκνευρίζομαι — to get irritated", "τακτοποιεί": "τακτοποιώ — to tidy, arrange", "ντουλάπια": "ντουλάπι — cupboard", "εθελοντής": "εθελοντής — volunteer", "οικονομικά": "οικονομικά — finances", "χρήσιμος": "χρήσιμος — useful"}
})

ITEMS.append({
 "id": "l130-mono-pazari-vivlion", "title": "Τα βιβλία μου στο κυριακάτικο παζάρι", "title_en": "My books at the Sunday flea market", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια νεαρή γυναίκα να μιλά σε ένα πόντκαστ για ένα ασυνήθιστο χόμπι.",
 "script": [
  L("Ιωάννα", "f", "Κάθε Κυριακή πρωί στήνω έναν πάγκο σε ένα παζάρι μεταχειρισμένων αντικειμένων στο Μοναστηράκι και πουλάω παλιά βιβλία. Όλα ξεκίνησαν όταν μετακόμισα σε ένα μικρό διαμέρισμα και δεν χωρούσαν οι οχτώ κούτες με βιβλία που είχα.", "Every Sunday morning I set up a stall at a second-hand market in Monastiraki and sell old books. It all started when I moved into a small flat and the eight boxes of books I had wouldn't fit."),
  L("Ιωάννα", "f", "Στην αρχή ήθελα απλώς να τα ξεφορτωθώ. Γρήγορα όμως άρχισα να αγοράζω βιβλία από άλλους, σε σπίτια που άδειαζαν ή σε σκουπίδια, και να τα πουλάω φτηνά, συνήθως ένα με δύο ευρώ. Δεν βγάζω πολλά χρήματα· αρκεί να καλύπτω τα έξοδα.", "At first I just wanted to get rid of them. But soon I started buying books from other people, from houses being cleared or from the rubbish, and selling them cheaply, usually for one or two euros. I don't make much money; it's enough to cover my costs."),
  L("Ιωάννα", "f", "Αυτό που αγαπώ περισσότερο είναι οι κουβέντες. Ένας ηλικιωμένος κύριος βρήκε κάποτε στον πάγκο μου ένα βιβλίο με την υπογραφή του πατέρα του στην πρώτη σελίδα. Έκλαψε. Από τότε δεν κρατάω πια λογαριασμό για το πόσα πουλάω.", "What I love most is the conversations. An elderly man once found on my stall a book with his father's signature on the first page. He cried. Since then I don't keep track any more of how much I sell."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε η Ιωάννα να πουλάει βιβλία;", ["Έχασε τη δουλειά της", "Μετακόμισε σε μικρό διαμέρισμα και δεν χωρούσαν τα βιβλία της", "Κληρονόμησε ένα βιβλιοπωλείο", "Της το πρότεινε μια φίλη"], 1, "δεν χωρούσαν οι οχτώ κούτες με βιβλία που είχα"),
  Q("Πόσο πουλάει συνήθως τα βιβλία;", ["Πέντε με δέκα ευρώ", "Τα χαρίζει", "Ένα με δύο ευρώ", "Ανάλογα με την ηλικία του βιβλίου"], 2, "συνήθως ένα με δύο ευρώ"),
  Q("Τι συνέβη με τον ηλικιωμένο κύριο;", ["Βρήκε ένα βιβλίο με την υπογραφή του πατέρα του και έκλαψε", "Αγόρασε όλα τα βιβλία", "Της έδωσε μια συλλογή βιβλίων", "Παραπονέθηκε για τις τιμές"], 0, "βρήκε κάποτε στον πάγκο μου ένα βιβλίο με την υπογραφή του πατέρα του"),
 ],
 "gloss": {"παζάρι": "παζάρι — flea market, bazaar", "χόμπι": "χόμπι — hobby", "στήνω": "στήνω — to set up", "πάγκο": "πάγκος — stall", "μεταχειρισμένων": "μεταχειρισμένος — second-hand", "κούτες": "κούτα — (cardboard) box", "ξεφορτωθώ": "ξεφορτώνομαι — to get rid of", "έξοδα": "έξοδα — expenses, costs", "κουβέντες": "κουβέντα — conversation, chat", "υπογραφή": "υπογραφή — signature", "λογαριασμό": "κρατάω λογαριασμό — to keep count"}
})

ITEMS.append({
 "id": "l130-c1-stroop", "title": "Όταν το χρώμα μπερδεύει τη λέξη", "title_en": "When the colour confuses the word", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια ραδιοφωνική εκπομπή για την ψυχολογία της προσοχής.",
 "script": [
  L("Ομιλήτρια", "f", "Δοκιμάστε κάτι απλό: γράψτε τη λέξη «κόκκινο» με πράσινο μελάνι και ζητήστε από έναν φίλο να πει, όσο πιο γρήγορα μπορεί, το χρώμα του μελανιού και όχι τη λέξη. Θα διαπιστώσετε ότι διστάζει ή κάνει λάθος πολύ συχνότερα απ' ό,τι όταν η λέξη και το χρώμα συμφωνούν.", "Try something simple: write the word 'red' in green ink and ask a friend to say, as fast as they can, the colour of the ink and not the word. You'll find that they hesitate or make mistakes much more often than when the word and the colour match."),
  L("Ομιλήτρια", "f", "Το φαινόμενο περιγράφηκε συστηματικά το 1935 από τον Αμερικανό ψυχολόγο Τζον Ρίντλεϊ Στρουπ και φέρει από τότε το όνομά του. Η εξήγηση που δίνεται συνήθως είναι ότι η ανάγνωση έχει γίνει για τους ενήλικες μια σχεδόν αυτόματη διαδικασία, ενώ η ονομασία ενός χρώματος απαιτεί περισσότερη συνειδητή προσπάθεια.", "The phenomenon was described systematically in 1935 by the American psychologist John Ridley Stroop and has borne his name ever since. The explanation usually given is that for adults reading has become an almost automatic process, while naming a colour requires more conscious effort."),
  L("Ομιλήτρια", "f", "Όταν οι δύο πληροφορίες συγκρούονται, ο εγκέφαλος πρέπει να καταστείλει την αυτόματη απάντηση, και αυτό κοστίζει χρόνο. Γι' αυτό η δοκιμασία Στρουπ χρησιμοποιείται ευρέως στην κλινική πράξη, για να εκτιμηθεί η ικανότητα ελέγχου της προσοχής, για παράδειγμα σε ασθενείς μετά από εγκεφαλικό ή σε ηλικιωμένους.", "When the two pieces of information conflict, the brain has to suppress the automatic response, and that costs time. That's why the Stroop test is widely used in clinical practice to assess the ability to control attention, for example in patients after a stroke or in older people."),
  L("Ομιλήτρια", "f", "Ενδιαφέρον παρουσιάζει και το εξής: τα παιδιά που μόλις μαθαίνουν να διαβάζουν επηρεάζονται λιγότερο, ακριβώς επειδή η ανάγνωση δεν έχει ακόμη αυτοματοποιηθεί. Με άλλα λόγια, αυτό που μας μπερδεύει είναι, παραδόξως, μια δεξιότητα που κατακτήσαμε πολύ καλά.", "Also interesting is this: children who are just learning to read are less affected, precisely because reading has not yet become automatic. In other words, what confuses us is, paradoxically, a skill we have mastered very well."),
 ],
 "questions": [
  Q("Τι συμβαίνει όταν η λέξη και το χρώμα του μελανιού δεν συμφωνούν;", ["Ο φίλος απαντά πιο γρήγορα", "Ο φίλος διστάζει ή κάνει λάθος πιο συχνά", "Ο φίλος δεν βλέπει το χρώμα", "Δεν αλλάζει τίποτα"], 1, "Θα διαπιστώσετε ότι διστάζει ή κάνει λάθος πολύ συχνότερα"),
  Q("Ποια είναι η συνηθισμένη εξήγηση του φαινομένου;", ["Ότι τα χρώματα κουράζουν τα μάτια", "Ότι οι ενήλικες δεν ξέρουν καλά τα χρώματα", "Ότι η ανάγνωση είναι σχεδόν αυτόματη, ενώ η ονομασία χρώματος απαιτεί προσπάθεια", "Ότι το πράσινο μελάνι διαβάζεται δύσκολα"], 2, "η ανάγνωση έχει γίνει για τους ενήλικες μια σχεδόν αυτόματη διαδικασία"),
  Q("Πού χρησιμοποιείται η δοκιμασία Στρουπ;", ["Στην κλινική πράξη, για να εκτιμηθεί ο έλεγχος της προσοχής", "Στα σχολεία, για να μάθουν τα παιδιά χρώματα", "Στη διαφήμιση", "Στην εκπαίδευση πιλότων μόνο"], 0, "χρησιμοποιείται ευρέως στην κλινική πράξη"),
  Q("Γιατί τα παιδιά που μόλις μαθαίνουν να διαβάζουν επηρεάζονται λιγότερο;", ["Γιατί βλέπουν καλύτερα τα χρώματα", "Γιατί η ανάγνωση δεν έχει ακόμη αυτοματοποιηθεί", "Γιατί συγκεντρώνονται περισσότερο", "Γιατί δεν καταλαβαίνουν την οδηγία"], 1, "η ανάγνωση δεν έχει ακόμη αυτοματοποιηθεί"),
 ],
 "gloss": {"μελάνι": "μελάνι — ink", "διστάζει": "διστάζω — to hesitate", "συστηματικά": "συστηματικά — systematically", "ανάγνωση": "ανάγνωση — reading", "ονομασία": "ονομασία — naming", "συνειδητή": "συνειδητός — conscious", "συγκρούονται": "συγκρούομαι — to clash, conflict", "καταστείλει": "καταστέλλω — to suppress", "δοκιμασία": "δοκιμασία — test", "κλινική πράξη": "κλινική πράξη — clinical practice", "εκτιμηθεί": "εκτιμώμαι — to be assessed", "εγκεφαλικό": "εγκεφαλικό — stroke", "αυτοματοποιηθεί": "αυτοματοποιούμαι — to become automatic", "δεξιότητα": "δεξιότητα — skill", "κατακτήσαμε": "κατακτώ — to master, conquer"}
})

ITEMS.append({
 "id": "l130-c1-visvizi", "title": "Δόμνα Βισβίζη, η καπετάνισσα της Θράκης", "title_en": "Domna Visvizi, the woman captain from Thrace", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με έναν ιστορικό για τη Δόμνα Βισβίζη, μια από τις γυναίκες του Αγώνα του 1821.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Παπαθανασίου, η Δόμνα Βισβίζη είναι πολύ λιγότερο γνωστή από την Μπουμπουλίνα. Ποια ήταν;", "Mr Papathanasiou, Domna Visvizi is much less well known than Bouboulina. Who was she?"),
  L("Ιστορικός", "m", "Σύμφωνα με τις περισσότερες πηγές, γεννήθηκε στη Χίο γύρω στο 1783 και παντρεύτηκε στην Αίνο της Ανατολικής Θράκης τον Αντώνιο Βισβίζη, έναν πλούσιο πλοιοκτήτη και μέλος της Φιλικής Εταιρείας. Όταν ξέσπασε η Επανάσταση, το ζευγάρι εξόπλισε το δικό του πλοίο, την «Καλομοίρα», και έπλευσε νότια για να ενωθεί με τον ελληνικό στόλο.", "According to most sources, she was born on Chios around 1783 and married, in Ainos in Eastern Thrace, Antonios Visvizis, a wealthy shipowner and member of the Filiki Etaireia. When the Revolution broke out, the couple armed their own ship, the Kalomoira, and sailed south to join the Greek fleet."),
  L("Δημοσιογράφος", "f", "Και πώς βρέθηκε η ίδια επικεφαλής του πλοίου;", "And how did she herself end up in command of the ship?"),
  L("Ιστορικός", "m", "Το καλοκαίρι του 1822 ο άντρας της σκοτώθηκε σε μια επιχείρηση κοντά στην Εύβοια, κατά την παράδοση μπροστά στα μάτια της. Αντί να αποσυρθεί, ανέλαβε η ίδια τη διοίκηση του πλοίου και του πληρώματος και συνέχισε να πολεμά, πληρώνοντας τα έξοδα από τη δική της περιουσία. Όταν τα χρήματα τελείωσαν, το 1824 παραχώρησε την «Καλομοίρα» στον εθνικό στόλο, όπου, σύμφωνα με τις πηγές, μετατράπηκε σε πυρπολικό.", "In summer 1822 her husband was killed in an operation near Euboea, according to tradition before her eyes. Instead of withdrawing, she took command of the ship and crew herself and carried on fighting, paying the costs out of her own fortune. When the money ran out, in 1824 she handed the Kalomoira over to the national fleet, where, according to the sources, it was converted into a fireship."),
  L("Δημοσιογράφος", "f", "Πώς έζησε μετά τον Αγώνα;", "How did she live after the war?"),
  L("Ιστορικός", "m", "Δυστυχώς, όπως και άλλες ηρωίδες της εποχής, σε μεγάλη φτώχεια. Ζήτησε επανειλημμένα βοήθεια από το κράτος και της δόθηκε τελικά ένα πολύ μικρό μηνιαίο επίδομα. Πέθανε το 1850 στον Πειραιά. Σήμερα υπάρχει άγαλμά της στην Αλεξανδρούπολη, μια καθυστερημένη αναγνώριση μιας γυναίκας που έδωσε κυριολεκτικά ό,τι είχε.", "Sadly, like other heroines of the period, in great poverty. She repeatedly asked the state for help and was finally given a very small monthly allowance. She died in 1850 in Piraeus. Today there is a statue of her in Alexandroupoli, a belated recognition of a woman who literally gave everything she had."),
 ],
 "questions": [
  Q("Τι έκανε το ζευγάρι Βισβίζη όταν ξέσπασε η Επανάσταση;", ["Μετακόμισε στη Ρωσία", "Εξόπλισε το πλοίο του και έπλευσε για να ενωθεί με τον στόλο", "Πούλησε το πλοίο του", "Έκρυψε την περιουσία του"], 1, "το ζευγάρι εξόπλισε το δικό του πλοίο"),
  Q("Τι έκανε η Δόμνα μετά τον θάνατο του άντρα της;", ["Γύρισε στη Χίο", "Παρέδωσε αμέσως το πλοίο", "Ανέλαβε η ίδια τη διοίκηση του πλοίου και συνέχισε να πολεμά", "Έγινε μοναχή"], 2, "ανέλαβε η ίδια τη διοίκηση του πλοίου και του πληρώματος"),
  Q("Τι απέγινε η «Καλομοίρα» το 1824;", ["Παραχωρήθηκε στον εθνικό στόλο και, κατά τις πηγές, έγινε πυρπολικό", "Βυθίστηκε σε τρικυμία", "Πουλήθηκε σε Άγγλους εμπόρους", "Έγινε μουσείο"], 0, "το 1824 παραχώρησε την «Καλομοίρα» στον εθνικό στόλο"),
  Q("Πώς χαρακτηρίζει ο ιστορικός το άγαλμα στην Αλεξανδρούπολη;", ["Ως υπερβολική τιμή", "Ως καθυστερημένη αναγνώριση", "Ως έργο χωρίς ιστορική αξία", "Ως δώρο της οικογένειάς της"], 1, "μια καθυστερημένη αναγνώριση"),
 ],
 "gloss": {"πηγές": "πηγή — source", "πλοιοκτήτη": "πλοιοκτήτης — shipowner", "ξέσπασε": "ξεσπώ — to break out", "εξόπλισε": "εξοπλίζω — to arm, equip", "έπλευσε": "πλέω — to sail", "επικεφαλής": "επικεφαλής — in command, at the head", "αποσυρθεί": "αποσύρομαι — to withdraw", "διοίκηση": "διοίκηση — command", "πληρώματος": "πλήρωμα — crew", "παραχώρησε": "παραχωρώ — to hand over, cede", "πυρπολικό": "πυρπολικό — fireship", "ηρωίδες": "ηρωίδα — heroine", "επανειλημμένα": "επανειλημμένα — repeatedly", "επίδομα": "επίδομα — allowance", "αναγνώριση": "αναγνώριση — recognition"}
})

rnd = random.Random(130)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-130.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
