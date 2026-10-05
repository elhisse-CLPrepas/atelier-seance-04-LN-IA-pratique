# Déployer le mini site sur GitHub Pages
Le dépôt doit contenir la racine de ce pack, y compris mini-site-seance-04 et .github/workflows. Nom proposé : atelier-seance-04-LN-IA-pratique.

1. Vérifier localement le mini-site avec npm ci, npm run check et npm run build.
2. Créer ou choisir le dépôt dans le compte voulu. Si un dépôt existe, préserver son contenu et son historique. Examiner git status et le diff puis sélectionner les fichiers utiles pour le commit.
3. Ne pas ajouter travail-personnel, secrets, fichiers candidats réels ni node_modules. Les copies publiques de Nadia ne contiennent que le cas fictif.
4. Dans Settings > Pages, choisir GitHub Actions. Le workflow vise main. Adapter ce nom si nécessaire.
5. Pousser les fichiers autorisés. Le workflow installe et compile dans mini-site-seance-04, puis publie mini-site-seance-04/dist.
6. Copier l’URL réellement affichée par GitHub. Tester les vues, le logo, les Word, le ZIP dossier et ses pages HTML.

La configuration base './' et les routes hash permettent un hébergement sous un nom de dépôt. Le site n’a pas de serveur ni d’API IA. Ne pas ouvrir l’index source Vite par double-clic ; lancer npm run dev ou utiliser la version déployée.
Le pack prépare la publication mais aucune publication distante n’est attestée par la compilation locale.
