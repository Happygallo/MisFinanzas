from typing import Dict
from pydantic import BaseModel

class UserDB(BaseModel):
    username: str
    password: str

database_users = Dict[str, UserDB]

database_users = {
    "gura20": UserDB(**{"username":"gura20",
                            "password":"root"}),
    "watson09": UserDB(**{"username":"watson09",
                            "password":"doom"}),
    "ivan": UserDB(**{"username":"ivan",
                            "password":"navi"}),                        
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else: 
        return None


def post_user(username: str, password: str, user_in_db: UserDB):
    UserDB.username= username
    UserDB.password = password
    database_users[str(username)] = UserDB
    return UserDB
