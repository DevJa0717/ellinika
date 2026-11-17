# Source for library/listening/listening-149.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l149.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l149-vm-optika", "title": "Οι φακοί θα αργήσουν", "title_en": "The lenses will be late", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από το κατάστημα οπτικών όπου παραγγείλατε γυαλιά οράσεως.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, από το κατάστημα οπτικών «Ίρις» σας τηλεφωνώ. Ο σκελετός που διαλέξατε ήρθε, αλλά οι φακοί με την αντιθαμβωτική επίστρωση θα καθυστερήσουν περίπου μία εβδομάδα, γιατί ο προμηθευτής έχει πρόβλημα με τις παραγγελίες.", "Good morning, I'm calling from the Iris optician's. The frame you chose has arrived, but the lenses with the anti-fog coating will be about a week late, because the supplier has a problem with orders."),
  L("Υπάλληλος", "f", "Αν βιάζεστε, μπορούμε να σας βάλουμε προσωρινά απλούς φακούς, χωρίς καμία επιπλέον χρέωση, και να τους αλλάξουμε όταν έρθουν οι κανονικοί. Αλλιώς, θα σας ειδοποιήσουμε με μήνυμα μόλις είναι έτοιμα.", "If you're in a hurry, we can fit simple lenses temporarily, at no extra charge, and change them when the proper ones arrive. Otherwise, we'll let you know by text as soon as they're ready."),
  L("Υπάλληλος", "f", "Όταν έρθετε, φέρτε μαζί και τα παλιά σας γυαλιά, για να ελέγξουμε αν η καινούργια συνταγή σάς ταιριάζει καλύτερα. Είμαστε ανοιχτά καθημερινά μέχρι τις εννιά, εκτός από την Τετάρτη το απόγευμα.", "When you come, bring your old glasses too, so we can check whether the new prescription suits you better. We're open every day until nine, except Wednesday afternoon."),
 ],
 "questions": [
  Q("Τι θα καθυστερήσει;", ["Ο σκελετός", "Οι φακοί με την αντιθαμβωτική επίστρωση", "Η θήκη των γυαλιών", "Η συνταγή του γιατρού"], 1, "οι φακοί με την αντιθαμβωτική επίστρωση θα καθυστερήσουν"),
  Q("Τι σας προτείνει, αν βιάζεστε;", ["Να πάρετε άλλον σκελετό", "Να πάτε σε άλλο κατάστημα", "Να σας βάλουν προσωρινά απλούς φακούς", "Να πληρώσετε για γρήγορη παράδοση"], 2, "μπορούμε να σας βάλουμε προσωρινά απλούς φακούς"),
  Q("Τι πρέπει να φέρετε όταν πάτε;", ["Τα παλιά σας γυαλιά", "Την απόδειξη", "Τη συνταγή του γιατρού", "Μια φωτογραφία"], 0, "φέρτε μαζί και τα παλιά σας γυαλιά"),
 ],
 "gloss": {"οπτικών": "οπτικά — optician's", "οράσεως": "γυαλιά οράσεως — prescription glasses", "σκελετός": "σκελετός — frame (of glasses)", "φακοί": "φακός — lens", "αντιθαμβωτική": "αντιθαμβωτικός — anti-fog", "επίστρωση": "επίστρωση — coating", "προμηθευτής": "προμηθευτής — supplier", "προσωρινά": "προσωρινά — temporarily", "συνταγή": "συνταγή — prescription"}
})

