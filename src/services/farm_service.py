from src.models.dog import Dog
from src.models.chicken import Chicken
from src.models.combat import Combat
from src.models.animal import Animal

from src.utils_files.csv_importer import CSVImporter
from src.utils_files.csv_exporter import CSVExporter
from src.utils_files.detector import FormatterDetector

import difflib


class FarmService:
    """Service to manage animals in the farm."""

    def __init__(self, repository):
        self.repository = repository
        self.importer = CSVImporter()
        self.detector = FormatterDetector(self.repository)
        self.exporter = CSVExporter()

    def add_dog(self, name: str, age: int):
        """Add a dog to the zoo."""
        dog = Dog(name, age)
        self.repository.add_animal(dog)

    def add_chicken(self, name: str, age: int):
        """Add a chicken to the farm."""
        chicken = Chicken(name, age)
        self.repository.add_animal(chicken)
    
    def chercher_animal(self, nom: str): 
        noms = [animal.name for animal in self.repository.get_all_animal()]
        resultats = difflib.get_close_matches(nom, noms, n=1)

        if resultats:
            return next(animal for animal in self.repository.animals if animal.name == resultats[0])
        return None

    def add_combat(self, animal1: Animal, animal2: Animal, score1: int, score2: int):
        combat = Combat(animal1, animal2, score1, score2)
        self.repository.add_combat(combat)

    def add_animals(self, file_path: str):
        """Add a list of animals to the farm"""
        try:
            rows, headers = self.importer.import_file(file_path)
            formatter = self.detector.detect_animal(headers)

            for row in rows:
                animal = formatter.format_animal(row)
                self.repository.add_animal(animal)
        except FileNotFoundError as e:
            print(f"❌ Erreur : {e}")

    def add_combats(self, file_path: str): 

        ignored = 0

        try:
            rows, headers = self.importer.import_file(file_path)
            formatter = self.detector.detect_combat(headers)

            for row in rows:
                combat = formatter.format_combat(row)

                if combat is None:
                    ignored += 1
                else:
                    self.repository.add_combat(combat)
            # 🔔 message final
            if ignored > 0:
                print(f"⚠️ {ignored} lignes de combats n'ont pas été chargées (données invalides)")

        except FileNotFoundError as e:
            print(f"❌ Erreur : {e}")

    def export_animals(self, file_path: str):
        """Export all animals of the farm in csv"""
        animals = self.repository.get_all_animal()
        self.exporter.export_animals(file_path, animals)

    def list_animals(self):
        """Return all animals."""
        return self.repository.get_all_animal()

    def animals_speak(self):
        """Make all animals speak."""
        for animal in self.repository.get_all_animal():
            print(f"{animal.name} say {animal.speak()}")

    def list_combats(self):
        return self.repository.get_all_game()
    
    def modifier_combat(self, combat: Combat, score1: int, score2: int):
        return combat.modifier_score(score1, score2)

    def export_combat(self, file_path: str): 
        """Export all combats of the farm in csv"""
        combats = self.repository.get_all_game()
        self.exporter.export_combats(file_path, combats)
    
    def choisir_combat(self):
        if not self.repository.combats:
            print("Aucun combat disponible")
            return None

        self.repository.afficher_combats()

        try:
            choix = int(input("Choisissez un combat (numéro) : "))
            if 1 <= choix <= len(self.repository.combats):
                return self.repository.combats[choix - 1]
            else:
                print("Choix invalide")
                return None
        except ValueError:
            print("Veuillez entrer un nombre")
            return None
