# Source for library/listening/listening-120.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l120.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l120-ann-kolymvitirio-syntirisi", "title": "Κλειστό το δημοτικό κολυμβητήριο για συντήρηση", "title_en": "The municipal pool closes for maintenance", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε στο δημοτικό κολυμβητήριο, όπου κολυμπάτε τακτικά. Ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Υπάλληλος", "m", "Αγαπητοί κολυμβητές, σας ενημερώνουμε ότι από την ερχόμενη Δευτέρα το κολυμβητήριο θα παραμείνει κλειστό για δύο εβδομάδες, λόγω εργασιών συντήρησης. Θα αλλάξουν τα φίλτρα του νερού και θα επισκευαστούν τα πλακάκια στον πάτο της μεγάλης πισίνας.", "Dear swimmers, we would like to inform you that from next Monday the pool will remain closed for two weeks for maintenance work. The water filters will be replaced and the tiles at the bottom of the large pool will be repaired."),
  L("Υπάλληλος", "m", "Κατά τη διάρκεια των εργασιών, οι κάτοχοι μηνιαίας κάρτας μπορούν να κολυμπούν δωρεάν στο κολυμβητήριο του γειτονικού δήμου, δείχνοντας την κάρτα τους στην είσοδο. Οι μέρες που θα χάσετε θα προστεθούν αυτόματα στη συνδρομή σας.", "During the work, holders of a monthly card can swim free of charge at the pool of the neighbouring municipality by showing their card at the entrance. The days you miss will be added automatically to your membership."),
  L("Υπάλληλος", "m", "Τα μαθήματα κολύμβησης για παιδιά δεν θα ακυρωθούν. Θα γίνονται στη μικρή πισίνα, που δεν επηρεάζεται από τις εργασίες, τις ίδιες μέρες και ώρες. Ευχαριστούμε για την κατανόηση.", "Children's swimming lessons will not be cancelled. They will take place in the small pool, which is not affected by the work, on the same days and at the same times. Thank you for your understanding."),
 ],
 "questions": [
  Q("Γιατί θα κλείσει το κολυμβητήριο;", ["Λόγω απεργίας", "Λόγω εργασιών συντήρησης", "Λόγω έλλειψης προσωπικού", "Λόγω αγώνων κολύμβησης"], 1, "λόγω εργασιών συντήρησης"),
  Q("Τι μπορούν να κάνουν οι κάτοχοι μηνιαίας κάρτας στο διάστημα αυτό;", ["Να πάρουν πίσω τα χρήματά τους", "Να κολυμπήσουν στη θάλασσα με τον σύλλογο", "Να κολυμπούν δωρεάν στο κολυμβητήριο του γειτονικού δήμου", "Να γυμνάζονται στο γυμναστήριο του κολυμβητηρίου"], 2, "μπορούν να κολυμπούν δωρεάν στο κολυμβητήριο του γειτονικού δήμου"),
  Q("Τι θα γίνει με τα μαθήματα για παιδιά;", ["Θα γίνονται στη μικρή πισίνα τις ίδιες μέρες και ώρες", "Θα ακυρωθούν για δύο εβδομάδες", "Θα γίνονται στο γειτονικό κολυμβητήριο", "Θα μετακινηθούν στο Σαββατοκύριακο"], 0, "Θα γίνονται στη μικρή πισίνα"),
 ],
 "gloss": {"κολυμβητήριο": "κολυμβητήριο — swimming pool (complex)", "μεγάφωνα": "μεγάφωνο — loudspeaker", "συντήρησης": "συντήρηση — maintenance", "φίλτρα": "φίλτρο — filter", "πλακάκια": "πλακάκι — tile", "κάτοχοι": "κάτοχος — holder", "γειτονικού": "γειτονικός — neighbouring", "συνδρομή": "συνδρομή — membership, subscription", "επηρεάζεται": "επηρεάζομαι — to be affected", "κατανόηση": "κατανόηση — understanding"}
})

ITEMS.append({
 "id": "l120-vm-foititiki-estia", "title": "Μήνυμα από τη φοιτητική εστία", "title_en": "A message from the student residence", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κάνει αίτηση για ένα δωμάτιο σε φοιτητική εστία. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "f", "Καλησπέρα σας, από τη γραμματεία της φοιτητικής εστίας σας καλώ. Με χαρά σας ενημερώνω ότι η αίτησή σας εγκρίθηκε και σας έχει δοθεί ένα μονόκλινο δωμάτιο στο κτίριο Β, στον τρίτο όροφο.", "Good evening, I'm calling from the office of the student residence. I'm pleased to inform you that your application has been approved and you have been given a single room in building B, on the third floor."),
  L("Υπάλληλος", "f", "Για να κρατήσετε τη θέση σας, πρέπει να έρθετε μέχρι την Πέμπτη με την αστυνομική σας ταυτότητα, μια φωτογραφία και μια βεβαίωση εγγραφής από τη σχολή σας. Αν δεν έρθετε ως τότε, το δωμάτιο θα δοθεί στον επόμενο στη λίστα.", "To keep your place, you must come by Thursday with your identity card, a photograph and a certificate of enrolment from your school. If you don't come by then, the room will be given to the next person on the list."),
  L("Υπάλληλος", "f", "Να ξέρετε ότι στα δωμάτια δεν επιτρέπονται ηλεκτρικές εστίες μαγειρέματος, για λόγους ασφαλείας. Σε κάθε όροφο όμως υπάρχει κοινή κουζίνα, και το εστιατόριο της εστίας προσφέρει δωρεάν σίτιση στους δικαιούχους.", "Please note that electric hotplates are not allowed in the rooms for safety reasons. On each floor, however, there is a shared kitchen, and the residence restaurant offers free meals to those who are eligible."),
 ],
 "questions": [
  Q("Τι δωμάτιο πήρε ο ακροατής;", ["Ένα δίκλινο στο ισόγειο", "Ένα μονόκλινο δωμάτιο στο κτίριο Β, στον τρίτο όροφο", "Ένα στούντιο με κουζίνα", "Ένα δωμάτιο σε άλλη εστία"], 1, "ένα μονόκλινο δωμάτιο στο κτίριο Β, στον τρίτο όροφο"),
  Q("Τι θα γίνει αν δεν πάει ως την Πέμπτη;", ["Θα πληρώσει πρόστιμο", "Θα πρέπει να κάνει νέα αίτηση την άλλη χρονιά", "Το δωμάτιο θα δοθεί στον επόμενο στη λίστα", "Θα του δώσουν δωμάτιο σε άλλο κτίριο"], 2, "το δωμάτιο θα δοθεί στον επόμενο στη λίστα"),
  Q("Τι δεν επιτρέπεται στα δωμάτια;", ["Ηλεκτρικές εστίες μαγειρέματος", "Επισκέπτες μετά τις δέκα", "Κατοικίδια ζώα", "Μουσική μετά τα μεσάνυχτα"], 0, "στα δωμάτια δεν επιτρέπονται ηλεκτρικές εστίες μαγειρέματος"),
 ],
 "gloss": {"φοιτητική": "φοιτητικός — student (adj.)", "εστία": "εστία — (student) residence; also hotplate", "γραμματεία": "γραμματεία — office, secretariat", "εγκρίθηκε": "εγκρίνομαι — to be approved", "μονόκλινο": "μονόκλινο — single room", "αστυνομική σας ταυτότητα": "αστυνομική ταυτότητα — identity card", "βεβαίωση εγγραφής": "βεβαίωση εγγραφής — certificate of enrolment", "επιτρέπονται": "επιτρέπομαι — to be allowed", "σίτιση": "σίτιση — meals, board", "δικαιούχους": "δικαιούχος — eligible person, beneficiary"}
})

