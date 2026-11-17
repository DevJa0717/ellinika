# Source for library/listening/listening-139.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l139.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l139-dia-chrysoi-gamoi", "title": "Πενήντα χρόνια μαζί", "title_en": "Fifty years together", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο αδέρφια να συζητούν στο τηλέφωνο.",
 "script": [
  L("Άννα", "f", "Τον Ιούνιο κλείνουν πενήντα χρόνια γάμου η μαμά και ο μπαμπάς. Λέω να τους κάνουμε μια γιορτή έκπληξη, με όλους τους συγγενείς και τους φίλους τους.", "In June Mum and Dad will have been married for fifty years. I say we throw them a surprise party, with all their relatives and friends."),
  L("Πέτρος", "m", "Έκπληξη; Ξέρεις τον μπαμπά. Αν δει ξαφνικά εκατό ανθρώπους, θα θέλει να φύγει. Και η μαμά θα στενοχωρηθεί που δεν φόρεσε το καλό της φόρεμα.", "A surprise? You know Dad. If he suddenly sees a hundred people, he'll want to leave. And Mum will be upset that she didn't wear her good dress."),
  L("Άννα", "f", "Δίκιο έχεις. Τότε να τους το πούμε από πριν, αλλά να κρατήσουμε κάτι κρυφό. Σκέφτομαι να ζητήσω από τον καθένα να φέρει μια παλιά φωτογραφία μαζί τους και να φτιάξουμε ένα άλμπουμ.", "You're right. Then let's tell them in advance, but keep something secret. I'm thinking of asking everyone to bring an old photo with them and making an album."),
  L("Πέτρος", "m", "Αυτό είναι τέλειο. Κι εγώ θα βρω τον ίδιο μουσικό που έπαιζε βιολί στον γάμο τους. Η θεία Λένα λέει ότι ζει ακόμα στο χωριό και παίζει στα πανηγύρια.", "That's perfect. And I'll find the same musician who played the violin at their wedding. Aunt Lena says he still lives in the village and plays at the festivals."),
 ],
 "questions": [
  Q("Τι προτείνει αρχικά η Άννα;", ["Ένα ταξίδι για τους γονείς", "Μια γιορτή έκπληξη με συγγενείς και φίλους", "Ένα δείπνο μόνο για την οικογένεια", "Να μην κάνουν τίποτα"], 1, "Λέω να τους κάνουμε μια γιορτή έκπληξη"),
  Q("Γιατί διαφωνεί ο Πέτρος με την έκπληξη;", ["Γιατί κοστίζει πολύ", "Γιατί ο μπαμπάς θα θέλει να φύγει και η μαμά θα στενοχωρηθεί", "Γιατί δεν έχει χρόνο", "Γιατί οι γονείς θα είναι σε ταξίδι"], 1, "Αν δει ξαφνικά εκατό ανθρώπους, θα θέλει να φύγει"),
  Q("Τι θα κρατήσουν κρυφό;", ["Το μέρος της γιορτής", "Την ημερομηνία", "Ένα άλμπουμ με παλιές φωτογραφίες και τον μουσικό του γάμου", "Τη λίστα των καλεσμένων"], 2, "να ζητήσω από τον καθένα να φέρει μια παλιά φωτογραφία μαζί τους και να φτιάξουμε ένα άλμπουμ"),
 ],
 "gloss": {"γάμου": "γάμος — marriage, wedding", "έκπληξη": "έκπληξη — surprise", "συγγενείς": "συγγενής — relative", "στενοχωρηθεί": "στενοχωριέμαι — to get upset", "Δίκιο έχεις": "έχω δίκιο — to be right", "κρυφό": "κρυφός — secret", "άλμπουμ": "άλμπουμ — album", "βιολί": "βιολί — violin", "πανηγύρια": "πανηγύρι — village festival"}
})

