from src.models.chicken import Chicken
from src.models.dog import Dog
from src.models.combat import Combat
from src.utils_files.formatters.formatter import AnimalFormatter


class MixedFormatter(AnimalFormatter):

    def __init__(self, animal_repository):
        self.animal_repository = animal_repository


    def format_animal(self, row):

        if row["type"] == "dog":
            return Dog(row["nom"], int(row["age"]))

        if row["type"] == "chicken":
            return Chicken(row["nom"], int(row["age"]))

        raise ValueError("Unknown type")
    
    def format_combat(self, row):
        a1 = self.animal_repository.chercher_animal(row["chien"])
        a2 = self.animal_repository.chercher_animal(row["chicken"])

        if not a1 or not a2:
            return None

        return Combat(
            adversaire1=a1,
            adversaire2=a2,
            score1=int(row["nombre1"]),
            score2=int(row["nombre2"])
        )
