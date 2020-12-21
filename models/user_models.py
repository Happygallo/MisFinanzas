from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str
    budget: float

class Transaccion(BaseModel):
    usuario: int
    concept: str
    amount: int
    budget: int




