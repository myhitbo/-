# Valeur pratique — ce que l'app fait pour faciliter Shnayim Mikra

## Déjà dans l'app (version de test)

### Verset sans Targoum : 3 fois, ou Targoum Yerouchalmi
- Un verset est « sans Targoum » quand Onkelos est absent ou identique à l'hébreu (seulement des noms), et toujours Bamidbar 32:3 (« Atarot ve-Divon », Berakhot 8a).
- Réglage « Verset sans Targoum » : lire l'hébreu 3 fois / lire le Targoum Yerouchalmi / les deux (par défaut).
- Le Targoum Yerouchalmi est pris sur Sefaria (« Targum Jerusalem », sinon « Targum Jonathan »).
- Dans le lecteur : bloc « 3ᵉ lecture · pas de Targoum » et/ou bloc « Targoum Yerouchalmi ». Sur la feuille imprimée : ✱.
- Présentation et choix par défaut validés par un rav.

### Échéances et rattrapage (Choul'han Aroukh O.H. 285:4)
- Objectif affiché : finir avant Chabbat, avec l'heure d'allumage et un compte à rebours.
- Vendredi, si ce n'est pas fini : lien pour imprimer le reste et le lire Chabbat matin, avant le repas.
- Après Chabbat : carte « À rattraper », jusqu'à mardi au coucher du soleil.
- Ensuite : carnet « À compléter avant Sim'hat Torah » (22 Tichri en Israël, 23 en diaspora).
- Progression enregistrée par semaine (clé = date du Shabbat). Une alya lue jusqu'au bout dans le lecteur est comptée automatiquement.

### Heure d'allumage réelle
- Calcul local du coucher du soleil (sans réseau), pour 40 villes en Israël, en France, en Europe et dans les Amériques.
- Coucher du soleil moins 40 min à Jérusalem, 30 à Haïfa, 20 dans les autres villes d'Israël et 18 en diaspora. Les minutes sont affichées. Validé par un rav.

### Imprimer le reste pour Chabbat
- Écran Imprimer : « Ce qu'il me reste » ou « Toute la paracha », avec le nombre de pages estimé.
- Feuille A4 : chaque verset puis son Targoum, par alya.
- Sur Android, la fenêtre d'impression propose aussi « Enregistrer en PDF ».

### Rythmes et ordres de lecture
- Quatre rythmes, au choix à l'accueil et dans les Réglages : une alya par jour ; toute la paracha d'un coup (jour au choix) ; 2 séances (lundi, jeudi) ou 3 (dimanche, mardi, jeudi) ; libre.
- Le bouton principal ouvre la prochaine séance : « Lire Rishon », « Lire Rishon – Shlishi », « Lire la paracha » ou « Lire la suite ».
- Retard : si des séances prévues avant aujourd'hui ne sont pas lues, l'accueil indique le nombre d'alyot à rattraper (jamais en rythme libre).
- Quatre ordres : verset, verset, Targoum ; par paragraphe (petou'ha ou setouma) ; par alya ; toute la séance deux fois puis tout son Targoum. Dans les lectures groupées, un titre annonce chaque passage (« Rishon · 2ᵉ lecture »).
- Les fins de paragraphe viennent du texte de Sefaria (marques {פ} et {ס}) ; un paragraphe ne chevauche jamais deux alyot.
- Une séance est comptée quand on arrive au bout du texte, à la main comme en défilement automatique. Dans une séance de plusieurs alyot lues à la suite, chaque alya est comptée dès qu'on entre dans la suivante.

### Vitesse de lecture et durées
- Tout part du nombre de mots à lire et de la vitesse choisie dans le lecteur : à ×1, 160 mots à la minute pour le texte hébreu ; le Targoum est lu 20 % plus lentement par défaut (réglable : même vitesse, −20 %, −40 %).
- Huit vitesses, de ×0,5 à ×3 (80 à 480 mots à la minute). La vitesse et le réglage du Targoum sont enregistrés.
- Défilement automatique : chaque bloc met exactement son temps de lecture à passer sous la ligne de lecture, quelle que soit la taille du texte ou la largeur de l'écran.
- Le même calcul donne le temps restant dans le lecteur, la durée de chaque alya, la lecture restante de l'accueil, les durées des rappels et de la feuille imprimée.
- Avant : le défilement avançait en pixels par seconde (environ 100 mots à la minute en taille normale, 49 en grande taille) et les durées comptaient 24 secondes par verset, quelle que soit sa longueur.

### Rappel de lecture (notification Android)
- Réglage dans l'accueil de bienvenue et dans les Réglages : interrupteur et heure (07:30 par défaut).
- Un rappel par jour où une séance est prévue et pas encore lue ; les séances en retard s'y ajoutent (« dont 2 alyot en retard »). En rythme libre : un rappel par jour tant que la paracha n'est pas finie.
- Jamais pendant Shabbat ni les fêtes, de l'allumage des bougies à la sortie des étoiles, selon la ville ; second jour de fête en diaspora seulement.
- L'app calcule les rappels des 21 prochains jours et les confie à Android ; la liste est refaite à chaque ouverture et à chaque alya lue.
- Si Android bloque les notifications, les Réglages l'indiquent et proposent de les autoriser.
- L'heure choisie est celle du téléphone (la ville ne sert qu'aux horaires de Shabbat et des fêtes).
- Heure exacte : Android livre le rappel à la minute près quand l'app a l'accès « Alarmes et rappels » (accordé d'office jusqu'à Android 13 ; à autoriser par l'utilisateur à partir d'Android 14, les Réglages le proposent). Sans cet accès, le rappel arrive dans les dix minutes.
- Un rappel arrivé à échéance n'est jamais perdu : si Android a pris du retard et que l'app est rouverte entre-temps, il est affiché à ce moment-là.
- Réglages : la ligne « Prochain rappel » indique quand il arrivera, et le bouton « Tester » envoie une notification tout de suite.

