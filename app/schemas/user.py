from pydantic import BaseModel

class Register(BaseModel):
    name: str
    email: str

class Login(BaseModel):
    email: str
