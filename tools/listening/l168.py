# Source for library/listening/listening-168.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l168.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l168-ann-ixitikos-odigos", "title": "Νέος ηχητικός οδηγός στο μουσείο", "title_en": "A new audio guide at the museum", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός αρχαιολογικού μουσείου.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί επισκέπτες, σας ενημερώνουμε ότι από σήμερα το μουσείο διαθέτει δωρεάν ηχητικό οδηγό σε έξι γλώσσες. Για να τον χρησιμοποιήσετε, κατεβάστε την εφαρμογή του μουσείου στο κινητό σας, συνδεόμενοι στο ασύρματο δίκτυο, που είναι επίσης δωρεάν.", "Dear visitors, we inform you that from today the museum offers a free audio guide in six languages. To use it, download the museum's app to your phone by connecting to the wireless network, which is also free."),
  L("Εκφωνήτρια", "f", "Δίπλα σε κάθε σημαντικό έκθεμα θα βρείτε έναν αριθμό. Πληκτρολογήστε τον στην εφαρμογή για να ακούσετε μια σύντομη περιγραφή. Υπάρχει και ειδική διαδρομή για παιδιά, με ιστορίες και ερωτήσεις-παιχνίδια.", "Next to every important exhibit you will find a number. Type it into the app to hear a short description. There is also a special route for children, with stories and quiz games."),
  L("Εκφωνήτρια", "f", "Παρακαλούμε να χρησιμοποιείτε ακουστικά, για να μην ενοχλείτε τους άλλους επισκέπτες. Αν δεν έχετε, μπορείτε να δανειστείτε ένα ζευγάρι από το πωλητήριο, αφήνοντας την ταυτότητά σας.", "Please use headphones so as not to disturb other visitors. If you don't have any, you can borrow a pair from the museum shop by leaving your ID card."),
 ],
 "questions": [
  Q("Πώς μπορεί κανείς να χρησιμοποιήσει τον ηχητικό οδηγό;", ["Νοικιάζοντας μια συσκευή στο ταμείο", "Κατεβάζοντας την εφαρμογή του μουσείου στο κινητό", "Καλώντας έναν αριθμό τηλεφώνου", "Ζητώντας έναν ξεναγό"], 1, "κατεβάστε την εφαρμογή του μουσείου στο κινητό σας"),
  Q("Τι υπάρχει ειδικά για τα παιδιά;", ["Ένα εργαστήρι ζωγραφικής", "Δωρεάν παγωτό", "Μια διαδρομή με ιστορίες και ερωτήσεις-παιχνίδια", "Μια αίθουσα με βίντεο"], 2, "Υπάρχει και ειδική διαδρομή για παιδιά, με ιστορίες και ερωτήσεις-παιχνίδια"),
  Q("Τι πρέπει να αφήσει κανείς για να δανειστεί ακουστικά;", ["Την ταυτότητά του", "Δέκα ευρώ", "Το εισιτήριό του", "Το κινητό του"], 0, "αφήνοντας την ταυτότητά σας"),
 ],
 "gloss": {"μεγάφωνα": "μεγάφωνο — loudspeaker", "διαθέτει": "διαθέτω — to have, offer", "ηχητικό οδηγό": "ηχητικός οδηγός — audio guide", "κατεβάστε": "κατεβάζω — to download", "εφαρμογή": "εφαρμογή — app", "ασύρματο δίκτυο": "ασύρματο δίκτυο — wireless network", "έκθεμα": "έκθεμα — exhibit", "Πληκτρολογήστε": "πληκτρολογώ — to type", "ακουστικά": "ακουστικά — headphones", "ενοχλείτε": "ενοχλώ — to disturb", "πωλητήριο": "πωλητήριο — museum shop", "ταυτότητά": "ταυτότητα — ID card"},
})

