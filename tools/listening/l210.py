# Source for library/listening/listening-210.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l210.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l210-news-ees-synora", "title": "Τέλος οι σφραγίδες στα διαβατήρια", "title_en": "No more passport stamps: the EU's new border system", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα δελτίο ειδήσεων στο ραδιόφωνο σχετικά με ένα νέο σύστημα ελέγχου στα σύνορα της Ευρωπαϊκής Ένωσης.",
 "script": [
  L("Εκφωνήτρια", "f", "Σταδιακά καταργούνται οι σφραγίδες στα διαβατήρια των ταξιδιωτών από χώρες εκτός Ευρωπαϊκής Ένωσης. Στη θέση τους λειτουργεί ένα νέο ψηφιακό σύστημα εισόδου και εξόδου, που καταγράφει πότε μπαίνει και πότε βγαίνει κάθε επισκέπτης από τον χώρο Σένγκεν.", "Passport stamps for travellers from countries outside the European Union are gradually being abolished. In their place a new digital entry and exit system is operating, which records when each visitor enters and leaves the Schengen area."),
  L("Εκφωνήτρια", "f", "Την πρώτη φορά που θα περάσουν τα σύνορα, οι ταξιδιώτες θα δίνουν τα δακτυλικά τους αποτυπώματα και θα φωτογραφίζονται. Τα στοιχεία αυτά θα αποθηκεύονται, ώστε στα επόμενα ταξίδια ο έλεγχος να γίνεται γρηγορότερα. Οι Ευρωπαίοι πολίτες δεν επηρεάζονται.", "The first time they cross the border, travellers will give their fingerprints and be photographed. This data will be stored so that on subsequent trips the check is quicker. European citizens are not affected."),
  L("Εκφωνήτρια", "f", "Στα αεροδρόμια και στα λιμάνια, πάντως, οι πρώτες εβδομάδες έφεραν μεγαλύτερες ουρές, κυρίως σε ώρες αιχμής. Οι αρχές συνιστούν στους ταξιδιώτες από τρίτες χώρες να φτάνουν νωρίτερα, ενώ οργανώσεις για τα προσωπικά δεδομένα ζητούν περισσότερη διαφάνεια για το πόσο καιρό θα κρατούνται οι φωτογραφίες.", "At airports and ports, however, the first weeks brought longer queues, mainly at peak times. The authorities advise travellers from third countries to arrive earlier, while personal-data organisations are asking for more transparency about how long the photographs will be kept."),
 ],
 "questions": [
  Q("Τι αντικαθιστά το νέο σύστημα;", ["Τις βίζες", "Τις σφραγίδες στα διαβατήρια", "Τα εισιτήρια", "Τις ταυτότητες των Ευρωπαίων"], 1, "Σταδιακά καταργούνται οι σφραγίδες στα διαβατήρια"),
  Q("Τι θα κάνουν οι ταξιδιώτες την πρώτη φορά που θα περάσουν τα σύνορα;", ["Θα πληρώνουν ένα τέλος", "Θα δίνουν δακτυλικά αποτυπώματα και θα φωτογραφίζονται", "Θα συμπληρώνουν ένα έντυπο στο αεροπλάνο", "Θα περνούν ιατρικό έλεγχο"], 1, "θα δίνουν τα δακτυλικά τους αποτυπώματα και θα φωτογραφίζονται"),
  Q("Ποιους αφορά το σύστημα;", ["Όλους τους ταξιδιώτες", "Μόνο τους Ευρωπαίους πολίτες", "Ταξιδιώτες από χώρες εκτός Ευρωπαϊκής Ένωσης", "Μόνο τους οδηγούς φορτηγών"], 2, "ταξιδιωτών από χώρες εκτός Ευρωπαϊκής Ένωσης ... Οι Ευρωπαίοι πολίτες δεν επηρεάζονται"),
  Q("Τι ζητούν οι οργανώσεις για τα προσωπικά δεδομένα;", ["Να καταργηθεί το σύστημα", "Περισσότερη διαφάνεια για το πόσο καιρό θα κρατούνται οι φωτογραφίες", "Να μπαίνουν σφραγίδες ξανά", "Να γίνεται ο έλεγχος μόνο στα λιμάνια"], 1, "ζητούν περισσότερη διαφάνεια για το πόσο καιρό θα κρατούνται οι φωτογραφίες"),
 ],
 "gloss": {"σφραγίδες": "σφραγίδα — stamp", "καταργούνται": "καταργούμαι — to be abolished", "αποτυπώματα": "αποτύπωμα — print; δακτυλικό αποτύπωμα = fingerprint", "αποθηκεύονται": "αποθηκεύομαι — to be stored", "αιχμής": "ώρα αιχμής — peak time", "δεδομένα": "δεδομένα — data", "διαφάνεια": "διαφάνεια — transparency"},
})
ITEMS.append({
 "id": "l210-dia-ergasia-logoklopi", "title": "Μια εργασία που έγραψε... το κινητό", "title_en": "An essay written by... the phone", "type": "dialogue", "level": "B2",
 "context_el": "Δύο φοιτητές συζητούν στην καφετέρια της σχολής για μια εργασία που πρέπει να παραδώσουν.",
 "script": [
  L("Πάνος", "m", "Τελείωσες την εργασία για τη Δευτέρα; Εγώ τη γράφω σε δέκα λεπτά. Βάζω το θέμα σε μια εφαρμογή τεχνητής νοημοσύνης και μου βγάζει τρεις σελίδες έτοιμες.", "Have you finished the essay for Monday? I'll write mine in ten minutes. I put the topic into an AI app and it gives me three pages ready-made."),
  L("Λήδα", "f", "Πάνο, πρόσεξε. Ο καθηγητής είπε στο μάθημα ότι όποιος παραδώσει κείμενο που δεν έγραψε ο ίδιος θα το θεωρήσει λογοκλοπή. Και ελέγχει τις εργασίες με ειδικό πρόγραμμα.", "Panos, be careful. The professor said in class that anyone who hands in a text they didn't write themselves will be treated as plagiarising. And he checks the essays with a special program."),
  L("Πάνος", "m", "Αυτά τα προγράμματα κάνουν λάθη. Και τι διαφορά έχει από το να ψάξω στο ίντερνετ;", "Those programs make mistakes. And how is it different from searching on the internet?"),
  L("Λήδα", "f", "Όταν ψάχνεις, διαβάζεις, συγκρίνεις και μετά γράφεις με δικά σου λόγια, αναφέροντας τις πηγές. Εδώ δεν μαθαίνεις τίποτα. Και θυμήσου ότι στην εξεταστική θα πρέπει να γράψεις μόνος σου, χωρίς κινητό.", "When you search, you read, compare and then write in your own words, citing the sources. Here you learn nothing. And remember that in the exams you'll have to write on your own, without a phone."),
  L("Πάνος", "m", "Εντάξει, έχεις ένα δίκιο. Τι λες, μπορώ να τη χρησιμοποιήσω τουλάχιστον για να μου εξηγήσει ό,τι δεν κατάλαβα και να διορθώσει τα ορθογραφικά μου;", "OK, you've got a point. What do you think, can I at least use it to explain whatever I didn't understand and correct my spelling?"),
  L("Λήδα", "f", "Αυτό ρώτα τον καθηγητή. Μου φαίνεται λογικό, αρκεί να το γράψεις στην εργασία. Έλα, πάμε στη βιβλιοθήκη να ξεκινήσουμε μαζί.", "Ask the professor that. It seems reasonable to me, as long as you mention it in the essay. Come on, let's go to the library and start together."),
 ],
 "questions": [
  Q("Πώς σκοπεύει ο Πάνος να γράψει την εργασία του;", ["Με τη βοήθεια ενός φίλου", "Με μια εφαρμογή τεχνητής νοημοσύνης", "Αντιγράφοντας από ένα βιβλίο", "Δεν σκοπεύει να τη γράψει"], 1, "Βάζω το θέμα σε μια εφαρμογή τεχνητής νοημοσύνης"),
  Q("Τι είχε πει ο καθηγητής;", ["Ότι επιτρέπεται κάθε βοήθεια", "Ότι κείμενο που δεν έγραψε ο φοιτητής θα θεωρείται λογοκλοπή", "Ότι η εργασία δεν μετράει", "Ότι η προθεσμία παρατείνεται"], 1, "όποιος παραδώσει κείμενο που δεν έγραψε ο ίδιος θα το θεωρήσει λογοκλοπή"),
  Q("Ποια διαφορά βλέπει η Λήδα από την αναζήτηση στο ίντερνετ;", ["Ότι το ίντερνετ είναι πιο αργό", "Ότι όταν ψάχνεις διαβάζεις, συγκρίνεις και γράφεις με δικά σου λόγια", "Ότι στο ίντερνετ όλα είναι λάθος", "Δεν βλέπει καμία διαφορά"], 1, "διαβάζεις, συγκρίνεις και μετά γράφεις με δικά σου λόγια"),
  Q("Τι προτείνει τελικά η Λήδα;", ["Να παραδώσει ό,τι έγραψε η εφαρμογή", "Να μην παραδώσει εργασία", "Να ρωτήσει τον καθηγητή και να πάνε μαζί στη βιβλιοθήκη", "Να αλλάξει μάθημα"], 2, "Αυτό ρώτα τον καθηγητή ... πάμε στη βιβλιοθήκη να ξεκινήσουμε μαζί"),
 ],
 "gloss": {"τεχνητής νοημοσύνης": "τεχνητή νοημοσύνη — artificial intelligence", "λογοκλοπή": "λογοκλοπή — plagiarism", "πηγές": "πηγή — source", "εξεταστική": "εξεταστική (περίοδος) — exam period", "ορθογραφικά": "ορθογραφικά (λάθη) — spelling mistakes", "αναφέροντας": "αναφέρω — to cite, mention"},
})
ITEMS.append({
 "id": "l210-c1-mono-qwerty", "title": "Γιατί τα γράμματα στο πληκτρολόγιο δεν είναι με αλφαβητική σειρά", "title_en": "Why keyboard letters aren't in alphabetical order", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν ιστορικό της τεχνολογίας σε μια ραδιοφωνική εκπομπή για την καθημερινότητα.",
 "script": [
  L("Ιστορικός", "m", "Κοιτάξτε την πάνω σειρά γραμμάτων στο πληκτρολόγιό σας: Q, W, E, R, T, Y. Η διάταξη αυτή δεν σχεδιάστηκε για υπολογιστές· είναι κληρονομιά από τις γραφομηχανές του 19ου αιώνα, και συγκεκριμένα από μια μηχανή που ανέπτυξε στη δεκαετία του 1870 ο Αμερικανός Κρίστοφερ Σολς.", "Look at the top row of letters on your keyboard: Q, W, E, R, T, Y. This layout was not designed for computers; it is an inheritance from 19th-century typewriters, specifically from a machine developed in the 1870s by the American Christopher Sholes."),
  L("Ιστορικός", "m", "Η πιο διαδεδομένη εξήγηση είναι ότι τα γράμματα που χρησιμοποιούνται συχνά μαζί τοποθετήθηκαν σε απόσταση το ένα από το άλλο, για να μην μπλέκονται οι μεταλλικοί βραχίονες της μηχανής όταν κάποιος έγραφε γρήγορα. Οι ιστορικοί, πάντως, διαφωνούν για το πόσο καθοριστικός ήταν αυτός ο λόγος· ρόλο φαίνεται ότι έπαιξαν και οι ανάγκες των τηλεγραφητών, που ήταν από τους πρώτους πελάτες.", "The most widespread explanation is that letters often used together were placed apart from one another, so that the machine's metal arms wouldn't tangle when someone typed fast. Historians, however, disagree about how decisive that reason was; the needs of telegraph operators, who were among the first customers, also seem to have played a part."),
  L("Ιστορικός", "m", "Αργότερα προτάθηκαν διατάξεις που υπόσχονταν γρηγορότερη πληκτρολόγηση, με πιο γνωστή εκείνη του Ντβόρακ τη δεκαετία του 1930. Καμία δεν κατάφερε να εκτοπίσει την παλιά. Όταν εκατομμύρια άνθρωποι έχουν μάθει να γράφουν με έναν τρόπο, το κόστος της αλλαγής φαίνεται μεγαλύτερο από το όφελος, ακόμη κι αν η καινούργια λύση είναι καλύτερη.", "Later, layouts were proposed that promised faster typing, the best known being Dvorak's in the 1930s. None managed to displace the old one. When millions of people have learned to type one way, the cost of change seems greater than the benefit, even if the new solution is better."),
  L("Ιστορικός", "m", "Οι οικονομολόγοι το ονομάζουν «εξάρτηση από την πορεία»: μια επιλογή του παρελθόντος, που ίσως έγινε για λόγους που δεν ισχύουν πια, συνεχίζει να καθορίζει το παρόν. Ακόμη και το ελληνικό πληκτρολόγιο, άλλωστε, ακολουθεί σε μεγάλο βαθμό την ίδια διάταξη: Ε, Ρ, Τ, Υ.", "Economists call it 'path dependence': a choice from the past, perhaps made for reasons that no longer apply, continues to shape the present. Even the Greek keyboard, after all, largely follows the same layout: E, R, T, Y."),
 ],
 "questions": [
  Q("Από πού προέρχεται η διάταξη QWERTY;", ["Από τους πρώτους υπολογιστές", "Από τις γραφομηχανές του 19ου αιώνα", "Από τα κινητά τηλέφωνα", "Από τις στοιχειοθετικές μηχανές των εφημερίδων"], 1, "είναι κληρονομιά από τις γραφομηχανές του 19ου αιώνα"),
  Q("Ποια είναι η πιο διαδεδομένη εξήγηση για τη διάταξη;", ["Να είναι εύκολη για τα παιδιά", "Να μην μπλέκονται οι μεταλλικοί βραχίονες όταν κάποιος έγραφε γρήγορα", "Να χωράνε περισσότερα πλήκτρα", "Να μοιάζει με το αλφάβητο"], 1, "για να μην μπλέκονται οι μεταλλικοί βραχίονες της μηχανής"),
  Q("Πώς παρουσιάζει ο ομιλητής αυτή την εξήγηση;", ["Ως απόλυτα αποδεδειγμένη", "Ως μύθο χωρίς βάση", "Ως πιθανή, αλλά οι ιστορικοί διαφωνούν για το πόσο καθοριστική ήταν", "Ως εξήγηση που δόθηκε μόλις πρόσφατα"], 2, "Οι ιστορικοί, πάντως, διαφωνούν για το πόσο καθοριστικός ήταν αυτός ο λόγος"),
  Q("Τι σημαίνει «εξάρτηση από την πορεία», σύμφωνα με τον ομιλητή;", ["Ότι η τεχνολογία προχωρά πάντα προς το καλύτερο", "Ότι μια παλιά επιλογή συνεχίζει να καθορίζει το παρόν, ακόμη κι αν οι λόγοι της δεν ισχύουν πια", "Ότι οι καταναλωτές προτιμούν πάντα το φθηνότερο", "Ότι οι νέες διατάξεις είναι πάντα χειρότερες"], 1, "μια επιλογή του παρελθόντος ... συνεχίζει να καθορίζει το παρόν"),
 ],
 "gloss": {"πληκτρολόγιο": "πληκτρολόγιο — keyboard", "διάταξη": "διάταξη — layout, arrangement", "γραφομηχανές": "γραφομηχανή — typewriter", "βραχίονες": "βραχίονας — arm, lever", "καθοριστικός": "καθοριστικός — decisive", "τηλεγραφητών": "τηλεγραφητής — telegraph operator", "εκτοπίσει": "εκτοπίζω — to displace", "όφελος": "όφελος — benefit"},
})
ITEMS.append({
 "id": "l210-c1-int-athlitiki-psychologia", "title": "Όταν τα πόδια «κόβονται» στο πέναλτι", "title_en": "Choking under pressure: a sports psychologist", "type": "interview", "level": "C1",
 "context_el": "Ένας δημοσιογράφος συζητά με μια αθλητική ψυχολόγο σε μια αθλητική εκπομπή.",
 "script": [
  L("Δημοσιογράφος", "m", "Βλέπουμε συχνά επαγγελματίες αθλητές, που έχουν εκτελέσει χιλιάδες πέναλτι στην προπόνηση, να αποτυγχάνουν στο πιο κρίσιμο λεπτό. Τι συμβαίνει εκείνη τη στιγμή;", "We often see professional athletes, who have taken thousands of penalties in training, fail at the most critical moment. What happens at that moment?"),
  L("Ψυχολόγος", "f", "Αυτό που στη βιβλιογραφία λέγεται «κατάρρευση υπό πίεση». Μια κίνηση που έχει γίνει αυτόματη εκτελείται καλύτερα όταν δεν τη σκεφτόμαστε. Υπό πίεση, όμως, ο αθλητής αρχίζει να ελέγχει συνειδητά κάθε λεπτομέρεια: πού θα πατήσει, πώς θα κρατήσει το σώμα του. Είναι σαν να προσπαθείς να κατεβείς μια σκάλα σκεπτόμενος κάθε σκαλί· σκοντάφτεις.", "What the literature calls 'choking under pressure'. A movement that has become automatic is performed better when we don't think about it. Under pressure, though, the athlete starts consciously controlling every detail: where to step, how to hold the body. It's like trying to go down a staircase thinking about every step; you trip."),
  L("Δημοσιογράφος", "m", "Και πώς προετοιμάζετε έναν αθλητή γι' αυτό;", "And how do you prepare an athlete for that?"),
  L("Ψυχολόγος", "f", "Ένα βασικό εργαλείο είναι η ρουτίνα πριν από την κίνηση: ίδιες ανάσες, ίδιο βλέμμα, ίδιος αριθμός βημάτων, κάθε φορά. Η ρουτίνα απασχολεί το μυαλό με κάτι γνώριμο και αφήνει το σώμα να κάνει αυτό που ξέρει. Δουλεύουμε επίσης με τη νοερή εξάσκηση: ο αθλητής φαντάζεται με κάθε λεπτομέρεια το γήπεδο, τον θόρυβο, το βάρος της στιγμής, ώστε όταν έρθει η πραγματική να του φανεί λιγότερο ξένη.", "A basic tool is the routine before the movement: the same breaths, the same gaze, the same number of steps, every time. The routine occupies the mind with something familiar and lets the body do what it knows. We also work with mental rehearsal: the athlete imagines in every detail the stadium, the noise, the weight of the moment, so that when the real one comes it seems less unfamiliar."),
  L("Δημοσιογράφος", "m", "Υπάρχει κάτι που δεν πρέπει να λέει ένας προπονητής εκείνη την ώρα;", "Is there something a coach shouldn't say at that moment?"),
  L("Ψυχολόγος", "f", "Το «μην αστοχήσεις». Οι αρνητικές οδηγίες στρέφουν την προσοχή ακριβώς σε αυτό που θέλουμε να αποφύγουμε. Πολύ πιο χρήσιμο είναι να δώσει μια απλή, θετική εικόνα, π.χ. «χαμηλά, στη δεξιά γωνία», και, κυρίως, να έχει δημιουργήσει από πριν ένα κλίμα όπου η αποτυχία δεν είναι το τέλος του κόσμου.", "'Don't miss.' Negative instructions direct attention precisely to what we want to avoid. Much more useful is to give a simple, positive image, e.g. 'low, in the right corner', and, above all, to have created beforehand a climate in which failure is not the end of the world."),
 ],
 "questions": [
  Q("Τι συμβαίνει, κατά την ψυχολόγο, όταν ένας αθλητής «καταρρέει υπό πίεση»;", ["Κουράζεται σωματικά", "Αρχίζει να ελέγχει συνειδητά μια κίνηση που είχε γίνει αυτόματη", "Ξεχνάει τους κανόνες", "Χάνει την ακοή του από τον θόρυβο"], 1, "ο αθλητής αρχίζει να ελέγχει συνειδητά κάθε λεπτομέρεια"),
  Q("Με τι συγκρίνει αυτό το φαινόμενο;", ["Με την οδήγηση στη βροχή", "Με το να κατεβαίνεις μια σκάλα σκεπτόμενος κάθε σκαλί", "Με το να μαθαίνεις μια ξένη γλώσσα", "Με το κολύμπι σε κρύο νερό"], 1, "σαν να προσπαθείς να κατεβείς μια σκάλα σκεπτόμενος κάθε σκαλί"),
  Q("Πώς βοηθά η ρουτίνα πριν από την κίνηση;", ["Κάνει τον αντίπαλο να αγχωθεί", "Απασχολεί το μυαλό με κάτι γνώριμο και αφήνει το σώμα να κάνει αυτό που ξέρει", "Χαλαρώνει τους μυς", "Δίνει χρόνο στον προπονητή να σκεφτεί"], 1, "Η ρουτίνα απασχολεί το μυαλό με κάτι γνώριμο"),
  Q("Γιατί δεν πρέπει να πει ο προπονητής «μην αστοχήσεις»;", ["Γιατί είναι αγενές", "Γιατί οι αρνητικές οδηγίες στρέφουν την προσοχή σε αυτό που θέλουμε να αποφύγουμε", "Γιατί ο αθλητής δεν τον ακούει", "Γιατί απαγορεύεται από τους κανονισμούς"], 1, "Οι αρνητικές οδηγίες στρέφουν την προσοχή ακριβώς σε αυτό που θέλουμε να αποφύγουμε"),
 ],
 "gloss": {"εκτελέσει": "εκτελώ — to take (a penalty), carry out", "κρίσιμο": "κρίσιμος — critical", "κατάρρευση": "κατάρρευση — collapse", "συνειδητά": "συνειδητά — consciously", "σκοντάφτεις": "σκοντάφτω — to trip, stumble", "νοερή": "νοερός — mental", "αστοχήσεις": "αστοχώ — to miss (a target)", "κλίμα": "κλίμα — (here) atmosphere, climate"},
})
rnd = random.Random(210)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-210.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
