# 7. Mise en place de 21st.dev UI Build (Claude Code)

Skill de 21st.dev pour transformer une description d'écran en interface, dans un projet de code existant.

**Limite :** le catalogue 21st.dev contient des composants React/shadcn pour le web. Très adapté à une web app (Next.js par ex.), beaucoup moins à une app mobile native (React Native).

## 1. Prérequis
- Node.js
- Le dossier du projet de l'app
- Un compte sur 21st.dev

## 2. Installer le skill
Depuis le dossier du projet, puis choisir Claude Code :
```sh
npx skills add https://github.com/21st-dev/skill --skill 21st-ui-build
```
Pour installer aussi les skills voisins (`21st-ui-explore`, `21st-ui-review`, etc.) :
```sh
npx @21st-dev/cli install-skill
```

## 3. Se connecter (au choix)
- Session : `npx @21st-dev/cli login` (ouvre le navigateur, enregistre un jeton dans `~/.config/21st/auth.json`)
- Clé API `21st_sk_…` depuis https://21st.dev/mcp, via `--api-key` ou les variables `TWENTYFIRST_TOKEN` / `API_KEY_21ST`

## 4. Optionnel : serveur MCP pour Claude Code
```sh
npx @21st-dev/cli@latest init --client claude --write
```
Puis coller la clé API créée sur https://21st.dev/mcp.

## 5. Vérifier
```sh
21st whoami   # compte connecté
21st usage    # niveau, quota, génération IA activée ou non
```

## 6. Préparer le projet
À la racine :
```sh
21st init --design-context
```

## Exemple de demande dans Claude Code
> Utilise 21st UI Build pour créer l'écran Lecteur de la direction [A, B ou C] : lecture verset, verset, Targoum, défilement automatique avec vitesse réglable et Targoum plus lent (même vitesse, −20 %, −40 %). Réutilise nos composants et nos couleurs, et vérifie le rendu sur mobile et sur ordinateur.

## Sources
- https://github.com/21st-dev/skill
- https://21st.dev/mcp.md
- https://help.21st.dev/cli
