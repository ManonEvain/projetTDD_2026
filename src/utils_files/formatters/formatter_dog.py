from src.models.dog import Dog
from src.utils_files.formatters.formatter import AnimalFormatter


class DogFormatter(AnimalFormatter):

    def format(self, row):
        return Dog(
            name=row["dog_name"],
            age=int(row["years"])
        )
