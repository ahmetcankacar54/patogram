from typing import Optional
from pydantic import BaseModel


class LoginRequest(BaseModel): 
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None