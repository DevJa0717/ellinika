# Source for library/listening/listening-154.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l154.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l154-vm-katataktirio", "title": "Το τεστ κατάταξης στη σχολή γλωσσών", "title_en": "The placement test at the language school", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από μια σχολή ξένων γλωσσών.",
 "script": [
  L("Γραμματέας", "f", "Καλημέρα σας, από τη σχολή γλωσσών «Πολύγλωσσο». Λάβαμε την αίτησή σας για τα μαθήματα ιταλικών. Πριν σας βάλουμε σε τμήμα, πρέπει να γράψετε ένα σύντομο τεστ κατάταξης, για να δούμε σε ποιο επίπεδο είστε.", "Good morning, this is the Polyglosso language school. We have received your application for the Italian classes. Before we put you in a group, you need to take a short placement test, so we can see what level you're at."),
  L("Γραμματέας", "f", "Το τεστ γίνεται στη σχολή, διαρκεί σαράντα πέντε λεπτά και έχει γραπτό μέρος και μια μικρή συζήτηση με έναν καθηγητή. Μπορείτε να έρθετε όποιο απόγευμα θέλετε αυτή την εβδομάδα, από τις πέντε ως τις οχτώ.", "The test takes place at the school, lasts forty-five minutes and has a written part and a short conversation with a teacher. You can come any afternoon you like this week, from five to eight."),
  L("Γραμματέας", "f", "Αν προτιμάτε, υπάρχει και η δυνατότητα να το κάνετε από το σπίτι, μέσω βιντεοκλήσης, αλλά τότε θα πρέπει να κλείσετε ραντεβού τουλάχιστον μία μέρα πριν. Τα μαθήματα ξεκινούν στις δεκαπέντε του μήνα.", "If you prefer, you can also do it from home by video call, but then you'll need to book an appointment at least a day in advance. Classes start on the fifteenth of the month."),
 ],
 "questions": [
  Q("Γιατί πρέπει να γράψετε το τεστ;", ["Για να πάρετε πιστοποιητικό", "Για να δουν σε ποιο επίπεδο είστε και να σας βάλουν σε τμήμα", "Για να πάρετε έκπτωση", "Για να γίνετε καθηγητής"], 1, "για να δούμε σε ποιο επίπεδο είστε"),
  Q("Από τι αποτελείται το τεστ;", ["Από γραπτό μέρος και μια μικρή συζήτηση με έναν καθηγητή", "Μόνο από ερωτήσεις πολλαπλής επιλογής", "Από μια έκθεση", "Από μια άσκηση ακουστικής κατανόησης"], 0, "έχει γραπτό μέρος και μια μικρή συζήτηση με έναν καθηγητή"),
  Q("Τι πρέπει να κάνετε αν θέλετε να γράψετε το τεστ από το σπίτι;", ["Να στείλετε ένα email", "Να πληρώσετε επιπλέον", "Να κλείσετε ραντεβού τουλάχιστον μία μέρα πριν", "Να έρθετε πρώτα στη σχολή"], 2, "θα πρέπει να κλείσετε ραντεβού τουλάχιστον μία μέρα πριν"),
 ],
 "gloss": {"αίτησή": "αίτηση — application", "τμήμα": "τμήμα — class, group", "τεστ κατάταξης": "τεστ κατάταξης — placement test", "επίπεδο": "επίπεδο — level", "γραπτό": "γραπτός — written", "δυνατότητα": "δυνατότητα — possibility, option", "βιντεοκλήσης": "βιντεοκλήση — video call", "ραντεβού": "ραντεβού — appointment"}
})

