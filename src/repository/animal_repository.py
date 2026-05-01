class AnimalRepository:
    """Repository responsible for storing animals."""

    def __init__(self):
        self.animals = []
        self.combat = []

    def add_animal(self, animal):
        """Add an animal to the repository."""
        self.animals.append(animal)
    
    def add_combat(self, combat):
        """Add a game to the repository."""
        self.combat.append(combat)
        
    def get_all_animal(self):
        """Return all stored animals."""
        return self.animals

    def get_all_game(self):
        """Return all stored game."""
        return self.combat