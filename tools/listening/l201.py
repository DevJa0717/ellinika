# Source for library/listening/listening-201.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l201.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l201-ann-poulia-diadromos", "title": "Καθυστέρηση πτήσεων λόγω πουλιών", "title_en": "Flights delayed because of birds on the runway", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση στην αίθουσα αναμονής ενός περιφερειακού αεροδρομίου.",
 "script": [
  L("Εκφωνήτρια", "f", "Κυρίες και κύριοι, σας ενημερώνουμε ότι όλες οι αναχωρήσεις καθυστερούν περίπου σαράντα λεπτά. Ένα μεγάλο σμήνος από γλάρους έχει καθίσει στον διάδρομο προσγείωσης, και για λόγους ασφαλείας καμία πτήση δεν μπορεί να απογειωθεί πριν απομακρυνθούν τα πουλιά.", "Ladies and gentlemen, we inform you that all departures are delayed by about forty minutes. A large flock of seagulls has settled on the runway, and for safety reasons no flight can take off until the birds have been moved away."),
  L("Εκφωνήτρια", "f", "Το προσωπικό του αεροδρομίου χρησιμοποιεί ειδικά ηχητικά σήματα για να τα διώξει, χωρίς να τα βλάψει. Οι επιβάτες της πτήσης για Αθήνα που έχουν ανταπόκριση με διεθνή πτήση παρακαλούνται να απευθυνθούν στο γκισέ πέντε, όπου θα ελεγχθεί αν χρειάζεται αλλαγή εισιτηρίου.", "Airport staff are using special sound signals to drive them away without harming them. Passengers on the Athens flight who have a connection to an international flight are asked to go to desk five, where it will be checked whether a ticket change is needed."),
  L("Εκφωνήτρια", "f", "Η καφετέρια του πρώτου ορόφου θα προσφέρει στους επιβάτες δωρεάν νερό. Θα σας ενημερώσουμε ξανά μόλις έχουμε νεότερα.", "The café on the first floor will offer passengers free water. We will update you again as soon as we have news."),
 ],
 "questions": [
  Q("Γιατί καθυστερούν οι πτήσεις;", ["Λόγω ομίχλης", "Γιατί ένα σμήνος γλάρων κάθισε στον διάδρομο", "Λόγω απεργίας", "Λόγω βλάβης"], 1, "Ένα μεγάλο σμήνος από γλάρους έχει καθίσει στον διάδρομο προσγείωσης"),
  Q("Ποιοι πρέπει να πάνε στο γκισέ πέντε;", ["Όλοι οι επιβάτες", "Όσοι έχουν ανταπόκριση με διεθνή πτήση", "Όσοι έχουν παιδιά", "Όσοι θέλουν νερό"], 1, "που έχουν ανταπόκριση με διεθνή πτήση"),
  Q("Τι θα προσφέρει η καφετέρια;", ["Δωρεάν καφέ", "Έκπτωση", "Δωρεάν νερό", "Σάντουιτς"], 2, "θα προσφέρει στους επιβάτες δωρεάν νερό"),
 ],
 "gloss": {"σμήνος": "σμήνος — flock, swarm", "γλάρους": "γλάρος — seagull", "διάδρομο": "διάδρομος — runway", "ανταπόκριση": "ανταπόκριση — connection (flight)", "γκισέ": "γκισέ — desk, counter"},
})

