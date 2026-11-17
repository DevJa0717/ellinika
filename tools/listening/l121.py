# Source for library/listening/listening-121.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l121.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l121-ann-leoforeia-anti-trenou", "title": "Λεωφορεία αντί για τρένα λόγω εργασιών", "title_en": "Buses instead of trains because of engineering work", "type": "announcement", "level": "B2",
 "context_el": "Περιμένετε σε έναν σιδηροδρομικό σταθμό. Ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Υπάλληλος", "f", "Αγαπητοί επιβάτες, λόγω εργασιών στη σιδηροδρομική γραμμή, από αύριο Σάββατο και για τρεις εβδομάδες, τα δρομολόγια ανάμεσα στον σταθμό μας και στην Κόρινθο θα εκτελούνται με λεωφορεία. Τα λεωφορεία θα αναχωρούν από τον χώρο στάθμευσης μπροστά από την κεντρική είσοδο.", "Dear passengers, because of work on the railway line, from tomorrow, Saturday, and for three weeks, services between our station and Corinth will be operated by buses. The buses will depart from the car park in front of the main entrance."),
  L("Υπάλληλος", "f", "Παρακαλούμε να υπολογίσετε περίπου σαράντα λεπτά επιπλέον στη διάρκεια του ταξιδιού. Τα εισιτήρια που έχετε ήδη αγοράσει ισχύουν κανονικά και για τα λεωφορεία, χωρίς καμία επιβάρυνση.", "Please allow about forty minutes extra for the journey. Tickets you have already bought are valid on the buses as normal, at no extra charge."),
  L("Υπάλληλος", "f", "Στα λεωφορεία δεν επιτρέπονται ποδήλατα, εκτός από τα πτυσσόμενα. Επιβάτες με αναπηρικό αμαξίδιο παρακαλούνται να ενημερώσουν το εκδοτήριο μία μέρα νωρίτερα, ώστε να εξασφαλιστεί κατάλληλο όχημα.", "Bicycles are not allowed on the buses, except folding ones. Passengers using a wheelchair are asked to inform the ticket office a day in advance, so that a suitable vehicle can be arranged."),
 ],
 "questions": [
  Q("Από πού θα αναχωρούν τα λεωφορεία;", ["Από την αποβάθρα 1", "Από τον χώρο στάθμευσης μπροστά από την κεντρική είσοδο", "Από την πλατεία της πόλης", "Από τον σταθμό των ΚΤΕΛ"], 1, "Τα λεωφορεία θα αναχωρούν από τον χώρο στάθμευσης μπροστά από την κεντρική είσοδο"),
  Q("Τι ισχύει για τα εισιτήρια που έχουν ήδη αγοραστεί;", ["Πρέπει να αλλαχτούν στο εκδοτήριο", "Επιστρέφονται τα χρήματα", "Ισχύουν κανονικά και για τα λεωφορεία, χωρίς επιβάρυνση", "Ισχύουν με μια μικρή επιβάρυνση"], 2, "Τα εισιτήρια που έχετε ήδη αγοράσει ισχύουν κανονικά και για τα λεωφορεία"),
  Q("Τι πρέπει να κάνουν οι επιβάτες με αναπηρικό αμαξίδιο;", ["Να ενημερώσουν το εκδοτήριο μία μέρα νωρίτερα", "Να πάρουν ταξί με έξοδα του σιδηροδρόμου", "Να ταξιδέψουν μετά από τρεις εβδομάδες", "Να έρθουν μία ώρα νωρίτερα στον σταθμό"], 0, "παρακαλούνται να ενημερώσουν το εκδοτήριο μία μέρα νωρίτερα"),
 ],
 "gloss": {"σιδηροδρομικό": "σιδηροδρομικός — railway (adj.)", "δρομολόγια": "δρομολόγιο — service, scheduled trip", "εκτελούνται": "εκτελούμαι — to be operated, carried out", "χώρο στάθμευσης": "χώρος στάθμευσης — car park", "υπολογίσετε": "υπολογίζω — to allow for, calculate", "επιβάρυνση": "επιβάρυνση — extra charge", "πτυσσόμενα": "πτυσσόμενος — folding", "αναπηρικό αμαξίδιο": "αναπηρικό αμαξίδιο — wheelchair", "εκδοτήριο": "εκδοτήριο — ticket office", "όχημα": "όχημα — vehicle"}
})

