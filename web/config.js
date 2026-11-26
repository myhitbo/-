/* Shnayim Mikra — réglages de l'éditeur de l'app (pas de l'utilisateur). */
window.SM_CONFIG = {
  /* Adresse de la page de don de l'organisme. Vide = le bouton « Faire un don » n'est pas affiché. */
  donateUrl: '',
  /* Adresses des chaînes WhatsApp de l'organisme (https://whatsapp.com/channel/…) : une chaîne par langue.
     Les chaînes sont décrites dans chaine/config.json ; leur adresse s'écrit ici, et seulement ici :
     - l'app y prend le bouton « Rejoindre la chaîne » (la chaîne de la langue de l'app, les autres juste en dessous) ;
     - la page de publication y prend le bouton « Ouvrir la chaîne ».
     Vide = chaîne pas encore ouverte : rien n'est affiché pour elle dans l'app. */
  channelUrl: { fr: '', he: '', en: '', es: '', tn: '' }
};
