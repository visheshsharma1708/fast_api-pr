from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str
class ShowBlog(BaseModel):
    title:str
    body:str
    class config():
        orm_mode=True

class user(BaseModel):
    name:str
    email:str
    password:str