ITEMS.append({
 "id": "l139-vm-katataktirio", "title": "Το τεστ κατάταξης", "title_en": "The placement test", "type": "voicemail", "level": "B2",
 "context_el": "Γραφτήκατε σε μαθήματα ιταλικών. Ακούτε ένα μήνυμα από τη σχολή στον τηλεφωνητή σας.",
 "script": [
  L("Γραμματέας", "f", "Καλημέρα σας, από τη σχολή ξένων γλωσσών «Πολύγλωσσος» σας τηλεφωνώ. Είδαμε στην αίτησή σας ότι έχετε κάνει ιταλικά στο παρελθόν, οπότε πριν από την έναρξη των μαθημάτων θα χρειαστεί να γράψετε ένα σύντομο τεστ κατάταξης.", "Good morning, I'm calling from the 'Polyglossos' foreign-language school. We saw in your application that you've studied Italian before, so before classes start you'll need to take a short placement test."),
  L("Γραμματέας", "f", "Το τεστ γίνεται online και διαρκεί περίπου σαράντα λεπτά. Μετά ακολουθεί μια σύντομη συζήτηση με έναν καθηγητή, δέκα λεπτά, για να δούμε και πώς μιλάτε. Μην ανησυχείτε, δεν παίρνετε βαθμό· απλώς σας βάζουμε στο σωστό τμήμα.", "The test is online and takes about forty minutes. After that there's a short conversation with a teacher, ten minutes, so that we can also see how you speak. Don't worry, you don't get a mark; we just put you in the right group."),
  L("Γραμματέας", "f", "Θα σας στείλουμε τον σύνδεσμο με email σήμερα το απόγευμα. Παρακαλούμε να το έχετε ολοκληρώσει μέχρι την Παρασκευή, γιατί τα τμήματα ξεκινούν τη Δευτέρα.", "We'll send you the link by email this afternoon. Please have it completed by Friday, because the groups start on Monday."),
 ],
 "questions": [
  Q("Γιατί πρέπει να γράψετε τεστ κατάταξης;", ["Γιατί είναι υποχρεωτικό για όλους", "Γιατί έχετε κάνει ιταλικά στο παρελθόν", "Γιατί θέλετε δίπλωμα", "Γιατί αργήσατε να γραφτείτε"], 1, "έχετε κάνει ιταλικά στο παρελθόν"),
  Q("Ποιος είναι ο σκοπός του τεστ;", ["Να πάρετε βαθμό", "Να πάρετε υποτροφία", "Να μπείτε στο σωστό τμήμα", "Να γλιτώσετε τα δίδακτρα"], 2, "απλώς σας βάζουμε στο σωστό τμήμα"),
  Q("Μέχρι πότε πρέπει να ολοκληρώσετε το τεστ;", ["Μέχρι την Παρασκευή", "Μέχρι τη Δευτέρα", "Μέχρι σήμερα το απόγευμα", "Μέχρι το τέλος του μήνα"], 0, "μέχρι την Παρασκευή"),
 ],
 "gloss": {"αίτησή": "αίτηση — application", "έναρξη": "έναρξη — start", "κατάταξης": "κατάταξη — placement, ranking", "διαρκεί": "διαρκώ — to last", "ανησυχείτε": "ανησυχώ — to worry", "βαθμό": "βαθμός — mark, grade", "τμήμα": "τμήμα — class, group", "σύνδεσμο": "σύνδεσμος — link", "ολοκληρώσει": "ολοκληρώνω — to complete"}
})

ITEMS.append({
 "id": "l139-ann-pyli", "title": "Αλλαγή πύλης", "title_en": "Gate change", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε στο αεροδρόμιο και ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνήτρια", "f", "Παρακαλούνται οι επιβάτες της πτήσης προς Χανιά, που ήταν προγραμματισμένη για τις έξι και σαράντα, να προσέξουν: η πτήση θα αναχωρήσει με καθυστέρηση σαράντα πέντε λεπτών, λόγω της καθυστερημένης άφιξης του αεροσκάφους από τη Θεσσαλονίκη.", "Passengers on the flight to Chania, scheduled for six forty, are asked to note: the flight will depart forty-five minutes late, owing to the late arrival of the aircraft from Thessaloniki."),
  L("Εκφωνήτρια", "f", "Επίσης, η επιβίβαση δεν θα γίνει από την πύλη δώδεκα, αλλά από την πύλη είκοσι τρία, στο τέλος του δεξιού διαδρόμου. Η απόσταση είναι περίπου δέκα λεπτά με τα πόδια.", "Also, boarding will not take place from gate twelve, but from gate twenty-three, at the end of the right-hand corridor. The distance is about ten minutes on foot."),
  L("Εκφωνήτρια", "f", "Οι επιβάτες με μικρά παιδιά ή με μειωμένη κινητικότητα θα επιβιβαστούν πρώτοι. Σας ευχαριστούμε για την υπομονή σας και ζητούμε συγγνώμη για την ταλαιπωρία.", "Passengers with small children or reduced mobility will board first. We thank you for your patience and apologise for the inconvenience."),
 ],
 "questions": [
  Q("Γιατί καθυστερεί η πτήση;", ["Λόγω κακοκαιρίας στα Χανιά", "Λόγω της καθυστερημένης άφιξης του αεροσκάφους από τη Θεσσαλονίκη", "Λόγω απεργίας", "Λόγω τεχνικού προβλήματος"], 1, "λόγω της καθυστερημένης άφιξης του αεροσκάφους από τη Θεσσαλονίκη"),
  Q("Από ποια πύλη θα γίνει η επιβίβαση;", ["Από την πύλη δώδεκα", "Από την πύλη έξι", "Από την πύλη είκοσι τρία", "Από την πύλη σαράντα πέντε"], 2, "από την πύλη είκοσι τρία, στο τέλος του δεξιού διαδρόμου"),
  Q("Ποιοι θα επιβιβαστούν πρώτοι;", ["Οι επιβάτες με μικρά παιδιά ή με μειωμένη κινητικότητα", "Οι επιβάτες της business θέσης", "Όσοι έχουν μόνο χειραποσκευή", "Οι επιβάτες με κάρτα μέλους"], 0, "Οι επιβάτες με μικρά παιδιά ή με μειωμένη κινητικότητα θα επιβιβαστούν πρώτοι"),
 ],
 "gloss": {"μεγάφωνα": "μεγάφωνο — loudspeaker", "πτήσης": "πτήση — flight", "αναχωρήσει": "αναχωρώ — to depart", "άφιξης": "άφιξη — arrival", "αεροσκάφους": "αεροσκάφος — aircraft", "επιβίβαση": "επιβίβαση — boarding", "πύλη": "πύλη — gate", "διαδρόμου": "διάδρομος — corridor", "μειωμένη κινητικότητα": "μειωμένη κινητικότητα — reduced mobility", "ταλαιπωρία": "ταλαιπωρία — inconvenience"}
})

