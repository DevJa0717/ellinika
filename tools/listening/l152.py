# Source for library/listening/listening-152.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l152.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l152-vm-vivlio-kratisi", "title": "Το βιβλίο που ζητήσατε έφτασε", "title_en": "The book you reserved has arrived", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη δημοτική βιβλιοθήκη.",
 "script": [
  L("Βιβλιοθηκονόμος", "f", "Καλησπέρα σας, από τη Δημοτική Βιβλιοθήκη. Σας ενημερώνω ότι το μυθιστόρημα που είχατε κρατήσει επιστράφηκε σήμερα και σας περιμένει στον πάγκο του δανεισμού.", "Good evening, this is the Municipal Library. I'm letting you know that the novel you had reserved was returned today and is waiting for you at the loans desk."),
  L("Βιβλιοθηκονόμος", "f", "Θα σας το κρατήσουμε για μία εβδομάδα, δηλαδή μέχρι την επόμενη Τρίτη. Μετά θα περάσει στον επόμενο αναγνώστη της λίστας, γιατί υπάρχουν άλλοι τέσσερις που το περιμένουν.", "We'll hold it for you for one week, that is until next Tuesday. After that it will go to the next reader on the list, because four others are waiting for it."),
  L("Βιβλιοθηκονόμος", "f", "Επειδή υπάρχει μεγάλη ζήτηση, ο δανεισμός γι' αυτό το βιβλίο είναι δεκαπέντε μέρες και όχι ένας μήνας, και δεν μπορεί να ανανεωθεί. Μην ξεχάσετε να φέρετε την κάρτα μέλους σας.", "Because there is high demand, the loan for this book is fifteen days and not a month, and it can't be renewed. Don't forget to bring your membership card."),
 ],
 "questions": [
  Q("Πού σας περιμένει το βιβλίο;", ["Στο αναγνωστήριο", "Στον πάγκο του δανεισμού", "Στο γραμματοκιβώτιό σας", "Στο βιβλιοπωλείο"], 1, "σας περιμένει στον πάγκο του δανεισμού"),
  Q("Μέχρι πότε θα σας το κρατήσουν;", ["Μέχρι αύριο", "Για έναν μήνα", "Μέχρι την επόμενη Τρίτη", "Μέχρι το Σάββατο"], 2, "μέχρι την επόμενη Τρίτη"),
  Q("Τι ισχύει για τον δανεισμό αυτού του βιβλίου;", ["Είναι δεκαπέντε μέρες και δεν ανανεώνεται", "Είναι ένας μήνας", "Μπορεί να ανανεωθεί δύο φορές", "Το βιβλίο διαβάζεται μόνο μέσα στη βιβλιοθήκη"], 0, "ο δανεισμός γι' αυτό το βιβλίο είναι δεκαπέντε μέρες"),
 ],
 "gloss": {"μυθιστόρημα": "μυθιστόρημα — novel", "κρατήσει": "κρατάω — to reserve, hold", "επιστράφηκε": "επιστρέφομαι — to be returned", "πάγκο": "πάγκος — desk, counter", "δανεισμού": "δανεισμός — loan, lending", "αναγνώστη": "αναγνώστης — reader", "ζήτηση": "ζήτηση — demand", "ανανεωθεί": "ανανεώνομαι — to be renewed", "κάρτα μέλους": "κάρτα μέλους — membership card"}
})

