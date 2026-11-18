# Source for library/listening/listening-193.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l193.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l193-vm-sideras-kagkela", "title": "Μήνυμα από τον σιδερά για τα κάγκελα", "title_en": "A message from the blacksmith about the railings", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε παραγγείλει καινούργια κάγκελα για το μπαλκόνι σας. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Σιδεράς", "m", "Καλησπέρα σας, ο Σταύρος είμαι, ο σιδεράς. Σας παίρνω για τα κάγκελα του μπαλκονιού. Τα έχω σχεδόν τελειώσει, αλλά υπάρχει ένα πρόβλημα. Όταν ήρθα να πάρω μέτρα, μου είπατε ότι το μπαλκόνι έχει τέσσερα μέτρα μήκος. Ξαναείδα τις σημειώσεις μου και νομίζω ότι μέτρησα μόνο την μπροστινή πλευρά, όχι τα πλαϊνά.", "Good evening, it's Stavros, the blacksmith. I'm calling about the balcony railings. I've almost finished them, but there's a problem. When I came to take measurements, you told me the balcony is four metres long. I looked at my notes again and I think I only measured the front side, not the sides."),
  L("Σιδεράς", "m", "Θα ήθελα να περάσω αύριο το πρωί, γύρω στις εννιά, να ξαναμετρήσω, για να μη γίνει κανένα λάθος. Αν χρειαστούν και τα πλαϊνά, η τιμή θα ανέβει περίπου εκατόν πενήντα ευρώ, και η τοποθέτηση θα γίνει την επόμενη Τρίτη αντί για την Παρασκευή.", "I'd like to come by tomorrow morning, around nine, to measure again, so that there's no mistake. If the sides are needed too, the price will go up by about a hundred and fifty euros, and the fitting will be next Tuesday instead of Friday."),
  L("Σιδεράς", "m", "Μου είχατε ρωτήσει και για το χρώμα. Το σκούρο πράσινο που διαλέξατε το έχω, αλλά σας προτείνω να το δείτε πρώτα πάνω σε ένα κομμάτι σίδερο, γιατί στον ήλιο φαίνεται πιο ανοιχτό. Πείτε μου αν σας βολεύει η ώρα.", "You'd also asked me about the colour. I have the dark green you chose, but I suggest you see it first on a piece of iron, because in the sun it looks lighter. Let me know if the time suits you."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με τα κάγκελα;", ["Χάλασε η μηχανή του σιδερά", "Ίσως μέτρησε μόνο την μπροστινή πλευρά του μπαλκονιού", "Δεν βρίσκει το σωστό χρώμα", "Ακρίβυνε το σίδερο"], 1, "νομίζω ότι μέτρησα μόνο την μπροστινή πλευρά, όχι τα πλαϊνά"),
  Q("Τι θα γίνει αν χρειαστούν και τα πλαϊνά;", ["Η τοποθέτηση θα γίνει νωρίτερα", "Η τιμή θα ανέβει και η τοποθέτηση θα καθυστερήσει", "Θα αλλάξει το χρώμα", "Δεν θα αλλάξει τίποτα"], 1, "η τιμή θα ανέβει περίπου εκατόν πενήντα ευρώ, και η τοποθέτηση θα γίνει την επόμενη Τρίτη"),
  Q("Γιατί προτείνει να δείτε το χρώμα πάνω σε σίδερο;", ["Γιατί στον ήλιο φαίνεται πιο ανοιχτό", "Γιατί δεν το έχει", "Γιατί είναι πολύ ακριβό", "Γιατί ξεθωριάζει γρήγορα"], 0, "στον ήλιο φαίνεται πιο ανοιχτό"),
 ],
 "gloss": {"σιδεράς": "σιδεράς — blacksmith", "κάγκελα": "κάγκελο — railing", "πλαϊνά": "πλαϊνά — sides", "ξαναμετρήσω": "ξαναμετρώ — to measure again", "τοποθέτηση": "τοποθέτηση — fitting, installation"},
})

