import json, sys
N = [("το γεγονός","του γεγονότος","τα γεγονότα","fact, event"),
 ("το καθεστώς","του καθεστώτος","τα καθεστώτα","regime, status"),
 ("το φως","του φωτός","τα φώτα","light"),
 ("το πέρας","του πέρατος","—","end, completion"),
 ("το κρέας","του κρέατος","τα κρέατα","meat"),
 ("το τέρας","του τέρατος","τα τέρατα","monster"),
 ("το γήρας","του γήρατος","—","old age"),
 ("το ήπαρ","του ήπατος","—","liver (medical)"),
 ("το ύδωρ","του ύδατος","τα ύδατα","water (learned); waters"),
 ("το πυρ","του πυρός","τα πυρά","fire (gunfire)"),
 ("το άλας","του άλατος","τα άλατα","salt (chemistry)"),
 ("ο συγγραφέας","του συγγραφέα","οι συγγραφείς","author"),
 ("ο γραμματέας","του γραμματέα","οι γραμματείς","secretary"),
 ("ο αποστολέας","του αποστολέα","οι αποστολείς","sender"),
 ("ο εκπαιδευτής","του εκπαιδευτή","οι εκπαιδευτές","trainer (contrast: regular)"),
]
ML = [("ο/η μείζων, το μείζον","μείζονος","μείζονες / μείζονα","major, greater"),
      ("ο/η ελάσσων, το έλασσον","ελάσσονος","ελάσσονες / ελάσσονα","minor, lesser")]
