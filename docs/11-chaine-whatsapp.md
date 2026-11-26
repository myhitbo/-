# 11. Chaîne WhatsApp de l'association

## Décision (26 novembre 2026)
Le bot WhatsApp décrit dans le [document 4](04-bot-v1.md) est remplacé, pour l'instant, par une **chaîne WhatsApp** tenue par l'association.

| Solution | Coût | Pourquoi oui ou non |
|---|---|---|
| Bot WhatsApp officiel (Meta) | Payant | Depuis le 1er octobre 2026, Meta fait payer chaque message envoyé par un bot ; même les réponses sont payantes au-delà de 1 000 par mois. Ordre de grandeur vers la France : 0,03 à 0,09 $ par message, soit environ 0,80 à 2,20 $ par mois et par abonné pour un message chaque matin (chiffres de prestataires, à confirmer sur le tarif de Meta). **Écarté.** |
| Bot WhatsApp non officiel | Gratuit | Contraire aux règles de WhatsApp : le numéro peut être bloqué définitivement, sans préavis. **Écarté.** |
| **Chaîne WhatsApp** | Gratuit | Autorisé par WhatsApp, sans limite d'abonnés. **Retenu.** |
| Bot Telegram | Gratuit | Autorisé, permettrait tout le bot prévu. Possible plus tard, pour ceux qui utilisent Telegram. |

Ce qu'une chaîne ne fait pas :
- Le message est **le même pour tous** : pas d'heure choisie ni de rythme personnel. Ces réglages restent dans l'app, avec sa notification.
- Les abonnés ne répondent pas : ils **réagissent avec ✅**. Le nombre de ✅ sous chaque message montre combien ont lu.
- WhatsApp n'a **pas d'envoi automatique** pour les chaînes : une personne colle le message chaque matin. Tout le reste est préparé automatiquement.

## Ce que la chaîne publie

| Jour | Message |
|---|---|
| Dimanche | Annonce de la nouvelle paracha (référence, durée totale) et alya du jour |
| Lundi à jeudi | Alya du jour, versets et durée |
| Jeudi soir | Second message : ce qui reste pour vendredi, rappel de l'impression pour Chabbat |
| Vendredi | Shishi et Shvi'i, heure d'allumage des bougies, dvar Torah de la semaine, « Chabbat Chalom » |
| Chabbat et fêtes | Rien |

- Les sept alyot sont réparties sur les jours où l'on peut publier. Si une fête tombe dans la semaine, les derniers jours reçoivent une alya de plus.
- La veille d'une fête : heure d'allumage et salutation (« 'Hag Saméa'h », « Chana Tova », « Gmar 'Hatima Tova »).
- Vezot Haberakha : un message de rattrapage, puis une alya par jour pendant les sept derniers jours avant Sim'hat Torah.
- Les durées sont celles de l'app, à la vitesse de lecture normale.

Exemple (jeudi matin) :
```
📖 *Vayichla'h* — Hamishi (34:1 – 35:11) · environ 12 min
✅ Réagis à ce message quand c'est fait
```

## Mise en place (une seule fois)
1. **Créer la chaîne** : dans WhatsApp, onglet Actus → Chaînes → « + » → Créer une chaîne. Nom proposé : « Shnayim Mikra — שניים מקרא ». Image : `docs/icone-google-play-512.png`. Pour plusieurs langues, créer une chaîne par langue.
2. **Mettre la page des messages en ligne** : sur la page GitHub du projet, Settings → Pages → Source : « GitHub Actions » (c'est le même réglage que pour la politique de confidentialité). La page est alors à l'adresse `https://myhitbo.github.io/-/chaine/`.
3. **Garder cette page sous la main** : l'ouvrir sur le téléphone de la personne qui publie, puis « Ajouter à l'écran d'accueil ».
4. **Donner l'adresse de la chaîne** (dans la chaîne, toucher son nom, puis « Copier le lien »). Elle va dans `web/config.js` (`channelUrl`) : un bouton « Rejoindre la chaîne » apparaît alors dans les Réglages de l'app.
5. **Après la publication sur Google Play** : mettre l'adresse de l'app dans `chaine/config.json` (`appUrl`). La ligne « 🔗 Lire dans l'app » s'ajoute alors à chaque message.

## Chaque jour (une minute)
1. Ouvrir la page des messages.
2. Choisir la langue. Le calendrier (diaspora ou Israël) est déjà choisi selon la langue ; on peut le changer.
3. Toucher **Copier**.
4. Dans WhatsApp, ouvrir la chaîne, coller, envoyer.

Le jeudi, la page montre deux messages : un pour le matin, un pour le soir. Les jours de Chabbat et de fête, elle indique qu'il n'y a rien à publier. Les messages des jours suivants sont visibles plus bas.

## Dvar Torah du vendredi
L'association fournit les textes. Ils sont rangés dans `chaine/dvar-torah/`, un fichier par langue (`fr.md`, `he.md`, `en.md`, `es.md`, `tn.md`), avec un titre par paracha : le texte se colle sous le titre. Une paracha sans texte : le message du vendredi part sans dvar Torah. Pour une paracha double, les deux textes se suivent.

## Réglages
- `chaine/config.json` : adresse de l'app, villes dont on donne l'heure d'allumage pour chaque langue, calendrier proposé par défaut pour chaque langue.
- `chaine/textes.js` : la formulation des messages, dans les cinq langues. Le tounsi est un brouillon : il figure dans la feuille de relecture `docs/traductions-a-relire.csv` (lignes « chaine. »).
- Pour voir les messages sans les mettre en ligne : `node tools/fetch_sefaria.js`, puis `node tools/make_channel.js _site/chaine`, et ouvrir `_site/chaine/index.html`.

## Mise à jour automatique
- La tâche « Site public » prépare les messages de la semaine passée et des quatre suivantes. Elle tourne le dimanche et le mercredi, et à chaque modification des textes.
- Si les messages préparés s'arrêtent dans moins de trois jours, la page affiche un avertissement.
- GitHub suspend les tâches programmées d'un projet resté 60 jours sans modification. Pour la relancer : onglet Actions → « Site public » → Enable workflow, puis Run workflow.

## Sources
- [Tarifs de la plateforme WhatsApp Business (Meta)](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)
- [Tarification des messages hors modèle, à partir du 1er octobre 2026 (Meta)](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages/)
- [Limites de l'API des bots Telegram](https://core.telegram.org/bots/faq)