ITEMS.append({
 "id": "l201-int-agios-vasilis", "title": "Ένας επαγγελματίας Άγιος Βασίλης", "title_en": "A professional Father Christmas", "type": "interview", "level": "B2",
 "context_el": "Συνέντευξη με έναν συνταξιούχο ηθοποιό που κάθε Δεκέμβριο ντύνεται Άγιος Βασίλης σε ένα εμπορικό κέντρο.",
 "script": [
  L("Δημοσιογράφος", "f", "Η γενειάδα είναι αληθινή;", "Is the beard real?"),
  L("Ηθοποιός", "m", "Αληθινή, και την αφήνω να μακρύνει από τον Αύγουστο. Τα παιδιά τραβάνε πάντα τη γενειάδα για να ελέγξουν. Οι ψεύτικες βγαίνουν, και τότε έχεις πρόβλημα με όλη την ουρά.", "Real, and I let it grow from August. Children always pull the beard to check. The fake ones come off, and then you have a problem with the whole queue."),
  L("Δημοσιογράφος", "f", "Τι ζητάνε τα παιδιά φέτος;", "What are children asking for this year?"),
  L("Ηθοποιός", "m", "Κυρίως ηλεκτρονικά, όπως κάθε χρόνο. Αλλά κάθε μέρα υπάρχει κι ένα παιδί που δεν ζητάει τίποτα για τον εαυτό του. Χθες ένα κοριτσάκι μού ζήτησε να γίνει καλά η γιαγιά του. Τέτοιες στιγμές πρέπει να είσαι πολύ προσεκτικός: δεν μπορείς να υποσχεθείς κάτι που δεν ξέρεις.", "Mostly electronics, as every year. But every day there is also one child who doesn't ask for anything for themselves. Yesterday a little girl asked me for her grandmother to get well. At moments like that you have to be very careful: you can't promise something you don't know."),
  L("Δημοσιογράφος", "f", "Και τι της απαντήσατε;", "And what did you answer her?"),
  L("Ηθοποιός", "m", "Της είπα ότι θα σκέφτομαι τη γιαγιά της κάθε βράδυ, κι ότι κι εκείνη μπορεί να της ζωγραφίσει κάτι. Το πιο δύσκολο σε αυτή τη δουλειά δεν είναι η ζέστη μέσα στη στολή. Είναι να μην κλάψεις μπροστά στα παιδιά.", "I told her I would think of her grandmother every evening, and that she could draw her something. The hardest thing in this job isn't the heat inside the costume. It's not crying in front of the children."),
 ],
 "questions": [
  Q("Γιατί προτιμά αληθινή γενειάδα;", ["Γιατί είναι φθηνότερη", "Γιατί τα παιδιά την τραβάνε για να ελέγξουν", "Γιατί δεν του αρέσουν οι ψεύτικες", "Γιατί είναι πιο ζεστή"], 1, "Τα παιδιά τραβάνε πάντα τη γενειάδα για να ελέγξουν"),
  Q("Τι ζήτησε χθες ένα κοριτσάκι;", ["Ένα κινητό", "Να γίνει καλά η γιαγιά του", "Ένα σκυλάκι", "Να χιονίσει"], 1, "μού ζήτησε να γίνει καλά η γιαγιά του"),
  Q("Ποιο είναι το πιο δύσκολο στη δουλειά του;", ["Η ζέστη μέσα στη στολή", "Οι μεγάλες ουρές", "Να μην κλάψει μπροστά στα παιδιά", "Να θυμάται τα ονόματα"], 2, "Είναι να μην κλάψεις μπροστά στα παιδιά"),
 ],
 "gloss": {"γενειάδα": "γενειάδα — beard", "μακρύνει": "μακραίνω — to grow longer", "ουρά": "ουρά — queue", "υποσχεθείς": "υπόσχομαι — to promise", "στολή": "στολή — costume, uniform"},
})

