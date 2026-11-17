# Source for library/listening/listening-105.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l105.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l105-ann-podilatikos-gyros", "title": "Κλειστοί δρόμοι για τον νυχτερινό ποδηλατικό γύρο", "title_en": "Roads closed for the night bike ride", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση της τροχαίας στο ραδιόφωνο.",
 "script": [
  L("Εκφωνητής", "m", "Η Τροχαία ενημερώνει τους οδηγούς ότι το Σάββατο το βράδυ θα πραγματοποιηθεί ο ετήσιος νυχτερινός ποδηλατικός γύρος της πόλης. Από τις εννιά το βράδυ μέχρι τη μία μετά τα μεσάνυχτα θα διακοπεί η κυκλοφορία των αυτοκινήτων στην παραλιακή λεωφόρο και στους δρόμους γύρω από το λιμάνι.", "The traffic police inform drivers that on Saturday evening the town's annual night bike ride will take place. From nine in the evening until one after midnight, car traffic will be stopped on the seafront avenue and in the streets around the harbour."),
  L("Εκφωνητής", "m", "Η στάθμευση στις οδούς αυτές θα απαγορεύεται από τις έξι το απόγευμα. Τα αυτοκίνητα που δεν θα έχουν απομακρυνθεί θα μεταφερθούν με γερανό. Τα λεωφορεία των γραμμών ένα και τέσσερα θα ακολουθούν παρακαμπτήριες διαδρομές.", "Parking in these streets will be forbidden from six in the evening. Cars that have not been moved will be towed away. Buses on lines one and four will follow diversions."),
  L("Εκφωνητής", "m", "Οι ποδηλάτες που θέλουν να συμμετάσχουν πρέπει να έχουν μπροστινό και πίσω φως και να φορούν κράνος. Η συμμετοχή είναι δωρεάν, ενώ για παιδιά κάτω των δώδεκα ετών απαιτείται η συνοδεία ενήλικα.", "Cyclists who wish to take part must have a front and rear light and wear a helmet. Participation is free, while children under twelve must be accompanied by an adult."),
 ],
 "questions": [
  Q("Πότε θα διακοπεί η κυκλοφορία των αυτοκινήτων;", ["Όλη την ημέρα του Σαββάτου", "Από τις έξι το απόγευμα ως τα μεσάνυχτα", "Από τις εννιά το βράδυ μέχρι τη μία μετά τα μεσάνυχτα", "Την Κυριακή το πρωί"], 2, "Από τις εννιά το βράδυ μέχρι τη μία μετά τα μεσάνυχτα"),
  Q("Τι θα γίνει με τα αυτοκίνητα που δεν θα έχουν απομακρυνθεί;", ["Θα μεταφερθούν με γερανό", "Θα πάρουν μόνο προειδοποίηση", "Θα κλειδωθούν", "Τίποτα"], 0, "θα μεταφερθούν με γερανό"),
  Q("Τι πρέπει να έχουν οι ποδηλάτες;", ["Εισιτήριο συμμετοχής", "Μπροστινό και πίσω φως και κράνος", "Ειδική άδεια από τον δήμο", "Ηλεκτρικό ποδήλατο"], 1, "πρέπει να έχουν μπροστινό και πίσω φως και να φορούν κράνος"),
 ],
 "gloss": {"Τροχαία": "Τροχαία — traffic police", "πραγματοποιηθεί": "πραγματοποιούμαι — to take place", "παραλιακή": "παραλιακός — seafront", "στάθμευση": "στάθμευση — parking", "γερανό": "γερανός — tow truck, crane", "παρακαμπτήριες": "παρακαμπτήριος — diversion, detour", "συνοδεία": "συνοδεία — accompaniment"}
})

ITEMS.append({
 "id": "l105-vm-ekdromi-meteora", "title": "Αλλαγή στην εκδρομή στα Μετέωρα", "title_en": "A change to the Meteora trip", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε δηλώσει συμμετοχή σε μια εκδρομή ενός πολιτιστικού συλλόγου. Ακούτε ένα μήνυμα από την οργανώτρια.",
 "script": [
  L("Οργανώτρια", "f", "Καλησπέρα σας, η Ευγενία είμαι, από τον πολιτιστικό σύλλογο. Σας τηλεφωνώ για την εκδρομή στα Μετέωρα της επόμενης Κυριακής. Δυστυχώς, το λεωφορείο που είχαμε κλείσει χάλασε και η εταιρεία μάς δίνει άλλο, λίγο μικρότερο, οπότε θα φύγουμε μισή ώρα νωρίτερα, στις έξι και μισή, από την πλατεία του δημαρχείου.", "Good evening, it's Evgenia, from the cultural association. I'm calling about next Sunday's trip to Meteora. Unfortunately, the coach we had booked has broken down and the company is giving us another, slightly smaller one, so we'll leave half an hour earlier, at half past six, from the town hall square."),
  L("Οργανώτρια", "f", "Θα επισκεφθούμε δύο μοναστήρια αντί για τρία, γιατί το ένα είναι κλειστό εκείνη τη μέρα. Σας θυμίζω ότι στα μοναστήρια οι γυναίκες πρέπει να φορούν φούστα κάτω από το γόνατο και οι άντρες μακρύ παντελόνι. Αν δεν έχετε, δίνουν μαντίλες στην είσοδο.", "We'll visit two monasteries instead of three, because one is closed that day. I remind you that in the monasteries women must wear a skirt below the knee and men long trousers. If you don't have one, they give out wraps at the entrance."),
  L("Οργανώτρια", "f", "Λόγω της αλλαγής, η τιμή μειώνεται κατά πέντε ευρώ, και θα σας επιστρέψουμε τη διαφορά στο λεωφορείο. Αν δεν σας βολεύει πια η ώρα, ενημερώστε με μέχρι την Πέμπτη, γιατί υπάρχουν τρία άτομα σε λίστα αναμονής.", "Because of the change, the price goes down by five euros, and we'll refund the difference on the coach. If the time no longer suits you, let me know by Thursday, because there are three people on a waiting list."),
 ],
 "questions": [
  Q("Γιατί θα φύγουν μισή ώρα νωρίτερα;", ["Γιατί θα επισκεφθούν περισσότερα μοναστήρια", "Γιατί το λεωφορείο χάλασε και η εταιρεία δίνει άλλο, μικρότερο", "Γιατί αναμένεται κίνηση στον δρόμο", "Γιατί άλλαξε ο οδηγός"], 1, "το λεωφορείο που είχαμε κλείσει χάλασε και η εταιρεία μάς δίνει άλλο, λίγο μικρότερο"),
  Q("Πόσα μοναστήρια θα επισκεφθούν;", ["Ένα", "Τρία", "Τέσσερα", "Δύο"], 3, "Θα επισκεφθούμε δύο μοναστήρια αντί για τρία"),
  Q("Τι θα γίνει με τη διαφορά στην τιμή;", ["Θα την επιστρέψουν στο λεωφορείο", "Θα χρησιμοποιηθεί για φαγητό", "Θα δοθεί στα μοναστήρια", "Θα την επιστρέψουν με τραπεζική μεταφορά"], 0, "θα σας επιστρέψουμε τη διαφορά στο λεωφορείο"),
 ],
 "gloss": {"πολιτιστικό": "πολιτιστικός σύλλογος — cultural association", "μοναστήρια": "μοναστήρι — monastery", "μαντίλες": "μαντίλα — shawl, wrap", "μειώνεται": "μειώνομαι — to be reduced", "διαφορά": "διαφορά — difference", "βολεύει": "βολεύω — to suit", "αναμονής": "λίστα αναμονής — waiting list"}
})

