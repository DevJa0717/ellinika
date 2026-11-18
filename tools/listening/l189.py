# Source for library/listening/listening-189.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l189.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l189-ann-nychta-me-pitzames-sto-mouseio", "title": "Μια νύχτα με πιτζάμες στο μουσείο", "title_en": "A pyjama night at the museum", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση ενός μουσείου φυσικής ιστορίας στο ραδιόφωνο.",
 "script": [
  L("Εκφωνήτρια", "f", "Το Μουσείο Φυσικής Ιστορίας διοργανώνει το Σάββατο 14 Δεκεμβρίου μια νύχτα με πιτζάμες για παιδιά από επτά ως δώδεκα χρονών. Τα παιδιά θα εξερευνήσουν τις αίθουσες με φακούς, θα λύσουν γρίφους για τα ζώα των εκθεμάτων και θα κοιμηθούν σε υπνόσακους δίπλα στον σκελετό της φάλαινας.", "The Natural History Museum is organising a pyjama night on Saturday 14 December for children aged seven to twelve. The children will explore the halls with torches, solve puzzles about the animals in the exhibits and sleep in sleeping bags next to the whale skeleton."),
  L("Εκφωνήτρια", "f", "Η προσέλευση είναι στις επτά το βράδυ, και οι γονείς παραλαμβάνουν τα παιδιά στις εννιά το πρωί της Κυριακής, μετά το πρωινό. Κάθε παιδί πρέπει να φέρει υπνόσακο, μαξιλάρι, φακό και ένα ζεστό ρούχο, γιατί οι αίθουσες δεν θερμαίνονται τη νύχτα.", "Arrival is at seven in the evening, and parents collect the children at nine on Sunday morning, after breakfast. Each child must bring a sleeping bag, a pillow, a torch and a warm piece of clothing, because the halls are not heated at night."),
  L("Εκφωνήτρια", "f", "Τα παιδιά θα τα συνοδεύουν βιολόγοι και εκπαιδευτικοί του μουσείου, ένας για κάθε οχτώ παιδιά. Οι θέσεις είναι πενήντα, και οι κρατήσεις γίνονται μόνο ηλεκτρονικά. Για παιδιά με αλλεργίες σε τροφές, παρακαλούμε να το δηλώσετε κατά την κράτηση.", "The children will be accompanied by the museum's biologists and educators, one for every eight children. There are fifty places, and bookings are made online only. For children with food allergies, please state this when booking."),
 ],
 "questions": [
  Q("Πού θα κοιμηθούν τα παιδιά;", ["Σε ένα ξενοδοχείο δίπλα στο μουσείο", "Σε σκηνές στην αυλή", "Δίπλα στον σκελετό της φάλαινας", "Στο εστιατόριο του μουσείου"], 2, "θα κοιμηθούν σε υπνόσακους δίπλα στον σκελετό της φάλαινας"),
  Q("Γιατί πρέπει τα παιδιά να φέρουν ζεστό ρούχο;", ["Γιατί οι αίθουσες δεν θερμαίνονται τη νύχτα", "Γιατί θα βγουν έξω για παρατήρηση", "Γιατί είναι χειμώνας και θα χιονίσει", "Γιατί θα πάνε στο υπόγειο"], 0, "γιατί οι αίθουσες δεν θερμαίνονται τη νύχτα"),
  Q("Τι πρέπει να δηλώσουν οι γονείς κατά την κράτηση;", ["Την ηλικία του παιδιού", "Αν το παιδί έχει αλλεργίες σε τροφές", "Τι ώρα θα το παραλάβουν", "Αν θα μείνουν κι εκείνοι"], 1, "Για παιδιά με αλλεργίες σε τροφές, παρακαλούμε να το δηλώσετε κατά την κράτηση"),
 ],
 "gloss": {"πιτζάμες": "πιτζάμα — pyjamas", "γρίφους": "γρίφος — puzzle, riddle", "εκθεμάτων": "έκθεμα — exhibit", "υπνόσακους": "υπνόσακος — sleeping bag", "προσέλευση": "προσέλευση — arrival", "θερμαίνονται": "θερμαίνομαι — to be heated"},
})

