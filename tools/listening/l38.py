# Source for library/listening/listening-38.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l38.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l38-ann-apergia", "title": "Απεργία στα πλοία", "title_en": "A ferry strike", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα του λιμανιού του Πειραιά.",
 "script": [
  L("Εκφωνητής", "m", "Προσοχή, παρακαλώ. Λόγω της εικοσιτετράωρης απεργίας των ναυτεργατών, όλα τα πλοία θα παραμείνουν δεμένα στο λιμάνι από τα μεσάνυχτα της Τετάρτης μέχρι τα μεσάνυχτα της Πέμπτης. Τα δρομολόγια προς τις Κυκλάδες, τα Δωδεκάνησα και την Κρήτη δεν θα πραγματοποιηθούν.", "Attention, please. Because of the twenty-four-hour seafarers' strike, all ships will remain moored in the port from midnight on Wednesday until midnight on Thursday. Sailings to the Cyclades, the Dodecanese and Crete will not take place."),
  L("Εκφωνητής", "m", "Τα εισιτήρια για την Πέμπτη ισχύουν χωρίς επιπλέον χρέωση για οποιοδήποτε δρομολόγιο της ίδιας εταιρείας μέσα στον επόμενο μήνα. Όσοι επιθυμούν επιστροφή χρημάτων μπορούν να απευθυνθούν στα πρακτορεία ή να υποβάλουν αίτηση στην ιστοσελίδα της εταιρείας τους.", "Tickets for Thursday are valid at no extra charge for any sailing of the same company within the next month. Those who wish to have their money refunded can go to the agencies or submit an application on their company's website."),
  L("Εκφωνητής", "m", "Τα πλοία της γραμμής του Αργοσαρωνικού θα εκτελέσουν κανονικά τα τελευταία δρομολόγια της Τετάρτης, με αναχώρηση έως τις δέκα το βράδυ. Οι επιβάτες με αυτοκίνητα παρακαλούνται να μην έρχονται στο λιμάνι χωρίς επιβεβαίωση, για να αποφευχθεί η συμφόρηση. Ευχαριστούμε για την κατανόηση.", "The ships on the Saronic Gulf line will run Wednesday's last sailings as normal, with departures until ten in the evening. Passengers with cars are asked not to come to the port without confirmation, to avoid congestion. Thank you for your understanding."),
 ],
 "questions": [
  Q("Γιατί δεν θα ταξιδέψουν τα πλοία την Πέμπτη;", ["Λόγω κακοκαιρίας", "Λόγω απεργίας των ναυτεργατών", "Λόγω βλάβης", "Λόγω αργίας"], 1, "Λόγω της εικοσιτετράωρης απεργίας των ναυτεργατών"),
  Q("Τι ισχύει για τα εισιτήρια της Πέμπτης;", ["Ακυρώνονται χωρίς επιστροφή", "Ισχύουν χωρίς χρέωση για άλλο δρομολόγιο μέσα σε έναν μήνα", "Ισχύουν μόνο για την Παρασκευή", "Μετατρέπονται σε εισιτήρια λεωφορείου"], 1, "Τα εισιτήρια για την Πέμπτη ισχύουν χωρίς επιπλέον χρέωση"),
  Q("Τι ζητείται από τους επιβάτες με αυτοκίνητα;", ["Να έρθουν νωρίς την Πέμπτη", "Να μην έρχονται στο λιμάνι χωρίς επιβεβαίωση", "Να αφήσουν τα αυτοκίνητα στο πάρκινγκ", "Να πάρουν άλλο λιμάνι"], 1, "να μην έρχονται στο λιμάνι χωρίς επιβεβαίωση"),
 ],
 "gloss": {"απεργίας": "απεργία — strike", "ναυτεργατών": "ναυτεργάτης — seafarer", "δεμένα": "δεμένος — moored, tied", "δρομολόγια": "δρομολόγιο — scheduled sailing", "δεν θα πραγματοποιηθούν": "πραγματοποιούμαι — to take place", "επιπλέον χρέωση": "επιπλέον χρέωση — extra charge", "επιστροφή χρημάτων": "επιστροφή χρημάτων — refund", "πρακτορεία": "πρακτορείο — (ticket) agency", "επιβεβαίωση": "επιβεβαίωση — confirmation", "συμφόρηση": "συμφόρηση — congestion"},
})

