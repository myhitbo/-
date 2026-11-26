# Application web (version de test)

Écrans générés à partir des maquettes V2, puis tenus à la main. `index.html` charge, dans l'ordre :

- `vendor/kosher-zmanim-0.9.0.min.js` — le calendrier juif (LGPL-3.0, fichier non modifié ; `vendor/LICENCES.txt`).
- `lecture.js` — le moteur des lectures : la paracha de la semaine, ses montées, son maftir et sa haftara selon le lieu et le rite.
- `donnees.js` — le chargeur des données embarquées (`SM_DATA`, `SM_DONNEES`).
- `data/lecture.js` — les lectures. Le texte (`data/texte/<Livre>.js`), le Targoum (`data/targoum/<Livre>.js`) et les halakhot (`data/halakhot.js`) sont chargés à la demande.
- `sefaria.js` — seulement le Targoum Yerouchalmi des versets sans Targoum, en ligne.
- `globals.js` — données partagées (semaines, haftara, échéances, progression, impression).
- `runtime.js` — moteur des écrans, navigation et réglages (enregistrés sur le téléphone).
- `screens.js` — les écrans des maquettes ; `ecrans.js` — les écrans ajoutés (halakhot).

`data/` n'est pas suivi par git : il est écrit par `node tools/construit_donnees.js` à partir de `../data/` (sans réseau). Sans lui, l'application affiche « Textes absents ».

Tout est en scripts classiques, sans module : l'application s'ouvre depuis un fichier (`file://`), comme dans la WebView de l'APK.

L'APK de test est compilé par GitHub Actions (`.github/workflows/android.yml`).
