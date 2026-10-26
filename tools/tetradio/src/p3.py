from common import P, ph, q, ex

U08 = dict(
    id="complaint", kind="unit", part="formal", level="B2", el="Επιστολή παραπόνων", title="Letter of complaint",
    intro=[
        {"p": "Complaints are a named Part B genre («να εκφράζει αιτιολογημένα παράπονα»). The key word is **αιτιολογημένα**: give dates, facts and consequences, stay polite and firm, and say exactly what you want done and by when. Anger is shown through vocabulary (έντονη δυσαρέσκεια, απαράδεκτο), never through exclamation marks."},
    ],
    structure=[
        ["Προσφώνηση", "Greeting", "Αξιότιμε κύριε / Αξιότιμη κυρία + surname, or Αξιότιμοι κύριοι,"],
        ["Σκοπός", "Purpose", "Σας γράφω για να εκφράσω την έντονη δυσαρέσκειά μου για…"],
        ["Τα γεγονότα", "The facts", "What, when, where, in order: Στις 3 Οκτωβρίου… Μία εβδομάδα αργότερα…"],
        ["Οι συνέπειες", "Consequences", "Why it matters to you: Η κατάσταση αυτή μου έχει προκαλέσει…"],
        ["Το αίτημα", "What you want", "Ζητώ / Σας παρακαλώ να… εντός… ημερών. Σε διαφορετική περίπτωση…"],
        ["Κλείσιμο", "Sign-off", "Με εκτίμηση, + invented name"],
    ],
    phrases=[
        dict(el="Σκοπός και δυσαρέσκεια", en="Purpose and displeasure", items=ph(
            ("Σας γράφω για να εκφράσω την έντονη δυσαρέσκειά μου για…", "I am writing to express my strong dissatisfaction with…", "Ε"),
            ("Θα ήθελα να διαμαρτυρηθώ για…", "I would like to complain about…", "Ε"),
            ("Θεωρώ απαράδεκτο το γεγονός ότι…", "I find it unacceptable that…", "Ε"),
            ("Δυστυχώς, παρά τις επανειλημμένες προσπάθειές μου, …", "Unfortunately, despite my repeated attempts, …", "Ε"),
        )),
        dict(el="Γεγονότα και συνέπειες", en="Facts and consequences", items=ph(
            ("Στις… παρήγγειλα / επισκέφθηκα / αγόρασα…", "On… I ordered / visited / bought…"),
            ("Μου υποσχέθηκαν ότι…, κάτι που δεν έγινε ποτέ.", "I was promised that…, which never happened."),
            ("Όπως καταλαβαίνετε, η κατάσταση αυτή μου έχει προκαλέσει…", "As you will appreciate, this situation has caused me…", "Ε"),
        )),
        dict(el="Αίτημα", en="The demand", items=ph(
            ("Σας παρακαλώ να με ενημερώσετε εντός πέντε εργάσιμων ημερών.", "Please inform me within five working days.", "Ε"),
            ("Ζητώ την αντικατάσταση του προϊόντος ή την επιστροφή των χρημάτων μου.", "I request a replacement or a refund.", "Ε"),
            ("Σε διαφορετική περίπτωση, θα αναγκαστώ να…", "Otherwise I shall be obliged to…", "Ε"),
            ("Είμαι βέβαιος ότι θα δείξετε την απαραίτητη κατανόηση.", "I am sure you will show the necessary understanding.", "Ε"),
        )),
    ],
    models=[dict(
        el="Ένας χαλασμένος υπολογιστής", en="A faulty laptop", level="B2",
        task_el="Αγοράσατε από ένα ηλεκτρονικό κατάστημα έναν φορητό υπολογιστή, που παρουσίασε πρόβλημα την πρώτη εβδομάδα. Γράφετε στον υπεύθυνο εξυπηρέτησης πελατών για να διαμαρτυρηθείτε και να ζητήσετε λύση. (200 λέξεις)",
        task_en="You bought a laptop from an online shop and it broke down in the first week. Write to the customer service manager to complain and ask for a solution. (200 words)",
        text=P("""
            Αξιότιμε κύριε,

            Σας γράφω για να εκφράσω την έντονη δυσαρέσκειά μου για ένα προϊόν που αγόρασα από το κατάστημά σας και για τον τρόπο με τον οποίο αντιμετωπίστηκε το πρόβλημά μου.

            Στις 3 Οκτωβρίου παρήγγειλα από την ιστοσελίδα σας έναν φορητό υπολογιστή, τον οποίο παρέλαβα δύο μέρες αργότερα. Μόλις μία εβδομάδα μετά, η οθόνη άρχισε να σβήνει χωρίς λόγο, ενώ η μπαταρία δεν κρατούσε περισσότερο από μία ώρα. Επικοινώνησα αμέσως με την εξυπηρέτηση πελατών, όπου μου υποσχέθηκαν ότι θα με καλέσει τεχνικός μέσα σε δύο ημέρες. Δυστυχώς, κανείς δεν επικοινώνησε μαζί μου, παρόλο που τηλεφώνησα άλλες τρεις φορές.

            Όπως καταλαβαίνετε, η κατάσταση αυτή μου έχει προκαλέσει σοβαρά προβλήματα, καθώς χρησιμοποιώ τον υπολογιστή για τη δουλειά μου. Θεωρώ απαράδεκτο ένα κατάστημα με τη φήμη σας να αγνοεί με αυτόν τον τρόπο τους πελάτες του.

            Σύμφωνα με την εγγύηση, έχω το δικαίωμα να ζητήσω την αντικατάσταση του προϊόντος ή την επιστροφή των χρημάτων μου. Σας παρακαλώ, λοιπόν, να με ενημερώσετε εντός πέντε εργάσιμων ημερών για τη λύση που προτείνετε. Σε διαφορετική περίπτωση, θα αναγκαστώ να απευθυνθώ στον Συνήγορο του Καταναλωτή.

            Με εκτίμηση,
            Π. Αλεξίου
        """),
        text_en=P("""
            Dear Sir,

            I am writing to express my strong dissatisfaction with a product I bought from your shop and with the way my problem was handled.

            On 3 October I ordered a laptop from your website, which I received two days later. Just one week afterwards, the screen began to switch off for no reason, while the battery lasted no more than an hour. I contacted customer service at once, where I was promised that a technician would call me within two days. Unfortunately, nobody contacted me, although I phoned three more times.

            As you will appreciate, this situation has caused me serious problems, since I use the computer for my work. I find it unacceptable that a shop with your reputation should ignore its customers in this way.

            Under the guarantee, I am entitled to ask for the product to be replaced or my money refunded. I would therefore ask you to inform me within five working days of the solution you propose. Otherwise, I shall be obliged to turn to the Consumer Ombudsman.

            Yours sincerely,
            P. Alexiou
        """),
        notes=[
            "**Five paragraphs, five jobs**: purpose, facts in date order, consequences, demand with deadline, sign-off.",
            "**Firm but polite**: the anger is in the vocabulary (έντονη δυσαρέσκεια, απαράδεκτο), not in exclamation marks or insults.",
            "**The threat is institutional**: the Συνήγορος του Καταναλωτή is Greece's independent authority for consumer disputes, a credible next step.",
            "**αντιμετωπίστηκε, υποσχέθηκαν, αναγκαστώ, απευθυνθώ**: formal letters lean on passive and deponent aorists. See the grammar note.",
        ],
    )],
    grammar=[dict(
        title="Passive aorists in formal letters",
        en="Formal Greek uses the passive to put the problem, not the person, in focus. Learn the aorist stems: **-θηκα / -τηκα** in the past (αντιμετωπίστηκε, στάλθηκε), **-θώ / -τώ** after να and θα (να αντικατασταθεί, θα επιστραφούν).",
        examples=ex(
            ("Το δέμα στάλθηκε σε λάθος διεύθυνση.", "The parcel was sent to the wrong address."),
            ("Ζητώ να αντικατασταθεί το προϊόν.", "I request that the product be replaced."),
            ("Τα χρήματα θα επιστραφούν στον λογαριασμό σας.", "The money will be returned to your account."),
            ("Θα αναγκαστώ να απευθυνθώ στις αρμόδιες αρχές.", "I shall be obliged to turn to the competent authorities."),
        ),
    )],
    drills=[
        q("Ποια φράση ανοίγει μια επιστολή παραπόνων;", ["Σας γράφω για να εκφράσω τη δυσαρέσκειά μου για…", "Γεια σας! Έχω ένα θέμα…", "Είστε απαράδεκτοι!!!"], "Σας γράφω για να εκφράσω τη δυσαρέσκειά μου για…"),
        q("Ζητώ να μου ___ τα χρήματα.", ["επιστραφούν", "επιστρέφουν", "επέστρεψαν"], "επιστραφούν", "να + passive perfective subjunctive."),
        q("Ποιο αίτημα είναι καλύτερο;", ["Σας παρακαλώ να με ενημερώσετε εντός πέντε εργάσιμων ημερών.", "Κάντε κάτι γρήγορα.", "Περιμένω, αν θέλετε, μια απάντηση κάποια στιγμή."], "Σας παρακαλώ να με ενημερώσετε εντός πέντε εργάσιμων ημερών.", "Specific, polite, with a deadline."),
        q("Τηλεφώνησα πολλές φορές, ___ κανείς δεν απάντησε.", ["αλλά", "γιατί", "για να"], "αλλά"),
    ],
    tasks=[
        dict(id="complaint-1", level="B2", words=200,
             el="Γράφετε στον δήμαρχο της πόλης σας, εκ μέρους των κατοίκων του δρόμου σας, για να διαμαρτυρηθείτε επειδή τα σκουπίδια δεν μαζεύονται τακτικά και ο δρόμος δεν φωτίζεται τη νύχτα. Ζητάτε συγκεκριμένα μέτρα. (200 λέξεις)",
             en="Write to your mayor, on behalf of the residents of your street, to complain that rubbish isn't collected regularly and the street is unlit at night. Ask for specific measures. (200 words)",
             plan=["Who you are and on whose behalf.", "Problem 1 + consequence; problem 2 + consequence.", "What you have already tried.", "Two specific demands; polite confidence."],
             model=P("""
                Αξιότιμε κύριε Δήμαρχε,

                Είμαι κάτοικος της οδού Ανεμώνης και σας γράφω εκ μέρους πολλών γειτόνων μου, για να διαμαρτυρηθώ για την κατάσταση που επικρατεί στον δρόμο μας εδώ και δύο μήνες.

                Πρώτον, τα σκουπίδια δεν μαζεύονται τακτικά. Οι κάδοι είναι γεμάτοι για μέρες, με αποτέλεσμα να υπάρχει έντονη δυσοσμία και να εμφανίζονται ποντίκια, κάτι που είναι επικίνδυνο κυρίως για τα παιδιά που παίζουν στην πλατεία. Δεύτερον, τρεις από τις λάμπες του δημοτικού φωτισμού είναι καμένες από τον Σεπτέμβριο. Τα βράδια ο δρόμος είναι σκοτεινός, και οι ηλικιωμένοι φοβούνται να βγουν από τα σπίτια τους.

                Έχουμε ήδη τηλεφωνήσει αρκετές φορές στις αρμόδιες υπηρεσίες του Δήμου, χωρίς όμως κανένα αποτέλεσμα.

                Γι' αυτό σας παρακαλούμε να φροντίσετε ώστε τα σκουπίδια να μαζεύονται τουλάχιστον τρεις φορές την εβδομάδα και να αντικατασταθούν το συντομότερο δυνατόν οι λάμπες. Είμαστε βέβαιοι ότι θα δείξετε την απαραίτητη κατανόηση.

                Με εκτίμηση,
                Ε. Κωνσταντίνου
                εκ μέρους των κατοίκων της οδού Ανεμώνης
             """),
             model_en=P("""
                Dear Mayor,

                I am a resident of Anemonis Street and I am writing on behalf of many of my neighbours to complain about the situation on our street over the past two months.

                Firstly, the rubbish is not collected regularly. The bins stay full for days, with the result that there is a strong smell and rats appear, which is dangerous above all for the children who play in the square. Secondly, three of the street lamps have been burnt out since September. In the evenings the street is dark, and elderly residents are afraid to leave their homes.

                We have already phoned the relevant municipal services several times, but without any result.

                We therefore ask you to ensure that the rubbish is collected at least three times a week and that the lamps are replaced as soon as possible. We are confident that you will show the necessary understanding.

                Yours sincerely,
                E. Konstantinou
                on behalf of the residents of Anemonis Street
             """)),
        dict(id="complaint-2", level="B2", words=200,
             el="Περάσατε μια εβδομάδα σε ένα ξενοδοχείο που δεν ήταν καθόλου όπως το περιέγραφε η ιστοσελίδα του. Γράφετε στον διευθυντή για να διαμαρτυρηθείτε και να ζητήσετε αποζημίωση. (200 λέξεις)",
             en="You spent a week at a hotel that was nothing like its website. Write to the manager to complain and ask for compensation. (200 words)",
             plan=["Dates of stay, booking reference.", "Three differences between promise and reality.", "Consequences for your holiday.", "Demand: partial refund within a deadline."]),
        dict(id="complaint-3", level="B2+", words=220,
             el="Η αεροπορική εταιρεία έχασε τη βαλίτσα σας και, δέκα μέρες μετά, δεν έχετε καμία ενημέρωση. Γράφετε στο τμήμα εξυπηρέτησης πελατών. (220 λέξεις)",
             en="The airline lost your suitcase and, ten days later, you have had no news. Write to customer service. (220 words)",
             plan=["Flight details and claim number.", "What you have done and been told.", "Expenses you have had to cover.", "Demand: tracking, reimbursement of expenses, deadline."]),
    ],
)