ITEMS.append({
 "id": "l38-vm-metakomisi", "title": "Μήνυμα από την εταιρεία μετακομίσεων", "title_en": "A message from the removal company", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από μια εταιρεία μετακομίσεων.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα σας, από την εταιρεία μετακομίσεων «Ερμής» σας τηλεφωνώ, για τη μετακόμισή σας το Σάββατο. Ο συνεργάτης μας που ήρθε για την εκτίμηση είπε ότι το πιάνο δεν χωράει στη σκάλα της καινούργιας πολυκατοικίας, οπότε θα χρειαστεί ανυψωτικό από το μπαλκόνι.", "Good morning, I'm calling from the «Hermes» removal company about your move on Saturday. Our colleague who came to make the estimate said the piano won't fit up the stairs of the new building, so we'll need a lift through the balcony."),
  L("Υπάλληλος", "m", "Αυτό σημαίνει ότι πρέπει να εκδοθεί άδεια από τον δήμο για να κλείσει μια λωρίδα του δρόμου για δύο ώρες. Μπορούμε να την αναλάβουμε εμείς, με μια επιπλέον χρέωση σαράντα ευρώ, ή να την κάνετε μόνος σας στο δημαρχείο. Η τελική τιμή, μαζί με το ανυψωτικό, ανεβαίνει στα εξακόσια είκοσι ευρώ.", "This means a permit must be issued by the municipality to close one lane of the road for two hours. We can take care of it, with an extra charge of forty euros, or you can do it yourself at the town hall. The final price, including the lift, goes up to six hundred and twenty euros."),
  L("Υπάλληλος", "m", "Επίσης, θα σας φέρουμε τα χαρτόκουτα την Τετάρτη το απόγευμα. Σας παρακαλώ να γράψετε σε κάθε κούτα σε ποιο δωμάτιο πηγαίνει, και να βάλετε τα εύθραυστα χωριστά. Περιμένω να μου επιβεβαιώσετε για την άδεια μέχρι αύριο. Ευχαριστώ.", "Also, we'll bring you the cardboard boxes on Wednesday afternoon. Please write on each box which room it goes to, and put the fragile items separately. I'll wait for you to confirm about the permit by tomorrow. Thank you."),
 ],
 "questions": [
  Q("Γιατί χρειάζεται ανυψωτικό;", ["Γιατί η πολυκατοικία δεν έχει ασανσέρ", "Γιατί το πιάνο δεν χωράει στη σκάλα", "Γιατί τα έπιπλα είναι πολλά", "Γιατί ο δρόμος είναι στενός"], 1, "το πιάνο δεν χωράει στη σκάλα"),
  Q("Γιατί χρειάζεται άδεια από τον δήμο;", ["Για να παρκάρει το φορτηγό στο πεζοδρόμιο", "Για να κλείσει μια λωρίδα του δρόμου για δύο ώρες", "Για να μεταφερθεί το πιάνο", "Για να δουλέψουν το Σάββατο"], 1, "για να κλείσει μια λωρίδα του δρόμου για δύο ώρες"),
  Q("Τι πρέπει να γράψει ο πελάτης σε κάθε κούτα;", ["Το όνομά του", "Σε ποιο δωμάτιο πηγαίνει", "Το βάρος της", "Την τιμή των αντικειμένων"], 1, "να γράψετε σε κάθε κούτα σε ποιο δωμάτιο πηγαίνει"),
 ],
 "gloss": {"μετακομίσεων": "μετακόμιση — move, removal", "εκτίμηση": "εκτίμηση — estimate", "δεν χωράει": "χωράω — to fit", "ανυψωτικό": "ανυψωτικό — lift, hoist", "να εκδοθεί": "εκδίδομαι — to be issued", "λωρίδα": "λωρίδα — lane", "δημαρχείο": "δημαρχείο — town hall", "χαρτόκουτα": "χαρτόκουτο — cardboard box", "εύθραυστα": "εύθραυστος — fragile"},
})

ITEMS.append({
 "id": "l38-dia-yiothesia", "title": "Υιοθεσία από το καταφύγιο ζώων", "title_en": "Adopting from an animal shelter", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα καταφύγιο αδέσποτων ζώων.",
 "script": [
  L("Επισκέπτρια", "f", "Καλημέρα. Θα θέλαμε να υιοθετήσουμε έναν σκύλο. Μένουμε σε διαμέρισμα, αλλά έχουμε μεγάλη βεράντα, και ο γιος μου είναι δέκα χρονών.", "Good morning. We'd like to adopt a dog. We live in a flat, but we have a big balcony, and my son is ten."),
  L("Εθελοντής", "m", "Πολύ ωραία. Για διαμέρισμα σας προτείνω έναν σκύλο μεσαίου μεγέθους και όχι πολύ νεαρό. Τα κουτάβια είναι γλυκά, αλλά χρειάζονται πολύ χρόνο και εκπαίδευση. Έχουμε, για παράδειγμα, τη Μέλι, τριών χρονών, πολύ ήρεμη και αγαπάει τα παιδιά. Τη βρήκαμε δεμένη σε ένα χωράφι.", "Very good. For a flat I'd suggest a medium-sized dog, and not a very young one. Puppies are sweet, but they need a lot of time and training. We have, for example, Meli, three years old, very calm, and she loves children. We found her tied up in a field."),
  L("Επισκέπτρια", "f", "Τι πρέπει να κάνουμε για να την πάρουμε;", "What do we have to do to take her?"),
  L("Εθελοντής", "m", "Πρώτα θα συμπληρώσετε ένα ερωτηματολόγιο, και μετά ένας εθελοντής θα έρθει να δει το σπίτι σας. Η Μέλι είναι ήδη στειρωμένη, εμβολιασμένη και έχει τσιπ, που θα το περάσουμε στο όνομά σας. Δεν υπάρχει κόστος, αλλά ζητάμε μια μικρή δωρεά, αν μπορείτε. Και σας προτείνουμε να έρθετε δυο τρεις φορές να τη βγάλετε βόλτα πριν την πάρετε, για να σας γνωρίσει.", "First you'll fill in a questionnaire, and then a volunteer will come to see your home. Meli is already spayed, vaccinated and has a microchip, which we'll transfer to your name. There's no cost, but we ask for a small donation if you can. And we suggest you come two or three times to take her for a walk before you take her, so that she gets to know you."),
 ],
 "questions": [
  Q("Γιατί ο εθελοντής δεν προτείνει κουτάβι;", ["Γιατί δεν έχουν κουτάβια", "Γιατί τα κουτάβια χρειάζονται πολύ χρόνο και εκπαίδευση", "Γιατί είναι ακριβά", "Γιατί δεν αγαπούν τα παιδιά"], 1, "χρειάζονται πολύ χρόνο και εκπαίδευση"),
  Q("Τι θα γίνει μετά το ερωτηματολόγιο;", ["Θα πληρώσουν ένα ποσό", "Ένας εθελοντής θα επισκεφθεί το σπίτι τους", "Θα πάρουν αμέσως τη Μέλι", "Θα πάνε σε κτηνίατρο"], 1, "ένας εθελοντής θα έρθει να δει το σπίτι σας"),
  Q("Τι προτείνει ο εθελοντής πριν από την υιοθεσία;", ["Να αγοράσουν κρεβάτι για τον σκύλο", "Να έρθουν μερικές φορές να βγάλουν βόλτα τη Μέλι", "Να κάνουν μαθήματα εκπαίδευσης", "Να ρωτήσουν τους γείτονες"], 1, "να έρθετε δυο τρεις φορές να τη βγάλετε βόλτα"),
 ],
 "gloss": {"καταφύγιο": "καταφύγιο — shelter", "αδέσποτων": "αδέσποτος — stray", "να υιοθετήσουμε": "υιοθετώ — to adopt", "μεσαίου μεγέθους": "μεσαίου μεγέθους — medium-sized", "κουτάβια": "κουτάβι — puppy", "εκπαίδευση": "εκπαίδευση — training", "ερωτηματολόγιο": "ερωτηματολόγιο — questionnaire", "στειρωμένη": "στειρωμένος — spayed, neutered", "εμβολιασμένη": "εμβολιασμένος — vaccinated", "τσιπ": "τσιπ — microchip", "δωρεά": "δωρεά — donation"},
})

