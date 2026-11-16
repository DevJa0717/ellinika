# Source for library/listening/listening-26.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l26.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l26-ann-souper", "title": "Ένα παιδί ψάχνει τους γονείς του", "title_en": "A child is looking for their parents", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα ενός μεγάλου σούπερ μάρκετ.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί πελάτες, σας παρακαλούμε για λίγη προσοχή. Στο γραφείο εξυπηρέτησης πελατών, δίπλα στην κεντρική είσοδο, βρίσκεται ένα κοριτσάκι περίπου πέντε ετών, που λέγεται Δανάη. Φοράει κόκκινο φόρεμα και κρατάει ένα λούτρινο λαγουδάκι.", "Dear customers, may we have your attention for a moment. At the customer service desk, next to the main entrance, there is a little girl of about five, called Danai. She is wearing a red dress and holding a soft toy rabbit."),
  L("Εκφωνήτρια", "f", "Η μικρή μάς είπε ότι ήρθε με τη γιαγιά της και ότι χάθηκαν κοντά στα ψυγεία με τα γαλακτοκομικά. Παρακαλείται η συνοδός της να προσέλθει αμέσως στο γραφείο εξυπηρέτησης. Η Δανάη είναι ασφαλής και την προσέχει μια υπάλληλός μας.", "The little one told us that she came with her grandmother and that they lost each other near the dairy fridges. Her companion is asked to come to the customer service desk immediately. Danai is safe and one of our staff is looking after her."),
  L("Εκφωνήτρια", "f", "Υπενθυμίζουμε επίσης ότι, για λόγους ασφαλείας, οι έξοδοι του καταστήματος παρακολουθούνται από το προσωπικό μας μέχρι να βρεθεί η συνοδός. Ευχαριστούμε για την κατανόηση.", "We would also remind you that, for safety reasons, the store's exits are being watched by our staff until the companion is found. Thank you for your understanding."),
 ],
 "questions": [
  Q("Πού βρίσκεται τώρα το παιδί;", ["Στο ταμείο", "Στο γραφείο εξυπηρέτησης πελατών", "Στα ψυγεία με τα γαλακτοκομικά", "Στο πάρκινγκ"], 1, "Στο γραφείο εξυπηρέτησης πελατών, δίπλα στην κεντρική είσοδο"),
  Q("Με ποιον είχε έρθει η Δανάη;", ["Με τη μητέρα της", "Με τη γιαγιά της", "Με τον πατέρα της", "Με τη δασκάλα της"], 1, "ήρθε με τη γιαγιά της"),
  Q("Τι κάνει το προσωπικό μέχρι να βρεθεί η συνοδός;", ["Κλείνει το κατάστημα", "Παρακολουθεί τις εξόδους", "Καλεί την αστυνομία", "Ψάχνει στους διαδρόμους με το παιδί"], 1, "οι έξοδοι του καταστήματος παρακολουθούνται από το προσωπικό μας"),
 ],
 "gloss": {"μεγάφωνα": "μεγάφωνο — loudspeaker", "γραφείο εξυπηρέτησης πελατών": "γραφείο εξυπηρέτησης πελατών — customer service desk", "λούτρινο": "λούτρινος — plush, soft (toy)", "γαλακτοκομικά": "γαλακτοκομικά — dairy products", "συνοδός": "συνοδός — companion, escort", "να προσέλθει": "προσέρχομαι — to come forward, present oneself", "ασφαλής": "ασφαλής — safe", "παρακολουθούνται": "παρακολουθούμαι — to be watched, monitored", "κατανόηση": "κατανόηση — understanding"},
})

ITEMS.append({
 "id": "l26-vm-gymnastis", "title": "Μήνυμα από τον γυμναστή", "title_en": "A message from the personal trainer", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τον προσωπικό σας γυμναστή.",
 "script": [
  L("Γυμναστής", "m", "Γεια σου, Ελπίδα, ο Στέλιος είμαι, από το γυμναστήριο. Σε παίρνω για την αυριανή προπόνηση. Δυστυχώς έχω ένα πρόβλημα με τον αστράγαλο, τον στραμπούληξα στο ποδόσφαιρο, και ο γιατρός μού είπε να μην πατάω για μερικές μέρες.", "Hi Elpida, it's Stelios, from the gym. I'm calling about tomorrow's training session. Unfortunately I have a problem with my ankle, I sprained it playing football, and the doctor told me not to put weight on it for a few days."),
  L("Γυμναστής", "m", "Δεν θέλω όμως να χάσεις τον ρυθμό σου, τώρα που πας τόσο καλά. Η συνάδελφός μου, η Ναταλία, μπορεί να σε δει αύριο στην ίδια ώρα. Της έχω ήδη στείλει το πρόγραμμά σου, οπότε ξέρει ακριβώς τι ασκήσεις κάνουμε και πού έχουμε μείνει.", "But I don't want you to lose your rhythm, now that you're doing so well. My colleague Natalia can see you tomorrow at the same time. I've already sent her your programme, so she knows exactly which exercises we do and where we've got to."),
  L("Γυμναστής", "m", "Αν προτιμάς να περιμένεις εμένα, κανένα πρόβλημα· θα αναπληρώσουμε τη χαμένη προπόνηση την άλλη εβδομάδα, χωρίς χρέωση. Στείλε μου μόνο ένα μήνυμα μέχρι απόψε να ξέρω τι να πω στη Ναταλία.", "If you'd rather wait for me, no problem; we'll make up the missed session next week, free of charge. Just send me a message by tonight so I know what to tell Natalia."),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί να κάνει την προπόνηση ο Στέλιος;", ["Γιατί έχει γρίπη", "Γιατί στραμπούληξε τον αστράγαλό του", "Γιατί έχει άλλο ραντεβού", "Γιατί το γυμναστήριο κλείνει"], 1, "τον στραμπούληξα στο ποδόσφαιρο"),
  Q("Τι ξέρει ήδη η Ναταλία;", ["Το τηλέφωνο της Ελπίδας", "Το πρόγραμμα των ασκήσεων της Ελπίδας", "Ότι η Ελπίδα θα ακυρώσει", "Τίποτα"], 1, "Της έχω ήδη στείλει το πρόγραμμά σου"),
  Q("Τι θα γίνει αν η Ελπίδα προτιμήσει να περιμένει τον Στέλιο;", ["Θα πληρώσει κανονικά την προπόνηση", "Θα κάνουν την προπόνηση την άλλη εβδομάδα χωρίς χρέωση", "Θα χάσει την προπόνηση", "Θα αλλάξει γυμναστήριο"], 1, "θα αναπληρώσουμε τη χαμένη προπόνηση την άλλη εβδομάδα, χωρίς χρέωση"),
 ],
 "gloss": {"γυμναστή": "γυμναστής — (personal) trainer", "προπόνηση": "προπόνηση — training session", "αστράγαλο": "αστράγαλος — ankle", "τον στραμπούληξα": "στραμπουλάω — to sprain", "να μην πατάω": "πατάω — to step, put weight on", "ρυθμό": "ρυθμός — rhythm, pace", "ασκήσεις": "άσκηση — exercise", "θα αναπληρώσουμε": "αναπληρώνω — to make up (for)", "χρέωση": "χρέωση — charge"},
})