ITEMS.append({
 "id": "l152-ann-tainiothiki", "title": "Πριν από την προβολή στην Ταινιοθήκη", "title_en": "Before the screening at the film archive", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση σε μια αίθουσα κινηματογράφου λίγο πριν από την προβολή.",
 "script": [
  L("Υπεύθυνη", "f", "Καλησπέρα και καλώς ήρθατε στο αφιέρωμα στον ελληνικό κινηματογράφο της δεκαετίας του εξήντα. Η αποψινή ταινία προβάλλεται από αποκατεστημένη κόπια, με αγγλικούς υπότιτλους.", "Good evening and welcome to the tribute to Greek cinema of the sixties. Tonight's film is being screened from a restored print, with English subtitles."),
  L("Υπεύθυνη", "f", "Σας παρακαλούμε να απενεργοποιήσετε τα κινητά σας τηλέφωνα και να μη βγάζετε φωτογραφίες κατά τη διάρκεια της προβολής. Η ταινία διαρκεί περίπου εκατό λεπτά, χωρίς διάλειμμα.", "Please switch off your mobile phones and don't take photos during the screening. The film lasts about a hundred minutes, with no interval."),
  L("Υπεύθυνη", "f", "Μετά το τέλος θα ακολουθήσει συζήτηση με τη σκηνοθέτρια που επιμελήθηκε την αποκατάσταση. Όσοι θέλετε να μείνετε, παρακαλούμε να μην αφήσετε τις θέσεις σας, γιατί η συζήτηση θα ξεκινήσει αμέσως.", "After the end there will be a discussion with the director who supervised the restoration. Those of you who want to stay, please don't leave your seats, because the discussion will start straight away."),
 ],
 "questions": [
  Q("Τι ισχύει για την αποψινή ταινία;", ["Είναι καινούργια ταινία", "Προβάλλεται από αποκατεστημένη κόπια με αγγλικούς υπότιτλους", "Είναι μεταγλωττισμένη", "Είναι βουβή"], 1, "προβάλλεται από αποκατεστημένη κόπια, με αγγλικούς υπότιτλους"),
  Q("Πόσο διαρκεί η ταινία;", ["Περίπου εκατό λεπτά χωρίς διάλειμμα", "Δύο ώρες με διάλειμμα", "Εξήντα λεπτά", "Τρεις ώρες"], 0, "περίπου εκατό λεπτά, χωρίς διάλειμμα"),
  Q("Τι θα γίνει μετά την ταινία;", ["Θα προβληθεί δεύτερη ταινία", "Θα σερβιριστεί κρασί", "Θα ακολουθήσει συζήτηση με τη σκηνοθέτρια της αποκατάστασης", "Θα κλείσει αμέσως η αίθουσα"], 2, "θα ακολουθήσει συζήτηση με τη σκηνοθέτρια που επιμελήθηκε την αποκατάσταση"),
 ],
 "gloss": {"αφιέρωμα": "αφιέρωμα — tribute, retrospective", "δεκαετίας": "δεκαετία — decade", "προβάλλεται": "προβάλλομαι — to be screened", "αποκατεστημένη": "αποκατεστημένος — restored", "κόπια": "κόπια — (film) print, copy", "υπότιτλους": "υπότιτλος — subtitle", "απενεργοποιήσετε": "απενεργοποιώ — to switch off", "διάλειμμα": "διάλειμμα — interval", "επιμελήθηκε": "επιμελούμαι — to supervise, edit"}
})

ITEMS.append({
 "id": "l152-dia-fotografies-diavatiriou", "title": "Φωτογραφίες για το διαβατήριο", "title_en": "Passport photos", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν πελάτη και μια φωτογράφο σε ένα φωτογραφείο.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Θέλω φωτογραφίες για διαβατήριο. Μπορείτε να μου τις βγάλετε τώρα;", "Good morning. I want photos for a passport. Can you take them now?"),
  L("Φωτογράφος", "f", "Βεβαίως. Αλλά θα πρέπει να βγάλετε τα γυαλιά σας, δεν επιτρέπονται στις φωτογραφίες διαβατηρίου. Και μη χαμογελάτε, το στόμα πρέπει να είναι κλειστό.", "Of course. But you'll need to take off your glasses, they're not allowed in passport photos. And don't smile, your mouth must be closed."),
  L("Πελάτης", "m", "Ούτε ένα μικρό χαμόγελο; Θα φαίνομαι σαν να με έχουν συλλάβει!", "Not even a little smile? I'll look as if I've been arrested!"),
  L("Φωτογράφος", "f", "Όλοι έτσι φαίνονται, μην ανησυχείτε. Καθίστε εδώ, μπροστά στο λευκό φόντο, και κοιτάξτε κατευθείαν τον φακό. Τα μαλλιά να μην κρύβουν το πρόσωπο.", "Everyone looks like that, don't worry. Sit here, in front of the white background, and look straight into the lens. Your hair mustn't hide your face."),
  L("Πελάτης", "m", "Εντάξει. Πόσο κάνουν και πότε θα είναι έτοιμες;", "OK. How much are they and when will they be ready?"),
  L("Φωτογράφος", "f", "Δώδεκα ευρώ οι τέσσερις, και θα είναι έτοιμες σε δέκα λεπτά. Σας στέλνω και τον ψηφιακό κωδικό με μήνυμα, γιατί για την αίτηση στο διαδίκτυο χρειάζεται κι αυτός.", "Twelve euros for four, and they'll be ready in ten minutes. I'll also send you the digital code by text, because you need that too for the online application."),
 ],
 "questions": [
  Q("Τι πρέπει να κάνει ο πελάτης πριν από τη φωτογραφία;", ["Να χτενιστεί", "Να βγάλει τα γυαλιά του", "Να φορέσει γραβάτα", "Να βγάλει το καπέλο του"], 1, "θα πρέπει να βγάλετε τα γυαλιά σας"),
  Q("Γιατί διαμαρτύρεται ο πελάτης;", ["Γιατί δεν μπορεί να χαμογελάσει", "Γιατί η τιμή είναι υψηλή", "Γιατί πρέπει να περιμένει πολύ", "Γιατί δεν του αρέσει το φόντο"], 0, "Ούτε ένα μικρό χαμόγελο;"),
  Q("Τι θα του στείλει η φωτογράφος με μήνυμα;", ["Την απόδειξη", "Τις φωτογραφίες", "Έναν ψηφιακό κωδικό για την αίτηση", "Την ώρα που θα είναι έτοιμες"], 2, "Σας στέλνω και τον ψηφιακό κωδικό με μήνυμα"),
 ],
 "gloss": {"διαβατήριο": "διαβατήριο — passport", "επιτρέπονται": "επιτρέπομαι — to be allowed", "χαμόγελο": "χαμόγελο — smile", "συλλάβει": "συλλαμβάνω — to arrest", "φόντο": "φόντο — background", "φακό": "φακός — lens", "ψηφιακό": "ψηφιακός — digital", "κωδικό": "κωδικός — code", "αίτηση": "αίτηση — application"}
})

