from src.models.chicken import Chicken
from src.models.dog import Dog
from src.utils_files.formatters.formatter import AnimalFormatter


class MixedFormatter(AnimalFormatter):

    def format(self, row):

        if row["type"] == "dog":
            return Dog(row["nom"], int(row["age"]))

        if row["type"] == "chicken":
            return Chicken(row["nom"], int(row["age"]))

        raise ValueError("Unknown type")
