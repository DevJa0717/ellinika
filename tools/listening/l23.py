# Source for library/listening/listening-23.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l23.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l23-ann-episkeptirio", "title": "Νέο ωράριο επισκεπτηρίου", "title_en": "New hospital visiting hours", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα ενός νοσοκομείου.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί επισκέπτες, σας ενημερώνουμε ότι από τη Δευτέρα αλλάζει το ωράριο επισκεπτηρίου στις κλινικές του νοσοκομείου. Οι επισκέψεις θα επιτρέπονται καθημερινά από τις έξι ως τις οχτώ το απόγευμα, ενώ τα Σαββατοκύριακα και από τις δώδεκα ως τη μία το μεσημέρι.", "Dear visitors, we inform you that from Monday the visiting hours in the hospital's wards are changing. Visits will be allowed daily from six to eight in the evening, and at weekends also from twelve to one at midday."),
  L("Εκφωνήτρια", "f", "Για την προστασία των ασθενών, κάθε ασθενής μπορεί να δέχεται έως δύο επισκέπτες ταυτόχρονα. Παιδιά κάτω των δώδεκα ετών δεν επιτρέπεται να εισέρχονται στις κλινικές. Παρακαλούμε επίσης να μη φέρνετε λουλούδια στη Μονάδα Εντατικής Θεραπείας.", "To protect patients, each patient may receive up to two visitors at a time. Children under twelve are not allowed to enter the wards. We also ask you not to bring flowers to the Intensive Care Unit."),
  L("Εκφωνήτρια", "f", "Οι συνοδοί ασθενών που χρειάζονται να μείνουν το βράδυ πρέπει να έχουν ειδική κάρτα, την οποία εκδίδει η προϊσταμένη της κλινικής. Ευχαριστούμε για την κατανόηση.", "Companions of patients who need to stay overnight must have a special card, which is issued by the ward's head nurse. Thank you for your understanding."),
 ],
 "questions": [
  Q("Πότε επιτρέπονται οι επισκέψεις τις καθημερινές;", ["Από τις δώδεκα ως τη μία", "Από τις έξι ως τις οχτώ το απόγευμα", "Όλη την ημέρα", "Μόνο το πρωί"], 1, "καθημερινά από τις έξι ως τις οχτώ το απόγευμα"),
  Q("Πόσοι επισκέπτες μπορούν να βρίσκονται ταυτόχρονα με έναν ασθενή;", ["Ένας", "Έως δύο", "Τρεις", "Όσοι θέλουν"], 1, "έως δύο επισκέπτες ταυτόχρονα"),
  Q("Ποιος εκδίδει την κάρτα για τους συνοδούς που μένουν το βράδυ;", ["Ο διευθυντής του νοσοκομείου", "Η προϊσταμένη της κλινικής", "Η γραμματεία", "Ο θεράποντας γιατρός"], 1, "την οποία εκδίδει η προϊσταμένη της κλινικής"),
 ],
 "gloss": {"μεγάφωνα": "μεγάφωνο — loudspeaker", "ωράριο επισκεπτηρίου": "ωράριο επισκεπτηρίου — visiting hours", "κλινικές": "κλινική — ward, clinic", "ασθενών": "ασθενής — patient", "ταυτόχρονα": "ταυτόχρονα — at the same time", "εισέρχονται": "εισέρχομαι — to enter", "Μονάδα Εντατικής Θεραπείας": "Μονάδα Εντατικής Θεραπείας (ΜΕΘ) — intensive care unit", "συνοδοί": "συνοδός — companion, escort", "εκδίδει": "εκδίδω — to issue", "προϊσταμένη": "προϊσταμένη — head nurse, supervisor", "κατανόηση": "κατανόηση — understanding"},
})

ITEMS.append({
 "id": "l23-vm-grammateia", "title": "Μήνυμα από τη γραμματεία", "title_en": "A message from the university office", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τη γραμματεία του τμήματός σας.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα, κύριε Σωτηρίου, από τη γραμματεία του Τμήματος Ιστορίας σάς καλώ. Ελέγξαμε τον φάκελό σας για την ορκωμοσία και διαπιστώσαμε ότι λείπει η βεβαίωση από τη βιβλιοθήκη ότι δεν χρωστάτε βιβλία.", "Good morning, Mr Sotiriou, I'm calling from the History Department office. We checked your file for the graduation ceremony and found that the certificate from the library confirming you don't owe any books is missing."),
  L("Υπάλληλος", "f", "Χωρίς αυτή τη βεβαίωση δεν μπορούμε να σας συμπεριλάβουμε στην ορκωμοσία του Ιουλίου. Η προθεσμία λήγει την Παρασκευή. Μπορείτε να ζητήσετε τη βεβαίωση ηλεκτρονικά από την ιστοσελίδα της βιβλιοθήκης και να μας τη στείλετε με email.", "Without this certificate we can't include you in the July graduation. The deadline is Friday. You can request the certificate online from the library website and send it to us by email."),
  L("Υπάλληλος", "f", "Αν έχετε ακόμη κάποιο βιβλίο, πρέπει πρώτα να το επιστρέψετε. Για οποιαδήποτε απορία, η γραμματεία δέχεται τηλεφωνήματα από τις δέκα ως τις δώδεκα.", "If you still have a book, you must return it first. For any questions, the office takes calls from ten to twelve."),
 ],
 "questions": [
  Q("Τι λείπει από τον φάκελο του φοιτητή;", ["Η αίτηση ορκωμοσίας", "Η βεβαίωση της βιβλιοθήκης ότι δεν χρωστάει βιβλία", "Η φωτογραφία του", "Η αναλυτική βαθμολογία"], 1, "λείπει η βεβαίωση από τη βιβλιοθήκη ότι δεν χρωστάτε βιβλία"),
  Q("Τι θα συμβεί αν δεν στείλει τη βεβαίωση ως την Παρασκευή;", ["Θα πληρώσει πρόστιμο", "Δεν θα συμπεριληφθεί στην ορκωμοσία του Ιουλίου", "Θα χάσει το πτυχίο του", "Θα πρέπει να ξαναδώσει εξετάσεις"], 1, "δεν μπορούμε να σας συμπεριλάβουμε στην ορκωμοσία του Ιουλίου"),
  Q("Πώς μπορεί να ζητήσει τη βεβαίωση;", ["Μόνο αυτοπροσώπως", "Ηλεκτρονικά από την ιστοσελίδα της βιβλιοθήκης", "Με συστημένη επιστολή", "Τηλεφωνικά από τη γραμματεία"], 1, "Μπορείτε να ζητήσετε τη βεβαίωση ηλεκτρονικά από την ιστοσελίδα της βιβλιοθήκης"),
 ],
 "gloss": {"γραμματεία": "γραμματεία — (university) office, secretariat", "τμήματός": "τμήμα — department", "φάκελό": "φάκελος — file", "ορκωμοσία": "ορκωμοσία — graduation ceremony (oath-taking)", "διαπιστώσαμε": "διαπιστώνω — to find, ascertain", "βεβαίωση": "βεβαίωση — certificate", "χρωστάτε": "χρωστάω — to owe", "να σας συμπεριλάβουμε": "συμπεριλαμβάνω — to include", "προθεσμία": "προθεσμία — deadline", "λήγει": "λήγω — to expire, end", "απορία": "απορία — question, query"},
})

