# Source for library/listening/listening-245.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l245.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l245-news-vyzantina-nomismata", "title": "Βυζαντινά νομίσματα βρέθηκαν σε οικόπεδο κατά τις εκσκαφές", "title_en": "Byzantine coins found on a building plot during excavation", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός τοπικού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνήτρια", "f", "Ένα πήλινο αγγείο γεμάτο χρυσά και χάλκινα νομίσματα βρέθηκε την Τρίτη σε ένα οικόπεδο στο κέντρο της πόλης, όπου γίνονταν εκσκαφές για τα θεμέλια μιας νέας πολυκατοικίας.", "A clay pot full of gold and bronze coins was found on Tuesday on a plot in the town centre, where digging was under way for the foundations of a new apartment block."),
  L("Εκφωνήτρια", "f", "Τον θησαυρό τον εντόπισε ο χειριστής του εκσκαφέα, που σταμάτησε αμέσως τις εργασίες και ειδοποίησε την Εφορεία Αρχαιοτήτων. Σύμφωνα με τους αρχαιολόγους, τα νομίσματα είναι πάνω από διακόσια και χρονολογούνται στον ενδέκατο αιώνα.", "The treasure was spotted by the excavator operator, who immediately stopped work and notified the Ephorate of Antiquities. According to the archaeologists, there are more than two hundred coins and they date to the eleventh century."),
  L("Εκφωνήτρια", "f", "Οι ειδικοί πιστεύουν ότι κάποιος τα έκρυψε σε μια επικίνδυνη περίοδο, ίσως πριν από μια επιδρομή, και δεν γύρισε ποτέ να τα πάρει. Το αγγείο είχε θαφτεί κάτω από το δάπεδο ενός σπιτιού, που ήταν άγνωστο μέχρι σήμερα.", "The experts believe someone hid them during a dangerous period, perhaps before a raid, and never came back to collect them. The pot had been buried under the floor of a house that was unknown until now."),
  L("Εκφωνήτρια", "f", "Οι εργασίες στο οικόπεδο θα σταματήσουν για τουλάχιστον τρεις μήνες, όσο διαρκεί η ανασκαφή. Ο ιδιοκτήτης δήλωσε ότι δεν τον πειράζει η καθυστέρηση και ότι θα ήθελε να εκτεθούν τα νομίσματα στο μουσείο της πόλης.", "Work on the plot will stop for at least three months, while the excavation lasts. The owner said he doesn't mind the delay and would like the coins to be displayed in the town museum."),
 ],
 "questions": [
  Q("Πού βρέθηκαν τα νομίσματα;", ["Στον βυθό του λιμανιού", "Σε ένα οικόπεδο όπου θα χτιζόταν πολυκατοικία", "Σε μια παλιά εκκλησία", "Στο μουσείο της πόλης"], 1, "σε ένα οικόπεδο στο κέντρο της πόλης, όπου γίνονταν εκσκαφές για τα θεμέλια μιας νέας πολυκατοικίας"),
  Q("Τι έκανε ο χειριστής του εκσκαφέα;", ["Πήρε μερικά νομίσματα", "Σταμάτησε τις εργασίες και ειδοποίησε την Εφορεία Αρχαιοτήτων", "Ειδοποίησε την τηλεόραση", "Συνέχισε τη δουλειά του"], 1, "σταμάτησε αμέσως τις εργασίες και ειδοποίησε την Εφορεία Αρχαιοτήτων"),
  Q("Γιατί πιστεύουν οι ειδικοί ότι κρύφτηκαν τα νομίσματα;", ["Για να πληρωθούν φόροι", "Κάποιος τα έκρυψε σε μια επικίνδυνη περίοδο και δεν γύρισε", "Ήταν δώρο σε μια εκκλησία", "Ήταν πλαστά"], 1, "κάποιος τα έκρυψε σε μια επικίνδυνη περίοδο, ίσως πριν από μια επιδρομή, και δεν γύρισε ποτέ"),
  Q("Τι θα ήθελε ο ιδιοκτήτης του οικοπέδου;", ["Να πάρει αποζημίωση", "Να εκτεθούν τα νομίσματα στο μουσείο της πόλης", "Να πουλήσει το οικόπεδο", "Να συνεχιστούν αμέσως οι εργασίες"], 1, "θα ήθελε να εκτεθούν τα νομίσματα στο μουσείο της πόλης"),
 ],
 "gloss": {"πήλινο": "πήλινος — clay, earthenware", "εκσκαφές": "εκσκαφή — excavation, digging", "θεμέλια": "θεμέλια — foundations", "θησαυρό": "θησαυρός — treasure", "χειριστής": "χειριστής — operator", "εκσκαφέα": "εκσκαφέας — excavator, digger", "Εφορεία Αρχαιοτήτων": "Εφορεία Αρχαιοτήτων — (regional) Ephorate of Antiquities", "χρονολογούνται": "χρονολογούμαι — to date (from)", "επιδρομή": "επιδρομή — raid", "θαφτεί": "θάβομαι — to be buried", "δάπεδο": "δάπεδο — floor", "ανασκαφή": "ανασκαφή — (archaeological) excavation"},
})

