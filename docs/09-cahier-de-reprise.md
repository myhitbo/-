# Projet Chnayim mikra : cahier de reprise

*État au 26 novembre 2026.* Ce travail a été commencé par erreur dans l'application My Hitbodedut. Il en sort, et ce fichier sert à le reprendre dans le projet Chnayim mikra.

## 1. Ce qui part, ce qui reste

- **Part vers le projet Chnayim mikra :**
  - la paracha de la semaine pour Chnayim mikra et le Targoum Onkelos ;
  - les haftarot ;
  - le recueil des halakhot de Chnayim mikra ;
  - le contexte des haftarot.
- **Reste dans My Hitbodedut** (décision du propriétaire du 26/11) : la lecture de la Torah du jour, repliée à sa place dans les offices de semaine, sans haftara. Elle concerne Cha'harit des lundis, jeudis, Roch 'Hodech, 'Hol hamoed, 'Hanouka, Pourim et jeûnes, et Min'ha des jeûnes.
- **Code :** tout ce qui a été écrit est gardé sur deux branches d'archive du dépôt `myhitbo/MyHitbodedut` (section 7).

## 2. Demandes et décisions du propriétaire

Elles sont données dans l'ordre où elles sont venues, car chacune corrige la précédente. Les citations sont mot pour mot.

| # | Demande | Décision retenue |
|---|---|---|
| 1 | « Je veux que tu rajoutes le texte de la parasha concordant le jour de lecture de la Torah » | Tous les jours de lecture, avec les montées, selon Israël ou la diaspora. Haftara selon le rite. Repliée à sa place, vocalisée avec te'amim, découpée par montée. |
| 2 | (décidé par Claude, le propriétaire ayant dit « enchaîne sans me demander ») | Le qere est affiché. Seuls les usages séfarades appuyés par le Kitsour Yalkout Yossef sont retenus. Le texte est gardé hors connexion. |
| 3 | « Pas de yom Tov on ne lis pas shnem mikra pour yom Tov » | L'écran montre la paracha de la semaine, jamais une lecture de Yom tov ou de Chabbat 'Hol hamoed : on passe alors à la paracha suivante. |
| 4 | « Oui, Onkelos » | Chaque verset deux fois en hébreu, puis une fois le Targoum Onkelos. Un réglage permet de n'afficher l'hébreu qu'une fois. |
| 5 | « C'est quoi abdias??? », puis « Mets les noms en hébreu ecris en français en anglais en fonction du mode ex. Ovadia Shmuel » | Les livres portent leur nom hébreu, translittéré selon la langue de l'interface. Jamais les noms de tradition chrétienne (Abdias, Élie, Achab…). |
| 6 | « Fais un recueil d'halachot pour shnem mikra » | Un recueil de halakhot, sources citées mot pour mot, avec le rite de chaque halakha. |
| 7 | « Prends Sources aussi des questions de הידברות, קו ההלכה הספרדי, הלכה למעשה מהרב אופיר מלכא, הרב בנימין חותה » | Ces réponses d'aujourd'hui sont résumées et référencées, jamais recopiées, car elles sont protégées par le droit d'auteur. |
| 8 | « Pour la haftara je propose un petit ajout un debrief rapide en option sur l'histoire de la haftara et des personnes mentionnées et du contextes sources HAREDI UNIQUEMENT » | Un encadré « Contexte » replié sous chaque haftara (section 6). Sources : 'Hazal, commentateurs classiques, auteurs 'harédim d'aujourd'hui. |
| 9 | « Je me suis trompé de projet tour ce qui concerne shnem mikra et haftara et a sortir du projet my hitbodedut » | Tout cela devient le projet Chnayim mikra. |

## 3. Le moteur des lectures

Pour une date, un office (Cha'harit ou Min'ha), Israël ou la diaspora, Jérusalem et un rite, le moteur donne la lecture : titre, montées libellées, maftir et haftara. Il existe en Kotlin et en JavaScript, avec des réponses identiques.

### Données

| Fichier | Contenu | Taille |
|---|---|---|
| `lecture_torah.json` | Parachiot et lectures de fête, montées, haftarot par rite, titres he / fr / en | 117 ko (14 ko compressé) |
| `lecture_torah_texte.json` | La Torah et les chapitres des haftarot, vocalisés et cantillés | 2,18 Mo (0,53 Mo compressé) |
| `lecture_torah_targoum.json` | Targoum Onkelos des cinq livres, 5 847 versets | 1,31 Mo (0,23 Mo compressé) |

### Sources et licences

- **Montées et haftarot :** `@hebcal/leyning` 10.1.0, licence BSD 2 clauses ; garder sa notice.
- **Texte :** « Tanach with Ta'amei Hamikra » (tanach.us, codex de Leningrad, domaine public), par l'export Sefaria.
  - Le qere est retenu.
  - Les ketiv de plusieurs mots sont traités (Chmouel I 20:2, Melakhim II 11:15).
  - Bamidbar 25:19 est séparé de 26:1, comme chez hebcal.
- **Targoum :** « Onkelos », édition Torat Emet (export Sefaria), domaine public.
  - Les éditions yéménite (CC BY-SA) et Metsudah (CC BY-NC) sont écartées.
  - Nettoyage : notes de l'éditeur retirées, cinq deux-points égarés corrigés, sof passouq ajouté.
- **Contrôles :**
  - le texte a été comparé au codex d'Alep sur 8 743 versets : seulement des graphies pleines ou défectives et des variantes connues, aucune erreur de conversion ;
  - les montées ont été comparées à Sefaria : un seul écart, Terouma, où hebcal est gardé.

### Décisions de rite

