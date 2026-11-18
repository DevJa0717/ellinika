# Source for library/listening/listening-216.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l216.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l216-news-exypnoi-kadoi", "title": "Κάδοι που «λένε» πότε γέμισαν", "title_en": "Bins that 'say' when they're full", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια τοπική είδηση στο ραδιόφωνο για ένα νέο σύστημα αποκομιδής απορριμμάτων.",
 "script": [
  L("Εκφωνητής", "m", "Από τον επόμενο μήνα, διακόσιοι κάδοι απορριμμάτων στο κέντρο της πόλης θα έχουν αισθητήρες που μετρούν πόσο έχουν γεμίσει. Τα στοιχεία θα στέλνονται σε ένα κέντρο ελέγχου, και τα απορριμματοφόρα θα ακολουθούν κάθε μέρα διαφορετική διαδρομή, ανάλογα με το πού χρειάζεται πραγματικά αποκομιδή.", "From next month, two hundred rubbish bins in the city centre will have sensors that measure how full they are. The data will be sent to a control centre, and the dustcarts will follow a different route every day, depending on where collection is really needed."),
  L("Εκφωνητής", "m", "Σήμερα τα απορριμματοφόρα περνούν από όλους τους κάδους με το ίδιο πρόγραμμα, είτε είναι γεμάτοι είτε μισοάδειοι. Ο δήμος υπολογίζει ότι με το νέο σύστημα τα δρομολόγια θα μειωθούν περίπου κατά ένα τέταρτο, με λιγότερα καύσιμα, λιγότερο θόρυβο τη νύχτα και λιγότερη κίνηση στους στενούς δρόμους.", "Today the dustcarts pass every bin on the same schedule, whether they're full or half empty. The municipality estimates that with the new system the rounds will fall by about a quarter, with less fuel, less noise at night and less traffic in the narrow streets."),
  L("Εκφωνητής", "m", "Οι αισθητήρες θα ειδοποιούν επίσης αν η θερμοκρασία μέσα σε έναν κάδο ανέβει απότομα, κάτι που μπορεί να σημαίνει φωτιά. Οι εργαζόμενοι στην καθαριότητα ζητούν διαβεβαιώσεις ότι το σύστημα δεν θα οδηγήσει σε μείωση προσωπικού. Ο δήμαρχος απάντησε ότι οι ώρες που θα εξοικονομηθούν θα διατεθούν στο πλύσιμο των κάδων και των πεζοδρομίων.", "The sensors will also give a warning if the temperature inside a bin rises sharply, which may mean a fire. Cleaning workers are asking for assurances that the system won't lead to staff cuts. The mayor replied that the hours saved will go to washing bins and pavements."),
 ],
 "questions": [
  Q("Τι θα μετρούν οι αισθητήρες στους κάδους;", ["Το βάρος των σκουπιδιών", "Πόσο έχουν γεμίσει οι κάδοι", "Πόσοι περαστικοί πετούν σκουπίδια", "Την ποιότητα του αέρα"], 1, "αισθητήρες που μετρούν πόσο έχουν γεμίσει"),
  Q("Πώς θα αλλάξουν τα δρομολόγια των απορριμματοφόρων;", ["Θα γίνονται μόνο τη νύχτα", "Θα ακολουθούν κάθε μέρα διαφορετική διαδρομή, ανάλογα με τις ανάγκες", "Θα γίνονται δύο φορές την ημέρα", "Θα σταματήσουν τα Σαββατοκύριακα"], 1, "θα ακολουθούν κάθε μέρα διαφορετική διαδρομή, ανάλογα με το πού χρειάζεται πραγματικά αποκομιδή"),
  Q("Τι άλλο θα ανιχνεύουν οι αισθητήρες;", ["Απότομη άνοδο της θερμοκρασίας, που μπορεί να σημαίνει φωτιά", "Αν κάποιος ανοίγει τον κάδο", "Τα ανακυκλώσιμα υλικά", "Τη βροχή"], 0, "αν η θερμοκρασία μέσα σε έναν κάδο ανέβει απότομα, κάτι που μπορεί να σημαίνει φωτιά"),
  Q("Τι απάντησε ο δήμαρχος στους εργαζόμενους;", ["Ότι θα γίνουν απολύσεις", "Ότι οι ώρες που θα εξοικονομηθούν θα πάνε στο πλύσιμο κάδων και πεζοδρομίων", "Ότι το σύστημα θα δοκιμαστεί μόνο για έναν μήνα", "Ότι θα αυξηθούν οι μισθοί"], 1, "οι ώρες που θα εξοικονομηθούν θα διατεθούν στο πλύσιμο των κάδων και των πεζοδρομίων"),
 ],
 "gloss": {"αισθητήρες": "αισθητήρας — sensor", "απορριμματοφόρα": "απορριμματοφόρο — dustcart, garbage truck", "αποκομιδή": "αποκομιδή — (rubbish) collection", "μισοάδειοι": "μισοάδειος — half empty", "δρομολόγια": "δρομολόγιο — route, round", "διαβεβαιώσεις": "διαβεβαίωση — assurance", "εξοικονομηθούν": "εξοικονομώ — to save (time, money)", "διατεθούν": "διαθέτω — to allocate, make available"},
})
ITEMS.append({
 "id": "l216-dia-sofita-giagias", "title": "Τι κρατάμε από τη σοφίτα της γιαγιάς;", "title_en": "What do we keep from grandma's attic?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο αδέρφια αδειάζουν τη σοφίτα του σπιτιού της γιαγιάς τους, που πρόκειται να πουληθεί.",
 "script": [
  L("Ματίνα", "f", "Θεέ μου, πόση σκόνη! Κοίτα, Πέτρο, η ραπτομηχανή της γιαγιάς. Με αυτήν μας έραβε τις στολές για τις παρελάσεις. Αυτή δεν την πετάμε με τίποτα.", "My God, so much dust! Look, Petros, grandma's sewing machine. She sewed our uniforms for the parades on it. We're not throwing that away whatever happens."),
  L("Πέτρος", "m", "Ματίνα, το διαμέρισμά σου έχει πενήντα τετραγωνικά. Πού θα τη βάλεις; Αν κρατήσουμε ό,τι μας θυμίζει τη γιαγιά, θα χρειαστούμε δεύτερο σπίτι. Ας κρατήσουμε λίγα πράγματα, και τα υπόλοιπα να τα δώσουμε σε κάποιον που θα τα χρησιμοποιήσει.", "Matina, your flat is fifty square metres. Where will you put it? If we keep everything that reminds us of grandma, we'll need a second house. Let's keep a few things, and give the rest to someone who'll use them."),
  L("Ματίνα", "f", "Καλά, έχεις δίκιο. Η σχολή χορού της γειτονιάς ψάχνει ραπτομηχανή για τα κοστούμια. Θα της άρεσε της γιαγιάς να ράβει ακόμα, έστω και χωρίς εκείνη.", "OK, you're right. The neighbourhood dance school is looking for a sewing machine for costumes. Grandma would have liked it to go on sewing, even without her."),
  L("Πέτρος", "m", "Ωραία ιδέα. Κι αυτό το κουτί με τα γράμματα; Είναι από τον παππού, όταν δούλευε στη Γερμανία. Αυτά δεν τα δίνουμε σε κανέναν.", "Nice idea. And this box of letters? They're from grandad, when he worked in Germany. We're not giving those to anyone."),
  L("Ματίνα", "f", "Όχι βέβαια. Λέω να τα σκανάρουμε, για να έχουν αντίγραφο και τα ξαδέρφια μας. Τα πρωτότυπα τα κρατάω εγώ, χωράνε σε ένα συρτάρι.", "Of course not. I say we scan them, so our cousins can have a copy too. I'll keep the originals, they fit in a drawer."),
  L("Πέτρος", "m", "Συμφωνώ. Και τα έπιπλα θα τα πάρει ο κύριος Στάθης, που φτιάχνει παλιά έπιπλα. Τουλάχιστον θα ξέρουμε ότι δεν κατέληξαν στη χωματερή.", "Agreed. And Mr Stathis, who restores old furniture, will take the furniture. At least we'll know it didn't end up at the tip."),
 ],
 "questions": [
  Q("Γιατί ο Πέτρος δεν θέλει να κρατήσει η Ματίνα τη ραπτομηχανή;", ["Γιατί είναι χαλασμένη", "Γιατί το διαμέρισμά της είναι μικρό", "Γιατί θέλει να την πουλήσει", "Γιατί θέλει να την κρατήσει ο ίδιος"], 1, "το διαμέρισμά σου έχει πενήντα τετραγωνικά. Πού θα τη βάλεις;"),
  Q("Πού θα δώσουν τελικά τη ραπτομηχανή;", ["Σε ένα μουσείο", "Στη σχολή χορού της γειτονιάς", "Σε μια ξαδέρφη", "Σε έναν συλλέκτη"], 1, "Η σχολή χορού της γειτονιάς ψάχνει ραπτομηχανή"),
  Q("Τι θα κάνουν με τα γράμματα του παππού;", ["Θα τα δωρίσουν σε ένα αρχείο", "Θα τα πετάξουν", "Θα τα σκανάρουν και η Ματίνα θα κρατήσει τα πρωτότυπα", "Θα τα στείλουν στη Γερμανία"], 2, "Λέω να τα σκανάρουμε ... Τα πρωτότυπα τα κρατάω εγώ"),
  Q("Ποιος θα πάρει τα έπιπλα;", ["Ο κύριος Στάθης, που φτιάχνει παλιά έπιπλα", "Ο νέος ιδιοκτήτης του σπιτιού", "Τα ξαδέρφια τους", "Ο δήμος"], 0, "τα έπιπλα θα τα πάρει ο κύριος Στάθης, που φτιάχνει παλιά έπιπλα"),
 ],
 "gloss": {"σοφίτα": "σοφίτα — attic", "ραπτομηχανή": "ραπτομηχανή — sewing machine", "έραβε": "ράβω — to sew", "παρελάσεις": "παρέλαση — parade", "τετραγωνικά": "τετραγωνικά (μέτρα) — square metres", "σκανάρουμε": "σκανάρω — to scan", "πρωτότυπα": "πρωτότυπο — original", "χωματερή": "χωματερή — rubbish tip, landfill"},
})
ITEMS.append({
 "id": "l216-c1-mono-vrachnas", "title": "Ο Βραχνάς: τι είναι η παράλυση του ύπνου", "title_en": "The Vrachnas: what sleep paralysis is", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ομιλία σε έναν κύκλο εκλαϊκευμένων διαλέξεων για τον ύπνο.",
 "script": [
  L("Ομιλητής", "m", "Φανταστείτε να ξυπνάτε μέσα στη νύχτα, να έχετε πλήρη συνείδηση, αλλά να μην μπορείτε να κουνήσετε ούτε το δάχτυλό σας. Κάποιοι νιώθουν ταυτόχρονα ένα βάρος στο στήθος ή την παρουσία κάποιου μέσα στο δωμάτιο. Η ελληνική λαϊκή παράδοση έδωσε σε αυτή την εμπειρία ένα όνομα: τον Βραχνά, ένα πλάσμα που κάθεται πάνω στον κοιμισμένο και τον πνίγει.", "Imagine waking in the middle of the night, fully conscious, but unable to move even a finger. Some people feel at the same time a weight on their chest or the presence of someone in the room. Greek folk tradition gave this experience a name: the Vrachnas, a creature that sits on the sleeper and chokes him."),
  L("Ομιλητής", "m", "Η επιστήμη σήμερα έχει μια πιο πεζή εξήγηση. Στη φάση του ύπνου που ονομάζεται REM, εκείνη στην οποία βλέπουμε τα πιο ζωντανά όνειρα, ο εγκέφαλος «αποσυνδέει» σχεδόν όλους τους μύες, για να μην εκτελούμε με το σώμα όσα ονειρευόμαστε. Στην παράλυση του ύπνου, η συνείδηση ξυπνά, αλλά αυτή η αποσύνδεση κρατάει ακόμα λίγα δευτερόλεπτα ή λεπτά. Ο εγκέφαλος βρίσκεται κυριολεκτικά ανάμεσα στον ύπνο και στον ξύπνιο.", "Science today has a more prosaic explanation. In the phase of sleep called REM, the one in which we have our most vivid dreams, the brain 'disconnects' almost all the muscles, so that we don't act out with our body what we dream. In sleep paralysis, consciousness wakes up, but this disconnection lasts a few more seconds or minutes. The brain is literally between sleep and waking."),
  L("Ομιλητής", "m", "Και οι παραισθήσεις; Τα όνειρα συνεχίζουν να «διαρρέουν» στην ξύπνια αντίληψη. Ο εγκέφαλος, που αντιλαμβάνεται ότι το σώμα δεν υπακούει και ότι η αναπνοή είναι ρηχή, ψάχνει μια αιτία και, συχνά, την κατασκευάζει: μια σκιά στη γωνία, κάποιον που πατάει το στήθος. Δεν είναι τυχαίο ότι παρόμοια πλάσματα εμφανίζονται στη λαογραφία πολλών λαών, από τη Νέα Γη ως την Ιαπωνία.", "And the hallucinations? Dreams go on 'leaking' into waking perception. The brain, which senses that the body won't obey and that breathing is shallow, looks for a cause and often constructs one: a shadow in the corner, someone pressing on the chest. It's no coincidence that similar creatures appear in the folklore of many peoples, from Newfoundland to Japan."),
  L("Ομιλητής", "m", "Τα επεισόδια είναι πιο συχνά όταν κοιμόμαστε λίγο, ακανόνιστα ή ανάσκελα, και σε περιόδους άγχους. Είναι τρομακτικά, αλλά οι ειδικοί επιμένουν ότι δεν είναι επικίνδυνα. Όσοι τα ζουν συχνά βοηθιούνται απλώς όταν μαθαίνουν τι συμβαίνει: ο φόβος μικραίνει, όταν ξέρεις ότι ο Βραχνάς είναι ένας εγκέφαλος που ξύπνησε λίγο νωρίτερα από το σώμα.", "Episodes are more frequent when we sleep little, irregularly or on our back, and in periods of stress. They're frightening, but specialists insist they're not dangerous. People who experience them often are helped simply by learning what's happening: the fear shrinks when you know that the Vrachnas is a brain that woke up a little earlier than the body."),
 ],
 "questions": [
  Q("Ποιο είναι το κύριο χαρακτηριστικό της παράλυσης του ύπνου;", ["Περπατάμε ενώ κοιμόμαστε", "Έχουμε συνείδηση αλλά δεν μπορούμε να κινηθούμε", "Δεν μπορούμε να κοιμηθούμε καθόλου", "Ξεχνάμε τα όνειρά μας"], 1, "να έχετε πλήρη συνείδηση, αλλά να μην μπορείτε να κουνήσετε ούτε το δάχτυλό σας"),
  Q("Τι κάνει ο εγκέφαλος κατά τη φάση REM;", ["Σταματά να ονειρεύεται", "Αποσυνδέει σχεδόν όλους τους μύες", "Αυξάνει τον ρυθμό της αναπνοής", "Ξυπνά το σώμα"], 1, "ο εγκέφαλος «αποσυνδέει» σχεδόν όλους τους μύες"),
  Q("Πώς εξηγεί ο ομιλητής τις παραισθήσεις;", ["Ως σημάδι σοβαρής ασθένειας", "Ως αποτέλεσμα φαρμάκων", "Τα όνειρα διαρρέουν στην ξύπνια αντίληψη και ο εγκέφαλος κατασκευάζει μια αιτία", "Ως τύχη"], 2, "Τα όνειρα συνεχίζουν να «διαρρέουν» στην ξύπνια αντίληψη ... ψάχνει μια αιτία και, συχνά, την κατασκευάζει"),
  Q("Τι βοηθά συχνά όσους ζουν τέτοια επεισόδια;", ["Να κοιμούνται ανάσκελα", "Να μάθουν τι ακριβώς συμβαίνει", "Να μην κοιμούνται τη νύχτα", "Να πίνουν καφέ πριν τον ύπνο"], 1, "βοηθιούνται απλώς όταν μαθαίνουν τι συμβαίνει"),
 ],
 "gloss": {"συνείδηση": "συνείδηση — consciousness; conscience", "Βραχνά": "Βραχνάς — the Vrachnas (night demon of Greek folklore)", "πεζή": "πεζός — prosaic; pedestrian", "αποσυνδέει": "αποσυνδέω — to disconnect", "παραισθήσεις": "παραίσθηση — hallucination", "διαρρέουν": "διαρρέω — to leak", "ρηχή": "ρηχός — shallow", "λαογραφία": "λαογραφία — folklore", "ανάσκελα": "ανάσκελα — on one's back"},
})
ITEMS.append({
 "id": "l216-c1-int-skoteini-yli", "title": "Αναζητώντας την αόρατη ύλη του σύμπαντος", "title_en": "Searching for the universe's invisible matter: a physicist on dark matter", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε επιστημονική εκπομπή με μια φυσικό που μελετά τη σκοτεινή ύλη.",
 "script": [
  L("Δημοσιογράφος", "m", "Λέτε ότι το μεγαλύτερο μέρος της ύλης του σύμπαντος δεν το έχουμε δει ποτέ. Πώς ξέρουμε, τότε, ότι υπάρχει;", "You say that most of the matter in the universe has never been seen. How do we know, then, that it exists?"),
  L("Φυσικός", "f", "Από τη βαρύτητά της. Ήδη το 1933 ο Ελβετός αστρονόμος Φριτς Τσβίκι παρατήρησε ότι οι γαλαξίες σε ένα σμήνος κινούνταν τόσο γρήγορα, που κανονικά θα έπρεπε να είχαν σκορπίσει. Κάτι αόρατο τους κρατούσε μαζί. Τη δεκαετία του 1970 η Αμερικανίδα Βέρα Ρούμπιν μέτρησε πώς περιστρέφονται τα αστέρια στους γαλαξίες και βρήκε το ίδιο: τα αστέρια στις άκρες κινούνται πολύ πιο γρήγορα από όσο επιτρέπει η ορατή ύλη.", "From its gravity. As early as 1933 the Swiss astronomer Fritz Zwicky observed that the galaxies in a cluster were moving so fast that they should normally have scattered. Something invisible was holding them together. In the 1970s the American Vera Rubin measured how stars rotate in galaxies and found the same thing: stars at the edges move much faster than the visible matter allows."),
  L("Δημοσιογράφος", "m", "Και πόση είναι αυτή η σκοτεινή ύλη;", "And how much of this dark matter is there?"),
  L("Φυσικός", "f", "Σύμφωνα με τις σημερινές μετρήσεις, περίπου πέντε φορές περισσότερη από τη συνηθισμένη ύλη, αυτή από την οποία είμαστε φτιαγμένοι εμείς, οι πλανήτες και τα αστέρια. Η συνηθισμένη ύλη αποτελεί μόλις το πέντε τοις εκατό περίπου του σύμπαντος. Το υπόλοιπο είναι σκοτεινή ύλη και κάτι ακόμα πιο αινιγματικό, η σκοτεινή ενέργεια.", "According to current measurements, about five times as much as ordinary matter, the kind we, the planets and the stars are made of. Ordinary matter makes up just about five per cent of the universe. The rest is dark matter and something even more puzzling, dark energy."),
  L("Δημοσιογράφος", "m", "Πώς προσπαθείτε να την ανιχνεύσετε;", "How do you try to detect it?"),
  L("Φυσικός", "f", "Με ανιχνευτές που βρίσκονται βαθιά κάτω από βουνά, για να προστατεύονται από την κοσμική ακτινοβολία. Περιμένουμε ένα σωματίδιο σκοτεινής ύλης να συγκρουστεί, έστω και μία φορά, με έναν πυρήνα ατόμου μέσα στον ανιχνευτή. Μέχρι σήμερα δεν το έχουμε δει. Κάποιοι συνάδελφοι αναρωτιούνται μήπως πρέπει να αλλάξουμε τους νόμους της βαρύτητας αντί να ψάχνουμε κάτι αόρατο. Εγώ πιστεύω ότι ένα αρνητικό αποτέλεσμα είναι κι αυτό γνώση: μας λέει πού δεν βρίσκεται η απάντηση.", "With detectors located deep under mountains, so that they're shielded from cosmic radiation. We're waiting for a dark-matter particle to collide, even once, with an atomic nucleus inside the detector. So far we haven't seen it. Some colleagues wonder whether we should change the laws of gravity instead of looking for something invisible. I believe a negative result is knowledge too: it tells us where the answer isn't."),
 ],
 "questions": [
  Q("Πώς γνωρίζουμε ότι υπάρχει η σκοτεινή ύλη;", ["Από φωτογραφίες τηλεσκοπίων", "Από τη βαρύτητά της", "Από το χρώμα των αστεριών", "Από δείγματα μετεωριτών"], 1, "Από τη βαρύτητά της"),
  Q("Τι παρατήρησε η Βέρα Ρούμπιν;", ["Ότι οι γαλαξίες συγκρούονται", "Ότι τα αστέρια στις άκρες των γαλαξιών κινούνται πιο γρήγορα από όσο επιτρέπει η ορατή ύλη", "Ότι το σύμπαν συρρικνώνεται", "Ότι υπάρχουν νέοι πλανήτες"], 1, "τα αστέρια στις άκρες κινούνται πολύ πιο γρήγορα από όσο επιτρέπει η ορατή ύλη"),
  Q("Τι ποσοστό του σύμπαντος αποτελεί η συνηθισμένη ύλη;", ["Περίπου το πενήντα τοις εκατό", "Περίπου το πέντε τοις εκατό", "Περίπου το ογδόντα τοις εκατό", "Περίπου το είκοσι πέντε τοις εκατό"], 1, "Η συνηθισμένη ύλη αποτελεί μόλις το πέντε τοις εκατό περίπου του σύμπαντος"),
  Q("Γιατί οι ανιχνευτές βρίσκονται βαθιά κάτω από βουνά;", ["Για να είναι πιο κοντά στο κέντρο της Γης", "Για να προστατεύονται από την κοσμική ακτινοβολία", "Επειδή εκεί είναι πιο φθηνό", "Για να μην τους βλέπει κανείς"], 1, "για να προστατεύονται από την κοσμική ακτινοβολία"),
 ],
 "gloss": {"σμήνος": "σμήνος — cluster; swarm", "σκορπίσει": "σκορπίζω — to scatter", "περιστρέφονται": "περιστρέφομαι — to rotate", "αινιγματικό": "αινιγματικός — puzzling, enigmatic", "ανιχνεύσετε": "ανιχνεύω — to detect", "ανιχνευτές": "ανιχνευτής — detector", "κοσμική ακτινοβολία": "κοσμική ακτινοβολία — cosmic radiation", "σωματίδιο": "σωματίδιο — particle", "πυρήνα": "πυρήνας — nucleus"},
})
rnd = random.Random(216)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-216.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
