from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management System")

@app.post("/students/", response_model=schemas.StudentResponse  , status_code=201)   #StudentResponse: Used for sending API data in responses
def create_student(student: schemas.StudentCreate, db:Session = Depends(get_db)):
    existing = db.query(models.Student).filter(
        models.Student.email == student.email
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail = "Email already regstered")

    db_student = models.Student(**student.model_dump())       
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# READ ALL
@app.get("/students/", response_model=List[schemas. StudentResponse])
def get_all_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()
#READ ONE
@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(
    models.Student.id == student_id
    ).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
# UPDATE
@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(
    student_id: int,
    student: schemas. StudentCreate,
    db: Session = Depends (get_db)
):
    db_student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()
    if not db_student:
        raise HTTPException (status_code=404, detail="Student not found")
    
    for key, value in student.model_dump().items():
        setattr(db_student, key, value)
    db.commit()
    db.refresh(db_student)
    return db_student

#DELETE
@app.delete("/students/{student_id}")
def delete_student (student_id: int, db: Session =  Depends (get_db)):
    db_student = db.query(models.Student).filter(
    models.Student.id == student_id
    ).first()

    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted cessfully"}    