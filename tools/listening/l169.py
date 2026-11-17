# Source for library/listening/listening-169.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l169.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l169-ann-poulman", "title": "Ανακοίνωση στο πούλμαν", "title_en": "An announcement on the coach", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε τη συνοδό ενός τουριστικού πούλμαν να μιλάει στους επιβάτες κατά τη διάρκεια μιας εκδρομής.",
 "script": [
  L("Συνοδός", "f", "Καλημέρα σε όλους. Σε δέκα λεπτά θα κάνουμε μια στάση σε σταθμό εξυπηρέτησης αυτοκινητοδρόμου. Η στάση θα διαρκέσει είκοσι λεπτά. Εκεί θα βρείτε τουαλέτες, καφετέρια και ένα μικρό κατάστημα με τοπικά προϊόντα.", "Good morning, everyone. In ten minutes we'll stop at a motorway service station. The stop will last twenty minutes. There you'll find toilets, a café and a small shop with local products."),
  L("Συνοδός", "f", "Παρακαλώ, κοιτάξτε τον αριθμό του πούλμαν μας, που είναι γραμμένος στο μπροστινό τζάμι, γιατί στον σταθμό θα σταθμεύουν και άλλα πούλμαν που μοιάζουν πολύ. Αναχωρούμε στις έντεκα και τέταρτο ακριβώς. Δεν μπορούμε να περιμένουμε όσους αργήσουν, γιατί μας περιμένει το κρουαζιερόπλοιο στο λιμάνι.", "Please note the number of our coach, written on the front windscreen, because other coaches that look very similar will be parked at the station. We leave at a quarter past eleven sharp. We can't wait for anyone who is late, because the cruise ship is waiting for us at the port."),
  L("Συνοδός", "f", "Όταν ξαναμπείτε, μην ξεχάσετε να δέσετε τη ζώνη σας. Σας θυμίζω επίσης ότι μέσα στο πούλμαν επιτρέπεται μόνο νερό. Καφέδες και φαγητό, παρακαλώ, στον σταθμό.", "When you get back on, don't forget to fasten your seat belt. I also remind you that only water is allowed inside the coach. Coffee and food, please, at the station."),
 ],
 "questions": [
  Q("Πόση ώρα θα διαρκέσει η στάση;", ["Δέκα λεπτά", "Είκοσι λεπτά", "Μισή ώρα", "Μία ώρα"], 1, "Η στάση θα διαρκέσει είκοσι λεπτά"),
  Q("Γιατί πρέπει οι επιβάτες να κοιτάξουν τον αριθμό του πούλμαν;", ["Για να βρουν τη θέση τους", "Για να πληρώσουν στο ταμείο", "Γιατί θα υπάρχουν και άλλα πούλμαν που μοιάζουν πολύ", "Γιατί θα αλλάξουν πούλμαν"], 2, "στον σταθμό θα σταθμεύουν και άλλα πούλμαν που μοιάζουν πολύ"),
  Q("Τι επιτρέπεται μέσα στο πούλμαν;", ["Μόνο νερό", "Καφές και σάντουιτς", "Ό,τι αγοράσουν από τον σταθμό", "Τίποτα απολύτως"], 0, "μέσα στο πούλμαν επιτρέπεται μόνο νερό"),
 ],
 "gloss": {"συνοδό": "συνοδός — tour escort", "πούλμαν": "πούλμαν — coach", "σταθμό εξυπηρέτησης": "σταθμός εξυπηρέτησης — service station", "αυτοκινητοδρόμου": "αυτοκινητόδρομος — motorway", "διαρκέσει": "διαρκώ — to last", "τζάμι": "τζάμι — window, windscreen", "σταθμεύουν": "σταθμεύω — to park", "Αναχωρούμε": "αναχωρώ — to depart", "κρουαζιερόπλοιο": "κρουαζιερόπλοιο — cruise ship", "ζώνη": "ζώνη — seat belt"},
})

