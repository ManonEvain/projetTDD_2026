from src.models.dog import Dog


class TestDog:

    def setup_method(self):
        """Cette méthode est appelée avant chaque test"""
        self.a = Dog("Test", 2)

    def test_speak(self):
        assert self.a.speak() == "Woof"

    def test_description(self):
        assert self.a.description() == "Test (2 ans)"
