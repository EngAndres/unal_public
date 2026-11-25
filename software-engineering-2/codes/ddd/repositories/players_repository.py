"""This module has a repository to get data from the database related with Players.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from typing import List, Optional

from sqlalchemy.orm import Session
from domains import PlayerIn, PlayerOut
from .orm import PlayerModel


class PlayersRepository:
    """This class represents the repository to handle the players data in the database."""

    def __init__(self, db: Session):
        self.__db = db

    def get_all(self) -> List[PlayerOut]:
        """This method extracts all players from the database.

        Returns:
            A List of PlayerOut objects with all the players in the database.
        """
        return self.__db.query(PlayerModel).all()

    def get_by_id(self, player_id: int) -> Optional[PlayerOut]:
        """This method gets a player by its id.

        Args:
            player_id (int): An integer with the player id to search.

        Returns:
            An optional PlayerOut object with the player data if found, otherwise None.
        """
        return self.__db.query(PlayerModel).filter(PlayerModel.id == player_id).first()

    def get_by_team(self, team_id: int) -> List[PlayerOut]:
        """This method gets all players belonging to a team.

        Args:
            team_id (int): An integer with the team id to filter by.

        Returns:
            A List of PlayerOut objects for the given team.
        """
        return self.__db.query(PlayerModel).filter(PlayerModel.team_id == team_id).all()

    def create(self, player: PlayerIn) -> PlayerOut:
        """This method creates a new player in the database.

        Args:
            player (PlayerIn): A PlayerIn object with the player data to create.

        Returns:
            A PlayerOut object with the created player data.
        """
        db_player = PlayerModel(**player.model_dump())
        self.__db.add(db_player)
        self.__db.commit()
        self.__db.refresh(db_player)
        return db_player

    def update(self, player_id: int, player: PlayerIn) -> Optional[PlayerOut]:
        """This method updates an existing player in the database.

        Args:
            player_id (int): An integer with the player id to update.
            player (PlayerIn): A PlayerIn object with the new player data.

        Returns:
            An optional PlayerOut object with the updated player data, or None if not found.
        """
        db_player = self.__db.query(PlayerModel).filter(PlayerModel.id == player_id).first()
        if not db_player:
            return None
        for key, value in player.model_dump().items():
            setattr(db_player, key, value)
        self.__db.commit()
        self.__db.refresh(db_player)
        return db_player

    def delete(self, player_id: int) -> bool:
        """This method deletes a player from the database.

        Args:
            player_id (int): An integer with the player id to delete.

        Returns:
            A boolean indicating whether the deletion was successful.
        """
        db_player = self.__db.query(PlayerModel).filter(PlayerModel.id == player_id).first()
        if not db_player:
            return False
        self.__db.delete(db_player)
        self.__db.commit()
        return True
