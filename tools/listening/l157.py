# Source for library/listening/listening-157.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l157.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l157-ann-pagodromio", "title": "Ανακοίνωση στο παγοδρόμιο", "title_en": "An announcement at the ice rink", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός παγοδρομίου.",
 "script": [
  L("Εκφωνητής", "m", "Αγαπητοί πατινέρ, σε δέκα λεπτά η πίστα θα κλείσει για είκοσι λεπτά, για να περάσει το μηχάνημα που ισιώνει τον πάγο. Παρακαλούμε, όταν ακούσετε το κουδούνι, να βγείτε όλοι από την πίστα από την έξοδο δίπλα στο κυλικείο.", "Dear skaters, in ten minutes the rink will close for twenty minutes so that the machine that smooths the ice can go over it. When you hear the bell, please all leave the rink by the exit next to the snack bar."),
  L("Εκφωνητής", "m", "Όσοι έχετε νοικιάσει παγοπέδιλα, μπορείτε να τα κρατήσετε κατά τη διάρκεια του διαλείμματος. Το εισιτήριό σας ισχύει για όλη την απογευματινή βάρδια, μέχρι τις οκτώ.", "Those of you who have rented skates can keep them during the break. Your ticket is valid for the whole afternoon session, until eight."),
  L("Εκφωνητής", "m", "Υπενθυμίζουμε ότι για τα παιδιά κάτω των δέκα ετών το κράνος είναι υποχρεωτικό. Κράνη δίνονται δωρεάν στο γκισέ των παγοπέδιλων. Επίσης, το Σάββατο το πρωί ξεκινούν μαθήματα για αρχάριους· οι εγγραφές γίνονται στο ταμείο.", "We remind you that for children under ten a helmet is compulsory. Helmets are given free of charge at the skate counter. Also, on Saturday morning, lessons for beginners begin; you can sign up at the ticket office."),
 ],
 "questions": [
  Q("Γιατί θα κλείσει η πίστα για είκοσι λεπτά;", ["Για να καθαριστούν οι κερκίδες", "Για να περάσει το μηχάνημα που ισιώνει τον πάγο", "Για μια επίδειξη καλλιτεχνικού πατινάζ", "Επειδή τελειώνει η βάρδια"], 1, "για να περάσει το μηχάνημα που ισιώνει τον πάγο"),
  Q("Τι ισχύει για το εισιτήριο;", ["Ισχύει μόνο μέχρι το διάλειμμα", "Ισχύει για όλη την απογευματινή βάρδια", "Πρέπει να αγοραστεί καινούργιο μετά το διάλειμμα", "Ισχύει και για το Σάββατο"], 1, "Το εισιτήριό σας ισχύει για όλη την απογευματινή βάρδια"),
  Q("Τι πρέπει να φορούν τα παιδιά κάτω των δέκα ετών;", ["Γάντια", "Επιγονατίδες", "Κράνος", "Ζεστό μπουφάν"], 2, "το κράνος είναι υποχρεωτικό"),
 ],
 "gloss": {"παγοδρομίου": "παγοδρόμιο — ice rink", "πατινέρ": "πατινέρ — skater", "πίστα": "πίστα — rink, track", "ισιώνει": "ισιώνω — to smooth, to level", "κυλικείο": "κυλικείο — snack bar", "παγοπέδιλα": "παγοπέδιλο — ice skate", "βάρδια": "βάρδια — session, shift", "υποχρεωτικό": "υποχρεωτικός — compulsory", "γκισέ": "γκισέ — counter", "αρχάριους": "αρχάριος — beginner"},
})

