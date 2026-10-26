from common import P, ph, q, ex

U12 = dict(
    id="opinion", kind="unit", part="argue", level="B2+", el="Άρθρο γνώμης", title="Opinion article",
    intro=[
        {"p": "The opinion article is the bridge from B2 letters to the Γ1 paper. It has a title, an opening that hooks the reader and states a thesis, two or three body paragraphs with one argument each, a paragraph that **takes the opposing view seriously**, and a conclusion that returns to the thesis in new words. No greeting, no signature."},
    ],
    structure=[
        ["Τίτλος", "Title", "Short, often a question or a contrast: «Κινητό στο σχολείο: απαγόρευση ή εκπαίδευση;»"],
        ["Πρόλογος", "Introduction", "A hook (image, fact, question), the issue, your thesis in one sentence."],
        ["Κύριο μέρος", "Body", "One argument per paragraph: topic sentence, reason, example."],
        ["Αντίλογος", "Counterargument", "Από την άλλη πλευρά… / Βέβαια, δεν μπορεί κανείς να αγνοήσει… then your answer."],
        ["Επίλογος", "Conclusion", "Συνοψίζοντας… / Εν κατακλείδι… The thesis restated, ideally in a memorable final sentence."],
    ],
    phrases=[
        dict(el="Γνώμη", en="Opinion", items=ph(
            ("Κατά τη γνώμη μου, …", "In my opinion, …"),
            ("Είμαι πεπεισμένος ότι…", "I am convinced that…"),
            ("Από τη μεριά μου, θεωρώ ότι…", "For my part, I consider that…"),
        )),
        dict(el="Γενικεύσεις", en="Generalising", items=ph(
            ("Είναι γεγονός ότι…", "It is a fact that…"),
            ("Όλο και περισσότεροι…", "More and more people…"),
            ("Δεν είναι λίγοι εκείνοι που…", "There are quite a few people who…"),
            ("Πρόκειται για…", "It is a matter of…"),
        )),
        dict(el="Αντίλογος", en="Counterargument", items=ph(
            ("Από την άλλη πλευρά, …", "On the other hand, …"),
            ("Βέβαια, δεν μπορεί κανείς να αγνοήσει ότι…", "Of course, one cannot ignore that…"),
            ("Είναι αλήθεια ότι…· ωστόσο…", "It is true that…; however…"),
        )),
        dict(el="Επίλογος", en="Concluding", items=ph(
            ("Συνοψίζοντας, …", "To sum up, …"),
            ("Εν κατακλείδι, …", "In conclusion, …", "Ε"),
            ("Το συμπέρασμα είναι ότι…", "The conclusion is that…"),
        )),
    ],
    models=[dict(
        el="Κινητό στο σχολείο", en="Mobile phones at school", level="B2+",
        task_el="Γράψτε ένα άρθρο γνώμης για ένα περιοδικό με θέμα: «Πρέπει να απαγορεύονται τα κινητά τηλέφωνα στο σχολείο;» (300 λέξεις)",
        task_en="Write an opinion article for a magazine: “Should mobile phones be banned at school?” (300 words)",
        text=P("""
            Κινητό στο σχολείο: απαγόρευση ή εκπαίδευση;

            Πριν από είκοσι χρόνια, το μεγαλύτερο πρόβλημα ενός καθηγητή ήταν τα σημειώματα που περνούσαν οι μαθητές κάτω από τα θρανία. Σήμερα, ο «εχθρός» χωράει σε μια τσέπη. Πολλές χώρες, ανάμεσά τους και η Ελλάδα, απαγόρευσαν τα κινητά τηλέφωνα στις σχολικές αίθουσες. Είναι όμως η απαγόρευση η σωστή απάντηση; Κατά τη γνώμη μου, είναι απαραίτητη, αλλά δεν αρκεί.

            Είναι γεγονός ότι το κινητό διασπά την προσοχή. Ένας μαθητής που κοιτάζει κάθε λίγα λεπτά τις ειδοποιήσεις του δυσκολεύεται να παρακολουθήσει ένα σύνθετο μάθημα ή να διαβάσει ένα μεγάλο κείμενο. Επιπλέον, τα διαλείμματα χωρίς οθόνες ξαναγίνονται χρόνος για παιχνίδι και κουβέντα, κάτι που μόνο θετικό μπορεί να είναι για την κοινωνική ζωή των παιδιών.

            Από την άλλη πλευρά, δεν μπορούμε να κάνουμε ότι η τεχνολογία δεν υπάρχει. Οι μαθητές θα περάσουν όλη τους τη ζωή με μια οθόνη στο χέρι. Αν το σχολείο απλώς κλειδώνει τα κινητά σε ένα ντουλάπι, χάνει την ευκαιρία να τους μάθει πώς να τα χρησιμοποιούν με κρίση: πώς να ξεχωρίζουν μια ψεύτικη είδηση, πώς να προστατεύουν τα προσωπικά τους δεδομένα, πώς να βάζουν οι ίδιοι όρια στον χρόνο τους.

            Επομένως, η απαγόρευση πρέπει να συνοδεύεται από ένα σοβαρό πρόγραμμα ψηφιακής παιδείας, από το δημοτικό κιόλας. Μόνο έτσι οι νέοι θα μάθουν να ελέγχουν την τεχνολογία, αντί να τους ελέγχει εκείνη.

            Συνοψίζοντας, το κινητό δεν έχει θέση στο θρανίο, έχει όμως θέση στο μάθημα. Το σχολείο που απλώς απαγορεύει προστατεύει τους μαθητές για σήμερα· το σχολείο που εκπαιδεύει προετοιμάζει πολίτες για αύριο.
        """),
        text_en=P("""
            Phones at school: ban or education?

            Twenty years ago, a teacher's biggest problem was the notes pupils passed under the desks. Today the “enemy” fits in a pocket. Many countries, Greece among them, have banned mobile phones from classrooms. But is a ban the right answer? In my opinion, it is necessary, but not enough.

            It is a fact that the phone breaks concentration. A pupil who checks notifications every few minutes struggles to follow a complex lesson or read a long text. Moreover, breaks without screens become time for play and conversation again, which can only be good for children's social lives.

            On the other hand, we cannot pretend technology doesn't exist. Pupils will spend their whole lives with a screen in their hand. If school simply locks phones in a cupboard, it misses the chance to teach them how to use them with judgement: how to spot fake news, how to protect their personal data, how to set limits on their own time.

            The ban must therefore come with a serious programme of digital education, starting in primary school. Only then will young people learn to control technology, instead of being controlled by it.

            To sum up, the phone has no place on the desk, but it does have a place in the lesson. A school that simply bans protects its pupils for today; a school that educates prepares citizens for tomorrow.
        """),
        notes=[
            "**Hook → issue → question → thesis** in the first paragraph. The thesis is nuanced (necessary but not enough), which gives the article somewhere to go.",
            "**Argument, counterargument, synthesis**: paragraphs 2, 3 and 4. Paragraph 4 is your own solution, not just a summary.",
            "**The last sentence balances two halves** around the ano teleia: the kind of ending examiners remember.",
            "**κάνω ότι** = pretend (κάνει ότι δεν ακούει, he pretends not to hear).",
        ],
    )],
    grammar=[dict(
        title="Impersonal and generalising structures",
        en="Arguments sound objective when they are not about «εγώ». Use **είναι + adjective + να/ότι** (είναι απαραίτητο να, είναι γεγονός ότι), **πρέπει να**, the passive (**θεωρείται, υποστηρίζεται**), generic **κανείς**, and **αντί να** (instead of) for alternatives.",
        examples=ex(
            ("Είναι απαραίτητο να αλλάξει το σύστημα.", "It is essential that the system change."),
            ("Υποστηρίζεται συχνά ότι οι νέοι δεν διαβάζουν.", "It is often claimed that young people don't read."),
            ("Δεν μπορεί κανείς να αγνοήσει το κόστος.", "One cannot ignore the cost."),
            ("Αντί να απαγορεύουμε, ας εκπαιδεύουμε.", "Instead of banning, let us educate."),
        ),
    )],
    drills=[
        q("Πού διατυπώνετε τη θέση σας σε ένα άρθρο γνώμης;", ["στον πρόλογο", "μόνο στον επίλογο", "πουθενά, το άρθρο πρέπει να είναι ουδέτερο"], "στον πρόλογο"),
        q("___ συχνά ότι η τεχνολογία βλάπτει τα παιδιά.", ["Υποστηρίζεται", "Υποστηρίζω", "Υποστηρίζει"], "Υποστηρίζεται", "The impersonal passive keeps the claim at a distance."),
        q("Ποια φράση ανοίγει τον αντίλογο;", ["Από την άλλη πλευρά, …", "Πρώτα απ' όλα, …", "Συνοψίζοντας, …"], "Από την άλλη πλευρά, …"),
        q("___ να παραπονιόμαστε, ας κάνουμε κάτι.", ["Αντί", "Παρά", "Αφού"], "Αντί"),
    ],
    tasks=[
        dict(id="opinion-1", level="B2+", words=250,
             el="Γράψτε ένα άρθρο γνώμης με θέμα: «Τετραήμερη εργασία: πολυτέλεια ή ανάγκη;» (250 λέξεις)",
             en="Write an opinion article: “The four-day week: luxury or necessity?” (250 words)",
             plan=["Title, hook, thesis.", "Argument 1: health; argument 2: productivity.", "Counterargument: sectors that can't stop; your answer.", "Conclusion with a balanced final sentence."],
             model=P("""
                Τετραήμερη εργασία: πολυτέλεια ή ανάγκη;

                Η ιδέα να δουλεύουμε τέσσερις μέρες την εβδομάδα, χωρίς μείωση μισθού, ακουγόταν μέχρι πριν από λίγα χρόνια σαν ουτοπία. Σήμερα δοκιμάζεται από επιχειρήσεις σε πολλές χώρες. Πιστεύω ότι, παρά τις δυσκολίες, πρόκειται για ένα βήμα προς τη σωστή κατεύθυνση.

                Το πρώτο και ισχυρότερο επιχείρημα αφορά την υγεία των εργαζομένων. Η χρόνια κούραση και το άγχος οδηγούν σε επαγγελματική εξουθένωση, η οποία κοστίζει ακριβά τόσο στους ίδιους όσο και στις επιχειρήσεις. Μια επιπλέον μέρα ξεκούρασης δίνει χρόνο για την οικογένεια, την άσκηση και τα ενδιαφέροντα του καθενός.

                Επιπλέον, οι εργαζόμενοι που ξεκουράζονται συγκεντρώνονται καλύτερα. Σε αρκετά πιλοτικά προγράμματα, οι εταιρείες ανέφεραν ότι η παραγωγικότητα έμεινε σταθερή, παρόλο που οι ώρες λιγόστεψαν.

                Βέβαια, δεν μπορεί κανείς να αγνοήσει τις αντιρρήσεις. Σε ένα νοσοκομείο, σε ένα σούπερ μάρκετ ή σε ένα ξενοδοχείο η εργασία δεν σταματά την Παρασκευή, και η μείωση του ωραρίου σημαίνει περισσότερο προσωπικό, άρα μεγαλύτερο κόστος. Γι' αυτό η αλλαγή δεν μπορεί να γίνει παντού με τον ίδιο τρόπο ούτε από τη μια μέρα στην άλλη.

                Εν κατακλείδι, η τετραήμερη εργασία δεν είναι μαγική λύση, αλλά αξίζει να δοκιμαστεί με σύνεση, κλάδο προς κλάδο. Μια κοινωνία που εργάζεται λιγότερο, αλλά καλύτερα, είναι πιθανότατα και πιο υγιής.
             """),
             model_en=P("""
                The four-day week: luxury or necessity?

                The idea of working four days a week with no cut in pay sounded like a utopia until a few years ago. Today businesses in many countries are trying it. I believe that, despite the difficulties, it is a step in the right direction.

                The first and strongest argument concerns workers' health. Chronic fatigue and stress lead to burnout, which is costly both for workers themselves and for businesses. An extra day of rest gives time for family, exercise and personal interests.

                Moreover, workers who rest concentrate better. In several pilot schemes, companies reported that productivity held steady even though hours fell.

                Of course, one cannot ignore the objections. In a hospital, a supermarket or a hotel, work doesn't stop on Friday, and shorter hours mean more staff, and so higher costs. That is why the change cannot happen everywhere in the same way, nor overnight.

                In conclusion, the four-day week is no magic solution, but it deserves to be tried carefully, sector by sector. A society that works less, but better, is very probably also a healthier one.
             """)),
        dict(id="opinion-2", level="B2+", words=250,
             el="Γράψτε ένα άρθρο γνώμης για τη σχολική εφημερίδα: «Αξίζει να σπουδάσει κανείς στο εξωτερικό;» (250 λέξεις)",
             en="Write an opinion article for a school paper: “Is it worth studying abroad?” (250 words)",
             plan=["Hook with a figure or a personal image.", "Two arguments for, one against, your synthesis.", "Final sentence that answers the title."]),
        dict(id="opinion-3", level="C1", words=300,
             el="Γράψτε ένα άρθρο γνώμης: «Ο μαζικός τουρισμός: ευλογία ή κατάρα για τα ελληνικά νησιά;» (300 λέξεις)",
             en="Write an opinion article: “Mass tourism: blessing or curse for the Greek islands?” (300 words)",
             plan=["Avoid a yes/no answer: what kind of tourism?", "Economic, environmental and social paragraphs.", "Concrete proposals before the conclusion."]),
    ],
)

