#!/bin/bash
# Hook de démarrage des sessions Claude Code dans le cloud.
# Il prépare ce qu'il faut pour travailler tout de suite :
#   1. les dépendances de test (npm : @hebcal/core et @hebcal/leyning) ;
#   2. les données de l'application (web/data/, non suivies par git), pour qu'elle s'ouvre.
# Chaque étape est sautée si rien de ce qui la décide n'a changé depuis sa dernière réussite.
# Les outils Python (tools/*.py) n'utilisent que la bibliothèque standard : rien à installer.
set -euo pipefail

# Seulement dans une session cloud : sur un ordinateur, on installe à la main (README).
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-.}"

# Tout ce qui s'affiche part sur la sortie d'erreur : la sortie standard d'un hook entre dans la conversation.
exec 1>&2

# 1. Dépendances de test. L'empreinte est dans node_modules : elle disparaît avec les paquets.
hashes=node_modules/.session-start.sha256
if ! sha256sum --check --status "$hashes" 2>/dev/null; then
  # L'ancienne empreinte part d'abord : une installation ratée sera refaite la prochaine fois.
  rm -f "$hashes"
  echo "session-start : npm install"
  npm install --no-audit --no-fund
  sha256sum .claude/hooks/session-start.sh package.json package-lock.json > "$hashes" || rm -f "$hashes"
fi

# 2. Données de l'application, écrites par tools/construit_donnees.js à partir de data/ (sans réseau, moins
#    d'une seconde). L'empreinte couvre les fichiers de data/ présents aujourd'hui : un fichier ajouté ou
#    retiré la change aussi. Elle est dans web/data, que l'outil vide avant d'écrire.
donnees=web/data/.session-start.sha256
actuel="$(sha256sum .claude/hooks/session-start.sh tools/construit_donnees.js web/lecture.js web/vendor/kosher-zmanim-0.9.0.min.js data/*.json)"
if [ "$actuel" != "$(cat "$donnees" 2>/dev/null)" ]; then
  echo "session-start : données de l'application (web/data)"
  node tools/construit_donnees.js
  printf '%s\n' "$actuel" > "$donnees"
fi
