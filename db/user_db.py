from typing import Dict
from pydantic import BaseModel

class UserDB(BaseModel):
    username: str
    password: str
    budget: int

database_users = Dict[str, UserDB]

database_users = {
    "gura20": UserDB(**{"username":"gura20",
                            "password":"root",
                            "budget": 12000}),
    "watson09": UserDB(**{"username":"watson09",
                            "password":"doom",
                            "budget": 15000}),
}


def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else: 
        return None

def post_user(username: str, password: str, budget: float, expenses: float, remaining: float):
    UserDB.username= username
    UserDB.password = password
    UserDB.budget = budget
    database_users.append(UserDB)
    return UserDB

def update_user(user_in_db: UserDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db

def update_user_balance(user_in_db: UserDB):
    database_users[user_in_db.username] = user_in_db
    return user_in_db


