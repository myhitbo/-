/* Écran « Année » — gabarit (tpl) puis logique (make). */
SCREENS.annee = {
  title: "Année",
  tpl: `

<div class="t {{themeClass}}" dir="{{dir}}" style="{{rootStyle}}; position: relative; width: 100%; height: 100vh; overflow: hidden; background: var(--bg); color: var(--text); font-family: Inter, 'Heebo', 'Noto Sans Arabic', sans-serif">
<sc-if value="{{isParch}}" hint-placeholder-val="{{false}}"><svg aria-hidden="true" viewBox="0 0 400 900" preserveAspectRatio="none" style="position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none"><defs><filter id="pm" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.011" numOctaves="5" seed="5"></feTurbulence><feColorMatrix values="0 0 0 0 0.50  0 0 0 0 0.33  0 0 0 0 0.12  0 0 0 0.55 -0.12"></feColorMatrix></filter><filter id="pf" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.018 0.9" numOctaves="2" seed="8"></feTurbulence><feColorMatrix values="0 0 0 0 0.40  0 0 0 0 0.27  0 0 0 0 0.10  0 0 0 0.16 0"></feColorMatrix></filter><filter id="pg" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" stitchTiles="stitch"></feTurbulence><feColorMatrix values="0 0 0 0 0.35  0 0 0 0 0.24  0 0 0 0 0.10  0 0 0 0.15 0"></feColorMatrix></filter><filter id="pbl"><feGaussianBlur stdDeviation="2"></feGaussianBlur></filter><radialGradient id="pv" cx="50%" cy="45%" r="75%"><stop offset="0.55" stop-color="#6B4415" stop-opacity="0"></stop><stop offset="0.86" stop-color="#6B4415" stop-opacity="0.15"></stop><stop offset="1" stop-color="#4A2C0A" stop-opacity="0.38"></stop></radialGradient></defs><rect width="400" height="900" filter="url(#pm)"></rect><rect width="400" height="900" filter="url(#pf)"></rect><rect width="400" height="900" filter="url(#pg)"></rect><circle cx="249" cy="668" r="6.8" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="296" cy="830" r="2.2" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="377" cy="584" r="7.4" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="188" cy="222" r="5.3" fill="#8A5A1C" opacity="0.11" filter="url(#pbl)"></circle><circle cx="5" cy="195" r="3.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="306" cy="144" r="6.8" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="247" cy="114" r="2.0" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="84" cy="194" r="7.9" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="116" cy="865" r="5.2" fill="#8A5A1C" opacity="0.12" filter="url(#pbl)"></circle><circle cx="82" cy="847" r="6.1" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="357" cy="269" r="4.2" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="58" cy="59" r="3.8" fill="#8A5A1C" opacity="0.11" filter="url(#pbl)"></circle><circle cx="1" cy="610" r="4.0" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="327" cy="433" r="3.9" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="282" cy="51" r="7.9" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="300" cy="760" r="2.1" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="146" cy="521" r="2.1" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="72" cy="860" r="3.2" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="372" cy="848" r="4.1" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="210" cy="698" r="2.6" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="319" cy="774" r="2.2" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="36" cy="307" r="5.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="136" cy="832" r="5.3" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="127" cy="160" r="2.5" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="276" cy="897" r="3.0" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="395" cy="480" r="4.4" fill="#8A5A1C" opacity="0.08" filter="url(#pbl)"></circle><circle cx="238" cy="744" r="4.7" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="22" cy="824" r="2.2" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="335" cy="118" r="6.4" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="252" cy="709" r="2.6" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="60" cy="760" r="3.8" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="400" cy="767" r="7.9" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="195" cy="657" r="4.9" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="162" cy="132" r="4.3" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="384" cy="564" r="5.0" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="36" cy="245" r="6.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><rect width="400" height="900" fill="url(#pv)"></rect></svg></sc-if><div aria-hidden="true" style="position: absolute; top: -120px; right: -90px; width: 340px; height: 340px; border-radius: 50%; background: radial-gradient(circle at 40% 40%, var(--blob1), transparent 68%); opacity: var(--blobop); filter: blur(30px); pointer-events: none"></div>
<div aria-hidden="true" style="position: absolute; top: -60px; left: -120px; width: 300px; height: 260px; border-radius: 50%; background: radial-gradient(circle, var(--blob2), transparent 70%); opacity: var(--blobop); filter: blur(40px); pointer-events: none"></div>
<div class="scroll" style="position: absolute; inset: 0; overflow-y: auto">
<main style="position: relative; max-width: 560px; margin: 0 auto; padding: 22px 20px 120px; display: flex; flex-direction: column; gap: 24px">
<header style="display: flex; flex-direction: column; gap: 4px"><p class="cap" style="margin: 0">{{yearLabel}}</p><h1 class="serif foil" style="margin: 0; font-size: clamp(36px, 11vw, 52px); font-weight: 500; line-height: 1; letter-spacing: -0.02em">{{t.yearTitle}}</h1></header>
<section style="display: flex; gap: 28px; flex-wrap: wrap; align-items: flex-end">
  <div><p class="cap" style="margin: 0">{{t.parashiyotDone}}</p><p class="serif count" style="margin: 4px 0 0; font-size: 48px; font-weight: 500; line-height: 1">{{doneCount}}<span style="font-size: 22px; color: var(--soft)">/54</span></p></div>
  <div><p class="cap" style="margin: 0">{{t.streak}}</p><p class="serif" style="margin: 4px 0 0; font-size: 30px; font-weight: 500; line-height: 1">{{G.streak}} <span style="font-family: Inter, sans-serif; font-size: 13px; color: var(--soft)">{{t.weeks}}</span></p></div>
  <div style="flex: 1; min-width: 160px"><p class="cap" style="margin: 0 0 8px">{{t.untilST}}</p><div style="height: 6px; border-radius: 3px; background: var(--line)"><div style="{{yearBar}}"></div></div></div>
</section>
<div style="display: flex; gap: 16px; flex-wrap: wrap; font-size: 12px; color: var(--soft)">
  <span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 50%; background: var(--accent-line)"></span>{{t.lgDone}}</span>
  <span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 50%; border: 2px solid var(--text); box-sizing: border-box"></span>{{t.lgWeek}}</span>
  <span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 50%; border: 1px solid var(--line2); box-sizing: border-box"></span>{{t.lgLater}}</span>
  <span style="display: flex; align-items: center; gap: 6px"><span style="width: 10px; height: 10px; border-radius: 50%; border: 1.5px dashed var(--accent-line); box-sizing: border-box"></span>{{t.lgLate}}</span>
</div>
<sc-for list="{{books}}" as="bk" hint-placeholder-count="5">
  <section style="display: flex; flex-direction: column; gap: 10px">
    <div style="display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1px solid var(--line); padding-bottom: 6px">
      <h2 class="serif" style="margin: 0; font-size: 24px; font-weight: 500">{{bk.name}}</h2>
      <span lang="he" dir="rtl" style="font-family: 'Frank Ruhl Libre', serif; font-size: 18px; color: var(--soft)">{{bk.heb}}</span>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(96px, 1fr)); gap: 6px">
      <sc-for list="{{bk.items}}" as="p" hint-placeholder-count="12">
        <div style="{{p.style}}"><span style="font-size: 13px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{{p.name}}</span><span style="display: flex; justify-content: space-between; align-items: baseline; gap: 6px"><span style="font-size: 11px; font-weight: 600; color: var(--accent)">{{p.note}}</span><span lang="he" dir="rtl" style="font-family: 'Frank Ruhl Libre', serif; font-size: 14px; opacity: 0.8">{{p.heb}}</span></span></div>
      </sc-for>
    </div>
  </section>
</sc-for>
</main>
</div>
${SM_NAV('annee')}
</div>
`,
  make: function () {
const THEMES = SM_THEMES, rootVars = SM_ROOTVARS;
/* Les cinq livres : nom hébreu, et nom hébreu de chacune de leurs parachiyot (54 en tout) */
const BOOKS = [{"heb": "בראשית", "items": ["בראשית", "נח", "לך לך", "וירא", "חיי שרה", "תולדות", "ויצא", "וישלח", "וישב", "מקץ", "ויגש", "ויחי"]}, {"heb": "שמות", "items": ["שמות", "וארא", "בא", "בשלח", "יתרו", "משפטים", "תרומה", "תצוה", "כי תשא", "ויקהל", "פקודי"]}, {"heb": "ויקרא", "items": ["ויקרא", "צו", "שמיני", "תזריע", "מצורע", "אחרי מות", "קדושים", "אמור", "בהר", "בחוקותי"]}, {"heb": "במדבר", "items": ["במדבר", "נשא", "בהעלותך", "שלח", "קרח", "חקת", "בלק", "פינחס", "מטות", "מסעי"]}, {"heb": "דברים", "items": ["דברים", "ואתחנן", "עקב", "ראה", "שופטים", "כי תצא", "כי תבוא", "נצבים", "וילך", "האזינו", "וזאת הברכה"]}];
class Component extends DCLogic {
  renderVals() {
    /* Vraie progression : terminée = les 7 alyot lues cette année ; à compléter = semaine passée non terminée */
    const mode = this.props.mode || 'clair'; let k = 0;
    const Y = window.SM_YEAR ? SM_YEAR() : { year: '', done: {}, part: {}, cur: [], count: 0 };
    const first = Y.cur.length ? Math.min.apply(null, Y.cur) : -1;
    const books = BOOKS.map((b, bi) => ({ heb: SM_HEB(SM_BOOK(bi), b.heb), name: SM_BOOK(bi), items: b.items.map(heb => { const i = k++; const p = { name: SM_PARASHA([i]) }; p.heb = SM_HEB(p.name, heb);
      const st = Y.done[i] ? 'done' : Y.cur.indexOf(i) >= 0 ? 'cur' : (first >= 0 && i < first) ? 'late' : 'todo';
      return { ...p, note: st !== 'done' && Y.part[i] ? Y.part[i] + '/7' : '', style: 'min-width: 0; min-height: 52px; padding: 8px 10px; border-radius: 14px; display: flex; flex-direction: column; justify-content: center; gap: 1px; ' +
        (st === 'done' ? 'background: var(--accent-line); color: #1C1A17;' : st === 'cur' ? 'border: 2px solid var(--text); background: var(--glass);' :
         st === 'late' ? 'border: 1.5px dashed var(--accent-line); color: var(--soft);' : 'border: 1px solid var(--line); color: var(--soft);') }; }) }));
    return { themeClass: 'th-' + mode, isParch: mode === 'parchemin', rootStyle: rootVars(mode), books, yearLabel: SM_FMT(SM_TR().yearN, { year: Y.year }), doneCount: Y.count,
      yearBar: 'height: 100%; border-radius: 3px; background: var(--accent-line); width: ' + Math.round(Y.count / 54 * 100) + '%' };
  }
}

return Component;
  }
};
