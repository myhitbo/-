/* Écran « Bienvenue » — gabarit (tpl) puis logique (make). */
SCREENS.bienvenue = {
  title: "Bienvenue",
  tpl: `

<div class="t {{themeClass}}" dir="{{dir}}" style="{{rootStyle}}; position: relative; width: 100%; height: 100vh; overflow: hidden; background: var(--bg); color: var(--text); font-family: Inter, 'Heebo', 'Noto Sans Arabic', sans-serif">
<sc-if value="{{isParch}}" hint-placeholder-val="{{false}}"><svg aria-hidden="true" viewBox="0 0 400 900" preserveAspectRatio="none" style="position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none"><defs><filter id="pm" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.011" numOctaves="5" seed="5"></feTurbulence><feColorMatrix values="0 0 0 0 0.50  0 0 0 0 0.33  0 0 0 0 0.12  0 0 0 0.55 -0.12"></feColorMatrix></filter><filter id="pf" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.018 0.9" numOctaves="2" seed="8"></feTurbulence><feColorMatrix values="0 0 0 0 0.40  0 0 0 0 0.27  0 0 0 0 0.10  0 0 0 0.16 0"></feColorMatrix></filter><filter id="pg" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" stitchTiles="stitch"></feTurbulence><feColorMatrix values="0 0 0 0 0.35  0 0 0 0 0.24  0 0 0 0 0.10  0 0 0 0.15 0"></feColorMatrix></filter><filter id="pbl"><feGaussianBlur stdDeviation="2"></feGaussianBlur></filter><radialGradient id="pv" cx="50%" cy="45%" r="75%"><stop offset="0.55" stop-color="#6B4415" stop-opacity="0"></stop><stop offset="0.86" stop-color="#6B4415" stop-opacity="0.15"></stop><stop offset="1" stop-color="#4A2C0A" stop-opacity="0.38"></stop></radialGradient></defs><rect width="400" height="900" filter="url(#pm)"></rect><rect width="400" height="900" filter="url(#pf)"></rect><rect width="400" height="900" filter="url(#pg)"></rect><circle cx="249" cy="668" r="6.8" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="296" cy="830" r="2.2" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="377" cy="584" r="7.4" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="188" cy="222" r="5.3" fill="#8A5A1C" opacity="0.11" filter="url(#pbl)"></circle><circle cx="5" cy="195" r="3.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="306" cy="144" r="6.8" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="247" cy="114" r="2.0" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="84" cy="194" r="7.9" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="116" cy="865" r="5.2" fill="#8A5A1C" opacity="0.12" filter="url(#pbl)"></circle><circle cx="82" cy="847" r="6.1" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="357" cy="269" r="4.2" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="58" cy="59" r="3.8" fill="#8A5A1C" opacity="0.11" filter="url(#pbl)"></circle><circle cx="1" cy="610" r="4.0" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="327" cy="433" r="3.9" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="282" cy="51" r="7.9" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="300" cy="760" r="2.1" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="146" cy="521" r="2.1" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="72" cy="860" r="3.2" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="372" cy="848" r="4.1" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="210" cy="698" r="2.6" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="319" cy="774" r="2.2" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="36" cy="307" r="5.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="136" cy="832" r="5.3" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="127" cy="160" r="2.5" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="276" cy="897" r="3.0" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="395" cy="480" r="4.4" fill="#8A5A1C" opacity="0.08" filter="url(#pbl)"></circle><circle cx="238" cy="744" r="4.7" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="22" cy="824" r="2.2" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="335" cy="118" r="6.4" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="252" cy="709" r="2.6" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="60" cy="760" r="3.8" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="400" cy="767" r="7.9" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="195" cy="657" r="4.9" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="162" cy="132" r="4.3" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="384" cy="564" r="5.0" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="36" cy="245" r="6.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><rect width="400" height="900" fill="url(#pv)"></rect></svg></sc-if><div aria-hidden="true" style="position: absolute; top: -120px; right: -90px; width: 340px; height: 340px; border-radius: 50%; background: radial-gradient(circle at 40% 40%, var(--blob1), transparent 68%); opacity: var(--blobop); filter: blur(30px); pointer-events: none"></div>
<div aria-hidden="true" style="position: absolute; top: -60px; left: -120px; width: 300px; height: 260px; border-radius: 50%; background: radial-gradient(circle, var(--blob2), transparent 70%); opacity: var(--blobop); filter: blur(40px); pointer-events: none"></div>
<div class="scroll" style="position: absolute; inset: 0; overflow-y: auto">
<main style="position: relative; max-width: 560px; margin: 0 auto; padding: 22px 20px 40px; display: flex; flex-direction: column; gap: 24px">
<div style="display: flex; align-items: center; justify-content: space-between">
  <div aria-label="Étape {{stepNum}} sur 3" style="display: flex; gap: 6px"><sc-for list="{{dots}}" as="d" hint-placeholder-count="3"><span style="{{d}}"></span></sc-for></div>
  <sc-if value="{{canBack}}" hint-placeholder-val="{{false}}"><button onClick="{{back}}" style="height: 44px; padding: 0 12px; border: none; background: none; color: var(--soft); font: 500 14px Inter, sans-serif">Retour</button></sc-if>
</div>

<sc-if value="{{s0}}" hint-placeholder-val="{{true}}">
  <div class="rise" style="display: flex; flex-direction: column; gap: 22px">
    <div><p lang="he" dir="rtl" class="foil" style="margin: 0 0 6px; text-align: left; font-family: 'Frank Ruhl Libre', serif; font-size: 34px">שְׁנַיִם מִקְרָא</p>
    <h1 class="serif" style="margin: 0; font-size: clamp(32px, 10vw, 44px); font-weight: 500; line-height: 1.05">Bienvenue.<br>Quelle langue ?</h1></div>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">
      <sc-for list="{{langs}}" as="l" hint-placeholder-count="6"><button onClick="{{l.pick}}" aria-pressed="{{l.on}}" style="{{l.style}}"><span dir="{{l.dir}}" style="font-size: 17px; font-weight: 700">{{l.native}}</span><span style="font-size: 12px; color: var(--soft)">{{l.sub}}</span></button></sc-for>
    </div>
  </div>
</sc-if>

<sc-if value="{{s1}}" hint-placeholder-val="{{false}}">
  <div class="rise" style="display: flex; flex-direction: column; gap: 22px">
    <h1 class="serif" style="margin: 0; font-size: clamp(32px, 10vw, 44px); font-weight: 500; line-height: 1.05">Où vis-tu ?</h1>
    <p style="margin: -10px 0 0; font-size: 15px; line-height: 1.5; color: var(--soft)">Pour la bonne paracha de la semaine et l'heure d'allumage des bougies.</p>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">
      <sc-for list="{{places}}" as="p" hint-placeholder-count="2"><button onClick="{{p.pick}}" aria-pressed="{{p.on}}" style="{{p.style}}"><span style="font-size: 17px; font-weight: 700">{{p.name}}</span></button></sc-for>
    </div>
    <label style="display: flex; flex-direction: column; gap: 8px"><span class="cap">Ville</span><select class="field" aria-label="Ville" ref="{{fillCities}}" onChange="{{pickCity}}"></select></label>
  </div>
</sc-if>

<sc-if value="{{s2}}" hint-placeholder-val="{{false}}">
  <div class="rise" style="display: flex; flex-direction: column; gap: 22px">
    <h1 class="serif" style="margin: 0; font-size: clamp(32px, 10vw, 44px); font-weight: 500; line-height: 1.05">Ton rythme</h1>
    <div role="radiogroup" aria-label="Rythme" style="display: flex; flex-direction: column; gap: 8px">
      <sc-for list="{{rhythms}}" as="r" hint-placeholder-count="4"><button role="radio" aria-checked="{{r.on}}" onClick="{{r.pick}}" style="{{r.style}}"><span style="{{r.dot}}"></span><span style="flex: 1; min-width: 0; text-align: start"><span style="display: block; font-size: 15px; font-weight: 600">{{r.title}}</span><span style="display: block; font-size: 13px; color: var(--soft)">{{r.sub}}</span></span></button></sc-for>
    </div>
    <label style="display: flex; flex-direction: column; gap: 8px"><span class="cap">{{t.remTime}}</span><input class="field" type="time" value="{{remAt}}" onChange="{{pickRemAt}}"></label>
  </div>
</sc-if>

<div style="display: flex; flex-direction: column; gap: 10px; margin-top: 6px">
  <sc-if value="{{notLast}}" hint-placeholder-val="{{true}}"><button onClick="{{next}}" style="height: 56px; border-radius: 28px; border: none; background: var(--pill); color: var(--on-pill); font: 600 16px Inter, sans-serif">Continuer</button></sc-if>
  <sc-if value="{{last}}" hint-placeholder-val="{{false}}"><a href="V2-Accueil.dc.html" style="height: 56px; border-radius: 28px; background: var(--pill); color: var(--on-pill); display: flex; align-items: center; justify-content: center; text-decoration: none; font: 600 16px Inter, sans-serif">C'est parti</a></sc-if>
  <p style="margin: 0; text-align: center; font-size: 12px; color: var(--soft)">Modifiable à tout moment dans les Réglages.</p>
</div>
</main>
</div>

</div>
`,
  make: function () {
const THEMES = SM_THEMES, rootVars = SM_ROOTVARS, LANGS = SM_LANGS;
class Component extends DCLogic {
  renderVals() {
    const mode = this.props.mode || 'clair'; const s = this.state || {}; const step = s.step ?? (this.props.step ?? 0);
    const lang = s.lang ?? APP.get('lang'), place = s.place ?? APP.get('place'), rh = s.rh ?? (APP.get('rh') ?? 0);
    const card = (on) => 'min-height: 60px; border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 1px; font-family: inherit; color: var(--text); background: ' + (on ? 'var(--glass)' : 'transparent') + '; border: ' + (on ? '2px solid var(--accent-line)' : '1px solid var(--line2)');
    const t = SM_TR(); const R = [0, 1, 2, 3].map(i => ({ title: t['rh' + i], sub: t['rh' + i + 's'] }));
    return { remAt: s.remAt ?? (APP.get('remAt') || '07:30'), pickRemAt: (e) => { if (e.target.value) this.setState({ remAt: e.target.value }); },
      themeClass: 'th-' + mode, isParch: mode === 'parchemin', dir: 'ltr', rootStyle: rootVars(mode), stepNum: step + 1,
      dots: [0, 1, 2].map(i => 'height: 6px; border-radius: 3px; transition: width .3s; width: ' + (i === step ? 28 : 6) + 'px; background: ' + (i <= step ? 'var(--accent-line)' : 'var(--line2)')),
      s0: step === 0, s1: step === 1, s2: step === 2, notLast: step < 2, last: step === 2, canBack: step > 0,
      next: () => this.setState({ step: Math.min(2, step + 1) }), back: () => this.setState({ step: Math.max(0, step - 1) }),
      langs: LANGS.map(l => ({ ...l, on: l.id === lang, pick: () => this.setState({ lang: l.id }), style: card(l.id === lang) })),
      places: ['Israël', 'Diaspora'].map((n, i) => ({ name: n, on: i === place, pick: () => this.setState({ place: i }), style: card(i === place) })),
      fillCities: (el) => { const L = SM_CITY_LIST(); el.innerHTML = L.map(c => '<option value="' + c.id + '">' + c.name + '</option>').join(''); const on = L.find(c => c.on); if (on) el.value = on.id; }, pickCity: (e) => this.setState({ city: e.target.value }),
      rhythms: R.map((r, i) => ({ ...r, on: i === rh, pick: () => this.setState({ rh: i }),
        style: 'display: flex; align-items: center; gap: 12px; min-height: 64px; padding: 10px 16px; border-radius: 20px; font-family: inherit; color: var(--text); background: ' + (i === rh ? 'var(--glass)' : 'transparent') + '; border: ' + (i === rh ? '2px solid var(--accent-line)' : '1px solid var(--line)'),
        dot: 'flex-shrink: 0; width: 20px; height: 20px; border-radius: 50%; box-sizing: border-box; ' + (i === rh ? 'border: 6px solid var(--accent-line)' : 'border: 2px solid var(--line2)') })) };
  }
}

return Component;
  }
};