ITEMS.append({
 "id": "l201-mono-grammata-ston-eafto-mou", "title": "Γράμματα στον εαυτό μου του μέλλοντος", "title_en": "Letters to my future self", "type": "monologue", "level": "B2",
 "context_el": "Ένας νοσηλευτής μιλάει σε ένα podcast για μια συνήθεια που έχει εδώ και χρόνια.",
 "script": [
  L("Νοσηλευτής", "m", "Κάθε χρόνο, την παραμονή της Πρωτοχρονιάς, γράφω ένα γράμμα στον εαυτό μου, το κλείνω σε φάκελο και γράφω απέξω: «Να ανοιχτεί σε δέκα χρόνια». Η ιδέα ήταν της δασκάλας μου στην έκτη δημοτικού. Μας έβαλε να γράψουμε τέτοιο γράμμα και μας το έστειλε με το ταχυδρομείο, δέκα χρόνια αργότερα.", "Every year, on New Year's Eve, I write a letter to myself, seal it in an envelope and write on the outside: 'To be opened in ten years.' The idea came from my teacher in the sixth grade. She had us write such a letter and posted it to us, ten years later."),
  L("Νοσηλευτής", "m", "Όταν το διάβασα, στα είκοσι δύο, γέλασα πολύ: ήθελα να γίνω αστροναύτης και να παντρευτώ την Κατερίνα από το διπλανό θρανίο. Αλλά υπήρχε και μια φράση που με σταμάτησε: «Ελπίζω να είσαι ακόμα καλός με τη γιαγιά». Την άλλη μέρα πήγα να τη δω.", "When I read it, at twenty-two, I laughed a lot: I wanted to become an astronaut and marry Katerina from the next desk. But there was also a sentence that stopped me: 'I hope you're still nice to Grandma.' The next day I went to see her."),
  L("Νοσηλευτής", "m", "Από τότε γράφω κάθε χρόνο. Δεν γράφω στόχους, γιατί ο μελλοντικός εαυτός μου μπορεί να μην τους θέλει πια. Γράφω τι με απασχολεί, τι με κάνει χαρούμενο και μια ερώτηση. Φέτος ανοίγω το πρώτο γράμμα που έγραψα μόνος μου. Ομολογώ ότι φοβάμαι λίγο την ερώτηση.", "Since then I write every year. I don't write goals, because my future self may no longer want them. I write what's on my mind, what makes me happy, and one question. This year I open the first letter I wrote on my own. I admit I'm a little afraid of the question."),
 ],
 "questions": [
  Q("Από πού πήρε την ιδέα;", ["Από ένα βιβλίο", "Από τη δασκάλα του στην έκτη δημοτικού", "Από τη γιαγιά του", "Από ένα podcast"], 1, "Η ιδέα ήταν της δασκάλας μου στην έκτη δημοτικού"),
  Q("Τι έκανε μετά τη φράση για τη γιαγιά;", ["Της έγραψε γράμμα", "Της τηλεφώνησε", "Πήγε να τη δει την άλλη μέρα", "Την κάλεσε για φαγητό"], 2, "Την άλλη μέρα πήγα να τη δω"),
  Q("Γιατί δεν γράφει στόχους στα γράμματα;", ["Γιατί δεν έχει στόχους", "Γιατί ο μελλοντικός εαυτός του μπορεί να μην τους θέλει πια", "Γιατί τους ξεχνάει", "Γιατί είναι προσωπικοί"], 1, "ο μελλοντικός εαυτός μου μπορεί να μην τους θέλει πια"),
 ],
 "gloss": {"παραμονή": "παραμονή — eve", "φάκελο": "φάκελος — envelope", "θρανίο": "θρανίο — school desk", "απασχολεί": "απασχολώ — to be on one's mind, concern", "Ομολογώ": "ομολογώ — to admit"},
})

ITEMS.append({
 "id": "l201-rep-plouti-vivliothiki", "title": "Μια βιβλιοθήκη πάνω σε καΐκι", "title_en": "A library on a fishing boat", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για μια πλωτή βιβλιοθήκη στα μικρά νησιά των Δωδεκανήσων.",
 "script": [
  L("Ρεπόρτερ", "m", "Το καΐκι λέγεται «Ανάγνωσμα» και ήταν κάποτε ψαράδικο. Σήμερα στο αμπάρι του, εκεί όπου άλλοτε έμπαιναν τα ψάρια, υπάρχουν πάνω από δύο χιλιάδες βιβλία. Κάθε καλοκαίρι επισκέπτεται νησιά όπου δεν υπάρχει ούτε βιβλιοπωλείο ούτε βιβλιοθήκη.", "The boat is called 'Anagnosma' and was once a fishing boat. Today in its hold, where the fish used to go, there are over two thousand books. Every summer it visits islands where there is neither a bookshop nor a library."),
  L("Ρεπόρτερ", "m", "Την ιδέα την είχαν δύο αδερφές, μια βιβλιοθηκονόμος και μια καπετάνισσα. Το καΐκι μένει δύο μέρες σε κάθε λιμάνι. Οι κάτοικοι δανείζονται βιβλία και τα επιστρέφουν την επόμενη χρονιά, ή τα αφήνουν στο καφενείο, και τα μαζεύει ο ταχυδρόμος.", "The idea came from two sisters, a librarian and a boat captain. The boat stays two days in each harbour. Residents borrow books and return them the following year, or leave them at the café, and the postman collects them."),
  L("Ρεπόρτερ", "m", "Τα πιο δημοφιλή βιβλία δεν είναι τα μυθιστορήματα, όπως περίμεναν, αλλά οι βιβλίοι μαγειρικής και οι οδηγοί για τον κήπο. Τα παιδιά, πάλι, ζητούν πάντα κόμικς. Μια ηλικιωμένη κάτοικος μάς είπε ότι περιμένει το καΐκι όπως περίμενε παλιά το καράβι με τα γράμματα από την Αμερική.", "The most popular books aren't novels, as they expected, but cookbooks and gardening guides. Children, on the other hand, always ask for comics. An elderly resident told us she waits for the boat the way she used to wait for the ship with the letters from America."),
 ],
 "questions": [
  Q("Πού φυλάγονται τα βιβλία στο καΐκι;", ["Στην καμπίνα", "Στο αμπάρι, όπου άλλοτε έμπαιναν τα ψάρια", "Στο κατάστρωμα", "Σε ένα δεύτερο καΐκι"], 1, "στο αμπάρι του, εκεί όπου άλλοτε έμπαιναν τα ψάρια"),
  Q("Πώς επιστρέφουν οι κάτοικοι τα βιβλία;", ["Με το ταχυδρομείο στην Αθήνα", "Την επόμενη χρονιά ή τα αφήνουν στο καφενείο", "Τα κρατούν για πάντα", "Τα δίνουν στο σχολείο"], 1, "τα επιστρέφουν την επόμενη χρονιά, ή τα αφήνουν στο καφενείο"),
  Q("Ποια βιβλία είναι τα πιο δημοφιλή;", ["Τα μυθιστορήματα", "Τα βιβλία ιστορίας", "Τα βιβλία μαγειρικής και οι οδηγοί για τον κήπο", "Τα ποιήματα"], 2, "οι βιβλίοι μαγειρικής και οι οδηγοί για τον κήπο"),
 ],
 "gloss": {"αμπάρι": "αμπάρι — hold (of a ship)", "βιβλιοθηκονόμος": "βιβλιοθηκονόμος — librarian", "καπετάνισσα": "καπετάνισσα — (female) captain", "δανείζονται": "δανείζομαι — to borrow", "δημοφιλή": "δημοφιλής — popular"},
})

