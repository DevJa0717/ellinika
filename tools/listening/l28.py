# Source for library/listening/listening-28.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l28.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l28-ann-ora", "title": "Αλλάζει η ώρα", "title_en": "The clocks are changing", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση στο ραδιόφωνο για την αλλαγή της ώρας.",
 "script": [
  L("Εκφωνήτρια", "f", "Υπενθυμίζουμε στους ακροατές μας ότι τα ξημερώματα της Κυριακής τελειώνει η θερινή ώρα. Στις τέσσερις το πρωί, οι δείκτες των ρολογιών θα γυρίσουν μία ώρα πίσω, στις τρεις. Έτσι, όσοι το επιθυμούν, θα κερδίσουν μία ώρα ύπνου.", "We remind our listeners that summer time ends in the early hours of Sunday. At four in the morning, clock hands will go back one hour, to three. So anyone who wishes will gain an hour's sleep."),
  L("Εκφωνήτρια", "f", "Τα κινητά τηλέφωνα και οι υπολογιστές θα αλλάξουν ώρα αυτόματα. Θα πρέπει όμως να ρυθμίσετε μόνοι σας τα ρολόγια του τοίχου, του φούρνου και του αυτοκινήτου. Όσοι ταξιδεύουν την Κυριακή το πρωί καλό είναι να ελέγξουν την ώρα αναχώρησης του πλοίου ή της πτήσης τους.", "Mobile phones and computers will change time automatically. You will, however, have to set wall clocks, oven clocks and car clocks yourselves. Anyone travelling on Sunday morning should check the departure time of their ship or flight."),
  L("Εκφωνήτρια", "f", "Οι γιατροί συμβουλεύουν, ιδίως τους γονείς μικρών παιδιών, να μεταθέτουν σταδιακά την ώρα του ύπνου, κατά δέκα με δεκαπέντε λεπτά κάθε βράδυ, ώστε ο οργανισμός να προσαρμοστεί πιο εύκολα.", "Doctors advise, especially parents of young children, to shift bedtime gradually, by ten to fifteen minutes each evening, so that the body can adjust more easily."),
 ],
 "questions": [
  Q("Τι θα γίνει στις τέσσερις το πρωί της Κυριακής;", ["Τα ρολόγια θα πάνε μία ώρα μπροστά", "Τα ρολόγια θα γυρίσουν μία ώρα πίσω", "Θα κοπεί το ρεύμα", "Θα αρχίσει η θερινή ώρα"], 1, "οι δείκτες των ρολογιών θα γυρίσουν μία ώρα πίσω"),
  Q("Ποια ρολόγια πρέπει να ρυθμίσουμε μόνοι μας;", ["Τα κινητά", "Του τοίχου, του φούρνου και του αυτοκινήτου", "Τους υπολογιστές", "Κανένα"], 1, "τα ρολόγια του τοίχου, του φούρνου και του αυτοκινήτου"),
  Q("Τι συμβουλεύουν οι γιατροί τους γονείς;", ["Να μη βάζουν τα παιδιά νωρίς για ύπνο", "Να μεταθέτουν σταδιακά την ώρα του ύπνου", "Να ξυπνούν τα παιδιά μία ώρα νωρίτερα", "Να δίνουν βιταμίνες"], 1, "να μεταθέτουν σταδιακά την ώρα του ύπνου"),
 ],
 "gloss": {"ακροατές": "ακροατής — listener", "ξημερώματα": "ξημερώματα — early hours", "θερινή ώρα": "θερινή ώρα — summer time", "δείκτες": "δείκτης — (clock) hand", "αυτόματα": "αυτόματα — automatically", "να ρυθμίσετε": "ρυθμίζω — to set, adjust", "αναχώρησης": "αναχώρηση — departure", "να μεταθέτουν": "μεταθέτω — to shift, move", "σταδιακά": "σταδιακά — gradually", "οργανισμός": "οργανισμός — body, organism", "να προσαρμοστεί": "προσαρμόζομαι — to adjust, adapt"},
})

ITEMS.append({
 "id": "l28-vm-frontistirio", "title": "Μήνυμα από το φροντιστήριο", "title_en": "A message from the language school", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από το φροντιστήριο ξένων γλωσσών του γιου σας.",
 "script": [
  L("Γραμματέας", "f", "Καλησπέρα σας, από το φροντιστήριο ξένων γλωσσών «Πολύγλωσσο» σας καλούμε για τον Ορέστη. Η καθηγήτριά του μάς είπε ότι τις τελευταίες εβδομάδες έχει απουσιάσει τρεις φορές από το μάθημα της Τρίτης, χωρίς να μας έχει ειδοποιήσει κανείς.", "Good evening, we're calling from the «Polyglosso» language school about Orestis. His teacher told us that in recent weeks he has missed the Tuesday lesson three times, without anyone letting us know."),
  L("Γραμματέας", "f", "Δεν θέλουμε να σας ανησυχήσουμε, αλλά οι εξετάσεις για το πτυχίο αγγλικών είναι τον Μάιο, και το μάθημα της Τρίτης είναι αυτό στο οποίο κάνουμε προφορική εξάσκηση. Αν υπάρχει κάποιο πρόβλημα με την ώρα, θα μπορούσαμε να τον μεταφέρουμε στο τμήμα της Πέμπτης, που έχει ακόμη δύο κενές θέσεις.", "We don't want to worry you, but the exams for the English certificate are in May, and the Tuesday lesson is the one in which we do speaking practice. If there's a problem with the time, we could move him to the Thursday group, which still has two free places."),
  L("Γραμματέας", "f", "Σας υπενθυμίζουμε επίσης ότι η προθεσμία για την εγγραφή στις εξετάσεις λήγει στις δεκαπέντε του μήνα. Μπορείτε να μας καλέσετε στο γραφείο, καθημερινά από τις τέσσερις έως τις εννιά το βράδυ.", "We'd also like to remind you that the deadline for registering for the exams is the fifteenth of the month. You can call us at the office, on weekdays from four to nine in the evening."),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί η γραμματέας;", ["Γιατί δεν έχουν πληρωθεί τα δίδακτρα", "Γιατί ο Ορέστης έχει απουσιάσει τρεις φορές χωρίς ειδοποίηση", "Γιατί άλλαξε η καθηγήτρια", "Γιατί ο Ορέστης κόπηκε στις εξετάσεις"], 1, "έχει απουσιάσει τρεις φορές από το μάθημα της Τρίτης, χωρίς να μας έχει ειδοποιήσει κανείς"),
  Q("Γιατί είναι σημαντικό το μάθημα της Τρίτης;", ["Γιατί γράφουν διαγωνίσματα", "Γιατί κάνουν προφορική εξάσκηση", "Γιατί είναι το μόνο μάθημα της εβδομάδας", "Γιατί είναι δωρεάν"], 1, "είναι αυτό στο οποίο κάνουμε προφορική εξάσκηση"),
  Q("Τι προτείνει το φροντιστήριο αν υπάρχει πρόβλημα με την ώρα;", ["Ιδιαίτερα μαθήματα", "Να μεταφερθεί ο Ορέστης στο τμήμα της Πέμπτης", "Να αναβάλει τις εξετάσεις", "Να κάνει μάθημα από το διαδίκτυο"], 1, "θα μπορούσαμε να τον μεταφέρουμε στο τμήμα της Πέμπτης"),
 ],
 "gloss": {"φροντιστήριο": "φροντιστήριο — private tutoring school, crammer", "έχει απουσιάσει": "απουσιάζω — to be absent", "να μας έχει ειδοποιήσει": "ειδοποιώ — to notify, let know", "να σας ανησυχήσουμε": "ανησυχώ — to worry", "πτυχίο": "πτυχίο — certificate, degree", "προφορική": "προφορικός — oral, spoken", "εξάσκηση": "εξάσκηση — practice", "κενές": "κενός — empty, free", "προθεσμία": "προθεσμία — deadline", "λήγει": "λήγω — to expire, end"},
})

