# Sources for the islands reader (library/nisia/). Paragraphs cite keys; build.py numbers them per chapter.
def wp(title, lang="en", label=None):
    from urllib.parse import quote
    return (f"Wikipedia ({'English' if lang == 'en' else 'Ελληνική'}), “{label or title}”", f"https://{lang}.wikipedia.org/wiki/" + quote(title.replace(" ", "_")))

SRC = {
    "elstat21": ("ΕΛΣΤΑΤ, Απογραφή Πληθυσμού-Κατοικιών 2021, μόνιμος πληθυσμός ανά δήμο και δημοτική ενότητα · Hellenic Statistical Authority, 2021 Population-Housing Census, permanent population by municipality", "https://www.statistics.gr/el/2021-census-pop-hous-results"),
    "islands_list": wp("List of islands of Greece"),
    "unesco": ("UNESCO World Heritage Centre, World Heritage List: Greece", "https://whc.unesco.org/en/statesparties/gr"),
    "unesco_ich": ("UNESCO Intangible Cultural Heritage, elements inscribed for Greece", "https://ich.unesco.org/en/state/greece-GR"),
    "eoppep_pdo": ("European Commission, eAmbrosia: the EU geographical indications register (PDO/PGI products of Greece)", "https://ec.europa.eu/agriculture/eambrosia/geographical-indications-register/"),
    "herodotus": ("Herodotus, Histories, book 8 (the battle of Salamis), trans. A. D. Godley, Perseus Digital Library", "https://www.perseus.tufts.edu/hopper/text?doc=Hdt.+8"),
    "clogg": ("R. Clogg, A Concise History of Greece, 4th ed., Cambridge University Press, 2021", None),
    "kremmydas": ("Β. Κρεμμυδάς, Ελληνική ναυτιλία 1776–1835, Εμπορική και Τεχνολογική Τράπεζα, 1985", None),
    "ypa_aigina": ("Υπουργείο Πολιτισμού, «Αίγινα: Ναός της Αφαίας» (Οδυσσέας, ιστότοπος αρχαιολογικών χώρων) · Ministry of Culture, Temple of Aphaia", "http://odysseus.culture.gr/h/3/gh351.jsp?obj_id=2375"),
    "nafsi": ("Ανεξάρτητη Αρχή Δημοσίων Εσόδων / Υπουργείο Ναυτιλίας, «Άγονες γραμμές»: ετήσιοι διαγωνισμοί για τις επιδοτούμενες ακτοπλοϊκές συνδέσεις · Ministry of Maritime Affairs, subsidised ferry routes", "https://www.ynanp.gr/el/"),
}
for k, t, lang in [
    ("wp_salamina", "Salamis Island", "en"), ("wp_aigina", "Aegina", "en"), ("wp_agistri", "Agistri", "en"),
    ("wp_ydra", "Hydra (island)", "en"), ("wp_spetses", "Spetses", "en"), ("wp_poros", "Poros", "en"),
    ("wp_saronic", "Saronic Islands", "en"), ("wp_battle_salamis", "Battle of Salamis", "en"),
    ("wp_kapodistrias", "Ioannis Kapodistrias", "en"), ("wp_phoenix", "Greek phoenix", "en"), ("wp_bouboulina", "Laskarina Bouboulina", "en"),
    ("wp_miaoulis", "Andreas Miaoulis", "en"), ("wp_arvanites", "Arvanites", "en"),
]:
    SRC[k] = wp(t, lang)