ITEMS.append({
 "id": "l26-dia-tourta", "title": "Μια τούρτα για τα γενέθλια", "title_en": "A birthday cake", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα ζαχαροπλαστείο.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Θα ήθελα να παραγγείλω μια τούρτα για τα γενέθλια του γιου μου, το Σάββατο. Κλείνει τα οχτώ και θα έχουμε περίπου είκοσι παιδιά.", "Good morning. I'd like to order a cake for my son's birthday, on Saturday. He's turning eight and we'll have about twenty children."),
  L("Ζαχαροπλάστης", "m", "Για είκοσι παιδιά, και μερικούς γονείς φαντάζομαι, σας προτείνω μια τούρτα δύο κιλών. Τι γεύση προτιμάτε; Η σοκολάτα με φράουλα είναι η πιο δημοφιλής στα παιδικά πάρτι.", "For twenty children, and some parents I imagine, I'd suggest a two-kilo cake. Which flavour do you prefer? Chocolate with strawberry is the most popular at children's parties."),
  L("Πελάτισσα", "f", "Σοκολάτα, ναι, αλλά χωρίς ξηρούς καρπούς, γιατί ένα από τα παιδιά έχει σοβαρή αλλεργία. Μπορείτε να μου εγγυηθείτε ότι δεν θα υπάρχουν ίχνη;", "Chocolate, yes, but without nuts, because one of the children has a serious allergy. Can you guarantee there won't be any traces?"),
  L("Ζαχαροπλάστης", "m", "Θα σας πω ειλικρινά: στο εργαστήριο δουλεύουμε και με αμύγδαλα και με φουντούκια, οπότε εγγύηση εκατό τοις εκατό δεν μπορώ να δώσω. Για το παιδί με την αλλεργία, θα σας πρότεινα να φέρετε κάτι ξεχωριστό από ένα κατάστημα που ειδικεύεται σε τέτοια προϊόντα.", "I'll be honest with you: in the workshop we work with both almonds and hazelnuts, so I can't give a hundred per cent guarantee. For the child with the allergy, I'd suggest you bring something separate from a shop that specialises in such products."),
  L("Πελάτισσα", "f", "Σας ευχαριστώ για την ειλικρίνεια. Εντάξει, κλείνουμε τη σοκολατένια. Μπορείτε να γράψετε πάνω «Χρόνια πολλά, Άρη» και να την έχω έτοιμη στις δώδεκα;", "Thank you for your honesty. All right, we'll go for the chocolate one. Can you write «Happy birthday, Aris» on it and have it ready for me at twelve?"),
 ],
 "questions": [
  Q("Πόσο μεγάλη τούρτα προτείνει ο ζαχαροπλάστης;", ["Ενός κιλού", "Δύο κιλών", "Τριών κιλών", "Μισού κιλού"], 1, "σας προτείνω μια τούρτα δύο κιλών"),
  Q("Γιατί δεν μπορεί να εγγυηθεί ότι η τούρτα δεν θα έχει ίχνη ξηρών καρπών;", ["Γιατί δεν ξέρει τη συνταγή", "Γιατί στο εργαστήριο χρησιμοποιούν αμύγδαλα και φουντούκια", "Γιατί η σοκολάτα περιέχει πάντα ξηρούς καρπούς", "Γιατί δεν έχει χρόνο"], 1, "στο εργαστήριο δουλεύουμε και με αμύγδαλα και με φουντούκια"),
  Q("Τι προτείνει για το παιδί με την αλλεργία;", ["Να μη φάει τίποτα", "Να φέρουν κάτι από ένα εξειδικευμένο κατάστημα", "Να φάει μόνο φράουλες", "Να φτιάξει μια μικρή τούρτα χωρίς σοκολάτα"], 1, "να φέρετε κάτι ξεχωριστό από ένα κατάστημα που ειδικεύεται σε τέτοια προϊόντα"),
 ],
 "gloss": {"ζαχαροπλαστείο": "ζαχαροπλαστείο — patisserie", "να παραγγείλω": "παραγγέλνω — to order", "δημοφιλής": "δημοφιλής — popular", "ξηρούς καρπούς": "ξηροί καρποί — nuts", "αλλεργία": "αλλεργία — allergy", "να μου εγγυηθείτε": "εγγυώμαι — to guarantee", "ίχνη": "ίχνος — trace", "αμύγδαλα": "αμύγδαλο — almond", "φουντούκια": "φουντούκι — hazelnut", "ειδικεύεται": "ειδικεύομαι — to specialise", "ειλικρίνεια": "ειλικρίνεια — honesty, frankness"},
})

