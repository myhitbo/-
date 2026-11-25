#!/usr/bin/env node
/* Télécharge les polices de l'app (Google Fonts) dans web/fonts/ et écrit web/fonts/fonts.css,
   pour que l'app fonctionne hors ligne et sans appel à Google. À relancer seulement si la liste change. */
const fs = require('fs'), path = require('path');
const OUT = path.join(__dirname, '..', 'web', 'fonts');
const CSS = 'https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=Inter:wght@400;500;600;700' +
  '&family=Frank+Ruhl+Libre:wght@400;500&family=David+Libre:wght@400;500&family=Noto+Serif+Hebrew:wght@400;500&family=Heebo:wght@400;500' +
  '&family=Noto+Sans+Arabic:wght@400;600;700&display=swap';
const KEEP = ['latin', 'latin-ext', 'hebrew', 'arabic'];
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36';
(async () => {
  const css = await (await fetch(CSS, { headers: { 'User-Agent': UA } })).text();
  const blocks = css.split('/* ').slice(1).map(b => ({ subset: b.slice(0, b.indexOf(' */')), body: b.slice(b.indexOf('@font-face')) }));
  fs.mkdirSync(OUT, { recursive: true });
  const seen = {}; let out = '/* Polices embarquées (licence SIL OFL 1.1, voir LICENCES.md). Fichier écrit par tools/fetch_fonts.js. */\n', total = 0;
  for (const b of blocks) {
    if (KEEP.indexOf(b.subset) < 0) continue;
    const fam = b.body.match(/font-family: '([^']+)'/)[1], w = b.body.match(/font-weight: ([\d ]+)/)[1].trim().replace(' ', '-'), url = b.body.match(/url\((https:[^)]+)\)/)[1];
    let name = seen[url];
    if (!name) { name = (fam.replace(/ /g, '') + '-' + b.subset + '.woff2'); let k = 2; while (Object.values(seen).indexOf(name) >= 0) name = fam.replace(/ /g, '') + '-' + b.subset + '-' + (k++) + '.woff2';
      const buf = Buffer.from(await (await fetch(url, { headers: { 'User-Agent': UA } })).arrayBuffer()); fs.writeFileSync(path.join(OUT, name), buf); total += buf.length; seen[url] = name; }
    out += b.body.replace(/url\(https:[^)]+\)/, "url('" + name + "')").replace(/\n+$/, '') + '\n';
    console.error(fam + ' ' + w + ' ' + b.subset + ' → ' + name);
  }
  fs.writeFileSync(path.join(OUT, 'fonts.css'), out);
  console.error(Object.keys(seen).length + ' fichiers, ' + Math.round(total / 1024) + ' Ko');
})();
