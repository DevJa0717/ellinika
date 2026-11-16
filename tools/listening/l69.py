# Source for library/listening/listening-69.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l69.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l69-ann-agonas-basket", "title": "Πριν από το τζάμπολ", "title_en": "Before the tip-off", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα κλειστό γήπεδο για έναν αγώνα μπάσκετ. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνητής", "m", "Καλησπέρα σας και καλώς ήρθατε στο κλειστό γήπεδο. Λόγω καθυστέρησης της πτήσης της φιλοξενούμενης ομάδας, το τζάμπολ του αγώνα μετατίθεται για τις εννιά παρά τέταρτο, δηλαδή σαράντα πέντε λεπτά αργότερα από την αρχική ώρα.", "Good evening and welcome to the indoor arena. Because the visiting team's flight was delayed, the tip-off of the game is moved to a quarter to nine, that is forty-five minutes later than the original time."),
  L("Εκφωνητής", "m", "Οι κάτοχοι διαρκείας μπορούν να βγουν από το γήπεδο και να ξαναμπούν, δείχνοντας την κάρτα τους στην είσοδο. Όσοι έχουν εισιτήριο ημέρας θα πρέπει να κρατήσουν το βραχιόλι που τους δόθηκε στην είσοδο· χωρίς αυτό δεν θα επιτρέπεται η επανείσοδος.", "Season-ticket holders may leave the arena and come back in by showing their card at the entrance. Those with a day ticket must keep the wristband they were given at the entrance; without it re-entry will not be allowed."),
  L("Εκφωνητής", "m", "Το κυλικείο θα μείνει ανοιχτό και στο ημίχρονο. Υπενθυμίζουμε ότι απαγορεύεται η είσοδος με γυάλινα μπουκάλια και καπνογόνα. Ευχαριστούμε για την κατανόηση.", "The snack bar will also stay open at half-time. We remind you that glass bottles and flares are not allowed into the arena. Thank you for your understanding."),
 ],
 "questions": [
  Q("Γιατί καθυστερεί ο αγώνας;", ["Λόγω βλάβης στους προβολείς", "Λόγω καθυστέρησης της πτήσης της φιλοξενούμενης ομάδας", "Λόγω επεισοδίων", "Λόγω τηλεοπτικής μετάδοσης"], 1, "Λόγω καθυστέρησης της πτήσης της φιλοξενούμενης ομάδας"),
  Q("Τι πρέπει να κάνουν όσοι έχουν εισιτήριο ημέρας, για να ξαναμπούν;", ["Να αγοράσουν νέο εισιτήριο", "Να δείξουν την ταυτότητά τους", "Να κρατήσουν το βραχιόλι που τους δόθηκε", "Να μπουν από άλλη είσοδο"], 2, "θα πρέπει να κρατήσουν το βραχιόλι που τους δόθηκε στην είσοδο"),
  Q("Τι απαγορεύεται;", ["Τα γυάλινα μπουκάλια και τα καπνογόνα", "Το φαγητό από το κυλικείο", "Οι σημαίες των ομάδων", "Οι φωτογραφίες"], 0, "απαγορεύεται η είσοδος με γυάλινα μπουκάλια και καπνογόνα"),
 ],
 "gloss": {"τζάμπολ": "τζάμπολ — tip-off", "φιλοξενούμενης": "φιλοξενούμενος — visiting (team)", "μετατίθεται": "μετατίθεμαι — to be moved, postponed", "κάτοχοι διαρκείας": "κάτοχος (εισιτηρίου) διαρκείας — season-ticket holder", "βραχιόλι": "βραχιόλι — wristband, bracelet", "επανείσοδος": "επανείσοδος — re-entry", "κυλικείο": "κυλικείο — snack bar", "ημίχρονο": "ημίχρονο — half-time", "καπνογόνα": "καπνογόνο — flare"},
})