ITEMS.append({
 "id": "l149-ann-nychterina-leoforeia", "title": "Νέες νυχτερινές γραμμές λεωφορείων", "title_en": "New night bus lines", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση της εταιρείας αστικών συγκοινωνιών στο ραδιόφωνο.",
 "script": [
  L("Εκφωνητής", "m", "Από την πρώτη του μήνα, τρεις νέες νυχτερινές γραμμές λεωφορείων θα συνδέουν το κέντρο της πόλης με τις ανατολικές και τις δυτικές συνοικίες. Τα λεωφορεία θα κυκλοφορούν από τα μεσάνυχτα μέχρι τις πέντε το πρωί, κάθε μισή ώρα.", "From the first of the month, three new night bus lines will link the city centre with the eastern and western districts. The buses will run from midnight until five in the morning, every half hour."),
  L("Εκφωνητής", "m", "Οι γραμμές δημιουργήθηκαν ύστερα από αίτημα εργαζομένων σε νοσοκομεία, εστιατόρια και καταστήματα που κλείνουν αργά, καθώς και φοιτητών. Τις Παρασκευές και τα Σάββατα τα δρομολόγια θα είναι πιο συχνά, κάθε είκοσι λεπτά.", "The lines were created after a request from people working in hospitals, restaurants and shops that close late, as well as students. On Fridays and Saturdays the services will be more frequent, every twenty minutes."),
  L("Εκφωνητής", "m", "Το εισιτήριο είναι το ίδιο με των κανονικών γραμμών. Για λόγους ασφαλείας, όλα τα νυχτερινά λεωφορεία θα έχουν κάμερες, και οι επιβάτες θα μπορούν να ζητήσουν από τον οδηγό να σταματήσει και ανάμεσα σε δύο στάσεις.", "The ticket is the same as on the regular lines. For safety reasons, all night buses will have cameras, and passengers will be able to ask the driver to stop between two stops as well."),
 ],
 "questions": [
  Q("Πόσο συχνά θα περνούν τα λεωφορεία τις καθημερινές;", ["Κάθε δέκα λεπτά", "Κάθε ώρα", "Κάθε μισή ώρα", "Κάθε είκοσι λεπτά"], 2, "κάθε μισή ώρα"),
  Q("Γιατί δημιουργήθηκαν οι γραμμές;", ["Ύστερα από αίτημα εργαζομένων και φοιτητών", "Για τους τουρίστες", "Γιατί έκλεισε το μετρό", "Για μια συναυλία"], 0, "ύστερα από αίτημα εργαζομένων σε νοσοκομεία, εστιατόρια και καταστήματα"),
  Q("Τι μπορούν να ζητήσουν οι επιβάτες για λόγους ασφαλείας;", ["Να τους συνοδεύσει ένας υπάλληλος", "Να σταματήσει ο οδηγός και ανάμεσα σε δύο στάσεις", "Να ταξιδέψουν δωρεάν", "Να κλείσουν θέση από πριν"], 1, "να ζητήσουν από τον οδηγό να σταματήσει και ανάμεσα σε δύο στάσεις"),
 ],
 "gloss": {"συγκοινωνιών": "συγκοινωνία — (public) transport", "νυχτερινές": "νυχτερινός — night", "συνοικίες": "συνοικία — district", "κυκλοφορούν": "κυκλοφορώ — to run, circulate", "αίτημα": "αίτημα — request", "δρομολόγια": "δρομολόγιο — (scheduled) service, route", "ασφαλείας": "ασφάλεια — safety", "επιβάτες": "επιβάτης — passenger"}
})

ITEMS.append({
 "id": "l149-dia-dentro-geitona", "title": "Το δέντρο του γείτονα", "title_en": "The neighbour's tree", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε μια συζήτηση ανάμεσα σε δύο γείτονες που μένουν σε μονοκατοικίες με κήπο.",
 "script": [
  L("Δέσποινα", "f", "Καλησπέρα, κύριε Μανώλη. Μπορώ να σας απασχολήσω λίγο; Η συκιά σας έχει μεγαλώσει πολύ, και τα κλαδιά της έχουν περάσει πάνω από τον τοίχο, στη δική μας αυλή.", "Good evening, Mr Manolis. Can I take a moment of your time? Your fig tree has grown a lot, and its branches have come over the wall into our yard."),
  L("Μανώλης", "m", "Το έχω προσέξει, κυρία Δέσποινα. Σας ενοχλούν τα σύκα που πέφτουν;", "I've noticed, Mrs Despoina. Are the figs that fall bothering you?"),
  L("Δέσποινα", "f", "Τα σύκα δεν με πειράζουν, μάλιστα τα τρώμε! Το πρόβλημα είναι ότι τα φύλλα βουλώνουν το λούκι της στέγης, και τον χειμώνα το νερό πέφτει μέσα στο σπίτι.", "The figs don't bother me, in fact we eat them! The problem is that the leaves block the roof gutter, and in winter the water comes into the house."),
  L("Μανώλης", "m", "Α, αυτό δεν το ήξερα. Τον Νοέμβριο, που θα έχουν πέσει τα φύλλα, θα φωνάξω έναν κηπουρό να κλαδέψει τα κλαδιά από τη μεριά σας. Και θα σας καθαρίσει και το λούκι, με δικά μου έξοδα.", "Ah, I didn't know that. In November, when the leaves have fallen, I'll call a gardener to prune the branches on your side. And he'll clean your gutter too, at my expense."),
  L("Δέσποινα", "f", "Σας ευχαριστώ πολύ. Και τα σύκα της επόμενης χρονιάς θα τα μοιραστούμε!", "Thank you very much. And we'll share next year's figs!"),
 ],
 "questions": [
  Q("Ποιο είναι το πραγματικό πρόβλημα της Δέσποινας;", ["Τα σύκα που πέφτουν", "Τα φύλλα βουλώνουν το λούκι της στέγης", "Η συκιά κρύβει τον ήλιο", "Τα πουλιά κάνουν θόρυβο"], 1, "τα φύλλα βουλώνουν το λούκι της στέγης"),
  Q("Πότε θα κλαδευτεί το δέντρο;", ["Αμέσως", "Την άνοιξη", "Τον Νοέμβριο", "Το καλοκαίρι"], 2, "Τον Νοέμβριο, που θα έχουν πέσει τα φύλλα"),
  Q("Ποιος θα πληρώσει τον κηπουρό;", ["Ο Μανώλης", "Η Δέσποινα", "Θα μοιραστούν τα έξοδα", "Ο δήμος"], 0, "με δικά μου έξοδα"),
 ],
 "gloss": {"μονοκατοικίες": "μονοκατοικία — detached house", "απασχολήσω": "απασχολώ — to take up someone's time", "συκιά": "συκιά — fig tree", "κλαδιά": "κλαδί — branch", "σύκα": "σύκο — fig", "βουλώνουν": "βουλώνω — to block, clog", "λούκι": "λούκι — gutter", "κηπουρό": "κηπουρός — gardener", "κλαδέψει": "κλαδεύω — to prune", "έξοδα": "έξοδα — expenses"}
})

