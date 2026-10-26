# Sources for the diaspora reader (library/diaspora/). Paragraphs cite keys; build.py numbers them per chapter.
def wp(title, lang="en", label=None):
    from urllib.parse import quote
    return (f"Wikipedia ({'English' if lang == 'en' else 'Ελληνική'}), “{label or title}”", f"https://{lang}.wikipedia.org/wiki/" + quote(title.replace(" ", "_")))

SRC = {
    "clogg_diaspora": ("R. Clogg (ed.), The Greek Diaspora in the Twentieth Century, Macmillan, 1999", None),
    "clogg": ("R. Clogg, A Concise History of Greece, 4th ed., Cambridge University Press, 2021", None),
    "dalachanis": ("A. Dalachanis, The Greek Exodus from Egypt: Diaspora Politics and Emigration, 1937–1962, Berghahn, 2017 (introduction)", "https://mail.berghahnbooks.com/downloads/intros/DalachanisGreek_intro.pdf"),
    "kitroeff": ("A. Kitroeff, The Greeks and the Making of Modern Egypt, American University in Cairo Press, 2019", None),
    "moskos": ("C. C. Moskos, Greek Americans: Struggle and Success, 2nd ed., Transaction, 1989", None),
    "plato_phaedo": ("Plato, Phaedo 109b (“like ants or frogs about a pond”), trans. H. N. Fowler, Perseus Digital Library", "https://www.perseus.tufts.edu/hopper/text?doc=Plat.+Phaedo+109b"),
    "herodotus4": ("Herodotus, Histories, book 4, ch. 150–159 (the founding of Cyrene), trans. A. D. Godley, Perseus Digital Library", "https://www.perseus.tufts.edu/hopper/text?doc=Hdt.+4.150"),
    "marciana": ("Biblioteca Nazionale Marciana, Venice: history of the library and Bessarion's gift (1468)", "https://marciana.venezia.sbn.it/"),
    "hellenic_institute_venice": ("Ελληνικό Ινστιτούτο Βυζαντινών και Μεταβυζαντινών Σπουδών Βενετίας · Hellenic Institute of Byzantine and Post-Byzantine Studies, Venice", "https://www.istitutoellenico.org/"),
    "abs_2021": ("Australian Bureau of Statistics, 2021 Census: ancestry and language spoken at home (Greek)", "https://www.abs.gov.au/census"),
    "destatis": ("Statistisches Bundesamt (Destatis), foreign population by citizenship (Greek nationals in Germany)", "https://www.destatis.de/"),
    "census_us": ("U.S. Census Bureau, American Community Survey: people reporting Greek ancestry", "https://data.census.gov/"),
    "statcan": ("Statistics Canada, 2021 Census of Population: ethnic or cultural origin (Greek)", "https://www12.statcan.gc.ca/"),
    "law_pontic": ("Νόμος 2193/1994: «Καθιέρωση της 19ης Μαΐου ως ημέρας μνήμης για τη γενοκτονία των Ελλήνων στον Μικρασιατικό Πόντο» · Greek law 2193/1994 establishing 19 May as the day of remembrance", None),
    "ypes_vote": ("Υπουργείο Εσωτερικών, «Επιστολική ψήφος» · Ministry of the Interior, postal vote for Greeks abroad", "https://www.ypes.gr/"),
    "boe_braindrain": ("Τράπεζα της Ελλάδος, «Διαρροή εγκεφάλων: η ελληνική περίπτωση» · Bank of Greece, Economic Bulletin on the brain drain, 2016", "https://www.bankofgreece.gr/"),
    "kythera_quota": ("Kythera Family, “USA 1917–1924: immigration restriction laws”", "https://www.kythera-family.net/en/history/general-history/usa-1917-1924-immigration-restriction-laws"),
    "neoskosmos_greeklish": ("Neos Kosmos, on Greek-Australian “Greeklish” words", "https://neoskosmos.com/en/?p=31516"),
    "boell_greeks": ("Heinrich-Böll-Stiftung, Heimatkunde: Greek migrants in Germany", "https://heimatkunde.boell.de/en/node/1739"),
    "globalhistory_greeks": ("Global History Dialogues, “The Greek guest workers in West Germany in the 1960s”", "https://globalhistorydialogues.org/stories/the-greek-guest-workers-in-west-germany-in-the-1960s"),
    "standrews_protest": ("University of St Andrews, Greek–West German protest project: the early to mid 1960s", "https://gr-frg-protest.wp.st-andrews.ac.uk/21-2/early-to-mid-60s/"),
    "neoskosmos_pontic": ("Neos Kosmos, “Pontian Greek genocide remembered as communities honour victims and survivors”, 19 May 2026", "https://neoskosmos.com/en/2026/05/19/news/pontian-greek-genocide-remembered-as-communities-honour-victims-and-survivors/"),
    "deportation_ua": ("Deportation.org.ua, “Deportations of Pontian Greeks in 1949”", "https://deportation.org.ua/deportations-of-pontian-greeks-in-1949/"),
    "un_pontic": ("UN Commission on Human Rights, NGO written statement E/CN.4/1998/NGO/24 (Pontic Greeks from the former USSR)", "https://digitallibrary.un.org/record/250956/files/E_CN.4_1998_NGO_24-EN.pdf"),
    "un_istanbul": ("UN Human Rights Council, NGO written statement A/HRC/25/NGO/171 (the Greek Orthodox community of Istanbul)", "https://digitallibrary.un.org/record/783447/files/A_HRC_25_NGO_171-EN.pdf"),
    "tovima_istanbul": ("To Vima, “Greeks of Istanbul hold on to a fading legacy”", "https://www.tovima.com/stories/greeks-of-istanbul-hold-on-to-a-fading-legacy/"),
    "pecob_refugees": ("PECOB, “Socialist camp, USSR and Greek political refugees: an unsettled historical issue”", "https://pecob.net/Socialist-camp-USSR-Greek-Political-Refugees-unsettled-historical-issue"),
    "coe_refugees": ("Council of Europe, Parliamentary Assembly, Doc. 11356 (2007): political refugees from the Greek Civil War", "https://assembly.coe.int/Documents/WorkingDocs/2007/EDOC11356.pdf"),
    "umdiaspora_refugees": ("United Macedonian Diaspora, on the child refugees of the Greek Civil War and the 1982 repatriation rules", "https://umdiaspora.org/?p=1329"),
    "uinp_mariupol": ("Ukrainian Institute of National Memory, “Why is the deportation of Mariupol citizens a repeating of history?”", "https://uinp.gov.ua/informaciyni-materialy/rosiysko-ukrayinska-viyna-istorychnyy-kontekst/why-is-the-deportation-of-mariupol-citizens-a-repeating-of-history"),
    "minorityrights_greek": ("Minority Rights Group, “Greek speakers” in Italy", "https://minorityrights.org/communities/greek-speakers/"),
    "boe_427": ("Neos Kosmos (Greek edition), «Σχεδόν μισό εκατομμύριο Έλληνες έφυγαν», 4 Sept. 2016, on Bank of Greece figures for 2008–2016", "https://neoskosmos.com/el/2016/09/04/news/greece/σχεδόν-μισό-εκατομμύριο-έλληνες-έφυγ/"),
    "taxheaven_5g": ("Κώδικας Φορολογίας Εισοδήματος (ν. 4172/2013), άρθρο 5Γ, όπως προστέθηκε με τον ν. 4758/2020 · Income Tax Code, article 5C", "https://www.taxheaven.gr/law/4172/2013/arthro/5Γ"),
    "neoskosmos_postal": ("Neos Kosmos, “Papastergiadis backs the postal vote but wants more diaspora representation in the Hellenic Parliament”, 25 Feb. 2026", "https://neoskosmos.com/en/2026/02/25/news/diaspora/papastergiadis-backs-the-postal-vote-but-wants-more-diaspora-representation-in-the-hellenic-parliament/"),
    "neoskosmos_school": ("Neos Kosmos, “The next generation of Greek Australians love their heritage, but are they slowly losing their language?”, 15 Sept. 2020", "https://neoskosmos.com/en/2020/09/15/life/education/the-next-generation-of-greek-australians-love-their-heritage-but-are-they-slowly-losing-their-language/"),
    "greekreporter_wave": ("Greek Reporter, “Economic crisis marks 3rd emigration wave of Greeks”, 2 July 2016", "https://greekreporter.com/2016/07/02/economic-crisis-marks-3rd-emigration-wave-of-greeks/"),
    "csmonitor_braindrain": ("Christian Science Monitor, “Greece's crashing economy drives the young and educated towards the exits”, 28 July 2015", "https://www.csmonitor.com/World/Europe/2015/0728/Greece-s-crashing-economy-drives-the-young-and-educated-towards-the-exits"),
    "greekcitytimes_postal": ("Greek City Times, “Inclusion of postal voting for 800,000 Greeks abroad in elections”, 3 Dec. 2023", "https://greekcitytimes.com/2023/12/03/inclusion-of-postal-voting-for-800000-greeks-abroad-in-elections/"),
    "kge_cert": ("Κέντρο Ελληνικής Γλώσσας, «Πιστοποίηση Ελληνομάθειας» · Centre for the Greek Language, Certificate of Attainment in Greek", "https://www.greek-language.gr/certification/"),
}
for k, t, lang in []:
    SRC[k] = wp(t, lang)
