# Source for library/listening/listening-65.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l65.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l65-ann-gipedo", "title": "Οδηγίες για την έξοδο από το γήπεδο", "title_en": "Instructions for leaving the stadium", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα γήπεδο ποδοσφαίρου λίγο πριν από το τέλος του αγώνα. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί φίλαθλοι, ο αγώνας ολοκληρώνεται σε λίγα λεπτά. Για λόγους ασφαλείας, οι φίλαθλοι της φιλοξενούμενης ομάδας παρακαλούνται να παραμείνουν στις θέσεις τους για είκοσι λεπτά μετά το τελικό σφύριγμα, μέχρι να τους δοθεί οδηγία από την αστυνομία.", "Dear fans, the match will finish in a few minutes. For safety reasons, supporters of the visiting team are asked to stay in their seats for twenty minutes after the final whistle, until they are given instructions by the police."),
  L("Εκφωνήτρια", "f", "Οι υπόλοιποι θεατές μπορούν να χρησιμοποιήσουν όλες τις εξόδους, εκτός από την Πύλη 7, που θα παραμείνει κλειστή. Ο σταθμός του μετρό θα λειτουργεί με έκτακτα δρομολόγια μέχρι τη μία μετά τα μεσάνυχτα.", "The other spectators may use all the exits except Gate 7, which will remain closed. The metro station will run extra trains until one o'clock after midnight."),
  L("Εκφωνήτρια", "f", "Υπενθυμίζουμε ότι η χρήση καπνογόνων απαγορεύεται αυστηρά και επισύρει πρόστιμο στην ομάδα. Σας ευχαριστούμε και καλή επιστροφή στα σπίτια σας.", "We remind you that the use of flares is strictly forbidden and results in a fine for the club. Thank you, and have a safe journey home."),
 ],
 "questions": [
  Q("Τι πρέπει να κάνουν οι φίλαθλοι της φιλοξενούμενης ομάδας;", ["Να φύγουν πριν από το τελικό σφύριγμα", "Να βγουν από την Πύλη 7", "Να παραμείνουν στις θέσεις τους για είκοσι λεπτά", "Να πάνε κατευθείαν στο μετρό"], 2, "να παραμείνουν στις θέσεις τους για είκοσι λεπτά μετά το τελικό σφύριγμα"),
  Q("Ποια έξοδος θα μείνει κλειστή;", ["Η Πύλη 1", "Η Πύλη 7", "Όλες οι έξοδοι", "Η έξοδος προς το μετρό"], 1, "εκτός από την Πύλη 7, που θα παραμείνει κλειστή"),
  Q("Μέχρι πότε θα λειτουργεί ο σταθμός του μετρό;", ["Μέχρι τις έντεκα", "Μέχρι τα μεσάνυχτα", "Μέχρι τη μία μετά τα μεσάνυχτα", "Όλη τη νύχτα"], 2, "με έκτακτα δρομολόγια μέχρι τη μία μετά τα μεσάνυχτα"),
 ],
 "gloss": {"φίλαθλοι": "φίλαθλος — sports fan", "φιλοξενούμενης": "φιλοξενούμενος — visiting (team)", "τελικό σφύριγμα": "τελικό σφύριγμα — final whistle", "έκτακτα δρομολόγια": "έκτακτο δρομολόγιο — extra service", "καπνογόνων": "καπνογόνο — flare, smoke bomb", "επισύρει": "επισύρω — to incur, result in"},
})

ITEMS.append({
 "id": "l65-vm-service", "title": "Μήνυμα από το συνεργείο της αντιπροσωπείας", "title_en": "A message from the dealership garage", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε αφήσει το αυτοκίνητό σας για σέρβις. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Τεχνικός", "m", "Καλημέρα σας, κύριε Παπαδάκη, σας τηλεφωνώ από το συνεργείο της αντιπροσωπείας για το αυτοκίνητό σας. Το σέρβις έχει ολοκληρωθεί, αλλά στον έλεγχο διαπιστώσαμε ότι τα τακάκια στα μπροστινά φρένα έχουν φθαρεί αρκετά.", "Good morning, Mr Papadakis, I'm calling from the dealership garage about your car. The service is finished, but during the check we found that the pads on the front brakes are quite worn."),
  L("Τεχνικός", "m", "Η αλλαγή κοστίζει εκατόν είκοσι ευρώ, μαζί με τα εργατικά. Θα χρειαστούμε όμως την έγκρισή σας τηλεφωνικά πριν από τις πέντε, για να προλάβουμε να τα αλλάξουμε σήμερα. Αλλιώς, το αυτοκίνητο θα είναι έτοιμο αύριο χωρίς την αλλαγή, και μπορείτε να το φέρετε άλλη φορά.", "Replacing them costs one hundred and twenty euros, including labour. But we'll need your approval by phone before five so that we can change them today. Otherwise, the car will be ready tomorrow without the change, and you can bring it in another time."),
  L("Τεχνικός", "m", "Σας θυμίζω ότι το Σάββατο είμαστε ανοιχτά μέχρι τις δύο. Ευχαριστώ.", "Just a reminder that on Saturday we're open until two. Thank you."),
 ],
 "questions": [
  Q("Τι διαπίστωσαν στον έλεγχο;", ["Ότι η μπαταρία είναι άδεια", "Ότι τα τακάκια στα μπροστινά φρένα έχουν φθαρεί", "Ότι τα λάστιχα πρέπει να αλλάξουν", "Ότι το αυτοκίνητο δεν έχει κανένα πρόβλημα"], 1, "τα τακάκια στα μπροστινά φρένα έχουν φθαρεί αρκετά"),
  Q("Τι πρέπει να κάνει ο κύριος Παπαδάκης για να γίνει η αλλαγή σήμερα;", ["Να πληρώσει online", "Να περάσει από το συνεργείο", "Να δώσει την έγκρισή του τηλεφωνικά πριν από τις πέντε", "Να στείλει email"], 2, "την έγκρισή σας τηλεφωνικά πριν από τις πέντε"),
  Q("Τι θα γίνει, αν δεν απαντήσει;", ["Το αυτοκίνητο θα είναι έτοιμο αύριο χωρίς την αλλαγή", "Η αλλαγή θα γίνει έτσι κι αλλιώς", "Το αυτοκίνητο θα μείνει στο συνεργείο μέχρι το Σάββατο", "Θα πληρώσει πρόστιμο"], 0, "το αυτοκίνητο θα είναι έτοιμο αύριο χωρίς την αλλαγή"),
 ],
 "gloss": {"αντιπροσωπείας": "αντιπροσωπεία — dealership", "τακάκια": "τακάκι — brake pad", "φρένα": "φρένο — brake", "έχουν φθαρεί": "φθείρομαι — to wear out", "εργατικά": "εργατικά — labour (cost)", "έγκρισή": "έγκριση — approval"},
})

