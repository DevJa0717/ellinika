# Source for library/listening/listening-182.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l182.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l182-ann-touristiko-leoforeio", "title": "Στο τουριστικό λεωφορείο της πόλης", "title_en": "On the city sightseeing bus", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα ανοιχτό τουριστικό λεωφορείο και ακούτε μια ηχογραφημένη ανακοίνωση πριν από την αναχώρηση.",
 "script": [
  L("Εκφωνήτρια", "f", "Καλώς ήρθατε στο τουριστικό λεωφορείο της πόλης. Η πλήρης διαδρομή διαρκεί περίπου μία ώρα και τριάντα λεπτά και περνά από δεκατέσσερις στάσεις. Με το εισιτήριό σας μπορείτε να κατεβαίνετε και να ξανανεβαίνετε σε όποια στάση θέλετε, για είκοσι τέσσερις ώρες από την πρώτη επικύρωση.", "Welcome to the city sightseeing bus. The full route takes about an hour and thirty minutes and passes fourteen stops. With your ticket you can get off and back on at any stop you like, for twenty-four hours from the first validation."),
  L("Εκφωνήτρια", "f", "Τα ακουστικά βρίσκονται στη θήκη μπροστά σας. Συνδέστε τα στην υποδοχή δίπλα στο κάθισμά σας και επιλέξτε τη γλώσσα σας με το κουμπί· η ξενάγηση είναι διαθέσιμη σε δώδεκα γλώσσες. Στο πάνω κατάστρωμα παρακαλούμε να μένετε καθισμένοι όσο το λεωφορείο κινείται, και να προσέχετε τα κλαδιά των δέντρων.", "The headphones are in the pocket in front of you. Plug them into the socket next to your seat and choose your language with the button; the tour is available in twelve languages. On the upper deck please remain seated while the bus is moving, and watch out for tree branches."),
  L("Εκφωνήτρια", "f", "Το τελευταίο λεωφορείο της ημέρας ξεκινά από την κεντρική πλατεία στις έξι το απόγευμα. Αν θέλετε να ολοκληρώσετε τη διαδρομή, βεβαιωθείτε ότι θα βρίσκεστε σε κάποια στάση πριν από αυτή την ώρα. Σας ευχόμαστε καλή διασκέδαση!", "The last bus of the day leaves the central square at six in the evening. If you want to complete the route, make sure you are at a stop before that time. Enjoy your trip!"),
 ],
 "questions": [
  Q("Για πόσο ισχύει το εισιτήριο;", ["Για μία μόνο διαδρομή", "Για είκοσι τέσσερις ώρες από την πρώτη επικύρωση", "Για όλη την εβδομάδα", "Μέχρι τις έξι το απόγευμα της ίδιας μέρας"], 1, "για είκοσι τέσσερις ώρες από την πρώτη επικύρωση"),
  Q("Τι ζητείται από τους επιβάτες στο πάνω κατάστρωμα;", ["Να μην τρώνε", "Να μη φωτογραφίζουν", "Να μένουν καθισμένοι και να προσέχουν τα κλαδιά", "Να φορούν ζώνη"], 2, "Στο πάνω κατάστρωμα παρακαλούμε να μένετε καθισμένοι όσο το λεωφορείο κινείται, και να προσέχετε τα κλαδιά των δέντρων"),
  Q("Τι πρέπει να κάνει όποιος θέλει να ολοκληρώσει τη διαδρομή;", ["Να βρίσκεται σε μια στάση πριν από τις έξι", "Να αγοράσει δεύτερο εισιτήριο", "Να μείνει στο λεωφορείο χωρίς να κατέβει", "Να ενημερώσει τον οδηγό"], 0, "βεβαιωθείτε ότι θα βρίσκεστε σε κάποια στάση πριν από αυτή την ώρα"),
 ],
 "gloss": {"τουριστικό λεωφορείο": "τουριστικό λεωφορείο — sightseeing bus", "ξανανεβαίνετε": "ξανανεβαίνω — to get back on", "επικύρωση": "επικύρωση — validation", "ακουστικά": "ακουστικά — headphones", "θήκη": "θήκη — pocket, holder", "υποδοχή": "υποδοχή — socket", "κατάστρωμα": "κατάστρωμα — deck", "κλαδιά": "κλαδί — branch", "βεβαιωθείτε": "βεβαιώνομαι — to make sure"},
})

