from abc import ABC, abstractmethod


class AnimalFormatter(ABC):

    @abstractmethod
    def format(self, row: dict):
        pass
