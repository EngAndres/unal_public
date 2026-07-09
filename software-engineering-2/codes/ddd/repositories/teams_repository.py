"""This module has a repository to get data from the database related with Teams.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from typing import List, Optional

from sqlalchemy.orm import Session
from domains import TeamBase, TeamOut
from .orm import TeamModel


class TeamsRepository:
    """This class represents the repository to handle the teams data in the database."""

    def __init__(self, db: Session):
        self.__db = db

    def get_all(self) -> List[TeamOut]:
        """This method extracts all teams from the database.

        Returns:
            A List of TeamOut objects with all the teams in the database.
        """
        return self.__db.query(TeamModel).all()

    def get_by_id(self, team_id: int) -> Optional[TeamOut]:
        """This method gets a team by its id.

        Args:
            team_id (int): An integer with the team id to search.

        Returns:
            An optional TeamOut object with the team data if found, otherwise None.
        """
        return self.__db.query(TeamModel).filter(TeamModel.id == team_id).first()

    def create(self, team: TeamBase) -> TeamOut:
        """This method creates a new team in the database.

        Args:
            team (TeamBase): A TeamBase object with the team data to create.

        Returns:
            A TeamOut object with the created team data.
        """
        db_team = TeamModel(**team.model_dump())
        self.__db.add(db_team)
        self.__db.commit()
        self.__db.refresh(db_team)
        return db_team

    def update(self, team_id: int, team: TeamBase) -> Optional[TeamOut]:
        """This method updates an existing team in the database.

        Args:
            team_id (int): An integer with the team id to update.
            team (TeamBase): A TeamBase object with the new team data.

        Returns:
            An optional TeamOut object with the updated team data, or None if not found.
        """
        db_team = self.__db.query(TeamModel).filter(TeamModel.id == team_id).first()
        if not db_team:
            return None
        for key, value in team.model_dump().items():
            setattr(db_team, key, value)
        self.__db.commit()
        self.__db.refresh(db_team)
        return db_team

    def delete(self, team_id: int) -> bool:
        """This method deletes a team from the database.

        Args:
            team_id (int): An integer with the team id to delete.

        Returns:
            A boolean indicating whether the deletion was successful.
        """
        db_team = self.__db.query(TeamModel).filter(TeamModel.id == team_id).first()
        if not db_team:
            return False
        self.__db.delete(db_team)
        self.__db.commit()
        return True