ITEMS.append({
 "id": "l182-int-pilotos-aerostatou", "title": "Ο πιλότος του αερόστατου", "title_en": "The hot-air balloon pilot", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν πιλότο αερόστατου σε μια ραδιοφωνική εκπομπή.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς οδηγεί κανείς ένα αερόστατο; Έχει τιμόνι;", "How does one steer a hot-air balloon? Does it have a steering wheel?"),
  L("Πιλότος", "m", "Καθόλου. Το μόνο που ελέγχω είναι το ύψος: ανάβω τον καυστήρα για να ζεσταθεί ο αέρας μέσα στο μπαλόνι και να ανεβούμε, και τον σβήνω για να κατεβούμε. Την κατεύθυνση την αποφασίζει ο άνεμος. Το κόλπο είναι ότι σε διαφορετικά ύψη ο άνεμος φυσάει συχνά προς διαφορετική κατεύθυνση, οπότε αλλάζοντας ύψος διαλέγω και δρόμο.", "Not at all. The only thing I control is height: I light the burner to heat the air inside the balloon so we go up, and I turn it off to come down. The direction is decided by the wind. The trick is that at different heights the wind often blows in a different direction, so by changing height I also choose a route."),
  L("Δημοσιογράφος", "f", "Γιατί οι πτήσεις γίνονται πάντα τόσο νωρίς το πρωί;", "Why do the flights always take place so early in the morning?"),
  L("Πιλότος", "m", "Γιατί τις πρώτες ώρες μετά την ανατολή ο αέρας είναι ήρεμος. Όταν ο ήλιος ζεστάνει το έδαφος, δημιουργούνται ρεύματα που ανεβαίνουν και ο αέρας γίνεται απρόβλεπτος. Γι' αυτό ξυπνάμε στις τέσσερις και, αν ο άνεμος ξεπερνά ένα όριο, ακυρώνουμε, όσο κι αν στενοχωριούνται οι επιβάτες.", "Because in the first hours after sunrise the air is calm. When the sun warms the ground, rising currents form and the air becomes unpredictable. That's why we get up at four and, if the wind exceeds a limit, we cancel, however disappointed the passengers are."),
  L("Δημοσιογράφος", "f", "Και πού προσγειώνεστε;", "And where do you land?"),
  L("Πιλότος", "m", "Εκεί που μας πάει ο αέρας, σε κάποιο χωράφι. Μας ακολουθεί ένα αυτοκίνητο με τρέιλερ, που μαζεύει το μπαλόνι και τους επιβάτες. Πάντα κουβαλάμε κι ένα μπουκάλι κρασί για τον ιδιοκτήτη του χωραφιού· είναι ο καλύτερος τρόπος να μας ξαναδεχτεί.", "Wherever the wind takes us, in some field. We're followed by a car with a trailer, which collects the balloon and the passengers. We always carry a bottle of wine for the owner of the field too; it's the best way to make sure he'll have us again."),
 ],
 "questions": [
  Q("Πώς αλλάζει κατεύθυνση ο πιλότος;", ["Με ένα μικρό τιμόνι στο καλάθι", "Αλλάζοντας ύψος, γιατί σε κάθε ύψος ο άνεμος μπορεί να φυσάει αλλιώς", "Με τη βοήθεια ενός μοτέρ", "Δεν μπορεί να αλλάξει καθόλου τη διαδρομή"], 1, "αλλάζοντας ύψος διαλέγω και δρόμο"),
  Q("Γιατί οι πτήσεις γίνονται νωρίς το πρωί;", ["Γιατί η θέα είναι καλύτερη", "Γιατί είναι φθηνότερο το καύσιμο", "Γιατί ο αέρας είναι ήρεμος πριν ζεσταθεί το έδαφος", "Γιατί το απαιτούν τα αεροδρόμια"], 2, "τις πρώτες ώρες μετά την ανατολή ο αέρας είναι ήρεμος"),
  Q("Γιατί κουβαλούν ένα μπουκάλι κρασί;", ["Για να το προσφέρουν στον ιδιοκτήτη του χωραφιού όπου προσγειώνονται", "Για να γιορτάσουν με τους επιβάτες", "Για να το πουλήσουν", "Για τον οδηγό του αυτοκινήτου"], 0, "ένα μπουκάλι κρασί για τον ιδιοκτήτη του χωραφιού"),
 ],
 "gloss": {"αερόστατου": "αερόστατο — hot-air balloon", "τιμόνι": "τιμόνι — steering wheel", "καυστήρα": "καυστήρας — burner", "κατεύθυνση": "κατεύθυνση — direction", "ανατολή": "ανατολή — sunrise", "απρόβλεπτος": "απρόβλεπτος — unpredictable", "στενοχωριούνται": "στενοχωριέμαι — to be upset", "προσγειώνεστε": "προσγειώνομαι — to land", "χωράφι": "χωράφι — field", "ξαναδεχτεί": "ξαναδέχομαι — to accept again"},
})

