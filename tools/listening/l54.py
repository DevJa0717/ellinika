# Source for library/listening/listening-54.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l54.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l54-ann-kafsonas", "title": "Κλειστός ο αρχαιολογικός χώρος λόγω καύσωνα", "title_en": "Archaeological site closed because of the heatwave", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε στην είσοδο ενός αρχαιολογικού χώρου ένα καλοκαιρινό μεσημέρι. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Ανακοίνωση", "f", "Αγαπητοί επισκέπτες, λόγω του καύσωνα και με απόφαση του Υπουργείου Πολιτισμού, ο αρχαιολογικός χώρος θα παραμείνει κλειστός σήμερα από τις δώδεκα το μεσημέρι έως τις πέντε το απόγευμα. Οι επισκέπτες που βρίσκονται ήδη μέσα παρακαλούνται να κατευθυνθούν σταδιακά προς την έξοδο.", "Dear visitors, because of the heatwave and by decision of the Ministry of Culture, the archaeological site will remain closed today from twelve noon until five in the afternoon. Visitors who are already inside are requested to make their way gradually towards the exit."),
  L("Ανακοίνωση", "f", "Όσοι έχουν αγοράσει ηλεκτρονικό εισιτήριο για τις ώρες αυτές μπορούν να το χρησιμοποιήσουν το απόγευμα, από τις πέντε μέχρι τις οκτώ, χωρίς καμία επιπλέον χρέωση. Το μουσείο του χώρου, που διαθέτει κλιματισμό, θα λειτουργεί κανονικά.", "Those who have bought an e-ticket for these hours can use it in the afternoon, from five to eight, at no extra charge. The site museum, which is air-conditioned, will operate as normal."),
  L("Ανακοίνωση", "f", "Σας υπενθυμίζουμε να πίνετε άφθονο νερό και να φοράτε καπέλο. Στο κυλικείο δίπλα στην είσοδο θα βρείτε δροσερό νερό δωρεάν. Ευχαριστούμε για την κατανόηση.", "We remind you to drink plenty of water and wear a hat. At the snack bar next to the entrance you will find cool water free of charge. Thank you for your understanding."),
 ],
 "questions": [
  Q("Πότε θα είναι κλειστός ο αρχαιολογικός χώρος;", ["Όλη την ημέρα", "Από τις δώδεκα έως τις πέντε", "Από τις πέντε έως τις οκτώ", "Μόνο το πρωί"], 1, "θα παραμείνει κλειστός σήμερα από τις δώδεκα το μεσημέρι έως τις πέντε το απόγευμα"),
  Q("Τι μπορούν να κάνουν όσοι έχουν ηλεκτρονικό εισιτήριο για αυτές τις ώρες;", ["Να πάρουν πίσω τα χρήματά τους", "Να το χρησιμοποιήσουν το απόγευμα χωρίς επιπλέον χρέωση", "Να έρθουν αύριο", "Να μπουν μόνο στο μουσείο"], 1, "μπορούν να το χρησιμοποιήσουν το απόγευμα, από τις πέντε μέχρι τις οκτώ, χωρίς καμία επιπλέον χρέωση"),
  Q("Τι θα βρουν οι επισκέπτες στο κυλικείο;", ["Καπέλα", "Δροσερό νερό δωρεάν", "Εισιτήρια", "Αντηλιακό"], 1, "Στο κυλικείο δίπλα στην είσοδο θα βρείτε δροσερό νερό δωρεάν"),
 ],
 "gloss": {"καύσωνα": "καύσωνας — heatwave", "κατευθυνθούν": "κατευθύνομαι — to head (towards)", "σταδιακά": "σταδιακά — gradually", "επιπλέον χρέωση": "επιπλέον χρέωση — extra charge", "κλιματισμό": "κλιματισμός — air conditioning", "υπενθυμίζουμε": "υπενθυμίζω — to remind", "άφθονο": "άφθονος — plenty of", "κυλικείο": "κυλικείο — snack bar, canteen", "κατανόηση": "κατανόηση — understanding"},
})

ITEMS.append({
 "id": "l54-vm-piano", "title": "Μήνυμα από τη δασκάλα του πιάνου", "title_en": "A message from the piano teacher", "type": "voicemail", "level": "B2",
 "context_el": "Η κόρη σας κάνει μαθήματα πιάνου. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τη δασκάλα της.",
 "script": [
  L("Δασκάλα", "f", "Καλησπέρα σας, κυρία Δημητρίου, η Αλίκη είμαι, η δασκάλα του πιάνου της Μυρτώς. Ήθελα να σας πω ότι η Μυρτώ έχει προοδεύσει πάρα πολύ φέτος, και σκέφτομαι να τη δηλώσω στις εξετάσεις του ωδείου τον Ιούνιο, για το πρώτο πτυχίο.", "Good evening, Mrs Dimitriou, it's Aliki, Myrto's piano teacher. I wanted to tell you that Myrto has made great progress this year, and I'm thinking of entering her for the conservatory exams in June, for the first certificate."),
  L("Δασκάλα", "f", "Αυτό σημαίνει, βέβαια, ότι θα πρέπει να μελετάει λίγο περισσότερο, τουλάχιστον μισή ώρα κάθε μέρα, και ίσως να προσθέσουμε ένα δεύτερο μάθημα την εβδομάδα από τον Μάρτιο. Δεν θέλω να την πιέσω, γι' αυτό καλό θα ήταν να το συζητήσετε πρώτα μαζί της.", "This means, of course, that she'll need to practise a little more, at least half an hour every day, and perhaps we'll add a second lesson a week from March. I don't want to pressure her, so it would be good if you discussed it with her first."),
  L("Δασκάλα", "f", "Οι δηλώσεις για τις εξετάσεις κλείνουν στις δεκαπέντε Ιανουαρίου. Πάρτε με όποτε μπορείτε, εκτός από την Πέμπτη, που έχω μαθήματα όλη μέρα. Καλό βράδυ!", "Registration for the exams closes on the fifteenth of January. Call me whenever you can, except on Thursday, when I have lessons all day. Good evening!"),
 ],
 "questions": [
  Q("Τι προτείνει η δασκάλα για τη Μυρτώ;", ["Να σταματήσει τα μαθήματα", "Να δώσει εξετάσεις στο ωδείο τον Ιούνιο", "Να αλλάξει όργανο", "Να παίξει σε μια συναυλία τον Μάρτιο"], 1, "σκέφτομαι να τη δηλώσω στις εξετάσεις του ωδείου τον Ιούνιο"),
  Q("Γιατί θέλει η δασκάλα να μιλήσει πρώτα η μητέρα με τη Μυρτώ;", ["Γιατί τα μαθήματα είναι ακριβά", "Γιατί δεν θέλει να την πιέσει", "Γιατί η Μυρτώ είναι άρρωστη", "Γιατί η ίδια θα λείψει"], 1, "Δεν θέλω να την πιέσω, γι' αυτό καλό θα ήταν να το συζητήσετε πρώτα μαζί της"),
  Q("Πότε δεν μπορεί να μιλήσει στο τηλέφωνο η δασκάλα;", ["Τη Δευτέρα", "Την Πέμπτη", "Το Σαββατοκύριακο", "Μετά τις δεκαπέντε Ιανουαρίου"], 1, "εκτός από την Πέμπτη, που έχω μαθήματα όλη μέρα"),
 ],
 "gloss": {"έχει προοδεύσει": "προοδεύω — to make progress", "δηλώσω": "δηλώνω — to enter, register (someone for)", "ωδείου": "ωδείο — conservatory, music school", "πτυχίο": "πτυχίο — certificate, diploma", "μελετάει": "μελετάω — to practise; to study", "πιέσω": "πιέζω — to pressure", "δηλώσεις": "δήλωση — registration; statement"},
})

