from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
from psycopg2.extras import RealDictCursor
import psycopg2
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str  
    published: bool = True

class updatePost(BaseModel):
    title: str
    content: str  
    published: bool = True
    rating: Optional[int] = None

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='Social Media Database', user='postgres', password="''''", cursor_factory=RealDictCursor)
        cursor = conn.cursor() 
        print("database connection was succesful")
        break
    except Exception as error:
        print("connecting to database failed")
        print("Error: ", error)
        time.sleep(3)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "My  First API"}







