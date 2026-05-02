from .animal import Animal


class Dog(Animal):
    """Dog class, inherits from Animal."""

    def __str__(self):
        print(self.name)
        
    def speak(self) -> str:
        return "Woof"
