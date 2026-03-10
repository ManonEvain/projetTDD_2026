class AnimalRepository:
    """Repository responsible for storing animals."""

    def __init__(self):
        self.animals = []

    def add(self, animal):
        """Add an animal to the repository."""
        self.animals.append(animal)

    def get_all(self):
        """Return all stored animals."""
        return self.animals