ITEMS.append({
 "id": "l169-int-choros-meta-ta-exinta", "title": "Χορεύοντας μετά τα εξήντα", "title_en": "Dancing after sixty", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια χορογράφο που ανεβάζει παραστάσεις σύγχρονου χορού με ερασιτέχνες χορευτές άνω των εξήντα.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς ξεκίνησε αυτή η ομάδα;", "How did this group start?"),
  L("Χορογράφος", "f", "Έκανα μαθήματα σε ένα ΚΑΠΗ, απλές ασκήσεις για την ισορροπία. Μια μέρα έβαλα μουσική και τους είπα να κινηθούν ελεύθερα. Μια κυρία ογδόντα χρονών άρχισε να χορεύει με τα μάτια κλειστά, και όλοι σταμάτησαν να την κοιτάζουν. Εκείνη τη στιγμή κατάλαβα ότι είχαμε μια παράσταση.", "I was teaching classes at a seniors' centre, simple balance exercises. One day I put on music and told them to move freely. An eighty-year-old lady began to dance with her eyes closed, and everyone stopped to watch her. At that moment I knew we had a show."),
  L("Δημοσιογράφος", "m", "Είναι δύσκολο να χορογραφείς για σώματα που δεν είναι πια νέα;", "Is it hard to choreograph for bodies that are no longer young?"),
  L("Χορογράφος", "f", "Δεν ζητάω πηδήματα ούτε σπαγκάτα. Κάθε κίνηση ξεκινά από κάτι που μπορεί να κάνει ο καθένας: ένα χέρι που ανοίγει, ένα βήμα πίσω. Η δύναμη της παράστασης είναι η ζωή που κουβαλάνε. Ένας πρώην ναυτικός κάνει μια κίνηση σαν να τραβάει σκοινί, και το κοινό βλέπει μια ολόκληρη ζωή στη θάλασσα.", "I don't ask for jumps or splits. Every movement starts from something anyone can do: a hand opening, a step back. The power of the show is the life they carry. A former sailor makes a movement as if pulling a rope, and the audience sees a whole life at sea."),
  L("Δημοσιογράφος", "m", "Τι λένε οι οικογένειές τους;", "What do their families say?"),
  L("Χορογράφος", "f", "Στην πρεμιέρα, μια εγγονή μού είπε ότι δεν είχε δει ποτέ τη γιαγιά της τόσο περήφανη. Και οι γιατροί κάποιων από αυτούς μού λένε ότι κοιμούνται καλύτερα και πέφτουν λιγότερο.", "At the premiere, a granddaughter told me she had never seen her grandmother so proud. And some of their doctors tell me they sleep better and fall less."),
 ],
 "questions": [
  Q("Τι έκανε τη χορογράφο να σκεφτεί μια παράσταση;", ["Μια πρόταση του δήμου", "Μια κυρία ογδόντα χρονών που χόρεψε με τα μάτια κλειστά", "Ένα βίντεο στο διαδίκτυο", "Ένας διαγωνισμός χορού"], 1, "Μια κυρία ογδόντα χρονών άρχισε να χορεύει με τα μάτια κλειστά"),
  Q("Από πού ξεκινά κάθε κίνηση της χορογραφίας;", ["Από τον κλασικό χορό", "Από πηδήματα και σπαγκάτα", "Από κάτι που μπορεί να κάνει ο καθένας", "Από παραδοσιακούς χορούς"], 2, "Κάθε κίνηση ξεκινά από κάτι που μπορεί να κάνει ο καθένας"),
  Q("Τι λένε οι γιατροί κάποιων χορευτών;", ["Ότι κοιμούνται καλύτερα και πέφτουν λιγότερο", "Ότι πρέπει να προσέχουν τα γόνατα", "Ότι πρέπει να χορεύουν λιγότερο", "Ότι έχουν χάσει βάρος"], 0, "κοιμούνται καλύτερα και πέφτουν λιγότερο"),
 ],
 "gloss": {"χορογράφο": "χορογράφος — choreographer", "ερασιτέχνες": "ερασιτέχνης — amateur", "ΚΑΠΗ": "ΚΑΠΗ — community centre for older people", "ισορροπία": "ισορροπία — balance", "χορογραφείς": "χορογραφώ — to choreograph", "πηδήματα": "πήδημα — jump", "σπαγκάτα": "σπαγκάτο — the splits", "κουβαλάνε": "κουβαλάω — to carry", "ναυτικός": "ναυτικός — sailor", "σκοινί": "σκοινί — rope", "πρεμιέρα": "πρεμιέρα — premiere", "περήφανη": "περήφανος — proud"},
})

ITEMS.append({
 "id": "l169-int-afigitria-ichitikon-vivlion", "title": "Η αφηγήτρια των ηχητικών βιβλίων", "title_en": "The audiobook narrator", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια ηθοποιό που διαβάζει μυθιστορήματα για ηχητικά βιβλία.",
 "script": [
  L("Δημοσιογράφος", "f", "Πόσο χρόνο χρειάζεστε για να ηχογραφήσετε ένα βιβλίο;", "How long do you need to record a book?"),
  L("Ηθοποιός", "f", "Για ένα μυθιστόρημα τριακοσίων σελίδων, περίπου δέκα μέρες στο στούντιο. Αλλά πριν από αυτό το διαβάζω ολόκληρο δύο φορές στο σπίτι. Σημειώνω ποιος μιλάει, με τι διάθεση, και ψάχνω πώς προφέρονται τα δύσκολα ονόματα. Δεν μπορείς να ανακαλύψεις στη σελίδα διακόσια ότι ένας ήρωας τραυλίζει.", "For a three-hundred-page novel, about ten days in the studio. But before that I read the whole thing twice at home. I note who is speaking and in what mood, and I look up how the difficult names are pronounced. You can't discover on page two hundred that a character stutters."),
  L("Δημοσιογράφος", "f", "Αλλάζετε φωνή για κάθε ήρωα;", "Do you change your voice for each character?"),
  L("Ηθοποιός", "f", "Λίγο, όχι πολύ. Αν κάνω μια υπερβολική ανδρική φωνή, ο ακροατής κουράζεται. Αρκεί μια μικρή διαφορά στον ρυθμό ή στο ύψος. Ο ακροατής τελικά ακούει τον ήρωα με το μυαλό του, όχι με τα αυτιά του.", "A little, not much. If I do an exaggerated male voice, the listener gets tired. A small difference in rhythm or pitch is enough. In the end the listener hears the character with their mind, not their ears."),
  L("Δημοσιογράφος", "f", "Ποιος είναι ο μεγαλύτερος εχθρός σας στο στούντιο;", "What is your biggest enemy in the studio?"),
  L("Ηθοποιός", "f", "Το στομάχι μου! Τα μικρόφωνα είναι τόσο ευαίσθητα, που πιάνουν κάθε γουργουρητό. Έχω πάντα μαζί μου ένα μήλο, και δεν φοράω ποτέ βραχιόλια, γιατί κάθε φορά που γυρίζω σελίδα ακούγονται σαν καμπάνες.", "My stomach! The microphones are so sensitive that they pick up every rumble. I always have an apple with me, and I never wear bracelets, because every time I turn a page they sound like bells."),
 ],
 "questions": [
  Q("Τι κάνει πριν πάει στο στούντιο;", ["Ακούει άλλα ηχητικά βιβλία", "Διαβάζει το βιβλίο ολόκληρο δύο φορές και κρατάει σημειώσεις", "Συναντά τον συγγραφέα", "Κάνει μαθήματα φωνητικής"], 1, "το διαβάζω ολόκληρο δύο φορές στο σπίτι"),
  Q("Γιατί δεν αλλάζει πολύ τη φωνή της για κάθε ήρωα;", ["Γιατί δεν της το επιτρέπει ο εκδότης", "Γιατί κουράζεται η ίδια", "Γιατί μια υπερβολική φωνή κουράζει τον ακροατή", "Γιατί δεν έχει χρόνο"], 2, "Αν κάνω μια υπερβολική ανδρική φωνή, ο ακροατής κουράζεται"),
  Q("Γιατί δεν φοράει βραχιόλια στο στούντιο;", ["Γιατί ακούγονται όταν γυρίζει σελίδα", "Γιατί είναι βαριά", "Γιατί τα έχει χάσει", "Γιατί την ενοχλούν όταν γράφει"], 0, "κάθε φορά που γυρίζω σελίδα ακούγονται σαν καμπάνες"),
 ],
 "gloss": {"ηχητικά βιβλία": "ηχητικό βιβλίο — audiobook", "ηχογραφήσετε": "ηχογραφώ — to record", "διάθεση": "διάθεση — mood", "προφέρονται": "προφέρομαι — to be pronounced", "τραυλίζει": "τραυλίζω — to stutter", "υπερβολική": "υπερβολικός — exaggerated", "ακροατής": "ακροατής — listener", "ύψος": "ύψος — pitch, height", "ευαίσθητα": "ευαίσθητος — sensitive", "γουργουρητό": "γουργουρητό — rumble (of the stomach)", "βραχιόλια": "βραχιόλι — bracelet", "καμπάνες": "καμπάνα — bell"},
})