ITEMS.append({
 "id": "l182-int-imerominies-sti-syskevasia", "title": "Τι σημαίνουν οι ημερομηνίες στη συσκευασία", "title_en": "What the dates on the packaging mean", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια τεχνολόγο τροφίμων σε μια εκπομπή για τον καταναλωτή.",
 "script": [
  L("Δημοσιογράφος", "m", "Στις συσκευασίες βλέπουμε άλλοτε «ανάλωση έως» και άλλοτε «ανάλωση κατά προτίμηση πριν από». Είναι το ίδιο πράγμα;", "On packaging we sometimes see 'use by' and sometimes 'best before'. Is it the same thing?"),
  L("Τεχνολόγος", "f", "Όχι, και η διαφορά είναι σημαντική. Το «ανάλωση έως» μπαίνει σε τρόφιμα που χαλάνε γρήγορα, όπως ο φρέσκος κιμάς ή το φρέσκο ψάρι. Αφορά την ασφάλεια: μετά από αυτή την ημερομηνία δεν πρέπει να το φάτε, ακόμη κι αν φαίνεται και μυρίζει μια χαρά.", "No, and the difference is important. 'Use by' goes on foods that spoil quickly, like fresh mince or fresh fish. It's about safety: after that date you shouldn't eat it, even if it looks and smells perfectly fine."),
  L("Δημοσιογράφος", "m", "Και το «κατά προτίμηση»;", "And 'best before'?"),
  L("Τεχνολόγος", "f", "Αυτό αφορά την ποιότητα. Τα μακαρόνια, το ρύζι, τα μπισκότα, τα κονσερβοποιημένα, μετά την ημερομηνία μπορεί να έχουν χάσει λίγη από τη γεύση ή την τραγανότητά τους, αλλά αν η συσκευασία είναι άθικτη και τα έχετε φυλάξει σωστά, συνήθως τρώγονται άφοβα. Εκεί εμπιστευτείτε τις αισθήσεις σας.", "That one is about quality. Pasta, rice, biscuits, tinned food may have lost a bit of their flavour or crunchiness after the date, but if the packaging is intact and you've stored them properly, they can usually be eaten without worry. There, trust your senses."),
  L("Δημοσιογράφος", "m", "Γιατί επιμένετε τόσο σε αυτή τη διάκριση;", "Why do you insist so much on this distinction?"),
  L("Τεχνολόγος", "f", "Γιατί πολλοί τα μπερδεύουν και πετάνε απολύτως φαγώσιμα τρόφιμα μόνο επειδή πέρασε η ημερομηνία. Αυτό σημαίνει χαμένα χρήματα για το νοικοκυριό και άσκοπη σπατάλη για τον πλανήτη.", "Because many people confuse them and throw away perfectly edible food just because the date has passed. That means lost money for the household and pointless waste for the planet."),
 ],
 "questions": [
  Q("Τι ισχύει για τα τρόφιμα με την ένδειξη «ανάλωση έως»;", ["Τρώγονται άφοβα για μία εβδομάδα ακόμη", "Δεν πρέπει να τα φάμε μετά την ημερομηνία, ακόμη κι αν φαίνονται καλά", "Αρκεί να μυρίζουν καλά", "Αφορούν μόνο τα κονσερβοποιημένα"], 1, "μετά από αυτή την ημερομηνία δεν πρέπει να το φάτε, ακόμη κι αν φαίνεται και μυρίζει μια χαρά"),
  Q("Τι αφορά η ένδειξη «ανάλωση κατά προτίμηση πριν από»;", ["Την ασφάλεια του τροφίμου", "Την τιμή του προϊόντος", "Την ποιότητα, όπως τη γεύση και την τραγανότητα", "Τη χώρα προέλευσης"], 2, "Αυτό αφορά την ποιότητα"),
  Q("Γιατί επιμένει η τεχνολόγος σε αυτή τη διάκριση;", ["Γιατί πολλοί πετάνε φαγώσιμα τρόφιμα επειδή πέρασε η ημερομηνία", "Γιατί άλλαξε πρόσφατα ο νόμος", "Γιατί τα σούπερ μάρκετ δεν βάζουν ημερομηνίες", "Γιατί θέλει να πουλήσει ένα βιβλίο"], 0, "πετάνε απολύτως φαγώσιμα τρόφιμα μόνο επειδή πέρασε η ημερομηνία"),
 ],
 "gloss": {"συσκευασίες": "συσκευασία — packaging", "ανάλωση έως": "ανάλωση έως — use by", "κατά προτίμηση": "κατά προτίμηση — preferably", "χαλάνε": "χαλάω — to spoil", "κιμάς": "κιμάς — mince", "κονσερβοποιημένα": "κονσερβοποιημένος — tinned, canned", "τραγανότητά": "τραγανότητα — crunchiness", "άθικτη": "άθικτος — intact", "άφοβα": "άφοβα — without fear", "διάκριση": "διάκριση — distinction", "φαγώσιμα": "φαγώσιμος — edible", "σπατάλη": "σπατάλη — waste"},
})

ITEMS.append({
 "id": "l182-vm-arkoudaki-paidikou", "title": "Το αρκουδάκι που ξεχάστηκε", "title_en": "The forgotten teddy bear", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη νηπιαγωγό του παιδικού σταθμού όπου πηγαίνει η κόρη σας.",
 "script": [
  L("Νηπιαγωγός", "f", "Καλησπέρα, η Κατερίνα είμαι, από τον παιδικό σταθμό. Μόλις φύγατε, βρήκαμε κάτω από ένα κρεβατάκι το αρκουδάκι της Δάφνης, αυτό με το κόκκινο φιόγκο. Ξέρω ότι δεν κοιμάται χωρίς αυτό, γι' αυτό σας παίρνω αμέσως.", "Good evening, it's Katerina, from the nursery. Just after you left, we found Dafni's teddy bear under one of the little beds, the one with the red bow. I know she doesn't sleep without it, so I'm calling you straight away."),
  L("Νηπιαγωγός", "f", "Εγώ θα μείνω στον σταθμό ως τις έξι και μισή, για τη συνάντηση με τους γονείς της άλλης τάξης. Αν προλαβαίνετε, περάστε να το πάρετε. Η εξωτερική πόρτα θα είναι κλειστή, οπότε χτυπήστε το κουδούνι της κουζίνας, στο πλάι του κτιρίου.", "I'll stay at the nursery until half past six, for the meeting with the parents of the other class. If you have time, come and pick it up. The front door will be closed, so ring the kitchen bell, at the side of the building."),
  L("Νηπιαγωγός", "f", "Αν δεν προλάβετε, μην ανησυχείτε· μπορώ να το αφήσω στη γειτόνισσά σας, την κυρία Ρούλα, που μένει δίπλα μου και περνάει από το σπίτι σας κάθε βράδυ με τον σκύλο της. Στείλτε μου απλώς ένα μήνυμα να μου πείτε τι προτιμάτε. Φιλάκια στη Δάφνη!", "If you can't make it, don't worry; I can leave it with your neighbour, Mrs Roula, who lives next to me and walks past your house every evening with her dog. Just send me a message to tell me what you prefer. Kisses to Dafni!"),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί αμέσως η νηπιαγωγός;", ["Γιατί η Δάφνη είναι άρρωστη", "Γιατί ξέρει ότι η Δάφνη δεν κοιμάται χωρίς το αρκουδάκι", "Γιατί το αρκουδάκι είναι σκισμένο", "Γιατί ο σταθμός κλείνει αύριο"], 1, "Ξέρω ότι δεν κοιμάται χωρίς αυτό, γι' αυτό σας παίρνω αμέσως"),
  Q("Πώς μπορεί να μπει κανείς στον σταθμό μετά τις έξι;", ["Από την εξωτερική πόρτα", "Τηλεφωνώντας στη νηπιαγωγό", "Χτυπώντας το κουδούνι της κουζίνας στο πλάι", "Από την αυλή"], 2, "χτυπήστε το κουδούνι της κουζίνας, στο πλάι του κτιρίου"),
  Q("Ποια λύση προτείνει, αν δεν προλάβουν;", ["Να αφήσει το αρκουδάκι στη γειτόνισσα, την κυρία Ρούλα", "Να το κρατήσει ως τη Δευτέρα", "Να το στείλει με ταξί", "Να το φέρει η ίδια το πρωί"], 0, "μπορώ να το αφήσω στη γειτόνισσά σας, την κυρία Ρούλα"),
 ],
 "gloss": {"νηπιαγωγό": "νηπιαγωγός — nursery teacher", "παιδικού σταθμού": "παιδικός σταθμός — nursery, day care", "αρκουδάκι": "αρκουδάκι — teddy bear", "κρεβατάκι": "κρεβατάκι — little bed, cot", "φιόγκο": "φιόγκος — bow", "προλαβαίνετε": "προλαβαίνω — to have time, make it", "κουδούνι": "κουδούνι — bell"},
})

