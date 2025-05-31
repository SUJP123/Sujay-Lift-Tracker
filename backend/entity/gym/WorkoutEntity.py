from typing import Self
from sqlalchemy import Enum, ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database.db import Base
from sqlalchemy.schema import PrimaryKeyConstraint



class WorkoutEntity(Base):
    __tablename__ = "workout"
    workoutId = Column(Integer, primary_key=True)
    name = Column(str)
    description = Column(str)

    workout_mapper = relationship('WorkoutMapper', back_populates='workout')

class WorkoutMapper(Base):
    __tablename__ = "workout_mapper"
    workoutId = Column(Integer, ForeignKey("workout.workoutId"))
    exerciseId = Column(Integer, ForeignKey("exercise.exerciseId"))
    order = Column(Integer)

    __table_args__ = (PrimaryKeyConstraint('workoutId',  'exerciseId'))

    workout = relationship('WorkoutEntity', back_populates='workout_mapper')
    exercise = relationship('ExerciseEntity', back_populates='workout_mapper')