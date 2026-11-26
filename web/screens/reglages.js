/* Écran « Réglages » — gabarit (tpl) puis logique (make). */
SCREENS.reglages = {
  title: "Réglages",
  tpl: `

<div class="t {{themeClass}}" dir="{{dir}}" style="{{rootStyle}}; position: relative; width: 100%; height: 100vh; overflow: hidden; background: var(--bg); color: var(--text); font-family: Inter, 'Heebo', 'Noto Sans Arabic', sans-serif">
<sc-if value="{{isParch}}" hint-placeholder-val="{{false}}"><svg aria-hidden="true" viewBox="0 0 400 900" preserveAspectRatio="none" style="position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none"><defs><filter id="pm" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.011" numOctaves="5" seed="5"></feTurbulence><feColorMatrix values="0 0 0 0 0.50  0 0 0 0 0.33  0 0 0 0 0.12  0 0 0 0.55 -0.12"></feColorMatrix></filter><filter id="pf" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.018 0.9" numOctaves="2" seed="8"></feTurbulence><feColorMatrix values="0 0 0 0 0.40  0 0 0 0 0.27  0 0 0 0 0.10  0 0 0 0.16 0"></feColorMatrix></filter><filter id="pg" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" stitchTiles="stitch"></feTurbulence><feColorMatrix values="0 0 0 0 0.35  0 0 0 0 0.24  0 0 0 0 0.10  0 0 0 0.15 0"></feColorMatrix></filter><filter id="pbl"><feGaussianBlur stdDeviation="2"></feGaussianBlur></filter><radialGradient id="pv" cx="50%" cy="45%" r="75%"><stop offset="0.55" stop-color="#6B4415" stop-opacity="0"></stop><stop offset="0.86" stop-color="#6B4415" stop-opacity="0.15"></stop><stop offset="1" stop-color="#4A2C0A" stop-opacity="0.38"></stop></radialGradient></defs><rect width="400" height="900" filter="url(#pm)"></rect><rect width="400" height="900" filter="url(#pf)"></rect><rect width="400" height="900" filter="url(#pg)"></rect><circle cx="249" cy="668" r="6.8" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="296" cy="830" r="2.2" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="377" cy="584" r="7.4" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="188" cy="222" r="5.3" fill="#8A5A1C" opacity="0.11" filter="url(#pbl)"></circle><circle cx="5" cy="195" r="3.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="306" cy="144" r="6.8" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="247" cy="114" r="2.0" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="84" cy="194" r="7.9" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="116" cy="865" r="5.2" fill="#8A5A1C" opacity="0.12" filter="url(#pbl)"></circle><circle cx="82" cy="847" r="6.1" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="357" cy="269" r="4.2" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="58" cy="59" r="3.8" fill="#8A5A1C" opacity="0.11" filter="url(#pbl)"></circle><circle cx="1" cy="610" r="4.0" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="327" cy="433" r="3.9" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="282" cy="51" r="7.9" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="300" cy="760" r="2.1" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="146" cy="521" r="2.1" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="72" cy="860" r="3.2" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="372" cy="848" r="4.1" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="210" cy="698" r="2.6" fill="#8A5A1C" opacity="0.13" filter="url(#pbl)"></circle><circle cx="319" cy="774" r="2.2" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="36" cy="307" r="5.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><circle cx="136" cy="832" r="5.3" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="127" cy="160" r="2.5" fill="#8A5A1C" opacity="0.07" filter="url(#pbl)"></circle><circle cx="276" cy="897" r="3.0" fill="#8A5A1C" opacity="0.06" filter="url(#pbl)"></circle><circle cx="395" cy="480" r="4.4" fill="#8A5A1C" opacity="0.08" filter="url(#pbl)"></circle><circle cx="238" cy="744" r="4.7" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="22" cy="824" r="2.2" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="335" cy="118" r="6.4" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="252" cy="709" r="2.6" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="60" cy="760" r="3.8" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="400" cy="767" r="7.9" fill="#8A5A1C" opacity="0.10" filter="url(#pbl)"></circle><circle cx="195" cy="657" r="4.9" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="162" cy="132" r="4.3" fill="#8A5A1C" opacity="0.15" filter="url(#pbl)"></circle><circle cx="384" cy="564" r="5.0" fill="#8A5A1C" opacity="0.09" filter="url(#pbl)"></circle><circle cx="36" cy="245" r="6.7" fill="#8A5A1C" opacity="0.14" filter="url(#pbl)"></circle><rect width="400" height="900" fill="url(#pv)"></rect></svg></sc-if><div aria-hidden="true" style="position: absolute; top: -120px; right: -90px; width: 340px; height: 340px; border-radius: 50%; background: radial-gradient(circle at 40% 40%, var(--blob1), transparent 68%); opacity: var(--blobop); filter: blur(30px); pointer-events: none"></div>
<div aria-hidden="true" style="position: absolute; top: -60px; left: -120px; width: 300px; height: 260px; border-radius: 50%; background: radial-gradient(circle, var(--blob2), transparent 70%); opacity: var(--blobop); filter: blur(40px); pointer-events: none"></div>
<div class="scroll" style="position: absolute; inset: 0; overflow-y: auto">
<main style="position: relative; max-width: 560px; margin: 0 auto; padding: 22px 20px 120px; display: flex; flex-direction: column; gap: 24px">
<header style="display: flex; flex-direction: column; gap: 4px"><h1 class="serif foil" style="margin: 0; font-size: clamp(36px, 11vw, 52px); font-weight: 500; line-height: 1">{{t.title}}</h1></header>
<sc-if value="{{hasDraft}}" hint-placeholder-val="{{false}}"><p dir="ltr" style="margin: -8px 0 0; padding: 8px 12px; border-radius: 12px; background: var(--hl); font-size: 12px; color: var(--soft)">{{t.draft}}</p></sc-if>

<section style="display: flex; flex-direction: column; gap: 10px">
  <h2 class="cap" style="margin: 0">{{t.appearance}}</h2>
  <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 6px">
    <sc-for list="{{modes}}" as="m" hint-placeholder-count="4"><button onClick="{{m.pick}}" aria-pressed="{{m.on}}" style="{{m.style}}"><span lang="he" style="font-family: 'Frank Ruhl Libre', serif; font-size: 22px">אָ</span><span style="font-size: 11px; font-weight: 600; max-width: 100%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap">{{m.name}}</span></button></sc-for>
  </div>
</section>

<section style="display: flex; flex-direction: column; gap: 10px">
  <h2 class="cap" style="margin: 0">{{t.lang}}</h2>
  <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 130px), 1fr)); gap: 8px">
    <sc-for list="{{langs}}" as="l" hint-placeholder-count="6"><button onClick="{{l.pick}}" aria-pressed="{{l.on}}" style="{{l.style}}"><span dir="{{l.dir}}" style="font-size: 17px; font-weight: 700">{{l.native}}</span><span style="font-size: 12px; color: var(--soft)">{{l.sub}}</span></button></sc-for>
  </div>
</section>

<section style="display: flex; flex-direction: column; gap: 10px">
  <h2 class="cap" style="margin: 0">{{t.font}}</h2>
  <div class="glass" style="border-radius: 22px; overflow: hidden">
    <sc-for list="{{fonts}}" as="f" hint-placeholder-count="5">
      <button onClick="{{f.pick}}" aria-pressed="{{f.on}}" style="{{f.style}}"><span style="{{f.dot}}"></span><span dir="ltr" style="flex: 1; min-width: 0; display: flex; flex-direction: column; text-align: start"><span style="font-size: 15px; font-weight: 600">{{f.name}}</span><span style="font-size: 12px; color: var(--soft); white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{{f.desc}}</span></span><span lang="he" dir="rtl" style="{{f.sample}}">בְּרֵאשִׁית</span></button>
    </sc-for>
  </div>
  <div style="display: flex; align-items: center; gap: 10px">
    <span style="flex: 1; font-size: 15px">{{t.size}}</span>
    <div dir="ltr" style="display: flex; align-items: center; gap: 8px">
      <button onClick="{{smaller}}" aria-label="A−" style="width: 44px; height: 44px; border-radius: 22px; border: 1px solid var(--line2); background: transparent; color: var(--text); font-size: 14px">A−</button>
      <span class="count" style="min-width: 28px; text-align: center; font-weight: 700">{{fs}}</span>
      <button onClick="{{bigger}}" aria-label="A+" style="width: 44px; height: 44px; border-radius: 22px; border: 1px solid var(--line2); background: transparent; color: var(--text); font-size: 18px">A+</button>
    </div>
  </div>
  <div class="glass" style="border-radius: 22px; padding: 16px">
    <p class="cap" style="margin: 0 0 6px">{{t.preview}}</p>
    <p dir="rtl" lang="he" style="{{previewStyle}}">וַיֵּצֵא יַעֲקֹב מִבְּאֵר שָׁבַע וַיֵּלֶךְ חָרָנָה׃</p>
    <p dir="rtl" lang="arc" style="{{previewT}}">וּנְפַק יַעֲקֹב מִבְּאֵרָא דְשָׁבַע וַאֲזַל לְחָרָן׃</p>
  </div>
</section>

<section style="display: flex; flex-direction: column">
  <h2 class="cap" style="margin: 0 0 10px">{{t.place}}</h2>
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-bottom: 8px">
    <sc-for list="{{places}}" as="p" hint-placeholder-count="2"><button onClick="{{p.pick}}" aria-pressed="{{p.on}}" style="{{p.style}}">{{p.name}}</button></sc-for>
  </div>
  <label style="display: flex; justify-content: space-between; align-items: center; gap: 12px; min-height: 60px; border-top: 1px solid var(--line)"><span style="font-size: 15px">{{t.city}}</span><select class="field" aria-label="{{t.city}}" ref="{{fillCities}}" onChange="{{pickCity}}" style="width: auto; min-width: 0; max-width: 62%; height: 44px"></select></label>
  <div style="display: flex; justify-content: space-between; align-items: center; gap: 12px; min-height: 52px; border-top: 1px solid var(--line)"><span style="font-size: 15px">{{t.reminder}}</span><span style="display: flex; align-items: center; gap: 10px"><input class="field" type="time" aria-label="{{t.remTime}}" value="{{remAt}}" onChange="{{pickRemAt}}" disabled="{{remOff}}" style="width: auto; min-width: 0; height: 44px; padding: 0 10px"><button role="switch" aria-checked="{{remOn}}" aria-label="{{t.reminder}}" onClick="{{toggleRem}}" style="{{remSwitch}}"><span style="{{remKnob}}"></span></button></span></div>
  <p style="margin: 0; padding: 8px 0 2px; font-size: 13px; line-height: 1.45; color: var(--soft)">{{t.remHelp}}</p>
  <div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 6px 0 4px"><p style="margin: 0; flex: 1; font-size: 13px; line-height: 1.45; font-weight: 600">{{remNextLine}}</p><sc-if value="{{canTest}}" hint-placeholder-val="{{false}}"><button onClick="{{testNotify}}" style="flex-shrink: 0; height: 40px; padding: 0 16px; border-radius: 20px; border: 1px solid var(--line2); background: transparent; color: var(--text); font: 600 14px Inter, sans-serif">{{t.remTest}}</button></sc-if></div>
  <sc-if value="{{remInexact}}" hint-placeholder-val="{{false}}"><div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 6px 0 4px"><p style="margin: 0; flex: 1; font-size: 13px; line-height: 1.45; color: var(--soft)">{{t.remExact}}</p><button onClick="{{askExact}}" style="flex-shrink: 0; height: 40px; padding: 0 16px; border-radius: 20px; border: none; background: var(--pill); color: var(--on-pill); font: 600 14px Inter, sans-serif">{{t.remAllow}}</button></div></sc-if>
  <sc-if value="{{remBlocked}}" hint-placeholder-val="{{false}}"><div style="display: flex; align-items: center; justify-content: space-between; gap: 12px; padding: 6px 0 4px"><p style="margin: 0; flex: 1; font-size: 13px; line-height: 1.45; font-weight: 600; color: var(--accent)">{{t.remBlocked}}</p><button onClick="{{askNotify}}" style="flex-shrink: 0; height: 40px; padding: 0 16px; border-radius: 20px; border: none; background: var(--pill); color: var(--on-pill); font: 600 14px Inter, sans-serif">{{t.remAllow}}</button></div></sc-if>
</section>

<section aria-label="{{t.rhythm}}" style="display: flex; flex-direction: column; gap: 10px">
  <h2 class="cap" style="margin: 0">{{t.reading}} · {{t.rhythm}}</h2>
  <div role="radiogroup" aria-label="{{t.rhythm}}" style="display: flex; flex-direction: column; gap: 8px">
    <sc-for list="{{rhOpts}}" as="o" hint-placeholder-count="4"><button role="radio" aria-checked="{{o.on}}" onClick="{{o.pick}}" style="{{o.style}}"><span style="{{o.dot}}"></span><span style="flex: 1; min-width: 0; text-align: start"><span style="display: block; font-size: 15px; font-weight: 600">{{o.title}}</span><span style="display: block; font-size: 13px; line-height: 1.4; color: var(--soft)">{{o.sub}}</span></span></button></sc-for>
  </div>
  <sc-if value="{{rhIsDay}}" hint-placeholder-val="{{false}}"><div style="display: flex; flex-direction: column; gap: 8px"><p class="cap" style="margin: 0">{{t.rhDay}}</p><div style="display: flex; flex-wrap: wrap; gap: 6px"><sc-for list="{{dayChips}}" as="d" hint-placeholder-count="3"><button onClick="{{d.pick}}" aria-pressed="{{d.on}}" style="{{d.style}}"><span style="display: block; font-size: 14px; font-weight: 600">{{d.name}}</span><span style="display: block; font-size: 11px; color: var(--soft)">{{d.sub}}</span></button></sc-for></div></div></sc-if>
  <sc-if value="{{rhIsN}}" hint-placeholder-val="{{false}}"><div style="display: flex; flex-direction: column; gap: 8px"><p class="cap" style="margin: 0">{{t.rhCount}}</p><div style="display: flex; flex-wrap: wrap; gap: 6px"><sc-for list="{{nChips}}" as="d" hint-placeholder-count="3"><button onClick="{{d.pick}}" aria-pressed="{{d.on}}" style="{{d.style}}"><span style="display: block; font-size: 14px; font-weight: 600">{{d.name}}</span><span style="display: block; font-size: 11px; color: var(--soft)">{{d.sub}}</span></button></sc-for></div></div></sc-if>
</section>

<section aria-label="{{t.order}}" style="display: flex; flex-direction: column; gap: 10px">
  <h2 class="cap" style="margin: 0">{{t.order}}</h2>
  <div role="radiogroup" aria-label="{{t.order}}" style="display: flex; flex-direction: column; gap: 8px">
    <sc-for list="{{orOpts}}" as="o" hint-placeholder-count="4"><button role="radio" aria-checked="{{o.on}}" onClick="{{o.pick}}" style="{{o.style}}"><span style="{{o.dot}}"></span><span style="flex: 1; min-width: 0; text-align: start"><span style="display: block; font-size: 15px; font-weight: 600">{{o.title}}</span><span style="display: block; font-size: 13px; line-height: 1.4; color: var(--soft)">{{o.sub}}</span></span></button></sc-for>
  </div>
</section>
<section aria-label="{{nt.title}}" style="display: flex; flex-direction: column; gap: 10px">
  <h2 class="cap" style="margin: 0">{{nt.title}}</h2>
  <p style="margin: 0; font-size: 13px; line-height: 1.5; color: var(--soft)">{{nt.help}}</p>
  <div role="radiogroup" aria-label="{{nt.title}}" style="display: flex; flex-direction: column; gap: 8px">
    <sc-for list="{{ntOpts}}" as="o" hint-placeholder-count="3"><button role="radio" aria-checked="{{o.on}}" onClick="{{o.pick}}" style="{{o.style}}"><span style="{{o.dot}}"></span><span style="flex: 1; min-width: 0; text-align: start; font-size: 15px; font-weight: 600">{{o.title}}</span></button></sc-for>
  </div>
</section>
<sc-if value="{{hasDonate}}" hint-placeholder-val="{{false}}">
<section aria-label="{{t.donate}}" class="glass" style="border-radius: 22px; padding: 16px 18px; display: flex; flex-direction: column; gap: 10px">
  <h2 class="cap" style="margin: 0">{{t.donate}}</h2>
  <p style="margin: 0; font-size: 14px; line-height: 1.5; color: var(--soft)">{{t.donateSub}}</p>
  <a href="{{donateUrl}}" target="_blank" rel="noopener" style="height: 52px; border-radius: 26px; background: var(--pill); color: var(--on-pill); display: flex; align-items: center; justify-content: center; text-decoration: none; font: 600 15px Inter, sans-serif">{{t.donateBtn}}</a>
</section>
</sc-if>
<section style="display: flex; flex-direction: column">
  <a href="V2-Sources.dc.html" style="min-height: 56px; display: flex; align-items: center; justify-content: space-between; gap: 12px; border-top: 1px solid var(--line); color: var(--text); text-decoration: none; font-size: 15px"><span>{{t.srcRow}}</span><span class="flip" style="display: inline-flex; color: var(--soft)"><svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"></path></svg></span></a>
</section>
</main>
</div>
${SM_NAV('reglages')}
</div>
`,
  make: function () {
const THEMES = SM_THEMES, rootVars = SM_ROOTVARS, LANGS = SM_LANGS;
const T = {"fr":{"title":"Réglages","appearance":"Apparence","lang":"Langue de l'application","font":"Police du texte hébreu","size":"Taille du texte","place":"Où vis-tu ?","israel":"Israël","diaspora":"Diaspora","city":"Ville","cityVal":"Jérusalem","reminder":"Rappel","reading":"Lecture","rhythm":"Rythme","rhythmVal":"Une alya par jour","order":"Ordre","orderVal":"Verset, verset, Targoum","preview":"Aperçu","clair":"Clair","sombre":"Sombre","texte":"Texte","parchemin":"Parchemin","draft":""},"en":{"title":"Settings","appearance":"Appearance","lang":"App language","font":"Hebrew text font","size":"Text size","place":"Where you live","israel":"Israel","diaspora":"Diaspora","city":"City","cityVal":"Jerusalem","reminder":"Reminder","reading":"Reading","rhythm":"Pace","rhythmVal":"One aliyah a day","order":"Order","orderVal":"Verse, verse, Targum","preview":"Preview","clair":"Light","sombre":"Dark","texte":"Text","parchemin":"Parchment","draft":""},"es":{"title":"Configuración","appearance":"Apariencia","lang":"Idioma de la app","font":"Tipo de letra del texto hebreo","size":"Tamaño del texto","place":"Dónde vives","israel":"Israel","diaspora":"Diáspora","city":"Ciudad","cityVal":"Jerusalén","reminder":"Recordatorio","reading":"Lectura","rhythm":"Ritmo","rhythmVal":"Una aliá por día","order":"Orden","orderVal":"Versículo, versículo, Targum","preview":"Vista previa","clair":"Claro","sombre":"Oscuro","texte":"Texto","parchemin":"Pergamino","draft":""},"he":{"title":"הגדרות","appearance":"מראה","lang":"שפת האפליקציה","font":"גופן הטקסט העברי","size":"גודל הטקסט","place":"מקום מגורים","israel":"ישראל","diaspora":"חוץ לארץ","city":"עיר","cityVal":"ירושלים","reminder":"תזכורת","reading":"קריאה","rhythm":"קצב","rhythmVal":"עלייה אחת ביום","order":"סדר","orderVal":"פסוק, פסוק, תרגום","preview":"תצוגה מקדימה","clair":"בהיר","sombre":"כהה","texte":"טקסט","parchemin":"קלף","draft":""},"tn":{"title":"אלאעדאדאת","appearance":"אלשכל","lang":"לע׳ה אלתטביקה","font":"אלכ׳ט מתאע אלנץ אלעברי","size":"קד אלכתיבה","place":"וין תסכן","israel":"ישראל","diaspora":"ברא","city":"אלמדינה","cityVal":"ירושלים","reminder":"אלתד׳כיר","reading":"אלקראיה","rhythm":"אלריתם","rhythmVal":"עליה כל נהאר","order":"אלתרתיב","orderVal":"איה, איה, תרגום","preview":"מעאינה","clair":"פאתח","sombre":"ע׳אמק","texte":"נץ","parchemin":"רק","draft":"Traduction brouillon — à faire valider par un locuteur tunisien"},"ma":{"title":"الإعدادات","appearance":"الشكل","lang":"لغة التطبيق","font":"الخط ديال النص العبري","size":"حجم الكتابة","place":"فين ساكن","israel":"إسرائيل","diaspora":"برّا","city":"المدينة","cityVal":"القدس","reminder":"التذكير","reading":"القراية","rhythm":"الإيقاع","rhythmVal":"عليا كل نهار","order":"الترتيب","orderVal":"آية، آية، ترجوم","preview":"معاينة","clair":"فاتح","sombre":"غامق","texte":"نص","parchemin":"رَقّ","draft":"Traduction brouillon — à faire valider par un locuteur marocain"}};
const FONTS = [{"id": "frank", "name": "Frank Ruhl", "css": "'Frank Ruhl Libre', serif"}, {"id": "david", "name": "David", "css": "'David Libre', serif"}, {"id": "noto", "name": "Noto Serif", "css": "'Noto Serif Hebrew', serif"}, {"id": "heebo", "name": "Heebo", "css": "Heebo, sans-serif"}];
const NT = {"fr":{"title":"Verset sans Targoum","help":"Quand Onkelos ne traduit pas le verset (ex. « Atarot ve-Divon », Bamidbar 32:3).","o":["Lire l'hébreu 3 fois","Lire le Targoum Yerouchalmi","Les deux (3 fois + Yerouchalmi)"]},"en":{"title":"Verse without Targum","help":"When Onkelos doesn't translate the verse (e.g. “Atarot and Divon”, Numbers 32:3).","o":["Read the Hebrew 3 times","Read Targum Yerushalmi","Both (3 times + Yerushalmi)"]},"es":{"title":"Versículo sin Targum","help":"Cuando Onkelos no traduce el versículo (p. ej. «Atarot y Dibón», Números 32:3).","o":["Leer el hebreo 3 veces","Leer el Targum Yerushalmi","Ambos (3 veces + Yerushalmi)"]},"he":{"title":"פסוק בלי תרגום","help":"כשאונקלוס אינו מתרגם את הפסוק (כגון „עטרות ודיבן”, במדבר לב, ג).","o":["לקרוא את המקרא שלוש פעמים","לקרוא תרגום ירושלמי","שניהם (שלוש פעמים + ירושלמי)"]},"tn":{"title":"איה בלא תרגום","help":"כי אונקלוס מא יתרג׳מש אלאיה (כימא «עטרות ודיבן», במדבר 32:3).","o":["אקרא אלעברי 3 מראת","אקרא תרגום ירושלמי","אלזוז (3 מראת + ירושלמי)"]},"ma":{"title":"آية بلا ترجوم","help":"ملي أونقلوس ما كيترجمش الآية (بحال «عطروت وديبون»، بمدبار 32:3).","o":["قرا العبري 3 دالمرات","قرا ترجوم يروشلمي","بجوج (3 دالمرات + يروشلمي)"]}};
const RADIO = (on) => 'display: flex; align-items: center; gap: 12px; min-height: 56px; padding: 10px 16px; border-radius: 20px; font-family: inherit; color: var(--text); background: ' + (on ? 'var(--glass)' : 'transparent') + '; border: ' + (on ? '2px solid var(--accent-line)' : '1px solid var(--line)');
const DOT = (on) => 'flex-shrink: 0; width: 20px; height: 20px; border-radius: 50%; box-sizing: border-box; ' + (on ? 'border: 6px solid var(--accent-line)' : 'border: 2px solid var(--line2)');
class Component extends DCLogic {
  renderVals() {
    const s = this.state || {}; const mode = s.mode ?? (this.props.mode || 'clair'); const lang = s.lang ?? APP.get('lang'); const font = s.font ?? APP.get('font'); const fs = s.fs ?? APP.get('fs'); const place = s.place ?? APP.get('place');
    const L = LANGS.find(l => l.id === lang); const F = FONTS.find(f => f.id === font) || FONTS[0]; const t = Object.assign({}, SM_TR(lang), T[lang]);
    const card = (on) => 'min-height: 60px; min-width: 0; border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 1px; font-family: inherit; color: var(--text); background: ' + (on ? 'var(--glass)' : 'transparent') + '; border: ' + (on ? '2px solid var(--accent-line)' : '1px solid var(--line2)');
    /* Rythme et ordre de lecture */
    const rh = s.rh ?? (APP.get('rh') ?? 0), order = s.order ?? (APP.get('order') ?? 0), rhDay = s.rhDay ?? (APP.get('rhDay') ?? 4), rhN = s.rhN ?? (APP.get('rhN') ?? 3);
    const chip = (on) => 'min-width: 52px; min-height: 48px; padding: 6px 12px; border-radius: 16px; font-family: inherit; color: var(--text); background: ' + (on ? 'var(--glass)' : 'transparent') + '; border: ' + (on ? '2px solid var(--accent-line)' : '1px solid var(--line2)');
    const reading = {
      rhOpts: [0, 1, 2, 3].map(i => ({ title: t['rh' + i], sub: t['rh' + i + 's'], on: i === rh, pick: () => this.setState({ rh: i }), style: RADIO(i === rh), dot: DOT(i === rh) })),
      orOpts: [0, 1, 2, 3].map(i => ({ title: t['or' + i], sub: t['or' + i + 's'], on: i === order, pick: () => this.setState({ order: i }), style: RADIO(i === order), dot: DOT(i === order) })),
      rhIsDay: rh === 1, rhIsN: rh === 2,
      dayChips: [0, 1, 2, 3, 4, 5].map(d => ({ name: SM_WEEKDAY(d, 'short'), sub: '', on: d === rhDay, pick: () => this.setState({ rhDay: d }), style: chip(d === rhDay) })),
      nChips: [2, 3].map(n => ({ name: t['rhN' + n], sub: t['rhN' + n + 's'], on: n === rhN, pick: () => this.setState({ rhN: n }), style: chip(n === rhN) }))
    };
    /* Rappel */
    const rem = (s.rem ?? APP.get('rem')) !== false, remAt = s.remAt ?? (APP.get('remAt') || '07:30');
    const reminder = { remOn: rem ? 'true' : 'false', remOff: !rem, remAt, pickRemAt: (e) => { if (e.target.value) this.setState({ remAt: e.target.value }); },
      toggleRem: () => { this.setState({ rem: !rem }); if (!rem && window.SMAndroid && SMAndroid.askNotify) SMAndroid.askNotify(); },
      remNextLine: (() => { const L = rem && window.SM_REMINDERS ? SM_REMINDERS() : []; if (!L.length) return t.remNone;
        let tz; try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone; } catch (e) {}
        return SM_FMT(t.remNext, { when: SM_DATE(L[0].at, { weekday: 'long', hour: '2-digit', minute: '2-digit' }, tz) }); })(),
      canTest: rem && !!(window.SMAndroid && SMAndroid.testNotify),
      testNotify: () => { if (window.SMAndroid && SMAndroid.testNotify && !SMAndroid.testNotify('Shnayim Mikra', t.remTestText) && SMAndroid.askNotify) SMAndroid.askNotify(); },
      remInexact: rem && !!(window.SMAndroid && SMAndroid.canExact) && !SMAndroid.canExact(), askExact: () => { if (window.SMAndroid && SMAndroid.askExact) SMAndroid.askExact(); },
      remBlocked: rem && !!(window.SMAndroid && SMAndroid.canNotify) && !SMAndroid.canNotify(), askNotify: () => { if (window.SMAndroid && SMAndroid.askNotify) SMAndroid.askNotify(); },
      remSwitch: 'flex-shrink: 0; width: 52px; height: 32px; padding: 0; border-radius: 16px; border: none; position: relative; transition: background-color .2s; background: ' + (rem ? 'var(--accent-line)' : 'var(--line2)'),
      remKnob: 'position: absolute; top: 3px; left: 3px; width: 26px; height: 26px; border-radius: 50%; background: #fff; box-shadow: 0 1px 3px rgba(0,0,0,.25); transition: transform .2s; transform: translateX(' + (rem ? '20px' : '0') + ')' };
    const nt = NT[lang] || NT.fr; const ntm = s.nt ?? APP.get('nt'); const donateUrl = (window.SM_CONFIG && SM_CONFIG.donateUrl) || ''; return { ...reading, ...reminder, donateUrl, hasDonate: /^https:\/\//.test(donateUrl), nt, fillCities: (el) => { const L = SM_CITY_LIST(); el.innerHTML = L.map(c => '<option value="' + c.id + '">' + c.name + '</option>').join(''); const on = L.find(c => c.on); if (on) el.value = on.id; }, pickCity: (e) => this.setState({ city: e.target.value }), ntOpts: ['trois', 'yer', 'deux'].map((k, i) => ({ title: nt.o[i], on: k === ntm, pick: () => this.setState({ nt: k }), style: RADIO(k === ntm), dot: DOT(k === ntm) })), themeClass: 'th-' + mode, isParch: mode === 'parchemin', rootStyle: rootVars(mode), t, hasDraft: !!t.draft, fs,
      smaller: () => this.setState({ fs: Math.max(20, fs - 2) }), bigger: () => this.setState({ fs: Math.min(40, fs + 2) }),
      modes: ['clair', 'sombre', 'texte', 'parchemin'].map(m => { const th = THEMES[m]; const on = m === mode; return { name: t[m], on, pick: () => this.setState({ mode: m }), style: 'height: 72px; min-width: 0; border-radius: 16px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; padding: 0 2px; font-family: inherit; background: ' + th['--bg'] + '; color: ' + th['--text'] + '; border: ' + (on ? '2px solid var(--accent-line)' : '1px solid ' + th['--line2']) }; }),
      langs: LANGS.map(l => ({ ...l, on: l.id === lang, pick: () => this.setState({ lang: l.id }), style: card(l.id === lang) })),
      places: [t.israel, t.diaspora].map((n, i) => ({ name: n, on: i === place, pick: () => this.setState({ place: i }), style: card(i === place).replace('min-height: 60px', 'min-height: 48px') + '; font-size: 15px; font-weight: 600' })),
      fonts: FONTS.map((f, i) => ({ ...f, desc: (t.fontDesc || {})[f.id] || '', on: f.id === font, pick: () => this.setState({ font: f.id }),
        style: 'width: 100%; min-height: 60px; display: flex; align-items: center; gap: 12px; padding: 8px 14px; border: none; font-family: Inter, sans-serif; color: var(--text); background: ' + (f.id === font ? 'var(--hl)' : 'transparent') + '; ' + (i ? 'border-top: 1px solid var(--line);' : ''),
        dot: 'flex-shrink: 0; width: 20px; height: 20px; border-radius: 50%; box-sizing: border-box; ' + (f.id === font ? 'border: 6px solid var(--accent-line);' : 'border: 2px solid var(--line2);'),
        sample: 'flex-shrink: 0; font-family: ' + f.css + '; font-size: 21px; color: var(--text)' })),
      previewStyle: 'margin: 0; font-family: ' + F.css + '; font-size: ' + fs + 'px; line-height: ' + (mode === 'texte' ? 2.05 : 1.9) + '; transition: font-size .2s',
      previewT: 'margin: 4px 0 0; font-family: ' + F.css + '; font-size: ' + (fs - 3) + 'px; line-height: 1.9; color: var(--soft)' };
  }
}

return Component;
  }
};
