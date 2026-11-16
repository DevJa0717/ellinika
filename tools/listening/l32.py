# Source for library/listening/listening-32.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l32.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l32-ann-xionodromiko", "title": "Ανακοίνωση στο χιονοδρομικό κέντρο", "title_en": "An announcement at the ski centre", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα του χιονοδρομικού κέντρου του Παρνασσού.",
 "script": [
  L("Εκφωνητής", "m", "Προσοχή, παρακαλώ. Λόγω των ισχυρών ανέμων που πνέουν στις ψηλότερες πίστες, οι αναβατήρες των Κελλαριών θα παραμείνουν κλειστοί σήμερα μέχρι νεωτέρας. Σε λειτουργία βρίσκονται μόνο οι αναβατήρες της Φτερόλακκας και η πίστα για αρχάριους.", "Attention, please. Because of the strong winds blowing on the higher slopes, the lifts at Kellaria will remain closed today until further notice. Only the Fterolakka lifts and the beginners' slope are in operation."),
  L("Εκφωνητής", "m", "Όσοι έχετε αγοράσει ημερήσιο εισιτήριο για όλο το χιονοδρομικό μπορείτε να ζητήσετε επιστροφή του μισού ποσού από τα ταμεία μέχρι τις δώδεκα. Τα μαθήματα σκι για παιδιά γίνονται κανονικά, αλλά μεταφέρονται στη Φτερόλακκα.", "Those of you who have bought a day pass for the whole ski centre can ask for half the amount back at the ticket desks until twelve. Children's ski lessons are going ahead as normal but are moving to Fterolakka."),
  L("Εκφωνητής", "m", "Υπενθυμίζουμε ότι στον δρόμο από την Αράχωβα οι αλυσίδες είναι υποχρεωτικές από το απόγευμα, καθώς αναμένεται χιονόπτωση. Σας ευχαριστούμε για την κατανόηση.", "We remind you that on the road from Arachova chains are compulsory from the afternoon, as snowfall is expected. Thank you for your understanding."),
 ],
 "questions": [
  Q("Γιατί είναι κλειστοί οι αναβατήρες των Κελλαριών;", ["Λόγω βλάβης", "Λόγω ισχυρών ανέμων", "Γιατί δεν έχει χιόνι", "Λόγω απεργίας"], 1, "Λόγω των ισχυρών ανέμων που πνέουν στις ψηλότερες πίστες"),
  Q("Τι μπορούν να κάνουν όσοι έχουν ημερήσιο εισιτήριο;", ["Να το χρησιμοποιήσουν αύριο", "Να ζητήσουν επιστροφή του μισού ποσού μέχρι τις δώδεκα", "Να πάρουν δωρεάν μάθημα", "Να πάρουν πίσω όλο το ποσό"], 1, "μπορείτε να ζητήσετε επιστροφή του μισού ποσού από τα ταμεία μέχρι τις δώδεκα"),
  Q("Τι ισχύει για τον δρόμο από την Αράχωβα;", ["Είναι κλειστός", "Οι αλυσίδες είναι υποχρεωτικές από το απόγευμα", "Περνούν μόνο λεωφορεία", "Έχει έργα"], 1, "οι αλυσίδες είναι υποχρεωτικές από το απόγευμα"),
 ],
 "gloss": {"χιονοδρομικού κέντρου": "χιονοδρομικό κέντρο — ski centre", "πνέουν": "πνέω — to blow (of wind)", "πίστες": "πίστα — (ski) slope", "αναβατήρες": "αναβατήρας — ski lift", "μέχρι νεωτέρας": "μέχρι νεωτέρας — until further notice", "αρχάριους": "αρχάριος — beginner", "ημερήσιο εισιτήριο": "ημερήσιο εισιτήριο — day pass", "ταμεία": "ταμείο — ticket desk, till", "αλυσίδες": "αλυσίδα — (snow) chain", "χιονόπτωση": "χιονόπτωση — snowfall"},
})

