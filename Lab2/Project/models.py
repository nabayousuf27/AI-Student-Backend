#database models

from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Student(Base):
    __tablename__ = "Students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_graduate = Column(Boolean, default=False)