- **Sfard = Ashkenaz** pour les lectures et les haftarot (le Sfard est le siddour des 'hassidim). Les variantes 'Habad ne sont pas reprises.
- **Edot** suivent le Choul'han Aroukh et le Kitsour Yalkout Yossef (KYY) :
  - **Min'ha des jeûnes :** pas de haftara (CA 566:1 ; KYY 550:40 ; Yé'havé Daat 5:40) ; le troisième monté est « Israël ».
  - **9 Av à Min'ha :** « שובה ישראל » (Hochéa 14:2-10 ; KYY 550:40, 559:10), puis Mikha 7:18-20, ce dernier sur une source secondaire seulement.
  - **'Hanouka :** KYY 684.
  - **'Hol hamoed Souccot en diaspora :** CA 663:1 ; MB 663:2.
  - **Chemini Atseret en semaine, en diaspora :** cinq montées depuis « כל הבכור » (CA 668:2).
  - **Sim'hat Torah :** KYY 668-669:13, 16 et 27.
  - **Versets ajoutés à la haftara :** « מחר חדש » (CA 425:2) et « השמים כסאי » (KYY 685).
- **Ashkenaz et Sfard :** « דרשו » à Min'ha de chaque jeûne, 9 Av compris (Rema 566:1).
- **Écarts voulus avec hebcal :**
  - 'Hol hamoed Souccot en Israël (Rema 663:1 ; KYY 662) ;
  - Pessa'h commençant un jeudi, en Israël (KYY 488:12) ;
  - Pourim à Jérusalem seulement le 15 Adar ;
  - Pourim triple (CA 688:6) ;
  - Chabbat à Min'ha (CA 135:2, 292:1).

### Tests faits

- **Couverture :** comparaison à hebcal pour chaque jour de 2025-09 à 2031-12, en Israël et en diaspora. Chaque écart est rangé dans une catégorie nommée.
- **Parité :** Android et le site donnent les mêmes réponses sur 13 866 lectures.
- **Cas ciblés :** les Chabbatot spéciaux, le 9 Av, 'Hanouka avec Roch 'Hodech Tevet, Pourim à Jérusalem et Pourim triple, Chemini Atseret et Sim'hat Torah, les semaines où Israël et la diaspora diffèrent.

## 4. L'écran de la paracha de la semaine

### Quelle paracha

- **Cas général :** celle du Chabbat qui vient, ou du jour même si c'est Chabbat. Elle s'affiche avec ses montées, son maftir et sa haftara.
- **Chabbat spécial** (Chekalim, Zakhor, Roch 'Hodech, 'Hanouka…) : il garde son maftir et sa haftara quand il garde sa paracha.
- **Yom tov ou Chabbat 'Hol hamoed :** jamais de lecture de fête. On montre la paracha suivante, avec sa date. Exemples :
  - la semaine de Sim'hat Torah mène à Berèchit ;
  - en 5789, après Pessa'h, la paracha suivante est lue le 07/04 en Israël et le 14/04 en diaspora.
- **Parachiot jumelées** (Matot-Massé…) : une seule lecture.
- **Israël ou diaspora :** selon le réglage. S'il n'est pas confirmé et que la paracha en dépend, une carte pose la question.

### Affichage

- **En-tête :** « Paracha de la semaine : Vayichla'h », puis la date du Chabbat en civil et en hébreu.
- **Montées :** chacune est repliée, intitulée « Cohen · Berèchit 32:4–13 », avec les numéros de verset discrets.
- **Versets :** chaque verset en hébreu deux fois, puis le Targoum, plus petit et d'une couleur discrète, numéroté comme le verset.
- **Haftara :** repliée à part, sans Targoum.
- **Bouton « ×2 / ×1 » :** il n'affiche l'hébreu qu'une fois. Il est enregistré avec les autres réglages (clé `lecture_hebreu_une_fois`).
- **Chargement :** le texte se charge à la première ouverture, hors du fil principal.

### Noms des livres

| Langue | Torah | Prophètes (exemples) |
|---|---|---|
| Français | Berèchit, Chemot, Vayikra, Bamidbar, Devarim | Yehochoua, Chmouel, Melakhim, Yecha'yahou, Ovadia |
| Anglais | Bereshit, Shemot, Vayikra, Bamidbar, Devarim | Yehoshua, Shmuel, Melachim, Yeshayahu, Ovadia |
| Hébreu | בראשית, שמות, ויקרא, במדבר, דברים | יהושע, שמואל, מלכים, ישעיהו, עובדיה |

## 5. Le recueil des halakhot

Un premier jet de 31 halakhot est rédigé. Il n'a **pas encore été vérifié par un relecteur indépendant** : leur texte français est en annexe.

Chaque halakha comporte :

- la citation hébraïque exacte de ses sources, avec leur référence ;
- un français et un anglais rédigés d'après ces sources ;
- son rite : tous, séfarade (Edot) ou ashkénaze (Ashkenaz et Sfard).

Le recueil ne tranche rien : chaque question pratique se pose à un rav.

| Chapitre | Halakhot | Tous | Séfarade | Ashkénaze |
|---|---|---|---|---|
| L'obligation | 2 | 2 | 0 | 0 |
| Quand lire | 7 | 2 | 3 | 2 |
| L'ordre de la lecture | 6 | 2 | 2 | 2 |
| Targoum et Rachi | 4 | 2 | 1 | 1 |
| Te'amim, séfer Torah, 'Houmach | 3 | 2 | 1 | 0 |
| La lecture à la synagogue | 4 | 0 | 2 | 2 |
| Haftara et fêtes | 5 | 3 | 1 | 1 |
| **Total** | **31** | **13** | **10** | **8** |

- **Sources classiques**, citées mot pour mot :
  - Berakhot 8a-b ; Choul'han Aroukh et Rema O.H. 285 (Maginei Eretz) ; Michna Beroura 285 ;
  - Kaf ha'Haïm 285 ; Kitsour Choul'han Aroukh 72:11 ; Ben Ich 'Haï ; Rambam, Tefila 13:25. Toutes ces sources sont dans le domaine public.
  - Choul'han Aroukh haRav 285 : l'édition Kehot est sous licence CC BY-NC, donc seulement de courtes citations sans vocalisation.
  - Kitsour Yalkout Yossef 285, édition Torat Emet sous licence CC BY-NC-SA 2.5. La licence a été reçue pour My Hitbodedut : **à revérifier pour ce projet**.