ITEMS.append({
 "id": "l54-dia-christougenna", "title": "Πού θα κάνουμε Χριστούγεννα;", "title_en": "Where shall we spend Christmas?", "type": "dialogue", "level": "B2",
 "context_el": "Η Νεφέλη και ο Άρης συζητούν πού θα περάσουν τα Χριστούγεννα με τα παιδιά τους.",
 "script": [
  L("Νεφέλη", "f", "Άρη, πρέπει να αποφασίσουμε για τα Χριστούγεννα. Η μητέρα μου ρωτάει κάθε μέρα αν θα πάμε στη Λάρισα.", "Aris, we have to decide about Christmas. My mother asks every day whether we're going to Larissa."),
  L("Άρης", "m", "Πέρσι όμως ήμασταν στους δικούς σου. Οι γονείς μου στην Καλαμάτα έχουν να δουν τα παιδιά από το Πάσχα.", "But last year we were with your family. My parents in Kalamata haven't seen the children since Easter."),
  L("Νεφέλη", "f", "Το ξέρω. Αλλά φέτος είναι και ο παππούς μου άρρωστος, και δεν ξέρουμε πόσα Χριστούγεννα του μένουν ακόμη.", "I know. But this year my grandfather is ill too, and we don't know how many more Christmases he has left."),
  L("Άρης", "m", "Έχεις δίκιο... Τι λες να το μοιράσουμε; Παραμονή και ανήμερα Χριστουγέννων στη Λάρισα, και την Πρωτοχρονιά στην Καλαμάτα.", "You're right... What if we split it? Christmas Eve and Christmas Day in Larissa, and New Year in Kalamata."),
  L("Νεφέλη", "f", "Θα είναι πολύ κουραστικό με τα παιδιά, οχτώ ώρες δρόμος. Και αν το κάναμε αλλιώς; Να καλέσουμε τους γονείς σου εδώ, στην Αθήνα, για την Πρωτοχρονιά.", "It'll be very tiring with the kids, eight hours on the road. What if we did it differently? We could invite your parents here, to Athens, for New Year."),
  L("Άρης", "m", "Καλή ιδέα. Η μητέρα μου θα χαρεί που θα δει το καινούργιο σπίτι. Μόνο που θα θέλει να μαγειρέψει εκείνη!", "Good idea. My mother will be glad to see the new house. Only she'll want to do the cooking herself!"),
 ],
 "questions": [
  Q("Γιατί ο Άρης θέλει να πάνε στην Καλαμάτα;", ["Γιατί εκεί έχει καλύτερο καιρό", "Γιατί οι γονείς του δεν έχουν δει τα παιδιά από το Πάσχα", "Γιατί ο παππούς του είναι άρρωστος", "Γιατί έχουν μεγαλύτερο σπίτι"], 1, "Οι γονείς μου στην Καλαμάτα έχουν να δουν τα παιδιά από το Πάσχα"),
  Q("Γιατί η Νεφέλη δεν θέλει να ταξιδέψουν και στις δύο πόλεις;", ["Γιατί κοστίζει πολύ", "Γιατί θα είναι πολύ κουραστικό με τα παιδιά", "Γιατί δουλεύει την Πρωτοχρονιά", "Γιατί δεν έχουν αυτοκίνητο"], 1, "Θα είναι πολύ κουραστικό με τα παιδιά, οχτώ ώρες δρόμος"),
  Q("Τι αποφασίζουν τελικά για την Πρωτοχρονιά;", ["Να πάνε στην Καλαμάτα", "Να καλέσουν τους γονείς του Άρη στην Αθήνα", "Να μείνουν στη Λάρισα", "Να πάνε ταξίδι μόνοι τους"], 1, "Να καλέσουμε τους γονείς σου εδώ, στην Αθήνα, για την Πρωτοχρονιά"),
 ],
 "gloss": {"στους δικούς σου": "οι δικοί σου — your family, your folks", "έχουν να δουν": "έχω να δω κάποιον από — not to have seen someone since", "του μένουν": "μου μένει — I have (something) left", "Παραμονή": "παραμονή — eve", "ανήμερα": "ανήμερα — on the day itself", "Πρωτοχρονιά": "Πρωτοχρονιά — New Year's Day", "κουραστικό": "κουραστικός — tiring"},
})

