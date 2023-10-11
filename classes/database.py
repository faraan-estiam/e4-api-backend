#Model Pydantic = Datatype
from uuid import uuid4
from classes.models import Student

students = [
    Student(id=uuid4(), name='Adama'),
    Student(id=uuid4(), name='Adrien'),
    Student(id=uuid4(), name='Akbar'),
]