# Source for library/listening/listening-167.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l167.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l167-ann-anaklisi-proiontos", "title": "Ανάκληση προϊόντος στο σούπερ μάρκετ", "title_en": "A product recall at the supermarket", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός σούπερ μάρκετ.",
 "script": [
  L("Υπάλληλος", "f", "Αγαπητοί πελάτες, σας ενημερώνουμε ότι ο προμηθευτής μας ανακαλεί μια συγκεκριμένη παρτίδα ταχινιού σε βάζο των τριακοσίων γραμμαρίων, μετά από έλεγχο που έδειξε πιθανή μικροβιακή επιμόλυνση. Πρόκειται μόνο για τα βάζα με ημερομηνία λήξης τον Μάρτιο του επόμενου έτους.", "Dear customers, we inform you that our supplier is recalling a specific batch of tahini in three-hundred-gram jars, after a check that showed possible microbial contamination. This concerns only the jars with an expiry date in March next year."),
  L("Υπάλληλος", "f", "Αν έχετε αγοράσει αυτό το προϊόν, παρακαλούμε να μην το καταναλώσετε. Μπορείτε να το επιστρέψετε σε οποιοδήποτε κατάστημά μας και θα σας επιστραφεί ολόκληρο το ποσό, ακόμη και χωρίς απόδειξη και ακόμη κι αν το βάζο είναι ανοιγμένο.", "If you have bought this product, please do not consume it. You can return it to any of our stores and the full amount will be refunded, even without a receipt and even if the jar has been opened."),
  L("Υπάλληλος", "f", "Οι υπόλοιπες παρτίδες, καθώς και όλα τα άλλα προϊόντα της ίδιας εταιρείας, είναι απολύτως ασφαλή. Για περισσότερες πληροφορίες απευθυνθείτε στο γραφείο εξυπηρέτησης πελατών, δίπλα στην έξοδο.", "The other batches, as well as all the other products of the same company, are completely safe. For more information please go to the customer service desk next to the exit."),
 ],
 "questions": [
  Q("Ποιο προϊόν ανακαλείται;", ["Όλα τα προϊόντα της εταιρείας", "Μια συγκεκριμένη παρτίδα ταχινιού", "Όλα τα βάζα με ταχίνι", "Ένα γιαούρτι"], 1, "ανακαλεί μια συγκεκριμένη παρτίδα ταχινιού"),
  Q("Τι ισχύει για την επιστροφή;", ["Χρειάζεται απόδειξη", "Γίνεται μόνο στο κατάστημα όπου έγινε η αγορά", "Επιστρέφεται όλο το ποσό, ακόμη και χωρίς απόδειξη", "Το βάζο πρέπει να είναι κλειστό"], 2, "θα σας επιστραφεί ολόκληρο το ποσό, ακόμη και χωρίς απόδειξη"),
  Q("Πού μπορεί κανείς να ζητήσει περισσότερες πληροφορίες;", ["Στο γραφείο εξυπηρέτησης πελατών, δίπλα στην έξοδο", "Στα ταμεία", "Στο τμήμα τροφίμων", "Μόνο τηλεφωνικά"], 0, "στο γραφείο εξυπηρέτησης πελατών, δίπλα στην έξοδο"),
 ],
 "gloss": {"προμηθευτής": "προμηθευτής — supplier", "ανακαλεί": "ανακαλώ — to recall (a product)", "παρτίδα": "παρτίδα — batch", "ταχινιού": "ταχίνι — tahini", "βάζο": "βάζο — jar", "μικροβιακή": "μικροβιακός — microbial", "επιμόλυνση": "επιμόλυνση — contamination", "ημερομηνία λήξης": "ημερομηνία λήξης — expiry date", "καταναλώσετε": "καταναλώνω — to consume", "επιστραφεί": "επιστρέφομαι — to be refunded, returned", "απόδειξη": "απόδειξη — receipt", "εξυπηρέτησης πελατών": "εξυπηρέτηση πελατών — customer service"},
})