ITEMS.append({
 "id": "l65-dia-diakopi-gym", "title": "Θέλω να σταματήσω το γυμναστήριο", "title_en": "I want to cancel my gym membership", "type": "dialogue", "level": "B2",
 "context_el": "Μια πελάτισσα μιλά με τον υπάλληλο της ρεσεψιόν σε ένα γυμναστήριο.",
 "script": [
  L("Πελάτισσα", "f", "Καλησπέρα. Θα ήθελα να διακόψω τη συνδρομή μου. Μετακομίζω στη Θεσσαλονίκη για δουλειά τον επόμενο μήνα.", "Good evening. I'd like to cancel my membership. I'm moving to Thessaloniki for work next month."),
  L("Υπάλληλος", "m", "Λυπάμαι που θα σας χάσουμε. Βλέπω ότι έχετε ετήσιο συμβόλαιο, που λήγει τον Μάρτιο. Σε περίπτωση πρόωρης διακοπής, προβλέπεται ρήτρα ίση με δύο μηνιαίες συνδρομές.", "I'm sorry we'll lose you. I see you have an annual contract that runs until March. For early cancellation, there's a penalty equal to two monthly fees."),
  L("Πελάτισσα", "f", "Δύο μήνες; Μα δεν φεύγω επειδή το θέλω. Η εταιρεία με μεταθέτει.", "Two months? But I'm not leaving because I want to. My company is transferring me."),
  L("Υπάλληλος", "m", "Μπορούμε να σας προτείνουμε πάγωμα της συνδρομής για τρεις μήνες. Αν, όμως, μας φέρετε μια βεβαίωση από τον εργοδότη σας για τη μετάθεση, η διακοπή γίνεται χωρίς καμία χρέωση.", "We can offer to freeze your membership for three months. But if you bring us a certificate from your employer about the transfer, cancellation is free of charge."),
  L("Πελάτισσα", "f", "Τέλεια. Θα τη ζητήσω αύριο από το λογιστήριο και θα σας τη φέρω μέσα στην εβδομάδα.", "Perfect. I'll ask the accounts department for it tomorrow and bring it in during the week."),
 ],
 "questions": [
  Q("Γιατί θέλει η πελάτισσα να διακόψει τη συνδρομή;", ["Γιατί δεν της αρέσει το γυμναστήριο", "Γιατί μετακομίζει στη Θεσσαλονίκη για δουλειά", "Γιατί είναι ακριβή", "Γιατί τραυματίστηκε"], 1, "Μετακομίζω στη Θεσσαλονίκη για δουλειά τον επόμενο μήνα"),
  Q("Τι προβλέπεται σε περίπτωση πρόωρης διακοπής;", ["Τίποτα", "Ρήτρα ίση με δύο μηνιαίες συνδρομές", "Ρήτρα ίση με μία ετήσια συνδρομή", "Ένας μήνας δωρεάν"], 1, "προβλέπεται ρήτρα ίση με δύο μηνιαίες συνδρομές"),
  Q("Πώς μπορεί να διακόψει χωρίς χρέωση;", ["Αν παγώσει τη συνδρομή", "Αν πληρώσει μετρητά", "Αν φέρει βεβαίωση από τον εργοδότη της για τη μετάθεση", "Αν φέρει μια φίλη στο γυμναστήριο"], 2, "μια βεβαίωση από τον εργοδότη σας για τη μετάθεση"),
 ],
 "gloss": {"διακόψω": "διακόπτω — to discontinue, cancel", "λήγει": "λήγω — to expire, end", "πρόωρης": "πρόωρος — early, premature", "ρήτρα": "ρήτρα — penalty clause", "με μεταθέτει": "μεταθέτω — to transfer (an employee)", "πάγωμα": "πάγωμα — freezing (of a membership)", "βεβαίωση": "βεβαίωση — certificate, written confirmation", "λογιστήριο": "λογιστήριο — accounts department"},
})