ITEMS.append({
 "id": "l54-dia-antiliako", "title": "Στο φαρμακείο για αντηλιακό", "title_en": "At the pharmacy for sunscreen", "type": "dialogue", "level": "B2",
 "context_el": "Ο Θοδωρής πηγαίνει σε ένα φαρμακείο πριν φύγει για διακοπές με τον μικρό του γιο.",
 "script": [
  L("Θοδωρής", "m", "Καλημέρα. Θέλω ένα αντηλιακό για τον γιο μου. Είναι τριών χρονών και έχει πολύ ευαίσθητο δέρμα.", "Good morning. I'd like a sunscreen for my son. He's three and has very sensitive skin."),
  L("Φαρμακοποιός", "f", "Για παιδιά αυτής της ηλικίας προτείνω ένα με δείκτη προστασίας πενήντα, ειδικό για παιδικό δέρμα, χωρίς άρωμα. Αυτό εδώ είναι και αδιάβροχο, αλλά πρέπει να το ξαναβάζετε κάθε δύο ώρες και μετά από κάθε μπάνιο.", "For children this age I suggest one with protection factor fifty, specially for children's skin, without perfume. This one is also waterproof, but you need to reapply it every two hours and after every swim."),
  L("Θοδωρής", "m", "Κάθε δύο ώρες; Νόμιζα ότι το αδιάβροχο κρατάει όλη μέρα.", "Every two hours? I thought waterproof lasted all day."),
  L("Φαρμακοποιός", "f", "Δυστυχώς όχι, αυτό είναι μια συνηθισμένη παρανόηση. Και καλύτερα να μην είναι στον ήλιο από τις έντεκα μέχρι τις τέσσερις, όταν η ακτινοβολία είναι πιο έντονη. Ένα καπέλο και ένα μπλουζάκι με μανίκια προστατεύουν περισσότερο από οποιοδήποτε αντηλιακό.", "Unfortunately not, that's a common misconception. And it's better for him not to be in the sun from eleven to four, when the radiation is strongest. A hat and a T-shirt with sleeves protect more than any sunscreen."),
  L("Θοδωρής", "m", "Εντάξει. Και αν καεί παρ' όλα αυτά;", "OK. And if he gets burnt despite all that?"),
  L("Φαρμακοποιός", "f", "Δροσερές κομπρέσες και αυτή την κρέμα με αλόη. Αν όμως βγάλει φουσκάλες ή πυρετό, πηγαίνετε αμέσως σε γιατρό.", "Cool compresses and this cream with aloe. But if he gets blisters or a fever, go to a doctor straight away."),
 ],
 "questions": [
  Q("Ποια είναι η παρανόηση του Θοδωρή;", ["Ότι τα παιδιά δεν χρειάζονται αντηλιακό", "Ότι το αδιάβροχο αντηλιακό κρατάει όλη μέρα", "Ότι το άρωμα κάνει καλό", "Ότι ο δείκτης δεν έχει σημασία"], 1, "Νόμιζα ότι το αδιάβροχο κρατάει όλη μέρα"),
  Q("Τι προστατεύει, σύμφωνα με τη φαρμακοποιό, περισσότερο από οποιοδήποτε αντηλιακό;", ["Η σκιά μιας ομπρέλας", "Ένα καπέλο και ένα μπλουζάκι με μανίκια", "Το μπάνιο στη θάλασσα", "Τα γυαλιά ηλίου"], 1, "Ένα καπέλο και ένα μπλουζάκι με μανίκια προστατεύουν περισσότερο από οποιοδήποτε αντηλιακό"),
  Q("Πότε πρέπει να πάει το παιδί σε γιατρό;", ["Αν κοκκινίσει λίγο", "Αν βγάλει φουσκάλες ή πυρετό", "Μετά από κάθε μπάνιο", "Αν δεν του αρέσει η κρέμα"], 1, "Αν όμως βγάλει φουσκάλες ή πυρετό, πηγαίνετε αμέσως σε γιατρό"),
 ],
 "gloss": {"αντηλιακό": "αντηλιακό — sunscreen", "ευαίσθητο": "ευαίσθητος — sensitive", "δείκτη προστασίας": "δείκτης προστασίας — (sun) protection factor", "αδιάβροχο": "αδιάβροχος — waterproof", "παρανόηση": "παρανόηση — misunderstanding, misconception", "ακτινοβολία": "ακτινοβολία — radiation", "καεί": "καίγομαι — to get burnt", "κομπρέσες": "κομπρέσα — compress", "φουσκάλες": "φουσκάλα — blister"},
})

