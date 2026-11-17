# Source for library/listening/listening-172.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l172.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l172-ann-pisina-xenodocheiou", "title": "Ανακοίνωση στην πισίνα του ξενοδοχείου", "title_en": "An announcement at the hotel pool", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα στην πισίνα ενός ξενοδοχείου.",
 "script": [
  L("Υπάλληλος", "f", "Αγαπητοί επισκέπτες, καλημέρα σας. Σας υπενθυμίζουμε ότι η πισίνα λειτουργεί από τις εννιά το πρωί έως τις επτά το απόγευμα. Από τη μία έως τις δύο ο ναυαγοσώστης κάνει διάλειμμα και το κολύμπι δεν επιτρέπεται.", "Dear guests, good morning. We remind you that the pool is open from nine in the morning until seven in the evening. From one to two the lifeguard takes a break and swimming is not allowed."),
  L("Υπάλληλος", "f", "Για λόγους ασφαλείας, παρακαλούμε να μη φέρνετε γυάλινα ποτήρια και μπουκάλια κοντά στην πισίνα. Στο μπαρ θα βρείτε πλαστικά ποτήρια. Τα παιδιά κάτω των δώδεκα ετών πρέπει να συνοδεύονται πάντα από έναν ενήλικα.", "For safety reasons, please do not bring glasses or bottles near the pool. You'll find plastic cups at the bar. Children under twelve must always be accompanied by an adult."),
  L("Υπάλληλος", "f", "Τέλος, σας ενημερώνουμε ότι σήμερα στις έντεκα θα γίνει μάθημα γυμναστικής μέσα στο νερό, στη μικρή πισίνα. Η συμμετοχή είναι δωρεάν, αλλά οι θέσεις είναι περιορισμένες, γι' αυτό δηλώστε το όνομά σας στη ρεσεψιόν. Καλή σας διασκέδαση.", "Finally, we inform you that today at eleven there will be an exercise class in the water, in the small pool. Participation is free, but places are limited, so give your name at reception. Have fun."),
 ],
 "questions": [
  Q("Γιατί δεν επιτρέπεται το κολύμπι από τη μία έως τις δύο;", ["Γιατί καθαρίζεται η πισίνα", "Γιατί ο ναυαγοσώστης κάνει διάλειμμα", "Γιατί κάνει πολλή ζέστη", "Γιατί γίνεται μάθημα"], 1, "ο ναυαγοσώστης κάνει διάλειμμα"),
  Q("Τι πρέπει να ισχύει για τα παιδιά κάτω των δώδεκα;", ["Να κολυμπούν μόνο στη μικρή πισίνα", "Να φορούν μπρατσάκια", "Να συνοδεύονται πάντα από έναν ενήλικα", "Να μην μπαίνουν στο νερό μετά τις πέντε"], 2, "πρέπει να συνοδεύονται πάντα από έναν ενήλικα"),
  Q("Τι πρέπει να κάνει όποιος θέλει να πάρει μέρος στο μάθημα;", ["Να δηλώσει το όνομά του στη ρεσεψιόν", "Να πληρώσει στο μπαρ", "Να έρθει στις δέκα", "Να φέρει δική του πετσέτα"], 0, "δηλώστε το όνομά σας στη ρεσεψιόν"),
 ],
 "gloss": {"πισίνα": "πισίνα — swimming pool", "ναυαγοσώστης": "ναυαγοσώστης — lifeguard", "διάλειμμα": "διάλειμμα — break", "γυάλινα": "γυάλινος — glass", "συνοδεύονται": "συνοδεύομαι — to be accompanied", "ενήλικα": "ενήλικας — adult", "συμμετοχή": "συμμετοχή — participation", "περιορισμένες": "περιορισμένος — limited", "ρεσεψιόν": "ρεσεψιόν — reception"},
})

