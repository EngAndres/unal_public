"""This module has the busines logic related to stadiums management.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from typing import List, Optional
from sqlalchemy.orm import Session

from domains import StadiumBase, StadiumOut
from repositories import StadiumsRepository

class StadiumService:
    """This class represents the behavior of stadiums logic"""

    def __init__(self, repository: StadiumsRepository):
        self.__repo = repository;

    def get_all(self) -> List[StadiumOut]:
        """This methods gets all the stadiums in the repository.
        
        Returns:
            A List of StadiumOut objects with all the stadiums in the repository.
        """
        return self.__repo.get_all()

    def get_by_id(self, id:int) -> Optional[StadiumOut]:
        """This method gets a stadium by its id.
        
        Args:
            id (int): An integer with the stadium id to search.
        
        Returns:
            An optional StadiumOut object with the stadium data if found, otherwise None.

        Raises:
            ValueError: If the id is less than or equal to zero.
        """
        if id <= 0:
            raise ValueError("Stadium ID cannot be negative.")
        return self.__repo.get_by_id(id) 


    def create(self, stadium: StadiumBase) -> StadiumOut:
        """This method creates a new stadium in the repository.
        
        Args:
            stadium (StadiumBase): A StadiumBase object with the stadium data to create.
        
        Returns:
            A StadiumOut object with the created stadium data.

        Raises:
            ValueError: If the stadium capacity is less than or equal to zero.
        """
        if stadium.capacity <= 0:
            raise ValueError("Stadium capacity cannot be negative.")
        return self.__repo.create(stadium)

    def update(self, id: int, stadium: StadiumBase) -> Optional[StadiumOut]:
        """This method updates an existing stadium in the repository.
        Args:
            id (int): An integer with the stadium id to update.
            stadium (StadiumBase): A StadiumBase object with the new stadium data to update.

        Returns:
            An optional StadiumOut object with the updated stadium data if the update was successful, otherwise None.
        """
        return self.__repo.update(id, stadium)

    def delete(self, id: int) -> bool:
        """This method deletes a stadium from the repository.
        
        Args:
            id (int): An integer with the stadium id to delete.

        Returns:
            A boolean indicating whether the deletion was successful.
        """
        return self.__repo.delete(id)