ITEMS.append({
 "id": "l168-int-ypotitlistria", "title": "Η μεταφράστρια των υποτίτλων", "title_en": "The subtitle translator", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια μεταφράστρια που γράφει ελληνικούς υπότιτλους για ταινίες και σειρές.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσο δύσκολο είναι να μεταφράζεις υπότιτλους;", "How hard is it to translate subtitles?"),
  L("Μεταφράστρια", "f", "Πιο δύσκολο απ' ό,τι φαίνεται. Ο θεατής πρέπει να προλαβαίνει να διαβάσει τον υπότιτλο και να δει και την εικόνα. Έτσι, κάθε γραμμή έχει περιορισμένο αριθμό χαρακτήρων και μένει στην οθόνη λίγα δευτερόλεπτα. Συχνά ο ηθοποιός λέει μια ολόκληρη πρόταση και εγώ έχω χώρο μόνο για πέντε λέξεις.", "Harder than it looks. The viewer must have time to read the subtitle and also see the picture. So every line has a limited number of characters and stays on screen for a few seconds. Often the actor says a whole sentence and I only have room for five words."),
  L("Δημοσιογράφος", "m", "Και τι γίνεται με τα αστεία;", "And what about the jokes?"),
  L("Μεταφράστρια", "f", "Είναι ο εφιάλτης μας. Ένα λογοπαίγνιο στα αγγλικά σχεδόν ποτέ δεν λειτουργεί αν το μεταφράσεις κατά λέξη. Πρέπει να βρεις ένα δικό σου αστείο, που να ταιριάζει με αυτό που δείχνει η εικόνα. Μια φορά έψαχνα τρεις μέρες για ένα αστείο με μια μπανάνα.", "They're our nightmare. A pun in English almost never works if you translate it word for word. You have to find a joke of your own that fits what the picture shows. Once I searched for three days for a joke with a banana."),
  L("Δημοσιογράφος", "m", "Σας αρέσει ακόμα να βλέπετε ταινίες;", "Do you still enjoy watching films?"),
  L("Μεταφράστρια", "f", "Πολύ, αλλά δεν μπορώ να μη διαβάζω τους υπότιτλους των άλλων. Ο άντρας μου λέει ότι στο σινεμά κάθομαι σαν δασκάλα που διορθώνει γραπτά. Γι' αυτό τις Κυριακές βλέπουμε μόνο ελληνικές ταινίες, χωρίς υπότιτλους.", "Very much, but I can't help reading other people's subtitles. My husband says that at the cinema I sit like a teacher marking papers. That's why on Sundays we only watch Greek films, without subtitles."),
 ],
 "questions": [
  Q("Γιατί κάθε υπότιτλος πρέπει να είναι σύντομος;", ["Γιατί το θέλουν οι ηθοποιοί", "Γιατί ο θεατής πρέπει να προλαβαίνει να τον διαβάσει και να δει και την εικόνα", "Γιατί η μετάφραση πληρώνεται ανά λέξη", "Γιατί οι οθόνες είναι μικρές"], 1, "Ο θεατής πρέπει να προλαβαίνει να διαβάσει τον υπότιτλο και να δει και την εικόνα"),
  Q("Τι κάνει με ένα λογοπαίγνιο που δεν μεταφράζεται;", ["Το αφήνει στα αγγλικά", "Το παραλείπει", "Βρίσκει ένα δικό της αστείο που ταιριάζει με την εικόνα", "Γράφει μια σημείωση στο κάτω μέρος"], 2, "Πρέπει να βρεις ένα δικό σου αστείο, που να ταιριάζει με αυτό που δείχνει η εικόνα"),
  Q("Γιατί τις Κυριακές βλέπουν μόνο ελληνικές ταινίες;", ["Για να μη διαβάζει υπότιτλους σαν να διορθώνει γραπτά", "Γιατί ο άντρας της δεν ξέρει αγγλικά", "Γιατί είναι φθηνότερες", "Γιατί τις μεταφράζει η ίδια"], 0, "δεν μπορώ να μη διαβάζω τους υπότιτλους των άλλων"),
 ],
 "gloss": {"μεταφράστρια": "μεταφράστρια — translator (f.)", "υπότιτλους": "υπότιτλος — subtitle", "θεατής": "θεατής — viewer", "περιορισμένο": "περιορισμένος — limited", "χαρακτήρων": "χαρακτήρας — character (letter)", "οθόνη": "οθόνη — screen", "εφιάλτης": "εφιάλτης — nightmare", "λογοπαίγνιο": "λογοπαίγνιο — pun", "κατά λέξη": "κατά λέξη — word for word", "γραπτά": "γραπτό — (exam) paper"},
})

ITEMS.append({
 "id": "l168-int-metaglottisi", "title": "Η φωνή των κινουμένων σχεδίων", "title_en": "The voice of the cartoons", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν ηθοποιό που δανείζει τη φωνή του σε ήρωες κινουμένων σχεδίων στη μεταγλώττιση.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς είναι μια μέρα στο στούντιο μεταγλώττισης;", "What is a day in the dubbing studio like?"),
  L("Ηθοποιός", "m", "Στέκομαι μπροστά σε ένα μικρόφωνο και σε μια οθόνη, όπου βλέπω την ταινία. Πρέπει να λέω τα λόγια ακριβώς τη στιγμή που ανοίγει το στόμα ο ήρωας, ούτε πιο νωρίς ούτε πιο αργά. Συνήθως ηχογραφούμε μόνοι μας, χωρίς τους άλλους ηθοποιούς, οπότε πρέπει να φανταστώ σε ποιον μιλάω.", "I stand in front of a microphone and a screen where I watch the film. I have to say the lines exactly when the character opens his mouth, neither earlier nor later. We usually record alone, without the other actors, so I have to imagine whom I'm talking to."),
  L("Δημοσιογράφος", "f", "Ποιος ήταν ο πιο δύσκολος ρόλος σας;", "What was your most difficult role?"),
  L("Ηθοποιός", "m", "Ένα σκαντζόχοιρος που μιλούσε πολύ γρήγορα και φτερνιζόταν σε κάθε πρόταση. Μετά από τέσσερις ώρες ηχογράφησης είχα πονοκέφαλο από τα φτερνίσματα. Το πιο δύσκολο όμως είναι το τραγούδι: στις ταινίες για παιδιά οι ήρωες τραγουδούν συχνά, και ο στίχος πρέπει να χωράει στη μουσική και στο στόμα του ήρωα.", "A hedgehog who spoke very fast and sneezed in every sentence. After four hours of recording I had a headache from the sneezes. But the hardest thing is singing: in children's films the characters often sing, and the lyrics have to fit the music and the character's mouth."),
  L("Δημοσιογράφος", "f", "Σας αναγνωρίζουν τα παιδιά;", "Do children recognise you?"),
  L("Ηθοποιός", "m", "Από το πρόσωπο, ποτέ. Από τη φωνή, καμιά φορά. Μια φορά, σε ένα φούρνο, ένα αγοράκι γύρισε απότομα και φώναξε στη μαμά του: «Ο σκαντζόχοιρος αγοράζει ψωμί!» Ήταν η καλύτερη κριτική που πήρα ποτέ.", "By my face, never. By my voice, sometimes. Once, at a bakery, a little boy turned round suddenly and shouted to his mum: 'The hedgehog is buying bread!' It was the best review I've ever had."),
 ],
 "questions": [
  Q("Τι είναι το πιο σημαντικό όταν λέει τα λόγια του;", ["Να μιλάει δυνατά", "Να τα λέει ακριβώς τη στιγμή που ανοίγει το στόμα ο ήρωας", "Να τα ξέρει απ' έξω", "Να αλλάζει τη φωνή του σε κάθε σκηνή"], 1, "Πρέπει να λέω τα λόγια ακριβώς τη στιγμή που ανοίγει το στόμα ο ήρωας"),
  Q("Ποιο είναι, κατά τον ίδιο, το πιο δύσκολο στη μεταγλώττιση;", ["Οι μεγάλες ώρες", "Τα φτερνίσματα", "Το τραγούδι, γιατί ο στίχος πρέπει να χωράει στη μουσική και στο στόμα του ήρωα", "Η συνεργασία με τους σκηνοθέτες"], 2, "Το πιο δύσκολο όμως είναι το τραγούδι"),
  Q("Πώς τον αναγνώρισε ένα αγοράκι;", ["Από τη φωνή του, σε έναν φούρνο", "Από μια αφίσα", "Από την τηλεόραση", "Από το πρόσωπό του"], 0, "σε ένα φούρνο, ένα αγοράκι γύρισε απότομα"),
 ],
 "gloss": {"δανείζει": "δανείζω — to lend", "κινουμένων σχεδίων": "κινούμενα σχέδια — cartoons", "μεταγλώττιση": "μεταγλώττιση — dubbing", "μεταγλώττισης": "μεταγλώττιση — dubbing", "ηχογραφούμε": "ηχογραφώ — to record", "φανταστώ": "φαντάζομαι — to imagine", "σκαντζόχοιρος": "σκαντζόχοιρος — hedgehog", "φτερνιζόταν": "φτερνίζομαι — to sneeze", "φτερνίσματα": "φτέρνισμα — sneeze", "στίχος": "στίχος — lyric, verse", "χωράει": "χωράω — to fit", "κριτική": "κριτική — review"},
})