U13 = dict(
    id="review", kind="unit", part="argue", level="B2+", el="Κριτική", title="Review: book, film, restaurant",
    intro=[
        {"p": "A review informs and judges. Give the facts the reader needs (what, who, where, when), summarise **without giving away the ending**, weigh strengths and weaknesses with examples, and end with a clear recommendation and who it is for. Plot summaries go in the present tense."},
    ],
    structure=[
        ["Τίτλος και βαθμολογία", "Title and rating", "A title that hints at your verdict, and stars if the medium uses them."],
        ["Εισαγωγή", "Introduction", "What it is, who made it, context: Ο Νίκος Καζαντζάκης έγραψε… το 1946."],
        ["Περίληψη", "Summary", "Present tense, no spoilers: Ο αφηγητής αποφασίζει να…"],
        ["Θετικά", "Strengths", "Το μεγαλύτερο προσόν… / Αυτό που με εντυπωσίασε…"],
        ["Αρνητικά", "Weaknesses", "Αν κάτι ενοχλεί… / Το μόνο αρνητικό ήταν…"],
        ["Σύσταση", "Recommendation", "Το συστήνω ανεπιφύλακτα σε όσους…"],
    ],
    phrases=[
        dict(el="Περιγραφή", en="Describing", items=ph(
            ("Η ιστορία διαδραματίζεται στην Κρήτη του 1920.", "The story is set in 1920s Crete."),
            ("Πρωταγωνιστεί ο/η…", "It stars…"),
            ("Η πλοκή περιστρέφεται γύρω από…", "The plot revolves around…"),
            ("Ο αφηγητής / ο ήρωας / η ηρωίδα…", "The narrator / the hero / the heroine…"),
        )),
        dict(el="Αξιολόγηση", en="Evaluating", items=ph(
            ("Το μεγαλύτερο προσόν του βιβλίου είναι…", "The book's greatest strength is…"),
            ("Αυτό που με εντυπωσίασε ήταν…", "What impressed me was…"),
            ("Αν κάτι με ενόχλησε, ήταν…", "If anything bothered me, it was…"),
            ("Το μόνο αρνητικό ήταν…", "The only drawback was…"),
            ("Οι τιμές ήταν λογικές / τσουχτερές.", "The prices were reasonable / steep."),
        )),
        dict(el="Σύσταση", en="Recommending", items=ph(
            ("Το συστήνω ανεπιφύλακτα σε όσους…", "I recommend it unreservedly to anyone who…"),
            ("Αξίζει να το δείτε / διαβάσετε.", "It's worth seeing / reading."),
            ("Θα το πρότεινα μόνο σε…", "I would only suggest it to…"),
        )),
    ],
    models=[dict(
        el="Βίος και πολιτεία του Αλέξη Ζορμπά", en="Zorba the Greek", level="B2+",
        task_el="Γράψτε μια κριτική για ένα ελληνικό βιβλίο που διαβάσατε, για την ιστοσελίδα μιας βιβλιοθήκης. (300 λέξεις)",
        task_en="Write a review of a Greek book you have read, for a library website. (300 words)",
        text=P("""
            Βίος και πολιτεία του Αλέξη Ζορμπά: ένα βιβλίο για όσους φοβούνται να ζήσουν
            ★★★★★

            Πολλοί γνωρίζουν τον Ζορμπά από τη διάσημη ταινία του 1964 και το συρτάκι του Άντονι Κουίν. Λιγότεροι, όμως, έχουν διαβάσει το μυθιστόρημα του Νίκου Καζαντζάκη, που κυκλοφόρησε το 1946. Και είναι κρίμα, γιατί το βιβλίο είναι πολύ πλουσιότερο από την ταινία.

            Ο αφηγητής, ένας νέος διανοούμενος που έχει περάσει τη ζωή του ανάμεσα στα βιβλία, αποφασίζει να ανοίξει ένα ορυχείο λιγνίτη στην Κρήτη. Στο λιμάνι του Πειραιά γνωρίζει τον Αλέξη Ζορμπά, έναν ηλικιωμένο εργάτη με περιπετειώδη ζωή, που τον πείθει να τον πάρει μαζί του. Το ορυχείο είναι μόνο η αφορμή· η πραγματική ιστορία είναι η φιλία των δύο ανδρών και η σύγκρουση δύο τρόπων ζωής.

            Το μεγαλύτερο προσόν του βιβλίου είναι ο ίδιος ο Ζορμπάς. Είναι ένας από τους πιο ζωντανούς ήρωες της ελληνικής λογοτεχνίας: χορεύει όταν δεν βρίσκει λέξεις, τρώει και αγαπά με πάθος και δεν φοβάται ούτε τον θάνατο. Μέσα από τους διαλόγους τους, ο αναγνώστης αναρωτιέται κι εκείνος: ζω πραγματικά ή απλώς σκέφτομαι τη ζωή;

            Αν κάτι ενοχλεί τον σημερινό αναγνώστη, είναι ορισμένες απόψεις για τις γυναίκες, που φανερώνουν την εποχή τους. Επίσης, η γλώσσα του Καζαντζάκη, πλούσια σε κρητικές λέξεις, απαιτεί υπομονή από τον ξένο αναγνώστη.

            Παρ' όλα αυτά, πρόκειται για ένα βιβλίο που αξίζει να διαβάσει κανείς τουλάχιστον μία φορά. Το συστήνω ανεπιφύλακτα, ιδίως σε όσους περνούν τη ζωή τους περιμένοντας την κατάλληλη στιγμή.
        """),
        text_en=P("""
            Zorba the Greek: a book for those who are afraid to live
            ★★★★★

            Many people know Zorba from the famous 1964 film and Anthony Quinn's sirtaki. Fewer, though, have read Nikos Kazantzakis's novel, published in 1946. And that is a pity, because the book is far richer than the film.

            The narrator, a young intellectual who has spent his life among books, decides to open a lignite mine in Crete. In the port of Piraeus he meets Alexis Zorba, an ageing labourer with an adventurous past, who persuades him to take him along. The mine is only the pretext; the real story is the friendship between the two men and the clash of two ways of life.

            The book's greatest strength is Zorba himself. He is one of the most vivid characters in Greek literature: he dances when he cannot find words, eats and loves with passion, and fears not even death. Through their conversations, the reader too wonders: am I really living, or just thinking about life?

            If anything bothers today's reader, it is certain views on women that betray their era. Kazantzakis's language, rich in Cretan words, also demands patience from a foreign reader.

            Even so, this is a book worth reading at least once. I recommend it unreservedly, especially to anyone who spends their life waiting for the right moment.
        """),
        notes=[
            "**The title carries the verdict**, and the last sentence echoes it (φοβούνται να ζήσουν → περιμένοντας την κατάλληλη στιγμή).",
            "**Present tense for the plot** (αποφασίζει, γνωρίζει, πείθει), past for facts about the book (κυκλοφόρησε το 1946).",
            "**Strengths, then weaknesses, then Παρ' όλα αυτά**: the weaknesses make the praise credible.",
            "**όσοι / όσους** (those who): a compact way to say who the book is for.",
        ],
    )],
    grammar=[dict(
        title="όσοι: ‘those who’, ‘anyone who’",
        en="**όσος, -η, -ο** works as a relative pronoun meaning ‘all those who / as many as’. Its case follows its role in the main clause: **σε όσους** (to those who), **όσοι** (those who, subject). Neuter plural **όσα** means ‘everything that’.",
        examples=ex(
            ("Το συστήνω σε όσους αγαπούν την Κρήτη.", "I recommend it to anyone who loves Crete."),
            ("Όσοι ήρθαν νωρίς βρήκαν θέση.", "Those who came early found a seat."),
            ("Σου λέω όσα ξέρω.", "I'm telling you everything I know."),
        ),
    )],
    drills=[
        q("Σε ποιον χρόνο γράφετε συνήθως την περίληψη της πλοκής;", ["στον ενεστώτα", "στον αόριστο", "στον μέλλοντα"], "στον ενεστώτα"),
        q("Το συστήνω σε ___ αγαπούν την ιστορία.", ["όσους", "όσοι", "όσα"], "όσους", "σε + accusative: όσους."),
        q("Ποια φράση εισάγει ένα αρνητικό σημείο;", ["Το μόνο αρνητικό ήταν η αναμονή.", "Το συστήνω ανεπιφύλακτα.", "Η ιστορία διαδραματίζεται στη Σμύρνη."], "Το μόνο αρνητικό ήταν η αναμονή."),
        q("«Η ταινία ___ στη Θεσσαλονίκη του 1940.»", ["διαδραματίζεται", "διαδραματίζει", "παίζεται"], "διαδραματίζεται"),
    ],
    tasks=[
        dict(id="review-1", level="B2", words=200,
             el="Γράψτε μια κριτική για μια ταβέρνα που επισκεφθήκατε, για μια ιστοσελίδα με κριτικές εστιατορίων. (200 λέξεις)",
             en="Write a review of a taverna you visited, for a restaurant review website. (200 words)",
             plan=["Title + stars; where and when you went.", "The setting.", "The food, with specific dishes.", "One drawback, the prices, the recommendation."],
             model=P("""
                Ταβέρνα «Το Κύμα»: απλό, φρέσκο και τίμιο
                ★★★★☆

                Την περασμένη Κυριακή επισκεφθήκαμε με την οικογένειά μου την ταβέρνα «Το Κύμα», που βρίσκεται πάνω στο λιμανάκι της Αγίας Μαρίνας, και ήταν μία από τις πιο ευχάριστες εκπλήξεις του καλοκαιριού.

                Το μαγαζί δεν έχει τίποτα το εντυπωσιακό: λίγα ξύλινα τραπέζια σχεδόν μέσα στο νερό, καρέκλες με ψάθα και ένας μικρός κατάλογος γραμμένος με το χέρι. Αυτό ακριβώς, όμως, είναι και η γοητεία του.

                Το φαγητό ήταν εξαιρετικό. Τα ψάρια ήταν φρέσκα, αφού ο ιδιοκτήτης είναι και ο ίδιος ψαράς, και ψημένα στα κάρβουνα με λίγο λαδολέμονο, όπως πρέπει. Δοκιμάσαμε επίσης γαύρο τηγανητό, χόρτα και μια χωριάτικη σαλάτα με ντομάτες που είχαν πραγματικά γεύση. Για επιδόρπιο, το κατάστημα μάς κέρασε χαλβά.

                Το μόνο αρνητικό ήταν η αναμονή. Επειδή το προσωπικό είναι λίγο, περιμέναμε σχεδόν μία ώρα για τα κυρίως πιάτα. Οι τιμές, πάντως, ήταν λογικές για ψαροταβέρνα: πληρώσαμε περίπου είκοσι πέντε ευρώ το άτομο.

                Συνολικά, τη συστήνω ανεπιφύλακτα σε όσους αναζητούν αυθεντική ελληνική κουζίνα, αρκεί να μη βιάζονται. Κλείστε τραπέζι από πριν, ιδίως τα Σαββατοκύριακα!
             """),
             model_en=P("""
                “To Kyma” taverna: simple, fresh and honest
                ★★★★☆

                Last Sunday my family and I went to the taverna “To Kyma”, right on the little harbour of Agia Marina, and it was one of the nicest surprises of the summer.

                There's nothing showy about the place: a few wooden tables almost in the water, rush-seated chairs and a short handwritten menu. But that is exactly its charm.

                The food was excellent. The fish was fresh, since the owner is a fisherman himself, and grilled over charcoal with a little olive oil and lemon, as it should be. We also tried fried anchovies, greens and a village salad with tomatoes that actually tasted of something. For dessert, the house treated us to halva.

                The only drawback was the wait. Because there are few staff, we waited almost an hour for our main courses. The prices, though, were reasonable for a fish taverna: we paid about twenty-five euros a head.

                All in all, I recommend it unreservedly to anyone looking for authentic Greek cooking, as long as they're not in a hurry. Book a table in advance, especially at weekends!
             """)),
        dict(id="review-2", level="B2+", words=250,
             el="Γράψτε μια κριτική για μια ταινία που είδατε πρόσφατα, για το ιστολόγιο μιας λέσχης κινηματογράφου. (250 λέξεις)",
             en="Write a review of a film you saw recently, for a film club's blog. (250 words)",
             plan=["Title with verdict; director, actors, year.", "Plot in the present, no spoilers.", "Two strengths (acting, music, photography), one weakness.", "Who should see it."]),
        dict(id="review-3", level="C1", words=300,
             el="Γράψτε μια κριτική για μια έκθεση ή μια συναυλία, για το πολιτιστικό ένθετο μιας εφημερίδας. (300 λέξεις)",
             en="Write a review of an exhibition or concert for a newspaper's arts supplement. (300 words)",
             plan=["Context: venue, curator or performers, why it matters now.", "Description with precise vocabulary.", "Argued judgement, not just likes and dislikes."]),
    ],
)