ITEMS.append({
 "id": "l26-dia-varka", "title": "Νοικιάζοντας βάρκα", "title_en": "Renting a boat", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα γραφείο ενοικίασης σκαφών σε ένα νησί.",
 "script": [
  L("Τουρίστας", "m", "Γεια σας. Θέλουμε να νοικιάσουμε μια βάρκα για αύριο, για να πάμε στις παραλίες της νότιας πλευράς. Δεν έχουμε δίπλωμα σκάφους. Γίνεται;", "Hello. We'd like to rent a boat for tomorrow, to go to the beaches on the south side. We don't have a boat licence. Is that possible?"),
  L("Υπάλληλος", "f", "Βεβαίως. Οι μικρές βάρκες με μηχανή μέχρι τριάντα ίππους δεν χρειάζονται δίπλωμα. Χωράνε πέντε άτομα και κοστίζουν ενενήντα ευρώ τη μέρα, με τα καύσιμα να πληρώνονται χωριστά.", "Of course. Small boats with engines up to thirty horsepower don't need a licence. They take five people and cost ninety euros a day, with fuel paid separately."),
  L("Τουρίστας", "m", "Δεν έχουμε οδηγήσει ποτέ βάρκα. Είναι δύσκολο;", "We've never driven a boat. Is it difficult?"),
  L("Υπάλληλος", "f", "Καθόλου. Πριν ξεκινήσετε, ο συνάδελφός μου θα σας κάνει μια σύντομη εκπαίδευση, θα σας δείξει τον χάρτη και τα σημεία όπου δεν επιτρέπεται να πλησιάσετε. Το σημαντικότερο είναι ο καιρός: αν φυσάει πάνω από πέντε μποφόρ, δεν βγαίνει καμία βάρκα, και σας επιστρέφουμε τα χρήματα.", "Not at all. Before you set off, my colleague will give you a short training session and show you the map and the spots you're not allowed to approach. The most important thing is the weather: if the wind is above five Beaufort, no boat goes out, and we give you your money back."),
  L("Τουρίστας", "m", "Τέλεια. Και τι ώρα πρέπει να την επιστρέψουμε;", "Perfect. And what time do we have to bring it back?"),
  L("Υπάλληλος", "f", "Μέχρι τις επτά το απόγευμα, πριν πέσει ο ήλιος. Θα σας ζητήσω επίσης μια εγγύηση διακοσίων ευρώ, που θα σας επιστραφεί αν η βάρκα γυρίσει χωρίς ζημιές.", "By seven in the evening, before the sun goes down. I'll also ask you for a two-hundred-euro deposit, which will be returned if the boat comes back without damage."),
 ],
 "questions": [
  Q("Ποιες βάρκες μπορεί να οδηγήσει κάποιος χωρίς δίπλωμα;", ["Όλες τις βάρκες", "Βάρκες με μηχανή μέχρι τριάντα ίππους", "Μόνο βάρκες με κουπιά", "Καμία"], 1, "Οι μικρές βάρκες με μηχανή μέχρι τριάντα ίππους δεν χρειάζονται δίπλωμα"),
  Q("Τι θα γίνει αν φυσάει πάνω από πέντε μποφόρ;", ["Θα πάνε μόνο σε κοντινές παραλίες", "Δεν θα βγει η βάρκα και θα πάρουν πίσω τα χρήματα", "Θα πληρώσουν επιπλέον", "Θα τους συνοδεύσει ένας υπάλληλος"], 1, "δεν βγαίνει καμία βάρκα, και σας επιστρέφουμε τα χρήματα"),
  Q("Πότε θα πάρουν πίσω την εγγύηση;", ["Αμέσως", "Αν η βάρκα γυρίσει χωρίς ζημιές", "Στο τέλος της εβδομάδας", "Ποτέ"], 1, "θα σας επιστραφεί αν η βάρκα γυρίσει χωρίς ζημιές"),
 ],
 "gloss": {"ενοικίασης": "ενοικίαση — rental", "σκαφών": "σκάφος — boat, vessel", "δίπλωμα": "δίπλωμα — licence", "ίππους": "ίππος — horsepower (lit. horse)", "καύσιμα": "καύσιμα — fuel", "εκπαίδευση": "εκπαίδευση — training", "μποφόρ": "μποφόρ — Beaufort (wind force)", "εγγύηση": "εγγύηση — deposit, guarantee", "ζημιές": "ζημιά — damage"},
})

