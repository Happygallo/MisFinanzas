from pydantic import BaseModel
from datetime import datetime

class MovementIn(BaseModel):
    id_movement: int
    username: str
    date: datetime
    concept: str
    amount: int

class MovementOut(BaseModel):
    id_movement: int
    username: str
    date: datetime
    concept: str
    amount: int
    budget: int