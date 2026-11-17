# Source for library/listening/listening-155.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l155.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l155-vm-diorthoseis", "title": "Οι διορθώσεις του βιβλίου σας", "title_en": "The proofs of your book", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον εκδοτικό οίκο που θα εκδώσει το βιβλίο σας.",
 "script": [
  L("Επιμελήτρια", "f", "Καλησπέρα, η Δανάη είμαι, η επιμελήτρια του βιβλίου σας. Σας έστειλα σήμερα με email τις πρώτες διορθώσεις. Θα δείτε ότι έχω σημειώσει με κόκκινο κάποιες προτάσεις που μου φάνηκαν λίγο μεγάλες, αλλά η τελική απόφαση είναι δική σας.", "Good evening, it's Danai, the editor of your book. I sent you the first proofs by email today. You'll see that I've marked in red some sentences that seemed a bit long to me, but the final decision is yours."),
  L("Επιμελήτρια", "f", "Θα σας παρακαλούσα να μου τις επιστρέψετε μέχρι την Παρασκευή, γιατί το τυπογραφείο μάς έχει δώσει ημερομηνία για τις αρχές του επόμενου μήνα και δεν θέλουμε να τη χάσουμε.", "I'd ask you to send them back to me by Friday, because the printer has given us a date at the beginning of next month and we don't want to miss it."),
  L("Επιμελήτρια", "f", "Κάτι ακόμα: ο γραφίστας ετοίμασε δύο προτάσεις για το εξώφυλλο. Αν μπορείτε, περάστε από τον εκδοτικό οίκο την Τετάρτη το απόγευμα να τις δούμε μαζί. Αν δεν σας βολεύει, πείτε μου και θα σας τις στείλω.", "One more thing: the graphic designer has prepared two proposals for the cover. If you can, drop by the publishing house on Wednesday afternoon so we can look at them together. If that doesn't suit you, tell me and I'll send them to you."),
 ],
 "questions": [
  Q("Τι έχει σημειώσει η επιμελήτρια με κόκκινο;", ["Ορθογραφικά λάθη", "Κάποιες προτάσεις που της φάνηκαν λίγο μεγάλες", "Ολόκληρα κεφάλαια που πρέπει να φύγουν", "Τα ονόματα των ηρώων"], 1, "έχω σημειώσει με κόκκινο κάποιες προτάσεις που μου φάνηκαν λίγο μεγάλες"),
  Q("Γιατί πρέπει να επιστραφούν οι διορθώσεις μέχρι την Παρασκευή;", ["Γιατί το τυπογραφείο έχει δώσει ημερομηνία για τις αρχές του επόμενου μήνα", "Γιατί η επιμελήτρια φεύγει για διακοπές", "Γιατί υπάρχει μια έκθεση βιβλίου", "Γιατί αλλιώς θα πληρώσουν πρόστιμο"], 0, "το τυπογραφείο μάς έχει δώσει ημερομηνία για τις αρχές του επόμενου μήνα"),
  Q("Γιατί σας ζητάει να περάσετε την Τετάρτη;", ["Για να υπογράψετε το συμβόλαιο", "Για να γνωρίσετε τον εκδότη", "Για να δείτε μαζί τις δύο προτάσεις για το εξώφυλλο", "Για να παραλάβετε τα πρώτα αντίτυπα"], 2, "περάστε από τον εκδοτικό οίκο την Τετάρτη το απόγευμα να τις δούμε μαζί"),
 ],
 "gloss": {"επιμελήτρια": "επιμελήτρια — (copy) editor", "διορθώσεις": "διορθώσεις — corrections, proofs", "τελική": "τελικός — final", "τυπογραφείο": "τυπογραφείο — printing house", "γραφίστας": "γραφίστας — graphic designer", "εξώφυλλο": "εξώφυλλο — book cover", "εκδοτικό οίκο": "εκδοτικός οίκος — publishing house", "βολεύει": "βολεύει — it suits, is convenient"}
})

