# Shared sources for the bilingual cookbook (library/kouzina/).
# Each part file defines PART and CHAPTERS; paragraphs are (el, en, [source keys]); build.py numbers the sources per chapter.
W = lambda t: "https://en.wikipedia.org/wiki/" + t
WEL = lambda t: "https://el.wikipedia.org/wiki/" + t
SRC = {
    # language and reference
    "triantafyllidis": ("Λεξικό της κοινής νεοελληνικής, Ινστιτούτο Νεοελληνικών Σπουδών (Ίδρυμα Μανόλη Τριανταφυλλίδη), στην Πύλη για την ελληνική γλώσσα · Dictionary of Standard Modern Greek (meanings and etymologies)", "https://www.greek-language.gr/greekLang/modern_greek/tools/lexica/triantafyllides/"),
    "holton": ("D. Holton, P. Mackridge, I. Philippaki-Warburton & V. Spyropoulos, Greek: A Comprehensive Grammar, 2nd ed., Routledge, 2012 (imperative, aspect, numerals and measure phrases)", None),
    "babiniotis": ("Γ. Μπαμπινιώτης, Λεξικό της νέας ελληνικής γλώσσας, 5η έκδ., Κέντρο Λεξικολογίας, 2019", None),
    # cookbooks and food history
    "tselementes": ("Ν. Τσελεμεντές, Οδηγός μαγειρικής και ζαχαροπλαστικής, Αθήνα, 1930 (πολλές επανεκδόσεις) · N. Tselementes, Guide to Cooking and Confectionery", None),
    "tselementes_w": ("Wikipedia, “Nikolaos Tselementes” (born Sifnos 1878, died 1958; Οδηγός Μαγειρικής magazine from 1910, cookbook 1930)", W("Nikolaos_Tselementes")),
    "kochilas": ("D. Kochilas, The Glorious Foods of Greece: Traditional Recipes from the Islands, Cities, and Villages, William Morrow, 2001", None),
    "kremezi": ("A. Kremezi, The Foods of Greece, Stewart, Tabori & Chang, 1993", None),
    "dalby": ("A. Dalby, Siren Feasts: A History of Food and Gastronomy in Greece, Routledge, 1996", None),
    "dalby_byz": ("A. Dalby, Flavours of Byzantium, Prospect Books, 2003", None),
    "wilkins": ("J. Wilkins & S. Hill, Food in the Ancient World, Blackwell, 2006", None),
    "greek_cuisine": ("Wikipedia, “Greek cuisine”", W("Greek_cuisine")),
    "ancient_cuisine": ("Wikipedia, “Ancient Greek cuisine”", W("Ancient_Greek_cuisine")),
    "fava_w": ("Wikipedia, “Fava Santorinis” (Lathyrus clymenum; found in jars at Akrotiri, c. 1600 BC)", W("Fava_Santorinis")),
    "spoon_w": ("Wikipedia, “Spoon sweets”", W("Spoon_sweets")),
    "fasting_w": ("Wikipedia, “Fasting in Eastern Orthodoxy” and “Clean Monday”", W("Clean_Monday")),
    "feta_w": ("Wikipedia, “Feta” (PDO 2002, upheld by the EU Court of Justice 2005; sheep's milk with up to 30% goat's milk; mainland Greece and Lesbos)", W("Feta")),
    "paximadi_w": ("Wikipedia, “Paximathia”", W("Paximathia")),
    "cretan_w": ("Wikipedia, “Cretan cuisine”", W("Cretan_cuisine")),
    "dakos_w": ("Wikipedia, “Dakos” (barley rusk, tomato, mizithra or feta; also called koukouvagia)", W("Dakos")),
    "kalitsounia_w": ("Wikipedia, “Kalitsounia”", W("Kalitsounia")),
    "psilakis": ("Μ. & Ν. Ψιλάκης, Κρητική παραδοσιακή κουζίνα, Καρμάνωρ, Ηράκλειο, 2001 · M. & N. Psilakis, Cretan Traditional Cuisine", None),
    "keys1970": ("A. Keys (ed.), “Coronary heart disease in seven countries”, Circulation 41 (Suppl. I), 1970", "https://doi.org/10.1161/01.CIR.41.4S1.I-1"),
    "seven_w": ("Wikipedia, “Seven Countries Study” (16 cohorts, 12,763 men aged 40–59, entry exams 1958–1964; two Greek cohorts)", W("Seven_Countries_Study")),
    "eambrosia": ("European Commission, eAmbrosia: the EU geographical indications register (PDO/PGI entries for Greece)", "https://ec.europa.eu/agriculture/eambrosia/geographical-indications-register/"),
    "visitgreece_pdo": ("Visit Greece (Greek National Tourism Organisation), “Select Protected Designation of Origin products”", "https://www.visitgreece.gr/en/experiences/nature/culture/select-protected-designation-of-origin-products"),
    "esifnos": ("e-sifnos.com, “Traditional dishes of Sifnos and wine production” (revithada baked overnight in clay pots in wood-fired ovens)", "https://it.e-sifnos.com/what-to-do-in-sifnos/sifnos-food-wine.php"),
    "karpathos_vg": ("Visit Greece, “Flavours of Karpathos: local produce and traditional recipes”", "https://www.visitgreece.gr/en/experiences/nature/culture/flavours-of-karpathos"),
    "makarounes_vima": ("To Vima, “Greek island pasta: 3 traditional recipes to try at home”", "https://www.tovima.com/food/greek-island-pasta-3-traditional-recipes-to-try-at-home/"),
    "kalloni_gct": ("Greek City Times, “Lesvos: the Kalloni sardine will be included in the Protected Designation of Origin products” (16 September 2023)", "https://greekcitytimes.com/2023/09/16/lesvian-kalloni-sardine-protected/"),
    "sardeles_lesvos": ("lesvos.com, “Sardeles pastes” (salted raw on the boat, eaten the same day with ouzo)", "https://lesvos.com/sardeles-pastes/index.html"),
    "ouzo_w": ("Wikipedia, “Ouzo” (EU geographical indication for Greece and Cyprus since 2006; Lesbos and Plomari)", W("Ouzo")),
    "santorini_w": ("Wikipedia, “Santorini” (volcanic soils, Minoan eruption, Akrotiri)", W("Santorini")),
    "corfu_w": ("Wikipedia, “Corfu” (Venetian rule 1386–1797, British protectorate 1815–1864; cuisine: pastitsada, sofrito, bourdeto)", W("Corfu")),
    "pastitsada_w": ("Wikipedia, “Pastitsada” (from Venetian pastizzada; Corfu Sunday dish; no garlic in the Corfu version)", W("Pastitsada")),
    "stifado_w": ("Wikipedia, “Greek cuisine”, on stifado (from Italian stufato; rabbit, hare, beef, octopus, with baby onions, wine or vinegar)", W("Greek_cuisine")),
    "diples_w": ("Wikipedia, “Diples” (Peloponnese; weddings and New Year; fried dough folded in hot oil, dipped in honey syrup)", W("Diples")),
}
