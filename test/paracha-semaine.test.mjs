// La paracha de la semaine pour Chnayim mikra : jamais une lecture de Yom tov, les parachiot jumelées, les
// Chabbatot spéciaux, Israël et la diaspora ; l'hébreu deux fois puis le Targoum ; le Targoum Onkelos aligné sur
// le texte ; les noms hébreux des livres selon la langue.
// Repris de My Hitbodedut (web/test/lecture-siddur.test.mjs, 26/11/2026), sans ce qui tient à son siddour.

import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import test from 'node:test';

const require = createRequire(import.meta.url);
const { NUSAH, chnayimMikra, nombreVersets, parachaSemaine, plage, reference, versets } = require('../web/lecture.js');
const { decoupeTexte, longueurs } = require('../tools/construit_donnees.js');

const raw = (nom) => JSON.parse(readFileSync(new URL(`../data/${nom}`, import.meta.url), 'utf8'));
const donnees = raw('lecture_torah.json');
const texte = raw('lecture_torah_texte.json');
const targoum = raw('lecture_torah_targoum.json');
const parLivre = decoupeTexte(texte);
const targoumParLivre = decoupeTexte(targoum);

const semaine = (iso, enIsrael = false, nusah = 'edot') => parachaSemaine(donnees, iso, { enIsrael, nusah });

test('la paracha de la semaine, jamais une lecture de Yom tov', () => {
  const mardi = semaine('2026-11-24');
  assert.equal(mardi.date, '2026-11-28');
  assert.equal(mardi.paracha, 'VAYISHLACH');
  assert.equal(mardi.lecture.cle, 'parasha:VAYISHLACH');
  assert.equal(mardi.lecture.montees.length, 8);
  assert.equal(mardi.lecture.haftara[0].livre, 'Obadiah');
  assert.deepEqual(semaine('2026-11-28'), mardi);
  // Avant Souccot 5787 et la semaine de Sim'hat Torah : Berèchit, le 10/10.
  for (const il of [true, false]) assert.equal(semaine('2026-09-22', il).date, '2026-10-10');
  assert.equal(semaine('2026-10-04').lecture.titre.fr, 'Berèchit');
  // Avant Pessa'h 5786 : Chabbat 'Hol hamoed sauté, Chemini le 11/04.
  assert.deepEqual([semaine('2026-03-31', false, 'ashkenaz').date, semaine('2026-03-31', false, 'ashkenaz').lecture.cle], ['2026-04-11', 'parasha:SHMINI']);
  // 5789 : le 8e jour de Pessa'h un Chabbat en diaspora.
  assert.equal(semaine('2029-04-03', true, 'ashkenaz').date, '2029-04-07');
  assert.equal(semaine('2029-04-03', false, 'ashkenaz').date, '2029-04-14');
  // Deux parachiot jointes : Matot-Masé.
  const jointes = semaine('2027-07-27', false, 'ashkenaz');
  assert.equal(jointes.paracha, 'MATOS_MASEI');
  assert.equal(jointes.lecture.cle, 'parasha:MATOS_MASEI');
  assert.equal(jointes.lecture.titre.fr, 'Matot-Masé');
  assert.deepEqual([jointes.lecture.montees[0].debut, jointes.lecture.montees[6].fin], ['30:2', '36:13']);
  // Chabbat Chekalim : son maftir et sa haftara.
  for (const nusah of NUSAH) {
    const l = semaine('2027-03-02', false, nusah).lecture;
    assert.ok(l.cle.startsWith('parasha:VAYAKHEL+Shabbat Shekalim'), nusah);
    assert.equal(l.montees.at(-1).debut, '30:11');
    assert.equal(l.haftara[0].livre, 'II Kings');
    assert.ok(l.raisons.length > 0);
  }
  // Dans tout un cycle : toujours une paracha, un Chabbat, pas avant le jour.
  for (let t = Date.UTC(2026, 8, 1); t < Date.UTC(2027, 9, 1); t += 864e5) {
    const iso = new Date(t).toISOString().slice(0, 10);
    for (const il of [true, false]) {
      const p = semaine(iso, il);
      assert.ok(p.lecture.cle.startsWith('parasha:') && new Date(`${p.date}T12:00:00Z`).getUTCDay() === 6 && p.date >= iso, iso);
    }
  }
});

