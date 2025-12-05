from fastapi import FastAPI  #core framework for apis
from pydantic import BaseModel  #basemodel helps with validation , all python webbreq there will be some data and there will be some data that i will send so the dtaa that i will send it shoukdl have some structure ans syntax so for that structure syntax guidelinew e can use pydantic , there are some default strycture stytax that we will use
from typing import List

app = FastAPI()

#model#data structure using pydantic
class Tea(BaseModel):
    id: int
    name: str
    origin: str

#no database so using this array
teas = []
#type defining
teas: List[Tea] = []

#decorater : give superpower to your functions

@app.get('/')  #this is decorator for home route
def read_root():  #method definition
    return {"message":"welcome to tea house"}

@app.get('/teas')
def get_teas():
    return teas

@app.post("/teas")
def add_tea(tea:Tea):  #when req will come it will come with some data which is tea and we are defining its type that it should be of Tea type means all three feilds will be in it
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int , updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = update_tea
            return update_tea
    return {"error": "not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id:int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deletedItem = teas.pop(index)
            return {"message": "dleted successfully"} 
    return {"message": "no tea found"}        

