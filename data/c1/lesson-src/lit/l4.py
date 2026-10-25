import sys; sys.path.insert(0, '/tmp/claude-0/-home-user/0382d7bb-6b8c-530a-8ab0-98d2dee28f52/scratchpad/lit-src')
from util import *

_, ko = src('s01'); _, pa = src('s02'); _, ve = src('s03')
J = "\n\n".join
ko = [p.replace(" καί ", " και ") for p in ko]
K1 = J(ko[0:3])
K2 = "[…]\n\n" + fix(J(ko[5:7]), [("άρμάδα", "αρμάδα"), ("Άλλά δεν εβάσταξε!.", "Αλλά δεν εβάσταξε!")])

pa = [fix(p, [x for x in [("έβεβήλωσαν", "εβεβήλωσαν"), ("Ύποκλινόμεθα", "Υποκλινόμεθα"), ("να χάραξη", "να χαράξη"), ("Ελ-Άλαμέϊν", "Ελ Αλαμέιν"),
                           ("Ι. Ο ΑΓΩΝ ΣΥΝΕΧΙΖΕΤΑΙ\n", "**I. Ο ΑΓΩΝ ΣΥΝΕΧΙΖΕΤΑΙ**\n\n"), ("II. Η ΛΟΓΟΔΟΣΙΑ ΤΟΥ ΠΑΡΕΛΘΟΝΤΟΣ\n", "**II. Η ΛΟΓΟΔΟΣΙΑ ΤΟΥ ΠΑΡΕΛΘΟΝΤΟΣ**\n\n")] if x[0] in p]) for p in pa]
P1, P2, P3 = J(pa[0:4]), J(pa[4:10]), J(pa[10:14]) + "\n\n[…]"

vfix = [("Κανένας σοφός η άσοφος", "Κανένας σοφός ή άσοφος"), ("αναμεσα", "ανάμεσα"), ("Μα ότι κι αν πούνε", "Μα ό,τι κι αν πούνε"), ("ελληνικότητα μας", "ελληνικότητά μας"),
        ("Αυτό κάνεις δεν", "Αυτό κανείς δεν"), ("επανάστασης, πού ύμνησε", "επανάστασης, που ύμνησε"), ("σαν αυτό πού υπογράφηκε", "σαν αυτό που υπογράφηκε"),
        ("κάτω από το όποιο", "κάτω από το οποίο"), ("Μα ότι έκανε", "Μα ό,τι έκανε")]
ve = [fix(p, [x for x in vfix if x[0] in p]) for p in ve]
def head(p): return "**" + p + "**" if len(p.split()) <= 4 else p
ve = [head(p) for p in ve]
V1, V2, V3 = J(ve[0:9]), J(ve[9:13]), J(ve[13:18]) + "\n\n[…]"
for x in vfix: assert x[0] not in V1 + V2 + V3

