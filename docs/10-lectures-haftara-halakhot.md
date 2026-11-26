# 10. Lectures, haftara et halakhot — ce qui est repris dans ce dépôt

*État au 26 novembre 2026.* Le travail décrit dans le [cahier de reprise](09-cahier-de-reprise.md) est maintenant dans ce dépôt et branché dans l'application de test.

## Ce qui a changé dans l'application

- **Texte hors connexion.** Toute la Torah, le Targoum Onkelos et les haftarot sont dans l'application (3,5 Mo). L'app ne télécharge plus la paracha sur Sefaria, ni à la compilation ni à l'ouverture.
- **Toutes les semaines.** La paracha est calculée pour n'importe quelle date, en Israël ou en diaspora, au lieu des 5 semaines téléchargées.
- **Jamais de lecture de Yom tov.** Un Chabbat de fête ou de 'Hol hamoed n'a pas de paracha : l'accueil montre la suivante, avec sa date.
- **Haftara selon le rite.** Nouvelle ligne sur l'accueil ; elle se lit dans le lecteur, une fois, sans Targoum, et ne compte pas dans les 7 alyot. Un Chabbat spécial (Chekalim, Zakhor, Roch 'Hodech, 'Hanouka…) affiche son nom, son maftir et sa haftara. La feuille imprimée la contient aussi.
- **Réglage « Rite »** (Réglages) : Edot hamizra'h (par défaut), Sfard, Ashkenaz.
- **Réglage « Hébreu affiché ×2 / ×1 »** (panneau « Aa » du lecteur) : en ×1, chaque verset n'est affiché qu'une fois, avec le rappel « à lire 2 fois ».
- **Noms hébreux** des livres et des parachiot, écrits selon la langue : Berèchit / Bereshit / בראשית, Ovadia / Ovadia / עובדיה. L'espagnol suit l'anglais ; le tunisien et le marocain suivent le français.
- **Écran « Halakhot »** : les 83 halakhot en 8 chapitres, filtrées par rite, avec les sources en hébreu repliées sous chaque halakha.
- **Sources et licences** en bas des Réglages.

Corrigé au passage dans le lecteur : une alya était comptée comme lue dès le démarrage du défilement automatique, et jamais quand on lisait à la main. Elle est maintenant comptée quand on arrive au bout, dans les deux cas.

## Écarts avec l'écran décrit dans le cahier

| Cahier de reprise | Dans cette application | Raison |
|---|---|---|
| Montées « Cohen, Lévi… » repliées | Les 7 alyot Rishon … Shvi'i, une par jour | C'est le modèle validé ici ([03](03-lecteur-v1.md)) |
| Avec trois Sifrei Torah, la 7e montée est la lecture de Roch 'Hodech | Les 7 alyot restent celles de la paracha ; la montée spéciale et le maftir s'affichent avec la haftara | Chnayim mikra porte sur la paracha entière |
| Bouton « ×2 / ×1 » sur l'écran | Dans le panneau « Aa » du lecteur : « Hébreu affiché ×2 / ×1 » | Même réglage, à la place des autres réglages d'affichage |
| Carte « Israël ou diaspora ? » | Pas reprise | L'accueil de bienvenue pose déjà la question |

## Où se trouve chaque chose

