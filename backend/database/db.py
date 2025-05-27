from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session


# Create SQLite engine (stored in file)
engine = create_engine("sqlite:///mydatabase.db", echo=True)

# Base class for models
Base = declarative_base()

def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()