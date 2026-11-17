# Source for library/listening/listening-148.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l148.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l148-vm-anthopoleio", "title": "Η ανθοδέσμη για τον γάμο", "title_en": "The wedding bouquet", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από το ανθοπωλείο όπου παραγγείλατε λουλούδια για τον γάμο σας.",
 "script": [
  L("Ανθοπώλισσα", "f", "Καλησπέρα, από το ανθοπωλείο «Γαρδένια» σας τηλεφωνώ, για την ανθοδέσμη της νύφης. Δυστυχώς οι λευκές παιώνιες που διαλέξατε δεν θα έρθουν εγκαίρως από την Ολλανδία, λόγω μιας καθυστέρησης στις μεταφορές.", "Good evening, I'm calling from the Gardenia flower shop, about the bride's bouquet. Unfortunately the white peonies you chose won't arrive from the Netherlands in time, because of a delay in transport."),
  L("Ανθοπώλισσα", "f", "Σας προτείνω δύο λύσεις: λευκά τριαντάφυλλα κήπου, που μοιάζουν αρκετά με τις παιώνιες, ή λευκές ορτανσίες. Και τα δύο ταιριάζουν με τη διακόσμηση της εκκλησίας. Τη διαφορά στην τιμή δεν θα τη χρεωθείτε εσείς.", "I suggest two solutions: white garden roses, which look quite like peonies, or white hydrangeas. Both go with the church decoration. You won't be charged the difference in price."),
  L("Ανθοπώλισσα", "f", "Θα σας στείλω φωτογραφίες και από τα δύο στο κινητό. Χρειάζομαι την απάντησή σας μέχρι την Τετάρτη το μεσημέρι, για να προλάβω να τα παραγγείλω.", "I'll send you photos of both to your mobile. I need your answer by Wednesday noon, so I have time to order them."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα;", ["Το ανθοπωλείο θα είναι κλειστό", "Οι λευκές παιώνιες δεν θα έρθουν εγκαίρως", "Η εκκλησία άλλαξε", "Η τιμή ανέβηκε"], 1, "οι λευκές παιώνιες που διαλέξατε δεν θα έρθουν εγκαίρως"),
  Q("Τι ισχύει για τη διαφορά στην τιμή;", ["Θα την πληρώσετε εσείς", "Θα τη μοιραστείτε", "Δεν θα τη χρεωθείτε εσείς", "Θα την πληρώσει η εκκλησία"], 2, "Τη διαφορά στην τιμή δεν θα τη χρεωθείτε εσείς"),
  Q("Μέχρι πότε πρέπει να απαντήσετε;", ["Μέχρι την Τετάρτη το μεσημέρι", "Μέχρι αύριο το πρωί", "Μέχρι την ημέρα του γάμου", "Μέχρι το Σάββατο"], 0, "Χρειάζομαι την απάντησή σας μέχρι την Τετάρτη το μεσημέρι"),
 ],
 "gloss": {"ανθοπωλείο": "ανθοπωλείο — florist's", "ανθοδέσμη": "ανθοδέσμη — bouquet", "νύφης": "νύφη — bride", "παιώνιες": "παιώνια — peony", "εγκαίρως": "εγκαίρως — in time", "τριαντάφυλλα": "τριαντάφυλλο — rose", "ορτανσίες": "ορτανσία — hydrangea", "διακόσμηση": "διακόσμηση — decoration", "χρεωθείτε": "χρεώνομαι — to be charged"}
})