ITEMS.append({
 "id": "l157-int-alpakas", "title": "Αλπακά στο βουνό", "title_en": "Alpacas in the mountains", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε τοπικό ραδιόφωνο με μια κτηνοτρόφο που εκτρέφει αλπακά σε ένα ορεινό χωριό.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς βρέθηκαν αλπακά σε ένα ελληνικό χωριό;", "How did alpacas end up in a Greek village?"),
  L("Κτηνοτρόφος", "f", "Δούλευα δέκα χρόνια σε γραφείο στην πόλη. Όταν πέθανε ο πατέρας μου, γύρισα στο χωριό και δεν ήθελα να κάνω ό,τι έκανε εκείνος, δηλαδή κατσίκια. Είχα δει αλπακά σε ένα ταξίδι στο Περού και σκέφτηκα ότι το κλίμα του βουνού μας τους ταιριάζει.", "I worked in an office in the city for ten years. When my father died, I went back to the village and didn't want to do what he had done, that is, goats. I had seen alpacas on a trip to Peru and thought that the climate of our mountain suits them."),
  L("Δημοσιογράφος", "m", "Τι κερδίζετε από αυτά τα ζώα;", "What do you earn from these animals?"),
  L("Κτηνοτρόφος", "f", "Κυρίως το μαλλί τους. Τα κουρεύουμε μία φορά τον χρόνο, την άνοιξη. Το μαλλί του αλπακά δεν έχει λανολίνη, όπως του προβάτου, οπότε ενοχλεί λιγότερο όσους έχουν ευαίσθητο δέρμα. Το πλένουμε, το γνέθουμε και πουλάμε νήματα και πλεκτά.", "Mainly their wool. We shear them once a year, in spring. Alpaca wool has no lanolin, unlike sheep's wool, so it bothers people with sensitive skin less. We wash it, spin it, and sell yarn and knitwear."),
  L("Δημοσιογράφος", "m", "Και είναι αλήθεια ότι φτύνουν;", "And is it true that they spit?"),
  L("Κτηνοτρόφος", "f", "Φτύνουν, αλλά σχεδόν πάντα το ένα το άλλο, όταν μαλώνουν για το φαγητό. Τους ανθρώπους σπάνια. Τα σαββατοκύριακα έρχονται σχολεία και οικογένειες για να τα γνωρίσουν, και αυτό έχει γίνει πια το μισό μας εισόδημα.", "They spit, but almost always at each other, when they fight over food. Rarely at people. At weekends schools and families come to meet them, and that has now become half our income."),
 ],
 "questions": [
  Q("Γιατί η κτηνοτρόφος δεν ασχολήθηκε με κατσίκια;", ["Γιατί δεν ήθελε να κάνει ό,τι έκανε ο πατέρας της", "Γιατί το κλίμα δεν τα ευνοεί", "Γιατί είναι αλλεργική σε αυτά", "Γιατί δεν βγάζουν χρήματα"], 0, "δεν ήθελα να κάνω ό,τι έκανε εκείνος"),
  Q("Γιατί, σύμφωνα με την κτηνοτρόφο, το μαλλί του αλπακά ενοχλεί λιγότερο το δέρμα;", ["Γιατί είναι πιο χοντρό", "Γιατί δεν έχει λανολίνη", "Γιατί πλένεται πολλές φορές", "Γιατί βάφεται με φυσικά χρώματα"], 1, "δεν έχει λανολίνη"),
  Q("Από πού προέρχεται πια το μισό τους εισόδημα;", ["Από την πώληση ζώων", "Από τα νήματα", "Από τις επισκέψεις σχολείων και οικογενειών", "Από το κρέας"], 2, "Τα σαββατοκύριακα έρχονται σχολεία και οικογένειες"),
 ],
 "gloss": {"εκτρέφει": "εκτρέφω — to breed, to raise", "κτηνοτρόφο": "κτηνοτρόφος — livestock farmer", "κουρεύουμε": "κουρεύω — to shear", "λανολίνη": "λανολίνη — lanolin", "ευαίσθητο": "ευαίσθητος — sensitive", "γνέθουμε": "γνέθω — to spin (wool)", "νήματα": "νήμα — yarn, thread", "πλεκτά": "πλεκτό — knitwear", "φτύνουν": "φτύνω — to spit", "εισόδημα": "εισόδημα — income"},
})

ITEMS.append({
 "id": "l157-dia-escape-room", "title": "Ένα δωμάτιο απόδρασης για τα γενέθλια", "title_en": "An escape room for the birthday", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλους να συζητούν πώς θα γιορτάσουν τα γενέθλια ενός κοινού τους φίλου.",
 "script": [
  L("Ελπίδα", "f", "Για τα γενέθλια του Στέλιου σκέφτηκα να πάμε σε ένα δωμάτιο απόδρασης. Σε κλειδώνουν σε ένα δωμάτιο και έχεις μία ώρα να λύσεις γρίφους για να βγεις.", "For Stelios's birthday I thought we could go to an escape room. They lock you in a room and you have an hour to solve puzzles to get out."),
  L("Νίκος", "m", "Ωραία ιδέα, αλλά ο Στέλιος δεν αντέχει τους κλειστούς χώρους. Θυμάσαι τι έγινε στο ασανσέρ πέρσι;", "Nice idea, but Stelios can't stand enclosed spaces. Remember what happened in the lift last year?"),
  L("Ελπίδα", "f", "Το ρώτησα. Η πόρτα στην πραγματικότητα δεν κλειδώνει· αν κάποιος θέλει να βγει, βγαίνει όποτε θέλει. Και υπάρχει κάμερα, ο υπάλληλος σε βλέπει συνέχεια και σου δίνει βοήθεια αν κολλήσεις.", "I asked about it. The door doesn't actually lock; if someone wants to get out, they can leave whenever they like. And there's a camera; the staff member watches you all the time and gives you help if you get stuck."),
  L("Νίκος", "m", "Τότε εντάξει. Πόσα άτομα χωράει;", "Then fine. How many people does it take?"),
  L("Ελπίδα", "f", "Από τρία ως έξι. Εμείς είμαστε οκτώ, οπότε ή χωριζόμαστε σε δύο ομάδες και παίζουμε σε δύο δωμάτια, ή πηγαίνουμε μόνο οι πιο στενοί φίλοι.", "From three to six. We're eight, so either we split into two teams and play in two rooms, or only the closest friends go."),
  L("Νίκος", "m", "Δύο ομάδες, σίγουρα. Και όποια ομάδα βγει πρώτη, κερνάει η άλλη την τούρτα.", "Two teams, definitely. And whichever team gets out first, the other one pays for the cake."),
 ],
 "questions": [
  Q("Τι ανησυχεί τον Νίκο;", ["Το κόστος", "Ότι ο Στέλιος δεν αντέχει τους κλειστούς χώρους", "Ότι οι γρίφοι είναι πολύ δύσκολοι", "Ότι το μαγαζί είναι μακριά"], 1, "ο Στέλιος δεν αντέχει τους κλειστούς χώρους"),
  Q("Τι έμαθε η Ελπίδα για την πόρτα;", ["Ότι ανοίγει μόνο με κωδικό", "Ότι στην πραγματικότητα δεν κλειδώνει", "Ότι ανοίγει ύστερα από μισή ώρα", "Ότι μένει ανοιχτή"], 1, "Η πόρτα στην πραγματικότητα δεν κλειδώνει"),
  Q("Τι αποφασίζουν τελικά;", ["Να πάνε μόνο οι πιο στενοί φίλοι", "Να πάνε σε εστιατόριο", "Να χωριστούν σε δύο ομάδες", "Να το αναβάλουν"], 2, "Δύο ομάδες, σίγουρα"),
 ],
 "gloss": {"απόδρασης": "απόδραση — escape", "κλειδώνουν": "κλειδώνω — to lock", "γρίφους": "γρίφος — puzzle, riddle", "αντέχει": "αντέχω — to bear, to stand", "κλειστούς χώρους": "κλειστός χώρος — enclosed space", "ασανσέρ": "ασανσέρ — lift, elevator", "κολλήσεις": "κολλάω — to get stuck", "χωριζόμαστε": "χωρίζομαι — to split up", "στενοί": "στενός (φίλος) — close (friend)", "κερνάει": "κερνάω — to treat, to pay for"},
})