ITEMS.append({
 "id": "l201-rep-scholiko-radiofono", "title": "Οι μαθητές βγάζουν το δικό τους ραδιόφωνο", "title_en": "Pupils run their own school radio", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από ένα γυμνάσιο στα Τρίκαλα.",
 "script": [
  L("Ρεπόρτερ", "f", "Κάθε μέρα, στο μεγάλο διάλειμμα, από τα μεγάφωνα της αυλής ακούγεται μια εκπομπή είκοσι λεπτών. Την ετοιμάζουν οι ίδιοι οι μαθητές, σε ένα μικρό στούντιο που έστησαν σε μια αποθήκη, με μικρόφωνα που δώρισε ένας τοπικός ραδιοφωνικός σταθμός.", "Every day, during the long break, a twenty-minute programme can be heard from the loudspeakers in the yard. The pupils themselves prepare it, in a small studio they set up in a storeroom, with microphones donated by a local radio station."),
  L("Ρεπόρτερ", "f", "Η εκπομπή έχει ειδήσεις του σχολείου, αφιερώσεις, και μια στήλη που λέγεται «Ρωτήστε τον καθηγητή», όπου οι καθηγητές απαντούν ζωντανά σε ερωτήσεις των μαθητών. Η πιο δημοφιλής ερώτηση μέχρι τώρα ήταν γιατί ο διευθυντής φοράει πάντα την ίδια γραβάτα.", "The programme has school news, dedications, and a section called 'Ask the teacher', where teachers answer pupils' questions live. The most popular question so far was why the head always wears the same tie."),
  L("Ρεπόρτερ", "f", "Ο υπεύθυνος καθηγητής λέει ότι το ραδιόφωνο βοήθησε ιδιαίτερα τους ντροπαλούς μαθητές. «Στο μικρόφωνο δεν σε βλέπει κανείς», εξηγεί. «Ένα παιδί που δεν μιλούσε ποτέ στην τάξη έγινε ο καλύτερος εκφωνητής μας.»", "The teacher in charge says the radio has particularly helped shy pupils. 'At the microphone nobody sees you,' he explains. 'A child who never spoke in class became our best announcer.'"),
 ],
 "questions": [
  Q("Πού έστησαν οι μαθητές το στούντιο;", ["Στη βιβλιοθήκη", "Σε μια αποθήκη", "Στο γραφείο του διευθυντή", "Σε έναν ραδιοφωνικό σταθμό"], 1, "σε ένα μικρό στούντιο που έστησαν σε μια αποθήκη"),
  Q("Ποια ήταν η πιο δημοφιλής ερώτηση στη στήλη;", ["Πότε κλείνουν τα σχολεία", "Γιατί ο διευθυντής φοράει πάντα την ίδια γραβάτα", "Γιατί υπάρχουν διαγωνίσματα", "Τι θα φάνε στην εκδρομή"], 1, "γιατί ο διευθυντής φοράει πάντα την ίδια γραβάτα"),
  Q("Ποιους βοήθησε ιδιαίτερα το ραδιόφωνο, κατά τον καθηγητή;", ["Τους καλούς μαθητές", "Τους ντροπαλούς μαθητές", "Τους καθηγητές", "Τους γονείς"], 1, "το ραδιόφωνο βοήθησε ιδιαίτερα τους ντροπαλούς μαθητές"),
 ],
 "gloss": {"μεγάφωνα": "μεγάφωνο — loudspeaker", "αποθήκη": "αποθήκη — storeroom", "αφιερώσεις": "αφιέρωση — dedication", "ντροπαλούς": "ντροπαλός — shy", "εκφωνητής": "εκφωνητής — announcer"},
})

