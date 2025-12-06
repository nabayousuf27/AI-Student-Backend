#naba yousuf se231020

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine, Base
import models, schemas, auth
#from schemas import UserCreate as ItemCreate, UserResponse as ItemResponse
from database import get_db


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vehicle Rental System")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# AUTHENTICATION 
@app.post("/auth/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(
        (models.User.username == user.username) | (models.User.email == user.email)
    ).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    
    hashed_password = auth.get_password_hash(user.password)
    new_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/auth/token", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/auth/profile", response_model=schemas.UserResponse)
def get_profile(current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    return current_user

#VEHICLE CRUD

@app.post("/api/items/", response_model=schemas.VehicleResponse, status_code=status.HTTP_201_CREATED)
def create_vehicle(
    item: schemas.VehicleCreate, 
    current_user: models.User = Depends(auth.get_current_user), 
    db: Session = Depends(get_db)
):
    new_vehicle = models.Vehicle(**item.dict(), owner_id=current_user.id)
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    return new_vehicle

@app.get("/api/items/", response_model=List[schemas.VehicleResponse])
def list_vehicles(
    skip: int = 0, 
    limit: int = 10, 
    current_user: models.User = Depends(auth.get_current_user), 
    db: Session = Depends(get_db)
):
    if current_user.role == "admin":
        vehicles = db.query(models.Vehicle).offset(skip).limit(limit).all()
    else:
        vehicles = db.query(models.Vehicle).filter(models.Vehicle.owner_id == current_user.id).offset(skip).limit(limit).all()
    return vehicles

@app.get("/api/items/{item_id}", response_model=schemas.VehicleResponse)
def get_vehicle(
    item_id: int, 
    current_user: models.User = Depends(auth.get_current_user), 
    db: Session = Depends(get_db)
):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == item_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Item not found")
    if current_user.role != "admin" and vehicle.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this item")
    return vehicle

@app.patch("/api/items/{item_id}", response_model=schemas.VehicleResponse)
def update_vehicle(
    item_id: int, 
    item: schemas.VehicleCreate, 
    current_user: models.User = Depends(auth.get_current_user), 
    db: Session = Depends(get_db)
):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == item_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Item not found")
    if current_user.role != "admin" and vehicle.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this item")
    
    for key, value in item.dict(exclude_unset=True).items():
        setattr(vehicle, key, value)
    db.commit()
    db.refresh(vehicle)
    return vehicle

@app.delete("/api/items/{item_id}")
def delete_vehicle(item_id: int, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.id == item_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Item not found")
    if current_user.role != "admin" and vehicle.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this item")
    
    db.delete(vehicle)
    db.commit()
    return {"message": "Item deleted successfully"}
