# Source for library/listening/listening-243.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l243.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l243-news-agriogata-kamera", "title": "Αγριόγατα καταγράφηκε από κάμερες σε ορεινό δάσος", "title_en": "A wildcat is recorded by cameras in a mountain forest", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός περιφερειακού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνήτρια", "f", "Μια αγριόγατα καταγράφηκε για πρώτη φορά από αυτόματες κάμερες σε ένα δάσος οξιάς της περιοχής. Οι κάμερες είχαν τοποθετηθεί πριν από έναν χρόνο από μια ομάδα βιολόγων, που μελετά τα θηλαστικά του βουνού.", "A wildcat has been recorded for the first time by automatic cameras in a beech forest in the region. The cameras had been placed a year ago by a team of biologists studying the mountain's mammals."),
  L("Εκφωνήτρια", "f", "Η αγριόγατα μοιάζει πολύ με μια μεγάλη ριγωτή γάτα του σπιτιού, αλλά έχει πιο χοντρή ουρά, με μαύρους δακτυλίους και στρογγυλή, μαύρη άκρη. Είναι εξαιρετικά ντροπαλό ζώο και κυνηγά κυρίως τη νύχτα, γι' αυτό σπάνια τη βλέπει άνθρωπος.", "The wildcat looks very much like a large striped house cat, but it has a thicker tail, with black rings and a round, black tip. It is an extremely shy animal and hunts mainly at night, which is why people rarely see it."),
  L("Εκφωνήτρια", "f", "Σύμφωνα με τους ερευνητές, η μεγαλύτερη απειλή για το είδος δεν είναι το κυνήγι, αλλά οι διασταυρώσεις με τις κατοικίδιες γάτες. Όταν γάτες από τα χωριά ζευγαρώνουν με αγριόγατες, τα χαρακτηριστικά του άγριου είδους σιγά σιγά χάνονται.", "According to the researchers, the greatest threat to the species is not hunting but crossbreeding with domestic cats. When cats from the villages mate with wildcats, the characteristics of the wild species are gradually lost."),
  L("Εκφωνήτρια", "f", "Γι' αυτό η ομάδα ζητά από τους κατοίκους των ορεινών χωριών να στειρώνουν τις γάτες τους και να μην τις αφήνουν στο δάσος. Ο δήμος ανακοίνωσε ότι θα καλύψει μέρος του κόστους της στείρωσης.", "That's why the team is asking residents of the mountain villages to neuter their cats and not to leave them in the forest. The municipality announced that it will cover part of the cost of neutering."),
 ],
 "questions": [
  Q("Ποιος είχε τοποθετήσει τις κάμερες;", ["Οι δασοφύλακες", "Μια ομάδα βιολόγων", "Κυνηγοί της περιοχής", "Ο δήμος"], 1, "είχαν τοποθετηθεί πριν από έναν χρόνο από μια ομάδα βιολόγων"),
  Q("Πώς ξεχωρίζει η αγριόγατα από μια γάτα του σπιτιού;", ["Είναι πολύ μικρότερη", "Έχει πιο χοντρή ουρά με μαύρους δακτυλίους", "Έχει κοντά αυτιά", "Είναι εντελώς γκρίζα"], 1, "έχει πιο χοντρή ουρά, με μαύρους δακτυλίους και στρογγυλή, μαύρη άκρη"),
  Q("Ποια είναι η μεγαλύτερη απειλή για το είδος;", ["Το κυνήγι", "Οι διασταυρώσεις με τις κατοικίδιες γάτες", "Οι πυρκαγιές", "Η έλλειψη τροφής"], 1, "η μεγαλύτερη απειλή για το είδος δεν είναι το κυνήγι, αλλά οι διασταυρώσεις"),
  Q("Τι θα κάνει ο δήμος;", ["Θα απαγορεύσει τις γάτες στα χωριά", "Θα καλύψει μέρος του κόστους της στείρωσης", "Θα τοποθετήσει περισσότερες κάμερες", "Θα φτιάξει καταφύγιο για αγριόγατες"], 1, "θα καλύψει μέρος του κόστους της στείρωσης"),
 ],
 "gloss": {"αγριόγατα": "αγριόγατα — wildcat", "οξιάς": "οξιά — beech", "θηλαστικά": "θηλαστικό — mammal", "ριγωτή": "ριγωτός — striped", "δακτυλίους": "δακτύλιος — ring", "ντροπαλό": "ντροπαλός — shy", "διασταυρώσεις": "διασταύρωση — crossbreeding, cross", "κατοικίδιες": "κατοικίδιος — domestic", "ζευγαρώνουν": "ζευγαρώνω — to mate", "στειρώνουν": "στειρώνω — to neuter, spay", "στείρωσης": "στείρωση — neutering"},
})