ITEMS.append({
 "id": "l167-int-antikatastatis", "title": "Ο αντικαταστάτης που βγήκε στη σκηνή", "title_en": "The understudy who went on stage", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν νέο ηθοποιό που αντικατέστησε ξαφνικά τον πρωταγωνιστή μιας παράστασης.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι ακριβώς κάνει ένας αντικαταστάτης;", "What exactly does an understudy do?"),
  L("Ηθοποιός", "m", "Μαθαίνει έναν ρόλο που μάλλον δεν θα παίξει ποτέ. Εγώ είχα έναν μικρό ρόλο στην παράσταση, αλλά ήξερα απ' έξω και όλα τα λόγια του πρωταγωνιστή. Κάθε βράδυ τον παρακολουθούσα από τα παρασκήνια και σημείωνα πού στέκεται, πότε κάθεται, πότε κοιτάζει τους άλλους.", "He learns a role he will probably never play. I had a small part in the show, but I also knew all the lead's lines by heart. Every night I watched him from the wings and noted where he stands, when he sits, when he looks at the others."),
  L("Δημοσιογράφος", "f", "Και ήρθε η μεγάλη στιγμή.", "And the big moment came."),
  L("Ηθοποιός", "m", "Ένα Σάββατο, δύο ώρες πριν από την παράσταση, ο πρωταγωνιστής έχασε τελείως τη φωνή του. Ο σκηνοθέτης με πήρε τηλέφωνο ενώ ήμουν στο μετρό. Τα πόδια μου έτρεμαν. Το κοστούμι μού ήταν μεγάλο, οπότε η ενδυματολόγος το έραβε πάνω μου ενώ εγώ επαναλάμβανα τις πρώτες σκηνές.", "One Saturday, two hours before the show, the lead completely lost his voice. The director phoned me while I was on the metro. My legs were shaking. The costume was too big for me, so the costume designer was sewing it on me while I went over the first scenes."),
  L("Δημοσιογράφος", "f", "Πώς πήγε;", "How did it go?"),
  L("Ηθοποιός", "m", "Ξέχασα μια ατάκα στη δεύτερη πράξη, αλλά ο συνάδελφός μου με βοήθησε τόσο φυσικά, που κανείς δεν το κατάλαβε. Στο τέλος ο πρωταγωνιστής, με τη βραχνή φωνή του, μου έστειλε μήνυμα: «Τώρα ξέρεις γιατί δεν αρρωσταίνω ποτέ.» Γελάσαμε πολύ.", "I forgot a line in the second act, but my colleague helped me so naturally that nobody noticed. At the end the lead, with his hoarse voice, sent me a message: 'Now you know why I never get ill.' We laughed a lot."),
 ],
 "questions": [
  Q("Τι έκανε κάθε βράδυ από τα παρασκήνια;", ["Ετοίμαζε τα σκηνικά", "Παρακολουθούσε τον πρωταγωνιστή και σημείωνε τις κινήσεις του", "Βοηθούσε την ενδυματολόγο", "Έλεγχε τα φώτα"], 1, "Κάθε βράδυ τον παρακολουθούσα από τα παρασκήνια και σημείωνα"),
  Q("Τι έγινε με το κοστούμι;", ["Ήταν μικρό και το άλλαξαν", "Δεν βρέθηκε", "Ήταν μεγάλο και η ενδυματολόγος το έραβε πάνω του", "Το φόρεσε ανάποδα"], 2, "Το κοστούμι μού ήταν μεγάλο, οπότε η ενδυματολόγος το έραβε πάνω μου"),
  Q("Τι συνέβη στη δεύτερη πράξη;", ["Ξέχασε μια ατάκα, αλλά ένας συνάδελφος τον βοήθησε χωρίς να φανεί", "Έπεσε στη σκηνή", "Σταμάτησε η παράσταση", "Το κοινό χειροκρότησε στη μέση"], 0, "Ξέχασα μια ατάκα στη δεύτερη πράξη, αλλά ο συνάδελφός μου με βοήθησε"),
 ],
 "gloss": {"αντικατέστησε": "αντικαθιστώ — to replace", "πρωταγωνιστή": "πρωταγωνιστής — lead actor", "αντικαταστάτης": "αντικαταστάτης — understudy, substitute", "απ' έξω": "ξέρω απ' έξω — to know by heart", "παρασκήνια": "παρασκήνια — backstage, wings", "σκηνοθέτης": "σκηνοθέτης — director", "έτρεμαν": "τρέμω — to tremble", "ενδυματολόγος": "ενδυματολόγος — costume designer", "έραβε": "ράβω — to sew", "ατάκα": "ατάκα — line (in a play)", "πράξη": "πράξη — act", "βραχνή": "βραχνός — hoarse"},
})

ITEMS.append({
 "id": "l167-int-xamena-antikeimena", "title": "Στο γραφείο απολεσθέντων του μετρό", "title_en": "At the metro lost property office", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με την υπεύθυνη του γραφείου απολεσθέντων αντικειμένων σε ένα δίκτυο μετρό.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ξεχνούν πιο συχνά οι επιβάτες;", "What do passengers forget most often?"),
  L("Υπεύθυνη", "f", "Ομπρέλες, χωρίς αμφιβολία. Μια βροχερή μέρα μπορεί να μαζέψουμε πάνω από πενήντα. Ακολουθούν τα κινητά, τα κλειδιά και τα γυαλιά. Αλλά έχουμε δει και πιο παράξενα πράγματα: ένα βιολί, μια πλαστική γλάστρα με βασιλικό, ακόμη και ένα νυφικό μέσα σε θήκη.", "Umbrellas, without a doubt. On a rainy day we may collect more than fifty. Next come mobile phones, keys and glasses. But we've also seen stranger things: a violin, a plastic pot of basil, even a wedding dress in a garment bag."),
  L("Δημοσιογράφος", "m", "Πόσο καιρό κρατάτε τα αντικείμενα;", "How long do you keep the items?"),
  L("Υπεύθυνη", "f", "Τα περισσότερα για τρεις μήνες. Ό,τι έχει ταυτότητα ή κάρτα με όνομα το στέλνουμε στην αστυνομία πολύ νωρίτερα, για να βρεθεί ο κάτοχος. Ό,τι δεν το ζητήσει κανείς, και είναι σε καλή κατάσταση, το δίνουμε σε φιλανθρωπικές οργανώσεις.", "Most for three months. Anything with an ID or a card with a name we send to the police much earlier, so the owner can be found. Whatever nobody claims, and is in good condition, we give to charities."),
  L("Δημοσιογράφος", "m", "Θυμάστε κάποια ιστορία με χαρούμενο τέλος;", "Do you remember a story with a happy ending?"),
  L("Υπεύθυνη", "f", "Η νύφη με το νυφικό! Ήρθε τρέχοντας, κλαίγοντας, την παραμονή του γάμου της. Όταν της είπαμε ότι το νυφικό ήταν εδώ, άρχισε να αγκαλιάζει όλους μας. Μας έστειλε μετά και φωτογραφία από τον γάμο. Την έχουμε ακόμα κολλημένη στον τοίχο.", "The bride with the wedding dress! She came running, crying, on the eve of her wedding. When we told her the dress was here, she started hugging all of us. She later sent us a photo from the wedding too. We still have it stuck on the wall."),
 ],
 "questions": [
  Q("Τι ξεχνούν πιο συχνά οι επιβάτες;", ["Κινητά", "Ομπρέλες", "Κλειδιά", "Βιβλία"], 1, "Ομπρέλες, χωρίς αμφιβολία"),
  Q("Τι γίνεται με όσα αντικείμενα έχουν ταυτότητα ή κάρτα με όνομα;", ["Πετιούνται", "Μένουν τρεις μήνες στο γραφείο", "Στέλνονται νωρίτερα στην αστυνομία", "Δίνονται σε φιλανθρωπικές οργανώσεις"], 2, "Ό,τι έχει ταυτότητα ή κάρτα με όνομα το στέλνουμε στην αστυνομία πολύ νωρίτερα"),
  Q("Τι έστειλε η νύφη στο γραφείο;", ["Μια φωτογραφία από τον γάμο", "Λουλούδια", "Γλυκά", "Ένα γράμμα"], 0, "Μας έστειλε μετά και φωτογραφία από τον γάμο"),
 ],
 "gloss": {"υπεύθυνη": "υπεύθυνος — person in charge", "απολεσθέντων": "απολεσθέντα — lost property", "επιβάτες": "επιβάτης — passenger", "αμφιβολία": "αμφιβολία — doubt", "βροχερή": "βροχερός — rainy", "παράξενα": "παράξενος — strange", "γλάστρα": "γλάστρα — flowerpot", "βασιλικό": "βασιλικός — basil", "νυφικό": "νυφικό — wedding dress", "θήκη": "θήκη — case, garment bag", "κάτοχος": "κάτοχος — owner, holder", "φιλανθρωπικές": "φιλανθρωπικός — charitable", "παραμονή": "παραμονή — eve"},
})