ITEMS.append({
 "id": "l201-news-fokia-xaplostra", "title": "Μια φώκια κοιμήθηκε σε ξαπλώστρα", "title_en": "A monk seal naps on a sunbed", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση σε ένα τοπικό ραδιόφωνο.",
 "script": [
  L("Παρουσιαστής", "m", "Απρόσμενος επισκέπτης σε μια οργανωμένη παραλία της Κεφαλονιάς σήμερα το πρωί: μια νεαρή μεσογειακή φώκια βγήκε από τη θάλασσα και ξάπλωσε σε μια ξαπλώστρα, όπου κοιμήθηκε για σχεδόν δύο ώρες.", "An unexpected visitor at an organised beach in Kefalonia this morning: a young Mediterranean monk seal came out of the sea and lay down on a sunbed, where it slept for almost two hours."),
  L("Παρουσιαστής", "m", "Ο ιδιοκτήτης της καντίνας ειδοποίησε αμέσως το λιμεναρχείο και μια περιβαλλοντική οργάνωση. Μέχρι να φτάσουν οι εθελοντές, οι λουόμενοι είχαν σχηματίσει έναν κύκλο γύρω από τη φώκια και τη φωτογράφιζαν. Οι εθελοντές τούς ζήτησαν να απομακρυνθούν σε απόσταση τουλάχιστον τριάντα μέτρων και να μην κάνουν θόρυβο.", "The canteen owner immediately notified the port authority and an environmental organisation. By the time the volunteers arrived, swimmers had formed a circle around the seal and were photographing it. The volunteers asked them to move back at least thirty metres and not to make noise."),
  L("Παρουσιαστής", "m", "Η μεσογειακή φώκια είναι προστατευόμενο είδος, και η ενόχλησή της απαγορεύεται. Μετά τον ύπνο της, η φώκια γύρισε ήρεμα στη θάλασσα. Ο ιδιοκτήτης της ξαπλώστρας δήλωσε ότι δεν θα τη χρεώσει.", "The Mediterranean monk seal is a protected species, and disturbing it is prohibited. After its nap, the seal calmly returned to the sea. The owner of the sunbed said he would not charge it."),
 ],
 "questions": [
  Q("Πόση ώρα κοιμήθηκε η φώκια;", ["Δέκα λεπτά", "Σχεδόν δύο ώρες", "Όλη τη μέρα", "Μισή ώρα"], 1, "όπου κοιμήθηκε για σχεδόν δύο ώρες"),
  Q("Τι ζήτησαν οι εθελοντές από τους λουόμενους;", ["Να της δώσουν ψάρια", "Να απομακρυνθούν τουλάχιστον τριάντα μέτρα και να μην κάνουν θόρυβο", "Να τη βοηθήσουν να γυρίσει στη θάλασσα", "Να φύγουν από την παραλία"], 1, "να απομακρυνθούν σε απόσταση τουλάχιστον τριάντα μέτρων"),
  Q("Τι δήλωσε αστειευόμενος ο ιδιοκτήτης της ξαπλώστρας;", ["Ότι θα της κρατάει θέση", "Ότι δεν θα τη χρεώσει", "Ότι θα της δώσει όνομα", "Ότι θα κλείσει την παραλία"], 1, "δήλωσε ότι δεν θα τη χρεώσει"),
 ],
 "gloss": {"φώκια": "φώκια — seal", "ξαπλώστρα": "ξαπλώστρα — sunbed", "λουόμενοι": "λουόμενος — swimmer, bather", "απομακρυνθούν": "απομακρύνομαι — to move away", "ενόχλησή": "ενόχληση — disturbance"},
})