ITEMS.append({
 "id": "l148-ann-anoichtoi-kipoi", "title": "Η Μέρα των Ανοιχτών Κήπων", "title_en": "Open Gardens Day", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση στο ραδιόφωνο για μια πολιτιστική εκδήλωση στην πόλη σας.",
 "script": [
  L("Εκφωνήτρια", "f", "Την Κυριακή η πόλη γιορτάζει τη Μέρα των Ανοιχτών Κήπων. Δεκαπέντε ιδιωτικοί κήποι και αυλές θα μείνουν ανοιχτοί για το κοινό από τις δέκα το πρωί μέχρι τη δύση του ηλίου, με ελεύθερη είσοδο.", "On Sunday the city celebrates Open Gardens Day. Fifteen private gardens and courtyards will be open to the public from ten in the morning until sunset, with free entry."),
  L("Εκφωνήτρια", "f", "Σε πολλούς κήπους οι ιδιοκτήτες θα κάνουν ξεναγήσεις, ενώ θα υπάρχουν και εργαστήρια κηπουρικής για παιδιά. Για τις ξεναγήσεις χρειάζεται κράτηση θέσης στην ιστοσελίδα του δήμου, γιατί ο αριθμός των συμμετεχόντων είναι περιορισμένος.", "In many gardens the owners will give guided tours, and there will also be gardening workshops for children. For the guided tours you need to book a place on the municipality's website, because the number of participants is limited."),
  L("Εκφωνήτρια", "f", "Ένα δωρεάν λεωφορείο θα συνδέει τους κήπους ανά είκοσι λεπτά, με αφετηρία την κεντρική πλατεία. Παρακαλούνται οι επισκέπτες να μην κόβουν λουλούδια και να μη φέρνουν κατοικίδια.", "A free bus will link the gardens every twenty minutes, starting from the central square. Visitors are asked not to pick flowers and not to bring pets."),
 ],
 "questions": [
  Q("Πότε θα είναι ανοιχτοί οι κήποι;", ["Μόνο το απόγευμα", "Από τις δέκα το πρωί μέχρι τη δύση του ηλίου", "Όλη τη νύχτα", "Μόνο με κράτηση"], 1, "από τις δέκα το πρωί μέχρι τη δύση του ηλίου"),
  Q("Γιατί χρειάζεται κράτηση για τις ξεναγήσεις;", ["Γιατί κοστίζουν", "Γιατί γίνονται μόνο στα αγγλικά", "Γιατί ο αριθμός των συμμετεχόντων είναι περιορισμένος", "Γιατί είναι μόνο για παιδιά"], 2, "ο αριθμός των συμμετεχόντων είναι περιορισμένος"),
  Q("Τι παρακαλούνται να μην κάνουν οι επισκέπτες;", ["Να μην κόβουν λουλούδια", "Να μην έρχονται με λεωφορείο", "Να μη φωτογραφίζουν", "Να μη μιλούν στους ιδιοκτήτες"], 0, "να μην κόβουν λουλούδια"),
 ],
 "gloss": {"πολιτιστική": "πολιτιστικός — cultural", "ιδιωτικοί": "ιδιωτικός — private", "αυλές": "αυλή — courtyard", "δύση": "δύση — setting (of the sun)", "ξεναγήσεις": "ξενάγηση — guided tour", "κηπουρικής": "κηπουρική — gardening", "κράτηση": "κράτηση — booking", "περιορισμένος": "περιορισμένος — limited", "αφετηρία": "αφετηρία — starting point", "κατοικίδια": "κατοικίδιο — pet"}
})

ITEMS.append({
 "id": "l148-dia-allergia-gyri", "title": "Η αλλεργία της άνοιξης", "title_en": "Spring allergy", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο σε ένα ιατρείο ανάμεσα σε μια γιατρό και έναν ασθενή.",
 "script": [
  L("Ασθενής", "m", "Γιατρέ μου, κάθε άνοιξη τα ίδια: φτερνίζομαι συνέχεια, τρέχει η μύτη μου και τα μάτια μου κοκκινίζουν. Φέτος είναι χειρότερα από ποτέ.", "Doctor, every spring it's the same: I sneeze all the time, my nose runs and my eyes go red. This year it's worse than ever."),
  L("Γιατρός", "f", "Μοιάζει με αλλεργία στη γύρη. Για να είμαστε σίγουροι, θα κάνουμε δερματικά τεστ, που δείχνουν σε ποια φυτά είστε αλλεργικός. Μέχρι τότε, θα σας γράψω ένα αντιισταμινικό χάπι και ένα σπρέι για τη μύτη.", "It looks like a pollen allergy. To be sure, we'll do skin tests, which show which plants you're allergic to. Until then, I'll prescribe you an antihistamine pill and a nasal spray."),
  L("Ασθενής", "m", "Τα χάπια αυτά δεν φέρνουν υπνηλία; Οδηγώ πολλές ώρες για τη δουλειά.", "Don't these pills cause drowsiness? I drive for many hours for work."),
  L("Γιατρός", "f", "Τα νεότερα σπάνια φέρνουν υπνηλία, αλλά τις πρώτες μέρες προσέξτε πώς νιώθετε. Και κάτι πρακτικό: τα πρωινά, όταν η γύρη είναι περισσότερη, κρατήστε τα παράθυρα κλειστά, και όταν γυρίζετε σπίτι, κάντε ένα ντους και αλλάξτε ρούχα.", "The newer ones rarely cause drowsiness, but during the first days notice how you feel. And something practical: in the mornings, when there's more pollen, keep the windows closed, and when you get home, take a shower and change clothes."),
 ],
 "questions": [
  Q("Τι θα δείξουν τα δερματικά τεστ;", ["Σε ποια φυτά είναι αλλεργικός", "Αν έχει πυρετό", "Αν έχει κάποια λοίμωξη", "Αν πρέπει να χειρουργηθεί"], 0, "δείχνουν σε ποια φυτά είστε αλλεργικός"),
  Q("Γιατί ανησυχεί ο ασθενής για τα χάπια;", ["Γιατί είναι ακριβά", "Γιατί οδηγεί πολλές ώρες και φοβάται την υπνηλία", "Γιατί έχει αλλεργία στα φάρμακα", "Γιατί δεν του αρέσουν τα χάπια"], 1, "Οδηγώ πολλές ώρες για τη δουλειά"),
  Q("Τι τον συμβουλεύει να κάνει τα πρωινά;", ["Να κάνει γυμναστική έξω", "Να ανοίγει τα παράθυρα", "Να κρατάει τα παράθυρα κλειστά", "Να πίνει πολύ νερό"], 2, "κρατήστε τα παράθυρα κλειστά"),
 ],
 "gloss": {"φτερνίζομαι": "φτερνίζομαι — to sneeze", "κοκκινίζουν": "κοκκινίζω — to go red", "γύρη": "γύρη — pollen", "δερματικά": "δερματικός — skin", "αλλεργικός": "αλλεργικός — allergic", "αντιισταμινικό": "αντιισταμινικό — antihistamine", "σπρέι": "σπρέι — spray", "υπνηλία": "υπνηλία — drowsiness"}
})

