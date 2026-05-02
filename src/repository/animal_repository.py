import difflib

class AnimalRepository:
    """Repository responsible for storing animals."""

    def __init__(self):
        self.animals = []
        self.combats = []

    def add_animal(self, animal):
        """Add an animal to the repository."""
        self.animals.append(animal)
    
    def add_combat(self, combat):
        """Add a game to the repository."""
        self.combats.append(combat)
        
    def get_all_animal(self):
        """Return all stored animals."""
        return self.animals

    def get_all_game(self):
        """Return all stored game."""
        return self.combats

    def afficher_combats(self): 
        if not self.combats:
            print("Aucun combat disponible")
            return

        for i, combat in enumerate(self.combats, start=1):
            print(f"{i}. {combat}")

    def chercher_animal(self, nom: str): 
        noms = [animal.name for animal in self.animals]
        resultats = difflib.get_close_matches(nom, noms, n=1)

        if resultats:
            return next(animal for animal in self.animals if animal.name == resultats[0])
        return None