#!/usr/bin/env node
/* Met une icône à tous les formats demandés par Android et Google Play.
   Usage : node tools/make_icons.js <icone.svg | icone.png> [dossier de sortie]
   - l'image fournie est l'icône « visible » : un carré plein, sans coins arrondis ni ombre ;
   - écrit les dossiers « mipmap » de android/app/src/main/res (icône classique, icône ronde, icône adaptative) et docs/icone-google-play-512.png.
   Demande Playwright (présent sur le poste de développement) ; les images produites sont enregistrées dans le dépôt. */
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const src = process.argv[2]; if (!src) { console.error('Usage : node tools/make_icons.js <icone.svg|icone.png> [sortie]'); process.exit(1); }
const root = path.resolve(process.argv[3] || path.join(__dirname, '..'));
const res = path.join(root, 'android', 'app', 'src', 'main', 'res');
const DENS = { mdpi: 1, hdpi: 1.5, xhdpi: 2, xxhdpi: 3, xxxhdpi: 4 };
const isSvg = /\.svg$/i.test(src);
const FONTS = '<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@800&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">';

(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ deviceScaleFactor: 1 });
  const svg = isSvg ? fs.readFileSync(src, 'utf8') : null;
  const dataUrl = isSvg ? null : 'data:image/png;base64,' + fs.readFileSync(src).toString('base64');
  /* Dessin de l'icône visible, dans un carré de `size` pixels ; `mask` : '' (carré), 'round' ou 'squircle' */
  async function shot(size, mask, file, wide) {
    const radius = mask === 'round' ? '50%' : mask === 'squircle' ? '22%' : '0';
    let inner;
    if (isSvg) {
      /* icône adaptative : le dessin occupe les deux tiers du milieu, le fond s'étend jusqu'aux bords */
      inner = wide ? svg.replace(/viewBox="0 0 512 512"/, 'viewBox="-128 -128 768 768"').replace(/<rect width="512" height="512"/g, '<rect x="-128" y="-128" width="768" height="768"') : svg;
    } else {
      inner = wide ? '<div style="width:100%;height:100%;background:var(--edge);display:flex;align-items:center;justify-content:center"><img src="' + dataUrl + '" style="width:66.667%;height:66.667%"></div>'
                   : '<img src="' + dataUrl + '" style="width:100%;height:100%;display:block">';
    }
    await p.setViewportSize({ width: size, height: size });
    await p.setContent('<!doctype html><html><head>' + FONTS + '<style>html,body{margin:0;background:transparent}#i{width:' + size + 'px;height:' + size + 'px;overflow:hidden;border-radius:' + radius + '}#i svg{display:block;width:100%;height:100%}</style></head><body><div id="i">' + inner + '</div></body></html>');
    if (!isSvg && wide) await p.evaluate(async () => { const im = document.querySelector('img'); await im.decode(); const c = document.createElement('canvas'); c.width = c.height = 8; const x = c.getContext('2d'); x.drawImage(im, 0, 0, 8, 8); const d = x.getImageData(0, 0, 1, 1).data; document.querySelector('#i > div').style.setProperty('--edge', 'rgb(' + d[0] + ',' + d[1] + ',' + d[2] + ')'); });
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(250);
    fs.mkdirSync(path.dirname(file), { recursive: true });
    await p.locator('#i').screenshot({ path: file, omitBackground: mask !== '' });
  }
  for (const d of Object.keys(DENS)) {
    await shot(Math.round(48 * DENS[d]), 'squircle', path.join(res, 'mipmap-' + d, 'ic_launcher.png'));
    await shot(Math.round(48 * DENS[d]), 'round', path.join(res, 'mipmap-' + d, 'ic_launcher_round.png'));
    await shot(Math.round(108 * DENS[d]), '', path.join(res, 'mipmap-' + d, 'ic_launcher_foreground.png'), true);
  }
  const adaptive = '<?xml version="1.0" encoding="utf-8"?>\n<!-- Icône adaptative (Android 8 et plus) : image écrite par tools/make_icons.js -->\n<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n    <background android:drawable="@mipmap/ic_launcher_foreground" />\n    <foreground android:drawable="@mipmap/ic_launcher_foreground" />\n</adaptive-icon>\n';
  fs.mkdirSync(path.join(res, 'mipmap-anydpi-v26'), { recursive: true });
  fs.writeFileSync(path.join(res, 'mipmap-anydpi-v26', 'ic_launcher.xml'), adaptive);
  fs.writeFileSync(path.join(res, 'mipmap-anydpi-v26', 'ic_launcher_round.xml'), adaptive);
  await shot(512, '', path.join(root, 'docs', 'icone-google-play-512.png'));
  await b.close(); console.error('Icônes écrites dans ' + res + ' et docs/icone-google-play-512.png');
})();
