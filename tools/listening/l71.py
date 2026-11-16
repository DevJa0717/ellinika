# Source for library/listening/listening-71.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l71.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l71-ann-syntagma-kleisto", "title": "Κλειστός ο σταθμός Σύνταγμα", "title_en": "Syntagma station closed", "type": "announcement", "level": "B2",
 "context_el": "Είστε σε έναν συρμό του μετρό της Αθήνας. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί επιβάτες, σας ενημερώνουμε ότι, λόγω συγκέντρωσης στο κέντρο της πόλης, ο σταθμός Σύνταγμα παραμένει κλειστός με εντολή της αστυνομίας. Οι συρμοί και των δύο γραμμών θα διέρχονται από τον σταθμό χωρίς στάση.", "Dear passengers, we inform you that, because of a rally in the city centre, Syntagma station remains closed by order of the police. Trains on both lines will pass through the station without stopping."),
  L("Εκφωνήτρια", "f", "Οι επιβάτες της μπλε γραμμής που θέλουν να αλλάξουν γραμμή μπορούν να χρησιμοποιήσουν τον σταθμό Μοναστηράκι. Οι επιβάτες της κόκκινης γραμμής μπορούν να αποβιβαστούν στους σταθμούς Ακρόπολη ή Πανεπιστήμιο.", "Blue line passengers who want to change lines can use Monastiraki station. Red line passengers can get off at Akropoli or Panepistimio stations."),
  L("Εκφωνήτρια", "f", "Η επαναλειτουργία του σταθμού θα ανακοινωθεί εγκαίρως. Ζητούμε την κατανόησή σας για την ταλαιπωρία.", "The reopening of the station will be announced in good time. We ask for your understanding for the inconvenience."),
 ],
 "questions": [
  Q("Γιατί είναι κλειστός ο σταθμός;", ["Λόγω βλάβης", "Λόγω συγκέντρωσης στο κέντρο", "Λόγω απεργίας", "Λόγω εργασιών"], 1, "λόγω συγκέντρωσης στο κέντρο της πόλης"),
  Q("Τι θα κάνουν οι συρμοί στο Σύνταγμα;", ["Θα σταματούν για λίγα δευτερόλεπτα", "Θα διέρχονται χωρίς στάση", "Θα τερματίζουν εκεί", "Θα αλλάζουν γραμμή"], 1, "θα διέρχονται από τον σταθμό χωρίς στάση"),
  Q("Πού μπορούν να αλλάξουν γραμμή οι επιβάτες της μπλε γραμμής;", ["Στην Ακρόπολη", "Στο Πανεπιστήμιο", "Στο Μοναστηράκι", "Στο Σύνταγμα"], 2, "μπορούν να χρησιμοποιήσουν τον σταθμό Μοναστηράκι"),
 ],
 "gloss": {"συρμό": "συρμός — (metro) train", "συγκέντρωσης": "συγκέντρωση — rally, gathering", "εντολή": "εντολή — order", "διέρχονται": "διέρχομαι — to pass through", "αποβιβαστούν": "αποβιβάζομαι — to get off", "επαναλειτουργία": "επαναλειτουργία — reopening", "εγκαίρως": "εγκαίρως — in good time", "ταλαιπωρία": "ταλαιπωρία — inconvenience"},
})

ITEMS.append({
 "id": "l71-vm-koufomata", "title": "Τα καινούργια κουφώματα", "title_en": "The new window frames", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε παραγγείλει καινούργια παράθυρα για το σπίτι σας. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από την εταιρεία που θα τα τοποθετήσει.",
 "script": [
  L("Τεχνικός", "m", "Καλησπέρα, ο Στέλιος είμαι, από την εταιρεία με τα κουφώματα. Δυστυχώς, πρέπει να μεταθέσουμε την τοποθέτηση, που ήταν για αύριο. Τα τζάμια για την μπαλκονόπορτα ήρθαν από το εργοστάσιο σε λάθος διάσταση και τα επιστρέψαμε.", "Good evening, it's Stelios from the window-frame company. Unfortunately, we have to postpone the installation, which was for tomorrow. The panes for the balcony door came from the factory in the wrong size and we sent them back."),
  L("Τεχνικός", "m", "Τα σωστά θα είναι έτοιμα την Τετάρτη, οπότε προτείνω να έρθουμε την Πέμπτη το πρωί. Θα χρειαστεί να είναι κάποιος στο σπίτι από τις οκτώ ως τις δώδεκα, και καλό θα ήταν να μετακινήσετε τα έπιπλα που είναι κοντά στα παράθυρα.", "The correct ones will be ready on Wednesday, so I suggest we come on Thursday morning. Someone will need to be at home from eight to twelve, and it would be good if you moved the furniture that is near the windows."),
  L("Τεχνικός", "m", "Το υπόλοιπο της πληρωμής το εξοφλείτε μετά την τοποθέτηση, όπως είχαμε συμφωνήσει. Πάρτε με, σας παρακαλώ, να μου πείτε αν σας βολεύει η Πέμπτη. Ευχαριστώ και συγγνώμη για την αλλαγή.", "You pay the rest of the payment after the installation, as we had agreed. Please call me to tell me whether Thursday suits you. Thank you, and sorry for the change."),
 ],
 "questions": [
  Q("Γιατί αναβάλλεται η τοποθέτηση;", ["Ο τεχνικός είναι άρρωστος", "Τα τζάμια ήρθαν σε λάθος διάσταση", "Ο πελάτης δεν πλήρωσε", "Το φορτηγό χάλασε"], 1, "ήρθαν από το εργοστάσιο σε λάθος διάσταση"),
  Q("Τι ζητάει ο τεχνικός από τον πελάτη;", ["Να αγοράσει καινούργια έπιπλα", "Να μετακινήσει τα έπιπλα κοντά στα παράθυρα", "Να πληρώσει από πριν", "Να πάει στο εργοστάσιο"], 1, "να μετακινήσετε τα έπιπλα που είναι κοντά στα παράθυρα"),
  Q("Πότε θα πληρωθεί το υπόλοιπο;", ["Την Τετάρτη", "Πριν από την τοποθέτηση", "Μετά την τοποθέτηση", "Σε δόσεις"], 2, "Το υπόλοιπο της πληρωμής το εξοφλείτε μετά την τοποθέτηση"),
 ],
 "gloss": {"κουφώματα": "κούφωμα — window/door frame", "τοποθετήσει": "τοποθετώ — to install, fit", "μεταθέσουμε": "μεταθέτω — to postpone, move", "τζάμια": "τζάμι — pane of glass", "μπαλκονόπορτα": "μπαλκονόπορτα — balcony door", "διάσταση": "διάσταση — size, dimension", "εξοφλείτε": "εξοφλώ — to pay off", "βολεύει": "βολεύω — to suit"},
})

