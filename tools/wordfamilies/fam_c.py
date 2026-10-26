from common import G

CHAPTERS = [
dict(id="suffix-people", part="Γ", el="Πρόσωπα: ποιος κάνει τι", title="Suffixes for people: doers, trades, origin, women's forms", level="A2–B2",
 intro=[{"p": "A suffix tells you the word class before you know the meaning. These ones make **people**: the one who does something (-της, -έας), the one who practises a trade (-άς, -άρης, -τζής), the one who comes from somewhere (-αίος, -ιώτης, -ινός), and the women's forms that go with them."}],
 groups=[
  G("-της / -τής (fem. -τρια)", "the person who does it", m="""
ποιητής|poet
μαθητής|pupil, schoolchild
φοιτητής|university student
καθηγητής|teacher (secondary); professor
θεατής|spectator, viewer
κριτής|judge (of a contest)
ερευνητής|researcher
θεραπευτής|therapist
ελεγκτής|inspector; auditor
παίκτης|player
εργάτης|worker, labourer
κλέφτης|thief
ψεύτης|liar
""", note="Built on the verb's aorist stem: ερευνώ / ερεύνησα → **ερευνητής**, ελέγχω / έλεγξα → **ελεγκτής**, παίζω / έπαιξα → **παίκτης**. Women's forms mostly end in **-τρια**: μαθήτρια, φοιτήτρια, ερευνήτρια, παίκτρια, εργάτρια; a few in **-τρα** (κλέφτρα, ψεύτρα)."),
  G("-έας", "the person who does it (learned)", m="""
συγγραφέας|author, writer
γραμματέας|secretary
κουρέας|barber
αλιέας|fisherman
ιερέας|priest
γονέας|parent
""", note="**-έας** nouns of people are common gender in modern usage: **ο/η συγγραφέας**, **ο/η γραμματέας**. Not every -έας is a person: **τομέας** is a *sector*, **ανεμιστήρας** (-ήρας) a *fan*."),
  G("-άς / -άρης / -ής / -τζής", "trades and habits (everyday)", m="""
ψαράς|fisherman; fishmonger
γαλατάς|milkman
σιδεράς|blacksmith
φουρνάρης|baker
βαρκάρης|boatman
παπουτσής|shoemaker
καφετζής|café owner
ταξιτζής|taxi driver
μπογιατζής|house painter
σουβλατζής|souvlaki cook
""", note="The everyday trade suffixes attach to the thing worked with: ψάρι → **ψαράς**, γάλα → **γαλατάς**, φούρνος → **φουρνάρης**, ταξί → **ταξιτζής**. **-τζής** (from Turkish *-ci*) is still productive. Women's forms: ψαρού, ταξιτζού, καφετζού (colloquial), or the same noun with η."),
  G("-αίος / -ιώτης / -ινός / -ιός", "where someone is from", m="""
Αθηναίος|Athenian
Κερκυραίος|Corfiot
Πειραιώτης|man from Piraeus
Ηπειρώτης|man from Epirus
Μανιάτης|man from Mani
Θεσσαλονικιός|man from Thessaloniki
Πατρινός|man from Patras
Κρητικός|Cretan
νησιώτης|islander
χωριανός|fellow villager
πρωτευουσιάνος|someone from the capital
""", note="Each place has its own form and the women's forms differ too: Αθηναία, Κερκυραία, Πειραιώτισσα, Ηπειρώτισσα, Μανιάτισσα, Θεσσαλονικιά, Πατρινή, Κρητικιά, νησιώτισσα, χωριανή. Demonyms take a capital letter; νησιώτης and χωριανός do not, because they are not tied to one named place."),
  G("-ισσα / -αινα / -ίδα / -ού", "women's forms", m="""
βασίλισσα|queen
πριγκίπισσα|princess
γειτόνισσα|(female) neighbour
λύκαινα|she-wolf
ηρωίδα|heroine
παπαδιά|priest's wife
νοικοκυρά|housewife; landlady
""", note="Modern Greek increasingly keeps the masculine noun and changes only the article: **η γιατρός**, **η δικηγόρος**, **η βουλευτής** (the form βουλεύτρια is also used). Forms in -ισσα and -αινα are older and often belong to fixed words."),
 ]),

dict(id="suffix-abstract", part="Γ", el="Πράξεις, αποτελέσματα, ιδιότητες", title="Suffixes for actions, results and qualities", level="B1–C1",
 intro=[{"p": "These nouns name an **action** (-ση, -μός, -σιμο), its **result** (-μα), a **state or field** (-ία, -εία) or a **quality** (-ότητα, -οσύνη, -ιά). The learned and the everyday suffix can stand side by side with a difference in meaning: **η κράτηση** is a *reservation*, **το κράτημα** *the holding*; **το πλύσιμο** is the washing you do at home, **η πλύση** the wash cycle of a machine."}],
 groups=[
  G("-ση / -ξη / -ψη", "the act, the process (learned)", m="""
λύση|solution
κίνηση|movement; traffic
απόφαση|decision
σκέψη|thought
λήψη|reception, receipt
σύγκριση|comparison
εξήγηση|explanation
πράξη|act, deed
ανάπτυξη|development; growth
κράτηση|reservation, booking
ενημέρωση|update; briefing
ανάγνωση|reading
""", note="Feminine, plural in **-σεις** (οι αποφάσεις, οι σκέψεις). The consonant follows the aorist: έλυ**σ**α → λύ**ση**, έπραξα → πρά**ξη**, σκέφτηκα (ancient ἐσκεψάμην) → σκέ**ψη**."),
  G("-μός", "the act, the process", m="""
καθαρισμός|cleaning
χωρισμός|separation; divorce
σεισμός|earthquake
ορισμός|definition
λογαριασμός|bill; account
εμβολιασμός|vaccination
χαιρετισμός|greeting
θαυμασμός|admiration
ανασχηματισμός|(cabinet) reshuffle
διωγμός|persecution
""", note="Masculine, mostly from verbs in -ίζω and -άζω: καθαρίζω → **καθαρισμός**, θαυμάζω → **θαυμασμός**, χαιρετώ (old χαιρετίζω) → **χαιρετισμός**."),
  G("-μα", "the result, the thing done", m="""
γράμμα|letter
πράγμα|thing
ποίημα|poem
μάθημα|lesson
μήνυμα|message
ζήτημα|issue, question
αίτημα|demand, request
πάθημα|misfortune; lesson learned
δέμα|parcel
φόρεμα|dress
σφάλμα|error
άνοιγμα|opening
""", note="Neuter, genitive in **-ματος**: του μηνύματος, των ζητημάτων. The base is the verb: ζητώ *ask for* → **ζήτημα**, δένω *tie* → **δέμα**, φορώ *wear* → **φόρεμα**, παθαίνω *suffer* → **πάθημα**. The proverb: *Τα παθήματα γίνονται μαθήματα*, misfortunes become lessons."),
  G("-σιμο / -ξιμο / -ψιμο / -εμα", "the act (everyday)", m="""
πλύσιμο|washing
ντύσιμο|dressing; the way someone dresses
τρέξιμο|running
γράψιμο|writing
κόψιμο|cut; cutting
ράψιμο|sewing
ψήσιμο|roasting, baking
κλείσιμο|closing
πότισμα|watering
σκούπισμα|sweeping; wiping
μαγείρεμα|cooking
""", note="The everyday noun of action, neuter, from the aorist stem: έπλυ**σ**α → **πλύσιμο**, έτρε**ξ**α → **τρέξιμο**, έκο**ψ**α → **κόψιμο**. Verbs in -εύω and -ίζω give **-εμα / -ισμα**: μαγειρεύω → **μαγείρεμα**, ποτίζω → **πότισμα**."),
  G("-ία / -εία", "state, activity, institution", m="""
ελευθερία|freedom
δημοκρατία|democracy
φιλία|friendship
ησυχία|quiet, peace
αστυνομία|police
εργασία|work; assignment
ταλαιπωρία|hardship, hassle
θεραπεία|treatment, therapy
ερμηνεία|interpretation
πορεία|course; march
εταιρεία|company
""", note="**-εία** comes from verbs in -εύω (θεραπεύω → **θεραπεία**, ερμηνεύω → **ερμηνεία**, πορεύομαι → **πορεία**). Spelling is etymological: **εταιρεία** *company* (from εταίρος *partner*) but **εταιρία** in older and some current texts; the app follows the official spelling εταιρεία."),
  G("-ότητα / -οσύνη / -ιά / -ίλα", "a quality", m="""
ποιότητα|quality
ποσότητα|quantity
ταχύτητα|speed
ικανότητα|ability
καλοσύνη|kindness
δικαιοσύνη|justice
ευγνωμοσύνη|gratitude
ομορφιά|beauty
ζεστασιά|warmth
ασχήμια|ugliness
ψαρίλα|fishy smell
σαπίλα|rot; rottenness
""", note="**-ότητα** is the neutral, learned one (ικανός → **ικανότητα**); **-οσύνη** is older and fixed in a few words (καλοσύνη, δικαιοσύνη); **-ιά** is everyday (όμορφος → **ομορφιά**, ζεστός → **ζεστασιά**); **-ίλα** names smells and tastes, usually unpleasant (ψάρι → **ψαρίλα**, ιδρώτας → **ιδρωτίλα**)."),
  G("-ισμός", "doctrine, movement, attitude (-ism)", m="""
ρατσισμός|racism
τουρισμός|tourism
ρεαλισμός|realism
ρομαντισμός|romanticism
εθνικισμός|nationalism
ατομικισμός|individualism
φεμινισμός|feminism
πατριωτισμός|patriotism
εγωισμός|selfishness
ελληνισμός|Hellenism; the Greek world
""", note="The person is in **-ιστής / -ίστρια** (ρατσιστής, ρεαλιστής, φεμινίστρια) or **-ίστας** (τουρίστας); the adjective in **-ιστικός** (ρατσιστικός, τουριστικός). **ο ελληνισμός** also means all Greeks everywhere, as in *ο απόδημος ελληνισμός* the Greek diaspora."),
 ]),

dict(id="suffix-places", part="Γ", el="Τόποι, εργαλεία, μικρά και μεγάλα", title="Suffixes for places, containers, trees, small things and big things", level="A2–B2",
 intro=[{"p": "Where something happens (-είο, -τήριο), what holds it (-θήκη, -ιέρα), which tree bears it or which blow it gives (-ιά), and how you feel about its size (-άκι, -ούλα, -άρα)."}],
 groups=[
  G("-είο", "the place for it (shops and offices)", m="""
σχολείο|school
φαρμακείο|pharmacy
ταχυδρομείο|post office
νοσοκομείο|hospital
υπουργείο|ministry
κουρείο|barber's
μουσείο|museum
βιβλιοπωλείο|bookshop
ζαχαροπλαστείο|patisserie, cake shop
πρακτορείο|agency
ψυγείο|fridge
""", note="Shops are named with **-πωλείο** *where it is sold* (βιβλιοπωλείο, ιχθυοπωλείο, αρτοπωλείο) or **-ποιείο** *where it is made* (αρτοποιείο, οινοποιείο). **ψυγείο** (ψύχω *cool*) shows the suffix naming a device as well as a place. Always stressed on **-είο**."),
  G("-τήριο", "the place or device where it is done", m="""
δικαστήριο|court
εστιατόριο|restaurant
κομμωτήριο|hairdresser's
γυμναστήριο|gym
πλυντήριο|washing machine; launderette
καθαριστήριο|dry cleaner's
φροντιστήριο|cram school; private tutorial school
ακροατήριο|audience
κοιμητήριο|cemetery
εντευκτήριο|clubroom, lounge
""", note="From the verb: δικάζω *try (a case)* → **δικαστήριο**, εστιάζω *host, feed* → **εστιατόριο**, κοιμάμαι *sleep* → **κοιμητήριο** *sleeping place*. **πλυντήριο πιάτων** is a *dishwasher*. A **γυμνάσιο** is a lower secondary school, not a gym: the gym is the **γυμναστήριο**."),
  G("-θήκη / -ιέρα", "the container for it", m="""
βιβλιοθήκη|library; bookcase
αποθήκη|storeroom; warehouse
παπουτσοθήκη|shoe cabinet
πινακοθήκη|picture gallery
ταινιοθήκη|film archive
δισκοθήκη|record collection; disco
θήκη|case, cover
αλατιέρα|salt shaker
ζαχαριέρα|sugar bowl
τσαγιέρα|teapot
καφετιέρα|coffee maker
φρουτιέρα|fruit bowl
""", note="**-θήκη** is the ancient *place where something is put* (from τίθημι, see the *Placing* family): **βιβλιοθήκη** is a library or a bookcase, never a bookshop (**βιβλιοπωλείο**). **-ιέρα** (from Italian *-iera*) makes household containers from the thing they hold."),
  G("-ιά (tree, blow)", "the tree that bears it; a blow with it", m="""
μηλιά|apple tree
κερασιά|cherry tree
λεμονιά|lemon tree
συκιά|fig tree
καρυδιά|walnut tree
ελιά|olive tree; olive; mole (on skin)
κλοτσιά|kick
μαχαιριά|stab
πετριά|hit with a stone
ματιά|glance
γροθιά|punch; fist
δαγκωματιά|bite
""", note="Two everyday meanings of the same suffix: the fruit **μήλο** grows on the **μηλιά**; a **μαχαίρι** gives a **μαχαιριά**, a **πέτρα** a **πετριά**, the **μάτι** a **ματιά**. Stressed on **-ιά**, plural **-ιές**."),
  G("-άκι / -ούλα / -ίτσα / -ούλης", "small, dear (diminutives)", m="""
σπιτάκι|little house
παιδάκι|little child
καφεδάκι|a nice little coffee
κουταλάκι|teaspoon
πιατάκι|saucer; small plate
αρκουδάκι|teddy bear
βαρκούλα|little boat
μανούλα|mummy
κουκλίτσα|little doll; sweetie
κοπελίτσα|young girl
λιγάκι|a little bit
μικρούλης|tiny, little one
""", note="**-άκι** (neuter) works on almost any noun and adds affection more than smallness: *ένα καφεδάκι;* is an invitation, not a small coffee. Some have their own meaning: **κουταλάκι** *teaspoon*, **πιατάκι** *saucer*. Feminine nouns take **-ούλα** or **-ίτσα**; adjectives **-ούλης / -ούλα / -ούλι**."),
  G("-άρα / -αράς / -όνα", "big; admired or mocked (augmentatives)", m="""
σπιταρόνα|big house, mansion
φωνάρα|powerful voice
κεφάλα|big head
ποδάρα|big foot
κοιλάρα|big belly
μουστάκα|big moustache
παιδαράς|big strapping lad
γυναικάρα|an impressive woman
αυτοκινητάρα|a great car
""", note="Augmentatives are about feeling more than size: **φωνάρα** praises a singer, **κοιλάρα** mocks a belly. The neuter noun usually turns feminine: το σπίτι → **η σπιταρόνα**, το αυτοκίνητο → **η αυτοκινητάρα**."),
 ]),

dict(id="suffix-adj", part="Γ", el="Επίθετα και επιρρήματα", title="Suffixes for adjectives and adverbs", level="A2–C1",
 intro=[{"p": "Adjective suffixes say what kind of link the adjective makes: *related to* (-ικός), *of a time or material* (-ινός / -ινος), *able to be* (-ιμος, -τός), *full of* (-ερός, -ώδης), *too much of* (-ιάρης). Adverbs come from adjectives in **-α** (everyday) or **-ως** (learned)."}],
 groups=[
  G("-ικός", "related to, of", m="""
ιστορικός|historical; historian
οικονομικός|economic; financial; cheap
πολιτικός|political; politician; civil
μουσικός|musical; musician
ηλεκτρικός|electric
θεατρικός|theatrical, of the theatre
φιλικός|friendly
πρακτικός|practical
τεχνικός|technical; technician
κοινωνικός|social; sociable
ιατρικός|medical
""", note="The most productive adjective suffix. Many -ικός adjectives double as nouns for people: **ο ιστορικός** *the historian*, **ο μουσικός** *the musician*, **ο τεχνικός** *the technician*; and the feminine names the field: **η ιστορία** is history but **η μουσική** *music*, **η πολιτική** *politics, policy*, **η τεχνική** *technique*."),
  G("-ινός / -ινος", "of a time or place / made of", m="""
πρωινός|morning
βραδινός|evening
καλοκαιρινός|summer
σημερινός|today's
αυριανός|tomorrow's
χθεσινός|yesterday's
ξύλινος|wooden
πέτρινος|stone, made of stone
γυάλινος|glass, made of glass
μάλλινος|woollen
δερμάτινος|leather
""", note="Stress tells them apart: **-ινός** (stressed) for time and place (πρωινός, σημερινός), **-ινος** (unstressed) for material (ξύλινος, πέτρινος). Precious metals take **-ένιος**: ασημένιος *silver*, χρυσός / χρυσαφένιος *golden*. **το πρωινό** as a noun is *breakfast*."),
  G("-ιμος / -σιμος", "able to be, fit for", m="""
χρήσιμος|useful
ωφέλιμος|beneficial
διαθέσιμος|available
φαγώσιμος|edible
πόσιμος|drinkable
κατοικήσιμος|habitable
αναγνώσιμος|readable, legible
μόνιμος|permanent
νόμιμος|legal, lawful
τρόφιμα|food, foodstuffs
""", note="**-σιμος** often means *can be done*: φαγώσιμος, πόσιμος (πόσιμο νερό *drinking water*). Others name a quality: **μόνιμος** *lasting* (μένω *stay*), **νόμιμος** *according to the law* (νόμος). **τα τρόφιμα** is the neuter plural used as a noun: *food(stuffs)*."),
  G("-τός", "done, can be done", m="""
γραπτός|written
αγαπητός|dear, beloved
ορατός|visible
ακουστός|audible
πιστευτός|believable
απίστευτος|unbelievable
ανεκτός|tolerable
ψητός|grilled, roast
βραστός|boiled
τηγανητός|fried
γεμιστός|stuffed
""", note="Like the English *-ed / -able*: ψήνω → **ψητός** *grilled*, πιστεύω → **πιστευτός** *believable*. With **α-** it becomes *un-…-able*: **απίστευτος**, **αόρατος** *invisible*. On a menu: **ψητά**, **βραστά**, **τηγανητά**, **γεμιστά**."),
  G("-ερός / -ώδης", "full of, causing", m="""
φοβερός|terrible; amazing
τρομερός|terrible; tremendous
δροσερός|cool, fresh
λαμπερός|bright, shiny
λυπηρός|sad (of events)
βλαβερός|harmful
λιπαρός|fatty, greasy
θορυβώδης|noisy
ογκώδης|bulky
βραχώδης|rocky
ουσιώδης|essential
""", note="**-ερός** is everyday (φόβος → **φοβερός**, δροσιά → **δροσερός**); **-ώδης** is learned and declines like ακριβής (ο θορυβώδης, του θορυβώδους, οι θορυβώδεις). In speech **φοβερός** and **τρομερός** usually praise: *Φοβερή ταινία!* What a film!"),
  G("-ιάρης", "too much of it (colloquial, critical)", m="""
γκρινιάρης|grumbler, whiner
ζηλιάρης|jealous type
φοβιτσιάρης|scaredy-cat
πεισματάρης|stubborn
παραπονιάρης|complainer
κλαψιάρης|cry-baby
αρρωστιάρης|sickly
""", note="Built on a noun: γκρίνια → **γκρινιάρης**, ζήλια → **ζηλιάρης**, πείσμα → **πεισματάρης**. Feminine **-ιάρα** (γκρινιάρα), neuter **-ιάρικο** (γκρινιάρικο παιδί)."),
  G("-α / -ως", "adverbs (everyday / learned)", m="""
καλά|well
γρήγορα|quickly
σιγά|slowly; quietly
ειλικρινά|honestly, sincerely
πρόσφατα|recently
τελικά|in the end, after all
αμέσως|immediately
ακριβώς|exactly
ευτυχώς|fortunately
σαφώς|clearly, of course
βεβαίως|certainly
απολύτως|absolutely
""", note="From adjectives in -ος the everyday adverb ends in **-α** (σίγουρος → **σίγουρα**); adjectives in -ής and many learned ones give **-ώς / -ως** (ακριβής → **ακριβώς**, σαφής → **σαφώς**). Some have both, with **-ως** more formal: βέβαια / βεβαίως, απόλυτα / απολύτως."),
 ]),

dict(id="suffix-verbs", part="Γ", el="Ρήματα από ονόματα", title="Making verbs from nouns and adjectives", level="B1–C1",
 intro=[{"p": "Greek turns nouns and adjectives into verbs with a handful of endings. Knowing them helps both ways: you can recognise **κοκκινίζω** as *go red* from κόκκινος, and you can produce **ζεσταίνω** from ζεστός. Each ending also decides the conjugation, so the drill will help your verb forms too."}],
 groups=[
  G("-ίζω", "make, become; use the thing", m="""
ασπρίζω|whiten; go grey
κοκκινίζω|blush, go red
μαυρίζω|tan; turn black
φωτίζω|light up
ελπίζω|hope
αρχίζω|begin
χαρίζω|give as a gift
σκουπίζω|wipe; sweep
χτενίζω|comb
σφυρίζω|whistle
""", note="Colours make verbs of change: άσπρος → **ασπρίζω**, κόκκινος → **κοκκινίζω**, μαύρος → **μαυρίζω**, κίτρινος → **κιτρινίζω**. Tools make verbs of use: σκούπα → **σκουπίζω**, χτένα → **χτενίζω**. Aorist in **-ισα**: κοκκίνισα, σκούπισα."),
  G("-άζω", "make, do", m="""
ετοιμάζω|prepare
αγοράζω|buy
δοκιμάζω|try; taste
αλλάζω|change
ησυχάζω|calm down
διπλασιάζω|double
σκεπάζω|cover
φωνάζω|shout; call
θαυμάζω|admire
λογαριάζω|reckon; count on
""", note="έτοιμος → **ετοιμάζω**, αγορά → **αγοράζω**, δοκιμή → **δοκιμάζω**, άλλος → **αλλάζω** *make other*, φωνή → **φωνάζω**. Aorist in **-ασα** (ετοίμασα), but a few in **-αξα** (αλλάζω → άλλαξα, φωνάζω → φώναξα)."),
  G("-ώνω", "make, cause, become", m="""
μεγαλώνω|grow up; bring up
τελειώνω|finish
ολοκληρώνω|complete
πληρώνω|pay
κλειδώνω|lock
καρφώνω|nail
ισιώνω|straighten
ψηλώνω|grow taller
ενώνω|unite, join
θυμώνω|get angry
λερώνω|dirty, stain
""", note="From adjectives: μεγάλος → **μεγαλώνω**, ολόκληρος → **ολοκληρώνω**, ίσιος → **ισιώνω**; from nouns: κλειδί → **κλειδώνω**, καρφί → **καρφώνω**, θυμός → **θυμώνω**. Aorist **-ωσα**, passive aorist **-ώθηκα** (κλειδώθηκα *I got locked in*)."),
  G("-αίνω / -ύνω", "become (more), make (more)", m="""
ζεσταίνω|warm up
παχαίνω|put on weight
γλυκαίνω|sweeten
πικραίνω|embitter
φαρδαίνω|widen
κονταίνω|shorten; get shorter
ομορφαίνω|become more beautiful
βαραίνω|get heavier; weigh on
πλαταίνω|widen
ευκολύνω|make easier
επιβαρύνω|burden; aggravate
""", note="Mostly from adjectives of size, weight, temperature and taste: ζεστός → **ζεσταίνω**, παχύς → **παχαίνω**, γλυκός → **γλυκαίνω**, φαρδύς → **φαρδαίνω**. The learned form **-ύνω** appears in εύκολος → **ευκολύνω** and βαρύς → **επιβαρύνω**. Aorist **-ανα / -ηνα** (ζέστανα, πάχυνα, γλύκανα)."),
  G("-εύω", "do as an activity", m="""
μαγειρεύω|cook
χορεύω|dance
ταξιδεύω|travel
ψαρεύω|fish
φυτεύω|plant
μαζεύω|gather, pick up
γιατρεύω|cure, heal
βασιλεύω|reign; (of the sun) set
κινδυνεύω|be in danger
ονειρεύομαι|dream
δυσκολεύω|make difficult
""", note="μάγειρας → **μαγειρεύω**, χορός → **χορεύω**, ταξίδι → **ταξιδεύω**, ψάρι → **ψαρεύω**, κίνδυνος → **κινδυνεύω**. Aorist in **-εψα** (μαγείρεψα, χόρεψα); the noun of action in **-εμα** (μαγείρεμα, χόρεμα *dancing*) or **-εία** in learned words (θεραπεύω → θεραπεία)."),
  G("-ιάζει / -ώνει", "weather and the time of day", m="""
βραδιάζει|it's getting dark
ξημερώνει|day is breaking
σουρουπώνει|dusk is falling
συννεφιάζει|it's clouding over
χειμωνιάζει|winter is setting in
καλοκαιριάζει|summer is coming
σκουριάζω|rust
μουχλιάζω|go mouldy
""", note="Impersonal verbs from nouns of time and weather: βράδυ → **βραδιάζει**, σύννεφο → **συννεφιάζει**, χειμώνας → **χειμωνιάζει**. The same **-ιάζω** turns a substance into a change of state: σκουριά → **σκουριάζω**, μούχλα → **μουχλιάζω**.",
    ex=[("Βράδιασε και δεν έχουν γυρίσει ακόμα.", "It's got dark and they haven't come back yet."), ("Συννεφιάζει, θα βρέξει.", "It's clouding over, it's going to rain.")]),
 ]),
]
