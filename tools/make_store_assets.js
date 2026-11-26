#!/usr/bin/env node
/* Produit les images de la fiche Google Play dans docs/fiche-google-play/ :
   - captures d'écran téléphone 1080 × 1920 (JPEG) pour chaque langue de la fiche ;
   - bannière 1024 × 500 (PNG).
   Usage : node tools/make_store_assets.js <fichier text.js avec les vrais textes>
   (lancer d'abord `node tools/fetch_sefaria.js`, qui écrit web/data/text.js). Demande Playwright. */
const fs = require('fs'), path = require('path'), os = require('os');
const { chromium } = require('playwright');
const root = path.join(__dirname, '..'), out = path.join(root, 'docs', 'fiche-google-play');
const data = path.resolve(process.argv[2] || path.join(root, 'web', 'data', 'text.js'));
const LANGS = ['fr', 'en', 'es', 'he'];

(async () => {
  /* copie de l'app avec les textes fournis */
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'sm-fiche-')); fs.cpSync(path.join(root, 'web'), path.join(tmp, 'web'), { recursive: true });
  fs.copyFileSync(data, path.join(tmp, 'web', 'data', 'text.js'));
  const T = {}; global.window = {}; require(path.join(tmp, 'web', 'data', 'text.js')); const weeks = (window.SM_TEXT.diaspora || {}).weeks || [];
  const cur = weeks.filter(w => w.alyot && !w.holiday).slice(-1)[0]; if (!cur) throw new Error('pas de textes dans ' + data);
  /* « maintenant » : le mardi de la semaine de la dernière paracha disponible, 9 h à Paris */
  const sh = new Date(cur.shabbatISO + 'T00:00:00Z'), now = Date.UTC(sh.getUTCFullYear(), sh.getUTCMonth(), sh.getUTCDate() - 4, 8, 0, 0);
  /* progression d'exemple : deux alyot lues cette semaine, sept semaines terminées avant */
  const prog = {}; prog[cur.shabbatISO] = { n: 2, name: cur.parasha, he: cur.parashaHe, idx: [cur.parashaIndex] };
  for (let k = 1; k <= 7 && cur.parashaIndex - k >= 0; k++) { const d = new Date(sh.getTime() - 7 * k * 864e5).toISOString().slice(0, 10); prog[d] = { n: 7, name: '', he: '', idx: [cur.parashaIndex - k] }; }
  const b = await chromium.launch();
  for (const lang of LANGS) {
    const ctx = await b.newContext({ viewport: { width: 360, height: 640 }, deviceScaleFactor: 3, locale: 'fr-FR', timezoneId: 'Europe/Paris' });
    await ctx.route(/^https?:/, r => r.abort());
    await ctx.addInitScript(([l, n, pr]) => { window.SM_NOW = n; if (!localStorage.getItem('sm.settings')) { localStorage.setItem('sm.settings', JSON.stringify({ onboarded: true, place: 1, city: 'paris', lang: l })); localStorage.setItem('sm.prog', JSON.stringify(pr)); } }, [lang, now, prog]);
    const p = await ctx.newPage(); await p.goto('file://' + path.join(tmp, 'web', 'index.html')); await p.waitForTimeout(700);
    const dir = path.join(out, 'captures', lang); fs.mkdirSync(dir, { recursive: true });
    const go = async (h) => { await p.evaluate(x => { location.hash = '#/' + x; }, h); await p.waitForTimeout(900); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(200); };
    const shot = (name) => p.screenshot({ path: path.join(dir, name + '.jpg'), type: 'jpeg', quality: 90 });
    await go('accueil'); await shot('1-accueil');
    await p.evaluate(() => { APP.set('par', 0); APP.set('alya', 2); APP.set('alyaTo', null); }); await go('lecteur'); await shot('2-lecteur');
    await p.evaluate(() => { APP.set('mode', 'sombre'); }); await p.waitForTimeout(900); await shot('3-lecteur-sombre'); await p.evaluate(() => { APP.set('mode', 'clair'); });
    await go('annee'); await shot('4-annee');
    await go('reglages'); await p.evaluate(() => { const el = document.querySelector('.scroll'); const h = [...el.querySelectorAll('h2')].find(x => x.closest('section') && x.closest('section').querySelector('[role=radiogroup]')); if (h) el.scrollTop = h.getBoundingClientRect().top + el.scrollTop - 24; }); await p.waitForTimeout(400); await shot('5-reglages');
    await go('imprimer'); await shot('6-imprimer');
    await ctx.close(); console.error(lang + ' : 6 captures');
  }
  /* bannière : le dessin de l'icône et le nom */
  const icon = fs.readFileSync(path.join(root, 'android', 'icone', 'icone.svg'), 'utf8').replace(/<!--[\s\S]*?-->/, '');
  const inner = icon.replace(/^[\s\S]*?<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '').replace(/<rect width="512" height="512"[^>]*\/>/, '');
  const html = '<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Heebo:wght@500;800&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">' +
    '<style>html,body{margin:0}#b{width:1024px;height:500px;position:relative;overflow:hidden;background:radial-gradient(circle at 30% 45%,#1D3F86 0%,#0A1C47 75%);color:#fff}' +
    '#b svg{position:absolute;left:36px;top:26px;width:448px;height:448px}#t{position:absolute;left:520px;right:44px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;gap:18px}' +
    'h1{margin:0;font:700 66px/1.05 "Playfair Display",serif;letter-spacing:-.01em}p{margin:0}.he{font:500 40px/1.2 Heebo,sans-serif;color:#E9C778;direction:rtl;text-align:left}.l{width:120px;height:5px;border-radius:3px;background:linear-gradient(90deg,#B8842A,#F6DC95,#B8842A)}</style></head>' +
    '<body><div id="b"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">' + inner + '</svg><div id="t"><h1>Shnayim Mikra</h1><div class="l"></div><p class="he">שניים מקרא ואחד תרגום</p></div></div></body></html>';
  const pg = await b.newPage({ viewport: { width: 1024, height: 500 }, deviceScaleFactor: 1 }); await pg.setContent(html); await pg.evaluate(() => document.fonts.ready); await pg.waitForTimeout(500);
  await pg.locator('#b').screenshot({ path: path.join(out, 'banniere-1024x500.png') });
  await b.close(); fs.rmSync(tmp, { recursive: true, force: true }); console.error('bannière écrite');
})();
