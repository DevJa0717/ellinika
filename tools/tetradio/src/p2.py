from common import P, ph, q, ex

U05 = dict(
    id="advice-letter", kind="unit", part="personal", level="B2", el="Φιλικό γράμμα με συμβουλές", title="Friendly letter giving advice",
    intro=[
        {"p": "Advice letters are the commonest Part A task. The friend has a problem; you show you understand it, give two or three pieces of advice **with reasons**, and end with encouragement. Vary the advice formulas: an examiner who reads «πρέπει να» five times marks your range down."},
    ],
    structure=[
        ["Χαιρετισμός και αντίδραση", "Greeting and reaction", "Thank them for writing and react to the news: Λυπάμαι πολύ που… / Χάρηκα που…"],
        ["Κατανόηση", "Empathy", "Show you see the problem: Καταλαβαίνω απόλυτα πώς νιώθεις."],
        ["Συμβουλή 1 + αιτιολόγηση", "Advice 1 + reason", "Αν ήμουν στη θέση σου, θα… γιατί…"],
        ["Συμβουλή 2 (+3) + αιτιολόγηση", "Advice 2 (+3) + reason", "Σου προτείνω να… / Καλό θα ήταν να…"],
        ["Ενθάρρυνση και κλείσιμο", "Encouragement and close", "Ό,τι κι αν αποφασίσεις, … / Είμαι σίγουρη ότι θα τα καταφέρεις."],
    ],
    phrases=[
        dict(el="Συμβουλές", en="Advising", items=ph(
            ("Αν ήμουν στη θέση σου, θα…", "If I were you, I would…"),
            ("Στη θέση σου θα…", "In your place I would…"),
            ("Γιατί δεν…;", "Why don't you…?"),
            ("Τι θα έλεγες να…;", "How about…?"),
            ("Καλό θα ήταν να…", "It would be a good idea to…"),
            ("Σου προτείνω να…", "I suggest you…"),
            ("Το καλύτερο που έχεις να κάνεις είναι να…", "The best thing you can do is…"),
            ("Μην…", "Don't…"),
            ("Σκέψου και το εξής: …", "Consider this too: …"),
        )),
        dict(el="Κατανόηση", en="Sympathy", items=ph(
            ("Λυπάμαι πολύ που…", "I'm very sorry that…"),
            ("Καταλαβαίνω απόλυτα πώς νιώθεις.", "I completely understand how you feel."),
            ("Δεν σε αδικώ.", "I don't blame you."),
            ("Μην ανησυχείς, …", "Don't worry, …"),
        )),
        dict(el="Ενθάρρυνση", en="Encouragement", items=ph(
            ("Είμαι σίγουρος ότι θα τα καταφέρεις.", "I'm sure you'll manage."),
            ("Ό,τι κι αν αποφασίσεις, θα είμαι στο πλευρό σου.", "Whatever you decide, I'll be by your side."),
            ("Κουράγιο!", "Hang in there!"),
        )),
    ],
    models=[dict(
        el="Δουλειά στο εξωτερικό;", en="A job abroad?", level="B2",
        task_el="Ένας φίλος σας σας γράφει ότι του πρότειναν δουλειά στο εξωτερικό, αλλά διστάζει να φύγει από την Ελλάδα. Του γράφετε για να του δώσετε συμβουλές. (200 λέξεις)",
        task_en="A friend writes that he has been offered a job abroad but hesitates to leave Greece. Write to give him advice. (200 words)",
        text=P("""
            Αγαπητέ μου Άρη,

            Χάρηκα πολύ που πήρα το γράμμα σου, αν και κατάλαβα από τον τόνο σου ότι είσαι αγχωμένος. Δεν σε αδικώ· μια τόσο μεγάλη απόφαση δεν παίρνεται εύκολα.

            Αν ήμουν στη θέση σου, θα δεχόμουν την πρόταση. Μια τέτοια ευκαιρία δεν παρουσιάζεται κάθε μέρα, και η εμπειρία σε μια διεθνή εταιρεία θα σου ανοίξει πολλές πόρτες, ακόμα κι αν κάποια στιγμή αποφασίσεις να γυρίσεις. Επιπλέον, η σύμβαση είναι για δύο χρόνια, όχι για πάντα. Δεν καις τις γέφυρες πίσω σου.

            Καταλαβαίνω, βέβαια, ότι σε στενοχωρεί η ιδέα να αφήσεις τους γονείς σου και την παρέα. Σκέψου όμως ότι σήμερα οι αποστάσεις έχουν μικρύνει: με τις βιντεοκλήσεις θα μας βλέπεις κάθε βδομάδα, και με μια πτήση τριών ωρών θα είσαι εδώ για τις γιορτές. Σου προτείνω, πριν απαντήσεις, να μιλήσεις με κάποιον που ήδη δουλεύει εκεί, για να έχεις μια πιο ρεαλιστική εικόνα για το κόστος ζωής και το κλίμα στην εταιρεία.

            Ό,τι κι αν αποφασίσεις, εγώ θα είμαι στο πλευρό σου. Και αν φύγεις, να ξέρεις ότι θα σου κάνω σίγουρα επίσκεψη!

            Με αγάπη,
            Νεφέλη
        """),
        text_en=P("""
            Dear Aris,

            I was very glad to get your letter, although I could tell from your tone that you're anxious. I don't blame you; such a big decision isn't made easily.

            If I were you, I would accept the offer. An opportunity like this doesn't come along every day, and experience in an international company will open many doors for you, even if at some point you decide to come back. Besides, the contract is for two years, not for ever. You're not burning your bridges.

            I understand, of course, that the idea of leaving your parents and our group of friends upsets you. But think how distances have shrunk today: with video calls you'll see us every week, and with a three-hour flight you'll be here for the holidays. Before you answer, I suggest you talk to someone who already works there, so that you get a more realistic picture of the cost of living and the atmosphere at the company.

            Whatever you decide, I'll be by your side. And if you go, you know I'll definitely come and visit!

            With love,
            Nefeli
        """),
        notes=[
            "**Empathy first, advice second.** The second paragraph opens with the clearest piece of advice and two reasons; the third answers the friend's objection before giving the second piece of advice.",
            "**Αν ήμουν στη θέση σου, θα δεχόμουν**: the hypothetical conditional, imperfect in both halves. See the grammar note.",
            "**Δεν σε αδικώ·** the ano teleia (·) links two closely related statements, a mark of good Greek punctuation.",
            "**Ό,τι κι αν αποφασίσεις** (whatever you decide): ό,τι with a comma means ‘whatever’; ότι without it means ‘that’.",
        ],
    )],
    grammar=[dict(
        title="Three conditionals",
        en="**Real:** αν + present/aorist subjunctive, θα + future. **Hypothetical (if I were…):** αν + imperfect, θα + imperfect. **Past counterfactual (if I had…):** αν + pluperfect, θα + pluperfect (or θα + imperfect in speech).",
        examples=ex(
            ("Αν δεχτείς την πρόταση, θα μάθεις πολλά.", "If you accept the offer, you'll learn a lot."),
            ("Αν ήμουν στη θέση σου, θα έφευγα.", "If I were you, I would go."),
            ("Αν είχα διαβάσει, θα είχα περάσει.", "If I had studied, I would have passed."),
        ),
    )],
    drills=[
        q("Αν ___ στη θέση σου, θα του μιλούσα.", ["ήμουν", "είμαι", "θα είμαι"], "ήμουν", "Hypothetical: αν + imperfect, θα + imperfect."),
        q("___ κι αν πεις, δεν θα αλλάξω γνώμη.", ["Ό,τι", "Ότι", "Όταν"], "Ό,τι", "‘Whatever’ is ό,τι, with the comma."),
        q("Ποια συμβουλή είναι πιο ευγενική;", ["Καλό θα ήταν να μιλήσεις με τον διευθυντή σου.", "Πρέπει να μιλήσεις με τον διευθυντή σου.", "Μίλα με τον διευθυντή σου."], "Καλό θα ήταν να μιλήσεις με τον διευθυντή σου."),
        q("Αν είχες ζητήσει βοήθεια, θα σε ___.", ["είχα βοηθήσει", "βοηθήσω", "βοηθάω"], "είχα βοηθήσει", "Past counterfactual: pluperfect in both halves."),
    ],
    tasks=[
        dict(id="advice-letter-1", level="B2", words=200,
             el="Μια φίλη σας σας γράφει ότι θέλει να αφήσει το πανεπιστήμιο στο τελευταίο έτος για να ανοίξει ένα καφέ με τον αδερφό της. Της γράφετε για να της δώσετε τη γνώμη και τις συμβουλές σας. (200 λέξεις)",
             en="A friend writes that she wants to leave university in her final year to open a café with her brother. Write to give her your opinion and advice. (200 words)",
             plan=["React to the news honestly but kindly.", "Advice 1: finish the degree first (reason: safety net).", "Advice 2: a business plan, ask an accountant.", "Encouragement: Ό,τι κι αν αποφασίσεις…"],
             model=P("""
                Αγαπητή μου Δάφνη,

                Διάβασα το μήνυμά σου δύο φορές για να βεβαιωθώ ότι κατάλαβα καλά: θέλεις να αφήσεις τη σχολή στο τελευταίο έτος για να ανοίξεις καφέ με τον αδερφό σου! Να σου πω την αλήθεια, ξαφνιάστηκα, αλλά καταλαβαίνω ότι το σκέφτεσαι καιρό.

                Θαυμάζω το θάρρος σου, και η ιδέα σου μού φαίνεται πολύ καλή. Ωστόσο, στη θέση σου δεν θα παρατούσα τις σπουδές μου τώρα. Σου μένουν μόνο λίγα μαθήματα και η πτυχιακή. Γιατί δεν τελειώνεις πρώτα και μετά ασχολείσαι με το καφέ; Το πτυχίο είναι ένα δίχτυ ασφαλείας, αν τα πράγματα δεν πάνε όπως τα θέλεις.

                Επιπλέον, καλό θα ήταν να ετοιμάσετε ένα σοβαρό επιχειρηματικό σχέδιο. Πόσα χρήματα χρειάζεστε; Πόσους πελάτες πρέπει να έχετε κάθε μέρα για να βγάζετε το ενοίκιο; Μπορείς να ζητήσεις συμβουλές από έναν λογιστή ή από ανθρώπους που έχουν ήδη δική τους επιχείρηση.

                Ό,τι κι αν αποφασίσεις, να ξέρεις ότι θα είμαι ο πρώτος σας πελάτης!

                Φιλιά πολλά,
                Στέλιος
             """),
             model_en=P("""
                Dear Dafni,

                I read your message twice to make sure I'd understood: you want to leave university in your final year to open a café with your brother! To tell you the truth, I was taken aback, but I understand you've been thinking about it for a long time.

                I admire your courage, and your idea seems very good to me. However, in your place I wouldn't drop my studies now. You only have a few courses and your dissertation left. Why not finish first and then turn to the café? The degree is a safety net if things don't go the way you want.

                Also, it would be a good idea to put together a serious business plan. How much money do you need? How many customers do you need each day to cover the rent? You could ask an accountant for advice, or people who already have their own business.

                Whatever you decide, you know I'll be your first customer!

                Lots of love,
                Stelios
             """)),
        dict(id="advice-letter-2", level="B2", words=200,
             el="Ένας φίλος σας σας γράφει ότι εδώ και μήνες δεν κοιμάται καλά εξαιτίας του άγχους στη δουλειά. Του γράφετε για να του δείξετε ότι τον καταλαβαίνετε και να του δώσετε συμβουλές. (200 λέξεις)",
             en="A friend writes that for months he hasn't slept well because of stress at work. Write to show you understand and to give advice. (200 words)",
             plan=["Sympathy (Λυπάμαι πολύ που…).", "Three pieces of advice, three different formulas, each with a reason.", "Suggest doing something together; encouragement."]),
        dict(id="advice-letter-3", level="B1+", words=120,
             el="Η ξαδέρφη σας θα επισκεφθεί την πόλη σας για πρώτη φορά. Γράψτε της τι να δει, τι να φάει και τι να αποφύγει. (120 λέξεις)",
             en="Your cousin is visiting your city for the first time. Tell her what to see, what to eat and what to avoid. (120 words)",
             plan=["Imperatives (δες, δοκίμασε, μην πας) mixed with Σου προτείνω να…", "One paragraph each: see, eat, avoid."]),
    ],
)