- **Réponses d'aujourd'hui**, résumées avec leur référence, une courte phrase citée au plus :
  - Hidabroot (Rav Hillel Meirs, Rav Binyamin Chmouéli…) ;
  - Kav haHalakha haSéfaradi (Rav Y. Achkenazi, Rav O. Azoulay) ;
  - Halakha lémaassé du Rav Ofir Malka.
  - **Le Rav Binyamin 'Hota (הרב בנימין חותה) n'a pas encore été utilisé.**
- **Fichiers :**
  - le livre : `livre_chnayim_mikra.json` ;
  - la table de vérification : `tools/chnayim_mikra/sources.json`, qui donne pour chaque halakha la référence, le lien et la citation ;
  - le script `tools/chnayim_mikra/construction.py --verifie`, qui relit chaque citation à sa source.

## 6. Le contexte des haftarot : cahier des charges

Rien n'est encore rédigé.

- **Forme :** sous chaque haftara, un encadré replié « Contexte » de 4 à 6 phrases, en français et en anglais.
- **Contenu :**
  - l'histoire que raconte la haftara ;
  - qui sont les personnes mentionnées, selon le regard de 'Hazal ;
  - l'époque, avec la chronologie du Séder Olam ;
  - pourquoi on lit cette haftara avec cette paracha ou ce jour.
- **Chaque phrase porte sa source :** une référence, un lien et, pour une source classique, une courte citation exacte.
- **Sources acceptées, 'harédi uniquement :**
  - 'Hazal : Talmud, Midrach, Séder Olam ;
  - commentateurs : Rachi, Radak, Ibn Ezra, Ralbag, Abarbanel, Metsoudot, Malbim ;
  - pour le choix de la haftara : Guemara Meguila 29b-31b, Aboudarham, Levouch, Michna Beroura ;
  - auteurs 'harédim d'aujourd'hui : reformulés avec auteur, titre et lien, jamais recopiés.
- **Exclus :**
  - l'universitaire et la critique biblique ;
  - Wikipédia et les encyclopédies générales ;
  - les sources chrétiennes ;
  - Daat Mikra.
  - Un point sans source acceptée est laissé de côté.
- **Noms et ton :**
  - les noms hébreux : Ovadia, Eliyahou, A'hav, Izével, Yerov'am ;
  - jamais Abdias, Élie, Achab, Jézabel ;
  - un ton respectueux, sans spéculation sur les prophètes.
- **Portée :** les haftarot effectivement affichées. Les données en comptent 102 en tout, fêtes comprises.
- **Contrôle :** un script vérifie que chaque haftara affichée a son contexte, que chaque phrase a sa source, qu'aucun domaine exclu ni nom interdit n'apparaît. Puis un relecteur indépendant vérifie chaque source.

## 7. Où se trouve le code

Dépôt `myhitbo/MyHitbodedut`, deux branches d'archive, à ne jamais fusionner dans My Hitbodedut :

| Branche | Commit | Contenu |
|---|---|---|
| `claude/archive-chnayim-mikra-haftara` | `b14b8981` | Le moteur des lectures, la paracha de la semaine, Onkelos, les haftarot et les noms des livres. Contient aussi la refonte du siddour de My Hitbodedut, à ne pas reprendre. |
| `claude/halakhot-chnayim-mikra` | `f6e7385f` | Le recueil des 31 halakhot, comme livre de bibliothèque |

Les étapes sur la première branche, dans l'ordre :

1. `52484f48` : données, calcul et tests.
2. `bfb89ce9` et `6798678b` : la lecture dans les offices, puis une correction.
3. `95ecf3b3` : la paracha de la semaine et Onkelos.
4. `b14b8981` : les noms hébreux des livres.

Pour récupérer les fichiers dans un autre dépôt :

```bash
git fetch https://github.com/myhitbo/MyHitbodedut.git claude/archive-chnayim-mikra-haftara claude/halakhot-chnayim-mikra
```

Fichiers à reprendre :

- **Construction des données :**
  - `tools/lecture_torah_construction.py` et `tools/lecture_torah_targoum.py`, avec l'option `--test` ;
  - `web/tools/lecture-torah.mjs`.
- **Données :** `android/app/src/main/res/raw/lecture_torah.json`, `lecture_torah_texte.json` et `lecture_torah_targoum.json`.
- **Calcul :**
  - `android/app/src/main/java/com/myhitbodedut/LectureTorah.kt` : `lectures()`, `parachaSemaine()`, `versets()`, `reference()` ;
  - son jumeau `web/src/js/lecture-torah.js`.
- **Écran :**
  - Android : `SiddurLectureActivity.kt` (lignes `Lecture` et `Passage`) ;
  - site : `web/src/js/app.js` (`ecranLectureTorah`, `boiteLecture`, `passageLu`).
  - Ces deux fichiers sont mêlés au siddour de My Hitbodedut : n'en reprendre que la logique.
- **Tests :**
  - `LectureTorahTest.kt` et `LectureSiddurTest.kt` ;
  - `web/test/lecture-torah.test.mjs` et `lecture-siddur.test.mjs` ;
  - les vecteurs de parité `web/test/vecteurs_lecture_torah.json`.
- **Licences :**
  - `android/app/src/main/assets/licences/BSD-2-hebcal-leyning.txt` ;
  - les mentions du Tanakh cantillé et d'Onkelos.
- **Halakhot :**
  - `android/app/src/main/res/raw/livre_chnayim_mikra.json` ;
  - `tools/chnayim_mikra/` ;
  - `ChnayimMikraTest.kt` et `web/test/chnayim-mikra.test.mjs`.

## 8. Questions ouvertes et prochaines étapes

- [ ] Choisir le dépôt et les plateformes du projet Chnayim mikra (Android, site, iPhone). Rien n'est encore porté sur iPhone.
- [ ] Faire vérifier les 31 halakhot par un relecteur indépendant, citation par citation.
- [ ] Chercher les réponses du Rav Binyamin 'Hota et les ajouter au recueil.
- [ ] Revérifier la licence du Kitsour Yalkout Yossef pour ce projet.
- [ ] Rédiger le contexte des haftarot (section 6), puis le faire vérifier.
- [ ] Trancher les usages séfarades laissés de côté faute de source dans le KYY :
  - « השמים כסאי » et « מחר חדש » au Chabbat 'Hanouka Roch 'Hodech ;
  - Chekalim à Roch 'Hodech Adar ;
  - ha'Hodech la veille d'un Roch 'Hodech dimanche.