ITEMS.append({
 "id": "l139-vm-chalia", "title": "Τα χαλιά είναι έτοιμα", "title_en": "The rugs are ready", "type": "voicemail", "level": "B2",
 "context_el": "Τον Μάιο δώσατε τα χαλιά σας για πλύσιμο. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλησπέρα σας, από το ταπητοκαθαριστήριο «Λευκό» σας παίρνω. Τα τρία χαλιά σας, που τα είχατε αφήσει τον Μάιο για πλύσιμο και φύλαξη, είναι έτοιμα να σας τα φέρουμε.", "Good evening, I'm calling from the 'Lefko' rug cleaners. Your three rugs, which you left in May for washing and storage, are ready for us to bring to you."),
  L("Υπάλληλος", "m", "Το μεγάλο χαλί του σαλονιού είχε έναν λεκέ από κρασί, που δυστυχώς δεν έφυγε εντελώς, παρόλο που το πλύναμε δύο φορές. Δεν σας χρεώσαμε το δεύτερο πλύσιμο.", "The large living-room rug had a wine stain, which unfortunately didn't come out completely, even though we washed it twice. We didn't charge you for the second wash."),
  L("Υπάλληλος", "m", "Η παράδοση στο σπίτι είναι δωρεάν. Μπορούμε να έρθουμε αυτή την Πέμπτη ή το Σάββατο το πρωί. Πείτε μας ποια μέρα σας βολεύει, και αν θέλετε, ο οδηγός μας μπορεί να τα στρώσει κιόλας.", "Home delivery is free. We can come this Thursday or on Saturday morning. Tell us which day suits you, and if you like, our driver can also lay them out."),
 ],
 "questions": [
  Q("Πόσα χαλιά είχατε δώσει;", ["Ένα", "Δύο", "Τρία", "Τέσσερα"], 2, "Τα τρία χαλιά σας"),
  Q("Τι πρόβλημα υπήρξε με το χαλί του σαλονιού;", ["Χάθηκε", "Ένας λεκές από κρασί δεν έφυγε εντελώς", "Άλλαξε χρώμα", "Μίκρυνε"], 1, "είχε έναν λεκέ από κρασί, που δυστυχώς δεν έφυγε εντελώς"),
  Q("Τι μπορεί να κάνει ο οδηγός, αν θέλετε;", ["Να τα στρώσει", "Να τα φυλάξει άλλον έναν χρόνο", "Να σας φέρει καινούργιο χαλί", "Να πάρει και τις κουρτίνες"], 0, "ο οδηγός μας μπορεί να τα στρώσει κιόλας"),
 ],
 "gloss": {"χαλιά": "χαλί — rug, carpet", "ταπητοκαθαριστήριο": "ταπητοκαθαριστήριο — rug cleaner's", "πλύσιμο": "πλύσιμο — washing", "φύλαξη": "φύλαξη — storage", "λεκέ": "λεκές — stain", "εντελώς": "εντελώς — completely", "χρεώσαμε": "χρεώνω — to charge", "παράδοση": "παράδοση — delivery", "βολεύει": "βολεύει — it suits", "στρώσει": "στρώνω — to lay (a rug)"}
})

