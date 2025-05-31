from typing import Self
from sqlalchemy import Enum, create_engine, Column, Integer, String
from sqlalchemy.orm import relationship
from backend.model.User import Role, User
from backend.database.db import Base

class ExerciseEntity(Base):
    __tablename__ = "exercise"
    exerciseId = Column(Integer, primary_key=True)
    name = Column(str)
    description = Column(str)

    workout_mapper = relationship('WorkoutMapper', back_populates='exercise')