- [ ] Confirmer Mikha 7:18-20 après « שובה » au 9 Av à Min'ha chez les Edot.
- [ ] Dire si les communautés nord-africaines de France ont un usage propre pour 'Hol hamoed en diaspora.
- [ ] Dire si l'on veut ce qui n'est pas inclus : variantes 'Habad, lecture du soir de Sim'hat Torah, Meguilot.

## Annexe : les 31 halakhot (premier jet, non vérifié)


### L’obligation

1. **[tous]** Même si l’on entend chaque Chabbat toute la paracha lue en public, on doit lire soi-même, chaque semaine, la paracha de cette semaine : deux fois le texte hébreu (mikra) et une fois la traduction araméenne (targoum), et cela même pour le verset « Atarot et Divon » (Bamidbar 32:3). Le Talmud enseigne que celui qui « achève ses parachiot avec la communauté » voit ses jours et ses années prolongés.  
   *Sources : Berakhot 8a-b ; Choul’han Aroukh O.H. 285:1* (`chm-01`)

2. **[tous]** Une femme est dispensée de lire chaque Chabbat Chnayim mikra véé’had targoum (Kitsour Yalkout Yossef). Le Rav Hillel Meirs (Hidabroot) répond de même que les femmes n’y sont pas obligées, en renvoyant au Mishné Halakhot (t. 6, siman 60) et au ’Hazon Ovadia (Chabbat, t. 1, p. 228) ; il en déduit, dans une autre réponse, qu’une épouse ne peut pas acquitter son mari malade en lisant pour lui, puisqu’elle-même n’y est pas obligée.  
   *Sources : Kitsour Yalkout Yossef 285:12 ; Hidabroot, question 262097 ; Hidabroot, question 253987* (`chm-02`)


### Quand lire

3. **[tous]** On peut lire la paracha de la semaine à partir du dimanche : on la lit déjà « avec la communauté » (Choul’han Aroukh). La Michna Beroura précise que ce « dimanche » n’est pas strict : dès la Min’ha de Chabbat, où l’on commence en public la paracha suivante, la lire compte déjà ; mais on ne la lit pas avant cette semaine-là, et on ne tarde pas non plus. Il n’est pas nécessaire de tout lire d’une traite : selon la loi, on peut répartir la paracha sur les jours de la semaine (Choul’han Aroukh haRav), et la Michna Beroura rapporte que le Gaon de Vilna en lisait chaque jour une partie après la prière, pour finir le vendredi. Le Rav Hillel Meirs (Hidabroot) répond dans le même sens : on peut commencer dès la Min’ha de Chabbat et répartir la lecture sur la semaine ; le Rav Binyamin Chmouéli (Hidabroot) ajoute qu’on peut dire le targoum séparément de la lecture du ’Houmach.  
   *Sources : Choul’han Aroukh O.H. 285:3 ; Michna Beroura 285:1 ; Michna Beroura 285:7 ; Michna Beroura 285:8 ; Choul’han Aroukh haRav O.H. 285:6 ; Hidabroot, question 221007 ; Hidabroot, question 354260* (`chm-03`)

4. **[ashkénaze (Ashkenaz, Sfard)]** Le Kitsour Choul’han Aroukh écrit que le mieux est de lire la paracha la veille de Chabbat, après midi (’hatsot). La Michna Beroura rapporte que plusieurs A’haronim placent le meilleur moment la veille de Chabbat, mais que, selon le Maté Yehouda, celui qui lit dès le début de la semaine accomplit lui aussi la mitsva de la meilleure façon.  
   *Sources : Kitsour Choul’han Aroukh 72:11 ; Michna Beroura 285:8* (`chm-04`)

5. **[séfarade (Edot)]** Le Ari lisait la paracha le vendredi, aussitôt après la prière du matin, et le Kaf ha’Haïm rapporte que tel est l’usage des ’hassidim et des hommes d’action : la lire le matin, après Cha’harit, encore enveloppés du talith et des tefilines. Le Ben Ich ’Haï compte la lecture de toute la paracha, le vendredi, parmi les préparatifs du Chabbat « par la parole » ; celui qui a l’habitude d’étudier chaque matin après la prière lira plutôt, le vendredi, Chnayim mikra, puis ira faire les achats du Chabbat, et s’il veut d’abord sortir acheter rapidement, il le peut et lira ensuite chez lui. Le Kitsour Yalkout Yossef conclut que celui dont le temps est compté peut de toute façon lire dès le dimanche, comme le tranche le Choul’han Aroukh. Le Rav Binyamin Chmouéli (Hidabroot) répond qu’on peut lire Chnayim mikra sans porter les tefilines.  
   *Sources : Kaf ha’Haïm 285:24 ; Ben Ich ’Haï, 2e année, Lekh Lekha §11 ; Ben Ich ’Haï, 2e année, Lekh Lekha §1 ; Kitsour Yalkout Yossef 285:8 ; Hidabroot, question 354076* (`chm-05`)

6. **[tous]** Le mieux est d’achever la paracha avant de manger le Chabbat ; sinon, on l’achève après le repas, jusqu’à Min’ha. Certains permettent de l’achever jusqu’au mercredi – c’est-à-dire pendant les trois premiers jours de la semaine, qui tiennent encore un peu du Chabbat passé, explique la Michna Beroura –, d’autres jusqu’à Chemini Atseret – c’est-à-dire, précise le Rema, jusqu’à Sim’hat Torah, quand la communauté achève la Torah. Selon ce dernier avis, celui qui a laissé passer une semaine peut encore la rattraper jusque-là ; il la lit alors avec le targoum, et non le seul texte (Michna Beroura), et le Kaf ha’Haïm cite l’Abudarham : il est bon de la rattraper pendant les dix jours de pénitence. Le Rav Binyamin Chmouéli (Hidabroot) résume : a posteriori jusqu’au dimanche, selon beaucoup jusqu’au mardi, et a posteriori jusqu’à Sim’hat Torah.  
   *Sources : Choul’han Aroukh O.H. 285:4 ; Rema O.H. 285:4 ; Michna Beroura 285:11 ; Michna Beroura 285:13 ; Kaf ha’Haïm 285:28 ; Hidabroot, question 301252* (`chm-06`)

