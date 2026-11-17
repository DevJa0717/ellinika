# Source for library/listening/listening-95.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l95.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l95-ann-paros", "title": "Φτάνουμε στην Πάρο", "title_en": "Arriving in Paros", "type": "announcement", "level": "B2",
 "context_el": "Ταξιδεύετε με πλοίο από τον Πειραιά προς τις Κυκλάδες. Ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνήτρια", "f", "Κυρίες και κύριοι, σε δεκαπέντε λεπτά περίπου θα φτάσουμε στο λιμάνι της Παροικιάς, στην Πάρο. Παρακαλούνται οι επιβάτες που αποβιβάζονται στην Πάρο να ετοιμάσουν τις αποσκευές τους και να μην αφήσουν τίποτα στα καθίσματα.", "Ladies and gentlemen, in about fifteen minutes we will arrive at the port of Paroikia on Paros. Passengers disembarking at Paros are asked to get their luggage ready and not to leave anything on the seats."),
  L("Εκφωνήτρια", "f", "Οι οδηγοί οχημάτων παρακαλούνται να κατέβουν στο γκαράζ μόνο όταν ακούσουν τη σχετική ανακοίνωση, και όχι νωρίτερα, για λόγους ασφαλείας. Οι πεζοί επιβάτες θα αποβιβαστούν από την πλαϊνή έξοδο του τρίτου καταστρώματος, και όχι από τον καταπέλτη.", "Vehicle drivers are asked to go down to the car deck only when they hear the relevant announcement, and not earlier, for safety reasons. Foot passengers will disembark through the side exit on the third deck, not via the ramp."),
  L("Εκφωνήτρια", "f", "Οι επιβάτες που συνεχίζουν για Νάξο και Αμοργό παρακαλούνται να παραμείνουν στις θέσεις τους. Το πλοίο θα παραμείνει στο λιμάνι για είκοσι λεπτά. Υπενθυμίζουμε ότι το εστιατόριο θα κλείσει κατά τη διάρκεια της παραμονής μας στην Πάρο. Ευχαριστούμε που ταξιδέψατε μαζί μας.", "Passengers continuing to Naxos and Amorgos are asked to remain in their seats. The ship will stay in port for twenty minutes. We remind you that the restaurant will close during our stay in Paros. Thank you for travelling with us."),
 ],
 "questions": [
  Q("Πότε πρέπει να κατέβουν οι οδηγοί στο γκαράζ;", ["Αμέσως", "Όταν ακούσουν τη σχετική ανακοίνωση", "Μετά τους πεζούς", "Όταν δέσει το πλοίο"], 1, "να κατέβουν στο γκαράζ μόνο όταν ακούσουν τη σχετική ανακοίνωση"),
  Q("Από πού θα αποβιβαστούν οι πεζοί επιβάτες;", ["Από τον καταπέλτη", "Από το γκαράζ", "Από την πλαϊνή έξοδο του τρίτου καταστρώματος", "Από την πλώρη"], 2, "θα αποβιβαστούν από την πλαϊνή έξοδο του τρίτου καταστρώματος"),
  Q("Τι θα γίνει όσο το πλοίο μένει στην Πάρο;", ["Θα κλείσει το εστιατόριο", "Θα γίνει έλεγχος εισιτηρίων", "Θα ανοίξει το κατάστημα", "Θα αλλάξει το πλήρωμα"], 0, "το εστιατόριο θα κλείσει κατά τη διάρκεια της παραμονής μας στην Πάρο"),
 ],
 "gloss": {"μεγάφωνα": "μεγάφωνο — loudspeaker", "αποβιβάζονται": "αποβιβάζομαι — to disembark", "αποσκευές": "αποσκευές — luggage", "οχημάτων": "όχημα — vehicle", "γκαράζ": "γκαράζ — garage, car deck", "πεζοί": "πεζός — on foot, pedestrian", "καταστρώματος": "κατάστρωμα — deck", "καταπέλτη": "καταπέλτης — (ship's) ramp", "παραμείνουν": "παραμένω — to remain", "παραμονής": "παραμονή — stay"}
})
ITEMS.append({
 "id": "l95-vm-trakarisma", "title": "Ένα σημείωμα στο παρμπρίζ", "title_en": "A note on the windscreen", "type": "voicemail", "level": "B2",
 "context_el": "Βρήκατε ένα σημείωμα με ένα τηλέφωνο στο παρμπρίζ του αυτοκινήτου σας και τηλεφωνήσατε. Κανείς δεν απάντησε. Λίγο αργότερα ακούτε αυτό το μήνυμα.",
 "script": [
  L("Οδηγός", "m", "Καλησπέρα, Αντώνης Δημάκης εδώ, είδα ότι με πήρατε. Εγώ σας άφησα το σημείωμα. Σήμερα το πρωί, στο πάρκινγκ του σούπερ μάρκετ, έκανα όπισθεν και ακούμπησα τον μπροστινό σας προφυλακτήρα. Ζητώ συγγνώμη, ήταν εντελώς δικό μου λάθος.", "Good afternoon, Antonis Dimakis here, I saw you called me. I'm the one who left you the note. This morning, in the supermarket car park, I was reversing and touched your front bumper. I apologise; it was entirely my fault."),
  L("Οδηγός", "m", "Η ζημιά δεν είναι μεγάλη, μια γρατζουνιά και ένα μικρό βαθούλωμα, αλλά φυσικά θέλω να την πληρώσω. Έχουμε δύο λύσεις: ή να συμπληρώσουμε μαζί το δελτίο φιλικού διακανονισμού, για να πληρώσει η ασφαλιστική μου, ή, αν προτιμάτε, να το πάτε σε ένα συνεργείο της επιλογής σας και να σας δώσω τα χρήματα απευθείας.", "The damage isn't big, a scratch and a small dent, but of course I want to pay for it. There are two options: either we fill in the accident report form together so that my insurer pays, or, if you prefer, you take it to a garage of your choice and I give you the money directly."),
  L("Οδηγός", "m", "Εγώ θα πρότεινα το δεύτερο, γιατί είναι πιο γρήγορο και δεν θα χάσω την έκπτωση που έχω στην ασφάλεια. Πάρτε με όποτε μπορείτε, εκτός από τις δύο με τέσσερις, που είμαι σε μάθημα. Και πάλι συγγνώμη για την ταλαιπωρία.", "I'd suggest the second, because it's quicker and I won't lose the discount I have on my insurance. Call me whenever you can, except between two and four, when I'm in a lesson. Sorry again for the trouble."),
 ],
 "questions": [
  Q("Τι έπαθε το αυτοκίνητο;", ["Έσπασε ο καθρέφτης", "Γρατζουνίστηκε και βαθούλωσε λίγο ο μπροστινός προφυλακτήρας", "Έσπασε το παρμπρίζ", "Έσκασε ένα λάστιχο"], 1, "μια γρατζουνιά και ένα μικρό βαθούλωμα"),
  Q("Ποια λύση προτιμά ο οδηγός;", ["Να πληρώσει η ασφαλιστική του", "Να πάνε στην αστυνομία", "Να πληρώσει ο ίδιος απευθείας το συνεργείο", "Να το επισκευάσει ο ίδιος"], 2, "Εγώ θα πρότεινα το δεύτερο"),
  Q("Πότε δεν μπορεί να του τηλεφωνήσει;", ["Το πρωί", "Από τις δύο ως τις τέσσερις", "Μετά τις οχτώ", "Το Σαββατοκύριακο"], 1, "εκτός από τις δύο με τέσσερις, που είμαι σε μάθημα"),
 ],
 "gloss": {"σημείωμα": "σημείωμα — note", "παρμπρίζ": "παρμπρίζ — windscreen", "όπισθεν": "κάνω όπισθεν — to reverse", "ακούμπησα": "ακουμπάω — to touch, brush against", "προφυλακτήρα": "προφυλακτήρας — bumper", "γρατζουνιά": "γρατζουνιά — scratch", "βαθούλωμα": "βαθούλωμα — dent", "φιλικού διακανονισμού": "δελτίο φιλικού διακανονισμού — accident report form (for an amicable settlement)", "ασφαλιστική": "ασφαλιστική (εταιρεία) — insurance company", "συνεργείο": "συνεργείο — (car) repair shop", "ταλαιπωρία": "ταλαιπωρία — inconvenience, trouble"}
})
ITEMS.append({
 "id": "l95-dia-epistrofi-poulover", "title": "Επιστροφή ενός πουλόβερ", "title_en": "Returning a jumper", "type": "dialogue", "level": "B2",
 "context_el": "Μια γυναίκα θέλει να επιστρέψει ένα πουλόβερ σε ένα κατάστημα ρούχων.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Θα ήθελα να επιστρέψω αυτό το πουλόβερ. Το πήρα δώρο στον άντρα μου, αλλά του είναι στενό στους ώμους.", "Good morning. I'd like to return this jumper. I bought it as a present for my husband, but it's tight on the shoulders."),
  L("Πωλήτρια", "f", "Βεβαίως. Έχετε την απόδειξη; Και έχει περάσει λιγότερο από ένας μήνας από την αγορά;", "Of course. Do you have the receipt? And has it been less than a month since you bought it?"),
  L("Πελάτισσα", "f", "Ναι, να η απόδειξη, το πήρα πριν από δύο εβδομάδες. Τα καρτελάκια είναι ακόμα πάνω. Μπορώ να πάρω πίσω τα χρήματά μου;", "Yes, here's the receipt; I bought it two weeks ago. The tags are still on. Can I get my money back?"),
  L("Πωλήτρια", "f", "Δυστυχώς, επειδή ήταν σε προσφορά, δεν μπορούμε να επιστρέψουμε χρήματα. Μπορείτε, όμως, να το αλλάξετε με ένα άλλο νούμερο ή να πάρετε ένα πιστωτικό σημείωμα, που ισχύει για έξι μήνες σε όλα τα καταστήματά μας.", "Unfortunately, because it was on offer, we can't refund the money. You can, however, exchange it for another size or take a credit note, which is valid for six months in all our shops."),
  L("Πελάτισσα", "f", "Τότε ας το αλλάξω. Έχετε το ίδιο σε λάρτζ;", "Then I'll exchange it. Do you have the same in large?"),
  L("Πωλήτρια", "f", "Στο γκρι δεν μας έχει μείνει, μόνο στο μπλε σκούρο. Αν θέλετε το γκρι, μπορώ να το παραγγείλω από άλλο κατάστημα και θα έρθει σε τρεις με τέσσερις μέρες. Θα σας στείλουμε μήνυμα μόλις φτάσει.", "We don't have any left in grey, only in navy. If you want the grey, I can order it from another shop and it'll arrive in three to four days. We'll send you a message as soon as it arrives."),
 ],
 "questions": [
  Q("Γιατί θέλει να επιστρέψει το πουλόβερ;", ["Δεν του αρέσει το χρώμα", "Είναι στενό στους ώμους", "Είναι ελαττωματικό", "Είναι πολύ ακριβό"], 1, "του είναι στενό στους ώμους"),
  Q("Γιατί δεν μπορεί να πάρει πίσω τα χρήματά της;", ["Γιατί έχασε την απόδειξη", "Γιατί πέρασε ο μήνας", "Γιατί το πουλόβερ ήταν σε προσφορά", "Γιατί έβγαλε τα καρτελάκια"], 2, "επειδή ήταν σε προσφορά, δεν μπορούμε να επιστρέψουμε χρήματα"),
  Q("Τι θα γίνει αν θέλει το γκρι πουλόβερ;", ["Θα το παραγγείλουν από άλλο κατάστημα", "Θα πρέπει να γυρίσει του χρόνου", "Θα της δώσουν το μπλε σκούρο", "Θα πάρει έκπτωση"], 0, "μπορώ να το παραγγείλω από άλλο κατάστημα"),
 ],
 "gloss": {"επιστρέψω": "επιστρέφω — to return", "πουλόβερ": "πουλόβερ — jumper, sweater", "ώμους": "ώμος — shoulder", "απόδειξη": "απόδειξη — receipt", "καρτελάκια": "καρτελάκι — (price) tag", "προσφορά": "σε προσφορά — on offer", "νούμερο": "νούμερο — size", "πιστωτικό σημείωμα": "πιστωτικό σημείωμα — credit note", "ισχύει": "ισχύω — to be valid", "παραγγείλω": "παραγγέλνω — to order"}
})
ITEMS.append({
 "id": "l95-int-mastoras-petras", "title": "Ένας μάστορας της πέτρας", "title_en": "A master stonemason", "type": "interview", "level": "B2",
 "context_el": "Σε μια εκπομπή για την παραδοσιακή αρχιτεκτονική, ένας δημοσιογράφος μιλά με έναν πετρά από τα Ζαγοροχώρια.",
 "script": [
  L("Δημοσιογράφος", "m", "Τα χωριά του Ζαγορίου είναι γνωστά για τα πέτρινα σπίτια και τα γεφύρια τους. Εσείς συνεχίζετε αυτή την παράδοση. Πώς ξεκινήσατε;", "The villages of Zagori are known for their stone houses and bridges. You carry on this tradition. How did you start?"),
  L("Πετράς", "m", "Στα δεκαέξι μου άρχισα να δουλεύω βοηθός σε έναν παλιό μάστορα από το χωριό μου. Τα πρώτα δύο χρόνια δεν με άφηνε να αγγίξω το σφυρί· κουβαλούσα πέτρες και κοίταζα. Έλεγε ότι πρώτα μαθαίνεις με τα μάτια και μετά με τα χέρια.", "At sixteen I started working as an assistant to an old master from my village. For the first two years he didn't let me touch the hammer; I carried stones and watched. He said you learn first with your eyes and then with your hands."),
  L("Δημοσιογράφος", "m", "Τι κάνετε σήμερα, κυρίως;", "What do you mainly do today?"),
  L("Πετράς", "m", "Κυρίως αναπαλαιώσεις. Πολλά παλιά σπίτια έχουν αγοραστεί από ανθρώπους της πόλης που θέλουν να τα κάνουν ξενώνες ή εξοχικά. Υπάρχουν αυστηροί κανόνες, γιατί τα χωριά είναι διατηρητέα: η πέτρα πρέπει να είναι ντόπια και οι στέγες να σκεπάζονται με πλάκες από σχιστόλιθο, όχι με κεραμίδια.", "Mainly restorations. Many old houses have been bought by city people who want to turn them into guesthouses or holiday homes. There are strict rules, because the villages are listed: the stone must be local and the roofs must be covered with slate slabs, not tiles."),
  L("Δημοσιογράφος", "m", "Ακούσαμε ότι οι παλιοί μαστόροι είχαν και δική τους γλώσσα.", "We heard that the old master builders even had their own language."),
  L("Πετράς", "m", "Ναι, τα λεγόμενα «κουδαρίτικα». Ήταν μια κρυφή γλώσσα, για να μιλούν μεταξύ τους χωρίς να τους καταλαβαίνει ο νοικοκύρης, για παράδειγμα όταν συζητούσαν την πληρωμή. Ο δάσκαλός μου ήξερε αρκετές λέξεις. Εγώ θυμάμαι μόνο λίγες, και φοβάμαι ότι σε λίγα χρόνια δεν θα τις θυμάται κανείς.", "Yes, the so-called 'koudaritika'. It was a secret language, so that they could talk among themselves without the house owner understanding them, for example when they were discussing payment. My teacher knew quite a few words. I remember only a few, and I'm afraid that in a few years no one will remember them."),
 ],
 "questions": [
  Q("Τι έκανε ο πετράς τα πρώτα δύο χρόνια;", ["Δούλευε με το σφυρί", "Κουβαλούσε πέτρες και κοίταζε", "Σχεδίαζε σπίτια", "Πήγαινε σε σχολή"], 1, "κουβαλούσα πέτρες και κοίταζα"),
  Q("Με τι πρέπει να σκεπάζονται οι στέγες στα χωριά;", ["Με κεραμίδια", "Με ξύλο", "Με πλάκες από σχιστόλιθο", "Με τσίγκο"], 2, "οι στέγες να σκεπάζονται με πλάκες από σχιστόλιθο"),
  Q("Γιατί είχαν οι παλιοί μαστόροι μια κρυφή γλώσσα;", ["Για να μη χάνουν την παράδοση", "Για να μιλούν μεταξύ τους χωρίς να τους καταλαβαίνει ο νοικοκύρης", "Γιατί ήταν ξένοι", "Για να τραγουδούν στη δουλειά"], 1, "για να μιλούν μεταξύ τους χωρίς να τους καταλαβαίνει ο νοικοκύρης"),
 ],
 "gloss": {"μάστορα": "μάστορας — master craftsman, builder", "πετρά": "πετράς — stonemason", "γεφύρια": "γεφύρι — (stone) bridge", "σφυρί": "σφυρί — hammer", "κουβαλούσα": "κουβαλάω — to carry", "αναπαλαιώσεις": "αναπαλαίωση — restoration", "ξενώνες": "ξενώνας — guesthouse", "εξοχικά": "εξοχικό — holiday home", "διατηρητέα": "διατηρητέος — listed, protected", "σχιστόλιθο": "σχιστόλιθος — slate", "κεραμίδια": "κεραμίδι — roof tile", "νοικοκύρης": "νοικοκύρης — householder, owner"}
})
ITEMS.append({
 "id": "l95-rep-sifnos", "title": "Σίφνος, το νησί των αγγειοπλαστών", "title_en": "Sifnos, the island of potters", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια ραδιοφωνική εκπομπή για τα νησιά.",
 "script": [
  L("Ρεπόρτερ", "m", "Η Σίφνος, στις δυτικές Κυκλάδες, ήταν στην αρχαιότητα από τα πλουσιότερα νησιά του Αιγαίου, χάρη στα ορυχεία χρυσού και ασημιού της. Οι Σίφνιοι έχτισαν μάλιστα στους Δελφούς έναν από τους πιο εντυπωσιακούς θησαυρούς του ιερού, για να φυλάνε εκεί τις προσφορές τους προς τον Απόλλωνα.", "Sifnos, in the western Cyclades, was in antiquity one of the richest islands in the Aegean, thanks to its gold and silver mines. The Sifnians even built at Delphi one of the most impressive treasuries in the sanctuary, to keep their offerings to Apollo there."),
  L("Ρεπόρτερ", "m", "Σήμερα το νησί είναι γνωστό για άλλα πράγματα: για την αγγειοπλαστική του, που συνεχίζεται σε εργαστήρια στις Καμάρες και στον Πλατύ Γιαλό, και για τη μαγειρική του. Από τη Σίφνο καταγόταν ο Νικόλαος Τσελεμεντές, του οποίου το βιβλίο μαγειρικής έγινε τόσο δημοφιλές, ώστε το όνομά του κατέληξε να σημαίνει «βιβλίο συνταγών».", "Today the island is known for other things: for its pottery, which continues in workshops at Kamares and Platys Gialos, and for its cooking. Nikolaos Tselementes came from Sifnos; his cookbook became so popular that his name ended up meaning 'recipe book'."),
  L("Ρεπόρτερ", "m", "Το πιο χαρακτηριστικό φαγητό του νησιού είναι η ρεβιθάδα. Τα ρεβίθια μπαίνουν το Σάββατο το βράδυ σε ένα πήλινο σκεπαστό σκεύος, το σκεπαστάρι, και ψήνονται όλη τη νύχτα στον ξυλόφουρνο, για να φαγωθούν την Κυριακή μετά την εκκλησία. Μην παραλείψετε να επισκεφθείτε το Κάστρο, ένα μεσαιωνικό χωριό πάνω σε βράχο, και τη Χρυσοπηγή, ένα μοναστήρι χτισμένο σε μια βραχονησίδα που ενώνεται με την ακτή με μια μικρή γέφυρα.", "The island's most characteristic dish is revithada. The chickpeas go into a covered clay pot, the skepastari, on Saturday evening and bake all night in the wood oven, to be eaten on Sunday after church. Don't miss Kastro, a medieval village on a rock, and Chrysopigi, a monastery built on a rocky islet joined to the shore by a small bridge."),
 ],
 "questions": [
  Q("Γιατί ήταν πλούσια η Σίφνος στην αρχαιότητα;", ["Χάρη στο εμπόριο κρασιού", "Χάρη στα ορυχεία χρυσού και ασημιού", "Χάρη στον στόλο της", "Χάρη στην αγγειοπλαστική"], 1, "χάρη στα ορυχεία χρυσού και ασημιού της"),
  Q("Τι σημαίνει σήμερα το όνομα «Τσελεμεντές»;", ["Ένα είδος γλυκού", "Βιβλίο συνταγών", "Ένα πήλινο σκεύος", "Μάγειρας"], 1, "το όνομά του κατέληξε να σημαίνει «βιβλίο συνταγών»"),
  Q("Πώς μαγειρεύεται η ρεβιθάδα;", ["Τηγανίζεται την Κυριακή το πρωί", "Βράζει σε κατσαρόλα για μία ώρα", "Ψήνεται όλη τη νύχτα στον ξυλόφουρνο μέσα σε πήλινο σκεύος", "Ψήνεται στα κάρβουνα"], 2, "ψήνονται όλη τη νύχτα στον ξυλόφουρνο"),
 ],
 "gloss": {"ορυχεία": "ορυχείο — mine", "θησαυρούς": "θησαυρός — treasury (at a sanctuary)", "προσφορές": "προσφορά — offering", "αγγειοπλαστική": "αγγειοπλαστική — pottery", "ρεβιθάδα": "ρεβιθάδα — baked chickpea stew", "ρεβίθια": "ρεβίθι — chickpea", "πήλινο": "πήλινος — clay (adj.)", "σκεύος": "σκεύος — pot, vessel", "ξυλόφουρνο": "ξυλόφουρνος — wood-fired oven", "βραχονησίδα": "βραχονησίδα — rocky islet"}
})
ITEMS.append({
 "id": "l95-rep-naxos", "title": "Νάξος, το μεγαλύτερο νησί των Κυκλάδων", "title_en": "Naxos, the largest of the Cyclades", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ταξιδιωτικό ρεπορτάζ σε μια τηλεοπτική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "f", "Μόλις το πλοίο μπαίνει στο λιμάνι της Νάξου, το πρώτο που βλέπει κανείς είναι η Πορτάρα, μια τεράστια μαρμάρινη πύλη πάνω σε ένα νησάκι. Είναι ό,τι έχει απομείνει από έναν ναό του Απόλλωνα που άρχισε να χτίζεται τον έκτο αιώνα π.Χ. και δεν τελείωσε ποτέ. Το ηλιοβασίλεμα εκεί είναι από τα πιο φημισμένα του Αιγαίου.", "As soon as the ship enters the harbour of Naxos, the first thing you see is the Portara, a huge marble gateway on an islet. It is all that remains of a temple of Apollo that began to be built in the sixth century BC and was never finished. The sunset there is one of the most famous in the Aegean."),
  L("Ρεπόρτερ", "f", "Η Νάξος είναι το μεγαλύτερο νησί των Κυκλάδων και, σε αντίθεση με πολλά γειτονικά της, είναι πράσινη και εύφορη. Στο κέντρο της υψώνεται ο Ζας, το ψηλότερο βουνό των Κυκλάδων, λίγο πάνω από τα χίλια μέτρα. Στα ορεινά χωριά, όπως η Χαλκί και η Απείρανθος, θα δοκιμάσετε τη γραβιέρα του νησιού, τις περίφημες ναξιώτικες πατάτες και το λικέρ κίτρο.", "Naxos is the largest island in the Cyclades and, unlike many of its neighbours, it is green and fertile. In its centre rises Zas, the highest mountain in the Cyclades, just over a thousand metres. In the mountain villages, such as Chalki and Apeiranthos, you can try the island's graviera cheese, the famous Naxos potatoes and kitron liqueur."),
  L("Ρεπόρτερ", "f", "Η Νάξος ήταν στην αρχαιότητα κέντρο της γλυπτικής, χάρη στο μάρμαρό της. Στις Μέλανες και στον Απόλλωνα σώζονται ακόμα, ξαπλωμένοι στο έδαφος, τεράστιοι ημιτελείς κούροι, που δεν έφυγαν ποτέ από τα αρχαία λατομεία. Σύμφωνα με τον μύθο, εδώ ο Θησέας εγκατέλειψε την Αριάδνη, μετά τη νίκη του επί του Μινώταυρου.", "In antiquity Naxos was a centre of sculpture, thanks to its marble. At Melanes and Apollonas huge unfinished kouroi still lie on the ground; they never left the ancient quarries. According to myth, it was here that Theseus abandoned Ariadne after his victory over the Minotaur."),
 ],
 "questions": [
  Q("Τι είναι η Πορτάρα;", ["Ένα κάστρο", "Η μαρμάρινη πύλη ενός ημιτελούς ναού του Απόλλωνα", "Ένας φάρος", "Ένα μουσείο"], 1, "μια τεράστια μαρμάρινη πύλη πάνω σε ένα νησάκι. Είναι ό,τι έχει απομείνει από έναν ναό του Απόλλωνα"),
  Q("Σε τι διαφέρει η Νάξος από πολλά γειτονικά νησιά;", ["Δεν έχει παραλίες", "Είναι πράσινη και εύφορη", "Δεν έχει βουνά", "Δεν έχει λιμάνι"], 1, "είναι πράσινη και εύφορη"),
  Q("Τι σώζεται στις Μέλανες και στον Απόλλωνα;", ["Ημιτελείς κούροι ξαπλωμένοι στο έδαφος", "Ένα αρχαίο θέατρο", "Βυζαντινές εκκλησίες", "Ενετικοί πύργοι"], 0, "σώζονται ακόμα, ξαπλωμένοι στο έδαφος, τεράστιοι ημιτελείς κούροι"),
 ],
 "gloss": {"Πορτάρα": "Πορτάρα — the Portara (marble gateway on Naxos)", "πύλη": "πύλη — gateway", "ηλιοβασίλεμα": "ηλιοβασίλεμα — sunset", "εύφορη": "εύφορος — fertile", "υψώνεται": "υψώνομαι — to rise", "γραβιέρα": "γραβιέρα — graviera (hard cheese)", "γλυπτικής": "γλυπτική — sculpture", "ημιτελείς": "ημιτελής — unfinished", "κούροι": "κούρος — kouros (archaic statue of a young man)", "λατομεία": "λατομείο — quarry", "εγκατέλειψε": "εγκαταλείπω — to abandon"}
})
ITEMS.append({
 "id": "l95-mono-adeia-folia", "title": "Η άδεια φωλιά", "title_en": "The empty nest", "type": "monologue", "level": "B2",
 "context_el": "Μια μητέρα μιλά σε μια ραδιοφωνική εκπομπή για το πώς ένιωσε όταν η κόρη της έφυγε για σπουδές.",
 "script": [
  L("Μητέρα", "f", "Τον Σεπτέμβριο η κόρη μου πέρασε στο πανεπιστήμιο, στη Θεσσαλονίκη. Ήμασταν όλοι πολύ χαρούμενοι. Τη βοηθήσαμε να βρει σπίτι, ψωνίσαμε κουρτίνες και κατσαρόλες, και την τελευταία μέρα γυρίσαμε με τον άντρα μου στην Πάτρα με ένα άδειο αυτοκίνητο.", "In September my daughter got into university in Thessaloniki. We were all very happy. We helped her find a flat, bought curtains and saucepans, and on the last day my husband and I drove back to Patras with an empty car."),
  L("Μητέρα", "f", "Δεν περίμενα ότι θα ήταν τόσο δύσκολο. Το σπίτι ξαφνικά μου φαινόταν τεράστιο και ήσυχο. Το πρώτο βράδυ μαγείρεψα για τρεις, από συνήθεια. Περνούσα έξω από το δωμάτιό της και έκλεινα την πόρτα, για να μη βλέπω το άδειο κρεβάτι. Της τηλεφωνούσα κάθε μέρα, ώσπου μου είπε, πολύ ευγενικά, ότι μπορούμε να μιλάμε και κάθε δεύτερη μέρα.", "I didn't expect it to be so hard. The house suddenly seemed huge and quiet to me. The first evening I cooked for three, out of habit. I would walk past her room and close the door so as not to see the empty bed. I phoned her every day, until she told me, very politely, that we could also talk every other day."),
  L("Μητέρα", "f", "Μια φίλη μου, που το είχε περάσει, μου είπε: «Μην προσπαθείς να γεμίσεις το κενό με εκείνη· γέμισέ το με σένα». Έτσι, γράφτηκα σε ένα μάθημα κεραμικής, που το ήθελα χρόνια, και με τον άντρα μου ξαναρχίσαμε τις βόλτες μας στο κάστρο. Ακόμα μου λείπει, φυσικά. Αλλά όταν γυρίζει για τις γιορτές, έχουμε κι οι δύο πολλά να πούμε.", "A friend of mine who had been through it said to me: 'Don't try to fill the gap with her; fill it with yourself.' So I signed up for a pottery class I'd wanted for years, and my husband and I started our walks up to the castle again. I still miss her, of course. But when she comes home for the holidays, we both have a lot to tell each other."),
 ],
 "questions": [
  Q("Τι έκανε η μητέρα το πρώτο βράδυ;", ["Έκλαψε όλη τη νύχτα", "Μαγείρεψε για τρεις από συνήθεια", "Πήγε στο δωμάτιο της κόρης της", "Τηλεφώνησε στη φίλη της"], 1, "Το πρώτο βράδυ μαγείρεψα για τρεις, από συνήθεια"),
  Q("Τι της είπε η κόρη της για τα τηλεφωνήματα;", ["Ότι δεν θέλει να της τηλεφωνεί", "Ότι μπορούν να μιλάνε κάθε δεύτερη μέρα", "Ότι θα της τηλεφωνεί εκείνη", "Ότι προτιμά τα μηνύματα"], 1, "μπορούμε να μιλάμε και κάθε δεύτερη μέρα"),
  Q("Τι έκανε η μητέρα μετά τη συμβουλή της φίλης της;", ["Πήρε ένα σκύλο", "Μετακόμισε στη Θεσσαλονίκη", "Γράφτηκε σε μάθημα κεραμικής", "Βρήκε δουλειά"], 2, "γράφτηκα σε ένα μάθημα κεραμικής"),
 ],
 "gloss": {"πέρασε": "περνάω (στο πανεπιστήμιο) — to get into (university)", "κουρτίνες": "κουρτίνα — curtain", "κατσαρόλες": "κατσαρόλα — saucepan", "από συνήθεια": "από συνήθεια — out of habit", "κενό": "κενό — gap, void", "γράφτηκα": "γράφομαι — to enrol, sign up", "κεραμικής": "κεραμική — ceramics, pottery", "λείπει": "μου λείπει — I miss (him/her/it)"}
})
ITEMS.append({
 "id": "l95-mono-psychotherapeia", "title": "Πήγα σε ψυχοθεραπεύτρια", "title_en": "I went to a therapist", "type": "monologue", "level": "B2",
 "context_el": "Ένας άντρας τριάντα πέντε χρόνων μιλά σε ένα podcast για την εμπειρία του από την ψυχοθεραπεία.",
 "script": [
  L("Άντρας", "m", "Για χρόνια πίστευα ότι η ψυχοθεραπεία είναι για ανθρώπους με «σοβαρά» προβλήματα. Εγώ είχα μια καλή δουλειά, φίλους, οικογένεια. Ωστόσο, ξυπνούσα κάθε πρωί με ένα σφίξιμο στο στήθος, θύμωνα με το παραμικρό και δεν κοιμόμουν καλά.", "For years I believed therapy was for people with 'serious' problems. I had a good job, friends, family. Yet I woke every morning with a tightness in my chest, got angry at the slightest thing and didn't sleep well."),
  L("Άντρας", "m", "Η αδερφή μου ήταν αυτή που με έπεισε να κλείσω ένα ραντεβού. Την πρώτη φορά ήμουν πολύ αμήχανος· δεν ήξερα τι να πω, και φοβόμουν ότι η ψυχοθεραπεύτρια θα με κρίνει. Εκείνη, όμως, κυρίως άκουγε, και έκανε ερωτήσεις που δεν είχα κάνει ποτέ στον εαυτό μου.", "My sister was the one who persuaded me to book an appointment. The first time I was very awkward; I didn't know what to say and I was afraid the therapist would judge me. She, however, mostly listened, and asked questions I had never asked myself."),
  L("Άντρας", "m", "Πηγαίνω πια έναν χρόνο, μία φορά την εβδομάδα. Δεν άλλαξαν όλα από τη μια μέρα στην άλλη· είναι μια αργή δουλειά. Έμαθα, όμως, να καταλαβαίνω τι με αγχώνει και να το λέω, αντί να το καταπίνω. Το λέω ανοιχτά, γιατί ακόμα πολλοί άντρες ντρέπονται να ζητήσουν βοήθεια. Δεν είναι αδυναμία· είναι σαν να πηγαίνεις στον γιατρό όταν πονάει το πόδι σου.", "I've been going for a year now, once a week. Not everything changed overnight; it's slow work. But I learned to understand what stresses me and to say it, instead of swallowing it. I say this openly because many men are still ashamed to ask for help. It isn't weakness; it's like going to the doctor when your leg hurts."),
 ],
 "questions": [
  Q("Ποια συμπτώματα είχε ο άντρας;", ["Πονοκεφάλους και πυρετό", "Σφίξιμο στο στήθος, θυμό και αϋπνίες", "Πόνο στο πόδι", "Δεν είχε κανένα σύμπτωμα"], 1, "ξυπνούσα κάθε πρωί με ένα σφίξιμο στο στήθος, θύμωνα με το παραμικρό και δεν κοιμόμουν καλά"),
  Q("Ποιος τον έπεισε να κλείσει ραντεβού;", ["Ο γιατρός του", "Η αδερφή του", "Ένας φίλος", "Η γυναίκα του"], 1, "Η αδερφή μου ήταν αυτή που με έπεισε"),
  Q("Γιατί μιλάει ανοιχτά για την εμπειρία του;", ["Γιατί πολλοί άντρες ντρέπονται να ζητήσουν βοήθεια", "Γιατί είναι ψυχολόγος", "Γιατί του το ζήτησε η θεραπεύτρια", "Γιατί θέλει να γράψει βιβλίο"], 0, "γιατί ακόμα πολλοί άντρες ντρέπονται να ζητήσουν βοήθεια"),
 ],
 "gloss": {"ψυχοθεραπεύτρια": "ψυχοθεραπεύτρια — (female) therapist", "ψυχοθεραπεία": "ψυχοθεραπεία — psychotherapy", "σφίξιμο": "σφίξιμο — tightness", "με το παραμικρό": "με το παραμικρό — at the slightest thing", "έπεισε": "πείθω — to persuade", "αμήχανος": "αμήχανος — awkward, embarrassed", "κρίνει": "κρίνω — to judge", "αγχώνει": "αγχώνω — to stress, make anxious", "καταπίνω": "καταπίνω — to swallow", "ντρέπονται": "ντρέπομαι — to be ashamed", "αδυναμία": "αδυναμία — weakness"}
})
ITEMS.append({
 "id": "l95-c1-times-9-99", "title": "Γιατί όλα κοστίζουν 9,99", "title_en": "Why everything costs 9.99", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την οικονομία της καθημερινότητας, η παρουσιάστρια συζητά με έναν καθηγητή μάρκετινγκ.",
 "script": [
  L("Παρουσιάστρια", "f", "Γιατί τόσα προϊόντα κοστίζουν 9,99 και όχι 10 ευρώ; Ένα λεπτό διαφορά δεν μπορεί να έχει σημασία.", "Why do so many products cost 9.99 and not 10 euros? A one-cent difference can't matter."),
  L("Καθηγητής", "m", "Κι όμως, έχει. Διαβάζουμε τους αριθμούς από τα αριστερά προς τα δεξιά, και το πρώτο ψηφίο επηρεάζει δυσανάλογα την εκτίμησή μας. Το 9,99 το κατατάσσουμε ασυναίσθητα στα «εννιά κάτι», όχι στα δέκα. Οι ερευνητές το ονομάζουν «φαινόμενο του αριστερού ψηφίου». Επιπλέον, οι τιμές που λήγουν σε 9 έχουν συνδεθεί στο μυαλό μας με τις εκπτώσεις και τις ευκαιρίες.", "And yet it does. We read numbers from left to right, and the first digit has a disproportionate influence on our estimate. We unconsciously file 9.99 under 'nine-something', not ten. Researchers call it the 'left-digit effect'. In addition, prices ending in 9 have become linked in our minds with sales and bargains."),
  L("Παρουσιάστρια", "f", "Γι’ αυτό, φαντάζομαι, τα ακριβά εστιατόρια γράφουν «25» και όχι «24,99».", "That's why, I imagine, expensive restaurants write '25' and not '24.99'."),
  L("Καθηγητής", "m", "Ακριβώς. Μια στρογγυλή τιμή εκπέμπει ποιότητα και σιγουριά, όχι ευκαιρία. Υπάρχει και ένα πιο ύπουλο τέχνασμα, το λεγόμενο «φαινόμενο του δολώματος». Ο οικονομολόγος Νταν Αριέλι περιγράφει μια συνδρομή σε περιοδικό: μόνο ηλεκτρονική έκδοση στα 59 δολάρια, μόνο έντυπη στα 125, και έντυπη μαζί με ηλεκτρονική επίσης στα 125. Κανείς σχεδόν δεν διάλεγε τη σκέτη έντυπη, αλλά η παρουσία της έκανε το πακέτο να μοιάζει ασυναγώνιστο, και οι περισσότεροι το προτιμούσαν. Όταν η επιλογή-δόλωμα αφαιρέθηκε, οι περισσότεροι διάλεξαν τη φθηνότερη ηλεκτρονική έκδοση.", "Exactly. A round price conveys quality and confidence, not a bargain. There is also a more insidious trick, the so-called 'decoy effect'. The economist Dan Ariely describes a magazine subscription: online only at 59 dollars, print only at 125, and print plus online also at 125. Almost no one chose print alone, but its presence made the bundle look unbeatable, and most people preferred it. When the decoy option was removed, most chose the cheaper online edition."),
 ],
 "questions": [
  Q("Τι είναι το «φαινόμενο του αριστερού ψηφίου»;", ["Η τάση να στρογγυλεύουμε τις τιμές προς τα πάνω", "Η τάση να επηρεάζεται δυσανάλογα η εκτίμησή μας από το πρώτο ψηφίο", "Η προτίμηση για ζυγούς αριθμούς", "Η δυσκολία να θυμόμαστε τιμές"], 1, "το πρώτο ψηφίο επηρεάζει δυσανάλογα την εκτίμησή μας"),
  Q("Γιατί τα ακριβά εστιατόρια χρησιμοποιούν στρογγυλές τιμές;", ["Για να υπολογίζεται εύκολα ο λογαριασμός", "Γιατί εκπέμπουν ποιότητα και σιγουριά", "Γιατί το απαιτεί ο νόμος", "Για να μοιάζουν φθηνότερα"], 1, "Μια στρογγυλή τιμή εκπέμπει ποιότητα και σιγουριά"),
  Q("Ποιος ήταν ο ρόλος της σκέτης έντυπης συνδρομής στο παράδειγμα του Αριέλι;", ["Ήταν η πιο δημοφιλής επιλογή", "Έκανε το πακέτο έντυπης και ηλεκτρονικής να μοιάζει ασυναγώνιστο", "Ήταν η φθηνότερη επιλογή", "Απευθυνόταν στους ηλικιωμένους"], 1, "η παρουσία της έκανε το πακέτο να μοιάζει ασυναγώνιστο"),
  Q("Τι συνέβη όταν αφαιρέθηκε η επιλογή-δόλωμα;", ["Οι περισσότεροι διάλεξαν την ηλεκτρονική έκδοση", "Οι περισσότεροι διάλεξαν το πακέτο", "Κανείς δεν αγόρασε συνδρομή", "Αυξήθηκαν οι τιμές"], 0, "οι περισσότεροι διάλεξαν τη φθηνότερη ηλεκτρονική έκδοση"),
 ],
 "gloss": {"ψηφίο": "ψηφίο — digit", "δυσανάλογα": "δυσανάλογα — disproportionately", "ασυναίσθητα": "ασυναίσθητα — unconsciously", "λήγουν": "λήγω — to end (in)", "στρογγυλή": "στρογγυλός — round", "εκπέμπει": "εκπέμπω — to emit, convey", "ύπουλο": "ύπουλος — insidious, sneaky", "τέχνασμα": "τέχνασμα — trick", "δολώματος": "δόλωμα — decoy, bait", "συνδρομή": "συνδρομή — subscription", "έντυπη": "έντυπος — printed", "ασυναγώνιστο": "ασυναγώνιστος — unbeatable"}
})
ITEMS.append({
 "id": "l95-c1-gyros", "title": "Η ιστορία του γύρου", "title_en": "The story of the gyros", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια διάλεξη για την ιστορία της ελληνικής κουζίνας σε ένα φεστιβάλ γαστρονομίας.",
 "script": [
  L("Ομιλητής", "m", "Για πολλούς ξένους, ο γύρος είναι το κατεξοχήν ελληνικό φαγητό. Κι όμως, η ιστορία του στην Ελλάδα είναι σχετικά πρόσφατη. Η τεχνική του κρέατος που ψήνεται σε κάθετη σούβλα, που γυρίζει αργά μπροστά στη φωτιά, αναπτύχθηκε στην Οθωμανική Αυτοκρατορία τον δέκατο ένατο αιώνα· στα τουρκικά λέγεται «ντονέρ», δηλαδή «αυτό που γυρίζει».", "For many foreigners, gyros is the Greek dish par excellence. And yet its history in Greece is relatively recent. The technique of meat roasted on a vertical spit that turns slowly in front of the fire developed in the Ottoman Empire in the nineteenth century; in Turkish it is called 'döner', meaning 'that which turns'."),
  L("Ομιλητής", "m", "Στην Ελλάδα το έφεραν, σύμφωνα με τις περισσότερες μαρτυρίες, πρόσφυγες από τη Μικρά Ασία και την Κωνσταντινούπολη, και διαδόθηκε κυρίως μετά τον Δεύτερο Παγκόσμιο Πόλεμο, στις δεκαετίες του πενήντα και του εξήντα. Στην αρχή ονομαζόταν κι εδώ «ντονέρ»· σταδιακά επικράτησε η ελληνική απόδοση της λέξης, ο «γύρος».", "According to most accounts, it was brought to Greece by refugees from Asia Minor and Constantinople, and it spread mainly after the Second World War, in the fifties and sixties. At first it was called 'döner' here too; gradually the Greek rendering of the word, 'gyros', prevailed."),
  L("Ομιλητής", "m", "Οι Έλληνες, πάντως, τον προσάρμοσαν στα δικά τους γούστα. Ενώ στην Τουρκία φτιάχνεται παραδοσιακά από αρνί ή μοσχάρι, στην Ελλάδα επικράτησε το χοιρινό και αργότερα το κοτόπουλο. Και, κυρίως, ο ελληνικός γύρος τυλίγεται σε πίτα με τζατζίκι, ντομάτα, κρεμμύδι και, όσο κι αν ξενίζει τους ξένους, πατάτες τηγανητές μέσα. Είναι ένα καλό παράδειγμα του πώς η κουζίνα κάθε λαού δεν είναι κάτι σταθερό, αλλά μια συνεχής συνομιλία με τους γείτονές του.", "Greeks, however, adapted it to their own tastes. While in Turkey it is traditionally made from lamb or beef, in Greece pork prevailed, and later chicken. And above all, Greek gyros is wrapped in a pitta with tzatziki, tomato, onion and, however much it surprises foreigners, chips inside. It is a good example of how every people's cuisine is not something fixed, but a continuous conversation with its neighbours."),
 ],
 "questions": [
  Q("Πού αναπτύχθηκε η τεχνική της κάθετης σούβλας;", ["Στην αρχαία Ελλάδα", "Στην Οθωμανική Αυτοκρατορία τον δέκατο ένατο αιώνα", "Στη Γερμανία", "Στο Βυζάντιο"], 1, "αναπτύχθηκε στην Οθωμανική Αυτοκρατορία τον δέκατο ένατο αιώνα"),
  Q("Ποιοι έφεραν τον γύρο στην Ελλάδα, σύμφωνα με τις περισσότερες μαρτυρίες;", ["Τουρίστες", "Έλληνες ναυτικοί", "Πρόσφυγες από τη Μικρά Ασία και την Κωνσταντινούπολη", "Γερμανοί μετανάστες"], 2, "πρόσφυγες από τη Μικρά Ασία και την Κωνσταντινούπολη"),
  Q("Ποιο κρέας επικράτησε στον ελληνικό γύρο;", ["Το αρνί", "Το μοσχάρι", "Το χοιρινό", "Το ψάρι"], 2, "στην Ελλάδα επικράτησε το χοιρινό"),
  Q("Τι θέλει να δείξει ο ομιλητής με το παράδειγμα του γύρου;", ["Ότι η ελληνική κουζίνα είναι η παλαιότερη", "Ότι η κουζίνα κάθε λαού είναι μια συνεχής συνομιλία με τους γείτονές του", "Ότι ο γύρος δεν είναι υγιεινός", "Ότι οι ξένοι δεν καταλαβαίνουν την ελληνική κουζίνα"], 1, "η κουζίνα κάθε λαού δεν είναι κάτι σταθερό, αλλά μια συνεχής συνομιλία με τους γείτονές του"),
 ],
 "gloss": {"γαστρονομίας": "γαστρονομία — gastronomy", "κατεξοχήν": "κατεξοχήν — par excellence", "κάθετη": "κάθετος — vertical", "σούβλα": "σούβλα — spit", "μαρτυρίες": "μαρτυρία — account, testimony", "διαδόθηκε": "διαδίδομαι — to spread", "απόδοση": "απόδοση — rendering, translation", "επικράτησε": "επικρατώ — to prevail", "προσάρμοσαν": "προσαρμόζω — to adapt", "τυλίγεται": "τυλίγομαι — to be wrapped", "ξενίζει": "ξενίζω — to surprise, seem strange", "συνομιλία": "συνομιλία — conversation"}
})

rnd = random.Random(95)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-95.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
