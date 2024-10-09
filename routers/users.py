from fastapi  import FastAPI, Depends, status, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2=OAuth2PasswordBearer(tokenUrl="login")


app=FastAPI()

class User(BaseModel):
    id:int
    username:str
    full_name:str
    email:str
    disabled:bool

class UserDB(User):   
    password:str


users_db = {
    "jorgehaq": {
        "username":"jorgehaq",
        "full_name": "Jorge Alvarez",                                     
        "email":"jorgehaq@gmail.com",
        "disabled":False,
        "password":"123456"                            
    },
    "jorgehaq2": {
        "username":"jorgehaq2",
        "full_name": "Jorge Alvarez 2",                                     
        "email":"jorgehaq2@gmail.com",
        "disabled":True,
        "password":"654321" 
    }
}



def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])
    
async def current_user(token:str = Depends(oauth2)):
    user=search_user_db(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticacion invalidas",
            headers={"www-Authenticate":"Bearer"}
            )
        return user
'''
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_401_BAD_REQUEST,
            detail="Usuario Inactivo",
            headers={"www-Authenticate":"Bearer"}
            )
'''       
@app.post('/login')
async def login(form: OAuth2PasswordRequestForm=Depends()):
    return {
            "access_token": "user.username",
            "token_type":"bearer"
        }
    user_db=users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto"
        )
    
    user=search_user(user_db.username)
    if not form.password==user.password:
        raise HTTPException(
            status_code=400,
            detail="La constrasena no es valida"
        )
        return {
            "access_token": user.username,
            "token_type":"bearer"
        }
    

    
@app.get('/url')
async def root():
    return {
        "un curso":"fas api tutorial"
    }


@app.get("/users/me")
async def me(user:User = Depends(current_user)):
    return user

