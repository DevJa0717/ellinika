# Source for library/listening/listening-42.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l42.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l42-ann-plimmyra", "title": "Προειδοποίηση για πλημμύρες", "title_en": "A flood warning", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια έκτακτη ανακοίνωση στο ραδιόφωνο από την Πολιτική Προστασία.",
 "script": [
  L("Εκφωνητής", "m", "Έκτακτη ανακοίνωση της Πολιτικής Προστασίας. Λόγω των ισχυρών βροχοπτώσεων που αναμένονται από απόψε το βράδυ έως το μεσημέρι της Πέμπτης, κηρύσσεται κατάσταση αυξημένης ετοιμότητας στη Θεσσαλία και στην Κεντρική Μακεδονία. Τα σχολεία των περιοχών αυτών θα παραμείνουν κλειστά αύριο.", "Emergency announcement from Civil Protection. Because of the heavy rainfall expected from this evening until Thursday midday, a state of heightened alert is declared in Thessaly and Central Macedonia. Schools in these areas will remain closed tomorrow."),
  L("Εκφωνητής", "m", "Οι πολίτες καλούνται να αποφεύγουν τις μετακινήσεις, εκτός αν είναι απολύτως απαραίτητες, και να μην περνούν με το αυτοκίνητο ή με τα πόδια από χείμαρρους και πλημμυρισμένους δρόμους. Όσοι μένουν σε ισόγεια ή υπόγεια κοντά σε ποτάμια καλό είναι να μεταφέρουν τα πολύτιμα αντικείμενα και τα έγγραφά τους σε ψηλότερο σημείο.", "Citizens are asked to avoid travel unless absolutely necessary, and not to cross streams or flooded roads by car or on foot. Those living on ground floors or in basements near rivers would do well to move their valuables and documents to a higher place."),
  L("Εκφωνητής", "m", "Αν λάβετε μήνυμα από τον αριθμό έκτακτης ανάγκης εκατόν δώδεκα με οδηγία εκκένωσης, ακολουθήστε το χωρίς καθυστέρηση. Μην μπαίνετε σε υπόγειους χώρους, όπως γκαράζ, για να μετακινήσετε αυτοκίνητα. Για ενημέρωση, ακούτε τους τοπικούς ραδιοφωνικούς σταθμούς.", "If you receive a message from the emergency number one-one-two with an evacuation order, follow it without delay. Do not go into underground spaces, such as garages, to move cars. For updates, listen to local radio stations."),
 ],
 "questions": [
  Q("Τι θα γίνει με τα σχολεία των περιοχών αυτών;", ["Θα κλείσουν νωρίτερα", "Θα παραμείνουν κλειστά αύριο", "Θα λειτουργήσουν κανονικά", "Θα γίνουν χώροι φιλοξενίας"], 1, "Τα σχολεία των περιοχών αυτών θα παραμείνουν κλειστά αύριο"),
  Q("Τι συμβουλεύει η ανακοίνωση όσους μένουν σε ισόγεια κοντά σε ποτάμια;", ["Να φύγουν αμέσως από την περιοχή", "Να μεταφέρουν πολύτιμα αντικείμενα και έγγραφα σε ψηλότερο σημείο", "Να κλείσουν το ρεύμα", "Να τηλεφωνήσουν στο εκατόν δώδεκα"], 1, "καλό είναι να μεταφέρουν τα πολύτιμα αντικείμενα και τα έγγραφά τους σε ψηλότερο σημείο"),
  Q("Τι ΔΕΝ πρέπει να κάνουν οι πολίτες;", ["Να ακούν τους τοπικούς σταθμούς", "Να μπαίνουν σε υπόγεια γκαράζ για να μετακινήσουν αυτοκίνητα", "Να ακολουθούν οδηγίες εκκένωσης", "Να μένουν στο σπίτι"], 1, "Μην μπαίνετε σε υπόγειους χώρους, όπως γκαράζ, για να μετακινήσετε αυτοκίνητα"),
 ],
 "gloss": {"Πολιτική Προστασία": "Πολιτική Προστασία — Civil Protection", "βροχοπτώσεων": "βροχόπτωση — rainfall", "κηρύσσεται": "κηρύσσομαι — to be declared", "αυξημένης ετοιμότητας": "αυξημένη ετοιμότητα — heightened alert", "μετακινήσεις": "μετακίνηση — travel, movement", "χείμαρρους": "χείμαρρος — torrent, stream", "πλημμυρισμένους": "πλημμυρισμένος — flooded", "έγγραφά": "έγγραφο — document", "έκτακτης ανάγκης": "έκτακτη ανάγκη — emergency", "εκκένωσης": "εκκένωση — evacuation"},
})