ITEMS.append({
 "id": "l193-mono-zo-se-varka", "title": "Ζω σε μια βάρκα στο λιμάνι", "title_en": "I live on a boat in the harbour", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άνδρα να μιλάει σε ένα podcast για το πώς ζει σε ένα ιστιοφόρο.",
 "script": [
  L("Νίκος", "m", "Πριν από τρία χρόνια το ενοίκιο του διαμερίσματός μου στον Πειραιά ανέβηκε τόσο, που έπρεπε να πάρω μια απόφαση. Είχα ένα παλιό ιστιοφόρο δέκα μέτρων, που το χρησιμοποιούσα μόνο τα καλοκαίρια. Έτσι μετακόμισα σε αυτό. Πληρώνω στη μαρίνα το ένα τρίτο από όσα πλήρωνα για το διαμέρισμα.", "Three years ago the rent on my flat in Piraeus went up so much that I had to make a decision. I had an old ten-metre sailing boat that I only used in summer. So I moved onto it. I pay the marina a third of what I paid for the flat."),
  L("Νίκος", "m", "Το πιο δύσκολο ήταν να αποχωριστώ τα πράγματά μου. Στη βάρκα χωράνε μόνο τα απαραίτητα: λίγα ρούχα, δέκα βιβλία, μια κατσαρόλα και ένα τηγάνι. Το νερό το παίρνω από τη βρύση της μαρίνας και το ρεύμα από δύο μικρά φωτοβολταϊκά. Τον χειμώνα, όταν φυσάει, το σκάφος κουνιέται τόσο, που στην αρχή δεν μπορούσα να κοιμηθώ.", "The hardest part was parting with my things. Only the essentials fit on the boat: a few clothes, ten books, a pot and a frying pan. I get water from the marina tap and electricity from two small solar panels. In winter, when the wind blows, the boat rocks so much that at first I couldn't sleep."),
  L("Νίκος", "m", "Τώρα δεν θα το άλλαζα με τίποτα. Οι γείτονές μου είναι ένας ψαράς, ένα ζευγάρι Γάλλων συνταξιούχων και μια νεαρή γιατρός. Τρώμε συχνά μαζί στην προβλήτα. Και όταν βαρεθώ τη θέα, λύνω τα σχοινιά και πάω σε άλλο λιμάνι. Ποιο διαμέρισμα σού το επιτρέπει αυτό;", "Now I wouldn't change it for anything. My neighbours are a fisherman, a French retired couple and a young doctor. We often eat together on the jetty. And when I get bored of the view, I untie the ropes and go to another harbour. Which flat lets you do that?"),
 ],
 "questions": [
  Q("Γιατί μετακόμισε στη βάρκα;", ["Γιατί πούλησε το διαμέρισμα", "Γιατί ανέβηκε πολύ το ενοίκιο", "Γιατί ήθελε να γίνει ψαράς", "Γιατί έχασε τη δουλειά του"], 1, "το ενοίκιο του διαμερίσματός μου στον Πειραιά ανέβηκε τόσο"),
  Q("Από πού παίρνει ρεύμα;", ["Από τη μαρίνα", "Από μια γεννήτρια", "Από δύο μικρά φωτοβολταϊκά", "Από τον γείτονά του"], 2, "το ρεύμα από δύο μικρά φωτοβολταϊκά"),
  Q("Τι του άρεσε λιγότερο στην αρχή;", ["Οι γείτονες", "Ότι το σκάφος κουνιόταν και δεν μπορούσε να κοιμηθεί", "Το φαγητό", "Η θέα"], 1, "το σκάφος κουνιέται τόσο, που στην αρχή δεν μπορούσα να κοιμηθώ"),
 ],
 "gloss": {"ιστιοφόρο": "ιστιοφόρο — sailing boat", "μαρίνα": "μαρίνα — marina", "αποχωριστώ": "αποχωρίζομαι — to part with", "απαραίτητα": "απαραίτητος — essential", "προβλήτα": "προβλήτα — jetty, pier", "σχοινιά": "σχοινί — rope"},
})

ITEMS.append({
 "id": "l193-news-alepou-pantoufles", "title": "Μια αλεπού έκλεβε παπούτσια σε ένα χωριό", "title_en": "A fox was stealing shoes in a village", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο τέλος ενός δελτίου ειδήσεων.",
 "script": [
  L("Εκφωνήτρια", "f", "Λύθηκε το μυστήριο που απασχολούσε εδώ και δύο μήνες τους κατοίκους ενός χωριού της Αρκαδίας. Από τις αυλές και τα μπαλκόνια εξαφανίζονταν κάθε νύχτα παπούτσια, παντόφλες και γαλότσες, πάντα ένα από κάθε ζευγάρι.", "The mystery that had been puzzling the residents of a village in Arcadia for two months has been solved. Every night shoes, slippers and wellington boots were disappearing from yards and balconies, always one from each pair."),
  L("Εκφωνήτρια", "f", "Στην αρχή οι κάτοικοι υποψιάστηκαν τα παιδιά του χωριού, που όμως ορκίζονταν ότι δεν είχαν καμία σχέση. Το μυστήριο λύθηκε όταν ένας κάτοικος έβαλε μια κάμερα στην αυλή του και κατέγραψε μια αλεπού να αρπάζει ένα παπούτσι και να εξαφανίζεται στο δάσος.", "At first the residents suspected the village children, who however swore they had nothing to do with it. The mystery was solved when a resident put a camera in his yard and recorded a fox grabbing a shoe and vanishing into the forest."),
  L("Εκφωνήτρια", "f", "Λίγο αργότερα, ένας κυνηγός βρήκε κοντά σε μια φωλιά πάνω από εκατό παπούτσια. Σύμφωνα με έναν βιολόγο, οι νεαρές αλεπούδες παίζουν συχνά με αντικείμενα που μυρίζουν άνθρωπο. Οι κάτοικοι μάζεψαν τα παπούτσια στην πλατεία, για να βρει ο καθένας τα δικά του.", "A little later, a hunter found over a hundred shoes near a den. According to a biologist, young foxes often play with objects that smell of people. The residents gathered the shoes in the square, so that everyone could find their own."),
 ],
 "questions": [
  Q("Τι εξαφανιζόταν από τις αυλές;", ["Ζευγάρια παπούτσια ολόκληρα", "Ένα παπούτσι από κάθε ζευγάρι", "Παιχνίδια παιδιών", "Ρούχα από τις απλώστρες"], 1, "πάντα ένα από κάθε ζευγάρι"),
  Q("Πώς λύθηκε το μυστήριο;", ["Ομολόγησαν τα παιδιά", "Μια κάμερα κατέγραψε την αλεπού", "Η αστυνομία έκανε έρευνα", "Ένας κυνηγός είδε την αλεπού στην πλατεία"], 1, "έβαλε μια κάμερα στην αυλή του και κατέγραψε μια αλεπού"),
  Q("Τι εξήγηση δίνει ο βιολόγος;", ["Οι αλεπούδες τρώνε το δέρμα", "Οι νεαρές αλεπούδες παίζουν με αντικείμενα που μυρίζουν άνθρωπο", "Οι αλεπούδες φτιάχνουν φωλιές από παπούτσια", "Οι αλεπούδες πεινούσαν"], 1, "οι νεαρές αλεπούδες παίζουν συχνά με αντικείμενα που μυρίζουν άνθρωπο"),
 ],
 "gloss": {"αλεπού": "αλεπού — fox", "παντόφλες": "παντόφλα — slipper", "γαλότσες": "γαλότσα — wellington boot", "υποψιάστηκαν": "υποψιάζομαι — to suspect", "ορκίζονταν": "ορκίζομαι — to swear", "αρπάζει": "αρπάζω — to grab", "φωλιά": "φωλιά — den, nest"},
})