ITEMS.append({
 "id": "l139-int-stavrolexa", "title": "Ο άνθρωπος πίσω από τα σταυρόλεξα", "title_en": "The man behind the crosswords", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από μια ραδιοφωνική εκπομπή για τις λέξεις.",
 "script": [
  L("Δημοσιογράφος", "f", "Φτιάχνετε σταυρόλεξα για μια εφημερίδα εδώ και είκοσι πέντε χρόνια. Πώς ξεκινάτε ένα καινούργιο;", "You've been making crosswords for a newspaper for twenty-five years. How do you start a new one?"),
  L("Σταυρολεξάς", "m", "Πρώτα διαλέγω τις μεγάλες λέξεις, που διασχίζουν όλο το πλέγμα, και συνήθως έχουν ένα κοινό θέμα, για παράδειγμα τα νησιά ή τον κινηματογράφο. Μετά γεμίζω τα κενά με μικρότερες λέξεις. Αυτό είναι το πιο δύσκολο κομμάτι και μπορεί να μου πάρει μια ολόκληρη μέρα.", "First I choose the long words that run across the whole grid, and they usually share a theme, for example the islands or the cinema. Then I fill the gaps with shorter words. That's the hardest part and it can take me a whole day."),
  L("Δημοσιογράφος", "f", "Και οι ορισμοί;", "And the clues?"),
  L("Σταυρολεξάς", "m", "Εκεί είναι η διασκέδαση. Προσπαθώ να είναι έξυπνοι, αλλά δίκαιοι: ο αναγνώστης πρέπει να μπορεί να βρει τη λύση χωρίς λεξικό. Κάθε εβδομάδα λαμβάνω γράμματα από αναγνώστες. Μια κυρία ενενήντα χρονών μού γράφει εδώ και δέκα χρόνια για να μου επισημάνει τα λάθη μου, και συνήθως έχει δίκιο.", "That's where the fun is. I try to make them clever but fair: the reader must be able to find the answer without a dictionary. Every week I get letters from readers. A ninety-year-old lady has been writing to me for ten years to point out my mistakes, and she's usually right."),
 ],
 "questions": [
  Q("Τι διαλέγει πρώτα ο σταυρολεξάς;", ["Τους ορισμούς", "Τις μεγάλες λέξεις, που συνήθως έχουν ένα κοινό θέμα", "Τις μικρές λέξεις", "Το μέγεθος του πλέγματος"], 1, "Πρώτα διαλέγω τις μεγάλες λέξεις"),
  Q("Ποιο είναι για εκείνον το πιο δύσκολο κομμάτι;", ["Να γράψει τους ορισμούς", "Να βρει θέμα", "Να γεμίσει τα κενά με μικρότερες λέξεις", "Να απαντήσει στα γράμματα"], 2, "Μετά γεμίζω τα κενά με μικρότερες λέξεις. Αυτό είναι το πιο δύσκολο κομμάτι"),
  Q("Τι κάνει η κυρία των ενενήντα χρονών;", ["Του γράφει για να του επισημάνει τα λάθη του", "Λύνει όλα τα σταυρόλεξα σε πέντε λεπτά", "Του στέλνει καινούργιες λέξεις", "Του ζητά πιο εύκολα σταυρόλεξα"], 0, "μού γράφει εδώ και δέκα χρόνια για να μου επισημάνει τα λάθη μου"),
 ],
 "gloss": {"σταυρόλεξα": "σταυρόλεξο — crossword", "διασχίζουν": "διασχίζω — to cross", "πλέγμα": "πλέγμα — grid", "κενά": "κενό — gap, blank", "ορισμοί": "ορισμός — definition, clue", "διασκέδαση": "διασκέδαση — fun", "δίκαιοι": "δίκαιος — fair", "λύση": "λύση — solution", "λαμβάνω": "λαμβάνω — to receive", "επισημάνει": "επισημαίνω — to point out"}
})

ITEMS.append({
 "id": "l139-dia-anemokoudouno", "title": "Το καμπανάκι του γείτονα", "title_en": "The neighbour's wind chime", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά στην κουζίνα το πρωί.",
 "script": [
  L("Μανώλης", "m", "Πάλι δεν έκλεισα μάτι. Αυτό το καμπανάκι στο μπαλκόνι του κυρίου Τάκη χτυπούσε όλη τη νύχτα με τον αέρα. Ντιν, ντιν, ντιν, μέχρι τις πέντε.", "I didn't sleep a wink again. That wind chime on Mr Takis's balcony was ringing all night in the wind. Ding, ding, ding, until five."),
  L("Λίνα", "f", "Το ξέρω, το άκουγα κι εγώ. Αλλά μην πας να του χτυπήσεις την πόρτα θυμωμένος. Μου είπε η κυρά-Ρένα ότι του το χάρισε η κόρη του πριν μετακομίσει στην Αυστραλία.", "I know, I heard it too. But don't go and knock on his door angry. Mrs Rena told me his daughter gave it to him before she moved to Australia."),
  L("Μανώλης", "m", "Δηλαδή να μην πω τίποτα; Να μην κοιμάμαι για πάντα;", "So I shouldn't say anything? Should I never sleep again?"),
  L("Λίνα", "f", "Όχι, αλλά να του το πεις ευγενικά. Ίσως μπορεί να το βγάζει μόνο τα βράδια με αέρα, ή να το κρεμάσει μέσα, δίπλα στο παράθυρο. Έτσι θα το βλέπει και θα θυμάται την κόρη του, κι εμείς θα κοιμόμαστε.", "No, but tell him politely. Maybe he could take it down only on windy nights, or hang it inside, next to the window. That way he'll see it and remember his daughter, and we'll sleep."),
 ],
 "questions": [
  Q("Γιατί δεν κοιμήθηκε ο Μανώλης;", ["Γιατί έκανε ζέστη", "Γιατί το καμπανάκι του γείτονα χτυπούσε όλη τη νύχτα", "Γιατί γάβγιζε ένας σκύλος", "Γιατί είχε δουλειά"], 1, "Αυτό το καμπανάκι στο μπαλκόνι του κυρίου Τάκη χτυπούσε όλη τη νύχτα με τον αέρα"),
  Q("Γιατί είναι σημαντικό το καμπανάκι για τον κύριο Τάκη;", ["Το αγόρασε σε ένα ταξίδι", "Του το χάρισε η κόρη του πριν μετακομίσει στην Αυστραλία", "Ήταν της γυναίκας του", "Το έφτιαξε ο ίδιος"], 1, "του το χάρισε η κόρη του πριν μετακομίσει στην Αυστραλία"),
  Q("Τι προτείνει η Λίνα;", ["Να καλέσουν την αστυνομία", "Να μετακομίσουν", "Να του μιλήσουν ευγενικά και να του προτείνουν να το κρεμάσει μέσα", "Να βάλουν ωτοασπίδες χωρίς να του πουν τίποτα"], 2, "να του το πεις ευγενικά"),
 ],
 "gloss": {"δεν έκλεισα μάτι": "δεν κλείνω μάτι — not to sleep a wink", "καμπανάκι": "καμπανάκι — little bell, wind chime", "θυμωμένος": "θυμωμένος — angry", "χάρισε": "χαρίζω — to give as a present", "μετακομίσει": "μετακομίζω — to move house", "ευγενικά": "ευγενικά — politely", "κρεμάσει": "κρεμάω — to hang"}
})