ITEMS.append({
 "id": "l201-vm-maia-mathima", "title": "Μήνυμα από τη μαία για το μάθημα προετοιμασίας", "title_en": "A message from the midwife about the antenatal class", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη μαία που οργανώνει μαθήματα για μελλοντικούς γονείς.",
 "script": [
  L("Μαία", "f", "Καλημέρα, κυρία Πετράκη, η Ρένα είμαι, η μαία από το κέντρο υγείας. Σας παίρνω για το μάθημα προετοιμασίας της Πέμπτης. Δυστυχώς η αίθουσα που κάνουμε τα μαθήματα θα βάφεται όλη την εβδομάδα, οπότε το μάθημα μεταφέρεται στη βιβλιοθήκη του δήμου, στον πρώτο όροφο.", "Good morning, Mrs Petraki, it's Rena, the midwife from the health centre. I'm calling about Thursday's antenatal class. Unfortunately the room where we hold the classes will be painted all week, so the class is moving to the municipal library, on the first floor."),
  L("Μαία", "f", "Η ώρα μένει η ίδια, στις έξι. Αυτή τη φορά θα κάνουμε ασκήσεις αναπνοής, γι' αυτό φέρτε ένα μαξιλάρι ή ένα στρώμα γιόγκα και φορέστε άνετα ρούχα. Αν μπορεί, ας έρθει και ο σύζυγός σας, γιατί οι ασκήσεις γίνονται σε ζευγάρια.", "The time stays the same, at six. This time we'll do breathing exercises, so bring a cushion or a yoga mat and wear comfortable clothes. If he can, your husband should come too, because the exercises are done in pairs."),
  L("Μαία", "f", "Η βιβλιοθήκη έχει ασανσέρ, αλλά η είσοδος είναι από το πλάι, από την οδό Αθηνάς, όχι από την πλατεία. Αν έχετε ερωτήσεις, στείλτε μου ένα μήνυμα.", "The library has a lift, but the entrance is at the side, from Athinas Street, not from the square. If you have questions, send me a message."),
 ],
 "questions": [
  Q("Γιατί αλλάζει ο χώρος του μαθήματος;", ["Γιατί η αίθουσα θα βάφεται", "Γιατί η μαία είναι άρρωστη", "Γιατί ήρθαν πολλοί γονείς", "Γιατί χάλασε η θέρμανση"], 0, "η αίθουσα που κάνουμε τα μαθήματα θα βάφεται όλη την εβδομάδα"),
  Q("Γιατί καλό είναι να έρθει και ο σύζυγος;", ["Για να οδηγήσει", "Γιατί οι ασκήσεις γίνονται σε ζευγάρια", "Για να μάθει να αλλάζει πάνες", "Γιατί είναι υποχρεωτικό"], 1, "γιατί οι ασκήσεις γίνονται σε ζευγάρια"),
  Q("Από πού είναι η είσοδος της βιβλιοθήκης;", ["Από την πλατεία", "Από το πλάι, από την οδό Αθηνάς", "Από το πάρκινγκ", "Από το κέντρο υγείας"], 1, "η είσοδος είναι από το πλάι, από την οδό Αθηνάς"),
 ],
 "gloss": {"μαία": "μαία — midwife", "προετοιμασίας": "προετοιμασία — preparation (μάθημα προετοιμασίας = antenatal class)", "αναπνοής": "αναπνοή — breathing", "στρώμα": "στρώμα — mat, mattress", "ασανσέρ": "ασανσέρ — lift"},
})