ITEMS.append({
 "id": "l193-rep-synavlia-se-spilaio", "title": "Συναυλία μέσα σε ένα σπήλαιο", "title_en": "A concert inside a cave", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για μια ασυνήθιστη μουσική εκδήλωση στην Πελοπόννησο.",
 "script": [
  L("Ρεπόρτερ", "m", "Διακόσιοι θεατές κατεβαίνουν προσεκτικά ένα στενό μεταλλικό σκαλοπάτι, εκατό μέτρα κάτω από την επιφάνεια της γης. Στο βάθος, ανάμεσα σε σταλακτίτες και σταλαγμίτες, τους περιμένει ένα κουαρτέτο εγχόρδων. Είναι η πρώτη συναυλία που γίνεται ποτέ σε αυτό το σπήλαιο.", "Two hundred spectators carefully go down a narrow metal staircase, a hundred metres below the surface of the earth. At the bottom, among stalactites and stalagmites, a string quartet is waiting for them. It is the first concert ever held in this cave."),
  L("Ρεπόρτερ", "m", "Η ακουστική, λένε οι μουσικοί, είναι μοναδική. Ο ήχος δεν χάνεται, αλλά ταξιδεύει ανάμεσα στους βράχους και επιστρέφει λίγο αργότερα, σαν να παίζει μια δεύτερη ορχήστρα. Το πρόβλημα είναι η υγρασία, που φτάνει σχεδόν το εκατό τοις εκατό: τα βιολιά ξεκουρδίζονται συνεχώς, και οι μουσικοί τα κουρδίζουν ανάμεσα στα κομμάτια.", "The acoustics, the musicians say, are unique. The sound doesn't get lost, but travels among the rocks and comes back a little later, as if a second orchestra were playing. The problem is the humidity, which reaches almost one hundred per cent: the violins keep going out of tune, and the musicians tune them between pieces."),
  L("Ρεπόρτερ", "m", "Οι γεωλόγοι που φροντίζουν το σπήλαιο έθεσαν αυστηρούς όρους. Δεν επιτρέπονται φλας ούτε δυνατά φώτα, γιατί ευνοούν την ανάπτυξη φυκιών στους βράχους, και ο αριθμός των θεατών είναι περιορισμένος, για να μην ανέβει η θερμοκρασία. Γι' αυτό οι συναυλίες θα γίνονται μόνο τέσσερις φορές τον χρόνο, και τα εισιτήρια εξαντλήθηκαν σε μία ώρα.", "The geologists who look after the cave set strict conditions. No flash or bright lights are allowed, because they encourage the growth of algae on the rocks, and the number of spectators is limited so that the temperature doesn't rise. That's why the concerts will be held only four times a year, and the tickets sold out in an hour."),
 ],
 "questions": [
  Q("Τι λένε οι μουσικοί για την ακουστική;", ["Ότι ο ήχος χάνεται γρήγορα", "Ότι ο ήχος επιστρέφει σαν να παίζει δεύτερη ορχήστρα", "Ότι χρειάζονται μικρόφωνα", "Ότι είναι χειρότερη από μια αίθουσα"], 1, "επιστρέφει λίγο αργότερα, σαν να παίζει μια δεύτερη ορχήστρα"),
  Q("Ποιο πρόβλημα προκαλεί η υγρασία;", ["Τα βιολιά ξεκουρδίζονται συνεχώς", "Γλιστράνε τα σκαλοπάτια", "Κρυώνουν οι θεατές", "Σβήνουν τα φώτα"], 0, "τα βιολιά ξεκουρδίζονται συνεχώς"),
  Q("Γιατί ο αριθμός των θεατών είναι περιορισμένος;", ["Για να μην ανέβει η θερμοκρασία", "Γιατί η σκάλα είναι επικίνδυνη", "Γιατί οι μουσικοί το ζήτησαν", "Για να είναι ακριβά τα εισιτήρια"], 0, "ο αριθμός των θεατών είναι περιορισμένος, για να μην ανέβει η θερμοκρασία"),
 ],
 "gloss": {"σπήλαιο": "σπήλαιο — cave", "σταλακτίτες": "σταλακτίτης — stalactite", "εγχόρδων": "έγχορδα — string instruments", "ακουστική": "ακουστική — acoustics", "ξεκουρδίζονται": "ξεκουρδίζομαι — to go out of tune", "φυκιών": "φύκι — alga, seaweed", "εξαντλήθηκαν": "εξαντλούμαι — to sell out, run out"},
})