ITEMS.append({
 "id": "l182-mon-minas-choris-kafe", "title": "Ένας μήνας χωρίς καφέ", "title_en": "A month without coffee", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλά σε ένα podcast για τον μήνα που πέρασε χωρίς καφέ.",
 "script": [
  L("Αλέκος", "m", "Έπινα πέντε καφέδες την ημέρα: έναν μόλις ξυπνούσα, δύο στο γραφείο, έναν μετά το φαγητό κι έναν «για να αντέξω» το απόγευμα. Όταν ο γιατρός μου είπε ότι η πίεσή μου ανεβαίνει, αποφάσισα να δοκιμάσω έναν μήνα χωρίς καθόλου καφέ.", "I used to drink five coffees a day: one as soon as I woke up, two at the office, one after lunch and one 'to get through' the afternoon. When my doctor told me my blood pressure was going up, I decided to try a month with no coffee at all."),
  L("Αλέκος", "m", "Οι τρεις πρώτες μέρες ήταν οι χειρότερες. Είχα πονοκέφαλο από το πρωί ως το βράδυ και ήμουν τόσο νευρικός, που η κόρη μου με ρώτησε αν μάλωσα με κάποιον. Από την πέμπτη μέρα όμως ο πονοκέφαλος έφυγε, και κάτι παράξενο συνέβη: άρχισα να κοιμάμαι πιο βαθιά και να ξυπνάω πριν χτυπήσει το ξυπνητήρι.", "The first three days were the worst. I had a headache from morning till night and I was so irritable that my daughter asked me if I'd had a row with someone. From the fifth day, though, the headache went away, and something strange happened: I started sleeping more deeply and waking up before the alarm went off."),
  L("Αλέκος", "m", "Το πιο δύσκολο δεν ήταν η καφεΐνη, αλλά η συνήθεια: το διάλειμμα στο γραφείο, η κουβέντα με τους συναδέλφους. Γι' αυτό συνέχισα να κατεβαίνω στο κυλικείο, απλώς παράγγελνα ένα τσάι του βουνού. Σήμερα πίνω έναν καφέ την ημέρα, το πρωί, και τον απολαμβάνω πολύ περισσότερο απ' ό,τι τους πέντε.", "The hardest part wasn't the caffeine, but the habit: the break at the office, the chat with colleagues. So I kept going down to the canteen, I just ordered a mountain tea. Today I drink one coffee a day, in the morning, and I enjoy it much more than the five."),
 ],
 "questions": [
  Q("Γιατί αποφάσισε ο Αλέκος να κόψει τον καφέ;", ["Γιατί δεν κοιμόταν καθόλου", "Γιατί ο γιατρός του είπε ότι η πίεσή του ανεβαίνει", "Γιατί τον ζήτησε η κόρη του", "Γιατί ο καφές ακρίβυνε"], 1, "Όταν ο γιατρός μου είπε ότι η πίεσή μου ανεβαίνει"),
  Q("Τι άλλαξε μετά την πέμπτη μέρα;", ["Ένιωθε πιο νευρικός", "Έπινε περισσότερο τσάι", "Κοιμόταν πιο βαθιά και ξυπνούσε πριν από το ξυπνητήρι", "Έχασε βάρος"], 2, "άρχισα να κοιμάμαι πιο βαθιά και να ξυπνάω πριν χτυπήσει το ξυπνητήρι"),
  Q("Ποιο ήταν, κατά τον Αλέκο, το πιο δύσκολο;", ["Η συνήθεια και το διάλειμμα με τους συναδέλφους", "Η καφεΐνη", "Η γεύση του τσαγιού", "Η κούραση το πρωί"], 0, "Το πιο δύσκολο δεν ήταν η καφεΐνη, αλλά η συνήθεια"),
 ],
 "gloss": {"για να αντέξω": "αντέχω — to endure, get through", "πίεσή": "πίεση — blood pressure", "πονοκέφαλο": "πονοκέφαλος — headache", "νευρικός": "νευρικός — irritable, nervous", "ξυπνητήρι": "ξυπνητήρι — alarm clock", "συνήθεια": "συνήθεια — habit", "κυλικείο": "κυλικείο — canteen", "τσάι του βουνού": "τσάι του βουνού — Greek mountain tea", "απολαμβάνω": "απολαμβάνω — to enjoy"},
})