ITEMS.append({
 "id": "l152-int-tilergasia-chorio", "title": "Δουλεύοντας από ένα ορεινό χωριό", "title_en": "Working from a mountain village", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε μια ραδιοφωνική εκπομπή για την περιφέρεια.",
 "script": [
  L("Δημοσιογράφος", "m", "Η Ιωάννα είναι γραφίστρια και πριν από τρία χρόνια άφησε τη Θεσσαλονίκη για ένα χωριό των Γρεβενών. Ιωάννα, πώς πήρες αυτή την απόφαση;", "Ioanna is a graphic designer, and three years ago she left Thessaloniki for a village in Grevena. Ioanna, how did you make that decision?"),
  L("Ιωάννα", "f", "Στην πανδημία κατάλαβα ότι μπορώ να κάνω τη δουλειά μου από οπουδήποτε, αρκεί να έχω καλό ίντερνετ. Το σπίτι της γιαγιάς μου ήταν άδειο, οπότε το επισκεύασα και μετακόμισα.", "During the pandemic I realised I can do my job from anywhere, as long as I have good internet. My grandmother's house was empty, so I repaired it and moved."),
  L("Δημοσιογράφος", "m", "Και δεν νιώθεις μοναξιά;", "And don't you feel lonely?"),
  L("Ιωάννα", "f", "Τον πρώτο χειμώνα, ναι. Μετά όμως ήρθαν άλλοι δύο νέοι που δουλεύουν κι αυτοί εξ αποστάσεως, και ζητήσαμε από την κοινότητα το παλιό σχολείο, που ήταν κλειστό. Τώρα είναι ο κοινός μας χώρος εργασίας.", "The first winter, yes. But then two other young people came who also work remotely, and we asked the community for the old school, which was closed. Now it's our shared workspace."),
  L("Ιωάννα", "f", "Το μόνο πραγματικό πρόβλημα είναι ο δρόμος τον χειμώνα. Όταν χιονίζει πολύ, μπορεί να μείνουμε αποκλεισμένοι για δυο μέρες. Γι' αυτό έχω πάντα γεμάτη αποθήκη και μια γεννήτρια.", "The only real problem is the road in winter. When it snows a lot, we can be cut off for a couple of days. That's why I always keep a full larder and a generator."),
 ],
 "questions": [
  Q("Τι κατάλαβε η Ιωάννα στην πανδημία;", ["Ότι ήθελε να αλλάξει επάγγελμα", "Ότι μπορεί να δουλεύει από οπουδήποτε με καλό ίντερνετ", "Ότι της έλειπε η γιαγιά της", "Ότι η πόλη ήταν ακριβή"], 1, "μπορώ να κάνω τη δουλειά μου από οπουδήποτε, αρκεί να έχω καλό ίντερνετ"),
  Q("Τι έγινε το παλιό σχολείο του χωριού;", ["Ξενώνας", "Μουσείο", "Κοινός χώρος εργασίας", "Καφενείο"], 2, "Τώρα είναι ο κοινός μας χώρος εργασίας"),
  Q("Ποιο είναι το μόνο πραγματικό πρόβλημα, σύμφωνα με την Ιωάννα;", ["Ο δρόμος τον χειμώνα, όταν χιονίζει πολύ", "Το ίντερνετ", "Οι γείτονες", "Η έλλειψη δουλειάς"], 0, "Το μόνο πραγματικό πρόβλημα είναι ο δρόμος τον χειμώνα"),
 ],
 "gloss": {"γραφίστρια": "γραφίστρια — graphic designer", "πανδημία": "πανδημία — pandemic", "οπουδήποτε": "οπουδήποτε — anywhere", "επισκεύασα": "επισκευάζω — to repair", "μοναξιά": "μοναξιά — loneliness", "εξ αποστάσεως": "εξ αποστάσεως — remotely", "κοινότητα": "κοινότητα — village council, community", "αποκλεισμένοι": "αποκλεισμένος — cut off", "γεννήτρια": "γεννήτρια — generator"}
})

