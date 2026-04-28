import os 
from dotenv import load_dotenv

from src.interface.cli import show_menu
from src.repository.animal_repository import AnimalRepository
from src.services.farm_service import FarmService
from src.utils.utils import welcome


load_dotenv()


def principal_view():
    repository = AnimalRepository()
    service = FarmService(repository)

    chemin = os.path.join(os.getenv("data_path"), os.getenv("import_files"))

    welcome()

    service.add_animals(chemin)

    while True:
        show_menu()
        choice = input("Choix : ")

        if choice == "1":
            name = input("Nom : ")
            age = int(input("Age : "))
            service.add_dog(name, age)
        elif choice == "2":
            name = input("Nom : ")
            age = int(input("Age : "))
            service.add_chicken(name, age)
        elif choice == "3":
            for a in service.list_animals():
                print(a.description())
        elif choice == "4":
            service.animals_speak()
        elif choice == '5':
            file = input("Fichier :")
            service.add_animals(file)
        elif choice == '6':
            file = input("Nom du fichier :")
            service.export_animals(file)
        elif choice == "7":
            print("Au revoir !")
            break
