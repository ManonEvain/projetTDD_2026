from .animal import Animal


class Dog(Animal):
    """Dog class, inherits from Animal."""

    def speak(self) -> str:
        return "Woof"