ITEMS.append({
 "id": "l121-vm-theatriki-omada", "title": "Μήνυμα από τη θεατρική ομάδα του δήμου", "title_en": "A message from the municipal theatre group", "type": "voicemail", "level": "B2",
 "context_el": "Είστε μέλος μιας ερασιτεχνικής θεατρικής ομάδας. Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη σκηνοθέτιδα.",
 "script": [
  L("Σκηνοθέτιδα", "f", "Γεια σου, η Ρένα είμαι. Σε παίρνω για να σου πω ότι η πρόβα της Πέμπτης μεταφέρεται την Τετάρτη, στις επτά, γιατί την Πέμπτη η αίθουσα χρειάζεται για μια συναυλία. Θα δουλέψουμε κυρίως τη δεύτερη πράξη, που είναι ακόμα αδύναμη.", "Hi, it's Rena. I'm calling to tell you that Thursday's rehearsal is moving to Wednesday, at seven, because on Thursday the hall is needed for a concert. We'll mainly work on the second act, which is still weak."),
  L("Σκηνοθέτιδα", "f", "Θα ήθελα να ξέρεις τον μονόλογό σου απέξω ως τότε, χωρίς το κείμενο στο χέρι. Αν δυσκολεύεσαι, ηχογράφησε τις ατάκες των άλλων στο κινητό σου και κάνε πρόβα μαζί τους. Εμένα με βοηθούσε πολύ αυτό.", "I'd like you to know your monologue by heart by then, without the script in your hand. If you're finding it hard, record the others' lines on your phone and rehearse with them. That helped me a lot."),
  L("Σκηνοθέτιδα", "f", "Και κάτι ακόμα: η κυρία από το βεστιάριο θέλει να σου πάρει μέτρα για το κοστούμι. Φέρε μαζί σου τα μαύρα παπούτσια που μου είπες, για να δούμε αν ταιριάζουν. Τα λέμε την Τετάρτη!", "And one more thing: the lady from the wardrobe wants to take your measurements for the costume. Bring the black shoes you told me about, so we can see if they go with it. See you on Wednesday!"),
 ],
 "questions": [
  Q("Γιατί μεταφέρεται η πρόβα;", ["Γιατί η σκηνοθέτιδα είναι άρρωστη", "Γιατί την Πέμπτη η αίθουσα χρειάζεται για μια συναυλία", "Γιατί λείπουν πολλοί ηθοποιοί", "Γιατί η παράσταση πήρε αναβολή"], 1, "την Πέμπτη η αίθουσα χρειάζεται για μια συναυλία"),
  Q("Τι συμβουλεύει η Ρένα για τον μονόλογο;", ["Να τον διαβάζει πριν κοιμηθεί", "Να τον γράψει πολλές φορές", "Να ηχογραφήσει τις ατάκες των άλλων και να κάνει πρόβα μαζί τους", "Να τον πει μπροστά στον καθρέφτη"], 2, "ηχογράφησε τις ατάκες των άλλων στο κινητό σου και κάνε πρόβα μαζί τους"),
  Q("Τι πρέπει να φέρει ο ακροατής την Τετάρτη;", ["Τα μαύρα παπούτσια", "Το κοστούμι του", "Το κείμενο του έργου", "Ένα καπέλο"], 0, "Φέρε μαζί σου τα μαύρα παπούτσια"),
 ],
 "gloss": {"ερασιτεχνικής": "ερασιτεχνικός — amateur", "σκηνοθέτιδα": "σκηνοθέτιδα — (female) director", "πρόβα": "πρόβα — rehearsal", "αίθουσα": "αίθουσα — hall", "πράξη": "πράξη — act", "μονόλογό": "μονόλογος — monologue", "απέξω": "απέξω — by heart", "ατάκες": "ατάκα — line (in a play)", "βεστιάριο": "βεστιάριο — wardrobe (theatre)", "μέτρα": "παίρνω μέτρα — to take measurements"}
})

ITEMS.append({
 "id": "l121-dial-agora-i-enoikio", "title": "Αγοράζουμε ή συνεχίζουμε να νοικιάζουμε;", "title_en": "Buy or keep renting?", "type": "dialogue", "level": "B2",
 "context_el": "Ο Κώστας και η Δέσποινα, ένα ζευγάρι τριάντα πέντε χρονών, συζητούν αν πρέπει να αγοράσουν δικό τους διαμέρισμα.",
 "script": [
  L("Κώστας", "m", "Δέσποινα, ο ιδιοκτήτης μάς ανέβασε πάλι το ενοίκιο. Πληρώνουμε σχεδόν όσο θα πληρώναμε τη δόση ενός δανείου. Μήπως ήρθε η ώρα να αγοράσουμε κάτι δικό μας;", "Despina, the landlord has put the rent up again. We pay almost as much as we'd pay for a mortgage instalment. Maybe it's time to buy a place of our own?"),
  L("Δέσποινα", "f", "Το έχω σκεφτεί κι εγώ. Αλλά ένα δάνειο είναι δέσμευση για είκοσι πέντε χρόνια. Κι αν χρειαστεί να αλλάξουμε πόλη για δουλειά; Με το ενοίκιο είμαστε πιο ελεύθεροι.", "I've thought about it too. But a loan is a commitment for twenty-five years. And what if we need to move city for work? With renting we're freer."),
  L("Κώστας", "m", "Αν χρειαστεί να φύγουμε, μπορούμε να το νοικιάσουμε. Και κάποια στιγμή θα το έχουμε ξεπληρώσει, ενώ τα ενοίκια είναι χρήματα που δεν θα τα ξαναδούμε ποτέ.", "If we need to leave, we can rent it out. And at some point we'll have paid it off, whereas rent is money we'll never see again."),
  L("Δέσποινα", "f", "Σωστό. Το πρόβλημα είναι η προκαταβολή. Τα χρήματα που έχουμε στην άκρη φτάνουν μόνο για το ένα πέμπτο της τιμής. Πριν αποφασίσουμε, ας μιλήσουμε με έναν σύμβουλο στην τράπεζα να δούμε τι δάνειο μπορούμε πραγματικά να αντέξουμε.", "True. The problem is the down payment. The money we have put aside is only enough for a fifth of the price. Before we decide, let's talk to an adviser at the bank to see what loan we can really afford."),
 ],
 "questions": [
  Q("Γιατί ο Κώστας σκέφτεται να αγοράσουν σπίτι;", ["Γιατί κληρονόμησαν χρήματα", "Γιατί ο ιδιοκτήτης ανέβασε πάλι το ενοίκιο", "Γιατί θέλουν μεγαλύτερο σπίτι", "Γιατί θα κάνουν παιδί"], 1, "ο ιδιοκτήτης μάς ανέβασε πάλι το ενοίκιο"),
  Q("Ποιο είναι το επιχείρημα της Δέσποινας υπέρ του ενοικίου;", ["Ότι είναι πιο φθηνό", "Ότι ο ιδιοκτήτης κάνει τις επισκευές", "Ότι με το ενοίκιο είναι πιο ελεύθεροι αν χρειαστεί να αλλάξουν πόλη", "Ότι τα σπίτια θα φθηνύνουν"], 2, "Με το ενοίκιο είμαστε πιο ελεύθεροι"),
  Q("Τι προτείνει η Δέσποινα στο τέλος;", ["Να μιλήσουν με έναν σύμβουλο στην τράπεζα", "Να ψάξουν φθηνότερο σπίτι για ενοίκιο", "Να περιμένουν δύο χρόνια", "Να ζητήσουν δανεικά από τους γονείς τους"], 0, "ας μιλήσουμε με έναν σύμβουλο στην τράπεζα"),
 ],
 "gloss": {"διαμέρισμα": "διαμέρισμα — flat, apartment", "ιδιοκτήτης": "ιδιοκτήτης — landlord, owner", "ενοίκιο": "ενοίκιο — rent", "δόση": "δόση — instalment", "δανείου": "δάνειο — loan, mortgage", "δέσμευση": "δέσμευση — commitment", "ξεπληρώσει": "ξεπληρώνω — to pay off", "προκαταβολή": "προκαταβολή — down payment, deposit", "στην άκρη": "βάζω στην άκρη — to put aside (money)", "αντέξουμε": "αντέχω — to afford, bear"}
})

