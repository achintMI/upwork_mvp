from pydantic import BaseModel, EmailStr, constr


class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=64)

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    text: constr(min_length=1, max_length=1024)


class Post(BaseModel):
    id: int
    text: str
    owner_id: int

    class Config:
        orm_mode = True