ITEMS.append({
 "id": "l152-news-gefyra-kleinei", "title": "Κλειστή για έναν μήνα η γέφυρα του λιμανιού", "title_en": "The harbour bridge closed for a month", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα δελτίο ειδήσεων από τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνητής", "m", "Από τη Δευτέρα η γέφυρα που ενώνει το λιμάνι με το κέντρο της πόλης θα κλείσει για έναν μήνα, για εργασίες ενίσχυσης. Οι μηχανικοί του δήμου εντόπισαν διάβρωση στις μεταλλικές δοκούς.", "From Monday the bridge connecting the harbour to the town centre will close for a month for strengthening works. The municipality's engineers found corrosion in the metal beams."),
  L("Εκφωνητής", "m", "Τα αυτοκίνητα θα κυκλοφορούν από την παραλιακή λεωφόρο, όπου αναμένεται αυξημένη κίνηση τις ώρες αιχμής. Η τροχαία συνιστά στους οδηγούς να υπολογίζουν τουλάχιστον είκοσι λεπτά επιπλέον.", "Cars will be routed along the coastal avenue, where heavier traffic is expected at rush hour. The traffic police advise drivers to allow at least twenty extra minutes."),
  L("Εκφωνητής", "m", "Για τους πεζούς και τους ποδηλάτες ο δήμος θα λειτουργεί δωρεάν πλωτό λεωφορείο από τις έξι το πρωί ως τα μεσάνυχτα, κάθε δεκαπέντε λεπτά. Τα ποδήλατα θα μεταφέρονται χωρίς χρέωση.", "For pedestrians and cyclists the municipality will run a free water bus from six in the morning until midnight, every fifteen minutes. Bicycles will be carried free of charge."),
 ],
 "questions": [
  Q("Γιατί κλείνει η γέφυρα;", ["Για να βαφτεί", "Για εργασίες ενίσχυσης, λόγω διάβρωσης", "Για μια γιορτή", "Γιατί χτυπήθηκε από πλοίο"], 1, "για εργασίες ενίσχυσης"),
  Q("Τι συνιστά η τροχαία στους οδηγούς;", ["Να μην κυκλοφορούν τη νύχτα", "Να αφήνουν το αυτοκίνητο στο λιμάνι", "Να υπολογίζουν τουλάχιστον είκοσι λεπτά επιπλέον", "Να χρησιμοποιούν το πλωτό λεωφορείο"], 2, "να υπολογίζουν τουλάχιστον είκοσι λεπτά επιπλέον"),
  Q("Τι ισχύει για το πλωτό λεωφορείο;", ["Είναι δωρεάν και μεταφέρει και ποδήλατα χωρίς χρέωση", "Κοστίζει ένα ευρώ", "Λειτουργεί μόνο τις ώρες αιχμής", "Δεν δέχεται ποδήλατα"], 0, "δωρεάν πλωτό λεωφορείο"),
 ],
 "gloss": {"γέφυρα": "γέφυρα — bridge", "ενίσχυσης": "ενίσχυση — strengthening", "εντόπισαν": "εντοπίζω — to detect", "διάβρωση": "διάβρωση — corrosion", "δοκούς": "δοκός — beam (fem.)", "αιχμής": "ώρα αιχμής — rush hour", "τροχαία": "τροχαία — traffic police", "πλωτό": "πλωτός — floating; πλωτό λεωφορείο = water bus", "χρέωση": "χρέωση — charge"}
})