ITEMS.append({
 "id": "l155-ann-garaz-ploiou", "title": "Ανακοίνωση για το γκαράζ του πλοίου", "title_en": "An announcement about the ship's car deck", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός πλοίου, λίγο μετά την αναχώρηση.",
 "script": [
  L("Αξιωματικός", "m", "Κυρίες και κύριοι, καλησπέρα σας. Σας υπενθυμίζουμε ότι, για λόγους ασφαλείας, απαγορεύεται η παραμονή επιβατών στο γκαράζ του πλοίου κατά τη διάρκεια του ταξιδιού. Παρακαλούμε, πριν ανεβείτε, βεβαιωθείτε ότι έχετε πάρει μαζί σας ό,τι θα χρειαστείτε.", "Ladies and gentlemen, good evening. We remind you that, for safety reasons, passengers may not stay on the ship's car deck during the voyage. Before you go up, please make sure you have taken with you everything you will need."),
  L("Αξιωματικός", "m", "Τα κατοικίδια ζώα μπορούν να μείνουν στους ειδικούς χώρους στο κατάστρωμα ή στις καμπίνες που έχουν χαρακτηριστεί φιλικές προς τα ζώα. Δεν επιτρέπεται να μείνουν μέσα στα αυτοκίνητα.", "Pets may stay in the special areas on deck or in the cabins designated as pet-friendly. They may not stay inside the cars."),
  L("Αξιωματικός", "m", "Η πρόσβαση στο γκαράζ θα επιτραπεί ξανά δεκαπέντε λεπτά πριν από την άφιξη στον Πειραιά, όταν θα ακούσετε σχετική ανακοίνωση. Οι οδηγοί παρακαλούνται να μη βάζουν μπρος τις μηχανές πριν ανοίξει ο καταπέλτης. Σας ευχόμαστε καλό ταξίδι.", "Access to the car deck will be allowed again fifteen minutes before arrival in Piraeus, when you hear the relevant announcement. Drivers are asked not to start their engines before the ramp opens. We wish you a pleasant journey."),
 ],
 "questions": [
  Q("Τι απαγορεύεται κατά τη διάρκεια του ταξιδιού;", ["Το κάπνισμα στο κατάστρωμα", "Η παραμονή επιβατών στο γκαράζ", "Η είσοδος στις καμπίνες", "Η χρήση του ασανσέρ"], 1, "απαγορεύεται η παραμονή επιβατών στο γκαράζ του πλοίου κατά τη διάρκεια του ταξιδιού"),
  Q("Πού δεν επιτρέπεται να μείνουν τα κατοικίδια;", ["Στις φιλικές προς τα ζώα καμπίνες", "Στους ειδικούς χώρους στο κατάστρωμα", "Στο σαλόνι", "Μέσα στα αυτοκίνητα"], 3, "Δεν επιτρέπεται να μείνουν μέσα στα αυτοκίνητα"),
  Q("Τι πρέπει να κάνουν οι οδηγοί στο τέλος του ταξιδιού;", ["Να μη βάλουν μπρος τις μηχανές πριν ανοίξει ο καταπέλτης", "Να κατέβουν στο γκαράζ μισή ώρα πριν", "Να δείξουν τα εισιτήριά τους", "Να περιμένουν να βγουν πρώτα οι πεζοί"], 0, "Οι οδηγοί παρακαλούνται να μη βάζουν μπρος τις μηχανές πριν ανοίξει ο καταπέλτης"),
 ],
 "gloss": {"υπενθυμίζουμε": "υπενθυμίζω — to remind", "παραμονή": "παραμονή — staying", "γκαράζ": "γκαράζ — garage, car deck", "βεβαιωθείτε": "βεβαιώνομαι — to make sure", "κατοικίδια": "κατοικίδιο — pet", "κατάστρωμα": "κατάστρωμα — deck", "πρόσβαση": "πρόσβαση — access", "βάζουν μπρος": "βάζω μπρος — to start (an engine)", "καταπέλτης": "καταπέλτης — (car) ramp of a ferry"}
})

ITEMS.append({
 "id": "l155-dia-skylos-avgoustos", "title": "Ποιος θα κρατήσει τον σκύλο τον Αύγουστο;", "title_en": "Who will keep the dog in August?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο αδέλφια να συζητούν στο τηλέφωνο για τις καλοκαιρινές διακοπές.",
 "script": [
  L("Νίκος", "m", "Φωτεινή, θέλω να σου ζητήσω μια χάρη. Φεύγουμε για Ισπανία από τις πέντε μέχρι τις είκοσι Αυγούστου και δεν έχουμε πού να αφήσουμε τον Μπόμπο. Θα μπορούσες να τον κρατήσεις;", "Fotini, I want to ask you a favour. We're leaving for Spain from the fifth to the twentieth of August and we have nowhere to leave Bobos. Could you keep him?"),
  L("Φωτεινή", "f", "Νίκο μου, το ξέρεις ότι τον λατρεύω, αλλά τον Αύγουστο θα είμαι στο χωριό, και η πεθερά μου φοβάται τα σκυλιά. Τις πρώτες μέρες, πάντως, μέχρι τις δέκα, είμαι ακόμα στην Αθήνα.", "Nikos dear, you know I adore him, but in August I'll be in the village, and my mother-in-law is afraid of dogs. For the first days, though, until the tenth, I'm still in Athens."),
  L("Νίκος", "m", "Τότε ίσως να τον κρατήσεις εσύ ως τις δέκα, και μετά να τον πάρει ο Άρης, ο γείτονάς μας, που γυρίζει από τις διακοπές του εκείνη τη μέρα. Το ξενοδοχείο σκύλων κοστίζει τριάντα ευρώ τη μέρα, και ο Μπόμπος εκεί δεν τρώει τίποτα.", "Then maybe you could keep him until the tenth, and after that Aris, our neighbour, could take him, as he's back from his holidays that day. The dog hotel costs thirty euros a day, and Bobos doesn't eat a thing there."),
  L("Φωτεινή", "f", "Εντάξει, συμφωνώ. Αλλά θα μου φέρεις και την τροφή του και το κρεβατάκι του, γιατί αλλιώς δεν κοιμάται.", "All right, I agree. But you'll bring me his food and his little bed too, because otherwise he doesn't sleep."),
 ],
 "questions": [
  Q("Γιατί η Φωτεινή δεν μπορεί να κρατήσει τον σκύλο όλο τον Αύγουστο;", ["Γιατί έχει αλλεργία", "Γιατί θα είναι στο χωριό και η πεθερά της φοβάται τα σκυλιά", "Γιατί φεύγει κι εκείνη για Ισπανία", "Γιατί το διαμέρισμά της είναι μικρό"], 1, "τον Αύγουστο θα είμαι στο χωριό, και η πεθερά μου φοβάται τα σκυλιά"),
  Q("Τι λύση προτείνει ο Νίκος;", ["Να πάει ο σκύλος σε ξενοδοχείο σκύλων", "Να πάρουν τον σκύλο μαζί στην Ισπανία", "Να κρατήσει η Φωτεινή τον σκύλο ως τις δέκα και μετά ο γείτονας", "Να μείνει ο σκύλος στο χωριό"], 2, "ίσως να τον κρατήσεις εσύ ως τις δέκα, και μετά να τον πάρει ο Άρης"),
  Q("Τι ζητάει η Φωτεινή;", ["Να της φέρει την τροφή και το κρεβατάκι του σκύλου", "Να της πληρώσει τριάντα ευρώ τη μέρα", "Να της φέρει δώρο από την Ισπανία", "Να πάει πρώτα τον σκύλο στον κτηνίατρο"], 0, "θα μου φέρεις και την τροφή του και το κρεβατάκι του"),
 ],
 "gloss": {"χάρη": "χάρη — favour", "λατρεύω": "λατρεύω — to adore", "πεθερά": "πεθερά — mother-in-law", "φοβάται": "φοβάμαι — to be afraid", "ξενοδοχείο σκύλων": "ξενοδοχείο σκύλων — dog hotel, kennels", "τροφή": "τροφή — (pet) food", "κρεβατάκι": "κρεβατάκι — little bed"}
})

