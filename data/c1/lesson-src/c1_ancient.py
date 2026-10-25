import json, sys, random
random.seed(3)
S = [ # saying, meaning, origin, modern use
 ("Μηδέν άγαν","nothing in excess","Delphic maxim","Ακόμα και στη γυμναστική: μηδέν άγαν."),
 ("Γνώθι σαυτόν","know thyself","Delphic maxim","Πριν κρίνεις τους άλλους, γνώθι σαυτόν."),
 ("Τα πάντα ρει","everything flows","Heraclitus","Η πολιτική αλλάζει συνεχώς· τα πάντα ρει."),
 ("Εν οίδα ότι ουδέν οίδα","I know one thing: that I know nothing","Socrates (Plato)","Όσο περισσότερο διαβάζω, τόσο πιο πολύ καταλαβαίνω το «εν οίδα ότι ουδέν οίδα»."),
 ("Ουκ εν τω πολλώ το ευ","quality is not in quantity","proverbial","Δεν χρειάζεσαι δέκα συνταγές· ουκ εν τω πολλώ το ευ."),
 ("Αρχή ήμισυ παντός","the beginning is half of everything","Pythagoreans / Plato","Γράψε την πρώτη σελίδα σήμερα. Αρχή ήμισυ παντός!"),
 ("Η αρχή άνδρα δείκνυσι","office shows the man","Bias of Priene","Θα δούμε τι θα κάνει ως υπουργός· η αρχή άνδρα δείκνυσι."),
 ("Μολών λαβέ","come and take them","Leonidas at Thermopylae","Ο εργαζόμενος απάντησε στις απειλές με ένα «μολών λαβέ»."),
 ("Ή ταν ή επί τας","with it or on it (the shield)","Spartan mothers","Πήγε στον τελικό με το πνεύμα «ή ταν ή επί τας»."),
 ("Ουδείς αναμάρτητος","nobody is without sin","New Testament","Όλοι κάνουμε λάθη· ουδείς αναμάρτητος."),
 ("Ο κύβος ερρίφθη","the die is cast","Caesar via Plutarch","Υπέβαλα την παραίτησή μου. Ο κύβος ερρίφθη."),
 ("Συν Αθηνά και χείρα κίνει","with Athena's help, move your hand too","Aesop","Η προσευχή δεν φτάνει· συν Αθηνά και χείρα κίνει."),
 ("Παν μέτρον άριστον","moderation is best","Cleobulus","Καλό το κρασί, αλλά παν μέτρον άριστον."),
 ("Ουαί τοις ηττημένοις","woe to the vanquished","Latin 'vae victis' in Greek","Στην πολιτική, ουαί τοις ηττημένοις."),
 ("Πταίσμα / ουδέν πταίσμα","no fault (formula)","legal","—"),
 ("Ενός κακού μύρια έπονται","one evil is followed by ten thousand","proverbial","Χάλασε το αυτοκίνητο, μετά το κινητό, μετά... ενός κακού μύρια έπονται."),
 ("Ουκ αν λάβοις παρά του μη έχοντος","you can't take from one who has nothing","proverbial","Ζητάνε φόρους από ανέργους; Ουκ αν λάβοις παρά του μη έχοντος."),
 ("Έπεα πτερόεντα","winged words (empty promises)","Homer","Οι προεκλογικές υποσχέσεις ήταν έπεα πτερόεντα."),
 ("Πόλεμος πάντων πατήρ","war is the father of all","Heraclitus","Χωρίς σύγκρουση δεν υπάρχει πρόοδος· πόλεμος πάντων πατήρ."),
 ("Ο εχθρός του καλού είναι το καλύτερο","the enemy of the good is the better","modern (Voltaire)","Σταμάτα να το διορθώνεις· ο εχθρός του καλού είναι το καλύτερο."),
 ("Κατά το δοκούν","as one sees fit","learned formula","Ο καθένας ερμηνεύει τον νόμο κατά το δοκούν."),
 ("Εξ ιδίων τα αλλότρια","judge others by oneself","proverbial","Νομίζει ότι όλοι λένε ψέματα· εξ ιδίων τα αλλότρια."),
 ("Ουδέν κακόν αμιγές καλού","no evil without some good","proverbial","Έχασα τη δουλειά, αλλά βρήκα χρόνο να σπουδάσω· ουδέν κακόν αμιγές καλού."),
 ("Τοις πάσι","to all, publicly","learned","Είναι γνωστό τοις πάσι ότι…"),
]
S=[x for x in S if x[3]!="—"]
meanings=[m for _,m,_,_ in S]
L = {
 "el":"Αρχαίες φράσεις στη νέα ελληνική",
 "title":"Ancient sayings in modern use: μηδέν άγαν, ουδέν κακόν αμιγές καλού",
 "section":"C1 · idiom",
 "goal":"Recognise and use the ancient phrases that educated Greeks quote in conversation, journalism and speeches.",
 "blocks":[
  {"type":"text","text":"Greek has one advantage no other European language has: its classical quotations need no translation for a native speaker to half-understand them. Phrases like **μηδέν άγαν** or **ουδέν κακόν αμιγές καλού** are quoted as naturally as English quotes Shakespeare, in editorials, parliament and at the dinner table. They are written in **monotonic** spelling in everyday use and pronounced in modern Greek."},
  {"type":"table","title":"Two dozen to quote","head":["Saying","Meaning","Origin","In use"],"rows":[[f"**{a}**",b,c,f"*{d}*"] for a,b,c,d in S]},
  {"type":"callout","text":"**Reading the grammar.** These keep ancient forms you've met in learned phrases: datives (*εν τω πολλώ, τοις ηττημένοις, τοις πάσι*), infinitive-like participles (*του μη έχοντος* 'of the one not having'), the ancient optative (*λάβοις* 'you could take'), and **ουδέν/ουδείς** 'nothing/nobody' for modern τίποτα/κανείς. You don't need to produce these forms; you need to parse them when someone quotes."},
  {"type":"culture","title":"Η αρχαία στην καθημερινότητα","text":"Every Greek pupil studies Ancient Greek for six years at secondary school, so a phrase from Plato or Thucydides is shared cultural capital, not erudition. Politicians lean on it heavily (and get mocked for misquoting). *Μολών λαβέ* is printed on army badges and T-shirts; *Ο κύβος ερρίφθη* closes a decision; and *Εν οίδα ότι ουδέν οίδα* is the standard reply to a compliment on your knowledge."},
  {"type":"reading","title":"Από ένα κύριο άρθρο","text":"Τα πάντα ρει, έλεγε ο Ηράκλειτος, και σπάνια η φράση του ήταν τόσο επίκαιρη. Η τεχνητή νοημοσύνη αλλάζει την αγορά εργασίας με ρυθμούς που κανείς δεν προέβλεψε. Οι αισιόδοξοι μάς θυμίζουν ότι **ουδέν κακόν αμιγές καλού**: θα χαθούν θέσεις, αλλά θα γεννηθούν άλλες. Οι απαισιόδοξοι απαντούν ότι **ενός κακού μύρια έπονται**.\n\nΗ αλήθεια, όπως συνήθως, βρίσκεται κάπου στη μέση. **Παν μέτρον άριστον**, και στον ενθουσιασμό και στον φόβο. Η κυβέρνηση υποσχέθηκε νομοθετικό πλαίσιο, αλλά μέχρι στιγμής οι δεσμεύσεις της μοιάζουν με **έπεα πτερόεντα**.\n\nΑς ξεκινήσουμε από το αυτονόητο: την εκπαίδευση. **Αρχή ήμισυ παντός.** Και ας θυμηθούμε ότι η τεχνολογία δεν είναι μοίρα: **συν Αθηνά και χείρα κίνει**.","en":"Everything flows, said Heraclitus, and rarely has his phrase been so topical. Artificial intelligence is changing the labour market at a pace nobody predicted. The optimists remind us that no evil is without some good: jobs will be lost, but others will be born. The pessimists reply that one evil brings ten thousand more.\n\nThe truth, as usual, lies somewhere in between. Moderation is best, in enthusiasm and in fear. The government has promised a legislative framework, but so far its commitments look like empty words.\n\nLet us start from the obvious: education. Well begun is half done. And let us remember that technology is not fate: God helps those who help themselves.",
   "gloss":{"επίκαιρη":"topical","αισιόδοξοι":"optimists","νομοθετικό πλαίσιο":"legislative framework","αυτονόητο":"self-evident"},
   "questions":[{"prompt":"Τι εννοεί ο αρθρογράφος με το «έπεα πτερόεντα»;","answer":"Ότι οι υποσχέσεις της κυβέρνησης δεν έχουν ακόμη ουσία.","options":["Ότι οι υποσχέσεις της κυβέρνησης δεν έχουν ακόμη ουσία.","Ότι η κυβέρνηση νομοθέτησε γρήγορα.","Ότι η τεχνολογία πετάει.","Ότι οι απαισιόδοξοι έχουν δίκιο."],"why":"έπεα πτερόεντα = λόγια που τα παίρνει ο αέρας."},
     {"prompt":"Ποια είναι η θέση του αρθρογράφου;","answer":"Ούτε υπερβολικός ενθουσιασμός ούτε φόβος· χρειάζεται δράση, ξεκινώντας από την εκπαίδευση.","options":["Ούτε υπερβολικός ενθουσιασμός ούτε φόβος· χρειάζεται δράση, ξεκινώντας από την εκπαίδευση.","Η τεχνητή νοημοσύνη πρέπει να απαγορευτεί.","Οι αισιόδοξοι έχουν απόλυτο δίκιο.","Η τεχνολογία είναι μοίρα."],"why":"Παν μέτρον άριστον … Αρχή ήμισυ παντός … συν Αθηνά και χείρα κίνει."}]}
 ],
 "practice":[
  {"gen":"mc","n":12,"items":[{"prompt":f"**{a}** means…","answer":b,"options":[b]+random.sample([x for x in meanings if x!=b],3),"why":f"{c}. *{d}*"} for a,b,c,d in S]},
  {"gen":"type","n":8,"items":[{"prompt":f"Ancient saying for **{b}**","answer":a,"accept":[a,a.lower()],"why":f"*{d}*"} for a,b,c,d in S]}
 ]
}
json.dump(L, open("/mnt/project-files/app/lessons/c1-ancient-sayings.json","w"), ensure_ascii=False, indent=1)
print(len(S))