ITEMS.append({
 "id": "l26-mon-istioforo", "title": "Το σπίτι μου είναι ένα ιστιοφόρο", "title_en": "My home is a sailing boat", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να μιλά για τη ζωή της σε ένα ιστιοφόρο.",
 "script": [
  L("Γυναίκα", "f", "Πριν από έξι χρόνια, ο άντρας μου κι εγώ πουλήσαμε το διαμέρισμά μας στην Αθήνα και αγοράσαμε ένα μεταχειρισμένο ιστιοφόρο δώδεκα μέτρων. Οι φίλοι μας νόμιζαν ότι είχαμε τρελαθεί. Εμείς απλώς είχαμε κουραστεί να περνάμε δύο ώρες τη μέρα στην κίνηση.", "Six years ago, my husband and I sold our flat in Athens and bought a second-hand twelve-metre sailing boat. Our friends thought we'd gone mad. We were simply tired of spending two hours a day in traffic."),
  L("Γυναίκα", "f", "Η ζωή στο σκάφος δεν είναι τόσο ρομαντική όσο φαίνεται στις φωτογραφίες. Ο χώρος είναι ελάχιστος, το νερό το μετράμε με το λίτρο, και κάθε τόσο κάτι χαλάει: μια αντλία, ένα πανί, η μηχανή. Έχω μάθει να επισκευάζω πράγματα που πριν ούτε ήξερα ότι υπάρχουν.", "Life on board isn't as romantic as it looks in photos. Space is minimal, we measure water by the litre, and every so often something breaks: a pump, a sail, the engine. I've learned to repair things I didn't even know existed before."),
  L("Γυναίκα", "f", "Δουλεύουμε και οι δύο εξ αποστάσεως, εγώ ως μεταφράστρια κι εκείνος ως προγραμματιστής, οπότε το πιο σημαντικό εργαλείο μας είναι μια καλή σύνδεση στο διαδίκτυο. Τον χειμώνα μένουμε σε μια μαρίνα στη Λέρο· το καλοκαίρι ταξιδεύουμε στο Αιγαίο.", "We both work remotely, me as a translator and him as a programmer, so our most important tool is a good internet connection. In winter we stay in a marina on Leros; in summer we sail around the Aegean."),
  L("Γυναίκα", "f", "Αυτό που κέρδισα δεν είναι η θάλασσα, είναι ο χρόνος. Όταν έχεις τόσο λίγα πράγματα, καταλαβαίνεις πόσο λίγα χρειάζεσαι πραγματικά.", "What I've gained isn't the sea, it's time. When you have so few things, you realise how little you really need."),
 ],
 "questions": [
  Q("Γιατί αποφάσισαν να ζήσουν σε ιστιοφόρο;", ["Γιατί κληρονόμησαν ένα σκάφος", "Γιατί είχαν κουραστεί από την κίνηση και τον τρόπο ζωής στην πόλη", "Γιατί έχασαν τη δουλειά τους", "Γιατί ήθελαν να γίνουν ψαράδες"], 1, "είχαμε κουραστεί να περνάμε δύο ώρες τη μέρα στην κίνηση"),
  Q("Ποια δυσκολία της ζωής στο σκάφος αναφέρει;", ["Τη μοναξιά", "Τον ελάχιστο χώρο και τις συχνές βλάβες", "Τη ναυτία", "Το υψηλό κόστος της μαρίνας"], 1, "Ο χώρος είναι ελάχιστος, το νερό το μετράμε με το λίτρο, και κάθε τόσο κάτι χαλάει"),
  Q("Πώς βγάζουν τα προς το ζην;", ["Νοικιάζουν το σκάφος σε τουρίστες", "Δουλεύουν εξ αποστάσεως", "Ψαρεύουν", "Ζουν από τα λεφτά του διαμερίσματος"], 1, "Δουλεύουμε και οι δύο εξ αποστάσεως"),
 ],
 "gloss": {"ιστιοφόρο": "ιστιοφόρο — sailing boat", "μεταχειρισμένο": "μεταχειρισμένος — second-hand", "είχαμε τρελαθεί": "τρελαίνομαι — to go mad", "ελάχιστος": "ελάχιστος — minimal", "αντλία": "αντλία — pump", "πανί": "πανί — sail", "εξ αποστάσεως": "εξ αποστάσεως — remotely", "μεταφράστρια": "μεταφράστρια — translator (female)", "προγραμματιστής": "προγραμματιστής — programmer", "μαρίνα": "μαρίνα — marina"},
})

ITEMS.append({
 "id": "l26-rep-ikaria", "title": "Η Ικαρία", "title_en": "Ikaria", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από την Ικαρία.",
 "script": [
  L("Δημοσιογράφος", "f", "Το νησί πήρε, σύμφωνα με τον μύθο, το όνομά του από τον Ίκαρο, που έπεσε στη θάλασσα εδώ κοντά, όταν πέταξε πολύ κοντά στον ήλιο και έλιωσε το κερί στα φτερά του. Σήμερα, όμως, η Ικαρία είναι γνωστή σε όλο τον κόσμο για κάτι πολύ πιο γήινο: τη μακροζωία των κατοίκων της.", "According to myth, the island took its name from Icarus, who fell into the sea nearby when he flew too close to the sun and the wax on his wings melted. Today, though, Ikaria is known around the world for something much more down to earth: the longevity of its inhabitants."),
  L("Δημοσιογράφος", "f", "Οι ερευνητές έχουν κατατάξει την Ικαρία στις λεγόμενες «γαλάζιες ζώνες», περιοχές όπου ένα ασυνήθιστα μεγάλο ποσοστό ανθρώπων ξεπερνά τα ενενήντα. Οι εξηγήσεις που δίνονται είναι πολλές: η απλή διατροφή με λαχανικά, όσπρια και λάδι, το περπάτημα στα ορεινά χωριά, ο ύπνος το μεσημέρι και, κυρίως, οι στενοί κοινωνικοί δεσμοί.", "Researchers have classed Ikaria among the so-called «blue zones», areas where an unusually large share of people live past ninety. Many explanations are given: a simple diet of vegetables, pulses and oil, walking in the mountain villages, the midday nap and, above all, close social ties."),
  L("Δημοσιογράφος", "f", "Οι δεσμοί αυτοί φαίνονται καλύτερα στα περίφημα πανηγύρια του καλοκαιριού, όπου νέοι και ηλικιωμένοι χορεύουν μαζί τον ικαριώτικο χορό μέχρι το πρωί. «Εδώ κανείς δεν βιάζεται», μου είπε ένας ογδοντάχρονος βοσκός. «Το ρολόι το έχουμε για στολίδι.»", "These ties are best seen at the famous summer festivals, where young and old dance the Ikarian dance together until morning. «Nobody hurries here», an eighty-year-old shepherd told me. «We keep the clock as an ornament.»"),
 ],
 "questions": [
  Q("Από πού πήρε το όνομά της η Ικαρία σύμφωνα με τον μύθο;", ["Από έναν βασιλιά", "Από τον Ίκαρο, που έπεσε στη θάλασσα κοντά στο νησί", "Από ένα ποτάμι", "Από έναν θεό του κρασιού"], 1, "πήρε, σύμφωνα με τον μύθο, το όνομά του από τον Ίκαρο"),
  Q("Τι είναι οι «γαλάζιες ζώνες»;", ["Προστατευμένες θαλάσσιες περιοχές", "Περιοχές όπου πολλοί άνθρωποι ξεπερνούν τα ενενήντα", "Παραλίες με γαλάζια σημαία", "Ζώνες χωρίς αυτοκίνητα"], 1, "περιοχές όπου ένα ασυνήθιστα μεγάλο ποσοστό ανθρώπων ξεπερνά τα ενενήντα"),
  Q("Τι εννοεί ο βοσκός με τη φράση «Το ρολόι το έχουμε για στολίδι»;", ["Ότι τα ρολόγια είναι ακριβά", "Ότι στο νησί δεν ζουν με το άγχος του χρόνου", "Ότι του αρέσουν τα κοσμήματα", "Ότι το ρολόι του είναι χαλασμένο"], 1, "«Εδώ κανείς δεν βιάζεται»"),
 ],
 "gloss": {"μύθο": "μύθος — myth", "έλιωσε": "λιώνω — to melt", "κερί": "κερί — wax", "γήινο": "γήινος — earthly, down to earth", "μακροζωία": "μακροζωία — longevity", "έχουν κατατάξει": "κατατάσσω — to classify, rank", "όσπρια": "όσπρια — pulses", "δεσμοί": "δεσμός — tie, bond", "πανηγύρια": "πανηγύρι — village festival", "βοσκός": "βοσκός — shepherd", "στολίδι": "στολίδι — ornament"},
})

