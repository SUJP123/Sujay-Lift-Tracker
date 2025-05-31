from pydantic import BaseModel


class Workout(BaseModel):
    workoutId:int
    name:str
    description:str

# Maps Workouts to Exercises
class WorkoutMapper(BaseModel):
    workoutId: int
    exerciseId: int
    order: int