ITEMS.append({
 "id": "l243-vm-geitonas-drone", "title": "Μήνυμα από τον γείτονα: «Το drone σας είναι στη στέγη μου»", "title_en": "A message from the neighbour: 'Your drone is on my roof'", "type": "voicemail", "level": "B2",
 "context_el": "Ο γιος σας πέταξε χθες ένα μικρό drone στη γειτονιά και το έχασε. Ακούτε ένα μήνυμα που σας άφησε ένας γείτονας στον τηλεφωνητή.",
 "script": [
  L("Γείτονας", "m", "Καλησπέρα, ο Παντελής είμαι, από το σπίτι με τη μεγάλη μουριά, στη γωνία. Νομίζω ότι βρήκα κάτι δικό σας. Σήμερα το πρωί άκουσα έναν θόρυβο στα κεραμίδια, και όταν ανέβηκα με τη σκάλα, βρήκα ένα μικρό drone, άσπρο με κόκκινες έλικες.", "Good evening, it's Pantelis, from the house with the big mulberry tree, on the corner. I think I've found something of yours. This morning I heard a noise on the roof tiles, and when I went up the ladder, I found a small drone, white with red propellers."),
  L("Γείτονας", "m", "Η κυρία από το περίπτερο μου είπε ότι χθες το απόγευμα έψαχνε ο γιος σας κάτι τέτοιο στον δρόμο, γι' αυτό σας παίρνω. Το drone φαίνεται εντάξει, μόνο μία έλικα έχει σπάσει. Το έχω στο σπίτι, σε ένα κουτί, να μην το βρουν τα εγγόνια μου.", "The lady from the kiosk told me your son was looking for something like that in the street yesterday afternoon, which is why I'm calling. The drone seems fine, only one propeller is broken. I've got it at home, in a box, so my grandchildren don't find it."),
  L("Γείτονας", "m", "Δυστυχώς, όταν έπεσε, έσπασε κι ένα κεραμίδι. Δεν είναι τίποτα σοβαρό, αλλά αν βρέξει, θα στάξει νερό στη σοφίτα. Έχω έναν μάστορα που έρχεται το Σάββατο για άλλη δουλειά. Αν θέλετε, να του πω να το αλλάξει και να μοιραστούμε τα έξοδα, θα είναι λίγα ευρώ.", "Unfortunately, when it fell, it also broke a roof tile. It's nothing serious, but if it rains, water will drip into the attic. I've got a builder coming on Saturday for another job. If you like, I'll ask him to replace it and we can share the cost, it'll be a few euros."),
  L("Γείτονας", "m", "Περάστε να το πάρετε όποτε θέλετε, είμαι σπίτι όλο το απόγευμα. Και πείτε στον μικρό να το πετάει καλύτερα στο γήπεδο του σχολείου, εκεί δεν έχει στέγες. Γεια σας.", "Come and get it whenever you like, I'm home all afternoon. And tell the boy to fly it at the school sports ground instead, there are no roofs there. Goodbye."),
 ],
 "questions": [
  Q("Πού βρήκε ο γείτονας το drone;", ["Στη μουριά του", "Πάνω στα κεραμίδια της στέγης", "Στο περίπτερο", "Στο γήπεδο του σχολείου"], 1, "άκουσα έναν θόρυβο στα κεραμίδια, και όταν ανέβηκα με τη σκάλα, βρήκα ένα μικρό drone"),
  Q("Πώς κατάλαβε ότι το drone ήταν του γιου του/της ακροατή/τριας;", ["Είχε γραμμένο το όνομά του", "Του το είπε η κυρία από το περίπτερο", "Το είδε να πέφτει", "Τον πήρε τηλέφωνο ο γιος"], 1, "Η κυρία από το περίπτερο μου είπε ότι χθες το απόγευμα έψαχνε ο γιος σας κάτι τέτοιο"),
  Q("Τι ζημιά έκανε το drone όταν έπεσε;", ["Έσπασε ένα παράθυρο", "Έσπασε ένα κεραμίδι", "Χάλασε την κεραία", "Τρόμαξε τα εγγόνια του"], 1, "όταν έπεσε, έσπασε κι ένα κεραμίδι"),
  Q("Τι προτείνει για την επισκευή;", ["Να την πληρώσει όλη ο/η ακροατής/τρια", "Να αλλάξει το κεραμίδι ο μάστορας και να μοιραστούν τα έξοδα", "Να την κάνει μόνος του", "Να περιμένουν μέχρι το καλοκαίρι"], 1, "να του πω να το αλλάξει και να μοιραστούμε τα έξοδα"),
 ],
 "gloss": {"μουριά": "μουριά — mulberry tree", "κεραμίδια": "κεραμίδι — roof tile", "σκάλα": "σκάλα — ladder", "έλικες": "έλικα — propeller", "περίπτερο": "περίπτερο — kiosk", "στάξει": "στάζω — to drip", "σοφίτα": "σοφίτα — attic", "μάστορα": "μάστορας — builder, craftsman", "έξοδα": "έξοδα — costs, expenses", "γήπεδο": "γήπεδο — sports ground, pitch"},
})