ITEMS.append({
 "id": "l172-int-syntaktria-lexikon", "title": "Η συντάκτρια λεξικών", "title_en": "The dictionary editor", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γλωσσολόγο που δουλεύει στη σύνταξη ενός λεξικού της νέας ελληνικής.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς αποφασίζετε ότι μια καινούργια λέξη θα μπει στο λεξικό;", "How do you decide that a new word will go into the dictionary?"),
  L("Γλωσσολόγος", "f", "Δεν αρκεί να την ακούσουμε μια δυο φορές. Ψάχνουμε σε μια τεράστια ηλεκτρονική βάση με κείμενα, εφημερίδες, βιβλία, ακόμα και αναρτήσεις. Αν η λέξη εμφανίζεται συχνά, για αρκετά χρόνια και σε διαφορετικά είδη κειμένων, τότε την εξετάζουμε σοβαρά.", "It's not enough to hear it once or twice. We search a huge electronic database of texts, newspapers, books, even posts. If the word appears often, for several years and in different kinds of texts, then we consider it seriously."),
  L("Δημοσιογράφος", "m", "Δηλαδή μπορεί να μπει και μια λέξη της αργκό;", "So a slang word could go in too?"),
  L("Γλωσσολόγος", "f", "Βεβαίως, με την κατάλληλη σημείωση: «λαϊκό», «οικείο», «αργκό». Το λεξικό δεν λέει στον κόσμο πώς πρέπει να μιλάει· καταγράφει πώς μιλάει. Αυτό ενοχλεί μερικούς αναγνώστες, που μας στέλνουν θυμωμένα γράμματα.", "Of course, with the appropriate label: 'popular', 'familiar', 'slang'. The dictionary doesn't tell people how they should speak; it records how they speak. That annoys some readers, who send us angry letters."),
  L("Δημοσιογράφος", "m", "Βγαίνουν και λέξεις από το λεξικό;", "Do words also come out of the dictionary?"),
  L("Γλωσσολόγος", "f", "Σπάνια τις σβήνουμε. Συνήθως τις χαρακτηρίζουμε «παρωχημένες». Μια λέξη που δεν τη χρησιμοποιεί κανείς σήμερα μπορεί να τη συναντήσει ένας μαθητής σε ένα παλιό μυθιστόρημα, και πρέπει να μπορεί να τη βρει.", "We rarely delete them. Usually we label them 'obsolete'. A word nobody uses today may be met by a student in an old novel, and he must be able to find it."),
 ],
 "questions": [
  Q("Πότε εξετάζουν σοβαρά μια καινούργια λέξη;", ["Όταν τη χρησιμοποιεί ένας γνωστός συγγραφέας", "Όταν εμφανίζεται συχνά, για αρκετά χρόνια και σε διαφορετικά κείμενα", "Όταν τη ζητούν οι αναγνώστες", "Όταν μπει σε ένα ξένο λεξικό"], 1, "Αν η λέξη εμφανίζεται συχνά, για αρκετά χρόνια και σε διαφορετικά είδη κειμένων"),
  Q("Ποιος είναι, κατά τη γλωσσολόγο, ο ρόλος του λεξικού;", ["Να λέει στον κόσμο πώς πρέπει να μιλάει", "Να καταγράφει πώς μιλάει ο κόσμος", "Να καθαρίζει τη γλώσσα από την αργκό", "Να μεταφράζει ξένες λέξεις"], 1, "καταγράφει πώς μιλάει"),
  Q("Τι κάνουν συνήθως με τις λέξεις που δεν χρησιμοποιούνται πια;", ["Τις χαρακτηρίζουν «παρωχημένες»", "Τις σβήνουν αμέσως", "Τις μεταφέρουν σε ένα άλλο βιβλίο", "Τις αντικαθιστούν με νέες"], 0, "Συνήθως τις χαρακτηρίζουμε «παρωχημένες»"),
 ],
 "gloss": {"γλωσσολόγο": "γλωσσολόγος — linguist", "σύνταξη": "σύνταξη — compiling, editing", "λεξικού": "λεξικό — dictionary", "βάση": "βάση — database", "αναρτήσεις": "ανάρτηση — (online) post", "αργκό": "αργκό — slang", "σημείωση": "σημείωση — label, note", "οικείο": "οικείος — familiar, informal", "καταγράφει": "καταγράφω — to record", "σβήνουμε": "σβήνω — to delete", "παρωχημένες": "παρωχημένος — obsolete"},
})

ITEMS.append({
 "id": "l172-int-pilotos-ydroplanou", "title": "Η πιλότος του υδροπλάνου", "title_en": "The seaplane pilot", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γυναίκα που πετάει με υδροπλάνο.",
 "script": [
  L("Δημοσιογράφος", "m", "Σε τι διαφέρει ένα υδροπλάνο από ένα κανονικό αεροπλάνο;", "How is a seaplane different from an ordinary aeroplane?"),
  L("Πιλότος", "f", "Αντί για ρόδες έχει πλωτήρες, δηλαδή δύο μακριές βάρκες κάτω από την άτρακτο. Απογειώνεται και προσθαλασσώνεται στο νερό. Το πιο δύσκολο δεν είναι η πτήση, αλλά η θάλασσα: πρέπει να διαβάζεις τα κύματα όπως ένας ψαράς.", "Instead of wheels it has floats, that is, two long boats under the fuselage. It takes off from and lands on the water. The hardest part isn't the flight but the sea: you have to read the waves like a fisherman."),
  L("Δημοσιογράφος", "m", "Πού μάθατε να πετάτε έτσι;", "Where did you learn to fly like that?"),
  L("Πιλότος", "f", "Στον Καναδά, όπου τα υδροπλάνα είναι κάτι σαν ταξί. Υπάρχουν χωριά στις λίμνες του Βορρά που δεν έχουν δρόμο· το υδροπλάνο τούς φέρνει τρόφιμα, γιατρούς, ταχυδρομείο. Εκεί έκανα τρία χρόνια πριν γυρίσω στην Ελλάδα.", "In Canada, where seaplanes are something like taxis. There are villages on the northern lakes with no road; the seaplane brings them food, doctors, mail. I spent three years there before returning to Greece."),
  L("Δημοσιογράφος", "m", "Ποια είναι η αγαπημένη σας στιγμή σε μια πτήση;", "What is your favourite moment in a flight?"),
  L("Πιλότος", "f", "Η προσθαλάσσωση το πρωί, όταν η θάλασσα είναι λάδι. Ακούς το νερό να χτυπάει τους πλωτήρες και ξαφνικά από αεροπλάνο γίνεσαι βάρκα. Οι επιβάτες πάντα χειροκροτούν, ακόμα κι αν πετάνε για δέκατη φορά.", "Landing on the water in the morning, when the sea is like oil. You hear the water hit the floats and suddenly you go from aeroplane to boat. The passengers always clap, even if they're flying for the tenth time."),
 ],
 "questions": [
  Q("Τι είναι, κατά την πιλότο, το πιο δύσκολο στη δουλειά της;", ["Η πτήση μέσα στα σύννεφα", "Να διαβάζει τα κύματα της θάλασσας", "Η επικοινωνία με τους επιβάτες", "Ο καιρός στα βουνά"], 1, "πρέπει να διαβάζεις τα κύματα όπως ένας ψαράς"),
  Q("Τι ρόλο έχουν τα υδροπλάνα στον Καναδά;", ["Χρησιμοποιούνται μόνο από τουρίστες", "Είναι κάτι σαν ταξί για χωριά χωρίς δρόμο", "Μεταφέρουν μόνο ψάρια", "Χρησιμοποιούνται από τον στρατό"], 1, "τα υδροπλάνα είναι κάτι σαν ταξί"),
  Q("Τι κάνουν πάντα οι επιβάτες στην προσθαλάσσωση;", ["Βγάζουν φωτογραφίες", "Φοβούνται", "Χειροκροτούν", "Κοιμούνται"], 2, "Οι επιβάτες πάντα χειροκροτούν"),
 ],
 "gloss": {"υδροπλάνο": "υδροπλάνο — seaplane", "πλωτήρες": "πλωτήρας — float (of a seaplane)", "άτρακτο": "άτρακτος — fuselage", "Απογειώνεται": "απογειώνομαι — to take off", "προσθαλασσώνεται": "προσθαλασσώνομαι — to land on water", "πτήση": "πτήση — flight", "τρόφιμα": "τρόφιμα — food supplies", "προσθαλάσσωση": "προσθαλάσσωση — landing on water", "η θάλασσα είναι λάδι": "η θάλασσα είναι λάδι — the sea is dead calm", "χειροκροτούν": "χειροκροτώ — to clap"},
})