ITEMS.append({
 "id": "l169-dia-na-xyriso-ta-genia", "title": "Να ξυρίσω τα γένια;", "title_en": "Should I shave my beard?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν νεαρό να συζητά με τη σύντροφό του αν πρέπει να ξυρίσει τα γένια του πριν από μια συνέντευξη για δουλειά.",
 "script": [
  L("Άρης", "m", "Αύριο έχω τη συνέντευξη στην τράπεζα. Λες να ξυρίσω τα γένια;", "Tomorrow I have the interview at the bank. Do you think I should shave my beard?"),
  L("Μυρτώ", "f", "Γιατί; Σου πάνε πολύ. Και τα έχεις τρία χρόνια, θα νιώθεις σαν να φοράς τα ρούχα κάποιου άλλου.", "Why? They really suit you. And you've had it for three years; you'll feel like you're wearing someone else's clothes."),
  L("Άρης", "m", "Ναι, αλλά οι τράπεζες είναι συντηρητικές. Δεν θέλω να με απορρίψουν για μια λεπτομέρεια.", "Yes, but banks are conservative. I don't want them to reject me over a detail."),
  L("Μυρτώ", "f", "Κοίτα τις φωτογραφίες των στελεχών στην ιστοσελίδα τους. Αν έχουν κι αυτοί γένια, έχεις την απάντησή σου. Πάντως, εγώ στη θέση σου θα τα κόνταινα και θα τα περιποιόμουν. Περιποιημένα γένια δείχνουν ότι προσέχεις τον εαυτό σου.", "Look at the photos of their executives on their website. If they have beards too, you have your answer. Anyway, if I were you I'd trim it and tidy it up. A well-kept beard shows you take care of yourself."),
  L("Άρης", "m", "Κάτσε να δω... Ο διευθυντής έχει μούσι! Ωραία, τότε θα πάω απόψε στον κουρέα να μου τα φτιάξει.", "Let me see... The director has a beard! Great, then I'll go to the barber tonight to have it tidied up."),
  L("Μυρτώ", "f", "Και μην ξεχάσεις να σιδερώσεις το πουκάμισο. Αυτό το προσέχουν σίγουρα.", "And don't forget to iron your shirt. That they definitely notice."),
 ],
 "questions": [
  Q("Γιατί σκέφτεται ο Άρης να ξυρίσει τα γένια του;", ["Γιατί δεν αρέσουν στη Μυρτώ", "Γιατί πιστεύει ότι οι τράπεζες είναι συντηρητικές", "Γιατί είναι καλοκαίρι", "Γιατί το ζήτησε η τράπεζα"], 1, "οι τράπεζες είναι συντηρητικές"),
  Q("Τι του προτείνει η Μυρτώ να κάνει;", ["Να ρωτήσει έναν φίλο του", "Να ξυριστεί εντελώς", "Να κοιτάξει τις φωτογραφίες των στελεχών στην ιστοσελίδα της τράπεζας", "Να ακυρώσει τη συνέντευξη"], 2, "Κοίτα τις φωτογραφίες των στελεχών στην ιστοσελίδα τους"),
  Q("Τι αποφασίζει τελικά ο Άρης;", ["Να πάει στον κουρέα να του φτιάξει τα γένια", "Να ξυριστεί μόνος του", "Να μην κάνει τίποτα", "Να αγοράσει καινούργιο πουκάμισο"], 0, "θα πάω απόψε στον κουρέα να μου τα φτιάξει"),
 ],
 "gloss": {"ξυρίσει": "ξυρίζω — to shave", "γένια": "γένια — beard", "σύντροφό": "σύντροφος — partner", "συντηρητικές": "συντηρητικός — conservative", "απορρίψουν": "απορρίπτω — to reject", "στελεχών": "στέλεχος — executive", "κόνταινα": "κονταίνω — to shorten, trim", "περιποιόμουν": "περιποιούμαι — to take care of, groom", "Περιποιημένα": "περιποιημένος — well-kept", "μούσι": "μούσι — beard", "κουρέα": "κουρέας — barber", "σιδερώσεις": "σιδερώνω — to iron"},
})