ITEMS.append({
 "id": "l71-dia-sykia", "title": "Τα κλαδιά της συκιάς", "title_en": "The fig tree's branches", "type": "dialogue", "level": "B2",
 "context_el": "Δύο γείτονες σε μια μονοκατοικία των προαστίων συζητούν στον φράχτη που χωρίζει τις αυλές τους.",
 "script": [
  L("Λευτέρης", "m", "Κυρία Βούλα, καλημέρα. Δεν θέλω να σας στενοχωρήσω, αλλά τα κλαδιά της συκιάς σας έχουν περάσει για τα καλά στη δική μας αυλή. Τα σύκα πέφτουν στο πλακόστρωτο, λιώνουν και μαζεύουν σφήκες.", "Mrs Voula, good morning. I don't want to upset you, but the branches of your fig tree have well and truly come over into our yard. The figs fall on the paving, go mushy and attract wasps."),
  L("Βούλα", "f", "Έχετε δίκιο, κύριε Λευτέρη, το έχω δει κι εγώ. Η συκιά τη φύτεψε ο άντρας μου πριν από τριάντα χρόνια και δεν μου πάει η καρδιά να την κόψω. Αλλά το κλάδεμα είναι άλλο πράγμα.", "You're right, Mr Lefteris, I've seen it too. My husband planted the fig tree thirty years ago and I don't have the heart to cut it down. But pruning is another matter."),
  L("Λευτέρης", "m", "Κανείς δεν μιλάει για κόψιμο! Λέω μόνο να κοπούν τα κλαδιά που περνάνε από τον φράχτη. Μάλιστα, ο γαμπρός μου έχει αλυσοπρίονο και μπορεί να έρθει το Σάββατο.", "Nobody's talking about cutting it down! I'm only saying the branches that come over the fence should be cut. In fact, my son-in-law has a chainsaw and can come on Saturday."),
  L("Βούλα", "f", "Να ξέρετε ότι η συκιά κλαδεύεται τον χειμώνα, όταν δεν έχει φύλλα. Αν την κόψουμε τώρα, θα ταλαιπωρηθεί. Τον Ιανουάριο, όμως, ευχαρίστως. Και μέχρι τότε, ό,τι σύκα πέφτουν σε σας, μαζέψτε τα πριν πέσουν και φτιάξτε γλυκό!", "You should know that a fig tree is pruned in winter, when it has no leaves. If we cut it now, it will suffer. In January, though, gladly. And until then, whatever figs fall on your side, pick them before they fall and make jam!"),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα του Λευτέρη;", ["Η συκιά του κόβει τον ήλιο", "Τα σύκα πέφτουν στην αυλή του και μαζεύουν σφήκες", "Οι ρίζες χάλασαν τον φράχτη", "Τα φύλλα βουλώνουν τις υδρορροές"], 1, "Τα σύκα πέφτουν στο πλακόστρωτο, λιώνουν και μαζεύουν σφήκες"),
  Q("Γιατί η Βούλα δεν θέλει να κόψει τη συκιά;", ["Γιατί τη φύτεψε ο άντρας της", "Γιατί πουλάει τα σύκα", "Γιατί απαγορεύεται", "Γιατί κοστίζει ακριβά"], 0, "Η συκιά τη φύτεψε ο άντρας μου πριν από τριάντα χρόνια"),
  Q("Πότε προτείνει η Βούλα να γίνει το κλάδεμα;", ["Το Σάββατο", "Τον Ιανουάριο", "Την άνοιξη", "Αμέσως"], 1, "Τον Ιανουάριο, όμως, ευχαρίστως"),
 ],
 "gloss": {"μονοκατοικία": "μονοκατοικία — detached house", "φράχτη": "φράχτης — fence", "συκιάς": "συκιά — fig tree", "πλακόστρωτο": "πλακόστρωτο — paving", "σφήκες": "σφήκα — wasp", "κλάδεμα": "κλάδεμα — pruning", "αλυσοπρίονο": "αλυσοπρίονο — chainsaw", "κλαδεύεται": "κλαδεύω — to prune", "ταλαιπωρηθεί": "ταλαιπωρούμαι — to suffer, be put through hardship", "ευχαρίστως": "ευχαρίστως — gladly"},
})