ITEMS.append({
 "id": "l157-vm-korniza", "title": "Μήνυμα από το κορνιζάδικο", "title_en": "A message from the frame shop", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από το κατάστημα όπου αφήσατε μια παλιά φωτογραφία για κορνίζα.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, από το κορνιζάδικο σας παίρνω, για τη φωτογραφία του γάμου των παππούδων σας. Όταν τη βγάλαμε από το παλιό τζάμι, είδαμε ότι είχε πάθει υγρασία στη μία γωνία.", "Good morning, I'm calling from the frame shop about the photograph of your grandparents' wedding. When we took it out from behind the old glass, we saw that it had suffered damp in one corner."),
  L("Υπάλληλος", "f", "Δεν θέλαμε να την κόψουμε χωρίς να σας ρωτήσουμε. Μια λύση είναι να τη σκανάρουμε και να τυπώσουμε ένα αντίγραφο σε ειδικό χαρτί, και την αυθεντική να τη φυλάξετε σε φάκελο χωρίς οξέα. Κοστίζει δεκαπέντε ευρώ παραπάνω.", "We didn't want to cut it without asking you. One solution is to scan it and print a copy on special paper, and keep the original in an acid-free envelope. It costs fifteen euros more."),
  L("Υπάλληλος", "f", "Αν θέλετε να μπει η αυθεντική στην κορνίζα, θα βάλουμε τζάμι που προστατεύει από τον ήλιο. Πείτε μας τι προτιμάτε ως την Παρασκευή, γιατί από Δευτέρα κλείνουμε για απογραφή.", "If you want the original to go in the frame, we'll use glass that protects from the sun. Tell us what you prefer by Friday, because from Monday we're closed for stocktaking."),
 ],
 "questions": [
  Q("Τι πρόβλημα βρήκαν στη φωτογραφία;", ["Ήταν σκισμένη στη μέση", "Είχε πάθει υγρασία στη μία γωνία", "Είχε ξεθωριάσει από τον ήλιο", "Ήταν κολλημένη στο τζάμι"], 1, "είχε πάθει υγρασία στη μία γωνία"),
  Q("Τι προτείνει η υπάλληλος για την αυθεντική φωτογραφία;", ["Να φυλαχτεί σε φάκελο χωρίς οξέα", "Να κοπεί η γωνία", "Να ξαναβαφτεί", "Να μπει σε άλμπουμ"], 0, "την αυθεντική να τη φυλάξετε σε φάκελο χωρίς οξέα"),
  Q("Γιατί πρέπει να απαντήσετε ως την Παρασκευή;", ["Γιατί αυξάνονται οι τιμές", "Γιατί από Δευτέρα κλείνουν για απογραφή", "Γιατί φεύγει για διακοπές η υπάλληλος", "Γιατί τελειώνει το ειδικό χαρτί"], 1, "από Δευτέρα κλείνουμε για απογραφή"),
 ],
 "gloss": {"κορνίζα": "κορνίζα — picture frame", "κορνιζάδικο": "κορνιζάδικο — frame shop", "τζάμι": "τζάμι — glass (pane)", "υγρασία": "υγρασία — damp, humidity", "σκανάρουμε": "σκανάρω — to scan", "αντίγραφο": "αντίγραφο — copy", "αυθεντική": "αυθεντικός — original, authentic", "οξέα": "οξύ — acid", "προστατεύει": "προστατεύω — to protect", "απογραφή": "απογραφή — stocktaking, inventory"},
})

