# Source for library/listening/listening-27.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l27.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l27-ann-apergia", "title": "Απεργία στα μέσα μεταφοράς", "title_en": "A public transport strike", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση στο ραδιόφωνο για μια απεργία στα μέσα μαζικής μεταφοράς.",
 "script": [
  L("Εκφωνητής", "m", "Λόγω της εικοσιτετράωρης απεργίας που έχουν προκηρύξει τα σωματεία των εργαζομένων, την Πέμπτη δεν θα κυκλοφορήσουν τα λεωφορεία και τα τρόλεϊ. Το μετρό και ο ηλεκτρικός θα λειτουργήσουν με στάσεις εργασίας: δεν θα υπάρχουν δρομολόγια από τις δέκα το πρωί έως τις τέσσερις το απόγευμα.", "Because of the twenty-four-hour strike called by the workers' unions, on Thursday buses and trolleybuses will not run. The metro and the electric railway will operate with work stoppages: there will be no services from ten in the morning to four in the afternoon."),
  L("Εκφωνητής", "m", "Το τραμ θα κινείται κανονικά, ενώ ο προαστιακός θα πραγματοποιήσει μειωμένο αριθμό δρομολογίων, κυρίως προς και από το αεροδρόμιο. Οι επιβάτες με προγραμματισμένες πτήσεις καλούνται να ξεκινήσουν νωρίτερα από το σπίτι τους.", "The tram will run normally, while the suburban railway will run a reduced number of services, mainly to and from the airport. Passengers with scheduled flights are asked to leave home earlier."),
  L("Εκφωνητής", "m", "Η τροχαία αναμένει αυξημένη κίνηση στους κεντρικούς δρόμους και συστήνει στους οδηγούς να αποφύγουν το κέντρο τις πρωινές ώρες. Οι εργαζόμενοι ζητούν προσλήψεις προσωπικού και ανανέωση του στόλου των οχημάτων.", "The traffic police expect heavy traffic on the main roads and advise drivers to avoid the centre in the morning hours. The workers are asking for staff to be hired and the vehicle fleet to be renewed."),
 ],
 "questions": [
  Q("Ποιο μέσο θα κυκλοφορεί κανονικά την Πέμπτη;", ["Τα λεωφορεία", "Το τραμ", "Το μετρό", "Τα τρόλεϊ"], 1, "Το τραμ θα κινείται κανονικά"),
  Q("Πότε δεν θα υπάρχουν δρομολόγια στο μετρό;", ["Όλη τη μέρα", "Από τις δέκα το πρωί έως τις τέσσερις το απόγευμα", "Μόνο το βράδυ", "Μόνο το πρωί πριν τις δέκα"], 1, "δεν θα υπάρχουν δρομολόγια από τις δέκα το πρωί έως τις τέσσερις το απόγευμα"),
  Q("Τι ζητούν οι εργαζόμενοι;", ["Μικρότερο ωράριο", "Προσλήψεις προσωπικού και νέα οχήματα", "Φθηνότερα εισιτήρια", "Περισσότερες άδειες"], 1, "Οι εργαζόμενοι ζητούν προσλήψεις προσωπικού και ανανέωση του στόλου των οχημάτων"),
 ],
 "gloss": {"απεργία": "απεργία — strike", "έχουν προκηρύξει": "προκηρύσσω — to call, announce", "σωματεία": "σωματείο — union, association", "στάσεις εργασίας": "στάση εργασίας — work stoppage", "προαστιακός": "προαστιακός — suburban railway", "μειωμένο": "μειωμένος — reduced", "τροχαία": "τροχαία — traffic police", "συστήνει": "συστήνω — to advise, recommend", "προσλήψεις": "πρόσληψη — hiring", "στόλου": "στόλος — fleet"},
})

ITEMS.append({
 "id": "l27-vm-kipouros", "title": "Μήνυμα από τον κηπουρό", "title_en": "A message from the gardener", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τον κηπουρό που φροντίζει τον κήπο σας.",
 "script": [
  L("Κηπουρός", "m", "Καλησπέρα, κυρία Αθανασίου, ο Γρηγόρης είμαι, ο κηπουρός. Πέρασα σήμερα από τον κήπο, όπως κανονίσαμε, και κούρεψα το γκαζόν. Πρόσεξα όμως ότι η λεμονιά δίπλα στην πόρτα έχει άρρωστα φύλλα, κίτρινα με μαύρες κουκκίδες.", "Good evening, Mrs Athanasiou, it's Grigoris, the gardener. I came by the garden today, as we arranged, and mowed the lawn. But I noticed that the lemon tree by the door has diseased leaves, yellow with black spots."),
  L("Κηπουρός", "m", "Μάλλον είναι κάποιος μύκητας, από την πολλή υγρασία των τελευταίων εβδομάδων. Δεν είναι κάτι σοβαρό αν το πιάσουμε τώρα. Θα σας πρότεινα ένα βιολογικό σκεύασμα, χωρίς χημικά, αφού έχετε παιδιά και σκύλο που παίζουν στον κήπο.", "It's probably some kind of fungus, from all the humidity of the last few weeks. It isn't serious if we catch it now. I'd suggest an organic treatment, with no chemicals, since you have children and a dog playing in the garden."),
  L("Κηπουρός", "m", "Αν συμφωνείτε, μπορώ να έρθω το Σάββατο το πρωί να ψεκάσω και να κλαδέψω τα ξερά κλαδιά. Θα σας κοστίσει γύρω στα σαράντα ευρώ μαζί με το υλικό. Πείτε μου μόνο αν θα είστε σπίτι ή αν θα μου αφήσετε το κλειδί της αυλόπορτας στη γειτόνισσα.", "If you agree, I can come on Saturday morning to spray and prune the dry branches. It'll cost you about forty euros including the material. Just let me know whether you'll be at home or whether you'll leave the key to the garden gate with your neighbour."),
 ],
 "questions": [
  Q("Τι πρόβλημα έχει η λεμονιά;", ["Δεν κάνει λεμόνια", "Έχει άρρωστα φύλλα, πιθανώς από μύκητα", "Έσπασε ένα κλαδί της", "Έχει μυρμήγκια"], 1, "Μάλλον είναι κάποιος μύκητας"),
  Q("Γιατί προτείνει σκεύασμα χωρίς χημικά;", ["Γιατί είναι φθηνότερο", "Γιατί στον κήπο παίζουν παιδιά και σκύλος", "Γιατί τα χημικά απαγορεύονται", "Γιατί το ζήτησε η γειτόνισσα"], 1, "αφού έχετε παιδιά και σκύλο που παίζουν στον κήπο"),
  Q("Τι ζητάει να του πει η κυρία Αθανασίου;", ["Πόσα χρήματα θα του δώσει", "Αν θα είναι σπίτι ή αν θα αφήσει το κλειδί στη γειτόνισσα", "Ποιο σκεύασμα προτιμά", "Αν θέλει να κόψει τη λεμονιά"], 1, "Πείτε μου μόνο αν θα είστε σπίτι ή αν θα μου αφήσετε το κλειδί"),
 ],
 "gloss": {"κηπουρό": "κηπουρός — gardener", "κούρεψα": "κουρεύω — to mow, cut", "γκαζόν": "γκαζόν — lawn", "λεμονιά": "λεμονιά — lemon tree", "κουκκίδες": "κουκκίδα — dot, spot", "μύκητας": "μύκητας — fungus", "υγρασία": "υγρασία — humidity", "σκεύασμα": "σκεύασμα — preparation, product", "να ψεκάσω": "ψεκάζω — to spray", "να κλαδέψω": "κλαδεύω — to prune", "αυλόπορτας": "αυλόπορτα — garden gate"},
})

