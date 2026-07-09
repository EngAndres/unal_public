from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import db_settings

Base = declarative_base()

class PGConn:

    def __init__(self):
        engine = create_engine(db_settings.DATABASE_URL)
        self.Connection = sessionmaker(
            autocommit=False, 
            autoflush=False, 
            bind=engine)
        

    def get_db(self):
        db = self.Connection()
        try:
            yield db
        finally:
            db.close()