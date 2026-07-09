"""ß
This module has a repository to get data from the databse related with Stadiums.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from typing import List, Optional

from sqlalchemy.orm import Session
from domains import StadiumBase, StadiumOut
from .orm import StadiumModel

class StadiumsRepository:
    """This class represents the repository to handle the stadiums data in the database."""
    
    def __init__(self, db: Session):
        self.__db = db

    def get_all(self) -> List[StadiumOut]:
        """This method extracts the stadiums from the database.
        
        Returns:
            A List of StadiumOut objects with all the stadiums in the database.
        """
        return self.__db.query(StadiumModel).all()

    def get_by_id(self, stadium_id: int) -> Optional[StadiumOut]:
        """This method gets a stadium by its id.
        
        Args:
            stadium_id (int): An integer with the stadium id to search.
        
        Returns:
            An optional StadiumOut object with the stadium data if found, otherwise None.
        """
        return self.__db.query(StadiumModel)\
                .filter(StadiumModel.id == stadium_id)\
                .first()

    def create(self, stadium: StadiumBase) -> StadiumOut:
        """This method creates a new stadium in the database.
        
        Args:
            stadium (StadiumBase): A StadiumBase object with the stadium data to create.
        
        Returns:
            A StadiumOut object with the created stadium data.
        """ 
        db_stadium = StadiumModel(**stadium.model_dump())
        self.__db.add(db_stadium)
        self.__db.commit()
        self.__db.refresh(db_stadium);
        return db_stadium

    def update(self, stadium_id: int, stadium: StadiumBase) -> Optional[StadiumOut]:
        """This method updates an existing stadium in the database.
        
        Args:
            stadium_id (int): An integer with the stadium id to update.
            stadium (StadiumBase): A StadiumBase object with the new stadium data to update.

        Returns:
            An optional StadiumOut object with the updated stadium data if the update was successful, otherwise None
        """
        db_stadium = self.__db.query(StadiumModel).filter(StadiumModel.id == stadium_id).first()
        if not db_stadium:
            return None
        for key, value in stadium.model_dump().items():
            setattr(db_stadium, key, value)
        self.__db.commit()
        self.__db.refresh(db_stadium)
        return db_stadium

    def delete(self, stadium_id: int) -> bool:
        """This method deletes a stadium from the database.
        
        Args:
            stadium_id (int): An integer with the stadium id to delete.

        Returns:
            A boolean indicating whether the deletion was successful.
        """
        db_stadium = self.__db.query(StadiumModel).filter(StadiumModel.id == stadium_id).first()
        if not db_stadium:
            return False
        self.__db.delete(db_stadium)
        self.__db.commit()
        return True
    