ITEMS.append({
 "id": "l42-vm-gymnastirio", "title": "Μήνυμα από το γυμναστήριο", "title_en": "A message from the gym", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα από το γυμναστήριο της γειτονιάς σας στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "m", "Γεια σας, κύριε Ζαχαρίου, από το γυμναστήριο «Κίνηση» σας παίρνω. Σας ενημερώνω ότι η συνδρομή σας λήγει στο τέλος του μήνα. Αν την ανανεώσετε για έναν χρόνο μέχρι την Παρασκευή, θα έχετε δύο μήνες δώρο και δωρεάν πρόγραμμα με προσωπικό γυμναστή για τον πρώτο μήνα.", "Hello, Mr Zachariou, I'm calling from the \"Kinisi\" gym. I'm letting you know that your membership expires at the end of the month. If you renew it for a year by Friday, you'll get two months free and a free programme with a personal trainer for the first month."),
  L("Υπάλληλος", "m", "Επίσης, από τη Δευτέρα αλλάζει το πρόγραμμα των ομαδικών μαθημάτων. Το πιλάτες που παρακολουθείτε την Τρίτη στις επτά μεταφέρεται στις οχτώ, γιατί στις επτά θα γίνεται ένα νέο μάθημα για άτομα άνω των εξήντα. Η πισίνα θα είναι κλειστή για συντήρηση την πρώτη εβδομάδα του μήνα.", "Also, from Monday the schedule of group classes is changing. The Pilates class you attend on Tuesdays at seven is moving to eight, because at seven there will be a new class for people over sixty. The pool will be closed for maintenance during the first week of the month."),
  L("Υπάλληλος", "m", "Και κάτι τελευταίο: ξεχάσατε στα αποδυτήρια ένα μπλε μπουφάν και τα γυαλιά σας. Τα έχουμε φυλάξει στη ρεσεψιόν. Περάστε όποτε σας βολεύει. Καλή σας μέρα.", "And one last thing: you left a blue jacket and your glasses in the changing room. We've kept them at reception. Drop by whenever suits you. Have a good day."),
 ],
 "questions": [
  Q("Τι προσφορά υπάρχει για την ανανέωση της συνδρομής;", ["Έκπτωση πενήντα τοις εκατό", "Δύο μήνες δώρο και δωρεάν προσωπικό γυμναστή τον πρώτο μήνα", "Δωρεάν πισίνα για έναν χρόνο", "Ένα δώρο από το κατάστημα"], 1, "θα έχετε δύο μήνες δώρο και δωρεάν πρόγραμμα με προσωπικό γυμναστή"),
  Q("Γιατί αλλάζει η ώρα του πιλάτες;", ["Επειδή έφυγε η γυμνάστρια", "Επειδή στις επτά θα γίνεται νέο μάθημα για άτομα άνω των εξήντα", "Επειδή η αίθουσα επισκευάζεται", "Επειδή λίγοι το παρακολουθούσαν"], 1, "στις επτά θα γίνεται ένα νέο μάθημα για άτομα άνω των εξήντα"),
  Q("Τι ξέχασε ο κύριος Ζαχαρίου;", ["Το κινητό του", "Ένα μπουφάν και τα γυαλιά του", "Την κάρτα μέλους", "Την τσάντα του"], 1, "ξεχάσατε στα αποδυτήρια ένα μπλε μπουφάν και τα γυαλιά σας"),
 ],
 "gloss": {"γυμναστήριο": "γυμναστήριο — gym", "συνδρομή": "συνδρομή — membership", "λήγει": "λήγω — to expire", "την ανανεώσετε": "ανανεώνω — to renew", "γυμναστή": "γυμναστής — (fitness) trainer", "ομαδικών": "ομαδικός — group (adj.)", "παρακολουθείτε": "παρακολουθώ — to attend", "πισίνα": "πισίνα — swimming pool", "συντήρηση": "συντήρηση — maintenance", "αποδυτήρια": "αποδυτήρια — changing room"},
})

ITEMS.append({
 "id": "l42-dia-fotovoltaika", "title": "Φωτοβολταϊκά στην ταράτσα", "title_en": "Solar panels on the roof", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο ανάμεσα σε μια ιδιοκτήτρια σπιτιού και έναν τεχνικό για την τοποθέτηση φωτοβολταϊκών.",
 "script": [
  L("Ιδιοκτήτρια", "f", "Καλημέρα. Σκεφτόμαστε να βάλουμε φωτοβολταϊκά στην ταράτσα, γιατί ο λογαριασμός του ρεύματος έχει γίνει απλησίαστος. Τι χρειάζεται για να ξεκινήσουμε;", "Good morning. We're thinking of putting solar panels on the roof, because the electricity bill has become unaffordable. What's needed to get started?"),
  L("Τεχνικός", "m", "Πρώτα θα έρθω να δω την ταράτσα: τον προσανατολισμό, αν υπάρχουν σκιές από γύρω κτίρια ή δέντρα, και πόσο χώρο έχετε. Για ένα σπίτι με τέσσερα άτομα, ένα σύστημα πέντε κιλοβάτ συνήθως αρκεί. Επειδή μένετε σε πολυκατοικία, θα χρειαστεί και η συναίνεση των άλλων ιδιοκτητών, αφού η ταράτσα είναι κοινόχρηστη.", "First I'll come and look at the roof: the orientation, whether there are shadows from surrounding buildings or trees, and how much space you have. For a household of four, a five-kilowatt system is usually enough. Because you live in a block of flats, you'll also need the consent of the other owners, since the roof is shared."),
  L("Ιδιοκτήτρια", "f", "Και πόσο κοστίζει; Και σε πόσα χρόνια θα αποσβεστεί;", "And how much does it cost? And how many years before it pays for itself?"),
  L("Τεχνικός", "m", "Υπολογίστε γύρω στις έξι με επτά χιλιάδες ευρώ με την τοποθέτηση. Συνήθως υπάρχουν και επιδοτήσεις, που καλύπτουν ένα μέρος του κόστους, αλλά οι όροι αλλάζουν κάθε χρόνο, οπότε πρέπει να το ελέγξουμε. Με τον ήλιο που έχουμε εδώ, η απόσβεση είναι συνήθως πέντε με επτά χρόνια, και τα πάνελ κρατάνε πάνω από είκοσι πέντε.", "Reckon on around six to seven thousand euros including installation. There are usually subsidies too, which cover part of the cost, but the conditions change every year, so we need to check. With the sun we have here, the payback period is usually five to seven years, and the panels last more than twenty-five."),
 ],
 "questions": [
  Q("Γιατί σκέφτεται η ιδιοκτήτρια να βάλει φωτοβολταϊκά;", ["Για να πουλήσει ρεύμα", "Επειδή ο λογαριασμός του ρεύματος έχει γίνει πολύ ακριβός", "Επειδή το απαιτεί ο νόμος", "Επειδή το έκαναν οι γείτονες"], 1, "ο λογαριασμός του ρεύματος έχει γίνει απλησίαστος"),
  Q("Γιατί χρειάζεται η συναίνεση των άλλων ιδιοκτητών;", ["Επειδή θα πληρώσουν κι εκείνοι", "Επειδή η ταράτσα είναι κοινόχρηστη", "Επειδή θα κοπούν δέντρα", "Επειδή θα κλείσει ο δρόμος"], 1, "αφού η ταράτσα είναι κοινόχρηστη"),
  Q("Σε πόσα χρόνια αποσβένεται συνήθως η επένδυση;", ["Σε έναν με δύο", "Σε πέντε με επτά", "Σε είκοσι πέντε", "Δεν αποσβένεται ποτέ"], 1, "η απόσβεση είναι συνήθως πέντε με επτά χρόνια"),
 ],
 "gloss": {"φωτοβολταϊκά": "φωτοβολταϊκά — solar (photovoltaic) panels", "απλησίαστος": "απλησίαστος — unaffordable, sky-high", "προσανατολισμό": "προσανατολισμός — orientation", "κιλοβάτ": "κιλοβάτ — kilowatt", "συναίνεση": "συναίνεση — consent", "κοινόχρηστη": "κοινόχρηστος — shared, communal", "θα αποσβεστεί": "αποσβένομαι — to pay for itself", "επιδοτήσεις": "επιδότηση — subsidy", "όροι": "όρος — condition, term", "απόσβεση": "απόσβεση — payback"},
})

