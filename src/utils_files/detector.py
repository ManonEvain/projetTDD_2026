from src.utils_files.formatters.formatter_mixed import MixedFormatter
from src.utils_files.formatters.formatter_dog import DogFormatter
from src.utils_files.formatters.formatter_chicken import ChickenFormatter


class FormatterDetector:

    def __init__(self, animal_repository):
        self.animal_repository = animal_repository

    def detect_animal(self, headers):

        headers = set(headers)

        if {"nom", "type", "age"} <= headers:
            return MixedFormatter(self.animal_repository)

        if {"dog_name", "years"} <= headers:
            return DogFormatter(self.animal_repository)

        if {"name", "age_years"} <= headers:
            return ChickenFormatter(self.animal_repository)

        raise ValueError("Unknown format")

    def detect_combat(self, headers): 
        headers = set(headers)

        if {"ani1", "ani2", "score1", "score2"} <= headers:
            return DogFormatter(self.animal_repository)

        if {"chien", "chicken", "nombre1", "nombre2"} <= headers:
            return MixedFormatter(self.animal_repository)

        if {"adv1", "adv2", "score1", "score2"} <= headers:
            return ChickenFormatter(self.animal_repository)

        raise ValueError("Unknown format")