ITEMS.append({
 "id": "l148-int-fotografos-gamou", "title": "Η φωτογράφος γάμων", "title_en": "The wedding photographer", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε μια ραδιοφωνική εκπομπή με μια φωτογράφο που φωτογραφίζει γάμους.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσους γάμους φωτογραφίζετε τον χρόνο;", "How many weddings do you photograph a year?"),
  L("Φωτογράφος", "f", "Γύρω στους σαράντα, οι περισσότεροι από τον Μάιο μέχρι τον Σεπτέμβριο. Το καλοκαίρι υπάρχουν Σαββατοκύριακα που έχω δύο γάμους, έναν το Σάββατο και έναν την Κυριακή, σε διαφορετικά νησιά.", "About forty, most of them from May to September. In summer there are weekends when I have two weddings, one on Saturday and one on Sunday, on different islands."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το πιο δύσκολο;", "What's the hardest part?"),
  L("Φωτογράφος", "f", "Ότι δεν υπάρχει δεύτερη ευκαιρία. Αν χάσεις τη στιγμή που ο πατέρας παραδίδει τη νύφη ή που ανταλλάσσονται τα στέφανα, δεν μπορείς να πεις «ξανακάντε το». Γι' αυτό έχω πάντα μαζί μου δύο μηχανές και πολλές μπαταρίες.", "That there's no second chance. If you miss the moment when the father gives away the bride or when the wedding crowns are exchanged, you can't say \"do it again\". That's why I always have two cameras and lots of batteries with me."),
  L("Δημοσιογράφος", "m", "Έχετε κάποια αγαπημένη φωτογραφία;", "Do you have a favourite photo?"),
  L("Φωτογράφος", "f", "Μια γιαγιά που χόρευε ξυπόλυτη στο τέλος της βραδιάς, με τα παπούτσια στο χέρι. Δεν ήταν η νύφη ούτε ο γαμπρός, αλλά όταν την είδαν, οι νεόνυμφοι τη διάλεξαν για το εξώφυλλο του άλμπουμ.", "A grandmother dancing barefoot at the end of the evening, with her shoes in her hand. She wasn't the bride or the groom, but when they saw it, the newlyweds chose it for the album cover."),
 ],
 "questions": [
  Q("Πότε γίνονται οι περισσότεροι γάμοι;", ["Από τον Μάιο μέχρι τον Σεπτέμβριο", "Τον χειμώνα", "Μόνο τον Αύγουστο", "Όλο τον χρόνο εξίσου"], 0, "οι περισσότεροι από τον Μάιο μέχρι τον Σεπτέμβριο"),
  Q("Γιατί έχει πάντα μαζί της δύο μηχανές;", ["Γιατί δουλεύει με βοηθό", "Γιατί δεν υπάρχει δεύτερη ευκαιρία", "Γιατί η μία είναι για βίντεο", "Γιατί το ζητούν οι πελάτες"], 1, "δεν υπάρχει δεύτερη ευκαιρία"),
  Q("Ποια φωτογραφία διάλεξαν οι νεόνυμφοι για το εξώφυλλο;", ["Τη φωτογραφία με τα στέφανα", "Τη φωτογραφία της νύφης με τον πατέρα της", "Μια γιαγιά που χόρευε ξυπόλυτη", "Μια φωτογραφία της εκκλησίας"], 2, "Μια γιαγιά που χόρευε ξυπόλυτη"),
 ],
 "gloss": {"φωτογραφίζει": "φωτογραφίζω — to photograph", "ευκαιρία": "ευκαιρία — chance", "παραδίδει": "παραδίδω — to give away, hand over", "στέφανα": "στέφανα — wedding crowns", "μηχανές": "μηχανή — camera", "ξυπόλυτη": "ξυπόλυτος — barefoot", "γαμπρός": "γαμπρός — groom", "νεόνυμφοι": "νεόνυμφος — newlywed", "εξώφυλλο": "εξώφυλλο — cover"}
})

