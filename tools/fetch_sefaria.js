#!/usr/bin/env node
/* Construit web/data/text.js depuis Sefaria : semaine passée + 4 suivantes, pour Israël et la diaspora.
   En cas d'échec, le fichier de secours reste en place (l'app retentera en ligne). */
const fs = require('fs'), path = require('path');
const S = require('../web/sefaria.js');
const OUT = path.join(__dirname, '..', 'web', 'data', 'text.js');
const COUNT = +(process.env.SM_WEEKS || 5);
const log = (m) => console.error(m);

(async () => {
  try {
    const r = await fetch('https://www.sefaria.org/api/calendars', { headers: { Origin: 'null' } });
    log('CORS Sefaria (access-control-allow-origin) : ' + r.headers.get('access-control-allow-origin'));
  } catch (e) { log('Vérification CORS impossible : ' + e.message); }
  const now = process.env.SM_FROM ? new Date(process.env.SM_FROM + 'T00:00:00Z') : new Date();   /* SM_FROM=AAAA-MM-JJ : pour essayer une autre période */
  const from = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate() - 7));
  const data = { source: 'Sefaria (sefaria.org)', builtAt: now.toISOString() };
  for (const [key, dia] of [['diaspora', true], ['israel', false]]) {
    log('=== ' + key);
    const weeks = await S.weeks(from, COUNT, dia, log);
    if (!weeks.some(w => w.alyot)) { log('Aucune paracha pour ' + key + ', texte de secours conservé.'); process.exitCode = 1; return; }
    data[key] = { weeks };
  }
  fs.writeFileSync(OUT, 'window.SM_TEXT = ' + JSON.stringify(data) + ';\n');
  log('OK : ' + data.diaspora.weeks.map(w => w.parasha).join(', ') + ' | Israël : ' + data.israel.weeks.map(w => w.parasha).join(', '));
})().catch(e => { log('Sefaria indisponible : ' + e.message); process.exitCode = 1; });
