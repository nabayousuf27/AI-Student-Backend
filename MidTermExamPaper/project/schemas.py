# Naba yousuf 
# se231020
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    full_name: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
    role: str
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class VehicleCreate(BaseModel):
    vehicle_name: str
    registration_no: str
    vehicle_type: str
    daily_rate: float
    is_available: Optional[bool] = True
    seating_capacity: int

class VehicleResponse(VehicleCreate):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True