ITEMS.append({
 "id": "l149-int-metafrastria", "title": "Η μεταφράστρια παιδικών βιβλίων", "title_en": "The translator of children's books", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη στο ραδιόφωνο με μια γυναίκα που μεταφράζει παιδικά βιβλία.",
 "script": [
  L("Δημοσιογράφος", "m", "Είναι πιο εύκολο να μεταφράζεις παιδικά βιβλία από ό,τι βιβλία για μεγάλους;", "Is it easier to translate children's books than books for adults?"),
  L("Μεταφράστρια", "f", "Όλοι αυτό νομίζουν, αλλά συχνά είναι πιο δύσκολο. Τα παιδικά βιβλία έχουν ρίμες, λογοπαίγνια και ονόματα που σημαίνουν κάτι. Αν τα μεταφράσεις κατά λέξη, χάνεται όλο το αστείο.", "Everyone thinks so, but it's often harder. Children's books have rhymes, puns and names that mean something. If you translate them word for word, the whole joke is lost."),
  L("Δημοσιογράφος", "m", "Και τι κάνετε τότε;", "And what do you do then?"),
  L("Μεταφράστρια", "f", "Ψάχνω ένα ελληνικό αστείο που να κάνει το ίδιο αποτέλεσμα. Μια φορά άλλαξα το όνομα ενός σκύλου τρεις φορές, μέχρι να βρω ένα που να ριμάρει με το «κουτάβι».", "I look for a Greek joke that has the same effect. Once I changed a dog's name three times, until I found one that rhymed with 'puppy'."),
  L("Δημοσιογράφος", "m", "Πώς ξέρετε ότι πετύχατε;", "How do you know you've succeeded?"),
  L("Μεταφράστρια", "f", "Διαβάζω τη μετάφραση δυνατά στα ανίψια μου. Αν γελάσουν, την κρατάω. Αν βαρεθούν, ξαναρχίζω. Είναι οι πιο αυστηροί κριτές που έχω γνωρίσει.", "I read the translation aloud to my nieces and nephews. If they laugh, I keep it. If they get bored, I start again. They're the strictest critics I've ever met."),
 ],
 "questions": [
  Q("Γιατί είναι δύσκολη η μετάφραση παιδικών βιβλίων;", ["Γιατί έχουν πολλές σελίδες", "Γιατί έχουν ρίμες, λογοπαίγνια και ονόματα που σημαίνουν κάτι", "Γιατί είναι γραμμένα σε παλιά γλώσσα", "Γιατί πληρώνονται λιγότερο"], 1, "Τα παιδικά βιβλία έχουν ρίμες, λογοπαίγνια και ονόματα που σημαίνουν κάτι"),
  Q("Τι άλλαξε μια φορά τρεις φορές;", ["Τον τίτλο ενός βιβλίου", "Το τέλος μιας ιστορίας", "Το όνομα ενός σκύλου", "Τις εικόνες"], 2, "άλλαξα το όνομα ενός σκύλου τρεις φορές"),
  Q("Πώς ελέγχει αν η μετάφραση πέτυχε;", ["Τη διαβάζει δυνατά στα ανίψια της", "Τη στέλνει στον συγγραφέα", "Τη δίνει σε έναν δάσκαλο", "Τη συγκρίνει με άλλες μεταφράσεις"], 0, "Διαβάζω τη μετάφραση δυνατά στα ανίψια μου"),
 ],
 "gloss": {"μεταφράζει": "μεταφράζω — to translate", "ρίμες": "ρίμα — rhyme", "λογοπαίγνια": "λογοπαίγνιο — pun", "κατά λέξη": "κατά λέξη — word for word", "ριμάρει": "ριμάρω — to rhyme", "κουτάβι": "κουτάβι — puppy", "ανίψια": "ανίψι — nephew/niece", "βαρεθούν": "βαριέμαι — to get bored", "κριτές": "κριτής — critic, judge"}
})

