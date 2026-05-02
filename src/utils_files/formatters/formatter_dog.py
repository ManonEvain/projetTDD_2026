from src.models.dog import Dog
from src.models.animal import Animal
from src.models.combat import Combat
from src.utils_files.formatters.formatter import AnimalFormatter


class DogFormatter(AnimalFormatter):
    
    def __init__(self, animal_repository):
        self.animal_repository = animal_repository

    def format_animal(self, row):
        return Dog(
            name=row["dog_name"],
            age=int(row["years"])
        )

    def format_combat(self, row):
        a1 = self.animal_repository.chercher_animal(row["ani1"])
        a2 = self.animal_repository.chercher_animal(row["ani2"])

        if not a1 or not a2:
            return None

        return Combat(
            adversaire1=a1,
            adversaire2=a2,
            score1=int(row["score1"]),
            score2=int(row["score2"])
        )