ITEMS.append({
 "id": "l157-vm-vulkanizater", "title": "Τα λάστιχα θέλουν αλλαγή", "title_en": "The tyres need changing", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από το βουλκανιζατέρ όπου πήγατε το αυτοκίνητο για ένα σκασμένο λάστιχο.",
 "script": [
  L("Τεχνίτης", "m", "Γεια σας, ο Μανώλης από το βουλκανιζατέρ. Το λάστιχο που είχε σκάσει το φτιάξαμε· ήταν ένα καρφί και κλείστηκε χωρίς πρόβλημα.", "Hello, it's Manolis from the tyre shop. We fixed the tyre that had a puncture; it was a nail and it was sealed without any problem."),
  L("Τεχνίτης", "m", "Όμως, κοιτάξαμε και τα άλλα τρία, και τα δύο μπροστινά έχουν φαγωθεί πολύ στην εσωτερική πλευρά. Αυτό σημαίνει ότι το αυτοκίνητο θέλει ευθυγράμμιση. Αν αλλάξετε μόνο τα λάστιχα, σε λίγους μήνες θα φαγωθούν πάλι.", "But we also looked at the other three, and the two front ones are very worn on the inner side. That means the car needs a wheel alignment. If you only change the tyres, they'll wear out again in a few months."),
  L("Τεχνίτης", "m", "Εμείς ευθυγράμμιση δεν κάνουμε, αλλά σας προτείνω ένα συνεργείο εδώ δίπλα. Το αυτοκίνητο είναι έτοιμο, μπορείτε να το πάρετε από τις τέσσερις και μετά.", "We don't do alignment ourselves, but I can recommend a garage right next door. The car is ready; you can pick it up from four o'clock onwards."),
 ],
 "questions": [
  Q("Τι είχε προκαλέσει το σκάσιμο του λάστιχου;", ["Ένα κομμάτι γυαλί", "Ένα καρφί", "Μια λακκούβα", "Η μεγάλη ζέστη"], 1, "ήταν ένα καρφί"),
  Q("Τι δείχνει, κατά τον τεχνίτη, η φθορά στα μπροστινά λάστιχα;", ["Ότι το αυτοκίνητο θέλει ευθυγράμμιση", "Ότι τα λάστιχα ήταν φτηνά", "Ότι ο οδηγός φρενάρει απότομα", "Ότι η πίεση ήταν χαμηλή"], 0, "το αυτοκίνητο θέλει ευθυγράμμιση"),
  Q("Πότε μπορείτε να πάρετε το αυτοκίνητο;", ["Αμέσως", "Από τις τέσσερις και μετά", "Αύριο το πρωί", "Μετά την ευθυγράμμιση"], 1, "μπορείτε να το πάρετε από τις τέσσερις και μετά"),
 ],
 "gloss": {"βουλκανιζατέρ": "βουλκανιζατέρ — tyre repair shop", "σκασμένο": "σκασμένος — punctured, burst", "λάστιχο": "λάστιχο — tyre", "καρφί": "καρφί — nail", "μπροστινά": "μπροστινός — front", "φαγωθεί": "τρώγομαι — to wear out", "εσωτερική": "εσωτερικός — inner", "ευθυγράμμιση": "ευθυγράμμιση — (wheel) alignment", "συνεργείο": "συνεργείο — garage, repair shop"},
})

ITEMS.append({
 "id": "l157-mon-synodos-piano", "title": "Συνοδεύοντας τους άλλους", "title_en": "Accompanying others", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια πιανίστρια να μιλάει σε μια εκπομπή για τη δουλειά της ως συνοδός σε ωδείο.",
 "script": [
  L("Πιανίστρια", "f", "Όταν ήμουν φοιτήτρια, ονειρευόμουν να δίνω ρεσιτάλ σε μεγάλες αίθουσες. Τελικά, εδώ και είκοσι χρόνια, είμαι συνοδός στο πιάνο: παίζω μαζί με τραγουδιστές, βιολονίστες και φλαουτίστες, στα μαθήματα, στις εξετάσεις και στις συναυλίες τους.", "When I was a student, I dreamed of giving recitals in big halls. In the end, for twenty years now, I've been a piano accompanist: I play together with singers, violinists and flautists, in their lessons, exams and concerts."),
  L("Πιανίστρια", "f", "Πολλοί νομίζουν ότι ο συνοδός απλώς παίζει από πίσω. Στην πραγματικότητα πρέπει να ακούς τον άλλον συνέχεια. Αν ο τραγουδιστής πάρει ανάσα πιο αργά, περιμένεις· αν ξεχάσει μια φράση, συνεχίζεις σαν να μην έγινε τίποτα.", "Many people think the accompanist just plays in the background. In reality you have to listen to the other person all the time. If the singer takes a breath later, you wait; if they forget a phrase, you carry on as if nothing happened."),
  L("Πιανίστρια", "f", "Το πιο δύσκολο είναι ότι μια εβδομάδα πριν από τις εξετάσεις μπορεί να μου δώσουν δέκα καινούργια κομμάτια. Το πιο όμορφο είναι όταν ένας νέος μουσικός, που έτρεμε στην πρόβα, βγαίνει στη σκηνή και ηρεμεί επειδή ξέρει ότι είμαι εκεί.", "The hardest thing is that a week before exams I may be given ten new pieces. The most beautiful thing is when a young musician who was trembling at the rehearsal goes on stage and calms down because they know I'm there."),
 ],
 "questions": [
  Q("Τι ονειρευόταν η πιανίστρια ως φοιτήτρια;", ["Να διδάσκει σε ωδείο", "Να δίνει ρεσιτάλ σε μεγάλες αίθουσες", "Να γράφει μουσική για ταινίες", "Να τραγουδάει"], 1, "ονειρευόμουν να δίνω ρεσιτάλ σε μεγάλες αίθουσες"),
  Q("Τι κάνει ο καλός συνοδός, αν ο τραγουδιστής ξεχάσει μια φράση;", ["Σταματάει και ξεκινάει από την αρχή", "Του ψιθυρίζει τα λόγια", "Συνεχίζει σαν να μην έγινε τίποτα", "Παίζει πιο δυνατά"], 2, "συνεχίζεις σαν να μην έγινε τίποτα"),
  Q("Ποιο είναι για εκείνη το πιο δύσκολο κομμάτι της δουλειάς;", ["Οι πολλές ώρες στο ωδείο", "Τα καινούργια κομμάτια που της δίνουν λίγο πριν από τις εξετάσεις", "Το άγχος της σκηνής", "Οι χαμηλές αμοιβές"], 1, "μια εβδομάδα πριν από τις εξετάσεις μπορεί να μου δώσουν δέκα καινούργια κομμάτια"),
 ],
 "gloss": {"πιανίστρια": "πιανίστρια — (female) pianist", "συνοδός": "συνοδός — accompanist", "ωδείο": "ωδείο — conservatory, music school", "ρεσιτάλ": "ρεσιτάλ — recital", "βιολονίστες": "βιολονίστας — violinist", "φλαουτίστες": "φλαουτίστας — flautist", "ανάσα": "ανάσα — breath", "κομμάτια": "κομμάτι — (musical) piece", "έτρεμε": "τρέμω — to tremble", "πρόβα": "πρόβα — rehearsal"},
})

