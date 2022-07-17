import time
from fastapi import FastAPI, HTTPException, Response, Depends, status
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session

from app import models
from app.database import engine
from app.routers import post, user, auth

# from . import models, schemas, utils
# from .database import engine, get_db
# from .routers import user, post, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(
            host="localhost", database="socialMediaAPI", user="postgres",
            password="romel123", cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database was successfully connected")
        break
    except Exception as error:
        print("Connection to the database failed!!!")
        print(f"Error was {error}")
        time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
