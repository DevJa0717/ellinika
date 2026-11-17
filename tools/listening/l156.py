# Source for library/listening/listening-156.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l156.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l156-vm-karnagio", "title": "Η βάρκα σας είναι έτοιμη", "title_en": "Your boat is ready", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από ένα καρνάγιο, όπου έχετε αφήσει τη βάρκα σας για επισκευή.",
 "script": [
  L("Μάστορας", "m", "Γεια σας, ο Παντελής από το καρνάγιο. Σας παίρνω για τη βάρκα σας. Τελειώσαμε την επισκευή στο πάτωμα, αλλάξαμε δύο σάπιες σανίδες και βάψαμε το κάτω μέρος με ειδική μπογιά, για να μην πιάνουν πάνω της στρείδια και φύκια.", "Hello, it's Pantelis from the boatyard. I'm calling about your boat. We've finished the repair on the floor, replaced two rotten planks and painted the bottom with special paint, so that oysters and seaweed don't stick to it."),
  L("Μάστορας", "m", "Η μπογιά θέλει τρεις μέρες για να στεγνώσει καλά, οπότε τη βάρκα μπορούμε να τη ρίξουμε στη θάλασσα από την Πέμπτη και μετά. Αν θέλετε να είστε κι εσείς εκεί, πείτε μου ποια ώρα σας βολεύει.", "The paint needs three days to dry properly, so we can put the boat in the water from Thursday onwards. If you want to be there too, tell me what time suits you."),
  L("Μάστορας", "m", "Κάτι ακόμα: η μηχανή θέλει σέρβις, γιατί το νερό που βγάζει είναι πολύ λίγο. Δεν το κάναμε, γιατί δεν ήταν στη συμφωνία μας. Αν θέλετε, το αναλαμβάνει ένας συνεργάτης μου, που έρχεται εδώ κάθε Τρίτη.", "One more thing: the engine needs a service, because very little water comes out of it. We didn't do it, because it wasn't part of our agreement. If you like, a colleague of mine who comes here every Tuesday can take care of it."),
 ],
 "questions": [
  Q("Γιατί βάψανε το κάτω μέρος της βάρκας με ειδική μπογιά;", ["Για να είναι πιο γρήγορη", "Για να μην πιάνουν πάνω της στρείδια και φύκια", "Για να φαίνεται τη νύχτα", "Για να μην τη χτυπάει ο ήλιος"], 1, "για να μην πιάνουν πάνω της στρείδια και φύκια"),
  Q("Από πότε μπορεί η βάρκα να μπει στη θάλασσα;", ["Από αύριο", "Από την Τρίτη", "Από την Πέμπτη και μετά", "Από την άλλη εβδομάδα"], 2, "μπορούμε να τη ρίξουμε στη θάλασσα από την Πέμπτη και μετά"),
  Q("Γιατί δεν έκαναν σέρβις στη μηχανή;", ["Γιατί δεν ήταν στη συμφωνία τους", "Γιατί έλειπε ένα ανταλλακτικό", "Γιατί η μηχανή είναι καινούργια", "Γιατί δεν είχαν χρόνο"], 0, "Δεν το κάναμε, γιατί δεν ήταν στη συμφωνία μας"),
 ],
 "gloss": {"καρνάγιο": "καρνάγιο — boatyard", "σάπιες": "σάπιος — rotten", "σανίδες": "σανίδα — plank", "μπογιά": "μπογιά — paint", "στρείδια": "στρείδι — oyster", "φύκια": "φύκι — seaweed", "στεγνώσει": "στεγνώνω — to dry", "ρίξουμε": "ρίχνω (στη θάλασσα) — to launch", "σέρβις": "σέρβις — service", "αναλαμβάνει": "αναλαμβάνω — to take on"}
})