ITEMS.append({
 "id": "l121-int-xenagos-orycheiou", "title": "Ξεναγός σε ένα παλιό ορυχείο", "title_en": "A guide in an old mine", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με τον Αντώνη, ξεναγό σε ένα παλιό μεταλλείο που έγινε μουσείο.",
 "script": [
  L("Δημοσιογράφος", "f", "Αντώνη, το μεταλλείο έκλεισε πριν από πενήντα χρόνια. Τι βλέπει σήμερα ο επισκέπτης;", "Antonis, the mine closed fifty years ago. What does the visitor see today?"),
  L("Αντώνης", "m", "Οι επισκέπτες φορούν κράνος και μπαίνουν σε μια στοά τριακοσίων μέτρων. Βλέπουν τις ράγες όπου κυλούσαν τα βαγονέτα, τα εργαλεία των μεταλλωρύχων και τα σημάδια από τις αξίνες στους τοίχους. Το πιο εντυπωσιακό, όμως, είναι η σιωπή και το σκοτάδι, όταν σβήνουμε για λίγα δευτερόλεπτα τα φώτα.", "Visitors wear a helmet and go into a gallery three hundred metres long. They see the rails where the mine carts rolled, the miners' tools and the marks of the picks on the walls. The most striking thing, though, is the silence and the darkness when we switch off the lights for a few seconds."),
  L("Δημοσιογράφος", "f", "Έχετε προσωπική σχέση με το μεταλλείο;", "Do you have a personal connection with the mine?"),
  L("Αντώνης", "m", "Ο παππούς μου δούλευε εδώ τριάντα χρόνια. Μου έλεγε ότι έβγαιναν από τη στοά μαύροι από τη σκόνη και ότι πολλοί συνάδελφοί του αρρώστησαν από τους πνεύμονες. Γι’ αυτό, στην ξενάγηση δεν μιλάω μόνο για τα ορυκτά, αλλά και για τους ανθρώπους.", "My grandfather worked here for thirty years. He told me that they came out of the gallery black with dust and that many of his colleagues got lung disease. That's why on the tour I don't just talk about the minerals, but also about the people."),
  L("Δημοσιογράφος", "f", "Ποιοι έρχονται περισσότερο;", "Who comes most?"),
  L("Αντώνης", "m", "Πολλά σχολεία, και αυτό με χαροποιεί. Τα παιδιά συνήθως ρωτούν αν υπάρχουν ακόμα θησαυροί μέσα. Τους απαντώ ότι ο μεγαλύτερος θησαυρός είναι οι ιστορίες των ανθρώπων που δούλεψαν εδώ.", "Many schools, and that makes me glad. The children usually ask if there are still treasures inside. I answer that the greatest treasure is the stories of the people who worked here."),
 ],
 "questions": [
  Q("Τι είναι, κατά τον Αντώνη, το πιο εντυπωσιακό στην ξενάγηση;", ["Τα ορυκτά στους τοίχους", "Η σιωπή και το σκοτάδι όταν σβήνουν τα φώτα", "Τα βαγονέτα", "Η θέα από την είσοδο"], 1, "Το πιο εντυπωσιακό, όμως, είναι η σιωπή και το σκοτάδι"),
  Q("Γιατί ο Αντώνης μιλάει στην ξενάγηση και για τους ανθρώπους;", ["Γιατί του το ζήτησε ο δήμος", "Γιατί τα ορυκτά δεν ενδιαφέρουν κανέναν", "Γιατί ο παππούς του δούλευε εκεί και πολλοί συνάδελφοί του αρρώστησαν", "Γιατί έχει σπουδάσει ιστορία"], 2, "Ο παππούς μου δούλευε εδώ τριάντα χρόνια"),
  Q("Τι απαντά στα παιδιά που ρωτούν για θησαυρούς;", ["Ότι ο μεγαλύτερος θησαυρός είναι οι ιστορίες των ανθρώπων", "Ότι οι θησαυροί είναι στο μουσείο της πόλης", "Ότι υπάρχει χρυσάφι βαθιά μέσα", "Ότι οι θησαυροί είναι μύθος"], 0, "ο μεγαλύτερος θησαυρός είναι οι ιστορίες των ανθρώπων που δούλεψαν εδώ"),
 ],
 "gloss": {"μεταλλείο": "μεταλλείο — mine", "κράνος": "κράνος — helmet", "στοά": "στοά — gallery, tunnel", "ράγες": "ράγα — rail", "βαγονέτα": "βαγονέτο — mine cart", "μεταλλωρύχων": "μεταλλωρύχος — miner", "αξίνες": "αξίνα — pick(axe)", "σκόνη": "σκόνη — dust", "πνεύμονες": "πνεύμονας — lung", "ορυκτά": "ορυκτό — mineral", "χαροποιεί": "χαροποιώ — to make glad"}
})

