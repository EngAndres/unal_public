"""This module has some services asociated to a simple aritmetic calculator tasks.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from typing import Optional

class Calculator:
    """This class represents the behavior of a simple calculator."""

    def sum(self, num_1: int, num_2: int) -> int:
        """
        This method performs a sum of two numbers provided as parameters.

        Args:
            num_1(int): First number of the sum
            num_2(int): Second number of the sum

        Returns:
            An integer number with the sum of the numbers.
        """
        return num_1 + num_2
    
    def division(self, num_1: int, num_2: int) -> Optional[float]:
        """
        This method performs a division of two numbers provided as parameters.
        A validation for denominatore different to zero is applied.

        Args:
            num_1(int): Enumerator number of the division
            num_2(int): Denominator number of the division

        Returns:
            An decimal number with the division of the numbers.
        """
        if num_2 != 0:
            return num_1 / num_2
        else:
            return None