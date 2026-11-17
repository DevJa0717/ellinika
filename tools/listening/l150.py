# Source for library/listening/listening-150.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l150.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l150-vm-metakomisi", "title": "Αλλαγή στη μετακόμιση", "title_en": "A change to the move", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη μεταφορική εταιρεία που θα κάνει τη μετακόμισή σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλησπέρα σας, από τη μεταφορική εταιρεία «Ερμής» σας τηλεφωνώ, για τη μετακόμιση της Παρασκευής. Δυστυχώς ο δήμος μάς ενημέρωσε ότι εκείνη τη μέρα ο δρόμος σας θα είναι κλειστός για έργα, οπότε το φορτηγό δεν θα μπορεί να σταθμεύσει.", "Good evening, I'm calling from the Hermes removals company, about Friday's move. Unfortunately the municipality has informed us that your street will be closed for roadworks that day, so the truck won't be able to park."),
  L("Υπάλληλος", "m", "Μπορούμε να έρθουμε την Πέμπτη, στις οχτώ το πρωί, ή το Σάββατο, με μια μικρή επιβάρυνση για τη μέρα. Θα σας φέρουμε και τα χαρτόκουτα δύο μέρες νωρίτερα, όπως είχαμε συμφωνήσει.", "We can come on Thursday at eight in the morning, or on Saturday, with a small surcharge for the day. We'll also bring you the cardboard boxes two days earlier, as we had agreed."),
  L("Υπάλληλος", "m", "Σας παρακαλώ, μην ξεχάσετε να αδειάσετε το ψυγείο και να το αποσυνδέσετε από το ρεύμα το προηγούμενο βράδυ. Περιμένω το τηλεφώνημά σας μέχρι αύριο το απόγευμα.", "Please don't forget to empty the fridge and unplug it the night before. I'll wait for your call until tomorrow afternoon."),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί να γίνει η μετακόμιση την Παρασκευή;", ["Γιατί το φορτηγό χάλασε", "Γιατί ο δρόμος θα είναι κλειστός για έργα", "Γιατί είναι αργία", "Γιατί δεν υπάρχουν εργάτες"], 1, "ο δρόμος σας θα είναι κλειστός για έργα"),
  Q("Τι ισχύει για το Σάββατο;", ["Είναι δωρεάν", "Δεν δουλεύουν", "Υπάρχει μια μικρή επιβάρυνση", "Έρχονται μόνο το απόγευμα"], 2, "με μια μικρή επιβάρυνση για τη μέρα"),
  Q("Τι πρέπει να κάνετε το προηγούμενο βράδυ;", ["Να αδειάσετε και να αποσυνδέσετε το ψυγείο", "Να πληρώσετε την προκαταβολή", "Να ενημερώσετε τον δήμο", "Να πακετάρετε τα βιβλία"], 0, "να αδειάσετε το ψυγείο και να το αποσυνδέσετε από το ρεύμα"),
 ],
 "gloss": {"μεταφορική εταιρεία": "μεταφορική εταιρεία — removals company", "μετακόμιση": "μετακόμιση — move (house)", "έργα": "έργα — roadworks", "σταθμεύσει": "σταθμεύω — to park", "επιβάρυνση": "επιβάρυνση — surcharge", "χαρτόκουτα": "χαρτόκουτο — cardboard box", "αδειάσετε": "αδειάζω — to empty", "αποσυνδέσετε": "αποσυνδέω — to disconnect, unplug"}
})

ITEMS.append({
 "id": "l150-ann-gioga-parko", "title": "Γιόγκα στο πάρκο", "title_en": "Yoga in the park", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου στο τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος ξεκινά και φέτος το καλοκαιρινό πρόγραμμα «Αθλητισμός για όλους». Κάθε Τρίτη και Πέμπτη, στις επτά το πρωί, θα γίνονται δωρεάν μαθήματα γιόγκα στο μεγάλο πάρκο, δίπλα στη λίμνη.", "Once again this year the municipality is starting its summer programme 'Sport for All'. Every Tuesday and Thursday at seven in the morning there will be free yoga classes in the big park, next to the lake."),
  L("Εκφωνήτρια", "f", "Τα μαθήματα είναι κατάλληλα και για αρχάριους, και θα τα διδάσκουν πιστοποιημένοι εκπαιδευτές. Οι συμμετέχοντες πρέπει να φέρουν το δικό τους στρωματάκι, νερό και, αν θέλουν, ένα καπέλο.", "The classes are suitable for beginners too, and will be taught by certified instructors. Participants must bring their own mat, water and, if they wish, a hat."),
  L("Εκφωνήτρια", "f", "Δεν χρειάζεται εγγραφή. Σε περίπτωση βροχής, τα μαθήματα θα γίνονται στο κλειστό γυμναστήριο του δημοτικού σχολείου, που βρίσκεται απέναντι από την είσοδο του πάρκου.", "No registration is needed. If it rains, the classes will take place in the indoor gym of the primary school, which is opposite the park entrance."),
 ],
 "questions": [
  Q("Πότε γίνονται τα μαθήματα;", ["Κάθε μέρα το απόγευμα", "Τρίτη και Πέμπτη στις επτά το πρωί", "Μόνο τα σαββατοκύριακα", "Κάθε Δευτέρα το βράδυ"], 1, "Κάθε Τρίτη και Πέμπτη, στις επτά το πρωί"),
  Q("Τι πρέπει να φέρουν οι συμμετέχοντες;", ["Το δικό τους στρωματάκι και νερό", "Ιατρική βεβαίωση", "Αθλητικά παπούτσια", "Μια φωτογραφία"], 0, "πρέπει να φέρουν το δικό τους στρωματάκι, νερό"),
  Q("Πού θα γίνονται τα μαθήματα αν βρέχει;", ["Δεν θα γίνονται", "Στο δημαρχείο", "Στο κλειστό γυμναστήριο του δημοτικού σχολείου", "Κάτω από τα δέντρα"], 2, "θα γίνονται στο κλειστό γυμναστήριο του δημοτικού σχολείου"),
 ],
 "gloss": {"Αθλητισμός": "αθλητισμός — sport", "δωρεάν": "δωρεάν — free of charge", "αρχάριους": "αρχάριος — beginner", "πιστοποιημένοι": "πιστοποιημένος — certified", "εκπαιδευτές": "εκπαιδευτής — instructor", "στρωματάκι": "στρωματάκι — (yoga) mat", "εγγραφή": "εγγραφή — registration", "γυμναστήριο": "γυμναστήριο — gym"}
})