ITEMS.append({
 "id": "l139-news-kafeneio", "title": "Ένα χωριό αγοράζει το καφενείο του", "title_en": "A village buys its café", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια ειδησεογραφική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "m", "Όταν ο ιδιοκτήτης του μοναδικού καφενείου ενός ορεινού χωριού της Ηπείρου ανακοίνωσε ότι βγαίνει στη σύνταξη και ότι κανείς από τα παιδιά του δεν ήθελε να το συνεχίσει, οι κάτοικοι ανησύχησαν. Το καφενείο ήταν το μόνο μέρος όπου μαζεύονταν όλοι, από τους βοσκούς ως τους λίγους νέους του χωριού.", "When the owner of the only café in a mountain village in Epirus announced that he was retiring and that none of his children wanted to carry it on, the residents were worried. The café was the only place where everyone gathered, from the shepherds to the few young people in the village."),
  L("Ρεπόρτερ", "m", "Αποφάσισαν λοιπόν να το αγοράσουν μαζί. Ογδόντα τρεις κάτοικοι και φίλοι του χωριού έγιναν μέλη ενός συνεταιρισμού, ο καθένας με ένα μερίδιο. Με τα χρήματα αγόρασαν το κτίριο και το ανακαίνισαν, κυρίως με εθελοντική εργασία.", "So they decided to buy it together. Eighty-three residents and friends of the village became members of a cooperative, each with a share. With the money they bought the building and renovated it, mainly with volunteer labour."),
  L("Ρεπόρτερ", "m", "Σήμερα το καφενείο έχει έναν μισθωτό υπάλληλο, πουλά και βασικά τρόφιμα, για να μην κατεβαίνουν οι ηλικιωμένοι στην πόλη, και κάθε Σάββατο φιλοξενεί ένα μικρό σινεμά. Τα κέρδη, όσα υπάρχουν, μένουν στο χωριό.", "Today the café has one paid employee, also sells basic groceries, so that the elderly don't have to go down to the town, and every Saturday it hosts a small cinema. The profits, such as they are, stay in the village."),
 ],
 "questions": [
  Q("Γιατί ανησύχησαν οι κάτοικοι;", ["Γιατί το καφενείο θα έκλεινε, αφού ο ιδιοκτήτης έβγαινε στη σύνταξη", "Γιατί αυξήθηκαν οι τιμές", "Γιατί άνοιξε ένα δεύτερο καφενείο", "Γιατί χάλασε ο δρόμος"], 0, "ανακοίνωσε ότι βγαίνει στη σύνταξη"),
  Q("Πώς αγόρασαν το καφενείο;", ["Με ένα δάνειο του δήμου", "Με μια δωρεά από έναν επιχειρηματία", "Μέσα από έναν συνεταιρισμό, με ογδόντα τρία μέλη", "Το αγόρασε ο πρόεδρος του χωριού"], 2, "Ογδόντα τρεις κάτοικοι και φίλοι του χωριού έγιναν μέλη ενός συνεταιρισμού"),
  Q("Γιατί πουλά το καφενείο και βασικά τρόφιμα;", ["Για να βγάζει περισσότερα κέρδη", "Για να μην κατεβαίνουν οι ηλικιωμένοι στην πόλη", "Γιατί το ζήτησε ο νόμος", "Για τους τουρίστες"], 1, "για να μην κατεβαίνουν οι ηλικιωμένοι στην πόλη"),
 ],
 "gloss": {"ιδιοκτήτης": "ιδιοκτήτης — owner", "καφενείου": "καφενείο — traditional café", "σύνταξη": "σύνταξη — retirement, pension", "ανησύχησαν": "ανησυχώ — to worry", "βοσκούς": "βοσκός — shepherd", "συνεταιρισμού": "συνεταιρισμός — cooperative", "μερίδιο": "μερίδιο — share", "ανακαίνισαν": "ανακαινίζω — to renovate", "εθελοντική": "εθελοντικός — voluntary", "μισθωτό": "μισθωτός — salaried, paid", "κέρδη": "κέρδος — profit"}
})

