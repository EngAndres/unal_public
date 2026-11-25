"""This module has a definition for some CRUD endpoints
to handle the stadiums into the project.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from typing import List, Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from domains import StadiumBase, StadiumOut
from repositories import StadiumsRepository, PGConn
from services import StadiumService

pg = PGConn()
router = APIRouter(prefix="/stadiums")

def get_service(db: Session = Depends(pg.get_db)) ->StadiumOut:
    return StadiumService(StadiumsRepository(db))

@router.get("/get_all", response_model=List[StadiumOut])
def get_all(services: StadiumService = Depends(get_service)):
    """This service returns all the stadiums."""
    return services.get_all()
    
@router.get("/get_by_id/{id}", response_model=Optional[StadiumOut])
def get_one(id: int, services: StadiumService = Depends(get_service)):
    """This service returns a stadium searching by the id."""
    return services.get_by_id(id)

@router.post("/add")
def insert(stadium: StadiumBase, services: StadiumService = Depends(get_service)):
    """This service add a new stadium."""
    return services.create(stadium)

@router.put("/update/{id}")
def update(id: int, stadium: StadiumBase, services: StadiumService = Depends(get_service)):
    """This service update an existing stadium using the id as reference."""
    return services.update(id, stadium)

@router.delete("/delete/{id}")
def delete(id: int, services: StadiumService = Depends(get_service)):
    """This service deletes a stadium based on the id."""
    return services.delete(id)
