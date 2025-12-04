"""This module has an api router definition for the calculator services.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from fastapi import APIRouter
from ..models import CalculatorInput, CalculatorOutputDecimal, CalculatorOutputInteger
from ..services import CalculatorService

router = APIRouter(prefix="/calculator")
service = CalculatorService()

@router.post('/sum', response_model=CalculatorOutputInteger)
def api_sum(numbers: CalculatorInput):
    """This service performs a sum of two numbers."""
    return service.sum(numbers.num_1, numbers.num_2)

@router.post('/division', response_model=CalculatorOutputDecimal)
def api_division(numbers: CalculatorInput):
    """This service performs a division of two numbers."""
    return service.division(numbers.num_1, numbers.num_2)