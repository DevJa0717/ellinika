# Source for library/listening/listening-99.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l99.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l99-ann-anelkystiras-stathmou", "title": "Εκτός λειτουργίας ο ανελκυστήρας του σταθμού", "title_en": "Station lift out of service", "type": "announcement", "level": "B2",
 "context_el": "Περιμένετε το μετρό σε έναν σταθμό. Ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνητής", "m", "Αγαπητοί επιβάτες, σας ενημερώνουμε ότι ο ανελκυστήρας που συνδέει την αποβάθρα με την έξοδο προς την οδό Πατησίων είναι εκτός λειτουργίας λόγω τεχνικής βλάβης. Οι τεχνικοί εργάζονται για την αποκατάστασή του, η οποία υπολογίζεται ότι θα ολοκληρωθεί αύριο το μεσημέρι.", "Dear passengers, we inform you that the lift connecting the platform with the exit towards Patision Street is out of service because of a technical fault. Technicians are working to repair it, which is expected to be completed tomorrow at noon."),
  L("Εκφωνητής", "m", "Οι κυλιόμενες σκάλες λειτουργούν κανονικά. Επιβάτες με αναπηρικό αμαξίδιο, καθώς και γονείς με καρότσια, μπορούν να χρησιμοποιούν τον ανελκυστήρα της απέναντι εξόδου, προς την πλατεία, ή να απευθυνθούν στο προσωπικό του σταθμού, που θα τους εξυπηρετήσει.", "The escalators are working normally. Passengers in wheelchairs, as well as parents with pushchairs, can use the lift at the opposite exit, towards the square, or contact the station staff, who will assist them."),
  L("Εκφωνητής", "m", "Όσοι ταξιδεύετε προς τον επόμενο σταθμό και χρειάζεστε ανελκυστήρα, σας συνιστούμε να κατεβείτε εκεί, όπου όλοι οι ανελκυστήρες λειτουργούν. Ζητούμε συγγνώμη για την ταλαιπωρία.", "Those of you travelling towards the next station who need a lift are advised to get off there, where all the lifts are working. We apologise for the inconvenience."),
 ],
 "questions": [
  Q("Πότε υπολογίζεται ότι θα επισκευαστεί ο ανελκυστήρας;", ["Σε μία εβδομάδα", "Αύριο το μεσημέρι", "Σήμερα το βράδυ", "Δεν είναι γνωστό"], 1, "θα ολοκληρωθεί αύριο το μεσημέρι"),
  Q("Τι μπορούν να κάνουν οι επιβάτες με αναπηρικό αμαξίδιο;", ["Να χρησιμοποιήσουν τον ανελκυστήρα της απέναντι εξόδου", "Να χρησιμοποιήσουν τις κυλιόμενες σκάλες", "Να περιμένουν μέχρι αύριο", "Να πάρουν ταξί με έξοδα του μετρό"], 0, "μπορούν να χρησιμοποιούν τον ανελκυστήρα της απέναντι εξόδου"),
  Q("Τι συνιστάται σε όσους χρειάζονται ανελκυστήρα και πηγαίνουν προς τον επόμενο σταθμό;", ["Να αλλάξουν γραμμή", "Να πάρουν το λεωφορείο", "Να κατεβούν στον επόμενο σταθμό", "Να γυρίσουν πίσω"], 2, "σας συνιστούμε να κατεβείτε εκεί"),
 ],
 "gloss": {"ανελκυστήρας": "ανελκυστήρας — lift, elevator", "αποβάθρα": "αποβάθρα — platform", "βλάβης": "βλάβη — fault", "αποκατάστασή": "αποκατάσταση — repair, restoration", "κυλιόμενες": "κυλιόμενη σκάλα — escalator", "αναπηρικό": "αναπηρικό αμαξίδιο — wheelchair", "καρότσια": "καρότσι — pushchair", "απευθυνθούν": "απευθύνομαι — to turn to, contact", "εξυπηρετήσει": "εξυπηρετώ — to assist, serve", "ταλαιπωρία": "ταλαιπωρία — inconvenience"}
})
ITEMS.append({
 "id": "l99-vm-vivliodetis", "title": "Μήνυμα από τον βιβλιοδέτη", "title_en": "A message from the bookbinder", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε δώσει ένα παλιό βιβλίο του παππού σας σε ένα βιβλιοδετείο για επισκευή. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Βιβλιοδέτης", "m", "Καλημέρα σας, ο Θανάσης είμαι, από το βιβλιοδετείο της οδού Ασκληπιού. Σας παίρνω για το λεξικό του παππού σας. Το κοίταξα με την ησυχία μου, και τα νέα είναι καλά: το χαρτί είναι γερό, το πρόβλημα είναι κυρίως η ράχη, που έχει ξεκολλήσει, και μερικές σελίδες που έχουν σκιστεί στις άκρες.", "Good morning, it's Thanasis, from the bookbindery on Asklipiou Street. I'm calling about your grandfather's dictionary. I looked at it at my leisure, and the news is good: the paper is sturdy, the problem is mainly the spine, which has come unstuck, and a few pages that are torn at the edges."),
  L("Βιβλιοδέτης", "m", "Έχετε δύο επιλογές. Μπορώ να κρατήσω το παλιό εξώφυλλο και να το ενισχύσω, ώστε να μείνει όπως το θυμάστε. Ή να του φτιάξω καινούργιο δερμάτινο, που θα είναι πιο ανθεκτικό, αλλά θα χάσει λίγο από τον παλιό του χαρακτήρα. Το πρώτο κοστίζει περίπου σαράντα ευρώ, το δεύτερο γύρω στα εβδομήντα.", "You have two options. I can keep the old cover and reinforce it, so that it stays the way you remember it. Or I can make it a new leather one, which will be more durable but will lose a little of its old character. The first costs about forty euros, the second around seventy."),
  L("Βιβλιοδέτης", "m", "Εγώ, προσωπικά, θα κρατούσα το παλιό, γιατί έχει και την υπογραφή του παππού σας στο εσωτερικό. Πείτε μου τι αποφασίζετε, και σε δέκα μέρες περίπου θα είναι έτοιμο. Το τηλέφωνο του μαγαζιού το έχετε. Καλή συνέχεια!", "Personally, I would keep the old one, because it also has your grandfather's signature on the inside. Tell me what you decide, and in about ten days it will be ready. You have the shop's number. Have a good day!"),
 ],
 "questions": [
  Q("Ποιο είναι κυρίως το πρόβλημα του βιβλίου;", ["Το χαρτί έχει κιτρινίσει", "Λείπουν σελίδες", "Έχει μουχλιάσει", "Η ράχη έχει ξεκολλήσει"], 3, "το πρόβλημα είναι κυρίως η ράχη, που έχει ξεκολλήσει"),
  Q("Τι θα κερδίσει ο πελάτης με το καινούργιο δερμάτινο εξώφυλλο;", ["Θα είναι πιο ανθεκτικό", "Θα είναι πιο φθηνό", "Θα είναι έτοιμο πιο γρήγορα", "Θα κρατήσει την υπογραφή"], 0, "θα είναι πιο ανθεκτικό"),
  Q("Γιατί ο βιβλιοδέτης θα κρατούσε το παλιό εξώφυλλο;", ["Γιατί είναι πιο εύκολο", "Γιατί έχει την υπογραφή του παππού στο εσωτερικό", "Γιατί δεν έχει δέρμα", "Γιατί ο πελάτης βιάζεται"], 1, "έχει και την υπογραφή του παππού σας στο εσωτερικό"),
 ],
 "gloss": {"βιβλιοδετείο": "βιβλιοδετείο — bookbindery", "λεξικό": "λεξικό — dictionary", "ράχη": "ράχη — spine (of a book)", "ξεκολλήσει": "ξεκολλάω — to come unstuck", "σκιστεί": "σκίζομαι — to tear", "εξώφυλλο": "εξώφυλλο — cover", "ενισχύσω": "ενισχύω — to reinforce", "δερμάτινο": "δερμάτινος — leather", "ανθεκτικό": "ανθεκτικός — durable", "υπογραφή": "υπογραφή — signature"}
})
ITEMS.append({
 "id": "l99-dia-plysimo-chalion", "title": "Πλύσιμο χαλιών για τον χειμώνα", "title_en": "Carpet cleaning for the winter", "type": "dialogue", "level": "B2",
 "context_el": "Ένας άντρας τηλεφωνεί σε ένα κατάστημα που καθαρίζει χαλιά, για να ρωτήσει πώς λειτουργεί η υπηρεσία.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Θα ήθελα να στείλω τα χαλιά μου για πλύσιμο. Είναι τρία: δύο μεγάλα του σαλονιού κι ένα μικρό, μάλλινο, χειροποίητο, από τη γιαγιά μου.", "Good morning. I'd like to send my carpets for cleaning. There are three: two large ones from the living room and a small one, woollen, handmade, from my grandmother."),
  L("Υπάλληλος", "f", "Καλημέρα σας. Ερχόμαστε εμείς και τα παίρνουμε από το σπίτι σας, χωρίς χρέωση, και σας τα φέρνουμε πίσω καθαρά. Το πλύσιμο κοστίζει με το τετραγωνικό μέτρο. Για τα συνηθισμένα χαλιά είναι τέσσερα ευρώ το μέτρο.", "Good morning. We come and collect them from your home, free of charge, and bring them back to you clean. Cleaning is priced per square metre. For ordinary carpets it's four euros per metre."),
  L("Πελάτης", "m", "Και το χειροποίητο; Φοβάμαι λίγο μήπως ξεβάψει.", "And the handmade one? I'm a bit afraid it might lose its colour."),
  L("Υπάλληλος", "f", "Τα χειροποίητα και τα μάλλινα τα πλένουμε χωριστά, στο χέρι, με ειδικά απορρυπαντικά, και πριν ξεκινήσουμε κάνουμε δοκιμή σε μια γωνία για τα χρώματα. Κοστίζει λίγο παραπάνω, έξι ευρώ το μέτρο, αλλά δεν διατρέχει κανέναν κίνδυνο.", "We wash handmade and woollen carpets separately, by hand, with special detergents, and before we start we test the colours on a corner. It costs a bit more, six euros per metre, but it runs no risk at all."),
  L("Πελάτης", "m", "Πόσο θα κάνουν να έρθουν πίσω;", "How long will it take for them to come back?"),
  L("Υπάλληλος", "f", "Τώρα, τον Οκτώβριο, έχουμε πολλή δουλειά, γιατί όλοι στρώνουν τα χαλιά τους για τον χειμώνα. Υπολογίστε δύο εβδομάδες. Αν θέλετε, μπορούμε να τα κρατήσουμε και να σας τα φέρουμε όποτε μας πείτε, χωρίς επιπλέον κόστος για τον πρώτο μήνα.", "Now, in October, we're very busy, because everyone is putting down their carpets for the winter. Allow two weeks. If you like, we can keep them and bring them to you whenever you tell us, at no extra cost for the first month."),
 ],
 "questions": [
  Q("Πόσο χρεώνεται η παραλαβή από το σπίτι;", ["Δέκα ευρώ", "Τέσσερα ευρώ", "Τίποτα", "Εξαρτάται από την απόσταση"], 2, "χωρίς χρέωση"),
  Q("Τι κάνουν πριν πλύνουν ένα χειροποίητο χαλί;", ["Δοκιμή σε μια γωνία για τα χρώματα", "Το φωτογραφίζουν", "Το μετρούν δύο φορές", "Το αφήνουν μια μέρα στον ήλιο"], 0, "κάνουμε δοκιμή σε μια γωνία για τα χρώματα"),
  Q("Γιατί έχουν πολλή δουλειά τον Οκτώβριο;", ["Γιατί έχουν λιγότερο προσωπικό", "Γιατί όλοι στρώνουν τα χαλιά τους για τον χειμώνα", "Γιατί κάνουν εκπτώσεις", "Γιατί βρέχει πολύ"], 1, "όλοι στρώνουν τα χαλιά τους για τον χειμώνα"),
 ],
 "gloss": {"χαλιά": "χαλί — carpet, rug", "μάλλινο": "μάλλινος — woollen", "χειροποίητο": "χειροποίητος — handmade", "χρέωση": "χρέωση — charge", "τετραγωνικό": "τετραγωνικό μέτρο — square metre", "ξεβάψει": "ξεβάφω — to lose colour, run", "απορρυπαντικά": "απορρυπαντικό — detergent", "διατρέχει": "διατρέχω κίνδυνο — to run a risk", "στρώνουν": "στρώνω — to lay (a carpet)", "επιπλέον": "επιπλέον — extra"}
})
ITEMS.append({
 "id": "l99-int-daskala-nosokomeiou", "title": "Δασκάλα σε σχολείο νοσοκομείου", "title_en": "A teacher at a hospital school", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή για την εκπαίδευση, μια δημοσιογράφος μιλά με μια δασκάλα που διδάσκει σε ένα σχολείο μέσα σε νοσοκομείο παίδων.",
 "script": [
  L("Δημοσιογράφος", "f", "Κυρία Παπαδάκη, πώς είναι ένα σχολείο μέσα σε νοσοκομείο;", "Mrs Papadaki, what is a school inside a hospital like?"),
  L("Δασκάλα", "f", "Είναι μια μικρή τάξη στον τρίτο όροφο, με πολύχρωμους τοίχους και λίγα θρανία. Έρχονται παιδιά που νοσηλεύονται για εβδομάδες ή και μήνες, ώστε να μη χάσουν τη χρονιά τους. Όσα δεν μπορούν να σηκωθούν από το κρεβάτι, τα επισκέπτομαι εγώ στον θάλαμο.", "It's a small classroom on the third floor, with colourful walls and a few desks. Children who are in hospital for weeks or even months come, so that they don't lose their school year. Those who can't get out of bed, I visit in the ward myself."),
  L("Δημοσιογράφος", "f", "Τι είναι το πιο δύσκολο σε αυτή τη δουλειά;", "What is the hardest thing in this job?"),
  L("Δασκάλα", "f", "Ότι δεν ξέρεις ποτέ τι σε περιμένει. Ένα παιδί μπορεί να έχει διάθεση να λύσει ασκήσεις τη Δευτέρα και την Τρίτη να είναι πολύ κουρασμένο από τη θεραπεία. Πρέπει να προσαρμόζεις το μάθημα κάθε μέρα, σχεδόν κάθε ώρα. Και, βέβαια, συνεργάζομαι στενά με τους γιατρούς και με τα σχολεία των παιδιών, για να ξέρουμε τι ύλη έχουν.", "That you never know what's waiting for you. A child may feel like doing exercises on Monday and on Tuesday be very tired from the treatment. You have to adapt the lesson every day, almost every hour. And of course I work closely with the doctors and with the children's schools, so we know what material they're covering."),
  L("Δημοσιογράφος", "f", "Και το πιο όμορφο;", "And the most beautiful thing?"),
  L("Δασκάλα", "f", "Όταν ένα παιδί μού λέει ότι στο μάθημα ξεχνάει ότι είναι άρρωστο. Για εκείνη την ώρα, δεν είναι ασθενής, είναι μαθητής. Αυτό, πιστεύω, το βοηθά να κρατήσει μια κανονικότητα, και τους γονείς να ελπίζουν.", "When a child tells me that in class it forgets it is ill. For that hour, it isn't a patient, it's a pupil. That, I believe, helps it keep a sense of normality, and the parents to hope."),
 ],
 "questions": [
  Q("Τι κάνει η δασκάλα με τα παιδιά που δεν μπορούν να σηκωθούν;", ["Τους στέλνει ασκήσεις με email", "Τα επισκέπτεται στον θάλαμο", "Τους δίνει άδεια από το μάθημα", "Τα φέρνει στην τάξη με αναπηρικό αμαξίδιο"], 1, "τα επισκέπτομαι εγώ στον θάλαμο"),
  Q("Γιατί πρέπει να προσαρμόζει συνεχώς το μάθημα;", ["Γιατί αλλάζουν τα βιβλία", "Γιατί η κατάσταση των παιδιών αλλάζει από μέρα σε μέρα", "Γιατί οι γονείς το ζητούν", "Γιατί η τάξη είναι πολύ μικρή"], 1, "Πρέπει να προσαρμόζεις το μάθημα κάθε μέρα"),
  Q("Ποιο είναι, για εκείνη, το πιο όμορφο;", ["Όταν ένα παιδί λέει ότι στο μάθημα ξεχνά ότι είναι άρρωστο", "Οι διακοπές του καλοκαιριού", "Οι καλοί βαθμοί", "Τα δώρα των γονιών"], 0, "στο μάθημα ξεχνάει ότι είναι άρρωστο"),
 ],
 "gloss": {"θρανία": "θρανίο — school desk", "νοσηλεύονται": "νοσηλεύομαι — to be in hospital", "θάλαμο": "θάλαμος — (hospital) ward", "θεραπεία": "θεραπεία — treatment", "προσαρμόζεις": "προσαρμόζω — to adapt", "στενά": "στενά — closely", "ύλη": "ύλη — (course) material", "ασθενής": "ασθενής — patient", "κανονικότητα": "κανονικότητα — normality"}
})
ITEMS.append({
 "id": "l99-rep-kiniti-vivliothiki", "title": "Μια βιβλιοθήκη πάνω σε ρόδες", "title_en": "A library on wheels", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε έναν τοπικό ραδιοφωνικό σταθμό για ένα λεωφορείο που μεταφέρει βιβλία στα χωριά.",
 "script": [
  L("Ρεπόρτερ", "f", "Κάθε Τρίτη πρωί, ένα παλιό λεωφορείο, βαμμένο πράσινο και κίτρινο, ξεκινά από την πρωτεύουσα του νομού και ανεβαίνει στα ορεινά χωριά. Μέσα δεν έχει καθίσματα, αλλά ράφια με περίπου δύο χιλιάδες βιβλία. Είναι η κινητή βιβλιοθήκη της δημοτικής βιβλιοθήκης, που επισκέπτεται δώδεκα χωριά, όπου δεν υπάρχει ούτε βιβλιοπωλείο ούτε βιβλιοθήκη.", "Every Tuesday morning, an old bus, painted green and yellow, sets off from the capital of the prefecture and climbs up to the mountain villages. Inside it has no seats, but shelves with about two thousand books. It is the mobile library of the municipal library, which visits twelve villages where there is neither a bookshop nor a library."),
  L("Ρεπόρτερ", "f", "Ο οδηγός, που είναι ταυτόχρονα και βιβλιοθηκονόμος, σταματά στην πλατεία κάθε χωριού για μία ώρα. Οι κάτοικοι δανείζονται βιβλία για τρεις εβδομάδες, μέχρι την επόμενη επίσκεψη. Οι πιο πιστοί αναγνώστες, λέει, είναι οι ηλικιωμένες γυναίκες και τα παιδιά του δημοτικού, ενώ οι άντρες προτιμούν τις εφημερίδες και τα βιβλία ιστορίας.", "The driver, who is at the same time the librarian, stops in the square of each village for one hour. Residents borrow books for three weeks, until the next visit. The most loyal readers, he says, are the elderly women and the primary school children, while the men prefer newspapers and history books."),
  L("Ρεπόρτερ", "f", "Η κινητή βιβλιοθήκη έγινε και σημείο συνάντησης. Οι κάτοικοι κανονίζουν να βρεθούν την ώρα που φτάνει, για έναν καφέ και μια κουβέντα. Το επόμενο βήμα, σύμφωνα με τον δήμο, είναι να εξοπλιστεί το λεωφορείο με υπολογιστή και ίντερνετ, ώστε οι κάτοικοι να μπορούν να εξυπηρετούνται και για απλές υποθέσεις με το δημόσιο.", "The mobile library has also become a meeting point. Residents arrange to meet at the time it arrives, for a coffee and a chat. The next step, according to the municipality, is to equip the bus with a computer and internet, so that residents can also get help with simple dealings with public services."),
 ],
 "questions": [
  Q("Τι υπάρχει μέσα στο λεωφορείο;", ["Καθίσματα για επιβάτες", "Ράφια με περίπου δύο χιλιάδες βιβλία", "Ένα μικρό καφενείο", "Υπολογιστές για τα παιδιά"], 1, "ράφια με περίπου δύο χιλιάδες βιβλία"),
  Q("Για πόσο καιρό δανείζονται τα βιβλία οι κάτοικοι;", ["Για μία εβδομάδα", "Για έναν μήνα", "Για τρεις εβδομάδες", "Για όσο θέλουν"], 2, "δανείζονται βιβλία για τρεις εβδομάδες"),
  Q("Ποιο είναι το επόμενο σχέδιο του δήμου;", ["Να εξοπλίσει το λεωφορείο με υπολογιστή και ίντερνετ", "Να αγοράσει δεύτερο λεωφορείο", "Να ανοίξει βιβλιοπωλείο σε κάθε χωριό", "Να καταργήσει την υπηρεσία"], 0, "να εξοπλιστεί το λεωφορείο με υπολογιστή και ίντερνετ"),
 ],
 "gloss": {"νομού": "νομός — prefecture", "ορεινά": "ορεινός — mountain (adj.)", "ράφια": "ράφι — shelf", "κινητή": "κινητός — mobile", "βιβλιοθηκονόμος": "βιβλιοθηκονόμος — librarian", "δανείζονται": "δανείζομαι — to borrow", "πιστοί": "πιστός — loyal", "εξοπλιστεί": "εξοπλίζω — to equip", "υποθέσεις": "υπόθεση — matter, business"}
})
ITEMS.append({
 "id": "l99-rep-prasines-taratses", "title": "Πράσινες ταράτσες για πιο δροσερή πόλη", "title_en": "Green roofs for a cooler city", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για το περιβάλλον σχετικά με ένα πρόγραμμα ενός δήμου.",
 "script": [
  L("Ρεπόρτερ", "m", "Τα καλοκαίρια στις ελληνικές πόλεις γίνονται όλο και πιο ζεστά, και το τσιμέντο των πολυκατοικιών αποθηκεύει τη ζέστη της μέρας και την αποδίδει τη νύχτα. Ένας δήμος της Αττικής προσπαθεί να το αλλάξει με ένα πρόγραμμα που επιδοτεί τις λεγόμενες «πράσινες ταράτσες»: ταράτσες καλυμμένες με χώμα και φυτά.", "Summers in Greek cities are getting hotter and hotter, and the concrete of apartment blocks stores the heat of the day and gives it off at night. A municipality in Attica is trying to change this with a programme that subsidises so-called 'green roofs': roofs covered with soil and plants."),
  L("Ρεπόρτερ", "m", "Οι ιδιοκτήτες που συμμετέχουν παίρνουν επιδότηση για ένα μέρος του κόστους, με την προϋπόθεση ότι ένας μηχανικός θα ελέγξει πρώτα αν η ταράτσα αντέχει το επιπλέον βάρος. Χρησιμοποιούνται κυρίως φυτά που χρειάζονται ελάχιστο νερό, όπως αρωματικά και παχύφυτα, ώστε η συντήρηση να είναι απλή.", "Owners who take part get a subsidy for part of the cost, on condition that an engineer first checks whether the roof can bear the extra weight. Mostly plants that need very little water are used, such as herbs and succulents, so that maintenance is simple."),
  L("Ρεπόρτερ", "m", "Οι κάτοικοι του τελευταίου ορόφου είναι οι πρώτοι που βλέπουν τη διαφορά: τα διαμερίσματά τους είναι πιο δροσερά και ο λογαριασμός του κλιματιστικού μικρότερος. Οι επιστήμονες, πάντως, τονίζουν ότι για να δροσιστεί μια ολόκληρη γειτονιά, χρειάζονται πολλές τέτοιες ταράτσες, μαζί με δέντρα στους δρόμους.", "The residents of the top floor are the first to see the difference: their flats are cooler and the air-conditioning bill smaller. Scientists, however, stress that for a whole neighbourhood to cool down, many such roofs are needed, together with trees in the streets."),
 ],
 "questions": [
  Q("Τι κάνει το τσιμέντο των πολυκατοικιών;", ["Αποθηκεύει τη ζέστη της μέρας και την αποδίδει τη νύχτα", "Κρατά την υγρασία", "Δροσίζει τα διαμερίσματα", "Απορροφά τον θόρυβο"], 0, "αποθηκεύει τη ζέστη της μέρας και την αποδίδει τη νύχτα"),
  Q("Τι πρέπει να γίνει πριν από την επιδότηση;", ["Να συμφωνήσουν όλοι οι γείτονες", "Να ελέγξει ένας μηχανικός αν η ταράτσα αντέχει το βάρος", "Να φυτευτούν δέντρα", "Να πληρωθεί όλο το κόστος"], 1, "ένας μηχανικός θα ελέγξει πρώτα αν η ταράτσα αντέχει το επιπλέον βάρος"),
  Q("Τι τονίζουν οι επιστήμονες;", ["Ότι οι πράσινες ταράτσες είναι επικίνδυνες", "Ότι αρκεί μία ταράτσα σε κάθε δρόμο", "Ότι χρειάζονται πολλές ταράτσες μαζί με δέντρα στους δρόμους", "Ότι τα κλιματιστικά είναι η μόνη λύση"], 2, "χρειάζονται πολλές τέτοιες ταράτσες, μαζί με δέντρα στους δρόμους"),
 ],
 "gloss": {"τσιμέντο": "τσιμέντο — concrete, cement", "αποθηκεύει": "αποθηκεύω — to store", "αποδίδει": "αποδίδω — to give off, release", "επιδοτεί": "επιδοτώ — to subsidise", "ταράτσες": "ταράτσα — flat roof", "προϋπόθεση": "προϋπόθεση — condition", "αρωματικά": "αρωματικά — herbs", "παχύφυτα": "παχύφυτο — succulent", "συντήρηση": "συντήρηση — maintenance", "κλιματιστικού": "κλιματιστικό — air conditioner"}
})
ITEMS.append({
 "id": "l99-mono-aimodotis", "title": "Γιατί έγινα τακτικός αιμοδότης", "title_en": "Why I became a regular blood donor", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν νεαρό άντρα να μιλά σε ένα podcast για την εμπειρία του ως αιμοδότη.",
 "script": [
  L("Γιώργος", "m", "Μέχρι τα είκοσι πέντε μου δεν είχα δώσει ποτέ αίμα. Φοβόμουν τις βελόνες και έλεγα πάντα ότι θα το κάνω «κάποια στιγμή». Ώσπου ο πατέρας ενός φίλου μου χρειάστηκε χειρουργείο, και το νοσοκομείο μάς ζήτησε να βρούμε αιμοδότες. Πήγα, έτρεμα, αλλά τελικά δεν ήταν τίποτα: ένα τσίμπημα και δέκα λεπτά ξάπλωμα.", "Until I was twenty-five I had never given blood. I was afraid of needles and always said I'd do it 'at some point'. Until a friend's father needed surgery, and the hospital asked us to find donors. I went, I was shaking, but in the end it was nothing: a prick and ten minutes lying down."),
  L("Γιώργος", "m", "Εκείνο που με εντυπωσίασε ήταν η νοσηλεύτρια, που μου εξήγησε ότι μία μόνο μονάδα αίματος μπορεί να βοηθήσει περισσότερους από έναν ασθενείς, γιατί χωρίζεται σε διαφορετικά συστατικά. Από τότε δίνω αίμα τρεις φορές τον χρόνο, όσο επιτρέπεται για τους άντρες, και έχω γραφτεί και σε μια ομάδα εθελοντών του δήμου.", "What impressed me was the nurse, who explained to me that a single unit of blood can help more than one patient, because it is separated into different components. Since then I give blood three times a year, as often as is allowed for men, and I've also joined a volunteer group of the municipality."),
  L("Γιώργος", "m", "Δεν το λέω για να παινευτώ. Το λέω γιατί ξέρω πόσοι το αναβάλλουν, όπως εγώ. Αν φοβάστε, πηγαίνετε με έναν φίλο, φάτε καλά πριν και πιείτε πολύ νερό. Και να ξέρετε ότι το κουλούρι και ο χυμός που σας δίνουν μετά είναι τα πιο νόστιμα του κόσμου.", "I'm not saying this to boast. I'm saying it because I know how many people put it off, like I did. If you're afraid, go with a friend, eat well beforehand and drink plenty of water. And know that the bread ring and juice they give you afterwards are the tastiest in the world."),
 ],
 "questions": [
  Q("Τι τον έκανε να δώσει αίμα για πρώτη φορά;", ["Μια διαφήμιση στην τηλεόραση", "Το χειρουργείο του πατέρα ενός φίλου του", "Μια εκδήλωση στο πανεπιστήμιο", "Η δική του αρρώστια"], 1, "ο πατέρας ενός φίλου μου χρειάστηκε χειρουργείο"),
  Q("Τι του εξήγησε η νοσηλεύτρια;", ["Ότι μία μονάδα αίματος μπορεί να βοηθήσει περισσότερους από έναν ασθενείς", "Ότι δεν πρέπει να φάει πριν", "Ότι μπορεί να δίνει αίμα κάθε μήνα", "Ότι το αίμα του είναι σπάνιο"], 0, "μία μόνο μονάδα αίματος μπορεί να βοηθήσει περισσότερους από έναν ασθενείς"),
  Q("Τι συμβουλεύει όσους φοβούνται;", ["Να μην κοιτάζουν τη βελόνα", "Να πάνε νωρίς το πρωί", "Να πάνε με έναν φίλο, να φάνε καλά και να πιουν πολύ νερό", "Να ρωτήσουν πρώτα τον γιατρό τους"], 2, "πηγαίνετε με έναν φίλο, φάτε καλά πριν και πιείτε πολύ νερό"),
 ],
 "gloss": {"βελόνες": "βελόνα — needle", "χειρουργείο": "χειρουργείο — surgery, operation", "αιμοδότες": "αιμοδότης — blood donor", "τσίμπημα": "τσίμπημα — prick", "νοσηλεύτρια": "νοσηλεύτρια — nurse", "μονάδα": "μονάδα — unit", "συστατικά": "συστατικό — component", "παινευτώ": "παινεύομαι — to boast", "αναβάλλουν": "αναβάλλω — to put off", "κουλούρι": "κουλούρι — bread ring"}
})
ITEMS.append({
 "id": "l99-mono-kagiak", "title": "Η πρώτη μου βόλτα με καγιάκ", "title_en": "My first kayak trip", "type": "monologue", "level": "B2",
 "context_el": "Μια γυναίκα διηγείται σε φίλους την πρώτη της εκδρομή με θαλάσσιο καγιάκ.",
 "script": [
  L("Ναταλία", "f", "Το καλοκαίρι, στη Μήλο, η αδελφή μου με έπεισε να κάνουμε μια οργανωμένη εκδρομή με καγιάκ γύρω από τις σπηλιές της νότιας ακτής. Εγώ δεν είχα κρατήσει ποτέ κουπί και φοβόμουν ότι θα αναποδογυρίσω με το πρώτο κύμα.", "In the summer, on Milos, my sister persuaded me to go on an organised kayak trip around the caves of the south coast. I had never held a paddle and was afraid I would capsize at the first wave."),
  L("Ναταλία", "f", "Ο οδηγός μας, όμως, ήταν πολύ υπομονετικός. Πριν ξεκινήσουμε, μας έδειξε στη στεριά πώς να κρατάμε το κουπί και πώς να στρίβουμε, και μας έβαλε να φορέσουμε σωσίβια. Μας εξήγησε, επίσης, ότι τα θαλάσσια καγιάκ είναι πολύ πιο σταθερά απ' όσο φαίνονται. Είχε δίκιο: μέσα σε μισή ώρα κωπηλατούσα σχεδόν κανονικά.", "Our guide, however, was very patient. Before we set off, he showed us on land how to hold the paddle and how to turn, and he made us put on life jackets. He also explained that sea kayaks are much more stable than they look. He was right: within half an hour I was paddling almost normally."),
  L("Ναταλία", "f", "Το πιο μαγικό ήταν όταν μπήκαμε σε μια σπηλιά, όπου το νερό είχε ένα απίστευτο γαλάζιο χρώμα και ακουγόταν μόνο ο ήχος των κουπιών. Γυρίσαμε το απόγευμα με καμένους ώμους και πιασμένα χέρια, αλλά ήδη σκεφτόμαστε την επόμενη εκδρομή. Μόνο που την επόμενη φορά θα βάλω περισσότερο αντηλιακό.", "The most magical part was when we went into a cave where the water had an incredible light-blue colour and you could only hear the sound of the paddles. We came back in the afternoon with sunburnt shoulders and stiff arms, but we're already thinking about the next trip. Only next time I'll put on more sunscreen."),
 ],
 "questions": [
  Q("Τι φοβόταν πριν από την εκδρομή;", ["Ότι θα χαθούν", "Ότι θα αναποδογυρίσει με το πρώτο κύμα", "Ότι θα βρέξει", "Ότι θα βαρεθεί"], 1, "φοβόμουν ότι θα αναποδογυρίσω με το πρώτο κύμα"),
  Q("Τι έκανε ο οδηγός πριν ξεκινήσουν;", ["Τους έδειξε στη στεριά πώς να κρατούν το κουπί και να στρίβουν", "Τους έδωσε φαγητό", "Τους έδειξε έναν χάρτη των σπηλιών", "Τους ζήτησε να υπογράψουν ένα συμβόλαιο"], 0, "μας έδειξε στη στεριά πώς να κρατάμε το κουπί και πώς να στρίβουμε"),
  Q("Τι θα κάνει διαφορετικά την επόμενη φορά;", ["Θα πάει μόνη της", "Θα νοικιάσει δικό της καγιάκ", "Θα βάλει περισσότερο αντηλιακό", "Θα φορέσει σωσίβιο"], 2, "θα βάλω περισσότερο αντηλιακό"),
 ],
 "gloss": {"καγιάκ": "καγιάκ — kayak", "σπηλιές": "σπηλιά — cave", "κουπί": "κουπί — paddle, oar", "αναποδογυρίσω": "αναποδογυρίζω — to capsize", "υπομονετικός": "υπομονετικός — patient", "στεριά": "στεριά — dry land", "σωσίβια": "σωσίβιο — life jacket", "σταθερά": "σταθερός — stable", "κωπηλατούσα": "κωπηλατώ — to paddle, row", "αντηλιακό": "αντηλιακό — sunscreen"}
})
ITEMS.append({
 "id": "l99-c1-kopwsi-apofaseon", "title": "Υπάρχει «κόπωση των αποφάσεων»;", "title_en": "Is there such a thing as decision fatigue?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη ψυχολογίας για το ευρύ κοινό σε ένα πολιτιστικό κέντρο.",
 "script": [
  L("Ομιλήτρια", "f", "Λέγεται συχνά ότι ορισμένοι γνωστοί επιχειρηματίες φορούν κάθε μέρα τα ίδια ρούχα, για να μη σπαταλούν ενέργεια σε ασήμαντες επιλογές. Πίσω από αυτή την ιδέα βρίσκεται η έννοια της «κόπωσης των αποφάσεων»: η υπόθεση ότι κάθε απόφαση που παίρνουμε εξαντλεί λίγο την ικανότητά μας να αποφασίζουμε σωστά, με αποτέλεσμα, προς το τέλος της μέρας, να καταφεύγουμε σε εύκολες ή παρορμητικές λύσεις.", "It is often said that some well-known business people wear the same clothes every day so as not to waste energy on trivial choices. Behind this idea lies the notion of 'decision fatigue': the hypothesis that every decision we make slightly depletes our ability to decide well, so that, towards the end of the day, we resort to easy or impulsive solutions."),
  L("Ομιλήτρια", "f", "Η πιο διάσημη απόδειξη προήλθε από μια μελέτη του 2011 για Ισραηλινούς δικαστές που αποφάσιζαν για αιτήσεις αποφυλάκισης. Οι ερευνητές παρατήρησαν ότι οι θετικές αποφάσεις ήταν πολύ συχνότερες στην αρχή κάθε συνεδρίασης, ύστερα από ένα διάλειμμα για φαγητό, και μειώνονταν δραματικά όσο περνούσε η ώρα. Το εύρημα έκανε τον γύρο του κόσμου.", "The most famous evidence came from a 2011 study of Israeli judges deciding on parole applications. The researchers observed that favourable decisions were much more frequent at the start of each session, after a food break, and fell dramatically as time went by. The finding went around the world."),
  L("Ομιλήτρια", "f", "Σύντομα, όμως, άλλοι επιστήμονες επισήμαναν ότι η σειρά των υποθέσεων δεν ήταν τυχαία: για παράδειγμα, οι κρατούμενοι χωρίς δικηγόρο εξετάζονταν συχνά στο τέλος, και οι υποθέσεις τους είχαν από μόνες τους μικρότερες πιθανότητες επιτυχίας. Παράλληλα, μεγάλες προσπάθειες να επαναληφθούν πειράματα για την «εξάντληση της θέλησης» έδωσαν πολύ ασθενέστερα αποτελέσματα από τα αρχικά.", "Soon, however, other scientists pointed out that the order of the cases was not random: for example, prisoners without a lawyer were often heard at the end, and their cases had lower chances of success in themselves. At the same time, large efforts to replicate experiments on 'ego depletion' produced much weaker results than the original ones."),
  L("Ομιλήτρια", "f", "Σημαίνει αυτό ότι η κούραση δεν επηρεάζει την κρίση μας; Όχι βέβαια. Σημαίνει ότι πρέπει να είμαστε επιφυλακτικοί με τις εντυπωσιακές ιστορίες που μοιάζουν να εξηγούν τα πάντα με έναν απλό μηχανισμό. Η πρακτική συμβουλή, πάντως, παραμένει λογική: τις σημαντικές αποφάσεις, καλύτερα να μην τις παίρνουμε πεινασμένοι και εξαντλημένοι.", "Does this mean that tiredness doesn't affect our judgement? Of course not. It means we must be cautious with impressive stories that seem to explain everything with a simple mechanism. The practical advice, though, remains sensible: important decisions are better not made when we are hungry and exhausted."),
 ],
 "questions": [
  Q("Τι υποστηρίζει η υπόθεση της «κόπωσης των αποφάσεων»;", ["Ότι οι αποφάσεις του πρωινού είναι πάντα λάθος", "Ότι κάθε απόφαση εξαντλεί λίγο την ικανότητά μας να αποφασίζουμε σωστά", "Ότι οι επιχειρηματίες αποφασίζουν καλύτερα", "Ότι τα ρούχα επηρεάζουν τη διάθεσή μας"], 1, "κάθε απόφαση που παίρνουμε εξαντλεί λίγο την ικανότητά μας να αποφασίζουμε σωστά"),
  Q("Τι παρατήρησε η μελέτη του 2011;", ["Ότι οι δικαστές αποφάσιζαν τυχαία", "Ότι οι θετικές αποφάσεις ήταν συχνότερες μετά από διάλειμμα για φαγητό", "Ότι οι γυναίκες δικαστές ήταν πιο επιεικείς", "Ότι οι αιτήσεις απορρίπτονταν πάντα το πρωί"], 1, "οι θετικές αποφάσεις ήταν πολύ συχνότερες στην αρχή κάθε συνεδρίασης"),
  Q("Ποια αδυναμία της μελέτης επισήμαναν άλλοι επιστήμονες;", ["Ότι η σειρά των υποθέσεων δεν ήταν τυχαία", "Ότι οι δικαστές ήταν πολύ λίγοι", "Ότι δεν υπήρχαν διαλείμματα", "Ότι τα στοιχεία είχαν χαθεί"], 0, "η σειρά των υποθέσεων δεν ήταν τυχαία"),
  Q("Ποιο είναι το συμπέρασμα της ομιλήτριας;", ["Η κούραση δεν επηρεάζει καθόλου την κρίση", "Πρέπει να φοράμε κάθε μέρα τα ίδια ρούχα", "Πρέπει να είμαστε επιφυλακτικοί με τις εντυπωσιακές απλές εξηγήσεις", "Οι δικαστικές αποφάσεις πρέπει να παίρνονται μόνο το πρωί"], 2, "πρέπει να είμαστε επιφυλακτικοί με τις εντυπωσιακές ιστορίες"),
 ],
 "gloss": {"σπαταλούν": "σπαταλώ — to waste", "ασήμαντες": "ασήμαντος — trivial", "κόπωσης": "κόπωση — fatigue", "εξαντλεί": "εξαντλώ — to deplete, exhaust", "παρορμητικές": "παρορμητικός — impulsive", "αποφυλάκισης": "αποφυλάκιση — release from prison, parole", "συνεδρίασης": "συνεδρίαση — session", "κρατούμενοι": "κρατούμενος — prisoner", "επισήμαναν": "επισημαίνω — to point out", "επαναληφθούν": "επαναλαμβάνομαι — to be repeated, replicated", "ασθενέστερα": "ασθενής — weak (comparative ασθενέστερος)", "επιφυλακτικοί": "επιφυλακτικός — cautious"}
})
ITEMS.append({
 "id": "l99-c1-thalamoi-antichisis", "title": "Ζούμε σε «θαλάμους αντήχησης»;", "title_en": "Do we live in echo chambers?", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για τα μέσα ενημέρωσης, ένας δημοσιογράφος συζητά με μια ερευνήτρια επικοινωνίας για την ενημέρωση στο διαδίκτυο.",
 "script": [
  L("Δημοσιογράφος", "m", "Ακούμε συνεχώς ότι στα μέσα κοινωνικής δικτύωσης ζούμε κλεισμένοι σε «θαλάμους αντήχησης», όπου βλέπουμε μόνο απόψεις που συμφωνούν με τις δικές μας. Ισχύει;", "We keep hearing that on social media we live shut up in 'echo chambers', where we only see views that agree with our own. Is that true?"),
  L("Ερευνήτρια", "f", "Εν μέρει. Οι αλγόριθμοι πράγματι μας δείχνουν περισσότερο ό,τι πιστεύουν ότι θα μας κρατήσει στην οθόνη, και αυτό συχνά σημαίνει περιεχόμενο που επιβεβαιώνει όσα ήδη πιστεύουμε. Πολλές έρευνες, ωστόσο, δείχνουν ότι οι περισσότεροι χρήστες εκτίθενται σε μεγαλύτερη ποικιλία απόψεων απ' όσο νομίζουμε. Οι πραγματικά απομονωμένες ομάδες είναι μάλλον μικρές, αν και πολύ θορυβώδεις.", "Partly. Algorithms do show us more of what they think will keep us on the screen, and that often means content that confirms what we already believe. Many studies, however, show that most users are exposed to a greater variety of views than we think. Truly isolated groups are rather small, though very noisy."),
  L("Δημοσιογράφος", "m", "Δηλαδή το πρόβλημα είναι υπερβολή;", "So the problem is an exaggeration?"),
  L("Ερευνήτρια", "f", "Θα έλεγα ότι το πρόβλημα είναι άλλο. Δεν είναι τόσο ότι δεν βλέπουμε την αντίθετη άποψη, όσο ότι τη βλέπουμε συνήθως στη χειρότερη εκδοχή της: μέσα από ένα σχόλιο που χλευάζει, ένα απόσπασμα βγαλμένο από το πλαίσιό του. Έτσι, η επαφή με τον «άλλον» δεν μας κάνει πιο ανοιχτούς, αλλά συχνά πιο καχύποπτους.", "I'd say the problem is a different one. It's not so much that we don't see the opposing view, as that we usually see it in its worst version: through a mocking comment, a quote taken out of context. So contact with the 'other side' doesn't make us more open, but often more suspicious."),
  L("Δημοσιογράφος", "m", "Τι μπορεί να κάνει ο απλός χρήστης;", "What can the ordinary user do?"),
  L("Ερευνήτρια", "f", "Να αναζητά συνειδητά την καλύτερη, όχι τη χειρότερη, εκδοχή των απόψεων με τις οποίες διαφωνεί, για παράδειγμα διαβάζοντας ένα σοβαρό άρθρο αντί για τα σχόλια από κάτω. Και να θυμάται ότι η οργή είναι το πιο αποδοτικό καύσιμο των πλατφορμών: όταν κάτι μας εξοργίζει πολύ γρήγορα, αξίζει να σταματήσουμε για ένα λεπτό πριν το μοιραστούμε.", "To consciously seek out the best, not the worst, version of the views they disagree with, for example by reading a serious article instead of the comments underneath. And to remember that anger is the platforms' most efficient fuel: when something enrages us very quickly, it's worth stopping for a minute before we share it."),
 ],
 "questions": [
  Q("Τι δείχνουν, σύμφωνα με την ερευνήτρια, πολλές έρευνες;", ["Ότι όλοι οι χρήστες ζουν σε απομονωμένες ομάδες", "Ότι οι περισσότεροι χρήστες εκτίθενται σε μεγαλύτερη ποικιλία απόψεων απ' όσο νομίζουμε", "Ότι οι αλγόριθμοι δεν παίζουν κανέναν ρόλο", "Ότι οι νέοι δεν διαβάζουν ειδήσεις"], 1, "οι περισσότεροι χρήστες εκτίθενται σε μεγαλύτερη ποικιλία απόψεων απ' όσο νομίζουμε"),
  Q("Ποιο είναι, κατά τη γνώμη της, το πραγματικό πρόβλημα;", ["Ότι βλέπουμε την αντίθετη άποψη συνήθως στη χειρότερη εκδοχή της", "Ότι δεν υπάρχουν σοβαρά άρθρα", "Ότι οι πλατφόρμες λογοκρίνουν", "Ότι οι χρήστες δεν σχολιάζουν"], 0, "τη βλέπουμε συνήθως στη χειρότερη εκδοχή της"),
  Q("Τι αποτέλεσμα έχει συχνά η επαφή με τον «άλλον»;", ["Μας κάνει πιο ανοιχτούς", "Μας αφήνει αδιάφορους", "Μας κάνει πιο καχύποπτους", "Μας κάνει να αλλάξουμε γνώμη"], 2, "συχνά πιο καχύποπτους"),
  Q("Τι συμβουλεύει όταν κάτι μας εξοργίζει πολύ γρήγορα;", ["Να το μοιραστούμε αμέσως", "Να σταματήσουμε για ένα λεπτό πριν το μοιραστούμε", "Να γράψουμε ένα σχόλιο", "Να κλείσουμε τον λογαριασμό μας"], 1, "αξίζει να σταματήσουμε για ένα λεπτό πριν το μοιραστούμε"),
 ],
 "gloss": {"θαλάμους": "θάλαμος — chamber", "αντήχησης": "αντήχηση — echo", "αλγόριθμοι": "αλγόριθμος — algorithm", "επιβεβαιώνει": "επιβεβαιώνω — to confirm", "εκτίθενται": "εκτίθεμαι — to be exposed", "θορυβώδεις": "θορυβώδης — noisy", "χλευάζει": "χλευάζω — to mock", "πλαίσιό": "πλαίσιο — context", "καχύποπτους": "καχύποπτος — suspicious", "συνειδητά": "συνειδητά — consciously", "αποδοτικό": "αποδοτικός — efficient", "εξοργίζει": "εξοργίζω — to enrage"}
})

rnd = random.Random(99)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-99.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