ITEMS.append({
 "id": "l105-dia-skylos-pou-gavgizei", "title": "Ο σκύλος που γαβγίζει όλη μέρα", "title_en": "The dog that barks all day", "type": "dialogue", "level": "B2",
 "context_el": "Μια γυναίκα χτυπά την πόρτα του γείτονά της.",
 "script": [
  L("Μαρίνα", "f", "Καλησπέρα, κύριε Θανάση. Συγγνώμη για την ενόχληση. Είμαι η Μαρίνα από τον δεύτερο.", "Good evening, Mr Thanasis. Sorry to bother you. I'm Marina from the second floor."),
  L("Θανάσης", "m", "Καλησπέρα. Τι συμβαίνει;", "Good evening. What's the matter?"),
  L("Μαρίνα", "f", "Δουλεύω από το σπίτι τις τελευταίες εβδομάδες και... ο σκύλος σας γαβγίζει σχεδόν όλη μέρα, όσο λείπετε. Χθες είχα μια βιντεοκλήση με πελάτες και αναγκάστηκα να τη διακόψω.", "I've been working from home for the last few weeks and... your dog barks almost all day while you're out. Yesterday I had a video call with clients and I had to cut it short."),
  L("Θανάσης", "m", "Αλήθεια; Δεν είχα ιδέα. Όταν γυρίζω το βράδυ είναι πάντα ήσυχος. Τον πήραμε από το καταφύγιο πριν από δύο μήνες και φαίνεται ότι δεν του αρέσει να μένει μόνος.", "Really? I had no idea. When I come back in the evening he's always quiet. We got him from the shelter two months ago and it seems he doesn't like being left alone."),
  L("Μαρίνα", "f", "Το φαντάστηκα. Δεν θέλω να σας δημιουργήσω πρόβλημα, απλώς σκέφτηκα να σας το πω πριν παραπονεθεί κάποιος άλλος στη γενική συνέλευση.", "I thought so. I don't want to cause you trouble, I just thought I'd tell you before someone else complains at the residents' meeting."),
  L("Θανάσης", "m", "Σας ευχαριστώ που ήρθατε πρώτα σε μένα. Θα μιλήσω με μια εκπαιδεύτρια σκύλων που μου σύστησαν. Και από την επόμενη εβδομάδα η κόρη μου θα έρχεται το μεσημέρι να τον βγάζει βόλτα.", "Thank you for coming to me first. I'll talk to a dog trainer who was recommended to me. And from next week my daughter will come at midday to take him for a walk."),
  L("Μαρίνα", "f", "Πολύ καλή ιδέα. Κι αν κάποια μέρα δεν μπορεί εκείνη, χτυπήστε μου. Μου αρέσουν πολύ τα σκυλιά.", "Very good idea. And if one day she can't, knock on my door. I really like dogs."),
 ],
 "questions": [
  Q("Γιατί ενοχλείται η Μαρίνα;", ["Γιατί ο σκύλος γαβγίζει σχεδόν όλη μέρα όσο λείπει ο γείτονας", "Γιατί ο σκύλος λερώνει τη σκάλα", "Γιατί ο γείτονας βάζει δυνατά μουσική", "Γιατί ο σκύλος τη δάγκωσε"], 0, "ο σκύλος σας γαβγίζει σχεδόν όλη μέρα, όσο λείπετε"),
  Q("Γιατί πιστεύει ο κύριος Θανάσης ότι γαβγίζει ο σκύλος;", ["Γιατί πεινάει", "Γιατί είναι άρρωστος", "Γιατί δεν του αρέσει να μένει μόνος", "Γιατί φοβάται τους γείτονες"], 2, "φαίνεται ότι δεν του αρέσει να μένει μόνος"),
  Q("Τι θα κάνει η κόρη του από την επόμενη εβδομάδα;", ["Θα πάρει τον σκύλο στο σπίτι της", "Θα έρχεται το μεσημέρι να τον βγάζει βόλτα", "Θα μιλήσει στη γενική συνέλευση", "Θα τον πάει σε εκπαιδεύτρια"], 1, "η κόρη μου θα έρχεται το μεσημέρι να τον βγάζει βόλτα"),
 ],
 "gloss": {"ενόχληση": "ενόχληση — bother, disturbance", "γαβγίζει": "γαβγίζω — to bark", "βιντεοκλήση": "βιντεοκλήση — video call", "καταφύγιο": "καταφύγιο ζώων — animal shelter", "παραπονεθεί": "παραπονιέμαι — to complain", "συνέλευση": "γενική συνέλευση — residents' meeting", "εκπαιδεύτρια": "εκπαιδεύτρια σκύλων — dog trainer (f.)"}
})