ITEMS.append({
 "id": "l189-int-maestros-mantolinatas", "title": "Η μαέστρος της μαντολινάτας", "title_en": "The conductor of the mandolin orchestra", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με τη μαέστρο μιας ορχήστρας με μαντολίνα στην Κέρκυρα.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι είναι ακριβώς μια μαντολινάτα;", "What exactly is a mandolinata?"),
  L("Μαέστρος", "f", "Είναι μια ορχήστρα με νυκτά όργανα: μαντολίνα, μαντόλες, κιθάρες και ένα κοντραμπάσο. Στα Επτάνησα η παράδοση αυτή ήρθε από την Ιταλία, και στην Κέρκυρα υπάρχουν μαντολινάτες εδώ και πάνω από έναν αιώνα. Η δική μας έχει τριάντα μέλη, από δώδεκα ως ογδόντα χρονών.", "It's an orchestra of plucked instruments: mandolins, mandolas, guitars and a double bass. In the Ionian Islands this tradition came from Italy, and on Corfu there have been mandolin orchestras for over a century. Ours has thirty members, aged from twelve to eighty."),
  L("Δημοσιογράφος", "m", "Πώς τα πάνε μαζί ένας δωδεκάχρονος και ένας ογδοντάρης;", "How do a twelve-year-old and an eighty-year-old get on together?"),
  L("Μαέστρος", "f", "Καλύτερα απ' ό,τι φαντάζεστε. Οι μεγάλοι έχουν την εμπειρία και ξέρουν τα παλιά κομμάτια απ' έξω. Οι μικροί διαβάζουν πιο γρήγορα την παρτιτούρα. Στις πρόβες βλέπω συχνά έναν παππού να δείχνει σε ένα παιδί πώς να κρατά την πένα.", "Better than you'd imagine. The older ones have the experience and know the old pieces by heart. The young ones read the score faster. At rehearsals I often see a grandfather showing a child how to hold the plectrum."),
  L("Δημοσιογράφος", "m", "Τι παίζετε;", "What do you play?"),
  L("Μαέστρος", "f", "Από επτανησιακές καντάδες μέχρι Βιβάλντι και κινηματογραφική μουσική. Το καλοκαίρι κάνουμε συναυλίες στις πλατείες των χωριών, και η μεγαλύτερη χαρά μου είναι όταν οι γιαγιάδες τραγουδούν μαζί μας τις καντάδες που άκουγαν από τα παράθυρα όταν ήταν κορίτσια.", "From Ionian serenades to Vivaldi and film music. In summer we give concerts in village squares, and my greatest joy is when the grandmothers sing along with us the serenades they used to hear from their windows as girls."),
 ],
 "questions": [
  Q("Από πού ήρθε η παράδοση της μαντολινάτας στα Επτάνησα;", ["Από την Ιταλία", "Από την Αθήνα", "Από τη Γαλλία", "Από την Κρήτη"], 0, "Στα Επτάνησα η παράδοση αυτή ήρθε από την Ιταλία"),
  Q("Τι προσφέρουν οι μικρότεροι στην ορχήστρα;", ["Ξέρουν τα παλιά κομμάτια απ' έξω", "Παίζουν πιο δυνατά", "Διαβάζουν πιο γρήγορα την παρτιτούρα", "Φέρνουν καινούργια όργανα"], 2, "Οι μικροί διαβάζουν πιο γρήγορα την παρτιτούρα"),
  Q("Ποια είναι η μεγαλύτερη χαρά της μαέστρου;", ["Να παίζουν στο εξωτερικό", "Να κερδίζουν διαγωνισμούς", "Να ηχογραφούν δίσκους", "Να τραγουδούν οι γιαγιάδες μαζί τους τις καντάδες"], 3, "όταν οι γιαγιάδες τραγουδούν μαζί μας τις καντάδες"),
 ],
 "gloss": {"μαντολινάτα": "μαντολινάτα — mandolin orchestra", "νυκτά": "νυκτός — plucked (instrument)", "κοντραμπάσο": "κοντραμπάσο — double bass", "παρτιτούρα": "παρτιτούρα — musical score", "πένα": "πένα — plectrum, pick", "καντάδες": "καντάδα — serenade (Ionian song)"},
})

ITEMS.append({
 "id": "l189-vm-violi-apo-ton-organopoio", "title": "Το βιολί σας είναι σχεδόν έτοιμο", "title_en": "Your violin is almost ready", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε αφήσει το βιολί σας για επισκευή σε έναν οργανοποιό. Ακούτε ένα μήνυμα που σας άφησε στον τηλεφωνητή.",
 "script": [
  L("Οργανοποιός", "m", "Καλησπέρα, από το εργαστήριο σας παίρνω, για το βιολί που μου φέρατε την περασμένη εβδομάδα. Η ρωγμή στο καπάκι κόλλησε πολύ καλά και δεν φαίνεται σχεδόν καθόλου. Άλλαξα επίσης τη γέφυρα, που ήταν στραβή, και τις χορδές, όπως είχαμε συμφωνήσει.", "Good evening, I'm calling from the workshop, about the violin you brought me last week. The crack in the top has glued very well and is almost invisible. I also changed the bridge, which was warped, and the strings, as we had agreed."),
  L("Οργανοποιός", "m", "Βρήκα όμως και κάτι που δεν είχαμε δει: η ψυχή, το μικρό ξυλάκι μέσα στο σώμα του οργάνου, έχει μετακινηθεί, και γι' αυτό ο ήχος ήταν τόσο πνιχτός. Αν θέλετε, μπορώ να τη διορθώσω. Θα κοστίσει τριάντα ευρώ ακόμα και θα χρειαστώ δύο μέρες.", "But I also found something we hadn't noticed: the soundpost, the small piece of wood inside the body of the instrument, has shifted, and that's why the sound was so muffled. If you like, I can fix it. It will cost another thirty euros and I'll need two days."),
  L("Οργανοποιός", "m", "Πείτε μου μέχρι αύριο το μεσημέρι αν θέλετε να το κάνω, για να το έχετε πριν από τη συναυλία σας την Κυριακή. Και κάτι ακόμα: μην το αφήνετε δίπλα στο καλοριφέρ, η ξηρασία είναι ο μεγαλύτερος εχθρός του ξύλου.", "Let me know by tomorrow midday if you want me to do it, so you have it before your concert on Sunday. And one more thing: don't leave it next to the radiator; dryness is wood's greatest enemy."),
 ],
 "questions": [
  Q("Τι έχει ήδη επισκευάσει ο οργανοποιός;", ["Τη ρωγμή, τη γέφυρα και τις χορδές", "Μόνο τις χορδές", "Τη θήκη του βιολιού", "Το δοξάρι"], 0, "Η ρωγμή στο καπάκι κόλλησε πολύ καλά"),
  Q("Γιατί ο ήχος του βιολιού ήταν πνιχτός;", ["Γιατί οι χορδές ήταν παλιές", "Γιατί η γέφυρα ήταν στραβή", "Γιατί είχε μετακινηθεί η ψυχή", "Γιατί είχε ραγίσει το καπάκι"], 2, "η ψυχή, το μικρό ξυλάκι μέσα στο σώμα του οργάνου, έχει μετακινηθεί"),
  Q("Τι συμβουλεύει ο οργανοποιός;", ["Να παίζει κάθε μέρα", "Να μην αφήνει το βιολί δίπλα στο καλοριφέρ", "Να αλλάζει χορδές κάθε μήνα", "Να το φέρνει για έλεγχο κάθε χρόνο"], 1, "μην το αφήνετε δίπλα στο καλοριφέρ"),
 ],
 "gloss": {"οργανοποιό": "οργανοποιός — instrument maker, luthier", "ρωγμή": "ρωγμή — crack", "καπάκι": "καπάκι — top (of a violin)", "γέφυρα": "γέφυρα — bridge", "χορδές": "χορδή — string", "πνιχτός": "πνιχτός — muffled", "ξηρασία": "ξηρασία — dryness"},
})