ITEMS.append({
 "id": "l150-dia-gata-diakopes", "title": "Ποιος θα ταΐσει τη γάτα;", "title_en": "Who will feed the cat?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε μια συζήτηση ανάμεσα σε δύο γειτόνισσες στη σκάλα της πολυκατοικίας.",
 "script": [
  L("Ρένα", "f", "Λίνα, μπορώ να σου ζητήσω μια χάρη; Φεύγουμε για δέκα μέρες στην Κρήτη, και δεν έχω πού να αφήσω τη Μέλισσα.", "Lina, can I ask you a favour? We're going to Crete for ten days, and I have nowhere to leave Melissa."),
  L("Λίνα", "f", "Τη γάτα σου; Ευχαρίστως! Τι πρέπει να κάνω;", "Your cat? Gladly! What do I need to do?"),
  L("Ρένα", "f", "Να της βάζεις φαγητό και φρέσκο νερό μία φορά την ημέρα, κατά προτίμηση το βράδυ. Την άμμο της αρκεί να την καθαρίζεις μέρα παρά μέρα. Θα σου αφήσω και τα κλειδιά.", "Put out food and fresh water for her once a day, preferably in the evening. It's enough to clean her litter every other day. I'll leave you the keys too."),
  L("Λίνα", "f", "Χρειάζεται να της δίνω κάποιο φάρμακο;", "Do I need to give her any medicine?"),
  L("Ρένα", "f", "Όχι, είναι υγιέστατη. Μόνο μην ανοίγεις τα παράθυρα της κουζίνας, γιατί πηδάει στο μπαλκόνι του από κάτω. Το τηλέφωνο του κτηνιάτρου είναι γραμμένο πάνω στο ψυγείο, για κάθε ενδεχόμενο.", "No, she's perfectly healthy. Just don't open the kitchen windows, because she jumps onto the balcony below. The vet's phone number is written on the fridge, just in case."),
  L("Λίνα", "f", "Εντάξει. Και θα σου στέλνω φωτογραφίες, για να μη σου λείπει!", "OK. And I'll send you photos, so you don't miss her!"),
 ],
 "questions": [
  Q("Πόσο συχνά πρέπει να καθαρίζει η Λίνα την άμμο;", ["Κάθε μέρα", "Μέρα παρά μέρα", "Μία φορά την εβδομάδα", "Δεν χρειάζεται"], 1, "Την άμμο της αρκεί να την καθαρίζεις μέρα παρά μέρα"),
  Q("Γιατί δεν πρέπει να ανοίγει τα παράθυρα της κουζίνας;", ["Γιατί μπαίνουν έντομα", "Γιατί κάνει κρύο", "Γιατί η γάτα πηδάει στο μπαλκόνι του από κάτω", "Γιατί είναι χαλασμένα"], 2, "γιατί πηδάει στο μπαλκόνι του από κάτω"),
  Q("Πού είναι γραμμένο το τηλέφωνο του κτηνιάτρου;", ["Πάνω στο ψυγείο", "Σε ένα μήνυμα", "Στην πόρτα", "Στο κινητό της Λίνας"], 0, "Το τηλέφωνο του κτηνιάτρου είναι γραμμένο πάνω στο ψυγείο"),
 ],
 "gloss": {"γειτόνισσες": "γειτόνισσα — (female) neighbour", "χάρη": "χάρη — favour", "Ευχαρίστως": "ευχαρίστως — gladly", "κατά προτίμηση": "κατά προτίμηση — preferably", "άμμο": "άμμος — (cat) litter, sand", "μέρα παρά μέρα": "μέρα παρά μέρα — every other day", "υγιέστατη": "υγιέστατος — perfectly healthy", "πηδάει": "πηδάω — to jump", "κτηνιάτρου": "κτηνίατρος — vet", "ενδεχόμενο": "για κάθε ενδεχόμενο — just in case"}
})