ITEMS.append({
 "id": "l149-news-ichorypansi", "title": "Μέτρα για τον θόρυβο από τα μπαρ", "title_en": "Measures against noise from bars", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση από το τοπικό δελτίο ειδήσεων.",
 "script": [
  L("Παρουσιάστρια", "f", "Αυστηρότερους κανόνες για την ηχορύπανση αποφάσισε χθες το δημοτικό συμβούλιο, ύστερα από δεκάδες καταγγελίες κατοίκων του ιστορικού κέντρου. Από τον επόμενο μήνα, η μουσική στους εξωτερικούς χώρους των μπαρ θα πρέπει να σταματά στις δώδεκα τα μεσάνυχτα.", "Stricter rules on noise pollution were decided yesterday by the city council, after dozens of complaints from residents of the historic centre. From next month, music in the outdoor areas of bars will have to stop at midnight."),
  L("Παρουσιάστρια", "f", "Τα καταστήματα θα πρέπει επίσης να εγκαταστήσουν συσκευές που μετρούν την ένταση του ήχου. Όσα ξεπερνούν το όριο θα πληρώνουν πρόστιμο, και σε περίπτωση επανάληψης θα κλείνουν για μία εβδομάδα.", "Venues will also have to install devices that measure sound levels. Those that exceed the limit will pay a fine, and if it happens again they will be closed for a week."),
  L("Παρουσιάστρια", "f", "Ο σύλλογος των ιδιοκτητών εκφράζει ανησυχία για τις θέσεις εργασίας, αλλά δηλώνει ότι θα συνεργαστεί με τον δήμο. Οι κάτοικοι, από την πλευρά τους, ζητούν και περισσότερους ελέγχους από τη δημοτική αστυνομία.", "The owners' association expresses concern about jobs, but says it will cooperate with the municipality. The residents, for their part, are also asking for more checks by the municipal police."),
 ],
 "questions": [
  Q("Γιατί πάρθηκαν τα νέα μέτρα;", ["Ύστερα από δεκάδες καταγγελίες κατοίκων", "Μετά από ένα ατύχημα", "Για να έρθουν περισσότεροι τουρίστες", "Λόγω των εκλογών"], 0, "ύστερα από δεκάδες καταγγελίες κατοίκων του ιστορικού κέντρου"),
  Q("Τι θα γίνεται σε περίπτωση επανάληψης;", ["Θα διπλασιάζεται το πρόστιμο", "Το κατάστημα θα κλείνει για μία εβδομάδα", "Θα αφαιρείται η άδεια για πάντα", "Δεν θα γίνεται τίποτα"], 1, "σε περίπτωση επανάληψης θα κλείνουν για μία εβδομάδα"),
  Q("Τι ζητούν οι κάτοικοι;", ["Να κλείσουν όλα τα μπαρ", "Να μπουν κάμερες", "Περισσότερους ελέγχους από τη δημοτική αστυνομία", "Χαμηλότερους φόρους"], 2, "ζητούν και περισσότερους ελέγχους από τη δημοτική αστυνομία"),
 ],
 "gloss": {"ηχορύπανση": "ηχορύπανση — noise pollution", "καταγγελίες": "καταγγελία — complaint (to the authorities)", "εξωτερικούς": "εξωτερικός — outdoor", "εγκαταστήσουν": "εγκαθιστώ — to install", "ένταση": "ένταση — volume, intensity", "ξεπερνούν": "ξεπερνώ — to exceed", "πρόστιμο": "πρόστιμο — fine", "επανάληψης": "επανάληψη — repetition", "ανησυχία": "ανησυχία — concern"}
})

ITEMS.append({
 "id": "l149-mon-sde", "title": "Στο σχολείο στα πενήντα οχτώ", "title_en": "Back at school at fifty-eight", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλάει σε μια εκδήλωση για τα Σχολεία Δεύτερης Ευκαιρίας.",
 "script": [
  L("Στέλιος", "m", "Σταμάτησα το σχολείο στα δώδεκα, γιατί ο πατέρας μου αρρώστησε και έπρεπε να δουλέψω στο συνεργείο. Για σαράντα χρόνια έκρυβα από όλους ότι δεν είχα τελειώσει ούτε το γυμνάσιο.", "I left school at twelve, because my father fell ill and I had to work at the garage. For forty years I hid from everyone that I hadn't even finished secondary school."),
  L("Στέλιος", "m", "Η εγγονή μου ήταν αυτή που με έγραψε στο Σχολείο Δεύτερης Ευκαιρίας. Την πρώτη μέρα έτρεμαν τα χέρια μου, σαν να έδινα εξετάσεις. Στην τάξη όμως ήμασταν όλοι σαν εμένα: μια μοδίστρα, ένας ψαράς, δύο νεαρές μητέρες.", "It was my granddaughter who enrolled me in the Second Chance School. On the first day my hands were shaking, as if I were sitting exams. But in the class we were all like me: a dressmaker, a fisherman, two young mothers."),
  L("Στέλιος", "m", "Το πιο δύσκολο για μένα ήταν η έκθεση. Τώρα όμως γράφω ολόκληρες σελίδες, και πέρσι έγραψα για πρώτη φορά ένα γράμμα στη γυναίκα μου. Το έχει κορνιζάρει και το έχει κρεμάσει στο σαλόνι.", "The hardest thing for me was essay writing. But now I write whole pages, and last year I wrote a letter to my wife for the first time. She has framed it and hung it in the living room."),
 ],
 "questions": [
  Q("Γιατί σταμάτησε το σχολείο ο Στέλιος;", ["Γιατί δεν του άρεσε", "Γιατί μετακόμισε η οικογένειά του", "Γιατί αρρώστησε ο πατέρας του και έπρεπε να δουλέψει", "Γιατί απέτυχε στις εξετάσεις"], 2, "ο πατέρας μου αρρώστησε και έπρεπε να δουλέψω στο συνεργείο"),
  Q("Ποιος τον έγραψε στο σχολείο;", ["Η εγγονή του", "Η γυναίκα του", "Ένας φίλος", "Ο ίδιος"], 0, "Η εγγονή μου ήταν αυτή που με έγραψε"),
  Q("Τι έκανε η γυναίκα του με το γράμμα του;", ["Το έδειξε στα παιδιά", "Το κορνιζάρισε και το κρέμασε στο σαλόνι", "Το έστειλε σε μια εφημερίδα", "Το διόρθωσε"], 1, "Το έχει κορνιζάρει και το έχει κρεμάσει στο σαλόνι"),
 ],
 "gloss": {"Δεύτερης Ευκαιρίας": "Σχολείο Δεύτερης Ευκαιρίας — Second Chance School (adult education)", "συνεργείο": "συνεργείο — car repair garage", "γυμνάσιο": "γυμνάσιο — lower secondary school", "εγγονή": "εγγονή — granddaughter", "έτρεμαν": "τρέμω — to tremble", "μοδίστρα": "μοδίστρα — dressmaker", "έκθεση": "έκθεση — (school) essay", "κορνιζάρει": "κορνιζάρω — to frame"}
})

