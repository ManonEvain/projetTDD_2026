from src.models.dog import Dog
from src.models.chicken import Chicken


class FarmService:
    """Service to manage animals in the farm."""

    def __init__(self, repository):
        self.repository = repository

    def add_dog(self, name: str, age: int):
        """Add a dog to the zoo."""
        dog = Dog(name, age)
        self.repository.add(dog)

    def add_chicken(self, name: str, age: int):
        """Add a chicken to the farm."""
        chicken = Chicken(name, age)
        self.repository.add(chicken)

    def list_animals(self):
        """Return all animals."""
        return self.repository.get_all()

    def animals_speak(self):
        """Make all animals speak."""
        for animal in self.repository.get_all():
            print(f"{animal.name} say {animal.speak()}")