### Six langues
- Français, hébreu, anglais, espagnol (Amérique latine), tounsi, darija : tous les écrans, la feuille imprimée et les rappels.
- Hébreu, tounsi et darija s'affichent de droite à gauche. Les dates suivent la langue ; les noms des parachiyot, des alyot et des villes aussi.
- **Le tounsi est écrit en lettres hébraïques** (judéo-arabe tunisien), y compris les jours et les mois. Conventions : ג׳ pour le j, כ׳ pour le kh, ע׳ pour le gh, ת׳ ד׳ צ׳ ט׳ pour les lettres emphatiques ou interdentales ; les mots hébreux gardent leur orthographe (שבת, פרשה, עליה, תרגום). Outil : `tools/judeo_arabe.js`.
- La darija est pour l'instant en lettres arabes ; les noms des parachiyot et des alyot y sont en lettres hébraïques.
- Tounsi et darija sont des brouillons à faire relire (`docs/traductions-a-relire.csv`).
- Les textes sont dans `web/i18n.js` (français) et `web/i18n/<langue>.js`.

### Écran Année : la vraie progression
- Une paracha est « terminée » quand ses 7 alyot sont lues depuis le dernier Sim'hat Torah ; l'année hébraïque affichée est celle de ce cycle.
- Les semaines passées non terminées sont marquées « à compléter », avec le nombre d'alyot lues.
- L'accueil affiche le même total (« Cette année »).

### Hors ligne
- Les polices sont embarquées dans l'app (plus aucun appel à Google Fonts) : l'hébreu s'affiche de la même façon sans réseau.
- Le seul accès réseau restant est la mise à jour des textes sur Sefaria.

### Israël / diaspora
- Les textes sont construits pour les deux calendriers. Le lieu choisi à l'accueil ou dans les Réglages décide de la paracha.
- Les semaines de fête (pas de paracha ordinaire) sont sautées. Les parachot doubles viennent du calendrier de Sefaria.
- Mise à jour en ligne : l'app retélécharge les semaines depuis Sefaria quand le texte embarqué arrive à sa fin. Si elle est hors ligne, elle garde le texte embarqué.

## Prochaines idées
- Mesurer la vitesse réelle du lecteur (temps passé sur une alya) pour ajuster les durées sans réglage.
- Toucher un mot araméen pour voir son sens (dictionnaire Jastrow sur Sefaria).
- Widget Android.
- Mode Rachi à la place du Targoum : les versets sans Rachi lus 3 fois (Michna Beroura 285:5).
