/* Textes des messages de la chaîne WhatsApp, dans les cinq langues.
   Entre accolades : ce que l'outil remplace (paracha, alyot, minutes…). Les *étoiles* donnent du gras dans WhatsApp.
   Les noms de parachiyot, d'alyot, de villes et les dates viennent de l'app (web/i18n). */
module.exports = {
  fr: {
    newWeek: '🗓 *Nouvelle paracha : {parasha}*\n{ref} · 7 alyot · environ {total} min en tout',
    today: '📖 Aujourd\'hui : {alyot} · environ {min} min',
    day: '📖 *{parasha}* — {alyot} · environ {min} min',
    and: ' et ',
    link: '🔗 Lire dans l\'app : {url}',
    react: '✅ Réagis à ce message quand c\'est fait',
    candles: '🕯 Allumage des bougies : {list}',
    shabbat: 'Chabbat Chalom', hag: '\'Hag Saméa\'h', rh: 'Chana Tova', yk: 'Gmar \'Hatima Tova',
    greet: '*{a} !*', greet2: '*{a} et {b} !*',
    eveTitle: '⏳ *Chabbat approche*',
    eveBody: 'Demain, les dernières alyot de {parasha} : {alyot} · environ {min} min.\nPas encore à jour ? Toute la paracha se lit en {total} min environ, et l\'app peut imprimer ce qu\'il te reste pour Chabbat.',
    stIntro: '🍂 *Avant Sim\'hat Torah*\nC\'est le moment de rattraper les parachiyot que tu n\'as pas terminées cette année.\nLa dernière paracha, {parasha}, commence ici {date}.',
    stWeek: '🗓 *Dernière paracha de l\'année : {parasha}*\n{ref} · 7 alyot · environ {total} min en tout\nÀ terminer avant Sim\'hat Torah ({date}).',
    dvar: '💬 *Dvar Torah*'
  },
  en: {
    newWeek: '🗓 *New parashah: {parasha}*\n{ref} · 7 aliyot · about {total} min in all',
    today: '📖 Today: {alyot} · about {min} min',
    day: '📖 *{parasha}* — {alyot} · about {min} min',
    and: ' and ',
    link: '🔗 Read in the app: {url}',
    react: '✅ React to this message when you\'re done',
    candles: '🕯 Candle lighting: {list}',
    shabbat: 'Shabbat Shalom', hag: 'Chag Sameach', rh: 'Shanah Tovah', yk: 'Gmar Chatimah Tovah',
    greet: '*{a}!*', greet2: '*{a} and {b}!*',
    eveTitle: '⏳ *Shabbat is coming*',
    eveBody: 'Tomorrow, the last aliyot of {parasha}: {alyot} · about {min} min.\nNot up to date yet? The whole parashah takes about {total} min, and the app can print what you have left for Shabbat.',
    stIntro: '🍂 *Before Simchat Torah*\nNow is the time to catch up on the parashiyot you did not finish this year.\nThe last parashah, {parasha}, starts here on {date}.',
    stWeek: '🗓 *Last parashah of the year: {parasha}*\n{ref} · 7 aliyot · about {total} min in all\nTo finish before Simchat Torah ({date}).',
    dvar: '💬 *Dvar Torah*'
  },
  es: {
    newWeek: '🗓 *Nueva parashá: {parasha}*\n{ref} · 7 aliot · alrededor de {total} min en total',
    today: '📖 Hoy: {alyot} · alrededor de {min} min',
    day: '📖 *{parasha}* — {alyot} · alrededor de {min} min',
    and: ' y ',
    link: '🔗 Leer en la app: {url}',
    react: '✅ Reacciona a este mensaje cuando termines',
    candles: '🕯 Encendido de velas: {list}',
    shabbat: 'Shabat Shalom', hag: 'Jag Sameaj', rh: 'Shaná Tová', yk: 'Gmar Jatimá Tová',
    greet: '*¡{a}!*', greet2: '*¡{a} y {b}!*',
    eveTitle: '⏳ *Se acerca Shabat*',
    eveBody: 'Mañana, las últimas aliot de {parasha}: {alyot} · alrededor de {min} min.\n¿Todavía no estás al día? Toda la parashá se lee en unos {total} min, y la app puede imprimir lo que te falta para Shabat.',
    stIntro: '🍂 *Antes de Simjat Torá*\nEs el momento de ponerte al día con las parashiot que no terminaste este año.\nLa última parashá, {parasha}, empieza aquí el {date}.',
    stWeek: '🗓 *Última parashá del año: {parasha}*\n{ref} · 7 aliot · alrededor de {total} min en total\nPara terminar antes de Simjat Torá ({date}).',
    dvar: '💬 *Dvar Torá*'
  },
  he: {
    newWeek: '🗓 *פרשה חדשה: {parasha}*\n{ref} · 7 עליות · כ־{total} דק׳ בסך הכול',
    today: '📖 היום: {alyot} · כ־{min} דק׳',
    day: '📖 *{parasha}* — {alyot} · כ־{min} דק׳',
    and: ' ו',
    link: '🔗 לקריאה באפליקציה: {url}',
    react: '✅ סמנו את ההודעה כשסיימתם',
    candles: '🕯 הדלקת נרות: {list}',
    shabbat: 'שבת שלום', hag: 'חג שמח', rh: 'שנה טובה', yk: 'גמר חתימה טובה',
    greet: '*{a}!*', greet2: '*{a} ו{b}!*',
    eveTitle: '⏳ *שבת מתקרבת*',
    eveBody: 'מחר, העליות האחרונות של {parasha}: {alyot} · כ־{min} דק׳.\nעוד לא הספקתם? כל הפרשה נקראת בכ־{total} דק׳, ובאפליקציה אפשר להדפיס את מה שנשאר לשבת.',
    stIntro: '🍂 *לפני שמחת תורה*\nזה הזמן להשלים את הפרשיות שלא סיימתם השנה.\nהפרשה האחרונה, {parasha}, מתחילה כאן ב{date}.',
    stWeek: '🗓 *הפרשה האחרונה של השנה: {parasha}*\n{ref} · 7 עליות · כ־{total} דק׳ בסך הכול\nלסיים לפני שמחת תורה ({date}).',
    dvar: '💬 *דבר תורה*'
  },
  /* Tounsi (judéo-arabe tunisien en lettres hébraïques) : brouillon à faire relire, comme les textes de l'app */
  tn: {
    newWeek: '🗓 *פרשה ג׳דידה: {parasha}*\n{ref} · 7 עליות · תקריב {total} דק׳ פי אלכל',
    today: '📖 אליום: {alyot} · תקריב {min} דק׳',
    day: '📖 *{parasha}* — {alyot} · תקריב {min} דק׳',
    and: ' ו',
    link: '🔗 אקרא פי אלתטביקה: {url}',
    react: '✅ עלם עלא אלמסאג׳ הד׳א כי תכמל',
    candles: '🕯 תשעיל אלשמע: {list}',
    shabbat: 'שבת שלום', hag: 'חג שמח', rh: 'שנה טובה', yk: 'גמר חתימה טובה',
    greet: '*{a}!*', greet2: '*{a} ו{b}!*',
    eveTitle: '⏳ *שבת קרבת*',
    eveBody: 'ע׳דוה, אלעליות אלאכ׳רין מתאע {parasha}: {alyot} · תקריב {min} דק׳.\nמאזלת מא כמלתש? אלפרשה אלכל תתקרא פי תקריב {total} דק׳, ואלתטביקה תנג׳ם תטבעלך אלבאקי לשבת.',
    stIntro: '🍂 *קבל שמחת תורה*\nהד׳א וקת אלתדארך: כמל אלפרשיות אלי מא כמלתהמש אלעאם הד׳א.\nאלפרשה אלאכ׳רה, {parasha}, תבדא הנא נהאר {date}.',
    stWeek: '🗓 *אלפרשה אלאכ׳רה מתאע אלעאם: {parasha}*\n{ref} · 7 עליות · תקריב {total} דק׳ פי אלכל\nתכמלהא קבל שמחת תורה ({date}).',
    dvar: '💬 *דבר תורה*'
  }
};
