from typing import Self
from sqlalchemy import Enum, ForeignKey, create_engine, Column, Integer, String, Float
from sqlalchemy.orm import relationship
from backend.model.User import Role, User
from backend.database.db import Base


class WorkingSetEntity(Base):
    __tablename__ = "working_set"
    workingSetId = Column(Integer, primary_key=True)
    workoutId = Column(Integer, ForeignKey('workout.workoutId'))
    exerciseId = Column(Integer, ForeignKey('exercise.exerciseId'))
    sets = Column(Integer)
    reps = Column(Integer)
    weight = Column(Float)
    notes = Column(String)

    workout = relationship("WorkoutEntity", backref="WorkingSetEntity")
    exercise = relationship("ExerciseEntity", backref="WorkingSetEntity")