ITEMS.append({
 "id": "l120-dial-defteri-xeni-glossa", "title": "Ποια δεύτερη ξένη γλώσσα για την κόρη μας;", "title_en": "Which second foreign language for our daughter?", "type": "dialogue", "level": "B2",
 "context_el": "Ο Μιχάλης και η Ζωή συζητούν ποια δεύτερη ξένη γλώσσα θα μάθει η δεκάχρονη κόρη τους, η Ηλέκτρα, που ήδη μαθαίνει αγγλικά.",
 "script": [
  L("Ζωή", "f", "Μιχάλη, πρέπει να αποφασίσουμε μέχρι την Παρασκευή για τη δεύτερη ξένη γλώσσα της Ηλέκτρας. Το φροντιστήριο προσφέρει γαλλικά, γερμανικά, ισπανικά και, από φέτος, κινέζικα.", "Michalis, we have to decide by Friday about Electra's second foreign language. The language school offers French, German, Spanish and, from this year, Chinese."),
  L("Μιχάλης", "m", "Εγώ λέω γερμανικά. Είναι χρήσιμα για σπουδές και για δουλειά, και ο ξάδερφός της μένει στο Μόναχο. Θα έχει και με ποιον να τα μιλάει.", "I say German. It's useful for studies and for work, and her cousin lives in Munich. She'll also have someone to speak it with."),
  L("Ζωή", "f", "Ναι, αλλά εκείνη ζητάει ισπανικά, επειδή βλέπει μια ισπανική σειρά με υπότιτλους και της αρέσουν τα τραγούδια. Σε αυτή την ηλικία, αν δεν της αρέσει κάτι, θα το παρατήσει σε έναν χρόνο.", "Yes, but she's asking for Spanish, because she watches a Spanish series with subtitles and she likes the songs. At this age, if she doesn't like something, she'll give it up within a year."),
  L("Μιχάλης", "m", "Έχεις δίκιο ότι το κίνητρο μετράει πολύ. Και τα κινέζικα; Δεν θα ήταν ένα μεγάλο προσόν στο μέλλον;", "You're right that motivation counts for a lot. And Chinese? Wouldn't it be a big advantage in the future?"),
  L("Ζωή", "f", "Ίσως, αλλά τα μαθήματα είναι μόνο μία φορά την εβδομάδα και ο δάσκαλος έρχεται από άλλη πόλη. Ας ξεκινήσει ισπανικά, που τα θέλει η ίδια, και αν αργότερα της αρέσουν οι γλώσσες, μπορεί να προσθέσει και τρίτη.", "Maybe, but the lessons are only once a week and the teacher comes from another town. Let her start Spanish, which she wants herself, and if later on she likes languages, she can add a third."),
 ],
 "questions": [
  Q("Γιατί ο Μιχάλης προτιμά τα γερμανικά;", ["Γιατί τα έμαθε κι ο ίδιος", "Γιατί είναι χρήσιμα για σπουδές και δουλειά και ο ξάδερφός της μένει στο Μόναχο", "Γιατί είναι πιο φθηνά τα μαθήματα", "Γιατί το πρότεινε η δασκάλα"], 1, "Είναι χρήσιμα για σπουδές και για δουλειά, και ο ξάδερφός της μένει στο Μόναχο"),
  Q("Γιατί η Ηλέκτρα θέλει ισπανικά;", ["Γιατί θα πάει διακοπές στην Ισπανία", "Γιατί οι φίλες της μαθαίνουν ισπανικά", "Γιατί βλέπει μια ισπανική σειρά και της αρέσουν τα τραγούδια", "Γιατί είναι εύκολη γλώσσα"], 2, "βλέπει μια ισπανική σειρά με υπότιτλους και της αρέσουν τα τραγούδια"),
  Q("Ποια λύση προτείνει τελικά η Ζωή;", ["Να ξεκινήσει ισπανικά και αργότερα, αν θέλει, να προσθέσει τρίτη γλώσσα", "Να μάθει δύο γλώσσες μαζί", "Να ξεκινήσει κινέζικα", "Να περιμένουν έναν χρόνο"], 0, "Ας ξεκινήσει ισπανικά, που τα θέλει η ίδια"),
 ],
 "gloss": {"φροντιστήριο": "φροντιστήριο — (private) language school", "κινέζικα": "κινέζικα — Chinese (language)", "ξάδερφός": "ξάδερφος — cousin", "υπότιτλους": "υπότιτλος — subtitle", "παρατήσει": "παρατάω — to give up, quit", "κίνητρο": "κίνητρο — motivation", "μετράει": "μετράω — to count, matter", "προσόν": "προσόν — asset, qualification", "προσθέσει": "προσθέτω — to add"}
})