ITEMS.append({
 "id": "l148-news-gyali", "title": "Κάδοι για το γυαλί σε κάθε γειτονιά", "title_en": "Glass bins in every neighbourhood", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός τοπικού ραδιοφώνου.",
 "script": [
  L("Εκφωνητής", "m", "Ο δήμος τοποθετεί από αυτή την εβδομάδα διακόσιους νέους κάδους ανακύκλωσης για το γυαλί, σε σχήμα καμπάνας, σε όλες τις γειτονιές της πόλης. Μέχρι τώρα, τα γυάλινα μπουκάλια και βάζα πετιούνταν μαζί με τα υπόλοιπα ανακυκλώσιμα, και πολλά έσπαγαν στη μεταφορά.", "From this week the municipality is installing two hundred new bell-shaped recycling bins for glass in all the city's neighbourhoods. Until now, glass bottles and jars were thrown away with the other recyclables, and many broke in transport."),
  L("Εκφωνητής", "m", "Οι κάτοικοι παρακαλούνται να αδειάζουν και να ξεπλένουν τα γυάλινα δοχεία πριν τα ρίξουν στον κάδο, και να μην πετούν εκεί καθρέφτες, ποτήρια ή λάμπες, γιατί είναι από διαφορετικό υλικό.", "Residents are asked to empty and rinse glass containers before throwing them in the bin, and not to throw mirrors, drinking glasses or light bulbs there, because they are made of a different material."),
  L("Εκφωνητής", "m", "Τα καταστήματα εστίασης θα έχουν δικούς τους κάδους, που θα αδειάζονται δύο φορές την εβδομάδα. Σύμφωνα με τον δήμο, το γυαλί μπορεί να ανακυκλωθεί ξανά και ξανά χωρίς να χάσει την ποιότητά του.", "Food and drink businesses will have their own bins, which will be emptied twice a week. According to the municipality, glass can be recycled again and again without losing its quality."),
 ],
 "questions": [
  Q("Τι πρόβλημα υπήρχε μέχρι τώρα;", ["Δεν υπήρχαν καθόλου κάδοι", "Τα γυάλινα πετιούνταν με τα υπόλοιπα ανακυκλώσιμα και πολλά έσπαγαν", "Οι κάτοικοι δεν ανακύκλωναν", "Οι κάδοι ήταν πολύ ακριβοί"], 1, "πολλά έσπαγαν στη μεταφορά"),
  Q("Τι δεν πρέπει να ρίχνουν οι κάτοικοι στους νέους κάδους;", ["Μπουκάλια κρασιού", "Βάζα από μαρμελάδα", "Καθρέφτες, ποτήρια ή λάμπες", "Μπουκάλια από λάδι"], 2, "να μην πετούν εκεί καθρέφτες, ποτήρια ή λάμπες"),
  Q("Τι ισχύει για το γυαλί σύμφωνα με τον δήμο;", ["Μπορεί να ανακυκλωθεί ξανά και ξανά χωρίς να χάσει την ποιότητά του", "Ανακυκλώνεται μόνο μία φορά", "Δεν ανακυκλώνεται", "Χάνει την ποιότητά του κάθε φορά"], 0, "το γυαλί μπορεί να ανακυκλωθεί ξανά και ξανά χωρίς να χάσει την ποιότητά του"),
 ],
 "gloss": {"κάδους": "κάδος — bin", "ανακύκλωσης": "ανακύκλωση — recycling", "καμπάνας": "καμπάνα — bell", "γυάλινα": "γυάλινος — glass", "ανακυκλώσιμα": "ανακυκλώσιμος — recyclable", "ξεπλένουν": "ξεπλένω — to rinse", "δοχεία": "δοχείο — container", "καθρέφτες": "καθρέφτης — mirror", "εστίασης": "εστίαση — food service, catering"}
})

ITEMS.append({
 "id": "l148-mon-magnitiki", "title": "Πριν από μια μαγνητική τομογραφία", "title_en": "Before an MRI scan", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια νοσηλεύτρια να δίνει οδηγίες σε έναν ασθενή πριν από μια εξέταση.",
 "script": [
  L("Νοσηλεύτρια", "f", "Πριν μπείτε στο μηχάνημα, πρέπει να βγάλετε όλα τα μεταλλικά αντικείμενα: κοσμήματα, ρολόι, ζώνη, ακόμα και τα κλειδιά από την τσέπη σας. Ο μαγνήτης είναι πολύ ισχυρός. Τα πράγματά σας θα μείνουν σε ένα ντουλαπάκι με κλειδί.", "Before you go into the machine, you must take off all metal objects: jewellery, watch, belt, even the keys from your pocket. The magnet is very strong. Your things will stay in a small locker with a key."),
  L("Νοσηλεύτρια", "f", "Αν έχετε βηματοδότη ή κάποιο μεταλλικό εμφύτευμα από επέμβαση, πρέπει να μου το πείτε τώρα. Η εξέταση κρατάει περίπου είκοσι λεπτά. Το μηχάνημα κάνει δυνατό θόρυβο, γι' αυτό θα σας δώσουμε ωτοασπίδες.", "If you have a pacemaker or a metal implant from an operation, you must tell me now. The examination lasts about twenty minutes. The machine makes a loud noise, so we'll give you earplugs."),
  L("Νοσηλεύτρια", "f", "Το πιο σημαντικό είναι να μείνετε εντελώς ακίνητος, αλλιώς οι εικόνες θα βγουν θολές. Αν νιώσετε άσχημα, πατήστε το κουμπί που θα κρατάτε στο χέρι, και θα σταματήσουμε αμέσως.", "The most important thing is to stay completely still, otherwise the images will come out blurred. If you feel unwell, press the button you'll be holding in your hand, and we'll stop immediately."),
 ],
 "questions": [
  Q("Γιατί πρέπει να βγάλει ο ασθενής τα μεταλλικά αντικείμενα;", ["Γιατί ο μαγνήτης είναι πολύ ισχυρός", "Για να μη χαθούν", "Γιατί κάνουν θόρυβο", "Γιατί είναι βαριά"], 0, "Ο μαγνήτης είναι πολύ ισχυρός"),
  Q("Γιατί θα του δώσουν ωτοασπίδες;", ["Για να κοιμηθεί", "Γιατί το μηχάνημα κάνει δυνατό θόρυβο", "Για να μην ακούει τη νοσηλεύτρια", "Γιατί κάνει κρύο"], 1, "Το μηχάνημα κάνει δυνατό θόρυβο"),
  Q("Τι θα γίνει αν ο ασθενής κουνηθεί;", ["Η εξέταση θα κρατήσει λιγότερο", "Θα πρέπει να πληρώσει ξανά", "Οι εικόνες θα βγουν θολές", "Το μηχάνημα θα σταματήσει μόνο του"], 2, "οι εικόνες θα βγουν θολές"),
 ],
 "gloss": {"μεταλλικά": "μεταλλικός — metal", "κοσμήματα": "κόσμημα — jewellery", "μαγνήτης": "μαγνήτης — magnet", "ντουλαπάκι": "ντουλαπάκι — small locker", "βηματοδότη": "βηματοδότης — pacemaker", "εμφύτευμα": "εμφύτευμα — implant", "επέμβαση": "επέμβαση — operation", "ωτοασπίδες": "ωτοασπίδα — earplug", "θολές": "θολός — blurred"}
})

