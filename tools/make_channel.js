#!/usr/bin/env node
/* Prépare les messages de la chaîne WhatsApp, jour par jour, dans les cinq langues.
   Usage : node tools/make_channel.js <dossier de sortie> [fichier text.js]
   (lancer d'abord `node tools/fetch_sefaria.js`, qui écrit web/data/text.js).
   Écrit <sortie>/messages.js et y copie la page chaine/index.html, où l'on copie le message du jour.

   Les calculs sont ceux de l'app, chargée telle quelle : paracha de la semaine (Israël ou diaspora), durée des alyot,
   heure d'allumage, jours de Chabbat et de fête. La chaîne et l'app disent donc la même chose.

   Règles :
   - une alya par jour du dimanche au vendredi ; les sept alyot sont réparties sur les jours sans Chabbat ni fête,
     les derniers jours recevant une alya de plus (le vendredi : Shishi et Shvi'i) ;
   - le premier jour annonce la paracha ; le jeudi soir, un second message rappelle ce qu'il reste ;
   - la veille de Chabbat ou d'une fête : heure d'allumage des bougies, dvar Torah de la semaine s'il a été fourni, salutation ;
   - aucun message pendant Chabbat et les fêtes ;
   - Vezot Haberakha : les sept derniers jours avant Sim'hat Torah, précédés d'un message de rattrapage. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const root = path.join(__dirname, '..'), web = path.join(root, 'web'), src = path.join(root, 'chaine');
const out = path.resolve(process.argv[2] || path.join(root, '_site', 'chaine'));
const data = path.resolve(process.argv[3] || path.join(web, 'data', 'text.js'));
const TX = require(path.join(src, 'textes.js')), CFG = JSON.parse(fs.readFileSync(path.join(src, 'config.json'), 'utf8'));
const LANGS = ['fr', 'he', 'en', 'es', 'tn'], CALS = ['diaspora', 'israel'];

/* ---------- L'app, chargée dans un bac à part ; S = ses réglages (langue, lieu) ---------- */
const w = { console, setTimeout: () => 0, clearTimeout: () => {} }; w.window = w; const ctx = vm.createContext(w);
const S = { lang: 'fr', place: 1 }; w.APP = { get: (k) => S[k] };
for (const f of [data, 'config.js', 'i18n.js', 'i18n/en.js', 'i18n/es.js', 'i18n/he.js', 'i18n/tn.js', 'sefaria.js', 'globals.js'])
  vm.runInContext(fs.readFileSync(path.isAbsolute(f) ? f : path.join(web, f), 'utf8'), ctx, { filename: f });
if (!w.SM_TEXT || !w.SM_TEXT.diaspora) { console.error('Pas de textes dans ' + data + ' : lancer d\'abord node tools/fetch_sefaria.js'); process.exit(1); }

const Z = w.SM_ZMAN, addDays = Z.addDays, F = w.SM_FMT;
const at = (iso) => Date.parse(iso + 'T10:00:00Z');            /* milieu de journée, en France comme en Israël */
const dow = (iso) => new Date(iso + 'T12:00:00Z').getUTCDay();
const heb = new Intl.DateTimeFormat('en-u-ca-hebrew', { day: 'numeric', month: 'long', timeZone: 'UTC' });
function hebDate(iso) { const p = {}; heb.formatToParts(new Date(iso + 'T12:00:00Z')).forEach(x => p[x.type] = x.value); return { month: p.month, day: +p.day }; }

