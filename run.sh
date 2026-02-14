#!/bin/bash

# Script d'installation et lancement de "Guess The Movie – Valentine Edition"
# Pour macOS & Linux

echo ""
echo "============================================================"
echo "   🎬 Guess The Movie - Valentine Edition"
echo "   Installation et Lancement"
echo "============================================================"
echo ""

# Vérifier si Python est installé
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    echo "Veuillez installer Python 3.8+ depuis https://python.org"
    exit 1
fi

echo "✓ Python détecté: $(python3 --version)"

# Créer un environnement virtuel (optionnel mais recommandé)
if [ ! -d "venv" ]; then
    echo ""
    echo "📦 Création d'un environnement virtuel..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✓ Environnement virtuel créé"
else
    echo ""
    echo "✓ Environnement virtuel existant trouvé"
    source venv/bin/activate
fi

# Installer les dépendances
echo ""
echo "📥 Installation des dépendances Streamlit..."
pip install -r requirements.txt

echo ""
echo "✓ Installation terminée !"
echo ""
echo "🚀 Lancement de l'application..."
echo "   → Ouvre http://localhost:8501 dans ton navigateur"
echo ""

# Lancer l'application
streamlit run app.py
