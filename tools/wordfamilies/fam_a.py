from common import G

CHAPTERS = [dict(
    id="build", part="Α", el="Πώς χτίζεται μια ελληνική λέξη", title="How a Greek word is built",
    level="A2–C1",
    intro=[
        {"p": "Most Greek words you meet after A2 are not new at all. They are a root you already know, a prefix in front of it and a suffix behind it. Once you can see the three parts, one known word opens a dozen others: from **γράφω** *write* come **γραφή** *writing*, **γράμμα** *letter*, **γραπτός** *written*, **γραφείο** *office, desk*, **συγγραφέας** *author*, **περιγράφω** *describe*, **υπογραφή** *signature* and **φωτογραφία** *photograph*."},
        {"p": "This guide shows the parts first (prefixes, then suffixes) and then the great root families. Every word is tappable, and each chapter ends with a production drill: you see the English and the root, and you type the Greek word yourself."},
        {"table": {"head": ["Part", "What it does", "Example"], "rows": [
            ["Root (ρίζα)", "carries the core meaning", "**γραφ-** write"],
            ["Prefix (πρόθημα)", "adds direction, negation, degree", "**υπο**γράφω *sign* (write under)"],
            ["Suffix (επίθημα)", "makes a noun, adjective, verb or adverb", "γραφ**είο** *office* (place of writing)"],
            ["Ending (κατάληξη)", "marks case, number, person", "γραφεί**ου**, γράφ**ουμε**"],
            ["Compound (σύνθετη λέξη)", "two roots joined, usually by -ο-", "φωτ**ο**γραφία *photograph*"],
        ]}},
    ],
    sections=[
        dict(el="Το θέμα του αορίστου", title="The aorist stem feeds the nouns", level="B1", body=[
            {"p": "The single most useful rule: many nouns and adjectives are built on the **aorist stem** of the verb, not on the present. If you know the aorist, you can usually guess the noun."},
            {"table": {"head": ["Verb", "Aorist", "The act (-ση / -ξη)", "The doer (-της)", "Adjective (-τός / -τικός)"], "rows": [
                ["λύνω *solve, untie*", "έλυ**σ**α", "λύ**ση** *solution*", "", "λυ**τός** *loose*"],
                ["αποφασίζω *decide*", "αποφάσι**σ**α", "απόφα**ση** *decision*", "", "αποφασι**στικός** *decisive*"],
                ["οργανώνω *organise*", "οργάνω**σ**α", "οργάνω**ση** *organisation*", "οργανω**τής** *organiser*", "οργανω**τικός** *organisational*"],
                ["παρατηρώ *observe*", "παρατήρη**σ**α", "παρατήρη**ση** *observation, remark*", "παρατηρη**τής** *observer*", "παρατηρη**τικός** *observant*"],
                ["εξηγώ *explain*", "εξήγη**σ**α", "εξήγη**ση** *explanation*", "", "εξηγη**τικός** *explanatory*"],
                ["ανοίγω *open*", "άνοι**ξ**α", "άνοι**ξη** *spring (the opening of the year)*", "", "ανοι**χτός** *open*"],
                ["γράφω *write*", "έγρα**ψ**α", "", "", "γρα**πτός** *written*"],
                ["διδάσκω *teach*", "δίδα**ξ**α", "", "", "διδα**κτικός** *instructive, teaching*"],
            ]}},
            {"tip": "Rule of thumb: aorist in **-σα** → noun in **-ση**; aorist in **-ξα** → noun in **-ξη** (ανοίγω/άνοιξα → **άνοιξη** *spring*, *the opening*); aorist in **-ψα** → noun in **-ψη** (λείπω/έλειψα → **έλλειψη** *lack, shortage* (with the prefix εν-); καλύπτω/κάλυψα → **κάλυψη** *cover, coverage*)."},
            {"p": "The everyday noun of action in **-σιμο / -ξιμο / -ψιμο** is built the same way: **γράψιμο** *the writing (of it)*, **τρέξιμο** *running*, **ντύσιμο** *getting dressed, the way one dresses*, **πλύσιμο** *washing*, **μαγείρεμα** *cooking* (from -εύω verbs: -εμα)."},
        ]),
        dict(el="Εναλλαγή ε / ο", title="The ε / ο switch", level="B2", body=[
            {"p": "Greek inherited a vowel switch from its oldest stage: the verb has **ε**, the noun of the action or its result has **ο**. Seeing the pair lets you link words that look unrelated."},
            {"table": {"head": ["Verb (ε)", "Noun (ο)", "More of the family"], "rows": [
                ["λέ(γ)ω *say*", "λόγος *speech, reason*", "διάλογος, πρόλογος, λογικός"],
                ["φέρνω (φέρω) *bring, carry*", "φορά *time, turn*; φόρος *tax*", "διαφορά, μεταφορά, φορτίο"],
                ["στέλνω (στέλλω) *send*", "στολή *uniform*, στόλος *fleet*", "αποστολή, επιστολή, απόστολος"],
                ["τρέπω *turn*", "τρόπος *way, manner*; τροπή *turn*", "μετατροπή, τρόπαιο"],
                ["τρέφω *nourish*", "τροφή *food*", "τροφός, διατροφή, θρεπτικός"],
                ["κλέβω *steal*", "κλοπή *theft*", "κλέφτης, κλεψιά"],
                ["πλέκω *knit, weave*", "πλοκή *plot*", "περιπλοκή, συμπλοκή, πλεκτό"],
                ["σπέρνω *sow*", "σπόρος *seed*", "σπορά, διασπορά"],
                ["τρέμω *tremble*", "τρόμος *terror*", "τρομερός, ατρόμητος"],
                ["στρέφω *turn*", "στροφή *turn, bend*", "επιστροφή, καταστροφή, αναστροφή"],
            ]}},
        ]),
        dict(el="Σύνθετες λέξεις", title="Compounds and the linking -ο-", level="B1", body=[
            {"p": "Two roots are usually joined by **-ο-**: **φως + γράφω → φωτ-ο-γραφία**, **νύχτα + λουλούδι → νυχτολούλουδο** *night-blooming jasmine*, **σπίτι + νοικοκύρης → σπιτονοικοκύρης** *landlord*. Before a vowel the -ο- usually drops: **αρχ-ηγός** *leader* (αρχή + άγω), **ψυχ-αγωγία** *entertainment*."},
            {"ex": [
                {"el": "μαχαίρι + πιρούνι → μαχαιροπίρουνα", "en": "knife + fork → cutlery (lit. knife-forks)"},
                {"el": "αλάτι + πιπέρι → αλατοπίπερο", "en": "salt + pepper → salt and pepper (seasoning)"},
                {"el": "άγριος + γάτα → αγριόγατα", "en": "wild + cat → wildcat"},
                {"el": "μέρα + νύχτα → μερόνυχτο", "en": "day + night → a full day, twenty-four hours"},
                {"el": "γλυκός + κοιτάζω → γλυκοκοιτάζω", "en": "sweet + look → look at someone tenderly"},
            ]},
            {"p": "Stress in a compound noun tends to move as far back as the ending allows: **λάδι + λεμόνι** gives **λαδολέμονο** *oil-and-lemon dressing*, **θάλασσα + πούλι** gives **θαλασσοπούλι** *seabird*."},
            {"p": "Compounds of two nouns of equal weight (**αντρόγυνο** *married couple*, **μαχαιροπίρουνα**) are called coordinate (*παρατακτικά*); those where the first part describes the second (**αγριόγατα**, **νυχτολούλουδο**) are determinative (*προσδιοριστικά*). The distinction matters for meaning: **ανθρωποφάγος** is one who eats people, not a person who eats."},
        ]),
        dict(el="Λόγια και λαϊκά θέματα", title="Learned and everyday stems side by side", level="B2", body=[
            {"p": "Modern Greek often keeps an everyday word and, beside it, the ancient root in learned derivatives. The everyday word may look nothing like its family, so learn the pairs: they unlock hundreds of words in the press and in the B2 and C1 papers."},
            {"table": {"head": ["Everyday word", "Ancient stem", "Learned derivatives"], "rows": [
                ["νερό *water*", "ύδωρ, υδρ-", "υδραυλικός *plumber*, ύδρευση *water supply*, αφυδάτωση *dehydration*"],
                ["ψάρι *fish*", "ιχθύς, ιχθυ-", "ιχθυοπωλείο *fishmonger's*, ιχθυοτροφείο *fish farm*"],
                ["ψωμί *bread*", "άρτος, αρτο-", "αρτοποιείο *bakery*, αρτοπωλείο *bread shop*"],
                ["κρασί *wine*", "οίνος, οινο-", "οινοποιείο *winery*, οινοπνευματώδη *spirits*"],
                ["σπίτι *house*", "οίκος, οικ-", "οικογένεια *family*, οικονομία *economy*, πολυκατοικία *apartment block*"],
                ["μάτι *eye*", "όμμα, οφθαλμός", "οφθαλμίατρος *eye doctor*, ομματοϋάλια *spectacles (formal)*"],
                ["αυτί *ear*", "ους, ωτ-", "ωτορινολαρυγγολόγος *ENT specialist*"],
                ["τρώω *eat*", "εσθίω; φαγ-", "φαγητό *food*, ανθρωποφάγος *cannibal*, φαγοπότι *feasting*"],
                ["βλέπω *see*", "ορώ, οπ-, οψ-", "όραση *sight*, οπτικός *optical*, άποψη *view, opinion*"],
            ]}},
            {"tip": "When a word in a newspaper begins with υδρ-, ιχθ-, αρτ-, οιν-, οικ- or οφθαλμ-, think νερό, ψάρι, ψωμί, κρασί, σπίτι, μάτι."},
        ]),
        dict(el="Πώς να μαντεύεις", title="How to guess an unknown word", level="B1", body=[
            {"list": [
                "Strip the ending: **ανεξαρτησία** → ανεξαρτησ-ία.",
                "Strip the prefixes one by one: **αν-εξ-αρτησ-ία**: αν- *not*, εξ- *from*, αρτ- *hang* (ancient αρτώ). Not hanging from something: *independence*.",
                "Find the root in a word you know: **απο-χώρ-ηση** → χώρος *space* → *withdrawal* (making space away).",
                "Check the suffix for the word class: -ση act, -της person, -είο place, -ικός relating to, -ώνω make.",
                "Test the guess against the sentence. Prefixes have several senses (παρα- can mean *beside*, *wrong* or *too much*), so context chooses.",
            ]},
            {"ex": [
                {"el": "Η κυβέρνηση ανακοίνωσε την αποκρατικοποίηση της εταιρείας.", "en": "The government announced the privatisation of the company (απο- away, κράτος state, -ποίηση making)."},
                {"el": "Το νερό είναι ακατάλληλο για πόση.", "en": "The water is unfit for drinking (α- not, κατάλληλος suitable; πόση drinking, from πίνω)."},
                {"el": "Ήταν μια αναπάντεχη επιτυχία.", "en": "It was an unexpected success (αν- not + απαντέχω, an old verb for *expect*)."},
            ]},
        ]),
    ],
    groups=[
        G("γραφ- / γραμ- / γραπτ-", "write", el="γράφω", m="""
γράφω|write
γραφή|writing; script
γράμμα|letter
γραμματική|grammar
γραμματέας|secretary
γραπτός|written
γραφείο|office; desk
γράψιμο|writing (the act)
συγγραφέας|author, writer
περιγράφω|describe
περιγραφή|description
υπογράφω|sign
υπογραφή|signature
φωτογραφία|photograph
ορθογραφία|spelling
πρόγραμμα|programme
διάγραμμα|diagram
γραμμή|line
""", note="The root shows up as **γραφ-** (present stem), **γραψ- / γραπτ-** (aorist and adjective) and **γραμ-** (result in -μα: γράμμα, πρόγραμμα, διάγραμμα)."),
    ],
)]
