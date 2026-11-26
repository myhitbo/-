# -*- coding: utf-8 -*-
"""
« Chnayim mikra : les halakhot » (demande du propriétaire, 26/11/2026 : « Fais un recueil
d'halachot pour shnem mikra »), le recueil de l'application Shnayim Mikra.

Repris du projet My Hitbodedut (docs/09-cahier-de-reprise.md § 5 et 7), où il était un livre de
la bibliothèque ; ici le livre est écrit seul, dans data/livre_chnayim_mikra.json.

Chaque halakha repose sur des sources lues le 26/11/2026, citées mot pour mot en hébreu. Le recueil
a d'abord eu 31 halakhot ; à la demande du propriétaire (« Enrichi les halachot ils Yen a beaucoup
plus que 31 », 26/11/2026), il a été enrichi de tout ce que ces sources disent d'autre sur le sujet :
  - Choul'han Aroukh O.H. 285 (et 139, 146, 553) avec les gloses du Rema, Taz, Cha'arei Techouva —
    « Maginei Eretz: Shulchan Aruch Orach Chaim, Lemberg, 1893 » (API Sefaria), Public Domain ;
  - Maguen Avraham, Baèr Hétev (Torat Emet 357), Eliya Rabba (Sulzbach 1757), 'Hayé Adam
    (Vilna 1844) — API Sefaria, Public Domain ;
  - Michna Beroura 285 et 669:4 — « On Your Way » ; Béour Halakha 285 et 494 — « Biur Halacha »
    (API Sefaria), Public Domain ;
  - Kaf ha'Haïm O.H. 285 (et 25, 128, 496, 553) — « Kaf Hachayim, Orach Chayim vol. I-IV » et
    « vol. V-VIII, Jerusalem 1910-1933 » (API Sefaria), Public Domain ;
  - Kitsour Choul'han Aroukh 72, 125, 219 — « Torat Emet 357 » (API Sefaria), Public Domain ;
  - Ben Ich 'Haï — « Ben Ish Hai -- Wikisource » (API Sefaria), Public Domain, l'édition du
    Ben Ich 'Haï de My Hitbodedut ; le 'Hida, Moré beEtsba (Livourne 1842) et Tsiporen Chamir
    (Presbourg 1859) ; Séfer 'Hassidim (Zhitomir 1857) — API Sefaria, Public Domain ;
  - Choul'han Aroukh Y.D. 400:1, Chakh, Rabbi Akiva Eiger — « Ashlei Ravrevei: Shulchan Aruch
    Yoreh Deah, Lemberg, 1888 » (API Sefaria), Public Domain ;
  - Rambam, Hilkhot Tefila 13:25 — « Torat Emet 370 » (API Sefaria), Public Domain ;
  - Choul'han Aroukh haRav O.H. 285 — « Kehot Publication Society » (API Sefaria), CC-BY-NC :
    citations courtes, sans la vocalisation, créditées dans le livre (application gratuite) ;
  - Aroukh haChoul'han O.H. 285 et 139 — « Arukh HaShulchan, Orach Chayim -- Wikisource »
    (API Sefaria), CC-BY-SA : texte de 1903-1907, dans le domaine public ; saisie et ponctuation
    de Wikisource : citations courtes, créditées dans le livre ;
  - Kitsour Choul'han Aroukh Yalkout Yossef, siman 285 — l'édition de My Hitbodedut
    (livre_yalkut_yosef_kitsour.json : Torat Emet, mahadoura 5767, CC BY-NC-SA 2.5, crédit
    « הרב יצחק יוסף שליט״א »). Licence reçue par le propriétaire le 19/10/2026 pour My Hitbodedut ;
    le propriétaire confirme le 26/11/2026 qu'elle est déjà vérifiée (« licence du Kitsour Yalkout
    Yossef. Déjà vérifié sur le projet my hitbodedut »). Ce livre entier n'est pas dans ce dépôt :
    --verifie le lit dans le fichier donné par --yalkut (voir plus bas), sinon ses citations sont
    notées « non relues ».

Sources d'aujourd'hui (demande du propriétaire transmise le 26/11/2026) : réponses de
Hidabroot (« שאל את הרב »), de Kav haHalakha haSefaradi (kavhalacha.co.il), du beit hora'a
« Halakha lema'assé » du Rav Ofir Malka (hl5047.co.il) et du Rav Binyamin 'Hota (« הלכה ב-60
שניות », Kikar haChabbat, kikar.co.il : les deux réponses dont la page donne le texte ; ses
autres réponses sur le sujet sont en vidéo seulement et ne sont pas reprises). Œuvres
protégées : rien n'en est recopié ; chaque réponse est résumée, attribuée (auteur, titre,
date, adresse), avec au plus une courte phrase citée.

Pas de psak : chaque halakha dit qui tient quoi ; « rite » dit à qui elle s'adresse
(tous, sefarade = rite Edot, ashkenaze = rites Ashkenaz et Sfard).

Sorties :
  - data/livre_chnayim_mikra.json : le livre, avec ses sources et licences dans son « _meta »
    (tools/construit_donnees.js en tire web/data/halakhot.js) ;
  - tools/chnayim_mikra/sources.json : la table de vérification (référence, adresse lue,
    citation hébraïque exacte ou passage résumé), pour le relecteur.

  python3 tools/chnayim_mikra/construction.py            # écrit le livre et la table
  python3 tools/chnayim_mikra/construction.py --verifie  # relit chaque citation à sa source
  python3 tools/chnayim_mikra/construction.py --verifie --yalkut <livre_yalkut_yosef_kitsour.json>

Le fichier du Yalkout Yossef se prend dans l'archive de My Hitbodedut :
  git fetch https://github.com/myhitbo/MyHitbodedut.git claude/halakhot-chnayim-mikra
  git show FETCH_HEAD:android/app/src/main/res/raw/livre_yalkut_yosef_kitsour.json > /tmp/kyy.json
"""
import html
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.normpath(os.path.join(ICI, "..", ".."))
LIVRE = os.path.join(RACINE, "data", "livre_chnayim_mikra.json")
# Le Kitsour Yalkout Yossef entier n'est pas dans ce dépôt : --yalkut <fichier> pour relire ses citations.
YALKUT = sys.argv[sys.argv.index("--yalkut") + 1] if "--yalkut" in sys.argv else None
TABLE = os.path.join(ICI, "sources.json")
DATE = "26/11/2026"

# --- Les éditions -----------------------------------------------------------------------------

EDITIONS = {
    "ber": {"titre": "Talmud Bavli, Berakhot 8a-b (texte cité par le Kaf ha'Haïm 285:1)",
            "edition": "Kaf Hachayim, Orach Chayim vol. I-IV, Jerusalem 1910-1933", "licence": "Public Domain",
            "verifie_aussi": "Wikisource Talmud Bavli (Sefaria, CC-BY-SA), Berakhot 8a:30 et 8b:1, lu le 26/11/2026"},
    "sa": {"titre": "Choul'han Aroukh, Ora'h 'Haïm", "edition": "Maginei Eretz: Shulchan Aruch Orach Chaim, Lemberg, 1893", "licence": "Public Domain"},
    "rema": {"titre": "Rema (gloses du Choul'han Aroukh), Ora'h 'Haïm", "edition": "Maginei Eretz: Shulchan Aruch Orach Chaim, Lemberg, 1893", "licence": "Public Domain"},
    "mb": {"titre": "Michna Beroura", "edition": "On Your Way", "licence": "Public Domain"},
    "kh": {"titre": "Kaf ha'Haïm, Ora'h 'Haïm", "edition": "Kaf Hachayim, Orach Chayim vol. I-IV, Jerusalem 1910-1933", "licence": "Public Domain"},
    "ksa": {"titre": "Kitsour Choul'han Aroukh", "edition": "Torat Emet 357", "licence": "Public Domain"},
    "bih": {"titre": "Ben Ich 'Haï, Halakhot", "edition": "Ben Ish Hai -- Wikisource", "licence": "Public Domain"},
    "rambam": {"titre": "Rambam, Michné Torah, Hilkhot Tefila", "edition": "Torat Emet 370", "licence": "Public Domain"},
    "sahr": {"titre": "Choul'han Aroukh haRav, Ora'h 'Haïm", "edition": "Kehot Publication Society", "licence": "CC-BY-NC",
             "note": "Texte de 1814 ; saisie de Kehot sous CC-BY-NC : courtes citations sans vocalisation, créditées en tête du livre ; application gratuite, sans publicité ni achat."},
    "kyy": {"titre": "Kitsour Choul'han Aroukh Yalkout Yossef, Rav Yitzhak Yosef chlita",
            "edition": "Torat Emet, mahadoura 5767 — la copie de My Hitbodedut (livre_yalkut_yosef_kitsour.json, section « סימן רפה »)",
            "licence": "CC BY-NC-SA 2.5, licence publique de Torat Emet (toratemetfreeware.com/contents/copyrights2.html, lu le 26/11/2026) ; crédit « הרב יצחק יוסף שליט״א »"},
    "bh": {"titre": "Béour Halakha (Michna Beroura)", "edition": "Biur Halacha", "licence": "Public Domain"},
    "ma": {"titre": "Maguen Avraham", "edition": "Magen Avraham", "licence": "Public Domain"},
    "taz": {"titre": "Taz (Tourei Zahav), Ora'h 'Haïm", "edition": "Maginei Eretz: Shulchan Aruch Orach Chaim, Lemberg, 1893", "licence": "Public Domain"},
    "bht": {"titre": "Baèr Hétev, Ora'h 'Haïm", "edition": "Torat Emet 357", "licence": "Public Domain"},
    "sht": {"titre": "Cha'arei Techouva, Ora'h 'Haïm", "edition": "Maginei Eretz: Shulchan Aruch Orach Chaim, Lemberg, 1893", "licence": "Public Domain"},
    "er": {"titre": "Eliya Rabba, Ora'h 'Haïm", "edition": "Eliya Rabba, Sulzbach 1757", "licence": "Public Domain"},
    "ha": {"titre": "'Hayé Adam, Hilkhot Chabbat", "edition": "Chayei Adam, Vilna, 1844", "licence": "Public Domain"},
    "ahs": {"titre": "Aroukh haChoul'han, Ora'h 'Haïm", "edition": "Arukh HaShulchan, Orach Chayim -- Wikisource", "licence": "CC-BY-SA",
            "note": "Texte de 1903-1907, dans le domaine public ; saisie et ponctuation de Wikisource sous CC-BY-SA : courtes citations, créditées en tête du livre."},
    "sayd": {"titre": "Choul'han Aroukh, Yoré Déa", "edition": "Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888", "licence": "Public Domain"},
    "shakh": {"titre": "Chakh (Siftei Cohen), Yoré Déa", "edition": "Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888", "licence": "Public Domain"},
    "rae": {"titre": "Rabbi Akiva Eiger, gloses du Yoré Déa", "edition": "Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888", "licence": "Public Domain"},
    "sch": {"titre": "Séfer 'Hassidim", "edition": "Sefer Chassidim, Zhitomir, 1857", "licence": "Public Domain"},
    "mbe": {"titre": "Moré beEtsba, du 'Hida", "edition": "Moreh BeEtzba, Livorno, 1842", "licence": "Public Domain"},
    "tsh": {"titre": "Tsiporen Chamir, du 'Hida", "edition": "Avodat HaKodesh, Pressburg, 1859", "licence": "Public Domain"},
    "hid": {"titre": "Hidabroot, « שאל את הרב »", "edition": "hidabroot.org", "licence": "Tous droits réservés : résumé et référence, au plus une courte phrase citée"},
    "kav": {"titre": "Kav haHalakha haSefaradi (קו ההלכה הספרדי)", "edition": "kavhalacha.co.il", "licence": "Tous droits réservés : résumé et référence, au plus une courte phrase citée"},
    "malka": {"titre": "Beit hora'a « Halakha lema'assé » du Rav Ofir Malka (הלכה למעשה)", "edition": "hl5047.co.il", "licence": "Tous droits réservés : résumé et référence, au plus une courte phrase citée"},
    "kikar": {"titre": "Kikar haChabbat, « הלכה ב-60 שניות », Rav Binyamin 'Hota (כיכר השבת)", "edition": "kikar.co.il", "licence": "Tous droits réservés : résumé et référence, au plus une courte phrase citée"},
}

# Les livres classiques. {s} et {n} : siman et paragraphe en chiffres ; {S} et {N} : en lettres.
# « siman » : celui que R(source, n) sous-entend ; R(source, (siman, n)) en nomme un autre ; sans « siman »,
# le livre n'a qu'un niveau. « sefaria » : la référence lue à l'API Sefaria, dans l'édition « version »
# (le Kitsour Yalkout Yossef n'y est pas : il se lit dans le fichier donné par --yalkut).
MAGINEI = "Maginei Eretz: Shulchan Aruch Orach Chaim, Lemberg, 1893"
ASHLEI = "Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888"
KAF_1 = "Kaf Hachayim, Orach Chayim vol. I-IV, Jerusalem 1910-1933"
KAF_2 = "Kaf Hachayim, Orach Chayim vol. V-VIII, Jerusalem 1910-1933"
BIH_VERSION = "Ben Ish Hai -- Wikisource"
CLASSIQUES = {
    "ber": {"siman": 285, "sefaria": "Kaf HaChayim on Shulchan Arukh, Orach Chayim {s}:{n}", "version": KAF_1},
    "sa": {"siman": 285, "sefaria": "Shulchan Arukh, Orach Chayim {s}:{n}", "version": MAGINEI,
           "fr": "Choul’han Aroukh O.H. {s}:{n}", "en": "Shulchan Aruch O.C. {s}:{n}", "he": "שולחן ערוך או״ח {S}, {N}"},
    "rema": {"siman": 285, "sefaria": "Shulchan Arukh, Orach Chayim {s}:{n}", "version": MAGINEI,
             "fr": "Rema O.H. {s}:{n}", "en": "Rema O.C. {s}:{n}", "he": "רמ״א או״ח {S}, {N}"},
    "mb": {"siman": 285, "sefaria": "Mishnah Berurah {s}:{n}", "version": "On Your Way",
           "fr": "Michna Beroura {s}:{n}", "en": "Mishnah Berurah {s}:{n}", "he": "משנה ברורה {S}, ס״ק {N}"},
    "bh": {"siman": 285, "sefaria": "Biur Halacha {s}:{n}", "version": "Biur Halacha",
           "fr": "Béour Halakha {s}:{n}", "en": "Beur Halacha {s}:{n}", "he": "ביאור הלכה {S}, סעיף {N}"},
    "kh": {"siman": 285, "sefaria": "Kaf HaChayim on Shulchan Arukh, Orach Chayim {s}:{n}", "version": KAF_1, "versions": {496: KAF_2, 553: KAF_2},
           "fr": "Kaf ha’Haïm {s}:{n}", "en": "Kaf HaChaim {s}:{n}", "he": "כף החיים {S}, אות {N}"},
    "ksa": {"siman": 72, "sefaria": "Kitzur Shulchan Arukh {s}:{n}", "version": "Torat Emet 357",
            "fr": "Kitsour Choul’han Aroukh {s}:{n}", "en": "Kitzur Shulchan Aruch {s}:{n}", "he": "קיצור שולחן ערוך {S}, {N}"},
    "rambam": {"siman": 13, "sefaria": "Mishneh Torah, Prayer and the Priestly Blessing {s}:{n}", "version": "Torat Emet 370",
               "fr": "Rambam, Hilkhot Tefila {s}:{n}", "en": "Rambam, Hilchot Tefillah {s}:{n}", "he": "רמב״ם, הלכות תפילה {S}, {N}"},
    "sahr": {"siman": 285, "sefaria": "Shulchan Arukh HaRav, Orach Chayim {s}:{n}", "version": "Kehot Publication Society",
             "fr": "Choul’han Aroukh haRav O.H. {s}:{n}", "en": "Shulchan Aruch HaRav O.C. {s}:{n}", "he": "שולחן ערוך הרב או״ח {S}, {N}"},
    "kyy": {"siman": 285,
            "fr": "Kitsour Yalkout Yossef {s}:{n}", "en": "Kitzur Yalkut Yosef {s}:{n}", "he": "ילקוט יוסף, קיצור שולחן ערוך {S}, {N}"},
    "ma": {"siman": 285, "sefaria": "Magen Avraham {s}:{n}", "version": "Magen Avraham",
           "fr": "Maguen Avraham {s}:{n}", "en": "Magen Avraham {s}:{n}", "he": "מגן אברהם {S}, ס״ק {N}"},
    "taz": {"siman": 285, "sefaria": "Turei Zahav on Shulchan Arukh, Orach Chayim {s}:{n}", "version": MAGINEI,
            "fr": "Taz O.H. {s}:{n}", "en": "Taz O.C. {s}:{n}", "he": "ט״ז או״ח {S}, ס״ק {N}"},
    "bht": {"siman": 285, "sefaria": "Ba'er Hetev on Shulchan Arukh, Orach Chayim {s}:{n}", "version": "Torat Emet 357",
            "fr": "Baèr Hétev O.H. {s}:{n}", "en": "Ba’er Hetev O.C. {s}:{n}", "he": "באר היטב או״ח {S}, ס״ק {N}"},
    "sht": {"siman": 285, "sefaria": "Sha'arei Teshuvah on Shulchan Arukh, Orach Chayim {s}:{n}", "version": MAGINEI,
            "fr": "Cha’arei Techouva O.H. {s}:{n}", "en": "Sha’arei Teshuvah O.C. {s}:{n}", "he": "שערי תשובה או״ח {S}, ס״ק {N}"},
    "er": {"siman": 285, "sefaria": "Eliyah Rabbah on Shulchan Arukh, Orach Chayim {s}:{n}", "version": "Eliya Rabba, Sulzbach 1757",
           "fr": "Eliya Rabba {s}:{n}", "en": "Eliyah Rabbah {s}:{n}", "he": "אליה רבה {S}, ס״ק {N}"},
    "ha": {"siman": 7, "sefaria": "Chayyei Adam, Shabbat and Festivals {s}:{n}", "version": "Chayei Adam, Vilna, 1844",
           "fr": "’Hayé Adam, Chabbat {s}:{n}", "en": "Chayei Adam, Shabbat {s}:{n}", "he": "חיי אדם, הלכות שבת, כלל {S}, {N}"},
    "ahs": {"siman": 285, "sefaria": "Arukh HaShulchan, Orach Chaim {s}:{n}", "version": "Arukh HaShulchan, Orach Chayim -- Wikisource",
            "fr": "Aroukh haChoul’han O.H. {s}:{n}", "en": "Aruch HaShulchan O.C. {s}:{n}", "he": "ערוך השולחן או״ח {S}, סעיף {N}"},
    "sayd": {"siman": 400, "sefaria": "Shulchan Arukh, Yoreh De'ah {s}:{n}", "version": ASHLEI,
             "fr": "Choul’han Aroukh Y.D. {s}:{n}", "en": "Shulchan Aruch Y.D. {s}:{n}", "he": "שולחן ערוך יו״ד {S}, {N}"},
    "shakh": {"siman": 400, "sefaria": "Siftei Kohen on Shulchan Arukh, Yoreh De'ah {s}:{n}", "version": ASHLEI,
              "fr": "Chakh Y.D. {s}:{n}", "en": "Shach Y.D. {s}:{n}", "he": "ש״ך יו״ד {S}, ס״ק {N}"},
    "rae": {"siman": 400, "sefaria": "Rabbi Akiva Eiger on Shulchan Arukh, Yoreh De'ah {s}:{n}", "version": ASHLEI,
            "fr": "Rabbi Akiva Eiger Y.D. {s}:{n}", "en": "Rabbi Akiva Eiger Y.D. {s}:{n}", "he": "רבי עקיבא איגר יו״ד {S}, {N}"},
    "sch": {"sefaria": "Sefer Chasidim {n}", "version": "Sefer Chassidim, Zhitomir, 1857",
            "fr": "Séfer ’Hassidim {n}", "en": "Sefer Chasidim {n}", "he": "ספר חסידים, סימן {N}"},
    "mbe": {"sefaria": "Moreh BeEtzba {n}", "version": "Moreh BeEtzba, Livorno, 1842",
            "fr": "Moré beEtsba (’Hida) §{n}", "en": "Moreh BeEtzba (Chida) §{n}", "he": "מורה באצבע לחיד״א, אות {N}"},
    "tsh": {"sefaria": "Tziporen Shamir {n}", "version": "Avodat HaKodesh, Pressburg, 1859",
            "fr": "Tsiporen Chamir (’Hida) §{n}", "en": "Tziporen Shamir (Chida) §{n}", "he": "צפורן שמיר לחיד״א, אות {N}"},
}


def lieu(r):
    """(siman, paragraphe) d'une référence classique ; siman None pour un livre à un seul niveau."""
    n = r["num"]
    return n if isinstance(n, tuple) else (CLASSIQUES[r["src"]].get("siman"), n)


# Les réponses d'aujourd'hui : auteur, titre, date, adresse.
MODERNES = {
    ("hid", "221007"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "הלכה לגבי קריאת שניים מקרא ואחד תרגום", "date": "23/01/2017", "date_he": "כ״ה טבת התשע״ז"},
    ("hid", "262007"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "הלכות שניים מקרא ואחד תרגום", "date": "14/03/2019", "date_he": "ז׳ אדר ב׳ התשע״ט"},
    ("hid", "262097"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "האם גם נשים חייבות בשניים מקרא ואחד תרגום?", "date": "17/03/2019", "date_he": "י׳ אדר ב׳ התשע״ט"},
    ("hid", "253987"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "האם חולה יכול לשמוע שניים מקרא ואחד תרגום מאשתו?", "date": "01/10/2018", "date_he": "כ״ב תשרי התשע״ט"},
    ("hid", "299490"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "איך לקרוא שניים מקרא אחד תרגום?", "date": "13/12/2021", "date_he": "ט׳ טבת התשפ״ב"},
    ("hid", "301252"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "לגבי שניים מקרא ואחד תרגום", "date": "11/02/2022", "date_he": "י׳ אדר א׳ התשפ״ב"},
    ("hid", "303250"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "פרשות השבוע, שניים מקרא ואחד תרגום", "date": "11/04/2022", "date_he": "י׳ ניסן התשפ״ב"},
    ("hid", "354076"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "קריאת שניים מקרא ואחד תרגום", "date": "08/08/2025", "date_he": "י״ד אב התשפ״ה"},
    ("hid", "354260"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "שניים מקרא", "date": "21/08/2025", "date_he": "כ״ז אב התשפ״ה"},
    ("hid", "15385"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "שניים מקרא ואחד תרגום וטעמים", "date": "25/02/2014", "date_he": "כ״ה אדר א׳ התשע״ד"},
    ("kav", "yaron1"): {"auteur": "Rav Yaron Achkenazi", "auteur_court": "Rav Y. Achkenazi", "auteur_he": "הרב ירון אשכנזי", "titre": "הלכה יומית - הרב ירון אשכנזי - שנים מקרא ואחד תרגום", "date": "13/07/2017", "date_he": "י״ט תמוז התשע״ז",
                        "url": "https://kavhalacha.co.il/%D7%90%D7%A7%D7%98%D7%95%D7%90%D7%9C%D7%99%D7%94-%D7%91%D7%94%D7%9C%D7%9B%D7%94/%D7%9E%D7%90%D7%92%D7%A8-%D7%94%D7%94%D7%9C%D7%9B%D7%95%D7%AA/%D7%A7%D7%A8%D7%99%D7%90%D7%AA-%D7%94%D7%AA%D7%95%D7%A8%D7%94/2017-05-30-05-42-86"},
    ("kav", "yaron2"): {"auteur": "Rav Yaron Achkenazi", "auteur_court": "Rav Y. Achkenazi", "auteur_he": "הרב ירון אשכנזי", "titre": "הלכה יומית - הרב ירון אשכנזי - המשך דיני הפטרה וחיוב לומר שניים מקרא", "date": "07/06/2017", "date_he": "י״ג סיון התשע״ז",
                        "url": "https://kavhalacha.co.il/%D7%90%D7%A7%D7%98%D7%95%D7%90%D7%9C%D7%99%D7%94-%D7%91%D7%94%D7%9C%D7%9B%D7%94/%D7%9E%D7%90%D7%92%D7%A8-%D7%94%D7%94%D7%9C%D7%9B%D7%95%D7%AA/%D7%A7%D7%A8%D7%99%D7%90%D7%AA-%D7%94%D7%AA%D7%95%D7%A8%D7%94/2017-05-30-05-42-81"},
    ("kav", "azoulay"): {"auteur": "Rav Ochri Azoulay", "auteur_court": "Rav O. Azoulay", "auteur_he": "הרב אושרי אזולאי", "titre": "האם מותר לקרוא שניים מקרא ואחד תרגום בלילה?", "date": "13/01/2023", "date_he": "כ׳ טבת התשפ״ג",
                         "url": "https://kavhalacha.co.il/%D7%90%D7%A7%D7%98%D7%95%D7%90%D7%9C%D7%99%D7%94-%D7%91%D7%94%D7%9C%D7%9B%D7%94/%D7%94%D7%9C%D7%9B%D7%95%D7%AA-%D7%9E%D7%A2%D7%A0%D7%99%D7%99%D7%A0%D7%95%D7%AA/%D7%9E%D7%94-%D7%93%D7%99%D7%A0%D7%94-%D7%A9%D7%9C-%D7%97%D7%9C%D7%94-%D7%97%D7%AA%D7%95%D7%9B%D7%94-%D7%A9%D7%94%D7%99%D7%AA%D7%94-%D7%A2%D7%9C-%D7%A9%D7%95%D7%9C%D7%97%D7%9F-%D7%A9%D7%A0%D7%90%D7%9B%D7%9C-%D7%91%D7%95-%D7%91%D7%A9%D7%A8%D7%99,-%D7%94%D7%90%D7%9D-%D7%A0%D7%99%D7%AA%D7%9F-%D7%9C%D7%90%D7%9B%D7%95%D7%9C-%D7%9E%D7%9E%D7%A0%D7%94-%D7%A2%D7%9D-%D7%97%D7%9C%D7%91%D7%99-2"},
    ("malka", "142"): {"auteur": "Rav Menaché Moreno", "auteur_court": "Rav M. Moreno", "auteur_he": "הרב מנשה מורנו", "titre": "פרשת וזאת הברכה בתיקון קורא אחד", "date": "12/10/2025", "date_he": "12.10.2025"},
    ("kikar", "t409fv"): {"auteur": "Rav Binyamin 'Hota", "auteur_court": "Rav B. 'Hota", "auteur_he": "הרב בנימין חותה", "titre": "מתי סוף זמן קריאת 'שניים מקרא ואחד תרגום' של השנה?", "date": "12/10/2025", "date_he": "כ׳ תשרי התשפ״ו"},
    ("kikar", "sxoq8i"): {"auteur": "Rav Binyamin 'Hota", "auteur_court": "Rav B. 'Hota", "auteur_he": "הרב בנימין חותה", "titre": "האם יוצא ידי מצוות 'הכנה לשבת' בקריאת 'שניים מקרא ואחד תרגום'?", "date": "13/06/2025", "date_he": "י״ז סיון התשפ״ה"},
    ("malka", "484"): {"auteur": "Rav Emmanuel Molkandov", "auteur_court": "Rav E. Molkandov", "auteur_he": "הרב עמנואל מולקנדוב", "titre": "מכשיר אלקטרוני עם ספרי קודש", "date": "22/09/2026", "date_he": "22.09.2026"},
}