ITEMS.append({
 "id": "l38-dia-taverna", "title": "Σε μια ταβέρνα με μια χορτοφάγο φίλη", "title_en": "At a taverna with a vegetarian friend", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε μια ταβέρνα ανάμεσα σε έναν σερβιτόρο και μια παρέα.",
 "script": [
  L("Σερβιτόρος", "m", "Καλησπέρα σας! Τι θα πάρετε; Σήμερα έχουμε φρέσκο ψάρι, τσιπούρες και μπαρμπούνια, και από τα μαγειρευτά κοκκινιστό με χυλοπίτες.", "Good evening! What will you have? Today we have fresh fish, sea bream and red mullet, and from the cooked dishes beef in tomato sauce with pasta."),
  L("Πελάτης", "m", "Η φίλη μου είναι χορτοφάγος, δεν τρώει ούτε κρέας ούτε ψάρι. Τι θα μπορούσατε να της προτείνετε;", "My friend is vegetarian; she doesn't eat meat or fish. What could you suggest for her?"),
  L("Σερβιτόρος", "m", "Πολλά! Η ελληνική κουζίνα έχει άπειρα λαδερά. Σήμερα έχουμε φασολάκια, γεμιστά και μπριάμ. Από τα ορεκτικά, φάβα με κάπαρη, χόρτα βραστά και κολοκυθοκεφτέδες. Μόνο προσοχή: τα γεμιστά μας έχουν λίγο κιμά, και οι κολοκυθοκεφτέδες έχουν φέτα και αυγό, αν δεν τρώει ούτε αυτά.", "Lots! Greek cuisine has countless dishes cooked in olive oil. Today we have green beans, stuffed vegetables and briam. From the starters, fava with capers, boiled greens and courgette fritters. Just one warning: our stuffed vegetables have a little mince, and the courgette fritters have feta and egg, in case she doesn't eat those either."),
  L("Χορτοφάγος", "f", "Τυρί και αυγά τρώω, ευτυχώς! Τότε θα πάρω τους κολοκυθοκεφτέδες, τη φάβα και το μπριάμ. Και για να μοιραστούμε, μια χωριάτικη χωρίς κρεμμύδι, αν γίνεται.", "Luckily I do eat cheese and eggs! Then I'll have the courgette fritters, the fava and the briam. And to share, a Greek salad without onion, if possible."),
 ],
 "questions": [
  Q("Τι δεν τρώει η φίλη του πελάτη;", ["Λαχανικά", "Κρέας και ψάρι", "Τυρί", "Ψωμί"], 1, "δεν τρώει ούτε κρέας ούτε ψάρι"),
  Q("Για ποιο φαγητό την προειδοποιεί ο σερβιτόρος;", ["Για τη φάβα, που έχει κάπαρη", "Για τα γεμιστά, που έχουν λίγο κιμά", "Για τα χόρτα, που είναι αλμυρά", "Για το μπριάμ, που είναι καυτερό"], 1, "τα γεμιστά μας έχουν λίγο κιμά"),
  Q("Τι ζητάει η χορτοφάγος για τη σαλάτα;", ["Επιπλέον φέτα", "Να μην έχει κρεμμύδι", "Να έχει λιγότερο λάδι", "Να έρθει πρώτη"], 1, "μια χωριάτικη χωρίς κρεμμύδι"),
 ],
 "gloss": {"ταβέρνα": "ταβέρνα — taverna", "χορτοφάγο": "χορτοφάγος — vegetarian", "τσιπούρες": "τσιπούρα — sea bream", "μπαρμπούνια": "μπαρμπούνι — red mullet", "μαγειρευτά": "μαγειρευτά — cooked dishes", "κοκκινιστό": "κοκκινιστό — meat in tomato sauce", "λαδερά": "λαδερά — dishes cooked in olive oil", "γεμιστά": "γεμιστά — stuffed vegetables", "κάπαρη": "κάπαρη — capers", "κολοκυθοκεφτέδες": "κολοκυθοκεφτές — courgette fritter", "κιμά": "κιμάς — mince", "να μοιραστούμε": "μοιράζομαι — to share"},
})