ITEMS.append({
 "id": "l167-dia-dyo-protaseis-ergasias", "title": "Δύο προτάσεις για δουλειά", "title_en": "Two job offers", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο ανάμεσα σε δύο φίλους. Ο ένας έχει δεχτεί δύο προτάσεις εργασίας και δεν ξέρει ποια να διαλέξει.",
 "script": [
  L("Θοδωρής", "m", "Λοιπόν, Ελπίδα, χρειάζομαι τη γνώμη σου. Με πήραν και από τις δύο εταιρείες. Η μία είναι μεγάλη, στο κέντρο, με καλύτερο μισθό. Η άλλη είναι μια μικρή εταιρεία λογισμικού εδώ στη γειτονιά.", "So, Elpida, I need your opinion. Both companies called me. One is big, in the centre, with a better salary. The other is a small software company here in the neighbourhood."),
  L("Ελπίδα", "f", "Πόση είναι η διαφορά στον μισθό;", "How big is the difference in salary?"),
  L("Θοδωρής", "m", "Γύρω στα διακόσια ευρώ τον μήνα. Αλλά για τη μεγάλη θα χρειάζομαι μία ώρα να πάω και μία να γυρίσω. Στη μικρή θα πηγαίνω με τα πόδια, και μου είπαν ότι μπορώ να δουλεύω από το σπίτι δύο μέρες την εβδομάδα.", "About two hundred euros a month. But for the big one I'll need an hour to get there and an hour to get back. To the small one I'll walk, and they told me I can work from home two days a week."),
  L("Ελπίδα", "f", "Δηλαδή δέκα ώρες την εβδομάδα στον δρόμο, για διακόσια ευρώ. Αν βάλεις μέσα και τα εισιτήρια, η διαφορά μικραίνει ακόμα περισσότερο.", "So ten hours a week on the road, for two hundred euros. If you include the tickets, the difference gets even smaller."),
  L("Θοδωρής", "m", "Σωστά. Από την άλλη, η μεγάλη εταιρεία έχει προγράμματα εκπαίδευσης και μπορείς να ανέβεις πιο γρήγορα. Στη μικρή θα είμαι ένας από τους οχτώ.", "Right. On the other hand, the big company has training programmes and you can move up faster. At the small one I'll be one of eight."),
  L("Ελπίδα", "f", "Σε μια μικρή ομάδα μαθαίνεις συχνά περισσότερα, γιατί κάνεις λίγο απ' όλα. Ρώτα τους πάντως αν σου πληρώνουν σεμινάρια. Αν πουν ναι, εγώ ξέρω τι θα διάλεγα.", "In a small team you often learn more, because you do a bit of everything. Ask them, anyway, whether they'll pay for courses. If they say yes, I know what I'd choose."),
 ],
 "questions": [
  Q("Ποιο είναι το μεγάλο μειονέκτημα της μεγάλης εταιρείας;", ["Ο χαμηλός μισθός", "Οι δύο ώρες μετακίνησης κάθε μέρα", "Οι λίγοι συνάδελφοι", "Το ωράριο τα Σάββατα"], 1, "για τη μεγάλη θα χρειάζομαι μία ώρα να πάω και μία να γυρίσω"),
  Q("Γιατί, κατά την Ελπίδα, η διαφορά στον μισθό είναι μικρότερη από ό,τι φαίνεται;", ["Γιατί η μικρή εταιρεία δίνει μπόνους", "Γιατί υπάρχουν φόροι", "Γιατί πρέπει να υπολογίσει και τα εισιτήρια", "Γιατί η μεγάλη πληρώνει αργά"], 2, "Αν βάλεις μέσα και τα εισιτήρια, η διαφορά μικραίνει"),
  Q("Τι του προτείνει να ρωτήσει τη μικρή εταιρεία;", ["Αν του πληρώνουν σεμινάρια", "Αν μπορεί να ξεκινήσει αργότερα", "Πόσες μέρες άδεια έχει", "Αν έχει πάρκινγκ"], 0, "Ρώτα τους πάντως αν σου πληρώνουν σεμινάρια"),
 ],
 "gloss": {"προτάσεις εργασίας": "πρόταση εργασίας — job offer", "μισθό": "μισθός — salary", "λογισμικού": "λογισμικό — software", "εισιτήρια": "εισιτήριο — ticket", "μικραίνει": "μικραίνω — to shrink", "εκπαίδευσης": "εκπαίδευση — training", "ανέβεις": "ανεβαίνω — to move up, be promoted", "σεμινάρια": "σεμινάριο — training course", "διάλεγα": "διαλέγω — to choose"},
})

