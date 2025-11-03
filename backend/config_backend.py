from pydantic import BaseModel, EmailStr

DB_NAME='piggie.db'

class UserSignup(BaseModel):
    name: str
    surname: str
    birthday: str
    email: str
    password: str

# Pydantic model for login
class UserLogin(BaseModel):
    email: str
    password: str