ITEMS.append({
 "id": "l32-vm-mpaleto", "title": "Μήνυμα από τη σχολή μπαλέτου", "title_en": "A message from the ballet school", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τη σχολή μπαλέτου της κόρης σας.",
 "script": [
  L("Δασκάλα", "f", "Καλησπέρα σας, είμαι η Ελένη από τη σχολή μπαλέτου «Πιρουέτα». Σας τηλεφωνώ για την ετήσια παράσταση των παιδιών. Επειδή το Δημοτικό Θέατρο δεν είναι διαθέσιμο το Σάββατο, η παράσταση μεταφέρεται την Κυριακή στις έξι το απόγευμα.", "Good evening, this is Eleni from the «Pirouette» ballet school. I'm calling about the children's annual performance. Because the Municipal Theatre isn't available on Saturday, the performance is moving to Sunday at six in the evening."),
  L("Δασκάλα", "f", "Η γενική πρόβα θα γίνει την Παρασκευή στις έξι, στο θέατρο και όχι στη σχολή. Είναι πολύ σημαντικό να έρθουν όλα τα παιδιά, γιατί θα δοκιμάσουμε και τα κοστούμια με τα φώτα της σκηνής.", "The dress rehearsal will take place on Friday at six, at the theatre and not at the school. It's very important that all the children come, because we'll also try out the costumes under the stage lights."),
  L("Δασκάλα", "f", "Η μικρή χρειάζεται λευκό καλσόν και τα μαλλιά της πρέπει να είναι πιασμένα κότσο. Τα εισιτήρια για τους γονείς κοστίζουν οχτώ ευρώ και τα έσοδα θα διατεθούν στον Σύλλογο Φίλων του Παιδιού. Αν έχετε απορίες, καλέστε με στο κινητό.", "Your little girl needs white tights and her hair must be tied up in a bun. Tickets for parents cost eight euros and the proceeds will go to the Friends of the Child Association. If you have questions, call me on my mobile."),
 ],
 "questions": [
  Q("Γιατί αλλάζει η μέρα της παράστασης;", ["Γιατί αρρώστησε η δασκάλα", "Γιατί το θέατρο δεν είναι διαθέσιμο το Σάββατο", "Γιατί δεν είναι έτοιμα τα κοστούμια", "Λόγω καιρού"], 1, "το Δημοτικό Θέατρο δεν είναι διαθέσιμο το Σάββατο"),
  Q("Πού θα γίνει η γενική πρόβα;", ["Στη σχολή", "Στο θέατρο", "Σε ένα γυμναστήριο", "Στο σχολείο της κόρης"], 1, "στο θέατρο και όχι στη σχολή"),
  Q("Πού θα πάνε τα έσοδα από τα εισιτήρια;", ["Στη σχολή για νέα κοστούμια", "Σε έναν σύλλογο για τα παιδιά", "Στον δήμο", "Στο θέατρο"], 1, "τα έσοδα θα διατεθούν στον Σύλλογο Φίλων του Παιδιού"),
 ],
 "gloss": {"μπαλέτου": "μπαλέτο — ballet", "ετήσια": "ετήσιος — annual", "παράσταση": "παράσταση — performance, show", "γενική πρόβα": "γενική πρόβα — dress rehearsal", "κοστούμια": "κοστούμι — costume", "σκηνής": "σκηνή — stage", "καλσόν": "καλσόν — tights", "πιασμένα": "πιάνω (τα μαλλιά) — to tie up (hair)", "κότσο": "κότσος — bun (hair)", "έσοδα": "έσοδα — proceeds, income", "θα διατεθούν": "διατίθεμαι — to be allocated, given"},
})

ITEMS.append({
 "id": "l32-dia-stroma", "title": "Ψάχνοντας καινούργιο στρώμα", "title_en": "Looking for a new mattress", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα κατάστημα με στρώματα.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Ψάχνω ένα καινούργιο στρώμα για διπλό κρεβάτι. Τον τελευταίο καιρό ξυπνάω με πόνους στη μέση, και ο γιατρός μού είπε ότι ίσως φταίει το στρώμα, που είναι πάνω από δεκαπέντε χρονών.", "Good morning. I'm looking for a new mattress for a double bed. Lately I've been waking up with lower back pain, and the doctor told me the mattress might be to blame; it's over fifteen years old."),
  L("Πωλητής", "m", "Δεκαπέντε χρόνια είναι πολλά· ένα στρώμα καλό είναι να αλλάζει κάθε οχτώ με δέκα χρόνια. Για τη μέση δεν προτείνουμε πια τα πολύ σκληρά στρώματα, όπως παλιά, αλλά τα μέτρια, που στηρίζουν τη σπονδυλική στήλη χωρίς να πιέζουν τους ώμους. Ξαπλώστε σε αυτό να δείτε πώς σας φαίνεται.", "Fifteen years is a lot; it's best to change a mattress every eight to ten years. For the back we no longer recommend very firm mattresses, as in the past, but medium ones, which support the spine without pressing on the shoulders. Lie down on this one and see how it feels."),
  L("Πελάτισσα", "f", "Είναι πολύ άνετο. Αλλά πώς θα ξέρω αν μου κάνει πραγματικά, αν δεν κοιμηθώ πάνω του;", "It's very comfortable. But how will I know if it really suits me if I don't sleep on it?"),
  L("Πωλητής", "m", "Γι' αυτό έχουμε δοκιμαστική περίοδο εκατό νυχτών: αν δεν σας ικανοποιεί, το αλλάζουμε. Η παράδοση είναι δωρεάν, και με είκοσι ευρώ παίρνουμε και το παλιό σας στρώμα για ανακύκλωση.", "That's why we have a trial period of a hundred nights: if it doesn't satisfy you, we exchange it. Delivery is free, and for twenty euros we also take your old mattress for recycling."),
 ],
 "questions": [
  Q("Γιατί θέλει η πελάτισσα να αλλάξει το στρώμα της;", ["Γιατί μετακόμισε", "Γιατί ξυπνάει με πόνους στη μέση", "Γιατί αγόρασε νέο κρεβάτι", "Γιατί σκίστηκε"], 1, "ξυπνάω με πόνους στη μέση"),
  Q("Τι στρώμα προτείνει ο πωλητής για τη μέση;", ["Ένα πολύ σκληρό", "Ένα μέτριο", "Ένα πολύ μαλακό", "Ένα με ελατήρια"], 1, "τα μέτρια, που στηρίζουν τη σπονδυλική στήλη"),
  Q("Τι γίνεται αν το στρώμα δεν την ικανοποιεί;", ["Χάνει τα χρήματά της", "Το αλλάζουν μέσα σε εκατό νύχτες", "Πληρώνει είκοσι ευρώ", "Της δίνουν ένα μαξιλάρι"], 1, "δοκιμαστική περίοδο εκατό νυχτών: αν δεν σας ικανοποιεί, το αλλάζουμε"),
 ],
 "gloss": {"στρώμα": "στρώμα — mattress", "μέση": "μέση — lower back, waist", "φταίει": "φταίω — to be to blame", "σκληρά": "σκληρός — hard, firm", "στηρίζουν": "στηρίζω — to support", "σπονδυλική στήλη": "σπονδυλική στήλη — spine", "Ξαπλώστε": "ξαπλώνω — to lie down", "άνετο": "άνετος — comfortable", "δοκιμαστική περίοδο": "δοκιμαστική περίοδος — trial period", "παράδοση": "παράδοση — delivery", "ανακύκλωση": "ανακύκλωση — recycling"},
})