ITEMS.append({
 "id": "l54-int-artopoios", "title": "Ο φούρναρης της γειτονιάς", "title_en": "The neighbourhood baker", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με τον Παντελή, που έχει έναν μικρό φούρνο σε μια γειτονιά του Πειραιά.",
 "script": [
  L("Δημοσιογράφος", "f", "Παντελή, τι ώρα ξεκινάει η μέρα σας;", "Pantelis, what time does your day start?"),
  L("Παντελής", "m", "Στις τρεις τα ξημερώματα. Το προζύμι το έχω ετοιμάσει από το προηγούμενο βράδυ, οπότε πρώτα ζυμώνω, μετά αφήνω τη ζύμη να φουσκώσει και στις πέντε μπαίνουν τα πρώτα ψωμιά στον φούρνο. Στις έξι και μισή που ανοίγω, η ουρά έχει ήδη φτάσει στη γωνία.", "At three in the morning. I've prepared the sourdough starter the night before, so first I knead, then I let the dough rise, and at five the first loaves go into the oven. At half past six when I open, the queue has already reached the corner."),
  L("Δημοσιογράφος", "f", "Ο φούρνος είναι οικογενειακός;", "Is the bakery a family business?"),
  L("Παντελής", "m", "Τον άνοιξε ο παππούς μου το 1958, όταν ήρθε από την Κεφαλονιά. Τον ξύλινο φούρνο τον κρατήσαμε, αν και θα ήταν πολύ πιο εύκολο να βάλουμε ηλεκτρικό. Το ψωμί από ξύλα έχει άλλη γεύση και κρατάει περισσότερες μέρες.", "My grandfather opened it in 1958, when he came from Kefalonia. We kept the wood-fired oven, although it would be much easier to put in an electric one. Bread from a wood oven tastes different and keeps for more days."),
  L("Δημοσιογράφος", "f", "Οι μεγάλες αλυσίδες δεν σας ανησυχούν;", "Don't the big chains worry you?"),
  L("Παντελής", "m", "Στην αρχή ναι. Αλλά οι πελάτες μου δεν έρχονται μόνο για το ψωμί. Έρχονται για να πουν δυο κουβέντες, να μάθουν τα νέα της γειτονιάς. Ο φούρνος είναι κάτι σαν το παλιό καφενείο. Αυτό δεν μπορεί να το προσφέρει καμία αλυσίδα.", "At first, yes. But my customers don't come only for the bread. They come to have a chat, to find out the neighbourhood news. The bakery is something like the old café. No chain can offer that."),
 ],
 "questions": [
  Q("Τι κάνει ο Παντελής το προηγούμενο βράδυ;", ["Καθαρίζει τον φούρνο", "Ετοιμάζει το προζύμι", "Ψήνει τα κουλούρια", "Παραγγέλνει αλεύρι"], 1, "Το προζύμι το έχω ετοιμάσει από το προηγούμενο βράδυ"),
  Q("Γιατί κράτησαν τον ξύλινο φούρνο;", ["Γιατί ένας ηλεκτρικός είναι ακριβός", "Γιατί το ψωμί από ξύλα έχει άλλη γεύση και κρατάει περισσότερο", "Γιατί το απαιτεί ο νόμος", "Γιατί δεν υπάρχει χώρος"], 1, "Το ψωμί από ξύλα έχει άλλη γεύση και κρατάει περισσότερες μέρες"),
  Q("Γιατί δεν ανησυχεί πια για τις αλυσίδες;", ["Γιατί έχει χαμηλότερες τιμές", "Γιατί οι πελάτες έρχονται και για την κουβέντα και τα νέα της γειτονιάς", "Γιατί άνοιξε και δεύτερο κατάστημα", "Γιατί πουλάει και στο διαδίκτυο"], 1, "οι πελάτες μου δεν έρχονται μόνο για το ψωμί. Έρχονται για να πουν δυο κουβέντες"),
 ],
 "gloss": {"τα ξημερώματα": "τα ξημερώματα — the small hours, daybreak", "προζύμι": "προζύμι — sourdough starter", "ζυμώνω": "ζυμώνω — to knead", "φουσκώσει": "φουσκώνω — to rise (of dough)", "ουρά": "ουρά — queue; tail", "ξύλινο": "ξύλινος — wooden; (of an oven) wood-fired", "αλυσίδες": "αλυσίδα — (shop) chain", "δυο κουβέντες": "λέω δυο κουβέντες — to have a chat"},
})

ITEMS.append({
 "id": "l54-rep-anafiotika", "title": "Τα Αναφιώτικα", "title_en": "Anafiotika", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από τα Αναφιώτικα, μια μικρή γειτονιά κάτω από την Ακρόπολη.",
 "script": [
  L("Ρεπόρτερ", "f", "Λίγα μέτρα πάνω από την πολύβουη Πλάκα, κάτω από τους βράχους της Ακρόπολης, ο θόρυβος της πόλης σβήνει. Περπατώ σε στενά σοκάκια ανάμεσα σε μικρά άσπρα σπίτια με μπλε πόρτες και γλάστρες με βασιλικό. Θα νόμιζε κανείς ότι βρίσκεται σε ένα νησί των Κυκλάδων.", "A few metres above bustling Plaka, beneath the rocks of the Acropolis, the noise of the city fades away. I'm walking through narrow alleys between little white houses with blue doors and pots of basil. You'd think you were on a Cycladic island."),
  L("Ρεπόρτερ", "f", "Και κατά κάποιον τρόπο είναι. Τα Αναφιώτικα τα έχτισαν τον 19ο αιώνα μάστορες από την Ανάφη, που είχαν έρθει στην Αθήνα για να δουλέψουν στις οικοδομές της νέας πρωτεύουσας. Επειδή δεν είχαν χρήματα για σπίτι, έχτιζαν τα δικά τους, συχνά μέσα σε μία νύχτα, πάνω στην πλαγιά του βράχου, όπως τα σπίτια του νησιού τους.", "And in a way it is. Anafiotika was built in the 19th century by builders from Anafi who had come to Athens to work on the buildings of the new capital. Because they had no money for a house, they built their own, often in a single night, on the slope of the rock, like the houses of their island."),
  L("Ρεπόρτερ", "f", "Σήμερα στη γειτονιά μένουν ελάχιστοι μόνιμοι κάτοικοι. Πολλά σπίτια είναι κλειστά, ενώ οι τουρίστες γεμίζουν τα σοκάκια όλη μέρα. Οι λίγοι κάτοικοι ζητούν από τους επισκέπτες κάτι απλό: να μιλούν χαμηλόφωνα, γιατί πίσω από αυτές τις μπλε πόρτες ζουν ακόμη άνθρωποι.", "Today very few permanent residents live in the neighbourhood. Many houses are shut, while tourists fill the alleys all day long. The few residents ask visitors for something simple: to speak quietly, because behind these blue doors people still live."),
 ],
 "questions": [
  Q("Με τι μοιάζουν τα Αναφιώτικα;", ["Με ένα ορεινό χωριό", "Με ένα νησί των Κυκλάδων", "Με μια σύγχρονη γειτονιά", "Με ένα αρχαίο θέατρο"], 1, "Θα νόμιζε κανείς ότι βρίσκεται σε ένα νησί των Κυκλάδων"),
  Q("Ποιοι έχτισαν τα Αναφιώτικα;", ["Αρχιτέκτονες από τη Γερμανία", "Μάστορες από την Ανάφη που δούλευαν στις οικοδομές της Αθήνας", "Ψαράδες από τον Πειραιά", "Μοναχοί"], 1, "Τα Αναφιώτικα τα έχτισαν τον 19ο αιώνα μάστορες από την Ανάφη"),
  Q("Τι ζητούν οι κάτοικοι από τους επισκέπτες;", ["Να μη βγάζουν φωτογραφίες", "Να μιλούν χαμηλόφωνα", "Να πληρώνουν εισιτήριο", "Να μην έρχονται το βράδυ"], 1, "να μιλούν χαμηλόφωνα, γιατί πίσω από αυτές τις μπλε πόρτες ζουν ακόμη άνθρωποι"),
 ],
 "gloss": {"πολύβουη": "πολύβουος — bustling, noisy", "σβήνει": "σβήνω — to fade away, go out", "σοκάκια": "σοκάκι — alley, lane", "βασιλικό": "βασιλικός — basil", "μάστορες": "μάστορας — builder, craftsman", "οικοδομές": "οικοδομή — building (site), construction", "πλαγιά": "πλαγιά — slope", "μόνιμοι κάτοικοι": "μόνιμος κάτοικος — permanent resident", "χαμηλόφωνα": "χαμηλόφωνα — in a low voice, quietly"},
})