ITEMS.append({
 "id": "l120-int-nomismatologos", "title": "Μια νομισματολόγος", "title_en": "A numismatist", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με τη Δανάη, νομισματολόγο σε ένα μουσείο, που μελετά αρχαία νομίσματα.",
 "script": [
  L("Δημοσιογράφος", "m", "Δανάη, τι μπορεί να μας πει ένα νόμισμα που ένα βιβλίο δεν μπορεί;", "Danae, what can a coin tell us that a book can't?"),
  L("Δανάη", "f", "Πολλά. Τα νομίσματα είναι μικρά ντοκουμέντα της εποχής τους. Μας λένε ποιος κυβερνούσε, ποιους θεούς λάτρευαν, ακόμα και με ποιες πόλεις εμπορεύονταν οι άνθρωποι. Όταν βρίσκουμε αθηναϊκά νομίσματα με την κουκουβάγια σε μακρινές περιοχές, καταλαβαίνουμε πόσο μακριά έφταναν οι εμπορικοί δρόμοι.", "A lot. Coins are small documents of their time. They tell us who ruled, which gods people worshipped, even which cities they traded with. When we find Athenian coins with the owl in distant regions, we understand how far the trade routes reached."),
  L("Δημοσιογράφος", "m", "Πώς είναι μια μέρα στη δουλειά σας;", "What is a day at your work like?"),
  L("Δανάη", "f", "Λιγότερο ρομαντική από όσο νομίζετε. Ζυγίζω, μετράω, φωτογραφίζω και καταγράφω κάθε νόμισμα σε μια βάση δεδομένων. Συχνά χρειάζομαι μεγεθυντικό φακό για να διαβάσω επιγραφές που έχουν σχεδόν σβηστεί.", "Less romantic than you think. I weigh, measure, photograph and record each coin in a database. I often need a magnifying glass to read inscriptions that have almost been worn away."),
  L("Δημοσιογράφος", "m", "Υπάρχουν πλαστά αρχαία νομίσματα;", "Are there fake ancient coins?"),
  L("Δανάη", "f", "Δυστυχώς, πάρα πολλά, και μερικά είναι εξαιρετικά καλές απομιμήσεις. Γι’ αυτό λέω πάντα στους συλλέκτες να μην αγοράζουν νομίσματα από το διαδίκτυο χωρίς πιστοποιητικό. Και να θυμούνται ότι η αγορά αρχαίων χωρίς άδεια είναι παράνομη.", "Unfortunately, very many, and some are extremely good imitations. That's why I always tell collectors not to buy coins online without a certificate. And to remember that buying antiquities without a licence is illegal."),
 ],
 "questions": [
  Q("Τι δείχνουν τα αθηναϊκά νομίσματα που βρίσκονται σε μακρινές περιοχές;", ["Ότι οι Αθηναίοι είχαν αποικίες παντού", "Πόσο μακριά έφταναν οι εμπορικοί δρόμοι", "Ότι τα νομίσματα ήταν πολύ φθηνά", "Ότι οι κουκουβάγιες ζούσαν παντού"], 1, "καταλαβαίνουμε πόσο μακριά έφταναν οι εμπορικοί δρόμοι"),
  Q("Πώς περιγράφει η Δανάη την καθημερινή της δουλειά;", ["Γεμάτη περιπέτειες και ταξίδια", "Κυρίως ανασκαφές στο ύπαιθρο", "Λιγότερο ρομαντική από όσο νομίζουμε", "Πολύ βαρετή"], 2, "Λιγότερο ρομαντική από όσο νομίζετε"),
  Q("Τι συμβουλεύει τους συλλέκτες;", ["Να μην αγοράζουν νομίσματα από το διαδίκτυο χωρίς πιστοποιητικό", "Να αγοράζουν μόνο χρυσά νομίσματα", "Να δωρίζουν τα νομίσματα σε μουσεία", "Να καθαρίζουν τα νομίσματα με νερό"], 0, "να μην αγοράζουν νομίσματα από το διαδίκτυο χωρίς πιστοποιητικό"),
 ],
 "gloss": {"νομισματολόγο": "νομισματολόγος — numismatist", "νομίσματα": "νόμισμα — coin", "ντοκουμέντα": "ντοκουμέντο — document, evidence", "λάτρευαν": "λατρεύω — to worship", "εμπορεύονταν": "εμπορεύομαι — to trade", "κουκουβάγια": "κουκουβάγια — owl", "Ζυγίζω": "ζυγίζω — to weigh", "βάση δεδομένων": "βάση δεδομένων — database", "μεγεθυντικό φακό": "μεγεθυντικός φακός — magnifying glass", "επιγραφές": "επιγραφή — inscription", "πλαστά": "πλαστός — fake, forged", "απομιμήσεις": "απομίμηση — imitation", "συλλέκτες": "συλλέκτης — collector"}
})