ITEMS.append({
 "id": "l189-mon-tetradio-me-ta-genethlia", "title": "Το τετράδιο με τα γενέθλια", "title_en": "The birthday notebook", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλά σε μια ραδιοφωνική εκπομπή για μια συνήθειά της.",
 "script": [
  L("Γυναίκα", "f", "Οι φίλοι μου λένε ότι δεν ξεχνάω ποτέ τα γενέθλια κανενός, και νομίζουν ότι έχω καταπληκτική μνήμη. Η αλήθεια είναι πιο απλή: έχω ένα μικρό κόκκινο τετράδιο, που μου το χάρισε η μητέρα μου όταν ήμουν δεκατρία χρονών, και εκεί γράφω όλες τις ημερομηνίες.", "My friends say I never forget anyone's birthday, and they think I have an amazing memory. The truth is simpler: I have a small red notebook, which my mother gave me when I was thirteen, and that's where I write all the dates."),
  L("Γυναίκα", "f", "Ξέρω ότι το κινητό σού θυμίζει τα γενέθλια μόνο του. Αλλά στο τετράδιο δεν γράφω μόνο ημερομηνίες. Δίπλα σε κάθε όνομα σημειώνω τι δώρο του πήρα, τι του άρεσε, πού ήμασταν. Έτσι δεν χαρίζω ποτέ το ίδιο βιβλίο δύο φορές.", "I know the phone reminds you of birthdays on its own. But in the notebook I don't only write dates. Next to each name I note what present I got them, what they liked, where we were. That way I never give the same book twice."),
  L("Γυναίκα", "f", "Κάθε Ιανουάριο το ξεφυλλίζω από την αρχή. Μερικά ονόματα είναι διαγραμμένα, γιατί αυτοί οι άνθρωποι δεν ζουν πια· δεν τα σβήνω όμως, τα αφήνω εκεί. Και κάθε χρόνο προστίθενται καινούργια: τα παιδιά των φίλων μου, οι συνάδελφοι, ο γείτονας από τον τρίτο.", "Every January I leaf through it from the beginning. Some names are crossed out, because those people are no longer alive; but I don't erase them, I leave them there. And every year new ones are added: my friends' children, colleagues, the neighbour from the third floor."),
 ],
 "questions": [
  Q("Πώς θυμάται τα γενέθλια των φίλων της;", ["Έχει καταπληκτική μνήμη", "Τα γράφει σε ένα τετράδιο", "Της τα θυμίζει το κινητό", "Τα θυμάται η μητέρα της"], 1, "έχω ένα μικρό κόκκινο τετράδιο"),
  Q("Τι σημειώνει δίπλα σε κάθε όνομα;", ["Το τηλέφωνο και τη διεύθυνση", "Μόνο την ημερομηνία", "Τι δώρο του πήρε, τι του άρεσε και πού ήταν", "Πόσων χρονών είναι"], 2, "Δίπλα σε κάθε όνομα σημειώνω τι δώρο του πήρα"),
  Q("Τι κάνει με τα ονόματα των ανθρώπων που δεν ζουν πια;", ["Τα σβήνει", "Τα γράφει σε άλλο τετράδιο", "Σκίζει τη σελίδα", "Τα αφήνει στο τετράδιο"], 3, "δεν τα σβήνω όμως, τα αφήνω εκεί"),
 ],
 "gloss": {"καταπληκτική": "καταπληκτικός — amazing", "χάρισε": "χαρίζω — to give (as a present)", "ξεφυλλίζω": "ξεφυλλίζω — to leaf through", "διαγραμμένα": "διαγραμμένος — crossed out", "προστίθενται": "προστίθεμαι — to be added", "συνάδελφοι": "συνάδελφος — colleague"},
})