ITEMS.append({
 "id": "l168-dia-allagi-dorou", "title": "Αλλάζοντας ένα δώρο", "title_en": "Exchanging a present", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο σε ένα κατάστημα με είδη σπιτιού, όπου μια πελάτισσα θέλει να αλλάξει ένα δώρο.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Μου χάρισαν αυτή την καφετιέρα για τα γενέθλιά μου, αλλά έχω ήδη μία ίδια. Θα ήθελα να την αλλάξω, αν γίνεται.", "Good morning. I was given this coffee maker for my birthday, but I already have an identical one. I'd like to exchange it, if possible."),
  L("Υπάλληλος", "m", "Βεβαίως. Έχετε την απόδειξη ή μια απόδειξη δώρου;", "Of course. Do you have the receipt or a gift receipt?"),
  L("Πελάτισσα", "f", "Όχι, δυστυχώς. Η φίλη που μου την έκανε δώρο έχει φύγει για ταξίδι και δεν θέλω να τη ρωτήσω, για να μην καταλάβει ότι την αλλάζω.", "No, unfortunately. The friend who gave it to me has gone travelling and I don't want to ask her, so she won't realise I'm exchanging it."),
  L("Υπάλληλος", "m", "Καταλαβαίνω. Χωρίς απόδειξη δεν μπορώ να σας επιστρέψω χρήματα, αλλά μπορώ να σας κάνω αλλαγή με άλλο προϊόν, στην τρέχουσα τιμή της καφετιέρας. Βλέπω ότι είναι σφραγισμένη, οπότε δεν υπάρχει πρόβλημα.", "I understand. Without a receipt I can't give you a refund, but I can exchange it for another product, at the coffee maker's current price. I see that it's sealed, so there's no problem."),
  L("Πελάτισσα", "f", "Τέλεια. Τότε θα ήθελα εκείνο το σετ με τα μαχαίρια. Αν είναι πιο ακριβό, πληρώνω τη διαφορά.", "Perfect. Then I'd like that set of knives. If it's more expensive, I'll pay the difference."),
  L("Υπάλληλος", "m", "Είναι ακριβώς δέκα ευρώ πιο ακριβό. Και αν θέλετε, σας δίνω και ένα κουπόνι, γιατί η καφετιέρα είναι αυτή την εβδομάδα σε προσφορά και η τιμή της έχει πέσει.", "It's exactly ten euros more expensive. And if you like, I'll give you a voucher too, because the coffee maker is on offer this week and its price has gone down."),
 ],
 "questions": [
  Q("Γιατί θέλει να αλλάξει την καφετιέρα;", ["Γιατί είναι χαλασμένη", "Γιατί έχει ήδη μία ίδια", "Γιατί δεν της αρέσει το χρώμα", "Γιατί είναι πολύ μεγάλη"], 1, "έχω ήδη μία ίδια"),
  Q("Τι δεν μπορεί να κάνει ο υπάλληλος χωρίς απόδειξη;", ["Να κάνει αλλαγή", "Να ελέγξει το προϊόν", "Να επιστρέψει χρήματα", "Να δώσει κουπόνι"], 2, "Χωρίς απόδειξη δεν μπορώ να σας επιστρέψω χρήματα"),
  Q("Τι ισχύει για το σετ με τα μαχαίρια;", ["Είναι δέκα ευρώ πιο ακριβό", "Κοστίζει όσο και η καφετιέρα", "Είναι σε προσφορά", "Δεν υπάρχει σε απόθεμα"], 0, "Είναι ακριβώς δέκα ευρώ πιο ακριβό"),
 ],
 "gloss": {"πελάτισσα": "πελάτισσα — customer (f.)", "χάρισαν": "χαρίζω — to give (as a present)", "καφετιέρα": "καφετιέρα — coffee maker", "απόδειξη δώρου": "απόδειξη δώρου — gift receipt", "τρέχουσα": "τρέχων — current", "σφραγισμένη": "σφραγισμένος — sealed", "μαχαίρια": "μαχαίρι — knife", "διαφορά": "διαφορά — difference", "κουπόνι": "κουπόνι — voucher", "προσφορά": "προσφορά — special offer"},
})