ITEMS.append({
 "id": "l65-dia-pascha-arni", "title": "Ποιος θα φέρει το αρνί;", "title_en": "Who's bringing the lamb?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο αδέρφια οργανώνουν το Πάσχα της οικογένειας στο χωριό.",
 "script": [
  L("Ελένη", "f", "Λοιπόν, ας τα κανονίσουμε από τώρα, για να μην τρέχουμε τη Μεγάλη Εβδομάδα. Το αρνί θα το πάρεις εσύ από τον χασάπη του χωριού;", "Right, let's sort it out now so we're not rushing around in Holy Week. Will you get the lamb from the village butcher?"),
  L("Κώστας", "m", "Ναι, το έχω ήδη παραγγείλει. Θα φέρω και τα σπλάχνα για το κοκορέτσι. Η σούβλα, όμως, χρειάζεται καινούργιο μοτέρ. Το παλιό κάηκε πέρσι.", "Yes, I've already ordered it. I'll bring the offal for the kokoretsi too. But the spit needs a new motor. The old one burned out last year."),
  L("Ελένη", "f", "Εντάξει, θα το αγοράσω εγώ στην Αθήνα. Τα αυγά θα τα βάψουμε με τη μαμά τη Μεγάλη Πέμπτη, όπως πάντα, και τη μαγειρίτσα θα την ετοιμάσει εκείνη για μετά την Ανάσταση.", "OK, I'll buy it in Athens. We'll dye the eggs with Mum on Holy Thursday, as always, and she'll make the mayiritsa for after the Resurrection service."),
  L("Κώστας", "m", "Και οι καρέκλες; Πέρσι ήμασταν είκοσι άτομα και κάποιοι έφαγαν όρθιοι.", "And the chairs? Last year there were twenty of us and some people ate standing up."),
  L("Ελένη", "f", "Θα ζητήσουμε από τον πρόεδρο του χωριού να μας δανείσει από τον πολιτιστικό σύλλογο. Τα τραπέζια τα έχουμε.", "We'll ask the village head to lend us some from the cultural association. We've got the tables."),
 ],
 "questions": [
  Q("Τι πρέπει να αγοραστεί για τη σούβλα;", ["Καινούργια σούβλα", "Κάρβουνα", "Καινούργιο μοτέρ", "Τίποτα"], 2, "Η σούβλα, όμως, χρειάζεται καινούργιο μοτέρ"),
  Q("Πότε θα βάψουν τα αυγά;", ["Το Μεγάλο Σάββατο", "Τη Μεγάλη Πέμπτη", "Την Κυριακή του Πάσχα", "Τη Μεγάλη Παρασκευή"], 1, "Τα αυγά θα τα βάψουμε με τη μαμά τη Μεγάλη Πέμπτη"),
  Q("Πώς θα λύσουν το πρόβλημα με τις καρέκλες;", ["Θα αγοράσουν καινούργιες", "Θα ζητήσουν να δανειστούν από τον πολιτιστικό σύλλογο", "Θα φάνε όλοι όρθιοι", "Θα καλέσουν λιγότερους"], 1, "να μας δανείσει από τον πολιτιστικό σύλλογο"),
 ],
 "gloss": {"Μεγάλη Εβδομάδα": "Μεγάλη Εβδομάδα — Holy Week", "χασάπη": "χασάπης — butcher", "σπλάχνα": "σπλάχνα — offal, innards", "κοκορέτσι": "κοκορέτσι — spit-roasted offal wrapped in intestines", "σούβλα": "σούβλα — spit (for roasting)", "μαγειρίτσα": "μαγειρίτσα — Easter soup eaten after the midnight service", "Ανάσταση": "Ανάσταση — the Resurrection (midnight Easter service)", "πολιτιστικό σύλλογο": "πολιτιστικός σύλλογος — cultural association"},
})

