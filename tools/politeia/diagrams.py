"""Draw the labelled diagrams and charts of the polity reader as SVG (own work, CC0).
Writes app/img/politeia/*.svg and prints image entries for images.json."""
import math, json, os
from html import escape as E

OUT = "/mnt/project-files/app/img/politeia"
W = 1100
FONT = "'Noto Sans','Segoe UI',Roboto,Arial,sans-serif"
INK, MUTE, PAPER, LINE = "#1d2433", "#5b6475", "#fbf8f1", "#c9c2b2"
BLUE, NAVY, GOLD, TEAL, RED, GREEN = "#0d5eaf", "#1f3a5f", "#c8962e", "#2a8c82", "#b8433a", "#3f8f4a"
PARTY = {"ΝΔ": "#1f5fbf", "ΠΑΣΟΚ": "#2e9e44", "ΣΥΡΙΖΑ": "#c2185b", "ΚΚΕ": "#c62828", "ΑΝΕΛ": "#213a7a",
         "Χρυσή Αυγή": "#3b3b3b", "ΔΗΜΑΡ": "#e08e0b", "Σπαρτιάτες": "#5d4037", "Ελληνική Λύση": "#4fa3d9",
         "Νίκη": "#00a19a", "Πλεύση Ελευθερίας": "#8e44ad"}


def svg(name, h, body, title, sub):
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" font-family="{FONT}">'
         f'<title>{E(title)}</title><rect width="{W}" height="{h}" fill="{PAPER}"/>'
         f'<text x="40" y="54" font-size="32" font-weight="700" fill="{INK}">{E(title)}</text>'
         f'<text x="40" y="86" font-size="19" fill="{MUTE}">{E(sub)}</text>'
         + body + "</svg>")
    open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8").write(s)


def T(x, y, s, size=20, fill=INK, w="400", anchor="start", italic=False):
    st = ' font-style="italic"' if italic else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}"{st}>{E(s)}</text>'


def lines(x, y, rows, size=20, fill=INK, w="400", anchor="start", gap=1.3):
    return "".join(T(x, y + i * size * gap, r, size, fill, w, anchor) for i, r in enumerate(rows))


def box(x, y, w, h, head, rows=(), fill=BLUE, sub=None):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#fff" stroke="{fill}" stroke-width="3"/>'
    s += f'<path d="M{x} {y+14} a14 14 0 0 1 14 -14 h{w-28} a14 14 0 0 1 14 14 v34 h-{w} z" fill="{fill}"/>'
    s += T(x + w / 2, y + 33, head, 22, "#fff", "700", "middle")
    yy = y + 76
    if sub:
        s += T(x + w / 2, yy, sub, 17, MUTE, "400", "middle", True); yy += 30
    s += lines(x + w / 2, yy, rows, 19, INK, "400", "middle")
    return s


def arrow(x1, y1, x2, y2, col=MUTE, label=None, lx=None, ly=None, size=17):
    a = math.atan2(y2 - y1, x2 - x1); L = 14
    p1 = (x2 - L * math.cos(a - 0.4), y2 - L * math.sin(a - 0.4)); p2 = (x2 - L * math.cos(a + 0.4), y2 - L * math.sin(a + 0.4))
    s = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="3"/>'
    s += f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{col}"/>'
    if label:
        s += T(lx if lx is not None else (x1 + x2) / 2, ly if ly is not None else (y1 + y2) / 2 - 8, label, size, col, "600", "middle")
    return s


def foot(h, s):
    return T(40, h - 22, s, 15, MUTE)


IMAGES = {}


def reg(cid, name, cap, cap_en, src="Σύνταγμα της Ελλάδας / Constitution of Greece"):
    IMAGES[cid] = {"file": f"img/politeia/{name}.svg", "caption": cap, "caption_en": cap_en,
                   "credit": f"Διάγραμμα της εφαρμογής Ελληνικά · diagram drawn for Ellinika; data: {src}",
                   "license": "CC0", "source": "https://devja0717.github.io/ellinika/img/politeia/" + name + ".svg"}


