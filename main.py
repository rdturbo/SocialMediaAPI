from turtle import title
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/posts")
def get_posts():
    return {"data": "posts"}


@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    return {"data": post}
