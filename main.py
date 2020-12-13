from db.user_db import UserInDB
from db.user_db import update_user, get_user
from db.transaction_db import TransactionInDB
from db.transaction_db import save_transaction
from models.user_models import UserIn, UserOut
from models.transaction_models import TransactionIn, TransactionOut
import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()

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