ITEMS.append({
 "id": "l156-ann-louna-park", "title": "Ανακοίνωση στο λούνα παρκ", "title_en": "An announcement at the funfair", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός λούνα παρκ.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί επισκέπτες, λόγω των ισχυρών ανέμων, η ρόδα και τα δύο ψηλά παιχνίδια δίπλα στη λίμνη σταματούν να λειτουργούν προσωρινά. Θα ξαναλειτουργήσουν μόλις ο άνεμος πέσει κάτω από το όριο ασφαλείας.", "Dear visitors, because of the strong winds, the Ferris wheel and the two tall rides next to the lake are temporarily stopping. They will run again as soon as the wind drops below the safety limit."),
  L("Εκφωνήτρια", "f", "Όσοι έχετε ήδη αγοράσει εισιτήριο για αυτά τα παιχνίδια, μπορείτε να το χρησιμοποιήσετε σε οποιοδήποτε άλλο παιχνίδι ή να το κρατήσετε για την επόμενη επίσκεψή σας, μέσα σε έναν μήνα. Χρήματα δεν επιστρέφονται.", "Those of you who have already bought a ticket for these rides can use it on any other ride or keep it for your next visit, within a month. Money is not refunded."),
  L("Εκφωνήτρια", "f", "Στο μεταξύ, σας περιμένουμε στο κλειστό θέατρο, όπου στις έξι ξεκινά παράσταση με ταχυδακτυλουργό. Η είσοδος για τα παιδιά κάτω των δώδεκα είναι δωρεάν. Ευχαριστούμε για την κατανόηση.", "In the meantime, we look forward to seeing you at the indoor theatre, where a magic show starts at six. Entry for children under twelve is free. Thank you for your understanding."),
 ],
 "questions": [
  Q("Γιατί σταματούν να λειτουργούν ορισμένα παιχνίδια;", ["Λόγω βλάβης", "Λόγω των ισχυρών ανέμων", "Λόγω βροχής", "Επειδή κλείνει το λούνα παρκ"], 1, "λόγω των ισχυρών ανέμων"),
  Q("Τι μπορούν να κάνουν όσοι έχουν ήδη εισιτήριο για αυτά τα παιχνίδια;", ["Να πάρουν πίσω τα χρήματά τους", "Να το χρησιμοποιήσουν μόνο αύριο", "Να το χρησιμοποιήσουν σε άλλο παιχνίδι ή σε επόμενη επίσκεψη μέσα σε έναν μήνα", "Να το ανταλλάξουν με φαγητό"], 2, "μπορείτε να το χρησιμοποιήσετε σε οποιοδήποτε άλλο παιχνίδι"),
  Q("Τι γίνεται στις έξι;", ["Παράσταση με ταχυδακτυλουργό στο κλειστό θέατρο", "Ξανανοίγει η ρόδα", "Κλείνει το λούνα παρκ", "Πυροτεχνήματα δίπλα στη λίμνη"], 0, "στις έξι ξεκινά παράσταση με ταχυδακτυλουργό"),
 ],
 "gloss": {"λούνα παρκ": "λούνα παρκ — funfair, amusement park", "ισχυρών": "ισχυρός — strong", "ρόδα": "ρόδα — (Ferris) wheel", "προσωρινά": "προσωρινά — temporarily", "όριο ασφαλείας": "όριο ασφαλείας — safety limit", "επιστρέφονται": "επιστρέφομαι — to be refunded", "ταχυδακτυλουργό": "ταχυδακτυλουργός — magician", "κατανόηση": "κατανόηση — understanding"}
})

ITEMS.append({
 "id": "l156-dia-kataskinosi-i-giagia", "title": "Κατασκήνωση ή γιαγιά;", "title_en": "Summer camp or grandma's?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο γονείς να συζητούν πού θα περάσει ο γιος τους, ο Άρης, τον Ιούλιο.",
 "script": [
  L("Κατερίνα", "f", "Είδα ότι η κατασκήνωση στην Πιερία έχει ακόμα θέσεις για τη δεύτερη περίοδο, από τις εννιά ως τις είκοσι τρεις Ιουλίου. Ο Άρης είναι πια δέκα χρονών, νομίζω ότι είναι έτοιμος.", "I saw that the camp in Pieria still has places for the second session, from the ninth to the twenty-third of July. Aris is ten now; I think he's ready."),
  L("Μιχάλης", "m", "Δεν ξέρω. Πέρσι, στη σχολική εκδρομή με διανυκτέρευση, μας πήρε τηλέφωνο κλαίγοντας στις έντεκα το βράδυ. Και η μάνα μου περιμένει να πάει στο χωριό, όπως κάθε χρόνο.", "I don't know. Last year, on the overnight school trip, he called us crying at eleven at night. And my mother is expecting him to go to the village, like every year."),
  L("Κατερίνα", "f", "Ναι, αλλά στο χωριό δεν υπάρχει κανένα παιδί της ηλικίας του, και περνάει όλη τη μέρα με το τάμπλετ. Στην κατασκήνωση θα κάνει κολύμπι, θα κάνει φίλους, θα μάθει να τα βγάζει πέρα μόνος του.", "Yes, but there isn't a single child his age in the village, and he spends the whole day on the tablet. At camp he'll swim, make friends, learn to manage on his own."),
  L("Μιχάλης", "m", "Εντάξει, ας το ρωτήσουμε πρώτα τον ίδιο. Κι αν θέλει, να πάει και στη γιαγιά του τον Αύγουστο, για μια εβδομάδα, να μη στενοχωρηθεί.", "All right, let's ask him first. And if he wants, he can go to his grandmother in August too, for a week, so she won't be upset."),
 ],
 "questions": [
  Q("Γιατί ο Μιχάλης έχει αμφιβολίες για την κατασκήνωση;", ["Γιατί είναι ακριβή", "Γιατί πέρσι ο Άρης τους πήρε τηλέφωνο κλαίγοντας στη σχολική εκδρομή", "Γιατί η κατασκήνωση είναι μακριά", "Γιατί ο Άρης δεν ξέρει κολύμπι"], 1, "μας πήρε τηλέφωνο κλαίγοντας στις έντεκα το βράδυ"),
  Q("Ποιο πρόβλημα βλέπει η Κατερίνα στο χωριό;", ["Δεν υπάρχει ίντερνετ", "Κάνει πολλή ζέστη", "Δεν υπάρχει κανένα παιδί της ηλικίας του και περνάει τη μέρα με το τάμπλετ", "Η γιαγιά είναι άρρωστη"], 2, "στο χωριό δεν υπάρχει κανένα παιδί της ηλικίας του"),
  Q("Τι αποφασίζουν;", ["Να ρωτήσουν πρώτα τον Άρη", "Να τον γράψουν αμέσως στην κατασκήνωση", "Να πάει μόνο στη γιαγιά", "Να μείνει στο σπίτι"], 0, "ας το ρωτήσουμε πρώτα τον ίδιο"),
 ],
 "gloss": {"κατασκήνωση": "κατασκήνωση — summer camp", "περίοδο": "περίοδος — session, period", "διανυκτέρευση": "διανυκτέρευση — overnight stay", "κλαίγοντας": "κλαίω — to cry", "τάμπλετ": "τάμπλετ — tablet", "τα βγάζει πέρα": "τα βγάζω πέρα — to manage, cope", "στενοχωρηθεί": "στενοχωριέμαι — to be upset"}
})

