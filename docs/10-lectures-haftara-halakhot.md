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
| Tests | `test/` : `npm install` puis `npm test` (36 tests) |
| Vecteurs de parité | `test/vecteurs_lecture_torah.json`, régénérés par `tools/vecteurs_lecture.mjs` |
| Licences | `web/licences/BSD-2-hebcal-leyning.txt`, `web/vendor/LICENCES.txt` |

## Contrôles faits ici

- Les deux outils Python ont été relancés depuis leurs sources : les trois fichiers de données sortent **identiques** à ceux de l'archive.
- Le moteur donne la même réponse qu'hebcal chaque jour de septembre 2025 à décembre 2031, sauf les écarts voulus, comptés par catégorie. Les vecteurs de parité de l'archive passent sans changement.
- `construction.py --verifie` a relu les 135 références des 31 halakhot à leur source : toutes les citations y sont. Ce contrôle dit que la citation existe, pas que le résumé français est fidèle.
- Les écrans ont été ouverts dans Chromium depuis un fichier, comme dans l'APK : accueil, lecteur, haftara, halakhot, réglages, impression.
- Non fait : compiler l'APK. La compilation se fait sur GitHub, à la fusion dans `main`.

## Prochaines étapes (cahier, section 8)

Voir la liste à jour dans le [README](../README.md#prochaines-étapes).