ITEMS.append({
 "id": "l148-rep-katafygia", "title": "Γεμάτα τα ορειβατικά καταφύγια", "title_en": "Mountain refuges are full", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για τον τουρισμό.",
 "script": [
  L("Ρεπόρτερ", "m", "Τα ορειβατικά καταφύγια, που άλλοτε φιλοξενούσαν κυρίως έμπειρους ορειβάτες, γεμίζουν πλέον κάθε Σαββατοκύριακο από οικογένειες και νέους. Σε ορισμένα καταφύγια του Ολύμπου, οι κρατήσεις για τον Αύγουστο κλείνουν από τον Μάρτιο.", "Mountain refuges, which once mainly hosted experienced climbers, now fill up every weekend with families and young people. In some refuges on Olympus, bookings for August are full by March."),
  L("Ρεπόρτερ", "m", "Ο φύλακας ενός καταφυγίου μάς είπε ότι η αύξηση είναι ευχάριστη, αλλά φέρνει και προβλήματα. Πολλοί επισκέπτες έρχονται χωρίς κατάλληλα παπούτσια ή χωρίς ζεστά ρούχα, νομίζοντας ότι επειδή είναι καλοκαίρι, κάνει ζέστη και στα δύο χιλιάδες μέτρα.", "The warden of one refuge told us that the increase is welcome, but it also brings problems. Many visitors come without suitable shoes or warm clothes, thinking that because it's summer, it's warm at two thousand metres too."),
  L("Ρεπόρτερ", "m", "Οι ορειβατικοί σύλλογοι συνιστούν να κλείνετε θέση από πριν, να ελέγχετε τον καιρό και να ενημερώνετε κάποιον για τη διαδρομή σας. Και να θυμάστε ότι στο καταφύγιο δεν υπάρχει ρεύμα όλη μέρα, οπότε ένας φακός είναι απαραίτητος.", "Mountaineering clubs advise you to book a place in advance, check the weather and tell someone about your route. And to remember that in the refuge there isn't electricity all day, so a torch is essential."),
 ],
 "questions": [
  Q("Τι έχει αλλάξει στα καταφύγια;", ["Γεμίζουν πλέον από οικογένειες και νέους", "Έκλεισαν πολλά", "Έγιναν ακριβότερα", "Τα επισκέπτονται μόνο ξένοι"], 0, "γεμίζουν πλέον κάθε Σαββατοκύριακο από οικογένειες και νέους"),
  Q("Ποιο πρόβλημα αναφέρει ο φύλακας;", ["Ότι δεν υπάρχει νερό", "Ότι πολλοί έρχονται χωρίς κατάλληλα παπούτσια ή ζεστά ρούχα", "Ότι οι επισκέπτες κάνουν θόρυβο", "Ότι δεν πληρώνουν"], 1, "Πολλοί επισκέπτες έρχονται χωρίς κατάλληλα παπούτσια"),
  Q("Γιατί είναι απαραίτητος ένας φακός;", ["Για τις νυχτερινές πεζοπορίες", "Για να βρίσκουν το μονοπάτι", "Γιατί στο καταφύγιο δεν υπάρχει ρεύμα όλη μέρα", "Γιατί το ζητάει ο φύλακας"], 2, "στο καταφύγιο δεν υπάρχει ρεύμα όλη μέρα"),
 ],
 "gloss": {"ορειβατικά": "ορειβατικός — mountaineering", "καταφύγια": "καταφύγιο — refuge, shelter", "φιλοξενούσαν": "φιλοξενώ — to host", "ορειβάτες": "ορειβάτης — climber", "κρατήσεις": "κράτηση — booking", "φύλακας": "φύλακας — warden", "κατάλληλα": "κατάλληλος — suitable", "συνιστούν": "συνιστώ — to recommend", "φακός": "φακός — torch"}
})