ITEMS.append({
 "id": "l189-dia-karavaki-i-dentro", "title": "Καραβάκι ή δέντρο φέτος;", "title_en": "A little boat or a tree this year?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά τι θα στολίσει φέτος τα Χριστούγεννα.",
 "script": [
  L("Ελένη", "f", "Φέτος λέω να μην πάρουμε δέντρο. Θα στολίσουμε καραβάκι, όπως έκανε η γιαγιά μου στη Σύρο.", "This year I'm thinking we don't get a tree. We'll decorate a little boat, like my grandmother did on Syros."),
  L("Άρης", "m", "Καραβάκι; Τα παιδιά θα στεναχωρηθούν. Πού θα βάζουμε τα δώρα, μέσα στο αμπάρι;", "A boat? The children will be upset. Where will we put the presents, in the hold?"),
  L("Ελένη", "f", "Τα δώρα θα τα βάζουμε από κάτω, όπως και στο δέντρο. Το καραβάκι είναι ελληνικό έθιμο, Άρη. Οι γυναίκες στα νησιά το στόλιζαν για να γυρίσουν σώοι οι ναυτικοί. Και θα το φτιάξουμε μαζί με τα παιδιά, από ξύλο, με πανιά από ύφασμα.", "We'll put the presents underneath, just like with the tree. The boat is a Greek custom, Aris. Women on the islands decorated it so the sailors would come home safe. And we'll make it together with the children, out of wood, with fabric sails."),
  L("Άρης", "m", "Αυτό μου αρέσει περισσότερο. Αλλά να ξέρεις ότι ο μικρός θα ζητήσει και φωτάκια, και αστέρι στην κορυφή του καταρτιού.", "I like that better. But you should know the little one will ask for lights too, and a star on top of the mast."),
  L("Ελένη", "f", "Ας κάνουμε συμφωνία: φέτος καραβάκι με φωτάκια, και του χρόνου ψηφίζουμε όλοι μαζί.", "Let's make a deal: this year a boat with lights, and next year we all vote together."),
 ],
 "questions": [
  Q("Πού στόλιζε καραβάκι η γιαγιά της Ελένης;", ["Στην Αθήνα", "Στη Σύρο", "Στην Κρήτη", "Στη Θεσσαλονίκη"], 1, "όπως έκανε η γιαγιά μου στη Σύρο"),
  Q("Γιατί στόλιζαν παλιά το καραβάκι οι γυναίκες στα νησιά;", ["Για να γυρίσουν σώοι οι ναυτικοί", "Γιατί δεν υπήρχαν δέντρα", "Για να φέρει τύχη στο ψάρεμα", "Για να το δουν οι επισκέπτες"], 0, "Οι γυναίκες στα νησιά το στόλιζαν για να γυρίσουν σώοι οι ναυτικοί"),
  Q("Ποια συμφωνία προτείνει τελικά η Ελένη;", ["Να στολίσουν και δέντρο και καραβάκι", "Να μη στολίσουν τίποτα", "Να αποφασίσουν τα παιδιά μόνα τους", "Φέτος καραβάκι με φωτάκια και του χρόνου ψηφοφορία"], 3, "φέτος καραβάκι με φωτάκια, και του χρόνου ψηφίζουμε όλοι μαζί"),
 ],
 "gloss": {"καραβάκι": "καραβάκι — little boat", "αμπάρι": "αμπάρι — hold (of a ship)", "έθιμο": "έθιμο — custom", "σώοι": "σώος — safe, unharmed", "πανιά": "πανί — sail", "καταρτιού": "κατάρτι — mast"},
})