7. **[ashkénaze (Ashkenaz, Sfard)]** La Michna Beroura précise qu’on ne retarde pas pour cela le repas du Chabbat au-delà de midi (’hatsot) ; mais celui qui n’a pas lu la veille fera bien de se lever tôt le Chabbat matin pour lire avant d’aller à la synagogue ; et a priori, tous s’accordent à ne pas dépasser le Chabbat. Le Choul’han Aroukh haRav conseille, à qui a laissé passer le temps, d’achever jusqu’à la fin du mardi, et sinon jusqu’à Sim’hat Torah.  
   *Sources : Michna Beroura 285:9 ; Michna Beroura 285:12 ; Choul’han Aroukh haRav O.H. 285:5* (`chm-07`)

8. **[séfarade (Edot)]** Le Kitsour Yalkout Yossef reprend l’ordre du Choul’han Aroukh : achever avant le repas du Chabbat, sans pour autant retarder le repas jusqu’à midi ; sinon après le repas, jusqu’à Min’ha ; a posteriori jusqu’au mercredi (« רביעי בשבת »), et certains disent jusqu’à Chemini Atseret. Le Ben Ich ’Haï écrit que celui qui a été empêché de lire le vendredi lira le Chabbat après la prière, avant le Kiddouch. Le Kaf ha’Haïm rapporte que le Ari, en cas de grand empêchement, lisait le Chabbat après la prière du matin, avant le repas, et non pendant l’office comme certains le font.  
   *Sources : Kitsour Yalkout Yossef 285:5 ; Ben Ich ’Haï, 2e année, Lekh Lekha §11 ; Kaf ha’Haïm 285:3* (`chm-08`)

9. **[séfarade (Edot)]** La nuit. Le Kitsour Yalkout Yossef permet à qui manque de temps de lire Chnayim mikra la nuit du Chabbat (le vendredi soir), ainsi qu’à celui qui étudie la Torah en écrivant des ’hidouchim et des décisions de halakha. Le Kaf ha’Haïm rapporte, au nom des disciples du Ari, qu’on ne lit pas la paracha à la fin de la nuit de jeudi à vendredi, avant qu’il fasse jour, car on ne lit pas le targoum la nuit. Pour le Rav Ochri Azoulay (Kav haHalakha haSefaradi), c’est une règle de la Kabbale, alors que selon le sens simple rien n’empêche de lire la Torah écrite la nuit ; il conclut qu’on peut lire Chnayim mikra la nuit en y joignant un peu de commentaire, comme Rachi, et que celui qui sinon n’étudierait pas du tout peut lire même sans commentaire. Le Rav Menaché Moreno (beit hora’a « Halakha lema’assé » du Rav Ofir Malka) juge plus juste de lire le jour que la nuit, et le Rav Binyamin Chmouéli (Hidabroot) écrit qu’on ne lit pas depuis le début de la nuit jusqu’à minuit.  
   *Sources : Kitsour Yalkout Yossef 285:9 ; Kitsour Yalkout Yossef 285:1 ; Kaf ha’Haïm 285:14 ; Kav haHalakha haSefaradi (Rav O. Azoulay, 13/01/2023) ; Halakha lema’assé (Rav O. Malka), question 142 ; Hidabroot, question 303250* (`chm-09`)


### L’ordre de la lecture

10. **[tous]** On lit les versets dans l’ordre, sans lire un verset avant celui qui le précède ; on dit d’abord deux fois le texte, puis le targoum, et non le targoum en premier ni au milieu (Michna Beroura, Kaf ha’Haïm). Celui qui a sauté un verset et s’en aperçoit plus loin revient lire le verset oublié, puis ce qu’il avait lu après, pour garder l’ordre (Kaf ha’Haïm). À la fin de la paracha, on répète le dernier verset, pour finir par le texte de la Torah, sans avoir à en répéter le targoum (Ben Ich ’Haï ; de même le Kitsour Choul’han Aroukh, le Choul’han Aroukh haRav et le Kaf ha’Haïm). À qui demande s’il peut lire d’abord toute la paracha une fois, puis chaque verset une seconde fois suivi de son targoum, le Rav Binyamin Chmouéli (Hidabroot) répond que c’est possible.  
   *Sources : Michna Beroura 285:6 ; Kaf ha’Haïm 285:6 ; Kaf ha’Haïm 285:15 ; Ben Ich ’Haï, 2e année, Lekh Lekha §11 ; Kitsour Choul’han Aroukh 72:11 ; Choul’han Aroukh haRav O.H. 285:3 ; Kaf ha’Haïm 285:33 ; Hidabroot, question 299490* (`chm-10`)

11. **[ashkénaze (Ashkenaz, Sfard)]** Verset par verset, ou section par section ? La Michna Beroura rapporte les deux avis : lire chaque verset deux fois puis son targoum, ou chaque section (ouverte ou fermée) deux fois puis son targoum ; le Maguen Avraham et les Cha’arei Techouva penchent pour le premier, le Gaon de Vilna disait le targoum après chaque section, et chacun peut suivre l’une ou l’autre façon. Le Kitsour Choul’han Aroukh retient la lecture par section, selon le Gaon de Vilna, en s’arrêtant à la fin de la section même au milieu d’un verset. Le Choul’han Aroukh haRav juge la lecture verset par verset plus juste, tout en notant que, selon la loi, on peut lire de la façon que l’on veut.  
   *Sources : Michna Beroura 285:2 ; Kitsour Choul’han Aroukh 72:11 ; Choul’han Aroukh haRav O.H. 285:3* (`chm-11`)