ITEMS.append({
 "id": "l105-int-grammi-voitheias", "title": "Στην άλλη άκρη της γραμμής βοήθειας", "title_en": "At the other end of the helpline", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια ψυχολόγο που απαντά σε μια τηλεφωνική γραμμή ψυχολογικής υποστήριξης.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσα χρόνια δουλεύετε στη γραμμή;", "How many years have you worked on the line?"),
  L("Ψυχολόγος", "f", "Εννιά. Στην αρχή ήμουν εθελόντρια, όσο έκανα το μεταπτυχιακό μου, και αργότερα έγινα υπεύθυνη της βραδινής βάρδιας. Η γραμμή λειτουργεί όλο το εικοσιτετράωρο, αλλά οι περισσότερες κλήσεις έρχονται μετά τις έντεκα το βράδυ, όταν το σπίτι ησυχάζει και οι σκέψεις δυναμώνουν.", "Nine. At first I was a volunteer, while I was doing my master's, and later I became head of the evening shift. The line runs round the clock, but most calls come after eleven at night, when the house goes quiet and thoughts get louder."),
  L("Δημοσιογράφος", "m", "Ποιοι σας τηλεφωνούν;", "Who calls you?"),
  L("Ψυχολόγος", "f", "Όλοι. Φοιτητές πριν από τις εξετάσεις, γονείς εξαντλημένοι, ηλικιωμένοι που δεν έχουν μιλήσει με άνθρωπο όλη τη μέρα. Πολλοί ξεκινούν λέγοντας «Δεν ξέρω γιατί πήρα, δεν είναι κάτι σοβαρό». Η πρώτη μας δουλειά δεν είναι να δώσουμε συμβουλές, αλλά να ακούσουμε χωρίς να κρίνουμε.", "Everyone. Students before exams, exhausted parents, elderly people who haven't spoken to anyone all day. Many begin by saying 'I don't know why I called, it's nothing serious.' Our first job isn't to give advice, but to listen without judging."),
  L("Δημοσιογράφος", "m", "Πώς αντέχετε ψυχολογικά;", "How do you cope psychologically?"),
  L("Ψυχολόγος", "f", "Μετά από κάθε βάρδια συζητάμε τις δύσκολες κλήσεις με την ομάδα, και μια φορά τον μήνα έχουμε εποπτεία από έναν πιο έμπειρο συνάδελφο. Και έχω μάθει να κλείνω την πόρτα όταν φεύγω. Αν κουβαλάω όλες τις ιστορίες στο σπίτι, την επόμενη μέρα δεν θα μπορώ να ακούσω κανέναν.", "After each shift we discuss the difficult calls with the team, and once a month we have supervision from a more experienced colleague. And I've learnt to close the door when I leave. If I carry all the stories home, the next day I won't be able to listen to anyone."),
 ],
 "questions": [
  Q("Πότε έρχονται οι περισσότερες κλήσεις;", ["Νωρίς το πρωί", "Το μεσημέρι", "Μετά τις έντεκα το βράδυ", "Τα Σαββατοκύριακα"], 2, "οι περισσότερες κλήσεις έρχονται μετά τις έντεκα το βράδυ"),
  Q("Ποια είναι, κατά την ψυχολόγο, η πρώτη τους δουλειά;", ["Να ακούσουν χωρίς να κρίνουν", "Να δώσουν συμβουλές", "Να στείλουν τον καλούντα σε γιατρό", "Να κρατήσουν τη συζήτηση σύντομη"], 0, "να ακούσουμε χωρίς να κρίνουμε"),
  Q("Τι κάνουν μετά από κάθε βάρδια;", ["Γράφουν αναφορά για κάθε κλήση", "Συζητούν τις δύσκολες κλήσεις με την ομάδα", "Παίρνουν μια μέρα άδεια", "Τηλεφωνούν ξανά στους καλούντες"], 1, "Μετά από κάθε βάρδια συζητάμε τις δύσκολες κλήσεις με την ομάδα"),
 ],
 "gloss": {"υποστήριξης": "υποστήριξη — support", "μεταπτυχιακό": "μεταπτυχιακό — master's degree", "εικοσιτετράωρο": "όλο το εικοσιτετράωρο — round the clock", "εξαντλημένοι": "εξαντλημένος — exhausted", "κρίνουμε": "κρίνω — to judge", "εποπτεία": "εποπτεία — supervision", "κουβαλάω": "κουβαλάω — to carry"}
})

