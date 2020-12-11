from typing import Dict
from pydantic import BaseModel

class UserDB(BaseModel):
    username: str
    password: str

database_users = DIct[str, UserDB]

database_users = {
    "gura20": UserDB(**{"username":"gura20",
                            "password":"root"}),
    "watson09": UserDB(**{"username":"watson09",
                            "password":"doom"}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else: 
        return None