ITEMS.append({
 "id": "l32-dia-portofoli", "title": "Δήλωση απώλειας στο αστυνομικό τμήμα", "title_en": "Reporting a loss at the police station", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα αστυνομικό τμήμα της Αθήνας.",
 "script": [
  L("Πολίτης", "m", "Καλημέρα. Θέλω να δηλώσω την απώλεια του πορτοφολιού μου. Νομίζω ότι μου έπεσε χθες το βράδυ στο λεωφορείο, ανάμεσα στο Σύνταγμα και την Κηφισιά. Μέσα είχα την ταυτότητα, το δίπλωμα οδήγησης και δύο κάρτες.", "Good morning. I'd like to report the loss of my wallet. I think it fell out last night on the bus, between Syntagma and Kifisia. Inside I had my ID card, my driving licence and two cards."),
  L("Αστυνομικός", "f", "Μάλιστα. Τις κάρτες τις έχετε ακυρώσει; Αυτό πρέπει να γίνει αμέσως, πριν από οτιδήποτε άλλο, για να μην τις χρησιμοποιήσει κάποιος άλλος.", "I see. Have you cancelled the cards? That has to be done immediately, before anything else, so that no one else can use them."),
  L("Πολίτης", "m", "Ναι, πήρα την τράπεζα από χθες. Τι χρειάζομαι για να βγάλω καινούργια ταυτότητα;", "Yes, I called the bank last night. What do I need to get a new ID card?"),
  L("Αστυνομικός", "f", "Θα σας δώσω μια βεβαίωση απώλειας, την οποία θα προσκομίσετε μαζί με φωτογραφίες στο τμήμα ταυτοτήτων. Σας συμβουλεύω επίσης να ρωτήσετε σε λίγες μέρες στο γραφείο απολεσθέντων αντικειμένων του ΟΑΣΑ· πολλά πορτοφόλια βρίσκονται από τους οδηγούς.", "I'll give you a certificate of loss, which you'll present with photographs at the ID card office. I also advise you to ask in a few days at the OASA lost property office; many wallets are found by the drivers."),
 ],
 "questions": [
  Q("Πού πιστεύει ο πολίτης ότι έχασε το πορτοφόλι;", ["Σε ένα ταξί", "Στο λεωφορείο", "Στο μετρό", "Σε μια καφετέρια"], 1, "μου έπεσε χθες το βράδυ στο λεωφορείο"),
  Q("Τι λέει η αστυνομικός ότι πρέπει να γίνει πρώτα;", ["Να βγάλει νέα ταυτότητα", "Να ακυρώσει τις κάρτες", "Να βγάλει φωτογραφίες", "Να πάει στον ΟΑΣΑ"], 1, "πρέπει να γίνει αμέσως, πριν από οτιδήποτε άλλο"),
  Q("Γιατί τον συμβουλεύει να ρωτήσει στο γραφείο απολεσθέντων;", ["Γιατί εκεί βγαίνουν ταυτότητες", "Γιατί πολλά πορτοφόλια βρίσκονται από τους οδηγούς", "Γιατί εκεί πληρώνει το πρόστιμο", "Γιατί εκεί είναι η τράπεζα"], 1, "πολλά πορτοφόλια βρίσκονται από τους οδηγούς"),
 ],
 "gloss": {"αστυνομικό τμήμα": "αστυνομικό τμήμα — police station", "να δηλώσω": "δηλώνω — to report, declare", "απώλεια": "απώλεια — loss", "πορτοφολιού": "πορτοφόλι — wallet", "ταυτότητα": "ταυτότητα — ID card", "δίπλωμα οδήγησης": "δίπλωμα οδήγησης — driving licence", "ακυρώσει": "ακυρώνω — to cancel", "βεβαίωση": "βεβαίωση — certificate", "θα προσκομίσετε": "προσκομίζω — to present, submit (documents)", "απολεσθέντων αντικειμένων": "απολεσθέντα αντικείμενα — lost property"},
})

