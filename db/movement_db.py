from datetime import datetime
from pydantic import BaseModel

class MovementInDB(BaseModel):
    id_movement: int = 0
    username: str
    date: datetime = datetime.now()
    movement: str
    movement_type: str
    movement_category: str
    description: str
    amount: int
    actual_balance: int

database_movements = []
generator = {"id":0}

def save_movement(movement_in_db: MovementInDB):
    generator["id"] = generator["id"] + 1
    movement_in_db.id_movement = generator["id"]
    database_movements.append(movement_in_db)
    return movement_in_db