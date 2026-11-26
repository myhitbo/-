/* Shnayim Mikra — les écrans ajoutés à ceux des maquettes (screens.js) : le recueil des halakhot.
   Même moteur d'écrans (runtime.js) : un gabarit, une classe, les quatre apparences. */
(function () {
const THEMES = {"clair": {"--bg": "#F6F2EC", "--bg2": "#FFFFFF", "--text": "#1C1A17", "--soft": "#6B645A", "--line": "#E2D9CB", "--line2": "#CFC4B3", "--accent": "#A24E14", "--accent-line": "#E07B39", "--pill": "#1C1A17", "--on-pill": "#F6F2EC", "--hl": "#FBE4D2", "--glass": "rgba(255,255,255,0.66)", "--glass-b": "rgba(255,255,255,0.9)", "--blob1": "#FFC6A0", "--blob2": "#FFE6AE", "--blobop": "0.75", "--shadow": "0 10px 30px -12px rgba(60,40,20,0.25)"}, "sombre": {"--bg": "#1A1916", "--bg2": "#24221E", "--text": "#EDE7DB", "--soft": "#A59D90", "--line": "rgba(237,231,219,0.12)", "--line2": "rgba(237,231,219,0.28)", "--accent": "#E3B577", "--accent-line": "#D9A35B", "--pill": "#EDE7DB", "--on-pill": "#1A1916", "--hl": "rgba(217,163,91,0.15)", "--glass": "rgba(44,41,36,0.72)", "--glass-b": "rgba(255,255,255,0.08)", "--blob1": "#6A4E2A", "--blob2": "#3F3524", "--blobop": "0.55", "--shadow": "0 10px 30px -10px rgba(0,0,0,0.6)"}, "texte": {"--bg": "#F1E7D0", "--bg2": "#F7EFDC", "--text": "#2E241A", "--soft": "#67533D", "--line": "#DCCBA6", "--line2": "#C9B48A", "--accent": "#7A4B12", "--accent-line": "#A86A2A", "--pill": "#2E241A", "--on-pill": "#F1E7D0", "--hl": "#E8D8B4", "--glass": "rgba(247,239,220,0.86)", "--glass-b": "#E3D3AE", "--blob1": "transparent", "--blob2": "transparent", "--blobop": "0", "--shadow": "0 10px 30px -14px rgba(60,40,10,0.3)"}, "parchemin": {"--bg": "#EFE2C4", "--bg2": "#F7EEDA", "--text": "#2A2119", "--soft": "#5E4E3C", "--line": "#D3BE95", "--line2": "#BFA273", "--accent": "#7A520C", "--accent-line": "#A67B26", "--pill": "#2A2119", "--on-pill": "#F1DFA9", "--hl": "rgba(214,170,80,0.22)", "--glass": "rgba(250,243,226,0.62)", "--glass-b": "#CDB27E", "--blob1": "transparent", "--blob2": "transparent", "--blobop": "0", "--shadow": "0 10px 26px -14px rgba(70,45,10,0.45)"}};
function rootVars(mode) { const t = THEMES[mode] || THEMES.clair; return Object.keys(t).map(k => k + ': ' + t[k]).join('; '); }

/* Le texte d'une halakha ne porte que <b>, <small> et <br> (test/chnayim-mikra.test.mjs) : rendu sans innerHTML. */
function riche(el, html) {
  el.textContent = ''; let cur = el;
  String(html || '').split(/(<\/?(?:b|small)>|<br>)/).forEach(tok => {
    if (!tok) return;
    if (tok === '<br>') { el.appendChild(document.createElement('br')); cur = el; }
    else if (tok === '<b>' || tok === '<small>') { const n = document.createElement(tok === '<b>' ? 'b' : 'small'); if (tok === '<small>') n.style.cssText = 'font-size: 0.82em; color: var(--soft)'; cur.appendChild(n); cur = n; }
    else if (tok === '</b>' || tok === '</small>') { cur = cur.parentNode && cur !== el ? cur.parentNode : el; }
    else cur.appendChild(document.createTextNode(tok));
  });
}

/* ---------- Halakhot de Chnayim mikra ---------- */
const T = {
  fr: { back: 'Retour', cap: 'Halakhot', title: 'Les lois de Chnayim mikra', draft: 'Chaque citation a été relue à sa source. Le texte de chaque halakha a ensuite été relu contre ses sources par une seconde relecture automatique (26/11/2026). Il n’a pas été relu par un rav.',
    rav: 'Ce recueil ne tranche rien : chaque question pratique se pose à un rav.', filter: 'Rite', mine: 'Mon rite', all: 'Tous les rites', n: 'halakhot', src: 'Sources en hébreu', hide: 'Masquer les sources', wait: 'Chargement…',
    rites: { edot: 'Edot hamizra’h', sefard: 'Sfard', ashkenaz: 'Ashkenaz' } },
  en: { back: 'Back', cap: 'Halacha', title: 'The laws of Shnayim mikra', draft: 'Every quotation was re-read at its source. The text of each law was then checked against its sources by a second automatic review (26 Nov 2026). It has not been reviewed by a rabbi.',
    rav: 'This collection decides nothing: for a practical question, ask a rabbi.', filter: 'Rite', mine: 'My rite', all: 'All rites', n: 'laws', src: 'Hebrew sources', hide: 'Hide sources', wait: 'Loading…',
    rites: { edot: 'Edot HaMizrach', sefard: 'Sfard', ashkenaz: 'Ashkenaz' } },
  he: { back: 'חזרה', cap: 'הלכה', title: 'הלכות שנים מקרא ואחד תרגום', draft: 'כל ציטוט נבדק מול מקורו. לאחר מכן נבדק נוסח כל הלכה מול מקורותיה בבדיקה ממוחשבת שנייה (ט״ז בכסלו תשפ״ז). הנוסח לא עבר הגהת רב.',
    rav: 'אין כאן הכרעה: כל שאלה למעשה תישאל לרב.', filter: 'נוסח', mine: 'הנוסח שלי', all: 'כל העדות', n: 'הלכות', src: 'המקורות', hide: 'הסתר מקורות', wait: 'טוען…',
    rites: { edot: 'עדות המזרח', sefard: 'ספרד', ashkenaz: 'אשכנז' } }
};
/* Langue du texte : français (aussi pour le tunisien et le marocain), anglais (aussi pour l'espagnol), ou l'hébreu seul */
const LANGUE = { fr: 'fr', tn: 'fr', ma: 'fr', en: 'en', es: 'en', he: 'he' };

SCREENS["halakhot"] = { title: "Halakhot", tpl: `
<div class="t {{themeClass}}" style="{{rootStyle}}; position: relative; width: 100%; height: 100vh; overflow: hidden; background: var(--bg); color: var(--text); font-family: Inter, 'Heebo', sans-serif">
<div class="scroll" style="position: absolute; inset: 0; overflow-y: auto">
<main dir="{{dir}}" style="position: relative; max-width: 640px; margin: 0 auto; padding: 14px 20px 72px; display: flex; flex-direction: column; gap: 22px">
  <header style="display: flex; align-items: center; gap: 12px">
    <a href="V2-Accueil.dc.html" aria-label="{{t.back}}" class="glass" style="flex-shrink: 0; width: 44px; height: 44px; border-radius: 22px; display: flex; align-items: center; justify-content: center; color: var(--text)"><span class="flip" style="display: inline-flex"><svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"></path></svg></span></a>
    <div style="flex: 1; min-width: 0">
      <p class="cap" style="margin: 0">{{t.cap}}</p>
      <h1 class="serif foil" style="margin: 2px 0 0; font-size: clamp(26px, 8vw, 34px); font-weight: 500; line-height: 1.05; letter-spacing: -0.01em">{{t.title}}</h1>
    </div>
  </header>
  <section class="glass" style="border-radius: 22px; padding: 14px 16px; display: flex; flex-direction: column; gap: 6px">
    <p style="margin: 0; font-size: 14px; font-weight: 600; line-height: 1.4">{{t.rav}}</p>
    <p style="margin: 0; font-size: 13px; line-height: 1.5; color: var(--soft)">{{t.draft}}</p>
  </section>
  <sc-if value="{{waiting}}" hint-placeholder-val="{{false}}"><p style="margin: 0; color: var(--soft)">{{t.wait}}</p></sc-if>
  <sc-if value="{{loaded}}" hint-placeholder-val="{{true}}">
    <div role="radiogroup" aria-label="{{t.filter}}" style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">
      <sc-for list="{{filters}}" as="f" hint-placeholder-count="2"><button role="radio" aria-checked="{{f.on}}" onClick="{{f.pick}}" style="{{f.style}}"><span style="font-size: 14px; font-weight: 600">{{f.name}}</span><span style="font-size: 12px; color: var(--soft)">{{f.sub}}</span></button></sc-for>
    </div>
    <sc-for list="{{chapters}}" as="c" hint-placeholder-count="8">
      <section style="display: flex; flex-direction: column">
        <div style="display: flex; align-items: baseline; justify-content: space-between; gap: 12px; margin-bottom: 6px">
          <h2 class="serif" style="margin: 0; font-size: 24px; font-weight: 500; line-height: 1.15">{{c.title}}</h2>
          <span lang="he" dir="rtl" style="flex-shrink: 0; font-family: 'Frank Ruhl Libre', serif; font-size: 18px; color: var(--soft)">{{c.heb}}</span>
        </div>
        <sc-for list="{{c.items}}" as="h" hint-placeholder-count="4">
          <article style="border-top: 1px solid var(--line); padding: 14px 0 8px; display: flex; flex-direction: column; gap: 6px">
            <p ref="{{h.fill}}" lang="{{h.lang}}" dir="{{h.dir}}" style="{{h.style}}"></p>
            <sc-if value="{{h.hasSrc}}" hint-placeholder-val="{{true}}">
              <button onClick="{{h.toggle}}" aria-expanded="{{h.aria}}" style="align-self: flex-start; min-height: 44px; padding: 0; border: none; background: none; color: var(--accent); font-family: inherit; font-size: 13px; font-weight: 600">{{h.label}}</button>
            </sc-if>
            <sc-if value="{{h.open}}" hint-placeholder-val="{{false}}">
              <p ref="{{h.fillHe}}" lang="he" dir="rtl" style="{{heStyle}}"></p>
            </sc-if>
          </article>
        </sc-for>
      </section>
    </sc-for>
  </sc-if>
</main>
</div>
</div>`, make: function () {
class Component extends DCLogic {
  componentDidMount() { if (!SM_DONNEES.lue('halakhot')) SM_DONNEES.charge('halakhot').then(() => this.forceUpdate(), () => this.setState({ absent: true })); }
  renderVals() {
    const s = this.state || {}; const mode = this.props.mode || 'clair'; const lang = APP.get('lang') || 'fr';
    const t = T[lang] || T[LANGUE[lang]] || T.fr; const L = LANGUE[lang] || 'fr'; const livre = SM_DONNEES.lue('halakhot');
    const rite = (window.SM_RITE ? SM_RITE().id : 'edot'); const tout = !!s.tout; const open = s.open || {};
    const card = (on) => 'min-height: 56px; min-width: 0; border-radius: 18px; padding: 6px 10px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 1px; font-family: inherit; color: var(--text); background: ' + (on ? 'var(--glass)' : 'transparent') + '; border: ' + (on ? '2px solid var(--accent-line)' : '1px solid var(--line2)');
    const fontCss = "'Frank Ruhl Libre', 'David Libre', serif";
    const style = L === 'he' ? 'margin: 0; font-family: ' + fontCss + '; font-size: 20px; line-height: 1.75; text-wrap: pretty' : 'margin: 0; font-size: 16px; line-height: 1.6; text-wrap: pretty';
    const pour = (h) => !h.id || tout || (livre.rites[h.rite] || []).indexOf(rite) >= 0;
    let n = 0;
    const chapters = !livre ? [] : livre.sections.map(sec => {
      const items = sec.blocs.filter(pour).map(h => { if (h.id) n++; const k = h.id || 'intro'; const isOpen = !!open[k];
        return { hasSrc: L !== 'he' && !!h.id, open: L !== 'he' && isOpen, aria: String(isOpen), label: isOpen ? t.hide : t.src, lang: L, dir: L === 'he' ? 'rtl' : 'ltr', style,
          fill: (el) => riche(el, L === 'he' ? h.t : h[L]), fillHe: (el) => riche(el, h.t),
          toggle: () => this.setState({ open: Object.assign({}, open, { [k]: !isOpen }) }) }; });
      return { title: L === 'he' ? sec.titre : sec['titre_' + L], heb: L === 'he' ? '' : sec.titre, items, any: items.length > 0 };
    }).filter(c => c.any);
    return { themeClass: 'th-' + mode, isParch: mode === 'parchemin', rootStyle: rootVars(mode), dir: (lang === 'he' || lang === 'tn' || lang === 'ma') ? 'rtl' : 'ltr', t,
      loaded: !!livre, waiting: !livre && !s.absent, chapters,
      heStyle: 'margin: 0; padding: 12px 14px; border-radius: 16px; background: var(--hl); font-family: ' + fontCss + '; font-size: 19px; line-height: 1.8; text-wrap: pretty',
      filters: [{ name: t.mine, sub: t.rites[rite], on: !tout, pick: () => this.setState({ tout: false }), style: card(!tout) },
        { name: t.all, sub: (livre ? livre.sections.reduce((a, x) => a + x.blocs.filter(b => b.id).length, 0) : '') + ' ' + t.n, on: tout, pick: () => this.setState({ tout: true }), style: card(tout) }] };
  }
}
return Component; } };
})();