# 1. Separation of powers
def diakrisi():
    h = 640; b = ""
    b += box(40, 130, 320, 250, "Νομοθετική", ["Βουλή (300 βουλευτές)", "και Πρόεδρος της", "Δημοκρατίας", "ψηφίζουν τους νόμους"], NAVY, "legislative · Άρθρο 26(1)")
    b += box(390, 130, 320, 250, "Εκτελεστική", ["Πρόεδρος της Δημοκρατίας", "και Κυβέρνηση", "εφαρμόζουν τους νόμους"], BLUE, "executive · Άρθρο 26(2)")
    b += box(740, 130, 320, 250, "Δικαστική", ["Τα δικαστήρια", "αποφασίζουν «εν ονόματι", "του Ελληνικού Λαού»"], TEAL, "judicial · Άρθρο 26(3)")
    b += arrow(360, 300, 390, 300, NAVY)
    b += T(200, 430, "Η Βουλή δίνει ή αρνείται", 19, NAVY, "600", "middle") + T(200, 456, "ψήφο εμπιστοσύνης στην Κυβέρνηση", 19, NAVY, "600", "middle")
    b += T(200, 484, "confidence vote (Άρθρα 84, 37)", 16, MUTE, "400", "middle", True)
    b += T(550, 430, "Η Κυβέρνηση φέρνει νομοσχέδια", 19, BLUE, "600", "middle") + T(550, 456, "και ελέγχεται στη Βουλή", 19, BLUE, "600", "middle")
    b += T(550, 484, "bills, questions, inquiries", 16, MUTE, "400", "middle", True)
    b += T(900, 430, "Κάθε δικαστής αφήνει", 19, TEAL, "600", "middle") + T(900, 456, "ανεφάρμοστο αντισυνταγματικό νόμο", 19, TEAL, "600", "middle")
    b += T(900, 484, "diffuse review (Άρθρο 93(4))", 16, MUTE, "400", "middle", True)
    b += f'<rect x="40" y="520" width="1020" height="64" rx="12" fill="#efe8d8"/>'
    b += T(550, 560, "Πάνω από όλους: το Σύνταγμα και η λαϊκή κυριαρχία (Άρθρο 1)", 21, INK, "700", "middle")
    svg("diakrisi", h, b, "Η διάκριση των εξουσιών", "The separation of powers in the Constitution of 1975")
    reg("diakrisi", "diakrisi", "Οι τρεις εξουσίες και πώς ελέγχει η μία την άλλη (Άρθρο 26).", "The three powers and how they check one another (Article 26).")


# 2. Revision procedure
def anatheorisi():
    h = 700; b = ""
    b += box(40, 120, 300, 170, "1. Πρόταση", ["τουλάχιστον 50 βουλευτές", "ορίζουν τα άρθρα"], NAVY, "proposal")
    b += box(400, 120, 300, 170, "2. Δύο ψηφοφορίες", ["με απόσταση", "τουλάχιστον ενός μήνα"], NAVY, "two votes, a month apart")
    b += box(760, 120, 300, 170, "3. Εκλογές", ["νέα Βουλή:", "η αναθεωρητική"], GOLD, "general election")
    b += arrow(340, 205, 400, 205) + arrow(700, 205, 760, 205)
    b += T(550, 345, "Η πλειοψηφία της πρώτης Βουλής καθορίζει τι χρειάζεται η δεύτερη:", 20, INK, "600", "middle")
    b += box(90, 380, 420, 160, "180+ ψήφοι (3/5)", ["η επόμενη Βουλή αποφασίζει", "με 151 ψήφους"], BLUE, "first Parliament: three fifths")
    b += box(590, 380, 420, 160, "151–179 ψήφοι", ["η επόμενη Βουλή χρειάζεται", "180 ψήφους"], TEAL, "first Parliament: absolute majority")
    b += f'<rect x="40" y="570" width="1020" height="84" rx="12" fill="#efe8d8"/>'
    b += T(550, 604, "Δεν αναθεωρούνται: η μορφή του πολιτεύματος και βασικά άρθρα για δικαιώματα (Άρθρο 110(1)).", 18, INK, "600", "middle")
    b += T(550, 634, "Νέα αναθεώρηση μόνο πέντε χρόνια μετά την προηγούμενη (Άρθρο 110(6)).", 18, INK, "600", "middle")
    svg("anatheorisi", h, b, "Πώς αλλάζει το Σύνταγμα", "Revising the Constitution: Article 110, over two parliamentary terms")
    reg("anatheorisi", "anatheorisi", "Η διαδικασία της αναθεώρησης: δύο Βουλές και εκλογές ανάμεσα (Άρθρο 110).", "The revision procedure: two Parliaments with an election in between (Article 110).")


# 3. Presidential ballots
def proedros():
    h = 620; b = ""
    data = [("1η", 200, "2/3"), ("2η", 200, "2/3"), ("3η", 180, "3/5"), ("4η", 151, "απόλυτη πλειοψηφία"), ("5η", None, "οι δύο πρώτοι")]
    x0, base, sc = 90, 520, 1.25
    b += f'<line x1="70" y1="{base}" x2="1050" y2="{base}" stroke="{LINE}" stroke-width="2"/>'
    for v in (151, 180, 200, 300):
        y = base - v * sc
        b += f'<line x1="70" y1="{y}" x2="1050" y2="{y}" stroke="{LINE}" stroke-dasharray="6 6"/>' + T(60, y + 6, str(v), 16, MUTE, "400", "end")
    for i, (n, v, lab) in enumerate(data):
        x = x0 + i * 195
        if v:
            y = base - v * sc
            b += f'<rect x="{x}" y="{y}" width="150" height="{v*sc}" rx="8" fill="{NAVY if i < 4 else GOLD}"/>'
            b += T(x + 75, y + 40, str(v), 34, "#fff", "700", "middle") + T(x + 75, y + 68, "ψήφοι", 17, "#fff", "400", "middle")
        else:
            y = base - 120
            b += f'<rect x="{x}" y="{y}" width="150" height="120" rx="8" fill="{GOLD}"/>'
            b += lines(x + 75, y + 40, ["σχετική", "πλειοψηφία"], 19, "#fff", "700", "middle")
        b += T(x + 75, base + 32, f"{n} ψηφοφορία", 19, INK, "700", "middle") + T(x + 75, base + 56, lab, 16, MUTE, "400", "middle")
    b += f'<circle cx="{x0+3*195+75}" cy="{base-160*sc}" r="9" fill="{RED}"/>'
    b += T(x0 + 3 * 195 + 75, base - 160 * sc - 22, "Τασούλας 2025: 160", 17, RED, "700", "middle")
    b += T(1050, 118, "Οι ψηφοφορίες γίνονται κάθε πέντε μέρες · ballots five days apart", 16, MUTE, "400", "end")
    svg("proedros", h, b + foot(h + 0, ""), "Η εκλογή του Προέδρου της Δημοκρατίας", "Votes needed in each parliamentary ballot since the 2019 revision (Article 32)")
    reg("proedros", "proedros", "Πόσες ψήφους χρειάζεται ο υποψήφιος σε κάθε ψηφοφορία (Άρθρο 32, μετά το 2019).", "Votes a candidate needs in each ballot (Article 32, as revised in 2019).")