ITEMS.append({
 "id": "l157-dia-kourtines", "title": "Κουρτίνες ή στόρια;", "title_en": "Curtains or blinds?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητάει τι θα βάλει στα παράθυρα του καινούργιου του σπιτιού.",
 "script": [
  L("Σοφία", "f", "Για το σαλόνι εγώ θέλω μακριές κουρτίνες, ως το πάτωμα. Κάνουν το δωμάτιο πιο ζεστό και πιο ψηλό.", "For the living room I want long curtains, down to the floor. They make the room warmer and taller."),
  L("Άρης", "m", "Ωραίες είναι, αλλά μαζεύουν σκόνη, και με τη γάτα θα γίνουν κουρέλια σε έναν μήνα. Γιατί δεν βάζουμε στόρια; Ανεβαίνουν και κατεβαίνουν, και ρυθμίζεις όσο φως θέλεις.", "They're nice, but they gather dust, and with the cat they'll be in tatters in a month. Why don't we put up blinds? They go up and down, and you can adjust as much light as you want."),
  L("Σοφία", "f", "Στόρια στην κουζίνα και στο μπάνιο, σύμφωνοι. Στο σαλόνι, όμως, το πρωί ο ήλιος μπαίνει πολύ δυνατός. Θέλω κάτι βαρύ που να τον κόβει εντελώς τα καλοκαίρια.", "Blinds in the kitchen and bathroom, agreed. In the living room, though, the sun comes in very strong in the morning. I want something heavy that blocks it completely in summer."),
  L("Άρης", "m", "Τότε ας βάλουμε στόρι συσκότισης και από πάνω μια λεπτή κουρτίνα για ομορφιά, ψηλά από το πάτωμα, να μην τη φτάνει η γάτα.", "Then let's put up a blackout blind and, over it, a thin curtain for looks, hanging high off the floor so the cat can't reach it."),
 ],
 "questions": [
  Q("Γιατί θέλει η Σοφία μακριές κουρτίνες στο σαλόνι;", ["Γιατί είναι φτηνότερες", "Γιατί κάνουν το δωμάτιο πιο ζεστό και πιο ψηλό", "Γιατί καθαρίζονται εύκολα", "Γιατί της αρέσουν στη μητέρα της"], 1, "Κάνουν το δωμάτιο πιο ζεστό και πιο ψηλό"),
  Q("Ποιο πρόβλημα βλέπει ο Άρης στις κουρτίνες;", ["Ότι κρατάνε τη μυρωδιά", "Ότι μαζεύουν σκόνη και θα τις χαλάσει η γάτα", "Ότι είναι δύσκολο να τοποθετηθούν", "Ότι κρύβουν τη θέα"], 1, "μαζεύουν σκόνη, και με τη γάτα θα γίνουν κουρέλια"),
  Q("Ποια λύση προτείνει τελικά ο Άρης για το σαλόνι;", ["Μόνο μακριές κουρτίνες", "Μόνο απλά στόρια", "Στόρι συσκότισης με μια λεπτή κουρτίνα από πάνω", "Παντζούρια"], 2, "ας βάλουμε στόρι συσκότισης και από πάνω μια λεπτή κουρτίνα"),
 ],
 "gloss": {"κουρτίνες": "κουρτίνα — curtain", "στόρια": "στόρι — blind", "σκόνη": "σκόνη — dust", "κουρέλια": "κουρέλι — rag; γίνομαι κουρέλι = to be in tatters", "ρυθμίζεις": "ρυθμίζω — to adjust", "σύμφωνοι": "σύμφωνος — agreed", "εντελώς": "εντελώς — completely", "συσκότισης": "συσκότιση — blackout", "λεπτή": "λεπτός — thin"},
})