ITEMS.append({
 "id": "l121-rep-trapeza-trofimon", "title": "Η τράπεζα τροφίμων της πόλης", "title_en": "The city's food bank", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε τοπικό ραδιόφωνο για την τράπεζα τροφίμων μιας πόλης.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε μια αποθήκη στη βιομηχανική περιοχή, είκοσι εθελοντές ταξινομούν κιβώτια με μακαρόνια, όσπρια, γάλα και κονσέρβες. Είναι η τράπεζα τροφίμων της πόλης, που μαζεύει τρόφιμα από σούπερ μάρκετ, εταιρείες και ιδιώτες και τα μοιράζει σε οικογένειες που τα έχουν ανάγκη.", "In a warehouse in the industrial area, twenty volunteers are sorting boxes of pasta, pulses, milk and tins. This is the city's food bank, which collects food from supermarkets, companies and private individuals and distributes it to families in need."),
  L("Ρεπόρτερ", "m", "Πολλά από τα προϊόντα είναι απολύτως κατάλληλα, αλλά πλησιάζουν την ημερομηνία λήξης ή έχουν μια μικρή ζημιά στη συσκευασία, και τα καταστήματα δεν μπορούν πια να τα πουλήσουν. Έτσι, η τράπεζα τροφίμων μειώνει και τη σπατάλη: αντί να πεταχτούν, τα τρόφιμα φτάνουν σε ένα τραπέζι.", "Many of the products are perfectly fine but are close to their best-before date or have slight damage to the packaging, and the shops can no longer sell them. So the food bank also reduces waste: instead of being thrown away, the food reaches a table."),
  L("Ρεπόρτερ", "m", "Οι οικογένειες που βοηθιούνται είναι πάνω από τετρακόσιες, και ο αριθμός αυξάνεται. Οι υπεύθυνοι λένε ότι χρειάζονται κυρίως εθελοντές με δίπλωμα οδήγησης για τις παραλαβές και ένα δεύτερο ψυγείο για τα φρέσκα προϊόντα.", "The families being helped number over four hundred, and the number is growing. Those in charge say they mainly need volunteers with a driving licence for the collections and a second fridge for fresh products."),
 ],
 "questions": [
  Q("Από πού μαζεύει τρόφιμα η τράπεζα τροφίμων;", ["Μόνο από τον δήμο", "Από σούπερ μάρκετ, εταιρείες και ιδιώτες", "Από τα σχολεία", "Από αγρότες της περιοχής"], 1, "μαζεύει τρόφιμα από σούπερ μάρκετ, εταιρείες και ιδιώτες"),
  Q("Γιατί τα καταστήματα δεν μπορούν να πουλήσουν πολλά από αυτά τα προϊόντα;", ["Γιατί είναι χαλασμένα", "Γιατί είναι πολύ ακριβά", "Γιατί πλησιάζουν την ημερομηνία λήξης ή έχουν μικρή ζημιά στη συσκευασία", "Γιατί δεν τα ζητάει κανείς"], 2, "πλησιάζουν την ημερομηνία λήξης ή έχουν μια μικρή ζημιά στη συσκευασία"),
  Q("Τι χρειάζεται κυρίως η τράπεζα τροφίμων;", ["Εθελοντές με δίπλωμα οδήγησης και ένα δεύτερο ψυγείο", "Χρήματα για ενοίκιο", "Μεγαλύτερη αποθήκη", "Περισσότερα όσπρια"], 0, "εθελοντές με δίπλωμα οδήγησης για τις παραλαβές και ένα δεύτερο ψυγείο"),
 ],
 "gloss": {"τράπεζα τροφίμων": "τράπεζα τροφίμων — food bank", "αποθήκη": "αποθήκη — warehouse", "ταξινομούν": "ταξινομώ — to sort", "κιβώτια": "κιβώτιο — box, crate", "όσπρια": "όσπρια — pulses", "κονσέρβες": "κονσέρβα — tin, can", "ιδιώτες": "ιδιώτης — private individual", "ημερομηνία λήξης": "ημερομηνία λήξης — expiry / best-before date", "συσκευασία": "συσκευασία — packaging", "σπατάλη": "σπατάλη — waste", "παραλαβές": "παραλαβή — collection, pick-up"}
})

ITEMS.append({
 "id": "l121-rep-kolymbi-paidia-prosfygon", "title": "Μαθήματα κολύμβησης για παιδιά προσφύγων", "title_en": "Swimming lessons for refugee children", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα πρόγραμμα κολύμβησης για παιδιά προσφύγων σε ένα νησί του Αιγαίου.",
 "script": [
  L("Ρεπόρτερ", "f", "Για πολλά από τα παιδιά που ζουν στη δομή φιλοξενίας του νησιού, η θάλασσα δεν ήταν ποτέ τόπος παιχνιδιού. Κάποια τη διέσχισαν με βάρκες, μέσα στη νύχτα, και τη φοβούνται ακόμα. Ένας τοπικός ναυτικός όμιλος αποφάσισε να τα βοηθήσει να τη δουν με άλλα μάτια.", "For many of the children living in the island's reception centre, the sea was never a place to play. Some crossed it in boats, at night, and are still afraid of it. A local sailing club decided to help them see it differently."),
  L("Ρεπόρτερ", "f", "Δύο φορές την εβδομάδα, προπονητές του ομίλου δίνουν δωρεάν μαθήματα κολύμβησης σε τριάντα παιδιά, από έξι έως δεκατεσσάρων χρονών. Τα πρώτα μαθήματα γίνονται στα ρηχά, χωρίς βιασύνη. «Κάποια παιδιά χρειάστηκαν τρεις εβδομάδες μόνο για να βάλουν το πρόσωπο στο νερό», λέει μια προπονήτρια.", "Twice a week, the club's coaches give free swimming lessons to thirty children, from six to fourteen years old. The first lessons take place in the shallows, without hurrying. \"Some children needed three weeks just to put their face in the water\", says one coach."),
  L("Ρεπόρτερ", "f", "Στα μαθήματα συμμετέχουν και παιδιά του νησιού, και πολλές φιλίες έχουν γεννηθεί στο νερό. Στο τέλος του καλοκαιριού, τα παιδιά πήραν μέρος σε έναν μικρό αγώνα κολύμβησης, και οι γονείς τους τα χειροκροτούσαν από την ακτή.", "Children from the island also take part in the lessons, and many friendships have been born in the water. At the end of the summer, the children took part in a small swimming race, and their parents applauded them from the shore."),
 ],
 "questions": [
  Q("Γιατί πολλά παιδιά φοβούνται τη θάλασσα;", ["Γιατί δεν έχουν δει ποτέ θάλασσα", "Γιατί κάποια τη διέσχισαν με βάρκες μέσα στη νύχτα", "Γιατί είχαν πνιγεί φίλοι τους στην πισίνα", "Γιατί η θάλασσα του νησιού είναι επικίνδυνη"], 1, "Κάποια τη διέσχισαν με βάρκες, μέσα στη νύχτα, και τη φοβούνται ακόμα"),
  Q("Πώς γίνονται τα πρώτα μαθήματα;", ["Σε κλειστή πισίνα", "Από βάρκα, στα βαθιά", "Στα ρηχά, χωρίς βιασύνη", "Μόνο στη στεριά, με ασκήσεις"], 2, "Τα πρώτα μαθήματα γίνονται στα ρηχά, χωρίς βιασύνη"),
  Q("Τι έγινε στο τέλος του καλοκαιριού;", ["Τα παιδιά πήραν μέρος σε έναν μικρό αγώνα κολύμβησης", "Το πρόγραμμα σταμάτησε", "Τα παιδιά πήγαν εκδρομή με ιστιοφόρο", "Ο όμιλος πήρε ένα βραβείο"], 0, "τα παιδιά πήραν μέρος σε έναν μικρό αγώνα κολύμβησης"),
 ],
 "gloss": {"προσφύγων": "πρόσφυγας — refugee", "δομή φιλοξενίας": "δομή φιλοξενίας — reception centre", "διέσχισαν": "διασχίζω — to cross", "ναυτικός όμιλος": "ναυτικός όμιλος — sailing club", "προπονητές": "προπονητής — coach", "ρηχά": "τα ρηχά — the shallows", "βιασύνη": "βιασύνη — hurry, haste", "φιλίες": "φιλία — friendship", "χειροκροτούσαν": "χειροκροτώ — to applaud", "ακτή": "ακτή — shore"}
})

