// L'application (web/globals.js) sur le moteur et le texte embarqués, sans navigateur : la semaine en cours,
// ses 7 alyot, la haftara selon le rite, les Chabbatot spéciaux, Israël et la diaspora, les noms selon la
// langue, les versets sans Targoum, la progression. Les scripts de web/ sont chargés tels que la page les
// charge (scripts classiques, dans l'ordre d'index.html), dans un contexte qui tient lieu de fenêtre.

import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import test from 'node:test';
import vm from 'node:vm';

const require = createRequire(import.meta.url);
const { fichiers, script } = require('../tools/construit_donnees.js');
const web = (nom) => readFileSync(new URL(`../web/${nom}`, import.meta.url), 'utf8');
const DONNEES = Object.values(fichiers()).map(([nom, contenu]) => script(nom, contenu)).join('');

/** Une application neuve : [reglages] (place : 0 Israël, 1 diaspora), à la date [iso] à midi, heure de Paris. */
function application(reglages = {}, iso = '2026-11-26') {
  const stock = {};
  const fenetre = {
    console, Intl, Date, Math, JSON, Promise, setTimeout, clearTimeout,
    navigator: { onLine: false },
    localStorage: { getItem: (k) => (k in stock ? stock[k] : null), setItem: (k, v) => { stock[k] = String(v); }, removeItem: (k) => { delete stock[k]; } },
    document: { createElement: () => ({}), head: { appendChild: () => {} }, getElementById: () => null },
  };
  fenetre.window = fenetre;
  const etat = Object.assign({ place: 1, city: 'paris', lang: 'fr', rite: 'edot', nt: 'deux' }, reglages);
  fenetre.APP = { get: (k) => (k === 'done' ? fenetre.SM_DONE.get() : etat[k]), set: (k, v) => { etat[k] = v; } };
  fenetre.SM_NOW = Date.parse(`${iso}T11:00:00Z`);
  vm.createContext(fenetre);
  for (const nom of ['vendor/kosher-zmanim-0.9.0.min.js', 'lecture.js', 'donnees.js']) vm.runInContext(web(nom), fenetre, { filename: nom });
  vm.runInContext(DONNEES, fenetre, { filename: 'data' });
  vm.runInContext(web('globals.js'), fenetre, { filename: 'globals.js' });
  return { w: fenetre, etat, stock, date: (d) => { fenetre.SM_NOW = Date.parse(`${d}T11:00:00Z`); } };
}
const refs = (h) => h.parts.map((p) => p.ref).join(' ; ');

test('la page charge les scripts dans l\'ordre : calendrier, moteur, données, puis l\'application', () => {
  const scripts = [...web('index.html').matchAll(/<script src="([^"]+)"/g)].map((m) => m[1]);
  assert.deepEqual(scripts, ['vendor/kosher-zmanim-0.9.0.min.js', 'lecture.js', 'donnees.js', 'data/lecture.js', 'sefaria.js', 'globals.js', 'runtime.js', 'screens.js', 'ecrans.js']);
});

