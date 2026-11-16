# Source for library/listening/listening-50.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l50.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l50-ann-allagi-limaniou", "title": "Αλλαγή λιμανιού αναχώρησης", "title_en": "A change of departure port", "type": "announcement", "level": "B2",
 "context_el": "Περιμένετε στο λιμάνι του Πειραιά να πάρετε το πλοίο για τη Νάξο. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Ανακοίνωση", "m", "Προσοχή, παρακαλώ. Ενημερώνουμε τους επιβάτες του πλοίου «Αιγαίον» με προορισμό Πάρο και Νάξο ότι, λόγω βλάβης στον καταπέλτη του πλοίου, η σημερινή αναχώρηση δεν θα γίνει από τον Πειραιά αλλά από το λιμάνι της Ραφήνας. Η ώρα αναχώρησης μεταφέρεται από τις επτά και μισή στις δέκα το πρωί.", "Attention, please. Passengers on the ship Aegaeon bound for Paros and Naxos are informed that, due to a fault in the ship's loading ramp, today's departure will not be from Piraeus but from the port of Rafina. The departure time is moved from half past seven to ten in the morning."),
  L("Ανακοίνωση", "m", "Για τη μεταφορά των επιβατών, η εταιρεία έχει διαθέσει δωρεάν λεωφορεία, που θα αναχωρούν από την πύλη Ε7 κάθε μισή ώρα, από τις επτά μέχρι τις οχτώ και μισή. Η διαδρομή διαρκεί περίπου μία ώρα. Οι επιβάτες με αυτοκίνητο παρακαλούνται να κατευθυνθούν οι ίδιοι στη Ραφήνα.", "To transport passengers, the company has laid on free buses, which will leave from gate E7 every half hour, from seven until half past eight. The journey takes about an hour. Passengers with cars are asked to make their own way to Rafina."),
  L("Ανακοίνωση", "m", "Τα εισιτήρια ισχύουν κανονικά και δεν χρειάζεται να αλλαχτούν. Όσοι επιβάτες δεν επιθυμούν να ταξιδέψουν μπορούν να ζητήσουν πλήρη επιστροφή του ποσού από τα εκδοτήρια της εταιρείας. Ζητούμε συγγνώμη για την ταλαιπωρία.", "Tickets remain valid and do not need to be changed. Passengers who do not wish to travel can ask for a full refund at the company's ticket offices. We apologise for the inconvenience."),
 ],
 "questions": [
  Q("Γιατί αλλάζει το λιμάνι αναχώρησης;", ["Λόγω απεργίας", "Λόγω βλάβης στον καταπέλτη του πλοίου", "Λόγω ισχυρών ανέμων", "Λόγω έργων στο λιμάνι"], 1, "λόγω βλάβης στον καταπέλτη του πλοίου"),
  Q("Πώς θα πάνε στη Ραφήνα οι επιβάτες χωρίς αυτοκίνητο;", ["Με ταξί που θα πληρώσει η εταιρεία", "Με δωρεάν λεωφορεία από την πύλη Ε7", "Με το μετρό", "Με άλλο πλοίο"], 1, "η εταιρεία έχει διαθέσει δωρεάν λεωφορεία, που θα αναχωρούν από την πύλη Ε7"),
  Q("Τι πρέπει να κάνουν όσοι δεν θέλουν πια να ταξιδέψουν;", ["Να αλλάξουν το εισιτήριό τους για αύριο", "Να ζητήσουν επιστροφή χρημάτων από τα εκδοτήρια", "Να τηλεφωνήσουν στην εταιρεία", "Να περιμένουν το επόμενο πλοίο"], 1, "μπορούν να ζητήσουν πλήρη επιστροφή του ποσού από τα εκδοτήρια"),
 ],
 "gloss": {"μεγάφωνα": "μεγάφωνο — loudspeaker", "προορισμό": "προορισμός — destination", "βλάβης": "βλάβη — fault, breakdown", "καταπέλτη": "καταπέλτης — loading ramp (of a ferry)", "μεταφέρεται": "μεταφέρομαι — to be moved, transferred", "έχει διαθέσει": "διαθέτω — to make available", "να κατευθυνθούν": "κατευθύνομαι — to head for", "να αλλαχτούν": "αλλάζομαι — to be changed", "επιθυμούν": "επιθυμώ — to wish", "εκδοτήρια": "εκδοτήριο — ticket office", "ταλαιπωρία": "ταλαιπωρία — inconvenience"},
})

