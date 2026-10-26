from common import P, ph, q, ex

GUIDE = dict(
    id="exam", kind="guide", part="exam", level="B2", el="Η εξέταση γραπτού λόγου", title="The B2 writing paper and how to use this workbook",
    intro=[
        {"p": "The writing paper of the Certificate of Attainment in Greek (Πιστοποίηση Ελληνομάθειας, Κέντρο Ελληνικής Γλώσσας) at B2 asks for **two texts of about 200 words each in 85 minutes**. Each is worth 10 points, and writing is 20% of the whole exam. You must reach **60% in every skill** to pass, so a weak writing paper sinks a strong reading score."},
        {"tip": "Everything here is built for production: read a model, borrow its skeleton and phrases, write your own text in the box under each task (it is saved on this device), then go through the correction checklist before you open the model answer."},
    ],
    sections=[
        dict(el="Η μορφή της εξέτασης", en="Format", body=[
            {"table": {"head": ["Μέρος", "Τι γράφετε", "Λέξεις", "Μονάδες"], "rows": [
                ["Α΄ μέρος", "Φιλικό γράμμα ή email σε φίλο, συγγενή, κάποιον λιγότερο γνωστό, σε εφημερίδα ή σε φόρουμ: συμβουλές, πληροφορίες, επιχειρήματα", "200", "10"],
                ["Β΄ μέρος", "Τυπικό κείμενο: δίνει προσωπικές ή άλλες πληροφορίες, ζητά αιτιολογημένη άδεια, εκφράζει αιτιολογημένα παράπονα", "200", "10"],
            ]}},
            {"p": "Part A is personal in tone (εσύ, warm openings, everyday vocabulary); Part B is formal (εσείς, fixed formulas, more nouns and passives). Units 4–7 train Part A, units 8–11 train Part B. Units 12–16 take you past the exam into the opinion pieces, essays, reports and speeches of the Γ1 (C1) paper, where texts grow to 250–300 words."},
        ]),
        dict(el="Οι κανόνες της αίθουσας", en="Rules on the day", body=[
            {"list": [
                "**Never sign with your real name.** The paper says so explicitly: «στο τέλος μην υπογράψετε με το όνομά σας». Use an invented name or initials.",
                "**Write in lower-case letters** (πεζά). The exam guide requires it for the writing paper, because capitals hide accents and spelling.",
                "Answer **every point** in the prompt. The task usually lists two or three things to do (explain, propose, ask); each one missing costs content marks.",
                "Stay close to **200 words**. Much shorter leaves points undeveloped; much longer only adds room for mistakes.",
            ]},
        ]),
        dict(el="Πώς βαθμολογείται", en="How the texts are marked", body=[
            {"p": "The Centre for the Greek Language publishes a detailed marking grid for Γ1; its dimensions are the right target at B2 too, at a lower standard:"},
            {"table": {"head": ["Κριτήριο", "What the examiner looks for"], "rows": [
                ["Εκπλήρωση του στόχου", "Every point of the prompt covered; the purpose clear from the first lines"],
                ["Είδος κειμένου και ύφος", "The right genre (letter, email, article) and a register kept consistently (εσύ or εσείς)"],
                ["Οργάνωση και συνοχή", "Paragraphs with one idea each, linked by varied connectives"],
                ["Λεξιλόγιο", "Range and precision, no repetition, no anglicisms"],
                ["Σύνταξη", "Complex sentences: relative, causal, concessive and conditional clauses"],
                ["Μορφολογία", "Case endings, agreement, verb forms and aspect"],
                ["Ορθογραφία, τονισμός, στίξη", "Spelling, accents and punctuation; the Γ1 top band asks for flawless accents"],
            ]}},
        ]),
        dict(el="Το πλάνο των 85 λεπτών", en="Timing plan for 85 minutes", body=[
            {"table": {"head": ["Λεπτά", "Τι κάνετε"], "rows": [
                ["0–5", "Read both prompts. Underline every task point and the recipient. Decide εσύ or εσείς for each."],
                ["5–10", "Plan text 1: four or five paragraph headings and the connectives you will use."],
                ["10–40", "Write text 1."],
                ["40–45", "Plan text 2."],
                ["45–75", "Write text 2."],
                ["75–85", "Correction checklist on both: endings, accents, punctuation, the fake name."],
            ]}},
        ]),
        dict(el="Πώς να χρησιμοποιήσετε το τετράδιο", en="How to use this workbook", body=[
            {"list": [
                "**Weeks 1–4: units 1–3.** Paragraphs, linking and register. Short, but they decide your organisation and style marks.",
                "**Then one unit a week**, in order, on your Wednesday writing slot from the study plan. Each unit: read the model with connectives highlighted, learn eight to ten phrases, do the quick drills, write the first task, check it with the checklist, then compare with the model answer.",
                "**Paste your draft to Claude** for correction (the Copy button under each task), and log every case or agreement error in the Mistakes notebook.",
                "**From March 2027**, write both exam tasks in one 85-minute sitting every week, timed.",
            ]},
            {"tip": "The Writing coach shelf has the official B2 and Γ1 sample prompts with structural checks. This workbook teaches the genres; the coach is where you rehearse the real prompts."},
        ]),
    ],
    drills=[
        q("Πόσες λέξεις γράφετε σε κάθε μέρος της εξέτασης Β2;", ["περίπου 200", "περίπου 100", "περίπου 400"], "περίπου 200"),
        q("Πώς υπογράφετε το γράμμα σας στην εξέταση;", ["με ένα επινοημένο όνομα", "με το πραγματικό σας όνομα", "δεν υπογράφετε ποτέ"], "με ένα επινοημένο όνομα", "The paper tells you not to sign with your own name; an invented name or initials is the norm."),
        q("Τι είδους κείμενο είναι συνήθως το Β΄ μέρος;", ["τυπικό, π.χ. επιστολή παραπόνων", "φιλικό email", "διήγημα"], "τυπικό, π.χ. επιστολή παραπόνων"),
        q("Πόσο τοις εκατό πρέπει να πάρετε σε κάθε δεξιότητα για να περάσετε;", ["60%", "50%", "75%"], "60%"),
    ],
)