ITEMS.append({
 "id": "l27-dia-dema", "title": "Ένα δέμα για την Αυστραλία", "title_en": "A parcel for Australia", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα κατάστημα ταχυδρομείου.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Θέλω να στείλω αυτό το δέμα στη Μελβούρνη, στην αδελφή μου. Είναι γλυκά του κουταλιού, λάδι και μερικά βιβλία.", "Good morning. I want to send this parcel to Melbourne, to my sister. It's spoon sweets, oil and a few books."),
  L("Υπάλληλος", "f", "Τα βιβλία δεν έχουν πρόβλημα. Για τα τρόφιμα όμως η Αυστραλία έχει πολύ αυστηρούς κανόνες. Το λάδι επιτρέπεται, αν είναι σε κλειστή, εργοστασιακή συσκευασία. Το σπιτικό γλυκό μάλλον θα το κατασχέσουν στο τελωνείο.", "The books are no problem. For food, though, Australia has very strict rules. Oil is allowed if it's in sealed, factory packaging. The homemade sweet will probably be confiscated at customs."),
  L("Πελάτης", "m", "Κρίμα, το έφτιαξε η μητέρα μου. Λοιπόν, θα το βγάλω. Πόσο θα κοστίσει και πόσο θα κάνει να φτάσει;", "Pity, my mother made it. Well, I'll take it out. How much will it cost and how long will it take to arrive?"),
  L("Υπάλληλος", "f", "Το δέμα ζυγίζει τέσσερα κιλά. Με την οικονομική υπηρεσία κοστίζει πενήντα δύο ευρώ και φτάνει σε τρεις με πέντε εβδομάδες. Με την ταχεία, σε μία εβδομάδα, αλλά κοστίζει σχεδόν το διπλό. Και στις δύο περιπτώσεις πρέπει να συμπληρώσετε αυτό το έντυπο για το τελωνείο, με το περιεχόμενο και την αξία.", "The parcel weighs four kilos. With the economy service it costs fifty-two euros and arrives in three to five weeks. With express, in one week, but it costs almost double. In both cases you have to fill in this customs form, with the contents and the value."),
  L("Πελάτης", "m", "Δεν βιάζομαι, τα Χριστούγεννα είναι μακριά. Θα πάρω την οικονομική.", "I'm not in a hurry, Christmas is a long way off. I'll take economy."),
 ],
 "questions": [
  Q("Τι πιθανότατα δεν θα επιτραπεί να μπει στην Αυστραλία;", ["Τα βιβλία", "Το σπιτικό γλυκό", "Το λάδι σε εργοστασιακή συσκευασία", "Τίποτα από αυτά"], 1, "Το σπιτικό γλυκό μάλλον θα το κατασχέσουν στο τελωνείο"),
  Q("Πόσο κάνει να φτάσει το δέμα με την οικονομική υπηρεσία;", ["Μία εβδομάδα", "Τρεις με πέντε εβδομάδες", "Δύο μήνες", "Τρεις μέρες"], 1, "φτάνει σε τρεις με πέντε εβδομάδες"),
  Q("Γιατί διαλέγει ο πελάτης την οικονομική υπηρεσία;", ["Γιατί η ταχεία δεν πάει στην Αυστραλία", "Γιατί δεν βιάζεται", "Γιατί το δέμα είναι βαρύ", "Γιατί δεν θέλει να συμπληρώσει έντυπο"], 1, "Δεν βιάζομαι"),
 ],
 "gloss": {"δέμα": "δέμα — parcel", "γλυκά του κουταλιού": "γλυκό του κουταλιού — spoon sweet (fruit preserve)", "αυστηρούς": "αυστηρός — strict", "εργοστασιακή": "εργοστασιακός — factory", "συσκευασία": "συσκευασία — packaging", "σπιτικό": "σπιτικός — homemade", "θα το κατασχέσουν": "κατάσχω — to confiscate", "τελωνείο": "τελωνείο — customs", "ζυγίζει": "ζυγίζω — to weigh", "ταχεία": "ταχεία (υπηρεσία) — express (service)", "έντυπο": "έντυπο — form", "περιεχόμενο": "περιεχόμενο — contents"},
})

