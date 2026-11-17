# Source for library/listening/listening-115.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l115.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l115-ann-omichli-ptisi", "title": "Αλλαγή προορισμού λόγω ομίχλης", "title_en": "A change of destination because of fog", "type": "announcement", "level": "B2",
 "context_el": "Είστε σε μια πτήση για τη Θεσσαλονίκη. Ακούτε μια ανακοίνωση του κυβερνήτη.",
 "script": [
  L("Κυβερνήτης", "m", "Κυρίες και κύριοι, σας μιλά ο κυβερνήτης. Όπως ίσως καταλάβατε, κάνουμε κύκλους εδώ και είκοσι λεπτά. Στο αεροδρόμιο της Θεσσαλονίκης υπάρχει πυκνή ομίχλη και η ορατότητα είναι κάτω από το όριο που επιτρέπει την προσγείωση.", "Ladies and gentlemen, this is the captain speaking. As you may have realised, we've been circling for twenty minutes. There is thick fog at Thessaloniki airport and visibility is below the limit that allows landing."),
  L("Κυβερνήτης", "m", "Επειδή η πρόγνωση δεν δείχνει βελτίωση την επόμενη ώρα, αποφασίσαμε να προσγειωθούμε στην Καβάλα. Θα φτάσουμε εκεί σε περίπου τριάντα πέντε λεπτά. Η εταιρεία έχει ήδη κανονίσει λεωφορεία που θα σας μεταφέρουν στη Θεσσαλονίκη.", "Because the forecast shows no improvement in the next hour, we have decided to land at Kavala. We'll get there in about thirty-five minutes. The airline has already arranged coaches that will take you to Thessaloniki."),
  L("Κυβερνήτης", "m", "Οι αποσκευές σας θα παραδοθούν κανονικά στην Καβάλα και θα ταξιδέψουν μαζί σας με τα λεωφορεία. Όσοι έχετε ανταπόκριση για άλλη πτήση, παρακαλείστε να ενημερώσετε το πλήρωμα πριν από την προσγείωση, ώστε να βρεθεί λύση. Ζητούμε συγγνώμη για την ταλαιπωρία.", "Your luggage will be delivered as normal in Kavala and will travel with you on the coaches. Those of you with a connection to another flight are asked to inform the crew before landing, so that a solution can be found. We apologise for the inconvenience."),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί να προσγειωθεί το αεροπλάνο στη Θεσσαλονίκη;", ["Λόγω απεργίας", "Λόγω πυκνής ομίχλης", "Λόγω βλάβης στο αεροπλάνο", "Λόγω ισχυρών ανέμων"], 1, "Στο αεροδρόμιο της Θεσσαλονίκης υπάρχει πυκνή ομίχλη"),
  Q("Πώς θα φτάσουν οι επιβάτες στη Θεσσαλονίκη;", ["Με άλλη πτήση", "Με τρένο", "Με λεωφορεία που κανόνισε η εταιρεία", "Με ταξί"], 2, "Η εταιρεία έχει ήδη κανονίσει λεωφορεία"),
  Q("Τι πρέπει να κάνουν όσοι έχουν ανταπόκριση;", ["Να ενημερώσουν το πλήρωμα πριν από την προσγείωση", "Να μείνουν στις θέσεις τους", "Να πάρουν τις αποσκευές τους πρώτοι", "Να καλέσουν την εταιρεία από την Καβάλα"], 0, "παρακαλείστε να ενημερώσετε το πλήρωμα πριν από την προσγείωση"),
 ],
 "gloss": {"κυβερνήτης": "κυβερνήτης — captain (of an aircraft)", "κύκλους": "κάνω κύκλους — to circle", "πυκνή": "πυκνός — thick, dense", "ορατότητα": "ορατότητα — visibility", "προσγείωση": "προσγείωση — landing", "πρόγνωση": "πρόγνωση — forecast", "αποσκευές": "αποσκευές — luggage", "ανταπόκριση": "ανταπόκριση — connection (flight)", "πλήρωμα": "πλήρωμα — crew", "ταλαιπωρία": "ταλαιπωρία — inconvenience, hassle"}
})