U01 = dict(
    id="paragraph", kind="unit", part="found", level="B1", el="Η παράγραφος", title="The paragraph: one idea, announced, supported, closed",
    intro=[
        {"p": "Greek school writing teaches the paragraph as three named parts, and examiners read with that template in mind: a **θεματική περίοδος** (topic sentence) that states one idea, **λεπτομέρειες** or **σχόλια** (supporting details: reasons, examples, facts) and an optional **κατακλείδα** (closing sentence) that sums up or leads on."},
    ],
    structure=[
        ["Θεματική περίοδος", "Topic sentence", "One sentence that tells the reader what the paragraph is about and what you think of it."],
        ["Λεπτομέρειες / σχόλια", "Support", "Two or three reasons, examples or facts, each introduced by a connective."],
        ["Κατακλείδα", "Closing sentence", "Sums up (Γι' αυτό…, Έτσι…) or points to the next paragraph. Optional in short texts."],
    ],
    phrases=[
        dict(el="Για να ανοίξετε", en="Opening the paragraph", items=ph(
            ("Κατά τη γνώμη μου, …", "In my opinion, …"),
            ("Είναι γεγονός ότι …", "It is a fact that …"),
            ("Πολλοί πιστεύουν ότι …", "Many people believe that …"),
            ("Ένα από τα μεγαλύτερα προβλήματα της εποχής μας είναι …", "One of the biggest problems of our time is …"),
        )),
        dict(el="Για να αναπτύξετε", en="Developing", items=ph(
            ("Πρώτα απ' όλα, …", "First of all, …"),
            ("Επιπλέον, …", "Moreover, …"),
            ("Για παράδειγμα, …", "For example, …"),
            ("Τέλος, …", "Finally, …"),
        )),
        dict(el="Για να κλείσετε", en="Closing", items=ph(
            ("Γι' αυτό …", "That is why …"),
            ("Έτσι, …", "So, / In this way, …"),
            ("Με λίγα λόγια, …", "In short, …"),
        )),
    ],
    models=[dict(
        el="Τα πλεονεκτήματα της πόλης", en="The advantages of the city", level="B1",
        task_el="Γράψτε μια παράγραφο για τα πλεονεκτήματα της ζωής σε μια μεγάλη πόλη. (100–120 λέξεις)",
        task_en="Write a paragraph on the advantages of living in a big city. (100–120 words)",
        text=P("""
            Η ζωή σε μια μεγάλη πόλη έχει, κατά τη γνώμη μου, περισσότερα πλεονεκτήματα από όσα νομίζουμε. Πρώτα απ' όλα, όλα είναι κοντά: η δουλειά, τα καταστήματα, τα νοσοκομεία και τα σχολεία βρίσκονται σε απόσταση λίγων λεπτών. Επιπλέον, η πόλη προσφέρει πολλές ευκαιρίες για ψυχαγωγία, αφού υπάρχουν θέατρα, κινηματογράφοι, μουσεία και συναυλίες σχεδόν κάθε βράδυ. Τέλος, στην πόλη βρίσκει κανείς πιο εύκολα δουλειά, γιατί εκεί έχουν την έδρα τους οι περισσότερες επιχειρήσεις. Γι' αυτό, παρά τον θόρυβο και την κίνηση, πολλοί άνθρωποι προτιμούν να μένουν στο κέντρο.
        """),
        text_en=P("""
            Life in a big city has, in my opinion, more advantages than we think. First of all, everything is close: work, shops, hospitals and schools are a few minutes away. Moreover, the city offers many opportunities for entertainment, since there are theatres, cinemas, museums and concerts almost every evening. Finally, in the city one finds work more easily, because most businesses have their headquarters there. That is why, despite the noise and the traffic, many people prefer to live in the centre.
        """),
        notes=[
            "**Topic sentence:** the first sentence gives the topic (life in a big city) and the writer's view (more advantages than we think).",
            "**Three supports**, each with its own connective: Πρώτα απ' όλα, Επιπλέον, Τέλος. Each support carries a reason clause (αφού, γιατί), which lifts the syntax mark.",
            "**Closing sentence** with Γι' αυτό, and a concession (παρά τον θόρυβο) that shows you have thought about the other side.",
            "**βρίσκει κανείς** = one finds: the generic κανείς with a third-person verb, a neat way to avoid «εμείς» everywhere.",
        ],
    )],
    grammar=[dict(
        title="Reason clauses: γιατί, επειδή, αφού",
        en="All three take the indicative. **Επειδή** can open the sentence; **γιατί** normally follows the main clause; **αφού** gives a reason the reader already accepts (since). After a preposition, use a noun instead: **λόγω** + genitive, **παρά** + accusative (despite).",
        examples=ex(
            ("Επειδή βρέχει, θα μείνουμε σπίτι.", "Because it is raining, we will stay home."),
            ("Θα μείνουμε σπίτι, γιατί βρέχει.", "We will stay home, because it is raining."),
            ("Αφού δεν σου αρέσει, μην το τρως.", "Since you don't like it, don't eat it."),
            ("Η πτήση ακυρώθηκε λόγω της απεργίας.", "The flight was cancelled because of the strike."),
        ),
    )],
    drills=[
        q("Ποια πρόταση είναι η καλύτερη θεματική περίοδος για μια παράγραφο για το περπάτημα;",
          ["Το περπάτημα είναι ο πιο απλός τρόπος να μείνουμε υγιείς.", "Χθες περπάτησα δύο ώρες στο πάρκο.", "Ο φίλος μου έχει καινούργιο ποδήλατο."],
          "Το περπάτημα είναι ο πιο απλός τρόπος να μείνουμε υγιείς.", "A topic sentence states the idea and a view of it; the others are details or off topic."),
        q("Το λεωφορείο είναι φθηνό. ___, είναι συχνά γεμάτο.", ["Ωστόσο", "Επιπλέον", "Γι' αυτό"], "Ωστόσο", "The second sentence goes against the first, so you need contrast."),
        q("Ποια φράση ταιριάζει ως κατακλείδα;", ["Γι' αυτό, αξίζει να δοκιμάσει κανείς τη ζωή στο χωριό.", "Πρώτα απ' όλα, το χωριό είναι ήσυχο.", "Για παράδειγμα, έχει καθαρό αέρα."],
          "Γι' αυτό, αξίζει να δοκιμάσει κανείς τη ζωή στο χωριό."),
        q("Έμεινε στο σπίτι ___ της ασθένειάς του.", ["λόγω", "επειδή", "γιατί"], "λόγω", "Before a noun in the genitive you need λόγω; επειδή and γιατί introduce a clause with a verb."),
    ],
    tasks=[
        dict(id="paragraph-1", level="B1", words=120,
             el="Γράψτε μια παράγραφο με θέμα: «Γιατί αξίζει να μάθει κανείς μια ξένη γλώσσα;» (100–120 λέξεις)",
             en="Write a paragraph: “Why is it worth learning a foreign language?” (100–120 words)",
             plan=["Topic sentence with your view.", "Three reasons: Πρώτα απ' όλα, Επιπλέον, Τέλος, each with a γιατί or αφού clause.", "Closing sentence with Γι' αυτό."],
             model=P("""
                Η εκμάθηση μιας ξένης γλώσσας είναι, νομίζω, μία από τις καλύτερες επενδύσεις που μπορεί να κάνει κανείς. Πρώτα απ' όλα, μια ξένη γλώσσα ανοίγει πόρτες στην αγορά εργασίας, αφού οι εταιρείες αναζητούν υπαλλήλους που επικοινωνούν με πελάτες από άλλες χώρες. Επιπλέον, όταν ταξιδεύουμε και μιλάμε τη γλώσσα του τόπου, γνωρίζουμε τους ανθρώπους από κοντά και όχι μόνο τα αξιοθέατα. Τέλος, η εκμάθηση μιας γλώσσας είναι εξαιρετική άσκηση για το μυαλό σε οποιαδήποτε ηλικία. Γι' αυτό, όσο κουραστική κι αν είναι στην αρχή, η προσπάθεια αξίζει τον κόπο.
             """),
             model_en=P("""
                Learning a foreign language is, I think, one of the best investments one can make. First of all, a foreign language opens doors in the job market, since companies look for employees who can communicate with clients from other countries. Moreover, when we travel and speak the local language, we get to know the people up close and not only the sights. Finally, learning a language is excellent exercise for the mind at any age. That is why, however tiring it may be at the start, the effort is worth it.
             """)),
        dict(id="paragraph-2", level="B1", words=120,
             el="Γράψτε μια παράγραφο για τα μειονεκτήματα της ζωής σε μια μεγάλη πόλη. (100–120 λέξεις)",
             en="Write a paragraph on the disadvantages of living in a big city. (100–120 words)",
             plan=["Mirror the model: topic sentence, three supports, closing sentence.", "Use one reason clause with επειδή at the start of a sentence."]),
        dict(id="paragraph-3", level="B2", words=150,
             el="Γράψτε δύο παραγράφους: στην πρώτη τα πλεονεκτήματα της ζωής στο χωριό, στη δεύτερη τα μειονεκτήματα. Κλείστε με τη δική σας γνώμη. (150 λέξεις)",
             en="Write two paragraphs: the advantages of village life, then the disadvantages. End with your own view. (150 words)",
             plan=["Paragraph 1: topic sentence + two advantages.", "Paragraph 2 opens with Από την άλλη πλευρά, + two disadvantages.", "One closing sentence with your view: Κατά τη γνώμη μου, …"]),
    ],
)

