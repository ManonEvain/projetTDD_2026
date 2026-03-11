from src.interface.cli import show_menu
from src.repository.animal_repository import AnimalRepository
from src.services.farm_service import FarmService

from src.utils.utils import welcome


def principal_view():
    repository = AnimalRepository()
    service = FarmService(repository)

    welcome()

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
        elif choice == "5":
            print("Au revoir !")
            break
