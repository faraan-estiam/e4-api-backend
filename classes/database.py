#Model Pydantic = Datatype
from uuid import uuid4
from classes.models import Student

students = [
    Student(id=str(uuid4()), name='Adama'),
    Student(id=str(uuid4()), name='Adrien'),
    Student(id=str(uuid4()), name='Akbar'),
]