ITEMS.append({
 "id": "l50-vm-kteo", "title": "Ραντεβού στο ΚΤΕΟ", "title_en": "An appointment for the vehicle inspection", "type": "voicemail", "level": "B2",
 "context_el": "Είχατε κλείσει ραντεβού για τον τεχνικό έλεγχο του αυτοκινήτου σας. Θα ακούσετε ένα μήνυμα από το ΚΤΕΟ στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, από το ιδιωτικό ΚΤΕΟ «Ασφάλεια» σας τηλεφωνούμε, για τον κύριο Σπύρο Αναστασίου. Είχατε ραντεβού για τον τεχνικό έλεγχο του αυτοκινήτου σας την Πέμπτη στις έντεκα. Δυστυχώς, εκείνη τη μέρα θα γίνει συντήρηση στα μηχανήματά μας και το κέντρο θα μείνει κλειστό.", "Good morning, we're calling from the Asfaleia private vehicle inspection centre, for Mr Spyros Anastasiou. You had an appointment for your car's roadworthiness test on Thursday at eleven. Unfortunately, on that day our machines will be serviced and the centre will be closed."),
  L("Υπάλληλος", "f", "Μπορούμε να σας εξυπηρετήσουμε την Παρασκευή στις εννιά ή τη Δευτέρα στις δώδεκα. Επειδή το πιστοποιητικό σας λήγει στο τέλος του μήνα, σας συνιστούμε να μην αφήσετε τον έλεγχο για αργότερα, γιατί αν κυκλοφορείτε με ληγμένο πιστοποιητικό, κινδυνεύετε με πρόστιμο.", "We can see you on Friday at nine or on Monday at twelve. Because your certificate expires at the end of the month, we advise you not to put the test off, because if you drive with an expired certificate you risk a fine."),
  L("Υπάλληλος", "f", "Μην ξεχάσετε να φέρετε την άδεια κυκλοφορίας και την απόδειξη πληρωμής των τελών κυκλοφορίας. Και, αν μπορείτε, ελέγξτε πριν τα φώτα και τα λάστιχα, γιατί είναι οι πιο συχνές αιτίες αποτυχίας. Παρακαλούμε επιβεβαιώστε το νέο ραντεβού στο ίδιο τηλέφωνο. Ευχαριστούμε.", "Don't forget to bring the vehicle registration document and the receipt for the road tax. And, if you can, check the lights and the tyres beforehand, because they are the most common reasons for failing. Please confirm the new appointment on the same number. Thank you."),
 ],
 "questions": [
  Q("Γιατί ακυρώνεται το ραντεβού της Πέμπτης;", ["Επειδή απεργούν οι υπάλληλοι", "Επειδή θα γίνει συντήρηση στα μηχανήματα", "Επειδή είναι αργία", "Επειδή ο κύριος Αναστασίου άργησε"], 1, "εκείνη τη μέρα θα γίνει συντήρηση στα μηχανήματά μας"),
  Q("Γιατί δεν πρέπει να καθυστερήσει τον έλεγχο;", ["Επειδή θα ακριβύνει", "Επειδή το πιστοποιητικό του λήγει στο τέλος του μήνα", "Επειδή φεύγει ταξίδι", "Επειδή το ΚΤΕΟ κλείνει για καλοκαίρι"], 1, "Επειδή το πιστοποιητικό σας λήγει στο τέλος του μήνα"),
  Q("Ποιες είναι οι πιο συχνές αιτίες αποτυχίας στον έλεγχο;", ["Τα φρένα και η μηχανή", "Τα φώτα και τα λάστιχα", "Τα καθίσματα και οι ζώνες", "Η εξάτμιση και η μπαταρία"], 1, "ελέγξτε πριν τα φώτα και τα λάστιχα, γιατί είναι οι πιο συχνές αιτίες αποτυχίας"),
 ],
 "gloss": {"ΚΤΕΟ": "ΚΤΕΟ — vehicle inspection centre (roadworthiness test)", "τεχνικό έλεγχο": "τεχνικός έλεγχος — roadworthiness test", "συντήρηση": "συντήρηση — maintenance, servicing", "μηχανήματά": "μηχάνημα — machine", "να σας εξυπηρετήσουμε": "εξυπηρετώ — to serve, attend to", "πιστοποιητικό": "πιστοποιητικό — certificate", "λήγει": "λήγω — to expire", "ληγμένο": "ληγμένος — expired", "πρόστιμο": "πρόστιμο — fine", "άδεια κυκλοφορίας": "άδεια κυκλοφορίας — vehicle registration document", "τελών κυκλοφορίας": "τέλη κυκλοφορίας — road tax", "αποτυχίας": "αποτυχία — failure", "επιβεβαιώστε": "επιβεβαιώνω — to confirm"},
})

ITEMS.append({
 "id": "l50-dia-onoma-moro", "title": "Ένα όνομα για το μωρό", "title_en": "A name for the baby", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε ένα ζευγάρι που περιμένει το πρώτο του παιδί να συζητάει για το όνομα του μωρού.",
 "script": [
  L("Ειρήνη", "f", "Γιάννη, πρέπει να αποφασίσουμε για το όνομα. Η μητέρα σου με ρώτησε πάλι σήμερα αν θα τη βγάλουμε Ευανθία, σαν τη γιαγιά σου. Της είπα ότι το σκεφτόμαστε ακόμα.", "Giannis, we have to decide about the name. Your mother asked me again today whether we'll call her Evanthia, like your grandmother. I told her we're still thinking about it."),
  L("Γιάννης", "m", "Ξέρω ότι το περιμένει, είναι η παράδοση στην οικογένειά μας. Το πρώτο παιδί παίρνει το όνομα της γιαγιάς από τη μεριά του πατέρα. Αλλά δεν θέλω να το κάνουμε μόνο από υποχρέωση. Εσύ τι λες;", "I know she expects it; it's the tradition in our family. The first child takes the name of the grandmother on the father's side. But I don't want us to do it just out of obligation. What do you think?"),
  L("Ειρήνη", "f", "Το όνομα μου αρέσει, είναι παλιό αλλά όμορφο. Το πρόβλημα είναι ότι η δική μου μητέρα θα στενοχωρηθεί, γιατί το όνομά της δεν θα το πάρει κανένα εγγόνι για χρόνια. Μήπως να της δώσουμε δύο ονόματα, Ευανθία-Μαρία;", "I like the name; it's old but beautiful. The problem is that my mother will be upset, because none of her grandchildren will get her name for years. What if we give her two names, Evanthia-Maria?"),
  L("Γιάννης", "m", "Δύο ονόματα είναι λίγο βαριά για ένα μωρό. Ας την ονομάσουμε Ευανθία, και τη φωνάζουμε Εύα για συντομία. Και αν κάνουμε δεύτερο παιδί, παίρνει το όνομα της δικής σου μητέρας. Έτσι δεν θα παρεξηγηθεί κανείς.", "Two names are a bit heavy for a baby. Let's name her Evanthia and call her Eva for short. And if we have a second child, it gets your mother's name. That way nobody will take offence."),
 ],
 "questions": [
  Q("Ποια είναι η παράδοση στην οικογένεια του Γιάννη;", ["Το πρώτο παιδί παίρνει το όνομα του νονού", "Το πρώτο παιδί παίρνει το όνομα της γιαγιάς από τη μεριά του πατέρα", "Τα παιδιά παίρνουν όνομα αγίου", "Το πρώτο παιδί παίρνει το όνομα της μητέρας"], 1, "Το πρώτο παιδί παίρνει το όνομα της γιαγιάς από τη μεριά του πατέρα"),
  Q("Γιατί ανησυχεί η Ειρήνη;", ["Επειδή δεν της αρέσει το όνομα Ευανθία", "Επειδή η μητέρα της θα στενοχωρηθεί", "Επειδή το όνομα είναι πολύ μεγάλο", "Επειδή ο Γιάννης δεν θέλει παιδί"], 1, "η δική μου μητέρα θα στενοχωρηθεί"),
  Q("Τι προτείνει τελικά ο Γιάννης;", ["Να δώσουν δύο ονόματα", "Να την ονομάσουν Ευανθία και να τη φωνάζουν Εύα", "Να διαλέξουν ένα καινούργιο όνομα", "Να αποφασίσουν οι γιαγιάδες"], 1, "Ας την ονομάσουμε Ευανθία, και τη φωνάζουμε Εύα για συντομία"),
 ],
 "gloss": {"θα τη βγάλουμε": "βγάζω (όνομα) — to name (a child)", "παράδοση": "παράδοση — tradition", "μεριά": "μεριά — side", "υποχρέωση": "υποχρέωση — obligation", "θα στενοχωρηθεί": "στενοχωριέμαι — to be upset", "εγγόνι": "εγγόνι — grandchild", "βαριά": "βαρύς — heavy", "Ας την ονομάσουμε": "ονομάζω — to name", "για συντομία": "για συντομία — for short", "δεν θα παρεξηγηθεί": "παρεξηγούμαι — to take offence"},
})

