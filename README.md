# Présentation de votre projet 

Pour lancer le projet : 

1. Installer les requirements 
```
pip install poetry
poetry install --no-root
```

2. Lancer l'environnement virtuel 
```
python -m venv venv
```

3. Lancer le menu principal : 
```
python -m main
```

4. Lancer les tests (avec pytest) : 
```
pytest -v
pytest --cov=src/ tests/ 
```
