"""ORM Definition for the Teams table.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from repositories.db_connection import Base


class TeamModel(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    color = Column(String, nullable=False)
    players = relationship("PlayerModel", back_populates="team")
