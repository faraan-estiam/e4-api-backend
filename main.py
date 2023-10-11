from fastapi import FastAPI

#importing routers
import routers.router_students

# Documentation
from documentation.description import api_description
from documentation.tags import tags_metadata

#api init (launch with uvicorn main:api --reload)
api = FastAPI( 
    title="Watches API",
    description=api_description,
    openapi_tags=tags_metadata # tagsmetadata definit au dessus
    )

api.include_router(routers.router_students.router)

#'Students' auront des 'Attendances' pour des 'Sessions'
# utilisateurs, lien vers une ressource
# API vendu à des centre de formations ... 'Center' -> Sessions + Students -> Attendences