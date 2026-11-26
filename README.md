# Shnayim Mikra — שניים מקרא

Application (et bot) pour encourager à faire **Shnayim Mikra ve'Ehad Targoum** chaque semaine : lire la paracha deux fois et une fois le Targoum Onkelos.

> « Celui qui termine ses parachiyot avec la communauté, ses jours et ses années sont prolongés. » — d'après Berakhot 8a

## Statut

Version de test : une application web (`web/`) embarquée dans un APK Android. Depuis le 26/11/2026, elle contient hors connexion toute la Torah, le Targoum Onkelos, les haftarot selon le rite et un recueil de 31 halakhot ([détail](docs/10-lectures-haftara-halakhot.md)).

## Lancer et tester

```sh
npm install                      # dépendances de test (hebcal)
npm test                         # 36 tests, sans réseau
node tools/construit_donnees.js  # écrit web/data/ ; puis ouvrir web/index.html
```

L'APK de test est compilé par GitHub Actions à chaque fusion dans `main` et publié dans les Releases.

## Documents

| # | Document | Statut |
|---|---|---|
| 1 | [Motivation : freins et leviers](docs/01-motivation.md) | Réflexion |
| 2 | [Cadrage produit](docs/02-cadrage.md) | Validé |
| 3 | [Lecteur — version 1](docs/03-lecteur-v1.md) | Validé |
| 4 | [Bot WhatsApp / Telegram — version 1](docs/04-bot-v1.md) | Validé |
| 5 | [Directions artistiques](docs/05-directions-artistiques.md) | En choix |
| 6 | [Autres aspects de l'app](docs/06-autres-aspects.md) | Propositions |
| 7 | [Mise en place de 21st.dev UI Build](docs/07-setup-21st-dev.md) | Guide |
| 8 | [Valeur pratique](docs/08-valeur-pratique.md) | Dans l'app |
| 9 | [Cahier de reprise (venu de My Hitbodedut)](docs/09-cahier-de-reprise.md) | Référence |
| 10 | [Lectures, haftara et halakhot repris ici](docs/10-lectures-haftara-halakhot.md) | Dans l'app |

Les maquettes visuelles (canevas de design) sont tenues à part, hors de ce dépôt.

## Prochaines étapes

Reprises de la section 8 du [cahier de reprise](docs/09-cahier-de-reprise.md).

- [x] Dépôt et plateformes : ce dépôt, application web et APK Android. Rien sur iPhone pour l'instant.
- [ ] Faire vérifier les 31 halakhot par un relecteur indépendant, citation par citation. Fait : le script a relu les 135 références à leur source.
- [ ] Chercher les réponses du Rav Binyamin 'Hota et les ajouter au recueil.
- [ ] Revérifier la licence du Kitsour Yalkout Yossef pour ce projet.
- [ ] Rédiger le contexte des haftarot (cahier, section 6), puis le faire vérifier.
- [ ] Trancher les usages séfarades laissés de côté faute de source dans le Kitsour Yalkout Yossef.
- [ ] Confirmer Mikha 7:18-20 après « שובה » au 9 Av à Min'ha chez les Edot.
- [ ] Dire si les communautés nord-africaines de France ont un usage propre pour 'Hol hamoed en diaspora.
- [ ] Dire si l'on veut les variantes 'Habad, la lecture du soir de Sim'hat Torah, les Meguilot.
- [ ] Proposer Vézot haBérakha en Chnayim mikra à Hochaana Rabba (halakha 31) : aucune semaine ne la montre aujourd'hui.