U02 = dict(
    id="linking", kind="unit", part="found", level="B1", el="Από απλές σε σύνθετες προτάσεις", title="Linking: from short sentences to complex ones",
    intro=[
        {"p": "Strings of short main clauses read like a shopping list and cap your syntax mark. The cure is a small kit of subordinators: **που / ο οποίος** (who, which), **όταν, ενώ, αφού** (time), **επειδή** (reason), **για να** (purpose), **παρόλο που** (although), **αν** (if). Combine two or three facts per sentence, not more."},
    ],
    structure=[
        ["Σχετική πρόταση", "Relative clause", "που (invariable) or ο οποίος, η οποία, το οποίο (formal, agrees with its noun)."],
        ["Χρονική πρόταση", "Time clause", "όταν, μόλις, ενώ, αφού, πριν, μέχρι να."],
        ["Αιτιολογική πρόταση", "Reason clause", "επειδή, γιατί, αφού, καθώς."],
        ["Τελική πρόταση", "Purpose clause", "για να + subjunctive."],
        ["Εναντιωματική πρόταση", "Concessive clause", "παρόλο που, αν και."],
    ],
    phrases=[
        dict(el="Σύνδεσμοι που χρειάζεστε από την αρχή", en="The starter kit", items=ph(
            ("Η πόλη, η οποία…", "The city, which…"),
            ("…ένα καφέ που βρίσκεται…", "…a café that is…"),
            ("Όταν φτάσαμε, …", "When we arrived, …"),
            ("Παρόλο που ήταν αργά, …", "Although it was late, …"),
            ("…για να μην αργήσουμε.", "…so as not to be late."),
            ("Πρώτα… Έπειτα… Στο τέλος…", "First… Then… In the end…"),
        )),
    ],
    models=[dict(
        el="Μια μέρα στο Ναύπλιο", en="A day in Nafplio", level="B1",
        task_el="Ξαναγράψτε τις σύντομες προτάσεις σε ένα κείμενο με σύνθετες προτάσεις.",
        task_en="Rewrite the short sentences as one text of complex sentences.",
        before="Πήγαμε στο Ναύπλιο. Ήταν Σάββατο. Ο καιρός ήταν ωραίος. Περπατήσαμε στην παλιά πόλη. Η παλιά πόλη είναι πολύ όμορφη. Ανεβήκαμε στο Παλαμήδι. Ήταν κουραστικό. Η θέα ήταν υπέροχη. Φάγαμε σε μια ταβέρνα. Η ταβέρνα ήταν δίπλα στη θάλασσα.",
        text=P("""
            Το περασμένο Σάββατο, επειδή ο καιρός ήταν ωραίος, πήγαμε εκδρομή στο Ναύπλιο. Πρώτα περπατήσαμε στην παλιά πόλη, η οποία είναι πραγματικά πανέμορφη, με στενά δρομάκια και νεοκλασικά σπίτια. Έπειτα ανεβήκαμε στο Παλαμήδι. Παρόλο που η ανάβαση ήταν κουραστική, η θέα από ψηλά μας αποζημίωσε. Το μεσημέρι φάγαμε σε μια ταβέρνα που βρισκόταν δίπλα στη θάλασσα, και γυρίσαμε στην Αθήνα αργά το βράδυ, κουρασμένοι αλλά ευχαριστημένοι.
        """),
        text_en=P("""
            Last Saturday, because the weather was fine, we went on a trip to Nafplio. First we walked around the old town, which is truly beautiful, with narrow lanes and neoclassical houses. Then we climbed up to the Palamidi fortress. Although the climb was tiring, the view from the top made up for it. At midday we ate at a taverna that was right by the sea, and we came back to Athens late in the evening, tired but happy.
        """),
        notes=[
            "Ten sentences became five. Each new sentence joins two or three facts, never more.",
            "**η οποία** agrees with **πόλη** (feminine singular); **που** after ταβέρνα would also be correct, and is more natural in speech.",
            "**Παρόλο που** concedes a negative point and then overturns it: a pattern examiners love.",
            "**κουρασμένοι αλλά ευχαριστημένοι**: two participles at the end of the sentence describe the subject, a compact way to close a narrative.",
        ],
    )],
    grammar=[dict(
        title="ο οποίος: agreement and case",
        en="**ο οποίος** takes its gender and number from the noun it refers to, and its case from its role in the relative clause. After a preposition you must use it (or a preposition + **που** is impossible): **στην οποία, με τον οποίο, για τους οποίους**. Plain **που** covers subject and object.",
        examples=ex(
            ("Η πόλη στην οποία γεννήθηκα είναι μικρή.", "The town where (in which) I was born is small."),
            ("Ο φίλος με τον οποίο δουλεύω είναι από την Κρήτη.", "The friend I work with is from Crete."),
            ("Τα βιβλία που μου δάνεισες ήταν υπέροχα.", "The books you lent me were wonderful."),
            ("Οι μαθητές, οι οποίοι είχαν διαβάσει, πέρασαν όλοι.", "The pupils, who had studied, all passed."),
        ),
    )],
    drills=[
        q("Η πόλη, ___ γεννήθηκα, είναι μικρή.", ["στην οποία", "την οποία", "η οποία"], "στην οποία", "γεννιέμαι σε μια πόλη: the preposition σε comes in front of the relative."),
        q("Έχω έναν φίλο. Ο φίλος μου ζει στην Κρήτη. →", ["Έχω έναν φίλο που ζει στην Κρήτη.", "Έχω έναν φίλο τον οποίο ζει στην Κρήτη.", "Έχω έναν φίλο ο οποίο ζει στην Κρήτη."], "Έχω έναν φίλο που ζει στην Κρήτη."),
        q("___ βρέχει, θα πάμε βόλτα.", ["Παρόλο που", "Επειδή", "Για να"], "Παρόλο που", "Rain would normally stop a walk, so this is a concession."),
        q("Έφυγα νωρίς ___ μην αργήσω στη δουλειά.", ["για να", "επειδή", "όταν"], "για να", "Purpose: για να + subjunctive (μην αργήσω)."),
    ],
    tasks=[
        dict(id="linking-1", level="B1", words=60,
             el="Ξαναγράψτε το κείμενο σε τρεις ή τέσσερις σύνθετες προτάσεις: «Η Μαρία είναι φοιτήτρια. Σπουδάζει ιατρική. Μένει στη Θεσσαλονίκη. Δουλεύει τα βράδια σε ένα καφέ. Θέλει να πληρώνει μόνη της το ενοίκιο. Είναι πολύ κουρασμένη. Δεν τα παρατάει. Θέλει να γίνει παιδίατρος.»",
             en="Rewrite the text as three or four complex sentences: “Maria is a student. She studies medicine. She lives in Thessaloniki. She works evenings in a café. She wants to pay the rent herself. She is very tired. She doesn't give up. She wants to become a paediatrician.”",
             plan=["Join the facts about who she is.", "Use για να for why she works.", "Use παρόλο που for tired / doesn't give up, and γιατί for her dream."],
             model=P("""
                Η Μαρία είναι φοιτήτρια ιατρικής και μένει στη Θεσσαλονίκη. Τα βράδια δουλεύει σε ένα καφέ, για να πληρώνει μόνη της το ενοίκιό της. Παρόλο που είναι πολύ κουρασμένη, δεν τα παρατάει, γιατί το όνειρό της είναι να γίνει παιδίατρος.
             """),
             model_en=P("""
                Maria is a medical student and lives in Thessaloniki. In the evenings she works in a café, so that she can pay her rent herself. Although she is very tired, she doesn't give up, because her dream is to become a paediatrician.
             """)),
        dict(id="linking-2", level="B1", words=120,
             el="Περιγράψτε την τελευταία σας εκδρομή σε 120 λέξεις. Χρησιμοποιήστε τουλάχιστον πέντε από τους συνδέσμους: όταν, επειδή, παρόλο που, για να, ο οποίος, που, έπειτα.",
             en="Describe your last trip in 120 words, using at least five of: όταν, επειδή, παρόλο που, για να, ο οποίος, που, έπειτα.",
             plan=["When and where, and why you went (επειδή).", "What you did, in order (Πρώτα, Έπειτα, Στο τέλος).", "One concession (παρόλο που) and one relative clause."]),
        dict(id="linking-3", level="B2", words=150,
             el="Γράψτε ένα σύντομο διήγημα (150 λέξεις) που αρχίζει: «Μόλις άνοιξα την πόρτα, κατάλαβα ότι κάτι δεν πήγαινε καλά.»",
             en="Write a short story (150 words) beginning: “As soon as I opened the door, I realised something was wrong.”",
             plan=["Past tenses: aorist for events, imperfect for background.", "At least one ενώ (while) and one μέχρι να (until)."]),
    ],
)