ITEMS.append({
 "id": "l193-rep-panepistimio-tritis-ilikias", "title": "Φοιτητές στα εβδομήντα", "title_en": "Students in their seventies", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα πρόγραμμα μαθημάτων για συνταξιούχους σε ένα πανεπιστήμιο.",
 "script": [
  L("Ρεπόρτερ", "f", "Η αίθουσα είναι γεμάτη, και κανείς δεν κοιτάζει το κινητό του. Ο μέσος όρος ηλικίας των φοιτητών είναι εξήντα οχτώ χρόνια. Πρόκειται για ένα πρόγραμμα του πανεπιστημίου για άτομα τρίτης ηλικίας, που προσφέρει μαθήματα ιστορίας, αστρονομίας, λογοτεχνίας και υπολογιστών.", "The lecture hall is full, and nobody is looking at their phone. The average age of the students is sixty-eight. This is a university programme for people of the third age, offering courses in history, astronomy, literature and computers."),
  L("Ρεπόρτερ", "f", "Δεν υπάρχουν εξετάσεις ούτε βαθμοί, αλλά οι φοιτητές παίρνουν τα μαθήματα πολύ σοβαρά. Ο κύριος Ηλίας, συνταξιούχος ναυτικός εβδομήντα τεσσάρων χρονών, δεν έχει χάσει ούτε ένα μάθημα αστρονομίας. Όπως λέει, για σαράντα χρόνια κοίταζε τα αστέρια από τη γέφυρα του πλοίου χωρίς να ξέρει τα ονόματά τους.", "There are no exams or grades, but the students take the courses very seriously. Mr Ilias, a seventy-four-year-old retired sailor, hasn't missed a single astronomy class. As he says, for forty years he looked at the stars from the ship's bridge without knowing their names."),
  L("Ρεπόρτερ", "f", "Οι καθηγητές λένε ότι η διδασκαλία εδώ είναι διαφορετική. Οι φοιτητές κάνουν δύσκολες ερωτήσεις και συχνά διορθώνουν τον διδάσκοντα με τις δικές τους αναμνήσεις, ιδίως στο μάθημα της σύγχρονης ιστορίας. Φέτος οι αιτήσεις ήταν τριπλάσιες από τις θέσεις, και το πανεπιστήμιο σκέφτεται να ανοίξει ένα δεύτερο τμήμα.", "The professors say that teaching here is different. The students ask difficult questions and often correct the lecturer with their own memories, especially in the modern history course. This year the applications were three times the number of places, and the university is thinking of opening a second class."),
 ],
 "questions": [
  Q("Τι ισχύει για το πρόγραμμα;", ["Έχει δύσκολες εξετάσεις", "Δεν έχει εξετάσεις ούτε βαθμούς", "Είναι μόνο για πρώην καθηγητές", "Γίνεται μόνο διαδικτυακά"], 1, "Δεν υπάρχουν εξετάσεις ούτε βαθμοί"),
  Q("Γιατί ο κύριος Ηλίας παρακολουθεί αστρονομία;", ["Γιατί ήταν αστρονόμος", "Γιατί κοίταζε τα αστέρια για χρόνια χωρίς να ξέρει τα ονόματά τους", "Γιατί του το πρότεινε ο γιατρός", "Γιατί θέλει να αγοράσει τηλεσκόπιο"], 1, "κοίταζε τα αστέρια από τη γέφυρα του πλοίου χωρίς να ξέρει τα ονόματά τους"),
  Q("Τι κάνουν συχνά οι φοιτητές στο μάθημα της σύγχρονης ιστορίας;", ["Κοιμούνται", "Διορθώνουν τον διδάσκοντα με τις αναμνήσεις τους", "Φεύγουν νωρίς", "Γράφουν εργασίες"], 1, "συχνά διορθώνουν τον διδάσκοντα με τις δικές τους αναμνήσεις"),
 ],
 "gloss": {"ηλικίας": "τρίτη ηλικία — old age, the third age", "μέσος": "μέσος όρος — average", "ναυτικός": "ναυτικός — sailor", "γέφυρα": "γέφυρα (πλοίου) — (ship's) bridge", "διδάσκοντα": "διδάσκων — lecturer", "τριπλάσιες": "τριπλάσιος — three times as many"},
})

