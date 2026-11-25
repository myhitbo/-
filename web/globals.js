/* Shnayim Mikra — données partagées : semaines (Sefaria), Israël/diaspora, heure d'allumage,
   échéances, progression par semaine, textes du lecteur, impression. */
(function () {
  /* Noms dans la langue de l'interface (voir i18n.js) : alya n° i, paracha d'une semaine, référence « Livre chap:verset » */
  const AN = (i) => window.SM_ALYA(i);
  const FR_BOOKS = ['Béréchit', 'Chemot', 'Vayikra', 'Bamidbar', 'Devarim'];
  const pn = (w) => w ? window.SM_PARASHA(idxOf(w), w.parasha || w.name || '') : '';
  const pref = (w) => { const m = String((w && w.parashaRef) || '').match(/^(.+?) (\d.*)$/); if (!m) return (w && w.parashaRef) || ''; const i = FR_BOOKS.indexOf(m[1]); return (i >= 0 ? window.SM_BOOK(i) : m[1]) + ' ' + m[2]; };
  const noon = (iso) => Date.parse(iso + 'T12:00:00Z');
  const FALLBACK = { parasha: 'Vayétsé', parashaHe: 'וַיֵּצֵא', parashaRef: 'Béréchit 28:10 – 32:3' };
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
  window.SM_CITY_LIST = () => { const cur = city(); return CITIES.filter(c => c.il === isIL()).map(c => ({ id: c.id, name: window.SM_CITY_NAME(c), on: c.id === cur.id })); };

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
  const dayLabel = (iso, y) => window.SM_DATE(noon(iso), y ? { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' } : { weekday: 'long', day: 'numeric', month: 'long' });
  const candle = (shIso, c) => sunset(addDays(shIso, -1), c) - c.off * 60e3;
  const shabbatEnd = (shIso, c) => sunset(shIso, c) + 42 * 60e3;
  const tuesdayEnd = (shIso, c) => sunset(addDays(shIso, 3), c);
  function inDur(ms) { const m = Math.max(0, Math.round(ms / 60e3)); const d = Math.floor(m / 1440), h = Math.floor(m % 1440 / 60), mi = m % 60, T = window.SM_TR(), F = window.SM_FMT;
    return d ? F(T.durDH, { d, h }) : h ? F(T.durHM, { h, m: String(mi).padStart(2, '0') }) : F(T.durM, { m: mi }); }
  window.SM_ZMAN = { sunset, candle, hhmm, localISO, addDays };

  /* ---------- Sim'hat Torah : 22 Tichri en Israël (Chemini Atséret), 23 Tichri en diaspora ---------- */
  let hebF, hebY; try { hebF = new Intl.DateTimeFormat('en-u-ca-hebrew', { day: 'numeric', month: 'long', timeZone: 'UTC' });
    hebY = new Intl.DateTimeFormat('en-u-ca-hebrew', { year: 'numeric', timeZone: 'UTC' }); } catch (e) {}
  function simhatTorah(fromIso, dir, il) {
    if (!hebF) return null; const want = il ? 22 : 23;
    for (let k = 0; k < 400; k++) { const iso = addDays(fromIso, dir * k); const p = {}; hebF.formatToParts(new Date(iso + 'T12:00:00Z')).forEach(x => p[x.type] = x.value);
      if (p.month === 'Tishri' && +p.day === want) return iso; }
    return null;
  }

  /* ---------- Données : texte embarqué + cache téléchargé, par lieu ---------- */
  const key = () => isIL() ? 'israel' : 'diaspora';
  function cacheGet() { try { return JSON.parse(localStorage.getItem('sm.text.' + key()) || 'null'); } catch (e) { return null; } }
  let memo = null;
  function weeks() {
    const k = key(), c = cacheGet(), stamp = k + (c ? c.at : '');
    if (memo && memo.stamp === stamp) return memo.list;
    const T = window.SM_TEXT; const by = {};
    const base = T ? (T[k] ? T[k].weeks : (T.weeks || [])) : [];
    base.concat(c ? c.weeks : []).forEach(w => { if (w && w.shabbatISO) by[w.shabbatISO] = w; });
    const list = Object.keys(by).sort().map(i => by[i]);
    memo = { stamp, list }; return list;
  }
  /* Semaine en cours : la première dont le Shabbat n'est pas encore sorti (les semaines de fête sont sautées) */
  function state() {
    const c = city(), t = now(), W = weeks().filter(w => !w.holiday);
    let ci = W.findIndex(w => shabbatEnd(w.shabbatISO, c) > t);
    if (ci < 0) ci = W.length - 1;
    return { c, t, W, ci, cur: W[ci] || null };
  }

  /* Numéros (0 à 53) des parachiyot d'une semaine, ou d'une ligne de progression ; deux numéros pour une paracha double */
  function idxOf(w) {
    const S = window.SM_SEFARIA; if (!w || !S) return [];
    if (Array.isArray(w.idx)) return w.idx;
    const en = w.parashaEn || '';
    if (en) { const one = S.EN.indexOf(en); const parts = one >= 0 ? [one] : en.split('-').map(x => S.EN.indexOf(x.trim())); if (parts.every(i => i >= 0)) return parts; }
    return String(w.name || w.parasha || '').split(' – ').map(x => S.FR.indexOf(x.trim())).filter(i => i >= 0);
  }

  /* ---------- Progression : alyot lues par semaine (clé = date du Shabbat) ---------- */
  function progAll() { try { return JSON.parse(localStorage.getItem('sm.prog') || '{}'); } catch (e) { return {}; } }
  function progSet(w, n) { if (!w) return; const p = progAll(); const old = p[w.shabbatISO] || {}; p[w.shabbatISO] = { n: Math.max(0, Math.min(7, n)), name: w.parasha, he: w.parashaHe, idx: idxOf(w) };
    if (old.n === p[w.shabbatISO].n && old.name) return; try { localStorage.setItem('sm.prog', JSON.stringify(p)); } catch (e) {}
    if (window.SM_SYNC_REMINDERS) SM_SYNC_REMINDERS(); }
  const progN = (w) => w ? ((progAll()[w.shabbatISO] || {}).n || 0) : 0;
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
  /* Les 7 alyot de la semaine, avec leur durée calculée (sec = secondes, min = minutes arrondies) */
  window.SM_ALYOT = () => { const w = state().cur; return w && w.alyot ? w.alyot.map(a => { const sec = alyaSec(a); return Object.assign({}, a, { sec, min: toMin(sec) }); }) : null; };
  /* Fin d'une alya dans le lecteur */
  /* Séance ouverte dans le lecteur : alyot from..to de la semaine choisie (une seule alya si `alyaTo` est absent) */
  function portion() {
    const W = weekFor(get('par')); if (!W || !W.alyot) return null;
    const from = alyaIndex(); let to = get('alyaTo'); to = (to === undefined || to === null || to < from) ? from : Math.min(6, to);
    return { W, from, to };
  }
  window.SM_PORTION = function () { const P = portion(); return P ? { from: P.from, to: P.to, order: get('order') || 0, names: [0, 1, 2, 3, 4, 5, 6].map(AN) } : null; };
  /* Progression depuis le lecteur : `upTo` alyot lues (sans argument : toute la séance) */
  window.SM_MARK = function (upTo) { const P = portion(); if (!P) return; progSet(P.W, Math.max(progN(P.W), upTo === undefined ? P.to + 1 : upTo)); };

  /* ---------- Rythme : la semaine découpée en séances ----------
     rh : 0 = une alya par jour · 1 = toute la paracha d'un coup (jour choisi) · 2 = 2 ou 3 séances · 3 = libre.
     Une séance = alyot from..to, prévue un jour de la semaine (0 = dimanche … 6 = Shabbat). */
  function sessions() {
    const rh = get('rh') || 0;
    if (rh === 1) { const d = get('rhDay'); return [{ from: 0, to: 6, day: (d === undefined || d === null) ? 4 : d }]; }
    if (rh === 2) return get('rhN') === 2 ? [{ from: 0, to: 3, day: 1 }, { from: 4, to: 6, day: 4 }] : [{ from: 0, to: 2, day: 0 }, { from: 3, to: 4, day: 2 }, { from: 5, to: 6, day: 4 }];
    return [0, 1, 2, 3, 4, 5, 6].map(i => ({ from: i, to: i, day: i }));
  }
  /* ---------- Temps de lecture ----------
     Tout part du nombre de mots à lire et de la vitesse choisie dans le lecteur (réglage `spd`) :
     à ×1, WPM mots à la minute pour le texte hébreu ; le Targoum est lu plus lentement (réglage `tf`, 0,8 = 20 % plus lent).
     Le même calcul sert au défilement automatique, au temps restant et à toutes les durées affichées :
     ils ne dépendent donc ni de la taille du texte ni de la largeur de l'écran. */
  const WPM = 160, SPEEDS = [0.5, 0.75, 1, 1.25, 1.5, 2, 2.5, 3], SPEED0 = 2;
  const wordCount = (s) => { const m = String(s || '').trim(); return m ? m.split(/[\s\u05BE]+/).length : 0; };
  const speedIndex = () => { const i = get('spd'); return (i === undefined || i === null || !SPEEDS[i]) ? SPEED0 : i; };
  const targumFactor = () => { const t = get('tf'); return (t === undefined || t === null) ? 0.8 : t; };
  /* Secondes pour lire un texte une fois (au moins une seconde) */
  const readSec = (text, isTargum) => Math.max(1, wordCount(text) / (WPM * SPEEDS[speedIndex()] / 60 * (isTargum ? targumFactor() : 1)));
  /* Secondes pour une alya : chaque verset deux fois, puis son Targoum (ou ce qui le remplace quand Onkelos ne traduit pas) */
  function alyaSec(a) {
    if (!a || !a.v) return ((a && a.min) || 0) * 60;
    const nt = get('nt') || 'deux'; let s = 0;
    a.v.forEach(v => { s += 2 * readSec(v.he);
      if (!v.nt) { s += readSec(v.onk, true); return; }
      const yer = nt !== 'trois' && v.yer; if (nt !== 'yer' || !yer) s += readSec(v.he); if (yer) s += readSec(v.yer, true); });
    return s;
  }
  const toMin = (sec) => Math.max(1, Math.round(sec / 60));
  window.SM_SPEEDS = SPEEDS;
  window.SM_SPEED_INDEX = speedIndex;
  window.SM_BLOCK_SEC = (b) => readSec(b.text, b.kind === 'targum');   /* durée d'un bloc du lecteur */

  const sessionAt = (n) => { const from = Math.min(6, n); return sessions().find(x => from >= x.from && from <= x.to) || { from, to: 6, day: 6 }; };
  const rangeMin = (w, from, to) => w && w.alyot ? toMin(w.alyot.slice(from, to + 1).reduce((a, x) => a + alyaSec(x), 0)) : 0;
  /* Jour dans la semaine de lecture : 0 = dimanche … 6 = Shabbat ; −1 le samedi soir, une fois le Shabbat précédent sorti */
  function dayInWeek(s) {
    const today = localISO(s.t, s.c.tz); if (!s.cur) return dow(today);
    return Math.round((Date.parse(today + 'T12:00:00Z') - Date.parse(addDays(s.cur.shabbatISO, -6) + 'T12:00:00Z')) / 864e5);
  }
  /* Prochaine séance de la semaine en cours, et nombre d'alyot en retard sur le rythme choisi */
  window.SM_PLAN = function () {
    const s = state(), n = progN(s.cur), rh = get('rh') || 0, d = dayInWeek(s), cur = sessionAt(n);
    const due = rh === 3 ? 0 : sessions().filter(x => x.day < d).reduce((a, x) => Math.max(a, x.to + 1), 0);
    return { rh, from: Math.min(6, n), to: cur.to, day: cur.day, today: d, late: n >= 7 ? 0 : Math.max(0, due - n), done: n >= 7, min: rangeMin(s.cur, Math.min(6, n), cur.to), names: [0, 1, 2, 3, 4, 5, 6].map(AN) };
  };

  /* Année en cours (depuis le dernier Sim'hat Torah) : parachiyot vraiment terminées, commencées, et celle(s) de la semaine */
  window.SM_YEAR = function () {
    const s = state(), stPrev = simhatTorah(localISO(s.t, s.c.tz), -1, isIL());
    let year = ''; try { if (hebY && stPrev) year = hebY.formatToParts(new Date(stPrev + 'T12:00:00Z')).find(x => x.type === 'year').value; } catch (e) {}
    const p = progAll(), done = {}, part = {};
    Object.keys(p).forEach(iso => { if (stPrev && iso <= stPrev) return;
      idxOf(p[iso]).forEach(i => { if (p[iso].n >= 7) done[i] = 1; else if (p[iso].n > 0) part[i] = Math.max(part[i] || 0, p[iso].n); }); });
    Object.keys(done).forEach(i => { delete part[i]; });
    return { year, done, part, cur: s.cur ? idxOf(s.cur) : [], count: Object.keys(done).length };
  };

  window.SM_G = function () {
    const s = state(), c = s.c, w = s.cur || FALLBACK, R = weekFor(get('par')) || w, al = R.alyot || null, i = alyaIndex();
    if (s.cur) touch(s.cur);
    const nRead = progN(R);
    const T = window.SM_TR(), F = window.SM_FMT, nx = nRead < 7 && al ? sessionAt(nRead) : null, nf = Math.min(6, nRead);
    const d = new Date(s.t), todayIso = localISO(s.t, c.tz);
    const out = { parasha: pn(w), parashaHe: window.SM_HEB(pn(w), w.parashaHe), parashaRef: pref(w), readParasha: pn(R), readIso: R.shabbatISO || '',
      date: cap(window.SM_DATE(s.t, { weekday: 'long', day: 'numeric', month: 'long' }, c.tz)), alyaName: AN(i) || AN(0),
      afterText: !nx ? T.nextNone : nx.to > nf ? F(T.nextRange, { a: AN(nf), b: AN(nx.to), min: rangeMin(R, nf, nx.to) }) : F(T.nextOne, { name: AN(nf), min: rangeMin(R, nf, nf) }), cityName: window.SM_CITY_NAME(c), place: isIL() ? T.israel : T.diaspora };
    out.allReadLine = F(T.allRead, { parasha: out.parasha });
    /* Allumage et compte à rebours */
    if (s.cur) {
      const cl = candle(s.cur.shabbatISO, c), left = cl - s.t, n = progN(s.cur);
      out.candle = hhmm(cl, c.tz);
      out.candleLine = F(left > 0 ? T.candleFri : T.candle, { time: out.candle, city: window.SM_CITY_NAME(c), min: c.off });
      out.countdown = left > 0 ? F(T.shabbatIn, { dur: inDur(left) }) : T.shabbatShalom;
      out.goal = n >= 7 ? T.doneAll : left > 0 ? T.goalBefore : T.goalShabbat;
      out.friday = left > 0 && left < 30 * 3600e3 && dow(todayIso) === 5 && n < 7;
    } else { out.candleLine = T.candleNoData; out.countdown = ''; out.goal = ''; out.friday = false; }
    /* Rattrapage de la semaine passée : jusqu'à mardi soir */
    out.prev = null;
    const P = s.W[s.ci - 1];
    if (P && progN(P) < 7 && progAll()[P.shabbatISO]) {
      const end = tuesdayEnd(P.shabbatISO, c);
      if (s.t < end && s.t > shabbatEnd(P.shabbatISO, c)) { const n = progN(P);
        out.prev = { name: pn(P), n, left: 7 - n, title: F(T.prevUntil, { time: hhmm(end, c.tz) }), line: F(T.prevLine, { n, left: 7 - n }), href: 'V2-Lecteur.dc.html?par=' + P.shabbatISO + '&alya=' + Math.min(6, n), canRead: !!P.alyot }; }
    }
    out.hasPrev = !!out.prev;
    /* Carnet : semaines non terminées, à compléter avant Sim'hat Torah */
    const st = simhatTorah(todayIso, 1, isIL()), stPrev = simhatTorah(todayIso, -1, isIL());
    const p = progAll(); const avail = {}; weeks().forEach(x => avail[x.shabbatISO] = x);
    out.carnet = Object.keys(p).sort().filter(iso => p[iso].n < 7 && (!s.cur || iso < s.cur.shabbatISO) && (!out.prev || iso !== P.shabbatISO) && (!stPrev || iso > stPrev))
      .map(iso => ({ name: pn(p[iso]), n: p[iso].n, label: F(T.nOf7, { n: p[iso].n }), href: avail[iso] && avail[iso].alyot ? 'V2-Lecteur.dc.html?par=' + iso + '&alya=' + Math.min(6, p[iso].n) : '', canRead: !!(avail[iso] && avail[iso].alyot) }));
    out.hasCarnet = out.carnet.length > 0;
    out.stLabel = st ? F(T.completeBeforeST, { date: dayLabel(st, 1) }) : T.completeBeforeST0;
    /* Série : semaines terminées d'affilée */
    let streak = 0; const isos = Object.keys(p).sort().reverse();
    for (const iso of isos) { if (s.cur && iso === s.cur.shabbatISO && p[iso].n < 7) continue; if (p[iso].n >= 7) streak++; else break; }
    out.streak = streak;
    out.yearDone = window.SM_YEAR().count;
    const plan = window.SM_PLAN(); out.hasLate = !!s.cur && plan.late > 0; out.lateLine = plan.late === 1 ? T.late1 : F(T.lateN, { n: plan.late });
    return out;
  };

  /* ---------- Textes du lecteur ---------- */
  window.SM_BLOCKS = function () {
    const P = portion(); if (!P) return null;
    const al = P.W.alyot.slice(P.from, P.to + 1); if (!al.length || !al[0]) return null;
    const t = window.SM_TR(), ntMode = get('nt') || 'deux', order = get('order') || 0, out = [];
    /* Versets de la séance, dans l'ordre : al = numéro de l'alya, vi = rang du verset dans la séance */
    const V = []; al.forEach((a, k) => a.v.forEach(v => V.push({ v, al: P.from + k, vi: V.length + 1 })));
    const add = (x, kind, n, text, label) => out.push({ kind, n, ref: x.v.ref, text, al: x.al, aln: AN(x.al), vi: x.vi, label: label || '' });
    const mik = (x, n) => add(x, 'mikra', n, x.v.he);
    const tg = (x) => {   /* le Targoum du verset, ou ce qui le remplace quand Onkelos ne le traduit pas */
      if (!x.v.nt) { add(x, 'targum', 3, x.v.onk); return; }
      const yer = ntMode !== 'trois' && x.v.yer;
      if (ntMode !== 'yer' || !yer) add(x, 'mikra', 3, x.v.he, t.read3nt);
      if (yer) add(x, 'targum', 4, x.v.yer, t.yer);
    };
    if (order === 0) { V.forEach(x => { mik(x, 1); mik(x, 2); tg(x); }); return out; }
    /* Lectures groupées : chaque groupe est lu deux fois, puis vient son Targoum.
       1 = par paragraphe (jamais à cheval sur deux alyot) · 2 = par alya · 3 = toute la séance */
    let groups = [];
    if (order === 3) groups = [V];
    else if (order === 2) groups = al.map((a, k) => V.filter(x => x.al === P.from + k));
    else { let cur = []; V.forEach((x, i) => { cur.push(x); if (x.v.pb || i === V.length - 1 || V[i + 1].al !== x.al) { groups.push(cur); cur = []; } }); }
    groups.forEach(grp => { if (!grp.length) return;
      const a = grp[0], b = grp[grp.length - 1];
      const name = order === 1 ? (a.v.ref === b.v.ref ? a.v.ref : a.v.ref + ' – ' + b.v.ref) : a.al === b.al ? AN(a.al) : (a.al === 0 && b.al === 6) ? pn(P.W) : AN(a.al) + ' – ' + AN(b.al);
      [[1, t.read1], [2, t.read2]].forEach(pass => { const i = out.length; grp.forEach(x => mik(x, pass[0])); out[i].head = name + ' · ' + pass[1]; });
      const i = out.length; grp.forEach(tg); out[i].head = name + ' · ' + t.targum;
    });
    return out;
  };
  /* ---------- Rappels : liste des prochaines notifications, confiée à Android ---------- */
  /* Jours de fête où l'on n'écrit pas (Yom Tov) ; le second jour ne vaut qu'en diaspora */
  const YT = { Tishri: [1, 2, 10, 15, 22], Nisan: [15, 21], Sivan: [6] }, YT2 = { Tishri: [16, 23], Nisan: [16, 22], Sivan: [7] };
  function yomTov(iso, il) {
    if (!hebF) return false; const p = {}; hebF.formatToParts(new Date(iso + 'T12:00:00Z')).forEach(x => p[x.type] = x.value);
    return (YT[p.month] || []).indexOf(+p.day) >= 0 || (!il && (YT2[p.month] || []).indexOf(+p.day) >= 0);
  }
  const holy = (iso, il) => dow(iso) === 6 || yomTov(iso, il);
  /* Vrai si l'instant t tombe pendant Shabbat ou une fête, de l'allumage des bougies à la sortie des étoiles */
  function isRest(t, c) {
    const D = localISO(t, c.tz), h0 = holy(D, c.il), h1 = holy(addDays(D, 1), c.il);
    return (h0 && h1) || (h0 && t < sunset(D, c) + 42 * 60e3) || (h1 && t >= sunset(D, c) - c.off * 60e3);
  }
  window.SM_IS_REST = (t) => isRest(t === undefined ? now() : t, city());
  /* Les rappels des 21 prochains jours : [{ at, title, text }].
     Un rappel par jour où une séance est prévue et pas encore lue (les séances en retard s'y ajoutent) ;
     en rythme libre, un rappel par jour tant que la paracha n'est pas finie. Rien pendant Shabbat et les fêtes.
     La liste est recalculée à chaque ouverture de l'app et à chaque alya lue. */
  window.SM_REMINDERS = function () {
    if (get('rem') === false) return [];
    const hm = String(get('remAt') || '07:30').split(':').map(Number); if (isNaN(hm[0])) return [];
    const s = state(), c = s.c, T = window.SM_TR(), F = window.SM_FMT, rh = get('rh') || 0, ss = sessions(), out = [], d0 = new Date(s.t);
    for (let k = 0; k < 21; k++) {
      /* L'heure choisie est celle du téléphone (pas celle de la ville, qui ne sert qu'aux horaires de Shabbat) */
      const t = new Date(d0.getFullYear(), d0.getMonth(), d0.getDate() + k, hm[0], hm[1] || 0, 0, 0).getTime(), D = localISO(t, c.tz);
      if (t <= s.t + 60e3 || isRest(t, c)) continue;
      const w = s.W.find(x => shabbatEnd(x.shabbatISO, c) > t);   /* la semaine de lecture à cet instant */
      if (!w) { out.push({ at: t, title: 'Shnayim Mikra', text: T.remGeneric }); continue; }
      const n = progN(w); if (n >= 7) continue;
      const d = Math.round((Date.parse(D + 'T12:00:00Z') - Date.parse(addDays(w.shabbatISO, -6) + 'T12:00:00Z')) / 864e5);
      let to, late = 0;
      if (rh === 3) to = Math.min(6, n);
      else { const due = ss.filter(x => x.day <= d); if (!due.length) continue;
        to = due.reduce((a, x) => Math.max(a, x.to), 0); if (n > to) continue;
        late = Math.max(0, ss.filter(x => x.day < d).reduce((a, x) => Math.max(a, x.to + 1), 0) - n); }
      const from = Math.min(6, n), name = from === to ? AN(from) : (from === 0 && to === 6) ? T.wholeParasha : AN(from) + ' – ' + AN(to);
      const text = !w.alyot ? T.remGeneric : F(T.remMin, { min: rangeMin(w, from, to) }) + (late === 1 ? T.remLate1 : late > 1 ? F(T.remLateN, { n: late }) : '');
      out.push({ at: t, title: pn(w) + ' — ' + name, text });
    }
    return out;
  };
  let remTimer = 0;
  window.SM_SYNC_REMINDERS = function () {
    clearTimeout(remTimer);
    remTimer = setTimeout(function () { try { if (window.SMAndroid && SMAndroid.reminders) SMAndroid.reminders(JSON.stringify(window.SM_REMINDERS())); } catch (e) {} }, 400);
  };

  /* Les 3 prochaines parachiyot */
  window.SM_NEXT = function () {
    const s = state(); const list = s.W.slice(s.ci + 1, s.ci + 4);
    const T = window.SM_TR();
    return list.map((w, k) => ({ name: pn(w), heb: window.SM_HEB(pn(w), w.parashaHe), ref: pref(w), when: window.SM_FMT(T.shabbatDate, { date: window.SM_DATE(noon(w.shabbatISO), { day: 'numeric', month: 'long' }) }),
      href: w.alyot ? 'V2-Lecteur.dc.html?par=' + (k + 1) + '&alya=0' : '#', canRead: !!w.alyot }));
  };

  /* ---------- Impression : ce qu'il reste (ou toute la paracha) ---------- */
  window.SM_PRINT_INFO = function (all) {
    const w = state().cur; if (!w || !w.alyot) return null; const from = all ? 0 : Math.min(6, progN(w));
    const al = w.alyot.slice(from); const chars = al.reduce((a, x) => a + x.v.reduce((b, v) => b + v.he.length + (v.onk || '').length, 0), 0);
    return { from, names: al.map((a, k) => AN(from + k)), range: al.length > 1 ? AN(from) + ' – ' + AN(6) : AN(from), first: AN(from) + ' · ' + al[0].v[0].ref,
      min: rangeMin(w, from, 6), pages: Math.max(1, Math.ceil(chars / 3400)), count: al.length };
  };
  const esc = (s) => String(s || '').replace(/[&<>]/g, ch => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' })[ch]);
  window.SM_PRINT = function (all) {
    const w = state().cur; const info = window.SM_PRINT_INFO(all); if (!info) return false;
    const ntMode = get('nt') || 'deux', T = window.SM_TR();
    let h = '<header><span>' + esc(pn(w)) + ' · ' + esc(info.range) + '</span><span lang="he" dir="rtl">' + esc(window.SM_HEB(pn(w), w.parashaHe)) + '</span></header>' +
      '<p class="how">' + esc(T.printHow) + '</p>';
    w.alyot.slice(info.from).forEach((a, k) => {
      h += '<h2><span>' + esc(AN(info.from + k)) + ' · ' + esc(a.verses) + '</span><span lang="he" dir="rtl">' + esc(window.SM_HEB(AN(info.from + k), a.heb)) + '</span></h2>';
      a.v.forEach(v => {
        h += '<div class="pv"><p class="he" dir="rtl" lang="he"><b>' + esc(v.ref) + '</b> ' + esc(v.he) + (v.nt ? ' ✱' : '') + '</p>';
        if (!v.nt) h += '<p class="tg" dir="rtl" lang="arc">' + esc(v.onk) + '</p>';
        else if (v.yer && ntMode !== 'trois') h += '<p class="tg" dir="rtl" lang="arc"><i>' + esc(T.yer) + '</i> · ' + esc(v.yer) + '</p>';
        h += '</div>';
      });
    });
    let el = document.getElementById('print'); if (!el) { el = document.createElement('div'); el.id = 'print'; document.body.appendChild(el); }
    el.innerHTML = h; document.title = 'Shnayim Mikra — ' + pn(w);
    if (window.SMAndroid && SMAndroid.print) SMAndroid.print('Shnayim Mikra — ' + pn(w)); else window.print();
    return true;
  };

  /* ---------- Mise à jour en ligne (Sefaria), en arrière-plan ---------- */
  window.SM_REFRESH = async function (force) {
    if (!window.SM_SEFARIA || (navigator.onLine === false)) return;
    const k = key(), c = cacheGet(), s = state(), today = localISO(now(), s.c.tz);
    const last = weeks().slice(-1)[0];
    const fresh = c && (now() - c.at) < 3 * 864e5;
    if (!force && fresh) return;
    if (!force && s.cur && last && last.shabbatISO >= addDays(today, 14)) return;
    if (window.__smRefreshing) return; window.__smRefreshing = true;
    try {
      const from = new Date(addDays(today, -7) + 'T00:00:00Z');
      const ws = await SM_SEFARIA.weeks(from, 5, k === 'diaspora');
      if (!ws.some(w => w.alyot)) return;
      const keep = (c ? c.weeks : []).filter(w => (progAll()[w.shabbatISO] || {}).n < 7 && !ws.some(x => x.shabbatISO === w.shabbatISO));
      const val = { at: now(), weeks: keep.concat(ws) };
      try { localStorage.setItem('sm.text.' + k, JSON.stringify(val)); } catch (e) { localStorage.setItem('sm.text.' + k, JSON.stringify({ at: now(), weeks: ws })); }
      memo = null; if (window.SM_RERENDER) SM_RERENDER(); if (window.SM_SYNC_REMINDERS) SM_SYNC_REMINDERS();
    } catch (e) { /* hors ligne ou Sefaria indisponible : on garde le texte embarqué */ }
    finally { window.__smRefreshing = false; }
  };
})();