ITEMS.append({
 "id": "l28-dia-taxidiotiko", "title": "Στο ταξιδιωτικό γραφείο", "title_en": "At the travel agency", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα ταξιδιωτικό γραφείο.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Θέλουμε να πάμε με τη γυναίκα μου μια εκδρομή για την επέτειό μας, τον Μάρτιο, κάπου στην Ευρώπη. Κάτι ρομαντικό, όχι πολύ ακριβό, και όχι με πολύ κόσμο.", "Good morning. My wife and I want to go on a trip for our anniversary, in March, somewhere in Europe. Something romantic, not too expensive, and not too crowded."),
  L("Υπάλληλος", "f", "Ο Μάρτιος είναι καλή εποχή, γιατί οι τιμές είναι χαμηλότερες πριν από το Πάσχα. Θα σας πρότεινα το Πόρτο, στην Πορτογαλία. Υπάρχει απευθείας πτήση από την Αθήνα δύο φορές την εβδομάδα, και ένα πακέτο τεσσάρων νυχτών σε ξενοδοχείο κοντά στο ποτάμι κοστίζει γύρω στα πεντακόσια πενήντα ευρώ το άτομο.", "March is a good time, because prices are lower before Easter. I'd suggest Porto, in Portugal. There's a direct flight from Athens twice a week, and a four-night package in a hotel near the river costs about five hundred and fifty euros per person."),
  L("Πελάτης", "m", "Ακούγεται ωραίο. Περιλαμβάνεται πρωινό; Και τι γίνεται αν χρειαστεί να ακυρώσουμε;", "Sounds lovely. Is breakfast included? And what happens if we need to cancel?"),
  L("Υπάλληλος", "f", "Το πρωινό περιλαμβάνεται. Για την ακύρωση, αν ειδοποιήσετε μέχρι τριάντα μέρες πριν, παίρνετε πίσω όλο το ποσό εκτός από την πτήση. Μετά από αυτό, η επιστροφή είναι μόνο πενήντα τοις εκατό. Γι' αυτό σας συνιστώ να βγάλετε και μια ταξιδιωτική ασφάλεια· κοστίζει μόνο τριάντα ευρώ και καλύπτει την ακύρωση για λόγους υγείας.", "Breakfast is included. As for cancellation, if you let us know up to thirty days before, you get the whole amount back except for the flight. After that, the refund is only fifty per cent. That's why I'd recommend you also take out travel insurance; it costs only thirty euros and covers cancellation for health reasons."),
  L("Πελάτης", "m", "Εντάξει, θα το συζητήσω με τη γυναίκα μου, γιατί θέλω να είναι έκπληξη μόνο ο προορισμός, όχι το κόστος!", "All right, I'll talk it over with my wife, because I want only the destination to be a surprise, not the cost!"),
 ],
 "questions": [
  Q("Γιατί ο Μάρτιος είναι καλή εποχή για ταξίδι;", ["Γιατί κάνει ζέστη", "Γιατί οι τιμές είναι χαμηλότερες πριν από το Πάσχα", "Γιατί υπάρχουν φεστιβάλ", "Γιατί είναι διακοπές"], 1, "οι τιμές είναι χαμηλότερες πριν από το Πάσχα"),
  Q("Τι ισχύει αν ακυρώσουν μέχρι τριάντα μέρες πριν;", ["Δεν παίρνουν τίποτα πίσω", "Παίρνουν πίσω όλο το ποσό εκτός από την πτήση", "Παίρνουν πίσω το πενήντα τοις εκατό", "Πληρώνουν πρόστιμο"], 1, "παίρνετε πίσω όλο το ποσό εκτός από την πτήση"),
  Q("Τι θέλει να είναι έκπληξη για τη γυναίκα του ο πελάτης;", ["Το κόστος", "Μόνο ο προορισμός", "Η ημερομηνία", "Το ξενοδοχείο"], 1, "θέλω να είναι έκπληξη μόνο ο προορισμός, όχι το κόστος"),
 ],
 "gloss": {"ταξιδιωτικό γραφείο": "ταξιδιωτικό γραφείο — travel agency", "επέτειό": "επέτειος — anniversary", "απευθείας": "απευθείας — direct", "πακέτο": "πακέτο — package", "Περιλαμβάνεται": "περιλαμβάνομαι — to be included", "να ακυρώσουμε": "ακυρώνω — to cancel", "ποσό": "ποσό — amount", "επιστροφή": "επιστροφή — refund, return", "ασφάλεια": "ασφάλεια — insurance", "καλύπτει": "καλύπτω — to cover", "προορισμός": "προορισμός — destination"},
})

