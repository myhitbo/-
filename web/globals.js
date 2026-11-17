/* Données partagées : paracha de la semaine (Sefaria si disponible), alya choisie, textes du lecteur */
(function () {
  const FALLBACK = { parasha: 'Vayétsé', parashaHe: 'וַיֵּצֵא', parashaRef: 'Béréchit 28:10 – 32:3' };
  const NAMES = ['Rishon', 'Sheni', 'Shlishi', "Revi'i", 'Hamishi', 'Shishi', "Shvi'i"];
  const MONTHS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'];
  const DAYS = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi'];
  function alyaIndex() { const a = window.APP && APP.get('alya'); return (a === undefined || a === null) ? new Date().getDay() : a; }
  window.SM_G = function () {
    const T = window.SM_TEXT || FALLBACK; const d = new Date(); const i = alyaIndex();
    const al = window.SM_TEXT ? SM_TEXT.alyot : null;
    const next = i < 6 ? NAMES[i + 1] + (al ? ', ' + al[i + 1].min + ' min' : '') : null;
    return { parasha: T.parasha, parashaHe: T.parashaHe, parashaRef: T.parashaRef, date: DAYS[d.getDay()] + ' ' + d.getDate() + ' ' + MONTHS[d.getMonth()],
      alyaName: NAMES[i], afterText: next ? 'Prochaine alya : ' + next + '.' : 'La paracha est terminée. Shabbat Shalom !' };
  };
  window.SM_BLOCKS = function () {
    if (!window.SM_TEXT) return null; const a = SM_TEXT.alyot[alyaIndex()]; if (!a) return null; const out = [];
    a.v.forEach(v => { out.push({ kind: 'mikra', n: 1, ref: v.ref, text: v.he }); out.push({ kind: 'mikra', n: 2, ref: v.ref, text: v.he }); if (v.onk) out.push({ kind: 'targum', n: 3, ref: v.ref, text: v.onk }); });
    return out;
  };
})();
