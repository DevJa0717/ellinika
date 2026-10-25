import json, sys
VN = [("εφαρμόζω","η εφαρμογή"),("αποφασίζω","η απόφαση"),("αυξάνω / αυξάνομαι","η αύξηση"),("μειώνω","η μείωση"),("αναπτύσσω","η ανάπτυξη"),
 ("προστατεύω","η προστασία"),("συμμετέχω","η συμμετοχή"),("αντιμετωπίζω","η αντιμετώπιση"),("καταργώ","η κατάργηση"),("εξασφαλίζω","η εξασφάλιση"),
 ("ενισχύω","η ενίσχυση"),("αξιολογώ","η αξιολόγηση"),("διασφαλίζω","η διασφάλιση"),("επιλύω","η επίλυση"),("εκσυγχρονίζω","ο εκσυγχρονισμός"),
 ("αποτυγχάνω","η αποτυχία"),("επιτυγχάνω","η επίτευξη"),("καθυστερώ","η καθυστέρηση"),("αξιοποιώ","η αξιοποίηση"),("διευκολύνω","η διευκόλυνση"),
 ("υλοποιώ","η υλοποίηση"),("επεκτείνω","η επέκταση"),("απαγορεύω","η απαγόρευση"),("συγκρίνω","η σύγκριση"),("περιορίζω","ο περιορισμός")]
