/* Shnayim Mikra — récupération des textes sur Sefaria (navigateur et Node).
   Une semaine = la paracha lue le Shabbat qui suit une date : 7 alyot, texte hébreu + Onkelos.
   Les versets sans vrai Targoum Onkelos (ex. Bamidbar 32:3, « Atarot ve-Divon ») sont marqués nt:1
   et reçoivent le Targoum Yerouchalmi quand Sefaria l'a. */
(function (root) {
  const API = 'https://www.sefaria.org/api';
  const EN = ["Bereshit","Noach","Lech-Lecha","Vayera","Chayei Sara","Toldot","Vayetzei","Vayishlach","Vayeshev","Miketz","Vayigash","Vayechi",
    "Shemot","Vaera","Bo","Beshalach","Yitro","Mishpatim","Terumah","Tetzaveh","Ki Tisa","Vayakhel","Pekudei",
    "Vayikra","Tzav","Shmini","Tazria","Metzora","Achrei Mot","Kedoshim","Emor","Behar","Bechukotai",
    "Bamidbar","Nasso","Beha'alotcha","Sh'lach","Korach","Chukat","Balak","Pinchas","Matot","Masei",
    "Devarim","Vaetchanan","Eikev","Re'eh","Shoftim","Ki Teitzei","Ki Tavo","Nitzavim","Vayeilech","Ha'Azinu","V'Zot HaBerachah"];
  const FR = ["Béréchit","Noa'h","Lekh Lekha","Vayéra","'Hayé Sarah","Toledot","Vayétsé","Vayichla'h","Vayéchev","Mikets","Vayigach","Vayé'hi",
    "Chemot","Vaéra","Bo","Bechala'h","Yitro","Michpatim","Terouma","Tetsavé","Ki Tissa","Vayakhel","Pekoudé",
    "Vayikra","Tsav","Chemini","Tazria","Metsora","A'harei Mot","Kedochim","Emor","Behar","Be'houkotaï",
    "Bamidbar","Nasso","Behaalotekha","Chela'h","Kora'h","'Houkat","Balak","Pin'has","Matot","Massé'i",
    "Devarim","Vaet'hanan","Ekev","Reé","Choftim","Ki Tetsé","Ki Tavo","Nitsavim","Vayélekh","Haazinou","Vezot Haberakha"];
  const BOOKS = { Genesis: 'Béréchit', Exodus: 'Chemot', Leviticus: 'Vayikra', Numbers: 'Bamidbar', Deuteronomy: 'Devarim' };
  const ALYA = [["Rishon","רִאשׁוֹן"],["Sheni","שֵׁנִי"],["Shlishi","שְׁלִישִׁי"],["Revi'i","רְבִיעִי"],["Hamishi","חֲמִישִׁי"],["Shishi","שִׁשִּׁי"],["Shvi'i","שְׁבִיעִי"]];
  const DAYS = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Shabbat'];
  const MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'];
  /* Versets connus sans Targoum Onkelos (Berakhot 8a : « même Atarot ve-Divon ») */
  const NO_TARGUM = { 'Numbers 32:3': 1 };
  const YER_TITLES = ['Targum Jerusalem, ', 'Targum Jonathan on '];
  /* Éditions demandées à Sefaria (voir docs/09-licences-textes.md). Si l'une disparaît, on prend l'édition par défaut ;
     dans tous les cas l'édition et la licence réellement reçues sont notées dans `src`, pour l'écran Sources. */
  const MIKRA_V = 'Miqra according to the Masorah';
  const ONKELOS_V = 'Sifsei Chachomim Chumash, Metsudah Publications, 2009';

  const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  let last = 0;
  /* Requêtes espacées (~0,4 s) et nouvelles tentatives si Sefaria répond 429 (trop de requêtes) */
  async function get(path, params) {
    const q = params ? '?' + Object.keys(params).map(k => k + '=' + encodeURIComponent(params[k])).join('&') : '';
    for (let k = 0; ; k++) {
      const wait = last + 400 - Date.now(); if (wait > 0) await sleep(wait); last = Date.now();
      const r = await fetch(API + path + q, { headers: { Accept: 'application/json' } });
      if (r.ok) return r.json();
      if ((r.status === 429 || r.status >= 500) && k < 6) { const ra = +(r.headers.get('retry-after') || 0); await sleep(Math.max(ra * 1000, 2000 * Math.pow(2, k))); continue; }
      throw new Error('HTTP ' + r.status + ' ' + path);
    }
  }
  function clean(s) {
    s = String(s || '').replace(/<[^>]+>/g, '');
    s = s.replace(/&nbsp;/g, ' ').replace(/&thinsp;/g, ' ').replace(/&amp;/g, '&').replace(/&#(\d+);/g, (_, n) => String.fromCharCode(+n));
    s = s.replace(/\s*\{[פס]\}\s*/g, ' ');
    return s.replace(/\s+/g, ' ').trim();
  }
  /* Fin de paragraphe après ce verset : 'p' (petou'ha) ou 's' (setouma), d'après la marque {פ} / {ס} du texte */
  function brk(s) { const m = String(s || '').match(/\{([פס])\}(?:\s|&nbsp;|<[^>]+>)*$/); return m ? (m[1] === 'פ' ? 'p' : 's') : ''; }
  function skel(s) { return clean(s).replace(/[֑-ׇ׳״]/g, '').replace(/[^א-ת ]/g, ' ').replace(/\s+/g, ' ').trim(); }
  /* Onkelos vide ou identique à l'hébreu (seulement des noms) → pas de vrai Targoum */
  function noTargum(fullRef, he, onk) {
    if (NO_TARGUM[fullRef]) return true;
    if (!onk) return true;
    return skel(he) === skel(onk);
  }
  async function verses(ref, vhe) {
    const path = '/texts/' + encodeURIComponent(ref.replace(/ /g, '_')), base = { context: 0, commentary: 0, pad: 0 };
    let d = await get(path, vhe ? Object.assign({ vhe }, base) : base);
    if (vhe && !(d.he && d.he.length)) d = await get(path, base);
    const he = d.he || []; const sec = d.sections || [1, 1];
    const ch = +sec[0], v0 = sec.length > 1 ? +sec[1] : 1; const out = [];
    if (he.length && Array.isArray(he[0])) he.forEach((chap, ci) => { const st = ci === 0 ? v0 : 1; chap.forEach((t, vi) => out.push([ch + ci, st + vi, clean(t), brk(t)])); });
    else he.forEach((t, vi) => out.push([ch, v0 + vi, clean(t), brk(t)]));
    out.meta = { title: String(d.heVersionTitle || '').trim(), license: d.heLicense || '' };
    return out;
  }
  async function yerushalmi(fullRef, log) {
    for (const t of YER_TITLES) {
      try { const d = await get('/texts/' + encodeURIComponent((t + fullRef).replace(/ /g, '_')), { context: 0, commentary: 0, pad: 0 });
        const he = Array.isArray(d.he) ? d.he.flat().join(' ') : d.he; const txt = clean(he);
        if (txt) { log && log('    Yerouchalmi ' + fullRef + ' ← ' + t.trim()); return { txt, meta: { title: String(d.heVersionTitle || '').trim(), license: d.heLicense || '' } }; } } catch (e) { log && log('    ' + t + fullRef + ' : ' + e.message); }
    }
    return null;
  }
  function span(ref) {
    const m = ref.match(/^[A-Za-z ]+?\s+(\d+):(\d+)-(?:(\d+):)?(\d+)$/); if (!m) return ref;
    const [, c1, v1, c2, v2] = m; return (!c2 || c2 === c1) ? c1 + ':' + v1 + ' – ' + v2 : c1 + ':' + v1 + ' – ' + c2 + ':' + v2;
  }
  function iso(d) { return d.getUTCFullYear() + '-' + String(d.getUTCMonth() + 1).padStart(2, '0') + '-' + String(d.getUTCDate()).padStart(2, '0'); }
  /* Les 7 alyot d'une suite de références : texte hébreu, Onkelos, versets sans Targoum ; et les éditions reçues */
  async function buildAlyot(arefs, log) {
    const alyot = [], src = {};
    for (let i = 0; i < 7; i++) {
      const aref = arefs[i]; const bk = aref.split(' ')[0];
      const mik = await verses(aref, MIKRA_V); const onk = {};
      const onkL = await verses('Onkelos ' + aref, ONKELOS_V); onkL.forEach(([c, v, t]) => { onk[c + ':' + v] = t; });
      if (!src.mikra && mik.meta.title) src.mikra = mik.meta; if (!src.onk && onkL.meta.title) src.onk = onkL.meta;
      const vs = [];
      for (const [c, v, t, pb] of mik) {
        const r = c + ':' + v; const o = onk[r] || ''; const x = { ref: r, he: t, onk: o }; if (pb) x.pb = pb;
        if (noTargum(bk + ' ' + r, t, o)) { x.nt = 1; const y = await yerushalmi(bk + ' ' + r, log); x.yer = y ? y.txt : ''; if (y && !src.yer) src.yer = y.meta; }
        vs.push(x);
      }
      alyot.push({ name: ALYA[i][0], heb: ALYA[i][1], day: DAYS[i], verses: span(aref), min: Math.max(3, Math.round(vs.length * 0.4)), ref: aref, v: vs });
      log && log('  ' + ALYA[i][0] + ': ' + aref + ' — ' + vs.length + ' versets, Onkelos ' + Object.keys(onk).length + ', sans Targoum ' + vs.filter(x => x.nt).length);
    }
    return { alyot, src };
  }
  /* ---------- Vezot Haberakha ----------
     La dernière paracha se lit à Sim'hat Torah (22 Tichri en Israël, 23 en diaspora) et non un Shabbat : le calendrier de
     Sefaria ne la donne donc jamais comme paracha de la semaine. On en fait une « semaine » à part (special: 'st'),
     dont l'échéance est le jour de Sim'hat Torah ; ses alyot viennent de l'index du livre. */
  let hebCal; try { hebCal = new Intl.DateTimeFormat('en-u-ca-hebrew', { day: 'numeric', month: 'long', timeZone: 'UTC' }); } catch (e) {}
  function simhatTorahIn(from, days, diaspora) {
    if (!hebCal) return ''; const want = diaspora ? 23 : 22;
    for (let k = 0; k < days; k++) { const d = new Date(from.getTime() + k * 864e5); const p = {}; hebCal.formatToParts(d).forEach(x => p[x.type] = x.value);
      if (p.month === 'Tishri' && +p.day === want) return iso(d); }
    return '';
  }
  async function vezot(stISO, log) {
    const idx = await get('/v2/raw/index/Deuteronomy');
    const node = ((((idx.alt_structs || {}).Parasha || {}).nodes) || []).find(n => n.sharedTitle === EN[53]);
    const arefs = ((node && node.refs) || []).map(r => r.replace(/\u2013/g, '-')).slice(0, 7);
    if (arefs.length < 7) throw new Error('alyot manquantes pour ' + EN[53]);
    const built = await buildAlyot(arefs, log), d = new Date(stISO + 'T00:00:00Z');
    return { shabbatISO: stISO, shabbat: d.getUTCDate() + ' ' + MOIS[d.getUTCMonth()], special: 'st', parasha: FR[53], parashaEn: EN[53], parashaHe: 'וזאת הברכה',
      parashaRef: BOOKS.Deuteronomy + ' 33:1 – 34:12', parashaIndex: 53, alyot: built.alyot, src: built.src };
  }

  /* day : Date (UTC, minuit). diaspora : true/false */
  async function week(day, diaspora, log) {
    const cal = await get('/calendars', { diaspora: diaspora ? 1 : 0, year: day.getUTCFullYear(), month: day.getUTCMonth() + 1, day: day.getUTCDate() });
    const item = cal.calendar_items.find(i => i.title.en === 'Parashat Hashavua');
    const sh = new Date(day.getTime() + ((6 - day.getUTCDay() + 7) % 7) * 864e5);
    const base = { shabbatISO: iso(sh), shabbat: sh.getUTCDate() + ' ' + MOIS[sh.getUTCMonth()] };
    const en = item.displayValue.en, he = item.displayValue.he, ref = item.ref;
    const parts = EN.indexOf(en) >= 0 ? [en] : en.split('-').map(p => p.trim());
    if (EN.indexOf(parts[0]) < 0) return Object.assign(base, { holiday: true, parasha: en, parashaEn: en, parashaHe: he });
    const fr = parts.map(p => EN.indexOf(p) >= 0 ? FR[EN.indexOf(p)] : p).join(' – ');
    const book = ref.split(' ')[0];
    const arefs = ((item.extraDetails || {}).aliyot || []).slice(0, 7);
    if (arefs.length < 7) throw new Error('alyot manquantes pour ' + en);
    const built = await buildAlyot(arefs, log), alyot = built.alyot, src = built.src;
    return Object.assign(base, { parasha: fr, parashaEn: en, parashaHe: he, parashaRef: (BOOKS[book] || book) + ' ' + span(ref), parashaIndex: EN.indexOf(parts[0]), alyot, src });
  }
  /* Semaines à partir de `from` (Date), `count` semaines, dédoublonnées par Shabbat */
  async function weeks(from, count, diaspora, log) {
    const out = []; const seen = {};
    for (let k = 0; k < count; k++) {
      const d = new Date(Date.UTC(from.getUTCFullYear(), from.getUTCMonth(), from.getUTCDate() + 7 * k));
      try { const w = await week(d, diaspora, log); if (seen[w.shabbatISO]) continue; seen[w.shabbatISO] = 1; out.push(w);
        log && log('Semaine ' + w.shabbatISO + ' : ' + w.parasha + (w.holiday ? ' (fête)' : ''));
      } catch (e) { log && log('Semaine ' + k + ' ignorée : ' + e.message); }
    }
    /* Vezot Haberakha, si Sim'hat Torah tombe dans la période demandée (elle remplace alors le Shabbat de fête du même jour) */
    try {
      const st = simhatTorahIn(from, 7 * count + 7, diaspora);
      if (st) { const w = await vezot(st, log); const i = out.findIndex(x => x.shabbatISO === st); if (i >= 0) out.splice(i, 1);
        out.push(w); out.sort((a, b) => a.shabbatISO < b.shabbatISO ? -1 : 1); log && log('Sim\'hat Torah ' + st + ' : ' + w.parasha); }
    } catch (e) { log && log('Vezot Haberakha ignorée : ' + e.message); }
    return out;
  }
  const API_OBJ = { weeks, week, noTargum, skel, EN, FR };
  if (typeof module !== 'undefined' && module.exports) module.exports = API_OBJ; else root.SM_SEFARIA = API_OBJ;
})(typeof window !== 'undefined' ? window : globalThis);
