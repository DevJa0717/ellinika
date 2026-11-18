# Source for library/listening/listening-175.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l175.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l175-ann-vivliopazaro", "title": "Ανακοίνωση στο βιβλιοπαζάρο", "title_en": "An announcement at the book fair", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός υπαίθριου βιβλιοπαζάρου σε μια πλατεία.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί φίλοι του βιβλίου, λόγω των ισχυρών ανέμων που προβλέπονται για απόψε, το βιβλιοπαζάρο θα κλείσει σήμερα στις εννιά αντί για τις έντεκα. Οι εκδότες παρακαλούνται να έχουν σκεπάσει τους πάγκους τους μέχρι τις εννιά και μισή.", "Dear book lovers, because of the strong winds forecast for tonight, the book fair will close today at nine instead of eleven. Publishers are asked to have covered their stalls by half past nine."),
  L("Εκφωνήτρια", "f", "Η παρουσίαση του νέου μυθιστορήματος της Ελένης Δημάκη, που ήταν προγραμματισμένη για τις δέκα, μεταφέρεται στις επτά, στη σκηνή δίπλα στο σιντριβάνι. Μετά την παρουσίαση η συγγραφέας θα υπογράφει βιβλία.", "The presentation of Eleni Dimaki's new novel, which was scheduled for ten, is moved to seven, on the stage next to the fountain. After the presentation the author will sign books."),
  L("Εκφωνήτρια", "f", "Σας υπενθυμίζουμε ότι για κάθε τρία βιβλία που αγοράζετε από τα περίπτερα με την πράσινη σημαία, το τέταρτο σας προσφέρεται δωρεάν. Καλή ανάγνωση!", "We remind you that for every three books you buy from the stands with the green flag, the fourth is offered to you free. Happy reading!"),
 ],
 "questions": [
  Q("Γιατί θα κλείσει νωρίτερα το βιβλιοπαζάρο;", ["Γιατί θα βρέξει", "Γιατί προβλέπονται ισχυροί άνεμοι", "Γιατί θα γίνει συναυλία στην πλατεία", "Γιατί τελείωσαν τα βιβλία"], 1, "λόγω των ισχυρών ανέμων που προβλέπονται για απόψε"),
  Q("Τι αλλάζει στην παρουσίαση του μυθιστορήματος;", ["Ακυρώνεται", "Μεταφέρεται σε άλλη μέρα", "Γίνεται στις επτά αντί για τις δέκα", "Γίνεται μέσα σε ένα βιβλιοπωλείο"], 2, "μεταφέρεται στις επτά"),
  Q("Ποια προσφορά ισχύει στα περίπτερα με την πράσινη σημαία;", ["Με τρία βιβλία, το τέταρτο δωρεάν", "Έκπτωση πενήντα τοις εκατό", "Δωρεάν τσάντα", "Υπογραφή από τη συγγραφέα"], 0, "το τέταρτο σας προσφέρεται δωρεάν"),
 ],
 "gloss": {"υπαίθριου": "υπαίθριος — open-air", "βιβλιοπαζάρου": "βιβλιοπαζάρο — book fair", "ισχυρών ανέμων": "ισχυρός άνεμος — strong wind", "εκδότες": "εκδότης — publisher", "πάγκους": "πάγκος — stall, bench", "παρουσίαση": "παρουσίαση — (book) presentation", "σιντριβάνι": "σιντριβάνι — fountain", "υπογράφει": "υπογράφω — to sign", "υπενθυμίζουμε": "υπενθυμίζω — to remind", "περίπτερα": "περίπτερο — stand, booth"},
})