SRC.update({
    "thuc": ("Thucydides, History of the Peloponnesian War, trans. R. Crawley, Perseus Digital Library", "https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0200"),
    "ich_tinos": ("UNESCO Intangible Cultural Heritage, “Tinian marble craftsmanship” (inscribed 2015)", "https://ich.unesco.org/en/RL/tinian-marble-craftsmanship-01097"),
    "delos_unesco": ("UNESCO World Heritage Centre, “Delos” (inscribed 1990)", "https://whc.unesco.org/en/list/530/"),
    "louvre_venus": ("Musée du Louvre, “Aphrodite, known as the Venus de Milo”, collection record Ma 399", "https://collections.louvre.fr/en/ark:/53355/cl010277627"),
    "akrotiri": ("Υπουργείο Πολιτισμού, «Ακρωτήρι Θήρας» (Οδυσσέας) · Ministry of Culture, Akrotiri on Thera", "http://odysseus.culture.gr/h/3/gh351.jsp?obj_id=2410"),
    "doumas": ("Ch. Doumas, Thera: Pompeii of the Ancient Aegean, Thames & Hudson, 1983", None),
    "sigalas": ("H. Sigurdsson et al., “Marine investigations of Greece's Santorini volcanic field”, Eos 87(34), 2006", None),
    "santorini2025": ("Reuters, “Greece declares state of emergency on Santorini as earthquakes rattle island”, 6 February 2025", "https://www.reuters.com/world/europe/greece-declares-state-emergency-santorini-2025-02-06/"),
    "cruisefee": ("Πρώτο Θέμα (English edition), “In force from today, Monday 21 July, the per-passenger fee” for cruise visitors (€20 in Santorini and Mykonos, June–September), 21 July 2025", "https://origin01-en.protothema.gr/2025/07/21/in-force-from-today-monday-21-july-the-per-passenger-fee"),
    "pdo_list": ("Υπουργείο Αγροτικής Ανάπτυξης και Τροφίμων, Κατάλογος προϊόντων ΠΟΠ/ΠΓΕ · Ministry of Rural Development and Food, list of Greek PDO/PGI products", "https://www.minagric.gr/"),
    "babiniotis": ("Γ. Μπαμπινιώτης, Λεξικό της Νέας Ελληνικής Γλώσσας, 5η έκδ., Κέντρο Λεξικολογίας, 2019", None),
    "triantafyllidis": ("Λεξικό της Κοινής Νεοελληνικής (Ίδρυμα Μανόλη Τριανταφυλλίδη), Πύλη για την ελληνική γλώσσα", "https://www.greek-language.gr/greekLang/modern_greek/tools/lexica/triantafyllides/"),
    "parian_chronicle": ("Ashmolean Museum, Oxford, “The Parian Marble” (Marmor Parium), AN1667.14", "https://www.ashmolean.org/"),
    "hozoviotissa": ("Ιερά Μονή Παναγίας Χοζοβιώτισσας, Ιερά Μητρόπολις Θήρας, Αμοργού και Νήσων · Monastery of Hozoviotissa", "https://www.imthira.gr/"),
})

SRC.update({
    "herodotus3": ("Herodotus, Histories, book 3, ch. 60 (the three great works of Samos), trans. A. D. Godley, Perseus Digital Library", "https://www.perseus.tufts.edu/hopper/text?doc=Hdt.+3.60"),
    "herodotus6": ("Herodotus, Histories, book 6, ch. 46–47 (the gold mines of Thasos), trans. A. D. Godley, Perseus Digital Library", "https://www.perseus.tufts.edu/hopper/text?doc=Hdt.+6.47"),
})

SRC.update({
    "apollon_syros": ("ΣΚΑΪ, «Θέατρο Απόλλων: Το “στολίδι” της Ερμούπολης κουβαλάει μία ιδιαίτερη ιστορία» · Skai news on the Apollo Theatre of Ermoupoli (architect Pietro Sampo, 1864)", "https://www.skai.gr/news/culture/theatro-apollon-to-stolidi-tis-ermoupolis-kouvalaei-mia-idiaiteri-istoria"),
    "towel2023": ("Reuters, “Greeks protest for space on the beach as pricey sunbeds multiply”, 10 August 2023 (via The Star)", "https://www.thestar.com.my/news/world/2023/08/10/greeks-protest-for-space-on-the-beach-as-pricey-sunbeds-multiply"),
})