ITEMS.append({
 "id": "l38-mono-erhomos", "title": "Ο δρόμος από την Αλβανία", "title_en": "The road from Albania", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν άντρα να μιλάει για το πώς ήρθε στην Ελλάδα πριν από τριάντα χρόνια.",
 "script": [
  L("Αρμπέν", "m", "Ήρθα στην Ελλάδα τον χειμώνα του 1991, δεκαεννιά χρονών, με τα πόδια. Περπατήσαμε τρεις μέρες στα βουνά με άλλους πέντε από το χωριό μου, με λίγο ψωμί και τυρί στις τσέπες. Δεν ήξερα ούτε μία λέξη ελληνικά, εκτός από το «ευχαριστώ».", "I came to Greece in the winter of 1991, nineteen years old, on foot. We walked for three days in the mountains with five others from my village, with a little bread and cheese in our pockets. I didn't know a single word of Greek, except 'thank you'."),
  L("Αρμπέν", "m", "Τα πρώτα χρόνια δούλεψα σε χωράφια στη Θεσσαλία και μετά σε οικοδομές στην Αθήνα. Δεν ήταν εύκολα. Κάποιοι μας κοίταζαν με καχυποψία, και ήταν και αυτοί που δεν μας πλήρωναν. Αλλά βρήκα και ανθρώπους που με βοήθησαν πολύ. Ο πρώτος μου εργοδότης, ο κυρ Νίκος, μου έμαθε τη δουλειά του σοβατζή και με έβαλε να μένω στο σπίτι του τον πρώτο χειμώνα.", "The first years I worked in the fields in Thessaly and then on building sites in Athens. It wasn't easy. Some people looked at us with suspicion, and there were also those who didn't pay us. But I also found people who helped me a lot. My first employer, kyr Nikos, taught me the plasterer's trade and let me stay at his house the first winter."),
  L("Αρμπέν", "m", "Σήμερα έχω δική μου εταιρεία ανακαινίσεων και δώδεκα υπαλλήλους, Έλληνες και Αλβανούς. Η κόρη μου σπουδάζει ιατρική στη Θεσσαλονίκη. Όταν με ρωτάνε από πού είμαι, δεν ξέρω πια τι να απαντήσω. Είμαι από εκεί που γεννήθηκα και από εδώ που έζησα. Και τα δύο είναι αλήθεια.", "Today I have my own renovation company and twelve employees, Greeks and Albanians. My daughter is studying medicine in Thessaloniki. When people ask me where I'm from, I no longer know what to answer. I'm from where I was born and from here where I've lived. Both are true."),
 ],
 "questions": [
  Q("Πώς ήρθε ο Αρμπέν στην Ελλάδα;", ["Με λεωφορείο", "Με τα πόδια από τα βουνά", "Με πλοίο", "Με αεροπλάνο"], 1, "με τα πόδια. Περπατήσαμε τρεις μέρες στα βουνά"),
  Q("Τι λέει για τον κυρ Νίκο;", ["Ότι δεν τον πλήρωσε", "Ότι του έμαθε τη δουλειά και τον φιλοξένησε", "Ότι τον έστειλε πίσω", "Ότι ήταν συγγενής του"], 1, "μου έμαθε τη δουλειά του σοβατζή και με έβαλε να μένω στο σπίτι του"),
  Q("Τι απαντά σήμερα όταν τον ρωτούν από πού είναι;", ["Ότι είναι μόνο Αλβανός", "Ότι είναι και από τις δύο χώρες", "Ότι είναι μόνο Έλληνας", "Ότι δεν τον ενδιαφέρει"], 1, "Είμαι από εκεί που γεννήθηκα και από εδώ που έζησα"),
 ],
 "gloss": {"χωράφια": "χωράφι — field", "οικοδομές": "οικοδομή — building site", "καχυποψία": "καχυποψία — suspicion", "εργοδότης": "εργοδότης — employer", "σοβατζή": "σοβατζής — plasterer", "ανακαινίσεων": "ανακαίνιση — renovation", "υπαλλήλους": "υπάλληλος — employee", "ιατρική": "ιατρική — medicine"},
})

ITEMS.append({
 "id": "l38-rep-soufli", "title": "Το μετάξι του Σουφλίου", "title_en": "The silk of Soufli", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από το Σουφλί, μια μικρή πόλη του Έβρου.",
 "script": [
  L("Δημοσιογράφος", "f", "Στα τέλη του 19ου και στις αρχές του 20ού αιώνα, το Σουφλί ήταν ένα από τα σημαντικότερα κέντρα παραγωγής μεταξιού στα Βαλκάνια. Σχεδόν κάθε οικογένεια έτρεφε μεταξοσκώληκες στο πάνω πάτωμα του σπιτιού της, και τα πλούσια αρχοντικά της πόλης χτίστηκαν με τα κέρδη από το μετάξι.", "In the late 19th and early 20th century, Soufli was one of the most important centres of silk production in the Balkans. Almost every family raised silkworms on the upper floor of its house, and the town's rich mansions were built with the profits from silk."),
  L("Μουσειολόγος", "m", "Οι μεταξοσκώληκες τρέφονται μόνο με φύλλα μουριάς, γι' αυτό γύρω από την πόλη υπήρχαν χιλιάδες μουριές. Μέσα σε έναν περίπου μήνα, κάθε σκουλήκι τυλίγεται σε ένα κουκούλι από μια ενιαία κλωστή, μήκους πάνω από ένα χιλιόμετρο. Μετά τον πόλεμο, με την εμφάνιση των συνθετικών ινών, η παραγωγή παρήκμασε σχεδόν εντελώς.", "Silkworms feed only on mulberry leaves, which is why there were thousands of mulberry trees around the town. In about a month, each worm wraps itself in a cocoon made of a single thread more than a kilometre long. After the war, with the appearance of synthetic fibres, production declined almost completely."),
  L("Δημοσιογράφος", "f", "Σήμερα το Μουσείο Μεταξιού, σε ένα αναπαλαιωμένο αρχοντικό, αφηγείται αυτή την ιστορία, ενώ λίγες επιχειρήσεις συνεχίζουν να υφαίνουν μεταξωτά μαντίλια και γραβάτες. Μερικοί νέοι παραγωγοί προσπαθούν μάλιστα να αναβιώσουν την καλλιέργεια, πιστεύοντας ότι το φυσικό, τοπικό μετάξι μπορεί να βρει ξανά τη θέση του στην αγορά.", "Today the Silk Museum, in a restored mansion, tells this story, while a few businesses continue to weave silk scarves and ties. Some young producers are even trying to revive sericulture, believing that natural, local silk can find its place in the market again."),
 ],
 "questions": [
  Q("Πού έτρεφαν οι οικογένειες τους μεταξοσκώληκες;", ["Σε ειδικά εργοστάσια", "Στο πάνω πάτωμα των σπιτιών τους", "Στα χωράφια", "Στις εκκλησίες"], 1, "έτρεφε μεταξοσκώληκες στο πάνω πάτωμα του σπιτιού της"),
  Q("Γιατί υπήρχαν χιλιάδες μουριές γύρω από την πόλη;", ["Για τα φρούτα τους", "Γιατί οι μεταξοσκώληκες τρώνε μόνο φύλλα μουριάς", "Για τη σκιά", "Για το ξύλο τους"], 1, "Οι μεταξοσκώληκες τρέφονται μόνο με φύλλα μουριάς"),
  Q("Γιατί παρήκμασε η παραγωγή μεταξιού;", ["Λόγω μιας αρρώστιας των δέντρων", "Λόγω της εμφάνισης των συνθετικών ινών", "Γιατί οι κάτοικοι μετανάστευσαν", "Γιατί απαγορεύτηκε"], 1, "με την εμφάνιση των συνθετικών ινών, η παραγωγή παρήκμασε"),
 ],
 "gloss": {"μεταξιού": "μετάξι — silk", "Έβρου": "Έβρος — Evros (region, river)", "έτρεφε": "τρέφω — to raise, feed", "μεταξοσκώληκες": "μεταξοσκώληκας — silkworm", "αρχοντικά": "αρχοντικό — mansion", "μουριάς": "μουριά — mulberry tree", "κουκούλι": "κουκούλι — cocoon", "κλωστή": "κλωστή — thread", "συνθετικών ινών": "συνθετική ίνα — synthetic fibre", "παρήκμασε": "παρακμάζω — to decline", "αναπαλαιωμένο": "αναπαλαιωμένος — restored", "να υφαίνουν": "υφαίνω — to weave", "να αναβιώσουν": "αναβιώνω — to revive"},
})