ITEMS.append({
 "id": "l156-int-ippotherapeftria", "title": "Μια ιπποθεραπεύτρια", "title_en": "A hippotherapist", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από μια ραδιοφωνική συνέντευξη με μια φυσικοθεραπεύτρια που κάνει θεραπεία με άλογα.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς είναι η ιπποθεραπεία;", "What exactly is hippotherapy?"),
  L("Μυρτώ", "f", "Είναι μια μορφή φυσικοθεραπείας όπου χρησιμοποιούμε την κίνηση του αλόγου. Όταν το άλογο περπατάει, η λεκάνη του αναβάτη κινείται με τρόπο πολύ παρόμοιο με αυτόν του ανθρώπινου βαδίσματος. Έτσι, παιδιά που δυσκολεύονται να περπατήσουν δυναμώνουν τους μυς τους και βελτιώνουν την ισορροπία τους.", "It's a form of physiotherapy in which we use the movement of the horse. When the horse walks, the rider's pelvis moves in a way very similar to human walking. So children who find it hard to walk strengthen their muscles and improve their balance."),
  L("Δημοσιογράφος", "m", "Και τα παιδιά δεν φοβούνται;", "And aren't the children afraid?"),
  L("Μυρτώ", "f", "Κάποια στην αρχή, ναι. Γι' αυτό το πρώτο μάθημα δεν ανεβαίνουν καθόλου· απλώς χαϊδεύουν το άλογο και του δίνουν ένα καρότο. Τα άλογά μας είναι ήρεμα και ειδικά εκπαιδευμένα. Το πιο συγκινητικό για μένα είναι όταν ένα παιδί που δεν μιλάει πολύ αρχίζει να μιλάει στο άλογο. Πολλές φορές οι γονείς μάς λένε ότι το παιδί περιμένει όλη την εβδομάδα τη μέρα του μαθήματος.", "Some at first, yes. That's why in the first lesson they don't get on at all; they just stroke the horse and give it a carrot. Our horses are calm and specially trained. The most moving thing for me is when a child who doesn't talk much starts talking to the horse. Parents often tell us that their child waits all week for the day of the lesson."),
 ],
 "questions": [
  Q("Γιατί η κίνηση του αλόγου βοηθάει τα παιδιά;", ["Γιατί τα κουράζει", "Γιατί είναι διασκεδαστική", "Γιατί η λεκάνη του αναβάτη κινείται όπως στο ανθρώπινο βάδισμα", "Γιατί τα μαθαίνει να τρέχουν"], 2, "η λεκάνη του αναβάτη κινείται με τρόπο πολύ παρόμοιο με αυτόν του ανθρώπινου βαδίσματος"),
  Q("Τι κάνουν τα παιδιά στο πρώτο μάθημα;", ["Χαϊδεύουν το άλογο και του δίνουν ένα καρότο", "Κάνουν μια μικρή βόλτα", "Μαθαίνουν να καθαρίζουν το άλογο", "Βλέπουν άλλα παιδιά να κάνουν ιππασία"], 0, "απλώς χαϊδεύουν το άλογο και του δίνουν ένα καρότο"),
  Q("Τι είναι το πιο συγκινητικό για τη Μυρτώ;", ["Όταν ένα παιδί καβαλάει μόνο του", "Όταν οι γονείς την ευχαριστούν", "Όταν ένα παιδί περπατάει για πρώτη φορά", "Όταν ένα παιδί που δεν μιλάει πολύ αρχίζει να μιλάει στο άλογο"], 3, "όταν ένα παιδί που δεν μιλάει πολύ αρχίζει να μιλάει στο άλογο"),
 ],
 "gloss": {"ιπποθεραπεία": "ιπποθεραπεία — hippotherapy", "μορφή": "μορφή — form", "λεκάνη": "λεκάνη — pelvis", "αναβάτη": "αναβάτης — rider", "βαδίσματος": "βάδισμα — walking, gait", "μυς": "μυς — muscle(s)", "ισορροπία": "ισορροπία — balance", "χαϊδεύουν": "χαϊδεύω — to stroke", "εκπαιδευμένα": "εκπαιδευμένος — trained", "συγκινητικό": "συγκινητικός — moving, touching"}
})