ITEMS.append({
 "id": "l189-news-protochronia-choris-pyrotechnimata", "title": "Πρωτοχρονιά χωρίς πυροτεχνήματα", "title_en": "New Year without fireworks", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο τοπικό δελτίο ειδήσεων λίγες εβδομάδες πριν από την Πρωτοχρονιά.",
 "script": [
  L("Παρουσιαστής", "m", "Ο δήμος αποφάσισε φέτος να μην κάνει τα καθιερωμένα πυροτεχνήματα στην παραλία τα μεσάνυχτα της Πρωτοχρονιάς. Τη θέση τους θα πάρει μια παράσταση με φώτα και ντρόνους πάνω από τη θάλασσα, που θα διαρκέσει δεκαπέντε λεπτά.", "This year the municipality decided not to hold the customary fireworks on the beach at midnight on New Year's Eve. Their place will be taken by a light and drone show over the sea, lasting fifteen minutes."),
  L("Παρουσιαστής", "m", "Η απόφαση πάρθηκε ύστερα από αίτημα φιλοζωικών οργανώσεων και κατοίκων. Όπως εξηγούν, ο δυνατός θόρυβος τρομάζει τα κατοικίδια και τα πουλιά, και κάθε χρόνο, μετά την Πρωτοχρονιά, οι οργανώσεις δέχονται δεκάδες τηλεφωνήματα για σκυλιά που χάθηκαν επειδή έφυγαν τρομαγμένα από τα σπίτια τους.", "The decision was taken after a request from animal welfare organisations and residents. As they explain, the loud noise frightens pets and birds, and every year, after New Year, the organisations receive dozens of calls about dogs that got lost because they ran away from home in fright."),
  L("Παρουσιαστής", "m", "Δεν συμφωνούν όλοι. Ορισμένοι καταστηματάρχες της παραλίας λένε ότι τα πυροτεχνήματα φέρνουν κόσμο και φοβούνται ότι η νέα παράσταση δεν θα έχει την ίδια επιτυχία. Ο δήμος απαντά ότι θα αξιολογήσει το αποτέλεσμα και θα αποφασίσει για του χρόνου.", "Not everyone agrees. Some shop owners on the seafront say the fireworks bring crowds and fear the new show won't be as successful. The municipality replies that it will assess the outcome and decide about next year."),
 ],
 "questions": [
  Q("Τι θα γίνει φέτος στη θέση των πυροτεχνημάτων;", ["Μια συναυλία", "Μια παράσταση με φώτα και ντρόνους", "Τίποτα", "Ένας χορός στην πλατεία"], 1, "Τη θέση τους θα πάρει μια παράσταση με φώτα και ντρόνους"),
  Q("Γιατί ζήτησαν οι φιλοζωικές οργανώσεις να σταματήσουν τα πυροτεχνήματα;", ["Γιατί ο θόρυβος τρομάζει τα κατοικίδια και τα πουλιά", "Γιατί κοστίζουν πολύ", "Γιατί προκαλούν πυρκαγιές", "Γιατί ρυπαίνουν τη θάλασσα"], 0, "ο δυνατός θόρυβος τρομάζει τα κατοικίδια και τα πουλιά"),
  Q("Τι φοβούνται ορισμένοι καταστηματάρχες;", ["Ότι θα κλείσουν τα μαγαζιά τους νωρίτερα", "Ότι θα αυξηθούν οι φόροι", "Ότι οι ντρόνοι είναι επικίνδυνοι", "Ότι η νέα παράσταση δεν θα έχει την ίδια επιτυχία"], 3, "φοβούνται ότι η νέα παράσταση δεν θα έχει την ίδια επιτυχία"),
 ],
 "gloss": {"καθιερωμένα": "καθιερωμένος — customary", "πυροτεχνήματα": "πυροτέχνημα — firework", "ντρόνους": "ντρόνος — drone", "φιλοζωικών": "φιλοζωικός — animal welfare", "καταστηματάρχες": "καταστηματάρχης — shop owner", "αξιολογήσει": "αξιολογώ — to assess"},
})

ITEMS.append({
 "id": "l189-rep-raptiki-sto-gymnasio", "title": "Ραπτική στο γυμνάσιο", "title_en": "Sewing at secondary school", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα πρόγραμμα σε ένα γυμνάσιο της Πάτρας.",
 "script": [
  L("Ρεπόρτερ", "f", "Σε μια αίθουσα ενός γυμνασίου της Πάτρας, δεκαπέντε μαθητές σκύβουν πάνω από ραπτομηχανές. Δεν είναι μάθημα του προγράμματος, αλλά ένας όμιλος που γίνεται κάθε Τετάρτη απόγευμα. Τον οργάνωσε μια καθηγήτρια οικονομικών, που έμαθε ράψιμο από τη γιαγιά της.", "In a classroom at a secondary school in Patras, fifteen pupils are bent over sewing machines. It isn't a timetabled lesson but a club that meets every Wednesday afternoon. It was organised by an economics teacher who learned sewing from her grandmother."),
  L("Ρεπόρτερ", "f", "Οι μαθητές ξεκίνησαν με τα απλά: να ράβουν ένα κουμπί, να κονταίνουν ένα παντελόνι, να μπαλώνουν μια τρύπα. Τώρα φτιάχνουν τσάντες από παλιά τζιν και κουρτίνες για τη βιβλιοθήκη του σχολείου. Η μισή ομάδα είναι αγόρια, κάτι που, όπως λέει η καθηγήτρια, ξάφνιασε αρχικά τους γονείς.", "The pupils started with the basics: sewing on a button, shortening a pair of trousers, patching a hole. Now they make bags from old jeans and curtains for the school library. Half the group are boys, something which, the teacher says, surprised the parents at first."),
  L("Ρεπόρτερ", "f", "Στο τέλος της χρονιάς ο όμιλος θα οργανώσει μια επίδειξη μόδας με ρούχα που έχουν μεταποιήσει οι ίδιοι οι μαθητές. «Πριν, όταν σκιζόταν ένα ρούχο, το πετούσα», μας λέει ένας μαθητής. «Τώρα το φτιάχνω μόνος μου, και η μητέρα μου μού φέρνει και τα δικά της».", "At the end of the year the club will organise a fashion show with clothes altered by the pupils themselves. \"Before, when a piece of clothing tore, I threw it away,\" a pupil tells us. \"Now I fix it myself, and my mother brings me hers too.\""),
 ],
 "questions": [
  Q("Πότε γίνεται ο όμιλος ραπτικής;", ["Κάθε πρωί πριν από τα μαθήματα", "Το Σάββατο", "Κάθε Τετάρτη απόγευμα", "Μία φορά τον μήνα"], 2, "ένας όμιλος που γίνεται κάθε Τετάρτη απόγευμα"),
  Q("Τι φτιάχνουν τώρα οι μαθητές;", ["Τσάντες από παλιά τζιν και κουρτίνες για τη βιβλιοθήκη", "Στολές για την ομάδα του σχολείου", "Κοστούμια για το θέατρο", "Παιχνίδια για ένα νηπιαγωγείο"], 0, "Τώρα φτιάχνουν τσάντες από παλιά τζιν και κουρτίνες για τη βιβλιοθήκη του σχολείου"),
  Q("Τι ξάφνιασε αρχικά τους γονείς;", ["Ότι ο όμιλος είναι δωρεάν", "Ότι η μισή ομάδα είναι αγόρια", "Ότι οι μαθητές πουλούν τα ρούχα", "Ότι η καθηγήτρια διδάσκει οικονομικά"], 1, "Η μισή ομάδα είναι αγόρια, κάτι που, όπως λέει η καθηγήτρια, ξάφνιασε αρχικά τους γονείς"),
 ],
 "gloss": {"ραπτομηχανές": "ραπτομηχανή — sewing machine", "όμιλος": "όμιλος — club", "κονταίνουν": "κονταίνω — to shorten", "μπαλώνουν": "μπαλώνω — to patch", "επίδειξη μόδας": "επίδειξη μόδας — fashion show", "μεταποιήσει": "μεταποιώ — to alter (clothes)"},
})

