from pydantic import BaseModel
from typing import Optional

class UserLogin(BaseModel):
    username: str
    password: str

class ImageSchema(BaseModel):
    # id: int
    file_path: str
    file_name: str
    file_type: str

class PostSchema(BaseModel):
    # id: int
    title: str
    content: str
    author: str