ITEMS.append({
 "id": "l167-dia-doro-daskala", "title": "Δώρο για τη δασκάλα στο τέλος της χρονιάς", "title_en": "An end-of-year gift for the teacher", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο ανάμεσα σε δύο γονείς της ίδιας τάξης, που οργανώνουν ένα δώρο για τη δασκάλα.",
 "script": [
  L("Μαρίνα", "f", "Στέφανε, μαζέψαμε από τους γονείς γύρω στα εκατόν πενήντα ευρώ για το δώρο της κυρίας Ευτυχίας. Κάποιοι πρότειναν μια κάρτα δώρου από ένα κατάστημα με καλλυντικά.", "Stefanos, we've collected about a hundred and fifty euros from the parents for Mrs Eftychia's gift. Some suggested a gift card from a cosmetics shop."),
  L("Στέφανος", "m", "Δεν ξέρω, μου φαίνεται λίγο απρόσωπο. Η κυρία Ευτυχία έφτιαξε φέτος με τα παιδιά έναν ολόκληρο λαχανόκηπο στην αυλή. Κάτι που να έχει σχέση με αυτό;", "I don't know, it seems a bit impersonal to me. This year Mrs Eftychia made a whole vegetable garden in the yard with the children. Something to do with that?"),
  L("Μαρίνα", "f", "Ωραία ιδέα. Θα μπορούσαμε να πάρουμε ένα καλό σετ εργαλεία κηπουρικής και μια πανέμορφη γλάστρα. Και με τα υπόλοιπα, να κάνουμε ένα άλμπουμ.", "Nice idea. We could get a good set of gardening tools and a beautiful pot. And with the rest, make an album."),
  L("Στέφανος", "m", "Άλμπουμ με φωτογραφίες από τον κήπο;", "An album with photos from the garden?"),
  L("Μαρίνα", "f", "Όχι μόνο. Κάθε παιδί να ζωγραφίσει μια σελίδα και να γράψει μια φράση για ό,τι θυμάται πιο πολύ από τη χρονιά. Αυτό θα το κρατήσει για πάντα, ενώ μια κάρτα δώρου την ξοδεύεις και την ξεχνάς.", "Not only that. Each child could draw a page and write a sentence about what they remember most from the year. She'll keep that forever, whereas a gift card you spend and forget."),
  L("Στέφανος", "m", "Συμφωνώ. Αναλαμβάνω εγώ να μαζέψω τις ζωγραφιές μέχρι την Παρασκευή, και εσύ τα εργαλεία;", "Agreed. I'll take on collecting the drawings by Friday, and you the tools?"),
 ],
 "questions": [
  Q("Γιατί ο Στέφανος δεν θέλει την κάρτα δώρου;", ["Γιατί είναι ακριβή", "Γιατί του φαίνεται απρόσωπη", "Γιατί στη δασκάλα δεν αρέσουν τα καλλυντικά", "Γιατί δεν μαζεύτηκαν αρκετά χρήματα"], 1, "μου φαίνεται λίγο απρόσωπο"),
  Q("Τι έφτιαξε η δασκάλα με τα παιδιά φέτος;", ["Μια θεατρική παράσταση", "Μια σχολική εφημερίδα", "Έναν λαχανόκηπο στην αυλή", "Ένα βίντεο"], 2, "έφτιαξε φέτος με τα παιδιά έναν ολόκληρο λαχανόκηπο στην αυλή"),
  Q("Τι θα περιέχει το άλμπουμ;", ["Μια ζωγραφιά και μια φράση από κάθε παιδί", "Μόνο φωτογραφίες από την τάξη", "Ευχές από τους γονείς", "Συνταγές με λαχανικά"], 0, "Κάθε παιδί να ζωγραφίσει μια σελίδα και να γράψει μια φράση"),
 ],
 "gloss": {"οργανώνουν": "οργανώνω — to organise", "κάρτα δώρου": "κάρτα δώρου — gift card", "καλλυντικά": "καλλυντικά — cosmetics", "απρόσωπο": "απρόσωπος — impersonal", "λαχανόκηπο": "λαχανόκηπος — vegetable garden", "εργαλεία κηπουρικής": "εργαλεία κηπουρικής — gardening tools", "γλάστρα": "γλάστρα — flowerpot", "άλμπουμ": "άλμπουμ — album", "ζωγραφίσει": "ζωγραφίζω — to draw, paint", "ξοδεύεις": "ξοδεύω — to spend", "ζωγραφιές": "ζωγραφιά — drawing"},
})

