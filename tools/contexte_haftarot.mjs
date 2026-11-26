// Le contexte des haftarot (docs/09-cahier-de-reprise.md § 6) : le contrôle de data/contexte_haftarot.json.
//
//   node tools/contexte_haftarot.mjs              contrôle hors ligne : forme, sources, noms, couverture
//   node tools/contexte_haftarot.mjs --strict     échoue aussi si une haftara affichée n'a pas son contexte
//   node tools/contexte_haftarot.mjs --sources    relit chaque citation classique sur Sefaria (réseau)
//
// La forme d'un contexte :
//   { "id": "vayichlah",
//     "occasions": ["VAYISHLACH"],             d'où vient la haftara : clé de paracha (web/lecture.js, PARSHIOT)
//                                              ou de lecture spéciale (data/lecture_torah.json, « lectures »)
//     "passages": ["Obadiah 1:1-1:21"],        le premier passage de la haftara, sous chaque forme selon le rite
//     "phrases": [                             4 à 6 phrases
//       { "fr": "…", "en": "…",
//         "sources": [                         au moins une par phrase
//           { "genre": "classique", "ref": { "fr": "Rachi sur Ovadia 1:1", "en": "Rashi on Ovadia 1:1" },
//             "sefaria": "Rashi on Obadiah 1:1", "version": "Sefaria Vocalized Edition", "licence": "CC0",
//             "citation": "עֹבַדְיָה גֵּר אֲדוֹמִי הָיָה" },
//           { "genre": "aujourdhui", "ref": { "fr": "…", "en": "…" }, "auteur": "…", "titre": "…", "url": "https://…" } ] } ] }
//
// Les règles (cahier § 6) : sources 'harédi uniquement — 'Hazal, commentateurs classiques, auteurs 'harédim
// d'aujourd'hui reformulés, jamais recopiés ; ni travaux universitaires, ni critique biblique, ni Wikipédia, ni
// encyclopédies générales, ni sources chrétiennes, ni Daat Mikra ; les noms hébreux (Ovadia, Eliyahou, A'hav),
// jamais les noms de tradition chrétienne ; un point sans source acceptée est laissé de côté.

import { readFileSync, writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const L = require('../web/lecture.js');

const ICI = dirname(fileURLToPath(import.meta.url));
export const FICHIER = join(ICI, '..', 'data', 'contexte_haftarot.json');
const DONNEES = join(ICI, '..', 'data', 'lecture_torah.json');

// --- Les sources classiques acceptées, par leur référence Sefaria ------------------------------------------

const TANAKH = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'I Samuel', 'II Samuel', 'I Kings', 'II Kings',
  'Isaiah', 'Jeremiah', 'Ezekiel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah',
  'Malachi', 'Psalms', 'Proverbs', 'Job', 'Song of Songs', 'Ruth', 'Lamentations', 'Ecclesiastes', 'Esther', 'Daniel', 'Ezra', 'Nehemiah',
  'I Chronicles', 'II Chronicles'];
const COMMENTATEURS = ['Rashi', 'Radak', 'Ibn Ezra', 'Ralbag', 'Abarbanel', 'Metzudat David', 'Metzudat Zion', 'Malbim'];
const TALMUD = ['Berakhot', 'Shabbat', 'Eruvin', 'Pesachim', 'Shekalim', 'Yoma', 'Sukkah', 'Beitzah', 'Rosh Hashanah', 'Taanit', 'Megillah',
  'Moed Katan', 'Chagigah', 'Yevamot', 'Ketubot', 'Nedarim', 'Nazir', 'Sotah', 'Gittin', 'Kiddushin', 'Bava Kamma', 'Bava Metzia', 'Bava Batra',
  'Sanhedrin', 'Makkot', 'Shevuot', 'Avodah Zarah', 'Horayot', 'Zevachim', 'Menachot', 'Chullin', 'Bekhorot', 'Arakhin', 'Temurah', 'Keritot',
  'Meilah', 'Tamid', 'Niddah'];