ITEMS.append({
 "id": "l175-int-metaforeas-epiplon", "title": "Ο μεταφορέας επίπλων", "title_en": "The furniture mover", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν άντρα που δουλεύει εδώ και είκοσι χρόνια σε μεταφορική εταιρεία.",
 "script": [
  L("Δημοσιογράφος", "f", "Ποια είναι η πιο δύσκολη μετακόμιση που έχετε κάνει;", "What is the hardest move you have done?"),
  L("Μεταφορέας", "m", "Ένα πιάνο με ουρά σε πέμπτο όροφο, χωρίς ασανσέρ, σε ένα στενό δρομάκι της Πλάκας. Δεν χωρούσε στη σκάλα, οπότε το ανεβάσαμε από το μπαλκόνι με γερανό. Ο ιδιοκτήτης δεν μπορούσε να κοιτάξει· καθόταν στο καφενείο απέναντι με κλειστά μάτια.", "A grand piano to a fifth floor, with no lift, in a narrow little street in Plaka. It didn't fit on the stairs, so we lifted it up through the balcony with a crane. The owner couldn't watch; he sat in the café opposite with his eyes closed."),
  L("Δημοσιογράφος", "f", "Τι συμβουλή θα δίνατε σε κάποιον που μετακομίζει;", "What advice would you give someone who is moving?"),
  L("Μεταφορέας", "m", "Να γράφει πάνω σε κάθε κούτα σε ποιο δωμάτιο πηγαίνει, όχι απλώς «διάφορα». Και να μη γεμίζει τις μεγάλες κούτες με βιβλία· γίνονται τόσο βαριές που σκίζονται. Τα βιβλία μπαίνουν σε μικρές κούτες, τα μαξιλάρια στις μεγάλες.", "To write on every box which room it's going to, not just 'miscellaneous'. And not to fill the big boxes with books; they get so heavy that they tear. Books go in small boxes, pillows in the big ones."),
  L("Δημοσιογράφος", "f", "Σας έχουν συγκινήσει ποτέ οι πελάτες;", "Have customers ever moved you?"),
  L("Μεταφορέας", "m", "Πολλές φορές. Μια ηλικιωμένη κυρία μετακόμιζε σε γηροκομείο και μπορούσε να πάρει μόνο ένα έπιπλο. Διάλεξε μια παλιά καρέκλα της κουζίνας, γιατί σε αυτήν καθόταν ο άντρας της κάθε πρωί. Τη μεταφέραμε σαν να ήταν από κρύσταλλο.", "Many times. An elderly lady was moving to a care home and could take only one piece of furniture. She chose an old kitchen chair, because her husband used to sit on it every morning. We carried it as if it were made of crystal."),
 ],
 "questions": [
  Q("Πώς ανέβασαν το πιάνο στον πέμπτο όροφο;", ["Από τη σκάλα, σε κομμάτια", "Από το μπαλκόνι με γερανό", "Με το ασανσέρ", "Δεν κατάφεραν να το ανεβάσουν"], 1, "το ανεβάσαμε από το μπαλκόνι με γερανό"),
  Q("Γιατί δεν πρέπει να γεμίζουμε μεγάλες κούτες με βιβλία;", ["Γιατί τα βιβλία χαλάνε", "Γιατί δεν χωράνε στο φορτηγό", "Γιατί γίνονται πολύ βαριές και σκίζονται", "Γιατί είναι ακριβές"], 2, "γίνονται τόσο βαριές που σκίζονται"),
  Q("Γιατί η ηλικιωμένη κυρία διάλεξε την καρέκλα της κουζίνας;", ["Γιατί σε αυτήν καθόταν κάθε πρωί ο άντρας της", "Γιατί ήταν πολύ ακριβή", "Γιατί ήταν η μόνη που χωρούσε", "Γιατί την είχε φτιάξει η ίδια"], 0, "σε αυτήν καθόταν ο άντρας της κάθε πρωί"),
 ],
 "gloss": {"μεταφορική εταιρεία": "μεταφορική εταιρεία — removal company", "μετακόμιση": "μετακόμιση — move (house)", "πιάνο με ουρά": "πιάνο με ουρά — grand piano", "ασανσέρ": "ασανσέρ — lift, elevator", "γερανό": "γερανός — crane", "κούτα": "κούτα — cardboard box", "διάφορα": "διάφορα — miscellaneous", "σκίζονται": "σκίζομαι — to tear", "γηροκομείο": "γηροκομείο — care home", "κρύσταλλο": "κρύσταλλο — crystal (glass)"},
})

ITEMS.append({
 "id": "l175-int-aerosynodos", "title": "Η αεροσυνοδός", "title_en": "The flight attendant", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια αεροσυνοδό που πετάει εδώ και δώδεκα χρόνια.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι περισσότεροι πιστεύουν ότι η δουλειά σας είναι να σερβίρετε καφέ. Ισχύει;", "Most people think your job is to serve coffee. Is that true?"),
  L("Αεροσυνοδός", "f", "Ο καφές είναι το μικρότερο κομμάτι. Είμαστε εκεί κυρίως για την ασφάλεια των επιβατών. Κάθε χρόνο περνάμε εκπαίδευση σε πυρκαγιά, πρώτες βοήθειες και εκκένωση του αεροσκάφους. Πρέπει να μπορούμε να αδειάσουμε ένα γεμάτο αεροπλάνο σε ενενήντα δευτερόλεπτα.", "Coffee is the smallest part. We're there mainly for the passengers' safety. Every year we go through training in fire, first aid and evacuating the aircraft. We have to be able to empty a full plane in ninety seconds."),
  L("Δημοσιογράφος", "m", "Ποιοι επιβάτες είναι οι πιο δύσκολοι;", "Which passengers are the most difficult?"),
  L("Αεροσυνοδός", "f", "Όχι οι θυμωμένοι, αλλά όσοι φοβούνται και δεν το λένε. Τους καταλαβαίνεις από τα χέρια: κρατάνε σφιχτά το μπράτσο του καθίσματος. Τότε κάθομαι δίπλα τους για λίγο και τους εξηγώ τι σημαίνει κάθε θόρυβος. Όταν ξέρεις ότι το «μπαμ» είναι οι ρόδες που ανοίγουν, φοβάσαι λιγότερο.", "Not the angry ones, but those who are afraid and don't say so. You can tell from their hands: they hold the armrest tightly. Then I sit next to them for a while and explain what each noise means. When you know that the 'bang' is the wheels coming down, you're less afraid."),
  L("Δημοσιογράφος", "m", "Τι σας λείπει περισσότερο;", "What do you miss most?"),
  L("Αεροσυνοδός", "f", "Ένα κανονικό πρόγραμμα. Έχω περάσει Χριστούγεννα σε ξενοδοχεία στη Φρανκφούρτη και γενέθλια σε διαδρόμους αεροδρομίων. Αλλά όταν το αεροπλάνο σηκώνεται πάνω από τα σύννεφα και βγαίνει ο ήλιος, ξέρω ότι δεν θα το άλλαζα με τίποτα.", "A normal schedule. I've spent Christmases in hotels in Frankfurt and birthdays in airport corridors. But when the plane rises above the clouds and the sun comes out, I know I wouldn't change it for anything."),
 ],
 "questions": [
  Q("Ποια είναι, κατά την αεροσυνοδό, η κύρια δουλειά της;", ["Να σερβίρει φαγητό και καφέ", "Η ασφάλεια των επιβατών", "Να πουλάει προϊόντα αφορολόγητα", "Να βοηθάει τον πιλότο"], 1, "Είμαστε εκεί κυρίως για την ασφάλεια των επιβατών"),
  Q("Πώς καταλαβαίνει ότι ένας επιβάτης φοβάται;", ["Από τις φωνές του", "Από το ότι ζητάει νερό", "Από το ότι κρατάει σφιχτά το μπράτσο του καθίσματος", "Από το ότι δεν τρώει"], 2, "κρατάνε σφιχτά το μπράτσο του καθίσματος"),
  Q("Τι της λείπει περισσότερο;", ["Ένα κανονικό πρόγραμμα", "Τα ταξίδια", "Οι συνάδελφοί της", "Η Φρανκφούρτη"], 0, "Ένα κανονικό πρόγραμμα"),
 ],
 "gloss": {"αεροσυνοδό": "αεροσυνοδός — flight attendant", "επιβατών": "επιβάτης — passenger", "πυρκαγιά": "πυρκαγιά — fire", "πρώτες βοήθειες": "πρώτες βοήθειες — first aid", "εκκένωση": "εκκένωση — evacuation", "αεροσκάφους": "αεροσκάφος — aircraft", "σφιχτά": "σφιχτά — tightly", "μπράτσο του καθίσματος": "μπράτσο του καθίσματος — armrest", "ρόδες": "ρόδα — wheel", "διαδρόμους": "διάδρομος — corridor"},
})

