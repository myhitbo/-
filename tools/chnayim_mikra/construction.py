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
  - Michna Beroura 285, 553:10 et 669:4 — « On Your Way » ; Béour Halakha 285 et 494 — « Biur Halacha »
    (API Sefaria), Public Domain ;
  - Kaf ha'Haïm O.H. 285 (et 25, 128, 496, 553) — « Kaf Hachayim, Orach Chayim vol. I-IV » et
    « vol. V-VIII, Jerusalem 1910-1933 » (API Sefaria), Public Domain ;
  - Kitsour Choul'han Aroukh 72, 125, 219 — « Torat Emet 357 » (API Sefaria), Public Domain ;
  - Ben Ich 'Haï — « Ben Ish Hai -- Wikisource » (API Sefaria), Public Domain, l'édition du
    Ben Ich 'Haï de My Hitbodedut ; le 'Hida, Moré beEtsba (Livourne 1842) et Tsiporen Chamir
    (Presbourg 1859) ; Séfer 'Hassidim (Zhitomir 1857) — API Sefaria, Public Domain ;
  - Choul'han Aroukh Y.D. 400:1, Taz, Chakh, Rabbi Akiva Eiger — « Ashlei Ravrevei: Shulchan Aruch
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

Sources d'aujourd'hui (demandes du propriétaire du 26/11/2026) : réponses de Hidabroot
(« שאל את הרב »), de Kav haHalakha haSefaradi (kavhalacha.co.il), du beit hora'a « Halakha
lema'assé » du Rav Ofir Malka (hl5047.co.il) et du Rav Binyamin 'Hota (« הלכה ב-60 שניות »,
Kikar haChabbat, kikar.co.il : les deux réponses dont la page donne le texte ; les autres sont
en vidéo seulement et ne sont pas reprises). « Halacha broura » : le siman 285 de « הלכה ברורה »
du Rav David Yossef (volume 17) ne se lit pas en ligne ; sont repris à la place ses cours
hebdomadaires (traduction anglaise, halachayomit.co.il/he/pdf/) et les articles de Halacha
Yomit, d'après les décisions du Rav Ovadia Yossef (voir NON_RETENUS). Œuvres protégées : rien
n'en est recopié ; chaque réponse est résumée, attribuée (auteur, titre, date, adresse), avec
au plus une courte phrase citée.

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
import shutil
import subprocess
import sys
import tempfile
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
    "tazyd": {"titre": "Taz (Tourei Zahav), Yoré Déa", "edition": "Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888", "licence": "Public Domain"},
    "shakh": {"titre": "Chakh (Siftei Cohen), Yoré Déa", "edition": "Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888", "licence": "Public Domain"},
    "rae": {"titre": "Rabbi Akiva Eiger, gloses du Yoré Déa", "edition": "Ashlei Ravrevei: Shulchan Aruch Yoreh Deah, Lemberg, 1888", "licence": "Public Domain"},
    "sch": {"titre": "Séfer 'Hassidim", "edition": "Sefer Chassidim, Zhitomir, 1857", "licence": "Public Domain"},
    "mbe": {"titre": "Moré beEtsba, du 'Hida", "edition": "Moreh BeEtzba, Livorno, 1842", "licence": "Public Domain"},
    "tsh": {"titre": "Tsiporen Chamir, du 'Hida", "edition": "Avodat HaKodesh, Pressburg, 1859", "licence": "Public Domain"},
    "hid": {"titre": "Hidabroot, « שאל את הרב »", "edition": "hidabroot.org", "licence": "Tous droits réservés : résumé et référence, au plus une courte phrase citée"},
    "kav": {"titre": "Kav haHalakha haSefaradi (קו ההלכה הספרדי)", "edition": "kavhalacha.co.il", "licence": "Tous droits réservés : résumé et référence, au plus une courte phrase citée"},
    "malka": {"titre": "Beit hora'a « Halakha lema'assé » du Rav Ofir Malka (הלכה למעשה)", "edition": "hl5047.co.il", "licence": "Tous droits réservés : résumé et référence, au plus une courte phrase citée"},
    "kikar": {"titre": "Kikar haChabbat, « הלכה ב-60 שניות », Rav Binyamin 'Hota (כיכר השבת)", "edition": "kikar.co.il", "licence": "Tous droits réservés : résumé et référence, au plus une courte phrase citée"},
    "ryd": {"titre": "Rav David Yossef, Richon leTsion, auteur de « Halakha Beroura » : cours hebdomadaire (השיעור השבועי)",
            "edition": "traduction anglaise publiée sur halachayomit.co.il/he/pdf/", "licence": "Tous droits réservés : résumé et référence",
            "note": "Le siman 285 de « Halakha Beroura » (volume 17, simanim 275-286, Makhon Ye'havé Daat) ne se lit pas en ligne : rien n'en est cité. Ces cours sont lus dans leur traduction anglaise : les repères de la table sont en anglais ; --verifie les relit avec pdftotext."},
    "hy": {"titre": "Halacha Yomit (הלכה יומית), d'après les décisions du Rav Ovadia Yossef", "edition": "halachayomit.co.il",
           "licence": "Tous droits réservés : résumé et référence, au plus une courte phrase citée",
           "note": "Ajouté le 26/11/2026, faute de pouvoir lire « Halakha Beroura ». Les articles sont rediffusés chaque année : la date est celle du dernier envoi. Les questions-réponses sous un article sont des réponses de la rédaction du site, chacune datée."},
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
    "tazyd": {"siman": 400, "sefaria": "Turei Zahav on Shulchan Arukh, Yoreh De'ah {s}:{n}", "version": ASHLEI,
              "fr": "Taz Y.D. {s}:{n}", "en": "Taz Y.D. {s}:{n}", "he": "ט״ז יו״ד {S}, ס״ק {N}"},
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
    # Ajoutées le 26/11/2026 (recherche du jour ; œuvres protégées : résumées, jamais recopiées).
    ("hid", "217642"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "שומע כעונה בשניים מקרא ואחד תרגום", "date": "16/11/2016", "date_he": "ט״ו חשון התשע״ז"},
    ("hid", "111245"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "שניים מקרא ואחד תרגום ביום טוב שחל בשבת", "date": "01/04/2015", "date_he": "י״ב ניסן התשע״ה"},
    ("hid", "356863"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "שמו\"ת", "date": "26/03/2026", "date_he": "ח׳ ניסן התשפ״ו"},
    ("hid", "234777"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "האם מותר לקרוא שמות בחול המועד", "date": "25/09/2017", "date_he": "ה׳ תשרי התשע״ח"},
    ("hid", "235423"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "שניים מקרא ואחד תרגום של פרשת בראשית", "date": "03/10/2017", "date_he": "י״ג תשרי התשע״ח"},
    ("hid", "307701"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "שניים מקרא ואחד תרגום בתשעה באב", "date": "08/09/2022", "date_he": "י״ב אלול התשפ״ב"},
    ("hid", "324169"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "האם מותר לקרוא שניים מקרא ואחד תרגום כשביום שישי חל חג?", "date": "25/05/2023", "date_he": "ה׳ סיון התשפ״ג"},
    ("hid", "290482"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "איך לקרוא שניים מקרא ואחד תרגום?", "date": "16/03/2021", "date_he": "ג׳ ניסן התשפ״א"},
    ("hid", "356365"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "שמו\"ת", "date": "09/02/2026", "date_he": "כ״ב שבט התשפ״ו"},
    ("hid", "233792"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "האם אפשר לקרוא תרגום יונתן במקום תרגום אונקלוס?", "date": "06/09/2017", "date_he": "ט״ו אלול התשע״ז"},
    ("hid", "203590"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "שניי'ם מקרא ואחד תרגום", "date": "11/04/2016", "date_he": "ג׳ ניסן התשע״ו"},
    ("hid", "15646"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "האם מותר לי למחוק את שם ה-ו-י-ה, בתכנת וורד במחשב", "date": "25/02/2014", "date_he": "כ״ה אדר א׳ התשע״ד"},
    ("hid", "274474"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "קריאת שניים מקרא ואחד תרגום", "date": "05/11/2019", "date_he": "ז׳ חשון התש״פ"},
    ("hid", "259534"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "אפשר לקרוא מקרא ואז תרגום ואז שוב מקרא?", "date": "31/01/2019", "date_he": "כ״ה שבט התשע״ט"},
    ("hid", "255408"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "סדר קריאת שניים מקרא ואחד תרגום", "date": "29/10/2018", "date_he": "כ׳ חשון התשע״ט"},
    ("hid", "27340"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "מהו סדר קריאת שניים מקרא ואחד תרגום.?", "date": "25/02/2014", "date_he": "כ״ה אדר א׳ התשע״ד"},
    ("hid", "286915"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "ממתי אפשר לקרוא שניים מקרא ואחד תרגום?", "date": "30/11/2020", "date_he": "י״ד כסלו התשפ״א"},
    ("hid", "260576"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "שניים מקרא ואחד תרגום בלב", "date": "16/02/2019", "date_he": "י״א אדר א׳ התשע״ט"},
    ("hid", "241128"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "האם יש איסור לקרוא שניים מקרא אחד תרגום מהמחשב או פלאפון?", "date": "23/01/2018", "date_he": "ז׳ שבט התשע״ח"},
    ("hid", "331141"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "אם אני לא יכול לקרוא שניים מקרא ואחד תרגום האם יש משהו קצר יותר שאפשר לקרוא במקום?", "date": "14/05/2024", "date_he": "ו׳ אייר התשפ״ד"},
    ("hid", "226173"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "שניים מקרא ואחד תרגום בפרשיות מחוברות", "date": "30/04/2017", "date_he": "ד׳ אייר התשע״ז"},
    ("hid", "31258"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "שניים מקרא ואחד תרגום, מה הכוונה?", "date": "25/02/2014", "date_he": "כ״ה אדר א׳ התשע״ד"},
    ("hid", "298335"): {"auteur": "Hillel Meirs", "auteur_he": "הרב הלל מאירס", "titre": "האם מי שקרא שמו\"ת יכול לטבול לכבוד שבת לפני חצות היום?", "date": "06/11/2021", "date_he": "ב׳ כסלו התשפ״ב"},
    ("hid", "170276"): {"auteur": "Binyamin Chmouéli", "auteur_he": "הרב בנימין שמואלי", "titre": "שם ה' בקריאת שניים מקרא ואחד תרגום", "date": "30/10/2015", "date_he": "י״ז חשון התשע״ו"},
    ("kav", "azoulay2"): {"auteur": "Rav Ochri Azoulay", "auteur_court": "Rav O. Azoulay", "auteur_he": "הרב אושרי אזולאי", "titre": "האם חייבים לקרוא שנים מקרא ואחד תרגום - הרב אושרי אזולאי", "date": "09/10/2026", "date_he": "כ״ח תשרי התשפ״ז", "url": "https://kavhalacha.co.il/%D7%90%D7%A7%D7%98%D7%95%D7%90%D7%9C%D7%99%D7%94-%D7%91%D7%94%D7%9C%D7%9B%D7%94/%D7%94%D7%9C%D7%9B%D7%95%D7%AA-%D7%9E%D7%A2%D7%A0%D7%99%D7%99%D7%A0%D7%95%D7%AA/%D7%94%D7%90%D7%9D-%D7%97%D7%99%D7%99%D7%91%D7%99%D7%9D-%D7%9C%D7%A7%D7%A8%D7%95%D7%90-%D7%A9%D7%A0%D7%99%D7%9D-%D7%9E%D7%A7%D7%A8%D7%90-%D7%95%D7%90%D7%97%D7%93-%D7%AA%D7%A8%D7%92%D7%95%D7%9D-%D7%94%D7%A8%D7%91-%D7%90%D7%95%D7%A9%D7%A8%D7%99-%D7%90%D7%96%D7%95%D7%9C%D7%90%D7%99"},
    ("kav", "yaron3"): {"auteur": "Rav Yaron Achkenazi", "auteur_court": "Rav Y. Achkenazi", "auteur_he": "הרב ירון אשכנזי", "titre": "הלכה יומית - הרב ירון אשכנזי - שאין לסיים העליה כשיש פחות מג' פסוקים לסוף הפרשה", "date": "12/07/2017", "date_he": "י״ח תמוז התשע״ז", "url": "https://kavhalacha.co.il/%D7%90%D7%A7%D7%98%D7%95%D7%90%D7%9C%D7%99%D7%94-%D7%91%D7%94%D7%9C%D7%9B%D7%94/%D7%9E%D7%90%D7%92%D7%A8-%D7%94%D7%94%D7%9C%D7%9B%D7%95%D7%AA/%D7%A7%D7%A8%D7%99%D7%90%D7%AA-%D7%94%D7%AA%D7%95%D7%A8%D7%94/2017-05-30-05-42-84"},
    ("kav", "yaron4"): {"auteur": "Rav Yaron Achkenazi", "auteur_court": "Rav Y. Achkenazi", "auteur_he": "הרב ירון אשכנזי", "titre": "הלכה יומית - הרב ירון אשכנזי - האם קריאת התורה חובת ציבור או חובת יחיד", "date": "27/05/2017", "date_he": "ב׳ סיון התשע״ז", "url": "https://kavhalacha.co.il/%D7%90%D7%A7%D7%98%D7%95%D7%90%D7%9C%D7%99%D7%94-%D7%91%D7%94%D7%9C%D7%9B%D7%94/%D7%9E%D7%90%D7%92%D7%A8-%D7%94%D7%94%D7%9C%D7%9B%D7%95%D7%AA/%D7%A7%D7%A8%D7%99%D7%90%D7%AA-%D7%94%D7%AA%D7%95%D7%A8%D7%94/2017-05-30-05-42-72"},
    ("kav", "dyaakov"): {"auteur": "Rav David Yaakov", "auteur_court": "Rav D. Yaakov", "auteur_he": "הרב דוד יעקב", "titre": "הושענא רבה ושמחת תורה - הרב דוד יעקב", "date": "01/10/2026", "date_he": "כ׳ תשרי התשפ״ז", "url": "https://kavhalacha.co.il/%D7%90%D7%A7%D7%98%D7%95%D7%90%D7%9C%D7%99%D7%94-%D7%91%D7%94%D7%9C%D7%9B%D7%94/%D7%97%D7%92%D7%99%D7%9D-%D7%95%D7%9E%D7%95%D7%A2%D7%93%D7%99%D7%9D/2017-10-02-07-45-35/%D7%94%D7%95%D7%A9%D7%A2%D7%A0%D7%90-%D7%A8%D7%91%D7%94-%D7%95%D7%A9%D7%9E%D7%97%D7%AA-%D7%AA%D7%95%D7%A8%D7%94-%D7%94%D7%A8%D7%91-%D7%93%D7%95%D7%93-%D7%99%D7%A2%D7%A7%D7%91"},
    ("malka", "520"): {"auteur": "Rav Emmanuel Molkandov", "auteur_court": "Rav E. Molkandov", "auteur_he": "הרב עמנואל מולקנדוב", "titre": "טבילה בערב שבת אם קרא שמו\"ת בימי השבוע", "date": "10/10/2026", "date_he": "10.10.2026"},
    ("malka", "564"): {"auteur": "Rav Emmanuel Molkandov", "auteur_court": "Rav E. Molkandov", "auteur_he": "הרב עמנואל מולקנדוב", "titre": "ספק בנוסח קריאת שמו\"ת – חזרה על מילים וסדר הנוסחים", "date": "04/11/2026", "date_he": "04.11.2026"},
    ("hy", "1659"): {"auteur": "Halacha Yomit", "auteur_he": "הלכה יומית", "titre": "שניים מקרא ואחד תרגום", "date": "05/10/2026", "date_he": "כ״ד תשרי התשפ״ז"},
    # Les questions-réponses placées sous un article ont chacune leur date (de 2010 à 2022 pour celles qui sont
    # résumées ici) : « date » dit leurs années, non la date du dernier envoi de l'article.
    ("hy", "1659q"): {"auteur": "Halacha Yomit, réponses de la rédaction", "auteur_he": "הלכה יומית", "titre": "שניים מקרא ואחד תרגום",
                      "date": "questions-réponses publiées sous l’article, en 2018", "date_en": "Q&A published under the article, 2018",
                      "date_he": "שאלות ותשובות שנתפרסמו תחת המאמר, תשע״ט (תשובות מערכת האתר)"},
    ("hy", "1660"): {"auteur": "Halacha Yomit", "auteur_he": "הלכה יומית", "titre": "פרטי דינים בהלכות שניים מקרא ואחד תרגום", "date": "06/10/2026", "date_he": "כ״ה תשרי התשפ״ז"},
    ("hy", "1660q"): {"auteur": "Halacha Yomit, réponses de la rédaction", "auteur_he": "הלכה יומית", "titre": "פרטי דינים בהלכות שניים מקרא ואחד תרגום",
                      "date": "questions-réponses publiées sous l’article, de 2010 à 2022", "date_en": "Q&A published under the article, 2010–2022",
                      "date_he": "שאלות ותשובות שנתפרסמו תחת המאמר, תשע״א–תשפ״ג (תשובות מערכת האתר)"},
    ("hy", "2740"): {"auteur": "Halacha Yomit", "auteur_he": "הלכה יומית", "titre": "הושענא רבה", "date": "01/10/2026", "date_he": "כ׳ תשרי התשפ״ז"},
    ("ryd", "323"): {"auteur": "Rav David Yossef", "auteur_he": "הראשון לציון הרב דוד יוסף", "titre": "The Final Time for Reciting Shenayim Mikra Ve’Echad Targum", "date": "motsaé Chabbat Lekh Lekha 5786", "date_he": "מוצאי שבת לך לך התשפ״ו", "url": "https://halachayomit.co.il/he/pdf/6322.pdf"},
    ("ryd", "351"): {"auteur": "Rav David Yossef", "auteur_he": "הראשון לציון הרב דוד יוסף", "titre": "The Time for Reading Shenayim Mikra Ve’Echad Targum This Shavuot", "date": "motsaé Chabbat Bamidbar 5786", "date_he": "מוצאי שבת במדבר התשפ״ו", "url": "https://halachayomit.co.il/he/pdf/6376.pdf"},
    ("ryd", "369"): {"auteur": "Rav David Yossef", "auteur_he": "הראשון לציון הרב דוד יוסף", "titre": "Chag HaSukkot – Simchat Torah, § 149", "date": "recueil pour Souccot et Sim'hat Torah", "date_he": "קובץ לחג הסוכות ושמחת תורה", "url": "https://halachayomit.co.il/he/pdf/6414.pdf"},
}


AUJOURDHUI = ("hid", "kav", "malka", "kikar", "hy", "ryd")


