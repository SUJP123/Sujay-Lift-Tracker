from pydantic import BaseModel


class Workout(BaseModel):
    workoutId:int
    name:str
    description:str
    