ITEMS.append({
 "id": "l154-ann-ergastirio-apolithomaton", "title": "Εργαστήριο απολιθωμάτων για παιδιά", "title_en": "A fossil workshop for children", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός μουσείου φυσικής ιστορίας.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί επισκέπτες, σε δεκαπέντε λεπτά ξεκινά στην αίθουσα του ισογείου το εργαστήριο «Μικροί παλαιοντολόγοι», για παιδιά από έξι έως δώδεκα ετών. Τα παιδιά θα σκάψουν σε ειδικά κουτιά με άμμο και θα ανακαλύψουν αντίγραφα απολιθωμάτων.", "Dear visitors, in fifteen minutes the workshop \"Young palaeontologists\" begins in the ground-floor hall, for children aged six to twelve. The children will dig in special sandboxes and discover replica fossils."),
  L("Εκφωνήτρια", "f", "Η συμμετοχή είναι δωρεάν, αλλά οι θέσεις είναι περιορισμένες: μόνο είκοσι παιδιά σε κάθε ομάδα. Οι γονείς παρακαλούνται να συνοδεύσουν τα παιδιά μέχρι την είσοδο της αίθουσας και να τα παραλάβουν στο τέλος, σε μία ώρα.", "Participation is free, but places are limited: only twenty children per group. Parents are asked to accompany their children to the entrance of the hall and to collect them at the end, in one hour."),
  L("Εκφωνήτρια", "f", "Για όσους δεν βρουν θέση, το εργαστήριο θα επαναληφθεί στις πέντε το απόγευμα. Στο τέλος κάθε παιδί θα πάρει μαζί του ένα μικρό εκμαγείο από γύψο, που θα φτιάξει μόνο του.", "For those who don't find a place, the workshop will be repeated at five in the afternoon. At the end each child will take home a small plaster cast, which they will make themselves."),
 ],
 "questions": [
  Q("Τι θα κάνουν τα παιδιά στο εργαστήριο;", ["Θα δουν μια ταινία για τους δεινόσαυρους", "Θα σκάψουν σε κουτιά με άμμο και θα ανακαλύψουν αντίγραφα απολιθωμάτων", "Θα ζωγραφίσουν ζώα", "Θα επισκεφθούν μια ανασκαφή"], 1, "Τα παιδιά θα σκάψουν σε ειδικά κουτιά με άμμο"),
  Q("Τι πρέπει να κάνουν οι γονείς;", ["Να συνοδεύσουν τα παιδιά ως την είσοδο της αίθουσας και να τα παραλάβουν στο τέλος", "Να μείνουν μέσα στην αίθουσα", "Να πληρώσουν στο ταμείο", "Να φέρουν φαγητό"], 0, "Οι γονείς παρακαλούνται να συνοδεύσουν τα παιδιά μέχρι την είσοδο της αίθουσας"),
  Q("Τι θα πάρει κάθε παιδί στο τέλος;", ["Ένα βιβλίο", "Ένα αληθινό απολίθωμα", "Ένα μικρό εκμαγείο από γύψο που θα φτιάξει μόνο του", "Ένα εισιτήριο για το επόμενο εργαστήριο"], 2, "κάθε παιδί θα πάρει μαζί του ένα μικρό εκμαγείο από γύψο"),
 ],
 "gloss": {"παλαιοντολόγοι": "παλαιοντολόγος — palaeontologist", "σκάψουν": "σκάβω — to dig", "αντίγραφα": "αντίγραφο — copy, replica", "απολιθωμάτων": "απολίθωμα — fossil", "περιορισμένες": "περιορισμένος — limited", "συνοδεύσουν": "συνοδεύω — to accompany", "επαναληφθεί": "επαναλαμβάνομαι — to be repeated", "εκμαγείο": "εκμαγείο — cast", "γύψο": "γύψος — plaster"}
})

ITEMS.append({
 "id": "l154-dia-epeteios-goneon", "title": "Σαράντα χρόνια γάμου", "title_en": "Forty years of marriage", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο αδέλφια να συζητούν στο τηλέφωνο για την επέτειο των γονιών τους.",
 "script": [
  L("Δανάη", "f", "Θυμάσαι ότι τον Ιούνιο οι γονείς κλείνουν σαράντα χρόνια γάμου; Σκέφτηκα να τους κάνουμε μια έκπληξη.", "Do you remember that in June our parents will have been married forty years? I thought we could give them a surprise."),
  L("Μιχάλης", "m", "Ναι, το είχα στο μυαλό μου. Ένα τραπέζι με όλη την οικογένεια; Αλλά ο μπαμπάς δεν αντέχει τις μεγάλες παρέες, θα μας κρατάει μούτρα όλο το βράδυ.", "Yes, I'd had it in mind. A dinner with the whole family? But Dad can't stand big gatherings, he'll sulk all evening."),
  L("Δανάη", "f", "Γι' αυτό σκέφτηκα κάτι άλλο. Να τους στείλουμε ένα Σαββατοκύριακο στη Ζαγορά, στο ξενοδοχείο όπου πήγαν για τον μήνα του μέλιτος. Το βρήκα, λειτουργεί ακόμα!", "That's why I thought of something else. To send them for a weekend to Zagora, to the hotel where they went on their honeymoon. I found it, it's still open!"),
  L("Μιχάλης", "m", "Καταπληκτικό! Και μπορούμε να ζητήσουμε από τον ξενοδόχο να τους έχει στο δωμάτιο ένα άλμπουμ με φωτογραφίες από όλα αυτά τα χρόνια. Αναλαμβάνω εγώ να σκανάρω τις παλιές φωτογραφίες.", "Amazing! And we can ask the hotel owner to have an album of photos from all these years waiting in their room. I'll take care of scanning the old photos."),
  L("Δανάη", "f", "Τέλεια. Εγώ κλείνω το δωμάτιο. Μόνο μην πεις τίποτα στη μαμά, γιατί δεν κρατάει μυστικό ούτε πέντε λεπτά.", "Perfect. I'll book the room. Just don't say anything to Mum, because she can't keep a secret for even five minutes."),
 ],
 "questions": [
  Q("Γιατί δεν θέλουν να κάνουν τραπέζι με όλη την οικογένεια;", ["Γιατί είναι ακριβό", "Γιατί ο μπαμπάς δεν αντέχει τις μεγάλες παρέες", "Γιατί η μαμά θα είναι άρρωστη", "Γιατί δεν έχουν χώρο"], 1, "ο μπαμπάς δεν αντέχει τις μεγάλες παρέες"),
  Q("Τι προτείνει η Δανάη;", ["Ένα ταξίδι στο εξωτερικό", "Ένα Σαββατοκύριακο στο ξενοδοχείο όπου πήγαν για τον μήνα του μέλιτος", "Ένα πάρτι έκπληξη στο σπίτι", "Ένα καινούργιο αυτοκίνητο"], 1, "Να τους στείλουμε ένα Σαββατοκύριακο στη Ζαγορά, στο ξενοδοχείο όπου πήγαν για τον μήνα του μέλιτος"),
  Q("Γιατί δεν πρέπει να πουν τίποτα στη μαμά;", ["Γιατί δεν της αρέσουν οι εκπλήξεις", "Γιατί θα θυμώσει", "Γιατί δεν κρατάει μυστικό ούτε πέντε λεπτά", "Γιατί είναι στο εξωτερικό"], 2, "δεν κρατάει μυστικό ούτε πέντε λεπτά"),
 ],
 "gloss": {"γάμου": "γάμος — marriage, wedding", "έκπληξη": "έκπληξη — surprise", "μούτρα": "κρατάω μούτρα — to sulk", "μήνα του μέλιτος": "μήνας του μέλιτος — honeymoon", "λειτουργεί": "λειτουργώ — to operate, be open", "ξενοδόχο": "ξενοδόχος — hotel owner", "σκανάρω": "σκανάρω — to scan", "μυστικό": "μυστικό — secret"}
})

