"""This module has some models for the I/O of the calculator

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from pydantic import BaseModel

class CalculatorInput(BaseModel):
    """Class for two numbers input."""
    num_1: int
    num_2: int

class  CalculatorOutputInteger(BaseModel):
    """Class for calculator integer response."""
    response: int

class  CalculatorOutputDecimal(BaseModel):
    """Class for calculator integer response."""
    response: float