ITEMS.append({
 "id": "l169-dia-ti-tainia-apopse", "title": "Τι ταινία θα δούμε απόψε;", "title_en": "Which film shall we watch tonight?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλους που προσπαθούν να διαλέξουν μια ταινία για το βράδυ.",
 "script": [
  L("Στέλιος", "m", "Λοιπόν, τι βλέπουμε; Έχω βρει ένα θρίλερ που λένε ότι δεν σε αφήνει να κοιμηθείς.", "So, what are we watching? I've found a thriller that they say won't let you sleep."),
  L("Δανάη", "f", "Ακριβώς γι' αυτό όχι. Αύριο ξυπνάω στις έξι για τη δουλειά. Θέλω κάτι ελαφρύ, μια κωμωδία.", "That's exactly why not. Tomorrow I wake up at six for work. I want something light, a comedy."),
  L("Στέλιος", "m", "Οι καινούργιες κωμωδίες είναι όλες ίδιες. Τι λες για ένα ντοκιμαντέρ; Υπάρχει ένα για τα χταπόδια που έχει πάρει βραβεία.", "The new comedies are all the same. What about a documentary? There's one about octopuses that has won awards."),
  L("Δανάη", "f", "Χταπόδια στις έντεκα το βράδυ; Θα με πάρει ο ύπνος στα πρώτα δέκα λεπτά. Ξέρεις κάτι; Ας δούμε μια παλιά ελληνική ταινία. Αυτές δεν αποτυγχάνουν ποτέ.", "Octopuses at eleven at night? I'll fall asleep in the first ten minutes. You know what? Let's watch an old Greek film. Those never fail."),
  L("Στέλιος", "m", "Με τη Βουγιουκλάκη; Τις έχω δει όλες δέκα φορές.", "With Vougiouklaki? I've seen them all ten times."),
  L("Δανάη", "f", "Ε, και; Θα τις δεις και ενδέκατη. Εσύ φτιάχνεις ποπ κορν, εγώ διαλέγω. Και το θρίλερ το βλέπουμε το Σάββατο, που δεν θα ξυπνάμε νωρίς.", "So what? You'll watch them an eleventh time. You make popcorn, I choose. And we'll watch the thriller on Saturday, when we won't be getting up early."),
 ],
 "questions": [
  Q("Γιατί η Δανάη δεν θέλει να δει το θρίλερ απόψε;", ["Γιατί το έχει ήδη δει", "Γιατί αύριο ξυπνάει νωρίς για τη δουλειά", "Γιατί δεν της αρέσουν τα θρίλερ", "Γιατί είναι πολύ μεγάλο"], 1, "Αύριο ξυπνάω στις έξι για τη δουλειά"),
  Q("Γιατί απορρίπτει το ντοκιμαντέρ;", ["Γιατί δεν της αρέσουν τα ζώα", "Γιατί είναι στα αγγλικά", "Γιατί φοβάται ότι θα την πάρει ο ύπνος", "Γιατί το έχει δει"], 2, "Θα με πάρει ο ύπνος στα πρώτα δέκα λεπτά"),
  Q("Τι συμφωνούν τελικά;", ["Μια παλιά ελληνική ταινία απόψε και το θρίλερ το Σάββατο", "Το θρίλερ απόψε", "Να βγουν στο σινεμά", "Μια καινούργια κωμωδία"], 0, "Και το θρίλερ το βλέπουμε το Σάββατο"),
 ],
 "gloss": {"θρίλερ": "θρίλερ — thriller", "ελαφρύ": "ελαφρύς — light", "κωμωδία": "κωμωδία — comedy", "ντοκιμαντέρ": "ντοκιμαντέρ — documentary", "χταπόδια": "χταπόδι — octopus", "βραβεία": "βραβείο — award, prize", "αποτυγχάνουν": "αποτυγχάνω — to fail", "Βουγιουκλάκη": "Βουγιουκλάκη — Aliki Vougiouklaki, star of classic Greek film comedies", "ποπ κορν": "ποπ κορν — popcorn"},
})

