from ..database.db import Base, engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

def create_db():
    # Create the table in the database
    Base.metadata.create_all(engine)