ITEMS.append({
 "id": "l189-c1-ereunitria-ichotopiou", "title": "Η ερευνήτρια που ηχογραφεί την πόλη", "title_en": "The researcher who records the city", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια ερευνήτρια που μελετά το ηχοτοπίο των πόλεων.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι εννοούμε όταν λέμε «ηχοτοπίο»;", "What do we mean when we say \"soundscape\"?"),
  L("Ερευνήτρια", "f", "Το σύνολο των ήχων ενός τόπου, όπως τους αντιλαμβάνονται οι άνθρωποι που ζουν εκεί. Δεν μετράμε μόνο πόσα ντεσιμπέλ έχει ένας δρόμος· μας ενδιαφέρει τι ακούγεται και πώς το βιώνουν οι κάτοικοι. Ένα σιντριβάνι και ένας δρόμος με κίνηση μπορεί να έχουν την ίδια ένταση, αλλά τα αισθανόμαστε εντελώς διαφορετικά.", "The totality of the sounds of a place, as perceived by the people who live there. We don't only measure how many decibels a street has; we are interested in what can be heard and how residents experience it. A fountain and a busy road may have the same loudness, but we feel them completely differently."),
  L("Δημοσιογράφος", "m", "Πώς γίνεται η έρευνα στην πράξη;", "How is the research done in practice?"),
  L("Ερευνήτρια", "f", "Κάνουμε τους λεγόμενους ηχοπεριπάτους. Περπατάμε με μια ομάδα κατοίκων σε μια διαδρομή, χωρίς να μιλάμε, και σε κάθε στάση σημειώνουν τι ακούνε και πώς νιώθουν. Παράλληλα ηχογραφούμε. Συχνά οι κάτοικοι εκπλήσσονται: ανακαλύπτουν πουλιά ή καμπάνες που δεν είχαν προσέξει ποτέ, μολονότι περνούν από εκεί κάθε μέρα.", "We do what are called soundwalks. We walk a route with a group of residents, without talking, and at each stop they note what they hear and how they feel. At the same time we record. Residents are often surprised: they discover birds or bells they had never noticed, even though they pass by every day."),
  L("Δημοσιογράφος", "m", "Και τι μπορεί να κάνει μια πόλη με αυτά τα στοιχεία;", "And what can a city do with this data?"),
  L("Ερευνήτρια", "f", "Να σχεδιάσει διαφορετικά. Αντί να σκέφτεται μόνο πώς θα μειώσει τον θόρυβο, μπορεί να προστατεύσει τους ήχους που οι κάτοικοι αγαπούν. Σε μια γειτονιά που μελετήσαμε, οι κάτοικοι ζήτησαν να μην κοπεί ένας γέρικος πλάτανος, όχι για τη σκιά, αλλά για τα τζιτζίκια του. Αυτό δεν θα το έβρισκε κανένα ηχόμετρο.", "Design differently. Instead of thinking only about how to reduce noise, it can protect the sounds residents love. In one neighbourhood we studied, residents asked that an old plane tree not be cut down, not for the shade, but for its cicadas. No sound meter would have found that."),
 ],
 "questions": [
  Q("Τι ενδιαφέρει την ερευνήτρια πέρα από τα ντεσιμπέλ;", ["Μόνο η ένταση του θορύβου", "Τι ακούγεται και πώς το βιώνουν οι κάτοικοι", "Πόσο κοστίζει η ηχομόνωση", "Οι ήχοι μέσα στα σπίτια"], 1, "μας ενδιαφέρει τι ακούγεται και πώς το βιώνουν οι κάτοικοι"),
  Q("Τι ανακαλύπτουν συχνά οι κάτοικοι στους ηχοπεριπάτους;", ["Ότι η γειτονιά τους είναι πιο θορυβώδης απ' ό,τι νόμιζαν", "Ότι δεν ακούνε καλά", "Πουλιά ή καμπάνες που δεν είχαν προσέξει ποτέ", "Ότι προτιμούν τη σιωπή"], 2, "ανακαλύπτουν πουλιά ή καμπάνες που δεν είχαν προσέξει ποτέ"),
  Q("Γιατί ζήτησαν οι κάτοικοι να μην κοπεί ο πλάτανος;", ["Για τη σκιά του", "Γιατί ήταν πολύ παλιός", "Γιατί εμπόδιζε τον θόρυβο των αυτοκινήτων", "Για τα τζιτζίκια του"], 3, "όχι για τη σκιά, αλλά για τα τζιτζίκια του"),
 ],
 "gloss": {"ηχοτοπίο": "ηχοτοπίο — soundscape", "αντιλαμβάνονται": "αντιλαμβάνομαι — to perceive", "ντεσιμπέλ": "ντεσιμπέλ — decibel", "βιώνουν": "βιώνω — to experience", "ηχοπεριπάτους": "ηχοπερίπατος — soundwalk", "εκπλήσσονται": "εκπλήσσομαι — to be surprised", "μολονότι": "μολονότι — even though", "ηχόμετρο": "ηχόμετρο — sound level meter"},
})