ITEMS.append({
 "id": "l243-c1-mono-grammatosimo", "title": "Ένα κομματάκι χαρτί που άλλαξε την αλληλογραφία: η ιστορία του γραμματοσήμου", "title_en": "A scrap of paper that changed the post: the history of the postage stamp", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν ιστορικό σε μια ραδιοφωνική εκπομπή για τα αντικείμενα της καθημερινής ζωής.",
 "script": [
  L("Ιστορικός", "m", "Πριν από το γραμματόσημο, στις περισσότερες χώρες της Ευρώπης το ταχυδρομικό τέλος δεν το πλήρωνε αυτός που έστελνε το γράμμα, αλλά αυτός που το παραλάμβανε. Και η τιμή εξαρτιόταν από την απόσταση και από τον αριθμό των φύλλων. Πολλοί αρνούνταν απλώς να πληρώσουν, και το γράμμα γύριζε πίσω.", "Before the postage stamp, in most European countries the postage was paid not by the person sending the letter but by the person receiving it. And the price depended on the distance and on the number of sheets. Many people simply refused to pay, and the letter went back."),
  L("Ιστορικός", "m", "Στη Βρετανία, ένας μεταρρυθμιστής, ο Ρόουλαντ Χιλ, πρότεινε κάτι ριζοσπαστικό: μια φθηνή, ενιαία τιμή για όλη τη χώρα, πληρωμένη από πριν. Η απόδειξη της πληρωμής θα ήταν ένα μικρό κολλημένο χαρτάκι. Έτσι, το 1840 κυκλοφόρησε το πρώτο γραμματόσημο, μαύρο, με το προφίλ της νεαρής βασίλισσας Βικτωρίας.", "In Britain, a reformer, Rowland Hill, proposed something radical: a cheap, uniform price for the whole country, paid in advance. The proof of payment would be a small piece of paper stuck on. And so in 1840 the first postage stamp came out, black, with the profile of the young Queen Victoria."),
  L("Ιστορικός", "m", "Η ιδέα εξαπλώθηκε γρήγορα. Η Ελλάδα απέκτησε τα πρώτα της γραμματόσημα το 1861, με το κεφάλι του Ερμή, του αγγελιοφόρου των θεών, και, απ' όσο ξέρουμε, τα πρώτα τυπώθηκαν στο Παρίσι. Μέσα σε λίγες δεκαετίες, ο όγκος της αλληλογραφίας πολλαπλασιάστηκε.", "The idea spread quickly. Greece got its first stamps in 1861, with the head of Hermes, the messenger of the gods, and as far as we know the first ones were printed in Paris. Within a few decades, the volume of mail multiplied."),
  L("Ιστορικός", "m", "Αυτό που μου φαίνεται πιο ενδιαφέρον είναι ότι το γραμματόσημο δεν ήταν τεχνολογική εφεύρεση. Χαρτί και κόλλα υπήρχαν από αιώνες. Ήταν μια οργανωτική ιδέα: άλλαξε το ποιος πληρώνει και πότε. Και συχνά, οι πιο μεγάλες αλλαγές στην καθημερινή ζωή ξεκινούν ακριβώς από τέτοιες απλές, σχεδόν βαρετές αποφάσεις.", "What I find most interesting is that the stamp was not a technological invention. Paper and glue had existed for centuries. It was an organisational idea: it changed who pays and when. And often, the biggest changes in daily life start precisely from such simple, almost boring decisions."),
 ],
 "questions": [
  Q("Ποιος πλήρωνε συνήθως το ταχυδρομικό τέλος πριν από το γραμματόσημο;", ["Ο αποστολέας", "Ο παραλήπτης", "Το κράτος", "Ο ταχυδρόμος"], 1, "αυτός που το παραλάμβανε"),
  Q("Τι πρότεινε ο Ρόουλαντ Χιλ;", ["Ακριβότερα τέλη για τα μακρινά γράμματα", "Μια φθηνή, ενιαία τιμή για όλη τη χώρα, πληρωμένη από πριν", "Δωρεάν αποστολή για τους φτωχούς", "Να καταργηθούν τα γράμματα"], 1, "μια φθηνή, ενιαία τιμή για όλη τη χώρα, πληρωμένη από πριν"),
  Q("Τι απεικόνιζαν τα πρώτα ελληνικά γραμματόσημα;", ["Τον βασιλιά Όθωνα", "Το κεφάλι του Ερμή", "Την Ακρόπολη", "Μια κουκουβάγια"], 1, "με το κεφάλι του Ερμή, του αγγελιοφόρου των θεών"),
  Q("Γιατί, κατά τον ομιλητή, το γραμματόσημο δεν ήταν τεχνολογική εφεύρεση;", ["Γιατί το είχαν εφεύρει οι αρχαίοι", "Γιατί άλλαξε μόνο το ποιος πληρώνει και πότε, με υλικά που υπήρχαν ήδη", "Γιατί δεν χρησιμοποιήθηκε ποτέ ευρέως", "Γιατί ήταν πολύ ακριβό"], 1, "Ήταν μια οργανωτική ιδέα: άλλαξε το ποιος πληρώνει και πότε"),
 ],
 "gloss": {"γραμματόσημο": "γραμματόσημο — postage stamp", "ταχυδρομικό τέλος": "ταχυδρομικό τέλος — postage", "παραλάμβανε": "παραλαμβάνω — to receive", "μεταρρυθμιστής": "μεταρρυθμιστής — reformer", "ριζοσπαστικό": "ριζοσπαστικός — radical", "ενιαία": "ενιαίος — uniform, single", "κολλημένο": "κολλημένος — stuck (on)", "αγγελιοφόρου": "αγγελιοφόρος — messenger", "όγκος": "όγκος — volume", "αλληλογραφίας": "αλληλογραφία — mail, correspondence", "πολλαπλασιάστηκε": "πολλαπλασιάζομαι — to multiply", "οργανωτική": "οργανωτικός — organisational"},
})