ITEMS.append({
 "id": "l71-dia-antlia-thermotitas", "title": "Αντλία θερμότητας ή λέβητας;", "title_en": "Heat pump or boiler?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι αποφασίζει τι θέρμανση θα βάλει στο παλιό διαμέρισμα που ανακαινίζει.",
 "script": [
  L("Ρένα", "f", "Ο υδραυλικός μάς έστειλε δύο προσφορές: έναν καινούργιο λέβητα φυσικού αερίου ή μια αντλία θερμότητας. Η αντλία κοστίζει σχεδόν τα διπλά.", "The plumber sent us two quotes: a new natural gas boiler or a heat pump. The heat pump costs almost twice as much."),
  L("Νίκος", "m", "Ναι, αλλά καταναλώνει πολύ λιγότερη ενέργεια, και μπορεί να μας δώσει και δροσιά το καλοκαίρι. Επιπλέον, υπάρχει επιδότηση για τέτοια συστήματα, αν το διαμέρισμα πάρει καλύτερη ενεργειακή κατηγορία.", "Yes, but it uses much less energy, and it can also cool us in the summer. Besides, there's a subsidy for such systems if the flat gets a better energy rating."),
  L("Ρένα", "f", "Η αντλία, όμως, αποδίδει καλά μόνο αν το σπίτι είναι καλά μονωμένο. Με τα παλιά παράθυρα και χωρίς μόνωση στην ταράτσα, θα πετάμε λεφτά.", "But a heat pump only performs well if the house is well insulated. With the old windows and no insulation on the roof, we'll be throwing money away."),
  L("Νίκος", "m", "Τότε ας κάνουμε πρώτα τη μόνωση και τα παράθυρα, που έτσι κι αλλιώς τα χρειαζόμαστε, και μετά βάζουμε την αντλία. Μέχρι τότε, τα καλοριφέρ κρατάνε άλλον έναν χειμώνα.", "Then let's do the insulation and the windows first, which we need anyway, and then we put in the heat pump. Until then, the radiators will last another winter."),
 ],
 "questions": [
  Q("Τι πλεονέκτημα της αντλίας αναφέρει ο Νίκος;", ["Είναι φθηνότερη στην αγορά", "Καταναλώνει λιγότερη ενέργεια και δροσίζει το καλοκαίρι", "Δεν χρειάζεται συντήρηση", "Μπαίνει σε μία μέρα"], 1, "καταναλώνει πολύ λιγότερη ενέργεια, και μπορεί να μας δώσει και δροσιά το καλοκαίρι"),
  Q("Τι ανησυχεί τη Ρένα;", ["Ο θόρυβος της αντλίας", "Ότι το σπίτι δεν είναι καλά μονωμένο", "Ότι ο υδραυλικός δεν είναι αξιόπιστος", "Ότι δεν υπάρχει φυσικό αέριο στην περιοχή"], 1, "αποδίδει καλά μόνο αν το σπίτι είναι καλά μονωμένο"),
  Q("Τι αποφασίζουν τελικά;", ["Να βάλουν λέβητα αμέσως", "Να κάνουν πρώτα μόνωση και παράθυρα και μετά την αντλία", "Να μείνουν για πάντα με τα καλοριφέρ", "Να πουλήσουν το διαμέρισμα"], 1, "ας κάνουμε πρώτα τη μόνωση και τα παράθυρα"),
 ],
 "gloss": {"ανακαινίζει": "ανακαινίζω — to renovate", "υδραυλικός": "υδραυλικός — plumber", "λέβητα": "λέβητας — boiler", "αντλία θερμότητας": "αντλία θερμότητας — heat pump", "επιδότηση": "επιδότηση — subsidy", "ενεργειακή κατηγορία": "ενεργειακή κατηγορία — energy rating", "αποδίδει": "αποδίδω — to perform, be efficient", "μονωμένο": "μονωμένος — insulated", "ταράτσα": "ταράτσα — flat roof", "καλοριφέρ": "καλοριφέρ — radiator(s)"},
})