ITEMS.append({
 "id": "l26-rep-samaria", "title": "Το φαράγγι της Σαμαριάς", "title_en": "The Samaria Gorge", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από το φαράγγι της Σαμαριάς, στη δυτική Κρήτη.",
 "script": [
  L("Δημοσιογράφος", "m", "Είναι έξι το πρωί στο Ξυλόσκαλο, στο οροπέδιο του Ομαλού, και εκατοντάδες πεζοπόροι ετοιμάζονται να κατέβουν στο φαράγγι της Σαμαριάς, ένα από τα μεγαλύτερα της Ευρώπης. Η διαδρομή, περίπου δεκαέξι χιλιόμετρα, ξεκινά από τα Λευκά Όρη και καταλήγει στην Αγία Ρουμέλη, στο Λιβυκό πέλαγος.", "It's six in the morning at Xyloskalo, on the Omalos plateau, and hundreds of hikers are getting ready to go down into the Samaria Gorge, one of the largest in Europe. The route, about sixteen kilometres long, starts in the White Mountains and ends at Agia Roumeli, on the Libyan Sea."),
  L("Δημοσιογράφος", "m", "Το φαράγγι είναι εθνικός δρυμός από το 1962 και ανοίγει για το κοινό μόνο από την άνοιξη ως το φθινόπωρο, όταν δεν υπάρχει κίνδυνος από τα νερά του χειμώνα. Το πιο εντυπωσιακό σημείο είναι οι Σιδερόπορτες, όπου τα βράχια υψώνονται εκατοντάδες μέτρα και το πέρασμα στενεύει τόσο, που σχεδόν αγγίζεις και τις δύο πλευρές.", "The gorge has been a national park since 1962 and is open to the public only from spring to autumn, when there is no danger from the winter waters. The most impressive spot is the Iron Gates, where the rocks rise hundreds of metres and the passage narrows so much that you can almost touch both sides."),
  L("Δημοσιογράφος", "m", "Με λίγη τύχη, ο επισκέπτης μπορεί να δει και τον κρητικό αγριόγιδο, το κρι-κρι, που βρήκε εδώ καταφύγιο. Οι δασοφύλακες υπενθυμίζουν ότι η διαδρομή είναι απαιτητική: χρειάζονται καλά παπούτσια, νερό και πέντε με επτά ώρες περπάτημα. Από την Αγία Ρουμέλη, που δεν έχει δρόμο, η επιστροφή γίνεται με πλοίο.", "With a bit of luck, visitors may also see the Cretan wild goat, the kri-kri, which found refuge here. The forest rangers remind people that the route is demanding: you need good shoes, water and five to seven hours of walking. From Agia Roumeli, which has no road, the return is by boat."),
 ],
 "questions": [
  Q("Πού τελειώνει η διαδρομή;", ["Στο Ξυλόσκαλο", "Στην Αγία Ρουμέλη, στη θάλασσα", "Στα Χανιά", "Στο οροπέδιο του Ομαλού"], 1, "καταλήγει στην Αγία Ρουμέλη, στο Λιβυκό πέλαγος"),
  Q("Γιατί το φαράγγι είναι κλειστό τον χειμώνα;", ["Γιατί κάνει πολύ κρύο", "Γιατί υπάρχει κίνδυνος από τα νερά", "Γιατί προστατεύονται τα ζώα", "Γιατί δεν υπάρχουν πλοία"], 1, "όταν δεν υπάρχει κίνδυνος από τα νερά του χειμώνα"),
  Q("Πώς επιστρέφουν οι πεζοπόροι από την Αγία Ρουμέλη;", ["Με λεωφορείο", "Με πλοίο", "Με τα πόδια", "Με ταξί"], 1, "η επιστροφή γίνεται με πλοίο"),
 ],
 "gloss": {"φαράγγι": "φαράγγι — gorge", "οροπέδιο": "οροπέδιο — plateau", "πεζοπόροι": "πεζοπόρος — hiker", "καταλήγει": "καταλήγω — to end up, finish", "εθνικός δρυμός": "εθνικός δρυμός — national park", "υψώνονται": "υψώνομαι — to rise", "στενεύει": "στενεύω — to narrow", "αγριόγιδο": "αγριόγιδο — wild goat", "δασοφύλακες": "δασοφύλακας — forest ranger", "απαιτητική": "απαιτητικός — demanding"},
})