ITEMS.append({
 "id": "l154-int-diaititria", "title": "Μια γυναίκα με τη σφυρίχτρα", "title_en": "A woman with the whistle", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε μια αθλητική εκπομπή στο ραδιόφωνο.",
 "script": [
  L("Δημοσιογράφος", "m", "Η Κατερίνα είναι διαιτήτρια ποδοσφαίρου εδώ και δώδεκα χρόνια και φέτος σφυρίζει για πρώτη φορά αγώνες ανδρών σε επαγγελματική κατηγορία. Κατερίνα, πώς έγινες διαιτήτρια;", "Katerina has been a football referee for twelve years, and this year for the first time she is refereeing men's matches in a professional league. Katerina, how did you become a referee?"),
  L("Κατερίνα", "f", "Έπαιζα ποδόσφαιρο, αλλά στα δεκαεννιά τραυματίστηκα στο γόνατο. Ο προπονητής μου μού είπε: «Αφού δεν μπορείς να παίξεις, μάθε να σφυρίζεις». Πήγα σε ένα σεμινάριο της ένωσης διαιτητών και από τότε δεν σταμάτησα.", "I used to play football, but at nineteen I injured my knee. My coach told me: \"Since you can't play, learn to referee.\" I went to a course run by the referees' association and I haven't stopped since."),
  L("Δημοσιογράφος", "m", "Αντιμετωπίζεις διαφορετικά σχόλια από τις κερκίδες επειδή είσαι γυναίκα;", "Do you get different comments from the stands because you're a woman?"),
  L("Κατερίνα", "f", "Στην αρχή, σίγουρα. Άκουγα να μου λένε να πάω στην κουζίνα. Τώρα πια όμως με βρίζουν όπως και τους άντρες συναδέλφους μου, μόνο για τις αποφάσεις μου! Το θεωρώ πρόοδο.", "At the beginning, definitely. I'd hear them telling me to go to the kitchen. But now they insult me just like my male colleagues, only for my decisions! I consider that progress."),
  L("Κατερίνα", "f", "Το πιο δύσκολο είναι η φυσική κατάσταση. Σε έναν αγώνα τρέχω πάνω από δέκα χιλιόμετρα, γι' αυτό προπονούμαι πέντε μέρες την εβδομάδα, πριν ή μετά τη δουλειά μου ως λογίστρια.", "The hardest thing is fitness. In a match I run more than ten kilometres, so I train five days a week, before or after my job as an accountant."),
 ],
 "questions": [
  Q("Πώς έγινε η Κατερίνα διαιτήτρια;", ["Τη βρήκε η ομοσπονδία", "Μετά από έναν τραυματισμό στο γόνατο, την παρότρυνε ο προπονητής της", "Ήταν διαιτητής ο πατέρας της", "Το διάβασε σε μια αγγελία"], 1, "στα δεκαεννιά τραυματίστηκα στο γόνατο"),
  Q("Τι λέει για τα σχόλια από τις κερκίδες σήμερα;", ["Ότι τη βρίζουν όπως και τους άντρες, μόνο για τις αποφάσεις της", "Ότι δεν ακούει τίποτα", "Ότι την προσβάλλουν συνέχεια επειδή είναι γυναίκα", "Ότι οι οπαδοί τη χειροκροτούν"], 0, "με βρίζουν όπως και τους άντρες συναδέλφους μου, μόνο για τις αποφάσεις μου"),
  Q("Τι είναι το πιο δύσκολο για εκείνη;", ["Οι αποφάσεις", "Τα ταξίδια", "Η φυσική κατάσταση", "Οι κανονισμοί"], 2, "Το πιο δύσκολο είναι η φυσική κατάσταση"),
 ],
 "gloss": {"διαιτήτρια": "διαιτήτρια — referee (female)", "σφυρίζει": "σφυρίζω — to whistle; to referee", "κατηγορία": "κατηγορία — division, league", "τραυματίστηκα": "τραυματίζομαι — to be injured", "γόνατο": "γόνατο — knee", "ένωσης": "ένωση — association", "κερκίδες": "κερκίδα — stand (in a stadium)", "βρίζουν": "βρίζω — to insult, swear at", "πρόοδο": "πρόοδος — progress", "φυσική κατάσταση": "φυσική κατάσταση — fitness", "λογίστρια": "λογίστρια — accountant"}
})