ITEMS.append({
 "id": "l27-dia-kamping", "title": "Στο κατάστημα για κάμπινγκ", "title_en": "At the camping shop", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα κατάστημα με είδη κάμπινγκ και ορειβασίας.",
 "script": [
  L("Πελάτισσα", "f", "Γεια σας. Θα πάμε με τον φίλο μου για τρεις μέρες στα Άγραφα, με σκηνή. Είναι η πρώτη μας φορά, και δεν έχουμε σχεδόν τίποτα.", "Hello. My boyfriend and I are going to the Agrafa mountains for three days, camping. It's our first time, and we have almost nothing."),
  L("Πωλητής", "m", "Ωραία επιλογή, αλλά ο Σεπτέμβρης στα βουνά μπορεί να είναι κρύος, ειδικά τη νύχτα. Το πιο σημαντικό είναι ο υπνόσακος: σας προτείνω έναν που αντέχει μέχρι τους μηδέν βαθμούς. Μη σας ξεγελάει η ζέστη της Αθήνας.", "Good choice, but September in the mountains can be cold, especially at night. The most important thing is the sleeping bag: I suggest one that's good down to zero degrees. Don't be fooled by the heat in Athens."),
  L("Πελάτισσα", "f", "Και σκηνή; Υπάρχουν τόσα μοντέλα.", "And a tent? There are so many models."),
  L("Πωλητής", "m", "Για δύο άτομα, πάρτε μια ελαφριά σκηνή τριών εποχών. Αυτή εδώ ζυγίζει λιγότερο από δύο κιλά και στήνεται σε πέντε λεπτά. Αν δεν θέλετε να ξοδέψετε πολλά για μια πρώτη δοκιμή, μπορείτε και να νοικιάσετε εξοπλισμό από εμάς: σκηνή, υπνόσακους και γκαζάκι, γύρω στα τριάντα ευρώ για όλο το τριήμερο.", "For two people, take a lightweight three-season tent. This one here weighs less than two kilos and goes up in five minutes. If you don't want to spend a lot on a first try, you can also rent equipment from us: tent, sleeping bags and a small gas stove, around thirty euros for the whole three days."),
  L("Πελάτισσα", "f", "Αυτό ακούγεται ιδανικό. Αν μας αρέσει, την επόμενη φορά θα αγοράσουμε δικά μας.", "That sounds ideal. If we like it, next time we'll buy our own."),
 ],
 "questions": [
  Q("Γιατί ο πωλητής δίνει τόση σημασία στον υπνόσακο;", ["Γιατί είναι το πιο φθηνό είδος", "Γιατί τις νύχτες στο βουνό μπορεί να κάνει κρύο", "Γιατί η σκηνή δεν προστατεύει από τη βροχή", "Γιατί η πελάτισσα έχει ήδη σκηνή"], 1, "ο Σεπτέμβρης στα βουνά μπορεί να είναι κρύος, ειδικά τη νύχτα"),
  Q("Τι πλεονέκτημα έχει η σκηνή που προτείνει;", ["Χωράει τέσσερα άτομα", "Είναι ελαφριά και στήνεται γρήγορα", "Είναι για τον χειμώνα", "Είναι η πιο φθηνή"], 1, "ζυγίζει λιγότερο από δύο κιλά και στήνεται σε πέντε λεπτά"),
  Q("Τι αποφασίζει τελικά η πελάτισσα;", ["Να αγοράσει όλο τον εξοπλισμό", "Να νοικιάσει εξοπλισμό για την πρώτη φορά", "Να μείνει σε ξενοδοχείο", "Να αναβάλει την εκδρομή"], 1, "Αυτό ακούγεται ιδανικό"),
 ],
 "gloss": {"ορειβασίας": "ορειβασία — mountaineering", "σκηνή": "σκηνή — tent", "υπνόσακος": "υπνόσακος — sleeping bag", "Μη σας ξεγελάει": "ξεγελάω — to fool, deceive", "ελαφριά": "ελαφρύς — light", "εποχών": "εποχή — season", "στήνεται": "στήνομαι — to be set up, pitched", "να ξοδέψετε": "ξοδεύω — to spend", "εξοπλισμό": "εξοπλισμός — equipment", "γκαζάκι": "γκαζάκι — small camping gas stove", "τριήμερο": "τριήμερο — three days, long weekend"},
})