ITEMS.append({
 "id": "l148-dia-podilato-aggelia", "title": "Ένα μεταχειρισμένο ποδήλατο", "title_en": "A second-hand bike", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο ανάμεσα σε έναν αγοραστή και μια πωλήτρια που έβαλε αγγελία στο διαδίκτυο.",
 "script": [
  L("Αγοραστής", "m", "Καλησπέρα, για το ποδήλατο της αγγελίας. Στη φωτογραφία φαινόταν σαν καινούργιο. Γιατί το πουλάτε;", "Good evening, about the bike in the ad. In the photo it looked brand new. Why are you selling it?"),
  L("Πωλήτρια", "f", "Το αγόρασα πριν από δύο χρόνια για να πηγαίνω στη δουλειά, αλλά τώρα μετακόμισα και η δουλειά είναι πολύ μακριά. Το έχω χρησιμοποιήσει ελάχιστα. Μπορείτε να κάνετε μια βόλτα στο τετράγωνο, να το δοκιμάσετε.", "I bought it two years ago to go to work, but now I've moved and work is too far. I've used it very little. You can ride it round the block to try it."),
  L("Αγοραστής", "m", "Ωραίο είναι, αλλά τα φρένα πιάνουν λίγο αργά, και η αλυσίδα θέλει λάδωμα. Θα κάνατε κάτι στην τιμή; Θα χρειαστεί να το πάω για σέρβις.", "It's nice, but the brakes engage a bit late, and the chain needs oiling. Would you do something on the price? I'll need to take it for a service."),
  L("Πωλήτρια", "f", "Η τιμή στην αγγελία είναι διακόσια ευρώ. Ας πούμε εκατόν ογδόντα, και σας δίνω μαζί και την κλειδαριά και τα φώτα, που τα αγόρασα χωριστά.", "The price in the ad is two hundred euros. Let's say a hundred and eighty, and I'll give you the lock and the lights too, which I bought separately."),
 ],
 "questions": [
  Q("Γιατί πουλάει η γυναίκα το ποδήλατο;", ["Γιατί χάλασε", "Γιατί μετακόμισε και η δουλειά είναι πολύ μακριά", "Γιατί αγόρασε αυτοκίνητο", "Γιατί είναι μικρό για εκείνη"], 1, "τώρα μετακόμισα και η δουλειά είναι πολύ μακριά"),
  Q("Τι πρόβλημα βρίσκει ο αγοραστής;", ["Τα φρένα πιάνουν αργά και η αλυσίδα θέλει λάδωμα", "Το λάστιχο είναι τρύπιο", "Λείπει η σέλα", "Είναι πολύ βαρύ"], 0, "τα φρένα πιάνουν λίγο αργά, και η αλυσίδα θέλει λάδωμα"),
  Q("Τι του προτείνει η πωλήτρια;", ["Να το πληρώσει σε δόσεις", "Να το φέρει πίσω αν δεν του αρέσει", "Εκατόν ογδόντα ευρώ μαζί με την κλειδαριά και τα φώτα", "Διακόσια ευρώ χωρίς έκπτωση"], 2, "Ας πούμε εκατόν ογδόντα, και σας δίνω μαζί και την κλειδαριά και τα φώτα"),
 ],
 "gloss": {"αγγελία": "αγγελία — ad", "μετακόμισα": "μετακομίζω — to move house", "ελάχιστα": "ελάχιστα — very little", "τετράγωνο": "τετράγωνο — block", "φρένα": "φρένο — brake", "αλυσίδα": "αλυσίδα — chain", "λάδωμα": "λάδωμα — oiling", "σέρβις": "σέρβις — service", "κλειδαριά": "κλειδαριά — lock"}
})