ITEMS.append({
 "id": "l168-dia-proto-kinito", "title": "Το πρώτο κινητό στα έντεκα;", "title_en": "A first phone at eleven?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο ανάμεσα σε δύο γονείς που συζητούν αν θα πάρουν κινητό στην κόρη τους.",
 "script": [
  L("Μητέρα", "f", "Η Ηλέκτρα μού ζήτησε πάλι κινητό. Λέει ότι όλα τα παιδιά της τάξης έχουν και ότι μένει έξω από τις συζητήσεις τους.", "Ilektra asked me for a phone again. She says all the children in her class have one and that she's left out of their conversations."),
  L("Πατέρας", "m", "Είναι μόλις έντεκα. Διάβαζα ότι πολλοί ειδικοί προτείνουν να περιμένουμε τουλάχιστον μέχρι το γυμνάσιο. Και με ανησυχεί ο χρόνος που θα περνάει στην οθόνη.", "She's only eleven. I was reading that many experts suggest waiting at least until secondary school. And I'm worried about the time she'll spend on the screen."),
  L("Μητέρα", "f", "Κι εμένα. Από την άλλη, από τον Σεπτέμβριο θα πηγαίνει μόνη της στο κολυμβητήριο με το λεωφορείο. Θα ήθελα να μπορώ να τη βρίσκω.", "Me too. On the other hand, from September she'll be going to the pool alone by bus. I'd like to be able to reach her."),
  L("Πατέρας", "m", "Τότε ας της πάρουμε ένα απλό κινητό, μόνο για κλήσεις και μηνύματα, χωρίς διαδίκτυο. Έτσι λύνεται το θέμα της ασφάλειας.", "Then let's get her a simple phone, only for calls and messages, without internet. That solves the safety issue."),
  L("Μητέρα", "f", "Θα το θεωρήσει τιμωρία. Ας κάνουμε μια συμφωνία: έξυπνο κινητό, αλλά με όρια. Το βράδυ θα μένει στην κουζίνα, όχι στο δωμάτιό της, και τα πρώτα μέσα κοινωνικής δικτύωσης στα δεκατρία.", "She'll see it as a punishment. Let's make a deal: a smartphone, but with limits. At night it stays in the kitchen, not in her room, and the first social media at thirteen."),
  L("Πατέρας", "m", "Μου ακούγεται λογικό. Αλλά τη συμφωνία να τη γράψουμε σε χαρτί και να την υπογράψει κι εκείνη. Και εμείς να αφήνουμε τα δικά μας κινητά στην κουζίνα, για να δίνουμε το παράδειγμα.", "Sounds reasonable to me. But let's write the deal on paper and have her sign it too. And we should leave our own phones in the kitchen as well, to set an example."),
 ],
 "questions": [
  Q("Τι ανησυχεί κυρίως τον πατέρα;", ["Το κόστος του κινητού", "Ο χρόνος που θα περνάει η κόρη στην οθόνη", "Ότι θα το χάσει", "Ότι θα παίζει παιχνίδια στο σχολείο"], 1, "με ανησυχεί ο χρόνος που θα περνάει στην οθόνη"),
  Q("Γιατί η μητέρα θέλει να μπορεί να βρίσκει την κόρη τους;", ["Γιατί θα μείνει μόνη στο σπίτι", "Γιατί θα πηγαίνει σε κατασκήνωση", "Γιατί θα πηγαίνει μόνη στο κολυμβητήριο με το λεωφορείο", "Γιατί αλλάζει σχολείο"], 2, "θα πηγαίνει μόνη της στο κολυμβητήριο με το λεωφορείο"),
  Q("Τι προτείνει ο πατέρας στο τέλος;", ["Να γραφτεί η συμφωνία σε χαρτί και να αφήνουν κι εκείνοι τα κινητά τους στην κουζίνα", "Να περιμένουν έναν χρόνο", "Να πάρουν απλό κινητό", "Να αποφασίσει η δασκάλα"], 0, "τη συμφωνία να τη γράψουμε σε χαρτί"),
 ],
 "gloss": {"συζητήσεις": "συζήτηση — conversation", "ειδικοί": "ειδικός — expert", "οθόνη": "οθόνη — screen", "κολυμβητήριο": "κολυμβητήριο — swimming pool", "κλήσεις": "κλήση — call", "διαδίκτυο": "διαδίκτυο — internet", "τιμωρία": "τιμωρία — punishment", "συμφωνία": "συμφωνία — deal, agreement", "όρια": "όριο — limit", "μέσα κοινωνικής δικτύωσης": "μέσα κοινωνικής δικτύωσης — social media", "υπογράψει": "υπογράφω — to sign", "παράδειγμα": "δίνω το παράδειγμα — to set an example"},
})

