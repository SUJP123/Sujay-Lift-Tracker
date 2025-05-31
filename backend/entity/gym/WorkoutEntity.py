from typing import Self
from sqlalchemy import Enum, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.model.User import Role, User
from backend.database.db import Base



class WorkoutEntity(Base):
    __tablename__ = "workout"
    workoutId = Column(Integer, primary_key=True)
    name = Column(str)
    description = Column(str)