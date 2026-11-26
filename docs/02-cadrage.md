# 2. Cadrage produit (validé)

## Public
Tout public, toutes nationalités.
- Interface en **5 langues** : français, hébreu, anglais, espagnol, tounsi (judéo-arabe tunisien). La darija, d'abord prévue, a été retirée le 26/11/2026.
  - Hébreu et arabe : interface entièrement inversée (droite à gauche).
  - Tounsi : dialecte peu standardisé à l'écrit → traduction à faire relire par un locuteur natif. Écriture (décidé le 26/11/2026) : **en lettres hébraïques** (judéo-arabe).
  - Espagnol : **variante d'Amérique latine** (validé).
  - Noms des parachiyot et des alyot adaptés à chaque langue (Vayétsé, Vayetzei, ויצא…).
  - Police d'interface couvrant latin, hébreu et arabe (ex. Heebo + Noto Sans Arabic).
- Niveaux réglables : le lecteur à l'aise lit sans aide, le débutant a plus d'accompagnement.
- Calendrier Israël / diaspora géré automatiquement selon la localisation.

## Plateformes
**App + bot**, avec un compte partagé.
- **Bot (WhatsApp, Telegram)** : porte d'entrée sans effort, envoie l'alya du jour et permet de la cocher.
- **App** : lecteur, groupes, historique de l'année, statistiques.

## Modes de lecture
Les deux :
- **Lire dans l'app** : verset, verset, Targoum, avec marque-page automatique.
- **« Je l'ai lu dans mon Houmash »** : un bouton par alya, pour ceux qui lisent dans le livre (notamment le Shabbat).

## Première version
1. Lecteur verset, verset, Targoum, découpé par alya du jour → [03-lecteur-v1.md](03-lecteur-v1.md)
2. Bot qui envoie l'alya chaque matin et permet de la cocher → [04-bot-v1.md](04-bot-v1.md)
3. Groupes (famille, synagogue) avec la progression de chacun
4. Compteur mondial et vue de l'année

Plus tard : multilingue complet, dédicaces.

## Point technique
Les textes (Torah, Onkelos, Rashi, traductions) sont disponibles via l'API de Sefaria.