ITEMS.append({
 "id": "l115-vm-scholi-chorou-kostoumia", "title": "Μήνυμα από τη δασκάλα χορού για την παράσταση", "title_en": "A message from the dance teacher about the show", "type": "voicemail", "level": "B2",
 "context_el": "Η κόρη σας κάνει μαθήματα χορού. Ακούτε ένα μήνυμα στον τηλεφωνητή.",
 "script": [
  L("Δασκάλα", "f", "Καλησπέρα σας, η Νεφέλη είμαι, η δασκάλα της Ιφιγένειας στο μπαλέτο. Σας τηλεφωνώ για την παράσταση της δεκαπέντε Ιουνίου. Η πρόβα τζενεράλε θα γίνει την προηγούμενη μέρα, το Σάββατο, στο δημοτικό θέατρο και όχι στη σχολή, από τις δέκα μέχρι τη μία.", "Good evening, it's Nefeli, Ifigeneia's ballet teacher. I'm calling about the show on the fifteenth of June. The dress rehearsal will be the day before, on Saturday, at the municipal theatre and not at the school, from ten to one."),
  L("Δασκάλα", "f", "Τα κοστούμια τα ράβει μια μοδίστρα, αλλά χρειάζεται τις μετρήσεις της μικρής μέχρι την Παρασκευή: ύψος, περιφέρεια μέσης και μήκος από τον ώμο ως το γόνατο. Μπορείτε να μου τις στείλετε με μήνυμα. Το κόστος για το κοστούμι είναι τριάντα ευρώ.", "The costumes are being sewn by a dressmaker, but she needs the little one's measurements by Friday: height, waist and the length from shoulder to knee. You can send them to me by text. The cost for the costume is thirty euros."),
  L("Δασκάλα", "f", "Την ημέρα της παράστασης τα κορίτσια πρέπει να είναι στο θέατρο μία ώρα νωρίτερα, με τα μαλλιά πιασμένα κότσο. Το μακιγιάζ θα το κάνουμε εμείς. Και μια παράκληση: κατά τη διάρκεια της παράστασης δεν επιτρέπονται φωτογραφίες με φλας, γιατί τα παιδιά τυφλώνονται και μπορεί να χάσουν τη χορογραφία.", "On the day of the show the girls must be at the theatre an hour early, with their hair in a bun. We'll do the make-up. And one request: during the show flash photography is not allowed, because the children are dazzled and may lose track of the choreography."),
 ],
 "questions": [
  Q("Πού θα γίνει η πρόβα τζενεράλε;", ["Στη σχολή χορού", "Στο δημοτικό θέατρο", "Στο σχολείο της μικρής", "Στο σπίτι της δασκάλας"], 1, "στο δημοτικό θέατρο και όχι στη σχολή"),
  Q("Τι χρειάζεται η μοδίστρα μέχρι την Παρασκευή;", ["Τα χρήματα για το κοστούμι", "Μια φωτογραφία της μικρής", "Τις μετρήσεις της μικρής", "Το ύφασμα"], 2, "χρειάζεται τις μετρήσεις της μικρής μέχρι την Παρασκευή"),
  Q("Γιατί δεν επιτρέπονται φωτογραφίες με φλας;", ["Γιατί τα παιδιά τυφλώνονται και μπορεί να χάσουν τη χορογραφία", "Γιατί το απαγορεύει το θέατρο", "Γιατί θα υπάρχει επαγγελματίας φωτογράφος", "Γιατί ενοχλούν το υπόλοιπο κοινό"], 0, "τα παιδιά τυφλώνονται και μπορεί να χάσουν τη χορογραφία"),
 ],
 "gloss": {"παράσταση": "παράσταση — show, performance", "πρόβα τζενεράλε": "πρόβα τζενεράλε — dress rehearsal", "κοστούμια": "κοστούμι — costume; suit", "μοδίστρα": "μοδίστρα — dressmaker", "μετρήσεις": "μέτρηση — measurement", "περιφέρεια μέσης": "περιφέρεια μέσης — waist measurement", "κότσο": "κότσος — bun (hair)", "τυφλώνονται": "τυφλώνομαι — to be dazzled, blinded", "χορογραφία": "χορογραφία — choreography"}
})

ITEMS.append({
 "id": "l115-dia-kyriakatiko-trapezi", "title": "Κάθε Κυριακή στα πεθερικά;", "title_en": "Every Sunday at the in-laws'?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά για το κυριακάτικο τραπέζι στα πεθερικά.",
 "script": [
  L("Ελπίδα", "f", "Γιώργο, πρέπει να το συζητήσουμε. Εδώ και τρία χρόνια, κάθε Κυριακή τρώμε στους γονείς σου. Δεν έχουμε πάει ούτε μία εκδρομή, ούτε έχουμε δει ποτέ τους φίλους μας μεσημέρι Κυριακής.", "Giorgos, we need to talk about it. For three years now, every Sunday we eat at your parents'. We haven't gone on a single trip, and we've never seen our friends on a Sunday lunchtime."),
  L("Γιώργος", "m", "Το ξέρω, αλλά η μάνα μου μαγειρεύει από το Σάββατο. Αν της πω ότι δεν θα πάμε, θα το πάρει πολύ βαριά. Από τότε που βγήκε στη σύνταξη ο πατέρας μου, αυτό το τραπέζι είναι το μόνο που την κάνει χαρούμενη.", "I know, but my mum starts cooking on Saturday. If I tell her we're not going, she'll take it very hard. Since my dad retired, that lunch is the only thing that makes her happy."),
  L("Ελπίδα", "f", "Δεν λέω να σταματήσουμε. Λέω να πηγαίνουμε δύο Κυριακές τον μήνα. Και τις άλλες, γιατί να μην έρχονται εκείνοι σε μας πού και πού; Θα μαγειρέψω εγώ, να ξεκουραστεί κι η μητέρα σου.", "I'm not saying we should stop. I'm saying we go two Sundays a month. And on the others, why shouldn't they come to us now and then? I'll cook, so your mother can have a rest too."),
  L("Γιώργος", "m", "Αυτό μπορεί να της αρέσει, αρκεί να της το πούμε σωστά. Ας της ζητήσουμε να σου δείξει πώς φτιάχνει το παστίτσιο της. Αν νιώσει ότι τη χρειαζόμαστε, θα το δεχτεί πιο εύκολα.", "She might like that, as long as we put it to her the right way. Let's ask her to show you how she makes her pastitsio. If she feels we need her, she'll accept it more easily."),
 ],
 "questions": [
  Q("Τι ενοχλεί την Ελπίδα;", ["Ότι η πεθερά της δεν μαγειρεύει καλά", "Ότι κάθε Κυριακή τρώνε στους γονείς του Γιώργου", "Ότι ο Γιώργος δουλεύει τις Κυριακές", "Ότι οι φίλοι τους δεν τους καλούν"], 1, "κάθε Κυριακή τρώμε στους γονείς σου"),
  Q("Γιατί ο Γιώργος διστάζει να αλλάξει τη συνήθεια;", ["Γιατί του αρέσει πολύ το φαγητό", "Γιατί ο πατέρας του είναι άρρωστος", "Γιατί η μητέρα του θα το πάρει πολύ βαριά", "Γιατί δεν έχουν χρόνο για εκδρομές"], 2, "θα το πάρει πολύ βαριά"),
  Q("Πώς σκέφτεται ο Γιώργος να το πουν στη μητέρα του;", ["Να της ζητήσουν να δείξει στην Ελπίδα πώς φτιάχνει το παστίτσιο", "Να της στείλουν ένα μήνυμα", "Να της το πει ο πατέρας του", "Να της πουν ότι έχουν δουλειά"], 0, "Ας της ζητήσουμε να σου δείξει πώς φτιάχνει το παστίτσιο της"),
 ],
 "gloss": {"πεθερικά": "πεθερικά — in-laws", "κυριακάτικο": "κυριακάτικος — Sunday (adjective)", "θα το πάρει πολύ βαριά": "το παίρνω βαριά — to take something hard", "σύνταξη": "βγαίνω στη σύνταξη — to retire", "πού και πού": "πού και πού — now and then", "ξεκουραστεί": "ξεκουράζομαι — to rest", "αρκεί να": "αρκεί να — as long as, provided that"}
})