ITEMS.append({
 "id": "l154-news-allagi-oras", "title": "Τα ρολόγια πάνε μία ώρα πίσω", "title_en": "The clocks go back an hour", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα δελτίο ειδήσεων στο ραδιόφωνο, λίγο πριν από το τέλος του Οκτωβρίου.",
 "script": [
  L("Εκφωνητής", "m", "Τα ξημερώματα της Κυριακής τελειώνει η θερινή ώρα: στις τέσσερις τα ρολόγια θα γυρίσουν μία ώρα πίσω, στις τρεις. Τα κινητά τηλέφωνα και οι υπολογιστές θα αλλάξουν ώρα αυτόματα, αλλά τα ρολόγια του τοίχου και του αυτοκινήτου πρέπει να τα αλλάξουμε μόνοι μας.", "In the early hours of Sunday summer time ends: at four o'clock the clocks will go back one hour, to three. Mobile phones and computers will change automatically, but we have to change wall clocks and car clocks ourselves."),
  L("Εκφωνητής", "m", "Οι γιατροί συμβουλεύουν όσους δυσκολεύονται με την αλλαγή να πηγαίνουν για ύπνο λίγο αργότερα τις επόμενες μέρες και να βγαίνουν στο φως το πρωί. Τα παιδιά και οι ηλικιωμένοι χρειάζονται συνήθως περισσότερες μέρες για να προσαρμοστούν.", "Doctors advise those who find the change hard to go to bed a little later over the next few days and to get out into the light in the morning. Children and older people usually need more days to adjust."),
  L("Εκφωνητής", "m", "Υπενθυμίζουμε ότι η Ευρωπαϊκή Ένωση συζητά εδώ και χρόνια την κατάργηση της αλλαγής ώρας, αλλά μέχρι σήμερα δεν έχει υπάρξει συμφωνία ανάμεσα στα κράτη-μέλη για το ποια ώρα θα κρατήσουν.", "We remind you that the European Union has for years been discussing abolishing the clock change, but so far there has been no agreement among member states on which time to keep."),
 ],
 "questions": [
  Q("Τι θα γίνει τα ξημερώματα της Κυριακής;", ["Τα ρολόγια θα πάνε μία ώρα μπροστά", "Τα ρολόγια θα γυρίσουν μία ώρα πίσω", "Θα κοπεί το ρεύμα", "Θα αλλάξει η ώρα μόνο στα κινητά"], 1, "στις τέσσερις τα ρολόγια θα γυρίσουν μία ώρα πίσω, στις τρεις"),
  Q("Τι συμβουλεύουν οι γιατροί;", ["Να πηγαίνουμε για ύπνο λίγο αργότερα και να βγαίνουμε στο φως το πρωί", "Να παίρνουμε υπνωτικά", "Να μην πίνουμε καφέ", "Να κοιμόμαστε το μεσημέρι"], 0, "να πηγαίνουν για ύπνο λίγο αργότερα τις επόμενες μέρες και να βγαίνουν στο φως το πρωί"),
  Q("Γιατί δεν έχει καταργηθεί η αλλαγή ώρας στην Ευρωπαϊκή Ένωση;", ["Γιατί κανείς δεν το ζήτησε", "Γιατί κοστίζει πολύ", "Γιατί δεν υπάρχει συμφωνία για το ποια ώρα θα κρατήσουν", "Γιατί η Ελλάδα διαφωνεί"], 2, "δεν έχει υπάρξει συμφωνία ανάμεσα στα κράτη-μέλη για το ποια ώρα θα κρατήσουν"),
 ],
 "gloss": {"ξημερώματα": "ξημερώματα — early hours of the morning", "θερινή ώρα": "θερινή ώρα — summer time", "ρολόγια": "ρολόι — clock", "αυτόματα": "αυτόματα — automatically", "συμβουλεύουν": "συμβουλεύω — to advise", "προσαρμοστούν": "προσαρμόζομαι — to adjust", "κατάργηση": "κατάργηση — abolition", "κράτη-μέλη": "κράτος-μέλος — member state"}
})

