from pydantic import BaseModel
from typing import Optional
from datetime import date

class RecordCreate(BaseModel):
    amount: float
    type: str  # income or expense
    category: Optional[str]
    date: Optional[date]
    notes: Optional[str]
    user_id: int

class RecordUpdate(BaseModel):
    amount: Optional[float]
    type: Optional[str]
    category: Optional[str]
    date: Optional[date]
    notes: Optional[str]

class RecordResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: Optional[str]
    date: Optional[date]
    notes: Optional[str]
    user_id: int

    class Config:
        from_attributes = True