ITEMS.append({
 "id": "l167-mon-gata-me-yiothetise", "title": "Η γάτα που με υιοθέτησε", "title_en": "The cat that adopted me", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να διηγείται σε ένα ραδιοφωνικό πρόγραμμα πώς απέκτησε γάτα, χωρίς να το θέλει.",
 "script": [
  L("Άντρας", "m", "Ποτέ δεν ήθελα κατοικίδιο. Δουλεύω πολλές ώρες και ταξιδεύω συχνά. Πριν από τρία χρόνια όμως, ένα βράδυ του Νοεμβρίου, μια κοκαλιάρικη γκρίζα γάτα κάθισε στο μπαλκόνι μου και με κοίταζε από το τζάμι. Της έδωσα λίγο τυρί, μόνο για εκείνο το βράδυ, όπως είπα στον εαυτό μου.", "I never wanted a pet. I work long hours and travel often. Three years ago, though, one November evening, a scrawny grey cat sat on my balcony and stared at me through the glass. I gave her a bit of cheese, just for that evening, as I told myself."),
  L("Άντρας", "m", "Το επόμενο βράδυ ήταν πάλι εκεί, στην ίδια θέση, στην ίδια ώρα. Μετά από μία εβδομάδα είχα αγοράσει τροφή για γάτες, «για να μην τρώει τυρί, που δεν της κάνει καλό». Μετά από έναν μήνα, μια μέρα με βροχή, άφησα την μπαλκονόπορτα ανοιχτή. Μπήκε, έκανε έναν γύρο στο σαλόνι και κοιμήθηκε στον καναπέ, σαν να ήταν πάντα δικός της.", "The next evening she was there again, in the same spot, at the same time. After a week I had bought cat food, 'so she wouldn't eat cheese, which isn't good for her'. After a month, on a rainy day, I left the balcony door open. She came in, did a lap of the living room and fell asleep on the sofa, as if it had always been hers."),
  L("Άντρας", "m", "Την πήγα στον κτηνίατρο, της έβαλα τσιπάκι και την ονόμασα Σταχτή. Όταν ταξιδεύω, τη φροντίζει η γειτόνισσα, που την έχει πια ερωτευτεί κι εκείνη. Οι φίλοι μου λένε ότι εγώ υιοθέτησα μια γάτα. Εγώ ξέρω την αλήθεια: εκείνη με διάλεξε, και εγώ απλώς δεν αντιστάθηκα.", "I took her to the vet, had her microchipped and named her Stachti. When I travel, the neighbour looks after her, who has fallen for her too by now. My friends say I adopted a cat. I know the truth: she chose me, and I simply didn't resist."),
 ],
 "questions": [
  Q("Γιατί δεν ήθελε ποτέ κατοικίδιο;", ["Γιατί έχει αλλεργία", "Γιατί δουλεύει πολλές ώρες και ταξιδεύει συχνά", "Γιατί το σπίτι του είναι μικρό", "Γιατί φοβάται τις γάτες"], 1, "Δουλεύω πολλές ώρες και ταξιδεύω συχνά"),
  Q("Γιατί αγόρασε τροφή για γάτες;", ["Γιατί του το είπε ο κτηνίατρος", "Γιατί ήταν σε προσφορά", "Για να μην τρώει η γάτα τυρί, που δεν της κάνει καλό", "Για τη γάτα της γειτόνισσας"], 2, "«για να μην τρώει τυρί, που δεν της κάνει καλό»"),
  Q("Ποιος φροντίζει τη γάτα όταν εκείνος ταξιδεύει;", ["Η γειτόνισσα", "Ένας φίλος", "Ένα ξενοδοχείο για ζώα", "Η αδελφή του"], 0, "τη φροντίζει η γειτόνισσα"),
 ],
 "gloss": {"απέκτησε": "αποκτώ — to acquire, get", "κατοικίδιο": "κατοικίδιο — pet", "κοκαλιάρικη": "κοκαλιάρικος — scrawny, bony", "τζάμι": "τζάμι — windowpane", "τροφή": "τροφή — food (for animals)", "μπαλκονόπορτα": "μπαλκονόπορτα — balcony door", "κτηνίατρο": "κτηνίατρος — vet", "τσιπάκι": "τσιπάκι — microchip", "ερωτευτεί": "ερωτεύομαι — to fall in love", "υιοθέτησα": "υιοθετώ — to adopt", "αντιστάθηκα": "αντιστέκομαι — to resist"},
})

ITEMS.append({
 "id": "l167-vm-xenodoxeio-fortistis", "title": "Μήνυμα από το ξενοδοχείο για έναν ξεχασμένο φορτιστή", "title_en": "A message from the hotel about a forgotten charger", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από ένα ξενοδοχείο όπου μείνατε το περασμένο Σαββατοκύριακο.",
 "script": [
  L("Ρεσεψιονίστ", "f", "Καλημέρα σας, κύριε Αλεξίου, η Δέσποινα από τη ρεσεψιόν του ξενοδοχείου «Αμάραντος» στην Καλαμπάκα. Η καμαριέρα βρήκε στο δωμάτιο που μείνατε έναν φορτιστή φορητού υπολογιστή, μαζί με ένα μαύρο καλώδιο, στην πρίζα πίσω από το κομοδίνο. Υποθέτουμε ότι είναι δικά σας.", "Good morning, Mr Alexiou, this is Despoina from the reception of the Amarantos hotel in Kalambaka. The chambermaid found in the room you stayed in a laptop charger, together with a black cable, in the socket behind the bedside table. We assume they're yours."),
  L("Ρεσεψιονίστ", "f", "Μπορούμε να σας τα στείλουμε με courier. Το κόστος είναι περίπου επτά ευρώ, με αντικαταβολή, και θα τα έχετε σε δύο εργάσιμες μέρες. Αν προτιμάτε, μπορεί να τα παραλάβει κάποιος γνωστός σας από τη ρεσεψιόν, αρκεί να μας πείτε το όνομά του.", "We can send them to you by courier. The cost is about seven euros, cash on delivery, and you'll have them in two working days. If you prefer, someone you know can collect them from reception, as long as you tell us their name."),
  L("Ρεσεψιονίστ", "f", "Παρακαλώ στείλτε μας ένα email με τη διεύθυνση όπου θέλετε να σας τα στείλουμε. Τα κρατάμε στο χρηματοκιβώτιο της ρεσεψιόν για έναν μήνα. Ευχαριστούμε και ελπίζουμε να σας ξαναδούμε.", "Please send us an email with the address where you'd like us to send them. We'll keep them in the reception safe for a month. Thank you and we hope to see you again."),
 ],
 "questions": [
  Q("Πού βρέθηκε ο φορτιστής;", ["Στο μπάνιο", "Στην πρίζα πίσω από το κομοδίνο", "Στη ρεσεψιόν", "Στο εστιατόριο"], 1, "στην πρίζα πίσω από το κομοδίνο"),
  Q("Πώς θα πληρωθεί η αποστολή με courier;", ["Με κάρτα από πριν", "Δωρεάν", "Με αντικαταβολή", "Με τραπεζική μεταφορά"], 2, "με αντικαταβολή"),
  Q("Τι ζητάει να της στείλει ο πελάτης;", ["Ένα email με τη διεύθυνση αποστολής", "Μια φωτογραφία του φορτιστή", "Τον αριθμό της κράτησης", "Την απόδειξη"], 0, "στείλτε μας ένα email με τη διεύθυνση"),
 ],
 "gloss": {"καμαριέρα": "καμαριέρα — chambermaid", "φορτιστή": "φορτιστής — charger", "φορητού υπολογιστή": "φορητός υπολογιστής — laptop", "καλώδιο": "καλώδιο — cable", "πρίζα": "πρίζα — socket", "κομοδίνο": "κομοδίνο — bedside table", "Υποθέτουμε": "υποθέτω — to assume", "αντικαταβολή": "αντικαταβολή — cash on delivery", "εργάσιμες": "εργάσιμος — working (day)", "παραλάβει": "παραλαμβάνω — to collect, receive", "χρηματοκιβώτιο": "χρηματοκιβώτιο — safe"},
})

