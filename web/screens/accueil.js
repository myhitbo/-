/* Écran « Accueil » — gabarit (tpl) puis logique (make). */
SCREENS.accueil = {
  title: "Accueil",
  tpl: `

<div class="t {{themeClass}}" style="{{rootStyle}}; position: relative; width: 100%; height: 100vh; overflow: hidden; background: var(--bg); color: var(--text); font-family: Inter, 'Heebo', sans-serif">
<sc-if value="{{isParch}}" hint-placeholder-val="{{false}}"><svg aria-hidden="true" viewBox="0 0 400 900" preserveAspectRatio="none" style="position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none"><defs><filter id="pm" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.011" numOctaves="5" seed="5"></feTurbulence><feColorMatrix values="0 0 0 0 0.50  0 0 0 0 0.33  0 0 0 0 0.12  0 0 0 0.55 -0.12"></feColorMatrix></filter><filter id="pf" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.018 0.9" numOctaves="2" seed="8"></feTurbulence><feColorMatrix values="0 0 0 0 0.40  0 0 0 0 0.27  0 0 0 0 0.10  0 0 0 0.16 0"></feColorMatrix></filter><filter id="pg" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" stitchTiles="stitch"></feTurbulence><feColorMatrix values="0 0 0 0 0.35  0 0 0 0 0.24  0 0 0 0 0.10  0 0 0 0.15 0"></feColorMatrix></filter><filter id="pbl"><feGaussianBlur stdDeviation="2"></feGaussianBlur></filter><radialGradient id="pv" cx="50%" cy="45%" r="75%"><stop offset="0.55" stop-color="#6B4415" stop-opacity="0"></stop><stop offset="0.86" stop-color="#6B4415" stop-opacity="0.15"></stop><stop offset="1" stop-color="#4A2C0A" stop-opacity="0.38"></stop></radialGradient></defs><rect width="400" height="900" filter="url(#pm)"></rect><rect width="400" height="900" filter="url(#pf)"></rect><rect width="400" height="900" filter="url(#pg)"></rect><circle cx="249" cy="668" r="6.8" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="296" cy="830" r="2.2" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="377" cy="584" r="7.4" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="188" cy="222" r="5.3" fill="#8A5A1C" opacity="0.11" filter="url(#pbl)"></circle><circle cx="5" cy="195" r="3.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="306" cy="144" r="6.8" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="247" cy="114" r="2.0" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="84" cy="194" r="7.9" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="116" cy="865" r="5.2" fill="#8A5A1C" opacity="0.12" filter="url(#pbl)"></circle><circle cx="82" cy="847" r="6.1" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="357" cy="269" r="4.2" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="58" cy="59" r="3.8" fill="#8A5A1C" opacity="0.11" filter="url(#pbl)"></circle><circle cx="1" cy="610" r="4.0" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="327" cy="433" r="3.9" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="282" cy="51" r="7.9" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="300" cy="760" r="2.1" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="146" cy="521" r="2.1" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="72" cy="860" r="3.2" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="372" cy="848" r="4.1" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="210" cy="698" r="2.6" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="319" cy="774" r="2.2" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="36" cy="307" r="5.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="136" cy="832" r="5.3" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="127" cy="160" r="2.5" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="276" cy="897" r="3.0" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="395" cy="480" r="4.4" fill="#8A5A1C" opacity="0.08" filter="url(#pbl)"></circle><circle cx="238" cy="744" r="4.7" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="22" cy="824" r="2.2" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="335" cy="118" r="6.4" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="252" cy="709" r="2.6" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="60" cy="760" r="3.8" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="400" cy="767" r="7.9" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="195" cy="657" r="4.9" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="162" cy="132" r="4.3" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="384" cy="564" r="5.0" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="36" cy="245" r="6.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><rect width="400" height="900" fill="url(#pv)"></rect></svg></sc-if><div aria-hidden="true" style="position: absolute; top: -120px; right: -90px; width: 340px; height: 340px; border-radius: 50%; background: radial-gradient(circle at 40% 40%, var(--blob1), transparent 68%); opacity: var(--blobop); filter: blur(30px); pointer-events: none"></div>
<div aria-hidden="true" style="position: absolute; top: -60px; left: -120px; width: 300px; height: 260px; border-radius: 50%; background: radial-gradient(circle, var(--blob2), transparent 70%); opacity: var(--blobop); filter: blur(40px); pointer-events: none"></div>
<div class="scroll" style="position: absolute; inset: 0; overflow-y: auto">
<main style="position: relative; max-width: 560px; margin: 0 auto; padding: 22px 20px 120px; display: flex; flex-direction: column; gap: 26px">

  <header style="display: flex; justify-content: space-between; align-items: center">
    <p style="margin: 0; font-size: 13px; color: var(--soft)">{{G.date}}</p>
    <a href="V2-Imprimer.dc.html" aria-label="{{t.printTitle}}" class="glass" style="height: 40px; padding: 0 14px; border-radius: 20px; display: flex; align-items: center; gap: 8px; color: var(--text); text-decoration: none; font-size: 13px; font-weight: 600"><svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 9V3h10v6"></path><rect x="4" y="9" width="16" height="8" rx="2"></rect><path d="M7 14h10v7H7z"></path></svg><span>{{t.shabbat}}</span></a>
  </header>

  <section style="display: flex; flex-direction: column; gap: 6px">
    <p class="cap" style="margin: 0">{{t.parashaOfWeek}}</p>
    <div style="display: flex; align-items: baseline; justify-content: space-between; gap: 12px; flex-wrap: wrap">
      <h1 class="serif foil" style="margin: 0; font-size: clamp(40px, 13vw, 60px); font-weight: 500; line-height: 0.95; letter-spacing: -0.02em">{{G.parasha}}</h1>
      <p lang="he" dir="rtl" class="foil" style="margin: 0; font-family: 'Frank Ruhl Libre', serif; font-size: clamp(26px, 8vw, 36px); color: var(--soft)">{{G.parashaHe}}</p>
    </div>
    <p style="margin: 0; font-size: 14px; color: var(--soft)">{{G.parashaRef}}</p>
  </section>

  <sc-if value="{{G.hasPrev}}" hint-placeholder-val="{{false}}">
    <section aria-label="{{t.catchUp}}" style="border-radius: 22px; padding: 14px 16px; border: 2px solid var(--accent-line); display: flex; align-items: center; gap: 12px; flex-wrap: wrap">
      <div style="flex: 1; min-width: 160px">
        <p class="cap" style="margin: 0">{{G.prev.title}}</p>
        <p class="serif" style="margin: 2px 0 0; font-size: 24px; font-weight: 500; line-height: 1.1">{{G.prev.name}}</p>
        <p style="margin: 2px 0 0; font-size: 13px; color: var(--soft)">{{G.prev.line}}</p>
      </div>
      <a href="{{G.prev.href}}" style="flex-shrink: 0; height: 48px; padding: 0 20px; border-radius: 24px; background: var(--pill); color: var(--on-pill); display: flex; align-items: center; font-size: 15px; font-weight: 600; text-decoration: none">{{t.continue}}</a>
    </section>
  </sc-if>
  <section aria-label="{{t.weekProgress}}" style="display: flex; gap: 6px; align-items: stretch">
    <div role="list" style="flex-shrink: 0; width: 70px; display: flex; flex-direction: column">
      <sc-for list="{{scale}}" as="r" hint-placeholder-count="7">
        <button role="listitem" onClick="{{r.pick}}" aria-label="{{r.name}}" style="{{r.style}}"><span>{{r.name}}</span></button>
      </sc-for>
    </div>
    <svg aria-hidden="true" class="flip" width="58" height="294" viewBox="0 0 58 294" style="flex-shrink: 0; overflow: hidden">
      <defs>
        <clipPath id="below"><rect x="-10" y="0" width="80" height="294"></rect></clipPath>
        <clipPath id="above"><rect x="-10" y="-294" width="80" height="294"></rect></clipPath>
      </defs>
      <sc-for list="{{ticks}}" as="k" hint-placeholder-count="29"><line x1="{{k.x1}}" y1="{{k.y}}" x2="14" y2="{{k.y}}" stroke="var(--line2)" stroke-width="1"></line></sc-for>
      <g class="wave" style="{{waveStyle}}">
        <path d="M20 -400 L20 -50 C20 -24 46 -24 46 0 C46 24 20 24 20 50 L20 400" fill="none" stroke="var(--line2)" stroke-width="2" clip-path="url(#above)"></path>
        <path d="M20 -400 L20 -50 C20 -24 46 -24 46 0 C46 24 20 24 20 50 L20 400" fill="none" stroke="var(--accent-line)" stroke-width="3" clip-path="url(#below)"></path>
        <circle cx="46" cy="0" r="13" fill="var(--text)"></circle>
        <path d="M41.5 -2 l4.5 -4.5 l4.5 4.5 M41.5 2 l4.5 4.5 l4.5 -4.5" fill="none" stroke="var(--bg)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"></path>
      </g>
    </svg>
    <div style="flex: 1; min-width: 0; padding-left: 8px; display: flex; flex-direction: column; justify-content: center; gap: 16px">
      <div>
        <p class="cap" style="margin: 0">{{sel.day}} · {{sel.status}}</p>
        <p class="serif" style="margin: 4px 0 0; font-size: clamp(30px, 10vw, 46px); font-weight: 500; line-height: 1; letter-spacing: -0.02em">{{sel.name}}</p>
        <p lang="he" dir="rtl" style="margin: 4px 0 0; text-align: left; font-family: 'Frank Ruhl Libre', serif; font-size: 20px; color: var(--soft)">{{sel.heb}}</p>
      </div>
      <div style="display: flex; gap: 18px; flex-wrap: wrap">
        <div><p class="cap" style="margin: 0">{{t.verses}}</p><p style="margin: 3px 0 0; font-size: 16px; font-weight: 600">{{sel.verses}}</p></div>
        <div><p class="cap" style="margin: 0">{{t.duration}}</p><p style="margin: 3px 0 0; font-size: 16px; font-weight: 600">{{sel.min}} {{t.min}}</p></div>
      </div>
      <div>
        <p class="cap" style="margin: 0">{{t.remaining}}</p>
        <p class="serif count" style="margin: 2px 0 0; font-size: 34px; font-weight: 500; line-height: 1">{{minLeft}}<span style="font-size: 16px; font-family: Inter, sans-serif; font-weight: 600; margin-inline-start: 4px">{{t.min}}</span></p>
      </div>
    </div>
  </section>

  <section aria-label="{{t.deadline}}" class="glass" style="margin-top: -8px; border-radius: 22px; padding: 14px 16px; display: flex; flex-direction: column; gap: 4px">
    <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 4px 12px; flex-wrap: wrap">
      <p style="margin: 0; font-size: 15px; font-weight: 600">{{G.goal}}</p>
      <p class="count" style="margin: 0; font-size: 15px; font-weight: 700; color: var(--accent)">{{G.countdown}}</p>
    </div>
    <p style="margin: 0; font-size: 13px; line-height: 1.45; color: var(--soft)">{{G.candleLine}}</p>
    <sc-if value="{{G.hasLate}}" hint-placeholder-val="{{false}}"><p style="margin: 0; font-size: 13px; font-weight: 600; color: var(--accent)">{{G.lateLine}}</p></sc-if>
    <sc-if value="{{G.friday}}" hint-placeholder-val="{{false}}">
      <a href="V2-Imprimer.dc.html" style="margin-top: 6px; min-height: 44px; display: flex; align-items: center; gap: 8px; color: var(--accent); font-size: 14px; font-weight: 600; text-decoration: none"><svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9V3h12v6"></path><rect x="3" y="9" width="18" height="8" rx="2"></rect><path d="M7 14h10v7H7z"></path></svg><span>{{t.printRest}}</span></a>
    </sc-if>
  </section>

  <sc-if value="{{notFinished}}" hint-placeholder-val="{{true}}">
    <div style="display: flex; gap: 10px">
      <a href="{{readHref}}" style="flex: 1; min-width: 0; height: 56px; border-radius: 28px; background: var(--pill); color: var(--on-pill); display: flex; align-items: center; justify-content: center; gap: 10px; text-decoration: none; font-size: 16px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; padding: 0 18px"><svg aria-hidden="true" width="14" height="14" viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z" fill="currentColor"></path></svg>{{readLabel}}</a>
      <button onClick="{{markRead}}" aria-label="{{markLabel}}" class="glass" style="flex-shrink: 0; height: 56px; padding: 0 18px; border-radius: 28px; color: var(--text); display: flex; align-items: center; gap: 8px; font-family: Inter, sans-serif; font-size: 15px; font-weight: 600"><svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5 9-10"></path></svg><span>{{t.stRead}}</span></button>
    </div>
  </sc-if>
  <sc-if value="{{finished}}" hint-placeholder-val="{{false}}">
    <div class="rise" style="text-align: center; display: flex; flex-direction: column; gap: 8px; align-items: center">
      <p class="serif" style="margin: 0; font-size: 30px; font-weight: 500">{{t.doneAll}}</p>
      <p style="margin: 0; color: var(--soft); font-size: 14px">{{G.allReadLine}}</p>
    </div>
  </sc-if>

  <sc-if value="{{G.hasCarnet}}" hint-placeholder-val="{{false}}">
    <section aria-label="{{t.notebook}}" style="display: flex; flex-direction: column">
      <h2 class="cap" style="margin: 0 0 4px">{{G.stLabel}}</h2>
      <sc-for list="{{G.carnet}}" as="k" hint-placeholder-count="2">
        <a href="{{k.href}}" style="min-height: 52px; display: flex; align-items: center; justify-content: space-between; gap: 12px; border-top: 1px solid var(--line); color: var(--text); text-decoration: none">
          <span class="serif" style="font-size: 20px; font-weight: 500">{{k.name}}</span><span style="font-size: 13px; color: var(--soft)">{{k.label}}</span>
        </a>
      </sc-for>
    </section>
  </sc-if>
  <section style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">
    <div class="glass" style="border-radius: 22px; padding: 16px; display: flex; flex-direction: column; gap: 6px">
      <p class="cap" style="margin: 0; display: flex; align-items: center; gap: 6px">{{t.streak}}</p>
      <p class="serif" style="margin: 0; font-size: 32px; font-weight: 500; line-height: 1">{{G.streak}} <span style="font-family: Inter, sans-serif; font-size: 13px; font-weight: 500; color: var(--soft)">{{t.weeks}}</span></p>
    </div>
    <a href="V2-Annee.dc.html" class="glass" style="border-radius: 22px; padding: 16px; display: flex; flex-direction: column; gap: 6px; color: var(--text); text-decoration: none">
      <p class="cap" style="margin: 0">{{t.thisYear}}</p>
      <p class="serif" style="margin: 0; font-size: 32px; font-weight: 500; line-height: 1">{{G.yearDone}}<span style="font-size: 20px; color: var(--soft)">/54</span> <span style="font-family: Inter, sans-serif; font-size: 13px; font-weight: 500; color: var(--soft)">{{t.finishedPl}}</span></p>
    </a>
  </section>

  <section aria-label="{{t.nextParashiyot}}" style="display: flex; flex-direction: column; gap: 4px">
    <h2 class="cap" style="margin: 0 0 6px">{{t.nextParashiyot}}</h2>
    <sc-for list="{{next}}" as="w" hint-placeholder-count="3">
      <a href="{{w.href}}" aria-disabled="{{w.locked}}" style="display: flex; align-items: center; gap: 12px; min-height: 64px; padding: 8px 0; border-top: 1px solid var(--line); color: var(--text); text-decoration: none">
        <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px">
          <span style="display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap"><span class="serif" style="font-size: 22px; font-weight: 500; line-height: 1.1">{{w.name}}</span><span lang="he" dir="rtl" style="font-family: 'Frank Ruhl Libre', serif; font-size: 17px; color: var(--soft)">{{w.heb}}</span></span>
          <span style="font-size: 12px; color: var(--soft)">{{w.when}}</span><span style="font-size: 12px; color: var(--soft)">{{w.ref}}</span>
        </span>
        <sc-if value="{{w.canRead}}" hint-placeholder-val="{{true}}"><span style="flex-shrink: 0; font-size: 13px; font-weight: 600; color: var(--accent)">{{t.readAhead}}</span></sc-if>
      </a>
    </sc-for>
  </section>
</main>
</div>
${SM_NAV('accueil')}
<sc-if value="{{showToast}}" hint-placeholder-val="{{false}}">
  <div style="position: absolute; left: 16px; right: 16px; bottom: 82px; display: flex; justify-content: center; z-index: 6; pointer-events: none">
    <div class="toast glass" role="status" style="width: 100%; max-width: 420px; padding: 14px 18px; border-radius: 22px; box-shadow: var(--shadow); display: flex; justify-content: space-between; gap: 10px; font-size: 14px; font-weight: 600">
      <span>{{toastLine}}</span><span class="count" style="flex-shrink: 0; color: var(--soft)">−{{toastMin}} {{t.min}}</span>
    </div>
  </div>
</sc-if>
</div>
`,
  make: function () {
const THEMES = SM_THEMES, rootVars = SM_ROOTVARS;
const ALYOT = (window.SM_ALYOT && SM_ALYOT()) || [{"name": "Rishon", "heb": "רִאשׁוֹן", "day": "Dimanche", "verses": "28:10 – 22", "min": 5}, {"name": "Sheni", "heb": "שֵׁנִי", "day": "Lundi", "verses": "29:1 – 17", "min": 6}, {"name": "Shlishi", "heb": "שְׁלִישִׁי", "day": "Mardi", "verses": "29:18 – 30:13", "min": 12}, {"name": "Revi'i", "heb": "רְבִיעִי", "day": "Mercredi", "verses": "30:14 – 27", "min": 5}, {"name": "Hamishi", "heb": "חֲמִישִׁי", "day": "Jeudi", "verses": "30:28 – 31:16", "min": 12}, {"name": "Shishi", "heb": "שִׁשִּׁי", "day": "Vendredi", "verses": "31:17 – 42", "min": 10}, {"name": "Shvi'i", "heb": "שְׁבִיעִי", "day": "Shabbat", "verses": "31:43 – 32:3", "min": 6}];
const ROWH = 42;
const READER = 'V2-Lecteur.dc.html';

class Component extends DCLogic {
  componentWillUnmount() { clearInterval(this.cnt); clearTimeout(this.tt); }
  st() { const s = this.state || {}; const total = (d) => ALYOT.slice(d).reduce((a, x) => a + x.min, 0); const done = s.done ?? (APP.get('done') ?? 0); return { mode: this.props.mode || 'clair', done, sel: Math.min(6, s.sel ?? done), shown: s.shown ?? total(done), toast: !!s.toast, total, toastName: s.toastName, toastMin: s.toastMin }; }
  markRead() {
    const s = this.st(); if (s.done >= 7) return;
    const target = s.total(s.done + 1), from = s.shown;
    this.setState({ done: s.done + 1, sel: Math.min(6, s.done + 1), toast: true, toastName: SM_ALYA(s.done), toastMin: ALYOT[s.done].min });
    clearInterval(this.cnt); const t0 = performance.now();
    this.cnt = setInterval(() => { const p = Math.min(1, (performance.now() - t0) / 700); this.setState({ shown: Math.round(from + (target - from) * p) }); if (p >= 1) clearInterval(this.cnt); }, 30);
    clearTimeout(this.tt); this.tt = setTimeout(() => this.setState({ toast: false }), 2400);
  }
  renderVals() {
    const s = this.st();
    if (!this._x) this._x = { mr: () => this.markRead(), rs: () => this.setState({ done: 2, sel: 2, shown: undefined, toast: false }) };
    const H = ROWH * 7;
    const yOf = (i) => H - (i + 0.5) * ROWH;
    const scale = ALYOT.map((a, i) => ({ ...a, i })).reverse().map(a => ({ name: SM_ALYA(a.i), pick: () => this.setState({ sel: a.i }),
      style: 'height: ' + ROWH + 'px; border: none; background: none; padding: 0 4px 0 0; display: flex; align-items: center; justify-content: flex-end; text-align: right; font-family: Inter, sans-serif; font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; cursor: pointer; ' +
        (a.i === s.sel ? 'color: var(--text); font-weight: 800; font-size: 12px;' : a.i < s.done ? 'color: var(--accent); font-weight: 600;' : 'color: var(--soft); font-weight: 500;') }));
    const ticks = []; for (let k = 0; k <= 28; k++) { const y = k * (H / 28); ticks.push({ y: y.toFixed(1), x1: k % 4 === 2 ? 4 : 9 }); }
    const a = { ...ALYOT[s.sel], name: SM_ALYA(s.sel), day: s.sel === 6 ? SM_TR().shabbat : SM_WEEKDAY(s.sel) };
    a.day = a.day.charAt(0).toUpperCase() + a.day.slice(1); a.heb = SM_HEB(a.name, a.heb);
    /* Prochaine séance selon le rythme choisi : une alya, plusieurs, ou toute la paracha */
    const t = SM_TR(), F = SM_FMT, plan = window.SM_PLAN ? SM_PLAN() : { rh: 0, from: Math.min(s.done, 6), to: Math.min(s.done, 6), today: new Date().getDay() };
    const from = Math.min(s.done, 6), to = Math.max(from, plan.to);
    const status = s.sel < s.done ? t.stRead : (s.sel >= from && s.sel <= to) ? (plan.rh === 0 && s.sel === plan.today ? t.stToday : t.stToRead) : t.stLater;
    const today = ALYOT[from];
    const readLabel = from === to ? F(t.readOne, { name: SM_ALYA(from) }) : (from === 0 && to === 6) ? t.readAll : (to === 6 && plan.rh === 1) ? t.readRest : F(t.readRange, { a: SM_ALYA(from), b: SM_ALYA(to) });
    return { next: window.SM_NEXT ? SM_NEXT().map(w => ({ ...w, locked: !w.canRead })) : [], themeClass: 'th-' + s.mode, isParch: s.mode === 'parchemin', rootStyle: rootVars(s.mode), scale, ticks, waveStyle: 'transform: translateY(' + yOf(s.sel) + 'px)',
      sel: { ...a, status }, today, minLeft: s.shown, markRead: this._x.mr, reset: this._x.rs, readLabel, markLabel: F(t.markRead, { name: SM_ALYA(from) }), toastLine: F(t.toast, { name: s.toastName || '' }), readHref: 'V2-Lecteur.dc.html?par=0&alya=' + from + '&to=' + to,
      finished: s.done >= 7, notFinished: s.done < 7, showToast: s.toast, toastName: s.toastName || '', toastMin: s.toastMin || 0 };
  }
}

return Component;
  }
};