ITEMS.append({
 "id": "l175-dia-agorazoume-lacheio", "title": "Αγοράζουμε λαχείο;", "title_en": "Shall we buy a lottery ticket?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά μπροστά σε έναν λαχειοπώλη, λίγες μέρες πριν από την Πρωτοχρονιά.",
 "script": [
  L("Στέλιος", "m", "Έλα, ας πάρουμε ένα λαχείο της Πρωτοχρονιάς. Ο πατέρας μου έπαιρνε πάντα ένα, κάθε χρόνο, από τον ίδιο λαχειοπώλη.", "Come on, let's get a New Year lottery ticket. My father always bought one, every year, from the same seller."),
  L("Μυρτώ", "f", "Και κέρδισε ποτέ τίποτα; Ξέρεις ποιες είναι οι πιθανότητες να κερδίσεις το πρώτο λαχνό; Πιο πιθανό είναι να σε χτυπήσει κεραυνός.", "And did he ever win anything? Do you know the odds of winning the first prize? You're more likely to be struck by lightning."),
  L("Στέλιος", "m", "Δεν το αγοράζω για να γίνω πλούσιος. Το αγοράζω για να ονειρευτώ για μια εβδομάδα τι θα έκανα με τα λεφτά. Αυτό το όνειρο κοστίζει όσο δύο καφέδες.", "I don't buy it to get rich. I buy it to dream for a week about what I'd do with the money. That dream costs as much as two coffees."),
  L("Μυρτώ", "f", "Εντάξει, με έπεισες. Αλλά με έναν όρο: αν κερδίσουμε, το πρώτο που θα κάνουμε είναι να φτιάξουμε τη στέγη της μητέρας σου, όχι να αγοράσουμε σκάφος.", "OK, you've convinced me. But on one condition: if we win, the first thing we'll do is fix your mother's roof, not buy a boat."),
  L("Στέλιος", "m", "Σύμφωνοι. Το σκάφος θα το πάρουμε με τα ρέστα.", "Agreed. We'll buy the boat with the change."),
 ],
 "questions": [
  Q("Γιατί η Μυρτώ είναι αρχικά αρνητική;", ["Γιατί δεν έχει λεφτά μαζί της", "Γιατί οι πιθανότητες να κερδίσουν είναι ελάχιστες", "Γιατί δεν της αρέσει ο λαχειοπώλης", "Γιατί έχει ήδη αγοράσει λαχείο"], 1, "Πιο πιθανό είναι να σε χτυπήσει κεραυνός"),
  Q("Γιατί αγοράζει λαχείο ο Στέλιος;", ["Για να γίνει πλούσιος", "Για να βοηθήσει τον λαχειοπώλη", "Για να ονειρευτεί για μια εβδομάδα", "Γιατί του το ζήτησε η μητέρα του"], 2, "Το αγοράζω για να ονειρευτώ για μια εβδομάδα"),
  Q("Ποιον όρο βάζει η Μυρτώ;", ["Να φτιάξουν πρώτα τη στέγη της μητέρας του Στέλιου", "Να μοιράσουν τα λεφτά στα δύο", "Να αγοράσουν σκάφος", "Να μην πουν τίποτα σε κανέναν"], 0, "το πρώτο που θα κάνουμε είναι να φτιάξουμε τη στέγη της μητέρας σου"),
 ],
 "gloss": {"λαχειοπώλη": "λαχειοπώλης — lottery-ticket seller", "λαχείο": "λαχείο — lottery ticket", "πιθανότητες": "πιθανότητα — chance, odds", "λαχνό": "λαχνός — (lottery) prize", "κεραυνός": "κεραυνός — lightning bolt", "ονειρευτώ": "ονειρεύομαι — to dream", "όρο": "όρος — condition, term", "στέγη": "στέγη — roof", "σκάφος": "σκάφος — boat", "ρέστα": "ρέστα — change (money)"},
})

