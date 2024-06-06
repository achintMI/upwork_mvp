from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import crud, schemas, auth
from ..dependencies import get_db
from ..auth import get_current_user
from cachetools import TTLCache, cached

router = APIRouter()

cache = TTLCache(maxsize=100, ttl=300)


@router.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(get_current_user)):
    return crud.create_post(db=db, post=post, user_id=current_user.id)


@cached(cache)
def get_cached_posts(db: Session, user_id: int):
    return crud.get_posts(db=db, user_id=user_id)


@router.get("/posts/", response_model=list[schemas.Post])
def read_posts(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return get_cached_posts(db, current_user.id)


@router.delete("/posts/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    post = crud.delete_post(db=db, post_id=post_id, user_id=current_user.id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    if current_user.id in cache:
        del cache[current_user.id]
    return post