ITEMS.append({
 "id": "l172-dia-gipedo-i-kanapes", "title": "Γήπεδο ή καναπές;", "title_en": "Stadium or sofa?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλους να συζητούν αν θα πάνε στο γήπεδο να δουν τον τελικό του κυπέλλου ή θα τον δουν στην τηλεόραση.",
 "script": [
  L("Γιάννης", "m", "Βρήκα δύο εισιτήρια για τον τελικό! Είναι λίγο ακριβά, αλλά τέτοιος αγώνας δεν ξανάρχεται.", "I found two tickets for the final! They're a bit expensive, but a match like this won't come again."),
  L("Άρης", "m", "Πόσο ακριβά; Και πού είναι οι θέσεις;", "How expensive? And where are the seats?"),
  L("Γιάννης", "m", "Εξήντα ευρώ το ένα, στην πάνω κερκίδα, πίσω από το τέρμα. Δεν θα βλέπουμε πολύ καλά την άλλη άκρη, αλλά η ατμόσφαιρα είναι αυτό που μετράει.", "Sixty euros each, in the upper stand, behind the goal. We won't see the other end very well, but the atmosphere is what counts."),
  L("Άρης", "m", "Στο σπίτι θα το βλέπαμε σε μεγάλη οθόνη, με επαναλήψεις, ζεστοί, και χωρίς να περιμένουμε δύο ώρες στην ουρά για να βγούμε. Θυμάσαι πέρσι που φτάσαμε σπίτι στις δύο τα ξημερώματα;", "At home we'd watch it on a big screen, with replays, warm, and without waiting two hours in the queue to get out. Remember last year when we got home at two in the morning?"),
  L("Γιάννης", "m", "Θυμάμαι, αλλά θυμάμαι και το γκολ στο τελευταίο λεπτό, που πανηγυρίζαμε με αγνώστους. Αυτό δεν το ζεις στον καναπέ.", "I remember, but I also remember the goal in the last minute, when we celebrated with strangers. You don't experience that on the sofa."),
  L("Άρης", "m", "Καλά, με έπεισες. Αλλά πάμε με το μετρό, όχι με αυτοκίνητο. Και τα σουβλάκια μετά τα κερνάω εγώ.", "OK, you've convinced me. But we go by metro, not by car. And I'll buy the souvlaki afterwards."),
 ],
 "questions": [
  Q("Πού είναι οι θέσεις που βρήκε ο Γιάννης;", ["Δίπλα στον πάγκο των παικτών", "Στην πάνω κερκίδα, πίσω από το τέρμα", "Στην κεντρική κερκίδα", "Στο θεωρείο"], 1, "στην πάνω κερκίδα, πίσω από το τέρμα"),
  Q("Ποιο επιχείρημα χρησιμοποιεί ο Άρης για το σπίτι;", ["Ότι δεν του αρέσει το ποδόσφαιρο", "Ότι θα δουν τον αγώνα σε μεγάλη οθόνη και χωρίς ουρές", "Ότι ο τελικός θα ακυρωθεί", "Ότι έχει πολλή δουλειά"], 1, "Στο σπίτι θα το βλέπαμε σε μεγάλη οθόνη"),
  Q("Τι προτείνει ο Άρης στο τέλος;", ["Να πάνε με το αυτοκίνητο", "Να μείνουν στο σπίτι", "Να πάνε με το μετρό", "Να πουλήσουν τα εισιτήρια"], 2, "πάμε με το μετρό, όχι με αυτοκίνητο"),
 ],
 "gloss": {"γήπεδο": "γήπεδο — stadium", "τελικό": "τελικός — final", "κυπέλλου": "κύπελλο — cup (competition)", "κερκίδα": "κερκίδα — stand", "τέρμα": "τέρμα — goal", "ατμόσφαιρα": "ατμόσφαιρα — atmosphere", "επαναλήψεις": "επανάληψη — replay", "ξημερώματα": "ξημερώματα — early hours", "πανηγυρίζαμε": "πανηγυρίζω — to celebrate", "αγνώστους": "άγνωστος — stranger", "έπεισες": "πείθω — to convince", "κερνάω": "κερνάω — to treat, buy for"},
})

