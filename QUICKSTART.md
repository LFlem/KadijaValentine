# ⚡ Quick Start Guide (5 minutes)

## 🚀 Pour Commencer TOUT DE SUITE

### Étape 1: Ouvre une fenêtre de terminal

**Windows:**
- Ouvre l'Explorateur
- Navigue à: `C:\Users\myhan\Desktop\Mes Projets\gessmouvie`
- Clique droit → "Ouvrir dans un terminal"

**macOS/Linux:**
- Ouvre Terminal
- `cd ~/Desktop/Mes\ Projets/gessmouvie`

### Étape 2: Lance l'app (choisis une méthode)

**Méthode A - Ultra Rapide (Windows):**
```bash
run.bat
```

**Méthode B - Ultra Rapide (macOS/Linux):**
```bash
./run.sh
```

**Méthode C - Manuel:**
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Étape 3: Joue ! ✨

L'app s'ouvre à:
```
http://localhost:8501
```

Tapez les réponses, accumule des fleurs 🌸 et des chocolats 🍫 !

---

## 📦 Qu'est-ce qui est inclus ?

```
✅ app.py              - L'app complète prête à lancer
✅ 10 Questions        - Avec indices et descriptions
✅ Design Mignon       - Palette rose/violet Saint-Valentin
✅ Système de Score    - Fleurs 🌸 et Chocolats 🍫
✅ Scripts de Lancement - run.bat (Windows) + run.sh (Mac/Linux)
✅ Configuration       - .streamlit/config.toml
✅ Documentation       - README.md, GUIDE.md, DEPLOYMENT.md, etc.
```

---

## 📚 Fichiers Importants

| Fichier | Utilité |
|---------|---------|
| `app.py` | ⭐ L'application principale |
| `requirements.txt` | Dépendances à installer |
| `README.md` | Documentation générale |
| `GUIDE.md` | Guide d'utilisation complet |
| `DEPLOYMENT.md` | Comment déployer en ligne |
| `QUESTIONS.md` | Détail de chaque question |
| `IMPROVEMENTS.md` | Idées pour améliorer |
| `.streamlit/config.toml` | Configuration Streamlit |

---

## 🎮 Comment Joueur ?

1. **Accueil** → Clique "Commencer le quiz"
2. **Question** → Lis l'indices 🎬, lis la description 💭
3. **Réponse** → Clique sur le film que tu penses
4. **Feedback** → Voir si c'était correct ✅ ou ❌
5. **Score** → Accumule fleurs 🌸 et chocolats 🍫
6. **Fin** → Voir ton résultat et rejouer 🔄

---

## 🎯 Les 10 Films

1. 🚿 **Psycho** - Nuit cauchemardesque à l'hôtel
2. 🧛 **Dracula (1992)** - L'amour selon celui qui abhorre la lumière
3. 🛥️ **Titanic** - Romance sur une baignoire qui coule
4. 💍 **Seigneur des Anneaux** - Une créature marche longtemps
5. 🤡 **Joker** - Le sourire d'un homme oublié
6. 🌅 **Before Sunrise** - Deux étrangers parlent jusqu'à l'aube
7. 🏢 **The Apartment** - Un bureau devient un petit hôtel
8. 🏝️ **L'Avventura** - Femme disparaît, personne n'a l'air concerné
9. 🚀 **2001: A Space Odyssey** - Homme et machine parlent de l'infini
10. 🎈 **Le Ballon Rouge** - Enfant et ballon amis de Paris

---

## 🎨 Les Couleurs

| Couleur | Code | Utilité |
|---------|------|---------|
| Rose Principal | #d63384 | Titres, accents |
| Fond Clair | #fff5f7 | Arrière-plan principal |
| Violet Clair | #f0e6ff | Fond des containers |
| Texte Sombre | #212529 | Texte lisible |

---

## ❓ Questions Fréquentes

### Ça marche sur Mac ?
✅ Oui! Utilise `./run.sh` au lieu de `run.bat`

### Ça marche sur mobile ?
✅ Oui! Streamlit fonctionne sur tous les appareils

### Faut installer Python ?
✅ Oui, Python 3.8+ requis sur ta machine

### Je peux partager avec des amis ?
✅ Oui! Déploie sur Streamlit Cloud et donne-leur le lien

### Je peux ajouter mes propres films ?
✅ Oui! Édite le `app.py` et ajoute des questions

### C'est gratuit ?
✅ Oui! Tout est open-source et gratuit

---

## 🚨 Dépannage Express

### "Python not found"
→ Installe Python depuis https://python.org

### "Module not found: streamlit"
→ Exécute: `pip install -r requirements.txt`

### Le port 8501 est utilisé
→ Utilise: `streamlit run app.py --server.port 8502`

### L'app ne se lance pas
→ Vérifier le terminal pour les erreurs

---

## 🌟 Prochaines Étapes

- [ ] 1. Lancer l'app et jouer
- [ ] 2. Lire [GUIDE.md](GUIDE.md) pour comprendre le système
- [ ] 3. Consulter [DEPLOYMENT.md](DEPLOYMENT.md) pour mettre en ligne
- [ ] 4. Lire [IMPROVEMENTS.md](IMPROVEMENTS.md) pour améliorer
- [ ] 5. Partager avec tes ami(e)s ! 💝

---

## 🎬 Commandes Utiles

```bash
# Lancer l'app
streamlit run app.py

# Lancer avec port personnalisé
streamlit run app.py --server.port 8502

# Vérifier la version de Streamlit
pip show streamlit

# Mettre à jour Streamlit
pip install --upgrade streamlit

# Afficher l'aide
streamlit --help
```

---

## 📱 Sur Téléphone

1. Lance l'app sur ton PC
2. Regarde l'URL (ex: `http://192.168.x.x:8501`)
3. Sur ton téléphone, ouvre cette URL dans le navigateur
4. Joue ! 📱✨

---

**C'est tout ! Maintenant... À toi de jouer ! 🎬💕**

Besoin d'aide? Lis les autres fichiers .md ou modifie `app.py` directement !
