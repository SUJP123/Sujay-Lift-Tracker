from pydantic import BaseModel


class Exercise(BaseModel):
    exerciseId: int
    name: str
    description: str