ITEMS.append({
 "id": "l54-dia-parking", "title": "Ο γείτονας και η θέση στάθμευσης", "title_en": "The neighbour and the parking space", "type": "dialogue", "level": "B2",
 "context_el": "Η κυρία Σοφία χτυπάει την πόρτα του καινούργιου γείτονά της, του Μιλτιάδη, για ένα πρόβλημα με την πυλωτή της πολυκατοικίας.",
 "script": [
  L("Σοφία", "f", "Καλησπέρα, συγγνώμη για την ενόχληση. Είμαι η Σοφία, από τον τρίτο. Το αυτοκίνητό σας είναι το γκρι;", "Good evening, sorry to bother you. I'm Sofia, from the third floor. Is the grey car yours?"),
  L("Μιλτιάδης", "m", "Ναι, καλησπέρα. Συμβαίνει κάτι;", "Yes, good evening. Is something wrong?"),
  L("Σοφία", "f", "Το έχετε παρκάρει στη θέση μου στην πυλωτή. Κάθε διαμέρισμα έχει τη δική του θέση, και η δική σας είναι η τελευταία, δίπλα στις αποθήκες.", "You've parked it in my space under the building. Each flat has its own space, and yours is the last one, next to the storerooms."),
  L("Μιλτιάδης", "m", "Α, ζητώ συγγνώμη! Δεν το ήξερα. Ο προηγούμενος ένοικος μου είπε ότι παρκάρει όποιος έρθει πρώτος.", "Oh, I'm sorry! I didn't know. The previous tenant told me whoever comes first parks."),
  L("Σοφία", "f", "Όχι, όχι, οι θέσεις είναι γραμμένες στο συμβόλαιο. Μην ανησυχείτε, δεν έγινε τίποτα. Απλώς σήμερα έφερα ψώνια και έπρεπε να παρκάρω δύο τετράγωνα μακριά.", "No, no, the spaces are written in the deeds. Don't worry, nothing happened. It's just that today I brought shopping and had to park two blocks away."),
  L("Μιλτιάδης", "m", "Το μετακινώ αμέσως. Και αν χρειαστείτε ποτέ βοήθεια με τα ψώνια, χτυπήστε μου. Μένω ακριβώς από κάτω σας.", "I'll move it straight away. And if you ever need help with the shopping, knock on my door. I live right below you."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα;", ["Ο Μιλτιάδης κάνει θόρυβο", "Ο Μιλτιάδης έχει παρκάρει στη θέση της Σοφίας", "Το αυτοκίνητο του Μιλτιάδη έχει χτυπήσει", "Η πυλωτή είναι κλειστή"], 1, "Το έχετε παρκάρει στη θέση μου στην πυλωτή"),
  Q("Γιατί ο Μιλτιάδης παρκάρισε εκεί;", ["Γιατί η δική του θέση ήταν πιασμένη", "Γιατί ο προηγούμενος ένοικος του είπε ότι παρκάρει όποιος έρθει πρώτος", "Γιατί βιαζόταν", "Γιατί δεν βρήκε τις αποθήκες"], 1, "Ο προηγούμενος ένοικος μου είπε ότι παρκάρει όποιος έρθει πρώτος"),
  Q("Τι προσφέρεται να κάνει ο Μιλτιάδης;", ["Να πληρώσει πρόστιμο", "Να τη βοηθάει με τα ψώνια", "Να ανταλλάξουν θέσεις", "Να μιλήσει στον διαχειριστή"], 1, "αν χρειαστείτε ποτέ βοήθεια με τα ψώνια, χτυπήστε μου"),
 ],
 "gloss": {"πυλωτή": "πυλωτή — open ground floor of a block, used for parking", "ενόχληση": "ενόχληση — bother, disturbance", "αποθήκες": "αποθήκη — storeroom", "ένοικος": "ένοικος — tenant, occupant", "τετράγωνα": "τετράγωνο — (city) block", "μετακινώ": "μετακινώ — to move", "χτυπήστε μου": "χτυπάω σε κάποιον — to knock on someone's door"},
})

ITEMS.append({
 "id": "l54-mono-benaki", "title": "Ξενάγηση στο Μουσείο Μπενάκη", "title_en": "A tour of the Benaki Museum", "type": "monologue", "level": "B2",
 "context_el": "Επισκέπτεστε το Μουσείο Μπενάκη στην Αθήνα με μια ομάδα. Θα ακούσετε την ξεναγό στην αρχή της ξενάγησης.",
 "script": [
  L("Ξεναγός", "f", "Καλώς ήρθατε στο Μουσείο Μπενάκη. Το κτίριο όπου βρισκόμαστε ήταν το σπίτι της οικογένειας Μπενάκη. Ο Αντώνης Μπενάκης, γιος ενός πλούσιου εμπόρου από την Αλεξάνδρεια, συγκέντρωνε έργα τέχνης σε όλη του τη ζωή, και το 1930 δώρισε το σπίτι και τις συλλογές του στο ελληνικό κράτος.", "Welcome to the Benaki Museum. The building we're in was the home of the Benakis family. Antonis Benakis, son of a wealthy merchant from Alexandria, collected works of art throughout his life, and in 1930 he donated the house and his collections to the Greek state."),
  L("Ξεναγός", "f", "Αυτό που κάνει το μουσείο μοναδικό είναι ότι καλύπτει όλη την ελληνική ιστορία, από την προϊστορία μέχρι τον 20ό αιώνα. Θα ξεκινήσουμε από το ισόγειο, με τα αρχαία και τα βυζαντινά, και θα ανεβαίνουμε όροφο όροφο προς τη νεότερη εποχή. Στον δεύτερο όροφο θα δείτε δύο ολόκληρα δωμάτια από αρχοντικά της Κοζάνης και της Σιάτιστας, που μεταφέρθηκαν εδώ κομμάτι κομμάτι.", "What makes the museum unique is that it covers the whole of Greek history, from prehistory to the 20th century. We'll start on the ground floor, with the ancient and Byzantine collections, and go up floor by floor towards the modern era. On the second floor you'll see two complete rooms from mansions in Kozani and Siatista, which were moved here piece by piece."),
  L("Ξεναγός", "f", "Η ξενάγηση θα διαρκέσει περίπου μιάμιση ώρα. Μπορείτε να φωτογραφίζετε, αλλά χωρίς φλας. Στο τέλος σας προτείνω να ανεβείτε στο καφέ της ταράτσας, που έχει μια από τις ωραιότερες θέες στον Εθνικό Κήπο.", "The tour will last about an hour and a half. You may take photographs, but without flash. At the end I suggest you go up to the rooftop café, which has one of the finest views over the National Garden."),
 ],
 "questions": [
  Q("Τι έκανε ο Αντώνης Μπενάκης το 1930;", ["Αγόρασε το κτίριο", "Δώρισε το σπίτι και τις συλλογές του στο κράτος", "Γύρισε από την Αλεξάνδρεια", "Έγινε διευθυντής του μουσείου"], 1, "το 1930 δώρισε το σπίτι και τις συλλογές του στο ελληνικό κράτος"),
  Q("Τι κάνει το μουσείο μοναδικό, σύμφωνα με την ξεναγό;", ["Το μέγεθός του", "Ότι καλύπτει όλη την ελληνική ιστορία", "Ότι έχει μόνο αρχαία", "Η δωρεάν είσοδος"], 1, "καλύπτει όλη την ελληνική ιστορία, από την προϊστορία μέχρι τον 20ό αιώνα"),
  Q("Τι θα δουν οι επισκέπτες στον δεύτερο όροφο;", ["Βυζαντινές εικόνες", "Δύο δωμάτια από αρχοντικά της Κοζάνης και της Σιάτιστας", "Ένα καφέ", "Σύγχρονη τέχνη"], 1, "Στον δεύτερο όροφο θα δείτε δύο ολόκληρα δωμάτια από αρχοντικά της Κοζάνης και της Σιάτιστας"),
 ],
 "gloss": {"ξεναγό": "ξεναγός — tour guide", "συγκέντρωνε": "συγκεντρώνω — to collect", "δώρισε": "δωρίζω — to donate", "συλλογές": "συλλογή — collection", "όροφο όροφο": "όροφο όροφο — floor by floor", "αρχοντικά": "αρχοντικό — mansion", "κομμάτι κομμάτι": "κομμάτι κομμάτι — piece by piece", "φλας": "φλας — flash (camera)", "ταράτσας": "ταράτσα — roof terrace"},
})

ITEMS.append({
 "id": "l54-c1-mimidia", "title": "Η γλώσσα των μιμιδίων", "title_en": "The language of memes", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν γλωσσολόγο για τα μιμίδια (memes) και τη γλώσσα του διαδικτύου.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Μαργαρίτη, μελετάτε τα μιμίδια, αυτές τις αστείες εικόνες με λεζάντες που κυκλοφορούν στο διαδίκτυο. Τι ενδιαφέρον μπορεί να έχουν για έναν γλωσσολόγο;", "Mr Margaritis, you study memes, those funny captioned images circulating on the internet. What interest can they hold for a linguist?"),
  L("Γλωσσολόγος", "m", "Πολύ μεγάλο. Ένα μιμίδιο είναι, κατά βάση, μια μορφή επικοινωνίας που βασίζεται σε κοινές γνώσεις. Για να το καταλάβεις, πρέπει να αναγνωρίσεις την εικόνα, να ξέρεις σε ποιο πλαίσιο χρησιμοποιείται συνήθως και να καταλάβεις πώς το συγκεκριμένο κείμενο παραλλάσσει αυτό το πρότυπο. Στην ουσία, είναι ένα παιχνίδι με κανόνες, σαν τις παροιμίες ή τα ανέκδοτα των παλαιότερων γενεών.", "A great deal. A meme is basically a form of communication based on shared knowledge. To understand one, you have to recognise the image, know the context in which it is usually used and understand how the particular text varies that template. In essence, it's a game with rules, like the proverbs or jokes of older generations."),
  L("Δημοσιογράφος", "f", "Πολλοί όμως θεωρούν ότι η γλώσσα του διαδικτύου φτωχαίνει τα ελληνικά.", "But many people think the language of the internet impoverishes Greek."),
  L("Γλωσσολόγος", "m", "Αυτός ο φόβος εκφράζεται σε κάθε εποχή, με κάθε νέο μέσο. Η έρευνα δείχνει ότι οι νέοι κινούνται με μεγάλη ευκολία ανάμεσα σε διαφορετικά επίπεδα ύφους: γράφουν αλλιώς σε ένα μιμίδιο, αλλιώς σε μια σχολική έκθεση. Αυτή η ικανότητα, να προσαρμόζεις τη γλώσσα στην περίσταση, είναι σημάδι γλωσσικής ωριμότητας, όχι φτώχειας. Άλλωστε, πολλά μιμίδια παίζουν με τα αρχαία, με την καθαρεύουσα ή με διαλέκτους, κάτι που προϋποθέτει μια αρκετά καλή γνώση τους.", "That fear is expressed in every era, with every new medium. Research shows that young people move with great ease between different levels of style: they write one way in a meme and another way in a school essay. This ability, to adapt language to the occasion, is a sign of linguistic maturity, not poverty. Besides, many memes play with ancient Greek, katharevousa or dialects, which presupposes a fairly good knowledge of them."),
  L("Δημοσιογράφος", "f", "Υπάρχει κάποια σκοτεινή πλευρά;", "Is there a dark side?"),
  L("Γλωσσολόγος", "m", "Ασφαλώς. Επειδή το χιούμορ λειτουργεί σαν ασπίδα, τα μιμίδια μπορούν να μεταφέρουν ρατσιστικά ή σεξιστικά μηνύματα με τρόπο που φαίνεται αθώος: «αστείο ήταν». Γι' αυτό πιστεύω ότι το σχολείο θα έπρεπε να τα χρησιμοποιεί, όχι για να τα απαγορεύσει, αλλά για να μάθουν τα παιδιά να τα διαβάζουν κριτικά.", "Certainly. Because humour works as a shield, memes can carry racist or sexist messages in a way that seems innocent: 'it was a joke'. That's why I believe schools should use them, not to ban them, but so that children learn to read them critically."),
 ],
 "questions": [
  Q("Τι χρειάζεται, κατά τον γλωσσολόγο, για να καταλάβει κανείς ένα μιμίδιο;", ["Καλή γνώση αγγλικών", "Κοινές γνώσεις: να αναγνωρίσει την εικόνα, το πλαίσιο και την παραλλαγή", "Ειδικό λογισμικό", "Να είναι κάτω από τριάντα χρονών"], 1, "πρέπει να αναγνωρίσεις την εικόνα, να ξέρεις σε ποιο πλαίσιο χρησιμοποιείται συνήθως και να καταλάβεις πώς το συγκεκριμένο κείμενο παραλλάσσει αυτό το πρότυπο"),
  Q("Με τι συγκρίνει τα μιμίδια;", ["Με τα διαφημιστικά σλόγκαν", "Με τις παροιμίες και τα ανέκδοτα των παλαιότερων γενεών", "Με τα αρχαία επιγράμματα", "Με τα σχολικά βιβλία"], 1, "σαν τις παροιμίες ή τα ανέκδοτα των παλαιότερων γενεών"),
  Q("Γιατί δεν πιστεύει ότι η γλώσσα του διαδικτύου φτωχαίνει τα ελληνικά;", ["Γιατί οι νέοι δεν χρησιμοποιούν το διαδίκτυο", "Γιατί οι νέοι προσαρμόζουν το ύφος τους στην περίσταση, κάτι που δείχνει ωριμότητα", "Γιατί τα μιμίδια γράφονται μόνο στα αγγλικά", "Γιατί το σχολείο απαγορεύει τα μιμίδια"], 1, "Αυτή η ικανότητα, να προσαρμόζεις τη γλώσσα στην περίσταση, είναι σημάδι γλωσσικής ωριμότητας"),
  Q("Ποια είναι, κατά τον ίδιο, η σωστή στάση του σχολείου απέναντι στα μιμίδια;", ["Να τα απαγορεύσει", "Να τα αγνοήσει", "Να τα χρησιμοποιεί για να μάθουν τα παιδιά να τα διαβάζουν κριτικά", "Να διδάσκει πώς να τα φτιάχνουν"], 2, "το σχολείο θα έπρεπε να τα χρησιμοποιεί, όχι για να τα απαγορεύσει, αλλά για να μάθουν τα παιδιά να τα διαβάζουν κριτικά"),
 ],
 "gloss": {"μιμίδια": "μιμίδιο — meme", "λεζάντες": "λεζάντα — caption", "κατά βάση": "κατά βάση — basically", "πλαίσιο": "πλαίσιο — context; frame", "παραλλάσσει": "παραλλάσσω — to vary, alter", "πρότυπο": "πρότυπο — template, model", "παροιμίες": "παροιμία — proverb", "επίπεδα ύφους": "επίπεδο ύφους — level of style, register", "περίσταση": "περίσταση — occasion, circumstance", "ωριμότητας": "ωριμότητα — maturity", "ασπίδα": "ασπίδα — shield", "κριτικά": "κριτικά — critically"},
})