ITEMS.append({
 "id": "l139-int-mageiras-ploiou", "title": "Μάγειρας στους ωκεανούς", "title_en": "A cook on the oceans", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από μια ραδιοφωνική εκπομπή για τα επαγγέλματα της θάλασσας.",
 "script": [
  L("Δημοσιογράφος", "f", "Είστε μάγειρας σε ένα φορτηγό πλοίο. Για πόσους ανθρώπους μαγειρεύετε;", "You're a cook on a cargo ship. How many people do you cook for?"),
  L("Μάγειρας", "m", "Είμαστε είκοσι δύο άτομα πλήρωμα, από έξι διαφορετικές χώρες. Μαγειρεύω τρία γεύματα τη μέρα, επτά μέρες την εβδομάδα. Και πρέπει να ευχαριστήσω και τον Φιλιππινέζο ναύτη και τον Ουκρανό μηχανικό και τον Έλληνα καπετάνιο. Γι' αυτό κάθε μέρα έχω τουλάχιστον δύο κυρίως πιάτα, και ένα από αυτά πάντα με ρύζι.", "We're a crew of twenty-two, from six different countries. I cook three meals a day, seven days a week. And I have to please the Filipino sailor and the Ukrainian engineer and the Greek captain. That's why every day I have at least two main dishes, and one of them always with rice."),
  L("Δημοσιογράφος", "f", "Τι γίνεται όταν έχει φουρτούνα;", "What happens when there's a storm?"),
  L("Μάγειρας", "m", "Τότε ξεχνάς τις σούπες! Οι κατσαρόλες έχουν ειδικές μεταλλικές μπάρες για να μη γλιστρούν, αλλά πάλι μαγειρεύω πιο απλά φαγητά. Το πιο δύσκολο όμως είναι να σχεδιάσεις τα ψώνια: όταν ταξιδεύουμε τρεις εβδομάδες στον ωκεανό, αν ξεχάσω τα κρεμμύδια, δεν υπάρχει μπακάλικο στη γωνία.", "Then you forget about soups! The pots have special metal bars so they don't slide, but I still cook simpler dishes. The hardest thing, though, is planning the shopping: when we sail for three weeks across the ocean, if I forget the onions, there's no grocer's on the corner."),
 ],
 "questions": [
  Q("Γιατί ο μάγειρας φτιάχνει κάθε μέρα τουλάχιστον δύο κυρίως πιάτα;", ["Γιατί το πλήρωμα είναι από διαφορετικές χώρες και πρέπει να ευχαριστήσει όλους", "Γιατί του περισσεύουν υλικά", "Γιατί το ζητά η εταιρεία", "Γιατί ο καπετάνιος είναι χορτοφάγος"], 0, "πρέπει να ευχαριστήσω και τον Φιλιππινέζο ναύτη και τον Ουκρανό μηχανικό και τον Έλληνα καπετάνιο"),
  Q("Τι κάνει όταν έχει φουρτούνα;", ["Δεν μαγειρεύει καθόλου", "Φτιάχνει μόνο σούπες", "Μαγειρεύει πιο απλά φαγητά", "Σερβίρει μόνο σάντουιτς"], 2, "μαγειρεύω πιο απλά φαγητά"),
  Q("Ποιο είναι το πιο δύσκολο, κατά τον μάγειρα;", ["Το κρύο", "Να σχεδιάσει τα ψώνια", "Να πλύνει τα πιάτα", "Η μοναξιά"], 1, "Το πιο δύσκολο όμως είναι να σχεδιάσεις τα ψώνια"),
 ],
 "gloss": {"φορτηγό πλοίο": "φορτηγό πλοίο — cargo ship", "πλήρωμα": "πλήρωμα — crew", "γεύματα": "γεύμα — meal", "ναύτη": "ναύτης — sailor", "μηχανικό": "μηχανικός — engineer", "κυρίως πιάτα": "κυρίως πιάτο — main dish", "φουρτούνα": "φουρτούνα — storm at sea", "κατσαρόλες": "κατσαρόλα — pot", "γλιστρούν": "γλιστράω — to slide, slip", "μπακάλικο": "μπακάλικο — grocer's"}
})