ITEMS.append({
 "id": "l121-mon-cheimonas-schoinousa", "title": "Ένας χειμώνας στη Σχοινούσα", "title_en": "A winter on Schinoussa", "type": "monologue", "level": "B2",
 "context_el": "Η Αλεξάνδρα, γραφίστρια από την Αθήνα, διηγείται πώς πέρασε έναν ολόκληρο χειμώνα σε ένα μικρό νησί των Κυκλάδων.",
 "script": [
  L("Αλεξάνδρα", "f", "Δουλεύω από το σπίτι, οπότε πέρσι αποφάσισα να δοκιμάσω κάτι τρελό: να περάσω τον χειμώνα στη Σχοινούσα, ένα νησάκι με λίγες εκατοντάδες κατοίκους. Τον Αύγουστο ήταν γεμάτο τουρίστες. Τον Νοέμβριο είχαμε μείνει μόνο οι ντόπιοι κι εγώ.", "I work from home, so last year I decided to try something crazy: to spend the winter on Schinoussa, a little island with a few hundred inhabitants. In August it was full of tourists. By November only the locals and I were left."),
  L("Αλεξάνδρα", "f", "Τις πρώτες εβδομάδες ένιωθα πολύ μόνη. Τα μαγαζιά είχαν κλείσει, το πλοίο ερχόταν λίγες φορές την εβδομάδα και, όταν φυσούσε, καθόλου. Μια φορά μείναμε πέντε μέρες χωρίς φρέσκα λαχανικά. Έμαθα να ψωνίζω για δέκα μέρες και να μην πετάω τίποτα.", "In the first weeks I felt very lonely. The shops had closed, the boat came a few times a week and, when it was windy, not at all. Once we went five days without fresh vegetables. I learned to shop for ten days at a time and not to throw anything away."),
  L("Αλεξάνδρα", "f", "Σιγά σιγά όμως με δέχτηκαν. Η κυρία Ουρανία μού έμαθε να φτιάχνω τυρί, και τα βράδια μαζευόμασταν στο μοναδικό καφενείο που έμενε ανοιχτό. Τον Μάρτιο, όταν γύρισα στην Αθήνα, ένιωθα σαν να άφηνα το σπίτι μου. Φέτος θα ξαναπάω.", "But little by little they accepted me. Mrs Ourania taught me to make cheese, and in the evenings we gathered at the only café that stayed open. In March, when I went back to Athens, I felt as if I were leaving my home. This year I'm going again."),
 ],
 "questions": [
  Q("Γιατί μπόρεσε η Αλεξάνδρα να περάσει τον χειμώνα στο νησί;", ["Γιατί πήρε άδεια από τη δουλειά", "Γιατί δουλεύει από το σπίτι", "Γιατί είναι συνταξιούχος", "Γιατί βρήκε δουλειά στο νησί"], 1, "Δουλεύω από το σπίτι"),
  Q("Τι έμαθε να κάνει εξαιτίας του πλοίου;", ["Να μαγειρεύει ψάρια", "Να ψαρεύει", "Να ψωνίζει για δέκα μέρες και να μην πετάει τίποτα", "Να καλλιεργεί λαχανικά"], 2, "Έμαθα να ψωνίζω για δέκα μέρες και να μην πετάω τίποτα"),
  Q("Πώς ένιωσε όταν γύρισε στην Αθήνα;", ["Σαν να άφηνε το σπίτι της", "Ανακουφισμένη", "Κουρασμένη", "Αδιάφορη"], 0, "ένιωθα σαν να άφηνα το σπίτι μου"),
 ],
 "gloss": {"γραφίστρια": "γραφίστρια — (female) graphic designer", "νησάκι": "νησάκι — little island", "ντόπιοι": "ντόπιος — local", "φυσούσε": "φυσάει — it is windy", "ψωνίζω": "ψωνίζω — to shop", "δέχτηκαν": "δέχομαι — to accept", "μαζευόμασταν": "μαζεύομαι — to gather", "μοναδικό": "μοναδικός — only, single"}
})

