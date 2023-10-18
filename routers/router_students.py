from uuid import uuid4
from fastapi import APIRouter, HTTPException
from classes.database import Student, students
from classes.models import StudentNoID
from database.firebase import db

#api init (launch with uvicorn main:api --reload)
router = APIRouter(
    prefix='/students',
    tags=['Students']
)


# Verbs + Endpoints
@router.get("/", response_model=list[Student])
async def get_student():
    queryResults = db.child("students").get().val()
    if not queryResults : return []
    studentArray = [value for value in queryResults.values()]
    return studentArray

# 1. Exercice (10min) Create new Student: POST
#connecter la vraie DB (10 min)
@router.post("/", status_code=201, response_model=Student)
async def create_student(student: StudentNoID):
    generatedId=str(uuid4())
    newStudent = Student (id=generatedId, name=student.name)
    db.child("students").child(generatedId).set(newStudent.model_dump())
    return newStudent

# 2. Exercice (10min) Student GET by ID
#connecter la vraie DB (10 min)
@router.get("/{student_id}", response_model=Student)
async def get_student_by_id(student_id: str):
    queryResult = db.child('students').child(student_id).get().val()
    if not queryResult : raise HTTPException(status_code=404, detail="Student not found") 
    return queryResult

# 3. Exercice (10min) PATCH Student (name)
#connecter la vraie DB (10 min)
@router.patch("/{student_id}", response_model=Student)
async def student_update(student_id: str, student: StudentNoID):
    queryResult = db.child('students').child(student_id).get().val()
    if not queryResult : raise HTTPException(status_code=404, detail="Student not found") 
    updatedStudent = Student(id=student_id, **student.model_dump())
    return db.child('students').child(student_id).update(updatedStudent.model_dump())

# 4. Exercice (10min) DELETE Student
#connecter la vraie DB (10 min)
@router.delete("/{student_id}", status_code=202, response_model=None)
async def student_delete(student_id) :
    queryResult = db.child('students').child(student_id).get().val()
    if not queryResult : 
        raise HTTPException(status_code=404, detail="Student not found")
    db.child('students').child(student_id).remove()
    return {"message": "Student deleted"}


#'Students' auront des 'Attendances' pour des 'Sessions'
# utilisateurs, lien vers une ressource
# API vendu à des centre de formations ... 'Center' -> Sessions + Students -> Attendences