ITEMS.append({
 "id": "l156-news-laografiko-mouseio", "title": "Λαογραφικό μουσείο στο παλιό σχολείο", "title_en": "A folk museum in the old school", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα τοπικό δελτίο ειδήσεων.",
 "script": [
  L("Εκφωνητής", "m", "Τις πόρτες του ανοίγει την Κυριακή το λαογραφικό μουσείο ενός ορεινού χωριού της περιοχής μας, στο κτίριο του παλιού δημοτικού σχολείου, που είχε κλείσει το 1989 λόγω έλλειψης μαθητών.", "The folk museum of a mountain village in our area opens its doors on Sunday, in the building of the old primary school, which had closed in 1989 for lack of pupils."),
  L("Εκφωνητής", "m", "Τα περισσότερα από τα πεντακόσια εκθέματα τα έφεραν οι ίδιοι οι κάτοικοι: αργαλειοί, γεωργικά εργαλεία, φορεσιές, φωτογραφίες, ακόμα και τα παλιά θρανία και ο μαυροπίνακας του σχολείου, που βρέθηκαν σε μια αποθήκη της κοινότητας.", "Most of the five hundred exhibits were brought by the villagers themselves: looms, farming tools, costumes, photographs, even the school's old desks and blackboard, which were found in a community storeroom."),
  L("Εκφωνητής", "m", "Το μουσείο θα λειτουργεί τα Σαββατοκύριακα, με εθελοντές ξεναγούς, ενώ τις καθημερινές θα δέχεται σχολικές ομάδες μόνο κατόπιν ραντεβού. Στα εγκαίνια θα παρουσιαστεί και ένα βίντεο με μαρτυρίες των τελευταίων μαθητών του σχολείου.", "The museum will open at weekends, with volunteer guides, while on weekdays it will receive school groups by appointment only. At the opening, a video with testimonies from the school's last pupils will also be shown."),
 ],
 "questions": [
  Q("Γιατί είχε κλείσει το σχολείο;", ["Λόγω σεισμού", "Λόγω έλλειψης μαθητών", "Γιατί χτίστηκε καινούργιο", "Γιατί έλειπαν δάσκαλοι"], 1, "που είχε κλείσει το 1989 λόγω έλλειψης μαθητών"),
  Q("Από πού προέρχονται τα περισσότερα εκθέματα;", ["Από ένα μουσείο της Αθήνας", "Από ανασκαφές", "Από αγορές σε παζάρια", "Τα έφεραν οι ίδιοι οι κάτοικοι"], 3, "Τα περισσότερα από τα πεντακόσια εκθέματα τα έφεραν οι ίδιοι οι κάτοικοι"),
  Q("Πώς μπορούν να το επισκεφθούν τα σχολεία;", ["Οποιαδήποτε μέρα χωρίς ραντεβού", "Μόνο τα Σαββατοκύριακα", "Τις καθημερινές, μόνο κατόπιν ραντεβού", "Μόνο την ημέρα των εγκαινίων"], 2, "τις καθημερινές θα δέχεται σχολικές ομάδες μόνο κατόπιν ραντεβού"),
 ],
 "gloss": {"λαογραφικό": "λαογραφικός — folk(lore)", "έλλειψης": "έλλειψη — lack", "εκθέματα": "έκθεμα — exhibit", "αργαλειοί": "αργαλειός — loom", "φορεσιές": "φορεσιά — (traditional) costume", "θρανία": "θρανίο — school desk", "μαυροπίνακας": "μαυροπίνακας — blackboard", "κατόπιν ραντεβού": "κατόπιν ραντεβού — by appointment", "εγκαίνια": "εγκαίνια — opening, inauguration", "μαρτυρίες": "μαρτυρία — testimony"}
})

