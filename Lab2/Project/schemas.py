#pydantic model

from pydantic import BaseModel, EmailStr, Field
class StudentCreate(BaseModel):
    name: str
    age: int
    email: EmailStr
    is_graduate : bool =False

#StudentResponse: Used for sending API data in responses

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    is_graduate : bool

    class Config:
        from_attributes = True


    