ITEMS.append({
 "id": "l23-dia-plyntirio", "title": "Ένα καινούργιο πλυντήριο", "title_en": "A new washing machine", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα κατάστημα ηλεκτρικών συσκευών.",
 "script": [
  L("Πελάτισσα", "f", "Χάλασε το πλυντήριό μας μετά από δώδεκα χρόνια και ο τεχνικός είπε ότι δεν αξίζει να το επισκευάσουμε. Ψάχνω κάτι αξιόπιστο, χωρίς πολλά προγράμματα που δεν θα χρησιμοποιήσω ποτέ.", "Our washing machine broke after twelve years and the technician said it's not worth repairing. I'm looking for something reliable, without lots of programmes I'll never use."),
  L("Πωλητής", "m", "Σας καταλαβαίνω. Αυτό εδώ είναι οκτώ κιλών, ενεργειακής κλάσης Α, και είναι από τα πιο αθόρυβα που έχουμε. Κοστίζει λίγο περισσότερο από τα άλλα, αλλά θα το κερδίσετε πίσω στον λογαριασμό του ρεύματος μέσα σε λίγα χρόνια.", "I understand. This one here is eight kilos, energy class A, and it's one of the quietest we have. It costs a bit more than the others, but you'll earn it back on your electricity bill within a few years."),
  L("Πελάτισσα", "f", "Μένουμε σε μικρό διαμέρισμα και το πλυντήριο είναι στην κουζίνα, οπότε ο θόρυβος μετράει. Τι εγγύηση έχει; Και παίρνετε το παλιό;", "We live in a small flat and the washing machine is in the kitchen, so noise matters. What guarantee does it have? And do you take the old one?"),
  L("Πωλητής", "m", "Έχει δύο χρόνια εγγύηση από τον κατασκευαστή και πέντε χρόνια για το μοτέρ. Την παράδοση και την εγκατάσταση τις κάνουμε δωρεάν, και ναι, παίρνουμε το παλιό για ανακύκλωση χωρίς χρέωση. Μπορούμε να έρθουμε ακόμη και αύριο το απόγευμα.", "It has a two-year manufacturer's guarantee and five years on the motor. Delivery and installation are free, and yes, we take the old one for recycling at no charge. We can even come tomorrow afternoon."),
 ],
 "questions": [
  Q("Γιατί θέλει να αγοράσει καινούργιο πλυντήριο;", ["Γιατί μετακόμισε", "Γιατί το παλιό χάλασε και δεν αξίζει να επισκευαστεί", "Γιατί θέλει μεγαλύτερο", "Γιατί το παλιό καταναλώνει πολύ ρεύμα"], 1, "ο τεχνικός είπε ότι δεν αξίζει να το επισκευάσουμε"),
  Q("Γιατί τη νοιάζει ιδιαίτερα ο θόρυβος;", ["Γιατί έχει μωρό", "Γιατί το πλυντήριο είναι στην κουζίνα ενός μικρού διαμερίσματος", "Γιατί δουλεύει από το σπίτι", "Γιατί οι γείτονες παραπονιούνται"], 1, "Μένουμε σε μικρό διαμέρισμα και το πλυντήριο είναι στην κουζίνα"),
  Q("Τι ισχύει για το παλιό πλυντήριο;", ["Πρέπει να το πετάξει η ίδια", "Το κατάστημα το παίρνει για ανακύκλωση χωρίς χρέωση", "Το κατάστημα το αγοράζει", "Χρεώνεται η μεταφορά του"], 1, "παίρνουμε το παλιό για ανακύκλωση χωρίς χρέωση"),
 ],
 "gloss": {"πλυντήριο": "πλυντήριο — washing machine", "αξίζει": "αξίζει — it is worth", "να το επισκευάσουμε": "επισκευάζω — to repair", "αξιόπιστο": "αξιόπιστος — reliable", "ενεργειακής κλάσης": "ενεργειακή κλάση — energy class", "αθόρυβα": "αθόρυβος — quiet, noiseless", "μετράει": "μετράω — to matter, count", "εγγύηση": "εγγύηση — guarantee", "κατασκευαστή": "κατασκευαστής — manufacturer", "μοτέρ": "μοτέρ — motor", "εγκατάσταση": "εγκατάσταση — installation"},
})