ITEMS.append({
 "id": "l50-dia-skini", "title": "Σαββατοκύριακο στη σκηνή", "title_en": "A weekend in a tent", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε δύο φίλους να οργανώνουν ένα Σαββατοκύριακο με σκηνή στην παραλία.",
 "script": [
  L("Θοδωρής", "m", "Λοιπόν, για το Σαββατοκύριακο σκέφτηκα να πάμε με σκηνή σε εκείνη την παραλία στην Εύβοια που μας είχε πει ο Άρης. Δεν έχει τίποτα, ούτε ταβέρνα ούτε ντους. Μόνο θάλασσα και πεύκα.", "So, for the weekend I thought we'd go camping on that beach in Evia that Aris told us about. There's nothing there, no taverna, no shower. Just sea and pine trees."),
  L("Λένα", "f", "Ακούγεται υπέροχο, αλλά ξέρεις ότι το ελεύθερο κάμπινγκ απαγορεύεται; Αν έρθει το λιμενικό, μπορεί να μας βάλει πρόστιμο. Δεν θα ήταν καλύτερα να πάμε σε ένα οργανωμένο κάμπινγκ;", "Sounds wonderful, but you know free camping is forbidden? If the coastguard comes, they might fine us. Wouldn't it be better to go to an organised campsite?"),
  L("Θοδωρής", "m", "Έχεις δίκιο. Υπάρχει ένα μικρό κάμπινγκ δέκα λεπτά από εκεί, με σκιά και καθαρές τουαλέτες. Κοστίζει οχτώ ευρώ το άτομο τη νύχτα. Και το πρωί μπορούμε να περπατήσουμε μέχρι την ερημική παραλία.", "You're right. There's a small campsite ten minutes from there, with shade and clean toilets. It costs eight euros per person per night. And in the morning we can walk to the deserted beach."),
  L("Λένα", "f", "Τέλεια. Εγώ θα φέρω τη σκηνή και το γκαζάκι για τον καφέ. Εσύ φέρε τα υπνόσακα και κάνε τα ψώνια. Και θυμήσου να βάλεις αντικουνουπικό, γιατί την περασμένη φορά μας έφαγαν τα κουνούπια!", "Perfect. I'll bring the tent and the little gas stove for coffee. You bring the sleeping bags and do the shopping. And remember to pack mosquito repellent, because last time the mosquitoes ate us alive!"),
 ],
 "questions": [
  Q("Γιατί η Λένα δεν θέλει να μείνουν στην ερημική παραλία;", ["Επειδή δεν έχει σκιά", "Επειδή το ελεύθερο κάμπινγκ απαγορεύεται", "Επειδή είναι πολύ μακριά", "Επειδή έχει πολύ κόσμο"], 1, "ξέρεις ότι το ελεύθερο κάμπινγκ απαγορεύεται;"),
  Q("Πόσο κοστίζει το κάμπινγκ;", ["Πέντε ευρώ τη νύχτα για δύο άτομα", "Οχτώ ευρώ το άτομο τη νύχτα", "Δέκα ευρώ τη μέρα", "Είναι δωρεάν"], 1, "Κοστίζει οχτώ ευρώ το άτομο τη νύχτα"),
  Q("Τι θα φέρει η Λένα;", ["Τα υπνόσακα και τα ψώνια", "Τη σκηνή και το γκαζάκι", "Το αντικουνουπικό", "Το φαγητό"], 1, "Εγώ θα φέρω τη σκηνή και το γκαζάκι για τον καφέ"),
 ],
 "gloss": {"σκηνή": "σκηνή — tent; stage", "πεύκα": "πεύκο — pine tree", "ελεύθερο κάμπινγκ": "ελεύθερο κάμπινγκ — wild camping", "λιμενικό": "λιμενικό — coastguard", "πρόστιμο": "πρόστιμο — fine", "οργανωμένο κάμπινγκ": "οργανωμένο κάμπινγκ — organised campsite", "ερημική": "ερημικός — deserted, remote", "γκαζάκι": "γκαζάκι — small camping gas stove", "υπνόσακα": "υπνόσακος — sleeping bag", "αντικουνουπικό": "αντικουνουπικό — mosquito repellent", "κουνούπια": "κουνούπι — mosquito"},
})