ITEMS.append({
 "id": "l168-mon-stathero-tilefono", "title": "Γιατί κράτησα το σταθερό τηλέφωνο", "title_en": "Why I kept my landline", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να εξηγεί σε ένα ραδιοφωνικό πρόγραμμα γιατί δεν κατάργησε το σταθερό τηλέφωνο του σπιτιού της.",
 "script": [
  L("Γυναίκα", "f", "Όλοι οι φίλοι μου έχουν καταργήσει το σταθερό. Λένε ότι είναι περιττό έξοδο, αφού όλοι έχουμε κινητά. Κι εγώ το σκεφτόμουν, μέχρι που μια μέρα το κινητό μου χάλασε και έμεινα τρεις μέρες χωρίς τηλέφωνο. Η μητέρα μου, που είναι ογδόντα πέντε, με έπαιρνε στο σταθερό, και ήταν η μόνη που με βρήκε.", "All my friends have got rid of the landline. They say it's an unnecessary expense, since we all have mobiles. I was thinking about it too, until one day my mobile broke and I was left without a phone for three days. My mother, who is eighty-five, called me on the landline, and she was the only one who reached me."),
  L("Γυναίκα", "f", "Υπάρχει όμως και κάτι άλλο. Το σταθερό είναι στον διάδρομο, οπότε όταν μιλάω, δεν κάνω τίποτα άλλο. Δεν κοιτάζω μηνύματα, δεν πλένω πιάτα, δεν περπατάω στον δρόμο. Απλώς κάθομαι στο σκαμπό και ακούω. Οι συζητήσεις μου με τη μητέρα μου έχουν γίνει πιο ουσιαστικές.", "But there's something else too. The landline is in the hallway, so when I talk, I do nothing else. I don't look at messages, I don't wash dishes, I don't walk down the street. I just sit on the stool and listen. My conversations with my mother have become more meaningful."),
  L("Γυναίκα", "f", "Τα παιδιά μου γελάνε. Ο γιος μου με ρώτησε τι είναι αυτός ο ήχος όταν χτύπησε για πρώτη φορά μπροστά του. Δεν ξέρω για πόσο θα το κρατήσω. Αλλά για τώρα, εκείνο το παλιό κουδούνισμα στον διάδρομο μου θυμίζει ότι κάποιος σκέφτηκε να μου μιλήσει πραγματικά.", "My children laugh. My son asked me what that sound was when it rang in front of him for the first time. I don't know how long I'll keep it. But for now, that old ring in the hallway reminds me that someone thought of really talking to me."),
 ],
 "questions": [
  Q("Τι την έκανε να αλλάξει γνώμη για το σταθερό;", ["Μια προσφορά της εταιρείας", "Όταν χάλασε το κινητό της, μόνο η μητέρα της τη βρήκε στο σταθερό", "Μια συμβουλή του γιου της", "Ένα άρθρο που διάβασε"], 1, "με έπαιρνε στο σταθερό, και ήταν η μόνη που με βρήκε"),
  Q("Γιατί λέει ότι οι συζητήσεις της έχουν γίνει πιο ουσιαστικές;", ["Γιατί μιλάει περισσότερη ώρα", "Γιατί η γραμμή είναι πιο καθαρή", "Γιατί όταν μιλάει στο σταθερό δεν κάνει τίποτα άλλο", "Γιατί η μητέρα της ακούει καλύτερα"], 2, "όταν μιλάω, δεν κάνω τίποτα άλλο"),
  Q("Τι ρώτησε ο γιος της;", ["Τι είναι αυτός ο ήχος, όταν χτύπησε το σταθερό", "Γιατί δεν αγοράζει καινούργιο κινητό", "Πόσο κοστίζει το σταθερό", "Ποιος την παίρνει τηλέφωνο"], 0, "Ο γιος μου με ρώτησε τι είναι αυτός ο ήχος"),
 ],
 "gloss": {"κατάργησε": "καταργώ — to abolish, get rid of", "σταθερό": "σταθερό — landline", "καταργήσει": "καταργώ — to abolish, get rid of", "περιττό": "περιττός — unnecessary", "έξοδο": "έξοδο — expense", "διάδρομο": "διάδρομος — hallway", "σκαμπό": "σκαμπό — stool", "ουσιαστικές": "ουσιαστικός — meaningful, substantial", "κουδούνισμα": "κουδούνισμα — ringing"},
})

ITEMS.append({
 "id": "l168-vm-fotografos-apofoitisi", "title": "Μήνυμα από τον φωτογράφο της αποφοίτησης", "title_en": "A message from the graduation photographer", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον φωτογράφο που φωτογράφισε την τελετή αποφοίτησης της κόρης σας.",
 "script": [
  L("Φωτογράφος", "m", "Καλησπέρα σας, ο Νίκος είμαι, ο φωτογράφος από την αποφοίτηση του λυκείου. Οι φωτογραφίες είναι έτοιμες. Έχω ανεβάσει μια επιλογή σε έναν ιδιωτικό σύνδεσμο, που θα σας τον στείλω με μήνυμα, μαζί με τον κωδικό.", "Good evening, it's Nikos, the photographer from the high school graduation. The photos are ready. I've uploaded a selection to a private link, which I'll send you by text, together with the password."),
  L("Φωτογράφος", "m", "Το πακέτο που κλείσατε περιλαμβάνει είκοσι ψηφιακές φωτογραφίες και δύο εκτυπώσεις σε μεγάλο μέγεθος. Διαλέξτε, παρακαλώ, ποιες θέλετε μέχρι την Παρασκευή. Κάθε επιπλέον ψηφιακή φωτογραφία κοστίζει τρία ευρώ.", "The package you booked includes twenty digital photos and two large prints. Please choose which ones you want by Friday. Each extra digital photo costs three euros."),
  L("Φωτογράφος", "m", "Και κάτι ακόμα: έχω μια πολύ ωραία φωτογραφία της κόρης σας τη στιγμή που πετάει το καπέλο στον αέρα. Επειδή πιάνει και άλλους μαθητές στο φόντο, θα ήθελα την άδειά σας για να τη χρησιμοποιήσω στην ιστοσελίδα μου. Αν δεν συμφωνείτε, δεν υπάρχει κανένα πρόβλημα.", "And one more thing: I have a very nice photo of your daughter at the moment she throws her cap in the air. Because it also shows other students in the background, I'd like your permission to use it on my website. If you don't agree, there's no problem at all."),
 ],
 "questions": [
  Q("Πώς θα δείτε τις φωτογραφίες;", ["Στο στούντιο του φωτογράφου", "Σε έναν ιδιωτικό σύνδεσμο με κωδικό", "Σε ένα άλμπουμ που θα σας στείλει", "Στην ιστοσελίδα του σχολείου"], 1, "Έχω ανεβάσει μια επιλογή σε έναν ιδιωτικό σύνδεσμο"),
  Q("Τι περιλαμβάνει το πακέτο;", ["Όλες τις φωτογραφίες της τελετής", "Δέκα εκτυπώσεις", "Είκοσι ψηφιακές φωτογραφίες και δύο μεγάλες εκτυπώσεις", "Ένα βίντεο"], 2, "είκοσι ψηφιακές φωτογραφίες και δύο εκτυπώσεις σε μεγάλο μέγεθος"),
  Q("Για ποιο λόγο ζητάει την άδειά σας;", ["Για να χρησιμοποιήσει μια φωτογραφία στην ιστοσελίδα του", "Για να τη στείλει σε έναν διαγωνισμό", "Για να τη δώσει στο σχολείο", "Για να την τυπώσει σε περιοδικό"], 0, "θα ήθελα την άδειά σας για να τη χρησιμοποιήσω στην ιστοσελίδα μου"),
 ],
 "gloss": {"φωτογράφισε": "φωτογραφίζω — to photograph", "τελετή": "τελετή — ceremony", "αποφοίτησης": "αποφοίτηση — graduation", "αποφοίτηση": "αποφοίτηση — graduation", "ανεβάσει": "ανεβάζω — to upload", "σύνδεσμο": "σύνδεσμος — link", "κωδικό": "κωδικός — password, code", "πακέτο": "πακέτο — package", "ψηφιακές": "ψηφιακός — digital", "εκτυπώσεις": "εκτύπωση — print", "φόντο": "φόντο — background", "άδειά": "άδεια — permission"},
})