ITEMS.append({
 "id": "l23-dia-astynomia", "title": "Δήλωση κλοπής", "title_en": "Reporting a theft", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα αστυνομικό τμήμα.",
 "script": [
  L("Αστυνομικός", "m", "Καλησπέρα. Πώς μπορώ να σας βοηθήσω;", "Good evening. How can I help you?"),
  L("Πολίτης", "f", "Θέλω να δηλώσω μια κλοπή. Μου έκλεψαν το ποδήλατο σήμερα το πρωί έξω από τον σταθμό του μετρό στο Μοναστηράκι. Το είχα δέσει με κλειδαριά σε μια κολόνα, αλλά όταν γύρισα το απόγευμα είχε μείνει μόνο η κλειδαριά, κομμένη.", "I want to report a theft. My bicycle was stolen this morning outside the metro station in Monastiraki. I had locked it to a post, but when I came back in the afternoon only the lock was left, cut."),
  L("Αστυνομικός", "m", "Λυπάμαι. Θα χρειαστώ μια περιγραφή: μάρκα, χρώμα, οποιοδήποτε ιδιαίτερο σημάδι. Έχετε τον αριθμό του σκελετού; Συνήθως είναι χαραγμένος κάτω από τα πετάλια.", "I'm sorry. I'll need a description: make, colour, any distinctive mark. Do you have the frame number? It's usually engraved under the pedals."),
  L("Πολίτης", "f", "Είναι ένα μπλε ποδήλατο πόλης με ένα καλάθι μπροστά. Τον αριθμό τον έχω φωτογραφίσει, ευτυχώς. Χρειάζομαι τη δήλωση και για την ασφαλιστική μου εταιρεία.", "It's a blue city bike with a basket on the front. I've photographed the number, luckily. I also need the report for my insurance company."),
  L("Αστυνομικός", "m", "Πολύ καλά κάνατε. Θα σας δώσω αντίγραφο της δήλωσης για την ασφαλιστική. Σας συμβουλεύω επίσης να ελέγχετε τις αγγελίες για μεταχειρισμένα ποδήλατα στο διαδίκτυο· αρκετά κλεμμένα ποδήλατα έχουν βρεθεί έτσι.", "You did very well. I'll give you a copy of the report for the insurer. I'd also advise you to check the online ads for second-hand bicycles; quite a few stolen bikes have been found that way."),
 ],
 "questions": [
  Q("Τι βρήκε η πολίτισσα όταν γύρισε το απόγευμα;", ["Το ποδήλατο με σκασμένο λάστιχο", "Μόνο την κλειδαριά, κομμένη", "Τίποτα, ούτε την κλειδαριά", "Το ποδήλατο σε άλλη κολόνα"], 1, "είχε μείνει μόνο η κλειδαριά, κομμένη"),
  Q("Γιατί χρειάζεται τη δήλωση;", ["Για την ασφαλιστική της εταιρεία", "Για τον εργοδότη της", "Για να αγοράσει καινούργιο ποδήλατο", "Για τον δήμο"], 0, "Χρειάζομαι τη δήλωση και για την ασφαλιστική μου εταιρεία"),
  Q("Τι της συμβουλεύει ο αστυνομικός;", ["Να μη χρησιμοποιεί πια ποδήλατο", "Να ελέγχει τις αγγελίες για μεταχειρισμένα ποδήλατα στο διαδίκτυο", "Να αγοράσει καλύτερη κλειδαριά", "Να ξαναπεράσει αύριο"], 1, "να ελέγχετε τις αγγελίες για μεταχειρισμένα ποδήλατα στο διαδίκτυο"),
 ],
 "gloss": {"αστυνομικό τμήμα": "αστυνομικό τμήμα — police station", "να δηλώσω": "δηλώνω — to report, declare", "κλοπή": "κλοπή — theft", "κλειδαριά": "κλειδαριά — lock", "κολόνα": "κολόνα — post, pole", "κομμένη": "κομμένος — cut", "περιγραφή": "περιγραφή — description", "μάρκα": "μάρκα — make, brand", "σκελετού": "σκελετός — frame", "χαραγμένος": "χαραγμένος — engraved", "πετάλια": "πετάλι — pedal", "ασφαλιστική": "ασφαλιστική (εταιρεία) — insurance company", "αγγελίες": "αγγελία — advertisement", "κλεμμένα": "κλεμμένος — stolen"},
})