U06 = dict(
    id="persuade", kind="unit", part="personal", level="B2", el="Γράμμα που πείθει", title="Persuasive letter to a friend",
    intro=[
        {"p": "The first official B2 sample asks you to persuade a rich friend to donate to a shelter. Persuasion letters follow a pattern: make the request early, explain why it matters, show how it will work, **answer the objection before it is made**, and make it easy to say yes (a deadline, a concrete next step)."},
        {"tip": "The official prompt is in the Writing coach shelf with its model answer; write it there after this unit."},
    ],
    structure=[
        ["Άνοιγμα και αίτημα", "Opening and request", "A warm line, then the request in the first paragraph: Σου γράφω γιατί θέλω να σου ζητήσω…"],
        ["Γιατί είναι σημαντικό", "Why it matters", "The cause, the people it helps, a concrete detail."],
        ["Πώς θα γίνει", "How it will work", "Practical details that remove effort for the friend."],
        ["Απάντηση στην αντίρρηση", "Meeting the objection", "Ξέρω τι θα πεις: … Κι όμως, …"],
        ["Τελευταίο επιχείρημα και κλείσιμο", "Final argument and close", "What they gain; a deadline; warm sign-off."],
    ],
    phrases=[
        dict(el="Αίτημα σε φίλο", en="Asking a friend", items=ph(
            ("Θέλω να σου ζητήσω μια μεγάλη χάρη.", "I want to ask you a big favour."),
            ("Θα μου έκανες τεράστια χάρη αν…", "You'd be doing me a huge favour if…"),
            ("Ξέρω ότι είσαι πολύ απασχολημένος, αλλά…", "I know you're very busy, but…"),
            ("Θα σου ήμουν ευγνώμων αν…", "I'd be grateful if…"),
        )),
        dict(el="Πειθώ", en="Persuading", items=ph(
            ("Φαντάσου πόσο…", "Imagine how much…"),
            ("Σκέψου ότι…", "Think that…"),
            ("Το πιο σημαντικό, όμως, είναι…", "The most important thing, though, is…"),
            ("Και κάτι ακόμα: …", "And one more thing: …"),
            ("Ξέρω τι θα πεις: …", "I know what you'll say: …"),
            ("Κι όμως, …", "And yet, …"),
            ("Δεν χρειάζεται παρά να…", "All you need to do is…"),
        )),
        dict(el="Κλείσιμο", en="Closing", items=ph(
            ("Σκέψου το και απάντησέ μου μέχρι…", "Think it over and answer me by…"),
            ("Περιμένω με ανυπομονησία την απάντησή σου.", "I'm looking forward to your answer."),
            ("Ελπίζω να πεις ναι!", "I hope you'll say yes!"),
        )),
    ],
    models=[dict(
        el="Τρέξε μαζί μου!", en="Run with me!", level="B2",
        task_el="Γράφετε σε έναν φίλο σας που δεν αθλείται καθόλου, για να τον πείσετε να τρέξει μαζί σας στον αγώνα των 5 χιλιομέτρων του Μαραθωνίου της Αθήνας, για να μαζέψετε χρήματα για έναν φιλανθρωπικό σύλλογο. Του εξηγείτε γιατί αξίζει, πώς θα προετοιμαστείτε και ό,τι άλλο νομίζετε για να τον πείσετε. (200 λέξεις)",
        task_en="Write to a friend who never exercises, to persuade him to run the 5 km race of the Athens Marathon with you to raise money for a charity. Explain why it's worth it, how you'll prepare and anything else that might persuade him. (200 words)",
        text=P("""
            Αγαπητέ μου Θοδωρή,

            Ελπίζω να είσαι καλά. Σου γράφω γιατί έχω μια πρόταση που, είμαι σίγουρη, στην αρχή θα σε κάνει να γελάσεις: θέλω να τρέξουμε μαζί στον αγώνα των 5 χιλιομέτρων του Μαραθωνίου της Αθήνας, τον Νοέμβριο.

            Ξέρω τι θα πεις: «Εγώ; Που λαχανιάζω όταν ανεβαίνω τις σκάλες;» Κι όμως, τα 5 χιλιόμετρα δεν είναι τόσο δύσκολα όσο φαίνονται. Αν βγαίνουμε τρεις φορές την εβδομάδα για μισή ώρα, ξεκινώντας με γρήγορο περπάτημα, σε δύο μήνες θα είμαστε έτοιμοι χωρίς να ταλαιπωρηθούμε.

            Το πιο σημαντικό, όμως, είναι ο σκοπός. Η ομάδα μας θα τρέξει για τον σύλλογο που στηρίζει παιδιά με χρόνιες ασθένειες. Κάθε δρομέας ζητάει από φίλους και συναδέλφους μια μικρή δωρεά, και όλα τα χρήματα θα πάνε στον σύλλογο, για να αγοράσει ιατρικό εξοπλισμό. Φαντάσου πόσα μπορούμε να μαζέψουμε, αν ο καθένας μας πείσει είκοσι γνωστούς του!

            Και κάτι ακόμα: η άσκηση θα σου κάνει καλό. Μου έλεγες πριν από λίγο καιρό ότι νιώθεις συνέχεια κουρασμένος. Τι καλύτερο από τρεις βόλτες την εβδομάδα με παρέα;

            Σε παρακαλώ, σκέψου το και απάντησέ μου μέχρι την Παρασκευή, για να σε γράψω στην ομάδα.

            Με αγάπη,
            Ρένα
        """),
        text_en=P("""
            Dear Thodoris,

            I hope you're well. I'm writing because I have a proposal that, I'm sure, will make you laugh at first: I want us to run the 5 km race of the Athens Marathon together, in November.

            I know what you'll say: “Me? I get out of breath climbing the stairs!” And yet 5 km isn't as hard as it looks. If we go out three times a week for half an hour, starting with brisk walking, in two months we'll be ready without wearing ourselves out.

            The most important thing, though, is the cause. Our team will run for the association that supports children with chronic illnesses. Each runner asks friends and colleagues for a small donation, and all the money will go to the association to buy medical equipment. Imagine how much we could raise if each of us persuades twenty acquaintances!

            And one more thing: the exercise will do you good. You were telling me not long ago that you feel tired all the time. What could be better than three walks a week in good company?

            Please think about it and answer me by Friday, so I can sign you up for the team.

            With love,
            Rena
        """),
        notes=[
            "**Request in the first paragraph.** The reader knows at once what is being asked.",
            "**The objection is quoted and answered** (Ξέρω τι θα πεις… Κι όμως…): the strongest persuasive move in the letter.",
            "**Each paragraph has one argument**: it's doable, the cause matters, it's good for you. Then a **deadline**.",
            "**ξεκινώντας** (starting) and **χωρίς να ταλαιπωρηθούμε** (without wearing ourselves out): see the grammar note.",
        ],
    )],
    grammar=[dict(
        title="The gerund (-οντας / -ώντας) and χωρίς να",
        en="The gerund (μετοχή) shows how or when something happens, and refers to the subject of the main verb: **-οντας** for verbs stressed on the stem (τρέχω → τρέχοντας), **-ώντας** for verbs in -ώ/-άω (ξεκινώ → ξεκινώντας). It never changes form. For ‘without doing’, use **χωρίς να** + subjunctive.",
        examples=ex(
            ("Ξεκινώντας με περπάτημα, θα είμαστε έτοιμοι σε δύο μήνες.", "Starting with walking, we'll be ready in two months."),
            ("Έμαθε ελληνικά βλέποντας σειρές.", "He learned Greek by watching series."),
            ("Έφυγε χωρίς να πει αντίο.", "She left without saying goodbye."),
        ),
    )],
    drills=[
        q("Πού βάζετε το αίτημα σε ένα γράμμα που πείθει;", ["στην πρώτη παράγραφο", "στο τέλος", "στο υστερόγραφο"], "στην πρώτη παράγραφο"),
        q("Έμαθε να μαγειρεύει ___ τη γιαγιά της.", ["παρακολουθώντας", "παρακολουθόντας", "να παρακολουθεί"], "παρακολουθώντας", "παρακολουθώ is stressed on the ending, so the gerund is -ώντας."),
        q("Έφυγε ___ μας πει τίποτα.", ["χωρίς να", "χωρίς", "για να"], "χωρίς να"),
        q("Ποια φράση προλαβαίνει την αντίρρηση του φίλου;", ["Ξέρω τι θα πεις: δεν έχεις χρόνο.", "Σου στέλνω πολλά φιλιά.", "Τι κάνεις; Πώς είσαι;"], "Ξέρω τι θα πεις: δεν έχεις χρόνο."),
    ],
    tasks=[
        dict(id="persuade-1", level="B2", words=200,
             el="Γράφετε σε μια φίλη σας που είναι μουσικός, για να της ζητήσετε να παίξει χωρίς αμοιβή στη χριστουγεννιάτικη γιορτή του σχολείου όπου πηγαίνει το παιδί σας. Της εξηγείτε για ποιο σκοπό γίνεται η γιορτή, πώς θα οργανωθεί και ό,τι άλλο νομίζετε για να την πείσετε. (200 λέξεις)",
             en="Write to a musician friend asking her to play for free at the Christmas party of your child's school. Explain the purpose, how it will be organised and anything else that might persuade her. (200 words)",
             plan=["Warm opening (compliment her music).", "Request + purpose (what the money is for).", "Practical details you will take care of.", "What she gains + emotional argument.", "Ask for an answer."],
             model=P("""
                Αγαπητή μου Ιφιγένεια,

                Πώς είσαι; Είδα στο διαδίκτυο το βίντεο από τη συναυλία σου στη Θεσσαλονίκη και ενθουσιάστηκα. Μπράβο σου!

                Σου γράφω γιατί θέλω να σου ζητήσω μια μεγάλη χάρη. Ο σύλλογος γονέων του σχολείου όπου πηγαίνει ο γιος μου οργανώνει στις 14 Δεκεμβρίου μια χριστουγεννιάτικη γιορτή στην αυλή του σχολείου. Τα έσοδα θα διατεθούν για την αγορά βιβλίων για τη σχολική βιβλιοθήκη, η οποία, δυστυχώς, είναι σχεδόν άδεια. Θα μου έκανες τεράστια χάρη αν έπαιζες μισή ώρα με την κιθάρα σου, χωρίς αμοιβή.

                Ξέρω ότι είσαι πολύ απασχολημένη αυτή την εποχή, γι' αυτό σου υπόσχομαι ότι θα φροντίσουμε για όλα: το ηχητικό, τη μεταφορά σου και, φυσικά, ένα καλό φαγητό μετά! Σκέψου επίσης ότι θα σε ακούσουν πάνω από διακόσιοι γονείς, ανάμεσα στους οποίους μπορεί να βρεις και καινούργιους θαυμαστές για τις συναυλίες σου.

                Πάνω απ' όλα, όμως, θα δώσεις χαρά σε πολλά παιδιά, που θα έχουν επιτέλους βιβλία να διαβάζουν στα διαλείμματα.

                Περιμένω με ανυπομονησία την απάντησή σου. Ελπίζω να πεις ναι!

                Φιλιά,
                Μυρτώ
             """),
             model_en=P("""
                Dear Ifigenia,

                How are you? I saw the video of your concert in Thessaloniki online and I loved it. Well done!

                I'm writing because I want to ask you a big favour. The parents' association at my son's school is holding a Christmas party in the schoolyard on 14 December. The proceeds will go towards buying books for the school library, which, sadly, is almost empty. You'd be doing me a huge favour if you played for half an hour on your guitar, without a fee.

                I know you're very busy at this time of year, so I promise we'll take care of everything: the sound system, your transport and, of course, a good meal afterwards! Think, too, that more than two hundred parents will hear you, and among them you may find some new fans for your concerts.

                Above all, though, you'll bring joy to a lot of children, who will finally have books to read at break time.

                I'm looking forward to your answer. I hope you'll say yes!

                Love,
                Myrto
             """)),
        dict(id="persuade-2", level="B2", words=200,
             el="Γράφετε στην αδερφή σας για να την πείσετε να υιοθετήσει έναν σκύλο από ένα καταφύγιο ζώων, αντί να αγοράσει κουτάβι από κατάστημα. (200 λέξεις)",
             en="Write to your sister to persuade her to adopt a dog from a shelter instead of buying a puppy from a shop. (200 words)",
             plan=["Request first.", "Two arguments (the animal's life, cost or health).", "Answer her likely objection (a shelter dog will be difficult).", "Offer concrete help: you'll go with her to the shelter."]),
        dict(id="persuade-3", level="C1", words=250,
             el="Γράφετε σε μια παλιά σας καθηγήτρια, με την οποία έχετε χρόνια να επικοινωνήσετε, για να την πείσετε να μιλήσει σε μια εκδήλωση του πολιτιστικού συλλόγου σας. (250 λέξεις)",
             en="Write to a former teacher you haven't been in touch with for years, to persuade her to speak at an event of your cultural association. (250 words)",
             plan=["Semi-formal register: εσείς, but warm (Αγαπητή κυρία…).", "Remind her who you are and what she meant to you.", "The event, the audience, why her in particular.", "Make it easy: date options, travel, length of the talk."]),
    ],
)