ITEMS.append({
 "id": "l169-mon-ski-sta-saranta", "title": "Έμαθα σκι στα σαράντα", "title_en": "I learned to ski at forty", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να διηγείται σε ένα ραδιοφωνικό πρόγραμμα πώς έμαθε σκι στα σαράντα του.",
 "script": [
  L("Άντρας", "m", "Μεγάλωσα σε νησί, και το χιόνι το έβλεπα μόνο στην τηλεόραση. Όταν η κόρη μου άρχισε σκι με το σχολείο, εγώ καθόμουν στην καφετέρια του χιονοδρομικού και την κοίταζα από το τζάμι. Μια μέρα μού είπε: «Μπαμπά, γιατί δεν έρχεσαι κι εσύ;» Δεν είχα απάντηση.", "I grew up on an island and only ever saw snow on television. When my daughter started skiing with her school, I sat in the ski centre café and watched her through the window. One day she said to me: 'Dad, why don't you come too?' I had no answer."),
  L("Άντρας", "m", "Έκλεισα μαθήματα με έναν δάσκαλο. Την πρώτη μέρα έπεσα, νομίζω, τριάντα φορές. Το πιο δύσκολο δεν ήταν τα πόδια, ήταν το μυαλό. Τα παιδιά πέφτουν και σηκώνονται γελώντας· εμείς οι μεγάλοι ντρεπόμαστε. Ο δάσκαλός μου μού είπε να μάθω πρώτα να πέφτω σωστά, στο πλάι, και μετά να σκέφτομαι το στρίψιμο.", "I booked lessons with an instructor. On the first day I fell, I think, thirty times. The hardest part wasn't the legs, it was the mind. Children fall and get up laughing; we adults feel embarrassed. My instructor told me to learn first how to fall properly, to the side, and then think about turning."),
  L("Άντρας", "m", "Τώρα, τρία χρόνια μετά, κατεβαίνουμε μαζί με την κόρη μου τις κόκκινες πίστες. Εκείνη είναι πολύ καλύτερη από μένα, και αυτό μου αρέσει. Είναι η μόνη ώρα της εβδομάδας που με περιμένει εκείνη, αντί να την περιμένω εγώ.", "Now, three years later, my daughter and I go down the red runs together. She's much better than me, and I like that. It's the only time of the week when she waits for me instead of me waiting for her."),
 ],
 "questions": [
  Q("Τι τον έκανε να αρχίσει σκι;", ["Μια συμβουλή του γιατρού του", "Μια ερώτηση της κόρης του", "Μια διαφήμιση στην τηλεόραση", "Ένας φίλος του από το νησί"], 1, "«Μπαμπά, γιατί δεν έρχεσαι κι εσύ;»"),
  Q("Τι ήταν, κατά τον ίδιο, το πιο δύσκολο;", ["Το κρύο", "Τα πόδια", "Το μυαλό, γιατί οι μεγάλοι ντρέπονται όταν πέφτουν", "Ο εξοπλισμός"], 2, "Το πιο δύσκολο δεν ήταν τα πόδια, ήταν το μυαλό"),
  Q("Τι του αρέσει τώρα που κάνουν σκι μαζί;", ["Ότι η κόρη του είναι καλύτερη και τον περιμένει", "Ότι είναι πια καλύτερος από την κόρη του", "Ότι κατεβαίνουν μόνο τις εύκολες πίστες", "Ότι πηγαίνουν κάθε μέρα"], 0, "Εκείνη είναι πολύ καλύτερη από μένα, και αυτό μου αρέσει"),
 ],
 "gloss": {"χιονοδρομικού": "χιονοδρομικό (κέντρο) — ski centre", "τζάμι": "τζάμι — window pane", "Έκλεισα": "κλείνω — to book", "ντρεπόμαστε": "ντρέπομαι — to feel embarrassed", "πλάι": "πλάι — side", "στρίψιμο": "στρίψιμο — turning", "πίστες": "πίστα — ski run, slope"},
})

ITEMS.append({
 "id": "l169-vm-xechasate-ta-gantia", "title": "Ξεχάσατε τα γάντια σας", "title_en": "You left your gloves behind", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από το ταμείο ενός θεάτρου.",
 "script": [
  L("Υπάλληλος", "f", "Καλησπέρα σας, σας τηλεφωνούμε από το ταμείο του θεάτρου «Ορφέας». Χθες το βράδυ, μετά την παράσταση, οι ταξιθέτριες βρήκαν στη θέση σας, στη σειρά Ζ, ένα ζευγάρι δερμάτινα γάντια και ένα μάλλινο κασκόλ. Βρήκαμε τον αριθμό σας από την ηλεκτρονική κράτηση.", "Good evening, we're calling from the box office of the Orfeas theatre. Last night, after the performance, the ushers found on your seat, in row Z, a pair of leather gloves and a woollen scarf. We found your number from the online booking."),
  L("Υπάλληλος", "f", "Μπορείτε να τα παραλάβετε από το ταμείο, που είναι ανοιχτό καθημερινά από τις πέντε το απόγευμα. Τη Δευτέρα είμαστε κλειστά. Παρακαλούμε να φέρετε μαζί σας την ταυτότητά σας.", "You can collect them from the box office, which is open daily from five in the afternoon. On Monday we're closed. Please bring your ID card with you."),
  L("Υπάλληλος", "f", "Αν δεν μπορείτε να έρθετε εσείς, μπορεί να τα πάρει κάποιος άλλος για λογαριασμό σας, αρκεί να μας στείλετε πρώτα ένα μήνυμα με το όνομά του. Ευχαριστούμε, και ελπίζουμε να σας ξαναδούμε σύντομα.", "If you can't come yourself, someone else can collect them on your behalf, as long as you first send us a message with their name. Thank you, and we hope to see you again soon."),
 ],
 "questions": [
  Q("Τι βρέθηκε στη θέση του ακροατή;", ["Ένα κινητό τηλέφωνο", "Ένα ζευγάρι γάντια και ένα κασκόλ", "Μια ομπρέλα", "Ένα πορτοφόλι"], 1, "ένα ζευγάρι δερμάτινα γάντια και ένα μάλλινο κασκόλ"),
  Q("Πότε είναι κλειστό το ταμείο;", ["Το Σάββατο", "Κάθε πρωί", "Τη Δευτέρα", "Την Κυριακή"], 2, "Τη Δευτέρα είμαστε κλειστά"),
  Q("Τι πρέπει να κάνει ο ακροατής αν στείλει κάποιον άλλον;", ["Να στείλει πρώτα ένα μήνυμα με το όνομά του", "Να πληρώσει ένα μικρό ποσό", "Να του δώσει το εισιτήριο", "Να τηλεφωνήσει την ίδια μέρα"], 0, "αρκεί να μας στείλετε πρώτα ένα μήνυμα με το όνομά του"),
 ],
 "gloss": {"ταμείο": "ταμείο — box office", "ταξιθέτριες": "ταξιθέτρια — usher (f.)", "σειρά": "σειρά — row", "δερμάτινα": "δερμάτινος — leather", "μάλλινο": "μάλλινος — woollen", "κασκόλ": "κασκόλ — scarf", "ηλεκτρονική κράτηση": "ηλεκτρονική κράτηση — online booking", "παραλάβετε": "παραλαμβάνω — to collect", "για λογαριασμό σας": "για λογαριασμό κάποιου — on someone's behalf"},
})

