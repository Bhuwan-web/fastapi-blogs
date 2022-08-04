from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class BlogModel(BaseModel):
    title: str
    body: str
    published: bool | None


@app.get("/")
def index():
    return "Heyyyy"


@app.get("/messages/{id}")
def messages(id):
    return {"messsages": id}


@app.post("/blog")
async def create_blog(blog: BlogModel):
    return {
        "status": f"Created blog with title {blog.title} having body {blog.body} whose published status is {blog.published}"
    }
