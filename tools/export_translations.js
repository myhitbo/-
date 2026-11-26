#!/usr/bin/env node
/* Écrit docs/traductions-a-relire.csv : tous les textes de l'interface et de la chaîne WhatsApp, en français et en tounsi,
   avec une colonne vide pour les corrections des relecteurs. À relancer après chaque changement de texte. */
const fs = require('fs'), path = require('path'), vm = require('vm');
const web = path.join(__dirname, '..', 'web');
const w = {}; w.window = w; const ctx = vm.createContext(w);
for (const f of ['i18n.js', 'i18n/tn.js']) vm.runInContext(fs.readFileSync(path.join(web, f), 'utf8'), ctx);
const T = w.SM_I18N;
/* Les textes propres à l'écran Réglages sont dans screens/reglages.js */
const src = fs.readFileSync(path.join(web, 'screens', 'reglages.js'), 'utf8');
const grab = (name) => JSON.parse(src.split('\n').find(l => l.startsWith('const ' + name + ' = ')).slice(('const ' + name + ' = ').length).replace(/;\s*$/, ''));
const R = grab('T'), NT = grab('NT');
const rows = [['Clé', 'Français', 'Tounsi (brouillon)', 'Correction']];
const skip = { locale: 1, alyot: 1, books: 1, parashiyot: 1, cities: 1 };
for (const k of Object.keys(T.fr)) { if (skip[k]) continue; const v = T.fr[k];
  if (v && typeof v === 'object') { for (const j of Object.keys(v)) rows.push([k + '.' + j, v[j], (T.tn[k] || {})[j] || '', '']); }
  else rows.push([k, v, T.tn[k] || '', '']); }
for (const k of Object.keys(R.fr)) { if (k === 'draft' || k === 'cityVal' || k === 'rhythmVal' || k === 'orderVal') continue; rows.push(['reglages.' + k, R.fr[k], R.tn[k] || '', '']); }
rows.push(['reglages.nt.title', NT.fr.title, NT.tn.title, '']); rows.push(['reglages.nt.help', NT.fr.help, NT.tn.help, '']);
NT.fr.o.forEach((x, i) => rows.push(['reglages.nt.' + (i + 1), x, NT.tn.o[i], '']));
for (const id of Object.keys(T.tn.cities)) rows.push(['ville.' + id, id, T.tn.cities[id], '']);
/* Les messages de la chaîne WhatsApp sont dans chaine/textes.js */
const CH = require(path.join(__dirname, '..', 'chaine', 'textes.js'));
for (const k of Object.keys(CH.fr)) rows.push(['chaine.' + k, CH.fr[k], CH.tn[k] || '', '']);
const csv = rows.map(r => r.map(c => '"' + String(c).replace(/"/g, '""') + '"').join(';')).join('\r\n');
fs.writeFileSync(path.join(__dirname, '..', 'docs', 'traductions-a-relire.csv'), '﻿' + csv + '\r\n');
console.error((rows.length - 1) + ' lignes');