U09 = dict(
    id="request", kind="unit", part="formal", level="B2", el="Επίσημο αίτημα", title="Formal request: permission, an exception, information",
    intro=[
        {"p": "The second official Part B genre asks for something: leave, permission, an exception, information («να ζητά αιτιολογημένη άδεια»). Again the key is **αιτιολογημένη**: who you are, what exactly you ask, why, and why it is reasonable to agree. Offer guarantees and make the recipient's answer easy."},
    ],
    structure=[
        ["Προσφώνηση", "Greeting", "Αξιότιμε κύριε Καθηγητά, / Κύριε Διαχειριστή, / Αξιότιμοι κύριοι,"],
        ["Ποιος είστε και τι ζητάτε", "Who you are, what you ask", "Ονομάζομαι… και είμαι… Σας γράφω σχετικά με…"],
        ["Αιτιολόγηση", "Reasons", "What happened or why you need it; evidence (επισυνάπτω…)."],
        ["Το αίτημα", "The request itself", "Θα σας ήμουν ευγνώμων αν… / Θα ήθελα να σας παρακαλέσω να…"],
        ["Εγγυήσεις", "Guarantees", "Why saying yes costs them nothing: Θέλω να σας διαβεβαιώσω ότι…"],
        ["Κλείσιμο", "Close", "Είμαι στη διάθεσή σας για… Σας ευχαριστώ εκ των προτέρων. Με εκτίμηση / Με τιμή,"],
    ],
    phrases=[
        dict(el="Αίτημα", en="Requesting", items=ph(
            ("Σας γράφω σχετικά με…", "I am writing regarding…", "Ε"),
            ("Θα ήθελα να σας ζητήσω την άδεια να…", "I would like to ask your permission to…", "Ε"),
            ("Θα σας ήμουν ιδιαίτερα ευγνώμων αν μου επιτρέπατε να…", "I would be most grateful if you allowed me to…", "Ε"),
            ("Θα σας παρακαλούσα να εξετάσετε το ενδεχόμενο να…", "I would ask you to consider the possibility of…", "Ε"),
        )),
        dict(el="Αιτιολόγηση και εγγυήσεις", en="Reasons and guarantees", items=ph(
            ("Ο λόγος είναι ότι…", "The reason is that…"),
            ("Επισυνάπτω τη σχετική βεβαίωση.", "I attach the relevant certificate.", "Ε"),
            ("Θέλω να σας διαβεβαιώσω ότι…", "I want to assure you that…", "Ε"),
            ("Θα τηρηθούν όλοι οι κανόνες.", "All the rules will be observed.", "Ε"),
        )),
        dict(el="Κλείσιμο", en="Closing", items=ph(
            ("Είμαι στη διάθεσή σας για οποιαδήποτε επιπλέον πληροφορία.", "I am at your disposal for any further information.", "Ε"),
            ("Σας ευχαριστώ εκ των προτέρων για την κατανόησή σας.", "Thank you in advance for your understanding.", "Ε"),
            ("Με τιμή,", "Respectfully, (applications to an authority)", "Ε"),
        )),
    ],
    models=[dict(
        el="Εξέταση σε άλλη ημερομηνία", en="Sitting an exam on another date", level="B2",
        task_el="Είστε φοιτητής σε ελληνικό πανεπιστήμιο. Λόγω ενός σοβαρού προβλήματος υγείας δεν μπορέσατε να δώσετε ένα μάθημα στην εξεταστική. Γράφετε στον καθηγητή του μαθήματος για να του εξηγήσετε τι συνέβη και να του ζητήσετε να εξεταστείτε σε άλλη ημερομηνία. (200 λέξεις)",
        task_en="You are a student at a Greek university. Because of a serious health problem you missed an exam. Write to the professor to explain and ask to sit it on another date. (200 words)",
        text=P("""
            Αξιότιμε κύριε Καθηγητά,

            Ονομάζομαι Λουκάς Μαρκόπουλος και είμαι φοιτητής του τρίτου έτους του Τμήματος Ιστορίας. Σας γράφω σχετικά με την εξέταση του μαθήματος «Νεότερη Ελληνική Ιστορία», η οποία πραγματοποιήθηκε στις 2 Φεβρουαρίου.

            Δυστυχώς, δεν μπόρεσα να παρευρεθώ στην εξέταση, καθώς το προηγούμενο βράδυ μεταφέρθηκα στο νοσοκομείο με οξεία σκωληκοειδίτιδα και χειρουργήθηκα την ίδια νύχτα. Παρέμεινα στο νοσοκομείο τέσσερις ημέρες. Επισυνάπτω τη σχετική ιατρική βεβαίωση, όπου αναφέρονται οι ημερομηνίες της νοσηλείας μου.

            Γνωρίζω ότι ο κανονισμός σπουδών δεν προβλέπει επαναληπτική εξέταση πριν από τον Σεπτέμβριο. Ωστόσο, θα σας ήμουν ιδιαίτερα ευγνώμων αν μου επιτρέπατε να εξεταστώ σε κάποια ημερομηνία της επιλογής σας μέσα στο τρέχον εξάμηνο, είτε γραπτώς είτε προφορικά. Το μάθημα είναι προαπαιτούμενο για δύο μαθήματα του επόμενου έτους, και μια καθυστέρηση θα επηρέαζε σημαντικά την πρόοδο των σπουδών μου.

            Είμαι στη διάθεσή σας για οποιαδήποτε επιπλέον πληροφορία ή δικαιολογητικό χρειαστείτε.

            Σας ευχαριστώ εκ των προτέρων για την κατανόησή σας.

            Με τιμή,
            Λουκάς Μαρκόπουλος
        """),
        text_en=P("""
            Dear Professor,

            My name is Loukas Markopoulos and I am a third-year student in the Department of History. I am writing about the exam for the course “Modern Greek History”, which took place on 2 February.

            Unfortunately, I was unable to attend the exam, as the evening before I was taken to hospital with acute appendicitis and operated on that same night. I remained in hospital for four days. I attach the medical certificate, which states the dates of my stay.

            I am aware that the study regulations do not provide for a resit before September. However, I would be most grateful if you allowed me to sit the exam on a date of your choice within the current semester, either in writing or orally. The course is a prerequisite for two courses next year, and a delay would seriously affect the progress of my studies.

            I am at your disposal for any further information or documents you may need.

            Thank you in advance for your understanding.

            Respectfully,
            Loukas Markopoulos
        """),
        notes=[
            "**Identity and subject first**, so the professor knows at once which student and which exam.",
            "**Evidence** (επισυνάπτω τη σχετική ιατρική βεβαίωση) turns the request into a reasonable one.",
            "**The rule is acknowledged before the exception is asked for** (Γνωρίζω ότι… Ωστόσο…), and the request is flexible: a date of your choice, written or oral.",
            "In the exam you would sign with an invented name, as here.",
        ],
    )],
    grammar=[dict(
        title="Formal requests: θα + imperfect, αν + imperfect",
        en="The politest request is a hypothetical conditional: **θα σας ήμουν ευγνώμων αν + imperfect** (αν μου επιτρέπατε, αν με ενημερώνατε). Also common: **θα σας παρακαλούσα να + subjunctive**, and the cause connective **καθώς** (as, since), which is more formal than επειδή.",
        examples=ex(
            ("Θα σας ήμουν ευγνώμων αν μου στέλνατε το πρόγραμμα.", "I would be grateful if you sent me the programme."),
            ("Θα σας παρακαλούσα να μου απαντήσετε το συντομότερο.", "I would ask you to reply as soon as possible."),
            ("Δεν μπόρεσα να έρθω, καθώς ήμουν άρρωστος.", "I could not come, as I was ill."),
        ),
    )],
    drills=[
        q("Θα σας ήμουν ευγνώμων αν μου ___ να εξεταστώ αργότερα.", ["επιτρέπατε", "επιτρέψετε", "επιτρέπετε"], "επιτρέπατε", "Polite hypothetical: αν + imperfect."),
        q("Ποια φράση δείχνει ότι στέλνετε έγγραφο μαζί με την επιστολή;", ["Επισυνάπτω τη βεβαίωση.", "Σας θυμίζω τη βεβαίωση.", "Σας ζητώ τη βεβαίωση."], "Επισυνάπτω τη βεβαίωση."),
        q("Δεν παρευρέθηκα, ___ ήμουν στο νοσοκομείο.", ["καθώς", "ώστε", "αν και"], "καθώς"),
        q("Ποιο είναι πιο επίσημο κλείσιμο σε αίτηση προς αρχή;", ["Με τιμή,", "Τα λέμε,", "Φιλικά,"], "Με τιμή,"),
    ],
    tasks=[
        dict(id="request-1", level="B2", words=200,
             el="Γράφετε στον διαχειριστή της πολυκατοικίας σας για να του ζητήσετε την άδεια να χρησιμοποιήσετε την ταράτσα για μια γιορτή. Του εξηγείτε τον λόγο και τον διαβεβαιώνετε ότι δεν θα ενοχληθεί κανείς. (200 λέξεις)",
             en="Write to your building manager asking permission to use the roof terrace for a party. Explain why and assure him nobody will be disturbed. (200 words)",
             plan=["Who you are (flat number) and the request with date and hours.", "The reason.", "Three guarantees (music, supervision, cleaning).", "Ask for an answer by a date; thanks."],
             model=P("""
                Κύριε Διαχειριστή,

                Είμαι η ένοικος του διαμερίσματος 4Β και σας γράφω για να σας ζητήσω την άδεια να χρησιμοποιήσω την ταράτσα της πολυκατοικίας το Σάββατο 19 Ιουνίου, από τις οχτώ έως τις δώδεκα το βράδυ.

                Ο λόγος είναι ότι η κόρη μου τελειώνει φέτος το σχολείο και θα ήθελα να οργανώσω μια μικρή γιορτή για τους συμμαθητές της, περίπου είκοσι άτομα. Επειδή το διαμέρισμά μας είναι μικρό, η ταράτσα θα ήταν ιδανική.

                Θέλω να σας διαβεβαιώσω ότι θα τηρηθούν όλοι οι κανόνες της πολυκατοικίας. Η μουσική θα είναι χαμηλή και θα σταματήσει στις δώδεκα ακριβώς, ενώ εγώ και ο σύζυγός μου θα είμαστε παρόντες όλη την ώρα. Την επόμενη μέρα θα φροντίσουμε να καθαριστεί πλήρως ο χώρος. Επιπλέον, σκοπεύω να ενημερώσω προσωπικά τους γείτονες και να ζητήσω την κατανόησή τους.

                Θα σας ήμουν ευγνώμων αν μου απαντούσατε μέχρι το τέλος του μήνα, ώστε να προλάβω να στείλω τις προσκλήσεις.

                Σας ευχαριστώ εκ των προτέρων.

                Με εκτίμηση,
                Α. Νικολάου
             """),
             model_en=P("""
                Dear Building Manager,

                I am the tenant of flat 4B and I am writing to ask your permission to use the building's roof terrace on Saturday 19 June, from eight until midnight.

                The reason is that my daughter finishes school this year and I would like to organise a small party for her classmates, about twenty people. As our flat is small, the roof terrace would be ideal.

                I want to assure you that all the building's rules will be observed. The music will be low and will stop at midnight exactly, and my husband and I will be present the whole time. The next day we will make sure the space is cleaned thoroughly. I also intend to inform the neighbours personally and ask for their understanding.

                I would be grateful if you could reply by the end of the month, so that I have time to send out the invitations.

                Thank you in advance.

                Yours sincerely,
                A. Nikolaou
             """)),
        dict(id="request-2", level="B2", words=200,
             el="Ο προϊστάμενός σας σας έχει ζητήσει να δουλέψετε δύο Σάββατα τον επόμενο μήνα. Γράφετε για να του ζητήσετε να σας εξαιρέσει από το ένα, εξηγώντας τον λόγο και προτείνοντας λύση. (200 λέξεις)",
             en="Your manager has asked you to work two Saturdays next month. Write asking to be excused from one, explaining why and proposing a solution. (200 words)",
             plan=["Acknowledge the request and your willingness.", "The reason, with a date.", "Your proposal (swap with a colleague, extra hours).", "Thanks; availability to discuss."]),
        dict(id="request-3", level="B2", words=200,
             el="Γράφετε στη γραμματεία ενός μουσείου για να οργανώσετε μια επίσκεψη για την τάξη σας των ελληνικών (15 ενήλικες). Ζητάτε πληροφορίες για ξενάγηση, εκπτώσεις και πρόσβαση για έναν συμμαθητή με αναπηρικό αμαξίδιο, και δίνετε τα στοιχεία σας. (200 λέξεις)",
             en="Write to a museum's office to organise a visit for your Greek class (15 adults). Ask about a guided tour, discounts and access for a classmate in a wheelchair, and give your details. (200 words)",
             plan=["Who you are and the group.", "Preferred dates.", "Three questions as polite statements.", "Contact details; thanks."]),
    ],
)