ITEMS.append({
 "id": "l71-int-taktopoiisi", "title": "Μια επαγγελματίας της τακτοποίησης", "title_en": "A professional home organiser", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη σε ραδιοφωνική εκπομπή με μια γυναίκα που τακτοποιεί σπίτια επαγγελματικά.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αλεξίου, πολλοί ακροατές δεν ξέρουν ότι υπάρχει τέτοιο επάγγελμα. Τι ακριβώς κάνετε;", "Ms Alexiou, many listeners don't know that such a profession exists. What exactly do you do?"),
  L("Ελπίδα", "f", "Βοηθάω ανθρώπους να ξεφορτωθούν όσα δεν χρειάζονται και να οργανώσουν όσα κρατάνε. Δεν έρχομαι να καθαρίσω· δουλεύω μαζί με τον πελάτη, γιατί αυτός αποφασίζει τι μένει και τι φεύγει.", "I help people get rid of what they don't need and organise what they keep. I don't come to clean; I work together with the client, because they decide what stays and what goes."),
  L("Δημοσιογράφος", "m", "Ποιοι σας καλούν συνήθως;", "Who usually calls you?"),
  L("Ελπίδα", "f", "Συχνά άνθρωποι που περνούν μια αλλαγή: μια μετακόμιση, ένα διαζύγιο, τον θάνατο ενός γονιού. Το πιο δύσκολο είναι να αδειάσει κανείς το πατρικό του. Εκεί κάθε αντικείμενο έχει μια ιστορία, και η δουλειά πάει αργά.", "Often people going through a change: a move, a divorce, the death of a parent. The hardest thing is emptying one's family home. There every object has a story, and the work goes slowly."),
  L("Δημοσιογράφος", "m", "Και πού καταλήγουν όσα πετάτε;", "And where do the things you throw out end up?"),
  L("Ελπίδα", "f", "Πετάμε όσο το δυνατόν λιγότερα. Τα ρούχα και τα έπιπλα σε καλή κατάσταση πηγαίνουν σε κοινωνικά παντοπωλεία και σε οργανώσεις, τα βιβλία σε δημοτικές βιβλιοθήκες. Ο κανόνας μου είναι απλός: ό,τι δεν το χρησιμοποίησες εδώ και δύο χρόνια, κάποιος άλλος το χρειάζεται περισσότερο.", "We throw away as little as possible. Clothes and furniture in good condition go to social groceries and organisations, books to municipal libraries. My rule is simple: whatever you haven't used for two years, someone else needs more."),
 ],
 "questions": [
  Q("Πώς δουλεύει η Ελπίδα;", ["Καθαρίζει το σπίτι μόνη της", "Αποφασίζει εκείνη τι θα πεταχτεί", "Δουλεύει μαζί με τον πελάτη, που αποφασίζει", "Δίνει μόνο συμβουλές από το τηλέφωνο"], 2, "δουλεύω μαζί με τον πελάτη, γιατί αυτός αποφασίζει τι μένει και τι φεύγει"),
  Q("Ποια δουλειά θεωρεί την πιο δύσκολη;", ["Μια μετακόμιση", "Το άδειασμα του πατρικού σπιτιού", "Την τακτοποίηση ενός γραφείου", "Τα σπίτια με παιδιά"], 1, "Το πιο δύσκολο είναι να αδειάσει κανείς το πατρικό του"),
  Q("Ποιος είναι ο κανόνας της;", ["Ό,τι δεν χρησιμοποιήθηκε για δύο χρόνια το χρειάζεται κάποιος άλλος", "Κρατάμε μόνο τα ακριβά πράγματα", "Πετάμε τα μισά από όσα έχουμε", "Δεν δίνουμε τίποτα σε άγνωστους"], 0, "ό,τι δεν το χρησιμοποίησες εδώ και δύο χρόνια, κάποιος άλλος το χρειάζεται περισσότερο"),
 ],
 "gloss": {"τακτοποιεί": "τακτοποιώ — to tidy, organise", "ξεφορτωθούν": "ξεφορτώνομαι — to get rid of", "μετακόμιση": "μετακόμιση — house move", "διαζύγιο": "διαζύγιο — divorce", "πατρικό": "πατρικό (σπίτι) — family home", "καταλήγουν": "καταλήγω — to end up", "κοινωνικά παντοπωλεία": "κοινωνικό παντοπωλείο — social grocery (free food/goods for those in need)"},
})