ITEMS.append({
 "id": "l150-int-xenagisi-afis", "title": "Ξενάγηση με τα χέρια", "title_en": "A tour with your hands", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια αρχαιολόγο που οργανώνει ξεναγήσεις για τυφλούς σε ένα μουσείο.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς γίνεται μια ξενάγηση για ανθρώπους που δεν βλέπουν;", "How does a guided tour work for people who can't see?"),
  L("Αρχαιολόγος", "f", "Με την αφή. Έχουμε φτιάξει πιστά αντίγραφα από είκοσι αγάλματα και αγγεία, που οι επισκέπτες μπορούν να τα αγγίξουν. Τα πρωτότυπα, βέβαια, μένουν πίσω από τις προθήκες.", "Through touch. We've made faithful copies of twenty statues and vases, which the visitors can touch. The originals, of course, stay behind the display cases."),
  L("Δημοσιογράφος", "m", "Και αρκεί αυτό;", "And is that enough?"),
  L("Αρχαιολόγος", "f", "Όχι μόνο. Περιγράφω με λεπτομέρεια τα χρώματα και το φως, και έχουμε ετικέτες σε γραφή μπράιγ. Η πιο συγκινητική στιγμή είναι όταν κάποιος ανακαλύπτει με τα δάχτυλά του το χαμόγελο ενός αρχαϊκού κούρου.", "Not only. I describe the colours and light in detail, and we have labels in Braille. The most moving moment is when someone discovers with their fingers the smile of an archaic kouros."),
  L("Δημοσιογράφος", "m", "Έχετε μάθει κι εσείς κάτι από αυτές τις ξεναγήσεις;", "Have you learnt something from these tours too?"),
  L("Αρχαιολόγος", "f", "Πάρα πολλά. Οι τυφλοί επισκέπτες προσέχουν λεπτομέρειες που εμείς δεν βλέπουμε, όπως τα σημάδια από τα εργαλεία του γλύπτη. Τώρα συμμετέχουν και βλέποντες, με κλειστά μάτια, και λένε ότι είδαν τα αγάλματα για πρώτη φορά.", "A great deal. Blind visitors notice details that we don't see, like the marks of the sculptor's tools. Now sighted people take part too, with their eyes closed, and they say they saw the statues for the first time."),
 ],
 "questions": [
  Q("Τι αγγίζουν οι επισκέπτες;", ["Τα πρωτότυπα αγάλματα", "Πιστά αντίγραφα αγαλμάτων και αγγείων", "Μόνο τις προθήκες", "Μικρά παιχνίδια"], 1, "Έχουμε φτιάξει πιστά αντίγραφα από είκοσι αγάλματα και αγγεία"),
  Q("Ποια είναι για την αρχαιολόγο η πιο συγκινητική στιγμή;", ["Όταν τελειώνει η ξενάγηση", "Όταν οι επισκέπτες αγοράζουν αντίγραφα", "Όταν κάποιος ανακαλύπτει με τα δάχτυλα το χαμόγελο ενός κούρου", "Όταν έρχονται παιδιά"], 2, "όταν κάποιος ανακαλύπτει με τα δάχτυλά του το χαμόγελο ενός αρχαϊκού κούρου"),
  Q("Τι λένε οι βλέποντες που συμμετέχουν με κλειστά μάτια;", ["Ότι είδαν τα αγάλματα για πρώτη φορά", "Ότι βαρέθηκαν", "Ότι φοβήθηκαν", "Ότι δεν κατάλαβαν τίποτα"], 0, "λένε ότι είδαν τα αγάλματα για πρώτη φορά"),
 ],
 "gloss": {"τυφλούς": "τυφλός — blind", "αφή": "αφή — (sense of) touch", "πιστά": "πιστός — faithful, exact", "αντίγραφα": "αντίγραφο — copy, replica", "πρωτότυπα": "πρωτότυπο — original", "προθήκες": "προθήκη — display case", "μπράιγ": "γραφή μπράιγ — Braille", "κούρου": "κούρος — kouros (archaic statue of a youth)", "γλύπτη": "γλύπτης — sculptor", "βλέποντες": "βλέπων — sighted person"}
})