U14 = dict(
    id="essay", kind="unit", part="argue", level="C1", el="Δοκίμιο: υπέρ και κατά", title="Argumentative essay: for and against",
    intro=[
        {"p": "At Γ1 the opinion piece becomes an essay: more formal, more abstract, with arguments weighed on both sides before you reach a position. The marking grid rewards **developed** arguments (claim, reason, evidence), **correlative structures** (αφενός… αφετέρου, μεν… δε, όχι μόνο… αλλά και) and the learned register of written Greek, without pomposity."},
    ],
    structure=[
        ["Πρόλογος", "Introduction", "Context, the question, why it matters now."],
        ["Επιχειρήματα υπέρ", "Arguments for", "Οι υποστηρικτές… τονίζουν… Εξίσου σημαντικό είναι…"],
        ["Επιχειρήματα κατά", "Arguments against", "Οι επικριτές, από την άλλη πλευρά, επισημαίνουν…"],
        ["Προσωπική θέση", "Your position", "Κατά τη γνώμη μου, το δίλημμα… Το ζητούμενο, συνεπώς, είναι…"],
        ["Επίλογος", "Conclusion", "Εν κατακλείδι… with a condition or a perspective."],
    ],
    phrases=[
        dict(el="Παρουσίαση απόψεων", en="Presenting views", items=ph(
            ("Οι υποστηρικτές της άποψης αυτής τονίζουν ότι…", "Supporters of this view stress that…", "Ε"),
            ("Οι επικριτές επισημαίνουν ότι…", "Critics point out that…", "Ε"),
            ("Υποστηρίζεται συχνά ότι…", "It is often argued that…", "Ε"),
            ("Το επιχείρημα αυτό, ωστόσο, παραβλέπει ότι…", "This argument, however, overlooks that…", "Ε"),
        )),
        dict(el="Λόγιες συνδέσεις", en="Learned connectives", items=ph(
            ("αφενός… αφετέρου…", "on the one hand… on the other…", "Ε"),
            ("…μεν…, …δε…", "(balances two clauses)", "Ε"),
            ("Εξίσου σημαντικό είναι το γεγονός ότι…", "Equally important is the fact that…", "Ε"),
            ("Είναι αναμφισβήτητο ότι…", "It is indisputable that…", "Ε"),
            ("Δεν θα πρέπει να παραβλέψουμε ότι…", "We should not overlook that…", "Ε"),
            ("Ως εκ τούτου, …", "Consequently, …", "Ε"),
        )),
        dict(el="Σύνθεση", en="Synthesis", items=ph(
            ("Το δίλημμα «…ή…» είναι ψευδές.", "The dilemma “… or …” is a false one.", "Ε"),
            ("Το ζητούμενο, συνεπώς, είναι…", "What is needed, therefore, is…", "Ε"),
            ("υπό έναν όρο: …", "on one condition: …", "Ε"),
        )),
    ],
    models=[dict(
        el="Τεχνητή νοημοσύνη και εκπαίδευση", en="Artificial intelligence and education", level="C1",
        task_el="Γράψτε ένα δοκίμιο: «Η τεχνητή νοημοσύνη στην εκπαίδευση: απειλή ή εργαλείο;» (350 λέξεις)",
        task_en="Write an essay: “Artificial intelligence in education: threat or tool?” (350 words)",
        text=P("""
            Τεχνητή νοημοσύνη και εκπαίδευση: απειλή ή εργαλείο;

            Μέσα σε λίγα μόλις χρόνια, οι εφαρμογές τεχνητής νοημοσύνης πέρασαν από τα εργαστήρια των πανεπιστημίων στα κινητά των μαθητών. Ένα πρόγραμμα που γράφει μια έκθεση σε δευτερόλεπτα θέτει αναπόφευκτα το ερώτημα: ποιος είναι πια ο ρόλος του σχολείου και του δασκάλου;

            Οι υποστηρικτές της νέας τεχνολογίας τονίζουν, πρώτα απ' όλα, τις δυνατότητες εξατομίκευσης της μάθησης. Ένας ψηφιακός βοηθός μπορεί να εξηγήσει την ίδια άσκηση δέκα φορές, με δέκα διαφορετικούς τρόπους, χωρίς να χάσει την υπομονή του. Αφενός, λοιπόν, ο αδύναμος μαθητής βρίσκει στήριξη· αφετέρου, ο ταχύτερος δεν βαριέται περιμένοντας τους υπόλοιπους. Εξίσου σημαντικό είναι το γεγονός ότι η πρόσβαση σε τέτοια εργαλεία είναι συχνά δωρεάν, γεγονός που θα μπορούσε να μειώσει την εξάρτηση από τα ακριβά φροντιστήρια.

            Οι επικριτές, από την άλλη πλευρά, επισημαίνουν ότι η μάθηση προϋποθέτει προσπάθεια. Όταν ο μαθητής αναθέτει τη σκέψη σε μια μηχανή, παίρνει μεν μια σωστή απάντηση, χάνει δε τη διαδικασία που οδηγεί σε αυτήν. Επιπλέον, τα συστήματα αυτά δεν είναι αλάνθαστα: παρουσιάζουν με απόλυτη βεβαιότητα πληροφορίες που μερικές φορές είναι λανθασμένες, και μόνο ένας αναγνώστης με γνώσεις και κριτική σκέψη μπορεί να τις εντοπίσει.

            Κατά τη γνώμη μου, το δίλημμα «απαγόρευση ή ελευθερία» είναι ψευδές. Η τεχνητή νοημοσύνη δεν θα εξαφανιστεί, όπως δεν εξαφανίστηκαν ούτε οι αριθμομηχανές ούτε το διαδίκτυο. Το ζητούμενο, συνεπώς, είναι να αλλάξει ο τρόπος με τον οποίο διδάσκουμε και αξιολογούμε: περισσότερη προφορική συζήτηση, περισσότερες εργασίες μέσα στην τάξη και ρητή διδασκαλία του πώς ελέγχουμε μια πηγή.

            Εν κατακλείδι, η τεχνολογία αυτή μπορεί να γίνει πολύτιμος σύμμαχος του εκπαιδευτικού, υπό έναν όρο: να μη θεωρηθεί υποκατάστατο της σκέψης, αλλά αφορμή για περισσότερη σκέψη.
        """),
        text_en=P("""
            Artificial intelligence and education: threat or tool?

            In just a few years, artificial intelligence applications have moved from university laboratories to pupils' phones. A program that writes an essay in seconds inevitably raises the question: what is the role of the school and the teacher now?

            Supporters of the new technology stress, first of all, its potential to personalise learning. A digital assistant can explain the same exercise ten times, in ten different ways, without losing patience. On the one hand, then, the weaker pupil finds support; on the other, the faster one isn't bored waiting for the rest. Equally important is the fact that access to such tools is often free, which could reduce dependence on expensive private tutoring.

            Critics, on the other hand, point out that learning requires effort. When a pupil hands thinking over to a machine, they do get a correct answer, but they lose the process that leads to it. Moreover, these systems are not infallible: they present, with complete confidence, information that is sometimes wrong, and only a reader with knowledge and critical thinking can spot it.

            In my view, the dilemma “ban or freedom” is a false one. Artificial intelligence will not disappear, just as neither calculators nor the internet disappeared. What is needed, therefore, is a change in the way we teach and assess: more oral discussion, more work done in class, and explicit teaching of how to check a source.

            In conclusion, this technology can become a valuable ally for teachers, on one condition: that it is not seen as a substitute for thinking, but as an occasion for more thinking.
        """),
        notes=[
            "**Both sides get a full paragraph** with claim, reason and example, before the writer takes a position.",
            "**C1 structures**: αφενός… αφετέρου, μεν… δε, ούτε… ούτε, γεγονός που (a fact which).",
            "**The synthesis rejects the false dilemma** and proposes something concrete: examiners reward a position that goes beyond picking a side.",
            "**φροντιστήρια**: private after-school tutoring centres, a fixture of Greek education.",
        ],
    )],
    grammar=[dict(
        title="Correlatives: αφενός… αφετέρου, μεν… δε, όχι μόνο… αλλά και",
        en="**αφενός… αφετέρου** opens two parallel points. **μεν… δε** is placed second in each clause and balances them, usually with a contrast. **όχι μόνο… αλλά και** adds with emphasis; **τόσο… όσο και** joins two equal items.",
        examples=ex(
            ("Το μέτρο αφενός μειώνει το κόστος, αφετέρου βελτιώνει την ποιότητα.", "The measure on the one hand cuts costs, on the other improves quality."),
            ("Η πρόταση είναι μεν ενδιαφέρουσα, δεν είναι δε ρεαλιστική.", "The proposal is interesting, but it is not realistic."),
            ("Η κρίση επηρέασε όχι μόνο την οικονομία αλλά και την ψυχολογία των πολιτών.", "The crisis affected not only the economy but also people's morale."),
            ("Κοστίζει τόσο στους εργαζόμενους όσο και στις επιχειρήσεις.", "It costs both workers and businesses."),
        ),
    )],
    drills=[
        q("Η πρόταση είναι ___ ενδιαφέρουσα, δεν είναι ___ ρεαλιστική.", ["μεν… δε", "αφού… γιατί", "ούτε… ή"], "μεν… δε"),
        q("Ποια φράση παρουσιάζει την αντίθετη άποψη;", ["Οι επικριτές επισημαίνουν ότι…", "Συνοψίζοντας, …", "Για παράδειγμα, …"], "Οι επικριτές επισημαίνουν ότι…"),
        q("___, λοιπόν, ο αδύναμος μαθητής βρίσκει στήριξη· αφετέρου…", ["Αφενός", "Επομένως", "Μολονότι"], "Αφενός"),
        q("Το λόγιο συνώνυμο του «γι' αυτό» είναι:", ["ως εκ τούτου", "ωστόσο", "εντούτοις"], "ως εκ τούτου", "ωστόσο and εντούτοις mean ‘however’."),
    ],
    tasks=[
        dict(id="essay-1", level="C1", words=300,
             el="Γράψτε ένα δοκίμιο: «Πρέπει οι μεγάλες πόλεις να περιορίσουν τις βραχυχρόνιες μισθώσεις κατοικιών σε τουρίστες;» (300 λέξεις)",
             en="Write an essay: “Should big cities restrict short-term lets to tourists?” (300 words)",
             plan=["Context and question.", "For: income, renovation, local spending.", "Against: rents, displacement, empty neighbourhoods.", "Position: regulation, not a ban; proposals.", "Conclusion with a perspective."],
             model=P("""
                Βραχυχρόνιες μισθώσεις: ανάπτυξη ή απειλή για τις γειτονιές;

                Τα τελευταία χρόνια, χιλιάδες διαμερίσματα στο κέντρο των ελληνικών πόλεων έχουν μετατραπεί σε καταλύματα για τουρίστες, που νοικιάζονται μέσω ψηφιακών πλατφορμών. Το φαινόμενο έχει προκαλέσει έντονη δημόσια συζήτηση: πρέπει το κράτος να το περιορίσει ή να το αφήσει στους νόμους της αγοράς;

                Δεν μπορεί κανείς να αρνηθεί ότι οι βραχυχρόνιες μισθώσεις είχαν θετικές συνέπειες. Κατά τη διάρκεια της οικονομικής κρίσης, πολλές οικογένειες εξασφάλισαν ένα συμπληρωματικό εισόδημα, ενώ παλιά, εγκαταλελειμμένα κτίρια ανακαινίστηκαν. Επιπλέον, οι τουρίστες που μένουν σε γειτονιές και όχι σε ξενοδοχεία ξοδεύουν τα χρήματά τους στα μικρά καταστήματα της περιοχής.

                Ωστόσο, το κόστος είναι εξίσου ορατό. Καθώς οι ιδιοκτήτες προτιμούν τους τουρίστες, που πληρώνουν περισσότερα, οι κατοικίες για μακροχρόνια μίσθωση λιγοστεύουν και τα ενοίκια ανεβαίνουν. Φοιτητές, νέα ζευγάρια και ηλικιωμένοι με χαμηλή σύνταξη αναγκάζονται να μετακομίσουν στα προάστια. Έτσι, ορισμένες ιστορικές γειτονιές κινδυνεύουν να μετατραπούν σε σκηνικά χωρίς κατοίκους, όπου τα καταστήματα με αναμνηστικά παίρνουν τη θέση των φούρνων και των μπακάλικων.

                Κατά τη γνώμη μου, η λύση δεν είναι η πλήρης απαγόρευση, αλλά η ρύθμιση. Ένα όριο στον αριθμό των καταλυμάτων ανά γειτονιά, η αυστηρή φορολόγηση όσων διαθέτουν πολλά ακίνητα και κίνητρα για όσους νοικιάζουν σε μόνιμους κατοίκους θα μπορούσαν να εξισορροπήσουν τα συμφέροντα.

                Συμπερασματικά, ο τουρισμός είναι πολύτιμος για τη χώρα, αλλά μια πόλη δεν είναι μόνο προορισμός· είναι πρώτα απ' όλα ο τόπος όπου ζουν οι άνθρωποί της.
             """),
             model_en=P("""
                Short-term lets: development or threat to neighbourhoods?

                In recent years, thousands of flats in the centres of Greek cities have been turned into tourist accommodation let through digital platforms. The phenomenon has sparked heated public debate: should the state restrict it, or leave it to the laws of the market?

                No one can deny that short-term lets have had positive effects. During the economic crisis, many families secured a supplementary income, and old, abandoned buildings were renovated. Moreover, tourists who stay in neighbourhoods rather than hotels spend their money in the area's small shops.

                However, the cost is just as visible. As owners prefer tourists, who pay more, homes for long-term rent become scarce and rents rise. Students, young couples and pensioners on low incomes are forced to move to the suburbs. Some historic neighbourhoods thus risk becoming stage sets without residents, where souvenir shops take the place of bakeries and grocers.

                In my view, the solution is not an outright ban but regulation. A cap on the number of lets per neighbourhood, strict taxation of those who own many properties and incentives for those who rent to permanent residents could balance the interests involved.

                In conclusion, tourism is valuable for the country, but a city is not only a destination; it is first and foremost the place where its people live.
             """)),
        dict(id="essay-2", level="C1", words=300,
             el="Γράψτε ένα δοκίμιο: «Είναι ο εθελοντισμός καθήκον του πολίτη;» (300 λέξεις)",
             en="Write an essay: “Is volunteering a citizen's duty?” (300 words)",
             plan=["Define the terms (εθελοντισμός, καθήκον).", "For and against, each developed with an example.", "Position with a condition."]),
        dict(id="essay-3", level="C1", words=350,
             el="Γράψτε ένα δοκίμιο: «Απειλεί η παγκοσμιοποίηση τις μικρές γλώσσες, όπως τα ελληνικά;» (350 λέξεις)",
             en="Write an essay: “Does globalisation threaten small languages such as Greek?” (350 words)",
             plan=["Context: English loanwords, the internet, migration.", "Threat arguments; resilience arguments.", "What speakers and the state can do."]),
    ],
)

