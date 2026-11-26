#!/usr/bin/env node
/* Construit les données que l'application charge (web/data/) à partir des sources de data/.

   L'application s'ouvre depuis un fichier (file://, WebView Android) : fetch() n'y lit pas de JSON,
   une balise <script> si. Chaque fichier écrit ici appelle donc SM_DATA(nom, contenu) :

     web/data/lecture.js            les lectures (data/lecture_torah.json) et la longueur des chapitres
     web/data/texte/<Livre>.js      le texte d'un livre, lu à la demande (data/lecture_torah_texte.json)
     web/data/targoum/<Livre>.js    le Targoum Onkelos d'un livre (data/lecture_torah_targoum.json)
     web/data/halakhot.js           le recueil des halakhot (data/livre_chnayim_mikra.json), s'il existe
     web/data/contexte.js           le contexte des haftarot (data/contexte_haftarot.json), s'il existe

   web/data/ n'est pas suivi par git : relancer « node tools/construit_donnees.js » après un clone
   (la compilation de l'APK le fait). Sans réseau, quelques dixièmes de seconde. */
const fs = require('fs'), path = require('path');
const { fichierLivre } = require('../web/lecture.js');

const RACINE = path.join(__dirname, '..');
const DATA = path.join(RACINE, 'data');
const lis = (nom) => JSON.parse(fs.readFileSync(path.join(DATA, nom), 'utf8'));
const existe = (nom) => fs.existsSync(path.join(DATA, nom));

/** Un fichier par livre : { livre, chapitres, paragraphes }. */
function decoupeTexte(texte) {
  const sortie = {};
  for (const [livre, chapitres] of Object.entries(texte.livres)) {
    if (!/^[A-Za-z ]+$/.test(livre)) throw new Error(`Livre inattendu : ${livre}`);
    sortie[fichierLivre(livre)] = { livre, chapitres, paragraphes: (texte.paragraphes && texte.paragraphes[livre]) || {} };
  }
  return sortie;
}

/** { livre: { chapitre: nombre de versets } } : pour compter les versets d'une montée sans charger le texte. */
function longueurs(texte) {
  const sortie = {};
  for (const [livre, chapitres] of Object.entries(texte.livres)) {
    sortie[livre] = Object.fromEntries(Object.entries(chapitres).map(([c, v]) => [c, v.length]));
  }
  return sortie;
}

/** Tout ce qui sera écrit : { 'chemin relatif à web/data': [nom, contenu] }. */
function fichiers() {
  const texte = lis('lecture_torah_texte.json'), targoum = lis('lecture_torah_targoum.json');
  const lecture = Object.assign({}, lis('lecture_torah.json'), { longueurs: longueurs(texte) });
  const sortie = { 'lecture.js': ['lecture', lecture] };
  for (const [f, contenu] of Object.entries(decoupeTexte(texte))) sortie[`texte/${f}.js`] = [`texte/${f}`, contenu];
  for (const [f, contenu] of Object.entries(decoupeTexte(targoum))) sortie[`targoum/${f}.js`] = [`targoum/${f}`, contenu];
  if (existe('livre_chnayim_mikra.json')) sortie['halakhot.js'] = ['halakhot', lis('livre_chnayim_mikra.json')];
  if (existe('contexte_haftarot.json')) sortie['contexte.js'] = ['contexte', lis('contexte_haftarot.json')];
  return sortie;
}

const script = (nom, contenu) => `SM_DATA(${JSON.stringify(nom)}, ${JSON.stringify(contenu)});\n`;

function construit(dossier = path.join(RACINE, 'web', 'data')) {
  fs.rmSync(dossier, { recursive: true, force: true });
  let octets = 0; const liste = fichiers();
  for (const [chemin, [nom, contenu]] of Object.entries(liste)) {
    const cible = path.join(dossier, chemin);
    fs.mkdirSync(path.dirname(cible), { recursive: true });
    const s = script(nom, contenu); octets += Buffer.byteLength(s);
    fs.writeFileSync(cible, s);
  }
  return { n: Object.keys(liste).length, octets };
}

module.exports = { decoupeTexte, longueurs, fichiers, script, construit };

if (require.main === module) {
  const { n, octets } = construit();
  console.error(`web/data : ${n} fichiers, ${(octets / 1048576).toFixed(2)} Mo`);
}