ITEMS.append({
 "id": "l148-c1-anosia-agelis", "title": "Η ανοσία της αγέλης", "title_en": "Herd immunity", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια ομιλία για τη δημόσια υγεία.",
 "script": [
  L("Ομιλήτρια", "f", "Όταν ένα μεγάλο μέρος ενός πληθυσμού έχει ανοσία σε μια μεταδοτική ασθένεια, είτε επειδή έχει εμβολιαστεί είτε επειδή έχει νοσήσει, ο μικροοργανισμός δυσκολεύεται να βρει νέους ξενιστές. Οι αλυσίδες της μετάδοσης σπάνε, και έτσι προστατεύονται έμμεσα και όσοι δεν έχουν ανοσία.", "When a large part of a population is immune to an infectious disease, either because it has been vaccinated or because it has had the disease, the microorganism has difficulty finding new hosts. The chains of transmission break, and so even those who are not immune are indirectly protected."),
  L("Ομιλήτρια", "f", "Αυτό είναι κρίσιμο για ανθρώπους που δεν μπορούν να εμβολιαστούν, όπως τα πολύ μικρά βρέφη ή ασθενείς με εξασθενημένο ανοσοποιητικό σύστημα. Η προστασία τους εξαρτάται, κυριολεκτικά, από τη συμπεριφορά των άλλων.", "This is critical for people who cannot be vaccinated, such as very young infants or patients with a weakened immune system. Their protection depends, literally, on the behaviour of others."),
  L("Ομιλήτρια", "f", "Το ποσοστό που χρειάζεται δεν είναι το ίδιο για όλες τις ασθένειες. Εξαρτάται από το πόσο μεταδοτική είναι η καθεμία. Για την ιλαρά, που είναι από τις πιο μεταδοτικές, οι ειδικοί εκτιμούν ότι χρειάζεται ανοσία περίπου στο ενενήντα πέντε τοις εκατό του πληθυσμού.", "The percentage needed is not the same for all diseases. It depends on how infectious each one is. For measles, which is one of the most infectious, experts estimate that immunity is needed in about ninety-five per cent of the population."),
  L("Ομιλήτρια", "f", "Γι' αυτό ακόμα και μια μικρή πτώση στα ποσοστά εμβολιασμού μπορεί να οδηγήσει σε νέα κρούσματα ασθενειών που θεωρούσαμε ότι ανήκουν στο παρελθόν. Η ανοσία της αγέλης είναι, με αυτή την έννοια, ένα κοινό αγαθό, που το χτίζουμε όλοι μαζί.", "That's why even a small drop in vaccination rates can lead to new cases of diseases we thought belonged to the past. Herd immunity is, in this sense, a common good, which we all build together."),
 ],
 "questions": [
  Q("Πώς προστατεύονται όσοι δεν έχουν ανοσία;", ["Με ειδικά φάρμακα", "Έμμεσα, επειδή σπάνε οι αλυσίδες της μετάδοσης", "Μένοντας στο σπίτι", "Δεν προστατεύονται"], 1, "προστατεύονται έμμεσα και όσοι δεν έχουν ανοσία"),
  Q("Για ποιους είναι κρίσιμη η ανοσία της αγέλης;", ["Για τους αθλητές", "Για τους γιατρούς", "Για όσους δεν μπορούν να εμβολιαστούν, όπως τα πολύ μικρά βρέφη", "Για τους ταξιδιώτες"], 2, "για ανθρώπους που δεν μπορούν να εμβολιαστούν"),
  Q("Από τι εξαρτάται το ποσοστό ανοσίας που χρειάζεται;", ["Από το πόσο μεταδοτική είναι η ασθένεια", "Από την εποχή του χρόνου", "Από το μέγεθος της χώρας", "Από την ηλικία των ασθενών"], 0, "Εξαρτάται από το πόσο μεταδοτική είναι η καθεμία"),
  Q("Τι μπορεί να προκαλέσει μια μικρή πτώση στα ποσοστά εμβολιασμού;", ["Τίποτα σημαντικό", "Ακριβότερα εμβόλια", "Νέες ασθένειες", "Νέα κρούσματα ασθενειών που θεωρούσαμε ότι ανήκουν στο παρελθόν"], 3, "νέα κρούσματα ασθενειών που θεωρούσαμε ότι ανήκουν στο παρελθόν"),
 ],
 "gloss": {"ανοσία": "ανοσία — immunity", "μεταδοτική": "μεταδοτικός — infectious", "εμβολιαστεί": "εμβολιάζομαι — to be vaccinated", "νοσήσει": "νοσώ — to fall ill", "ξενιστές": "ξενιστής — host (biology)", "έμμεσα": "έμμεσα — indirectly", "βρέφη": "βρέφος — infant", "εξασθενημένο": "εξασθενημένος — weakened", "ανοσοποιητικό σύστημα": "ανοσοποιητικό σύστημα — immune system", "ιλαρά": "ιλαρά — measles", "κρούσματα": "κρούσμα — case (of a disease)", "αγαθό": "αγαθό — good"}
})

