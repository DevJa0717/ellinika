# Source for library/listening/listening-86.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l86.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l86-ann-stadio", "title": "Ανακοίνωση στο γήπεδο", "title_en": "Announcement at the stadium", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα γήπεδο μπάσκετ, λίγο πριν από την έναρξη ενός αγώνα. Ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνήτρια", "f", "Καλησπέρα σας και καλώς ήρθατε στο κλειστό γήπεδο. Σας ενημερώνουμε ότι, λόγω τεχνικού προβλήματος στον φωτισμό, η έναρξη του αγώνα μετατίθεται κατά είκοσι λεπτά, για τις εννιά και είκοσι. Οι ομάδες θα βγουν για προθέρμανση μόλις αποκατασταθεί η βλάβη.", "Good evening and welcome to the indoor arena. Please note that, because of a technical problem with the lighting, the start of the game is moved back by twenty minutes, to twenty past nine. The teams will come out to warm up as soon as the fault is fixed."),
  L("Εκφωνήτρια", "f", "Υπενθυμίζουμε ότι απαγορεύεται η χρήση φωτοβολίδων και η ρίψη αντικειμένων στον αγωνιστικό χώρο. Οι παραβάτες θα απομακρύνονται από το γήπεδο. Αν χάσετε κάποιο αντικείμενο ή χρειάζεστε ιατρική βοήθεια, απευθυνθείτε στους εθελοντές με τα κίτρινα γιλέκα.", "We remind you that the use of flares and throwing objects onto the court are forbidden. Offenders will be removed from the arena. If you lose something or need medical help, please speak to the volunteers in yellow vests."),
  L("Εκφωνήτρια", "f", "Μετά τον αγώνα, παρακαλούμε τους φιλάθλους της φιλοξενούμενης ομάδας να παραμείνουν στις θέσεις τους για δέκα λεπτά και να αποχωρήσουν από την έξοδο Δ. Το μετρό θα λειτουργεί με έκτακτα δρομολόγια μέχρι τη μία μετά τα μεσάνυχτα. Σας ευχαριστούμε και καλή διασκέδαση!", "After the game, we ask the away team's fans to stay in their seats for ten minutes and to leave by exit D. The metro will run extra trains until one in the morning. Thank you and enjoy the game!"),
 ],
 "questions": [
  Q("Γιατί καθυστερεί ο αγώνας;", ["Γιατί δεν έχει έρθει η μία ομάδα", "Λόγω τεχνικού προβλήματος στον φωτισμό", "Λόγω επεισοδίων στην είσοδο", "Γιατί άργησαν οι διαιτητές"], 1, "λόγω τεχνικού προβλήματος στον φωτισμό"),
  Q("Σε ποιον πρέπει να απευθυνθεί κάποιος που έχασε κάτι;", ["Στο ταμείο", "Στους αστυνομικούς", "Στους εθελοντές με τα κίτρινα γιλέκα", "Στη γραμματεία της ομάδας"], 2, "απευθυνθείτε στους εθελοντές με τα κίτρινα γιλέκα"),
  Q("Τι πρέπει να κάνουν οι φίλαθλοι της φιλοξενούμενης ομάδας μετά τον αγώνα;", ["Να φύγουν αμέσως από την έξοδο Α", "Να περιμένουν δέκα λεπτά και να βγουν από την έξοδο Δ", "Να πάρουν το λεωφορείο της ομάδας", "Να μείνουν μέχρι τη μία"], 1, "να παραμείνουν στις θέσεις τους για δέκα λεπτά"),
 ],
 "gloss": {"γήπεδο": "γήπεδο — stadium, ground", "μεγάφωνα": "μεγάφωνο — loudspeaker", "μετατίθεται": "μετατίθεμαι — to be moved, postponed", "προθέρμανση": "προθέρμανση — warm-up", "αποκατασταθεί": "αποκαθίσταμαι — to be restored, fixed", "βλάβη": "βλάβη — fault, breakdown", "φωτοβολίδων": "φωτοβολίδα — flare", "ρίψη": "ρίψη — throwing", "αγωνιστικό χώρο": "αγωνιστικός χώρος — playing area, court", "παραβάτες": "παραβάτης — offender", "γιλέκα": "γιλέκο — vest", "φιλάθλους": "φίλαθλος — fan, supporter", "φιλοξενούμενης": "φιλοξενούμενη ομάδα — away team"},
})
ITEMS.append({
 "id": "l86-vm-vivlio-kathysterisi", "title": "Ένα βιβλίο που αργεί να επιστραφεί", "title_en": "An overdue library book", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη δημοτική βιβλιοθήκη.",
 "script": [
  L("Βιβλιοθηκονόμος", "m", "Καλημέρα σας, σας τηλεφωνώ από τη Δημοτική Βιβλιοθήκη. Σύμφωνα με το σύστημά μας, έχετε δανειστεί από τις δέκα του προηγούμενου μήνα το βιβλίο «Η ιστορία της Θεσσαλονίκης», που έπρεπε να επιστραφεί πριν από δύο εβδομάδες.", "Good morning, I'm calling from the Municipal Library. According to our system, since the tenth of last month you have had the book 'The History of Thessaloniki' on loan, which should have been returned two weeks ago."),
  L("Βιβλιοθηκονόμος", "m", "Το βιβλίο το έχει κρατήσει μια άλλη αναγνώστρια, που το χρειάζεται για την εργασία της, γι’ αυτό δεν μπορούμε να σας δώσουμε παράταση. Αν το επιστρέψετε μέχρι την Παρασκευή, δεν θα χρεωθείτε πρόστιμο. Μετά την Παρασκευή, το πρόστιμο είναι πενήντα λεπτά για κάθε μέρα καθυστέρησης.", "The book has been reserved by another reader who needs it for her project, so we can't give you an extension. If you return it by Friday, you won't be charged a fine. After Friday, the fine is fifty cents for each day it's late."),
  L("Βιβλιοθηκονόμος", "m", "Αν δεν σας βολεύει το ωράριό μας, μπορείτε να αφήσετε το βιβλίο στο κουτί επιστροφών δίπλα στην κεντρική είσοδο, που είναι ανοιχτό όλο το εικοσιτετράωρο. Για οποιαδήποτε απορία, καλέστε μας στο ίδιο νούμερο. Ευχαριστώ.", "If our opening hours aren't convenient, you can leave the book in the returns box next to the main entrance, which is open twenty-four hours a day. For any questions, call us on the same number. Thank you."),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί η βιβλιοθήκη να δώσει παράταση;", ["Γιατί ο αναγνώστης έχει ήδη πάρει δύο", "Γιατί μια άλλη αναγνώστρια έχει κρατήσει το βιβλίο", "Γιατί το βιβλίο είναι πολύ σπάνιο", "Γιατί η βιβλιοθήκη κλείνει για διακοπές"], 1, "Το βιβλίο το έχει κρατήσει μια άλλη αναγνώστρια"),
  Q("Τι θα συμβεί αν επιστραφεί το βιβλίο μέχρι την Παρασκευή;", ["Θα πληρώσει μισό πρόστιμο", "Δεν θα χρεωθεί πρόστιμο", "Θα χάσει την κάρτα μέλους", "Θα πάρει δώρο ένα βιβλίο"], 1, "δεν θα χρεωθείτε πρόστιμο"),
  Q("Πού μπορεί να αφήσει το βιβλίο εκτός ωραρίου;", ["Στο περίπτερο απέναντι", "Στο κουτί επιστροφών δίπλα στην κεντρική είσοδο", "Στο δημαρχείο", "Σε έναν φύλακα"], 1, "στο κουτί επιστροφών δίπλα στην κεντρική είσοδο"),
 ],
 "gloss": {"τηλεφωνητή": "τηλεφωνητής — answering machine, voicemail", "δανειστεί": "δανείζομαι — to borrow", "επιστραφεί": "επιστρέφομαι — to be returned", "κρατήσει": "κρατάω — to reserve", "αναγνώστρια": "αναγνώστρια — (female) reader", "παράταση": "παράταση — extension", "χρεωθείτε": "χρεώνομαι — to be charged", "πρόστιμο": "πρόστιμο — fine", "καθυστέρησης": "καθυστέρηση — delay", "κουτί επιστροφών": "κουτί επιστροφών — returns box", "εικοσιτετράωρο": "εικοσιτετράωρο — twenty-four hours"},
})
ITEMS.append({
 "id": "l86-dia-skylos-ploio", "title": "Με τον σκύλο στο πλοίο", "title_en": "Taking the dog on the ferry", "type": "dialogue", "level": "B2",
 "context_el": "Μια επιβάτισσα αγοράζει εισιτήρια για τη Νάξο σε ένα ναυτιλιακό πρακτορείο στον Πειραιά.",
 "script": [
  L("Επιβάτισσα", "f", "Καλημέρα. Θα ήθελα δύο εισιτήρια για τη Νάξο το Σάββατο, για μένα και τον άντρα μου. Θα έρθει μαζί μας κι ο σκύλος μας. Τι πρέπει να ξέρω;", "Good morning. I'd like two tickets to Naxos on Saturday, for me and my husband. Our dog is coming with us too. What do I need to know?"),
  L("Πράκτορας", "m", "Τι μέγεθος είναι ο σκύλος; Αν είναι μικρός και χωράει σε κλουβί μεταφοράς, μπορεί να μείνει μαζί σας στους εξωτερικούς χώρους. Μέσα στα σαλόνια, όμως, δεν επιτρέπονται ζώα.", "What size is the dog? If it's small and fits in a carrier, it can stay with you in the outdoor areas. Inside the lounges, though, animals aren't allowed."),
  L("Επιβάτισσα", "f", "Όχι, είναι λαμπραντόρ, ζυγίζει τριάντα κιλά. Σε κλουβί δεν χωράει.", "No, he's a Labrador, he weighs thirty kilos. He won't fit in a carrier."),
  L("Πράκτορας", "m", "Τότε έχετε δύο επιλογές. Ή θα μείνει στα ειδικά κλουβιά του πλοίου, στο κατάστρωμα, ή μπορείτε να κλείσετε μια καμπίνα για κατοικίδια, όπου μένει μαζί σας. Αυτές είναι λίγες, όμως, και το Σάββατο έχει μείνει μόνο μία. Κοστίζει εξήντα ευρώ επιπλέον.", "Then you have two options. Either he stays in the ship's special kennels on deck, or you can book a pet cabin, where he stays with you. There are only a few of those, though, and on Saturday there's only one left. It costs sixty euros extra."),
  L("Επιβάτισσα", "f", "Θα πάρω την καμπίνα. Το ταξίδι είναι έξι ώρες και φοβάται τη φασαρία. Χρειάζεται κάποιο έγγραφο;", "I'll take the cabin. The journey is six hours and he's afraid of noise. Does he need any document?"),
  L("Πράκτορας", "m", "Ναι, το βιβλιάριο υγείας του, με τα εμβόλια σε ισχύ. Και στους κοινόχρηστους χώρους πρέπει να φοράει φίμωτρο και λουρί. Ελέγχεται στην επιβίβαση, οπότε μην το ξεχάσετε.", "Yes, his health booklet, with up-to-date vaccinations. And in the shared areas he has to wear a muzzle and a lead. It's checked at boarding, so don't forget it."),
 ],
 "questions": [
  Q("Γιατί ο σκύλος δεν μπορεί να μείνει σε κλουβί μεταφοράς;", ["Γιατί είναι πολύ μεγάλος", "Γιατί είναι άρρωστος", "Γιατί δεν το επιτρέπει η εταιρεία", "Γιατί η επιβάτισσα δεν έχει κλουβί"], 0, "Σε κλουβί δεν χωράει"),
  Q("Τι διαλέγει τελικά η επιβάτισσα;", ["Τα κλουβιά στο κατάστρωμα", "Να αφήσει τον σκύλο σε φίλους", "Μια καμπίνα για κατοικίδια", "Ένα άλλο πλοίο"], 2, "Θα πάρω την καμπίνα"),
  Q("Τι πρέπει να φοράει ο σκύλος στους κοινόχρηστους χώρους;", ["Ένα γιλέκο", "Φίμωτρο και λουρί", "Μόνο κολάρο", "Τίποτα"], 1, "πρέπει να φοράει φίμωτρο και λουρί"),
 ],
 "gloss": {"ναυτιλιακό πρακτορείο": "ναυτιλιακό πρακτορείο — shipping agency", "κλουβί μεταφοράς": "κλουβί μεταφοράς — pet carrier", "σαλόνια": "σαλόνι — lounge", "ζυγίζει": "ζυγίζω — to weigh", "κατάστρωμα": "κατάστρωμα — deck", "καμπίνα": "καμπίνα — cabin", "κατοικίδια": "κατοικίδιο — pet", "φασαρία": "φασαρία — noise, fuss", "βιβλιάριο υγείας": "βιβλιάριο υγείας — health booklet", "σε ισχύ": "σε ισχύ — valid, in force", "κοινόχρηστους": "κοινόχρηστος — shared, communal", "φίμωτρο": "φίμωτρο — muzzle", "λουρί": "λουρί — lead, leash", "επιβίβαση": "επιβίβαση — boarding"},
})
ITEMS.append({
 "id": "l86-int-taxitzis-nyxtas", "title": "Ταξιτζής της νύχτας", "title_en": "A night taxi driver", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή για τα νυχτερινά επαγγέλματα, ένας δημοσιογράφος μιλά με μια ταξιτζού που δουλεύει μόνο τη νύχτα.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Στέλλα, εδώ και δώδεκα χρόνια οδηγείτε ταξί μόνο τη νύχτα. Γιατί διαλέξατε αυτή τη βάρδια;", "Ms Stella, for twelve years you've driven a taxi only at night. Why did you choose this shift?"),
  L("Στέλλα", "f", "Στην αρχή ήταν ανάγκη. Τα παιδιά μου ήταν μικρά, και έτσι μπορούσα να είμαι σπίτι τη μέρα. Μετά, όμως, το αγάπησα. Η πόλη τη νύχτα είναι άλλη πόλη: δεν έχει κίνηση, δεν έχει κόρνες, και οι άνθρωποι είναι πιο ειλικρινείς.", "At first it was out of necessity. My children were little, and this way I could be at home during the day. But then I came to love it. The city at night is a different city: there's no traffic, no horns, and people are more honest."),
  L("Δημοσιογράφος", "m", "Πιο ειλικρινείς; Τι εννοείτε;", "More honest? What do you mean?"),
  L("Στέλλα", "f", "Τη νύχτα οι πελάτες μιλάνε. Κάποιος γυρίζει από τη βάρδια στο νοσοκομείο και θέλει να πει πώς έχασε έναν ασθενή. Κάποιος άλλος γυρίζει από έναν χωρισμό. Εγώ ακούω. Μερικές φορές νιώθω περισσότερο ψυχολόγος παρά οδηγός.", "At night customers talk. Someone is coming back from a hospital shift and wants to tell how they lost a patient. Someone else is coming back from a break-up. I listen. Sometimes I feel more like a psychologist than a driver."),
  L("Δημοσιογράφος", "m", "Δεν φοβάστε ποτέ, ως γυναίκα μόνη;", "Are you never afraid, as a woman on your own?"),
  L("Στέλλα", "f", "Έχω πάρει τα μέτρα μου. Το ταξί έχει κάμερα και κουμπί κινδύνου, και είμαστε μια ομάδα από ταξιτζήδες που επικοινωνούμε συνέχεια μέσω ασυρμάτου. Σε δώδεκα χρόνια έχω ζήσει μόνο δύο δυσάρεστα περιστατικά. Το πιο δύσκολο, για να πω την αλήθεια, δεν είναι οι πελάτες, αλλά ο ύπνος. Ο οργανισμός δεν συνηθίζει ποτέ εντελώς να κοιμάται τη μέρα.", "I've taken my precautions. The taxi has a camera and a panic button, and we're a group of taxi drivers who are constantly in touch by radio. In twelve years I've had only two unpleasant incidents. The hardest thing, to tell the truth, isn't the customers but sleep. The body never completely gets used to sleeping during the day."),
 ],
 "questions": [
  Q("Γιατί άρχισε η Στέλλα να δουλεύει τη νύχτα;", ["Γιατί κερδίζει περισσότερα", "Για να είναι σπίτι τη μέρα με τα μικρά παιδιά της", "Γιατί δεν της αρέσει ο ήλιος", "Γιατί δεν έβρισκε δουλειά τη μέρα"], 1, "έτσι μπορούσα να είμαι σπίτι τη μέρα"),
  Q("Γιατί λέει ότι μερικές φορές νιώθει ψυχολόγος;", ["Γιατί έχει σπουδάσει ψυχολογία", "Γιατί οι πελάτες τής μιλάνε για τα προβλήματά τους", "Γιατί μεταφέρει γιατρούς", "Γιατί δίνει συμβουλές στους συναδέλφους"], 1, "Τη νύχτα οι πελάτες μιλάνε"),
  Q("Τι είναι το πιο δύσκολο στη δουλειά της, σύμφωνα με την ίδια;", ["Οι επικίνδυνοι πελάτες", "Η κίνηση", "Ο ύπνος τη μέρα", "Η μοναξιά"], 2, "Το πιο δύσκολο, για να πω την αλήθεια, δεν είναι οι πελάτες, αλλά ο ύπνος"),
 ],
 "gloss": {"ταξιτζού": "ταξιτζού — (female) taxi driver", "βάρδια": "βάρδια — shift", "κόρνες": "κόρνα — horn", "ειλικρινείς": "ειλικρινής — honest, sincere", "χωρισμό": "χωρισμός — separation, break-up", "μέτρα": "παίρνω τα μέτρα μου — to take precautions", "κουμπί κινδύνου": "κουμπί κινδύνου — panic button", "ασυρμάτου": "ασύρματος — two-way radio", "περιστατικά": "περιστατικό — incident", "οργανισμός": "οργανισμός — body, organism"},
})
ITEMS.append({
 "id": "l86-rep-limnos", "title": "Η Λήμνος", "title_en": "Lemnos", "type": "report", "level": "B2",
 "context_el": "Σε μια ταξιδιωτική εκπομπή, μια δημοσιογράφος παρουσιάζει τη Λήμνο, στο βόρειο Αιγαίο.",
 "script": [
  L("Δημοσιογράφος", "f", "Η Λήμνος δεν μοιάζει με τα άλλα νησιά του Αιγαίου. Είναι επίπεδη, με χρυσά χωράφια με σιτάρι και χαμηλούς λόφους, και θυμίζει περισσότερο ηπειρωτική πεδιάδα. Σύμφωνα με τη μυθολογία, εδώ έπεσε ο Ήφαιστος, όταν τον πέταξαν από τον Όλυμπο, και εδώ έστησε το εργαστήριό του.", "Lemnos doesn't look like the other islands of the Aegean. It's flat, with golden wheat fields and low hills, and it is more reminiscent of a mainland plain. According to mythology, this is where Hephaestus fell when he was thrown off Olympus, and where he set up his workshop."),
  L("Δημοσιογράφος", "f", "Η πρωτεύουσα, η Μύρινα, απλώνεται κάτω από ένα επιβλητικό κάστρο πάνω σε έναν βράχο. Μέσα στο κάστρο ζουν ελεύθερα ελάφια, που τα βλέπει κανείς συχνά το σούρουπο. Στο βόρειο μέρος του νησιού βρίσκονται οι Αμμοθίνες, αμμόλοφοι που οι ντόπιοι αποκαλούν, με λίγη υπερβολή, «η έρημος της Λήμνου».", "The capital, Myrina, spreads out beneath an imposing castle on a rock. Deer live freely inside the castle, and you can often see them at dusk. In the north of the island are the Ammothines, sand dunes that the locals call, with a little exaggeration, 'the desert of Lemnos'."),
  L("Δημοσιογράφος", "f", "Στην ανατολική ακτή, ο προϊστορικός οικισμός της Πολιόχνης θεωρείται από τους παλαιότερους οργανωμένους οικισμούς της Ευρώπης. Και στον κόλπο του Μούδρου, το 1915, συγκεντρώθηκε ο στόλος των Συμμάχων για την εκστρατεία της Καλλίπολης. Τα στρατιωτικά νεκροταφεία με τους στρατιώτες που σκοτώθηκαν εκεί δέχονται ακόμη επισκέπτες από την Αυστραλία και τη Νέα Ζηλανδία.", "On the east coast, the prehistoric settlement of Poliochni is considered one of the oldest organised settlements in Europe. And in the bay of Moudros, in 1915, the Allied fleet gathered for the Gallipoli campaign. The military cemeteries with the soldiers who died there still receive visitors from Australia and New Zealand."),
 ],
 "questions": [
  Q("Σε τι διαφέρει η Λήμνος από τα άλλα νησιά του Αιγαίου;", ["Έχει ψηλά βουνά", "Είναι επίπεδη, με χωράφια και χαμηλούς λόφους", "Δεν έχει παραλίες", "Είναι πολύ πράσινη και δασωμένη"], 1, "Είναι επίπεδη, με χρυσά χωράφια με σιτάρι και χαμηλούς λόφους"),
  Q("Τι μπορεί να δει κανείς στο κάστρο της Μύρινας;", ["Αρχαία αγάλματα", "Ελεύθερα ελάφια", "Ένα μουσείο του Ηφαίστου", "Έναν φάρο"], 1, "Μέσα στο κάστρο ζουν ελεύθερα ελάφια"),
  Q("Τι συνέβη στον κόλπο του Μούδρου το 1915;", ["Έγινε ένας μεγάλος σεισμός", "Συγκεντρώθηκε ο στόλος των Συμμάχων για την Καλλίπολη", "Βρέθηκε ο οικισμός της Πολιόχνης", "Χτίστηκε το κάστρο"], 1, "συγκεντρώθηκε ο στόλος των Συμμάχων για την εκστρατεία της Καλλίπολης"),
 ],
 "gloss": {"επίπεδη": "επίπεδος — flat", "σιτάρι": "σιτάρι — wheat", "ηπειρωτική": "ηπειρωτικός — mainland", "πεδιάδα": "πεδιάδα — plain", "εργαστήριό": "εργαστήριο — workshop", "επιβλητικό": "επιβλητικός — imposing", "σούρουπο": "σούρουπο — dusk", "αμμόλοφοι": "αμμόλοφος — sand dune", "υπερβολή": "υπερβολή — exaggeration", "έρημος": "έρημος — desert", "οικισμός": "οικισμός — settlement", "κόλπο": "κόλπος — bay, gulf", "στόλος": "στόλος — fleet", "Συμμάχων": "Σύμμαχοι — the Allies", "εκστρατεία": "εκστρατεία — campaign", "νεκροταφεία": "νεκροταφείο — cemetery"},
})
ITEMS.append({
 "id": "l86-rep-chalkida", "title": "Η Χαλκίδα και τα νερά του Ευρίπου", "title_en": "Chalkida and the waters of the Euripus", "type": "report", "level": "B2",
 "context_el": "Σε μια εκπομπή για τις ελληνικές πόλεις, ένας δημοσιογράφος βρίσκεται πάνω στην παλιά γέφυρα της Χαλκίδας.",
 "script": [
  L("Δημοσιογράφος", "m", "Βρίσκομαι πάνω στη γέφυρα που ενώνει την Εύβοια με τη στεριά. Από κάτω περνά ο Εύριπος, ένα στενό κανάλι, πλάτους μόλις σαράντα μέτρων. Αυτό που κάνει τον Εύριπο διάσημο είναι τα ρεύματά του: το νερό αλλάζει κατεύθυνση αρκετές φορές τη μέρα, άλλοτε με κανονικό ρυθμό και άλλοτε τελείως ακανόνιστα.", "I'm standing on the bridge that joins Euboea to the mainland. Underneath runs the Euripus, a narrow channel only forty metres wide. What makes the Euripus famous is its currents: the water changes direction several times a day, sometimes at a regular rhythm and sometimes quite irregularly."),
  L("Δημοσιογράφος", "m", "Το φαινόμενο απασχολούσε τους ανθρώπους από την αρχαιότητα. Σύμφωνα με έναν θρύλο, ο Αριστοτέλης προσπάθησε για καιρό να το εξηγήσει, χωρίς επιτυχία. Σήμερα οι επιστήμονες ξέρουν ότι οφείλεται στις παλίρροιες των δύο κόλπων, βόρεια και νότια της πόλης, που δεν συμπίπτουν.", "The phenomenon has occupied people since antiquity. According to a legend, Aristotle tried for a long time to explain it, without success. Today scientists know that it is due to the tides of the two gulfs, north and south of the town, which don't coincide."),
  L("Δημοσιογράφος", "m", "Η γέφυρα αυτή είναι συρόμενη: τα βράδια, όταν πρέπει να περάσει κάποιο πλοίο, τα δύο κομμάτια της ανοίγουν, και οι περαστικοί μαζεύονται για να δουν το θέαμα. Λίγο πιο πέρα αρχίζει το Κάστρο, η παλιά συνοικία, με το τζαμί, την εκκλησία της Αγίας Παρασκευής και τη συναγωγή μιας από τις παλαιότερες εβραϊκές κοινότητες της Ευρώπης.", "This bridge is a sliding bridge: in the evenings, when a ship needs to pass, its two parts open, and passers-by gather to watch the spectacle. A little further on begins the Kastro, the old quarter, with the mosque, the church of Agia Paraskevi and the synagogue of one of the oldest Jewish communities in Europe."),
 ],
 "questions": [
  Q("Τι κάνει τον Εύριπο διάσημο;", ["Το βάθος του", "Τα ρεύματα που αλλάζουν κατεύθυνση", "Τα ψάρια του", "Το χρώμα του νερού"], 1, "Αυτό που κάνει τον Εύριπο διάσημο είναι τα ρεύματά του"),
  Q("Πώς εξηγούν σήμερα οι επιστήμονες το φαινόμενο;", ["Με τους ανέμους της περιοχής", "Με τις παλίρροιες των δύο κόλπων, που δεν συμπίπτουν", "Με τους σεισμούς", "Με τα πλοία που περνούν"], 1, "οφείλεται στις παλίρροιες των δύο κόλπων"),
  Q("Τι γίνεται τα βράδια στη γέφυρα;", ["Κλείνει για τα αυτοκίνητα για πάντα", "Ανοίγει για να περάσουν πλοία", "Γίνονται συναυλίες", "Φωτίζεται με πολύχρωμα φώτα"], 1, "όταν πρέπει να περάσει κάποιο πλοίο, τα δύο κομμάτια της ανοίγουν"),
 ],
 "gloss": {"στεριά": "στεριά — mainland, dry land", "κανάλι": "κανάλι — channel", "πλάτους": "πλάτος — width", "ρεύματά": "ρεύμα — current", "κατεύθυνση": "κατεύθυνση — direction", "ακανόνιστα": "ακανόνιστα — irregularly", "θρύλο": "θρύλος — legend", "παλίρροιες": "παλίρροια — tide", "συμπίπτουν": "συμπίπτω — to coincide", "συρόμενη": "συρόμενος — sliding", "θέαμα": "θέαμα — spectacle", "τζαμί": "τζαμί — mosque", "συναγωγή": "συναγωγή — synagogue"},
})
ITEMS.append({
 "id": "l86-mono-mythistorima", "title": "Το πρώτο μου μυθιστόρημα", "title_en": "My first novel", "type": "monologue", "level": "B2",
 "context_el": "Σε μια παρουσίαση βιβλίου, ένας καθηγητής μαθηματικών μιλά για το πρώτο του μυθιστόρημα.",
 "script": [
  L("Κώστας", "m", "Πάντα ήθελα να γράψω ένα βιβλίο, αλλά πάντα έβρισκα μια δικαιολογία: τα παιδιά, η δουλειά, η κούραση. Πριν από τέσσερα χρόνια, στα πενήντα μου, αποφάσισα να γράφω κάθε πρωί μία ώρα, πριν πάω στο σχολείο. Ξυπνούσα στις πέντε και μισή, έφτιαχνα καφέ και έγραφα στο τραπέζι της κουζίνας, όσο όλοι κοιμούνταν.", "I always wanted to write a book, but I always found an excuse: the children, work, tiredness. Four years ago, at fifty, I decided to write for an hour every morning before going to school. I'd wake up at half past five, make coffee and write at the kitchen table while everyone was asleep."),
  L("Κώστας", "m", "Η πρώτη εκδοχή ήταν απαίσια. Την έδωσα στη γυναίκα μου, και εκείνη, με μεγάλη ευγένεια, μου είπε ότι δεν κατάλαβε τίποτα μετά το τρίτο κεφάλαιο. Είχε δίκιο. Την ξανάγραψα από την αρχή, και μετά άλλη μία φορά. Έμαθα ότι το γράψιμο είναι κυρίως σβήσιμο.", "The first draft was awful. I gave it to my wife, and she told me, very kindly, that she didn't understand anything after the third chapter. She was right. I rewrote it from the beginning, and then once more. I learnt that writing is mostly crossing out."),
  L("Κώστας", "m", "Το έστειλα σε δώδεκα εκδοτικούς οίκους. Οι δέκα δεν απάντησαν ποτέ, ο ένας μου έστειλε μια ευγενική άρνηση, και ο τελευταίος με πήρε τηλέφωνο έναν Σεπτέμβριο, ενώ διόρθωνα διαγωνίσματα. Το βιβλίο που κρατάτε σήμερα είναι εκείνο. Το μόνο που θα έλεγα σε όποιον θέλει να γράψει είναι αυτό: μην περιμένετε να βρείτε χρόνο. Ο χρόνος δεν βρίσκεται· τον κλέβεις.", "I sent it to twelve publishing houses. Ten never replied, one sent me a polite rejection, and the last one rang me one September while I was marking tests. The book you are holding today is that one. The only thing I'd say to anyone who wants to write is this: don't wait to find time. Time isn't found; you steal it."),
 ],
 "questions": [
  Q("Πότε έγραφε ο Κώστας;", ["Τα βράδια, μετά το σχολείο", "Κάθε πρωί μία ώρα, πριν πάει στο σχολείο", "Μόνο τα καλοκαίρια", "Τα Σαββατοκύριακα"], 1, "αποφάσισα να γράφω κάθε πρωί μία ώρα, πριν πάω στο σχολείο"),
  Q("Τι του είπε η γυναίκα του για την πρώτη εκδοχή;", ["Ότι ήταν υπέροχη", "Ότι δεν κατάλαβε τίποτα μετά το τρίτο κεφάλαιο", "Ότι ήταν πολύ σύντομη", "Ότι έπρεπε να την στείλει αμέσως σε εκδότη"], 1, "δεν κατάλαβε τίποτα μετά το τρίτο κεφάλαιο"),
  Q("Πόσοι εκδοτικοί οίκοι δεν απάντησαν ποτέ;", ["Δώδεκα", "Δέκα", "Ένας", "Κανείς"], 1, "Οι δέκα δεν απάντησαν ποτέ"),
 ],
 "gloss": {"μυθιστόρημα": "μυθιστόρημα — novel", "δικαιολογία": "δικαιολογία — excuse", "κούραση": "κούραση — tiredness", "εκδοχή": "εκδοχή — version, draft", "απαίσια": "απαίσιος — awful", "κεφάλαιο": "κεφάλαιο — chapter", "σβήσιμο": "σβήσιμο — crossing out, erasing", "εκδοτικούς οίκους": "εκδοτικός οίκος — publishing house", "άρνηση": "άρνηση — refusal, rejection", "διαγωνίσματα": "διαγώνισμα — test"},
})
ITEMS.append({
 "id": "l86-mono-ksenodoxeio", "title": "Μεγάλωσα σε ένα ξενοδοχείο", "title_en": "I grew up in a hotel", "type": "monologue", "level": "B2",
 "context_el": "Σε ένα podcast για τα παιδικά χρόνια, μια γυναίκα θυμάται πώς ήταν να μεγαλώνει στο οικογενειακό ξενοδοχείο στη Ρόδο.",
 "script": [
  L("Αλεξάνδρα", "f", "Οι γονείς μου είχαν ένα μικρό ξενοδοχείο με είκοσι δωμάτια στη Ρόδο, και εμείς μέναμε σε δύο από αυτά, στο ισόγειο. Για ένα παιδί ήταν όνειρο: είχαμε πισίνα, μια τεράστια κουζίνα και κάθε εβδομάδα καινούργιους φίλους από όλη την Ευρώπη. Έτσι έμαθα αγγλικά και λίγα γερμανικά πριν πάω σχολείο.", "My parents had a small hotel with twenty rooms in Rhodes, and we lived in two of them, on the ground floor. For a child it was a dream: we had a swimming pool, a huge kitchen and new friends every week from all over Europe. That's how I learnt English and a little German before I went to school."),
  L("Αλεξάνδρα", "f", "Υπήρχε, όμως, και η άλλη πλευρά. Από τον Μάιο μέχρι τον Οκτώβριο οι γονείς μου δούλευαν από το πρωί ως το βράδυ, και εγώ τους έβλεπα ελάχιστα. Δεν κάναμε ποτέ διακοπές το καλοκαίρι· οι διακοπές μας ήταν τον Νοέμβριο, όταν το ξενοδοχείο έκλεινε. Και οι φίλοι μου έφευγαν πάντα μετά από μια εβδομάδα. Θυμάμαι ότι έκλαιγα κάθε Σάββατο, τη μέρα των αναχωρήσεων.", "There was, though, the other side. From May to October my parents worked from morning till night, and I hardly saw them. We never went on holiday in summer; our holidays were in November, when the hotel closed. And my friends always left after a week. I remember crying every Saturday, the day of departures."),
  L("Αλεξάνδρα", "f", "Στα δεκατέσσερα άρχισα να δουλεύω στη ρεσεψιόν. Σήμερα το ξενοδοχείο το διευθύνω εγώ. Οι γονείς μου, που είναι πια συνταξιούχοι, κάθονται κάθε πρωί στην αυλή και πίνουν τον καφέ τους με τους πελάτες, σαν να είναι κι εκείνοι σε διακοπές. Επιτέλους.", "At fourteen I started working at reception. Today I run the hotel. My parents, who are retired now, sit in the courtyard every morning and drink their coffee with the guests, as if they too were on holiday. At last."),
 ],
 "questions": [
  Q("Πώς έμαθε η Αλεξάνδρα ξένες γλώσσες;", ["Σε ένα φροντιστήριο", "Από τους ξένους φίλους που έκανε στο ξενοδοχείο", "Από την τηλεόραση", "Στο σχολείο"], 1, "Έτσι έμαθα αγγλικά και λίγα γερμανικά πριν πάω σχολείο"),
  Q("Πότε έκανε διακοπές η οικογένειά της;", ["Τον Αύγουστο", "Τα Χριστούγεννα", "Τον Νοέμβριο, όταν έκλεινε το ξενοδοχείο", "Ποτέ"], 2, "οι διακοπές μας ήταν τον Νοέμβριο"),
  Q("Γιατί έκλαιγε κάθε Σάββατο;", ["Γιατί έπρεπε να δουλεύει", "Γιατί έφευγαν οι φίλοι της", "Γιατί οι γονείς της έλειπαν", "Γιατί είχε σχολείο"], 1, "έκλαιγα κάθε Σάββατο, τη μέρα των αναχωρήσεων"),
 ],
 "gloss": {"ισόγειο": "ισόγειο — ground floor", "πισίνα": "πισίνα — swimming pool", "ελάχιστα": "ελάχιστα — hardly, very little", "αναχωρήσεων": "αναχώρηση — departure", "ρεσεψιόν": "ρεσεψιόν — reception (desk)", "διευθύνω": "διευθύνω — to run, manage", "συνταξιούχοι": "συνταξιούχος — pensioner, retired person", "Επιτέλους": "επιτέλους — at last"},
})
ITEMS.append({
 "id": "l86-c1-pieso-omadas", "title": "Γιατί συμφωνούμε με την πλειοψηφία;", "title_en": "Why do we go along with the majority?", "type": "interview", "level": "C1",
 "context_el": "Σε μια επιστημονική εκπομπή, μια δημοσιογράφος συζητά με έναν κοινωνικό ψυχολόγο για τα πειράματα συμμόρφωσης.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε καθηγητά, ποιο είναι το πείραμα που, κατά τη γνώμη σας, δείχνει καλύτερα πόσο μας επηρεάζουν οι άλλοι;", "Professor, which experiment, in your opinion, best shows how much other people influence us?"),
  L("Ψυχολόγος", "m", "Χωρίς αμφιβολία, τα πειράματα του Σόλομον Ας, τη δεκαετία του 1950. Η διαδικασία ήταν απλή: μια ομάδα φοιτητών έβλεπε μια γραμμή και έπρεπε να πει ποια από τρεις άλλες γραμμές είχε το ίδιο μήκος. Η απάντηση ήταν προφανής. Το κόλπο ήταν ότι όλοι οι συμμετέχοντες, εκτός από έναν, ήταν συνεργάτες του ερευνητή και σε ορισμένες δοκιμές έδιναν συνειδητά την ίδια λανθασμένη απάντηση.", "Without a doubt, Solomon Asch's experiments in the 1950s. The procedure was simple: a group of students looked at a line and had to say which of three other lines was the same length. The answer was obvious. The trick was that all the participants except one were the researcher's accomplices, and in certain trials they deliberately gave the same wrong answer."),
  L("Δημοσιογράφος", "f", "Και ο μοναδικός πραγματικός συμμετέχων τι έκανε;", "And what did the only real participant do?"),
  L("Ψυχολόγος", "m", "Σε περίπου ένα τρίτο των δοκιμών αυτών, ακολουθούσε την πλειοψηφία, παρόλο που έβλεπε με τα μάτια του ότι έκανε λάθος. Περίπου τρεις στους τέσσερις συμμετέχοντες υποχώρησαν τουλάχιστον μία φορά. Όταν τους ρωτούσαν μετά, κάποιοι έλεγαν ότι δεν ήθελαν να φανούν παράξενοι· άλλοι είχαν αρχίσει πραγματικά να αμφιβάλλουν για την κρίση τους.", "In about a third of those trials, he went along with the majority, even though he could see with his own eyes that it was wrong. About three in four participants gave in at least once. When asked afterwards, some said they didn't want to seem odd; others had genuinely begun to doubt their own judgement."),
  L("Δημοσιογράφος", "f", "Υπάρχει κάτι που μας βοηθά να αντισταθούμε;", "Is there anything that helps us resist?"),
  L("Ψυχολόγος", "m", "Ναι, και είναι ίσως το πιο ελπιδοφόρο εύρημα. Αρκούσε ένας μόνο σύμμαχος, ένας συνεργάτης που έδινε τη σωστή απάντηση, για να μειωθεί δραματικά η συμμόρφωση. Δεν χρειάζεται, δηλαδή, να είσαι ήρωας· χρειάζεται να μην είσαι μόνος. Γι’ αυτό, σε μια σύσκεψη, η πρώτη φωνή που διαφωνεί έχει τεράστια αξία: ανοίγει τον δρόμο και για τους υπόλοιπους.", "Yes, and it's perhaps the most hopeful finding. A single ally, one accomplice who gave the right answer, was enough to reduce conformity dramatically. In other words, you don't need to be a hero; you need not to be alone. That's why, in a meeting, the first voice that disagrees is enormously valuable: it opens the way for the rest too."),
 ],
 "questions": [
  Q("Ποιο ήταν το «κόλπο» του πειράματος;", ["Οι γραμμές ήταν σχεδόν ίδιες", "Όλοι εκτός από έναν ήταν συνεργάτες του ερευνητή", "Οι συμμετέχοντες δεν έβλεπαν καλά", "Οι απαντήσεις δίνονταν γραπτώς"], 1, "όλοι οι συμμετέχοντες, εκτός από έναν, ήταν συνεργάτες του ερευνητή"),
  Q("Πόσοι συμμετέχοντες υποχώρησαν τουλάχιστον μία φορά;", ["Ένας στους δέκα", "Περίπου οι μισοί", "Περίπου τρεις στους τέσσερις", "Όλοι"], 2, "Περίπου τρεις στους τέσσερις συμμετέχοντες υποχώρησαν τουλάχιστον μία φορά"),
  Q("Τι μείωνε δραματικά τη συμμόρφωση;", ["Μια χρηματική αμοιβή", "Η παρουσία ενός μόνο συμμάχου", "Ο χρόνος σκέψης", "Η ανωνυμία"], 1, "Αρκούσε ένας μόνο σύμμαχος"),
 ],
 "gloss": {"συμμόρφωσης": "συμμόρφωση — conformity", "μήκος": "μήκος — length", "προφανής": "προφανής — obvious", "κόλπο": "κόλπο — trick", "συνεργάτες": "συνεργάτης — accomplice, associate", "δοκιμές": "δοκιμή — trial", "συνειδητά": "συνειδητά — deliberately", "πλειοψηφία": "πλειοψηφία — majority", "υποχώρησαν": "υποχωρώ — to give in", "αμφιβάλλουν": "αμφιβάλλω — to doubt", "κρίση": "κρίση — judgement", "ελπιδοφόρο": "ελπιδοφόρος — hopeful", "εύρημα": "εύρημα — finding", "σύμμαχος": "σύμμαχος — ally", "σύσκεψη": "σύσκεψη — meeting"},
})
ITEMS.append({
 "id": "l86-c1-fainomeno-provolea", "title": "Μας κοιτάζουν όλοι;", "title_en": "Is everyone looking at us?", "type": "monologue", "level": "C1",
 "context_el": "Σε μια διάλεξη για την καθημερινή ψυχολογία, μια ψυχολόγος μιλά για το λεγόμενο «φαινόμενο του προβολέα».",
 "script": [
  L("Ψυχολόγος", "f", "Έχετε μπει ποτέ σε μια αίθουσα με έναν λεκέ στο πουκάμισο και είχατε την αίσθηση ότι όλοι τον κοιτάζουν; Ή σκοντάψατε στον δρόμο και νιώσατε ότι το είδε όλη η γειτονιά; Οι ψυχολόγοι ονομάζουν αυτή την αίσθηση «φαινόμενο του προβολέα»: πιστεύουμε ότι βρισκόμαστε στο κέντρο της σκηνής, κάτω από ένα δυνατό φως, ενώ στην πραγματικότητα οι άλλοι μάς προσέχουν πολύ λιγότερο απ’ ό,τι νομίζουμε.", "Have you ever walked into a room with a stain on your shirt and had the feeling that everyone was looking at it? Or tripped in the street and felt that the whole neighbourhood saw it? Psychologists call this feeling the 'spotlight effect': we believe we are at the centre of the stage, under a bright light, while in reality others notice us much less than we think."),
  L("Ψυχολόγος", "f", "Σε ένα γνωστό πείραμα, ζητήθηκε από φοιτητές να φορέσουν ένα μπλουζάκι με το πρόσωπο ενός τραγουδιστή που θεωρούνταν τότε εντελώς ντεμοντέ, και να μπουν σε μια αίθουσα όπου κάθονταν οι συμφοιτητές τους. Οι φοιτητές υπολόγισαν ότι περίπου οι μισοί θα πρόσεχαν το μπλουζάκι. Στην πραγματικότητα, το πρόσεξε μόνο ένας στους τέσσερις.", "In a well-known experiment, students were asked to wear a T-shirt with the face of a singer who was then considered utterly unfashionable, and to walk into a room where their fellow students were sitting. The students estimated that about half would notice the T-shirt. In reality, only one in four noticed it."),
  L("Ψυχολόγος", "f", "Γιατί συμβαίνει αυτό; Επειδή ο καθένας μας ζει, κυριολεκτικά, μέσα στο κεφάλι του. Ξέρουμε πολύ καλά τι νιώθουμε εμείς, και δυσκολευόμαστε να φανταστούμε ότι οι άλλοι είναι το ίδιο απορροφημένοι από τον δικό τους εαυτό. Η ειρωνεία είναι ότι, την ώρα που ανησυχούμε για τον λεκέ μας, ο διπλανός μας ανησυχεί για το δικό του μαλλί. Αν το θυμόμαστε αυτό, ίσως τολμάμε λίγο περισσότερο: να κάνουμε μια ερώτηση σε μια διάλεξη, να χορέψουμε σε έναν γάμο, να μιλήσουμε σε μια γλώσσα που δεν ξέρουμε ακόμα τέλεια.", "Why does this happen? Because each of us lives, literally, inside our own head. We know very well what we feel, and we find it hard to imagine that others are just as absorbed in themselves. The irony is that while we worry about our stain, the person next to us is worrying about their own hair. If we remember this, we might dare a little more: to ask a question in a lecture, to dance at a wedding, to speak a language we don't yet know perfectly."),
 ],
 "questions": [
  Q("Τι είναι το «φαινόμενο του προβολέα»;", ["Ο φόβος να μιλάμε μπροστά σε κοινό", "Η πεποίθηση ότι οι άλλοι μάς προσέχουν πολύ περισσότερο απ’ ό,τι στην πραγματικότητα", "Η τάση να κοιτάζουμε τους άλλους", "Μια ασθένεια των ματιών"], 1, "οι άλλοι μάς προσέχουν πολύ λιγότερο απ’ ό,τι νομίζουμε"),
  Q("Πόσοι πρόσεξαν πραγματικά το μπλουζάκι στο πείραμα;", ["Σχεδόν όλοι", "Περίπου οι μισοί", "Ένας στους τέσσερις", "Κανείς"], 2, "το πρόσεξε μόνο ένας στους τέσσερις"),
  Q("Ποια είναι, σύμφωνα με την ομιλήτρια, η πρακτική συνέπεια του φαινομένου;", ["Ότι πρέπει να ντυνόμαστε πιο προσεκτικά", "Ότι μπορούμε να τολμάμε περισσότερο", "Ότι πρέπει να αποφεύγουμε τις διαλέξεις", "Ότι οι άλλοι μάς κρίνουν αυστηρά"], 1, "ίσως τολμάμε λίγο περισσότερο"),
 ],
 "gloss": {"προβολέα": "προβολέας — spotlight", "λεκέ": "λεκές — stain", "σκοντάψατε": "σκοντάφτω — to trip", "σκηνής": "σκηνή — stage", "μπλουζάκι": "μπλουζάκι — T-shirt", "ντεμοντέ": "ντεμοντέ — out of fashion", "συμφοιτητές": "συμφοιτητής — fellow student", "υπολόγισαν": "υπολογίζω — to estimate", "κυριολεκτικά": "κυριολεκτικά — literally", "απορροφημένοι": "απορροφημένος — absorbed", "ειρωνεία": "ειρωνεία — irony", "τολμάμε": "τολμώ — to dare"},
})

rnd = random.Random(86)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-86.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