# 4. Government formation
def kyvernisi():
    h = 720; b = ""
    b += box(40, 120, 330, 180, "Αυτοδυναμία;", ["Αν ένα κόμμα έχει 151+", "έδρες, ο αρχηγός του", "γίνεται πρωθυπουργός"], GREEN, "Art. 37(2)")
    b += box(400, 120, 660, 180, "Διερευνητικές εντολές", ["Ο Πρόεδρος δίνει εντολή στο 1ο, μετά στο 2ο", "και στο 3ο κόμμα, για τρεις μέρες στο καθένα", "exploratory mandates, Art. 37(3)"], BLUE)
    b += arrow(370, 210, 400, 210, MUTE)
    b += T(205, 335, "ναι", 20, GREEN, "700", "middle")
    b += box(40, 360, 330, 170, "Ορκωμοσία", ["και ψήφος εμπιστοσύνης", "μέσα σε 15 μέρες"], NAVY, "Art. 84")
    b += arrow(205, 300, 205, 360, GREEN)
    b += box(400, 360, 310, 170, "Συμμαχία", ["αν βρεθεί πλειοψηφία,", "κυβέρνηση συνεργασίας"], TEAL, "coalition")
    b += box(750, 360, 310, 170, "Υπηρεσιακή", ["κυβέρνηση με ανώτατο", "δικαστή και εκλογές"], GOLD, "caretaker, Art. 37(3)")
    b += arrow(555, 300, 555, 360, TEAL) + arrow(905, 300, 905, 360, GOLD)
    b += arrow(400, 445, 370, 445, TEAL)
    b += f'<rect x="40" y="570" width="1020" height="96" rx="12" fill="#efe8d8"/>'
    b += T(550, 606, "Μάιος 2023: κανένα κόμμα δεν δέχτηκε να σχηματίσει κυβέρνηση.", 19, INK, "600", "middle")
    b += T(550, 640, "Υπηρεσιακός πρωθυπουργός ο Ιωάννης Σαρμάς, και νέες εκλογές στις 25 Ιουνίου.", 19, INK, "600", "middle")
    svg("kyvernisi", h, b, "Πώς σχηματίζεται κυβέρνηση", "Forming a government after an election (Articles 37 and 84)")
    reg("kyvernisi", "kyvernisi", "Από τις εκλογές στην κυβέρνηση: αυτοδυναμία, διερευνητικές εντολές ή υπηρεσιακή κυβέρνηση.", "From election to government: a majority, exploratory mandates or a caretaker government.")


# 5. Seat bonus
def ekloges():
    h = 660; b = ""
    X = lambda p: 120 + (p - 20) * 36
    Y = lambda s: 540 - s * 7.4
    b += f'<line x1="{X(20)}" y1="{Y(0)}" x2="{X(45)}" y2="{Y(0)}" stroke="{INK}" stroke-width="2"/>'
    b += f'<line x1="{X(20)}" y1="{Y(0)}" x2="{X(20)}" y2="{Y(55)}" stroke="{INK}" stroke-width="2"/>'
    for p in range(20, 46, 5):
        b += T(X(p), Y(0) + 30, f"{p}%", 17, MUTE, "400", "middle")
    for s in (0, 10, 20, 30, 40, 50):
        b += f'<line x1="{X(20)}" y1="{Y(s)}" x2="{X(45)}" y2="{Y(s)}" stroke="{LINE}" stroke-dasharray="5 6"/>' + T(X(20) - 12, Y(s) + 6, str(s), 16, MUTE, "400", "end")
    pts = [(20, 0), (25, 0)] + [(25 + k * 0.5, 20 + k) for k in range(31)] + [(45, 50)]
    path = f"M{X(20)} {Y(0)} H{X(25)} V{Y(20)}"
    for p, s in pts[2:]:
        path += f" H{X(p)} V{Y(s)}"
    path += f" H{X(45)}"
    b += f'<path d="{path}" fill="none" stroke="{BLUE}" stroke-width="4"/>'
    b += T(X(20) + 6, Y(55) - 14, "έδρες μπόνους · bonus seats", 18, INK, "600")
    b += T(X(45), Y(0) + 62, "ποσοστό του πρώτου κόμματος · first party's share of the vote", 17, INK, "600", "end")
    b += f'<circle cx="{X(25)}" cy="{Y(20)}" r="8" fill="{NAVY}"/>' + T(X(25) + 14, Y(20) + 26, "25% → 20 έδρες", 18, NAVY, "700")
    b += f'<circle cx="{X(40.56)}" cy="{Y(50)}" r="9" fill="{RED}"/>' + T(X(45), Y(50) - 20, "ΝΔ, Ιούνιος 2023: 40,56% → 50 έδρες μπόνους, 158 συνολικά", 18, RED, "700", "end")
    b += T(X(29), Y(44), "+1 έδρα για κάθε μισή μονάδα", 18, BLUE, "600", "middle")
    svg("ekloges", h, b, "Το μπόνους εδρών (ν. 4654/2020)", "Bonus seats for the first party under the electoral law used since June 2023", )
    reg("ekloges", "ekloges", "Το μπόνους εδρών του νόμου 4654/2020: 20 έδρες στο 25%, έως 50 έδρες στο 40%.", "The seat bonus under Law 4654/2020: 20 seats at 25%, rising to 50 seats at 40%.", "ν. 4654/2020; Υπουργείο Εσωτερικών, εκλογές 2023")


