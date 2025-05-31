from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.database.db import get_session
from sqlalchemy import select, insert

from backend.entity.gym.WorkoutEntity import WorkoutEntity
from backend.model.gym.Workout import Workout

class WorkoutServiceException(Exception):
    def __init__(self, arg:str):
        raise Exception(arg)

class WorkoutService:
    _session: Session

    def __init__(self):
        self._session = next(get_session())