U03 = dict(
    id="register", kind="unit", part="found", level="B1+", el="Ύφος: φιλικό, ουδέτερο, επίσημο", title="Register: friendly, neutral, formal",
    intro=[
        {"p": "Register (ύφος) is a scored criterion, and the most common B2 failure is mixing it: a formal letter that slips into εσύ, or a friendly one full of «θα ήθελα να σας ενημερώσω». Decide before you write, and keep the same address, verbs and vocabulary from the greeting to the signature."},
    ],
    structure=[
        ["Προσφώνηση", "Greeting", "Γεια σου Νίκο! / Αγαπητή μου Ελένη, ↔ Αξιότιμε κύριε Παπαδόπουλε, / Αξιότιμοι κύριοι,"],
        ["Πρόσωπο", "Address", "εσύ (στείλε μου) ↔ εσείς (θα μπορούσατε να μου στείλετε)"],
        ["Ρήματα", "Verbs", "θέλω, ψάχνω, παίρνω ↔ θα ήθελα, αναζητώ, λαμβάνω"],
        ["Σύνταξη", "Syntax", "short sentences, questions, exclamations ↔ longer sentences, nouns, passives"],
        ["Αποχαιρετισμός", "Sign-off", "Φιλιά, / Τα λέμε, ↔ Με εκτίμηση, / Με τιμή,"],
    ],
    phrases=[
        dict(el="Καθημερινό ↔ επίσημο λεξιλόγιο", en="Everyday ↔ formal vocabulary", items=ph(
            ("ψάχνω ↔ αναζητώ", "look for"),
            ("παίρνω (ένα γράμμα) ↔ λαμβάνω", "receive"),
            ("δίνω ↔ παρέχω", "give, provide"),
            ("τελειώνω ↔ ολοκληρώνω", "finish, complete"),
            ("ρωτάω ↔ ζητώ πληροφορίες", "ask"),
            ("λέω ↔ αναφέρω, δηλώνω", "say, state"),
            ("έχει ↔ διαθέτει", "has, offers"),
            ("φτιάχνω ↔ δημιουργώ, διοργανώνω", "make, organise"),
            ("αρχίζω ↔ ξεκινώ, εγκαινιάζω", "begin, launch"),
            ("εργαστήρι ↔ εργαστήριο", "workshop (everyday ↔ formal form)"),
        )),
        dict(el="Ευγένεια", en="Politeness", items=ph(
            ("Θα ήθελα να…", "I would like to…", "Ε"),
            ("Θα μπορούσατε να…;", "Could you…?", "Ε"),
            ("Θα σας παρακαλούσα να…", "I would ask you to…", "Ε"),
            ("Ευχαριστώ εκ των προτέρων.", "Thank you in advance.", "Ε"),
            ("Μου λες…;", "Can you tell me…?", "Φ"),
        )),
    ],
    models=[
        dict(el="Το ίδιο μήνυμα σε φίλη", en="The message to a friend", level="B1",
             task_el="Ρωτάτε μια φίλη για τα μαθήματα κεραμικής που κάνει.", task_en="You ask a friend about the pottery classes she takes.",
             text=P("""
                Γεια σου Ελένη μου!

                Τι κάνεις; Άκουσα ότι κάνεις μαθήματα κεραμικής και ζήλεψα! Θέλω κι εγώ να ξεκινήσω, αλλά δεν ξέρω πού να πάω. Μου λες πού είναι το εργαστήρι και πόσο κοστίζει; Α, και κάθε πότε γίνονται τα μαθήματα; Αν υπάρχει θέση, μπορεί να έρθω μαζί σου από τον άλλο μήνα.

                Τα λέμε σύντομα,
                Άννα
             """),
             text_en=P("""
                Hi Eleni dear!

                How are you? I heard you're taking pottery classes and I'm jealous! I want to start too, but I don't know where to go. Can you tell me where the workshop is and how much it costs? Oh, and how often are the classes? If there's a place, I might come with you from next month.

                Speak soon,
                Anna
             """),
             notes=["Questions, exclamations, short sentences, εσύ throughout. **Μου λες…;** is the friendly way to ask for information.", "**ζήλεψα** (I'm jealous, literally ‘I envied’) and **Α, και…** are spoken Greek, perfect here and impossible in a formal letter."]),
        dict(el="Το ίδιο μήνυμα στο εργαστήριο", en="The message to the workshop", level="B1+",
             task_el="Γράφετε στο εργαστήριο για να ζητήσετε πληροφορίες.", task_en="You write to the workshop to ask for information.",
             text=P("""
                Αξιότιμοι κύριοι,

                Με ενδιαφέρον πληροφορήθηκα ότι το εργαστήριό σας οργανώνει μαθήματα κεραμικής για ενήλικες. Θα ήθελα να σας παρακαλέσω να μου στείλετε περισσότερες πληροφορίες σχετικά με το πρόγραμμα, το κόστος και τη διάρκεια των μαθημάτων. Επιπλέον, θα ήθελα να μάθω εάν υπάρχουν ακόμη διαθέσιμες θέσεις για τον επόμενο κύκλο.

                Ευχαριστώ εκ των προτέρων για τον χρόνο σας.

                Με εκτίμηση,
                Άννα Δημητρίου
             """),
             text_en=P("""
                Dear Sirs,

                I was interested to learn that your workshop runs pottery classes for adults. I would like to ask you to send me more information about the programme, the cost and the length of the classes. In addition, I would like to know whether there are still places available for the next course.

                Thank you in advance for your time.

                Yours sincerely,
                Anna Dimitriou
             """),
             notes=["Same content, different register: **πληροφορήθηκα** for ‘I heard’, **σχετικά με** for ‘about’, **εάν** for ‘if’, **εργαστήριο** instead of εργαστήρι.", "The questions became statements (θα ήθελα να μάθω εάν…): formal Greek avoids direct questions to the recipient.", "**το εργαστήριό σας**: a word stressed on the third syllable from the end takes a second accent before an enclitic pronoun."]),
    ],
    grammar=[dict(
        title="The polite plural",
        en="With εσείς for one person, the **verb is plural** but an **adjective or participle stays singular** and agrees with the person's sex. Use **θα + imperfect** (θα ήθελα, θα μπορούσατε) to soften a request.",
        examples=ex(
            ("Είστε πολύ ευγενικός, κύριε Ιωάννου.", "You are very kind, Mr Ioannou."),
            ("Είστε ικανοποιημένη από τις υπηρεσίες μας, κυρία Λάμπρου;", "Are you satisfied with our services, Mrs Lambrou?"),
            ("Θα μπορούσατε να μου στείλετε τον κατάλογο;", "Could you send me the catalogue?"),
        ),
    )],
    drills=[
        q("Ποια φράση ταιριάζει σε επίσημη επιστολή;", ["Σας γράφω για να ζητήσω πληροφορίες.", "Σου γράφω να ρωτήσω κάτι.", "Γράφω γιατί θέλω να μάθω."], "Σας γράφω για να ζητήσω πληροφορίες."),
        q("Το επίσημο συνώνυμο του «ψάχνω» είναι:", ["αναζητώ", "βρίσκω", "κοιτάζω"], "αναζητώ"),
        q("Πώς κλείνετε ένα email σε φίλο;", ["Φιλιά,", "Με εκτίμηση,", "Με τιμή,"], "Φιλιά,"),
        q("Κυρία Νικολάου, είστε ___ από το δωμάτιό σας;", ["ευχαριστημένη", "ευχαριστημένες", "ευχαριστημένοι"], "ευχαριστημένη", "Polite plural verb, singular adjective that agrees with the person."),
        q("___ να μου στείλετε τον κατάλογο;", ["Θα μπορούσατε", "Μπορείς", "Στείλε"], "Θα μπορούσατε"),
    ],
    tasks=[
        dict(id="register-1", level="B1+", words=80,
             el="Ξαναγράψτε το μήνυμα σε επίσημο ύφος: «Γεια σας! Θέλω να κλείσω ένα δωμάτιο για δύο άτομα από τις 10 ως τις 14 Ιουλίου. Έχετε κάτι με θέα στη θάλασσα; Πόσο κάνει; Πείτε μου και αν έχει πάρκινγκ. Ευχαριστώ!»",
             en="Rewrite the message formally: “Hello! I want to book a room for two from 10 to 14 July. Do you have anything with a sea view? How much is it? Tell me also if there's parking. Thanks!”",
             plan=["Formal greeting.", "Turn each question into θα ήθελα / θα σας παρακαλούσα να με ενημερώσετε…", "Formal vocabulary: δίκλινο δωμάτιο, διανυκτέρευση, χώρος στάθμευσης, διαθέτω.", "Formal sign-off."],
             model=P("""
                Αξιότιμοι κύριοι,

                Θα ήθελα να κάνω κράτηση ενός δίκλινου δωματίου για το διάστημα από τις 10 έως τις 14 Ιουλίου. Θα σας παρακαλούσα να με ενημερώσετε εάν διαθέτετε δωμάτιο με θέα στη θάλασσα, καθώς και ποια είναι η τιμή ανά διανυκτέρευση. Τέλος, θα ήθελα να μάθω αν το ξενοδοχείο διαθέτει χώρο στάθμευσης.

                Ευχαριστώ εκ των προτέρων.

                Με εκτίμηση,
                Ι. Παππάς
             """),
             model_en=P("""
                Dear Sirs,

                I would like to book a double room for the period from 10 to 14 July. I would be grateful if you could let me know whether you have a room with a sea view, and what the price per night is. Finally, I would like to know whether the hotel has parking.

                Thank you in advance.

                Yours sincerely,
                I. Pappas
             """)),
        dict(id="register-2", level="B1+", words=100,
             el="Είστε η Ελένη. Απαντήστε στο μήνυμα της Άννας (μοντέλο 1): πού είναι το εργαστήρι, πόσο κοστίζει, πότε γίνονται τα μαθήματα. (100 λέξεις)",
             en="You are Eleni. Answer Anna's message (model 1): where the workshop is, the cost, when classes are held. (100 words)",
             plan=["Friendly greeting and reaction (Τι ωραία ιδέα!).", "Answer all three questions.", "Invite her to come along; friendly sign-off."]),
        dict(id="register-3", level="B2", words=150,
             el="Γράφετε σε ένα κέντρο ελληνικών για ξένους για να ζητήσετε πληροφορίες για τα εντατικά μαθήματα του καλοκαιριού: επίπεδα, ώρες, κόστος, διαμονή. (150 λέξεις)",
             en="Write to a Greek-language school asking about its summer intensive courses: levels, hours, cost, accommodation. (150 words)",
             plan=["Formal greeting; say where you saw the course.", "Introduce yourself in one sentence (level, why).", "Four requests, each in a different polite formula.", "Thanks and formal sign-off."]),
    ],
)