ITEMS.append({
 "id": "l157-int-filarmoniki", "title": "Τρομπόνι στη φιλαρμονική", "title_en": "Trombone in the town band", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν συνταξιούχο που παίζει τρομπόνι στη φιλαρμονική του δήμου του.",
 "script": [
  L("Δημοσιογράφος", "f", "Πόσα χρόνια παίζετε στη φιλαρμονική;", "How many years have you been playing in the town band?"),
  L("Μουσικός", "m", "Μπήκα στα δώδεκα, ως μαθητής. Οι φιλαρμονικές των δήμων τότε, όπως και σήμερα, έδιναν δωρεάν μαθήματα στα παιδιά, και έτσι πολλοί από εμάς μάθαμε μουσική χωρίς να πληρώσουμε δραχμή. Μετά έφυγα για δουλειά και γύρισα στα εξήντα, όταν βγήκα στη σύνταξη.", "I joined at twelve, as a pupil. Town bands back then, as today, gave free lessons to children, and so many of us learned music without paying a drachma. Then I left for work and came back at sixty, when I retired."),
  L("Δημοσιογράφος", "f", "Πού σας ακούει ο κόσμος;", "Where do people hear you?"),
  L("Μουσικός", "m", "Στις παρελάσεις των εθνικών εορτών, στις λιτανείες, στον Επιτάφιο τη Μεγάλη Παρασκευή, αλλά και σε συναυλίες στην πλατεία το καλοκαίρι, όπου παίζουμε από εμβατήρια μέχρι κινηματογραφική μουσική.", "In the parades on national holidays, in religious processions, at the Epitaphios on Good Friday, but also in concerts in the square in summer, where we play everything from marches to film music."),
  L("Δημοσιογράφος", "f", "Είναι δύσκολο όργανο το τρομπόνι;", "Is the trombone a difficult instrument?"),
  L("Μουσικός", "m", "Δεν έχει κλειδιά όπως η τρομπέτα· αλλάζεις τη νότα μετακινώντας τον βραχίονα. Άρα το αυτί σου πρέπει να είναι πολύ καλό. Και στην παρέλαση πρέπει να προσέχεις να μη χτυπήσεις με τον βραχίονα αυτόν που περπατάει μπροστά σου!", "It doesn't have valves like the trumpet; you change the note by moving the slide. So your ear has to be very good. And in the parade you have to be careful not to hit the person walking in front of you with the slide!"),
 ],
 "questions": [
  Q("Πώς έμαθε μουσική ο μουσικός;", ["Με ιδιαίτερα μαθήματα", "Με δωρεάν μαθήματα της φιλαρμονικής", "Μόνος του, από βιβλία", "Στο στρατό"], 1, "έδιναν δωρεάν μαθήματα στα παιδιά"),
  Q("Πότε γύρισε στη φιλαρμονική;", ["Στα είκοσι", "Όταν άλλαξε δουλειά", "Όταν βγήκε στη σύνταξη", "Όταν άρχισε να μαθαίνει το εγγόνι του"], 2, "γύρισα στα εξήντα, όταν βγήκα στη σύνταξη"),
  Q("Γιατί, κατά τον μουσικό, χρειάζεται πολύ καλό αυτί το τρομπόνι;", ["Γιατί αλλάζεις τη νότα μετακινώντας τον βραχίονα", "Γιατί παίζει πάντα μόνο του", "Γιατί είναι πολύ δυνατό", "Γιατί δεν έχει παρτιτούρες"], 0, "αλλάζεις τη νότα μετακινώντας τον βραχίονα"),
 ],
 "gloss": {"τρομπόνι": "τρομπόνι — trombone", "φιλαρμονική": "φιλαρμονική — (municipal) brass band", "σύνταξη": "σύνταξη — pension; βγαίνω στη σύνταξη = to retire", "παρελάσεις": "παρέλαση — parade", "λιτανείες": "λιτανεία — religious procession", "Επιτάφιο": "Επιτάφιος — Epitaphios (Good Friday bier procession)", "εμβατήρια": "εμβατήριο — march", "κλειδιά": "κλειδί — (instrument) valve, key", "βραχίονα": "βραχίονας — (trombone) slide; arm", "τρομπέτα": "τρομπέτα — trumpet"},
})