ITEMS.append({
 "id": "l168-vm-kathigitria-italikon", "title": "Μήνυμα από την καθηγήτρια ιταλικών", "title_en": "A message from the Italian teacher", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από την καθηγήτρια ιταλικών του γιου σας, λίγο πριν από τις εξετάσεις πιστοποίησης.",
 "script": [
  L("Καθηγήτρια", "f", "Καλημέρα σας, η κυρία Ρένα είμαι, η καθηγήτρια ιταλικών του Άγγελου. Σας τηλεφωνώ για τις εξετάσεις πιστοποίησης του Μαΐου. Η προθεσμία για τις αιτήσεις λήγει την επόμενη Δευτέρα, και δεν έχω λάβει ακόμα τη δική του.", "Good morning, it's Mrs Rena, Angelos's Italian teacher. I'm calling about the certification exams in May. The deadline for applications expires next Monday, and I haven't received his yet."),
  L("Καθηγήτρια", "f", "Ο Άγγελος έχει κάνει μεγάλη πρόοδο, ειδικά στην προφορική έκφραση. Πιστεύω ότι μπορεί άνετα να δώσει για το επίπεδο Β2 και όχι για το Β1, όπως είχαμε συζητήσει στην αρχή της χρονιάς. Θα ήθελα όμως να το αποφασίσουμε μαζί, γιατί το Β2 θέλει περισσότερη δουλειά στην έκθεση.", "Angelos has made great progress, especially in speaking. I believe he can comfortably sit the B2 level and not B1, as we had discussed at the beginning of the year. But I'd like us to decide together, because B2 needs more work on the essay."),
  L("Καθηγήτρια", "f", "Αν συμφωνείτε, μπορούμε να προσθέσουμε ένα επιπλέον μάθημα την εβδομάδα μέχρι τις εξετάσεις, χωρίς χρέωση για τις δύο πρώτες εβδομάδες. Πάρτε με, παρακαλώ, μετά τις πέντε, όταν τελειώνω τα μαθήματα.", "If you agree, we can add an extra lesson a week until the exams, free of charge for the first two weeks. Please call me after five, when I finish my lessons."),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί η καθηγήτρια;", ["Γιατί ο Άγγελος έλειψε από το μάθημα", "Γιατί λήγει η προθεσμία για τις αιτήσεις και δεν έχει λάβει τη δική του", "Γιατί αλλάζει το ωράριο", "Γιατί θέλει να αυξήσει τα δίδακτρα"], 1, "Η προθεσμία για τις αιτήσεις λήγει την επόμενη Δευτέρα, και δεν έχω λάβει ακόμα τη δική του"),
  Q("Τι προτείνει για το επίπεδο;", ["Να δώσει για το Β1", "Να περιμένει έναν χρόνο", "Να δώσει για το Β2", "Να δώσει για το Γ1"], 2, "μπορεί άνετα να δώσει για το επίπεδο Β2"),
  Q("Τι προσφέρει χωρίς χρέωση;", ["Ένα επιπλέον μάθημα την εβδομάδα για τις δύο πρώτες εβδομάδες", "Τα βιβλία της εξέτασης", "Την αίτηση", "Ένα δοκιμαστικό διαγώνισμα"], 0, "χωρίς χρέωση για τις δύο πρώτες εβδομάδες"),
 ],
 "gloss": {"ιταλικών": "ιταλικά — Italian (language)", "πιστοποίησης": "πιστοποίηση — certification", "προθεσμία": "προθεσμία — deadline", "αιτήσεις": "αίτηση — application", "λήγει": "λήγω — to expire", "πρόοδο": "πρόοδος — progress", "προφορική έκφραση": "προφορική έκφραση — speaking", "επίπεδο": "επίπεδο — level", "έκθεση": "έκθεση — essay", "χρέωση": "χρέωση — charge"},
})