ITEMS.append({
 "id": "l32-mono-mpouzouki", "title": "Μπουζούκι στα σαράντα", "title_en": "Bouzouki at forty", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να μιλάει για το πώς έμαθε μπουζούκι.",
 "script": [
  L("Δέσποινα", "f", "Όταν έκλεισα τα σαράντα, ο άντρας μου μού έκανε δώρο ένα μπουζούκι. Από μικρή ήθελα να παίξω, αλλά στο σπίτι μας έλεγαν ότι το μπουζούκι είναι όργανο για άντρες και για ταβέρνες. Έτσι, πήγα σε ωδείο και έμαθα πιάνο, χωρίς ποτέ να το αγαπήσω πραγματικά.", "When I turned forty, my husband gave me a bouzouki as a present. Since I was little I'd wanted to play, but at home they said the bouzouki was an instrument for men and for tavernas. So I went to a conservatory and learned piano, without ever really loving it."),
  L("Δέσποινα", "f", "Οι πρώτοι μήνες ήταν απογοητευτικοί. Τα δάχτυλά μου πονούσαν από τις μεταλλικές χορδές και η πένα μού έφευγε συνέχεια από το χέρι. Ο δάσκαλός μου, ένας ηλικιωμένος μουσικός, μου είπε κάτι που δεν θα ξεχάσω: «Το μπουζούκι δεν το παίζεις με τα δάχτυλα, το παίζεις με την υπομονή.»", "The first months were discouraging. My fingers hurt from the metal strings and the plectrum kept slipping out of my hand. My teacher, an elderly musician, told me something I'll never forget: «You don't play the bouzouki with your fingers, you play it with patience.»"),
  L("Δέσποινα", "f", "Σήμερα, τρία χρόνια μετά, παίζω με μια μικρή κομπανία σε γιορτές της γειτονιάς. Δεν είμαι βιρτουόζος, αλλά όταν παίζω ένα ταξίμι και ο κόσμος σωπαίνει, νιώθω ότι ξαναβρήκα κάτι που είχα χάσει από παιδί.", "Today, three years later, I play with a small band at neighbourhood festivals. I'm no virtuoso, but when I play a taximi and people fall silent, I feel I've found again something I'd lost since childhood."),
 ],
 "questions": [
  Q("Γιατί δεν έμαθε μπουζούκι όταν ήταν μικρή;", ["Γιατί δεν είχαν χρήματα", "Γιατί στο σπίτι έλεγαν ότι είναι όργανο για άντρες", "Γιατί δεν υπήρχε δάσκαλος", "Γιατί προτιμούσε το πιάνο"], 1, "έλεγαν ότι το μπουζούκι είναι όργανο για άντρες και για ταβέρνες"),
  Q("Τι δυσκολίες είχε στην αρχή;", ["Δεν μπορούσε να διαβάσει νότες", "Πονούσαν τα δάχτυλά της και της έφευγε η πένα", "Δεν είχε χρόνο", "Ενοχλούνταν οι γείτονες"], 1, "Τα δάχτυλά μου πονούσαν από τις μεταλλικές χορδές"),
  Q("Πού παίζει σήμερα;", ["Σε ένα ωδείο", "Με μια μικρή κομπανία σε γιορτές της γειτονιάς", "Σε μια μεγάλη ορχήστρα", "Μόνο στο σπίτι"], 1, "παίζω με μια μικρή κομπανία σε γιορτές της γειτονιάς"),
 ],
 "gloss": {"όργανο": "όργανο — (musical) instrument", "ωδείο": "ωδείο — conservatory, music school", "απογοητευτικοί": "απογοητευτικός — discouraging", "μεταλλικές": "μεταλλικός — metal", "χορδές": "χορδή — string", "πένα": "πένα — plectrum, pick", "υπομονή": "υπομονή — patience", "κομπανία": "κομπανία — small band", "βιρτουόζος": "βιρτουόζος — virtuoso", "ταξίμι": "ταξίμι — taximi (improvised prelude)", "σωπαίνει": "σωπαίνω — to fall silent"},
})

ITEMS.append({
 "id": "l32-rep-gefyria", "title": "Τα πέτρινα γεφύρια της Ηπείρου", "title_en": "The stone bridges of Epirus", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ για τα πέτρινα γεφύρια της Ηπείρου.",
 "script": [
  L("Ρεπόρτερ", "f", "Στα βουνά της Ηπείρου σώζονται εκατοντάδες πέτρινα γεφύρια, τα περισσότερα χτισμένα τον 18ο και τον 19ο αιώνα. Τα έφτιαχναν περιπλανώμενοι μάστορες από τα χωριά της περιοχής, οι οποίοι ταξίδευαν σε συντροφιές και μιλούσαν μεταξύ τους μια μυστική γλώσσα, τα κουδαρίτικα, για να μην τους καταλαβαίνουν οι ξένοι.", "In the mountains of Epirus hundreds of stone bridges survive, most built in the 18th and 19th centuries. They were made by itinerant master builders from the villages of the region, who travelled in companies and spoke a secret language among themselves, koudaritika, so that outsiders couldn't understand them."),
  L("Ρεπόρτερ", "f", "Τα γεφύρια χρηματοδοτούνταν συχνά από πλούσιους ευεργέτες ή από τις ίδιες τις κοινότητες, γιατί χωρίς αυτά τα χωριά έμεναν αποκομμένα τον χειμώνα, όταν φούσκωναν τα ποτάμια. Γύρω τους γεννήθηκαν πολλοί θρύλοι, όπως το γνωστό τραγούδι για το γεφύρι της Άρτας.", "The bridges were often funded by wealthy benefactors or by the communities themselves, because without them the villages were cut off in winter, when the rivers swelled. Many legends grew up around them, such as the well-known song about the bridge of Arta."),
  L("Ρεπόρτερ", "f", "Το πιο συγκινητικό παράδειγμα είναι το γεφύρι της Πλάκας, πάνω από τον Άραχθο, το μεγαλύτερο μονότοξο γεφύρι των Βαλκανίων. Το 2015 κατέρρευσε σε μια πλημμύρα, και πολλοί πίστεψαν ότι χάθηκε για πάντα. Χάρη όμως σε μια μεγάλη προσπάθεια επιστημόνων και τεχνιτών, αναστηλώθηκε με τα ίδια του τα υλικά και άνοιξε ξανά το 2020.", "The most moving example is the Plaka bridge over the Arachthos, the largest single-arch bridge in the Balkans. In 2015 it collapsed in a flood, and many believed it was lost forever. But thanks to a great effort by scientists and craftsmen, it was restored with its own materials and reopened in 2020."),
 ],
 "questions": [
  Q("Γιατί οι μάστορες μιλούσαν μια μυστική γλώσσα;", ["Για να προσεύχονται", "Για να μην τους καταλαβαίνουν οι ξένοι", "Γιατί ήταν ξένοι", "Για να τραγουδούν"], 1, "για να μην τους καταλαβαίνουν οι ξένοι"),
  Q("Γιατί ήταν τόσο σημαντικά τα γεφύρια για τα χωριά;", ["Για το εμπόριο με την Ιταλία", "Χωρίς αυτά έμεναν αποκομμένα τον χειμώνα", "Για να μαζεύουν νερό", "Για τη στρατιωτική άμυνα"], 1, "χωρίς αυτά τα χωριά έμεναν αποκομμένα τον χειμώνα"),
  Q("Τι έγινε με το γεφύρι της Πλάκας;", ["Αντικαταστάθηκε από ένα νέο", "Κατέρρευσε το 2015 και αναστηλώθηκε", "Μεταφέρθηκε σε μουσείο", "Είναι ακόμη χαλασμένο"], 1, "Το 2015 κατέρρευσε σε μια πλημμύρα"),
 ],
 "gloss": {"γεφύρια": "γεφύρι — (stone) bridge", "περιπλανώμενοι": "περιπλανώμενος — itinerant, wandering", "μάστορες": "μάστορας — master builder, craftsman", "συντροφιές": "συντροφιά — company, group", "ευεργέτες": "ευεργέτης — benefactor", "αποκομμένα": "αποκομμένος — cut off", "φούσκωναν": "φουσκώνω — to swell", "θρύλοι": "θρύλος — legend", "μονότοξο": "μονότοξος — single-arch", "κατέρρευσε": "καταρρέω — to collapse", "αναστηλώθηκε": "αναστηλώνω — to restore (a monument)"},
})