ITEMS.append({
 "id": "l27-mon-anadoxi", "title": "Ανάδοχη μητέρα", "title_en": "A foster mother", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να μιλά για την εμπειρία της ως ανάδοχη μητέρα.",
 "script": [
  L("Γυναίκα", "f", "Όταν τα δικά μας παιδιά έφυγαν για σπουδές, το σπίτι άδειασε ξαφνικά. Ο άντρας μου κι εγώ νιώθαμε ότι είχαμε ακόμη πολλή αγάπη να δώσουμε. Έτσι κάναμε αίτηση να γίνουμε ανάδοχη οικογένεια.", "When our own children left for university, the house suddenly emptied. My husband and I felt we still had a lot of love to give. So we applied to become a foster family."),
  L("Γυναίκα", "f", "Η διαδικασία κράτησε σχεδόν έναν χρόνο: συνεντεύξεις με κοινωνικούς λειτουργούς, σεμινάρια, επισκέψεις στο σπίτι. Στην αρχή με εκνεύριζε, αλλά τώρα καταλαβαίνω γιατί είναι τόσο αυστηρή. Αυτά τα παιδιά έχουν ήδη περάσει πολλά.", "The process took almost a year: interviews with social workers, seminars, home visits. At first it annoyed me, but now I understand why it's so strict. These children have already been through a lot."),
  L("Γυναίκα", "f", "Ο Άγγελος ήρθε σε μας στα έξι του. Τους πρώτους μήνες δεν μιλούσε σχεδόν καθόλου και έκρυβε φαγητό κάτω από το κρεβάτι του, γιατί φοβόταν ότι αύριο δεν θα υπάρχει. Χρειάστηκε πολλή υπομονή για να καταλάβει ότι εδώ είναι ασφαλής.", "Angelos came to us at six. For the first months he hardly spoke at all and hid food under his bed, because he was afraid there wouldn't be any tomorrow. It took a lot of patience for him to understand that he's safe here."),
  L("Γυναίκα", "f", "Το πιο δύσκολο είναι να ξέρεις ότι ίσως κάποια μέρα επιστρέψει στη βιολογική του οικογένεια. Οι φίλοι μου με ρωτούν πώς θα το αντέξω. Τους απαντώ ότι η αναδοχή δεν σημαίνει ότι κρατάς ένα παιδί· σημαίνει ότι του δίνεις ένα ασφαλές σπίτι όσο το χρειάζεται.", "The hardest thing is knowing that one day he may return to his biological family. My friends ask me how I'll bear it. I tell them that fostering doesn't mean keeping a child; it means giving them a safe home for as long as they need it."),
 ],
 "questions": [
  Q("Γιατί αποφάσισαν να γίνουν ανάδοχη οικογένεια;", ["Γιατί δεν μπορούσαν να κάνουν παιδιά", "Γιατί, μετά την αναχώρηση των παιδιών τους, ένιωθαν ότι είχαν ακόμη αγάπη να δώσουν", "Γιατί τους το ζήτησε μια κοινωνική λειτουργός", "Για οικονομικούς λόγους"], 1, "νιώθαμε ότι είχαμε ακόμη πολλή αγάπη να δώσουμε"),
  Q("Τι έκανε ο Άγγελος τους πρώτους μήνες;", ["Έκλαιγε κάθε βράδυ", "Έκρυβε φαγητό κάτω από το κρεβάτι του", "Δεν ήθελε να πάει σχολείο", "Έφευγε από το σπίτι"], 1, "έκρυβε φαγητό κάτω από το κρεβάτι του"),
  Q("Πώς βλέπει η γυναίκα την αναδοχή;", ["Ως πρώτο βήμα για υιοθεσία", "Ως ένα ασφαλές σπίτι για όσο το χρειάζεται το παιδί", "Ως προσωρινή δουλειά", "Ως υποχρέωση προς το κράτος"], 1, "σημαίνει ότι του δίνεις ένα ασφαλές σπίτι όσο το χρειάζεται"),
 ],
 "gloss": {"ανάδοχη": "ανάδοχος — foster", "άδειασε": "αδειάζω — to empty", "κοινωνικούς λειτουργούς": "κοινωνικός λειτουργός — social worker", "με εκνεύριζε": "εκνευρίζω — to annoy", "έκρυβε": "κρύβω — to hide", "υπομονή": "υπομονή — patience", "ασφαλής": "ασφαλής — safe", "βιολογική": "βιολογικός — biological", "θα το αντέξω": "αντέχω — to bear, endure", "αναδοχή": "αναδοχή — fostering"},
})

ITEMS.append({
 "id": "l27-rep-nisyros", "title": "Η Νίσυρος", "title_en": "Nisyros", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από τη Νίσυρο, στα Δωδεκάνησα.",
 "script": [
  L("Δημοσιογράφος", "f", "Στέκομαι στον πάτο του κρατήρα Στέφανος, στο κέντρο της Νισύρου, και κάτω από τα πόδια μου το έδαφος είναι ζεστό. Από μικρές τρύπες βγαίνουν ατμοί που μυρίζουν θειάφι, και ακούγεται ένας ήχος σαν να βράζει κάτι βαθιά μέσα στη γη.", "I'm standing on the floor of the Stefanos crater, in the centre of Nisyros, and under my feet the ground is warm. Steam that smells of sulphur comes out of small holes, and there's a sound as if something were boiling deep inside the earth."),
  L("Δημοσιογράφος", "f", "Η Νίσυρος είναι ένα ηφαίστειο που αναδύθηκε από τη θάλασσα. Το ηφαίστειο θεωρείται ενεργό, αλλά οι τελευταίες εκρήξεις, τον δέκατο ένατο αιώνα, ήταν υδροθερμικές: ατμός και λάσπη, όχι λάβα. Οι επιστήμονες το παρακολουθούν συνεχώς με σεισμογράφους και αισθητήρες.", "Nisyros is a volcano that rose from the sea. The volcano is considered active, but the last eruptions, in the nineteenth century, were hydrothermal: steam and mud, not lava. Scientists monitor it continuously with seismographs and sensors."),
  L("Δημοσιογράφος", "f", "Το ηφαίστειο έχει χαρίσει στο νησί εύφορο έδαφος και ιαματικές πηγές. Στο Μανδράκι, την πρωτεύουσα, τα σπίτια είναι χτισμένα κάτω από ένα κάστρο, ενώ τα χωριά στο χείλος της καλντέρας, όπως η Νικιά, προσφέρουν μια από τις πιο εντυπωσιακές θέες του Αιγαίου. Οι κάτοικοι, λίγο περισσότεροι από χίλιοι, λένε χαμογελώντας ότι ζουν «πάνω στο καπάκι μιας κατσαρόλας».", "The volcano has given the island fertile soil and healing springs. In Mandraki, the capital, the houses are built below a castle, while the villages on the rim of the caldera, like Nikia, offer one of the most impressive views in the Aegean. The inhabitants, a little over a thousand, say with a smile that they live «on the lid of a pot»."),
 ],
 "questions": [
  Q("Τι νιώθει η δημοσιογράφος στον κρατήρα;", ["Κρύο αέρα", "Ζεστό έδαφος και μυρωδιά θειαφιού", "Βροχή", "Σεισμική δόνηση"], 1, "κάτω από τα πόδια μου το έδαφος είναι ζεστό"),
  Q("Πώς ήταν οι τελευταίες εκρήξεις του ηφαιστείου;", ["Με πολλή λάβα", "Υδροθερμικές, με ατμό και λάσπη", "Δεν έχει γίνει ποτέ έκρηξη", "Έγιναν πέρσι"], 1, "ήταν υδροθερμικές: ατμός και λάσπη, όχι λάβα"),
  Q("Τι εννοούν οι κάτοικοι λέγοντας ότι ζουν «πάνω στο καπάκι μιας κατσαρόλας»;", ["Ότι μαγειρεύουν πολύ", "Ότι ζουν πάνω σε ένα ηφαίστειο", "Ότι το νησί είναι μικρό", "Ότι κάνει πολλή ζέστη το καλοκαίρι"], 1, "ζουν «πάνω στο καπάκι μιας κατσαρόλας»"),
 ],
 "gloss": {"πάτο": "πάτος — bottom, floor", "κρατήρα": "κρατήρας — crater", "ατμοί": "ατμός — steam", "θειάφι": "θειάφι — sulphur", "αναδύθηκε": "αναδύομαι — to emerge, rise", "ενεργό": "ενεργός — active", "υδροθερμικές": "υδροθερμικός — hydrothermal", "αισθητήρες": "αισθητήρας — sensor", "εύφορο": "εύφορος — fertile", "ιαματικές πηγές": "ιαματικές πηγές — healing (thermal) springs", "χείλος": "χείλος — rim, edge", "καλντέρας": "καλντέρα — caldera", "καπάκι": "καπάκι — lid"},
})