ITEMS.append({
 "id": "l71-rep-peristera", "title": "Το υποβρύχιο μουσείο της Αλοννήσου", "title_en": "The underwater museum of Alonissos", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από ραδιοφωνική εκπομπή για τον πολιτισμό.",
 "script": [
  L("Ρεπόρτερ", "f", "Ανοιχτά της νησίδας Περιστέρα, κοντά στην Αλόννησο, βρίσκεται σε βάθος περίπου τριάντα μέτρων ένα από τα πιο σημαντικά αρχαία ναυάγια της Μεσογείου. Το πλοίο βυθίστηκε τον 5ο αιώνα π.Χ. και μετέφερε χιλιάδες αμφορείς με κρασί.", "Off the islet of Peristera, near Alonissos, lies at a depth of about thirty metres one of the most important ancient shipwrecks of the Mediterranean. The ship sank in the 5th century BC and was carrying thousands of amphorae of wine."),
  L("Ρεπόρτερ", "f", "Το ναυάγιο το εντόπισε τη δεκαετία του 1980 ένας ψαράς του νησιού, που είδε αμφορείς να ξεχωρίζουν στον βυθό. Από το 2020, ο χώρος είναι επισκέψιμος για δύτες, με τη συνοδεία πιστοποιημένων οδηγών, και θεωρείται το πρώτο υποβρύχιο μουσείο της χώρας.", "The wreck was located in the 1980s by a fisherman from the island, who saw amphorae standing out on the seabed. Since 2020 the site has been open to divers, accompanied by certified guides, and it is considered the country's first underwater museum."),
  L("Ρεπόρτερ", "f", "Όσοι δεν καταδύονται δεν μένουν έξω από την εμπειρία: στο κέντρο ενημέρωσης του νησιού, με γυαλιά εικονικής πραγματικότητας, μπορούν να «κολυμπήσουν» πάνω από τους αμφορείς χωρίς να βραχούν. Οι κάτοικοι ελπίζουν ότι το μουσείο θα φέρει επισκέπτες και εκτός καλοκαιριού.", "Those who don't dive are not left out of the experience: at the island's information centre, with virtual-reality headsets, they can 'swim' over the amphorae without getting wet. The residents hope the museum will bring visitors outside the summer too."),
 ],
 "questions": [
  Q("Τι μετέφερε το αρχαίο πλοίο;", ["Λάδι", "Αγάλματα", "Αμφορείς με κρασί", "Σιτάρι"], 2, "μετέφερε χιλιάδες αμφορείς με κρασί"),
  Q("Ποιος εντόπισε το ναυάγιο;", ["Ένας αρχαιολόγος", "Ένας ψαράς του νησιού", "Ένας τουρίστας δύτης", "Το Πολεμικό Ναυτικό"], 1, "Το ναυάγιο το εντόπισε τη δεκαετία του 1980 ένας ψαράς του νησιού"),
  Q("Τι μπορούν να κάνουν όσοι δεν καταδύονται;", ["Να δουν το ναυάγιο από γυάλινη βάρκα", "Να το δουν με γυαλιά εικονικής πραγματικότητας", "Να αγγίξουν αμφορείς στο λιμάνι", "Τίποτα"], 1, "με γυαλιά εικονικής πραγματικότητας"),
 ],
 "gloss": {"νησίδας": "νησίδα — islet", "ναυάγια": "ναυάγιο — shipwreck", "βυθίστηκε": "βυθίζομαι — to sink", "αμφορείς": "αμφορέας — amphora", "βυθό": "βυθός — seabed", "επισκέψιμος": "επισκέψιμος — open to visitors", "δύτες": "δύτης — diver", "πιστοποιημένων": "πιστοποιημένος — certified", "καταδύονται": "καταδύομαι — to dive", "εικονικής πραγματικότητας": "εικονική πραγματικότητα — virtual reality"},
})

ITEMS.append({
 "id": "l71-mono-giagia-anoia", "title": "Η γιαγιά μου και η άνοια", "title_en": "My grandmother and dementia", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια νεαρή γυναίκα να μιλά σε μια ομάδα υποστήριξης για οικογένειες ανθρώπων με άνοια.",
 "script": [
  L("Μυρτώ", "f", "Η γιαγιά μου άρχισε να ξεχνάει πριν από τέσσερα χρόνια. Στην αρχή ήταν μικρά πράγματα: έχανε τα κλειδιά, ρωτούσε δύο φορές το ίδιο. Όταν μια μέρα χάθηκε στη γειτονιά όπου ζούσε πενήντα χρόνια, καταλάβαμε ότι κάτι σοβαρό συνέβαινε.", "My grandmother began to forget four years ago. At first it was little things: she lost her keys, asked the same thing twice. When one day she got lost in the neighbourhood where she had lived for fifty years, we realised that something serious was happening."),
  L("Μυρτώ", "f", "Το πιο δύσκολο για μένα δεν ήταν η κούραση, αλλά η μέρα που με κοίταξε και με ρώτησε ποια είμαι. Έκλαψα στο μπάνιο για μισή ώρα. Μετά έμαθα κάτι που με βοήθησε πολύ: να μην τη διορθώνω. Αν νομίζει ότι είναι 1975, ζω μαζί της στο 1975.", "The hardest thing for me wasn't the tiredness, but the day she looked at me and asked who I was. I cried in the bathroom for half an hour. Afterwards I learned something that helped me a lot: not to correct her. If she thinks it's 1975, I live with her in 1975."),
  L("Μυρτώ", "f", "Η μουσική κάνει θαύματα. Της βάζω τραγούδια της νιότης της και τα λέει ολόκληρα, χωρίς να ξεχνάει ούτε μία λέξη. Σε αυτές τις στιγμές τη βρίσκω ξανά. Και έμαθα να ζητάω βοήθεια· μόνος κανείς δεν τα βγάζει πέρα.", "Music works miracles. I put on songs from her youth and she sings them all the way through, without forgetting a single word. In those moments I find her again. And I learned to ask for help; nobody can cope alone."),
 ],
 "questions": [
  Q("Πότε κατάλαβε η οικογένεια ότι το πρόβλημα ήταν σοβαρό;", ["Όταν η γιαγιά έχασε τα κλειδιά", "Όταν χάθηκε στη γειτονιά της", "Όταν σταμάτησε να μιλάει", "Όταν πήγε στο νοσοκομείο"], 1, "Όταν μια μέρα χάθηκε στη γειτονιά όπου ζούσε πενήντα χρόνια"),
  Q("Τι έμαθε η Μυρτώ να κάνει;", ["Να διορθώνει τη γιαγιά της", "Να μην τη διορθώνει", "Να της κρύβει τα κλειδιά", "Να μην της μιλάει για το παρελθόν"], 1, "να μην τη διορθώνω"),
  Q("Τι λέει για τη μουσική;", ["Ότι ενοχλεί τη γιαγιά", "Ότι η γιαγιά θυμάται ολόκληρα τα τραγούδια της νιότης της", "Ότι η γιαγιά δεν άκουγε ποτέ μουσική", "Ότι τη βοηθάει να κοιμηθεί"], 1, "Της βάζω τραγούδια της νιότης της και τα λέει ολόκληρα"),
 ],
 "gloss": {"άνοια": "άνοια — dementia", "υποστήριξης": "υποστήριξη — support", "χάθηκε": "χάνομαι — to get lost", "κούραση": "κούραση — tiredness", "διορθώνω": "διορθώνω — to correct", "νιότης": "νιότη — youth", "τα βγάζει πέρα": "τα βγάζω πέρα — to cope, manage"},
})