ITEMS.append({
 "id": "l23-mon-diglossos", "title": "Μεγαλώνοντας με δύο γλώσσες", "title_en": "Growing up with two languages", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν νέο άντρα να μιλάει για το πώς μεγάλωσε με δύο γλώσσες.",
 "script": [
  L("Νέος", "m", "Γεννήθηκα στη Στουτγάρδη από Έλληνες γονείς. Στο σπίτι μιλούσαμε ελληνικά, στο σχολείο και με τους φίλους μου γερμανικά. Όταν ήμουν μικρός, ντρεπόμουν όταν η μητέρα μου μού μιλούσε ελληνικά μπροστά στους συμμαθητές μου, και της απαντούσα πάντα στα γερμανικά.", "I was born in Stuttgart to Greek parents. At home we spoke Greek, at school and with my friends German. When I was little I was embarrassed when my mother spoke Greek to me in front of my classmates, and I always answered her in German."),
  L("Νέος", "m", "Οι γονείς μου όμως επέμεναν να πηγαίνω κάθε Σάββατο σε ελληνικό σχολείο. Το μισούσα, γιατί οι φίλοι μου έπαιζαν ποδόσφαιρο κι εγώ έκανα ορθογραφία. Τα καλοκαίρια περνούσαμε δύο μήνες στο χωριό της γιαγιάς μου στην Αρκαδία, και εκεί τα ελληνικά μου ξυπνούσαν.", "But my parents insisted that I go to Greek school every Saturday. I hated it, because my friends played football and I was doing spelling. In the summers we spent two months in my grandmother's village in Arcadia, and there my Greek would wake up."),
  L("Νέος", "m", "Σήμερα δουλεύω ως μεταφραστής, και ό,τι μισούσα τότε είναι το επάγγελμά μου. Ακόμη, όμως, όταν θυμώνω, βρίζω στα ελληνικά, και όταν μετράω, μετράω στα γερμανικά. Νομίζω ότι δεν θα αποφασίσω ποτέ ποια είναι η μητρική μου γλώσσα, και δεν με πειράζει πια.", "Today I work as a translator, and what I hated then is my profession. But still, when I get angry I swear in Greek, and when I count I count in German. I think I'll never decide which is my mother tongue, and it doesn't bother me any more."),
 ],
 "questions": [
  Q("Πώς αντιδρούσε όταν ήταν μικρός και η μητέρα του μιλούσε ελληνικά μπροστά στους συμμαθητές του;", ["Της απαντούσε στα ελληνικά", "Ντρεπόταν και της απαντούσε στα γερμανικά", "Δεν της απαντούσε καθόλου", "Μετέφραζε για τους φίλους του"], 1, "ντρεπόμουν ... και της απαντούσα πάντα στα γερμανικά"),
  Q("Γιατί μισούσε το ελληνικό σχολείο του Σαββάτου;", ["Γιατί ο δάσκαλος ήταν αυστηρός", "Γιατί οι φίλοι του έπαιζαν ποδόσφαιρο εκείνη την ώρα", "Γιατί ήταν μακριά", "Γιατί τα μαθήματα ήταν βαρετά"], 1, "οι φίλοι μου έπαιζαν ποδόσφαιρο κι εγώ έκανα ορθογραφία"),
  Q("Ποια γλώσσα χρησιμοποιεί όταν μετράει;", ["Τα ελληνικά", "Τα γερμανικά", "Και τις δύο", "Τα αγγλικά"], 1, "όταν μετράω, μετράω στα γερμανικά"),
 ],
 "gloss": {"ντρεπόμουν": "ντρέπομαι — to be embarrassed, ashamed", "συμμαθητές": "συμμαθητής — classmate", "επέμεναν": "επιμένω — to insist", "μισούσα": "μισώ — to hate", "ορθογραφία": "ορθογραφία — spelling", "ξυπνούσαν": "ξυπνάω — to wake up", "μεταφραστής": "μεταφραστής — translator", "επάγγελμά": "επάγγελμα — profession", "θυμώνω": "θυμώνω — to get angry", "βρίζω": "βρίζω — to swear, curse", "μητρική μου γλώσσα": "μητρική γλώσσα — mother tongue", "με πειράζει": "με πειράζει — it bothers me"},
})

ITEMS.append({
 "id": "l23-rep-metsovo", "title": "Το Μέτσοβο", "title_en": "Metsovo", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ταξιδιωτικό ρεπορτάζ από το Μέτσοβο.",
 "script": [
  L("Ρεπόρτερ", "f", "Σε υψόμετρο πάνω από χίλια μέτρα, στις πλαγιές της Πίνδου, το Μέτσοβο είναι ένα από τα πιο ζωντανά ορεινά χωριά της Ηπείρου. Πολλοί κάτοικοι μιλούν ακόμη, εκτός από τα ελληνικά, τα βλάχικα, μια γλώσσα συγγενική με τα ρουμανικά.", "At an altitude of over a thousand metres, on the slopes of the Pindus, Metsovo is one of the liveliest mountain villages in Epirus. Many residents still speak, besides Greek, Vlach (Aromanian), a language related to Romanian."),
  L("Ρεπόρτερ", "f", "Το χωριό οφείλει πολλά στους ευεργέτες του, κυρίως στην οικογένεια Αβέρωφ. Χάρη σε αυτούς ιδρύθηκαν σχολεία, ένα τυροκομείο και μια σημαντική πινακοθήκη με έργα Ελλήνων ζωγράφων του δέκατου ένατου και του εικοστού αιώνα.", "The village owes a lot to its benefactors, mainly the Averoff family. Thanks to them, schools, a cheese dairy and an important art gallery with works by Greek painters of the nineteenth and twentieth centuries were founded."),
  L("Ρεπόρτερ", "f", "Ο επισκέπτης δεν πρέπει να φύγει χωρίς να δοκιμάσει το καπνιστό τυρί μετσοβόνε και τα τοπικά κρασιά. Τον χειμώνα το χωριό γεμίζει σκιέρ, ενώ το καλοκαίρι η δροσιά του προσελκύει όσους θέλουν να ξεφύγουν από τη ζέστη των πόλεων.", "Visitors shouldn't leave without tasting the smoked cheese metsovone and the local wines. In winter the village fills with skiers, while in summer its coolness attracts those who want to escape the heat of the cities."),
 ],
 "questions": [
  Q("Ποια γλώσσα μιλούν πολλοί κάτοικοι εκτός από τα ελληνικά;", ["Τα αλβανικά", "Τα βλάχικα", "Τα ιταλικά", "Τα τουρκικά"], 1, "μιλούν ακόμη, εκτός από τα ελληνικά, τα βλάχικα"),
  Q("Τι ίδρυσαν οι ευεργέτες του χωριού;", ["Ένα νοσοκομείο και ένα αεροδρόμιο", "Σχολεία, ένα τυροκομείο και μια πινακοθήκη", "Ένα χιονοδρομικό κέντρο", "Ένα πανεπιστήμιο"], 1, "ιδρύθηκαν σχολεία, ένα τυροκομείο και μια σημαντική πινακοθήκη"),
  Q("Τι προσελκύει τους επισκέπτες το καλοκαίρι;", ["Οι παραλίες", "Η δροσιά του χωριού", "Τα φεστιβάλ", "Το σκι"], 1, "το καλοκαίρι η δροσιά του προσελκύει όσους θέλουν να ξεφύγουν από τη ζέστη"),
 ],
 "gloss": {"υψόμετρο": "υψόμετρο — altitude", "πλαγιές": "πλαγιά — slope", "ορεινά": "ορεινός — mountain (adj.)", "βλάχικα": "βλάχικα — Vlach (Aromanian) language", "συγγενική": "συγγενικός — related", "οφείλει": "οφείλω — to owe", "ευεργέτες": "ευεργέτης — benefactor", "τυροκομείο": "τυροκομείο — cheese dairy", "πινακοθήκη": "πινακοθήκη — art gallery", "καπνιστό": "καπνιστός — smoked", "δροσιά": "δροσιά — coolness", "να ξεφύγουν": "ξεφεύγω — to escape"},
})