ITEMS.append({
 "id": "l27-rep-vergina", "title": "Οι βασιλικοί τάφοι της Βεργίνας", "title_en": "The royal tombs of Vergina", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από το μουσείο των βασιλικών τάφων στη Βεργίνα της Μακεδονίας.",
 "script": [
  L("Δημοσιογράφος", "m", "Από έξω μοιάζει με έναν απλό λόφο σκεπασμένο με χορτάρι. Όταν όμως μπαίνεις μέσα, βρίσκεσαι σε έναν σκοτεινό, σιωπηλό χώρο, όπου λάμπουν χρυσά στεφάνια και πανοπλίες. Είναι το μουσείο των βασιλικών τάφων των Αιγών, της πρώτης πρωτεύουσας του αρχαίου μακεδονικού βασιλείου.", "From outside it looks like an ordinary hill covered in grass. But when you go inside, you find yourself in a dark, silent space where golden wreaths and suits of armour gleam. It is the museum of the royal tombs of Aigai, the first capital of the ancient Macedonian kingdom."),
  L("Δημοσιογράφος", "m", "Το 1977 ο αρχαιολόγος Μανόλης Ανδρόνικος ανακάλυψε κάτω από τον μεγάλο τύμβο τάφους που δεν είχαν συληθεί. Σε έναν από αυτούς βρέθηκε μια χρυσή λάρνακα με τα οστά ενός άνδρα, που ο Ανδρόνικος απέδωσε στον Φίλιππο Β΄, τον πατέρα του Μεγάλου Αλεξάνδρου. Η ταύτιση συζητιέται ακόμη από τους ειδικούς, αλλά η σημασία του ευρήματος δεν αμφισβητείται.", "In 1977 the archaeologist Manolis Andronikos discovered beneath the great mound tombs that had not been looted. In one of them a gold larnax was found with the bones of a man, whom Andronikos attributed to Philip II, the father of Alexander the Great. The identification is still debated by specialists, but the importance of the find is not disputed."),
  L("Δημοσιογράφος", "m", "Το μουσείο χτίστηκε μέσα στον ίδιο τον τύμβο, ώστε οι τάφοι να μείνουν στη θέση τους. Ο αρχαιολογικός χώρος έχει ανακηρυχθεί μνημείο παγκόσμιας κληρονομιάς από την UNESCO. «Εδώ δεν βλέπεις απλώς αντικείμενα», μου λέει μια φύλακας. «Νιώθεις ότι μπαίνεις σε έναν τάφο.»", "The museum was built inside the mound itself, so that the tombs could stay where they are. The archaeological site has been declared a World Heritage Site by UNESCO. «Here you don't just see objects», a guard tells me. «You feel that you're entering a tomb.»"),
 ],
 "questions": [
  Q("Πώς μοιάζει το μουσείο από έξω;", ["Με ένα σύγχρονο κτίριο από γυαλί", "Με έναν λόφο σκεπασμένο με χορτάρι", "Με έναν αρχαίο ναό", "Με ένα κάστρο"], 1, "μοιάζει με έναν απλό λόφο σκεπασμένο με χορτάρι"),
  Q("Τι ήταν ιδιαίτερο στους τάφους που βρήκε ο Ανδρόνικος;", ["Ήταν άδειοι", "Δεν είχαν συληθεί", "Ήταν ρωμαϊκοί", "Βρίσκονταν κάτω από τη θάλασσα"], 1, "τάφους που δεν είχαν συληθεί"),
  Q("Τι λέει το ρεπορτάζ για την ταύτιση του τάφου με τον Φίλιππο Β΄;", ["Ότι έχει αποδειχθεί οριστικά", "Ότι συζητιέται ακόμη από τους ειδικούς", "Ότι απορρίφθηκε", "Ότι έγινε το 2020"], 1, "Η ταύτιση συζητιέται ακόμη από τους ειδικούς"),
 ],
 "gloss": {"στεφάνια": "στεφάνι — wreath", "πανοπλίες": "πανοπλία — suit of armour", "τύμβο": "τύμβος — burial mound", "δεν είχαν συληθεί": "συλώ — to loot, rob (a tomb)", "λάρνακα": "λάρνακα — larnax, small coffin", "οστά": "οστό — bone", "απέδωσε": "αποδίδω — to attribute", "ταύτιση": "ταύτιση — identification", "ευρήματος": "εύρημα — find", "έχει ανακηρυχθεί": "ανακηρύσσομαι — to be declared"},
})