ITEMS.append({
 "id": "l28-dia-dypa", "title": "Στο γραφείο απασχόλησης", "title_en": "At the employment office", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα γραφείο της Δημόσιας Υπηρεσίας Απασχόλησης.",
 "script": [
  L("Πολίτισσα", "f", "Καλημέρα. Έχασα τη δουλειά μου πριν από δύο εβδομάδες, γιατί έκλεισε η εταιρεία όπου δούλευα. Θα ήθελα να κάνω αίτηση για επίδομα ανεργίας.", "Good morning. I lost my job two weeks ago, because the company I worked for closed. I'd like to apply for unemployment benefit."),
  L("Υπάλληλος", "m", "Λυπάμαι πολύ. Πρώτα πρέπει να εγγραφείτε στο μητρώο ανέργων· αυτό μπορείτε να το κάνετε και ηλεκτρονικά, με τους κωδικούς σας. Για το επίδομα χρειάζεται να έχετε δουλέψει έναν ελάχιστο αριθμό ημερών τα τελευταία δύο χρόνια. Πόσο καιρό δουλεύατε εκεί;", "I'm very sorry. First you have to register on the list of the unemployed; you can also do that online, with your passwords. For the benefit you need to have worked a minimum number of days in the last two years. How long did you work there?"),
  L("Πολίτισσα", "f", "Πέντε χρόνια, με πλήρη απασχόληση.", "Five years, full time."),
  L("Υπάλληλος", "m", "Τότε δεν θα έχετε πρόβλημα. Η αίτηση πρέπει να γίνει μέσα σε εξήντα μέρες από την απόλυση, οπότε είστε μέσα στην προθεσμία. Επίσης, ως εγγεγραμμένη άνεργη, έχετε δικαίωμα σε δωρεάν προγράμματα κατάρτισης. Αυτή την περίοδο έχουμε σεμινάρια ψηφιακών δεξιοτήτων και λογιστικής.", "Then you won't have a problem. The application must be made within sixty days of the dismissal, so you're within the deadline. Also, as a registered unemployed person, you're entitled to free training programmes. At the moment we have seminars in digital skills and accounting."),
  L("Πολίτισσα", "f", "Η λογιστική με ενδιαφέρει πολύ. Ίσως είναι η ευκαιρία να αλλάξω επάγγελμα.", "Accounting interests me a lot. Maybe this is the chance to change profession."),
 ],
 "questions": [
  Q("Γιατί έχασε τη δουλειά της η γυναίκα;", ["Γιατί παραιτήθηκε", "Γιατί έκλεισε η εταιρεία", "Γιατί μετακόμισε", "Γιατί έληξε η σύμβασή της"], 1, "γιατί έκλεισε η εταιρεία όπου δούλευα"),
  Q("Μέσα σε πόσες μέρες πρέπει να γίνει η αίτηση;", ["Τριάντα", "Εξήντα", "Δεκαπέντε", "Ενενήντα"], 1, "Η αίτηση πρέπει να γίνει μέσα σε εξήντα μέρες από την απόλυση"),
  Q("Τι άλλο δικαιούται ως εγγεγραμμένη άνεργη;", ["Δωρεάν μετακινήσεις", "Δωρεάν προγράμματα κατάρτισης", "Έκπτωση στο ρεύμα", "Δάνειο χωρίς τόκο"], 1, "έχετε δικαίωμα σε δωρεάν προγράμματα κατάρτισης"),
 ],
 "gloss": {"Απασχόλησης": "απασχόληση — employment", "επίδομα ανεργίας": "επίδομα ανεργίας — unemployment benefit", "να εγγραφείτε": "εγγράφομαι — to register", "μητρώο ανέργων": "μητρώο ανέργων — unemployment register", "ελάχιστο": "ελάχιστος — minimum", "πλήρη απασχόληση": "πλήρης απασχόληση — full-time work", "απόλυση": "απόλυση — dismissal", "προθεσμία": "προθεσμία — deadline", "κατάρτισης": "κατάρτιση — (vocational) training", "δεξιοτήτων": "δεξιότητα — skill", "επάγγελμα": "επάγγελμα — profession"},
})

