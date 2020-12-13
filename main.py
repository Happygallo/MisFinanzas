from fastapi import FastAPI, Request, HTTPException 
from fastapi.templating import Jinja2Templates
from db.user_db import get_user, post_user, UserDB
from models.user_models import UserIn, UserOut
app = FastAPI()

templates = Jinja2Templates(directory="layout")

@app.get("/")
def inicio(request: Request):
    """
    inicio de la aplicacion, petición de usuario
    """
    return templates.TemplateResponse("inicio.html", {
        "request": request,
        "variable": "MinTIC 2022"
    })


@app.get("/usuario/{username}")
async def display_user(username: str, request: Request):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return templates.TemplateResponse("usuario.html", {
        "request": request,
        "usuario": str(user_out.username),
    })

@app.post("/crear_usuario/")
async def create_user(user_in: UserIn):
    user_in_db = UserDB(**user_in.dict())
    user_in_db = post_user(user_in_db.username, user_in.password, user_in_db=UserDB)
    return user_in