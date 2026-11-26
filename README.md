# Shnayim Mikra — שניים מקרא

Application (et bot) pour encourager à faire **Shnayim Mikra ve'Ehad Targoum** chaque semaine : lire la paracha deux fois et une fois le Targoum Onkelos.

> « Celui qui termine ses parachiyot avec la communauté, ses jours et ses années sont prolongés. » — d'après Berakhot 8a

## Statut

Version de test : une application web (`web/`) embarquée dans un APK Android. Depuis le 26/11/2026, elle contient hors connexion toute la Torah, le Targoum Onkelos, les haftarot selon le rite et un recueil de 83 halakhot ([détail](docs/10-lectures-haftara-halakhot.md)).

## Lancer et tester

```sh
npm install                      # dépendances de test (hebcal)
npm test                         # 41 tests, sans réseau
node tools/construit_donnees.js  # écrit web/data/ ; puis ouvrir web/index.html
```

Dans une session Claude Code cloud, `.claude/hooks/session-start.sh` fait l'installation et écrit `web/data/` au démarrage ; il saute ce qui est déjà fait.

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
- [x] Enrichir le recueil des halakhot : de 31 à 83, d'après tout le siman 285 (Michna Beroura, Kaf ha'Haïm, Kitsour Yalkout Yossef, Aroukh haChoul'han…) et 47 réponses d'aujourd'hui, 3 articles de Halacha Yomit et 3 cours du Rav David Yossef ([détail](docs/10-lectures-haftara-halakhot.md#halakhot--de-31-à-83-26112026)).
- [x] Relecture indépendante des 83 halakhot, citation par citation : faite par neuf relecteurs automatiques ; aucune citation fausse ; 15 halakhot corrigées à la première relecture, 30 à la seconde. Le propriétaire a tranché onze points le 26/11/2026 ([décisions](docs/10-lectures-haftara-halakhot.md#décisions-du-propriétaire-26112026)) ; huit restent à montrer à un rav ([liste](docs/10-lectures-haftara-halakhot.md#ce-qui-reste-à-montrer-à-un-rav)).
- [x] Réponses du Rav Binyamin 'Hota : deux réponses écrites ajoutées (halakhot 10 et 11) ; les autres sont en vidéo seulement.
- [x] Licence du Kitsour Yalkout Yossef : CC BY-NC-SA 2.5, sans autorisation à demander ; le propriétaire a indiqué qu'elle avait déjà été vérifiée dans My Hitbodedut. Elle demande de rester non commercial.
- [ ] « Halakha Beroura » du Rav David Yossef : le siman 285 est au volume 17, qui ne se lit pas en ligne et que le propriétaire n'a pas. Rien n'en est cité ; ses cours hebdomadaires sont repris à la place. À ajouter si le volume devient disponible.
- [x] Halacha Yomit, que le propriétaire n'avait pas nommé : il a décidé de le garder (12 halakhot le citent).
- [ ] Rédiger le contexte des haftarot (cahier, section 6), puis le faire vérifier : 7 contextes écrits et relus sur environ 70.
- [ ] Trancher, avec un rav, les usages séfarades laissés de côté faute de source dans le Kitsour Yalkout Yossef. Ils changent la haftara affichée ici :
  - « השמים כסאי » et « מחר חדש » au Chabbat 'Hanouka Roch 'Hodech ;
  - Chekalim à Roch 'Hodech Adar ;
  - ha'Hodech la veille d'un Roch 'Hodech dimanche.
- [ ] Dire si l'on veut les variantes 'Habad et les Meguilot.
- [ ] Proposer Vézot haBérakha en Chnayim mikra à Hochaana Rabba (halakhot 68, 74 et 75) : aucune semaine ne la montre aujourd'hui.

Trois questions du cahier ne concernent que la lecture du jour, restée dans My Hitbodedut : Mikha 7:18-20 au 9 Av à Min'ha, l'usage nord-africain de 'Hol hamoed en diaspora, la lecture du soir de Sim'hat Torah.