ITEMS.append({
 "id": "l201-c1-mono-kalyteroi-apo-ton-meso-oro", "title": "Γιατί όλοι πιστεύουμε ότι είμαστε καλύτεροι από τον μέσο όρο;", "title_en": "Why do we all think we're better than average?", "type": "monologue", "level": "C1",
 "context_el": "Μια κοινωνική ψυχολόγος μιλάει σε μια σειρά διαλέξεων για την αυτογνωσία.",
 "script": [
  L("Ψυχολόγος", "f", "Σε μια γνωστή έρευνα των αρχών της δεκαετίας του 1980, η μεγάλη πλειονότητα των οδηγών που ρωτήθηκαν δήλωσε ότι οδηγεί καλύτερα και με μεγαλύτερη ασφάλεια από τον μέσο οδηγό. Μαθηματικά, βέβαια, δεν γίνεται οι περισσότεροι να είναι πάνω από τον μέσο όρο. Το φαινόμενο ονομάζεται «ψευδαίσθηση ανωτερότητας».", "In a well-known study from the early 1980s, the great majority of the drivers asked said they drove better and more safely than the average driver. Mathematically, of course, most people can't be above average. The phenomenon is called 'illusory superiority'."),
  L("Ψυχολόγος", "f", "Εμφανίζεται κυρίως σε ιδιότητες που είναι ασαφείς και που μπορούμε να τις ορίσουμε όπως μας βολεύει. Ο ένας θεωρεί καλό οδηγό αυτόν που δεν παραβιάζει ποτέ το όριο ταχύτητας, ο άλλος αυτόν που αντιδρά γρήγορα. Ο καθένας επιλέγει, χωρίς να το καταλαβαίνει, το κριτήριο στο οποίο υπερέχει ο ίδιος.", "It appears mainly in qualities that are vague and that we can define as suits us. One person considers a good driver someone who never breaks the speed limit, another someone who reacts quickly. Each of us chooses, without realising it, the criterion in which we ourselves excel."),
  L("Ψυχολόγος", "f", "Ενδιαφέρον έχει ότι σε δεξιότητες όπου κανείς μας δεν νιώθει καλός, όπως η ταχυδακτυλουργία, συμβαίνει το αντίθετο: υποτιμούμε τον εαυτό μας σε σχέση με τους άλλους. Δεν πρόκειται λοιπόν απλώς για αλαζονεία. Πρόκειται για το ότι κρίνουμε τους άλλους με βάση τον εαυτό μας, που είναι το μόνο μέτρο που γνωρίζουμε από μέσα.", "Interestingly, in skills where none of us feels good, like juggling, the opposite happens: we underestimate ourselves compared to others. So it isn't simply arrogance. It's that we judge others on the basis of ourselves, which is the only yardstick we know from the inside."),
 ],
 "questions": [
  Q("Τι δήλωσαν οι περισσότεροι οδηγοί στην έρευνα;", ["Ότι οδηγούν χειρότερα από τους άλλους", "Ότι οδηγούν καλύτερα και με μεγαλύτερη ασφάλεια από τον μέσο οδηγό", "Ότι δεν τους αρέσει η οδήγηση", "Ότι έχουν κάνει ατύχημα"], 1, "οδηγεί καλύτερα και με μεγαλύτερη ασφάλεια από τον μέσο οδηγό"),
  Q("Σε ποιες ιδιότητες εμφανίζεται κυρίως το φαινόμενο;", ["Σε ιδιότητες που μετριούνται με ακρίβεια", "Σε ασαφείς ιδιότητες που μπορούμε να ορίσουμε όπως μας βολεύει", "Μόνο στην οδήγηση", "Στις σωματικές ικανότητες"], 1, "σε ιδιότητες που είναι ασαφείς"),
  Q("Τι συμβαίνει σε δεξιότητες όπως η ταχυδακτυλουργία;", ["Υπερεκτιμούμε τον εαυτό μας", "Δεν έχουμε άποψη", "Υποτιμούμε τον εαυτό μας σε σχέση με τους άλλους", "Θαυμάζουμε τους άλλους"], 2, "υποτιμούμε τον εαυτό μας σε σχέση με τους άλλους"),
  Q("Ποια είναι η βασική εξήγηση της ομιλήτριας;", ["Η αλαζονεία", "Ότι κρίνουμε τους άλλους με βάση τον εαυτό μας", "Η έλλειψη εκπαίδευσης", "Ο ανταγωνισμός"], 1, "κρίνουμε τους άλλους με βάση τον εαυτό μας"),
 ],
 "gloss": {"πλειονότητα": "πλειονότητα — majority", "ψευδαίσθηση": "ψευδαίσθηση — illusion", "ανωτερότητας": "ανωτερότητα — superiority", "ασαφείς": "ασαφής — vague", "υπερέχει": "υπερέχω — to excel, be superior", "αλαζονεία": "αλαζονεία — arrogance"},
})

