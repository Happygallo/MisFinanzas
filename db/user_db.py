from typing import Dict
from pydantic import BaseModel

class UserDB(BaseModel):
    username: str
    password: str

class BudgetDB(BaseModel):
    username: str
    budget: int

database_users = Dict[str, UserDB]

database_users = {
    "gura20": UserDB(**{"username":"gura20",
                            "password":"root"}),
    "watson09": UserDB(**{"username":"watson09",
                            "password":"doom"}),
}

database_budget = {
    "gura20": BudgetDB(**{"username":"gura20",
                            "budget":600000}),
    "watson09": BudgetDB(**{"username":"watson09",
                            "budget":400000}),
}


def get_user(username: str):
    if username in database_users.keys():
        return database_budget[username]
    else: 
        return None

def get_auth_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else: 
        return None

def post_user(username: str, password: str):
    UserDB.username= username
    UserDB.password = password
    database_users.append(UserDB)
    return UserDB

def post_budget(username: str, budget:int):
    BudgetDB.username= username
    BudgetDB.budget = budget
    database_budget.append(BudgetDB)
    return BudgetDB

def update_user(user_in_db: BudgetDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db

def update_user_budget(user_in_db: BudgetDB, budget):
    database_users[user_in_db.budget] = budget
    return user_in_db




