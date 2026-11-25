"""Interface to define connection with a Postgresql data source

Author: Carlos A Sierra
"""

from typing import Type, TypeVar, List, Optional

from abc import ABC
from sqlalchemy.orm import Session

model_obj = TypeVar("ModelType")

class PosgresRepository(ABC):
    """This is a mother class to use in repositories connection to tables"""
    
    def __init__(self, db: Session, model: Type[model_obj]):
        self.__db = db
        self.__model = model

    def get_all(self) -> List[model_obj]:
        return self.__db.query(self.__model).all()

    def get_id(self, _id: int) -> Optional[model_obj]:
        return self.__db.query(self.__model).filter(self.__model.id == _id).first()
        
    def create(self, object: model_obj):
        pass
    
    def delete(self, id: int):
        pass
