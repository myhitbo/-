// Le contexte des haftarot (docs/09-cahier-de-reprise.md § 6) : data/contexte_haftarot.json respecte les règles
// du propriétaire — 4 à 6 phrases en français et en anglais, chacune avec sa source, sources 'harédi uniquement,
// noms hébreux — et l'application trouve le contexte de la haftara qu'elle affiche. La relecture des citations
// à leur source se fait à part, avec le réseau : node tools/contexte_haftarot.mjs --sources

import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import test from 'node:test';
import { affichees, classiqueAcceptee, controle, lien, nomsInterdits, trouve } from '../tools/contexte_haftarot.mjs';

const require = createRequire(import.meta.url);
const L = require('../web/lecture.js');
const lis = (nom) => JSON.parse(readFileSync(new URL(`../data/${nom}`, import.meta.url), 'utf8'));
const donnees = lis('lecture_torah.json');
const fichier = lis('contexte_haftarot.json');

test('chaque contexte écrit respecte la forme, les sources acceptées et les noms hébreux', () => {
  const { erreurs, manquantes, couvertes, total } = controle(fichier, donnees);
  assert.deepEqual(erreurs, []);
  assert.equal(total, 105); // les haftarot que l'application peut afficher : origine et premier passage, tous rites
  assert.equal(couvertes + manquantes.length, total);
  // Tant que la rédaction est en cours, des haftarot restent sans contexte : l'encadré ne s'affiche pas pour elles.
  if (fichier._meta.etat === 'complet') assert.deepEqual(manquantes, []);
});

test('les règles du contrôle : sources, noms, liens', () => {
  for (const ref of ['Rashi on Obadiah 1:1', 'Radak on Ezekiel 37:16', 'Megillah 31a', 'Seder Olam Rabbah 20', 'Obadiah 1:1', 'Malbim on I Kings 2:1',
    'Mishnah Berurah 428:8', 'Shulchan Arukh, Orach Chayim 428:8', 'Bereishit Rabbah 84:3', 'Targum Jonathan on Zechariah 3:1']) assert.ok(classiqueAcceptee(ref), ref);
  for (const ref of ['Wikipedia', 'JPS 1985 Footnotes, Obadiah 1', 'The Koren Jerusalem Bible', 'Steinsaltz on Obadiah 1:1', 'Daat Mikra on Obadiah']) assert.ok(!classiqueAcceptee(ref), ref);
  assert.deepEqual(nomsInterdits('Le prophète Abdias vivait au temps d’Achab et de Jézabel.', 'fr'), ['Abdias', 'Achab', 'Jézabel']);
  assert.deepEqual(nomsInterdits("Ovadia vivait au temps d'A'hav et d'Izével ; Eliyahou, Elicha, Éliézer, les rois de Yehouda.", 'fr'), []);
  assert.deepEqual(nomsInterdits('Obadiah lived in the days of Ahab.', 'en'), ['Obadiah', 'Ahab']);
  assert.deepEqual(nomsInterdits('Ovadia lived in the days of Achav; Eliyahu, the kings of Yehuda.', 'en'), []);
  assert.equal(lien({ genre: 'classique', sefaria: 'Rashi on Obadiah 1:1' }), 'https://www.sefaria.org/Rashi_on_Obadiah_1:1?lang=he');
  // Un contexte fautif est refusé : trop court, sans source, nom interdit, source exclue.
  const fautif = { contextes: [{ id: 'x', occasions: ['VAYISHLACH'], passages: ['Obadiah 1:1-1:21'], phrases: [
    { fr: 'Abdias parle à Edom.', en: 'Ovadia speaks to Edom.', sources: [] },
    { fr: 'Ovadia parle à Edom.', en: 'Ovadia speaks to Edom.', sources: [{ genre: 'classique', ref: { fr: 'Encyclopédie', en: 'Encyclopedia' }, sefaria: 'Jewish Encyclopedia', citation: 'עובדיה' }] },
  ] }] };
  const { erreurs } = controle(fautif, donnees);
  for (const attendu of [/2 phrases/, /sans source/, /nom interdit « Abdias »/, /source classique non acceptée/]) assert.ok(erreurs.some((e) => attendu.test(e)), String(attendu));
});

test('une haftara affichée retrouve son contexte par son origine et son premier passage', () => {
  const vues = affichees(donnees, '2026-11-01', '2027-02-01');
  const cette = [...vues.values()].find((v) => v.origine === 'VAYISHLACH');
  assert.deepEqual([cette.passage, [...cette.rites].sort()], ['Obadiah 1:1-1:21', ['ashkenaz', 'edot', 'sefard']]);
  const p = L.parachaSemaine(donnees, '2026-11-26', { nusah: 'edot' });
  assert.equal(p.lecture.haftaraDe, 'VAYISHLACH');
  // Chabbat 'Hanouka : la haftara vient du jour, non de la paracha.
  assert.equal(L.parachaSemaine(donnees, '2026-12-01', { nusah: 'edot' }).lecture.haftaraDe, 'Chanukah Day 1 (on Shabbat)');
  assert.equal(L.parachaSemaine(donnees, '2026-12-08', { nusah: 'edot' }).lecture.haftaraDe, 'Chanukah Day 8 (on Shabbat)');
  for (const c of fichier.contextes) {
    for (const o of c.occasions) for (const passage of c.passages) assert.equal(trouve(fichier.contextes, o, passage), c, c.id);
  }
});