ITEMS.append({
 "id": "l121-mon-anoigo-fyllo", "title": "Έμαθα να ανοίγω φύλλο για πίτα", "title_en": "I learned to roll out filo for pies", "type": "monologue", "level": "B2",
 "context_el": "Ο Στέφανος, μηχανικός σαράντα χρονών, μιλάει σε μια εκπομπή μαγειρικής για ένα παλιό οικογενειακό μυστικό.",
 "script": [
  L("Στέφανος", "m", "Η γιαγιά μου από τα Γιάννενα άνοιγε φύλλο με τον πλάστη πάνω σε ένα μεγάλο στρογγυλό τραπέζι. Το έκανε τόσο λεπτό, που μπορούσες να διαβάσεις εφημερίδα από κάτω. Όταν πέθανε, κατάλαβα ότι κανείς στην οικογένεια δεν είχε μάθει να το κάνει.", "My grandmother from Ioannina used to roll out filo with a rolling pin on a big round table. She made it so thin that you could read a newspaper through it. When she died, I realised that nobody in the family had learned to do it."),
  L("Στέφανος", "m", "Έτσι, στα τριάντα οκτώ μου, γράφτηκα σε ένα εργαστήρι με μια κυρία που ήξερε την τέχνη. Τα πρώτα φύλλα μου σκίζονταν συνέχεια ή έβγαιναν χοντρά σαν χαρτόνι. Το μυστικό, μου είπε, είναι το ζύμωμα και η υπομονή: η ζύμη πρέπει να ξεκουραστεί πριν την ανοίξεις.", "So, at thirty-eight, I signed up for a workshop with a lady who knew the craft. My first sheets kept tearing or came out as thick as cardboard. The secret, she told me, is the kneading and patience: the dough must rest before you roll it out."),
  L("Στέφανος", "m", "Χρειάστηκα σχεδόν έναν χρόνο για να φτιάξω μια πίτα που να μοιάζει με της γιαγιάς. Δεν είναι ακόμα τέλεια, αλλά όταν την έφερα στο τραπέζι την Πρωτοχρονιά, η μητέρα μου δάκρυσε. Τώρα μαθαίνω την τέχνη στον γιο μου, για να μη χαθεί ξανά.", "It took me almost a year to make a pie that resembled my grandmother's. It's not perfect yet, but when I brought it to the table on New Year's Day, my mother had tears in her eyes. Now I'm teaching the craft to my son, so that it won't be lost again."),
 ],
 "questions": [
  Q("Τι κατάλαβε ο Στέφανος όταν πέθανε η γιαγιά του;", ["Ότι είχε χαθεί η συνταγή της", "Ότι κανείς στην οικογένεια δεν είχε μάθει να ανοίγει φύλλο", "Ότι ο πλάστης της είχε χαθεί", "Ότι δεν του άρεσε η πίτα"], 1, "κανείς στην οικογένεια δεν είχε μάθει να το κάνει"),
  Q("Ποιο είναι το μυστικό, σύμφωνα με τη δασκάλα του;", ["Το καλό αλεύρι", "Ο ζεστός φούρνος", "Το ζύμωμα και η υπομονή", "Ένας ειδικός πλάστης"], 2, "Το μυστικό, μου είπε, είναι το ζύμωμα και η υπομονή"),
  Q("Γιατί μαθαίνει τώρα την τέχνη στον γιο του;", ["Για να μη χαθεί ξανά", "Για να ανοίξει μαγαζί", "Γιατί του το ζήτησε η μητέρα του", "Για να λάβει μέρος σε διαγωνισμό"], 0, "για να μη χαθεί ξανά"),
 ],
 "gloss": {"άνοιγε φύλλο": "ανοίγω φύλλο — to roll out filo pastry", "πλάστη": "πλάστης — rolling pin", "στρογγυλό": "στρογγυλός — round", "εργαστήρι": "εργαστήρι — workshop", "σκίζονταν": "σκίζομαι — to tear", "χαρτόνι": "χαρτόνι — cardboard", "ζύμωμα": "ζύμωμα — kneading", "ζύμη": "ζύμη — dough", "ξεκουραστεί": "ξεκουράζομαι — to rest", "δάκρυσε": "δακρύζω — to have tears in one's eyes"}
})