ITEMS.append({
 "id": "l156-mono-pontiaka", "title": "Μαθαίνοντας ποντιακά από τη γιαγιά", "title_en": "Learning Pontic Greek from grandma", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν νέο άνδρα να μιλάει σε ένα podcast για τη γλώσσα της γιαγιάς του.",
 "script": [
  L("Γιώργος", "m", "Η γιαγιά μου μιλούσε ποντιακά με τις φίλες της, αλλά με εμάς, τα εγγόνια, μιλούσε πάντα κοινά ελληνικά. Όταν ήμουν μικρός, νόμιζα ότι τα ποντιακά ήταν μια μυστική γλώσσα για τους μεγάλους.", "My grandmother spoke Pontic with her friends, but with us, the grandchildren, she always spoke standard Greek. When I was little, I thought Pontic was a secret language for grown-ups."),
  L("Γιώργος", "m", "Πριν από δύο χρόνια αποφάσισα να τη μάθω. Κάθε Κυριακή πηγαίνω στο σπίτι της με ένα τετράδιο και ένα κινητό, και ηχογραφώ τραγούδια, παροιμίες και ιστορίες από το χωριό των γονιών της. Στην αρχή γελούσε με την προφορά μου, τώρα με διορθώνει με πολλή υπομονή.", "Two years ago I decided to learn it. Every Sunday I go to her house with a notebook and a phone, and I record songs, proverbs and stories from her parents' village. At first she laughed at my accent; now she corrects me with a lot of patience."),
  L("Γιώργος", "m", "Το πιο δύσκολο δεν είναι οι λέξεις, αλλά ότι πολλές εκφράσεις δεν μεταφράζονται. Ετοιμάζω τώρα ένα μικρό αρχείο με τις ηχογραφήσεις, για να μπορούν να τις ακούσουν και τα ξαδέλφια μου. Γιατί μια γλώσσα δεν χάνεται όταν πεθαίνει ο τελευταίος ομιλητής, αλλά όταν πάψει να ενδιαφέρεται ο επόμενος.", "The hardest thing isn't the words, but that many expressions can't be translated. I'm now preparing a small archive of the recordings, so my cousins can listen to them too. Because a language isn't lost when the last speaker dies, but when the next one stops caring."),
 ],
 "questions": [
  Q("Τι νόμιζε ο Γιώργος για τα ποντιακά όταν ήταν μικρός;", ["Ότι ήταν μια ξένη γλώσσα", "Ότι ήταν μια μυστική γλώσσα για τους μεγάλους", "Ότι μιλιόταν μόνο στο χωριό", "Ότι ήταν πολύ εύκολα"], 1, "νόμιζα ότι τα ποντιακά ήταν μια μυστική γλώσσα για τους μεγάλους"),
  Q("Τι κάνει κάθε Κυριακή;", ["Ηχογραφεί τραγούδια, παροιμίες και ιστορίες στο σπίτι της γιαγιάς του", "Παρακολουθεί μαθήματα σε έναν σύλλογο", "Διαβάζει βιβλία στα ποντιακά", "Γράφει τραγούδια"], 0, "ηχογραφώ τραγούδια, παροιμίες και ιστορίες"),
  Q("Γιατί ετοιμάζει ένα αρχείο;", ["Για να το πουλήσει", "Για να το δώσει σε ένα μουσείο", "Για ένα πανεπιστημιακό πρόγραμμα", "Για να μπορούν να ακούσουν τις ηχογραφήσεις και τα ξαδέλφια του"], 3, "για να μπορούν να τις ακούσουν και τα ξαδέλφια μου"),
 ],
 "gloss": {"ποντιακά": "ποντιακά — Pontic Greek", "εγγόνια": "εγγόνι — grandchild", "κοινά ελληνικά": "κοινά ελληνικά — standard Greek", "ηχογραφώ": "ηχογραφώ — to record", "παροιμίες": "παροιμία — proverb", "προφορά": "προφορά — accent, pronunciation", "υπομονή": "υπομονή — patience", "αρχείο": "αρχείο — archive", "ομιλητής": "ομιλητής — speaker", "πάψει": "παύω — to stop, cease"}
})

ITEMS.append({
 "id": "l156-rep-vagonia-xenonas", "title": "Ένας ξενώνας σε παλιά βαγόνια", "title_en": "A guesthouse in old railway carriages", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια ταξιδιωτική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "f", "Στον μικρό σταθμό του χωριού, όπου το τρένο σταμάτησε να περνάει πριν από δεκαπέντε χρόνια, τρία παλιά βαγόνια έχουν γίνει ξενώνας. Η ιδέα ήταν δύο αδελφών, του Στάθη και της Ελένης, που μεγάλωσαν ακούγοντας το σφύριγμα του τρένου από το σπίτι τους.", "At the village's small station, where the train stopped running fifteen years ago, three old carriages have become a guesthouse. The idea came from a brother and sister, Stathis and Eleni, who grew up hearing the train's whistle from their house."),
  L("Ρεπόρτερ", "f", "Τα βαγόνια τα αγόρασαν σε δημοπρασία και χρειάστηκαν δύο χρόνια για να τα επισκευάσουν. Κράτησαν τις ξύλινες πόρτες και τα παλιά φωτιστικά, αλλά πρόσθεσαν μπάνιο, θέρμανση και μεγάλα παράθυρα. Κάθε βαγόνι έχει δύο δωμάτια.", "They bought the carriages at auction and it took two years to repair them. They kept the wooden doors and the old lamps, but added a bathroom, heating and large windows. Each carriage has two rooms."),
  L("Ρεπόρτερ", "f", "Οι πρώτοι επισκέπτες ήταν κυρίως λάτρεις των τρένων, αλλά τώρα έρχονται και οικογένειες, που κάνουν πεζοπορία στις παλιές γραμμές. Το μόνο που λείπει, λέει η Ελένη, είναι ο ήχος του τρένου. Γι' αυτό κάθε πρωί, στις οχτώ, παίζουν από ένα ηχείο το σφύριγμα, για να ξυπνήσουν οι επισκέπτες.", "The first guests were mostly train enthusiasts, but now families come too, hiking along the old tracks. The only thing missing, says Eleni, is the sound of the train. That's why every morning at eight they play the whistle from a speaker to wake the guests."),
 ],
 "questions": [
  Q("Πώς απέκτησαν τα βαγόνια τα δύο αδέλφια;", ["Τους τα χάρισε ο δήμος", "Τα αγόρασαν σε δημοπρασία", "Τα βρήκαν εγκαταλειμμένα και τα πήραν", "Τα νοίκιασαν από τον σιδηρόδρομο"], 1, "Τα βαγόνια τα αγόρασαν σε δημοπρασία"),
  Q("Τι κράτησαν από τα παλιά βαγόνια;", ["Τα παράθυρα", "Τα καθίσματα", "Τις ξύλινες πόρτες και τα παλιά φωτιστικά", "Τους τροχούς"], 2, "Κράτησαν τις ξύλινες πόρτες και τα παλιά φωτιστικά"),
  Q("Τι γίνεται κάθε πρωί στις οχτώ;", ["Περνάει ένα τουριστικό τρενάκι", "Σερβίρεται πρωινό στον σταθμό", "Ξεκινά μια πεζοπορία", "Παίζει από ένα ηχείο το σφύριγμα του τρένου"], 3, "παίζουν από ένα ηχείο το σφύριγμα"),
 ],
 "gloss": {"ξενώνας": "ξενώνας — guesthouse", "βαγόνια": "βαγόνι — railway carriage", "σφύριγμα": "σφύριγμα — whistle", "δημοπρασία": "δημοπρασία — auction", "φωτιστικά": "φωτιστικό — lamp", "θέρμανση": "θέρμανση — heating", "λάτρεις": "λάτρης — enthusiast, lover", "πεζοπορία": "πεζοπορία — hiking", "ηχείο": "ηχείο — loudspeaker"}
})