T = [ # verbal → nominal
 ("Επειδή αυξήθηκαν οι τιμές, ο κόσμος ξοδεύει λιγότερο.","Η αύξηση των τιμών οδήγησε σε μείωση της κατανάλωσης."),
 ("Αν εφαρμοστεί ο νόμος σωστά, θα προστατευτεί το περιβάλλον.","Η σωστή εφαρμογή του νόμου θα συμβάλει στην προστασία του περιβάλλοντος."),
 ("Πρέπει να αντιμετωπίσουμε αμέσως την ανεργία.","Η άμεση αντιμετώπιση της ανεργίας είναι επιτακτική."),
 ("Όταν καθυστέρησε το έργο, ανέβηκε το κόστος.","Η καθυστέρηση του έργου είχε ως αποτέλεσμα την αύξηση του κόστους."),
 ("Οι πολίτες δεν συμμετέχουν και γι' αυτό η δημοκρατία αδυνατίζει.","Η χαμηλή συμμετοχή των πολιτών αποδυναμώνει τη δημοκρατία."),
]
L = {
 "el": "Ονοματοποίηση",
 "title": "Nominal style: from «επειδή αυξήθηκαν οι τιμές» to «η αύξηση των τιμών»",
 "section": "C1 · argument and register",
 "goal": "Turn spoken verb-heavy sentences into the dense noun style of essays, reports and the press, and back again.",
 "blocks": [
  {"type":"text","text":"The biggest single difference between B2 and C1 written Greek is **nominalisation**: actions become nouns, and the nouns are chained with genitives. Speech says *Επειδή αυξήθηκαν οι τιμές, ο κόσμος ξοδεύει λιγότερο*; an article says *Η αύξηση των τιμών οδήγησε σε μείωση της κατανάλωσης*. The second sentence has one verb, four nouns and two genitives. That is why declension matters so much at C1: every nominalised sentence is a genitive drill."},
  {"type":"table","title":"Verb → action noun","head":["Verb","Noun"],"rows":[[a,f"**{b}**"] for a,b in VN]},
  {"type":"table","title":"The toolkit","head":["Move","Spoken","Written"],"rows":[
    ["Clause → noun + genitive","όταν εφαρμοστεί ο νόμος","**με την εφαρμογή του νόμου**"],
    ["Adverb → adjective","εφαρμόζεται σωστά","**η σωστή εφαρμογή**"],
    ["Subject → genitive","οι πολίτες συμμετέχουν","**η συμμετοχή των πολιτών**"],
    ["Object → genitive","προστατεύουμε το περιβάλλον","**η προστασία του περιβάλλοντος**"],
    ["Cause verb","…και γι' αυτό…","**οδηγεί σε, έχει ως αποτέλεσμα, συμβάλλει σε, προκαλεί**"],
    ["Whole clause as a noun","ότι έφυγε με πείραξε","**Το ότι έφυγε** με πείραξε / **Το γεγονός ότι** έφυγε…"],
    ["να-clause as a noun","να μαθαίνεις γλώσσες είναι ωραίο","**Το να μαθαίνεις** γλώσσες είναι ωραίο"]]},
  {"type":"callout","text":"**Chains of genitives** are normal: *η αύξηση του κόστους της ενέργειας των νοικοκυριών* 'the increase in the cost of household energy'. Two are elegant, three are acceptable, four are officialese. To break a chain, use **σε, για, ως προς, όσον αφορά** + accusative: *η αύξηση του κόστους για τα νοικοκυριά*.\n\n**Light verbs** carry the noun: *προβαίνω σε, προχωρώ σε, θέτω σε, φέρνω σε* + noun: *Η κυβέρνηση προχώρησε σε περικοπές* 'The government made cuts'."},
  {"type":"examples","title":"Spoken → written","items":[{"el":b,"en":a} for a,b in T]},
  {"type":"culture","title":"Η «ξύλινη γλώσσα»","text":"Greeks call officialese **ξύλινη γλώσσα** 'wooden language', and political speeches are its home: *Προχωρούμε στην υλοποίηση της αναβάθμισης του πλαισίου διασφάλισης της ποιότητας.* The school essay (*έκθεση*) trains the same habits, so educated Greeks write densely by reflex. The C1 skill is to choose: nominal style for a report or essay, verbs and people for a talk or a conversation."},
  {"type":"reading","title":"Η στέγαση των νέων","text":"Η **αύξηση** των ενοικίων στα μεγάλα αστικά κέντρα αποτελεί πλέον ένα από τα σοβαρότερα κοινωνικά προβλήματα της χώρας. Η **ανάπτυξη** της βραχυχρόνιας μίσθωσης, σε συνδυασμό με τη **μείωση** της οικοδομικής δραστηριότητας κατά την περίοδο της κρίσης, οδήγησε σε δραματική **συρρίκνωση** της προσφοράς κατοικιών.\n\nΗ **αντιμετώπιση** του προβλήματος απαιτεί συνδυασμό μέτρων. Η **αξιοποίηση** των κλειστών ακινήτων του Δημοσίου, η **ενίσχυση** της κοινωνικής κατοικίας και ο **περιορισμός** των νέων αδειών βραχυχρόνιας μίσθωσης σε ορισμένες περιοχές θα μπορούσαν να συμβάλουν στη **σταθεροποίηση** των τιμών.\n\n**Το γεγονός ότι** σχεδόν οι μισοί νέοι κάτω των 30 ζουν ακόμη με τους γονείς τους δεν είναι μόνο οικονομικό ζήτημα. **Το να μην** μπορείς να ανεξαρτητοποιηθείς επηρεάζει την **απόφαση** για οικογένεια, την επαγγελματική **κινητικότητα** και, τελικά, τη δημογραφική **εξέλιξη** της χώρας.","en":"Rising rents in the big urban centres are now one of the country's most serious social problems. The growth of short-term letting, combined with the fall in construction during the crisis years, has led to a dramatic shrinking of the housing supply.\n\nTackling the problem requires a combination of measures. Using the State's empty properties, strengthening social housing and limiting new short-term-let licences in certain areas could help stabilise prices.\n\nThe fact that almost half of young people under 30 still live with their parents is not just an economic matter. Not being able to become independent affects the decision to start a family, professional mobility and, ultimately, the country's demographic development.",
   "gloss":{"βραχυχρόνιας μίσθωσης":"short-term letting (gen.)","συρρίκνωση":"shrinkage","ακινήτων":"properties (gen. pl.)","κοινωνικής κατοικίας":"social housing (gen.)","ανεξαρτητοποιηθείς":"become independent","κινητικότητα":"mobility"},
   "questions":[
    {"prompt":"Ποιοι δύο παράγοντες μείωσαν την προσφορά κατοικιών;","answer":"Οι βραχυχρόνιες μισθώσεις και το ότι χτίστηκαν λιγότερα σπίτια.","options":["Οι βραχυχρόνιες μισθώσεις και το ότι χτίστηκαν λιγότερα σπίτια.","Τα κλειστά ακίνητα του Δημοσίου και οι νέοι.","Η κοινωνική κατοικία και οι άδειες.","Η δημογραφία και η κινητικότητα."],"why":"Η ανάπτυξη της βραχυχρόνιας μίσθωσης … με τη μείωση της οικοδομικής δραστηριότητας."},
    {"prompt":"Γιατί, κατά το κείμενο, το πρόβλημα δεν είναι μόνο οικονομικό;","answer":"Επειδή επηρεάζει την οικογένεια, την εργασία και τη δημογραφία.","options":["Επειδή επηρεάζει την οικογένεια, την εργασία και τη δημογραφία.","Επειδή οι νέοι δεν θέλουν να φύγουν από το σπίτι.","Επειδή το Δημόσιο έχει κλειστά ακίνητα.","Επειδή οι τιμές σταθεροποιήθηκαν."],"why":"επηρεάζει την απόφαση για οικογένεια, την επαγγελματική κινητικότητα … τη δημογραφική εξέλιξη."}]}
 ],
 "practice": [
  {"gen":"type","n":10,"items":[{"prompt":f"Noun from **{a}** (with article)","answer":b,"accept":[b,b.split(' ',1)[1]],"why":f"{a} → {b}"} for a,b in VN]},
  {"gen":"mc","items":[
    {"prompt":"*Επειδή καθυστέρησε το έργο…* → ___ του έργου…","answer":"Η καθυστέρηση","options":["Η καθυστέρηση","Το καθυστερημένο","Καθυστερώντας","Η καθυστερούσα"],"why":"Clause → action noun + genitive."},
    {"prompt":"Η ___ των πολιτών στις εκλογές μειώθηκε. (participation)","answer":"συμμετοχή","options":["συμμετοχή","συμμετέχοντες","συμμετοχής","συμμετέχουσα"],"why":"Nominative subject: η συμμετοχή."},
    {"prompt":"Η κρίση οδήγησε ___ της ανεργίας.","answer":"στην αύξηση","options":["στην αύξηση","την αύξηση","της αύξησης","με την αύξηση"],"why":"οδηγώ σε + accusative."},
    {"prompt":"___ μαθαίνεις μια γλώσσα μετά τα 40 είναι πρόκληση.","answer":"Το να","options":["Το να","Το ότι","Που να","Αυτό να"],"why":"Το να + clause works as a noun subject (general, non-factual)."},
    {"prompt":"___ δεν απάντησε στο email μου με εκνεύρισε.","answer":"Το ότι","options":["Το ότι","Το να","Ότι το","Το πως να"],"why":"Το ότι + indicative for a fact."},
    {"prompt":"Η προστασία ___ είναι προτεραιότητα. (the environment)","answer":"του περιβάλλοντος","options":["του περιβάλλοντος","το περιβάλλον","του περιβάλλον","στο περιβάλλον"],"why":"Object → genitive: του περιβάλλοντος."},
    {"prompt":"Ποια πρόταση είναι πιο «γραπτή»;","answer":"Η μείωση των φόρων συνέβαλε στην ανάκαμψη της οικονομίας.","options":["Η μείωση των φόρων συνέβαλε στην ανάκαμψη της οικονομίας.","Μείωσαν τους φόρους και η οικονομία πήγε καλύτερα.","Αφού μειώθηκαν οι φόροι, η οικονομία ανέβηκε.","Η οικονομία ανέβηκε γιατί κατέβηκαν οι φόροι."],"why":"Two action nouns with genitives and a learned cause verb."},
    {"prompt":"Η κυβέρνηση ___ σε περικοπές δαπανών. (proceeded)","answer":"προχώρησε","options":["προχώρησε","έκανε","έβαλε","πήγε"],"why":"Light verb: προχωρώ σε + noun."}]}
 ]
}
json.dump(L, open(sys.argv[1],"w"), ensure_ascii=False, indent=1)