ITEMS.append({
 "id": "l71-mono-allilografia", "title": "Ξανά γράμματα με το χέρι", "title_en": "Handwritten letters again", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν άντρα να μιλά σε ένα podcast για ένα χόμπι που ξεκίνησε πριν από δύο χρόνια.",
 "script": [
  L("Θοδωρής", "m", "Πριν από δύο χρόνια γράφτηκα σε μια διεθνή ομάδα αλληλογραφίας. Σήμερα έχω επτά φίλους δι' αλληλογραφίας, από την Ιαπωνία μέχρι τη Χιλή, και τους γράφω γράμματα με το χέρι, σε χαρτί, με γραμματόσημο.", "Two years ago I joined an international letter-writing group. Today I have seven pen friends, from Japan to Chile, and I write them letters by hand, on paper, with a stamp."),
  L("Θοδωρής", "m", "Οι φίλοι μου γελάνε: «Γιατί δεν στέλνεις ένα μήνυμα;» Μα ακριβώς αυτή είναι η ομορφιά. Ένα γράμμα κάνει δύο με τρεις εβδομάδες να φτάσει, άρα γράφεις πιο προσεκτικά, σκέφτεσαι τι αξίζει να πεις. Δεν απαντάς βιαστικά, όπως στο κινητό.", "My friends laugh: 'Why don't you send a message?' But that's exactly the beauty of it. A letter takes two to three weeks to arrive, so you write more carefully, you think about what is worth saying. You don't answer hastily, as on your phone."),
  L("Θοδωρής", "m", "Υπάρχει και κάτι άλλο: το γράμμα είναι αντικείμενο. Η φίλη μου από την Ιαπωνία βάζει μέσα αποξηραμένα λουλούδια, ένας Χιλιανός μού στέλνει ζωγραφιές. Τα φυλάω σε ένα κουτί. Τα μηνύματα στο κινητό κάποτε χάνονται· αυτό το κουτί θα το έχω για πάντα.", "There's something else too: a letter is an object. My friend from Japan puts dried flowers inside, a Chilean sends me drawings. I keep them in a box. Messages on your phone get lost at some point; this box I'll have forever."),
 ],
 "questions": [
  Q("Πόσους φίλους δι' αλληλογραφίας έχει ο Θοδωρής;", ["Δύο", "Τρεις", "Επτά", "Δέκα"], 2, "Σήμερα έχω επτά φίλους δι' αλληλογραφίας"),
  Q("Γιατί, κατά τον Θοδωρή, γράφει κανείς πιο προσεκτικά ένα γράμμα;", ["Γιατί κοστίζει ακριβά", "Γιατί κάνει εβδομάδες να φτάσει", "Γιατί δεν μπορεί να σβήσει", "Γιατί το διαβάζουν πολλοί"], 1, "Ένα γράμμα κάνει δύο με τρεις εβδομάδες να φτάσει, άρα γράφεις πιο προσεκτικά"),
  Q("Τι κάνει με τα γράμματα που παίρνει;", ["Τα πετάει", "Τα φωτογραφίζει", "Τα φυλάει σε ένα κουτί", "Τα δίνει σε μουσείο"], 2, "Τα φυλάω σε ένα κουτί"),
 ],
 "gloss": {"αλληλογραφίας": "αλληλογραφία — correspondence", "φίλους δι' αλληλογραφίας": "φίλος δι' αλληλογραφίας — pen friend", "γραμματόσημο": "γραμματόσημο — postage stamp", "βιαστικά": "βιαστικά — hastily", "αποξηραμένα": "αποξηραμένος — dried", "φυλάω": "φυλάω — to keep"},
})

