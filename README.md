# 🎬 Guess The Movie – Valentine Edition

Une application Streamlit adorable pour deviner les films avec un thème Saint-Valentin ! 💝

## 🎯 Concept

Devinez 20 films à partir d'indices cryptiques, d'emojis et de descriptions humoristiques. Chaque bonne réponse = 1 fleur 🌸, et chaque 3 bonnes réponses = 1 chocolat 🍫.

## 📋 Films du Quiz (20 questions)

1. **Psycho** | 2. **Dracula (1992)** | 3. **Titanic** | 4. **Le Seigneur des Anneaux** | 5. **Inception**
6. **Before Sunrise** | 7. **The Apartment** | 8. **Seul au Monde** | 9. **Joker** | 10. **Interstellar**
11. **A Clockwork Orange** | 12. **Forrest Gump** | 13. **Le Ballon Rouge** | 14. **2001: A Space Odyssey** | 15. **Spirited Away**
16. **The Shining** | 17. **Fight Club** | 18. **Kung Fu Panda** | 19. **L'Avventura** | 20. **Amélie**

## 🚀 Installation et Lancement

### Prérequis
- Python 3.8 ou supérieur
- pip

### Étapes

1. **Cloner ou télécharger le repo**
   ```bash
   cd "chemin/vers/gessmouvie"
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'application**
   ```bash
   streamlit run app.py
   ```

L'application s'ouvrira dans votre navigateur par défaut à `http://localhost:8501`.

## ✨ Fonctionnalités

✅ **Écran d'accueil** - Présentation mignonne avec contexte  
✅ **Quiz interactif** - 20 questions avec indices variés (emoji, description, minimaliste)  
✅ **Système de score** - Fleurs et chocolats en temps réel  
✅ **Mélange aléatoire** - Questions et réponses dans un ordre différent à chaque partie  
✅ **Écran final** - Résumé des résultats avec option pour rejouer  
✅ **Historique des réponses** - Voir tes réponses détaillés  
✅ **Design cute** - Palette douce rose/violet avec emojis  

## 🎨 Design

- **Palette de couleurs** : Rose pastel (#d63384), Beige, Violet clair
- **Emojis** : Utilisés partout pour créer une atmosphère mignonne
- **Responsive** : Fonctionne sur desktop et mobile

## 📦 Déploiement sur Streamlit Cloud

1. Pousse ton code sur GitHub
2. Va sur [Streamlit Cloud](https://streamlit.io/cloud)
3. Connecte ton repo GitHub
4. Lance l'app ! 🚀

## 🛠️ Structure du Code

```
app.py
├── Configuration Streamlit
├── CSS personnalisé
├── Base de données des questions
├── Session State
├── Fonctions d'initialisation
├── Page d'accueil
├── Page du quiz
└── Page finale
```

## 💡 Personnalisation

Tu peux facilement ajouter plus de questions en modifiant la liste `MOVIES` dans `app.py` :

```python
{
    "id": 11,
    "title": "Mon Film Préféré",
    "hint": "🎬 🎭 🎪",
    "description": "Un indice cool sur le film",
    "options": ["Mon Film Préféré", "Autre Film", "Autre Film 2"],
}
```

## 📝 Licence

Libre d'utilisation pour usage personnel et éducatif.

## 💝 Bon amusement !

Prêt à tester tes connaissances cinématographiques ? C'est parti ! 🎭✨