ITEMS.append({
 "id": "l65-int-santouras", "title": "Ο κατασκευαστής σαντουριών", "title_en": "The santouri maker", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή, μια δημοσιογράφος μιλά με έναν κατασκευαστή μουσικών οργάνων.",
 "script": [
  L("Δημοσιογράφος", "f", "Το εργαστήριό σας είναι γεμάτο σαντούρια σε κάθε στάδιο κατασκευής. Πόσο καιρό χρειάζεται για να φτιάξετε ένα;", "Your workshop is full of santouris at every stage of construction. How long does it take you to make one?"),
  L("Κατασκευαστής", "m", "Περίπου δύο μήνες, αν όλα πάνε καλά. Το ξύλο πρέπει πρώτα να έχει ξεραθεί σωστά, αλλιώς το όργανο δεν κρατάει το κούρδισμα. Για τον σκελετό χρησιμοποιώ καρυδιά, και για το καπάκι έλατο, που δίνει καθαρό ήχο.", "About two months, if everything goes well. The wood must first have been properly dried, otherwise the instrument won't stay in tune. For the frame I use walnut, and for the soundboard fir, which gives a clear sound."),
  L("Δημοσιογράφος", "f", "Πώς ήρθε το σαντούρι στην Ελλάδα;", "How did the santouri come to Greece?"),
  L("Κατασκευαστής", "m", "Ήταν πολύ αγαπητό στη Σμύρνη και στην Πόλη. Με τους πρόσφυγες του 1922 διαδόθηκε σε όλη τη χώρα, και σήμερα το ακούμε και στα νησιά και στα δημοτικά της ηπειρωτικής Ελλάδας. Το πιο κουραστικό κομμάτι είναι το κούρδισμα: ένα σαντούρι έχει πάνω από εκατό χορδές.", "It was very popular in Smyrna and Constantinople. With the refugees of 1922 it spread all over the country, and today we hear it both on the islands and in the folk music of mainland Greece. The most tiring part is tuning: a santouri has more than a hundred strings."),
 ],
 "questions": [
  Q("Γιατί πρέπει το ξύλο να έχει ξεραθεί σωστά;", ["Για να είναι πιο ελαφρύ", "Για να κρατάει το όργανο το κούρδισμα", "Για να έχει ωραίο χρώμα", "Για να κοστίζει λιγότερο"], 1, "αλλιώς το όργανο δεν κρατάει το κούρδισμα"),
  Q("Από ποιο ξύλο φτιάχνει το καπάκι;", ["Από καρυδιά", "Από έλατο", "Από βελανιδιά", "Από πεύκο"], 1, "για το καπάκι έλατο, που δίνει καθαρό ήχο"),
  Q("Πώς διαδόθηκε το σαντούρι σε όλη την Ελλάδα;", ["Από τους ναυτικούς", "Μέσα από το ραδιόφωνο", "Με τους πρόσφυγες του 1922", "Από τα σχολεία μουσικής"], 2, "Με τους πρόσφυγες του 1922 διαδόθηκε σε όλη τη χώρα"),
 ],
 "gloss": {"σαντούρια": "σαντούρι — santouri (hammered dulcimer)", "εργαστήριό": "εργαστήριο — workshop", "κούρδισμα": "κούρδισμα — tuning", "σκελετό": "σκελετός — frame", "καρυδιά": "καρυδιά — walnut (tree, wood)", "καπάκι": "καπάκι — soundboard, lid", "έλατο": "έλατο — fir", "διαδόθηκε": "διαδίδομαι — to spread", "χορδές": "χορδή — string"},
})

ITEMS.append({
 "id": "l65-rep-asteroskopeio", "title": "Το Αστεροσκοπείο Αθηνών", "title_en": "The Athens Observatory", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από μια εκπομπή για την ιστορία της Αθήνας.",
 "script": [
  L("Ρεπόρτερ", "f", "Βρισκόμαστε στον Λόφο των Νυμφών, απέναντι από την Ακρόπολη. Εδώ βρίσκεται το Αστεροσκοπείο Αθηνών, το παλαιότερο ερευνητικό ίδρυμα της σύγχρονης Ελλάδας. Ο θεμέλιος λίθος του τοποθετήθηκε το 1842, με χρήματα του ευεργέτη Γεωργίου Σίνα.", "We're on the Hill of the Nymphs, opposite the Acropolis. This is the site of the Athens Observatory, the oldest research institution in modern Greece. Its foundation stone was laid in 1842, with money from the benefactor Georgios Sinas."),
  L("Ρεπόρτερ", "f", "Το κομψό νεοκλασικό κτίριο σχεδίασε ο Δανός αρχιτέκτονας Θεόφιλος Χάνσεν. Η αρχική του αποστολή ήταν οι αστρονομικές παρατηρήσεις, αλλά με τα χρόνια το ίδρυμα επεκτάθηκε και στη μετεωρολογία και στη σεισμολογία.", "The elegant neoclassical building was designed by the Danish architect Theophil Hansen. Its original mission was astronomical observation, but over the years the institution expanded into meteorology and seismology too."),
  L("Ρεπόρτερ", "f", "Σήμερα οι μεγάλες έρευνες γίνονται σε σταθμούς μακριά από τα φώτα της πόλης. Το ιστορικό κτίριο, όμως, παραμένει ανοιχτό για το κοινό: στο κέντρο επισκεπτών, οι επισκέπτες μπορούν να παρατηρήσουν τον ουρανό από ένα ιστορικό τηλεσκόπιο τις καθαρές νύχτες.", "Today the major research is carried out at stations far from the city lights. The historic building, however, remains open to the public: at the visitor centre, people can observe the sky through a historic telescope on clear nights."),
 ],
 "questions": [
  Q("Τι ξεχωρίζει το Αστεροσκοπείο Αθηνών;", ["Είναι το μεγαλύτερο της Ευρώπης", "Είναι το παλαιότερο ερευνητικό ίδρυμα της σύγχρονης Ελλάδας", "Βρίσκεται πάνω στην Ακρόπολη", "Χτίστηκε τον 20ό αιώνα"], 1, "το παλαιότερο ερευνητικό ίδρυμα της σύγχρονης Ελλάδας"),
  Q("Ποιος σχεδίασε το κτίριο;", ["Ο Γεώργιος Σίνας", "Ένας Γερμανός αστρονόμος", "Ο Δανός αρχιτέκτονας Θεόφιλος Χάνσεν", "Ένας Έλληνας μηχανικός"], 2, "σχεδίασε ο Δανός αρχιτέκτονας Θεόφιλος Χάνσεν"),
  Q("Πού γίνονται σήμερα οι μεγάλες έρευνες;", ["Στο ιστορικό κτίριο", "Σε σταθμούς μακριά από τα φώτα της πόλης", "Στο εξωτερικό μόνο", "Στο κέντρο επισκεπτών"], 1, "σε σταθμούς μακριά από τα φώτα της πόλης"),
 ],
 "gloss": {"Λόφο των Νυμφών": "Λόφος των Νυμφών — Hill of the Nymphs (Athens)", "ερευνητικό ίδρυμα": "ερευνητικό ίδρυμα — research institution", "θεμέλιος λίθος": "θεμέλιος λίθος — foundation stone", "ευεργέτη": "ευεργέτης — benefactor", "νεοκλασικό": "νεοκλασικός — neoclassical", "σεισμολογία": "σεισμολογία — seismology", "τηλεσκόπιο": "τηλεσκόπιο — telescope"},
})

