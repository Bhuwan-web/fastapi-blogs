from pydantic import BaseModel


class BlogModel(BaseModel):
    title: str
    body: str
    author: str
    published: bool | None
