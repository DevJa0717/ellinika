# Source for library/listening/listening-229.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l229.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l229-news-paralies-skylon", "title": "Παραλίες για σκύλους και τους ιδιοκτήτες τους", "title_en": "Beaches for dogs and their owners", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο ραδιόφωνο λίγο πριν από την έναρξη της καλοκαιρινής περιόδου.",
 "script": [
  L("Εκφωνητής", "m", "Ένας παραθαλάσσιος δήμος της Αττικής ορίζει φέτος για πρώτη φορά δύο παραλίες όπου θα επιτρέπονται οι σκύλοι. Μέχρι σήμερα, στις περισσότερες οργανωμένες παραλίες τα κατοικίδια απαγορεύονταν, και οι ιδιοκτήτες τους κινδύνευαν με πρόστιμο.", "A seaside municipality in Attica is designating, for the first time this year, two beaches where dogs will be allowed. Until now, pets were banned on most organised beaches, and their owners risked a fine."),
  L("Εκφωνητής", "m", "Στις δύο παραλίες θα υπάρχουν βρύσες με γλυκό νερό, σκιά, σακουλάκια για τις ακαθαρσίες και ειδικοί κάδοι. Οι σκύλοι θα πρέπει να είναι εμβολιασμένοι και να φορούν λουρί όταν κινούνται ανάμεσα στους λουόμενους.", "On the two beaches there will be freshwater taps, shade, bags for droppings and special bins. Dogs will have to be vaccinated and wear a lead when moving among bathers."),
  L("Εκφωνητής", "m", "Η απόφαση προκάλεσε αντιδράσεις. Ορισμένοι κάτοικοι ανησυχούν για την καθαριότητα της άμμου και για τα παιδιά που φοβούνται τα ζώα. Ο δήμος απαντά ότι οι δύο παραλίες είναι μικρές και απομονωμένες, και ότι οι υπόλοιπες δεκαπέντε παραλίες του δήμου μένουν όπως ήταν.", "The decision provoked reactions. Some residents are worried about the cleanliness of the sand and about children who are afraid of animals. The municipality replies that the two beaches are small and isolated, and that the other fifteen beaches in the municipality stay as they were."),
  L("Εκφωνητής", "m", "Σύμφωνα με τον δήμαρχο, ο στόχος είναι και να περιοριστούν τα εγκαταλελειμμένα ζώα. «Κάθε καλοκαίρι», δήλωσε, «κάποιοι αφήνουν τον σκύλο τους στον δρόμο γιατί δεν έχουν πού να τον πάνε στις διακοπές.»", "According to the mayor, the aim is also to reduce the number of abandoned animals. 'Every summer,' he said, 'some people leave their dog on the street because they have nowhere to take it on holiday.'"),
 ],
 "questions": [
  Q("Τι ίσχυε μέχρι σήμερα στις περισσότερες οργανωμένες παραλίες;", ["Οι σκύλοι επιτρέπονταν χωρίς όρους", "Τα κατοικίδια απαγορεύονταν", "Οι σκύλοι επιτρέπονταν μόνο το βράδυ", "Δεν υπήρχαν κανόνες"], 1, "στις περισσότερες οργανωμένες παραλίες τα κατοικίδια απαγορεύονταν"),
  Q("Πότε πρέπει οι σκύλοι να φορούν λουρί;", ["Πάντα, και μέσα στο νερό", "Όταν κινούνται ανάμεσα στους λουόμενους", "Μόνο αν είναι μεγάλοι", "Ποτέ"], 1, "να φορούν λουρί όταν κινούνται ανάμεσα στους λουόμενους"),
  Q("Πώς απαντά ο δήμος στις αντιδράσεις;", ["Ότι θα ακυρώσει την απόφαση", "Ότι οι δύο παραλίες είναι μικρές και απομονωμένες", "Ότι θα επιτρέψει τους σκύλους παντού", "Ότι θα κλείσει τις παραλίες για τα παιδιά"], 1, "οι δύο παραλίες είναι μικρές και απομονωμένες"),
  Q("Ποιος άλλος στόχος αναφέρεται από τον δήμαρχο;", ["Να έρθουν περισσότεροι τουρίστες", "Να περιοριστούν τα εγκαταλελειμμένα ζώα", "Να μαζευτούν χρήματα από πρόστιμα", "Να καθαριστούν οι παραλίες"], 1, "ο στόχος είναι και να περιοριστούν τα εγκαταλελειμμένα ζώα"),
 ],
 "gloss": {"ορίζει": "ορίζω — to designate, set", "κατοικίδια": "κατοικίδιο — pet", "πρόστιμο": "πρόστιμο — fine", "ακαθαρσίες": "ακαθαρσίες — droppings, dirt", "εμβολιασμένοι": "εμβολιασμένος — vaccinated", "λουρί": "λουρί — lead, leash", "λουόμενους": "λουόμενος — bather", "αντιδράσεις": "αντίδραση — reaction", "απομονωμένες": "απομονωμένος — isolated", "εγκαταλελειμμένα": "εγκαταλελειμμένος — abandoned"},
})
ITEMS.append({
 "id": "l229-vm-architektonas", "title": "Μήνυμα από την αρχιτέκτονα για την άδεια", "title_en": "A message from the architect about the permit", "type": "voicemail", "level": "B2",
 "context_el": "Χτίζετε ένα μικρό σπίτι στο χωριό σας. Ακούτε ένα μήνυμα στον τηλεφωνητή σας από την αρχιτέκτονα.",
 "script": [
  L("Αρχιτέκτονας", "f", "Γεια σας, κύριε Ανδρέου, η Χαρά είμαι, η αρχιτέκτονας. Σας τηλεφωνώ για την άδεια δόμησης του σπιτιού στο χωριό, γιατί υπάρχει μια εξέλιξη που δεν περιμέναμε.", "Hello, Mr Andreou, it's Chara, the architect. I'm calling about the building permit for the house in the village, because there's a development we didn't expect."),
  L("Αρχιτέκτονας", "f", "Η πολεοδομία μάς ενημέρωσε ότι το οικόπεδο βρίσκεται κοντά σε μια περιοχή όπου έχουν βρεθεί αρχαία. Αυτό σημαίνει ότι, πριν βγει η άδεια, πρέπει να δώσει τη σύμφωνη γνώμη της η Εφορεία Αρχαιοτήτων. Μην ανησυχείτε, είναι συνηθισμένο στην Ελλάδα και τις περισσότερες φορές δεν βρίσκεται τίποτα.", "The planning office has informed us that the plot is near an area where antiquities have been found. This means that, before the permit is issued, the Ephorate of Antiquities must give its approval. Don't worry, it's common in Greece and most of the time nothing is found."),
  L("Αρχιτέκτονας", "f", "Πιθανότατα θα ζητήσουν μια δοκιμαστική τομή, δηλαδή ένα μικρό σκάψιμο με την παρουσία αρχαιολόγου, στο σημείο όπου θα γίνουν τα θεμέλια. Αυτό καθυστερεί τα πράγματα περίπου δύο με τρεις μήνες, οπότε ο εργολάβος δεν θα μπορέσει να ξεκινήσει τον Μάρτιο όπως λέγαμε.", "They'll most likely ask for a trial trench, that is, a small excavation with an archaeologist present, at the spot where the foundations will go. That delays things by about two to three months, so the builder won't be able to start in March as we'd said."),
  L("Αρχιτέκτονας", "f", "Θα ήθελα να τα πούμε από κοντά την Πέμπτη, για να ενημερώσουμε μαζί και τον εργολάβο. Αν δεν μπορείτε, στείλτε μου ένα μήνυμα να βρούμε άλλη μέρα. Καλή συνέχεια!", "I'd like to talk in person on Thursday, so we can update the builder together too. If you can't, send me a message and we'll find another day. All the best!"),
 ],
 "questions": [
  Q("Γιατί χρειάζεται η γνώμη της Εφορείας Αρχαιοτήτων;", ["Γιατί το σπίτι είναι πολύ μεγάλο", "Γιατί το οικόπεδο είναι κοντά σε περιοχή όπου βρέθηκαν αρχαία", "Γιατί ο εργολάβος δεν έχει άδεια", "Γιατί το σπίτι είναι παραδοσιακό"], 1, "το οικόπεδο βρίσκεται κοντά σε μια περιοχή όπου έχουν βρεθεί αρχαία"),
  Q("Τι λέει η αρχιτέκτονας για να ηρεμήσει τον πελάτη;", ["Ότι η διαδικασία είναι συνηθισμένη και συνήθως δεν βρίσκεται τίποτα", "Ότι θα πληρώσει η ίδια τα έξοδα", "Ότι η άδεια έχει ήδη βγει", "Ότι μπορεί να χτίσει αλλού"], 0, "είναι συνηθισμένο στην Ελλάδα και τις περισσότερες φορές δεν βρίσκεται τίποτα"),
  Q("Τι είναι η «δοκιμαστική τομή»;", ["Ένα σχέδιο του σπιτιού", "Ένα μικρό σκάψιμο με την παρουσία αρχαιολόγου", "Μια μελέτη για το κόστος", "Ένας έλεγχος της στέγης"], 1, "ένα μικρό σκάψιμο με την παρουσία αρχαιολόγου"),
  Q("Ποια είναι η συνέπεια για το χρονοδιάγραμμα;", ["Καμία", "Καθυστέρηση περίπου δύο με τρεις μήνες", "Καθυστέρηση ενός χρόνου", "Οι εργασίες θα ξεκινήσουν νωρίτερα"], 1, "Αυτό καθυστερεί τα πράγματα περίπου δύο με τρεις μήνες"),
 ],
 "gloss": {"άδεια δόμησης": "άδεια δόμησης — building permit", "εξέλιξη": "εξέλιξη — development", "πολεοδομία": "πολεοδομία — planning office", "οικόπεδο": "οικόπεδο — building plot", "σύμφωνη γνώμη": "σύμφωνη γνώμη — approval, consent", "Εφορεία Αρχαιοτήτων": "Εφορεία Αρχαιοτήτων — Ephorate (regional office) of Antiquities", "δοκιμαστική τομή": "δοκιμαστική τομή — trial trench", "θεμέλια": "θεμέλια — foundations", "εργολάβος": "εργολάβος — building contractor"},
})
ITEMS.append({
 "id": "l229-c1-mono-magikos-arithmos", "title": "Ο «μαγικός αριθμός επτά» και τα όρια της μνήμης", "title_en": "The 'magical number seven' and the limits of memory", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ραδιοφωνική εκπομπή για την ψυχολογία της καθημερινής ζωής.",
 "script": [
  L("Ομιλήτρια", "f", "Το 1956 ο Αμερικανός ψυχολόγος Τζορτζ Μίλερ δημοσίευσε ένα άρθρο με έναν από τους πιο διάσημους τίτλους στην ιστορία της ψυχολογίας: «Ο μαγικός αριθμός επτά, συν ή πλην δύο». Υποστήριζε ότι μπορούμε να κρατήσουμε στο μυαλό μας ταυτόχρονα περίπου επτά στοιχεία, όπως ψηφία, λέξεις ή γράμματα.", "In 1956 the American psychologist George Miller published an article with one of the most famous titles in the history of psychology: 'The magical number seven, plus or minus two'. He argued that we can hold roughly seven items in mind at once, such as digits, words or letters."),
  L("Ομιλήτρια", "f", "Η ιδέα έγινε τόσο δημοφιλής που συχνά ακούμε ότι γι' αυτό οι αριθμοί τηλεφώνου είχαν παλιά επτά ψηφία. Η σύνδεση αυτή, όμως, είναι μάλλον μύθος. Και, το σημαντικότερο, νεότερες έρευνες δείχνουν ότι ο πραγματικός αριθμός είναι μικρότερος: όταν δεν μπορούμε να επαναλαμβάνουμε τα στοιχεία από μέσα μας, συγκρατούμε συνήθως γύρω στα τέσσερα.", "The idea became so popular that we often hear this is why telephone numbers used to have seven digits. That link, however, is probably a myth. And, more importantly, later research suggests the real number is smaller: when we can't rehearse the items silently, we usually retain around four."),
  L("Ομιλήτρια", "f", "Πώς τότε θυμόμαστε έναν δεκαψήφιο αριθμό κινητού; Με ένα κόλπο που ο ίδιος ο Μίλερ είχε περιγράψει: την ομαδοποίηση. Δεν θυμόμαστε δέκα χωριστά ψηφία, αλλά τρία ή τέσσερα κομμάτια. Ένας σκακιστής δεν βλέπει είκοσι πιόνια· βλέπει μερικούς γνώριμους σχηματισμούς.", "So how do we remember a ten-digit mobile number? With a trick Miller himself had described: chunking. We don't remember ten separate digits, but three or four chunks. A chess player doesn't see twenty pieces; he sees a few familiar patterns."),
  L("Ομιλήτρια", "f", "Το πρακτικό δίδαγμα είναι απλό. Αν θέλετε να σας θυμηθούν, σε μια παρουσίαση ή σε ένα μάθημα, μην παρουσιάζετε δώδεκα σημεία. Ομαδοποιήστε τα σε τρία ή τέσσερα. Η μνήμη μας δεν είναι μια αποθήκη χωρίς τέλος· είναι ένα μικρό τραπέζι, πάνω στο οποίο χωράνε λίγα πράγματα κάθε φορά.", "The practical lesson is simple. If you want people to remember you, in a presentation or a lesson, don't present twelve points. Group them into three or four. Our memory isn't an endless warehouse; it's a small table that holds only a few things at a time."),
 ],
 "questions": [
  Q("Τι υποστήριζε ο Μίλερ το 1956;", ["Ότι η μνήμη δεν έχει όρια", "Ότι κρατάμε στο μυαλό μας ταυτόχρονα περίπου επτά στοιχεία", "Ότι θυμόμαστε καλύτερα τους αριθμούς από τις λέξεις", "Ότι η μνήμη χειροτερεύει μετά τα επτά χρόνια"], 1, "μπορούμε να κρατήσουμε στο μυαλό μας ταυτόχρονα περίπου επτά στοιχεία"),
  Q("Τι λέει η ομιλήτρια για τους επταψήφιους αριθμούς τηλεφώνου;", ["Ότι σχεδιάστηκαν με βάση το άρθρο του Μίλερ", "Ότι η σύνδεσή τους με τον Μίλερ είναι μάλλον μύθος", "Ότι ήταν πιο εύκολοι από τους σημερινούς", "Ότι υπάρχουν ακόμη σε όλες τις χώρες"], 1, "Η σύνδεση αυτή, όμως, είναι μάλλον μύθος"),
  Q("Τι δείχνουν οι νεότερες έρευνες;", ["Ότι ο αριθμός είναι μεγαλύτερος, γύρω στα δέκα", "Ότι ο αριθμός είναι μικρότερος, γύρω στα τέσσερα", "Ότι ο Μίλερ είχε απόλυτο δίκιο", "Ότι η μνήμη διαφέρει μόνο ανάλογα με την ηλικία"], 1, "συγκρατούμε συνήθως γύρω στα τέσσερα"),
  Q("Ποια συμβουλή δίνει για μια παρουσίαση;", ["Να παρουσιάζουμε όσο περισσότερα σημεία γίνεται", "Να μιλάμε πιο αργά", "Να ομαδοποιούμε τα σημεία σε τρία ή τέσσερα", "Να μοιράζουμε σημειώσεις"], 2, "Ομαδοποιήστε τα σε τρία ή τέσσερα"),
 ],
 "gloss": {"ταυτόχρονα": "ταυτόχρονα — at the same time", "ψηφία": "ψηφίο — digit", "δημοφιλής": "δημοφιλής — popular", "συγκρατούμε": "συγκρατώ — to retain, hold", "δεκαψήφιο": "δεκαψήφιος — ten-digit", "ομαδοποίηση": "ομαδοποίηση — grouping, chunking", "σκακιστής": "σκακιστής — chess player", "πιόνια": "πιόνι — (chess) piece", "σχηματισμούς": "σχηματισμός — formation, pattern", "δίδαγμα": "δίδαγμα — lesson, moral"},
})
ITEMS.append({
 "id": "l229-c1-int-ergonomos", "title": "Ένας εργονόμος για το κάθισμα, το γραφείο και τη στάση του σώματος", "title_en": "An ergonomist on chairs, desks and posture", "type": "interview", "level": "C1",
 "context_el": "Ένας εργονόμος, ειδικός στον σχεδιασμό χώρων εργασίας, μιλά σε μια ραδιοφωνική εκπομπή για την υγεία στη δουλειά.",
 "script": [
  L("Δημοσιογράφος", "f", "Πολλοί ακροατές μας περνούν οχτώ ώρες μπροστά σε μια οθόνη. Ποια είναι η σωστή στάση του σώματος;", "Many of our listeners spend eight hours in front of a screen. What is the correct posture?"),
  L("Εργονόμος", "m", "Θα σας απογοητεύσω: δεν υπάρχει μία σωστή στάση. Υπάρχουν κάποιες βασικές αρχές, η οθόνη περίπου στο ύψος των ματιών, τα πόδια να πατάνε στο πάτωμα, οι ώμοι χαλαροί. Αλλά ακόμη και η τέλεια στάση γίνεται πρόβλημα αν τη διατηρήσεις για ώρες. Στη δουλειά μας λέμε συχνά ότι η καλύτερη στάση είναι η επόμενη.", "I'll disappoint you: there is no single correct posture. There are some basic principles: the screen roughly at eye level, feet flat on the floor, shoulders relaxed. But even the perfect posture becomes a problem if you hold it for hours. In our line of work we often say that the best posture is the next one."),
  L("Δημοσιογράφος", "f", "Τα γραφεία όπου δουλεύει κανείς όρθιος είναι η λύση;", "Are standing desks the solution?"),
  L("Εργονόμος", "m", "Είναι ένα χρήσιμο εργαλείο, όχι θαύμα. Αν αντικαταστήσεις οχτώ ώρες καθισίματος με οχτώ ώρες ορθοστασίας, απλώς μεταφέρεις τον πόνο από τη μέση στα πόδια. Το ζητούμενο είναι η εναλλαγή. Τα στοιχεία για τα μακροπρόθεσμα οφέλη τους, εξάλλου, είναι ακόμη περιορισμένα, κι εγώ προτιμώ να το λέω ειλικρινά.", "It's a useful tool, not a miracle. If you replace eight hours of sitting with eight hours of standing, you just move the pain from your lower back to your legs. The point is alternation. The evidence for their long-term benefits, moreover, is still limited, and I prefer to say so honestly."),
  L("Δημοσιογράφος", "f", "Τι συμβουλεύετε λοιπόν στις εταιρείες;", "So what do you advise companies?"),
  L("Εργονόμος", "m", "Να μη σταματούν στην αγορά ακριβών καθισμάτων. Η εργονομία δεν είναι μόνο έπιπλα· είναι και ο τρόπος που οργανώνεται η δουλειά. Αν ένας εργαζόμενος έχει τόσο φόρτο που δεν σηκώνεται ούτε για νερό, καμία καρέκλα δεν θα τον σώσει. Μια σύντομη βόλτα κάθε μισή ώρα, ένα τηλεφώνημα που γίνεται όρθιος, μια συνάντηση που γίνεται περπατώντας: αυτά κοστίζουν ελάχιστα και κάνουν μεγάλη διαφορά.", "Not to stop at buying expensive chairs. Ergonomics isn't just furniture; it's also the way work is organised. If an employee has such a workload that he doesn't even get up for water, no chair will save him. A short walk every half hour, a phone call taken standing up, a meeting held while walking: these cost next to nothing and make a big difference."),
 ],
 "questions": [
  Q("Τι εννοεί με τη φράση «η καλύτερη στάση είναι η επόμενη»;", ["Ότι πρέπει να αλλάζουμε συχνά θέση", "Ότι η στάση μας βελτιώνεται με τον χρόνο", "Ότι πρέπει να αγοράσουμε νέα καρέκλα", "Ότι η πρώτη στάση είναι πάντα λάθος"], 0, "ακόμη και η τέλεια στάση γίνεται πρόβλημα αν τη διατηρήσεις για ώρες"),
  Q("Τι πιστεύει για τα γραφεία όπου δουλεύει κανείς όρθιος;", ["Ότι λύνουν οριστικά το πρόβλημα", "Ότι είναι επικίνδυνα", "Ότι είναι χρήσιμα, αλλά το σημαντικό είναι η εναλλαγή", "Ότι είναι πολύ ακριβά για να αξίζουν"], 2, "Το ζητούμενο είναι η εναλλαγή"),
  Q("Πώς περιγράφει τα στοιχεία για τα μακροπρόθεσμα οφέλη τους;", ["Ως πολύ ισχυρά", "Ως ακόμη περιορισμένα", "Ως ανύπαρκτα", "Ως αρνητικά"], 1, "Τα στοιχεία για τα μακροπρόθεσμα οφέλη τους, εξάλλου, είναι ακόμη περιορισμένα"),
  Q("Τι συμβουλεύει τις εταιρείες;", ["Να αγοράζουν τα πιο ακριβά καθίσματα", "Να οργανώνουν τη δουλειά ώστε οι εργαζόμενοι να κινούνται", "Να μειώσουν τις ώρες εργασίας στις τέσσερις", "Να απαγορεύσουν τις συναντήσεις"], 1, "Η εργονομία δεν είναι μόνο έπιπλα· είναι και ο τρόπος που οργανώνεται η δουλειά"),
 ],
 "gloss": {"εργονόμος": "εργονόμος — ergonomist", "απογοητεύσω": "απογοητεύω — to disappoint", "διατηρήσεις": "διατηρώ — to maintain, keep", "ορθοστασίας": "ορθοστασία — standing (for long periods)", "μέση": "μέση — lower back, waist", "ζητούμενο": "ζητούμενο — what matters, the goal", "εναλλαγή": "εναλλαγή — alternation", "μακροπρόθεσμα": "μακροπρόθεσμος — long-term", "οφέλη": "όφελος — benefit", "φόρτο": "φόρτος (εργασίας) — workload"},
})
rnd = random.Random(229)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-229.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
