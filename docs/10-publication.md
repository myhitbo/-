# 10. Publication sur Google Play — marche à suivre

## Ce qui est prêt dans le projet
- L'app cible Android 16 (API 36), comme l'exige Google Play depuis le 31 août 2026.
- La compilation automatique (GitHub Actions) vérifie chaque envoi et, sur la branche `main`, publie l'APK de test.
- Dès que la clé de signature est configurée (étape 1), elle produit aussi le fichier pour Google Play : `shnayim-mikra-google-play-aab`, à télécharger dans l'onglet Actions, sur la page de la compilation.
- Le numéro de version augmente tout seul à chaque compilation (`1.0.N`).

## Étape 1 — Créer la clé de signature (une seule fois)
La clé prouve que les mises à jour viennent bien de vous. **Gardez le fichier et les mots de passe en lieu sûr** : sans eux, plus de mise à jour possible sous la même signature.

Sur un ordinateur où Java est installé :

```
keytool -genkeypair -v -keystore shnayim-mikra.jks -alias shnayim -keyalg RSA -keysize 2048 -validity 10000
```

Puis, sur GitHub : dépôt → Settings → Secrets and variables → Actions → New repository secret. Créer quatre secrets :

| Nom | Valeur |
|---|---|
| `SM_KEYSTORE_BASE64` | le fichier encodé : résultat de `base64 -w0 shnayim-mikra.jks` |
| `SM_KEYSTORE_PASSWORD` | le mot de passe du fichier |
| `SM_KEY_ALIAS` | `shnayim` |
| `SM_KEY_PASSWORD` | le mot de passe de la clé |

Avec la clé, l'APK de test garde aussi la même signature d'une version à l'autre : il se met à jour sans désinstaller.

## Étape 2 — Créer l'app dans Google Play Console
Avec le compte d'organisation :
1. Créer une application : nom « Shnayim Mikra », application gratuite.
2. Activer la signature d'application par Google Play (proposée par défaut) et envoyer le fichier AAB d'abord en **test interne**.
3. L'identifiant de l'app est `org.shnayimmikra.app`. **Il devient définitif à la première publication** : pour en changer (par exemple pour le nom de domaine de l'organisation), le dire avant.

## Étape 3 — Renseigner la fiche
- **Icône 512 × 512** : `docs/icone-google-play-512.png` (dessin « bleu nuit »).
- **Nom, descriptions, bannière et captures d'écran** : tout est dans `docs/fiche-google-play/` — les textes à copier dans `textes.md` (français, anglais, espagnol, hébreu), la bannière `banniere-1024x500.png`, et six captures par langue dans `captures/`. Le tounsi n'a pas de fiche : Google Play ne le propose pas.
- **Catégorie** : Livres et références. **Classification du contenu** : questionnaire à remplir (aucun contenu sensible).
- **Sécurité des données** : l'app ne demande pas de compte, ne collecte et ne partage aucune donnée personnelle ; la progression et les réglages restent sur le téléphone. Seul échange réseau : le téléchargement des textes sur sefaria.org.
- **Politique de confidentialité** : adresse d'une page publique. La page est prête : `docs/confidentialite.html` (voir plus bas pour la mettre en ligne).
- **Dons** : le bouton ouvre la page de don de l'organisme hors de l'app. Google l'autorise pour un organisme exonéré d'impôt : fournir le justificatif dans la déclaration sur les paiements.
- **Notifications** : l'app demande l'autorisation pour le rappel de lecture. Elle déclare aussi l'accès « Alarmes et rappels » (`SCHEDULE_EXACT_ALARM`), pour que le rappel choisi par l'utilisateur arrive à l'heure ; si Google Play pose la question, c'est l'usage à indiquer.

## Étape 4 — Vérifier sur un vrai téléphone, puis publier
À contrôler avec la version de test avant de passer en production :
- le rappel arrive à l'heure choisie, et pas pendant Shabbat ;
- les barres du haut et du bas ne recouvrent pas l'app (Android 15 et 16) ;
- le bouton Retour revient à l'écran précédent ;
- l'impression et « Enregistrer en PDF » ;
- les liens (don, sources) s'ouvrent dans le navigateur.

## Politique de confidentialité
La page est prête : `docs/confidentialite.html`, en français, anglais, espagnol et hébreu. C'est un fichier unique, sans dépendance : il peut être déposé tel quel sur n'importe quel site.

Elle dit ce que fait réellement l'app : pas de compte, aucune donnée collectée, réglages et progression gardés sur le téléphone (et dans la sauvegarde Android de l'utilisateur si elle est activée), textes téléchargés sur sefaria.org, ville choisie dans une liste sans localisation, rappel préparé sur le téléphone, don et chaîne WhatsApp ouverts hors de l'app. **Si l'app change sur l'un de ces points, mettre la page à jour, avec sa date.**

Deux façons de la mettre en ligne :
1. **Sur GitHub (gratuit, sans autre site)** — une seule fois, sur la page du projet : Settings → Pages → Source : « GitHub Actions ». La tâche « Site public » la publie ensuite à chaque modification. Adresse : `https://myhitbo.github.io/-/`. Le même réglage met en ligne la page des messages des chaînes WhatsApp (voir `docs/11-chaine-whatsapp.md`).
2. **Sur le site de l'association** — déposer le fichier `confidentialite.html` à côté de la page de don.

L'adresse obtenue est à coller dans Google Play Console (Contenu de l'application → Règles de confidentialité).

## Ce qu'il reste à fournir
- L'adresse de la page de don (à mettre dans `web/config.js`).
- L'adresse de chaque chaîne WhatsApp (une par langue), une fois créée (à mettre dans `web/config.js`), et les divré Torah du vendredi (`chaine/dvar-torah/`) : voir `docs/11-chaine-whatsapp.md`.
- Après la publication : l'adresse de l'app sur Google Play, à mettre dans `chaine/config.json` pour que les messages des chaînes y renvoient.
- La relecture du tounsi par un locuteur natif : le fichier `docs/traductions-a-relire.csv` s'ouvre dans un tableur, avec une colonne « Correction » à remplir. Une relecture de l'hébreu, de l'anglais et de l'espagnol est aussi souhaitable.

## Déjà fourni
- L'adresse e-mail de contact : myhitbodedut26@gmail.com (politique de confidentialité, fiche Play, lettre à l'éditeur du Houmash).
- L'organisme éditeur : Association Hachiveinou Letoratekha.
- L'icône : dessin « bleu nuit ». Source : `android/icone/icone.svg` ; tous les formats sont refaits par `node tools/make_icons.js android/icone/icone.svg`.
