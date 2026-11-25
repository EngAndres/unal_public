"""This module has an example of a student class
with some encapsulations.

Author: Carlos Sierra <casierrav@unal.edu.co>
"""

class Student:
    """This class represents the behavior of a typical UN student."""

    def __init__(self):
        self.__papa = 4.2

    # ERROR
    def set_papa(self, new_papa: float):
        if 0 <= new_papa <= 5.0:
            self.__papa = new_papa
        else:
            raise ValueError("El rango de la nota es incorrecto.")

    def get_papa(self) -> float:
        # validate grants
        return self.__papa
    # ===== Encapsulation =====

    def is_good(self):
        if self.__papa > 4:
            print("Una chimba")
        elif self.__papa > 3:
            print("Ahí vamos")
        else:
            print("Pesadito")