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
- **Écran « Halakhot »** : les 31 halakhot, filtrées par rite, avec les sources en hébreu repliées sous chaque halakha.
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
| Tests | `test/` : `npm install` puis `npm test` (40 tests) |
| Vecteurs de parité | `test/vecteurs_lecture_torah.json`, régénérés par `tools/vecteurs_lecture.mjs` |
| Licences | `web/licences/BSD-2-hebcal-leyning.txt`, `web/vendor/LICENCES.txt` |

## Contrôles faits ici

- Les deux outils Python ont été relancés depuis leurs sources : les trois fichiers de données sortent **identiques** à ceux de l'archive.
- Le moteur donne la même réponse qu'hebcal chaque jour de septembre 2025 à décembre 2031, sauf les écarts voulus, comptés par catégorie. Les vecteurs de parité de l'archive passent sans changement.
- `construction.py --verifie` a relu les 141 références des 31 halakhot à leur source : toutes les citations y sont. La fidélité du français a été relue à part (voir plus bas).
- Les écrans ont été ouverts dans Chromium depuis un fichier, comme dans l'APK : accueil, lecteur, haftara, halakhot, réglages, impression.
- Non fait : compiler l'APK. La compilation se fait sur GitHub, à la fusion dans `main`.

## Halakhot : la relecture indépendante (26/11/2026)

Quatre relecteurs automatiques indépendants (aucun humain, aucun rav) ont relu les 31 halakhot contre leurs sources, chacun sur un quart du recueil, sans connaître le travail du rédacteur. Chacun a lu en entier chaque source citée.

| Résultat | Nombre |
|---|---|
| Halakhot jugées conformes | 16 |
| Halakhot corrigées | 15 |
| Citations hébraïques fausses ou mal référencées | 0 |
| Contresens | 0 |

Ce qui a été corrigé :

- **Une erreur de référence** (halakha 2) : 'Hazon Ovadia, page 328 et non 228.
- **Deux attributions** : le Rav Azoulay parle de la Torah écrite la nuit, non du targoum (halakha 9) ; le Kaf ha'Haïm cite le Kitsour Chla, non le Chla (halakha 26).
- **Des conditions oubliées** : « a posteriori » (6), « a priori » (10), « le mieux est » (8), « il semble » (2), « il convient » (24, 26).
- **Qui dit quoi** : le dernier verset (10), Rachi et le targoum (17, 18), 'Houmach sans targoum (19), les te'amim du targoum (21), la bénédiction dans le séfer Torah (22), la lecture pendant l'office (25), Yom Tov (30).
- **Des citations hébraïques coupées** qui perdaient une condition ou un avis : halakhot 5, 21, 23, 24, 25, 31.
- **La table de vérification** ne garde plus que les repères des réponses protégées (25 mots au plus), au lieu du passage entier.

Après correction, `construction.py --verifie` a relu les 141 références : toutes les citations sont dans leurs sources.

### À faire confirmer par un rav ou par le propriétaire

1. **Halakha 2, rite « tous »** (les femmes sont dispensées) : les sources lues sont séfarades ; l'étiquette repose sur le renvoi de Hidabroot au Mishné Halakhot 6:60, non lu.
2. **Halakhot 13 et 19, rite « tous »** : elles rapportent des avis nommés de chaque rite plutôt qu'un accord.
3. **Halakha 23** : « סברא הראשונה » du Choul'han Aroukh haRav 285:8 est lu comme l'avis qui compte l'écoute pour une lecture.
4. **Halakha 26** : l'abréviation « קשל"ה » est lue « Kitsour Chla » ; « והכי נקטינן » est attribué au Yafé laLev d'après le seul Kaf ha'Haïm.
5. **Deux coquilles probables de l'édition numérique du Kaf ha'Haïm**, affichées telles quelles : « כ"י כתבו » (285:14, sans doute « כי ») et « פסוק אחר » (285:15, peut-être « אחד »).
6. **Le titre « Rav »** des auteurs de Hidabroot : les pages sont signées « הלל מאירס » et « בנימין שמואלי », sans titre, sous la rubrique « שאל את הרב ».
7. **Ouvrages cités de seconde main**, non lus : Ma'assé Rav, Maté Yehouda, Kol Bo, Séder haYom, Korban Chabbat, Birké Yossef, Yafé laLev, Knesset haGuedola, Mishné Halakhot, 'Hazon Ovadia.
8. **Le Kitsour Yalkout Yossef** n'a été contrôlé que contre la copie Torat Emet, pas contre l'imprimé.

## Rav Binyamin 'Hota

Deux réponses de sa rubrique « הלכה ב-60 שניות » (Kikar haChabbat) ont un texte écrit sur la page. Elles sont résumées et référencées :

- **Halakha 5** : lire Chnayim mikra accomplit la préparation du Chabbat « par la parole » (13/06/2025).
- **Halakha 6** : le dernier délai de l'année est la lecture de la Torah à la synagogue, à Sim'hat Torah (12/10/2025).

Ses autres réponses sur le sujet sont en vidéo ou en enregistrement seulement (Kikar haChabbat 2022-2023 et 13/02/2026, kollel 'Hazon Ovadia, Kol haLachon). Rien n'en est tiré : un sous-titrage automatique n'est pas un texte fiable à attribuer à un rav. Ses livres « כי בו שבת » ne sont pas en ligne.

## Licence du Kitsour Yalkout Yossef

Vérifiée à la source : la page de licence de Torat Emet (`toratemetfreeware.com/contents/copyrights2.html`, lue le 26/11/2026). Tous les livres de la base, hors Wikisource, sont sous **CC BY-NC-SA 2.5** ; on peut les diffuser **sans demander d'autorisation**, à trois conditions.

| Condition | Dans ce projet |
|---|---|
| Mention des droits et des conditions de la licence, bien visibles | Fait : introduction du recueil, Réglages › Sources et licences, `web/licences/CC-BY-NC-SA-2.5.txt` |
| Usage non commercial | Tenu aujourd'hui : application gratuite, sans publicité. **À décider par le propriétaire** : une licence payante pour synagogues ou écoles ([06](06-autres-aspects.md), § 8) ne serait pas compatible avec ces citations |
| Partage à l'identique des œuvres dérivées | **À décider par le propriétaire** : placer le recueil des halakhot sous la même licence, ou retirer les citations mot pour mot du Yalkout Yossef |

Le Choul'han Aroukh haRav (saisie Kehot, CC BY-NC) pose la même condition d'usage non commercial.

## Contexte des haftarot

- **Socle** : `data/contexte_haftarot.json`, le contrôle `tools/contexte_haftarot.mjs` (`--sources` relit chaque citation sur Sefaria), l'encadré « Contexte de la haftara » replié sous la haftara de l'accueil.
- **Portée** : l'application peut afficher 105 haftarot (origine et premier passage, tous rites confondus), soit environ 70 contextes à écrire.
- **État** : voir `_meta.etat` dans le fichier et la sortie du contrôle.

## Prochaines étapes (cahier, section 8)

Voir la liste à jour dans le [README](../README.md#prochaines-étapes).
