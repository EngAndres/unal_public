"""This module has the business logic related to players management.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from typing import List, Optional
from sqlalchemy.orm import Session

from domains import PlayerIn, PlayerOut
from repositories import PlayersRepository


class PlayerService:
    """This class represents the behavior of players logic."""

    def __init__(self, repository: PlayersRepository):
        self.__repo = repository

    def get_all(self) -> List[PlayerOut]:
        """This method gets all the players in the repository.

        Returns:
            A List of PlayerOut objects with all the players in the repository.
        """
        return self.__repo.get_all()

    def get_by_id(self, id: int) -> Optional[PlayerOut]:
        """This method gets a player by its id.

        Args:
            id (int): An integer with the player id to search.

        Returns:
            An optional PlayerOut object with the player data if found, otherwise None.

        Raises:
            ValueError: If the id is less than or equal to zero.
        """
        if id <= 0:
            raise ValueError("Player ID must be a positive integer.")
        return self.__repo.get_by_id(id)

    def get_by_team(self, team_id: int) -> List[PlayerOut]:
        """This method gets all players belonging to a team.

        Args:
            team_id (int): An integer with the team id to filter by.

        Returns:
            A List of PlayerOut objects for the given team.

        Raises:
            ValueError: If the team_id is less than or equal to zero.
        """
        if team_id <= 0:
            raise ValueError("Team ID must be a positive integer.")
        return self.__repo.get_by_team(team_id)

    def create(self, player: PlayerIn) -> PlayerOut:
        """This method creates a new player in the repository.

        Args:
            player (PlayerIn): A PlayerIn object with the player data to create.

        Returns:
            A PlayerOut object with the created player data.

        Raises:
            ValueError: If the player age, weight, or height are invalid.
        """
        if player.age <= 0:
            raise ValueError("Player age must be a positive integer.")
        if player.weight <= 0:
            raise ValueError("Player weight must be a positive number.")
        if player.height <= 0:
            raise ValueError("Player height must be a positive number.")
        return self.__repo.create(player)

    def update(self, id: int, player: PlayerIn) -> Optional[PlayerOut]:
        """This method updates an existing player in the repository.

        Args:
            id (int): An integer with the player id to update.
            player (PlayerIn): A PlayerIn object with the new player data.

        Returns:
            An optional PlayerOut object with the updated player data, or None if not found.
        """
        return self.__repo.update(id, player)

    def delete(self, id: int) -> bool:
        """This method deletes a player from the repository.

        Args:
            id (int): An integer with the player id to delete.

        Returns:
            A boolean indicating whether the deletion was successful.
        """
        return self.__repo.delete(id)
