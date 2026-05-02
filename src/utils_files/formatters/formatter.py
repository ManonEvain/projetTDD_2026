from abc import ABC, abstractmethod


class AnimalFormatter(ABC):

    @abstractmethod
    def format_animal(self, row: dict):
        pass

    @abstractmethod
    def format_combat(self, row: dict):
        pass
