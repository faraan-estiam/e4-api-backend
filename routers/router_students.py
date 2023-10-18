from uuid import uuid4
from fastapi import APIRouter, HTTPException
from classes.database import Student, students
from database.firebase import db

#api init (launch with uvicorn main:api --reload)
router = APIRouter(
    prefix='/students',
    tags=['Students']
)


# Verbs + Endpoints
@router.get("/", response_model=list[Student])
async def get_student():
    return students

# 1. Exercice (10min) Create new Student: POST
@router.post("/", status_code=201, response_model=Student)
async def create_student(student_name: str):
    generatedId=str(uuid4())
    newStudent = Student (id=generatedId, name=student_name)
    students.append(newStudent)
    db.child("students").child(generatedId).set(newStudent.model_dump())
    return newStudent

# 2. Exercice (10min) Student GET by ID
@router.get("/{student_id}", response_model=Student)
async def get_student_by_id(student_id: str):
    for student in students :
        if student.id==student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")
# 3. Exercice (10min) PATCH Student (name)

@router.patch("/{student_id}", response_model=Student)
async def student_update(student_id: str, student_name: str):
    for student in students :
        if student.id==student_id:
            student.name = student_name
            return student
    raise HTTPException(status_code=404, detail="Student not found")

# 4. Exercice (10min) DELETE Student
@router.delete("/{student_id}", status_code=202, response_model=None)
async def student_delete(student_id) :
    for student in students:
        if student.id==student_id:
            students.remove(student)
            return
    raise HTTPException(status_code=404, detail="Student not found")


#'Students' auront des 'Attendances' pour des 'Sessions'
# utilisateurs, lien vers une ressource
# API vendu à des centre de formations ... 'Center' -> Sessions + Students -> Attendences