ITEMS.append({
 "id": "l32-rep-tilos", "title": "Η Τήλος, ένα μικρό νησί με μεγάλες ιδέες", "title_en": "Tilos, a small island with big ideas", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για την Τήλο, ένα μικρό νησί των Δωδεκανήσων.",
 "script": [
  L("Ρεπόρτερ", "m", "Η Τήλος έχει λιγότερους από χίλιους μόνιμους κατοίκους, όμως τα τελευταία χρόνια έχει γίνει παράδειγμα για όλη την Ευρώπη. Ήταν από τα πρώτα ελληνικά νησιά που απαγόρευσαν το κυνήγι, ήδη από τη δεκαετία του '90, και σήμερα φιλοξενεί σπάνια πουλιά που δύσκολα βλέπει κανείς αλλού.", "Tilos has fewer than a thousand permanent residents, yet in recent years it has become an example for the whole of Europe. It was among the first Greek islands to ban hunting, back in the 1990s, and today it is home to rare birds that are hard to see elsewhere."),
  L("Ρεπόρτερ", "m", "Στο νησί λειτουργεί ένα υβριδικό σύστημα με ανεμογεννήτρια, φωτοβολταϊκά και μεγάλες μπαταρίες, που καλύπτει μεγάλο μέρος των αναγκών του σε ηλεκτρισμό. Το 2021, μάλιστα, η Τήλος έγινε το πρώτο νησί στην Ελλάδα χωρίς χωματερή: τα απορρίμματα διαλέγονται από πόρτα σε πόρτα και σχεδόν όλα ανακυκλώνονται ή γίνονται λίπασμα.", "The island runs a hybrid system with a wind turbine, solar panels and large batteries, which covers a large part of its electricity needs. In 2021, what's more, Tilos became the first island in Greece without a landfill: rubbish is sorted door to door and almost all of it is recycled or turned into compost."),
  L("Ρεπόρτερ", "m", "Η Τήλος έχει και ένα ακόμη μυστικό: σε ένα σπήλαιο του νησιού βρέθηκαν απολιθώματα από νάνους ελέφαντες, ύψους μόλις ενάμισι μέτρου, που επέζησαν εδώ πολύ περισσότερο απ' ό,τι στην υπόλοιπη Ευρώπη. Μια μικρή έκθεση στο χωριό Μεγάλο Χωριό τα παρουσιάζει στους επισκέπτες.", "Tilos has one more secret: in a cave on the island fossils were found of dwarf elephants, just one and a half metres tall, which survived here much longer than in the rest of Europe. A small exhibition in the village of Megalo Chorio presents them to visitors."),
 ],
 "questions": [
  Q("Τι απαγόρευσε η Τήλος από τη δεκαετία του '90;", ["Τα αυτοκίνητα", "Το κυνήγι", "Το ψάρεμα", "Την οικοδομή"], 1, "απαγόρευσαν το κυνήγι"),
  Q("Τι έγινε το 2021;", ["Άνοιξε αεροδρόμιο", "Η Τήλος έγινε το πρώτο νησί χωρίς χωματερή", "Έκλεισε το σπήλαιο", "Χτίστηκε νέο λιμάνι"], 1, "η Τήλος έγινε το πρώτο νησί στην Ελλάδα χωρίς χωματερή"),
  Q("Τι βρέθηκε σε ένα σπήλαιο του νησιού;", ["Αρχαία νομίσματα", "Απολιθώματα από νάνους ελέφαντες", "Βυζαντινές τοιχογραφίες", "Ένα ναυάγιο"], 1, "βρέθηκαν απολιθώματα από νάνους ελέφαντες"),
 ],
 "gloss": {"μόνιμους": "μόνιμος — permanent", "απαγόρευσαν": "απαγορεύω — to ban", "κυνήγι": "κυνήγι — hunting", "υβριδικό": "υβριδικός — hybrid", "ανεμογεννήτρια": "ανεμογεννήτρια — wind turbine", "φωτοβολταϊκά": "φωτοβολταϊκά — solar panels", "χωματερή": "χωματερή — landfill", "απορρίμματα": "απορρίμματα — rubbish, waste", "λίπασμα": "λίπασμα — fertiliser, compost", "απολιθώματα": "απολίθωμα — fossil", "νάνους": "νάνος — dwarf", "επέζησαν": "επιζώ — to survive"},
})