ITEMS.append({
 "id": "l175-dia-poios-tha-adeiasei-tin-apothiki", "title": "Ποιος θα αδειάσει την αποθήκη;", "title_en": "Who's going to clear out the storeroom?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο συγκατοίκους σε μια πολυκατοικία να συζητούν για την αποθήκη τους στο υπόγειο.",
 "script": [
  L("Ηλίας", "m", "Ο διαχειριστής άφησε σημείωμα: μέχρι το τέλος του μήνα πρέπει να αδειάσουμε τις αποθήκες, γιατί θα βάψουν το υπόγειο και θα αλλάξουν τις σωληνώσεις.", "The building manager left a note: by the end of the month we have to empty the storerooms, because they're going to paint the basement and change the pipes."),
  L("Ρένα", "f", "Τέλεια... Η δική μας είναι γεμάτη πράγματα που δεν έχουμε ανοίξει από τότε που μετακομίσαμε. Δύο ποδήλατα με σκασμένα λάστιχα, ένα χαλασμένο ηλεκτρικό καλοριφέρ και δέκα κούτες που λένε «διάφορα».", "Great... Ours is full of things we haven't opened since we moved. Two bikes with flat tyres, a broken electric heater and ten boxes that say 'miscellaneous'."),
  L("Ηλίας", "m", "Ας το δούμε σαν ευκαιρία. Ό,τι δεν έχουμε χρησιμοποιήσει τρία χρόνια, φεύγει. Τα ποδήλατα μπορούμε να τα δώσουμε στο εργαστήρι της γειτονιάς που τα επισκευάζει για παιδιά.", "Let's see it as an opportunity. Whatever we haven't used in three years goes. We can give the bikes to the neighbourhood workshop that repairs them for children."),
  L("Ρένα", "f", "Σύμφωνοι. Και το καλοριφέρ στην ανακύκλωση ηλεκτρικών συσκευών, όχι στον κάδο. Το Σάββατο το πρωί κατεβαίνουμε μαζί, με καφέ και γάντια. Αλλά τις κούτες μου τις ανοίγω εγώ!", "Agreed. And the heater goes to electrical-appliance recycling, not in the bin. Saturday morning we go down together, with coffee and gloves. But I'm opening my boxes myself!"),
 ],
 "questions": [
  Q("Γιατί πρέπει να αδειάσουν την αποθήκη;", ["Γιατί θα την πουλήσουν", "Γιατί θα βάψουν το υπόγειο και θα αλλάξουν τις σωληνώσεις", "Γιατί μπήκαν νερά", "Γιατί μετακομίζουν"], 1, "θα βάψουν το υπόγειο και θα αλλάξουν τις σωληνώσεις"),
  Q("Τι θα κάνουν με τα ποδήλατα;", ["Θα τα πετάξουν", "Θα τα πουλήσουν", "Θα τα δώσουν σε ένα εργαστήρι που τα επισκευάζει για παιδιά", "Θα τα φτιάξουν οι ίδιοι"], 2, "να τα δώσουμε στο εργαστήρι της γειτονιάς"),
  Q("Τι θέλει να κάνει μόνη της η Ρένα;", ["Να ανοίξει τις δικές της κούτες", "Να μιλήσει στον διαχειριστή", "Να πάει το καλοριφέρ στην ανακύκλωση", "Να φτιάξει καφέ"], 0, "τις κούτες μου τις ανοίγω εγώ"),
 ],
 "gloss": {"συγκατοίκους": "συγκάτοικος — flatmate", "αποθήκη": "αποθήκη — storeroom", "υπόγειο": "υπόγειο — basement", "διαχειριστής": "διαχειριστής — building manager", "σωληνώσεις": "σωλήνωση — pipework", "σκασμένα λάστιχα": "σκασμένο λάστιχο — flat tyre", "καλοριφέρ": "καλοριφέρ — heater, radiator", "εργαστήρι": "εργαστήρι — workshop", "ηλεκτρικών συσκευών": "ηλεκτρική συσκευή — electrical appliance"},
})

