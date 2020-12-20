from pydantic import BaseModel
from datetime import datetime

class MovementIn(BaseModel):
    username: str
    movement: str
    movement_type: str
    movement_category: str
    description: str
    amount: int

class MovementOut(BaseModel):
    id_movement: int
    username: str
    date: datetime
    movement: str
    movement_type: str
    movement_category: str
    description: str
    amount: int
    actual_balance: int