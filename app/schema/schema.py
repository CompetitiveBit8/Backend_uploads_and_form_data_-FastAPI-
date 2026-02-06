from pydantic import BaseModel
from typing import Optional

class UserLogin(BaseModel):
    username: str
    password: str

class ImageSchema(BaseModel):
    file_path: str
    file_name: str
    file_type: str

class PostSchema(BaseModel):
    title: str
    content: str
    author: str