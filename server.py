from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# @app.get("/")
# def Home(): 
#     return {"messsage":"welcome to fastApi"}

class Student(BaseModel):
    id:int
    name:str
    age: int
    department:str

students = []

@app.post("/student")
def addStudent(student : Student):
    for s in students:
        if s.id == student.id:
            return {"message": "Students id already exist"}
    else:
        students.append(student)

    return {"message":"Student added succesfully" , "student": student}

@app.get("/student")
def get_students():
    return students

@app.delete("/students/{student_id}")
def delete_student(student_id : int):
    for s in students:
        if s.id == student_id:
            students.remove(s)
            return {"message":"Student deleted succesfully"}
    return {"message":"Student does not exist "}

@app.put("/students/{student_id}")
def update_student(student_id: int , update_value: Student):
    for i, s in enumerate (students):
        if s.id == student_id:
            students[i] = update_value
            return {"message":"studnet updated succesfully"}
    return{"error":"student mot found"}
    



