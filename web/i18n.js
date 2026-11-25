/* Shnayim Mikra — textes de l'interface.
   Une clé absente dans une langue retombe sur le français. {nom} = valeur insérée par SM_FMT. */
(function () {
  const T = {
    fr: {
      /* Rythme */
      rhythm: 'Rythme',
      rh0: 'Une alya par jour', rh0s: '5 à 12 min · conseillé',
      rh1: 'Toute la paracha d\'un coup', rh1s: 'Environ 1 h, le jour de ton choix',
      rh2: '2 ou 3 séances', rh2s: 'La paracha répartie sur la semaine',
      rh3: 'Libre', rh3s: 'Tu lis quand tu veux, sans échéance par jour',
      rhDay: 'Jour de lecture', rhCount: 'Nombre de séances',
      rhN2: '2 séances', rhN2s: 'lundi et jeudi', rhN3: '3 séances', rhN3s: 'dimanche, mardi et jeudi',
      daysShort: ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam'],
      /* Ordre de lecture */
      order: 'Ordre de lecture',
      or0: 'Verset, verset, Targoum', or0s: 'Chaque verset deux fois, puis son Targoum',
      or1: 'Par paragraphe', or1s: 'Chaque paragraphe (petou\'ha ou setouma) deux fois, puis son Targoum',
      or2: 'Par alya', or2s: 'L\'alya deux fois, puis son Targoum',
      or3: 'Tout, puis tout le Targoum', or3s: 'Toute la séance deux fois, puis tout son Targoum (toute la paracha si tu la lis d\'un coup)',
      /* Lecteur */
      read1: '1ʳᵉ lecture', read2: '2ᵉ lecture', targum: 'Targoum',
      read3nt: '3ᵉ lecture · pas de Targoum', yer: 'Targoum Yerouchalmi',
      verseOf: 'Verset {n} sur {total}', minLeft: '{n} min restantes',
      doneOne: '{name} terminé', doneRange: '{a} – {b} terminés', doneAll: 'Paracha terminée',
      nextOne: 'Prochaine alya : {name}, {min} min.', nextRange: 'Prochaine séance : {a} – {b}, {min} min.',
      nextNone: 'La paracha est terminée. Shabbat Shalom !',
      /* Accueil */
      readOne: 'Lire {name}', readRange: 'Lire {a} – {b}', readAll: 'Lire la paracha', readRest: 'Lire la suite',
      stRead: 'Lue', stToday: 'Aujourd\'hui', stToRead: 'À lire', stLater: 'À venir',
      late1: 'En retard : 1 alya à rattraper', lateN: 'En retard : {n} alyot à rattraper',
      /* Rappel */
      remTime: 'Heure du rappel', remBlocked: 'Les notifications sont bloquées pour l\'app : le rappel ne peut pas s\'afficher.', remAllow: 'Autoriser',
      remHelp: 'Une notification les jours de lecture, jamais pendant Shabbat ni les fêtes.',
      remMin: 'Environ {min} min', remLate1: ' · dont 1 alya en retard', remLateN: ' · dont {n} alyot en retard',
      remGeneric: 'C\'est l\'heure de ta lecture.', wholeParasha: 'toute la paracha',
      /* Sources et licences */
      srcTitle: 'Sources', srcKicker: 'Textes et licences', srcRow: 'Sources et licences', back: 'Retour',
      srcTexts: 'Textes', srcMikra: 'Torah (texte hébreu)', srcOnk: 'Targoum Onkelos', srcYer: 'Targoum Yerouchalmi',
      srcYerNote: 'pour les versets qu\'Onkelos ne traduit pas',
      srcPD: 'Domaine public', srcNC: 'usage non commercial', srcLicense: 'Licence',
      srcSefaria: 'Tous les textes sont fournis par Sefaria, bibliothèque libre de textes juifs :',
      srcFonts: 'Polices', srcFontsLine: 'Inter, Newsreader, Frank Ruhl Libre, David Libre, Noto Serif Hebrew, Heebo et Noto Sans Arabic, sous licence',
      /* Don */
      donate: 'Soutenir l\'app', donateSub: 'L\'app est gratuite et sans publicité. Un don aide à la faire vivre.', donateBtn: 'Faire un don'
    },
    en: {}, es: {}, he: {}, tn: {}, ma: {}
  };
  const RTL = { he: 1, tn: 1, ma: 1 };
  const memo = {};
  window.SM_I18N = T;
  window.SM_LANG = function () { return (window.APP && APP.get('lang')) || 'fr'; };
  window.SM_RTL = function () { return !!RTL[window.SM_LANG()]; };
  window.SM_TR = function (lang) { lang = lang || window.SM_LANG(); return memo[lang] || (memo[lang] = Object.assign({}, T.fr, T[lang] || {})); };
  window.SM_FMT = function (s, v) { return String(s == null ? '' : s).replace(/\{(\w+)\}/g, function (_, k) { return v && v[k] != null ? v[k] : ''; }); };
})();