ITEMS.append({
 "id": "l172-dia-frontistirio-i-idiaitera", "title": "Φροντιστήριο ή ιδιαίτερα;", "title_en": "Cram school or private lessons?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο γονείς να συζητούν πώς θα προετοιμαστεί η κόρη τους για τις Πανελλαδικές εξετάσεις.",
 "script": [
  L("Μαρία", "f", "Η Δανάη μπαίνει στη Β΄ Λυκείου. Πρέπει να αποφασίσουμε: φροντιστήριο ή ιδιαίτερα;", "Danae is starting the second year of lyceum. We have to decide: cram school or private lessons?"),
  L("Πέτρος", "m", "Τα ιδιαίτερα είναι πιο ακριβά, αλλά ο καθηγητής ασχολείται μόνο μαζί της. Στα μαθηματικά, που δυσκολεύεται, αυτό μετράει πολύ.", "Private lessons are more expensive, but the teacher works only with her. In maths, where she struggles, that counts a lot."),
  L("Μαρία", "f", "Ναι, όμως στο φροντιστήριο έχει συμμαθητές. Η Δανάη δουλεύει καλύτερα όταν βλέπει τους άλλους να διαβάζουν. Και κάνουν διαγωνίσματα κάθε Σάββατο, σαν να είναι οι κανονικές εξετάσεις.", "Yes, but at the cram school she has classmates. Danae works better when she sees the others studying. And they do practice tests every Saturday, as if they were the real exams."),
  L("Πέτρος", "m", "Τότε γιατί να μην κάνουμε συνδυασμό; Φροντιστήριο για τα περισσότερα μαθήματα, και ιδιαίτερο μόνο για τα μαθηματικά.", "Then why don't we do a combination? Cram school for most subjects, and a private lesson only for maths."),
  L("Μαρία", "f", "Αυτό ακούγεται λογικό. Αλλά πριν κλείσουμε οτιδήποτε, ας ρωτήσουμε και την ίδια. Είναι δεκαέξι χρονών, όχι έξι.", "That sounds sensible. But before we book anything, let's ask her too. She's sixteen, not six."),
 ],
 "questions": [
  Q("Ποιο πλεονέκτημα των ιδιαίτερων αναφέρει ο Πέτρος;", ["Ότι είναι φθηνότερα", "Ότι ο καθηγητής ασχολείται μόνο με τη Δανάη", "Ότι γίνονται στο σχολείο", "Ότι κρατούν λιγότερες ώρες"], 1, "ο καθηγητής ασχολείται μόνο μαζί της"),
  Q("Γιατί η Μαρία προτιμά το φροντιστήριο;", ["Γιατί είναι κοντά στο σπίτι", "Γιατί η Δανάη δουλεύει καλύτερα όταν βλέπει τους άλλους να διαβάζουν", "Γιατί εκεί δουλεύει μια φίλη της", "Γιατί δεν έχει διαγωνίσματα"], 1, "Η Δανάη δουλεύει καλύτερα όταν βλέπει τους άλλους να διαβάζουν"),
  Q("Τι θέλει να κάνει η Μαρία πριν αποφασίσουν;", ["Να ρωτήσουν τη Δανάη", "Να μιλήσουν με τον διευθυντή", "Να συγκρίνουν τιμές", "Να περιμένουν τους βαθμούς"], 0, "ας ρωτήσουμε και την ίδια"),
 ],
 "gloss": {"προετοιμαστεί": "προετοιμάζομαι — to prepare", "Πανελλαδικές εξετάσεις": "Πανελλαδικές εξετάσεις — national university entrance exams", "φροντιστήριο": "φροντιστήριο — cram school, tutoring centre", "ιδιαίτερα": "ιδιαίτερα — private lessons", "Λυκείου": "Λύκειο — upper secondary school", "ασχολείται": "ασχολούμαι — to deal with, work with", "δυσκολεύεται": "δυσκολεύομαι — to struggle", "συμμαθητές": "συμμαθητής — classmate", "διαγωνίσματα": "διαγώνισμα — test", "συνδυασμό": "συνδυασμός — combination"},
})

