from fastapi import Body, FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/posts")
def get_posts():
    return {"data": "posts"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title : {payload['title']} content: {payload['content']}"}