U04 = dict(
    id="friendly-email", kind="unit", part="personal", level="B1", el="Φιλικό email: νέα και πρόσκληση", title="Friendly email: news and an invitation",
    intro=[
        {"p": "The friendly email is the base of Part A. Its shape never changes: greeting, a warm opening, the reason you are writing, the body, a request or invitation, a warm close. What lifts it to B2 is natural phrasing (Μάντεψε τι έγινε!, Θα χαρώ πολύ αν…) and full sentences rather than notes."},
    ],
    structure=[
        ["Χαιρετισμός", "Greeting", "Γεια σου Κώστα! / Αγαπητή μου Μαρία,"],
        ["Εισαγωγή", "Warm opening", "Τι κάνεις; Πώς πάει η δουλειά; Συγγνώμη που άργησα να σου γράψω."],
        ["Αφορμή", "Why you're writing", "Σου γράφω γιατί… / Έχω μεγάλα νέα!"],
        ["Κύριο μέρος", "Body", "One paragraph per point: news, description, plans."],
        ["Πρόσκληση / αίτημα", "Invitation or request", "Θα χαρώ πολύ αν έρθεις. / Τι θα έλεγες να…;"],
        ["Κλείσιμο", "Close", "Γράψε μου σύντομα. / Περιμένω νέα σου. + Φιλιά, / Με αγάπη,"],
    ],
    phrases=[
        dict(el="Ανοίγματα", en="Openings", items=ph(
            ("Τι κάνεις; Ελπίζω να είσαι καλά.", "How are you? I hope you're well."),
            ("Συγγνώμη που άργησα τόσο να σου απαντήσω.", "Sorry I took so long to reply."),
            ("Χάρηκα πολύ που πήρα το μήνυμά σου.", "I was so glad to get your message."),
        )),
        dict(el="Νέα", en="Giving news", items=ph(
            ("Έχω μεγάλα νέα!", "I have big news!"),
            ("Μάντεψε τι έγινε!", "Guess what happened!"),
            ("Να σου πω τα νέα μου.", "Let me tell you my news."),
        )),
        dict(el="Πρόσκληση", en="Inviting", items=ph(
            ("Θα ήθελες να…;", "Would you like to…?"),
            ("Τι θα έλεγες να…;", "How about…?"),
            ("Θα χαρώ πολύ αν έρθεις.", "I'd be really happy if you came."),
            ("Έλα κι εσύ!", "Come too!"),
        )),
        dict(el="Απάντηση σε πρόσκληση", en="Accepting and declining", items=ph(
            ("Φυσικά και θα έρθω!", "Of course I'll come!"),
            ("Δεν θα το έχανα με τίποτα.", "I wouldn't miss it for anything."),
            ("Δυστυχώς δεν μπορώ, γιατί…", "Unfortunately I can't, because…"),
            ("Τι λες να βρεθούμε την άλλη εβδομάδα;", "What do you say we meet next week?"),
        )),
        dict(el="Κλεισίματα", en="Closings", items=ph(
            ("Γράψε μου σύντομα.", "Write soon."),
            ("Περιμένω νέα σου.", "I look forward to hearing from you."),
            ("Φιλιά, / Με αγάπη, / Τα λέμε,", "Love, / With love, / Speak soon,"),
        )),
    ],
    models=[dict(
        el="Μετακόμιση και γιορτή", en="A new flat and a name day", level="B1",
        task_el="Γράφετε σε έναν φίλο σας για να του πείτε ότι μετακομίσατε και να τον καλέσετε στη γιορτή σας. (150 λέξεις)",
        task_en="Write to a friend to tell him you've moved and to invite him to your name-day party. (150 words)",
        text=P("""
            Γεια σου Κώστα!

            Τι κάνεις; Πώς πάει η καινούργια δουλειά; Συγγνώμη που άργησα τόσο να σου απαντήσω, αλλά τον τελευταίο μήνα δεν είχα καθόλου ελεύθερο χρόνο.

            Έχω μεγάλα νέα: επιτέλους μετακόμισα! Το καινούργιο μου διαμέρισμα είναι στο Παγκράτι, κοντά στο Καλλιμάρμαρο. Είναι μικρό, αλλά φωτεινό, και έχει ένα μπαλκόνι με θέα στον Υμηττό. Τις πρώτες μέρες ήταν χάος με τα κουτιά, αλλά τώρα όλα είναι στη θέση τους.

            Την Κυριακή, 8 Νοεμβρίου, γιορτάζω, και σκέφτομαι να κάνω ένα μικρό πάρτι στο σπίτι, για να γιορτάσουμε μαζί και τη γιορτή μου και το καινούργιο σπίτι. Θα έρθουν και ο Γιάννης με τη Σοφία. Θα χαρώ πολύ αν έρθεις κι εσύ. Ξεκινάμε γύρω στις οχτώ.

            Γράψε μου αν μπορείς να έρθεις.

            Φιλιά,
            Μιχάλης
        """),
        text_en=P("""
            Hi Kostas!

            How are you? How's the new job going? Sorry I took so long to reply, but this last month I've had no free time at all.

            I have big news: I've finally moved! My new flat is in Pangrati, near the Panathenaic Stadium. It's small but bright, and it has a balcony looking out on Mount Hymettus. The first few days were chaos with all the boxes, but now everything is in its place.

            On Sunday 8 November it's my name day, and I'm thinking of having a little party at home, so we can celebrate both my name day and the new flat together. Giannis and Sofia are coming too. I'd be really happy if you came as well. We start around eight.

            Let me know if you can come.

            Love,
            Michalis
        """),
        notes=[
            "Six blocks, each with one job: greeting, warm opening, news, invitation with practical details (day, time, who), request for an answer, sign-off.",
            "**Culture:** 8 November is the feast of the Archangels Michael and Gabriel, so every Μιχάλης, Μιχαήλ and Γαβριήλ celebrates. Name days (ονομαστικές γιορτές) are traditionally as big as birthdays; the greeting is **Χρόνια πολλά!**",
            "**και… και…** (both… and…) and **κι εσύ** (you too) keep the tone natural without slang.",
        ],
    )],
    grammar=[dict(
        title="Where the possessive goes",
        en="The weak possessive (μου, σου, του…) normally follows the noun: **το διαμέρισμά μου**. With an adjective it can follow the adjective instead: **το καινούργιο μου διαμέρισμα**. If the word before it is stressed on the third syllable from the end, it takes a second accent: διαμέρισμά μου, όνομά της.",
        examples=ex(
            ("Το διαμέρισμά μου είναι μικρό.", "My flat is small."),
            ("Το καινούργιο μου διαμέρισμα είναι φωτεινό.", "My new flat is bright."),
            ("Ο φίλος μου ήρθε νωρίς.", "My friend came early. (no extra accent: φίλος is stressed on the second-last syllable)"),
        ),
    )],
    drills=[
        q("Ποια φράση ταιριάζει για να καλέσετε έναν φίλο;", ["Τι θα έλεγες να έρθεις την Κυριακή;", "Θα σας παρακαλούσα να παρευρεθείτε.", "Παρακαλείστε να έρθετε."], "Τι θα έλεγες να έρθεις την Κυριακή;"),
        q("Συγγνώμη που ___ τόσο να σου απαντήσω.", ["άργησα", "αργώ", "θα αργήσω"], "άργησα"),
        q("Ποιο είναι σωστό;", ["το όνομά μου", "το όνομα μού", "το ονομά μου"], "το όνομά μου", "όνομα is stressed on the third syllable from the end, so it takes a second accent before μου."),
        q("Στη γιορτή κάποιου λέμε:", ["Χρόνια πολλά!", "Καλή όρεξη!", "Καλό ταξίδι!"], "Χρόνια πολλά!"),
    ],
    tasks=[
        dict(id="friendly-email-1", level="B1", words=120,
             el="Είστε ο Κώστας. Απαντήστε στον Μιχάλη: δεχτείτε την πρόσκληση, πείτε τι θα φέρετε και δώστε του τα δικά σας νέα. (100–120 λέξεις)",
             en="You are Kostas. Reply to Michalis: accept the invitation, say what you'll bring and give him your own news. (100–120 words)",
             plan=["Congratulate him on the flat.", "Accept; say when you'll arrive and offer to bring something.", "Your news in two sentences.", "Χρόνια πολλά, sign-off."],
             model=P("""
                Αγαπητέ μου Μιχάλη,

                Χίλια συγχαρητήρια για το καινούργιο σπίτι! Το Παγκράτι είναι από τις αγαπημένες μου γειτονιές, οπότε θα έρχομαι συχνά για καφέ στο μπαλκόνι σου.

                Φυσικά και θα έρθω την Κυριακή! Δεν θα έχανα τη γιορτή σου με τίποτα. Μάλλον θα αργήσω λίγο, γιατί έχω τραπέζι στους γονείς μου το μεσημέρι, αλλά θα είμαι εκεί γύρω στις εννιά. Πες μου αν θέλεις να φέρω κάτι, ένα γλυκό ή ένα κρασί.

                Όσο για τη δουλειά, πάει καλά, αν και έχω πολλές υποχρεώσεις. Θα σου πω περισσότερα από κοντά.

                Χρόνια πολλά από τώρα!

                Φιλιά,
                Κώστας
             """),
             model_en=P("""
                Dear Michalis,

                A thousand congratulations on the new flat! Pangrati is one of my favourite neighbourhoods, so I'll be coming round often for coffee on your balcony.

                Of course I'll come on Sunday! I wouldn't miss your name day for anything. I'll probably be a bit late, because I'm having lunch at my parents', but I'll be there around nine. Tell me if you want me to bring anything, a dessert or some wine.

                As for work, it's going well, although I have a lot on. I'll tell you more in person.

                Many happy returns in advance!

                Love,
                Kostas
             """)),
        dict(id="friendly-email-2", level="B1", words=120,
             el="Δεν μπορείτε να πάτε στη γιορτή του Μιχάλη. Γράψτε του για να του ευχηθείτε, να εξηγήσετε γιατί δεν μπορείτε και να προτείνετε να βρεθείτε άλλη μέρα. (100–120 λέξεις)",
             en="You can't go to Michalis's party. Write to wish him well, explain why, and suggest meeting another day. (100–120 words)",
             plan=["Χρόνια πολλά first.", "Δυστυχώς δεν μπορώ, γιατί… (a real reason).", "Τι λες να βρεθούμε…; with a concrete day."]),
        dict(id="friendly-email-3", level="B2", words=200,
             el="Ένας φίλος σας από το εξωτερικό θα έρθει στην πόλη σας για πρώτη φορά. Γράψτε του για να τον καλέσετε να μείνει σπίτι σας και να του προτείνετε τι θα κάνετε μαζί. (200 λέξεις)",
             en="A friend from abroad is visiting your city for the first time. Invite him to stay with you and suggest what you'll do together. (200 words)",
             plan=["Warm opening, delight at the news.", "Invitation to stay + practical details.", "Two paragraphs of plans (sights, food, a day trip).", "Ask what he'd like; warm close."]),
    ],
)

ITEMS = [GUIDE, U01, U02, U03, U04]