const MIDRACH = ['Seder Olam Rabbah', 'Bereishit Rabbah', 'Shemot Rabbah', 'Vayikra Rabbah', 'Bamidbar Rabbah', 'Devarim Rabbah',
  'Shir HaShirim Rabbah', 'Eichah Rabbah', 'Kohelet Rabbah', 'Esther Rabbah', 'Ruth Rabbah', 'Midrash Tanchuma', 'Midrash Tanchuma Buber',
  'Pesikta DeRav Kahana', 'Pesikta Rabbati', 'Pirkei DeRabbi Eliezer', 'Yalkut Shimoni on Nach', 'Yalkut Shimoni on Torah', 'Sifrei Devarim',
  'Sifrei Bamidbar', 'Sifra', 'Mekhilta DeRabbi Yishmael', 'Midrash Tehillim', 'Tanna Debei Eliyahu Rabbah', 'Tanna debei Eliyahu Zuta',
  'Avot DeRabbi Natan', 'Midrash Mishlei', 'Midrash Shmuel', 'Jerusalem Talmud', 'Mishnah', 'Tosefta', 'Targum Jonathan on'];
// Le choix de la haftara : la Guemara (Meguila 29b-31b) et ses commentaires, Rambam, Tour, Choul'han Aroukh, Aboudarham, Levouch, Michna Beroura.
const CHOIX = ['Rashi on Megillah', 'Tosafot on Megillah', 'Mishneh Torah, Prayer and the Priestly Blessing', 'Tur, Orach Chaim', 'Tur, Orach Chayim',
  'Beit Yosef, Orach Chaim', 'Shulchan Arukh, Orach Chayim', 'Abudarham', 'Sefer Abudarham', 'Levush', 'Mishnah Berurah', 'Magen Avraham',
  'Kitzur Shulchan Arukh', 'Kaf HaChayim on Shulchan Arukh, Orach Chayim', 'Arukh HaShulchan, Orach Chaim'];

/** La référence Sefaria [ref] est-elle une source classique acceptée ? */
export function classiqueAcceptee(ref) {
  const commence = (liste) => liste.some((x) => ref === x || ref.startsWith(`${x} `) || ref.startsWith(`${x},`));
  if (COMMENTATEURS.some((c) => TANAKH.some((l) => ref.startsWith(`${c} on ${l} `)))) return true;
  return commence(TANAKH) || commence(TALMUD) || commence(MIDRACH) || commence(CHOIX);
}

/** Les sites d'auteurs 'harédim d'aujourd'hui acceptés : à compléter avec l'accord du propriétaire. */
export const AUJOURDHUI = [];

// --- Les noms : hébreux, jamais ceux de tradition chrétienne ----------------------------------------------------