ITEMS.append({
 "id": "l168-c1-psevdaisthisi-selinis", "title": "Γιατί το φεγγάρι φαίνεται τεράστιο στον ορίζοντα", "title_en": "Why the moon looks huge on the horizon", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια ερευνήτρια της αντίληψης σε μια εκπομπή για την επιστήμη.",
 "script": [
  L("Δημοσιογράφος", "m", "Όλοι έχουμε δει ένα πανσέληνο φεγγάρι να ανατέλλει τεράστιο πάνω από τη θάλασσα. Τι συμβαίνει;", "We've all seen a full moon rise huge above the sea. What's going on?"),
  L("Ερευνήτρια", "f", "Η απάντηση μάλλον θα σας απογοητεύσει: το φεγγάρι δεν είναι καθόλου μεγαλύτερο. Αν το φωτογραφίσετε στον ορίζοντα και μετά ψηλά στον ουρανό, και συγκρίνετε τις φωτογραφίες, θα δείτε ότι έχει το ίδιο μέγεθος. Μάλιστα, όταν είναι στον ορίζοντα βρίσκεται λίγο πιο μακριά από εμάς, οπότε είναι ελάχιστα μικρότερο. Πρόκειται για ψευδαίσθηση, και την περιγράφουν ήδη αρχαίοι συγγραφείς.", "The answer will probably disappoint you: the moon is not bigger at all. If you photograph it on the horizon and then high in the sky, and compare the photos, you'll see it has the same size. In fact, when it's on the horizon it is a little farther from us, so it's very slightly smaller. It's an illusion, and ancient writers already describe it."),
  L("Δημοσιογράφος", "m", "Δεν φταίει η ατμόσφαιρα, που λειτουργεί σαν φακός;", "Isn't it the atmosphere acting like a lens?"),
  L("Ερευνήτρια", "f", "Αυτή είναι η πιο διαδεδομένη παρανόηση. Η ατμόσφαιρα αλλάζει το χρώμα του φεγγαριού, το κάνει πορτοκαλί, αλλά δεν το μεγεθύνει. Η εξήγηση βρίσκεται στον εγκέφαλό μας. Μια θεωρία λέει ότι αντιλαμβανόμαστε τον ουρανό σαν θόλο πιο πλατύ παρά ψηλό, άρα κρίνουμε ότι ό,τι βρίσκεται στον ορίζοντα είναι πιο μακριά. Ένα αντικείμενο που μοιάζει πιο μακρινό, αλλά έχει το ίδιο μέγεθος στο μάτι, ο εγκέφαλος το «διορθώνει» και το βλέπει μεγαλύτερο. Μια άλλη θεωρία δίνει βάρος στη σύγκριση με δέντρα και σπίτια. Οι επιστήμονες ακόμη συζητούν ποια εξήγηση είναι η σωστή, ή αν παίζουν ρόλο και οι δύο.", "That's the most widespread misconception. The atmosphere changes the moon's colour, makes it orange, but doesn't magnify it. The explanation lies in our brain. One theory says we perceive the sky as a dome that is wider than it is high, so we judge that whatever is on the horizon is farther away. An object that seems farther away but has the same size on the eye, the brain 'corrects' and sees as bigger. Another theory emphasises the comparison with trees and houses. Scientists are still debating which explanation is right, or whether both play a role."),
  L("Δημοσιογράφος", "m", "Μπορούμε να ξεγελάσουμε την ψευδαίσθηση;", "Can we trick the illusion?"),
  L("Ερευνήτρια", "f", "Δοκιμάστε να κοιτάξετε το φεγγάρι μέσα από ένα χάρτινο ρολό, ώστε να μη βλέπετε τίποτε άλλο γύρω του. Οι περισσότεροι λένε ότι ξαφνικά «μικραίνει». Το φεγγάρι δεν άλλαξε· άλλαξαν τα στοιχεία που έδινε το μάτι στον εγκέφαλο.", "Try looking at the moon through a paper tube, so you can't see anything else around it. Most people say it suddenly 'shrinks'. The moon didn't change; what changed was the information the eye gave the brain."),
 ],
 "questions": [
  Q("Τι δείχνουν οι φωτογραφίες του φεγγαριού στον ορίζοντα και ψηλά στον ουρανό;", ["Ότι στον ορίζοντα είναι πολύ μεγαλύτερο", "Ότι έχει το ίδιο μέγεθος", "Ότι ψηλά είναι πολύ μικρότερο", "Ότι αλλάζει σχήμα"], 1, "θα δείτε ότι έχει το ίδιο μέγεθος"),
  Q("Ποιος είναι ο ρόλος της ατμόσφαιρας, σύμφωνα με την ερευνήτρια;", ["Μεγεθύνει το φεγγάρι σαν φακός", "Το κάνει να φαίνεται πιο κοντά", "Αλλάζει το χρώμα του, αλλά δεν το μεγεθύνει", "Δεν παίζει κανέναν ρόλο"], 2, "Η ατμόσφαιρα αλλάζει το χρώμα του φεγγαριού, το κάνει πορτοκαλί, αλλά δεν το μεγεθύνει"),
  Q("Τι συμβαίνει όταν κοιτάξουμε το φεγγάρι μέσα από ένα χάρτινο ρολό;", ["Οι περισσότεροι λένε ότι μικραίνει", "Φαίνεται πιο φωτεινό", "Φαίνεται ακόμη μεγαλύτερο", "Αλλάζει χρώμα"], 0, "Οι περισσότεροι λένε ότι ξαφνικά «μικραίνει»"),
 ],
 "gloss": {"ερευνήτρια": "ερευνήτρια — researcher (f.)", "αντίληψης": "αντίληψη — perception", "πανσέληνο": "πανσέληνος — full (moon)", "ανατέλλει": "ανατέλλω — to rise", "ορίζοντα": "ορίζοντας — horizon", "απογοητεύσει": "απογοητεύω — to disappoint", "ελάχιστα": "ελάχιστα — very slightly", "ψευδαίσθηση": "ψευδαίσθηση — illusion", "φακός": "φακός — lens", "παρανόηση": "παρανόηση — misconception", "μεγεθύνει": "μεγεθύνω — to magnify", "αντιλαμβανόμαστε": "αντιλαμβάνομαι — to perceive", "θόλο": "θόλος — dome", "ξεγελάσουμε": "ξεγελάω — to trick", "ρολό": "ρολό — tube, roll"},
})

