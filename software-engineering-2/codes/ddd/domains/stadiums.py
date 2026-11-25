"""This module has some models for the stadiums
into the project FootboolWorldCup.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from pydantic import BaseModel

class StadiumBase(BaseModel):
    name: str
    capacity: int
    address: str
    city: str

class StadiumOut(StadiumBase):
    id: int
    created_at: str

    class Config:
        from_attributes = True
    