ITEMS.append({
 "id": "l152-mono-imerologio", "title": "Τριάντα χρόνια ημερολόγιο", "title_en": "Thirty years of keeping a diary", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλάει σε μια εκπομπή για τις καθημερινές συνήθειες.",
 "script": [
  L("Ελένη", "f", "Κρατάω ημερολόγιο από τα δεκατέσσερά μου. Το πρώτο μού το χάρισε μια θεία, ένα μικρό τετράδιο με κλειδαριά, και από τότε δεν σταμάτησα. Έχω πια σαράντα τετράδια σε ένα κουτί κάτω από το κρεβάτι.", "I've kept a diary since I was fourteen. An aunt gave me the first one, a little notebook with a lock, and I haven't stopped since. I now have forty notebooks in a box under the bed."),
  L("Ελένη", "f", "Δεν γράφω κάθε μέρα. Γράφω όταν κάτι με απασχολεί ή όταν δεν μπορώ να κοιμηθώ. Συχνά, μόλις γράψω ένα πρόβλημα στο χαρτί, μου φαίνεται μικρότερο.", "I don't write every day. I write when something is on my mind or when I can't sleep. Often, as soon as I write a problem down on paper, it seems smaller."),
  L("Ελένη", "f", "Το πιο παράξενο είναι να ξαναδιαβάζω τα παλιά. Βρίσκω καβγάδες που τότε μου φαίνονταν τραγικοί και τώρα δεν θυμάμαι καν γιατί έγιναν. Αυτό με έχει κάνει πιο ήρεμη με τα σημερινά μου προβλήματα.", "The strangest thing is rereading the old ones. I find quarrels that seemed tragic to me back then, and now I don't even remember why they happened. That has made me calmer about my problems today."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε η Ελένη να κρατάει ημερολόγιο;", ["Της το ζήτησε μια δασκάλα", "Μια θεία τής χάρισε ένα τετράδιο με κλειδαριά", "Το διάβασε σε ένα βιβλίο", "Το ξεκίνησε σε ένα ταξίδι"], 1, "Το πρώτο μού το χάρισε μια θεία, ένα μικρό τετράδιο με κλειδαριά"),
  Q("Πότε γράφει;", ["Κάθε βράδυ", "Μόνο στις διακοπές", "Όταν κάτι την απασχολεί ή όταν δεν μπορεί να κοιμηθεί", "Κάθε Κυριακή πρωί"], 2, "Γράφω όταν κάτι με απασχολεί ή όταν δεν μπορώ να κοιμηθώ"),
  Q("Πώς την έχει επηρεάσει το ξαναδιάβασμα των παλιών τετραδίων;", ["Την έχει κάνει πιο ήρεμη με τα σημερινά της προβλήματα", "Τη στενοχωρεί", "Την έκανε να σταματήσει να γράφει", "Τη βοήθησε να γράψει ένα βιβλίο"], 0, "Αυτό με έχει κάνει πιο ήρεμη με τα σημερινά μου προβλήματα"),
 ],
 "gloss": {"ημερολόγιο": "ημερολόγιο — diary", "χάρισε": "χαρίζω — to give (as a gift)", "κλειδαριά": "κλειδαριά — lock", "τετράδια": "τετράδιο — notebook", "απασχολεί": "με απασχολεί κάτι — something is on my mind", "ξαναδιαβάζω": "ξαναδιαβάζω — to reread", "καβγάδες": "καβγάς — quarrel", "τραγικοί": "τραγικός — tragic"}
})

ITEMS.append({
 "id": "l152-rep-antallagi-spition", "title": "Διακοπές με ανταλλαγή σπιτιών", "title_en": "Holidays by swapping homes", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια ταξιδιωτική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "f", "Η οικογένεια Μαυρίδη από τα Χανιά πέρασε τον περσινό Αύγουστο σε ένα σπίτι στη Λυών. Την ίδια ώρα, μια γαλλική οικογένεια έμενε στο δικό τους διαμέρισμα. Κανείς δεν πλήρωσε ενοίκιο.", "The Mavridis family from Chania spent last August in a house in Lyon. At the same time, a French family was staying in their flat. Nobody paid rent."),
  L("Ρεπόρτερ", "f", "Η ανταλλαγή σπιτιών γίνεται συνήθως μέσα από ειδικές πλατφόρμες, όπου τα μέλη πληρώνουν μια ετήσια συνδρομή. Πριν συμφωνήσουν, οι οικογένειες μιλούν με βιντεοκλήσεις και ανταλλάσσουν φωτογραφίες και κανόνες.", "Home swapping usually happens through special platforms, where members pay an annual subscription. Before agreeing, the families talk by video call and exchange photos and rules."),
  L("Ρεπόρτερ", "f", "«Στην αρχή φοβόμουν να αφήσω ξένους στο σπίτι μου», λέει η κυρία Μαυρίδη. «Όταν γυρίσαμε όμως, βρήκαμε το σπίτι πιο καθαρό απ' ό,τι το αφήσαμε, και ένα γράμμα με συνταγές από τη Λυών.» Φέτος σχεδιάζουν ανταλλαγή με μια οικογένεια από τη Νορβηγία.", "\"At first I was afraid to leave strangers in my home,\" says Mrs Mavridi. \"But when we came back, we found the house cleaner than we left it, and a letter with recipes from Lyon.\" This year they're planning a swap with a family from Norway."),
 ],
 "questions": [
  Q("Τι πλήρωσαν οι δύο οικογένειες για το σπίτι;", ["Το μισό ενοίκιο", "Τίποτα, κανείς δεν πλήρωσε ενοίκιο", "Μόνο το ρεύμα", "Ένα ενοίκιο για μία εβδομάδα"], 1, "Κανείς δεν πλήρωσε ενοίκιο"),
  Q("Τι κάνουν οι οικογένειες πριν συμφωνήσουν;", ["Συναντιούνται από κοντά", "Υπογράφουν συμβόλαιο σε συμβολαιογράφο", "Μιλούν με βιντεοκλήσεις και ανταλλάσσουν φωτογραφίες και κανόνες", "Πληρώνουν μια εγγύηση"], 2, "οι οικογένειες μιλούν με βιντεοκλήσεις και ανταλλάσσουν φωτογραφίες και κανόνες"),
  Q("Τι βρήκε η οικογένεια Μαυρίδη όταν γύρισε;", ["Το σπίτι πιο καθαρό και ένα γράμμα με συνταγές", "Ένα σπασμένο παράθυρο", "Ένα δώρο από τη Νορβηγία", "Το σπίτι ακατάστατο"], 0, "βρήκαμε το σπίτι πιο καθαρό απ' ό,τι το αφήσαμε, και ένα γράμμα με συνταγές"),
 ],
 "gloss": {"διαμέρισμα": "διαμέρισμα — flat, apartment", "ενοίκιο": "ενοίκιο — rent", "ανταλλαγή": "ανταλλαγή — exchange, swap", "πλατφόρμες": "πλατφόρμα — platform", "συνδρομή": "συνδρομή — subscription", "βιντεοκλήσεις": "βιντεοκλήση — video call", "ανταλλάσσουν": "ανταλλάσσω — to exchange", "συνταγές": "συνταγή — recipe"}
})