ITEMS.append({
 "id": "l154-mono-na-leo-ochi", "title": "Πώς έμαθα να λέω όχι", "title_en": "How I learned to say no", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλάει σε ένα podcast για την ψυχολογία της καθημερινότητας.",
 "script": [
  L("Βάσω", "f", "Για χρόνια έλεγα ναι σε όλα. Να κρατήσω το παιδί της γειτόνισσας, να μείνω στη δουλειά ως αργά, να οργανώσω το πάρτι του γραφείου. Στο τέλος δεν είχα χρόνο ούτε για ένα καφέ με τον εαυτό μου.", "For years I said yes to everything. To mind my neighbour's child, to stay late at work, to organise the office party. In the end I didn't have time even for a coffee with myself."),
  L("Βάσω", "f", "Η αλλαγή ήρθε όταν αρρώστησα από την κούραση. Ο γιατρός μου με ρώτησε: «Πόσες από αυτές τις υποχρεώσεις τις διάλεξες εσύ;» Δεν ήξερα τι να απαντήσω.", "The change came when I got ill from exhaustion. My doctor asked me: \"How many of these obligations did you choose yourself?\" I didn't know what to answer."),
  L("Βάσω", "f", "Τώρα έχω έναν απλό κανόνα: δεν απαντάω ποτέ αμέσως. Λέω «άσε με να το σκεφτώ» και αποφασίζω την επόμενη μέρα. Τις περισσότερες φορές η απάντηση εξακολουθεί να είναι ναι, αλλά τώρα είναι δική μου επιλογή. Και όσοι με αγαπούν δεν θύμωσαν όταν άκουσαν το πρώτο μου όχι.", "Now I have a simple rule: I never answer straight away. I say \"let me think about it\" and decide the next day. Most of the time the answer is still yes, but now it's my own choice. And those who love me didn't get angry when they heard my first no."),
 ],
 "questions": [
  Q("Ποιο ήταν το πρόβλημα της Βάσως;", ["Δεν είχε φίλους", "Έλεγε ναι σε όλα και δεν είχε χρόνο για τον εαυτό της", "Δεν της άρεσε η δουλειά της", "Μάλωνε με τη γειτόνισσα"], 1, "Για χρόνια έλεγα ναι σε όλα"),
  Q("Τι τη ρώτησε ο γιατρός της;", ["Πόσες ώρες κοιμάται", "Αν κάνει γυμναστική", "Πόσες από τις υποχρεώσεις της τις διάλεξε η ίδια", "Αν παίρνει φάρμακα"], 2, "Πόσες από αυτές τις υποχρεώσεις τις διάλεξες εσύ;"),
  Q("Ποιος είναι ο κανόνας της σήμερα;", ["Δεν απαντάει ποτέ αμέσως, αποφασίζει την επόμενη μέρα", "Λέει πάντα όχι", "Δεν σηκώνει το τηλέφωνο", "Βοηθάει μόνο την οικογένειά της"], 0, "δεν απαντάω ποτέ αμέσως"),
 ],
 "gloss": {"κρατήσω": "κρατάω (παιδί) — to mind, babysit", "οργανώσω": "οργανώνω — to organise", "κούραση": "κούραση — exhaustion, tiredness", "υποχρεώσεις": "υποχρέωση — obligation", "εξακολουθεί": "εξακολουθώ — to continue, still be", "επιλογή": "επιλογή — choice", "θύμωσαν": "θυμώνω — to get angry"}
})

ITEMS.append({
 "id": "l154-rep-kinito-tachydromeio", "title": "Το ταχυδρομείο που πηγαίνει στα χωριά", "title_en": "The post office that goes to the villages", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για την ύπαιθρο.",
 "script": [
  L("Ρεπόρτερ", "f", "Σε πολλά ορεινά χωριά τα καταστήματα των ταχυδρομείων έκλεισαν τα τελευταία χρόνια. Σε έναν δήμο της Πελοποννήσου βρήκαν μια λύση: ένα μικρό φορτηγάκι, εξοπλισμένο σαν ταχυδρομικό γραφείο, που επισκέπτεται δεκαοχτώ χωριά.", "In many mountain villages the post office branches closed in recent years. In one municipality in the Peloponnese they found a solution: a small van, equipped like a post office, which visits eighteen villages."),
  L("Ρεπόρτερ", "f", "Το κινητό ταχυδρομείο σταματά σε κάθε χωριό μία φορά την εβδομάδα, πάντα την ίδια μέρα και ώρα, συνήθως στην πλατεία. Οι κάτοικοι μπορούν να στείλουν δέματα, να πληρώσουν λογαριασμούς και να παραλάβουν τη σύνταξή τους.", "The mobile post office stops in each village once a week, always on the same day and at the same time, usually in the square. Residents can send parcels, pay bills and collect their pension."),
  L("Ρεπόρτερ", "f", "«Πριν, έπρεπε να πάρω το λεωφορείο για την πόλη, και αυτό περνούσε δύο φορές την εβδομάδα», λέει μια ογδοντάχρονη κάτοικος. Ο υπάλληλος που οδηγεί το φορτηγάκι λέει ότι συχνά κάνει και άλλες δουλειές: διαβάζει γράμματα σε όσους δεν βλέπουν καλά και τους βοηθά να συμπληρώσουν έντυπα.", "\"Before, I had to take the bus to town, and that came twice a week,\" says an eighty-year-old resident. The employee who drives the van says he often does other jobs too: he reads letters to those who can't see well and helps them fill in forms."),
 ],
 "questions": [
  Q("Ποια λύση βρήκε ο δήμος;", ["Άνοιξε ξανά τα παλιά καταστήματα", "Ένα φορτηγάκι εξοπλισμένο σαν ταχυδρομικό γραφείο", "Ένα ταχυδρομείο στο διαδίκτυο", "Γραμματοκιβώτια σε κάθε σπίτι"], 1, "ένα μικρό φορτηγάκι, εξοπλισμένο σαν ταχυδρομικό γραφείο"),
  Q("Πόσο συχνά σταματά σε κάθε χωριό;", ["Κάθε μέρα", "Μία φορά τον μήνα", "Μία φορά την εβδομάδα, την ίδια μέρα και ώρα", "Όταν το καλέσουν οι κάτοικοι"], 2, "σταματά σε κάθε χωριό μία φορά την εβδομάδα, πάντα την ίδια μέρα και ώρα"),
  Q("Ποιες άλλες δουλειές κάνει συχνά ο υπάλληλος;", ["Διαβάζει γράμματα σε όσους δεν βλέπουν καλά και βοηθά με τα έντυπα", "Πουλάει εφημερίδες", "Μεταφέρει ασθενείς", "Επισκευάζει σπίτια"], 0, "διαβάζει γράμματα σε όσους δεν βλέπουν καλά και τους βοηθά να συμπληρώσουν έντυπα"),
 ],
 "gloss": {"ταχυδρομείων": "ταχυδρομείο — post office", "φορτηγάκι": "φορτηγάκι — small van", "εξοπλισμένο": "εξοπλισμένος — equipped", "δέματα": "δέμα — parcel", "λογαριασμούς": "λογαριασμός — bill", "παραλάβουν": "παραλαμβάνω — to collect", "σύνταξή": "σύνταξη — pension", "υπάλληλος": "υπάλληλος — employee, clerk", "έντυπα": "έντυπο — form"}
})