U07 = dict(
    id="forum", kind="unit", part="personal", level="B2", el="Ανάρτηση σε φόρουμ", title="Forum post: information and advice",
    intro=[
        {"p": "A forum post answers someone else's question for an audience. Refer to the question, say why you are qualified to answer (your own experience), then give numbered, concrete advice. The tone is friendly and direct, but this is still an exam text: no emojis, no abbreviations, full paragraphs."},
    ],
    structure=[
        ["Χαιρετισμός", "Hello", "Γεια σε όλους! / Καλησπέρα σε όλους!"],
        ["Αναφορά στην ερώτηση", "The question", "Διάβασα την ερώτηση του/της… και αποφάσισα να γράψω, γιατί…"],
        ["Η εμπειρία σας", "Your experience", "One or two sentences: why your advice is worth reading."],
        ["Συμβουλές", "Advice", "Πρώτον… Δεύτερον… Τρίτον… Τέλος…, each with a reason or example."],
        ["Κλείσιμο", "Sign-off", "Ελπίζω να βοήθησα. Καλή επιτυχία! + first name or nickname"],
    ],
    phrases=[
        dict(el="Στο φόρουμ", en="Forum phrases", items=ph(
            ("Διάβασα την ερώτησή σου και αποφάσισα να γράψω.", "I read your question and decided to write."),
            ("Βρέθηκα κι εγώ στην ίδια θέση πριν από…", "I was in the same position… ago."),
            ("Από τη δική μου εμπειρία, …", "From my own experience, …"),
            ("Ίσως σου φανούν χρήσιμα τα εξής: …", "You may find the following useful: …"),
            ("Πρώτον… Δεύτερον… Τρίτον…", "First… Second… Third…"),
            ("Αν θέλεις, στείλε μου μήνυμα για περισσότερες πληροφορίες.", "If you like, message me for more details."),
            ("Ελπίζω να βοήθησα.", "I hope that helped."),
            ("Καλή αρχή και μην τα παρατάς!", "Good luck with the start and don't give up!"),
        )),
    ],
    models=[dict(
        el="Πώς να μάθω ελληνικά μόνος μου;", en="How do I learn Greek on my own?", level="B2",
        task_el="Σε ένα φόρουμ για ξένους που ζουν στην Ελλάδα, κάποιος ρωτάει πώς μπορεί να μάθει ελληνικά μόνος του. Γράφετε μια ανάρτηση με τις συμβουλές σας. (200 λέξεις)",
        task_en="On a forum for foreigners living in Greece, someone asks how to learn Greek on his own. Write a post with your advice. (200 words)",
        text=P("""
            Γεια σε όλους!

            Διάβασα την ερώτηση του Τομ και αποφάσισα να γράψω, γιατί πριν από τρία χρόνια βρισκόμουν κι εγώ στην ίδια θέση. Σήμερα μιλάω ελληνικά αρκετά άνετα, οπότε ίσως σου φανούν χρήσιμα όσα έμαθα.

            Πρώτον, βάλε πρόγραμμα. Είκοσι λεπτά κάθε μέρα είναι πολύ πιο αποτελεσματικά από τρεις ώρες την Κυριακή. Εγώ μελετούσα κάθε πρωί στο μετρό, με μια εφαρμογή για λεξιλόγιο.

            Δεύτερον, μη φοβάσαι τη γραμματική. Οι πτώσεις και τα ρήματα τρομάζουν στην αρχή, αλλά αν μάθεις τους κανόνες σιγά σιγά και κάνεις πολλές ασκήσεις, κάποια στιγμή όλα μπαίνουν στη θέση τους.

            Τρίτον, άκουγε ελληνικά όσο πιο συχνά μπορείς: τραγούδια, ραδιόφωνο, ειδήσεις. Στην αρχή δεν θα καταλαβαίνεις σχεδόν τίποτα, αλλά το αυτί σου θα συνηθίσει τη μελωδία της γλώσσας.

            Τέλος, και πιο σημαντικό, βρες κάποιον να μιλάτε ελληνικά. Εγώ γνώρισα έναν Έλληνα φοιτητή που ήθελε να μάθει αγγλικά και κάναμε ανταλλαγή μια φορά την εβδομάδα. Τα λάθη είναι φυσιολογικά· κανείς δεν θα σε κοροϊδέψει.

            Ελπίζω να βοήθησα. Καλή αρχή και μην τα παρατάς!
            Μαρκ
        """),
        text_en=P("""
            Hello everyone!

            I read Tom's question and decided to write, because three years ago I was in the same position. Today I speak Greek quite comfortably, so you may find what I learned useful.

            First, make a schedule. Twenty minutes every day is far more effective than three hours on Sunday. I studied every morning on the metro, with a vocabulary app.

            Second, don't be afraid of the grammar. Cases and verbs are scary at first, but if you learn the rules bit by bit and do lots of exercises, at some point everything falls into place.

            Third, listen to Greek as often as you can: songs, radio, the news. At first you'll understand almost nothing, but your ear will get used to the melody of the language.

            Finally, and most important, find someone to speak Greek with. I met a Greek student who wanted to learn English and we did an exchange once a week. Mistakes are normal; nobody will laugh at you.

            I hope that helped. Good luck with the start and don't give up!
            Mark
        """),
        notes=[
            "**Credentials in two sentences**: the reader knows why to trust the advice.",
            "**Numbered advice** (Πρώτον, Δεύτερον, Τρίτον, Τέλος) with one example from the writer's life each time.",
            "**Imperatives** carry the advice: βάλε, μη φοβάσαι, άκουγε, βρες. Note **άκουγε** (imperfective: keep listening, habitually) against **βρες** (perfective: find, once).",
        ],
    )],
    grammar=[dict(
        title="Imperatives: aspect and negation",
        en="The **perfective** imperative (βάλε, βρες, γράψε) is for a single action; the **imperfective** (άκουγε, γράφε, διάβαζε) is for habits or ongoing actions. There is no negative imperative: use **μην** + subjunctive (μη φοβάσαι, μην ξεχάσεις). Weak pronouns follow the imperative: **γράψε μου, δώσ' το**.",
        examples=ex(
            ("Γράψε μου όταν φτάσεις.", "Write to me when you arrive. (once)"),
            ("Γράφε μου κάθε εβδομάδα.", "Write to me every week. (habit)"),
            ("Μην ξεχάσεις τα κλειδιά!", "Don't forget the keys!"),
            ("Μη μου πεις!", "You don't say! (literally: don't tell me)"),
        ),
    )],
    drills=[
        q("Συμβουλή για συνήθεια: «___ ελληνικό ραδιόφωνο κάθε μέρα.»", ["Άκουγε", "Άκου", "Ακούσεις"], "Άκουγε", "A daily habit takes the imperfective imperative."),
        q("Πώς λέτε «don't be afraid»;", ["μη φοβάσαι", "μην φοβάσαι", "δεν φοβάσαι"], "μη φοβάσαι", "μη before φ; μην only before a vowel or κ, π, τ, ξ, ψ, γκ, μπ, ντ, τσ, τζ."),
        q("Ποιο ταιριάζει σε ανάρτηση για εξέταση;", ["Ελπίζω να βοήθησα. Καλή επιτυχία!", "χαχα καλή φάση 😀", "ΚΑΛΗ ΕΠΙΤΥΧΙΑ!!!"], "Ελπίζω να βοήθησα. Καλή επιτυχία!"),
        q("___ μου το βιβλίο, σε παρακαλώ.", ["Δώσε", "Δίνεις", "Να δώσει"], "Δώσε"),
    ],
    tasks=[
        dict(id="forum-1", level="B2", words=200,
             el="Σε ένα ταξιδιωτικό φόρουμ, η Λένα ρωτάει πώς μπορεί να κάνει διακοπές στα ελληνικά νησιά χωρίς να ξοδέψει πολλά χρήματα. Γράφετε μια ανάρτηση με τις συμβουλές σας. (200 λέξεις)",
             en="On a travel forum, Lena asks how to holiday on the Greek islands without spending much. Write a post with your advice. (200 words)",
             plan=["Refer to her question; your experience.", "Four tips: when to go, which islands, food, beaches.", "Friendly sign-off."],
             model=P("""
                Καλησπέρα σε όλους!

                Η Λένα ρωτάει πώς μπορεί να κάνει διακοπές στην Ελλάδα χωρίς να ξοδέψει μια περιουσία. Ταξιδεύω στα νησιά κάθε καλοκαίρι με περιορισμένο προϋπολογισμό, οπότε έχω μερικές ιδέες.

                Καταρχάς, απόφυγε τον Αύγουστο. Τον Ιούνιο και τον Σεπτέμβριο ο καιρός είναι ακόμα υπέροχος, η θάλασσα ζεστή, και οι τιμές στα δωμάτια είναι πολύ χαμηλότερες. Επιπλέον, τα νησιά είναι πιο ήσυχα.

                Δεύτερον, προτίμησε τα λιγότερο γνωστά νησιά. Η Σίφνος, η Φολέγανδρος ή η Ικαρία είναι εξίσου όμορφες με τη Μύκονο, αλλά πολύ πιο οικονομικές. Αν κλείσεις τα εισιτήρια του πλοίου νωρίς, θα γλιτώσεις κι εκεί αρκετά χρήματα.

                Τρίτον, για φαγητό απόφυγε τα εστιατόρια στο λιμάνι, που συνήθως είναι ακριβά, και ψάξε τις ταβέρνες όπου τρώνε οι ντόπιοι. Το πρωί μπορείς να αγοράζεις φρούτα και τυρόπιτες από τον φούρνο.

                Τέλος, μην ξεχνάς ότι οι καλύτερες παραλίες είναι δωρεάν, αρκεί να περπατήσεις λίγο!

                Καλά να περάσεις!
                Αντώνης
             """),
             model_en=P("""
                Good evening, everyone!

                Lena asks how she can holiday in Greece without spending a fortune. I travel to the islands every summer on a tight budget, so I have a few ideas.

                First of all, avoid August. In June and September the weather is still wonderful, the sea warm, and room prices are much lower. The islands are also quieter.

                Second, choose the less famous islands. Sifnos, Folegandros or Ikaria are just as beautiful as Mykonos, but much cheaper. If you book your ferry tickets early, you'll save quite a lot there too.

                Third, for food, avoid the restaurants on the harbour, which are usually expensive, and look for the tavernas where the locals eat. In the morning you can buy fruit and cheese pies from the bakery.

                Finally, don't forget that the best beaches are free, as long as you walk a little!

                Have a great time!
                Antonis
             """)),
        dict(id="forum-2", level="B2", words=200,
             el="Σε ένα φόρουμ για εργαζόμενους, κάποιος ρωτάει αν αξίζει να ζητήσει από τον εργοδότη του να δουλεύει από το σπίτι. Γράφετε μια ανάρτηση με τα υπέρ και τα κατά, από τη δική σας εμπειρία. (200 λέξεις)",
             en="On a forum for employees, someone asks whether to ask their employer to work from home. Write a post with the pros and cons from your own experience. (200 words)",
             plan=["Your experience in one or two sentences.", "Two pros, two cons, with examples.", "Your advice: under what conditions it's worth it."]),
        dict(id="forum-3", level="B1+", words=150,
             el="Σε ένα φόρουμ για ζώα, κάποιος ρωτάει τι πρέπει να ξέρει πριν πάρει την πρώτη του γάτα. Γράψτε μια ανάρτηση με τρεις συμβουλές. (150 λέξεις)",
             en="On a pet forum, someone asks what to know before getting their first cat. Write a post with three tips. (150 words)",
             plan=["Imperatives, perfective and imperfective.", "Three tips, each with a reason."]),
    ],
)

ITEMS = [U05, U06, U07]
