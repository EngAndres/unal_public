"""ORM Definition for the Stadiums table.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from repositories.db_connection import Base

class StadiumModel(Base):
    __tablename__ = 'stadiums'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    capacity = Column(Integer, nullable=False)
    address = Column(String, default='')
    city = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