ITEMS.append({
 "id": "l157-c1-flynn", "title": "Γινόμαστε πιο έξυπνοι;", "title_en": "Are we getting smarter?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από διάλεξη για την ψυχολογία της νοημοσύνης.",
 "script": [
  L("Καθηγήτρια", "f", "Τη δεκαετία του 1980 ο Νεοζηλανδός πολιτικός επιστήμονας Τζέιμς Φλιν πρόσεξε κάτι παράξενο. Τα τεστ νοημοσύνης αναθεωρούνται κάθε τόσο, ώστε ο μέσος όρος να παραμένει εκατό. Όταν όμως σύγκρινε τις ακατέργαστες βαθμολογίες, είδε ότι κάθε γενιά απαντούσε σωστά σε περισσότερες ερωτήσεις από την προηγούμενη.", "In the 1980s the New Zealand political scientist James Flynn noticed something strange. IQ tests are revised every so often so that the average stays at one hundred. But when he compared the raw scores, he saw that each generation answered more questions correctly than the one before."),
  L("Καθηγήτρια", "f", "Σε πολλές χώρες η άνοδος έφτανε περίπου τις τρεις μονάδες ανά δεκαετία στη διάρκεια του εικοστού αιώνα, και ήταν μεγαλύτερη στα τεστ αφηρημένης σκέψης παρά στα τεστ λεξιλογίου ή αριθμητικής. Αν το πάρουμε κατά γράμμα, οι προπαππούδες μας θα έμοιαζαν, με τα σημερινά κριτήρια, σχεδόν σαν να είχαν νοητική υστέρηση· κάτι προφανώς παράλογο.", "In many countries the rise came to about three points per decade during the twentieth century, and it was greater on tests of abstract reasoning than on vocabulary or arithmetic tests. Taken literally, our great-grandparents would look, by today's standards, almost as if they had an intellectual disability, which is obviously absurd."),
  L("Καθηγήτρια", "f", "Γι' αυτό οι περισσότεροι ερευνητές δεν μιλούν για βιολογική αλλαγή, αλλά για αλλαγή στο περιβάλλον: καλύτερη διατροφή, περισσότερα χρόνια σχολείου, μικρότερες οικογένειες, και μια καθημερινότητα που μας εκπαιδεύει να ταξινομούμε και να σκεφτόμαστε με υποθέσεις. Ο ίδιος ο Φλιν έλεγε ότι δεν γίναμε πιο ευφυείς, αλλά φορέσαμε, όπως το έθεσε, «επιστημονικά γυαλιά».", "That's why most researchers do not speak of a biological change but of a change in the environment: better nutrition, more years of schooling, smaller families, and a daily life that trains us to classify and to reason with hypotheticals. Flynn himself said that we did not become more intelligent but, as he put it, put on 'scientific spectacles'."),
  L("Καθηγήτρια", "f", "Το ενδιαφέρον είναι ότι από τη δεκαετία του 1990 σε ορισμένες χώρες, όπως η Νορβηγία και η Δανία, οι βαθμολογίες των στρατευσίμων άρχισαν να πέφτουν. Μια νορβηγική μελέτη βρήκε την πτώση ακόμη και ανάμεσα σε αδέλφια της ίδιας οικογένειας, πράγμα που δείχνει και πάλι προς περιβαλλοντικές αιτίες, αν και ποιες ακριβώς είναι ακόμη ανοιχτό ερώτημα.", "What is interesting is that since the 1990s in some countries, such as Norway and Denmark, the scores of conscripts began to fall. A Norwegian study found the decline even among brothers of the same family, which again points to environmental causes, though exactly which ones is still an open question."),
 ],
 "questions": [
  Q("Τι παρατήρησε ο Φλιν στις ακατέργαστες βαθμολογίες;", ["Ότι ο μέσος όρος έμενε πάντα εκατό", "Ότι κάθε γενιά απαντούσε σωστά σε περισσότερες ερωτήσεις από την προηγούμενη", "Ότι οι γυναίκες ξεπερνούσαν τους άνδρες", "Ότι τα τεστ λεξιλογίου έδειχναν τη μεγαλύτερη άνοδο"], 1, "κάθε γενιά απαντούσε σωστά σε περισσότερες ερωτήσεις από την προηγούμενη"),
  Q("Σε ποια τεστ ήταν μεγαλύτερη η άνοδος;", ["Στα τεστ αριθμητικής", "Στα τεστ λεξιλογίου", "Στα τεστ αφηρημένης σκέψης", "Στα τεστ μνήμης"], 2, "ήταν μεγαλύτερη στα τεστ αφηρημένης σκέψης"),
  Q("Τι εννοούσε ο Φλιν με τα «επιστημονικά γυαλιά»;", ["Ότι η όραση των ανθρώπων βελτιώθηκε", "Ότι δεν γίναμε πιο ευφυείς, αλλά συνηθίσαμε έναν άλλο τρόπο σκέψης", "Ότι οι επιστήμονες έκαναν λάθη στις μετρήσεις", "Ότι τα τεστ έγιναν πιο εύκολα"], 1, "δεν γίναμε πιο ευφυείς"),
  Q("Γιατί η νορβηγική μελέτη με τα αδέλφια δείχνει προς περιβαλλοντικές αιτίες;", ["Γιατί η πτώση βρέθηκε ακόμη και ανάμεσα σε αδέλφια της ίδιας οικογένειας", "Γιατί τα αδέλφια είχαν διαφορετικούς γονείς", "Γιατί η πτώση σταμάτησε μετά το 2000", "Γιατί αφορούσε μόνο μετανάστες"], 0, "βρήκε την πτώση ακόμη και ανάμεσα σε αδέλφια της ίδιας οικογένειας"),
 ],
 "gloss": {"νοημοσύνης": "νοημοσύνη — intelligence", "αναθεωρούνται": "αναθεωρούμαι — to be revised", "ακατέργαστες": "ακατέργαστος — raw, unprocessed", "αφηρημένης": "αφηρημένος — abstract", "κατά γράμμα": "κατά γράμμα — literally", "νοητική υστέρηση": "νοητική υστέρηση — intellectual disability (dated term)", "παράλογο": "παράλογος — absurd", "ταξινομούμε": "ταξινομώ — to classify", "ευφυείς": "ευφυής — intelligent", "έθεσε": "θέτω — to put (it); όπως το έθεσε = as he put it", "στρατευσίμων": "στρατεύσιμος — conscript"},
})