ITEMS.append({
 "id": "l71-c1-seismiki-proeidopoiisi", "title": "Μπορούμε να προειδοποιηθούμε για έναν σεισμό;", "title_en": "Can we be warned about an earthquake?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια σεισμολόγο σε επιστημονική εκπομπή του ραδιοφώνου.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Ζαχαρίου, μετά από κάθε μεγάλο σεισμό ακούμε την ίδια ερώτηση: γιατί δεν μπορούμε να τον προβλέψουμε;", "Ms Zachariou, after every big earthquake we hear the same question: why can't we predict it?"),
  L("Σεισμολόγος", "f", "Γιατί η πρόβλεψη, με την αυστηρή έννοια, δηλαδή η ακριβής ώρα, ο τόπος και το μέγεθος, παραμένει αδύνατη με τις σημερινές γνώσεις. Μπορούμε να εκτιμήσουμε πιθανότητες για δεκαετίες, όχι να πούμε «την Τρίτη στις τρεις». Όποιος ισχυρίζεται το αντίθετο, παραπλανά το κοινό.", "Because prediction in the strict sense, that is the exact time, place and magnitude, remains impossible with today's knowledge. We can estimate probabilities over decades, not say 'on Tuesday at three'. Anyone who claims otherwise is misleading the public."),
  L("Δημοσιογράφος", "m", "Τι είναι, τότε, τα συστήματα έγκαιρης προειδοποίησης που λειτουργούν σε χώρες όπως η Ιαπωνία;", "What, then, are the early warning systems that operate in countries like Japan?"),
  L("Σεισμολόγος", "f", "Δεν προβλέπουν· αντιδρούν. Όταν ξεκινά ένας σεισμός, τα πρώτα κύματα, που είναι πιο γρήγορα αλλά λιγότερο καταστροφικά, ανιχνεύονται από τους σταθμούς κοντά στο επίκεντρο. Το σύστημα υπολογίζει σε δευτερόλεπτα το μέγεθος και στέλνει ειδοποίηση, πριν φτάσουν τα πιο επικίνδυνα κύματα σε πιο απομακρυσμένες περιοχές.", "They don't predict; they react. When an earthquake starts, the first waves, which are faster but less destructive, are detected by the stations near the epicentre. The system calculates the magnitude in seconds and sends an alert before the more dangerous waves reach more distant areas."),
  L("Δημοσιογράφος", "m", "Και τι κερδίζουμε με λίγα δευτερόλεπτα;", "And what do we gain with a few seconds?"),
  L("Σεισμολόγος", "f", "Περισσότερα απ' όσα νομίζετε. Ένα τρένο υψηλής ταχύτητας φρενάρει, ένας χειρουργός σταματά την τομή, οι ανελκυστήρες σταματούν στον πλησιέστερο όροφο, τα παιδιά προλαβαίνουν να μπουν κάτω από τα θρανία. Το αδύναμο σημείο είναι η «τυφλή ζώνη»: όσοι βρίσκονται πολύ κοντά στο επίκεντρο δεν προλαβαίνουν να ειδοποιηθούν. Γι' αυτό καμία τεχνολογία δεν αντικαθιστά τα αντισεισμικά κτίρια.", "More than you think. A high-speed train brakes, a surgeon stops the incision, lifts stop at the nearest floor, children have time to get under their desks. The weak point is the 'blind zone': those very close to the epicentre do not get warned in time. That is why no technology replaces earthquake-resistant buildings."),
 ],
 "questions": [
  Q("Τι λέει η σεισμολόγος για την πρόβλεψη των σεισμών;", ["Ότι θα είναι δυνατή σε λίγα χρόνια", "Ότι μπορούμε να εκτιμήσουμε μόνο πιθανότητες για δεκαετίες", "Ότι γίνεται ήδη στην Ιαπωνία", "Ότι τα ζώα την κάνουν καλύτερα"], 1, "Μπορούμε να εκτιμήσουμε πιθανότητες για δεκαετίες"),
  Q("Πώς λειτουργούν τα συστήματα έγκαιρης προειδοποίησης;", ["Προβλέπουν τον σεισμό από τις αλλαγές του καιρού", "Ανιχνεύουν τα πρώτα, γρηγορότερα κύματα και στέλνουν ειδοποίηση", "Μετρούν το νερό στα πηγάδια", "Βασίζονται σε στατιστικά παλιών σεισμών"], 1, "τα πρώτα κύματα, που είναι πιο γρήγορα αλλά λιγότερο καταστροφικά, ανιχνεύονται"),
  Q("Ποιο είναι το αδύναμο σημείο τους;", ["Κοστίζουν πολύ", "Όσοι είναι πολύ κοντά στο επίκεντρο δεν προλαβαίνουν να ειδοποιηθούν", "Δίνουν συχνά ψεύτικους συναγερμούς", "Λειτουργούν μόνο τη μέρα"], 1, "όσοι βρίσκονται πολύ κοντά στο επίκεντρο δεν προλαβαίνουν να ειδοποιηθούν"),
  Q("Ποιο είναι το συμπέρασμά της;", ["Η τεχνολογία θα λύσει το πρόβλημα", "Καμία τεχνολογία δεν αντικαθιστά τα αντισεισμικά κτίρια", "Πρέπει να εγκαταλείψουμε τις σεισμογενείς περιοχές", "Τα σχολεία πρέπει να κλείνουν"], 1, "καμία τεχνολογία δεν αντικαθιστά τα αντισεισμικά κτίρια"),
 ],
 "gloss": {"σεισμολόγο": "σεισμολόγος — seismologist", "προβλέψουμε": "προβλέπω — to predict", "παραπλανά": "παραπλανώ — to mislead", "έγκαιρης προειδοποίησης": "έγκαιρη προειδοποίηση — early warning", "ανιχνεύονται": "ανιχνεύω — to detect", "επίκεντρο": "επίκεντρο — epicentre", "τομή": "τομή — incision", "θρανία": "θρανίο — school desk", "αντισεισμικά": "αντισεισμικός — earthquake-resistant"},
})

