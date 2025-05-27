from pydantic import BaseModel
from enum import Enum

class Role(Enum):
    ROOT = "root"
    VIEWER = "viewer"

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    role: Role