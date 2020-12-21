from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str
    amount: float
    budget: float
    expenses: float
    remaining: float
