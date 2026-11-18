# Source for library/listening/listening-214.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l214.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l214-news-pagkaki-kouventas", "title": "Ένα παγκάκι για κουβέντα ενάντια στη μοναξιά", "title_en": "A 'chatting bench' against loneliness", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια τοπική είδηση στο ραδιόφωνο για μια πρωτοβουλία ενός δήμου.",
 "script": [
  L("Εκφωνητής", "m", "Δέκα «παγκάκια για κουβέντα» τοποθετήθηκαν σε πλατείες και πάρκα του δήμου. Είναι κανονικά παγκάκια, με μια μικρή πινακίδα που γράφει: «Αν κάθεσαι εδώ, δεν πειράζει να σου μιλήσει κάποιος». Η ιδέα, που έχει δοκιμαστεί και σε άλλες χώρες, θέλει να ενθαρρύνει τους περαστικούς να πιάσουν κουβέντα.", "Ten 'chatting benches' have been placed in squares and parks in the municipality. They're ordinary benches, with a small sign that reads: 'If you sit here, you don't mind someone talking to you.' The idea, which has also been tried in other countries, aims to encourage passers-by to strike up a conversation."),
  L("Εκφωνητής", "m", "Σύμφωνα με τον δήμο, το πρόγραμμα απευθύνεται κυρίως σε ηλικιωμένους που ζουν μόνοι, αλλά και σε νέους που μετακόμισαν πρόσφατα στην πόλη και δεν γνωρίζουν κανέναν. Δύο φορές την εβδομάδα, εθελοντές του κοινωνικού παντοπωλείου κάθονται στα παγκάκια για να ξεκινήσουν τη συζήτηση.", "According to the municipality, the programme is aimed mainly at elderly people who live alone, but also at young people who recently moved to the city and don't know anyone. Twice a week, volunteers from the community grocery sit on the benches to get the conversation going."),
  L("Εκφωνητής", "m", "Οι πρώτες αντιδράσεις είναι θετικές, αν και κάποιοι κάτοικοι σχολιάζουν ότι στις γειτονιές παλιά δεν χρειαζόταν πινακίδα για να μιλήσει κανείς με τον διπλανό του. Ο δήμος σκοπεύει να αξιολογήσει το πρόγραμμα σε έξι μήνες με ένα ερωτηματολόγιο.", "The first reactions are positive, although some residents remark that in the old neighbourhoods you didn't need a sign to talk to the person next to you. The municipality plans to evaluate the programme in six months with a questionnaire."),
 ],
 "questions": [
  Q("Τι γράφει η πινακίδα στα παγκάκια;", ["«Απαγορεύεται το κάπνισμα»", "Ότι όποιος κάθεται εκεί δεν πειράζει να του μιλήσουν", "Το πρόγραμμα των εθελοντών", "«Μόνο για ηλικιωμένους»"], 1, "«Αν κάθεσαι εδώ, δεν πειράζει να σου μιλήσει κάποιος»"),
  Q("Σε ποιους απευθύνεται κυρίως το πρόγραμμα;", ["Σε τουρίστες", "Σε ηλικιωμένους που ζουν μόνοι και σε νέους που μετακόμισαν πρόσφατα", "Σε μαθητές", "Σε ιδιοκτήτες σκύλων"], 1, "απευθύνεται κυρίως σε ηλικιωμένους που ζουν μόνοι, αλλά και σε νέους που μετακόμισαν πρόσφατα"),
  Q("Τι κάνουν οι εθελοντές δύο φορές την εβδομάδα;", ["Καθαρίζουν τα παγκάκια", "Μοιράζουν φαγητό", "Κάθονται στα παγκάκια για να ξεκινήσουν τη συζήτηση", "Μετρούν πόσοι κάθονται"], 2, "εθελοντές ... κάθονται στα παγκάκια για να ξεκινήσουν τη συζήτηση"),
  Q("Τι σχολιάζουν κάποιοι κάτοικοι;", ["Ότι τα παγκάκια είναι άβολα", "Ότι παλιά δεν χρειαζόταν πινακίδα για να μιλήσει κανείς με τον διπλανό του", "Ότι το πρόγραμμα κοστίζει πολύ", "Ότι οι πινακίδες είναι μικρές"], 1, "στις γειτονιές παλιά δεν χρειαζόταν πινακίδα για να μιλήσει κανείς με τον διπλανό του"),
 ],
 "gloss": {"παγκάκια": "παγκάκι — bench", "περαστικούς": "περαστικός — passer-by", "πιάσουν κουβέντα": "πιάνω κουβέντα — to strike up a conversation", "απευθύνεται": "απευθύνομαι — to be aimed at, address", "παντοπωλείου": "κοινωνικό παντοπωλείο — community grocery (food bank)", "αξιολογήσει": "αξιολογώ — to evaluate", "ερωτηματολόγιο": "ερωτηματολόγιο — questionnaire"},
})
ITEMS.append({
 "id": "l214-dia-olympos-omichli", "title": "Συνεχίζουμε ή γυρίζουμε πίσω;", "title_en": "Go on or turn back? Fog on the mountain", "type": "dialogue", "level": "B2",
 "context_el": "Δύο φίλοι κάνουν πεζοπορία στον Όλυμπο και συζητούν τι θα κάνουν, καθώς πέφτει ομίχλη.",
 "script": [
  L("Στράτος", "m", "Δεν βλέπω ούτε δέκα μέτρα μπροστά μου. Πριν από μισή ώρα είχε ήλιο! Η κορυφή είναι μόνο μιάμιση ώρα από εδώ. Λες να συνεχίσουμε;", "I can't see even ten metres ahead. Half an hour ago it was sunny! The summit is only an hour and a half from here. Do you think we should go on?"),
  L("Αλίκη", "f", "Εγώ λέω όχι. Από εδώ και πάνω το μονοπάτι περνάει από βράχια, και τα σημάδια δεν θα φαίνονται μέσα στην ομίχλη. Αν χαθούμε, δεν έχουμε ούτε σήμα στο κινητό.", "I say no. From here up, the path goes over rocks, and the marks won't be visible in the fog. If we get lost, we don't even have a mobile signal."),
  L("Στράτος", "m", "Μα ξυπνήσαμε στις πέντε για να φτάσουμε στην κορυφή! Κι αν η ομίχλη φύγει σε μισή ώρα;", "But we got up at five to reach the summit! And what if the fog clears in half an hour?"),
  L("Αλίκη", "f", "Μπορεί, αλλά μπορεί και όχι. Ο φύλακας του καταφυγίου μάς είπε χθες ότι το απόγευμα υπάρχει πιθανότητα για καταιγίδα. Ας κατεβούμε στο καταφύγιο, να πιούμε ένα τσάι και να δούμε πώς θα πάει ο καιρός. Το βουνό δεν θα φύγει.", "Maybe, but maybe not. The refuge keeper told us yesterday there's a chance of a storm in the afternoon. Let's go down to the refuge, have a tea and see how the weather goes. The mountain won't go anywhere."),
  L("Στράτος", "m", "Εντάξει, έχεις δίκιο. Καλύτερα να είμαστε απογοητευμένοι στο καταφύγιο παρά χαμένοι στα βράχια. Αλλά αύριο, αν καθαρίσει, ξεκινάμε πάλι στις πέντε.", "OK, you're right. Better to be disappointed at the refuge than lost on the rocks. But tomorrow, if it clears, we start again at five."),
  L("Αλίκη", "f", "Συμφωνώ. Και αυτή τη φορά θα ενημερώσουμε τον φύλακα για τη διαδρομή μας πριν φύγουμε.", "Agreed. And this time we'll tell the refuge keeper our route before we leave."),
 ],
 "questions": [
  Q("Πόσο απέχει η κορυφή, σύμφωνα με τον Στράτο;", ["Μισή ώρα", "Μιάμιση ώρα", "Τρεις ώρες", "Δέκα λεπτά"], 1, "Η κορυφή είναι μόνο μιάμιση ώρα από εδώ"),
  Q("Γιατί η Αλίκη δεν θέλει να συνεχίσουν;", ["Είναι κουρασμένη", "Τα σημάδια του μονοπατιού δεν θα φαίνονται και δεν έχουν σήμα", "Δεν της αρέσουν τα ύψη", "Έχουν ξεμείνει από νερό"], 1, "τα σημάδια δεν θα φαίνονται μέσα στην ομίχλη. Αν χαθούμε, δεν έχουμε ούτε σήμα"),
  Q("Τι τους είχε πει ο φύλακας του καταφυγίου;", ["Ότι το μονοπάτι είναι κλειστό", "Ότι το απόγευμα υπάρχει πιθανότητα για καταιγίδα", "Ότι η ομίχλη θα φύγει γρήγορα", "Ότι το καταφύγιο είναι γεμάτο"], 1, "το απόγευμα υπάρχει πιθανότητα για καταιγίδα"),
  Q("Τι θα κάνουν διαφορετικά την επόμενη μέρα;", ["Θα πάνε χωρίς χάρτη", "Θα ξεκινήσουν πιο αργά", "Θα ενημερώσουν τον φύλακα για τη διαδρομή τους", "Θα πάρουν οδηγό"], 2, "θα ενημερώσουμε τον φύλακα για τη διαδρομή μας πριν φύγουμε"),
 ],
 "gloss": {"ομίχλη": "ομίχλη — fog", "κορυφή": "κορυφή — summit", "σημάδια": "σημάδι — mark, waymark", "σήμα": "σήμα — signal", "φύλακας": "φύλακας — keeper, guard", "καταφυγίου": "καταφύγιο — mountain refuge", "καταιγίδα": "καταιγίδα — storm", "απογοητευμένοι": "απογοητευμένος — disappointed"},
})
ITEMS.append({
 "id": "l214-c1-mono-omades-aimatos", "title": "Γιατί έχουμε διαφορετικές ομάδες αίματος;", "title_en": "Why do we have different blood groups?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ομιλία σε μια σειρά εκλαϊκευμένων διαλέξεων για την ιατρική.",
 "script": [
  L("Ομιλήτρια", "f", "Για αιώνες οι γιατροί δοκίμαζαν μεταγγίσεις αίματος, συχνά με τραγικά αποτελέσματα: κάποιοι ασθενείς σώζονταν, άλλοι πέθαιναν μέσα σε λίγα λεπτά. Το μυστήριο λύθηκε το 1901, όταν ο Αυστριακός Καρλ Λαντστάινερ ανακάλυψε ότι, όταν αναμειγνύεται αίμα διαφορετικών ανθρώπων, μερικές φορές τα ερυθρά αιμοσφαίρια συγκολλώνται. Έτσι γεννήθηκε το σύστημα ΑΒΟ, για το οποίο αργότερα του απονεμήθηκε το βραβείο Νόμπελ.", "For centuries doctors tried blood transfusions, often with tragic results: some patients were saved, others died within minutes. The mystery was solved in 1901, when the Austrian Karl Landsteiner discovered that when the blood of different people is mixed, the red blood cells sometimes clump together. Thus the ABO system was born, for which he was later awarded the Nobel Prize."),
  L("Ομιλήτρια", "f", "Οι ομάδες καθορίζονται από μόρια στην επιφάνεια των ερυθρών αιμοσφαιρίων, τα αντιγόνα. Όποιος έχει ομάδα Α φέρει αντιγόνο Α, όποιος έχει Β φέρει Β, η ομάδα ΑΒ έχει και τα δύο και η ομάδα Ο κανένα. Το ανοσοποιητικό σύστημα επιτίθεται σε όποιο αντιγόνο δεν αναγνωρίζει ως δικό του. Γι' αυτό το αίμα Ο αρνητικό θεωρείται «πανδότης» για τα ερυθρά: δεν έχει αντιγόνα Α και Β ούτε τον παράγοντα Ρέζους, που ανακαλύφθηκε το 1940.", "Groups are determined by molecules on the surface of red blood cells, the antigens. Whoever has group A carries antigen A, whoever has B carries B, group AB has both and group O has neither. The immune system attacks any antigen it doesn't recognise as its own. That's why O negative blood is considered a 'universal donor' for red cells: it has no A or B antigens, nor the Rhesus factor, which was discovered in 1940."),
  L("Ομιλήτρια", "f", "Το πιο ενδιαφέρον ερώτημα, όμως, είναι γιατί υπάρχουν καν διαφορετικές ομάδες. Η επικρατέστερη υπόθεση είναι ότι διαμορφώθηκαν από τη μακραίωνη μάχη με τα μικρόβια. Κάποια παθογόνα χρησιμοποιούν τα αντιγόνα ως «πόρτα» για να μπουν στα κύτταρα, οπότε κάθε ομάδα μπορεί να προστατεύει από ορισμένες ασθένειες και να εκθέτει σε άλλες. Για παράδειγμα, μελέτες δείχνουν ότι η ομάδα Ο συνδέεται με μικρότερο κίνδυνο σοβαρής ελονοσίας.", "The most interesting question, however, is why different groups exist at all. The prevailing hypothesis is that they were shaped by the age-old battle with microbes. Some pathogens use the antigens as a 'door' to get into cells, so each group may protect against certain diseases and expose people to others. For example, studies show that group O is associated with a lower risk of severe malaria."),
  L("Ομιλήτρια", "f", "Αυτό ίσως εξηγεί γιατί η συχνότητα των ομάδων διαφέρει τόσο από περιοχή σε περιοχή. Όσο για τις δημοφιλείς δίαιτες «ανάλογα με την ομάδα αίματος», μην ενθουσιάζεστε: οι έρευνες που τις έχουν ελέγξει δεν βρήκαν στοιχεία ότι λειτουργούν. Το μόνο σίγουρο είναι ότι, όποια ομάδα κι αν έχετε, μια αιμοδοσία μπορεί να σώσει μια ζωή.", "This may explain why the frequency of the groups varies so much from region to region. As for the popular 'blood-type diets', don't get excited: the studies that have tested them found no evidence that they work. The only certainty is that, whatever group you have, a blood donation can save a life."),
 ],
 "questions": [
  Q("Τι ανακάλυψε ο Λαντστάινερ το 1901;", ["Ότι το αίμα αποτελείται από νερό", "Ότι το αίμα διαφορετικών ανθρώπων μερικές φορές συγκολλάται όταν αναμειγνύεται", "Τον παράγοντα Ρέζους", "Τη θεραπεία της ελονοσίας"], 1, "όταν αναμειγνύεται αίμα διαφορετικών ανθρώπων, μερικές φορές τα ερυθρά αιμοσφαίρια συγκολλώνται"),
  Q("Γιατί το αίμα Ο αρνητικό θεωρείται «πανδότης» για τα ερυθρά;", ["Γιατί είναι το πιο σπάνιο", "Γιατί δεν έχει αντιγόνα Α και Β ούτε τον παράγοντα Ρέζους", "Γιατί έχει όλα τα αντιγόνα", "Γιατί παράγεται πιο γρήγορα"], 1, "δεν έχει αντιγόνα Α και Β ούτε τον παράγοντα Ρέζους"),
  Q("Ποια είναι η επικρατέστερη εξήγηση για την ύπαρξη διαφορετικών ομάδων;", ["Η διατροφή των προγόνων μας", "Η μάχη με τα μικρόβια", "Το κλίμα", "Η τύχη"], 1, "διαμορφώθηκαν από τη μακραίωνη μάχη με τα μικρόβια"),
  Q("Τι λέει η ομιλήτρια για τις δίαιτες «ανάλογα με την ομάδα αίματος»;", ["Ότι είναι πολύ αποτελεσματικές", "Ότι λειτουργούν μόνο για την ομάδα Ο", "Ότι οι έρευνες δεν βρήκαν στοιχεία ότι λειτουργούν", "Ότι δεν έχουν μελετηθεί ποτέ"], 2, "οι έρευνες που τις έχουν ελέγξει δεν βρήκαν στοιχεία ότι λειτουργούν"),
 ],
 "gloss": {"μεταγγίσεις": "μετάγγιση — transfusion", "ερυθρά αιμοσφαίρια": "ερυθρό αιμοσφαίριο — red blood cell", "συγκολλώνται": "συγκολλώμαι — to clump, stick together", "αντιγόνα": "αντιγόνο — antigen", "ανοσοποιητικό": "ανοσοποιητικός — immune", "πανδότης": "πανδότης — universal donor", "παθογόνα": "παθογόνο — pathogen", "ελονοσίας": "ελονοσία — malaria", "αιμοδοσία": "αιμοδοσία — blood donation"},
})
ITEMS.append({
 "id": "l214-c1-int-vyzantini-mousiki", "title": "Η γραφή που τραγουδάει: η βυζαντινή σημειογραφία", "title_en": "Writing that sings: a researcher on Byzantine chant notation", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε μουσική εκπομπή με έναν ερευνητή της βυζαντινής μουσικής.",
 "script": [
  L("Δημοσιογράφος", "f", "Όποιος ανοίξει ένα βιβλίο βυζαντινής μουσικής βλέπει σημάδια που δεν μοιάζουν καθόλου με τις γνωστές νότες. Τι ακριβώς διαβάζει ο ψάλτης;", "Anyone who opens a book of Byzantine music sees signs that look nothing like familiar notes. What exactly does the cantor read?"),
  L("Ερευνητής", "m", "Τα σημάδια αυτά λέγονται νεύματα, και η βασική τους διαφορά από το δυτικό πεντάγραμμο είναι ότι δεν δείχνουν απόλυτο ύψος αλλά κίνηση. Λένε στον ψάλτη: ανέβα ένα βήμα, κατέβα δύο, μείνε στον ίδιο φθόγγο. Η μελωδία είναι, ας πούμε, ένα ταξίδι που περιγράφεται από τη μια στάση στην άλλη.", "These signs are called neumes, and their basic difference from the Western stave is that they don't show absolute pitch but movement. They tell the cantor: go up one step, go down two, stay on the same note. The melody is, so to speak, a journey described from one stop to the next."),
  L("Δημοσιογράφος", "f", "Και πώς ξέρει από ποια νότα να ξεκινήσει;", "And how does he know which note to start from?"),
  L("Ερευνητής", "m", "Από τον ήχο. Η βυζαντινή μουσική οργανώνεται σε οκτώ ήχους, την Οκτώηχο, κάθε ένας με τη δική του κλίμακα και τον δικό του χαρακτήρα. Και οι κλίμακες αυτές δεν χωρίζονται σε ίσα ημιτόνια, όπως το πιάνο· έχουν διαστήματα μικρότερα ή μεγαλύτερα, που ένα δυτικό αυτί μπορεί να τα ακούσει σαν «φάλτσα», ενώ είναι απολύτως σκόπιμα.", "From the mode. Byzantine music is organised in eight modes, the Octoechos, each with its own scale and its own character. And these scales aren't divided into equal semitones, like the piano; they have smaller or larger intervals, which a Western ear may hear as 'out of tune', though they're entirely deliberate."),
  L("Δημοσιογράφος", "f", "Η σημειογραφία που χρησιμοποιείται σήμερα είναι η ίδια με του Βυζαντίου;", "Is the notation used today the same as Byzantium's?"),
  L("Ερευνητής", "m", "Όχι ακριβώς. Το 1814 τρεις δάσκαλοι στην Κωνσταντινούπολη, ο Χρύσανθος, ο Γρηγόριος και ο Χουρμούζιος, απλοποίησαν το σύστημα, που είχε γίνει εξαιρετικά περίπλοκο, και μετέγραψαν χιλιάδες σελίδες παλαιότερων μελών. Η λεγόμενη «Νέα Μέθοδος» είναι αυτή που διδάσκεται ακόμα. Το 2019, μάλιστα, η βυζαντινή ψαλτική εγγράφηκε στον κατάλογο της άυλης πολιτιστικής κληρονομιάς της UNESCO, με κοινή πρόταση Ελλάδας και Κύπρου. Για μένα, όμως, η μεγαλύτερη αναγνώριση είναι όταν ένα παιδί σε μια ενορία μαθαίνει να διαβάζει αυτά τα σημάδια και τα κάνει φωνή.", "Not exactly. In 1814 three teachers in Constantinople, Chrysanthos, Gregorios and Chourmouzios, simplified the system, which had become extremely complicated, and transcribed thousands of pages of older chants. The so-called 'New Method' is the one still taught. In 2019, in fact, Byzantine chant was inscribed on UNESCO's list of intangible cultural heritage, on a joint proposal by Greece and Cyprus. For me, though, the greatest recognition is when a child in a parish learns to read these signs and turns them into voice."),
 ],
 "questions": [
  Q("Ποια είναι η βασική διαφορά των νευμάτων από το δυτικό πεντάγραμμο;", ["Γράφονται από δεξιά προς τα αριστερά", "Δείχνουν κίνηση και όχι απόλυτο ύψος", "Δείχνουν μόνο τον ρυθμό", "Χρησιμοποιούν γράμματα αντί για σύμβολα"], 1, "δεν δείχνουν απόλυτο ύψος αλλά κίνηση"),
  Q("Τι είναι η Οκτώηχος;", ["Ένα μουσικό όργανο", "Το σύστημα των οκτώ ήχων της βυζαντινής μουσικής", "Μια χορωδία οκτώ ψαλτών", "Ένα βιβλίο με οκτώ ύμνους"], 1, "Η βυζαντινή μουσική οργανώνεται σε οκτώ ήχους, την Οκτώηχο"),
  Q("Γιατί ένα δυτικό αυτί μπορεί να ακούσει κάποια διαστήματα σαν «φάλτσα»;", ["Γιατί οι ψάλτες κάνουν λάθη", "Γιατί οι κλίμακες δεν χωρίζονται σε ίσα ημιτόνια", "Γιατί η μουσική είναι πολύ γρήγορη", "Γιατί δεν υπάρχει μελωδία"], 1, "οι κλίμακες αυτές δεν χωρίζονται σε ίσα ημιτόνια"),
  Q("Τι έκαναν οι τρεις δάσκαλοι το 1814;", ["Ίδρυσαν ένα ωδείο", "Απλοποίησαν το σύστημα σημειογραφίας", "Έγραψαν την Οκτώηχο", "Μετέφρασαν ύμνους στα λατινικά"], 1, "απλοποίησαν το σύστημα, που είχε γίνει εξαιρετικά περίπλοκο"),
 ],
 "gloss": {"σημειογραφία": "σημειογραφία — (musical) notation", "ψάλτης": "ψάλτης — cantor", "νεύματα": "νεύμα — neume; nod", "πεντάγραμμο": "πεντάγραμμο — stave", "φθόγγο": "φθόγγος — note, tone", "ημιτόνια": "ημιτόνιο — semitone", "φάλτσα": "φάλτσος — out of tune", "σκόπιμα": "σκόπιμος — deliberate", "μελών": "μέλος — melody, chant (also: member)", "άυλης": "άυλος — intangible", "ενορία": "ενορία — parish"},
})
rnd = random.Random(214)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-214.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