ITEMS.append({
 "id": "l172-mon-to-prozymi-tis-giagias", "title": "Το προζύμι της γιαγιάς", "title_en": "Grandma's sourdough starter", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια νέα γυναίκα να μιλάει για το προζύμι που κληρονόμησε από τη γιαγιά της.",
 "script": [
  L("Γυναίκα", "f", "Η γιαγιά μου έφτιαχνε ψωμί κάθε Σάββατο, χωρίς μαγιά από το σούπερ μάρκετ. Είχε ένα βαζάκι με προζύμι στο ψυγείο, που το «τάιζε» με αλεύρι και νερό, σαν να ήταν κατοικίδιο. Έλεγε ότι το προζύμι αυτό το είχε φέρει η δική της μητέρα από τη Μικρά Ασία.", "My grandmother made bread every Saturday, without yeast from the supermarket. She had a little jar of starter in the fridge, which she 'fed' with flour and water, as if it were a pet. She said this starter had been brought by her own mother from Asia Minor."),
  L("Γυναίκα", "f", "Δεν ξέρω αν αυτό είναι αλήθεια. Ένα προζύμι δεν ζει εκατό χρόνια χωρίς φροντίδα, και κάθε φορά που το ταΐζεις αλλάζει λίγο. Αλλά μου αρέσει να το πιστεύω.", "I don't know if that's true. A starter doesn't live a hundred years without care, and every time you feed it, it changes a little. But I like to believe it."),
  L("Γυναίκα", "f", "Όταν η γιαγιά μπήκε στο νοσοκομείο, μου έδωσε το βαζάκι και μου είπε: «Μην το αφήσεις να πεθάνει». Τις πρώτες φορές το ψωμί μου έβγαινε σαν τούβλο. Τώρα, μετά από δύο χρόνια, βγαίνει σχεδόν σαν το δικό της.", "When grandma went into hospital, she gave me the jar and said: 'Don't let it die.' The first few times my bread came out like a brick. Now, after two years, it comes out almost like hers."),
  L("Γυναίκα", "f", "Έχω δώσει κομμάτια από το προζύμι σε φίλους στη Θεσσαλονίκη, στο Βερολίνο, ακόμα και στη Βοστόνη. Έτσι το προζύμι της γιαγιάς ταξιδεύει πάλι, όπως ταξίδεψε κάποτε η μητέρα της.", "I've given pieces of the starter to friends in Thessaloniki, in Berlin, even in Boston. So grandma's starter is travelling again, as her mother once travelled."),
 ],
 "questions": [
  Q("Πώς φρόντιζε η γιαγιά το προζύμι;", ["Το κρατούσε στον ήλιο", "Το τάιζε με αλεύρι και νερό", "Το ανακάτευε με μαγιά", "Το έβραζε κάθε εβδομάδα"], 1, "το «τάιζε» με αλεύρι και νερό"),
  Q("Τι πιστεύει η αφηγήτρια για την ιστορία από τη Μικρά Ασία;", ["Ότι είναι σίγουρα αληθινή", "Ότι την επινόησε η μητέρα της", "Δεν ξέρει αν είναι αλήθεια, αλλά της αρέσει να το πιστεύει", "Ότι είναι εντελώς ψέματα"], 2, "Δεν ξέρω αν αυτό είναι αλήθεια"),
  Q("Τι κάνει σήμερα με το προζύμι;", ["Δίνει κομμάτια σε φίλους σε διάφορες πόλεις", "Το πουλάει σε φούρνους", "Το έχει σε μουσείο", "Το χρησιμοποιεί μόνο τα Χριστούγεννα"], 0, "Έχω δώσει κομμάτια από το προζύμι σε φίλους"),
 ],
 "gloss": {"προζύμι": "προζύμι — sourdough starter", "κληρονόμησε": "κληρονομώ — to inherit", "μαγιά": "μαγιά — yeast", "βαζάκι": "βαζάκι — little jar", "τάιζε": "ταΐζω — to feed", "αλεύρι": "αλεύρι — flour", "κατοικίδιο": "κατοικίδιο — pet", "φροντίδα": "φροντίδα — care", "τούβλο": "τούβλο — brick"},
})

ITEMS.append({
 "id": "l172-vm-taverna-kratisi", "title": "Μήνυμα από την ταβέρνα για την κράτηση", "title_en": "A message from the taverna about the booking", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από μια ταβέρνα όπου έχετε κλείσει τραπέζι για μια οικογενειακή γιορτή.",
 "script": [
  L("Ιδιοκτήτης", "m", "Καλησπέρα σας, κύριε Αντωνίου, ο Μιχάλης από την ταβέρνα «Το Πλατάνι». Σας παίρνω για την κράτηση του Σαββάτου, για τα ογδοηκοστά γενέθλια της μητέρας σας.", "Good evening, Mr Antoniou, it's Michalis from the 'Plane Tree' taverna. I'm calling about Saturday's booking, for your mother's eightieth birthday."),
  L("Ιδιοκτήτης", "m", "Είχατε ζητήσει τραπέζι για δεκαοκτώ άτομα στην αυλή. Η πρόγνωση όμως λέει βροχή για το Σάββατο το βράδυ, οπότε σας προτείνω να σας βάλουμε στην πάνω σάλα, που έχει τζάκι. Εκεί θα είστε μόνοι σας, χωρίς άλλους πελάτες.", "You'd asked for a table for eighteen in the courtyard. But the forecast says rain for Saturday evening, so I suggest we put you in the upstairs room, which has a fireplace. There you'll be on your own, without other customers."),
  L("Ιδιοκτήτης", "m", "Για την τούρτα, μην ανησυχείτε· μπορείτε να τη φέρετε το πρωί και θα τη βάλουμε στο ψυγείο. Θα ήθελα μόνο να μου πείτε μέχρι την Πέμπτη αν θα έρθουν και τα δύο παιδιά που είχατε αναφέρει, για να ετοιμάσουμε ειδικό μενού. Καλή σας βραδιά.", "As for the cake, don't worry; you can bring it in the morning and we'll put it in the fridge. I'd just like you to tell me by Thursday whether the two children you mentioned will come, so we can prepare a special menu. Have a good evening."),
 ],
 "questions": [
  Q("Γιατί προτείνει ο ιδιοκτήτης να αλλάξουν χώρο;", ["Γιατί η αυλή είναι πολύ μικρή", "Γιατί η πρόγνωση λέει βροχή", "Γιατί η αυλή έχει κλείσει για επισκευή", "Γιατί υπάρχει άλλη μεγάλη κράτηση"], 1, "Η πρόγνωση όμως λέει βροχή για το Σάββατο το βράδυ"),
  Q("Τι θα γίνει με την τούρτα;", ["Θα τη φτιάξει η ταβέρνα", "Θα την παραγγείλουν από ζαχαροπλαστείο", "Μπορούν να τη φέρουν το πρωί και θα μπει στο ψυγείο", "Δεν επιτρέπεται να φέρουν δική τους"], 2, "μπορείτε να τη φέρετε το πρωί και θα τη βάλουμε στο ψυγείο"),
  Q("Τι πρέπει να του πει ο κύριος Αντωνίου μέχρι την Πέμπτη;", ["Αν θα έρθουν τα δύο παιδιά", "Πόσα κεριά θέλει στην τούρτα", "Τι κρασί προτιμά", "Τι ώρα θα φτάσουν"], 0, "αν θα έρθουν και τα δύο παιδιά που είχατε αναφέρει"),
 ],
 "gloss": {"ταβέρνα": "ταβέρνα — taverna", "κράτηση": "κράτηση — booking", "ογδοηκοστά": "ογδοηκοστός — eightieth", "αυλή": "αυλή — courtyard", "πρόγνωση": "πρόγνωση — (weather) forecast", "σάλα": "σάλα — hall, room", "τζάκι": "τζάκι — fireplace", "τούρτα": "τούρτα — cake", "αναφέρει": "αναφέρω — to mention", "μενού": "μενού — menu"},
})

