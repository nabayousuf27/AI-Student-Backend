from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import EmailStr


app = FastAPI()

# @app.get("/")
# def Home(): 
#     return {"messsage":"welcome to fastApi"}

class Student(BaseModel):
    id:int
    name:str
    age: int
    department:str
    email: str
    graduated: bool=False

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
    
@app.get("/students/search")             #Query params automatically work like:
def search_student(student_name: str):  #/student/search?name=Ali
    searchList=[]
    for s in students:
        if student_name.lower() in s.name.lower():
            searchList.append(s)
    return searchList

@app.get("/students/summary")
def get_students_summary():
    num_of_graduates = 0 
    total = len(students)

    for s in students:
        if s.graduated:
            num_of_graduates += 1
    return {
        "total":total,
        "num_of_graduates":num_of_graduates
        }
#or
# @app.get("/students/summary")
# def student_summary():
#     total = len(students)
#     graduates = sum(1 for s in students if s.is_graduate)
    
#     return {
#         "total_students": total,
#         "graduates": graduates
#     }