def url_moderne(src, n):
    if src == "hid":
        return f"https://www.hidabroot.org/question/{n}"
    if src == "malka":
        return f"https://hl5047.co.il/questions/{n}"
    if src == "kikar":
        return f"https://www.kikar.co.il/629/{n}"
    return MODERNES[(src, n)]["url"]


# --- Les nombres en lettres (Reference.lettres, sans le tour de 15 et 16 oublié) -------------

def lettres(n, geresh=True):
    u, d, c = " אבגדהוזחט", " יכלמנסעפצ", " קרשת"
    b, r = "", n
    while r >= 400:
        b += "ת"; r -= 400
    if r >= 100:
        b += c[r // 100]; r %= 100
    if r == 15:
        b += "טו"
    elif r == 16:
        b += "טז"
    else:
        if r >= 10:
            b += d[r // 10]
        if r % 10:
            b += u[r % 10]
    if not geresh:
        return b
    return b + "׳" if len(b) == 1 else b[:-1] + "״" + b[-1]


# --- Une référence ------------------------------------------------------------------------------
# R(source, numéro, cite=…) : numéro du se'if, de l'os ou de la question ; pour le Ben Ich 'Haï,
# (année, paracha anglaise de Sefaria, paracha française, paracha hébraïque, paragraphe).

def R(src, num, cite=None, passage=None):
    return {"src": src, "num": num, "cite": cite, "passage": passage}


BIH_ANNEE = {1: ("1st Year", "1re", "1st", "שנה א׳"), 2: ("2nd Year", "2e", "2nd", "שנה ב׳")}


def ref_texte(r, langue):
    """La référence d'une source, seule, dans la langue voulue."""
    s, n = r["src"], r["num"]
    if s == "bih":
        annee, _, par_fr, par_en, par_he, para = n
        a = BIH_ANNEE[annee]
        return {"fr": f"Ben Ich ’Haï, {a[1]} année, {par_fr} §{para}",
                "en": f"Ben Ish Chai, Year {annee}, {par_en} §{para}",
                "he": f"בן איש חי, {a[3]}, {par_he}, אות {lettres(para)}"}[langue]
    if s in ("hid", "kav", "malka", "kikar"):
        m = MODERNES[(s, n)]
        if s == "kikar":
            return {"fr": f"Kikar haChabbat ({m['auteur_court'].replace(chr(39), '’')}, {m['date']})",
                    "en": f"Kikar HaShabbat (Rav B. Chota, {m['date']})",
                    "he": f"כיכר השבת, ״הלכה ב-60 שניות״, ״{m['titre']}״, {m['auteur_he']}, {m['date_he']}, kikar.co.il/629/{n}"}[langue]
        if s == "hid":
            return {"fr": f"Hidabroot, question {n}", "en": f"Hidabroot, question {n}",
                    "he": f"הידברות, ״{m['titre']}״, {m['auteur_he']}, {m['date_he']}, hidabroot.org/question/{n}"}[langue]
        if s == "kav":
            return {"fr": f"Kav haHalakha haSefaradi ({m['auteur_court']}, {m['date']})",
                    "en": f"Kav HaHalacha HaSefaradi ({m['auteur_court'].replace('Achkenazi', 'Ashkenazi').replace('Ochri', 'Oshri')}, {m['date']})",
                    "he": f"קו ההלכה הספרדי, ״{m['titre']}״, {m['auteur_he']}, {m['date_he']} (kavhalacha.co.il)"}[langue]
        return {"fr": f"Halakha lema’assé, question {n} ({m['auteur_court']})", "en": f"Halacha LeMaaseh, question {n} ({m['auteur_court']})",
                "he": f"בית ההוראה ״הלכה למעשה״ של הרב אופיר מלכא, ״{m['titre']}״, {m['auteur_he']}, {m['date_he']}, hl5047.co.il/questions/{n}"}[langue]
    if s == "ber":
        return {"fr": "Berakhot 8a-b", "en": "Berakhot 8a-b", "he": "ברכות ח ע״א–ע״ב, בלשון כף החיים רפ״ה, אות א׳"}[langue]
    sm, para = lieu(r)
    return CLASSIQUES[s][langue].format(s=sm, n=para, S=lettres(sm) if sm else "", N=lettres(para))


def crochets(refs, langue):
    """Les références en fin de halakha, regroupées par livre : « Michna Beroura 285:1, 7 »."""
    groupes = []
    for r in refs:
        s = r["src"]
        cle = (s, r["num"][1]) if s == "bih" else (s, lieu(r)[0]) if s in CLASSIQUES else s
        for g in groupes:
            if g[0] == cle:
                g[1].append(r)
                break
        else:
            groupes.append((cle, [r]))
    sortie = []
    for cle, rs in groupes:
        # Deux citations du même se'if ne le nomment qu'une fois.
        uniques = []
        for x in rs:
            if x["num"] not in [u["num"] for u in uniques]:
                uniques.append(x)
        rs = uniques
        s = rs[0]["src"]
        if s == "hid" and len(rs) > 1:
            et = {"fr": " et ", "en": " and "}[langue]
            nums = et.join(str(x["num"]) for x in rs)
            base = ref_texte(rs[0], langue).rsplit(" ", 1)[0].replace("question", "questions")
            sortie.append(f"{base} {nums}")
        elif s == "bih" and len(rs) > 1:
            base = ref_texte(rs[0], langue).rsplit("§", 1)[0]
            et = {"fr": " et ", "en": " and "}[langue]
            sortie.append(base + et.join(f"§{x['num'][5]}" for x in rs))
        elif s in ("kav", "kikar", "malka", "ber") or len(rs) == 1 or lieu(rs[0])[0] is None:
            vus = []
            for x in rs:
                t = ref_texte(x, langue)
                if t not in vus:
                    vus.append(t)
            sortie.extend(vus)
        else:
            base = ref_texte(rs[0], langue).rsplit(":", 1)[0]
            sortie.append(base + ":" + ", ".join(str(lieu(x)[1]) for x in rs))
    sep = {"fr": " ; ", "en": "; "}[langue]
    return sep.join(sortie)


# --- La typographie ------------------------------------------------------------------------------

def typo_fr(t):
    t = t.replace("'", "’")
    t = re.sub(r" ([:;?!»])", " \\1", t)
    t = t.replace("« ", "« ")
    return t


def typo_en(t):
    return t.replace("'", "’")


ETIQUETTES = {
    "sefarade": {"he": "[ספרדים – עדות המזרח]", "fr": "[Séfarades – rite Edot hamizra'h]", "en": "[Sephardim – Edot HaMizrach rite]"},
    "ashkenaze": {"he": "[אשכנזים – נוסח אשכנז ונוסח ספרד]", "fr": "[Ashkénazes – rites Ashkenaz et Sfard]", "en": "[Ashkenazim – Ashkenaz and Sfard rites]"},
}
RITES = {"tous": ["edot", "sefard", "ashkenaz"], "sefarade": ["edot"], "ashkenaze": ["ashkenaz", "sefard"]}

# --- Les halakhot -------------------------------------------------------------------------------
# H(rite, refs, fr, en) : le français et l'anglais sans numéro ni références (ajoutés ici).

def H(rite, refs, fr, en):
    return {"rite": rite, "refs": refs, "fr": fr, "en": en}


SECTIONS = [
    {"titre": "חיוב המצוה", "titre_fr": "L'obligation", "titre_en": "The obligation", "halakhot": [
        H("tous", [
            R("ber", 1, cite="לעולם ישלים אדם פרשיותיו עם הצבור שנים מקרא ואחד תרגום ואפי' עטרות ודיבון שכל המשלים פרשיותיו עם הצבור מאריכין לו ימיו ושנותיו"),
            R("sa", 1, cite='אע"פ שאדם שומע כל התורה כולה כל שבת בצבור חייב לקרות לעצמו בכל שבוע פרשת אותו שבוע שנים מקרא ואחד תרגום אפילו עטרות ודיבון'),
        ],
            "Même si l'on entend toute la Torah lue en public, Chabbat après Chabbat, on doit lire soi-même, chaque semaine, la paracha de cette semaine : deux fois le texte hébreu (mikra) et une fois la traduction araméenne (targoum), et cela même pour le verset « Atarot et Divon » (Bamidbar 32:3). Le Talmud enseigne que celui qui « achève ses parachiot avec la communauté » voit ses jours et ses années prolongés.",
            "Even though one hears the whole Torah read in public, Shabbat after Shabbat, one must read the parasha of each week by oneself: twice in the Hebrew original (mikra) and once in the Aramaic translation (targum), even the verse “Atarot and Divon” (Numbers 32:3). The Talmud teaches that whoever “completes his portions with the congregation” has his days and years lengthened."),
        H("tous", [
            R("kyy", 12, cite="אשה פטורה מלקרוא בכל שבת שנים מקרא ואחד תרגום"),
            R("hid", "262097", cite="לא חייבות", passage='לא חייבות. מקורות: שו"ת משנה הלכות חלק ו\' (סימן ס) וספר חזון עובדיה שבת חלק א\' (עמוד שכח).'),
            R("hid", "253987", passage='נראה שאשתו לא יכולה להוציא אותו ידי חובת שניים מקרא ואחד תרגום כיוון שהיא לא חייבת בזה כלל'),
        ],
            "Une femme est dispensée de lire chaque Chabbat Chnayim mikra véé'had targoum (Kitsour Yalkout Yossef). Le Rav Hillel Meirs (Hidabroot) répond de même que les femmes n'y sont pas obligées, en renvoyant au Mishné Halakhot (t. 6, siman 60) et au 'Hazon Ovadia (Chabbat, t. 1, p. 328) ; dans une autre réponse, il lui semble qu'une épouse ne peut pas acquitter son mari malade en lisant pour lui, puisqu'elle-même n'y est pas du tout obligée.",
            "A woman is exempt from reading Shnayim mikra ve-echad targum every week (Kitzur Yalkut Yosef). Rav Hillel Meirs (Hidabroot) likewise answers that women are not obligated, citing Mishneh Halachot (vol. 6, siman 60) and Chazon Ovadia (Shabbat, vol. 1, p. 328); in another answer he writes that it seems a wife cannot discharge her sick husband by reading for him, since she herself is not obligated at all."),
        H("tous", [
            R("ahs", 2, cite='''ולא נודע לנו טעמו של דבר, ובוודאי בשעה שתקן משה רבינו לקרות בתורה – תקן גם כן תקנה זו'''),
            R("ahs", 2, cite='''והלבוש כתב: כדי שיהא בקי בתורה, עיין שם, ואין זה מספיק כמובן'''),
            R("ahs", 2, cite='''ולכן ילמוד מקודם בחומש, ויעלה בקודש לשמוע מספר תורה'''),
            R("ahs", 2, cite='''לכן צריך ללמוד שלוש פעמים, אפילו בפסוק שאין בו תרגום, כמו שיתבאר, כנגד אלו השלוש. אך במקום שיש תרגום – בחרו בתרגום הפעם השלישי, כדי שיבין מה שהוא לומד'''),
            R("ahs", 2, cite='''ויש אומרים: כנגד שנים הקורין, ואחד המתרגם (ראב"ן)'''),
            R("kh", 1, cite='''ואלה שמות ר"ת וחייב אדם להשלים הפרשה שניים מקרא ואחד תרגום'''),
        ],
            "Pourquoi cette lecture ? L'Aroukh haChoul'han écrit que la raison ne nous en est pas connue, et que Moché Rabbénou, en instituant la lecture de la Torah, a certainement institué aussi celle-ci. Il rapporte la raison du Levouch – être versé dans la Torah – et la juge insuffisante. Il propose : la Torah demande d'écouter et d'étudier ; on étudie donc d'abord dans le 'Houmach, puis l'on « monte en sainteté » en écoutant la lecture dans le séfer Torah. Et trois fois, même pour un verset sans targoum, parce que la Torah a été dite au Sinaï, répétée dans la Tente d'assignation et dite une troisième fois dans les plaines de Moav ; là où il y a un targoum, on l'a choisi pour la troisième fois, afin de comprendre ce qu'on étudie. Il cite un autre avis, au nom du Raavan : en regard des deux qui lisent et de celui qui traduit. Le Kaf ha'Haïm rapporte une allusion : les initiales de « Véélé chemot » forment, en hébreu, « on doit achever la paracha, deux fois le texte et une fois le targoum ».",
            "Why this reading? The Aruch HaShulchan writes that its reason is not known to us, and that Moshe Rabbenu, when he instituted the reading of the Torah, surely instituted this as well. He quotes the Levush's reason – to be well versed in the Torah – and finds it insufficient. He suggests: the Torah calls for hearing and for studying; so one first studies in the Chumash, then “rises in holiness” by hearing the reading from the Torah scroll. And three times, even for a verse with no targum, because the Torah was said at Sinai, repeated in the Tent of Meeting and said a third time in the plains of Moav; where there is a targum, it was chosen for the third time, so that one understands what one studies. He cites another view, in the name of the Raavan: corresponding to the two who read and the one who translates. The Kaf HaChaim reports a hint: the initials of “Ve'eleh shemot” spell out, in Hebrew, “one must complete the parasha, twice the text and once the targum”."),
        H("tous", [
            R("kh", 4, cite='''שאתה קורא הפ' שנים מקרא ואחד תרגום ברהיטא כחותה על הגחלים לפרוק עול מעליך'''),
            R("kh", 4, cite='''אבל צריך לקרות הפרשה בנחת ולהרגיש בדקדוקיה ולתרץ אותם ומה שלא תוכל לתרץ עיין במפרשים'''),
            R("sch", 301, cite='''יהודי אחד לא היה קורא שנים מקרא ואחד תרגום שמאריכין לו ימיו ושנותיו כי אמר אני קץ בחיי למה אקרא אמר ליה החכם לא אמר זה רק כנגד האוהבי חיים'''),
            R("sch", 301, cite='''שאין העבד עושה תנאי לרבו'''),
            R("kh", 4, cite='''דיקרא האדם שמו"ת לשם מי שאמר למען תהיה תורת ה' בפיך'''),
            R("kh", 4, cite='''ואל יסמוך על תנאי'''),
            R("kh", 4, cite='''וע"כ קודם שיקרא הפ' שמו"ת י"ל לשם יחוד קבה"ו וכו' הריני בא לקרות הפ' של השבוע שמו"ת לתקן את שורשה במקום עליון'''),
        ],
            "On lit la paracha posément. Le Kaf ha'Haïm rapporte du Maguid Mécharim le reproche fait à Maran (Rabbi Yossef Karo) : la lire à la hâte, « comme on remue des braises », pour se décharger du joug ; il faut la lire avec calme, être attentif à ses difficultés, les résoudre, et chercher chez les commentateurs ce qu'on ne sait pas résoudre. Le Séfer 'Hassidim raconte qu'un homme ne lisait pas Chnayim mikra parce que, las de vivre, il ne voulait pas de la longue vie promise ; le sage lui répondit que cette promesse ne s'adresse qu'à ceux qui aiment la vie, et que les autres ne sont pas dispensés pour autant : le serviteur ne pose pas de condition à son maître. Le Kaf ha'Haïm en retient qu'on lit Chnayim mikra pour Celui qui a dit « afin que la Torah de Hachem soit dans ta bouche », sans faire de la récompense une condition ; il écrit qu'avant de lire, on dit « Léchem yi'houd… : je viens lire la paracha de la semaine, deux fois le texte et une fois le targoum, pour en réparer la racine en haut lieu ».",
            "The parasha is read unhurriedly. The Kaf HaChaim reports from the Maggid Mesharim the reproach made to Maran (Rabbi Yosef Karo): reading it in haste, “like one raking coals”, to throw off the yoke; one must read it calmly, notice its difficulties, resolve them, and look in the commentators for what one cannot resolve. Sefer Chasidim tells of a man who did not read Shnayim mikra because, weary of life, he did not want the promised long life; the sage answered that this promise is addressed only to those who love life, and that the others are not thereby exempt: a servant sets no condition to his master. The Kaf HaChaim concludes that one reads Shnayim mikra for the sake of the One who said “so that the Torah of Hashem be in your mouth”, without making the reward a condition; he writes that before reading one says “Leshem yichud…: I come to read the parasha of the week, twice the text and once the targum, to repair its root on high”."),
        H("sefarade", [
            R("kyy", 1, cite='''וגם העוסק בלימוד תורה כל היום, ותורתו אומנותו, לא יבטל קריאת פרשיותיו עם הצבור. וחייב לקרוא הפרשה שנים מקרא ואחד תרגום'''),
        ],
            "Même celui qui étudie la Torah toute la journée, et dont la Torah est le métier, ne néglige pas la lecture de ses parachiot avec la communauté : il doit lire la paracha deux fois dans le texte et une fois dans le targoum (Kitsour Yalkout Yossef).",
            "Even one who studies Torah all day, and whose Torah is his occupation, does not neglect reading his portions with the congregation: he must read the parasha twice in the text and once in the targum (Kitzur Yalkut Yosef)."),
        H("sefarade", [
            R("kh", 9, cite='''חולה וחש בעיניו פטורים וא"צ לשמוע מאחר'''),
            R("kh", 9, cite='''ומ"מ נראה דיש להשלימה אחר שיתרפא כדי שלא תהא תורתו של שמו"ת עולה לרקיע חסירה בשנה ההיא'''),
            R("kh", 10, cite='''סומא פטור מחיוב זה דדברים שבכתב א"א לאומרם ע"פ וא"צ לשמוע מאחר'''),
            R("kh", 10, cite='''וזהו לפום דינא אמנם המחמיר לשמוע מאחרים תע"ב וכן נכון לעשות'''),
            R("kh", 11, cite='''מי שאינו יודע לקרות פטור מחיוב זה וא"צ לשמוע מאחר'''),
            R("kyy", 15, cite='''אף מי שחלה בעיניו ומצטער בקריאת שנים מקרא ואחד תרגום, חייב לקרוא את הפרשה שנים מקרא ואחד תרגום, או שישמע הפרשה מאחר ויכוין לצאת ידי חובה'''),
            R("kyy", 16, cite='''יש אומרים שגם הסומא (עיור) חייב בשנים מקרא ואחד תרגום בכל שבת, כדין הפקח. ולכן צריך שישמע מאחר קריאת הפרשה שנים מקרא ואחד תרגום'''),
            R("kyy", 16, cite='''וכן מי שנעשה אילם, ואינו יכול לדבר ולקרוא, ישמע הקריאה מאחר'''),
        ],
            "Le malade, l'aveugle, celui qui ne sait pas lire. Le Kaf ha'Haïm rapporte, au nom du Radbaz cité par le Ma'hazik Berakha : le malade et celui qui souffre des yeux sont dispensés et n'ont pas à écouter la lecture d'un autre – il lui semble pourtant qu'il y a lieu de la compléter après la guérison, pour que la Torah de son Chnayim mikra ne monte pas incomplète cette année-là ; l'aveugle est dispensé, car ce qui est écrit ne se dit pas par cœur, et il n'a pas à écouter un autre – c'est le strict droit, mais celui qui est strict et écoute la lecture d'autrui est digne de bénédiction, et c'est ce qu'il convient de faire ; celui qui ne sait pas lire est dispensé lui aussi. Le Kitsour Yalkout Yossef écrit autrement : même celui qui a mal aux yeux et souffre en lisant doit lire, ou écouter la paracha d'un autre en pensant à s'acquitter ; certains disent que l'aveugle est tenu lui aussi, chaque Chabbat, comme celui qui voit, et il lui faut donc écouter la lecture d'un autre, qui pense à l'acquitter ; de même celui qui est devenu muet et ne peut pas lire écoute la lecture d'un autre.",
            "The sick, the blind, one who cannot read. The Kaf HaChaim reports, in the name of the Radbaz as cited by the Machazik Berachah: a sick person and one with eye pain are exempt and need not hear the reading from another – yet it seems to him that one should make it up after recovering, so that the Torah of one's Shnayim mikra does not ascend incomplete that year; a blind person is exempt, since what is written may not be said by heart, and need not hear it from another – that is the strict law, but one who is stringent and hears it from others is to be blessed, and this is the proper thing to do; one who does not know how to read is likewise exempt. The Kitzur Yalkut Yosef writes otherwise: even one whose eyes are ailing and who suffers when reading must read, or hear the parasha from another with the intention of fulfilling his obligation; some say that a blind person, too, is obligated every week like a sighted one, and must therefore hear the reading from another who intends to discharge him; likewise one who has become mute and cannot read listens to another's reading."),
    ]},
    {"titre": "זמן הקריאה", "titre_fr": "Quand lire", "titre_en": "When to read", "halakhot": [
        H("tous", [
            R("sa", 3, cite="מיום ראשון ואילך חשיב עם הצבור"),
            R("mb", 1, cite="היינו שלא יקדים לקרות קודם אותו שבוע וגם לא יאחר"),
            R("mb", 7, cite='כיון שמתחילין במנחתא דשבתא לקרות פרשת שבוע הבא נחשב שוב הקורא כקורא עם הציבור וא"כ מה שכתב המחבר מיום ראשון ואילך לאו דוקא הוא'),
            R("kh", 24, cite="ובכלבו דלא יצא אז מאחר שקראו אותו היום פרשה שעברה"),
            R("mb", 8, cite='וכן בספר מעשה רב כתב בהנהגת הגר"א שהיה נוהג תיכף אחר התפלה בכל יום לקרוא מקצת מהסדרה שנים מקרא ואחד תרגום ומסיים בע"ש'),
            R("sahr", 6, cite="אבל מן הדין אין צריך לקרות כל הפרשה שנים מקרא ואחד תרגום בפעם אחת"),
            R("hid", "221007", cite="אפשר להתחיל לקרוא שניים מקרא ואחד תרגום ממנחה של שבת",
              passage="אפשר להתחיל לקרוא שניים מקרא ואחד תרגום ממנחה של שבת (ראה שלחן ערוך אורח חיים סימן רפה סעיף ג ומשנה ברורה סק\"ז). וניתן גם לחלק את הקריאה לימי השבוע, ולקרוא כל יום חלק מפרשת השבוע"),
            R("hid", "354260", cite="אפשר לומר את התרגום בנפרד מקריאת החומש"),
        ],
            "On peut lire la paracha de la semaine à partir du dimanche : on la lit déjà « avec la communauté » (Choul'han Aroukh). La Michna Beroura précise que ce « dimanche » n'est pas strict : dès la Min'ha de Chabbat, où l'on commence en public la paracha suivante, la lire compte déjà ; mais on ne la lit pas avant cette semaine-là, et on ne tarde pas non plus. Le Kaf ha'Haïm rapporte toutefois l'avis du Kol Bo : on n'est pas quitte en lisant à ce moment-là, puisqu'on a lu ce jour-là la paracha précédente. Il n'est pas nécessaire de tout lire d'une traite : selon la loi, on peut répartir la paracha sur les jours de la semaine (Choul'han Aroukh haRav), et la Michna Beroura rapporte que le Gaon de Vilna en lisait chaque jour une partie aussitôt après la prière, pour finir le vendredi. Le Rav Hillel Meirs (Hidabroot) répond dans le même sens : on peut commencer dès la Min'ha de Chabbat et répartir la lecture sur la semaine ; le Rav Binyamin Chmouéli (Hidabroot) ajoute qu'on peut dire le targoum séparément de la lecture du 'Houmach.",
            "One may read the weekly parasha from Sunday on: it already counts as reading “with the congregation” (Shulchan Aruch). The Mishnah Berurah explains that “Sunday” is not exact: from Minchah of Shabbat, when the next parasha is begun in public, reading it already counts; but one should neither read it before that week nor delay it. The Kaf HaChaim reports, however, the view of the Kol Bo: one does not fulfil the obligation by reading then, since the previous parasha was read that day. It need not be read at one sitting: by law one may spread the parasha over the days of the week (Shulchan Aruch HaRav), and the Mishnah Berurah reports that the Vilna Gaon read part of it each day right after prayers, finishing on Friday. Rav Hillel Meirs (Hidabroot) answers in the same way: one may begin from Minchah of Shabbat and spread the reading over the week; Rav Binyamin Shmueli (Hidabroot) adds that the targum may be said separately from the reading of the Chumash."),
        H("ashkenaze", [
            R("ksa", 11, cite="אֲבָל הַמִּצְוָה מִן הַמֻּבְחָר הִיא לִקְרֹתָהּ בְּעֶרֶב שַׁבָּת אַחַר חֲצוֹת הַיּוֹם"),
            R("mb", 8, cite='כמה אחרונים כתבו דמן המובחר הוא לקרותה בע"ש ועיין בשע"ת ובספר מטה יהודה כתב דאם הוא קורא מתחלת השבוע והלאה הוא ג"כ בכלל מצוה מן המובחר'),
        ],
            "Le Kitsour Choul'han Aroukh écrit que le mieux est de lire la paracha la veille de Chabbat, après midi ('hatsot). La Michna Beroura rapporte que plusieurs A'haronim placent le meilleur moment la veille de Chabbat, mais que, selon le Maté Yehouda, celui qui lit dès le début de la semaine accomplit lui aussi la mitsva de la meilleure façon.",
            "The Kitzur Shulchan Aruch writes that it is best to read the parasha on Friday, after midday (chatzot). The Mishnah Berurah reports that several Acharonim hold Friday to be the best time, but that according to the Mateh Yehudah one who reads from the beginning of the week also fulfils the mitzvah in the best way."),
        H("sefarade", [
            R("kh", 24, cite='שרבינו האר"י ז"ל יום הששי תכף ומיד אחר תפלת שחרית היה הולך למקום שיש ס"ת וקורא שמו"ת'),
            R("kh", 24, cite="ומנהג החסידים ואנשי מעשה לקרות אותה בבוקר אחר סיום תפלת שחרית בעודנו מעוטף בציצית ותפילין"),
            R("bih", (2, "Lech Lecha", "Lekh Lekha", "Lech Lecha", "לך לך", 11), cite="גם צריך עוד הכנה בדיבור ביום הששי בעצמו - לקרות הפרשה כולה שנים מקרא ואחד תרגום"),
            R("bih", (2, "Lech Lecha", "Lekh Lekha", "Lech Lecha", "לך לך", 1), cite='ואם ירצה לצאת קודם שיקרא שניים מקרא ואחד תרגום, כדי שילך לקנות במהרה, רשאי, ואח"כ יקרא בביתו'),
            R("kyy", 8, cite="ומכל מקום, מי ששעתו דחוקה לו ואינו יכול לנהוג כן, בודאי שיכול לקרוא שמו״ת החל מיום ראשון, וכפסק מרן השלחן ערוך"),
            R("hid", "354076", passage="האם יש מניעה ללמוד שנים מקרא ללא תפילין [...] שני הדברים אפשריים ללא כל חשש."),
            R("kikar", "sxoq8i", passage="יש בהכנה בשבת דיבור וגם מעשה. מעשה, צריך להכין משהו, לנקות, לסדר, להכין נרות, פלטה, סדינים, אבל יש הכנה בדיבור. הכנה בדיבור מקיימים בקריאת שניים מקרא ואחד תרגום."),
        ],
            "Le Ari lisait la paracha le vendredi, aussitôt après la prière du matin, et le Kaf ha'Haïm rapporte que tel est l'usage des hommes pieux ('hassidim) et des hommes d'action : la lire le matin, après Cha'harit, encore enveloppés du talith et des tefilines. Le Ben Ich 'Haï compte la lecture de toute la paracha, le vendredi, parmi les préparatifs du Chabbat « par la parole » ; celui qui a l'habitude d'étudier chaque matin après la prière lira plutôt, le vendredi, Chnayim mikra, puis ira faire les achats du Chabbat, et s'il veut d'abord sortir acheter rapidement, il le peut et lira ensuite chez lui. Le Kitsour Yalkout Yossef conclut que celui dont le temps est compté peut de toute façon lire dès le dimanche, comme le tranche le Choul'han Aroukh. Le Rav Binyamin Chmouéli (Hidabroot) répond qu'on peut lire Chnayim mikra sans porter les tefilines. Le Rav Binyamin 'Hota (Kikar haChabbat) explique que la préparation du Chabbat se fait en actes et en paroles : lire Chnayim mikra accomplit la préparation par la parole, sans dispenser de préparer aussi quelque chose de ses mains.",
            "The Ari read the parasha on Friday, right after the morning prayer, and the Kaf HaChaim reports that this is the custom of the pious (chassidim) and men of deeds: to read it in the morning after Shacharit, still wrapped in tallit and tefillin. The Ben Ish Chai counts reading the whole parasha on Friday among the preparations for Shabbat “by speech”; one who usually studies every morning after prayers should rather read Shnayim mikra on Friday and then go shopping for Shabbat, and if he wants to go out shopping quickly first, he may, and read at home afterwards. The Kitzur Yalkut Yosef concludes that one whose time is short may in any case read from Sunday on, as the Shulchan Aruch rules. Rav Binyamin Shmueli (Hidabroot) answers that one may read Shnayim mikra without wearing tefillin. Rav Binyamin Chota (Kikar HaShabbat) explains that preparing for Shabbat is done in deed and in speech: reading Shnayim mikra fulfils the preparation by speech, without exempting one from also preparing something with one’s hands."),
        H("tous", [
            R("sa", 4, cite='מצוה מן המובחר שישלים אותה קודם שיאכל בשבת ואם לא השלים קודם אכילה ישלים אחר אכילה עד המנחה וי"א עד רביעי בשבת וי"א עד שמיני עצרת'),
            R("rema", 4, cite="(דהיינו בשמחת תורה שאז משלימים הצבור)"),
            R("mb", 11, cite="דג' ימים הראשונים שייכין עדיין קצת לשבת שעבר"),
            R("mb", 13, cite="ויש לו לקרות אז שנים מקרא ואחד תרגום ודלא כאותן שקורין מקרא לחוד"),
            R("kh", 28, cite='ובאבודרהם כתב דטוב להשלימה שמו"ת בעשרת ימי תשובה'),
            R("hid", "301252", passage='בדיעבד אפשר להשלים גם ביום ראשון ולהרבה דיעות גם עד יום שלישי. בדיעבד ישלים עד לשמחתת ורה.'),
            R("kikar", "t409fv", passage="זה הדד-ליין האחרון, הזמן האחרון, שאי אפשר לתקן יותר. מתי הוא? שמחת תורה. מתי בשמחת תורה? כשקראו בבית הכנסת קריאת התורה. [...] שב כל הלילה, תשלים את החובות שלך [...] קרה ונזכרת בבקר, תרוץ מהר, תפלל במניין יותר מאוחר."),
        ],
            "Le mieux est d'achever la paracha avant de manger le Chabbat ; sinon, on l'achève après le repas, jusqu'à Min'ha. Certains permettent, a posteriori, de l'achever jusqu'au mercredi – c'est-à-dire pendant les trois premiers jours de la semaine, qui tiennent encore un peu du Chabbat passé, explique la Michna Beroura –, d'autres jusqu'à Chemini Atseret – c'est-à-dire, précise le Rema, jusqu'à Sim'hat Torah, quand la communauté achève la Torah. Selon ce dernier avis, celui qui a laissé passer une semaine peut encore la rattraper jusque-là ; il la lit alors avec le targoum, et non le seul texte (Michna Beroura), et le Kaf ha'Haïm cite l'Abudarham : il est bon de la rattraper pendant les dix jours de pénitence. Le Rav Binyamin Chmouéli (Hidabroot) résume : a posteriori on peut encore compléter le dimanche, et selon beaucoup d'avis jusqu'au mardi ; a posteriori, on complète jusqu'à Sim'hat Torah. Le Rav Binyamin 'Hota (Kikar haChabbat) précise que ce dernier délai s'arrête à la lecture de la Torah à la synagogue, le jour de Sim'hat Torah : celui à qui il reste des parachiot les achève la nuit qui précède, et, s'il ne s'en souvient que le matin, il prie à un office plus tardif pour les achever avant la lecture.",
            "It is best to finish the parasha before eating on Shabbat; if not, one finishes it after the meal, until Minchah. Some allow, after the fact, finishing it until Wednesday – that is, during the first three days of the week, which still belong somewhat to the past Shabbat, the Mishnah Berurah explains –, others until Shemini Atzeret – that is, the Rema specifies, until Simchat Torah, when the congregation completes the Torah. According to this last view, one who missed a week may still make it up until then; he then reads it with the targum, not the text alone (Mishnah Berurah), and the Kaf HaChaim cites Abudarham: it is good to make it up during the ten days of repentance. Rav Binyamin Shmueli (Hidabroot) sums up: after the fact one may still make it up on Sunday, and according to many opinions until Tuesday; after the fact, one makes it up until Simchat Torah. Rav Binyamin Chota (Kikar HaShabbat) specifies that this last deadline ends at the Torah reading in the synagogue on Simchat Torah: one who still owes parashiot completes them during the preceding night, and if he remembers only in the morning, he prays at a later service so as to finish them before the reading."),
        H("ashkenaze", [
            R("mb", 9, cite='ומ"מ פשוט דאין לעכב מחמת זה האכילה עד אחר חצות'),
            R("mb", 9, cite='ולכתחלה מהנכון אם לא קרא שנים מקרא ואחד תרגום בע"ש להשכים בשבת בבקר ולקרא השמו"ת קודם הליכתו לבהכ"נ'),
            R("mb", 12, cite='אבל לכתחלה לכו"ע לא יאחר יותר מיום השבת'),
            R("sahr", 5, cite="וטוב לחוש לדבריהם שמי שעבר ולא השלים בזמנה ישלים עד סוף יום ג' ואם לא השלים יש לו להשלים עד שמחת תורה"),
        ],
            "La Michna Beroura précise qu'on ne retarde pas, pour achever la paracha, le repas du Chabbat au-delà de midi ('hatsot) ; mais celui qui n'a pas lu la veille fera bien de se lever tôt le Chabbat matin pour lire avant d'aller à la synagogue ; et a priori, tous s'accordent à ne pas dépasser le Chabbat. Le Choul'han Aroukh haRav conseille, à qui a laissé passer le temps, d'achever jusqu'à la fin du mardi, et sinon jusqu'à Sim'hat Torah.",
            "The Mishnah Berurah specifies that one does not delay the Shabbat meal past midday (chatzot) in order to finish the parasha; but one who did not read on Friday should rise early on Shabbat morning and read before going to the synagogue; and ideally all agree not to go beyond Shabbat. The Shulchan Aruch HaRav advises one who let the time pass to finish by the end of Tuesday, and otherwise by Simchat Torah."),
        H("sefarade", [
            R("kyy", 5, cite="ומכל מקום פשוט שאין לעכב מחמת זה האכילה עד חצות. ואם לא השלים קודם האכילה, ישלים אחר האכילה עד זמן מנחה. ובדיעבד עד רביעי בשבת, ויש אומרים עד שמיני עצרת"),
            R("bih", (2, "Lech Lecha", "Lekh Lekha", "Lech Lecha", "לך לך", 11), cite="ואם נאנס ולא קרא הפרשה שנים מקרא ואחד תרגום ביום ששי, יקראנה שנים מקרא ואחד תרגום ביום שבת אחר התפילה קודם קידוש שבת"),
            R("kh", 26, cite="ולסברה ב' עד יום ד' בדיעבד משלים ומיום ד' ואילך לא מהני כדין הבדלה"),
            R("kh", 3, cite="זולת אם אירע לו שום אונס גדול מאד שאז היה קורא הפ' שמו\"ת אחר סיום תפלת שחרית דיום שבת קודם סעודת שחרית כמו שצוה רבינו הקדוש לבנו ולא כמו אותם הקורים אותה באמצע תפלת שחרית דשבת"),
        ],
            "Le Kitsour Yalkout Yossef reprend l'ordre du Choul'han Aroukh : le mieux est d'achever avant le repas du Chabbat, sans pour autant retarder le repas jusqu'à midi ; sinon après le repas, jusqu'à Min'ha ; a posteriori jusqu'au mercredi (« רביעי בשבת »), et certains disent jusqu'à Chemini Atseret. Le Kaf ha'Haïm précise que le mercredi lui-même n'est pas compris : à partir du mercredi, cela ne vaut plus. Le Ben Ich 'Haï écrit que celui qui a été empêché de lire le vendredi lira le Chabbat après la prière, avant le Kiddouch. Le Kaf ha'Haïm rapporte que le Ari, en cas de très grand empêchement, lisait le Chabbat après la prière du matin, avant le repas, et non pendant l'office comme certains le font.",
            "The Kitzur Yalkut Yosef follows the order of the Shulchan Aruch: it is best to finish before the Shabbat meal, without delaying the meal until midday; if not, after the meal until Minchah; after the fact until Wednesday, and some say until Shemini Atzeret. The Kaf HaChaim specifies that Wednesday itself is not included: from Wednesday on, it no longer helps. The Ben Ish Chai writes that one who was prevented from reading on Friday should read on Shabbat after prayers, before Kiddush. The Kaf HaChaim reports that the Ari, when very greatly prevented, read on Shabbat after the morning prayer, before the meal, and not during the service as some do."),
        H("sefarade", [
            R("kyy", 9, cite="מי שזמנו דחוק, מותר לו לקרוא שנים מקרא ואחד תרגום בליל שבת"),
            R("kyy", 1, cite="ואם עוסק בתורה שיש עמה כתיבת חידושי תורה ופסקי הלכה, יכול לקרוא בליל שבת שנים מקרא ואחד תרגום"),
            R("kh", 14, cite='אין לקרות הפ\' שמו"ת באשמורת אור הששי קודם שיאיר היום כ"י כתבו גורי האר"י ז"ל שאין לקרות תרגום בלילה'),
            R("kav", "azoulay", cite='וכל זה הוא ע"פ הקבלה אבל ע"פ הפשט אין מניעה ללמוד מקרא בלילה',
              passage='ולכן להלכה, אפשר לקרוא ב\' מקרא ואחד תרגום בלילה כאשר קוראים יחד עם זה מעט מדברי המפרשים כרש"י וכדו\'. ואם ממילא אדם לא ילמד אם לא יקרא שניים מקרא, ואינו יודע ללמוד רש"י או אחד ממפרשי התורה, יש להורות לו לכתחילה שיכול לקרוא אף ללא מפרשים'),
            R("malka", "142", cite='ותו דיותר נכון לקרא שמו"ת ביום ולא בלילה'),
            R("hid", "303250", cite="אין קוראים מתחילת הלילה עד חצות"),
        ],
            "La nuit. Le Kitsour Yalkout Yossef permet à qui manque de temps de lire Chnayim mikra la nuit du Chabbat (le vendredi soir), ainsi qu'à celui qui étudie la Torah en écrivant des 'hidouchim et des décisions de halakha. Le Kaf ha'Haïm rapporte, d'après le Ma'hazik Berakha et les Cha'arei Techouva, qu'on ne lit pas Chnayim mikra à la fin de la nuit de jeudi à vendredi, avant qu'il fasse jour, parce que les disciples du Ari ont écrit qu'on ne lit pas le targoum la nuit. Le Rav Ochri Azoulay (Kav haHalakha haSefaradi) traite d'une autre règle, rapportée au nom du Ari : ne pas lire la Torah écrite la nuit. Il écrit qu'elle relève de la Kabbale, alors que selon le sens simple rien n'empêche d'étudier la Torah écrite la nuit ; il conclut qu'on peut lire Chnayim mikra la nuit en y joignant un peu de commentaire, comme Rachi, et qu'à celui qui, sinon, n'étudierait pas et qui ne sait pas étudier Rachi ou un autre commentateur, on indique qu'il peut lire même sans commentaire. Le Rav Menaché Moreno (beit hora'a « Halakha lema'assé » du Rav Ofir Malka) juge plus juste de lire le jour que la nuit, et le Rav Binyamin Chmouéli (Hidabroot) écrit qu'on ne lit pas depuis le début de la nuit jusqu'à 'hatsot (le milieu de la nuit).",
            "At night. The Kitzur Yalkut Yosef allows one who is short of time to read Shnayim mikra on Friday night, as well as one who studies Torah while writing chiddushim and halachic rulings. The Kaf HaChaim reports, following the Machazik Berachah and the Shaarei Teshuvah, that one does not read Shnayim mikra at the end of Thursday night, before daybreak, because the Ari’s disciples wrote that the targum is not read at night. Rav Oshri Azoulay (Kav HaHalacha HaSefaradi) deals with another rule, reported in the name of the Ari: not to read the Written Torah at night. He writes that it belongs to Kabbalah, whereas by the plain law nothing prevents studying the Written Torah at night; he concludes that one may read Shnayim mikra at night while adding a little commentary such as Rashi, and that one who would otherwise not study, and who does not know how to study Rashi or another commentator, is told that he may read even without commentary. Rav Menashe Moreno (the “Halacha LeMaaseh” beit hora’ah of Rav Ofir Malka) considers it more correct to read by day than by night, and Rav Binyamin Shmueli (Hidabroot) writes that one does not read from nightfall until chatzot (halachic midnight)."),
        H("ashkenaze", [
            R("mb", 10, cite='''דממנחה ולמעלה מתחילין הצבור לקרות פרשת שבוע הבא'''),
            R("bh", 4, cite='''ומה שצוה רבי שיגמרו הפרשה קודם הסעודה הוא רק משום דחייש דלמא אגב רוב סעודת שבת משתמיט ולא יגמור'''),
            R("bh", 4, cite='''המגן אברהם הביא דעות דמספר הכונות משמע דלכתחלה ישלים בע"ש ורק כשהיה אנוס ישלים בשבת ובב"י ומגיד מישרים משמע דלכתחלה יתחיל בע"ש וישלים בשבת'''),
            R("ha", 9, cite='''ולכתחלה ישלים בע"ש ועכ"פ לא יאכל בשבת שחרית עד שישלים'''),
            R("ahs", 9, cite='''ומתבאר מדבריו שאין הידור להשלים קודם קריאת התורה, רק קודם אכילה'''),
            R("ahs", 10, cite='''ויש אומרים דמצוה מן המובחר לקרא כל יום מעט, ובערב שבת להשלימה, כמו שנדפס בספר חוק לישראל'''),
        ],
            "Jusqu'à Min'ha, parce qu'à partir de Min'ha la communauté commence à lire la paracha de la semaine suivante (Michna Beroura). Le Béour Halakha explique, d'après le Or Zaroua, que Rabbi n'a demandé d'achever la paracha avant le repas que par crainte qu'entraîné par le grand repas du Chabbat on ne s'y dérobe et ne l'achève pas ; il rapporte aussi les avis cités par le Maguen Avraham : d'après le Séfer haKavanot, on achève a priori la veille de Chabbat, et le Chabbat seulement si l'on a été empêché ; d'après le Beit Yossef et le Maguid Mécharim, on commence a priori la veille et l'on achève le Chabbat. Le 'Hayé Adam écrit : a priori on achève la veille de Chabbat, et en tout cas on ne mange pas le Chabbat matin avant d'avoir achevé. L'Aroukh haChoul'han déduit du Tour qu'il n'y a pas de mérite particulier à achever avant la lecture de la Torah, mais seulement avant le repas ; il rapporte aussi l'avis pour qui le mieux est de lire un peu chaque jour et d'achever la veille de Chabbat, comme c'est imprimé dans le 'Hok leIsraël.",
            "Until Minchah, because from Minchah on the congregation begins to read the next week's parasha (Mishnah Berurah). The Beur Halacha explains, following the Or Zarua, that Rabbi asked that the parasha be finished before the meal only out of concern that, carried along by the large Shabbat meal, one might slip out of it and not finish; it also reports the views quoted by the Magen Avraham: according to Sefer HaKavanot one finishes on Friday in the first place, and on Shabbat only if prevented; according to the Beit Yosef and the Maggid Mesharim one begins on Friday in the first place and finishes on Shabbat. The Chayei Adam writes: in the first place one finishes on Friday, and in any case one does not eat on Shabbat morning before finishing. The Aruch HaShulchan infers from the Tur that there is no particular merit in finishing before the Torah reading, only before the meal; he also reports the view that it is best to read a little each day and finish on Friday, as printed in Chok LeYisrael."),
        H("sefarade", [
            R("kh", 26, cite='''ומשמע לפי סברה זאת דיש ג' חלוקות מצוה מן המובחר קודם אכילה ובדיעבד גם אחר אכילה מהני קודם מנחה אבל אחר מנחה לא מהני וכן דעת הש"ע שסתם כן כסברה א\''''),
            R("kh", 26, cite='''ונראה ברור דגם לסברה ג' אינו מועיל אלא יום ש"ע אבל יום ש"ת שהתחילו פ' בראשית לא מהני לכ"ע'''),
            R("kh", 26, cite='''ואנה"נ דביום ש"ת לא מהני אלא קודם קריאת פ' בראשית'''),
            R("kh", 28, cite='''והיינו אם לא השלים ביום ג' דיעבד יש להשלימה כל השנה עד שמיני עצרת בא"י ולדידן בשמחת תורה מיקרי שפיר משלים עם הצבור ומכאן ואילך עבר זמנו'''),
            R("kh", 29, cite='''וכל עוד שלא גמרו הצבור וזאת הברכה מיקרי זמנה'''),
        ],
            "Jusqu'à quand, précisément. Le Kaf ha'Haïm relève, au nom du Maté Yehouda, trois degrés selon le premier avis : le mieux, avant le repas ; a posteriori, après le repas, avant Min'ha ; après Min'ha, cela ne vaut plus – et tel est l'avis du Choul'han Aroukh, qui énonce cet avis en premier, sans le nommer. Même selon le troisième avis (jusqu'à Chemini Atseret), il lui paraît clair que seul le jour de Chemini Atseret vaut : le jour de Sim'hat Torah, une fois commencée la paracha Beréchit, cela ne vaut plus pour personne ; le Rema ne veut pas ajouter un jour mais donner la raison – la communauté achève alors –, et à Sim'hat Torah cela ne vaut qu'avant la lecture de Beréchit. Il rapporte de l'Échel Avraham : celui qui n'a pas achevé jusqu'au mardi peut encore, a posteriori, rattraper toute l'année, jusqu'à Chemini Atseret en terre d'Israël et, « pour nous », jusqu'à Sim'hat Torah ; passé ce moment, le temps est révolu. Et tant que la communauté n'a pas achevé Vezot haBerakha, c'est encore son temps.",
            "Until when, exactly. The Kaf HaChaim notes, in the name of the Mateh Yehudah, three levels according to the first view: best, before the meal; after the fact, after the meal, before Minchah; after Minchah it no longer counts – and such is the view of the Shulchan Aruch, which states this view first, unattributed. Even according to the third view (until Shemini Atzeret), it seems clear to him that only the day of Shemini Atzeret counts: on Simchat Torah, once parashat Bereshit has been begun, it no longer counts according to anyone; the Rema does not mean to add a day but to give the reason – the congregation completes then –, and on Simchat Torah it counts only before the reading of Bereshit. He reports from the Eshel Avraham: one who did not finish by Tuesday may still, after the fact, make it up all year, until Shemini Atzeret in the Land of Israel and, “for us”, until Simchat Torah; after that the time has passed. And as long as the congregation has not completed Vezot HaBerachah, it is still its time."),
        H("sefarade", [
            R("mbe", 129, cite='''יום הששי בבקר יזהר לקרות פרשת השבוע שנים מקרא ואחד תרגום ואם אפשר בטלית ותפילין יקראנה'''),
            R("kh", 24, cite='''ואם חל ר"ח ביום ו' לא יחזור ללבוש תפילין כמ"ש לעיל סי' כ"ה או' צ"ו אלא יקרא אותה מעוטף בטלית בלבד'''),
            R("tsh", 58, cite='''אם נאנס יום הששי ולא קרא הפרשה שמו״ת יקראנה יום שבת שמו״ת ודלא כמי שכתב דבשבת לא יקרא תרגום'''),
            R("kh", 25, cite='''זולת אם אירע לו אונס גדול מאד שאז היה קורא אותה אחר סיום תפלת שחרית קודם סעודת שחרית'''),
        ],
            "Le 'Hida (Moré beEtsba) : le vendredi matin, on veille à lire la paracha de la semaine deux fois dans le texte et une fois dans le targoum, si possible avec le talith et les tefilines. Quand Roch 'Hodech tombe un vendredi, on ne remet pas les tefilines pour cela : on la lit enveloppé du talith seulement (Kaf ha'Haïm). Celui qui a été empêché le vendredi la lit le Chabbat, texte et targoum, et non comme celui qui a écrit qu'on ne lit pas le targoum le Chabbat ('Hida, Tsiporen Chamir) ; le Kaf ha'Haïm rapporte que le Ari, s'il lui arrivait un très grand empêchement, la lisait après la prière du matin (du Chabbat), avant le repas du matin.",
            "The Chida (Moreh BeEtzba): on Friday morning one takes care to read the weekly parasha twice in the text and once in the targum, if possible in tallit and tefillin. When Rosh Chodesh falls on a Friday, one does not put the tefillin back on for this: one reads it wrapped in the tallit only (Kaf HaChaim). One who was prevented on Friday reads it on Shabbat, text and targum, unlike the one who wrote that the targum is not read on Shabbat (Chida, Tziporen Shamir); the Kaf HaChaim reports that the Ari, if something very serious prevented him, read it after the morning prayer (of Shabbat), before the morning meal."),
        H("tous", [
            R("ma", 1, cite='''ויטבול אחר הקריא' [הכוונו'] עיין בשל"ה עניני טבילה ואין לי כאן עסק בנסתרות ויקוץ הצפרנים קודם הקריאה [של"ה]'''),
            R("bht", 1, cite='''ויקוץ הצפרנים קודם שמו"ת. ועיקר המצוה לקרות אחר חצות ואחר שקרא ילך לבית המרחץ ויטבול'''),
            R("er", (260, 4), cite='''ומי שקורא שנים מקרא ואחד תרגום בערב שבת יטבול קודם שיקרא (של"ה)'''),
            R("ahs", 7, cite='''וזהו ממדת חסידות, ולהקוראים אותה כולה בערב שבת'''),
            R("kh", 38, cite='''ובענין קציצת הצפרנים והטבילה וכוונתה כבר כתבנו לעיל סי' ר"ס קחנו משם'''),
        ],
            "Ongles et mikvé. Le Maguen Avraham rapporte qu'on s'immerge après la lecture, d'après le Séfer haKavanot – en ajoutant : « je n'ai pas affaire ici aux choses cachées » –, et qu'on se coupe les ongles avant la lecture, d'après le Chla. Le Baèr Hétev de même : les ongles avant Chnayim mikra ; l'essentiel de la mitsva est de lire après midi ; et après avoir lu, on va au bain et l'on s'immerge. L'Eliya Rabba rapporte au contraire, au nom du Chla, que celui qui lit Chnayim mikra la veille de Chabbat s'immerge avant de lire. L'Aroukh haChoul'han précise que c'est une conduite de piété, pour ceux qui lisent toute la paracha la veille de Chabbat. Le Kaf ha'Haïm renvoie, pour les ongles et l'immersion, à ce qu'il en a écrit au siman 260.",
            "Nails and mikveh. The Magen Avraham reports that one immerses after the reading, according to Sefer HaKavanot – adding: “I have no business here with hidden matters” –, and that one cuts one's nails before the reading, according to the Shelah. The Ba'er Hetev likewise: nails before Shnayim mikra; the main mitzvah is to read after midday; and after reading one goes to the bathhouse and immerses. The Eliyah Rabbah reports on the contrary, in the name of the Shelah, that one who reads Shnayim mikra on Friday immerses before reading. The Aruch HaShulchan specifies that this is a pious practice, for those who read the whole parasha on Friday. The Kaf HaChaim refers, for nails and immersion, to what he wrote about them in siman 260."),
    ]},
    {"titre": "סדר הקריאה", "titre_fr": "L'ordre de la lecture", "titre_en": "The order of reading", "halakhot": [
        H("tous", [
            R("mb", 6, cite='לא יקרא פסוק המאוחר קודם המוקדם אלא יקרא כסדר. לא יקרא התרגום תחלה ואח"כ מקרא אלא יקרא לכתחלה שנים מקרא מקודם ואח"כ תרגום'),
            R("kh", 6, cite='לא יקרא אחד מקרא ואח"כ תרגום ואח"כ מקרא אלא שנים מקרא וא\' תרגום'),
            R("kh", 15, cite='אם טעה ודילג פסוק אחר וקרא איזה פסוקים ואח"כ נזכר צריך לחזור ולקרות פסוק המדולג וגם מה שקרא אחריו כדי שיהיו כסדר'),
            R("bih", (2, "Lech Lecha", "Lekh Lekha", "Lech Lecha", "לך לך", 11), cite="ואחר שסיים הפרשה יכפול פסוק האחרון, ואין צריך לכפול גם התרגום שלו"),
            R("ksa", 11, cite="וּבַגְּמָר יֵשׁ לוֹמַר אַחַר הַתַּרְגּוּם פָּסוּק אֶחָד בַּתּוֹרָה, כְּדֵי לְסַיֵּם בַּתּוֹרָה"),
            R("sahr", 3, cite="ופסוק האחרון טוב לכופלו ולחזור ולאמרו כדי לסיים בתורה"),
            R("kh", 33, cite='אחר שגמר כל הפ\' שמו"ת יקרא פסוק אחרון פ"ג מקרא לבד כדי להשלים במקרא'),
            R("hid", "299490", passage="רציתי לשאול אם אני יכול לקרוא פעם אחת את הפרשה, ואז לקרוא פסוק אחד ואז תרגום,עוד פסוק ותרגום וככה הלאה? [...] 1. יכול."),
        ],
            "On lit les versets dans l'ordre, sans lire un verset avant celui qui le précède ; a priori, on dit d'abord deux fois le texte, puis le targoum, et non le targoum en premier (Michna Beroura) ni entre les deux lectures (Kaf ha'Haïm). Celui qui a sauté un verset et s'en aperçoit plus loin revient lire le verset oublié, puis ce qu'il avait lu après, pour garder l'ordre (Kaf ha'Haïm). À la fin de la paracha, on répète le dernier verset, sans avoir à en répéter le targoum (Ben Ich 'Haï) ; le Kitsour Choul'han Aroukh, le Choul'han Aroukh haRav (« il est bon ») et le Kaf ha'Haïm (le texte seul, une troisième fois) en donnent la raison : finir par le texte de la Torah. À qui demande s'il peut lire d'abord toute la paracha une fois, puis chaque verset une seconde fois suivi de son targoum, le Rav Binyamin Chmouéli (Hidabroot) répond que c'est possible.",
            "One reads the verses in order, never a verse before the one that precedes it; ideally, one says the text twice first, then the targum, not the targum first (Mishnah Berurah) nor between the two readings (Kaf HaChaim). One who skipped a verse and notices later goes back to read the skipped verse and then what he had read after it, to keep the order (Kaf HaChaim). At the end of the parasha one repeats the last verse, without having to repeat its targum (Ben Ish Chai); the Kitzur Shulchan Aruch, the Shulchan Aruch HaRav (“it is good”) and the Kaf HaChaim (the text alone, a third time) give the reason: to finish with the text of the Torah. To one who asks whether he may first read the whole parasha once and then each verse a second time followed by its targum, Rav Binyamin Shmueli (Hidabroot) answers that he may."),
        H("ashkenaze", [
            R("mb", 2, cite='י"א שיקרא כל פסוק ב"פ ותרגום עליו וי"א שיקרא כל פרשה ב"פ ואח"כ התרגום'),
            R("mb", 2, cite="ודעביד כמר עביד ודעביד כמר עביד"),
            R("ksa", 11, cite="וְיֵשׁ לִקְרוֹת כָּל פָּרָשָׁה, דְּהַיְנוּ פְּתוּחָה אוֹ סְתוּמָה, שְׁנֵי פְּעָמִים, וְאַחַר כָּךְ הַתַּרְגּוּם עָלֶיהָ, (כֵּן הִסְכִּים הַגָּאוֹן הָרַב רַבִּי אֵלִיָהוּ מִוִילְנָא זֵכֶר צַדִּיק לִבְרָכָה) וַאֲפִלּוּ הַפָּרָשָׁה מְסַיֶּמֶת בְּאֶמְצַע פָּסוּק, יַפְסִיק שָׁם"),
            R("sahr", 3, cite="ויש נוהגין לקרות כל פסוק ב' פעמים והתרגום עליו מיד ומנהג זה נכון יותר"),
            R("sahr", 3, cite="(אבל מן הדין יכול לקרות שנים מקרא ואחד תרגום בכל ענין שירצה)"),
        ],
            "Verset par verset, ou section par section ? La Michna Beroura rapporte les deux avis : lire chaque verset deux fois puis son targoum, ou chaque section (ouverte ou fermée) deux fois puis son targoum ; le Maguen Avraham et les Cha'arei Techouva penchent pour le premier, le Gaon de Vilna disait le targoum après chaque section, ou là où le sujet marque une pause plus nette, et chacun peut suivre l'une ou l'autre façon. Le Kitsour Choul'han Aroukh retient la lecture par section, selon le Gaon de Vilna, en s'arrêtant à la fin de la section même au milieu d'un verset. Le Choul'han Aroukh haRav juge la lecture verset par verset plus juste, tout en notant que, selon la loi, on peut lire de la façon que l'on veut.",
            "Verse by verse, or section by section? The Mishnah Berurah reports both views: read each verse twice and then its targum, or each section (open or closed) twice and then its targum; the Magen Avraham and the Shaarei Teshuvah lean to the first, the Vilna Gaon said the targum after each section, or wherever the subject pauses more clearly, and one may follow either way. The Kitzur Shulchan Aruch adopts reading by section, following the Vilna Gaon, stopping at the end of the section even in the middle of a verse. The Shulchan Aruch HaRav considers reading verse by verse more correct, while noting that by law one may read in whatever way one wishes."),
        H("sefarade", [
            R("kh", 3, cite='וכן היה עושה בכל פסוק ופסוק עד שמשלים הפרשה'),
            R("kyy", 4, cite="על פי דברי המקובלים צריך לקרוא את הפרשה כל פסוק ופסוק שנים מקרא ואחד תרגום, עד סיום כל הפרשה, בהמשך אחד"),
            R("kyy", 4, cite="ובאופן כזה גם כשמגיע לפסוק שמע ישראל, רשאי לקרוא שנים מקרא ואחד תרגום"),
            R("kav", "yaron1", cite="ומכל מקום אין זה מעכב להלכה",
              passage='הנה על פי דברי רבינו האר"י ז"ל, יש לקרות שנים מקרא ואחד תרגום כל פסוק עם תרגומו בפני עצמו, ולא להניח התרגום עד סיום הפרשה כולה, וכן הוא בספר האשכול (הלכות שני וחמישי סימן ב\'), ומכל מקום אין זה מעכב להלכה'),
            R("hid", "354076", passage="האם יש מניעה לחזור על פרשת שמע פעמיים הן לאלו שקוראים פרשה פרשה והן לאלו שקוראים פסוק פסוק [...] שני הדברים אפשריים ללא כל חשש."),
        ],
            "Selon les kabbalistes, on lit chaque verset deux fois puis son targoum, verset après verset, jusqu'à la fin de la paracha, d'une seule traite : ainsi faisait le Ari, et ainsi font les hommes pieux et les gens d'action qui se conduisent en tout selon la Kabbale (Kaf ha'Haïm ; Kitsour Yalkout Yossef). Le Rav Yaron Achkenazi (Kav haHalakha haSefaradi) précise que cela n'est pas indispensable selon la halakha. Lu ainsi, le verset « Chema Israël » peut être dit deux fois, car on voit bien qu'on le répète pour Chnayim mikra (Kitsour Yalkout Yossef) ; le Rav Binyamin Chmouéli (Hidabroot) répond aussi qu'on peut sans crainte répéter le passage du Chema, que l'on lise par section ou verset par verset.",
            "According to the kabbalists, one reads each verse twice and then its targum, verse after verse, to the end of the parasha, at one sitting: so did the Ari, and so do the pious and men of deeds who follow Kabbalah in all their ways (Kaf HaChaim; Kitzur Yalkut Yosef). Rav Yaron Ashkenazi (Kav HaHalacha HaSefaradi) specifies that this is not indispensable by halachah. Read this way, the verse “Shema Yisrael” may be said twice, since it is clear that it is repeated for Shnayim mikra (Kitzur Yalkut Yosef); Rav Binyamin Shmueli (Hidabroot) also answers that one may repeat the passage of the Shema without concern, whether reading by section or verse by verse."),
        H("tous", [
            R("rambam", 25, cite="וּפָסוּק שֶׁאֵין בּוֹ תַּרְגּוּם קוֹרְאֵהוּ שָׁלֹשׁ פְּעָמִים"),
            R("sa", 1, cite="שנים מקרא ואחד תרגום אפילו עטרות ודיבון"),
            R("mb", 3, cite='ר"ל אע"פ שאין בו תרגום וה"ה ראובן ושמעון וכי"ב צריך לקרותו ג"פ ויש מחמירין דבעטרות ודיבן שיש בו תרגום ירושלמי צריך לקרות שם התרגום'),
            R("kh", 18, cite='וכן הוא מנהג העולם שאין קורין ג"פ מקרא רק לפסוק שאין בו תרגום כלל כמו ראובן ושמעון וכדומה אבל לפסוק שיש בו תרגום כגון ברכת כהנים ועטרות ודיבון אין קורין כ"א שמו"ת לבד'),
            R("kav", "yaron2", passage='ומרן השלחן ערוך פסק כדעת הרמב,,ם שיקרא ג\' פעמים עטרות ודיבון ואינו צריך לקרוא בפעם השלישית את התרגום ירושלמי.'),
        ],
            "Un verset qui n'a pas de targoum se lit trois fois (Rambam). Le Choul'han Aroukh demande Chnayim mikra « même pour Atarot et Divon » ; la Michna Beroura explique : ce verset se lit trois fois parce qu'il n'a pas de targoum, et de même à « Réouven et Chimon » et aux versets semblables ; certains, plus stricts, lisent pour « Atarot et Divon » le targoum Yerouchalmi. Le Kaf ha'Haïm rapporte l'usage répandu : on ne lit trois fois que le verset qui n'a aucun targoum, comme « Réouven et Chimon », tandis que la bénédiction des Cohanim et « Atarot et Divon », qui ont un targoum, se lisent seulement deux fois avec leur targoum. Le Rav Yaron Achkenazi (Kav haHalakha haSefaradi) écrit, lui, que le Choul'han Aroukh a tranché comme le Rambam : « Atarot et Divon » trois fois, sans avoir à lire la troisième fois le targoum Yerouchalmi.",
            "A verse that has no targum is read three times (Rambam). The Shulchan Aruch requires Shnayim mikra “even for Atarot and Divon”; the Mishnah Berurah explains: this verse is read three times because it has no targum, and likewise to “Reuven and Shimon” and similar verses; some, more stringent, read the Targum Yerushalmi for “Atarot and Divon”. The Kaf HaChaim reports the widespread custom: only a verse with no targum at all, such as “Reuven and Shimon”, is read three times, whereas the Priestly Blessing and “Atarot and Divon”, which have a targum, are read only twice with their targum. Rav Yaron Ashkenazi (Kav HaHalacha HaSefaradi), for his part, writes that the Shulchan Aruch ruled like the Rambam: “Atarot and Divon” three times, without having to read the Targum Yerushalmi the third time."),
        H("ashkenaze", [
            R("mb", 6, cite='אם אפשר לו שלא יפסיק בשמו"ת על שום דבר הוא טוב ויפה מאד וכן ראיתי מהמדקדקים עושין כן וכן ראוי לבעל נפש לעשות'),
            R("ksa", 11, cite="וְטוֹב שֶׁלֹּא יַפְסִיק בְּשִׂיחָה בֵּין הַקְּרִיאָה"),
            R("sahr", 6, cite="ויש נוהגין לגמור כולה ערב שבת שחרית אחר התפלה ושלא להפסיק כלל באמצע שנים מקרא ואחד תרגום אפילו בדבור"),
        ],
            "Il est très bien, si possible, de ne s'interrompre pour rien pendant Chnayim mikra : les gens scrupuleux le font, et il convient à qui tient à son âme de faire ainsi (Michna Beroura). Il est bon de ne pas s'interrompre par une conversation au milieu de la lecture (Kitsour Choul'han Aroukh). Le Choul'han Aroukh haRav rapporte l'usage de certains d'achever toute la paracha le vendredi matin après la prière, sans s'interrompre du tout, même par la parole.",
            "It is very good, if possible, not to interrupt Shnayim mikra for anything: careful people do so, and it befits one who cares for his soul (Mishnah Berurah). It is good not to interrupt the reading with conversation (Kitzur Shulchan Aruch). The Shulchan Aruch HaRav reports the custom of some to finish the whole parasha on Friday morning after prayers without any interruption, even by speech."),
        H("sefarade", [
            R("kyy", 6, cite="אף על פי שמדין התלמוד אין איסור להפסיק בדברים באמצע קריאת שנים מקרא ואחד תרגום, מכל מקום כבר נתבאר שעל פי הקבלה אין להפסיק כלל באמצע קריאתם"),
            R("kyy", 6, cite="זולת אם הוא צמא למים, שרשאי לברך ולשתות, וכן לברך ברכת בורא נפשות רבות"),
            R("kyy", 7, cite="מותר לו להפסיק בין פסוק לפסוק להשיב לשואלו דבר הלכה"),
            R("kh", 15, cite='וכתבו חכמי המקובלים שלא להפסיק בקריאת שמו"ת בשום דבר רק יקרא הכל בפעם אחת במעמד אחד'),
            R("kav", "yaron1", passage="מי שהתחיל לקרוא שנים מקרא ואחד תרגום אחר תפלת שחרית, ובאמצע קריאתו נתבקש לקרוא לפני הקהל איזה דבר הלכה, רשאי להפסיק מקריאתו, ולזכות את הרבים בקריאת דבר הלכה."),
        ],
            "Selon le Talmud, il n'est pas interdit de parler au milieu de Chnayim mikra ; mais selon la Kabbale on ne s'interrompt pas du tout, et l'on lit tout d'une traite (Kitsour Yalkout Yossef ; Kaf ha'Haïm). Celui qui a soif d'eau peut s'interrompre pour boire, avec la bénédiction avant et Boré nefachot après (Kitsour Yalkout Yossef ; le Kaf ha'Haïm dit : « très soif »). Celui à qui l'on demande, au milieu de sa lecture du matin, de lire au public une halakha ou un enseignement sur la paracha peut s'interrompre pour en faire profiter le public (Kitsour Yalkout Yossef ; de même le Rav Yaron Achkenazi, Kav haHalakha haSefaradi) ; un érudit à qui l'on pose une question de halakha peut y répondre entre deux versets.",
            "By the Talmud it is not forbidden to talk in the middle of Shnayim mikra; but according to Kabbalah one does not interrupt at all, and reads everything at one sitting (Kitzur Yalkut Yosef; Kaf HaChaim). One who is thirsty for water may stop to drink, with the blessing before and Borei nefashot after (Kitzur Yalkut Yosef; the Kaf HaChaim says: “very thirsty”). One who is asked, in the middle of his morning reading, to read a halachah or a teaching on the parasha to the public may stop to benefit the public (Kitzur Yalkut Yosef; likewise Rav Yaron Ashkenazi, Kav HaHalacha HaSefaradi); a Torah scholar asked a question of halachah may answer it between two verses."),
        H("tous", [
            R("ahs", 7, cite='''ויש שקורין כל הסדרה, ואחר כך פעם שני, ואחר כך התרגום. וכן משמע קצת מלשון רש"י בברכות שם'''),
            R("ahs", 7, cite='''ולכן נראה לעניות דעתי דאין קפידא, ויכול לעשות כמו שירצה, דלכולם יש פנים בהלכה. ואפשר שגם יכול לעשות פעמים כך ופעמים כך. ואי סלקא דעתך שיש קפידא לעשות דווקא כך או כך – לא הוה שתקי רבותינו הראשונים מלפרשה'''),
            R("kh", 3, cite='''ולא היה עושה כמו שיש מתייהרים לקרוא כל הפרשה כולה מקרא פ"א ולשנותה מקרא פ"ב ואח"כ קורים כולה יחד תרגום פ"ג אלא כל פסוק ופסוק בפ"ע היה קורא שמו"ת'''),
            R("mbe", 130, cite='''וכ״ש שלא ילמוד כל פרשת השבוע כולה שנים מקרא ואח״כ יקראנה כלה תרגום. לא אריך למעבד הכי'''),
        ],
            "Lire toute la paracha une fois, puis une seconde fois, puis tout le targoum ? L'Aroukh haChoul'han rapporte que certains font ainsi, y voit un certain appui dans les mots de Rachi, et conclut qu'à son humble avis rien n'est ici impératif : on peut faire comme on veut, chaque façon a un fondement dans la halakha, et peut-être même tantôt d'une façon, tantôt d'une autre – s'il fallait absolument faire d'une seule façon, les Richonim ne se seraient pas tus. À l'inverse, le Kaf ha'Haïm rapporte du Cha'ar haKavanot que le Ari ne faisait pas comme ceux qui se piquent de lire toute la paracha une fois, de la répéter, puis de lire tout le targoum d'un coup : il lisait chaque verset à part, deux fois puis son targoum. Et le 'Hida (Moré beEtsba) écrit qu'à plus forte raison on n'étudie pas toute la paracha deux fois pour lire ensuite tout le targoum : « il ne convient pas de faire ainsi ».",
            "Reading the whole parasha once, then a second time, then the whole targum? The Aruch HaShulchan reports that some do so, sees some support for it in Rashi's wording, and concludes that in his humble opinion nothing here is imperative: one may do as one wishes, each way has a basis in halachah, and perhaps even sometimes one way and sometimes another – had one way been required, the Rishonim would not have kept silent. Conversely, the Kaf HaChaim reports from Sha'ar HaKavanot that the Ari did not do as those who presume to read the whole parasha once, repeat it, and then read the whole targum together: he read each verse by itself, twice and then its targum. And the Chida (Moreh BeEtzba) writes that all the more so one should not study the whole parasha twice and then read the whole targum: “it is not fitting to do so”."),
        H("ashkenaze", [
            R("ahs", 4, cite='''ו"פרשה" מקרי פתוחה או סתומה. וזה שמצויין בחומשים "שלישי", "רביעי", וכו' – זה אינו כלום'''),
            R("ahs", 5, cite='''אך לפי זה יש להסתפק כשיש פרשה באמצע פסוק'''),
            R("ahs", 5, cite='''נראה שיעשה כן. ואי משום "כל פסוקא דלא פסקיה משה לא פסקינן" – הא כאן פסקיה משה'''),
        ],
            "Pour qui lit section par section, l'Aroukh haChoul'han précise que la « paracha » est la section ouverte ou fermée ; les repères « troisième », « quatrième »… imprimés dans les 'Houmachim n'y comptent pour rien. Quand une section s'achève au milieu d'un verset – il cite « Ce fut après le fléau » (Pin'has), « Les fils de Yaakov étaient douze » (Vayichla'h) et « d'Eilat et d'Etsion Guéver » (Devarim) –, il lui semble qu'on s'y arrête tout de même : la règle « un verset que Moché n'a pas coupé, nous ne le coupons pas » ne s'y oppose pas, puisqu'ici Moché l'a coupé.",
            "For one who reads section by section, the Aruch HaShulchan specifies that the “parasha” is the open or closed section; the marks “third”, “fourth”… printed in the Chumashim count for nothing here. When a section ends in the middle of a verse – he cites “It was after the plague” (Pinchas), “The sons of Yaakov were twelve” (Vayishlach) and “from Eilat and Etzion Gever” (Devarim) –, it seems to him that one stops there all the same: the rule “a verse that Moshe did not divide, we do not divide” is no objection, since here Moshe did divide it."),
        H("tous", [
            R("bh", (494, 1), cite='''ובפרשת יתרו ובפרשת ואתחנן קורין אף בצבור בטעם התחתון ויש נוהגין לקרות בצבור לעולם בטעם העליון דהיינו אף בפרשת יתרו ובפרשת ואתחנן רק היחיד הקורא לעצמו קורא בשני'''),
            R("kh", 5, cite='''בקריאת עשרת הדברות צריך ליזהר לקרותם שמו"ת כפי הטעמים של סדר הפסוקים'''),
            R("kh", 5, cite='''אמנם לא תרצח לא תנאף לא תגנוב לא תענה צריך ליזהר לקרותם שנים מקרא בבת אחת ואח"כ אחד תרגום בב"א לפי שכולם פסוק אחד'''),
            R("kh", 5, cite='''ואין לקרות פסוק אחד פסקי פסקי שמו"ת אלא צריך לקרות כל הפסוק שלם תחלה שנים מקרא ואח"כ אחד תרגום'''),
        ],
            "Les Dix Paroles ont deux cantillations : l'une fait de chaque Parole un seul verset (ta'am 'elyon), l'autre suit le découpage ordinaire des versets (ta'am ta'hton). Le Béour Halakha résume les A'haronim : à Chavouot on lit en public selon la première ; aux parachiot Yitro et Vaet'hanan on lit, même en public, selon la seconde, et certains lisent toujours en public selon la première – seul le particulier qui lit pour lui-même lit alors selon la seconde. Le Kaf ha'Haïm écrit de même que, pour Chnayim mikra, on lit les Dix Paroles selon la cantillation de l'ordre des versets ; « Tu ne tueras pas, tu ne commettras pas d'adultère, tu ne voleras pas, tu ne témoigneras pas… » forment un seul verset : on les lit ensemble deux fois, puis leur targoum ensemble. Et l'on ne lit pas un verset par morceaux : on lit d'abord le verset entier deux fois, puis son targoum.",
            "The Ten Commandments have two cantillations: one makes each commandment a single verse (ta'am elyon), the other follows the ordinary division into verses (ta'am tachton). The Beur Halacha sums up the Acharonim: on Shavuot the public reading follows the first; in parashiot Yitro and Va'etchanan one reads, even in public, according to the second, and some always read in public according to the first – only the individual reading for himself then reads according to the second. The Kaf HaChaim likewise writes that for Shnayim mikra one reads the Ten Commandments with the cantillation of the order of the verses; “You shall not murder, you shall not commit adultery, you shall not steal, you shall not bear [false] witness…” form a single verse: one reads them together twice, then their targum together. And a verse is not read piecemeal: one first reads the whole verse twice, then its targum."),
        H("ashkenaze", [
            R("bht", 1, cite='''ואיסור גדול להפסיק בקריאת שמו"ת בדיבור'''),
            R("ma", 11, cite='''וטוב שלא יפסיק כלל בשיחה [כ"ה]'''),
            R("ahs", 7, cite='''ויש מי שכתב שיש איסור להפסיק בדיבור בקריאת שנים מקרא ואחד תרגום (באר היטב סעיף קטן א). ותמיה לומר כן, דבלא ברכה מה שייך הפסק?'''),
            R("ahs", 7, cite='''ועוד, דאותם שקורין פרשה בכל יום – הלא מפסיקין הרבה, ולכן אין לזה מקום מדינא'''),
        ],
            "S'interrompre : interdit, ou seulement à éviter ? Le Baèr Hétev écrit que c'est « un grand interdit » de s'interrompre par la parole pendant Chnayim mikra. Le Maguen Avraham, après avoir décrit la haftara et ce qu'on lit ensuite, écrit au nom de la Knesset haGuedola qu'il est bon de ne pas s'interrompre du tout par une conversation. L'Aroukh haChoul'han cite le Baèr Hétev et s'en étonne : là où il n'y a pas de bénédiction, que vient faire la notion d'interruption ? Et ceux qui lisent une section chaque jour s'interrompent bien davantage ; cela n'a donc pas de fondement selon la loi.",
            "Interrupting: forbidden, or merely to be avoided? The Ba'er Hetev writes that it is “a great prohibition” to interrupt Shnayim mikra by speaking. The Magen Avraham, after describing the haftarah and what is read after it, writes in the name of the Knesset HaGedolah that it is good not to interrupt at all with conversation. The Aruch HaShulchan quotes the Ba'er Hetev and wonders at it: where there is no blessing, what place is there for the notion of an interruption? And those who read a section each day interrupt far more; so this has no basis in law."),
        H("tous", [
            R("sch", 745, cite='''כמו שאין אומרים כשאנו קורין בתורה על משה ועל אהרן זכרונם לטובה'''),
            R("sch", 745, cite='''וכן כשאדם אומר שנים מקרא ואחד תרגום כשמזכיר הצדיקים שנזכר בפסוקים אין צריך לומר ז"ל'''),
        ],
            "Celui qui dit Chnayim mikra n'a pas à ajouter « de mémoire bénie » quand il nomme les justes mentionnés dans les versets, de même qu'on ne le dit pas de Moché et d'Aharon quand on lit la Torah (Séfer 'Hassidim).",
            "One who says Shnayim mikra need not add “of blessed memory” when naming the righteous mentioned in the verses, just as it is not said of Moshe and Aharon when the Torah is read (Sefer Chasidim)."),
    ]},
    {"titre": "תרגום ופירוש רש״י", "titre_fr": "Targoum et Rachi", "titre_en": "Targum and Rashi", "halakhot": [
        H("tous", [
            R("sa", 2, cite='אם למד הפרשה בפירוש רש"י חשוב כמו תרגום וירא שמים יקרא תרגום וגם פרש"י'),
            R("hid", "299490", cite="מעיקר הדין יוצאים אבל מבואר בשולחן ערוך שיש לעשות את שניהם",
              passage='2. מעיקר הדין יוצאים אבל מבואר בשולחן ערוך שיש לעשות את שניהם. בפסוקים שאין רש"י יש לחזור על הפסוק שלושה פעמים.'),
            R("mb", 6, cite='כי התרגום יש לו מעלה שניתן בסיני וגם הוא מפרש כל מלה ומלה ופירש"י יש לו מעלה שהוא מפרש את הענין ע"פ מדרשי חז"ל יותר מהתרגום'),
            R("hid", "262007", passage='והסביר המשנה ברורה (סק"ו) כי התרגום יש לו מעלה שניתן בסיני וגם הוא מפרש כל מילה ומילה. ופירוש רש"י יש לו מעלה שהוא מפרש את העניין על פי מדרשי חז"ל יותר מהתרגום.'),
        ],
            "Celui qui a étudié la paracha avec le commentaire de Rachi est considéré comme ayant lu le targoum ; mais celui qui craint le Ciel lit le targoum et aussi Rachi (Choul'han Aroukh). Le Rav Binyamin Chmouéli (Hidabroot) le résume ainsi : on est quitte selon le strict droit, mais le Choul'han Aroukh demande les deux ; et, pour qui lit Rachi à la place du targoum, un verset que Rachi ne commente pas se lit trois fois. Le Rav Hillel Meirs (Hidabroot) explique, avec la Michna Beroura, que le targoum a la qualité d'avoir été donné au Sinaï et de traduire chaque mot, et Rachi celle d'expliquer le sujet selon les midrachim des Sages, davantage que le targoum.",
            "One who studied the parasha with Rashi’s commentary is considered to have read the targum; but one who fears Heaven reads the targum and Rashi as well (Shulchan Aruch). Rav Binyamin Shmueli (Hidabroot) sums it up: by strict law one fulfils the obligation, but the Shulchan Aruch calls for both; and, for one who reads Rashi instead of the targum, a verse on which Rashi does not comment is read three times. Rav Hillel Meirs (Hidabroot) explains, with the Mishnah Berurah, that the targum has the merit of having been given at Sinai and of translating every word, and Rashi that of explaining the matter according to the midrashim of the Sages, more than the targum."),
        H("ashkenaze", [
            R("mb", 4, cite='אבל אם קראה בשאר לעז שהוא מפרש רק את המלות לחוד לא יצא י"ח במקום תרגום לפי שהתרגום מפרש כמה דברים שאין להבין מתוך המקרא'),
            R("mb", 5, cite='ואותן פסוקים שאין עליהם פירש"י יקרא אותן ג"פ. מי שאינו בר הכי שיבין את פירש"י ראוי לקרות בפירוש התורה שיש בלשון אשכנז בזמנינו כגון ספר צאינה וראינה וכיוצא בו המבארים את הפרשה ע"פ פירש"י ושאר חכמינו ז"ל הבנוים על יסוד התלמוד'),
            R("mb", 6, cite='ובאמת כן ראוי לנהוג לכל אדם שילמוד בכל שבוע הסדרה עם פירש"י לבד התרגום'),
            R("ksa", 11, cite='גַּם יֵשׁ לוֹ לְכָל יְרֵא שָׁמַיִם, לִלְמוֹד פֵּרוּשׁ רַשִׁ"י עַל הַסִּדְרָה, וְאִם לָאו בַּר הָכִי הוּא יִלְמַד פֵּרוּשׁ אַשְׁכְּנַזִי (לוֹעֲזִי) עַל הַסִּדְרָה, כְּגוֹן סֵפֶר "צְאֶינָה וּרְאֶינָה" וְכַדּוֹמֶה, שֶׁיָּבִין עִנְיַן הַסִּדְרָה'),
            R("sahr", 2, cite="הרי זה מועיל יותר מהתרגום שהוא מפרש יותר ויש אומרים שהתרגום זכה מפני שניתן בסיני כגון יגר שהדותא והעיקר כסברא הראשונה"),
            R("sahr", 2, cite='ומכל מקום כל ירא שמים יש לו לקרות התרגום וגם פירוש רש"י ומי שאינו מבין פירוש רש"י יש לו לקרות בפירוש התורה שבלשון לע"ז שמבין'),
        ],
            "Rachi tient lieu de targoum parce qu'il explique le texte comme le targoum, et davantage ; en revanche, une traduction dans une autre langue qui ne rend que les mots ne remplace pas le targoum, car le targoum explique des choses que le texte seul ne laisse pas comprendre. Celui qui lit Rachi à la place du targoum lit trois fois les versets que Rachi ne commente pas. La Michna Beroura écrit qu'il convient en vérité que chacun étudie chaque semaine la paracha avec Rachi, en plus du targoum ; celui qui ne peut pas comprendre Rachi lira un commentaire de la Torah dans une langue qu'il comprend (Choul'han Aroukh haRav) ; la Michna Beroura et le Kitsour Choul'han Aroukh donnent en exemple le Tseéna ourééna, en yiddish, la Michna Beroura précisant qu'il convient de lire un commentaire qui explique la paracha selon Rachi et les Sages. Le Choul'han Aroukh haRav écrit que Rachi est plus utile que le targoum, parce qu'il explique davantage ; il rapporte un autre avis, pour qui le targoum l'emporte parce qu'il a été donné au Sinaï, et retient le premier comme l'essentiel ; il dit lui aussi que celui qui craint le Ciel lit les deux.",
            "Rashi takes the place of the targum because he explains the text as the targum does, and more; but a translation into another language that renders only the words does not replace the targum, since the targum explains things that cannot be understood from the text alone. One who reads Rashi instead of the targum reads three times the verses on which Rashi does not comment. The Mishnah Berurah writes that it is truly fitting for everyone to study the parasha each week with Rashi, besides the targum; one who cannot understand Rashi should read a commentary on the Torah in a language he understands (Shulchan Aruch HaRav); the Mishnah Berurah and the Kitzur Shulchan Aruch give the Yiddish Tze’enah U-re’enah as an example, the Mishnah Berurah specifying that it is fitting to read a commentary that explains the parasha according to Rashi and the Sages. The Shulchan Aruch HaRav writes that Rashi is more useful than the targum, because he explains more; he reports another view, for which the targum prevails because it was given at Sinai, and holds the first to be the main one; he too says that one who fears Heaven reads both."),
        H("sefarade", [
            R("kyy", 3, cite="אף מי שאינו מבין כל כך את שפת התרגום, עליו לקרוא את הפרשה שנים מקרא ואחד תרגום. וירא שמים יקרא גם תרגום וגם פירוש רש״י על הפרשה"),
            R("kh", 22, cite='וכ"כ רש"ל ביש"ש (קדושין פ"ב סי\' י"ד) וכתב דאם אינו יכול ללמוד שניהם יקרא פרש"י ולא תרגום יעו"ש. אבל לפי מ"ש חכמי האמת יש קפידא בתרגום ולכן אם אין לו שהות ללמוד שניהם ילמוד תרגום'),
            R("kh", 22, cite='ומיהו אם הולך בדרך ואין לו כ"א מקרא ורש"י אז יש לסמוך על המתירין ויקרא ב"פ מקרא ואחד פרש"י'),
            R("kav", "yaron1", passage='אף מי שאינו מבין כל כך את שפת התרגום, עליו לקרוא את הפרשה שנים מקרא ואחד תרגום. וירא שמים יקרא גם תרגום וגם פירוש רש"י על הפרשה.'),
        ],
            "Même celui qui ne comprend pas bien la langue du targoum doit lire la paracha deux fois dans le texte et une fois dans le targoum, et celui qui craint le Ciel lit aussi Rachi (Kitsour Yalkout Yossef ; de même le Rav Yaron Achkenazi, Kav haHalakha haSefaradi). Le Kaf ha'Haïm rapporte que, pour le Maharchal, celui qui ne peut pas étudier les deux lit Rachi et non le targoum ; mais que, d'après les kabbalistes, on tient au targoum, si bien que celui qui n'a pas le temps d'étudier les deux étudie le targoum (au nom du Birké Yossef et des Cha'arei Techouva). Il ajoute qu'en voyage, celui qui n'a que le texte et Rachi peut s'appuyer sur ceux qui permettent, et lire deux fois le texte et une fois Rachi.",
            "Even one who does not understand the language of the targum well must read the parasha twice in the text and once in the targum, and one who fears Heaven reads Rashi as well (Kitzur Yalkut Yosef; likewise Rav Yaron Ashkenazi, Kav HaHalacha HaSefaradi). The Kaf HaChaim reports that, for the Maharshal, one who cannot study both reads Rashi and not the targum; but that, according to the kabbalists, the targum is insisted upon, so that one who has no time to study both studies the targum (in the name of the Birkei Yosef and the Shaarei Teshuvah). He adds that when travelling, one who has only the text and Rashi may rely on those who permit it, and read the text twice and Rashi once."),
        H("tous", [
            R("mb", 6, cite='מי שאין בידו תרגום רק החומש לבד יש לו יקרא שני פעמים מקרא ואח"כ כשיזדמן לו תרגום יאמר'),
            R("ksa", 11, cite="וּמִי שֶׁהוּא בַּדֶּרֶךְ וְאֵין לוֹ רַק חֻמָּשׁ בְּלִי תַּרְגּוּם, יִקְרָא שְׁתֵּי פְּעָמִים מִקְרָא. וּכְשֶׁיָּבוֹא לְמָקוֹם שֶׁיִּהְיֶה לוֹ תַּרְגּוּם, יִקְרָא הַתַּרְגּוּם"),
            R("sahr", 6, cite="ואם אין לו תרגום יקרא מקרא ב' פעמים ואח\"כ כשיהיה לו תרגום יקראנו"),
            R("kh", 16, cite='כתב בסדה"י אם אין בידו חומש עם תרגום יקרא שנים מקרא וכשיגיע לישוב יקרא התרגום. והביאו מ"א סק"ד'),
            R("kh", 16, cite='ול"נ דכדי להשלים פרשיותיו עם הצבור יש לקרות ג"פ מקרא כמו הפסוקים שאין להם תרגום כיון דלא אפשר ליה בענין אחר ואח"כ כשיגיע לישוב אם אפשר חוזר לקרות שמו"ת'),
        ],
            "Celui qui n'a qu'un 'Houmach sans targoum – en voyage, dit le Kitsour Choul'han Aroukh – lit le texte deux fois, puis le targoum quand il en trouve un (Michna Beroura ; Kitsour Choul'han Aroukh ; Choul'han Aroukh haRav ; le Kaf ha'Haïm le rapporte au nom du Séder haYom, cité par le Maguen Avraham). Le Kaf ha'Haïm propose, pour achever malgré tout la paracha avec la communauté, de lire alors le texte trois fois, comme un verset sans targoum, puis, une fois arrivé, de relire si possible Chnayim mikra véé'had targoum.",
            "One who has only a Chumash without targum – when travelling, says the Kitzur Shulchan Aruch – reads the text twice, and the targum when he finds one (Mishnah Berurah; Kitzur Shulchan Aruch; Shulchan Aruch HaRav; the Kaf HaChaim reports it in the name of the Seder HaYom, cited by the Magen Avraham). The Kaf HaChaim suggests that, in order to complete the parasha with the congregation all the same, he should then read the text three times, like a verse without targum, and once he arrives, read Shnayim mikra ve-echad targum again if possible."),
        H("ashkenaze", [
            R("bh", 2, cite='''היוצא מדברינו דאין לנו פוסק מפורש שיסבור דהתרגום חשוב טפי מפירש"י ומ"מ נראה לדינא לנהוג כהב"י דאף שפירש"י מפרש את הענין יותר מתרגום אבל מפני שיש כמה תיבות וגם כמה פסוקים שאין עליהם פירושו של רש"י וא"כ לא נשאר לו שם כ"א מקרא לבד והתרגום מפרש כל פסוק וכל תיבה'''),
            R("ahs", 12, cite='''והגדולים הסכימו דדווקא תרגום אונקלוס, ואין יוצאין בדבר אחר, שהתרגום קדוש וניתן מסיני. וכן הוא על פי חכמת הקבלה, וכך נוהגים כל ישראל, וחלילה לשנות מזה'''),
            R("ahs", 12, cite='''ואם אינו מצפה שיבא תרגום לידו – נראה לעניות דעתי שצריך לקרא המקרא שלוש פעמים, לפי הטעמים שנתבארו'''),
        ],
            "Le Béour Halakha conclut de son examen qu'aucun décisionnaire ne dit expressément que le targoum l'emporte sur Rachi ; il lui semble pourtant qu'en pratique on suit le Beit Yossef (lire le targoum et aussi Rachi) : Rachi explique davantage le sujet, mais il y a des mots, et même des versets, qu'il ne commente pas, pour lesquels il ne resterait que le texte seul, alors que le targoum explique chaque verset et chaque mot. L'Aroukh haChoul'han écrit que les grands décisionnaires se sont accordés : il faut précisément le targoum d'Onkelos, et l'on n'est quitte par rien d'autre, car le targoum est saint et a été donné au Sinaï ; ainsi le veut aussi la Kabbale, ainsi fait tout Israël, « et loin de nous d'y rien changer ». Celui qui n'espère pas avoir un targoum entre les mains doit, à son humble avis, lire le texte trois fois.",
            "The Beur Halacha concludes from its analysis that no authority states explicitly that the targum outranks Rashi; yet it seems to it that in practice one follows the Beit Yosef (reading the targum and also Rashi): Rashi explains the subject more, but there are words, and even verses, on which he does not comment, where only the bare text would remain, whereas the targum explains every verse and every word. The Aruch HaShulchan writes that the great authorities have agreed: it must be Targum Onkelos specifically, and nothing else discharges the obligation, for the targum is holy and was given at Sinai; so too according to Kabbalah, so all Israel practise, “and far be it from us to change this”. One who does not expect a targum to come to hand must, in his humble opinion, read the text three times."),
        H("sefarade", [
            R("kh", 19, cite='''פי' שצריך לקרות שנים מקרא ואחד פירוש אבל בפירוש לחודיה לא סגי. ופסוקים שאין להם פירוש צריך לקרותם ג"פ מקרא כמו פסוקים שאין להם תרגום'''),
            R("kh", 20, cite='''מיהו לפי חכמי המקו' משמע דוקא תרגום'''),
            R("kh", 23, cite='''ונראה דאפי' אם לא הותר לקרות הפרשה שמו"ת בליל הששי יכול לקרות פרש"י בליל ו' כדי לצאת י"ח וירא שמים יצא ידי שתיהם תרגום ורש"י'''),
        ],
            "« S'il a étudié la paracha avec Rachi » : le Kaf ha'Haïm explique qu'il faut lire deux fois le texte et une fois le commentaire – le commentaire seul ne suffit pas – et que les versets sans commentaire se lisent trois fois, comme les versets sans targoum. Il rapporte que, d'après les kabbalistes, il faut précisément le targoum. Et il rapporte du Roua'h 'Haïm que, même si l'on ne permet pas de lire Chnayim mikra la nuit de jeudi à vendredi, on peut lire Rachi cette nuit-là pour s'acquitter ; celui qui craint le Ciel s'acquitte des deux, targoum et Rachi.",
            "“If one studied the parasha with Rashi”: the Kaf HaChaim explains that one must read the text twice and the commentary once – the commentary alone is not enough – and that verses without commentary are read three times, like verses without targum. He reports that according to the kabbalists it must be the targum specifically. And he reports from the Ruach Chaim that even if reading Shnayim mikra on Thursday night is not permitted, one may read Rashi that night to fulfil the obligation; one who fears Heaven fulfils both, targum and Rashi."),
        H("tous", [
            R("taz", 1, cite='''דלא מבעיא ראובן ושמעון שהם שמות השבטים ויש בהם ודאי קדושה בטעם שמות אלו אלא אפי' עטרות ודיבון שהם שמות ערי א"י ואפש' שקראו אות' העכו"ם אפ"ה צריך לקרות' ג"פ'''),
            R("kh", 17, cite='''ורבינו בחיי כתב לפי שיש באלו העיירות שמות של ע"ז ושלא תאמר כיון שהתרגום הוא פי' הכתב אין לנו לתרגם הכתוב הזה כי יש בו זכרון ע"ז וע"כ באו חכמים לומר שאף הפסוק הזה ראוי לתרגמו ושלא להקל בו'''),
            R("ahs", 11, cite='''ולא מפני התרגום, שהרי גם בלשון התרגום השמות שוין ללשון המקרא, אלא משום דצריך שלושה פעמים'''),
        ],
            "Pourquoi le Talmud nomme-t-il justement « Atarot et Divon » ? Le Taz : non seulement « Réouven et Chimon », noms des tribus, qui portent certainement une sainteté, mais même « Atarot et Divon », noms de villes de la terre d'Israël que les nations ont peut-être ainsi appelées, se lisent trois fois. Rabbénou Be'hayé, cité par le Kaf ha'Haïm : ces villes portent des noms d'idolâtrie, et l'on aurait pu dire qu'il ne faut pas traduire ce verset qui en porte le souvenir ; les Sages enseignent que même ce verset mérite son targoum, sans allègement. L'Aroukh haChoul'han : pour des noms comme « Réouven et Chimon », ce n'est pas à cause du targoum – les noms y sont les mêmes que dans le texte – mais parce qu'il faut trois lectures.",
            "Why does the Talmud name precisely “Atarot and Divon”? The Taz: not only “Reuven and Shimon”, names of the tribes, which certainly carry holiness, but even “Atarot and Divon”, names of towns of the Land of Israel that the nations may have given, are read three times. Rabbenu Bachya, quoted by the Kaf HaChaim: these towns bear names of idolatry, and one might have said that this verse, which recalls it, should not be translated; the Sages teach that even this verse deserves its targum, with no leniency. The Aruch HaShulchan: for names such as “Reuven and Shimon”, it is not because of the targum – the names are the same there as in the text – but because three readings are required."),
    ]},
    {"titre": "טעמים, ספר תורה וחומש", "titre_fr": "Te'amim, séfer Torah, 'Houmach", "titre_en": "Cantillation, Torah scroll, Chumash", "halakhot": [
        H("tous", [
            R("kyy", 14, cite="אולם גם מי שאינו יודע לקרוא את הפרשה עם הטעמים, חייב בקריאת הפרשה שנים מקרא ואחד תרגום. וחובה קדושה על ההורים והמלמדים ללמד את בני ישראל בטעמי המקרא"),
            R("mb", 17, cite='מכאן שניגון הטעמים אינו מעכב לגבי שמו"ת'),
            R("hid", "15385", cite="ולכתחילה יש לקראה בטעמיה, אבל מי שאינו בקי בטעמים יקראנה ללא טעמים"),
        ],
            "On lit les versets avec la cantillation (te'amim) ; mais celui qui ne la connaît pas reste obligé de lire Chnayim mikra, et la mélodie des te'amim n'est pas indispensable (Kitsour Yalkout Yossef ; Michna Beroura, d'après le Pri Megadim). Le Kitsour Yalkout Yossef ajoute que parents et maîtres ont le devoir sacré d'enseigner les te'amim aux enfants d'Israël. Le Rav Binyamin Chmouéli (Hidabroot) répond de même : a priori avec les te'amim, et sans eux pour qui ne les connaît pas.",
            "The verses are read with the cantillation (te’amim); but one who does not know it is still obligated to read Shnayim mikra, and the melody of the te’amim is not indispensable (Kitzur Yalkut Yosef; Mishnah Berurah, after the Pri Megadim). The Kitzur Yalkut Yosef adds that parents and teachers have a sacred duty to teach the children of Israel the te’amim. Rav Binyamin Shmueli (Hidabroot) answers likewise: ideally with the te’amim, and without them for one who does not know them."),
        H("sefarade", [
            R("kyy", 14, cite="פסוקי המקרא צריך לקוראם בטעמי המקרא, והתרגום בלי טעמים, בדוקא"),
            R("bih", (2, "Lech Lecha", "Lekh Lekha", "Lech Lecha", "לך לך", 11), cite="ואין קוראים התרגום בטעמים, כנזכר בשער טעמי המצוות"),
            R("kh", 12, cite='התרגום א"צ לקרות בטעמים. כ"כ רבינו מהרח"ו ז"ל שקבל מרבינו האר"י ז"ל. ובס\' קרבן שבת פ"ה דף י"ד ביאר הטעם עד"ה ושם מפורש דהתרגום צריך לקרותו בלא טעמים דוקא ויש קפידא בזה'),
        ],
            "Le targoum se lit sans les te'amim : le Kitsour Yalkout Yossef écrit que c'est « précisément » ainsi, le Ben Ich 'Haï le rapporte d'après le Cha'ar Ta'amei haMitsvot, et le Kaf ha'Haïm écrit, au nom de Rabbi 'Haïm Vital qui l'avait reçu du Ari, qu'il n'y a pas à lire le targoum avec les te'amim, puis rapporte du Korban Chabbat qu'il faut le lire précisément sans te'amim et qu'on y tient.",
            "The targum is read without the te’amim: the Kitzur Yalkut Yosef writes that this is “precisely” so, the Ben Ish Chai reports it from the Shaar Taamei HaMitzvot, and the Kaf HaChaim writes, in the name of Rabbi Chaim Vital who received it from the Ari, that the targum need not be read with the te’amim, then reports from the Korban Shabbat that it must be read precisely without te’amim and that this is insisted upon."),
        H("tous", [
            R("mb", 2, cite='מי שהוא בקי בטעם ובנקודות בע"פ טוב להדר לקרות בס"ת גופא'),
            R("sahr", 4, cite="מי שהוא רגיל בפסקי טעמים בעל פה טוב שיקרא שנים מקרא בספר תורה כשר"),
            R("kyy", 17, cite="מי שבקי בקריאת הפרשה בטעמי המקרא והנקודות כראוי, מצוה מן המובחר לקרוא שנים מקרא מתוך ספר תורה, ויקרא התרגום מתוך החומש"),
            R("kyy", 17, cite="אולם אם אינו בקי מוטב שיקראנה מתוך חומש שיש בו הטעמים והנקודות, ולא יקראנה קריאה משובשת בספר תורה. ופשוט שאין לו לברך על קריאתה"),
            R("kh", 7, cite='ואם אינו בקי יותר טוב שיקרא בחומש שמו"ת ממה שיקרא בס"ת קריאה משובשת'),
            R("kh", 7, cite='ואף אם הוא בקי וקורא בס"ת אין לברך בה"ת שלא נתקנה אלא בצבור'),
            R("malka", "484", cite="זה נקרא כלומד מספר לענין זה",
              passage='2) כהמשך לשאלה הקודמת האם מותר ללמוד במכשיר תורה שבכתב ולהעביר שניים מקרא ואחד תרגום? [...] לגבי 1 ו 2 אין כ"כ נ"מ בשאלות הנ"ל. אבל אם חשוב לך - זה נקרא כלומד מספר לענין זה.'),
        ],
            "Celui qui connaît par cœur la vocalisation et les te'amim fait bien de lire le texte dans un séfer Torah (Michna Beroura ; Choul'han Aroukh haRav, qui précise : un séfer Torah cachère) ; pour le Kitsour Yalkout Yossef, c'est la meilleure façon d'accomplir la mitsva, le targoum se lisant alors dans un 'Houmach. Celui qui ne les connaît pas lit plutôt dans un 'Houmach vocalisé, avec les te'amim, que de lire de façon fautive dans le séfer Torah (Kitsour Yalkout Yossef ; Kaf ha'Haïm). Même celui qui s'y connaît et lit dans le séfer Torah ne récite pas la bénédiction de la Torah, qui n'a été instituée que pour la lecture en public (Kaf ha'Haïm) ; le Kitsour Yalkout Yossef écrit de même qu'il est évident qu'on ne récite pas de bénédiction sur cette lecture. À la question de lire Chnayim mikra sur un appareil électronique, le Rav Emmanuel Molkandov (beit hora'a « Halakha lema'assé » du Rav Ofir Malka) répond que la question a peu de conséquence pratique, mais que, si l'on y tient, cela compte comme étudier dans un livre.",
            "One who knows the vowels and te’amim by heart does well to read the text from a Torah scroll (Mishnah Berurah; Shulchan Aruch HaRav, which specifies: a kosher Torah scroll); for the Kitzur Yalkut Yosef, this is the best way to fulfil the mitzvah, the targum then being read from a Chumash. One who does not know them should rather read from a Chumash with vowels and te’amim than read wrongly from the Torah scroll (Kitzur Yalkut Yosef; Kaf HaChaim). Even one who knows them and reads from the Torah scroll does not recite the blessing over the Torah, which was instituted only for public reading (Kaf HaChaim); the Kitzur Yalkut Yosef likewise writes that it is obvious that no blessing is said over this reading. Asked about reading Shnayim mikra on an electronic device, Rav Emmanuel Molkandov (the “Halacha LeMaaseh” beit hora’ah of Rav Ofir Malka) answers that the question has little practical consequence, but that, if it matters to the asker, it counts as studying from a book."),
        H("ashkenaze", [
            R("taz", 2, cite='''ועוד אני אומר על ירא שמים שיראה לקרות בפני עצמו בס"ת הסדרה לכל הפחות פעם א' ואח"כ עם החזן פעם שנית דהקריא' בחומש לבד אין יוצא בה שפיר דבעי' דברים שבכת' והיינו ס"ת שלימה כדינה ויש לו להשלים זה עד ש"ת וכך נהגתי מעודי'''),
        ],
            "Le Taz ajoute, pour celui qui craint le Ciel : qu'il veille à lire lui-même la paracha dans un séfer Torah au moins une fois, puis une seconde fois avec l'officiant ; car la lecture dans un 'Houmach seul n'acquitte pas pleinement : il faut « ce qui est écrit », c'est-à-dire un séfer Torah entier et conforme. On peut compléter cela jusqu'à Sim'hat Torah – « et c'est ainsi que j'ai toujours fait ».",
            "The Taz adds, for one who fears Heaven: let him see to reading the parasha by himself from a Torah scroll at least once, and then a second time with the reader; for reading from a Chumash alone does not properly fulfil it: it requires “what is written”, that is, a complete and valid Torah scroll. This may be made up until Simchat Torah – “and so I have always done”."),
        H("sefarade", [
            R("kh", 13, cite='''צריך ליזהר בקריאת המקרא בנגינת הטעמים בשלם שבפנים'''),
            R("kh", 13, cite='''שיזהרו בקריאת שמו"ת לקרות המקרא כל שישנו בנותן טעם לשבח'''),
            R("kyy", 17, cite='''ובפרט מי שהוא שליח צבור הקורא בתורה, ובקי בקריאת הפרשה בטעמיה, ורוצה לקרוא הפרשה מתוך הספר הנמצא בהיכל, כדי שיהיה רגיל בקריאת הפרשה, שיש להקל בזה. ונכון שלא לטלטל את הספר תורה לתיבה'''),
        ],
            "Autant le targoum se lit sans te'amim, autant il faut veiller à lire le texte avec la mélodie des te'amim, le mieux possible : le Kaf ha'Haïm rapporte, du Ma'hazik Berakha, que le pieux Rabbi Moché haCohen en avertissait beaucoup ses élèves. Le Kitsour Yalkout Yossef permet en particulier à l'officiant qui lit la Torah, s'il connaît la paracha avec ses te'amim et veut la lire dans le séfer qui se trouve dans le heikhal pour s'y exercer, de le faire ; il convient de ne pas déplacer le séfer Torah jusqu'à la téva.",
            "Just as the targum is read without te'amim, so one must take care to read the text with the melody of the te'amim, as fully as possible: the Kaf HaChaim reports, from the Machazik Berachah, that the pious Rabbi Moshe HaKohen used to warn his students strongly about this. The Kitzur Yalkut Yosef allows in particular the reader who reads the Torah in public, if he knows the parasha with its te'amim and wishes to read it from the scroll kept in the heichal in order to practise, to do so; it is proper not to carry the Torah scroll to the tevah."),
    ]},
    {"titre": "קריאת הציבור", "titre_fr": "La lecture à la synagogue", "titre_en": "The public reading", "halakhot": [
        H("ashkenaze", [
            R("mb", 2, cite='אבל לא יקרא אחד מקרא ואחד תרגום ויכוין לשמוע מהש"ץ אלא צריך לקרות ב"פ מקרא חוץ ממה ששמע מהש"ץ אם לא שקרא אז ג"כ בפיו'),
            R("mb", 2, cite='וע\' במ"א סק"ח שכ\' בשם לחם חמודות דבדיעבד יוצא פ"א במה ששמע מהש"ץ ויש אחרונים שמחמירין אפי\' דיעבד'),
            R("sahr", 8, cite='ויש אומרים שיוצא ידי חובתו בשמיעת הקריאה מהש"ץ אם שמע כל הפרשה בבירור ודי שיקרא עוד פעם אחת עם תרגום אלא שלכתחלה אין לסמוך על השמיעה מטעם שנתבאר בסימן נ"ט אבל יש אומרים שאינו יוצא כלל בשמיעת הש"ץ שמלבד שמיעה זו חייב לקרות שנים מקרא ואחד תרגום כמו שנתבאר למעלה ובשעת הדחק יש לסמוך על סברא הראשונה'),
            R("hid", "262007", cite="אם הוא קורא בפיו עם הבעל קורא זה עולה לו"),
        ],
            "On ne se contente pas de lire une fois le texte et le targoum en comptant sur la lecture entendue de l'officiant : il faut lire soi-même deux fois le texte, en plus de ce qu'on a entendu, à moins d'avoir lu alors avec lui, de sa propre bouche. A posteriori, selon le Maguen Avraham au nom du Le'hem 'Hamoudot, l'écoute compte pour une fois ; d'autres A'haronim sont stricts même a posteriori (Michna Beroura). Le Choul'han Aroukh haRav rapporte ces avis et permet, en cas de nécessité, de s'appuyer sur l'avis selon lequel celui qui a bien entendu toute la paracha n'a plus qu'à la lire une fois avec le targoum. Le Rav Hillel Meirs (Hidabroot) répond, avec la Michna Beroura, que lire de sa bouche avec le lecteur compte pour une fois.",
            "One may not read the text once with the targum and rely on hearing the reader: one must read the text twice oneself, besides what one heard, unless one read along with him at the time, with one’s own mouth. After the fact, according to the Magen Avraham citing the Lechem Chamudot, hearing counts as one reading; other Acharonim are strict even after the fact (Mishnah Berurah). The Shulchan Aruch HaRav reports these views and, in case of need, allows relying on the view that one who heard the whole parasha clearly need only read it once more with the targum. Rav Hillel Meirs (Hidabroot) answers, with the Mishnah Berurah, that reading along with one’s mouth with the reader counts as one reading."),
        H("sefarade", [
            R("kyy", 10, cite="מי שהשעה דחוקה לו ביותר, ואין לו פנאי כלל לקרוא לעצמו את הפרשה שנים מקרא ואחד תרגום, נכון להורות לו שיקרא בלחש את כל הפרשה עם השליח צבור הקורא בתורה, פסוק בפסוק, ושוב יחזור ויקראנה פעם שניה בביתו, ואחר כך יקרא פעם אחת את כל התרגום, ויצא ידי חובתו. וכן השליח צבור הקורא בתורה, רשאי לקרות הפרשה בהכנתה לפחות פעם אחת מתחלתה ועד סופה, ופעם שניה כשקורא אותה בצבור, ואחר כך יקרא התרגום של כל הפרשה פעם אחת ויוצא ידי חובה. אבל אין לסמוך על מה ששומע קריאת הפרשה מהשליח צבור"),
        ],
            "On ne s'appuie pas sur la lecture entendue de l'officiant. Mais à celui qui est vraiment pressé et n'a pas le temps de lire seul la paracha, il convient d'indiquer de lire à voix basse toute la paracha avec l'officiant, verset par verset, puis de la relire une seconde fois chez lui, puis de lire une fois tout le targoum : il est quitte. De même, l'officiant qui lit la Torah en public peut compter sa préparation, au moins une lecture complète, et sa lecture publique, puis lire une fois le targoum.",
            "One does not rely on hearing the reader. But one who is truly pressed and has no time to read the parasha by himself should be told to read the whole parasha in a whisper with the reader, verse by verse, then to read it a second time at home, then to read the whole targum once: he has fulfilled his obligation. Likewise, the reader who reads the Torah in public may count his preparation, at least one complete reading, and his public reading, then read the targum once."),
        H("ashkenaze", [
            R("sa", 5, cite="יכול לקרות הפרשה שנים מקרא ואחד תרגום בשעת קריאת התורה"),
            R("mb", 14, cite='ובסימן קמ"ו במ"א סק"ה הביא בשם השל"ה שמחמיר בזה אלא הכל צריכין לשמוע הקריאה מפי הש"ץ וכן הוא דעת הגר"א שהובא בספר מעשה רב דצריך לשמוע כל תיבה ותיבה ולראות בחומש ולא יסייע להקורא כלל'),
            R("mb", 14, cite='ומ"מ נראה דלקרוא בלחש מלה במלה עם הש"ץ אין להחמיר בזה כיון שמכוין אז גם לשמוע כל תיבה מפי הש"ץ והמ"א הביא שם בשם מטה משה דלכתחלה נכון לעשות כן וכ"כ כמה אחרונים'),
        ],
            "Le Choul'han Aroukh permet de lire Chnayim mikra pendant la lecture publique de la Torah. La Michna Beroura rapporte que le Maguen Avraham cite le Chla, qui est strict : tous doivent écouter la lecture de la bouche du lecteur ; et que tel est l'avis du Gaon de Vilna (Ma'assé Rav) : il faut écouter chaque mot en suivant dans un 'Houmach, sans accompagner du tout le lecteur. La Michna Beroura estime cependant qu'il n'y a pas lieu d'être strict pour qui lit à voix basse, mot à mot, avec le lecteur, puisqu'il veille alors à écouter aussi chaque mot de sa bouche ; elle ajoute que le Maguen Avraham rapporte, au nom du Maté Moché, qu'il est bon d'agir ainsi a priori, et que plusieurs A'haronim l'ont écrit.",
            "The Shulchan Aruch allows reading Shnayim mikra during the public Torah reading. The Mishnah Berurah reports that the Magen Avraham cites the Shelah, who is strict: everyone must hear the reading from the reader’s mouth; and that this is the view of the Vilna Gaon (Maaseh Rav): one must hear every word while following in a Chumash, without reading along with the reader at all. The Mishnah Berurah holds, however, that there is no need to be strict about reading in a whisper, word for word, with the reader, since one then also takes care to hear every word from him; it adds that the Magen Avraham reports, in the name of the Mateh Moshe, that it is proper to do so in the first place, and that several Acharonim wrote likewise."),
        H("sefarade", [
            R("kh", 31, cite='ובקשל"ה דף פ"א ע"ב כתב דהעושים כן לא יפה עושין כי מן הראוי לשמוע מן הש"ץ והוא ישתוק'),
            R("kh", 31, cite='והכי נקטינן ודלא כמ"ש בב"י ובד"מ. יפ"ל או\' ז\''),
            R("kyy", 11, cite="אם השליח צבור מאריך בטעמים בקריאתו בתורה באופן שיכול היחיד להספיק לקרוא אז שנים מקרא ואחד תרגום, בעת קריאת התורה, רשאי לעשות כן, ויוצא ידי חובה"),
            R("kyy", 11, cite="ומכל מקום הנכון הוא שבכל הפרשיות ראוי למדקדק בדרכיו לכוין דעתו ולשמוע קריאת התורה מפי השליח צבור"),
        ],
            "Le Kaf ha'Haïm cite le Kitsour Chla : ceux qui lisent Chnayim mikra pendant la lecture publique n'agissent pas bien, car il convient d'écouter l'officiant et de se taire ; et il cite le Yafé laLev : « c'est ainsi que nous tenons », contre le Beit Yossef et le Darkhei Moché. Le Kitsour Yalkout Yossef permet, si l'officiant s'attarde sur les te'amim au point qu'on ait le temps de lire Chnayim mikra pendant la lecture, de le faire et d'être quitte – sauf pour Zakhor et Para, qu'il faut écouter –, à condition de lire à voix basse et que dix autres écoutent, ou de s'être tourné de côté et d'avoir commencé à lire avant le début de la lecture ; il conclut cependant que celui qui est scrupuleux écoute, dans toutes les parachiot, la lecture de l'officiant.",
            "The Kaf HaChaim cites the Kitzur Shelah: those who read Shnayim mikra during the public reading do not act well, since it is fitting to listen to the reader and be silent; and he cites the Yafeh LaLev: “this is how we hold”, against the Beit Yosef and the Darkei Moshe. The Kitzur Yalkut Yosef allows it, if the reader lingers over the te’amim so that one has time to read Shnayim mikra during the reading, and one fulfils the obligation – except for Zachor and Parah, which must be heard – provided one reads in a whisper and ten others are listening, or one turned aside and began reading before the reading began; he concludes, however, that a careful person listens to the reader in all the parashiyot."),
        H("tous", [
            R("kh", 8, cite='''אם שמע שמו"ת מאחר אפי' בלא אונס יצא ובלבד שיכוין לשמוע מלה במלה'''),
            R("kh", 8, cite='''אמנם כבר כתבנו במקום אחר דיותר טוב לאדם להוציא הוא עצמו ולא לסמוך לצאת ע"י אחרים'''),
            R("sht", 6, cite='''אם שמע שמו"ת מאחר אפילו בלי אונס יצא ובלבד שיכוין לשמוע מלה במלה'''),
            R("ahs", 3, cite='''וכן יש מי שאומר שאם שמע שנים מקרא ואחד תרגום – גם כן יצא, עם כיוון לשמוע (שערי תשובה בשם רדב"ז). ולעניות דעתי בעינן דווקא לימוד, ולא שמיעה'''),
        ],
            "Écouter la lecture d'un autre. Celui qui a entendu d'un autre Chnayim mikra véé'had targoum, même sans y être contraint, est quitte, pourvu qu'il se soit appliqué à écouter mot à mot : c'est l'avis du Radbaz, rapporté par le Ma'hazik Berakha, puis par les Cha'arei Techouva et le Kaf ha'Haïm. Le Kaf ha'Haïm ajoute qu'il vaut mieux s'acquitter soi-même que de compter sur d'autres. L'Aroukh haChoul'han rapporte cet avis et écrit qu'à son humble avis il faut précisément étudier, et non écouter.",
            "Hearing another person read. One who heard Shnayim mikra ve-echad targum from someone else, even when not forced to, has fulfilled the obligation, provided he took care to listen word by word: this is the view of the Radbaz, reported by the Machazik Berachah and then by the Sha'arei Teshuvah and the Kaf HaChaim. The Kaf HaChaim adds that it is better to fulfil it oneself than to rely on others. The Aruch HaShulchan reports this view and writes that in his humble opinion what is required is study specifically, not hearing."),
        H("ashkenaze", [
            R("sa", 6, cite='''מלמדי תינוקות אין צריכים לחזור ולקרות הפרשה בשבת'''),
            R("mb", 16, cite='''ודוקא בימיהם שהיו לומדים פירוש המקרא עם התינוקות ולכך יוצאין בזה גם ידי תרגום'''),
            R("mb", 16, cite='''אבל אם לומד פירוש המלות לחוד לא יצא ידי תרגום אלא השני פעמים מקרא דבודאי קרא עם התינוקות שני פעמים ולכן צריך לומר תרגום בעצמו'''),
            R("sahr", 7, cite='''לפיכך מלמדי תינוקות שגמרו הפרשה עם התינוקות פעם אחת אינם צריכין לחזור ולקרותה ב' פעמים אלא יקראו פעם אחת והתרגום'''),
            R("sahr", 7, cite='''אבל אם למדו פירוש המקרא יצאו ידי תרגום גם כן'''),
            R("ahs", 13, cite='''וכן כל מי שלמד הסדרה באמצע השבוע שני פעמים – אין צריך לחזור ולקרות הפרשה בשבת'''),
        ],
            "Les maîtres qui enseignent aux enfants n'ont pas à relire la paracha le Chabbat (Choul'han Aroukh). La Michna Beroura précise : cela valait de leur temps, où l'on étudiait avec les enfants l'explication du texte, ce qui acquittait aussi du targoum ; mais celui qui n'enseigne que le sens des mots n'est quitte que des deux lectures du texte – il a certainement lu deux fois avec les enfants – et doit dire lui-même le targoum. Le Choul'han Aroukh haRav : les maîtres qui ont achevé la paracha une fois avec les enfants n'ont pas à la relire deux fois, ils la lisent une fois, avec le targoum ; et s'ils ont étudié avec eux l'explication du texte, ils sont quittes aussi du targoum. L'Aroukh haChoul'han l'étend : quiconque a étudié la paracha deux fois dans la semaine n'a pas à la relire le Chabbat.",
            "Teachers of children need not read the parasha again on Shabbat (Shulchan Aruch). The Mishnah Berurah specifies: that applied in their days, when the explanation of the text was studied with the children, which also discharged the targum; but one who teaches only the meaning of the words has fulfilled only the two readings of the text – he certainly read it twice with the children – and must say the targum himself. The Shulchan Aruch HaRav: teachers who completed the parasha once with the children need not read it twice again; they read it once, with the targum; and if they studied the explanation of the text with them, they have fulfilled the targum as well. The Aruch HaShulchan extends this: anyone who studied the parasha twice during the week need not read it again on Shabbat."),
        H("sefarade", [
            R("kh", 32, cite='''מפני שהם חוזרים הרבה פעמים עם התינוקות מיהא תרגום צריכים לקרות'''),
            R("kh", 32, cite='''וע"כ יזהרו שלא להפסיק בעת קריאת הפרשה בשום שיחה ואפי' בד"ת'''),
            R("kh", 32, cite='''וא"כ לפ"ז גם מלמדי תינוקות אע"ג דלומדים כמה פעמים עם התינוקות צריך לקרות חוץ מזה שמו"ת כדי שיהיו תיכף בלתי הפסק בינתיים וגם כדי שילמדו כל פסוק ופסוק בפ"ע שמו"ת'''),
        ],
            "Le Kaf ha'Haïm explique que les maîtres d'enfants sont dispensés parce qu'ils répètent bien des fois la paracha avec les enfants, mais qu'ils doivent tout de même lire le targoum. Il rapporte ensuite du Maté Yehouda, au nom des kabbalistes, que la lecture de Chnayim mikra prépare à recevoir le supplément d'âme du Chabbat, et qu'on veille donc à ne pas l'interrompre par une conversation, pas même par des paroles de Torah ; il en conclut que, d'après cela, les maîtres d'enfants eux aussi doivent lire, en plus, Chnayim mikra véé'had targoum, d'une traite, sans interruption, chaque verset à part.",
            "The Kaf HaChaim explains that teachers of children are exempt because they review the parasha many times with the children, but that they must still read the targum. He then reports from the Mateh Yehudah, in the name of the kabbalists, that reading Shnayim mikra prepares one to receive the additional soul of Shabbat, and that one should therefore take care not to interrupt it with any conversation, not even words of Torah; he concludes that, accordingly, teachers of children too must read Shnayim mikra ve-echad targum in addition, at one stretch, without interruption, each verse by itself."),
        H("ashkenaze", [
            R("sa", (146, 2), cite='''ולקרות שנים מקרא ואחד תרגום בשעת קריאת התורה שרי'''),
            R("sa", (146, 2), cite='''והנכון שבכל הפרשיות ראוי למדקדק בדבריו לכוין דעתו ולשמעם מפי הקורא'''),
            R("mb", 15, cite='''דשם מסיק המחבר בס"ב דנכון להמדקדק בדבריו לכוין דעתו לשמעם מפי הקורא'''),
            R("bh", 5, cite='''עיין בא"ר שכתב דהוא מצוה מן המובחר ופלא הוא'''),
            R("bh", 5, cite='''אלא דיוכל לסמוך מי שרוצה להקל על המקילין ע"ש אבל חלילה דנימא דהוא מצוה מן המובחר'''),
            R("bh", 5, cite='''[אם לא דנימא דכונת הא"ר הוא בין גברא לגברא]'''),
            R("mb", 14, cite='''דרק בין גברא לגברא מותר'''),
        ],
            "Au siman 146, le Choul'han Aroukh, après avoir permis de lire Chnayim mikra pendant la lecture de la Torah, conclut que, dans toutes les parachiot, il convient à celui qui est scrupuleux d'appliquer son esprit à les écouter de la bouche du lecteur ; la Michna Beroura le rappelle ici. Le Béour Halakha s'étonne donc de l'Eliya Rabba, pour qui lire Chnayim mikra à ce moment serait la meilleure façon d'accomplir la mitsva : celui qui veut être indulgent peut s'appuyer sur ceux qui permettent, mais on ne saurait dire que c'est la meilleure façon – à moins que l'Eliya Rabba ne parle de l'intervalle entre deux appelés. La Michna Beroura rapporte en effet l'avis pour lequel ce n'est permis qu'entre deux appelés.",
            "In siman 146 the Shulchan Aruch, after permitting Shnayim mikra during the Torah reading, concludes that in all parashiot it is proper for one who is meticulous to direct his mind to hearing them from the reader; the Mishnah Berurah recalls this here. The Beur Halacha therefore wonders at the Eliyah Rabbah, for whom reading Shnayim mikra at that time would be the best way to perform the mitzvah: one who wishes to be lenient may rely on those who permit, but it cannot be said to be the best way – unless the Eliyah Rabbah means the interval between two aliyot. The Mishnah Berurah indeed reports the view that it is permitted only between two aliyot."),
        H("tous", [
            R("bht", (128, 46), cite='''נשאלתי אם מותר לקרות הפרשה שנים מקרא ואחד תרגום בשעה שהכהנים מברכים לעם והשבתי דאינו מותר אפי' למ"ד דמותר לקרות הפרשה שמו"ת בשעה שהש"ץ קורא הפרשה בס"ת אפ"ה אסור בברכת כהנים'''),
            R("kh", (128, 158), cite='''דאסור לקרות הפרשה שנים מקרא וא' תרגום בשעת ב"כ'''),
        ],
            "On ne lit pas Chnayim mikra pendant la bénédiction des Cohanim : même pour celui qui permet de la lire pendant que l'officiant lit la paracha dans le séfer Torah, c'est interdit à ce moment-là (Baèr Hétev, qui renvoie au Chiyouré Knesset haGuedola et au Pri 'Hadach ; Kaf ha'Haïm).",
            "Shnayim mikra is not read during the Priestly Blessing: even for one who permits reading it while the reader reads the parasha from the Torah scroll, it is forbidden at that time (Ba'er Hetev, referring to the Shiyurei Knesset HaGedolah and the Pri Chadash; Kaf HaChaim)."),
        H("ashkenaze", [
            R("sa", (139, 1), cite='''ובמקום שהחזן קורא הוא צריך לסדר תחלה'''),
            R("er", (139, 1), cite='''ועל כן ראוי שכל אחד יסדר אותה תחילה דשמא יקראו אותו לעלות למחר בשבת'''),
            R("er", (139, 1), cite='''דבקריאת הפרשה שנים מקרא ואחד תרגום יוצא ידי חובת הסידור'''),
            R("ahs", (139, 2), cite='''ועכשיו ששליח הציבור קורא – מחויב לחזור הפרשה שני פעמים מקודם, אפילו אם הוא בקי. וכשקרא בערב שבת שנים מקרא – יצא בזה'''),
        ],
            "Celui qui lit la Torah en public doit d'abord préparer sa lecture (Choul'han Aroukh, siman 139). L'Eliya Rabba rapporte du Ba'h qu'il convient que chacun la prépare aussi, car on pourrait l'appeler à monter le lendemain, Chabbat ; et il rapporte qu'en lisant la paracha Chnayim mikra véé'had targoum on s'acquitte de cette préparation. L'Aroukh haChoul'han : aujourd'hui que l'officiant lit, il doit revoir la paracha deux fois auparavant, même s'il la connaît ; et s'il a lu Chnayim mikra la veille de Chabbat, il est quitte par là.",
            "One who reads the Torah in public must first prepare his reading (Shulchan Aruch, siman 139). The Eliyah Rabbah reports from the Bach that it is fitting for everyone to prepare it too, since he might be called up the next day, Shabbat; and he reports that by reading the parasha Shnayim mikra ve-echad targum one fulfils this preparation. The Aruch HaShulchan: nowadays, when the reader reads, he must review the parasha twice beforehand, even if he knows it well; and if he read Shnayim mikra on Friday, he has thereby fulfilled this."),
    ]},
    {"titre": "הפטרה וימים טובים", "titre_fr": "Haftara et fêtes", "titre_en": "Haftarah and festivals", "halakhot": [
        H("tous", [
            R("rema", 7, cite="וכן אין צריך לקרות ההפטרות (מרדכי ה\"ק) ומכל מקום נהגו לקרות ההפטרה"),
            R("mb", 19, cite="טעם המנהג שמא יקראוהו למחר למפטיר ויהא בקי ורגיל בה"),
            R("ksa", 11, cite="וְנוֹהֲגִין לִקְרוֹת גַּם הַהַפְטָרָה"),
            R("kyy", 2, cite="הקורא את הפרשה שנים מקרא ואחד תרגום, מן הדין אין צריך לקרוא את ההפטרה. ומכל מקום נהגו לקרוא גם את ההפטרה [פעם אחת]"),
            R("kav", "yaron1", passage="הקורא את הפרשה שנים מקרא ואחד תרגום, מן הדין אינו צריך לקרוא את ההפטרה. ומכל מקום נהגו לקרוא גם את ההפטרה [פעם אחת]."),
        ],
            "Selon la loi, celui qui lit Chnayim mikra n'a pas à lire la haftara ; mais l'usage est de la lire (Rema ; Kitsour Choul'han Aroukh), une fois (Kitsour Yalkout Yossef ; Rav Yaron Achkenazi, Kav haHalakha haSefaradi). La Michna Beroura en donne la raison, d'après le Maguen Avraham : on pourrait être appelé le lendemain pour la lire comme maftir, et il faut la connaître.",
            "By law, one who reads Shnayim mikra need not read the haftarah; but the custom is to read it (Rema; Kitzur Shulchan Aruch), once (Kitzur Yalkut Yosef; Rav Yaron Ashkenazi, Kav HaHalacha HaSefaradi). The Mishnah Berurah gives the reason, after the Magen Avraham: one might be called up the next day to read it as maftir, and should know it."),
        H("sefarade", [
            R("bih", (2, "Lech Lecha", "Lekh Lekha", "Lech Lecha", "לך לך", 11), cite='ואם חל שבת בראש חודש, או "שקלים" ו"זכור" ו"פרה" ו"החודש", צריך לומר ההפטרה של שנים מקרא ואחד תרגום, הפטרת השבוע הן אם קורא השנים מקרא ואחד תרגום ביום ששי, הן אם קוראה ביום שבת עצמו'),
            R("kh", 36, cite='ואני נוהג בשבת שיש הפטרה מחודשת כגון הפטרת שבת של ר"ח או שבת שלפני ר"ח או של חנוכה ושל ד\' פרשיות לחזור עם הפרשה הפטרת השבוע וביום שבת לקרוא המחודשת עם המפטיר'),
            R("kh", 36, cite="וכן עמא דבר"),
        ],
            "Quand le Chabbat tombe à Roch 'Hodech, ou que c'est Chabbat Chekalim, Zakhor, Para ou Ha'Hodech, la haftara que l'on lit avec Chnayim mikra est celle de la paracha de la semaine, qu'on lise le vendredi ou le Chabbat même (Ben Ich 'Haï). Le Kaf ha'Haïm, citant la Knesset haGuedola, l'étend au Chabbat qui précède Roch 'Hodech et à celui de 'Hanouka – la haftara propre au jour, on la lit le Chabbat avec le maftir – et conclut : « et tel est l'usage ».",
            "When Shabbat falls on Rosh Chodesh, or it is Shabbat Shekalim, Zachor, Parah or HaChodesh, the haftarah read with Shnayim mikra is that of the weekly parasha, whether one reads on Friday or on Shabbat itself (Ben Ish Chai). The Kaf HaChaim, citing the Knesset HaGedolah, extends this to the Shabbat before Rosh Chodesh and to Shabbat Chanukah – the special haftarah is read on Shabbat along with the maftir – and concludes: “and this is the custom”."),
        H("ashkenaze", [
            R("mb", 20, cite="ובד' פרשיות יקרא הפטרה דד' פרשיות"),
            R("sahr", 10, cite="ובד' פרשיות יש לו לקרות הפטרה של ד' פרשיות שמפטירין אותה בבית הכנסת ולא הפטרה של פרשת השבוע וכן בשבת ראש חודש ומחר חדש ושבת חנוכה"),
        ],
            "Pour les quatre parachiot (Chekalim, Zakhor, Para, Ha'Hodech), on lit la haftara des quatre parachiot (Michna Beroura). Le Choul'han Aroukh haRav précise : celle qu'on lira à la synagogue, et non celle de la paracha de la semaine ; de même pour Chabbat Roch 'Hodech, le Chabbat veille de Roch 'Hodech (Ma'har 'Hodech) et Chabbat 'Hanouka.",
            "For the four parashiyot (Shekalim, Zachor, Parah, HaChodesh), one reads the haftarah of the four parashiyot (Mishnah Berurah). The Shulchan Aruch HaRav specifies: the one that will be read in the synagogue, and not that of the weekly parasha; likewise on Shabbat Rosh Chodesh, the Shabbat on the eve of Rosh Chodesh (Machar Chodesh) and Shabbat Chanukah."),
        H("tous", [
            R("sa", 7, cite='אין צריך לקרות פרשת יו"ט'),
            R("mb", 18, cite="ר\"ל שאין צריך לקרות לעצמו שמו\"ת דהא כבר קרא כל התורה מדי שבת בשבתו"),
            R("kyy", 13, cite="אין צריך לקרוא את הפרשה שנים מקרא ואחד תרגום בימים טובים"),
            R("sahr", 9, cite="אין צריך לקרות פרשת יו\"ט לעצמו בערב יו\"ט שהרי כבר קרא או יקרא פרשה זו בשבתה"),
            R("kh", 35, cite='וה"ה פרשת של חו"ה א"צ להשלים. כנה"ג בהגב"י. וכללא נקטינן בכל מקום שקוראין מה שכבר קראו בסדר הפרשיות א"צ לחזור ולקרות'),
        ],
            "On n'a pas à lire Chnayim mikra pour la lecture de Yom Tov (Choul'han Aroukh ; Kitsour Yalkout Yossef) : on a déjà lu toute la Torah, Chabbat après Chabbat (Michna Beroura) ; on a déjà lu, ou on lira, cette paracha à son Chabbat (Choul'han Aroukh haRav). Le Kaf ha'Haïm rapporte, au nom de la Knesset haGuedola, qu'il en va de même pour la lecture de 'Hol haMoed, et énonce la règle : partout où l'on lit ce qui a déjà été lu dans l'ordre des parachiot, on n'a pas à le relire.",
            "One need not read Shnayim mikra for the Yom Tov reading (Shulchan Aruch; Kitzur Yalkut Yosef): one has already read the whole Torah, Shabbat after Shabbat (Mishnah Berurah); one has already read, or will read, that parasha on its Shabbat (Shulchan Aruch HaRav). The Kaf HaChaim reports, in the name of the Knesset HaGedolah, that the same holds for the Chol HaMoed reading, and states the rule: wherever what is read was already read in the order of the parashiyot, one need not read it again."),
        H("tous", [
            R("mb", 18, cite='וביום הו"ר יקרא שמו"ת פרשת וזאת הברכה ואם קרא ביום שמ"ע לא הפסיד'),
            R("kh", 29, cite='ביום הו"ר יקרא פ\' וזאת הברכה שמו"ת'),
            R("kh", 29, cite='ומ"מ אם קראה ביום ש"ע לא הפסיד'),
            R("sahr", 9, cite="ומכל מקום בערב שמחת תורה יקרא פרשת וזאת הברכה שנים מקרא ואחד תרגום שעכשיו הוא זמנה"),
            R("bih", (1, "V'Zot HaBerachah", "Vezot haBerakha", "VeZot HaBerachah", "וזאת הברכה", 15), cite='שנים מקרא ואחד תרגום של פרשת וזאת הברכה יקראנה ביום הו"ר ולא ביום ש"ע מפני התרגום, ואם שכח ולא קראה ביום הו"ר יקראנה ביום ש"ע אחר מנחה'),
            R("kyy", 19, cite="פרשת ״וזאת הברכה״ יש לקרוא שנים מקרא ואחד תרגום ביום הושענא רבה, ואם שכח לקרוא בהושענא רבה, יקרא בשמיני עצרת קודם שחרית, או יחד עם השליח צבור"),
            R("kyy", 9, cite="מי שזמנו דחוק, מותר לו לקרוא שנים מקרא ואחד תרגום בליל שבת, וכן מותר לקרוא פרשת וזאת הברכה בליל שמחת תורה"),
            R("malka", "142", cite='אפשר, אך יותר טוב לקרא כל פסוק שמו"ת',
              passage='האם אפשר לכתחילה להחשיב פרשת וזאת הברכה שקורים בתוך התיקון לאחד מקרא ? [...] אפשר, אך יותר טוב לקרא כל פסוק שמו"ת כמש"כ כה"ח בסימן רפה\' ע"פ האר"י, וכ"ה בברכ"י. ותו דיותר נכון לקרא שמו"ת ביום ולא בלילה, כמש"כ מחב"ר וכה"ח הנ"ל.'),
        ],
            "La paracha Vezot haBerakha se lit en Chnayim mikra le jour de Hochaana Rabba (Michna Beroura ; Kaf ha'Haïm ; Ben Ich 'Haï ; Kitsour Yalkout Yossef) ; le Choul'han Aroukh haRav dit : la veille de Sim'hat Torah, qui est son moment. Celui qui l'a lue le jour de Chemini Atseret n'a rien perdu (Michna Beroura ; Kaf ha'Haïm). Le Ben Ich 'Haï veut qu'on ne la lise pas le jour de Chemini Atseret, à cause du targoum, et, si l'on a oublié, qu'on la lise ce jour-là après Min'ha ; le Kitsour Yalkout Yossef dit de la lire alors à Chemini Atseret avant Cha'harit, ou avec l'officiant, et permet à qui manque de temps de la lire la nuit de Sim'hat Torah. Le Rav Menaché Moreno (beit hora'a « Halakha lema'assé » du Rav Ofir Malka) répond que la lecture de Vezot haBerakha faite dans le Tikoun peut compter pour l'une des deux lectures du texte, mais qu'il vaut mieux lire chaque verset en Chnayim mikra, et de jour plutôt que de nuit.",
            "The parasha Vezot HaBerachah is read as Shnayim mikra on the day of Hoshana Rabbah (Mishnah Berurah; Kaf HaChaim; Ben Ish Chai; Kitzur Yalkut Yosef); the Shulchan Aruch HaRav says: on the eve of Simchat Torah, which is its time. One who read it on the day of Shemini Atzeret has lost nothing (Mishnah Berurah; Kaf HaChaim). The Ben Ish Chai wants it not read on the day of Shemini Atzeret, because of the targum, and, if one forgot, read that day after Minchah; the Kitzur Yalkut Yosef says to read it then on Shemini Atzeret before Shacharit, or with the reader, and allows one who is short of time to read it on the night of Simchat Torah. Rav Menashe Moreno (the “Halacha LeMaaseh” beit hora’ah of Rav Ofir Malka) answers that reading Vezot HaBerachah in the Tikkun may count as one of the two readings of the text, but that it is better to read each verse as Shnayim mikra, and by day rather than by night."),
        H("ashkenaze", [
            R("ma", 11, cite='''פעם א' מקרא וא' תרגום ואח"כ מזמור מכתובים משיר של יום א' מקרא וא' תרגום או לעז אחר ואח"כ משנה א' [של"ה בשם מהרמ"ק]'''),
            R("bht", 9, cite='''פעם א' מקרא וא' תרגום ועיין של"ה'''),
            R("ksa", 11, cite='''וְיֵשׁ נוֹהֲגִין עוֹד לוֹמַר אַחַר כָּךְ שִׁיר הַשִּׁירִים'''),
            R("ahs", 13, cite='''וכל מה שכתב המגן אברהם בסעיף י"א וי"ב – לא ידענו ממנהגים כאלו'''),
        ],
            "La haftara, et ce qu'on lit ensuite. Le Maguen Avraham rapporte, du Chla au nom de Rabbi Moché Cordovero : la haftara une fois dans le texte et une fois dans le targoum ; puis un psaume, celui du cantique du jour, une fois dans le texte et une fois dans le targoum ou une autre langue ; puis une michna. Le Baèr Hétev rapporte de même : une fois le texte et une fois le targoum. Le Kitsour Choul'han Aroukh note que certains ont encore l'usage de dire ensuite le Cantique des cantiques. L'Aroukh haChoul'han écrit de ce que rapporte là le Maguen Avraham : « nous ne connaissons pas de tels usages ».",
            "The haftarah, and what is read after it. The Magen Avraham reports, from the Shelah in the name of Rabbi Moshe Cordovero: the haftarah once in the text and once in the targum; then a psalm, that of the song of the day, once in the text and once in the targum or another language; then a mishnah. The Ba'er Hetev likewise reports: once the text and once the targum. The Kitzur Shulchan Aruch notes that some also have the custom of saying the Song of Songs afterwards. The Aruch HaShulchan writes of what the Magen Avraham reports there: “we do not know of such customs”."),
        H("sefarade", [
            R("kh", 38, cite='''אמנם המט"י או' ח' כתב דנהגו לקרות הפטרה של כל שבוע פ"א מקרא לבד ודלא כמ"ש המ"א פ"א וא' תרגום דלא נהגו בתרגום ולכך נדפסו ההפטרות בחומשין מקרא לבד'''),
            R("kh", 38, cite='''וע"כ אחר קריאת שמו"ת יאמר הפטרה של השבוע ואח"כ מזמור שיר ליום השבת וה' מלך גאות לבש וסדר חק לישראל המסודר ליום ו' משנה גמ' זוהר הלכות ואח"כ א"ר הונא בריה דרב יהודה א"ר אמי לעולם ישלים אדם פרשיותיו וכו\''''),
            R("mbe", 131, cite='''פסוק אחרון מהפרשה אחר שקראו שמו״ת יחזור לקרותו'''),
            R("mbe", 133, cite='''וילמוד מאמר קטן מזהר ונמצא שקרא מקרא תנ״ך משנה גמרא זהר'''),
        ],
            "Après la lecture. Le Kaf ha'Haïm rapporte du Maté Yehouda que l'usage est de lire la haftara de chaque semaine une seule fois, dans le texte seul, et non avec le targoum comme l'écrit le Maguen Avraham : on n'a pas pris l'usage du targoum, et c'est pourquoi les haftarot sont imprimées dans les 'Houmachim sans targoum. Il donne l'ordre à suivre : après Chnayim mikra, la haftara de la semaine, puis « Mizmor chir léyom haChabbat » et « Hachem malakh guéout lavech », l'étude du 'Hok leIsraël du vendredi (michna, guemara, Zohar, halakhot), puis l'enseignement de Rav Houna au nom de Rabbi Ami (« Qu'on achève toujours ses parachiot avec la communauté… ») et « Rabbi 'Hanania ben Akachia dit… ». Le 'Hida (Moré beEtsba) demande de relire le dernier verset après Chnayim mikra, de lire la haftara, puis « Hachem malakh », la michna « Bamé madlikin », l'enseignement de Rav Houna et un court passage du Zohar : on a ainsi lu Torah, Prophètes et Écrits, michna, guemara et Zohar.",
            "After the reading. The Kaf HaChaim reports from the Mateh Yehudah that the custom is to read each week's haftarah once only, in the text alone, and not with the targum as the Magen Avraham writes: the targum did not become customary, which is why the haftarot are printed in the Chumashim without targum. He gives the order to follow: after Shnayim mikra, the haftarah of the week, then “Mizmor shir leyom haShabbat” and “Hashem malach ge'ut lavesh”, the Friday portion of Chok LeYisrael (mishnah, gemara, Zohar, halachot), then the teaching of Rav Huna in the name of Rabbi Ami (“One should always complete his portions with the congregation…”) and “Rabbi Chananya ben Akashya says…”. The Chida (Moreh BeEtzba) asks one to reread the last verse after Shnayim mikra, to read the haftarah, then “Hashem malach”, the mishnah “Bameh madlikin”, Rav Huna's teaching and a short passage of the Zohar: one has thus read Torah, Prophets and Writings, mishnah, gemara and Zohar."),
        H("sefarade", [
            R("kh", 37, cite='''כתב שם היפ"ל דיקרא ביום ו' אחר שמו"ת הפטרת השבוע חוץ מפ' אלא הדברים דיקרא הפטרת חזון'''),
            R("kh", 37, cite='''אלא ההפטרה שקורא המפטיר למחר בס"ת וכתב שכן המנהג פשוט'''),
        ],
            "Pendant les trois Chabbatot « de malheur », les sept « de consolation » et les deux « de repentir » : le Kaf ha'Haïm rapporte que, pour le Yafé laLev, on lit le vendredi, après Chnayim mikra, la haftara de la paracha, sauf à la paracha Devarim, où l'on lit « 'Hazon » ; mais que le Péta'h haDevir établit que le particulier qui lit Chnayim mikra la veille de ces Chabbatot lit la haftara que le maftir lira le lendemain, et écrit que tel est l'usage répandu ; le Lev 'Haïm s'y accorde, au nom de plusieurs décisionnaires.",
            "During the three Shabbatot “of calamity”, the seven “of consolation” and the two “of repentance”: the Kaf HaChaim reports that, according to the Yafeh LaLev, on Friday after Shnayim mikra one reads the haftarah of the parasha, except at parashat Devarim, when one reads “Chazon”; but that the Petach HaDevir establishes that an individual reading Shnayim mikra on the eve of those Shabbatot reads the haftarah which the maftir will read the next day, and writes that such is the widespread custom; the Lev Chaim concurs, in the name of several authorities."),
        H("tous", [
            R("rema", 7, cite='''ובשבת של חתונה יקרא ההפטר' של שבת ולא שוש אשיש'''),
            R("mb", 20, cite='''וקמ"ל דבשעה שקורא לעצמו ההפטרה אין צריך לקרות אלו הפסוקים משום דהוא מצוי ושגור בפי הכל ובקי בהן בלא זו הקריאה'''),
            R("ma", 12, cite='''לכן נראה לי דיחזור אותה אך אם יש הרבה חתנות זו אחר זו שוב א"צ'''),
            R("sahr", 10, cite='''ואם אירע חתונה בשבת במקומות שנוהגים אז להפטיר בבית הכנסת שוש אשיש יש לו ג"כ לקרותה לעצמו ולא הפטרת השבוע כי שמא יקראוהו למחר'''),
            R("ahs", 13, cite='''דבימיו היה המנהג לקרא לחתן "שוש אשיש", ובימינו לא ידענו ממנהג זה'''),
            R("kh", 39, cite='''גם בשבת חתונה אין לקרות ביום ו' אחר השמו"ת רק הפטרת השבוע'''),
        ],
            "Le Chabbat d'un mariage. Le Rema : on lit pour soi la haftara du Chabbat, et non « Sos assis ». La Michna Beroura explique : là où l'on ajoute en public, à la haftara de la paracha, quelques versets de « Sos assis », celui qui lit la haftara pour lui-même n'a pas à les lire, car ils sont courants, familiers à tous, et on les connaît sans cette lecture. Le Maguen Avraham pense au contraire qu'on la relit, sauf si plusieurs mariages se suivent ; le Choul'han Aroukh haRav de même : là où l'on a l'usage de lire alors à la synagogue « Sos assis », on la lit aussi pour soi, et non la haftara de la semaine, car on pourrait être appelé le lendemain. L'Aroukh haChoul'han note que cet usage existait du temps du Rema et qu'on ne le connaît plus de son temps. Le Kaf ha'Haïm conclut, d'après la raison donnée par la Knesset haGuedola, que même le Chabbat d'un mariage on ne lit le vendredi, après Chnayim mikra, que la haftara de la semaine.",
            "The Shabbat of a wedding. The Rema: one reads for oneself the haftarah of the Shabbat, not “Sos asis”. The Mishnah Berurah explains: where a few verses of “Sos asis” are added in public to the haftarah of the parasha, one who reads the haftarah for himself need not read them, since they are common, familiar to all, and known without this reading. The Magen Avraham holds on the contrary that one does review it, unless several weddings follow one another; the Shulchan Aruch HaRav likewise: where the custom is to read “Sos asis” in the synagogue then, one also reads it for oneself, not the haftarah of the week, since one might be called up the next day. The Aruch HaShulchan notes that this custom existed in the Rema's time and is no longer known in his. The Kaf HaChaim concludes, following the reason given by the Knesset HaGedolah, that even on the Shabbat of a wedding one reads on Friday, after Shnayim mikra, only the haftarah of the week."),
        H("ashkenaze", [
            R("ahs", 13, cite='''וכן מה שקורין בראש חודש, ורגלים, וימים נוראים – אין צריך היחיד לקרותם, שכבר קראו כל אחד בשבתו'''),
            R("mb", 19, cite='''משא"כ בפרשיות של יו"ט ששם החזן הוא הקורא'''),
        ],
            "L'Aroukh haChoul'han : ce qu'on lit à Roch 'Hodech, aux fêtes de pèlerinage et aux jours redoutables, le particulier n'a pas à le lire, puisque chacun de ces passages a déjà été lu à son Chabbat. La Michna Beroura explique pourquoi on lit pourtant la haftara et non la lecture de Yom Tov : on peut être appelé à lire la haftara, alors que les lectures de Yom Tov, c'est l'officiant qui les lit.",
            "The Aruch HaShulchan: what is read on Rosh Chodesh, the pilgrimage festivals and the Days of Awe need not be read by the individual, since each of these passages has already been read on its Shabbat. The Mishnah Berurah explains why the haftarah is nevertheless read but not the Yom Tov reading: one may be called up to read the haftarah, whereas the Yom Tov readings are read by the reader."),
        H("ashkenaze", [
            R("mb", (669, 4), cite='''כתבו הפוסקים שבליל שמחת תורה יקרא הפרשה שנים מקרא ואחד תרגום שעתה הוא זמנה'''),
            R("ma", 10, cite='''וערב ש"ת יקרא וזאת הברכה [כונות]'''),
            R("bht", 8, cite='''ובערב ש"ת יקרא וזאת הברכה'''),
        ],
            "Vezot haBerakha. La Michna Beroura écrit aussi, dans les lois de Sim'hat Torah, que selon les décisionnaires on lit la paracha deux fois dans le texte et une fois dans le targoum la nuit de Sim'hat Torah, « car c'est maintenant son moment » ; le Maguen Avraham et le Baèr Hétev disent, d'après le Séfer haKavanot : la veille de Sim'hat Torah.",
            "Vezot HaBerachah. The Mishnah Berurah also writes, in the laws of Simchat Torah, that according to the authorities one reads the parasha twice in the text and once in the targum on the night of Simchat Torah, “for now is its time”; the Magen Avraham and the Ba'er Hetev say, following Sefer HaKavanot: on the eve of Simchat Torah."),
    ]},
    {"titre": "מקרים מיוחדים", "titre_fr": "Cas particuliers", "titre_en": "Special cases", "halakhot": [
        H("tous", [
            R("sayd", 1, cite='''ות"ת הוי דבר שבצינעא אבל לחזור הפרשה כיון שחייב אדם להשלים פרשיותיו עם הצבור הוי כקורא את שמע ומותר'''),
            R("shakh", 4, cite='''כתוב בדרישה בשם מהרש"ל דה"ה לחזור שנים מקרא ואחד תרגום מותר'''),
            R("ksa", (219, 1), cite='''אֲבָל לַחֲזוֹר אֶת הַפָּרָשָׁה שְׁנַיִם מִקְרָא וְאֶחָד תַּרְגוּם, מֻתָּר'''),
            R("kyy", 18, cite='''אבל בתוך שבעה ימי האבלות, חייב לקרוא שנים מקרא ואחד תרגום'''),
            R("kh", 27, cite='''דאבל יכול לחזור הפרשה בשבת שתוך ז' וכתב שם דהיינו דוקא כשלא יכלו ז' ימים קודם יום ג' אבל אם יכלו קודם יום ג' אז לדעת י"א קמא צריך להמתין עד יום ג\''''),
            R("kh", 27, cite='''מיהו אין דבריו מוכרחים דכיון דעיקר המצוה לקרות בשבת אלא דבדיעבד יכול לקרות עד יום ג' שפ"ר מקרי חובת היום'''),
            R("rae", 1, cite='''דאפשר אם חל יום ז' בשבת צריך להמתין עד אחר יציאה מבהכ"נ וישלים קודם אכילה'''),
        ],
            "L'endeuillé. Le Chabbat des sept jours de deuil, l'étude de la Torah compte parmi les choses privées (où le deuil s'applique) ; mais relire la paracha est permis : puisqu'on est tenu d'achever ses parachiot avec la communauté, c'est comme lire le Chema (Choul'han Aroukh, Yoré Déa). Le Chakh rapporte, de la Dericha au nom du Maharchal, qu'il en va de même pour Chnayim mikra véé'had targoum ; le Kitsour Choul'han Aroukh le dit expressément, et le Kitsour Yalkout Yossef écrit que l'endeuillé, pendant les sept jours, est tenu de lire Chnayim mikra. Le Kaf ha'Haïm rapporte un avis qui limite cette permission au cas où les sept jours ne s'achèvent pas avant le mardi – sinon, selon le premier « certains disent », il attendrait jusque-là –, puis le Tossefet Chabbat, pour qui cela ne s'impose pas : l'essentiel de la mitsva est de lire le Chabbat, c'est donc bien l'obligation du jour. Si le septième jour tombe un Chabbat, peut-être attend-il la sortie de la synagogue pour achever avant le repas (Échel Avraham, rapporté par Rabbi Akiva Eiger et par le Kaf ha'Haïm).",
            "The mourner. On the Shabbat within the seven days of mourning, Torah study counts among the private matters (in which mourning applies); but reviewing the parasha is permitted: since one is obliged to complete one's portions with the congregation, it is like reading the Shema (Shulchan Aruch, Yoreh De'ah). The Shach reports, from the Derishah in the name of the Maharshal, that the same holds for Shnayim mikra ve-echad targum; the Kitzur Shulchan Aruch says so explicitly, and the Kitzur Yalkut Yosef writes that a mourner, during the seven days, is obliged to read Shnayim mikra. The Kaf HaChaim reports a view limiting this permission to the case where the seven days do not end before Tuesday – otherwise, according to the first “some say”, he would wait until then –, and then the Tosefet Shabbat, for whom this is not compelling: the main mitzvah is to read on Shabbat, so it is indeed the obligation of the day. If the seventh day falls on Shabbat, perhaps he waits until leaving the synagogue and completes it before the meal (Eshel Avraham, reported by Rabbi Akiva Eiger and by the Kaf HaChaim)."),
        H("tous", [
            R("rema", (553, 2), cite='''ונהגו שלא ללמוד בערב תשעה באב מחצות ואילך כי אם בדברים המותרים בתשעה באב ולכן אם חל בשבת אין אומרים פרקי אבות'''),
            R("ksa", (125, 4), cite='''אֲבָל לִקְרוֹת הַסִּדְרָה שְׁנַיִם מִקְרָא וְאֶחָד תַּרְגּוּם, מֻתָּר וּמִכָּל שֶׁכֵּן קֹדֶם חֲצוֹת הַיּוֹם'''),
            R("kh", (553, 19), cite='''אבל מותר לחזור שמו"ת ומכ"ש קודם חצות'''),
            R("kh", (553, 19), cite='''דאם עבר ולא קראה עד אחר חצות נראה פשוט דיכול לקרותה אח"כ אפי' אם ט"ב בשבת עצמו'''),
        ],
            "Le 9 Av ou sa veille, un Chabbat. L'usage rapporté par le Rema est de n'étudier, la veille du 9 Av à partir de midi, que ce qui est permis le 9 Av ; c'est pourquoi, un Chabbat, on ne dit pas alors les Pirké Avot. Mais lire la paracha deux fois dans le texte et une fois dans le targoum est permis, à plus forte raison avant midi (Kitsour Choul'han Aroukh, pour le 9 Av qui tombe un Chabbat ; Kaf ha'Haïm, au nom du 'Hayé Adam). Le Kaf ha'Haïm ajoute, au nom du Zekhor leAvraham : celui qui ne l'a pas lue avant midi peut à l'évidence la lire ensuite, même si le 9 Av tombe le Chabbat même.",
            "The 9th of Av or its eve, on a Shabbat. The custom reported by the Rema is to study, on the eve of the 9th of Av from midday on, only what is permitted on the 9th of Av; hence on a Shabbat Pirkei Avot is not said then. But reading the parasha twice in the text and once in the targum is permitted, all the more so before midday (Kitzur Shulchan Aruch, for a 9th of Av that falls on Shabbat; Kaf HaChaim, in the name of the Chayei Adam). The Kaf HaChaim adds, in the name of the Zechor LeAvraham: one who did not read it before midday may obviously read it afterwards, even if the 9th of Av falls on that very Shabbat."),
        H("sefarade", [
            R("kh", (496, 62), cite='''ויום ח' של פסח חל בשבת ובא"י קורין פ' אחרי אם יקרא פ' אחרי שמו"ת כבני א"י או יתנהג בקריאת הפ' כבני חו"ל'''),
            R("kh", (496, 62), cite='''דטפי עדיף להשלים פרשיותיו עם הצבור שהוא עמהם ולענין זה לא יעשה כא"י'''),
        ],
            "Un habitant de la terre d'Israël de passage à l'étranger, quand le huitième jour de Pessa'h tombe un Chabbat : en terre d'Israël on lit ce jour-là la paracha de la semaine (dans le cas posé, A'haré Mot), à l'étranger la lecture de la fête. Lit-il cette paracha en Chnayim mikra comme les habitants d'Israël, ou suit-il les parachiot du lieu ? Le Kaf ha'Haïm rapporte la réponse du 'Hida (Mar'it ha'Ayin) : il vaut mieux achever ses parachiot avec la communauté où il se trouve ; sur ce point, il ne fait pas comme en terre d'Israël.",
            "A resident of the Land of Israel staying abroad, when the eighth day of Pesach falls on a Shabbat: in the Land of Israel the weekly parasha is read that day (in the case posed, Acharei Mot), abroad the festival reading. Does he read that parasha as Shnayim mikra like the residents of Israel, or follow the parashiot of the place? The Kaf HaChaim reports the answer of the Chida (Mar'it HaAyin): it is better to complete one's portions with the congregation one is with; on this point he does not act as in the Land of Israel."),
        H("sefarade", [
            R("kh", (25, 27), cite='''בשעת קריאת שנים מקרא ואחד תרגום בפ' קדש והיה כי יביאך א"צ להיות עליו ולא הוי כעדות שקר כיון שאומר רק דרך קריאה'''),
        ],
            "Lire en Chnayim mikra les passages « Kadech » et « Vehaya ki yeviakha », qui parlent des tefilines, ne demande pas de les porter : ce n'est pas « un faux témoignage », puisqu'on ne les dit qu'en manière de lecture (Kaf ha'Haïm, au nom du Binyan Olam).",
            "Reading as Shnayim mikra the passages “Kadesh” and “Vehayah ki yevi'acha”, which speak of tefillin, does not require wearing them: it is not “false testimony”, since one says them only by way of reading (Kaf HaChaim, in the name of the Binyan Olam)."),
    ]},
]

INTRO = {
    "t": ("<b>מבוא</b> הלכות שנים מקרא ואחד תרגום, מלוקטות מן הפוסקים: כל הלכה עם מקורה ובלשונו. "
          "<small>[ספרדים – עדות המזרח]</small> – לבני עדות המזרח; <small>[אשכנזים – נוסח אשכנז ונוסח ספרד]</small> – לנוסח אשכנז ולנוסח ספרד; "
          "הלכה בלי ציון – לכל העדות. אין כאן הכרעה: כל שאלה למעשה תישאל לרב."
          "<br><small>מקורות: שולחן ערוך עם הגהות הרמ״א, ט״ז ושערי תשובה (מגיני ארץ, למברג תרנ״ג), מגן אברהם, משנה ברורה וביאור הלכה, "
          "באר היטב וקיצור שולחן ערוך (תורת אמת), חיי אדם, אליה רבה, ספר חסידים, מורה באצבע וצפורן שמיר לחיד״א, ש״ך ורבי עקיבא איגר ליורה דעה, "
          "כף החיים (ירושלים תר״ע–תרצ״ג), בן איש חי (ויקיטקסט), רמב״ם (תורת אמת) – נחלת הכלל, דרך ספריא; "
          "ערוך השולחן – ויקיטקסט, CC BY-SA, דרך ספריא; "
          "שולחן ערוך הרב – הוצאת קה״ת (Kehot Publication Society), CC BY-NC, דרך ספריא; "
          # La mention que demande Torat Emet pour ses livres sous CC BY-NC-SA 2.5 (toratemetfreeware.com/contents/copyrights2.html).
          "ילקוט יוסף – קיצור שולחן ערוך, מהדורת התשס״ז, מתוך מאגר תורת אמת: כל הזכויות שמורות לרב יצחק יוסף שליט״א, בכפוף לתנאי רשיון CC BY-NC-SA 2.5 – אסור בשימוש מסחרי (creativecommons.org/licenses/by-nc-sa/2.5/deed.he); "
          "תשובות הידברות, קו ההלכה הספרדי, בית ההוראה ״הלכה למעשה״ של הרב אופיר מלכא והרב בנימין חותה (כיכר השבת) – בתמצית ובציון מקומן, לא בהעתקה.</small>"),
    "fr": ("<b>Introduction</b> Les lois de Chnayim mikra véé'had targoum – lire chaque semaine la paracha deux fois dans le texte hébreu et une fois dans la traduction araméenne d'Onkelos –, réunies d'après les décisionnaires : chaque halakha cite sa source en hébreu. "
           "<small>[Séfarades – rite Edot hamizra'h]</small> : pour qui suit les décisionnaires séfarades ; <small>[Ashkénazes – rites Ashkenaz et Sfard]</small> : pour les rites Ashkenaz et Sfard ; sans indication : pour tous. "
           "Ce recueil ne tranche rien : pour une question pratique, on interroge un rav."
           "<br><small>Sources : Choul'han Aroukh avec les gloses du Rema, Taz et Cha'arei Techouva (Maginei Eretz, Lemberg 1893), Maguen Avraham, Michna Beroura et Béour Halakha, Baèr Hétev et Kitsour Choul'han Aroukh (Torat Emet), 'Hayé Adam, Eliya Rabba, Séfer 'Hassidim, Moré beEtsba et Tsiporen Chamir du 'Hida, Chakh et Rabbi Akiva Eiger sur Yoré Déa, Kaf ha'Haïm (Jérusalem 1910-1933), Ben Ich 'Haï (Wikisource), Rambam (Torat Emet) : domaine public, via Sefaria. "
           "Aroukh haChoul'han : Wikisource, CC BY-SA, via Sefaria. "
           "Choul'han Aroukh haRav : Kehot Publication Society, CC BY-NC, via Sefaria. "
           "Kitsour Choul'han Aroukh Yalkout Yossef, édition 5767, base Torat Emet : tous droits réservés au Rav Yitzhak Yosef, sous la licence CC BY-NC-SA 2.5, usage commercial interdit (creativecommons.org/licenses/by-nc-sa/2.5/deed.fr). "
           "Réponses de Hidabroot, de Kav haHalakha haSefaradi, du beit hora'a « Halakha lema'assé » du Rav Ofir Malka et du Rav Binyamin 'Hota (Kikar haChabbat) : résumées et référencées, non reproduites. "
           "Français et anglais rédigés par ordinateur d'après les sources ; chaque citation hébraïque a été relue à sa source. Une seconde relecture automatique du français et de l'anglais contre les sources est faite pour les 31 premières halakhot et en cours pour celles ajoutées le 26/11/2026. Non relus par un rav : l'hébreu fait foi.</small>"),
    "en": ("<b>Introduction</b> The laws of Shnayim mikra ve-echad targum – reading the weekly parasha twice in the Hebrew text and once in Onkelos’ Aramaic translation –, gathered from the halachic authorities: each law quotes its source in Hebrew. "
           "<small>[Sephardim – Edot HaMizrach rite]</small>: for those who follow the Sephardi authorities; <small>[Ashkenazim – Ashkenaz and Sfard rites]</small>: for the Ashkenaz and Sfard rites; unmarked: for everyone. "
           "This collection decides nothing: for a practical question, ask a rabbi."
           "<br><small>Sources: Shulchan Aruch with the Rema’s glosses, Taz and Sha’arei Teshuvah (Maginei Eretz, Lemberg 1893), Magen Avraham, Mishnah Berurah and Beur Halacha, Ba’er Hetev and Kitzur Shulchan Aruch (Torat Emet), Chayei Adam, Eliyah Rabbah, Sefer Chasidim, the Chida’s Moreh BeEtzba and Tziporen Shamir, Shach and Rabbi Akiva Eiger on Yoreh De’ah, Kaf HaChaim (Jerusalem 1910-1933), Ben Ish Chai (Wikisource), Rambam (Torat Emet): public domain, via Sefaria. "
           "Aruch HaShulchan: Wikisource, CC BY-SA, via Sefaria. "
           "Shulchan Aruch HaRav: Kehot Publication Society, CC BY-NC, via Sefaria. "
           "Kitzur Shulchan Aruch Yalkut Yosef, 5767 edition, Torat Emet database: all rights reserved to Rav Yitzchak Yosef, under the CC BY-NC-SA 2.5 licence, no commercial use (creativecommons.org/licenses/by-nc-sa/2.5/). "
           "Answers from Hidabroot, Kav HaHalacha HaSefaradi, Rav Ofir Malka’s “Halacha LeMaaseh” beit hora’ah and Rav Binyamin Chota (Kikar HaShabbat): summarised with references, not reproduced. "
           "French and English written by computer from the sources; every Hebrew quotation has been re-read at its source. A second automatic review of the French and English against the sources is done for the first 31 laws and under way for those added on 26 Nov 2026. Not reviewed by a rabbi: the Hebrew prevails.</small>"),
}

TITRE = {"he": "הלכות שנים מקרא ואחד תרגום", "fr": "Chnayim mikra : les halakhot", "en": "Shnayim mikra: the laws"}

SOURCES_META = [
    "Choul'han Aroukh O.H. 285 et Rema — Maginei Eretz, Lemberg 1893 (via API Sefaria), Public Domain",
    "Michna Beroura 285 et 669:4 — On Your Way (via API Sefaria), Public Domain ; Béour Halakha 285 et 494 — Biur Halacha (via API Sefaria), Public Domain",
    "Maguen Avraham 285 ; Taz et Cha'arei Techouva 285 — Maginei Eretz, Lemberg 1893 ; Baèr Hétev 285 et 128 — Torat Emet 357 ; Eliya Rabba 139 et 260 — Sulzbach 1757 ; 'Hayé Adam, Chabbat 7:9 — Vilna 1844 (via API Sefaria), Public Domain",
    "Choul'han Aroukh O.H. 139, 146 et 553 — Maginei Eretz, Lemberg 1893 ; Choul'han Aroukh Y.D. 400:1, Chakh et Rabbi Akiva Eiger — Ashlei Ravrevei, Lemberg 1888 (via API Sefaria), Public Domain",
    "Séfer 'Hassidim 301 et 745 — Zhitomir 1857 ; Moré beEtsba (Livourne 1842) et Tsiporen Chamir (Presbourg 1859) du 'Hida (via API Sefaria), Public Domain",
    "Aroukh haChoul'han O.H. 285 et 139 — Wikisource (via API Sefaria), CC-BY-SA : texte de 1903-1907 dans le domaine public, saisie et ponctuation de Wikisource ; courtes citations, créditées en tête du livre",
    "Kaf ha'Haïm O.H. 285, 25, 128, 496 et 553 — Jérusalem 1910-1933 (via API Sefaria), Public Domain",
    "Kitsour Choul'han Aroukh 72, 125 et 219 — Torat Emet 357 (via API Sefaria), Public Domain",
    "Ben Ich 'Haï — Wikisource (via API Sefaria), Public Domain",
    "Rambam, Hilkhot Tefila 13:25 — Torat Emet 370 (via API Sefaria), Public Domain",
    "Choul'han Aroukh haRav O.H. 285 — Kehot Publication Society (via API Sefaria), CC-BY-NC : courtes citations sans vocalisation, créditées en tête du livre",
    "Kitsour Yalkout Yossef 285 — édition Torat Emet, mahadoura 5767 : CC BY-NC-SA 2.5, la licence publique de tous les livres de la base hors Wikisource (toratemetfreeware.com/contents/copyrights2.html, lu le 26/11/2026) ; aucune autorisation à demander, à trois conditions : mention des droits en tête, usage non commercial, partage à l'identique",
    "réponses de Hidabroot, Kav haHalakha haSefaradi, du beit hora'a Halakha lema'assé (Rav Ofir Malka) et du Rav Binyamin 'Hota (Kikar haChabbat) — résumées avec leur référence, non reproduites (une courte phrase citée au plus) ; table de vérification : tools/chnayim_mikra/sources.json",
]


def blocs_halakha(n, h):
    """Le paragraphe affiché : hébreu (citations et références), français, anglais."""
    lignes = []
    for r in h["refs"]:
        ref = ref_texte(r, "he")
        if r["cite"]:
            lignes.append(f"{r['cite']} <small>({ref})</small>")
        elif r["src"] in ("hid", "kav", "malka", "kikar"):
            lignes.append(f"<small>({ref})</small>")
        else:
            raise ValueError(f"halakha {n} : source classique sans citation {r}")
    # Deux citations successives de la même référence ne la répètent pas.
    fusion = []
    for r, l in zip(h["refs"], lignes):
        if fusion and fusion[-1][0] == ref_texte(r, "he") and r["cite"]:
            prec = fusion[-1][1].rsplit(" <small>", 1)[0]
            fusion[-1] = (fusion[-1][0], f"{prec} … {r['cite']} <small>({fusion[-1][0]})</small>")
        else:
            fusion.append((ref_texte(r, "he"), l))
    he_tag = f" <small>{ETIQUETTES[h['rite']]['he']}</small>" if h["rite"] in ETIQUETTES else ""
    fr_tag = f" <small>{ETIQUETTES[h['rite']]['fr']}</small>" if h["rite"] in ETIQUETTES else ""
    en_tag = f" <small>{ETIQUETTES[h['rite']]['en']}</small>" if h["rite"] in ETIQUETTES else ""
    t = f"<b>{lettres(n, geresh=False)}</b>{he_tag} " + "<br>".join(l for _, l in fusion)
    fr = typo_fr(f"<b>{n}</b>{fr_tag} {h['fr']} <small>[{crochets(h['refs'], 'fr')}]</small>")
    en = typo_en(f"<b>{n}</b>{en_tag} {h['en']} <small>[{crochets(h['refs'], 'en')}]</small>")
    refs = []
    for r in h["refs"]:
        if ref_texte(r, "fr") not in refs:
            refs.append(ref_texte(r, "fr"))
    return {"id": f"chm-{n:02d}", "rite": h["rite"], "refs": refs,
            "t": t, "fr": fr, "en": en}


def livre():
    sections = [{"titre": "מבוא", "titre_fr": "Introduction", "titre_en": "Introduction",
                 "blocs": [{"t": INTRO["t"], "fr": typo_fr(INTRO["fr"]), "en": typo_en(INTRO["en"])}]}]
    n = 0
    for s in SECTIONS:
        blocs = []
        for h in s["halakhot"]:
            n += 1
            blocs.append(blocs_halakha(n, h))
        sections.append({"titre": s["titre"], "titre_fr": typo_fr(s["titre_fr"]), "titre_en": typo_en(s["titre_en"]), "blocs": blocs})
    return {
        "id": "chnayim_mikra",
        "groupe": "halakha",
        "titre": TITRE,
        "source": "Choul'han Aroukh et Rema avec leurs commentaires (Maguen Avraham, Taz, Baèr Hétev, Cha'arei Techouva, Eliya Rabba), Michna Beroura et Béour Halakha, 'Hayé Adam, Kitsour Choul'han Aroukh, Choul'han Aroukh haRav (Kehot, CC-BY-NC), Aroukh haChoul'han (Wikisource, CC-BY-SA), Kaf ha'Haïm, Ben Ich 'Haï, 'Hida, Séfer 'Hassidim, Rambam ; Kitsour Yalkout Yossef (Torat Emet, CC BY-NC-SA 2.5) ; réponses de Hidabroot, Kav haHalakha haSefaradi, Halakha lema'assé et du Rav Binyamin 'Hota (Kikar haChabbat), résumées — tools/chnayim_mikra/sources.json",
        "traduction": f"FR et EN rédigées par Claude ({DATE}) d'après les sources citées, chaque halakha avec sa référence ; relecture humaine souhaitable.",
        "rites": RITES,
        # Les sources et licences du livre.
        "_meta": {"sources": SOURCES_META, "verification": "tools/chnayim_mikra/sources.json",
                  "nature": "Recueil : citations hébraïques exactes des sources ; français et anglais rédigés d'après elles ; réponses d'aujourd'hui résumées avec leur référence, non reproduites."},
        "sections": sections,
    }


# --- La table de vérification -----------------------------------------------------------------

def sur_sefaria(src):
    return src == "bih" or "sefaria" in CLASSIQUES.get(src, {})


def sefaria(r):
    s, n = r["src"], r["num"]
    if s == "bih":
        annee, par_sefaria = n[0], n[1]
        ref = f"Ben Ish Hai, Halachot {BIH_ANNEE[annee][0]}, {par_sefaria} {n[5]}"
        version = BIH_VERSION
    else:
        c = CLASSIQUES[s]
        sm, para = lieu(r)
        ref = c["sefaria"].format(s=sm, n=para)
        version = c.get("versions", {}).get(sm, c["version"])
    api = ("https://www.sefaria.org/api/v3/texts/" + urllib.parse.quote(ref)
           + "?version=" + urllib.parse.quote("hebrew|" + version) + "&return_format=text_only")
    page = "https://www.sefaria.org/" + urllib.parse.quote(ref.replace(" ", "_").replace(",_", ",_")) + "?lang=he"
    return ref, version, api, page


def abrege(passage, morceau=12, total=25):
    """
    Le passage sur lequel repose un résumé, réduit à ses repères : les réponses d'aujourd'hui sont protégées,
    la table ne doit pas les recopier. Chaque morceau garde ses premiers et ses derniers mots (« [...] » entre
    les deux), assez pour retrouver le passage dans la page ; --verifie cherche chaque morceau tel quel.
    """
    def court(m):
        mots = m.split()
        return m.strip() if len(mots) <= morceau else " ".join(mots[:6]) + " [...] " + " ".join(mots[-5:])
    morceaux = [court(m) for m in passage.split("[...]") if m.strip()]
    sortie = " [...] ".join(morceaux)
    if len(sortie.replace("[...]", " ").split()) > total:
        sortie = morceaux[0] + " [...] " + morceaux[-1]
    return sortie


def table():
    lignes = []
    n = 0
    for si, s in enumerate(SECTIONS, start=1):
        for h in s["halakhot"]:
            n += 1
            refs = []
            for r in h["refs"]:
                e = {"source": r["src"], "reference": ref_texte(r, "fr"), "reference_he": ref_texte(r, "he"),
                     "edition": EDITIONS[r["src"]]["edition"], "licence": EDITIONS[r["src"]]["licence"]}
                if sur_sefaria(r["src"]):
                    ref, version, api, page = sefaria(r)
                    e.update({"edition": version, "sefaria_ref": ref, "sefaria_version": version, "lu_via": api, "page": page})
                elif r["src"] == "kyy":
                    e.update({"lu_via": "livre_yalkut_yosef_kitsour.json (archive de My Hitbodedut), section « סימן רפה - לקרוא הפרשה ב' מקרא וא' תרגום », se'if " + lettres(r["num"], geresh=False)})
                else:
                    m = MODERNES[(r["src"], r["num"])]
                    e.update({"url": url_moderne(r["src"], r["num"]), "auteur": m["auteur"], "titre": m["titre"], "date": m["date"],
                              "nature": "paraphrase avec référence (œuvre protégée)"})
                if r["cite"]:
                    e["citation"] = r["cite"]
                if r["passage"]:
                    e["passage_resume"] = abrege(r["passage"])
                refs.append(e)
            lignes.append({"id": f"chm-{n:02d}", "section": si, "rite": h["rite"], "rites_app": RITES[h["rite"]], "references": refs})
    return {
        "_meta": {
            "livre": "chnayim_mikra (data/livre_chnayim_mikra.json ; application : web/data/halakhot.js)",
            "date": DATE,
            "outil": "tools/chnayim_mikra/construction.py (--verifie relit chaque citation à sa source)",
            "regle": "Chaque « citation » est le texte exact de la source lue (sans balises) ; « passage_resume » donne les repères (premiers et derniers mots) du passage sur lequel repose un résumé, pour les œuvres protégées, qui ne sont reproduites ni dans l'application ni ici.",
            "rites": RITES,
            "editions": EDITIONS,
            "non_retenus": NON_RETENUS,
        },
        "halakhot": lignes,
    }


NON_RETENUS = [
    "Garçons (mineurs) : aucune source lue ne traite de leur obligation ou de leur éducation à Chnayim mikra.",
    "Parachiot jumelées : aucune source lue n'en parle pour Chnayim mikra (le Choul'han Aroukh 284:7 ne traite que de la haftara publique).",
    "Chabbat qui tombe un Yom Tov : quelle paracha lire cette semaine-là n'est dit explicitement par aucune source lue ; seule la règle « pas de Chnayim mikra pour la lecture de Yom Tov » (285:7) est retenue.",
    "Rav Binyamin 'Hota : deux réponses de « הלכה ב-60 שניות » (Kikar haChabbat) dont la page donne le texte sont reprises (halakhot 5 et 6). Les autres sont en vidéo ou en enregistrement seulement (Kikar haChabbat 2022-2023 et 13/02/2026, chaîne du kollel 'Hazon Ovadia, Kol haLachon) : rien n'en est tiré, faute de texte à relire. Ses livres « כי בו שבת » ne sont pas en ligne.",
    "Rav Ofir Malka lui-même : aucune réponse écrite de sa main trouvée ; les deux réponses retenues sont celles des rabbanim de son beit hora'a (hl5047.co.il).",
]


# --- La vérification ----------------------------------------------------------------------------

def plat(t):
    t = html.unescape(t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = unicodedata.normalize("NFC", t).replace(" ", " ")
    return re.sub(r"\s+", " ", t).strip()


def lire_url(url, essais=4):
    """Lit une page ; en cas de refus passager (429, 5xx, coupure), attend et recommence."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (verification chnayim_mikra)"})
    for essai in range(essais):
        try:
            with urllib.request.urlopen(req, timeout=60) as f:
                return f.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504) or essai == essais - 1:
                raise
        except (urllib.error.URLError, TimeoutError):
            if essai == essais - 1:
                raise
        time.sleep(3 * (essai + 1))


def texte_sefaria(api):
    d = json.loads(lire_url(api))
    morceaux = []

    def tout(x):
        if isinstance(x, list):
            for y in x:
                tout(y)
        elif isinstance(x, str):
            morceaux.append(x)
    for v in d.get("versions", []):
        tout(v.get("text"))
    return plat(" ".join(morceaux))


def texte_yalkut(num):
    y = json.load(open(YALKUT, encoding="utf-8"))
    siman = next(s for s in y["textes"][0]["sections"] if s["titre"].startswith("סימן רפה "))
    lettre = lettres(num, geresh=False)
    bloc = next(b for b in siman["blocs"] if b.get("t", "").startswith(f"<b>{lettre}</b>"))
    return plat(bloc["t"])


def verifie():
    fautes, vus, non_relues = [], {}, []
    for h in table()["halakhot"]:
        for e in h["references"]:
            if "lu_via" in e and e["lu_via"].startswith("http"):
                cle = e["lu_via"]
                if cle not in vus:
                    vus[cle] = texte_sefaria(cle)
                source = vus[cle]
            elif e["source"] == "kyy":
                if not YALKUT:
                    non_relues.append(f"{h['id']} {e['reference']}")
                    print(f"{h['id']} {e['reference']} : non relu (--yalkut absent)")
                    continue
                source = texte_yalkut(int(re.search(r"285:(\d+)", e["reference"]).group(1)))
            else:
                cle = e["url"]
                if cle not in vus:
                    vus[cle] = plat(lire_url(cle))
                source = vus[cle]
            for champ in ("citation", "passage_resume"):
                if champ in e:
                    attendu = plat(e[champ]).replace(" [...] ", " ")
                    morceaux = [m.strip() for m in plat(e[champ]).split("[...]")]
                    if not all(m and m in source for m in morceaux):
                        fautes.append(f"{h['id']} {e['reference']} ({champ}) : « {attendu[:90]} »")
            print(f"{h['id']} {e['reference']} : lu")
    print()
    if non_relues:
        print(f"{len(non_relues)} citation(s) du Kitsour Yalkout Yossef non relue(s) : relancer avec --yalkut <fichier>")
    if fautes:
        print(f"{len(fautes)} citation(s) introuvable(s) :")
        print("\n".join(fautes))
        sys.exit(1)
    print("toutes les citations relues sont dans leurs sources")


# --- L'écriture ---------------------------------------------------------------------------------

def ecrire():
    nouveau = livre()
    with open(LIVRE, "w", encoding="utf-8") as f:
        json.dump(nouveau, f, ensure_ascii=False, indent=1)
        f.write("\n")
    with open(TABLE, "w", encoding="utf-8") as f:
        json.dump(table(), f, ensure_ascii=False, indent=1)
        f.write("\n")
    n = sum(1 for s in nouveau["sections"] for b in s["blocs"] if "id" in b)
    print(f"chnayim_mikra : {n} halakhot en {len(nouveau['sections'])} chapitres ; table : {os.path.relpath(TABLE, RACINE)}")


if __name__ == "__main__":
    if "--verifie" in sys.argv:
        verifie()
    else:
        ecrire()
