from typing import Self
from sqlalchemy import Enum, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.model.User import Role, User
from backend.database.db import Base


# User Entity For SQL ORM
class UserEntity(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    role = Column(Enum(Role))

    @classmethod
    def model_to_entity(cls, user: User) -> Self:
        return cls(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            role=user.role
        )