from pydantic import BaseModel, EmailStr
from typing import Optional

# User
from pydantic import BaseModel, EmailStr
from typing import Optional

# Input from client when registering
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Output back to client
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    role: str
    profile_image: Optional[str]
    welcome_message: Optional[str] = None

    class Config:
        from_attributes = True  # important! allows SQLAlchemy model -> Pydantic



# class Token(BaseModel):
#     access_token: str
#     token_type: str

# # Tea
# class TeaCreate(BaseModel):
#     name: str
#     origin: str

# class TeaResponse(BaseModel):
#     id: int
#     name: str
#     origin: str
