# 9. Licences des textes et demande d'autorisation à Metsudah

## Décision (24 novembre 2026)
- On **garde le Targoum Onkelos de l'édition Metsudah**.
- L'app sort gratuite, sans publicité, avec des **dons libres seulement**.
- **Parrainages payants** (« cette semaine est dédiée par… ») et **licences synagogues / écoles** : pas avant une autorisation écrite de l'éditeur.

## Ce qui a été vérifié
- Sefaria classe cet Onkelos (« Sifsei Chachomim Chumash, Metsudah Publications, 2009 ») sous licence **CC BY-NC** : réutilisation permise, mention obligatoire, usage non commercial seulement.
- Définition de la licence : est non commercial un usage qui n'est « pas principalement destiné à un avantage commercial ou à une compensation financière ». Seul le but principal compte ; le fait d'être une association ne suffit pas.
- Creative Commons ne tranche pas les cas limites et conseille, en cas de doute, de demander au titulaire des droits.
- Aucune autorisation publiée par Metsudah pour des dons ou des parrainages n'a été trouvée.
- Conclusion : des dons libres sur une app gratuite sont défendables ; un parrainage payant est une zone grise ; une licence vendue n'est pas couverte.

Ceci n'est pas un avis juridique.

## Textes utilisés et mentions obligatoires

| Texte | Édition reçue de Sefaria | Licence | Obligation |
|---|---|---|---|
| Torah (hébreu) | Miqra according to the Masorah | CC BY-SA | Citer la source et la licence |
| Targoum Onkelos | Sifsei Chachomim Chumash, Metsudah Publications, 2009 | CC BY-NC | Citer l'éditeur et la licence ; usage non commercial |
| Targoum Yerouchalmi | Targum Jerusalem on Torah (sinon Targum Jonathan) | Domaine public | Aucune |

**Dans l'app** : Réglages → « Sources et licences » affiche ces trois lignes, avec un lien vers chaque licence, la mention de Sefaria et la licence des polices. Les éditions de la Torah et de l'Onkelos sont demandées nommément à Sefaria ; l'écran affiche l'édition et la licence réellement reçues.

**Bouton de don** : il apparaît dans les Réglages dès que l'adresse de la page de don est renseignée dans `web/config.js` (`donateUrl`). Il ouvre cette page dans le navigateur du téléphone. Pas de parrainage payant tant que l'éditeur n'a pas répondu.

Point à surveiller : la Torah est sous CC BY-SA et l'Onkelos sous CC BY-NC, deux licences qui ne se mélangent pas dans une œuvre dérivée. L'app les affiche côte à côte sans les modifier, comme Sefaria. Pour écarter la question, Sefaria propose aussi une Torah du domaine public (« Tanach with Ta'amei Hamikra »).

## Demande d'autorisation

**Destinataire** : Israel Bookshop Publications, qui vend le Houmash Metsudah — sales@israelbookshoppublications.com, +1 732 901 3009, 501 Prospect Street, Suite 97, Lakewood, NJ 08701, États-Unis.

**En parallèle** : écrire à Sefaria (hello@sefaria.org) pour demander qui détient les droits chez Metsudah, puisque c'est Sefaria qui a reçu la licence.

**Avant l'envoi** : compléter les crochets.

### Lettre à envoyer (anglais)

> **Subject:** Permission request — Targum Onkelos from the Sifsei Chachomim Chumash (Metsudah, 2009) in a free Shnayim Mikra app
>
> Dear Sir or Madam,
>
> I am writing on behalf of Association Hachiveinou Letoratekha, a non-profit association. We are developing "Shnayim Mikra", a free app with no advertising that helps people complete Shnayim Mikra ve-Echad Targum every week. The weekly parashah is shown aliyah by aliyah: each verse twice, followed by Targum Onkelos.
>
> The Targum shown in the app is the text of the Sifsei Chachomim Chumash (Metsudah Publications, 2009), as published on Sefaria under the Creative Commons Attribution-NonCommercial (CC BY-NC) license. The app retrieves it through Sefaria's public API, displays it unchanged, and credits the edition, the publisher and the license.
>
> The app is and will remain free to read. The text is never sold, never placed behind a paywall, and no advertising is shown. To cover running costs, we would like to:
>
> 1. accept voluntary donations from users;
> 2. offer dedications — a short line such as "This week's learning is dedicated by … / in memory of …" — in return for a contribution;
> 3. possibly later, offer a group plan to synagogues and schools for the group features, while the text itself stays free for everyone.
>
> We want to be sure that these uses are acceptable to you. Could you confirm in writing that we may keep using the Metsudah Onkelos text in the app under these conditions, or tell us which of them you would not allow, or on what terms?
>
> We would be glad to display the credit line of your choice, together with a link to buy the printed Chumash.
>
> If this request should go to someone else, I would be grateful if you could forward it or tell me whom to contact.
>
> Thank you very much,
>
> [Name]
> Association Hachiveinou Letoratekha
> [E-mail]
> [Link to the app or to a test version]

### Traduction (pour relecture)

> **Objet :** Demande d'autorisation — Targoum Onkelos du Houmash Sifsei Chachomim (Metsudah, 2009) dans une application gratuite de Shnayim Mikra
>
> Madame, Monsieur,
>
> Je vous écris au nom de l'Association Hachiveinou Letoratekha, association à but non lucratif. Nous développons « Shnayim Mikra », une application gratuite et sans publicité qui aide à faire Shnayim Mikra ve'Ehad Targoum chaque semaine. La paracha est présentée alya par alya : chaque verset deux fois, puis le Targoum Onkelos.
>
> Le Targoum affiché est le texte du Houmash Sifsei Chachomim (Metsudah Publications, 2009), tel que publié sur Sefaria sous licence Creative Commons Attribution – Pas d'utilisation commerciale (CC BY-NC). L'application le récupère par l'API publique de Sefaria, l'affiche sans modification et cite l'édition, l'éditeur et la licence.
>
> L'application est et restera gratuite à la lecture. Le texte n'est jamais vendu, jamais placé derrière un accès payant, et aucune publicité n'est affichée. Pour couvrir les frais de fonctionnement, nous souhaitons :
>
> 1. accepter des dons libres des utilisateurs ;
> 2. proposer des dédicaces — une courte ligne comme « L'étude de cette semaine est dédiée par… / à la mémoire de… » — en échange d'une contribution ;
> 3. éventuellement plus tard, proposer une formule de groupe aux synagogues et aux écoles pour les fonctions de groupe, le texte restant gratuit pour tous.
>
> Nous voulons nous assurer que ces usages vous conviennent. Pouvez-vous nous confirmer par écrit que nous pouvons continuer à utiliser le texte de l'Onkelos Metsudah dans ces conditions, ou nous indiquer lesquelles vous n'accepteriez pas, ou à quelles conditions ?
>
> Nous afficherons volontiers la mention de votre choix, avec un lien pour acheter le Houmash imprimé.
>
> Si cette demande doit être adressée à quelqu'un d'autre, je vous serais reconnaissant de la transmettre ou de m'indiquer la bonne personne.
>
> Avec mes remerciements,
>
> [Nom]
> Association Hachiveinou Letoratekha
> [E-mail]
> [Lien vers l'application ou une version de test]

## Sources
- [Guide de réutilisation des textes de Sefaria](https://www.sefaria.org/sheets/228381)
- [Licence CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/legalcode.en)
- [Interprétation de « NonCommercial » par Creative Commons](https://wiki.creativecommons.org/wiki/NonCommercial_interpretation)
- [FAQ Creative Commons](https://creativecommons.org/faq/)