ITEMS.append({
 "id": "l182-dia-me-to-treno-stin-evropi", "title": "Ένα καλοκαίρι με το τρένο στην Ευρώπη", "title_en": "A summer by train around Europe", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλους να σχεδιάζουν ένα ταξίδι με τρένο στην Ευρώπη.",
 "script": [
  L("Άρης", "m", "Βρήκα την κάρτα που λέγαμε: δεκαπέντε μέρες ταξίδι μέσα σε δύο μήνες, σε όσα τρένα θέλεις. Δεν χρειάζεται να ταξιδεύεις κάθε μέρα· μετράνε μόνο οι μέρες που μπαίνεις σε τρένο.", "I found the pass we were talking about: fifteen travel days within two months, on as many trains as you like. You don't have to travel every day; only the days you get on a train count."),
  L("Δανάη", "f", "Τέλεια. Αλλά διάβασα ότι στα γρήγορα τρένα, σε Γαλλία και Ιταλία, πρέπει να κλείσεις και θέση, και πληρώνεις κάτι επιπλέον. Αν τα παίρνουμε όλα αυτά, η κάρτα δεν θα βγει πιο ακριβή από τα κανονικά εισιτήρια;", "Perfect. But I read that on the fast trains, in France and Italy, you also have to book a seat, and you pay something extra. If we take all of those, won't the pass end up more expensive than normal tickets?"),
  L("Άρης", "m", "Γι' αυτό λέω να παίρνουμε κυρίως τα περιφερειακά, που είναι πιο αργά αλλά δεν θέλουν κράτηση. Δεν βιαζόμαστε· άλλωστε από το παράθυρο ενός αργού τρένου βλέπεις περισσότερα.", "That's why I say we take mainly the regional ones, which are slower but don't need a reservation. We're not in a hurry; besides, from the window of a slow train you see more."),
  L("Δανάη", "f", "Και πώς φτάνουμε στην Ιταλία; Δεν θέλω να πετάξουμε.", "And how do we get to Italy? I don't want to fly."),
  L("Άρης", "m", "Με το πλοίο από την Πάτρα για το Μπάρι. Κάποιος μου είπε ότι με την κάρτα έχεις έκπτωση στο εισιτήριο, αλλά πρέπει να το ελέγξουμε πριν κλείσουμε οτιδήποτε.", "By ferry from Patras to Bari. Someone told me that with the pass you get a discount on the ticket, but we need to check before we book anything."),
 ],
 "questions": [
  Q("Πώς λειτουργεί η κάρτα που βρήκε ο Άρης;", ["Ισχύει μόνο για δεκαπέντε συνεχόμενες μέρες", "Μετράνε μόνο οι μέρες που ταξιδεύουν με τρένο, μέσα σε δύο μήνες", "Ισχύει μόνο για τα γρήγορα τρένα", "Ισχύει για ένα τρένο την ημέρα"], 1, "μετράνε μόνο οι μέρες που μπαίνεις σε τρένο"),
  Q("Τι ανησυχεί τη Δανάη;", ["Ότι τα τρένα θα είναι γεμάτα", "Ότι δεν θα βρουν ξενοδοχεία", "Ότι οι επιπλέον κρατήσεις στα γρήγορα τρένα θα ανεβάσουν το κόστος", "Ότι η κάρτα δεν ισχύει στην Ιταλία"], 2, "η κάρτα δεν θα βγει πιο ακριβή από τα κανονικά εισιτήρια"),
  Q("Τι λέει ο Άρης για την έκπτωση στο πλοίο;", ["Ότι κάποιος του το είπε και πρέπει να το ελέγξουν", "Ότι είναι σίγουρη", "Ότι ισχύει μόνο τον χειμώνα", "Ότι δεν υπάρχει καμία έκπτωση"], 0, "πρέπει να το ελέγξουμε πριν κλείσουμε οτιδήποτε"),
 ],
 "gloss": {"κλείσεις και θέση": "κλείνω θέση — to book a seat", "επιπλέον": "επιπλέον — extra", "περιφερειακά": "περιφερειακός — regional", "κράτηση": "κράτηση — reservation", "βιαζόμαστε": "βιάζομαι — to be in a hurry", "πετάξουμε": "πετάω — to fly", "έκπτωση": "έκπτωση — discount", "να το ελέγξουμε": "ελέγχω — to check"},
})