ITEMS.append({
 "id": "l168-c1-akyrosi-thoryvou", "title": "Πώς δουλεύουν τα ακουστικά ακύρωσης θορύβου", "title_en": "How noise-cancelling headphones work", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν μηχανικό ήχου να εξηγεί σε ένα ψηφιακό ραδιοφωνικό πρόγραμμα πώς λειτουργούν τα ακουστικά ενεργητικής ακύρωσης θορύβου.",
 "script": [
  L("Μηχανικός", "m", "Ο ήχος είναι ένα κύμα πίεσης στον αέρα, με κορυφές και κοιλάδες. Αν προσθέσουμε σε αυτό το κύμα ένα δεύτερο, ακριβώς ίδιο αλλά ανεστραμμένο, δηλαδή με κοιλάδα εκεί όπου το πρώτο έχει κορυφή, τα δύο αλληλοεξουδετερώνονται. Αυτό το φαινόμενο λέγεται καταστροφική συμβολή. Η ιδέα κατοχυρώθηκε με δίπλωμα ευρεσιτεχνίας ήδη από τη δεκαετία του 1930, αλλά χρειάστηκαν δεκαετίες για να γίνει η τεχνολογία αρκετά γρήγορη και φθηνή.", "Sound is a pressure wave in the air, with peaks and troughs. If we add to this wave a second one, exactly the same but inverted, that is, with a trough where the first has a peak, the two cancel each other out. This phenomenon is called destructive interference. The idea was patented as early as the 1930s, but it took decades for the technology to become fast and cheap enough."),
  L("Μηχανικός", "m", "Στα ακουστικά, μικρά μικρόφωνα πιάνουν συνεχώς τον θόρυβο του περιβάλλοντος. Ένα κύκλωμα υπολογίζει μέσα σε κλάσματα του δευτερολέπτου το ανεστραμμένο κύμα και το στέλνει στο ηχείο, μαζί με τη μουσική. Έτσι ο θόρυβος φτάνει στο αυτί σας εξασθενημένος, ενώ η μουσική μένει ανέπαφη.", "In the headphones, small microphones constantly pick up the ambient noise. A circuit calculates the inverted wave within fractions of a second and sends it to the speaker, together with the music. So the noise reaches your ear weakened, while the music stays intact."),
  L("Μηχανικός", "m", "Η μέθοδος λειτουργεί άριστα με χαμηλούς, σταθερούς ήχους, όπως το βουητό της μηχανής ενός αεροπλάνου. Με ξαφνικούς και ψηλούς ήχους, όπως μια φωνή ή ένα πιάτο που σπάει, τα πάει χειρότερα, γιατί αλλάζουν πολύ γρήγορα. Εκεί βοηθούν κυρίως τα μαξιλαράκια, που κλείνουν μηχανικά το αυτί. Και μια σημείωση: κάποιοι νιώθουν μια περίεργη αίσθηση πίεσης όταν ενεργοποιούν την ακύρωση, σαν να είναι σε αεροπλάνο που κατεβαίνει, παρόλο που η πίεση στο αυτί δεν έχει αλλάξει.", "The method works excellently with low, steady sounds, like the hum of an aeroplane engine. With sudden, high sounds, like a voice or a plate breaking, it does worse, because they change very quickly. There, it's mainly the ear cushions that help, by sealing the ear mechanically. And one note: some people feel a strange sensation of pressure when they switch the cancellation on, as if they were on a descending plane, even though the pressure in the ear hasn't changed."),
 ],
 "questions": [
  Q("Πώς εξουδετερώνεται ο θόρυβος;", ["Με ένα παχύ υλικό που απορροφά τον ήχο", "Προσθέτοντας ένα ανεστραμμένο κύμα που τον ακυρώνει", "Δυναμώνοντας πολύ τη μουσική", "Κλείνοντας τα μικρόφωνα"], 1, "Αν προσθέσουμε σε αυτό το κύμα ένα δεύτερο, ακριβώς ίδιο αλλά ανεστραμμένο"),
  Q("Με ποιους ήχους λειτουργεί καλύτερα η ενεργητική ακύρωση;", ["Με τις φωνές", "Με ξαφνικούς θορύβους", "Με χαμηλούς, σταθερούς ήχους, όπως το βουητό μιας μηχανής", "Με τα σπασμένα πιάτα"], 2, "Η μέθοδος λειτουργεί άριστα με χαμηλούς, σταθερούς ήχους"),
  Q("Τι ισχύει για την αίσθηση πίεσης που νιώθουν κάποιοι;", ["Η πίεση στο αυτί δεν έχει στην πραγματικότητα αλλάξει", "Οφείλεται σε βλάβη των ακουστικών", "Είναι επικίνδυνη για την ακοή", "Εμφανίζεται μόνο στα αεροπλάνα"], 0, "παρόλο που η πίεση στο αυτί δεν έχει αλλάξει"),
 ],
 "gloss": {"ακουστικά": "ακουστικά — headphones", "ενεργητικής": "ενεργητικός — active", "ακύρωσης": "ακύρωση — cancellation", "θορύβου": "θόρυβος — noise", "πίεσης": "πίεση — pressure", "κοιλάδες": "κοιλάδα — trough (of a wave)", "ανεστραμμένο": "ανεστραμμένος — inverted", "αλληλοεξουδετερώνονται": "αλληλοεξουδετερώνομαι — to cancel each other out", "συμβολή": "συμβολή — interference", "δίπλωμα ευρεσιτεχνίας": "δίπλωμα ευρεσιτεχνίας — patent", "κύκλωμα": "κύκλωμα — circuit", "κλάσματα": "κλάσμα — fraction", "ηχείο": "ηχείο — speaker", "εξασθενημένος": "εξασθενημένος — weakened", "ανέπαφη": "ανέπαφος — intact", "βουητό": "βουητό — hum, drone", "μαξιλαράκια": "μαξιλαράκι — cushion"},
})

rnd = random.Random(168)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-168.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