ITEMS.append({
 "id": "l105-rep-choros-parkinson", "title": "Χορός για ανθρώπους με Πάρκινσον", "title_en": "Dance for people with Parkinson's", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για την υγεία.",
 "script": [
  L("Ρεπόρτερ", "f", "Σε μια αίθουσα χορού στο κέντρο της πόλης, δεκαπέντε άνθρωποι στέκονται σε κύκλο. Κάποιοι κρατούν μπαστούνι, ένας κάθεται σε καρέκλα. Όλοι έχουν τη νόσο Πάρκινσον, μια πάθηση του νευρικού συστήματος που προκαλεί τρέμουλο, δυσκαμψία και δυσκολία στο περπάτημα.", "In a dance studio in the town centre, fifteen people stand in a circle. Some hold a walking stick, one sits on a chair. They all have Parkinson's disease, a condition of the nervous system that causes tremor, stiffness and difficulty walking."),
  L("Δασκάλα", "f", "Η μουσική βοηθά το σώμα να βρει έναν ρυθμό που η ασθένεια του έχει πάρει. Ξεκινάμε πάντα καθιστοί, με κινήσεις των χεριών, και σιγά-σιγά σηκωνόμαστε. Ορισμένες μελέτες δείχνουν ότι ο χορός μπορεί να βελτιώσει την ισορροπία και το βάδισμα, αλλά δεν αντικαθιστά τη φαρμακευτική αγωγή.", "Music helps the body find a rhythm that the illness has taken away from it. We always start seated, with arm movements, and gradually stand up. Some studies show that dance may improve balance and walking, but it doesn't replace medication."),
  L("Ρεπόρτερ", "f", "Ο κύριος Ανδρέας, εβδομήντα δύο χρονών, έρχεται κάθε Τρίτη με τη σύζυγό του, που χορεύει μαζί του. «Πριν από έναν χρόνο φοβόμουν να βγω από το σπίτι», λέει. «Τώρα πάμε και σε γλέντια.» Τα μαθήματα είναι δωρεάν, χάρη σε έναν σύλλογο ασθενών, και η δασκάλα ψάχνει εθελοντές για ένα δεύτερο τμήμα.", "Mr Andreas, seventy-two, comes every Tuesday with his wife, who dances with him. 'A year ago I was afraid to leave the house,' he says. 'Now we even go to parties.' The classes are free, thanks to a patients' association, and the teacher is looking for volunteers for a second group."),
 ],
 "questions": [
  Q("Πώς ξεκινά πάντα το μάθημα;", ["Με τρέξιμο", "Καθιστοί, με κινήσεις των χεριών", "Με χορό σε ζευγάρια", "Με ασκήσεις αναπνοής στο πάτωμα"], 1, "Ξεκινάμε πάντα καθιστοί, με κινήσεις των χεριών"),
  Q("Τι λέει η δασκάλα για τον χορό και τα φάρμακα;", ["Ότι ο χορός μπορεί να αντικαταστήσει τα φάρμακα", "Ότι οι μαθητές δεν πρέπει να παίρνουν φάρμακα πριν από το μάθημα", "Ότι τα φάρμακα κάνουν τον χορό δύσκολο", "Ότι ο χορός δεν αντικαθιστά τη φαρμακευτική αγωγή"], 3, "δεν αντικαθιστά τη φαρμακευτική αγωγή"),
  Q("Τι έχει αλλάξει για τον κύριο Ανδρέα;", ["Πριν φοβόταν να βγει από το σπίτι, τώρα πηγαίνει και σε γλέντια", "Δεν χρειάζεται πια μπαστούνι", "Έγινε δάσκαλος χορού", "Γνώρισε τη σύζυγό του στα μαθήματα"], 0, "Πριν από έναν χρόνο φοβόμουν να βγω από το σπίτι"),
 ],
 "gloss": {"νόσο": "νόσος — disease", "πάθηση": "πάθηση — condition, disorder", "τρέμουλο": "τρέμουλο — tremor", "δυσκαμψία": "δυσκαμψία — stiffness", "ισορροπία": "ισορροπία — balance", "βάδισμα": "βάδισμα — walking, gait", "αγωγή": "φαρμακευτική αγωγή — medication", "γλέντια": "γλέντι — party, celebration"}
})

ITEMS.append({
 "id": "l105-rep-poulia-tis-polis", "title": "Μετρώντας τα πουλιά της πόλης", "title_en": "Counting the city's birds", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για το περιβάλλον.",
 "script": [
  L("Ρεπόρτερ", "m", "Είναι επτά το πρωί της Κυριακής και σε ένα πάρκο της πόλης μια ομάδα ανθρώπων με κιάλια στέκεται σιωπηλή κάτω από έναν πλάτανο. Είναι μέλη μιας ομάδας εθελοντών που κάθε μήνα καταγράφουν τα πουλιά που ζουν στην πόλη.", "It's seven on Sunday morning and in a city park a group of people with binoculars stands silently under a plane tree. They are members of a volunteer group that records the birds living in the city every month."),
  L("Συντονίστρια", "f", "Οι περισσότεροι νομίζουν ότι στην πόλη υπάρχουν μόνο περιστέρια και σπουργίτια. Εμείς έχουμε καταγράψει πάνω από πενήντα είδη μέσα σε τρία χρόνια: κοτσύφια, καρδερίνες, δρυοκολάπτες, ακόμη και ένα γεράκι που φωλιάζει σε ένα καμπαναριό. Τα στοιχεία μας τα στέλνουμε σε μια ηλεκτρονική βάση δεδομένων που χρησιμοποιούν και επιστήμονες.", "Most people think there are only pigeons and sparrows in the city. We have recorded more than fifty species in three years: blackbirds, goldfinches, woodpeckers, even a falcon nesting in a bell tower. We send our data to an online database that scientists also use."),
  L("Ρεπόρτερ", "m", "Δεν χρειάζεται να είναι κανείς ειδικός για να συμμετάσχει. Οι νέοι εθελοντές μαθαίνουν πρώτα να αναγνωρίζουν τα πουλιά από τη φωνή τους, γιατί συχνά τα ακούς πριν τα δεις. Η ομάδα ζητά από τον δήμο να μην κόβει τα δέντρα την άνοιξη, όταν τα πουλιά κάνουν φωλιές.", "You don't need to be an expert to take part. New volunteers first learn to recognise birds by their song, because you often hear them before you see them. The group is asking the municipality not to cut trees in spring, when the birds are nesting."),
 ],
 "questions": [
  Q("Πόσα είδη πουλιών έχει καταγράψει η ομάδα;", ["Λιγότερα από δέκα", "Πάνω από πενήντα μέσα σε τρία χρόνια", "Μόνο περιστέρια και σπουργίτια", "Εκατό μέσα σε έναν χρόνο"], 1, "Εμείς έχουμε καταγράψει πάνω από πενήντα είδη μέσα σε τρία χρόνια"),
  Q("Τι μαθαίνουν πρώτα οι νέοι εθελοντές;", ["Να φωτογραφίζουν τα πουλιά", "Να φτιάχνουν φωλιές", "Να χρησιμοποιούν τη βάση δεδομένων", "Να αναγνωρίζουν τα πουλιά από τη φωνή τους"], 3, "μαθαίνουν πρώτα να αναγνωρίζουν τα πουλιά από τη φωνή τους"),
  Q("Τι ζητά η ομάδα από τον δήμο;", ["Να φυτέψει περισσότερα δέντρα", "Να βάλει ταΐστρες στα πάρκα", "Να μην κόβει τα δέντρα την άνοιξη", "Να κλείνει τα πάρκα το πρωί"], 2, "να μην κόβει τα δέντρα την άνοιξη"),
 ],
 "gloss": {"κιάλια": "κιάλια — binoculars", "πλάτανο": "πλάτανος — plane tree", "σπουργίτια": "σπουργίτι — sparrow", "κοτσύφια": "κοτσύφι — blackbird", "καρδερίνες": "καρδερίνα — goldfinch", "δρυοκολάπτες": "δρυοκολάπτης — woodpecker", "φωλιάζει": "φωλιάζω — to nest", "καμπαναριό": "καμπαναριό — bell tower"}
})