ITEMS.append({
 "id": "l28-mon-diavitis", "title": "Ζώντας με διαβήτη", "title_en": "Living with diabetes", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν νέο άντρα να μιλά για τη ζωή του με διαβήτη τύπου 1.",
 "script": [
  L("Άντρας", "m", "Ήμουν δεκατεσσάρων χρονών όταν μου είπαν ότι έχω διαβήτη τύπου 1. Είχα χάσει πολλά κιλά, διψούσα συνέχεια και ήμουν πάντα κουρασμένος. Όταν ο γιατρός μού εξήγησε ότι θα χρειάζομαι ινσουλίνη για όλη μου τη ζωή, νόμιζα ότι ο κόσμος μου τελείωσε.", "I was fourteen when they told me I had type 1 diabetes. I'd lost a lot of weight, I was always thirsty and always tired. When the doctor explained that I'd need insulin for the rest of my life, I thought my world had ended."),
  L("Άντρας", "m", "Τα πρώτα χρόνια ήταν δύσκολα. Έπρεπε να μετράω το σάκχαρό μου πολλές φορές τη μέρα, να υπολογίζω τους υδατάνθρακες σε κάθε γεύμα και να κάνω ενέσεις. Ντρεπόμουν να το κάνω μπροστά στους φίλους μου, γι' αυτό κρυβόμουν στις τουαλέτες του σχολείου.", "The first years were hard. I had to measure my blood sugar several times a day, count the carbohydrates in every meal and give myself injections. I was embarrassed to do it in front of my friends, so I hid in the school toilets."),
  L("Άντρας", "m", "Σήμερα, χάρη στην τεχνολογία, η ζωή μου είναι πολύ πιο εύκολη. Φοράω έναν αισθητήρα στο μπράτσο που μετράει το σάκχαρο συνεχώς και στέλνει τις τιμές στο κινητό μου, και μια μικρή αντλία ινσουλίνης. Παίζω μπάσκετ, ταξιδεύω, πέρσι ανέβηκα και στον Όλυμπο.", "Today, thanks to technology, my life is much easier. I wear a sensor on my arm that measures my blood sugar continuously and sends the readings to my phone, and a small insulin pump. I play basketball, I travel, last year I even climbed Olympus."),
  L("Άντρας", "m", "Αυτό που θέλω να πω στα παιδιά που μόλις έμαθαν ότι έχουν διαβήτη είναι ότι δεν φταίνε σε τίποτα. Ο τύπος 1 δεν οφείλεται στα γλυκά ούτε στον τρόπο ζωής. Και δεν χρειάζεται να κρύβονται.", "What I want to tell children who have just found out they have diabetes is that it's not their fault at all. Type 1 isn't caused by sweets or by lifestyle. And they don't need to hide."),
 ],
 "questions": [
  Q("Ποια συμπτώματα είχε πριν από τη διάγνωση;", ["Πονοκέφαλο και πυρετό", "Είχε χάσει κιλά, διψούσε και ήταν κουρασμένος", "Δεν είχε κανένα σύμπτωμα", "Πονούσε το στομάχι του"], 1, "Είχα χάσει πολλά κιλά, διψούσα συνέχεια και ήμουν πάντα κουρασμένος"),
  Q("Γιατί κρυβόταν στις τουαλέτες του σχολείου;", ["Για να αποφύγει ένα μάθημα", "Γιατί ντρεπόταν να κάνει ενέσεις μπροστά στους φίλους του", "Γιατί ένιωθε άρρωστος", "Γιατί τον κορόιδευαν"], 1, "Ντρεπόμουν να το κάνω μπροστά στους φίλους μου"),
  Q("Τι θέλει να πει στα παιδιά με διαβήτη;", ["Να μην τρώνε ποτέ γλυκά", "Ότι δεν φταίνε και δεν χρειάζεται να κρύβονται", "Να σταματήσουν τον αθλητισμό", "Ότι ο διαβήτης θεραπεύεται"], 1, "δεν φταίνε σε τίποτα"),
 ],
 "gloss": {"διαβήτη": "διαβήτης — diabetes", "ινσουλίνη": "ινσουλίνη — insulin", "σάκχαρό": "σάκχαρο — blood sugar", "υδατάνθρακες": "υδατάνθρακας — carbohydrate", "ενέσεις": "ένεση — injection", "Ντρεπόμουν": "ντρέπομαι — to be embarrassed, ashamed", "αισθητήρα": "αισθητήρας — sensor", "μπράτσο": "μπράτσο — upper arm", "αντλία": "αντλία — pump", "φταίνε": "φταίω — to be to blame", "οφείλεται": "οφείλομαι — to be due to"},
})

ITEMS.append({
 "id": "l28-rep-kefalonia", "title": "Η λίμνη της Μελισσάνης", "title_en": "Melissani Lake", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από την Κεφαλονιά.",
 "script": [
  L("Δημοσιογράφος", "m", "Είναι μεσημέρι, και η βάρκα μας γλιστράει σε μια λίμνη μέσα σε ένα σπήλαιο. Πάνω από τα κεφάλια μας, η οροφή του σπηλαίου έχει καταρρεύσει, και από το άνοιγμα πέφτει μια δέσμη φωτός που κάνει το νερό να λάμπει σε απίστευτες αποχρώσεις του γαλάζιου. Βρισκόμαστε στη λίμνη της Μελισσάνης, στην Κεφαλονιά.", "It's midday, and our boat is gliding on a lake inside a cave. Above our heads, the cave roof has collapsed, and through the opening falls a beam of light that makes the water glow in incredible shades of blue. We're at Melissani Lake, in Kefalonia."),
  L("Δημοσιογράφος", "m", "Το νερό της λίμνης είναι ένα μείγμα γλυκού και θαλασσινού νερού. Σύμφωνα με τους γεωλόγους, το θαλασσινό νερό μπαίνει σε υπόγειες σχισμές στην άλλη πλευρά του νησιού και ταξιδεύει κάτω από τη γη για αρκετές μέρες μέχρι να φτάσει εδώ. Στην αρχαιότητα, το σπήλαιο ήταν αφιερωμένο στον θεό Πάνα και στις νύμφες.", "The lake water is a mix of fresh and sea water. According to geologists, sea water enters underground cracks on the other side of the island and travels under the earth for several days before arriving here. In antiquity, the cave was dedicated to the god Pan and the nymphs."),
  L("Δημοσιογράφος", "m", "Η Κεφαλονιά είναι ένα νησί με πολλές πληγές. Ο μεγάλος σεισμός του 1953 κατέστρεψε σχεδόν όλα τα χωριά της, και χιλιάδες κάτοικοι μετανάστευσαν. Σήμερα όμως ο τουρισμός έχει δώσει νέα ζωή στο νησί. «Το καλύτερο είναι να έρθετε τον Μάιο ή τον Σεπτέμβριο», μας λέει ο βαρκάρης. «Τον Αύγουστο, η ουρά για τη βάρκα είναι μεγαλύτερη από τη λίμνη!»", "Kefalonia is an island with many wounds. The great earthquake of 1953 destroyed almost all its villages, and thousands of inhabitants emigrated. Today, though, tourism has given the island new life. «The best thing is to come in May or September», the boatman tells us. «In August, the queue for the boat is longer than the lake!»"),
 ],
 "questions": [
  Q("Γιατί το νερό λάμπει το μεσημέρι;", ["Γιατί υπάρχουν φώτα μέσα στο σπήλαιο", "Γιατί πέφτει φως από το άνοιγμα της οροφής", "Γιατί το νερό είναι ζεστό", "Γιατί έχει μέσα φύκια"], 1, "από το άνοιγμα πέφτει μια δέσμη φωτός"),
  Q("Από πού έρχεται το θαλασσινό νερό της λίμνης;", ["Από ένα ποτάμι", "Από υπόγειες σχισμές στην άλλη πλευρά του νησιού", "Από τη βροχή", "Από ένα κοντινό λιμάνι"], 1, "το θαλασσινό νερό μπαίνει σε υπόγειες σχισμές στην άλλη πλευρά του νησιού"),
  Q("Τι εννοεί ο βαρκάρης για τον Αύγουστο;", ["Ότι η λίμνη μεγαλώνει", "Ότι υπάρχει πάρα πολύς κόσμος", "Ότι οι βάρκες δεν λειτουργούν", "Ότι κάνει πολλή ζέστη"], 1, "η ουρά για τη βάρκα είναι μεγαλύτερη από τη λίμνη"),
 ],
 "gloss": {"γλιστράει": "γλιστράω — to glide, slip", "σπήλαιο": "σπήλαιο — cave", "οροφή": "οροφή — roof, ceiling", "έχει καταρρεύσει": "καταρρέω — to collapse", "δέσμη": "δέσμη — beam, bundle", "αποχρώσεις": "απόχρωση — shade, hue", "μείγμα": "μείγμα — mixture", "σχισμές": "σχισμή — crack, fissure", "αφιερωμένο": "αφιερωμένος — dedicated", "πληγές": "πληγή — wound", "μετανάστευσαν": "μεταναστεύω — to emigrate", "βαρκάρης": "βαρκάρης — boatman"},
})