ITEMS.append({
 "id": "l115-int-daktylioseis-poulion", "title": "Δαχτυλίδια για τα πουλιά", "title_en": "Rings for the birds", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια ορνιθολόγο σε εκπομπή για τη φύση.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Σταθοπούλου, τι ακριβώς κάνετε στον σταθμό δακτυλίωσης;", "Ms Stathopoulou, what exactly do you do at the ringing station?"),
  L("Ορνιθολόγος", "f", "Πιάνουμε πουλιά με ειδικά, πολύ λεπτά δίχτυα, τους φοράμε στο πόδι ένα μικρό μεταλλικό δαχτυλίδι με μοναδικό κωδικό και τα αφήνουμε ελεύθερα. Πριν τα αφήσουμε, τα ζυγίζουμε, μετράμε τα φτερά τους και σημειώνουμε το είδος και την ηλικία τους. Όλο αυτό κρατά λιγότερο από ένα λεπτό.", "We catch birds with special, very fine nets, put a small metal ring with a unique code on their leg and set them free. Before releasing them, we weigh them, measure their wings and record their species and age. The whole thing takes less than a minute."),
  L("Δημοσιογράφος", "m", "Και τι μαθαίνετε από αυτό;", "And what do you learn from it?"),
  L("Ορνιθολόγος", "f", "Αν το ίδιο πουλί πιαστεί ξανά κάπου αλλού, ή βρεθεί νεκρό, ο κωδικός μάς λέει από πού ήρθε. Έτσι χαρτογραφούμε τις διαδρομές της μετανάστευσης. Πέρσι, για παράδειγμα, ένα χελιδόνι που δακτυλιώσαμε εδώ βρέθηκε στη Νιγηρία. Μαθαίνουμε επίσης πόσο ζουν τα πουλιά και αν οι πληθυσμοί τους μειώνονται.", "If the same bird is caught again somewhere else, or found dead, the code tells us where it came from. That way we map migration routes. Last year, for example, a swallow we ringed here was found in Nigeria. We also learn how long birds live and whether their populations are declining."),
  L("Δημοσιογράφος", "m", "Μπορεί να το κάνει οποιοσδήποτε;", "Can anyone do it?"),
  L("Ορνιθολόγος", "f", "Όχι. Χρειάζεται εκπαίδευση και ειδική άδεια, γιατί ένα πουλί είναι εύθραυστο και πρέπει να το κρατάς σωστά. Το κοινό όμως μπορεί να βοηθήσει πολύ: αν βρείτε ένα πουλί με δαχτυλίδι, σημειώστε τον κωδικό και πού το βρήκατε, και στείλτε τον στον σταθμό.", "No. It takes training and a special licence, because a bird is fragile and you have to hold it correctly. But the public can help a lot: if you find a bird with a ring, write down the code and where you found it, and send it to the station."),
 ],
 "questions": [
  Q("Τι κάνουν στα πουλιά πριν τα αφήσουν ελεύθερα;", ["Τους δίνουν τροφή", "Τα ζυγίζουν, μετρούν τα φτερά τους και σημειώνουν είδος και ηλικία", "Τα φωτογραφίζουν για μια έκθεση", "Τα κρατούν μια μέρα για παρατήρηση"], 1, "τα ζυγίζουμε, μετράμε τα φτερά τους και σημειώνουμε το είδος και την ηλικία τους"),
  Q("Πού βρέθηκε το χελιδόνι που δακτυλίωσαν;", ["Στην Αίγυπτο", "Στη Σουηδία", "Στη Νιγηρία", "Στην Κρήτη"], 2, "βρέθηκε στη Νιγηρία"),
  Q("Πώς μπορεί να βοηθήσει το κοινό;", ["Στέλνοντας στον σταθμό τον κωδικό ενός πουλιού με δαχτυλίδι και πού βρέθηκε", "Πιάνοντας πουλιά με δίχτυα", "Ταΐζοντας τα πουλιά τον χειμώνα", "Βάζοντας δαχτυλίδια στα πουλιά του κήπου"], 0, "σημειώστε τον κωδικό και πού το βρήκατε, και στείλτε τον στον σταθμό"),
 ],
 "gloss": {"ορνιθολόγο": "ορνιθολόγος — ornithologist", "δακτυλίωσης": "δακτυλίωση — (bird) ringing", "δαχτυλίδι": "δαχτυλίδι — ring", "κωδικό": "κωδικός — code", "ζυγίζουμε": "ζυγίζω — to weigh", "χαρτογραφούμε": "χαρτογραφώ — to map", "μετανάστευσης": "μετανάστευση — migration", "χελιδόνι": "χελιδόνι — swallow", "άδεια": "άδεια — licence, permit", "εύθραυστο": "εύθραυστος — fragile"}
})