ITEMS.append({
 "id": "l23-rep-milos", "title": "Η Μήλος", "title_en": "Milos", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τη Μήλο σε μια ταξιδιωτική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "m", "Η Μήλος είναι ένα ηφαιστειογενές νησί των Κυκλάδων, και αυτό φαίνεται παντού: στους λευκούς βράχους του Σαρακήνικου, που θυμίζουν σεληνιακό τοπίο, στις πολύχρωμες ακτές και στις θερμές πηγές.", "Milos is a volcanic island in the Cyclades, and you can see it everywhere: in the white rocks of Sarakiniko, which recall a lunar landscape, in the multicoloured coasts and in the hot springs."),
  L("Ρεπόρτερ", "m", "Από την αρχαιότητα το νησί ζούσε από τον ορυκτό του πλούτο. Ο οψιανός της Μήλου, μια μαύρη ηφαιστειακή πέτρα, χρησιμοποιούνταν για εργαλεία ήδη από την προϊστορία. Ακόμη και σήμερα, τα ορυχεία του νησιού δίνουν δουλειά σε εκατοντάδες κατοίκους.", "Since antiquity the island has lived from its mineral wealth. The obsidian of Milos, a black volcanic stone, was used for tools as early as prehistory. Even today the island's mines give work to hundreds of residents."),
  L("Ρεπόρτερ", "m", "Το πιο διάσημο εύρημα του νησιού, όμως, δεν βρίσκεται εδώ. Το 1820 ένας αγρότης βρήκε στο χωράφι του το άγαλμα της Αφροδίτης, που σήμερα εκτίθεται στο Λούβρο ως Αφροδίτη της Μήλου. Στο σημείο της ανακάλυψης μια μικρή πινακίδα θυμίζει στους επισκέπτες τι χάθηκε.", "The island's most famous find, however, isn't here. In 1820 a farmer found in his field the statue of Aphrodite, which is now displayed in the Louvre as the Venus de Milo. At the spot of the discovery a small sign reminds visitors what was lost."),
 ],
 "questions": [
  Q("Με τι μοιάζει το τοπίο στο Σαρακήνικο;", ["Με έρημο", "Με σεληνιακό τοπίο", "Με τροπικό δάσος", "Με χιονισμένο βουνό"], 1, "θυμίζουν σεληνιακό τοπίο"),
  Q("Για τι χρησιμοποιούνταν ο οψιανός στην προϊστορία;", ["Για κοσμήματα", "Για εργαλεία", "Για χτίσιμο σπιτιών", "Για νομίσματα"], 1, "χρησιμοποιούνταν για εργαλεία ήδη από την προϊστορία"),
  Q("Πού βρίσκεται σήμερα η Αφροδίτη της Μήλου;", ["Στο μουσείο του νησιού", "Στην Αθήνα", "Στο Λούβρο", "Στο Βρετανικό Μουσείο"], 2, "σήμερα εκτίθεται στο Λούβρο"),
 ],
 "gloss": {"ηφαιστειογενές": "ηφαιστειογενής — volcanic (in origin)", "σεληνιακό": "σεληνιακός — lunar", "πολύχρωμες": "πολύχρωμος — multicoloured", "θερμές πηγές": "θερμή πηγή — hot spring", "ορυκτό": "ορυκτός — mineral", "πλούτο": "πλούτος — wealth", "οψιανός": "οψιανός — obsidian", "προϊστορία": "προϊστορία — prehistory", "ορυχεία": "ορυχείο — mine", "εύρημα": "εύρημα — find", "χωράφι": "χωράφι — field", "εκτίθεται": "εκτίθεμαι — to be exhibited", "πινακίδα": "πινακίδα — sign"},
})

