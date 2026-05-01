from src.models.dog import Dog
from src.models.chicken import Chicken

from src.utils_files.csv_importer import CSVImporter
from src.utils_files.csv_exporter import CSVExporter
from src.utils_files.detector import FormatterDetector


class FarmService:
    """Service to manage animals in the farm."""

    def __init__(self, repository):
        self.repository = repository
        self.importer = CSVImporter()
        self.detector = FormatterDetector()
        self.exporter = CSVExporter()

    def add_dog(self, name: str, age: int):
        """Add a dog to the zoo."""
        dog = Dog(name, age)
        self.repository.add_animal(dog)

    def add_chicken(self, name: str, age: int):
        """Add a chicken to the farm."""
        chicken = Chicken(name, age)
        self.repository.add_animal(chicken)

    def add_animals(self, file_path: str):
        """Add a list of animals to the farm"""
        try:
            rows, headers = self.importer.import_file(file_path)
            formatter = self.detector.detect(headers)

            for row in rows:
                animal = formatter.format(row)
                self.repository.add_animal(animal)
        except FileNotFoundError as e:
            print(f"❌ Erreur : {e}")

    def export_animals(self, file_path: str):
        """Export all animals of the farm in csv"""
        animals = self.repository.get_all_animal()
        self.exporter.export(file_path, animals)

    def list_animals(self):
        """Return all animals."""
        return self.repository.get_all()

    def animals_speak(self):
        """Make all animals speak."""
        for animal in self.repository.get_all():
            print(f"{animal.name} say {animal.speak()}")