ITEMS.append({
 "id": "l115-rep-xenodocheio-entomon", "title": "Ένα ξενοδοχείο για έντομα στην αυλή του σχολείου", "title_en": "A bug hotel in the schoolyard", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε εκπομπή για την εκπαίδευση.",
 "script": [
  L("Ρεπόρτερ", "f", "Στην αυλή ενός δημοτικού σχολείου στη Λάρισα υπάρχει ένα ξενοδοχείο με πενήντα «δωμάτια», αλλά κανένας ανθρώπινος πελάτης. Πρόκειται για ένα ξενοδοχείο εντόμων: μια ξύλινη κατασκευή γεμάτη καλάμια, κουκουνάρια, τρυπημένα κούτσουρα και άχυρο, που έφτιαξαν οι μαθητές της πέμπτης τάξης.", "In the yard of a primary school in Larissa there is a hotel with fifty \"rooms\" but not a single human guest. It is an insect hotel: a wooden structure full of canes, pine cones, drilled logs and straw, built by the fifth-grade pupils."),
  L("Ρεπόρτερ", "f", "Όπως εξηγεί η δασκάλα τους, τα σύγχρονα κτίρια και οι περιποιημένοι κήποι δεν αφήνουν πολλές κρυψώνες για τις μοναχικές μέλισσες, τις πασχαλίτσες και άλλα ωφέλιμα έντομα. Το ξενοδοχείο τούς προσφέρει καταφύγιο τον χειμώνα και μέρος για να αφήσουν τα αυγά τους την άνοιξη.", "As their teacher explains, modern buildings and tidy gardens don't leave many hiding places for solitary bees, ladybirds and other beneficial insects. The hotel offers them shelter in winter and a place to lay their eggs in spring."),
  L("Ρεπόρτερ", "f", "Τα παιδιά το τοποθέτησαν με την πρόσοψη προς τον νότο, για να το ζεσταίνει ο ήλιος, και φύτεψαν γύρω του λεβάντα και θυμάρι. Κάθε εβδομάδα σημειώνουν σε ένα τετράδιο ποια έντομα είδαν. «Πριν φοβόμουν τις μέλισσες», λέει ένας μαθητής, «τώρα τις μετράω.»", "The children placed it facing south, so that the sun warms it, and planted lavender and thyme around it. Every week they note down in a notebook which insects they saw. \"I used to be scared of bees,\" says one pupil, \"now I count them.\""),
 ],
 "questions": [
  Q("Ποιος έφτιαξε το ξενοδοχείο εντόμων;", ["Ο δήμος", "Οι μαθητές της πέμπτης τάξης", "Ένας μελισσοκόμος", "Οι γονείς"], 1, "που έφτιαξαν οι μαθητές της πέμπτης τάξης"),
  Q("Γιατί χρειάζονται τα έντομα τέτοιες κατασκευές;", ["Γιατί κάνει πολύ κρύο στη Λάρισα", "Γιατί δεν βρίσκουν τροφή", "Γιατί τα σύγχρονα κτίρια και οι περιποιημένοι κήποι δεν αφήνουν κρυψώνες", "Γιατί τα κυνηγούν τα πουλιά"], 2, "τα σύγχρονα κτίρια και οι περιποιημένοι κήποι δεν αφήνουν πολλές κρυψώνες"),
  Q("Γιατί το τοποθέτησαν με την πρόσοψη προς τον νότο;", ["Για να το ζεσταίνει ο ήλιος", "Για να φαίνεται από τον δρόμο", "Για να μην το βρέχει η βροχή", "Για να είναι κοντά στις τάξεις"], 0, "για να το ζεσταίνει ο ήλιος"),
 ],
 "gloss": {"έντομα": "έντομο — insect", "καλάμια": "καλάμι — cane, reed", "κουκουνάρια": "κουκουνάρι — pine cone", "κούτσουρα": "κούτσουρο — log", "άχυρο": "άχυρο — straw", "περιποιημένοι": "περιποιημένος — tidy, well-kept", "κρυψώνες": "κρυψώνα — hiding place", "μοναχικές": "μοναχικός — solitary", "πασχαλίτσες": "πασχαλίτσα — ladybird", "ωφέλιμα": "ωφέλιμος — beneficial, useful", "πρόσοψη": "πρόσοψη — front, façade"}
})

ITEMS.append({
 "id": "l115-rep-chorio-rigani", "title": "Ένα χωριό που μυρίζει ρίγανη", "title_en": "A village that smells of oregano", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε εκπομπή για την ύπαιθρο.",
 "script": [
  L("Ρεπόρτερ", "m", "Τον Ιούλιο, στα βουνά γύρω από το χωριό, οι κάτοικοι ξυπνούν πριν από την ανατολή για να μαζέψουν ρίγανη. Τη μαζεύουν όταν είναι ανθισμένη, γιατί τότε έχει το πιο έντονο άρωμα, και μόνο νωρίς το πρωί, πριν τη χτυπήσει ο καυτός ήλιος.", "In July, in the mountains around the village, the residents wake before sunrise to gather oregano. They pick it when it's in flower, because that's when it has the strongest aroma, and only early in the morning, before the scorching sun hits it."),
  L("Ρεπόρτερ", "m", "Ο κανόνας είναι απαράβατος: κόβεις τα κλωνάρια με ψαλίδι, ποτέ δεν ξεριζώνεις το φυτό, για να ξαναβγεί την επόμενη χρονιά. Έπειτα τα δένουν σε ματσάκια και τα κρεμούν ανάποδα σε σκιερές αποθήκες, γιατί ο ήλιος θα έκαιγε το άρωμα.", "The rule is unbreakable: you cut the sprigs with scissors, you never uproot the plant, so that it grows back the following year. Then they tie them in little bunches and hang them upside down in shady storerooms, because the sun would burn off the aroma."),
  L("Ρεπόρτερ", "m", "Πριν από πέντε χρόνια οι κάτοικοι ίδρυσαν συνεταιρισμό και άρχισαν να πουλούν τη ρίγανη συσκευασμένη, με το όνομα του χωριού. Σήμερα φτάνει μέχρι τη Γερμανία και τη Σουηδία. Το πιο σημαντικό, λέει ο πρόεδρος, είναι ότι δύο νέα ζευγάρια γύρισαν στο χωριό για να δουλέψουν στον συνεταιρισμό.", "Five years ago the residents founded a cooperative and started selling the oregano packaged, with the village's name. Today it reaches as far as Germany and Sweden. The most important thing, says the president, is that two young couples came back to the village to work at the cooperative."),
 ],
 "questions": [
  Q("Γιατί μαζεύουν τη ρίγανη όταν είναι ανθισμένη;", ["Γιατί είναι πιο εύκολο να κοπεί", "Γιατί τότε έχει το πιο έντονο άρωμα", "Γιατί τότε πληρώνεται καλύτερα", "Γιατί μετά ξεραίνεται"], 1, "γιατί τότε έχει το πιο έντονο άρωμα"),
  Q("Γιατί δεν ξεριζώνουν ποτέ το φυτό;", ["Γιατί απαγορεύεται από τον δήμο", "Γιατί οι ρίζες είναι πικρές", "Για να ξαναβγεί την επόμενη χρονιά", "Για να μη χαλάσει το χώμα"], 2, "για να ξαναβγεί την επόμενη χρονιά"),
  Q("Ποιο είναι, κατά τον πρόεδρο, το πιο σημαντικό αποτέλεσμα του συνεταιρισμού;", ["Ότι δύο νέα ζευγάρια γύρισαν στο χωριό", "Ότι η ρίγανη φτάνει στη Σουηδία", "Ότι οι τιμές ανέβηκαν", "Ότι το χωριό έγινε γνωστό στην τηλεόραση"], 0, "δύο νέα ζευγάρια γύρισαν στο χωριό"),
 ],
 "gloss": {"ρίγανη": "ρίγανη — oregano", "ανατολή": "ανατολή — sunrise; east", "ανθισμένη": "ανθισμένος — in bloom", "άρωμα": "άρωμα — aroma, scent", "καυτός": "καυτός — scorching, very hot", "απαράβατος": "απαράβατος — unbreakable, inviolable", "κλωνάρια": "κλωνάρι — sprig, twig", "ξεριζώνεις": "ξεριζώνω — to uproot", "ματσάκια": "ματσάκι — small bunch", "σκιερές": "σκιερός — shady", "συσκευασμένη": "συσκευασμένος — packaged"}
})