ITEMS.append({
 "id": "l193-c1-int-psychologia-routinas", "title": "Ψυχολόγος για τη δύναμη της ρουτίνας", "title_en": "A psychologist on the power of routine", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια ραδιοφωνική συνέντευξη με μια ψυχολόγο για τον ρόλο των συνηθειών στη ζωή μας.",
 "script": [
  L("Δημοσιογράφος", "m", "Η ρουτίνα έχει κακή φήμη. Τη συνδέουμε με την πλήξη. Εσείς υποστηρίζετε το αντίθετο.", "Routine has a bad reputation. We associate it with boredom. You argue the opposite."),
  L("Ψυχολόγος", "f", "Υποστηρίζω ότι μια καλή ρουτίνα μάς ελευθερώνει. Κάθε μέρα παίρνουμε εκατοντάδες μικρές αποφάσεις, και κάθε απόφαση κοστίζει λίγη νοητική ενέργεια. Όταν κάτι γίνεται αυτόματα, όπως το πρωινό βούρτσισμα των δοντιών, ο εγκέφαλος δεν σπαταλά ενέργεια γι' αυτό και την κρατά για ό,τι πραγματικά χρειάζεται σκέψη.", "I argue that a good routine frees us. Every day we make hundreds of small decisions, and each decision costs a little mental energy. When something happens automatically, like brushing our teeth in the morning, the brain doesn't waste energy on it and keeps it for what really needs thought."),
  L("Δημοσιογράφος", "m", "Πόσος χρόνος χρειάζεται για να γίνει μια πράξη συνήθεια; Ακούμε συχνά για είκοσι μία μέρες.", "How long does it take for an action to become a habit? We often hear twenty-one days."),
  L("Ψυχολόγος", "f", "Αυτός ο αριθμός είναι μάλλον μύθος. Μια γνωστή βρετανική μελέτη βρήκε ότι κατά μέσο όρο χρειάστηκαν περίπου δύο μήνες, αλλά με τεράστιες διαφορές: για κάποιους λίγες εβδομάδες, για άλλους σχεδόν έναν χρόνο. Κι αυτό που μετρά δεν είναι να μη χάσεις ποτέ μέρα· μια χαμένη μέρα δεν φάνηκε να καταστρέφει την προσπάθεια.", "That number is probably a myth. A well-known British study found that on average it took about two months, but with huge differences: for some a few weeks, for others almost a year. And what matters isn't never missing a day; one missed day didn't seem to ruin the effort."),
  L("Δημοσιογράφος", "m", "Μπορεί όμως η ρουτίνα να γίνει φυλακή;", "But can routine become a prison?"),
  L("Ψυχολόγος", "f", "Βεβαίως, όταν γίνεται άκαμπτη. Αν ο άνθρωπος αγχώνεται μόλις αλλάξει η παραμικρή λεπτομέρεια του προγράμματός του, τότε η ρουτίνα δεν τον στηρίζει πια, τον ελέγχει. Μια υγιής ρουτίνα μοιάζει περισσότερο με σκαλωσιά παρά με τοίχο: σε κρατά όρθιο στις δύσκολες περιόδους, για παράδειγμα μετά από ένα πένθος, αλλά μπορείς να τη μετακινήσεις.", "Of course, when it becomes rigid. If a person gets anxious as soon as the slightest detail of their schedule changes, then the routine no longer supports them, it controls them. A healthy routine is more like scaffolding than a wall: it keeps you standing in difficult periods, for example after a bereavement, but you can move it."),
 ],
 "questions": [
  Q("Γιατί, κατά την ψυχολόγο, μας ελευθερώνει μια καλή ρουτίνα;", ["Γιατί μας κάνει πιο κοινωνικούς", "Γιατί εξοικονομεί νοητική ενέργεια για ό,τι χρειάζεται σκέψη", "Γιατί μας κάνει να κοιμόμαστε περισσότερο", "Γιατί μειώνει τις ώρες εργασίας"], 1, "ο εγκέφαλος δεν σπαταλά ενέργεια γι' αυτό και την κρατά για ό,τι πραγματικά χρειάζεται σκέψη"),
  Q("Τι λέει για τις «είκοσι μία μέρες»;", ["Ότι είναι επιστημονικά αποδεδειγμένες", "Ότι μάλλον είναι μύθος", "Ότι ισχύουν μόνο για παιδιά", "Ότι είναι υπερβολικά λίγες για όλους"], 1, "Αυτός ο αριθμός είναι μάλλον μύθος"),
  Q("Τι βρήκε η μελέτη για τη χαμένη μέρα;", ["Ότι ξεκινά την προσπάθεια από την αρχή", "Ότι δεν φάνηκε να καταστρέφει την προσπάθεια", "Ότι διπλασιάζει τον χρόνο", "Ότι δεν μελετήθηκε"], 1, "μια χαμένη μέρα δεν φάνηκε να καταστρέφει την προσπάθεια"),
  Q("Με τι μοιάζει, κατά την ψυχολόγο, μια υγιής ρουτίνα;", ["Με τοίχο", "Με φυλακή", "Με σκαλωσιά", "Με ρολόι"], 2, "Μια υγιής ρουτίνα μοιάζει περισσότερο με σκαλωσιά παρά με τοίχο"),
 ],
 "gloss": {"ρουτίνα": "ρουτίνα — routine", "πλήξη": "πλήξη — boredom", "νοητική": "νοητικός — mental", "σπαταλά": "σπαταλώ — to waste", "άκαμπτη": "άκαμπτος — rigid", "σκαλωσιά": "σκαλωσιά — scaffolding", "πένθος": "πένθος — bereavement, mourning"},
})