ITEMS.append({
 "id": "l152-dia-daneismos-aftokinitou", "title": "Μου δανείζεις το αυτοκίνητο;", "title_en": "Will you lend me the car?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλους να μιλούν στο τηλέφωνο.",
 "script": [
  L("Άρης", "m", "Γιώργο, μια μεγάλη χάρη. Μπορείς να μου δανείσεις το αυτοκίνητο το Σαββατοκύριακο; Πρέπει να μεταφέρω κάτι έπιπλα στο εξοχικό της μάνας μου.", "Giorgos, a big favour. Can you lend me the car at the weekend? I need to move some furniture to my mother's country house."),
  L("Γιώργος", "m", "Ευχαρίστως, αλλά πρώτα πρέπει να δω αν η ασφάλεια καλύπτει κι άλλον οδηγό. Θα πάρω την ασφαλιστική αύριο το πρωί.", "Gladly, but first I need to check whether the insurance covers another driver. I'll call the insurance company tomorrow morning."),
  L("Άρης", "m", "Σωστά, δεν το είχα σκεφτεί. Και φυσικά θα σου το φέρω με γεμάτο ρεζερβουάρ.", "Right, I hadn't thought of that. And of course I'll bring it back with a full tank."),
  L("Γιώργος", "m", "Δεν χρειάζεται γεμάτο, όσο ήταν. Μόνο πρόσεξε το πίσω δεξί λάστιχο, χάνει λίγο αέρα. Φούσκωσέ το σε ένα βενζινάδικο πριν φύγεις.", "It doesn't need to be full, just as it was. Only watch the back right tyre, it loses a bit of air. Pump it up at a petrol station before you leave."),
  L("Άρης", "m", "Θα το κάνω. Και για να σε ευχαριστήσω, την άλλη εβδομάδα σε κερνάω φαγητό.", "I will. And to thank you, I'm buying you dinner next week."),
 ],
 "questions": [
  Q("Γιατί χρειάζεται ο Άρης το αυτοκίνητο;", ["Για να πάει διακοπές", "Για να μεταφέρει έπιπλα στο εξοχικό της μητέρας του", "Για να πάει στο αεροδρόμιο", "Γιατί το δικό του χάλασε"], 1, "Πρέπει να μεταφέρω κάτι έπιπλα στο εξοχικό της μάνας μου"),
  Q("Τι πρέπει να ελέγξει πρώτα ο Γιώργος;", ["Αν έχει βενζίνη", "Αν η ασφάλεια καλύπτει κι άλλον οδηγό", "Αν είναι ελεύθερος το Σαββατοκύριακο", "Αν έχει γίνει σέρβις"], 1, "να δω αν η ασφάλεια καλύπτει κι άλλον οδηγό"),
  Q("Τι πρέπει να προσέξει ο Άρης;", ["Τα φρένα", "Το ραδιόφωνο", "Το πίσω δεξί λάστιχο, που χάνει αέρα", "Τα φώτα"], 2, "πρόσεξε το πίσω δεξί λάστιχο, χάνει λίγο αέρα"),
 ],
 "gloss": {"χάρη": "χάρη — favour", "δανείσεις": "δανείζω — to lend", "έπιπλα": "έπιπλο — piece of furniture", "εξοχικό": "εξοχικό — country house", "ασφάλεια": "ασφάλεια — insurance", "ασφαλιστική": "ασφαλιστική (εταιρεία) — insurance company", "ρεζερβουάρ": "ρεζερβουάρ — fuel tank", "λάστιχο": "λάστιχο — tyre", "Φούσκωσέ": "φουσκώνω — to inflate", "κερνάω": "κερνάω — to treat (someone)"}
})

