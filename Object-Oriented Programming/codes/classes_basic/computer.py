"""This file has a simple class to make an 
example of OOP in Python.
Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

class Computer:
    """This class represents a Personal Computer in the app."""

    def __init__(self, brand: str, processor: str, ram: int, hd_space: int, operative_system: str):
        """Constructor of the class"""
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.hd_space = hd_space
        self.operative_system = operative_system

    def specs(self):
        print(f"Hello. I am a computer of brand {self.brand}. \
              I have a processor {self.processor}, {self.ram} GB of RAM, \
              {self.hd_space} HDD capacity, and a {self.operative_system} OS.")

    