12. **[séfarade (Edot)]** Selon les kabbalistes, on lit chaque verset deux fois puis son targoum, verset après verset, jusqu’à la fin de la paracha, d’une seule traite : ainsi faisait le Ari, et ainsi font les ’hassidim et les hommes d’action (Kaf ha’Haïm ; Kitsour Yalkout Yossef). Le Rav Yaron Achkenazi (Kav haHalakha haSefaradi) précise que cela n’est pas indispensable selon la halakha. Lu ainsi, le verset « Chema Israël » peut être dit deux fois, car on voit bien qu’on le répète pour Chnayim mikra (Kitsour Yalkout Yossef) ; le Rav Binyamin Chmouéli (Hidabroot) répond aussi qu’on peut sans crainte répéter le Chema, que l’on lise par section ou verset par verset.  
   *Sources : Kaf ha’Haïm 285:3 ; Kitsour Yalkout Yossef 285:4 ; Kav haHalakha haSefaradi (Rav Y. Achkenazi, 13/07/2017) ; Hidabroot, question 354076* (`chm-12`)

13. **[tous]** Un verset qui n’a pas de targoum se lit trois fois (Rambam). La Michna Beroura l’applique à « Atarot et Divon », lu trois fois parce qu’il n’a pas de targoum, et de même à « Réouven et Chimon » et aux versets semblables ; certains, plus stricts, lisent pour « Atarot et Divon » le targoum Yerouchalmi. Le Kaf ha’Haïm rapporte l’usage répandu : on ne lit trois fois que le verset qui n’a aucun targoum, comme « Réouven et Chimon », tandis que la bénédiction des Cohanim et « Atarot et Divon », qui ont un targoum, se lisent seulement deux fois avec leur targoum. Le Rav Yaron Achkenazi (Kav haHalakha haSefaradi) comprend, lui, que le Choul’han Aroukh suit le Rambam : « Atarot et Divon » trois fois, sans le targoum Yerouchalmi.  
   *Sources : Rambam, Hilkhot Tefila 13:25 ; Michna Beroura 285:3 ; Kaf ha’Haïm 285:18 ; Kav haHalakha haSefaradi (Rav Y. Achkenazi, 07/06/2017)* (`chm-13`)

14. **[ashkénaze (Ashkenaz, Sfard)]** Il est très bien, si possible, de ne s’interrompre pour rien pendant Chnayim mikra : les gens scrupuleux le font, et il convient à qui tient à son âme de faire ainsi (Michna Beroura). Il est bon de ne pas s’interrompre par une conversation au milieu de la lecture (Kitsour Choul’han Aroukh). Le Choul’han Aroukh haRav rapporte l’usage de certains d’achever toute la paracha le vendredi matin après la prière, sans s’interrompre du tout, même par la parole.  
   *Sources : Michna Beroura 285:6 ; Kitsour Choul’han Aroukh 72:11 ; Choul’han Aroukh haRav O.H. 285:6* (`chm-14`)

15. **[séfarade (Edot)]** Selon le Talmud, il n’est pas interdit de parler au milieu de Chnayim mikra ; mais selon la Kabbale on ne s’interrompt pas du tout, et l’on lit tout d’une traite (Kitsour Yalkout Yossef ; Kaf ha’Haïm). Celui qui a soif peut s’interrompre pour boire, avec la bénédiction avant et Boré nefachot après. Celui à qui l’on demande, au milieu de sa lecture du matin, de lire au public une halakha ou un enseignement sur la paracha peut s’interrompre pour en faire profiter le public (Kitsour Yalkout Yossef ; de même le Rav Yaron Achkenazi, Kav haHalakha haSefaradi) ; un érudit à qui l’on pose une question de halakha peut y répondre entre deux versets.  
   *Sources : Kitsour Yalkout Yossef 285:6 ; Kitsour Yalkout Yossef 285:7 ; Kaf ha’Haïm 285:15 ; Kav haHalakha haSefaradi (Rav Y. Achkenazi, 13/07/2017)* (`chm-15`)


### Targoum et Rachi

16. **[tous]** Celui qui a étudié la paracha avec le commentaire de Rachi est considéré comme ayant lu le targoum ; mais celui qui craint le Ciel lit le targoum et aussi Rachi (Choul’han Aroukh). Le Rav Binyamin Chmouéli (Hidabroot) le résume ainsi : on est quitte selon le strict droit, mais le Choul’han Aroukh demande les deux ; et un verset que Rachi ne commente pas se lit trois fois. Le Rav Hillel Meirs (Hidabroot) explique, avec la Michna Beroura, que le targoum a la qualité d’avoir été donné au Sinaï et de traduire chaque mot, et Rachi celle d’expliquer le sujet selon les midrachim des Sages.  
   *Sources : Choul’han Aroukh O.H. 285:2 ; Hidabroot, question 299490 ; Hidabroot, question 262007* (`chm-16`)

17. **[ashkénaze (Ashkenaz, Sfard)]** Rachi tient lieu de targoum parce qu’il explique le texte comme le targoum, et davantage ; en revanche, une traduction dans une autre langue qui ne rend que les mots ne remplace pas le targoum, car le targoum explique des choses que le texte seul ne laisse pas comprendre. Celui qui lit Rachi à la place du targoum lit trois fois les versets que Rachi ne commente pas. La Michna Beroura écrit qu’il convient en vérité que chacun étudie chaque semaine la paracha avec Rachi, en plus du targoum ; celui qui ne peut pas comprendre Rachi lira un commentaire de la Torah dans une langue qu’il comprend, qui explique la paracha selon Rachi et les Sages – la Michna Beroura et le Kitsour Choul’han Aroukh donnent en exemple le Tseéna ourééna, en yiddish ; de même le Choul’han Aroukh haRav. Le Choul’han Aroukh haRav tient Rachi pour plus utile que le targoum, et dit lui aussi que celui qui craint le Ciel lit les deux.  
   *Sources : Michna Beroura 285:4 ; Michna Beroura 285:5 ; Michna Beroura 285:6 ; Kitsour Choul’han Aroukh 72:11 ; Choul’han Aroukh haRav O.H. 285:2* (`chm-17`)

