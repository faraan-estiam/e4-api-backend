from pydantic import BaseModel

class Student(BaseModel):
    id: str
    name: str

class StudentNoID(BaseModel):
    name:str

class User(BaseModel):
    email: str
    password: str