ITEMS.append({
 "id": "l245-vm-lixiarxeio", "title": "Μήνυμα από το ληξιαρχείο: «Υπάρχει λάθος στο επώνυμό σας»", "title_en": "A message from the registry office: 'There is a mistake in your surname'", "type": "voicemail", "level": "B2",
 "context_el": "Πριν από λίγες εβδομάδες ζητήσατε ένα πιστοποιητικό από το ληξιαρχείο του δήμου σας. Ακούτε ένα μήνυμα που σας άφησε μια υπάλληλος στον τηλεφωνητή.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, σας παίρνω από το ληξιαρχείο του Δήμου, η Σταματία Ζαχαρίου. Ετοίμαζα το πιστοποιητικό που ζητήσατε για την αίτηση ιθαγένειας και πρόσεξα ότι στην παλιά ληξιαρχική πράξη το επώνυμό σας είναι γραμμένο με ένα λάθος γράμμα: «ι» αντί για «η».", "Good morning, I'm calling from the municipal registry office, it's Stamatia Zachariou. I was preparing the certificate you asked for for your citizenship application and noticed that in the old registry record your surname is written with a wrong letter: 'iota' instead of 'eta'."),
  L("Υπάλληλος", "f", "Αν βγάλουμε το πιστοποιητικό έτσι, μάλλον θα σας το επιστρέψουν από την υπηρεσία, γιατί δεν θα ταιριάζει με το διαβατήριό σας. Γι' αυτό είναι καλύτερα να κάνουμε πρώτα τη διόρθωση. Δεν είναι κάτι δύσκολο, αλλά χρειάζεται μια αίτηση και λίγα δικαιολογητικά.", "If we issue the certificate like that, they'll probably send it back to you from the department, because it won't match your passport. So it's better to make the correction first. It's nothing difficult, but it needs an application and a few supporting documents."),
  L("Υπάλληλος", "f", "Θα χρειαστώ το διαβατήριό σας και μια επίσημη μετάφραση της ληξιαρχικής πράξης γέννησης από τη χώρα σας. Αν έχετε και κάποιο παλιότερο έγγραφο με το σωστό επώνυμο, για παράδειγμα ένα σχολικό απολυτήριο, φέρτε το κι αυτό. Θα βοηθήσει.", "I'll need your passport and an official translation of your birth record from your country. If you also have some older document with the correct surname, for example a school leaving certificate, bring that too. It will help."),
  L("Υπάλληλος", "f", "Η διόρθωση γίνεται συνήθως μέσα σε δέκα εργάσιμες μέρες, και μετά βγάζουμε το πιστοποιητικό την ίδια μέρα. Δεχόμαστε κοινό χωρίς ραντεβού από τις οκτώ ως τις δύο, εκτός από την Τετάρτη. Ευχαριστώ.", "The correction usually takes ten working days, and then we issue the certificate the same day. We see the public without an appointment from eight to two, except on Wednesdays. Thank you."),
 ],
 "questions": [
  Q("Τι λάθος βρήκε η υπάλληλος;", ["Λάθος ημερομηνία γέννησης", "Ένα λάθος γράμμα στο επώνυμο", "Λάθος όνομα πατέρα", "Λάθος διεύθυνση"], 1, "το επώνυμό σας είναι γραμμένο με ένα λάθος γράμμα"),
  Q("Γιατί προτείνει να γίνει πρώτα η διόρθωση;", ["Γιατί αλλιώς θα πληρώσει πρόστιμο", "Γιατί το πιστοποιητικό δεν θα ταιριάζει με το διαβατήριο και μάλλον θα επιστραφεί", "Γιατί το ζήτησε ο δήμαρχος", "Γιατί έτσι θα βγει πιο γρήγορα το διαβατήριο"], 1, "μάλλον θα σας το επιστρέψουν από την υπηρεσία, γιατί δεν θα ταιριάζει με το διαβατήριό σας"),
  Q("Ποιο έγγραφο είναι προαιρετικό αλλά χρήσιμο;", ["Το διαβατήριο", "Ένα παλιότερο έγγραφο με το σωστό επώνυμο", "Η μετάφραση της πράξης γέννησης", "Ένας λογαριασμός ρεύματος"], 1, "Αν έχετε και κάποιο παλιότερο έγγραφο με το σωστό επώνυμο … φέρτε το κι αυτό"),
  Q("Πότε δεν δέχεται κοινό το ληξιαρχείο;", ["Τη Δευτέρα", "Την Τετάρτη", "Την Παρασκευή", "Τα πρωινά"], 1, "από τις οκτώ ως τις δύο, εκτός από την Τετάρτη"),
 ],
 "gloss": {"ληξιαρχείο": "ληξιαρχείο — registry office", "επώνυμό": "επώνυμο — surname", "πιστοποιητικό": "πιστοποιητικό — certificate", "ιθαγένειας": "ιθαγένεια — citizenship", "ληξιαρχική πράξη": "ληξιαρχική πράξη — civil registry record (birth, marriage, death)", "διόρθωση": "διόρθωση — correction", "δικαιολογητικά": "δικαιολογητικά — supporting documents", "μετάφραση": "μετάφραση — translation", "απολυτήριο": "απολυτήριο — school leaving certificate", "εργάσιμες": "εργάσιμος — working (day)", "κοινό": "κοινό — the public"},
})