ITEMS.append({
 "id": "l50-int-violi", "title": "Το βιολί των πανηγυριών", "title_en": "The festival fiddle", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με έναν νέο βιολιστή που παίζει παραδοσιακή μουσική σε πανηγύρια.",
 "script": [
  L("Δημοσιογράφος", "f", "Λευτέρη, είσαι μόλις είκοσι τεσσάρων χρονών και παίζεις κάθε καλοκαίρι σε δεκάδες πανηγύρια. Πώς ξεκίνησες;", "Lefteris, you're only twenty-four and you play at dozens of village festivals every summer. How did you start?"),
  L("Λευτέρης", "m", "Ο παππούς μου έπαιζε βιολί στα χωριά της Ηπείρου. Όταν ήμουν μικρός, τον ακολουθούσα στα πανηγύρια και κοιμόμουν κάτω από τα τραπέζια. Στα δέκα μου μού χάρισε το πρώτο μου βιολί. Μετά σπούδασα κλασικό βιολί στο ωδείο, αλλά η καρδιά μου ήταν πάντα στα δημοτικά.", "My grandfather played the fiddle in the villages of Epirus. When I was little I followed him to festivals and slept under the tables. At ten he gave me my first violin. Later I studied classical violin at the conservatory, but my heart was always in folk music."),
  L("Δημοσιογράφος", "f", "Τι διαφορά έχει να παίζεις σε ένα πανηγύρι από το να παίζεις σε μια αίθουσα συναυλιών;", "What's the difference between playing at a festival and playing in a concert hall?"),
  L("Λευτέρης", "m", "Στη συναυλία ο κόσμος κάθεται και ακούει. Στο πανηγύρι ο κόσμος χορεύει, και εσύ πρέπει να τον ακολουθείς. Αν ο πρώτος χορευτής θέλει να αργήσεις, αργείς. Είναι ένας διάλογος. Και συχνά παίζουμε από τις δέκα το βράδυ μέχρι τις έξι το πρωί, χωρίς διάλειμμα.", "At a concert people sit and listen. At a festival people dance, and you have to follow them. If the leading dancer wants you to slow down, you slow down. It's a dialogue. And we often play from ten at night until six in the morning, without a break."),
  L("Δημοσιογράφος", "f", "Βλέπεις ενδιαφέρον από τους νέους;", "Do you see interest from young people?"),
  L("Λευτέρης", "m", "Πάρα πολύ. Πριν από δέκα χρόνια, στα πανηγύρια χόρευαν κυρίως μεγάλοι. Τώρα η πίστα γεμίζει παιδιά είκοσι χρονών, που ξέρουν όλα τα βήματα. Νομίζω ότι, σε μια εποχή που όλα είναι ψηφιακά, οι νέοι ψάχνουν κάτι αληθινό, κάτι που τους δένει με τον τόπο τους.", "Very much. Ten years ago, it was mainly older people who danced at festivals. Now the dance floor fills with twenty-year-olds who know all the steps. I think that, at a time when everything is digital, young people are looking for something real, something that ties them to their place."),
 ],
 "questions": [
  Q("Πώς γνώρισε ο Λευτέρης την παραδοσιακή μουσική;", ["Από το ραδιόφωνο", "Ακολουθώντας τον παππού του στα πανηγύρια", "Στο σχολείο", "Από τον πατέρα του στην Αθήνα"], 1, "τον ακολουθούσα στα πανηγύρια και κοιμόμουν κάτω από τα τραπέζια"),
  Q("Τι λέει για το παίξιμο στο πανηγύρι;", ["Ότι είναι πιο εύκολο από τη συναυλία", "Ότι ο μουσικός πρέπει να ακολουθεί τους χορευτές", "Ότι ο κόσμος κάθεται και ακούει", "Ότι παίζουν μόνο δύο ώρες"], 1, "Στο πανηγύρι ο κόσμος χορεύει, και εσύ πρέπει να τον ακολουθείς"),
  Q("Πώς εξηγεί το ενδιαφέρον των νέων;", ["Είναι μια μόδα που θα περάσει", "Οι νέοι ψάχνουν κάτι αληθινό που τους δένει με τον τόπο τους", "Τα πανηγύρια είναι φτηνά", "Τους αναγκάζουν οι γονείς τους"], 1, "οι νέοι ψάχνουν κάτι αληθινό, κάτι που τους δένει με τον τόπο τους"),
 ],
 "gloss": {"βιολιστή": "βιολιστής — violinist, fiddler", "πανηγύρια": "πανηγύρι — village festival", "μού χάρισε": "χαρίζω — to give as a gift", "ωδείο": "ωδείο — conservatory, music school", "δημοτικά": "δημοτικά (τραγούδια) — folk songs", "αίθουσα συναυλιών": "αίθουσα συναυλιών — concert hall", "πρώτος χορευτής": "πρώτος χορευτής — leading dancer (at the head of the line)", "διάλειμμα": "διάλειμμα — break", "πίστα": "πίστα — dance floor", "βήματα": "βήμα — step", "τους δένει": "δένω — to tie, bind"},
})