ITEMS.append({
 "id": "l27-int-maia", "title": "Μια μαία", "title_en": "A midwife", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια μαία που εργάζεται σε δημόσιο μαιευτήριο.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσα μωρά έχετε βοηθήσει να έρθουν στον κόσμο;", "How many babies have you helped bring into the world?"),
  L("Μαία", "f", "Κάπου τρεις χιλιάδες, σε είκοσι χρόνια. Κάθε φορά όμως είναι σαν την πρώτη. Ακόμη και σήμερα, όταν ακούω το πρώτο κλάμα ενός μωρού, ανατριχιάζω.", "About three thousand, in twenty years. But every time is like the first. Even today, when I hear a baby's first cry, I get goosebumps."),
  L("Δημοσιογράφος", "m", "Τι κάνει μια μαία που δεν κάνει ο γιατρός;", "What does a midwife do that a doctor doesn't?"),
  L("Μαία", "f", "Ο γιατρός επεμβαίνει όταν υπάρχει πρόβλημα. Εμείς είμαστε δίπλα στη γυναίκα σε όλη τη διάρκεια του τοκετού, που μπορεί να κρατήσει πολλές ώρες. Της εξηγούμε τι συμβαίνει, τη βοηθάμε να αναπνέει, να αλλάζει θέσεις, να μη φοβάται. Μετά τη γέννα, μαθαίνουμε στις μητέρες να θηλάζουν και να φροντίζουν το μωρό.", "The doctor intervenes when there's a problem. We are beside the woman throughout labour, which can last many hours. We explain what's happening, help her breathe, change position, not be afraid. After the birth, we teach mothers to breastfeed and look after the baby."),
  L("Δημοσιογράφος", "m", "Ποια είναι η μεγαλύτερη δυσκολία του επαγγέλματος;", "What's the biggest difficulty in the profession?"),
  L("Μαία", "f", "Οι βάρδιες και η έλλειψη προσωπικού. Υπάρχουν νύχτες που μία μαία έχει τρεις και τέσσερις γυναίκες ταυτόχρονα. Τότε δεν μπορείς να δώσεις σε καθεμιά τον χρόνο που της αξίζει, και αυτό είναι που με στενοχωρεί περισσότερο.", "The shifts and the shortage of staff. There are nights when one midwife has three or four women at the same time. Then you can't give each one the time she deserves, and that's what upsets me most."),
 ],
 "questions": [
  Q("Πώς νιώθει ακόμη η μαία όταν ακούει το πρώτο κλάμα ενός μωρού;", ["Κουρασμένη", "Ανατριχιάζει από συγκίνηση", "Αδιάφορη", "Ανήσυχη"], 1, "όταν ακούω το πρώτο κλάμα ενός μωρού, ανατριχιάζω"),
  Q("Ποιος είναι ο ρόλος της μαίας κατά τον τοκετό;", ["Κάνει μόνο τις επεμβάσεις", "Στέκεται δίπλα στη γυναίκα σε όλη τη διάρκεια και τη στηρίζει", "Συμπληρώνει τα χαρτιά", "Ειδοποιεί την οικογένεια"], 1, "Εμείς είμαστε δίπλα στη γυναίκα σε όλη τη διάρκεια του τοκετού"),
  Q("Τι τη στενοχωρεί περισσότερο;", ["Ο χαμηλός μισθός", "Ότι λόγω έλλειψης προσωπικού δεν μπορεί να δώσει αρκετό χρόνο σε κάθε γυναίκα", "Οι δύσκολοι γιατροί", "Η απόσταση από το σπίτι της"], 1, "δεν μπορείς να δώσεις σε καθεμιά τον χρόνο που της αξίζει"),
 ],
 "gloss": {"μαία": "μαία — midwife", "μαιευτήριο": "μαιευτήριο — maternity hospital", "κλάμα": "κλάμα — crying, cry", "ανατριχιάζω": "ανατριχιάζω — to shiver, get goosebumps", "επεμβαίνει": "επεμβαίνω — to intervene", "τοκετού": "τοκετός — labour, delivery", "να αναπνέει": "αναπνέω — to breathe", "γέννα": "γέννα — birth", "να θηλάζουν": "θηλάζω — to breastfeed", "βάρδιες": "βάρδια — shift", "έλλειψη": "έλλειψη — shortage, lack"},
})