ITEMS.append({
 "id": "l115-mono-chathike-o-skylos", "title": "Η μέρα που χάθηκε ο σκύλος μας", "title_en": "The day our dog went missing", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να διηγείται μια ιστορία σε ραδιοφωνική εκπομπή με ιστορίες ακροατών.",
 "script": [
  L("Αφηγητής", "m", "Ήταν παραμονή Πρωτοχρονιάς. Στις δώδεκα ακριβώς άρχισαν τα βεγγαλικά, και ο Ρεξ, που φοβάται τους κρότους, πήδηξε τον φράχτη της αυλής και εξαφανίστηκε στο σκοτάδι. Τον ψάχναμε μέχρι τις τέσσερις το πρωί, με φακούς, φωνάζοντας το όνομά του.", "It was New Year's Eve. At exactly twelve the fireworks started, and Rex, who's afraid of bangs, jumped the yard fence and vanished into the dark. We searched for him until four in the morning, with torches, calling his name."),
  L("Αφηγητής", "m", "Το πρωί η κόρη μου ανέβασε τη φωτογραφία του σε μια ομάδα της γειτονιάς στο διαδίκτυο. Μέσα σε μία ώρα την είχαν κοινοποιήσει εκατοντάδες άνθρωποι. Ο κτηνίατρος μας θύμισε κάτι που είχαμε ξεχάσει: ο Ρεξ είχε μικροτσίπ, οπότε όποιος τον έβρισκε μπορούσε να μάθει πού μένουμε.", "In the morning my daughter posted his photo in a neighbourhood group online. Within an hour hundreds of people had shared it. The vet reminded us of something we'd forgotten: Rex had a microchip, so whoever found him could find out where we live."),
  L("Αφηγητής", "m", "Το απόγευμα χτύπησε το τηλέφωνο. Ένας φούρναρης τρία χιλιόμετρα μακριά τον είχε βρει να κοιμάται κουλουριασμένος πίσω από τον φούρνο του, εκεί που ήταν ζεστά. Όταν πήγαμε, ο Ρεξ έτρωγε ήδη το δεύτερο κουλούρι του. Από τότε, κάθε παραμονή Πρωτοχρονιάς, μένει μέσα στο μπάνιο, με το ραδιόφωνο ανοιχτό.", "In the afternoon the phone rang. A baker three kilometres away had found him sleeping curled up behind his oven, where it was warm. When we got there, Rex was already eating his second bread ring. Since then, every New Year's Eve, he stays inside in the bathroom, with the radio on."),
 ],
 "questions": [
  Q("Γιατί έφυγε ο Ρεξ από την αυλή;", ["Γιατί κυνηγούσε μια γάτα", "Γιατί φοβήθηκε τα βεγγαλικά", "Γιατί η πόρτα ήταν ανοιχτή", "Γιατί πεινούσε"], 1, "ο Ρεξ, που φοβάται τους κρότους, πήδηξε τον φράχτη"),
  Q("Τι τους θύμισε ο κτηνίατρος;", ["Ότι ο Ρεξ ήξερε τον δρόμο", "Ότι πρέπει να ειδοποιήσουν την αστυνομία", "Ότι ο Ρεξ είχε μικροτσίπ", "Ότι οι σκύλοι γυρίζουν μόνοι τους"], 2, "ο Ρεξ είχε μικροτσίπ"),
  Q("Πού βρήκε ο φούρναρης τον Ρεξ;", ["Να κοιμάται πίσω από τον φούρνο του", "Μέσα στο μαγαζί του", "Στον δρόμο μπροστά από τον φούρνο", "Σε ένα πάρκο"], 0, "να κοιμάται κουλουριασμένος πίσω από τον φούρνο του"),
 ],
 "gloss": {"παραμονή": "παραμονή — eve", "βεγγαλικά": "βεγγαλικά — fireworks", "κρότους": "κρότος — bang", "φράχτη": "φράχτης — fence", "κοινοποιήσει": "κοινοποιώ — to share (online); to notify", "μικροτσίπ": "μικροτσίπ — microchip", "φούρναρης": "φούρναρης — baker", "κουλουριασμένος": "κουλουριασμένος — curled up", "κουλούρι": "κουλούρι — bread ring"}
})