ITEMS.append({
 "id": "l172-vm-syllogos-goneon-avli", "title": "Μήνυμα από τον σύλλογο γονέων για την αυλή του σχολείου", "title_en": "A message from the parents' association about the school yard", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από την πρόεδρο του συλλόγου γονέων του σχολείου του παιδιού σας.",
 "script": [
  L("Πρόεδρος", "f", "Καλημέρα, είμαι η Κατερίνα, η πρόεδρος του συλλόγου γονέων. Σας τηλεφωνώ επειδή είχατε γράψει ότι μπορείτε να βοηθήσετε στην ανακαίνιση της αυλής. Τελικά το ξεκινάμε την Κυριακή στις εννιά το πρωί.", "Good morning, it's Katerina, the president of the parents' association. I'm calling because you'd written that you could help with renovating the yard. We're finally starting on Sunday at nine in the morning."),
  L("Πρόεδρος", "f", "Το πρόγραμμα είναι να βάψουμε τα παγκάκια, να φυτέψουμε δέκα δέντρα που μας χάρισε ο δήμος και να ζωγραφίσουμε στο τσιμέντο κουτσό και ένα μεγάλο σκάκι. Τα χρώματα και τα πινέλα τα έχουμε· φέρτε μόνο γάντια και ρούχα που δεν σας πειράζει να λερωθούν.", "The plan is to paint the benches, plant ten trees the municipality gave us, and paint hopscotch and a big chessboard on the concrete. We have the paints and brushes; just bring gloves and clothes you don't mind getting dirty."),
  L("Πρόεδρος", "f", "Αν έχετε τσάπα ή φτυάρι, θα ήταν πολύ χρήσιμο για τα δέντρα. Τα παιδιά είναι ευπρόσδεκτα, αλλά όσα είναι κάτω από οχτώ χρονών θα ζωγραφίζουν μόνο σε χαρτί, μακριά από τα εργαλεία. Το μεσημέρι θα φάμε όλοι μαζί πίτες που θα φέρουν κάποιες μαμάδες.", "If you have a hoe or a spade, it would be very useful for the trees. Children are welcome, but those under eight will only draw on paper, away from the tools. At midday we'll all eat together pies that some mums will bring."),
 ],
 "questions": [
  Q("Τι πρέπει να φέρουν οι γονείς οπωσδήποτε;", ["Χρώματα και πινέλα", "Γάντια και ρούχα που μπορούν να λερωθούν", "Δέντρα", "Φαγητό για όλους"], 1, "φέρτε μόνο γάντια και ρούχα που δεν σας πειράζει να λερωθούν"),
  Q("Για ποια δουλειά θα ήταν χρήσιμη μια τσάπα ή ένα φτυάρι;", ["Για τα παγκάκια", "Για το σκάκι", "Για τα δέντρα", "Για το κουτσό"], 2, "θα ήταν πολύ χρήσιμο για τα δέντρα"),
  Q("Τι θα κάνουν τα παιδιά κάτω από οχτώ χρονών;", ["Θα ζωγραφίζουν μόνο σε χαρτί", "Θα μείνουν στο σπίτι", "Θα φυτεύουν λουλούδια", "Θα βάφουν τα παγκάκια"], 0, "θα ζωγραφίζουν μόνο σε χαρτί"),
 ],
 "gloss": {"συλλόγου γονέων": "σύλλογος γονέων — parents' association", "πρόεδρος": "πρόεδρος — president, chair", "ανακαίνιση": "ανακαίνιση — renovation", "παγκάκια": "παγκάκι — bench", "φυτέψουμε": "φυτεύω — to plant", "τσιμέντο": "τσιμέντο — concrete", "κουτσό": "κουτσό — hopscotch", "πινέλα": "πινέλο — paintbrush", "λερωθούν": "λερώνομαι — to get dirty", "τσάπα": "τσάπα — hoe", "φτυάρι": "φτυάρι — spade", "ευπρόσδεκτα": "ευπρόσδεκτος — welcome"},
})