def url_moderne(src, n):
    if src == "hy":
        return f"https://halachayomit.co.il/he/Default.aspx?HalachaID={n.rstrip('q')}"
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
    if s in AUJOURDHUI:
        m = MODERNES[(s, n)]
        if s == "ryd":
            return {"fr": f"Rav David Yossef, cours n° {n}", "en": f"Rav David Yosef, shiur no. {n}",
                    "he": f"הראשון לציון הרב דוד יוסף, ״השיעור השבועי״, גיליון {n} ({m['date_he']}), בתרגום לאנגלית: {m['url'].replace('https://', '')}"}[langue]
        if s == "hy":
            num, qr = n.rstrip("q"), n.endswith("q")
            if qr:
                # Réponses de la rédaction du site, placées sous l'article : ni la date de l'article, ni le nom du Rav Ovadia Yossef.
                return {"fr": f"Halacha Yomit n° {num} ({m['date']})",
                        "en": f"Halacha Yomit no. {num} ({m['date_en']})",
                        "he": f"הלכה יומית, ״{m['titre']}״, {m['date_he']}, halachayomit.co.il (HalachaID={num})"}[langue]
            return {"fr": f"Halacha Yomit n° {num}",
                    "en": f"Halacha Yomit no. {num}",
                    "he": f"הלכה יומית על פי פסקי מרן הרב עובדיה יוסף, ״{m['titre']}״, {m['date_he']}, halachayomit.co.il (HalachaID={num})"}[langue]
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
            # « 1, 2 et 3 », non « 1 et 2 et 3 ».
            nums = ", ".join(str(x["num"]) for x in rs[:-1]) + et + str(rs[-1]["num"])
            base = ref_texte(rs[0], langue).rsplit(" ", 1)[0].replace("question", "questions")
            sortie.append(f"{base} {nums}")
        elif s == "bih" and len(rs) > 1:
            base = ref_texte(rs[0], langue).rsplit("§", 1)[0]
            et = {"fr": " et ", "en": " and "}[langue]
            sortie.append(base + et.join(f"§{x['num'][5]}" for x in rs))
        elif s in ("kav", "kikar", "malka", "ber", "hy", "ryd") or len(rs) == 1 or lieu(rs[0])[0] is None:
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
            R("hy", "1660", passage='''היא בכלל מצות תלמוד תורה [...] תבא עליה הברכה, ויש לה שכר על כך'''),
        ],
            "Une femme est dispensée de lire chaque Chabbat Chnayim mikra véé'had targoum (Kitsour Yalkout Yossef). Le Rav Hillel Meirs (Hidabroot) répond de même que les femmes n'y sont pas obligées, en renvoyant au Michné Halakhot (t. 6, siman 60) et au 'Hazon Ovadia (Chabbat, t. 1, p. 328) ; dans une autre réponse, il lui semble qu'une épouse ne peut pas acquitter son mari malade en lisant pour lui, puisqu'elle-même n'y est pas du tout obligée. Halacha Yomit (d'après les décisions du Rav Ovadia Yossef) l'explique : Chnayim mikra relève de l'étude de la Torah, dont les femmes sont dispensées (hormis l'étude des lois et des points essentiels de la Torah qui les concernent) ; mais la femme qui veut lire la paracha deux fois avec le targoum est digne de bénédiction et en est récompensée, sans y être tenue.",
            "A woman is exempt from reading Shnayim mikra ve-echad targum every Shabbat (Kitzur Yalkut Yosef). Rav Hillel Meirs (Hidabroot) likewise answers that women are not obligated, citing Mishneh Halachot (vol. 6, siman 60) and Chazon Ovadia (Shabbat, vol. 1, p. 328); in another answer he writes that it seems a wife cannot discharge her sick husband by reading for him, since she herself is not obligated at all. Halacha Yomit (following the rulings of Rav Ovadia Yosef) explains: Shnayim mikra is part of Torah study, from which women are exempt (apart from studying the laws and the main points of the Torah that concern them); but a woman who wishes to read the parasha twice with the targum is to be blessed and is rewarded for it, without being obligated."),
        H("tous", [
            R("ahs", 2, cite='''ולא נודע לנו טעמו של דבר, ובוודאי בשעה שתקן משה רבינו לקרות בתורה – תקן גם כן תקנה זו'''),
            R("ahs", 2, cite='''והלבוש כתב: כדי שיהא בקי בתורה, עיין שם, ואין זה מספיק כמובן'''),
            R("ahs", 2, cite='''ולכן ילמוד מקודם בחומש, ויעלה בקודש לשמוע מספר תורה'''),
            R("ahs", 2, cite='''ואיתא בסוטה (לז ב): "כללות ופרטות נאמרו בסיני, ונשנו באהל מועד, ונשתלשו בערבות מואב", עיין שם. לכן צריך ללמוד שלוש פעמים, אפילו בפסוק שאין בו תרגום, כמו שיתבאר, כנגד אלו השלוש. אך במקום שיש תרגום – בחרו בתרגום הפעם השלישי, כדי שיבין מה שהוא לומד'''),
            R("ahs", 2, cite='''ויש אומרים: כנגד שנים הקורין, ואחד המתרגם (ראב"ן)'''),
            R("kh", 1, cite='''ואלה שמות ר"ת וחייב אדם להשלים הפרשה שניים מקרא ואחד תרגום. מש"ז או' א\''''),
        ],
            "Pourquoi cette lecture ? L'Aroukh haChoul'han écrit que la raison ne nous en est pas connue, et que Moché Rabbénou, en instituant la lecture de la Torah, a certainement institué aussi celle-ci. Il rapporte la raison du Levouch – être versé dans la Torah – et la juge insuffisante. Il lui semble que la Torah demande d'écouter et d'étudier ; on étudie donc d'abord dans le 'Houmach, puis l'on « monte en sainteté » en écoutant la lecture dans le séfer Torah. Et trois fois, même pour un verset sans targoum, parce que, d'après Sota 37b, les règles générales et les détails ont été dits au Sinaï, répétés dans la Tente d'assignation et dits une troisième fois dans les plaines de Moav ; là où il y a un targoum, on l'a choisi pour la troisième fois, afin de comprendre ce qu'on étudie. Il cite un autre avis, au nom du Raavan : en regard des deux qui lisent et de celui qui traduit. Le Kaf ha'Haïm rapporte, du Michbetsot Zahav (Pri Megadim), une allusion : les initiales de « Véélé chemot » forment, en hébreu, « on doit achever la paracha, deux fois le texte et une fois le targoum ».",
            "Why this reading? The Aruch HaShulchan writes that its reason is not known to us, and that Moshe Rabbenu, when he instituted the reading of the Torah, surely instituted this as well. He quotes the Levush's reason – to be well versed in the Torah – and finds it insufficient. It seems to him that the Torah calls for hearing and for studying; so one first studies in the Chumash, then “rises in holiness” by hearing the reading from the Torah scroll. And three times, even for a verse with no targum, because, as Sotah 37b says, the general rules and the details were said at Sinai, repeated in the Tent of Meeting and said a third time in the plains of Moav; where there is a targum, it was chosen for the third time, so that one understands what one studies. He cites another view, in the name of the Raavan: corresponding to the two who read and the one who translates. The Kaf HaChaim reports, from the Mishbetzot Zahav (Pri Megadim), a hint: the initials of “Ve'eleh shemot” spell out, in Hebrew, “one must complete the parasha, twice the text and once the targum”."),
        H("tous", [
            R("kh", 4, cite='''שאתה קורא הפ' שנים מקרא ואחד תרגום ברהיטא כחותה על הגחלים לפרוק עול מעליך'''),
            R("kh", 4, cite='''אבל צריך לקרות הפרשה בנחת ולהרגיש בדקדוקיה ולתרץ אותם ומה שלא תוכל לתרץ עיין במפרשים'''),
            R("sch", 301, cite='''יהודי אחד לא היה קורא שנים מקרא ואחד תרגום שמאריכין לו ימיו ושנותיו כי אמר אני קץ בחיי למה אקרא אמר ליה החכם לא אמר זה רק כנגד האוהבי חיים'''),
            R("sch", 301, cite='''שאין העבד עושה תנאי לרבו'''),
            R("sch", 301, cite='''לכך יקרא אדם שנים מקרא ואחד תרגום לשם מי שאמר למען תהיה תורת ה' בפיך'''),
            R("kh", 4, cite='''דיקרא האדם שמו"ת לשם מי שאמר למען תהיה תורת ה' בפיך'''),
            R("kh", 4, cite='''ומ"מ הקב"ה יאריך ימיו ושנותיו ואל יסמוך על תנאי'''),
            R("kh", 4, cite='''וע"כ קודם שיקרא הפ' שמו"ת י"ל לשם יחוד קבה"ו וכו' הריני בא לקרות הפ' של השבוע שמו"ת לתקן את שורשה במקום עליון. ויהי נועם וכו\''''),
        ],
            "On lit la paracha posément. Le Kaf ha'Haïm rapporte du Maguid Mécharim le reproche fait à Maran (Rabbi Yossef Karo) : la lire à la hâte, « comme on ramasse des braises », pour se décharger du joug ; il faut la lire avec calme, être attentif à ses difficultés, les résoudre, et chercher chez les commentateurs ce qu'on ne sait pas résoudre. Le Séfer 'Hassidim raconte qu'un homme ne lisait pas Chnayim mikra parce que, las de vivre, il ne voulait pas de la longue vie promise ; le sage lui répondit que cette promesse ne s'adresse qu'à ceux qui aiment la vie, et que les autres ne sont pas dispensés pour autant : le serviteur ne pose pas de condition à son maître. Le Séfer 'Hassidim conclut – et le Kaf ha'Haïm le cite – qu'on lit Chnayim mikra pour Celui qui a dit « afin que la Torah de Hachem soit dans ta bouche » : le Saint béni soit-Il prolongera de toute façon ses jours et ses années, mais on ne fait pas de cette récompense une condition. Le Kaf ha'Haïm ajoute pour sa part que c'est pourquoi il y a lieu de dire, avant de lire : « Léchem yi'houd… : je viens lire la paracha de la semaine, deux fois le texte et une fois le targoum, pour en réparer la racine en haut lieu », puis « Vihi noam… ».",
            "The parasha is read unhurriedly. The Kaf HaChaim reports from the Maggid Mesharim the reproach made to Maran (Rabbi Yosef Karo): reading it in haste, “like one raking coals”, to throw off the yoke; one must read it calmly, notice its difficulties, resolve them, and look in the commentators for what one cannot resolve. Sefer Chasidim tells of a man who did not read Shnayim mikra because, weary of life, he did not want the promised long life; the sage answered that this promise is addressed only to those who love life, and that the others are not thereby exempt: a servant sets no condition to his master. Sefer Chasidim concludes – and the Kaf HaChaim quotes it – that one reads Shnayim mikra for the sake of the One who said “so that the Torah of Hashem be in your mouth”: the Holy One, blessed be He, will lengthen his days and years in any case, but one does not make that reward a condition. The Kaf HaChaim adds for his part that this is why, before reading, one should say “Leshem yichud…: I come to read the parasha of the week, twice the text and once the targum, to repair its root on high”, followed by “Vihi noam…”."),
        H("sefarade", [
            R("kyy", 1, cite='''וגם העוסק בלימוד תורה כל היום, ותורתו אומנותו, לא יבטל קריאת פרשיותיו עם הצבור. וחייב לקרוא הפרשה שנים מקרא ואחד תרגום'''),
            R("hy", "1659", passage='''כי באמת מן הדין חייב אדם לקרוא שניים מקרא ואחד תרגום [...] אל יפשע מלהשלים פרשיותיו עם הציבור'''),
            R("kav", "azoulay2", passage='''וגם מי שתורתו אומנתו חייב בקריאת הפרשה'''),
            R("ryd", "351", passage='''is not just a preferred practice but an absolute obligation'''),
        ],
            "Même celui qui étudie la Torah toute la journée, et dont la Torah est le métier, ne néglige pas la lecture de ses parachiot avec la communauté : il doit lire la paracha deux fois dans le texte et une fois dans le targoum (Kitsour Yalkout Yossef). Halacha Yomit rappelle que ce n'est pas un simple bon conseil mais une obligation selon la loi, et cite une réponse des Guéonim : le talmid 'hakham, même s'il tient à son étude, ne néglige pas d'achever ses parachiot avec la communauté. Le Rav Ochri Azoulay (Kav haHalakha haSefaradi) écrit de même que celui dont la Torah est le métier y est tenu. Le Rav David Yossef, dans un cours, dit que ce n'est pas seulement un bon usage mais une obligation à part entière, une institution des Sages distincte de l'écoute de la lecture de la Torah.",
            "Even one who studies Torah all day, and whose Torah is his occupation, does not neglect reading his portions with the congregation: he must read the parasha twice in the text and once in the targum (Kitzur Yalkut Yosef). Halacha Yomit recalls that this is not mere good advice but an obligation by law, and quotes a responsum of the Geonim: a Torah scholar, even if he is eager for his own study, must not neglect completing his portions with the congregation. Rav Oshri Azoulay (Kav HaHalacha HaSefaradi) likewise writes that one whose Torah is his occupation is obligated. Rav David Yosef, in a shiur, says that this is a full obligation and not merely a commendable practice: a distinct enactment of the Sages, apart from hearing the Torah reading."),
        H("sefarade", [
            R("kh", 9, cite='''חולה וחש בעיניו פטורים וא"צ לשמוע מאחר'''),
            R("kh", 9, cite='''ומ"מ נראה דיש להשלימה אחר שיתרפא כדי שלא תהא תורתו של שמו"ת עולה לרקיע חסירה בשנה ההיא'''),
            R("kh", 10, cite='''סומא פטור מחיוב זה דדברים שבכתב א"א לאומרם ע"פ וא"צ לשמוע מאחר'''),
            R("kh", 10, cite='''וזהו לפום דינא אמנם המחמיר לשמוע מאחרים תע"ב וכן נכון לעשות'''),
            R("kh", 11, cite='''מי שאינו יודע לקרות פטור מחיוב זה וא"צ לשמוע מאחר'''),
            R("kyy", 15, cite='''אף מי שחלה בעיניו ומצטער בקריאת שנים מקרא ואחד תרגום, חייב לקרוא את הפרשה שנים מקרא ואחד תרגום, או שישמע הפרשה מאחר ויכוין לצאת ידי חובה'''),
            R("kyy", 16, cite='''יש אומרים שגם הסומא (עיור) חייב בשנים מקרא ואחד תרגום בכל שבת, כדין הפקח. ולכן צריך שישמע מאחר קריאת הפרשה שנים מקרא ואחד תרגום, ויכוין להוציאו ידי חובה, וגם הוא יתכוין לצאת ידי חובת הקריאה. וכן מי שנעשה אילם, ואינו יכול לדבר ולקרוא, ישמע הקריאה מאחר'''),
        ],
            "Le malade, l'aveugle, celui qui ne sait pas lire. Le Kaf ha'Haïm rapporte, au nom du Radbaz cité par le Ma'hazik Berakha : le malade et celui qui souffre des yeux sont dispensés et n'ont pas à écouter la lecture d'un autre – le Kaf ha'Haïm ajoute qu'il semble pourtant qu'il y a lieu de la compléter après la guérison, pour que la Torah de son Chnayim mikra ne monte pas au ciel incomplète cette année-là ; l'aveugle est dispensé, car ce qui est écrit ne se dit pas par cœur, et il n'a pas à écouter un autre – c'est le strict droit, ajoute-t-il, mais celui qui est plus strict et écoute la lecture d'autrui est digne de bénédiction, et c'est ce qu'il convient de faire ; celui qui ne sait pas lire est dispensé lui aussi et n'a pas à écouter un autre. Le Kitsour Yalkout Yossef écrit autrement : même celui qui a mal aux yeux et souffre en lisant doit lire, ou écouter la paracha d'un autre en pensant à s'acquitter ; certains disent que l'aveugle est tenu lui aussi, chaque Chabbat, comme celui qui voit, et il lui faut donc écouter la lecture d'un autre, qui pense à l'acquitter tandis que lui-même pense à s'acquitter ; de même celui qui est devenu muet et ne peut ni parler ni lire écoute la lecture d'un autre.",
            "The sick, the blind, one who cannot read. The Kaf HaChaim reports, in the name of the Radbaz as cited by the Machazik Berachah: a sick person and one with eye pain are exempt and need not hear the reading from another – the Kaf HaChaim adds that it nevertheless seems one should make it up after recovering, so that the Torah of one's Shnayim mikra does not ascend to heaven incomplete that year; a blind person is exempt, since what is written may not be said by heart, and need not hear it from another – that is the strict law, he adds, but one who is stringent and hears it from others is to be blessed, and this is the proper thing to do; one who does not know how to read is likewise exempt and need not hear it from another. The Kitzur Yalkut Yosef writes otherwise: even one whose eyes are ailing and who suffers when reading must read, or hear the parasha from another with the intention of fulfilling his obligation; some say that a blind person, too, is obligated every Shabbat like a sighted one, and must therefore hear the reading from another, who intends to discharge him while he himself intends to fulfil his obligation; likewise one who has become mute and can neither speak nor read listens to another's reading."),
        H("tous", [
            R("kav", "azoulay2", cite='''ומחנכים גם את הקטנים לקרוא הפרשה כאמור'''),
            R("kyy", 14, cite='''וחובה קדושה על ההורים והמלמדים ללמד את בני ישראל בטעמי המקרא, כדי שיקראו שנים מקרא ואחד תרגום בניגון כדת וכדין'''),
            R("hid", "331141", passage='''תקרא כל יום קצת וכך עד שבת תסיים את הפרשה'''),
        ],
            "Les enfants. Le Rav Ochri Azoulay (Kav haHalakha haSefaradi) conclut son exposé de l'obligation en écrivant qu'on éduque aussi les enfants à lire la paracha de cette façon. Le Kitsour Yalkout Yossef fait un devoir sacré aux parents et aux maîtres d'enseigner les te'amim aux enfants d'Israël, pour qu'ils lisent Chnayim mikra avec la mélodie, comme il se doit. À un garçon de treize ans qui disait ne pas y arriver et demandait un texte plus court, le Rav Binyamin Chmouéli (Hidabroot) a répondu de lire un peu chaque jour : ainsi, d'ici Chabbat, il aura achevé la paracha.",
            "Children. Rav Oshri Azoulay (Kav HaHalacha HaSefaradi) ends his account of the obligation by writing that children too are trained to read the parasha in this way. The Kitzur Yalkut Yosef lays a sacred duty on parents and teachers to teach the te'amim to the children of Israel, so that they read Shnayim mikra with the melody, as is proper. To a thirteen-year-old boy who said he could not manage and asked for something shorter, Rav Binyamin Shmueli (Hidabroot) answered that he should read a little each day: that way he will have finished the parasha by Shabbat."),
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
            R("sht", 1, cite='''עיין בה"ט שכתב שמצוה לקרות אחר חצות וכתב בק"א למח"ב שיש שכתבו כן בשם גורי האר"י זצ"ל ואין האמת כן כי בסדר הכוונות שסידר מהר"ש וויטל מכת"י מר אביו מהרח"ו כתב שרבינו האר"י זצ"ל יום הששי תיכף ומיד אחר תפלת שחרית היה הולך למקום שיש ס"ת וקר' שמו"ת'''),
        ],
            "Le Kitsour Choul'han Aroukh écrit que le mieux est de lire la paracha la veille de Chabbat, après midi ('hatsot). La Michna Beroura rapporte que plusieurs A'haronim placent le meilleur moment la veille de Chabbat, mais que, selon le Maté Yehouda, celui qui lit dès le début de la semaine accomplit lui aussi la mitsva de la meilleure façon. Elle renvoie aux Cha'arei Techouva, qui rapportent du Ma'hazik Berakha, à propos de la lecture « après midi », que certains l'ont écrit au nom des disciples du Ari, mais que « ce n'est pas la vérité » : le Ari allait, le vendredi, aussitôt après la prière du matin, là où il y avait un séfer Torah, et y lisait Chnayim mikra.",
            "The Kitzur Shulchan Aruch writes that it is best to read the parasha on Friday, after midday (chatzot). The Mishnah Berurah reports that several Acharonim hold Friday to be the best time, but that according to the Mateh Yehudah one who reads from the beginning of the week also fulfils the mitzvah in the best way. It refers to the Sha'arei Teshuvah, which reports from the Machazik Berachah, about reading “after midday”, that some wrote so in the name of the Ari's disciples, but that “this is not the truth”: the Ari would go on Friday, right after the morning prayer, to a place where there was a Torah scroll, and read Shnayim mikra."),
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
            "It is best to finish the parasha before eating on Shabbat; if not, one finishes it after the meal, until Minchah. Some allow, after the fact, finishing it until Wednesday – that is, during the first three days of the week, which still belong somewhat to the past Shabbat, the Mishnah Berurah explains –, others until Shemini Atzeret – that is, the Rema specifies, until Simchat Torah, when the congregation completes the Torah. According to this last view, one who missed a week may still make it up until then; he then reads it with the targum, not the text alone (Mishnah Berurah), and the Kaf HaChaim cites Abudarham: it is good to make it up during the ten days of repentance. Rav Binyamin Shmueli (Hidabroot) sums up: after the fact one may still make it up on Sunday, and according to many opinions until Tuesday; after the fact, one makes it up until Simchat Torah. Rav Binyamin Chota (Kikar HaShabbat) specifies that this last deadline ends at the Torah reading in the synagogue on Simchat Torah: one who still owes parashiyot completes them during the preceding night, and if he remembers only in the morning, he prays at a later service so as to finish them before the reading."),
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
              passage='''מלבד בליל שישי כיון שיום שישי מכין לשבת [...] ולכן להלכה, אפשר לקרוא ב' מקרא [...] יש להורות לו לכתחילה שיכול לקרוא אף ללא מפרשים'''),
            R("malka", "142", cite='ותו דיותר נכון לקרא שמו"ת ביום ולא בלילה'),
            R("hid", "303250", cite="אין קוראים מתחילת הלילה עד חצות"),
            R("hy", "1660q", passage='''בליל שבת, מותר לקרוא מקרא בלילה [...] נכון שלא לקרוא מקרא, עד חצות הלילה'''),
        ],
            "La nuit. Le Kitsour Yalkout Yossef permet à qui manque de temps de lire Chnayim mikra la nuit du Chabbat (le vendredi soir), ainsi qu'à celui qui étudie la Torah en écrivant des 'hidouchim et des décisions de halakha. Le Kaf ha'Haïm rapporte, d'après le Ma'hazik Berakha et les Cha'arei Techouva, qu'on ne lit pas Chnayim mikra à la fin de la nuit de jeudi à vendredi, avant qu'il fasse jour, parce que les disciples du Ari ont écrit qu'on ne lit pas le targoum la nuit. Le Rav Ochri Azoulay (Kav haHalakha haSefaradi) traite d'une autre règle, rapportée au nom du Ari : ne pas lire la Torah écrite la nuit (sauf, selon le Ari, la nuit de jeudi à vendredi). Il écrit qu'elle relève de la Kabbale, alors que selon le sens simple rien n'empêche d'étudier la Torah écrite la nuit ; il conclut qu'on peut lire Chnayim mikra la nuit en y joignant un peu de commentaire, comme Rachi, et qu'à celui qui, sinon, n'étudierait pas et qui ne sait pas étudier Rachi ou un autre commentateur, on indique, même a priori, qu'il peut lire sans commentaire : mieux vaut lire le texte la nuit que rester sans étude. Le Rav Menaché Moreno (beit hora'a « Halakha lema'assé » du Rav Ofir Malka), interrogé sur Vezot haBerakha lue dans le Tikoun, ajoute qu'il est plus juste de lire Chnayim mikra le jour que la nuit, en renvoyant au Ma'hazik Berakha et au Kaf ha'Haïm ; et le Rav Binyamin Chmouéli (Hidabroot) écrit qu'on ne lit pas depuis le début de la nuit jusqu'à 'hatsot (le milieu de la nuit). Halacha Yomit répond : la nuit de Chabbat, il est permis de lire le texte la nuit ; les nuits de semaine, il convient de ne pas le lire avant 'hatsot.",
            "At night. The Kitzur Yalkut Yosef allows one who is short of time to read Shnayim mikra on Friday night, as well as one who studies Torah while writing chiddushim and halachic rulings. The Kaf HaChaim reports, following the Machazik Berachah and the Sha'arei Teshuvah, that one does not read Shnayim mikra at the end of Thursday night, before daybreak, because the Ari’s disciples wrote that the targum is not read at night. Rav Oshri Azoulay (Kav HaHalacha HaSefaradi) deals with another rule, reported in the name of the Ari: not to read the Written Torah at night (except, according to the Ari, on Thursday night). He writes that it belongs to Kabbalah, whereas according to the plain meaning nothing prevents studying the Written Torah at night; he concludes that one may read Shnayim mikra at night while adding a little commentary such as Rashi, and that one who would otherwise not study, and who does not know how to study Rashi or another commentator, is told, even in the first place, that he may read without commentary: better to read Scripture at night than to go without study. Rav Menashe Moreno (the “Halacha LeMaaseh” beit hora’ah of Rav Ofir Malka), asked about Vezot HaBerachah read in the Tikkun, adds that it is more correct to read Shnayim mikra by day than by night, referring to the Machazik Berachah and the Kaf HaChaim; and Rav Binyamin Shmueli (Hidabroot) writes that one does not read from nightfall until chatzot (halachic midnight). Halacha Yomit answers: on Friday night it is permitted to read Scripture at night; on weeknights it is proper not to read it before chatzot."),
        H("ashkenaze", [
            R("mb", 10, cite='''דממנחה ולמעלה מתחילין הצבור לקרות פרשת שבוע הבא'''),
            R("bh", 4, cite='''המגן אברהם הביא דעות דמספר הכונות משמע דלכתחלה ישלים בע"ש ורק כשהיה אנוס ישלים בשבת ובב"י ומגיד מישרים משמע דלכתחלה יתחיל בע"ש וישלים בשבת'''),
            R("bh", 4, cite='''ומה שצוה רבי שיגמרו הפרשה קודם הסעודה הוא רק משום דחייש דלמא אגב רוב סעודת שבת משתמיט ולא יגמור'''),
            R("ha", 9, cite='''ולכתחלה ישלים בע"ש ועכ"פ לא יאכל בשבת שחרית עד שישלים'''),
            R("ahs", 9, cite='''ומתבאר מדבריו שאין הידור להשלים קודם קריאת התורה, רק קודם אכילה'''),
            R("ahs", 9, cite='''וגם מבואר מדבריו דכשמשלים בערב שבת – אין זה מצוה מן המובחר. וכן כתב המרדכי פרק קמא דברכות, דדווקא בשבת בבוקר קודם אכילה'''),
            R("ahs", 10, cite='''אבל יש שכתבו דעיקר ההידור הוא בערב שבת; יש אומרים קודם חצות, ויש אומרים אחר חצות'''),
            R("ahs", 10, cite='''ויש אומרים דמצוה מן המובחר לקרא כל יום מעט, ובערב שבת להשלימה, כמו שנדפס בספר חוק לישראל'''),
        ],
            "« Jusqu'à Min'ha » : parce qu'à partir de Min'ha la communauté commence à lire la paracha de la semaine suivante (Michna Beroura). Le Béour Halakha explique, d'après le Or Zaroua, que Rabbi n'a demandé d'achever la paracha avant le repas que par crainte qu'entraîné par le grand repas du Chabbat on ne s'y dérobe et ne l'achève pas ; il rapporte aussi les avis cités par le Maguen Avraham : il ressort du Séfer haKavanot qu'on achève a priori la veille de Chabbat, et le Chabbat seulement si l'on a été empêché ; il ressort du Beit Yossef et du Maguid Mécharim qu'on commence a priori la veille et qu'on achève le Chabbat. Le 'Hayé Adam écrit : a priori on achève la veille de Chabbat, et en tout cas on ne mange pas le Chabbat matin avant d'avoir achevé. L'Aroukh haChoul'han déduit du Tour qu'il n'y a pas de mérite particulier à achever avant la lecture de la Torah, mais seulement avant le repas, et qu'achever la veille de Chabbat n'est pas la meilleure façon – ainsi écrit le Mordekhaï : précisément le Chabbat matin, avant de manger ; il rapporte ensuite que d'autres ont écrit que l'essentiel du mérite est la veille de Chabbat, les uns disant avant midi, les autres après midi, et l'avis pour qui le mieux est de lire un peu chaque jour et d'achever la veille de Chabbat, comme c'est imprimé dans le 'Hok leIsraël.",
            "“Until Minchah”: because from Minchah on the congregation begins to read the next week's parasha (Mishnah Berurah). The Beur Halacha explains, following the Or Zarua, that Rabbi asked that the parasha be finished before the meal only out of concern that, carried along by the large Shabbat meal, one might slip out of it and not finish; it also reports the views quoted by the Magen Avraham: Sefer HaKavanot implies that one finishes on Friday in the first place, and on Shabbat only if prevented; the Beit Yosef and the Maggid Mesharim imply that one begins on Friday in the first place and finishes on Shabbat. The Chayei Adam writes: in the first place one finishes on Friday, and in any case one does not eat on Shabbat morning before finishing. The Aruch HaShulchan infers from the Tur that there is no particular merit in finishing before the Torah reading, only before the meal, and that finishing on Friday is not the best way – so too writes the Mordechai: specifically on Shabbat morning, before eating; he then reports that others wrote that the main merit is on Friday, some saying before midday and some after midday, and the view that it is best to read a little each day and finish on Friday, as printed in Chok LeYisrael."),
        H("sefarade", [
            R("kh", 26, cite='''ומשמע לפי סברה זאת דיש ג' חלוקות מצוה מן המובחר קודם אכילה ובדיעבד גם אחר אכילה מהני קודם מנחה אבל אחר מנחה לא מהני וכן דעת הש"ע שסתם כן כסברה א\''''),
            R("kh", 26, cite='''ונראה ברור דגם לסברה ג' אינו מועיל אלא יום ש"ע אבל יום ש"ת שהתחילו פ' בראשית לא מהני לכ"ע'''),
            R("kh", 26, cite='''ומ"ש מור"ם ז"ל בהגה דהיינו בש"ת וכו' לא בא להוסיף יום ש"ת מלבד ש"ע אלא בא להודיענו הטעם והוא שאז משלימין הצבור ור"ל יקרא עם הצבור ואנה"נ דביום ש"ת לא מהני אלא קודם קריאת פ' בראשית. מט"י או' ד\''''),
            R("kh", 28, cite='''והיינו אם לא השלים ביום ג' דיעבד יש להשלימה כל השנה עד שמיני עצרת בא"י ולדידן בשמחת תורה מיקרי שפיר משלים עם הצבור ומכאן ואילך עבר זמנו. א"א או' ז\''''),
            R("kh", 29, cite='''וכל עוד שלא גמרו הצבור וזאת הברכה מיקרי זמנה כמ"ש לעיל או' כ"ו'''),
        ],
            "Jusqu'à quand, précisément. Le Kaf ha'Haïm relève, au nom du Maté Yehouda, trois degrés selon le premier avis : le mieux, avant le repas ; a posteriori, après le repas, avant Min'ha ; après Min'ha, cela ne vaut plus – et tel est l'avis du Choul'han Aroukh, qui énonce cet avis en premier, sans le nommer. Toujours d'après le Maté Yehouda, il paraît clair que, même selon le troisième avis (jusqu'à Chemini Atseret), cela ne vaut que jusqu'au jour de Chemini Atseret : le jour de Sim'hat Torah, une fois commencée la paracha Beréchit, cela ne vaut plus pour personne ; le Rema ne veut pas ajouter un jour mais donner la raison – la communauté achève alors –, et à Sim'hat Torah cela ne vaut qu'avant la lecture de Beréchit. Le Kaf ha'Haïm rapporte de l'Échel Avraham (Pri Megadim) : pour celui qui n'a pas achevé jusqu'au mardi, il y a lieu, a posteriori, de rattraper toute l'année, jusqu'à Chemini Atseret en terre d'Israël ; et « pour nous », à Sim'hat Torah, cela s'appelle encore achever avec la communauté ; passé ce moment, le temps est révolu. Et à propos de Vezot haBerakha, il ajoute que tant que la communauté ne l'a pas achevée, c'est encore son temps, comme il l'a écrit plus haut (§26).",
            "Until when, exactly. The Kaf HaChaim notes, in the name of the Mateh Yehudah, three levels according to the first view: best, before the meal; after the fact, after the meal, before Minchah; after Minchah it no longer counts – and such is the view of the Shulchan Aruch, which states this view first, unattributed. Still following the Mateh Yehudah, it seems clear that, even according to the third view (until Shemini Atzeret), it counts only up to the day of Shemini Atzeret: on Simchat Torah, once parashat Bereshit has been begun, it no longer counts according to anyone; the Rema does not mean to add a day but to give the reason – the congregation completes then –, and on Simchat Torah it counts only before the reading of Bereshit. The Kaf HaChaim reports from the Eshel Avraham (Pri Megadim): one who did not finish by Tuesday should, after the fact, make it up all year, until Shemini Atzeret in the Land of Israel; and “for us”, on Simchat Torah it still counts as completing with the congregation; after that the time has passed. And regarding Vezot HaBerachah he adds that as long as the congregation has not completed it, it is still its time, as he wrote above (§26)."),
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
            R("bht", 1, cite='''ויקוץ הצפרנים קודם שמו"ת. ועיקר המצוה לקרות אחר חצות ואחר שקרא ילך לבית המרחץ ויטבול. הכוונות'''),
            R("sht", 1, cite='''עיין בה"ט שכתב שמצוה לקרות אחר חצות וכתב בק"א למח"ב שיש שכתבו כן בשם גורי האר"י זצ"ל ואין האמת כן כי בסדר הכוונות שסידר מהר"ש וויטל מכת"י מר אביו מהרח"ו כתב שרבינו האר"י זצ"ל יום הששי תיכף ומיד אחר תפלת שחרית היה הולך למקום שיש ס"ת וקר' שמו"ת'''),
            R("er", (260, 4), cite='''ומי שקורא שנים מקרא ואחד תרגום בערב שבת יטבול קודם שיקרא (של"ה)'''),
            R("ahs", 7, cite='''ויש מי שכתב דאם בקי בטעמים – יקרא בספר תורה, ויטבול אחר הקריאה, ויקוץ הצפרנים קודם הקריאה (מגן אברהם שם). וזהו ממדת חסידות, ולהקוראים אותה כולה בערב שבת'''),
            R("kh", 38, cite='''ובענין קציצת הצפרנים והטבילה וכוונתה כבר כתבנו לעיל סי' ר"ס קחנו משם'''),
            R("hid", "298335", passage='''אלא אם יטבול שעה קודם חצות היום ואילך [...] ואחר תפילת שחרית'''),
            R("malka", "520", passage='''העיקר לפי דעת האר"י הוא לטבול לאחר שסיים את קריאת שמו"ת [...] ויכול לטבול גם לפי האר"י [...] דעדיף טפי'''),
        ],
            "Ongles et mikvé. Le Maguen Avraham rapporte qu'on s'immerge après la lecture, d'après le Séfer haKavanot – en ajoutant : « je n'ai pas affaire ici aux choses cachées » –, et qu'on se coupe les ongles avant la lecture, d'après le Chla. Le Baèr Hétev de même, au nom du Séfer haKavanot : les ongles avant Chnayim mikra ; l'essentiel de la mitsva est de lire après midi ; et après avoir lu, on va au bain et l'on s'immerge. Sur ce « après midi », les Cha'arei Techouva rapportent du Ma'hazik Berakha que certains l'ont écrit au nom des disciples du Ari, mais que « ce n'est pas la vérité » : d'après l'ordre des Kavanot établi par Rabbi Chmouel Vital sur le manuscrit de son père, Rabbi 'Haïm Vital, le Ari allait, le vendredi, aussitôt après la prière du matin, là où il y avait un séfer Torah, et y lisait Chnayim mikra. Pour l'immersion, l'Eliya Rabba rapporte à l'inverse, au nom du Chla, que celui qui lit Chnayim mikra la veille de Chabbat s'immerge avant de lire. L'Aroukh haChoul'han, qui cite ces mots du Maguen Avraham (s'immerger après la lecture, se couper les ongles avant), précise que c'est là une conduite de piété, pour ceux qui lisent toute la paracha la veille de Chabbat. Le Kaf ha'Haïm renvoie, pour les ongles et l'immersion, à ce qu'il en a écrit au siman 260. Le Rav Hillel Meirs (Hidabroot), répondant à qui avait entendu dire qu'en lisant le vendredi matin on peut s'immerger avant midi, confirme que l'immersion en l'honneur du Chabbat ne vaut qu'à partir d'une heure avant midi, ou bien après avoir lu la paracha Chnayim mikra et après la prière du matin (il renvoie au Chivat Tsion). Le Rav Emmanuel Molkandov (beit hora'a « Halakha lema'assé » du Rav Ofir Malka), à qui l'on demandait si celui qui a lu pendant la semaine peut aller au mikvé dès le vendredi matin, répond que l'essentiel, selon le Ari, est de s'immerger après avoir achevé Chnayim mikra, le moment de la lecture n'y étant guère lié : celui qui a pour règle de lire pendant la semaine, et le fait, a pour sa part achevé sa lecture et peut s'immerger, même selon le Ari – d'autant mieux s'il garde quelques versets pour le vendredi.",
            "Nails and mikveh. The Magen Avraham reports that one immerses after the reading, according to Sefer HaKavanot – adding: “I have no business here with hidden matters” –, and that one cuts one's nails before the reading, according to the Shelah. The Ba'er Hetev likewise, in the name of Sefer HaKavanot: nails before Shnayim mikra; the main mitzvah is to read after midday; and after reading one goes to the bathhouse and immerses. On this “after midday”, the Sha'arei Teshuvah reports from the Machazik Berachah that some wrote so in the name of the Ari's disciples, but that “this is not the truth”: according to the order of the Kavanot arranged by Rabbi Shmuel Vital from the manuscript of his father, Rabbi Chaim Vital, the Ari would go on Friday, right after the morning prayer, to a place where there was a Torah scroll, and read Shnayim mikra. As for immersion, the Eliyah Rabbah reports on the contrary, in the name of the Shelah, that one who reads Shnayim mikra on Friday immerses before reading. The Aruch HaShulchan, quoting these words of the Magen Avraham (immersing after the reading, cutting one's nails before it), specifies that this is a pious practice, for those who read the whole parasha on Friday. The Kaf HaChaim refers, for nails and immersion, to what he wrote about them in siman 260. Rav Hillel Meirs (Hidabroot), answering someone who had heard that one who reads on Friday morning may immerse before midday, confirms that immersion in honour of Shabbat counts only from one hour before midday, or else after reading the parasha Shnayim mikra and after the morning prayer (he refers to the Shivat Tzion). Rav Emmanuel Molkandov (Rav Ofir Malka's “Halacha LeMaaseh” beit hora'ah), asked whether one who read during the week may go to the mikveh already on Friday morning, answers that the main point, according to the Ari, is to immerse after finishing Shnayim mikra, the time of the reading having little to do with it: one whose rule is to read during the week, and who does so, has for his part finished his reading and may immerse, even according to the Ari – all the better if he keeps a few verses for Friday."),
        H("tous", [
            R("sahr", 5, cite='''שלא יקרא בשבוע זה פרשת שבוע אחר'''),
            R("ahs", 1, cite='''אבל אין לו להקדים לפני שבוע זו'''),
            R("hid", "286915", cite='''עד שהוא עצמו יתפלל מנחה''', passage='''אפשר להתחיל לקרוא רק אחרי מנחה של שבת [...] עד שהוא עצמו יתפלל מנחה'''),
            R("hid", "235423", passage='''אי אפשר לקרוא עכשיו שניים מקרא ואחד תרגום של פרשת בראשית [...] רק אחרי שיתחילו לקרוא את פרשת בראשית בשמחת תורה'''),
        ],
            "Pas avant sa semaine. On ne devance pas : on ne lit pas cette semaine la paracha d'une autre semaine (Choul'han Aroukh haRav ; Aroukh haChoul'han). Le Rav Hillel Meirs (Hidabroot) répond qu'on ne peut commencer la paracha suivante qu'après Min'ha du Chabbat, et rapporte au nom du Rav 'Haïm Kanievsky que, même l'heure de Min'ha venue, il semble qu'on ne puisse commencer tant qu'on n'a pas soi-même prié Min'ha. De même, à la mi-Tichri, on ne peut pas encore lire Beréchit : la prochaine paracha lue est Vezot haBerakha, et c'est seulement quand on aura commencé à lire Beréchit, à Sim'hat Torah, qu'on pourra la commencer (Rav Hillel Meirs, qui renvoie au 'Hout Chani).",
            "Not before its week. One does not anticipate: one does not read this week the parasha of another week (Shulchan Aruch HaRav; Aruch HaShulchan). Rav Hillel Meirs (Hidabroot) answers that the next parasha may be begun only after Minchah of Shabbat, and reports in the name of Rav Chaim Kanievsky that even once the time of Minchah has come, it seems one may not begin until one has oneself prayed Minchah. Likewise, in mid-Tishrei one cannot yet read Bereshit: the next parasha to be read is Vezot HaBerachah, and only once Bereshit has been begun, on Simchat Torah, may one begin it (Rav Hillel Meirs, referring to the Chut Shani)."),
        H("sefarade", [
            R("ryd", "351", passage='''begins from Minchah on Shabbat [...] read it on Friday morning [...] reading on Thursday is not ideal [...] on any of the preceding weekdays'''),
            R("ryd", "323", passage='''there are no makeup readings [...] wrote this in the book Halachah Berurah [...] whoever has not read has lost out'''),
        ],
            "Le Rav David Yossef, Richon leTsion et auteur de Halakha Beroura, dans ses cours hebdomadaires (lus ici dans leur traduction anglaise ; le siman 285 de son livre n'est pas en ligne et n'a pas pu être lu). Il ressort du Choul'han Aroukh, dit-il, que le temps de la lecture commence à Min'ha du Chabbat précédent ; on peut aussi commencer le dimanche et répartir la lecture sur la semaine. Selon les kabbalistes, il importe en temps normal de lire le vendredi – non pas après midi, comme certains l'ont compris, mais le vendredi matin, comme l'écrit le 'Hida : le Ari lisait aussitôt après Cha'harit, avec talith et tefilines, et le Chabbat seulement s'il n'avait pas pu. Le 'Hida écrit qu'on peut lire aussi le jeudi ; selon le Ari ce n'est pas l'idéal, l'essentiel étant de lire près du Chabbat, mais nous suivons la décision de Maran (285:3) : n'importe quel jour de la semaine qui précède. Quant à la fin du temps : à bien lire le Choul'han Aroukh (285:4), dit-il, l'avis de Maran en pratique est qu'il n'y a pas de rattrapage ; on lit jusqu'à l'heure de Min'ha guedola du Chabbat. Certains décisionnaires récents comptent jusqu'à la Min'ha que l'on prie soi-même ; le Rav David Yossef pense autrement, et dit l'avoir écrit, preuves à l'appui, dans Halakha Beroura : une fois venue l'heure de Min'ha guedola, celui qui n'a pas lu a manqué la lecture ; on veille donc à finir avant.",
            "Rav David Yosef, Rishon LeTzion and author of Halacha Berurah, in his weekly shiurim (read here in their English translation; siman 285 of his book is not available online and could not be read). He says the Shulchan Aruch implies that the time for reading starts at Minchah of the previous Shabbat; one may equally start on Sunday and spread the reading over the week. According to the kabbalists it matters, ordinarily, to read on Friday – not after midday, as some understood, but on Friday morning, as the Chida writes: the Ari read right after Shacharit, in tallit and tefillin, and on Shabbat only if he had been unable to. The Chida writes that Thursday is also possible; for the Ari that is not ideal, the main thing being to read close to Shabbat, but we follow Maran's ruling (285:3): any weekday of the week before. As for the end of the time: on a careful reading of the Shulchan Aruch (285:4), he says, Maran's view in practice is that there is no making up; one reads up to the time of Minchah Gedolah on Shabbat. Some recent authorities count until the Minchah one actually prays; Rav David Yosef thinks otherwise, and says he wrote so, with proofs, in Halacha Berurah: once Minchah Gedolah time has come, one who has not yet read has missed it; so one must take care to finish before then."),
        H("tous", [
            R("hid", "203590", cite='''וכן פרשה אחת מתחילת התורה''', passage='''ניתן להשלים בדיעבד עד שמחת תורה את כל הפרשיות שלא קראת עדיין [...] וכן פרשה אחת מתחילת התורה'''),
        ],
            "À celui qui découvre l'obligation en cours d'année, le Rav Binyamin Chmouéli (Hidabroot) répond qu'a posteriori on peut compléter, jusqu'à Sim'hat Torah, toutes les parachiot qu'on n'a pas encore lues ; il conseille de lire chaque semaine la paracha de la semaine et, en plus, une paracha depuis le début de la Torah, de façon à avoir tout achevé à Sim'hat Torah.",
            "To one who discovers the obligation in the course of the year, Rav Binyamin Shmueli (Hidabroot) answers that after the fact one may make up, until Simchat Torah, all the parashiyot not yet read; he advises reading each week the parasha of the week and, in addition, one parasha from the beginning of the Torah, so as to have completed everything by Simchat Torah."),
        H("sefarade", [
            R("hy", "1660q", passage='''צריך שנים מקרא ואחד תרגום במשך השבוע. פעם אחת. [...] ולא צריך לקרוא מפטיר'''),
            R("hy", "1660q", passage='''מותר לעשות כך. יכול אפילו לקרוא כל הפרשה ביום ראשון'''),
            R("hy", "1660q", passage='''אחרי ברכות התורה, אפשר.'''),
        ],
            "Quelques réponses de Halacha Yomit. On lit Chnayim mikra une fois dans la semaine ; il n'y a pas à recommencer le vendredi. Il n'est pas nécessaire de répéter une troisième fois la fin de la septième montée, ni de lire le maftir, sauf quand on lit avec l'officiant à la synagogue. On peut répartir la lecture par montées, selon le temps dont on dispose, et même lire toute la paracha le dimanche. On peut lire avant la prière du matin, après les bénédictions de la Torah.",
            "Some answers from Halacha Yomit. Shnayim mikra is read once during the week; there is no need to start again on Friday. There is no need to repeat a third time the end of the seventh aliyah, nor to read the maftir, except when reading along with the reader in the synagogue. One may divide the reading by aliyot, as time allows, and may even read the whole parasha on Sunday. One may read before the morning prayer, after the blessings over the Torah."),
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
            "Verse by verse, or section by section? The Mishnah Berurah reports both views: read each verse twice and then its targum, or each section (open or closed) twice and then its targum; the Magen Avraham and the Sha'arei Teshuvah lean to the first, the Vilna Gaon said the targum after each section, or wherever the subject pauses more clearly, and one may follow either way. The Kitzur Shulchan Aruch adopts reading by section, following the Vilna Gaon, stopping at the end of the section even in the middle of a verse. The Shulchan Aruch HaRav considers reading verse by verse more correct, while noting that by law one may read in whatever way one wishes."),
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
            R("mbe", 130, cite='''יקרא כל פסוק שנים מקרא ואחד תרגום ולא כמי שנהג ללמוד כל פרשה מפרשיות קטנות כלה שנים מקרא ואח״כ קוראה תרגום. וכ״ש שלא ילמוד כל פרשת השבוע כולה שנים מקרא ואח״כ יקראנה כלה תרגום. לא אריך למעבד הכי'''),
            R("hid", "255408", passage='''יש שתי אפשרויות לקרוא שניים מקרא ואחד תרגום [...] ורק אחר כך לקרוא את התרגום'''),
            R("hid", "27340", passage='''ויש נוהגים להעביר את כל הסידרה כולה [...] ואם לא ידוע לך תנהג איך שתבחר'''),
            R("hy", "1659", passage='''ולכתחילה יש לקרוא כל פסוק ופסוק שתי פעמים [...] קרא את כל התרגום, יצא ידי חובתו'''),
            R("ryd", "351", passage='''entire parashah a second time, and then the Targum'''),
        ],
            "Lire toute la paracha une fois, puis une seconde fois, puis tout le targoum ? L'Aroukh haChoul'han rapporte que certains font ainsi, y voit un certain appui dans les mots de Rachi, et conclut qu'à son humble avis rien n'est ici impératif : on peut faire comme on veut, chaque façon a un fondement dans la halakha, et peut-être même tantôt d'une façon, tantôt d'une autre – s'il fallait absolument faire d'une seule façon, les Richonim ne se seraient pas tus. À l'inverse, le Kaf ha'Haïm rapporte du Cha'ar haKavanot que le Ari ne faisait pas comme ceux qui se piquent de lire toute la paracha une fois, de la répéter, puis de lire tout le targoum d'un coup : il lisait chaque verset à part, deux fois puis son targoum. Et le 'Hida (Moré beEtsba) demande de lire chaque verset deux fois puis son targoum, non comme celui qui a pris l'usage d'étudier chaque petite section tout entière deux fois avant d'en lire le targoum, et à plus forte raison de ne pas étudier toute la paracha de la semaine deux fois pour lire ensuite tout le targoum : « il ne convient pas de faire ainsi ». Parmi les réponses d'aujourd'hui : le Rav Hillel Meirs (Hidabroot) écrit qu'on ne peut pas lire toute la paracha du début à la fin et ne lire le targoum qu'ensuite ; le Rav Binyamin Chmouéli (Hidabroot) compte au contraire trois usages – verset par verset, section par section, ou toute la sidra deux fois puis le targoum – et dit de suivre celui de ses pères ou, si on ne le connaît pas, celui que l'on choisit. Halacha Yomit : a priori chaque verset deux fois, puis son targoum ; mais celui qui a lu toute la paracha, l'a relue, puis a lu tout le targoum est quitte. Le Rav David Yossef raconte que son père, le Rav Ovadia Yossef, relisait après la prière toute la paracha une seconde fois, puis le targoum, et non verset par verset.",
            "Reading the whole parasha once, then a second time, then the whole targum? The Aruch HaShulchan reports that some do so, sees some support for it in Rashi's wording, and concludes that in his humble opinion nothing here is imperative: one may do as one wishes, each way has a basis in halachah, and perhaps even sometimes one way and sometimes another – had one way been required, the Rishonim would not have kept silent. Conversely, the Kaf HaChaim reports from Sha'ar HaKavanot that the Ari did not do as those who presume to read the whole parasha once, repeat it, and then read the whole targum together: he read each verse by itself, twice and then its targum. And the Chida (Moreh BeEtzba) says to read each verse twice and then its targum, unlike one whose practice is to study each small section in full twice and then read its targum, and all the more so not to study the whole weekly parasha twice and then read the whole targum: “it is not fitting to do so”. Among today's answers: Rav Hillel Meirs (Hidabroot) writes that one cannot read the whole parasha from beginning to end and only then read the targum; Rav Binyamin Shmueli (Hidabroot), on the contrary, lists three customs – verse by verse, section by section, or the whole sidra twice and then the targum – and says to follow that of one's fathers or, if it is not known, whichever one chooses. Halacha Yomit: in the first place each verse twice, then its targum; but one who read the whole parasha, read it again, and then read the whole targum has fulfilled the obligation. Rav David Yosef relates that his father, Rav Ovadia Yosef, would read the whole parasha a second time after prayers, and then the targum, not verse by verse."),
        H("ashkenaze", [
            R("ahs", 4, cite='''ו"פרשה" מקרי פתוחה או סתומה. וזה שמצויין בחומשים "שלישי", "רביעי", וכו' – זה אינו כלום'''),
            R("ahs", 5, cite='''אך לפי זה יש להסתפק כשיש פרשה באמצע פסוק'''),
            R("ahs", 5, cite='''ומכל מקום נראה שיעשה כן. ואי משום "כל פסוקא דלא פסקיה משה לא פסקינן" – הא כאן פסקיה משה. וכן בעשרת הדברות ב"לא תרצח" וגו', שיש פרשה'''),
        ],
            "Pour qui lit section par section, l'Aroukh haChoul'han précise que la « paracha » est la section ouverte ou fermée ; les repères « troisième », « quatrième »… imprimés dans les 'Houmachim n'y comptent pour rien. Quand une section s'achève au milieu d'un verset – il cite « Ce fut après le fléau » (Pin'has), « Les fils de Yaakov étaient douze » (Vayichla'h) et « d'Eilat et d'Etsion Guéver » (Devarim) –, il hésite, puis il lui semble qu'on s'y arrête tout de même : la règle « un verset que Moché n'a pas coupé, nous ne le coupons pas » ne s'y oppose pas, puisqu'ici Moché l'a coupé ; et de même, ajoute-t-il, dans les Dix Paroles, à « Tu ne tueras pas… », où il y a une section.",
            "For one who reads section by section, the Aruch HaShulchan specifies that the “parasha” is the open or closed section; the marks “third”, “fourth”… printed in the Chumashim count for nothing here. When a section ends in the middle of a verse – he cites “It was after the plague” (Pinchas), “The sons of Yaakov were twelve” (Vayishlach) and “from Eilat and Etzion Gever” (Devarim) –, he hesitates, then it seems to him that one stops there all the same: the rule “a verse that Moshe did not divide, we do not divide” is no objection, since here Moshe did divide it; and likewise, he adds, in the Ten Commandments, at “You shall not murder…”, where there is a section break."),
        H("tous", [
            R("bh", (494, 1), cite='''שלענין הקריאה אין מלא תרצח עד לא תחמוד אלא פסוק אחד בלבד דהיינו שאסור להפסיק קריאתו לגמרי בתוך אמצע פסוק זה אפילו כשקורא ביחיד'''),
            R("bh", (494, 1), cite='''וע"כ בשבועות נוהגין לקרות בצבור בהראשון דהיינו בטעם העליון לעשות מכל דיבור פסוק אחד לפי שבו ביום נתנו עשרת הדברות. ובפרשת יתרו ובפרשת ואתחנן קורין אף בצבור בטעם התחתון ויש נוהגין לקרות בצבור לעולם בטעם העליון דהיינו אף בפרשת יתרו ובפרשת ואתחנן רק היחיד הקורא לעצמו קורא בשני'''),
            R("kh", 5, cite='''בקריאת עשרת הדברות צריך ליזהר לקרותם שמו"ת כפי הטעמים של סדר הפסוקים כפי מ"ש הרב משאת בנימין סי' ו\''''),
            R("kh", 5, cite='''אמנם לא תרצח לא תנאף לא תגנוב לא תענה צריך ליזהר לקרותם שנים מקרא בבת אחת ואח"כ אחד תרגום בב"א לפי שכולם פסוק אחד'''),
            R("kh", 5, cite='''ואין לקרות פסוק אחד פסקי פסקי שמו"ת אלא צריך לקרות כל הפסוק שלם תחלה שנים מקרא ואח"כ אחד תרגום. ב"ד סי' קי"א'''),
            R("ahs", 5, cite='''ומכל מקום נראה שיעשה כן. ואי משום "כל פסוקא דלא פסקיה משה לא פסקינן" – הא כאן פסקיה משה. וכן בעשרת הדברות ב"לא תרצח" וגו', שיש פרשה'''),
        ],
            "Les Dix Paroles ont deux cantillations : l'une fait de chaque Parole un seul verset (ta'am 'elyon), l'autre suit le découpage ordinaire des versets (ta'am ta'hton). Le Béour Halakha résume les A'haronim : à Chavouot on lit en public selon la première ; aux parachiot Yitro et Vaet'hanan on lit, même en public, selon la seconde, et certains lisent toujours en public selon la première – seul le particulier qui lit pour lui-même lit alors selon la seconde. Il précise que, pour la lecture, de « Tu ne tueras pas » jusqu'à « Tu ne convoiteras pas » il n'y a qu'un seul verset, au milieu duquel il est interdit de s'arrêter tout à fait, même quand on lit seul. Le Kaf ha'Haïm rapporte de même, du Beit David (siman 111) qui s'appuie sur le Massat Binyamin (siman 6), que, pour Chnayim mikra, il faut veiller à lire les Dix Paroles selon la cantillation de l'ordre des versets ; « Tu ne tueras pas, tu ne commettras pas d'adultère, tu ne voleras pas, tu ne témoigneras pas… » forment un seul verset : il faut veiller à les lire ensemble deux fois, puis leur targoum ensemble. Et l'on ne lit pas un verset par morceaux : on lit d'abord le verset entier deux fois, puis son targoum. L'Aroukh haChoul'han, pour qui lit section par section, écrit à l'inverse qu'on s'arrête à la fin d'une section même au milieu d'un verset, et de même, dans les Dix Paroles, à « Tu ne tueras pas… », où il y a une section.",
            "The Ten Commandments have two cantillations: one makes each commandment a single verse (ta'am elyon), the other follows the ordinary division into verses (ta'am tachton). The Beur Halacha sums up the Acharonim: on Shavuot the public reading follows the first; in parashiyot Yitro and Va'etchanan one reads, even in public, according to the second, and some always read in public according to the first – only the individual reading for himself then reads according to the second. It specifies that, for reading purposes, from “You shall not murder” up to “You shall not covet” there is only one verse, in the middle of which one may not stop altogether, even when reading alone. The Kaf HaChaim likewise reports, from the Beit David (siman 111), who relies on the Mas'at Binyamin (siman 6), that for Shnayim mikra one must take care to read the Ten Commandments with the cantillation of the order of the verses; “You shall not murder, you shall not commit adultery, you shall not steal, you shall not bear [false] witness…” form a single verse: one must take care to read them together twice, then their targum together. And a verse is not read piecemeal: one first reads the whole verse twice, then its targum. The Aruch HaShulchan, for one who reads section by section, writes on the contrary that one stops at the end of a section even in mid-verse, and likewise, in the Ten Commandments, at “You shall not murder…”, where there is a section break."),
        H("ashkenaze", [
            R("bht", 1, cite='''ואיסור גדול להפסיק בקריאת שמו"ת בדיבור'''),
            R("ma", 11, cite='''וטוב שלא יפסיק כלל בשיחה [כ"ה]'''),
            R("ahs", 7, cite='''ויש מי שכתב שיש איסור להפסיק בדיבור בקריאת שנים מקרא ואחד תרגום (באר היטב סעיף קטן א). ותמיה לומר כן, דבלא ברכה מה שייך הפסק?'''),
            R("ahs", 7, cite='''ואי משום שאין להפסיק בלימוד התורה למילי דעלמא - דאם כן אין זה שייך לקריאת שנים מקרא ואחד תרגום, ומסתמא מפסיק לדבר שצריך. ועוד, דאותם שקורין פרשה בכל יום – הלא מפסיקין הרבה, ולכן אין לזה מקום מדינא'''),
        ],
            "S'interrompre : interdit, ou seulement à éviter ? Le Baèr Hétev écrit que c'est « un grand interdit » de s'interrompre par la parole pendant Chnayim mikra. Le Maguen Avraham, après avoir décrit la haftara et ce qu'on lit ensuite, écrit au nom de la Knesset haGuedola qu'il est bon de ne pas s'interrompre du tout par une conversation. L'Aroukh haChoul'han cite le Baèr Hétev et s'en étonne : là où il n'y a pas de bénédiction, que vient faire la notion d'interruption ? Et si c'est parce qu'on n'interrompt pas l'étude de la Torah pour des propos profanes, cela n'est pas propre à Chnayim mikra, et l'on s'interrompt sans doute pour une chose nécessaire. De plus, ceux qui lisent une section chaque jour s'interrompent beaucoup ; cela n'a donc pas de fondement selon la loi.",
            "Interrupting: forbidden, or merely to be avoided? The Ba'er Hetev writes that it is “a great prohibition” to interrupt Shnayim mikra by speaking. The Magen Avraham, after describing the haftarah and what is read after it, writes in the name of the Knesset HaGedolah that it is good not to interrupt at all with conversation. The Aruch HaShulchan quotes the Ba'er Hetev and wonders at it: where there is no blessing, what place is there for the notion of an interruption? And if it is because Torah study is not to be interrupted for mundane talk, that is not particular to Shnayim mikra, and one presumably does interrupt for something necessary. Moreover, those who read a section each day interrupt a great deal; so this has no basis in law."),
        H("tous", [
            R("sch", 745, cite='''כשמזכירים תלמידי חכמים אין צריך לומר זכרונם לברכה כמו שאין אומרים כשאנו קורין בתורה על משה ועל אהרן זכרונם לטובה'''),
            R("sch", 745, cite='''וכן כשאדם אומר שנים מקרא ואחד תרגום כשמזכיר הצדיקים שנזכר בפסוקים אין צריך לומר ז"ל'''),
        ],
            "Celui qui dit Chnayim mikra n'a pas à ajouter « de mémoire bénie » quand il nomme les justes mentionnés dans les versets, de même qu'on ne le dit pas de Moché et d'Aharon quand on lit la Torah (Séfer 'Hassidim).",
            "One who says Shnayim mikra need not add “of blessed memory” when naming the righteous mentioned in the verses, just as it is not said of Moshe and Aharon when the Torah is read (Sefer Chasidim)."),
        H("tous", [
            R("ahs", 3, cite='''ויש להסתפק: אי בעינן דווקא שנים מקרא מקודם, ואחר כך תרגום, או שיצא כשקרא מקרא ותרגום ומקרא. ומדברי הלבוש מתבאר שכן דעתו'''),
            R("ahs", 3, cite='''הרי שכתב מפורש דהתרגום יכול להיות באמצע'''),
            R("hid", "259534", cite='''בדיעבד יצאת ידי חובה''', passage='''צריך לקרוא שניים מקרא תחילה ורק אח"כ את התרגום [...] בדיעבד יצאת ידי חובה'''),
        ],
            "Texte, targoum, puis texte ? L'Aroukh haChoul'han se demande s'il faut absolument deux fois le texte d'abord, ou si l'on est quitte en lisant le texte, le targoum, puis le texte ; il déduit du Levouch que le targoum peut se trouver au milieu : celui qui lit seul une fois le texte et une fois le targoum, puis lit mot à mot avec l'officiant à la synagogue, a accompli Chnayim mikra véé'had targoum. Le Rav Hillel Meirs (Hidabroot) répond qu'il faut lire d'abord deux fois le texte et ensuite seulement le targoum, mais que celui qui a lu le texte, le targoum, puis de nouveau le texte est quitte a posteriori (il renvoie au Cha'ar haTsiyoun 285:10).",
            "Text, targum, then text? The Aruch HaShulchan asks whether the text must come twice first, or whether one fulfils the obligation by reading text, targum and then text; he infers from the Levush that the targum may come in the middle: one who reads the text once and the targum once by himself, and then reads word for word with the reader in the synagogue, has fulfilled Shnayim mikra ve-echad targum. Rav Hillel Meirs (Hidabroot) answers that one must first read the text twice and only then the targum, but that one who read text, targum and then text again has fulfilled the obligation after the fact (he refers to the Sha'ar HaTziyun 285:10)."),
        H("tous", [
            R("hid", "15646", cite='''יש לעצור באמצע שניים מקרא ואחד תרגום, לענית קדושה וקדיש'''),
            R("hid", "274474", passage='''יש בזה מעלה גדולה בוודאי [...] ובתנאי שלא מפסיקים בדיבור עד סיום קריאת שמו"ת'''),
        ],
            "On s'arrête au milieu de Chnayim mikra pour répondre à la kedoucha et au kaddich (Rav Binyamin Chmouéli, Hidabroot). Étudier Rachi après chaque verset, dans une édition disposée ainsi, a certainement une grande valeur, répond-il aussi, à condition de ne pas s'interrompre par la parole avant la fin de la lecture.",
            "One stops in the middle of Shnayim mikra to answer Kedushah and Kaddish (Rav Binyamin Shmueli, Hidabroot). Studying Rashi after each verse, in an edition laid out that way, certainly has great merit, he also answers, provided one does not interrupt by speaking until the reading is finished."),
        H("tous", [
            R("malka", "564", cite='''אין צורך לחזור מתחלת הפסוק, אלא מתחלת הענין''', passage='''לכתחלה יש לומר בתחלה את הפחות נכון [...] לכתחלה יש לחזור על כל המשפט שיש לו משמעות [...] אלא מתחלת הענין'''),
        ],
            "Si l'on doute de la lecture d'un mot, ou s'il existe deux versions du targoum et qu'on veut dire les deux : le Rav Emmanuel Molkandov (beit hora'a « Halakha lema'assé » du Rav Ofir Malka) rapproche la question de celle de la lecture de la Méguila, où certains répètent des mots dans deux versions, et répond qu'a priori on dit d'abord la version la moins exacte et en dernier la plus exacte ; qu'a priori aussi on répète tout le membre de phrase qui a un sens, et non le mot seul ; et qu'il n'est pas nécessaire de reprendre depuis le début du verset, mais depuis le début du propos.",
            "If one is unsure how to read a word, or there are two versions of the targum and one wishes to say both: Rav Emmanuel Molkandov (Rav Ofir Malka's “Halacha LeMaaseh” beit hora'ah) likens the question to that of the Megillah reading, where some repeat words in two versions, and answers that in the first place one says the less accurate version first and the more accurate one last; that, also in the first place, one repeats the whole meaningful phrase and not the word alone; and that one need not go back to the beginning of the verse, but to the beginning of the phrase."),
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
            R("hy", "1659q", passage='''בכל מקרה צריך לקרוא את התרגום'''),
            R("hy", "1660q", passage='''לדעת רוב הפוסקים אין הדין כן [...] מומלץ מאד להחמיר ולקרוא גם את פירוש רש"י'''),
        ],
            "Même celui qui ne comprend pas bien la langue du targoum doit lire la paracha deux fois dans le texte et une fois dans le targoum, et celui qui craint le Ciel lit aussi Rachi (Kitsour Yalkout Yossef ; de même le Rav Yaron Achkenazi, Kav haHalakha haSefaradi). Le Kaf ha'Haïm rapporte que, pour le Maharchal, celui qui ne peut pas étudier les deux lit Rachi et non le targoum ; mais que, d'après les kabbalistes, on tient au targoum, si bien que celui qui n'a pas le temps d'étudier les deux étudie le targoum (au nom du Birké Yossef et des Cha'arei Techouva). Il ajoute qu'en voyage, celui qui n'a que le texte et Rachi peut s'appuyer sur ceux qui permettent, et lire deux fois le texte et une fois Rachi. Halacha Yomit répond de même : celui qui ne comprend pas le targoum d'Onkelos le lit de toute façon, et apprendra peu à peu à en comprendre la plus grande partie ; Rachi ne dispense pas du targoum, que les Sages ont précisément institué – tel est, écrit la rédaction, l'avis de la plupart des décisionnaires, même si certains disent qu'aujourd'hui on peut lire Rachi –, mais il est très recommandé de lire aussi Rachi.",
            "Even one who does not understand the language of the targum well must read the parasha twice in the text and once in the targum, and one who fears Heaven reads Rashi as well (Kitzur Yalkut Yosef; likewise Rav Yaron Ashkenazi, Kav HaHalacha HaSefaradi). The Kaf HaChaim reports that, for the Maharshal, one who cannot study both reads Rashi and not the targum; but that, according to the kabbalists, the targum is insisted upon, so that one who has no time to study both studies the targum (in the name of the Birkei Yosef and the Sha'arei Teshuvah). He adds that when travelling, one who has only the text and Rashi may rely on those who permit it, and read the text twice and Rashi once. Halacha Yomit answers likewise: one who does not understand Targum Onkelos reads it in any case, and will gradually learn to understand most of it; Rashi does not exempt from the targum, which is precisely what the Sages instituted – this, the editors write, is the view of most authorities, though some say that nowadays one may read Rashi –, but it is highly recommended to read Rashi as well."),
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
            R("kh", 19, cite='''פי' שצריך לקרות שנים מקרא ואחד פירוש אבל בפירוש לחודיה לא סגי. ופסוקים שאין להם פירוש צריך לקרותם ג"פ מקרא כמו פסוקים שאין להם תרגום. הר"ם מינץ סי' פ"ז. כנה"ג בהגה"ט'''),
            R("kh", 20, cite='''מיהו לפי חכמי המקו' משמע דוקא תרגום לסוד הכמוס כדי להכניס קליפת נוגה למקום הקדושה ביום השבת והבין. עו"ת או' ב\''''),
            R("kh", 23, cite='''ונראה דאפי' אם לא הותר לקרות הפרשה שמו"ת בליל הששי יכול לקרות פרש"י בליל ו' כדי לצאת י"ח וירא שמים יצא ידי שתיהם תרגום ורש"י. רו"ח או' ג\''''),
        ],
            "« S'il a étudié la paracha avec Rachi » : le Kaf ha'Haïm rapporte, du Maharam Mintz cité par la Knesset haGuedola, qu'il faut lire deux fois le texte et une fois le commentaire – le commentaire seul ne suffit pas – et que les versets sans commentaire se lisent trois fois, comme les versets sans targoum. Il rapporte cependant, du 'Olat Tamid, que d'après les kabbalistes il ressort qu'il faut précisément le targoum. Et il rapporte du Roua'h 'Haïm qu'il semble que, même si l'on ne permet pas de lire Chnayim mikra la nuit de jeudi à vendredi, on peut lire Rachi cette nuit-là pour s'acquitter ; celui qui craint le Ciel s'acquitte des deux, targoum et Rachi.",
            "“If one studied the parasha with Rashi”: the Kaf HaChaim reports, from the Maharam Mintz as cited by the Knesset HaGedolah, that one must read the text twice and the commentary once – the commentary alone is not enough – and that verses without commentary are read three times, like verses without targum. He reports, however, from the Olat Tamid, that according to the kabbalists it appears that it must be the targum specifically. And he reports from the Ruach Chaim that it seems that, even if reading Shnayim mikra on Thursday night is not permitted, one may read Rashi that night to fulfil the obligation; one who fears Heaven fulfils both, targum and Rashi."),
        H("tous", [
            R("taz", 1, cite='''וצריך לתרץ לפירש"י למה לא נקט בגמ' באמת ראובן ושמעון ונראה דיש רבותא בזה דלא מבעיא ראובן ושמעון שהם שמות השבטים ויש בהם ודאי קדושה בטעם שמות אלו אלא אפי' עטרות ודיבון שהם שמות ערי א"י ואפש' שקראו אות' העכו"ם אפ"ה צריך לקרות' ג"פ'''),
            R("kh", 17, cite='''ורבינו בחיי כתב לפי שיש באלו העיירות שמות של ע"ז ושלא תאמר כיון שהתרגום הוא פי' הכתב אין לנו לתרגם הכתוב הזה כי יש בו זכרון ע"ז וע"כ באו חכמים לומר שאף הפסוק הזה ראוי לתרגמו ושלא להקל בו. שכנה"ג בהגה"ט או' ד\''''),
            R("ahs", 11, cite='''אפילו פסוקי שמות כ"ראובן ושמעון" – צריך תרגום. ולא מפני התרגום, שהרי גם בלשון התרגום השמות שוין ללשון המקרא, אלא משום דצריך שלושה פעמים'''),
        ],
            "Pourquoi le Talmud nomme-t-il justement « Atarot et Divon » ? Le Taz propose, dans l'explication de Rachi : non seulement « Réouven et Chimon », noms des tribus, qui portent certainement une sainteté, mais même « Atarot et Divon », noms de villes de la terre d'Israël que les nations ont peut-être ainsi appelées, se lisent trois fois. Rabbénou Be'hayé, que le Kaf ha'Haïm cite d'après le Chiyouré Knesset haGuedola : ces villes portent des noms d'idolâtrie, et l'on aurait pu dire qu'il ne faut pas traduire ce verset qui en porte le souvenir ; les Sages enseignent que même ce verset mérite son targoum, sans allègement. L'Aroukh haChoul'han : pour des noms comme « Réouven et Chimon », ce n'est pas à cause du targoum – les noms y sont les mêmes que dans le texte – mais parce qu'il faut trois lectures.",
            "Why does the Talmud name precisely “Atarot and Divon”? The Taz suggests, within Rashi's explanation: not only “Reuven and Shimon”, names of the tribes, which certainly carry holiness, but even “Atarot and Divon”, names of towns of the Land of Israel that the nations may have given, are read three times. Rabbenu Bachya, whom the Kaf HaChaim quotes from the Shiyurei Knesset HaGedolah: these towns bear names of idolatry, and one might have said that this verse, which recalls it, should not be translated; the Sages teach that even this verse deserves its targum, with no leniency. The Aruch HaShulchan: for names such as “Reuven and Shimon”, it is not because of the targum – the names are the same there as in the text – but because three readings are required."),
        H("tous", [
            R("hid", "290482", passage='''במקרה כזה תוכל להקל [...] שהתרגום יהיה על ידי יהודי ירא שמים'''),
            R("hid", "356365", passage='''יש להתיר את הדבר [...] כל פסוק בפני עצמו עם התרגום לרוסית'''),
            R("hid", "233792", cite='''ולא ניתן לקרוא תרגום יונתן במקום זה''', passage='''חובה לקרוא תרגום אונקלוס [...] ולא ניתן לקרוא תרגום יונתן במקום זה'''),
        ],
            "Une traduction dans sa langue ? À celui qui ne comprend pas le targoum d'Onkelos et trouve Rachi trop difficile, le Rav Hillel Meirs (Hidabroot) répond qu'on peut, dans ce cas, être indulgent et lire une traduction dans la langue qu'il comprend, en veillant à ce qu'elle soit l'œuvre d'un Juif craignant le Ciel et qu'elle explique la paracha d'après Rachi et les Sages (il renvoie à la Michna Beroura 285:5). À qui demandait s'il est permis, même selon la Kabbale, de lire Chnayim mikra de nuit en lisant le texte en hébreu et, en guise de targoum, une traduction russe, le Rav Binyamin Chmouéli (Hidabroot) répond qu'il y a lieu de le permettre si l'on dit chaque verset à part, avec sa traduction russe. En revanche, le Targoum Yonatan ne remplace pas le targoum d'Onkelos, qu'il faut lire (Rav Hillel Meirs, qui cite le Maamar Mordekhaï du Rav Mordekhaï Eliyahou).",
            "A translation into one's own language? To one who does not understand Targum Onkelos and finds Rashi too difficult, Rav Hillel Meirs (Hidabroot) answers that in such a case one may be lenient and read a translation in the language one understands, taking care that it is the work of a God-fearing Jew and explains the parasha according to Rashi and the Sages (he refers to Mishnah Berurah 285:5). Asked whether it is permitted, even according to Kabbalah, to read Shnayim mikra at night, reading the text in Hebrew and, as targum, a Russian translation, Rav Binyamin Shmueli (Hidabroot) answers that this is to be permitted if one says each verse by itself with its Russian translation. By contrast, Targum Yonatan does not replace Targum Onkelos, which must be read (Rav Hillel Meirs, citing the Maamar Mordechai of Rav Mordechai Eliyahu)."),
        H("tous", [
            R("hid", "170276", passage='''יש לקרוא אדונ-י'''),
            R("hy", "1660q", passage='''כשקוראים תרגום קוראים עם שם ה' כמו שקוראים במקרא עצמו'''),
        ],
            "Dans le targoum aussi, on prononce le Nom divin. À qui demandait si l'on dit le Nom en lisant le targoum, Halacha Yomit répond qu'on le lit avec le Nom, comme lorsqu'on lit le texte lui-même. À qui demandait comment lire le Nom, que le targoum imprime partout « יי » – en suivant chaque fois le Nom du verset, ou en lisant partout le Tétragramme –, le Rav Binyamin Chmouéli (Hidabroot) répond qu'on lit « Ado-naï ».",
            "In the targum too, the Divine Name is pronounced. Asked whether the Name is said when reading the targum, Halacha Yomit answers that it is read with the Name, just as when one reads the text itself. Asked how to read the Name, which the targum prints everywhere as “יי” – following the Name of each verse, or reading the Tetragrammaton throughout –, Rav Binyamin Shmueli (Hidabroot) answers that one reads “Ado-nai”."),
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
            R("er", 2, cite='''וט"ז כתב שירא שמים יקרא לפחות פעם אחת בספר תורה, אבל בפרישה כתב דוקא להוציא אחרים בעינן ספר תורה'''),
        ],
            "Le Taz ajoute, pour celui qui craint le Ciel : qu'il veille à lire lui-même la paracha dans un séfer Torah au moins une fois, puis une seconde fois avec l'officiant ; car la lecture dans un 'Houmach seul n'acquitte pas pleinement : il faut « ce qui est écrit », c'est-à-dire un séfer Torah entier et conforme. Il a jusqu'à Sim'hat Torah pour compléter cela – « et c'est ainsi que j'ai toujours fait ». L'Eliya Rabba cite le Taz et note que, pour le Pericha, un séfer Torah n'est requis que pour acquitter d'autres personnes.",
            "The Taz adds, for one who fears Heaven: let him see to reading the parasha by himself from a Torah scroll at least once, and then a second time with the reader; for reading from a Chumash alone does not properly fulfil it: it requires “what is written”, that is, a complete and valid Torah scroll. He has until Simchat Torah to make this up – “and so I have always done”. The Eliyah Rabbah quotes the Taz and notes that, for the Perishah, a Torah scroll is required only when discharging others."),
        H("sefarade", [
            R("kh", 13, cite='''כל קבל דנא צריך ליזהר בקריאת המקרא בנגינת הטעמים בשלם שבפנים וכך שמענו שהיה מזהיר מאד הרב החסיד הקדוש מהר"ר משה הכהן ז"ל מעיר פי"ס לתלמידיו שיזהרו בקריאת שמו"ת לקרות המקרא כל שישנו בנותן טעם לשבח. מחב"ר או' ח\''''),
            R("kyy", 17, cite='''ובפרט מי שהוא שליח צבור הקורא בתורה, ובקי בקריאת הפרשה בטעמיה, ורוצה לקרוא הפרשה מתוך הספר הנמצא בהיכל, כדי שיהיה רגיל בקריאת הפרשה, שיש להקל בזה. ונכון שלא לטלטל את הספר תורה לתיבה'''),
        ],
            "Autant le targoum se lit sans te'amim, autant il faut veiller à lire le texte avec la mélodie des te'amim, le mieux possible : le Kaf ha'Haïm rapporte, du Ma'hazik Berakha, que le pieux Rabbi Moché haCohen en avertissait beaucoup ses élèves. Le Kitsour Yalkout Yossef permet en particulier à l'officiant qui lit la Torah, s'il connaît la paracha avec ses te'amim et veut la lire dans le séfer qui se trouve dans le heikhal pour s'y exercer, de le faire ; il convient de ne pas déplacer le séfer Torah jusqu'à la téva.",
            "Just as the targum is read without te'amim, so one must take care to read the text with the melody of the te'amim, as fully as possible: the Kaf HaChaim reports, from the Machazik Berachah, that the pious Rabbi Moshe HaKohen used to warn his students strongly about this. The Kitzur Yalkut Yosef allows in particular the reader who reads the Torah, if he knows the parasha with its te'amim and wishes to read it from the scroll kept in the heichal in order to practise, to do so; it is proper not to carry the Torah scroll to the tevah."),
        H("tous", [
            R("hid", "260576", cite='''יש לקרוא בקול באופן שתשמע מה שאתה מוציא מפיך'''),
            R("hid", "31258", passage='''בדיבור ולא בעיניים'''),
            R("hy", "1660q", passage='''חובה לקרוא בפיו ממש, ואין להסתפק בהרהור הלב בלבד'''),
            R("hid", "241128", passage='''1. אין איסור. [...] 2. אין הבדל.'''),
        ],
            "On lit de sa bouche. Le Rav Hillel Meirs (Hidabroot) répond qu'on lit à voix haute, de façon à entendre ce qu'on prononce ; le Rav Binyamin Chmouéli (Hidabroot), qu'on étudie l'explication du texte en la prononçant, et non des yeux seulement. Halacha Yomit : la pensée ne vaut pas la parole ; pour Chnayim mikra comme pour les bénédictions et les prières, il faut prononcer réellement, et la seule pensée ne suffit pas. Sur un ordinateur ou un téléphone : le Rav Binyamin Chmouéli répond qu'il n'y a pas d'interdit, et pas de différence avec un livre imprimé.",
            "One reads with one's mouth. Rav Hillel Meirs (Hidabroot) answers that one reads aloud, so as to hear what one utters; Rav Binyamin Shmueli (Hidabroot), that one studies the explanation of the text by saying it, not with the eyes alone. Halacha Yomit: thought does not count as speech; for Shnayim mikra, as for blessings and prayers, one must actually pronounce the words, and thinking them is not enough. On a computer or a phone: Rav Binyamin Shmueli answers that there is no prohibition, and no difference from a printed book."),
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
            R("hy", "1660", passage='''מותר מן הדין לקרוא את הפרשה שניים מקרא ואחד תרגום בזמן קריאת [...] שיקרא מילה במילה עם השליח ציבור את כל הפרשה [...] וכן נוהגים רבים'''),
        ],
            "Le Kaf ha'Haïm cite le Kitsour Chla : ceux qui lisent Chnayim mikra pendant la lecture publique n'agissent pas bien, car il convient d'écouter l'officiant et de se taire ; et il cite le Yafé laLev : « c'est ainsi que nous tenons », contre le Beit Yossef et le Darkhei Moché. Le Kitsour Yalkout Yossef permet, si l'officiant s'attarde sur les te'amim au point qu'on ait le temps de lire Chnayim mikra pendant la lecture, de le faire et d'être quitte – sauf pour Zakhor et Para, qu'il faut écouter –, à condition de lire à voix basse et que dix autres écoutent, ou de s'être tourné de côté et d'avoir commencé à lire avant le début de la lecture ; il conclut cependant qu'il convient, pour celui qui est scrupuleux, d'écouter dans toutes les parachiot la lecture de l'officiant. Halacha Yomit distingue trois degrés : la stricte loi permet de lire Chnayim mikra pendant la lecture de la Torah ; il convient pourtant de s'en tenir alors à une seule lecture du texte, mot à mot avec l'officiant, quitte à relire ensuite une fois le texte et une fois le targoum, comme beaucoup le font ; le mieux reste de se taire pendant toute la lecture et de lire Chnayim mikra à un autre moment.",
            "The Kaf HaChaim cites the Kitzur Shelah: those who read Shnayim mikra during the public reading do not act well, since it is fitting to listen to the reader and be silent; and he cites the Yafeh LaLev: “this is how we hold”, against the Beit Yosef and the Darkei Moshe. The Kitzur Yalkut Yosef allows it, if the reader lingers over the te’amim so that one has time to read Shnayim mikra during the reading, and one fulfils the obligation – except for Zachor and Parah, which must be heard – provided one reads in a whisper and ten others are listening, or one turned aside and began reading before the reading began; he concludes, however, that it is fitting for a careful person to listen to the reader in all the parashiyot. Halacha Yomit distinguishes three levels: strict law permits reading Shnayim mikra during the Torah reading; it is nevertheless proper to keep then to a single reading of the text, word for word with the reader, and to read the text once more and the targum once afterwards, as many do; best of all is to stay silent throughout the reading and read Shnayim mikra at another time."),
        H("tous", [
            R("kh", 8, cite='''אם שמע שמו"ת מאחר אפי' בלא אונס יצא ובלבד שיכוין לשמוע מלה במלה. הרדב"ז שם סי' תכ"ה. מחב"ר או' ג'. אמנם כבר כתבנו במקום אחר דיותר טוב לאדם להוציא הוא עצמו ולא לסמוך לצאת ע"י אחרים'''),
            R("sht", 6, cite='''ובמח"ב כתב בשם הרדב"ז בתשובה ד"פ אם שמע שמו"ת מאחר אפילו בלי אונס יצא ובלבד שיכוין לשמוע מלה במלה'''),
            R("ahs", 3, cite='''וכן יש מי שאומר שאם שמע שנים מקרא ואחד תרגום – גם כן יצא, עם כיוון לשמוע (שערי תשובה בשם רדב"ז). ולעניות דעתי בעינן דווקא לימוד, ולא שמיעה'''),
            R("hid", "217642", passage='''ובלבד שיכוון לשמוע מילה במילה [...] לכתחילה יותר עדיף לקרוא שניים מקרא ואחד תרגום בעצמו [...] אלא אם כן קרא בפיו ביחד עם החזן'''),
        ],
            "Écouter la lecture d'un autre. Celui qui a entendu d'un autre Chnayim mikra véé'had targoum, même sans y être contraint, est quitte, pourvu qu'il se soit appliqué à écouter mot à mot : c'est l'avis du Radbaz, rapporté par le Ma'hazik Berakha, puis par les Cha'arei Techouva et le Kaf ha'Haïm. Le Kaf ha'Haïm ajoute qu'il vaut mieux s'acquitter soi-même que de compter sur d'autres. L'Aroukh haChoul'han rapporte cet avis et écrit qu'à son humble avis il faut précisément étudier, et non écouter. Le Rav Hillel Meirs (Hidabroot) répond dans le sens du Radbaz : par la règle « celui qui écoute est comme celui qui dit », on peut s'acquitter en écoutant un autre, à condition de s'appliquer à entendre mot à mot ; a priori il vaut mieux lire soi-même ; il signale l'avis de l'Aroukh haChoul'han et du 'Hazon Ich, pour qui cette règle n'a pas été dite pour Chnayim mikra ; et l'on ne s'acquitte pas en écoutant l'officiant lire la Torah, à moins d'avoir lu de sa bouche avec lui.",
            "Hearing another person read. One who heard Shnayim mikra ve-echad targum from someone else, even when not forced to, has fulfilled the obligation, provided he took care to listen word by word: this is the view of the Radbaz, reported by the Machazik Berachah and then by the Sha'arei Teshuvah and the Kaf HaChaim. The Kaf HaChaim adds that it is better to fulfil it oneself than to rely on others. The Aruch HaShulchan reports this view and writes that in his humble opinion what is required is study specifically, not hearing. Rav Hillel Meirs (Hidabroot) answers in line with the Radbaz: by the rule “one who hears is like one who says”, one may fulfil the obligation by hearing another, provided one takes care to hear word by word; in the first place it is better to read oneself; he notes the view of the Aruch HaShulchan and the Chazon Ish that this rule was not said for Shnayim mikra; and one does not fulfil it by hearing the reader read the Torah, unless one read it with one's own mouth together with him."),
        H("ashkenaze", [
            R("sa", 6, cite='''מלמדי תינוקות אין צריכים לחזור ולקרות הפרשה בשבת'''),
            R("mb", 16, cite='''ודוקא בימיהם שהיו לומדים פירוש המקרא עם התינוקות ולכך יוצאין בזה גם ידי תרגום'''),
            R("mb", 16, cite='''אבל אם לומד פירוש המלות לחוד לא יצא ידי תרגום אלא השני פעמים מקרא דבודאי קרא עם התינוקות שני פעמים ולכן צריך לומר תרגום בעצמו [מחה"ש וכן מצדד הפמ"ג]'''),
            R("sahr", 7, cite='''לפיכך מלמדי תינוקות שגמרו הפרשה עם התינוקות פעם אחת אינם צריכין לחזור ולקרותה ב' פעמים אלא יקראו פעם אחת והתרגום במה דברים אמורים כשלמדו עם התינוקות פירוש המלות בלבד אבל אם למדו פירוש המקרא יצאו ידי תרגום גם כן ועל דרך שנתבאר למעלה ואינם צריכים אלא לחזור ולקרות המקרא פעם אחת אם לא קראו עם התינוקות ב' פעמים'''),
            R("ahs", 13, cite='''ומלמדי תינוקות שקראו הסדרה בכל השבוע עם התינוקות כמה פעמים – יוצאים בזה ידי קריאה. ואם קראו עמהם התרגום או פירוש רש"י – יוצאים בזה ידי חובת תרגום גם כן'''),
            R("ahs", 13, cite='''וכן כל מי שלמד הסדרה באמצע השבוע שני פעמים – אין צריך לחזור ולקרות הפרשה בשבת'''),
        ],
            "Les maîtres qui enseignent aux enfants n'ont pas à relire la paracha le Chabbat (Choul'han Aroukh). La Michna Beroura précise, d'après le Ma'hatsit haChékel (le Pri Megadim penche aussi en ce sens) : cela valait de leur temps, où l'on étudiait avec les enfants l'explication du texte, ce qui acquittait aussi du targoum ; mais celui qui n'enseigne que le sens des mots n'est quitte que des deux lectures du texte – il a certainement lu deux fois avec les enfants – et doit dire lui-même le targoum. Le Choul'han Aroukh haRav : les maîtres qui ont achevé la paracha une fois avec les enfants n'ont pas à la relire deux fois, ils la lisent une fois, avec le targoum – cela, s'ils n'ont enseigné que le sens des mots ; s'ils ont étudié avec eux l'explication du texte, ils sont quittes aussi du targoum, de la façon expliquée plus haut, et n'ont plus qu'à relire le texte une fois, s'ils ne l'ont pas lu deux fois avec les enfants. L'Aroukh haChoul'han : les maîtres qui ont lu la paracha plusieurs fois dans la semaine avec les enfants sont quittes de la lecture, et, s'ils ont lu avec eux le targoum ou Rachi, quittes aussi du targoum ; de même, quiconque a étudié la paracha deux fois dans la semaine n'a pas à la relire le Chabbat.",
            "Teachers of children need not read the parasha again on Shabbat (Shulchan Aruch). The Mishnah Berurah specifies, following the Machatzit HaShekel (the Pri Megadim also leans this way): that applied in their days, when the explanation of the text was studied with the children, which also discharged the targum; but one who teaches only the meaning of the words has fulfilled only the two readings of the text – he certainly read it twice with the children – and must say the targum himself. The Shulchan Aruch HaRav: teachers who completed the parasha once with the children need not read it twice again; they read it once, with the targum – that is, if they taught only the meaning of the words; if they studied the explanation of the text with them, they have fulfilled the targum as well, in the manner explained above, and need only read the text once more, if they did not read it twice with the children. The Aruch HaShulchan: teachers who read the parasha several times during the week with the children have fulfilled the reading, and, if they read the targum or Rashi with them, the targum as well; likewise, anyone who studied the parasha twice during the week need not read it again on Shabbat."),
        H("sefarade", [
            R("kh", 32, cite='''מפני שהם חוזרים הרבה פעמים עם התינוקות מיהא תרגום צריכים לקרות. וכ"כ הל"ח. עו"ת או' ג' וכ"כ הלב"ש ומחה"ש סק"ט להגיה בדברי המ"יא ומ"מ די שיקרא עוד פ"א תרגום'''),
            R("kh", 32, cite='''מיהו עיין מט"י או' ט' מ"ש בשם המקו' כי ע"י קריאת שמו"ת יזכה האדם להכנת תוספת נשמה יתירה'''),
            R("kh", 32, cite='''וע"כ יזהרו שלא להפסיק בעת קריאת הפרשה בשום שיחה ואפי' בד"ת'''),
            R("kh", 32, cite='''וא"כ לפ"ז גם מלמדי תינוקות אע"ג דלומדים כמה פעמים עם התינוקות צריך לקרות חוץ מזה שמו"ת כדי שיהיו תיכף בלתי הפסק בינתיים וגם כדי שילמדו כל פסוק ופסוק בפ"ע שמו"ת כדי לצאת ד"ה'''),
        ],
            "Le Kaf ha'Haïm rapporte, du 'Olat Tamid – de même le Le'hem 'Hamoudot, le Levouché Serad et le Ma'hatsit haChékel –, que les maîtres d'enfants sont dispensés parce qu'ils répètent bien des fois la paracha avec les enfants, mais qu'ils doivent tout de même lire le targoum. Il rapporte ensuite du Maté Yehouda, au nom des kabbalistes, que la lecture de Chnayim mikra prépare à recevoir le supplément d'âme du Chabbat, et qu'on veille donc à ne pas l'interrompre par une conversation, pas même par des paroles de Torah ; il en conclut que, d'après cela, les maîtres d'enfants eux aussi, bien qu'ils étudient plusieurs fois avec les enfants, doivent lire en plus Chnayim mikra véé'had targoum, pour que la lecture se fasse d'une traite, sans interruption, et pour étudier chaque verset à part, deux fois dans le texte et une fois dans le targoum, afin d'être quittes selon tous les avis.",
            "The Kaf HaChaim reports, from the Olat Tamid – and likewise the Lechem Chamudot, the Levushei Serad and the Machatzit HaShekel – that teachers of children are exempt because they review the parasha many times with the children, but that they must still read the targum. He then reports from the Mateh Yehudah, in the name of the kabbalists, that reading Shnayim mikra prepares one to receive the additional soul of Shabbat, and that one should therefore take care not to interrupt it with any conversation, not even words of Torah; he concludes that, accordingly, teachers of children too, although they study several times with the children, must read Shnayim mikra ve-echad targum in addition, so that it be read at one stretch, without interruption, and so as to study each verse by itself, twice in the text and once in the targum, in order to fulfil the obligation according to all views."),
        H("ashkenaze", [
            R("sa", (146, 2), cite='''ולקרות שנים מקרא ואחד תרגום בשעת קריאת התורה שרי וכל זה אינו ענין לפרש' זכור ופרשת פרה שהם בעשר' מדאוריית' שצריך לכוין ולשמעם מפי הקורא והנכון שבכל הפרשיות ראוי למדקדק בדבריו לכוין דעתו ולשמעם מפי הקורא'''),
            R("mb", 15, cite='''דשם מסיק המחבר בס"ב דנכון להמדקדק בדבריו לכוין דעתו לשמעם מפי הקורא'''),
            R("bh", 5, cite='''עיין בא"ר שכתב דהוא מצוה מן המובחר ופלא הוא'''),
            R("bh", 5, cite='''אלא דיוכל לסמוך מי שרוצה להקל על המקילין ע"ש אבל חלילה דנימא דהוא מצוה מן המובחר'''),
            R("bh", 5, cite='''[אם לא דנימא דכונת הא"ר הוא בין גברא לגברא]'''),
            R("mb", 14, cite='''דרק בין גברא לגברא מותר'''),
        ],
            "Au siman 146, le Choul'han Aroukh, après avoir permis de lire Chnayim mikra pendant la lecture de la Torah, ajoute que rien de cela ne concerne les parachiot Zakhor et Para – lues à dix par obligation de la Torah –, qu'il faut s'appliquer à écouter de la bouche du lecteur ; et il conclut que, dans toutes les parachiot, il convient à celui qui est scrupuleux d'appliquer son esprit à les écouter de la bouche du lecteur ; la Michna Beroura le rappelle ici. Le Béour Halakha s'étonne donc de l'Eliya Rabba, pour qui lire Chnayim mikra à ce moment serait la meilleure façon d'accomplir la mitsva : celui qui veut être indulgent peut s'appuyer sur ceux qui permettent, mais loin de nous de dire que c'est la meilleure façon – à moins que l'Eliya Rabba ne parle de l'intervalle entre deux appelés. La Michna Beroura rapporte en effet l'avis pour lequel ce n'est permis qu'entre deux appelés.",
            "In siman 146 the Shulchan Aruch, after permitting Shnayim mikra during the Torah reading, adds that none of this applies to parashat Zachor and parashat Parah – read with ten by Torah law – which one must take care to hear from the reader; and he concludes that in all parashiyot it is proper for one who is meticulous to direct his mind to hearing them from the reader; the Mishnah Berurah recalls this here. The Beur Halacha therefore wonders at the Eliyah Rabbah, for whom reading Shnayim mikra at that time would be the best way to perform the mitzvah: one who wishes to be lenient may rely on those who permit, but far be it from us to say that it is the best way – unless the Eliyah Rabbah means the interval between two aliyot. The Mishnah Berurah indeed reports the view that it is permitted only between two aliyot."),
        H("tous", [
            R("bht", (128, 46), cite='''נשאלתי אם מותר לקרות הפרשה שנים מקרא ואחד תרגום בשעה שהכהנים מברכים לעם והשבתי דאינו מותר אפי' למ"ד דמותר לקרות הפרשה שמו"ת בשעה שהש"ץ קורא הפרשה בס"ת אפ"ה אסור בברכת כהנים. שכנה"ג ופר"ח'''),
            R("kh", (128, 158), cite='''דאסור לקרות הפרשה שנים מקרא וא' תרגום בשעת ב"כ'''),
        ],
            "On ne lit pas Chnayim mikra pendant la bénédiction des Cohanim : même pour celui qui permet de la lire pendant que l'officiant lit la paracha dans le séfer Torah, c'est interdit à ce moment-là (Baèr Hétev, qui le rapporte du Chiyouré Knesset haGuedola et du Pri 'Hadach ; Kaf ha'Haïm).",
            "Shnayim mikra is not read during the Priestly Blessing: even for one who permits reading it while the reader reads the parasha from the Torah scroll, it is forbidden at that time (Ba'er Hetev, reporting it from the Shiyurei Knesset HaGedolah and the Pri Chadash; Kaf HaChaim)."),
        H("ashkenaze", [
            R("rema", (139, 1), cite='''ובמקום שהחזן קורא הוא צריך לסדר תחלה'''),
            R("er", (139, 1), cite='''משמע דהחזן צריך לסדר תחילה ולא העולה וכן משמע בבית יוסף, וקשיא על לבוש דמצריך גם עולה, מיהו גם הב"ח כתב דמצוה מן המובחר שגם העולה יסדר פעמיים ושלוש, ועל כן ראוי שכל אחד יסדר אותה תחילה דשמא יקראו אותו לעלות למחר בשבת, עד כאן. וש"ך כתב דבקריאת הפרשה שנים מקרא ואחד תרגום יוצא ידי חובת הסידור'''),
            R("ahs", (139, 2), cite='''ועכשיו ששליח הציבור קורא – מחויב לחזור הפרשה שני פעמים מקודם, אפילו אם הוא בקי. וכשקרא בערב שבת שנים מקרא – יצא בזה. ויש מי שכתב שמצוה שגם העולה יסדר (באר היטב בשם כנסת הגדולה). ואין טעם לזה, שהרי אומר בלחש אחר שליח הציבור. וגם אין המנהג כן'''),
        ],
            "Là où c'est le 'hazan qui lit la Torah, c'est lui qui doit d'abord préparer la lecture (Rema, siman 139). L'Eliya Rabba en déduit que cette préparation incombe au 'hazan et non à celui qui monte ; il rapporte toutefois du Ba'h que la meilleure façon d'accomplir la mitsva est que celui qui monte la prépare aussi, deux ou trois fois, et qu'il convient donc que chacun la prépare, car on pourrait l'appeler à monter le lendemain, Chabbat ; et il rapporte du Chiyouré Knesset haGuedola (noté « ש״ך ») qu'en lisant la paracha Chnayim mikra véé'had targoum on s'acquitte de cette préparation. L'Aroukh haChoul'han : aujourd'hui que l'officiant lit, il est tenu de revoir la paracha deux fois auparavant, même s'il la connaît ; et s'il a lu Chnayim mikra la veille de Chabbat, il est quitte par là. Quant à l'avis qui fait une mitsva, pour celui qui monte, de la préparer lui aussi (Baèr Hétev au nom de la Knesset haGuedola), l'Aroukh haChoul'han écrit qu'il n'a pas de raison – celui qui monte lit à voix basse après l'officiant – et que tel n'est pas l'usage.",
            "Where it is the chazan who reads the Torah, it is he who must first prepare the reading (Rema, siman 139). The Eliyah Rabbah infers that this preparation falls on the chazan and not on the one called up; he reports, however, from the Bach that the choicest way of fulfilling the mitzvah is for the one called up to prepare it too, two or three times, and that it is therefore fitting for everyone to prepare it, since he might be called up the next day, Shabbat; and he reports from the Shiyurei Knesset HaGedolah (written “ש״ך”) that by reading the parasha Shnayim mikra ve-echad targum one fulfils this preparation. The Aruch HaShulchan: nowadays, when the reader reads, he is obliged to review the parasha twice beforehand, even if he knows it well; and if he read Shnayim mikra on Friday, he has thereby fulfilled this. As for the view that it is a mitzvah for the one called up to prepare it as well (Ba'er Hetev in the name of the Knesset HaGedolah), the Aruch HaShulchan writes that there is no reason for it – the one called up reads quietly after the reader – and that such is not the custom."),
        H("sefarade", [
            R("kav", "yaron3", passage='''יכול להסתפק בקריאת שנים מקרא ואחד תרגום [...] ובליל שבת מותר להכין הפרשה כולה [...] יוצא ידי חובת הסידור'''),
            R("hy", "1660q", passage='''בעל קורא שחוזר על הפרשה כמה וכמה פעמים [...] בודאי שכן.'''),
        ],
            "Le lecteur de la Torah. Le Rav Yaron Achkenazi (Kav haHalakha haSefaradi) écrit que l'officiant qui lit la Torah pour tous les appelés doit préparer la paracha ; s'il est habitué à cette lecture, il peut se contenter de Chnayim mikra véé'had targoum qu'il lit le vendredi ou la nuit de Chabbat. Il cite le Chiyouré Knesset haGuedola – par Chnayim mikra on s'acquitte de cette préparation – et le Pri 'Hadach, qui demande de la préparer encore une fois pour arriver à trois ; la nuit de Chabbat, on peut préparer toute la paracha. Halacha Yomit répond qu'un lecteur qui a repassé la paracha plusieurs fois peut ne lire ensuite que le targoum.",
            "The Torah reader. Rav Yaron Ashkenazi (Kav HaHalacha HaSefaradi) writes that the reader who reads the Torah for all those called up must prepare the parasha; if he is used to this reading, he may make do with the Shnayim mikra ve-echad targum that he reads on Friday or on Friday night. He cites the Shiyurei Knesset HaGedolah – by Shnayim mikra one fulfils this preparation – and the Pri Chadash, who requires preparing it once more to reach three times; on Friday night one may prepare the whole parasha. Halacha Yomit answers that a reader who has reviewed the parasha several times may then read the targum alone."),
        H("sefarade", [
            R("ryd", "351", passage='''he would prepare the parashah on Friday night [...] entire parashah a second time, and then the Targum [...] before eating the Shabbat meal'''),
        ],
            "Le Rav David Yossef raconte l'usage de son père, le Rav Ovadia Yossef. Tant qu'il lisait lui-même la Torah à la synagogue, il préparait la paracha la nuit de Chabbat, la lisait le lendemain dans le séfer Torah – la deuxième fois –, puis lisait le targoum après Moussaf, avant le repas. Plus tard, il lisait à voix basse, mot à mot, avec le lecteur, relisait après la prière toute la paracha une seconde fois, puis le targoum. Il ne tenait pas à lire le vendredi comme le Ari, mais veillait à avoir lu aussi le targoum avant le repas du Chabbat.",
            "Rav David Yosef relates the practice of his father, Rav Ovadia Yosef. As long as he himself read the Torah in the synagogue, he prepared the parasha on Friday night, read it the next day from the Torah scroll – the second time –, then read the targum after Musaf, before the meal. Later, he would read along quietly, word for word, with the reader, read the whole parasha a second time after prayers, and then the targum. He did not insist on reading on Friday like the Ari, but took care to have read the targum as well before the Shabbat meal."),
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
            R("hid", "234777", passage='''קוראים רק את ההפטרה שיקראו בבית הכנסת'''),
        ],
            "Quand le Chabbat tombe à Roch 'Hodech, ou que c'est Chabbat Chekalim, Zakhor, Para ou Ha'Hodech, la haftara que l'on lit avec Chnayim mikra est celle de la paracha de la semaine, qu'on lise le vendredi ou le Chabbat même (Ben Ich 'Haï). Le Kaf ha'Haïm, citant la Knesset haGuedola, l'étend au Chabbat qui précède Roch 'Hodech et à celui de 'Hanouka – la haftara propre au jour, on la lit le Chabbat avec le maftir – et conclut : « et tel est l'usage ». À qui demandait quelle haftara lire quand la synagogue en lit une particulière, le Rav Binyamin Chmouéli (Hidabroot) répond autrement : on ne lit que la haftara qui sera lue à la synagogue.",
            "When Shabbat falls on Rosh Chodesh, or it is Shabbat Shekalim, Zachor, Parah or HaChodesh, the haftarah read with Shnayim mikra is that of the weekly parasha, whether one reads on Friday or on Shabbat itself (Ben Ish Chai). The Kaf HaChaim, citing the Knesset HaGedolah, extends this to the Shabbat before Rosh Chodesh and to Shabbat Chanukah – the special haftarah is read on Shabbat along with the maftir – and concludes: “and this is the custom”. Asked which haftarah to read when the synagogue reads a special one, Rav Binyamin Shmueli (Hidabroot) answers otherwise: one reads only the haftarah that will be read in the synagogue."),
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
            R("kh", 38, cite='''וע"כ אחר קריאת שמו"ת יאמר הפטרה של השבוע ואח"כ מזמור שיר ליום השבת וה' מלך גאות לבש וסדר חק לישראל המסודר ליום ו' משנה גמ' זוהר הלכות ואח"כ א"ר הונא בריה דרב יהודה א"ר אמי לעולם ישלים אדם פרשיותיו וכו' רבי חנניא בן עקשיא אומר רצה הקב"ה לזכות את ישראל וכו' ונמצא קרא תנ"ך משנה גמ קבלה'''),
            R("mbe", 131, cite='''פסוק אחרון מהפרשה אחר שקראו שמו״ת יחזור לקרותו ב׳ מקרא לבד ויקרא ההפטרה'''),
            R("mbe", 133, cite='''אח״כ יאמר ה׳ מלך גאות לבש ומשנת במה מדליקין ויאמר א״ר הונא בריה דרב יהודה א״ר אמי לעולם ישלים אדם פרשיותיו עם הציבור שמו״ת ואפילו עטרות ודיבון שכל המשלים פרשיותיו עם הצבור שמו״ת מאריכין לו ימיו ושנותיו וילמוד מאמר קטן מזהר ונמצא שקרא מקרא תנ״ך משנה גמרא זהר'''),
        ],
            "Après la lecture. Le Kaf ha'Haïm rapporte du Maté Yehouda que l'usage est de lire la haftara de chaque semaine une seule fois, dans le texte seul, et non avec le targoum comme l'écrit le Maguen Avraham : on n'a pas pris l'usage du targoum, et c'est pourquoi les haftarot sont imprimées dans les 'Houmachim sans targoum. Le Kaf ha'Haïm en conclut l'ordre à suivre : après Chnayim mikra, la haftara de la semaine, puis « Mizmor chir léyom haChabbat » et « Hachem malakh guéout lavech », l'étude du 'Hok leIsraël du vendredi (michna, guemara, Zohar, halakhot), puis l'enseignement de Rav Houna fils de Rav Yehouda au nom de Rabbi Ami (« Qu'on achève toujours ses parachiot… ») et « Rabbi 'Hanania ben Akachia dit… » : on a ainsi lu Torah, Prophètes et Écrits, michna, guemara et Kabbale. Le 'Hida (Moré beEtsba) demande, après Chnayim mikra, de relire le dernier verset de la paracha deux fois, dans le texte seul, et de lire la haftara ; puis de dire « Hachem malakh guéout lavech » et la michna « Bamé madlikin », l'enseignement de Rav Houna fils de Rav Yehouda au nom de Rabbi Ami, et d'étudier un court passage du Zohar : on a ainsi lu Torah, Prophètes et Écrits, michna, guemara et Zohar.",
            "After the reading. The Kaf HaChaim reports from the Mateh Yehudah that the custom is to read each week's haftarah once only, in the text alone, and not with the targum as the Magen Avraham writes: the targum did not become customary, which is why the haftarot are printed in the Chumashim without targum. The Kaf HaChaim concludes from this the order to follow: after Shnayim mikra, the haftarah of the week, then “Mizmor shir leyom haShabbat” and “Hashem malach ge'ut lavesh”, the Friday portion of Chok LeYisrael (mishnah, gemara, Zohar, halachot), then the teaching of Rav Huna son of Rav Yehudah in the name of Rabbi Ami (“One should always complete his portions…”) and “Rabbi Chananya ben Akashya says…”: one has thus read Torah, Prophets and Writings, mishnah, gemara and Kabbalah. The Chida (Moreh BeEtzba) asks one, after Shnayim mikra, to reread the last verse of the parasha twice, in the text alone, and to read the haftarah; then to say “Hashem malach ge'ut lavesh” and the mishnah “Bameh madlikin”, the teaching of Rav Huna son of Rav Yehudah in the name of Rabbi Ami, and to study a short passage of the Zohar: one has thus read Torah, Prophets and Writings, mishnah, gemara and Zohar."),
        H("sefarade", [
            R("kh", 37, cite='''ובענין תלתא דפורענותא וז' דנחמתא כתב שם היפ"ל דיקרא ביום ו' אחר שמו"ת הפטרת השבוע חוץ מפ' אלא הדברים דיקרא הפטרת חזון אבל הפתה"ד שם הוכיח לומר שיחיד הקורא שמו"ת בע"ש בג' דפורענותא וז' דנחמתא ותרי דתיובתא אין לו לשנות ולקרות ההפטרה מס' האיטלייא אלא ההפטרה שקורא המפטיר למחר בס"ת וכתב שכן המנהג פשוט וגם שכן הסכים הרב לב חיים ח"ב סי' קס"ו בשם כמה פו\''''),
        ],
            "Pendant les trois Chabbatot « de malheur », les sept « de consolation » et les deux « de repentir » : le Kaf ha'Haïm rapporte que, pour le Yafé laLev, on lit le vendredi, après Chnayim mikra, la haftara de la paracha, sauf à la paracha Devarim, où l'on lit « 'Hazon » ; mais que le Péta'h haDevir établit que le particulier qui lit Chnayim mikra la veille de ces Chabbatot n'a pas à changer pour lire une autre haftara : il lit celle que le maftir lira le lendemain dans le séfer Torah ; et qu'il écrit que tel est l'usage répandu, et que le Lev 'Haïm s'y est accordé lui aussi, au nom de plusieurs décisionnaires.",
            "During the three Shabbatot “of calamity”, the seven “of consolation” and the two “of repentance”: the Kaf HaChaim reports that, according to the Yafeh LaLev, on Friday after Shnayim mikra one reads the haftarah of the parasha, except at parashat Devarim, when one reads “Chazon”; but that the Petach HaDevir establishes that an individual reading Shnayim mikra on the eve of those Shabbatot should not change and read another haftarah: he reads the one which the maftir will read the next day from the Torah scroll; and that he writes that such is the widespread custom, and that the Lev Chaim too concurred, in the name of several authorities."),
        H("tous", [
            R("rema", 7, cite='''ובשבת של חתונה יקרא ההפטר' של שבת ולא שוש אשיש'''),
            R("mb", 20, cite='''ר"ל שיש מנהג באיזה מקומות שקורין בצבור לבד הפטרת הסדרה עוד איזה פסוקים מהפטרת שוש אשיש [משום דכתיב בה כחתן יכהן פאר וגומר] וקמ"ל דבשעה שקורא לעצמו ההפטרה אין צריך לקרות אלו הפסוקים משום דהוא מצוי ושגור בפי הכל ובקי בהן בלא זו הקריאה'''),
            R("ma", 12, cite='''לכן נראה לי דיחזור אותה אך אם יש הרבה חתנות זו אחר זו שוב א"צ'''),
            R("sahr", 10, cite='''ואם אירע חתונה בשבת במקומות שנוהגים אז להפטיר בבית הכנסת שוש אשיש יש לו ג"כ לקרותה לעצמו ולא הפטרת השבוע כי שמא יקראוהו למחר אבל אם אירעו הרבה חתונות בשבתות זו אחר זו די במה שקרא שוש אשיש בראשונה ויש לו לקרות בשאר השבתות הפטרת השבוע'''),
            R("ahs", 13, cite='''דבימיו היה המנהג לקרא לחתן "שוש אשיש", ובימינו לא ידענו ממנהג זה'''),
            R("kh", 39, cite='''המ"א ס"ק י"ב כתב דיחזור אותה אך אם יש הרבה תחינות זו אחר זו שוב א"צ וזהו לפי הטעם שכתבנו שחזרת ההפטרה כדי לידע מה מפטירין למחר אבל לפי הטעם שכתבנו לעיל או' ל"ו בשם הכנה"ג גם בשבת חתונה אין לקרות ביום ו' אחר השמו"ת רק הפטרת השבוע'''),
        ],
            "Le Chabbat d'un mariage. Le Rema : on lit pour soi la haftara du Chabbat, et non « Sos assis ». La Michna Beroura explique : il y a des endroits où l'usage est d'ajouter en public, à la haftara de la paracha, quelques versets de « Sos assis » ; celui qui lit la haftara pour lui-même n'a pas à les lire, car ils sont courants, familiers à tous, et on les connaît sans cette lecture. Au Maguen Avraham il semble au contraire qu'on révise « Sos assis » ; mais si plusieurs mariages se suivent, on n'a plus à le refaire. Le Choul'han Aroukh haRav de même : là où l'on a l'usage de lire alors à la synagogue « Sos assis », on la lit aussi pour soi, et non la haftara de la semaine, car on pourrait être appelé le lendemain ; mais si plusieurs mariages tombent des Chabbatot qui se suivent, il suffit de l'avoir lue la première fois, et les autres Chabbatot on lit la haftara de la semaine. L'Aroukh haChoul'han note que cet usage existait du temps du Rema et qu'on ne le connaît plus de son temps. Le Kaf ha'Haïm : l'avis du Maguen Avraham tient à la raison selon laquelle on révise la haftara pour savoir ce qu'on lira le lendemain ; mais d'après la raison rapportée au nom de la Knesset haGuedola, même le Chabbat d'un mariage on ne lit le vendredi, après Chnayim mikra, que la haftara de la semaine.",
            "The Shabbat of a wedding. The Rema: one reads for oneself the haftarah of the Shabbat, not “Sos asis”. The Mishnah Berurah explains: in some places the custom is to add in public, to the haftarah of the parasha, a few verses of “Sos asis”; one who reads the haftarah for himself need not read them, since they are common, familiar to all, and known without this reading. To the Magen Avraham it seems, on the contrary, that one does review “Sos asis”; but if several weddings follow one another, one need not do so again. The Shulchan Aruch HaRav likewise: where the custom is to read “Sos asis” in the synagogue then, one also reads it for oneself, not the haftarah of the week, since one might be called up the next day; but if several weddings fall on consecutive Shabbatot, it is enough to have read it the first time, and on the other Shabbatot one reads the haftarah of the week. The Aruch HaShulchan notes that this custom existed in the Rema's time and is no longer known in his. The Kaf HaChaim: the Magen Avraham's view rests on the reason that the haftarah is reviewed in order to know what will be read the next day; but according to the reason reported in the name of the Knesset HaGedolah, even on the Shabbat of a wedding one reads on Friday, after Shnayim mikra, only the haftarah of the week."),
        H("ashkenaze", [
            R("ahs", 13, cite='''וכן מה שקורין בראש חודש, ורגלים, וימים נוראים – אין צריך היחיד לקרותם, שכבר קראו כל אחד בשבתו'''),
            R("mb", 19, cite='''טעם המנהג שמא יקראוהו למחר למפטיר ויהא בקי ורגיל בה משא"כ בפרשיות של יו"ט ששם החזן הוא הקורא [מ"א]'''),
        ],
            "L'Aroukh haChoul'han : ce qu'on lit à Roch 'Hodech, aux fêtes de pèlerinage et aux jours redoutables, le particulier n'a pas à le lire, puisque chacun de ces passages a déjà été lu à son Chabbat. La Michna Beroura explique, d'après le Maguen Avraham, pourquoi on lit pourtant la haftara et non la lecture de Yom Tov : on peut être appelé à lire la haftara, alors que les lectures de Yom Tov, c'est l'officiant qui les lit.",
            "The Aruch HaShulchan: what is read on Rosh Chodesh, the pilgrimage festivals and the Days of Awe need not be read by the individual, since each of these passages has already been read on its Shabbat. The Mishnah Berurah explains, following the Magen Avraham, why the haftarah is nevertheless read but not the Yom Tov reading: one may be called up to read the haftarah, whereas the Yom Tov readings are read by the reader."),
        H("ashkenaze", [
            R("mb", (669, 4), cite='''כתבו הפוסקים שבליל שמחת תורה יקרא הפרשה שנים מקרא ואחד תרגום שעתה הוא זמנה'''),
            R("ma", 10, cite='''וערב ש"ת יקרא וזאת הברכה [כונות]'''),
            R("bht", 8, cite='''ובערב ש"ת יקרא וזאת הברכה. הכוונות'''),
        ],
            "Vezot haBerakha. Outre ce qu'elle écrit au siman 285, la Michna Beroura écrit, dans les lois de Sim'hat Torah, que selon les décisionnaires on lit la paracha deux fois dans le texte et une fois dans le targoum la nuit de Sim'hat Torah, « car c'est maintenant son moment » ; le Maguen Avraham et le Baèr Hétev disent, d'après le Séfer haKavanot : la veille de Sim'hat Torah.",
            "Vezot HaBerachah. Besides what it writes in siman 285, the Mishnah Berurah writes, in the laws of Simchat Torah, that according to the authorities one reads the parasha twice in the text and once in the targum on the night of Simchat Torah, “for now is its time”; the Magen Avraham and the Ba'er Hetev say, following Sefer HaKavanot: on the eve of Simchat Torah."),
        H("sefarade", [
            R("kav", "dyaakov", cite='''יקראנה בליל שמיני עצרת או בבוקר לפני תפילת שחרית'''),
            R("hy", "2740", passage='''ביום הושענא רבה יקרא פרשת וזאת הברכה שנים מקרא ואחד תרגום [...] יקרא בליל שמיני עצרת, או בבוקר השכם לפני התפלה'''),
            R("ryd", "369", passage='''It is fitting on the day of Hoshana Rabbah to read Parashat [...] or on Yom Tov morning before the Shacharit prayer'''),
            R("hid", "234777", passage='''של שמחת תורה בליל הושענא רבה [...] מעת שקראו פעם ראשונה במנחה את פרשת וזאת הברכה'''),
        ],
            "Vezot haBerakha, si l'on a oublié. On la lit le jour de Hochaana Rabba ; celui qui a oublié, ou a été empêché, la lit la nuit de Chemini Atseret ou le matin avant la prière de Cha'harit (Rav David Yaakov, Kav haHalakha haSefaradi, qui renvoie au 'Hazon Ovadia ; Halacha Yomit ; de même le Rav David Yossef : la nuit de Sim'hat Torah, ou le matin de la fête avant Cha'harit). Le Rav Binyamin Chmouéli (Hidabroot) écrit que l'usage est de la lire la nuit de Hochaana Rabba, et qu'on peut la lire dès que Vezot haBerakha a été lue une première fois à Min'ha.",
            "Vezot HaBerachah, if one forgot. It is read on the day of Hoshana Rabbah; one who forgot, or was prevented, reads it on the night of Shemini Atzeret or in the morning before the Shacharit prayer (Rav David Yaakov, Kav HaHalacha HaSefaradi, referring to Chazon Ovadia; Halacha Yomit; likewise Rav David Yosef: on Simchat Torah night, or the next morning before Shacharit). Rav Binyamin Shmueli (Hidabroot) writes that the custom is to read it on the night of Hoshana Rabbah, and that it may be read from the time Vezot HaBerachah has first been read at Minchah."),
    ]},
    {"titre": "מקרים מיוחדים", "titre_fr": "Cas particuliers", "titre_en": "Special cases", "halakhot": [
        H("tous", [
            R("sayd", 1, cite='''ות"ת הוי דבר שבצינעא אבל לחזור הפרשה כיון שחייב אדם להשלים פרשיותיו עם הצבור הוי כקורא את שמע ומותר'''),
            R("tazyd", 1, cite='''ובאגודה כתב ונראה לאיסור וכ' רש"ל להכריע דבחול אסור ובשבת שרי שהוא זמנו והוא מחובת היום'''),
            R("shakh", 4, cite='''כתוב בדרישה בשם מהרש"ל דה"ה לחזור שנים מקרא ואחד תרגום מותר'''),
            R("ksa", (219, 1), cite='''אֲבָל לַחֲזוֹר אֶת הַפָּרָשָׁה שְׁנַיִם מִקְרָא וְאֶחָד תַּרְגוּם, מֻתָּר'''),
            R("kyy", 18, cite='''אבל בתוך שבעה ימי האבלות, חייב לקרוא שנים מקרא ואחד תרגום'''),
            R("kh", 27, cite='''וראיתי בס' בה"י ביו"ד סי' ת אתא דאיתא שם דאבל יכול לחזור הפרשה בשבת שתוך ז' וכתב שם דהיינו דוקא כשלא יכלו ז' ימים קודם יום ג' אבל אם יכלו קודם יום ג' אז לדעת י"א קמא צריך להמתין עד יום ג\''''),
            R("kh", 27, cite='''מיהו אין דבריו מוכרחים דכיון דעיקר המצוה לקרות בשבת אלא דבדיעבד יכול לקרות עד יום ג' שפ"ר מקרי חובת היום. תו"ש או' ה\''''),
            R("kh", 27, cite='''והביאו א"א או' ו'. וכתב ואפשר אם חל ז' שלו בשבת דמקצת היום ככולו ימתין אחר יציאת מבהכ"נ וישלים קודם אכילה'''),
            R("rae", 1, cite='''דאפשר אם חל יום ז' בשבת צריך להמתין עד אחר יציאה מבהכ"נ וישלים קודם אכילה'''),
            R("kav", "yaron4", passage='''שמותר לאבל תוך שבעה לחזור הפרשה [...] דאיירי גבי חיוב היחיד בקריאת שנים מקרא ואחד תרגום'''),
        ],
            "L'endeuillé. Le Chabbat des sept jours de deuil, l'étude de la Torah compte parmi les choses privées (où le deuil s'applique) ; mais relire la paracha est permis : puisqu'on est tenu d'achever ses parachiot avec la communauté, c'est comme lire le Chema (Choul'han Aroukh, Yoré Déa). Le Taz rapporte que l'Agouda penche pour l'interdire et que le Maharchal tranche entre les deux : en semaine c'est interdit, le Chabbat c'est permis, car c'est son temps et l'obligation du jour. Le Chakh rapporte, de la Dericha au nom du Maharchal, qu'il en va de même pour Chnayim mikra véé'had targoum ; le Kitsour Choul'han Aroukh le dit expressément, et le Kitsour Yalkout Yossef écrit que l'endeuillé, pendant les sept jours, est tenu de lire Chnayim mikra. Le Kaf ha'Haïm rapporte l'avis du Beit Hillel (sur Yoré Déa 400), qui limite cette permission au cas où les sept jours ne s'achèvent pas avant le mardi – sinon, selon le premier « certains disent », il doit attendre jusqu'au mardi –, puis le Tossefet Chabbat, pour qui cela ne s'impose pas : l'essentiel de la mitsva est de lire le Chabbat, et ce n'est qu'a posteriori qu'on peut lire jusqu'au mardi ; c'est donc bien l'obligation du jour. Si le septième jour tombe un Chabbat, peut-être – une partie du jour comptant comme le jour entier – attend-il la sortie de la synagogue pour achever avant le repas (Échel Avraham, rapporté par Rabbi Akiva Eiger et par le Kaf ha'Haïm). Le Rav Yaron Achkenazi (Kav haHalakha haSefaradi) rapporte que le Rav Pe'alim entend cette permission de celui qui n'a pas entendu la paracha de l'officiant, et non de Chnayim mikra ; le Yabia Omer s'en étonne et renvoie au Birké Yossef, qui l'entend de l'obligation de chacun de lire Chnayim mikra.",
            "The mourner. On the Shabbat within the seven days of mourning, Torah study counts among the private matters (in which mourning applies); but reviewing the parasha is permitted: since one is obliged to complete one's portions with the congregation, it is like reading the Shema (Shulchan Aruch, Yoreh De'ah). The Taz reports that the Agudah inclines to forbid it and that the Maharshal decides between the two: on weekdays it is forbidden, on Shabbat it is permitted, since that is its time and it is the obligation of the day. The Shach reports, from the Derishah in the name of the Maharshal, that the same holds for Shnayim mikra ve-echad targum; the Kitzur Shulchan Aruch says so explicitly, and the Kitzur Yalkut Yosef writes that a mourner, during the seven days, is obliged to read Shnayim mikra. The Kaf HaChaim reports the view of the Beit Hillel (on Yoreh De'ah 400), which limits this permission to the case where the seven days do not end before Tuesday – otherwise, according to the first “some say”, he must wait until Tuesday –, and then the Tosefet Shabbat, for whom this is not compelling: the main mitzvah is to read on Shabbat, and only after the fact may one read until Tuesday; so it is indeed the obligation of the day. If the seventh day falls on Shabbat, perhaps – part of the day counting as the whole – he waits until leaving the synagogue and completes it before the meal (Eshel Avraham, reported by Rabbi Akiva Eiger and by the Kaf HaChaim). Rav Yaron Ashkenazi (Kav HaHalacha HaSefaradi) reports that the Rav Pe'alim understands this permission as referring to one who did not hear the parasha from the reader, not to Shnayim mikra; the Yabia Omer wonders at this and refers to the Birkei Yosef, who understands it of each person's obligation to read Shnayim mikra."),
        H("tous", [
            R("rema", (553, 2), cite='''ונהגו שלא ללמוד בערב תשעה באב מחצות ואילך כי אם בדברים המותרים בתשעה באב ולכן אם חל בשבת אין אומרים פרקי אבות'''),
            R("ksa", (125, 4), cite='''אֲבָל לִקְרוֹת הַסִּדְרָה שְׁנַיִם מִקְרָא וְאֶחָד תַּרְגּוּם, מֻתָּר וּמִכָּל שֶׁכֵּן קֹדֶם חֲצוֹת הַיּוֹם'''),
            R("kh", (553, 19), cite='''אבל מותר לחזור שמו"ת ומכ"ש קודם חצות. ח"א כלל קל"ו או' ד' וכ"כ הזכ"ל או' ט' דאם עבר ולא קראה עד אחר חצות נראה פשוט דיכול לקרותה אח"כ אפי' אם ט"ב בשבת עצמו יעו"ש. והיינו אף לדעת המחמירים אבל לדעת המתירין כבר כתבנו באו' הקודם'''),
            R("mb", (553, 10), cite='''והט"ז מפקפק מאד על מניעת הלימוד בשבת ומסיים דהלומד בשבת אחר חצות לא הפסיד שכרו והיינו אפילו כשחל ט"ב בשבת וכ"ש כשחל עט"ב בשבת. ונראה דיש לסמוך ע"ז אחרי דאפילו כשחל בחול כמה אחרונים מקילין'''),
            R("hid", "307701", passage='''בשבת שחל בו תשעה באב [...] עד חצות של יום שבת'''),
        ],
            "Le 9 Av ou sa veille, un Chabbat. L'usage rapporté par le Rema est de n'étudier, la veille du 9 Av à partir de midi, que ce qui est permis le 9 Av ; c'est pourquoi, un Chabbat, on ne dit pas alors les Pirké Avot. Mais lire la paracha deux fois dans le texte et une fois dans le targoum est permis, à plus forte raison avant midi (Kitsour Choul'han Aroukh, pour le 9 Av qui tombe un Chabbat ; Kaf ha'Haïm, au nom du 'Hayé Adam). Le Kaf ha'Haïm ajoute, au nom du Zekhor leAvraham : si l'on a laissé passer midi sans l'avoir lue, il semble évident qu'on peut la lire ensuite, même si le 9 Av tombe le Chabbat même. Il précise que cela vaut même pour ceux qui sont stricts ; pour ceux qui permettent l'étude ce jour-là, il renvoie à ce qu'il a écrit au paragraphe précédent. La Michna Beroura rapporte que le Taz doute fort de cette abstention d'étude le Chabbat et conclut que celui qui étudie le Chabbat après midi n'a pas perdu sa récompense – même quand le 9 Av tombe un Chabbat, à plus forte raison quand c'est sa veille ; il lui semble qu'on peut s'appuyer là-dessus, puisque, même en semaine, plusieurs A'haronim sont indulgents. Le Rav Binyamin Chmouéli (Hidabroot) répond que, lorsque le 9 Av tombe un Chabbat, on lit Chnayim mikra jusqu'à midi ('hatsot) du Chabbat.",
            "The 9th of Av or its eve, on a Shabbat. The custom reported by the Rema is to study, on the eve of the 9th of Av from midday on, only what is permitted on the 9th of Av; hence on a Shabbat Pirkei Avot is not said then. But reading the parasha twice in the text and once in the targum is permitted, all the more so before midday (Kitzur Shulchan Aruch, for a 9th of Av that falls on Shabbat; Kaf HaChaim, in the name of the Chayei Adam). The Kaf HaChaim adds, in the name of the Zechor LeAvraham: if one let midday pass without having read it, it seems obvious that one may read it afterwards, even if the 9th of Av falls on that very Shabbat. He specifies that this holds even for those who are stringent; as for those who permit study on that day, he refers to what he wrote in the preceding paragraph. The Mishnah Berurah reports that the Taz strongly questions this refraining from study on Shabbat and concludes that one who studies on Shabbat after midday has not lost his reward – even when the 9th of Av falls on Shabbat, all the more so when it is its eve; and it appears that one may rely on this, since even on a weekday several Acharonim are lenient. Rav Binyamin Shmueli (Hidabroot) answers that when the 9th of Av falls on a Shabbat, one reads Shnayim mikra until midday (chatzot) of Shabbat."),
        H("sefarade", [
            R("kh", (496, 62), cite='''בן א"י שבא לחו"ל ואשתו ובניו בא"י והוא נוהג ביו"ט כמנהג א"י שהוא כאורח בחו"ל ויום ח' של פסח חל בשבת ובא"י קורין פ' אחרי אם יקרא פ' אחרי שמו"ת כבני א"י או יתנהג בקריאת הפ' כבני חו"ל השיב הרב חיד"א ז"ל בס' מראית העין בליקוטים סי' ך' או' ד' דטפי עדיף להשלים פרשיותיו עם הצבור שהוא עמהם ולענין זה לא יעשה כא"י'''),
        ],
            "Un habitant de la terre d'Israël venu à l'étranger – sa femme et ses enfants sont en terre d'Israël, et il observe la fête selon l'usage de la terre d'Israël, n'étant à l'étranger qu'un hôte –, quand le huitième jour de Pessa'h tombe un Chabbat : en terre d'Israël on lit ce jour-là la paracha de la semaine (dans le cas posé, A'haré Mot), à l'étranger la lecture de la fête. Lit-il cette paracha en Chnayim mikra comme les habitants d'Israël, ou suit-il les parachiot du lieu ? Le Kaf ha'Haïm rapporte la réponse du 'Hida (Mar'it ha'Ayin) : il vaut mieux achever ses parachiot avec la communauté où il se trouve ; sur ce point, il ne fait pas comme en terre d'Israël.",
            "A resident of the Land of Israel who has come abroad – his wife and children are in the Land of Israel, and he keeps the festival according to the custom of the Land of Israel, being only a guest abroad –, when the eighth day of Pesach falls on a Shabbat: in the Land of Israel the weekly parasha is read that day (in the case posed, Acharei Mot), abroad the festival reading. Does he read that parasha as Shnayim mikra like the residents of Israel, or follow the parashiyot of the place? The Kaf HaChaim reports the answer of the Chida (Mar'it HaAyin): it is better to complete one's portions with the congregation one is with; on this point he does not act as in the Land of Israel."),
        H("sefarade", [
            R("kh", (25, 27), cite='''בשעת קריאת שנים מקרא ואחד תרגום בפ' קדש והיה כי יביאך א"צ להיות עליו ולא הוי כעדות שקר כיון שאומר רק דרך קריאה. תשו' בנין עולם סי' ל' והביאו פתחי עולם אות יו"ד'''),
        ],
            "Lire en Chnayim mikra les passages « Kadech » et « Vehaya ki yeviakha », qui parlent des tefilines, ne demande pas de les porter : ce n'est pas « un faux témoignage », puisqu'on ne les dit qu'en manière de lecture (Kaf ha'Haïm, au nom du Binyan Olam, rapporté par le Pit'hé Olam).",
            "Reading as Shnayim mikra the passages “Kadesh” and “Vehayah ki yevi'acha”, which speak of tefillin, does not require wearing them: it is not “false testimony”, since one says them only by way of reading (Kaf HaChaim, in the name of the Binyan Olam, as reported by the Pitchei Olam)."),
        H("tous", [
            R("hid", "226173", cite='''צריך לקרוא את שתי הפרשיות שניים מקרא ואחד תרגום'''),
        ],
            "Quand deux parachiot sont jumelées, il faut lire les deux en Chnayim mikra véé'had targoum (Rav Hillel Meirs, Hidabroot).",
            "When two parashiyot are joined, both must be read as Shnayim mikra ve-echad targum (Rav Hillel Meirs, Hidabroot)."),
        H("tous", [
            R("hid", "111245", cite='''השבוע אין צורך לקרוא שניים מקרא ואחד תרגום''', passage='''השבוע אין צורך לקרוא שניים מקרא ואחד תרגום [...] ואין צורך לקרוא פרשה זו שניים מקרא ואחד תרגום'''),
            R("hid", "356863", cite='''בפרשת חול המועד אין קוראים שמו"ת כי אין פרשת השבוע'''),
        ],
            "La semaine où Yom Tov tombe un Chabbat, on n'a pas à lire Chnayim mikra : ce Chabbat-là on lit la lecture de Yom Tov, qui ne le demande pas (Rav Hillel Meirs, Hidabroot, d'après le Choul'han Aroukh 285:7 et la Michna Beroura). De même pour le Chabbat de 'Hol haMoed : on ne lit pas Chnayim mikra, puisqu'il n'y a pas de paracha de la semaine (Rav Binyamin Chmouéli, Hidabroot).",
            "In a week when Yom Tov falls on Shabbat, there is no need to read Shnayim mikra: on that Shabbat the Yom Tov reading is read, which does not require it (Rav Hillel Meirs, Hidabroot, following Shulchan Aruch 285:7 and the Mishnah Berurah). Likewise for Shabbat Chol HaMoed: Shnayim mikra is not read, since there is no parasha of the week (Rav Binyamin Shmueli, Hidabroot)."),
        H("sefarade", [
            R("ryd", "351", passage='''writes not to read it on Yom Tov, mainly because of the [...] there is no real prohibition to read it on Yom'''),
            R("hid", "324169", cite='''על פי הפשט יש לקרוא כרגיל ביום שישי''', passage='''המקובלים מורים לקרוא ביום שבת בבוקר [...] על פי הפשט יש לקרוא כרגיל ביום שישי'''),
        ],
            "Quand Yom Tov tombe un vendredi. Le Rav David Yossef expose que les kabbalistes divergent sur la lecture de Chnayim mikra un jour de Yom Tov : le Rama de Fano écrit de ne pas la lire à Yom Tov, surtout à cause du targoum – sans que ce soit un interdit absolu, comme l'a écrit le 'Hazon Ovadia ; le Ben Ich 'Haï, au nom de Rabbi Eliyahou Mani, écrit de ne pas lire à Yom Tov mais le Chabbat ; Rabbi 'Haïm Falaji, qu'on lit à Yom Tov même a priori, et que tel était l'usage. La même divergence vaut pour Vezot haBerakha et, hors d'Israël, pour Beréchit quand le second jour de fête tombe un vendredi. Sa conclusion pour Chavouot un vendredi, pour les habitants de la terre d'Israël – qui lisent le lendemain la paracha Nasso : le mieux est de lire le Chabbat ; celui qui sait qu'il n'en aura pas le temps lit le jeudi – on peut lire en plusieurs fois ; et celui qui n'a pas lu le jeudi et ne pourra pas lire le Chabbat lit le vendredi, à Yom Tov, car il n'y a pas là de véritable interdit. Le Rav Binyamin Chmouéli (Hidabroot) répond pour sa part : les kabbalistes enseignent de lire le Chabbat matin ; selon le sens simple, on lit comme d'habitude le vendredi.",
            "When Yom Tov falls on a Friday. Rav David Yosef explains that the kabbalists disagree about reading Shnayim mikra on Yom Tov: the Rama of Fano holds that it should not be read on Yom Tov, chiefly on account of the targum – though this is not an absolute prohibition, as Chazon Ovadia wrote; the Ben Ish Chai, in the name of Rabbi Eliyahu Mani, writes not to read on Yom Tov but on Shabbat; Rabbi Chaim Palagi, that one reads on Yom Tov even in the first place, and that such was the custom. The same disagreement applies to Vezot HaBerachah and, outside Israel, to Bereshit when the second day of the festival falls on a Friday. His conclusion for Shavuot on a Friday, for residents of the Land of Israel – who read Parashat Nasso the next day: it is best to read on Shabbat; one who knows he will not have time reads on Thursday – it may be read in parts; and one who did not read on Thursday and will not be able to read on Shabbat reads on Friday, on Yom Tov, for there is no real prohibition in this. Rav Binyamin Shmueli (Hidabroot) answers for his part: the kabbalists teach to read on Shabbat morning; according to the plain meaning, one reads as usual on Friday."),
        H("sefarade", [
            R("tsh", 56, cite='''בסדר לימוד הפסוקים שמו״ת אשר יסד רבינו האר״י ז״ל ומסודר בסדר חק לישראל אור הששי לא ילמוד כי אם כ״ו פסוקים שנים מקרא לבד בלי תרגום'''),
            R("hy", "1660q", passage='''האם קריאת חוק לישראל פוטרת מקריאת שניים מקרא ואחד תרגום [...] כן, בהחלט.'''),
        ],
            "'Hok leIsraël. À qui demandait si la lecture du 'Hok leIsraël dispense de Chnayim mikra – pour les versets qu'on y a lus, s'entend –, Halacha Yomit répond : oui, tout à fait. Le 'Hida (Tsiporen Chamir) rappelle que cet ordre d'étude des versets en Chnayim mikra, disposé dans le 'Hok leIsraël, a été institué par le Ari, et précise que la nuit de jeudi à vendredi on n'y lit que vingt-six versets, deux fois dans le texte seul, sans targoum.",
            "Chok LeYisrael. Asked whether reading Chok LeYisrael exempts one from Shnayim mikra – for the verses read there, of course –, Halacha Yomit answers: yes, absolutely. The Chida (Tziporen Shamir) recalls that this order of studying the verses as Shnayim mikra, set out in Chok LeYisrael, was instituted by the Ari, and specifies that on Thursday night one reads there only twenty-six verses, twice in the text alone, without targum."),
    ]},
]