ITEMS.append({
 "id": "l23-int-ktel", "title": "Οδηγός στο ΚΤΕΛ", "title_en": "A long-distance bus driver", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια οδηγό υπεραστικών λεωφορείων.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς αποφασίσατε να γίνετε οδηγός λεωφορείου;", "How did you decide to become a bus driver?"),
  L("Οδηγός", "f", "Ο πατέρας μου ήταν οδηγός στο ΚΤΕΛ Αρκαδίας και με έπαιρνε μαζί του τα καλοκαίρια. Καθόμουν στην πρώτη θέση και τον κοίταζα να παίρνει τις στροφές στα βουνά. Όταν τελείωσα το σχολείο, όλοι μου έλεγαν να γίνω κομμώτρια ή νηπιαγωγός. Εγώ έβγαλα δίπλωμα λεωφορείου στα είκοσι πέντε.", "My father was a driver with the Arcadia KTEL and took me with him in the summers. I sat in the front seat and watched him take the bends in the mountains. When I finished school, everyone told me to become a hairdresser or a nursery teacher. I got a bus licence at twenty-five."),
  L("Δημοσιογράφος", "m", "Πώς αντιδρούν οι επιβάτες όταν βλέπουν μια γυναίκα στο τιμόνι;", "How do passengers react when they see a woman at the wheel?"),
  L("Οδηγός", "f", "Οι περισσότεροι δεν το σχολιάζουν πια. Κάποιοι ηλικιωμένοι στα χωριά με ρωτούσαν στην αρχή αν είμαι σίγουρη ότι θα τα καταφέρω στον χιονισμένο δρόμο. Μετά από δέκα χρόνια, τώρα μου φέρνουν αυγά και κουλουράκια. Το πιο δύσκολο δεν είναι οι στροφές· είναι το ωράριο. Ξεκινάω στις πέντε το πρωί, και τα Χριστούγεννα σπάνια τα περνάω στο σπίτι.", "Most don't comment on it any more. Some elderly people in the villages asked me at first whether I was sure I'd manage on the snowy road. After ten years, now they bring me eggs and biscuits. The hardest thing isn't the bends; it's the hours. I start at five in the morning, and I rarely spend Christmas at home."),
 ],
 "questions": [
  Q("Πώς γνώρισε τη δουλειά του οδηγού;", ["Από ένα σεμινάριο", "Ταξιδεύοντας με τον πατέρα της, που ήταν οδηγός", "Από μια φίλη της", "Από μια αγγελία"], 1, "Ο πατέρας μου ήταν οδηγός στο ΚΤΕΛ Αρκαδίας και με έπαιρνε μαζί του"),
  Q("Πώς φέρονται σήμερα οι ηλικιωμένοι των χωριών;", ["Αρνούνται να ταξιδέψουν μαζί της", "Της φέρνουν αυγά και κουλουράκια", "Της κάνουν παράπονα", "Δεν της μιλούν"], 1, "τώρα μου φέρνουν αυγά και κουλουράκια"),
  Q("Τι θεωρεί το πιο δύσκολο στη δουλειά της;", ["Τις στροφές", "Τους επιβάτες", "Το ωράριο", "Τον χιονισμένο δρόμο"], 2, "Το πιο δύσκολο δεν είναι οι στροφές· είναι το ωράριο"),
 ],
 "gloss": {"υπεραστικών": "υπεραστικός — intercity, long-distance", "στροφές": "στροφή — bend, turn", "κομμώτρια": "κομμώτρια — hairdresser", "νηπιαγωγός": "νηπιαγωγός — nursery-school teacher", "δίπλωμα": "δίπλωμα — licence", "στο τιμόνι": "τιμόνι — steering wheel", "σχολιάζουν": "σχολιάζω — to comment on", "χιονισμένο": "χιονισμένος — snowy", "κουλουράκια": "κουλουράκι — biscuit (butter cookie)", "ωράριο": "ωράριο — working hours"},
})