ITEMS.append({
 "id": "l189-c1-giati-oi-zevres-echoun-rigez", "title": "Γιατί οι ζέβρες έχουν ρίγες;", "title_en": "Why do zebras have stripes?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια επιστημονική εκπομπή στο ραδιόφωνο που εξηγεί ένα ερώτημα της βιολογίας.",
 "script": [
  L("Παρουσιάστρια", "f", "Το ερώτημα γιατί οι ζέβρες έχουν ρίγες απασχολεί τους βιολόγους από την εποχή του Δαρβίνου. Έχουν προταθεί πολλές εξηγήσεις: ότι οι ρίγες μπερδεύουν τα λιοντάρια, ότι βοηθούν τη ζέβρα να δροσίζεται ή ότι λειτουργούν σαν ταυτότητα, αφού κάθε ζώο έχει διαφορετικό σχέδιο.", "The question of why zebras have stripes has occupied biologists since Darwin's time. Many explanations have been proposed: that the stripes confuse lions, that they help the zebra stay cool, or that they act as an identity card, since each animal has a different pattern."),
  L("Παρουσιάστρια", "f", "Τα τελευταία χρόνια όμως κερδίζει έδαφος μια λιγότερο αναμενόμενη εξήγηση: οι ρίγες φαίνεται να προστατεύουν από τις μύγες που τσιμπούν. Σε ένα πείραμα, ερευνητές έντυσαν άλογα με ριγέ κουβέρτες και παρατήρησαν ότι οι μύγες πλησίαζαν, αλλά δυσκολεύονταν να προσγειωθούν πάνω τους, σαν να έχαναν τον προσανατολισμό τους την τελευταία στιγμή.", "In recent years, however, a less expected explanation has been gaining ground: stripes seem to protect against biting flies. In one experiment, researchers dressed horses in striped blankets and observed that the flies approached but had difficulty landing on them, as if they lost their bearings at the last moment."),
  L("Παρουσιάστρια", "f", "Αυτό έχει σημασία, γιατί στις περιοχές της Αφρικής όπου ζουν οι ζέβρες οι μύγες αυτές μεταδίδουν σοβαρές ασθένειες. Οι επιστήμονες πάντως είναι προσεκτικοί: δεν αποκλείεται οι ρίγες να εξυπηρετούν περισσότερους από έναν σκοπούς ταυτόχρονα. Η φύση, όπως συχνά συμβαίνει, σπάνια δίνει μία μόνο απάντηση.", "This matters, because in the parts of Africa where zebras live these flies transmit serious diseases. Scientists are cautious, though: it is not ruled out that the stripes serve more than one purpose at the same time. Nature, as often happens, rarely gives just one answer."),
 ],
 "questions": [
  Q("Ποια από τις παρακάτω ΔΕΝ αναφέρεται ως παλιότερη εξήγηση για τις ρίγες;", ["Ότι μπερδεύουν τα λιοντάρια", "Ότι βοηθούν τη ζέβρα να δροσίζεται", "Ότι λειτουργούν σαν ταυτότητα", "Ότι προσελκύουν ταίρι"], 3, "Έχουν προταθεί πολλές εξηγήσεις"),
  Q("Τι παρατήρησαν οι ερευνητές στο πείραμα με τα άλογα;", ["Οι μύγες δυσκολεύονταν να προσγειωθούν στις ριγέ κουβέρτες", "Τα άλογα δεν ήθελαν να φορέσουν τις κουβέρτες", "Οι μύγες δεν πλησίαζαν καθόλου", "Τα άλογα δροσίζονταν περισσότερο"], 0, "οι μύγες πλησίαζαν, αλλά δυσκολεύονταν να προσγειωθούν πάνω τους"),
  Q("Ποια είναι η στάση των επιστημόνων;", ["Είναι βέβαιοι ότι οι ρίγες υπάρχουν μόνο για τις μύγες", "Θεωρούν ότι οι ρίγες ίσως εξυπηρετούν πολλούς σκοπούς", "Πιστεύουν ότι το ερώτημα δεν θα απαντηθεί ποτέ", "Επιστρέφουν στην εξήγηση του Δαρβίνου"], 1, "δεν αποκλείεται οι ρίγες να εξυπηρετούν περισσότερους από έναν σκοπούς ταυτόχρονα"),
 ],
 "gloss": {"ζέβρες": "ζέβρα — zebra", "ρίγες": "ρίγα — stripe", "δροσίζεται": "δροσίζομαι — to cool down", "κερδίζει έδαφος": "κερδίζω έδαφος — to gain ground", "ριγέ": "ριγέ — striped", "προσανατολισμό": "προσανατολισμός — orientation, bearings", "αποκλείεται": "αποκλείεται — it is ruled out"},
})