ITEMS.append({
 "id": "l69-vm-fotografies-gamou", "title": "Οι φωτογραφίες του γάμου είναι έτοιμες", "title_en": "The wedding photos are ready", "type": "voicemail", "level": "B2",
 "context_el": "Παντρευτήκατε πριν από δύο μήνες. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τον φωτογράφο του γάμου.",
 "script": [
  L("Φωτογράφος", "m", "Γεια σας, ο Άρης είμαι, ο φωτογράφος. Σας έχω καλά νέα: οι φωτογραφίες του γάμου σας είναι έτοιμες. Σας έστειλα ήδη στο ηλεκτρονικό ταχυδρομείο έναν σύνδεσμο, απ’ όπου μπορείτε να τις κατεβάσετε σε υψηλή ανάλυση. Ο σύνδεσμος θα ισχύει για τριάντα μέρες.", "Hello, it's Aris, the photographer. I have good news: your wedding photos are ready. I've already emailed you a link from which you can download them in high resolution. The link will be valid for thirty days."),
  L("Φωτογράφος", "m", "Για το άλμπουμ, χρειάζομαι να μου διαλέξετε εξήντα φωτογραφίες. Μπορείτε απλώς να βάλετε μια καρδούλα σε όσες θέλετε μέσα στη σελίδα. Το εξώφυλλο το προτείνω δερμάτινο, σε μπεζ χρώμα, αλλά αν προτιμάτε κάτι άλλο, πείτε μου.", "For the album, I need you to choose sixty photos. You can simply put a heart on the ones you want on the page. For the cover I suggest leather, in beige, but if you prefer something else, let me know."),
  L("Φωτογράφος", "m", "Το άλμπουμ θα είναι έτοιμο περίπου τρεις εβδομάδες αφότου μου στείλετε την επιλογή σας. Και κάτι ακόμα: το βίντεο θα καθυστερήσει μια εβδομάδα, γιατί ο συνεργάτης μου που το επεξεργάζεται είναι άρρωστος. Ζητώ συγγνώμη. Τα λέμε!", "The album will be ready about three weeks after you send me your selection. And one more thing: the video will be a week late, because my colleague who edits it is ill. I apologise. Speak soon!"),
 ],
 "questions": [
  Q("Για πόσο καιρό θα ισχύει ο σύνδεσμος;", ["Για μία εβδομάδα", "Για τρεις εβδομάδες", "Για τριάντα μέρες", "Για πάντα"], 2, "Ο σύνδεσμος θα ισχύει για τριάντα μέρες"),
  Q("Τι πρέπει να κάνει το ζευγάρι για το άλμπουμ;", ["Να διαλέξει εξήντα φωτογραφίες", "Να πληρώσει προκαταβολή", "Να πάει στο στούντιο", "Να στείλει δικές του φωτογραφίες"], 0, "χρειάζομαι να μου διαλέξετε εξήντα φωτογραφίες"),
  Q("Γιατί θα καθυστερήσει το βίντεο;", ["Γιατί χάλασε η κάμερα", "Γιατί ο συνεργάτης που το επεξεργάζεται είναι άρρωστος", "Γιατί ο φωτογράφος έχει πολλή δουλειά", "Γιατί χάθηκαν κάποια αρχεία"], 1, "γιατί ο συνεργάτης μου που το επεξεργάζεται είναι άρρωστος"),
 ],
 "gloss": {"σύνδεσμο": "σύνδεσμος — link", "κατεβάσετε": "κατεβάζω — to download", "υψηλή ανάλυση": "υψηλή ανάλυση — high resolution", "ισχύει": "ισχύω — to be valid", "άλμπουμ": "άλμπουμ — album", "εξώφυλλο": "εξώφυλλο — cover", "δερμάτινο": "δερμάτινος — leather", "αφότου": "αφότου — after, since", "επεξεργάζεται": "επεξεργάζομαι — to edit, process"},
})

ITEMS.append({
 "id": "l69-dia-adeies-avgoustou", "title": "Ποιος θα πάρει άδεια τον Αύγουστο;", "title_en": "Who gets leave in August?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο συνάδελφοι σε ένα μικρό γραφείο συζητούν πώς θα μοιράσουν τις καλοκαιρινές τους άδειες.",
 "script": [
  L("Νίκη", "f", "Η διευθύντρια θέλει να της δώσουμε τις ημερομηνίες για τις άδειες μέχρι την Παρασκευή. Και ξέρεις ότι ο ένας από τους δυο μας πρέπει να είναι πάντα στο γραφείο.", "The manager wants us to give her the dates for our leave by Friday. And you know one of the two of us always has to be in the office."),
  L("Ορέστης", "m", "Το ξέρω. Πέρσι πήρα εγώ το πρώτο δεκαπενθήμερο του Αυγούστου, οπότε φέτος είναι σωστό να το πάρεις εσύ. Μόνο που ο γάμος της αδερφής μου είναι στις δεκαπέντε Αυγούστου, στη Λέσβο.", "I know. Last year I took the first half of August, so this year it's fair that you take it. The only thing is that my sister's wedding is on the fifteenth of August, on Lesbos."),
  L("Νίκη", "f", "Τότε ας το κάνουμε αλλιώς. Εγώ φεύγω από την πρώτη μέχρι τις δώδεκα, κι εσύ από τις δεκατρείς μέχρι το τέλος του μήνα. Έτσι προλαβαίνεις τον γάμο.", "Then let's do it differently. I'll be away from the first to the twelfth, and you from the thirteenth to the end of the month. That way you make the wedding."),
  L("Ορέστης", "m", "Τέλεια, σ’ ευχαριστώ πολύ! Και για να σου το ξεπληρώσω, τα Χριστούγεννα μένω εγώ στο γραφείο.", "Perfect, thank you so much! And to make it up to you, I'll stay in the office at Christmas."),
 ],
 "questions": [
  Q("Τι ισχύει για τις άδειες στο γραφείο;", ["Πρέπει να τις πάρουν και οι δύο μαζί", "Ο ένας από τους δύο πρέπει να είναι πάντα στο γραφείο", "Απαγορεύονται τον Αύγουστο", "Τις αποφασίζει μόνη της η διευθύντρια"], 1, "ο ένας από τους δυο μας πρέπει να είναι πάντα στο γραφείο"),
  Q("Γιατί ο Ορέστης θέλει να είναι ελεύθερος στις δεκαπέντε Αυγούστου;", ["Για να πάει στον γάμο της αδερφής του", "Για να πάει στο πανηγύρι του χωριού", "Γιατί έχει γενέθλια", "Γιατί μετακομίζει"], 0, "ο γάμος της αδερφής μου είναι στις δεκαπέντε Αυγούστου"),
  Q("Τι θα κάνει ο Ορέστης, για να ευχαριστήσει τη Νίκη;", ["Θα την κεράσει φαγητό", "Θα μείνει στο γραφείο τα Χριστούγεννα", "Θα της φέρει δώρο από τη Λέσβο", "Θα πάρει λιγότερες μέρες άδεια"], 1, "τα Χριστούγεννα μένω εγώ στο γραφείο"),
 ],
 "gloss": {"άδειες": "άδεια — leave (from work)", "διευθύντρια": "διευθύντρια — manager (f.)", "δεκαπενθήμερο": "δεκαπενθήμερο — fortnight", "αλλιώς": "αλλιώς — differently", "προλαβαίνεις": "προλαβαίνω — to make it in time", "ξεπληρώσω": "ξεπληρώνω — to repay, make up for"},
})