ITEMS.append({
 "id": "l120-rep-noimatiki-sto-scholeio", "title": "Μια τάξη μαθαίνει νοηματική γλώσσα", "title_en": "A class learns sign language", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα δημοτικό σχολείο όπου τα παιδιά μιας τάξης μαθαίνουν την Ελληνική Νοηματική Γλώσσα.",
 "script": [
  L("Ρεπόρτερ", "f", "Όταν ο Άγγελος, ένα κωφό αγόρι εννέα χρονών, ήρθε στο σχολείο τον Σεπτέμβριο, οι συμμαθητές του δεν ήξεραν πώς να του μιλήσουν. Η δασκάλα τους πρότεινε κάτι απλό: να μάθουν όλοι μαζί τη γλώσσα του.", "When Angelos, a nine-year-old deaf boy, came to the school in September, his classmates didn't know how to talk to him. Their teacher suggested something simple: that they all learn his language together."),
  L("Ρεπόρτερ", "f", "Δύο φορές την εβδομάδα, μια δασκάλα νοηματικής, που είναι κι εκείνη κωφή, διδάσκει στην τάξη. Τα παιδιά έμαθαν πρώτα να λένε τα ονόματά τους με τα δάχτυλα και ύστερα λέξεις για το σχολείο, το φαγητό και το παιχνίδι. Σήμερα, στο διάλειμμα, πολλά από αυτά συνομιλούν με τον Άγγελο χωρίς βοήθεια.", "Twice a week, a sign language teacher, who is also deaf, teaches the class. The children first learned to spell their names with their fingers and then words for school, food and play. Today, at break time, many of them chat with Angelos without help."),
  L("Ρεπόρτερ", "f", "Οι γονείς λένε ότι τα παιδιά έγιναν πιο προσεκτικά στο πώς επικοινωνούν: κοιτάζουν τον άλλον στα μάτια και περιμένουν τη σειρά τους. Το σχολείο σκοπεύει από του χρόνου να προσφέρει μαθήματα νοηματικής και στους γονείς, που το ζήτησαν οι ίδιοι.", "Parents say the children have become more attentive in how they communicate: they look the other person in the eye and wait their turn. From next year the school plans to offer sign language lessons to parents too, who asked for it themselves."),
 ],
 "questions": [
  Q("Τι πρότεινε η δασκάλα όταν ήρθε ο Άγγελος;", ["Να μεταφερθεί σε ειδικό σχολείο", "Να μάθουν όλοι μαζί τη γλώσσα του", "Να έχει έναν βοηθό σε όλα τα μαθήματα", "Να γράφουν σημειώματα"], 1, "να μάθουν όλοι μαζί τη γλώσσα του"),
  Q("Τι έμαθαν πρώτα τα παιδιά;", ["Τραγούδια στη νοηματική", "Τα χρώματα και τους αριθμούς", "Να λένε τα ονόματά τους με τα δάχτυλα", "Να διαβάζουν τα χείλη"], 2, "να λένε τα ονόματά τους με τα δάχτυλα"),
  Q("Τι σκοπεύει να κάνει το σχολείο από του χρόνου;", ["Να προσφέρει μαθήματα νοηματικής και στους γονείς", "Να προσλάβει κι άλλους κωφούς δασκάλους", "Να διδάσκει νοηματική σε όλες τις τάξεις", "Να οργανώσει ένα θεατρικό στη νοηματική"], 0, "να προσφέρει μαθήματα νοηματικής και στους γονείς"),
 ],
 "gloss": {"Νοηματική Γλώσσα": "νοηματική γλώσσα — sign language", "κωφό": "κωφός — deaf", "συμμαθητές": "συμμαθητής — classmate", "διάλειμμα": "διάλειμμα — break (at school)", "συνομιλούν": "συνομιλώ — to converse, chat", "προσεκτικά": "προσεκτικός — attentive, careful", "επικοινωνούν": "επικοινωνώ — to communicate", "σκοπεύει": "σκοπεύω — to intend, plan"}
})

ITEMS.append({
 "id": "l120-rep-scholeio-xananoigei", "title": "Το σχολείο ενός χωριού ξανανοίγει", "title_en": "A village school reopens", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα ορεινό χωριό της Αρκαδίας, όπου το δημοτικό σχολείο ξανανοίγει μετά από δώδεκα χρόνια.",
 "script": [
  L("Ρεπόρτερ", "m", "Το κουδούνι του δημοτικού σχολείου είχε να χτυπήσει δώδεκα χρόνια. Φέτος τον Σεπτέμβριο ακούστηκε ξανά, γιατί στο χωριό εγκαταστάθηκαν τέσσερις οικογένειες από την Αθήνα και την Πάτρα, με εννέα παιδιά συνολικά.", "The bell of the primary school hadn't rung for twelve years. This September it was heard again, because four families from Athens and Patras settled in the village, with nine children altogether."),
  L("Ρεπόρτερ", "m", "Οι περισσότεροι γονείς εργάζονται από απόσταση, μέσω διαδικτύου. Η κοινότητα τους βοήθησε να βρουν σπίτια με χαμηλό ενοίκιο, και ο δήμος επισκεύασε τη σκεπή του σχολείου και έφερε καινούργιους υπολογιστές.", "Most of the parents work remotely, online. The community helped them find houses with low rent, and the municipality repaired the school roof and brought new computers."),
  L("Ρεπόρτερ", "m", "Οι ηλικιωμένοι του χωριού είναι οι πιο ενθουσιασμένοι. Κάποιοι έρχονται στο σχολείο και διηγούνται στα παιδιά ιστορίες από τα παλιά, ενώ ένας συνταξιούχος γεωπόνος φύτεψε μαζί τους έναν λαχανόκηπο στην αυλή. «Χωριό χωρίς παιδιά είναι χωριό χωρίς μέλλον», λέει ο πρόεδρος της κοινότητας.", "The elderly villagers are the most enthusiastic. Some come to the school and tell the children stories from the old days, while a retired agronomist planted a vegetable garden with them in the yard. \"A village without children is a village without a future\", says the community president."),
 ],
 "questions": [
  Q("Γιατί ξανάνοιξε το σχολείο;", ["Γιατί το αποφάσισε το υπουργείο", "Γιατί στο χωριό εγκαταστάθηκαν τέσσερις οικογένειες με εννέα παιδιά", "Γιατί χτίστηκε καινούργιο κτίριο", "Γιατί έκλεισε το σχολείο της γειτονικής πόλης"], 1, "στο χωριό εγκαταστάθηκαν τέσσερις οικογένειες από την Αθήνα και την Πάτρα"),
  Q("Τι έκανε ο δήμος;", ["Πλήρωσε τα ενοίκια των οικογενειών", "Έφερε λεωφορείο για τα παιδιά", "Επισκεύασε τη σκεπή και έφερε καινούργιους υπολογιστές", "Προσέλαβε τρεις δασκάλους"], 2, "ο δήμος επισκεύασε τη σκεπή του σχολείου και έφερε καινούργιους υπολογιστές"),
  Q("Πώς συμμετέχουν οι ηλικιωμένοι του χωριού;", ["Διηγούνται ιστορίες στα παιδιά και ένας φύτεψε μαζί τους λαχανόκηπο", "Μαγειρεύουν για τα παιδιά", "Δίνουν χρήματα στο σχολείο", "Δεν συμμετέχουν καθόλου"], 0, "Κάποιοι έρχονται στο σχολείο και διηγούνται στα παιδιά ιστορίες από τα παλιά"),
 ],
 "gloss": {"ξανανοίγει": "ξανανοίγω — to reopen", "κουδούνι": "κουδούνι — bell", "εγκαταστάθηκαν": "εγκαθίσταμαι — to settle", "συνολικά": "συνολικά — in total", "από απόσταση": "από απόσταση — remotely", "ενοίκιο": "ενοίκιο — rent", "σκεπή": "σκεπή — roof", "ενθουσιασμένοι": "ενθουσιασμένος — enthusiastic", "γεωπόνος": "γεωπόνος — agronomist", "λαχανόκηπο": "λαχανόκηπος — vegetable garden"}
})