ITEMS.append({
 "id": "l27-mon-ochi", "title": "Το «Όχι» του 1940", "title_en": "The «No» of 1940", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη για την 28η Οκτωβρίου 1940.",
 "script": [
  L("Ιστορικός", "f", "Τα ξημερώματα της 28ης Οκτωβρίου 1940, ο Ιταλός πρεσβευτής Εμανουέλε Γκράτσι επισκέφθηκε τον Ιωάννη Μεταξά στο σπίτι του, στην Κηφισιά, και του επέδωσε τελεσίγραφο: η Ελλάδα έπρεπε να επιτρέψει στα ιταλικά στρατεύματα να καταλάβουν στρατηγικά σημεία της χώρας. Ο Μεταξάς απέρριψε το αίτημα.", "In the early hours of 28 October 1940, the Italian ambassador Emanuele Grazzi visited Ioannis Metaxas at his home in Kifisia and handed him an ultimatum: Greece had to allow Italian troops to occupy strategic points in the country. Metaxas rejected the demand."),
  L("Ιστορικός", "f", "Αξίζει να σημειώσουμε ότι η περίφημη λέξη «Όχι» δεν ειπώθηκε, απ' ό,τι φαίνεται, αυτούσια. Σύμφωνα με τις μαρτυρίες, ο Μεταξάς απάντησε στα γαλλικά, «Alors, c'est la guerre», δηλαδή «Λοιπόν, έχουμε πόλεμο». Το «Όχι» είναι η συμπύκνωση που επέλεξε η συλλογική μνήμη· και, όπως συχνά συμβαίνει, το σύμβολο αποδείχθηκε ισχυρότερο από την ακριβή διατύπωση.", "It's worth noting that the famous word «No» was apparently not uttered as such. According to the testimonies, Metaxas replied in French, «Alors, c'est la guerre», that is, «Well, then it's war». «No» is the condensed version that collective memory chose; and, as often happens, the symbol proved stronger than the exact wording."),
  L("Ιστορικός", "f", "Αυτό που ακολούθησε ξάφνιασε την Ευρώπη. Ο ελληνικός στρατός όχι μόνο ανέκοψε την ιταλική επίθεση στα βουνά της Ηπείρου, αλλά απώθησε τους Ιταλούς βαθιά μέσα στην Αλβανία. Σε μια εποχή που ο Άξονας φαινόταν ανίκητος, ήταν μία από τις πρώτες νίκες των Συμμάχων στην ξηρά.", "What followed astonished Europe. The Greek army not only halted the Italian attack in the mountains of Epirus, but pushed the Italians back deep into Albania. At a time when the Axis seemed invincible, it was one of the first Allied victories on land."),
  L("Ιστορικός", "f", "Η νίκη, όμως, δεν άλλαξε την έκβαση. Τον Απρίλιο του 1941 η Γερμανία εισέβαλε στην Ελλάδα, και ακολούθησαν τρία χρόνια κατοχής. Γι' αυτό η 28η Οκτωβρίου δεν γιορτάζεται ως η μέρα μιας τελικής νίκης, αλλά ως η μέρα μιας επιλογής: της απόφασης να αντισταθείς, ακόμη κι όταν οι πιθανότητες είναι εναντίον σου.", "The victory, however, did not change the outcome. In April 1941 Germany invaded Greece, and three years of occupation followed. That is why 28 October is celebrated not as the day of a final victory, but as the day of a choice: the decision to resist, even when the odds are against you."),
 ],
 "questions": [
  Q("Τι ζητούσε το ιταλικό τελεσίγραφο;", ["Να κηρύξει η Ελλάδα πόλεμο στη Βρετανία", "Να επιτραπεί στα ιταλικά στρατεύματα να καταλάβουν στρατηγικά σημεία της χώρας", "Να παραδοθεί ο ελληνικός στόλος", "Να παραιτηθεί ο Μεταξάς"], 1, "η Ελλάδα έπρεπε να επιτρέψει στα ιταλικά στρατεύματα να καταλάβουν στρατηγικά σημεία της χώρας"),
  Q("Τι λέει η ιστορικός για τη λέξη «Όχι»;", ["Ότι ο Μεταξάς τη φώναξε στα ελληνικά", "Ότι μάλλον δεν ειπώθηκε αυτούσια, αλλά έμεινε ως σύμβολο", "Ότι την έγραψε ο Γκράτσι", "Ότι επινοήθηκε μετά τον πόλεμο από τους Γερμανούς"], 1, "η περίφημη λέξη «Όχι» δεν ειπώθηκε, απ' ό,τι φαίνεται, αυτούσια"),
  Q("Γιατί η νίκη του ελληνικού στρατού ξάφνιασε την Ευρώπη;", ["Γιατί ο ελληνικός στρατός ήταν ο μεγαλύτερος της Ευρώπης", "Γιατί ήταν μία από τις πρώτες νίκες κατά του Άξονα σε μια εποχή που φαινόταν ανίκητος", "Γιατί η Ιταλία δεν είχε στρατό", "Γιατί ο πόλεμος κράτησε μόνο μία μέρα"], 1, "Σε μια εποχή που ο Άξονας φαινόταν ανίκητος, ήταν μία από τις πρώτες νίκες"),
  Q("Ως τι γιορτάζεται, κατά την ιστορικό, η 28η Οκτωβρίου;", ["Ως η μέρα της τελικής νίκης", "Ως η μέρα μιας επιλογής αντίστασης", "Ως η μέρα της απελευθέρωσης", "Ως η μέρα της ίδρυσης του κράτους"], 1, "ως η μέρα μιας επιλογής: της απόφασης να αντισταθείς"),
 ],
 "gloss": {"ξημερώματα": "ξημερώματα — early hours, daybreak", "πρεσβευτής": "πρεσβευτής — ambassador", "επέδωσε": "επιδίδω — to hand over, serve", "τελεσίγραφο": "τελεσίγραφο — ultimatum", "απέρριψε": "απορρίπτω — to reject", "αυτούσια": "αυτούσιος — verbatim, in its exact form", "μαρτυρίες": "μαρτυρία — testimony", "συμπύκνωση": "συμπύκνωση — condensation, summary", "διατύπωση": "διατύπωση — wording", "ανέκοψε": "ανακόπτω — to halt, check", "απώθησε": "απωθώ — to push back, repel", "ανίκητος": "ανίκητος — invincible", "έκβαση": "έκβαση — outcome", "εισέβαλε": "εισβάλλω — to invade"},
})