ITEMS.append({
 "id": "l65-dia-fakoi-epafis", "title": "Φακοί επαφής για πρώτη φορά", "title_en": "Contact lenses for the first time", "type": "dialogue", "level": "B2",
 "context_el": "Ένας νεαρός άντρας μιλά με μια οπτικό σε ένα κατάστημα οπτικών.",
 "script": [
  L("Πελάτης", "m", "Φοράω γυαλιά χρόνια, αλλά παίζω μπάσκετ και θα ήθελα να δοκιμάσω φακούς επαφής.", "I've worn glasses for years, but I play basketball and I'd like to try contact lenses."),
  L("Οπτικός", "f", "Πολύ καλή ιδέα για τον αθλητισμό. Για αρχάριους προτείνω ημερήσιους φακούς: τους φοράτε μία μέρα και τους πετάτε, οπότε δεν χρειάζεται καθαρισμός. Είναι λίγο πιο ακριβοί από τους μηνιαίους, αλλά πιο υγιεινοί.", "A very good idea for sport. For beginners I recommend daily lenses: you wear them for one day and throw them away, so they don't need cleaning. They're a little more expensive than monthly ones, but more hygienic."),
  L("Πελάτης", "m", "Υπάρχει κάτι που πρέπει να προσέχω;", "Is there anything I need to be careful about?"),
  L("Οπτικός", "f", "Δύο πράγματα. Ποτέ μην κοιμάστε με τους φακούς, και ποτέ μην τους ξεπλένετε με νερό της βρύσης. Και πάντα να πλένετε τα χέρια σας πριν τους βάλετε. Θα σας δώσω ένα δοκιμαστικό ζευγάρι και θα σας δω ξανά σε μια εβδομάδα, να δούμε πώς τα πάτε.", "Two things. Never sleep in your lenses, and never rinse them with tap water. And always wash your hands before putting them in. I'll give you a trial pair and see you again in a week to see how you're getting on."),
 ],
 "questions": [
  Q("Γιατί θέλει ο πελάτης φακούς επαφής;", ["Γιατί έσπασαν τα γυαλιά του", "Γιατί παίζει μπάσκετ", "Γιατί είναι φθηνότεροι", "Γιατί του το είπε ο γιατρός"], 1, "παίζω μπάσκετ και θα ήθελα να δοκιμάσω φακούς επαφής"),
  Q("Τι ισχύει για τους ημερήσιους φακούς, σύμφωνα με την οπτικό;", ["Είναι φθηνότεροι από τους μηνιαίους", "Χρειάζονται καθημερινό καθαρισμό", "Δεν χρειάζονται καθαρισμό και είναι πιο υγιεινοί", "Μπορεί κανείς να κοιμάται με αυτούς"], 2, "δεν χρειάζεται καθαρισμός"),
  Q("Τι δεν πρέπει να κάνει ποτέ ο πελάτης;", ["Να πλένει τα χέρια του", "Να ξεπλένει τους φακούς με νερό της βρύσης", "Να φοράει τους φακούς στο μπάσκετ", "Να επιστρέψει σε μια εβδομάδα"], 1, "ποτέ μην τους ξεπλένετε με νερό της βρύσης"),
 ],
 "gloss": {"οπτικό": "οπτικός — optician", "φακούς επαφής": "φακός επαφής — contact lens", "αρχάριους": "αρχάριος — beginner", "ημερήσιους": "ημερήσιος — daily", "υγιεινοί": "υγιεινός — hygienic, healthy", "ξεπλένετε": "ξεπλένω — to rinse", "δοκιμαστικό": "δοκιμαστικός — trial"},
})