ITEMS.append({
 "id": "l169-vm-ypotrofia", "title": "Μήνυμα για την υποτροφία", "title_en": "A message about the scholarship", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από ένα ίδρυμα που χορηγεί υποτροφίες σε φοιτητές.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα, σας τηλεφωνώ από το γραφείο υποτροφιών του ιδρύματος. Έχω την ευχάριστη υποχρέωση να σας ανακοινώσω ότι η αίτησή σας εγκρίθηκε. Η υποτροφία καλύπτει τα δίδακτρα του μεταπτυχιακού και ένα μηνιαίο ποσό για τα έξοδα διαμονής.", "Good morning, I'm calling from the foundation's scholarship office. I have the pleasant duty of informing you that your application has been approved. The scholarship covers the master's tuition fees and a monthly amount for living expenses."),
  L("Υπάλληλος", "m", "Για να υπογράψουμε τη σύμβαση, χρειαζόμαστε ακόμα δύο έγγραφα: τη βεβαίωση εγγραφής από το πανεπιστήμιο και ένα αντίγραφο του διαβατηρίου σας. Μπορείτε να τα στείλετε ηλεκτρονικά μέχρι τις δεκαπέντε του μήνα.", "To sign the contract, we still need two documents: the certificate of enrolment from the university and a copy of your passport. You can send them electronically by the fifteenth of the month."),
  L("Υπάλληλος", "m", "Τέλος, κάθε χρόνο οργανώνουμε μια συνάντηση με όλους τους νέους υποτρόφους. Φέτος θα γίνει στις είκοσι Σεπτεμβρίου. Δεν είναι υποχρεωτική, αλλά θα σας συνιστούσα να έρθετε, γιατί θα γνωρίσετε παλιούς υποτρόφους που σπούδασαν στην ίδια πόλη. Συγχαρητήρια ξανά!", "Finally, every year we organise a meeting with all the new scholarship holders. This year it will be on the twentieth of September. It's not compulsory, but I'd recommend you come, because you'll meet former scholars who studied in the same city. Congratulations again!"),
 ],
 "questions": [
  Q("Τι καλύπτει η υποτροφία;", ["Μόνο τα εισιτήρια του αεροπλάνου", "Τα δίδακτρα και ένα μηνιαίο ποσό για τη διαμονή", "Μόνο τα βιβλία", "Το μισό ενοίκιο"], 1, "καλύπτει τα δίδακτρα του μεταπτυχιακού και ένα μηνιαίο ποσό"),
  Q("Ποια έγγραφα λείπουν ακόμα;", ["Η αίτηση και το βιογραφικό", "Οι συστατικές επιστολές", "Η βεβαίωση εγγραφής και ένα αντίγραφο του διαβατηρίου", "Το πτυχίο και η βαθμολογία"], 2, "τη βεβαίωση εγγραφής από το πανεπιστήμιο και ένα αντίγραφο του διαβατηρίου σας"),
  Q("Γιατί ο υπάλληλος προτείνει να πάει στη συνάντηση;", ["Για να γνωρίσει παλιούς υποτρόφους που σπούδασαν στην ίδια πόλη", "Γιατί είναι υποχρεωτική", "Για να υπογράψει τη σύμβαση", "Για να πάρει τα χρήματα"], 0, "θα γνωρίσετε παλιούς υποτρόφους που σπούδασαν στην ίδια πόλη"),
 ],
 "gloss": {"ίδρυμα": "ίδρυμα — foundation", "χορηγεί": "χορηγώ — to grant", "υποτροφίες": "υποτροφία — scholarship", "εγκρίθηκε": "εγκρίνω — to approve", "δίδακτρα": "δίδακτρα — tuition fees", "μεταπτυχιακού": "μεταπτυχιακό — master's degree", "διαμονής": "διαμονή — living, stay", "σύμβαση": "σύμβαση — contract", "βεβαίωση εγγραφής": "βεβαίωση εγγραφής — certificate of enrolment", "αντίγραφο": "αντίγραφο — copy", "υποτρόφους": "υπότροφος — scholarship holder", "υποχρεωτική": "υποχρεωτικός — compulsory"},
})