test('Chnayim mikra : l\'hébreu deux fois puis le Targoum, ou une fois selon le réglage', () => {
  const h = versets('Genesis', '32:4', '32:6', parLivre.Genesis);
  const t = versets('Genesis', '32:4', '32:6', targoumParLivre.Genesis);
  const deux = chnayimMikra(h, t);
  assert.deepEqual(deux.map((l) => l.v), [4, 4, 4, 5, 5, 5, 6, 6, 6]);
  assert.deepEqual(deux.map((l) => l.targoum), [false, false, true, false, false, true, false, false, true]);
  assert.equal(deux[0].t, h[0].t);
  assert.deepEqual(deux[0], deux[1]);
  assert.ok(deux[2].t.startsWith('וּשְׁלַח יַעֲקֹב אִזְגַּדִּין'));
  assert.deepEqual(chnayimMikra(h, t, true).map((l) => l.targoum), [false, true, false, true, false, true]);
  assert.throws(() => chnayimMikra(h, t.slice(1)));
});

test('le Targoum Onkelos : même versification que le texte, livre par livre', () => {
  const heb = texte.livres;
  assert.deepEqual(Object.keys(targoum.livres), ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy']);
  let n = 0;
  for (const [livre, chapitres] of Object.entries(targoum.livres)) {
    assert.deepEqual(Object.keys(chapitres), Object.keys(heb[livre]), livre);
    for (const [c, v] of Object.entries(chapitres)) { assert.equal(v.length, heb[livre][c].length, `${livre} ${c}`); n += v.length; }
  }
  assert.equal(n, 5847);
  assert.equal(targoum.livres.Numbers['25'][18], 'וַהֲוָה בָּתַר מוֹתָנָא׃');
  assert.equal(targoum._meta.licence, 'Public Domain');
});

test('les livres portent leur nom hébreu, écrit à la manière de chaque langue', () => {
  assert.equal(reference(donnees, 'Genesis', '32:4', '32:13'), 'Berèchit 32:4–13');
  assert.equal(reference(donnees, 'Hosea', '14:2', '14:10', (t) => t.he), 'הושע 14:2–10');
  assert.equal(reference(donnees, 'Hosea', '14:2', '14:10', (t) => t.en), 'Hoshea 14:2–10');
  assert.equal(reference(donnees, 'Obadiah', '1:1', '1:21'), 'Ovadia 1:1–21');
  assert.equal(reference(donnees, 'I Samuel', '20:18', '20:42', (t) => t.en), 'Shmuel I 20:18–42');
  assert.equal(reference(donnees, 'Genesis', '32:31', '33:5'), 'Berèchit 32:31–33:5');
  assert.equal(plage('36:43', '36:43'), '36:43');
  // Jamais les noms de tradition chrétienne dans ce qui s'affiche (les clés internes restent celles d'hebcal).
  const noms = Object.values(donnees.livres).flatMap((l) => [l.he, l.fr, l.en]);
  for (const interdit of ['Abdias', 'Osée', 'Isaïe', 'Ésaïe', 'Jérémie', 'Ézéchiel', 'Genèse', 'Exode', 'Obadiah', 'Hosea', 'Isaiah', 'Kings', 'Rois']) {
    assert.ok(!noms.some((n) => n.includes(interdit)), interdit);
  }
  for (const l of Object.values(donnees.livres)) assert.ok(l.he && l.fr && l.en);
});

test('le nombre de versets d\'une montée se compte sans charger le texte', () => {
  const L = longueurs(texte);
  for (const p of Object.values(donnees.parachiot)) {
    for (const [, livre, debut, fin] of p.alyot) {
      assert.equal(nombreVersets(debut, fin, L[livre]), versets(livre, debut, fin, parLivre[livre.replace(/ /g, '_')]).length, `${livre} ${debut}-${fin}`);
    }
  }
  assert.equal(nombreVersets('32:4', '32:13', L.Genesis), 10);
  assert.equal(nombreVersets('32:31', '33:5', L.Genesis), 8);
});