blocks = [
 {"type": "text", "text":
  "Three speeches about Greek freedom, three registers. **Kolokotronis** (1838), the old hero of 1821, speaks to Athenian schoolboys on the Pnyx in the plain, concrete Greek of a man who learned to read late, written down by a listener with a light coat of learned spelling (*εις, οπού, ηξεύρω, είμεθα*). **Georgios Papandreou** (18 October 1944), returning with the government of national unity on the day of liberation, addresses the crowd in Syntagma in ceremonial **katharevousa**: tricolons, abstractions, capital-letter nouns (*Πατρίς, Ελευθερία, Έθνος*). Eleven days later **Aris Velouchiotis**, the ELAS guerrilla leader, speaks in Lamia in blunt **demotic** with proverbs, sarcasm and a fairy-tale opening, and turns the national story into a class story.\n\n"
  "Read them for **rhetoric** as much as content. Who is the audience? Who is 'we'? What is never named (in these excerpts Papandreou never says *Germans*, Velouchiotis never mentions the *Allies*)? Notice that the demotic speaker still reaches for learned vocabulary when he wants weight (*δεν επιδιώκω ν' αποσπάσω επαίνους για τη ρητορική μου δεινότητα*): that mixture is modern standard Greek.\n\n"
  "*Πηγές: Θεόδωρος Κολοκοτρώνης, Ομιλία στην Πνύκα (1838, public domain); Γεώργιος Παπανδρέου, Ο λόγος της απελευθερώσεως (1944; text from Greek Wikisource, personal study use); Άρης Βελουχιώτης, Λόγος στη Λαμία (1944, public domain). Excerpts; polytonic sources given in monotonic, obvious typos corrected.*"},
 {"type": "reading", "title": "Κολοκοτρώνης (1): «Παιδιά μου!»", "text": K1,
  "en": "My children!\n\n"
        "On this spot where I stand today, wise men walked and addressed the people in the old days, men with whom I am not worthy to be compared, nor even to follow in their footsteps. I wished to see you, my children, in the great glory of our forefathers, and I have come to tell you what I myself observed in the time of the struggle, before it and after it, so that from these things we may draw conclusions for your future happiness too, although God alone knows what is to come. As for the ancient Greeks, what knowledge they had, what glory and honour they enjoyed among the other nations of their time, what heroes, generals and statesmen they had: about all this your teachers and our educated men tell you every day. I am not up to it. I tell you only that they were wise, and that it was from here that the other nations took and borrowed their wisdom.\n\n"
        "In the land we live in lived the ancient Greeks, from whom we too descend and from whom we took this name. They differed from us in religion, because they worshipped stones and wood. Then, after Christ came into the world, all the peoples believed in His Gospel and stopped worshipping idols. He did not take with Him wise men or men of means, but simple people, peasants and fishermen, and with the help of the Holy Spirit they learned all the languages of the world; and although they met opposition wherever they went, and kings and tyrants persecuted them, no one could do anything to them. They established the faith.",
  "gloss": {"οπού": "οπού — where, that (= που)", "εδημηγορούσαν": "δημηγορώ — to address the people", "ίχνη": "ίχνος — footprint, trace", "προπατόρων": "προπάτορας — forefather", "ιδώ": "δω — see (old form of subj.)", "ειπώ": "πω — tell (old form of subj.)", "επαρατήρησα": "παρατηρώ — I observed (old augment)", "συμπερασμούς": "συμπερασμός — conclusion (= συμπέρασμα)", "μέλλουσαν": "μέλλων — future (fem. acc.)", "μολονότι": "μολονότι — although", "ηξεύρει": "ξέρει — knows (old form)", "έχαιραν": "χαίρω — to enjoy (+ acc.: τιμή, εκτίμηση)", "πεπαιδευμένοι": "πεπαιδευμένος — educated (learned perfect participle)", "αρκετός": "αρκετός — adequate, up to the task", "εδανείσθησαν": "δανείζομαι — they borrowed (= δανείστηκαν)", "καταγόμεθα": "κατάγομαι — we descend from (= καταγόμαστε)", "είδωλα": "είδωλο — idol", "προκομμένους": "προκομμένος — capable, successful", "εναντιότητες": "εναντιότητα — opposition, adversity", "κατέτρεχαν": "κατατρέχω — to persecute"},
  "questions": [
   q("Πώς παρουσιάζει ο Κολοκοτρώνης τον εαυτό του απέναντι στους αρχαίους;", "Με μετριοφροσύνη: λέει ότι δεν είναι άξιος να συγκριθεί μαζί τους", ["Ως ισάξιο διάδοχο του Περικλή", "Ως δάσκαλο της αρχαίας ιστορίας", "Ως αντίπαλο της αρχαίας θρησκείας"], "«δεν είμαι άξιος να συγκριθώ και ούτε να φθάσω τα ίχνη των»."),
   q("Γιατί αφήνει στους δασκάλους να μιλήσουν για τους αρχαίους;", "Δεν έχει τη μόρφωση· θα μιλήσει από τη δική του πείρα", ["Επειδή δεν τον ενδιαφέρουν οι αρχαίοι", "Επειδή οι δάσκαλοι του το απαγόρευσαν", "Επειδή δεν έχει χρόνο"], "«Εγώ δεν είμαι αρκετός»: his authority is experience (ο ίδιος επαρατήρησα)."),
  ]},
 {"type": "reading", "title": "Κολοκοτρώνης (2): «ως μία βροχή»", "text": K2,
  "en": "[…]\n\n"
        "When we decided to make the Revolution, we did not stop to think how few we were, or that we had no weapons, or that the Turks held the fortresses and the towns; nor did any sensible man tell us 'where do you think you're going, to fight here with grain boats?'; but like a rain the desire for our freedom fell on all of us, and all of us, our clergy and the notables and the captains and the educated and the merchants, small and great, all of us agreed on this aim and we made the Revolution.\n\n"
        "In the first year of the Revolution we had great concord and we all ran together as one. One man went to war, his brother brought wood, his wife kneaded bread, his child carried bread and ammunition to the camp; and if that concord had lasted another two years, we would have conquered Thessaly and Macedonia too, and perhaps we would have reached as far as Constantinople. We frightened the Turks so much that they heard 'Greek' and fled a thousand miles. A hundred Greeks put five thousand to flight, and one ship a whole fleet. But it did not last!",
  "gloss": {"εσυλλογισθήκαμε": "συλλογίζομαι — we considered (= σκεφτήκαμε)", "είμεθα": "είμαστε — we were (old form)", "άρματα": "άρματα — weapons (old popular)", "εβαστούσαν": "βαστώ — to hold", "φρόνιμος": "φρόνιμος — sensible, prudent", "σιταροκάραβα": "σιταροκάραβο — grain ship", "βατσέλα": "βατσέλο — (Italian vascello) vessel", "προεστοί": "προεστός — notable, local elder", "καπεταναίοι": "καπετάνιος — (here) guerrilla captain", "εσυμφωνήσαμε": "συμφωνώ — we agreed (old augment)", "ομόνοια": "ομόνοια — concord, unity", "σύμφωνοι": "σύμφωνος — in agreement, as one", "εζύμωνε": "ζυμώνω — to knead", "μπαρουτόβολα": "μπαρουτόβολο — cartridge, ammunition", "ηθέλαμε": "ηθέλαμε + inf. — we would have (old conditional)", "κυριεύσει": "κυριεύω — to conquer", "αρμάδα": "αρμάδα — fleet, armada", "εβάσταξε": "βαστώ — it lasted (= βάσταξε, κράτησε)"},
  "questions": [
   q("Κατά τον Κολοκοτρώνη, τι θα είχε γίνει αν κρατούσε η ομόνοια;", "Θα είχαν ελευθερώσει Θεσσαλία και Μακεδονία, ίσως και την Πόλη", ["Δεν θα χρειαζόταν πόλεμος", "Θα είχαν συμμαχήσει με τους Τούρκους", "Θα είχε έρθει νωρίτερα ο βασιλιάς"], "«ηθέλαμε κυριεύσει και την Θεσσαλία και την Μακεδονία…»."),
   q("Τι δείχνει η εικόνα «ως μία βροχή έπεσε εις όλους μας η επιθυμία»;", "Ότι η επιθυμία για ελευθερία ήταν αυθόρμητη και καθολική", ["Ότι η Επανάσταση άρχισε τον χειμώνα", "Ότι οι Έλληνες ήταν απροετοίμαστοι για τον καιρό", "Ότι μόνο οι αγρότες συμμετείχαν"], "Rain falls on everyone at once: clergy, notables, captains, merchants."),
   q("Ποιο είναι το σιωπηρό δίδαγμα της τελευταίας φράσης «Αλλά δεν εβάσταξε!»;", "Η διχόνοια κατέστρεψε όσα πέτυχε η ομόνοια", ["Οι Τούρκοι ήταν πολύ δυνατότεροι", "Τα καράβια δεν άντεξαν στη θάλασσα", "Η Επανάσταση ήταν λάθος από την αρχή"], "The speech's lesson to the youth: concord wins, discord loses."),
  ]},
 {"type": "reading", "title": "Παπανδρέου (1): «Ασπαζόμεθα την ιεράν γην»", "text": P1,
  "en": "We kiss the sacred soil of the Free Fatherland… The Barbarians, having desecrated, burned and laid waste for three and a half years, pressed now by the Allied victory and by our national resistance, are turning to flight. And the blue-and-white flies alone on the Acropolis…\n\n"
        "From the depths of History the Greek centuries celebrate the return of Freedom to its ancient homeland. And they crown our Generation. For our whole people has been a fighter for Freedom. There is surely no other example in occupied Europe of such universal resistance and such unshakeable optimism about final Victory.\n\n"
        "But to You above all, people of Athens, people of the region of the Capital, belongs the nation's praise. Here beat the indomitable heart of Greece. Here those who ran risks and suffered oppression were happy; [unhappy] those who had no chance to run risks…\n\n"
        "And to You, young men and young women, we express our admiration. You had made a daily habit of defying the enemy and scorning death. Before the muzzles of his machine guns you cheered for Greece!",
  "gloss": {"Ασπαζόμεθα": "ασπάζομαι — we kiss (reverently); also 'embrace (a view)'", "εβεβήλωσαν": "βεβηλώνω — to desecrate", "επυρπόλησαν": "πυρπολώ — to set on fire", "εδήωσαν": "δηώ — to ravage, lay waste (ancient)", "ήμισυ": "ήμισυ — half (τρία και ήμισυ = τρεισήμισι)", "πιεζόμενοι": "πιέζομαι — being pressed (participle)", "τρέπονται": "τρέπομαι — to turn (εις φυγήν = to flight)", "Κυανόλευκος": "η Κυανόλευκος — the blue-and-white (flag)", "κυματίζει": "κυματίζω — to fly, wave (flag)", "επάνοδον": "επάνοδος — return", "Γενεάν": "γενιά — generation", "καθολικής": "καθολικός — universal, general", "ακλονήτου": "ακλόνητος — unshakeable", "επάλλετο": "πάλλομαι — was beating, throbbing", "αδάμαστος": "αδάμαστος — indomitable", "επροκινδύνευαν": "προκινδυνεύω — to run risks (for others)", "κατεθλίβοντο": "καταθλίβομαι — to be crushed, oppressed", "πρόκλησιν": "πρόκληση — defiance, provocation", "στόμια": "στόμιο — muzzle (of a gun)", "εζητωκραυγάζατε": "ζητωκραυγάζω — to cheer"},
  "questions": [
   q("Ποιους επαινεί ιδιαίτερα ο ομιλητής;", "Τον λαό της Αθήνας και τους νέους", ["Τους στρατιωτικούς της Μέσης Ανατολής", "Τους πολιτικούς της κυβέρνησης", "Τους Μεγάλους Συμμάχους"], "«προς Σε, περισσότερον, λαέ των Αθηνών» and «προς Σας, Νέοι και Νέαι»."),
   q("Πώς ονομάζει ο ομιλητής τους κατακτητές;", "«Οι Βάρβαροι», χωρίς να τους κατονομάσει", ["«Οι Γερμανοί και οι Ιταλοί»", "«Οι φασίστες»", "«Ο εχθρός του λαού»"], "Ceremonial abstraction: never Germans, always Barbarians."),
  ]},
 {"type": "reading", "title": "Παπανδρέου (2): θύματα, ομογενείς, σύμμαχοι", "text": P2,
  "en": "The whole Greek People has proved worthy of the Fatherland. With the passing of time, the legend of universal resistance will be added to the glorious epic of Albania…\n\n"
        "Countless, however, were the victims of the Barbarians… We bow reverently before the named and nameless martyrs of Freedom. In the Nation's gratitude their memory will be eternal…\n\n"
        "And outside the enslaved Fatherland, on the common Allied front of Freedom, the children of Greece continued the struggle. Both our Navy and our Merchant Marine have been fighting for four years, making the harshest sacrifices and performing heroic feats.\n\n"
        "And our incomparable Air Force is in the front line and is regarded by the Allied command as a model.\n\n"
        "And our army of the Middle East gave us El Alamein, the Sacred Band and, the day before yesterday, the glory of Rimini. The free Fatherland awaits with deep emotion her children far from home, who today, with such irresistible longing, turn their moist eyes impatiently towards our shores…\n\n"
        "But on the day of this great national joy we wish to address a grateful greeting to our Great Allies too. They were steadfast and warm supporters throughout the common struggle. In days of trial and in days of joy they were at our side. When the flood of the Barbarians was covering our Fatherland and the soldiers of Great Britain were leaving Greece, they promised us they would return as liberators. And today they are keeping their word. We express to them the deepest gratitude of the Nation.",
  "gloss": {"καταστή": "καθίσταμαι — to become (έχει καταστή = has become)", "περίλαμπρον": "περίλαμπρος — glorious", "έπος": "έπος — epic", "προστεθή": "προστίθεμαι — to be added (= προστεθεί)", "Άπειρα": "άπειρος — countless, infinite", "Υποκλινόμεθα": "υποκλίνομαι — we bow (= υποκλινόμαστε)", "ευλαβώς": "ευλαβικά — reverently", "ενώπιον": "ενώπιον — before, in front of (+ gen.)", "αιωνία": "αιώνιος — eternal (katharevousa fem.)", "δούλης": "δούλος — enslaved (fem. gen.)", "εξηκολούθησαν": "εξακολουθώ — they continued (internal augment)", "επιτελούν": "επιτελώ — to perform, accomplish", "κατορθώματα": "κατόρθωμα — feat, achievement", "απαράμιλλος": "απαράμιλλος — incomparable", "ακαταμάχητον": "ακαταμάχητος — irresistible", "παραστάται": "παραστάτης — supporter, one who stands by (nom. pl.)", "δοκιμασίας": "δοκιμασία — trial, ordeal", "κατακλυσμός": "κατακλυσμός — flood, deluge", "υπεσχέθησαν": "υπόσχομαι — they promised (= υποσχέθηκαν)", "ελευθερωταί": "ελευθερωτής — liberator (katharevousa nom. pl.)"},
  "questions": [
   q("Ποια υπόσχεση, κατά τον ομιλητή, τηρήθηκε;", "Ότι οι Βρετανοί θα επέστρεφαν ως ελευθερωτές", ["Ότι η Ελλάδα θα αποκτούσε νέα εδάφη", "Ότι ο στρατός της Μέσης Ανατολής θα γύριζε αμέσως", "Ότι η κυβέρνηση θα παραιτούνταν"], "«μας υπεσχέθησαν ότι θα επανέλθουν ελευθερωταί. Και σήμερον τηρούν τον λόγον των»."),
   q("Ποια ρητορική τεχνική κυριαρχεί στις παραγράφους «Και το Πολεμικόν… Και η απαράμιλλος… Και ο στρατός…»;", "Πολυσύνδετο: συνεχής επανάληψη του «Και» για μεγαλοπρέπεια", ["Ρητορική ερώτηση", "Ειρωνεία", "Λαϊκή παροιμία"], "Polysyndeton gives a liturgical, accumulating rhythm."),
  ]},
 {"type": "reading", "title": "Παπανδρέου (3): ο αγών συνεχίζεται", "text": P3,
  "en": "I. THE STRUGGLE CONTINUES\n\n"
        "But the struggle continues. The Barbarians are still in Greece. And the front of Freedom is fighting its last battle against Nazism. In this final phase of the struggle of Freedom against barbarism, in which even yesterday's defeated are trying to slip in, posing as 'co-belligerents', Greece, the glorious protagonist, cannot be absent. Until the final victory we shall stand by our Great Allies.\n\n"
        "II. ACCOUNTING FOR THE PAST\n\n"
        "The Government, returning to the Free Fatherland, must give an account of the past and chart the course of the future.\n\n"
        "Looking back at the past is a thankless task today. We confine ourselves to noting that we inherited ruins in the Middle East and armed division in the enslaved Fatherland… In the bitter words of the leader of Great Britain, 'the glory of Greece had been tarnished'.\n\n"
        "And today the Government, standing before the Greek People, has the right to proclaim that Greece's standing among the Allies has also regained its old glory. And our armed forces, throbbing with faith in the Fatherland, are covered in glory daily. And today's gathering of the whole people proves that we have overcome civil war and that the idea of National Unity has prevailed. But the future matters more…\n\n[…]",
  "gloss": {"αγών": "αγώνας — struggle (katharevousa nom.)", "παρεμβληθούν": "παρεμβάλλομαι — to slip in, insert oneself", "παριστάνοντες": "παριστάνω — posing as (participle)", "συνεμπολέμους": "συνεμπόλεμος — co-belligerent", "δύναται": "δύναμαι — can (= μπορεί)", "απουσιάση": "απουσιάζω — to be absent", "συμπαραστάται": "συμπαραστάτης — supporter, ally", "ΛΟΓΟΔΟΣΙΑ": "λογοδοσία — accountability, rendering account", "επανερχόμενη": "επανέρχομαι — returning", "οφείλει": "οφείλω — to be obliged to", "λογοδοτήση": "λογοδοτώ — to give account", "Αχάριστος": "αχάριστος — thankless", "αναδρομή": "αναδρομή — looking back, retrospect", "Αρκούμεθα": "αρκούμαι — we confine ourselves (= αρκούμαστε)", "διαπίστωσιν": "διαπίστωση — finding, observation", "εκληρονομήσαμεν": "κληρονομώ — we inherited", "αμαυρωθή": "αμαυρώνομαι — to be tarnished", "επανεύρει": "επανευρίσκω — to regain, rediscover", "πάνδημος": "πάνδημος — of the whole people, mass", "υπερνικήσει": "υπερνικώ — to overcome"},
  "questions": [
   q("Ποιο μήνυμα θέλει να περάσει για την εσωτερική κατάσταση;", "Ότι ο εμφύλιος ξεπεράστηκε και επικράτησε η εθνική ενότητα", ["Ότι ο εμφύλιος μόλις αρχίζει", "Ότι η κυβέρνηση θα παραιτηθεί", "Ότι ο λαός πρέπει να οπλιστεί"], "«έχομεν υπερνικήσει τον εμφύλιον πόλεμον… έχει επιβληθή η ιδέα της Εθνικής Ενώσεως» (six weeks before the Dekemvriana)."),
   q("Ποιοι είναι οι «χθεσινοί ηττημένοι» που «παριστάνουν τους συνεμπολέμους»;", "Χώρες που πολέμησαν με τον Άξονα και τώρα αλλάζουν στρατόπεδο", ["Οι Έλληνες αντάρτες", "Οι Βρετανοί στρατιώτες", "Οι Έλληνες της Μέσης Ανατολής"], "Italy and Bulgaria switched sides in 1943–44 and claimed co-belligerent status."),
  ]},
 {"type": "reading", "title": "Βελουχιώτης (1): «Θ' αρχίσω σαν τα παραμύθια»", "text": V1,
  "en": "Why I fought.\n\n"
        "Brothers and sisters, men and women of Greece, of Lamia and its region!\n\n"
        "On behalf of the General Headquarters of ELAS, I bring you our warmest greetings.\n\n"
        "As you see, I'm supposed 'to make a speech'. But this speech of mine will be nothing like the speeches you have known until today. I'm not going to promise you that I'll build you bridges or rivers, the way the old party bosses used to promise they would bring you. Nor am I going to promise you the moon. I'm not out to win praise for my oratorical skill. I simply want you to listen to what I'm going to tell you. Pay attention. I'll begin like the fairy tales:\n\n"
        "The immortal Greek race.\n\n"
        "Once upon a time this corner of the earth we stand on, which is called Greece, was glorious and happy and had a civilisation which for 2,500 years has gone on enduring and being admired by the whole world. Nobody, wise or unwise, can to this day write a single word without referring to the works left by the creators of that civilisation, which is called ancient Greek civilisation.\n\n"
        "Once, then, our country was glorious, but later they enslaved it and it lost that old glory of its own. But after a good many years our country rose to its feet and after hard struggles against slavery it was free again.\n\n"
        "In the age of slavery it went through hard, black years, and many 'clever' people, among them a certain Fallmerayer, claimed that the Greek race had died out and that it had mixed with other races that have nothing in common with the ancient Greek race.\n\n"
        "But whatever they say, it is worthless. We proved our Greekness. The fact is that our country rose up and became free once again.",
  "gloss": {"Στρατηγείου": "Στρατηγείο — (military) headquarters", "χαιρετισμούς": "χαιρετισμός — greeting", "υποσχόντουσαν": "υπόσχομαι — they used to promise (popular = υπόσχονταν)", "κομματάρχες": "κομματάρχης — local party boss", "τάξω": "τάζω — to promise", "λαγούς": "τάζω λαγούς με πετραχήλια — to promise the moon", "πετραχήλια": "πετραχήλι — priest's stole", "επιδιώκω": "επιδιώκω — to seek, aim at", "αποσπάσω": "αποσπώ — to win, extract (praise)", "επαίνους": "έπαινος — praise", "δεινότητα": "δεινότητα — skill, prowess", "φυλή": "φυλή — race, nation (period usage)", "δοξασμένη": "δοξασμένος — glorious", "υποδούλωσαν": "υποδουλώνω — to enslave", "λευτερώθηκε": "λευτερώνομαι — to be freed (popular = ελευθερώθηκε)", "ισχυρίστηκαν": "ισχυρίζομαι — to claim", "διασταυρώθηκε": "διασταυρώνομαι — to interbreed, cross", "ελληνικότητά": "ελληνικότητα — Greekness", "ξεσηκώθηκε": "ξεσηκώνομαι — to rise up", "ξαναγένηκε": "ξαναγίνομαι — to become again (popular aorist)"},
  "questions": [
   q("Πώς προσπαθεί ο ομιλητής να κερδίσει το ακροατήριο στην αρχή;", "Λέει ότι δεν θα κάνει ψεύτικες υποσχέσεις όπως οι παλιοί πολιτικοί", ["Υπόσχεται γέφυρες και δρόμους", "Επαινεί τη μόρφωση του ακροατηρίου", "Διαβάζει ένα επίσημο κείμενο του Στρατηγείου"], "Anti-rhetoric as rhetoric: «Δεν πρόκειται να σας υποσχεθώ…»."),
   q("Τι σημαίνει «θα σας τάξω λαγούς με πετραχήλια»;", "Θα σας δώσω απίθανες, ψεύτικες υποσχέσεις", ["Θα σας φέρω κυνήγι για το τραπέζι", "Θα σας μιλήσω για θρησκεία", "Θα σας διηγηθώ ένα αστείο"], "A hare wearing a priest's stole: something impossible."),
   q("Σε ποιον απαντά για την καταγωγή των νέων Ελλήνων;", "Στον Φαλμεράγιερ", ["Στον Καποδίστρια", "Στους κομματάρχες", "Στους αρχαίους συγγραφείς"], "«κάποιος Φαλμεράγιερ, ισχυρίστηκαν πως η ελληνική φυλή έσβησε»."),
  ]},
 {"type": "reading", "title": "Βελουχιώτης (2): «Η αντίδραση ουρλιάζει»", "text": V2,
  "en": "Nobody wanted this. Neither the foreign kings nor the local kotzabasides. The foreigners did not want it because, frightened by the French Revolution, they crushed every uprising and for that purpose set up the Holy Alliance among themselves. The local kotzabasides, because they were in cahoots with the Turks and squeezed the people dry.\n\n"
        "Reaction howls.\n\n"
        "But the Greek people would not be this people, the people, that is, of the land of freedom and civilisation, but a people of the jungle, if it had not brought forth from its own guts those leaders who would lead it to its freedom. As you see, then, everyone, foreigners and locals, fought to stop the people from rising up and winning its freedom.\n\n"
        "In the years of slavery the struggles never stopped. Small or large. Armed or not. And then out of this people sprang the great bard of the revolution, who in his songs sang the idea of the nation's uprising, the forerunner of the Philiki Etaireia: Rigas. Reaction killed him before he could carry his principles through. But the seed he sowed soon sprouted.",
  "gloss": {"ντόπιοι": "ντόπιος — local", "κοτζαμπάσηδες": "κοτζαμπάσης — Ottoman-era Greek notable", "εξεγέρσεις": "εξέγερση — uprising", "Ιερή": "Ιερή Συμμαχία — the Holy Alliance (1815)", "είχανε": "τα έχω καλά με — to be on good terms with", "ξεζουμίζανε": "ξεζουμίζω — to squeeze dry, exploit", "αντίδραση": "αντίδραση — (political) reaction, reactionaries", "ουρλιάζει": "ουρλιάζω — to howl", "ζούγκλας": "ζούγκλα — jungle", "σπλάχνα": "σπλάχνα — guts, bowels; one's own flesh", "πάλεψαν": "παλεύω — to fight, struggle", "αποχτήσει": "αποκτώ — to acquire (popular -χτ-)", "ξεπήδησε": "ξεπηδώ — to spring up", "βάρδος": "βάρδος — bard", "ύμνησε": "υμνώ — to sing the praises of", "πρόδρομος": "πρόδρομος — forerunner", "προλάβει": "προλαβαίνω — to manage in time", "πέρας": "φέρνω σε πέρας — to carry through, complete", "βλάστησε": "βλασταίνω — to sprout"},
  "questions": [
   q("Γιατί, κατά τον Βελουχιώτη, οι κοτζαμπάσηδες δεν ήθελαν την επανάσταση;", "Τα είχαν καλά με τους Τούρκους και εκμεταλλεύονταν τον λαό", ["Φοβούνταν τη Γαλλική Επανάσταση", "Ήταν πιστοί χριστιανοί", "Δεν είχαν όπλα"], "«τα είχανε καλά με τους Τούρκους και ξεζουμίζανε το λαό»."),
   q("Ποιο είναι το κοινό σημείο ξένων και ντόπιων «ισχυρών» στον λόγο του;", "Φοβούνταν τον ξεσηκωμό του λαού", ["Αγαπούσαν τον αρχαίο πολιτισμό", "Υποστήριζαν τον Ρήγα", "Ήθελαν μια ενωμένη Ευρώπη"], "«όλοι - ξένοι και ντόπιοι - πάλεψαν για να μην ξεσηκωθεί ο λαός»: the class reading of 1821."),
  ]},
 {"type": "reading", "title": "Βελουχιώτης (3): Καποδίστριας και Παπαφλέσσας", "text": V3,
  "en": "Soon the Philiki Etaireia was founded and took in thousands of Greeks.\n\n"
        "Let reaction howl. Let it sign shameful papers, like the one signed at the Congress of Vienna in 1815, under which the great Ioannis Kapodistrias too put his signature, and which stipulated that not only would no national liberation movement in Greece be favoured or permitted, but it would be drowned in blood if it broke out.\n\n"
        "Ioannis Kapodistrias, whom they present to us in the schools as great and mighty, with busts and portraits, is the first destroyer of Greece. But whatever he did, he did not do it as Kapodistrias, but as the representative of the whole of Greek reaction. So let it howl, local reaction together with international reaction. And let them sign shameful papers.\n\n"
        "The people moves forward.\n\n"
        "Nothing was able to hold back the flame for freedom that burned in the hearts of our people. So, in 1821, after toil and sacrifices and thanks to the enthusiasm and the fire of Papaflessas, who used every means, even lies, in proclaiming the uprising, the Morea rose first. From here, from the Morea, the revolution of 1821 began.\n\n[…]",
  "gloss": {"αγκάλιασε": "αγκαλιάζω — to embrace, take in", "άτιμα": "άτιμος — shameful, dishonourable", "διάσκεψη": "διάσκεψη — conference, congress", "πολύς": "ο πολύς — the great (ironic)", "διαλάμβανε": "διαλαμβάνω — to stipulate, contain", "ευνοηθεί": "ευνοούμαι — to be favoured", "επιτραπεί": "επιτρέπομαι — to be permitted", "εθνικοαπελευθερωτικό": "εθνικοαπελευθερωτικός — national-liberation (adj.)", "πνιγεί": "πνίγομαι — to be drowned", "ξεσπάσει": "ξεσπώ — to break out", "τρανό": "τρανός — great, mighty (popular)", "προτομές": "προτομή — bust (sculpture)", "καταστροφέας": "καταστροφέας — destroyer", "εκπρόσωπος": "εκπρόσωπος — representative", "συγκρατήσει": "συγκρατώ — to hold back", "θυσίες": "θυσία — sacrifice", "ψευτιά": "ψευτιά — lie, falsehood", "κηρύσσοντας": "κηρύσσω — proclaiming"},
  "questions": [
   q("Πώς παρουσιάζει τον Καποδίστρια;", "Ως εκπρόσωπο της αντίδρασης, αντίθετα με την εικόνα των σχολικών βιβλίων", ["Ως τον μεγαλύτερο ήρωα του 1821", "Ως ουδέτερο διπλωμάτη", "Ως φίλο του Ρήγα"], "«μας τον παρουσιάζουν στα σχολειά σαν μεγάλο και τρανό… είναι ο πρώτος καταστροφέας»: a deliberate counter-history."),
   q("Τι αποκαλύπτει για τη ρητορική του ο έπαινος του Παπαφλέσσα που «χρησιμοποίησε… ακόμα και την ψευτιά»;", "Ότι ο σκοπός της λευτεριάς δικαιολογεί κάθε μέσο", ["Ότι κατηγορεί τον Παπαφλέσσα", "Ότι αμφισβητεί την επανάσταση του 1821", "Ότι προτιμά την ειλικρίνεια από τη νίκη"], "Means justified by the end: a revolutionary's ethic."),
  ]},
 {"type": "table", "title": "The same idea in two registers",
  "head": ["Katharevousa (Papandreou / Kolokotronis)", "Demotic equivalent", "English"],
  "rows": [
   ["Ασπαζόμεθα την ιεράν γην", "Φιλάμε το ιερό χώμα", "we kiss the sacred soil"],
   ["επί τρία και ήμισυ έτη", "τρεισήμισι χρόνια", "for three and a half years"],
   ["τρέπονται εις φυγήν", "το βάζουν στα πόδια", "they turn to flight"],
   ["εβεβήλωσαν, επυρπόλησαν και εδήωσαν", "μόλυναν, έκαψαν και ρήμαξαν", "desecrated, burned and laid waste"],
   ["Η Κυανόλευκος κυματίζει", "Η γαλανόλευκη ανεμίζει", "the blue-and-white flies"],
   ["ο αγών συνεχίζεται", "ο αγώνας συνεχίζεται", "the struggle goes on"],
   ["η Ελλάς δεν δύναται ν' απουσιάση", "η Ελλάδα δεν μπορεί να λείπει", "Greece cannot be absent"],
   ["εκφράζομεν τον θαυμασμόν μας", "σας θαυμάζουμε", "we express our admiration"],
   ["Υποκλινόμεθα ευλαβώς ενώπιον των μαρτύρων", "Σκύβουμε το κεφάλι μπροστά στους νεκρούς μας", "we bow reverently before the martyrs"],
   ["υπήρξαν παραστάται μας", "μας στάθηκαν", "they stood by us"],
   ["μας υπεσχέθησαν ότι θα επανέλθουν", "μας υποσχέθηκαν πως θα ξαναγυρίσουν", "they promised to return"],
   ["τηρούν τον λόγον των", "κρατάνε τον λόγο τους", "they keep their word"],
   ["Αρκούμεθα εις την διαπίστωσιν ότι…", "Λέμε μόνο ότι…", "we confine ourselves to noting that…"],
   ["εκληρονομήσαμεν ερείπια", "βρήκαμε χαλάσματα", "we inherited ruins"],
   ["η πάνδημος συγκέντρωσις", "μαζεύτηκε όλος ο κόσμος", "the mass gathering of the whole people"],
   ["μέχρι της τελικής νίκης", "ως την τελική νίκη", "until final victory"],
   ["εδημηγορούσαν (Kolokotronis)", "έβγαζαν λόγους (Velouchiotis: να βγάλω λόγο)", "they made speeches"],
   ["οι πεπαιδευμένοι", "οι μορφωμένοι, οι γραμματισμένοι", "the educated"],
   ["εσυλλογισθήκαμε, είμεθα", "σκεφτήκαμε, είμαστε", "we considered, we were"],
   ["ηθέλαμε κυριεύσει", "θα είχαμε κυριέψει", "we would have conquered"],
  ]},
 {"type": "table", "title": "Rhetorical tools to name in Greek",
  "head": ["Device (Greek term)", "Example here", "Effect"],
  "rows": [
   ["**τρικώλο** (tricolon)", "εβεβήλωσαν, επυρπόλησαν και εδήωσαν", "rhythm, completeness"],
   ["**πολυσύνδετο** (polysyndeton)", "Και το Πολεμικόν… Και η Αεροπορία… Και ο στρατός…", "solemn accumulation"],
   ["**αναφορά** (anaphora)", "Εδώ επάλλετο… Εδώ ήσαν ευτυχείς…", "emphasis on place"],
   ["**αποστροφή** (apostrophe)", "λαέ των Αθηνών / Αδέλφια / Παιδιά μου!", "direct address, intimacy or grandeur"],
   ["**προσωποποίηση** (personification)", "οι Ελληνικοί αιώνες πανηγυρίζουν", "history itself approves"],
   ["**ευφημισμός / αφαίρεση**", "οι Βάρβαροι (never 'Germans')", "timeless, ceremonial tone"],
   ["**αντι-ρητορική**", "Δεν πρόκειται να σας υποσχεθώ…", "builds trust by rejecting politicians' talk"],
   ["**παροιμία / ιδιωματισμός**", "λαγούς με πετραχήλια, η χώρα σηκώθηκε στο πόδι", "folk authority, humour"],
   ["**ειρωνεία με εισαγωγικά**", "πολλοί «έξυπνοι», ο πολύς Καποδίστριας", "mockery of opponents"],
   ["**ονοματικές μικροπροτάσεις** (headline sentences)", "Η αντίδραση ουρλιάζει. Ο λαός προχωρεί.", "slogan-like punch"],
   ["**μετριοφροσύνη** (modesty topos)", "Εγώ δεν είμαι αρκετός.", "authority through humility"],
   ["**συγκεκριμένη εικόνα**", "ο αδελφός του έφερνε ξύλα, η γυναίκα του εζύμωνε", "makes 'unity' visible"],
  ]},
 {"type": "culture", "title": "Οκτώβριος 1944: δύο λόγοι, δύο Ελλάδες",
  "text": "The Germans left Athens on **12 October 1944**. On **18 October** Georgios Papandreou, prime minister of the government of national unity formed in the Middle East (the 'Lebanon' agreement he alludes to), arrived with British troops and spoke from a balcony in Syntagma. On **29 October**, the day after the anniversary of the 1940 *Όχι*, Aris Velouchiotis, legendary commander of ELAS (the communist-led resistance army), spoke in Lamia. The 'national unity' Papandreou proclaimed collapsed within weeks: the **Δεκεμβριανά** (December 1944) set ELAS against British and government forces in Athens; the Varkiza agreement (February 1945) disarmed ELAS; Velouchiotis rejected it, was disowned by his party and died in June 1945, and the full **Εμφύλιος** (1946–49) followed.\n\n"
          "The register split mapped onto politics: the state, the Right and the Church wrote katharevousa; the Left and the resistance used demotic, which is why demotic was smeared as 'communist' for decades. The irony is that Papandreou himself, as education minister in 1930 and prime minister in 1964, was one of demotic's main champions in schools; on the balcony, though, the occasion demanded katharevousa.\n\n"
          "**Kolokotronis' Pnyx speech** (1838) is still read in Greek schools: the old general, by then pardoned after a death sentence under the Bavarian regency, tells schoolboys that the Revolution was won by **ομόνοια** and nearly lost by **διχόνοια**. Velouchiotis' attack on **Kapodistrias** is partisan history: Kapodistrias served the Russian tsar at Vienna and declined to lead the Philiki Etaireia, but he became Greece's first governor in 1828 and most Greeks remember him as a founder of the state."},
]

