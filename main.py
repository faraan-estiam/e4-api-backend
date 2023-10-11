from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

#importing routers
import routers.router_students

#api init (launch with uvicorn main:api --reload)
api = FastAPI(
    title="e4 api backend"
)

api.include_router(routers.router_students.router)

#'Students' auront des 'Attendances' pour des 'Sessions'
# utilisateurs, lien vers une ressource
# API vendu à des centre de formations ... 'Center' -> Sessions + Students -> Attendences