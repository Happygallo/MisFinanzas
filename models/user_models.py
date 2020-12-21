from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str
class UserOut(BaseModel): 
    username: str
    budget: int
class BudgetOut(BaseModel):
    username: str
    budget: int
    expenses: int
    remaining: int  

# class Transaccion(BaseModel):
#     usuario: int
#     concept: str
#     amount: int
#     budget: int




