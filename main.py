from db.user_db import UserDB
from db.user_db import database_users
from db.user_db import post_user, get_user
from models.user_models import UserIn
import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

# página de inicio
@api.get("/")
def inicio():
    #inicio de la aplicacion, petición de usuario
    return {"Pagina de Inicio": "Mision TIC 2022 - Mis Finanzas"}

@api.get("/users/")
async def users():
    return {"message": database_users}

# mostrar usuario
@api.get("/users/{username}")
async def display_user(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserIn(**user_in_db.dict())
    return user_out

# crear usuario
@api.post("/users/")
async def create_user(user_in: UserDB):
    database_users[user_in.username] = user_in
    return user_in

@api.post("/users/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if user_in_db.password != user_in.password:
        return  {"Autenticado": False}
    return  {"Autenticado": True}