ITEMS.append({
 "id": "l172-c1-giati-rochalizoume", "title": "Γιατί ροχαλίζουμε", "title_en": "Why we snore", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε ραδιοφωνική εκπομπή υγείας με μια γιατρό που ειδικεύεται στις διαταραχές του ύπνου.",
 "script": [
  L("Παρουσιαστής", "m", "Τι ακριβώς συμβαίνει όταν ροχαλίζουμε;", "What exactly happens when we snore?"),
  L("Γιατρός", "f", "Όταν κοιμόμαστε, οι μύες του λαιμού χαλαρώνουν και ο αεραγωγός στενεύει. Ο αέρας που περνά με δυσκολία κάνει τους μαλακούς ιστούς, κυρίως τη μαλθακή υπερώα και τη σταφυλή, να πάλλονται. Αυτός ο κραδασμός είναι ο ήχος που ακούμε, και που συχνά κρατάει ξύπνιο τον διπλανό μας περισσότερο από εμάς.", "When we sleep, the throat muscles relax and the airway narrows. The air that passes with difficulty makes the soft tissues, mainly the soft palate and the uvula, vibrate. That vibration is the sound we hear, and it often keeps the person next to us awake more than ourselves."),
  L("Παρουσιαστής", "m", "Γιατί κάποιοι ροχαλίζουν και άλλοι όχι;", "Why do some people snore and others don't?"),
  L("Γιατρός", "f", "Παίζουν ρόλο η ανατομία, η ηλικία και ο τρόπος ζωής. Το ροχαλητό είναι συχνότερο στους άντρες και αυξάνεται με τα χρόνια, καθώς οι ιστοί χάνουν την ελαστικότητά τους. Το υπερβολικό βάρος, το αλκοόλ πριν από τον ύπνο και ο ύπνος ανάσκελα το επιδεινώνουν, γιατί όλα στενεύουν ακόμη περισσότερο τον αεραγωγό. Γι' αυτό μερικές φορές αρκεί να κοιμηθεί κανείς στο πλάι.", "Anatomy, age and lifestyle play a role. Snoring is more common in men and increases with age, as the tissues lose their elasticity. Excess weight, alcohol before bed and sleeping on one's back make it worse, because they all narrow the airway even more. That's why sometimes it's enough to sleep on one's side."),
  L("Παρουσιαστής", "m", "Είναι επικίνδυνο;", "Is it dangerous?"),
  L("Γιατρός", "f", "Το απλό ροχαλητό συνήθως δεν είναι. Πρέπει όμως να μας ανησυχήσει όταν συνοδεύεται από παύσεις στην αναπνοή, που ακολουθούνται από ένα απότομο ρουθούνισμα. Αυτό μπορεί να σημαίνει άπνοια ύπνου, μια κατάσταση που κουράζει την καρδιά και προκαλεί έντονη υπνηλία τη μέρα. Σε αυτή την περίπτωση, καλό είναι να γίνει μελέτη ύπνου.", "Simple snoring usually isn't. But it should worry us when it is accompanied by pauses in breathing, followed by a sudden snort. This can mean sleep apnoea, a condition that tires the heart and causes severe daytime sleepiness. In that case, it's good to have a sleep study."),
 ],
 "questions": [
  Q("Τι προκαλεί τον ήχο του ροχαλητού;", ["Η μύτη που είναι βουλωμένη", "Ο κραδασμός των μαλακών ιστών όταν ο αεραγωγός στενεύει", "Τα δόντια που τρίζουν", "Το στομάχι"], 1, "Αυτός ο κραδασμός είναι ο ήχος που ακούμε"),
  Q("Γιατί βοηθά μερικές φορές ο ύπνος στο πλάι;", ["Γιατί ο ύπνος ανάσκελα στενεύει περισσότερο τον αεραγωγό", "Γιατί ζεσταίνει τον λαιμό", "Γιατί μειώνει το βάρος", "Γιατί ο διπλανός δεν ακούει"], 0, "ο ύπνος ανάσκελα το επιδεινώνουν"),
  Q("Πότε πρέπει να μας ανησυχήσει το ροχαλητό;", ["Όταν είναι πολύ δυνατό", "Όταν το ακούνε οι γείτονες", "Όταν συνοδεύεται από παύσεις στην αναπνοή", "Όταν σταματάει το πρωί"], 2, "όταν συνοδεύεται από παύσεις στην αναπνοή"),
 ],
 "gloss": {"ροχαλίζουμε": "ροχαλίζω — to snore", "ειδικεύεται": "ειδικεύομαι — to specialise", "διαταραχές": "διαταραχή — disorder", "μύες": "μυς — muscle", "αεραγωγός": "αεραγωγός — airway", "ιστούς": "ιστός — tissue", "μαλθακή υπερώα": "μαλθακή υπερώα — soft palate", "σταφυλή": "σταφυλή — uvula", "πάλλονται": "πάλλομαι — to vibrate", "κραδασμός": "κραδασμός — vibration", "ελαστικότητά": "ελαστικότητα — elasticity", "ανάσκελα": "ανάσκελα — on one's back", "επιδεινώνουν": "επιδεινώνω — to worsen", "παύσεις": "παύση — pause", "ρουθούνισμα": "ρουθούνισμα — snort", "άπνοια ύπνου": "άπνοια ύπνου — sleep apnoea", "υπνηλία": "υπνηλία — drowsiness"},
})