ITEMS.append({
 "id": "l23-mon-machi-kritis", "title": "Η Μάχη της Κρήτης", "title_en": "The Battle of Crete", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη για τη Μάχη της Κρήτης το 1941.",
 "script": [
  L("Ιστορικός", "m", "Το πρωί της 20ής Μαΐου 1941, ο ουρανός πάνω από τα Χανιά, το Ρέθυμνο και το Ηράκλειο γέμισε αλεξίπτωτα. Ήταν η πρώτη φορά στην ιστορία που ένα νησί δεχόταν εισβολή κυρίως από τον αέρα. Οι Γερμανοί υπολόγιζαν ότι θα καταλάμβαναν την Κρήτη μέσα σε λίγες μέρες, χωρίς σοβαρή αντίσταση.", "On the morning of 20 May 1941, the sky over Chania, Rethymno and Heraklion filled with parachutes. It was the first time in history that an island was invaded mainly from the air. The Germans reckoned they would take Crete within a few days, without serious resistance."),
  L("Ιστορικός", "m", "Αυτό που δεν είχαν προβλέψει ήταν η αντίδραση του πληθυσμού. Εκτός από τις ελληνικές και τις βρετανικές δυνάμεις, μαζί με τους Αυστραλούς και τους Νεοζηλανδούς, πολέμησαν και άμαχοι, ηλικιωμένοι, γυναίκες, ακόμη και ιερείς, συχνά με κυνηγετικά όπλα ή με ό,τι βρήκαν μπροστά τους. Οι απώλειες των αλεξιπτωτιστών ήταν τόσο βαριές, ώστε ο Χίτλερ δεν ενέκρινε ποτέ ξανά μια τόσο μεγάλη αεροπορική επιχείρηση.", "What they had not foreseen was the reaction of the population. Besides the Greek and British forces, together with the Australians and New Zealanders, civilians fought too, elderly people, women, even priests, often with hunting rifles or whatever they found to hand. The paratroopers' losses were so heavy that Hitler never again approved such a large airborne operation."),
  L("Ιστορικός", "m", "Η μάχη κράτησε περίπου δώδεκα μέρες. Μετά την πτώση του αεροδρομίου του Μάλεμε, οι συμμαχικές δυνάμεις υποχώρησαν προς τα Σφακιά, από όπου χιλιάδες στρατιώτες απομακρύνθηκαν με πλοία προς την Αίγυπτο. Πολλοί όμως έμειναν πίσω, και οι Κρητικοί τούς έκρυβαν για μήνες στα βουνά, με κίνδυνο της ζωής τους.", "The battle lasted about twelve days. After the fall of Maleme airfield, the Allied forces retreated towards Sfakia, from where thousands of soldiers were evacuated by ship to Egypt. But many stayed behind, and the Cretans hid them for months in the mountains, at the risk of their lives."),
  L("Ιστορικός", "m", "Το τίμημα ήταν φοβερό: η κατοχή που ακολούθησε συνοδεύτηκε από αντίποινα, εκτελέσεις και καταστροφές χωριών. Γι' αυτό, κάθε Μάιο, στις τελετές μνήμης στην Κρήτη, συναντά κανείς ακόμη βετεράνους ή απογόνους τους από την Αυστραλία και τη Νέα Ζηλανδία, που έρχονται να τιμήσουν μια σχέση σφυρηλατημένη στη φωτιά.", "The price was terrible: the occupation that followed was accompanied by reprisals, executions and the destruction of villages. That is why, every May, at the memorial ceremonies in Crete, one still meets veterans or their descendants from Australia and New Zealand, who come to honour a bond forged in fire."),
 ],
 "questions": [
  Q("Τι ήταν πρωτοφανές στην εισβολή της 20ής Μαΐου 1941;", ["Ότι έγινε τη νύχτα", "Ότι ένα νησί δεχόταν εισβολή κυρίως από τον αέρα", "Ότι συμμετείχαν πλοία", "Ότι δεν υπήρξε αντίσταση"], 1, "Ήταν η πρώτη φορά στην ιστορία που ένα νησί δεχόταν εισβολή κυρίως από τον αέρα"),
  Q("Ποια ήταν η συνέπεια των βαριών απωλειών των αλεξιπτωτιστών;", ["Οι Γερμανοί αποχώρησαν από την Κρήτη", "Ο Χίτλερ δεν ενέκρινε ποτέ ξανά τόσο μεγάλη αεροπορική επιχείρηση", "Η μάχη κράτησε μήνες", "Οι Σύμμαχοι επιτέθηκαν στην Αίγυπτο"], 1, "ο Χίτλερ δεν ενέκρινε ποτέ ξανά μια τόσο μεγάλη αεροπορική επιχείρηση"),
  Q("Τι έκαναν οι Κρητικοί με τους στρατιώτες που έμειναν πίσω;", ["Τους παρέδωσαν στους Γερμανούς", "Τους έκρυβαν στα βουνά με κίνδυνο της ζωής τους", "Τους μετέφεραν στην Αίγυπτο με βάρκες", "Τους έστειλαν στα Χανιά"], 1, "οι Κρητικοί τούς έκρυβαν για μήνες στα βουνά, με κίνδυνο της ζωής τους"),
  Q("Γιατί έρχονται κάθε Μάιο επισκέπτες από την Αυστραλία και τη Νέα Ζηλανδία;", ["Για διακοπές", "Για να τιμήσουν μια σχέση σφυρηλατημένη στον πόλεμο", "Για επαγγελματικούς λόγους", "Για να μελετήσουν αρχαιολογία"], 1, "έρχονται να τιμήσουν μια σχέση σφυρηλατημένη στη φωτιά"),
 ],
 "gloss": {"αλεξίπτωτα": "αλεξίπτωτο — parachute", "εισβολή": "εισβολή — invasion", "θα καταλάμβαναν": "καταλαμβάνω — to capture, seize", "αντίσταση": "αντίσταση — resistance", "είχαν προβλέψει": "προβλέπω — to foresee", "άμαχοι": "άμαχος — civilian, non-combatant", "κυνηγετικά όπλα": "κυνηγετικό όπλο — hunting rifle", "απώλειες": "απώλεια — loss, casualty", "αλεξιπτωτιστών": "αλεξιπτωτιστής — paratrooper", "ενέκρινε": "εγκρίνω — to approve", "υποχώρησαν": "υποχωρώ — to retreat", "απομακρύνθηκαν": "απομακρύνομαι — to be evacuated, removed", "τίμημα": "τίμημα — price, cost", "αντίποινα": "αντίποινα — reprisals", "εκτελέσεις": "εκτέλεση — execution", "απογόνους": "απόγονος — descendant", "σφυρηλατημένη": "σφυρηλατημένος — forged"},
})