ITEMS.append({
 "id": "l182-news-orio-trianta", "title": "Τριάντα χιλιόμετρα την ώρα στο κέντρο", "title_en": "Thirty kilometres an hour in the centre", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση από ένα τοπικό δελτίο ειδήσεων.",
 "script": [
  L("Παρουσιαστής", "m", "Από την πρώτη του επόμενου μήνα, το όριο ταχύτητας στους περισσότερους δρόμους του κέντρου της πόλης μειώνεται από τα πενήντα στα τριάντα χιλιόμετρα την ώρα. Εξαιρούνται οι μεγάλες λεωφόροι, όπου το όριο παραμένει ως έχει.", "From the first of next month, the speed limit on most streets in the town centre is being reduced from fifty to thirty kilometres an hour. The main avenues are excluded, where the limit stays as it is."),
  L("Παρουσιαστής", "m", "Σύμφωνα με τον δήμο, ο στόχος είναι να μειωθούν τα σοβαρά τροχαία, κυρίως αυτά με πεζούς και ποδηλάτες. Όπως εξήγησε ο αρμόδιος αντιδήμαρχος, ένας πεζός που χτυπιέται από αυτοκίνητο με τριάντα χιλιόμετρα έχει πολύ περισσότερες πιθανότητες να επιβιώσει απ' ό,τι με πενήντα. Επιπλέον, αναμένεται να μειωθεί και ο θόρυβος.", "According to the municipality, the aim is to reduce serious road accidents, mainly those involving pedestrians and cyclists. As the deputy mayor in charge explained, a pedestrian hit by a car at thirty kilometres has a much better chance of surviving than at fifty. In addition, noise is expected to fall."),
  L("Παρουσιαστής", "m", "Οι ταξιτζήδες και οι επαγγελματίες οδηγοί εκφράζουν αντιρρήσεις, υποστηρίζοντας ότι οι διαδρομές θα γίνουν πιο αργές. Ο δήμος απαντά ότι στο κέντρο, λόγω της κίνησης, η μέση ταχύτητα σπάνια ξεπερνά ήδη τα είκοσι πέντε χιλιόμετρα. Τον πρώτο μήνα δεν θα επιβάλλονται πρόστιμα, αλλά οι παραβάτες θα παίρνουν ενημερωτικό σημείωμα.", "Taxi drivers and professional drivers have raised objections, arguing that journeys will become slower. The municipality replies that in the centre, because of the traffic, the average speed already rarely exceeds twenty-five kilometres. During the first month no fines will be imposed, but offenders will receive an information note."),
 ],
 "questions": [
  Q("Πού δεν θα ισχύσει το νέο όριο;", ["Στους δρόμους γύρω από τα σχολεία", "Στις μεγάλες λεωφόρους", "Στους πεζόδρομους", "Στη γειτονιά του λιμανιού"], 1, "Εξαιρούνται οι μεγάλες λεωφόροι, όπου το όριο παραμένει ως έχει"),
  Q("Πώς απαντά ο δήμος στις αντιρρήσεις των ταξιτζήδων;", ["Ότι θα τους δώσει αποζημίωση", "Ότι θα ανοίξει νέους δρόμους", "Ότι η μέση ταχύτητα στο κέντρο σπάνια ξεπερνά ήδη τα είκοσι πέντε χιλιόμετρα", "Ότι το μέτρο είναι προσωρινό"], 2, "η μέση ταχύτητα σπάνια ξεπερνά ήδη τα είκοσι πέντε χιλιόμετρα"),
  Q("Τι θα γίνει τον πρώτο μήνα με όσους παραβαίνουν το όριο;", ["Θα παίρνουν ενημερωτικό σημείωμα, χωρίς πρόστιμο", "Θα πληρώνουν διπλό πρόστιμο", "Θα χάνουν το δίπλωμα", "Δεν θα ελέγχονται καθόλου"], 0, "Τον πρώτο μήνα δεν θα επιβάλλονται πρόστιμα, αλλά οι παραβάτες θα παίρνουν ενημερωτικό σημείωμα"),
 ],
 "gloss": {"όριο ταχύτητας": "όριο ταχύτητας — speed limit", "Εξαιρούνται": "εξαιρούμαι — to be excluded", "ως έχει": "ως έχει — as it is", "τροχαία": "τροχαίο — road accident", "αρμόδιος αντιδήμαρχος": "αρμόδιος αντιδήμαρχος — deputy mayor in charge", "επιβιώσει": "επιβιώνω — to survive", "αντιρρήσεις": "αντίρρηση — objection", "πρόστιμα": "πρόστιμο — fine", "παραβάτες": "παραβάτης — offender"},
})

ITEMS.append({
 "id": "l182-rep-gaitanaki", "title": "Το γαϊτανάκι της Αποκριάς", "title_en": "The carnival ribbon dance", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από την πλατεία ενός χωριού την τελευταία Κυριακή της Αποκριάς.",
 "script": [
  L("Ρεπόρτερ", "f", "Στη μέση της πλατείας έχει στηθεί ένα ψηλό ξύλινο κοντάρι. Από την κορυφή του κρέμονται δώδεκα μακριές κορδέλες, σε όλα τα χρώματα. Γύρω του, δώδεκα χορευτές με αποκριάτικες στολές κρατούν από μία κορδέλα ο καθένας και περιμένουν τη μουσική.", "In the middle of the square a tall wooden pole has been set up. From its top hang twelve long ribbons, in every colour. Around it, twelve dancers in carnival costumes each hold one ribbon and wait for the music."),
  L("Ρεπόρτερ", "f", "Είναι το γαϊτανάκι, ένας αποκριάτικος χορός που χορεύεται σε πολλά μέρη της Ελλάδας. Οι χορευτές κινούνται σε δύο κύκλους, ο ένας προς τα δεξιά κι ο άλλος προς τα αριστερά, περνώντας ο ένας κάτω από την κορδέλα του άλλου. Έτσι οι κορδέλες πλέκονται σιγά σιγά γύρω από το κοντάρι, σαν μια πολύχρωμη κοτσίδα.", "It's the gaitanaki, a carnival dance danced in many parts of Greece. The dancers move in two circles, one to the right and the other to the left, passing under each other's ribbons. In this way the ribbons are braided little by little around the pole, like a colourful plait."),
  L("Χορευτής", "m", "Το δύσκολο είναι το ξέπλεγμα. Στο τέλος πρέπει να κάνουμε όλες τις κινήσεις ανάποδα, για να λυθούν οι κορδέλες. Αν κάποιος μπερδευτεί, μπερδεύονται όλοι, και το χωριό γελάει μαζί μας. Γι' αυτό κάνουμε πρόβες από τα Χριστούγεννα.", "The hard part is the unbraiding. At the end we have to do all the moves in reverse, so the ribbons come undone. If someone gets mixed up, everyone gets mixed up, and the village laughs with us. That's why we rehearse from Christmas."),
 ],
 "questions": [
  Q("Πόσοι χορευτές παίρνουν μέρος στο γαϊτανάκι του ρεπορτάζ;", ["Έξι", "Δώδεκα", "Είκοσι τέσσερις", "Όλοι οι κάτοικοι"], 1, "δώδεκα χορευτές με αποκριάτικες στολές κρατούν από μία κορδέλα ο καθένας"),
  Q("Πώς πλέκονται οι κορδέλες γύρω από το κοντάρι;", ["Τις δένουν οι θεατές", "Τις τυλίγει ένας χορευτής στην κορυφή", "Οι χορευτές κινούνται σε δύο αντίθετους κύκλους και περνούν ο ένας κάτω από την κορδέλα του άλλου", "Γυρίζει το κοντάρι"], 2, "Οι χορευτές κινούνται σε δύο κύκλους, ο ένας προς τα δεξιά κι ο άλλος προς τα αριστερά"),
  Q("Ποιο είναι, κατά τον χορευτή, το πιο δύσκολο;", ["Το ξέπλεγμα, με όλες τις κινήσεις ανάποδα", "Το στήσιμο του κονταριού", "Οι στολές", "Ο ρυθμός της μουσικής"], 0, "Το δύσκολο είναι το ξέπλεγμα"),
 ],
 "gloss": {"Αποκριάς": "Αποκριά — Carnival", "κοντάρι": "κοντάρι — pole", "κορδέλες": "κορδέλα — ribbon", "χορευτές": "χορευτής — dancer", "πλέκονται": "πλέκομαι — to be braided", "κοτσίδα": "κοτσίδα — plait, braid", "ξέπλεγμα": "ξέπλεγμα — unbraiding", "ανάποδα": "ανάποδα — in reverse", "μπερδευτεί": "μπερδεύομαι — to get mixed up", "πρόβες": "πρόβα — rehearsal"},
})