ITEMS.append({
 "id": "l149-rep-choris-syskevasia", "title": "Ψώνια χωρίς συσκευασία", "title_en": "Packaging-free shopping", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια ραδιοφωνική εκπομπή για το περιβάλλον.",
 "script": [
  L("Ρεπόρτερ", "f", "Σε αυτό το μικρό μαγαζί δεν θα βρείτε ούτε μία πλαστική σακούλα. Ρύζι, φακές, ζυμαρικά, ξηροί καρποί, ακόμα και απορρυπαντικά βρίσκονται σε μεγάλα γυάλινα δοχεία, και ο πελάτης παίρνει όση ποσότητα θέλει.", "In this small shop you won't find a single plastic bag. Rice, lentils, pasta, nuts, even detergents are in large glass containers, and the customer takes as much as they want."),
  L("Ρεπόρτερ", "f", "Οι περισσότεροι πελάτες φέρνουν τα δικά τους βάζα και σακουλάκια. Τα ζυγίζουν άδεια στην είσοδο, τα γεμίζουν και πληρώνουν μόνο το προϊόν. Όσοι ξεχάσουν τα δικά τους μπορούν να αγοράσουν υφασμάτινα σακουλάκια από το μαγαζί.", "Most customers bring their own jars and little bags. They weigh them empty at the entrance, fill them and pay only for the product. Those who forget theirs can buy cloth bags from the shop."),
  L("Ρεπόρτερ", "f", "Η ιδιοκτήτρια λέει ότι οι τιμές είναι συχνά χαμηλότερες από του σούπερ μάρκετ, γιατί δεν πληρώνεις τη συσκευασία. Το μεγαλύτερο όφελος όμως, προσθέτει, είναι ότι οι πελάτες αγοράζουν μόνο όσα χρειάζονται, και πετάνε λιγότερο φαγητό.", "The owner says prices are often lower than at the supermarket, because you don't pay for the packaging. But the biggest benefit, she adds, is that customers buy only what they need, and throw away less food."),
 ],
 "questions": [
  Q("Πού βρίσκονται τα προϊόντα στο μαγαζί;", ["Σε πλαστικές σακούλες", "Σε μεγάλα γυάλινα δοχεία", "Σε χάρτινα κουτιά", "Σε ψυγεία"], 1, "βρίσκονται σε μεγάλα γυάλινα δοχεία"),
  Q("Τι κάνουν οι πελάτες στην είσοδο;", ["Ζυγίζουν τα άδεια βάζα τους", "Πληρώνουν από πριν", "Παίρνουν ένα καλάθι", "Δείχνουν μια κάρτα"], 0, "Τα ζυγίζουν άδεια στην είσοδο"),
  Q("Ποιο είναι, κατά την ιδιοκτήτρια, το μεγαλύτερο όφελος;", ["Οι χαμηλές τιμές", "Η γρήγορη εξυπηρέτηση", "Οι πελάτες αγοράζουν μόνο όσα χρειάζονται και πετάνε λιγότερο φαγητό", "Τα βιολογικά προϊόντα"], 2, "οι πελάτες αγοράζουν μόνο όσα χρειάζονται, και πετάνε λιγότερο φαγητό"),
 ],
 "gloss": {"σακούλα": "σακούλα — bag", "φακές": "φακή — lentil", "ζυμαρικά": "ζυμαρικά — pasta", "ξηροί καρποί": "ξηροί καρποί — nuts", "απορρυπαντικά": "απορρυπαντικό — detergent", "δοχεία": "δοχείο — container", "ζυγίζουν": "ζυγίζω — to weigh", "υφασμάτινα": "υφασμάτινος — cloth, fabric", "συσκευασία": "συσκευασία — packaging", "όφελος": "όφελος — benefit"}
})