ITEMS.append({
 "id": "l23-int-epistimi-politon", "title": "Η επιστήμη των πολιτών", "title_en": "Citizen science", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια θαλάσσια βιολόγο για την «επιστήμη των πολιτών».",
 "script": [
  L("Δημοσιογράφος", "m", "Τι εννοούμε όταν λέμε «επιστήμη των πολιτών»;", "What do we mean when we say 'citizen science'?"),
  L("Βιολόγος", "f", "Εννοούμε ερευνητικά προγράμματα στα οποία συμμετέχουν απλοί πολίτες, χωρίς επιστημονική κατάρτιση, συλλέγοντας δεδομένα. Στη δική μας περίπτωση, ζητάμε από λουόμενους, ψαράδες και δύτες να φωτογραφίζουν μέδουσες ή ξενικά ψάρια που βλέπουν και να ανεβάζουν τις φωτογραφίες σε μια εφαρμογή, μαζί με την τοποθεσία και την ημερομηνία.", "We mean research programmes in which ordinary citizens without scientific training take part by collecting data. In our case, we ask swimmers, fishermen and divers to photograph jellyfish or non-native fish they see and upload the photos to an app, together with the location and date."),
  L("Δημοσιογράφος", "m", "Δεν φοβάστε ότι τα δεδομένα αυτά δεν είναι αξιόπιστα;", "Aren't you afraid that this data isn't reliable?"),
  L("Βιολόγος", "f", "Είναι εύλογη ανησυχία. Γι' αυτό κάθε φωτογραφία ελέγχεται από ειδικούς πριν μπει στη βάση δεδομένων. Τα λάθη υπάρχουν, αλλά το πλεονέκτημα είναι τεράστιο: καμία ερευνητική ομάδα δεν θα μπορούσε ποτέ να παρακολουθεί ταυτόχρονα χιλιάδες χιλιόμετρα ακτών. Χάρη στους πολίτες, εντοπίσαμε την εξάπλωση του λαγοκέφαλου, ενός τοξικού ψαριού που ήρθε από την Ερυθρά Θάλασσα, πολύ νωρίτερα απ' ό,τι θα το είχαμε κάνει μόνοι μας.", "It's a reasonable concern. That's why every photo is checked by experts before it goes into the database. Mistakes exist, but the advantage is huge: no research team could ever monitor thousands of kilometres of coastline at the same time. Thanks to citizens, we detected the spread of the silver-cheeked toadfish, a toxic fish that came from the Red Sea, much earlier than we would have done on our own."),
  L("Βιολόγος", "f", "Υπάρχει και ένα όφελος που δεν μετριέται σε δεδομένα. Όποιος έχει φωτογραφίσει μια μέδουσα για να βοηθήσει μια έρευνα, κοιτάζει τη θάλασσα διαφορετικά. Γίνεται, κατά κάποιον τρόπο, συνυπεύθυνος για αυτήν.", "There's also a benefit that can't be measured in data. Anyone who has photographed a jellyfish to help a study looks at the sea differently. They become, in a way, jointly responsible for it."),
 ],
 "questions": [
  Q("Τι ζητούν οι ερευνητές από τους πολίτες;", ["Να καθαρίζουν τις παραλίες", "Να φωτογραφίζουν μέδουσες ή ξενικά ψάρια και να ανεβάζουν τις φωτογραφίες σε μια εφαρμογή", "Να μην ψαρεύουν", "Να κάνουν δωρεές"], 1, "να φωτογραφίζουν μέδουσες ή ξενικά ψάρια ... και να ανεβάζουν τις φωτογραφίες σε μια εφαρμογή"),
  Q("Πώς αντιμετωπίζεται το ζήτημα της αξιοπιστίας των δεδομένων;", ["Δεν αντιμετωπίζεται", "Κάθε φωτογραφία ελέγχεται από ειδικούς", "Δεκτές γίνονται μόνο φωτογραφίες από δύτες", "Οι πολίτες περνούν εξετάσεις"], 1, "κάθε φωτογραφία ελέγχεται από ειδικούς πριν μπει στη βάση δεδομένων"),
  Q("Ποιο παράδειγμα δίνει για τη χρησιμότητα του προγράμματος;", ["Τη μείωση της ρύπανσης", "Τον έγκαιρο εντοπισμό της εξάπλωσης του λαγοκέφαλου", "Την ανακάλυψη ενός νέου είδους φώκιας", "Την προστασία των θαλάσσιων χελωνών"], 1, "εντοπίσαμε την εξάπλωση του λαγοκέφαλου ... πολύ νωρίτερα"),
  Q("Ποιο είναι το όφελος «που δεν μετριέται σε δεδομένα»;", ["Η οικονομική ενίσχυση της έρευνας", "Ότι οι πολίτες νιώθουν συνυπεύθυνοι για τη θάλασσα", "Η διαφήμιση του πανεπιστημίου", "Η τουριστική ανάπτυξη"], 1, "Γίνεται, κατά κάποιον τρόπο, συνυπεύθυνος για αυτήν"),
 ],
 "gloss": {"θαλάσσια βιολόγο": "θαλάσσιος βιολόγος — marine biologist", "κατάρτιση": "κατάρτιση — training", "συλλέγοντας": "συλλέγω — to collect", "δεδομένα": "δεδομένα — data", "λουόμενους": "λουόμενος — swimmer, bather", "δύτες": "δύτης — diver", "μέδουσες": "μέδουσα — jellyfish", "ξενικά": "ξενικός — non-native, alien (species)", "εφαρμογή": "εφαρμογή — app", "εύλογη": "εύλογος — reasonable", "βάση δεδομένων": "βάση δεδομένων — database", "εντοπίσαμε": "εντοπίζω — to detect, locate", "εξάπλωση": "εξάπλωση — spread", "λαγοκέφαλου": "λαγοκέφαλος — silver-cheeked toadfish (pufferfish)", "τοξικού": "τοξικός — toxic", "όφελος": "όφελος — benefit", "συνυπεύθυνος": "συνυπεύθυνος — jointly responsible"},
})
rnd = random.Random(23)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-23.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