ITEMS.append({
 "id": "l175-mon-egina-nona", "title": "Πώς έγινα νονά", "title_en": "How I became a godmother", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια νέα γυναίκα να μιλάει σε ένα ραδιοφωνικό πρόγραμμα για την πρώτη φορά που βάφτισε ένα παιδί.",
 "script": [
  L("Νέα γυναίκα", "f", "Όταν η καλύτερή μου φίλη μού ζήτησε να βαφτίσω την κόρη της, έκλαψα. Ήταν τιμή, αλλά και ευθύνη. Στην Ελλάδα ο νονός ή η νονά δεν είναι απλώς ένας καλεσμένος· θεωρείται κάτι σαν δεύτερος γονιός, και συχνά διαλέγει και το όνομα του παιδιού.", "When my best friend asked me to baptise her daughter, I cried. It was an honour, but also a responsibility. In Greece the godfather or godmother isn't just a guest; they are considered something like a second parent, and often they even choose the child's name."),
  L("Νέα γυναίκα", "f", "Σύμφωνα με το έθιμο, η νονά αγοράζει τα λευκά ρούχα της βάφτισης, τη λαμπάδα και τις μπομπονιέρες. Το πιο αγχωτικό για μένα ήταν η ίδια η τελετή. Ο ιερέας βύθισε το μωρό τρεις φορές στην κολυμπήθρα, εκείνο έβαλε τις φωνές, κι εγώ έπρεπε να το πάρω στην αγκαλιά μου, βρεγμένο και θυμωμένο, χωρίς να μου πέσει.", "According to custom, the godmother buys the white baptism clothes, the candle and the favours. The most stressful thing for me was the ceremony itself. The priest immersed the baby three times in the font, she started screaming, and I had to take her in my arms, wet and angry, without dropping her."),
  L("Νέα γυναίκα", "f", "Αυτό έγινε πριν από τέσσερα χρόνια. Τώρα η βαφτιστήρα μου τρέχει να με αγκαλιάσει μόλις με δει, και κάθε Πάσχα της φέρνω μια λαμπάδα. Δεν είναι κόρη μου, αλλά δεν είναι και απλώς η κόρη μιας φίλης.", "That was four years ago. Now my goddaughter runs to hug me as soon as she sees me, and every Easter I bring her a candle. She isn't my daughter, but she isn't just a friend's daughter either."),
 ],
 "questions": [
  Q("Πώς θεωρείται συχνά η νονά στην Ελλάδα;", ["Ένας απλός καλεσμένος", "Κάτι σαν δεύτερος γονιός", "Η δασκάλα του παιδιού", "Ένας μακρινός συγγενής"], 1, "θεωρείται κάτι σαν δεύτερος γονιός"),
  Q("Τι ήταν το πιο αγχωτικό για εκείνη;", ["Η επιλογή του ονόματος", "Οι μπομπονιέρες", "Η τελετή, όταν έπρεπε να πάρει το βρεγμένο μωρό στην αγκαλιά", "Το τραπέζι μετά τη βάφτιση"], 2, "Το πιο αγχωτικό για μένα ήταν η ίδια η τελετή"),
  Q("Τι κάνει κάθε Πάσχα;", ["Φέρνει στη βαφτιστήρα της μια λαμπάδα", "Πηγαίνει στο χωριό", "Ψήνει αρνί με τη φίλη της", "Φτιάχνει κουλουράκια"], 0, "κάθε Πάσχα της φέρνω μια λαμπάδα"),
 ],
 "gloss": {"βάφτισε": "βαφτίζω — to baptise; to be godparent to", "τιμή": "τιμή — honour", "ευθύνη": "ευθύνη — responsibility", "νονός": "νονός — godfather", "νονά": "νονά — godmother", "λαμπάδα": "λαμπάδα — (large) candle", "μπομπονιέρες": "μπομπονιέρα — favour (sugared almonds at a christening or wedding)", "τελετή": "τελετή — ceremony", "βύθισε": "βυθίζω — to immerse", "κολυμπήθρα": "κολυμπήθρα — baptismal font", "βαφτιστήρα": "βαφτιστήρα — goddaughter"},
})

ITEMS.append({
 "id": "l175-vm-diskadiko-pikap", "title": "Μήνυμα από το δισκάδικο για το πικάπ", "title_en": "A message from the record shop about the turntable", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα που άφησε ο ιδιοκτήτης ενός δισκάδικου σε έναν πελάτη.",
 "script": [
  L("Ιδιοκτήτης", "m", "Γεια σου, Λευτέρη, ο Τάκης από το δισκάδικο. Το πικάπ του πατέρα σου είναι έτοιμο. Άλλαξα τη βελόνα και τον ιμάντα, που είχε σκληρύνει από τα χρόνια, και τώρα γυρίζει στη σωστή ταχύτητα. Δοκίμασα έναν δίσκο του Χατζιδάκι και ακούγεται υπέροχα.", "Hi, Lefteris, it's Takis from the record shop. Your father's turntable is ready. I changed the needle and the belt, which had gone hard over the years, and now it turns at the right speed. I tried a Hadjidakis record and it sounds wonderful."),
  L("Ιδιοκτήτης", "m", "Το κόστος είναι πενήντα ευρώ, όπως είχαμε πει. Και κάτι ακόμα: ο δίσκος που μου είχες ζητήσει, η πρώτη έκδοση από το 1971, μου ήρθε χθες από έναν συλλέκτη στη Θεσσαλονίκη. Το εξώφυλλο έχει μια μικρή σχισμή στη γωνία, αλλά ο ίδιος ο δίσκος δεν έχει ούτε μία γρατζουνιά.", "The cost is fifty euros, as we'd said. And one more thing: the record you'd asked me for, the first edition from 1971, came to me yesterday from a collector in Thessaloniki. The sleeve has a small tear at the corner, but the record itself doesn't have a single scratch."),
  L("Ιδιοκτήτης", "m", "Θα σου τον κρατήσω ως την Κυριακή. Πέρνα όποτε μπορείς, εκτός από Δευτέρα, που είμαστε κλειστά. Και φέρε μια τσάντα, γιατί το πικάπ είναι βαρύ!", "I'll keep it for you until Sunday. Come by whenever you can, except Monday, when we're closed. And bring a bag, because the turntable is heavy!"),
 ],
 "questions": [
  Q("Τι επισκεύασε ο ιδιοκτήτης στο πικάπ;", ["Τα ηχεία", "Άλλαξε τη βελόνα και τον ιμάντα", "Το καλώδιο του ρεύματος", "Το καπάκι"], 1, "Άλλαξα τη βελόνα και τον ιμάντα"),
  Q("Σε τι κατάσταση είναι ο δίσκος του 1971;", ["Έχει πολλές γρατζουνιές", "Είναι καινούργιος, στο πλαστικό του", "Το εξώφυλλο έχει μια μικρή σχισμή, αλλά ο δίσκος είναι άψογος", "Λείπει το εξώφυλλο"], 2, "Το εξώφυλλο έχει μια μικρή σχισμή στη γωνία, αλλά ο ίδιος ο δίσκος δεν έχει ούτε μία γρατζουνιά"),
  Q("Πότε δεν μπορεί να περάσει ο πελάτης;", ["Τη Δευτέρα", "Την Κυριακή", "Το Σάββατο", "Την Παρασκευή"], 0, "εκτός από Δευτέρα, που είμαστε κλειστά"),
 ],
 "gloss": {"δισκάδικου": "δισκάδικο — record shop", "πικάπ": "πικάπ — record player, turntable", "βελόνα": "βελόνα — needle, stylus", "ιμάντα": "ιμάντας — belt", "σκληρύνει": "σκληραίνω — to harden", "ταχύτητα": "ταχύτητα — speed", "δίσκο": "δίσκος — record", "έκδοση": "έκδοση — edition", "συλλέκτη": "συλλέκτης — collector", "εξώφυλλο": "εξώφυλλο — sleeve, cover", "σχισμή": "σχισμή — tear, slit", "γρατζουνιά": "γρατζουνιά — scratch"},
})