# 6. Hierarchy of norms
def nomoi():
    h = 660; b = ""
    rows = [("Σύνταγμα", "Constitution", NAVY), ("Διεθνές και ενωσιακό δίκαιο", "international law, EU law (Art. 28)", BLUE),
            ("Νόμοι της Βουλής · ΠΝΠ", "statutes · acts of legislative content (Art. 44)", TEAL),
            ("Προεδρικά διατάγματα", "presidential decrees, checked by the Council of State", GOLD),
            ("Υπουργικές αποφάσεις", "ministerial decisions", "#8a7a5a")]
    top, hh = 120, 92
    for i, (el, en, c) in enumerate(rows):
        y = top + i * (hh + 8); half = 130 + i * 85
        b += f'<polygon points="{550-half+40},{y} {550+half-40},{y} {550+half+45},{y+hh} {550-half-45},{y+hh}" fill="{c}"/>'
        b += T(550, y + 40, el, 23, "#fff", "700", "middle") + T(550, y + 68, en, 16, "#fff", "400", "middle")
    b += arrow(1040, 600, 1040, 130, MUTE)
    b += T(1020, 380, "υπερέχει", 18, MUTE, "600", "end")
    svg("nomoi", h, b, "Η ιεραρχία των κανόνων δικαίου", "Which rule prevails: from the Constitution down to a minister's decision")
    reg("nomoi", "nomoi", "Η πυραμίδα του δικαίου: κάθε κανόνας πρέπει να συμφωνεί με τους ανώτερους.", "The pyramid of law: each rule must conform to those above it.")