ITEMS.append({
 "id": "l42-dia-lista-gamou", "title": "Δώρο για έναν γάμο", "title_en": "A wedding present", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε δύο φίλους που συζητούν τι δώρο θα κάνουν σε έναν κοινό τους φίλο που παντρεύεται.",
 "script": [
  L("Νίκος", "m", "Ο Άγγελος και η Δανάη έστειλαν τα προσκλητήρια. Ο γάμος είναι στη Σαντορίνη, τον Σεπτέμβριο. Τι λες, να τους πάρουμε κάτι μαζί;", "Angelos and Danai have sent the invitations. The wedding is on Santorini, in September. What do you think, shall we get them something together?"),
  L("Μαρίνα", "f", "Ναι, καλή ιδέα. Έχουν κάνει λίστα γάμου σε ένα κατάστημα με είδη σπιτιού, αλλά τα περισσότερα πράγματα είναι ήδη κρατημένα. Έμειναν μόνο κάτι πανάκριβα μαχαιροπίρουνα και μια φρυγανιέρα.", "Yes, good idea. They've made a wedding list at a homeware shop, but most things are already reserved. All that's left is some outrageously expensive cutlery and a toaster."),
  L("Νίκος", "m", "Η φρυγανιέρα μού φαίνεται λίγο φτωχή για γάμο. Μου είπε ο Άγγελος ότι μαζεύουν χρήματα για το ταξίδι του μέλιτος στην Ιαπωνία. Ίσως είναι πιο χρήσιμο να τους δώσουμε χρήματα, σε μια ωραία κάρτα.", "The toaster seems a bit poor for a wedding. Angelos told me they're saving money for their honeymoon in Japan. Maybe it's more useful to give them money, in a nice card."),
  L("Μαρίνα", "f", "Συμφωνώ, αλλά δεν θέλω να είναι μόνο ένα φάκελος. Ας κάνουμε κάτι πιο προσωπικό: να πληρώσουμε, ας πούμε, μια βραδιά σε ένα παραδοσιακό ιαπωνικό πανδοχείο, και να τους φτιάξω κι ένα άλμπουμ με φωτογραφίες από τα φοιτητικά μας χρόνια. Θα γελάσουν πολύ.", "I agree, but I don't want it to be just an envelope. Let's do something more personal: pay for, say, a night at a traditional Japanese inn, and I'll make them an album with photos from our student years too. They'll laugh a lot."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με τη λίστα γάμου;", ["Είναι σε κατάστημα της Σαντορίνης", "Τα περισσότερα πράγματα είναι ήδη κρατημένα", "Δεν έχει καθόλου είδη σπιτιού", "Είναι πολύ φθηνή"], 1, "τα περισσότερα πράγματα είναι ήδη κρατημένα"),
  Q("Για τι μαζεύει χρήματα το ζευγάρι;", ["Για καινούργιο σπίτι", "Για το ταξίδι του μέλιτος στην Ιαπωνία", "Για αυτοκίνητο", "Για τη δεξίωση"], 1, "μαζεύουν χρήματα για το ταξίδι του μέλιτος στην Ιαπωνία"),
  Q("Τι προτείνει τελικά η Μαρίνα;", ["Να πάρουν τη φρυγανιέρα", "Να πληρώσουν μια βραδιά σε ιαπωνικό πανδοχείο και να φτιάξει ένα άλμπουμ φωτογραφιών", "Να δώσουν μόνο χρήματα σε φάκελο", "Να μην πάνε στον γάμο"], 1, "να πληρώσουμε… μια βραδιά σε ένα παραδοσιακό ιαπωνικό πανδοχείο, και να τους φτιάξω κι ένα άλμπουμ"),
 ],
 "gloss": {"προσκλητήρια": "προσκλητήριο — (wedding) invitation", "λίστα γάμου": "λίστα γάμου — wedding list", "είδη σπιτιού": "είδη σπιτιού — homeware", "κρατημένα": "κρατημένος — reserved", "πανάκριβα": "πανάκριβος — extremely expensive", "μαχαιροπίρουνα": "μαχαιροπίρουνα — cutlery", "φρυγανιέρα": "φρυγανιέρα — toaster", "ταξίδι του μέλιτος": "ταξίδι του μέλιτος — honeymoon", "φάκελος": "φάκελος — envelope", "πανδοχείο": "πανδοχείο — inn"},
})

ITEMS.append({
 "id": "l42-mono-erasmus", "title": "Ένα εξάμηνο στη Θεσσαλονίκη", "title_en": "A semester in Thessaloniki", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια Ισπανίδα φοιτήτρια να μιλάει για το εξάμηνο που πέρασε στη Θεσσαλονίκη με το πρόγραμμα Erasmus.",
 "script": [
  L("Λουθία", "f", "Όταν διάλεξα τη Θεσσαλονίκη για το Erasmus, οι φίλοι μου στη Βαλένθια με ρώτησαν αν είμαι τρελή, γιατί δεν ήξερα ούτε μία λέξη ελληνικά. Τις πρώτες εβδομάδες ήταν πράγματι δύσκολα: δεν μπορούσα να διαβάσω ούτε τις πινακίδες των λεωφορείων, και στο σούπερ μάρκετ αγόραζα πράγματα από τη φωτογραφία στη συσκευασία.", "When I chose Thessaloniki for Erasmus, my friends in Valencia asked me if I was crazy, because I didn't know a single word of Greek. The first weeks were indeed difficult: I couldn't even read the bus signs, and in the supermarket I bought things from the photo on the packaging."),
  L("Λουθία", "f", "Το πανεπιστήμιο οργάνωνε δωρεάν μαθήματα ελληνικών για ξένους φοιτητές, και η δασκάλα μας μάς έβαζε να παραγγέλνουμε στα ελληνικά στις καφετέριες. Οι σερβιτόροι, βέβαια, μου απαντούσαν αμέσως στα αγγλικά, μόλις άκουγαν την προφορά μου. Χρειάστηκε να επιμείνω πολύ.", "The university organised free Greek classes for foreign students, and our teacher made us order in Greek in cafés. The waiters, of course, answered me in English immediately as soon as they heard my accent. I had to insist a lot."),
  L("Λουθία", "f", "Αυτό που θα μου λείψει περισσότερο είναι η ζωή στον δρόμο. Στη Θεσσαλονίκη οι άνθρωποι βγαίνουν, περπατούν στην παραλία, κάθονται για ώρες με έναν καφέ. Γύρισα στην Ισπανία με ένα βασικό επίπεδο ελληνικών, πολλούς φίλους και μια απόφαση: να κάνω το μεταπτυχιακό μου εδώ. Και η μητέρα μου ακόμα δεν το έχει χωνέψει.", "What I'll miss most is street life. In Thessaloniki people go out, walk along the seafront, sit for hours over a coffee. I went back to Spain with basic Greek, lots of friends and a decision: to do my master's here. And my mother still hasn't come to terms with it."),
 ],
 "questions": [
  Q("Γιατί οι φίλοι της νόμιζαν ότι η επιλογή της ήταν τρελή;", ["Επειδή η Θεσσαλονίκη είναι ακριβή", "Επειδή δεν ήξερε καθόλου ελληνικά", "Επειδή ήταν πολύ μακριά", "Επειδή δεν υπήρχε πρόγραμμα Erasmus"], 1, "δεν ήξερα ούτε μία λέξη ελληνικά"),
  Q("Ποιο πρόβλημα αντιμετώπιζε στις καφετέριες;", ["Οι τιμές ήταν πολύ υψηλές", "Οι σερβιτόροι της απαντούσαν στα αγγλικά", "Δεν καταλάβαινε το μενού", "Δεν της άρεσε ο καφές"], 1, "Οι σερβιτόροι… μου απαντούσαν αμέσως στα αγγλικά"),
  Q("Τι αποφάσισε η Λουθία;", ["Να μη γυρίσει ποτέ στην Ελλάδα", "Να κάνει το μεταπτυχιακό της στη Θεσσαλονίκη", "Να γίνει δασκάλα ελληνικών", "Να μείνει για πάντα στη Βαλένθια"], 1, "να κάνω το μεταπτυχιακό μου εδώ"),
 ],
 "gloss": {"εξάμηνο": "εξάμηνο — semester", "πινακίδες": "πινακίδα — sign", "συσκευασία": "συσκευασία — packaging", "να παραγγέλνουμε": "παραγγέλνω — to order", "προφορά": "προφορά — accent, pronunciation", "να επιμείνω": "επιμένω — to insist", "θα μου λείψει": "μου λείπει — I miss", "μεταπτυχιακό": "μεταπτυχιακό — master's degree", "δεν το έχει χωνέψει": "χωνεύω — to digest; (fig.) to accept"},
})

ITEMS.append({
 "id": "l42-rep-anemogennitries", "title": "Ανεμογεννήτριες στο βουνό", "title_en": "Wind turbines on the mountain", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τη διαμάχη γύρω από ένα αιολικό πάρκο σε ένα νησί.",
 "script": [
  L("Ρεπόρτερ", "f", "Στις κορυφές της νότιας Εύβοιας, δεκάδες ανεμογεννήτριες γυρίζουν αργά στον αέρα. Η περιοχή είναι από τις πιο ανεμώδεις της χώρας, και γι' αυτό έχει προσελκύσει πολλές εταιρείες αιολικής ενέργειας. Τώρα σχεδιάζεται ένα ακόμα αιολικό πάρκο, και οι κάτοικοι είναι διχασμένοι.", "On the peaks of southern Evia, dozens of wind turbines turn slowly in the wind. The area is among the windiest in the country, and for that reason it has attracted many wind energy companies. Now another wind farm is being planned, and the residents are divided."),
  L("Κάτοικος", "m", "Δεν είμαι κατά της πράσινης ενέργειας. Αλλά για να φτάσουν οι γερανοί εδώ πάνω, άνοιξαν δρόμους μέσα στο δάσος και έκοψαν βουνοπλαγιές. Οι πηγές από όπου έπινε νερό το χωριό στέρεψαν. Και κανείς δεν μας ρώτησε.", "I'm not against green energy. But to get the cranes up here, they opened roads through the forest and cut into mountainsides. The springs the village drank from dried up. And nobody asked us."),
  L("Ρεπόρτερ", "f", "Από την άλλη, ο δήμαρχος υποστηρίζει ότι οι εταιρείες καταβάλλουν στην τοπική κοινωνία ένα ποσοστό από τα έσοδα, με το οποίο έχουν επισκευαστεί σχολεία και δρόμοι. Οι περιβαλλοντικές οργανώσεις ζητούν έναν εθνικό χωροταξικό σχεδιασμό, που θα καθορίζει πού μπορούν να εγκατασταθούν ανεμογεννήτριες, ώστε να προστατεύονται οι περιοχές με μεγάλη φυσική αξία.", "On the other hand, the mayor maintains that the companies pay the local community a percentage of their revenue, with which schools and roads have been repaired. Environmental organisations are calling for national spatial planning that will set out where wind turbines can be installed, so that areas of high natural value are protected."),
 ],
 "questions": [
  Q("Γιατί η περιοχή έχει προσελκύσει εταιρείες αιολικής ενέργειας;", ["Επειδή είναι κοντά στην Αθήνα", "Επειδή είναι από τις πιο ανεμώδεις της χώρας", "Επειδή η γη είναι φθηνή", "Επειδή δεν έχει κατοίκους"], 1, "Η περιοχή είναι από τις πιο ανεμώδεις της χώρας"),
  Q("Τι παράπονο έχει ο κάτοικος;", ["Ότι οι ανεμογεννήτριες κάνουν θόρυβο", "Ότι άνοιξαν δρόμους στο δάσος, στέρεψαν οι πηγές και κανείς δεν ρώτησε το χωριό", "Ότι το ρεύμα έγινε ακριβότερο", "Ότι δεν βρήκε δουλειά στην εταιρεία"], 1, "άνοιξαν δρόμους μέσα στο δάσος… Οι πηγές… στέρεψαν. Και κανείς δεν μας ρώτησε"),
  Q("Τι ζητούν οι περιβαλλοντικές οργανώσεις;", ["Να καταργηθούν όλες οι ανεμογεννήτριες", "Έναν εθνικό χωροταξικό σχεδιασμό για το πού μπορούν να εγκατασταθούν", "Περισσότερα χρήματα για τους δήμους", "Να γίνουν μόνο υπεράκτια πάρκα"], 1, "ζητούν έναν εθνικό χωροταξικό σχεδιασμό"),
 ],
 "gloss": {"διαμάχη": "διαμάχη — dispute", "αιολικό πάρκο": "αιολικό πάρκο — wind farm", "ανεμογεννήτριες": "ανεμογεννήτρια — wind turbine", "ανεμώδεις": "ανεμώδης — windy", "διχασμένοι": "διχασμένος — divided", "γερανοί": "γερανός — crane", "βουνοπλαγιές": "βουνοπλαγιά — mountainside", "στέρεψαν": "στερεύω — to dry up", "καταβάλλουν": "καταβάλλω — to pay", "χωροταξικό": "χωροταξικός — spatial (planning)", "να εγκατασταθούν": "εγκαθίσταμαι — to be installed"},
})

ITEMS.append({
 "id": "l42-rep-dorea-organon", "title": "Ένα δώρο ζωής", "title_en": "A gift of life", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ για τη δωρεά οργάνων στην Ελλάδα.",
 "script": [
  L("Ρεπόρτερ", "m", "Η Αφροδίτη είναι τριάντα τεσσάρων χρονών και πριν από δύο χρόνια έκανε μεταμόσχευση νεφρού. «Επί τέσσερα χρόνια έκανα αιμοκάθαρση τρεις φορές την εβδομάδα, τέσσερις ώρες κάθε φορά», λέει. «Δεν μπορούσα να δουλέψω, ούτε να ταξιδέψω. Ένας άγνωστος άνθρωπος μού έδωσε πίσω τη ζωή μου.»", "Afroditi is thirty-four, and two years ago she had a kidney transplant. \"For four years I was on dialysis three times a week, four hours each time,\" she says. \"I couldn't work or travel. An unknown person gave me my life back.\""),
  L("Ρεπόρτερ", "m", "Η Ελλάδα, ωστόσο, παραμένει πίσω από τις περισσότερες ευρωπαϊκές χώρες στις δωρεές οργάνων, και χιλιάδες ασθενείς βρίσκονται σε λίστα αναμονής. Σύμφωνα με τον νόμο, κάθε ενήλικας θεωρείται δωρητής, εκτός αν έχει δηλώσει το αντίθετο. Στην πράξη, όμως, οι γιατροί ζητούν πάντα τη συγκατάθεση της οικογένειας, και πολλές οικογένειες αρνούνται.", "Greece, however, remains behind most European countries in organ donation, and thousands of patients are on a waiting list. Under the law, every adult is considered a donor unless they have stated otherwise. In practice, though, doctors always ask for the family's consent, and many families refuse."),
  L("Ρεπόρτερ", "m", "Οι ειδικοί λένε ότι το σημαντικότερο είναι να συζητάμε το θέμα με τους δικούς μας όσο είμαστε υγιείς. «Όταν η οικογένεια ξέρει τι ήθελε ο άνθρωπός της, η απόφαση είναι πιο εύκολη, ακόμα και μέσα στον πόνο», εξηγεί μια συντονίστρια μεταμοσχεύσεων. Η Αφροδίτη έχει γράψει ένα γράμμα ευχαριστίας στην οικογένεια του δότη της, μέσω του νοσοκομείου, αφού τα στοιχεία των δοτών παραμένουν απόρρητα.", "Experts say that the most important thing is to discuss the subject with our loved ones while we are healthy. \"When the family knows what their loved one wanted, the decision is easier, even amid the pain,\" explains a transplant coordinator. Afroditi has written a thank-you letter to her donor's family, through the hospital, since donors' details remain confidential."),
 ],
 "questions": [
  Q("Πώς ήταν η ζωή της Αφροδίτης πριν από τη μεταμόσχευση;", ["Δούλευε κανονικά", "Έκανε αιμοκάθαρση τρεις φορές την εβδομάδα και δεν μπορούσε να δουλέψει", "Ζούσε στο εξωτερικό", "Δεν είχε κανένα πρόβλημα υγείας"], 1, "Επί τέσσερα χρόνια έκανα αιμοκάθαρση τρεις φορές την εβδομάδα"),
  Q("Τι ισχύει στην πράξη για τη δωρεά οργάνων;", ["Οι γιατροί δεν ρωτούν ποτέ την οικογένεια", "Οι γιατροί ζητούν πάντα τη συγκατάθεση της οικογένειας", "Μόνο όσοι έχουν κάρτα δωρητή μπορούν να δώσουν όργανα", "Η δωρεά απαγορεύεται"], 1, "οι γιατροί ζητούν πάντα τη συγκατάθεση της οικογένειας"),
  Q("Τι συμβουλεύουν οι ειδικοί;", ["Να γράψουμε διαθήκη", "Να συζητάμε το θέμα με τους δικούς μας όσο είμαστε υγιείς", "Να γίνουμε όλοι γιατροί", "Να αποφεύγουμε το θέμα"], 1, "να συζητάμε το θέμα με τους δικούς μας όσο είμαστε υγιείς"),
 ],
 "gloss": {"δωρεά": "δωρεά — donation", "οργάνων": "όργανο — organ", "μεταμόσχευση": "μεταμόσχευση — transplant", "νεφρού": "νεφρό — kidney", "αιμοκάθαρση": "αιμοκάθαρση — dialysis", "λίστα αναμονής": "λίστα αναμονής — waiting list", "δωρητής": "δωρητής — donor", "συγκατάθεση": "συγκατάθεση — consent", "συντονίστρια": "συντονίστρια — (female) coordinator", "δότη": "δότης — donor", "απόρρητα": "απόρρητος — confidential"},
})

ITEMS.append({
 "id": "l42-int-vosko", "title": "Ένας νέος βοσκός", "title_en": "A young shepherd", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν νέο κτηνοτρόφο από τα Σφακιά της Κρήτης.",
 "script": [
  L("Δημοσιογράφος", "f", "Είσαι είκοσι οχτώ χρονών και έχεις πτυχίο πληροφορικής. Γιατί έγινες βοσκός;", "You're twenty-eight and you have a degree in computer science. Why did you become a shepherd?"),
  L("Βοσκός", "m", "Δούλεψα τρία χρόνια σε μια εταιρεία στην Αθήνα, μπροστά σε μια οθόνη, δέκα ώρες τη μέρα. Κάθε καλοκαίρι που γύριζα στο χωριό και ανέβαινα με τον πατέρα μου στο μιτάτο, ένιωθα ότι ανέπνεα. Όταν εκείνος είπε ότι θα πουλήσει τα ζώα γιατί δεν αντέχει πια, αποφάσισα να γυρίσω.", "I worked for three years at a company in Athens, in front of a screen, ten hours a day. Every summer when I came back to the village and went up with my father to the mitato, I felt I could breathe. When he said he'd sell the animals because he couldn't cope any more, I decided to come back."),
  L("Δημοσιογράφος", "f", "Οι σπουδές σου σε βοηθάνε καθόλου;", "Do your studies help you at all?"),
  L("Βοσκός", "m", "Πάρα πολύ. Έχω βάλει GPS σε μερικά ζώα, για να ξέρω πού βρίσκεται το κοπάδι στο βουνό, και κρατάω σε υπολογιστή όλα τα στοιχεία για την υγεία και το γάλα τους. Πουλάμε επίσης το τυρί μας απευθείας μέσω διαδικτύου σε πελάτες σε όλη την Ελλάδα, οπότε δεν εξαρτιόμαστε από τους μεσάζοντες.", "Very much. I've put GPS on some animals, so I know where the flock is on the mountain, and I keep all the data on their health and milk on a computer. We also sell our cheese directly online to customers all over Greece, so we don't depend on middlemen."),
  L("Δημοσιογράφος", "f", "Ποια είναι η μεγαλύτερη δυσκολία;", "What's the biggest difficulty?"),
  L("Βοσκός", "m", "Δεν υπάρχει Κυριακή ούτε διακοπές. Τα ζώα θέλουν άρμεγμα δύο φορές τη μέρα, με βροχή, με χιόνι, με γιορτές. Και το κόστος των ζωοτροφών έχει ανέβει πολύ. Αλλά όταν το πρωί βλέπω τον ήλιο να βγαίνει πάνω από το Λιβυκό, δεν το αλλάζω με τίποτα.", "There are no Sundays or holidays. The animals need milking twice a day, in rain, in snow, on holidays. And the cost of animal feed has gone up a lot. But when in the morning I see the sun rise over the Libyan Sea, I wouldn't swap it for anything."),
 ],
 "questions": [
  Q("Τι έκανε πριν γίνει βοσκός;", ["Ήταν φοιτητής γεωπονίας", "Δούλευε σε εταιρεία στην Αθήνα μπροστά σε οθόνη", "Ήταν δάσκαλος", "Δούλευε σε ξενοδοχείο"], 1, "Δούλεψα τρία χρόνια σε μια εταιρεία στην Αθήνα, μπροστά σε μια οθόνη"),
  Q("Πώς χρησιμοποιεί τις γνώσεις πληροφορικής του;", ["Φτιάχνει βιντεοπαιχνίδια", "Βάζει GPS στα ζώα, κρατάει στοιχεία σε υπολογιστή και πουλάει τυρί μέσω διαδικτύου", "Διδάσκει σε παιδιά του χωριού", "Δεν τις χρησιμοποιεί καθόλου"], 1, "Έχω βάλει GPS σε μερικά ζώα… Πουλάμε επίσης το τυρί μας απευθείας μέσω διαδικτύου"),
  Q("Ποια είναι η μεγαλύτερη δυσκολία της δουλειάς;", ["Η μοναξιά", "Δεν υπάρχουν Κυριακές ούτε διακοπές", "Οι λύκοι", "Η έλλειψη νερού"], 1, "Δεν υπάρχει Κυριακή ούτε διακοπές"),
 ],
 "gloss": {"κτηνοτρόφο": "κτηνοτρόφος — livestock farmer", "πτυχίο": "πτυχίο — degree", "πληροφορικής": "πληροφορική — computer science", "μιτάτο": "μιτάτο — mitato (Cretan shepherd's stone hut)", "ανέπνεα": "αναπνέω — to breathe", "κοπάδι": "κοπάδι — flock", "μεσάζοντες": "μεσάζων — middleman", "άρμεγμα": "άρμεγμα — milking", "ζωοτροφών": "ζωοτροφή — animal feed", "Λιβυκό": "Λιβυκό (Πέλαγος) — Libyan Sea"},
})

ITEMS.append({
 "id": "l42-mono-thlimmenes-tainies", "title": "Γιατί μας αρέσουν οι θλιμμένες ιστορίες;", "title_en": "Why do we like sad stories?", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε απόσπασμα από μια ραδιοφωνική εκπομπή για την ψυχολογία της τέχνης.",
 "script": [
  L("Παρουσιάστρια", "f", "Πληρώνουμε εισιτήριο για να δούμε μια ταινία που ξέρουμε ότι θα μας κάνει να κλάψουμε. Διαβάζουμε μυθιστορήματα με τραγικό τέλος, ακούμε ξανά και ξανά τραγούδια για χαμένους έρωτες. Από την εποχή του Αριστοτέλη, που μίλησε για την «κάθαρση» στην τραγωδία, προσπαθούμε να εξηγήσουμε αυτό το φαινομενικό παράδοξο: γιατί επιδιώκουμε συναισθήματα που στην πραγματική ζωή θα αποφεύγαμε;", "We pay for a ticket to see a film we know will make us cry. We read novels with tragic endings, listen again and again to songs about lost loves. Since the time of Aristotle, who spoke of \"catharsis\" in tragedy, we have been trying to explain this apparent paradox: why do we seek out emotions that in real life we would avoid?"),
  L("Παρουσιάστρια", "f", "Μια πρώτη απάντηση είναι ότι η τέχνη μάς προσφέρει ένα ασφαλές πλαίσιο. Ξέρουμε ότι ο πόνος των ηρώων δεν είναι δικός μας και ότι, όταν ανάψουν τα φώτα, θα επιστρέψουμε στη ζωή μας. Μέσα σε αυτό το προστατευμένο περιβάλλον, μπορούμε να εξερευνήσουμε τη θλίψη χωρίς το πραγματικό της κόστος, σαν να κάνουμε μια πρόβα για στιγμές που αργά ή γρήγορα θα έρθουν.", "A first answer is that art offers us a safe frame. We know that the heroes' pain is not ours and that, when the lights come on, we will return to our lives. Within this protected environment, we can explore sadness without its real cost, as if rehearsing for moments that sooner or later will come."),
  L("Παρουσιάστρια", "f", "Οι ψυχολόγοι έχουν προτείνει και άλλες εξηγήσεις. Ορισμένες έρευνες δείχνουν ότι οι συγκινητικές ιστορίες ενισχύουν το αίσθημα σύνδεσης με τους άλλους: μετά από μια θλιμμένη ταινία, οι θεατές δηλώνουν συχνά ότι εκτιμούν περισσότερο τους δικούς τους ανθρώπους. Άλλοι μιλούν για το «νόημα»: οι θλιμμένες ιστορίες μάς ωθούν να σκεφτούμε τι είναι πραγματικά σημαντικό, και αυτή η αναστοχαστική διάθεση βιώνεται ως κάτι πολύτιμο, ακόμα κι αν δεν είναι ευχάριστο.", "Psychologists have proposed other explanations too. Some studies show that moving stories strengthen the feeling of connection with others: after a sad film, viewers often say that they appreciate their own loved ones more. Others speak of \"meaning\": sad stories push us to think about what really matters, and this reflective mood is experienced as something valuable, even if it is not pleasant."),
  L("Παρουσιάστρια", "f", "Δεν απολαμβάνουν, πάντως, όλοι τη θλίψη στην τέχνη στον ίδιο βαθμό. Η προτίμηση αυτή φαίνεται να σχετίζεται με χαρακτηριστικά της προσωπικότητας, όπως η ενσυναίσθηση και η ανοιχτότητα σε νέες εμπειρίες. Ίσως, τελικά, το να κλαίμε μπροστά σε μια οθόνη να μην είναι αδυναμία, αλλά μια από τις πιο ανθρώπινες ικανότητές μας: να νιώθουμε τον πόνο κάποιου που δεν υπήρξε ποτέ.", "Not everyone, however, enjoys sadness in art to the same extent. This preference seems to be related to personality traits, such as empathy and openness to new experiences. Perhaps, in the end, crying in front of a screen is not a weakness, but one of our most human abilities: to feel the pain of someone who never existed."),
 ],
 "questions": [
  Q("Ποιο παράδοξο εξετάζει η εκπομπή;", ["Γιατί οι ταινίες κοστίζουν ακριβά", "Γιατί επιδιώκουμε στην τέχνη συναισθήματα που στη ζωή θα αποφεύγαμε", "Γιατί οι τραγωδίες γράφονταν μόνο στην αρχαιότητα", "Γιατί οι άνθρωποι κλαίνε λιγότερο σήμερα"], 1, "γιατί επιδιώκουμε συναισθήματα που στην πραγματική ζωή θα αποφεύγαμε;"),
  Q("Τι σημαίνει ότι η τέχνη προσφέρει «ασφαλές πλαίσιο»;", ["Ότι οι κινηματογράφοι είναι ασφαλείς", "Ότι εξερευνούμε τη θλίψη χωρίς το πραγματικό της κόστος", "Ότι οι ταινίες έχουν πάντα καλό τέλος", "Ότι δεν νιώθουμε τίποτα"], 1, "μπορούμε να εξερευνήσουμε τη θλίψη χωρίς το πραγματικό της κόστος"),
  Q("Τι δείχνουν ορισμένες έρευνες για τους θεατές θλιμμένων ταινιών;", ["Ότι νιώθουν πιο μόνοι", "Ότι εκτιμούν περισσότερο τους δικούς τους ανθρώπους", "Ότι δεν θέλουν να δουν άλλη ταινία", "Ότι ξεχνούν γρήγορα την υπόθεση"], 1, "οι θεατές δηλώνουν συχνά ότι εκτιμούν περισσότερο τους δικούς τους ανθρώπους"),
  Q("Με τι φαίνεται να σχετίζεται η προτίμηση για θλιμμένες ιστορίες;", ["Με την ηλικία", "Με χαρακτηριστικά της προσωπικότητας, όπως η ενσυναίσθηση", "Με το επάγγελμα", "Με το φύλο"], 1, "φαίνεται να σχετίζεται με χαρακτηριστικά της προσωπικότητας, όπως η ενσυναίσθηση"),
 ],
 "gloss": {"θλιμμένες": "θλιμμένος — sad", "κάθαρση": "κάθαρση — catharsis", "φαινομενικό": "φαινομενικός — apparent", "επιδιώκουμε": "επιδιώκω — to seek, pursue", "πλαίσιο": "πλαίσιο — frame, context", "να εξερευνήσουμε": "εξερευνώ — to explore", "θλίψη": "θλίψη — sadness", "πρόβα": "πρόβα — rehearsal", "μάς ωθούν": "ωθώ — to push, drive", "αναστοχαστική": "αναστοχαστικός — reflective", "βιώνεται": "βιώνομαι — to be experienced", "ενσυναίσθηση": "ενσυναίσθηση — empathy", "ανοιχτότητα": "ανοιχτότητα — openness"},
})

ITEMS.append({
 "id": "l42-int-arxaia-profora", "title": "Πώς μιλούσαν οι αρχαίοι Αθηναίοι;", "title_en": "How did the ancient Athenians speak?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν γλωσσολόγο για την προφορά της αρχαίας ελληνικής.",
 "script": [
  L("Δημοσιογράφος", "f", "Πολλοί Έλληνες εκπλήσσονται όταν ακούν ξένους φιλολόγους να διαβάζουν αρχαία κείμενα με μια προφορά εντελώς διαφορετική από τη δική μας. Ποια είναι η σωστή;", "Many Greeks are surprised when they hear foreign classicists reading ancient texts with a pronunciation completely different from ours. Which is the correct one?"),
  L("Γλωσσολόγος", "m", "Το ερώτημα «ποια είναι η σωστή» δεν έχει νόημα χωρίς να ρωτήσουμε «για ποια εποχή». Η γλώσσα άλλαζε συνεχώς. Για την Αθήνα του πέμπτου αιώνα π.Χ., οι γλωσσολόγοι συμφωνούν σε αρκετά σημεία: το βήτα προφερόταν πιθανότατα σαν το αγγλικό b, το φι σαν ένα π με δυνατή εκπνοή, και η γλώσσα είχε μουσικό τονισμό, δηλαδή ο τόνος ήταν ανέβασμα της φωνής και όχι δυνάμωμα.", "The question \"which is correct\" makes no sense without asking \"for which period\". The language was constantly changing. For fifth-century BC Athens, linguists agree on quite a few points: beta was most probably pronounced like English b, phi like a p with a strong breath, and the language had a musical accent, meaning the accent was a rise in pitch and not an increase in loudness."),
  L("Δημοσιογράφος", "f", "Και πώς το ξέρουμε αυτό, αφού δεν υπάρχουν ηχογραφήσεις;", "And how do we know this, since there are no recordings?"),
  L("Γλωσσολόγος", "m", "Από πολλές έμμεσες πηγές που, όταν συνδυάζονται, δίνουν μια αρκετά πειστική εικόνα. Τα ορθογραφικά λάθη σε επιγραφές δείχνουν πότε δύο ήχοι άρχισαν να συγχέονται. Οι μεταγραφές ελληνικών λέξεων σε άλλες γλώσσες, όπως τα λατινικά, μας λένε πώς τις άκουγαν οι ξένοι. Υπάρχουν και μαρτυρίες αρχαίων γραμματικών, ακόμα και κωμωδίες: σε έναν στίχο ενός κωμικού ποιητή, το βέλασμα του προβάτου γράφεται «βη βη».", "From many indirect sources which, when combined, give a fairly convincing picture. Spelling mistakes in inscriptions show when two sounds began to be confused. Transcriptions of Greek words in other languages, such as Latin, tell us how foreigners heard them. There is also the testimony of ancient grammarians, even comedies: in a line by a comic poet, a sheep's bleat is written «βη βη»."),
  L("Δημοσιογράφος", "f", "Πρέπει λοιπόν να αλλάξουμε τον τρόπο που διαβάζουμε τα αρχαία στα σχολεία;", "So should we change the way we read ancient Greek in schools?"),
  L("Γλωσσολόγος", "m", "Δεν το νομίζω. Η νεοελληνική προφορά έχει το πλεονέκτημα ότι συνδέει τα αρχαία κείμενα με μια ζωντανή γλώσσα και αναδεικνύει τη συνέχεια. Αρκεί να γνωρίζουμε ότι δεν είναι η προφορά του Περικλή, ούτε υποτίθεται ότι είναι. Η γνώση της ιστορίας των ήχων δεν απειλεί την ταυτότητά μας· την κάνει πλουσιότερη.", "I don't think so. The modern Greek pronunciation has the advantage of connecting the ancient texts with a living language and highlighting continuity. As long as we know that it is not Pericles' pronunciation, nor is it supposed to be. Knowing the history of the sounds does not threaten our identity; it enriches it."),
 ],
 "questions": [
  Q("Γιατί, κατά τον γλωσσολόγο, το ερώτημα «ποια προφορά είναι η σωστή» δεν έχει νόημα από μόνο του;", ["Επειδή κανείς δεν ξέρει τίποτα", "Επειδή η γλώσσα άλλαζε συνεχώς και πρέπει να ρωτήσουμε για ποια εποχή", "Επειδή όλες οι προφορές είναι εξίσου σωστές", "Επειδή οι ξένοι δεν ξέρουν ελληνικά"], 1, "δεν έχει νόημα χωρίς να ρωτήσουμε «για ποια εποχή». Η γλώσσα άλλαζε συνεχώς"),
  Q("Τι σημαίνει ότι η αρχαία γλώσσα είχε μουσικό τονισμό;", ["Ότι τα κείμενα τραγουδιούνταν", "Ότι ο τόνος ήταν ανέβασμα της φωνής και όχι δυνάμωμα", "Ότι υπήρχαν μουσικά όργανα στα θέατρα", "Ότι δεν υπήρχαν τόνοι"], 1, "ο τόνος ήταν ανέβασμα της φωνής και όχι δυνάμωμα"),
  Q("Ποια πηγή ΔΕΝ αναφέρει ο γλωσσολόγος;", ["Ορθογραφικά λάθη σε επιγραφές", "Αρχαίες ηχογραφήσεις", "Μεταγραφές σε άλλες γλώσσες", "Μαρτυρίες αρχαίων γραμματικών"], 1, "αφού δεν υπάρχουν ηχογραφήσεις"),
  Q("Ποια είναι η θέση του για τη διδασκαλία στα σχολεία;", ["Να υιοθετηθεί αμέσως η αρχαία προφορά", "Να διατηρηθεί η νεοελληνική προφορά, με επίγνωση ότι δεν είναι η αρχαία", "Να καταργηθεί η διδασκαλία των αρχαίων", "Να διδάσκονται μόνο μεταφράσεις"], 1, "Η νεοελληνική προφορά έχει το πλεονέκτημα… Αρκεί να γνωρίζουμε ότι δεν είναι η προφορά του Περικλή"),
 ],
 "gloss": {"προφορά": "προφορά — pronunciation", "εκπλήσσονται": "εκπλήσσομαι — to be surprised", "φιλολόγους": "φιλόλογος — philologist, classicist", "εκπνοή": "εκπνοή — exhalation, breath", "τονισμό": "τονισμός — accentuation", "έμμεσες": "έμμεσος — indirect", "επιγραφές": "επιγραφή — inscription", "να συγχέονται": "συγχέομαι — to be confused", "μεταγραφές": "μεταγραφή — transcription", "μαρτυρίες": "μαρτυρία — testimony", "βέλασμα": "βέλασμα — bleat", "αναδεικνύει": "αναδεικνύω — to highlight", "υποτίθεται": "υποτίθεται — is supposed to"},
})

rnd = random.Random(42)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-42.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