ITEMS.append({
 "id": "l169-c1-kremmydi-dakrya", "title": "Γιατί κλαίμε όταν κόβουμε κρεμμύδι", "title_en": "Why we cry when we cut onions", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια χημικό τροφίμων σε μια εκπομπή για την επιστήμη στην κουζίνα.",
 "script": [
  L("Δημοσιογράφος", "m", "Γιατί το κρεμμύδι μάς κάνει να κλαίμε, ενώ η ντομάτα όχι;", "Why does an onion make us cry while a tomato doesn't?"),
  L("Χημικός", "f", "Το κρεμμύδι είναι, θα λέγαμε, οπλισμένο. Στα κύτταρά του υπάρχουν θειούχες ενώσεις και, χωριστά, ένζυμα. Όσο το κρεμμύδι είναι ακέραιο, δεν συναντιούνται. Όταν το κόβουμε, τα κύτταρα σπάνε, οι ουσίες ανακατεύονται και, μέσα από μια σειρά αντιδράσεων, παράγεται ένα πτητικό αέριο. Αυτό ανεβαίνει, φτάνει στα μάτια μας και ερεθίζει τα νεύρα του κερατοειδούς. Τα μάτια παράγουν δάκρυα για να το ξεπλύνουν.", "The onion is, so to speak, armed. Its cells contain sulphur compounds and, separately, enzymes. As long as the onion is whole, they don't meet. When we cut it, the cells break, the substances mix and, through a series of reactions, a volatile gas is produced. It rises, reaches our eyes and irritates the nerves of the cornea. The eyes produce tears to wash it away."),
  L("Δημοσιογράφος", "m", "Δηλαδή είναι ένας μηχανισμός άμυνας;", "So it's a defence mechanism?"),
  L("Χημικός", "f", "Έτσι πιστεύεται: προστατεύει το φυτό από ζώα και έντομα που θα ήθελαν να το φάνε. Εμείς απλώς είμαστε παράπλευρα θύματα. Ενδιαφέρον έχει ότι το μαγείρεμα καταστρέφει τα ένζυμα, γι' αυτό το ψημένο κρεμμύδι δεν τσούζει και γίνεται γλυκό.", "That's what's believed: it protects the plant from animals and insects that would like to eat it. We are simply collateral victims. Interestingly, cooking destroys the enzymes, which is why cooked onion doesn't sting and becomes sweet."),
  L("Δημοσιογράφος", "m", "Υπάρχει τρόπος να γλιτώσουμε τα δάκρυα;", "Is there a way to avoid the tears?"),
  L("Χημικός", "f", "Μερικοί μικροί. Βάλτε το κρεμμύδι στο ψυγείο μισή ώρα πριν, γιατί στο κρύο το αέριο εξατμίζεται πιο αργά. Χρησιμοποιήστε ένα πολύ κοφτερό μαχαίρι, που σπάει λιγότερα κύτταρα. Και αφήστε τη ρίζα για το τέλος, γιατί εκεί οι ουσίες είναι πιο πυκνές. Έχουν δημιουργηθεί και ποικιλίες που προκαλούν πολύ λιγότερα δάκρυα, αλλά πολλοί μάγειρες λένε ότι έχουν και λιγότερη γεύση.", "A few small ones. Put the onion in the fridge half an hour beforehand, because in the cold the gas evaporates more slowly. Use a very sharp knife, which breaks fewer cells. And leave the root till last, because the substances are more concentrated there. Varieties that cause far fewer tears have also been developed, but many cooks say they have less flavour too."),
 ],
 "questions": [
  Q("Πότε παράγεται το αέριο που μας κάνει να κλαίμε;", ["Όταν το κρεμμύδι μένει πολύ καιρό στο ράφι", "Όταν κόβουμε το κρεμμύδι και οι ουσίες των κυττάρων ανακατεύονται", "Όταν το κρεμμύδι ψήνεται", "Όταν το πλένουμε με νερό"], 1, "Όταν το κόβουμε, τα κύτταρα σπάνε, οι ουσίες ανακατεύονται"),
  Q("Γιατί το ψημένο κρεμμύδι δεν τσούζει;", ["Γιατί χάνει όλο το νερό του", "Γιατί το λάδι απορροφά το αέριο", "Γιατί το μαγείρεμα καταστρέφει τα ένζυμα", "Γιατί η ζάχαρη εξουδετερώνει το αέριο"], 2, "το μαγείρεμα καταστρέφει τα ένζυμα"),
  Q("Γιατί προτείνει να αφήσουμε τη ρίζα για το τέλος;", ["Γιατί εκεί οι ουσίες είναι πιο πυκνές", "Γιατί είναι πιο σκληρή", "Γιατί δεν τρώγεται", "Γιατί έχει περισσότερη γεύση"], 0, "γιατί εκεί οι ουσίες είναι πιο πυκνές"),
 ],
 "gloss": {"χημικό": "χημικός — chemist", "τροφίμων": "τρόφιμα — food", "οπλισμένο": "οπλισμένος — armed", "κύτταρά": "κύτταρο — cell", "θειούχες": "θειούχος — sulphur-containing", "ενώσεις": "ένωση — compound", "ένζυμα": "ένζυμο — enzyme", "ακέραιο": "ακέραιος — whole, intact", "πτητικό": "πτητικός — volatile", "ερεθίζει": "ερεθίζω — to irritate", "κερατοειδούς": "κερατοειδής — cornea", "άμυνας": "άμυνα — defence", "παράπλευρα θύματα": "παράπλευρα θύματα — collateral victims", "τσούζει": "τσούζω — to sting", "εξατμίζεται": "εξατμίζομαι — to evaporate", "κοφτερό": "κοφτερός — sharp", "ποικιλίες": "ποικιλία — variety"},
})