ITEMS.append({
 "id": "l154-dia-potisma-fyton", "title": "Ποιος θα ποτίζει τα φυτά όσο λείπουμε;", "title_en": "Who will water the plants while we're away?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο γείτονες να μιλούν στη σκάλα της πολυκατοικίας.",
 "script": [
  L("Ελένη", "f", "Κυρία Φωτεινή, μπορώ να σας ζητήσω μια χάρη; Φεύγουμε τον Αύγουστο για τρεις εβδομάδες στην Κρήτη, και ανησυχώ για τα φυτά στο μπαλκόνι.", "Mrs Fotini, can I ask you a favour? We're leaving for Crete for three weeks in August, and I'm worried about the plants on the balcony."),
  L("Κυρία Φωτεινή", "f", "Φυσικά, παιδί μου. Πόσο συχνά θέλουν πότισμα;", "Of course, dear. How often do they need watering?"),
  L("Ελένη", "f", "Οι ντομάτες και ο βασιλικός κάθε βράδυ, γιατί με τη ζέστη ξεραίνονται αμέσως. Οι κάκτοι δεν θέλουν σχεδόν τίποτα, μία φορά την εβδομάδα το πολύ. Θα σας γράψω ένα χαρτάκι για να μην μπερδευτείτε.", "The tomatoes and the basil every evening, because in the heat they dry out at once. The cacti need almost nothing, once a week at most. I'll write you a little note so you don't get confused."),
  L("Κυρία Φωτεινή", "f", "Και τις ντομάτες που θα ωριμάσουν τι να τις κάνω;", "And the tomatoes that ripen, what should I do with them?"),
  L("Ελένη", "f", "Να τις φάτε, φυσικά! Θα σας αφήσω και το κλειδί του διαμερίσματος, για να ανοίγετε το παράθυρο της κουζίνας και να αερίζεται λίγο το σπίτι. Και σας έφερα από τώρα ένα μικρό ευχαριστώ: ένα κουτί λουκούμια από τη Σύρο.", "Eat them, of course! I'll also leave you the key to the flat, so you can open the kitchen window and air the place a little. And I've brought you a little thank-you already: a box of loukoumi from Syros."),
 ],
 "questions": [
  Q("Πόσο συχνά θέλουν πότισμα οι ντομάτες και ο βασιλικός;", ["Μία φορά την εβδομάδα", "Κάθε βράδυ", "Κάθε δεύτερη μέρα", "Μόνο όταν δεν βρέχει"], 1, "Οι ντομάτες και ο βασιλικός κάθε βράδυ"),
  Q("Τι θα αφήσει η Ελένη στην κυρία Φωτεινή για να μη μπερδευτεί;", ["Ένα χαρτάκι με οδηγίες", "Ένα βίντεο", "Τον αριθμό του τηλεφώνου ενός κηπουρού", "Ένα ημερολόγιο"], 0, "Θα σας γράψω ένα χαρτάκι για να μην μπερδευτείτε"),
  Q("Γιατί θα της αφήσει και το κλειδί του διαμερίσματος;", ["Για να ποτίζει τα φυτά του σαλονιού", "Για να παίρνει την αλληλογραφία", "Για να ανοίγει το παράθυρο της κουζίνας και να αερίζεται το σπίτι", "Για να ταΐζει τη γάτα"], 2, "για να ανοίγετε το παράθυρο της κουζίνας και να αερίζεται λίγο το σπίτι"),
 ],
 "gloss": {"χάρη": "χάρη — favour", "πότισμα": "πότισμα — watering", "βασιλικός": "βασιλικός — basil", "ξεραίνονται": "ξεραίνομαι — to dry out", "κάκτοι": "κάκτος — cactus", "χαρτάκι": "χαρτάκι — little note", "μπερδευτείτε": "μπερδεύομαι — to get confused", "ωριμάσουν": "ωριμάζω — to ripen", "αερίζεται": "αερίζομαι — to be aired", "λουκούμια": "λουκούμι — loukoumi (Turkish delight)"}
})

