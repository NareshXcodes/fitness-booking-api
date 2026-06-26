from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr

class SignupRequest(BaseModel):
    name : str
    email : EmailStr
    password : str

class SignupResponse(BaseModel):
    id : int
    name : str
    email : EmailStr
    created_at : datetime



class LoginRequest(BaseModel):
    email : EmailStr
    password : str

class TokenResponse(BaseModel):
    access_token : str
    token_type : str
    model_config = ConfigDict(from_attributes=True)