ITEMS.append({
 "id": "l69-dia-psistaria-mpalkoni", "title": "Ψησταριά στο μπαλκόνι", "title_en": "A barbecue on the balcony", "type": "dialogue", "level": "B2",
 "context_el": "Η διαχειρίστρια μιας πολυκατοικίας χτυπά την πόρτα ενός ενοίκου.",
 "script": [
  L("Διαχειρίστρια", "f", "Καλησπέρα, κύριε Σταύρο. Συγγνώμη για την ενόχληση. Η κυρία από τον τρίτο παραπονέθηκε ότι κάθε Κυριακή γεμίζει το σπίτι της καπνό από την ψησταριά σας.", "Good evening, Mr Stavros. Sorry to bother you. The lady on the third floor complained that every Sunday her flat fills with smoke from your barbecue."),
  L("Σταύρος", "m", "Ειλικρινά δεν το είχα σκεφτεί. Ο καπνός ανεβαίνει, βέβαια... Αλλά απαγορεύεται; Δεν βλέπω κάτι σχετικό στον κανονισμό.", "Honestly, I hadn't thought of it. Smoke rises, of course... But is it forbidden? I don't see anything about it in the building rules."),
  L("Διαχειρίστρια", "f", "Ρητά δεν απαγορεύεται, αλλά ο κανονισμός λέει ότι δεν πρέπει να ενοχλούμε τους άλλους ενοίκους. Μήπως θα μπορούσατε να πάρετε μια ηλεκτρική ψησταριά; Βγάζει πολύ λιγότερο καπνό.", "It's not explicitly forbidden, but the rules say we mustn't disturb the other residents. Could you perhaps get an electric grill? It gives off much less smoke."),
  L("Σταύρος", "m", "Δεν είναι το ίδιο με τα κάρβουνα, αλλά εντάξει, έχετε δίκιο. Και την Κυριακή που έρχεται θα καλέσω και την κυρία από τον τρίτο για σουβλάκια, να τα βρούμε.", "It's not the same as charcoal, but all right, you're right. And this coming Sunday I'll invite the lady from the third floor for souvlaki, to make peace."),
 ],
 "questions": [
  Q("Γιατί παραπονέθηκε η κυρία από τον τρίτο;", ["Για τη φασαρία", "Για τον καπνό από την ψησταριά", "Για τη μυρωδιά από τα σκουπίδια", "Για τα νερά από το μπαλκόνι"], 1, "κάθε Κυριακή γεμίζει το σπίτι της καπνό από την ψησταριά σας"),
  Q("Τι λέει ο κανονισμός της πολυκατοικίας;", ["Ότι απαγορεύονται ρητά οι ψησταριές", "Ότι δεν πρέπει να ενοχλούμε τους άλλους ενοίκους", "Ότι επιτρέπονται μόνο ηλεκτρικές συσκευές", "Δεν λέει τίποτα"], 1, "ο κανονισμός λέει ότι δεν πρέπει να ενοχλούμε τους άλλους ενοίκους"),
  Q("Τι θα κάνει ο Σταύρος την επόμενη Κυριακή;", ["Θα πάει για φαγητό έξω", "Θα καλέσει την κυρία από τον τρίτο για σουβλάκια", "Θα μετακομίσει", "Θα ψήσει στην ταράτσα"], 1, "θα καλέσω και την κυρία από τον τρίτο για σουβλάκια"),
 ],
 "gloss": {"διαχειρίστρια": "διαχειρίστρια — building manager (f.)", "ενοίκου": "ένοικος — resident, tenant", "ψησταριά": "ψησταριά — barbecue, grill", "καπνό": "καπνός — smoke", "κανονισμό": "κανονισμός — rules, regulations", "Ρητά": "ρητά — explicitly", "κάρβουνα": "κάρβουνο — charcoal", "να τα βρούμε": "τα βρίσκω (με κάποιον) — to make peace, get on"},
})