ITEMS.append({
 "id": "l189-rep-efimerides-gia-tyflous", "title": "Οι εφημερίδες διαβάζονται δυνατά", "title_en": "Newspapers read aloud", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για έναν ραδιοφωνικό σταθμό που διαβάζει εφημερίδες για τυφλούς και ηλικιωμένους.",
 "script": [
  L("Ρεπόρτερ", "m", "Κάθε πρωί στις εφτά, σε ένα μικρό στούντιο στη Θεσσαλονίκη, δύο εθελοντές διαβάζουν δυνατά τις εφημερίδες της ημέρας. Η εκπομπή απευθύνεται σε τυφλούς και σε ηλικιωμένους που δεν μπορούν πια να διαβάσουν τα μικρά γράμματα.", "Every morning at seven, in a small studio in Thessaloniki, two volunteers read the day's newspapers aloud. The programme is aimed at blind people and at elderly people who can no longer read small print."),
  L("Ρεπόρτερ", "m", "Οι εθελοντές είναι εξήντα, κυρίως συνταξιούχοι δάσκαλοι και ηθοποιοί, και κάθε ένας διαβάζει μία φορά την εβδομάδα. Δεν διαβάζουν μόνο τα πρωτοσέλιδα: οι ακροατές ζητούν και τις αγγελίες, τα ψιλά της τοπικής ειδησεογραφίας, ακόμα και τις κηδείες, «για να ξέρουν ποιος έφυγε από τη γειτονιά».", "There are sixty volunteers, mostly retired teachers and actors, and each one reads once a week. They don't only read the front pages: listeners also ask for the classified ads, the small local news items, even the funeral notices, \"so they know who has passed away in the neighbourhood.\""),
  L("Ρεπόρτερ", "m", "Η εκπομπή μεταδίδεται και στο διαδίκτυο, και οι ακροατές μπορούν να τηλεφωνήσουν για να ζητήσουν να διαβαστεί ένα συγκεκριμένο άρθρο. Ένας ακροατής ογδόντα πέντε χρονών μάς λέει ότι το πρωινό του δεν είναι πλήρες χωρίς τον καφέ και «τη φωνή που του διαβάζει τα νέα».", "The programme is also broadcast online, and listeners can call to request that a particular article be read. An eighty-five-year-old listener tells us his morning is not complete without his coffee and \"the voice that reads him the news.\""),
 ],
 "questions": [
  Q("Σε ποιους απευθύνεται η εκπομπή;", ["Σε μαθητές", "Σε τυφλούς και ηλικιωμένους που δεν διαβάζουν τα μικρά γράμματα", "Σε ξένους που μαθαίνουν ελληνικά", "Σε οδηγούς ταξί"], 1, "Η εκπομπή απευθύνεται σε τυφλούς και σε ηλικιωμένους"),
  Q("Ποιοι είναι κυρίως οι εθελοντές;", ["Φοιτητές δημοσιογραφίας", "Γιατροί", "Συνταξιούχοι δάσκαλοι και ηθοποιοί", "Υπάλληλοι της εφημερίδας"], 2, "κυρίως συνταξιούχοι δάσκαλοι και ηθοποιοί"),
  Q("Τι μπορούν να κάνουν οι ακροατές;", ["Να τηλεφωνήσουν για να ζητήσουν ένα συγκεκριμένο άρθρο", "Να διαβάσουν οι ίδιοι στο ραδιόφωνο", "Να γραφτούν συνδρομητές στην εφημερίδα", "Να επισκεφτούν το στούντιο κάθε μέρα"], 0, "οι ακροατές μπορούν να τηλεφωνήσουν για να ζητήσουν να διαβαστεί ένα συγκεκριμένο άρθρο"),
 ],
 "gloss": {"απευθύνεται": "απευθύνομαι — to be aimed at", "πρωτοσέλιδα": "πρωτοσέλιδο — front page", "αγγελίες": "αγγελία — classified ad", "ψιλά": "τα ψιλά — small news items", "ειδησεογραφίας": "ειδησεογραφία — news coverage", "μεταδίδεται": "μεταδίδομαι — to be broadcast"},
})

rnd = random.Random(189)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-189.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
