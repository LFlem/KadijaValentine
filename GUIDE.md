# 🎬 Guide Complet – Guess The Movie Valentine Edition

## 📱 Comment Jouer

### Écran d'Accueil
- Lis le contexte du jeu
- Clique sur **"Commencer le quiz"** pour démarrer

### Quiz
- Lis l'indice (emojis cryptiques)
- Lis la description humoristique
- Clique sur le film que tu penses être correct
- Reçois un feedback immédiat ✅ ou ❌
- Clique sur **"Question suivante"** pour continuer

### Système de Scoring
- 🌸 **1 fleur** = 1 bonne réponse
- 🍫 **1 chocolat** = 3 bonnes réponses cumulées
- Ton score s'affiche en temps réel pendant le quiz

### Écran Final
- Vois ton résultat final
- Consulte tes réponses détaillées (section "Voir tes réponses")
- Clique sur **"Rejouer"** pour retenter ta chance !

---

## 🚀 Installation Rapide

### Option 1 : Script Automatique (Recommandé)

**Windows :**
```bash
double-clic sur run.bat
```

**macOS/Linux :**
```bash
chmod +x run.sh
./run.sh
```

### Option 2 : Installation Manuelle

1. **Ouvre un terminal** dans le dossier du projet
2. **Crée un environnement virtuel** (optionnel mais recommandé)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate.bat
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Installe les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Lance l'application**
   ```bash
   streamlit run app.py
   ```

---

## 🎓 Fonctionnement Technique

### Structure du Code

```python
app.py
├── Configuration Streamlit (thème, icône, layout)
├── CSS Personnalisé (couleurs rose/violet, design cute)
├── Base de Données (12 films avec indices et descriptions)
├── Session State (gestion de l'état du jeu)
├── Fonctions Utilitaires
│   ├── start_quiz() → Initialise le jeu
│   ├── reset_game() → Réinitialise tout
│   ├── update_score() → Calcule fleurs & chocolats
├── Page Accueil (home)
├── Page Quiz (questions interactives)
└── Page Finale (résumé & rejeu)
```

### Gestion de l'État avec `session_state`

L'app utilise `st.session_state` pour mémoriser:
- ✓ La progression dans les 20 questions
- ✓ Le score courant
- ✓ Les réponses de l'utilisateur
- ✓ L'état du jeu (accueil / quiz / fin)

---

## 🎨 Personnalisation

### Ajouter des Questions

Modifie la liste `MOVIES` dans `app.py` :

```python
{
    "id": 11,
    "title": "Titre du Film",
    "hint": "🎭 🎬 🎪",  # Emojis cryptiques
    "description": "Une description humoristique et détournée",
    "options": ["Film Correct", "Faux Film 1", "Faux Film 2"],
}
```

### Changer les Couleurs

Modifie les couleurs dans `.streamlit/config.toml` :

```toml
[theme]
primaryColor = "#d63384"           # Rose principal
backgroundColor = "#fff5f7"        # Fond très clair
secondaryBackgroundColor = "#f0e6ff" # Fond conteneurs
textColor = "#212529"              # Texte sombre
```

Ou directement dans le CSS du `app.py` :

```python
.title {
    color: #d63384;  # Modifier cette couleur
}
```

### Changer le Message Final

Cherche cette ligne dans `app.py` :

```python
"💝 Voici ce que tu as gagné pour notre premier date 💝"
```

---

## 🌐 Déploiement sur Streamlit Cloud

### Étapes

1. **Pousse le code sur GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Guess The Movie Valentine Edition"
   git push origin main
   ```

2. **Crée un compte sur [Streamlit Cloud](https://streamlit.io/cloud)**

3. **Lance une nouvelle app**
   - Clique "New app"
   - Sélectionne ton repo GitHub
   - Choisis la branche `main`
   - Indique le path: `app.py`

4. **L'app est live !** 🚀

### URL de Déploiement
Une fois déployée, tu auras une URL du type:
```
https://nom-app.streamlit.app
```

---

## ⚙️ Configuration DNS pour Domaine Personnalisé

Si tu veux un domaine personnalisé (ex: `guessthemovie.com`):

1. Dans Streamlit Cloud → Settings
2. Ajoute un CNAME DNS pointant vers `cname.streamlitapp.com`
3. Attends 24-48h pour propagation

---

## 🐛 Dépannage

### L'app ne démarre pas
```bash
# Vérifier Python
python --version

# Vérifier Streamlit
pip list | grep streamlit

# Réinstaller si nécessaire
pip install --upgrade streamlit
```

### Port 8501 déjà utilisé
```bash
# Utiliser un autre port
streamlit run app.py --server.port 8502
```

### Les questions se répètent
C'est normal ! Elles sont mélangés aléatoirement à chaque partie. 😊

---

## 📊 Statistiques des Questions

| # | Film | Difficulté | Indice Type |
|---|---|---|---|
| 1 | Psycho | Moyen | Visuel |
| 2 | Dracula (1992) | Difficile | Thématique |
| 3 | Titanic | Facile | Icônique |
| 4 | Seigneur des Anneaux | Moyen-Difficile | Narrative |
| 5 | Joker | Moyen | Personnage |
| 6 | Before Sunrise | Difficile | Ambiance |
| 7 | The Apartment | Moyen | Contexte |
| 8 | L'Avventura | Très Difficile | Absurde |
| 9 | 2001: A Space Odyssey | Difficile | Sci-Fi |
| 10 | Le Ballon Rouge | Facile | Visuel |

---

## 🎯 Améliorations Futures Possibles

- ✨ Ajouter des images (affiches, screenshots)
- 📊 Tracker les scores (base de données)
- 🏆 Leaderboard global
- 🎚️ Niveaux de difficulté
- 🌍 Support multilingue
- 🎵 Musique de fond
- ⏱️ Mode contre la montre

---

## 💝 Crédits

Développé avec ❤️ pour la Saint-Valentin 2026.  
Liste de films inspirée par "Films à voir dans une vie selon Kadija".

---

## 📞 Support

Questions ou bugs ? Tu peux:
- Vérifier le [code source](app.py)
- Consulter la [documentation Streamlit](https://docs.streamlit.io)
- Améliorer l'app sur GitHub

---

**Bon amusement et bonne Saint-Valentin ! 💕🎬**
