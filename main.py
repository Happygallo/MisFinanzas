from db.user_db import UserDB, BudgetDB
from db.user_db import database_users, database_budget
from db.user_db import post_user, get_user, get_auth_user
from models.user_models import UserIn, UserOut
from db.movement_db import MovementInDB
from db.movement_db import save_movement
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.movement_models import MovementOut, get_movements, add_movement, sum_balance


api = FastAPI()

origins = [
     "http://localhost", 
     "http://localhost:8080",
     "http://app-misfinanzas.herokuapp.com",
     "https://app-misfinanzas.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# # página de inicio
# @api.get("/")
# def inicio():
#     #inicio de la aplicacion, petición de usuario
#     return {"Pagina de Inicio": "Mision TIC 2022 - Mis Finanzas"}

@api.get("/users/")
async def users():
    return {"users": database_budget}

# crear usuario
@api.post("/users/")
async def create_user(user_in: UserDB):
    database_users[user_in.username] = user_in
    return user_in

# dar balance a usuario
@api.post("/users/budget")
async def update_budget(budget_in: BudgetDB):
    database_budget[budget_in.username] = budget_in
    return budget_in

# mostrar usuario
@api.get("/users/{username}")
async def display_user(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

# autenticar usuario
@api.post("/users/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_auth_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        raise HTTPException(status_code=403, detail="Error de autenticacion")
    return  {"Autenticado": True}



@api.post("/movements/add")
async def agregar_movimiento(movement: MovementOut):
    creado = add_movement(movement)
    if creado:
        return {"mensaje": "Movimiento generado"}
    else:
        raise HTTPException(status_code=400, detail="Lo siento, la id del movimiento esta ya creada")


@api.get("/movements/show")
async def obtener_movimientos(username: str):
    movimientos = get_movements(username)
    return movimientos

@api.get("/user/budget/see")
async def obtener_balance(username: str):
    username, budget, gastos, restante, movimientos = sum_balance(username)
    estado = {"username": username, "budget": budget, "gastos": gastos, "restante": restante, "movimientos": movimientos}
    return estado
