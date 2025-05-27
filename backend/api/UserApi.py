from typing import List
from fastapi import Depends, FastAPI, APIRouter, Path

from backend.model.User import User
from backend.service.UserService import UserService

api = APIRouter()


@api.get("/", tags=["Users"])
def get_all_users() -> List[User]:
    raise NotImplementedError("Not Implemented")

@api.get("/{id}", tags=["Users"])
def get_user_by_id(id: int, user_svc: UserService = Depends()) -> User:
    return user_svc.get_user_by_id(id)

@api.post("/", tags=["Users"])
def add_user(user: User) -> User:
    raise NotImplementedError("Not Implemented")