ITEMS.append({
 "id": "l152-c1-easterlin", "title": "Κάνουν τα χρήματα τις χώρες πιο ευτυχισμένες;", "title_en": "Does money make countries happier?", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από συνέντευξη μιας οικονομολόγου σε μια εκπομπή λόγου.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι είναι αυτό που οι οικονομολόγοι αποκαλούν «παράδοξο του Ίστερλιν»;", "What is it that economists call the \"Easterlin paradox\"?"),
  L("Οικονομολόγος", "f", "Το 1974 ο Αμερικανός οικονομολόγος Ρίτσαρντ Ίστερλιν παρατήρησε κάτι περίεργο. Μέσα σε μια χώρα, σε μια δεδομένη στιγμή, οι πλουσιότεροι δηλώνουν κατά μέσο όρο πιο ευτυχισμένοι από τους φτωχότερους. Όταν όμως ολόκληρη η χώρα γίνεται πλουσιότερη με τα χρόνια, ο μέσος όρος της ευτυχίας σχεδόν δεν αλλάζει.", "In 1974 the American economist Richard Easterlin noticed something odd. Within a country, at a given moment, richer people report on average being happier than poorer people. But when the whole country grows richer over the years, average happiness hardly changes."),
  L("Οικονομολόγος", "f", "Μια εξήγηση είναι ότι δεν μας ενδιαφέρει τόσο τι έχουμε, όσο τι έχουμε σε σύγκριση με τους άλλους. Αν όλοι γίνουν πλουσιότεροι μαζί, η θέση μας στη σύγκριση μένει ίδια. Μια δεύτερη εξήγηση είναι η προσαρμογή: συνηθίζουμε γρήγορα το καινούργιο αυτοκίνητο ή τον μεγαλύτερο μισθό.", "One explanation is that we care less about what we have than about what we have compared with others. If everyone gets richer together, our place in the comparison stays the same. A second explanation is adaptation: we quickly get used to the new car or the bigger salary."),
  L("Οικονομολόγος", "f", "Πρέπει πάντως να πω ότι το παράδοξο αμφισβητείται. Μεταγενέστερες μελέτες, με περισσότερες χώρες και μεγαλύτερες χρονοσειρές, βρήκαν ότι η ευτυχία αυξάνεται με το εισόδημα, αν και όλο και πιο αργά. Η συζήτηση, όπως συμβαίνει συχνά στην επιστήμη, δεν έχει κλείσει.", "I must say, though, that the paradox is disputed. Later studies, with more countries and longer time series, found that happiness does rise with income, though more and more slowly. The debate, as often happens in science, isn't closed."),
 ],
 "questions": [
  Q("Τι ισχύει μέσα σε μια χώρα, σε μια δεδομένη στιγμή;", ["Οι φτωχότεροι είναι πιο ευτυχισμένοι", "Οι πλουσιότεροι δηλώνουν κατά μέσο όρο πιο ευτυχισμένοι", "Δεν υπάρχει καμία διαφορά", "Η ευτυχία εξαρτάται μόνο από την ηλικία"], 1, "οι πλουσιότεροι δηλώνουν κατά μέσο όρο πιο ευτυχισμένοι από τους φτωχότερους"),
  Q("Τι παρατήρησε ο Ίστερλιν για τις χώρες που γίνονται πλουσιότερες με τα χρόνια;", ["Η ευτυχία διπλασιάζεται", "Η ευτυχία μειώνεται", "Ο μέσος όρος της ευτυχίας σχεδόν δεν αλλάζει", "Οι πλούσιοι γίνονται δυστυχισμένοι"], 2, "ο μέσος όρος της ευτυχίας σχεδόν δεν αλλάζει"),
  Q("Ποια είναι η δεύτερη εξήγηση που δίνει η οικονομολόγος;", ["Η προσαρμογή: συνηθίζουμε γρήγορα όσα αποκτούμε", "Οι φόροι αυξάνονται", "Οι άνθρωποι δουλεύουν περισσότερο", "Οι έρευνες είναι λανθασμένες"], 0, "Μια δεύτερη εξήγηση είναι η προσαρμογή"),
  Q("Τι βρήκαν οι μεταγενέστερες μελέτες;", ["Ότι το παράδοξο ισχύει παντού", "Ότι τα χρήματα δεν παίζουν κανέναν ρόλο", "Ότι η ευτυχία μειώνεται με το εισόδημα", "Ότι η ευτυχία αυξάνεται με το εισόδημα, αλλά όλο και πιο αργά"], 3, "η ευτυχία αυξάνεται με το εισόδημα, αν και όλο και πιο αργά"),
 ],
 "gloss": {"αποκαλούν": "αποκαλώ — to call, term", "παράδοξο": "παράδοξο — paradox", "δεδομένη": "δεδομένος — given", "μέσο όρο": "μέσος όρος — average", "σύγκριση": "σύγκριση — comparison", "προσαρμογή": "προσαρμογή — adaptation", "αμφισβητείται": "αμφισβητούμαι — to be disputed", "Μεταγενέστερες": "μεταγενέστερος — later, subsequent", "χρονοσειρές": "χρονοσειρά — time series", "εισόδημα": "εισόδημα — income"}
})

