/* Shnayim Mikra — mini runtime: templates {{ }}, sc-for, sc-if, DOM patching, router, settings */
(function () {
  const DEF = { mode: 'clair', lang: 'fr', font: 'frank', fs: 25, place: 0, city: null, nt: 'deux', onboarded: false };
  let data; try { data = Object.assign({}, DEF, JSON.parse(localStorage.getItem('sm.settings') || '{}')); } catch (e) { data = Object.assign({}, DEF); }
  const APP = window.APP = {
    get: (k) => (k === 'done' && window.SM_DONE) ? SM_DONE.get() : data[k],
    set: (k, v) => { if (k === 'done' && window.SM_DONE) { SM_DONE.set(v); return; } if (data[k] === v) return; data[k] = v; try { localStorage.setItem('sm.settings', JSON.stringify(data)); } catch (e) {} if (k === 'mode') rerenderWithProps(); if (k === 'place') { schedule(); if (window.SM_REFRESH) SM_REFRESH(); } if (k === 'city' || k === 'nt') schedule(); }
  };
  const SYNC = ['mode', 'lang', 'font', 'fs', 'place', 'city', 'nt', 'done'];

  window.DCLogic = class {
    constructor(props) { this.props = props; this.state = undefined; }
    setState(p) { if (typeof p === 'function') p = p(this.state); this.state = Object.assign({}, this.state || {}, p);
      SYNC.forEach(k => { if (p && k in p && p[k] !== undefined) APP.set(k, p[k]); }); schedule(); }
    forceUpdate() { schedule(); }
  };

  const whole = /^\{\{\s*([^}]+?)\s*\}\}$/;
  function look(path, scope) { path = path.trim(); if (path === 'true') return true; if (path === 'false') return false;
    if (/^-?\d+(\.\d+)?$/.test(path)) return Number(path); return path.split('.').reduce((o, k) => o == null ? undefined : o[k], scope); }
  function interp(str, scope) { return str.replace(/\{\{\s*([^}]+?)\s*\}\}/g, (_, p) => { const v = look(p, scope); return v == null ? '' : String(v); }); }
  function bind(el, type) { el.__bound = el.__bound || {}; if (el.__bound[type]) return; el.__bound[type] = true; el.addEventListener(type, (e) => { const h = el.__h && el.__h[type]; if (h) h(e); }); }

  let refs = [];
  function render(node, scope, out) {
    if (node.nodeType === 3) { out.push(document.createTextNode(interp(node.nodeValue, scope))); return; }
    if (node.nodeType !== 1) return;
    const tag = node.tagName.toLowerCase();
    if (tag === 'sc-for') { const m = (node.getAttribute('list') || '').match(whole); const list = m ? look(m[1], scope) : []; const as = node.getAttribute('as') || 'item';
      (list || []).forEach((it, i) => { const sc = Object.assign({}, scope, { [as]: it, $index: i }); node.childNodes.forEach(c => render(c, sc, out)); }); return; }
    if (tag === 'sc-if') { const m = (node.getAttribute('value') || '').match(whole); if (m && look(m[1], scope)) node.childNodes.forEach(c => render(c, scope, out)); return; }
    const svg = node.namespaceURI === 'http://www.w3.org/2000/svg';
    const el = svg ? document.createElementNS(node.namespaceURI, node.tagName) : document.createElement(tag);
    for (const a of Array.from(node.attributes)) {
      const m = a.value.match(whole);
      if (m) { const v = look(m[1], scope);
        if (/^on[A-Za-z]+$/.test(a.name) && (typeof v === 'function' || v == null)) { const type = a.name.slice(2).toLowerCase(); el.__h = el.__h || {}; el.__h[type] = v; bind(el, type); continue; }
        if (a.name === 'ref') { if (typeof v === 'function') refs.push([v, el]); continue; }
        if (a.name === 'value' && tag === 'input') { el.value = v == null ? '' : v; }
        if (v === false || v == null) continue; el.setAttribute(a.name, v === true ? 'true' : String(v));
      } else el.setAttribute(a.name, interp(a.value, scope));
    }
    const kids = []; node.childNodes.forEach(c => render(c, scope, kids)); kids.forEach(k => el.appendChild(k));
    out.push(el);
  }
  function same(o, n) { return o.nodeType === n.nodeType && (o.nodeType === 3 || o.tagName === n.tagName); }
  function patchChildren(parent, news) {
    const olds = Array.from(parent.childNodes);
    news.forEach((n, i) => { const o = olds[i]; if (!o) parent.appendChild(n); else if (same(o, n)) patchNode(o, n); else parent.replaceChild(n, o); });
    for (let i = news.length; i < olds.length; i++) parent.removeChild(olds[i]);
  }
  function patchNode(o, n) {
    n.__target = o;
    if (o.nodeType === 3) { if (o.nodeValue !== n.nodeValue) o.nodeValue = n.nodeValue; return; }
    for (const a of Array.from(o.attributes)) if (!n.hasAttribute(a.name)) o.removeAttribute(a.name);
    for (const a of Array.from(n.attributes)) if (o.getAttribute(a.name) !== a.value) o.setAttribute(a.name, a.value);
    if (o.tagName === 'INPUT' && document.activeElement !== o && n.value !== undefined && o.value !== n.value) o.value = n.value;
    o.__h = n.__h; if (n.__h) Object.keys(n.__h).forEach(t => bind(o, t));
    patchChildren(o, Array.from(n.childNodes));
  }

  const root = () => document.getElementById('app');
  let cur = null, tplEl = null, pending = false;
  function schedule() { if (pending) return; pending = true; requestAnimationFrame(() => { pending = false; draw(); }); }
  function draw() { if (!cur) return; refs = []; const vals = Object.assign({}, cur.props, { G: window.SM_G ? SM_G() : {} }, cur.renderVals()); const out = []; tplEl.childNodes.forEach(c => render(c, vals, out));
    patchChildren(root(), out); refs.forEach(([fn, el]) => fn(el.__target || el)); }
  function rerenderWithProps() { if (cur) { cur.props = Object.assign({}, cur.props, { mode: APP.get('mode') }); schedule(); } }

  const MAP = { Accueil: 'accueil', Lecteur: 'lecteur', Annee: 'annee', Reglages: 'reglages', Imprimer: 'imprimer', Bienvenue: 'bienvenue' };
  function mount(name) {
    const S = window.SCREENS[name] || window.SCREENS.accueil;
    if (cur && cur.componentWillUnmount) cur.componentWillUnmount();
    root().innerHTML = '';
    tplEl = document.createElement('div'); tplEl.innerHTML = S.tpl;
    const C = S.make(); cur = new C({ mode: APP.get('mode') });
    draw(); window.scrollTo(0, 0);
    if (cur.componentDidMount) cur.componentDidMount();
    document.title = S.title;
  }
  function route() { const h = location.hash.replace(/^#\/?/, ''); const name = window.SCREENS[h] ? h : (APP.get('onboarded') ? 'accueil' : 'bienvenue'); mount(name); }
  document.addEventListener('click', (e) => {
    const a = e.target.closest && e.target.closest('a[href]'); if (!a) return;
    const href = a.getAttribute('href');
    if (href.startsWith('#mode=')) { e.preventDefault(); APP.set('mode', href.slice(6)); return; }
    const m = href.match(/V2-([A-Za-z]+)/);
    if (m && MAP[m[1]]) { e.preventDefault(); const target = MAP[m[1]]; const q = href.match(/alya=(\d)/); const pq = href.match(/par=([^&]+)/); if (target === 'lecteur') { APP.set('par', pq ? (/^\d{4}-/.test(pq[1]) ? pq[1] : Number(pq[1])) : 0); APP.set('alya', q ? Number(q[1]) : null); } if (cur && document.title === 'Bienvenue' && target === 'accueil') APP.set('onboarded', true); location.hash = '#/' + target; return; }
    if (href === '#' || href === '') e.preventDefault();
  });
  window.addEventListener('hashchange', route);
  window.addEventListener('DOMContentLoaded', () => { route(); if (window.SM_REFRESH) setTimeout(() => SM_REFRESH(), 1500); });
  window.SM_RERENDER = schedule;
})();
