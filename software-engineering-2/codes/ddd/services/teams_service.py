"""This module has the business logic related to teams management.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from typing import List, Optional
from sqlalchemy.orm import Session

from domains import TeamBase, TeamOut
from repositories import TeamsRepository


class TeamService:
    """This class represents the behavior of teams logic."""

    def __init__(self, repository: TeamsRepository):
        self.__repo = repository

    def get_all(self) -> List[TeamOut]:
        """This method gets all the teams in the repository.

        Returns:
            A List of TeamOut objects with all the teams in the repository.
        """
        return self.__repo.get_all()

    def get_by_id(self, id: int) -> Optional[TeamOut]:
        """This method gets a team by its id.

        Args:
            id (int): An integer with the team id to search.

        Returns:
            An optional TeamOut object with the team data if found, otherwise None.

        Raises:
            ValueError: If the id is less than or equal to zero.
        """
        if id <= 0:
            raise ValueError("Team ID must be a positive integer.")
        return self.__repo.get_by_id(id)

    def create(self, team: TeamBase) -> TeamOut:
        """This method creates a new team in the repository.

        Args:
            team (TeamBase): A TeamBase object with the team data to create.

        Returns:
            A TeamOut object with the created team data.

        Raises:
            ValueError: If the team name is empty.
        """
        if not team.name.strip():
            raise ValueError("Team name cannot be empty.")
        return self.__repo.create(team)

    def update(self, id: int, team: TeamBase) -> Optional[TeamOut]:
        """This method updates an existing team in the repository.

        Args:
            id (int): An integer with the team id to update.
            team (TeamBase): A TeamBase object with the new team data.

        Returns:
            An optional TeamOut object with the updated team data, or None if not found.
        """
        return self.__repo.update(id, team)

    def delete(self, id: int) -> bool:
        """This method deletes a team from the repository.

        Args:
            id (int): An integer with the team id to delete.

        Returns:
            A boolean indicating whether the deletion was successful.
        """
        return self.__repo.delete(id)
