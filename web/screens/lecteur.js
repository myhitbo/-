/* Écran « Lecture » — gabarit (tpl) puis logique (make). */
SCREENS.lecteur = {
  title: "Lecture",
  tpl: `

<div class="t {{themeClass}}" style="{{rootStyle}}; position: relative; width: 100%; height: 100vh; overflow: hidden; background: var(--bg); color: var(--text); font-family: Inter, 'Heebo', sans-serif">

<sc-if value="{{isParch}}" hint-placeholder-val="{{false}}"><svg aria-hidden="true" viewBox="0 0 400 900" preserveAspectRatio="none" style="position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none"><defs><filter id="pm" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.011" numOctaves="5" seed="5"></feTurbulence><feColorMatrix values="0 0 0 0 0.50  0 0 0 0 0.33  0 0 0 0 0.12  0 0 0 0.55 -0.12"></feColorMatrix></filter><filter id="pf" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.018 0.9" numOctaves="2" seed="8"></feTurbulence><feColorMatrix values="0 0 0 0 0.40  0 0 0 0 0.27  0 0 0 0 0.10  0 0 0 0.16 0"></feColorMatrix></filter><filter id="pg" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" stitchTiles="stitch"></feTurbulence><feColorMatrix values="0 0 0 0 0.35  0 0 0 0 0.24  0 0 0 0 0.10  0 0 0 0.15 0"></feColorMatrix></filter><filter id="pbl"><feGaussianBlur stdDeviation="2"></feGaussianBlur></filter><radialGradient id="pv" cx="50%" cy="45%" r="75%"><stop offset="0.55" stop-color="#6B4415" stop-opacity="0"></stop><stop offset="0.86" stop-color="#6B4415" stop-opacity="0.15"></stop><stop offset="1" stop-color="#4A2C0A" stop-opacity="0.38"></stop></radialGradient></defs><rect width="400" height="900" filter="url(#pm)"></rect><rect width="400" height="900" filter="url(#pf)"></rect><rect width="400" height="900" filter="url(#pg)"></rect><circle cx="249" cy="668" r="6.8" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="296" cy="830" r="2.2" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="377" cy="584" r="7.4" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="188" cy="222" r="5.3" fill="#8A5A1C" opacity="0.11" filter="url(#pbl)"></circle><circle cx="5" cy="195" r="3.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="306" cy="144" r="6.8" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="247" cy="114" r="2.0" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="84" cy="194" r="7.9" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="116" cy="865" r="5.2" fill="#8A5A1C" opacity="0.12" filter="url(#pbl)"></circle><circle cx="82" cy="847" r="6.1" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="357" cy="269" r="4.2" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="58" cy="59" r="3.8" fill="#8A5A1C" opacity="0.11" filter="url(#pbl)"></circle><circle cx="1" cy="610" r="4.0" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="327" cy="433" r="3.9" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="282" cy="51" r="7.9" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="300" cy="760" r="2.1" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="146" cy="521" r="2.1" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="72" cy="860" r="3.2" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="372" cy="848" r="4.1" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="210" cy="698" r="2.6" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="319" cy="774" r="2.2" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="36" cy="307" r="5.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="136" cy="832" r="5.3" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="127" cy="160" r="2.5" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="276" cy="897" r="3.0" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="395" cy="480" r="4.4" fill="#8A5A1C" opacity="0.08" filter="url(#pbl)"></circle><circle cx="238" cy="744" r="4.7" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="22" cy="824" r="2.2" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="335" cy="118" r="6.4" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="252" cy="709" r="2.6" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="60" cy="760" r="3.8" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="400" cy="767" r="7.9" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="195" cy="657" r="4.9" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="162" cy="132" r="4.3" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="384" cy="564" r="5.0" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="36" cy="245" r="6.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><rect width="400" height="900" fill="url(#pv)"></rect></svg></sc-if>
<div ref="{{setEl}}" onClick="{{toggleChrome}}" class="scroll" style="position: absolute; inset: 0; overflow-y: auto">
  <div style="max-width: 640px; margin: 0 auto; padding: 34vh 22px 72vh">
    <sc-for list="{{blocks}}" as="b" hint-placeholder-count="6">
      <div data-kind="{{b.kind}}" style="{{b.wrap}}">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px">
          <span class="cap">{{b.label}}</span>
          <span style="font-size: 12px; color: var(--soft)">{{b.ref}}</span>
        </div>
        <p dir="rtl" lang="he" style="{{b.textStyle}}">{{b.text}}</p>
      </div>
    </sc-for>
  </div>
</div>

<header style="{{chromeTop}}">
  <a href="V2-Accueil.dc.html" aria-label="Retour" class="glass" style="flex-shrink: 0; width: 44px; height: 44px; border-radius: 22px; display: flex; align-items: center; justify-content: center; color: var(--text)"><svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"></path></svg></a>
  <div style="flex: 1; min-width: 0; text-align: center">
    <p class="cap" style="margin: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{{G.alyaName}} · {{verse}}</p>
    <p class="serif" style="margin: 1px 0 0; font-size: 18px; font-weight: 500">{{G.readParasha}}</p>
  </div>
  <button onClick="{{togglePanel}}" aria-label="Affichage du texte" class="glass" style="flex-shrink: 0; width: 44px; height: 44px; border-radius: 22px; color: var(--text); font-family: Newsreader, serif; font-size: 18px; font-weight: 500; padding: 0">Aa</button>
</header>

<div style="{{chromeBottom}}">
  <div style="display: flex; justify-content: space-between; font-size: 12px; color: var(--soft); padding: 0 6px"><span>{{posLabel}}</span><span class="count">{{remaining}}</span></div>
  <div style="height: 3px; border-radius: 2px; background: var(--line); margin: 0 6px"><div style="{{progress}}"></div></div>
  <div style="display: flex; gap: 8px; align-items: center">
    <div style="flex: 1; min-width: 0; height: 56px; border-radius: 28px; background: var(--pill); color: var(--on-pill); display: flex; align-items: center; padding: 0 4px; box-shadow: var(--shadow)">
      <button onClick="{{slower}}" aria-label="Plus lent" style="flex-shrink: 0; width: 46px; height: 48px; border: none; background: none; color: inherit; font-size: 22px; padding: 0">−</button>
      <button onClick="{{toggle}}" aria-label="{{playLabel}}" style="flex: 1; min-width: 0; height: 48px; border: none; background: none; color: inherit; display: flex; align-items: center; justify-content: center; gap: 8px; font-family: Inter, sans-serif; font-size: 15px; font-weight: 600; padding: 0; white-space: nowrap">
        <sc-if value="{{paused}}" hint-placeholder-val="{{true}}"><svg aria-hidden="true" width="14" height="14" viewBox="0 0 24 24"><path d="M6 4l14 8-14 8z" fill="currentColor"></path></svg></sc-if>
        <sc-if value="{{playing}}" hint-placeholder-val="{{false}}"><svg aria-hidden="true" width="14" height="14" viewBox="0 0 24 24"><rect x="5" y="4" width="5" height="16" fill="currentColor"></rect><rect x="14" y="4" width="5" height="16" fill="currentColor"></rect></svg></sc-if>
        <span>Auto</span><span class="count" style="opacity: 0.7">{{speedLabel}}</span>
      </button>
      <button onClick="{{faster}}" aria-label="Plus rapide" style="flex-shrink: 0; width: 46px; height: 48px; border: none; background: none; color: inherit; font-size: 22px; padding: 0">+</button>
    </div>
    <button onClick="{{cycleTf}}" aria-label="Vitesse du Targoum : {{tfLabel}}" class="glass" style="flex-shrink: 0; height: 56px; padding: 0 14px; border-radius: 28px; color: var(--text); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 0; font-family: Inter, sans-serif">
      <span class="cap" style="font-size: 9px">Targoum</span><span style="font-size: 14px; font-weight: 700">{{tfLabel}}</span>
    </button>
  </div>
</div>

<sc-if value="{{panel}}" hint-placeholder-val="{{false}}">
  <div onClick="{{togglePanel}}" style="position: absolute; inset: 0; z-index: 7; background: rgba(0,0,0,0.25)"></div>
  <div style="position: absolute; left: 12px; right: 12px; bottom: 12px; z-index: 8; display: flex; justify-content: center">
  <div class="rise glass" role="dialog" aria-label="Affichage" style="width: 100%; max-width: 520px; border-radius: 28px; padding: 18px; display: flex; flex-direction: column; gap: 16px; box-shadow: var(--shadow)">
    <div style="display: flex; justify-content: space-between; align-items: center"><p class="serif" style="margin: 0; font-size: 22px; font-weight: 500">Affichage</p><button onClick="{{togglePanel}}" style="height: 40px; padding: 0 14px; border-radius: 20px; border: none; background: var(--pill); color: var(--on-pill); font-family: Inter, sans-serif; font-size: 13px; font-weight: 600">OK</button></div>
    <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px">
      <sc-for list="{{modeCards}}" as="m" hint-placeholder-count="3">
        <a href="{{m.href}}" aria-current="{{m.on}}" style="{{m.style}}"><span lang="he" style="font-family: 'Frank Ruhl Libre', serif; font-size: 22px">אָ</span><span style="font-size: 11px; font-weight: 600; max-width: 100%; overflow: hidden; text-overflow: ellipsis">{{m.name}}</span></a>
      </sc-for>
    </div>
    <div>
      <p class="cap" style="margin: 0 0 8px">Police</p>
      <div class="scroll" style="display: flex; gap: 6px; overflow-x: auto">
        <sc-for list="{{fontChips}}" as="f" hint-placeholder-count="5">
          <button onClick="{{f.pick}}" aria-pressed="{{f.on}}" style="{{f.style}}"><span lang="he" style="{{f.sample}}">אָב</span><span style="font-size: 11px">{{f.name}}</span></button>
        </sc-for>
      </div>
    </div>
    <div style="display: flex; align-items: center; gap: 10px">
      <span class="cap" style="flex: 1">Taille</span>
      <button onClick="{{smaller}}" aria-label="Texte plus petit" style="width: 44px; height: 44px; border-radius: 22px; border: 1px solid var(--line2); background: transparent; color: var(--text); font-size: 14px">A−</button>
      <span class="count" style="min-width: 28px; text-align: center; font-weight: 700">{{fs}}</span>
      <button onClick="{{bigger}}" aria-label="Texte plus grand" style="width: 44px; height: 44px; border-radius: 22px; border: 1px solid var(--line2); background: transparent; color: var(--text); font-size: 18px">A+</button>
    </div>
  </div>
  </div>
</sc-if>
<sc-if value="{{hint}}" hint-placeholder-val="{{false}}">
  <p class="cap" style="position: absolute; left: 0; right: 0; bottom: 18px; margin: 0; text-align: center; pointer-events: none; opacity: 0.8">Touchez le texte pour les commandes</p>
</sc-if>

<sc-if value="{{finished}}" hint-placeholder-val="{{false}}">
  <div style="position: absolute; inset: 0; z-index: 9; background: var(--bg); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 14px; padding: 32px; text-align: center">
    <svg aria-hidden="true" width="88" height="88" viewBox="0 0 30 30"><circle class="ring" cx="15" cy="15" r="12" fill="none" stroke="var(--accent-line)" stroke-width="1.6" transform="rotate(-90 15 15)"></circle><path class="tick" d="M9.5 15.5l4 4 7.5-8.5" fill="none" stroke="var(--accent-line)" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg>
    <p class="serif rise" style="margin: 0; font-size: 34px; font-weight: 500; animation-delay: .6s">{{G.alyaName}} terminé</p>
    <p class="rise" style="margin: 0; font-size: 15px; line-height: 1.5; color: var(--soft); animation-delay: .75s">{{G.afterText}}</p>
    <a class="rise" href="V2-Accueil.dc.html" style="margin-top: 8px; width: 100%; max-width: 360px; height: 56px; border-radius: 28px; background: var(--pill); color: var(--on-pill); display: flex; align-items: center; justify-content: center; font-weight: 600; text-decoration: none; animation-delay: .9s">Retour à l'accueil</a>
    <button class="rise" onClick="{{again}}" style="height: 44px; border: none; background: none; color: var(--soft); font-family: Inter, sans-serif; font-size: 14px; animation-delay: 1s">Relire depuis le début</button>
  </div>
</sc-if>
</div>
`,
  make: function () {
const THEMES = SM_THEMES, rootVars = SM_ROOTVARS;
const LINE = 0.34;
const HFONTS = [["frank", "Frank Ruhl", "'Frank Ruhl Libre', serif"], ["david", "David", "'David Libre', serif"], ["noto", "Noto", "'Noto Serif Hebrew', serif"], ["heebo", "Heebo", "Heebo, sans-serif"], ["rashi", "Rashi", "'Noto Rashi Hebrew', serif"]];
const BLOCKS = window.SM_BLOCKS() || [{"kind": "mikra", "n": 1, "heb": "יח", "ref": "29:18", "text": "וַיֶּאֱהַב יַעֲקֹב אֶת־רָחֵל וַיֹּאמֶר אֶעֱבָדְךָ שֶׁבַע שָׁנִים בְּרָחֵל בִּתְּךָ הַקְּטַנָּה׃"}, {"kind": "mikra", "n": 2, "heb": "יח", "ref": "29:18", "text": "וַיֶּאֱהַב יַעֲקֹב אֶת־רָחֵל וַיֹּאמֶר אֶעֱבָדְךָ שֶׁבַע שָׁנִים בְּרָחֵל בִּתְּךָ הַקְּטַנָּה׃"}, {"kind": "targum", "n": 3, "heb": "יח", "ref": "29:18", "text": "וּרְחֵים יַעֲקֹב יָת רָחֵל וַאֲמַר אֶפְלְחִנָּךְ שְׁבַע שְׁנִין בְּרָחֵל בְּרַתָּךְ זְעֵירְתָּא׃"}, {"kind": "mikra", "n": 1, "heb": "יט", "ref": "29:19", "text": "וַיֹּאמֶר לָבָן טוֹב תִּתִּי אֹתָהּ לָךְ מִתִּתִּי אֹתָהּ לְאִישׁ אַחֵר שְׁבָה עִמָּדִי׃"}, {"kind": "mikra", "n": 2, "heb": "יט", "ref": "29:19", "text": "וַיֹּאמֶר לָבָן טוֹב תִּתִּי אֹתָהּ לָךְ מִתִּתִּי אֹתָהּ לְאִישׁ אַחֵר שְׁבָה עִמָּדִי׃"}, {"kind": "targum", "n": 3, "heb": "יט", "ref": "29:19", "text": "וַאֲמַר לָבָן טָב דְּאֶתֵּן יָתַהּ לָךְ מִדְּאֶתֵּן יָתַהּ לִגְבַר אָחֳרָן תִּיב עִמִּי׃"}, {"kind": "mikra", "n": 1, "heb": "כ", "ref": "29:20", "text": "וַיַּעֲבֹד יַעֲקֹב בְּרָחֵל שֶׁבַע שָׁנִים וַיִּהְיוּ בְעֵינָיו כְּיָמִים אֲחָדִים בְּאַהֲבָתוֹ אֹתָהּ׃"}, {"kind": "mikra", "n": 2, "heb": "כ", "ref": "29:20", "text": "וַיַּעֲבֹד יַעֲקֹב בְּרָחֵל שֶׁבַע שָׁנִים וַיִּהְיוּ בְעֵינָיו כְּיָמִים אֲחָדִים בְּאַהֲבָתוֹ אֹתָהּ׃"}, {"kind": "targum", "n": 3, "heb": "כ", "ref": "29:20", "text": "וּפְלַח יַעֲקֹב בְּרָחֵל שְׁבַע שְׁנִין וַהֲווֹ בְּעֵינוֹהִי כְּיוֹמִין קַלִּילִין בִּדְרָחֵים יָתַהּ׃"}, {"kind": "mikra", "n": 1, "heb": "כא", "ref": "29:21", "text": "וַיֹּאמֶר יַעֲקֹב אֶל־לָבָן הָבָה אֶת־אִשְׁתִּי כִּי מָלְאוּ יָמָי וְאָבוֹאָה אֵלֶיהָ׃"}, {"kind": "mikra", "n": 2, "heb": "כא", "ref": "29:21", "text": "וַיֹּאמֶר יַעֲקֹב אֶל־לָבָן הָבָה אֶת־אִשְׁתִּי כִּי מָלְאוּ יָמָי וְאָבוֹאָה אֵלֶיהָ׃"}, {"kind": "targum", "n": 3, "heb": "כא", "ref": "29:21", "text": "וַאֲמַר יַעֲקֹב לְלָבָן הַב יָת אִתְּתִי אֲרֵי שְׁלִימוּ יוֹמֵי וְאֵיעוֹל לְוָתַהּ׃"}, {"kind": "mikra", "n": 1, "heb": "כב", "ref": "29:22", "text": "וַיֶּאֱסֹף לָבָן אֶת־כָּל־אַנְשֵׁי הַמָּקוֹם וַיַּעַשׂ מִשְׁתֶּה׃"}, {"kind": "mikra", "n": 2, "heb": "כב", "ref": "29:22", "text": "וַיֶּאֱסֹף לָבָן אֶת־כָּל־אַנְשֵׁי הַמָּקוֹם וַיַּעַשׂ מִשְׁתֶּה׃"}, {"kind": "targum", "n": 3, "heb": "כב", "ref": "29:22", "text": "וּכְנַשׁ לָבָן יָת כָּל אֱנָשֵׁי אַתְרָא וַעֲבַד מִשְׁתְּיָא׃"}];
const MODE = 'clair';
class Component extends DCLogic {
  componentDidMount() { this.timer = setInterval(() => this.tick(), 33); }
  componentWillUnmount() { clearInterval(this.timer); }
  st() { const s = this.state || {}; return { playing: s.playing ?? false, speed: s.speed ?? 3, tf: s.tf ?? 0.8, cur: s.cur ?? 0 }; }
  tick() {
    const el = this.el; if (!el) return;
    const s = this.st();
    const now = performance.now(); const dt = Math.min(0.1, (now - (this.last || now)) / 1000); this.last = now;
    const userScrolling = this.hold || now < (this.userUntil || 0);
    const blocks = el.querySelectorAll('[data-kind]');
    const line = el.scrollTop + el.clientHeight * LINE;
    let cur = 0; blocks.forEach((b, i) => { if (b.offsetTop <= line) cur = i; });
    if (cur !== s.cur) this.setState({ cur });
    if (!s.playing || userScrolling) { this.pos = el.scrollTop; return; }
    const kind = blocks[cur] ? blocks[cur].getAttribute('data-kind') : 'mikra';
    const base = [0, 9, 14, 20, 28, 38][s.speed];
    this.pos = (this.pos ?? el.scrollTop) + base * (kind === 'targum' ? s.tf : 1) * dt;
    el.scrollTop = this.pos; this.lastSet = el.scrollTop;
    if (el.scrollTop + el.clientHeight >= el.scrollHeight - 2) this.setState({ playing: false, finished: true }); if (window.SM_MARK) SM_MARK();
  }
  handlers() {
    if (this._h) return this._h;
    this._h = {
      setEl: (el) => {
        this.el = el; if (!el || el.__smBound) return; el.__smBound = true;
        const later = (ms) => { this.userUntil = performance.now() + ms; };
        el.addEventListener('touchstart', () => { this.hold = true; }, { passive: true });
        const up = () => { this.hold = false; later(700); };
        el.addEventListener('touchend', up, { passive: true }); el.addEventListener('touchcancel', up, { passive: true });
        el.addEventListener('wheel', () => later(700), { passive: true });
        el.addEventListener('pointerdown', (e) => { if (e.pointerType === 'mouse') later(700); }, { passive: true });
        el.addEventListener('scroll', () => { if (Math.abs(el.scrollTop - (this.lastSet ?? -99)) > 2) { later(500); this.pos = el.scrollTop; } }, { passive: true });
      },
      toggle: () => { const s = this.st(); if (this.el) this.pos = this.el.scrollTop; this.setState({ playing: !s.playing }); },
      slower: () => { const s = this.st(); this.setState({ speed: Math.max(1, s.speed - 1) }); },
      faster: () => { const s = this.st(); this.setState({ speed: Math.min(5, s.speed + 1) }); },
      onSpeed: (e) => { this.setState({ speed: Number(e.target.value) }); },
      restart: () => { if (this.el) { this.el.scrollTop = 0; this.pos = 0; } }
    };
    return this._h;
  }
  common() {
    const s = this.st(); const h = this.handlers();
    const labels = ['', '×0.5', '×0.75', '×1', '×1.3', '×1.7'];
    const tfs = [{ v: 1, l: 'Même vitesse' }, { v: 0.8, l: '−20 %' }, { v: 0.6, l: '−40 %' }];
    return { s, h, speedLabel: labels[s.speed], playLabel: s.playing ? 'Pause' : 'Lecture auto', tfs: tfs.map(t => ({ ...t, on: s.tf === t.v, pick: () => this.setState({ tf: t.v }) })) };
  }

  renderVals() {
    const c = this.common(); const s = c.s; const st = this.state || {};
    const mode = this.props.mode || MODE; const isText = mode === 'texte';
    const fs = st.fs ?? APP.get('fs'); const chrome = isText ? !!st.chrome : true;
    const fontId = st.font ?? APP.get('font'); const fontCss = (HFONTS.find(f => f[0] === fontId) || HFONTS[0])[2];
    if (!this._x) this._x = {
      togglePanel: (e) => { if (e && e.stopPropagation) e.stopPropagation(); this.setState({ panel: !(this.state && this.state.panel) }); },
      toggleChrome: () => { const z = this.state || {}; if ((this.props.mode || MODE) === 'texte') this.setState({ chrome: !z.chrome }); },
      smaller: () => { const z = this.state || {}; this.setState({ fs: Math.max(20, (z.fs ?? APP.get('fs')) - 2) }); },
      bigger: () => { const z = this.state || {}; this.setState({ fs: Math.min(40, (z.fs ?? APP.get('fs')) + 2) }); },
      cycleTf: () => { const z = this.c2 || 0.8; const order = [1, 0.8, 0.6]; const cur = (this.state && this.state.tf) ?? 0.8; this.setState({ tf: order[(order.indexOf(cur) + 1) % 3] }); },
      again: () => { if (this.el) { this.el.scrollTop = 0; this.pos = 0; } this.setState({ finished: false, playing: false }); }
    };
    const x = this._x;
    const blocks = BLOCKS.map((b, i) => {
      const isT = b.kind === 'targum'; const on = i === s.cur;
      return { ...b, label: b.label ? b.label : isT ? 'Targoum' : (b.n === 1 ? '1ʳᵉ lecture' : '2ᵉ lecture'),
        wrap: 'padding: 14px 16px; margin: 0 -16px 8px; border-radius: 18px; transition: background-color .35s; background: ' + (on && !isText ? 'var(--hl)' : 'transparent') + (on && isText ? '; box-shadow: inset -3px 0 0 var(--accent-line)' : ''),
        textStyle: 'margin: 0; font-family: ' + fontCss + '; font-weight: ' + (mode === 'sombre' ? 500 : 400) + '; font-size: ' + (isT ? fs - 3 : fs) + 'px; line-height: ' + (isText ? 2.05 : 1.9) + '; color: ' + (isT ? 'var(--soft)' : 'var(--text)') + '; text-wrap: pretty' };
    });
    const fade = 'transition: opacity .35s ease, transform .35s ease; ' + (chrome ? 'opacity: 1;' : 'opacity: 0; pointer-events: none;');
    const tfLabel = s.tf === 1 ? '=' : s.tf === 0.8 ? '−20 %' : '−40 %';
    const remainingMin = Math.max(1, Math.round((BLOCKS.length - s.cur) / 3 * 0.4));
    const hrefs = { clair: '#mode=clair', sombre: '#mode=sombre', texte: '#mode=texte', parchemin: '#mode=parchemin' };
    return { themeClass: 'th-' + mode, isParch: mode === 'parchemin', rootStyle: rootVars(mode), blocks, setEl: c.h.setEl, toggle: (e) => { if (e && e.stopPropagation) e.stopPropagation(); c.h.toggle(); }, slower: c.h.slower, faster: c.h.faster,
      speedLabel: c.speedLabel, playing: s.playing, paused: !s.playing, playLabel: c.playLabel, cycleTf: x.cycleTf, tfLabel,
      verse: BLOCKS[s.cur] ? BLOCKS[s.cur].ref : '', posLabel: 'Verset ' + Math.max(1, BLOCKS.slice(0, s.cur + 1).filter(b => b.n === 1).length) + ' sur ' + BLOCKS.filter(b => b.n === 1).length, remaining: remainingMin + ' min restantes',
      progress: 'height: 100%; border-radius: 2px; width: ' + Math.round((s.cur + 1) / BLOCKS.length * 100) + '%; background: var(--accent-line); transition: width .4s',
      chromeTop: 'position: absolute; top: 0; left: 0; right: 0; z-index: 4; padding: 12px 14px 28px; display: flex; align-items: center; gap: 10px; background: linear-gradient(var(--bg) 62%, transparent); ' + fade + (chrome ? '' : ' transform: translateY(-12px);'),
      chromeBottom: 'position: absolute; left: 50%; bottom: 0; transform: translateX(-50%)' + (chrome ? '' : ' translateY(16px)') + '; width: 100%; max-width: 560px; z-index: 4; padding: 26px 14px 16px; display: flex; flex-direction: column; gap: 8px; background: linear-gradient(transparent, var(--bg) 30%); ' + fade,
      panel: !!st.panel, togglePanel: x.togglePanel, toggleChrome: x.toggleChrome, smaller: x.smaller, bigger: x.bigger, fs,
      modeCards: ['clair', 'sombre', 'texte', 'parchemin'].map(m => { const t = THEMES[m]; const on = m === mode; return { name: m === 'clair' ? 'Clair' : m === 'sombre' ? 'Sombre' : m === 'texte' ? 'Texte' : 'Parchemin', on, href: hrefs[m], style: 'height: 72px; min-width: 0; border-radius: 16px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; text-decoration: none; background: ' + t['--bg'] + '; color: ' + t['--text'] + '; border: ' + (on ? '2px solid var(--accent-line)' : '1px solid ' + t['--line2']) }; }),
      fontChips: HFONTS.map(f => ({ name: f[1], on: f[0] === fontId, pick: () => this.setState({ font: f[0] }), sample: 'font-family: ' + f[2] + '; font-size: 20px; line-height: 1.3', style: 'flex-shrink: 0; width: 64px; height: 60px; border-radius: 16px; padding: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; color: var(--text); font-family: Inter, sans-serif; background: ' + (f[0] === fontId ? 'var(--hl)' : 'transparent') + '; border: ' + (f[0] === fontId ? '2px solid var(--accent-line)' : '1px solid var(--line2)') })),
      hint: isText && !chrome && !st.panel, finished: !!st.finished, again: x.again };
  }
}

return Component;
  }
};