ITEMS.append({
 "id": "l38-rep-tsai-vounou", "title": "Το τσάι του βουνού", "title_en": "Mountain tea", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από τον Ταΰγετο την εποχή της συλλογής του τσαγιού του βουνού.",
 "script": [
  L("Δημοσιογράφος", "m", "Είναι αρχές Ιουλίου, και στις πλαγιές του Ταΰγετου, πάνω από τα χίλια μέτρα, μια ομάδα συλλεκτών κόβει με προσοχή τα ανθισμένα κλαδάκια του σιδερίτη, του φυτού που οι Έλληνες ονομάζουν «τσάι του βουνού». Ο αέρας μυρίζει ρίγανη και θυμάρι.", "It's early July, and on the slopes of Taygetos, above a thousand metres, a group of gatherers is carefully cutting the flowering sprigs of sideritis, the plant Greeks call 'mountain tea'. The air smells of oregano and thyme."),
  L("Συλλέκτρια", "f", "Τα κόβουμε με ψαλίδι, ποτέ δεν τα ξεριζώνουμε, για να ξαναβγούν του χρόνου. Παλιά τα μαζεύαμε μόνο για το σπίτι· η γιαγιά μου το έδινε για κάθε κρύωμα και για τον πονόκοιλο. Τώρα πολλοί το καλλιεργούν σε χωράφια, γιατί η ζήτηση έχει μεγαλώσει, και η άγρια συλλογή απαγορεύεται σε πολλές περιοχές.", "We cut them with scissors, we never pull them up, so that they grow back next year. In the old days we gathered it only for the house; my grandmother gave it for every cold and for stomach ache. Now many people cultivate it in fields, because demand has grown, and wild gathering is banned in many areas."),
  L("Δημοσιογράφος", "m", "Η επιστημονική έρευνα έχει δείξει ότι ο σιδερίτης περιέχει αντιοξειδωτικές ουσίες, και η ζήτηση από το εξωτερικό, ιδίως από τη Γερμανία, αυξάνεται συνεχώς. Οι παραγωγοί ελπίζουν ότι το ταπεινό αυτό βότανο θα δώσει μια νέα πνοή στα ορεινά χωριά, που έχουν ερημώσει τις τελευταίες δεκαετίες.", "Scientific research has shown that sideritis contains antioxidant substances, and demand from abroad, especially from Germany, is constantly increasing. Producers hope that this humble herb will breathe new life into the mountain villages, which have been deserted in recent decades."),
 ],
 "questions": [
  Q("Γιατί οι συλλέκτες κόβουν τα φυτά και δεν τα ξεριζώνουν;", ["Για να είναι πιο αρωματικά", "Για να ξαναβγούν του χρόνου", "Γιατί είναι πιο γρήγορο", "Γιατί το απαιτεί ο αγοραστής"], 1, "ποτέ δεν τα ξεριζώνουμε, για να ξαναβγούν του χρόνου"),
  Q("Γιατί πολλοί καλλιεργούν σήμερα τσάι του βουνού σε χωράφια;", ["Γιατί είναι πιο νόστιμο", "Γιατί η ζήτηση μεγάλωσε και η άγρια συλλογή απαγορεύεται σε πολλές περιοχές", "Γιατί τα βουνά κάηκαν", "Γιατί το επιδοτεί η ΕΕ"], 1, "η ζήτηση έχει μεγαλώσει, και η άγρια συλλογή απαγορεύεται σε πολλές περιοχές"),
  Q("Τι ελπίζουν οι παραγωγοί;", ["Να το πουλήσουν στα σούπερ μάρκετ", "Να δώσει νέα πνοή στα ορεινά χωριά", "Να γίνει φάρμακο", "Να ανοίξουν εργοστάσιο"], 1, "θα δώσει μια νέα πνοή στα ορεινά χωριά"),
 ],
 "gloss": {"τσαγιού του βουνού": "τσάι του βουνού — mountain tea", "Ταΰγετο": "Ταΰγετος — Taygetos (mountain)", "συλλεκτών": "συλλέκτης — gatherer", "ανθισμένα": "ανθισμένος — flowering", "σιδερίτη": "σιδερίτης — sideritis (ironwort)", "ρίγανη": "ρίγανη — oregano", "θυμάρι": "θυμάρι — thyme", "ξεριζώνουμε": "ξεριζώνω — to uproot", "πονόκοιλο": "πονόκοιλος — stomach ache", "αντιοξειδωτικές": "αντιοξειδωτικός — antioxidant", "βότανο": "βότανο — herb", "πνοή": "πνοή — breath", "έχουν ερημώσει": "ερημώνω — to become deserted"},
})

