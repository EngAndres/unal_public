"""This module has some classes related to an interface
called Animal, and some child classes for different animals.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self) -> str:
        """This is the sound and animal could make."""

class Dog(Animal):

    def make_sound(self):
        return "Guau"
    
class Tiger(Animal):

    def make_sound(self):
        return "Grrr"