ITEMS.append({
 "id": "l105-mono-aftoschediasmos", "title": "Τι μου έμαθε ένα μάθημα αυτοσχεδιασμού", "title_en": "What an improv class taught me", "type": "monologue", "level": "B2",
 "context_el": "Ένας άντρας μιλά σε ένα podcast για μια εμπειρία του.",
 "script": [
  L("Στέφανος", "m", "Είμαι λογιστής και σε όλη μου τη ζωή απέφευγα να μιλάω μπροστά σε κόσμο. Στις συσκέψεις κοκκίνιζα και ξεχνούσα τι ήθελα να πω. Πέρσι μια φίλη με γράφτηκε, σχεδόν με το ζόρι, σε ένα μάθημα θεατρικού αυτοσχεδιασμού.", "I'm an accountant and all my life I avoided speaking in front of people. In meetings I'd go red and forget what I wanted to say. Last year a friend signed me up, almost by force, for an improvised theatre class."),
  L("Στέφανος", "m", "Το πρώτο βράδυ ήθελα να φύγω. Ο δάσκαλος μάς έβαλε ανά δύο και μας είπε να παίξουμε μια σκηνή σε ένα ασανσέρ που κόλλησε, χωρίς να έχουμε προετοιμαστεί καθόλου. Ο βασικός κανόνας ήταν απλός: ό,τι σου προτείνει ο άλλος, το δέχεσαι και προσθέτεις κάτι δικό σου. Λέμε «ναι, και…», ποτέ «όχι, αλλά…».", "The first evening I wanted to leave. The teacher put us in pairs and told us to play a scene in a stuck lift, without any preparation at all. The basic rule was simple: whatever the other person suggests, you accept it and add something of your own. We say 'yes, and…', never 'no, but…'."),
  L("Στέφανος", "m", "Δεν έγινα ηθοποιός, ούτε το θέλω. Όμως έμαθα ότι το λάθος δεν είναι καταστροφή, είναι υλικό για την επόμενη ατάκα. Τον περασμένο μήνα παρουσίασα τον προϋπολογισμό της εταιρείας μπροστά σε σαράντα άτομα. Μου έπεσαν οι σημειώσεις στο πάτωμα, γέλασα, γέλασαν κι εκείνοι, και συνέχισα.", "I didn't become an actor, nor do I want to. But I learnt that a mistake isn't a disaster, it's material for the next line. Last month I presented the company's budget in front of forty people. My notes fell on the floor, I laughed, they laughed too, and I carried on."),
 ],
 "questions": [
  Q("Πώς βρέθηκε ο Στέφανος στο μάθημα;", ["Τον έγραψε μια φίλη του, σχεδόν με το ζόρι", "Το πρότεινε η εταιρεία του", "Ήθελε από μικρός να γίνει ηθοποιός", "Το είδε σε μια διαφήμιση"], 0, "μια φίλη με γράφτηκε, σχεδόν με το ζόρι"),
  Q("Ποιος ήταν ο βασικός κανόνας του μαθήματος;", ["Να μαθαίνεις το κείμενο απέξω", "Να μη μιλάς αν δεν είσαι σίγουρος", "Να δέχεσαι ό,τι σου προτείνει ο άλλος και να προσθέτεις κάτι δικό σου", "Να διορθώνεις τα λάθη του συνεργάτη σου"], 2, "ό,τι σου προτείνει ο άλλος, το δέχεσαι και προσθέτεις κάτι δικό σου"),
  Q("Τι έκανε όταν του έπεσαν οι σημειώσεις;", ["Σταμάτησε την παρουσίαση", "Ζήτησε συγγνώμη και έφυγε", "Ζήτησε από έναν συνάδελφο να συνεχίσει", "Γέλασε και συνέχισε"], 3, "γέλασα, γέλασαν κι εκείνοι, και συνέχισα"),
 ],
 "gloss": {"συσκέψεις": "σύσκεψη — meeting", "κοκκίνιζα": "κοκκινίζω — to blush", "ζόρι": "με το ζόρι — by force, reluctantly", "αυτοσχεδιασμού": "αυτοσχεδιασμός — improvisation", "ασανσέρ": "ασανσέρ — lift, elevator", "ατάκα": "ατάκα — line (in a play)", "προϋπολογισμό": "προϋπολογισμός — budget"}
})

