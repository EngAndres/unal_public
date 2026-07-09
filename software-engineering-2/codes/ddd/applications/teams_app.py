"""This module has a definition for some CRUD endpoints
to handle the teams into the project.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from domains import TeamBase, TeamOut
from repositories import TeamsRepository, PGConn
from services import TeamService

pg = PGConn()
router = APIRouter(prefix="/teams")

def get_service(db: Session = Depends(pg.get_db)) -> TeamService:
    return TeamService(TeamsRepository(db))

@router.get("/get_all", response_model=List[TeamOut])
def get_all(services: TeamService = Depends(get_service)):
    """This service returns all the teams."""
    return services.get_all()

@router.get("/get_by_id/{id}", response_model=Optional[TeamOut])
def get_one(id: int, services: TeamService = Depends(get_service)):
    """This service returns a team searching by the id."""
    return services.get_by_id(id)

@router.post("/add", response_model=TeamOut)
def insert(team: TeamBase, services: TeamService = Depends(get_service)):
    """This service adds a new team."""
    return services.create(team)

@router.put("/update/{id}", response_model=Optional[TeamOut])
def update(id: int, team: TeamBase, services: TeamService = Depends(get_service)):
    """This service updates an existing team using the id as reference."""
    return services.update(id, team)

@router.delete("/delete/{id}")
def delete(id: int, services: TeamService = Depends(get_service)):
    """This service deletes a team based on the id."""
    return services.delete(id)