ITEMS.append({
 "id": "l175-vm-omilos-kopilasias", "title": "Μήνυμα από τον όμιλο κωπηλασίας", "title_en": "A message from the rowing club", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα που άφησε ένας προπονητής κωπηλασίας στους γονείς μιας αθλήτριας.",
 "script": [
  L("Προπονητής", "m", "Καλησπέρα σας, ο Σπύρος είμαι, ο προπονητής της Ιφιγένειας στον όμιλο κωπηλασίας. Έχω καλά νέα: η Ιφιγένεια και η συναθλήτριά της επιλέχθηκαν για τη διπλή λέμβο στους πανελλήνιους αγώνες νέων, που θα γίνουν σε τρεις εβδομάδες στη λίμνη.", "Good evening, it's Spyros, Ifigeneia's coach at the rowing club. I have good news: Ifigeneia and her teammate have been selected for the double scull at the national youth championships, which will take place in three weeks on the lake."),
  L("Προπονητής", "m", "Από τη Δευτέρα οι προπονήσεις γίνονται καθημερινές, στις έξι το πρωί, πριν από το σχολείο, γιατί τότε το νερό είναι πιο ήρεμο. Ο όμιλος έχει μικρό λεωφορείο που θα μαζεύει τα παιδιά από την πλατεία στις πέντε και μισή.", "From Monday training is daily, at six in the morning, before school, because the water is calmer then. The club has a minibus that will pick the children up from the square at half past five."),
  L("Προπονητής", "m", "Για τους αγώνες θα χρειαστούμε την υπογραφή σας σε ένα έντυπο και ένα πρόσφατο πιστοποιητικό υγείας. Και φροντίστε να κοιμάται νωρίς· με ξύπνημα στις πέντε, το βράδυ δεν είναι ώρα για κινητά! Ευχαριστώ.", "For the championships we'll need your signature on a form and a recent health certificate. And make sure she goes to bed early; with a five o'clock wake-up, the evening is no time for mobile phones! Thank you."),
 ],
 "questions": [
  Q("Ποια είναι τα καλά νέα;", ["Η Ιφιγένεια κέρδισε ένα μετάλλιο", "Η Ιφιγένεια επιλέχθηκε για τους πανελλήνιους αγώνες νέων", "Ο όμιλος αγόρασε καινούργια βάρκα", "Οι προπονήσεις σταματούν"], 1, "επιλέχθηκαν για τη διπλή λέμβο στους πανελλήνιους αγώνες νέων"),
  Q("Γιατί οι προπονήσεις γίνονται στις έξι το πρωί;", ["Γιατί ο προπονητής δουλεύει το απόγευμα", "Γιατί κάνει λιγότερη ζέστη", "Γιατί τότε το νερό είναι πιο ήρεμο", "Γιατί η λίμνη κλείνει το απόγευμα"], 2, "γιατί τότε το νερό είναι πιο ήρεμο"),
  Q("Τι συμβουλεύει ο προπονητής τους γονείς;", ["Να φροντίσουν να κοιμάται νωρίς η κόρη τους", "Να της αγοράσουν καινούργια κουπιά", "Να την πηγαίνουν οι ίδιοι στη λίμνη", "Να μην πάει σχολείο"], 0, "φροντίστε να κοιμάται νωρίς"),
 ],
 "gloss": {"προπονητής": "προπονητής — coach", "κωπηλασίας": "κωπηλασία — rowing", "όμιλο": "όμιλος — club", "συναθλήτριά": "συναθλήτρια — (female) teammate", "επιλέχθηκαν": "επιλέγομαι — to be selected", "διπλή λέμβο": "διπλή λέμβος — double scull", "πανελλήνιους αγώνες": "πανελλήνιοι αγώνες — national championships", "ήρεμο": "ήρεμος — calm", "πιστοποιητικό υγείας": "πιστοποιητικό υγείας — health certificate"},
})