ITEMS.append({
 "id": "l115-mono-proti-synavlia-drams", "title": "Η πρώτη μου συναυλία στα σαράντα δύο", "title_en": "My first gig at forty-two", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλά σε ραδιοφωνική εκπομπή για ερασιτέχνες μουσικούς.",
 "script": [
  L("Αφηγήτρια", "f", "Ως έφηβη ονειρευόμουν να παίζω ντραμς σε μια ροκ μπάντα, αλλά οι γονείς μου έλεγαν ότι είναι «θόρυβος, όχι μουσική». Έτσι σπούδασα λογίστρια και ξέχασα το όνειρο για είκοσι πέντε χρόνια.", "As a teenager I dreamed of playing drums in a rock band, but my parents said it was \"noise, not music\". So I trained as an accountant and forgot the dream for twenty-five years."),
  L("Αφηγήτρια", "f", "Στα σαράντα, ο γιος μου ζήτησε μαθήματα ντραμς. Τον πήγαινα κάθε Τρίτη και περίμενα έξω από την αίθουσα. Ένα βράδυ ο δάσκαλος με ρώτησε γιατί χτυπούσα το πόδι μου στον ρυθμό. Του είπα την αλήθεια, κι εκείνος μου έδωσε δύο μπαγκέτες: «Η επόμενη ώρα είναι ελεύθερη».", "At forty, my son asked for drum lessons. I took him every Tuesday and waited outside the room. One evening the teacher asked me why I was tapping my foot to the rhythm. I told him the truth, and he handed me two drumsticks: \"The next hour is free.\""),
  L("Αφηγήτρια", "f", "Πριν από έναν μήνα παίξαμε για πρώτη φορά σε ένα μπαράκι, με τρεις φίλους που βρήκα μέσω της σχολής. Έτρεμαν τα χέρια μου στα πρώτα τραγούδια. Στο κοινό ήταν ο γιος μου, οι συνάδελφοί μου και, προς έκπληξή μου, η μητέρα μου, που στο τέλος είπε: «Τελικά, δεν ήταν και τόσο θόρυβος».", "A month ago we played for the first time in a little bar, with three friends I found through the school. My hands were shaking during the first songs. In the audience were my son, my colleagues and, to my surprise, my mother, who said at the end: \"It wasn't so much noise after all.\""),
 ],
 "questions": [
  Q("Γιατί δεν έπαιξε ντραμς ως έφηβη;", ["Γιατί δεν είχε χρήματα για μαθήματα", "Γιατί οι γονείς της θεωρούσαν τα ντραμς θόρυβο", "Γιατί δεν υπήρχε σχολή στην πόλη της", "Γιατί προτιμούσε την κιθάρα"], 1, "οι γονείς μου έλεγαν ότι είναι «θόρυβος, όχι μουσική»"),
  Q("Πώς ξεκίνησε τελικά τα μαθήματα;", ["Της τα έκανε δώρο ο άντρας της", "Γράφτηκε μαζί με μια φίλη", "Ο δάσκαλος του γιου της την είδε να χτυπά το πόδι της στον ρυθμό", "Τα είδε σε μια διαφήμιση"], 2, "ο δάσκαλος με ρώτησε γιατί χτυπούσα το πόδι μου στον ρυθμό"),
  Q("Τι είπε η μητέρα της μετά τη συναυλία;", ["Ότι τελικά δεν ήταν και τόσο θόρυβος", "Ότι έπρεπε να είχε αρχίσει νωρίτερα", "Ότι η μουσική ήταν πολύ δυνατή", "Ότι προτιμά τη λαϊκή μουσική"], 0, "«Τελικά, δεν ήταν και τόσο θόρυβος»"),
 ],
 "gloss": {"έφηβη": "έφηβος, έφηβη — teenager", "ντραμς": "ντραμς — drums", "μπάντα": "μπάντα — band", "λογίστρια": "λογίστρια — (female) accountant", "ρυθμό": "ρυθμός — rhythm", "μπαγκέτες": "μπαγκέτα — drumstick", "μπαράκι": "μπαράκι — small bar", "συνάδελφοί": "συνάδελφος — colleague", "έκπληξή": "έκπληξη — surprise"}
})

