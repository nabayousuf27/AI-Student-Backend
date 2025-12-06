
# Naba yousuf 
# se231020
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime , timezone

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    role = Column(String, default="user")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    vehicles = relationship("Vehicle", back_populates="owner")

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_name = Column(String, nullable=False)
    registration_no = Column(String, unique=True, nullable=False)
    vehicle_type = Column(String, nullable=False)  # e.g., Car, Bike
    daily_rate = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True)
    seating_capacity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))


    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    # Relationship back to user
    owner = relationship("User", back_populates="vehicles")