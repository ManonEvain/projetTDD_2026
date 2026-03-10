from .animal import Animal


class Chicken(Animal):
    """Chicken class, inherits from Animal."""

    def speak(self) -> str:
        return "Cocorico"