ITEMS.append({
 "id": "l28-rep-nymfaio", "title": "Το Νυμφαίο και οι αρκούδες", "title_en": "Nymfaio and the bears", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από το Νυμφαίο, ένα ορεινό χωριό της Φλώρινας.",
 "script": [
  L("Δημοσιογράφος", "f", "Στα χίλια τριακόσια περίπου μέτρα, ανάμεσα σε δάση από οξιές, βρίσκεται το Νυμφαίο, ένα από τα πιο όμορφα πέτρινα χωριά της Μακεδονίας. Τον δέκατο ένατο αιώνα οι κάτοικοί του, πολλοί από τους οποίους ήταν έμποροι και ασημουργοί, έχτισαν εδώ επιβλητικά αρχοντικά με τα κέρδη που έφερναν από τα ταξίδια τους.", "At around one thousand three hundred metres, among beech forests, lies Nymfaio, one of the most beautiful stone villages of Macedonia. In the nineteenth century its inhabitants, many of whom were merchants and silversmiths, built imposing mansions here with the profits they brought back from their travels."),
  L("Δημοσιογράφος", "f", "Λίγο έξω από το χωριό λειτουργεί από τη δεκαετία του '90 ένα καταφύγιο για καφέ αρκούδες. Εδώ ζουν ζώα που κάποτε οι αρκουδιάρηδες έσερναν στις πλατείες και τα πανηγύρια, για να χορεύουν με αλυσίδα στη μύτη, μια πρακτική που σήμερα απαγορεύεται. Επειδή έχουν ζήσει όλη τους τη ζωή σε αιχμαλωσία, δεν μπορούν να επιστρέψουν στο δάσος.", "Just outside the village, a sanctuary for brown bears has operated since the 1990s. Here live animals that bear-leaders once dragged around squares and village festivals to dance with a chain through their nose, a practice that is now banned. Because they've spent their whole lives in captivity, they can't return to the forest."),
  L("Δημοσιογράφος", "f", "Οι επισκέπτες μπορούν να δουν τις αρκούδες από απόσταση, σε μεγάλους φυσικούς χώρους με δέντρα και πισίνες. «Το πιο συγκινητικό», μου λέει μια εθελόντρια, «είναι όταν μια αρκούδα που έχει ζήσει χρόνια σε κλουβί σκάβει για πρώτη φορά το χώμα ή πέφτει στο νερό. Τότε καταλαβαίνεις γιατί αξίζει όλη αυτή η προσπάθεια.»", "Visitors can see the bears from a distance, in large natural enclosures with trees and pools. «The most moving thing», a volunteer tells me, «is when a bear that has lived for years in a cage digs in the earth or jumps into the water for the first time. Then you understand why all this effort is worth it.»"),
 ],
 "questions": [
  Q("Με τι χρήματα χτίστηκαν τα αρχοντικά του Νυμφαίου;", ["Με κρατικά χρήματα", "Με τα κέρδη εμπόρων και ασημουργών από τα ταξίδια τους", "Με δωρεές τουριστών", "Με τα έσοδα του καταφυγίου"], 1, "με τα κέρδη που έφερναν από τα ταξίδια τους"),
  Q("Γιατί οι αρκούδες του καταφυγίου δεν μπορούν να επιστρέψουν στο δάσος;", ["Γιατί είναι πολύ μεγάλες", "Γιατί έχουν ζήσει όλη τους τη ζωή σε αιχμαλωσία", "Γιατί το δάσος κάηκε", "Γιατί απαγορεύεται από τον νόμο"], 1, "Επειδή έχουν ζήσει όλη τους τη ζωή σε αιχμαλωσία"),
  Q("Τι συγκινεί περισσότερο την εθελόντρια;", ["Οι επισκέπτες", "Όταν μια αρκούδα σκάβει το χώμα ή πέφτει στο νερό για πρώτη φορά", "Τα αρχοντικά του χωριού", "Οι δωρεές"], 1, "όταν μια αρκούδα που έχει ζήσει χρόνια σε κλουβί σκάβει για πρώτη φορά το χώμα"),
 ],
 "gloss": {"οξιές": "οξιά — beech tree", "πέτρινα": "πέτρινος — stone (adj.)", "ασημουργοί": "ασημουργός — silversmith", "αρχοντικά": "αρχοντικό — mansion", "κέρδη": "κέρδος — profit", "καταφύγιο": "καταφύγιο — sanctuary, refuge", "αρκουδιάρηδες": "αρκουδιάρης — bear-leader (who made bears dance)", "έσερναν": "σέρνω — to drag", "αλυσίδα": "αλυσίδα — chain", "αιχμαλωσία": "αιχμαλωσία — captivity", "συγκινητικό": "συγκινητικός — moving, touching", "σκάβει": "σκάβω — to dig"},
})