ITEMS.append({
 "id": "l32-int-lyra", "title": "Ο κατασκευαστής λύρας", "title_en": "The lyre-maker", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν κατασκευαστή κρητικής λύρας από το Ρέθυμνο.",
 "script": [
  L("Δημοσιογράφος", "f", "Πόσο καιρό χρειάζεστε για να φτιάξετε μια λύρα;", "How long do you need to make a lyre?"),
  L("Μανόλης", "m", "Για μια καλή λύρα, περίπου ένα μήνα δουλειάς. Το πιο σημαντικό όμως γίνεται πριν: το ξύλο πρέπει να ξεραθεί σωστά, πολλές φορές για χρόνια. Για το σώμα χρησιμοποιώ συνήθως μουριά ή καρυδιά, ενώ για το καπάκι, που δίνει τον ήχο, προτιμώ κέδρο.", "For a good lyre, about a month's work. But the most important part happens before: the wood has to be dried properly, often for years. For the body I usually use mulberry or walnut, while for the soundboard, which gives the sound, I prefer cedar."),
  L("Δημοσιογράφος", "f", "Και το δοξάρι με τα κουδουνάκια;", "And the bow with the little bells?"),
  L("Μανόλης", "m", "Τα γερακοκούδουνα είναι μια παλιά παράδοση. Τα κρεμάμε στο δοξάρι και ακούγονται με κάθε κίνηση του χεριού, σαν να συνοδεύουν τον ρυθμό. Οι νεότεροι λυράρηδες δεν τα θέλουν πάντα, γιατί λένε ότι καλύπτουν τον ήχο, αλλά για μένα είναι η ψυχή της λύρας.", "The hawk bells are an old tradition. We hang them on the bow and they sound with every movement of the hand, as if they accompany the rhythm. Younger lyre players don't always want them, because they say they cover the sound, but for me they are the soul of the lyre."),
  L("Δημοσιογράφος", "f", "Έχετε μαθητές;", "Do you have apprentices?"),
  L("Μανόλης", "m", "Έχω δύο, και το ένα είναι κορίτσι. Πριν από τριάντα χρόνια θα ήταν αδιανόητο. Τώρα πια πολλές κοπέλες παίζουν λύρα στα γλέντια, και αυτό με κάνει να πιστεύω ότι η παράδοση δεν πεθαίνει· απλώς αλλάζει.", "I have two, and one is a girl. Thirty years ago it would have been unthinkable. Now many young women play the lyre at festivities, and that makes me believe the tradition isn't dying; it's just changing."),
 ],
 "questions": [
  Q("Τι είναι το πιο σημαντικό πριν αρχίσει η κατασκευή;", ["Να βρει πελάτη", "Να ξεραθεί σωστά το ξύλο", "Να κουρδίσει τις χορδές", "Να βάψει το σώμα"], 1, "το ξύλο πρέπει να ξεραθεί σωστά"),
  Q("Γιατί κάποιοι νέοι λυράρηδες δεν θέλουν τα γερακοκούδουνα;", ["Γιατί είναι ακριβά", "Γιατί λένε ότι καλύπτουν τον ήχο", "Γιατί είναι βαριά", "Γιατί σπάνε εύκολα"], 1, "λένε ότι καλύπτουν τον ήχο"),
  Q("Τι συμπεραίνει ο Μανόλης για την παράδοση;", ["Ότι θα χαθεί σύντομα", "Ότι δεν πεθαίνει, απλώς αλλάζει", "Ότι ανήκει μόνο στους άντρες", "Ότι πρέπει να μείνει ίδια"], 1, "η παράδοση δεν πεθαίνει· απλώς αλλάζει"),
 ],
 "gloss": {"κατασκευαστή": "κατασκευαστής — maker", "λύρας": "λύρα — (Cretan) lyre", "να ξεραθεί": "ξεραίνομαι — to dry", "μουριά": "μουριά — mulberry tree", "καρυδιά": "καρυδιά — walnut tree", "καπάκι": "καπάκι — lid; soundboard", "κέδρο": "κέδρος — cedar", "δοξάρι": "δοξάρι — bow", "γερακοκούδουνα": "γερακοκούδουνο — hawk bell", "λυράρηδες": "λυράρης — lyre player", "αδιανόητο": "αδιανόητος — unthinkable", "γλέντια": "γλέντι — festivity, party"},
})