ITEMS.append({
 "id": "l26-int-logotherapeftria", "title": "Λογοθεραπεύτρια", "title_en": "A speech therapist", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια λογοθεραπεύτρια.",
 "script": [
  L("Δημοσιογράφος", "m", "Με ποιους ανθρώπους δουλεύει ένας λογοθεραπευτής;", "Who does a speech therapist work with?"),
  L("Λογοθεραπεύτρια", "f", "Οι περισσότεροι πιστεύουν ότι δουλεύουμε μόνο με παιδιά που αργούν να μιλήσουν ή δεν προφέρουν σωστά κάποιους ήχους. Αυτό είναι ένα μεγάλο μέρος της δουλειάς μας, αλλά βοηθάμε και ενήλικες: ανθρώπους που έπαθαν εγκεφαλικό και έχασαν τον λόγο τους, ανθρώπους που τραυλίζουν, ακόμη και δασκάλους που κουράζουν τη φωνή τους.", "Most people think we only work with children who are late to talk or don't pronounce some sounds correctly. That's a big part of our work, but we also help adults: people who've had a stroke and lost their speech, people who stammer, even teachers who strain their voice."),
  L("Δημοσιογράφος", "m", "Πότε πρέπει να ανησυχήσουν οι γονείς;", "When should parents worry?"),
  L("Λογοθεραπεύτρια", "f", "Κάθε παιδί έχει τον δικό του ρυθμό, γι' αυτό δεν θέλω να τρομάξω κανέναν. Αν όμως ένα παιδί στα δύο του χρόνια δεν λέει σχεδόν καθόλου λέξεις, ή αν στα τέσσερα δεν το καταλαβαίνουν οι άνθρωποι εκτός οικογένειας, καλό είναι να γίνει μια αξιολόγηση. Όσο νωρίτερα ξεκινήσουμε, τόσο πιο γρήγορα έρχονται τα αποτελέσματα.", "Every child has its own pace, so I don't want to frighten anyone. But if a child at two says hardly any words, or if at four people outside the family can't understand them, it's a good idea to have an assessment. The earlier we start, the faster the results come."),
  L("Δημοσιογράφος", "m", "Τι είναι αυτό που σας δίνει τη μεγαλύτερη χαρά;", "What gives you the greatest joy?"),
  L("Λογοθεραπεύτρια", "f", "Θυμάμαι έναν κύριο εβδομήντα χρονών, που μετά από ένα εγκεφαλικό δεν μπορούσε να πει ούτε το όνομά του. Δουλέψαμε μαζί έναν ολόκληρο χρόνο. Την ημέρα που κατάφερε να πει «καλημέρα» στην εγγονή του, κλάψαμε και οι δύο.", "I remember a man of seventy who, after a stroke, couldn't even say his name. We worked together for a whole year. The day he managed to say «good morning» to his granddaughter, we both cried."),
 ],
 "questions": [
  Q("Ποια λανθασμένη αντίληψη υπάρχει για τους λογοθεραπευτές;", ["Ότι είναι γιατροί", "Ότι δουλεύουν μόνο με παιδιά", "Ότι δουλεύουν μόνο σε νοσοκομεία", "Ότι διδάσκουν ξένες γλώσσες"], 1, "Οι περισσότεροι πιστεύουν ότι δουλεύουμε μόνο με παιδιά"),
  Q("Πότε συμβουλεύει μια αξιολόγηση;", ["Αν το παιδί δεν διαβάζει στα πέντε", "Αν στα δύο δεν λέει σχεδόν καθόλου λέξεις ή στα τέσσερα δεν το καταλαβαίνουν οι ξένοι", "Αν το παιδί μιλάει πολύ", "Σε κάθε παιδί στα τρία"], 1, "Αν όμως ένα παιδί στα δύο του χρόνια δεν λέει σχεδόν καθόλου λέξεις"),
  Q("Γιατί έκλαψαν η λογοθεραπεύτρια και ο ηλικιωμένος κύριος;", ["Γιατί η θεραπεία απέτυχε", "Γιατί εκείνος κατάφερε να πει «καλημέρα» στην εγγονή του", "Γιατί τελείωσαν τα χρήματα", "Γιατί εκείνη άλλαζε δουλειά"], 1, "Την ημέρα που κατάφερε να πει «καλημέρα» στην εγγονή του"),
 ],
 "gloss": {"λογοθεραπεύτρια": "λογοθεραπεύτρια — speech therapist (female)", "προφέρουν": "προφέρω — to pronounce", "έπαθαν εγκεφαλικό": "παθαίνω εγκεφαλικό — to have a stroke", "λόγο": "λόγος — speech", "τραυλίζουν": "τραυλίζω — to stammer", "να ανησυχήσουν": "ανησυχώ — to worry", "ρυθμό": "ρυθμός — pace", "να τρομάξω": "τρομάζω — to frighten", "αξιολόγηση": "αξιολόγηση — assessment"},
})