| Sujet | Fichiers |
|---|---|
| Moteur des lectures | `web/lecture.js` (le jumeau Kotlin reste dans l'archive de My Hitbodedut) |
| Sources de vérité | `data/lecture_torah.json`, `data/lecture_torah_texte.json`, `data/lecture_torah_targoum.json`, `data/livre_chnayim_mikra.json` |
| Construction des données | `tools/lecture_torah_construction.py`, `tools/lecture_torah_targoum.py` (options `--test`) ; `tools/construit_donnees.js` écrit `web/data/` |
| Halakhot | `tools/chnayim_mikra/construction.py` (`--verifie`), `tools/chnayim_mikra/sources.json`, écran dans `web/ecrans.js` |
| Contexte des haftarot | `data/contexte_haftarot.json`, `tools/contexte_haftarot.mjs` |
| Tests | `test/` : `npm install` puis `npm test` (41 tests) |
| Vecteurs de parité | `test/vecteurs_lecture_torah.json`, régénérés par `tools/vecteurs_lecture.mjs` |
| Licences | `web/licences/BSD-2-hebcal-leyning.txt`, `web/vendor/LICENCES.txt` |

## Contrôles faits ici

- Les deux outils Python ont été relancés depuis leurs sources : les trois fichiers de données sortent **identiques** à ceux de l'archive.
- Le moteur donne la même réponse qu'hebcal chaque jour de septembre 2025 à décembre 2031, sauf les écarts voulus, comptés par catégorie. Les vecteurs de parité de l'archive passent sans changement.
- `construction.py --verifie` a relu les 338 références des 83 halakhot à leur source : toutes les citations y sont. La fidélité du français et de l'anglais a été relue à part (voir plus bas).
- Les écrans ont été ouverts dans Chromium depuis un fichier, comme dans l'APK : accueil, lecteur, haftara, halakhot, réglages, impression. L'écran des 83 halakhot a été rouvert en français, en anglais et en hébreu, pour les trois rites, sans erreur.
- Non fait : compiler l'APK. La compilation se fait sur GitHub, à la fusion dans `main`.

## Halakhot : de 31 à 83 (26/11/2026)

Demande du propriétaire : enrichir le recueil (« il y en a beaucoup plus que 31 »), vérifier toutes les sources, exploiter la Michna Beroura, Hidabroot et « Halakha Beroura ». Le siman 285 a été repris paragraphe par paragraphe dans chaque ouvrage ; les réponses d'aujourd'hui ont été cherchées question par question.

Le recueil a maintenant **83 halakhot** en 8 chapitres : 39 pour tous les rites, 25 séfarades, 19 ashkénazes. Le chapitre « Cas particuliers » est nouveau (parachiot jumelées, Yom Tov un Chabbat ou un vendredi, 'Hok leIsraël, endeuillé, 9 Av, voyageur…).

### Ce que le recueil exploite

| Ouvrage | Ce qui est repris |
|---|---|
| Choul'han Aroukh et Rema, O.H. 285 | les 7 se'ifim ; Rema 139:1 (le lecteur), Choul'han Aroukh 146:2 (pendant la lecture de la Torah), Rema 553:2 (veille du 9 Av) |
| Michna Beroura 285 | les 20 paragraphes ; Béour Halakha 285 et 494 ; Michna Beroura 553:10 et 669:4 |
| Kitsour Yalkout Yossef 285 | les 19 paragraphes |
| Kaf ha'Haïm 285 | 35 paragraphes sur 39 (les paragraphes 2, 21, 30 et 34 n'ajoutent rien) ; 25:27, 128:158, 496:62, 553:19 |
| Choul'han Aroukh haRav 285 | paragraphes 2 à 10 |
| Aroukh haChoul'han | 285:1-5, 7, 9-13 ; 139:2 |
| Autres classiques | Maguen Avraham, Taz, Baèr Hétev, Cha'arei Techouva, Eliya Rabba, 'Hayé Adam, Kitsour Choul'han Aroukh, Ben Ich 'Haï, le 'Hida (Moré beEtsba, Tsiporen Chamir), Séfer 'Hassidim, Rambam ; pour l'endeuillé, Yoré Déa 400 avec le Taz, le Chakh et Rabbi Akiva Eiger |
| Hidabroot, « שאל את הרב » | 34 réponses, attribuées au site |
| Kav haHalakha haSefaradi | 7 réponses |
| Beit hora'a « Halakha lema'assé » du Rav Ofir Malka | 4 réponses |
| Rav Binyamin 'Hota | 2 réponses écrites |
| Halacha Yomit | 3 articles (n° 1659, 1660, 2740) et les questions-réponses publiées sous deux d'entre eux |
| Rav David Yossef | 3 cours hebdomadaires (n° 323, 351, 369) |

Les réponses d'aujourd'hui sont protégées : elles sont résumées et référencées, jamais recopiées. Une citation tient en 16 mots au plus ; la table de vérification ne garde que des repères de 25 mots au plus.

### Michna Beroura

Tout le siman 285 est exploité : les 20 paragraphes, le Béour Halakha du siman, celui du siman 494 pour les Dix Paroles, 553:10 pour la veille du 9 Av et 669:4 pour Vézot haBérakha. La Michna Beroura des simanim 139 (le lecteur) et 146 (lire pendant la lecture de la Torah) n'est pas citée : Sefaria ne la donne que dans une saisie dont la licence est inconnue. Ces sujets sont traités d'après le Choul'han Aroukh, le Rema, la Michna Beroura 285:14-15, le Béour Halakha, le Kaf ha'Haïm et le Kitsour Yalkout Yossef.

### Hidabroot

Les 10 réponses déjà citées ont été relues à leur page, puis 24 réponses ont été ajoutées. Trois pages sans rav nommé ont été écartées : une de Hidabroot, deux de Kav haHalakha haSefaradi.

### « Halakha Beroura » du Rav David Yossef

Le siman 285 est paru, au volume 17 (simanim 275 à 286, Makhon Ye'havé Daat ; trois libraires concordent). Son texte ne se lit pas librement en ligne : il est dans Otzar HaHochma, sur abonnement. **Rien n'est cité du livre.**

À la place, le recueil reprend trois cours hebdomadaires du Rav David Yossef, lus dans leur traduction anglaise publiée par Halacha Yomit. Dans le cours n° 323, il dit lui-même ce qu'il a écrit dans le livre sur la fin du temps de lecture (halakha 20). Le propriétaire n'a pas le volume 17 : le recueil reste ainsi. Si le volume devient disponible, les halakhot du siman 285 pourront être ajoutées et contrôlées contre l'imprimé.

### Halacha Yomit

Ce site (« d'après les décisions du Rav Ovadia Yossef ») n'avait pas été nommé par le propriétaire. Il est repris parce qu'il publie des articles complets sur Chnayim mikra et les cours du Rav David Yossef. Les questions-réponses publiées sous les articles sont des rédacteurs du site : le recueil les attribue à « Halacha Yomit », jamais au Rav Ovadia Yossef. **Le propriétaire a décidé de le garder** : 12 halakhot le citent ; une seule (22) ne repose que sur lui.

## Vérification des sources

Trois contrôles. Aucun n'est celui d'un rav.

### 1. Le script relit chaque citation à sa source

`construction.py --verifie --yalkut <fichier>` retélécharge chaque source – Sefaria dans l'édition indiquée, la page de chaque réponse, le PDF de chaque cours – et y cherche chaque citation et chaque repère, mot pour mot. Le Kitsour Yalkout Yossef est relu dans la copie de My Hitbodedut.

Dernier passage, après toutes les corrections : **338 références relues, toutes les citations sont dans leurs sources.**

### 2. Première relecture indépendante : les 31 halakhot d'origine

Quatre relecteurs automatiques indépendants ont relu les 31 halakhot contre leurs sources, chacun sur un quart du recueil, sans connaître le travail du rédacteur. Chacun a lu en entier chaque source citée.

| Résultat | Nombre |
|---|---|
| Halakhot jugées conformes | 16 |
| Halakhot corrigées | 15 |
| Citations hébraïques fausses ou mal référencées | 0 |
| Contresens | 0 |

Ce qui a été corrigé (numéros d'aujourd'hui) :

- **Une erreur de référence** (halakha 2) : 'Hazon Ovadia, page 328 et non 228.
- **Deux attributions** : le Rav Azoulay parle de la Torah écrite la nuit, non du targoum (halakha 14) ; le Kaf ha'Haïm cite le Kitsour Chla, non le Chla (halakha 55).
- **Des conditions oubliées** : « a posteriori » (11), « a priori » (23), « le mieux est » (13), « il semble » (2), « il convient » (53, 55).
- **Qui dit quoi** : le dernier verset (23), Rachi et le targoum (38, 39), 'Houmach sans targoum (40), les te'amim du targoum (47), la bénédiction dans le séfer Torah (48), la lecture pendant l'office (54), Yom Tov (67).
- **Des citations hébraïques coupées** qui perdaient une condition ou un avis : halakhot 10, 47, 52, 53, 54, 68.

### 3. Seconde relecture indépendante : les 52 halakhot ajoutées

Cinq relecteurs automatiques indépendants, sur des copies figées du recueil. Les lots A à C couvrent les 34 halakhot ajoutées d'après les sources classiques. Les lots D et E couvrent les 18 halakhot ajoutées d'après les réponses d'aujourd'hui, et 11 halakhot complétées par ces réponses (5 des 31 d'origine, 6 des lots A à C). Chaque relecteur a relu chaque source en entier, avec les paragraphes voisins.

| Lot | Sources | Halakhot | Conformes | Corrigées |
|---|---|---|---|---|
| A | classiques | 11 | 2 | 9 |
| B | classiques | 12 | 7 | 5 |
| C | classiques | 11 | 6 | 5 |
| D | réponses d'aujourd'hui | 14 | 6 | 8 |
| E | réponses d'aujourd'hui | 15 | 10 | 5 |
| Total | | 63 | 31 | 32 |

Ces 63 relectures portent sur 57 halakhot : six ont été relues deux fois, pour leurs sources classiques puis pour les réponses d'aujourd'hui. 30 halakhot différentes ont été corrigées.

- **Citations** : aucune n'est fausse ni mal référencée. Toutes se retrouvent mot pour mot à l'adresse et dans l'édition indiquées.
- **Limites de 16 et 25 mots** pour les réponses protégées : aucun dépassement.
- **Une erreur d'attribution** (halakha 61) : une glose du Rema (O.H. 139:1) était donnée comme du Choul'han Aroukh. Corrigée.
- **Les autres corrections sont des nuances** : un avis rapporté par le Kaf ha'Haïm et donné comme le sien (Maté Yehouda, Beit David, Maharam Mintz, Roua'h 'Haïm) ; une réserve tombée dans la coupe d'une citation (Aroukh haChoul'han 285:5, 285:7, 285:9-10, 139:2) ; une condition omise (« a priori », « il semble », « même selon le Ari », « pour les habitants d'Erets Israël ») ; le cas précis d'une question (lecture de nuit « même selon la Kabbale », vendredi matin).
- **Une abréviation mal lue** (halakha 61) : « וש"ך » de l'Eliya Rabba 139:1 est le Chiyouré Knesset haGuedola, non le Chakh. Un avis laissé anonyme est maintenant nommé : « בה"י », le Beit Hillel (halakha 76).
- **Une exception oubliée** (halakha 59) : les parachiot Zakhor et Para, qu'il faut écouter de la bouche du lecteur (Choul'han Aroukh 146:2).

Les corrections demandées ont été appliquées, chacune relue à la source avant d'être portée dans le recueil. Trois choses ne l'ont pas été : l'ajout de la Michna Beroura 139:3, que Sefaria ne donne que dans une saisie sans licence connue ; les renvois d'une halakha à une autre par son numéro, parce que les numéros bougent ; quelques suggestions de style données comme facultatives.

Les rapports des relecteurs ne sont pas dans le dépôt. Les textes corrigés n'ont pas été relus une nouvelle fois par un relecteur : le script a relu leurs citations.

### Décisions du propriétaire (26/11/2026)

Les points ouverts lui ont été posés un par un.

| Point | Décision |
|---|---|
| Halacha Yomit, qu'il n'avait pas nommé | Le garder |
| « Halakha Beroura », volume 17 | Il ne l'a pas : le recueil garde les cours du Rav David Yossef à la place |
| Rite d'une halakha tirée seulement de sources séfarades | Le rite suit le contenu, non le rite des sources. Les halakhot 5, 78 et 79 passent de « séfarade » à « pour tous » |
| Formule « Léchem yi'houd » du Kaf ha'Haïm (halakha 4) | La garder pour tous, repliée : elle s'ouvre par un bouton sous la halakha |
| Titre des auteurs de Hidabroot, signés sans titre sur les pages | Écrire « Hidabroot », sans nommer l'auteur. Son nom reste dans la table de vérification |
| Cinq halakhot sans citation en hébreu (20, 22, 45, 62, 63) | Les garder ainsi |
| Abréviations du Kaf ha'Haïm développées sans avoir pu ouvrir l'ouvrage | Garder les noms développés |
| Trois coquilles probables de l'édition numérique du Kaf ha'Haïm | Les laisser telles quelles |
| « מס' האיטלייא » (Kaf ha'Haïm 285:37, halakha 71) | Se lit « בתפוצות איטלייא » : la haftara en usage dans les communautés d'Italie |
| « סברא הראשונה » (Choul'han Aroukh haRav 285:8, halakha 52) | C'est bien le premier avis : l'écoute de l'officiant compte pour une lecture |
| « קשל"ה » et « והכי נקטינן » (Kaf ha'Haïm 285:31, halakha 55) | Kitsour Chla ; « c'est ainsi que nous tenons » est du Yafé laLev |

Après ces décisions, le script a relu de nouveau les 338 références : toutes les citations sont dans leurs sources.

### Ce qui reste à montrer à un rav

1. **Abréviations développées par le rédacteur** : « עו"ת » lu « 'Olat Tamid » (halakhot 42 et 58 ; pour les lois du Chabbat le même auteur a écrit « 'Olat Chabbat », et l'ouvrage n'a pas été lu) ; « ב"ד סי' קי"א » lu « Beit David, siman 111 », et « מ"ב » lu « Massat Binyamin » (31) ; « בה"י » lu « Beit Hillel » (76) ; « וש"ך » de l'Eliya Rabba 139:1 lu « Chiyouré Knesset haGuedola » (61) ; « זכ"ל » lu « Zekhor leAvraham » (77).
2. **Coquilles probables de l'édition numérique du Kaf ha'Haïm**, affichées telles quelles : « כ"י כתבו » (285:14, sans doute « כי »), « פסוק אחר » (285:15, peut-être « אחד »), « תחינות » (285:39, sans doute « חתונות » ; halakha 72).
3. **Avis opposés rapportés sans trancher** : lire toute la paracha puis tout le targoum (29) ; s'acquitter en écoutant un autre (56) ; quelle haftara lire quand la synagogue en lit une particulière (65 et 66) ; Yom Tov un vendredi (82). Le recueil dit qui tient quoi et ne décide pas.
4. **Halakhot 2, 26 et 40, « pour tous »** : la 2 (les femmes sont dispensées) repose sur des sources séfarades et sur un renvoi de Hidabroot au Michné Halakhot 6:60, non lu ; les 26 et 40 rapportent des avis nommés de chaque rite plutôt qu'un accord.
5. **Les halakhot restées « séfarade » d'après les seules réponses d'aujourd'hui** (20, 22, 62, 63, 75, 82) : elles rapportent des décisions ou des usages séfarades (le Rav Ovadia Yossef, le Rav David Yossef, les kabbalistes). La règle « selon le contenu » pourrait en faire passer certaines « pour tous ».
6. **Ouvrages cités de seconde main**, non lus : Ma'assé Rav, Maté Yehouda, Kol Bo, Séder haYom, Korban Chabbat, Birké Yossef, Ma'hazik Berakha, Yafé laLev, Knesset haGuedola et ses Chiyourim, Beit David, Massat Binyamin, Maharam Mintz, Roua'h 'Haïm, Binyan Olam, Michné Halakhot, 'Hazon Ovadia, Yabia Omer, Rav Pe'alim, Chivat Tsion.
7. **Le Kitsour Yalkout Yossef** n'a été contrôlé que contre la copie Torat Emet, pas contre l'imprimé.
8. **Les cours du Rav David Yossef** sont lus dans leur traduction anglaise, non dans l'hébreu d'origine.

## Rav Binyamin 'Hota

Deux réponses de sa rubrique « הלכה ב-60 שניות » (Kikar haChabbat) ont un texte écrit sur la page. Elles sont résumées et référencées :

- **Halakha 10** : lire Chnayim mikra accomplit la préparation du Chabbat « par la parole » (13/06/2025).
- **Halakha 11** : le dernier délai de l'année est la lecture de la Torah à la synagogue, à Sim'hat Torah (12/10/2025).

Ses autres réponses sur le sujet sont en vidéo ou en enregistrement seulement (Kikar haChabbat 2022-2023 et 13/02/2026, kollel 'Hazon Ovadia, Kol haLachon). Rien n'en est tiré : un sous-titrage automatique n'est pas un texte fiable à attribuer à un rav. Ses livres « כי בו שבת » ne sont pas en ligne.

## Licences des textes cités

**Kitsour Yalkout Yossef.** Le propriétaire a indiqué le 26/11/2026 que cette licence a déjà été vérifiée dans le projet My Hitbodedut : ce n'est plus une question ouverte. Rappel de ce qu'elle demande (page de licence de Torat Emet, `toratemetfreeware.com/contents/copyrights2.html`) : les livres de la base, hors Wikisource, sont sous **CC BY-NC-SA 2.5** et se diffusent sans autorisation à demander, à trois conditions.

| Condition | Dans ce projet |
|---|---|
| Mention des droits et des conditions de la licence, bien visibles | Fait : introduction du recueil, Réglages › Sources et licences, `web/licences/CC-BY-NC-SA-2.5.txt` |
| Usage non commercial | Tenu : application gratuite, sans publicité. Une licence payante pour synagogues ou écoles ([06](06-autres-aspects.md), § 8) ne serait pas compatible avec ces citations |
| Partage à l'identique des œuvres dérivées | Le recueil des halakhot cite le Yalkout Yossef mot pour mot, avec la mention des droits en tête : il est concerné par cette condition |

**Autres textes.**

- Choul'han Aroukh haRav : saisie Kehot, CC BY-NC ; même condition d'usage non commercial.
- Aroukh haChoul'han : texte du domaine public ; Sefaria ne le donne que dans la saisie de Wikisource, sous CC BY-SA. Courtes citations, créditées en tête du recueil.
- Les autres classiques cités sont lus dans des éditions du domaine public.
- Réponses d'aujourd'hui : tous droits réservés ; résumées et référencées, jamais recopiées.

## Contexte des haftarot

- **Socle** : `data/contexte_haftarot.json`, le contrôle `tools/contexte_haftarot.mjs` (`--sources` relit chaque citation sur Sefaria), l'encadré « Contexte de la haftara » replié sous la haftara de l'accueil.
- **Portée** : l'application peut afficher 105 haftarot (origine et premier passage, tous rites confondus), soit environ 70 contextes à écrire.
- **État au 26/11/2026** : 7 contextes écrits (Vayichla'h, les deux Chabbat de 'Hanouka, Vayigach, Vaye'hi, Chemot selon chaque rite). Ils couvrent 12 des 105 haftarot affichées ; 93 restent sans contexte.
- **Relecture indépendante** : un relecteur automatique a relu les 42 phrases contre leurs sources. 29 étaient conformes, 13 ont été corrigées. Aucun rav ne les a relues.
- **Éditions** : les versets viennent de « Tanach with Ta'amei Hamikra » (domaine public). Le Talmud est cité dans l'édition William Davidson et Beréchit Rabba dans celle de Torat Emet, toutes deux sous CC BY-NC : usage non commercial, comme pour les halakhot. Pour le Radak (trois courtes citations), Sefaria ne déclare pas de licence.

## Prochaines étapes (cahier, section 8)

Voir la liste à jour dans le [README](../README.md#prochaines-étapes).