ITEMS.append({
 "id": "l152-c1-kuleshov", "title": "Ένα πρόσωπο, τρία συναισθήματα", "title_en": "One face, three emotions", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη για την ιστορία του μοντάζ στον κινηματογράφο.",
 "script": [
  L("Ομιλήτρια", "f", "Γύρω στο 1920, ο Σοβιετικός σκηνοθέτης Λεβ Κουλέσοφ έκανε ένα πείραμα που έμεινε στην ιστορία. Πήρε ένα κοντινό πλάνο από το ανέκφραστο πρόσωπο ενός γνωστού ηθοποιού και το μόνταρε με τρεις διαφορετικές εικόνες.", "Around 1920, the Soviet director Lev Kuleshov carried out an experiment that went down in history. He took a close-up of a well-known actor's expressionless face and edited it together with three different images."),
  L("Ομιλήτρια", "f", "Στην πρώτη εκδοχή, μετά το πρόσωπο ερχόταν ένα πιάτο σούπα. Στη δεύτερη, ένα παιδί σε φέρετρο. Στην τρίτη, μια γυναίκα ξαπλωμένη σε έναν καναπέ. Σύμφωνα με τις μαρτυρίες, οι θεατές θαύμασαν την ερμηνεία του ηθοποιού: είδαν πείνα, θλίψη και επιθυμία, ενώ το πρόσωπο ήταν κάθε φορά το ίδιο.", "In the first version, the face was followed by a bowl of soup. In the second, a child in a coffin. In the third, a woman lying on a sofa. According to the accounts, the viewers admired the actor's performance: they saw hunger, grief and desire, although the face was the same every time."),
  L("Ομιλήτρια", "f", "Το συμπέρασμα ήταν ότι το νόημα ενός πλάνου δεν βρίσκεται μόνο μέσα του, αλλά και στη σχέση του με όσα προηγούνται και ακολουθούν. Ο θεατής συμπληρώνει μόνος του όσα δεν του δείχνουμε.", "The conclusion was that the meaning of a shot doesn't lie only within it, but also in its relation to what comes before and after. The viewer fills in by himself what we don't show him."),
  L("Ομιλήτρια", "f", "Οφείλω να σημειώσω ότι το αρχικό φιλμ δεν σώζεται, και ξέρουμε το πείραμα κυρίως από τις περιγραφές του Κουλέσοφ και των μαθητών του. Σύγχρονες επαναλήψεις του έχουν δώσει μικτά αποτελέσματα, αν και αρκετές επιβεβαιώνουν ότι το πλαίσιο επηρεάζει το πώς διαβάζουμε ένα πρόσωπο.", "I must point out that the original film hasn't survived, and we know the experiment mainly from the descriptions of Kuleshov and his students. Modern replications have given mixed results, although several confirm that context affects how we read a face."),
 ],
 "questions": [
  Q("Τι έκανε ο Κουλέσοφ στο πείραμά του;", ["Ζήτησε από έναν ηθοποιό να παίξει τρία συναισθήματα", "Μόνταρε το ίδιο ανέκφραστο πρόσωπο με τρεις διαφορετικές εικόνες", "Έδειξε τρεις ταινίες σε τρεις ομάδες", "Γύρισε μια ταινία χωρίς ηθοποιούς"], 1, "το μόνταρε με τρεις διαφορετικές εικόνες"),
  Q("Τι είδαν οι θεατές στο πρόσωπο του ηθοποιού;", ["Μόνο κούραση", "Τίποτα ιδιαίτερο", "Πείνα, θλίψη και επιθυμία", "Φόβο και θυμό"], 2, "είδαν πείνα, θλίψη και επιθυμία"),
  Q("Ποιο ήταν το συμπέρασμα του πειράματος;", ["Το νόημα ενός πλάνου εξαρτάται και από όσα προηγούνται και ακολουθούν", "Οι καλοί ηθοποιοί δεν χρειάζονται μοντάζ", "Οι θεατές προτιμούν τα κοντινά πλάνα", "Η μουσική είναι πιο σημαντική από την εικόνα"], 0, "το νόημα ενός πλάνου δεν βρίσκεται μόνο μέσα του, αλλά και στη σχέση του με όσα προηγούνται και ακολουθούν"),
  Q("Τι επιφύλαξη διατυπώνει η ομιλήτρια;", ["Ότι το πείραμα έγινε στην Αμερική", "Ότι ο ηθοποιός ήταν άγνωστος", "Ότι κανείς δεν προσπάθησε να το επαναλάβει", "Ότι το αρχικό φιλμ δεν σώζεται και οι επαναλήψεις έδωσαν μικτά αποτελέσματα"], 3, "το αρχικό φιλμ δεν σώζεται"),
 ],
 "gloss": {"πείραμα": "πείραμα — experiment", "κοντινό πλάνο": "κοντινό πλάνο — close-up", "ανέκφραστο": "ανέκφραστος — expressionless", "μόνταρε": "μοντάρω — to edit (film)", "εκδοχή": "εκδοχή — version", "φέρετρο": "φέρετρο — coffin", "μαρτυρίες": "μαρτυρία — testimony, account", "ερμηνεία": "ερμηνεία — performance (of an actor)", "συμπληρώνει": "συμπληρώνω — to fill in", "επαναλήψεις": "επανάληψη — replication, repetition", "πλαίσιο": "πλαίσιο — context, frame"}
})

rnd = random.Random(152)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-152.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