ITEMS.append({
 "id": "l121-c1-giati-paizoun-ta-zoa", "title": "Γιατί παίζουν τα ζώα;", "title_en": "Why do animals play?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ηθολόγο σε μια εκπομπή επιστήμης για τη συμπεριφορά των ζώων.",
 "script": [
  L("Ηθολόγος", "f", "Τα σκυλάκια κυνηγιούνται και δαγκώνονται χωρίς να πονούν, τα γατάκια επιτίθενται σε ένα κουβάρι, τα δελφίνια φτιάχνουν δαχτυλίδια από φυσαλίδες και τα κοράκια, σύμφωνα με αρκετές παρατηρήσεις, γλιστρούν σε χιονισμένες στέγες. Το παιχνίδι είναι διαδεδομένο στα θηλαστικά και σε ορισμένα πουλιά. Το ερώτημα είναι γιατί.", "Puppies chase and bite each other without hurting, kittens attack a ball of wool, dolphins make rings of bubbles and ravens, according to several observations, slide down snowy roofs. Play is widespread in mammals and in some birds. The question is why."),
  L("Ηθολόγος", "f", "Το παιχνίδι έχει κόστος. Καταναλώνει ενέργεια, και ένα νεαρό ζώο που παίζει είναι λιγότερο προσεκτικό απέναντι στους θηρευτές. Αν η εξέλιξη το διατήρησε, πρέπει να έχει σημαντικά οφέλη. Η παλαιότερη εξήγηση είναι ότι το παιχνίδι είναι εξάσκηση: το λιοντάρι που παίζει «κυνηγητό» μαθαίνει να κυνηγά.", "Play has a cost. It uses energy, and a young animal that plays is less careful about predators. If evolution has kept it, it must have significant benefits. The oldest explanation is that play is practice: the lion cub that plays \"chase\" is learning to hunt."),
  L("Ηθολόγος", "f", "Πιο πρόσφατα, ερευνητές πρότειναν ότι το παιχνίδι μάς προετοιμάζει για το απρόβλεπτο. Στο παιχνίδι τα ζώα βάζουν συνεχώς τον εαυτό τους σε παράξενες θέσεις, χάνουν την ισορροπία τους και την ξαναβρίσκουν. Έτσι, όταν βρεθούν σε μια πραγματική απειλή, αντιδρούν πιο ευέλικτα. Το παιχνίδι έχει επίσης κοινωνικό ρόλο: τα ζώα μαθαίνουν τα όρια, πόσο δυνατά μπορούν να δαγκώσουν, πότε να υποχωρήσουν.", "More recently, researchers have suggested that play prepares us for the unexpected. In play, animals constantly put themselves in strange positions, lose their balance and regain it. So when they find themselves facing a real threat, they react more flexibly. Play also has a social role: animals learn limits, how hard they can bite, when to back down."),
  L("Ηθολόγος", "f", "Για να μην παρεξηγηθεί το παιχνίδι, πολλά ζώα χρησιμοποιούν ειδικά σήματα. Ο σκύλος, για παράδειγμα, χαμηλώνει τα μπροστινά του πόδια και σηκώνει τα πίσω, σαν να υποκλίνεται, λέγοντας ουσιαστικά «ό,τι ακολουθεί είναι για πλάκα». Ίσως τελικά να μην είναι τυχαίο ότι τα πιο έξυπνα είδη είναι και τα πιο παιχνιδιάρικα.", "So that play is not misunderstood, many animals use special signals. The dog, for example, lowers its front legs and raises its back end, as if bowing, essentially saying \"what follows is just for fun\". Perhaps, in the end, it's no coincidence that the most intelligent species are also the most playful."),
 ],
 "questions": [
  Q("Γιατί, κατά την ηθολόγο, το παιχνίδι πρέπει να έχει σημαντικά οφέλη;", ["Γιατί είναι ευχάριστο", "Γιατί έχει κόστος, κι όμως η εξέλιξη το διατήρησε", "Γιατί το κάνουν μόνο τα έξυπνα ζώα", "Γιατί οι γονείς το ενθαρρύνουν"], 1, "Αν η εξέλιξη το διατήρησε, πρέπει να έχει σημαντικά οφέλη"),
  Q("Τι υποστηρίζει η πιο πρόσφατη εξήγηση;", ["Ότι το παιχνίδι βοηθά στη χώνεψη", "Ότι το παιχνίδι είναι μόνο εξάσκηση στο κυνήγι", "Ότι το παιχνίδι προετοιμάζει τα ζώα για το απρόβλεπτο", "Ότι το παιχνίδι μειώνει την ενέργεια των νεαρών ζώων"], 2, "το παιχνίδι μάς προετοιμάζει για το απρόβλεπτο"),
  Q("Τι σημαίνει η «υπόκλιση» του σκύλου;", ["Ότι ό,τι ακολουθεί είναι για πλάκα", "Ότι είναι κουρασμένος", "Ότι θέλει φαγητό", "Ότι αναγνωρίζει τον αρχηγό"], 0, "ό,τι ακολουθεί είναι για πλάκα"),
  Q("Ποιο κοινωνικό όφελος του παιχνιδιού αναφέρεται;", ["Τα ζώα βρίσκουν σύντροφο", "Τα ζώα μοιράζονται την τροφή", "Τα ζώα αποκτούν δικό τους έδαφος", "Τα ζώα μαθαίνουν τα όρια, πόσο δυνατά μπορούν να δαγκώσουν και πότε να υποχωρήσουν"], 3, "τα ζώα μαθαίνουν τα όρια, πόσο δυνατά μπορούν να δαγκώσουν, πότε να υποχωρήσουν"),
 ],
 "gloss": {"ηθολόγο": "ηθολόγος — ethologist (animal behaviour scientist)", "συμπεριφορά": "συμπεριφορά — behaviour", "κουβάρι": "κουβάρι — ball of wool", "φυσαλίδες": "φυσαλίδα — bubble", "κοράκια": "κοράκι — raven, crow", "θηλαστικά": "θηλαστικό — mammal", "θηρευτές": "θηρευτής — predator", "εξέλιξη": "εξέλιξη — evolution", "απρόβλεπτο": "απρόβλεπτος — unexpected", "ευέλικτα": "ευέλικτα — flexibly", "υποχωρήσουν": "υποχωρώ — to back down", "υποκλίνεται": "υποκλίνομαι — to bow", "παιχνιδιάρικα": "παιχνιδιάρικος — playful"}
})