ITEMS.append({
 "id": "l157-c1-allee", "title": "Όταν είναι λίγοι, χάνονται πιο γρήγορα", "title_en": "When there are few, they vanish faster", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια οικολόγο για το λεγόμενο φαινόμενο Άλι.",
 "script": [
  L("Δημοσιογράφος", "m", "Συνήθως λέμε ότι όσο λιγότερα είναι τα ζώα ενός είδους, τόσο περισσότερη τροφή αντιστοιχεί στο καθένα. Δεν θα έπρεπε, λοιπόν, ένας μικρός πληθυσμός να ανακάμπτει εύκολα;", "We usually say that the fewer animals of a species there are, the more food there is for each. Shouldn't a small population, then, recover easily?"),
  L("Οικολόγος", "f", "Αυτή είναι η κλασική εικόνα, αλλά για πολλά είδη δεν ισχύει. Ήδη τη δεκαετία του 1930 ο Αμερικανός οικολόγος Γουόρντερ Άλι παρατήρησε σε πειράματα ότι χρυσόψαρα σε ομάδα άντεχαν καλύτερα σε νερό με τοξική ουσία από ό,τι μόνα τους. Γενικεύοντας, φαινόμενο Άλι λέμε την περίπτωση όπου, κάτω από ένα ορισμένο μέγεθος, ο πληθυσμός όχι μόνο δεν ανακάμπτει, αλλά μειώνεται ακόμη πιο γρήγορα.", "That's the classic picture, but for many species it doesn't hold. As early as the 1930s the American ecologist Warder Allee observed in experiments that goldfish in a group withstood water containing a toxic substance better than on their own. Generalising, we call the Allee effect the case where, below a certain size, a population not only fails to recover but declines even faster."),
  L("Δημοσιογράφος", "m", "Γιατί συμβαίνει αυτό;", "Why does that happen?"),
  L("Οικολόγος", "f", "Για διάφορους λόγους. Όταν τα άτομα είναι αραιά, δυσκολεύονται να βρουν ταίρι. Τα σουρικάτα χρειάζονται φρουρούς που να προειδοποιούν για τα αρπακτικά, κι αυτό δεν γίνεται με τρία ζώα. Τα αφρικανικά άγρια σκυλιά κυνηγούν σε αγέλη· αν η αγέλη μικρύνει πολύ, δεν μπορούν να κυνηγήσουν και ταυτόχρονα να φυλάνε τα κουτάβια τους.", "For various reasons. When individuals are scattered, they struggle to find a mate. Meerkats need sentinels to warn of predators, and that can't be done with three animals. African wild dogs hunt in packs; if the pack gets too small, they can't hunt and guard their pups at the same time."),
  L("Οικολόγος", "f", "Για την προστασία της φύσης αυτό έχει πρακτική σημασία: δεν αρκεί να σώσουμε μερικά ζώα. Αν ο πληθυσμός πέσει κάτω από ένα κατώφλι, μπορεί να συνεχίσει να μειώνεται ακόμη κι αν σταματήσουμε το κυνήγι. Πολλοί ερευνητές πιστεύουν ότι κάτι τέτοιο συνέβαλε στον αφανισμό του επιβατικού περιστεριού στην Αμερική, που κάποτε μετριόταν σε δισεκατομμύρια.", "For nature conservation this matters in practice: it is not enough to save a few animals. If the population falls below a threshold, it may keep declining even if we stop hunting. Many researchers believe something like this contributed to the extinction of the passenger pigeon in America, which once numbered in the billions."),
 ],
 "questions": [
  Q("Ποια είναι, σύμφωνα με τον δημοσιογράφο, η συνηθισμένη αντίληψη;", ["Ότι οι μικροί πληθυσμοί εξαφανίζονται πάντα", "Ότι ένας μικρός πληθυσμός θα έπρεπε να ανακάμπτει εύκολα, αφού υπάρχει περισσότερη τροφή για καθένα", "Ότι τα ζώα ζουν καλύτερα σε ομάδες", "Ότι η τροφή δεν παίζει ρόλο"], 1, "όσο λιγότερα είναι τα ζώα ενός είδους, τόσο περισσότερη τροφή αντιστοιχεί στο καθένα"),
  Q("Τι παρατήρησε ο Άλι στα πειράματά του;", ["Ότι τα χρυσόψαρα ζούσαν περισσότερο μόνα τους", "Ότι τα χρυσόψαρα σε ομάδα άντεχαν καλύτερα σε νερό με τοξική ουσία", "Ότι η τοξική ουσία δεν επηρέαζε τα ψάρια", "Ότι τα ψάρια μάλωναν σε ομάδες"], 1, "χρυσόψαρα σε ομάδα άντεχαν καλύτερα σε νερό με τοξική ουσία"),
  Q("Γιατί δυσκολεύονται τα σουρικάτα όταν είναι πολύ λίγα;", ["Γιατί δεν βρίσκουν τροφή", "Γιατί δεν υπάρχουν αρκετοί φρουροί για να προειδοποιούν για τα αρπακτικά", "Γιατί χάνουν τις φωλιές τους", "Γιατί αρρωσταίνουν πιο συχνά"], 1, "Τα σουρικάτα χρειάζονται φρουρούς που να προειδοποιούν για τα αρπακτικά"),
  Q("Ποιο πρακτικό συμπέρασμα βγάζει η οικολόγος για την προστασία της φύσης;", ["Ότι αρκεί να σταματήσει το κυνήγι", "Ότι κάτω από ένα κατώφλι ο πληθυσμός μπορεί να συνεχίσει να μειώνεται ακόμη κι αν σταματήσει το κυνήγι", "Ότι πρέπει να μεταφέρουμε τα ζώα σε ζωολογικούς κήπους", "Ότι τα μικρά είδη δεν κινδυνεύουν"], 1, "μπορεί να συνεχίσει να μειώνεται ακόμη κι αν σταματήσουμε το κυνήγι"),
 ],
 "gloss": {"πληθυσμός": "πληθυσμός — population", "ανακάμπτει": "ανακάμπτω — to recover", "χρυσόψαρα": "χρυσόψαρο — goldfish", "τοξική": "τοξικός — toxic", "Γενικεύοντας": "γενικεύω — to generalise", "αραιά": "αραιός — sparse, scattered", "ταίρι": "ταίρι — mate", "σουρικάτα": "σουρικάτα — meerkat", "αρπακτικά": "αρπακτικό — predator", "αγέλη": "αγέλη — pack, herd", "κατώφλι": "κατώφλι — threshold", "αφανισμό": "αφανισμός — extinction, wiping out", "επιβατικού περιστεριού": "επιβατικό περιστέρι — passenger pigeon"},
})

rnd = random.Random(157)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-157.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