ITEMS.append({
 "id": "l167-vm-vivliothiki-kratisi", "title": "Μήνυμα από τη βιβλιοθήκη: ήρθε το βιβλίο σας", "title_en": "A message from the library: your book has arrived", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη δημοτική βιβλιοθήκη, όπου είχατε ζητήσει ένα βιβλίο.",
 "script": [
  L("Βιβλιοθηκάριος", "m", "Καλησπέρα, από τη δημοτική βιβλιοθήκη σας παίρνουμε. Το βιβλίο που είχατε κρατήσει, «Η ζωή εν τάφω» του Στράτη Μυριβήλη, επιστράφηκε σήμερα και σας περιμένει στο γκισέ του δανεισμού.", "Good evening, we're calling from the municipal library. The book you had reserved, 'Life in the Tomb' by Stratis Myrivilis, was returned today and is waiting for you at the loans desk."),
  L("Βιβλιοθηκάριος", "m", "Θα το κρατήσουμε για εσάς ως την επόμενη Τετάρτη. Αν δεν περάσετε ως τότε, θα πάει στον επόμενο αναγνώστη της λίστας, γιατί υπάρχουν άλλοι τρεις που το περιμένουν. Για τον ίδιο λόγο, ο δανεισμός γι' αυτό το βιβλίο είναι δύο εβδομάδες και όχι τρεις, και δεν μπορεί να ανανεωθεί.", "We'll hold it for you until next Wednesday. If you don't come by then, it will go to the next reader on the list, because three others are waiting for it. For the same reason, the loan for this book is two weeks rather than three, and it cannot be renewed."),
  L("Βιβλιοθηκάριος", "m", "Να σας θυμίσουμε επίσης ότι έχετε ακόμη ένα βιβλίο με μαγειρικές συνταγές, που έπρεπε να επιστραφεί την περασμένη εβδομάδα. Φέρτε το, παρακαλώ, όταν έρθετε. Καλή ανάγνωση!", "We'd also like to remind you that you still have a cookery book which should have been returned last week. Please bring it when you come. Happy reading!"),
 ],
 "questions": [
  Q("Ως πότε θα κρατήσουν το βιβλίο;", ["Ως αύριο", "Ως την επόμενη Τετάρτη", "Για έναν μήνα", "Για τρεις εβδομάδες"], 1, "Θα το κρατήσουμε για εσάς ως την επόμενη Τετάρτη"),
  Q("Γιατί ο δανεισμός είναι μόνο δύο εβδομάδες;", ["Γιατί το βιβλίο είναι παλιό", "Γιατί η βιβλιοθήκη κλείνει", "Γιατί υπάρχουν άλλοι τρεις αναγνώστες που το περιμένουν", "Γιατί έχετε καθυστερήσει άλλο βιβλίο"], 2, "Για τον ίδιο λόγο, ο δανεισμός γι' αυτό το βιβλίο είναι δύο εβδομάδες"),
  Q("Τι σας ζητούν να φέρετε;", ["Ένα βιβλίο μαγειρικής που έπρεπε να έχει επιστραφεί", "Την κάρτα μέλους", "Ταυτότητα", "Ένα πρόστιμο"], 0, "έχετε ακόμη ένα βιβλίο με μαγειρικές συνταγές, που έπρεπε να επιστραφεί"),
 ],
 "gloss": {"βιβλιοθήκη": "βιβλιοθήκη — library", "κρατήσει": "κρατάω — to reserve, hold", "Μυριβήλη": "Μυριβήλης — Myrivilis (writer)", "επιστράφηκε": "επιστρέφομαι — to be returned", "γκισέ": "γκισέ — desk, counter", "δανεισμού": "δανεισμός — loan, lending", "αναγνώστη": "αναγνώστης — reader", "ανανεωθεί": "ανανεώνομαι — to be renewed", "συνταγές": "συνταγή — recipe"},
})

