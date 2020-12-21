from pydantic import BaseModel
from datetime import datetime
import numpy as np
# class MovementIn(BaseModel):
#     username: str
#     password: str
#     concept: str
#     amount: float
class MovementOut(BaseModel):
    id: int
    username: str
    date: str
    concept: str
    amount: float
    #budget: float


movements = {
    "1": MovementOut(id=1,username="gura20" , date = "04-07-2020", concept="ingreso",amount=10000),
    "2": MovementOut(id=2,username="gura20" , date = "05-08-2020", concept="ingreso",amount=12000),
    "3": MovementOut(id=3,username="gura20" , date = "06-09-2020", concept="ingreso",amount=10000),
    "4": MovementOut(id=4,username="watson09" , date = "04-07-2020", concept="ingreso",amount=10000),
    "5": MovementOut(id=5,username="watson09" , date = "05-08-2020", concept="ingreso",amount=12000),
    "6": MovementOut(id=6,username="watson09" , date = "06-09-2020", concept="ingreso",amount=10000),
}

def get_movements(username: str):
    #haga lo que tenga que hacer para conectarse a la base de datos y obtner todas las ordenes
    list_movements=[]
    for i in movements.values():

        if i.username==username:
            list_movements.append(i)
    return list_movements


def add_movement(movement: MovementOut):
    if movement.id in movements:
        return False
    else:
        movements[movement.id]= movement
        return True

