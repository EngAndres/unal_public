"""This module has a class with the aritmetic operations of the calculator.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

class Calculator:
    """This class represents the behavior of a classic calculator."""

    def sum(self, num_1: int, num_2: int) -> int:
        """
        This method performs a sum of two numbers.

        Args:
            num_1(int): First number to be in the sum
            num_2(int): Second number to be in the sum

        Result:
            An integer number with the sum of the numbers.
        """
        return num_1 + num_2
    
    def division(self, num_1: int, num_2: int) -> float:
        """
        This method performs a simple division of the two numbers.
        
        Args:
            num_1(int): The number to be used as numerator in the division.
            num_2(int): The number to be used as denominator in the division.
        """
        if num_2 != 0:
            return num_1 / num_2
        else:
            return None