ITEMS.append({
 "id": "l115-c1-giati-xechname-ta-oneira", "title": "Γιατί ξεχνάμε τα όνειρά μας", "title_en": "Why we forget our dreams", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ομιλία σε κύκλο διαλέξεων για τον ύπνο.",
 "script": [
  L("Ομιλήτρια", "f", "Όλοι ονειρευόμαστε κάθε νύχτα, ακόμη κι όσοι επιμένουν ότι «δεν βλέπουν ποτέ όνειρα». Τα πιο ζωντανά και αφηγηματικά όνειρα εμφανίζονται κυρίως κατά τη φάση REM, που επανέρχεται τέσσερις με έξι φορές σε έναν κανονικό νυχτερινό ύπνο. Κι όμως, το πρωί θυμόμαστε, στην καλύτερη περίπτωση, ένα θολό απόσπασμα.", "We all dream every night, even those who insist they \"never dream\". The most vivid, story-like dreams occur mainly during the REM phase, which comes back four to six times in a normal night's sleep. And yet in the morning we remember, at best, a hazy fragment."),
  L("Ομιλήτρια", "f", "Μια εξήγηση έχει να κάνει με τη χημεία του εγκεφάλου. Κατά τη φάση REM, τα επίπεδα της νοραδρεναλίνης, μιας ουσίας που φαίνεται να συμβάλλει στη σταθεροποίηση των αναμνήσεων, είναι πολύ χαμηλά. Ο εγκέφαλος, με άλλα λόγια, βλέπει την ταινία, αλλά δεν πατά το κουμπί της εγγραφής.", "One explanation has to do with brain chemistry. During REM sleep, levels of noradrenaline, a substance that seems to help consolidate memories, are very low. The brain, in other words, is watching the film but not pressing the record button."),
  L("Ομιλήτρια", "f", "Γι' αυτό θυμόμαστε πολύ καλύτερα ένα όνειρο όταν ξυπνάμε απότομα μέσα σε αυτό, για παράδειγμα από ένα ξυπνητήρι. Ακόμη και τότε, όμως, η ανάμνηση είναι εξαιρετικά εύθραυστη: αρκεί να σκεφτούμε τις υποχρεώσεις της ημέρας για να εξανεμιστεί μέσα σε λίγα λεπτά.", "That's why we remember a dream much better when we wake abruptly in the middle of it, for example to an alarm clock. Even then, though, the memory is extremely fragile: it takes only thinking of the day's obligations for it to evaporate within a few minutes."),
  L("Ομιλήτρια", "f", "Όσοι θέλουν να θυμούνται περισσότερα όνειρα μπορούν να κρατούν ένα σημειωματάριο δίπλα στο κρεβάτι και να γράφουν ό,τι θυμούνται πριν καν σηκωθούν. Οι μελέτες δείχνουν ότι μέσα σε λίγες εβδομάδες η ανάκληση βελτιώνεται αισθητά. Αν αυτό είναι ευχή ή κατάρα, εξαρτάται, φυσικά, από τα όνειρά σας.", "Those who want to remember more dreams can keep a notebook beside the bed and write down whatever they remember before they even get up. Studies show that within a few weeks recall improves noticeably. Whether that is a blessing or a curse depends, of course, on your dreams."),
 ],
 "questions": [
  Q("Τι λέει η ομιλήτρια για όσους λένε ότι δεν βλέπουν ποτέ όνειρα;", ["Ότι έχουν πρόβλημα ύπνου", "Ότι κι αυτοί ονειρεύονται κάθε νύχτα", "Ότι κοιμούνται πολύ λίγο", "Ότι δεν περνούν από τη φάση REM"], 1, "Όλοι ονειρευόμαστε κάθε νύχτα, ακόμη κι όσοι επιμένουν ότι «δεν βλέπουν ποτέ όνειρα»"),
  Q("Τι σημαίνει η εικόνα «βλέπει την ταινία, αλλά δεν πατά το κουμπί της εγγραφής»;", ["Ότι τα όνειρα είναι σαν κινηματογραφικές ταινίες", "Ότι ο εγκέφαλος ξεκουράζεται κατά τη φάση REM", "Ότι ο εγκέφαλος ονειρεύεται χωρίς να αποθηκεύει την ανάμνηση", "Ότι θυμόμαστε μόνο τις εικόνες και όχι τους ήχους"], 2, "βλέπει την ταινία, αλλά δεν πατά το κουμπί της εγγραφής"),
  Q("Τι μπορεί να κάνει μια ανάμνηση ονείρου να εξανεμιστεί;", ["Η σκέψη των υποχρεώσεων της ημέρας", "Ένα ξυπνητήρι", "Το φως της ημέρας", "Ένα ζεστό ρόφημα"], 0, "αρκεί να σκεφτούμε τις υποχρεώσεις της ημέρας για να εξανεμιστεί"),
  Q("Τι συμβουλεύει η ομιλήτρια όσους θέλουν να θυμούνται περισσότερα όνειρα;", ["Να κοιμούνται περισσότερες ώρες", "Να γράφουν ό,τι θυμούνται σε ένα σημειωματάριο πριν σηκωθούν", "Να ξυπνούν χωρίς ξυπνητήρι", "Να αποφεύγουν τον καφέ"], 1, "να γράφουν ό,τι θυμούνται πριν καν σηκωθούν"),
 ],
 "gloss": {"αφηγηματικά": "αφηγηματικός — narrative, story-like", "επανέρχεται": "επανέρχομαι — to return, recur", "θολό": "θολός — hazy, blurred", "απόσπασμα": "απόσπασμα — fragment, extract", "νοραδρεναλίνης": "νοραδρεναλίνη — noradrenaline", "σταθεροποίηση": "σταθεροποίηση — consolidation, stabilisation", "εύθραυστη": "εύθραυστος — fragile", "εξανεμιστεί": "εξανεμίζομαι — to evaporate, vanish", "σημειωματάριο": "σημειωματάριο — notebook", "ανάκληση": "ανάκληση — recall", "αισθητά": "αισθητά — noticeably", "κατάρα": "κατάρα — curse"}
})