ITEMS.append({
 "id": "l149-dia-asfaleia-taxidiou", "title": "Ασφάλεια για το ταξίδι", "title_en": "Travel insurance", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε μια συζήτηση σε ένα ταξιδιωτικό γραφείο.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Κλείσαμε μαζί σας το ταξίδι στην Ιαπωνία τον Απρίλιο, και θέλω να ρωτήσω για ασφάλεια ταξιδιού. Χρειάζεται;", "Good morning. We booked the trip to Japan with you for April, and I want to ask about travel insurance. Is it needed?"),
  L("Υπάλληλος", "f", "Δεν είναι υποχρεωτική, αλλά σας τη συνιστώ, ειδικά για τόσο μακρινό ταξίδι. Η ευρωπαϊκή κάρτα ασφάλισης υγείας δεν ισχύει στην Ιαπωνία, και τα νοσοκομεία εκεί είναι ακριβά.", "It isn't compulsory, but I recommend it, especially for such a long trip. The European health insurance card isn't valid in Japan, and hospitals there are expensive."),
  L("Πελάτης", "m", "Και τι καλύπτει;", "And what does it cover?"),
  L("Υπάλληλος", "f", "Ιατρικά έξοδα, απώλεια αποσκευών και ακύρωση του ταξιδιού για σοβαρό λόγο, για παράδειγμα αν αρρωστήσετε πριν φύγετε. Δεν καλύπτει όμως ακυρώσεις επειδή απλώς αλλάξατε γνώμη.", "Medical expenses, lost luggage and cancellation of the trip for a serious reason, for example if you fall ill before leaving. But it doesn't cover cancellations because you simply changed your mind."),
  L("Πελάτης", "m", "Εντάξει. Πότε πρέπει να την κάνουμε;", "OK. When do we need to take it out?"),
  L("Υπάλληλος", "f", "Καλύτερα τώρα, αμέσως μετά την κράτηση. Αν την κάνετε την τελευταία εβδομάδα, δεν θα σας καλύψει για ακύρωση.", "Better now, right after the booking. If you take it out in the last week, it won't cover you for cancellation."),
 ],
 "questions": [
  Q("Γιατί η υπάλληλος συνιστά την ασφάλεια;", ["Γιατί είναι υποχρεωτική", "Γιατί η ευρωπαϊκή κάρτα δεν ισχύει στην Ιαπωνία και τα νοσοκομεία είναι ακριβά", "Γιατί είναι φθηνή", "Γιατί το ζητάει η αεροπορική εταιρεία"], 1, "Η ευρωπαϊκή κάρτα ασφάλισης υγείας δεν ισχύει στην Ιαπωνία"),
  Q("Τι ΔΕΝ καλύπτει η ασφάλεια;", ["Τα ιατρικά έξοδα", "Την απώλεια αποσκευών", "Την ακύρωση επειδή αρρωστήσατε", "Την ακύρωση επειδή απλώς αλλάξατε γνώμη"], 3, "Δεν καλύπτει όμως ακυρώσεις επειδή απλώς αλλάξατε γνώμη"),
  Q("Πότε πρέπει να γίνει η ασφάλεια;", ["Αμέσως μετά την κράτηση", "Την τελευταία εβδομάδα", "Στο αεροδρόμιο", "Όταν φτάσουν στην Ιαπωνία"], 0, "Καλύτερα τώρα, αμέσως μετά την κράτηση"),
 ],
 "gloss": {"ταξιδιωτικό γραφείο": "ταξιδιωτικό γραφείο — travel agency", "ασφάλεια": "ασφάλεια — insurance", "υποχρεωτική": "υποχρεωτικός — compulsory", "συνιστώ": "συνιστώ — to recommend", "καλύπτει": "καλύπτω — to cover", "απώλεια": "απώλεια — loss", "αποσκευών": "αποσκευή — luggage", "ακύρωση": "ακύρωση — cancellation", "κράτηση": "κράτηση — booking"}
})