ITEMS.append({
 "id": "l71-c1-monotoniko", "title": "Από το πολυτονικό στο μονοτονικό", "title_en": "From the polytonic to the monotonic system", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε απόσπασμα από μια διάλεξη για την ιστορία της ελληνικής γραφής.",
 "script": [
  L("Καθηγήτρια", "f", "Όσοι μεγάλωσαν μετά το 1982 ίσως δεν έχουν γράψει ποτέ δασεία ή περισπωμένη. Το πολυτονικό σύστημα, με τρεις τόνους και δύο πνεύματα, επινοήθηκε από γραμματικούς της Αλεξάνδρειας για να αποδοθεί ο μουσικός τονισμός της αρχαίας γλώσσας, που χάθηκε ήδη στην ύστερη αρχαιότητα.", "Those who grew up after 1982 may never have written a rough breathing or a circumflex. The polytonic system, with three accents and two breathings, was devised by grammarians in Alexandria to render the musical pitch accent of the ancient language, which was already lost in late antiquity."),
  L("Καθηγήτρια", "f", "Για αιώνες, λοιπόν, οι μαθητές μάθαιναν να βάζουν σημάδια που δεν αντιστοιχούσαν πια σε καμία προφορά. Το «ὁ» και το «ὅ» ακούγονταν ακριβώς το ίδιο. Η διάκριση στηριζόταν στην απομνημόνευση κανόνων, και τα λάθη ήταν αναπόφευκτα, ακόμη και στους μορφωμένους.", "For centuries, then, pupils learned to put marks that no longer corresponded to any pronunciation. 'ὁ' and 'ὅ' sounded exactly the same. The distinction rested on memorising rules, and mistakes were inevitable, even among the educated."),
  L("Καθηγήτρια", "f", "Η καθιέρωση της δημοτικής ως επίσημης γλώσσας το 1976 άνοιξε τον δρόμο, και το 1982 το μονοτονικό έγινε το επίσημο σύστημα: ένας τόνος, μόνο στις λέξεις με περισσότερες από μία συλλαβές. Η αντίδραση ήταν έντονη· κάποιοι μίλησαν για «ακρωτηριασμό» της γλώσσας και για ρήξη με την παράδοση.", "The establishment of demotic as the official language in 1976 opened the way, and in 1982 the monotonic system became the official one: one accent, only on words with more than one syllable. The reaction was strong; some spoke of a 'mutilation' of the language and of a break with tradition."),
  L("Καθηγήτρια", "f", "Σήμερα η διαμάχη έχει κοπάσει. Το πολυτονικό επιβιώνει σε ορισμένους εκδοτικούς οίκους, στην εκκλησία και στη διδασκαλία των αρχαίων. Αξίζει, όμως, να θυμόμαστε ότι η ορθογραφία είναι σύμβαση και όχι ουσία της γλώσσας: ο Σολωμός και ο Καβάφης δεν έγιναν λιγότερο μεγάλοι επειδή τους διαβάζουμε με έναν τόνο.", "Today the dispute has died down. The polytonic system survives at some publishing houses, in the church and in the teaching of Ancient Greek. It is worth remembering, though, that spelling is a convention and not the essence of the language: Solomos and Cavafy did not become any less great because we read them with one accent."),
 ],
 "questions": [
  Q("Γιατί επινοήθηκε το πολυτονικό σύστημα;", ["Για να ξεχωρίζουν τα ελληνικά από τα λατινικά", "Για να αποδοθεί ο μουσικός τονισμός της αρχαίας γλώσσας", "Για να γράφονται πιο γρήγορα τα κείμενα", "Για τις ανάγκες της εκκλησίας"], 1, "για να αποδοθεί ο μουσικός τονισμός της αρχαίας γλώσσας"),
  Q("Ποιο πρόβλημα είχε το πολυτονικό στη νεότερη εποχή;", ["Δεν υπήρχαν τυπογραφεία", "Τα σημάδια δεν αντιστοιχούσαν πια σε καμία προφορά", "Το χρησιμοποιούσαν μόνο οι ποιητές", "Απαγορεύτηκε από την εκκλησία"], 1, "σημάδια που δεν αντιστοιχούσαν πια σε καμία προφορά"),
  Q("Τι συνέβη το 1982;", ["Η δημοτική έγινε επίσημη γλώσσα", "Το μονοτονικό έγινε το επίσημο σύστημα", "Καταργήθηκε η διδασκαλία των αρχαίων", "Επανήλθε το πολυτονικό"], 1, "το 1982 το μονοτονικό έγινε το επίσημο σύστημα"),
  Q("Ποια είναι η άποψη της ομιλήτριας;", ["Ότι το μονοτονικό ακρωτηρίασε τη γλώσσα", "Ότι η ορθογραφία είναι σύμβαση και όχι ουσία της γλώσσας", "Ότι πρέπει να επιστρέψουμε στο πολυτονικό", "Ότι ο Καβάφης έγραφε σε μονοτονικό"], 1, "η ορθογραφία είναι σύμβαση και όχι ουσία της γλώσσας"),
 ],
 "gloss": {"δασεία": "δασεία — rough breathing (῾)", "περισπωμένη": "περισπωμένη — circumflex accent (῀)", "πνεύματα": "πνεύμα — breathing (mark)", "επινοήθηκε": "επινοώ — to devise, invent", "τονισμός": "τονισμός — accentuation, pitch accent", "απομνημόνευση": "απομνημόνευση — memorisation", "αναπόφευκτα": "αναπόφευκτος — inevitable", "καθιέρωση": "καθιέρωση — establishment", "ακρωτηριασμό": "ακρωτηριασμός — mutilation", "κοπάσει": "κοπάζω — to die down, subside", "σύμβαση": "σύμβαση — convention"},
})

rnd = random.Random(71)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-71.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