ITEMS.append({
 "id": "l32-mono-ygro-pyr", "title": "Το υγρό πυρ των Βυζαντινών", "title_en": "The liquid fire of the Byzantines", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια ιστορικό να μιλάει σε μια διάλεξη για το «υγρό πυρ».",
 "script": [
  L("Ιστορικός", "f", "Το 672, σύμφωνα με τους Βυζαντινούς χρονογράφους, ένας αρχιτέκτονας ονόματι Καλλίνικος, πρόσφυγας από τη Συρία, έφτασε στην Κωνσταντινούπολη φέρνοντας μαζί του ένα μυστικό που έμελλε να αλλάξει την ιστορία: ένα εμπρηστικό υγρό που καιγόταν ακόμη και πάνω στο νερό.", "In 672, according to the Byzantine chroniclers, an architect named Kallinikos, a refugee from Syria, arrived in Constantinople bringing with him a secret that was to change history: an incendiary liquid that burned even on water."),
  L("Ιστορικός", "f", "Οι Βυζαντινοί το εκτόξευαν με σίφωνες από την πλώρη των πολεμικών τους πλοίων, των δρομώνων, και το χρησιμοποίησαν με καταστροφικά αποτελέσματα κατά των αραβικών στόλων που πολιόρκησαν την Πόλη. Οι εχθροί του έδωσαν το όνομα «ελληνικό πυρ», ενώ οι ίδιοι οι Βυζαντινοί το ονόμαζαν «υγρό» ή «θαλάσσιο πυρ».", "The Byzantines projected it with siphons from the prows of their warships, the dromons, and used it with devastating results against the Arab fleets that besieged the City. Their enemies gave it the name «Greek fire», while the Byzantines themselves called it «liquid» or «sea fire»."),
  L("Ιστορικός", "f", "Το πιο εκπληκτικό, ωστόσο, είναι ότι η σύνθεσή του χάθηκε. Ήταν κρατικό μυστικό τόσο αυστηρά φυλαγμένο, ώστε ο αυτοκράτορας Κωνσταντίνος Πορφυρογέννητος συμβούλευε τον γιο του να μην το παραδώσει ποτέ σε ξένους, λέγοντας ότι είχε δοθεί από άγγελο στον Μέγα Κωνσταντίνο. Η γνώση μοιραζόταν σε λίγους, και κανείς δεν ήξερε ολόκληρη τη διαδικασία.", "Most astonishing, however, is that its composition was lost. It was a state secret guarded so strictly that the emperor Constantine Porphyrogennetos advised his son never to hand it over to foreigners, saying that it had been given by an angel to Constantine the Great. The knowledge was shared among a few, and no one knew the entire process."),
  L("Ιστορικός", "f", "Οι σύγχρονοι ερευνητές υποθέτουν ότι η βάση του ήταν πετρέλαιο από τις ακτές της Μαύρης Θάλασσας, ίσως αναμεμειγμένο με ρητίνες. Αλλά καμία ανασύνθεση δεν έχει αναπαραγάγει με βεβαιότητα το αρχικό. Το υγρό πυρ μάς θυμίζει πόσο εύθραυστη είναι η γνώση όταν κρατιέται μυστική: η ίδια η μυστικότητα που το προστάτευε ήταν εκείνη που τελικά το εξαφάνισε.", "Modern researchers suppose that its base was petroleum from the shores of the Black Sea, perhaps mixed with resins. But no reconstruction has reproduced the original with certainty. Liquid fire reminds us how fragile knowledge is when it is kept secret: the very secrecy that protected it was what finally made it vanish."),
 ],
 "questions": [
  Q("Τι ήταν ιδιαίτερο στο υγρό που έφερε ο Καλλίνικος;", ["Ήταν δηλητηριώδες", "Καιγόταν ακόμη και πάνω στο νερό", "Ήταν αόρατο", "Έσβηνε τις φωτιές"], 1, "ένα εμπρηστικό υγρό που καιγόταν ακόμη και πάνω στο νερό"),
  Q("Πώς ονόμαζαν οι ίδιοι οι Βυζαντινοί το όπλο;", ["Ελληνικό πυρ", "Υγρό ή θαλάσσιο πυρ", "Αγγελικό πυρ", "Συριακό πυρ"], 1, "οι ίδιοι οι Βυζαντινοί το ονόμαζαν «υγρό» ή «θαλάσσιο πυρ»"),
  Q("Γιατί χάθηκε η σύνθεσή του;", ["Γιατί κάηκαν τα αρχεία", "Γιατί ήταν αυστηρό μυστικό και κανείς δεν ήξερε όλη τη διαδικασία", "Γιατί το έκλεψαν οι Άραβες", "Γιατί εξαντλήθηκαν τα υλικά"], 1, "κανείς δεν ήξερε ολόκληρη τη διαδικασία"),
  Q("Ποιο είναι το συμπέρασμα της ομιλήτριας;", ["Η μυστικότητα προστατεύει πάντα τη γνώση", "Η μυστικότητα που το προστάτευε τελικά το εξαφάνισε", "Οι σύγχρονοι επιστήμονες το αναπαρήγαγαν", "Το όπλο δεν ήταν ποτέ αποτελεσματικό"], 1, "η ίδια η μυστικότητα που το προστάτευε ήταν εκείνη που τελικά το εξαφάνισε"),
 ],
 "gloss": {"υγρό πυρ": "υγρό πυρ — liquid fire (Greek fire)", "χρονογράφους": "χρονογράφος — chronicler", "πρόσφυγας": "πρόσφυγας — refugee", "έμελλε": "μέλλω (έμελλε να) — was destined to", "εμπρηστικό": "εμπρηστικός — incendiary", "εκτόξευαν": "εκτοξεύω — to launch, project", "σίφωνες": "σίφωνας — siphon", "πλώρη": "πλώρη — prow, bow", "πολιόρκησαν": "πολιορκώ — to besiege", "σύνθεσή": "σύνθεση — composition", "ρητίνες": "ρητίνη — resin", "ανασύνθεση": "ανασύνθεση — reconstruction", "εύθραυστη": "εύθραυστος — fragile", "μυστικότητα": "μυστικότητα — secrecy"},
})

