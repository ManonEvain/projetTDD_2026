import os 
import sys
from dotenv import load_dotenv

from src.interface.cli import menu_gestion_combat, menu_gestion_ferme, menu_principal, menu_visite_ferme
from src.repository.animal_repository import AnimalRepository
from src.services.farm_service import FarmService
from src.utils.utils import welcome


load_dotenv()

def accueil(service):
    while True:
        menu_principal()
        choice = input("Que voulez vous faire ? ")

        if choice == "1":
            gestion_ferme(service)

        elif choice == "2":
            visite_ferme(service)

        elif choice == "3":
            gestion_combat(service)
            
        elif choice == "4":
            print("Au revoir !")
            sys.exit()

        else:
            print("Erreur, l'action que vous avez sélectionner n'existe pas.")


def gestion_ferme(service):

    while True:
        
        menu_gestion_ferme()
            
        choix = input("Quelle action voulez vous réaliser ?")

        if choix == "1":
            name = input("Nom : ")
            age = int(input("Age : "))
            service.add_dog(name, age)

        elif choix == "2": 
            name = input("Nom : ")
            age = int(input("Age : "))
            service.add_chicken(name, age)
    
        elif choix == "3": 
            file = input("Fichier :")
            service.add_animals(file)

        elif choix == "4": 
            file = input("Nom du fichier :")
            service.export_animals(file)

        elif choix == "5":
            accueil(service)
  
        else:
            print("Erreur, l'action que vous avez sélectionner n'existe pas.")


def visite_ferme(service):
    while True:
        menu_visite_ferme()

        choix = input("Quelle action voulez-vous réaliser ?")

        if choix == "1":
            for a in service.list_animals():
                print(a.description())

        elif choix == "2":
            service.animals_speak()

        elif choix == "3":
            accueil(service)

        else:
            print("Erreur, l'action que vous avez sélectionner n'existe pas.")


def gestion_combat():
    return None


def principal_view():
    repository = AnimalRepository()
    service = FarmService(repository)

    chemin = os.path.join(os.getenv("data_path"), os.getenv("import_files"))

    welcome()

    service.add_animals(chemin)
    while True:
        accueil(service)