ITEMS.append({
 "id": "l156-dia-agonas-dromou", "title": "Θα τρέξουμε τα πέντε χιλιόμετρα;", "title_en": "Shall we run the five kilometres?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο συναδέλφους να συζητούν για έναν αγώνα δρόμου της πόλης.",
 "script": [
  L("Νεφέλη", "f", "Πέτρο, είδες ότι τον Μάρτιο γίνεται ο αγώνας δρόμου της πόλης; Έχει και διαδρομή πέντε χιλιομέτρων για αρχάριους. Λέω να γραφτούμε μαζί, ως ομάδα του γραφείου.", "Petros, did you see that the city road race is in March? It also has a five-kilometre route for beginners. I'm thinking we should sign up together, as a team from the office."),
  L("Πέτρος", "m", "Εγώ; Δεν έχω τρέξει από το λύκειο. Με το ζόρι ανεβαίνω τις σκάλες ως τον τρίτο όροφο.", "Me? I haven't run since high school. I can barely climb the stairs to the third floor."),
  L("Νεφέλη", "f", "Γι' αυτό ακριβώς. Υπάρχει ένα πρόγραμμα οκτώ εβδομάδων: στην αρχή εναλλάσσεις ένα λεπτό τρέξιμο με δύο λεπτά περπάτημα, τρεις φορές την εβδομάδα. Μπορούμε να το κάνουμε μαζί στο πάρκο, μετά τη δουλειά.", "That's exactly why. There's an eight-week programme: at the start you alternate one minute of running with two minutes of walking, three times a week. We can do it together in the park, after work."),
  L("Πέτρος", "m", "Εντάξει, αλλά με έναν όρο: αν στις δύο πρώτες εβδομάδες δεν τα καταφέρνω, θα έρθω στον αγώνα μόνο για να σας χειροκροτώ. Και θα πρέπει να αγοράσω πρώτα κανονικά παπούτσια.", "OK, but on one condition: if I can't manage in the first two weeks, I'll come to the race only to cheer you on. And I'll have to buy proper shoes first."),
 ],
 "questions": [
  Q("Τι προτείνει η Νεφέλη;", ["Να γραφτούν μαζί στη διαδρομή των πέντε χιλιομέτρων", "Να τρέξουν τον μαραθώνιο", "Να πάνε σε γυμναστήριο", "Να οργανώσουν έναν αγώνα στο γραφείο"], 0, "Λέω να γραφτούμε μαζί, ως ομάδα του γραφείου"),
  Q("Πώς ξεκινά το πρόγραμμα των οκτώ εβδομάδων;", ["Με είκοσι λεπτά τρέξιμο", "Με γυμναστική στο σπίτι", "Με ένα λεπτό τρέξιμο και δύο λεπτά περπάτημα εναλλάξ", "Με καθημερινό περπάτημα"], 2, "εναλλάσσεις ένα λεπτό τρέξιμο με δύο λεπτά περπάτημα"),
  Q("Ποιον όρο βάζει ο Πέτρος;", ["Να τρέχουν μόνο τα Σαββατοκύριακα", "Να του αγοράσει παπούτσια η εταιρεία", "Να μην τρέξουν στη βροχή", "Αν δεν τα καταφέρει στις δύο πρώτες εβδομάδες, θα πάει μόνο για να χειροκροτεί"], 3, "θα έρθω στον αγώνα μόνο για να σας χειροκροτώ"),
 ],
 "gloss": {"αγώνας δρόμου": "αγώνας δρόμου — road race", "διαδρομή": "διαδρομή — route, course", "αρχάριους": "αρχάριος — beginner", "γραφτούμε": "γράφομαι — to sign up", "Με το ζόρι": "με το ζόρι — barely, with difficulty", "εναλλάσσεις": "εναλλάσσω — to alternate", "όρο": "όρος — condition", "χειροκροτώ": "χειροκροτώ — to applaud, cheer"}
})