ITEMS.append({
 "id": "l175-c1-pos-zestainontai-oi-pigkouinoi", "title": "Πώς αντέχουν οι αυτοκρατορικοί πιγκουίνοι το κρύο", "title_en": "How emperor penguins survive the cold", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια βιολόγο που έχει μελετήσει τους πιγκουίνους της Ανταρκτικής.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι αυτοκρατορικοί πιγκουίνοι αναπαράγονται στη διάρκεια του ανταρκτικού χειμώνα. Γιατί διάλεξαν την πιο σκληρή εποχή;", "Emperor penguins breed during the Antarctic winter. Why did they choose the harshest season?"),
  L("Βιολόγος", "f", "Επειδή ο κύκλος τους είναι πολύ μεγάλος. Αν τα μικρά δεν γεννηθούν τον χειμώνα, δεν θα είναι έτοιμα να ζήσουν μόνα τους το καλοκαίρι, όταν η θάλασσα είναι γεμάτη τροφή. Ο θηλυκός πιγκουίνος γεννά ένα αυγό και το αφήνει στο αρσενικό, που το κρατά πάνω στα πόδια του, κάτω από μια πτυχή του δέρματος, για περίπου δύο μήνες, σχεδόν χωρίς να φάει.", "Because their cycle is very long. If the chicks aren't born in winter, they won't be ready to live on their own in summer, when the sea is full of food. The female lays one egg and leaves it to the male, who holds it on his feet, under a fold of skin, for about two months, almost without eating."),
  L("Δημοσιογράφος", "m", "Πώς επιβιώνει μέσα σε τέτοιες θερμοκρασίες;", "How does he survive in such temperatures?"),
  L("Βιολόγος", "f", "Το πιο εντυπωσιακό είναι η συμπεριφορά της ομάδας. Χιλιάδες αρσενικά στριμώχνονται το ένα δίπλα στο άλλο, και μέσα στο σμήνος η θερμοκρασία μπορεί να ξεπεράσει τους είκοσι βαθμούς, ενώ έξω είναι πολύ κάτω από το μηδέν. Το σμήνος κινείται αργά και συνεχώς, έτσι ώστε κανένα πουλί να μη μένει για πολύ στην παγωμένη άκρη. Είναι, θα λέγαμε, μια εναλλαγή βαρδιών χωρίς αρχηγό.", "The most impressive thing is the group's behaviour. Thousands of males crowd together side by side, and inside the huddle the temperature can exceed twenty degrees, while outside it is far below zero. The huddle moves slowly and continuously, so that no bird stays for long on the frozen edge. It is, one might say, a rotation of shifts without a leader."),
  L("Βιολόγος", "f", "Βοηθά επίσης η ανατομία τους: πυκνά φτερά, ένα παχύ στρώμα λίπους και ένα σύστημα αγγείων στα πόδια, όπου το ζεστό αίμα που κατεβαίνει ζεσταίνει το κρύο αίμα που ανεβαίνει. Έτσι τα πόδια μένουν κρύα, αλλά χάνεται ελάχιστη θερμότητα.", "Their anatomy also helps: dense feathers, a thick layer of fat and a system of blood vessels in the feet, where the warm blood going down warms the cold blood coming up. So the feet stay cold, but very little heat is lost."),
 ],
 "questions": [
  Q("Ποιος κρατάει το αυγό τον χειμώνα;", ["Το θηλυκό", "Το αρσενικό, πάνω στα πόδια του", "Και οι δύο γονείς εναλλάξ", "Κανείς· το αυγό μένει στον πάγο"], 1, "το αφήνει στο αρσενικό, που το κρατά πάνω στα πόδια του"),
  Q("Γιατί το σμήνος κινείται συνεχώς;", ["Για να βρει τροφή", "Για να ξεφύγει από τους εχθρούς", "Για να μη μένει κανένα πουλί για πολύ στην παγωμένη άκρη", "Για να φτάσει στη θάλασσα"], 2, "έτσι ώστε κανένα πουλί να μη μένει για πολύ στην παγωμένη άκρη"),
  Q("Πώς βοηθά το σύστημα αγγείων στα πόδια;", ["Το ζεστό αίμα που κατεβαίνει ζεσταίνει το κρύο αίμα που ανεβαίνει, κι έτσι χάνεται λίγη θερμότητα", "Κρατάει τα πόδια πολύ ζεστά", "Σταματάει την κυκλοφορία του αίματος", "Παράγει λίπος"], 0, "το ζεστό αίμα που κατεβαίνει ζεσταίνει το κρύο αίμα που ανεβαίνει"),
 ],
 "gloss": {"πιγκουίνους": "πιγκουίνος — penguin", "αυτοκρατορικοί": "αυτοκρατορικός — emperor (penguin); imperial", "αναπαράγονται": "αναπαράγομαι — to breed, reproduce", "πτυχή": "πτυχή — fold", "επιβιώνει": "επιβιώνω — to survive", "στριμώχνονται": "στριμώχνομαι — to crowd together", "σμήνος": "σμήνος — huddle, swarm, flock", "εναλλαγή βαρδιών": "εναλλαγή βαρδιών — rotation of shifts", "ανατομία": "ανατομία — anatomy", "στρώμα λίπους": "στρώμα λίπους — layer of fat", "αγγείων": "αγγείο — (blood) vessel"},
})