SUP = [("άριστος","excellent (grade 'Άριστα')"),("βέλτιστος","optimal; οι βέλτιστες πρακτικές 'best practice'"),("μέγιστος","maximum, greatest"),("ελάχιστος","minimum, least"),("ύψιστος","supreme"),("κάκιστος","very bad, worst"),("πλείστος","most; ως επί το πλείστον 'mostly'"),("έσχατος","utmost; έσχατη προδοσία 'high treason'"),("ήκιστα","not at all (adv.)")]
L = {
 "el": "Λόγια κλίση",
 "title": "Learned declension: του γεγονότος, του φωτός, οι συγγραφείς, μείζων",
 "section": "C1 · learned morphology",
 "goal": "Get the genitives and plurals of the ancient-type nouns and adjectives right, which is where educated Greeks notice mistakes.",
 "blocks": [
  {"type":"text","text":"A small set of very common nouns still follows the ancient third declension: the nominative is short and the other cases add a consonant stem. You already know two families of this type, **το κράτος, του κράτους** and **το περιβάλλον, του περιβάλλοντος**. This lesson covers the rest: neuters in **-ός/-ότος, -ας/-ατος, -ωρ/-ατος**, the plural in **-είς** of nouns in -έας, and the learned comparatives **μείζων, ελάσσων** with the superlatives in **-ιστος**."},
  {"type":"table","title":"Neuters with a hidden stem","head":["Nominative","Genitive","Plural","Meaning"],"rows":[[f"**{a}**",b,c,d] for a,b,c,d in N[:11]]},
  {"type":"callout","text":"**τα φώτα, των φώτων**: φως is irregular in the plural (no -τ- doubling). **τα πυρά** is gunfire; ordinary fire is η φωτιά. **ύδωρ** lives mostly in compounds and set phrases (*υδάτινος, υδατάνθρακες, τα χωρικά ύδατα* 'territorial waters'). **το πέρας** is the bureaucrat's 'end': *μετά το πέρας της συνεδρίασης* 'after the end of the session'.\n\n**Words in -ός stressed on the end** keep the stress: *του γεγονότος, των γεγονότων, του καθεστώτος*. A useful model phrase: **το γεγονός ότι** + clause 'the fact that'."},
  {"type":"table","title":"Nouns in -έας: plural in -είς","head":["Singular","Genitive sg.","Plural (nom./acc.)","Meaning"],"rows":[[f"**{a}**",b,f"**{c}**",d] for a,b,c,d in N[11:]]},
  {"type":"callout","text":"Masculines in **-έας** (συγγραφέας, γραμματέας, αποστολέας, but not -ής nouns such as εκπαιδευτής) have the ancient plural **-είς, -έων**: *οι συγγραφείς, των συγγραφέων, τους συγγραφείς*. *Συγγραφέες* exists in speech but marks you as careless. The old nominative **-εύς** survives in formal names: *Βασιλέως Κωνσταντίνου* (an Athens avenue), *Γραμματεύς* on old documents."},
  {"type":"table","title":"μείζων and ελάσσων","head":["Nominative","Genitive sg.","Plural m-f / n","Meaning"],"rows":[[f"**{a}**",b,c,d] for a,b,c,d in ML]},
  {"type":"examples","items":[
    {"el":"Πρόκειται για ζήτημα μείζονος σημασίας.","en":"This is a matter of major importance."},
    {"el":"Η καθυστέρηση είναι ελάσσονος σημασίας.","en":"The delay is of minor importance."},
    {"el":"Το μείζον πρόβλημα είναι η στέγαση.","en":"The major problem is housing."},
    {"el":"Η ευρύτερη περιοχή της μείζονος Αθήνας.","en":"Greater Athens."},
    {"el":"Ακολουθούμε τις βέλτιστες πρακτικές.","en":"We follow best practice."},
    {"el":"Οι επιβάτες ήταν ως επί το πλείστον τουρίστες.","en":"The passengers were mostly tourists."},
    {"el":"Η απάντησή του ήταν ήκιστα πειστική.","en":"His answer was not in the least convincing."}]},
  {"type":"table","title":"Superlatives in -ιστος","head":["Form","Meaning and use"],"rows":[[f"**{a}**",b] for a,b in SUP]},
  {"type":"culture","title":"Βασιλίσσης Σοφίας, Πανεπιστημίου, Μητροπόλεως","text":"Athens street names are a crash course in learned genitives. Avenues were named in the 19th century, in katharevousa, and the names stuck: **Λεωφόρος Βασιλίσσης Σοφίας** (not *της βασίλισσας*), **Βασιλέως Κωνσταντίνου**, **Μητροπόλεως** (μητρόπολη → -εως), **Πλατεία Συντάγματος**, **Ερμού**, **Αθηνάς**. On the metro you hear *Επόμενη στάση: Ευαγγελισμός*; on the bus *Πανεπιστημίου*. Greeks use these forms unthinkingly, even people who never studied katharevousa. The **Τράπεζα της Ελλάδος** also keeps the old genitive of η Ελλάς."},
  {"type":"reading","title":"Το καθεστώς των ακτών","text":"Η πρόσβαση στις παραλίες αποτελεί ζήτημα **μείζονος** σημασίας για τη χώρα. Σύμφωνα με τη νομοθεσία, ο αιγιαλός είναι κοινόχρηστος, και το **γεγονός** αυτό δεν αλλάζει, ακόμη κι αν μια έκταση ανήκει σε ιδιώτη. Παρ' όλα αυτά, κάθε καλοκαίρι πολλοί λουόμενοι διαπιστώνουν ότι ξαπλώστρες καλύπτουν το **μέγιστο** μέρος της άμμου.\n\nΟι **συγγραφείς** μιας πρόσφατης έκθεσης υποστηρίζουν ότι το **καθεστώς** των παραχωρήσεων πρέπει να αναθεωρηθεί. Προτείνουν ένα **ελάχιστο** ποσοστό ελεύθερου χώρου σε κάθε ακτή και αυστηρότερους ελέγχους μετά το **πέρας** της τουριστικής περιόδου, όταν τα πρόστιμα συνήθως ξεχνιούνται.\n\nΤο ζήτημα δεν είναι **ελάσσονος** σημασίας: οι ακτές της χώρας ξεπερνούν τα 15.000 χιλιόμετρα, και η ποιότητα του **ύδατος** κατατάσσει την Ελλάδα σταθερά στις πρώτες θέσεις της Ευρώπης.","en":"Access to beaches is a matter of major importance for the country. By law the foreshore is common land, and this fact does not change even if a plot belongs to a private individual. Nevertheless, every summer many bathers find that sunbeds cover most of the sand.\n\nThe authors of a recent report argue that the regime of concessions must be revised. They propose a minimum share of free space on each beach and stricter checks after the end of the tourist season, when fines are usually forgotten.\n\nThe issue is not of minor importance: the country's coastline exceeds 15,000 km, and the quality of its water consistently ranks Greece among the top places in Europe.",
   "gloss":{"αιγιαλός":"foreshore","κοινόχρηστος":"for common use","λουόμενοι":"bathers","ξαπλώστρες":"sunbeds","παραχωρήσεων":"concessions (gen. pl.)","πρόστιμα":"fines","κατατάσσει":"ranks"},
   "questions":[
    {"prompt":"Τι ισχύει για τον αιγιαλό σύμφωνα με τον νόμο;","answer":"Ανήκει σε όλους.","options":["Ανήκει σε όλους.","Ανήκει στον ιδιοκτήτη της γύρω έκτασης.","Ανήκει στον δήμο μόνο το καλοκαίρι.","Μπορεί να πουληθεί σε ιδιώτες."],"why":"ο αιγιαλός είναι κοινόχρηστος."},
    {"prompt":"Τι προτείνουν οι συγγραφείς της έκθεσης;","answer":"Ένα ελάχιστο ποσοστό ελεύθερης παραλίας και περισσότερους ελέγχους.","options":["Ένα ελάχιστο ποσοστό ελεύθερης παραλίας και περισσότερους ελέγχους.","Να καταργηθούν όλες οι ξαπλώστρες.","Να αυξηθούν τα πρόστιμα το καλοκαίρι.","Να κλείσουν οι παραλίες μετά την περίοδο."],"why":"ελάχιστο ποσοστό ελεύθερου χώρου … αυστηρότερους ελέγχους."}]}
 ],
 "practice": [
  {"gen":"type","n":10,"items":[{"prompt":f"Genitive singular: **{a}** ({d})","answer":b,"accept":[b,b.split(' ',1)[1]],"why":f"{a}, {b}, {c}"} for a,b,c,d in N if a!="ο εκπαιδευτής"]+
    [{"prompt":f"Nominative plural: **{a}** ({d})","answer":c,"accept":[c,c.split(' ',1)[1]],"why":f"{a} → {c}"} for a,b,c,d in N if c!="—"]},
  {"gen":"mc","items":[
    {"prompt":"Το ζήτημα είναι ___ σημασίας. (major)","answer":"μείζονος","options":["μείζονος","μείζων","μείζον","μειζόνων"],"why":"Genitive singular: μείζονος σημασίας."},
    {"prompt":"Μετά το ___ της συνεδρίασης, έγινε δεξίωση. (end)","answer":"πέρας","options":["πέρας","πέρατος","πέρατα","περάτωμα"],"why":"Accusative = nominative for neuters: το πέρας."},
    {"prompt":"Λόγω του ___ ότι έβρεχε, η εκδήλωση αναβλήθηκε.","answer":"γεγονότος","options":["γεγονότος","γεγονός","γεγονού","γεγονότα"],"why":"λόγω + genitive: του γεγονότος."},
    {"prompt":"Στην έκθεση βιβλίου ήρθαν δεκάδες ___.","answer":"συγγραφείς","options":["συγγραφείς","συγγραφέες","συγγραφέων","συγγραφέας"],"why":"Plural of -έας: -είς."},
    {"prompt":"Οι υπογραφές των ___ (secretaries, gen. pl.)","answer":"γραμματέων","options":["γραμματέων","γραμματείς","γραμματεών","γραμματέα"],"why":"Gen. pl. -έων: των γραμματέων."},
    {"prompt":"Η ταχύτητα του ___ είναι σταθερή.","answer":"φωτός","options":["φωτός","φως","φώτου","φώτων"],"why":"το φως, του φωτός."},
    {"prompt":"Ακολουθούμε τις ___ πρακτικές του κλάδου. (best)","answer":"βέλτιστες","options":["βέλτιστες","καλύτατες","μείζονες","άριστα"],"why":"οι βέλτιστες πρακτικές 'best practice'."},
    {"prompt":"Οι θεατές ήταν ως επί το ___ φοιτητές.","answer":"πλείστον","options":["πλείστον","πλείστο","περισσότερο","μέγιστον"],"why":"Fixed phrase: ως επί το πλείστον 'mostly'."},
    {"prompt":"Η κατανάλωση ___ μειώθηκε στην Ευρώπη. (meat)","answer":"κρέατος","options":["κρέατος","κρέας","κρεάτου","κρεάτων"],"why":"το κρέας, του κρέατος."}]}
 ]
}
json.dump(L, open(sys.argv[1],"w"), ensure_ascii=False, indent=1)