ITEMS.append({
 "id": "l38-int-oinochoos", "title": "Μια οινοχόος", "title_en": "A sommelier", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια οινοχόο που εργάζεται σε ένα εστιατόριο της Αθήνας.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί πιστεύουν ότι η δουλειά σας είναι απλώς να ανοίγετε μπουκάλια. Τι κάνει πραγματικά ένας οινοχόος;", "Many people think your job is simply opening bottles. What does a sommelier really do?"),
  L("Οινοχόος", "f", "Το πιο σημαντικό είναι να ακούω. Ένας πελάτης σπάνια ξέρει να περιγράψει τι κρασί θέλει, αλλά αν τον ρωτήσεις τι του αρέσει να τρώει, αν προτιμά το γλυκό ή το ξινό, αν θέλει κάτι ελαφρύ για το καλοκαίρι, μπορείς να βρεις το κατάλληλο μπουκάλι. Δεν είναι θέμα τιμής. Συχνά ένα κρασί των δεκαπέντε ευρώ ταιριάζει καλύτερα με ένα πιάτο από ένα των εκατό.", "The most important thing is to listen. A customer rarely knows how to describe the wine they want, but if you ask them what they like to eat, whether they prefer sweet or sour, whether they want something light for summer, you can find the right bottle. It's not a question of price. Often a fifteen-euro wine goes better with a dish than a hundred-euro one."),
  L("Δημοσιογράφος", "m", "Οι ελληνικές ποικιλίες έχουν γίνει γνωστές στο εξωτερικό;", "Have Greek grape varieties become known abroad?"),
  L("Οινοχόος", "f", "Πολύ περισσότερο από πριν. Το Ασύρτικο της Σαντορίνης το βρίσκεις σήμερα σε εστιατόρια της Νέας Υόρκης και του Λονδίνου. Το μεγάλο μας πλεονέκτημα είναι ότι έχουμε πάνω από διακόσιες γηγενείς ποικιλίες, που δεν υπάρχουν πουθενά αλλού. Το μειονέκτημα είναι τα ονόματα: ο ξένος πελάτης δυσκολεύεται να προφέρει «Ξινόμαυρο» ή «Μαλαγουζιά». Γι' αυτό, πριν από τη γεύση, πουλάμε την ιστορία.", "Much more than before. You find Santorini's Assyrtiko today in restaurants in New York and London. Our great advantage is that we have more than two hundred native varieties that don't exist anywhere else. The disadvantage is the names: foreign customers struggle to pronounce 'Xinomavro' or 'Malagousia'. So, before the taste, we sell the story."),
 ],
 "questions": [
  Q("Ποιο είναι, κατά την οινοχόο, το πιο σημαντικό μέρος της δουλειάς της;", ["Να ανοίγει τα μπουκάλια σωστά", "Να ακούει τον πελάτη", "Να προτείνει ακριβά κρασιά", "Να ξέρει τις τιμές"], 1, "Το πιο σημαντικό είναι να ακούω"),
  Q("Τι λέει για την τιμή του κρασιού;", ["Τα ακριβά κρασιά ταιριάζουν πάντα καλύτερα", "Ένα φθηνότερο κρασί μπορεί να ταιριάζει καλύτερα με ένα πιάτο", "Οι πελάτες προτιμούν τα ακριβά", "Η τιμή δείχνει την ποιότητα"], 1, "Συχνά ένα κρασί των δεκαπέντε ευρώ ταιριάζει καλύτερα"),
  Q("Ποιο είναι το μειονέκτημα των ελληνικών ποικιλιών στο εξωτερικό;", ["Η υψηλή τιμή", "Τα δύσκολα ονόματα", "Η μικρή παραγωγή", "Η κακή ποιότητα"], 1, "Το μειονέκτημα είναι τα ονόματα"),
 ],
 "gloss": {"οινοχόο": "οινοχόος — sommelier", "μπουκάλια": "μπουκάλι — bottle", "ξινό": "ξινός — sour", "ελαφρύ": "ελαφρύς — light", "ποικιλίες": "ποικιλία — (grape) variety", "πλεονέκτημα": "πλεονέκτημα — advantage", "γηγενείς": "γηγενής — native, indigenous", "μειονέκτημα": "μειονέκτημα — disadvantage", "να προφέρει": "προφέρω — to pronounce", "γεύση": "γεύση — taste"},
})

