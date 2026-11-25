/* Écran « Sources » — éditions et licences des textes, polices. Gabarit (tpl) puis logique (make). */
SCREENS.sources = {
  title: "Sources",
  tpl: `

<div class="t {{themeClass}}" dir="{{dir}}" style="{{rootStyle}}; position: relative; width: 100%; height: 100vh; overflow: hidden; background: var(--bg); color: var(--text); font-family: Inter, 'Heebo', 'Noto Sans Arabic', sans-serif">
<sc-if value="{{isParch}}" hint-placeholder-val="{{false}}"><svg aria-hidden="true" viewBox="0 0 400 900" preserveAspectRatio="none" style="position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none"><defs><filter id="pm" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.011" numOctaves="5" seed="5"></feTurbulence><feColorMatrix values="0 0 0 0 0.50  0 0 0 0 0.33  0 0 0 0 0.12  0 0 0 0.55 -0.12"></feColorMatrix></filter><filter id="pf" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.018 0.9" numOctaves="2" seed="8"></feTurbulence><feColorMatrix values="0 0 0 0 0.40  0 0 0 0 0.27  0 0 0 0 0.10  0 0 0 0.16 0"></feColorMatrix></filter><filter id="pg" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" stitchTiles="stitch"></feTurbulence><feColorMatrix values="0 0 0 0 0.35  0 0 0 0 0.24  0 0 0 0 0.10  0 0 0 0.15 0"></feColorMatrix></filter><filter id="pbl"><feGaussianBlur stdDeviation="2"></feGaussianBlur></filter><radialGradient id="pv" cx="50%" cy="45%" r="75%"><stop offset="0.55" stop-color="#6B4415" stop-opacity="0"></stop><stop offset="0.86" stop-color="#6B4415" stop-opacity="0.15"></stop><stop offset="1" stop-color="#4A2C0A" stop-opacity="0.38"></stop></radialGradient></defs><rect width="400" height="900" filter="url(#pm)"></rect><rect width="400" height="900" filter="url(#pf)"></rect><rect width="400" height="900" filter="url(#pg)"></rect><circle cx="249" cy="668" r="6.8" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="296" cy="830" r="2.2" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="377" cy="584" r="7.4" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="188" cy="222" r="5.3" fill="#8A5A1C" opacity="0.11" filter="url(#pbl)"></circle><circle cx="5" cy="195" r="3.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="306" cy="144" r="6.8" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="247" cy="114" r="2.0" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="84" cy="194" r="7.9" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="116" cy="865" r="5.2" fill="#8A5A1C" opacity="0.12" filter="url(#pbl)"></circle><circle cx="82" cy="847" r="6.1" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="357" cy="269" r="4.2" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="58" cy="59" r="3.8" fill="#8A5A1C" opacity="0.11" filter="url(#pbl)"></circle><circle cx="1" cy="610" r="4.0" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="327" cy="433" r="3.9" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="282" cy="51" r="7.9" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="300" cy="760" r="2.1" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="146" cy="521" r="2.1" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="72" cy="860" r="3.2" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="372" cy="848" r="4.1" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="210" cy="698" r="2.6" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="319" cy="774" r="2.2" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="36" cy="307" r="5.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="136" cy="832" r="5.3" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="127" cy="160" r="2.5" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="276" cy="897" r="3.0" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="395" cy="480" r="4.4" fill="#8A5A1C" opacity="0.08" filter="url(#pbl)"></circle><circle cx="238" cy="744" r="4.7" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="22" cy="824" r="2.2" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="335" cy="118" r="6.4" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="252" cy="709" r="2.6" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="60" cy="760" r="3.8" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="400" cy="767" r="7.9" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="195" cy="657" r="4.9" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="162" cy="132" r="4.3" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="384" cy="564" r="5.0" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="36" cy="245" r="6.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><rect width="400" height="900" fill="url(#pv)"></rect></svg></sc-if><div aria-hidden="true" style="position: absolute; top: -120px; right: -90px; width: 340px; height: 340px; border-radius: 50%; background: radial-gradient(circle at 40% 40%, var(--blob1), transparent 68%); opacity: var(--blobop); filter: blur(30px); pointer-events: none"></div>
<div aria-hidden="true" style="position: absolute; top: -60px; left: -120px; width: 300px; height: 260px; border-radius: 50%; background: radial-gradient(circle, var(--blob2), transparent 70%); opacity: var(--blobop); filter: blur(40px); pointer-events: none"></div>
<div class="scroll" style="position: absolute; inset: 0; overflow-y: auto">
<main style="position: relative; max-width: 560px; margin: 0 auto; padding: 22px 20px 40px; display: flex; flex-direction: column; gap: 24px">
<a href="V2-Reglages.dc.html" aria-label="{{t.back}}" class="glass" style="width: 44px; height: 44px; border-radius: 22px; display: flex; align-items: center; justify-content: center; color: var(--text)"><svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"></path></svg></a>
<header style="display: flex; flex-direction: column; gap: 4px"><p class="cap" style="margin: 0">{{t.srcKicker}}</p><h1 class="serif foil" style="margin: 0; font-size: clamp(36px, 11vw, 52px); font-weight: 500; line-height: 1; letter-spacing: -0.02em">{{t.srcTitle}}</h1></header>
<section style="display: flex; flex-direction: column; gap: 10px">
  <h2 class="cap" style="margin: 0">{{t.srcTexts}}</h2>
  <sc-for list="{{texts}}" as="x" hint-placeholder-count="3">
    <div class="glass" style="border-radius: 20px; padding: 14px 16px; display: flex; flex-direction: column; gap: 4px">
      <p style="margin: 0; font-size: 15px; font-weight: 600">{{x.name}}</p>
      <p dir="ltr" style="margin: 0; font-size: 13px; line-height: 1.45; color: var(--soft); text-align: start">{{x.edition}}</p>
      <sc-if value="{{x.hasUrl}}" hint-placeholder-val="{{true}}"><p style="margin: 0; font-size: 13px">{{t.srcLicense}} : <a href="{{x.url}}" target="_blank" rel="noopener" style="font-weight: 600">{{x.license}}</a>{{x.note}}</p></sc-if>
      <sc-if value="{{x.noUrl}}" hint-placeholder-val="{{false}}"><p style="margin: 0; font-size: 13px">{{t.srcLicense}} : <span style="font-weight: 600">{{x.license}}</span>{{x.note}}</p></sc-if>
    </div>
  </sc-for>
  <p style="margin: 0; font-size: 13px; line-height: 1.5; color: var(--soft)">{{t.srcSefaria}} <a href="https://www.sefaria.org" target="_blank" rel="noopener" style="font-weight: 600">sefaria.org</a></p>
</section>
<section style="display: flex; flex-direction: column; gap: 8px">
  <h2 class="cap" style="margin: 0">{{t.srcFonts}}</h2>
  <p style="margin: 0; font-size: 13px; line-height: 1.5; color: var(--soft)">{{t.srcFontsLine}} <a href="https://openfontlicense.org" target="_blank" rel="noopener" style="font-weight: 600">SIL Open Font License 1.1</a>.</p>
</section>
</main>
</div>

</div>
`,
  make: function () {
const THEMES = SM_THEMES, rootVars = SM_ROOTVARS;
/* Éditions utilisées si les textes embarqués ne les indiquent pas encore (voir docs/09-licences-textes.md) */
const DEFAULTS = { mikra: { title: 'Miqra according to the Masorah', license: 'CC-BY-SA' }, onk: { title: 'Sifsei Chachomim Chumash, Metsudah Publications, 2009', license: 'CC-BY-NC' }, yer: { title: 'Targum Jerusalem on Torah', license: 'Public Domain' } };
const LICENSES = { 'CC-BY-SA': ['CC BY-SA', 'https://creativecommons.org/licenses/by-sa/3.0/'], 'CC-BY-NC': ['CC BY-NC', 'https://creativecommons.org/licenses/by-nc/4.0/'], 'CC-BY': ['CC BY', 'https://creativecommons.org/licenses/by/3.0/'], 'CC0': ['CC0', 'https://creativecommons.org/publicdomain/zero/1.0/'] };
class Component extends DCLogic {
  renderVals() {
    const mode = this.props.mode || 'clair', t = SM_TR();
    const w = window.SM_WEEK ? SM_WEEK(0) : null; const src = Object.assign({}, DEFAULTS, (w && w.src) || {});
    const row = (name, m, extra) => { const lic = LICENSES[m.license];
      return { name, edition: m.title + (extra ? ' — ' + extra : ''), license: lic ? lic[0] : (m.license === 'Public Domain' || m.license === 'PD') ? t.srcPD : (m.license || '—'),
        url: lic ? lic[1] : '', hasUrl: !!lic, noUrl: !lic, note: m.license === 'CC-BY-NC' ? ' (' + t.srcNC + ')' : '' }; };
    return { themeClass: 'th-' + mode, isParch: mode === 'parchemin', dir: 'ltr', rootStyle: rootVars(mode),
      texts: [row(t.srcMikra, src.mikra), row(t.srcOnk, src.onk), row(t.srcYer, src.yer, t.srcYerNote)] };
  }
}

return Component;
  }
};
