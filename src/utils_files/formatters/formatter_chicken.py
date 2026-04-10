from src.models.chicken import Chicken
from src.utils_files.formatters.formatter import AnimalFormatter


class ChickenFormatter(AnimalFormatter):

    def format(self, row):
        return Chicken(
            name=row["name"],
            age=int(row["age_years"])
        )