ITEMS.append({
 "id": "l167-c1-disekta-eti", "title": "Γιατί υπάρχουν δίσεκτα χρόνια", "title_en": "Why there are leap years", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν αστρονόμο σε μια ραδιοφωνική εκπομπή για την επιστήμη, με αφορμή την 29η Φεβρουαρίου.",
 "script": [
  L("Δημοσιογράφος", "f", "Γιατί χρειαζόμαστε μια επιπλέον μέρα κάθε τέσσερα χρόνια;", "Why do we need an extra day every four years?"),
  L("Αστρονόμος", "m", "Γιατί η Γη δεν κάνει τον γύρο του Ήλιου σε ακριβώς τριακόσιες εξήντα πέντε μέρες, αλλά σε τριακόσιες εξήντα πέντε μέρες και σχεδόν έξι ώρες. Αν αγνοούσαμε αυτές τις ώρες, το ημερολόγιο θα ξέφευγε σιγά σιγά από τις εποχές, και σε μερικούς αιώνες θα γιορτάζαμε τα Χριστούγεννα με καλοκαιρία. Οι έξι ώρες επί τέσσερα χρόνια μάς δίνουν περίπου μία μέρα, και αυτή την προσθέτουμε τον Φεβρουάριο.", "Because the Earth doesn't go round the Sun in exactly three hundred and sixty-five days, but in three hundred and sixty-five days and almost six hours. If we ignored those hours, the calendar would gradually drift away from the seasons, and in a few centuries we'd be celebrating Christmas in summer weather. Six hours times four years gives us about one day, and we add it in February."),
  L("Δημοσιογράφος", "f", "Είπατε «σχεδόν» έξι ώρες.", "You said 'almost' six hours."),
  L("Αστρονόμος", "m", "Ακριβώς, και εκεί βρίσκεται το πρόβλημα. Το ιουλιανό ημερολόγιο, που καθιερώθηκε επί Ιουλίου Καίσαρα, έβαζε δίσεκτο κάθε τέσσερα χρόνια χωρίς εξαίρεση. Έτσι κάθε χρόνος ήταν περίπου έντεκα λεπτά μεγαλύτερος από τον πραγματικό. Φαίνεται ασήμαντο, αλλά μέχρι τον 16ο αιώνα το λάθος είχε φτάσει τις δέκα μέρες. Το 1582 ο πάπας Γρηγόριος ο 13ος έβγαλε δέκα μέρες από το ημερολόγιο, και την Πέμπτη 4 Οκτωβρίου ακολούθησε η Παρασκευή 15 Οκτωβρίου.", "Exactly, and that's where the problem lies. The Julian calendar, established under Julius Caesar, made every fourth year a leap year without exception. So each year was about eleven minutes longer than the real one. It seems trivial, but by the 16th century the error had reached ten days. In 1582 Pope Gregory XIII removed ten days from the calendar, and Thursday 4 October was followed by Friday 15 October."),
  L("Δημοσιογράφος", "f", "Και πώς διορθώθηκε από εκεί και πέρα;", "And how was it corrected from then on?"),
  L("Αστρονόμος", "m", "Με έναν έξυπνο κανόνα: οι χρονιές που κλείνουν αιώνα δεν είναι δίσεκτες, εκτός αν διαιρούνται με το τετρακόσια. Γι' αυτό το 1900 δεν ήταν δίσεκτο, ενώ το 2000 ήταν. Με αυτόν τον κανόνα το λάθος περιορίζεται σε μία μέρα περίπου κάθε τρεις χιλιάδες χρόνια. Η Ελλάδα, πάντως, υιοθέτησε το γρηγοριανό ημερολόγιο για την πολιτική ζωή μόλις το 1923.", "With a clever rule: years that end a century are not leap years, unless they are divisible by four hundred. That's why 1900 was not a leap year, while 2000 was. With this rule the error is reduced to about one day every three thousand years. Greece, incidentally, adopted the Gregorian calendar for civil life only in 1923."),
 ],
 "questions": [
  Q("Τι θα συνέβαινε αν δεν υπήρχαν δίσεκτα χρόνια;", ["Οι μήνες θα είχαν διαφορετικό μήκος", "Το ημερολόγιο θα ξέφευγε σιγά σιγά από τις εποχές", "Η Γη θα γύριζε πιο αργά", "Τίποτα το ιδιαίτερο"], 1, "το ημερολόγιο θα ξέφευγε σιγά σιγά από τις εποχές"),
  Q("Ποιο ήταν το πρόβλημα του ιουλιανού ημερολογίου;", ["Δεν είχε καθόλου δίσεκτα χρόνια", "Είχε δεκατρείς μήνες", "Κάθε χρόνος ήταν περίπου έντεκα λεπτά μεγαλύτερος από τον πραγματικό", "Άρχιζε τον Μάρτιο"], 2, "κάθε χρόνος ήταν περίπου έντεκα λεπτά μεγαλύτερος από τον πραγματικό"),
  Q("Γιατί το 1900 δεν ήταν δίσεκτο;", ["Γιατί έκλεινε αιώνα και δεν διαιρείται με το τετρακόσια", "Γιατί δεν διαιρείται με το τέσσερα", "Γιατί το αποφάσισε η Ελλάδα", "Γιατί ήταν λάθος"], 0, "οι χρονιές που κλείνουν αιώνα δεν είναι δίσεκτες, εκτός αν διαιρούνται με το τετρακόσια"),
 ],
 "gloss": {"αστρονόμο": "αστρονόμος — astronomer", "αφορμή": "με αφορμή — on the occasion of", "αγνοούσαμε": "αγνοώ — to ignore", "ημερολόγιο": "ημερολόγιο — calendar", "ξέφευγε": "ξεφεύγω — to drift, escape", "εποχές": "εποχή — season", "καλοκαιρία": "καλοκαιρία — fine (summer) weather", "δίσεκτο": "δίσεκτος — leap (year)", "καθιερώθηκε": "καθιερώνομαι — to be established", "εξαίρεση": "εξαίρεση — exception", "ασήμαντο": "ασήμαντος — trivial", "διαιρούνται": "διαιρούμαι — to be divisible", "περιορίζεται": "περιορίζομαι — to be limited", "υιοθέτησε": "υιοθετώ — to adopt"},
})

