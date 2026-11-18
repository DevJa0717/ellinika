# Source for library/listening/listening-211.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l211.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l211-news-tileiatriki-nisia", "title": "Ο γιατρός στην οθόνη: τηλεϊατρική στα μικρά νησιά", "title_en": "The doctor on screen: telemedicine for small islands", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο ραδιόφωνο για ένα πρόγραμμα υγείας σε μικρά νησιά του Αιγαίου.",
 "script": [
  L("Εκφωνήτρια", "f", "Σε δεκαπέντε μικρά νησιά του Αιγαίου, όπου δεν υπάρχει μόνιμος ειδικός γιατρός, λειτουργούν από αυτή την εβδομάδα σταθμοί τηλεϊατρικής. Οι ασθενείς πηγαίνουν στο τοπικό ιατρείο και εξετάζονται μέσω βιντεοκλήσης από καρδιολόγους, παιδιάτρους και δερματολόγους ενός νοσοκομείου της Αθήνας.", "On fifteen small Aegean islands where there is no permanent specialist doctor, telemedicine stations have been operating since this week. Patients go to the local clinic and are examined by video call by cardiologists, paediatricians and dermatologists from an Athens hospital."),
  L("Εκφωνήτρια", "f", "Κάθε σταθμός διαθέτει ειδικές συσκευές, όπως ένα ψηφιακό στηθοσκόπιο και μια κάμερα υψηλής ανάλυσης για το δέρμα, ώστε ο γιατρός στην Αθήνα να ακούει την καρδιά και να βλέπει λεπτομέρειες. Τις συσκευές τις χειρίζεται ο γιατρός ή ο νοσηλευτής του νησιού, που έχουν εκπαιδευτεί γι' αυτό.", "Each station has special devices, such as a digital stethoscope and a high-resolution camera for the skin, so that the doctor in Athens can hear the heart and see details. The devices are operated by the island's doctor or nurse, who have been trained for this."),
  L("Εκφωνήτρια", "f", "Μέχρι σήμερα, πολλοί κάτοικοι έπρεπε να πάρουν το πλοίο και να μείνουν μία ή δύο νύχτες στην πρωτεύουσα για ένα απλό ραντεβού, κάτι ιδιαίτερα δύσκολο για τους ηλικιωμένους τον χειμώνα. Οι υπεύθυνοι τονίζουν πάντως ότι η τηλεϊατρική δεν αντικαθιστά τα επείγοντα περιστατικά, για τα οποία συνεχίζουν να υπάρχουν οι αεροδιακομιδές.", "Until now, many residents had to take the ferry and stay one or two nights in the capital for a simple appointment, something especially hard for the elderly in winter. Those in charge stress, however, that telemedicine does not replace emergencies, for which air ambulance transfers continue to exist."),
 ],
 "questions": [
  Q("Σε πόσα νησιά λειτουργούν οι σταθμοί τηλεϊατρικής;", ["Πέντε", "Δεκαπέντε", "Πενήντα", "Σε όλα τα νησιά του Αιγαίου"], 1, "Σε δεκαπέντε μικρά νησιά του Αιγαίου"),
  Q("Πώς εξετάζονται οι ασθενείς;", ["Στο σπίτι τους από νοσηλευτές", "Μέσω βιντεοκλήσης από γιατρούς ενός νοσοκομείου της Αθήνας", "Από γιατρούς που έρχονται με το πλοίο", "Με ένα ερωτηματολόγιο στο διαδίκτυο"], 1, "εξετάζονται μέσω βιντεοκλήσης από καρδιολόγους, παιδιάτρους και δερματολόγους ενός νοσοκομείου της Αθήνας"),
  Q("Ποιος χειρίζεται τις συσκευές στο νησί;", ["Ο ίδιος ο ασθενής", "Ένας τεχνικός από την Αθήνα", "Ο γιατρός ή ο νοσηλευτής του νησιού", "Ο δήμαρχος"], 2, "Τις συσκευές τις χειρίζεται ο γιατρός ή ο νοσηλευτής του νησιού"),
  Q("Τι τονίζουν οι υπεύθυνοι;", ["Ότι το πρόγραμμα θα σταματήσει τον χειμώνα", "Ότι η τηλεϊατρική δεν αντικαθιστά τα επείγοντα περιστατικά", "Ότι οι ασθενείς πρέπει να πληρώνουν", "Ότι θα κλείσουν τα τοπικά ιατρεία"], 1, "η τηλεϊατρική δεν αντικαθιστά τα επείγοντα περιστατικά"),
 ],
 "gloss": {"τηλεϊατρικής": "τηλεϊατρική — telemedicine", "μόνιμος": "μόνιμος — permanent", "στηθοσκόπιο": "στηθοσκόπιο — stethoscope", "ανάλυσης": "ανάλυση — resolution (of an image); analysis", "χειρίζεται": "χειρίζομαι — to operate, handle", "επείγοντα": "επείγων — urgent; τα επείγοντα = emergencies", "περιστατικά": "περιστατικό — (medical) case", "αεροδιακομιδές": "αεροδιακομιδή — air ambulance transfer"},
})
ITEMS.append({
 "id": "l211-dia-foniko-voitho-giagia", "title": "Γιαγιά, μίλα του σαν να είναι άνθρωπος", "title_en": "Teaching grandma to use a voice assistant", "type": "dialogue", "level": "B2",
 "context_el": "Ένας εγγονός δείχνει στη γιαγιά του πώς να χρησιμοποιεί ένα έξυπνο ηχείο με φωνητικό βοηθό που της χάρισε.",
 "script": [
  L("Νίκος", "m", "Γιαγιά, το συνδέσαμε. Τώρα δεν χρειάζεται να πατάς κουμπιά. Λες πρώτα τη λέξη ενεργοποίησης και μετά ό,τι θέλεις, π.χ. «Τι καιρό θα κάνει αύριο;».", "Grandma, we've connected it. Now you don't need to press buttons. You first say the wake word and then whatever you want, e.g. 'What will the weather be like tomorrow?'"),
  L("Γιαγιά", "f", "Και πώς ξέρει ότι μιλάω σ' αυτό και όχι στη γάτα; Κι αν μας ακούει όλη μέρα; Η κυρία Τούλα λέει ότι αυτά τα μηχανήματα τα ακούνε όλα.", "And how does it know I'm talking to it and not to the cat? And what if it's listening to us all day? Mrs Toula says these machines hear everything."),
  L("Νίκος", "m", "Περιμένει μόνο τη λέξη ενεργοποίησης. Όταν ακούει, ανάβει αυτό το μπλε φωτάκι. Κι αν δεν θέλεις να ακούει καθόλου, πατάς αυτό το κουμπί με το μικρόφωνο και κλείνει.", "It only waits for the wake word. When it's listening, this little blue light comes on. And if you don't want it listening at all, you press this button with the microphone and it switches off."),
  L("Γιαγιά", "f", "Καλά. Μπορεί να μου θυμίζει τα χάπια μου; Γιατί το μεσημεριανό το ξεχνάω συχνά.", "All right. Can it remind me about my pills? Because I often forget the midday one."),
  L("Νίκος", "m", "Φυσικά. Πες του «Θύμισέ μου κάθε μέρα στη μία να πάρω το χάπι». Και αν χρειαστείς κάτι, μπορείς να του πεις «Πάρε τηλέφωνο τον Νίκο» και θα με καλέσει.", "Of course. Tell it 'Remind me every day at one to take my pill'. And if you need something, you can tell it 'Call Nikos' and it will ring me."),
  L("Γιαγιά", "f", "Αυτό μου αρέσει. Να του ζητήσω και τραγούδια της Βέμπο;", "I like that. Can I ask it for songs by Vembo too?"),
  L("Νίκος", "m", "Ό,τι θέλεις. Μόνο να μιλάς καθαρά και όχι πολύ γρήγορα. Και μην του φωνάζεις, δεν είναι κουφό!", "Whatever you like. Just speak clearly and not too fast. And don't shout at it, it's not deaf!"),
 ],
 "questions": [
  Q("Τι πρέπει να πει πρώτα η γιαγιά για να χρησιμοποιήσει τη συσκευή;", ["Το όνομά της", "Τη λέξη ενεργοποίησης", "«Καλημέρα»", "Τον κωδικό του ασύρματου δικτύου"], 1, "Λες πρώτα τη λέξη ενεργοποίησης και μετά ό,τι θέλεις"),
  Q("Τι ανησυχεί τη γιαγιά;", ["Ότι η συσκευή είναι ακριβή", "Ότι θα την ενοχλεί τη νύχτα", "Ότι το μηχάνημα μπορεί να ακούει όλη μέρα", "Ότι θα φοβηθεί η γάτα"], 2, "Κι αν μας ακούει όλη μέρα;"),
  Q("Πώς μπορεί η γιαγιά να σταματήσει εντελώς το μικρόφωνο;", ["Βγάζοντας τη συσκευή από την πρίζα κάθε βράδυ", "Πατώντας το κουμπί με το μικρόφωνο", "Λέγοντας «σταμάτα»", "Δεν γίνεται"], 1, "πατάς αυτό το κουμπί με το μικρόφωνο και κλείνει"),
  Q("Για ποιο πρόβλημα θα βοηθήσει η συσκευή τη γιαγιά;", ["Ξεχνάει το μεσημεριανό χάπι της", "Δεν βλέπει καλά την τηλεόραση", "Χάνει τα κλειδιά της", "Δεν ξέρει να μαγειρεύει"], 0, "το μεσημεριανό το ξεχνάω συχνά"),
 ],
 "gloss": {"φωνητικό": "φωνητικός — voice (adj.); φωνητικός βοηθός = voice assistant", "ηχείο": "ηχείο — speaker", "ενεργοποίησης": "ενεργοποίηση — activation; λέξη ενεργοποίησης = wake word", "φωτάκι": "φωτάκι — little light", "Θύμισέ": "θυμίζω — to remind", "κουφό": "κουφός — deaf"},
})
ITEMS.append({
 "id": "l211-c1-mono-istoria-midenos", "title": "Ο αριθμός που άργησε χιλιάδες χρόνια: το μηδέν", "title_en": "The number that took millennia: a history of zero", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ομιλία για την ιστορία των μαθηματικών σε έναν κύκλο εκλαϊκευμένων διαλέξεων.",
 "script": [
  L("Ομιλήτρια", "f", "Μας φαίνεται αυτονόητο, κι όμως το μηδέν είναι μια από τις πιο καθυστερημένες ανακαλύψεις της ανθρωπότητας. Οι Βαβυλώνιοι, που είχαν ένα θεσιακό σύστημα αρίθμησης, χρειάστηκαν κάποια στιγμή ένα σημάδι για να δείξουν ότι μια θέση είναι κενή, αλλιώς ο αριθμός διαβαζόταν λάθος. Αυτό όμως ήταν ένα σύμβολο κράτησης θέσης, όχι ένας αριθμός με δική του αξία.", "It seems self-evident to us, and yet zero is one of humanity's most belated discoveries. The Babylonians, who had a positional number system, needed at some point a mark to show that a position was empty, otherwise the number was misread. But that was a placeholder, not a number with a value of its own."),
  L("Ομιλήτρια", "f", "Κάτι ανάλογο έκαναν και οι Έλληνες αστρονόμοι: στους πίνακες του Πτολεμαίου εμφανίζεται ένας μικρός κύκλος για τις κενές θέσεις. Οι Έλληνες μαθηματικοί, ωστόσο, δυσκολεύονταν να δεχτούν το «τίποτα» ως αριθμό· για πολλούς φιλοσόφους το κενό ήταν έννοια ύποπτη, σχεδόν αδιανόητη. Είναι χαρακτηριστικό ότι η ίδια η λέξη «μηδέν» προέρχεται από το «μηδέ έν», δηλαδή «ούτε ένα».", "Greek astronomers did something similar: in Ptolemy's tables a small circle appears for empty positions. Greek mathematicians, however, found it hard to accept 'nothing' as a number; for many philosophers the void was a suspect, almost unthinkable concept. Tellingly, the word 'μηδέν' itself comes from 'μηδέ έν', meaning 'not even one'."),
  L("Ομιλήτρια", "f", "Το αποφασιστικό βήμα έγινε στην Ινδία. Τον έβδομο αιώνα ο μαθηματικός Μπραχμαγκούπτα διατύπωσε κανόνες για το πώς προσθέτουμε, αφαιρούμε και πολλαπλασιάζουμε με το μηδέν, αντιμετωπίζοντάς το πλέον ως κανονικό αριθμό. Μέσω των Αράβων λογίων το σύστημα πέρασε στη Μεσόγειο, και το 1202 ο Φιμπονάτσι το παρουσίασε στο βιβλίο του για τη λογιστική και το εμπόριο.", "The decisive step came in India. In the seventh century the mathematician Brahmagupta formulated rules for adding, subtracting and multiplying with zero, now treating it as a proper number. Through Arab scholars the system reached the Mediterranean, and in 1202 Fibonacci presented it in his book on arithmetic for accounting and trade."),
  L("Ομιλήτρια", "f", "Η αποδοχή δεν ήταν άμεση. Αναφέρεται, για παράδειγμα, ότι στη Φλωρεντία του τέλους του δέκατου τρίτου αιώνα οι τραπεζίτες έπρεπε να γράφουν τα ποσά ολογράφως, επειδή τα νέα ψηφία θεωρούνταν εύκολο να πλαστογραφηθούν: ένα μηδέν μετατρέπεται εύκολα σε εννιά. Μόνο όταν φάνηκε πόσο πιο γρήγορα γίνονται οι πράξεις, το μηδέν κέρδισε οριστικά τη θέση του. Χωρίς αυτό, σήμερα δεν θα υπήρχε ούτε η άλγεβρα ούτε, φυσικά, οι υπολογιστές, που στηρίζονται σε ένα σύστημα από μηδενικά και άσσους.", "Acceptance was not immediate. It is reported, for example, that in late-thirteenth-century Florence bankers had to write sums out in words, because the new digits were considered easy to forge: a zero is easily turned into a nine. Only when it became clear how much faster calculations were did zero win its place for good. Without it there would be no algebra today, nor, of course, computers, which rest on a system of zeros and ones."),
 ],
 "questions": [
  Q("Τι ήταν το σημάδι των Βαβυλωνίων για τις κενές θέσεις;", ["Ένας αριθμός με δική του αξία", "Ένα σύμβολο κράτησης θέσης", "Ένα γράμμα του αλφαβήτου", "Ένα σημάδι για τους αρνητικούς αριθμούς"], 1, "Αυτό όμως ήταν ένα σύμβολο κράτησης θέσης, όχι ένας αριθμός με δική του αξία"),
  Q("Από πού προέρχεται η λέξη «μηδέν», σύμφωνα με την ομιλήτρια;", ["Από μια αραβική λέξη", "Από το όνομα ενός αστρονόμου", "Από το «μηδέ έν», δηλαδή «ούτε ένα»", "Από τη λατινική λέξη για τον κύκλο"], 2, "η ίδια η λέξη «μηδέν» προέρχεται από το «μηδέ έν», δηλαδή «ούτε ένα»"),
  Q("Ποια ήταν η συμβολή του Μπραχμαγκούπτα;", ["Επινόησε τα κλάσματα", "Έγραψε κανόνες για τις πράξεις με το μηδέν ως αριθμό", "Μετέφρασε τον Πτολεμαίο", "Έφερε το σύστημα στη Φλωρεντία"], 1, "διατύπωσε κανόνες για το πώς προσθέτουμε, αφαιρούμε και πολλαπλασιάζουμε με το μηδέν"),
  Q("Γιατί, σύμφωνα με την ομιλία, οι τραπεζίτες της Φλωρεντίας έπρεπε να γράφουν τα ποσά ολογράφως;", ["Επειδή δεν ήξεραν τα νέα ψηφία", "Επειδή τα νέα ψηφία πλαστογραφούνταν εύκολα", "Επειδή το απαιτούσε η Εκκλησία", "Επειδή τα ποσά ήταν πολύ μεγάλα"], 1, "τα νέα ψηφία θεωρούνταν εύκολο να πλαστογραφηθούν"),
 ],
 "gloss": {"αυτονόητο": "αυτονόητος — self-evident", "θεσιακό": "θεσιακός — positional", "κράτησης θέσης": "σύμβολο κράτησης θέσης — placeholder", "αδιανόητη": "αδιανόητος — unthinkable", "διατύπωσε": "διατυπώνω — to formulate", "λογίων": "λόγιος — scholar", "ολογράφως": "ολογράφως — (written) in words", "πλαστογραφηθούν": "πλαστογραφώ — to forge", "άσσους": "άσσος — ace; here, the digit one"},
})
ITEMS.append({
 "id": "l211-c1-int-iatrodikastiki-entomologia", "title": "Τι λένε οι μύγες στον ιατροδικαστή", "title_en": "What flies tell investigators: a forensic entomologist", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε επιστημονική εκπομπή με μια ερευνήτρια που ασχολείται με την ιατροδικαστική εντομολογία.",
 "script": [
  L("Δημοσιογράφος", "m", "Η δουλειά σας ακούγεται βγαλμένη από αστυνομική σειρά. Τι ακριβώς κάνει ένας ιατροδικαστικός εντομολόγος;", "Your job sounds like something out of a crime series. What exactly does a forensic entomologist do?"),
  L("Ερευνήτρια", "f", "Μελετάμε τα έντομα που βρίσκονται σε ένα πτώμα, για να βοηθήσουμε τις αρχές να εκτιμήσουν πόσος χρόνος έχει περάσει από τον θάνατο. Ορισμένες μύγες εντοπίζουν ένα νεκρό σώμα μέσα σε λίγα λεπτά ή ώρες και γεννούν εκεί τα αυγά τους. Οι προνύμφες αναπτύσσονται με έναν ρυθμό που είναι σχετικά προβλέψιμος, οπότε από το στάδιο ανάπτυξής τους μπορούμε να υπολογίσουμε αντίστροφα.", "We study the insects found on a body to help the authorities estimate how much time has passed since death. Certain flies locate a dead body within minutes or hours and lay their eggs there. The larvae develop at a rate that is relatively predictable, so from their stage of development we can calculate backwards."),
  L("Δημοσιογράφος", "m", "Δηλαδή αρκεί να μετρήσετε το μήκος μιας προνύμφης;", "So it's enough to measure the length of a larva?"),
  L("Ερευνήτρια", "f", "Μακάρι να ήταν τόσο απλό. Ο ρυθμός ανάπτυξης εξαρτάται πάρα πολύ από τη θερμοκρασία: με ζέστη όλα επιταχύνονται, με κρύο σχεδόν σταματούν. Γι' αυτό συλλέγουμε δεδομένα από τους πλησιέστερους μετεωρολογικούς σταθμούς και συχνά αφήνουμε δικούς μας καταγραφείς στο σημείο για μερικές μέρες. Παίζει ρόλο ακόμα και αν το σώμα ήταν στη σκιά ή τυλιγμένο σε κάτι.", "If only it were that simple. The rate of development depends enormously on temperature: in heat everything speeds up, in cold it almost stops. That's why we collect data from the nearest weather stations and often leave our own loggers at the scene for a few days. It even matters whether the body was in the shade or wrapped in something."),
  L("Δημοσιογράφος", "m", "Πόσο παλιά είναι αυτή η μέθοδος;", "How old is this method?"),
  L("Ερευνήτρια", "f", "Η πρώτη περιγραφή που συνήθως αναφέρεται βρίσκεται σε ένα κινέζικο εγχειρίδιο του δέκατου τρίτου αιώνα: σε μια υπόθεση φόνου με δρεπάνι, ο ανακριτής ζήτησε από τους χωρικούς να αφήσουν κάτω τα δρεπάνια τους, και οι μύγες μαζεύτηκαν σε ένα μόνο, όπου υπήρχαν αόρατα ίχνη αίματος. Ως συστηματική επιστήμη, όμως, η ιατροδικαστική εντομολογία αναπτύχθηκε κυρίως τον εικοστό αιώνα. Και σας διαβεβαιώνω ότι μετά από χρόνια δουλειάς δεν αηδιάζω πια· αυτό που με συναρπάζει είναι ότι ένα τόσο μικρό πλάσμα μπορεί να είναι ο πιο αξιόπιστος μάρτυρας.", "The first description usually cited is in a thirteenth-century Chinese handbook: in a murder case involving a sickle, the investigator asked the villagers to lay down their sickles, and the flies gathered on just one, where there were invisible traces of blood. As a systematic science, though, forensic entomology developed mainly in the twentieth century. And I assure you that after years of work I'm no longer disgusted; what fascinates me is that such a tiny creature can be the most reliable witness."),
 ],
 "questions": [
  Q("Σε τι βοηθά κυρίως η ιατροδικαστική εντομολογία;", ["Στην αναγνώριση του θύματος", "Στην εκτίμηση του χρόνου που πέρασε από τον θάνατο", "Στην ανεύρεση του όπλου", "Στη μελέτη των ασθενειών"], 1, "να εκτιμήσουν πόσος χρόνος έχει περάσει από τον θάνατο"),
  Q("Ποιος παράγοντας επηρεάζει περισσότερο τον ρυθμό ανάπτυξης των προνυμφών;", ["Το φως", "Η θερμοκρασία", "Η υγρασία του εδάφους", "Το είδος του φαγητού που έτρωγε ο νεκρός"], 1, "Ο ρυθμός ανάπτυξης εξαρτάται πάρα πολύ από τη θερμοκρασία"),
  Q("Γιατί η ερευνήτρια αφήνει καταγραφείς στο σημείο;", ["Για να κρατήσει μακριά τα ζώα", "Για να καταγράψει τις θερμοκρασίες εκεί", "Για να βιντεοσκοπήσει τις μύγες", "Για να το ζητήσει η αστυνομία"], 1, "συλλέγουμε δεδομένα από τους πλησιέστερους μετεωρολογικούς σταθμούς και συχνά αφήνουμε δικούς μας καταγραφείς"),
  Q("Τι έδειξαν οι μύγες στην υπόθεση από το κινέζικο εγχειρίδιο;", ["Πού ήταν κρυμμένο το πτώμα", "Ποιο δρεπάνι είχε ίχνη αίματος", "Ποια ώρα έγινε ο φόνος", "Ότι δεν επρόκειτο για φόνο"], 1, "οι μύγες μαζεύτηκαν σε ένα μόνο, όπου υπήρχαν αόρατα ίχνη αίματος"),
 ],
 "gloss": {"ιατροδικαστική": "ιατροδικαστικός — forensic (medical)", "εντομολογία": "εντομολογία — entomology", "πτώμα": "πτώμα — corpse, body", "προνύμφες": "προνύμφη — larva", "αντίστροφα": "αντίστροφα — backwards, in reverse", "επιταχύνονται": "επιταχύνομαι — to speed up", "καταγραφείς": "καταγραφέας — (data) logger", "δρεπάνι": "δρεπάνι — sickle", "ανακριτής": "ανακριτής — investigating magistrate, investigator", "αηδιάζω": "αηδιάζω — to be disgusted"},
})
rnd = random.Random(211)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-211.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
