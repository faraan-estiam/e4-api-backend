from pydantic import BaseModel
from uuid import UUID

class Student(BaseModel):
    id: UUID
    name: str