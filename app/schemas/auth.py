from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field

class SignupRequest(BaseModel):
    name : str
    email : EmailStr
    password : str = Field(min_length=8)

class SignupResponse(BaseModel):
    id : int
    name : str
    email : EmailStr
    created_at : datetime



class LoginRequest(BaseModel):
    email : EmailStr
    password : str = Field(min_length=8)

class TokenResponse(BaseModel):
    access_token : str
    token_type : str
    model_config = ConfigDict(from_attributes=True)