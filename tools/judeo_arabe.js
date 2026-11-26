#!/usr/bin/env node
/* Écrit en lettres hébraïques (judéo-arabe) un texte arabe dialectal écrit en lettres arabes.
   Sert à convertir les brouillons de traduction ; le résultat reste à relire par un locuteur.
   Conventions : ج ג׳ · خ כ׳ · غ ע׳ · ث ת׳ · ذ ד׳ · ض צ׳ · ظ ט׳ ; les mots hébreux reprennent leur orthographe hébraïque
   (שבת, פרשה, עליה, תרגום…) ; lettres finales ך ם ן ף ץ en fin de mot. */
const HEBREW_WORDS = [
  ['سمحات توراه', 'שמחת תורה'], ['يشار كوّاح', 'יישר כח'], ['شبات', 'שבת'], ['شالوم', 'שלום'],
  ['براشيوت', 'פרשיות'], ['براشا', 'פרשה'], ['عليوت', 'עליות'], ['عليا', 'עליה'], ['ترجوم', 'תרגום'],
  ['حوماش', 'חומש'], ['توراه', 'תורה'], ['أونقلوس', 'אונקלוס'], ['يروشلمي', 'ירושלמי'],
  ['بمدبار', 'במדבר'], ['ديبون', 'דיבן'], ['بتوحا', 'פתוחה'], ['ستوما', 'סתומה'], ['طعميم', 'טעמים'], ['إسرائيل', 'ישראל'], ['سفاريا', 'ספריא']
];
const MAP = { 'ا': 'א', 'أ': 'א', 'إ': 'א', 'آ': 'א', 'ٱ': 'א', 'ب': 'ב', 'ت': 'ת', 'ث': 'ת׳', 'ج': 'ג׳', 'ح': 'ח', 'خ': 'כ׳', 'د': 'ד', 'ذ': 'ד׳', 'ر': 'ר', 'ز': 'ז',
  'س': 'ס', 'ش': 'ש', 'ص': 'צ', 'ض': 'צ׳', 'ط': 'ט', 'ظ': 'ט׳', 'ع': 'ע', 'غ': 'ע׳', 'ف': 'פ', 'ق': 'ק', 'ك': 'כ', 'ل': 'ל', 'م': 'מ', 'ن': 'נ', 'ه': 'ה', 'و': 'ו', 'ي': 'י',
  'ة': 'ה', 'ى': 'א', 'ؤ': 'ו', 'ئ': 'י', 'ء': '', 'ڨ': 'ג', 'ڤ': 'ב׳', 'پ': 'פ', '،': ',', '؟': '?', '؛': ';' };
const FINAL = { 'כ': 'ך', 'מ': 'ם', 'נ': 'ן', 'פ': 'ף', 'צ': 'ץ' };
function judeoArabe(s) {
  s = String(s);
  HEBREW_WORDS.forEach(([a, h]) => { s = s.split(a).join(h); });
  s = s.replace(/ئي/g, 'אי').replace(/ـ /g, '־').replace(/ـ/g, '').replace(/[ً-ْٰ]/g, '');   /* voyelles brèves, chadda */
  s = s.replace(/[؀-ۿ]/g, (c) => (c in MAP ? MAP[c] : c));
  /* lettres finales : dernière lettre d'un mot (avant un éventuel ׳) */
  return s.replace(/([כמנפצ])(׳?)(?![א-ת׳])/g, (m, l, g) => FINAL[l] + g);
}
/* Variante : le texte reste en lettres arabes, seuls les termes religieux hébreux passent en lettres hébraïques.
   Un préfixe arabe (article, préposition) reste attaché au mot par un trait : البراشا → الـפרשה, لشبات → لـשבת. */
function termesHebreux(s) {
  s = String(s).split('عطروت وديبون').join('עטרות ודיבן');
  HEBREW_WORDS.filter(([a]) => a !== 'إسرائيل' && a !== 'سفاريا' && a !== 'ديبون').forEach(([a, h]) => {
    s = s.replace(new RegExp('(^|[^\\u0600-\\u06FF])((?:و)?(?:[بفكل])?(?:ال|ل)?)' + a, 'g'), (m, before, pre) => before + (pre ? pre + 'ـ' : '') + h);
  });
  return s;
}
module.exports = { judeoArabe, termesHebreux };
if (require.main === module) console.log(judeoArabe(process.argv.slice(2).join(' ')));