ITEMS.append({
 "id": "l155-int-frontistria-zoon", "title": "Μια φροντίστρια ζώων σε ζωολογικό πάρκο", "title_en": "An animal keeper at a zoo", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από μια ραδιοφωνική συνέντευξη με μια γυναίκα που φροντίζει ζώα σε ένα ζωολογικό πάρκο.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς ξεκινάει μια μέρα σας;", "How does one of your days begin?"),
  L("Ελπίδα", "f", "Στις έξι και μισή. Πρώτα κάνω έναν γύρο για να δω ότι όλα τα ζώα είναι καλά, γιατί ένα ζώο που δεν σηκώνεται ή δεν τρώει είναι συχνά το πρώτο σημάδι ότι κάτι δεν πάει καλά. Μετά καθαρίζουμε και ετοιμάζουμε το φαγητό. Οι λεμούριοι, για παράδειγμα, τρώνε φρούτα και λαχανικά κομμένα σε μικρά κομματάκια.", "At half past six. First I do a round to see that all the animals are fine, because an animal that doesn't get up or doesn't eat is often the first sign that something is wrong. Then we clean and prepare the food. The lemurs, for example, eat fruit and vegetables cut into small pieces."),
  L("Δημοσιογράφος", "m", "Δεν τους δίνετε το φαγητό απλώς σε ένα πιάτο;", "Don't you just give them their food on a plate?"),
  L("Ελπίδα", "f", "Όχι πάντα. Συχνά το κρύβουμε μέσα σε κουτιά ή σε κλαδιά, για να το ψάξουν, όπως θα έκαναν στη φύση. Αυτό το λέμε «εμπλουτισμό» και είναι πολύ σημαντικό για να μην βαριούνται. Το πιο δύσκολο στη δουλειά μου δεν είναι η κούραση· είναι ότι δένεσαι με τα ζώα, και όταν κάποιο μεταφέρεται σε άλλο πάρκο, σου λείπει πολύ.", "Not always. We often hide it in boxes or in branches, so they have to look for it, as they would in nature. We call this \"enrichment\" and it's very important so that they don't get bored. The hardest thing about my job isn't the tiredness; it's that you become attached to the animals, and when one is moved to another zoo, you miss it a lot."),
 ],
 "questions": [
  Q("Γιατί η Ελπίδα κάνει πρώτα έναν γύρο;", ["Για να μετρήσει τα ζώα", "Για να ανοίξει τις πόρτες για τους επισκέπτες", "Για να δει ότι όλα τα ζώα είναι καλά", "Για να ταΐσει τα πουλιά"], 2, "κάνω έναν γύρο για να δω ότι όλα τα ζώα είναι καλά"),
  Q("Γιατί κρύβουν συχνά το φαγητό;", ["Για να το ψάξουν τα ζώα, όπως στη φύση, και να μη βαριούνται", "Για να μην το κλέψουν άλλα ζώα", "Για να μη χαλάσει στον ήλιο", "Για να μην το δουν οι επισκέπτες"], 0, "για να το ψάξουν, όπως θα έκαναν στη φύση"),
  Q("Ποιο είναι για εκείνη το πιο δύσκολο στη δουλειά της;", ["Η κούραση", "Το πρωινό ξύπνημα", "Οι επισκέπτες που δεν σέβονται τους κανόνες", "Ότι δένεται με τα ζώα και της λείπουν όταν μεταφέρονται"], 3, "είναι ότι δένεσαι με τα ζώα"),
 ],
 "gloss": {"σημάδι": "σημάδι — sign", "λεμούριοι": "λεμούριος — lemur", "κομματάκια": "κομματάκι — small piece", "κλαδιά": "κλαδί — branch", "εμπλουτισμό": "εμπλουτισμός — enrichment", "βαριούνται": "βαριέμαι — to get bored", "δένεσαι": "δένομαι — to become attached", "μεταφέρεται": "μεταφέρομαι — to be moved, transferred"}
})