ITEMS.append({
 "id": "l154-c1-gell-mann", "title": "Γιατί ξεχνάμε τα λάθη των εφημερίδων", "title_en": "Why we forget the papers' mistakes", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από συνέντευξη μιας καθηγήτριας δημοσιογραφίας σε μια εκπομπή για τα μέσα ενημέρωσης.",
 "script": [
  L("Δημοσιογράφος", "m", "Μιλήσατε για την «αμνησία Γκελ-Μαν». Τι ακριβώς είναι;", "You talked about \"Gell-Mann amnesia\". What exactly is it?"),
  L("Καθηγήτρια", "f", "Τον όρο τον επινόησε ο συγγραφέας Μάικλ Κράιτον σε μια ομιλία του το 2002, και τον ονόμασε έτσι αστειευόμενος, από τον φυσικό Μάρεϊ Γκελ-Μαν. Περιέγραψε κάτι που όλοι έχουμε ζήσει. Διαβάζεις ένα άρθρο για ένα θέμα που ξέρεις πολύ καλά, ας πούμε τη δουλειά σου, και διαπιστώνεις ότι είναι γεμάτο λάθη και παρανοήσεις.", "The term was coined by the writer Michael Crichton in a talk in 2002, and he named it, half joking, after the physicist Murray Gell-Mann. He described something we have all experienced. You read an article on a subject you know very well, say your own job, and you find that it's full of mistakes and misunderstandings."),
  L("Καθηγήτρια", "f", "Ύστερα γυρίζεις σελίδα, στο άρθρο για την εξωτερική πολιτική ή την οικονομία, και το διαβάζεις σαν να είναι απολύτως αξιόπιστο. Έχεις ήδη ξεχάσει ότι η ίδια εφημερίδα μόλις σου έδειξε πόσο εύκολα κάνει λάθη.", "Then you turn the page to the article on foreign policy or the economy, and you read it as if it were completely reliable. You've already forgotten that the same newspaper has just shown you how easily it makes mistakes."),
  L("Καθηγήτρια", "f", "Πρέπει να πω ότι δεν πρόκειται για επιστημονικά αποδεδειγμένο φαινόμενο, αλλά για μια εύστοχη παρατήρηση. Και το συμπέρασμα δεν είναι να μην εμπιστευόμαστε κανέναν. Είναι να διαβάζουμε με την ίδια κριτική ματιά και τα θέματα που δεν γνωρίζουμε.", "I should say that this isn't a scientifically proven phenomenon, but an apt observation. And the conclusion isn't that we should trust no one. It's that we should read with the same critical eye the subjects we don't know about too."),
 ],
 "questions": [
  Q("Ποιος επινόησε τον όρο;", ["Ο φυσικός Μάρεϊ Γκελ-Μαν", "Ο συγγραφέας Μάικλ Κράιτον", "Μια ομάδα δημοσιογράφων", "Ένας ψυχολόγος"], 1, "Τον όρο τον επινόησε ο συγγραφέας Μάικλ Κράιτον"),
  Q("Τι διαπιστώνουμε όταν διαβάζουμε για ένα θέμα που ξέρουμε καλά;", ["Ότι είναι πολύ ακριβές", "Ότι είναι πολύ μεγάλο", "Ότι είναι γεμάτο λάθη και παρανοήσεις", "Ότι δεν έχει υπογραφή"], 2, "είναι γεμάτο λάθη και παρανοήσεις"),
  Q("Τι κάνουμε μετά, σύμφωνα με την καθηγήτρια;", ["Διαβάζουμε τα υπόλοιπα άρθρα σαν να είναι απολύτως αξιόπιστα", "Σταματάμε να διαβάζουμε την εφημερίδα", "Γράφουμε στην εφημερίδα", "Ελέγχουμε όλα τα άρθρα"], 0, "το διαβάζεις σαν να είναι απολύτως αξιόπιστο"),
  Q("Ποιο είναι το συμπέρασμα της καθηγήτριας;", ["Να μην εμπιστευόμαστε κανέναν", "Να διαβάζουμε μόνο ειδικούς", "Να αγοράζουμε περισσότερες εφημερίδες", "Να διαβάζουμε με την ίδια κριτική ματιά και τα θέματα που δεν γνωρίζουμε"], 3, "Είναι να διαβάζουμε με την ίδια κριτική ματιά και τα θέματα που δεν γνωρίζουμε"),
 ],
 "gloss": {"αμνησία": "αμνησία — amnesia", "επινόησε": "επινοώ — to coin, invent", "αστειευόμενος": "αστειεύομαι — to joke", "φυσικό": "φυσικός — physicist", "διαπιστώνεις": "διαπιστώνω — to find, realise", "παρανοήσεις": "παρανόηση — misunderstanding", "αξιόπιστο": "αξιόπιστος — reliable", "αποδεδειγμένο": "αποδεδειγμένος — proven", "εύστοχη": "εύστοχος — apt, to the point", "κριτική ματιά": "κριτική ματιά — critical eye"}
})