U10 = dict(
    id="application", kind="unit", part="formal", level="B2", el="Αίτηση και συνοδευτική επιστολή", title="Application and cover letter",
    intro=[
        {"p": "Part B can also ask you to give personal information: applying for a job, a scholarship, a volunteer post. This is the cover letter: why you are writing, who you are, what you bring, why this post, availability, and what you attach. Formal Greek here prefers **nouns to verbs**: εκδηλώνω ενδιαφέρον για συμμετοχή rather than θέλω να συμμετάσχω."},
    ],
    structure=[
        ["Προσφώνηση", "Greeting", "Αξιότιμη κυρία + surname, / Αξιότιμοι κύριοι,"],
        ["Αφορμή και θέση", "Occasion and post", "Με αφορμή την αγγελία σας…, θα ήθελα να εκδηλώσω το ενδιαφέρον μου για τη θέση…"],
        ["Ποιος είστε", "Who you are", "Ονομάζομαι…, είμαι… ετών, κατάγομαι από…, ζω…, εργάζομαι ως…"],
        ["Τι προσφέρετε", "What you bring", "Experience, studies, languages, linked to the post: Πιστεύω ότι η εμπειρία αυτή…"],
        ["Διαθεσιμότητα", "Availability", "Είμαι διαθέσιμη…"],
        ["Συνημμένα και κλείσιμο", "Attachments and close", "Επισυνάπτω το βιογραφικό μου σημείωμα και παραμένω στη διάθεσή σας για συνέντευξη."],
    ],
    phrases=[
        dict(el="Η αίτηση", en="Applying", items=ph(
            ("Με αφορμή την αγγελία σας στο…", "With reference to your advertisement in…", "Ε"),
            ("Θα ήθελα να εκδηλώσω το ενδιαφέρον μου για τη θέση…", "I would like to express my interest in the post of…", "Ε"),
            ("Σας γράφω για να υποβάλω αίτηση για…", "I am writing to apply for…", "Ε"),
        )),
        dict(el="Προσόντα", en="Qualifications", items=ph(
            ("Είμαι κάτοχος πτυχίου…", "I hold a degree in…", "Ε"),
            ("Διαθέτω τριετή εμπειρία στο/στη…", "I have three years' experience in…", "Ε"),
            ("Μιλώ άπταιστα αγγλικά και γαλλικά.", "I speak fluent English and French."),
            ("Θεωρώ ότι πληρώ τις προϋποθέσεις της θέσης.", "I believe I meet the requirements of the post.", "Ε"),
            ("σε συνδυασμό με…", "combined with…"),
        )),
        dict(el="Κλείσιμο", en="Closing", items=ph(
            ("Επισυνάπτω το βιογραφικό μου σημείωμα.", "I attach my CV.", "Ε"),
            ("Παραμένω στη διάθεσή σας για μια συνέντευξη.", "I remain at your disposal for an interview.", "Ε"),
            ("όποτε σας εξυπηρετεί", "whenever suits you"),
        )),
    ],
    models=[dict(
        el="Εθελόντρια σε φεστιβάλ", en="Volunteering at a festival", level="B2",
        task_el="Ένα φεστιβάλ κινηματογράφου ζητά εθελοντές για την υποδοχή των ξένων επισκεπτών. Γράφετε στην υπεύθυνη εθελοντών για να δηλώσετε ενδιαφέρον, δίνοντας πληροφορίες για τον εαυτό σας. (200 λέξεις)",
        task_en="A film festival is looking for volunteers to welcome foreign guests. Write to the volunteer coordinator to express interest, giving information about yourself. (200 words)",
        text=P("""
            Αξιότιμη κυρία Σταθοπούλου,

            Με αφορμή την ανακοίνωσή σας στην ιστοσελίδα του Φεστιβάλ Κινηματογράφου, θα ήθελα να εκδηλώσω το ενδιαφέρον μου να συμμετάσχω ως εθελόντρια στη φετινή διοργάνωση.

            Ονομάζομαι Λάουρα Μπιάνκι, είμαι 26 ετών και κατάγομαι από τη Γένοβα της Ιταλίας. Ζω στη Θεσσαλονίκη τα τελευταία δύο χρόνια, όπου εργάζομαι ως μεταφράστρια. Εκτός από ιταλικά, μιλώ άπταιστα αγγλικά και γαλλικά, ενώ τα ελληνικά μου βρίσκονται σε επίπεδο Β2.

            Ο κινηματογράφος υπήρξε ανέκαθεν το μεγαλύτερό μου πάθος. Κατά τη διάρκεια των σπουδών μου εργάστηκα εθελοντικά σε δύο φεστιβάλ στην Ιταλία, όπου υποδεχόμουν τους καλεσμένους και βοηθούσα στην οργάνωση των προβολών. Πιστεύω ότι η εμπειρία αυτή, σε συνδυασμό με τις γλώσσες που γνωρίζω, θα μου επέτρεπε να φανώ ιδιαίτερα χρήσιμη στην εξυπηρέτηση των ξένων επισκεπτών.

            Είμαι διαθέσιμη καθ' όλη τη διάρκεια του φεστιβάλ, ακόμη και τα βράδια και τα Σαββατοκύριακα.

            Επισυνάπτω το βιογραφικό μου σημείωμα και παραμένω στη διάθεσή σας για μια συνέντευξη, όποτε σας εξυπηρετεί.

            Με εκτίμηση,
            Λάουρα Μπιάνκι
        """),
        text_en=P("""
            Dear Ms Stathopoulou,

            With reference to your announcement on the Film Festival website, I would like to express my interest in taking part as a volunteer in this year's festival.

            My name is Laura Bianchi, I am 26 years old and I come from Genoa, Italy. I have lived in Thessaloniki for the past two years, where I work as a translator. As well as Italian, I speak fluent English and French, and my Greek is at B2 level.

            Cinema has always been my greatest passion. During my studies I volunteered at two festivals in Italy, where I welcomed guests and helped organise screenings. I believe that this experience, combined with the languages I know, would allow me to be particularly useful in looking after foreign visitors.

            I am available throughout the festival, including evenings and weekends.

            I attach my CV and remain at your disposal for an interview, whenever suits you.

            Yours sincerely,
            Laura Bianchi
        """),
        notes=[
            "**Every paragraph answers a question the reader has**: why are you writing, who are you, what can you do for us, when, what next.",
            "**Formal touches**: 26 ετών (not χρονών), υπήρξε ανέκαθεν, καθ' όλη τη διάρκεια, θα μου επέτρεπε να φανώ χρήσιμη.",
            "**Experience is linked to the post** (υποδεχόμουν τους καλεσμένους → εξυπηρέτηση των ξένων επισκεπτών): don't just list, connect.",
        ],
    )],
    grammar=[dict(
        title="Nominal style: verbs become nouns",
        en="Formal Greek turns verbs into nouns and links them with genitives. It sounds heavier in English but is exactly what the examiner expects in Part B: **οργανώνω → η οργάνωση, συμμετέχω → η συμμετοχή, εξυπηρετώ → η εξυπηρέτηση, αξιολογώ → η αξιολόγηση**.",
        examples=ex(
            ("Θέλω να συμμετέχω. → Εκδηλώνω ενδιαφέρον για συμμετοχή.", "I want to take part. → I express interest in participation."),
            ("Βοηθούσα να οργανωθούν οι προβολές. → Βοηθούσα στην οργάνωση των προβολών.", "I helped organise the screenings."),
            ("Εξυπηρετούσα τους επισκέπτες. → Ήμουν υπεύθυνη για την εξυπηρέτηση των επισκεπτών.", "I looked after the visitors."),
        ),
    )],
    drills=[
        q("Πώς λέτε την ηλικία σας σε επίσημη αίτηση;", ["Είμαι 26 ετών.", "Είμαι 26 χρονών.", "Έχω 26 χρόνια."], "Είμαι 26 ετών."),
        q("Το ουσιαστικό του «συμμετέχω» είναι:", ["η συμμετοχή", "η συμμετοχία", "το συμμετέχειν"], "η συμμετοχή"),
        q("Ποια φράση ανοίγει μια συνοδευτική επιστολή;", ["Με αφορμή την αγγελία σας…", "Γεια σας, θέλω τη δουλειά.", "Σου γράφω για τη θέση."], "Με αφορμή την αγγελία σας…"),
        q("Μιλώ ___ τρεις γλώσσες.", ["άπταιστα", "άπταιστες", "απταίστως"], "άπταιστα"),
    ],
    tasks=[
        dict(id="application-1", level="B2", words=200,
             el="Ένα ίδρυμα προσφέρει υποτροφίες για ένα θερινό πρόγραμμα ελληνικής γλώσσας στην Ελλάδα. Γράφετε για να υποβάλετε αίτηση, εξηγώντας ποιος είστε, γιατί μαθαίνετε ελληνικά και γιατί χρειάζεστε την υποτροφία. (200 λέξεις)",
             en="A foundation offers scholarships for a summer Greek course in Greece. Apply, explaining who you are, why you learn Greek and why you need the scholarship. (200 words)",
             plan=["Purpose: applying for the scholarship.", "Who you are and your Greek so far.", "Why Greek, linked to a concrete goal.", "Why the scholarship; attachments."],
             model=P("""
                Αξιότιμοι κύριοι,

                Σας γράφω για να υποβάλω αίτηση για μία από τις υποτροφίες που προσφέρει το Ίδρυμά σας για το θερινό πρόγραμμα ελληνικής γλώσσας και πολιτισμού.

                Ονομάζομαι Γιόνας Μπεργκ, είμαι 31 ετών και ζω στη Στοκχόλμη, όπου εργάζομαι ως αρχιτέκτονας. Μαθαίνω ελληνικά εδώ και τρία χρόνια, αρχικά σε ένα τμήμα του πανεπιστημίου και στη συνέχεια μόνος μου. Τον περασμένο Μάιο πέτυχα στις εξετάσεις πιστοποίησης του επιπέδου Β1.

                Το ενδιαφέρον μου για την Ελλάδα ξεκίνησε από την αρχιτεκτονική. Έχοντας επισκεφθεί πολλές φορές τις Κυκλάδες, θέλω να μελετήσω την παραδοσιακή τους αρχιτεκτονική, και για τον σκοπό αυτό χρειάζομαι πρόσβαση στην ελληνική βιβλιογραφία. Ένα εντατικό πρόγραμμα στην Ελλάδα θα με βοηθούσε να βελτιώσω κυρίως τον γραπτό λόγο, που είναι το πιο αδύναμο σημείο μου.

                Δυστυχώς, χωρίς την οικονομική σας υποστήριξη δεν θα μπορούσα να καλύψω τα δίδακτρα και τα έξοδα διαμονής.

                Επισυνάπτω το βιογραφικό μου σημείωμα, το πιστοποιητικό ελληνομάθειας και μια συστατική επιστολή της καθηγήτριάς μου. Παραμένω στη διάθεσή σας για κάθε επιπλέον πληροφορία.

                Με εκτίμηση,
                Γιόνας Μπεργκ
             """),
             model_en=P("""
                Dear Sirs,

                I am writing to apply for one of the scholarships your Foundation offers for the summer programme in Greek language and culture.

                My name is Jonas Berg, I am 31 years old and I live in Stockholm, where I work as an architect. I have been learning Greek for three years, first in a university class and then on my own. Last May I passed the certificate exam at B1 level.

                My interest in Greece began with architecture. Having visited the Cyclades many times, I want to study their traditional architecture, and for that I need access to the Greek literature on the subject. An intensive course in Greece would help me improve above all my writing, which is my weakest point.

                Unfortunately, without your financial support I would not be able to cover the tuition fees and living costs.

                I attach my CV, my Greek language certificate and a letter of recommendation from my teacher. I remain at your disposal for any further information.

                Yours sincerely,
                Jonas Berg
             """)),
        dict(id="application-2", level="B2", words=200,
             el="Ένα ταξιδιωτικό γραφείο ζητά βοηθό ξεναγού για το καλοκαίρι. Γράψτε τη συνοδευτική επιστολή της αίτησής σας. (200 λέξεις)",
             en="A travel agency is looking for an assistant tour guide for the summer. Write your cover letter. (200 words)",
             plan=["The advertisement and the post.", "Who you are; languages.", "Two experiences linked to guiding.", "Availability, attachments, interview."]),
        dict(id="application-3", level="B2", words=200,
             el="Ψάχνετε διαμέρισμα και γράφετε σε ένα μεσιτικό γραφείο. Συστήνεστε ως ενοικιαστής (δουλειά, οικογένεια, κατοικίδια), λέτε τι ψάχνετε και ζητάτε ραντεβού. (200 λέξεις)",
             en="You're looking for a flat and write to an estate agency. Introduce yourself as a tenant (job, family, pets), say what you're looking for and ask for an appointment. (200 words)",
             plan=["Purpose.", "Personal information that reassures a landlord.", "Your requirements (area, size, budget).", "Request for viewings; contact details."]),
    ],
)