U15 = dict(
    id="report", kind="unit", part="argue", level="C1", el="Έκθεση αξιολόγησης με προτάσεις", title="Evaluation report with proposals",
    intro=[
        {"p": "The Γ1 paper includes formal reports sent by email (one official sample is an evaluation report). A report is impersonal: a header, a stated purpose and method, findings under headings, numbered proposals, a short conclusion. Prefer passives (**εντοπίστηκαν, προτείνεται**), nouns (**η διατύπωση προτάσεων**) and figures over adjectives."},
    ],
    structure=[
        ["Κεφαλίδα", "Header", "Προς: … / Από: … / Θέμα: …"],
        ["Σκοπός και μέθοδος", "Purpose and method", "Σκοπός της παρούσας έκθεσης είναι… Η αξιολόγηση βασίζεται σε…"],
        ["Ευρήματα", "Findings", "Θετικά σημεία / Αδυναμίες, with numbers and examples."],
        ["Προτάσεις", "Proposals", "Με βάση τα παραπάνω, προτείνεται: – … – …"],
        ["Συμπέρασμα", "Conclusion", "Συνολικά, η εμπειρία κρίνεται… Εφόσον…"],
    ],
    phrases=[
        dict(el="Σκοπός και μέθοδος", en="Purpose and method", items=ph(
            ("Σκοπός της παρούσας έκθεσης είναι…", "The purpose of this report is…", "Ε"),
            ("Η έκθεση συντάχθηκε μετά από αίτημα…", "This report was drawn up at the request of…", "Ε"),
            ("Η αξιολόγηση βασίζεται σε ερωτηματολόγια / συνεντεύξεις.", "The evaluation is based on questionnaires / interviews.", "Ε"),
        )),
        dict(el="Ευρήματα", en="Findings", items=ph(
            ("Η πλειονότητα των ερωτηθέντων δήλωσε ότι…", "Most respondents stated that…", "Ε"),
            ("Ιδιαίτερα θετικά σχόλια συγκέντρωσε…", "Particularly positive comments went to…", "Ε"),
            ("Εντοπίστηκαν, ωστόσο, ορισμένες αδυναμίες.", "Some weaknesses were, however, identified.", "Ε"),
            ("Επισημάνθηκε ότι…", "It was pointed out that…", "Ε"),
        )),
        dict(el="Προτάσεις", en="Proposals", items=ph(
            ("Με βάση τα παραπάνω, προτείνεται…", "On the basis of the above, it is proposed…", "Ε"),
            ("Θα ήταν σκόπιμο να…", "It would be advisable to…", "Ε"),
            ("Εφόσον υιοθετηθούν οι προτάσεις αυτές, …", "Provided these proposals are adopted, …", "Ε"),
        )),
    ],
    models=[dict(
        el="Αξιολόγηση ενός φεστιβάλ", en="Evaluating a festival", level="C1",
        task_el="Είστε μέλος της επιτροπής που αξιολόγησε το καλοκαιρινό φεστιβάλ του δήμου σας. Γράφετε την έκθεση της επιτροπής προς το Τμήμα Πολιτισμού, με τα θετικά, τα προβλήματα και τις προτάσεις σας. (300 λέξεις)",
        task_en="You sat on the committee that evaluated your municipality's summer festival. Write the committee's report to the Culture Department, with strengths, problems and proposals. (300 words)",
        text=P("""
            Προς: Τμήμα Πολιτισμού του Δήμου
            Από: Επιτροπή αξιολόγησης
            Θέμα: Αξιολόγηση του φεστιβάλ «Καλοκαίρι στην πόλη» και προτάσεις για τη βελτίωσή του

            1. Σκοπός
            Σκοπός της παρούσας έκθεσης είναι η αξιολόγηση του φετινού φεστιβάλ, το οποίο πραγματοποιήθηκε από τις 5 έως τις 25 Ιουλίου, καθώς και η διατύπωση προτάσεων για την επόμενη διοργάνωση. Η αξιολόγηση βασίζεται σε ερωτηματολόγια που συμπλήρωσαν 412 θεατές, καθώς και σε συναντήσεις με καλλιτέχνες και εθελοντές.

            2. Θετικά σημεία
            Η συμμετοχή του κοινού ήταν ικανοποιητική, αφού οι περισσότερες εκδηλώσεις είχαν πληρότητα άνω του 80%. Το 74% των ερωτηθέντων αξιολόγησε το καλλιτεχνικό πρόγραμμα ως «πολύ καλό» ή «εξαιρετικό», ενώ ιδιαίτερα θετικά σχόλια συγκέντρωσαν οι δωρεάν συναυλίες στις πλατείες των συνοικιών.

            3. Προβλήματα
            Ωστόσο, εντοπίστηκαν και σημαντικές αδυναμίες. Πρώτον, η ενημέρωση για το πρόγραμμα ήταν ελλιπής: σχεδόν οι μισοί θεατές δήλωσαν ότι πληροφορήθηκαν τις εκδηλώσεις από φίλους και όχι από την ιστοσελίδα του Δήμου. Δεύτερον, οι χώροι δεν ήταν προσβάσιμοι σε άτομα με κινητικά προβλήματα. Τέλος, ο ήχος στις υπαίθριες συναυλίες προκάλεσε διαμαρτυρίες περιοίκων.

            4. Προτάσεις
            Με βάση τα παραπάνω, η επιτροπή προτείνει:
            – τη δημιουργία εφαρμογής για κινητά με το πλήρες πρόγραμμα και ειδοποιήσεις·
            – την εξασφάλιση ραμπών και ειδικών θέσεων σε όλους τους χώρους·
            – τη λήξη των υπαίθριων εκδηλώσεων στις 23:00 και τη συνεργασία με τους συλλόγους κατοίκων.

            5. Συμπέρασμα
            Το φεστιβάλ αποτελεί πλέον θεσμό για την πόλη. Αν υιοθετηθούν οι παραπάνω προτάσεις, η επόμενη διοργάνωση μπορεί να γίνει πιο ανοιχτή και πιο φιλική προς όλους τους δημότες.
        """),
        text_en=P("""
            To: Municipal Culture Department
            From: Evaluation committee
            Subject: Evaluation of the “Summer in the city” festival and proposals for its improvement

            1. Purpose
            The purpose of this report is to evaluate this year's festival, held from 5 to 25 July, and to put forward proposals for the next edition. The evaluation is based on questionnaires completed by 412 audience members and on meetings with artists and volunteers.

            2. Strengths
            Audience turnout was satisfactory, since most events were over 80% full. 74% of respondents rated the artistic programme “very good” or “excellent”, and the free concerts in neighbourhood squares received particularly positive comments.

            3. Problems
            However, significant weaknesses were also identified. First, information about the programme was inadequate: almost half the audience said they heard about the events from friends rather than from the municipal website. Second, the venues were not accessible to people with reduced mobility. Finally, the sound at the open-air concerts led to complaints from local residents.

            4. Proposals
            On the basis of the above, the committee proposes:
            – a mobile app with the full programme and notifications;
            – ramps and dedicated spaces at all venues;
            – an 11 pm finish for open-air events, and cooperation with residents' associations.

            5. Conclusion
            The festival is now an institution for the city. If the above proposals are adopted, the next edition can be more open and more welcoming to all residents.
        """),
        notes=[
            "**Numbered headings** let the reader find findings and proposals at a glance.",
            "**Numbers, not adjectives**: 412 questionnaires, over 80% full, 74% rated it highly.",
            "**Passive and nominal style**: εντοπίστηκαν, η διατύπωση προτάσεων, η εξασφάλιση ραμπών. Proposals as nouns in the accusative after προτείνει.",
            "**των ερωτηθέντων** (of the respondents): a learned participle, one of a handful worth knowing for reports.",
        ],
    )],
    grammar=[dict(
        title="Learned participles in reports",
        en="Reports use a few frozen participles from the learned tradition. Learn them as words: **οι ερωτηθέντες** (respondents), **οι συμμετέχοντες** (participants), **ο προαναφερθείς / η προαναφερθείσα** (the aforementioned), **τα ληφθέντα μέτρα** (the measures taken), **οι ενδιαφερόμενοι** (those interested).",
        examples=ex(
            ("Το 60% των ερωτηθέντων δήλωσε ικανοποιημένο.", "60% of respondents said they were satisfied."),
            ("Οι συμμετέχοντες έλαβαν βεβαίωση.", "Participants received a certificate."),
            ("Τα ληφθέντα μέτρα κρίθηκαν ανεπαρκή.", "The measures taken were judged inadequate."),
        ),
    )],
    drills=[
        q("Ποια φράση ανοίγει μια έκθεση;", ["Σκοπός της παρούσας έκθεσης είναι…", "Γεια σας, θέλω να σας πω…", "Μάντεψε τι έγινε!"], "Σκοπός της παρούσας έκθεσης είναι…"),
        q("Το 70% των ___ δήλωσε ικανοποιημένο.", ["ερωτηθέντων", "ερωτήσεων", "ερωτηθέντες"], "ερωτηθέντων", "Genitive plural after Το 70% των…"),
        q("Ποια διατύπωση ταιριάζει σε έκθεση;", ["Εντοπίστηκαν ορισμένες αδυναμίες.", "Βρήκαμε κάτι χάλια πράγματα.", "Δεν μας άρεσαν κάποια."], "Εντοπίστηκαν ορισμένες αδυναμίες."),
        q("___ υιοθετηθούν οι προτάσεις, η κατάσταση θα βελτιωθεί.", ["Εφόσον", "Ενώ", "Ωστόσο"], "Εφόσον"),
    ],
    tasks=[
        dict(id="report-1", level="C1", words=300,
             el="Είστε εκπρόσωπος των σπουδαστών σε ένα κέντρο ξένων γλωσσών. Η διεύθυνση σας ζήτησε να αξιολογήσετε την ηλεκτρονική πλατφόρμα μαθημάτων που χρησιμοποιήθηκε πιλοτικά το προηγούμενο εξάμηνο. Γράψτε την έκθεσή σας. (300 λέξεις)",
             en="You represent the students at a language school. The management asked you to evaluate the online learning platform piloted last semester. Write your report. (300 words)",
             plan=["Header, purpose and method (survey of how many).", "Strengths with figures.", "Weaknesses with figures or examples.", "Four proposals as a list.", "Conclusion with a condition (Εφόσον…)."],
             model=P("""
                Προς: Διεύθυνση του Κέντρου Ξένων Γλωσσών
                Από: Επιτροπή σπουδαστών
                Θέμα: Αξιολόγηση της νέας ηλεκτρονικής πλατφόρμας μαθημάτων

                Εισαγωγή
                Η παρούσα έκθεση συντάχθηκε μετά από αίτημα της Διεύθυνσης, με σκοπό να αξιολογηθεί η ηλεκτρονική πλατφόρμα που χρησιμοποιήθηκε πιλοτικά κατά το χειμερινό εξάμηνο. Βασίζεται σε σύντομη έρευνα στην οποία απάντησαν 58 σπουδαστές από όλα τα επίπεδα, καθώς και σε συζητήσεις με τους διδάσκοντες.

                Θετικά σημεία
                Η πλειονότητα των σπουδαστών (περίπου 70%) δήλωσε ικανοποιημένη από την ευελιξία που προσφέρει η πλατφόρμα. Η δυνατότητα να παρακολουθεί κανείς ξανά τα βιντεοσκοπημένα μαθήματα θεωρήθηκε ιδιαίτερα χρήσιμη από όσους εργάζονται ή απουσίασαν λόγω ασθένειας. Θετικά αξιολογήθηκαν επίσης οι διαδραστικές ασκήσεις γραμματικής, που διορθώνονται αυτόματα.

                Αδυναμίες
                Παρ' όλα αυτά, επισημάνθηκαν ορισμένα προβλήματα. Αρκετοί σπουδαστές ανέφεραν συχνές διακοπές της σύνδεσης κατά τις ζωντανές συνεδρίες, ενώ οι μεγαλύτεροι σε ηλικία δυσκολεύτηκαν να εξοικειωθούν με το περιβάλλον της εφαρμογής. Επιπλέον, η προφορική εξάσκηση φαίνεται ότι περιορίστηκε σημαντικά, γεγονός που, κατά τους ίδιους τους σπουδαστές, επηρέασε αρνητικά την ευχέρειά τους στον προφορικό λόγο.

                Προτάσεις
                Με βάση τα παραπάνω, προτείνεται:
                – να διατηρηθεί η πλατφόρμα ως συμπλήρωμα και όχι ως υποκατάστατο των δια ζώσης μαθημάτων·
                – να οργανωθεί ένα σύντομο εισαγωγικό σεμινάριο για τους νέους χρήστες·
                – να εξεταστεί η αναβάθμιση της σύνδεσης ή η αλλαγή παρόχου·
                – να προστεθούν εβδομαδιαίες ομάδες συζήτησης σε μικρά τμήματα.

                Συμπέρασμα
                Συνολικά, η εμπειρία κρίνεται θετική. Εφόσον αντιμετωπιστούν τα τεχνικά προβλήματα και ενισχυθεί η προφορική εξάσκηση, η πλατφόρμα μπορεί να αποτελέσει πολύτιμο εργαλείο για όλα τα τμήματα.
             """),
             model_en=P("""
                To: Management, Foreign Language Centre
                From: Student committee
                Subject: Evaluation of the new online learning platform

                Introduction
                This report was drawn up at the request of the management to evaluate the online platform piloted during the winter semester. It is based on a short survey answered by 58 students from all levels, and on discussions with the teachers.

                Strengths
                Most students (around 70%) said they were satisfied with the flexibility the platform offers. Being able to watch recorded lessons again was considered especially useful by those who work or were absent through illness. The interactive grammar exercises, which are marked automatically, were also rated positively.

                Weaknesses
                Nevertheless, some problems were pointed out. Several students reported frequent connection drops during live sessions, while older students found it hard to get used to the app's interface. Moreover, speaking practice appears to have been significantly reduced, which, according to the students themselves, harmed their fluency.

                Proposals
                On the basis of the above, it is proposed:
                – to keep the platform as a supplement to, not a substitute for, face-to-face lessons;
                – to run a short introductory session for new users;
                – to look into upgrading the connection or changing provider;
                – to add weekly small-group conversation classes.

                Conclusion
                Overall, the experience is judged positive. Provided the technical problems are solved and speaking practice is strengthened, the platform can become a valuable tool for all classes.
             """)),
        dict(id="report-2", level="C1", words=300,
             el="Η εταιρεία όπου εργάζεστε έκανε μια έρευνα για την ικανοποίηση του προσωπικού. Γράψτε έκθεση προς τη διοίκηση με τα αποτελέσματα και τις προτάσεις σας. (300 λέξεις)",
             en="Your company ran a staff satisfaction survey. Write a report to management with the results and your proposals. (300 words)",
             plan=["Invent plausible figures and use them.", "Group findings under two or three headings.", "Proposals as nouns or να-clauses, consistently."]),
        dict(id="report-3", level="B2", words=200,
             el="Γράψτε μια σύντομη έκθεση για τον σύλλογο της τάξης σας σχετικά με μια εκδρομή που οργανώσατε: τι πήγε καλά, τι όχι και τι προτείνετε για την επόμενη. (200 λέξεις)",
             en="Write a short report for your class association on a trip you organised: what went well, what didn't, and what you suggest next time. (200 words)",
             plan=["Simple header and purpose.", "Two strengths, two problems.", "Three proposals."]),
    ],
)

