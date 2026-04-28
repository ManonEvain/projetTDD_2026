# Présentation de votre projet 

Pour lancer le projet : 

1. Lancer l'environnement virtuel 
```
python -m venv venv
source venv/bin/activate
```

2. Installer les requirements 
```
pip install poetry
poetry install --no-root
```

3. Ajouter un fichier .env à la racine du projet, ayant la structure suivante :
```
data_path=changme
import_files=changme
```

Les variables d'environnement doivent contenir les informations suivantes

- data_path : Nom du dossier ou se trouve les données 
- import_files : Fichier chargé lors de l'ouverture de la ferme  

4. Lancer le menu principal : 
```
python -m main
```

5. Lancer les tests (avec pytest) : 
```
export PYTHONPATH=$PYTHONPATH:$(pwd)/src
pytest -v
pytest --cov=src/ tests/ 
```

6. Désactiver l'environnement virtuel 
```
deactivate
```