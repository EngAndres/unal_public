"""
This module has a set of endpoints to handle some calculator operations.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from typing import Optional

from fastapi import APIRouter, HTTPException
from models import CalculatorInput, CalculatorOutputDecimal, CalculatorOutputInteger
from services import CalculatorServices

router = APIRouter(prefix='/calculator')
service = CalculatorServices()

@router.post('/sum', response_model=CalculatorOutputInteger)
def api_sum(numbers: CalculatorInput):
    """This service performs the sum of two numbers."""
    result = service.sum(numbers.num_1, numbers.num_2)
    return CalculatorOutputInteger(result=result)

@router.post('/division', response_model=Optional[CalculatorOutputDecimal])
def api_division(numbers: CalculatorInput):    
    """This service performs the division of two numbers."""
    result = service.division(numbers.num_1, numbers.num_2)
    if result is not None:
        return CalculatorOutputDecimal(result=result)
    else:
        raise HTTPException(status_code=403, detail="The division by zero is forbidden.")
