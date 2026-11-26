# 11. Chaînes WhatsApp de l'association

## Décision (26 novembre 2026)
Le bot WhatsApp décrit dans le [document 4](04-bot-v1.md) est remplacé, pour l'instant, par des **chaînes WhatsApp** tenues par l'association : **une chaîne par langue**.

| Solution | Coût | Pourquoi oui ou non |
|---|---|---|
| Bot WhatsApp officiel (Meta) | Payant | Depuis le 1er octobre 2026, Meta fait payer chaque message envoyé par un bot ; même les réponses sont payantes au-delà de 1 000 par mois. Ordre de grandeur vers la France : 0,03 à 0,09 $ par message, soit environ 0,80 à 2,20 $ par mois et par abonné pour un message chaque matin (chiffres de prestataires, à confirmer sur le tarif de Meta). **Écarté.** |
| Bot WhatsApp non officiel | Gratuit | Contraire aux règles de WhatsApp : le numéro peut être bloqué définitivement, sans préavis. **Écarté.** |
| **Chaînes WhatsApp** | Gratuit | Autorisé par WhatsApp, sans limite d'abonnés. **Retenu.** |
| Bot Telegram | Gratuit | Autorisé, permettrait tout le bot prévu. Possible plus tard, pour ceux qui utilisent Telegram. |

Ce qu'une chaîne ne fait pas :
- Le message est **le même pour tous** les abonnés d'une chaîne : pas d'heure choisie ni de rythme personnel. Ces réglages restent dans l'app, avec sa notification.
- Les abonnés ne répondent pas : ils **réagissent avec ✅**. Le nombre de ✅ sous chaque message montre combien ont lu.
- WhatsApp n'a **pas d'envoi automatique** pour les chaînes : une personne colle le message chaque matin. Tout le reste est préparé automatiquement.

## Les chaînes : une par langue
Cinq chaînes sont prévues. Elles peuvent s'ouvrir l'une après l'autre : les messages de chacune sont déjà préparés.

| Chaîne (nom sur la page de publication) | Langue des messages | Calendrier des lectures | Heures d'allumage données pour | Nom proposé dans WhatsApp |
|---|---|---|---|---|
| Français | français | diaspora | Paris, Marseille, Lyon, Strasbourg, Bruxelles, Montréal | Shnayim Mikra — Français |
| Hébreu | hébreu | Israël | Jérusalem, Tel Aviv, Haïfa, Beer Sheva | שניים מקרא |
| Anglais | anglais | diaspora | New York, Los Angeles, Miami, Londres, Toronto, Melbourne | Shnayim Mikra — English |
| Espagnol | espagnol | diaspora | Buenos Aires, Mexico, Panama, Bogota, Caracas, Santiago | Shnayim Mikra — Español |
| Tounsi (arabe tunisien) | tounsi, en lettres hébraïques | diaspora | Tunis, Djerba, Paris, Marseille, Jérusalem | שניים מקרא — תונסי |