ITEMS.append({
 "id": "l193-c1-mono-oures-aeroplanon", "title": "Οι άσπρες γραμμές των αεροπλάνων", "title_en": "The white trails of aeroplanes", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια εκπομπή επιστήμης για τις λευκές γραμμές που αφήνουν τα αεροπλάνα στον ουρανό.",
 "script": [
  L("Παρουσιάστρια", "f", "Τις λέμε συχνά «καπνό», αλλά οι λευκές γραμμές πίσω από τα αεροπλάνα δεν είναι καπνός. Είναι σύννεφα, μικρά τεχνητά σύννεφα από κρυστάλλους πάγου. Οι κινητήρες βγάζουν, μαζί με τα καυσαέρια, μεγάλη ποσότητα θερμών υδρατμών. Στο ύψος όπου πετούν τα επιβατικά αεροσκάφη, η θερμοκρασία είναι συχνά κάτω από μείον σαράντα βαθμούς.", "We often call them 'smoke', but the white lines behind aeroplanes are not smoke. They are clouds, small artificial clouds of ice crystals. Along with the exhaust gases, the engines release a large amount of hot water vapour. At the height where passenger aircraft fly, the temperature is often below minus forty degrees."),
  L("Παρουσιάστρια", "f", "Οι υδρατμοί ψύχονται απότομα, συμπυκνώνονται γύρω από μικροσκοπικά σωματίδια αιθάλης και παγώνουν σχεδόν αμέσως. Γιατί όμως κάποιες γραμμές σβήνουν σε λίγα δευτερόλεπτα, ενώ άλλες μένουν για ώρες και απλώνονται; Η απάντηση βρίσκεται στην υγρασία του αέρα σε εκείνο το ύψος. Αν ο αέρας είναι ξηρός, οι κρύσταλλοι εξατμίζονται γρήγορα. Αν είναι σχεδόν κορεσμένος, οι κρύσταλλοι μεγαλώνουν και η γραμμή μπορεί να μετατραπεί σε ένα λεπτό, πλατύ σύννεφο.", "The water vapour cools abruptly, condenses around tiny soot particles and freezes almost immediately. But why do some trails vanish in a few seconds while others stay for hours and spread out? The answer lies in the humidity of the air at that height. If the air is dry, the crystals evaporate quickly. If it is nearly saturated, the crystals grow and the trail can turn into a thin, wide cloud."),
  L("Παρουσιάστρια", "f", "Αυτά τα επίμονα σύννεφα έχουν απασχολήσει τους κλιματολόγους. Τη νύχτα εμποδίζουν τη θερμότητα της Γης να διαφύγει, και ορισμένες μελέτες εκτιμούν ότι η συνολική τους επίδραση στη θέρμανση του πλανήτη μπορεί να είναι συγκρίσιμη με εκείνη του διοξειδίου του άνθρακα από τις πτήσεις, αν και οι εκτιμήσεις έχουν μεγάλη αβεβαιότητα. Γι' αυτό εξετάζεται μια απλή ιδέα: να αλλάζουν ελαφρά το ύψος τους οι πτήσεις, ώστε να αποφεύγουν τα πολύ υγρά στρώματα του αέρα.", "These persistent clouds have occupied climate scientists. At night they prevent the Earth's heat from escaping, and some studies estimate that their total effect on global warming may be comparable to that of the carbon dioxide from flights, although the estimates are very uncertain. That's why a simple idea is being examined: flights could slightly change their altitude so as to avoid very humid layers of air."),
 ],
 "questions": [
  Q("Από τι αποτελούνται οι λευκές γραμμές;", ["Από καπνό", "Από κρυστάλλους πάγου", "Από καύσιμο που δεν κάηκε", "Από σκόνη"], 1, "μικρά τεχνητά σύννεφα από κρυστάλλους πάγου"),
  Q("Από τι εξαρτάται πόσο διαρκεί μια γραμμή;", ["Από το μέγεθος του αεροπλάνου", "Από την ταχύτητα της πτήσης", "Από την υγρασία του αέρα σε εκείνο το ύψος", "Από την ώρα της ημέρας"], 2, "Η απάντηση βρίσκεται στην υγρασία του αέρα σε εκείνο το ύψος"),
  Q("Τι κάνουν τα επίμονα σύννεφα τη νύχτα;", ["Δροσίζουν τον πλανήτη", "Εμποδίζουν τη θερμότητα της Γης να διαφύγει", "Φέρνουν βροχή", "Εξαφανίζονται"], 1, "Τη νύχτα εμποδίζουν τη θερμότητα της Γης να διαφύγει"),
  Q("Πώς παρουσιάζει η παρουσιάστρια τις εκτιμήσεις για την επίδρασή τους στο κλίμα;", ["Ως βέβαιες", "Ως ασήμαντες", "Ως αβέβαιες", "Ως ξεπερασμένες"], 2, "αν και οι εκτιμήσεις έχουν μεγάλη αβεβαιότητα"),
 ],
 "gloss": {"κινητήρες": "κινητήρας — engine", "καυσαέρια": "καυσαέρια — exhaust gases", "υδρατμών": "υδρατμοί — water vapour", "αιθάλης": "αιθάλη — soot", "κορεσμένος": "κορεσμένος — saturated", "επίμονα": "επίμονος — persistent", "διαφύγει": "διαφεύγω — to escape"},
})