ITEMS.append({
 "id": "l28-int-enalia", "title": "Μια ενάλια αρχαιολόγος", "title_en": "An underwater archaeologist", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια ενάλια αρχαιολόγο.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς είναι μια μέρα δουλειάς στον βυθό;", "What's a working day on the seabed like?"),
  L("Αρχαιολόγος", "f", "Πολύ λιγότερο ρομαντική απ' ό,τι φαντάζεστε! Σε ένα ναυάγιο στα σαράντα μέτρα, μπορούμε να μείνουμε κάτω μόνο είκοσι με τριάντα λεπτά, λόγω της πίεσης. Γι' αυτό κάθε κατάδυση σχεδιάζεται στη λεπτομέρεια: ποιος θα φωτογραφίσει, ποιος θα μετρήσει, ποιος θα ανεβάσει ένα αντικείμενο. Τις υπόλοιπες ώρες τις περνάμε στο σκάφος, καταγράφοντας και συζητώντας.", "Much less romantic than you imagine! At a wreck forty metres down, we can only stay below for twenty to thirty minutes, because of the pressure. That's why every dive is planned in detail: who will photograph, who will measure, who will bring up an object. We spend the rest of the hours on the boat, recording and discussing."),
  L("Δημοσιογράφος", "m", "Τι βρίσκετε συνήθως σε ένα αρχαίο ναυάγιο;", "What do you usually find in an ancient wreck?"),
  L("Αρχαιολόγος", "f", "Κυρίως αμφορείς, τα δοχεία με τα οποία μετέφεραν κρασί και λάδι. Μπορεί να ακούγεται βαρετό, αλλά από το σχήμα τους καταλαβαίνουμε από πού ξεκίνησε το πλοίο και προς τα πού πήγαινε. Κάθε ναυάγιο είναι σαν μια φωτογραφία του εμπορίου μιας εποχής, παγωμένη τη στιγμή που βυθίστηκε.", "Mainly amphorae, the containers in which they transported wine and oil. It may sound boring, but from their shape we can tell where the ship set out from and where it was going. Every wreck is like a photograph of the trade of an era, frozen at the moment it sank."),
  L("Δημοσιογράφος", "m", "Ποιος είναι ο μεγαλύτερος κίνδυνος για τα ναυάγια σήμερα;", "What's the biggest threat to wrecks today?"),
  L("Αρχαιολόγος", "f", "Οι αρχαιοκάπηλοι και οι δύτες που παίρνουν «ένα σουβενίρ». Ένας αμφορέας έξω από τη θέση του χάνει το μεγαλύτερο μέρος της επιστημονικής του αξίας. Γι' αυτό ζητάμε από όποιον βρει κάτι στον βυθό να μην το αγγίξει και να ειδοποιήσει τις αρχές.", "Looters and divers who take «a souvenir». An amphora removed from its position loses most of its scientific value. That's why we ask anyone who finds something on the seabed not to touch it and to notify the authorities."),
 ],
 "questions": [
  Q("Γιατί κάθε κατάδυση σχεδιάζεται στη λεπτομέρεια;", ["Γιατί το νερό είναι κρύο", "Γιατί μπορούν να μείνουν στον βυθό μόνο λίγα λεπτά", "Γιατί οι δύτες είναι λίγοι", "Γιατί απαγορεύεται από τον νόμο"], 1, "μπορούμε να μείνουμε κάτω μόνο είκοσι με τριάντα λεπτά"),
  Q("Τι μαθαίνουν οι αρχαιολόγοι από το σχήμα των αμφορέων;", ["Την ηλικία του καπετάνιου", "Από πού ξεκίνησε το πλοίο και πού πήγαινε", "Πόσοι ήταν οι ναύτες", "Γιατί βυθίστηκε το πλοίο"], 1, "από το σχήμα τους καταλαβαίνουμε από πού ξεκίνησε το πλοίο και προς τα πού πήγαινε"),
  Q("Τι ζητούν από όποιον βρει κάτι στον βυθό;", ["Να το φέρει στο μουσείο", "Να μην το αγγίξει και να ειδοποιήσει τις αρχές", "Να το φωτογραφίσει και να το πάρει", "Να το πουλήσει σε συλλέκτη"], 1, "να μην το αγγίξει και να ειδοποιήσει τις αρχές"),
 ],
 "gloss": {"ενάλια": "ενάλιος — marine, underwater", "βυθό": "βυθός — seabed", "ναυάγιο": "ναυάγιο — wreck", "πίεσης": "πίεση — pressure", "κατάδυση": "κατάδυση — dive", "αμφορείς": "αμφορέας — amphora", "δοχεία": "δοχείο — container", "εμπορίου": "εμπόριο — trade", "βυθίστηκε": "βυθίζομαι — to sink", "αρχαιοκάπηλοι": "αρχαιοκάπηλος — looter of antiquities", "δύτες": "δύτης — diver"},
})