ITEMS.append({
 "id": "l50-rep-lykoi", "title": "Λύκοι κοντά στα χωριά", "title_en": "Wolves near the villages", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από ένα ραδιοφωνικό δελτίο ειδήσεων για την παρουσία λύκων σε ορεινές περιοχές.",
 "script": [
  L("Ρεπόρτερ", "m", "Τους τελευταίους μήνες, κάτοικοι χωριών στη Φωκίδα και την Ευρυτανία αναφέρουν ότι βλέπουν λύκους όλο και πιο κοντά στα σπίτια τους. Σε ορισμένες περιπτώσεις, λύκοι επιτέθηκαν σε κοπάδια και σκότωσαν πρόβατα και κατσίκες, προκαλώντας την οργή των κτηνοτρόφων.", "In recent months, residents of villages in Phocis and Evrytania report seeing wolves closer and closer to their homes. In some cases wolves have attacked flocks and killed sheep and goats, angering the livestock farmers."),
  L("Ρεπόρτερ", "m", "Οι επιστήμονες εξηγούν ότι ο πληθυσμός του λύκου στην Ελλάδα έχει αυξηθεί, επειδή το είδος προστατεύεται από τον νόμο και επειδή πολλά ορεινά χωριά έχουν ερημώσει. Τονίζουν, όμως, ότι ο λύκος σπάνια επιτίθεται σε ανθρώπους και ότι συνήθως αποφεύγει την επαφή μαζί τους.", "Scientists explain that the wolf population in Greece has grown, because the species is protected by law and because many mountain villages have been abandoned. They stress, however, that wolves rarely attack people and usually avoid contact with them."),
  L("Ρεπόρτερ", "m", "Περιβαλλοντικές οργανώσεις προτείνουν στους κτηνοτρόφους να χρησιμοποιούν ηλεκτρικούς φράχτες και ποιμενικά σκυλιά, που αποδεικνύονται ιδιαίτερα αποτελεσματικά. Το υπουργείο, από την πλευρά του, εξετάζει να αυξήσει τις αποζημιώσεις για όσους χάνουν ζώα, οι οποίες σήμερα καθυστερούν συχνά πάνω από έναν χρόνο.", "Environmental organisations suggest that farmers use electric fences and sheepdogs, which are proving particularly effective. The ministry, for its part, is considering raising the compensation for those who lose animals, which today is often delayed by more than a year."),
 ],
 "questions": [
  Q("Γιατί είναι θυμωμένοι οι κτηνοτρόφοι;", ["Επειδή έκλεισαν οι δρόμοι", "Επειδή λύκοι σκότωσαν πρόβατα και κατσίκες", "Επειδή αυξήθηκαν οι φόροι", "Επειδή δεν βρίσκουν εργάτες"], 1, "λύκοι επιτέθηκαν σε κοπάδια και σκότωσαν πρόβατα και κατσίκες"),
  Q("Γιατί, κατά τους επιστήμονες, αυξήθηκε ο πληθυσμός του λύκου;", ["Επειδή ήρθαν λύκοι από άλλες χώρες", "Επειδή προστατεύεται από τον νόμο και έχουν ερημώσει πολλά χωριά", "Επειδή αυξήθηκαν τα πρόβατα", "Επειδή ο χειμώνας ήταν ήπιος"], 1, "επειδή το είδος προστατεύεται από τον νόμο και επειδή πολλά ορεινά χωριά έχουν ερημώσει"),
  Q("Ποιο πρόβλημα υπάρχει με τις αποζημιώσεις;", ["Δεν δίνονται καθόλου", "Καθυστερούν συχνά πάνω από έναν χρόνο", "Δίνονται μόνο για πρόβατα", "Είναι πολύ υψηλές"], 1, "οι οποίες σήμερα καθυστερούν συχνά πάνω από έναν χρόνο"),
 ],
 "gloss": {"λύκων": "λύκος — wolf", "λύκους": "λύκος — wolf", "επιτέθηκαν": "επιτίθεμαι — to attack", "κοπάδια": "κοπάδι — flock, herd", "οργή": "οργή — anger, fury", "κτηνοτρόφων": "κτηνοτρόφος — livestock farmer", "πληθυσμός": "πληθυσμός — population", "έχουν ερημώσει": "ερημώνω — to become deserted", "Τονίζουν": "τονίζω — to stress", "ηλεκτρικούς φράχτες": "ηλεκτρικός φράχτης — electric fence", "ποιμενικά σκυλιά": "ποιμενικό σκυλί — sheepdog", "αποζημιώσεις": "αποζημίωση — compensation"},
})

ITEMS.append({
 "id": "l50-dia-douleies-spitiou", "title": "Οι δουλειές του σπιτιού", "title_en": "The household chores", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε τρεις φοιτητές που μένουν μαζί να συζητούν πώς θα μοιράσουν τις δουλειές του σπιτιού.",
 "script": [
  L("Μυρτώ", "f", "Παιδιά, πρέπει να μιλήσουμε. Τα πιάτα μένουν άπλυτα για μέρες, και το μπάνιο το καθάρισα εγώ τρεις φορές συνέχεια. Δεν γίνεται έτσι.", "Guys, we need to talk. The dishes stay unwashed for days, and I've cleaned the bathroom three times in a row. It can't go on like this."),
  L("Κώστας", "m", "Έχεις δίκιο, συγγνώμη. Αυτή την εβδομάδα είχα εξεταστική και δεν πρόλαβα τίποτα. Τι λέτε να φτιάξουμε ένα πρόγραμμα και να το κολλήσουμε στο ψυγείο; Κάθε εβδομάδα ο καθένας θα έχει διαφορετική δουλειά.", "You're right, sorry. This week I had exams and didn't get round to anything. What do you say we make a rota and stick it on the fridge? Each week everyone will have a different job."),
  L("Νίκος", "m", "Συμφωνώ. Εγώ όμως προτείνω τα πιάτα να τα πλένει ο καθένας αμέσως μόλις φάει. Δεν είναι δίκαιο να πλένει ένας τα πιάτα των άλλων. Και τα ψώνια για τα κοινά, χαρτί υγείας, απορρυπαντικά, να τα πληρώνουμε από ένα κοινό ταμείο.", "I agree. But I suggest everyone washes their own dishes right after eating. It's not fair for one person to wash everyone else's. And the shared shopping, toilet paper, detergents, we should pay for from a common kitty."),
  L("Μυρτώ", "f", "Ωραία. Τότε βάζουμε από δέκα ευρώ τον μήνα στο κουτί πάνω στο ράφι. Και όποιος δεν κάνει τη δουλειά του, κερνάει πίτσα την Παρασκευή. Έγινε;", "Great. Then we each put ten euros a month into the box on the shelf. And whoever doesn't do their job buys pizza on Friday. Deal?"),
 ],
 "questions": [
  Q("Γιατί παραπονιέται η Μυρτώ;", ["Επειδή οι άλλοι κάνουν θόρυβο", "Επειδή καθάρισε μόνη της το μπάνιο τρεις φορές", "Επειδή δεν πληρώθηκε το ενοίκιο", "Επειδή χάλασε το ψυγείο"], 1, "το μπάνιο το καθάρισα εγώ τρεις φορές συνέχεια"),
  Q("Τι προτείνει ο Νίκος για τα πιάτα;", ["Να τα πλένει η Μυρτώ", "Να πλένει ο καθένας τα δικά του αμέσως μόλις φάει", "Να αγοράσουν πλυντήριο πιάτων", "Να τα πλένουν μία φορά την εβδομάδα"], 1, "προτείνω τα πιάτα να τα πλένει ο καθένας αμέσως μόλις φάει"),
  Q("Τι θα γίνεται με όποιον δεν κάνει τη δουλειά του;", ["Θα πληρώνει πρόστιμο δέκα ευρώ", "Θα κερνάει πίτσα την Παρασκευή", "Θα φύγει από το σπίτι", "Θα καθαρίζει μόνος του όλο το σπίτι"], 1, "όποιος δεν κάνει τη δουλειά του, κερνάει πίτσα την Παρασκευή"),
 ],
 "gloss": {"άπλυτα": "άπλυτος — unwashed", "συνέχεια": "συνέχεια — in a row, continuously", "εξεταστική": "εξεταστική — exam period", "δεν πρόλαβα": "προλαβαίνω — to manage (in time)", "πρόγραμμα": "πρόγραμμα — schedule, rota", "να το κολλήσουμε": "κολλάω — to stick", "δίκαιο": "δίκαιος — fair", "απορρυπαντικά": "απορρυπαντικό — detergent", "κοινό ταμείο": "κοινό ταμείο — common fund, kitty", "ράφι": "ράφι — shelf", "κερνάει": "κερνάω — to treat (someone to something)"},
})

