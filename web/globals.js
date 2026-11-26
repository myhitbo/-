/* Shnayim Mikra — données partagées : semaines (moteur des lectures et texte embarqués, hors connexion),
   Israël/diaspora, rite, heure d'allumage, échéances, progression par semaine, textes du lecteur,
   haftara, impression. */
(function () {
  const NAMES = ['Rishon', 'Sheni', 'Shlishi', "Revi'i", 'Hamishi', 'Shishi', "Shvi'i"];
  const MONTHS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'];
  const DAYS = ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi'];
  const HEB = ['רִאשׁוֹן', 'שֵׁנִי', 'שְׁלִישִׁי', 'רְבִיעִי', 'חֲמִישִׁי', 'שִׁשִּׁי', 'שְׁבִיעִי'];
  const JOURS = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Shabbat'];
  const RITES = { edot: "Edot hamizra'h", sefard: 'Sfard', ashkenaz: 'Ashkenaz' };
  const FALLBACK = { parasha: '—', parashaHe: '', parashaRef: 'Données absentes' };
  const cap = (s) => s.charAt(0).toUpperCase() + s.slice(1);

  /* ---------- Villes : coordonnées, fuseau, minutes avant le coucher du soleil ---------- */
  const IL = 'Asia/Jerusalem';
  const CITIES = [
    ['jerusalem', 'Jérusalem', 31.7683, 35.2137, IL, 40, 1], ['telaviv', 'Tel Aviv', 32.0853, 34.7818, IL, 20, 1], ['haifa', 'Haïfa', 32.794, 34.9896, IL, 30, 1],
    ['bneibrak', 'Bné Brak', 32.0807, 34.8338, IL, 20, 1], ['petahtikva', 'Petah Tikva', 32.084, 34.8878, IL, 20, 1], ['netanya', 'Netanya', 32.3215, 34.8532, IL, 20, 1],
    ['raanana', "Ra'anana", 32.1848, 34.8713, IL, 20, 1], ['ashdod', 'Ashdod', 31.8044, 34.6553, IL, 20, 1], ['modiin', "Modi'in", 31.898, 35.0104, IL, 20, 1],
    ['beersheva', "Be'er Sheva", 31.2518, 34.7913, IL, 20, 1], ['eilat', 'Eilat', 29.5577, 34.9519, IL, 20, 1],
    ['paris', 'Paris', 48.8566, 2.3522, 'Europe/Paris', 18, 0], ['marseille', 'Marseille', 43.2965, 5.3698, 'Europe/Paris', 18, 0], ['lyon', 'Lyon', 45.764, 4.8357, 'Europe/Paris', 18, 0],
    ['nice', 'Nice', 43.7102, 7.262, 'Europe/Paris', 18, 0], ['strasbourg', 'Strasbourg', 48.5734, 7.7521, 'Europe/Paris', 18, 0], ['toulouse', 'Toulouse', 43.6047, 1.4442, 'Europe/Paris', 18, 0],
    ['bruxelles', 'Bruxelles', 50.8503, 4.3517, 'Europe/Brussels', 18, 0], ['anvers', 'Anvers', 51.2194, 4.4025, 'Europe/Brussels', 18, 0], ['geneve', 'Genève', 46.2044, 6.1432, 'Europe/Zurich', 18, 0],
    ['londres', 'Londres', 51.5074, -0.1278, 'Europe/London', 18, 0], ['manchester', 'Manchester', 53.4808, -2.2426, 'Europe/London', 18, 0], ['moscou', 'Moscou', 55.7558, 37.6173, 'Europe/Moscow', 18, 0],
    ['newyork', 'New York', 40.7128, -74.006, 'America/New_York', 18, 0], ['miami', 'Miami', 25.7617, -80.1918, 'America/New_York', 18, 0], ['losangeles', 'Los Angeles', 34.0522, -118.2437, 'America/Los_Angeles', 18, 0],
    ['montreal', 'Montréal', 45.5017, -73.5673, 'America/Toronto', 18, 0], ['toronto', 'Toronto', 43.6532, -79.3832, 'America/Toronto', 18, 0],
    ['mexico', 'Mexico', 19.4326, -99.1332, 'America/Mexico_City', 18, 0], ['panama', 'Panamá', 8.9824, -79.5199, 'America/Panama', 18, 0], ['bogota', 'Bogotá', 4.711, -74.0721, 'America/Bogota', 18, 0],
    ['caracas', 'Caracas', 10.4806, -66.9036, 'America/Caracas', 18, 0], ['saopaulo', 'São Paulo', -23.5505, -46.6333, 'America/Sao_Paulo', 18, 0], ['santiago', 'Santiago', -33.4489, -70.6693, 'America/Santiago', 18, 0],
    ['buenosaires', 'Buenos Aires', -34.6037, -58.3816, 'America/Argentina/Buenos_Aires', 18, 0],
    ['casablanca', 'Casablanca', 33.5731, -7.5898, 'Africa/Casablanca', 18, 0], ['tunis', 'Tunis', 36.8065, 10.1815, 'Africa/Tunis', 18, 0], ['djerba', 'Djerba', 33.8076, 10.8451, 'Africa/Tunis', 18, 0],
    ['johannesburg', 'Johannesburg', -26.2041, 28.0473, 'Africa/Johannesburg', 18, 0], ['melbourne', 'Melbourne', -37.8136, 144.9631, 'Australia/Melbourne', 18, 0]
  ].map(c => ({ id: c[0], name: c[1], lat: c[2], lon: c[3], tz: c[4], off: c[5], il: !!c[6] }));
  window.SM_CITIES = CITIES;

  const get = (k) => window.APP ? APP.get(k) : undefined;
  const now = () => window.SM_NOW || Date.now();
  const isIL = () => (get('place') ?? 0) === 0;
  function city() { const c = CITIES.find(x => x.id === get('city')); return c && c.il === isIL() ? c : CITIES.find(x => x.il === isIL()); }
  window.SM_CITY = city;
  window.SM_CITY_LIST = () => { const cur = city(); return CITIES.filter(c => c.il === isIL()).map(c => ({ id: c.id, name: c.name, on: c.id === cur.id })); };

  /* ---------- Coucher du soleil (algorithme de l'Almanac / NOAA simplifié) ---------- */
  const rad = Math.PI / 180;
  function sunset(iso, c) {
    const [y, m, d] = iso.split('-').map(Number);
    const N = Math.floor(275 * m / 9) - Math.floor((m + 9) / 12) * (1 + Math.floor((y - 4 * Math.floor(y / 4) + 2) / 3)) + d - 30;
    const lngH = c.lon / 15, t = N + (18 - lngH) / 24, M = 0.9856 * t - 3.289;
    let L = (M + 1.916 * Math.sin(M * rad) + 0.02 * Math.sin(2 * M * rad) + 282.634 + 720) % 360;
    let RA = (Math.atan(0.91764 * Math.tan(L * rad)) / rad + 720) % 360;
    RA = (RA + Math.floor(L / 90) * 90 - Math.floor(RA / 90) * 90) / 15;
    const sinD = 0.39782 * Math.sin(L * rad), cosD = Math.cos(Math.asin(sinD));
    const cosH = (Math.cos(90.833 * rad) - sinD * Math.sin(c.lat * rad)) / (cosD * Math.cos(c.lat * rad));
    const H = Math.acos(Math.max(-1, Math.min(1, cosH))) / rad / 15;
    let UT = H + RA - 0.06571 * t - 6.622 - lngH; const want = 18 - lngH;
    UT = UT + 24 * Math.round((want - UT) / 24);
    return Date.UTC(y, m - 1, d) + UT * 3600e3;
  }
  const fmt = {};
  function f(tz, opts) { const k = tz + JSON.stringify(opts); return fmt[k] || (fmt[k] = new Intl.DateTimeFormat('fr-FR', Object.assign({ timeZone: tz }, opts))); }
  const hhmm = (ms, tz) => f(tz, { hour: '2-digit', minute: '2-digit', hour12: false }).format(ms);
  function localISO(ms, tz) { const p = {}; f(tz, { year: 'numeric', month: '2-digit', day: '2-digit' }).formatToParts(ms).forEach(x => p[x.type] = x.value); return p.year + '-' + p.month + '-' + p.day; }
  function addDays(iso, n) { const [y, m, d] = iso.split('-').map(Number); const t = new Date(Date.UTC(y, m - 1, d + n)); return t.toISOString().slice(0, 10); }
  const dow = (iso) => new Date(iso + 'T12:00:00Z').getUTCDay();
  const dayLabel = (iso, y) => { const t = new Date(iso + 'T12:00:00Z'); return DAYS[t.getUTCDay()] + ' ' + t.getUTCDate() + ' ' + MONTHS[t.getUTCMonth()] + (y ? ' ' + t.getUTCFullYear() : ''); };
  const candle = (shIso, c) => sunset(addDays(shIso, -1), c) - c.off * 60e3;
  const shabbatEnd = (shIso, c) => sunset(shIso, c) + 42 * 60e3;
  const tuesdayEnd = (shIso, c) => sunset(addDays(shIso, 3), c);
  function inDur(ms) { const m = Math.max(0, Math.round(ms / 60e3)); const d = Math.floor(m / 1440), h = Math.floor(m % 1440 / 60), mi = m % 60;
    return d ? d + ' j ' + h + ' h' : h ? h + ' h ' + String(mi).padStart(2, '0') : mi + ' min'; }
  window.SM_ZMAN = { sunset, candle, hhmm, localISO, addDays };

  /* ---------- Sim'hat Torah : 22 Tichri en Israël (Chemini Atséret), 23 Tichri en diaspora ---------- */
  let hebF; try { hebF = new Intl.DateTimeFormat('en-u-ca-hebrew', { day: 'numeric', month: 'long', timeZone: 'UTC' }); } catch (e) {}
  function simhatTorah(fromIso, dir, il) {
    if (!hebF) return null; const want = il ? 22 : 23;
    for (let k = 0; k < 400; k++) { const iso = addDays(fromIso, dir * k); const p = {}; hebF.formatToParts(new Date(iso + 'T12:00:00Z')).forEach(x => p[x.type] = x.value);
      if (p.month === 'Tishri' && +p.day === want) return iso; }
    return null;
  }

  /* ---------- Données embarquées : les lectures au démarrage, le texte et le Targoum à la demande ---------- */
  const L = window.SM_LECTURE;
  const lue = (nom) => (window.SM_DONNEES ? SM_DONNEES.lue(nom) : undefined);
  const fichier = (livre) => L.fichierLivre(livre);
  /* Le nom hébreu des livres et des parachiot, écrit à la manière de la langue de l'interface
     (he, fr ou en dans les données ; l'espagnol suit l'anglais, le tunisien et le marocain le français). */
  const NOMS = { he: 'he', en: 'en', es: 'en' };
  const nom = (t) => (t ? t[NOMS[get('lang')] || 'fr'] || t.fr : '');
  const rite = () => { const r = get('rite'); return L && L.NUSAH.indexOf(r) >= 0 ? r : 'edot'; };
  window.SM_RITE = () => ({ id: rite(), name: RITES[rite()] });
  /* Jérusalem, ville murée : Pourim le 15 (le Pourim triple change le maftir et la haftara du Chabbat) */
  const options = () => ({ enIsrael: isIL(), mukafChoma: isIL() && city().id === 'jerusalem', nusah: rite() });
  const span = (debut, fin) => { const a = debut.split(':'), b = fin.split(':'); return debut === fin ? debut : a[0] === b[0] ? debut + ' – ' + b[1] : debut + ' – ' + fin; };

  /* Verset sans Targoum : Onkelos reprend l'hébreu lettre pour lettre (seulement des noms, « Réouven, Chimon »),
     et toujours Bamidbar 32:3 (« Atarot ve-Divon », Berakhot 8a), où l'édition imprime le Targoum Yerouchalmi. */
  const YER_EDITION = { 'Numbers 32:3': 1 };
  const skel = (x) => String(x || '').replace(/[־׀]/g, ' ').replace(/[֑-ׇ׳״]/g, '').replace(/[^א-ת ]/g, ' ').replace(/\s+/g, ' ').trim();
  function yerCache() { try { return JSON.parse(localStorage.getItem('sm.yer') || '{}'); } catch (e) { return {}; } }

  /* Les versets d'un passage de la Torah, avec leur Targoum : null tant que le livre n'est pas chargé */
  function verses(a) {
    if (a._v) return a._v;
    const T = lue('texte/' + fichier(a.livre)), G = lue('targoum/' + fichier(a.livre)); if (!T || !G) return null;
    const he = L.versets(a.livre, a.debut, a.fin, T), tg = L.versets(a.livre, a.debut, a.fin, G), yc = yerCache();
    a._v = he.map((x, k) => { const r = x.c + ':' + x.v, full = a.livre + ' ' + r, o = tg[k].t; const v = { ref: r, he: x.t, onk: o };
      if (YER_EDITION[full]) { v.nt = 1; v.yer = o; } else if (skel(x.t) === skel(o)) { v.nt = 1; v.yer = yc[full] || ''; }
      return v; });
    return a._v;
  }
  /* Les versets d'un passage lu une fois, sans Targoum (haftara, maftir d'un Chabbat spécial) */
  function versesOnce(p) { const T = lue('texte/' + fichier(p.livre)); return T ? L.versets(p.livre, p.debut, p.fin, T).map(x => ({ ref: x.c + ':' + x.v, he: x.t })) : null; }

  /* Une semaine : la paracha du Chabbat [p.date], ses 7 alyot, son maftir et sa haftara selon le rite */
  function week(d, p, o) {
    const l = p.lecture, P = d.parachiot[p.paracha], reg = P['alyot_' + o.nusah] || P.alyot;
    const sept = reg.filter(a => /^[1-7]$/.test(a[0])), t = new Date(p.date + 'T12:00:00Z');
    const alyot = sept.map((a, i) => { const n = L.nombreVersets(a[2], a[3], d.longueurs[a[1]]);
      return { name: NAMES[i], heb: HEB[i], day: JOURS[i], verses: span(a[2], a[3]), min: Math.max(3, Math.round(n * 0.4)), count: n,
        ref: a[1] + ' ' + a[2] + '-' + a[3], livre: a[1], debut: a[2], fin: a[3], get v() { return verses(this); } }; });
    /* Chabbat spécial : le maftir (et, avec trois Sifrei Torah, la septième montée) qui ne sont pas de la paracha */
    const base = {}; reg.forEach(a => { base[a[0]] = a.slice(1).join(' '); });
    const extra = l.montees.filter(m => (m.cle === '7' || m.cle === 'M') && base[m.cle] !== [m.livre, m.debut, m.fin].join(' '))
      .map(m => ({ label: nom(m.libelle), livre: m.livre, debut: m.debut, fin: m.fin, ref: L.reference(d, m.livre, m.debut, m.fin, nom), count: L.nombreVersets(m.debut, m.fin, d.longueurs[m.livre]) }));
    const parts = l.haftara.map(h => ({ livre: h.livre, debut: h.debut, fin: h.fin, ref: L.reference(d, h.livre, h.debut, h.fin, nom), count: L.nombreVersets(h.debut, h.fin, d.longueurs[h.livre]) }));
    const count = parts.concat(extra).reduce((a, x) => a + x.count, 0);
    const index = L.PARSHIOT.indexOf((L.JOINTES[p.paracha] || [p.paracha])[0]) - 1;
    return { shabbatISO: p.date, shabbat: t.getUTCDate() + ' ' + MONTHS[t.getUTCMonth()], key: p.paracha, cle: l.cle,
      parasha: nom(l.titre), parashaHe: l.titre.he, parashaEn: l.titre.en, parashaIndex: index,
      parashaRef: L.reference(d, sept[0][1], sept[0][2], sept[6][3], nom).replace('–', ' – '), alyot,
      haftara: { parts, extra, origine: l.haftaraDe, premier: parts.length ? parts[0].livre + ' ' + parts[0].debut + '-' + parts[0].fin : '', ref: parts.map(x => x.ref).join(' ; '), extraRef: extra.map(x => x.label + ' : ' + x.ref).join(' ; '), reasons: l.raisons.map(nom), rite: RITES[o.nusah],
        min: Math.max(2, Math.round(count * 0.15)), count } };
  }

  /* Les semaines autour d'aujourd'hui : un Chabbat de Yom tov ou de 'Hol hamoed n'a pas de paracha, on passe
     à la suivante (jamais une lecture de fête : on ne lit pas Chnayim mikra pour Yom tov). */
  const AVANT = 60, APRES = 8;
  let memo = null;
  function weeks() {
    const d = lue('lecture'); if (!d || !L) return [];
    const o = options(), today = localISO(now(), city().tz);
    const stamp = [o.enIsrael, o.mukafChoma, o.nusah, get('lang'), today].join('|');
    if (memo && memo.stamp === stamp) return memo.list;
    const list = [], seen = {}, end = addDays(today, 7 * APRES);
    for (let iso = L.chabbatSuivant(addDays(today, -7 * AVANT)); iso <= end; iso = addDays(iso, 7)) {
      const p = L.parachaSemaine(d, iso, o); if (seen[p.date]) continue; seen[p.date] = 1; list.push(week(d, p, o));
    }
    memo = { stamp, list }; return list;
  }
  /* Le contexte d'une haftara (data/contexte_haftarot.json) : celui qui nomme son origine et son premier passage.
     Phrases en français (aussi pour le tunisien et le marocain) ou en anglais ; chaque source avec son lien. */
  function contexte(h) {
    const C = lue('contexte'); if (!C || !h || !h.premier) return null;
    const c = C.contextes.find(x => x.occasions.indexOf(h.origine) >= 0 && x.passages.indexOf(h.premier) >= 0); if (!c) return null;
    const en = NOMS[get('lang')] === 'en' || get('lang') === 'he', lg = en ? 'en' : 'fr';
    return c.phrases.map(ph => ({ text: ph[lg], sources: ph.sources.map(s => ({ ref: s.ref[lg], citation: s.citation || '', hasCitation: !!s.citation,
      lien: s.genre === 'classique' ? 'https://www.sefaria.org/' + encodeURI(s.sefaria.replace(/ /g, '_')) + '?lang=he' : s.url })) }));
  }

  /* Ce qu'il faut charger pour lire une semaine : le texte et le Targoum de son livre, et les livres de la haftara */
  function needs(w, haftara) {
    const n = {}; w.alyot.forEach(a => { n['texte/' + fichier(a.livre)] = 1; n['targoum/' + fichier(a.livre)] = 1; });
    if (haftara) w.haftara.parts.concat(w.haftara.extra).forEach(x => { n['texte/' + fichier(x.livre)] = 1; });
    return Object.keys(n);
  }
  const ready = (w, haftara) => needs(w, haftara).every(lue);
  const ensure = (w, haftara) => (ready(w, haftara) ? Promise.resolve() : Promise.all(needs(w, haftara).map(n => SM_DONNEES.charge(n))));

  /* Semaine en cours : la première dont le Shabbat n'est pas encore sorti (les semaines de fête sont sautées) */
  function state() {
    const c = city(), t = now(), W = weeks();
    let ci = W.findIndex(w => shabbatEnd(w.shabbatISO, c) > t);
    if (ci < 0) ci = W.length - 1;
    return { c, t, W, ci, cur: W[ci] || null };
  }

  /* ---------- Progression : alyot lues par semaine (clé = date du Shabbat) ---------- */
  function progAll() { try { return JSON.parse(localStorage.getItem('sm.prog') || '{}'); } catch (e) { return {}; } }
  function progSet(w, n, haftara) { if (!w) return; const p = progAll(); const old = p[w.shabbatISO] || {};
    const val = { n: Math.max(0, Math.min(7, n)), name: w.parasha, he: w.parashaHe }; if (old.h || haftara) val.h = 1;
    if (old.n === val.n && old.name === val.name && !!old.h === !!val.h) return; p[w.shabbatISO] = val; try { localStorage.setItem('sm.prog', JSON.stringify(p)); } catch (e) {} }
  const progN = (w) => w ? ((progAll()[w.shabbatISO] || {}).n || 0) : 0;
  const progH = (w) => !!(w && (progAll()[w.shabbatISO] || {}).h);
  function touch(w) { if (w && !progAll()[w.shabbatISO]) progSet(w, 0); }
  window.SM_DONE = { get: () => progN(state().cur), set: (n) => progSet(state().cur, n) };

  /* Semaine affichée par le lecteur : par = 0 (en cours), 1..3 (suivantes), -1 (précédente) ou date ISO */
  function weekFor(par) {
    const s = state();
    if (typeof par === 'string' && par.indexOf('-') > 0 && par.length === 10) return weeks().find(w => w.shabbatISO === par) || s.cur;
    const k = Number(par) || 0; return s.W[s.ci + k] || s.cur;
  }
  function alyaIndex() { const a = get('alya'); return (a === undefined || a === null) ? Math.min(6, progN(state().cur)) : a; }
  window.SM_WEEK = (par) => weekFor(par === undefined ? get('par') : par);
  window.SM_ALYOT = () => { const w = state().cur; return w && w.alyot ? w.alyot : null; };
  /* Fin d'une alya dans le lecteur ; la haftara (alya = 7) est notée à part, hors des 7 alyot */
  window.SM_MARK = function () { const w = weekFor(get('par')); const i = alyaIndex(); if (!w) return; if (i >= 7) progSet(w, progN(w), true); else progSet(w, Math.max(progN(w), i + 1)); };

  window.SM_G = function () {
    const s = state(), c = s.c, w = s.cur || FALLBACK, R = weekFor(get('par')) || w, al = R.alyot || null, i = alyaIndex();
    if (s.cur) touch(s.cur);
    const nRead = progN(R);
    const next = nRead < 7 && al ? NAMES[Math.min(6, nRead)] + ', ' + al[Math.min(6, nRead)].min + ' min' : null;
    const d = new Date(s.t), todayIso = localISO(s.t, c.tz);
    const out = { parasha: w.parasha, parashaHe: w.parashaHe, parashaRef: w.parashaRef, readParasha: R.parasha, readIso: R.shabbatISO || '',
      date: cap(DAYS[dow(todayIso)]) + ' ' + d.getDate() + ' ' + MONTHS[d.getMonth()], alyaName: i >= 7 ? 'Haftara' : (NAMES[i] || NAMES[0]), doneTitle: i >= 7 ? 'Haftara terminée' : (NAMES[i] || NAMES[0]) + ' terminé',
      afterText: (i >= 7 ? 'La haftara est lue. ' : '') + (next ? 'Prochaine alya : ' + next + '.' : 'La paracha est terminée. Shabbat Shalom !'), cityName: c.name, place: isIL() ? 'Israël' : 'Diaspora' };
    /* Haftara de la semaine, selon le rite : lue une fois, sans Targoum, hors des 7 alyot */
    const hf = s.cur && s.cur.haftara && s.cur.haftara.parts.length ? s.cur.haftara : null;
    out.hasHaftara = !!hf;
    out.haftara = hf ? { ref: hf.ref, rite: hf.rite, min: hf.min, done: progH(s.cur), todo: !progH(s.cur), href: 'V2-Lecteur.dc.html?par=0&alya=7',
      reason: hf.reasons.join(' · '), hasReason: hf.reasons.length > 0, extra: hf.extraRef, hasExtra: hf.extra.length > 0 } : null;
    if (hf) { const cx = contexte(hf); out.haftara.contexte = cx || []; out.haftara.hasContexte = !!cx; }
    /* Allumage et compte à rebours */
    if (s.cur) {
      const cl = candle(s.cur.shabbatISO, c), left = cl - s.t, n = progN(s.cur);
      out.candle = hhmm(cl, c.tz);
      out.candleLine = 'Allumage ' + (left > 0 ? 'vendredi' : '') + ' à ' + out.candle + ' · ' + c.name + ' (coucher du soleil − ' + c.off + ' min)';
      out.countdown = left > 0 ? 'Chabbat dans ' + inDur(left) : 'Chabbat Chalom';
      out.goal = n >= 7 ? 'Paracha terminée' : left > 0 ? 'Objectif : finir avant Chabbat' : 'Encore possible ce Chabbat, avant le repas de midi';
      out.friday = left > 0 && left < 30 * 3600e3 && dow(todayIso) === 5 && n < 7;
    } else { out.candleLine = 'Allumage selon ta ville'; out.countdown = ''; out.goal = ''; out.friday = false; }
    /* Rattrapage de la semaine passée : jusqu'à mardi soir */
    out.prev = null;
    const P = s.W[s.ci - 1];
    if (P && progN(P) < 7 && progAll()[P.shabbatISO]) {
      const end = tuesdayEnd(P.shabbatISO, c);
      if (s.t < end && s.t > shabbatEnd(P.shabbatISO, c)) { const n = progN(P);
        out.prev = { name: P.parasha, n, left: 7 - n, until: 'mardi ' + hhmm(end, c.tz), href: 'V2-Lecteur.dc.html?par=' + P.shabbatISO + '&alya=' + Math.min(6, n), canRead: !!P.alyot }; }
    }
    out.hasPrev = !!out.prev;
    /* Carnet : semaines non terminées, à compléter avant Sim'hat Torah */
    const st = simhatTorah(todayIso, 1, isIL()), stPrev = simhatTorah(todayIso, -1, isIL());
    const p = progAll(); const avail = {}; weeks().forEach(x => avail[x.shabbatISO] = x);
    out.carnet = Object.keys(p).sort().filter(iso => p[iso].n < 7 && (!s.cur || iso < s.cur.shabbatISO) && (!out.prev || iso !== P.shabbatISO) && (!stPrev || iso > stPrev))
      .map(iso => ({ name: p[iso].name, n: p[iso].n, label: p[iso].n + '/7 alyot', href: avail[iso] && avail[iso].alyot ? 'V2-Lecteur.dc.html?par=' + iso + '&alya=' + Math.min(6, p[iso].n) : '', canRead: !!(avail[iso] && avail[iso].alyot) }));
    out.hasCarnet = out.carnet.length > 0;
    out.stLabel = st ? "avant Sim'hat Torah (" + dayLabel(st, 1) + ')' : "avant Sim'hat Torah";
    /* Série : semaines terminées d'affilée */
    let streak = 0; const isos = Object.keys(p).sort().reverse();
    for (const iso of isos) { if (s.cur && iso === s.cur.shabbatISO && p[iso].n < 7) continue; if (p[iso].n >= 7) streak++; else break; }
    out.streak = streak;
    return out;
  };

  /* ---------- Textes du lecteur ---------- */
  /* La haftara : le maftir d'un Chabbat spécial s'il y en a un, puis la haftara ; chaque verset une fois */
  function haftaraBlocks(W) {
    const out = []; const h = W.haftara;
    for (const x of h.extra.map(e => [e, e.label]).concat(h.parts.map(e => [e, 'Haftara']))) {
      const vs = versesOnce(x[0]); if (!vs) return null;
      vs.forEach(v => out.push({ kind: 'mikra', n: 1, ref: v.ref, text: v.he, label: x[1] }));
    }
    return out.length ? out : null;
  }
  window.SM_BLOCKS = function () {
    const W = weekFor(get('par')); if (!W || !W.alyot) return null; const i = alyaIndex();
    if (i >= 7) return haftaraBlocks(W);
    const a = W.alyot[i], vs = a && a.v; if (!vs) return null;
    const ntMode = get('nt') || 'deux'; const out = [];
    /* Réglage « ×1 » : l'hébreu n'est affiché qu'une fois, l'étiquette rappelle combien de fois le lire */
    const une = !!get('une');
    vs.forEach(v => {
      const yer = v.nt && ntMode !== 'trois' && v.yer, trois = v.nt && (ntMode !== 'yer' || !yer);
      if (une) out.push({ kind: 'mikra', n: 1, ref: v.ref, text: v.he, label: trois ? 'Mikra · à lire 3 fois, pas de Targoum' : 'Mikra · à lire 2 fois' });
      else { out.push({ kind: 'mikra', n: 1, ref: v.ref, text: v.he }); out.push({ kind: 'mikra', n: 2, ref: v.ref, text: v.he }); }
      if (!v.nt) { out.push({ kind: 'targum', n: 3, ref: v.ref, text: v.onk }); return; }
      if (trois && !une) out.push({ kind: 'mikra', n: 3, ref: v.ref, text: v.he, label: '3ᵉ lecture · pas de Targoum' });
      if (yer) out.push({ kind: 'targum', n: 4, ref: v.ref, text: v.yer, label: 'Targoum Yerouchalmi' });
    });
    return out;
  };
  /* Les 3 prochaines parachiyot */
  window.SM_NEXT = function () {
    const s = state(); const list = s.W.slice(s.ci + 1, s.ci + 4);
    return list.map((w, k) => ({ name: w.parasha, heb: w.parashaHe, ref: w.parashaRef, when: 'Shabbat ' + w.shabbat,
      href: w.alyot ? 'V2-Lecteur.dc.html?par=' + (k + 1) + '&alya=0' : '#', canRead: !!w.alyot }));
  };

  /* ---------- Impression : ce qu'il reste (ou toute la paracha), puis la haftara ---------- */
  window.SM_PRINT_INFO = function (all) {
    const w = state().cur; if (!w || !w.alyot || !ready(w, false)) return null; const from = all ? 0 : Math.min(6, progN(w));
    const al = w.alyot.slice(from); let chars = al.reduce((a, x) => a + x.v.reduce((b, v) => b + v.he.length + (v.onk || '').length, 0), 0);
    const hb = haftaraBlocks(w); if (hb) chars += hb.reduce((a, b) => a + b.text.length, 0);
    return { from, names: al.map(a => a.name), range: al.length > 1 ? al[0].name + ' – ' + al[al.length - 1].name : al[0].name, first: al[0].name + ' · ' + al[0].v[0].ref,
      min: al.reduce((a, x) => a + x.min, 0), pages: Math.max(1, Math.ceil(chars / 3400)), count: al.length, haftara: hb ? w.haftara.ref : '' };
  };
  const esc = (s) => String(s || '').replace(/[&<>]/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' })[ch]);
  window.SM_PRINT = function (all) {
    const w = state().cur; const info = window.SM_PRINT_INFO(all); if (!info) return false;
    const ntMode = get('nt') || 'deux';
    let h = '<header><span>' + esc(w.parasha) + ' · ' + esc(info.range) + '</span><span lang="he" dir="rtl">' + esc(w.parashaHe) + '</span></header>' +
      '<p class="how">Chaque verset deux fois, puis le Targoum. ✱ = verset sans Targoum Onkelos : le lire trois fois.</p>';
    w.alyot.slice(info.from).forEach(a => {
      h += '<h2><span>' + esc(a.name) + ' · ' + esc(a.verses) + '</span><span lang="he" dir="rtl">' + esc(a.heb) + '</span></h2>';
      a.v.forEach(v => {
        h += '<div class="pv"><p class="he" dir="rtl" lang="he"><b>' + esc(v.ref) + '</b> ' + esc(v.he) + (v.nt ? ' ✱' : '') + '</p>';
        if (!v.nt) h += '<p class="tg" dir="rtl" lang="arc">' + esc(v.onk) + '</p>';
        else if (v.yer && ntMode !== 'trois') h += '<p class="tg" dir="rtl" lang="arc"><i>Targoum Yerouchalmi</i> · ' + esc(v.yer) + '</p>';
        h += '</div>';
      });
    });
    /* La haftara (et le maftir d'un Chabbat spécial) : une fois, sans Targoum */
    const hb = haftaraBlocks(w);
    if (hb) {
      const hf = w.haftara; let label = null;
      h += '<p class="how">Haftara selon le rite ' + esc(hf.rite) + (hf.reasons.length ? ' · ' + esc(hf.reasons.join(' · ')) : '') + ' : une fois, sans Targoum.</p>';
      hb.forEach(b => {
        if (b.label !== label) { label = b.label; h += '<h2><span>' + esc(label) + ' · ' + esc(label === 'Haftara' ? hf.ref : hf.extraRef) + '</span><span lang="he" dir="rtl">' + (label === 'Haftara' ? 'הַפְטָרָה' : '') + '</span></h2>'; }
        h += '<div class="pv"><p class="he" dir="rtl" lang="he"><b>' + esc(b.ref) + '</b> ' + esc(b.text) + '</p></div>';
      });
    }
    let el = document.getElementById('print'); if (!el) { el = document.createElement('div'); el.id = 'print'; document.body.appendChild(el); }
    el.innerHTML = h; document.title = 'Shnayim Mikra — ' + w.parasha;
    if (window.SMAndroid && SMAndroid.print) SMAndroid.print('Shnayim Mikra — ' + w.parasha); else window.print();
    return true;
  };

  /* ---------- Chargement du texte (embarqué) avant d'ouvrir un écran qui le lit ---------- */
  /* null : rien à attendre ; sinon une promesse, tenue quand le texte de la semaine est chargé */
  window.SM_PREPARE = function (name) {
    if (!window.SM_DONNEES || !lue('lecture')) return null;
    const w = name === 'lecteur' ? weekFor(get('par')) : name === 'imprimer' ? state().cur : null; if (!w) return null;
    const haftara = name === 'imprimer' || alyaIndex() >= 7;
    return ready(w, haftara) ? null : ensure(w, haftara);
  };
  window.SM_OK = () => !!(L && lue('lecture'));

  /* ---------- En arrière-plan : le texte de la semaine en cours, puis le Targoum Yerouchalmi (en ligne) ---------- */
  /* Le Targoum Yerouchalmi des versets sans Targoum vient de Sefaria quand le téléphone est en ligne, puis reste
     gardé (sm.yer). Hors ligne, ces versets se lisent trois fois ; Bamidbar 32:3 a le sien dans l'édition. */
  async function yerushalmi(w) {
    if (!window.SM_SEFARIA || navigator.onLine === false) return false;
    const c = yerCache(); let changed = false;
    for (const a of w.alyot) for (const v of (a.v || [])) {
      const full = a.livre + ' ' + v.ref; if (!v.nt || v.yer || full in c) continue;
      try { c[full] = await SM_SEFARIA.yerushalmi(full); changed = true; } catch (e) { break; }
    }
    if (changed) { try { localStorage.setItem('sm.yer', JSON.stringify(c)); } catch (e) {} memo = null; }
    return changed;
  }
  window.SM_REFRESH = async function () {
    const w = state().cur; if (!w || window.__smRefreshing) return; window.__smRefreshing = true;
    try {
      await ensure(w, true);
      /* Le contexte des haftarot, s'il est dans cette copie de l'application : chargé une fois, puis affiché */
      if (!lue('contexte')) { try { await SM_DONNEES.charge('contexte'); if (window.SM_RERENDER) SM_RERENDER(); } catch (e) { /* pas encore rédigé */ } }
      if (await yerushalmi(w)) { if (window.SM_RERENDER) SM_RERENDER(); }
    }
    catch (e) { /* données absentes : l'accueil le dit */ }
    finally { window.__smRefreshing = false; }
  };
  /* Les anciens textes téléchargés de Sefaria (versions de test d'avant le texte embarqué) ne servent plus */
  try { localStorage.removeItem('sm.text.israel'); localStorage.removeItem('sm.text.diaspora'); } catch (e) {}
})();