INTRO = {
    "t": ("<b>מבוא</b> הלכות שנים מקרא ואחד תרגום, מלוקטות מן הפוסקים: כל הלכה עם מקורה – דברי הפוסקים בלשונם, ותשובות זמננו בתמצית ובציון מקומן. "
          "<small>[ספרדים – עדות המזרח]</small> – לבני עדות המזרח; <small>[אשכנזים – נוסח אשכנז ונוסח ספרד]</small> – לנוסח אשכנז ולנוסח ספרד; "
          "הלכה בלי ציון – לכל העדות. אין כאן הכרעה: כל שאלה למעשה תישאל לרב."
          "<br><small>מקורות: שולחן ערוך עם הגהות הרמ״א, ט״ז ושערי תשובה (מגיני ארץ, למברג תרנ״ג), מגן אברהם, משנה ברורה וביאור הלכה, "
          "באר היטב וקיצור שולחן ערוך (תורת אמת), חיי אדם, אליה רבה, ספר חסידים, מורה באצבע וצפורן שמיר לחיד״א, ט״ז, ש״ך ורבי עקיבא איגר ליורה דעה, "
          "כף החיים (ירושלים תר״ע–תרצ״ג), בן איש חי (ויקיטקסט), רמב״ם (תורת אמת) – נחלת הכלל, דרך ספריא; "
          "ערוך השולחן – ויקיטקסט, CC BY-SA, דרך ספריא; "
          "שולחן ערוך הרב – הוצאת קה״ת (Kehot Publication Society), CC BY-NC, דרך ספריא; "
          # La mention que demande Torat Emet pour ses livres sous CC BY-NC-SA 2.5 (toratemetfreeware.com/contents/copyrights2.html).
          "ילקוט יוסף – קיצור שולחן ערוך, מהדורת התשס״ז, מתוך מאגר תורת אמת: כל הזכויות שמורות לרב יצחק יוסף שליט״א, בכפוף לתנאי רשיון CC BY-NC-SA 2.5 – אסור בשימוש מסחרי (creativecommons.org/licenses/by-nc-sa/2.5/deed.he); "
          "תשובות הידברות, קו ההלכה הספרדי, בית ההוראה ״הלכה למעשה״ של הרב אופיר מלכא והרב בנימין חותה (כיכר השבת), ״הלכה יומית״ על פי פסקי מרן הרב עובדיה יוסף, "
          "והשיעור השבועי של הראשון לציון הרב דוד יוסף, מחבר ״הלכה ברורה״ (הספר עצמו לא נקרא כאן) – בתמצית ובציון מקומן, לא בהעתקה.</small>"),
    "fr": ("<b>Introduction</b> Les lois de Chnayim mikra véé'had targoum – lire chaque semaine la paracha deux fois dans le texte hébreu et une fois dans la traduction araméenne d'Onkelos –, réunies d'après les décisionnaires : chaque halakha donne sa source, citée en hébreu quand c'est un ouvrage classique, résumée et référencée quand c'est une réponse d'aujourd'hui. "
           "<small>[Séfarades – rite Edot hamizra'h]</small> : pour qui suit les décisionnaires séfarades ; <small>[Ashkénazes – rites Ashkenaz et Sfard]</small> : pour les rites Ashkenaz et Sfard ; sans indication : pour tous. "
           "Ce recueil ne tranche rien : pour une question pratique, on interroge un rav."
           "<br><small>Sources : Choul'han Aroukh avec les gloses du Rema, Taz et Cha'arei Techouva (Maginei Eretz, Lemberg 1893), Maguen Avraham, Michna Beroura et Béour Halakha, Baèr Hétev et Kitsour Choul'han Aroukh (Torat Emet), 'Hayé Adam, Eliya Rabba, Séfer 'Hassidim, Moré beEtsba et Tsiporen Chamir du 'Hida, Taz, Chakh et Rabbi Akiva Eiger sur Yoré Déa, Kaf ha'Haïm (Jérusalem 1910-1933), Ben Ich 'Haï (Wikisource), Rambam (Torat Emet) : domaine public, via Sefaria. "
           "Aroukh haChoul'han : Wikisource, CC BY-SA, via Sefaria. "
           "Choul'han Aroukh haRav : Kehot Publication Society, CC BY-NC, via Sefaria. "
           "Kitsour Choul'han Aroukh Yalkout Yossef, édition 5767, base Torat Emet : tous droits réservés au Rav Yitzhak Yosef, sous la licence CC BY-NC-SA 2.5, usage commercial interdit (creativecommons.org/licenses/by-nc-sa/2.5/deed.fr). "
           "Réponses de Hidabroot, de Kav haHalakha haSefaradi, du beit hora'a « Halakha lema'assé » du Rav Ofir Malka et du Rav Binyamin 'Hota (Kikar haChabbat), articles de Halacha Yomit (d'après les décisions du Rav Ovadia Yossef) et cours hebdomadaires du Rav David Yossef, auteur de Halakha Beroura (son livre lui-même n'a pas pu être lu ici) : résumés et référencés, non reproduits. "
           "Français et anglais rédigés par ordinateur d'après les sources ; chaque citation hébraïque a été relue à sa source. Une seconde relecture automatique du français et de l'anglais contre les sources a été faite pour chaque halakha (26/11/2026). Non relus par un rav : pour les sources citées, l'hébreu fait foi.</small>"),
    "en": ("<b>Introduction</b> The laws of Shnayim mikra ve-echad targum – reading the weekly parasha twice in the Hebrew text and once in Onkelos’ Aramaic translation –, gathered from the halachic authorities: each law gives its source, quoted in Hebrew when it is a classical work, summarised with its reference when it is an answer of today. "
           "<small>[Sephardim – Edot HaMizrach rite]</small>: for those who follow the Sephardi authorities; <small>[Ashkenazim – Ashkenaz and Sfard rites]</small>: for the Ashkenaz and Sfard rites; unmarked: for everyone. "
           "This collection decides nothing: for a practical question, ask a rabbi."
           "<br><small>Sources: Shulchan Aruch with the Rema’s glosses, Taz and Sha’arei Teshuvah (Maginei Eretz, Lemberg 1893), Magen Avraham, Mishnah Berurah and Beur Halacha, Ba’er Hetev and Kitzur Shulchan Aruch (Torat Emet), Chayei Adam, Eliyah Rabbah, Sefer Chasidim, the Chida’s Moreh BeEtzba and Tziporen Shamir, Taz, Shach and Rabbi Akiva Eiger on Yoreh De’ah, Kaf HaChaim (Jerusalem 1910-1933), Ben Ish Chai (Wikisource), Rambam (Torat Emet): public domain, via Sefaria. "
           "Aruch HaShulchan: Wikisource, CC BY-SA, via Sefaria. "
           "Shulchan Aruch HaRav: Kehot Publication Society, CC BY-NC, via Sefaria. "
           "Kitzur Shulchan Aruch Yalkut Yosef, 5767 edition, Torat Emet database: all rights reserved to Rav Yitzchak Yosef, under the CC BY-NC-SA 2.5 licence, no commercial use (creativecommons.org/licenses/by-nc-sa/2.5/). "
           "Answers from Hidabroot, Kav HaHalacha HaSefaradi, Rav Ofir Malka’s “Halacha LeMaaseh” beit hora’ah and Rav Binyamin Chota (Kikar HaShabbat), articles from Halacha Yomit (following the rulings of Rav Ovadia Yosef) and weekly shiurim of Rav David Yosef, author of Halacha Berurah (the book itself could not be read here): summarised with references, not reproduced. "
           "French and English written by computer from the sources; every Hebrew quotation has been re-read at its source. A second automatic review of the French and English against the sources was done for every law (26 Nov 2026). Not reviewed by a rabbi: for the sources quoted, the Hebrew prevails.</small>"),
}