ITEMS.append({
 "id": "l54-c1-ypsilantis", "title": "Αλέξανδρος Υψηλάντης", "title_en": "Alexandros Ypsilantis", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια ομιλία ενός ιστορικού για τον Αλέξανδρο Υψηλάντη και την αρχή της Επανάστασης του 1821.",
 "script": [
  L("Ιστορικός", "m", "Ο Αλέξανδρος Υψηλάντης γεννήθηκε το 1792 στην Κωνσταντινούπολη, σε μια φαναριώτικη οικογένεια με μεγάλη πολιτική παράδοση. Πολύ νέος κατατάχθηκε στον ρωσικό στρατό και στους ναπολεόντειους πολέμους έχασε το δεξί του χέρι. Η γενναιότητά του τον έφερε κοντά στον τσάρο Αλέξανδρο, του οποίου έγινε υπασπιστής.", "Alexandros Ypsilantis was born in 1792 in Constantinople, into a Phanariot family with a long political tradition. Very young, he enlisted in the Russian army, and in the Napoleonic wars he lost his right arm. His bravery brought him close to Tsar Alexander, whose aide-de-camp he became."),
  L("Ιστορικός", "m", "Το 1820 η Φιλική Εταιρεία, η μυστική οργάνωση που προετοίμαζε την επανάσταση, του πρότεινε την ηγεσία της, αφού ο Καποδίστριας είχε αρνηθεί. Ο Υψηλάντης δέχτηκε, πιστεύοντας, όπως και πολλοί Φιλικοί, ότι η Ρωσία τελικά θα στήριζε τον αγώνα. Τον Φεβρουάριο του 1821 πέρασε τον ποταμό Προύθο και κήρυξε την επανάσταση στη Μολδαβία.", "In 1820 the Filiki Eteria, the secret society preparing the revolution, offered him its leadership, since Kapodistrias had refused. Ypsilantis accepted, believing, like many members, that Russia would eventually support the struggle. In February 1821 he crossed the river Prut and proclaimed the revolution in Moldavia."),
  L("Ιστορικός", "m", "Οι ελπίδες του διαψεύστηκαν γρήγορα. Ο τσάρος καταδίκασε το κίνημα, οι ντόπιοι πληθυσμοί δεν ξεσηκώθηκαν όπως περίμενε, και στο Δραγατσάνι, τον Ιούνιο, ο Ιερός Λόχος, που αποτελούνταν κυρίως από νέους φοιτητές, σχεδόν εξοντώθηκε. Ο Υψηλάντης κατέφυγε στην Αυστρία, όπου φυλακίστηκε για έξι χρόνια. Αφέθηκε ελεύθερος άρρωστος και πέθανε στη Βιέννη το 1828, χωρίς να δει την ελεύθερη Ελλάδα.", "His hopes were soon dashed. The tsar condemned the movement, the local populations did not rise as he had expected, and at Dragatsani, in June, the Sacred Band, made up mainly of young students, was almost wiped out. Ypsilantis fled to Austria, where he was imprisoned for six years. He was released a sick man and died in Vienna in 1828, without seeing a free Greece."),
  L("Ιστορικός", "m", "Στρατιωτικά, το εγχείρημά του ήταν αποτυχία. Ιστορικά, όμως, η σημασία του ήταν τεράστια: η εξέγερση στις Παραδουνάβιες Ηγεμονίες απέσπασε οθωμανικές δυνάμεις και έδωσε το σήμα για την επανάσταση στην Πελοπόννησο, που ξέσπασε λίγες εβδομάδες αργότερα. Ο Υψηλάντης έχασε τη μάχη, αλλά άνοιξε τον δρόμο.", "Militarily, his venture was a failure. Historically, however, its significance was enormous: the uprising in the Danubian Principalities diverted Ottoman forces and gave the signal for the revolution in the Peloponnese, which broke out a few weeks later. Ypsilantis lost the battle, but he opened the way."),
 ],
 "questions": [
  Q("Πώς έχασε ο Υψηλάντης το δεξί του χέρι;", ["Σε ατύχημα στην Κωνσταντινούπολη", "Πολεμώντας στους ναπολεόντειους πολέμους", "Στη μάχη του Δραγατσανίου", "Στη φυλακή"], 1, "στους ναπολεόντειους πολέμους έχασε το δεξί του χέρι"),
  Q("Γιατί δέχτηκε την ηγεσία της Φιλικής Εταιρείας;", ["Γιατί του το ζήτησε ο τσάρος", "Γιατί πίστευε ότι η Ρωσία τελικά θα στήριζε τον αγώνα", "Γιατί ήθελε να γίνει βασιλιάς", "Γιατί τον πίεσε ο Καποδίστριας"], 1, "πιστεύοντας, όπως και πολλοί Φιλικοί, ότι η Ρωσία τελικά θα στήριζε τον αγώνα"),
  Q("Ποιο από τα παρακάτω ΔΕΝ αναφέρεται ως αιτία της αποτυχίας;", ["Ο τσάρος καταδίκασε το κίνημα", "Η έλλειψη χρημάτων", "Οι ντόπιοι δεν ξεσηκώθηκαν όπως περίμενε", "Η ήττα του Ιερού Λόχου στο Δραγατσάνι"], 1, "Αναφέρονται η καταδίκη από τον τσάρο, η στάση των ντόπιων και το Δραγατσάνι· όχι τα χρήματα"),
  Q("Ποια είναι, κατά τον ιστορικό, η ιστορική σημασία του εγχειρήματος;", ["Ότι οδήγησε στην απελευθέρωση της Μολδαβίας", "Ότι απέσπασε οθωμανικές δυνάμεις και έδωσε το σήμα για την επανάσταση στην Πελοπόννησο", "Ότι έφερε τη Ρωσία στον πόλεμο αμέσως", "Ότι έκανε τον Υψηλάντη κυβερνήτη"], 1, "απέσπασε οθωμανικές δυνάμεις και έδωσε το σήμα για την επανάσταση στην Πελοπόννησο"),
 ],
 "gloss": {"φαναριώτικη": "φαναριώτικος — Phanariot (Greek elite of the Phanar, Constantinople)", "κατατάχθηκε": "κατατάσσομαι — to enlist", "υπασπιστής": "υπασπιστής — aide-de-camp", "ηγεσία": "ηγεσία — leadership", "κήρυξε": "κηρύσσω — to proclaim, declare", "διαψεύστηκαν": "διαψεύδομαι — to be dashed, proved wrong", "κίνημα": "κίνημα — movement, uprising", "ξεσηκώθηκαν": "ξεσηκώνομαι — to rise up", "Ιερός Λόχος": "Ιερός Λόχος — the Sacred Band (1821)", "εξοντώθηκε": "εξοντώνομαι — to be wiped out", "Παραδουνάβιες Ηγεμονίες": "Παραδουνάβιες Ηγεμονίες — the Danubian Principalities (Moldavia, Wallachia)", "απέσπασε": "αποσπώ — to divert, draw away"},
})

rnd = random.Random(54)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-54.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