ITEMS.append({
 "id": "l50-mono-kompostopoiisi", "title": "Ο κάδος κομποστοποίησης", "title_en": "The compost bin", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια υπάλληλο του δήμου να εξηγεί σε μια συνάντηση κατοίκων πώς χρησιμοποιείται ο κάδος κομποστοποίησης που μοιράζει ο δήμος.",
 "script": [
  L("Υπάλληλος", "f", "Καλησπέρα σας. Από τον επόμενο μήνα, ο δήμος μας θα μοιράσει δωρεάν κάδους κομποστοποίησης σε όσα νοικοκυριά έχουν κήπο ή αυλή. Το κομπόστ είναι ένα φυσικό λίπασμα που φτιάχνεται από τα οργανικά απορρίμματα του σπιτιού. Σχεδόν το ένα τρίτο των σκουπιδιών μας μπορεί να γίνει κομπόστ αντί να καταλήξει στη χωματερή.", "Good evening. From next month, our municipality will hand out free compost bins to households with a garden or yard. Compost is a natural fertiliser made from the household's organic waste. Almost a third of our rubbish can become compost instead of ending up in the landfill."),
  L("Υπάλληλος", "f", "Στον κάδο βάζετε φλούδες από φρούτα και λαχανικά, υπολείμματα καφέ, τσόφλια αυγών, ξερά φύλλα και κομμένο γρασίδι. Δεν βάζετε κρέας, ψάρι, γαλακτοκομικά ή λάδι, γιατί μυρίζουν και τραβάνε ζώα. Το σημαντικό είναι να υπάρχει ισορροπία ανάμεσα στα πράσινα υλικά, που είναι υγρά, και στα καφέ, που είναι ξερά.", "In the bin you put fruit and vegetable peel, coffee grounds, eggshells, dry leaves and grass cuttings. You don't put in meat, fish, dairy or oil, because they smell and attract animals. The important thing is to have a balance between green materials, which are wet, and brown ones, which are dry."),
  L("Υπάλληλος", "f", "Μία φορά την εβδομάδα ανακατεύετε το περιεχόμενο με ένα φτυάρι, για να μπαίνει αέρας. Αν το κομπόστ μυρίζει άσχημα, σημαίνει ότι είναι πολύ υγρό, και πρέπει να προσθέσετε ξερά φύλλα. Μετά από τέσσερις με έξι μήνες θα έχετε ένα σκούρο, αφράτο χώμα, ιδανικό για τις γλάστρες και τον κήπο σας.", "Once a week you mix the contents with a spade, to let air in. If the compost smells bad, it means it's too wet, and you need to add dry leaves. After four to six months you'll have dark, crumbly soil, ideal for your pots and garden."),
 ],
 "questions": [
  Q("Σε ποιους θα μοιραστούν οι κάδοι;", ["Σε όλα τα σχολεία", "Σε νοικοκυριά με κήπο ή αυλή", "Μόνο σε αγρότες", "Σε όσους πληρώσουν"], 1, "σε όσα νοικοκυριά έχουν κήπο ή αυλή"),
  Q("Γιατί δεν βάζουμε κρέας και ψάρι στον κάδο;", ["Επειδή δεν σαπίζουν", "Επειδή μυρίζουν και τραβάνε ζώα", "Επειδή απαγορεύεται από τον νόμο", "Επειδή χαλάνε τον κάδο"], 1, "γιατί μυρίζουν και τραβάνε ζώα"),
  Q("Τι πρέπει να κάνουμε αν το κομπόστ μυρίζει άσχημα;", ["Να ρίξουμε νερό", "Να προσθέσουμε ξερά φύλλα", "Να το πετάξουμε", "Να το σκεπάσουμε με πλαστικό"], 1, "είναι πολύ υγρό, και πρέπει να προσθέσετε ξερά φύλλα"),
 ],
 "gloss": {"κάδος κομποστοποίησης": "κάδος κομποστοποίησης — compost bin", "κάδους κομποστοποίησης": "κάδος κομποστοποίησης — compost bin", "νοικοκυριά": "νοικοκυριό — household", "λίπασμα": "λίπασμα — fertiliser", "οργανικά απορρίμματα": "οργανικά απορρίμματα — organic waste", "χωματερή": "χωματερή — landfill, rubbish tip", "φλούδες": "φλούδα — peel", "τσόφλια": "τσόφλι — shell (of an egg)", "γρασίδι": "γρασίδι — grass, lawn", "γαλακτοκομικά": "γαλακτοκομικά — dairy products", "ανακατεύετε": "ανακατεύω — to mix, stir", "φτυάρι": "φτυάρι — spade, shovel", "αφράτο": "αφράτος — fluffy, crumbly"},
})