ITEMS.append({
 "id": "l139-c1-overton", "title": "Το «παράθυρο του Όβερτον»", "title_en": "The 'Overton window'", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκπομπή για την πολιτική επικοινωνία.",
 "script": [
  L("Δημοσιογράφος", "m", "Ακούμε όλο και συχνότερα για το «παράθυρο του Όβερτον». Από πού προέρχεται ο όρος;", "We hear more and more often about the 'Overton window'. Where does the term come from?"),
  L("Πολιτική επιστήμονας", "f", "Από τον Τζόζεφ Όβερτον, έναν Αμερικανό που εργαζόταν τη δεκαετία του 1990 σε ένα ερευνητικό ινστιτούτο του Μίσιγκαν. Η ιδέα του ήταν απλή: σε κάθε εποχή, μόνο ένα περιορισμένο φάσμα πολιτικών θεωρείται αποδεκτό από την κοινή γνώμη. Ό,τι βρίσκεται μέσα σε αυτό το «παράθυρο» μπορεί να το προτείνει ένας πολιτικός χωρίς να ρισκάρει την καριέρα του· ό,τι βρίσκεται έξω χαρακτηρίζεται ακραίο ή αδιανόητο.", "From Joseph Overton, an American who worked in the 1990s at a research institute in Michigan. His idea was simple: in every era, only a limited range of policies is considered acceptable by public opinion. Whatever lies inside this 'window' a politician can propose without risking their career; whatever lies outside is described as extreme or unthinkable."),
  L("Δημοσιογράφος", "m", "Δηλαδή οι πολιτικοί δεν οδηγούν, αλλά ακολουθούν.", "So politicians don't lead, they follow."),
  L("Πολιτική επιστήμονας", "f", "Αυτή ήταν η βασική του διαπίστωση. Το παράθυρο δεν το μετακινούν συνήθως οι ίδιοι οι πολιτικοί, αλλά οι συγγραφείς, τα κινήματα, οι δημοσιογράφοι, ακόμα και η λογοτεχνία, που κάνουν μια ιδέα σταδιακά συζητήσιμη, μετά λογική και τελικά αυτονόητη. Ο ίδιος ο Όβερτον σκοτώθηκε σε αεροπορικό δυστύχημα το 2003, και τον όρο τον διέδωσαν αργότερα οι συνεργάτες του.", "That was his central finding. The window is usually moved not by politicians themselves, but by writers, movements, journalists, even literature, which gradually make an idea discussable, then reasonable and finally self-evident. Overton himself was killed in a plane accident in 2003, and the term was spread later by his colleagues."),
  L("Δημοσιογράφος", "m", "Σήμερα όμως τον χρησιμοποιούν όλοι, συχνά για να κατηγορήσουν τους αντιπάλους τους.", "But today everyone uses it, often to accuse their opponents."),
  L("Πολιτική επιστήμονας", "f", "Ακριβώς, και εδώ χρειάζεται προσοχή. Το μοντέλο περιγράφει πώς αλλάζει η κοινή γνώμη· δεν μας λέει αν μια αλλαγή είναι καλή ή κακή. Με τον ίδιο μηχανισμό καθιερώθηκαν η ψήφος των γυναικών και η κατάργηση της δουλείας, αλλά μπορούν να κανονικοποιηθούν και επικίνδυνες ιδέες.", "Exactly, and care is needed here. The model describes how public opinion changes; it doesn't tell us whether a change is good or bad. Women's suffrage and the abolition of slavery became established by the same mechanism, but dangerous ideas can also be normalised."),
 ],
 "questions": [
  Q("Τι είναι, σύμφωνα με τον Όβερτον, το «παράθυρο»;", ["Ένα σύστημα ψηφοφορίας", "Το περιορισμένο φάσμα πολιτικών που θεωρείται αποδεκτό από την κοινή γνώμη", "Η περίοδος πριν από τις εκλογές", "Ένα ινστιτούτο του Μίσιγκαν"], 1, "μόνο ένα περιορισμένο φάσμα πολιτικών θεωρείται αποδεκτό από την κοινή γνώμη"),
  Q("Ποιοι μετακινούν συνήθως το παράθυρο;", ["Οι ίδιοι οι πολιτικοί", "Τα δικαστήρια", "Οι συγγραφείς, τα κινήματα, οι δημοσιογράφοι και η λογοτεχνία", "Οι δημοσκόποι"], 2, "αλλά οι συγγραφείς, τα κινήματα, οι δημοσιογράφοι, ακόμα και η λογοτεχνία"),
  Q("Πώς διαδόθηκε ο όρος;", ["Τον διέδωσαν οι συνεργάτες του μετά τον θάνατό του", "Τον χρησιμοποίησε ένας πρόεδρος", "Έγινε τίτλος ενός βιβλίου του", "Τον διέδωσε μια ταινία"], 0, "τον όρο τον διέδωσαν αργότερα οι συνεργάτες του"),
  Q("Για ποιο πράγμα προειδοποιεί η πολιτική επιστήμονας;", ["Ότι ο όρος είναι λάθος", "Ότι το μοντέλο δεν ισχύει πια", "Ότι μόνο κακές ιδέες κανονικοποιούνται", "Ότι το μοντέλο περιγράφει την αλλαγή, χωρίς να λέει αν είναι καλή ή κακή"], 3, "Το μοντέλο περιγράφει πώς αλλάζει η κοινή γνώμη· δεν μας λέει αν μια αλλαγή είναι καλή ή κακή"),
 ],
 "gloss": {"ινστιτούτο": "ινστιτούτο — institute", "περιορισμένο": "περιορισμένος — limited", "φάσμα": "φάσμα — range, spectrum", "κοινή γνώμη": "κοινή γνώμη — public opinion", "ρισκάρει": "ρισκάρω — to risk", "ακραίο": "ακραίος — extreme", "αδιανόητο": "αδιανόητος — unthinkable", "διαπίστωση": "διαπίστωση — finding", "σταδιακά": "σταδιακά — gradually", "αυτονόητη": "αυτονόητος — self-evident", "δυστύχημα": "δυστύχημα — accident", "διέδωσαν": "διαδίδω — to spread", "καθιερώθηκαν": "καθιερώνομαι — to become established", "κατάργηση": "κατάργηση — abolition", "κανονικοποιηθούν": "κανονικοποιούμαι — to be normalised"}
})