ITEMS.append({
 "id": "l150-news-katharismos-paralias", "title": "Εθελοντικός καθαρισμός παραλίας", "title_en": "Volunteer beach clean-up", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση από το περιφερειακό δελτίο ειδήσεων.",
 "script": [
  L("Παρουσιαστής", "m", "Περισσότεροι από τριακόσιοι εθελοντές, ανάμεσά τους πολλοί μαθητές, καθάρισαν χθες μια παραλία μήκους τριών χιλιομέτρων στη δυτική ακτή της πόλης. Συγκέντρωσαν συνολικά πάνω από δύο τόνους σκουπίδια.", "More than three hundred volunteers, many of them school pupils, yesterday cleaned a three-kilometre beach on the city's west coast. In total they collected more than two tonnes of rubbish."),
  L("Παρουσιαστής", "m", "Τα περισσότερα ήταν πλαστικά μπουκάλια, καπάκια και αποτσίγαρα, αλλά βρέθηκαν και πιο παράξενα αντικείμενα, όπως ένα παλιό ποδήλατο και δύο λάστιχα αυτοκινήτου. Όλα τα ανακυκλώσιμα υλικά μεταφέρθηκαν στο κέντρο ανακύκλωσης του δήμου.", "Most of it was plastic bottles, caps and cigarette butts, but stranger objects were also found, such as an old bicycle and two car tyres. All the recyclable materials were taken to the municipal recycling centre."),
  L("Παρουσιαστής", "m", "Οι διοργανωτές τόνισαν ότι το μεγαλύτερο μέρος των σκουπιδιών δεν το αφήνουν οι λουόμενοι, αλλά το φέρνει η θάλασσα από άλλες περιοχές. Ζητούν γι' αυτό να μπουν δίχτυα στις εκβολές των ρεμάτων.", "The organisers stressed that most of the rubbish is not left by bathers, but is brought by the sea from other areas. They are therefore asking for nets to be placed at the mouths of the streams."),
 ],
 "questions": [
  Q("Πόσα σκουπίδια συγκεντρώθηκαν;", ["Περίπου διακόσια κιλά", "Πάνω από δύο τόνοι", "Τρεις τόνοι ακριβώς", "Πάνω από δέκα τόνοι"], 1, "Συγκέντρωσαν συνολικά πάνω από δύο τόνους σκουπίδια"),
  Q("Πού μεταφέρθηκαν τα ανακυκλώσιμα υλικά;", ["Σε ένα σχολείο", "Σε μια χωματερή", "Στο κέντρο ανακύκλωσης του δήμου", "Στο λιμάνι"], 2, "μεταφέρθηκαν στο κέντρο ανακύκλωσης του δήμου"),
  Q("Από πού έρχονται, κατά τους διοργανωτές, τα περισσότερα σκουπίδια;", ["Τα φέρνει η θάλασσα από άλλες περιοχές", "Τα αφήνουν οι λουόμενοι", "Από τα εστιατόρια της παραλίας", "Από τα πλοία του λιμανιού"], 0, "το φέρνει η θάλασσα από άλλες περιοχές"),
 ],
 "gloss": {"περιφερειακό": "περιφερειακός — regional", "εθελοντές": "εθελοντής — volunteer", "τόνους": "τόνος — tonne", "αποτσίγαρα": "αποτσίγαρο — cigarette butt", "λάστιχα": "λάστιχο — tyre", "ανακυκλώσιμα": "ανακυκλώσιμος — recyclable", "διοργανωτές": "διοργανωτής — organiser", "λουόμενοι": "λουόμενος — bather", "εκβολές": "εκβολή — mouth (of a river)", "ρεμάτων": "ρέμα — stream"}
})