ITEMS.append({
 "id": "l167-c1-pagos-epiplei", "title": "Γιατί ο πάγος επιπλέει", "title_en": "Why ice floats", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια χημικό να μιλά σε μια διάλεξη για το κοινό σχετικά με τις παράξενες ιδιότητες του νερού.",
 "script": [
  L("Χημικός", "f", "Σχεδόν όλα τα υλικά, όταν στερεοποιούνται, γίνονται πυκνότερα: τα μόριά τους πλησιάζουν μεταξύ τους, και το στερεό βουλιάζει μέσα στο υγρό. Το νερό είναι μια εντυπωσιακή εξαίρεση. Ο πάγος είναι περίπου εννιά τοις εκατό λιγότερο πυκνός από το νερό, και γι' αυτό επιπλέει. Ο λόγος βρίσκεται στους δεσμούς υδρογόνου: όταν το νερό παγώνει, τα μόρια οργανώνονται σε ένα ανοιχτό εξαγωνικό πλέγμα, με περισσότερο κενό χώρο ανάμεσά τους από ό,τι στο υγρό.", "Almost all materials, when they solidify, become denser: their molecules move closer together, and the solid sinks in the liquid. Water is a striking exception. Ice is about nine per cent less dense than water, and that's why it floats. The reason lies in hydrogen bonds: when water freezes, the molecules arrange themselves in an open hexagonal lattice, with more empty space between them than in the liquid."),
  L("Χημικός", "f", "Υπάρχει και μια δεύτερη παραξενιά: το νερό έχει τη μεγαλύτερη πυκνότητά του όχι στους μηδέν, αλλά περίπου στους τέσσερις βαθμούς Κελσίου. Σκεφτείτε μια λίμνη τον χειμώνα. Το νερό της επιφάνειας κρυώνει, γίνεται βαρύτερο και βυθίζεται, ώσπου όλη η λίμνη να φτάσει περίπου στους τέσσερις βαθμούς. Από εκεί και πέρα, το πιο κρύο νερό μένει στην επιφάνεια και παγώνει πρώτο.", "There's a second oddity: water has its greatest density not at zero, but at about four degrees Celsius. Think of a lake in winter. The surface water cools, becomes heavier and sinks, until the whole lake reaches about four degrees. From then on, the colder water stays at the surface and freezes first."),
  L("Χημικός", "f", "Το στρώμα του πάγου λειτουργεί σαν μονωτικό καπάκι, και στον βυθό το νερό παραμένει υγρό. Έτσι επιβιώνουν τα ψάρια και τα φυτά όλο τον χειμώνα. Αν ο πάγος βούλιαζε, πολλές λίμνες θα πάγωναν από κάτω προς τα πάνω, ίσως και ολόκληρες. Η ίδια ιδιότητα έχει όμως και μια λιγότερο ευχάριστη πλευρά: όταν το νερό παγώνει μέσα σε έναν σωλήνα, διαστέλλεται και μπορεί να τον σπάσει.", "The layer of ice works like an insulating lid, and at the bottom the water stays liquid. That's how fish and plants survive all winter. If ice sank, many lakes would freeze from the bottom up, perhaps completely. The same property also has a less pleasant side, though: when water freezes inside a pipe, it expands and can burst it."),
 ],
 "questions": [
  Q("Γιατί ο πάγος είναι λιγότερο πυκνός από το νερό;", ["Γιατί περιέχει αέρα από την ατμόσφαιρα", "Γιατί τα μόριά του σχηματίζουν ανοιχτό πλέγμα με περισσότερο κενό χώρο", "Γιατί είναι πιο κρύος", "Γιατί χάνει μόρια όταν παγώνει"], 1, "τα μόρια οργανώνονται σε ένα ανοιχτό εξαγωνικό πλέγμα"),
  Q("Σε ποια θερμοκρασία είναι πιο πυκνό το νερό;", ["Στους μηδέν βαθμούς", "Στους εκατό βαθμούς", "Περίπου στους τέσσερις βαθμούς Κελσίου", "Στους είκοσι βαθμούς"], 2, "περίπου στους τέσσερις βαθμούς Κελσίου"),
  Q("Πώς βοηθά ο πάγος τα ψάρια μιας λίμνης;", ["Λειτουργεί σαν μονωτικό καπάκι και το νερό στον βυθό μένει υγρό", "Τους δίνει τροφή", "Κρατά μακριά τα πουλιά", "Ζεσταίνει το νερό"], 0, "Το στρώμα του πάγου λειτουργεί σαν μονωτικό καπάκι"),
 ],
 "gloss": {"χημικό": "χημικός — chemist", "ιδιότητες": "ιδιότητα — property", "στερεοποιούνται": "στερεοποιούμαι — to solidify", "πυκνότερα": "πυκνός — dense", "βουλιάζει": "βουλιάζω — to sink", "επιπλέει": "επιπλέω — to float", "δεσμούς υδρογόνου": "δεσμός υδρογόνου — hydrogen bond", "εξαγωνικό": "εξαγωνικός — hexagonal", "πλέγμα": "πλέγμα — lattice", "παραξενιά": "παραξενιά — oddity", "πυκνότητά": "πυκνότητα — density", "βυθίζεται": "βυθίζομαι — to sink", "μονωτικό": "μονωτικός — insulating", "βυθό": "βυθός — bottom (of a lake/sea)", "διαστέλλεται": "διαστέλλομαι — to expand"},
})

rnd = random.Random(167)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-167.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
