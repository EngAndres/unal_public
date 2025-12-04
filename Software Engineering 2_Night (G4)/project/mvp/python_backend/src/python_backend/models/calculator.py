"""This module has some models to interact with the calculator services.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from pydantic import BaseModel

class CalculatorInput(BaseModel):
    """Format of the input data to calculator."""
    num_1: int
    num_2: int

class CalculatorOutputInteger(BaseModel):
    """Format the output based on an integer results."""
    result: int

class CalculatorOutputDecimal(BaseModel):
    """Format the output based on an decinal results."""
    result: float