ITEMS.append({
 "id": "l50-c1-gkrafiti", "title": "Γκράφιτι: τέχνη ή βανδαλισμός;", "title_en": "Graffiti: art or vandalism?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συζήτηση με έναν κοινωνιολόγο που μελετά την τέχνη του δρόμου στην Αθήνα.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Μαργαρίτη, η Αθήνα έχει γίνει, σύμφωνα με ξένα μέσα, μία από τις «πρωτεύουσες του γκράφιτι» στην Ευρώπη. Είναι αυτό λόγος περηφάνιας ή ντροπής;", "Mr Margaritis, according to foreign media, Athens has become one of Europe's 'graffiti capitals'. Is that a reason for pride or shame?"),
  L("Κοινωνιολόγος", "m", "Και τα δύο, και γι' αυτό η συζήτηση είναι τόσο φορτισμένη. Πρέπει, πρώτα απ' όλα, να διακρίνουμε τα φαινόμενα. Το τάγκινγκ, δηλαδή οι υπογραφές που καλύπτουν προσόψεις και μνημεία, είναι κατά κανόνα πράξη ιδιοποίησης του χώρου, όχι αισθητικής δημιουργίας. Οι μεγάλες τοιχογραφίες, αντίθετα, είναι συχνά έργα με καλλιτεχνική πρόθεση, ορισμένες φορές και με την άδεια του ιδιοκτήτη.", "Both, and that's why the debate is so charged. First of all, we have to distinguish between the phenomena. Tagging, that is the signatures that cover facades and monuments, is as a rule an act of appropriating space, not of aesthetic creation. Large murals, on the other hand, are often works with artistic intent, sometimes even with the owner's permission."),
  L("Δημοσιογράφος", "f", "Γιατί εξαπλώθηκε τόσο το φαινόμενο στην Αθήνα;", "Why did the phenomenon spread so much in Athens?"),
  L("Κοινωνιολόγος", "m", "Η οικονομική κρίση έπαιξε καθοριστικό ρόλο. Κλειστά καταστήματα, εγκαταλελειμμένα κτίρια και μια γενικευμένη αίσθηση οργής δημιούργησαν ταυτόχρονα τον καμβά και το κίνητρο. Πολλά από τα έργα εκείνης της περιόδου είναι βαθιά πολιτικά: σχολιάζουν τη λιτότητα, τη μετανάστευση, την ανεργία των νέων. Από αυτή την άποψη, λειτουργούν ως ένα είδος ανεπίσημου χρονικού της εποχής.", "The economic crisis played a decisive role. Closed shops, abandoned buildings and a widespread sense of anger created both the canvas and the motive at the same time. Many works from that period are deeply political: they comment on austerity, migration, youth unemployment. In that sense, they function as a kind of unofficial chronicle of the era."),
  L("Δημοσιογράφος", "f", "Και ποια θα ήταν μια λογική πολιτική για τον δήμο;", "And what would be a sensible policy for the municipality?"),
  L("Κοινωνιολόγος", "m", "Η απόλυτη καταστολή έχει αποδειχθεί αναποτελεσματική: ό,τι σβήνεται το πρωί, ξαναγράφεται το βράδυ. Αυτό που φαίνεται να αποδίδει είναι ένας συνδυασμός: αυστηρή προστασία των μνημείων και των ιστορικών κτιρίων, και παράλληλα νόμιμοι χώροι, όπου οι καλλιτέχνες μπορούν να δημιουργούν ελεύθερα. Όταν ένας τοίχος φιλοξενεί μια αξιόλογη τοιχογραφία, σπάνια τον αγγίζουν άλλοι.", "Absolute repression has proved ineffective: whatever is erased in the morning is rewritten at night. What seems to work is a combination: strict protection of monuments and historic buildings, and alongside that legal spaces where artists can create freely. When a wall hosts a worthwhile mural, others rarely touch it."),
 ],
 "questions": [
  Q("Πώς χαρακτηρίζει ο κοινωνιολόγος το τάγκινγκ;", ["Ως μορφή υψηλής τέχνης", "Ως πράξη ιδιοποίησης του χώρου", "Ως νόμιμη διαφήμιση", "Ως παιδικό παιχνίδι"], 1, "είναι κατά κανόνα πράξη ιδιοποίησης του χώρου, όχι αισθητικής δημιουργίας"),
  Q("Ποιον ρόλο έπαιξε η οικονομική κρίση;", ["Κανέναν", "Δημιούργησε ταυτόχρονα τον «καμβά» και το κίνητρο", "Μείωσε τα γκράφιτι", "Έφερε ξένους καλλιτέχνες"], 1, "δημιούργησαν ταυτόχρονα τον καμβά και το κίνητρο"),
  Q("Γιατί λέει ότι τα έργα εκείνης της περιόδου είναι «ανεπίσημο χρονικό»;", ["Επειδή έχουν ημερομηνίες", "Επειδή σχολιάζουν τα προβλήματα της εποχής", "Επειδή φτιάχτηκαν από δημοσιογράφους", "Επειδή βρίσκονται σε μουσεία"], 1, "σχολιάζουν τη λιτότητα, τη μετανάστευση, την ανεργία των νέων"),
  Q("Ποια πολιτική θεωρεί αποτελεσματική;", ["Την απόλυτη καταστολή", "Προστασία των μνημείων και ταυτόχρονα νόμιμους χώρους για τους καλλιτέχνες", "Να σβήνονται όλα τα γκράφιτι κάθε πρωί", "Να μην κάνει τίποτα ο δήμος"], 1, "αυστηρή προστασία των μνημείων ... και παράλληλα νόμιμοι χώροι"),
 ],
 "gloss": {"κοινωνιολόγο": "κοινωνιολόγος — sociologist", "περηφάνιας": "περηφάνια — pride", "φορτισμένη": "φορτισμένος — charged (emotionally)", "να διακρίνουμε": "διακρίνω — to distinguish", "προσόψεις": "πρόσοψη — facade", "ιδιοποίησης": "ιδιοποίηση — appropriation", "πρόθεση": "πρόθεση — intention", "εξαπλώθηκε": "εξαπλώνομαι — to spread", "εγκαταλελειμμένα": "εγκαταλελειμμένος — abandoned", "καμβά": "καμβάς — canvas", "κίνητρο": "κίνητρο — motive, incentive", "λιτότητα": "λιτότητα — austerity", "χρονικού": "χρονικό — chronicle", "καταστολή": "καταστολή — repression, suppression", "να αποδίδει": "αποδίδω — to pay off, be effective", "αξιόλογη": "αξιόλογος — worthwhile, notable"},
})