ITEMS.append({
 "id": "l120-mon-ksechasa-tin-kori-mou", "title": "Η μέρα που ξέχασα την κόρη μου στο πάρκο", "title_en": "The day I forgot my daughter at the park", "type": "monologue", "level": "B2",
 "context_el": "Ο Παναγιώτης, πατέρας δύο παιδιών, διηγείται σε μια εκπομπή για γονείς μια μέρα που δεν θα ξεχάσει ποτέ.",
 "script": [
  L("Παναγιώτης", "m", "Ήταν ένα Σάββατο απόγευμα. Είχα πάει στο πάρκο με τα δύο παιδιά, τον εξάχρονο Νικόλα και την τετράχρονη Μυρτώ. Ο Νικόλας χτύπησε το γόνατό του, άρχισε να κλαίει, και εγώ τον σήκωσα αγκαλιά και έτρεξα στο αυτοκίνητο για να του βάλω ένα τσιρότο.", "It was a Saturday afternoon. I'd gone to the park with the two children, six-year-old Nikolas and four-year-old Myrto. Nikolas banged his knee and started crying, and I picked him up and ran to the car to put a plaster on it."),
  L("Παναγιώτης", "m", "Τον έβαλα στο κάθισμα, του έδωσα ένα μπισκότο και ξεκίνησα για το σπίτι. Είχα κάνει περίπου δύο χιλιόμετρα, όταν ο Νικόλας με ρώτησε: «Μπαμπά, η Μυρτώ πού είναι;» Ένιωσα το αίμα μου να παγώνει.", "I put him in his seat, gave him a biscuit and set off for home. I'd gone about two kilometres when Nikolas asked me: \"Dad, where's Myrto?\" I felt my blood run cold."),
  L("Παναγιώτης", "m", "Γύρισα πίσω πιο γρήγορα από ποτέ. Η Μυρτώ καθόταν ήσυχη στην κούνια, μαζί με μια κυρία που την είχε δει μόνη και περίμενε μαζί της. Ούτε που είχε καταλάβει ότι έλειπα. Από εκείνη τη μέρα, πριν βάλω μπρος το αυτοκίνητο, μετράω πάντα φωναχτά: ένα, δύο.", "I went back faster than ever. Myrto was sitting quietly on the swing, together with a lady who had seen her alone and was waiting with her. She hadn't even noticed I was gone. Since that day, before I start the car, I always count out loud: one, two."),
 ],
 "questions": [
  Q("Γιατί έτρεξε ο Παναγιώτης στο αυτοκίνητο;", ["Γιατί άρχισε να βρέχει", "Για να βάλει τσιρότο στο γόνατο του Νικόλα", "Γιατί είχε ξεχάσει τα κλειδιά", "Γιατί είχε αργήσει για το σπίτι"], 1, "έτρεξα στο αυτοκίνητο για να του βάλω ένα τσιρότο"),
  Q("Πώς κατάλαβε ότι η Μυρτώ έλειπε;", ["Του τηλεφώνησε η γυναίκα του", "Την είδε στον καθρέφτη", "Τον ρώτησε ο Νικόλας πού είναι", "Του το είπε ένας γείτονας"], 2, "ο Νικόλας με ρώτησε: «Μπαμπά, η Μυρτώ πού είναι;»"),
  Q("Τι κάνει από τότε ο Παναγιώτης;", ["Μετράει φωναχτά τα παιδιά πριν βάλει μπρος το αυτοκίνητο", "Δεν πηγαίνει πια στο πάρκο", "Πηγαίνει μόνο με ένα παιδί κάθε φορά", "Ζητάει πάντα από τη γυναίκα του να έρχεται μαζί"], 0, "πριν βάλω μπρος το αυτοκίνητο, μετράω πάντα φωναχτά"),
 ],
 "gloss": {"γόνατό": "γόνατο — knee", "αγκαλιά": "αγκαλιά — in one's arms", "τσιρότο": "τσιρότο — plaster, band-aid", "κάθισμα": "κάθισμα — (car) seat", "παγώνει": "παγώνω — to freeze, run cold", "κούνια": "κούνια — swing", "βάλω μπρος": "βάζω μπρος — to start (an engine)", "φωναχτά": "φωναχτά — out loud"}
})