ITEMS.append({
 "id": "l243-c1-int-vryologos", "title": "Μια βρυολόγος για τα βρύα, τα μικρά φυτά που αντέχουν τα πάντα", "title_en": "A bryologist on mosses, the little plants that survive everything", "type": "interview", "level": "C1",
 "context_el": "Μια βρυολόγος, δηλαδή μια βοτανολόγος που μελετά τα βρύα, μιλά σε μια ραδιοφωνική εκπομπή για τη φύση.",
 "script": [
  L("Δημοσιογράφος", "m", "Τα βρύα τα πατάμε χωρίς να τα προσέξουμε. Τι είναι αυτό που σας γοητεύει σε αυτά;", "We step on mosses without noticing them. What is it about them that fascinates you?"),
  L("Βρυολόγος", "f", "Η αντοχή τους. Τα βρύα δεν έχουν πραγματικές ρίζες, ούτε αγγεία που να μεταφέρουν νερό μέσα στο φυτό, όπως τα δέντρα. Απορροφούν την υγρασία απευθείας από τα φύλλα τους. Όταν έρθει η ξηρασία, ξεραίνονται εντελώς και μοιάζουν νεκρά. Μόλις όμως βρέξει, μέσα σε λίγες ώρες ξαναζωντανεύουν και αρχίζουν πάλι να φωτοσυνθέτουν, σαν να μην είχε συμβεί τίποτα.", "Their toughness. Mosses don't have real roots, nor vessels to carry water inside the plant, like trees. They absorb moisture directly through their leaves. When drought comes, they dry out completely and look dead. But as soon as it rains, within a few hours they come back to life and start photosynthesising again, as if nothing had happened."),
  L("Δημοσιογράφος", "m", "Έχουν και κάποια πρακτική χρησιμότητα για εμάς;", "Do they also have some practical use for us?"),
  L("Βρυολόγος", "f", "Πολλή. Επειδή παίρνουν ό,τι χρειάζονται από τη βροχή και τον αέρα, είναι πολύ ευαίσθητα στη ρύπανση. Γι' αυτό τα χρησιμοποιούμε ως δείκτες: αν σε μια πόλη εξαφανίζονται ορισμένα είδη, ο αέρας μάλλον χειροτερεύει. Ένα είδος βρύου, το σφάγνο, σχηματίζει τύρφη στους βάλτους του βορρά, που αποθηκεύει τεράστιες ποσότητες άνθρακα. Και στον Πρώτο Παγκόσμιο Πόλεμο, το σφάγνο χρησιμοποιήθηκε σε επιδέσμους, γιατί απορροφά πολλές φορές το βάρος του σε υγρό.", "A lot. Because they take what they need from the rain and the air, they are very sensitive to pollution. That's why we use them as indicators: if certain species disappear in a city, the air is probably getting worse. One kind of moss, sphagnum, forms peat in the bogs of the north, which stores huge amounts of carbon. And in the First World War, sphagnum was used in bandages, because it absorbs many times its weight in liquid."),
  L("Δημοσιογράφος", "m", "Τι θα θέλατε να κάνουν οι ακροατές μας;", "What would you like our listeners to do?"),
  L("Βρυολόγος", "f", "Απλώς να σκύψουν. Πάρτε έναν φακό και κοιτάξτε από κοντά ένα κομμάτι βρύο σε έναν παλιό τοίχο. Θα δείτε ένα ολόκληρο δάσος σε μικρογραφία, με μικροσκοπικά ζωάκια να κυκλοφορούν ανάμεσα στα «δέντρα». Και, παρακαλώ, μην ξεριζώνετε βρύα από τα βουνά για τη φάτνη των Χριστουγέννων. Μεγαλώνουν πολύ, πολύ αργά.", "Simply to bend down. Take a magnifying glass and look closely at a piece of moss on an old wall. You'll see a whole forest in miniature, with tiny creatures moving among the 'trees'. And please, don't pull up moss from the mountains for the Christmas crib. It grows very, very slowly."),
 ],
 "questions": [
  Q("Πώς παίρνουν τα βρύα το νερό που χρειάζονται;", ["Από βαθιές ρίζες", "Απευθείας από τα φύλλα τους", "Από τα δέντρα πάνω στα οποία ζουν", "Μόνο από το έδαφος"], 1, "Απορροφούν την υγρασία απευθείας από τα φύλλα τους"),
  Q("Τι συμβαίνει στα βρύα μετά από μια ξηρασία, όταν βρέξει;", ["Πεθαίνουν οριστικά", "Ξαναζωντανεύουν μέσα σε λίγες ώρες", "Χρειάζονται χρόνια για να συνέλθουν", "Αλλάζουν χρώμα για πάντα"], 1, "μέσα σε λίγες ώρες ξαναζωντανεύουν"),
  Q("Γιατί χρησιμοποιούνται τα βρύα ως δείκτες της ρύπανσης;", ["Γιατί αλλάζουν μυρωδιά", "Γιατί παίρνουν ό,τι χρειάζονται από τη βροχή και τον αέρα", "Γιατί μεγαλώνουν μόνο στις πόλεις", "Γιατί απορροφούν τον θόρυβο"], 1, "Επειδή παίρνουν ό,τι χρειάζονται από τη βροχή και τον αέρα, είναι πολύ ευαίσθητα στη ρύπανση"),
  Q("Τι ζητά η βρυολόγος από τους ακροατές για τα Χριστούγεννα;", ["Να φυτεύουν βρύα στα μπαλκόνια", "Να μην ξεριζώνουν βρύα από τα βουνά για τη φάτνη", "Να αγοράζουν τεχνητά βρύα", "Να ποτίζουν τα βρύα των τοίχων"], 1, "μην ξεριζώνετε βρύα από τα βουνά για τη φάτνη των Χριστουγέννων"),
 ],
 "gloss": {"βρυολόγος": "βρυολόγος — bryologist", "βρύα": "βρύο — moss", "αντοχή": "αντοχή — toughness, endurance", "αγγεία": "αγγείο — vessel (in a plant)", "ξηρασία": "ξηρασία — drought", "φωτοσυνθέτουν": "φωτοσυνθέτω — to photosynthesise", "δείκτες": "δείκτης — indicator", "σφάγνο": "σφάγνο — sphagnum (peat moss)", "τύρφη": "τύρφη — peat", "βάλτους": "βάλτος — bog, marsh", "επιδέσμους": "επίδεσμος — bandage", "μικρογραφία": "μικρογραφία — miniature", "ξεριζώνετε": "ξεριζώνω — to uproot, pull up", "φάτνη": "φάτνη — (Christmas) crib, manger"},
})

rnd = random.Random(243)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-243.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