U11 = dict(
    id="newspaper-letter", kind="unit", part="formal", level="B2+", el="Επιστολή σε εφημερίδα", title="Letter to a newspaper",
    intro=[
        {"p": "The letter to the editor sits between Part A (it can be the newspaper in «σε εφημερίδα») and the opinion article. Refer precisely to the article or event, state your position early, argue in two or three paragraphs, **acknowledge the other side before rejecting it**, and end with a proposal or a call."},
    ],
    structure=[
        ["Προσφώνηση", "Greeting", "Κύριε Διευθυντά, (the traditional address to the editor)"],
        ["Αφορμή και θέση", "Occasion and position", "Με αφορμή το άρθρο του/της…, που δημοσιεύθηκε στις…, θα ήθελα να…"],
        ["Επιχειρήματα", "Arguments", "One per paragraph, with a reason or example."],
        ["Αντίλογος", "Counterargument", "Οι υποστηρικτές… ισχυρίζονται ότι… Δεν αμφισβητώ ότι… όμως…"],
        ["Πρόταση και κλείσιμο", "Proposal and close", "Πιστεύω ότι υπάρχουν άλλοι δρόμοι: … Καλώ τις αρμόδιες αρχές να… / Με εκτίμηση, + name, town"],
    ],
    phrases=[
        dict(el="Αφορμή", en="Referring", items=ph(
            ("Με αφορμή το άρθρο σας της 12ης Μαρτίου με τίτλο «…»", "With reference to your article of 12 March entitled “…”", "Ε"),
            ("Με μεγάλο ενδιαφέρον διάβασα…", "I read with great interest…", "Ε"),
            ("Θα ήθελα να καταθέσω κι εγώ την άποψή μου.", "I would like to give my own view.", "Ε"),
        )),
        dict(el="Θέση και αντίλογος", en="Position and counterargument", items=ph(
            ("Συμφωνώ απόλυτα με τον αρθρογράφο ότι…", "I fully agree with the writer that…"),
            ("Θα ήθελα να εκφράσω την έντονη αντίθεσή μου σε…", "I wish to express my strong opposition to…", "Ε"),
            ("Οι υποστηρικτές του σχεδίου ισχυρίζονται ότι…", "Supporters of the plan claim that…", "Ε"),
            ("Δεν αμφισβητώ ότι…· πρόκειται, όμως, για…", "I do not dispute that…; it is, however, a matter of…", "Ε"),
            ("Με άλλα λόγια, το ζητούμενο δεν είναι…, αλλά…", "In other words, the point is not…, but…"),
        )),
        dict(el="Πρόταση", en="Proposing", items=ph(
            ("Πιστεύω ότι υπάρχουν άλλοι δρόμοι: …", "I believe there are other ways: …"),
            ("Καλώ, λοιπόν, τις αρμόδιες αρχές να…", "I therefore call on the authorities to…", "Ε"),
            ("Μόνο έτσι…", "Only in this way…"),
        )),
    ],
    models=[dict(
        el="Ένα κέντρο χωρίς αυτοκίνητα;", en="A city centre without cars?", level="B2+",
        task_el="Μια εφημερίδα δημοσίευσε άρθρο που προτείνει να απαγορευτούν τα αυτοκίνητα στο κέντρο της πόλης σας. Γράφετε μια επιστολή στην εφημερίδα με την άποψή σας. (250 λέξεις)",
        task_en="A newspaper published an article proposing to ban cars from your city centre. Write a letter to the paper with your view. (250 words)",
        text=P("""
            Κύριε Διευθυντά,

            Με μεγάλο ενδιαφέρον διάβασα το άρθρο του κ. Ν. Καλογήρου, που δημοσιεύθηκε στην εφημερίδα σας στις 12 Μαρτίου με τίτλο «Ένα κέντρο χωρίς αυτοκίνητα». Θα ήθελα να καταθέσω κι εγώ την άποψή μου, ως κάτοικος του κέντρου εδώ και είκοσι χρόνια.

            Συμφωνώ απόλυτα με τον αρθρογράφο ότι η κυκλοφοριακή συμφόρηση έχει κάνει την καθημερινότητά μας ανυπόφορη. Ο θόρυβος, η ατμοσφαιρική ρύπανση και τα αυτοκίνητα που είναι παρκαρισμένα πάνω στα πεζοδρόμια κάνουν τη βόλτα πραγματική περιπέτεια, ιδίως για τους ηλικιωμένους και τις μητέρες με καρότσια. Όπου τα αυτοκίνητα περιορίστηκαν, οι πεζόδρομοι ζωντάνεψαν τις γειτονιές.

            Ωστόσο, πιστεύω ότι μια απότομη απαγόρευση θα ήταν λάθος. Αν δεν βελτιωθούν πρώτα τα μέσα μαζικής μεταφοράς, οι κάτοικοι των προαστίων θα τιμωρηθούν άδικα, αφού για πολλούς από αυτούς το αυτοκίνητο είναι η μόνη επιλογή. Χρειάζονται, επομένως, συχνότερα δρομολόγια, χώροι στάθμευσης στις άκρες της πόλης και ασφαλείς ποδηλατόδρομοι.

            Με άλλα λόγια, το ζητούμενο δεν είναι να κηρύξουμε πόλεμο στο αυτοκίνητο, αλλά να δώσουμε στους πολίτες πραγματικές εναλλακτικές λύσεις. Μόνο έτσι η αλλαγή θα γίνει αποδεκτή από όλους.

            Με εκτίμηση,
            Δ. Ραφαηλίδης, Αθήνα
        """),
        text_en=P("""
            Dear Editor,

            I read with great interest the article by Mr N. Kalogirou, published in your newspaper on 12 March under the title “A centre without cars”. I would like to give my own view, as someone who has lived in the centre for twenty years.

            I fully agree with the writer that traffic congestion has made our daily lives unbearable. The noise, the air pollution and the cars parked on the pavements turn a walk into a real adventure, especially for elderly people and mothers with prams. Wherever cars have been restricted, pedestrian streets have brought neighbourhoods back to life.

            However, I believe a sudden ban would be a mistake. Unless public transport is improved first, people in the suburbs will be unfairly punished, since for many of them the car is the only option. What is needed, therefore, is more frequent services, car parks on the edges of the city and safe cycle lanes.

            In other words, the point is not to declare war on the car, but to give citizens real alternatives. Only then will the change be accepted by everyone.

            Yours faithfully,
            D. Rafailidis, Athens
        """),
        notes=[
            "**A precise reference** (author, date, title) and **the writer's credentials** (twenty years in the centre) in the first paragraph.",
            "**Agree, then qualify**: Συμφωνώ απόλυτα… Ωστόσο… The nuanced position reads as more mature than simple yes or no.",
            "**Με άλλα λόγια** reformulates the thesis in one memorable sentence before the close.",
            "**κ.** is the abbreviation of κύριος (Mr), **κ.κ.** of κύριοι.",
        ],
    )],
    grammar=[dict(
        title="Concession: ωστόσο, αν και, μολονότι, έστω κι αν",
        en="**Ωστόσο / όμως / εντούτοις** start a contrasting sentence. **Αν και / παρόλο που / μολονότι** (formal) introduce a concessive clause with the indicative. **Έστω κι αν / ακόμα κι αν** (even if) look at a possibility and take the subjunctive or indicative.",
        examples=ex(
            ("Συμφωνώ με την πρόταση. Ωστόσο, φοβάμαι ότι είναι πρόωρη.", "I agree with the proposal. However, I fear it is premature."),
            ("Μολονότι το σχέδιο έχει πλεονεκτήματα, δεν μπορώ να το στηρίξω.", "Although the plan has advantages, I cannot support it."),
            ("Θα αντιδράσουμε, έστω κι αν μείνουμε μόνοι.", "We will object, even if we are left on our own."),
        ),
    )],
    drills=[
        q("Πώς προσφωνείτε τον διευθυντή μιας εφημερίδας;", ["Κύριε Διευθυντά,", "Γεια σας κύριε,", "Αγαπητέ μου Διευθυντή,"], "Κύριε Διευθυντά,"),
        q("___ το σχέδιο έχει πλεονεκτήματα, δεν μπορώ να το στηρίξω.", ["Μολονότι", "Επομένως", "Επειδή"], "Μολονότι"),
        q("Η σύντμηση «κ.» σημαίνει:", ["κύριος", "κάτοικος", "και"], "κύριος"),
        q("Ποια φράση αναγνωρίζει την άλλη άποψη;", ["Δεν αμφισβητώ ότι το νησί χρειάζεται ανάπτυξη.", "Είναι προφανές ότι έχω δίκιο.", "Κανείς δεν μπορεί να διαφωνήσει."], "Δεν αμφισβητώ ότι το νησί χρειάζεται ανάπτυξη."),
    ],
    tasks=[
        dict(id="newspaper-letter-1", level="B2+", words=250,
             el="Η τοπική εφημερίδα έγραψε ότι πρόκειται να χτιστεί ένα μεγάλο ξενοδοχείο σε μια προστατευόμενη παραλία του νησιού σας. Γράφετε στην εφημερίδα για να εκφράσετε την αντίθεσή σας και να προτείνετε εναλλακτικές λύσεις. (250 λέξεις)",
             en="The local paper reported that a large hotel is to be built on a protected beach on your island. Write to the paper to express your opposition and propose alternatives. (250 words)",
             plan=["Reference to the report; your position.", "Why the beach matters (nature, character).", "The jobs argument: acknowledge, then rebut.", "Alternatives and a call to the authorities."],
             model=P("""
                Κύριε Διευθυντά,

                Με αφορμή το ρεπορτάζ που φιλοξενήθηκε στη χθεσινή έκδοση της εφημερίδας σας σχετικά με την κατασκευή ξενοδοχειακής μονάδας στην παραλία του Αγίου Στεφάνου, θα ήθελα να εκφράσω την έντονη αντίθεσή μου στο σχέδιο αυτό.

                Η παραλία είναι μία από τις τελευταίες ανέγγιχτες ακτές του νησιού μας. Εκεί γεννούν κάθε καλοκαίρι τα αυγά τους οι θαλάσσιες χελώνες καρέτα καρέτα, ενώ οι αμμοθίνες της φιλοξενούν σπάνια φυτά. Ένα συγκρότημα διακοσίων δωματίων, με πισίνες, φώτα και μουσική, θα κατέστρεφε σε λίγα χρόνια ένα οικοσύστημα που χρειάστηκε αιώνες για να δημιουργηθεί.

                Οι υποστηρικτές του έργου ισχυρίζονται ότι θα δημιουργηθούν νέες θέσεις εργασίας. Δεν αμφισβητώ ότι το νησί χρειάζεται ανάπτυξη. Πρόκειται, όμως, για εποχικές θέσεις, ενώ η ζημιά στο περιβάλλον θα είναι μόνιμη. Επιπλέον, οι επισκέπτες έρχονται στο νησί μας ακριβώς επειδή είναι ακόμα αυθεντικό. Αν το μετατρέψουμε σε αντίγραφο άλλων τουριστικών προορισμών, μακροπρόθεσμα θα χάσουμε περισσότερα από όσα θα κερδίσουμε.

                Πιστεύω ότι υπάρχουν άλλοι δρόμοι: η ανακαίνιση παλιών κτιρίων στα χωριά, ο οικοτουρισμός και η στήριξη των τοπικών προϊόντων. Καλώ, λοιπόν, τις αρμόδιες αρχές να μην εγκρίνουν το έργο και να ανοίξουν έναν πραγματικό διάλογο με τους κατοίκους.

                Με εκτίμηση,
                Μ. Βασιλείου
             """),
             model_en=P("""
                Dear Editor,

                With reference to the report in yesterday's edition of your newspaper on the construction of a hotel complex on the beach of Agios Stefanos, I wish to express my strong opposition to this plan.

                The beach is one of the last untouched stretches of coast on our island. Every summer loggerhead sea turtles lay their eggs there, and its sand dunes are home to rare plants. A complex of two hundred rooms, with swimming pools, lights and music, would destroy within a few years an ecosystem that took centuries to form.

                The project's supporters claim that new jobs will be created. I do not dispute that the island needs development. These are, however, seasonal jobs, while the damage to the environment will be permanent. Moreover, visitors come to our island precisely because it is still authentic. If we turn it into a copy of other tourist destinations, in the long run we will lose more than we gain.

                I believe there are other ways: restoring old buildings in the villages, ecotourism and support for local products. I therefore call on the competent authorities not to approve the project and to open a real dialogue with the residents.

                Yours faithfully,
                M. Vasileiou
             """)),
        dict(id="newspaper-letter-2", level="B2+", words=250,
             el="Μια εφημερίδα δημοσίευσε άρθρο με τίτλο «Οι νέοι δεν διαβάζουν πια». Γράφετε μια επιστολή στην εφημερίδα για να διαφωνήσετε. (250 λέξεις)",
             en="A newspaper published an article entitled “Young people don't read any more”. Write a letter to disagree. (250 words)",
             plan=["Reference and position.", "Two counterarguments with examples (what and how young people read now).", "Concede one point.", "Proposal: what schools and libraries could do."]),
        dict(id="newspaper-letter-3", level="C1", words=300,
             el="Στη γειτονιά σας τα ενοίκια έχουν ανέβει πολύ, επειδή όλο και περισσότερα διαμερίσματα νοικιάζονται σε τουρίστες. Γράφετε στην εφημερίδα της πόλης σας. (300 λέξεις)",
             en="Rents in your neighbourhood have soared because more and more flats are let to tourists. Write to your city's newspaper. (300 words)",
             plan=["Occasion: a recent article or your own experience.", "Consequences for residents, with examples.", "Acknowledge the owners' side.", "Concrete proposals; a call to the municipality."]),
    ],
)

ITEMS = [U08, U09, U10, U11]