ITEMS.append({
 "id": "l120-mon-kamino", "title": "Περπάτησα το Καμίνο του Σαντιάγο", "title_en": "I walked the Camino de Santiago", "type": "monologue", "level": "B2",
 "context_el": "Η Ειρήνη, μια φαρμακοποιός πενήντα δύο χρονών, μιλάει για το προσκύνημα που έκανε με τα πόδια στη βόρεια Ισπανία.",
 "script": [
  L("Ειρήνη", "f", "Μετά από ένα δύσκολο διαζύγιο, ένιωθα ότι χρειαζόμουν χρόνο μόνη μου. Μια φίλη μού μίλησε για το Καμίνο του Σαντιάγο, ένα πανάρχαιο προσκύνημα που καταλήγει στον καθεδρικό ναό του Σαντιάγο ντε Κομποστέλα. Αποφάσισα να περπατήσω τα τελευταία τριακόσια χιλιόμετρα.", "After a difficult divorce, I felt I needed time on my own. A friend told me about the Camino de Santiago, an age-old pilgrimage that ends at the cathedral of Santiago de Compostela. I decided to walk the last three hundred kilometres."),
  L("Ειρήνη", "f", "Περπατούσα περίπου είκοσι πέντε χιλιόμετρα τη μέρα και κοιμόμουν σε ξενώνες για προσκυνητές, σε μεγάλα δωμάτια με κουκέτες. Κάθε βράδυ έπαιρνα μια σφραγίδα σε ένα μικρό βιβλιαράκι, το «διαβατήριο του προσκυνητή». Τις πρώτες μέρες οι φουσκάλες στα πόδια μου ήταν τόσες, που σκέφτηκα να τα παρατήσω.", "I walked about twenty-five kilometres a day and slept in hostels for pilgrims, in large rooms with bunk beds. Every evening I got a stamp in a small booklet, the \"pilgrim's passport\". In the first days I had so many blisters on my feet that I thought of giving up."),
  L("Ειρήνη", "f", "Αυτό που με κράτησε ήταν οι άνθρωποι. Περπάτησα με μια Κορεάτισσα δασκάλα, με έναν Ιταλό συνταξιούχο, με δύο Γερμανούς φοιτητές. Μιλούσαμε για όλα, ή δεν μιλούσαμε καθόλου. Όταν έφτασα στον καθεδρικό, έκλαψα. Όχι από κούραση, αλλά γιατί κατάλαβα ότι μπορώ να συνεχίσω μόνη μου.", "What kept me going was the people. I walked with a Korean teacher, with an Italian pensioner, with two German students. We talked about everything, or we didn't talk at all. When I reached the cathedral, I cried. Not from tiredness, but because I realised I could go on on my own."),
 ],
 "questions": [
  Q("Γιατί αποφάσισε η Ειρήνη να κάνει το Καμίνο;", ["Για να γράψει ένα βιβλίο", "Γιατί ένιωθε ότι χρειαζόταν χρόνο μόνη της μετά από ένα δύσκολο διαζύγιο", "Γιατί της το πρότεινε ο γιατρός", "Για να χάσει βάρος"], 1, "ένιωθα ότι χρειαζόμουν χρόνο μόνη μου"),
  Q("Τι ήταν το «διαβατήριο του προσκυνητή»;", ["Μια ειδική βίζα", "Ένας χάρτης της διαδρομής", "Ένα βιβλιαράκι όπου έπαιρνε σφραγίδα κάθε βράδυ", "Ένα εισιτήριο για τους ξενώνες"], 2, "Κάθε βράδυ έπαιρνα μια σφραγίδα σε ένα μικρό βιβλιαράκι"),
  Q("Γιατί έκλαψε όταν έφτασε στον καθεδρικό;", ["Γιατί κατάλαβε ότι μπορεί να συνεχίσει μόνη της", "Από την κούραση", "Γιατί έπρεπε να αποχαιρετήσει τους φίλους της", "Γιατί ο ναός ήταν κλειστός"], 0, "γιατί κατάλαβα ότι μπορώ να συνεχίσω μόνη μου"),
 ],
 "gloss": {"φαρμακοποιός": "φαρμακοποιός — pharmacist", "προσκύνημα": "προσκύνημα — pilgrimage", "διαζύγιο": "διαζύγιο — divorce", "πανάρχαιο": "πανάρχαιος — age-old, ancient", "καθεδρικό ναό": "καθεδρικός ναός — cathedral", "ξενώνες": "ξενώνας — hostel, guesthouse", "προσκυνητές": "προσκυνητής — pilgrim", "κουκέτες": "κουκέτα — bunk bed", "σφραγίδα": "σφραγίδα — stamp", "φουσκάλες": "φουσκάλα — blister"}
})

