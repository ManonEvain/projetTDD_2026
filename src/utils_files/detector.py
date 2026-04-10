from src.utils_files.formatters.formatter_mixed import MixedFormatter
from src.utils_files.formatters.formatter_dog import DogFormatter
from src.utils_files.formatters.formatter_chicken import ChickenFormatter


class FormatterDetector:

    def detect(self, headers):

        headers = set(headers)

        if {"nom", "type", "age"} <= headers:
            return MixedFormatter()

        if {"dog_name", "years"} <= headers:
            return DogFormatter()

        if {"name", "age_years"} <= headers:
            return ChickenFormatter()

        raise ValueError("Unknown format")
