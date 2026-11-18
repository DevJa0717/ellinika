# Source for library/listening/listening-231.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l231.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l231-news-apothikes-mouseiou", "title": "Ένα μουσείο ανοίγει τις αποθήκες του", "title_en": "A museum opens its storerooms", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός περιφερειακού σταθμού.",
 "script": [
  L("Εκφωνητής", "m", "Το αρχαιολογικό μουσείο της πόλης μας ανοίγει για πρώτη φορά στο κοινό τις αποθήκες του. Από τον επόμενο μήνα, κάθε δεύτερο Σάββατο, μικρές ομάδες επισκεπτών θα μπορούν να δουν αντικείμενα που μέχρι σήμερα έβλεπαν μόνο οι ερευνητές.", "Our city's archaeological museum is opening its storerooms to the public for the first time. From next month, every other Saturday, small groups of visitors will be able to see objects that until now only researchers saw."),
  L("Εκφωνητής", "m", "Όπως εξήγησε η διευθύντρια του μουσείου, στις αίθουσες εκτίθεται λιγότερο από το ένα δέκατο της συλλογής. Τα υπόλοιπα, χιλιάδες αγγεία, εργαλεία και θραύσματα από ανασκαφές της περιοχής, φυλάγονται σε ράφια στο υπόγειο, γιατί δεν υπάρχει χώρος να εκτεθούν.", "As the museum director explained, less than a tenth of the collection is on display in the galleries. The rest, thousands of pots, tools and fragments from excavations in the area, are kept on shelves in the basement, because there is no room to display them."),
  L("Εκφωνητής", "m", "Οι ξεναγήσεις θα κρατούν μία ώρα και θα γίνονται από αρχαιολόγους του μουσείου, που θα δείχνουν και πώς καθαρίζονται και καταγράφονται τα ευρήματα. Για λόγους ασφαλείας, κάθε ομάδα δεν θα ξεπερνά τα δώδεκα άτομα και θα χρειάζεται κράτηση από πριν.", "The tours will last an hour and will be given by the museum's archaeologists, who will also show how the finds are cleaned and recorded. For safety reasons, each group will not exceed twelve people and a booking will be needed in advance."),
  L("Εκφωνητής", "m", "«Θέλουμε ο κόσμος να καταλάβει ότι ένα μουσείο δεν είναι μόνο οι προθήκες», δήλωσε η διευθύντρια. «Είναι και η αθόρυβη δουλειά που γίνεται πίσω από αυτές.» Η είσοδος θα είναι δωρεάν για μαθητές και φοιτητές.", "'We want people to understand that a museum isn't just the display cases,' the director said. 'It's also the quiet work done behind them.' Entry will be free for school pupils and students."),
 ],
 "questions": [
  Q("Τι θα μπορούν να δουν οι επισκέπτες;", ["Μια νέα έκθεση ζωγραφικής", "Αντικείμενα που φυλάγονται στις αποθήκες", "Μια ανασκαφή σε εξέλιξη", "Αντίγραφα αρχαίων αγαλμάτων"], 1, "να δουν αντικείμενα που μέχρι σήμερα έβλεπαν μόνο οι ερευνητές"),
  Q("Γιατί τα περισσότερα αντικείμενα δεν εκτίθενται;", ["Γιατί είναι πολύ εύθραυστα", "Γιατί δεν υπάρχει χώρος", "Γιατί δεν έχουν καθαριστεί", "Γιατί ανήκουν σε άλλο μουσείο"], 1, "γιατί δεν υπάρχει χώρος να εκτεθούν"),
  Q("Τι θα δείχνουν επίσης οι αρχαιολόγοι;", ["Πώς καθαρίζονται και καταγράφονται τα ευρήματα", "Πώς φτιάχνονται αντίγραφα", "Πώς γίνεται μια ανασκαφή", "Πώς στήνεται μια προθήκη"], 0, "θα δείχνουν και πώς καθαρίζονται και καταγράφονται τα ευρήματα"),
  Q("Ποιος κανόνας ισχύει για τις ομάδες;", ["Μόνο για μαθητές", "Χωρίς κράτηση", "Το πολύ δώδεκα άτομα, με κράτηση", "Μόνο τις καθημερινές"], 2, "κάθε ομάδα δεν θα ξεπερνά τα δώδεκα άτομα και θα χρειάζεται κράτηση από πριν"),
 ],
 "gloss": {"αποθήκες": "αποθήκη — storeroom", "εκτίθεται": "εκτίθεμαι — to be displayed, exhibited", "δέκατο": "δέκατο — a tenth", "θραύσματα": "θραύσμα — fragment, shard", "ανασκαφές": "ανασκαφή — excavation", "ευρήματα": "εύρημα — find", "καταγράφονται": "καταγράφομαι — to be recorded, catalogued", "προθήκες": "προθήκη — display case", "αθόρυβη": "αθόρυβος — quiet, noiseless"},
})
ITEMS.append({
 "id": "l231-vm-agonas-dromou", "title": "Μήνυμα από τους διοργανωτές του αγώνα δρόμου", "title_en": "A message from the race organisers", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε γραφτεί σε έναν αγώνα δρόμου δέκα χιλιομέτρων στα Χανιά. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Διοργανώτρια", "f", "Καλησπέρα σας, σας καλούμε από την οργανωτική επιτροπή του αγώνα δρόμου των Χανίων, για τη συμμετοχή σας στα δέκα χιλιόμετρα της Κυριακής. Έχουμε δύο αλλαγές που πρέπει να γνωρίζετε.", "Good evening, we're calling from the organising committee of the Chania road race, about your entry for Sunday's ten kilometres. We have two changes you need to know about."),
  L("Διοργανώτρια", "f", "Πρώτον, λόγω της ζέστης που προβλέπεται, η εκκίνηση μεταφέρεται μία ώρα νωρίτερα, στις επτά και μισή το πρωί. Δεύτερον, η παραλαβή του φακέλου με τον αριθμό συμμετοχής δεν θα γίνει στο δημαρχείο, όπως γράφαμε, αλλά στο κλειστό γυμναστήριο δίπλα στο λιμάνι, την Παρασκευή και το Σάββατο από τις δέκα ως τις οχτώ.", "First, because of the heat that's forecast, the start is moving one hour earlier, to half past seven in the morning. Second, collection of the envelope with your race number won't take place at the town hall, as we'd written, but at the indoor sports hall next to the harbour, on Friday and Saturday from ten to eight."),
  L("Διοργανώτρια", "f", "Στον φάκελο θα βρείτε το τσιπάκι για τη χρονομέτρηση, που το δένετε στο κορδόνι του παπουτσιού, και ένα μπλουζάκι. Μην ξεχάσετε να φέρετε την ταυτότητά σας και τη βεβαίωση του γιατρού, αν δεν την έχετε ανεβάσει ήδη στην ιστοσελίδα.", "In the envelope you'll find the timing chip, which you tie to your shoelace, and a T-shirt. Don't forget to bring your ID card and the doctor's certificate, if you haven't already uploaded it to the website."),
  L("Διοργανώτρια", "f", "Σταθμοί με νερό θα υπάρχουν στο τρίτο και στο έβδομο χιλιόμετρο. Για οποιαδήποτε απορία, μπορείτε να μας στείλετε μήνυμα. Καλή επιτυχία την Κυριακή!", "There will be water stations at the third and seventh kilometres. For any questions, you can send us a message. Good luck on Sunday!"),
 ],
 "questions": [
  Q("Γιατί αλλάζει η ώρα της εκκίνησης;", ["Γιατί κλείνουν οι δρόμοι αργότερα", "Λόγω της ζέστης που προβλέπεται", "Γιατί υπάρχουν πολλοί συμμετέχοντες", "Λόγω μιας άλλης εκδήλωσης"], 1, "λόγω της ζέστης που προβλέπεται, η εκκίνηση μεταφέρεται μία ώρα νωρίτερα"),
  Q("Πού θα γίνει η παραλαβή του φακέλου;", ["Στο δημαρχείο", "Στο λιμάνι, πάνω σε ένα πλοίο", "Στο κλειστό γυμναστήριο δίπλα στο λιμάνι", "Στη γραμμή εκκίνησης την Κυριακή"], 2, "στο κλειστό γυμναστήριο δίπλα στο λιμάνι"),
  Q("Πού δένεται το τσιπάκι της χρονομέτρησης;", ["Στον καρπό", "Στο κορδόνι του παπουτσιού", "Στο μπλουζάκι", "Στον αριθμό συμμετοχής"], 1, "που το δένετε στο κορδόνι του παπουτσιού"),
  Q("Τι πρέπει να φέρουν οι δρομείς στην παραλαβή;", ["Μόνο το μπλουζάκι", "Την ταυτότητα και, αν δεν την έχουν ανεβάσει, τη βεβαίωση του γιατρού", "Μια φωτογραφία", "Το παράβολο συμμετοχής σε μετρητά"], 1, "Μην ξεχάσετε να φέρετε την ταυτότητά σας και τη βεβαίωση του γιατρού"),
 ],
 "gloss": {"οργανωτική επιτροπή": "οργανωτική επιτροπή — organising committee", "συμμετοχή": "συμμετοχή — entry, participation", "εκκίνηση": "εκκίνηση — start (of a race)", "μεταφέρεται": "μεταφέρομαι — to be moved", "παραλαβή": "παραλαβή — collection, pick-up", "αριθμό συμμετοχής": "αριθμός συμμετοχής — race number, bib", "χρονομέτρηση": "χρονομέτρηση — timing", "κορδόνι": "κορδόνι — shoelace", "βεβαίωση": "βεβαίωση — certificate", "Σταθμοί": "σταθμός — station"},
})
ITEMS.append({
 "id": "l231-c1-mono-koryfi-telos", "title": "Ο κανόνας «κορυφή και τέλος»: πώς θυμόμαστε όσα ζήσαμε", "title_en": "The peak-end rule: how we remember what we lived through", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια εκπομπή για την ψυχολογία της καθημερινής ζωής.",
 "script": [
  L("Ομιλητής", "m", "Φανταστείτε δύο δοκιμασίες. Στην πρώτη, βάζετε το χέρι σας για ένα λεπτό σε πολύ κρύο νερό. Στη δεύτερη, κάνετε ακριβώς το ίδιο, αλλά μετά το λεπτό κρατάτε το χέρι μέσα για άλλα τριάντα δευτερόλεπτα, ενώ το νερό ζεσταίνεται ελάχιστα. Ποια από τις δύο θα επιλέγατε να επαναλάβετε;", "Imagine two ordeals. In the first, you put your hand in very cold water for a minute. In the second, you do exactly the same, but after the minute you keep your hand in for another thirty seconds while the water warms very slightly. Which of the two would you choose to repeat?"),
  L("Ομιλητής", "m", "Η λογική απάντηση είναι η πρώτη, αφού η δεύτερη περιέχει όλο τον πόνο της πρώτης και κάτι ακόμη. Κι όμως, σε ένα γνωστό πείραμα των αρχών της δεκαετίας του '90, οι περισσότεροι συμμετέχοντες προτίμησαν να επαναλάβουν τη δεύτερη. Ο λόγος; Τελείωνε λίγο λιγότερο άσχημα.", "The logical answer is the first, since the second contains all the pain of the first and something more. And yet, in a well-known experiment from the early nineties, most participants preferred to repeat the second. The reason? It ended slightly less badly."),
  L("Ομιλητής", "m", "Ο ψυχολόγος Ντάνιελ Κάνεμαν και οι συνεργάτες του ονόμασαν το φαινόμενο «κανόνα κορυφής και τέλους». Όταν κρίνουμε μια εμπειρία εκ των υστέρων, δεν αθροίζουμε κάθε στιγμή της. Θυμόμαστε κυρίως δύο σημεία: την πιο έντονη στιγμή και τον τρόπο που τελείωσε. Η διάρκεια σχεδόν δεν παίζει ρόλο.", "The psychologist Daniel Kahneman and his colleagues named the phenomenon the 'peak-end rule'. When we judge an experience after the fact, we don't add up each of its moments. We remember mainly two points: the most intense moment and the way it ended. Duration hardly plays a role."),
  L("Ομιλητής", "m", "Οι συνέπειες είναι πρακτικές. Ένας γιατρός που τελειώνει μια δυσάρεστη εξέταση πιο ήπια αφήνει στον ασθενή καλύτερη ανάμνηση, και ο ασθενής είναι πιο πρόθυμος να ξανάρθει. Ένα ταξίδι με πολλές δυσκολίες μπορεί να μείνει στη μνήμη ως υπέροχο, αν το τελευταίο βράδυ ήταν μαγικό. Ίσως, λοιπόν, να αξίζει να φροντίζουμε λίγο περισσότερο τα τέλη.", "The consequences are practical. A doctor who ends an unpleasant examination more gently leaves the patient with a better memory, and the patient is more willing to come back. A trip with many difficulties may stay in memory as wonderful if the last evening was magical. So perhaps it's worth taking a little more care over endings."),
 ],
 "questions": [
  Q("Ποια δοκιμασία προτίμησαν να επαναλάβουν οι περισσότεροι στο πείραμα;", ["Την πρώτη, που ήταν πιο σύντομη", "Τη δεύτερη, που ήταν πιο μεγάλη αλλά τελείωνε λιγότερο άσχημα", "Καμία από τις δύο", "Όποια ήταν πιο ζεστή από την αρχή"], 1, "οι περισσότεροι συμμετέχοντες προτίμησαν να επαναλάβουν τη δεύτερη. … Τελείωνε λίγο λιγότερο άσχημα"),
  Q("Σύμφωνα με τον κανόνα, ποια σημεία μιας εμπειρίας θυμόμαστε κυρίως;", ["Την αρχή και τη μέση", "Τη διάρκεια και την αρχή", "Την πιο έντονη στιγμή και το τέλος", "Κάθε στιγμή εξίσου"], 2, "Θυμόμαστε κυρίως δύο σημεία: την πιο έντονη στιγμή και τον τρόπο που τελείωσε"),
  Q("Τι λέει ο ομιλητής για τη διάρκεια μιας εμπειρίας;", ["Ότι είναι το πιο σημαντικό", "Ότι σχεδόν δεν παίζει ρόλο στην ανάμνηση", "Ότι μετράει μόνο στον πόνο", "Ότι κάνει τις εμπειρίες πιο ευχάριστες"], 1, "Η διάρκεια σχεδόν δεν παίζει ρόλο"),
  Q("Ποιο πρακτικό συμπέρασμα βγάζει;", ["Ότι πρέπει να αποφεύγουμε τις δυσάρεστες εμπειρίες", "Ότι οι γιατροί πρέπει να κάνουν πιο σύντομες εξετάσεις", "Ότι τα ταξίδια πρέπει να είναι μικρά", "Ότι αξίζει να φροντίζουμε περισσότερο τα τέλη"], 3, "Ίσως, λοιπόν, να αξίζει να φροντίζουμε λίγο περισσότερο τα τέλη"),
 ],
 "gloss": {"δοκιμασίες": "δοκιμασία — ordeal, test", "επαναλάβετε": "επαναλαμβάνω — to repeat", "συμμετέχοντες": "συμμετέχων — participant", "εκ των υστέρων": "εκ των υστέρων — after the fact, in retrospect", "αθροίζουμε": "αθροίζω — to add up", "έντονη": "έντονος — intense", "διάρκεια": "διάρκεια — duration", "συνέπειες": "συνέπεια — consequence", "ήπια": "ήπια — gently, mildly", "πρόθυμος": "πρόθυμος — willing"},
})
ITEMS.append({
 "id": "l231-c1-int-seismiko-sminos", "title": "Μια σεισμολόγος για το σεισμικό σμήνος ανάμεσα σε Σαντορίνη και Αμοργό", "title_en": "A seismologist on the earthquake swarm between Santorini and Amorgos", "type": "interview", "level": "C1",
 "context_el": "Μια σεισμολόγος μιλά σε μια ραδιοφωνική εκπομπή για τη σεισμική δραστηριότητα του χειμώνα του 2025 στις Κυκλάδες.",
 "script": [
  L("Δημοσιογράφος", "m", "Τον χειμώνα του 2025 χιλιάδες σεισμοί καταγράφηκαν μέσα σε λίγες εβδομάδες ανάμεσα στη Σαντορίνη και την Αμοργό. Τι ακριβώς είναι ένα σεισμικό σμήνος;", "In the winter of 2025 thousands of earthquakes were recorded within a few weeks between Santorini and Amorgos. What exactly is an earthquake swarm?"),
  L("Σεισμολόγος", "f", "Στη συνηθισμένη περίπτωση έχουμε έναν κύριο σεισμό, ακολουθούμενο από μετασεισμούς που σιγά σιγά εξασθενούν. Στο σμήνος δεν υπάρχει ένας ξεκάθαρος κύριος σεισμός. Έχουμε πολλούς σεισμούς παρόμοιου μεγέθους, που συνεχίζονται για μέρες ή εβδομάδες. Τότε, οι περισσότεροι ήταν μικροί, ενώ οι μεγαλύτεροι έφτασαν γύρω στα πέντε Ρίχτερ.", "In the usual case we have a main earthquake followed by aftershocks that gradually weaken. In a swarm there is no clear main earthquake. We have many earthquakes of similar size that go on for days or weeks. That time, most were small, while the largest reached around five on the Richter scale."),
  L("Δημοσιογράφος", "m", "Πολλοί κάτοικοι έφυγαν προσωρινά από το νησί. Ήταν υπερβολική αντίδραση;", "Many residents left the island temporarily. Was that an overreaction?"),
  L("Σεισμολόγος", "f", "Δεν θα το έλεγα. Όταν η γη τρέμει συνεχώς, ο φόβος είναι απολύτως κατανοητός, και οι αρχές πήραν μέτρα προφύλαξης, όπως το κλείσιμο των σχολείων. Το δύσκολο για εμάς ήταν να εξηγήσουμε την αβεβαιότητα. Ο κόσμος ήθελε να ακούσει «θα γίνει» ή «δεν θα γίνει» ένας μεγάλος σεισμός, και η επιστήμη δεν μπορεί να δώσει τέτοιες απαντήσεις.", "I wouldn't say so. When the ground shakes continuously, fear is entirely understandable, and the authorities took precautions, such as closing the schools. The hard part for us was explaining the uncertainty. People wanted to hear 'there will' or 'there won't' be a big earthquake, and science can't give such answers."),
  L("Δημοσιογράφος", "m", "Τι προκάλεσε τελικά το σμήνος;", "What caused the swarm in the end?"),
  L("Σεισμολόγος", "f", "Η επικρατέστερη ερμηνεία, σύμφωνα με αρκετές μελέτες που ακολούθησαν, είναι ότι μάγμα κινήθηκε σε μεγάλο βάθος και άνοιξε δρόμο μέσα από τα πετρώματα, χωρίς να φτάσει στην επιφάνεια. Η συζήτηση, πάντως, συνεχίζεται. Αυτό που κρατώ εγώ είναι ότι πρέπει να μιλάμε για τους σεισμούς και στις ήρεμες περιόδους, ώστε ο κόσμος να μην ακούει για πρώτη φορά τις λέξεις μας μέσα στον πανικό.", "The prevailing interpretation, according to several studies that followed, is that magma moved at great depth and forced a path through the rocks, without reaching the surface. The debate, however, continues. What I take away is that we need to talk about earthquakes in calm periods too, so that people don't hear our words for the first time in the middle of panic."),
 ],
 "questions": [
  Q("Πώς διαφέρει ένα σεισμικό σμήνος από τη συνηθισμένη ακολουθία;", ["Έχει πάντα έναν πολύ μεγάλο σεισμό", "Δεν έχει ξεκάθαρο κύριο σεισμό, αλλά πολλούς παρόμοιου μεγέθους", "Κρατά μόνο λίγες ώρες", "Γίνεται μόνο κάτω από τη θάλασσα"], 1, "Στο σμήνος δεν υπάρχει ένας ξεκάθαρος κύριος σεισμός. Έχουμε πολλούς σεισμούς παρόμοιου μεγέθους"),
  Q("Τι λέει η σεισμολόγος για όσους έφυγαν από το νησί;", ["Ότι αντέδρασαν υπερβολικά", "Ότι ο φόβος τους ήταν κατανοητός", "Ότι έπρεπε να μείνουν", "Ότι παρέβησαν τις οδηγίες"], 1, "ο φόβος είναι απολύτως κατανοητός"),
  Q("Τι ήταν το πιο δύσκολο για τους επιστήμονες;", ["Να μετρήσουν τους σεισμούς", "Να βρουν χρηματοδότηση", "Να εξηγήσουν την αβεβαιότητα στον κόσμο", "Να φτάσουν στο νησί"], 2, "Το δύσκολο για εμάς ήταν να εξηγήσουμε την αβεβαιότητα"),
  Q("Ποια είναι η επικρατέστερη ερμηνεία για την αιτία του σμήνους;", ["Μια έκρηξη του ηφαιστείου", "Η κίνηση μάγματος σε μεγάλο βάθος", "Ένα τσουνάμι", "Η κατασκευή νέων έργων στο νησί"], 1, "μάγμα κινήθηκε σε μεγάλο βάθος και άνοιξε δρόμο μέσα από τα πετρώματα"),
 ],
 "gloss": {"σεισμικό σμήνος": "σεισμικό σμήνος — earthquake swarm", "μετασεισμούς": "μετασεισμός — aftershock", "εξασθενούν": "εξασθενώ — to weaken, fade", "Ρίχτερ": "Ρίχτερ — Richter (scale)", "προσωρινά": "προσωρινά — temporarily", "προφύλαξης": "προφύλαξη — precaution", "αβεβαιότητα": "αβεβαιότητα — uncertainty", "επικρατέστερη": "επικρατέστερος — prevailing, most widely accepted", "ερμηνεία": "ερμηνεία — interpretation", "μάγμα": "μάγμα — magma", "πετρώματα": "πέτρωμα — rock (formation)", "πανικό": "πανικός — panic"},
})
rnd = random.Random(231)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-231.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
