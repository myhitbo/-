/* Données partagées : paracha de la semaine (Sefaria si disponible), alya choisie, textes du lecteur */
(function () {
  const FALLBACK = { parasha: 'Vayétsé', parashaHe: 'וַיֵּצֵא', parashaRef: 'Béréchit 28:10 – 32:3' };
  const NAMES = ['Rishon', 'Sheni', 'Shlishi', "Revi'i", 'Hamishi', 'Shishi', "Shvi'i"];
  const MONTHS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'];
  const DAYS = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi'];
  const NEXT_FALLBACK = [
    { parasha: "Vayichla'h", parashaHe: 'וַיִּשְׁלַח', parashaRef: 'Béréchit 32:4 – 36:43' },
    { parasha: 'Vayéchev', parashaHe: 'וַיֵּשֶׁב', parashaRef: 'Béréchit 37:1 – 40:23' },
    { parasha: 'Mikets', parashaHe: 'מִקֵּץ', parashaRef: 'Béréchit 41:1 – 44:17' }];
  function parIndex() { const p = window.APP && APP.get('par'); return p ? p : 0; }
  function week(k) { const W = window.SM_TEXT && SM_TEXT.weeks; return W && W[k] ? W[k] : (k === 0 ? (window.SM_TEXT || FALLBACK) : null); }
  function alyaIndex() { const a = window.APP && APP.get('alya'); return (a === undefined || a === null) ? new Date().getDay() : a; }
  window.SM_G = function () {
    const T = window.SM_TEXT || FALLBACK; const d = new Date(); const i = alyaIndex();
    const R = week(parIndex()) || T; const al = R.alyot || null;
    const next = i < 6 ? NAMES[i + 1] + (al ? ', ' + al[i + 1].min + ' min' : '') : null;
    return { parasha: T.parasha, parashaHe: T.parashaHe, parashaRef: T.parashaRef, readParasha: R.parasha, date: DAYS[d.getDay()] + ' ' + d.getDate() + ' ' + MONTHS[d.getMonth()],
      alyaName: NAMES[i], afterText: next ? 'Prochaine alya : ' + next + '.' : 'La paracha est terminée. Shabbat Shalom !' };
  };
  window.SM_BLOCKS = function () {
    const W = week(parIndex()); if (!W || !W.alyot) return null; const a = W.alyot[alyaIndex()]; if (!a) return null; const out = [];
    a.v.forEach(v => { out.push({ kind: 'mikra', n: 1, ref: v.ref, text: v.he }); out.push({ kind: 'mikra', n: 2, ref: v.ref, text: v.he }); if (v.onk) out.push({ kind: 'targum', n: 3, ref: v.ref, text: v.onk }); });
    return out;
  };
  /* Les 3 prochaines parachiyot (Sefaria si disponible) */
  window.SM_NEXT = function () {
    const W = window.SM_TEXT && SM_TEXT.weeks;
    const list = W ? W.slice(1, 4) : NEXT_FALLBACK;
    return list.map((w, k) => ({ name: w.parasha, heb: w.parashaHe, ref: w.parashaRef, when: w.shabbat ? 'Shabbat ' + w.shabbat : 'Dans ' + (k + 1) + ' semaine' + (k ? 's' : ''),
      href: w.alyot ? 'V2-Lecteur.dc.html?par=' + (k + 1) + '&alya=0' : '#', canRead: !!w.alyot }));
  };
})();