ITEMS.append({
 "id": "l120-c1-glossa-kai-skepsi", "title": "Μας διαμορφώνει η γλώσσα που μιλάμε;", "title_en": "Does the language we speak shape us?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν ψυχογλωσσολόγο σε μια διάλεξη για τη σχέση γλώσσας και σκέψης.",
 "script": [
  L("Ψυχογλωσσολόγος", "m", "Επηρεάζει η γλώσσα που μιλάμε τον τρόπο που σκεφτόμαστε; Η ιδέα συνδέεται με τους Αμερικανούς γλωσσολόγους Έντουαρντ Σάπιρ και Μπέντζαμιν Γουόρφ και είναι γνωστή ως «γλωσσική σχετικότητα». Στην ακραία της μορφή, υποστηρίζει ότι η γλώσσα καθορίζει τη σκέψη, ότι δηλαδή δεν μπορούμε να σκεφτούμε κάτι για το οποίο δεν έχουμε λέξη. Η μορφή αυτή έχει σήμερα εγκαταλειφθεί από τους περισσότερους ερευνητές.", "Does the language we speak influence the way we think? The idea is linked to the American linguists Edward Sapir and Benjamin Whorf and is known as \"linguistic relativity\". In its extreme form, it argues that language determines thought, that is, that we can't think of something for which we have no word. This form has now been abandoned by most researchers."),
  L("Ψυχογλωσσολόγος", "m", "Μια ηπιότερη εκδοχή, ότι η γλώσσα επηρεάζει ορισμένες πτυχές της αντίληψης, βρίσκει όμως στήριξη σε πειράματα. Ένα παράδειγμα αφορά εμάς άμεσα. Τα ελληνικά, όπως και τα ρωσικά, έχουν δύο βασικές λέξεις για το μπλε: το «γαλάζιο» και το «μπλε». Σε μια μελέτη του 2009, ερευνητές κατέγραψαν την εγκεφαλική δραστηριότητα Ελλήνων και Άγγλων και διαπίστωσαν ότι οι Έλληνες αντιδρούσαν πιο έντονα στη διαφορά ανάμεσα στο ανοιχτό και στο σκούρο μπλε.", "A milder version, that language influences certain aspects of perception, does however find support in experiments. One example concerns us directly. Greek, like Russian, has two basic words for blue: \"galazio\" and \"ble\". In a 2009 study, researchers recorded the brain activity of Greek and English speakers and found that the Greeks reacted more strongly to the difference between light and dark blue."),
  L("Ψυχογλωσσολόγος", "m", "Ένα ακόμη πιο εντυπωσιακό παράδειγμα έρχεται από ορισμένες γλώσσες της Αυστραλίας, που δεν χρησιμοποιούν λέξεις όπως «δεξιά» και «αριστερά», αλλά μόνο τα σημεία του ορίζοντα. Οι ομιλητές τους λένε, για παράδειγμα, «έχεις ένα μυρμήγκι στο νότιο πόδι σου». Σύμφωνα με τους ερευνητές, οι άνθρωποι αυτοί έχουν έναν εντυπωσιακό προσανατολισμό: ξέρουν πού είναι ο βορράς ακόμη και μέσα σε ένα άγνωστο κτίριο.", "An even more striking example comes from certain languages of Australia, which don't use words like \"right\" and \"left\", but only the points of the compass. Their speakers say, for example, \"there's an ant on your southern leg\". According to the researchers, these people have an impressive sense of direction: they know where north is even inside an unfamiliar building."),
  L("Ψυχογλωσσολόγος", "m", "Τι σημαίνουν όλα αυτά; Όχι ότι είμαστε φυλακισμένοι στη γλώσσα μας. Μπορούμε να μάθουμε νέες λέξεις και νέους τρόπους να βλέπουμε τον κόσμο. Ίσως μάλιστα αυτό να είναι το μεγαλύτερο δώρο της εκμάθησης μιας ξένης γλώσσας: δεν μαθαίνουμε μόνο νέες λέξεις, αλλά και μια νέα ματιά.", "What does all this mean? Not that we are prisoners of our language. We can learn new words and new ways of seeing the world. Perhaps that is in fact the greatest gift of learning a foreign language: we don't just learn new words, but also a new way of looking."),
 ],
 "questions": [
  Q("Τι ισχύει για την ακραία μορφή της γλωσσικής σχετικότητας;", ["Επιβεβαιώθηκε από πολλά πειράματα", "Έχει σήμερα εγκαταλειφθεί από τους περισσότερους ερευνητές", "Τη διατύπωσαν πρόσφατα Έλληνες ερευνητές", "Αφορά μόνο τα χρώματα"], 1, "Η μορφή αυτή έχει σήμερα εγκαταλειφθεί από τους περισσότερους ερευνητές"),
  Q("Τι έδειξε η μελέτη του 2009;", ["Ότι οι Άγγλοι βλέπουν περισσότερα χρώματα", "Ότι το μπλε είναι το αγαπημένο χρώμα των Ελλήνων", "Ότι οι Έλληνες αντιδρούσαν πιο έντονα στη διαφορά ανάμεσα στο ανοιχτό και στο σκούρο μπλε", "Ότι οι Ρώσοι και οι Έλληνες έχουν τις ίδιες λέξεις για τα χρώματα"], 2, "οι Έλληνες αντιδρούσαν πιο έντονα στη διαφορά ανάμεσα στο ανοιχτό και στο σκούρο μπλε"),
  Q("Τι χαρακτηρίζει τους ομιλητές ορισμένων γλωσσών της Αυστραλίας;", ["Έχουν εντυπωσιακό προσανατολισμό", "Δεν έχουν λέξεις για τα χρώματα", "Μιλούν πολύ αργά", "Χρησιμοποιούν μόνο χειρονομίες"], 0, "οι άνθρωποι αυτοί έχουν έναν εντυπωσιακό προσανατολισμό"),
  Q("Ποιο είναι, κατά τον ομιλητή, ίσως το μεγαλύτερο δώρο της εκμάθησης μιας ξένης γλώσσας;", ["Οι καλύτερες επαγγελματικές ευκαιρίες", "Τα ταξίδια", "Η καλύτερη μνήμη", "Μια νέα ματιά στον κόσμο"], 3, "δεν μαθαίνουμε μόνο νέες λέξεις, αλλά και μια νέα ματιά"),
 ],
 "gloss": {"ψυχογλωσσολόγο": "ψυχογλωσσολόγος — psycholinguist", "διάλεξη": "διάλεξη — lecture", "σχετικότητα": "σχετικότητα — relativity", "ακραία": "ακραίος — extreme", "καθορίζει": "καθορίζω — to determine", "εγκαταλειφθεί": "εγκαταλείπομαι — to be abandoned", "ηπιότερη": "ήπιος — mild; ηπιότερος milder", "πτυχές": "πτυχή — aspect", "αντίληψης": "αντίληψη — perception", "εγκεφαλική": "εγκεφαλικός — brain (adj.)", "σημεία του ορίζοντα": "σημεία του ορίζοντα — points of the compass", "μυρμήγκι": "μυρμήγκι — ant", "προσανατολισμό": "προσανατολισμός — sense of direction", "φυλακισμένοι": "φυλακισμένος — imprisoned"}
})

