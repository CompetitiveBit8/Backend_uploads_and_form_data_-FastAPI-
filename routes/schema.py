from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class Post(BaseModel):
    title: str
    content: str
    author: str