ITEMS.append({
 "id": "l65-mono-imerologio", "title": "Γιατί κρατάω ημερολόγιο", "title_en": "Why I keep a diary", "type": "monologue", "level": "B2",
 "context_el": "Σε ένα podcast για τις καθημερινές συνήθειες, μια γυναίκα μιλά για το ημερολόγιό της.",
 "script": [
  L("Αλεξάνδρα", "f", "Κρατάω ημερολόγιο από τα δεκαπέντε μου, δηλαδή εδώ και είκοσι χρόνια. Δεν γράφω σελίδες ολόκληρες. Κάθε βράδυ, πριν κοιμηθώ, σημειώνω τρεις γραμμές: τι έγινε, πώς ένιωσα και ένα πράγμα για το οποίο είμαι ευγνώμων.", "I've kept a diary since I was fifteen, so for twenty years now. I don't write whole pages. Every night, before I go to sleep, I note down three lines: what happened, how I felt and one thing I'm grateful for."),
  L("Αλεξάνδρα", "f", "Γράφω πάντα με το χέρι, σε τετράδιο. Το έχω δοκιμάσει στο κινητό, αλλά δεν είναι το ίδιο: με το χέρι γράφω πιο αργά και σκέφτομαι περισσότερο αυτό που γράφω.", "I always write by hand, in a notebook. I've tried it on my phone, but it's not the same: by hand I write more slowly and think more about what I'm writing."),
  L("Αλεξάνδρα", "f", "Κάθε χρόνο, στα γενέθλιά μου, ξαναδιαβάζω τις σελίδες της προηγούμενης χρονιάς. Έτσι έχω καταλάβει πολλά για τον εαυτό μου: για παράδειγμα, ότι κάθε Νοέμβριο έχω τις ίδιες ανησυχίες, που τελικά δεν βγαίνουν ποτέ αληθινές.", "Every year, on my birthday, I reread the pages from the previous year. That way I've understood a lot about myself: for example, that every November I have the same worries, which in the end never come true."),
 ],
 "questions": [
  Q("Τι γράφει η Αλεξάνδρα κάθε βράδυ;", ["Μια ολόκληρη σελίδα", "Τρεις γραμμές", "Μόνο τα ραντεβού της", "Ένα ποίημα"], 1, "σημειώνω τρεις γραμμές"),
  Q("Γιατί προτιμά να γράφει με το χέρι;", ["Γιατί δεν έχει κινητό", "Γιατί γράφει πιο αργά και σκέφτεται περισσότερο", "Γιατί είναι πιο γρήγορο", "Γιατί της το πρότεινε ένας φίλος"], 1, "με το χέρι γράφω πιο αργά και σκέφτομαι περισσότερο αυτό που γράφω"),
  Q("Τι έχει καταλάβει ξαναδιαβάζοντας το ημερολόγιό της;", ["Ότι ο Νοέμβριος είναι ο αγαπημένος της μήνας", "Ότι κάθε Νοέμβριο έχει τις ίδιες ανησυχίες, που δεν βγαίνουν αληθινές", "Ότι πρέπει να γράφει περισσότερο", "Ότι δεν θυμάται τίποτα από την προηγούμενη χρονιά"], 1, "κάθε Νοέμβριο έχω τις ίδιες ανησυχίες, που τελικά δεν βγαίνουν ποτέ αληθινές"),
 ],
 "gloss": {"ημερολόγιο": "ημερολόγιο — diary", "ευγνώμων": "ευγνώμων — grateful", "τετράδιο": "τετράδιο — notebook", "ξαναδιαβάζω": "ξαναδιαβάζω — to reread", "ανησυχίες": "ανησυχία — worry", "βγαίνουν ποτέ αληθινές": "βγαίνω αληθινός — to come true"},
})