ITEMS.append({
 "id": "l182-c1-giati-vouloynoun-ta-aftia", "title": "Γιατί βουλώνουν τα αυτιά στο αεροπλάνο", "title_en": "Why our ears pop on a plane", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν ωτορινολαρυγγολόγο σε μια εκπομπή για την υγεία.",
 "script": [
  L("Παρουσιάστρια", "f", "Πολλοί επιβάτες νιώθουν τα αυτιά τους να «βουλώνουν» όταν το αεροπλάνο κατεβαίνει. Τι ακριβώς συμβαίνει;", "Many passengers feel their ears 'block' when the plane is descending. What exactly happens?"),
  L("Γιατρός", "m", "Πίσω από το τύμπανο υπάρχει ένας μικρός θάλαμος με αέρα, το μέσο ους. Συνδέεται με το πίσω μέρος της μύτης μέσω ενός λεπτού σωλήνα, της ευσταχιανής σάλπιγγας, που συνήθως μένει κλειστή. Όταν το αεροπλάνο κατεβαίνει, η πίεση στην καμπίνα αυξάνεται, και ο αέρας έξω από το τύμπανο το σπρώχνει προς τα μέσα. Αυτό το νιώθουμε σαν βούλωμα ή και πόνο.", "Behind the eardrum there is a small chamber of air, the middle ear. It connects to the back of the nose through a thin tube, the Eustachian tube, which usually stays closed. When the plane descends, the pressure in the cabin increases, and the air outside the eardrum pushes it inwards. We feel this as blockage or even pain."),
  L("Παρουσιάστρια", "f", "Γιατί συμβαίνει κυρίως στην κάθοδο και όχι στην άνοδο;", "Why does it happen mainly on the descent and not on the ascent?"),
  L("Γιατρός", "m", "Γιατί η σάλπιγγα αφήνει τον αέρα να βγει πιο εύκολα απ' ό,τι να μπει. Στην άνοδο ο αέρας του μέσου ωτός διαστέλλεται και ξεφεύγει σχεδόν μόνος του. Στην κάθοδο πρέπει να τη βοηθήσουμε να ανοίξει: καταπίνοντας, χασμουριόμαστε, μασώντας τσίχλα. Γι' αυτό συνιστάμε στους γονείς να ταΐζουν τα μωρά την ώρα της προσγείωσης.", "Because the tube lets air out more easily than in. On the ascent the air in the middle ear expands and escapes almost on its own. On the descent we have to help it open: by swallowing, yawning, chewing gum. That's why we advise parents to feed babies during landing."),
  L("Παρουσιάστρια", "f", "Και όταν είμαστε κρυωμένοι;", "And when we have a cold?"),
  L("Γιατρός", "m", "Τότε η σάλπιγγα είναι συχνά πρησμένη και δεν ανοίγει εύκολα, οπότε ο πόνος μπορεί να είναι έντονος. Αν το ταξίδι δεν αναβάλλεται, καλό είναι να συμβουλευτεί κανείς πρώτα τον γιατρό του, που μπορεί να του προτείνει κάποιο αποσυμφορητικό.", "Then the tube is often swollen and doesn't open easily, so the pain can be intense. If the trip can't be postponed, it's a good idea to consult your doctor first, who may suggest a decongestant."),
 ],
 "questions": [
  Q("Τι προκαλεί το «βούλωμα» στην κάθοδο;", ["Ο θόρυβος των κινητήρων", "Η αυξημένη πίεση στην καμπίνα, που σπρώχνει το τύμπανο προς τα μέσα", "Η ξηρασία του αέρα", "Η χαμηλή θερμοκρασία"], 1, "η πίεση στην καμπίνα αυξάνεται, και ο αέρας έξω από το τύμπανο το σπρώχνει προς τα μέσα"),
  Q("Γιατί το πρόβλημα είναι μικρότερο στην άνοδο;", ["Γιατί το αεροπλάνο ανεβαίνει πιο αργά", "Γιατί οι επιβάτες μασούν τσίχλα", "Γιατί η σάλπιγγα αφήνει τον αέρα να βγει πιο εύκολα απ' ό,τι να μπει", "Γιατί η πίεση στην καμπίνα δεν αλλάζει"], 2, "η σάλπιγγα αφήνει τον αέρα να βγει πιο εύκολα απ' ό,τι να μπει"),
  Q("Τι συμβουλεύει για όσους είναι κρυωμένοι;", ["Να συμβουλευτούν πρώτα τον γιατρό τους, αν δεν μπορούν να αναβάλουν το ταξίδι", "Να μην πίνουν νερό στην πτήση", "Να κοιμούνται στην προσγείωση", "Να φορούν ωτοασπίδες"], 0, "καλό είναι να συμβουλευτεί κανείς πρώτα τον γιατρό του"),
 ],
 "gloss": {"ωτορινολαρυγγολόγο": "ωτορινολαρυγγολόγος — ear, nose and throat doctor", "βουλώνουν": "βουλώνω — to block", "τύμπανο": "τύμπανο — eardrum", "μέσο ους": "μέσο ους — middle ear", "ευσταχιανής σάλπιγγας": "ευσταχιανή σάλπιγγα — Eustachian tube", "κάθοδο": "κάθοδος — descent", "διαστέλλεται": "διαστέλλομαι — to expand", "καταπίνοντας": "καταπίνω — to swallow", "πρησμένη": "πρησμένος — swollen", "αποσυμφορητικό": "αποσυμφορητικό — decongestant"},
})