ITEMS.append({
 "id": "l139-c1-lombard", "title": "Γιατί φωνάζουμε στον θόρυβο", "title_en": "Why we shout in noise", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκλαϊκευτική ομιλία για τη φωνή και την ακοή.",
 "script": [
  L("Ομιλητής", "m", "Έχετε προσέξει ότι σε ένα θορυβώδες εστιατόριο όλοι μιλάμε όλο και πιο δυνατά, ώσπου στο τέλος σχεδόν φωνάζουμε; Το φαινόμενο περιέγραψε το 1909 ο Γάλλος ωτορινολαρυγγολόγος Ετιέν Λομπάρ, και από τότε φέρει το όνομά του.", "Have you noticed that in a noisy restaurant we all talk louder and louder, until in the end we're almost shouting? The phenomenon was described in 1909 by the French ear, nose and throat doctor Étienne Lombard, and it has borne his name ever since."),
  L("Ομιλητής", "m", "Ο Λομπάρ παρατήρησε ότι, όταν ο θόρυβος γύρω μας αυξάνεται, υψώνουμε τη φωνή μας ακούσια, χωρίς να το αποφασίσουμε. Και δεν αλλάζει μόνο η ένταση: ανεβαίνει ο τόνος, τα φωνήεντα μακραίνουν, και η άρθρωση γίνεται πιο προσεκτική. Ο οργανισμός μας, με άλλα λόγια, προσαρμόζει αυτόματα το «σήμα» για να ξεχωρίζει από τον «θόρυβο».", "Lombard observed that when the noise around us increases, we raise our voice involuntarily, without deciding to. And it isn't only the volume that changes: the pitch rises, vowels get longer, and articulation becomes more careful. Our organism, in other words, automatically adjusts the 'signal' so that it stands out from the 'noise'."),
  L("Ομιλητής", "m", "Ο Λομπάρ χρησιμοποίησε την ανακάλυψή του και με πρακτικό τρόπο: για να ξεσκεπάσει όσους προσποιούνταν ότι ήταν κουφοί. Αν κάποιος που λέει ότι δεν ακούει συνεχίζει να μιλά με την ίδια ένταση όταν του βάζεις θόρυβο στα αυτιά, κάτι δεν πάει καλά.", "Lombard also put his discovery to practical use: to unmask people who were pretending to be deaf. If someone who says they can't hear keeps speaking at the same volume when you play noise into their ears, something is wrong."),
  L("Ομιλητής", "m", "Το πιο εντυπωσιακό είναι ότι το φαινόμενο δεν είναι μόνο ανθρώπινο. Έχει παρατηρηθεί σε πουλιά, σε πιθήκους και σε φάλαινες. Έρευνες στο Βερολίνο έδειξαν, για παράδειγμα, ότι τα αηδόνια που ζουν δίπλα σε δρόμους με πολλή κίνηση τραγουδούν πιο δυνατά, και μάλιστα πιο δυνατά τις καθημερινές απ' ό,τι τις Κυριακές.", "The most impressive thing is that the phenomenon isn't only human. It has been observed in birds, monkeys and whales. Research in Berlin showed, for example, that nightingales living next to busy roads sing louder, and in fact louder on weekdays than on Sundays."),
 ],
 "questions": [
  Q("Τι περιέγραψε ο Λομπάρ το 1909;", ["Ότι ο θόρυβος βλάπτει την ακοή", "Ότι όταν ο θόρυβος αυξάνεται υψώνουμε τη φωνή μας ακούσια", "Ότι τα εστιατόρια είναι θορυβώδη", "Μια θεραπεία για την κώφωση"], 1, "όταν ο θόρυβος γύρω μας αυξάνεται, υψώνουμε τη φωνή μας ακούσια"),
  Q("Τι αλλάζει στη φωνή εκτός από την ένταση;", ["Τίποτα άλλο", "Μιλάμε πιο γρήγορα και πιο σιγά", "Ο τόνος ανεβαίνει, τα φωνήεντα μακραίνουν και η άρθρωση γίνεται πιο προσεκτική", "Η φωνή γίνεται πιο βαθιά"], 2, "ανεβαίνει ο τόνος, τα φωνήεντα μακραίνουν, και η άρθρωση γίνεται πιο προσεκτική"),
  Q("Πώς χρησιμοποίησε ο Λομπάρ την ανακάλυψή του;", ["Για να ξεσκεπάσει όσους προσποιούνταν ότι ήταν κουφοί", "Για να σχεδιάσει ακουστικά", "Για να μάθει τραγούδι", "Για να μειώσει τον θόρυβο στις πόλεις"], 0, "για να ξεσκεπάσει όσους προσποιούνταν ότι ήταν κουφοί"),
  Q("Τι έδειξαν οι έρευνες στο Βερολίνο;", ["Ότι τα αηδόνια φεύγουν από την πόλη", "Ότι τα αηδόνια τραγουδούν μόνο τις Κυριακές", "Ότι τα αηδόνια σωπαίνουν στον θόρυβο", "Ότι τα αηδόνια δίπλα σε δρόμους τραγουδούν πιο δυνατά, ιδίως τις καθημερινές"], 3, "τα αηδόνια που ζουν δίπλα σε δρόμους με πολλή κίνηση τραγουδούν πιο δυνατά"),
 ],
 "gloss": {"εκλαϊκευτική": "εκλαϊκευτικός — popular-science", "θορυβώδες": "θορυβώδης — noisy", "ωτορινολαρυγγολόγος": "ωτορινολαρυγγολόγος — ear, nose and throat doctor", "ακούσια": "ακούσια — involuntarily", "ένταση": "ένταση — volume, intensity", "φωνήεντα": "φωνήεν — vowel", "άρθρωση": "άρθρωση — articulation", "προσαρμόζει": "προσαρμόζω — to adjust", "ξεσκεπάσει": "ξεσκεπάζω — to unmask", "προσποιούνταν": "προσποιούμαι — to pretend", "κουφοί": "κουφός — deaf", "φάλαινες": "φάλαινα — whale", "αηδόνια": "αηδόνι — nightingale"}
})

rnd = random.Random(139)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-139.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