ITEMS.append({
 "id": "l69-int-everest", "title": "Στην κορυφή του Έβερεστ", "title_en": "At the top of Everest", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια ορειβάτισσα που ανέβηκε στο Έβερεστ.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσο καιρό προετοιμαζόσασταν για την ανάβαση;", "How long did you prepare for the climb?"),
  L("Ορειβάτισσα", "f", "Σχεδόν τρία χρόνια. Γυμναζόμουν κάθε μέρα και ανέβηκα σε αρκετές ψηλές κορυφές στις Άλπεις και στα Ιμαλάια. Στο Νεπάλ μείναμε σχεδόν δύο μήνες, γιατί ο οργανισμός πρέπει να συνηθίσει σιγά σιγά το λίγο οξυγόνο. Αυτό λέγεται εγκλιματισμός, και αν τον παραλείψεις, μπορεί να πεθάνεις.", "Almost three years. I trained every day and climbed several high peaks in the Alps and the Himalayas. In Nepal we stayed almost two months, because the body has to get used to the low oxygen gradually. That's called acclimatisation, and if you skip it, you can die."),
  L("Δημοσιογράφος", "m", "Τι νιώσατε, όταν φτάσατε στην κορυφή;", "What did you feel when you reached the summit?"),
  L("Ορειβάτισσα", "f", "Λιγότερο ενθουσιασμό απ’ όσο φανταζόσασταν. Ήμουν τόσο κουρασμένη, που σκεφτόμουν μόνο την κατάβαση· τα περισσότερα ατυχήματα συμβαίνουν στο κατέβασμα. Μείναμε στην κορυφή μόνο δεκαπέντε λεπτά. Τη χαρά την ένιωσα πραγματικά δύο μέρες αργότερα, όταν έφτασα στην κατασκήνωση βάσης και μπόρεσα να πάρω τηλέφωνο τη μητέρα μου.", "Less excitement than you'd imagine. I was so tired that I was only thinking about the descent; most accidents happen on the way down. We stayed on the summit only fifteen minutes. I really felt the joy two days later, when I reached base camp and was able to phone my mother."),
 ],
 "questions": [
  Q("Γιατί έμειναν σχεδόν δύο μήνες στο Νεπάλ;", ["Για να περιμένουν καλό καιρό", "Για να συνηθίσει ο οργανισμός το λίγο οξυγόνο", "Για να βρουν χρήματα", "Γιατί αρρώστησε"], 1, "ο οργανισμός πρέπει να συνηθίσει σιγά σιγά το λίγο οξυγόνο"),
  Q("Τι σκεφτόταν στην κορυφή;", ["Μόνο την κατάβαση", "Τις φωτογραφίες", "Την επόμενη ανάβαση", "Τους χορηγούς της"], 0, "σκεφτόμουν μόνο την κατάβαση"),
  Q("Πότε ένιωσε πραγματικά χαρά;", ["Στην κορυφή", "Όταν γύρισε στην Ελλάδα", "Όταν έφτασε στην κατασκήνωση βάσης και πήρε τηλέφωνο τη μητέρα της", "Όταν βγήκε στην τηλεόραση"], 2, "όταν έφτασα στην κατασκήνωση βάσης και μπόρεσα να πάρω τηλέφωνο τη μητέρα μου"),
 ],
 "gloss": {"ορειβάτισσα": "ορειβάτισσα — mountaineer (f.)", "ανάβαση": "ανάβαση — ascent, climb", "κορυφές": "κορυφή — peak, summit", "οξυγόνο": "οξυγόνο — oxygen", "εγκλιματισμός": "εγκλιματισμός — acclimatisation", "παραλείψεις": "παραλείπω — to skip, omit", "κατάβαση": "κατάβαση — descent", "ατυχήματα": "ατύχημα — accident", "κατασκήνωση βάσης": "κατασκήνωση βάσης — base camp"},
})

ITEMS.append({
 "id": "l69-rep-delta-evrou", "title": "Το Δέλτα του Έβρου", "title_en": "The Evros Delta", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από έναν υγρότοπο στη Θράκη.",
 "script": [
  L("Ρεπόρτερ", "m", "Καλημέρα από το Δέλτα του Έβρου, εκεί όπου ο ποταμός συναντά το Αιγαίο, στα σύνορα της Ελλάδας με την Τουρκία. Ο υγρότοπος αυτός είναι από τους σημαντικότερους της Ευρώπης και προστατεύεται από διεθνή σύμβαση.", "Good morning from the Evros Delta, where the river meets the Aegean, on Greece's border with Turkey. This wetland is one of the most important in Europe and is protected by an international convention."),
  L("Ρεπόρτερ", "m", "Εδώ έχουν καταγραφεί περισσότερα από τριακόσια είδη πουλιών, πολλά από τα οποία σταματούν για να ξεκουραστούν στο μακρύ τους ταξίδι από την Αφρική προς τον Βορρά. Τον χειμώνα, χιλιάδες αγριόχηνες και φλαμίνγκο γεμίζουν τις λιμνοθάλασσες.", "More than three hundred species of birds have been recorded here, many of which stop to rest on their long journey from Africa to the north. In winter, thousands of wild geese and flamingos fill the lagoons."),
  L("Ρεπόρτερ", "m", "Επειδή η περιοχή βρίσκεται κοντά στα σύνορα, σε ορισμένα σημεία χρειάζεται ειδική άδεια για να μπει κανείς. Ο πιο εύκολος τρόπος να γνωρίσετε το Δέλτα είναι μια οργανωμένη ξενάγηση με βάρκα από το κέντρο επισκεπτών, όπου οι ξεναγοί σάς δίνουν και κιάλια.", "Because the area is near the border, in some places you need a special permit to enter. The easiest way to get to know the Delta is an organised boat tour from the visitor centre, where the guides also give you binoculars."),
 ],
 "questions": [
  Q("Πού βρίσκεται το Δέλτα του Έβρου;", ["Στην Κρήτη", "Στα σύνορα της Ελλάδας με την Τουρκία", "Στα σύνορα με τη Βουλγαρία", "Στο Ιόνιο"], 1, "στα σύνορα της Ελλάδας με την Τουρκία"),
  Q("Γιατί σταματούν πολλά πουλιά στο Δέλτα;", ["Για να φτιάξουν φωλιές", "Για να ξεκουραστούν στο μακρύ τους ταξίδι", "Γιατί εκεί περνούν όλο τον χρόνο", "Γιατί τα ταΐζουν οι κάτοικοι"], 1, "σταματούν για να ξεκουραστούν στο μακρύ τους ταξίδι"),
  Q("Ποιος είναι ο πιο εύκολος τρόπος να γνωρίσει κανείς το Δέλτα;", ["Με ποδήλατο", "Με αυτοκίνητο", "Με μια οργανωμένη ξενάγηση με βάρκα", "Με τα πόδια, χωρίς οδηγό"], 2, "μια οργανωμένη ξενάγηση με βάρκα"),
 ],
 "gloss": {"υγρότοπος": "υγρότοπος — wetland", "σύνορα": "σύνορα — border", "σύμβαση": "σύμβαση — convention, agreement", "καταγραφεί": "καταγράφομαι — to be recorded", "είδη": "είδος — species, kind", "αγριόχηνες": "αγριόχηνα — wild goose", "λιμνοθάλασσες": "λιμνοθάλασσα — lagoon", "ξενάγηση": "ξενάγηση — guided tour", "κιάλια": "κιάλια — binoculars"},
})