ITEMS.append({
 "id": "l193-vm-ydrorroes", "title": "Μήνυμα για τις υδρορροές πριν από τις βροχές", "title_en": "A message about the gutters before the rains", "type": "voicemail", "level": "B2",
 "context_el": "Είστε διαχειριστής σε μια πολυκατοικία. Ακούτε ένα μήνυμα από έναν τεχνικό στον τηλεφωνητή σας.",
 "script": [
  L("Τεχνικός", "m", "Καλημέρα σας, ο Μανώλης είμαι, ο τεχνικός που ήρθε την Πέμπτη στην ταράτσα της πολυκατοικίας. Σας τηλεφωνώ για τις υδρορροές. Όπως φοβόμουν, η μεγάλη, αυτή που κατεβαίνει στην πίσω πλευρά, είναι σχεδόν εντελώς βουλωμένη από φύλλα και λάσπη. Γι' αυτό το νερό έτρεχε πέρσι στον τοίχο και μπήκε υγρασία στο διαμέρισμα του πρώτου ορόφου.", "Good morning, it's Manolis, the technician who came up to the building's roof terrace on Thursday. I'm calling about the gutters. As I feared, the big one, the one that runs down the back of the building, is almost completely blocked with leaves and mud. That's why last year the water ran down the wall and damp got into the first-floor flat."),
  L("Τεχνικός", "m", "Η μετεωρολογική υπηρεσία δίνει δυνατές βροχές από την άλλη Τρίτη, οπότε θα ήταν καλό να το καθαρίσουμε πριν. Μπορώ να έρθω τη Δευτέρα το πρωί. Θα χρειαστώ όμως να μπω στον ακάλυπτο χώρο από το διαμέρισμα του ισογείου, γιατί η σκάλα μου δεν περνάει από την είσοδο.", "The weather service is forecasting heavy rain from next Tuesday, so it would be good to clear it before then. I can come on Monday morning. But I'll need to get into the back courtyard through the ground-floor flat, because my ladder won't go through the entrance."),
  L("Τεχνικός", "m", "Το κόστος είναι εκατόν είκοσι ευρώ για όλη την πολυκατοικία. Αν θέλετε, μπορώ να βάλω και ένα πλέγμα στην κορυφή της υδρορροής, για να μη βουλώσει ξανά από τα φύλλα της μουριάς. Αυτό κοστίζει άλλα τριάντα. Ενημερώστε με αν συμφωνούν οι ένοικοι και αν ο κύριος του ισογείου θα είναι σπίτι.", "The cost is a hundred and twenty euros for the whole building. If you like, I can also put a mesh at the top of the gutter, so that it doesn't get blocked again by the leaves of the mulberry tree. That costs another thirty. Let me know if the residents agree and if the gentleman on the ground floor will be at home."),
 ],
 "questions": [
  Q("Τι πρόβλημα βρήκε ο τεχνικός;", ["Η ταράτσα έχει ρωγμές", "Η μεγάλη υδρορροή είναι σχεδόν βουλωμένη", "Χάλασε ο θερμοσίφωνας", "Λείπουν κεραμίδια"], 1, "είναι σχεδόν εντελώς βουλωμένη από φύλλα και λάσπη"),
  Q("Γιατί χρειάζεται να μπει από το διαμέρισμα του ισογείου;", ["Γιατί εκεί είναι η υδρορροή", "Γιατί η σκάλα του δεν περνάει από την είσοδο", "Γιατί η είσοδος είναι κλειδωμένη", "Γιατί εκεί μένει ο διαχειριστής"], 1, "η σκάλα μου δεν περνάει από την είσοδο"),
  Q("Σε τι χρησιμεύει το πλέγμα που προτείνει;", ["Να μην μπαίνουν πουλιά", "Να μη βουλώσει ξανά η υδρορροή από τα φύλλα", "Να τρέχει πιο γρήγορα το νερό", "Να μη σκουριάσει η υδρορροή"], 1, "για να μη βουλώσει ξανά από τα φύλλα της μουριάς"),
 ],
 "gloss": {"υδρορροές": "υδρορροή — gutter, downpipe", "βουλωμένη": "βουλωμένος — blocked", "λάσπη": "λάσπη — mud", "ακάλυπτο": "ακάλυπτος (χώρος) — back courtyard of a block", "πλέγμα": "πλέγμα — mesh", "μουριάς": "μουριά — mulberry tree", "ένοικοι": "ένοικος — resident, tenant"},
})

ITEMS.append({
 "id": "l193-int-sygkollitria-naupigeiou", "title": "Η συγκολλήτρια του ναυπηγείου", "title_en": "The shipyard welder", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γυναίκα που δουλεύει ως συγκολλήτρια σε ένα ναυπηγείο.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσες γυναίκες συγκολλήτριες υπάρχουν στο ναυπηγείο;", "How many women welders are there at the shipyard?"),
  L("Συγκολλήτρια", "f", "Όταν ξεκίνησα, πριν από οχτώ χρόνια, ήμουν η μόνη. Τώρα είμαστε τέσσερις. Την πρώτη μέρα ένας παλιός μάστορας με κοίταξε και είπε ότι δεν θα αντέξω ούτε μια εβδομάδα. Πέντε χρόνια αργότερα, όταν βγήκε στη σύνταξη, μου χάρισε την προσωπίδα του.", "When I started, eight years ago, I was the only one. Now there are four of us. On the first day an old foreman looked at me and said I wouldn't last a week. Five years later, when he retired, he gave me his welding mask."),
  L("Δημοσιογράφος", "m", "Τι είναι το πιο δύσκολο στη δουλειά σας;", "What is the hardest thing in your job?"),
  L("Συγκολλήτρια", "f", "Οι στενοί χώροι. Συχνά δουλεύω μέσα στο αμπάρι του πλοίου, ξαπλωμένη ή γονατιστή, με τη στολή, τα γάντια και την προσωπίδα, και το καλοκαίρι η θερμοκρασία εκεί μέσα ξεπερνά τους σαράντα βαθμούς. Πρέπει να πίνεις συνέχεια νερό και να βγαίνεις έξω κάθε μισή ώρα.", "The narrow spaces. I often work inside the ship's hold, lying down or kneeling, in the overalls, gloves and mask, and in summer the temperature in there goes above forty degrees. You have to keep drinking water and go outside every half hour."),
  L("Δημοσιογράφος", "m", "Και τι σας αρέσει περισσότερο;", "And what do you like most?"),
  L("Συγκολλήτρια", "f", "Η στιγμή που ένα πλοίο που επισκευάσαμε φεύγει από το ναυπηγείο. Ξέρω ότι κάπου μέσα στο σίδερο υπάρχουν οι δικές μου ραφές, και ότι κρατούν όρθιο ένα καράβι με εκατοντάδες ανθρώπους. Η μεγαλύτερη μου κόρη θέλει να γίνει μηχανικός πλοίων. Δεν της το πρότεινα εγώ, το αποφάσισε μόνη της.", "The moment a ship we repaired leaves the shipyard. I know that somewhere inside the steel there are my own seams, and that they hold together a ship with hundreds of people. My elder daughter wants to become a marine engineer. I didn't suggest it to her, she decided by herself."),
 ],
 "questions": [
  Q("Τι της χάρισε ο παλιός μάστορας όταν έφυγε στη σύνταξη;", ["Τα γάντια του", "Την προσωπίδα του", "Ένα εργαλείο", "Τη θέση του"], 1, "μου χάρισε την προσωπίδα του"),
  Q("Ποιο είναι το πιο δύσκολο στη δουλειά της;", ["Οι στενοί χώροι μέσα στο πλοίο", "Οι συνάδελφοι", "Το πρωινό ξύπνημα", "Ο θόρυβος"], 0, "Οι στενοί χώροι"),
  Q("Τι της αρέσει περισσότερο;", ["Ο μισθός", "Η στιγμή που ένα πλοίο που επισκεύασαν φεύγει από το ναυπηγείο", "Τα ταξίδια με τα πλοία", "Οι διακοπές το καλοκαίρι"], 1, "Η στιγμή που ένα πλοίο που επισκευάσαμε φεύγει από το ναυπηγείο"),
 ],
 "gloss": {"συγκολλήτρια": "συγκολλητής/συγκολλήτρια — welder", "ναυπηγείο": "ναυπηγείο — shipyard", "προσωπίδα": "προσωπίδα — (welding) mask", "αμπάρι": "αμπάρι — hold (of a ship)", "γονατιστή": "γονατιστός — kneeling", "ραφές": "ραφή — seam"},
})