18. **[séfarade (Edot)]** Même celui qui ne comprend pas bien la langue du targoum doit lire la paracha deux fois avec le targoum, et celui qui craint le Ciel lit aussi Rachi (Kitsour Yalkout Yossef ; de même le Rav Yaron Achkenazi, Kav haHalakha haSefaradi). Celui qui n’a pas le temps d’étudier les deux étudie le targoum, auquel les kabbalistes tiennent ; mais en voyage, s’il n’a que le texte et Rachi, il peut s’appuyer sur ceux qui permettent de lire deux fois le texte et une fois Rachi (Kaf ha’Haïm).  
   *Sources : Kitsour Yalkout Yossef 285:3 ; Kaf ha’Haïm 285:22 ; Kav haHalakha haSefaradi (Rav Y. Achkenazi, 13/07/2017)* (`chm-18`)

19. **[tous]** En voyage, celui qui n’a qu’un ’Houmach sans targoum lit le texte deux fois, puis le targoum quand il en trouve un (Michna Beroura ; Kitsour Choul’han Aroukh ; Choul’han Aroukh haRav). Le Kaf ha’Haïm propose, pour achever malgré tout la paracha avec la communauté, de lire alors le texte trois fois, comme un verset sans targoum, puis, une fois arrivé, de relire si possible Chnayim mikra véé’had targoum.  
   *Sources : Michna Beroura 285:6 ; Kitsour Choul’han Aroukh 72:11 ; Choul’han Aroukh haRav O.H. 285:6 ; Kaf ha’Haïm 285:16* (`chm-19`)


### Te’amim, séfer Torah, ’Houmach

20. **[tous]** On lit les versets avec la cantillation (te’amim) ; mais celui qui ne la connaît pas reste obligé de lire Chnayim mikra, et la mélodie des te’amim n’est pas indispensable (Kitsour Yalkout Yossef ; Michna Beroura, d’après le Pri Megadim). Le Kitsour Yalkout Yossef ajoute que parents et maîtres ont le devoir sacré d’enseigner les te’amim aux enfants. Le Rav Binyamin Chmouéli (Hidabroot) répond de même : a priori avec les te’amim, et sans eux pour qui ne les connaît pas.  
   *Sources : Kitsour Yalkout Yossef 285:14 ; Michna Beroura 285:17 ; Hidabroot, question 15385* (`chm-20`)

21. **[séfarade (Edot)]** Le targoum se lit sans les te’amim : le Kitsour Yalkout Yossef écrit que c’est « précisément » ainsi, le Ben Ich ’Haï le rapporte d’après le Cha’ar Ta’amei haMitsvot, et le Kaf ha’Haïm le tient de Rabbi ’Haïm Vital, qui l’avait reçu du Ari, et cite le Korban Chabbat : on y tient.  
   *Sources : Kitsour Yalkout Yossef 285:14 ; Ben Ich ’Haï, 2e année, Lekh Lekha §11 ; Kaf ha’Haïm 285:12* (`chm-21`)

22. **[tous]** Celui qui connaît par cœur la vocalisation et les te’amim fait bien de lire le texte dans un séfer Torah (Michna Beroura ; Choul’han Aroukh haRav), le targoum se lisant alors dans un ’Houmach (Kitsour Yalkout Yossef). Celui qui ne les connaît pas lit plutôt dans un ’Houmach vocalisé, avec les te’amim, que de lire de façon fautive dans le séfer Torah ; et l’on ne récite pas de bénédiction sur cette lecture (Kitsour Yalkout Yossef ; Kaf ha’Haïm). À la question de lire Chnayim mikra sur un appareil électronique, le Rav Emmanuel Molkandov (beit hora’a « Halakha lema’assé » du Rav Ofir Malka) répond que la question a peu de conséquence pratique, mais que, si l’on y tient, cela compte comme lire dans un livre.  
   *Sources : Michna Beroura 285:2 ; Choul’han Aroukh haRav O.H. 285:4 ; Kitsour Yalkout Yossef 285:17 ; Kaf ha’Haïm 285:7 ; Halakha lema’assé (Rav O. Malka), question 484* (`chm-22`)


### La lecture à la synagogue

23. **[ashkénaze (Ashkenaz, Sfard)]** On ne se contente pas de lire une fois le texte et le targoum en comptant sur la lecture entendue de l’officiant : il faut lire soi-même deux fois le texte, en plus de ce qu’on a entendu, à moins d’avoir lu alors avec lui, de sa propre bouche. A posteriori, selon le Maguen Avraham au nom du Le’hem ’Hamoudot, l’écoute compte pour une fois ; d’autres A’haronim sont stricts même a posteriori (Michna Beroura). Le Choul’han Aroukh haRav rapporte ces avis et permet, en cas de nécessité, de s’appuyer sur l’avis selon lequel celui qui a bien entendu toute la paracha n’a plus qu’à la lire une fois avec le targoum. Le Rav Hillel Meirs (Hidabroot) répond, avec la Michna Beroura, que lire de sa bouche avec le lecteur compte pour une fois.  
   *Sources : Michna Beroura 285:2 ; Choul’han Aroukh haRav O.H. 285:8 ; Hidabroot, question 262007* (`chm-23`)

24. **[séfarade (Edot)]** On ne s’appuie pas sur la lecture entendue de l’officiant. Mais celui qui est vraiment pressé et n’a pas le temps de lire seul la paracha lit à voix basse toute la paracha avec l’officiant, verset par verset, puis la relit une seconde fois chez lui, puis lit une fois tout le targoum : il est quitte. De même, l’officiant qui lit la Torah en public peut compter sa préparation, au moins une lecture complète, et sa lecture publique, puis lire une fois le targoum.  
   *Sources : Kitsour Yalkout Yossef 285:10* (`chm-24`)

