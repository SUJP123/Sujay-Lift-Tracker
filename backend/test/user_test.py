from fastapi import Depends
import pytest

from backend.entity.UserEntity import UserEntity
from backend.service.UserService import UserService
from backend.model.User import Role


def test_root_user_is_added(user_svc : UserService):
    user = user_svc.get_user_by_id(1)
    assert user is not None
    assert user.id == 1
    assert user.first_name == "Sujay"
    assert user.last_name == "Patel"
    assert user.role == Role.ROOT