ITEMS.append({
 "id": "l150-mon-klidomenos", "title": "Κλειδωμένος έξω στις δύο τα ξημερώματα", "title_en": "Locked out at two in the morning", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν νεαρό να διηγείται σε φίλους μια περιπέτειά του.",
 "script": [
  L("Άρης", "m", "Γύριζα από έναν γάμο, στις δύο τα ξημερώματα, και στην πόρτα της πολυκατοικίας κατάλαβα ότι τα κλειδιά μου ήταν στο σακάκι που είχα αφήσει στο αυτοκίνητο ενός φίλου. Ο φίλος, φυσικά, είχε ήδη φύγει για τη Λάρισα.", "I was coming back from a wedding at two in the morning, and at the front door of the building I realised my keys were in the jacket I'd left in a friend's car. The friend, of course, had already left for Larissa."),
  L("Άρης", "m", "Τηλεφώνησα σε έναν κλειδαρά που βρήκα στο ίντερνετ. Μου ζήτησε εκατόν πενήντα ευρώ για νυχτερινή κλήση, και μου είπε ότι θα αργούσε μία ώρα. Κάθισα στα σκαλιά με το κοστούμι και περίμενα, ενώ ένας γάτος με κοιτούσε σαν να με λυπόταν.", "I called a locksmith I found online. He asked me for a hundred and fifty euros for a night call, and told me he'd be an hour late. I sat on the steps in my suit and waited, while a tomcat looked at me as if he felt sorry for me."),
  L("Άρης", "m", "Τελικά με έσωσε η κυρία του πρώτου ορόφου, που ξύπνησε από τις φωνές μου στο τηλέφωνο. Μου άνοιξε την εξώπορτα, μου έφτιαξε τσάι, και ανακαλύψαμε ότι η κόρη της έχει ένα αντικλείδι του διαμερίσματός μου, από τότε που πότιζε τα λουλούδια μου πέρσι το καλοκαίρι.", "In the end I was saved by the lady on the first floor, who woke up from my shouting on the phone. She opened the front door for me, made me tea, and we discovered that her daughter has a spare key to my flat, from when she watered my flowers last summer."),
 ],
 "questions": [
  Q("Πού ήταν τα κλειδιά του Άρη;", ["Στο σακάκι του, στο αυτοκίνητο ενός φίλου", "Στο εστιατόριο του γάμου", "Μέσα στο διαμέρισμα", "Τα είχε χάσει στον δρόμο"], 0, "τα κλειδιά μου ήταν στο σακάκι που είχα αφήσει στο αυτοκίνητο ενός φίλου"),
  Q("Τι του είπε ο κλειδαράς;", ["Ότι δεν δουλεύει τη νύχτα", "Ότι θα ερχόταν αμέσως", "Ότι θα αργούσε μία ώρα", "Ότι η κλήση είναι δωρεάν"], 2, "μου είπε ότι θα αργούσε μία ώρα"),
  Q("Πώς λύθηκε τελικά το πρόβλημα;", ["Ήρθε ο φίλος του από τη Λάρισα", "Η κόρη της γειτόνισσας είχε ένα αντικλείδι", "Ο κλειδαράς άνοιξε την πόρτα", "Μπήκε από το μπαλκόνι"], 1, "η κόρη της έχει ένα αντικλείδι του διαμερίσματός μου"),
 ],
 "gloss": {"ξημερώματα": "ξημερώματα — small hours", "πολυκατοικίας": "πολυκατοικία — apartment building", "σακάκι": "σακάκι — jacket", "κλειδαρά": "κλειδαράς — locksmith", "κλήση": "κλήση — call-out", "λυπόταν": "λυπάμαι — to feel sorry for", "εξώπορτα": "εξώπορτα — front door (of a building)", "αντικλείδι": "αντικλείδι — spare key", "πότιζε": "ποτίζω — to water"}
})

ITEMS.append({
 "id": "l150-rep-galatas", "title": "Η επιστροφή του γαλατά", "title_en": "The return of the milkman", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια πρωινή εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "f", "Είναι έξι το πρωί, και ο Γιώργος αφήνει ήδη γυάλινα μπουκάλια με φρέσκο γάλα έξω από τις πόρτες μιας γειτονιάς των Ιωαννίνων. Το γάλα προέρχεται από τη φάρμα της οικογένειάς του, λίγα χιλιόμετρα έξω από την πόλη.", "It's six in the morning, and Giorgos is already leaving glass bottles of fresh milk outside the doors of a neighbourhood in Ioannina. The milk comes from his family's farm, a few kilometres outside the city."),
  L("Ρεπόρτερ", "f", "Οι πελάτες παραγγέλνουν μέσα από μια εφαρμογή στο κινητό και πληρώνουν μία φορά τον μήνα. Τα άδεια μπουκάλια τα αφήνουν έξω από την πόρτα, και ο Γιώργος τα μαζεύει, τα πλένει και τα ξαναγεμίζει.", "Customers order through a mobile app and pay once a month. They leave the empty bottles outside the door, and Giorgos collects them, washes them and refills them."),
  L("Ρεπόρτερ", "f", "Ο Γιώργος ξεκίνησε με είκοσι πελάτες, και σήμερα έχει πάνω από τριακόσιους. «Οι ηλικιωμένοι μού λένε ότι θυμούνται τον γαλατά της παιδικής τους ηλικίας», λέει. «Οι νέοι το κάνουν για το περιβάλλον. Κι όλοι λένε ότι το γάλα έχει άλλη γεύση.»", "Giorgos started with twenty customers, and today he has over three hundred. 'Older people tell me they remember the milkman of their childhood,' he says. 'Young people do it for the environment. And everyone says the milk tastes different.'"),
 ],
 "questions": [
  Q("Από πού προέρχεται το γάλα;", ["Από ένα εργοστάσιο", "Από τη φάρμα της οικογένειας του Γιώργου", "Από το σούπερ μάρκετ", "Από ένα χωριό της Κρήτης"], 1, "Το γάλα προέρχεται από τη φάρμα της οικογένειάς του"),
  Q("Τι γίνεται με τα άδεια μπουκάλια;", ["Τα πετάνε στην ανακύκλωση", "Τα κρατάνε οι πελάτες", "Ο Γιώργος τα μαζεύει, τα πλένει και τα ξαναγεμίζει", "Τα επιστρέφουν στο κατάστημα"], 2, "ο Γιώργος τα μαζεύει, τα πλένει και τα ξαναγεμίζει"),
  Q("Γιατί, κατά τον Γιώργο, αγοράζουν οι νέοι;", ["Για το περιβάλλον", "Γιατί είναι φθηνότερο", "Γιατί θυμούνται τον γαλατά", "Γιατί δεν έχουν χρόνο να ψωνίσουν"], 0, "Οι νέοι το κάνουν για το περιβάλλον"),
 ],
 "gloss": {"γαλατά": "γαλατάς — milkman", "γυάλινα": "γυάλινος — glass", "φάρμα": "φάρμα — farm", "παραγγέλνουν": "παραγγέλνω — to order", "εφαρμογή": "εφαρμογή — app", "ξαναγεμίζει": "ξαναγεμίζω — to refill", "ηλικιωμένοι": "ηλικιωμένος — elderly person", "γεύση": "γεύση — taste"}
})

