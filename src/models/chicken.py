from .animal import Animal


class Chicken(Animal):
    """Chicken class, inherits from Animal."""

    def __str__(self):
        print(self.name)
        
    def speak(self) -> str:
        return "Cocorico"