ITEMS.append({
 "id": "l156-c1-genethlia", "title": "Το παράδοξο των γενεθλίων", "title_en": "The birthday paradox", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκλαϊκευτική ομιλία για τις πιθανότητες.",
 "script": [
  L("Ομιλήτρια", "f", "Πόσοι άνθρωποι πρέπει να βρίσκονται σε ένα δωμάτιο, ώστε να υπάρχουν περισσότερες από τις μισές πιθανότητες δύο από αυτούς να έχουν γενέθλια την ίδια μέρα; Οι περισσότεροι απαντούν «γύρω στους εκατόν ογδόντα», δηλαδή τις μισές μέρες του χρόνου. Η σωστή απάντηση είναι μόλις είκοσι τρεις.", "How many people need to be in a room for there to be a better than even chance that two of them share a birthday? Most people answer \"around a hundred and eighty\", that is, half the days of the year. The correct answer is just twenty-three."),
  L("Ομιλήτρια", "f", "Το λάθος μας είναι ότι σκεφτόμαστε τον εαυτό μας: πόσο πιθανό είναι κάποιος να έχει γενέθλια την ίδια μέρα με εμένα. Το ερώτημα, όμως, αφορά οποιοδήποτε ζευγάρι. Και σε μια ομάδα είκοσι τριών ατόμων σχηματίζονται διακόσια πενήντα τρία διαφορετικά ζευγάρια, όχι είκοσι δύο.", "Our mistake is that we think about ourselves: how likely it is that someone has the same birthday as me. The question, however, concerns any pair. And in a group of twenty-three people, two hundred and fifty-three different pairs are formed, not twenty-two."),
  L("Ομιλήτρια", "f", "Με εβδομήντα άτομα, η πιθανότητα ξεπερνά το ενενήντα εννέα τοις εκατό. Γι' αυτό σε μια σχολική τάξη συμπτώσεις γενεθλίων είναι κάτι πολύ συνηθισμένο, και όχι ένδειξη μοίρας.", "With seventy people, the probability exceeds ninety-nine per cent. That's why birthday coincidences in a school class are something very common, and not a sign of fate."),
  L("Ομιλήτρια", "f", "Το παράδοξο έχει και πρακτική σημασία. Στην κρυπτογραφία, για παράδειγμα, η λεγόμενη «επίθεση γενεθλίων» εκμεταλλεύεται ακριβώς το ότι οι συμπτώσεις εμφανίζονται πολύ νωρίτερα απ' όσο μας λέει η διαίσθησή μας.", "The paradox also has practical importance. In cryptography, for example, the so-called \"birthday attack\" exploits precisely the fact that coincidences appear much sooner than our intuition tells us."),
 ],
 "questions": [
  Q("Πόσα άτομα χρειάζονται, ώστε να υπάρχουν πάνω από τις μισές πιθανότητες δύο να έχουν γενέθλια την ίδια μέρα;", ["Περίπου εκατόν ογδόντα", "Είκοσι τρία", "Εβδομήντα", "Τριακόσια εξήντα έξι"], 1, "Η σωστή απάντηση είναι μόλις είκοσι τρεις"),
  Q("Ποιο είναι, κατά την ομιλήτρια, το λάθος μας;", ["Ότι σκεφτόμαστε μόνο αν κάποιος έχει γενέθλια την ίδια μέρα με εμάς", "Ότι ξεχνάμε τα δίσεκτα έτη", "Ότι υπολογίζουμε λάθος τις μέρες του χρόνου", "Ότι δεν πιστεύουμε στις πιθανότητες"], 0, "Το λάθος μας είναι ότι σκεφτόμαστε τον εαυτό μας"),
  Q("Τι συμπέρασμα βγάζει για τις συμπτώσεις γενεθλίων σε μια τάξη;", ["Ότι είναι σπάνιες", "Ότι είναι ένδειξη μοίρας", "Ότι είναι κάτι πολύ συνηθισμένο", "Ότι συμβαίνουν μόνο σε μεγάλες τάξεις"], 2, "συμπτώσεις γενεθλίων είναι κάτι πολύ συνηθισμένο"),
  Q("Τι εκμεταλλεύεται η «επίθεση γενεθλίων» στην κρυπτογραφία;", ["Τις ημερομηνίες γέννησης των χρηστών", "Τα αδύναμα συνθηματικά", "Τα λάθη των προγραμματιστών", "Το ότι οι συμπτώσεις εμφανίζονται πολύ νωρίτερα απ' όσο λέει η διαίσθηση"], 3, "οι συμπτώσεις εμφανίζονται πολύ νωρίτερα απ' όσο μας λέει η διαίσθησή μας"),
 ],
 "gloss": {"εκλαϊκευτική": "εκλαϊκευτικός — popular-science", "πιθανότητες": "πιθανότητα — probability, chance", "ζευγάρι": "ζευγάρι — pair", "σχηματίζονται": "σχηματίζομαι — to be formed", "συμπτώσεις": "σύμπτωση — coincidence", "ένδειξη": "ένδειξη — sign, indication", "μοίρας": "μοίρα — fate", "κρυπτογραφία": "κρυπτογραφία — cryptography", "εκμεταλλεύεται": "εκμεταλλεύομαι — to exploit", "διαίσθησή": "διαίσθηση — intuition"}
})

