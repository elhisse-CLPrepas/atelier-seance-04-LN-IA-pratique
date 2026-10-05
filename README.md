# Pack pratique de la séance 04 LN-IA
Lundi 05 octobre 2026 — Module 01 — Challenge 100 Jours Relance Automne.
Prof. Abderrahman EL HISSE. Version pratique 2.0. Horaire à confirmer.

## Commencer
1. Lire les guides Word dans documents.
2. Ouvrir mon-dossier-challenge-100j/DEMARRER-ICI.html pour explorer le modèle rempli.
3. Ouvrir le dossier du pack dans VS Code. Dans le terminal :
```sh
cd mini-site-seance-04
npm ci
npm run dev -- --port 5174
```
Ouvrir http://localhost:5174. Le port 5173 est réservé au site de l’atelier séance 04. Node 24 LTS recommandé ; compatibilité minimale indiquée dans package.json.
4. Copier PROMPT-PILOTAGE-CODEX.md dans Codex si vous souhaitez poursuivre la production. Un prompt va dans Codex, pas dans le terminal.

## Accès à distance
Le mini-site est publié sur GitHub Pages : [https://elhisse-clprepas.github.io/atelier-seance-04-LN-IA-pratique/](https://elhisse-clprepas.github.io/atelier-seance-04-LN-IA-pratique/).
Dépôt : [atelier-seance-04-LN-IA-pratique](https://github.com/elhisse-CLPrepas/atelier-seance-04-LN-IA-pratique).
Les saisies du carnet restent dans le navigateur de chaque utilisateur ; les travaux personnels ne sont pas publiés.

## Ce que contient le pack
- mini-site-seance-04 : site Vite avec sept vues, quinze écrans, démonstration, carnet exportable et neuf prompts V3.
- mon-dossier-challenge-100j : cas Nadia rempli, séances 01 à 04, trois livrables, versions, preuves et portfolio.
- documents : guide candidat et guide formateur en Word, avec leurs sources Markdown.
- sources-fournies : trois ZIP d’origine conservés comme provenance.
- docs : adaptations, déploiement et compte rendu de contrôle.
- .github/workflows : publication GitHub Pages du mini-site.

## Le résultat minimal de la séance
Une fiche courte corrigée et trois pièces associées : prompt réellement utilisé, preuve datée et engagement. Le guide complet, la page et le rapport de Nadia sont déjà fournis comme modèles. Il n’est pas demandé de refaire ces trois productions de zéro en 100 minutes.

## Faits et simulations
Nadia et ses données sont fictives. Les textes d’engagement, retours de binôme et parcours rétrospectifs sont des exemples préparés. La trace technique est réellement exécutée sur les fichiers livrés. La pratique personnelle et la validation humaine restent à effectuer.

## Après une modification du dossier ou des Word
Depuis la racine du pack :
```sh
node scripts/synchroniser-site.mjs
```
Cette commande met à jour la copie publique du dossier fictif, les Word et le ZIP téléchargeable. N’insérez jamais de données personnelles réelles dans ces emplacements. Vos fichiers réels restent dans travail-personnel, hors site public.

Puis depuis mini-site-seance-04 :
```sh
npm run check
npm run build
npm run preview
```
La compilation locale ne publie rien. Voir docs/DEPLOIEMENT.md.