ITEMS.append({
 "id": "l105-mono-choris-tileorasi", "title": "Γιατί δεν έχουμε τηλεόραση στο σπίτι", "title_en": "Why we don't have a TV at home", "type": "monologue", "level": "B2",
 "context_el": "Μια μητέρα μιλά σε μια ραδιοφωνική εκπομπή για την οικογένεια.",
 "script": [
  L("Αλεξάνδρα", "f", "Όταν μετακομίσαμε πριν από τέσσερα χρόνια, η τηλεόραση έσπασε στη μεταφορά. Είπαμε να περιμένουμε λίγο πριν πάρουμε καινούργια. Αυτό το «λίγο» κρατάει ακόμα.", "When we moved house four years ago, the TV broke in transit. We said we'd wait a bit before getting a new one. That 'bit' is still going on."),
  L("Αλεξάνδρα", "f", "Τους πρώτους μήνες τα παιδιά παραπονιόντουσαν συνέχεια. Μετά άρχισαν να βρίσκουν άλλα πράγματα: επιτραπέζια, ζωγραφική, ο μεγάλος έμαθε κιθάρα από βίντεο στο λάπτοπ. Γιατί δεν είμαστε και ήρωες· βλέπουμε ταινίες, αλλά τις διαλέγουμε, μια φορά την εβδομάδα, όλοι μαζί, με ποπ κορν.", "For the first few months the children complained all the time. Then they started finding other things: board games, drawing, the eldest learnt guitar from videos on the laptop. Because we're not heroes, either; we watch films, but we choose them, once a week, all together, with popcorn."),
  L("Αλεξάνδρα", "f", "Το μεγαλύτερο κέρδος είναι το βραδινό τραπέζι. Πριν, τρώγαμε με τις ειδήσεις ανοιχτές και κανείς δεν μιλούσε. Τώρα μαθαίνω τι έγινε στο σχολείο, ποιος μάλωσε με ποιον. Δεν λέω ότι όλοι πρέπει να πετάξουν την τηλεόρασή τους. Λέω μόνο ότι αξίζει να δοκιμάσει κανείς έναν μήνα χωρίς αυτήν.", "The biggest gain is the dinner table. Before, we ate with the news on and nobody talked. Now I find out what happened at school, who fell out with whom. I'm not saying everyone should throw out their TV. I'm only saying it's worth trying a month without it."),
 ],
 "questions": [
  Q("Γιατί έμειναν χωρίς τηλεόραση;", ["Γιατί έσπασε στη μετακόμιση και δεν πήραν καινούργια", "Γιατί ήταν πολύ ακριβή", "Γιατί το ζήτησαν τα παιδιά", "Γιατί δεν είχε θέση στο νέο σπίτι"], 0, "η τηλεόραση έσπασε στη μεταφορά"),
  Q("Πώς βλέπουν ταινίες τώρα;", ["Δεν βλέπουν καθόλου ταινίες", "Κάθε βράδυ στο λάπτοπ", "Τις διαλέγουν, μια φορά την εβδομάδα, όλοι μαζί", "Μόνο στον κινηματογράφο"], 2, "τις διαλέγουμε, μια φορά την εβδομάδα, όλοι μαζί"),
  Q("Ποιο είναι για την Αλεξάνδρα το μεγαλύτερο κέρδος;", ["Τα παιδιά διαβάζουν περισσότερο", "Το βραδινό τραπέζι, όπου πλέον μιλάνε", "Ξοδεύουν λιγότερα χρήματα", "Κοιμούνται νωρίτερα"], 1, "Το μεγαλύτερο κέρδος είναι το βραδινό τραπέζι"),
 ],
 "gloss": {"μεταφορά": "μεταφορά — transport, move", "παραπονιόντουσαν": "παραπονιέμαι — to complain", "επιτραπέζια": "επιτραπέζια — board games", "ήρωες": "ήρωας — hero", "κέρδος": "κέρδος — gain, benefit", "μάλωσε": "μαλώνω — to quarrel"}
})

