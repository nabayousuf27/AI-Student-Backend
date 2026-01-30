from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String, default="user")
    profile_image = Column(String, nullable=True)
    
# class Tea(Base):
#     __tablename__ = "teas"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     origin = Column(String, nullable=False)