practice = [
 {"gen": "type", "items": [
  {"prompt": "Say in Greek: **to desecrate**", "answer": "βεβηλώνω", "accept": ["βεβηλώνω"]},
  {"prompt": "Say in Greek: **to set on fire, torch** (learned)", "answer": "πυρπολώ", "accept": ["πυρπολώ"]},
  {"prompt": "Say in Greek: **to bow** (before someone)", "answer": "υποκλίνομαι", "accept": ["υποκλίνομαι"]},
  {"prompt": "Say in Greek: **indomitable**", "answer": "αδάμαστος", "accept": ["αδάμαστος"]},
  {"prompt": "Say in Greek: **incomparable, unrivalled**", "answer": "απαράμιλλος", "accept": ["απαράμιλλος"]},
  {"prompt": "Say in Greek: **to be accountable, give an account**", "answer": "λογοδοτώ", "accept": ["λογοδοτώ"]},
  {"prompt": "Say in Greek: **to tarnish** (reputation, glory)", "answer": "αμαυρώνω", "accept": ["αμαυρώνω"]},
  {"prompt": "Say in Greek: **concord, unity** (Kolokotronis' word)", "answer": "ομόνοια", "accept": ["ομόνοια", "η ομόνοια"]},
  {"prompt": "Say in Greek: **discord**", "answer": "διχόνοια", "accept": ["διχόνοια", "η διχόνοια"]},
  {"prompt": "Say in Greek: **to promise the moon** (idiom with hares)", "answer": "τάζω λαγούς με πετραχήλια", "accept": ["τάζω λαγούς με πετραχήλια", "τάζει λαγούς με πετραχήλια", "λαγούς με πετραχήλια"]},
  {"prompt": "Say in Greek: **to squeeze dry, exploit** (colloquial)", "answer": "ξεζουμίζω", "accept": ["ξεζουμίζω"]},
  {"prompt": "Say in Greek: **uprising**", "answer": "εξέγερση", "accept": ["εξέγερση", "η εξέγερση", "ξεσηκωμός"]},
  {"prompt": "Say in Greek: **to carry through, complete** (φέρνω…)", "answer": "φέρνω σε πέρας", "accept": ["φέρνω σε πέρας", "φέρω εις πέρας"]},
  {"prompt": "Say in Greek: **oratorical skill**", "answer": "ρητορική δεινότητα", "accept": ["ρητορική δεινότητα", "η ρητορική δεινότητα"]},
  {"prompt": "Say in Greek: **forerunner**", "answer": "πρόδρομος", "accept": ["πρόδρομος", "ο πρόδρομος"]},
 ]},
 {"gen": "mc", "items": [
  mc("«Οι Βάρβαροι τρέπονται εις φυγήν» στα καθημερινά ελληνικά:", "Οι εχθροί το βάζουν στα πόδια", ["Οι εχθροί παραδίνονται", "Οι εχθροί επιτίθενται", "Οι εχθροί αλλάζουν δρόμο"], "τρέπομαι εις φυγήν = flee."),
  mc("«Η Ελλάς δεν δύναται ν' απουσιάση» =", "Η Ελλάδα δεν μπορεί να λείπει", ["Η Ελλάδα δεν θέλει να φύγει", "Η Ελλάδα δεν πρέπει να μιλήσει", "Η Ελλάδα δεν ξέρει πού να πάει"], "δύναμαι = μπορώ; απουσιάζω = λείπω."),
  mc("«Αρκούμεθα εις την διαπίστωσιν ότι…» σημαίνει:", "Περιοριζόμαστε να επισημάνουμε ότι…", ["Αρνούμαστε να δεχτούμε ότι…", "Μας φτάνει να ελπίζουμε ότι…", "Αποδεικνύουμε πέρα από κάθε αμφιβολία ότι…"], "αρκούμαι σε = confine oneself to."),
  mc("«Εδώ ήσαν ευτυχείς όσοι επροκινδύνευαν»: το «επροκινδύνευαν» =", "διακινδύνευαν τη ζωή τους", ["προειδοποιούσαν για κινδύνους", "απέφευγαν κάθε κίνδυνο", "προκαλούσαν φασαρίες"], "προκινδυνεύω = risk oneself (for others)."),
  mc("«ηθέλαμε κυριεύσει και την Θεσσαλία» =", "θα είχαμε κατακτήσει και τη Θεσσαλία", ["θέλαμε να κατακτήσουμε τη Θεσσαλία", "κατακτήσαμε τη Θεσσαλία", "θα κατακτήσουμε τη Θεσσαλία"], "Old conditional ήθελα + infinitive = θα είχα + participle."),
  mc("«Ανάγκασαν τους εχθρούς να γλύψουν εκεί που έφτυσαν» σημαίνει ότι οι εχθροί:", "αναγκάστηκαν ταπεινωτικά να πάρουν πίσω όσα έλεγαν", ["ζήτησαν συγγνώμη ευγενικά", "νίκησαν τελικά", "συνέχισαν να βρίζουν"], "γλείφω εκεί που έφτυσα = eat one's words, humiliatingly."),
  mc("Ποια φράση είναι ΔΗΜΟΤΙΚΗ;", "κρατάνε τον λόγο τους", ["τηρούν τον λόγον των", "υπεσχέθησαν ελευθερωταί", "εκφράζομεν τον θαυμασμόν μας"], "Final -ν, των and -θησαν mark the others as katharevousa."),
  mc("Ο Βελουχιώτης λέει «Δεν επιδιώκω ν' αποσπάσω επαίνους για τη ρητορική μου δεινότητα». Τι δείχνει αυτό;", "Ότι και ο δημοτικός λόγος χρησιμοποιεί λόγιες λέξεις για βάρος", ["Ότι μιλάει καθαρεύουσα", "Ότι δεν ξέρει ρητορική", "Ότι μιμείται τον Παπανδρέου ειρωνικά"], "επιδιώκω, αποσπώ, δεινότητα are learned words in demotic grammar: standard Greek's mix."),
  mc("«Ο πολύς Γιάννης Καποδίστριας»: το «πολύς» εδώ είναι:", "ειρωνικό («ο περιβόητος»)", ["κυριολεκτικό («ψηλός»)", "τιμητικό χωρίς ειρωνεία", "αριθμητικό («πολλοί»)"], "ο πολύς + name = 'the great so-and-so', usually sarcastic."),
 ]},
]

d = {"el": "Λόγοι για την ελευθερία: τρία ύφη", "title": "Register and rhetoric: Kolokotronis, Papandreou, Velouchiotis", "section": "C1 · reading",
     "goal": "Compare katharevousa and demotic oratory on the same theme, and name the rhetorical tools each speaker uses.",
     "blocks": blocks, "practice": practice}
write('c1-read-register-speeches', d)