TITRE = {"he": "הלכות שנים מקרא ואחד תרגום", "fr": "Chnayim mikra : les halakhot", "en": "Shnayim mikra: the laws"}

SOURCES_META = [
    "Choul'han Aroukh O.H. 285 et Rema — Maginei Eretz, Lemberg 1893 (via API Sefaria), Public Domain",
    "Michna Beroura 285, 553:10 et 669:4 — On Your Way (via API Sefaria), Public Domain ; Béour Halakha 285 et 494 — Biur Halacha (via API Sefaria), Public Domain",
    "Maguen Avraham 285 ; Taz et Cha'arei Techouva 285 — Maginei Eretz, Lemberg 1893 ; Baèr Hétev 285 et 128 — Torat Emet 357 ; Eliya Rabba 139, 260 et 285 — Sulzbach 1757 ; 'Hayé Adam, Chabbat 7:9 — Vilna 1844 (via API Sefaria), Public Domain",
    "Choul'han Aroukh O.H. 139, 146 et 553 — Maginei Eretz, Lemberg 1893 ; Choul'han Aroukh Y.D. 400:1, Taz, Chakh et Rabbi Akiva Eiger — Ashlei Ravrevei, Lemberg 1888 (via API Sefaria), Public Domain",
    "Séfer 'Hassidim 301 et 745 — Zhitomir 1857 ; Moré beEtsba (Livourne 1842) et Tsiporen Chamir (Presbourg 1859) du 'Hida (via API Sefaria), Public Domain",
    "Aroukh haChoul'han O.H. 285 et 139 — Wikisource (via API Sefaria), CC-BY-SA : texte de 1903-1907 dans le domaine public, saisie et ponctuation de Wikisource ; courtes citations, créditées en tête du livre",
    "Kaf ha'Haïm O.H. 285, 25, 128, 496 et 553 — Jérusalem 1910-1933 (via API Sefaria), Public Domain",
    "Kitsour Choul'han Aroukh 72, 125 et 219 — Torat Emet 357 (via API Sefaria), Public Domain",
    "Ben Ich 'Haï — Wikisource (via API Sefaria), Public Domain",
    "Rambam, Hilkhot Tefila 13:25 — Torat Emet 370 (via API Sefaria), Public Domain",
    "Choul'han Aroukh haRav O.H. 285 — Kehot Publication Society (via API Sefaria), CC-BY-NC : courtes citations sans vocalisation, créditées en tête du livre",
    "Kitsour Yalkout Yossef 285 — édition Torat Emet, mahadoura 5767 : CC BY-NC-SA 2.5, la licence publique de tous les livres de la base hors Wikisource (toratemetfreeware.com/contents/copyrights2.html, lu le 26/11/2026) ; aucune autorisation à demander, à trois conditions : mention des droits en tête, usage non commercial, partage à l'identique",
    "réponses de Hidabroot, Kav haHalakha haSefaradi, du beit hora'a Halakha lema'assé (Rav Ofir Malka) et du Rav Binyamin 'Hota (Kikar haChabbat) ; articles de Halacha Yomit (d'après les décisions du Rav Ovadia Yossef) ; cours hebdomadaires du Rav David Yossef, auteur de Halakha Beroura, lus dans leur traduction anglaise — résumés avec leur référence, non reproduits (une courte phrase citée au plus) ; table de vérification : tools/chnayim_mikra/sources.json",
    "« Halakha Beroura » du Rav David Yossef : le siman 285 est paru (volume 17, simanim 275-286, Makhon Ye'havé Daat) mais ne se lit pas en ligne ; rien n'en est cité",
]