- **Chaque chaîne a ses propres messages** : sa langue, son calendrier (Israël et diaspora ne lisent pas toujours la même paracha, et n'ont pas les mêmes jours de fête), ses villes.
- **Ajouter une chaîne dans une langue déjà prête** (par exemple une chaîne en français pour Israël, avec les heures de Jérusalem et de Tel Aviv) : c'est une ligne de plus dans la liste des chaînes, voir « Réglages ».
- **Ajouter une langue nouvelle** (par exemple l'arabe en lettres arabes) : il faut d'abord traduire les phrases des messages (une vingtaine) et les noms des parachiyot.
- Le tounsi est un brouillon tant qu'il n'a pas été relu : mieux vaut ouvrir cette chaîne après la relecture.

### Qui publie
- Une seule personne peut publier dans toutes les chaînes : la page de publication montre les messages de toutes les chaînes, l'un sous l'autre.
- Ou une personne par langue : le propriétaire d'une chaîne peut inviter d'autres administrateurs (dans les informations de la chaîne ; une quinzaine au maximum). Chacun n'affiche alors que ses chaînes sur la page de publication.

## Ce que chaque chaîne publie

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

Exemple (jeudi matin, chaîne en français) :
```
📖 *Vayichla'h* — Hamishi (34:1 – 35:11) · environ 12 min
✅ Réagis à ce message quand c'est fait
```

## Mise en place
Une seule fois :
1. **Mettre la page de publication en ligne** : sur la page GitHub du projet, Settings → Pages → Source : « GitHub Actions » (c'est le même réglage que pour la politique de confidentialité). La page est alors à l'adresse `https://myhitbo.github.io/-/chaine/`.
2. **Garder cette page sous la main** : l'ouvrir sur le téléphone de chaque personne qui publie, puis « Ajouter à l'écran d'accueil ».

Pour chaque chaîne :
1. **Créer la chaîne** : dans WhatsApp, onglet Actus → Chaînes → « + » → Créer une chaîne. Nom : voir le tableau ci-dessus. Image : `docs/icone-google-play-512.png`.
2. **Donner l'adresse de la chaîne** (dans la chaîne, toucher son nom, puis « Copier le lien »). Elle s'écrit à un seul endroit, `web/config.js` (`channelUrl`, une ligne par chaîne). Deux boutons apparaissent alors :
   - sur la page de publication, « Ouvrir la chaîne » sous chaque message de cette chaîne ;
   - dans les Réglages de l'app, « Rejoindre la chaîne » pour les utilisateurs de cette langue. Les chaînes des autres langues sont proposées juste en dessous (« Dans une autre langue »). Tant qu'aucune chaîne n'a d'adresse, l'app n'affiche rien.

Après la publication sur Google Play : mettre l'adresse de l'app dans `chaine/config.json` (`appUrl`). La ligne « 🔗 Lire dans l'app » s'ajoute alors à chaque message, dans toutes les chaînes.

## Chaque jour (une minute par chaîne)
1. Ouvrir la page de publication. La première fois, toucher dans « Mes chaînes » celles dont on ne s'occupe pas, pour les masquer ; ce choix reste sur le téléphone.
2. Pour chaque chaîne : toucher **Copier**, puis **Ouvrir la chaîne**, coller, envoyer.
3. Revenir sur la page et toucher **Marquer comme publié**. Le compteur en haut indique ce qui reste (« 2 messages publiés sur 5 », puis « Tout est publié pour aujourd'hui ✓ »).

À savoir :
- Le jeudi, chaque chaîne a deux messages : un pour le matin, un pour le soir.
- Les jours de Chabbat et de fête, la page indique qu'il n'y a rien à publier. Un jour de fête en diaspora seulement, les chaînes au calendrier d'Israël ont un message et pas les autres : la page le montre chaîne par chaîne.
- Les messages des jours suivants et de la semaine passée sont visibles plus bas.
- Les coches « publié » restent sur le téléphone de la personne : une autre personne ne les voit pas.

## Dvar Torah du vendredi
L'association fournit les textes. Ils sont rangés dans `chaine/dvar-torah/`, **un fichier par langue** (`fr.md`, `he.md`, `en.md`, `es.md`, `tn.md`), avec un titre par paracha : le texte se colle sous le titre. Il part dans toutes les chaînes de cette langue. Une paracha sans texte dans une langue : le message du vendredi de cette chaîne part sans dvar Torah. Pour une paracha double, les deux textes se suivent.

## Réglages
- `chaine/config.json` : l'adresse de l'app (`appUrl`) et la liste des chaînes (`chaines`). Pour chaque chaîne :
  - `id` : son nom court, en minuscules (`fr`, `he`… ; pour une deuxième chaîne dans une langue, par exemple `fr-il`) ;
  - `nom` : son nom sur la page de publication ;
  - `langue` : `fr`, `he`, `en`, `es` ou `tn` ;
  - `calendrier` : `diaspora` ou `israel` ;
  - `villes` : les villes dont on donne l'heure d'allumage (parmi les villes de l'app).
- `web/config.js` (`channelUrl`) : l'adresse WhatsApp de chaque chaîne, sous son `id`. L'app propose les chaînes dont l'`id` est une langue de l'app ; une chaîne supplémentaire (`fr-il`) n'apparaît que sur la page de publication.
- `chaine/textes.js` : la formulation des messages, dans les cinq langues. Le tounsi est un brouillon : il figure dans la feuille de relecture `docs/traductions-a-relire.csv` (lignes « chaine. »).
- Pour voir les messages sans les mettre en ligne : `node tools/fetch_sefaria.js`, puis `node tools/make_channel.js _site/chaine`, et ouvrir `_site/chaine/index.html`. Une erreur dans la liste des chaînes (langue ou ville inconnue) arrête l'outil avec un message qui dit quoi corriger.

## Mise à jour automatique
- La tâche « Site public » prépare les messages de la semaine passée et des quatre suivantes, pour toutes les chaînes. Elle tourne le dimanche et le mercredi, et à chaque modification des textes, des chaînes ou de leurs adresses.
- Si les messages préparés s'arrêtent dans moins de trois jours, la page affiche un avertissement.
- GitHub suspend les tâches programmées d'un projet resté 60 jours sans modification. Pour la relancer : onglet Actions → « Site public » → Enable workflow, puis Run workflow.

## Sources
- [Tarifs de la plateforme WhatsApp Business (Meta)](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)
- [Tarification des messages hors modèle, à partir du 1er octobre 2026 (Meta)](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages/)
- [Limites de l'API des bots Telegram](https://core.telegram.org/bots/faq)
- [Plusieurs administrateurs par chaîne WhatsApp (TechCrunch, 17 janvier 2024)](https://techcrunch.com/2024/01/17/whatsapp-launches-voice-updates-and-polls-for-channels)