ITEMS.append({
 "id": "l156-c1-monty-hall", "title": "Τρεις πόρτες και μια κατσίκα", "title_en": "Three doors and a goat", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια ραδιοφωνική εκπομπή για τα μαθηματικά της καθημερινότητας.",
 "script": [
  L("Παρουσιαστής", "m", "Φανταστείτε ότι είστε σε ένα τηλεπαιχνίδι. Μπροστά σας υπάρχουν τρεις πόρτες: πίσω από τη μία είναι ένα αυτοκίνητο, πίσω από τις άλλες δύο από μια κατσίκα. Διαλέγετε μια πόρτα. Ο παρουσιαστής, που ξέρει πού είναι το αυτοκίνητο, ανοίγει μία από τις άλλες δύο και σας δείχνει μια κατσίκα. Και σας ρωτά: θέλετε να αλλάξετε πόρτα;", "Imagine you're on a game show. In front of you there are three doors: behind one is a car, behind each of the other two a goat. You pick a door. The host, who knows where the car is, opens one of the other two and shows you a goat. And asks you: do you want to switch doors?"),
  L("Παρουσιαστής", "m", "Οι περισσότεροι πιστεύουν ότι δεν έχει σημασία: έμειναν δύο πόρτες, άρα οι πιθανότητες είναι ίσες. Κι όμως, αν αλλάξετε, κερδίζετε το αυτοκίνητο με πιθανότητα δύο στις τρεις.", "Most people believe it doesn't matter: two doors are left, so the chances are equal. And yet, if you switch, you win the car with a probability of two in three."),
  L("Παρουσιαστής", "m", "Όταν το 1990 η αρθρογράφος Μέριλιν βος Σαβάντ έγραψε αυτή την απάντηση σε ένα αμερικανικό περιοδικό, έλαβε χιλιάδες γράμματα, πολλά από καθηγητές μαθηματικών, που τη διαβεβαίωναν ότι έκανε λάθος. Είχε όμως δίκιο.", "When in 1990 the columnist Marilyn vos Savant gave this answer in an American magazine, she received thousands of letters, many from mathematics professors, assuring her that she was wrong. But she was right."),
  L("Παρουσιαστής", "m", "Το κλειδί είναι ότι ο παρουσιαστής δεν ανοίγει μια πόρτα στην τύχη. Η πρώτη σας επιλογή είναι σωστή μόνο σε μία περίπτωση στις τρεις· στις άλλες δύο, το αυτοκίνητο βρίσκεται πίσω από την πόρτα που αφήνει κλειστή εκείνος. Αν δεν σας πείθει, πάρτε τρία φλιτζάνια και ένα κέρμα, και παίξτε το είκοσι φορές με έναν φίλο.", "The key is that the host doesn't open a door at random. Your first choice is right in only one case in three; in the other two, the car is behind the door he leaves closed. If you're not convinced, take three cups and a coin, and play it twenty times with a friend."),
 ],
 "questions": [
  Q("Τι πιστεύουν οι περισσότεροι για την αλλαγή πόρτας;", ["Ότι πρέπει πάντα να αλλάζουν", "Ότι δεν έχει σημασία, γιατί οι πιθανότητες είναι ίσες", "Ότι πρέπει να κρατήσουν την πρώτη τους επιλογή", "Ότι ο παρουσιαστής τους ξεγελάει"], 1, "Οι περισσότεροι πιστεύουν ότι δεν έχει σημασία"),
  Q("Με ποια πιθανότητα κερδίζει όποιος αλλάζει πόρτα;", ["Μία στις τρεις", "Μία στις δύο", "Δύο στις τρεις", "Τρεις στις τέσσερις"], 2, "κερδίζετε το αυτοκίνητο με πιθανότητα δύο στις τρεις"),
  Q("Πώς αντέδρασαν πολλοί αναγνώστες στην απάντηση της Μέριλιν βος Σαβάντ;", ["Της έγραψαν ότι έκανε λάθος", "Τη συνεχάρησαν", "Ζήτησαν να παίξουν το παιχνίδι", "Δεν αντέδρασαν καθόλου"], 0, "τη διαβεβαίωναν ότι έκανε λάθος"),
  Q("Ποιο είναι, κατά τον παρουσιαστή, το κλειδί του προβλήματος;", ["Ότι τα αυτοκίνητα είναι πιο πολύτιμα από τις κατσίκες", "Ότι οι παίκτες βιάζονται", "Ότι οι πόρτες δεν είναι ίδιες", "Ότι ο παρουσιαστής δεν ανοίγει μια πόρτα στην τύχη"], 3, "ο παρουσιαστής δεν ανοίγει μια πόρτα στην τύχη"),
 ],
 "gloss": {"τηλεπαιχνίδι": "τηλεπαιχνίδι — TV game show", "κατσίκα": "κατσίκα — goat", "πιθανότητα": "πιθανότητα — probability", "αρθρογράφος": "αρθρογράφος — columnist", "διαβεβαίωναν": "διαβεβαιώνω — to assure", "στην τύχη": "στην τύχη — at random", "επιλογή": "επιλογή — choice", "πείθει": "πείθω — to convince", "κέρμα": "κέρμα — coin"}
})

rnd = random.Random(156)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-156.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