test('jeudi 26/11/2026 : Vayichla\'h, ses 7 alyot, la haftara d\'Ovadia', () => {
  const { w } = application();
  assert.equal(w.SM_OK(), true);
  const s = w.SM_WEEK(0), G = w.SM_G();
  assert.equal(s.shabbatISO, '2026-11-28');
  assert.deepEqual([G.parasha, G.parashaHe, G.parashaRef], ['Vayichla’h', 'וישלח', 'Berèchit 32:4 – 36:43']);
  assert.deepEqual(Array.from(s.alyot, (a) => `${a.name} ${a.verses} ${a.count}`), ['Rishon 32:4 – 13 10', 'Sheni 32:14 – 30 17', 'Shlishi 32:31 – 33:5 8', "Revi'i 33:6 – 20 15", 'Hamishi 34:1 – 35:11 42', 'Shishi 35:12 – 36:19 37', "Shvi'i 36:20 – 43 24"]);
  assert.equal(s.parashaIndex, 7); // la 8e paracha de l'année (écran Année)
  assert.deepEqual([G.haftara.ref, G.haftara.rite, G.haftara.hasReason, G.haftara.hasExtra], ['Ovadia 1:1–21', "Edot hamizra'h", false, false]);
  assert.match(G.candleLine, /^Allumage vendredi à 16:\d\d · Paris/);
  assert.deepEqual(Array.from(w.SM_NEXT(), (n) => n.name), ['Vayéchev', 'Mikets', 'Vayigach']);
  // Le lecteur : chaque verset deux fois, puis le Targoum.
  w.APP.set('par', 0); w.APP.set('alya', 0);
  const b = w.SM_BLOCKS();
  assert.equal(b.length, 30);
  assert.deepEqual(Array.from(b.slice(0, 3), (x) => `${x.kind} ${x.n} ${x.ref}`), ['mikra 1 32:4', 'mikra 2 32:4', 'targum 3 32:4']);
  assert.ok(b[2].text.startsWith('וּשְׁלַח יַעֲקֹב אִזְגַּדִּין'));
  // Réglage « ×1 » : l'hébreu affiché une fois, puis le Targoum.
  w.APP.set('une', true);
  assert.deepEqual(Array.from(w.SM_BLOCKS().slice(0, 4), (x) => `${x.kind} ${x.ref} ${x.label || ''}`.trim()), ['mikra 32:4 Mikra · à lire 2 fois', 'targum 32:4', 'mikra 32:5 Mikra · à lire 2 fois', 'targum 32:5']);
  assert.equal(w.SM_BLOCKS().length, 20);
  w.APP.set('une', false);
  // La haftara : chaque verset une fois, sans Targoum.
  w.APP.set('alya', 7);
  const h = w.SM_BLOCKS();
  assert.equal(h.length, 21);
  assert.ok(h.every((x) => x.kind === 'mikra' && x.label === 'Haftara'));
  assert.equal(w.SM_G().alyaName, 'Haftara');
});

test('la haftara ne compte pas dans les 7 alyot', () => {
  const { w, stock } = application();
  w.APP.set('par', 0); w.APP.set('alya', 7); w.SM_G(); w.SM_MARK();
  assert.deepEqual(JSON.parse(stock['sm.prog'])['2026-11-28'], { n: 0, name: 'Vayichla’h', he: 'וישלח', h: 1 });
  assert.equal(w.SM_G().haftara.done, true);
  w.APP.set('alya', 2); w.SM_MARK();
  assert.equal(JSON.parse(stock['sm.prog'])['2026-11-28'].n, 3);
  assert.equal(JSON.parse(stock['sm.prog'])['2026-11-28'].h, 1);
  assert.equal(w.SM_DONE.get(), 3);
});

test('jamais une lecture de Yom tov : la semaine de Souccot mène à Berèchit, avec sa date', () => {
  for (const place of [0, 1]) {
    const { w } = application({ place, city: place ? 'paris' : 'telaviv' }, '2026-09-29');
    assert.deepEqual([w.SM_WEEK(0).shabbatISO, w.SM_WEEK(0).key], ['2026-10-10', 'BERESHIS']);
    assert.ok(Array.from(w.SM_NEXT(), (n) => n.name).includes('Noa’h'));
  }
});

test('Israël et la diaspora : après Pessa\'h 5789, deux parachiot différentes', () => {
  const il = application({ place: 0, city: 'telaviv', rite: 'ashkenaz' }, '2029-04-04').w, dia = application({ rite: 'ashkenaz' }, '2029-04-04').w;
  assert.deepEqual([il.SM_WEEK(0).shabbatISO, il.SM_WEEK(0).key], ['2029-04-07', 'SHMINI']);
  assert.deepEqual([dia.SM_WEEK(0).shabbatISO, dia.SM_WEEK(0).key], ['2029-04-14', 'SHMINI']);
});