ITEMS.append({
 "id": "l150-dia-farmakeio-nautia", "title": "Στο φαρμακείο πριν από το πλοίο", "title_en": "At the pharmacy before the ferry", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε μια συζήτηση σε ένα φαρμακείο κοντά στο λιμάνι.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Ταξιδεύουμε σε δύο ώρες για την Ικαρία, και ο γιος μου ζαλίζεται πάντα στο πλοίο. Έχετε κάτι να του δώσω;", "Good morning. We're sailing to Ikaria in two hours, and my son always gets seasick on the ferry. Do you have something I can give him?"),
  L("Φαρμακοποιός", "m", "Πόσων χρονών είναι;", "How old is he?"),
  L("Πελάτισσα", "f", "Εννιά.", "Nine."),
  L("Φαρμακοποιός", "m", "Για παιδιά έχουμε αυτά τα μασώμενα δισκία. Πρέπει να πάρει ένα μισή ώρα πριν από την αναχώρηση, όχι όταν θα έχει ήδη ζαλιστεί. Να ξέρετε ότι μπορεί να του φέρουν λίγη υπνηλία.", "For children we have these chewable tablets. He should take one half an hour before departure, not when he already feels sick. Be aware that they may make him a little drowsy."),
  L("Πελάτισσα", "f", "Υπάρχει και κάτι χωρίς φάρμακα;", "Is there anything without medicine as well?"),
  L("Φαρμακοποιός", "m", "Αυτά τα βραχιολάκια πιέζουν ένα σημείο στον καρπό. Σε κάποιους βοηθούν, σε άλλους όχι. Το σημαντικότερο όμως είναι να κάθεται στο κατάστρωμα, να κοιτάζει τον ορίζοντα και να μη διαβάζει ούτε να παίζει με το κινητό.", "These wristbands press on a point on the wrist. They help some people, not others. But the most important thing is for him to sit on deck, look at the horizon and not read or play on his phone."),
 ],
 "questions": [
  Q("Πότε πρέπει να πάρει το παιδί το δισκίο;", ["Όταν αρχίσει να ζαλίζεται", "Μισή ώρα πριν από την αναχώρηση", "Το προηγούμενο βράδυ", "Μετά το φαγητό"], 1, "Πρέπει να πάρει ένα μισή ώρα πριν από την αναχώρηση"),
  Q("Ποια παρενέργεια μπορεί να έχουν τα δισκία;", ["Πονοκέφαλο", "Πόνο στο στομάχι", "Λίγη υπνηλία", "Αλλεργία"], 2, "μπορεί να του φέρουν λίγη υπνηλία"),
  Q("Ποια είναι, κατά τον φαρμακοποιό, η σημαντικότερη συμβουλή;", ["Να κάθεται στο κατάστρωμα και να κοιτάζει τον ορίζοντα", "Να φοράει πάντα το βραχιολάκι", "Να μην τρώει τίποτα", "Να κοιμηθεί στην καμπίνα"], 0, "να κάθεται στο κατάστρωμα, να κοιτάζει τον ορίζοντα"),
 ],
 "gloss": {"ζαλίζεται": "ζαλίζομαι — to feel dizzy/seasick", "μασώμενα": "μασώμενος — chewable", "δισκία": "δισκίο — tablet", "αναχώρηση": "αναχώρηση — departure", "υπνηλία": "υπνηλία — drowsiness", "βραχιολάκια": "βραχιολάκι — wristband", "καρπό": "καρπός — wrist", "κατάστρωμα": "κατάστρωμα — deck", "ορίζοντα": "ορίζοντας — horizon"}
})