ITEMS.append({
 "id": "l28-mon-loimos", "title": "Ο λοιμός της Αθήνας", "title_en": "The plague of Athens", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη για τον λοιμό της Αθήνας, όπως τον περιγράφει ο Θουκυδίδης.",
 "script": [
  L("Ιστορικός", "m", "Το καλοκαίρι του 430 π.Χ., στον δεύτερο χρόνο του Πελοποννησιακού Πολέμου, μια φοβερή επιδημία ξέσπασε στην Αθήνα. Η πόλη ήταν τότε υπερπλήρης: ο Περικλής είχε πείσει τους κατοίκους της υπαίθρου να καταφύγουν πίσω από τα τείχη, και χιλιάδες άνθρωποι ζούσαν στοιβαγμένοι σε πρόχειρα καταλύματα, με το καλοκαίρι στο αποκορύφωμά του.", "In the summer of 430 BC, in the second year of the Peloponnesian War, a terrible epidemic broke out in Athens. The city was overcrowded at the time: Pericles had persuaded the people of the countryside to take refuge behind the walls, and thousands of people were living crammed into makeshift shelters, at the height of summer."),
  L("Ιστορικός", "m", "Η πιο πολύτιμη πηγή μας είναι ο Θουκυδίδης, ο οποίος όχι μόνο έζησε την επιδημία, αλλά αρρώστησε και ο ίδιος και επέζησε. Περιγράφει τα συμπτώματα με μια σχεδόν ιατρική ακρίβεια, δηλώνοντας ότι το κάνει ώστε, αν η αρρώστια ξαναεμφανιστεί, να μπορεί κανείς να την αναγνωρίσει. Ποια ακριβώς ήταν η νόσος παραμένει αντικείμενο συζήτησης: έχουν προταθεί, μεταξύ άλλων, ο τύφος και ο τυφοειδής πυρετός.", "Our most valuable source is Thucydides, who not only lived through the epidemic but also fell ill himself and survived. He describes the symptoms with almost medical precision, stating that he does so in order that, if the disease reappears, one might be able to recognise it. Exactly what the disease was remains a matter of debate: typhus and typhoid fever, among others, have been proposed."),
  L("Ιστορικός", "m", "Αυτό όμως που κάνει την αφήγησή του συγκλονιστική δεν είναι τα συμπτώματα, αλλά η περιγραφή της κοινωνικής κατάρρευσης. Οι άνθρωποι, γράφει, βλέποντας ότι ευσεβείς και ασεβείς πέθαιναν το ίδιο, έπαψαν να φοβούνται τους θεούς και τους νόμους. Οι νεκροί έμεναν άταφοι, και ο καθένας ζούσε για τη στιγμή, αφού δεν ήξερε αν θα ζει αύριο.", "But what makes his account so shattering is not the symptoms but the description of social collapse. People, he writes, seeing that the pious and the impious died alike, stopped fearing the gods and the laws. The dead were left unburied, and everyone lived for the moment, since they didn't know if they would be alive tomorrow."),
  L("Ιστορικός", "m", "Ανάμεσα στα θύματα ήταν και ο ίδιος ο Περικλής, το 429. Η απώλειά του στέρησε από την Αθήνα τον πιο ικανό της ηγέτη στη χειρότερη δυνατή στιγμή. Γι' αυτό πολλοί ιστορικοί θεωρούν ότι ο λοιμός επηρέασε την έκβαση του πολέμου περισσότερο από οποιαδήποτε μάχη.", "Among the victims was Pericles himself, in 429. His loss deprived Athens of its most capable leader at the worst possible moment. That is why many historians believe the plague affected the outcome of the war more than any battle."),
 ],
 "questions": [
  Q("Γιατί η Αθήνα ήταν υπερπλήρης όταν ξέσπασε η επιδημία;", ["Γιατί γινόταν μια μεγάλη γιορτή", "Γιατί οι κάτοικοι της υπαίθρου είχαν καταφύγει πίσω από τα τείχη", "Γιατί είχαν έρθει πρόσφυγες από τη Σπάρτη", "Γιατί είχαν γυρίσει οι στρατιώτες"], 1, "ο Περικλής είχε πείσει τους κατοίκους της υπαίθρου να καταφύγουν πίσω από τα τείχη"),
  Q("Γιατί ο Θουκυδίδης περιγράφει τόσο λεπτομερώς τα συμπτώματα;", ["Για να εντυπωσιάσει τους αναγνώστες", "Για να μπορεί κανείς να αναγνωρίσει την αρρώστια αν ξαναεμφανιστεί", "Γιατί ήταν γιατρός", "Για να κατηγορήσει τον Περικλή"], 1, "ώστε, αν η αρρώστια ξαναεμφανιστεί, να μπορεί κανείς να την αναγνωρίσει"),
  Q("Τι θεωρεί ο ομιλητής το πιο συγκλονιστικό στοιχείο της αφήγησης;", ["Τον αριθμό των νεκρών", "Την περιγραφή της κοινωνικής κατάρρευσης", "Τα ιατρικά συμπτώματα", "Τη στρατηγική του πολέμου"], 1, "η περιγραφή της κοινωνικής κατάρρευσης"),
  Q("Γιατί πολλοί ιστορικοί θεωρούν τον λοιμό καθοριστικό για τον πόλεμο;", ["Γιατί αρρώστησαν και οι Σπαρτιάτες", "Γιατί στέρησε από την Αθήνα τον Περικλή στη χειρότερη στιγμή", "Γιατί σταμάτησε τον πόλεμο για δέκα χρόνια", "Γιατί κάηκε η πόλη"], 1, "Η απώλειά του στέρησε από την Αθήνα τον πιο ικανό της ηγέτη στη χειρότερη δυνατή στιγμή"),
 ],
 "gloss": {"λοιμό": "λοιμός — plague, pestilence", "επιδημία": "επιδημία — epidemic", "ξέσπασε": "ξεσπώ — to break out", "υπερπλήρης": "υπερπλήρης — overcrowded", "υπαίθρου": "ύπαιθρος — countryside", "να καταφύγουν": "καταφεύγω — to take refuge", "στοιβαγμένοι": "στοιβαγμένος — crammed, piled up", "αποκορύφωμά": "αποκορύφωμα — peak, climax", "επέζησε": "επιζώ — to survive", "συγκλονιστική": "συγκλονιστικός — shattering, deeply moving", "ευσεβείς": "ευσεβής — pious", "άταφοι": "άταφος — unburied", "έκβαση": "έκβαση — outcome"},
})