ITEMS.append({
 "id": "l105-c1-astiki-thermiki-nisida", "title": "Γιατί οι πόλεις είναι πιο ζεστές από την ύπαιθρο;", "title_en": "Why are cities hotter than the countryside?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια φυσικό του περιβάλλοντος σε μια εκπομπή εκλαΐκευσης της επιστήμης.",
 "script": [
  L("Επιστήμονας", "f", "Αν ένα καλοκαιρινό βράδυ οδηγήσετε από το κέντρο μιας μεγάλης πόλης προς την ύπαιθρο, με ένα θερμόμετρο στο αυτοκίνητο, θα δείτε τη θερμοκρασία να πέφτει όσο απομακρύνεστε από τις πολυκατοικίες. Το φαινόμενο ονομάζεται αστική θερμική νησίδα, και μελέτες για την Αθήνα έχουν καταγράψει διαφορές αρκετών βαθμών ανάμεσα στο κέντρο και στα προάστια με πολύ πράσινο.", "If on a summer evening you drive from the centre of a big city towards the countryside, with a thermometer in the car, you will see the temperature fall as you move away from the apartment blocks. The phenomenon is called the urban heat island, and studies of Athens have recorded differences of several degrees between the centre and leafy suburbs."),
  L("Επιστήμονας", "f", "Οι αιτίες είναι αρκετές. Η άσφαλτος και το σκυρόδεμα απορροφούν την ηλιακή ακτινοβολία όλη τη μέρα και την αποδίδουν σιγά σιγά τη νύχτα, γι' αυτό η διαφορά είναι συνήθως μεγαλύτερη μετά τη δύση του ηλίου. Η έλλειψη βλάστησης σημαίνει λιγότερη εξάτμιση, άρα λιγότερη φυσική ψύξη. Οι ψηλοί, πυκνοί δρόμοι εμποδίζουν τον αέρα να κυκλοφορήσει, και τα κλιματιστικά και τα αυτοκίνητα προσθέτουν τη δική τους θερμότητα: όσο πιο ζεστή η πόλη, τόσο περισσότερα κλιματιστικά, και όσο περισσότερα κλιματιστικά, τόσο πιο ζεστή η πόλη.", "There are several causes. Asphalt and concrete absorb solar radiation all day and release it slowly at night, which is why the difference is usually greatest after sunset. The lack of vegetation means less evaporation, and therefore less natural cooling. Tall, dense streets prevent air from circulating, and air conditioners and cars add their own heat: the hotter the city, the more air conditioners, and the more air conditioners, the hotter the city."),
  L("Επιστήμονας", "f", "Οι λύσεις δεν είναι μυστικές, αλλά απαιτούν σχέδιο και υπομονή. Δέντρα στους δρόμους, που σκιάζουν και δροσίζουν. Ταράτσες βαμμένες με ανοιχτόχρωμα υλικά που αντανακλούν το φως, ή φυτεμένα δώματα. Ακόμη και τα σιντριβάνια και τα μικρά πάρκα τσέπης βοηθούν τοπικά. Καμία από αυτές τις παρεμβάσεις δεν θα δροσίσει μόνη της μια ολόκληρη πόλη· όλες μαζί, όμως, μπορούν να κάνουν τις θερινές νύχτες πιο υποφερτές για εκείνους που δεν έχουν πού να καταφύγουν.", "The solutions aren't secret, but they require planning and patience. Trees in the streets, which provide shade and cool the air. Roofs painted with light-coloured materials that reflect light, or green roofs. Even fountains and small pocket parks help locally. None of these interventions will cool a whole city on its own; all together, though, they can make summer nights more bearable for those who have nowhere to escape to."),
 ],
 "questions": [
  Q("Τι έχουν καταγράψει μελέτες για την Αθήνα;", ["Ότι η θερμοκρασία είναι ίδια παντού", "Διαφορές αρκετών βαθμών ανάμεσα στο κέντρο και στα προάστια με πολύ πράσινο", "Ότι τα προάστια είναι πιο ζεστά από το κέντρο", "Ότι η διαφορά εμφανίζεται μόνο τον χειμώνα"], 1, "μελέτες για την Αθήνα έχουν καταγράψει διαφορές αρκετών βαθμών ανάμεσα στο κέντρο και στα προάστια με πολύ πράσινο"),
  Q("Γιατί η διαφορά είναι συνήθως μεγαλύτερη μετά τη δύση του ηλίου;", ["Γιατί η άσφαλτος και το σκυρόδεμα αποδίδουν σιγά σιγά τη νύχτα τη θερμότητα που απορρόφησαν", "Γιατί τη νύχτα φυσάει περισσότερο στην ύπαιθρο", "Γιατί τη νύχτα ανάβουν τα φώτα της πόλης", "Γιατί τη νύχτα κυκλοφορούν περισσότερα αυτοκίνητα"], 0, "την αποδίδουν σιγά σιγά τη νύχτα, γι' αυτό η διαφορά είναι συνήθως μεγαλύτερη μετά τη δύση του ηλίου"),
  Q("Ποιον φαύλο κύκλο περιγράφει η επιστήμονας;", ["Περισσότερα δέντρα, περισσότερα έντομα", "Περισσότερη κίνηση, περισσότερος θόρυβος", "Όσο πιο ζεστή η πόλη, τόσο περισσότερα κλιματιστικά, που την κάνουν ακόμη πιο ζεστή", "Λιγότερη βροχή, λιγότερο πράσινο"], 2, "όσο πιο ζεστή η πόλη, τόσο περισσότερα κλιματιστικά, και όσο περισσότερα κλιματιστικά, τόσο πιο ζεστή η πόλη"),
  Q("Τι λέει για τις λύσεις;", ["Ότι μία από αυτές αρκεί για μια ολόκληρη πόλη", "Ότι είναι πολύ ακριβές για να εφαρμοστούν", "Ότι δεν υπάρχουν ακόμη αποτελεσματικές λύσεις", "Ότι καμία δεν αρκεί μόνη της, αλλά όλες μαζί μπορούν να κάνουν τις νύχτες πιο υποφερτές"], 3, "Καμία από αυτές τις παρεμβάσεις δεν θα δροσίσει μόνη της μια ολόκληρη πόλη· όλες μαζί, όμως, μπορούν να κάνουν τις θερινές νύχτες πιο υποφερτές"),
 ],
 "gloss": {"νησίδα": "αστική θερμική νησίδα — urban heat island", "προάστια": "προάστιο — suburb", "σκυρόδεμα": "σκυρόδεμα — concrete", "ακτινοβολία": "ακτινοβολία — radiation", "βλάστησης": "βλάστηση — vegetation", "εξάτμιση": "εξάτμιση — evaporation", "αντανακλούν": "αντανακλώ — to reflect", "δώματα": "δώμα — flat roof", "υποφερτές": "υποφερτός — bearable"}
})