ITEMS.append({
 "id": "l65-c1-klimatiki-metanastefsi", "title": "Η κλιματική μετανάστευση", "title_en": "Climate migration", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή λόγου, μια δημοσιογράφος συζητά με έναν ερευνητή για τη μετανάστευση που προκαλεί η κλιματική αλλαγή.",
 "script": [
  L("Δημοσιογράφος", "f", "Ακούμε όλο και συχνότερα τον όρο «κλιματικοί πρόσφυγες». Είναι ακριβής;", "We hear the term 'climate refugees' more and more often. Is it accurate?"),
  L("Ερευνητής", "m", "Από νομική άποψη, όχι. Η Σύμβαση της Γενεύης του 1951 αναγνωρίζει ως πρόσφυγες όσους διώκονται, για παράδειγμα για τη θρησκεία ή τις πολιτικές τους απόψεις. Η ξηρασία ή η άνοδος της στάθμης της θάλασσας δεν περιλαμβάνονται. Γι’ αυτό οι ειδικοί προτιμούν τον όρο «κλιματική μετανάστευση» ή «εκτοπισμός».", "Legally speaking, no. The 1951 Geneva Convention recognises as refugees those who are persecuted, for instance for their religion or political views. Drought or rising sea levels are not included. That's why experts prefer the term 'climate migration' or 'displacement'."),
  L("Δημοσιογράφος", "f", "Και πού πηγαίνουν αυτοί οι άνθρωποι;", "And where do these people go?"),
  L("Ερευνητής", "m", "Εδώ υπάρχει μια μεγάλη παρανόηση. Η συντριπτική πλειονότητα δεν διασχίζει σύνορα· μετακινείται μέσα στη χώρα της, συνήθως από την ύπαιθρο προς τις πόλεις. Πρέπει επίσης να διακρίνουμε τις ξαφνικές καταστροφές, όπως οι πλημμύρες, από τις αργές διεργασίες, όπως η ερημοποίηση, που απομακρύνουν τους ανθρώπους σταδιακά και σχεδόν αθόρυβα.", "Here there's a big misconception. The overwhelming majority don't cross borders; they move within their own country, usually from the countryside to the cities. We also have to distinguish sudden disasters, such as floods, from slow processes, such as desertification, which push people away gradually and almost silently."),
  L("Ερευνητής", "m", "Και η Ελλάδα δεν είναι ανεπηρέαστη. Μετά από μεγάλες πυρκαγιές και πλημμύρες, κάποιες οικογένειες δεν επέστρεψαν ποτέ στα χωριά τους. Το ζητούμενο είναι να επενδύσουμε στην προσαρμογή, ώστε η μετακίνηση να είναι επιλογή και όχι αναγκαστική φυγή.", "And Greece isn't unaffected. After major fires and floods, some families never returned to their villages. What matters is investing in adaptation, so that moving is a choice and not a forced flight."),
 ],
 "questions": [
  Q("Γιατί ο όρος «κλιματικοί πρόσφυγες» δεν είναι νομικά ακριβής;", ["Γιατί η κλιματική αλλαγή δεν προκαλεί μετακινήσεις", "Γιατί η Σύμβαση της Γενεύης δεν περιλαμβάνει την ξηρασία ή την άνοδο της στάθμης της θάλασσας", "Γιατί τον απαγορεύει ο ΟΗΕ", "Γιατί αφορά μόνο την Ευρώπη"], 1, "Η ξηρασία ή η άνοδος της στάθμης της θάλασσας δεν περιλαμβάνονται"),
  Q("Ποια είναι η «μεγάλη παρανόηση», σύμφωνα με τον ερευνητή;", ["Ότι οι περισσότεροι διασχίζουν σύνορα, ενώ στην πραγματικότητα μετακινούνται μέσα στη χώρα τους", "Ότι οι πλημμύρες είναι πιο επικίνδυνες από την ξηρασία", "Ότι οι πόλεις δεν επηρεάζονται", "Ότι η μετανάστευση είναι πάντα επιλογή"], 0, "Η συντριπτική πλειονότητα δεν διασχίζει σύνορα· μετακινείται μέσα στη χώρα της"),
  Q("Πώς χαρακτηρίζει τις αργές διεργασίες, όπως η ερημοποίηση;", ["Ως ακίνδυνες", "Ως πιο γρήγορες από τις πλημμύρες", "Ως διεργασίες που απομακρύνουν τους ανθρώπους σταδιακά και σχεδόν αθόρυβα", "Ως φαινόμενα που αφορούν μόνο τις πόλεις"], 2, "απομακρύνουν τους ανθρώπους σταδιακά και σχεδόν αθόρυβα"),
  Q("Ποιο είναι, κατά τη γνώμη του, το ζητούμενο;", ["Να κλείσουν τα σύνορα", "Να επενδύσουμε στην προσαρμογή, ώστε η μετακίνηση να είναι επιλογή", "Να χτιστούν νέες πόλεις", "Να επιστρέψουν όλοι στα χωριά τους"], 1, "να επενδύσουμε στην προσαρμογή, ώστε η μετακίνηση να είναι επιλογή και όχι αναγκαστική φυγή"),
 ],
 "gloss": {"διώκονται": "διώκομαι — to be persecuted", "στάθμης": "στάθμη — level (of water)", "εκτοπισμός": "εκτοπισμός — displacement", "παρανόηση": "παρανόηση — misconception", "συντριπτική πλειονότητα": "συντριπτική πλειονότητα — overwhelming majority", "ύπαιθρο": "ύπαιθρος — countryside", "διεργασίες": "διεργασία — process", "ερημοποίηση": "ερημοποίηση — desertification", "ανεπηρέαστη": "ανεπηρέαστος — unaffected", "προσαρμογή": "προσαρμογή — adaptation"},
})