ITEMS.append({
 "id": "l115-c1-pnyka", "title": "Στην Πνύκα, εκεί όπου ψήφιζαν οι Αθηναίοι", "title_en": "On the Pnyx, where the Athenians voted", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν ιστορικό σε εκπομπή για την αρχαία Αθήνα.",
 "script": [
  L("Δημοσιογράφος", "f", "Οι περισσότεροι επισκέπτες της Αθήνας ανεβαίνουν στην Ακρόπολη, αλλά λίγοι στην Πνύκα. Γιατί αξίζει;", "Most visitors to Athens go up to the Acropolis, but few to the Pnyx. Why is it worth it?"),
  L("Ιστορικός", "m", "Γιατί εδώ, σε αυτόν τον βραχώδη λόφο απέναντι από την Ακρόπολη, συνεδρίαζε η εκκλησία του δήμου, η συνέλευση όλων των Αθηναίων πολιτών. Εδώ αποφασίζονταν πόλεμοι και ειρήνες, εκλέγονταν στρατηγοί, ψηφίζονταν νόμοι. Αν η Ακρόπολη είναι ο ναός της αθηναϊκής θρησκείας, η Πνύκα είναι ο ναός της δημοκρατίας της.", "Because here, on this rocky hill opposite the Acropolis, the ekklesia met, the assembly of all Athenian citizens. Here wars and peace treaties were decided, generals were elected, laws were voted. If the Acropolis is the temple of Athenian religion, the Pnyx is the temple of its democracy."),
  L("Δημοσιογράφος", "f", "Πόσοι συμμετείχαν;", "How many took part?"),
  L("Ιστορικός", "m", "Για ορισμένες σημαντικές αποφάσεις, όπως ο εξοστρακισμός, απαιτούνταν τουλάχιστον έξι χιλιάδες ψήφοι. Ο χώρος διαμορφώθηκε σε περισσότερες από μία φάσεις, για να χωρά όλο και περισσότερους. Η προσέλευση όμως δεν ήταν πάντα δεδομένη. Ο Αριστοφάνης περιγράφει δούλους-αστυφύλακες που σάρωναν την αγορά με ένα σκοινί βαμμένο κόκκινο· όποιος λερωνόταν, και άρα είχε καθυστερήσει, κινδύνευε με πρόστιμο. Στις αρχές του τέταρτου αιώνα, μάλιστα, θεσπίστηκε μια μικρή αποζημίωση για όσους έρχονταν, ακριβώς για να ενθαρρυνθεί η συμμετοχή.", "For certain important decisions, such as ostracism, at least six thousand votes were required. The site was shaped in more than one phase, to hold more and more people. But attendance was not always a given. Aristophanes describes slave constables sweeping the agora with a rope dyed red; whoever got stained, and so had been dawdling, risked a fine. At the start of the fourth century, moreover, a small allowance was introduced for those who came, precisely to encourage participation."),
  L("Δημοσιογράφος", "f", "Και πώς γινόταν η συζήτηση;", "And how did the debate work?"),
  L("Ιστορικός", "m", "Ο κήρυκας ρωτούσε: «Τις αγορεύειν βούλεται;», δηλαδή «Ποιος θέλει να μιλήσει;». Θεωρητικά, οποιοσδήποτε πολίτης μπορούσε να ανέβει στο βήμα, που σώζεται ακόμη, σκαλισμένο στον βράχο. Στην πράξη, βέβαια, μιλούσαν κυρίως όσοι είχαν ρητορική δεινότητα. Δεν πρέπει επίσης να ξεχνάμε ότι από αυτή τη «δημοκρατία» αποκλείονταν οι γυναίκες, οι δούλοι και οι μέτοικοι. Αυτό όμως δεν μειώνει τη ριζοσπαστικότητα της ιδέας: ότι οι αποφάσεις ανήκουν σε όσους θα ζήσουν με τις συνέπειές τους.", "The herald asked: \"Tis agoreuein bouletai?\", that is, \"Who wishes to speak?\". In theory, any citizen could step up to the bema, which still survives, carved into the rock. In practice, of course, it was mainly those with rhetorical skill who spoke. We must also not forget that women, slaves and resident foreigners were excluded from this \"democracy\". But that doesn't diminish the radical nature of the idea: that decisions belong to those who will live with their consequences."),
 ],
 "questions": [
  Q("Τι γινόταν στην Πνύκα;", ["Γίνονταν θρησκευτικές τελετές", "Συνεδρίαζε η εκκλησία του δήμου", "Γίνονταν θεατρικές παραστάσεις", "Γυμνάζονταν οι στρατιώτες"], 1, "συνεδρίαζε η εκκλησία του δήμου"),
  Q("Ποιος ήταν ο σκοπός του σκοινιού βαμμένου κόκκινο;", ["Να σημαδεύει τους ξένους", "Να χωρίζει τους πολίτες σε ομάδες", "Να πιέζει τους πολίτες να έρθουν εγκαίρως στη συνέλευση", "Να μετράει τις ψήφους"], 2, "όποιος λερωνόταν, και άρα είχε καθυστερήσει, κινδύνευε με πρόστιμο"),
  Q("Γιατί θεσπίστηκε μια μικρή αποζημίωση στις αρχές του τέταρτου αιώνα;", ["Για να ενθαρρυνθεί η συμμετοχή", "Για να πληρώνονται οι ρήτορες", "Για να καλυφθούν τα έξοδα του χώρου", "Για να τιμωρηθούν οι απόντες"], 0, "ακριβώς για να ενθαρρυνθεί η συμμετοχή"),
  Q("Ποια είναι, κατά τον ιστορικό, η ριζοσπαστική ιδέα της αθηναϊκής δημοκρατίας;", ["Ότι όλοι οι κάτοικοι ψήφιζαν", "Ότι οι αποφάσεις ανήκουν σε όσους θα ζήσουν με τις συνέπειές τους", "Ότι οι στρατηγοί εκλέγονταν με κλήρο", "Ότι οι ρήτορες πληρώνονταν από την πόλη"], 1, "οι αποφάσεις ανήκουν σε όσους θα ζήσουν με τις συνέπειές τους"),
 ],
 "gloss": {"Πνύκα": "Πνύκα — the Pnyx (hill in Athens)", "βραχώδη": "βραχώδης — rocky", "συνεδρίαζε": "συνεδριάζω — to meet, be in session", "εκκλησία του δήμου": "εκκλησία του δήμου — the assembly of the Athenian people", "εξοστρακισμός": "εξοστρακισμός — ostracism", "προσέλευση": "προσέλευση — attendance, turnout", "σάρωναν": "σαρώνω — to sweep", "θεσπίστηκε": "θεσπίζω — to establish, enact", "αποζημίωση": "αποζημίωση — allowance, compensation", "κήρυκας": "κήρυκας — herald", "βήμα": "βήμα — speaker's platform; step", "δεινότητα": "δεινότητα — skill, prowess", "μέτοικοι": "μέτοικος — resident foreigner (metic)", "ριζοσπαστικότητα": "ριζοσπαστικότητα — radicalism, radical nature"}
})

rnd = random.Random(115)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-115.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
