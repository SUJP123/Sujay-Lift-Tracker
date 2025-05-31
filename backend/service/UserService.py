from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from backend.database.db import get_session
from sqlalchemy import select, insert

from backend.entity.UserEntity import UserEntity
from backend.model.User import User

class UserServiceException(Exception):
    def __init__(self, arg:str):
        raise Exception(arg)

class UserService:
    _session: Session

    def __init__(self):
        self._session = next(get_session())
    
    def get_user_by_id(self, id:int) -> User:
        query = select(UserEntity).where(UserEntity.id == id)
        user = self._session.scalar(query)

        if not user:
            raise UserServiceException("User Not Found With id =" + id)
        return user

    def get_all_users(self) -> List[User]:
        query = select(UserEntity)
        users = self._session.scalar(query)

        if not users:
            raise UserServiceException("No Users Found")
        return users
    
    def add_user(self, user: User) -> User:
        try:
            result = self._session.add(UserEntity.model_to_entity(user))
        except:
            raise UserServiceException("User unable to be added")
        return user