"""This module has some definition of models for
teams and players handling.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from typing import List, Optional
from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str
    age: int
    weight: float
    height: float

class PlayerIn(PlayerBase):
    team_id: int

class PlayerOut(PlayerBase):
    id: int
    team_id: int

    class Config:
        from_attributes = True

class TeamBase(BaseModel):
    name: str
    color: str

class TeamOut(TeamBase):
    id: int
    players: List[PlayerOut] = []

    class Config:
        from_attributes = True