ITEMS.append({
 "id": "l182-c1-prosopa-sta-synnefa", "title": "Γιατί βλέπουμε πρόσωπα στα σύννεφα", "title_en": "Why we see faces in clouds", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ψυχολόγο να εξηγεί σε μια επιστημονική εκπομπή γιατί βλέπουμε πρόσωπα σε άψυχα αντικείμενα.",
 "script": [
  L("Ψυχολόγος", "f", "Δύο παράθυρα κι ένα μπαλκόνι γίνονται ξαφνικά ένα πρόσωπο που μας κοιτάζει. Μια πρίζα μοιάζει ξαφνιασμένη, ένα σύννεφο θυμίζει τον παππού μας. Το φαινόμενο λέγεται παρειδωλία, και δεν είναι παραίσθηση· είναι ένδειξη ότι ο εγκέφαλός μας κάνει πολύ καλά τη δουλειά του.", "Two windows and a balcony suddenly become a face looking at us. A socket looks surprised, a cloud reminds us of our grandfather. The phenomenon is called pareidolia, and it isn't a hallucination; it's a sign that our brain is doing its job very well."),
  L("Ψυχολόγος", "f", "Ο εγκέφαλος διαθέτει περιοχές που ειδικεύονται στην αναγνώριση προσώπων και αντιδρούν εξαιρετικά γρήγορα, μέσα σε κλάσματα του δευτερολέπτου. Για να είναι τόσο γρήγορες, αρκούνται σε ελάχιστα στοιχεία: δύο σημεία πάνω και μια γραμμή κάτω. Έτσι, πότε πότε, «βλέπουν» πρόσωπο εκεί όπου δεν υπάρχει.", "The brain has areas that specialise in recognising faces and react extremely quickly, within fractions of a second. To be so fast, they make do with very little: two dots above and a line below. So, now and then, they 'see' a face where there isn't one."),
  L("Ψυχολόγος", "f", "Από εξελικτική σκοπιά, το λάθος αυτό είναι φθηνό. Αν ο πρόγονός μας μπέρδευε έναν θάμνο με πρόσωπο, έχανε μια στιγμή. Αν δεν έβλεπε έναν άνθρωπο ή ένα ζώο που τον παρακολουθούσε, μπορεί να έχανε τη ζωή του. Ενδιαφέρον έχει και ένα πρόσφατο εύρημα: στα περισσότερα «πρόσωπα» που βλέπουμε σε αντικείμενα αποδίδουμε συχνότερα ανδρικό φύλο παρά γυναικείο, κάτι που οι ερευνητές δεν έχουν ακόμα εξηγήσει πλήρως.", "From an evolutionary point of view, this mistake is cheap. If our ancestor mistook a bush for a face, he lost a moment. If he failed to see a person or an animal watching him, he might lose his life. A recent finding is also interesting: to most 'faces' we see in objects we attribute the male sex more often than the female, something researchers have not yet fully explained."),
 ],
 "questions": [
  Q("Τι είναι, κατά την ψυχολόγο, η παρειδωλία;", ["Μια μορφή παραίσθησης", "Ένδειξη ότι ο εγκέφαλος κάνει καλά τη δουλειά του", "Ένα πρόβλημα της όρασης", "Μια φαντασίωση των παιδιών"], 1, "δεν είναι παραίσθηση· είναι ένδειξη ότι ο εγκέφαλός μας κάνει πολύ καλά τη δουλειά του"),
  Q("Γιατί οι περιοχές αναγνώρισης προσώπων κάνουν λάθη;", ["Γιατί κουράζονται εύκολα", "Γιατί λειτουργούν μόνο στο φως", "Γιατί, για να είναι γρήγορες, αρκούνται σε ελάχιστα στοιχεία", "Γιατί δεν αναπτύσσονται πλήρως"], 2, "Για να είναι τόσο γρήγορες, αρκούνται σε ελάχιστα στοιχεία"),
  Q("Γιατί το λάθος αυτό είναι «φθηνό» από εξελικτική σκοπιά;", ["Γιατί το να μη δεις έναν πραγματικό άνθρωπο ή ζώο μπορεί να κόστιζε τη ζωή", "Γιατί συμβαίνει σπάνια", "Γιατί δεν χρειάζεται ενέργεια", "Γιατί βοηθά στην επικοινωνία"], 0, "Αν δεν έβλεπε έναν άνθρωπο ή ένα ζώο που τον παρακολουθούσε, μπορεί να έχανε τη ζωή του"),
 ],
 "gloss": {"άψυχα": "άψυχος — inanimate", "πρίζα": "πρίζα — (electric) socket", "ξαφνιασμένη": "ξαφνιασμένος — surprised", "παρειδωλία": "παρειδωλία — pareidolia", "παραίσθηση": "παραίσθηση — hallucination", "ειδικεύονται": "ειδικεύομαι — to specialise", "αρκούνται": "αρκούμαι — to make do with", "εξελικτική σκοπιά": "εξελικτική σκοπιά — evolutionary point of view", "πρόγονός": "πρόγονος — ancestor", "αποδίδουμε": "αποδίδω — to attribute"},
})

rnd = random.Random(182)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-182.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
