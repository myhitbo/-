# Application web (version de test)

Écrans générés à partir des maquettes V2. `index.html` charge :
- `data/text.js` — paracha de la semaine. Remplacé au moment du build par `tools/fetch_sefaria.py` (textes de Sefaria). Fichier de secours : `null` → textes d'exemple.
- `globals.js` — données partagées (paracha, alya du jour).
- `runtime.js` — moteur des écrans, navigation et réglages (enregistrés sur le téléphone).
- `screens.js` — les écrans.

L'APK de test est compilé par GitHub Actions (`.github/workflows/android.yml`).