ITEMS.append({
 "id": "l172-c1-poulia-magnitiko-pedio", "title": "Πώς βρίσκουν τον δρόμο τους τα αποδημητικά πουλιά", "title_en": "How migratory birds find their way", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ορνιθολόγο σε μια διάλεξη για τον προσανατολισμό των αποδημητικών πουλιών.",
 "script": [
  L("Ορνιθολόγος", "f", "Ένα χελιδόνι που φωλιάζει σε ένα χωριό της Θεσσαλίας περνά τον χειμώνα στην Αφρική και την άνοιξη επιστρέφει, πολλές φορές στην ίδια ακριβώς φωλιά. Πώς το καταφέρνει, χωρίς χάρτη και χωρίς δορυφόρους; Η απάντηση είναι ότι χρησιμοποιεί όχι μία αλλά πολλές πυξίδες ταυτόχρονα.", "A swallow that nests in a village in Thessaly spends the winter in Africa and in spring returns, often to exactly the same nest. How does it manage, without a map and without satellites? The answer is that it uses not one but many compasses at once."),
  L("Ορνιθολόγος", "f", "Η πρώτη είναι ο ήλιος. Τα πουλιά διορθώνουν τη θέση του ανάλογα με την ώρα της ημέρας, χάρη σε ένα εσωτερικό ρολόι. Όσα ταξιδεύουν τη νύχτα προσανατολίζονται με τα αστέρια, και συγκεκριμένα με το σημείο γύρω από το οποίο φαίνεται να περιστρέφεται ο ουρανός, κοντά στον Πολικό Αστέρα.", "The first is the sun. Birds correct for its position according to the time of day, thanks to an internal clock. Those that travel at night orient themselves by the stars, and specifically by the point around which the sky seems to rotate, near the Pole Star."),
  L("Ορνιθολόγος", "f", "Η πιο αινιγματική πυξίδα είναι η μαγνητική. Ήδη από τη δεκαετία του '60, πειράματα με κοκκινολαίμηδες έδειξαν ότι τα πουλιά αντιλαμβάνονται το μαγνητικό πεδίο της Γης. Πώς ακριβώς το κάνουν, δεν το ξέρουμε ακόμη με βεβαιότητα. Η επικρατέστερη υπόθεση είναι ότι κάποιες πρωτεΐνες στα μάτια τους αντιδρούν στο πεδίο, οπότε ίσως τα πουλιά κυριολεκτικά «βλέπουν» τον Βορρά.", "The most puzzling compass is the magnetic one. As early as the 1960s, experiments with robins showed that birds perceive the Earth's magnetic field. Exactly how they do it, we still don't know for sure. The prevailing hypothesis is that certain proteins in their eyes react to the field, so perhaps birds literally 'see' north."),
  L("Ορνιθολόγος", "f", "Κοντά στον προορισμό, τα πουλιά στηρίζονται πια σε ορόσημα: ακτές, ποτάμια, βουνά, ακόμη και μυρωδιές. Η μετανάστευση, με λίγα λόγια, δεν είναι ένα θαύμα, αλλά ένα σύστημα με πολλές εφεδρείες, που λειτουργεί ακόμη κι όταν μία πυξίδα αποτύχει.", "Near the destination, birds rely on landmarks: coasts, rivers, mountains, even smells. Migration, in short, is not a miracle but a system with many backups, which works even when one compass fails."),
 ],
 "questions": [
  Q("Πώς χρησιμοποιούν τα πουλιά τον ήλιο για προσανατολισμό;", ["Πετούν πάντα προς τον ήλιο", "Διορθώνουν τη θέση του ανάλογα με την ώρα χάρη σε ένα εσωτερικό ρολόι", "Τον χρησιμοποιούν μόνο το καλοκαίρι", "Ακολουθούν τη σκιά τους"], 1, "Τα πουλιά διορθώνουν τη θέση του ανάλογα με την ώρα της ημέρας"),
  Q("Τι ισχύει για τη μαγνητική πυξίδα των πουλιών;", ["Ξέρουμε με βεβαιότητα πώς λειτουργεί", "Ανακαλύφθηκε πρόσφατα", "Δεν ξέρουμε ακόμη με βεβαιότητα πώς λειτουργεί", "Τη διαθέτουν μόνο τα χελιδόνια"], 2, "δεν το ξέρουμε ακόμη με βεβαιότητα"),
  Q("Πώς χαρακτηρίζει η ορνιθολόγος τη μετανάστευση στο τέλος;", ["Ένα σύστημα με πολλές εφεδρείες", "Ένα θαύμα που δεν εξηγείται", "Μια συνήθεια που χάνεται", "Ένα ταξίδι χωρίς κινδύνους"], 0, "ένα σύστημα με πολλές εφεδρείες"),
 ],
 "gloss": {"ορνιθολόγο": "ορνιθολόγος — ornithologist", "προσανατολισμό": "προσανατολισμός — orientation, navigation", "αποδημητικών": "αποδημητικός — migratory", "φωλιάζει": "φωλιάζω — to nest", "δορυφόρους": "δορυφόρος — satellite", "πυξίδες": "πυξίδα — compass", "προσανατολίζονται": "προσανατολίζομαι — to orient oneself", "περιστρέφεται": "περιστρέφομαι — to rotate", "Πολικό Αστέρα": "Πολικός Αστέρας — Pole Star", "αινιγματική": "αινιγματικός — puzzling", "κοκκινολαίμηδες": "κοκκινολαίμης — robin", "μαγνητικό πεδίο": "μαγνητικό πεδίο — magnetic field", "επικρατέστερη": "επικρατέστερος — prevailing", "πρωτεΐνες": "πρωτεΐνη — protein", "ορόσημα": "ορόσημο — landmark", "εφεδρείες": "εφεδρεία — backup, reserve"},
})

rnd = random.Random(172)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-172.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
