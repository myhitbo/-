/* Shnayim Mikra — le Targoum Yerouchalmi des versets sans Targoum Onkelos (« Réouven, Chimon… »), pris sur
   Sefaria quand le téléphone est en ligne. Tout le reste du texte est embarqué (web/data/) : sans réseau,
   ces versets se lisent simplement trois fois. Appelé par SM_REFRESH (web/globals.js), puis gardé (sm.yer). */
(function (root) {
  const API = 'https://www.sefaria.org/api';
  /* « Targum Jerusalem » (fragments) d'abord, sinon « Targum Jonathan » */
  const TITRES = ['Targum Jerusalem, ', 'Targum Jonathan on '];
  const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  let last = 0;
  /* Requêtes espacées (~0,4 s) et nouvelles tentatives si Sefaria répond 429 ou 5xx ; null si le texte n'existe pas */
  async function get(path, params) {
    const q = '?' + Object.keys(params).map(k => k + '=' + encodeURIComponent(params[k])).join('&');
    for (let k = 0; ; k++) {
      const wait = last + 400 - Date.now(); if (wait > 0) await sleep(wait); last = Date.now();
      const r = await fetch(API + path + q, { headers: { Accept: 'application/json' } });
      if (r.ok) return r.json();
      if ((r.status === 429 || r.status >= 500) && k < 4) { const ra = +(r.headers.get('retry-after') || 0); await sleep(Math.max(ra * 1000, 2000 * Math.pow(2, k))); continue; }
      if (r.status >= 400 && r.status < 500 && r.status !== 429) return null;
      throw new Error('HTTP ' + r.status + ' ' + path);
    }
  }
  function clean(s) {
    s = String(s || '').replace(/<[^>]+>/g, '');
    s = s.replace(/&nbsp;/g, ' ').replace(/&thinsp;/g, ' ').replace(/&amp;/g, '&').replace(/&#(\d+);/g, (_, n) => String.fromCharCode(+n));
    return s.replace(/\s*\{[פס]\}\s*/g, ' ').replace(/\s+/g, ' ').trim();
  }
  /* « Genesis 46:23 » → le Targoum Yerouchalmi du verset, ou '' si Sefaria ne l'a pas. Lève une erreur hors ligne. */
  async function yerushalmi(fullRef) {
    for (const t of TITRES) {
      const d = await get('/texts/' + encodeURIComponent((t + fullRef).replace(/ /g, '_')), { context: 0, commentary: 0, pad: 0 });
      const he = d && (Array.isArray(d.he) ? d.he.flat().join(' ') : d.he); const txt = clean(he);
      if (txt) return txt;
    }
    return '';
  }
  const API_OBJ = { yerushalmi };
  if (typeof module !== 'undefined' && module.exports) module.exports = API_OBJ; else root.SM_SEFARIA = API_OBJ;
})(typeof window !== 'undefined' ? window : globalThis);
