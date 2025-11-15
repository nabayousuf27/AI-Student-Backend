#this is where we have to do configuration
#what is session: evertime u connect to esomething thatis a session , if u connect to server thas one session, if u connect to database thast one session, u need to create a session before u do these operations
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./students.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args = {"check_same_thread":False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind = engine )

Base = declarative_base

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

