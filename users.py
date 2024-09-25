from fastapi import FastAPI
from pydantic import BaseModel
import pdb

app= FastAPI()

class User(BaseModel):
    id:int
    name:str
    apellido:str
    url:str
    age:int


users_list = [
    User(id=1, name="Jorge", apellido="Alvarez", url="google.com", age=40),
    User(id=2, name="Maria", apellido="Gonzales", url="maria.com", age=30),
    User(id=3, name="Jose", apellido="Gomez", url="jose.com", age=43),
    User(id=1, name="Pablo", apellido="Martinez", url="pablo.com", age=32),
]


@app.get("/usersjson")
async def usersjson():
    return users_list

@app.get("/user/{id}")             
async def user(id:int):
    return search_users(id)

@app.get("/userquery/{id}")
async def user(id:int):
    return search_users(id)

@app.post("/user")
async def user(user:User):
    if type(search_users(user.id))==User:
        return {"error":"El usuario ya existe"}
    else:
        users_list.append(user)
        return user
    
@app.put("/user/{id}")
async def user(user:User):
    found=False
    for index, saved_user in enumerate(users_list):
        if saved_user.id==user.id:
            users_list[index]=user
            found=True
    
    if not found:
        return {"error": "El usuario no ha sido actualizado"}




@app.delete("/user/{id}")
async def user(id:int):
    found=False
    for index, saved_users in enumerate(users_list):
        del users_list[index]
        found=True
    
    if not found:
        return {"error": "Usuario no encontrado"}



def search_users(id:int):
    users=filter(lambda user: user.id==id,users_list)
    try:
        return list(users)[0]
    except:
        return { "error": "No se ha encontrado el usuario"}