ITEMS.append({
 "id": "l175-c1-ti-dinei-to-chroma-sta-matia", "title": "Τι δίνει το χρώμα στα μάτια μας", "title_en": "What gives our eyes their colour", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια οφθαλμίατρο σε μια ομιλία για το χρώμα της ίριδας.",
 "script": [
  L("Οφθαλμίατρος", "f", "Το χρώμα των ματιών μας το καθορίζει κυρίως μια χρωστική, η μελανίνη, που βρίσκεται στην ίριδα. Τα καστανά μάτια έχουν πολλή μελανίνη, τα πράσινα και τα γαλανά λιγότερη. Και εδώ υπάρχει μια έκπληξη: στα γαλανά μάτια δεν υπάρχει καμία γαλάζια χρωστική.", "The colour of our eyes is determined mainly by a pigment, melanin, which is in the iris. Brown eyes have a lot of melanin, green and blue ones less. And here there's a surprise: in blue eyes there is no blue pigment at all."),
  L("Οφθαλμίατρος", "f", "Το γαλάζιο χρώμα οφείλεται στον τρόπο που σκεδάζεται το φως μέσα στην ίριδα, όπως περίπου ο ουρανός φαίνεται γαλάζιος χωρίς να είναι βαμμένος. Γι' αυτό τα γαλανά μάτια μπορεί να φαίνονται άλλοτε γκρίζα και άλλοτε σχεδόν πράσινα, ανάλογα με τον φωτισμό.", "The blue colour is due to the way light is scattered inside the iris, roughly as the sky looks blue without being painted. That's why blue eyes can sometimes look grey and sometimes almost green, depending on the lighting."),
  L("Οφθαλμίατρος", "f", "Πολλά μωρά γεννιούνται με ανοιχτόχρωμα μάτια, που σκουραίνουν τους πρώτους μήνες ή χρόνια, καθώς παράγεται περισσότερη μελανίνη. Παλιότερα στα σχολεία διδασκόταν ότι το χρώμα των ματιών ελέγχεται από ένα μόνο γονίδιο. Σήμερα ξέρουμε ότι παίζουν ρόλο πολλά γονίδια, γι' αυτό σπάνια, αλλά όχι αδύνατο, δύο γονείς με γαλανά μάτια μπορεί να έχουν παιδί με καστανά. Τέλος, τα σχέδια της ίριδας είναι τόσο μοναδικά, που χρησιμοποιούνται για την αναγνώριση προσώπων σε συστήματα ασφαλείας.", "Many babies are born with light-coloured eyes that darken in the first months or years, as more melanin is produced. In the past, schools taught that eye colour is controlled by a single gene. Today we know that many genes play a role, so rarely, but not impossibly, two blue-eyed parents may have a brown-eyed child. Finally, the patterns of the iris are so unique that they are used to identify people in security systems."),
 ],
 "questions": [
  Q("Τι ισχύει για τα γαλανά μάτια;", ["Έχουν πολλή γαλάζια χρωστική", "Δεν έχουν καμία γαλάζια χρωστική", "Έχουν περισσότερη μελανίνη από τα καστανά", "Αλλάζουν χρώμα κάθε μέρα"], 1, "στα γαλανά μάτια δεν υπάρχει καμία γαλάζια χρωστική"),
  Q("Σε τι οφείλεται το γαλάζιο χρώμα των ματιών;", ["Σε μια γαλάζια χρωστική", "Στο αίμα της ίριδας", "Στον τρόπο που σκεδάζεται το φως μέσα στην ίριδα", "Στο χρώμα του ουρανού που καθρεφτίζεται"], 2, "οφείλεται στον τρόπο που σκεδάζεται το φως μέσα στην ίριδα"),
  Q("Τι ξέρουμε σήμερα για την κληρονομικότητα του χρώματος των ματιών;", ["Ότι παίζουν ρόλο πολλά γονίδια", "Ότι το ελέγχει ένα μόνο γονίδιο", "Ότι δεν κληρονομείται", "Ότι εξαρτάται μόνο από τη μητέρα"], 0, "Σήμερα ξέρουμε ότι παίζουν ρόλο πολλά γονίδια"),
 ],
 "gloss": {"οφθαλμίατρο": "οφθαλμίατρος — ophthalmologist", "ίριδας": "ίριδα — iris", "καθορίζει": "καθορίζω — to determine", "χρωστική": "χρωστική — pigment", "μελανίνη": "μελανίνη — melanin", "σκεδάζεται": "σκεδάζομαι — to be scattered (of light)", "φωτισμό": "φωτισμός — lighting", "ανοιχτόχρωμα": "ανοιχτόχρωμος — light-coloured", "σκουραίνουν": "σκουραίνω — to darken", "γονίδιο": "γονίδιο — gene", "αναγνώριση": "αναγνώριση — identification, recognition"},
})

rnd = random.Random(175)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-175.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