ITEMS.append({
 "id": "l245-c1-mono-spirto", "title": "Μια μικρή φλόγα με μεγάλη ιστορία: πώς γεννήθηκε το σπίρτο", "title_en": "A small flame with a long history: how the match was born", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν ιστορικό σε μια ραδιοφωνική εκπομπή για τα αντικείμενα της καθημερινής ζωής.",
 "script": [
  L("Ιστορικός", "f", "Για χιλιάδες χρόνια, το να ανάψεις φωτιά ήταν κουραστική υπόθεση. Χρειαζόσουν πυρόλιθο, ένα κομμάτι ατσάλι και λίγο ξερό υλικό, και ήλπιζες να πιάσει η σπίθα. Το σπίρτο που ανάβει με τριβή εμφανίστηκε μόλις το 1826, όταν ένας Άγγλος φαρμακοποιός, ο Τζον Γουόκερ, πρόσεξε ότι ένα ξυλάκι με χημικό μείγμα πήρε φωτιά όταν το έξυσε στο πάτωμα.", "For thousands of years, lighting a fire was a tiring business. You needed flint, a piece of steel and some dry material, and you hoped the spark would catch. The friction match appeared only in 1826, when an English pharmacist, John Walker, noticed that a stick with a chemical mixture caught fire when he scraped it on the floor."),
  L("Ιστορικός", "f", "Λίγα χρόνια αργότερα, οι κατασκευαστές άρχισαν να χρησιμοποιούν λευκό φώσφορο, που άναβε πολύ εύκολα, σχεδόν πάνω σε οποιαδήποτε επιφάνεια. Το τίμημα όμως ήταν τρομερό. Οι εργάτριες των εργοστασίων, συχνά νεαρά κορίτσια, εισέπνεαν τους ατμούς του φωσφόρου και πολλές έπαθαν μια φρικτή ασθένεια, που κατέστρεφε τα κόκαλα του σαγονιού.", "A few years later, manufacturers began to use white phosphorus, which lit very easily, on almost any surface. The price, however, was terrible. The women working in the factories, often young girls, breathed in the phosphorus fumes and many suffered a horrific disease that destroyed the bones of the jaw."),
  L("Ιστορικός", "f", "Η λύση ήρθε από τη Σουηδία, στα μέσα του 19ου αιώνα, με το λεγόμενο «σπίρτο ασφαλείας». Η έξυπνη ιδέα ήταν να χωριστούν τα συστατικά: το κεφάλι του σπίρτου δεν περιέχει φώσφορο, και ο ακίνδυνος κόκκινος φώσφορος βρίσκεται στην τραχιά επιφάνεια του κουτιού. Το σπίρτο ανάβει μόνο όταν συναντηθούν τα δύο.", "The solution came from Sweden, in the middle of the 19th century, with the so-called 'safety match'. The clever idea was to separate the ingredients: the match head contains no phosphorus, and the harmless red phosphorus is on the rough surface of the box. The match lights only when the two meet."),
  L("Ιστορικός", "f", "Το 1888 οι εργάτριες ενός μεγάλου εργοστασίου σπίρτων στο Λονδίνο κατέβηκαν σε απεργία για τους μισθούς και τις συνθήκες εργασίας, και η υπόθεσή τους συγκίνησε την κοινή γνώμη. Χρειάστηκαν όμως ακόμη αρκετά χρόνια, ώσπου ο λευκός φώσφορος να απαγορευτεί στα σπίρτα σε όλη σχεδόν την Ευρώπη.", "In 1888 the women workers of a large match factory in London went on strike over wages and working conditions, and their cause moved public opinion. But it took several more years before white phosphorus was banned in matches across almost all of Europe."),
 ],
 "questions": [
  Q("Πώς ανακάλυψε ο Τζον Γουόκερ το σπίρτο;", ["Μελετώντας αρχαία κείμενα", "Ένα ξυλάκι με χημικό μείγμα πήρε φωτιά όταν το έξυσε στο πάτωμα", "Με πυρόλιθο και ατσάλι", "Σε ένα εργοστάσιο της Σουηδίας"], 1, "ένα ξυλάκι με χημικό μείγμα πήρε φωτιά όταν το έξυσε στο πάτωμα"),
  Q("Ποιο ήταν το τίμημα του λευκού φωσφόρου;", ["Τα σπίρτα ήταν πολύ ακριβά", "Οι εργάτριες αρρώσταιναν από τους ατμούς του", "Τα σπίρτα δεν άναβαν εύκολα", "Τα κουτιά έπαιρναν φωτιά"], 1, "εισέπνεαν τους ατμούς του φωσφόρου και πολλές έπαθαν μια φρικτή ασθένεια"),
  Q("Ποια ήταν η έξυπνη ιδέα του σπίρτου ασφαλείας;", ["Να γίνει το ξυλάκι πιο χοντρό", "Να χωριστούν τα συστατικά ανάμεσα στο κεφάλι και στο κουτί", "Να προστεθεί περισσότερος λευκός φώσφορος", "Να ανάβει μόνο σε υγρό καιρό"], 1, "Η έξυπνη ιδέα ήταν να χωριστούν τα συστατικά"),
  Q("Τι έγινε το 1888 στο Λονδίνο;", ["Απαγορεύτηκε ο λευκός φώσφορος", "Οι εργάτριες ενός εργοστασίου σπίρτων κατέβηκαν σε απεργία", "Ανακαλύφθηκε ο κόκκινος φώσφορος", "Έκλεισαν όλα τα εργοστάσια σπίρτων"], 1, "οι εργάτριες ενός μεγάλου εργοστασίου σπίρτων στο Λονδίνο κατέβηκαν σε απεργία"),
 ],
 "gloss": {"σπίρτο": "σπίρτο — match", "πυρόλιθο": "πυρόλιθος — flint", "ατσάλι": "ατσάλι — steel", "σπίθα": "σπίθα — spark", "τριβή": "τριβή — friction", "φαρμακοποιός": "φαρμακοποιός — pharmacist", "έξυσε": "ξύνω — to scrape, scratch", "φώσφορο": "φώσφορος — phosphorus", "τίμημα": "τίμημα — price, cost (figurative)", "εισέπνεαν": "εισπνέω — to inhale", "σαγονιού": "σαγόνι — jaw", "συστατικά": "συστατικό — ingredient, component", "τραχιά": "τραχύς — rough", "απεργία": "απεργία — strike"},
})

