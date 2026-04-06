from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    role: Optional[str] = "viewer"

class UserUpdate(BaseModel):
    role: Optional[str]
    status: Optional[str]

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    status: str

    class Config:
        from_attributes = True