ITEMS.append({
 "id": "l65-c1-trikoupis", "title": "Χαρίλαος Τρικούπης", "title_en": "Charilaos Trikoupis", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από διάλεξη ιστορικού για τον Χαρίλαο Τρικούπη και την εποχή του.",
 "script": [
  L("Ιστορικός", "f", "Το 1874 ο Χαρίλαος Τρικούπης δημοσίευσε στην εφημερίδα «Καιροί» ένα άρθρο με τον τίτλο «Τις πταίει;», δηλαδή «Ποιος φταίει;». Σε αυτό κατηγορούσε τον βασιλιά ότι διόριζε κυβερνήσεις που δεν είχαν την εμπιστοσύνη της Βουλής. Το άρθρο τού κόστισε τη σύλληψη, αλλά ένα χρόνο αργότερα ο Γεώργιος Α΄ αναγνώρισε την αρχή της δεδηλωμένης: ο βασιλιάς θα έδινε την εντολή σχηματισμού κυβέρνησης στον αρχηγό της κοινοβουλευτικής πλειοψηφίας.", "In 1874 Charilaos Trikoupis published an article in the newspaper Kairoi with the title 'Tis ptaiei?', that is, 'Who is to blame?'. In it he accused the king of appointing governments that did not have the confidence of Parliament. The article cost him his arrest, but a year later George I recognised the principle of the declared majority: the king would give the mandate to form a government to the leader of the parliamentary majority."),
  L("Ιστορικός", "f", "Ως πρωθυπουργός, ο Τρικούπης οραματίστηκε ένα σύγχρονο ευρωπαϊκό κράτος. Επέκτεινε το σιδηροδρομικό δίκτυο, κατασκεύασε δρόμους και ξεκίνησε τη διάνοιξη της Διώρυγας της Κορίνθου, που ολοκληρώθηκε το 1893. Τα έργα αυτά όμως χρηματοδοτήθηκαν με βαριά φορολογία και με εξωτερικά δάνεια.", "As prime minister, Trikoupis envisioned a modern European state. He expanded the railway network, built roads and started the cutting of the Corinth Canal, which was completed in 1893. But these works were financed with heavy taxation and foreign loans."),
  L("Ιστορικός", "f", "Το ίδιο έτος, το 1893, η χώρα σταμάτησε να εξυπηρετεί το εξωτερικό της χρέος. Η φράση «Δυστυχώς επτωχεύσαμεν», που του αποδίδεται, έμεινε παροιμιώδης. Δύο χρόνια αργότερα ηττήθηκε στις εκλογές και αποσύρθηκε από την πολιτική. Πέθανε το 1896 στις Κάννες. Η αποτίμηση του έργου του παραμένει διχασμένη: εκσυγχρονιστής για κάποιους, υπεύθυνος για την καταστροφή για άλλους.", "That same year, 1893, the country stopped servicing its foreign debt. The phrase 'Unfortunately, we are bankrupt', which is attributed to him, became proverbial. Two years later he was defeated in the elections and withdrew from politics. He died in 1896 in Cannes. The assessment of his work remains divided: a moderniser to some, responsible for the disaster to others."),
 ],
 "questions": [
  Q("Τι υποστήριζε ο Τρικούπης στο άρθρο «Τις πταίει;»;", ["Ότι η χώρα χρειαζόταν περισσότερους σιδηροδρόμους", "Ότι ο βασιλιάς διόριζε κυβερνήσεις χωρίς την εμπιστοσύνη της Βουλής", "Ότι έπρεπε να καταργηθεί η μοναρχία", "Ότι οι φόροι ήταν πολύ υψηλοί"], 1, "κατηγορούσε τον βασιλιά ότι διόριζε κυβερνήσεις που δεν είχαν την εμπιστοσύνη της Βουλής"),
  Q("Τι προέβλεπε η αρχή της δεδηλωμένης;", ["Ότι ο βασιλιάς θα έδινε την εντολή στον αρχηγό της κοινοβουλευτικής πλειοψηφίας", "Ότι οι εκλογές θα γίνονταν κάθε χρόνο", "Ότι η Βουλή θα εξέλεγε τον βασιλιά", "Ότι ο πρωθυπουργός θα ήταν ισόβιος"], 0, "ο βασιλιάς θα έδινε την εντολή σχηματισμού κυβέρνησης στον αρχηγό της κοινοβουλευτικής πλειοψηφίας"),
  Q("Πώς χρηματοδοτήθηκαν τα μεγάλα έργα;", ["Με δωρεές ευεργετών", "Με βαριά φορολογία και εξωτερικά δάνεια", "Με τα έσοδα των σιδηροδρόμων", "Με κονδύλια από την Ευρώπη"], 1, "χρηματοδοτήθηκαν με βαριά φορολογία και με εξωτερικά δάνεια"),
  Q("Πώς αποτιμάται σήμερα το έργο του;", ["Όλοι τον θεωρούν ήρωα", "Όλοι τον θεωρούν υπεύθυνο για την καταστροφή", "Η αποτίμηση παραμένει διχασμένη", "Έχει ξεχαστεί εντελώς"], 2, "Η αποτίμηση του έργου του παραμένει διχασμένη"),
 ],
 "gloss": {"πταίει": "πταίω (λόγιο) — to be at fault", "διόριζε": "διορίζω — to appoint", "σύλληψη": "σύλληψη — arrest", "αρχή της δεδηλωμένης": "αρχή της δεδηλωμένης — principle of the declared (parliamentary) majority", "κοινοβουλευτικής πλειοψηφίας": "κοινοβουλευτική πλειοψηφία — parliamentary majority", "οραματίστηκε": "οραματίζομαι — to envision", "διάνοιξη": "διάνοιξη — cutting, opening (of a canal, road)", "εξυπηρετεί": "εξυπηρετώ (χρέος) — to service (a debt)", "επτωχεύσαμεν": "πτωχεύω (λόγιο) — to go bankrupt", "παροιμιώδης": "παροιμιώδης — proverbial", "αποτίμηση": "αποτίμηση — assessment"},
})

rnd = random.Random(65)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-65.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