ITEMS.append({
 "id": "l150-c1-plani-maknamara", "title": "Η πλάνη του ΜακΝαμάρα", "title_en": "The McNamara fallacy", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη για τη διοίκηση οργανισμών.",
 "script": [
  L("Ομιλητής", "m", "Ο Ρόμπερτ ΜακΝαμάρα, υπουργός Άμυνας των Ηνωμένων Πολιτειών τη δεκαετία του '60, ήταν άνθρωπος των αριθμών. Στον πόλεμο του Βιετνάμ, μεταξύ άλλων, μετρούσε την πρόοδο με βάση τον αριθμό των νεκρών του αντιπάλου, γιατί ήταν ένα στοιχείο που μπορούσε να καταγραφεί εύκολα.", "Robert McNamara, US Secretary of Defense in the 1960s, was a man of numbers. In the Vietnam War, among other things, he measured progress by the number of enemy dead, because it was a figure that could be recorded easily."),
  L("Ομιλητής", "m", "Αυτό που δεν μετρούσαν οι πίνακές του ήταν η διάθεση του πληθυσμού, η αποφασιστικότητα του αντιπάλου, η αξιοπιστία της ίδιας της καταμέτρησης. Τα νούμερα έδειχναν πρόοδο, ενώ ο πόλεμος, όπως αποδείχτηκε, πήγαινε προς την ήττα.", "What his tables didn't measure was the mood of the population, the enemy's determination, the reliability of the count itself. The numbers showed progress, while the war, as it turned out, was heading towards defeat."),
  L("Ομιλητής", "m", "Ο κοινωνιολόγος Ντάνιελ Γιάνκελοβιτς περιέγραψε αργότερα την πλάνη σε τέσσερα βήματα. Πρώτα μετράς ό,τι μετριέται εύκολα. Μετά αγνοείς ό,τι δεν μετριέται. Ύστερα υποθέτεις ότι ό,τι δεν μετριέται δεν είναι σημαντικό. Και τέλος λες ότι δεν υπάρχει καν.", "The sociologist Daniel Yankelovich later described the fallacy in four steps. First you measure whatever is easily measured. Then you ignore what can't be measured. Then you presume that what can't be measured isn't important. And finally you say it doesn't even exist."),
  L("Ομιλητής", "m", "Η πλάνη αυτή δεν ανήκει στο παρελθόν. Τη βλέπουμε σε σχολεία που κρίνονται μόνο από τους βαθμούς, σε νοσοκομεία που κρίνονται μόνο από τον χρόνο αναμονής. Οι αριθμοί είναι πολύτιμοι, αρκεί να θυμόμαστε τι δεν μας λένε.", "This fallacy doesn't belong to the past. We see it in schools that are judged only by grades, in hospitals judged only by waiting times. Numbers are valuable, as long as we remember what they don't tell us."),
 ],
 "questions": [
  Q("Γιατί ο ΜακΝαμάρα χρησιμοποιούσε τον αριθμό των νεκρών του αντιπάλου;", ["Γιατί ήταν το πιο ηθικό κριτήριο", "Γιατί ήταν ένα στοιχείο που μπορούσε να καταγραφεί εύκολα", "Γιατί του το ζήτησε ο πρόεδρος", "Γιατί ήταν το μόνο στοιχείο που υπήρχε"], 1, "γιατί ήταν ένα στοιχείο που μπορούσε να καταγραφεί εύκολα"),
  Q("Τι ΔΕΝ μετρούσαν οι πίνακές του;", ["Τον αριθμό των στρατιωτών", "Το κόστος του πολέμου", "Τη διάθεση του πληθυσμού και την αποφασιστικότητα του αντιπάλου", "Τις απώλειες του αμερικανικού στρατού"], 2, "η διάθεση του πληθυσμού, η αποφασιστικότητα του αντιπάλου"),
  Q("Ποιο είναι το τελευταίο βήμα της πλάνης κατά τον Γιάνκελοβιτς;", ["Να μετράς ό,τι μετριέται εύκολα", "Να αγνοείς ό,τι δεν μετριέται", "Να υποθέτεις ότι δεν είναι σημαντικό", "Να λες ότι ό,τι δεν μετριέται δεν υπάρχει καν"], 3, "Και τέλος λες ότι δεν υπάρχει καν"),
  Q("Ποιο είναι το συμπέρασμα του ομιλητή;", ["Οι αριθμοί είναι πολύτιμοι, αρκεί να θυμόμαστε τι δεν μας λένε", "Πρέπει να καταργήσουμε τους βαθμούς", "Οι αριθμοί πάντα παραπλανούν", "Τα νοσοκομεία δουλεύουν καλύτερα από τα σχολεία"], 0, "Οι αριθμοί είναι πολύτιμοι, αρκεί να θυμόμαστε τι δεν μας λένε"),
 ],
 "gloss": {"πλάνη": "πλάνη — fallacy, error", "διοίκηση": "διοίκηση — management", "Άμυνας": "άμυνα — defence", "καταγραφεί": "καταγράφομαι — to be recorded", "διάθεση": "διάθεση — mood", "αποφασιστικότητα": "αποφασιστικότητα — determination", "αξιοπιστία": "αξιοπιστία — reliability", "καταμέτρησης": "καταμέτρηση — count", "ήττα": "ήττα — defeat", "αγνοείς": "αγνοώ — to ignore", "υποθέτεις": "υποθέτω — to assume"}
})