ITEMS.append({
 "id": "l50-c1-mikrasiatiki-logotechnia", "title": "Η Μικρασιατική Καταστροφή στη λογοτεχνία", "title_en": "The Asia Minor Catastrophe in literature", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη για το πώς αποτυπώθηκε η Μικρασιατική Καταστροφή του 1922 στην ελληνική λογοτεχνία.",
 "script": [
  L("Ομιλητής", "m", "Η Μικρασιατική Καταστροφή του 1922 δεν ήταν μόνο ένα στρατιωτικό και πολιτικό γεγονός. Ήταν ένα τραύμα που σημάδεψε γενιές, καθώς πάνω από ένα εκατομμύριο πρόσφυγες ξεριζώθηκαν από τις πατρίδες τους. Δεν είναι παράξενο ότι η λογοτεχνία επέστρεφε σε αυτό ξανά και ξανά, σαν να προσπαθούσε να το επεξεργαστεί.", "The Asia Minor Catastrophe of 1922 was not only a military and political event. It was a trauma that marked generations, as more than a million refugees were uprooted from their homelands. It is no wonder that literature returned to it again and again, as if trying to process it."),
  L("Ομιλητής", "m", "Ένα από τα πρώτα και πιο συγκλονιστικά κείμενα είναι «Το νούμερο 31328» του Ηλία Βενέζη. Ο Βενέζης, γεννημένος στο Αϊβαλί, αιχμαλωτίστηκε το 1922 και στάλθηκε στα τάγματα εργασίας. Ο τίτλος είναι ο αριθμός που του είχε δοθεί ως αιχμαλώτου. Το βιβλίο, γραμμένο με λιτή, σχεδόν ξερή γλώσσα, αρνείται τον μελοδραματισμό· η φρίκη αφήνεται να μιλήσει μόνη της.", "One of the first and most harrowing texts is 'Number 31328' by Ilias Venezis. Venezis, born in Ayvalik, was taken prisoner in 1922 and sent to the labour battalions. The title is the number he had been given as a prisoner. The book, written in sparse, almost dry language, refuses melodrama; the horror is left to speak for itself."),
  L("Ομιλητής", "m", "Τέσσερις δεκαετίες αργότερα, το 1962, η Διδώ Σωτηρίου δημοσίευσε τα «Ματωμένα χώματα». Η αφήγηση γίνεται από έναν απλό αγρότη, τον Μανώλη Αξιώτη, και αυτό που κάνει το βιβλίο ξεχωριστό είναι ότι δείχνει τη συμβίωση Ελλήνων και Τούρκων πριν από τον πόλεμο. Οι εχθροί δεν είναι οι λαοί, αλλά ο εθνικισμός και τα συμφέροντα που τους έστρεψαν τον έναν εναντίον του άλλου.", "Four decades later, in 1962, Dido Sotiriou published 'Farewell Anatolia' (literally 'Blood-soaked earth'). The narrator is a simple farmer, Manolis Axiotis, and what makes the book distinctive is that it shows Greeks and Turks living together before the war. The enemies are not the peoples, but nationalism and the interests that turned them against each other."),
  L("Ομιλητής", "m", "Τέλος, ένα χρόνο μετά, ο Κοσμάς Πολίτης έγραψε το «Στου Χατζηφράγκου», ένα μυθιστόρημα για μια γειτονιά της Σμύρνης πριν από την καταστροφή. Εδώ δεν κυριαρχεί η τραγωδία, αλλά η νοσταλγία για έναν πολυπολιτισμικό κόσμο που χάθηκε για πάντα. Αν τα τρία αυτά βιβλία διαβαστούν μαζί, συνθέτουν μια εικόνα του 1922 όχι ως αφηρημένου εθνικού γεγονότος, αλλά ως ανθρώπινης εμπειρίας.", "Finally, a year later, Kosmas Politis wrote 'At Hatzifrangou's', a novel about a neighbourhood of Smyrna before the catastrophe. Here tragedy does not dominate, but nostalgia for a multicultural world lost forever. If these three books are read together, they compose a picture of 1922 not as an abstract national event but as a human experience."),
 ],
 "questions": [
  Q("Γιατί, κατά τον ομιλητή, η λογοτεχνία επέστρεφε συνεχώς στην Καταστροφή;", ["Επειδή το ζητούσαν οι εκδότες", "Επειδή ήταν ένα τραύμα που προσπαθούσε να επεξεργαστεί", "Επειδή ήταν της μόδας", "Επειδή το επέβαλλε το κράτος"], 1, "σαν να προσπαθούσε να το επεξεργαστεί"),
  Q("Τι σημαίνει ο τίτλος «Το νούμερο 31328»;", ["Είναι η χρονιά της έκδοσης", "Είναι ο αριθμός που είχε δοθεί στον Βενέζη ως αιχμάλωτο", "Είναι ο αριθμός του σπιτιού του", "Είναι ο αριθμός των προσφύγων"], 1, "Ο τίτλος είναι ο αριθμός που του είχε δοθεί ως αιχμαλώτου"),
  Q("Τι κάνει ξεχωριστά τα «Ματωμένα χώματα»;", ["Ότι γράφτηκαν από στρατηγό", "Ότι δείχνουν τη συμβίωση Ελλήνων και Τούρκων πριν από τον πόλεμο", "Ότι γράφτηκαν στα τουρκικά", "Ότι δεν αναφέρουν τον πόλεμο"], 1, "δείχνει τη συμβίωση Ελλήνων και Τούρκων πριν από τον πόλεμο"),
  Q("Τι κυριαρχεί στο «Στου Χατζηφράγκου»;", ["Η περιγραφή των μαχών", "Η νοσταλγία για έναν πολυπολιτισμικό κόσμο που χάθηκε", "Η πολιτική ανάλυση", "Το χιούμορ"], 1, "δεν κυριαρχεί η τραγωδία, αλλά η νοσταλγία για έναν πολυπολιτισμικό κόσμο"),
 ],
 "gloss": {"αποτυπώθηκε": "αποτυπώνομαι — to be depicted, recorded", "τραύμα": "τραύμα — trauma, wound", "σημάδεψε": "σημαδεύω — to mark", "ξεριζώθηκαν": "ξεριζώνομαι — to be uprooted", "να το επεξεργαστεί": "επεξεργάζομαι — to process, work through", "συγκλονιστικά": "συγκλονιστικός — harrowing, shattering", "αιχμαλωτίστηκε": "αιχμαλωτίζομαι — to be taken prisoner", "τάγματα εργασίας": "τάγματα εργασίας — labour battalions", "αιχμαλώτου": "αιχμάλωτος — prisoner of war", "λιτή": "λιτός — sparse, plain", "μελοδραματισμό": "μελοδραματισμός — melodrama", "φρίκη": "φρίκη — horror", "αφήγηση": "αφήγηση — narration", "συμβίωση": "συμβίωση — living together, coexistence", "εθνικισμός": "εθνικισμός — nationalism", "νοσταλγία": "νοσταλγία — nostalgia", "πολυπολιτισμικό": "πολυπολιτισμικός — multicultural", "αφηρημένου": "αφηρημένος — abstract"},
})

rnd = random.Random(50)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-50.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
