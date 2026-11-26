# 2. Cadrage produit (validé)

## Public
Tout public, toutes nationalités.
- Interface en **6 langues** : français, hébreu, anglais, espagnol, arabe tunisien (tounsi), arabe marocain (darija).
  - Hébreu et arabe : interface entièrement inversée (droite à gauche).
  - Arabe tunisien et marocain : dialectes peu standardisés à l'écrit → traductions par des locuteurs natifs de chaque communauté, à faire relire. Écriture : **le tounsi s'écrit en lettres hébraïques** (judéo-arabe, décidé le 26/11/2026) ; pour la darija, le choix reste à confirmer.
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
