from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session
from . import schemas, models, database

models.Base.metadata.create_all(bind=database.engine)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.post("/blog", status_code=201)
def create_blog(req: schemas.BlogModel, db: Session = Depends(get_db)):
    new_blog = models.Blog(
        title=req.title,
        author=req.author,
        body=req.body,
        published=req.published,
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blogs")
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blogs/{id}")
def get_blog(id: int, res: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The user with specified id not found",
        )
    return blog