ITEMS.append({
 "id": "l105-c1-metadotiko-gelio", "title": "Γιατί το γέλιο είναι μεταδοτικό;", "title_en": "Why is laughter contagious?", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν νευροεπιστήμονα σε μια ραδιοφωνική εκπομπή.",
 "script": [
  L("Δημοσιογράφος", "f", "Γιατί γελάμε πιο εύκολα όταν γελούν και οι γύρω μας;", "Why do we laugh more easily when those around us are laughing?"),
  L("Επιστήμονας", "m", "Γιατί το γέλιο είναι πρώτα απ' όλα κοινωνικό σήμα, όχι αντίδραση στο αστείο. Ο Αμερικανός ψυχολόγος Ρόμπερτ Προβάιν, που μελέτησε το γέλιο για δεκαετίες, κατέγραφε τι έλεγαν οι άνθρωποι λίγο πριν γελάσουν σε καθημερινές συζητήσεις. Διαπίστωσε ότι στις περισσότερες περιπτώσεις δεν προηγούνταν κάποιο αστείο, αλλά φράσεις εντελώς συνηθισμένες, όπως «Τα λέμε αργότερα». Σύμφωνα με τις παρατηρήσεις του, γελάμε πολύ πιο συχνά όταν βρισκόμαστε με άλλους παρά όταν είμαστε μόνοι.", "Because laughter is first and foremost a social signal, not a reaction to a joke. The American psychologist Robert Provine, who studied laughter for decades, recorded what people said just before they laughed in everyday conversations. He found that in most cases it wasn't a joke that came before, but completely ordinary phrases, such as 'See you later.' According to his observations, we laugh far more often when we're with others than when we're alone."),
  L("Δημοσιογράφος", "f", "Και τι συμβαίνει στον εγκέφαλο όταν ακούμε κάποιον να γελάει;", "And what happens in the brain when we hear someone laugh?"),
  L("Επιστήμονας", "m", "Μελέτες απεικόνισης έχουν δείξει ότι ο ήχος του γέλιου ενεργοποιεί περιοχές του εγκεφάλου που σχετίζονται με την κίνηση των μυών του προσώπου, σαν να προετοιμάζεται ο εγκέφαλος να γελάσει κι εκείνος. Γι' αυτό οι τηλεοπτικές κωμωδίες χρησιμοποιούσαν για χρόνια ηχογραφημένα γέλια: ακόμη κι όταν ξέρουμε ότι είναι ψεύτικα, μας παρασύρουν.", "Imaging studies have shown that the sound of laughter activates areas of the brain related to the movement of facial muscles, as if the brain were getting ready to laugh too. That's why TV comedies used recorded laughter for years: even when we know it's fake, it carries us along."),
  L("Δημοσιογράφος", "f", "Έχει κάποια χρησιμότητα όλο αυτό;", "Is all this of any use?"),
  L("Επιστήμονας", "m", "Πιθανότατα. Το κοινό γέλιο φαίνεται να δυναμώνει τους δεσμούς μιας ομάδας και να εκτονώνει εντάσεις. Όποιος έχει γελάσει ανεξέλεγκτα με έναν φίλο σε μια σοβαρή περίσταση ξέρει ότι μετά από αυτό κάτι έχει αλλάξει ανάμεσά τους. Δεν σημαίνει, βέβαια, ότι κάθε γέλιο είναι φιλικό· υπάρχει και το γέλιο που αποκλείει, εκείνο που λέει «εσύ δεν είσαι από τους δικούς μας».", "Probably. Shared laughter seems to strengthen the bonds of a group and to defuse tension. Anyone who has laughed uncontrollably with a friend on a serious occasion knows that afterwards something has changed between them. That doesn't mean, of course, that all laughter is friendly; there is also the laughter that excludes, the kind that says 'you're not one of us.'"),
 ],
 "questions": [
  Q("Τι διαπίστωσε ο Προβάιν για το τι προηγείται του γέλιου;", ["Ότι προηγείται σχεδόν πάντα ένα αστείο", "Ότι συνήθως προηγούνται εντελώς συνηθισμένες φράσεις", "Ότι οι άνθρωποι γελούν μόνο με ανέκδοτα", "Ότι το γέλιο προηγείται πάντα του αστείου"], 1, "δεν προηγούνταν κάποιο αστείο, αλλά φράσεις εντελώς συνηθισμένες"),
  Q("Πότε γελάμε πιο συχνά, σύμφωνα με τις παρατηρήσεις του;", ["Όταν είμαστε μόνοι", "Όταν είμαστε κουρασμένοι", "Όταν βρισκόμαστε με άλλους", "Όταν βλέπουμε τηλεόραση"], 2, "γελάμε πολύ πιο συχνά όταν βρισκόμαστε με άλλους παρά όταν είμαστε μόνοι"),
  Q("Γιατί οι τηλεοπτικές κωμωδίες χρησιμοποιούσαν ηχογραφημένα γέλια;", ["Γιατί μας παρασύρουν ακόμη κι όταν ξέρουμε ότι είναι ψεύτικα", "Γιατί οι ηθοποιοί δεν ήταν αστείοι", "Γιατί ήταν φθηνότερα από το κοινό", "Γιατί το απαιτούσε ο νόμος"], 0, "ακόμη κι όταν ξέρουμε ότι είναι ψεύτικα, μας παρασύρουν"),
  Q("Τι λέει για το γέλιο που αποκλείει;", ["Ότι δεν υπάρχει", "Ότι είναι το πιο συνηθισμένο", "Ότι δυναμώνει τις φιλίες", "Ότι λέει στον άλλον πως δεν ανήκει στην ομάδα"], 3, "εκείνο που λέει «εσύ δεν είσαι από τους δικούς μας»"),
 ],
 "gloss": {"σήμα": "σήμα — signal", "προηγούνταν": "προηγούμαι — to precede", "απεικόνισης": "μελέτες απεικόνισης — imaging studies", "ενεργοποιεί": "ενεργοποιώ — to activate", "ηχογραφημένα": "ηχογραφημένος — recorded", "παρασύρουν": "παρασύρω — to carry along", "δεσμούς": "δεσμός — bond", "εκτονώνει": "εκτονώνω — to defuse, release", "αποκλείει": "αποκλείω — to exclude"}
})

rnd = random.Random(105)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-105.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
