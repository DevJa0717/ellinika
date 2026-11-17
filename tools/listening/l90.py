# Source for library/listening/listening-90.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l90.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l90-ann-dasos-pyrkagia", "title": "Κλειστό το δάσος λόγω κινδύνου πυρκαγιάς", "title_en": "The forest is closed because of fire risk", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε στο ραδιόφωνο μια ανακοίνωση της Περιφέρειας ένα ζεστό καλοκαιρινό πρωί.",
 "script": [
  L("Εκφωνήτρια", "f", "Σύμφωνα με τον χάρτη πρόβλεψης κινδύνου πυρκαγιάς της Πολιτικής Προστασίας, για αύριο, Σάββατο, ο κίνδυνος στην περιοχή μας χαρακτηρίζεται πολύ υψηλός, λόγω των ισχυρών ανέμων και των υψηλών θερμοκρασιών.", "According to Civil Protection's fire-risk forecast map, for tomorrow, Saturday, the risk in our region is classed as very high, because of strong winds and high temperatures."),
  L("Εκφωνήτρια", "f", "Για τον λόγο αυτό, από τις έξι το πρωί μέχρι τις οκτώ το βράδυ απαγορεύεται η είσοδος και η κυκλοφορία οχημάτων και πεζών στα δάση και στα πάρκα της Περιφέρειας. Ακυρώνονται επίσης όλες οι οργανωμένες πεζοπορίες. Οι παραβάτες θα πληρώσουν πρόστιμο.", "For this reason, from six in the morning until eight in the evening, entry and movement of vehicles and pedestrians in the region's forests and parks is prohibited. All organised hikes are also cancelled. Offenders will be fined."),
  L("Εκφωνήτρια", "f", "Υπενθυμίζεται ότι απαγορεύεται κάθε εργασία που μπορεί να προκαλέσει σπίθα, όπως οι συγκολλήσεις και το κάψιμο ξερών χόρτων. Αν δείτε καπνό ή φωτιά, καλέστε αμέσως την Πυροσβεστική στο 199 και μην προσπαθήσετε να τη σβήσετε μόνοι σας, αν δεν είναι πολύ μικρή.", "A reminder that any work that could cause a spark, such as welding and burning dry grass, is prohibited. If you see smoke or fire, call the Fire Service immediately on 199 and don't try to put it out yourselves, unless it's very small."),
 ],
 "questions": [
  Q("Γιατί ο κίνδυνος πυρκαγιάς είναι πολύ υψηλός;", ["Λόγω ξηρασίας μηνών", "Λόγω ισχυρών ανέμων και υψηλών θερμοκρασιών", "Λόγω πολλών επισκεπτών", "Λόγω κεραυνών"], 1, "λόγω των ισχυρών ανέμων και των υψηλών θερμοκρασιών"),
  Q("Τι απαγορεύεται από τις έξι το πρωί μέχρι τις οκτώ το βράδυ;", ["Το κολύμπι στη θάλασσα", "Η είσοδος σε δάση και πάρκα", "Η κυκλοφορία στο κέντρο της πόλης", "Οι συναυλίες"], 1, "απαγορεύεται η είσοδος και η κυκλοφορία οχημάτων και πεζών στα δάση και στα πάρκα"),
  Q("Τι πρέπει να κάνει κανείς αν δει καπνό;", ["Να προσπαθήσει να σβήσει τη φωτιά", "Να φωτογραφίσει τη φωτιά", "Να καλέσει αμέσως την Πυροσβεστική στο 199", "Να ειδοποιήσει τους γείτονες"], 2, "καλέστε αμέσως την Πυροσβεστική στο 199"),
 ],
 "gloss": {"Περιφέρειας": "περιφέρεια — region", "πρόβλεψης": "πρόβλεψη — forecast", "πυρκαγιάς": "πυρκαγιά — (large) fire", "χαρακτηρίζεται": "χαρακτηρίζομαι — to be classed, described", "οχημάτων": "όχημα — vehicle", "πεζών": "πεζός — pedestrian", "πεζοπορίες": "πεζοπορία — hike", "παραβάτες": "παραβάτης — offender", "πρόστιμο": "πρόστιμο — fine", "σπίθα": "σπίθα — spark", "συγκολλήσεις": "συγκόλληση — welding", "Πυροσβεστική": "Πυροσβεστική — fire service"},
})
ITEMS.append({
 "id": "l90-vm-ontision", "title": "Πέρασες στην οντισιόν!", "title_en": "You got through the audition!", "type": "voicemail", "level": "B2",
 "context_el": "Πριν από μία εβδομάδα κάνατε οντισιόν για μια ερασιτεχνική θεατρική ομάδα. Ακούτε ένα μήνυμα στο κινητό σας.",
 "script": [
  L("Σκηνοθέτρια", "f", "Γεια σου, η Ελπίδα είμαι, από τη θεατρική ομάδα «Αυλαία». Σε παίρνω με καλά νέα: σου άρεσε ο ρόλος της Λένας, έτσι δεν είναι; Ε λοιπόν, είναι δικός σου! Μας άρεσε πολύ ο τρόπος που διάβασες τη σκηνή του γράμματος, ήταν φυσικός και συγκινητικός.", "Hi, it's Elpida, from the 'Curtain' theatre group. I'm calling with good news: you liked the part of Lena, didn't you? Well, it's yours! We really liked the way you read the letter scene; it was natural and moving."),
  L("Σκηνοθέτρια", "f", "Οι πρόβες ξεκινούν την επόμενη Δευτέρα, στις οχτώ το βράδυ, στο πολιτιστικό κέντρο του δήμου, και θα γίνονται δύο φορές την εβδομάδα, Δευτέρα και Πέμπτη. Η πρεμιέρα είναι στις δεκαπέντε Μαρτίου, οπότε τον τελευταίο μήνα θα χρειαστούμε και κάποια Σάββατα.", "Rehearsals start next Monday, at eight in the evening, at the municipal cultural centre, and they'll be twice a week, Monday and Thursday. The premiere is on the fifteenth of March, so in the last month we'll need some Saturdays as well."),
  L("Σκηνοθέτρια", "f", "Ένα μόνο: θα σου στείλω το κείμενο με email σήμερα. Προσπάθησε να έχεις μάθει τουλάχιστον την πρώτη πράξη μέχρι τα μέσα του επόμενου μήνα. Και πες μου μέχρι την Παρασκευή αν δέχεσαι, γιατί αλλιώς πρέπει να ειδοποιήσω την επόμενη υποψήφια. Συγχαρητήρια!", "Just one thing: I'll email you the script today. Try to have learned at least the first act by the middle of next month. And let me know by Friday whether you accept, because otherwise I have to notify the next candidate. Congratulations!"),
 ],
 "questions": [
  Q("Τι άρεσε στη σκηνοθέτρια στην οντισιόν;", ["Το τραγούδι", "Ο τρόπος που διάβασε τη σκηνή του γράμματος", "Ο χορός", "Η εμφάνιση"], 1, "Μας άρεσε πολύ ο τρόπος που διάβασες τη σκηνή του γράμματος"),
  Q("Πότε θα γίνονται οι πρόβες;", ["Κάθε μέρα", "Δευτέρα και Πέμπτη", "Μόνο τα Σάββατα", "Τρίτη και Παρασκευή"], 1, "θα γίνονται δύο φορές την εβδομάδα, Δευτέρα και Πέμπτη"),
  Q("Μέχρι πότε πρέπει να απαντήσει;", ["Μέχρι τη Δευτέρα", "Μέχρι την Παρασκευή", "Μέχρι τα μέσα του επόμενου μήνα", "Μέχρι την πρεμιέρα"], 1, "πες μου μέχρι την Παρασκευή αν δέχεσαι"),
 ],
 "gloss": {"οντισιόν": "οντισιόν — audition", "ερασιτεχνική": "ερασιτεχνικός — amateur", "Αυλαία": "αυλαία — (stage) curtain", "ρόλος": "ρόλος — part, role", "συγκινητικός": "συγκινητικός — moving", "πρόβες": "πρόβα — rehearsal", "πρεμιέρα": "πρεμιέρα — premiere, opening night", "πράξη": "πράξη — act (of a play)", "ειδοποιήσω": "ειδοποιώ — to notify", "υποψήφια": "υποψήφια — (female) candidate", "Συγχαρητήρια": "συγχαρητήρια — congratulations"},
})
ITEMS.append({
 "id": "l90-dia-systimeno", "title": "Ένα συστημένο γράμμα", "title_en": "A registered letter", "type": "dialogue", "level": "B2",
 "context_el": "Ένας άντρας πηγαίνει στο ταχυδρομείο με ένα ειδοποιητήριο που βρήκε στο γραμματοκιβώτιό του.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Βρήκα αυτό το χαρτάκι στο γραμματοκιβώτιο. Γράφει ότι έχω ένα συστημένο.", "Good morning. I found this slip in my letterbox. It says I have a registered letter."),
  L("Υπάλληλος", "f", "Καλημέρα. Ναι, είναι ειδοποιητήριο: ο ταχυδρόμος πέρασε χθες, αλλά δεν σας βρήκε. Μου δίνετε την ταυτότητά σας, παρακαλώ;", "Good morning. Yes, it's a notice: the postman came by yesterday but didn't find you in. Could I have your ID card, please?"),
  L("Πελάτης", "m", "Ορίστε. Μήπως ξέρετε από πού είναι; Δεν περιμένω τίποτα.", "Here you are. Do you happen to know where it's from? I'm not expecting anything."),
  L("Υπάλληλος", "f", "Είναι από την εφορία. Υπογράψτε εδώ, ότι το παραλάβατε. Α, και για την επόμενη φορά: αν δεν μπορείτε να έρθετε εσείς, μπορεί να το παραλάβει κάποιος άλλος για εσάς, αρκεί να έχει εξουσιοδότηση με θεωρημένη υπογραφή και τη δική σας ταυτότητα ή φωτοτυπία της.", "It's from the tax office. Sign here to confirm you've received it. Oh, and for next time: if you can't come yourself, someone else can collect it for you, as long as they have an authorisation with a certified signature and your ID card or a photocopy of it."),
  L("Πελάτης", "m", "Και πόσο καιρό το κρατάτε εδώ, αν δεν έρθω;", "And how long do you keep it here if I don't come?"),
  L("Υπάλληλος", "f", "Δεκαπέντε μέρες. Μετά επιστρέφεται στον αποστολέα. Γι' αυτό είναι καλό να έρχεστε όσο πιο γρήγορα μπορείτε, ειδικά όταν είναι από δημόσια υπηρεσία, γιατί μπορεί να έχει προθεσμία.", "Fifteen days. After that it's returned to the sender. That's why it's good to come as soon as you can, especially when it's from a public service, because there might be a deadline."),
 ],
 "questions": [
  Q("Γιατί ο πελάτης δεν πήρε το γράμμα χθες;", ["Γιατί ήταν άρρωστος", "Γιατί ο ταχυδρόμος δεν τον βρήκε στο σπίτι", "Γιατί το γράμμα είχε λάθος διεύθυνση", "Γιατί δεν είχε ταυτότητα"], 1, "ο ταχυδρόμος πέρασε χθες, αλλά δεν σας βρήκε"),
  Q("Από πού είναι το γράμμα;", ["Από την τράπεζα", "Από την εφορία", "Από το δικαστήριο", "Από έναν φίλο"], 1, "Είναι από την εφορία"),
  Q("Τι γίνεται αν δεν το παραλάβει μέσα σε δεκαπέντε μέρες;", ["Το πετάνε", "Του το φέρνουν ξανά στο σπίτι", "Επιστρέφεται στον αποστολέα", "Πληρώνει πρόστιμο"], 2, "Μετά επιστρέφεται στον αποστολέα"),
 ],
 "gloss": {"ειδοποιητήριο": "ειδοποιητήριο — (delivery) notice", "γραμματοκιβώτιό": "γραμματοκιβώτιο — letterbox", "συστημένο": "συστημένο (γράμμα) — registered (letter)", "ταυτότητά": "ταυτότητα — identity card", "εφορία": "εφορία — tax office", "παραλάβατε": "παραλαμβάνω — to receive, collect", "εξουσιοδότηση": "εξουσιοδότηση — authorisation", "θεωρημένη": "θεωρημένος — certified", "αποστολέα": "αποστολέας — sender", "προθεσμία": "προθεσμία — deadline"},
})
ITEMS.append({
 "id": "l90-int-skinografos", "title": "Η κατασκευάστρια σκηνικών", "title_en": "The set builder", "type": "interview", "level": "B2",
 "context_el": "Σε μια πολιτιστική εκπομπή, ένας δημοσιογράφος μιλά με μια γυναίκα που φτιάχνει σκηνικά για θέατρα.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι θεατές βλέπουν τα σκηνικά σας μόνο για δύο ώρες. Πόσο καιρό χρειάζεστε για να τα φτιάξετε;", "Audiences see your sets for only two hours. How long do you need to build them?"),
  L("Κατασκευάστρια", "f", "Για μια μεγάλη παράσταση, περίπου δύο μήνες. Ξεκινάμε από τα σχέδια του σκηνογράφου, που είναι σαν τον αρχιτέκτονα. Εμείς είμαστε οι χτίστες: ξυλουργοί, ζωγράφοι, ηλεκτρολόγοι. Το πιο δύσκολο είναι ότι όλα πρέπει να μοιάζουν βαριά και στέρεα, αλλά να είναι ελαφριά, για να μετακινούνται γρήγορα ανάμεσα στις σκηνές.", "For a big production, about two months. We start from the set designer's drawings; the designer is like the architect. We're the builders: carpenters, painters, electricians. The hardest part is that everything has to look heavy and solid but be light, so it can be moved quickly between scenes."),
  L("Δημοσιογράφος", "m", "Και πώς το καταφέρνετε αυτό;", "And how do you manage that?"),
  L("Κατασκευάστρια", "f", "Με κόλπα. Ένας «πέτρινος» τοίχος είναι συνήθως φελιζόλ, ζωγραφισμένο με προσοχή. Ένα «μαρμάρινο» πάτωμα είναι ένα πανί βαμμένο στο χέρι. Από την πρώτη σειρά των καθισμάτων δεν καταλαβαίνεις τη διαφορά, αν είναι καλή η δουλειά και ο φωτισμός.", "With tricks. A 'stone' wall is usually polystyrene, carefully painted. A 'marble' floor is a hand-painted cloth. From the front row you can't tell the difference, if the work and the lighting are good."),
  L("Δημοσιογράφος", "m", "Τι γίνεται με τα σκηνικά όταν τελειώσει η παράσταση;", "What happens to the sets when the run ends?"),
  L("Κατασκευάστρια", "f", "Αυτό ήταν παλιά η πιο λυπηρή στιγμή: τα περισσότερα κατέληγαν στα σκουπίδια. Τώρα προσπαθούμε να τα ξαναχρησιμοποιούμε. Έχουμε μια αποθήκη με πόρτες, παράθυρα και έπιπλα που «παίζουν» σε τρεις και τέσσερις παραστάσεις, και δανείζουμε υλικά σε σχολεία και ερασιτεχνικές ομάδες.", "That used to be the saddest moment: most of them ended up in the rubbish. Now we try to reuse them. We have a storeroom with doors, windows and furniture that 'appear' in three or four productions, and we lend materials to schools and amateur groups."),
 ],
 "questions": [
  Q("Ποιος είναι ο ρόλος του σκηνογράφου, κατά την κατασκευάστρια;", ["Σαν του ηθοποιού", "Σαν του αρχιτέκτονα", "Σαν του ηλεκτρολόγου", "Σαν του σκηνοθέτη"], 1, "που είναι σαν τον αρχιτέκτονα"),
  Q("Ποιο είναι το πιο δύσκολο στη δουλειά της;", ["Να βρει υλικά", "Να μοιάζουν όλα βαριά και στέρεα, αλλά να είναι ελαφριά", "Να τελειώνει έγκαιρα", "Να συνεργάζεται με τους ηθοποιούς"], 1, "όλα πρέπει να μοιάζουν βαριά και στέρεα, αλλά να είναι ελαφριά"),
  Q("Τι γίνεται σήμερα με τα σκηνικά μετά την παράσταση;", ["Πετιούνται", "Πουλιούνται", "Ξαναχρησιμοποιούνται και δανείζονται", "Καίγονται"], 2, "Τώρα προσπαθούμε να τα ξαναχρησιμοποιούμε"),
 ],
 "gloss": {"σκηνικά": "σκηνικό — (stage) set", "θεατές": "θεατής — spectator, audience member", "παράσταση": "παράσταση — performance, production", "σκηνογράφου": "σκηνογράφος — set designer", "χτίστες": "χτίστης — builder", "ξυλουργοί": "ξυλουργός — carpenter", "στέρεα": "στέρεος — solid", "φελιζόλ": "φελιζόλ — polystyrene", "πανί": "πανί — cloth, canvas", "φωτισμός": "φωτισμός — lighting", "λυπηρή": "λυπηρός — sad", "κατέληγαν": "καταλήγω — to end up"},
})
ITEMS.append({
 "id": "l90-rep-symi", "title": "Η Σύμη", "title_en": "Symi", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ταξιδιωτικό ρεπορτάζ για ένα νησί των Δωδεκανήσων.",
 "script": [
  L("Ρεπόρτερ", "f", "Καθώς το πλοίο μπαίνει στο λιμάνι της Σύμης, στον Γιαλό, η πρώτη εικόνα σού κόβει την ανάσα: εκατοντάδες νεοκλασικά σπίτια, βαμμένα σε ώχρα, ροζ και γαλάζιο, ανεβαίνουν αμφιθεατρικά τις πλαγιές. Τα περισσότερα χτίστηκαν τον δέκατο ένατο αιώνα, όταν το νησί ήταν πλούσιο χάρη στη σπογγαλιεία και τη ναυπηγική.", "As the ship enters the harbour of Symi, at Gialos, the first sight takes your breath away: hundreds of neoclassical houses, painted ochre, pink and pale blue, climb the slopes like an amphitheatre. Most were built in the nineteenth century, when the island was rich thanks to sponge diving and shipbuilding."),
  L("Ρεπόρτερ", "f", "Από τον Γιαλό, η Καλή Στράτα, ένα πέτρινο μονοπάτι με εκατοντάδες σκαλιά, ανεβαίνει στο Χωριό, την πάνω πόλη. Η ανάβαση είναι κουραστική τον Αύγουστο, αλλά η θέα από ψηλά αξίζει κάθε σταγόνα ιδρώτα. Η Σύμη έχει και μια ιδιαίτερη θέση στην ιστορία: εδώ, τον Μάιο του 1945, υπογράφηκε η παράδοση των γερμανικών δυνάμεων των Δωδεκανήσων.", "From Gialos, the Kali Strata, a stone path with hundreds of steps, climbs to Chorio, the upper town. The climb is tiring in August, but the view from the top is worth every drop of sweat. Symi also has a special place in history: here, in May 1945, the surrender of the German forces in the Dodecanese was signed."),
  L("Ρεπόρτερ", "f", "Στο νότιο άκρο του νησιού βρίσκεται η μονή του Πανορμίτη, αφιερωμένη στον Αρχάγγελο Μιχαήλ, ένα από τα πιο γνωστά προσκυνήματα των Δωδεκανήσων. Και πριν φύγετε, δοκιμάστε το «συμιακό γαριδάκι», μικρές τηγανητές γαρίδες που τρώγονται ολόκληρες, με το κέλυφος.", "At the southern tip of the island is the monastery of Panormitis, dedicated to the Archangel Michael, one of the best-known pilgrimage sites in the Dodecanese. And before you leave, try the 'Symi shrimp', small fried shrimps eaten whole, shell and all."),
 ],
 "questions": [
  Q("Χάρη σε τι ήταν πλούσια η Σύμη τον δέκατο ένατο αιώνα;", ["Στον τουρισμό", "Στη σπογγαλιεία και τη ναυπηγική", "Στο κρασί", "Στο εμπόριο μαρμάρου"], 1, "χάρη στη σπογγαλιεία και τη ναυπηγική"),
  Q("Τι είναι η Καλή Στράτα;", ["Ένας δρόμος για αυτοκίνητα", "Μια παραλία", "Ένα πέτρινο μονοπάτι με σκαλιά", "Μια εκκλησία"], 2, "ένα πέτρινο μονοπάτι με εκατοντάδες σκαλιά"),
  Q("Τι έγινε στη Σύμη τον Μάιο του 1945;", ["Ένας μεγάλος σεισμός", "Υπογράφηκε η παράδοση των γερμανικών δυνάμεων των Δωδεκανήσων", "Χτίστηκε η μονή του Πανορμίτη", "Ένωση με την Ελλάδα"], 1, "υπογράφηκε η παράδοση των γερμανικών δυνάμεων των Δωδεκανήσων"),
 ],
 "gloss": {"ώχρα": "ώχρα — ochre", "αμφιθεατρικά": "αμφιθεατρικά — in tiers, like an amphitheatre", "πλαγιές": "πλαγιά — slope", "σπογγαλιεία": "σπογγαλιεία — sponge diving, sponge fishing", "ναυπηγική": "ναυπηγική — shipbuilding", "σκαλιά": "σκαλί — step", "ανάβαση": "ανάβαση — climb", "ιδρώτα": "ιδρώτας — sweat", "παράδοση": "παράδοση — surrender (also: tradition, delivery)", "προσκυνήματα": "προσκύνημα — place of pilgrimage", "κέλυφος": "κέλυφος — shell"},
})
ITEMS.append({
 "id": "l90-rep-galaxidi", "title": "Το Γαλαξίδι των καπεταναίων", "title_en": "Galaxidi, the captains' town", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για μια μικρή πόλη στις ακτές του Κορινθιακού κόλπου.",
 "script": [
  L("Ρεπόρτερ", "m", "Το Γαλαξίδι, στη Φωκίδα, είναι σήμερα μια ήσυχη κωμόπολη με δύο μικρά λιμάνια. Τον δέκατο ένατο αιώνα, όμως, ήταν ένα από τα σημαντικότερα ναυτικά κέντρα της Ελλάδας, με εκατοντάδες ιστιοφόρα πλοία που ταξίδευαν σε όλη τη Μεσόγειο και τη Μαύρη Θάλασσα.", "Galaxidi, in Phocis, is today a quiet little town with two small harbours. In the nineteenth century, however, it was one of the most important maritime centres in Greece, with hundreds of sailing ships travelling all over the Mediterranean and the Black Sea."),
  L("Ρεπόρτερ", "m", "Τα πέτρινα αρχοντικά των καπεταναίων στέκονται ακόμα στα στενά της πόλης. Η παρακμή ήρθε με τα ατμόπλοια: οι Γαλαξιδιώτες δεν μπόρεσαν να ανταγωνιστούν τα καινούργια πλοία, και πολλοί έφυγαν για τον Πειραιά. Στο Ναυτικό Μουσείο μπορεί κανείς να δει μοντέλα πλοίων, ναυτικά όργανα και πορτρέτα καπεταναίων εκείνης της εποχής.", "The captains' stone mansions still stand in the narrow streets of the town. Decline came with steamships: the people of Galaxidi couldn't compete with the new vessels, and many left for Piraeus. In the Maritime Museum you can see model ships, nautical instruments and portraits of captains from that era."),
  L("Ρεπόρτερ", "m", "Αν βρεθείτε εδώ την Καθαρά Δευτέρα, ετοιμαστείτε να λερωθείτε: στο λιμάνι γίνεται το περίφημο αλευρομουτζούρωμα, ένας «πόλεμος» με αλεύρι σε όλα τα χρώματα. Μην φορέσετε τα καλά σας ρούχα· κανείς δεν γλιτώνει!", "If you're here on Clean Monday, get ready to get dirty: the famous flour war takes place at the harbour, a 'battle' with flour in every colour. Don't wear your good clothes; nobody escapes!"),
 ],
 "questions": [
  Q("Τι ήταν το Γαλαξίδι τον δέκατο ένατο αιώνα;", ["Ένα αγροτικό χωριό", "Ένα από τα σημαντικότερα ναυτικά κέντρα της Ελλάδας", "Μια βιομηχανική πόλη", "Ένα θρησκευτικό κέντρο"], 1, "ήταν ένα από τα σημαντικότερα ναυτικά κέντρα της Ελλάδας"),
  Q("Γιατί παρήκμασε το Γαλαξίδι;", ["Λόγω ενός σεισμού", "Γιατί δεν μπόρεσε να ανταγωνιστεί τα ατμόπλοια", "Λόγω πολέμου", "Γιατί έκλεισε το λιμάνι"], 1, "Η παρακμή ήρθε με τα ατμόπλοια"),
  Q("Τι γίνεται την Καθαρά Δευτέρα στο λιμάνι;", ["Αγώνες κωπηλασίας", "Ένας «πόλεμος» με αλεύρι", "Μια λιτανεία", "Ένα πανηγύρι με ψάρια"], 1, "ένας «πόλεμος» με αλεύρι σε όλα τα χρώματα"),
 ],
 "gloss": {"καπεταναίων": "καπετάνιος — captain", "κωμόπολη": "κωμόπολη — small town", "ιστιοφόρα": "ιστιοφόρο — sailing ship", "αρχοντικά": "αρχοντικό — mansion", "παρακμή": "παρακμή — decline", "ατμόπλοια": "ατμόπλοιο — steamship", "ανταγωνιστούν": "ανταγωνίζομαι — to compete", "όργανα": "όργανο — instrument", "λερωθείτε": "λερώνομαι — to get dirty", "αλευρομουτζούρωμα": "αλευρομουτζούρωμα — flour war (Clean Monday custom)", "γλιτώνει": "γλιτώνω — to escape"},
})
ITEMS.append({
 "id": "l90-mono-kamino", "title": "Οχτακόσια χιλιόμετρα με τα πόδια", "title_en": "Eight hundred kilometres on foot", "type": "monologue", "level": "B2",
 "context_el": "Μια συνταξιούχος μιλά σε μια εκδήλωση για ένα μεγάλο ταξίδι που έκανε.",
 "script": [
  L("Συνταξιούχος", "f", "Την πρώτη μέρα της σύνταξής μου, αντί να κοιμηθώ μέχρι αργά, έβαλα σε ένα σακίδιο δύο αλλαξιές ρούχα, ένα αδιάβροχο και ένα σημειωματάριο, και πήρα το αεροπλάνο για τη Γαλλία. Από εκεί ξεκινά ένας από τους δρόμους για το Σαντιάγο ντε Κομποστέλα, στην Ισπανία: σχεδόν οχτακόσια χιλιόμετρα με τα πόδια.", "On the first day of my retirement, instead of sleeping in, I put two changes of clothes, a raincoat and a notebook in a rucksack and took a plane to France. From there one of the routes to Santiago de Compostela, in Spain, begins: almost eight hundred kilometres on foot."),
  L("Συνταξιούχος", "f", "Περπατούσα είκοσι με είκοσι πέντε χιλιόμετρα τη μέρα. Τις πρώτες εβδομάδες με πονούσαν τα πόδια μου τόσο, που κάθε βράδυ σκεφτόμουν να τα παρατήσω. Κοιμόμουν σε ξενώνες για προσκυνητές, σε κοιτώνες με δεκάδες κρεβάτια, και σε κάθε ξενώνα έπαιρνα μια σφραγίδα στο «διαβατήριο» του προσκυνητή.", "I walked twenty to twenty-five kilometres a day. In the first weeks my feet hurt so much that every evening I thought about giving up. I slept in pilgrims' hostels, in dormitories with dozens of beds, and at every hostel I got a stamp in my pilgrim's 'passport'."),
  L("Συνταξιούχος", "f", "Αυτό που θυμάμαι περισσότερο δεν είναι τα τοπία, αλλά οι άνθρωποι: ένας Κορεάτης φοιτητής, μια Ιρλανδή χήρα, ένας Γερμανός που είχε μόλις χάσει τη δουλειά του. Δεν μιλούσαμε όλοι την ίδια γλώσσα, αλλά περπατούσαμε μαζί. Έφτασα στο Σαντιάγο μετά από τριάντα τρεις μέρες, και έκλαψα σαν μικρό παιδί.", "What I remember most isn't the landscapes but the people: a Korean student, an Irish widow, a German who had just lost his job. We didn't all speak the same language, but we walked together. I reached Santiago after thirty-three days, and I cried like a small child."),
 ],
 "questions": [
  Q("Τι έκανε την πρώτη μέρα της σύνταξής της;", ["Κοιμήθηκε μέχρι αργά", "Ξεκίνησε για τον δρόμο προς το Σαντιάγο", "Πήγε διακοπές σε νησί", "Γράφτηκε σε γυμναστήριο"], 1, "πήρα το αεροπλάνο για τη Γαλλία"),
  Q("Πού κοιμόταν;", ["Σε ξενοδοχεία", "Σε σκηνή", "Σε ξενώνες για προσκυνητές", "Σε σπίτια φίλων"], 2, "Κοιμόμουν σε ξενώνες για προσκυνητές"),
  Q("Τι θυμάται περισσότερο από το ταξίδι;", ["Τα τοπία", "Το φαγητό", "Τους ανθρώπους που γνώρισε", "Τις εκκλησίες"], 2, "Αυτό που θυμάμαι περισσότερο δεν είναι τα τοπία, αλλά οι άνθρωποι"),
 ],
 "gloss": {"σύνταξής": "σύνταξη — retirement; pension", "σακίδιο": "σακίδιο — rucksack", "αλλαξιές": "αλλαξιά — change of clothes", "αδιάβροχο": "αδιάβροχο — raincoat", "σημειωματάριο": "σημειωματάριο — notebook", "παρατήσω": "παρατάω — to give up", "ξενώνες": "ξενώνας — hostel, guesthouse", "προσκυνητές": "προσκυνητής — pilgrim", "κοιτώνες": "κοιτώνας — dormitory", "σφραγίδα": "σφραγίδα — stamp", "τοπία": "τοπίο — landscape", "χήρα": "χήρα — widow"},
})
ITEMS.append({
 "id": "l90-mono-drams", "title": "Τα ντραμς στα σαράντα πέντε", "title_en": "Drums at forty-five", "type": "monologue", "level": "B2",
 "context_el": "Ένας λογιστής μιλά σε φίλους για ένα χόμπι που ξεκίνησε πρόσφατα.",
 "script": [
  L("Λογιστής", "m", "Από έφηβος ήθελα να παίζω ντραμς, αλλά οι γονείς μου δεν ήθελαν ούτε να το ακούσουν: «Θα τρελάνεις όλη την πολυκατοικία». Έτσι έγινα λογιστής, παντρεύτηκα, έκανα παιδιά, και τα ντραμς έμειναν ένα όνειρο. Πέρσι, όταν ο γιος μου ξεκίνησε μαθήματα κιθάρας, κάτι ξύπνησε μέσα μου.", "Ever since I was a teenager I wanted to play the drums, but my parents wouldn't even hear of it: 'You'll drive the whole building mad.' So I became an accountant, got married, had children, and the drums remained a dream. Last year, when my son started guitar lessons, something woke up inside me."),
  L("Λογιστής", "m", "Γράφτηκα σε μια σχολή μουσικής και αγόρασα ηλεκτρονικά ντραμς, που παίζονται με ακουστικά, για να μην ενοχλώ τους γείτονες. Τους πρώτους μήνες ήμουν απελπιστικά αργός· ο δάσκαλός μου, είκοσι τριών χρόνων, είχε την υπομονή αγίου. Μου έλεγε: «Ο ρυθμός δεν είναι στα χέρια, είναι στο κεφάλι».", "I signed up at a music school and bought an electronic drum kit, which you play with headphones, so as not to bother the neighbours. In the first months I was hopelessly slow; my teacher, who was twenty-three, had the patience of a saint. He used to tell me: 'Rhythm isn't in your hands, it's in your head.'"),
  L("Λογιστής", "m", "Τον Ιούνιο η σχολή έκανε μια συναυλία σε ένα μπαρ της γειτονιάς. Έπαιξα τρία τραγούδια με μια μπάντα από εφήβους και τον γιο μου στην κιθάρα. Η γυναίκα μου λέει ότι δεν με είχε δει ποτέ τόσο χαρούμενο. Και οι γονείς μου, στην πρώτη σειρά, χειροκροτούσαν πιο δυνατά απ' όλους.", "In June the school put on a concert at a bar in the neighbourhood. I played three songs with a band of teenagers and my son on guitar. My wife says she'd never seen me so happy. And my parents, in the front row, were clapping louder than anyone."),
 ],
 "questions": [
  Q("Γιατί δεν έπαιζε ντραμς ως έφηβος;", ["Γιατί δεν είχε χρήματα", "Γιατί οι γονείς του δεν το ήθελαν", "Γιατί δεν είχε χρόνο", "Γιατί προτιμούσε την κιθάρα"], 1, "οι γονείς μου δεν ήθελαν ούτε να το ακούσουν"),
  Q("Γιατί αγόρασε ηλεκτρονικά ντραμς;", ["Γιατί ήταν φθηνότερα", "Για να μην ενοχλεί τους γείτονες", "Γιατί του τα πρότεινε ο γιος του", "Γιατί χωράνε στο αυτοκίνητο"], 1, "για να μην ενοχλώ τους γείτονες"),
  Q("Τι έκαναν οι γονείς του στη συναυλία;", ["Δεν ήρθαν", "Έφυγαν νωρίς", "Χειροκροτούσαν πιο δυνατά απ' όλους", "Του είπαν να σταματήσει"], 2, "χειροκροτούσαν πιο δυνατά απ' όλους"),
 ],
 "gloss": {"λογιστής": "λογιστής — accountant", "ντραμς": "ντραμς — drums, drum kit", "έφηβος": "έφηβος — teenager", "τρελάνεις": "τρελαίνω — to drive mad", "ακουστικά": "ακουστικά — headphones", "ενοχλώ": "ενοχλώ — to bother", "απελπιστικά": "απελπιστικά — hopelessly", "υπομονή": "υπομονή — patience", "αγίου": "άγιος — saint", "ρυθμός": "ρυθμός — rhythm", "μπάντα": "μπάντα — band", "χειροκροτούσαν": "χειροκροτώ — to clap, applaud"},
})
ITEMS.append({
 "id": "l90-c1-fotostefano", "title": "Το φαινόμενο του φωτοστέφανου", "title_en": "The halo effect", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την ψυχολογία της καθημερινής ζωής, η παρουσιάστρια συζητά με μια κοινωνική ψυχολόγο.",
 "script": [
  L("Παρουσιάστρια", "f", "Λέμε ότι «την πρώτη εντύπωση δεν την αλλάζεις ποτέ». Ισχύει;", "We say that 'you never get a second chance to make a first impression'. Is it true?"),
  L("Ψυχολόγος", "f", "Σε μεγάλο βαθμό, ναι, και ένας λόγος είναι αυτό που ονομάζουμε «φαινόμενο του φωτοστέφανου». Όταν ένα χαρακτηριστικό κάποιου μας κάνει θετική εντύπωση, για παράδειγμα η εμφάνισή του, τείνουμε να του αποδίδουμε και άλλες θετικές ιδιότητες, για τις οποίες δεν έχουμε καμία ένδειξη: εξυπνάδα, ειλικρίνεια, ικανότητα. Είναι σαν να βλέπουμε ολόκληρο τον άνθρωπο μέσα από ένα φωτεινό στεφάνι.", "To a large extent, yes, and one reason is what we call the 'halo effect'. When one of someone's characteristics makes a positive impression on us, for example their appearance, we tend to attribute other positive qualities to them for which we have no evidence at all: intelligence, honesty, competence. It's as if we see the whole person through a bright halo."),
  L("Παρουσιάστρια", "f", "Από πότε το γνωρίζουμε;", "Since when have we known about it?"),
  L("Ψυχολόγος", "f", "Ο όρος χρησιμοποιήθηκε για πρώτη φορά το 1920 από τον Αμερικανό ψυχολόγο Έντουαρντ Θορνταϊκ. Είχε ζητήσει από αξιωματικούς του στρατού να αξιολογήσουν τους στρατιώτες τους σε διάφορα χαρακτηριστικά, όπως η σωματική διάπλαση, η εξυπνάδα και η ηγετική ικανότητα. Παρατήρησε ότι οι βαθμολογίες ήταν ύποπτα συνεπείς: όποιος έπαιρνε υψηλό βαθμό σε ένα χαρακτηριστικό, έπαιρνε υψηλό βαθμό σχεδόν σε όλα.", "The term was first used in 1920 by the American psychologist Edward Thorndike. He had asked army officers to rate their soldiers on various characteristics, such as physique, intelligence and leadership ability. He noticed that the ratings were suspiciously consistent: whoever got a high mark on one characteristic got a high mark on almost all of them."),
  L("Παρουσιάστρια", "f", "Και πού το συναντάμε σήμερα;", "And where do we come across it today?"),
  L("Ψυχολόγος", "f", "Παντού: σε συνεντεύξεις για δουλειά, στη βαθμολόγηση γραπτών, ακόμα και στα δικαστήρια. Λειτουργεί όμως και αντίστροφα· ένα αρνητικό χαρακτηριστικό μπορεί να «σκοτεινιάσει» όλα τα υπόλοιπα. Γι' αυτό πολλοί οργανισμοί εφαρμόζουν πλέον μεθόδους όπως η ανώνυμη διόρθωση των γραπτών ή οι οντισιόν πίσω από παραβάν στις ορχήστρες. Όταν δεν βλέπεις τον άνθρωπο, κρίνεις μόνο τη δουλειά του.", "Everywhere: in job interviews, in marking exam papers, even in the courts. But it also works in reverse; one negative characteristic can 'darken' all the others. That's why many organisations now use methods such as anonymous marking of papers or auditions behind a screen in orchestras. When you can't see the person, you judge only their work."),
 ],
 "questions": [
  Q("Τι είναι το «φαινόμενο του φωτοστέφανου»;", ["Η τάση να θυμόμαστε μόνο τις αρνητικές εντυπώσεις", "Η τάση να αποδίδουμε σε κάποιον θετικές ιδιότητες επειδή ένα χαρακτηριστικό του μας εντυπωσίασε", "Η τάση να κρίνουμε τους άλλους αυστηρότερα από τον εαυτό μας", "Η τάση να εμπιστευόμαστε τους ειδικούς"], 1, "τείνουμε να του αποδίδουμε και άλλες θετικές ιδιότητες, για τις οποίες δεν έχουμε καμία ένδειξη"),
  Q("Τι παρατήρησε ο Θορνταϊκ στις αξιολογήσεις των αξιωματικών;", ["Ότι ήταν τυχαίες", "Ότι ήταν ύποπτα συνεπείς", "Ότι ήταν πολύ αυστηρές", "Ότι αφορούσαν μόνο τη σωματική διάπλαση"], 1, "οι βαθμολογίες ήταν ύποπτα συνεπείς"),
  Q("Τι σημαίνει ότι το φαινόμενο λειτουργεί «αντίστροφα»;", ["Ότι οι άνθρωποι αλλάζουν γνώμη", "Ότι ένα αρνητικό χαρακτηριστικό μπορεί να επηρεάσει αρνητικά την εικόνα όλων των υπολοίπων", "Ότι τα θετικά χαρακτηριστικά ξεχνιούνται", "Ότι οι κριτές γίνονται πιο επιεικείς"], 1, "ένα αρνητικό χαρακτηριστικό μπορεί να «σκοτεινιάσει» όλα τα υπόλοιπα"),
  Q("Γιατί εφαρμόζονται οντισιόν πίσω από παραβάν;", ["Για να μη φοβούνται οι μουσικοί", "Για να κρίνεται μόνο η δουλειά και όχι ο άνθρωπος", "Για να ακούγεται καλύτερα ο ήχος", "Για λόγους ασφαλείας"], 1, "Όταν δεν βλέπεις τον άνθρωπο, κρίνεις μόνο τη δουλειά του"),
 ],
 "gloss": {"εντύπωση": "εντύπωση — impression", "φωτοστέφανου": "φωτοστέφανο — halo", "αποδίδουμε": "αποδίδω — to attribute", "ιδιότητες": "ιδιότητα — quality, property", "ένδειξη": "ένδειξη — evidence, indication", "στεφάνι": "στεφάνι — wreath, ring", "αξιωματικούς": "αξιωματικός — (military) officer", "αξιολογήσουν": "αξιολογώ — to assess, rate", "διάπλαση": "διάπλαση — build, physique", "ύποπτα": "ύποπτα — suspiciously", "συνεπείς": "συνεπής — consistent", "παραβάν": "παραβάν — screen, partition"},
})
ITEMS.append({
 "id": "l90-c1-epivevaiosi", "title": "Βλέπουμε ό,τι θέλουμε να δούμε", "title_en": "We see what we want to see", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε την αρχή μιας διάλεξης για την κριτική σκέψη σε ένα πανεπιστήμιο.",
 "script": [
  L("Καθηγητής", "m", "Το 1960, ο Βρετανός ψυχολόγος Πίτερ Γουέισον έκανε ένα απλό πείραμα. Έδειχνε στους συμμετέχοντες τρεις αριθμούς, δύο, τέσσερα, έξι, και τους έλεγε ότι ακολουθούν έναν κανόνα. Εκείνοι έπρεπε να βρουν τον κανόνα προτείνοντας δικές τους τριάδες αριθμών, και ο ερευνητής τους απαντούσε μόνο «ναι, ταιριάζει» ή «όχι, δεν ταιριάζει».", "In 1960, the British psychologist Peter Wason carried out a simple experiment. He showed participants three numbers, two, four, six, and told them they followed a rule. They had to find the rule by proposing their own triplets of numbers, and the researcher would only answer 'yes, it fits' or 'no, it doesn't'."),
  L("Καθηγητής", "m", "Οι περισσότεροι υπέθεταν αμέσως ότι ο κανόνας ήταν «ζυγοί αριθμοί που αυξάνονται κατά δύο», και πρότειναν τριάδες όπως οχτώ, δέκα, δώδεκα, ή είκοσι, είκοσι δύο, είκοσι τέσσερα. Η απάντηση ήταν πάντα «ναι», και έτσι ήταν όλο και πιο σίγουροι. Ο πραγματικός κανόνας, όμως, ήταν πολύ πιο απλός: «οποιοιδήποτε τρεις αριθμοί σε αύξουσα σειρά». Σχετικά λίγοι τον βρήκαν, γιατί σχεδόν κανείς δεν δοκίμασε μια τριάδα που θα μπορούσε να διαψεύσει την υπόθεσή του, όπως ένα, δύο, τρία.", "Most immediately assumed the rule was 'even numbers increasing by two', and proposed triplets like eight, ten, twelve, or twenty, twenty-two, twenty-four. The answer was always 'yes', and so they became more and more confident. But the real rule was much simpler: 'any three numbers in ascending order'. Relatively few found it, because hardly anyone tried a triplet that could have disproved their hypothesis, such as one, two, three."),
  L("Καθηγητής", "m", "Αυτή η τάση να αναζητούμε, να θυμόμαστε και να ερμηνεύουμε τις πληροφορίες με τρόπο που επιβεβαιώνει όσα ήδη πιστεύουμε ονομάζεται «προκατάληψη επιβεβαίωσης». Σήμερα, με αλγορίθμους που μας δείχνουν όλο και περισσότερα από όσα ήδη μας αρέσουν, είναι ισχυρότερη από ποτέ. Το αντίδοτο δεν είναι να μην έχουμε απόψεις, αλλά να κάνουμε συστηματικά την ερώτηση που απέφυγαν οι συμμετέχοντες του Γουέισον: «Τι θα με έπειθε ότι κάνω λάθος;». Σε αυτό το μάθημα θα την κάνουμε πολλές φορές.", "This tendency to seek out, remember and interpret information in a way that confirms what we already believe is called 'confirmation bias'. Today, with algorithms that show us more and more of what we already like, it is stronger than ever. The antidote isn't to have no opinions, but to systematically ask the question Wason's participants avoided: 'What would convince me that I'm wrong?' In this course we'll ask it many times."),
 ],
 "questions": [
  Q("Τι κανόνα υπέθεταν οι περισσότεροι συμμετέχοντες;", ["«Οποιοιδήποτε τρεις αριθμοί σε αύξουσα σειρά»", "«Ζυγοί αριθμοί που αυξάνονται κατά δύο»", "«Μονοί αριθμοί»", "«Αριθμοί μικρότεροι από το δέκα»"], 1, "ο κανόνας ήταν «ζυγοί αριθμοί που αυξάνονται κατά δύο»"),
  Q("Γιατί σχετικά λίγοι βρήκαν τον πραγματικό κανόνα;", ["Γιατί ήταν πολύ περίπλοκος", "Γιατί ο ερευνητής τους παραπλανούσε", "Γιατί σχεδόν κανείς δεν δοκίμασε μια τριάδα που θα μπορούσε να διαψεύσει την υπόθεσή του", "Γιατί δεν είχαν αρκετό χρόνο"], 2, "σχεδόν κανείς δεν δοκίμασε μια τριάδα που θα μπορούσε να διαψεύσει την υπόθεσή του"),
  Q("Γιατί, κατά τον καθηγητή, η προκατάληψη επιβεβαίωσης είναι σήμερα ισχυρότερη από ποτέ;", ["Λόγω της εκπαίδευσης", "Λόγω των αλγορίθμων που μας δείχνουν όσα ήδη μας αρέσουν", "Γιατί διαβάζουμε λιγότερα βιβλία", "Γιατί εμπιστευόμαστε περισσότερο τους ειδικούς"], 1, "με αλγορίθμους που μας δείχνουν όλο και περισσότερα από όσα ήδη μας αρέσουν"),
  Q("Ποιο αντίδοτο προτείνει;", ["Να μην έχουμε απόψεις", "Να ρωτάμε συστηματικά τι θα μας έπειθε ότι κάνουμε λάθος", "Να μη χρησιμοποιούμε το διαδίκτυο", "Να συμφωνούμε πάντα με την πλειοψηφία"], 1, "«Τι θα με έπειθε ότι κάνω λάθος;»"),
 ],
 "gloss": {"διάλεξης": "διάλεξη — lecture", "κριτική σκέψη": "κριτική σκέψη — critical thinking", "τριάδες": "τριάδα — triplet, group of three", "ζυγοί": "ζυγός — even (number)", "αύξουσα": "αύξων — ascending", "διαψεύσει": "διαψεύδω — to disprove, refute", "υπόθεσή": "υπόθεση — hypothesis", "ερμηνεύουμε": "ερμηνεύω — to interpret", "επιβεβαιώνει": "επιβεβαιώνω — to confirm", "προκατάληψη επιβεβαίωσης": "προκατάληψη επιβεβαίωσης — confirmation bias", "αλγορίθμους": "αλγόριθμος — algorithm", "έπειθε": "πείθω — to convince"},
})

rnd = random.Random(90)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-90.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