def blocs_halakha(n, h):
    """Le paragraphe affiché : hébreu (citations et références), français, anglais."""
    lignes = []
    for r in h["refs"]:
        ref = ref_texte(r, "he")
        if r["cite"]:
            lignes.append(f"{r['cite']} <small>({ref})</small>")
        elif r["src"] in AUJOURDHUI:
            lignes.append(f"<small>({ref})</small>")
        else:
            raise ValueError(f"halakha {n} : source classique sans citation {r}")
    # Deux citations successives de la même référence ne la répètent pas ; une réponse d'aujourd'hui
    # résumée en plusieurs passages (sans citation) n'affiche sa référence qu'une fois.
    fusion = []
    for r, l in zip(h["refs"], lignes):
        if not r["cite"] and any(f == (ref_texte(r, "he"), l) for f in fusion):
            continue
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
        "source": "Choul'han Aroukh et Rema avec leurs commentaires (Maguen Avraham, Taz, Baèr Hétev, Cha'arei Techouva, Eliya Rabba), Michna Beroura et Béour Halakha, 'Hayé Adam, Kitsour Choul'han Aroukh, Choul'han Aroukh haRav (Kehot, CC-BY-NC), Aroukh haChoul'han (Wikisource, CC-BY-SA), Kaf ha'Haïm, Ben Ich 'Haï, 'Hida, Séfer 'Hassidim, Rambam ; Kitsour Yalkout Yossef (Torat Emet, CC BY-NC-SA 2.5) ; réponses de Hidabroot, Kav haHalakha haSefaradi, Halakha lema'assé, du Rav Binyamin 'Hota (Kikar haChabbat), de Halacha Yomit et cours du Rav David Yossef, résumés — tools/chnayim_mikra/sources.json",
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
    "« Halakha Beroura » du Rav David Yossef (demande du propriétaire, 26/11/2026) : le siman 285 est paru au volume 17 (simanim 275-286, Makhon Ye'havé Daat ; trois libraires concordent), mais son texte ne se lit pas en ligne (Otzar HaHochma sur abonnement ; rien sur le site de l'éditeur ni sur HebrewBooks). Rien n'en est cité. Sont repris à la place : ses cours hebdomadaires (traduction anglaise publiée par Halacha Yomit), dont le n° 323 où il dit lui-même ce qu'il a écrit dans le livre sur la fin du temps de lecture ; et les articles de Halacha Yomit, d'après les décisions du Rav Ovadia Yossef. Le « Kitsour Choul'han Aroukh Halakha Beroura » (deux volumes, simanim 1-239) ne contient pas le siman 285.",
    "Halacha Yomit n'est pas une source nommée par le propriétaire : ajoutée le 26/11/2026 pour approcher Halakha Beroura ; à retirer s'il ne la veut pas (références « hy »).",
    "Trois pages sans rav nommé, écartées : Hidabroot 174052 (voyageur d'Israël en diaspora quand les parachiot sont décalées), et deux pages de Kav haHalakha haSefaradi (« השבת בשבעה », l'endeuillé ; « האומר שמע שמע », le verset Chema lu deux fois). Le voyageur est traité d'après le Kaf ha'Haïm 496:62, l'endeuillé d'après le Choul'han Aroukh Y.D. 400.",
    "Sujets cherchés sans réponse écrite et signée dans les sources désignées : l'onen ; celui qui devient bar mitsva en cours d'année ; l'enregistrement audio ; lire pendant la répétition de l'officiant. Pour les enfants, seules deux mentions ont été trouvées (Rav Azoulay ; un garçon de treize ans sur Hidabroot).",
    "Rav Binyamin 'Hota : deux réponses de « הלכה ב-60 שניות » (Kikar haChabbat) dont la page donne le texte sont reprises (chapitre « Quand lire »). Les autres sont en vidéo ou en enregistrement seulement (Kikar haChabbat 2022-2023 et 13/02/2026, chaîne du kollel 'Hazon Ovadia, Kol haLachon, hm-news) : rien n'en est tiré, faute de texte à relire. Ses livres « כי בו שבת » ne sont pas en ligne.",
    "Rav Ofir Malka lui-même : aucune réponse écrite de sa main trouvée ; les quatre réponses retenues sont celles des rabbanim de son beit hora'a (hl5047.co.il), seules des 538 questions du site à parler de Chnayim mikra.",
    "Michna Beroura 139 et 146 : la seule édition de Sefaria (« eu5 text ») n'a pas de licence indiquée ; elles ne sont pas citées. Ce que la Michna Beroura 146 dit de Chnayim mikra pendant la lecture publique est rapporté par la Michna Beroura 285:14-15 et le Béour Halakha 285:5 ; la préparation du lecteur (139:3) est traitée d'après le Rema, l'Eliya Rabba et l'Aroukh haChoul'han. Le Cha'ar haTsiyoun 285 n'est pas sur Sefaria : il n'est cité que par le renvoi d'une réponse de Hidabroot.",
    "Kaf ha'Haïm 285 : quatre paragraphes non repris (2, 21, 30, 34), qui redisent ce que d'autres sources citées disent déjà.",
]


