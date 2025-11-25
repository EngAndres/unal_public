"""
"""

from abc import ABC, abstractmethod
from ..pokemons import Pokemon

class IClinic(ABC):
    """"""
    
    @abstractmethod
    def recovery_pokemon(self, pokemon: Pokemon):
        pass

    @abstractmethod
    def info(self):
        pass