ITEMS.append({
 "id": "l201-c1-int-plani-tou-paikti", "title": "Η πλάνη του παίκτη", "title_en": "The gambler's fallacy", "type": "interview", "level": "C1",
 "context_el": "Συνέντευξη με έναν μαθηματικό σε μια εκπομπή για τις πιθανότητες στην καθημερινή ζωή.",
 "script": [
  L("Δημοσιογράφος", "f", "Η ρουλέτα έχει φέρει πέντε φορές στη σειρά μαύρο. Πολλοί θα ποντάρουν τώρα στο κόκκινο. Έχουν δίκιο;", "The roulette wheel has come up black five times in a row. Many would now bet on red. Are they right?"),
  L("Μαθηματικός", "m", "Όχι. Η ρουλέτα δεν έχει μνήμη. Σε κάθε γύρισμα η πιθανότητα για κόκκινο είναι ακριβώς η ίδια με πριν, ό,τι κι αν προηγήθηκε. Η πεποίθηση ότι μετά από μια σειρά μαύρων «έρχεται η σειρά» του κόκκινου λέγεται «πλάνη του παίκτη». Το πιο διάσημο παράδειγμα συνέβη σε ένα καζίνο του Μόντε Κάρλο το 1913, όταν η μπίλια έπεσε στο μαύρο είκοσι έξι φορές στη σειρά, και οι παίκτες έχασαν μια περιουσία ποντάροντας στο κόκκινο.", "No. The wheel has no memory. On each spin the probability of red is exactly the same as before, whatever came first. The belief that after a run of blacks red is 'due' is called the 'gambler's fallacy'. The most famous example happened at a casino in Monte Carlo in 1913, when the ball landed on black twenty-six times in a row, and players lost a fortune betting on red."),
  L("Δημοσιογράφος", "f", "Γιατί μας ξεγελάει τόσο εύκολα;", "Why does it fool us so easily?"),
  L("Μαθηματικός", "m", "Γιατί έχουμε μια διαίσθηση για το πώς «μοιάζει» η τύχη. Περιμένουμε ότι ακόμα και μια μικρή σειρά αποτελεσμάτων θα είναι ισορροπημένη, μισά κόκκινα και μισά μαύρα. Αυτό ισχύει μόνο για πάρα πολλά γυρίσματα. Σε μικρές σειρές, οι επαναλήψεις είναι πολύ πιο συχνές απ' ό,τι φανταζόμαστε.", "Because we have an intuition about what chance 'looks like'. We expect even a short series of results to be balanced, half red and half black. That holds only for a great many spins. In short series, repetitions are much more frequent than we imagine."),
  L("Δημοσιογράφος", "f", "Υπάρχει και το αντίθετο λάθος;", "Is there also the opposite mistake?"),
  L("Μαθηματικός", "m", "Ναι, και είναι εξίσου ανθρώπινο: το λεγόμενο «ζεστό χέρι», η πεποίθηση ότι κάποιος που πέτυχε τρία καλάθια στη σειρά θα πετύχει σίγουρα και το τέταρτο. Εκεί η συζήτηση είναι πιο περίπλοκη, γιατί ένας αθλητής, σε αντίθεση με τη ρουλέτα, μπορεί πράγματι να έχει μια καλή μέρα.", "Yes, and it's just as human: the so-called 'hot hand', the belief that someone who has scored three baskets in a row will surely score the fourth. There the debate is more complicated, because an athlete, unlike a roulette wheel, really can have a good day."),
 ],
 "questions": [
  Q("Γιατί δεν έχουν δίκιο όσοι ποντάρουν στο κόκκινο μετά από πέντε μαύρα;", ["Γιατί η ρουλέτα είναι στημένη", "Γιατί σε κάθε γύρισμα η πιθανότητα μένει ίδια", "Γιατί το μαύρο είναι πιο πιθανό", "Γιατί το καζίνο κερδίζει πάντα"], 1, "Σε κάθε γύρισμα η πιθανότητα για κόκκινο είναι ακριβώς η ίδια με πριν"),
  Q("Τι συνέβη στο Μόντε Κάρλο το 1913;", ["Ένας παίκτης κέρδισε μια περιουσία", "Η μπίλια έπεσε στο μαύρο είκοσι έξι φορές στη σειρά", "Το καζίνο έκλεισε", "Απαγορεύτηκε η ρουλέτα"], 1, "η μπίλια έπεσε στο μαύρο είκοσι έξι φορές στη σειρά"),
  Q("Ποια λανθασμένη διαίσθηση έχουμε για την τύχη;", ["Ότι ακόμα και μικρές σειρές θα είναι ισορροπημένες", "Ότι οι αριθμοί έχουν χρώματα", "Ότι η τύχη δεν υπάρχει", "Ότι οι μεγάλες σειρές είναι άνισες"], 0, "Περιμένουμε ότι ακόμα και μια μικρή σειρά αποτελεσμάτων θα είναι ισορροπημένη"),
  Q("Γιατί η συζήτηση για το «ζεστό χέρι» είναι πιο περίπλοκη;", ["Γιατί αφορά μόνο το μπάσκετ", "Γιατί ένας αθλητής μπορεί πράγματι να έχει μια καλή μέρα", "Γιατί δεν υπάρχουν δεδομένα", "Γιατί οι αθλητές δεν ποντάρουν"], 1, "ένας αθλητής, σε αντίθεση με τη ρουλέτα, μπορεί πράγματι να έχει μια καλή μέρα"),
 ],
 "gloss": {"ποντάρουν": "ποντάρω — to bet", "πεποίθηση": "πεποίθηση — belief", "μπίλια": "μπίλια — ball (in roulette), marble", "περιουσία": "περιουσία — fortune", "διαίσθηση": "διαίσθηση — intuition", "ισορροπημένη": "ισορροπημένος — balanced"},
})

rnd = random.Random(201)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-201.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