ITEMS.append({
 "id": "l38-mono-antallagi", "title": "Η ανταλλαγή των πληθυσμών", "title_en": "The population exchange", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια ιστορικό να μιλάει σε μια διάλεξη για την ανταλλαγή πληθυσμών ανάμεσα στην Ελλάδα και την Τουρκία.",
 "script": [
  L("Ιστορικός", "f", "Τον Σεπτέμβριο του 1922, με την κατάρρευση του μετώπου στη Μικρά Ασία και την καταστροφή της Σμύρνης, εκατοντάδες χιλιάδες Έλληνες ορθόδοξοι εγκατέλειψαν βιαστικά τις εστίες τους. Λίγους μήνες αργότερα, τον Ιανουάριο του 1923, η Ελλάδα και η Τουρκία υπέγραψαν στη Λωζάνη μια σύμβαση για την υποχρεωτική ανταλλαγή των πληθυσμών τους.", "In September 1922, with the collapse of the front in Asia Minor and the destruction of Smyrna, hundreds of thousands of Orthodox Greeks hastily abandoned their homes. A few months later, in January 1923, Greece and Turkey signed in Lausanne a convention for the compulsory exchange of their populations."),
  L("Ιστορικός", "f", "Το κριτήριο της ανταλλαγής δεν ήταν η γλώσσα ή η εθνική συνείδηση, αλλά η θρησκεία. Έτσι, τουρκόφωνοι ορθόδοξοι της Καππαδοκίας εστάλησαν στην Ελλάδα, ενώ ελληνόφωνοι μουσουλμάνοι της Κρήτης στην Τουρκία. Συνολικά, περίπου ένα εκατομμύριο διακόσιες χιλιάδες άνθρωποι ήρθαν στην Ελλάδα και περίπου τετρακόσιες χιλιάδες έφυγαν προς την αντίθετη κατεύθυνση. Οι μουσουλμάνοι της Δυτικής Θράκης και οι Έλληνες της Κωνσταντινούπολης εξαιρέθηκαν.", "The criterion for the exchange was not language or national consciousness, but religion. Thus Turkish-speaking Orthodox Christians of Cappadocia were sent to Greece, while Greek-speaking Muslims of Crete were sent to Turkey. In total, about one million two hundred thousand people came to Greece and about four hundred thousand left in the opposite direction. The Muslims of Western Thrace and the Greeks of Constantinople were exempted."),
  L("Ιστορικός", "f", "Για μια χώρα πέντε περίπου εκατομμυρίων, η άφιξη των προσφύγων ήταν τεράστιο σοκ. Πολλοί έζησαν για χρόνια σε παραπήγματα, αντιμετωπίστηκαν με καχυποψία και αποκαλούνταν υποτιμητικά «τουρκόσποροι». Ωστόσο, μακροπρόθεσμα, οι πρόσφυγες μεταμόρφωσαν την Ελλάδα: έδωσαν ώθηση στη γεωργία της Μακεδονίας, στη βιομηχανία, στη μουσική, με το ρεμπέτικο, και έφτιαξαν ολόκληρες συνοικίες, όπως η Νέα Σμύρνη και η Νέα Ιωνία.", "For a country of about five million, the arrival of the refugees was an enormous shock. Many lived for years in shacks, were treated with suspicion and were disparagingly called 'Turkish seed'. Yet in the long term the refugees transformed Greece: they gave a boost to Macedonian agriculture, to industry, to music with rebetiko, and they built whole districts, such as Nea Smyrni and Nea Ionia."),
  L("Ιστορικός", "f", "Η ανταλλαγή αποτέλεσε την πρώτη μαζική, διεθνώς νομιμοποιημένη μετακίνηση πληθυσμών του 20ού αιώνα, και χρησιμοποιήθηκε αργότερα ως πρότυπο σε άλλες περιοχές του κόσμου, με συχνά τραγικές συνέπειες. Αυτό μας υποχρεώνει να τη μελετάμε όχι μόνο ως εθνική ιστορία, αλλά και ως προειδοποίηση.", "The exchange was the first mass, internationally legitimised population transfer of the 20th century, and was later used as a model in other parts of the world, often with tragic consequences. This obliges us to study it not only as national history, but also as a warning."),
 ],
 "questions": [
  Q("Ποιο ήταν το κριτήριο της ανταλλαγής;", ["Η γλώσσα", "Η θρησκεία", "Ο τόπος γέννησης", "Η εθνική συνείδηση"], 1, "Το κριτήριο της ανταλλαγής δεν ήταν η γλώσσα ή η εθνική συνείδηση, αλλά η θρησκεία"),
  Q("Ποιοι εξαιρέθηκαν από την ανταλλαγή;", ["Οι ορθόδοξοι της Καππαδοκίας", "Οι μουσουλμάνοι της Δυτικής Θράκης και οι Έλληνες της Κωνσταντινούπολης", "Οι μουσουλμάνοι της Κρήτης", "Όλοι οι ελληνόφωνοι"], 1, "Οι μουσουλμάνοι της Δυτικής Θράκης και οι Έλληνες της Κωνσταντινούπολης εξαιρέθηκαν"),
  Q("Πώς αντιμετωπίστηκαν αρχικά οι πρόσφυγες;", ["Με ενθουσιασμό", "Συχνά με καχυποψία, και ζούσαν σε παραπήγματα", "Με μεγάλες κρατικές αποζημιώσεις", "Τους δόθηκαν αμέσως σπίτια"], 1, "Πολλοί έζησαν για χρόνια σε παραπήγματα, αντιμετωπίστηκαν με καχυποψία"),
  Q("Γιατί, κατά την ομιλήτρια, πρέπει να μελετάμε την ανταλλαγή και «ως προειδοποίηση»;", ["Γιατί μπορεί να επαναληφθεί στην Ελλάδα", "Γιατί χρησιμοποιήθηκε ως πρότυπο αλλού, με τραγικές συνέπειες", "Γιατί οι πρόσφυγες δεν ενσωματώθηκαν ποτέ", "Γιατί η σύμβαση ήταν παράνομη"], 1, "χρησιμοποιήθηκε αργότερα ως πρότυπο σε άλλες περιοχές του κόσμου, με συχνά τραγικές συνέπειες"),
 ],
 "gloss": {"ανταλλαγή": "ανταλλαγή — exchange", "πληθυσμών": "πληθυσμός — population", "κατάρρευση": "κατάρρευση — collapse", "μετώπου": "μέτωπο — front", "εστίες": "εστία — hearth, home", "σύμβαση": "σύμβαση — convention, treaty", "υποχρεωτική": "υποχρεωτικός — compulsory", "κριτήριο": "κριτήριο — criterion", "εθνική συνείδηση": "εθνική συνείδηση — national consciousness", "εξαιρέθηκαν": "εξαιρούμαι — to be exempted", "προσφύγων": "πρόσφυγας — refugee", "παραπήγματα": "παράπηγμα — shack", "υποτιμητικά": "υποτιμητικά — disparagingly", "ώθηση": "ώθηση — boost", "νομιμοποιημένη": "νομιμοποιημένος — legitimised"},
})