ITEMS.append({
 "id": "l245-c1-int-limnologos", "title": "Ένας λιμνολόγος για τις λίμνες, που «αναπνέουν» δύο φορές τον χρόνο", "title_en": "A limnologist on lakes, which 'breathe' twice a year", "type": "interview", "level": "C1",
 "context_el": "Ένας λιμνολόγος, δηλαδή ένας επιστήμονας που μελετά τις λίμνες και τα εσωτερικά νερά, μιλά σε μια ραδιοφωνική εκπομπή για το περιβάλλον.",
 "script": [
  L("Δημοσιογράφος", "f", "Για τους περισσότερους από εμάς μια λίμνη είναι απλώς ένα ήσυχο νερό. Τι συμβαίνει κάτω από την επιφάνεια;", "For most of us a lake is simply still water. What happens beneath the surface?"),
  L("Λιμνολόγος", "m", "Πολλά περισσότερα απ' όσα φαίνονται. Το καλοκαίρι, στις βαθιές λίμνες, το νερό χωρίζεται σε στρώματα: πάνω ένα ζεστό, ελαφρύ στρώμα και κάτω ένα κρύο και βαρύ, που σχεδόν δεν ανακατεύονται. Έτσι το οξυγόνο από τον αέρα δεν φτάνει στον βυθό, και εκεί κάτω τα ζωντανά πλάσματα δυσκολεύονται.", "Much more than meets the eye. In summer, in deep lakes, the water separates into layers: a warm, light layer on top and a cold, heavy one below, which hardly mix. So the oxygen from the air doesn't reach the bottom, and down there living creatures struggle."),
  L("Δημοσιογράφος", "f", "Και πότε αλλάζει αυτό;", "And when does that change?"),
  L("Λιμνολόγος", "m", "Το φθινόπωρο. Όταν κρυώνει ο αέρας, το επιφανειακό νερό ψύχεται, γίνεται βαρύτερο και βυθίζεται. Τότε όλη η λίμνη ανακατεύεται και το οξυγόνο φτάνει ως τον πάτο. Λέμε συχνά ότι η λίμνη «αναπνέει». Σε λίμνες ψυχρών περιοχών αυτό γίνεται δύο φορές τον χρόνο, την άνοιξη και το φθινόπωρο.", "In autumn. When the air cools, the surface water cools down, becomes heavier and sinks. Then the whole lake mixes and oxygen reaches the bottom. We often say the lake 'breathes'. In lakes in cold regions this happens twice a year, in spring and autumn."),
  L("Δημοσιογράφος", "f", "Ποιος είναι σήμερα ο μεγαλύτερος κίνδυνος για τις λίμνες μας;", "What is the greatest danger for our lakes today?"),
  L("Λιμνολόγος", "m", "Τα λιπάσματα και τα λύματα που καταλήγουν σε αυτές. Τρέφουν τα φύκια, που πολλαπλασιάζονται υπερβολικά και κάνουν το νερό πράσινο και θολό. Όταν πεθαίνουν και σαπίζουν, καταναλώνουν το οξυγόνο, και μπορεί να πεθάνουν τα ψάρια. Η ζέστη επιδεινώνει το πρόβλημα, γιατί τα ζεστά καλοκαίρια κάνουν τα στρώματα ακόμη πιο σταθερά. Οι λίμνες είναι από τα πρώτα μέρη όπου φαίνεται η αλλαγή του κλίματος.", "The fertilisers and sewage that end up in them. They feed the algae, which multiply excessively and make the water green and cloudy. When they die and rot, they use up the oxygen, and the fish may die. Heat makes the problem worse, because hot summers make the layers even more stable. Lakes are among the first places where climate change shows."),
 ],
 "questions": [
  Q("Τι συμβαίνει το καλοκαίρι στις βαθιές λίμνες;", ["Το νερό ανακατεύεται συνεχώς", "Το νερό χωρίζεται σε ένα ζεστό στρώμα πάνω και ένα κρύο κάτω", "Η λίμνη παγώνει", "Ο βυθός γεμίζει οξυγόνο"], 1, "το νερό χωρίζεται σε στρώματα: πάνω ένα ζεστό, ελαφρύ στρώμα και κάτω ένα κρύο και βαρύ"),
  Q("Γιατί ανακατεύεται η λίμνη το φθινόπωρο;", ["Γιατί φυσούν δυνατοί άνεμοι", "Γιατί το επιφανειακό νερό ψύχεται, γίνεται βαρύτερο και βυθίζεται", "Γιατί πέφτουν τα φύλλα των δέντρων", "Γιατί αυξάνονται τα ψάρια"], 1, "το επιφανειακό νερό ψύχεται, γίνεται βαρύτερο και βυθίζεται"),
  Q("Πώς βλάπτουν τα λιπάσματα και τα λύματα τις λίμνες;", ["Δηλητηριάζουν απευθείας τα ψάρια", "Τρέφουν τα φύκια, που όταν σαπίζουν καταναλώνουν το οξυγόνο", "Κάνουν το νερό πολύ κρύο", "Ρίχνουν τη στάθμη του νερού"], 1, "Τρέφουν τα φύκια … Όταν πεθαίνουν και σαπίζουν, καταναλώνουν το οξυγόνο"),
  Q("Γιατί η ζέστη επιδεινώνει το πρόβλημα;", ["Γιατί εξατμίζει όλο το νερό", "Γιατί κάνει τα στρώματα του νερού ακόμη πιο σταθερά", "Γιατί σκοτώνει τα φύκια", "Γιατί φέρνει περισσότερους λουόμενους"], 1, "τα ζεστά καλοκαίρια κάνουν τα στρώματα ακόμη πιο σταθερά"),
 ],
 "gloss": {"λιμνολόγος": "λιμνολόγος — limnologist", "στρώματα": "στρώμα — layer", "ανακατεύονται": "ανακατεύομαι — to mix", "βυθό": "βυθός — bottom (of sea, lake)", "πλάσματα": "πλάσμα — creature", "ψύχεται": "ψύχομαι — to cool down", "βυθίζεται": "βυθίζομαι — to sink", "λιπάσματα": "λίπασμα — fertiliser", "λύματα": "λύματα — sewage", "φύκια": "φύκι — alga, seaweed", "πολλαπλασιάζονται": "πολλαπλασιάζομαι — to multiply", "θολό": "θολός — cloudy, murky", "σαπίζουν": "σαπίζω — to rot", "επιδεινώνει": "επιδεινώνω — to worsen"},
})
rnd = random.Random(245)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-245.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
