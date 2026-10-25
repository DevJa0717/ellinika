"""Writes app/library/philosophers/index.json from the chapter plan below, listing only chapters whose file exists.
Run: python3 /mnt/project-files/tools/philosophers/make_index.py"""
import json, os
APP = "/mnt/project-files/app"
D = os.path.join(APP, "library/philosophers")
PARTS = [
    {"id": "ionia", "el": "Οι πρώτοι φυσικοί", "en": "The first natural philosophers", "dates": "περ. 600–480 π.Χ.",
     "intro_el": "Στις πόλεις της Ιωνίας και της Κάτω Ιταλίας, μερικοί άνθρωποι άρχισαν να εξηγούν τον κόσμο χωρίς μύθους, με παρατήρηση και επιχειρήματα.",
     "intro_en": "In the Greek cities of Ionia (the west coast of Asia Minor) and of southern Italy, a few people began to explain the world without myths, through observation and argument. Aristotle called them the physikoi, the students of nature."},
    {"id": "being", "el": "Το Είναι, τα στοιχεία, τα άτομα", "en": "Being, elements and atoms", "dates": "περ. 515–370 π.Χ.",
     "intro_el": "Ο Παρμενίδης αμφισβήτησε την ίδια την αλλαγή. Οι επόμενοι φιλόσοφοι προσπάθησαν να σώσουν τον κόσμο των αισθήσεων με στοιχεία, νου και άτομα.",
     "intro_en": "Parmenides argued that change and plurality are impossible. The next generation tried to rescue the world of the senses: Empedocles with four elements, Anaxagoras with Mind, Leucippus and Democritus with atoms and the void."},
    {"id": "athens", "el": "Η κλασική Αθήνα", "en": "Classical Athens", "dates": "περ. 490–322 π.Χ.",
     "intro_el": "Στη δημοκρατική Αθήνα η φιλοσοφία στράφηκε στον άνθρωπο: στη γλώσσα, στην ηθική, στην πολιτική. Εδώ έζησαν οι σοφιστές, ο Σωκράτης, ο Πλάτων και ο Αριστοτέλης.",
     "intro_en": "In democratic Athens philosophy turned towards human beings: language, ethics, politics and knowledge. Here the sophists taught for fees, Socrates questioned everyone, and Plato and Aristotle founded the first lasting schools."},
    {"id": "hellenistic", "el": "Οι δρόμοι της ευτυχίας", "en": "Hellenistic roads to happiness", "dates": "περ. 404–206 π.Χ.",
     "intro_el": "Σε έναν κόσμο βασιλείων και πολέμων, οι φιλόσοφοι ρωτούσαν πώς μπορεί κανείς να ζήσει ήρεμα και ελεύθερα. Κυνικοί, σκεπτικοί, επικούρειοι και στωικοί έδωσαν διαφορετικές απαντήσεις.",
     "intro_en": "In a world of kings, mercenaries and great new cities, philosophers asked how one can live calmly and freely whatever happens. Cynics, Sceptics, Epicureans and Stoics gave rival answers, and their schools lasted for centuries."},
    {"id": "late", "el": "Ρωμαϊκή εποχή και ύστερη αρχαιότητα", "en": "The Roman era and late antiquity", "dates": "1ος–5ος αι. μ.Χ.",
     "intro_el": "Υπό τη ρωμαϊκή εξουσία η ελληνική φιλοσοφία έγινε η φιλοσοφία ολόκληρης της αυτοκρατορίας. Ένας πρώην δούλος και ένας αυτοκράτορας έγραψαν ελληνικά για τη στωική ζωή, ενώ ο νεοπλατωνισμός έδωσε την τελευταία μεγάλη σύνθεση της αρχαίας σκέψης.",
     "intro_en": "Under Roman rule Greek philosophy became the philosophy of the whole empire, still written in Greek. A former slave and an emperor wrote about the Stoic life, and Neoplatonism produced the last great synthesis of ancient thought before the schools closed."},
]
CHAPTERS = [
    ("thales", "ionia", "Θαλής ο Μιλήσιος", "Thales of Miletus", "B1+", "περ. 624 – 546 π.Χ."),
    ("anaximander", "ionia", "Αναξίμανδρος", "Anaximander", "B1+", "περ. 610 – 546 π.Χ."),
    ("anaximenes", "ionia", "Αναξιμένης", "Anaximenes", "B1+", "περ. 585 – 525 π.Χ."),
    ("pythagoras", "ionia", "Πυθαγόρας", "Pythagoras", "B2", "περ. 570 – 495 π.Χ."),
    ("xenophanes", "ionia", "Ξενοφάνης", "Xenophanes", "B2", "περ. 570 – 475 π.Χ."),
    ("heraclitus", "ionia", "Ηράκλειτος", "Heraclitus", "B2", "περ. 535 – 475 π.Χ."),
    ("parmenides", "being", "Παρμενίδης", "Parmenides", "B2", "περ. 515 – 450 π.Χ."),
    ("zeno-elea", "being", "Ζήνων ο Ελεάτης", "Zeno of Elea", "B2", "περ. 490 – 430 π.Χ."),
    ("empedocles", "being", "Εμπεδοκλής", "Empedocles", "B2", "περ. 494 – 434 π.Χ."),
    ("anaxagoras", "being", "Αναξαγόρας", "Anaxagoras", "B2", "περ. 500 – 428 π.Χ."),
    ("democritus", "being", "Δημόκριτος", "Democritus", "B2", "περ. 460 – 370 π.Χ."),
    ("protagoras", "athens", "Πρωταγόρας", "Protagoras", "B2", "περ. 490 – 420 π.Χ."),
    ("gorgias", "athens", "Γοργίας", "Gorgias", "B2", "περ. 483 – 375 π.Χ."),
    ("socrates", "athens", "Σωκράτης", "Socrates", "B2+", "469 – 399 π.Χ."),
    ("plato", "athens", "Πλάτων", "Plato", "B2+", "περ. 428 – 348 π.Χ."),
    ("aristotle", "athens", "Αριστοτέλης", "Aristotle", "B2+", "384 – 322 π.Χ."),
    ("diogenes", "hellenistic", "Διογένης ο Κυνικός", "Diogenes the Cynic", "B2+", "περ. 412/404 – 323 π.Χ."),
    ("crates-hipparchia", "hellenistic", "Κράτης και Ιππαρχία", "Crates and Hipparchia", "B2+", "4ος – 3ος αι. π.Χ."),
    ("pyrrho", "hellenistic", "Πύρρων ο Ηλείος", "Pyrrho of Elis", "B2+", "περ. 360 – 270 π.Χ."),
    ("epicurus", "hellenistic", "Επίκουρος", "Epicurus", "C1", "341 – 270 π.Χ."),
    ("zeno-citium", "hellenistic", "Ζήνων ο Κιτιεύς", "Zeno of Citium", "C1", "περ. 334 – 262 π.Χ."),
    ("epictetus", "late", "Επίκτητος", "Epictetus", "C1", "περ. 50 – 135 μ.Χ."),
    ("marcus-aurelius", "late", "Μάρκος Αυρήλιος", "Marcus Aurelius", "C1", "121 – 180 μ.Χ."),
    ("plotinus", "late", "Πλωτίνος", "Plotinus", "C1", "περ. 204 – 270 μ.Χ."),
    ("hypatia", "late", "Υπατία", "Hypatia", "C1", "περ. 355/370 – 415 μ.Χ."),
]
items = [{"id": i, "file": i + ".json", "el": el, "title": en, "level": lv, "part": p, "dates": dt}
         for i, p, el, en, lv, dt in CHAPTERS if os.path.exists(os.path.join(D, i + ".json"))]
idx = {"kind": "bilingual", "el": "Οι Έλληνες φιλόσοφοι", "title": "The Greek philosophers: a bilingual reader",
       "intro_el": "Από τον Θαλή ως την Υπατία: η ζωή, η εποχή, η εικόνα του κόσμου, οι ιδέες και η επίδραση των Ελλήνων φιλοσόφων. Τα κεφάλαια ακολουθούν τη χρονολογική σειρά, και τα ελληνικά γίνονται σταδιακά πιο απαιτητικά.",
       "intro_en": "From Thales to Hypatia: the life, times, picture of the world, ideas and influence of each Greek philosopher. Chapters follow the chronological order and the Greek grows gradually harder, from B1+ to C1. Every chapter has the Greek text with a fuller English parallel (switch between Greek only, both and English only), new terms defined in Greek and English, graded grammar notes, numbered sources, questions and words to keep. Tap any Greek word to look it up.",
       "parts": [p for p in PARTS if any(x["part"] == p["id"] for x in items)], "items": items}
json.dump(idx, open(os.path.join(D, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(items), "chapters in index")
