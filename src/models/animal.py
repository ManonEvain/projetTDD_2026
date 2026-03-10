class Animal:
    """
    Represent an animal in the farm.

    Parameters
    ----------
    name : str
        Name of the animal.
    age : int
        Age of the animal in years.
    """

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def speak(self) -> str:
        """
        Make the animal produce a sound.

        Returns
        -------
        str
            The sound produced by the animal.
        """
        raise NotImplementedError()

    def description(self) -> str:
        """
        Return a description of the animal.

        Returns
        -------
        str
            Description of the animal.
        """
        return f"{self.name} ({self.age} ans)"