/* ---------- Dvar Torah fournis par l'association : chaine/dvar-torah/<langue>.md, un titre « ## numéro — nom » par paracha ---------- */
function dvarFile(lang) {
  const f = path.join(src, 'dvar-torah', lang + '.md'), by = {}; if (!fs.existsSync(f)) return by;
  const parts = fs.readFileSync(f, 'utf8').replace(/<!--[\s\S]*?-->/g, '').split(/^## +(\d+)[^\n]*$/m);
  for (let i = 1; i < parts.length; i += 2) { const txt = parts[i + 1].trim(); if (txt) by[+parts[i]] = txt; }
  return by;
}

/* ---------- Jours et répartition des alyot, pour un calendrier ---------- */
function plan(cal) {
  S.place = cal === 'israel' ? 0 : 1;
  const weeks = ((w.SM_TEXT[cal] || {}).weeks || []).slice().sort((a, b) => a.shabbatISO < b.shabbatISO ? -1 : 1);
  if (!weeks.length) return null;
  const days = [], byIso = {}, P = {};
  for (let d = addDays(weeks[0].shabbatISO, -6); d <= weeks[weeks.length - 1].shabbatISO; d = addDays(d, 1)) {
    w.SM_NOW = at(d); const wk = w.SM_WEEK(0);
    const x = { iso: d, rest: w.SM_IS_REST(w.SM_NOW), yt: w.SM_IS_YOMTOV(d), sat: dow(d) === 6, wk: wk ? wk.shabbatISO : '' };
    days.push(x); byIso[d] = x;
  }
  for (const wk of weeks) {
    if (wk.holiday || !wk.alyot) continue;
    /* jours où l'on peut publier : ceux de la semaine de lecture, hors Chabbat et fêtes */
    let av = days.filter(d => d.wk === wk.shabbatISO && !d.rest && d.iso < wk.shabbatISO);
    if (!wk.special) av = av.filter(d => d.iso >= addDays(wk.shabbatISO, -6));
    let intro = null; if (wk.special && av.length > 7) { intro = av[0]; av = av.slice(-7); }
    const n = av.length; if (!n) continue;
    const base = Math.floor(7 / n), extra = 7 % n; let from = 0;
    av.forEach((d, j) => { const size = base + (j >= n - extra ? 1 : 0); P[d.iso] = { wk, from, to: from + size - 1, first: j === 0, last: j === n - 1 }; from += size; });
    if (intro) P[intro.iso] = { wk, intro: true, start: av[0].iso };
    /* jeudi soir : rappel de ce qui reste pour le vendredi */
    if (!wk.special && n >= 2) { const thu = av[n - 2], fri = av[n - 1]; if (dow(thu.iso) === 4 && fri.iso === addDays(thu.iso, 1)) P[thu.iso].eve = { from: P[fri.iso].from, to: P[fri.iso].to }; }
  }
  return { days, byIso, P };
}

/* ---------- Messages d'un calendrier dans une langue ---------- */
function render(cal, lang, pl) {
  S.place = cal === 'israel' ? 0 : 1; S.lang = lang;
  const T = TX[lang], dvars = dvarFile(lang), cities = (CFG.villes[lang] || []).map(id => w.SM_CITIES.find(c => c.id === id)).filter(Boolean), res = {};
  const dateLabel = (iso) => w.SM_DATE(Date.parse(iso + 'T12:00:00Z'), { weekday: 'long', day: 'numeric', month: 'long' });
  const list = (a) => a.length < 2 ? a.join('') : a.slice(0, -1).join(', ') + T.and + a[a.length - 1];
  for (const d of pl.days) {
    if (d.rest) { res[d.iso] = { note: d.sat ? 'chabbat' : 'fete' }; continue; }
    const p = pl.P[d.iso], msgs = []; let body = '', dvar = '';
    if (p) {
      w.SM_NOW = at(d.iso);                                     /* l'app se place ce jour-là : c'est la semaine de lecture en cours */
      const info = w.SM_WEEK_INFO(p.wk), A = w.SM_ALYOT() || [];
      const mins = (a, b) => Math.max(1, Math.round(A.slice(a, b + 1).reduce((s, x) => s + x.sec, 0) / 60));
      const label = (a, b) => list(A.slice(a, b + 1).map((x, i) => w.SM_ALYA(a + i) + ' (' + x.verses + ')'));
      const total = mins(0, 6);
      if (p.intro) body = F(T.stIntro, { parasha: info.name, date: dateLabel(p.start) });
      else {
        const v = { parasha: info.name, ref: info.ref, total, alyot: label(p.from, p.to), min: mins(p.from, p.to), date: dateLabel(p.wk.shabbatISO) };
        body = p.first ? F(p.wk.special ? T.stWeek : T.newWeek, v) + '\n\n' + F(T.today, v) : F(T.day, v);
        if (CFG.appUrl) body += '\n' + F(T.link, { url: CFG.appUrl });
        body += '\n' + T.react;
        if (p.eve) msgs.push({ k: 'soir', text: T.eveTitle + '\n' + F(T.eveBody, { parasha: info.name, alyot: label(p.eve.from, p.eve.to), min: mins(p.eve.from, p.eve.to), total }) });
        if (p.last) { const dv = (info.idx || []).map(i => dvars[i + 1]).filter(Boolean).join('\n\n'); if (dv) dvar = T.dvar + '\n' + dv; }
      }
    }
    /* veille de Chabbat ou de fête : bougies, dvar Torah, salutation */
    const next = pl.byIso[addDays(d.iso, 1)];
    if (next && next.rest) {
      const blocks = body ? [body] : [];
      if (cities.length) blocks.push(F(T.candles, { list: cities.map(c => w.SM_CITY_NAME(c) + ' ' + Z.hhmm(Z.sunset(d.iso, c) - c.off * 60e3, c.tz)).join(' · ') }));
      if (dvar) blocks.push(dvar);
      const h = hebDate(next.iso), fest = !next.yt ? '' : (h.month === 'Tishri' && h.day <= 2) ? T.rh : (h.month === 'Tishri' && h.day === 10) ? T.yk : T.hag;
      blocks.push(fest === T.yk ? F(T.greet, { a: fest }) : next.sat && fest ? F(T.greet2, { a: T.shabbat, b: fest }) : F(T.greet, { a: next.sat ? T.shabbat : fest }));
      body = blocks.join('\n\n');
    }
    if (body) msgs.unshift({ k: 'matin', text: body });
    res[d.iso] = msgs.length ? { msgs } : { note: 'rien' };
  }
  return res;
}

const result = { builtAt: new Date().toISOString(), textAt: w.SM_TEXT.builtAt || '', appUrl: CFG.appUrl || '', calendrier: CFG.calendrier, days: {} };
for (const cal of CALS) {
  const pl = plan(cal); if (!pl) continue; result.days[cal] = {};
  for (const lang of LANGS) result.days[cal][lang] = render(cal, lang, pl);
  const isos = pl.days.map(d => d.iso); result.from = result.from && result.from < isos[0] ? result.from : isos[0];
  const last = isos[isos.length - 1]; result.to = result.to && result.to > last ? result.to : last;
}
if (!Object.keys(result.days).length) { console.error('Aucune semaine dans les textes.'); process.exit(1); }
fs.mkdirSync(out, { recursive: true });
fs.writeFileSync(path.join(out, 'messages.js'), 'window.SM_CHAINE = ' + JSON.stringify(result) + ';\n');
fs.copyFileSync(path.join(src, 'index.html'), path.join(out, 'index.html'));
const n = Object.values(result.days.diaspora.fr).filter(x => x.msgs).length;
console.error('Chaîne : ' + n + ' jours avec message, du ' + result.from + ' au ' + result.to + ' → ' + out);