ITEMS.append({
 "id": "l27-int-mikrovioma", "title": "Το μικροβίωμα του εντέρου", "title_en": "The gut microbiome", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια μικροβιολόγο για το μικροβίωμα του εντέρου.",
 "script": [
  L("Δημοσιογράφος", "m", "Ακούμε όλο και πιο συχνά τη λέξη «μικροβίωμα». Τι ακριβώς σημαίνει;", "We hear the word «microbiome» more and more often. What exactly does it mean?"),
  L("Μικροβιολόγος", "f", "Είναι το σύνολο των μικροοργανισμών που ζουν μέσα και πάνω στο σώμα μας, κυρίως στο έντερο: τρισεκατομμύρια βακτήρια, αλλά και μύκητες και ιοί. Για δεκαετίες τα βλέπαμε κυρίως ως απειλή. Σήμερα ξέρουμε ότι τα περισσότερα όχι μόνο δεν μας βλάπτουν, αλλά μας είναι απαραίτητα: βοηθούν στην πέψη, παράγουν βιταμίνες και εκπαιδεύουν το ανοσοποιητικό μας σύστημα.", "It's all the microorganisms that live in and on our body, mainly in the gut: trillions of bacteria, but also fungi and viruses. For decades we saw them mainly as a threat. Today we know that most of them not only don't harm us, but are essential to us: they help digestion, produce vitamins and train our immune system."),
  L("Δημοσιογράφος", "m", "Μπορούμε να επηρεάσουμε το μικροβίωμά μας;", "Can we influence our microbiome?"),
  L("Μικροβιολόγος", "f", "Σε μεγάλο βαθμό, ναι, κυρίως μέσω της διατροφής. Η ποικιλία είναι το κλειδί: μια διατροφή πλούσια σε φυτικές ίνες, λαχανικά, όσπρια και ζυμωμένα τρόφιμα, όπως το γιαούρτι, φαίνεται να ευνοεί ένα πιο ποικίλο μικροβίωμα. Αντίθετα, η αλόγιστη χρήση αντιβιοτικών μπορεί να το διαταράξει για μεγάλο διάστημα.", "To a large extent, yes, mainly through diet. Variety is the key: a diet rich in fibre, vegetables, pulses and fermented foods, like yoghurt, seems to favour a more diverse microbiome. Conversely, the reckless use of antibiotics can disrupt it for a long time."),
  L("Μικροβιολόγος", "f", "Θέλω όμως να είμαι προσεκτική. Υπάρχουν ενδιαφέρουσες ενδείξεις ότι το μικροβίωμα επικοινωνεί ακόμη και με τον εγκέφαλο και ίσως επηρεάζει τη διάθεσή μας. Η έρευνα αυτή, όμως, είναι ακόμη στα πρώτα της βήματα. Όταν βλέπετε συμπληρώματα που υπόσχονται να «θεραπεύσουν» το άγχος μέσω του εντέρου, να είστε δύσπιστοι: η επιστήμη δεν έχει φτάσει ακόμη εκεί.", "But I want to be careful. There are interesting indications that the microbiome communicates even with the brain and may affect our mood. This research, however, is still in its early stages. When you see supplements promising to «cure» anxiety through the gut, be sceptical: science isn't there yet."),
 ],
 "questions": [
  Q("Πώς άλλαξε η αντίληψή μας για τα βακτήρια του εντέρου;", ["Τα θεωρούμε πλέον πιο επικίνδυνα", "Παλιά τα βλέπαμε ως απειλή, σήμερα ξέρουμε ότι τα περισσότερα είναι απαραίτητα", "Δεν άλλαξε καθόλου", "Ανακαλύψαμε ότι δεν υπάρχουν"], 1, "Για δεκαετίες τα βλέπαμε κυρίως ως απειλή"),
  Q("Τι φαίνεται να ευνοεί ένα ποικίλο μικροβίωμα;", ["Τα αντιβιοτικά", "Μια ποικίλη διατροφή πλούσια σε φυτικές ίνες και ζυμωμένα τρόφιμα", "Η νηστεία", "Τα συμπληρώματα βιταμινών"], 1, "μια διατροφή πλούσια σε φυτικές ίνες, λαχανικά, όσπρια και ζυμωμένα τρόφιμα"),
  Q("Τι λέει για τη σχέση μικροβιώματος και εγκεφάλου;", ["Ότι έχει αποδειχθεί πλήρως", "Ότι υπάρχουν ενδείξεις, αλλά η έρευνα είναι στην αρχή", "Ότι δεν υπάρχει καμία σχέση", "Ότι τα συμπληρώματα θεραπεύουν το άγχος"], 1, "Η έρευνα αυτή, όμως, είναι ακόμη στα πρώτα της βήματα"),
  Q("Τι συμβουλεύει για τα συμπληρώματα που υπόσχονται θεραπεία του άγχους;", ["Να τα δοκιμάσουμε", "Να είμαστε δύσπιστοι", "Να τα παίρνουμε με αντιβιοτικά", "Να τα δίνουμε στα παιδιά"], 1, "να είστε δύσπιστοι"),
 ],
 "gloss": {"μικροβίωμα": "μικροβίωμα — microbiome", "εντέρου": "έντερο — gut, intestine", "μικροοργανισμών": "μικροοργανισμός — microorganism", "τρισεκατομμύρια": "τρισεκατομμύριο — trillion", "ιοί": "ιός — virus", "πέψη": "πέψη — digestion", "ανοσοποιητικό": "ανοσοποιητικό (σύστημα) — immune system", "φυτικές ίνες": "φυτικές ίνες — dietary fibre", "ζυμωμένα": "ζυμωμένος — fermented", "αλόγιστη": "αλόγιστος — reckless, thoughtless", "να το διαταράξει": "διαταράσσω — to disrupt", "ενδείξεις": "ένδειξη — indication", "συμπληρώματα": "συμπλήρωμα — supplement", "δύσπιστοι": "δύσπιστος — sceptical"},
})
rnd = random.Random(27)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-27.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
