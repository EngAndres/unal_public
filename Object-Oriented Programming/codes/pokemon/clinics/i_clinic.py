from abc import ABC, abstractmethod

class Clinic(ABC):
    """This is an interface of a clinic in the game."""

    @abstractmethod
    def recovery(self, pokemon_type: str):
        pass

    @abstractmethod
    def vacunate(self, pokemon_age: int):
        pass