const INTERDITS = {
  fr: ['Abdias', 'Élie', 'Elie', 'Élisée', 'Elisée', 'Achab', 'Jézabel', 'Jéroboam', 'Roboam', 'Osée', 'Isaïe', 'Ésaïe', 'Esaïe', 'Jérémie',
    'Ézéchiel', 'Ezéchiel', 'Zacharie', 'Malachie', 'Michée', 'Aggée', 'Josué', 'Moïse', 'Salomon', 'Saül', 'Ésaü', 'Esaü', 'Jacob', 'Isaac',
    'Jéhu', 'Sédécias', 'Ézéchias', 'Josias', 'Nabuchodonosor', 'Babylone', 'Samuel', 'Genèse', 'Exode', 'Lévitique', 'Deutéronome', 'Rois',
    'Juges', 'Chroniques', 'Ancien Testament', 'Bible hébraïque', 'Yahvé', 'Jéhovah'],
  en: ['Obadiah', 'Elijah', 'Elisha', 'Ahab', 'Jezebel', 'Jeroboam', 'Rehoboam', 'Hosea', 'Isaiah', 'Jeremiah', 'Ezekiel', 'Zechariah', 'Micah',
    'Haggai', 'Joshua', 'Moses', 'Solomon', 'Hiram', 'Saul', 'Esau', 'Jacob', 'Isaac', 'Jehu', 'Zedekiah', 'Hezekiah', 'Josiah', 'Nebuchadnezzar',
    'Babylon', 'Samuel', 'Genesis', 'Exodus', 'Leviticus', 'Deuteronomy', 'Kings', 'Judges', 'Chronicles', 'Old Testament', 'Hebrew Bible',
    'Yahweh', 'Jehovah'],
};
// Le 'het : le français du projet le marque d'une apostrophe en tête de mot ('Hazal, 'Hanouka, 'Hiram). Ces noms-ci ne sont
// interdits que sans elle : « Hiram » et « d'Hiram » sont refusés, « 'Hiram » est la forme attendue. (En anglais : « Chiram ».)
const SANS_HET = { fr: ['Hiram'], en: [] };
const litteral = (nom) => nom.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
const motif = (nom) => new RegExp(`(^|[^\\p{L}])${litteral(nom)}(?![\\p{L}])`, 'u');
const motifSansHet = (nom) => new RegExp(`(?<![\\p{L}])(?<!(?:^|[^\\p{L}])['’])${litteral(nom)}(?![\\p{L}])`, 'u');
/** Les noms interdits trouvés dans un texte français ou anglais. */
export const nomsInterdits = (texte, langue) => [
  ...INTERDITS[langue].filter((n) => motif(n).test(texte)),
  ...SANS_HET[langue].filter((n) => motifSansHet(n).test(texte)),
];

const EXCLUS = /wikipedia\.org|wikimedia\.org|britannica|jewishencyclopedia|thetorah\.com|biblehub|biblegateway|daat\.ac\.il|academia\.edu|jstor\.org|\.edu\//i;

// --- Les haftarot que l'application affiche ---------------------------------------------------------------------

const passage = (h) => `${h.livre} ${h.debut}-${h.fin}`;

/** { "origine|premier passage" : { origine, passage, rites, date } } : toutes les haftarot affichées entre [debut] et [fin]. */
export function affichees(donnees, debut = '2025-09-06', fin = '2075-09-01') {
  const vues = new Map();
  for (const options of [{ enIsrael: false }, { enIsrael: true }, { enIsrael: true, mukafChoma: true }]) {
    for (const nusah of L.NUSAH) {
      for (let iso = L.chabbatSuivant(debut); iso < fin; iso = L.ajouteJours(iso, 7)) {
        const p = L.parachaSemaine(donnees, iso, { ...options, nusah });
        if (p.date !== iso || !p.lecture.haftara.length) continue;
        const cle = `${p.lecture.haftaraDe}|${passage(p.lecture.haftara[0])}`;
        const e = vues.get(cle) ?? { origine: p.lecture.haftaraDe, passage: passage(p.lecture.haftara[0]), rites: new Set(), date: iso };
        e.rites.add(nusah);
        vues.set(cle, e);
      }
    }
  }
  return vues;
}

/** Le contexte d'une haftara : celui dont [occasions] nomme son origine et [passages] son premier passage. */
export const trouve = (contextes, origine, premier) => contextes.find((c) => c.occasions.includes(origine) && c.passages.includes(premier)) ?? null;

/** Le lien d'une source : la page Sefaria d'une source classique, l'adresse d'une source d'aujourd'hui. */
export const lien = (s) => (s.genre === 'classique' ? `https://www.sefaria.org/${encodeURI(s.sefaria.replace(/ /g, '_'))}?lang=he` : s.url);

// --- Le contrôle hors ligne -----------------------------------------------------------------------------------------

