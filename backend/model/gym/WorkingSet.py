from pydantic import BaseModel


class WorkingSet(BaseModel):
    workingSetId: int
    workoutId:int
    exerciseId: int
    sets: int
    reps: int
    weight: float
    notes: str