ITEMS.append({
 "id": "l149-c1-kopose-apofaseon", "title": "Η κόπωση των αποφάσεων", "title_en": "Decision fatigue", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη ψυχολογίας για το ευρύ κοινό.",
 "script": [
  L("Ομιλήτρια", "f", "Κάθε μέρα παίρνουμε εκατοντάδες αποφάσεις, από το τι θα φορέσουμε μέχρι το τι θα απαντήσουμε σε ένα δύσκολο μήνυμα. Αρκετοί ψυχολόγοι υποστηρίζουν ότι οι αποφάσεις αυτές μάς εξαντλούν, όπως ένας μυς που κουράζεται από τη συνεχή χρήση. Το φαινόμενο έχει ονομαστεί «κόπωση των αποφάσεων».", "Every day we make hundreds of decisions, from what to wear to how to answer a difficult message. Quite a few psychologists argue that these decisions wear us out, like a muscle that tires from constant use. The phenomenon has been called 'decision fatigue'."),
  L("Ομιλήτρια", "f", "Η πιο διάσημη μελέτη στο θέμα εξέτασε αποφάσεις επιτροπών αποφυλάκισης στο Ισραήλ. Οι ερευνητές βρήκαν ότι οι ευνοϊκές αποφάσεις ήταν πολύ συχνότερες στην αρχή της μέρας και αμέσως μετά από ένα διάλειμμα για φαγητό, και μειώνονταν δραματικά όσο περνούσε η ώρα.", "The most famous study on the subject examined decisions by parole boards in Israel. The researchers found that favourable decisions were much more frequent at the start of the day and right after a meal break, and fell dramatically as time went on."),
  L("Ομιλήτρια", "f", "Οφείλω όμως να είμαι προσεκτική. Άλλοι ερευνητές υποστήριξαν ότι το αποτέλεσμα εξηγείται εν μέρει από τη σειρά με την οποία εξετάζονταν οι υποθέσεις. Και η γενικότερη θεωρία ότι η θέληση «αδειάζει» σαν μπαταρία δεν επιβεβαιώθηκε σε μεγάλα πειράματα επανάληψης.", "But I have to be careful. Other researchers argued that the result is partly explained by the order in which the cases were heard. And the broader theory that willpower 'runs down' like a battery was not confirmed in large replication experiments."),
  L("Ομιλήτρια", "f", "Τι κρατάμε λοιπόν; Ίσως όχι έναν νόμο της φύσης, αλλά μια πρακτική συμβουλή: τις σημαντικές αποφάσεις καλό είναι να τις παίρνουμε όταν είμαστε ξεκούραστοι, και τις μικρές, όπως το πρωινό ή τα ρούχα, να τις μετατρέπουμε σε ρουτίνα.", "So what do we take away? Perhaps not a law of nature, but a practical tip: it's good to make important decisions when we're rested, and to turn small ones, like breakfast or clothes, into routine."),
 ],
 "questions": [
  Q("Με τι συγκρίνουν ορισμένοι ψυχολόγοι την ικανότητα να παίρνουμε αποφάσεις;", ["Με μια μηχανή", "Με έναν μυ που κουράζεται από τη συνεχή χρήση", "Με ένα ποτάμι", "Με έναν υπολογιστή"], 1, "όπως ένας μυς που κουράζεται από τη συνεχή χρήση"),
  Q("Τι βρήκε η μελέτη για τις επιτροπές αποφυλάκισης;", ["Οι ευνοϊκές αποφάσεις ήταν συχνότερες στην αρχή της μέρας και μετά από διάλειμμα", "Οι αποφάσεις ήταν πάντα ίδιες", "Οι δικαστές αποφάσιζαν καλύτερα το βράδυ", "Το φαγητό δεν είχε καμία σχέση"], 0, "οι ευνοϊκές αποφάσεις ήταν πολύ συχνότερες στην αρχή της μέρας και αμέσως μετά από ένα διάλειμμα"),
  Q("Ποια αντίρρηση αναφέρει η ομιλήτρια;", ["Ότι η μελέτη έγινε σε λίγους ανθρώπους", "Ότι οι δικαστές ήξεραν για το πείραμα", "Ότι το αποτέλεσμα εξηγείται εν μέρει από τη σειρά με την οποία εξετάζονταν οι υποθέσεις", "Ότι τα στοιχεία χάθηκαν"], 2, "το αποτέλεσμα εξηγείται εν μέρει από τη σειρά με την οποία εξετάζονταν οι υποθέσεις"),
  Q("Ποια πρακτική συμβουλή δίνει στο τέλος;", ["Να αποφεύγουμε κάθε απόφαση", "Να τρώμε συχνότερα", "Να ζητάμε πάντα τη γνώμη άλλων", "Να παίρνουμε τις σημαντικές αποφάσεις ξεκούραστοι και να κάνουμε τις μικρές ρουτίνα"], 3, "τις σημαντικές αποφάσεις καλό είναι να τις παίρνουμε όταν είμαστε ξεκούραστοι"),
 ],
 "gloss": {"διάλεξη": "διάλεξη — lecture", "εξαντλούν": "εξαντλώ — to exhaust", "μυς": "μυς — muscle", "κόπωση": "κόπωση — fatigue", "αποφυλάκισης": "αποφυλάκιση — release from prison, parole", "ευνοϊκές": "ευνοϊκός — favourable", "διάλειμμα": "διάλειμμα — break", "θέληση": "θέληση — willpower", "επιβεβαιώθηκε": "επιβεβαιώνομαι — to be confirmed", "επανάληψης": "πείραμα επανάληψης — replication study", "ρουτίνα": "ρουτίνα — routine"}
})

