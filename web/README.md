# Application web

`index.html` charge, dans l'ordre :
- `data/text.js` — textes des semaines. Remplacé au moment du build par `tools/fetch_sefaria.js` (textes de Sefaria). Fichier de secours : `null` → textes d'exemple.
- `sefaria.js` — récupération des textes sur Sefaria (sert au build et à la mise à jour en ligne).
- `globals.js` — données partagées (semaine en cours, alya du jour, heure d'allumage, progression, impression).
- `runtime.js` — moteur des écrans, navigation et réglages (enregistrés sur le téléphone).
- `screens/_shared.js` — thèmes de couleurs et langues, communs aux écrans.
- `screens/<nom>.js` — un fichier par écran : le gabarit HTML (`tpl`) puis sa logique (`make`).

L'APK est compilé par GitHub Actions (`.github/workflows/android.yml`), qui copie ce dossier tel quel dans l'application.
