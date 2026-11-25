/* Shnayim Mikra — données partagées : semaines (Sefaria), Israël/diaspora, heure d'allumage,
   échéances, progression par semaine, textes du lecteur, impression. */
(function () {
  const NAMES = ['Rishon', 'Sheni', 'Shlishi', "Revi'i", 'Hamishi', 'Shishi', "Shvi'i"];
  const MONTHS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'];
  const DAYS = ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi'];
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
    if (old.n === p[w.shabbatISO].n && old.name) return; try { localStorage.setItem('sm.prog', JSON.stringify(p)); } catch (e) {} }
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
  window.SM_ALYOT = () => { const w = state().cur; return w && w.alyot ? w.alyot : null; };
  /* Fin d'une alya dans le lecteur */
  /* Séance ouverte dans le lecteur : alyot from..to de la semaine choisie (une seule alya si `alyaTo` est absent) */
  function portion() {
    const W = weekFor(get('par')); if (!W || !W.alyot) return null;
    const from = alyaIndex(); let to = get('alyaTo'); to = (to === undefined || to === null || to < from) ? from : Math.min(6, to);
    return { W, from, to };
  }
  window.SM_PORTION = function () { const P = portion(); return P ? { from: P.from, to: P.to, order: get('order') || 0, names: NAMES } : null; };
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
  const sessionAt = (n) => { const from = Math.min(6, n); return sessions().find(x => from >= x.from && from <= x.to) || { from, to: 6, day: 6 }; };
  const rangeMin = (w, from, to) => w && w.alyot ? w.alyot.slice(from, to + 1).reduce((a, x) => a + x.min, 0) : 0;
  /* Jour dans la semaine de lecture : 0 = dimanche … 6 = Shabbat ; −1 le samedi soir, une fois le Shabbat précédent sorti */
  function dayInWeek(s) {
    const today = localISO(s.t, s.c.tz); if (!s.cur) return dow(today);
    return Math.round((Date.parse(today + 'T12:00:00Z') - Date.parse(addDays(s.cur.shabbatISO, -6) + 'T12:00:00Z')) / 864e5);
  }
  /* Prochaine séance de la semaine en cours, et nombre d'alyot en retard sur le rythme choisi */
  window.SM_PLAN = function () {
    const s = state(), n = progN(s.cur), rh = get('rh') || 0, d = dayInWeek(s), cur = sessionAt(n);
    const due = rh === 3 ? 0 : sessions().filter(x => x.day < d).reduce((a, x) => Math.max(a, x.to + 1), 0);
    return { rh, from: Math.min(6, n), to: cur.to, day: cur.day, today: d, late: n >= 7 ? 0 : Math.max(0, due - n), done: n >= 7, min: rangeMin(s.cur, Math.min(6, n), cur.to), names: NAMES };
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
    const out = { parasha: w.parasha, parashaHe: w.parashaHe, parashaRef: w.parashaRef, readParasha: R.parasha, readIso: R.shabbatISO || '',
      date: cap(DAYS[dow(todayIso)]) + ' ' + d.getDate() + ' ' + MONTHS[d.getMonth()], alyaName: NAMES[i] || NAMES[0],
      afterText: !nx ? T.nextNone : nx.to > nf ? F(T.nextRange, { a: NAMES[nf], b: NAMES[nx.to], min: rangeMin(R, nf, nx.to) }) : F(T.nextOne, { name: NAMES[nf], min: rangeMin(R, nf, nf) }), cityName: c.name, place: isIL() ? 'Israël' : 'Diaspora' };
    /* Allumage et compte à rebours */
    if (s.cur) {
      const cl = candle(s.cur.shabbatISO, c), left = cl - s.t, n = progN(s.cur);
      out.candle = hhmm(cl, c.tz);
      out.candleLine = 'Allumage ' + (left > 0 ? 'vendredi' : '') + ' à ' + out.candle + ' · ' + c.name + ' (coucher du soleil − ' + c.off + ' min)';
      out.countdown = left > 0 ? 'Chabbat dans ' + inDur(left) : 'Chabbat Chalom';
      out.goal = n >= 7 ? 'Paracha terminée' : left > 0 ? 'Objectif : finir avant Chabbat' : 'Encore possible ce Chabbat, avant le repas de midi';
      out.friday = left > 0 && left < 30 * 3600e3 && dow(todayIso) === 5 && n < 7;
    } else { out.candleLine = 'Allumage selon ta ville (textes en cours de téléchargement)'; out.countdown = ''; out.goal = ''; out.friday = false; }
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
    const add = (x, kind, n, text, label) => out.push({ kind, n, ref: x.v.ref, text, al: x.al, aln: NAMES[x.al], vi: x.vi, label: label || '' });
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
      const name = order === 1 ? (a.v.ref === b.v.ref ? a.v.ref : a.v.ref + ' – ' + b.v.ref) : a.al === b.al ? NAMES[a.al] : (a.al === 0 && b.al === 6) ? P.W.parasha : NAMES[a.al] + ' – ' + NAMES[b.al];
      [[1, t.read1], [2, t.read2]].forEach(pass => { const i = out.length; grp.forEach(x => mik(x, pass[0])); out[i].head = name + ' · ' + pass[1]; });
      const i = out.length; grp.forEach(tg); out[i].head = name + ' · ' + t.targum;
    });
    return out;
  };
  /* Les 3 prochaines parachiyot */
  window.SM_NEXT = function () {
    const s = state(); const list = s.W.slice(s.ci + 1, s.ci + 4);
    return list.map((w, k) => ({ name: w.parasha, heb: w.parashaHe, ref: w.parashaRef, when: 'Shabbat ' + w.shabbat,
      href: w.alyot ? 'V2-Lecteur.dc.html?par=' + (k + 1) + '&alya=0' : '#', canRead: !!w.alyot }));
  };

  /* ---------- Impression : ce qu'il reste (ou toute la paracha) ---------- */
  window.SM_PRINT_INFO = function (all) {
    const w = state().cur; if (!w || !w.alyot) return null; const from = all ? 0 : Math.min(6, progN(w));
    const al = w.alyot.slice(from); const chars = al.reduce((a, x) => a + x.v.reduce((b, v) => b + v.he.length + (v.onk || '').length, 0), 0);
    return { from, names: al.map(a => a.name), range: al.length > 1 ? al[0].name + ' – ' + al[al.length - 1].name : al[0].name, first: al[0].name + ' · ' + al[0].v[0].ref,
      min: al.reduce((a, x) => a + x.min, 0), pages: Math.max(1, Math.ceil(chars / 3400)), count: al.length };
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
    let el = document.getElementById('print'); if (!el) { el = document.createElement('div'); el.id = 'print'; document.body.appendChild(el); }
    el.innerHTML = h; document.title = 'Shnayim Mikra — ' + w.parasha;
    if (window.SMAndroid && SMAndroid.print) SMAndroid.print('Shnayim Mikra — ' + w.parasha); else window.print();
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
      memo = null; if (window.SM_RERENDER) SM_RERENDER();
    } catch (e) { /* hors ligne ou Sefaria indisponible : on garde le texte embarqué */ }
    finally { window.__smRefreshing = false; }
  };
})();