ITEMS.append({
 "id": "l149-c1-psychologia-ouras", "title": "Η ψυχολογία της αναμονής", "title_en": "The psychology of waiting", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκπομπή με καλεσμένο έναν ερευνητή που μελετά την εμπειρία των πελατών.",
 "script": [
  L("Δημοσιογράφος", "f", "Γιατί μια αναμονή δέκα λεπτών μάς φαίνεται άλλοτε σύντομη και άλλοτε ατελείωτη;", "Why does a ten-minute wait sometimes feel short and sometimes endless?"),
  L("Ερευνητής", "m", "Γιατί δεν μετράμε τον χρόνο με ρολόι, αλλά με την εμπειρία μας. Ήδη από τη δεκαετία του '80 ένας σύμβουλος επιχειρήσεων, ο Ντέιβιντ Μάιστερ, διατύπωσε μερικές απλές αρχές. Ο χρόνος που περνάμε χωρίς να κάνουμε τίποτα φαίνεται μεγαλύτερος από τον απασχολημένο. Και η αβέβαιη αναμονή είναι πιο βασανιστική από αυτή που ξέρουμε πόσο θα κρατήσει.", "Because we don't measure time by the clock, but by our experience. As early as the '80s a business consultant, David Maister, set out a few simple principles. Time we spend doing nothing seems longer than occupied time. And an uncertain wait is more agonising than one we know the length of."),
  L("Δημοσιογράφος", "f", "Έχετε κάποιο παράδειγμα;", "Do you have an example?"),
  L("Ερευνητής", "m", "Αναφέρεται συχνά ένα αεροδρόμιο στο Χιούστον. Οι επιβάτες παραπονιούνταν ότι περίμεναν πολύ τις βαλίτσες τους. Αντί να επιταχύνει την παράδοση, το αεροδρόμιο μετέφερε τις αφίξεις πιο μακριά από τους ιμάντες, ώστε οι επιβάτες να περπατούν περισσότερο. Τα παράπονα, όπως λέγεται, σχεδόν εξαφανίστηκαν.", "An airport in Houston is often mentioned. Passengers complained that they waited a long time for their suitcases. Instead of speeding up delivery, the airport moved the arrivals further from the carousels, so passengers walked longer. The complaints, it is said, almost disappeared."),
  L("Δημοσιογράφος", "f", "Και η δικαιοσύνη παίζει ρόλο;", "And does fairness play a role?"),
  L("Ερευνητής", "m", "Τεράστιο. Μας ενοχλεί λιγότερο να περιμένουμε πολύ σε μια ενιαία ουρά, παρά να βλέπουμε τη διπλανή ουρά να προχωρά πιο γρήγορα. Γι' αυτό πολλές τράπεζες και ταχυδρομεία έχουν πια μία μόνο ουρά, που μοιράζεται στα γκισέ, ή σύστημα με αριθμούς προτεραιότητας.", "Enormous. It bothers us less to wait a long time in a single queue than to see the queue next to us moving faster. That's why many banks and post offices now have only one queue, which is divided among the counters, or a numbered ticket system."),
 ],
 "questions": [
  Q("Ποια από τις αρχές του Μάιστερ αναφέρει ο ερευνητής;", ["Ο απασχολημένος χρόνος φαίνεται μεγαλύτερος", "Η αβέβαιη αναμονή είναι πιο βασανιστική από τη γνωστή", "Οι άνθρωποι προτιμούν να περιμένουν μόνοι", "Η αναμονή είναι πιο εύκολη το πρωί"], 1, "η αβέβαιη αναμονή είναι πιο βασανιστική από αυτή που ξέρουμε πόσο θα κρατήσει"),
  Q("Τι έκανε, σύμφωνα με την ιστορία, το αεροδρόμιο του Χιούστον;", ["Πρόσθεσε υπαλλήλους", "Έβαλε οθόνες με ταινίες", "Μετέφερε τις αφίξεις πιο μακριά από τους ιμάντες", "Έδωσε κουπόνια στους επιβάτες"], 2, "μετέφερε τις αφίξεις πιο μακριά από τους ιμάντες"),
  Q("Πώς παρουσιάζει ο ερευνητής το αποτέλεσμα στο Χιούστον;", ["Ως κάτι που λέγεται, χωρίς απόλυτη βεβαιότητα", "Ως αποτυχία", "Ως επίσημη μελέτη με αριθμούς", "Ως κάτι που δεν έγινε ποτέ"], 0, "Τα παράπονα, όπως λέγεται, σχεδόν εξαφανίστηκαν"),
  Q("Γιατί πολλές τράπεζες έχουν μία μόνο ουρά;", ["Γιατί χωράει περισσότερους", "Γιατί είναι φθηνότερη", "Γιατί το απαιτεί ο νόμος", "Γιατί μας ενοχλεί να βλέπουμε τη διπλανή ουρά να προχωρά πιο γρήγορα"], 3, "να βλέπουμε τη διπλανή ουρά να προχωρά πιο γρήγορα"),
 ],
 "gloss": {"αναμονή": "αναμονή — waiting", "ατελείωτη": "ατελείωτος — endless", "διατύπωσε": "διατυπώνω — to formulate, set out", "αβέβαιη": "αβέβαιος — uncertain", "βασανιστική": "βασανιστικός — agonising", "επιταχύνει": "επιταχύνω — to speed up", "ιμάντες": "ιμάντας — (baggage) carousel, belt", "παράπονα": "παράπονο — complaint", "ενιαία": "ενιαίος — single, unified", "γκισέ": "γκισέ — counter (window)", "προτεραιότητας": "αριθμός προτεραιότητας — queue number"}
})

rnd = random.Random(149)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-149.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
