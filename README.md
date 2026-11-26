# Shnayim Mikra — שניים מקרא

Application (et bot) pour encourager à faire **Shnayim Mikra ve'Ehad Targoum** chaque semaine : lire la paracha deux fois et une fois le Targoum Onkelos.

> « Celui qui termine ses parachiyot avec la communauté, ses jours et ses années sont prolongés. » — d'après Berakhot 8a

## Statut

Version de test : une application web (`web/`) embarquée dans un APK Android. Depuis le 26/11/2026, elle contient hors connexion toute la Torah, le Targoum Onkelos, les haftarot selon le rite et un recueil de 31 halakhot ([détail](docs/10-lectures-haftara-halakhot.md)).

## Lancer et tester

```sh
npm install                      # dépendances de test (hebcal)
npm test                         # 40 tests, sans réseau
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
- [x] Relecture indépendante des 31 halakhot, citation par citation : faite par quatre relecteurs automatiques ; 15 halakhot corrigées. Reste à faire confirmer huit points par un rav ([liste](docs/10-lectures-haftara-halakhot.md#à-faire-confirmer-par-un-rav-ou-par-le-propriétaire)).
- [x] Réponses du Rav Binyamin 'Hota : deux réponses écrites ajoutées (halakhot 5 et 6) ; les autres sont en vidéo seulement.
- [x] Licence du Kitsour Yalkout Yossef : vérifiée (CC BY-NC-SA 2.5, sans autorisation à demander). Deux décisions reviennent au propriétaire : rester non commercial, et le partage à l'identique du recueil.
- [ ] Rédiger le contexte des haftarot (cahier, section 6), puis le faire vérifier : socle fait, rédaction en cours.
- [ ] Trancher, avec un rav, les usages séfarades laissés de côté faute de source dans le Kitsour Yalkout Yossef. Ils changent la haftara affichée ici :
  - « השמים כסאי » et « מחר חדש » au Chabbat 'Hanouka Roch 'Hodech ;
  - Chekalim à Roch 'Hodech Adar ;
  - ha'Hodech la veille d'un Roch 'Hodech dimanche.
- [ ] Dire si l'on veut les variantes 'Habad et les Meguilot.
- [ ] Proposer Vézot haBérakha en Chnayim mikra à Hochaana Rabba (halakha 31) : aucune semaine ne la montre aujourd'hui.

Trois questions du cahier ne concernent que la lecture du jour, restée dans My Hitbodedut : Mikha 7:18-20 au 9 Av à Min'ha, l'usage nord-africain de 'Hol hamoed en diaspora, la lecture du soir de Sim'hat Torah.
