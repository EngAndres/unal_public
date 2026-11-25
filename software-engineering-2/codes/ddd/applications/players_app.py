"""This module has a definition for some CRUD endpoints
to handle the players into the project.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from domains import PlayerIn, PlayerOut
from repositories import PlayersRepository, PGConn
from services import PlayerService

pg = PGConn()
router = APIRouter(prefix="/players")

def get_service(db: Session = Depends(pg.get_db)) -> PlayerService:
    return PlayerService(PlayersRepository(db))

@router.get("/get_all", response_model=List[PlayerOut])
def get_all(services: PlayerService = Depends(get_service)):
    """This service returns all the players."""
    return services.get_all()

@router.get("/get_by_id/{id}", response_model=Optional[PlayerOut])
def get_one(id: int, services: PlayerService = Depends(get_service)):
    """This service returns a player searching by the id."""
    return services.get_by_id(id)

@router.get("/get_by_team/{team_id}", response_model=List[PlayerOut])
def get_by_team(team_id: int, services: PlayerService = Depends(get_service)):
    """This service returns all players belonging to a team."""
    return services.get_by_team(team_id)

@router.post("/add", response_model=PlayerOut)
def insert(player: PlayerIn, services: PlayerService = Depends(get_service)):
    """This service adds a new player."""
    return services.create(player)

@router.put("/update/{id}", response_model=Optional[PlayerOut])
def update(id: int, player: PlayerIn, services: PlayerService = Depends(get_service)):
    """This service updates an existing player using the id as reference."""
    return services.update(id, player)

@router.delete("/delete/{id}")
def delete(id: int, services: PlayerService = Depends(get_service)):
    """This service deletes a player based on the id."""
    return services.delete(id)