/* Shnayim Mikra — les données embarquées (web/data/, écrites par tools/construit_donnees.js).
   L'application s'ouvre aussi depuis un fichier (file://, WebView) : les données sont des scripts qui
   appellent SM_DATA(nom, contenu), chargés par une balise <script>, les lectures au démarrage, le texte
   de chaque livre à la demande. Aucun réseau : tout est dans l'application. */
(function () {
  const lues = {}, attentes = {};
  window.SM_DATA = function (nom, contenu) { lues[nom] = contenu; };
  window.SM_DONNEES = {
    /** Le contenu déjà chargé, ou undefined. */
    lue: (nom) => lues[nom],
    /** Charge data/<nom>.js une seule fois : Promise du contenu. */
    charge: function (nom) {
      if (lues[nom]) return Promise.resolve(lues[nom]);
      if (!attentes[nom]) attentes[nom] = new Promise((ok, ko) => {
        const s = document.createElement('script'); s.src = 'data/' + nom + '.js'; s.async = true;
        s.onload = () => (lues[nom] ? ok(lues[nom]) : ko(new Error('données vides : ' + nom)));
        s.onerror = () => { delete attentes[nom]; ko(new Error('données absentes : ' + nom)); };
        document.head.appendChild(s);
      });
      return attentes[nom];
    }
  };
})();