# --- La vérification ----------------------------------------------------------------------------

def plat(t):
    t = html.unescape(t)
    t = re.sub(r"<[^>]+>", " ", t)
    t = unicodedata.normalize("NFC", t).replace(" ", " ")
    t = re.sub("[\u200e\u200f\u202a-\u202e\u2066-\u2069]", "", t)  # marques invisibles de direction
    return re.sub(r"\s+", " ", t).strip()


def lire_octets(url, essais=4):
    """Lit une adresse ; en cas de refus passager (429, 5xx, coupure), attend et recommence."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (verification chnayim_mikra)"})
    for essai in range(essais):
        try:
            with urllib.request.urlopen(req, timeout=60) as f:
                return f.read()
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504) or essai == essais - 1:
                raise
        except (urllib.error.URLError, TimeoutError):
            if essai == essais - 1:
                raise
        time.sleep(3 * (essai + 1))


def lire_url(url):
    return lire_octets(url).decode("utf-8", errors="replace")


def lire_pdf(url):
    """Le texte d'un PDF, par pdftotext (poppler-utils) ; None si l'outil n'est pas installé."""
    if not shutil.which("pdftotext"):
        return None
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(lire_octets(url))
        f.flush()
        return subprocess.run(["pdftotext", "-q", "-enc", "UTF-8", f.name, "-"], capture_output=True).stdout.decode("utf-8", errors="replace")


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
                    brut = lire_pdf(cle) if cle.lower().endswith(".pdf") else lire_url(cle)
                    vus[cle] = None if brut is None else plat(brut)
                source = vus[cle]
                if source is None:
                    non_relues.append(f"{h['id']} {e['reference']}")
                    print(f"{h['id']} {e['reference']} : non relu (pdftotext absent)")
                    continue
            for champ in ("citation", "passage_resume"):
                if champ in e:
                    attendu = plat(e[champ]).replace(" [...] ", " ")
                    morceaux = [m.strip() for m in plat(e[champ]).split("[...]")]
                    if not all(m and m in source for m in morceaux):
                        fautes.append(f"{h['id']} {e['reference']} ({champ}) : « {attendu[:90]} »")
            print(f"{h['id']} {e['reference']} : lu")
    print()
    if non_relues:
        print(f"{len(non_relues)} référence(s) non relue(s) : le Kitsour Yalkout Yossef demande --yalkut <fichier>, les PDF demandent pdftotext")
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
