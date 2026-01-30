from urllib import response
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schemas, auth, ai_services
from database import engine, get_db
from ai_services import generate_welcome_message
from models import User
from schemas import UserCreate, UserResponse

models.Base.metadata.create_all(bind=engine)  # creates tables

app = FastAPI(title="User Registration with AI Welcome Message")

@app.post("/register", response_model=schemas.UserResponse, status_code=201)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if username/email exists
    existing = db.query(models.User).filter(
        (models.User.username == user.username) | (models.User.email == user.email)
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username or email already registered")

    #  Hash the password
    hashed_password = auth.get_password_hash(user.password)

    #  Create DB user
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # # Generate AI welcome message(Hard coded)
    # welcome_message = ai_services.generate_welcome_message(user.username)
    # response = schemas.UserResponse.model_validate(db_user)
    # response.welcome_message = f"Welcome {db_user.username}! 🎉 AI is happy to have you."

    # return response

    # Generate AI welcome message
    welcome_msg = ai_services.generate_welcome_message(db_user.username)

    # return UserResponse(
    #     id=db_user.id,
    #     username=db_user.username,
    #     email=db_user.email,
    #     role=db_user.role,
    #     is_active=db_user.is_active,
    #     welcome_message=welcome_msg
    # )
    response = schemas.UserResponse.model_validate(db_user)
    return response

