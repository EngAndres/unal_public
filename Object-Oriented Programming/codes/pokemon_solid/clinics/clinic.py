"""
"""

from i_clinic import IClinic
from ..pokemons import Pokemon

# ========== Small Clinic ========== #
class SmallClinic(IClinic):
    """"""

    def __init__(self, nurse_name: str):
        self.__nurse = nurse_name

    def info(self):
        """"""
        print(f"This is a small clinic. Here the nurse is called {self.__nurse}")

    def recovery_pokemon(self, pokemon: Pokemon):
        """

        Args:
            pokemon (Pokemon):
        """
        pokemon.health_recovery()



# ========== Big Clinic ========== #
class BigClinic(IClinic):
    """"""

    def __init__(self, medical_doctor_name: str):
        self.__medical_doctor = medical_doctor_name

    def info(self):
        """"""
        print(f"This is a big clinic. Here the medical doctor is called {self.__medical_doctor}")

    def recovery_pokemon(self, pokemon: Pokemon):
        """
        
        Args:
            pokemon (Pokemon):
        """
        pokemon.health_recovery()
        pokemon.health_recovery()
        