ITEMS.append({
 "id": "l32-int-tetraimero", "title": "Τέσσερις μέρες δουλειά την εβδομάδα;", "title_en": "A four-day working week?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια οικονομολόγο για την εβδομάδα εργασίας τεσσάρων ημερών.",
 "script": [
  L("Δημοσιογράφος", "m", "Σε πολλές χώρες συζητιέται η εβδομάδα εργασίας τεσσάρων ημερών. Τι δείχνουν τα πειράματα που έχουν γίνει;", "In many countries a four-day working week is being discussed. What do the experiments carried out so far show?"),
  L("Οικονομολόγος", "f", "Τα αποτελέσματα είναι ενθαρρυντικά, αλλά θέλουν προσεκτική ανάγνωση. Στη Βρετανία, το 2022, εξήντα περίπου εταιρείες δοκίμασαν το μοντέλο για έξι μήνες χωρίς μείωση μισθών, και οι περισσότερες αποφάσισαν να το διατηρήσουν. Οι εργαζόμενοι ανέφεραν λιγότερη εξουθένωση, ενώ η παραγωγικότητα, κατά μέσο όρο, δεν μειώθηκε.", "The results are encouraging, but they need careful reading. In Britain, in 2022, around sixty companies tried the model for six months without pay cuts, and most decided to keep it. Employees reported less burnout, while productivity, on average, did not fall."),
  L("Δημοσιογράφος", "m", "Γιατί λέτε ότι θέλουν προσεκτική ανάγνωση;", "Why do you say they need careful reading?"),
  L("Οικονομολόγος", "f", "Γιατί οι εταιρείες που συμμετείχαν ήταν εθελοντικές· ήταν, δηλαδή, ήδη πρόθυμες να αλλάξουν. Επιπλέον, το μοντέλο ταιριάζει σε γραφειακές δουλειές πολύ περισσότερο απ' ό,τι σε ένα νοσοκομείο ή ένα εργοστάσιο συνεχούς λειτουργίας, όπου κάποιος πρέπει να είναι εκεί κάθε ώρα.", "Because the participating companies were volunteers; that is, they were already willing to change. Moreover, the model suits office jobs much more than a hospital or a factory in continuous operation, where someone has to be there every hour."),
  L("Δημοσιογράφος", "m", "Και η Ελλάδα; Εδώ πρόσφατα επιτράπηκε σε ορισμένους κλάδους ακόμη και έκτη μέρα εργασίας.", "And Greece? Here a sixth working day was recently even permitted in certain sectors."),
  L("Οικονομολόγος", "f", "Ακριβώς, και αυτό δείχνει πόσο διαφορετικές είναι οι αφετηρίες. Οι Έλληνες εργάζονται από τις περισσότερες ώρες στην Ευρώπη, αλλά η παραγωγικότητα ανά ώρα παραμένει χαμηλή. Το πρόβλημα, λοιπόν, δεν είναι πόσες ώρες δουλεύουμε, αλλά πώς τις αξιοποιούμε. Χωρίς επενδύσεις σε τεχνολογία και οργάνωση, η μείωση του χρόνου εργασίας μπορεί να μείνει ευχολόγιο.", "Exactly, and that shows how different the starting points are. Greeks work some of the longest hours in Europe, but productivity per hour remains low. So the problem isn't how many hours we work, but how we use them. Without investment in technology and organisation, reducing working time may remain wishful thinking."),
 ],
 "questions": [
  Q("Τι έδειξε το βρετανικό πείραμα του 2022;", ["Οι περισσότερες εταιρείες εγκατέλειψαν το μοντέλο", "Οι περισσότερες εταιρείες αποφάσισαν να το διατηρήσουν", "Οι μισθοί μειώθηκαν", "Η παραγωγικότητα έπεσε πολύ"], 1, "οι περισσότερες αποφάσισαν να το διατηρήσουν"),
  Q("Γιατί τα αποτελέσματα χρειάζονται προσεκτική ανάγνωση;", ["Γιατί κράτησαν μόνο μία εβδομάδα", "Γιατί οι εταιρείες ήταν εθελοντικές και ήδη πρόθυμες να αλλάξουν", "Γιατί δεν μετρήθηκε η παραγωγικότητα", "Γιατί ήταν όλες εργοστάσια"], 1, "οι εταιρείες που συμμετείχαν ήταν εθελοντικές"),
  Q("Σε ποιες δουλειές ταιριάζει λιγότερο το μοντέλο;", ["Στις γραφειακές", "Σε θέσεις συνεχούς λειτουργίας, όπως νοσοκομεία", "Στην εκπαίδευση", "Στην πληροφορική"], 1, "ένα νοσοκομείο ή ένα εργοστάσιο συνεχούς λειτουργίας"),
  Q("Ποιο είναι, κατά την οικονομολόγο, το πραγματικό πρόβλημα στην Ελλάδα;", ["Οι λίγες ώρες εργασίας", "Το πώς αξιοποιούνται οι ώρες εργασίας", "Οι υψηλοί μισθοί", "Η έλλειψη εργαζομένων"], 1, "το πρόβλημα, λοιπόν, δεν είναι πόσες ώρες δουλεύουμε, αλλά πώς τις αξιοποιούμε"),
 ],
 "gloss": {"οικονομολόγο": "οικονομολόγος — economist", "ενθαρρυντικά": "ενθαρρυντικός — encouraging", "μείωση": "μείωση — reduction", "μισθών": "μισθός — salary, pay", "εξουθένωση": "εξουθένωση — burnout, exhaustion", "παραγωγικότητα": "παραγωγικότητα — productivity", "πρόθυμες": "πρόθυμος — willing", "γραφειακές": "γραφειακός — office (adj.)", "κλάδους": "κλάδος — sector, branch", "αφετηρίες": "αφετηρία — starting point", "αξιοποιούμε": "αξιοποιώ — to make good use of", "επενδύσεις": "επένδυση — investment", "ευχολόγιο": "ευχολόγιο — wish list, wishful thinking"},
})

rnd = random.Random(32)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-32.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