ITEMS.append({
 "id": "l169-c1-fournos-mikrokymaton", "title": "Πώς ζεσταίνει ο φούρνος μικροκυμάτων", "title_en": "How a microwave oven heats food", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν φυσικό να εξηγεί σε μια εκπομπή εκλαΐκευσης της επιστήμης πώς λειτουργεί ο φούρνος μικροκυμάτων.",
 "script": [
  L("Φυσικός", "m", "Ο φούρνος μικροκυμάτων δεν έχει αντιστάσεις που κοκκινίζουν. Παράγει ηλεκτρομαγνητικά κύματα που αλλάζουν κατεύθυνση περίπου δυόμισι δισεκατομμύρια φορές το δευτερόλεπτο. Τα μόρια του νερού στο φαγητό έχουν δύο πόλους, σαν μικροί μαγνήτες, και προσπαθούν συνεχώς να στραφούν προς την κατεύθυνση του πεδίου. Καθώς περιστρέφονται και συγκρούονται με τα γειτονικά μόρια, παράγεται θερμότητα.", "A microwave oven has no heating elements that glow red. It produces electromagnetic waves that change direction about two and a half billion times a second. The water molecules in food have two poles, like tiny magnets, and constantly try to turn towards the direction of the field. As they rotate and collide with neighbouring molecules, heat is produced."),
  L("Φυσικός", "m", "Υπάρχει ένας διαδεδομένος μύθος, ότι ο φούρνος ψήνει το φαγητό από μέσα προς τα έξω. Στην πραγματικότητα, τα μικροκύματα διεισδύουν μόνο λίγα εκατοστά. Το κέντρο ενός μεγάλου κομματιού κρέατος ζεσταίνεται με τον συνηθισμένο τρόπο, καθώς η θερμότητα περνάει σιγά σιγά προς τα μέσα. Επιπλέον, μέσα στον θάλαμο σχηματίζονται σημεία όπου τα κύματα ενισχύονται και άλλα όπου σχεδόν εξαφανίζονται. Γι' αυτό υπάρχει το περιστρεφόμενο πιάτο: για να περνάει το φαγητό από όλα τα σημεία.", "There's a widespread myth that the oven cooks food from the inside out. In reality, microwaves penetrate only a few centimetres. The centre of a large piece of meat heats up in the usual way, as the heat slowly passes inwards. Moreover, inside the chamber there form spots where the waves are reinforced and others where they almost vanish. That's why there is the rotating plate: so the food passes through all the spots."),
  L("Φυσικός", "m", "Και ο πάγος; Τα μόρια του νερού στον πάγο είναι παγιδευμένα σε κρυστάλλους και δεν περιστρέφονται εύκολα. Γι' αυτό η απόψυξη γίνεται με διακοπές: ο φούρνος δουλεύει λίγα δευτερόλεπτα και σταματάει, ώστε η θερμότητα από τα σημεία που έλιωσαν να απλωθεί, πριν αυτά αρχίσουν να βράζουν ενώ τα διπλανά είναι ακόμα παγωμένα.", "And ice? The water molecules in ice are trapped in crystals and don't rotate easily. That's why defrosting is done in bursts: the oven runs for a few seconds and stops, so that the heat from the parts that have melted can spread, before they start boiling while the parts next to them are still frozen."),
 ],
 "questions": [
  Q("Πώς παράγεται η θερμότητα στο φαγητό;", ["Από αντιστάσεις που κοκκινίζουν", "Από τα μόρια του νερού που περιστρέφονται και συγκρούονται", "Από τον ζεστό αέρα του θαλάμου", "Από το πιάτο που ζεσταίνεται"], 1, "Καθώς περιστρέφονται και συγκρούονται με τα γειτονικά μόρια, παράγεται θερμότητα"),
  Q("Τι ισχύει για τον μύθο ότι ο φούρνος ψήνει από μέσα προς τα έξω;", ["Ισχύει μόνο για το κρέας", "Ισχύει απόλυτα", "Δεν ισχύει, γιατί τα μικροκύματα διεισδύουν μόνο λίγα εκατοστά", "Ισχύει μόνο για τα κατεψυγμένα"], 2, "τα μικροκύματα διεισδύουν μόνο λίγα εκατοστά"),
  Q("Γιατί η απόψυξη γίνεται με διακοπές;", ["Για να απλωθεί η θερμότητα πριν αρχίσουν να βράζουν τα σημεία που έλιωσαν", "Για να μην καταναλώνει πολύ ρεύμα", "Για να μη χαλάσει ο φούρνος", "Για να μη σπάσει το πιάτο"], 0, "ώστε η θερμότητα από τα σημεία που έλιωσαν να απλωθεί"),
 ],
 "gloss": {"φυσικό": "φυσικός — physicist", "εκλαΐκευσης": "εκλαΐκευση — popularisation", "μικροκυμάτων": "μικροκύματα — microwaves", "αντιστάσεις": "αντίσταση — heating element", "ηλεκτρομαγνητικά": "ηλεκτρομαγνητικός — electromagnetic", "μόρια": "μόριο — molecule", "πόλους": "πόλος — pole", "πεδίου": "πεδίο — field", "περιστρέφονται": "περιστρέφομαι — to rotate", "συγκρούονται": "συγκρούομαι — to collide", "διεισδύουν": "διεισδύω — to penetrate", "θάλαμο": "θάλαμος — chamber", "ενισχύονται": "ενισχύομαι — to be reinforced", "περιστρεφόμενο": "περιστρεφόμενος — rotating", "παγιδευμένα": "παγιδευμένος — trapped", "κρυστάλλους": "κρύσταλλος — crystal", "απόψυξη": "απόψυξη — defrosting"},
})

rnd = random.Random(169)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-169.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
