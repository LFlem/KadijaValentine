# 🚀 INSTRUCTIONS DE DÉPLOIEMENT

## Déploiement Local (Recommandé pour développement)

### Windows
```bash
# 1. Ouvre PowerShell dans le dossier du projet

# 2. Double-clic sur run.bat
# OU tapez :
run.bat

# 3. L'app s'ouvre automatiquement sur http://localhost:8501
```

### macOS / Linux
```bash
# 1. Ouvre Terminal dans le dossier du projet

# 2. Exécute:
chmod +x run.sh
./run.sh

# 3. L'app s'ouvre automatiquement sur http://localhost:8501
```

### Déploiement Manuel
```bash
# Installation des dépendances
pip install -r requirements.txt

# Lancement
streamlit run app.py
```

---

## Déploiement sur Streamlit Cloud (Gratuit & Facile)

### Étape 1 : Préparer ton repo GitHub

```bash
# Si tu n'as pas encore Git:
git config --global user.name "Ton Nom"
git config --global user.email "ton.email@example.com"

# Dans le dossier du projet:
git init
git add .
git commit -m "🎬 Guess The Movie - Valentine Edition"
git branch -M main
git remote add origin https://github.com/TONUSERNAME/gessmouvie.git
git push -u origin main
```

### Étape 2 : Créer un compte Streamlit Cloud

1. Va sur https://streamlit.io/cloud
2. Clique "Sign up with GitHub"
3. Autoriser Streamlit

### Étape 3 : Déployer l'app

1. Clique "New app"
2. Remplis:
   - **Repository**: `TONUSERNAME/gessmouvie`
   - **Branch**: `main`
   - **Main file path**: `app.py`
3. Clique "Deploy"

### Étape 4 : Attendre le déploiement

- ⏳ Streamlit construit l'app (2-5 minutes)
- ✅ Un message "Your app is running" apparaît
- 🔗 L'URL de ton app s'affiche

### Ta nouvelle URL ressemblera à:
```
https://gessmouvie.streamlit.app
```

---

## Domaine Personnalisé (Optionnel, premium)

Si tu veux `tutmovie.com` au lieu de `streamlit.app`:

1. Achète un domaine (GoDaddy, Namecheap, etc.)
2. Dans Streamlit Cloud → Settings → Custom domain
3. Ajoute ton domaine
4. Suis les instructions DNS

---

## Mise à Jour de l'App en Ligne

L'app se met à jour **automatiquement** quand tu:

```bash
# Fais des changements localement
# Puis:
git add .
git commit -m "Description du changement"
git push origin main
```

Streamlit détecte le changement et redéploie automatiquement ! 🚀

---

## Variables d'Environnement (Streamlit Cloud)

Si tu veux ajouter des secrets:

1. Clique sur "..." → Settings
2. Secrets → Ajoute dans `.streamlit/secrets.toml`:

```toml
# Exemple:
MY_API_KEY = "abc123"
CONTACT_EMAIL = "contact@example.com"
```

Pour cette app, **aucun secret n'est requis** (app purement client-side).

---

## Monitoring & Logs

### Logs locaux
```bash
# Les logs s'affichent dans le terminal
```

### Logs Streamlit Cloud
1. Va sur ton app
2. Clique sur "..." (en haut à droite)
3. "View logs"

---

## Optimisations Possibles

### 1. Ajouter une favicon personnalisée
Crée `app.ico` et ajoute:
```python
st.set_page_config(page_icon="🎬")
```
✅ Déjà fait dans `app.py`

### 2. Ajouter du cache
```python
@st.cache_data
def load_questions():
    return MOVIES
```

### 3. Compresser les images (si tu en ajoutes)
Utilise [TinyPNG](https://tinypng.com) ou [Squoosh](https://squoosh.app)

---

## Dépannage

### L'app charge lentement
- Vérifier la connexion internet
- Streamlit Cloud peut être ralenti (demande une minute)

### Les boutons ne fonctionnent pas
- Vérifier que Streamlit est à jour:
```bash
pip install --upgrade streamlit
```

### Erreur "Module not found"
```bash
# Réinstalle les dépendances
pip install -r requirements.txt
```

### Cache plein (Streamlit Cloud)
- Les caches se vident automatiquement
- Si problème, redéploie

---

## Recommandations de Performance

✅ **Fait dans cette app:**
- Utilisation minimale de ressources
- Pas d'API externes
- CSS optimisé
- Code commenté et structuré

📝 **Peut être amélioré:**
- Ajouter du caching pour de plus grandes bases de données
- Optimiser les images si tu en ajoutes
- Utiliser `st.cache` pour les calculs lourds

---

## Sauvegardes & Backups

```bash
# Sauvegarder localement:
# Le dossier .git contient tout l'historique GitHub
# Tu peux aussi zipper le dossier complet

# Sur GitHub, tu as un backup automatique
# (Streamlit Cloud ne sauvegarde pas de données persistantes)
```

---

## Support & Ressources

- 📚 [Docs Streamlit](https://docs.streamlit.io)
- 🎥 [Tutoriels YouTube](https://youtube.com/streamlit)
- 💬 [Comunidad Discord](https://discord.gg/streamlit)
- 🐛 [Issues GitHub](https://github.com/streamlit/streamlit/issues)

---

## Checklist Pre-Launch

- [ ] Code testé localement
- [ ] Tous les fichiers committés (`git status` vide)
- [ ] `requirements.txt` à jour
- [ ] `.streamlit/config.toml` configuré
- [ ] Pas de secrets exposés
- [ ] README lisible
- [ ] App fonctionne en local

---

## Après le Déploiement

📊 **Partage ta création:**
- Twitter: `Check out my Streamlit app! 🎬 [lien]`
- LinkedIn: Démontre ton portfolio
- Amis: Jouez au quiz ! 💝

🌟 **Fier de ton app ?**
- Ajoute une ⭐ sur GitHub
- Partage sur Streamlit forums
- Améliore avec plus de questions

---

**Bonne chance ! Et n'hésite pas à personnaliser ! 🎯💕**