/** { erreurs, manquantes, couvertes, total } : la forme, les sources, les noms ; puis ce qui reste à écrire. */
export function controle(fichier, donnees) {
  const erreurs = [];
  const dit = (c, m) => erreurs.push(`${c.id ?? '?'} : ${m}`);
  const ids = new Set();
  for (const c of fichier.contextes) {
    if (!c.id || ids.has(c.id)) dit(c, 'identifiant absent ou en double');
    ids.add(c.id);
    if (!Array.isArray(c.occasions) || !c.occasions.length) dit(c, 'occasions absentes');
    for (const o of c.occasions ?? []) if (!donnees.parachiot[o] && !donnees.lectures[o]) dit(c, `occasion inconnue : ${o}`);
    if (!Array.isArray(c.passages) || !c.passages.length) dit(c, 'passages absents');
    for (const p of c.passages ?? []) if (!/^[A-Za-z ]+ \d+:\d+-\d+:\d+$/.test(p)) dit(c, `passage mal formé : ${p}`);
    const n = (c.phrases ?? []).length;
    if (n < 4 || n > 6) dit(c, `${n} phrases (il en faut 4 à 6)`);
    (c.phrases ?? []).forEach((ph, k) => {
      const ou = `phrase ${k + 1}`;
      for (const langue of ['fr', 'en']) {
        if (!ph[langue]?.trim()) dit(c, `${ou} : ${langue} absent`);
        else for (const nom of nomsInterdits(ph[langue], langue)) dit(c, `${ou} (${langue}) : nom interdit « ${nom} »`);
      }
      if (!Array.isArray(ph.sources) || !ph.sources.length) dit(c, `${ou} : sans source`);
      for (const s of ph.sources ?? []) {
        for (const langue of ['fr', 'en']) {
          if (!s.ref?.[langue]?.trim()) dit(c, `${ou} : référence ${langue} absente`);
          else for (const nom of nomsInterdits(s.ref[langue], langue)) dit(c, `${ou} : référence ${langue}, nom interdit « ${nom} »`);
        }
        if (s.genre === 'classique') {
          if (!s.sefaria || !classiqueAcceptee(s.sefaria)) dit(c, `${ou} : source classique non acceptée « ${s.sefaria} »`);
          if (!s.citation?.trim()) dit(c, `${ou} : citation absente (${s.sefaria})`);
          else if (!/[֐-׿]/.test(s.citation)) dit(c, `${ou} : citation sans hébreu (${s.sefaria})`);
          else if (s.citation.trim().split(/\s+/).length > 30) dit(c, `${ou} : citation de plus de 30 mots (${s.sefaria})`);
        } else if (s.genre === 'aujourdhui') {
          if (!s.auteur || !s.titre || !/^https:\/\//.test(s.url ?? '')) dit(c, `${ou} : source d'aujourd'hui sans auteur, titre ou adresse`);
          else if (!AUJOURDHUI.some((d) => new URL(s.url).hostname.replace(/^www\./, '') === d)) dit(c, `${ou} : site non accepté « ${new URL(s.url).hostname} »`);
          if (s.citation) dit(c, `${ou} : une source d'aujourd'hui se reformule, sans citation`);
        } else dit(c, `${ou} : genre de source inconnu « ${s.genre} »`);
        if (EXCLUS.test(`${s.url ?? ''} ${s.sefaria ?? ''}`)) dit(c, `${ou} : source exclue`);
      }
    });
  }
  const vues = affichees(donnees);
  const manquantes = [...vues.values()].filter((v) => !trouve(fichier.contextes, v.origine, v.passage));
  // Un contexte qui ne sert à aucune haftara affichée est sans doute mal désigné.
  for (const c of fichier.contextes) {
    if (![...vues.values()].some((v) => (c.occasions ?? []).includes(v.origine) && (c.passages ?? []).includes(v.passage))) dit(c, 'ne correspond à aucune haftara affichée');
  }
  return { erreurs, manquantes, couvertes: vues.size - manquantes.length, total: vues.size };
}

// --- La relecture des citations sur Sefaria ---------------------------------------------------------------------

const plat = (t) => t.replace(/<[^>]+>/g, ' ').normalize('NFC').replace(/ /g, ' ').replace(/\s+/g, ' ').trim();

async function texteSefaria(ref, version) {
  const v = `hebrew${version ? `|${version}` : ''}`;
  const url = `https://www.sefaria.org/api/v3/texts/${encodeURIComponent(ref)}?version=${encodeURIComponent(v)}&return_format=text_only`;
  for (let essai = 0; ; essai++) {
    const r = await fetch(url, { headers: { 'User-Agent': 'Mozilla/5.0 (verification contexte haftarot)' } });
    if (r.ok) {
      const d = await r.json();
      const morceaux = [];
      const tout = (x) => { if (Array.isArray(x)) x.forEach(tout); else if (typeof x === 'string') morceaux.push(x); };
      const lu = (d.versions ?? [])[0];
      if (!lu) throw new Error(`aucune version hébraïque pour « ${ref} »${version ? ` (${version})` : ''}`);
      tout(lu.text);
      return { texte: plat(morceaux.join(' ')), version: lu.versionTitle, licence: lu.license };
    }
    if ((r.status === 429 || r.status >= 500) && essai < 4) { await new Promise((ok) => setTimeout(ok, 2000 * 2 ** essai)); continue; }
    throw new Error(`HTTP ${r.status} pour « ${ref} »`);
  }
}

/** Relit chaque citation classique à sa source ; note la version et la licence lues. { fautes, lues, change }. */
export async function relit(fichier) {
  const fautes = []; let lues = 0, change = false; const dejaLus = new Map();
  for (const c of fichier.contextes) {
    for (const [k, ph] of c.phrases.entries()) {
      for (const s of ph.sources.filter((x) => x.genre === 'classique')) {
        const cle = `${s.sefaria}|${s.version ?? ''}`;
        try {
          if (!dejaLus.has(cle)) dejaLus.set(cle, await texteSefaria(s.sefaria, s.version));
          const lu = dejaLus.get(cle);
          const morceaux = plat(s.citation).split('[...]').map((m) => m.trim());
          if (!morceaux.every((m) => m && lu.texte.includes(m))) fautes.push(`${c.id}, phrase ${k + 1}, ${s.sefaria} : citation introuvable « ${s.citation.slice(0, 70)} »`);
          if (s.version !== lu.version || s.licence !== lu.licence) { s.version = lu.version; s.licence = lu.licence; change = true; }
          lues++;
        } catch (e) { fautes.push(`${c.id}, phrase ${k + 1}, ${s.sefaria} : ${e.message}`); }
      }
    }
  }
  return { fautes, lues, change };
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  const fichier = JSON.parse(readFileSync(FICHIER, 'utf8'));
  const donnees = JSON.parse(readFileSync(DONNEES, 'utf8'));
  const { erreurs, manquantes, couvertes, total } = controle(fichier, donnees);
  console.log(`${fichier.contextes.length} contextes ; ${couvertes} haftarot affichées couvertes sur ${total}`);
  for (const e of erreurs) console.log(`ERREUR ${e}`);
  if (manquantes.length) {
    console.log(`${manquantes.length} sans contexte :`);
    for (const m of manquantes.sort((a, b) => a.date.localeCompare(b.date))) console.log(`  ${m.origine} | ${m.passage} | ${[...m.rites].join(', ')} | première fois le ${m.date}`);
  }
  let echec = erreurs.length > 0 || (process.argv.includes('--strict') && manquantes.length > 0);
  if (process.argv.includes('--sources')) {
    const { fautes, lues, change } = await relit(fichier);
    console.log(`${lues} citations relues sur Sefaria`);
    for (const f of fautes) console.log(`ERREUR ${f}`);
    if (change) { writeFileSync(FICHIER, `${JSON.stringify(fichier, null, 1)}\n`); console.log('versions et licences notées dans le fichier'); }
    echec = echec || fautes.length > 0;
  }
  if (echec) process.exit(1);
  console.log(erreurs.length ? '' : 'forme, sources et noms : bon');
}