ITEMS.append({
 "id": "l148-c1-nocebo", "title": "Το φαινόμενο νοσίμπο", "title_en": "The nocebo effect", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκπομπή για την ιατρική, με καλεσμένο έναν φαρμακολόγο.",
 "script": [
  L("Δημοσιογράφος", "f", "Όλοι ξέρουμε το φαινόμενο πλασίμπο. Τι είναι όμως το «νοσίμπο»;", "We all know the placebo effect. But what is the \"nocebo\"?"),
  L("Φαρμακολόγος", "m", "Είναι η σκοτεινή του πλευρά. Ενώ στο πλασίμπο μια αδρανής ουσία βελτιώνει τα συμπτώματα επειδή περιμένουμε να μας κάνει καλό, στο νοσίμπο εμφανίζονται δυσάρεστα συμπτώματα επειδή περιμένουμε κάτι κακό. Η λέξη προέρχεται από τα λατινικά και σημαίνει «θα βλάψω».", "It's its dark side. While with the placebo an inactive substance improves symptoms because we expect it to do us good, with the nocebo unpleasant symptoms appear because we expect something bad. The word comes from Latin and means \"I will harm\"."),
  L("Δημοσιογράφος", "f", "Μπορείτε να δώσετε ένα παράδειγμα;", "Can you give an example?"),
  L("Φαρμακολόγος", "m", "Σε κλινικές μελέτες, ένα σημαντικό ποσοστό των ασθενών που παίρνουν χάπι χωρίς δραστική ουσία αναφέρουν παρενέργειες: πονοκέφαλο, ζάλη, κούραση. Συχνά μάλιστα πρόκειται για τις ίδιες παρενέργειες που διάβασαν στο φύλλο οδηγιών. Έχει παρατηρηθεί επίσης ότι ορισμένοι ασθενείς σταματούν ένα φάρμακο λόγω συμπτωμάτων που είναι, σε μεγάλο βαθμό, αποτέλεσμα της ανησυχίας τους.", "In clinical trials, a significant proportion of patients who take a pill without an active ingredient report side effects: headache, dizziness, tiredness. Often, in fact, these are the same side effects they read in the package leaflet. It has also been observed that some patients stop a drug because of symptoms that are, to a large extent, the result of their anxiety."),
  L("Δημοσιογράφος", "f", "Αυτό σημαίνει ότι οι γιατροί δεν πρέπει να ενημερώνουν για τις παρενέργειες;", "Does that mean doctors shouldn't inform about side effects?"),
  L("Φαρμακολόγος", "m", "Σε καμία περίπτωση. Η ενημέρωση είναι υποχρέωση. Μετράει όμως ο τρόπος: αν πεις «το ενενήντα τοις εκατό των ασθενών δεν έχει κανένα πρόβλημα» αντί για «ένας στους δέκα παθαίνει ζάλη», η πληροφορία είναι η ίδια, αλλά η επίδραση στον ασθενή μπορεί να είναι πολύ διαφορετική.", "By no means. Informing is an obligation. But the way matters: if you say \"ninety per cent of patients have no problem at all\" instead of \"one in ten gets dizzy\", the information is the same, but the effect on the patient can be very different."),
 ],
 "questions": [
  Q("Τι είναι το φαινόμενο νοσίμπο;", ["Η εμφάνιση δυσάρεστων συμπτωμάτων επειδή περιμένουμε κάτι κακό", "Ένα νέο φάρμακο", "Η βελτίωση των συμπτωμάτων με αδρανή ουσία", "Μια σπάνια αλλεργία"], 0, "εμφανίζονται δυσάρεστα συμπτώματα επειδή περιμένουμε κάτι κακό"),
  Q("Τι συμβαίνει συχνά με τις παρενέργειες στις κλινικές μελέτες;", ["Δεν εμφανίζονται ποτέ", "Είναι οι ίδιες με αυτές που διάβασαν οι ασθενείς στο φύλλο οδηγιών", "Είναι πάντα σοβαρές", "Εμφανίζονται μόνο στους ηλικιωμένους"], 1, "πρόκειται για τις ίδιες παρενέργειες που διάβασαν στο φύλλο οδηγιών"),
  Q("Πρέπει οι γιατροί να ενημερώνουν για τις παρενέργειες, κατά τον φαρμακολόγο;", ["Όχι, γιατί προκαλούν άγχος", "Μόνο αν το ζητήσει ο ασθενής", "Ναι, η ενημέρωση είναι υποχρέωση", "Μόνο γραπτώς"], 2, "Η ενημέρωση είναι υποχρέωση"),
  Q("Τι δείχνει το παράδειγμα με το «ενενήντα τοις εκατό»;", ["Ότι οι αριθμοί δεν έχουν σημασία", "Ότι οι ασθενείς δεν καταλαβαίνουν τα ποσοστά", "Ότι οι γιατροί κρύβουν πληροφορίες", "Ότι ο τρόπος που δίνεται η πληροφορία επηρεάζει τον ασθενή"], 3, "η επίδραση στον ασθενή μπορεί να είναι πολύ διαφορετική"),
 ],
 "gloss": {"φαρμακολόγο": "φαρμακολόγος — pharmacologist", "πλασίμπο": "πλασίμπο — placebo", "αδρανής": "αδρανής — inactive, inert", "συμπτώματα": "σύμπτωμα — symptom", "δυσάρεστα": "δυσάρεστος — unpleasant", "κλινικές μελέτες": "κλινική μελέτη — clinical trial", "δραστική ουσία": "δραστική ουσία — active ingredient", "παρενέργειες": "παρενέργεια — side effect", "ζάλη": "ζάλη — dizziness", "φύλλο οδηγιών": "φύλλο οδηγιών — package leaflet", "υποχρέωση": "υποχρέωση — obligation"}
})

rnd = random.Random(148)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-148.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