ITEMS.append({
 "id": "l26-mon-rigas", "title": "Ρήγας Βελεστινλής", "title_en": "Rigas Velestinlis", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια ραδιοφωνική εκπομπή ιστορίας για τον Ρήγα Βελεστινλή, γνωστό και ως Ρήγα Φεραίο.",
 "script": [
  L("Ιστορικός", "m", "Ο Ρήγας γεννήθηκε γύρω στο 1757 στο Βελεστίνο της Θεσσαλίας, κοντά στις αρχαίες Φερές, από όπου πήρε και το προσωνύμιο Φεραίος, αν και ο ίδιος υπέγραφε Βελεστινλής. Νέος ακόμη έφυγε για την Κωνσταντινούπολη και αργότερα για τη Βλαχία, όπου υπηρέτησε ως γραμματέας Φαναριωτών ηγεμόνων και ήρθε σε επαφή με τις ιδέες του Διαφωτισμού.", "Rigas was born around 1757 in Velestino in Thessaly, near ancient Pherae, from which he got the epithet Feraios, although he himself signed as Velestinlis. While still young he left for Constantinople and later for Wallachia, where he served as secretary to Phanariot princes and came into contact with the ideas of the Enlightenment."),
  L("Ιστορικός", "m", "Στη Βιέννη, το 1797, τύπωσε τα σημαντικότερα έργα του: τη μεγάλη Χάρτα της Ελλάδος, ένα πολιτικό σχέδιο με τίτλο «Νέα Πολιτική Διοίκησις» και τον «Θούριο», το πολεμικό τραγούδι που αρχίζει με τον στίχο «Ως πότε, παλικάρια, θα ζούμε στα στενά». Αυτό που κάνει το σχέδιό του πρωτοποριακό είναι ότι δεν οραματιζόταν ένα κράτος μόνο για τους Έλληνες, αλλά μια δημοκρατία για όλους τους λαούς των Βαλκανίων, χριστιανούς και μουσουλμάνους, με ίσα δικαιώματα.", "In Vienna, in 1797, he printed his most important works: the great Charter of Greece, a political plan entitled «New Political Constitution», and the «Thourios», the war song that begins with the line «How long, brave lads, shall we live in the narrow passes». What makes his plan pioneering is that he did not envision a state only for the Greeks, but a republic for all the peoples of the Balkans, Christians and Muslims, with equal rights."),
  L("Ιστορικός", "m", "Τον Δεκέμβριο του 1797 συνελήφθη στην Τεργέστη από τις αυστριακές αρχές, που τον παρέδωσαν, μαζί με επτά συντρόφους του, στους Οθωμανούς. Τον Ιούνιο του 1798 στραγγαλίστηκαν στο Βελιγράδι, και τα σώματά τους ρίχτηκαν στον Δούναβη.", "In December 1797 he was arrested in Trieste by the Austrian authorities, who handed him over, together with seven of his companions, to the Ottomans. In June 1798 they were strangled in Belgrade, and their bodies were thrown into the Danube."),
  L("Ιστορικός", "m", "Ο Ρήγας δεν είδε ποτέ την Επανάσταση, αλλά τη γενιά που την έκανε τη μεγάλωσε ο «Θούριός» του. Ίσως αυτή είναι η πιο μεγάλη ειρωνεία της ιστορίας του: οι αρχές που ήθελαν να σβήσουν τη φωνή του την έκαναν, με τον θάνατό του, ακόμη πιο δυνατή.", "Rigas never saw the Revolution, but the generation that made it was raised on his «Thourios». Perhaps this is the greatest irony of his story: the authorities who wanted to silence his voice made it, through his death, even stronger."),
 ],
 "questions": [
  Q("Από πού πήρε ο Ρήγας το προσωνύμιο «Φεραίος»;", ["Από το επώνυμο του πατέρα του", "Από τις αρχαίες Φερές, κοντά στο Βελεστίνο", "Από ένα ποίημά του", "Από τη Βλαχία"], 1, "κοντά στις αρχαίες Φερές, από όπου πήρε και το προσωνύμιο Φεραίος"),
  Q("Τι έκανε πρωτοποριακό το πολιτικό του σχέδιο;", ["Ότι πρότεινε μια μοναρχία", "Ότι οραματιζόταν μια δημοκρατία για όλους τους λαούς των Βαλκανίων με ίσα δικαιώματα", "Ότι αφορούσε μόνο την Πελοπόννησο", "Ότι ήταν γραμμένο στα γαλλικά"], 1, "μια δημοκρατία για όλους τους λαούς των Βαλκανίων, χριστιανούς και μουσουλμάνους, με ίσα δικαιώματα"),
  Q("Τι έκαναν οι αυστριακές αρχές μετά τη σύλληψή του;", ["Τον άφησαν ελεύθερο", "Τον παρέδωσαν στους Οθωμανούς", "Τον έστειλαν εξορία στη Ρωσία", "Τον δίκασαν στη Βιέννη"], 1, "τον παρέδωσαν, μαζί με επτά συντρόφους του, στους Οθωμανούς"),
  Q("Ποια «ειρωνεία» επισημαίνει ο ιστορικός;", ["Ότι ο Ρήγας έγινε Αυστριακός πολίτης", "Ότι ο θάνατός του έκανε τη φωνή του πιο δυνατή", "Ότι κανείς δεν διάβασε τα έργα του", "Ότι ο «Θούριος» απαγορεύτηκε στην Ελλάδα"], 1, "οι αρχές που ήθελαν να σβήσουν τη φωνή του την έκαναν, με τον θάνατό του, ακόμη πιο δυνατή"),
 ],
 "gloss": {"προσωνύμιο": "προσωνύμιο — epithet, byname", "υπέγραφε": "υπογράφω — to sign", "υπηρέτησε": "υπηρετώ — to serve", "ηγεμόνων": "ηγεμόνας — prince, ruler", "Διαφωτισμού": "Διαφωτισμός — the Enlightenment", "τύπωσε": "τυπώνω — to print", "πρωτοποριακό": "πρωτοποριακός — pioneering", "οραματιζόταν": "οραματίζομαι — to envision", "συνελήφθη": "συλλαμβάνομαι — to be arrested", "στραγγαλίστηκαν": "στραγγαλίζομαι — to be strangled", "ειρωνεία": "ειρωνεία — irony"},
})