ITEMS.append({
 "id": "l69-mono-ravo-sta-peninta", "title": "Έμαθα να ράβω στα πενήντα", "title_en": "I learned to sew at fifty", "type": "monologue", "level": "B2",
 "context_el": "Ένας άντρας μιλά για το μάθημα ραπτικής που άρχισε σε μεγάλη ηλικία.",
 "script": [
  L("Γιώργος", "m", "Όλα ξεκίνησαν από ένα κουμπί. Είχε φύγει το κουμπί από το αγαπημένο μου σακάκι, και αντί να το ράψω, το άφησα δύο μήνες στην ντουλάπα. Η κόρη μου γέλασε και μου έκανε δώρο μια συνδρομή σε ένα εργαστήρι ραπτικής της γειτονιάς.", "It all started with a button. A button had come off my favourite jacket, and instead of sewing it on, I left it in the wardrobe for two months. My daughter laughed and gave me a subscription to a neighbourhood sewing workshop as a present."),
  L("Γιώργος", "m", "Στην αρχή ήμουν ο μόνος άντρας και ένιωθα λίγο άβολα. Τα δάχτυλά μου ήταν αδέξια και τρυπιόμουν συνέχεια με τη βελόνα. Η δασκάλα, όμως, είχε απίστευτη υπομονή. Μάθαμε πρώτα να κάνουμε στρίφωμα, μετά να βάζουμε φερμουάρ, και στο τέλος της χρονιάς έραψα το πρώτο μου πουκάμισο.", "At first I was the only man and felt a bit awkward. My fingers were clumsy and I kept pricking myself with the needle. But the teacher had incredible patience. We first learned to hem, then to put in zips, and at the end of the year I sewed my first shirt."),
  L("Γιώργος", "m", "Το φοράω με περηφάνια, παρόλο που το ένα μανίκι είναι λίγο πιο μακρύ από το άλλο. Και κάτι ακόμα: δεν πετάω πια ρούχα, επειδή έσκισαν λίγο. Τα επιδιορθώνω μόνος μου.", "I wear it with pride, even though one sleeve is a little longer than the other. And something else: I no longer throw clothes away because they're slightly torn. I mend them myself."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε ο Γιώργος το μάθημα ραπτικής;", ["Το διάβασε σε μια εφημερίδα", "Η κόρη του τού έκανε δώρο μια συνδρομή", "Του το πρότεινε ένας φίλος", "Το χρειαζόταν για τη δουλειά του"], 1, "Η κόρη μου γέλασε και μου έκανε δώρο μια συνδρομή"),
  Q("Πώς ένιωθε στην αρχή;", ["Λίγο άβολα, γιατί ήταν ο μόνος άντρας", "Πολύ σίγουρος για τον εαυτό του", "Βαριόταν", "Θύμωνε με τη δασκάλα"], 0, "ήμουν ο μόνος άντρας και ένιωθα λίγο άβολα"),
  Q("Τι ισχύει για το πρώτο του πουκάμισο;", ["Το χάρισε στην κόρη του", "Δεν το φοράει ποτέ", "Το ένα μανίκι είναι λίγο πιο μακρύ από το άλλο", "Το πούλησε"], 2, "το ένα μανίκι είναι λίγο πιο μακρύ από το άλλο"),
 ],
 "gloss": {"κουμπί": "κουμπί — button", "σακάκι": "σακάκι — jacket", "συνδρομή": "συνδρομή — subscription", "ραπτικής": "ραπτική — sewing, dressmaking", "άβολα": "άβολα — awkward(ly)", "αδέξια": "αδέξιος — clumsy", "βελόνα": "βελόνα — needle", "στρίφωμα": "στρίφωμα — hem", "φερμουάρ": "φερμουάρ — zip", "μανίκι": "μανίκι — sleeve", "επιδιορθώνω": "επιδιορθώνω — to mend, repair"},
})

ITEMS.append({
 "id": "l69-mono-diakopes-moni", "title": "Διακοπές μόνη μου", "title_en": "On holiday on my own", "type": "monologue", "level": "B2",
 "context_el": "Μια γυναίκα περιγράφει τις πρώτες της διακοπές χωρίς παρέα.",
 "script": [
  L("Ζωή", "f", "Πέρσι το καλοκαίρι οι φίλες μου δεν μπορούσαν να πάρουν άδεια την ίδια εποχή με μένα. Είχα δύο επιλογές: να μείνω στην Αθήνα ή να φύγω μόνη. Με πολύ άγχος, έκλεισα ένα δωμάτιο για μια εβδομάδα στη Φολέγανδρο.", "Last summer my friends couldn't take leave at the same time as me. I had two choices: stay in Athens or go away on my own. Very anxiously, I booked a room for a week on Folegandros."),
  L("Ζωή", "f", "Το πιο δύσκολο ήταν το πρώτο βράδυ, όταν κάθισα μόνη σε ένα τραπέζι στην πλατεία. Νόμιζα ότι όλοι με κοίταζαν. Στην πραγματικότητα, κανείς δεν έδινε σημασία. Από τη δεύτερη μέρα έπαιρνα μαζί ένα βιβλίο, και το τραπέζι για έναν μου φαινόταν πια φυσικό.", "The hardest part was the first evening, when I sat alone at a table in the square. I thought everyone was looking at me. In reality, nobody was paying attention. From the second day I took a book with me, and the table for one felt natural by then."),
  L("Ζωή", "f", "Το καλύτερο ήταν ότι έκανα ό,τι ήθελα: ξυπνούσα όποτε ήθελα, περπατούσα ώρες στα μονοπάτια, άλλαζα σχέδια την τελευταία στιγμή. Και, παραδόξως, γνώρισα περισσότερους ανθρώπους απ’ ό,τι όταν ταξιδεύω με παρέα. Φέτος θα ξαναπάω, και πάλι μόνη.", "The best thing was that I did whatever I wanted: I woke up whenever I wanted, walked for hours on the paths, changed plans at the last minute. And, paradoxically, I met more people than when I travel with friends. This year I'll go again, on my own again."),
 ],
 "questions": [
  Q("Γιατί η Ζωή πήγε διακοπές μόνη;", ["Γιατί ήθελε να γράψει ένα βιβλίο", "Γιατί οι φίλες της δεν μπορούσαν να πάρουν άδεια την ίδια εποχή", "Γιατί είχε τσακωθεί με τις φίλες της", "Γιατί κέρδισε ένα ταξίδι"], 1, "οι φίλες μου δεν μπορούσαν να πάρουν άδεια την ίδια εποχή με μένα"),
  Q("Τι ήταν το πιο δύσκολο;", ["Το ταξίδι με το πλοίο", "Να βρει δωμάτιο", "Το πρώτο βράδυ, όταν κάθισε μόνη σε ένα τραπέζι", "Τα μονοπάτια"], 2, "Το πιο δύσκολο ήταν το πρώτο βράδυ"),
  Q("Τι συνέβη, παραδόξως;", ["Βαρέθηκε γρήγορα", "Γνώρισε περισσότερους ανθρώπους απ’ ό,τι με παρέα", "Γύρισε νωρίτερα", "Έχασε το βιβλίο της"], 1, "γνώρισα περισσότερους ανθρώπους απ’ ό,τι όταν ταξιδεύω με παρέα"),
 ],
 "gloss": {"επιλογές": "επιλογή — choice, option", "άγχος": "άγχος — anxiety, stress", "έδινε σημασία": "δίνω σημασία — to pay attention", "φυσικό": "φυσικός — natural", "όποτε": "όποτε — whenever", "μονοπάτια": "μονοπάτι — path", "παραδόξως": "παραδόξως — paradoxically", "παρέα": "παρέα — company, group of friends"},
})

ITEMS.append({
 "id": "l69-c1-den-petame-tipota", "title": "Γιατί δεν πετάμε τίποτα;", "title_en": "Why do we never throw anything away?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια ψυχολόγο για τη σχέση μας με τα αντικείμενα που κρατάμε.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί άνθρωποι έχουν ντουλάπες γεμάτες πράγματα που δεν χρησιμοποιούν ποτέ. Γιατί μας είναι τόσο δύσκολο να τα αποχωριστούμε;", "Many people have wardrobes full of things they never use. Why is it so hard for us to part with them?"),
  L("Ψυχολόγος", "f", "Οι λόγοι είναι αρκετοί. Ο πρώτος είναι αυτό που οι ψυχολόγοι ονομάζουν «φαινόμενο της κατοχής»: απλώς και μόνο επειδή κάτι μας ανήκει, του αποδίδουμε μεγαλύτερη αξία απ’ ό,τι θα του αποδίδαμε, αν δεν ήταν δικό μας. Ο δεύτερος είναι ο φόβος της μελλοντικής ανάγκης: «κι αν το χρειαστώ κάποτε;». Και, βέβαια, πολλά αντικείμενα είναι φορείς αναμνήσεων· όταν πετάμε το φόρεμα που φορέσαμε σε έναν γάμο, νιώθουμε σαν να πετάμε ένα κομμάτι του εαυτού μας.", "There are several reasons. The first is what psychologists call the 'endowment effect': simply because something belongs to us, we attribute more value to it than we would if it weren't ours. The second is fear of future need: 'what if I need it some day?'. And, of course, many objects carry memories; when we throw away the dress we wore at a wedding, we feel as if we are throwing away a piece of ourselves."),
  L("Δημοσιογράφος", "m", "Πότε η συνήθεια αυτή γίνεται πρόβλημα;", "When does this habit become a problem?"),
  L("Ψυχολόγος", "f", "Όταν τα πράγματα αρχίζουν να καταλαμβάνουν τον χώρο της ζωής μας, κυριολεκτικά και μεταφορικά. Υπάρχει μια σοβαρή διαταραχή, η παθολογική συσσώρευση, όπου οι άνθρωποι δεν μπορούν να χρησιμοποιήσουν την κουζίνα ή το κρεβάτι τους. Για τους περισσότερους, όμως, αρκεί μια απλή ερώτηση: «Αν το έβλεπα σήμερα σε ένα κατάστημα, θα το αγόραζα;» Αν η απάντηση είναι όχι, ίσως ήρθε η ώρα να το χαρίσουμε σε κάποιον που θα το χρησιμοποιήσει.", "When things begin to take over the space of our lives, literally and figuratively. There is a serious disorder, compulsive hoarding, in which people cannot use their kitchen or their bed. For most people, though, a simple question is enough: 'If I saw it in a shop today, would I buy it?' If the answer is no, perhaps it's time to give it to someone who will use it."),
 ],
 "questions": [
  Q("Τι είναι το «φαινόμενο της κατοχής»;", ["Ο φόβος ότι θα χρειαστούμε κάτι στο μέλλον", "Ότι αποδίδουμε μεγαλύτερη αξία σε κάτι απλώς επειδή μας ανήκει", "Η ανάγκη να αγοράζουμε συνέχεια", "Η συνήθεια να δανειζόμαστε πράγματα"], 1, "απλώς και μόνο επειδή κάτι μας ανήκει, του αποδίδουμε μεγαλύτερη αξία"),
  Q("Γιατί είναι δύσκολο να πετάξουμε το φόρεμα ενός γάμου;", ["Γιατί ήταν ακριβό", "Γιατί είναι φορέας αναμνήσεων", "Γιατί μπορεί να το ξαναφορέσουμε", "Γιατί είναι δώρο"], 1, "πολλά αντικείμενα είναι φορείς αναμνήσεων"),
  Q("Τι συμβαίνει στην παθολογική συσσώρευση;", ["Οι άνθρωποι πετούν τα πάντα", "Οι άνθρωποι δεν μπορούν να χρησιμοποιήσουν την κουζίνα ή το κρεβάτι τους", "Οι άνθρωποι αγοράζουν μόνο καινούργια πράγματα", "Οι άνθρωποι μετακομίζουν συχνά"], 1, "οι άνθρωποι δεν μπορούν να χρησιμοποιήσουν την κουζίνα ή το κρεβάτι τους"),
  Q("Τι προτείνει η ψυχολόγος στους περισσότερους ανθρώπους;", ["Να πετάξουν τα μισά τους πράγματα", "Να ρωτήσουν τον εαυτό τους αν θα αγόραζαν σήμερα το αντικείμενο", "Να νοικιάσουν αποθήκη", "Να επισκεφθούν ψυχολόγο"], 1, "«Αν το έβλεπα σήμερα σε ένα κατάστημα, θα το αγόραζα;»"),
 ],
 "gloss": {"αποχωριστούμε": "αποχωρίζομαι — to part with", "φαινόμενο της κατοχής": "φαινόμενο της κατοχής — endowment effect", "αποδίδουμε": "αποδίδω — to attribute", "φορείς": "φορέας — carrier, bearer", "αναμνήσεων": "ανάμνηση — memory", "καταλαμβάνουν": "καταλαμβάνω — to occupy, take over", "κυριολεκτικά": "κυριολεκτικά — literally", "μεταφορικά": "μεταφορικά — figuratively", "διαταραχή": "διαταραχή — disorder", "παθολογική συσσώρευση": "παθολογική συσσώρευση — compulsive hoarding"},
})