ITEMS.append({
 "id": "l28-int-eftychia", "title": "Μετριέται η ευτυχία;", "title_en": "Can happiness be measured?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια οικονομολόγο για τη μέτρηση της ευημερίας.",
 "script": [
  L("Δημοσιογράφος", "m", "Επί δεκαετίες, η επιτυχία μιας χώρας μετριόταν με το ΑΕΠ. Γιατί αυτό δεν αρκεί πια;", "For decades, a country's success was measured by GDP. Why isn't that enough any more?"),
  L("Οικονομολόγος", "f", "Γιατί το ΑΕΠ μετράει την παραγωγή, όχι την ευημερία. Αν ένας σεισμός καταστρέψει μια πόλη, οι δαπάνες για την ανοικοδόμηση θα αυξήσουν το ΑΕΠ, αλλά κανείς δεν θα πει ότι οι κάτοικοι είναι πιο ευτυχισμένοι. Επιπλέον, το ΑΕΠ αγνοεί πράγματα που μετράνε στη ζωή μας: τον ελεύθερο χρόνο, την υγεία, την ποιότητα των σχέσεων, την καθαρότητα του αέρα.", "Because GDP measures production, not well-being. If an earthquake destroys a city, spending on reconstruction will raise GDP, but nobody will say the inhabitants are happier. Moreover, GDP ignores things that matter in our lives: free time, health, the quality of our relationships, how clean the air is."),
  L("Δημοσιογράφος", "m", "Πώς όμως μετράς κάτι τόσο υποκειμενικό όσο η ευτυχία;", "But how do you measure something as subjective as happiness?"),
  L("Οικονομολόγος", "f", "Κυρίως με έρευνες, όπου ρωτάμε τους ανθρώπους πόσο ικανοποιημένοι είναι από τη ζωή τους, σε μια κλίμακα από το μηδέν ως το δέκα. Ακούγεται απλοϊκό, αλλά οι απαντήσεις αποδεικνύονται εκπληκτικά σταθερές και συνδέονται με μετρήσιμους παράγοντες. Στις διεθνείς κατατάξεις, οι σκανδιναβικές χώρες, και ιδίως η Φινλανδία, βρίσκονται σταθερά στις πρώτες θέσεις, όχι επειδή είναι οι πλουσιότερες, αλλά λόγω της εμπιστοσύνης στους θεσμούς και του ισχυρού κοινωνικού κράτους.", "Mainly with surveys, where we ask people how satisfied they are with their lives, on a scale from zero to ten. It sounds simplistic, but the answers prove remarkably stable and are linked to measurable factors. In the international rankings, the Scandinavian countries, and especially Finland, are consistently at the top, not because they're the richest, but because of trust in institutions and a strong welfare state."),
  L("Οικονομολόγος", "f", "Ένα από τα πιο ενδιαφέροντα ευρήματα είναι ότι, πάνω από ένα ορισμένο επίπεδο εισοδήματος, τα επιπλέον χρήματα προσθέτουν όλο και λιγότερη ικανοποίηση. Αυτό δεν σημαίνει ότι η φτώχεια δεν πονάει· σημαίνει ότι, όταν οι βασικές ανάγκες καλυφθούν, άλλα πράγματα αρχίζουν να μετράνε περισσότερο.", "One of the most interesting findings is that, above a certain level of income, extra money adds less and less satisfaction. That doesn't mean poverty doesn't hurt; it means that, once basic needs are met, other things start to matter more."),
 ],
 "questions": [
  Q("Γιατί, κατά την οικονομολόγο, το ΑΕΠ δεν αρκεί;", ["Γιατί υπολογίζεται λάθος", "Γιατί μετράει την παραγωγή και όχι την ευημερία", "Γιατί δεν περιλαμβάνει τις εξαγωγές", "Γιατί αλλάζει κάθε χρόνο"], 1, "το ΑΕΠ μετράει την παραγωγή, όχι την ευημερία"),
  Q("Τι δείχνει το παράδειγμα του σεισμού;", ["Ότι οι σεισμοί βλάπτουν την οικονομία", "Ότι το ΑΕΠ μπορεί να αυξηθεί χωρίς να αυξηθεί η ευημερία", "Ότι η ανοικοδόμηση είναι ακριβή", "Ότι οι κάτοικοι γίνονται πιο ευτυχισμένοι"], 1, "οι δαπάνες για την ανοικοδόμηση θα αυξήσουν το ΑΕΠ, αλλά κανείς δεν θα πει ότι οι κάτοικοι είναι πιο ευτυχισμένοι"),
  Q("Γιατί οι σκανδιναβικές χώρες βρίσκονται στις πρώτες θέσεις;", ["Γιατί είναι οι πλουσιότερες", "Λόγω της εμπιστοσύνης στους θεσμούς και του ισχυρού κοινωνικού κράτους", "Λόγω του κλίματος", "Γιατί έχουν μικρό πληθυσμό"], 1, "λόγω της εμπιστοσύνης στους θεσμούς και του ισχυρού κοινωνικού κράτους"),
  Q("Τι συμβαίνει πάνω από ένα ορισμένο επίπεδο εισοδήματος;", ["Η ικανοποίηση μειώνεται απότομα", "Τα επιπλέον χρήματα προσθέτουν όλο και λιγότερη ικανοποίηση", "Οι άνθρωποι σταματούν να δουλεύουν", "Η ευτυχία διπλασιάζεται"], 1, "τα επιπλέον χρήματα προσθέτουν όλο και λιγότερη ικανοποίηση"),
 ],
 "gloss": {"οικονομολόγο": "οικονομολόγος — economist", "ευημερίας": "ευημερία — well-being, prosperity", "ΑΕΠ": "ΑΕΠ (ακαθάριστο εγχώριο προϊόν) — GDP", "δαπάνες": "δαπάνη — spending", "ανοικοδόμηση": "ανοικοδόμηση — reconstruction", "υποκειμενικό": "υποκειμενικός — subjective", "ικανοποιημένοι": "ικανοποιημένος — satisfied", "κλίμακα": "κλίμακα — scale", "απλοϊκό": "απλοϊκός — simplistic", "κατατάξεις": "κατάταξη — ranking", "θεσμούς": "θεσμός — institution", "εισοδήματος": "εισόδημα — income"},
})
rnd = random.Random(28)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-28.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
