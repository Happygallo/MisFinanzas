from pydantic import BaseModel
from datetime import datetime
from db.user_db import database_users, database_budget
from db.user_db import post_user, get_user, get_auth_user
# class MovementIn(BaseModel):
#     username: str
#     password: str
#     concept: str
#     amount: float
class MovementOut(BaseModel):
    now = str(datetime.now())[:15]
    id = int(str(datetime.now())[-5:])
    username: str
    date = now
    concept: str
    amount: float
    #budget: float
class BudgetOut(BaseModel):
    username: str
    budget: int
    expenses: int
    remaining: int  

movements = {
    "1": MovementOut(id=1,username="gura20" , date = "04-07-2020 22:01", concept="gasto",amount=10000),
    "2": MovementOut(id=2,username="gura20" , date = "05-08-2020 22:02", concept="gasto",amount=12000),
    "3": MovementOut(id=3,username="gura20" , date = "06-09-2020 22:03", concept="gasto",amount=10000),
    "4": MovementOut(id=4,username="watson09" , date = "04-07-2020 22:04", concept="gasto",amount=10000),
    "5": MovementOut(id=5,username="watson09" , date = "05-08-2020 22:05", concept="gasto",amount=12000),
    "6": MovementOut(id=6,username="watson09" , date = "06-09-2020 22:06", concept="gasto",amount=10000),
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


def sum_balance(username: str):
    user_in = get_user(username)
    user_budget = user_in.budget
    
    user_movs = get_movements(username)
    gastos = []
    for i in user_movs:
        gastos.append(i.amount)
    gastos = sum(gastos)
    restante = user_budget - gastos
    return user_budget, gastos, restante