ITEMS.append({
 "id": "l69-c1-naumachia-salaminas", "title": "Η ναυμαχία της Σαλαμίνας", "title_en": "The battle of Salamis", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από διάλεξη ιστορικού για μια από τις πιο γνωστές ναυμαχίες της αρχαιότητας.",
 "script": [
  L("Ιστορικός", "m", "Το 480 π.Χ. ο στρατός του Πέρση βασιλιά Ξέρξη είχε περάσει τις Θερμοπύλες και προχωρούσε προς την Αθήνα. Οι Αθηναίοι πήραν μια δραματική απόφαση: εγκατέλειψαν την πόλη τους και μετέφεραν τις οικογένειές τους στη Σαλαμίνα, στην Τροιζήνα και στην Αίγινα. Ο Θεμιστοκλής είχε ερμηνεύσει έναν χρησμό του μαντείου των Δελφών, που μιλούσε για «ξύλινα τείχη», ως προτροπή να εμπιστευτούν τη σωτηρία τους στα πλοία.", "In 480 BC the army of the Persian king Xerxes had passed Thermopylae and was advancing on Athens. The Athenians took a dramatic decision: they abandoned their city and moved their families to Salamis, Troezen and Aegina. Themistocles had interpreted an oracle from Delphi which spoke of 'wooden walls' as an exhortation to entrust their salvation to the ships."),
  L("Ιστορικός", "m", "Ο περσικός στόλος ήταν πολύ μεγαλύτερος. Ο Θεμιστοκλής, όμως, κατάλαβε ότι στο στενό πέρασμα ανάμεσα στη Σαλαμίνα και την Αττική ο αριθμός δεν θα μετρούσε τόσο. Σύμφωνα με τον Ηρόδοτο, έστειλε μάλιστα κρυφά έναν απεσταλμένο στον Ξέρξη, για να τον πείσει ότι οι Έλληνες ετοιμάζονταν να διαφύγουν. Ο Ξέρξης έστειλε τα πλοία του στα στενά, όπου αυτά στριμώχτηκαν και δεν μπορούσαν να κινηθούν, ενώ οι ελληνικές τριήρεις τα εμβόλιζαν το ένα μετά το άλλο.", "The Persian fleet was much larger. But Themistocles realised that in the narrow strait between Salamis and Attica numbers would not count so much. According to Herodotus, he even secretly sent an envoy to Xerxes to persuade him that the Greeks were preparing to escape. Xerxes sent his ships into the straits, where they were crammed together and could not manoeuvre, while the Greek triremes rammed them one after another."),
  L("Ιστορικός", "m", "Ο Ξέρξης, που παρακολουθούσε τη μάχη από τις πλαγιές του Αιγάλεω, είδε τον στόλο του να καταστρέφεται. Η νίκη έσωσε την Αθήνα και άνοιξε τον δρόμο για τον «χρυσό αιώνα» της. Ανάμεσα σε όσους πολέμησαν ήταν και ο Αισχύλος, ο οποίος, οκτώ χρόνια αργότερα, ανέβασε την τραγωδία «Πέρσες», το μόνο σωζόμενο αρχαίο δράμα με θέμα ένα σύγχρονο ιστορικό γεγονός.", "Xerxes, who was watching the battle from the slopes of Aigaleo, saw his fleet being destroyed. The victory saved Athens and opened the way to its 'golden age'. Among those who fought was Aeschylus, who eight years later staged the tragedy 'The Persians', the only surviving ancient drama on a contemporary historical event."),
 ],
 "questions": [
  Q("Πώς ερμήνευσε ο Θεμιστοκλής τα «ξύλινα τείχη» του χρησμού;", ["Ως τα τείχη της Ακρόπολης", "Ως προτροπή να εμπιστευτούν τη σωτηρία τους στα πλοία", "Ως εντολή να χτίσουν νέα τείχη", "Ως προειδοποίηση για φωτιά"], 1, "ως προτροπή να εμπιστευτούν τη σωτηρία τους στα πλοία"),
  Q("Γιατί το στενό πέρασμα βοήθησε τους Έλληνες;", ["Γιατί εκεί ο αριθμός των πλοίων δεν μετρούσε τόσο", "Γιατί είχε πολύ αέρα", "Γιατί οι Πέρσες δεν το γνώριζαν καθόλου", "Γιατί ήταν πιο ρηχό για τους Έλληνες"], 0, "ο αριθμός δεν θα μετρούσε τόσο"),
  Q("Τι έκανε κρυφά ο Θεμιστοκλής, σύμφωνα με τον Ηρόδοτο;", ["Ζήτησε βοήθεια από τη Σπάρτη", "Έστειλε απεσταλμένο στον Ξέρξη, για να τον πείσει ότι οι Έλληνες θα διέφευγαν", "Δωροδόκησε Πέρσες αξιωματικούς", "Έκαψε τα περσικά πλοία τη νύχτα"], 1, "έστειλε μάλιστα κρυφά έναν απεσταλμένο στον Ξέρξη"),
  Q("Τι ιδιαίτερο έχουν οι «Πέρσες» του Αισχύλου;", ["Είναι η πρώτη κωμωδία", "Είναι το μόνο σωζόμενο αρχαίο δράμα με θέμα ένα σύγχρονο ιστορικό γεγονός", "Γράφτηκαν από τον Θεμιστοκλή", "Παίχτηκαν στη Σαλαμίνα"], 1, "το μόνο σωζόμενο αρχαίο δράμα με θέμα ένα σύγχρονο ιστορικό γεγονός"),
 ],
 "gloss": {"ναυμαχίες": "ναυμαχία — naval battle", "εγκατέλειψαν": "εγκαταλείπω — to abandon", "ερμηνεύσει": "ερμηνεύω — to interpret", "χρησμό": "χρησμός — oracle (pronouncement)", "μαντείου": "μαντείο — oracle (sanctuary)", "προτροπή": "προτροπή — exhortation", "στόλος": "στόλος — fleet", "απεσταλμένο": "απεσταλμένος — envoy", "διαφύγουν": "διαφεύγω — to escape", "στριμώχτηκαν": "στριμώχνομαι — to be crammed", "τριήρεις": "τριήρης — trireme", "εμβόλιζαν": "εμβολίζω — to ram"},
})

rnd = random.Random(69)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-69.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