ITEMS.append({
 "id": "l38-int-crispr", "title": "Επεμβαίνοντας στα γονίδια", "title_en": "Editing genes", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια μοριακή βιολόγο για τη γονιδιακή επεξεργασία και τα ηθικά της διλήμματα.",
 "script": [
  L("Δημοσιογράφος", "m", "Το 2020 το Βραβείο Νόμπελ Χημείας δόθηκε σε δύο ερευνήτριες για την τεχνική CRISPR. Τι ακριβώς κάνει αυτή η τεχνική;", "In 2020 the Nobel Prize in Chemistry was awarded to two researchers for the CRISPR technique. What exactly does this technique do?"),
  L("Βιολόγος", "f", "Με απλά λόγια, είναι ένα μοριακό «ψαλίδι» που μπορεί να κόψει το DNA σε ένα πολύ συγκεκριμένο σημείο, ώστε να απενεργοποιήσουμε, να διορθώσουμε ή να αντικαταστήσουμε ένα γονίδιο. Η επεξεργασία γονιδίων δεν είναι καινούργια ιδέα, αλλά πριν από το CRISPR ήταν πολύ πιο δύσκολη, αργή και ακριβή. Τώρα μπορεί να γίνει σε σχεδόν οποιοδήποτε εργαστήριο.", "In simple terms, it's a molecular 'pair of scissors' that can cut DNA at a very specific point, so that we can deactivate, correct or replace a gene. Gene editing isn't a new idea, but before CRISPR it was much more difficult, slow and expensive. Now it can be done in almost any laboratory."),
  L("Δημοσιογράφος", "m", "Υπάρχουν ήδη θεραπείες που τη χρησιμοποιούν;", "Are there already treatments that use it?"),
  L("Βιολόγος", "f", "Ναι. Από το 2023 έχει εγκριθεί σε αρκετές χώρες η πρώτη θεραπεία για τη δρεπανοκυτταρική αναιμία και τη μεσογειακή αναιμία, που είναι, όπως ξέρετε, συχνή στην Ελλάδα. Λαμβάνονται κύτταρα από τον μυελό των οστών του ασθενούς, τροποποιούνται στο εργαστήριο και επιστρέφονται στον οργανισμό. Τα αποτελέσματα είναι εντυπωσιακά, αλλά το κόστος είναι προς το παρόν τεράστιο.", "Yes. Since 2023 the first treatment for sickle-cell anaemia and thalassaemia, which is, as you know, common in Greece, has been approved in several countries. Cells are taken from the patient's bone marrow, modified in the laboratory and returned to the body. The results are impressive, but the cost is enormous for now."),
  L("Δημοσιογράφος", "m", "Και τα ηθικά ζητήματα;", "And the ethical questions?"),
  L("Βιολόγος", "f", "Εδώ πρέπει να κάνουμε μια κρίσιμη διάκριση. Άλλο είναι να τροποποιείς τα κύτταρα ενός ενήλικα ασθενούς, οπότε οι αλλαγές αφορούν μόνο εκείνον, και άλλο να επεμβαίνεις σε έμβρυα, οπότε οι αλλαγές περνούν στις επόμενες γενιές. Το 2018 ένας Κινέζος ερευνητής ανακοίνωσε τη γέννηση δύο παιδιών με τροποποιημένα γονίδια, και η επιστημονική κοινότητα αντέδρασε με οργή. Δεν είναι μόνο ότι δεν γνωρίζουμε τις μακροπρόθεσμες συνέπειες. Είναι και ο κίνδυνος να ανοίξει ο δρόμος για «παιδιά κατά παραγγελία», προνόμιο όσων μπορούν να πληρώσουν.", "Here we need to make a crucial distinction. It's one thing to modify the cells of an adult patient, so that the changes concern only them, and another to intervene in embryos, so that the changes pass on to the next generations. In 2018 a Chinese researcher announced the birth of two children with edited genes, and the scientific community reacted with outrage. It isn't only that we don't know the long-term consequences. There's also the risk of opening the way to 'designer babies', a privilege for those who can pay."),
 ],
 "questions": [
  Q("Τι έκανε το CRISPR διαφορετικό από τις προηγούμενες μεθόδους;", ["Ότι είναι η πρώτη μέθοδος επεξεργασίας γονιδίων", "Ότι είναι πολύ πιο εύκολο, γρήγορο και φθηνό", "Ότι δεν χρειάζεται εργαστήριο", "Ότι δεν κόβει το DNA"], 1, "πριν από το CRISPR ήταν πολύ πιο δύσκολη, αργή και ακριβή"),
  Q("Πώς λειτουργεί η θεραπεία για τη μεσογειακή αναιμία;", ["Με ένα χάπι", "Τα κύτταρα του μυελού τροποποιούνται στο εργαστήριο και επιστρέφονται στον ασθενή", "Με μετάγγιση αίματος από δότη", "Με εμβόλιο"], 1, "Λαμβάνονται κύτταρα από τον μυελό των οστών του ασθενούς, τροποποιούνται στο εργαστήριο"),
  Q("Ποια διάκριση θεωρεί κρίσιμη η βιολόγος;", ["Ανάμεσα σε φυτά και ζώα", "Ανάμεσα σε αλλαγές σε ενήλικο ασθενή και σε έμβρυα", "Ανάμεσα σε φθηνές και ακριβές θεραπείες", "Ανάμεσα σε Ευρώπη και Κίνα"], 1, "Άλλο είναι να τροποποιείς τα κύτταρα ενός ενήλικα ασθενούς ... και άλλο να επεμβαίνεις σε έμβρυα"),
  Q("Ποιον κίνδυνο αναφέρει εκτός από τις άγνωστες συνέπειες;", ["Να κλείσουν τα εργαστήρια", "Να γίνουν τα «παιδιά κατά παραγγελία» προνόμιο των πλουσίων", "Να απαγορευτεί κάθε έρευνα", "Να αυξηθούν οι ασθένειες"], 1, "ο κίνδυνος να ανοίξει ο δρόμος για «παιδιά κατά παραγγελία», προνόμιο όσων μπορούν να πληρώσουν"),
 ],
 "gloss": {"μοριακή": "μοριακός — molecular", "γονιδιακή επεξεργασία": "γονιδιακή επεξεργασία — gene editing", "διλήμματα": "δίλημμα — dilemma", "να απενεργοποιήσουμε": "απενεργοποιώ — to deactivate", "έχει εγκριθεί": "εγκρίνομαι — to be approved", "δρεπανοκυτταρική αναιμία": "δρεπανοκυτταρική αναιμία — sickle-cell anaemia", "μεσογειακή αναιμία": "μεσογειακή αναιμία — thalassaemia", "μυελό των οστών": "μυελός των οστών — bone marrow", "τροποποιούνται": "τροποποιούμαι — to be modified", "διάκριση": "διάκριση — distinction", "έμβρυα": "έμβρυο — embryo", "οργή": "οργή — outrage, anger", "κατά παραγγελία": "κατά παραγγελία — made to order"},
})

rnd = random.Random(38)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-38.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