ITEMS.append({
 "id": "l26-int-trofima", "title": "Τα τρόφιμα του μέλλοντος", "title_en": "The food of the future", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με έναν επιστήμονα τροφίμων για τις νέες πηγές πρωτεΐνης.",
 "script": [
  L("Δημοσιογράφος", "f", "Ακούμε όλο και συχνότερα για έντομα στο πιάτο και για κρέας από το εργαστήριο. Γιατί ψάχνουμε νέες πηγές πρωτεΐνης;", "We hear more and more often about insects on our plates and meat from the lab. Why are we looking for new sources of protein?"),
  L("Επιστήμονας", "m", "Επειδή η κτηνοτροφία, όπως την ασκούμε σήμερα, έχει τεράστιο περιβαλλοντικό αποτύπωμα: χρειάζεται τεράστιες εκτάσεις γης, πολύ νερό και ευθύνεται για ένα σημαντικό μέρος των εκπομπών αερίων του θερμοκηπίου. Αν ο πληθυσμός της γης συνεχίσει να αυξάνεται και να καταναλώνει κρέας με τους σημερινούς ρυθμούς, το σύστημα απλώς δεν θα αντέξει.", "Because livestock farming, as we practise it today, has a huge environmental footprint: it needs vast areas of land and a lot of water, and it is responsible for a significant share of greenhouse gas emissions. If the world's population keeps growing and eating meat at today's rates, the system simply won't cope."),
  L("Δημοσιογράφος", "f", "Και τα έντομα είναι η λύση;", "And are insects the solution?"),
  L("Επιστήμονας", "m", "Είναι μία από τις λύσεις. Τα έντομα μετατρέπουν την τροφή τους σε πρωτεΐνη πολύ πιο αποδοτικά από τα ζώα εκτροφής, και στην Ευρωπαϊκή Ένωση ορισμένα είδη έχουν ήδη εγκριθεί ως τρόφιμα, συνήθως σε μορφή αλευριού. Το εμπόδιο δεν είναι επιστημονικό αλλά πολιτισμικό: η αποστροφή που νιώθουμε. Ας μην ξεχνάμε όμως ότι και τα θαλασσινά κάποτε θεωρούνταν φαγητό της ανάγκης.", "It's one of the solutions. Insects convert their food into protein far more efficiently than farm animals, and in the European Union some species have already been approved as food, usually in the form of flour. The obstacle isn't scientific but cultural: the disgust we feel. Let's not forget, though, that seafood too was once considered food of necessity."),
  L("Επιστήμονας", "m", "Όσο για το κρέας από καλλιεργημένα κύτταρα, η τεχνολογία υπάρχει, αλλά το κόστος παραμένει υψηλό, και οι κυβερνήσεις αντιδρούν διαφορετικά: η Σιγκαπούρη το ενέκρινε πρώτη, ενώ η Ιταλία το απαγόρευσε. Προσωπικά πιστεύω ότι το μέλλον δεν θα ανήκει σε ένα μόνο τρόφιμο, αλλά σε μια πιο ισορροπημένη διατροφή, με περισσότερα φυτά και λιγότερο, αλλά καλύτερο, κρέας.", "As for meat from cultivated cells, the technology exists, but the cost remains high, and governments react differently: Singapore approved it first, while Italy banned it. Personally I believe the future won't belong to a single food, but to a more balanced diet, with more plants and less, but better, meat."),
 ],
 "questions": [
  Q("Γιατί, σύμφωνα με τον επιστήμονα, χρειαζόμαστε νέες πηγές πρωτεΐνης;", ["Γιατί το κρέας είναι ανθυγιεινό", "Γιατί η σημερινή κτηνοτροφία έχει τεράστιο περιβαλλοντικό αποτύπωμα", "Γιατί τα ζώα εκτροφής εξαφανίζονται", "Γιατί οι νέοι δεν τρώνε κρέας"], 1, "η κτηνοτροφία, όπως την ασκούμε σήμερα, έχει τεράστιο περιβαλλοντικό αποτύπωμα"),
  Q("Ποιο είναι το κύριο εμπόδιο για τα έντομα ως τροφή;", ["Η έλλειψη επιστημονικών στοιχείων", "Η πολιτισμική αποστροφή", "Η απαγόρευση στην Ευρώπη", "Η υψηλή τιμή"], 1, "Το εμπόδιο δεν είναι επιστημονικό αλλά πολιτισμικό"),
  Q("Γιατί αναφέρει τα θαλασσινά;", ["Για να δείξει ότι και αυτά είναι επικίνδυνα", "Για να δείξει ότι οι διατροφικές συνήθειες αλλάζουν με τον καιρό", "Γιατί περιέχουν έντομα", "Γιατί είναι πιο ακριβά από το κρέας"], 1, "και τα θαλασσινά κάποτε θεωρούνταν φαγητό της ανάγκης"),
  Q("Ποια είναι η προσωπική του άποψη για το μέλλον;", ["Ότι θα τρώμε μόνο έντομα", "Ότι θα επικρατήσει μια πιο ισορροπημένη διατροφή με περισσότερα φυτά", "Ότι το εργαστηριακό κρέας θα αντικαταστήσει το κανονικό", "Ότι τίποτα δεν θα αλλάξει"], 1, "σε μια πιο ισορροπημένη διατροφή, με περισσότερα φυτά και λιγότερο, αλλά καλύτερο, κρέας"),
 ],
 "gloss": {"πρωτεΐνης": "πρωτεΐνη — protein", "έντομα": "έντομο — insect", "κτηνοτροφία": "κτηνοτροφία — livestock farming", "αποτύπωμα": "αποτύπωμα — footprint", "εκτάσεις": "έκταση — area, expanse", "εκπομπών": "εκπομπή — emission", "θερμοκηπίου": "θερμοκήπιο — greenhouse", "αποδοτικά": "αποδοτικά — efficiently", "εκτροφής": "εκτροφή — rearing, farming", "αποστροφή": "αποστροφή — aversion, disgust", "κύτταρα": "κύτταρο — cell", "ισορροπημένη": "ισορροπημένος — balanced"},
})
rnd = random.Random(26)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-26.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
