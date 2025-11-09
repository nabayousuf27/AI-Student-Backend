#Book mangemnet API

from fastapi import FastAPI 
from pydantic import BaseModel,Field  
from typing import List, Optional

app = FastAPI()

class Book(BaseModel):
    id : int
    title : str
    author : str
    price : float = Field(..., gt=0, description ="price must be greater than 0")
    in_stock : bool=False
    published_year: Optional[int] = None

books: List[Book] = []
#add new book ,get book,  delete book , update book 

@app.get("/books")
def get_books():
    return books

@app.post("/books")
def add_newBook(book: Book):
    for b in books:
        if b.id == book.id:
            return {"error":"the book id already exist"}
    books.append(book)   
    return {"message": "Book added successfully", "book": book}

@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    for index , b in enumerate(books):
        if b.id == book_id:
            deleted_item = books.pop(index)
            return {"message":"book delted succesfully"}        
    return{"error":"book not found"}
    

@app.put("/books/{book_id}")
def update_book(book_id:int, update_value: Book):
    for index , b in enumerate(books):
        if b.id == book_id:
            books[index] = update_value
            return update_value 
    return{"error":"book not found"}



