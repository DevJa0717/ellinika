# Source for library/listening/listening-228.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l228.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l228-news-sxolikoi-dromoi", "title": "Δρόμοι χωρίς αυτοκίνητα έξω από τα σχολεία", "title_en": "Car-free streets outside schools", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο ραδιόφωνο για ένα πιλοτικό πρόγραμμα ενός δήμου.",
 "script": [
  L("Εκφωνήτρια", "f", "Από τη Δευτέρα, πέντε δρόμοι έξω από δημοτικά σχολεία ενός δήμου της Θεσσαλονίκης θα κλείνουν για τα αυτοκίνητα δύο φορές την ημέρα: μισή ώρα το πρωί, την ώρα που μπαίνουν τα παιδιά, και μισή ώρα το μεσημέρι, την ώρα που σχολάνε.", "From Monday, five streets outside primary schools in a Thessaloniki municipality will close to cars twice a day: for half an hour in the morning, when the children go in, and half an hour at midday, when school lets out."),
  L("Εκφωνήτρια", "f", "Στις άκρες των δρόμων θα μπαίνουν κινητά εμπόδια, και δημοτικοί αστυνομικοί θα βρίσκονται εκεί τις πρώτες εβδομάδες. Θα μπορούν να περνούν μόνο οι κάτοικοι του δρόμου, με πολύ χαμηλή ταχύτητα, καθώς και τα οχήματα έκτακτης ανάγκης.", "Movable barriers will be placed at the ends of the streets, and municipal police officers will be there for the first few weeks. Only residents of the street will be able to drive through, very slowly, as well as emergency vehicles."),
  L("Εκφωνήτρια", "f", "Ο δήμος εξηγεί ότι ο στόχος είναι λιγότερος κίνδυνος για τα παιδιά και καθαρότερος αέρας στις πύλες των σχολείων, όπου την ώρα της αιχμής σχηματίζονται ουρές από αυτοκίνητα με αναμμένες μηχανές. Παρόμοια προγράμματα εφαρμόζονται ήδη σε αρκετές ευρωπαϊκές πόλεις.", "The municipality explains that the aim is less danger for children and cleaner air at the school gates, where at rush hour queues of cars form with their engines running. Similar schemes already operate in several European cities."),
  L("Εκφωνήτρια", "f", "Δεν είναι όλοι ενθουσιασμένοι. Ορισμένοι γονείς που περνούν από το σχολείο πηγαίνοντας στη δουλειά λένε ότι θα αναγκαστούν να ξυπνούν νωρίτερα. Ο δήμος απαντά ότι θα αξιολογήσει το πρόγραμμα τον Ιούνιο, πριν αποφασίσει αν θα το επεκτείνει.", "Not everyone is enthusiastic. Some parents who drop off at school on their way to work say they'll have to get up earlier. The municipality replies that it will evaluate the scheme in June before deciding whether to extend it."),
 ],
 "questions": [
  Q("Πότε θα κλείνουν οι δρόμοι για τα αυτοκίνητα;", ["Όλη την ημέρα", "Μισή ώρα το πρωί και μισή ώρα το μεσημέρι", "Μόνο τα Σαββατοκύριακα", "Μόνο τις μέρες με κακό καιρό"], 1, "μισή ώρα το πρωί, την ώρα που μπαίνουν τα παιδιά, και μισή ώρα το μεσημέρι"),
  Q("Ποιοι θα μπορούν να περνούν;", ["Όλοι οι γονείς", "Τα σχολικά λεωφορεία μόνο", "Οι κάτοικοι του δρόμου, αργά, και τα οχήματα έκτακτης ανάγκης", "Κανείς απολύτως"], 2, "Θα μπορούν να περνούν μόνο οι κάτοικοι του δρόμου, με πολύ χαμηλή ταχύτητα, καθώς και τα οχήματα έκτακτης ανάγκης"),
  Q("Ποιος είναι ο στόχος του προγράμματος;", ["Να βρουν θέσεις στάθμευσης οι δάσκαλοι", "Λιγότερος κίνδυνος για τα παιδιά και καθαρότερος αέρας", "Να μειωθεί ο θόρυβος τη νύχτα", "Να μαζευτούν χρήματα από πρόστιμα"], 1, "ο στόχος είναι λιγότερος κίνδυνος για τα παιδιά και καθαρότερος αέρας"),
  Q("Τι θα γίνει τον Ιούνιο;", ["Το πρόγραμμα θα σταματήσει οριστικά", "Θα κλείσουν τα σχολεία για επισκευές", "Ο δήμος θα αξιολογήσει το πρόγραμμα", "Θα ξεκινήσει σε όλη την πόλη"], 2, "θα αξιολογήσει το πρόγραμμα τον Ιούνιο"),
 ],
 "gloss": {"σχολάνε": "σχολάω — to finish school/work for the day", "εμπόδια": "εμπόδιο — barrier, obstacle", "οχήματα": "όχημα — vehicle", "έκτακτης": "έκτακτη ανάγκη — emergency", "αιχμής": "ώρα αιχμής — rush hour", "πύλες": "πύλη — gate", "ενθουσιασμένοι": "ενθουσιασμένος — enthusiastic", "αξιολογήσει": "αξιολογώ — to evaluate", "επεκτείνει": "επεκτείνω — to extend"},
})
ITEMS.append({
 "id": "l228-vm-psaras", "title": "Μήνυμα από τον ψαρά για την παραγγελία", "title_en": "A message from the fisherman about your order", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε παραγγείλει ψάρια από έναν ψαρά του νησιού για ένα οικογενειακό τραπέζι. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Ψαράς", "m", "Γεια σου, Ελένη, ο Στέλιος είμαι, ο ψαράς. Σε παίρνω για τα ψάρια που μου παρήγγειλες για την Κυριακή, τα φαγγριά και τα μπαρμπούνια για το τραπέζι της γιορτής.", "Hi, Eleni, it's Stelios, the fisherman. I'm calling about the fish you ordered from me for Sunday, the sea bream and the red mullet for the name-day meal."),
  L("Ψαράς", "m", "Τα νέα δεν είναι καλά: από χθες φυσάει πολύ δυνατός βοριάς, εννιά μποφόρ, και το λιμεναρχείο έχει απαγορεύσει τον απόπλου στα μικρά σκάφη. Σύμφωνα με τον καιρό, δεν θα κοπάσει πριν από την Κυριακή, οπότε δεν θα μπορέσω να βγω.", "The news isn't good: since yesterday there's been a very strong north wind, force nine, and the port authority has banned small boats from sailing. According to the forecast, it won't die down before Sunday, so I won't be able to go out."),
  L("Ψαράς", "m", "Σου προτείνω δύο λύσεις. Η πρώτη: έχω στο ψυγείο σαρδέλες και γόπες που έπιασα την Τετάρτη, πριν από τον αέρα· είναι ολόφρεσκες και κάνουν πολύ καλό τηγανητό. Η δεύτερη: να μεταφέρεις το τραπέζι για την επόμενη Κυριακή, και σου κρατάω ό,τι καλύτερο πιάσω.", "I suggest two solutions. The first: I've got sardines and bogue in the fridge that I caught on Wednesday, before the wind; they're perfectly fresh and make a very good fry. The second: move the meal to the following Sunday, and I'll keep the best of whatever I catch for you."),
  L("Ψαράς", "m", "Πες μου μέχρι αύριο το βράδυ τι θέλεις, γιατί τις σαρδέλες μού τις ζητάει και η ταβέρνα στο λιμάνι. Και συγγνώμη· με τη θάλασσα, ποτέ δεν ξέρεις.", "Let me know by tomorrow evening what you want, because the taverna at the harbour is asking for the sardines too. And sorry; with the sea, you never know."),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί να βγει για ψάρεμα ο Στέλιος;", ["Γιατί χάλασε η βάρκα του", "Γιατί φυσάει δυνατός βοριάς και απαγορεύεται ο απόπλους", "Γιατί είναι άρρωστος", "Γιατί είναι αργία"], 1, "φυσάει πολύ δυνατός βοριάς, εννιά μποφόρ, και το λιμεναρχείο έχει απαγορεύσει τον απόπλου"),
  Q("Τι έχει στο ψυγείο;", ["Φαγγριά και μπαρμπούνια", "Χταπόδια", "Σαρδέλες και γόπες που έπιασε την Τετάρτη", "Τίποτα"], 2, "έχω στο ψυγείο σαρδέλες και γόπες που έπιασα την Τετάρτη"),
  Q("Ποια είναι η δεύτερη λύση που προτείνει;", ["Να αγοράσει ψάρια από το σούπερ μάρκετ", "Να μεταφέρει το τραπέζι για την επόμενη Κυριακή", "Να φάνε κρέας", "Να πάει η ίδια στο λιμάνι"], 1, "να μεταφέρεις το τραπέζι για την επόμενη Κυριακή"),
  Q("Γιατί θέλει απάντηση ως αύριο το βράδυ;", ["Γιατί φεύγει ταξίδι", "Γιατί τις σαρδέλες τις ζητάει και μια ταβέρνα", "Γιατί κλείνει το ψυγείο", "Γιατί αλλάζει ο καιρός"], 1, "τις σαρδέλες μού τις ζητάει και η ταβέρνα στο λιμάνι"),
 ],
 "gloss": {"φαγγριά": "φαγγρί — sea bream (red porgy)", "μπαρμπούνια": "μπαρμπούνι — red mullet", "βοριάς": "βοριάς — north wind", "μποφόρ": "μποφόρ — Beaufort (wind force)", "λιμεναρχείο": "λιμεναρχείο — port authority", "απόπλου": "απόπλους — departure (of a ship), sailing", "κοπάσει": "κοπάζω — to die down, abate", "γόπες": "γόπα — bogue (small fish)", "ολόφρεσκες": "ολόφρεσκος — perfectly fresh", "τηγανητό": "τηγανητό — fried dish, fry"},
})
ITEMS.append({
 "id": "l228-c1-mono-klepsydra", "title": "Ο χρόνος σε νερό: η κλεψύδρα των αθηναϊκών δικαστηρίων", "title_en": "Time in water: the clepsydra of the Athenian courts", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ραδιοφωνική εκπομπή για την καθημερινή ζωή στην αρχαία Αθήνα.",
 "script": [
  L("Ομιλητής", "m", "Στα δικαστήρια της κλασικής Αθήνας δεν υπήρχαν δικηγόροι με τη σημερινή έννοια. Κατήγορος και κατηγορούμενος μιλούσαν οι ίδιοι μπροστά σε εκατοντάδες ενόρκους, και ο χρόνος που είχε ο καθένας μετριόταν με ένα απλό αλλά έξυπνο σκεύος: την κλεψύδρα.", "In the courts of classical Athens there were no lawyers in today's sense. Accuser and accused spoke themselves before hundreds of jurors, and the time each one had was measured with a simple but clever vessel: the clepsydra."),
  L("Ομιλητής", "m", "Η λέξη σημαίνει κατά λέξη «αυτή που κλέβει το νερό». Ήταν ένα πήλινο δοχείο με μια μικρή οπή κοντά στη βάση. Γέμιζε με νερό, και όταν ο ομιλητής άρχιζε, έβγαζαν το βούλωμα. Μια κλεψύδρα που βρέθηκε στην αρχαία Αγορά χωρούσε περίπου έξι λίτρα και, απ' ό,τι υπολογίζουν οι αρχαιολόγοι, άδειαζε σε περίπου έξι λεπτά.", "The word literally means 'the one that steals the water'. It was a clay vessel with a small hole near the base. It was filled with water, and when the speaker began, the plug was removed. A clepsydra found in the ancient Agora held about six litres and, as archaeologists calculate, emptied in about six minutes."),
  L("Ομιλητής", "m", "Το νερό ήταν τόσο πολύτιμο που, όταν διαβαζόταν ένας νόμος ή μια μαρτυρία, ο ομιλητής ζητούσε να σταματήσει η ροή, ώστε να μη χάσει χρόνο από την ομιλία του. Στους σωζόμενους λόγους των ρητόρων συναντάμε συχνά τέτοιες εκκλήσεις προς τον υπάλληλο του νερού.", "Water was so precious that, when a law or a testimony was being read, the speaker asked for the flow to be stopped, so that he wouldn't lose time from his speech. In the surviving speeches of the orators we often find such appeals to the official in charge of the water."),
  L("Ομιλητής", "m", "Μου αρέσει να σκέφτομαι ότι η αθηναϊκή δημοκρατία, που τόσο συχνά την περιγράφουμε με μεγάλα λόγια, στηριζόταν και σε τέτοιες ταπεινές λεπτομέρειες. Η ισότητα δεν ήταν μόνο ιδέα· ήταν και ένα δοχείο που άδειαζε με τον ίδιο ρυθμό για τον πλούσιο και για τον φτωχό.", "I like to think that Athenian democracy, which we so often describe in grand words, also rested on humble details like this. Equality wasn't just an idea; it was also a vessel that emptied at the same rate for rich and poor alike."),
 ],
 "questions": [
  Q("Ποιοι μιλούσαν στα αθηναϊκά δικαστήρια;", ["Επαγγελματίες δικηγόροι", "Ο κατήγορος και ο κατηγορούμενος οι ίδιοι", "Μόνο οι δικαστές", "Οι μάρτυρες"], 1, "Κατήγορος και κατηγορούμενος μιλούσαν οι ίδιοι"),
  Q("Πόσο χρόνο, περίπου, έδινε η κλεψύδρα της αρχαίας Αγοράς;", ["Ένα λεπτό", "Περίπου έξι λεπτά", "Μία ώρα", "Μια ολόκληρη μέρα"], 1, "άδειαζε σε περίπου έξι λεπτά"),
  Q("Τι ζητούσε ο ομιλητής όταν διαβαζόταν ένας νόμος;", ["Να ξαναγεμίσει η κλεψύδρα", "Να σταματήσει η ροή του νερού", "Να βγουν οι ένορκοι", "Να διαβαστεί πιο αργά"], 1, "ο ομιλητής ζητούσε να σταματήσει η ροή"),
  Q("Ποιο είναι το συμπέρασμα του ομιλητή;", ["Ότι η αθηναϊκή δημοκρατία ήταν άδικη", "Ότι η κλεψύδρα ήταν ακριβή", "Ότι η ισότητα στηριζόταν και σε απλές πρακτικές λεπτομέρειες", "Ότι οι πλούσιοι είχαν περισσότερο χρόνο"], 2, "Η ισότητα δεν ήταν μόνο ιδέα· ήταν και ένα δοχείο που άδειαζε με τον ίδιο ρυθμό"),
 ],
 "gloss": {"κλεψύδρα": "κλεψύδρα — clepsydra, water clock", "κατηγορούμενος": "κατηγορούμενος — the accused, defendant", "ενόρκους": "ένορκος — juror", "σκεύος": "σκεύος — vessel, utensil", "πήλινο": "πήλινος — clay, earthenware", "οπή": "οπή — hole, opening", "βούλωμα": "βούλωμα — plug, stopper", "μαρτυρία": "μαρτυρία — testimony", "εκκλήσεις": "έκκληση — appeal", "ταπεινές": "ταπεινός — humble"},
})
ITEMS.append({
 "id": "l228-c1-int-palaiografos", "title": "Μια παλαιογράφος για τα χειρόγραφα που μιλούν", "title_en": "A palaeographer on manuscripts that speak", "type": "interview", "level": "C1",
 "context_el": "Μια παλαιογράφος που μελετά βυζαντινά χειρόγραφα μιλά σε μια ραδιοφωνική εκπομπή για τον πολιτισμό.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς κάνει ένας παλαιογράφος;", "What exactly does a palaeographer do?"),
  L("Παλαιογράφος", "f", "Στην πιο απλή εκδοχή, διαβάζει παλιές γραφές. Στην πράξη, όμως, ένα χειρόγραφο σπάνια σου λέει πότε και πού γράφτηκε. Πρέπει να το μαντέψεις από το σχήμα των γραμμάτων, από τις συντομογραφίες που χρησιμοποιεί ο γραφέας, ακόμη κι από τον τρόπο που έχει χαράξει τις γραμμές στην περγαμηνή. Κάθε εποχή και κάθε εργαστήριο έχει τις συνήθειές του, όπως ο καθένας μας έχει τον γραφικό του χαρακτήρα.", "In the simplest version, they read old scripts. In practice, though, a manuscript rarely tells you when and where it was written. You have to deduce it from the shape of the letters, from the abbreviations the scribe uses, even from the way he has ruled the lines on the parchment. Every period and every workshop has its habits, just as each of us has our own handwriting."),
  L("Δημοσιογράφος", "m", "Η τεχνολογία έχει αλλάξει τη δουλειά σας;", "Has technology changed your work?"),
  L("Παλαιογράφος", "f", "Ριζικά. Η πολυφασματική απεικόνιση, δηλαδή η φωτογράφιση με διαφορετικά μήκη κύματος φωτός, μας επιτρέπει να διαβάζουμε κείμενα που έχουν σβηστεί. Τον Μεσαίωνα η περγαμηνή ήταν ακριβή, έτσι συχνά έξυναν ένα παλιό βιβλίο και έγραφαν από πάνω ένα καινούργιο. Αυτά λέγονται παλίμψηστα. Το πιο διάσημο παράδειγμα είναι ένα βιβλίο προσευχών κάτω από το οποίο βρέθηκαν έργα του Αρχιμήδη που δεν σώζονταν πουθενά αλλού.", "Radically. Multispectral imaging, that is, photography with different wavelengths of light, lets us read texts that have been erased. In the Middle Ages parchment was expensive, so they often scraped an old book and wrote a new one over it. These are called palimpsests. The most famous example is a prayer book beneath which works by Archimedes were found that survive nowhere else."),
  L("Δημοσιογράφος", "m", "Υπάρχει κάτι που σας συγκινεί ιδιαίτερα σε αυτά τα χειρόγραφα;", "Is there anything in these manuscripts that particularly moves you?"),
  L("Παλαιογράφος", "f", "Οι σημειώσεις στα περιθώρια. Ένας γραφέας γράφει ότι κρυώνει και τα δάχτυλά του δεν υπακούνε, ένας άλλος παρακαλεί τον αναγνώστη να τον συγχωρήσει για τα λάθη του. Ξαφνικά, πίσω από το επίσημο κείμενο, εμφανίζεται ένας άνθρωπος που κουράζεται, που βαριέται, που θέλει να τελειώσει. Αυτές οι μικρές φωνές με κάνουν να νιώθω ότι δεν διαβάζω απλώς ένα αντικείμενο, αλλά κάποιον.", "The notes in the margins. One scribe writes that he's cold and his fingers won't obey, another begs the reader to forgive him for his mistakes. Suddenly, behind the official text, a person appears who gets tired, who gets bored, who wants to finish. These small voices make me feel that I'm not just reading an object, but someone."),
 ],
 "questions": [
  Q("Πώς χρονολογεί ένας παλαιογράφος ένα χειρόγραφο;", ["Από την ημερομηνία στο εξώφυλλο", "Από το σχήμα των γραμμάτων, τις συντομογραφίες και άλλες λεπτομέρειες", "Μόνο με χημικές αναλύσεις", "Από τον κατάλογο της βιβλιοθήκης"], 1, "Πρέπει να το μαντέψεις από το σχήμα των γραμμάτων, από τις συντομογραφίες"),
  Q("Τι είναι τα παλίμψηστα;", ["Βιβλία γραμμένα σε χαρτί", "Περγαμηνές όπου ένα παλιό κείμενο ξύστηκε και γράφτηκε από πάνω καινούργιο", "Χειρόγραφα με εικόνες", "Αντίγραφα έντυπων βιβλίων"], 1, "συχνά έξυναν ένα παλιό βιβλίο και έγραφαν από πάνω ένα καινούργιο"),
  Q("Τι βρέθηκε κάτω από ένα βιβλίο προσευχών;", ["Ένας χάρτης", "Έργα του Αρχιμήδη που δεν σώζονταν αλλού", "Μια ερωτική επιστολή", "Μουσικές νότες"], 1, "βρέθηκαν έργα του Αρχιμήδη που δεν σώζονταν πουθενά αλλού"),
  Q("Γιατί τη συγκινούν οι σημειώσεις στα περιθώρια;", ["Γιατί έχουν μεγάλη χρηματική αξία", "Γιατί διορθώνουν το κείμενο", "Γιατί φανερώνουν τον άνθρωπο πίσω από το κείμενο", "Γιατί είναι γραμμένες σε άλλη γλώσσα"], 2, "πίσω από το επίσημο κείμενο, εμφανίζεται ένας άνθρωπος"),
 ],
 "gloss": {"παλαιογράφος": "παλαιογράφος — palaeographer", "χειρόγραφα": "χειρόγραφο — manuscript", "συντομογραφίες": "συντομογραφία — abbreviation", "γραφέας": "γραφέας — scribe", "περγαμηνή": "περγαμηνή — parchment", "πολυφασματική": "πολυφασματικός — multispectral", "απεικόνιση": "απεικόνιση — imaging, depiction", "έξυναν": "ξύνω — to scrape", "παλίμψηστα": "παλίμψηστο — palimpsest", "περιθώρια": "περιθώριο — margin", "υπακούνε": "υπακούω — to obey"},
})
rnd = random.Random(228)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-228.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