25. **[ashkénaze (Ashkenaz, Sfard)]** Le Choul’han Aroukh permet de lire Chnayim mikra pendant la lecture publique de la Torah. La Michna Beroura rapporte que le Chla et le Gaon de Vilna sont stricts : chacun doit écouter la lecture de la bouche du lecteur, chaque mot, en suivant dans un ’Houmach ; mais lire à voix basse, mot à mot, avec le lecteur, en écoutant chaque mot, n’est pas à proscrire, et plusieurs A’haronim le recommandent.  
   *Sources : Choul’han Aroukh O.H. 285:5 ; Michna Beroura 285:14* (`chm-25`)

26. **[séfarade (Edot)]** Le Kaf ha’Haïm cite le Chla : ceux qui lisent Chnayim mikra pendant la lecture publique n’agissent pas bien, car il faut écouter l’officiant ; et il cite le Yafé laLev : « c’est ainsi que nous tenons », contre le Beit Yossef et le Darkhei Moché. Le Kitsour Yalkout Yossef permet, si l’officiant s’attarde sur les te’amim au point qu’on ait le temps de lire Chnayim mikra pendant la lecture, de le faire et d’être quitte – sauf pour Zakhor et Para, qu’il faut écouter –, à condition de lire à voix basse et que dix autres écoutent, ou de s’être tourné de côté avant le début de la lecture ; il conclut cependant que celui qui est scrupuleux écoute, dans toutes les parachiot, la lecture de l’officiant.  
   *Sources : Kaf ha’Haïm 285:31 ; Kitsour Yalkout Yossef 285:11* (`chm-26`)


### Haftara et fêtes

27. **[tous]** Selon la loi, celui qui lit Chnayim mikra n’a pas à lire la haftara ; mais l’usage est de la lire (Rema ; Kitsour Choul’han Aroukh), une fois (Kitsour Yalkout Yossef ; Rav Yaron Achkenazi, Kav haHalakha haSefaradi). La Michna Beroura en donne la raison, d’après le Maguen Avraham : on pourrait être appelé le lendemain pour la lire comme maftir, et il faut la connaître.  
   *Sources : Rema O.H. 285:7 ; Michna Beroura 285:19 ; Kitsour Choul’han Aroukh 72:11 ; Kitsour Yalkout Yossef 285:2 ; Kav haHalakha haSefaradi (Rav Y. Achkenazi, 13/07/2017)* (`chm-27`)

28. **[séfarade (Edot)]** Quand le Chabbat tombe à Roch ’Hodech, ou que c’est Chabbat Chekalim, Zakhor, Para ou Ha’Hodech, la haftara que l’on lit avec Chnayim mikra est celle de la paracha de la semaine, qu’on lise le vendredi ou le Chabbat même (Ben Ich ’Haï). Le Kaf ha’Haïm, citant la Knesset haGuedola, l’étend au Chabbat veille de Roch ’Hodech et à celui de ’Hanouka – la haftara propre au jour, on la lit le Chabbat avec le maftir – et conclut : « et tel est l’usage ».  
   *Sources : Ben Ich ’Haï, 2e année, Lekh Lekha §11 ; Kaf ha’Haïm 285:36* (`chm-28`)

29. **[ashkénaze (Ashkenaz, Sfard)]** Pour les quatre parachiot (Chekalim, Zakhor, Para, Ha’Hodech), on lit la haftara des quatre parachiot (Michna Beroura). Le Choul’han Aroukh haRav précise : celle qu’on lira à la synagogue, et non celle de la paracha de la semaine ; de même pour Chabbat Roch ’Hodech, la veille de Roch ’Hodech (Ma’har ’Hodech) et Chabbat ’Hanouka.  
   *Sources : Michna Beroura 285:20 ; Choul’han Aroukh haRav O.H. 285:10* (`chm-29`)

30. **[tous]** On n’a pas à lire Chnayim mikra pour la lecture de Yom Tov, puisqu’on lit de toute façon toute la Torah, Chabbat après Chabbat (Choul’han Aroukh ; Michna Beroura ; Kitsour Yalkout Yossef ; Choul’han Aroukh haRav). Le Kaf ha’Haïm ajoute qu’il en va de même pour la lecture de ’Hol haMoed : partout où l’on lit ce qui a déjà été lu dans l’ordre des parachiot, on n’a pas à le relire.  
   *Sources : Choul’han Aroukh O.H. 285:7 ; Michna Beroura 285:18 ; Kitsour Yalkout Yossef 285:13 ; Choul’han Aroukh haRav O.H. 285:9 ; Kaf ha’Haïm 285:35* (`chm-30`)

31. **[tous]** La paracha Vezot haBerakha se lit en Chnayim mikra le jour de Hochaana Rabba (Michna Beroura ; Kaf ha’Haïm ; Ben Ich ’Haï ; Kitsour Yalkout Yossef) ; le Choul’han Aroukh haRav dit : la veille de Sim’hat Torah, qui est son moment. Celui qui l’a lue le jour de Chemini Atseret n’a rien perdu (Michna Beroura). Le Ben Ich ’Haï veut qu’on ne la lise pas le jour de Chemini Atseret, à cause du targoum, et, si l’on a oublié, qu’on la lise ce jour-là après Min’ha ; le Kitsour Yalkout Yossef dit de la lire alors à Chemini Atseret avant Cha’harit, ou avec l’officiant, et permet à qui manque de temps de la lire la nuit de Sim’hat Torah. Le Rav Menaché Moreno (beit hora’a « Halakha lema’assé » du Rav Ofir Malka) répond que la lecture de Vezot haBerakha faite dans le Tikoun peut compter pour l’une des deux lectures du texte, mais qu’il vaut mieux lire chaque verset en Chnayim mikra, et de jour plutôt que de nuit.  
   *Sources : Michna Beroura 285:18 ; Kaf ha’Haïm 285:29 ; Choul’han Aroukh haRav O.H. 285:9 ; Ben Ich ’Haï, 1re année, Vezot haBerakha §15 ; Kitsour Yalkout Yossef 285:19 ; Kitsour Yalkout Yossef 285:9 ; Halakha lema’assé (Rav O. Malka), question 142* (`chm-31`)

