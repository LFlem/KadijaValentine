@echo off
REM Script d'installation et lancement de "Guess The Movie – Valentine Edition"
REM Pour Windows

echo.
echo ============================================================
echo   🎬 Guess The Movie - Valentine Edition
echo   Installation et Lancement
echo ============================================================
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python n'est pas installé ou n'est pas dans le PATH
    echo Veuillez installer Python 3.8+ depuis https://python.org
    pause
    exit /b 1
)

echo ✓ Python détecté

REM Créer un environnement virtuel (optionnel mais recommandé)
if not exist "venv" (
    echo.
    echo 📦 Création d'un environnement virtuel...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo ✓ Environnement virtuel créé
) else (
    echo.
    echo ✓ Environnement virtuel existant trouvé
    call venv\Scripts\activate.bat
)

REM Installer les dépendances
echo.
echo 📥 Installation des dépendances Streamlit...
pip install -r requirements.txt

echo.
echo ✓ Installation terminée !
echo.
echo 🚀 Lancement de l'application...
echo    → Ouvre http://localhost:8501 dans ton navigateur
echo.

REM Lancer l'application
streamlit run app.py

pause