ITEMS.append({
 "id": "l121-c1-evraioi-thessalonikis", "title": "Η εβραϊκή Θεσσαλονίκη", "title_en": "Jewish Thessaloniki", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν ιστορικό σε εκπομπή για την ιστορία της Θεσσαλονίκης.",
 "script": [
  L("Δημοσιογράφος", "f", "Λέγεται συχνά ότι για αιώνες η Θεσσαλονίκη ήταν μια πόλη με εβραϊκή πλειονότητα. Πώς έφτασαν εκεί οι Εβραίοι;", "It is often said that for centuries Thessaloniki was a city with a Jewish majority. How did the Jews get there?"),
  L("Ιστορικός", "m", "Υπήρχε μια μικρή εβραϊκή κοινότητα ήδη από την αρχαιότητα. Η μεγάλη αλλαγή όμως ήρθε μετά το 1492, όταν οι Εβραίοι εκδιώχθηκαν από την Ισπανία. Χιλιάδες από αυτούς, οι λεγόμενοι Σεφαραδίτες, βρήκαν καταφύγιο στην Οθωμανική Αυτοκρατορία, και πολλοί εγκαταστάθηκαν στη Θεσσαλονίκη. Έφεραν μαζί τους τη γλώσσα τους, τα λαδίνο, μια μορφή παλιών ισπανικών, που μιλιόταν στην πόλη ως τον 20ό αιώνα.", "There was a small Jewish community already in antiquity. But the big change came after 1492, when the Jews were expelled from Spain. Thousands of them, the so-called Sephardim, found refuge in the Ottoman Empire, and many settled in Thessaloniki. They brought with them their language, Ladino, a form of old Spanish, which was spoken in the city until the 20th century."),
  L("Δημοσιογράφος", "f", "Τι ρόλο έπαιξαν στη ζωή της πόλης;", "What role did they play in the life of the city?"),
  L("Ιστορικός", "m", "Καθοριστικό. Ήταν έμποροι, τεχνίτες, λιμενεργάτες, τυπογράφοι. Το λιμάνι σταματούσε να δουλεύει το Σάββατο, γιατί πολλοί από τους εργάτες του ήταν Εβραίοι. Η πόλη έγινε γνωστή ως «Ιερουσαλήμ των Βαλκανίων». Η μεγάλη πυρκαγιά του 1917 κατέστρεψε όμως ένα μεγάλο μέρος των εβραϊκών συνοικιών, και πολλές οικογένειες μετανάστευσαν.", "Decisive. They were merchants, craftsmen, dockworkers, printers. The port stopped working on Saturdays, because many of its workers were Jewish. The city became known as the \"Jerusalem of the Balkans\". The great fire of 1917, however, destroyed a large part of the Jewish quarters, and many families emigrated."),
  L("Δημοσιογράφος", "f", "Και ο Δεύτερος Παγκόσμιος Πόλεμος;", "And the Second World War?"),
  L("Ιστορικός", "m", "Ήταν το τραγικό τέλος. Το 1943, οι Γερμανοί κατακτητές εκτόπισαν δεκάδες χιλιάδες Εβραίους της πόλης στα στρατόπεδα εξόντωσης, κυρίως στο Άουσβιτς. Η συντριπτική πλειονότητα δεν επέστρεψε ποτέ. Ήδη από το 1942 είχε καταστραφεί και το αρχαίο εβραϊκό νεκροταφείο, πάνω σε μέρος του οποίου χτίστηκε αργότερα το Αριστοτέλειο Πανεπιστήμιο. Σήμερα, το Εβραϊκό Μουσείο και τα μνημεία της πόλης κρατούν ζωντανή αυτή τη μνήμη. Γιατί μια πόλη δεν είναι μόνο τα κτίριά της, αλλά και όσοι έλειψαν από αυτήν.", "It was the tragic end. In 1943, the German occupiers deported tens of thousands of the city's Jews to extermination camps, mainly Auschwitz. The overwhelming majority never returned. Already in 1942 the ancient Jewish cemetery had also been destroyed, and on part of it the Aristotle University was later built. Today the Jewish Museum and the city's memorials keep this memory alive. Because a city is not only its buildings, but also those who are missing from it."),
 ],
 "questions": [
  Q("Πότε ήρθε η μεγάλη αλλαγή στην εβραϊκή κοινότητα της πόλης;", ["Στην αρχαιότητα", "Μετά το 1492, όταν οι Εβραίοι εκδιώχθηκαν από την Ισπανία", "Μετά την πυρκαγιά του 1917", "Μετά την απελευθέρωση του 1912"], 1, "Η μεγάλη αλλαγή όμως ήρθε μετά το 1492"),
  Q("Γιατί το λιμάνι σταματούσε να δουλεύει το Σάββατο;", ["Γιατί ήταν αργία για όλη την πόλη", "Γιατί έρχονταν λιγότερα πλοία", "Γιατί πολλοί από τους εργάτες του ήταν Εβραίοι", "Γιατί το απαγόρευαν οι Οθωμανοί"], 2, "πολλοί από τους εργάτες του ήταν Εβραίοι"),
  Q("Τι συνέπειες είχε η πυρκαγιά του 1917;", ["Κατέστρεψε μεγάλο μέρος των εβραϊκών συνοικιών και πολλές οικογένειες μετανάστευσαν", "Κατέστρεψε το λιμάνι", "Έκαψε το εβραϊκό νεκροταφείο", "Οδήγησε στην ίδρυση του Πανεπιστημίου"], 0, "κατέστρεψε όμως ένα μεγάλο μέρος των εβραϊκών συνοικιών"),
  Q("Ποια σκέψη κλείνει τη συνέντευξη;", ["Ότι η πόλη πρέπει να ξαναχτιστεί", "Ότι η ιστορία δεν πρέπει να συζητιέται", "Ότι το μουσείο χρειάζεται χρήματα", "Ότι μια πόλη είναι και όσοι έλειψαν από αυτήν"], 3, "μια πόλη δεν είναι μόνο τα κτίριά της, αλλά και όσοι έλειψαν από αυτήν"),
 ],
 "gloss": {"πλειονότητα": "πλειονότητα — majority", "εκδιώχθηκαν": "εκδιώκομαι — to be expelled", "Σεφαραδίτες": "Σεφαραδίτης — Sephardic Jew", "καταφύγιο": "καταφύγιο — refuge", "λαδίνο": "λαδίνο — Ladino (Judeo-Spanish)", "Καθοριστικό": "καθοριστικός — decisive", "λιμενεργάτες": "λιμενεργάτης — dockworker", "τυπογράφοι": "τυπογράφος — printer", "κατακτητές": "κατακτητής — occupier, conqueror", "εκτόπισαν": "εκτοπίζω — to deport", "στρατόπεδα εξόντωσης": "στρατόπεδο εξόντωσης — extermination camp", "συντριπτική": "συντριπτικός — overwhelming", "νεκροταφείο": "νεκροταφείο — cemetery"}
})

rnd = random.Random(121)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-121.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