ITEMS.append({
 "id": "l150-c1-palindromisi", "title": "Η επιστροφή στον μέσο όρο", "title_en": "Regression to the mean", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκπομπή για τη στατιστική στην καθημερινή ζωή, με καλεσμένη μια μαθηματικό.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι είναι η «παλινδρόμηση προς τον μέσο όρο»; Ακούγεται πολύ τεχνικό.", "What is 'regression to the mean'? It sounds very technical."),
  L("Μαθηματικός", "f", "Η ιδέα είναι απλή. Όταν ένα αποτέλεσμα εξαρτάται εν μέρει από την τύχη, μια ακραία τιμή ακολουθείται συνήθως από μια πιο συνηθισμένη. Ο Βρετανός επιστήμονας Φράνσις Γκάλτον το παρατήρησε τον 19ο αιώνα: τα παιδιά πολύ ψηλών γονιών ήταν κατά κανόνα ψηλά, αλλά λιγότερο ψηλά από τους γονείς τους.", "The idea is simple. When a result depends partly on luck, an extreme value is usually followed by a more ordinary one. The British scientist Francis Galton observed it in the 19th century: the children of very tall parents were as a rule tall, but less tall than their parents."),
  L("Δημοσιογράφος", "m", "Και γιατί μας ενδιαφέρει αυτό;", "And why should that interest us?"),
  L("Μαθηματικός", "f", "Γιατί μας ξεγελά συνεχώς. Ο Ντάνιελ Κάνεμαν διηγείται ότι εκπαιδευτές πιλότων του έλεγαν πως ο έπαινος βλάπτει: όταν επαινούσαν μια εξαιρετική προσγείωση, η επόμενη ήταν χειρότερη, ενώ μετά από μια κατσάδα η επόμενη ήταν καλύτερη. Στην πραγματικότητα, οι εκπαιδευόμενοι απλώς επέστρεφαν στο συνηθισμένο τους επίπεδο.", "Because it fools us constantly. Daniel Kahneman tells how flight instructors told him that praise is harmful: when they praised an excellent landing, the next one was worse, while after a telling-off the next one was better. In reality, the trainees were simply returning to their usual level."),
  L("Δημοσιογράφος", "m", "Υπάρχουν κι άλλα παραδείγματα;", "Are there other examples?"),
  L("Μαθηματικός", "f", "Αμέτρητα. Ένας αθλητής που είχε μια απίστευτη χρονιά συνήθως παίζει χειρότερα την επόμενη, και αμέσως μιλάμε για «κατάρα». Ένα φάρμακο που δοκιμάζεται όταν τα συμπτώματα είναι στη χειρότερη φάση τους φαίνεται πιο αποτελεσματικό απ' ό,τι είναι. Γι' αυτό οι σοβαρές μελέτες έχουν πάντα ομάδα σύγκρισης.", "Countless. An athlete who had an incredible year usually plays worse the next, and immediately we talk about a 'curse'. A drug tested when symptoms are at their worst seems more effective than it is. That's why serious studies always have a comparison group."),
 ],
 "questions": [
  Q("Τι παρατήρησε ο Γκάλτον;", ["Ότι τα παιδιά ψηλών γονιών ήταν ψηλότερα από αυτούς", "Ότι τα παιδιά πολύ ψηλών γονιών ήταν ψηλά, αλλά λιγότερο από τους γονείς τους", "Ότι το ύψος δεν κληρονομείται", "Ότι τα κορίτσια ψηλώνουν περισσότερο"], 1, "τα παιδιά πολύ ψηλών γονιών ήταν κατά κανόνα ψηλά, αλλά λιγότερο ψηλά από τους γονείς τους"),
  Q("Τι συμπέραιναν λανθασμένα οι εκπαιδευτές πιλότων;", ["Ότι οι πιλότοι κουράζονται", "Ότι ο καιρός επηρεάζει τις προσγειώσεις", "Ότι ο έπαινος βλάπτει", "Ότι οι νέοι μαθαίνουν πιο γρήγορα"], 2, "ο έπαινος βλάπτει"),
  Q("Ποια είναι η πραγματική εξήγηση για τους εκπαιδευόμενους;", ["Επέστρεφαν απλώς στο συνηθισμένο τους επίπεδο", "Φοβούνταν τους εκπαιδευτές", "Τα αεροπλάνα ήταν διαφορετικά", "Δεν άκουγαν τις οδηγίες"], 0, "οι εκπαιδευόμενοι απλώς επέστρεφαν στο συνηθισμένο τους επίπεδο"),
  Q("Γιατί οι σοβαρές μελέτες φαρμάκων έχουν ομάδα σύγκρισης;", ["Για να μειωθεί το κόστος", "Για να συμμετέχουν περισσότεροι", "Γιατί το απαιτούν οι ασθενείς", "Γιατί ένα φάρμακο που δοκιμάζεται στη χειρότερη φάση φαίνεται πιο αποτελεσματικό απ' ό,τι είναι"], 3, "φαίνεται πιο αποτελεσματικό απ' ό,τι είναι"),
 ],
 "gloss": {"παλινδρόμηση": "παλινδρόμηση — regression", "μέσο όρο": "μέσος όρος — average, mean", "ακραία": "ακραίος — extreme", "κατά κανόνα": "κατά κανόνα — as a rule", "ξεγελά": "ξεγελώ — to fool", "έπαινος": "έπαινος — praise", "προσγείωση": "προσγείωση — landing", "κατσάδα": "κατσάδα — telling-off", "εκπαιδευόμενοι": "εκπαιδευόμενος — trainee", "κατάρα": "κατάρα — curse", "σύγκρισης": "ομάδα σύγκρισης — comparison/control group"}
})

rnd = random.Random(150)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-150.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