ITEMS.append({
 "id": "l155-news-lygmena-farmaka", "title": "Πού πάνε τα ληγμένα φάρμακα;", "title_en": "Where do expired medicines go?", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα τοπικό δελτίο ειδήσεων.",
 "script": [
  L("Εκφωνήτρια", "f", "Ξεκινά τη Δευτέρα στον δήμο μας μια εκστρατεία ενημέρωσης για τη σωστή απόρριψη των ληγμένων φαρμάκων. Σύμφωνα με τον δήμο, πολλοί κάτοικοι εξακολουθούν να πετούν τα φάρμακα στα σκουπίδια ή, ακόμα χειρότερα, στον νεροχύτη, με αποτέλεσμα ουσίες να καταλήγουν στο νερό και στο έδαφος.", "An information campaign on the correct disposal of expired medicines begins in our municipality on Monday. According to the municipality, many residents still throw medicines into the rubbish or, even worse, down the sink, with the result that substances end up in the water and the soil."),
  L("Εκφωνήτρια", "f", "Τα ληγμένα ή αχρησιμοποίητα φάρμακα μπορούν να παραδίδονται στους ειδικούς κάδους που υπάρχουν σε όλα τα φαρμακεία της πόλης. Οι κάτοικοι παρακαλούνται να αφαιρούν πρώτα τα χάρτινα κουτιά και τα φύλλα οδηγιών, που πάνε στην ανακύκλωση χαρτιού.", "Expired or unused medicines can be handed in at the special bins in all the city's pharmacies. Residents are asked to first remove the cardboard boxes and the instruction leaflets, which go into paper recycling."),
  L("Εκφωνήτρια", "f", "Οι βελόνες και οι σύριγγες δεν πρέπει να μπαίνουν στους κάδους αυτούς· για αυτές, οι κάτοικοι μπορούν να απευθύνονται στο κέντρο υγείας. Το Σάββατο, εθελοντές θα μοιράζουν φυλλάδια στη λαϊκή αγορά.", "Needles and syringes must not go into these bins; for those, residents can turn to the health centre. On Saturday, volunteers will hand out leaflets at the street market."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα, σύμφωνα με τον δήμο;", ["Τα φαρμακεία δεν δέχονται ληγμένα φάρμακα", "Πολλοί κάτοικοι πετούν τα φάρμακα στα σκουπίδια ή στον νεροχύτη", "Τα φάρμακα έχουν ακριβύνει", "Λείπουν φάρμακα από τα φαρμακεία"], 1, "πολλοί κάτοικοι εξακολουθούν να πετούν τα φάρμακα στα σκουπίδια"),
  Q("Τι πρέπει να κάνουν οι κάτοικοι πριν παραδώσουν τα φάρμακα;", ["Να τα πλύνουν", "Να τα βάλουν σε πλαστική σακούλα", "Να συμπληρώσουν ένα έντυπο", "Να αφαιρέσουν τα χάρτινα κουτιά και τα φύλλα οδηγιών"], 3, "να αφαιρούν πρώτα τα χάρτινα κουτιά και τα φύλλα οδηγιών"),
  Q("Πού πρέπει να πάνε οι βελόνες και οι σύριγγες;", ["Στους κάδους των φαρμακείων", "Στην ανακύκλωση", "Στο κέντρο υγείας", "Στη λαϊκή αγορά"], 2, "οι κάτοικοι μπορούν να απευθύνονται στο κέντρο υγείας"),
 ],
 "gloss": {"εκστρατεία": "εκστρατεία — campaign", "απόρριψη": "απόρριψη — disposal", "ληγμένων": "ληγμένος — expired", "νεροχύτη": "νεροχύτης — (kitchen) sink", "ουσίες": "ουσία — substance", "αχρησιμοποίητα": "αχρησιμοποίητος — unused", "κάδους": "κάδος — bin", "φύλλα οδηγιών": "φύλλο οδηγιών — instruction leaflet", "σύριγγες": "σύριγγα — syringe", "φυλλάδια": "φυλλάδιο — leaflet"}
})

ITEMS.append({
 "id": "l155-mono-vivliothiki-rouchon", "title": "Μια βιβλιοθήκη για ρούχα", "title_en": "A library for clothes", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια νέα γυναίκα να μιλάει σε ένα podcast για ένα κατάστημα όπου δανείζεται ρούχα.",
 "script": [
  L("Ζωή", "f", "Πριν από έναν χρόνο έγινα μέλος σε μια «βιβλιοθήκη ρούχων» στη γειτονιά μου. Λειτουργεί όπως μια δανειστική βιβλιοθήκη: πληρώνεις μια μικρή μηνιαία συνδρομή και μπορείς να δανείζεσαι ως τέσσερα κομμάτια τη φορά, για δύο εβδομάδες.", "A year ago I became a member of a \"clothes library\" in my neighbourhood. It works like a lending library: you pay a small monthly subscription and you can borrow up to four pieces at a time, for two weeks."),
  L("Ζωή", "f", "Η ιδέα μού άρεσε γιατί είχα μια ντουλάπα γεμάτη ρούχα που είχα φορέσει μία ή δύο φορές. Τώρα, για έναν γάμο ή μια συνέντευξη για δουλειά, δανείζομαι κάτι ωραίο και μετά το επιστρέφω. Τα ρούχα τα πλένει η ίδια η βιβλιοθήκη, οπότε δεν έχω κι αυτή τη φροντίδα.", "I liked the idea because I had a wardrobe full of clothes I had worn once or twice. Now, for a wedding or a job interview, I borrow something nice and then return it. The library itself washes the clothes, so I don't have that to worry about either."),
  L("Ζωή", "f", "Βέβαια, δεν είναι όλα τέλεια. Τα πιο ωραία κομμάτια είναι συνήθως δανεισμένα, και μερικές φορές πρέπει να περιμένω εβδομάδες. Αλλά φέτος αγόρασα μόνο δύο καινούργια ρούχα, και αυτό για μένα είναι μια μικρή επανάσταση.", "Of course, it's not all perfect. The nicest pieces are usually on loan, and sometimes I have to wait for weeks. But this year I only bought two new clothes, and for me that's a small revolution."),
 ],
 "questions": [
  Q("Πώς λειτουργεί η «βιβλιοθήκη ρούχων»;", ["Πουλάει μεταχειρισμένα ρούχα", "Με μια μηνιαία συνδρομή δανείζεσαι ως τέσσερα κομμάτια για δύο εβδομάδες", "Ανταλλάσσεις τα ρούχα σου με άλλων", "Νοικιάζεις ρούχα μόνο για γάμους"], 1, "πληρώνεις μια μικρή μηνιαία συνδρομή και μπορείς να δανείζεσαι ως τέσσερα κομμάτια τη φορά"),
  Q("Ποιος πλένει τα ρούχα;", ["Η ίδια η βιβλιοθήκη", "Η Ζωή", "Ένα καθαριστήριο που πληρώνουν τα μέλη", "Κανείς, επιστρέφονται όπως είναι"], 0, "Τα ρούχα τα πλένει η ίδια η βιβλιοθήκη"),
  Q("Ποιο είναι, κατά τη Ζωή, το μειονέκτημα;", ["Η συνδρομή είναι ακριβή", "Τα ρούχα δεν είναι καθαρά", "Τα πιο ωραία κομμάτια είναι συνήθως δανεισμένα και πρέπει να περιμένει", "Η βιβλιοθήκη είναι μακριά από το σπίτι της"], 2, "Τα πιο ωραία κομμάτια είναι συνήθως δανεισμένα"),
 ],
 "gloss": {"μέλος": "μέλος — member", "δανειστική βιβλιοθήκη": "δανειστική βιβλιοθήκη — lending library", "συνδρομή": "συνδρομή — subscription", "δανείζεσαι": "δανείζομαι — to borrow", "ντουλάπα": "ντουλάπα — wardrobe", "φροντίδα": "φροντίδα — care, worry", "δανεισμένα": "δανεισμένος — on loan", "επανάσταση": "επανάσταση — revolution"}
})

ITEMS.append({
 "id": "l155-rep-stathmoi-episkevis", "title": "Σταθμοί επισκευής ποδηλάτων στον δρόμο", "title_en": "Bike repair stations on the street", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια ραδιοφωνική εκπομπή για την πόλη.",
 "script": [
  L("Ρεπόρτερ", "m", "Στον ποδηλατόδρομο της παραλίας εμφανίστηκαν τον περασμένο μήνα τρεις μεταλλικές κολόνες σε έντονο πράσινο χρώμα. Είναι σταθμοί αυτοεξυπηρέτησης για ποδήλατα: ο καθένας έχει μια τρόμπα και μια σειρά από εργαλεία δεμένα με ατσάλινα καλώδια, για να μην τα παίρνει κανείς.", "Last month three metal posts in bright green appeared on the seafront cycle path. They are self-service stations for bicycles: each one has a pump and a set of tools attached with steel cables, so nobody takes them."),
  L("Ρεπόρτερ", "m", "Πάνω σε κάθε σταθμό υπάρχει ένας κωδικός QR που οδηγεί σε σύντομα βίντεο: πώς αλλάζεις σαμπρέλα, πώς ρυθμίζεις τα φρένα, πώς λαδώνεις την αλυσίδα. Υπάρχει ακόμα και ένα άγκιστρο για να κρεμάς το ποδήλατο όσο το επισκευάζεις.", "On each station there is a QR code that leads to short videos: how to change an inner tube, how to adjust the brakes, how to oil the chain. There's even a hook to hang the bike on while you repair it."),
  L("Ρεπόρτερ", "m", "Ο δήμος σκοπεύει να τοποθετήσει άλλους πέντε σταθμούς ως το καλοκαίρι, κοντά σε σχολεία και σταθμούς του μετρό. Οι ιδιοκτήτες συνεργείων ποδηλάτων, πάντως, δεν ανησυχούν: όπως μας είπε ένας από αυτούς, «όποιος μάθει να φτιάχνει το ποδήλατό του, θα το αγαπήσει περισσότερο και θα έρθει κάποια στιγμή και σε μας».", "The municipality plans to install another five stations by the summer, near schools and metro stations. Bicycle repair shop owners, though, are not worried: as one of them told us, \"whoever learns to fix their bike will love it more and will come to us at some point too\"."),
 ],
 "questions": [
  Q("Γιατί τα εργαλεία είναι δεμένα με ατσάλινα καλώδια;", ["Για να μην τα παίρνει κανείς", "Για να μη σκουριάζουν", "Για να μην τα χάνουν τα παιδιά", "Για να φορτίζονται"], 0, "δεμένα με ατσάλινα καλώδια, για να μην τα παίρνει κανείς"),
  Q("Πού οδηγεί ο κωδικός QR;", ["Σε έναν χάρτη με τους ποδηλατόδρομους", "Σε μια εφαρμογή για ενοικίαση ποδηλάτων", "Στη σελίδα του δήμου", "Σε σύντομα βίντεο για επισκευές"], 3, "ένας κωδικός QR που οδηγεί σε σύντομα βίντεο"),
  Q("Γιατί δεν ανησυχούν οι ιδιοκτήτες συνεργείων;", ["Γιατί οι σταθμοί είναι λίγοι", "Γιατί ο δήμος τους πληρώνει", "Γιατί όποιος μάθει να φτιάχνει το ποδήλατό του θα το αγαπήσει και θα πάει κάποια στιγμή και σε αυτούς", "Γιατί οι σταθμοί είναι μακριά από τα συνεργεία τους"], 2, "όποιος μάθει να φτιάχνει το ποδήλατό του, θα το αγαπήσει περισσότερο"),
 ],
 "gloss": {"ποδηλατόδρομο": "ποδηλατόδρομος — cycle path", "αυτοεξυπηρέτησης": "αυτοεξυπηρέτηση — self-service", "τρόμπα": "τρόμπα — pump", "ατσάλινα": "ατσάλινος — steel", "σαμπρέλα": "σαμπρέλα — inner tube", "ρυθμίζεις": "ρυθμίζω — to adjust", "λαδώνεις": "λαδώνω — to oil", "άγκιστρο": "άγκιστρο — hook", "συνεργείων": "συνεργείο — repair shop"}
})

ITEMS.append({
 "id": "l155-dia-xylosompa", "title": "Ξυλόσομπα ή κλιματιστικό στο σπίτι του βουνού;", "title_en": "A wood stove or air conditioning in the mountain house?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά πώς θα ζεστάνει το σπίτι που αγόρασε σε ένα ορεινό χωριό.",
 "script": [
  L("Στέλιος", "m", "Το σκέφτηκα πολύ: στο σπίτι του χωριού θέλω ξυλόσομπα. Τίποτα δεν ζεσταίνει όπως η φωτιά, και τα ξύλα εκεί πάνω είναι φθηνά, αφού τα πουλάει ο ίδιος ο συνεταιρισμός του χωριού.", "I've thought about it a lot: in the village house I want a wood stove. Nothing warms you like a fire, and wood up there is cheap, since the village cooperative itself sells it."),
  L("Μαρίνα", "f", "Κι εγώ τη λατρεύω, αλλά σκέψου ότι θα πηγαίνουμε συνήθως Παρασκευή βράδυ. Μέχρι να ανάψει η σόμπα και να ζεσταθεί το σπίτι, θα έχουν περάσει δύο ώρες. Με ένα κλιματιστικό θα το ανάβαμε από το κινητό πριν φτάσουμε.", "I love it too, but think that we'll usually go on a Friday evening. By the time the stove is lit and the house warms up, two hours will have passed. With an air conditioner we could switch it on from our phone before we arrive."),
  L("Στέλιος", "m", "Σωστό. Και τα κλιματιστικά στο κρύο του βουνού δεν αποδίδουν όλα το ίδιο καλά, θα πρέπει να ρωτήσουμε για κάποιο κατάλληλο για χαμηλές θερμοκρασίες.", "True. And not all air conditioners perform equally well in mountain cold; we'll have to ask about one suitable for low temperatures."),
  L("Μαρίνα", "f", "Τότε ας βάλουμε και τα δύο: το κλιματιστικό για να βρίσκουμε το σπίτι ζεστό, και τη σόμπα για τα βράδια. Ο Αντώνης, ο μάστορας, έρχεται το Σάββατο να μας πει πού μπορεί να μπει η καμινάδα.", "Then let's have both: the air conditioner so we find the house warm, and the stove for the evenings. Antonis, the builder, is coming on Saturday to tell us where the chimney can go."),
 ],
 "questions": [
  Q("Γιατί ο Στέλιος θέλει ξυλόσομπα;", ["Γιατί είναι πιο ασφαλής", "Γιατί τίποτα δεν ζεσταίνει όπως η φωτιά και τα ξύλα εκεί είναι φθηνά", "Γιατί το σπίτι δεν έχει ρεύμα", "Γιατί το ζητάει ο συνεταιρισμός"], 1, "Τίποτα δεν ζεσταίνει όπως η φωτιά, και τα ξύλα εκεί πάνω είναι φθηνά"),
  Q("Ποιο πλεονέκτημα του κλιματιστικού αναφέρει η Μαρίνα;", ["Ότι μπορούν να το ανάψουν από το κινητό πριν φτάσουν", "Ότι είναι φθηνότερο", "Ότι δεν χρειάζεται συντήρηση", "Ότι δροσίζει και το καλοκαίρι"], 0, "Με ένα κλιματιστικό θα το ανάβαμε από το κινητό πριν φτάσουμε"),
  Q("Τι αποφασίζουν τελικά;", ["Να βάλουν μόνο ξυλόσομπα", "Να βάλουν μόνο κλιματιστικό", "Να μην πηγαίνουν στο χωριό τον χειμώνα", "Να βάλουν και τα δύο"], 3, "ας βάλουμε και τα δύο"),
 ],
 "gloss": {"ξυλόσομπα": "ξυλόσομπα — wood stove", "ξύλα": "ξύλα — firewood", "συνεταιρισμός": "συνεταιρισμός — cooperative", "αποδίδουν": "αποδίδω — to perform", "κατάλληλο": "κατάλληλος — suitable", "μάστορας": "μάστορας — builder, craftsman", "καμινάδα": "καμινάδα — chimney"}
})

ITEMS.append({
 "id": "l155-c1-gorillas", "title": "Ο γορίλας που κανείς δεν είδε", "title_en": "The gorilla nobody saw", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη για την ψυχολογία της προσοχής.",
 "script": [
  L("Ομιλήτρια", "f", "Το 1999 δύο ψυχολόγοι του Χάρβαρντ, ο Ντάνιελ Σάιμονς και ο Κρίστοφερ Τσάμπρις, έδειξαν σε εθελοντές ένα σύντομο βίντεο με δύο ομάδες που πασάρουν μια μπάλα μπάσκετ. Τους ζήτησαν να μετρήσουν πόσες πάσες κάνουν οι παίκτες με τα λευκά μπλουζάκια.", "In 1999 two Harvard psychologists, Daniel Simons and Christopher Chabris, showed volunteers a short video of two teams passing a basketball. They asked them to count how many passes the players in white shirts made."),
  L("Ομιλήτρια", "f", "Στη μέση του βίντεο, ένας άνθρωπος ντυμένος γορίλας περνάει ανάμεσα στους παίκτες, σταματάει, χτυπάει το στήθος του και φεύγει. Περίπου οι μισοί εθελοντές δεν τον πρόσεξαν καθόλου, και πολλοί αρνούνταν να το πιστέψουν όταν ξαναέβλεπαν το βίντεο.", "In the middle of the video, a person dressed as a gorilla walks among the players, stops, beats their chest and leaves. About half the volunteers didn't notice them at all, and many refused to believe it when they watched the video again."),
  L("Ομιλήτρια", "f", "Το φαινόμενο ονομάστηκε «τύφλωση απροσεξίας». Δεν σημαίνει ότι τα μάτια μας δεν βλέπουν· σημαίνει ότι ο εγκέφαλος, όταν είναι απορροφημένος σε μια δύσκολη εργασία, φιλτράρει ό,τι θεωρεί άσχετο, ακόμη κι αν είναι κάτι τόσο απροσδόκητο όσο ένας γορίλας.", "The phenomenon was named \"inattentional blindness\". It doesn't mean that our eyes don't see; it means that the brain, when absorbed in a difficult task, filters out whatever it considers irrelevant, even if it is something as unexpected as a gorilla."),
  L("Ομιλήτρια", "f", "Οι συνέπειες ξεπερνούν το εργαστήριο. Ένας οδηγός που μιλάει στο τηλέφωνο μπορεί να κοιτάζει κατευθείαν έναν πεζό και να μην τον «δει». Γι' αυτό, η φράση «μα τον κοίταζα» δεν αποδεικνύει ότι τον είδαμε πραγματικά.", "The consequences go beyond the laboratory. A driver talking on the phone may look straight at a pedestrian and not \"see\" them. That's why the phrase \"but I was looking at him\" doesn't prove that we really saw him."),
 ],
 "questions": [
  Q("Τι ζητήθηκε από τους εθελοντές;", ["Να βρουν τον γορίλα", "Να μετρήσουν τις πάσες των παικτών με τα λευκά μπλουζάκια", "Να μετρήσουν τους παίκτες", "Να περιγράψουν το βίντεο"], 1, "Τους ζήτησαν να μετρήσουν πόσες πάσες κάνουν οι παίκτες με τα λευκά μπλουζάκια"),
  Q("Τι συνέβη με τους μισούς περίπου εθελοντές;", ["Δεν πρόσεξαν καθόλου τον γορίλα", "Μέτρησαν λάθος τις πάσες", "Γέλασαν με τον γορίλα", "Σταμάτησαν το βίντεο"], 0, "Περίπου οι μισοί εθελοντές δεν τον πρόσεξαν καθόλου"),
  Q("Τι σημαίνει, κατά την ομιλήτρια, η «τύφλωση απροσεξίας»;", ["Ότι τα μάτια μας κουράζονται γρήγορα", "Ότι βλέπουμε μόνο ό,τι περιμένουμε", "Ότι ο εγκέφαλος, απορροφημένος σε μια δύσκολη εργασία, φιλτράρει ό,τι θεωρεί άσχετο", "Ότι δεν μπορούμε να κάνουμε δύο πράγματα μαζί"], 2, "ο εγκέφαλος, όταν είναι απορροφημένος σε μια δύσκολη εργασία, φιλτράρει ό,τι θεωρεί άσχετο"),
  Q("Ποιο συμπέρασμα βγάζει για την καθημερινή ζωή;", ["Ότι πρέπει να οδηγούμε πιο αργά", "Ότι οι πεζοί φταίνε συχνά", "Ότι τα βίντεο μας ξεγελούν", "Ότι το να κοιτάζουμε κάτι δεν αποδεικνύει ότι το είδαμε πραγματικά"], 3, "η φράση «μα τον κοίταζα» δεν αποδεικνύει ότι τον είδαμε πραγματικά"),
 ],
 "gloss": {"πασάρουν": "πασάρω — to pass (a ball)", "πάσες": "πάσα — pass", "γορίλας": "γορίλας — gorilla", "στήθος": "στήθος — chest", "τύφλωση απροσεξίας": "τύφλωση απροσεξίας — inattentional blindness", "απορροφημένος": "απορροφημένος — absorbed", "φιλτράρει": "φιλτράρω — to filter", "άσχετο": "άσχετος — irrelevant", "απροσδόκητο": "απροσδόκητος — unexpected", "αποδεικνύει": "αποδεικνύω — to prove"}
})

ITEMS.append({
 "id": "l155-c1-makgkerk", "title": "Όταν ακούμε με τα μάτια", "title_en": "When we hear with our eyes", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκπομπή επιστήμης για την αντίληψη της ομιλίας.",
 "script": [
  L("Παρουσιαστής", "m", "Το 1976 οι Βρετανοί ψυχολόγοι Χάρι ΜακΓκερκ και Τζον ΜακΝτόναλντ δημοσίευσαν ένα άρθρο με τον εύγλωττο τίτλο «Ακούγοντας χείλη και βλέποντας φωνές». Είχαν ανακαλύψει, σχεδόν τυχαία, ένα εντυπωσιακό φαινόμενο.", "In 1976 the British psychologists Harry McGurk and John MacDonald published an article with the telling title \"Hearing lips and seeing voices\". They had discovered, almost by chance, a striking phenomenon."),
  L("Παρουσιαστής", "m", "Όταν σε ένα βίντεο ο ήχος λέει «μπα», αλλά τα χείλη του ομιλητή σχηματίζουν «γκα», οι περισσότεροι άνθρωποι δεν ακούν ούτε το ένα ούτε το άλλο: ακούν «ντα». Ο εγκέφαλος συνδυάζει δηλαδή αυτό που ακούει με αυτό που βλέπει και δημιουργεί έναν τρίτο ήχο, που δεν υπάρχει.", "When in a video the sound says \"ba\" but the speaker's lips form \"ga\", most people hear neither one nor the other: they hear \"da\". In other words, the brain combines what it hears with what it sees and creates a third sound, which doesn't exist."),
  L("Παρουσιαστής", "m", "Το πιο παράξενο είναι ότι το φαινόμενο δεν εξαφανίζεται ακόμα κι όταν το γνωρίζεις. Αρκεί να κλείσεις τα μάτια για να ακούσεις καθαρά «μπα»· μόλις τα ανοίξεις, ο ήχος αλλάζει ξανά.", "The strangest thing is that the phenomenon doesn't disappear even when you know about it. You only need to close your eyes to hear \"ba\" clearly; as soon as you open them, the sound changes again."),
  L("Παρουσιαστής", "m", "Αυτό εξηγεί γιατί καταλαβαίνουμε καλύτερα κάποιον σε ένα θορυβώδες μαγαζί όταν βλέπουμε το πρόσωπό του, και γιατί μια κακή μεταγλώττιση μάς κουράζει, ακόμα κι αν δεν καταλαβαίνουμε τον λόγο.", "This explains why we understand someone better in a noisy shop when we can see their face, and why bad dubbing tires us, even if we don't understand why."),
 ],
 "questions": [
  Q("Τι ακούν οι περισσότεροι όταν ο ήχος λέει «μπα» και τα χείλη σχηματίζουν «γκα»;", ["«Μπα»", "«Γκα»", "«Ντα»", "Τίποτα"], 2, "ακούν «ντα»"),
  Q("Τι κάνει, σύμφωνα με τον παρουσιαστή, ο εγκέφαλος;", ["Συνδυάζει αυτό που ακούει με αυτό που βλέπει και δημιουργεί έναν τρίτο ήχο", "Αγνοεί την εικόνα", "Αγνοεί τον ήχο", "Μπερδεύεται και δεν ακούει τίποτα"], 0, "εγκέφαλος συνδυάζει δηλαδή αυτό που ακούει με αυτό που βλέπει"),
  Q("Τι συμβαίνει όταν γνωρίζεις το φαινόμενο;", ["Εξαφανίζεται", "Γίνεται πιο έντονο", "Ακούς και τους δύο ήχους", "Δεν εξαφανίζεται· μόνο με κλειστά μάτια ακούς καθαρά «μπα»"], 3, "το φαινόμενο δεν εξαφανίζεται ακόμα κι όταν το γνωρίζεις"),
  Q("Τι εξηγεί, μεταξύ άλλων, το φαινόμενο;", ["Γιατί μας αρέσει η μουσική", "Γιατί καταλαβαίνουμε καλύτερα κάποιον σε θόρυβο όταν βλέπουμε το πρόσωπό του", "Γιατί ξεχνάμε τα ονόματα", "Γιατί οι ξένες γλώσσες είναι δύσκολες"], 1, "καταλαβαίνουμε καλύτερα κάποιον σε ένα θορυβώδες μαγαζί όταν βλέπουμε το πρόσωπό του"),
 ],
 "gloss": {"εύγλωττο": "εύγλωττος — eloquent, telling", "χείλη": "χείλη — lips", "εντυπωσιακό": "εντυπωσιακός — striking", "σχηματίζουν": "σχηματίζω — to form", "συνδυάζει": "συνδυάζω — to combine", "εξαφανίζεται": "εξαφανίζομαι — to disappear", "θορυβώδες": "θορυβώδης — noisy", "μεταγλώττιση": "μεταγλώττιση — dubbing"}
})

rnd = random.Random(155)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-155.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