ITEMS.append({
 "id": "l120-c1-naumachia-nafpaktou", "title": "Η ναυμαχία της Ναυπάκτου (1571)", "title_en": "The Battle of Lepanto (1571)", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια ιστορικό σε εκπομπή για τη Μεσόγειο στα χρόνια της Βενετοκρατίας και της Τουρκοκρατίας.",
 "script": [
  L("Δημοσιογράφος", "m", "Στην Ευρώπη τη λένε «μάχη του Λεπάντο». Εμείς τη λέμε «ναυμαχία της Ναυπάκτου». Έγινε όμως πράγματι στη Ναύπακτο;", "In Europe they call it the \"Battle of Lepanto\". We call it the \"naval battle of Nafpaktos\". But did it really take place at Nafpaktos?"),
  L("Ιστορικός", "f", "Όχι ακριβώς. Ο οθωμανικός στόλος είχε τη βάση του στη Ναύπακτο, που οι Ιταλοί ονόμαζαν Λεπάντο, αλλά η σύγκρουση έγινε δυτικότερα, στην είσοδο του Πατραϊκού κόλπου, κοντά στις Εχινάδες νήσους. Ήταν 7 Οκτωβρίου 1571. Απέναντι στους Οθωμανούς βρισκόταν ο στόλος της Ιερής Συμμαχίας, ένας συνασπισμός με επικεφαλής την Ισπανία, τη Βενετία και τον Πάπα, υπό τη διοίκηση του νεαρού Δον Χουάν της Αυστρίας.", "Not exactly. The Ottoman fleet had its base at Nafpaktos, which the Italians called Lepanto, but the clash took place further west, at the entrance to the Gulf of Patras, near the Echinades islands. It was 7 October 1571. Facing the Ottomans was the fleet of the Holy League, a coalition led by Spain, Venice and the Pope, under the command of the young Don John of Austria."),
  L("Δημοσιογράφος", "m", "Ποια ήταν η σημασία της;", "What was its significance?"),
  L("Ιστορικός", "f", "Ήταν η πρώτη μεγάλη ήττα του οθωμανικού στόλου και είχε τεράστιο ψυχολογικό αντίκτυπο στην Ευρώπη, που πίστευε ως τότε ότι οι Οθωμανοί ήταν ανίκητοι στη θάλασσα. Ήταν επίσης η τελευταία μεγάλη ναυμαχία με κωπήλατα πλοία, τις γαλέρες. Στρατηγικά, ωστόσο, τα αποτελέσματα ήταν περιορισμένα: μέσα σε έναν χρόνο ο σουλτάνος είχε ξαναχτίσει τον στόλο του, και η Κύπρος, που είχε μόλις κατακτηθεί, παρέμεινε οθωμανική.", "It was the first major defeat of the Ottoman fleet and had an enormous psychological impact on Europe, which until then believed the Ottomans were invincible at sea. It was also the last great naval battle fought with oared ships, the galleys. Strategically, however, the results were limited: within a year the sultan had rebuilt his fleet, and Cyprus, which had just been conquered, remained Ottoman."),
  L("Δημοσιογράφος", "m", "Ποια ήταν η θέση των Ελλήνων;", "What was the position of the Greeks?"),
  L("Ιστορικός", "f", "Ιδιαίτερα τραγική. Χιλιάδες Έλληνες κωπηλάτες και ναύτες υπηρετούσαν και στους δύο στόλους, άλλοι ως υπήκοοι της Βενετίας, άλλοι ως υπήκοοι του σουλτάνου, συχνά με τη βία. Έτσι, στην ίδια ναυμαχία, Έλληνες βρέθηκαν να πολεμούν απέναντι σε Έλληνες. Ας θυμηθούμε, τέλος, ότι στη μάχη τραυματίστηκε ένας νεαρός Ισπανός στρατιώτης, που έχασε τη χρήση του αριστερού του χεριού: ο Μιγκέλ ντε Θερβάντες, ο μετέπειτα συγγραφέας του «Δον Κιχώτη».", "Particularly tragic. Thousands of Greek oarsmen and sailors served in both fleets, some as subjects of Venice, others as subjects of the sultan, often by force. So in the same battle, Greeks found themselves fighting against Greeks. Let's remember, finally, that a young Spanish soldier was wounded in the battle and lost the use of his left hand: Miguel de Cervantes, the future author of Don Quixote."),
 ],
 "questions": [
  Q("Πού έγινε πραγματικά η ναυμαχία;", ["Μέσα στο λιμάνι της Ναυπάκτου", "Στην είσοδο του Πατραϊκού κόλπου, κοντά στις Εχινάδες", "Έξω από την Κύπρο", "Στο Ιόνιο, κοντά στην Κέρκυρα"], 1, "στην είσοδο του Πατραϊκού κόλπου, κοντά στις Εχινάδες νήσους"),
  Q("Γιατί, κατά την ιστορικό, τα στρατηγικά αποτελέσματα ήταν περιορισμένα;", ["Γιατί η Ιερή Συμμαχία διαλύθηκε αμέσως", "Γιατί η Βενετία έχασε τα πλοία της", "Γιατί μέσα σε έναν χρόνο ο σουλτάνος ξανάχτισε τον στόλο του και η Κύπρος παρέμεινε οθωμανική", "Γιατί ο Δον Χουάν σκοτώθηκε"], 2, "μέσα σε έναν χρόνο ο σουλτάνος είχε ξαναχτίσει τον στόλο του"),
  Q("Γιατί ήταν τραγική η θέση των Ελλήνων;", ["Γιατί υπηρετούσαν και στους δύο στόλους και πολέμησαν μεταξύ τους", "Γιατί δεν τους επέτρεψαν να πολεμήσουν", "Γιατί η Ναύπακτος καταστράφηκε", "Γιατί έχασαν τα νησιά τους"], 0, "στην ίδια ναυμαχία, Έλληνες βρέθηκαν να πολεμούν απέναντι σε Έλληνες"),
  Q("Ποιος τραυματίστηκε στη ναυμαχία, σύμφωνα με την ιστορικό;", ["Ο Δον Χουάν της Αυστρίας", "Ο Πάπας", "Ο σουλτάνος", "Ο Μιγκέλ ντε Θερβάντες"], 3, "ο Μιγκέλ ντε Θερβάντες, ο μετέπειτα συγγραφέας του «Δον Κιχώτη»"),
 ],
 "gloss": {"ναυμαχία": "ναυμαχία — naval battle", "Βενετοκρατίας": "Βενετοκρατία — Venetian rule", "σύγκρουση": "σύγκρουση — clash", "Ιερής Συμμαχίας": "Ιερή Συμμαχία — the Holy League", "συνασπισμός": "συνασπισμός — coalition", "επικεφαλής": "επικεφαλής — at the head of, leader", "αντίκτυπο": "αντίκτυπος — impact", "ανίκητοι": "ανίκητος — invincible", "κωπήλατα": "κωπήλατος — oared", "γαλέρες": "γαλέρα — galley", "υπήκοοι": "υπήκοος — subject (of a state)", "μετέπειτα": "μετέπειτα — later, future"}
})

rnd = random.Random(120)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-120.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
