/* Shnayim Mikra — textes de l'interface.
   Le français est ici ; les autres langues sont dans i18n/<langue>.js. Une clé absente dans une langue
   retombe sur le français. {nom} = valeur insérée par SM_FMT. */
(function () {
  const T = {
    fr: {
      locale: 'fr-FR',   /* format des dates */
      min: 'min', back: 'Retour', continue: 'Continuer', ok: 'OK',
      navMain: 'Navigation principale', navHome: 'Accueil', navYear: 'Année', navSettings: 'Réglages',
      israel: 'Israël', diaspora: 'Diaspora', city: 'Ville',
      /* Noms : alyot, livres ; parachiyot = null → noms français de sefaria.js ; villes = {} → noms français de globals.js */
      alyot: ['Rishon', 'Sheni', 'Shlishi', 'Revi\'i', 'Hamishi', 'Shishi', 'Shvi\'i'],
      books: ['Béréchit', 'Chemot', 'Vayikra', 'Bamidbar', 'Devarim'],
      parashiyot: null, cities: {},
      days: null, months: null,   /* noms des jours et des mois : seulement pour une langue qu'Intl ne sait pas dater */

      /* Accueil */
      shabbat: 'Shabbat', parashaOfWeek: 'Paracha de la semaine', catchUp: 'Rattrapage',
      prevUntil: 'À rattraper · jusqu\'à mardi {time}', prevLine: '{n}/7 alyot lues · encore {left}',
      weekProgress: 'Avancée de la semaine', verses: 'Versets', duration: 'Durée', remaining: 'Lecture restante',
      deadline: 'Échéance', printRest: 'Pas fini ? Imprime le reste pour Chabbat matin',
      markRead: 'Marquer {name} comme lue (lue dans mon Houmash)',
      allRead: 'Les 7 alyot de {parasha} sont lues. Shabbat Shalom.',
      notebook: 'Carnet de rattrapage', completeBeforeST: 'À compléter avant Sim\'hat Torah ({date})', completeBeforeST0: 'À compléter avant Sim\'hat Torah',
      nOf7: '{n}/7 alyot',
      streak: 'Série', weeks: 'semaines', thisYear: 'Cette année', finishedPl: 'terminées',
      nextParashiyot: 'Prochaines parachiyot', readAhead: 'Lire en avance', shabbatDate: 'Shabbat {date}',
      toast: 'Yasher koah ! {name} est lue',
      goalBefore: 'Objectif : finir avant Chabbat', goalShabbat: 'Encore possible ce Chabbat, avant le repas de midi',
      candleFri: 'Allumage vendredi à {time} · {city} (coucher du soleil − {min} min)', candle: 'Allumage à {time} · {city} (coucher du soleil − {min} min)',
      candleNoData: 'Allumage selon ta ville (textes en cours de téléchargement)',
      shabbatIn: 'Chabbat dans {dur}', shabbatShalom: 'Chabbat Chalom',
      durDH: '{d} j {h} h', durHM: '{h} h {m}', durM: '{m} min',
      readOne: 'Lire {name}', readRange: 'Lire {a} – {b}', readAll: 'Lire la paracha', readRest: 'Lire la suite',
      stRead: 'Lue', stToday: 'Aujourd\'hui', stToRead: 'À lire', stLater: 'À venir',
      late1: 'En retard : 1 alya à rattraper', lateN: 'En retard : {n} alyot à rattraper',

      /* Rythme */
      rhythm: 'Rythme',
      rh0: 'Une alya par jour', rh0s: '5 à 12 min · conseillé',
      rh1: 'Toute la paracha d\'un coup', rh1s: 'Environ 1 h, le jour de ton choix',
      rh2: '2 ou 3 séances', rh2s: 'La paracha répartie sur la semaine',
      rh3: 'Libre', rh3s: 'Tu lis quand tu veux, sans échéance par jour',
      rhDay: 'Jour de lecture', rhCount: 'Nombre de séances',
      rhN2: '2 séances', rhN2s: 'lundi et jeudi', rhN3: '3 séances', rhN3s: 'dimanche, mardi et jeudi',
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
      display: 'Affichage', displayText: 'Affichage du texte', slower: 'Plus lent', faster: 'Plus rapide',
      auto: 'Auto', pause: 'Pause', autoRead: 'Lecture auto', targumSpeed: 'Vitesse du Targoum',
      fontLabel: 'Police', sizeLabel: 'Taille', smaller: 'Texte plus petit', bigger: 'Texte plus grand',
      tapHint: 'Touchez le texte pour les commandes', backHome: 'Retour à l\'accueil', readAgain: 'Relire depuis le début',
      clair: 'Clair', sombre: 'Sombre', texte: 'Texte', parchemin: 'Parchemin',
      fontDesc: { frank: 'Classique, proche du Houmash', david: 'Traditionnelle, aérée', noto: 'Voyelles et te\'amim complets', heebo: 'Sans empattement' },

      /* Bienvenue */
      welcome: 'Bienvenue.', whichLang: 'Quelle langue ?', whereLive: 'Où vis-tu ?',
      whereHelp: 'Pour la bonne paracha de la semaine et l\'heure d\'allumage des bougies.',
      yourRhythm: 'Ton rythme', letsGo: 'C\'est parti', changeAnytime: 'Modifiable à tout moment dans les Réglages.', stepOf: 'Étape {n} sur 3',

      /* Année */
      yearN: 'Année {year}', yearTitle: 'Ton année', parashiyotDone: 'Parachiyot terminées', untilST: 'Jusqu\'à Simhat Torah',
      lgDone: 'Terminée', lgWeek: 'Cette semaine', lgLater: 'À venir', lgLate: 'À compléter',

      /* Imprimer */
      printKicker: 'Pour lire sans téléphone', printTitle: 'Imprimer pour Shabbat',
      printNote: 'Sans téléphone le Chabbat : la lecture reste possible le matin, avant le repas.',
      printBtn: 'Imprimer ou PDF', content: 'Contenu', previewA4: 'Aperçu de la page A4',
      printRestOpt: 'Ce qu\'il me reste', printAllOpt: 'Toute la paracha',
      printSub: '{range} · {min} min · ~{pages} p.', printSubAll: '7 alyot · {min} min · ~{pages} p.', printSubWait: 'Textes en cours de téléchargement', printSub7: '7 alyot',
      printSummary1: 'Chaque verset, puis son Targoum · A4 · environ 1 page', printSummaryN: 'Chaque verset, puis son Targoum · A4 · environ {n} pages',
      printNoText: 'Textes pas encore disponibles.',
      printHow: 'Chaque verset deux fois, puis le Targoum. ✱ = verset sans Targoum Onkelos : le lire trois fois.',

      /* Rappel */
      remTime: 'Heure du rappel', remBlocked: 'Les notifications sont bloquées pour l\'app : le rappel ne peut pas s\'afficher.', remAllow: 'Autoriser',
      remHelp: 'Une notification les jours de lecture, jamais pendant Shabbat ni les fêtes.',
      remNext: 'Prochain rappel : {when}', remNone: 'Aucun rappel prévu : rien à lire d\'ici là, ou rappel coupé.', remTest: 'Tester', remTestText: 'Le rappel fonctionne.',
      remExact: 'Pour recevoir le rappel à l\'heure exacte, autorise « Alarmes et rappels ». Sinon il peut arriver avec quelques minutes de retard.',
      remMin: 'Environ {min} min', remLate1: ' · dont 1 alya en retard', remLateN: ' · dont {n} alyot en retard',
      remGeneric: 'C\'est l\'heure de ta lecture.', wholeParasha: 'toute la paracha',

      /* Sources et licences */
      srcTitle: 'Sources', srcKicker: 'Textes et licences', srcRow: 'Sources et licences',
      srcTexts: 'Textes', srcMikra: 'Torah (texte hébreu)', srcOnk: 'Targoum Onkelos', srcYer: 'Targoum Yerouchalmi',
      srcYerNote: 'pour les versets qu\'Onkelos ne traduit pas',
      srcPD: 'Domaine public', srcNC: 'usage non commercial', srcLicense: 'Licence',
      srcSefaria: 'Tous les textes sont fournis par Sefaria, bibliothèque libre de textes juifs :',
      srcFonts: 'Polices', srcFontsLine: 'Inter, Newsreader, Frank Ruhl Libre, David Libre, Noto Serif Hebrew, Heebo et Noto Sans Arabic, sous licence',

      /* Don */
      donate: 'Soutenir l\'app', donateSub: 'L\'app est gratuite et sans publicité. Un don aide à la faire vivre.', donateBtn: 'Faire un don'
    }
  };
  const RTL = { he: 1, tn: 1, ma: 1 };
  const memo = {};
  window.SM_I18N = T;
  window.SM_LANG = function () { return (window.APP && APP.get('lang')) || 'fr'; };
  window.SM_RTL = function (lang) { return !!RTL[lang || window.SM_LANG()]; };
  /* Textes de la langue en cours (ou de `lang`), complétés par le français */
  window.SM_TR = function (lang) { lang = lang || window.SM_LANG(); return memo[lang] || (memo[lang] = Object.assign({}, T.fr, T[lang] || {})); };
  window.SM_FMT = function (s, v) { return String(s == null ? '' : s).replace(/\{(\w+)\}/g, function (_, k) { return v && v[k] != null ? v[k] : ''; }); };

  /* ---------- Noms selon la langue ---------- */
  window.SM_ALYA = function (i) { return window.SM_TR().alyot[i] || ''; };
  window.SM_BOOK = function (i) { return window.SM_TR().books[i] || ''; };
  /* Nom d'une paracha d'après ses numéros (deux pour une paracha double) ; `fallback` si les numéros manquent */
  window.SM_PARASHA = function (idx, fallback) {
    const list = window.SM_TR().parashiyot || (window.SM_SEFARIA && window.SM_SEFARIA.FR) || [];
    const names = (idx || []).map(function (i) { return list[i]; }).filter(Boolean);
    return names.length ? names.join(' – ') : (fallback || '');
  };
  /* Nom hébreu à afficher à côté d'un nom : rien si le nom est déjà écrit en lettres hébraïques (hébreu, tounsi, darija) */
  window.SM_HEB = function (name, heb) { return /[\u0590-\u05FF]/.test(String(name || '')) ? '' : (heb || ''); };
  window.SM_CITY_NAME = function (c) { return (c && (window.SM_TR().cities[c.id] || c.name)) || ''; };
  /* Dates dans la langue en cours. `opts` = options d'Intl.DateTimeFormat. */
  const fmts = {};
  window.SM_DATE = function (ms, opts, tz) {
    const T = window.SM_TR();
    /* Langue qui fournit ses propres noms de jours et de mois (judéo-arabe en lettres hébraïques) : date composée à la main */
    if (T.days && T.months) {
      try {
        const p = {}; (fmts['~' + (tz || 'UTC')] || (fmts['~' + (tz || 'UTC')] = new Intl.DateTimeFormat('en-GB', { timeZone: tz || 'UTC', weekday: 'short', year: 'numeric', month: 'numeric', day: 'numeric', hour: '2-digit', minute: '2-digit', hour12: false }))).formatToParts(ms).forEach(function (x) { p[x.type] = x.value; });
        const out = [];
        if (opts.weekday) out.push(T.days[['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(p.weekday)]);
        if (opts.day) out.push(String(+p.day));
        if (opts.month) out.push(T.months[+p.month - 1]);
        if (opts.year) out.push(p.year);
        if (opts.hour) out.push((p.hour === '24' ? '00' : p.hour) + ':' + p.minute);
        return out.join(' ');
      } catch (e) { return ''; }
    }
    const loc = T.locale || 'fr-FR', key = loc + '|' + (tz || 'UTC') + '|' + JSON.stringify(opts);
    try { return (fmts[key] || (fmts[key] = new Intl.DateTimeFormat(loc, Object.assign({ timeZone: tz || 'UTC' }, opts)))).format(ms); } catch (e) { return ''; }
  };
  /* Nom d'un jour de la semaine (0 = dimanche) */
  window.SM_WEEKDAY = function (i, style) { return window.SM_DATE(Date.UTC(2023, 0, 1 + i, 12), { weekday: style || 'long' }); };
})();
