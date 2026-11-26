// Les vecteurs de parité du moteur des lectures (test/vecteurs_lecture_torah.json) : la réponse de
// web/lecture.js, jour par jour, sous la forme que LectureTorahTest.kt relit dans le projet d'origine
// (même calcul côté Kotlin, docs/09-cahier-de-reprise.md § 7).
// Régénérer, seulement après un changement voulu du calcul : node tools/vecteurs_lecture.mjs

import { readFileSync, writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { ajouteJours, lectures, NUSAH, OFFICES } = require('../web/lecture.js');

const ICI = dirname(fileURLToPath(import.meta.url));
export const DATA = join(ICI, '..', 'data');
export const VECTEURS = join(ICI, '..', 'test', 'vecteurs_lecture_torah.json');
/** Six années hébraïques entières (5786 à 5791) et leurs bords. */
export const DEBUT = '2025-09-01';
export const FIN = '2031-12-31';
/** Diaspora, Israël, Jérusalem (Pourim le 15). */
export const LIEUX = { dia: { enIsrael: false, mukafChoma: false }, il: { enIsrael: true, mukafChoma: false }, jer: { enIsrael: true, mukafChoma: true } };

/** Une lecture en une ligne : clé | montées | haftara. */
export function resume(l) {
  const m = l.montees.map((x) => `${x.cle}:${x.livre} ${x.debut}-${x.fin}`).join(',');
  const h = l.haftara.map((x) => `${x.livre} ${x.debut}-${x.fin}`).join(',');
  return `${l.cle}|${m}|${h}`;
}

/**
 * { "AAAA-MM-JJ/lieu": { office: { nusah | "*": [résumé…] } } } pour les jours où l'on lit ; Jérusalem
 * seulement quand elle diffère d'Israël (vide si elle ne lit pas), le noussa'h « * » quand les trois s'accordent.
 */
export function vecteurs(donnees, debut = DEBUT, fin = FIN) {
  const jours = {};
  for (let iso = debut; iso <= fin; iso = ajouteJours(iso, 1)) {
    let israel = null;
    for (const [lieu, opts] of Object.entries(LIEUX)) {
      const parOffice = {};
      for (const office of OFFICES) {
        const parNusah = Object.fromEntries(NUSAH.map((n) => [n, lectures(donnees, iso, office, { ...opts, nusah: n }).map(resume)]));
        if (parNusah.edot.length === 0 && parNusah.sefard.length === 0 && parNusah.ashkenaz.length === 0) continue;
        const memes = NUSAH.every((n) => JSON.stringify(parNusah[n]) === JSON.stringify(parNusah.edot));
        parOffice[office] = memes ? { '*': parNusah.edot } : parNusah;
      }
      const cle = JSON.stringify(parOffice);
      if (lieu === 'il') israel = cle;
      if (lieu === 'jer' && cle === israel) continue;
      // Jérusalem sans lecture quand Israël en a une (le 14 Adar) : écrite vide.
      if (Object.keys(parOffice).length || lieu === 'jer') jours[`${iso}/${lieu}`] = parOffice;
    }
  }
  return { debut, fin, jours };
}

/** Le fichier des vecteurs, une entrée par ligne. */
export function ecritVecteurs(v, chemin = VECTEURS) {
  const lignes = Object.entries(v.jours).map(([k, x]) => `${JSON.stringify(k)}: ${JSON.stringify(x)}`);
  writeFileSync(chemin, `{\n"debut": ${JSON.stringify(v.debut)},\n"fin": ${JSON.stringify(v.fin)},\n"jours": {\n${lignes.join(',\n')}\n}\n}\n`);
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  const donnees = JSON.parse(readFileSync(join(DATA, 'lecture_torah.json'), 'utf8'));
  const v = vecteurs(donnees);
  ecritVecteurs(v);
  console.log(`${Object.keys(v.jours).length} entrées écrites dans ${VECTEURS}`);
}
