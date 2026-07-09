"""This is the main class for this example.
It has a Class Zoo and a simple instantiation
of a zoo with different animals.

Author: Carlos Andrés Sierra <casierrav@unal.edu.co>
"""

from typing import List

from animals import Animal, Dog, Tiger

class Zoo:

    def __init__(self):
        self._animals : List[Animal] = []
        self.__add_animals()

    def __add_animals(self):
        """This methods adds a set of animals
        to the zoo list.
        """
        self._animals.append(Dog())
        self._animals.append(Dog())
        self._animals.append(Tiger())

    def make_animals_sound(self):
        """This method has a behavior where
        each animal make a sound."""
        if len(self._animals) > 0:
            for animal in self._animals:
                print( animal.make_sound() )
                print("Soy un animal" if isinstance(animal, Animal) else "No se que soy")
        else:
            print("No animals")

# ==========================
my_zoo = Zoo()
my_zoo.make_animals_sound()