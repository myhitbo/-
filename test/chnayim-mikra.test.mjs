// « Chnayim mikra : les halakhot » (tools/chnayim_mikra/construction.py) : le livre de data/, tel que
// l'application le charge (web/data/halakhot.js), et sa table de vérification, citation par citation.
// Repris de My Hitbodedut (web/test/chnayim-mikra.test.mjs, 26/11/2026), sans ce qui tient à sa bibliothèque.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const lire = (chemin) => readFileSync(new URL(`../${chemin}`, import.meta.url), 'utf8');
const livre = JSON.parse(lire('data/livre_chnayim_mikra.json'));
const halakhot = livre.sections.flatMap((s) => s.blocs.filter((b) => b.id));
const table = JSON.parse(lire('tools/chnayim_mikra/sources.json'));

/** 1 → א, 15 → טו, 31 → לא : le numéro d'une halakha en lettres, sans guillemets. */
function lettres(n) {
  const u = ' אבגדהוזחט', d = ' יכלמנסעפצ';
  if (n === 15) return 'טו';
  if (n === 16) return 'טז';
  return ((n >= 10 ? d[Math.floor(n / 10)] : '') + (n % 10 ? u[n % 10] : '')).trim();
}

test('le livre a ses trois titres et ses neuf chapitres, et l\'application le charge tel quel', () => {
  assert.deepEqual(livre.titre, { he: 'הלכות שנים מקרא ואחד תרגום', fr: 'Chnayim mikra\u00a0: les halakhot', en: 'Shnayim mikra: the laws' });
  assert.equal(livre.sections.length, 9); // l'introduction et huit chapitres de halakhot
  for (const s of livre.sections) assert.ok(s.titre && s.titre_fr && s.titre_en, s.titre);
  const { fichiers } = require('../tools/construit_donnees.js');
  assert.deepEqual(fichiers()['halakhot.js'], ['halakhot', livre]);
});

test('chaque halakha a son hébreu, son français, son anglais, ses références et son rite', () => {
  assert.equal(halakhot.length, 65);
  assert.deepEqual(halakhot.map((h) => h.id), halakhot.map((_, i) => `chm-${String(i + 1).padStart(2, '0')}`));
  halakhot.forEach((h, i) => {
    for (const champ of ['t', 'fr', 'en']) assert.ok(h[champ]?.trim(), `${h.id} ${champ}`);
    assert.ok(['tous', 'sefarade', 'ashkenaze'].includes(h.rite), h.id);
    assert.ok(h.refs.length > 0, h.id);
    assert.ok(h.t.startsWith(`<b>${lettres(i + 1)}</b>`), h.id);
    assert.ok(h.fr.startsWith(`<b>${i + 1}</b>`) && h.en.startsWith(`<b>${i + 1}</b>`), h.id);
    // Seules les balises que l'écran sait rendre.
    for (const t of [h.t, h.fr, h.en]) assert.ok(!/<(?!\/?(b|small)>|br>)/.test(t), h.id);
  });
  assert.deepEqual(new Set(halakhot.map((h) => h.rite)), new Set(['tous', 'sefarade', 'ashkenaze']));
  // Les 31 du cahier de reprise (13 pour tous, 10 séfarades, 8 ashkénazes) et les 34 ajoutées le 26/11/2026 (12, 11, 11).
  const compte = (r) => halakhot.filter((h) => h.rite === r).length;
  assert.deepEqual([compte('tous'), compte('sefarade'), compte('ashkenaze')], [25, 21, 19]);
});

test('le rite se lit en tête de la halakha, dans les trois langues', () => {
  const etiquettes = {
    sefarade: ['[ספרדים – עדות המזרח]', '[Séfarades – rite Edot hamizra’h]', '[Sephardim – Edot HaMizrach rite]'],
    ashkenaze: ['[אשכנזים – נוסח אשכנז ונוסח ספרד]', '[Ashkénazes – rites Ashkenaz et Sfard]', '[Ashkenazim – Ashkenaz and Sfard rites]'],
  };
  for (const h of halakhot) {
    const textes = [h.t, h.fr, h.en];
    if (etiquettes[h.rite]) textes.forEach((t, k) => assert.ok(t.split('</b>')[1].startsWith(` <small>${etiquettes[h.rite][k]}</small>`), h.id));
    else for (const e of Object.values(etiquettes).flat()) assert.ok(!textes.some((t) => t.includes(e)), h.id);
  }
  assert.deepEqual(livre.rites, { tous: ['edot', 'sefard', 'ashkenaz'], sefarade: ['edot'], ashkenaze: ['ashkenaz', 'sefard'] });
});

test('la table de vérification suit le livre, citation par citation', () => {
  assert.equal(table.halakhot.length, halakhot.length);
  table.halakhot.forEach((l, i) => {
    const h = halakhot[i];
    assert.equal(l.id, h.id);
    assert.equal(l.rite, h.rite);
    for (const r of l.references) {
      assert.ok(h.refs.includes(r.reference), `${h.id} ${r.reference}`);
      if (r.citation) assert.ok(h.t.includes(r.citation), `${h.id} ${r.citation.slice(0, 30)}`);
      if (['hid', 'kav', 'malka', 'kikar'].includes(r.source)) {
        // Réponses d'aujourd'hui, protégées : résumées et référencées, une courte phrase citée au plus.
        assert.match(r.url, /^https:\/\//);
        assert.equal(r.nature, 'paraphrase avec référence (œuvre protégée)');
        if (r.citation) assert.ok(r.citation.split(' ').length <= 16, `${h.id} : citation trop longue`);
        // La table ne recopie pas la réponse : seulement les repères du passage résumé.
        if (r.passage_resume) assert.ok(r.passage_resume.replaceAll('[...]', ' ').trim().split(/\s+/).length <= 25, `${h.id} : passage trop long`);
      } else assert.ok(r.citation && r.lu_via, `${h.id} ${r.reference}`);
    }
  });
  // Les sources et licences du livre sont dans son _meta, et l'introduction crédite celles qui le demandent.
  assert.ok(livre._meta.sources.some((s) => s.includes('Kehot Publication Society (via API Sefaria), CC-BY-NC')));
  const intro = livre.sections[0].blocs[0];
  for (const t of [intro.t, intro.fr, intro.en]) assert.ok(t.includes('CC BY-NC') && t.includes('CC BY-NC-SA 2.5'));
});