# 7. Independent authorities
def anexartites():
    h = 680; b = ""
    items = [("Συνήγορος του Πολίτη", "Ombudsman · 1998", "Άρθρο 103(9)"), ("ΑΣΕΠ", "public-sector hiring · 1994", "Άρθρο 103(7)"),
             ("Αρχή Προστασίας Δεδομένων", "data protection · 1997", "Άρθρο 9Α"), ("ΕΣΡ", "radio and television · 1989", "Άρθρο 15(2)"),
             ("ΑΔΑΕ", "privacy of communications · 2003", "Άρθρο 19(2)")]
    b += T(40, 140, "Στο Σύνταγμα από το 2001 (Άρθρο 101Α): μέλη από τη Διάσκεψη των Προέδρων με 3/5", 19, INK, "600")
    for i, (el, en, art) in enumerate(items):
        x = 40 + (i % 3) * 345; y = 170 + (i // 3) * 170
        b += f'<rect x="{x}" y="{y}" width="325" height="145" rx="14" fill="#fff" stroke="{NAVY}" stroke-width="3"/>'
        b += T(x + 162, y + 44, el, 21, NAVY, "700", "middle") + T(x + 162, y + 76, en, 17, MUTE, "400", "middle", True)
        b += T(x + 162, y + 114, art, 18, INK, "600", "middle")
    b += T(40, 545, "Από την κρίση χρέους:", 19, INK, "600")
    for i, (el, en) in enumerate([("ΕΛΣΤΑΤ", "statistics · ανεξάρτητη από το 2010"), ("ΑΑΔΕ", "tax and customs · από το 2017")]):
        x = 40 + i * 520
        b += f'<rect x="{x}" y="565" width="500" height="80" rx="14" fill="#fff" stroke="{TEAL}" stroke-width="3"/>'
        b += T(x + 250, 598, el, 21, TEAL, "700", "middle") + T(x + 250, 628, en, 17, MUTE, "400", "middle", True)
    svg("anexartites", h, b, "Οι ανεξάρτητες αρχές", "Bodies that take no orders from the Government")
    reg("anexartites", "anexartites", "Οι πέντε ανεξάρτητες αρχές που κατοχυρώνει το Σύνταγμα, και δύο από την εποχή της κρίσης.", "The five independent authorities named in the Constitution, and two from the crisis years.")


# 8. Digital state timeline
def timeline(name, title, sub, ev, cid, cap, cap_en, src):
    h = 160 + len(ev) * 86; b = ""
    b += f'<line x1="200" y1="130" x2="200" y2="{h-50}" stroke="{LINE}" stroke-width="5"/>'
    for i, (yr, el, en) in enumerate(ev):
        y = 150 + i * 86
        b += f'<circle cx="200" cy="{y}" r="13" fill="{BLUE}" stroke="#fff" stroke-width="4"/>'
        b += T(170, y + 9, yr, 25, NAVY, "700", "end")
        b += T(232, y + 4, el, 22, INK, "600") + T(232, y + 32, en, 17, MUTE, "400", "start", True)
    svg(name, h, b, title, sub)
    reg(cid, name, cap, cap_en, src)


def dimosio():
    timeline("dimosio", "Από το γκισέ στο κινητό", "Milestones of the digital Greek state",
             [("1911", "Μονιμότητα των δημοσίων υπαλλήλων", "permanence of civil servants enters the Constitution"),
              ("1994", "ΑΣΕΠ: διορισμοί με διαγωνισμό ή μόρια", "merit-based hiring under an independent body"),
              ("2000s", "Taxisnet: φορολογικές δηλώσεις online", "online income-tax returns"),
              ("2010", "Διαύγεια: όλες οι αποφάσεις στο διαδίκτυο", "every public decision posted online"),
              ("2019", "Υπουργείο Ψηφιακής Διακυβέρνησης", "Ministry of Digital Governance"),
              ("2020", "gov.gr: πάνω από χίλιες υπηρεσίες", "single portal for state services")],
             "dimosio", "Σταθμοί στη μεταμόρφωση του Δημοσίου, από τη μονιμότητα ως το gov.gr.", "Milestones in the transformation of the public sector, from tenure to gov.gr.", "Σύνταγμα, ΑΣΕΠ, Διαύγεια, gov.gr")


def kathimerini():
    timeline("kathimerini", "Μισός αιώνας δημοκρατίας", "The Third Hellenic Republic: some turning points since 1974",
             [("1974", "Μεταπολίτευση · δημοψήφισμα για το πολίτευμα", "fall of the junta; monarchy abolished by referendum"),
              ("1975", "Το Σύνταγμα της Τρίτης Ελληνικής Δημοκρατίας", "the Constitution in force today"),
              ("1981", "Ένταξη στην ΕΟΚ · πρώτη κυβέρνηση ΠΑΣΟΚ", "EEC membership; first PASOK government"),
              ("2001", "Η Ελλάδα στην ευρωζώνη", "Greece joins the euro area"),
              ("2010", "Το πρώτο μνημόνιο", "the first bailout programme"),
              ("2015", "Δημοψήφισμα και τρίτο μνημόνιο", "referendum, then a third programme"),
              ("2018", "Τέλος των προγραμμάτων στήριξης", "exit from the bailout programmes"),
              ("2023", "Διπλές εκλογές, Μάιος και Ιούνιος", "two elections within five weeks")],
             "kathimerini", "Σταθμοί της Μεταπολίτευσης: οι θεσμοί του 1975 άντεξαν κρίσεις και αλλαγές.", "Turning points since 1974: the institutions of 1975 have weathered crisis and change.", "κεφάλαια αυτού του βιβλίου")


# 9. Local government levels
def aftodioikisi():
    h = 680; b = ""
    b += box(250, 115, 600, 120, "Κεντρικό κράτος", ["υπουργεία, Αθήνα"], NAVY, "central State")
    b += box(40, 290, 330, 170, "7 αποκεντρωμένες", ["διοικήσεις του κράτους:", "έλεγχος νομιμότητας"], "#7d7d7d", "not elected")
    b += box(400, 290, 660, 170, "2ος βαθμός: 13 περιφέρειες", ["περιφερειάρχης και περιφερειακό συμβούλιο", "74 περιφερειακές ενότητες"], BLUE, "regions, elected every 5 years")
    b += box(400, 490, 660, 150, "1ος βαθμός: 332 δήμοι", ["δήμαρχος και δημοτικό συμβούλιο"], TEAL, "municipalities, elected every 5 years")
    b += arrow(330, 235, 205, 290, MUTE)
    b += arrow(370, 375, 400, 375, "#7d7d7d")
    b += f'<path d="M205 460 V565 H400" fill="none" stroke="#7d7d7d" stroke-width="3"/>' + arrow(380, 565, 400, 565, "#7d7d7d")
    b += T(215, 600, "έλεγχος νομιμότητας", 17, "#7d7d7d", "600")
    svg("aftodioikisi", h, b, "Τα επίπεδα της διοίκησης", "Central State, decentralised administrations and the two levels of local government")
    reg("aftodioikisi", "aftodioikisi", "Δήμοι, περιφέρειες και αποκεντρωμένες διοικήσεις.", "Municipalities, regions and decentralised administrations.", "Σύνταγμα Άρθρο 102· ν. 3852/2010 (Καλλικράτης)· ν. 4555/2018 (Κλεισθένης)")


# 10. ND + PASOK share
EL = [("1974", 54.37, 13.58), ("1977", 41.84, 25.34), ("1981", 35.88, 48.07), ("1985", 40.84, 45.82), ("1989", 44.28, 39.13),
      ("1989Ν", 46.19, 40.67), ("1990", 46.89, 38.61), ("1993", 39.30, 46.88), ("1996", 38.12, 41.49), ("2000", 42.73, 43.80),
      ("2004", 45.36, 40.55), ("2007", 41.84, 38.10), ("2009", 33.47, 43.92), ("2012Μ", 18.85, 13.18), ("2012Ι", 29.66, 12.28),
      ("2015Ι", 27.81, 4.68), ("2015Σ", 28.09, 6.29), ("2019", 39.85, 8.10), ("2023Μ", 40.79, 11.46), ("2023Ι", 40.56, 11.84)]


def dikommatismos():
    h = 640; b = ""
    base, sc, bw = 520, 3.9, 40
    for v in (25, 50, 75):
        y = base - v * sc
        b += f'<line x1="70" y1="{y}" x2="1070" y2="{y}" stroke="{LINE}" stroke-dasharray="5 6"/>' + T(62, y + 6, f"{v}%", 15, MUTE, "400", "end")
    for i, (lab, nd, pa) in enumerate(EL):
        x = 84 + i * 49.5
        b += f'<rect x="{x}" y="{base-nd*sc}" width="{bw}" height="{nd*sc}" fill="{PARTY["ΝΔ"]}"/>'
        b += f'<rect x="{x}" y="{base-(nd+pa)*sc}" width="{bw}" height="{pa*sc}" fill="{PARTY["ΠΑΣΟΚ"]}"/>'
        b += T(x + bw / 2, base - (nd + pa) * sc - 8, f"{round(nd+pa)}", 14, INK, "700", "middle")
        b += f'<text x="{x+bw/2+5}" y="{base+14}" font-size="14" fill="{MUTE}" transform="rotate(50 {x+bw/2+5} {base+14})">{E(lab)}</text>'
    b += f'<rect x="700" y="112" width="22" height="22" fill="{PARTY["ΝΔ"]}"/>' + T(730, 130, "Νέα Δημοκρατία", 18)
    b += f'<rect x="880" y="112" width="22" height="22" fill="{PARTY["ΠΑΣΟΚ"]}"/>' + T(910, 130, "ΠΑΣΟΚ / ΚΙΝΑΛ", 18)
    b += T(84, 140, "1977–2009: τα δύο κόμματα μαζί πάνω από 77%", 18, NAVY, "700")
    b += T(835, 285, "2012: η κατάρρευση", 18, RED, "700", "middle")
    b += foot(h, "Μ = Μάιος, Ι = Ιούνιος/Ιανουάριος, Σ = Σεπτέμβριος, Ν = Νοέμβριος · ποσοστά των εθνικών εκλογών")
    svg("dikommatismos", h, b, "Ο δικομματισμός σε αριθμούς", "Combined vote share of New Democracy and PASOK in every general election, 1974–2023")
    reg("dikommatismos", "dikommatismos", "Το άθροισμα ΝΔ και ΠΑΣΟΚ σε κάθε εκλογή από το 1974: κυριαρχία ως το 2009, κατάρρευση το 2012.", "ND plus PASOK in every election since 1974: dominance until 2009, collapse in 2012.", "Υπουργείο Εσωτερικών, εκλογικά αποτελέσματα")


# 11–12. Hemicycles
def hemicycle(name, title, sub, parties, cid, cap, cap_en):
    h = 640; b = ""
    total = sum(n for _, n in parties); cx, cy = 550, 520
    rows, r0, r1 = 8, 190, 400
    radii = [r0 + (r1 - r0) * i / (rows - 1) for i in range(rows)]
    tot_len = sum(radii)
    counts = [round(total * r / tot_len) for r in radii]
    counts[-1] += total - sum(counts)
    seats = []
    for r, n in zip(radii, counts):
        for k in range(n):
            a = math.pi * (1 - k / (n - 1)) if n > 1 else math.pi / 2
            seats.append((a, r))
    seats.sort(key=lambda s: (-s[0], s[1]))
    i = 0
    for p, n in parties:
        for _ in range(n):
            a, r = seats[i]; i += 1
            b += f'<circle cx="{cx + r*math.cos(a):.1f}" cy="{cy - r*math.sin(a):.1f}" r="9.5" fill="{PARTY[p]}"/>'
    b += T(cx, cy - 40, f"{total}", 48, INK, "700", "middle") + T(cx, cy - 8, "έδρες", 20, MUTE, "400", "middle")
    b += T(cx, cy - 100, "151 για αυτοδυναμία", 18, NAVY, "600", "middle")
    cols = 4 if len(parties) > 6 else len(parties)
    for j, (p, n) in enumerate(parties):
        x = 60 + (j % cols) * (1000 / cols); y = 565 + (j // cols) * 34
        b += f'<rect x="{x}" y="{y-17}" width="20" height="20" rx="4" fill="{PARTY[p]}"/>' + T(x + 28, y, f"{p} {n}", 18)
    svg(name, h + (34 if len(parties) > 4 else 0), b, title, sub)
    reg(cid, name, cap, cap_en, "Υπουργείο Εσωτερικών, εκλογικά αποτελέσματα")


# 13. Crisis chart
def mnimonia():
    h = 680; b = ""
    une = {2009: 9.8, 2010: 12.9, 2011: 18.1, 2012: 24.8, 2013: 27.8, 2014: 26.6, 2015: 25.0, 2016: 23.9, 2017: 21.8, 2018: 19.7,
           2019: 17.9, 2020: 17.6, 2021: 14.7, 2022: 12.5, 2023: 11.1, 2024: 10.1, 2025: 8.9}
    gdp = {2007: 247133.7, 2008: 247275.7, 2009: 237089.8, 2010: 223590.5, 2011: 201507.0, 2012: 184719.1, 2013: 180522.1, 2014: 181952.2,
           2015: 181536.8, 2016: 181479.1, 2017: 184152.5, 2018: 187954.7, 2019: 192234.8, 2020: 174556.4, 2021: 189663.4,
           2022: 200182.6, 2023: 204277.2, 2024: 208646.7, 2025: 212936.3}
    X = lambda y: 110 + (y - 2007) * 52
    # GDP panel
    Yg = lambda v: 330 - (v - 70) * 5.2
    b += T(40, 128, "ΑΕΠ σε σταθερές τιμές (2008 = 100) · real GDP", 19, NAVY, "700")
    for v in (70, 80, 90, 100):
        b += f'<line x1="{X(2007)}" y1="{Yg(v)}" x2="{X(2025)}" y2="{Yg(v)}" stroke="{LINE}" stroke-dasharray="5 6"/>' + T(X(2007) - 10, Yg(v) + 6, str(v), 15, MUTE, "400", "end")
    pts = " ".join(f"{X(y):.0f},{Yg(v/gdp[2008]*100):.1f}" for y, v in gdp.items())
    b += f'<polyline points="{pts}" fill="none" stroke="{NAVY}" stroke-width="4"/>'
    low = gdp[2013] / gdp[2008] * 100
    b += f'<circle cx="{X(2013)}" cy="{Yg(low)}" r="7" fill="{RED}"/>' + T(X(2013), Yg(low) + 30, f"2013: {low:.0f}".replace(".", ","), 17, RED, "700", "middle")
    # unemployment panel
    Yu = lambda v: 610 - v * 7
    b += T(40, 390, "Ανεργία, % του εργατικού δυναμικού · unemployment rate", 19, TEAL, "700")
    for v in (10, 20, 30):
        b += f'<line x1="{X(2007)}" y1="{Yu(v)}" x2="{X(2025)}" y2="{Yu(v)}" stroke="{LINE}" stroke-dasharray="5 6"/>' + T(X(2007) - 10, Yu(v) + 6, f"{v}%", 15, MUTE, "400", "end")
    for y, v in une.items():
        b += f'<rect x="{X(y)-17}" y="{Yu(v)}" width="34" height="{v*7}" fill="{RED if y == 2013 else TEAL}"/>'
    b += T(X(2013), Yu(27.8) - 10, "27,8%", 17, RED, "700", "middle")
    for y in range(2007, 2026, 2):
        b += T(X(y), 640, str(y), 15, MUTE, "400", "middle")
    b += f'<rect x="{X(2010)}" y="140" width="{X(2018.6)-X(2010)}" height="8" fill="{GOLD}"/>' + T((X(2010) + X(2018.6)) / 2, 168, "μνημόνια 2010–2018", 16, GOLD, "700", "middle")
    svg("mnimonia", h, b, "Η κρίση σε δύο καμπύλες", "Greek output and unemployment through the bailout years")
    reg("mnimonia", "mnimonia", "Το ΑΕΠ έπεσε περίπου κατά ένα τέταρτο ως το 2013 και η ανεργία ξεπέρασε το 27%.", "GDP fell by about a quarter by 2013 and unemployment passed 27%.", "Eurostat (nama_10_gdp, une_rt_a), 2026")


# 14. Births and deaths
def esoterikes():
    h = 620; b = ""
    births = {1960: 157239, 1961: 150716, 1962: 152297, 1963: 148366, 1964: 153221, 1965: 151565, 1966: 154708, 1967: 162904, 1968: 160406, 1969: 154117, 1970: 144986, 1971: 141155, 1972: 140916, 1973: 137555, 1974: 144096, 1975: 142295, 1976: 146582, 1977: 143757, 1978: 146604, 1979: 147995, 1980: 148147, 1981: 140953, 1982: 137296, 1983: 132621, 1984: 125742, 1985: 116495, 1986: 112823, 1987: 106401, 1988: 107561, 1989: 101657, 1990: 102251, 1991: 102620, 1992: 104081, 1993: 101799, 1994: 103763, 1995: 101495, 1996: 100718, 1997: 102038, 1998: 100894, 1999: 100643, 2000: 103267, 2001: 102282, 2002: 103569, 2003: 104420, 2004: 105655, 2005: 107545, 2006: 112042, 2007: 111926, 2008: 118302, 2009: 117933, 2010: 114766, 2011: 106428, 2012: 100371, 2013: 94134, 2014: 92149, 2015: 91847, 2016: 92898, 2017: 88553, 2018: 86440, 2019: 83763, 2020: 84764, 2021: 85346, 2022: 75921, 2023: 71249, 2024: 68309, 2025: 65439}
    deaths = {1960: 60563, 1961: 63955, 1962: 66554, 1963: 66813, 1964: 69429, 1965: 67269, 1966: 67912, 1967: 71975, 1968: 73309, 1969: 71825, 1970: 74009, 1971: 73819, 1972: 76859, 1973: 77648, 1974: 76303, 1975: 80077, 1976: 81818, 1977: 83750, 1978: 81615, 1979: 82338, 1980: 87282, 1981: 86261, 1982: 86345, 1983: 90586, 1984: 88397, 1985: 92886, 1986: 91783, 1987: 95656, 1988: 92407, 1989: 92720, 1990: 94152, 1991: 95498, 1992: 98231, 1993: 97419, 1994: 97807, 1995: 100158, 1996: 100740, 1997: 99738, 1998: 102668, 1999: 103304, 2000: 105219, 2001: 102559, 2002: 103915, 2003: 105529, 2004: 104942, 2005: 105091, 2006: 105476, 2007: 109895, 2008: 107979, 2009: 108316, 2010: 109084, 2011: 111099, 2012: 116668, 2013: 111794, 2014: 113740, 2015: 121183, 2016: 118788, 2017: 124501, 2018: 120296, 2019: 124965, 2020: 131047, 2021: 143923, 2022: 139921, 2023: 127169, 2024: 125873, 2025: 120825}
    X = lambda y: 110 + (y - 1960) * 14.6
    Y = lambda v: 540 - v / 1000 * 2.6
    for v in (50, 100, 150):
        b += f'<line x1="{X(1960)}" y1="{Y(v*1000)}" x2="{X(2025)}" y2="{Y(v*1000)}" stroke="{LINE}" stroke-dasharray="5 6"/>' + T(X(1960) - 10, Y(v * 1000) + 6, f"{v}.000", 15, MUTE, "400", "end")
    for y in range(1960, 2026, 10):
        b += T(X(y), 572, str(y), 15, MUTE, "400", "middle")
    for d, c, lab, ly in ((births, BLUE, "γεννήσεις · births", 0), (deaths, RED, "θάνατοι · deaths", 0)):
        pts = " ".join(f"{X(y):.0f},{Y(v):.1f}" for y, v in sorted(d.items()))
        b += f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="4"/>'
    b += T(X(1962), Y(157239) - 14, "γεννήσεις · births", 18, BLUE, "700") + T(X(1962), Y(60563) + 30, "θάνατοι · deaths", 18, RED, "700")
    b += f'<line x1="{X(2011)}" y1="120" x2="{X(2011)}" y2="545" stroke="{GOLD}" stroke-width="2" stroke-dasharray="4 4"/>'
    b += T(X(2011) - 8, 140, "κάθε χρόνο από το 2011 οι θάνατοι", 16, GOLD, "700", "end") + T(X(2011) - 8, 162, "ξεπερνούν τις γεννήσεις", 16, GOLD, "700", "end")
    svg("esoterikes", h, b, "Γεννήσεις και θάνατοι, 1960–2025", "Live births and deaths in Greece each year")
    reg("esoterikes", "esoterikes", "Γεννήσεις και θάνατοι στην Ελλάδα: από το 2011 οι θάνατοι είναι κάθε χρόνο περισσότεροι από τις γεννήσεις.", "Births and deaths in Greece: deaths have outnumbered births every year since 2011.", "Eurostat (demo_gind), 2026")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    diakrisi(); anatheorisi(); proedros(); kyvernisi(); ekloges(); nomoi(); anexartites(); dimosio(); kathimerini(); aftodioikisi(); dikommatismos()
    hemicycle("katakermatismos", "Η Βουλή του Μαΐου 2012", "Seven parties and no majority: the election that broke the two-party system",
              [("ΚΚΕ", 26), ("ΣΥΡΙΖΑ", 52), ("ΔΗΜΑΡ", 19), ("ΠΑΣΟΚ", 41), ("ΝΔ", 108), ("ΑΝΕΛ", 33), ("Χρυσή Αυγή", 21)],
              "katakermatismos", "Οι έδρες μετά τις εκλογές της 6ης Μαΐου 2012: επτά κόμματα, καμία πλειοψηφία.", "Seats after the election of 6 May 2012: seven parties, no majority.")
    hemicycle("kommatiko-systima", "Η Βουλή του Ιουνίου 2023", "Seats won in the election of 25 June 2023",
              [("ΚΚΕ", 21), ("ΣΥΡΙΖΑ", 47), ("Πλεύση Ελευθερίας", 8), ("ΠΑΣΟΚ", 32), ("ΝΔ", 158), ("Ελληνική Λύση", 12), ("Νίκη", 10), ("Σπαρτιάτες", 12)],
              "kommatiko-systima", "Οι έδρες μετά τις εκλογές της 25ης Ιουνίου 2023 (η σύνθεση άλλαξε αργότερα).", "Seats after the election of 25 June 2023 (the make-up changed later).")
    mnimonia(); esoterikes()
    json.dump(IMAGES, open("/mnt/project-files/tools/politeia/diagrams.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(IMAGES), "diagrams")