U16 = dict(
    id="speech", kind="unit", part="argue", level="C1", el="Ομιλία", title="Speech or address",
    intro=[
        {"p": "A written speech (one official Γ1 sample is an address at a conference) is meant to be heard. Address the audience directly, thank the hosts, announce your topic, organise the body around three points, and use the rhetorical tools of spoken Greek: questions to the audience, repetition (anaphora), groups of three, a concrete image. End with a call to action and thanks."},
    ],
    structure=[
        ["Προσφώνηση", "Address", "Κυρίες και κύριοι, / Αγαπητοί συνάδελφοι, / Αγαπητοί γείτονες, (each group on its own line)"],
        ["Ευχαριστίες και θέμα", "Thanks and topic", "Θα ήθελα, πρώτα απ' όλα, να ευχαριστήσω… Σήμερα θα μιλήσω για…"],
        ["Κύριο μέρος", "Body", "Three points: Πρώτον… Δεύτερον… Τρίτον…, with examples and rhetorical questions."],
        ["Έκκληση", "Call to action", "Σας καλώ, λοιπόν, να… / Την επόμενη φορά που…"],
        ["Ευχαριστίες", "Thanks", "Σας ευχαριστώ για την προσοχή σας."],
    ],
    phrases=[
        dict(el="Άνοιγμα", en="Opening", items=ph(
            ("Κυρίες και κύριοι,", "Ladies and gentlemen,"),
            ("Θα ήθελα, πρώτα απ' όλα, να ευχαριστήσω τους διοργανωτές για την τιμή…", "I would like first of all to thank the organisers for the honour…", "Ε"),
            ("Επιτρέψτε μου να ξεκινήσω με μια ερώτηση.", "Allow me to begin with a question.", "Ε"),
            ("Σήμερα θα προσπαθήσω να…", "Today I will try to…"),
        )),
        dict(el="Ρητορικά μέσα", en="Rhetorical tools", items=ph(
            ("Τι είναι, όμως, …; Δεν είναι απλώς… Είναι…", "But what is…? It is not just… It is…"),
            ("Ποια άλλη… μάς επιτρέπει να…;", "What other… allows us to…?"),
            ("Ευχαριστώ, πρώτα… Ευχαριστώ… Και ευχαριστώ ιδιαίτερα…", "I thank first… I thank… And I especially thank… (anaphora)"),
            ("όσο καλός κι αν είναι", "however good he may be"),
        )),
        dict(el="Κλείσιμο", en="Closing", items=ph(
            ("Σας καλώ, λοιπόν, να…", "I invite you, then, to…", "Ε"),
            ("Και τώρα, ας…", "And now, let us…"),
            ("Σας ευχαριστώ για την προσοχή σας.", "Thank you for your attention."),
            ("Σας ευχαριστώ θερμά.", "Thank you warmly."),
        )),
    ],
    models=[dict(
        el="Γιατί ελληνικά;", en="Why Greek?", level="C1",
        task_el="Σας κάλεσαν να μιλήσετε σε ένα συνέδριο για τη διδασκαλία της ελληνικής ως ξένης γλώσσας. Γράψτε την ομιλία σας για το θέμα: «Γιατί μαθαίνουμε ελληνικά;» (350 λέξεις)",
        task_en="You have been invited to speak at a conference on teaching Greek as a foreign language. Write your speech: “Why do we learn Greek?” (350 words)",
        text=P("""
            Κυρίες και κύριοι,
            αγαπητοί φίλοι της ελληνικής γλώσσας,

            Θα ήθελα, πρώτα απ' όλα, να ευχαριστήσω τους διοργανωτές για την τιμή να μιλήσω σήμερα ενώπιόν σας. Και θα ξεκινήσω με μια ερώτηση που μου κάνουν σχεδόν όλοι όσοι μαθαίνουν ότι σπουδάζω ελληνικά: «Γιατί; Αφού τα μιλούν μόνο δεκατρία εκατομμύρια άνθρωποι!» Σήμερα θα προσπαθήσω να δώσω την απάντηση που δεν πρόλαβα ποτέ να δώσω σε ένα βιαστικό «γιατί».

            Μαθαίνουμε ελληνικά, πρώτον, γιατί δεν μαθαίνουμε απλώς μια γλώσσα· μαθαίνουμε μια ιστορία τριών χιλιάδων χρόνων. Όταν λέω «δημοκρατία», «φιλοσοφία» ή «θέατρο», χρησιμοποιώ λέξεις που γεννήθηκαν σε αυτή τη γλώσσα και ταξίδεψαν σε όλο τον κόσμο. Ποια άλλη ζωντανή γλώσσα μάς επιτρέπει να διαβάζουμε επιγραφές είκοσι πέντε αιώνων και να αναγνωρίζουμε τις λέξεις της καθημερινότητάς μας;

            Μαθαίνουμε ελληνικά, δεύτερον, γιατί μια γλώσσα δεν μετριέται με αριθμούς. Μετριέται με όσα ανοίγει: τα τραγούδια του Θεοδωράκη και του Χατζιδάκι, την ποίηση του Καβάφη και του Σεφέρη, μια κουβέντα με έναν ηλικιωμένο ψαρά σε ένα λιμάνι της Κρήτης. Κανένας μεταφραστής, όσο καλός κι αν είναι, δεν μπορεί να μας δώσει αυτή την εμπειρία.

            Μαθαίνουμε ελληνικά, τρίτον, και πιο προσωπικά, γιατί η ελληνική με έκανε πιο υπομονετικό. Οι πτώσεις, οι τόνοι, τα ανώμαλα ρήματα μού έμαθαν ότι η πρόοδος έρχεται αργά, βήμα βήμα, και ότι κάθε λάθος είναι ένα μάθημα.

            Αγαπητοί φίλοι,
            την επόμενη φορά που κάποιος θα σας ρωτήσει «γιατί ελληνικά;», μην απολογηθείτε. Απαντήστε του με μια λέξη που ξέρει ήδη, χωρίς να το ξέρει: «Από ενθουσιασμό». Γιατί κι αυτή, όπως γνωρίζετε, είναι ελληνική λέξη.

            Σας ευχαριστώ για την προσοχή σας.
        """),
        text_en=P("""
            Ladies and gentlemen,
            dear friends of the Greek language,

            I would like first of all to thank the organisers for the honour of speaking before you today. And I will begin with a question asked by almost everyone who learns that I study Greek: “Why? Only thirteen million people speak it!” Today I will try to give the answer I never had time to give to a hasty “why”.

            We learn Greek, first, because we are not just learning a language; we are learning a history of three thousand years. When I say “democracy”, “philosophy” or “theatre”, I use words that were born in this language and travelled the whole world. What other living language lets us read inscriptions twenty-five centuries old and recognise the words of our daily lives?

            We learn Greek, second, because a language is not measured in numbers. It is measured by what it opens up: the songs of Theodorakis and Hadjidakis, the poetry of Cavafy and Seferis, a conversation with an old fisherman in a Cretan harbour. No translator, however good, can give us that experience.

            We learn Greek, third, and more personally, because Greek has made me more patient. The cases, the accents, the irregular verbs taught me that progress comes slowly, step by step, and that every mistake is a lesson.

            Dear friends,
            the next time someone asks you “why Greek?”, don't apologise. Answer with a word they already know without knowing it: “Out of enthusiasm.” Because that, as you know, is a Greek word too.

            Thank you for your attention.
        """),
        notes=[
            "**Anaphora**: «Μαθαίνουμε ελληνικά, πρώτον… δεύτερον… τρίτον…» gives the listener a map of the speech.",
            "**A rhetorical question** closes the first argument; **concrete names and images** (Θεοδωράκης, a fisherman in Crete) carry the second.",
            "**The ending turns back to the opening question** and gives the audience something to do (μην απολογηθείτε).",
            "**ενθουσιασμός** comes from ancient ἐνθουσιασμός, ‘having the god within’.",
        ],
    )],
    grammar=[dict(
        title="Second-person plural imperatives and let-us forms",
        en="Speeches address the audience with **plural imperatives** (απαντήστε, σκεφτείτε, μην απολογηθείτε) and include the speaker with **ας + subjunctive** (ας κόψουμε, ας ξεκινήσουμε). **Επιτρέψτε μου να…** (allow me to…) is the classic polite opener.",
        examples=ex(
            ("Σκεφτείτε το για ένα λεπτό.", "Think about it for a minute."),
            ("Μην απολογηθείτε.", "Don't apologise."),
            ("Ας κόψουμε όλοι μαζί την κορδέλα.", "Let us all cut the ribbon together."),
            ("Επιτρέψτε μου να σας διηγηθώ μια ιστορία.", "Allow me to tell you a story."),
        ),
    )],
    drills=[
        q("Πώς ξεκινά μια ομιλία σε συνέδριο;", ["Κυρίες και κύριοι,", "Γεια σου!", "Αξιότιμοι κύριοι, σας γράφω…"], "Κυρίες και κύριοι,"),
        q("___ ξεκινήσουμε όλοι μαζί.", ["Ας", "Να ας", "Θα να"], "Ας", "ας + subjunctive: the let-us form."),
        q("___ μου να σας πω μια ιστορία.", ["Επιτρέψτε", "Επιτρέπω", "Επιτρέψει"], "Επιτρέψτε"),
        q("Ποιο ρητορικό μέσο είναι η επανάληψη «Ευχαριστώ… Ευχαριστώ… Ευχαριστώ…»;", ["η αναφορά", "η περίληψη", "η ερώτηση"], "η αναφορά", "Anaphora (αναφορά in Greek rhetoric) is the repetition of a word at the start of successive phrases."),
    ],
    tasks=[
        dict(id="speech-1", level="C1", words=300,
             el="Είστε πρόεδρος του συλλόγου που δημιούργησε έναν κοινοτικό κήπο στη γειτονιά σας. Γράψτε την ομιλία σας στα εγκαίνια. (300 λέξεις)",
             en="You chair the association that created a community garden in your neighbourhood. Write your speech for the opening. (300 words)",
             plan=["Address the audience groups.", "Before and after image.", "Thanks with anaphora.", "What a community garden is (rhetorical question).", "Call for volunteers; ribbon; thanks."],
             model=P("""
                Αγαπητοί γείτονες,
                κύριε Δήμαρχε,
                φίλες και φίλοι,

                Πριν από δύο χρόνια, σε αυτό ακριβώς το σημείο, υπήρχε ένα εγκαταλελειμμένο οικόπεδο γεμάτο σκουπίδια και ξερά χόρτα. Σήμερα στεκόμαστε ανάμεσα σε ντομάτες, βασιλικούς και λεμονιές. Επιτρέψτε μου, λοιπόν, να ξεκινήσω με ένα μεγάλο ευχαριστώ.

                Ευχαριστώ, πρώτα, τους εθελοντές, που αφιέρωσαν τα Σαββατοκύριακά τους για να σκάψουν, να φυτέψουν και να ποτίσουν. Ευχαριστώ τον Δήμο, που μας παραχώρησε τον χώρο και το νερό. Και ευχαριστώ ιδιαίτερα τα παιδιά του δημοτικού σχολείου, που ζωγράφισαν τις πινακίδες που βλέπετε γύρω σας.

                Τι είναι, όμως, ένας κοινοτικός κήπος; Δεν είναι απλώς ένα κομμάτι γης όπου καλλιεργούμε λαχανικά. Είναι ένας τόπος συνάντησης. Εδώ η κυρία Ελένη, που ζει στη γειτονιά πενήντα χρόνια, μαθαίνει στους φοιτητές πότε φυτεύονται τα κρεμμύδια. Εδώ οικογένειες που ήρθαν πρόσφατα από άλλες χώρες μοιράζονται σπόρους από τους δικούς τους τόπους. Σε μια πόλη όπου συχνά δεν ξέρουμε ούτε το όνομα του διπλανού μας, ο κήπος μάς θυμίζει ότι είμαστε κοινότητα.

                Ο κήπος, ωστόσο, δεν τελειώνει σήμερα· σήμερα αρχίζει. Χρειαζόμαστε χέρια για το πότισμα το καλοκαίρι, ιδέες για εργαστήρια με τα σχολεία και, πάνω απ' όλα, ανθρώπους που θα τον αγαπήσουν και θα τον φροντίσουν. Σας καλώ, λοιπόν, να γραφτείτε στη λίστα των εθελοντών που θα βρείτε στην είσοδο.

                Και τώρα, ας κόψουμε όλοι μαζί την κορδέλα και ας δοκιμάσουμε τις πρώτες μας ντομάτες!

                Σας ευχαριστώ θερμά.
             """),
             model_en=P("""
                Dear neighbours,
                Mr Mayor,
                friends,

                Two years ago, on this very spot, there was an abandoned plot full of rubbish and dry weeds. Today we stand among tomatoes, basil and lemon trees. Allow me, then, to begin with a big thank-you.

                I thank, first, the volunteers, who gave up their weekends to dig, plant and water. I thank the Municipality, which gave us the space and the water. And I especially thank the children of the primary school, who painted the signs you see around you.

                But what is a community garden? It is not just a piece of land where we grow vegetables. It is a meeting place. Here Mrs Eleni, who has lived in the neighbourhood for fifty years, teaches students when onions are planted. Here families who have recently arrived from other countries share seeds from their own homelands. In a city where we often don't even know our neighbour's name, the garden reminds us that we are a community.

                The garden, however, does not end today; today it begins. We need hands for watering in summer, ideas for workshops with the schools and, above all, people who will love it and look after it. I invite you, then, to sign up on the volunteers' list at the entrance.

                And now, let us all cut the ribbon together and taste our first tomatoes!

                Thank you warmly.
             """)),
        dict(id="speech-2", level="C1", words=300,
             el="Μιλάτε σε μια ημερίδα του δήμου σας για την κλιματική αλλαγή. Γράψτε μια ομιλία για το τι μπορεί να κάνει η τοπική κοινωνία. (300 λέξεις)",
             en="You are speaking at a municipal day conference on climate change. Write a speech on what the local community can do. (300 words)",
             plan=["Address and thanks.", "A local, concrete image of the problem.", "Three actions, anaphora.", "Call to action."]),
        dict(id="speech-3", level="B2", words=150,
             el="Γράψτε μια σύντομη πρόποση (150 λέξεις) για τον γάμο ενός φίλου σας.", en="Write a short toast (150 words) for a friend's wedding.",
             plan=["Who you are and how you know the couple.", "One funny or tender memory.", "Wishes: Να ζήσετε! Καλά στέφανα is said before; after the wedding: Να ζήσετε, να ευτυχήσετε!"]),
    ],
)

ITEMS = [U12, U13, U14, U15, U16]