test('Chabbat Chekalim : la paracha garde ses 7 alyot, le maftir et la haftara du jour selon le rite', () => {
  const edot = application({}, '2027-03-02').w.SM_WEEK(0), ashk = application({ rite: 'ashkenaz' }, '2027-03-02').w.SM_WEEK(0), sfard = application({ rite: 'sefard' }, '2027-03-02').w.SM_WEEK(0);
  assert.equal(edot.key, 'VAYAKHEL');
  assert.equal(edot.alyot.length, 7);
  assert.deepEqual([edot.alyot[0].debut, edot.alyot[6].fin], ['35:1', '38:20']);
  assert.deepEqual(Array.from(edot.haftara.reasons), ['Chabbat Chekalim']);
  assert.equal(edot.haftara.extraRef, 'Maftir : Chemot 30:11–16');
  assert.equal(refs(edot.haftara), 'Melakhim II 11:17–12:17');
  assert.equal(refs(ashk.haftara), 'Melakhim II 12:1–17');
  assert.equal(refs(sfard.haftara), refs(ashk.haftara));
  assert.equal(sfard.haftara.rite, 'Sfard');
});

test('trois Sifrei Torah (Chabbat Roch \'Hodech \'Hanouka) : les 7 alyot restent celles de la paracha', () => {
  const s = application({ rite: 'ashkenaz' }, '2025-12-16').w.SM_WEEK(0);
  assert.equal(s.key, 'MIKETZ');
  assert.deepEqual([s.alyot.length, s.alyot[0].debut, s.alyot[6].fin], [7, '41:1', '44:17']);
  assert.deepEqual(Array.from(s.haftara.extra, (x) => `${x.label} ${x.ref}`), ['Chevi’i Bamidbar 28:9–15', 'Maftir Bamidbar 7:42–47']);
  assert.equal(refs(s.haftara), 'Zekharia 2:14–4:7');
});

test('les noms selon la langue : hébreu écrit à la manière du français, de l\'anglais, ou en hébreu', () => {
  const lit = (lang) => { const { w } = application({ lang }); const G = w.SM_G(); return [G.parasha, G.parashaRef, G.haftara.ref]; };
  assert.deepEqual(lit('fr'), ['Vayichla’h', 'Berèchit 32:4 – 36:43', 'Ovadia 1:1–21']);
  assert.deepEqual(lit('en'), ['Vayishlach', 'Bereshit 32:4 – 36:43', 'Ovadia 1:1–21']);
  assert.deepEqual(lit('es'), lit('en'));
  assert.deepEqual(lit('tn'), lit('fr'));
  assert.deepEqual(lit('he'), ['וישלח', 'בראשית 32:4 – 36:43', 'עובדיה 1:1–21']);
});

test('versets sans Targoum : « Atarot ve-Divon » et les versets de noms seuls', () => {
  // Matot-Massé 5787 (Chabbat 31/07/2027) : Bamidbar 32:3 est dans la 3e alya.
  const { w, etat } = application({}, '2027-07-27');
  const s = w.SM_WEEK(0);
  assert.equal(s.key, 'MATOS_MASEI');
  const k = s.alyot.findIndex((a) => a.v.some((v) => v.ref === '32:3'));
  assert.ok(k >= 0);
  const v = s.alyot[k].v.find((x) => x.ref === '32:3');
  assert.equal(v.nt, 1);
  assert.ok(v.yer.startsWith('מַכְלֶלְתָּא וּמַלְבֶּשְׁתָּא'));
  w.APP.set('par', 0); w.APP.set('alya', k);
  const blocs = (mode) => { etat.nt = mode; return Array.from(w.SM_BLOCKS().filter((b) => b.ref === '32:3'), (b) => b.label || b.kind); };
  assert.deepEqual(blocs('deux'), ['mikra', 'mikra', '3ᵉ lecture · pas de Targoum', 'Targoum Yerouchalmi']);
  assert.deepEqual(blocs('trois'), ['mikra', 'mikra', '3ᵉ lecture · pas de Targoum']);
  assert.deepEqual(blocs('yer'), ['mikra', 'mikra', 'Targoum Yerouchalmi']);
  etat.une = true;
  assert.deepEqual(blocs('deux'), ['Mikra · à lire 3 fois, pas de Targoum', 'Targoum Yerouchalmi']);
  assert.deepEqual(blocs('trois'), ['Mikra · à lire 3 fois, pas de Targoum']);
  assert.deepEqual(blocs('yer'), ['Mikra · à lire 2 fois', 'Targoum Yerouchalmi']);
  etat.une = false;
  // Chemot 1:2 (« Réouven, Chimon, Lévi et Yehouda ») : Onkelos reprend l'hébreu, lu trois fois hors ligne.
  const chemot = application({}, '2027-01-01').w.SM_WEEK(0);
  assert.equal(chemot.key, 'SHEMOS');
  const noms = Array.from(chemot.alyot[0].v.filter((x) => x.nt), (x) => x.ref);
  assert.deepEqual(noms, ['1:2', '1:4']);
  assert.equal(chemot.alyot[0].v.find((x) => x.ref === '1:2').yer, '');
});