ITEMS.append({
 "id": "l154-c1-provoleas", "title": "Κανείς δεν κοιτάζει τόσο όσο νομίζουμε", "title_en": "Nobody is looking as much as we think", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια ομιλία για την κοινωνική ψυχολογία.",
 "script": [
  L("Ομιλητής", "m", "Έχετε μπει ποτέ σε μια αίθουσα με έναν λεκέ στο πουκάμισο και νιώσατε ότι όλοι τον κοιτάζουν; Οι ψυχολόγοι το ονομάζουν «φαινόμενο του προβολέα»: έχουμε την εντύπωση ότι βρισκόμαστε κάτω από ένα φως που μας ακολουθεί, ενώ οι άλλοι ασχολούνται κυρίως με τον εαυτό τους.", "Have you ever walked into a room with a stain on your shirt and felt that everyone was looking at it? Psychologists call it the \"spotlight effect\": we have the impression that we are under a light that follows us, while others are mostly busy with themselves."),
  L("Ομιλητής", "m", "Σε ένα γνωστό πείραμα του 2000, ο Τόμας Γκίλοβιτς και οι συνεργάτες του έβαλαν φοιτητές να φορέσουν ένα μπλουζάκι με το πρόσωπο ενός τραγουδιστή που οι συμφοιτητές τους θεωρούσαν μάλλον ντεμοντέ, και να μπουν σε μια αίθουσα γεμάτη κόσμο.", "In a well-known experiment in 2000, Thomas Gilovich and his colleagues had students put on a T-shirt with the face of a singer their fellow students considered rather uncool, and walk into a room full of people."),
  L("Ομιλητής", "m", "Οι φοιτητές πίστευαν ότι περίπου οι μισοί παρόντες θα πρόσεχαν το μπλουζάκι. Στην πραγματικότητα το πρόσεξε μόνο περίπου ένας στους τέσσερις. Υπερεκτιμούσαν, δηλαδή, κατά πολύ την προσοχή που τους έδιναν οι άλλοι.", "The students believed that about half of those present would notice the T-shirt. In reality only about one in four noticed it. In other words, they greatly overestimated the attention others were paying them."),
  L("Ομιλητής", "m", "Αυτό ισχύει και για τα λάθη μας: μια κομπιαστή φράση σε μια παρουσίαση μας απασχολεί για μέρες, ενώ οι περισσότεροι ακροατές την έχουν ξεχάσει πριν βγουν από την αίθουσα. Το να το γνωρίζουμε αυτό είναι, νομίζω, μια μικρή απελευθέρωση.", "The same goes for our mistakes: a stumbling sentence in a presentation bothers us for days, while most listeners have forgotten it before they leave the room. Knowing this is, I think, a small liberation."),
 ],
 "questions": [
  Q("Τι είναι το «φαινόμενο του προβολέα»;", ["Ο φόβος του σκοταδιού", "Η εντύπωση ότι οι άλλοι μας προσέχουν περισσότερο απ' ό,τι στην πραγματικότητα", "Η τάση να κοιτάζουμε τους άλλους", "Η ανάγκη να είμαστε στο κέντρο της προσοχής"], 1, "έχουμε την εντύπωση ότι βρισκόμαστε κάτω από ένα φως που μας ακολουθεί"),
  Q("Τι έκαναν οι φοιτητές στο πείραμα;", ["Έδωσαν μια ομιλία", "Τραγούδησαν μπροστά σε κοινό", "Φόρεσαν ένα μπλουζάκι με το πρόσωπο ενός μάλλον ντεμοντέ τραγουδιστή και μπήκαν σε μια αίθουσα", "Λέρωσαν τα πουκάμισά τους"], 2, "έβαλαν φοιτητές να φορέσουν ένα μπλουζάκι"),
  Q("Πόσοι πρόσεξαν πραγματικά το μπλουζάκι;", ["Περίπου ένας στους τέσσερις", "Οι μισοί", "Σχεδόν όλοι", "Κανένας"], 0, "το πρόσεξε μόνο περίπου ένας στους τέσσερις"),
  Q("Γιατί, κατά τον ομιλητή, η γνώση αυτή είναι μια μικρή απελευθέρωση;", ["Γιατί μας κάνει πιο δημοφιλείς", "Γιατί μας βοηθά να ντυνόμαστε καλύτερα", "Γιατί μας μαθαίνει να κρίνουμε τους άλλους", "Γιατί οι άλλοι ξεχνούν γρήγορα τα λάθη μας"], 3, "οι περισσότεροι ακροατές την έχουν ξεχάσει πριν βγουν από την αίθουσα"),
 ],
 "gloss": {"λεκέ": "λεκές — stain", "προβολέα": "προβολέας — spotlight", "εντύπωση": "εντύπωση — impression", "μπλουζάκι": "μπλουζάκι — T-shirt", "ντεμοντέ": "ντεμοντέ — old-fashioned, uncool", "παρόντες": "παρών — present (person)", "Υπερεκτιμούσαν": "υπερεκτιμώ — to overestimate", "κομπιαστή": "κομπιαστός — halting, stumbling", "απασχολεί": "απασχολώ — to occupy, preoccupy", "απελευθέρωση": "απελευθέρωση — liberation"}
})

rnd = random.Random(154)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-154.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