ITEMS.append({
 "id": "l193-dia-spiti-giagias-se-tourista", "title": "Θα νοικιάσουμε το σπίτι της γιαγιάς σε τουρίστες;", "title_en": "Shall we rent Grandma's house to tourists?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο αδέλφια συζητούν τι θα κάνουν με το σπίτι που κληρονόμησαν από τη γιαγιά τους στο Ναύπλιο.",
 "script": [
  L("Άννα", "f", "Ο μεσίτης λέει ότι αν νοικιάζουμε το σπίτι της γιαγιάς σε τουρίστες, μόνο το καλοκαίρι θα βγάζουμε όσα βγάζει ένας μόνιμος ενοικιαστής σε έναν ολόκληρο χρόνο.", "The estate agent says that if we rent Grandma's house to tourists, in the summer alone we'd make what a long-term tenant pays in a whole year."),
  L("Δημήτρης", "m", "Ναι, αλλά ποιος θα το φροντίζει; Κάθε δύο μέρες φεύγουν οι μεν, έρχονται οι δε. Πρέπει να αλλάζεις σεντόνια, να καθαρίζεις, να δίνεις κλειδιά. Εσύ μένεις στην Αθήνα κι εγώ στη Θεσσαλονίκη.", "Yes, but who will look after it? Every two days one lot leaves and another arrives. You have to change sheets, clean, hand over keys. You live in Athens and I live in Thessaloniki."),
  L("Άννα", "f", "Υπάρχουν εταιρείες που τα κάνουν όλα αυτά, αλλά παίρνουν περίπου το ένα τέταρτο από τα έσοδα. Και πρέπει να βάλουμε κλιματιστικό, καινούργια κρεβάτια και να βάψουμε.", "There are companies that do all that, but they take about a quarter of the income. And we'd have to put in air conditioning, new beds and paint."),
  L("Δημήτρης", "m", "Υπάρχει και κάτι άλλο. Η κυρία Ρούλα, η γειτόνισσα, μου είπε ότι στο στενό έχουν μείνει μόνο τρεις οικογένειες. Τα υπόλοιπα σπίτια είναι όλα για τουρίστες, και τον χειμώνα η γειτονιά είναι νεκρή. Δεν ξέρω αν θέλω να βάλουμε κι εμείς το χέρι μας σε αυτό.", "There's something else too. Mrs Roula, the neighbour, told me that only three families are left in the lane. The other houses are all for tourists, and in winter the neighbourhood is dead. I don't know if I want us to play a part in that too."),
  L("Άννα", "f", "Σε καταλαβαίνω. Τότε ας το δώσουμε σε έναν μόνιμο ενοικιαστή, ίσως σε μια οικογένεια με παιδιά, με λογικό ενοίκιο. Έτσι θα έχει πάλι φωνές το σπίτι, όπως όταν ζούσε η γιαγιά.", "I understand you. Then let's give it to a long-term tenant, maybe a family with children, at a reasonable rent. That way the house will have voices again, as when Grandma was alive."),
 ],
 "questions": [
  Q("Τι λέει ο μεσίτης;", ["Ότι το σπίτι πρέπει να πουληθεί", "Ότι το καλοκαίρι με τουρίστες θα βγάζουν όσο ένας μόνιμος ενοικιαστής σε έναν χρόνο", "Ότι κανείς δεν θέλει να το νοικιάσει", "Ότι χρειάζεται μεγάλη επισκευή"], 1, "μόνο το καλοκαίρι θα βγάζουμε όσα βγάζει ένας μόνιμος ενοικιαστής σε έναν ολόκληρο χρόνο"),
  Q("Ποιο πρακτικό πρόβλημα βλέπει ο Δημήτρης;", ["Ότι κανείς από τους δύο δεν μένει κοντά για να το φροντίζει", "Ότι το σπίτι είναι πολύ μικρό", "Ότι δεν έχει θέα", "Ότι η γιαγιά το απαγόρευσε"], 0, "Εσύ μένεις στην Αθήνα κι εγώ στη Θεσσαλονίκη"),
  Q("Τι αποφασίζουν τελικά;", ["Να το νοικιάζουν σε τουρίστες με μια εταιρεία", "Να το πουλήσουν", "Να το δώσουν σε έναν μόνιμο ενοικιαστή", "Να μείνει η Άννα εκεί"], 2, "ας το δώσουμε σε έναν μόνιμο ενοικιαστή"),
 ],
 "gloss": {"κληρονόμησαν": "κληρονομώ — to inherit", "μεσίτης": "μεσίτης — estate agent", "ενοικιαστής": "ενοικιαστής — tenant", "σεντόνια": "σεντόνι — sheet", "έσοδα": "έσοδα — income", "στενό": "στενό — lane, alley"},
})

rnd = random.Random(193)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-193.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
