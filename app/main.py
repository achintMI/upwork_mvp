from fastapi import FastAPI
from .routes import auth, posts
from .dependencies import engine
from .models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