test('le contexte de la haftara : trouvé par son origine et son premier passage, dans la langue de l\'interface', () => {
  const essai = { contextes: [{ id: 'essai', occasions: ['VAYISHLACH'], passages: ['Obadiah 1:1-1:21'], phrases: [
    { fr: 'Phrase une.', en: 'Sentence one.', sources: [{ genre: 'classique', ref: { fr: 'Rachi sur Ovadia 1:1', en: 'Rashi on Ovadia 1:1' }, sefaria: 'Rashi on Obadiah 1:1', citation: 'עֹבַדְיָה' }] },
    { fr: 'Phrase deux.', en: 'Sentence two.', sources: [{ genre: 'aujourdhui', ref: { fr: 'Auteur, Titre', en: 'Author, Title' }, auteur: 'A', titre: 'T', url: 'https://exemple.org/x' }] },
  ] }] };
  const { w, etat } = application();
  assert.equal(w.SM_G().haftara.hasContexte, false); // pas encore chargé : l'encadré ne s'affiche pas
  w.SM_DATA('contexte', essai);
  const h = w.SM_G().haftara;
  assert.equal(h.hasContexte, true);
  assert.deepEqual(Array.from(h.contexte, (c) => c.text), ['Phrase une.', 'Phrase deux.']);
  assert.deepEqual({ ...h.contexte[0].sources[0] }, { ref: 'Rachi sur Ovadia 1:1', citation: 'עֹבַדְיָה', hasCitation: true, lien: 'https://www.sefaria.org/Rashi_on_Obadiah_1:1?lang=he' });
  assert.deepEqual({ ...h.contexte[1].sources[0] }, { ref: 'Auteur, Titre', citation: '', hasCitation: false, lien: 'https://exemple.org/x' });
  etat.lang = 'en';
  assert.deepEqual(Array.from(w.SM_G().haftara.contexte, (c) => c.text), ['Sentence one.', 'Sentence two.']);
  // Une autre semaine, une autre haftara : pas de contexte pour elle.
  const autre = application({}, '2026-12-15');
  autre.w.SM_DATA('contexte', essai);
  assert.equal(autre.w.SM_G().haftara.hasContexte, false);
});

test('l\'impression : ce qu\'il reste, puis la haftara', () => {
  const { w } = application();
  const tout = w.SM_PRINT_INFO(true);
  assert.deepEqual([tout.count, tout.range, tout.first, tout.haftara], [7, "Rishon – Shvi'i", 'Rishon · 32:4', 'Ovadia 1:1–21']);
  w.SM_DONE.set(5);
  assert.deepEqual([w.SM_PRINT_INFO(false).count, w.SM_PRINT_INFO(false).range], [2, "Shishi – Shvi'i"]);
});

test('toute une année, en Israël et en diaspora, pour les trois rites : chaque semaine a ses 7 alyot et sa haftara', () => {
  for (const place of [0, 1]) {
    for (const rite of ['edot', 'sefard', 'ashkenaz']) {
      const app = application({ place, city: place ? 'paris' : 'jerusalem', rite });
      for (let t = Date.UTC(2026, 8, 6); t < Date.UTC(2027, 9, 10); t += 7 * 864e5) {
        app.date(new Date(t).toISOString().slice(0, 10));
        const s = app.w.SM_WEEK(0);
        assert.equal(s.alyot.length, 7, s.shabbatISO);
        assert.ok(s.haftara.parts.length >= 1 && s.haftara.ref, s.shabbatISO);
        assert.ok(s.parashaIndex >= 0 && s.parashaIndex <= 52, s.shabbatISO);
        assert.equal(new Date(`${s.shabbatISO}T12:00:00Z`).getUTCDay(), 6);
      }
    }
  }
});
