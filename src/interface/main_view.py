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
            print("Erreur, l'action que vous avez sélectionnée n'existe pas.")


def gestion_combat(service):

    while True:

        menu_gestion_combat()

        choix = input("Quelle action voulez-vous réaliser ? ")

        if choix == "1":
            for cmbt in service.list_combats():
                print(cmbt)

        elif choix == "2":
            ani1 = input("Nom du premier animal :")
            ani2 = input("Nom du deuxième animal :")
            score1 = input("Score de l'animal 1 :")
            score2 = input("Score de l'animal 2 :")

            animal1 = service.chercher_animal(ani1)
            animal2 = service.chercher_animal(ani2)
            if animal1 is not None and animal2 is not None:
                service.add_combat(animal1, animal2, int(score1), int(score2)) 
            else: 
                print("Un des animaux que vous avez demandé n'a pas été trouvé")

        elif choix == "3":
            combat = service.choisir_combat()
            if combat is not None : 
                score1 = input("Nouveau score de l'animal 1 :")
                score2 = input("Nouveau score de l'animal 2 :")
                combat.modifier_score(score1, score2)

        elif choix == "4":
            fichier = input("Nom du fichier :")
            service.add_combats(fichier)
        
        elif choix == "5":
            fichier = input("Nom du fichier : ")
            service.export_combat(fichier)

        elif choix == "6":
            accueil(service)

        else: 
            print("Erreur, l'action que vous avez sélectionnée n'existe pas.")


def principal_view():
    repository = AnimalRepository()
    service = FarmService(repository)

    liste_animaux = ["data/chicken/farm_chicken.csv", "data/dog/farm_dog.csv"]
    liste_combat = ["data/dog/combat_dog.csv"]

    for chemin_animaux in liste_animaux: 
        service.add_animals(chemin_animaux)
    
    for chemin_combat in liste_combat: 
        service.add_combats(chemin_combat)

    welcome()
    
    while True:
        accueil(service)
