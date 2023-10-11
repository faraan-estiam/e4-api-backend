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

# Reste à faire 
# X Sortir mon student's router dans un dossier "routers"
# X Rédiger une documentation et l'ajouter à mon app FastAPI()
# X Sortir mes pydantic models dans un dossier classes
# X Ajouter les tags 


# - et description pour chaque endpoing/methods
# - En ajouter suivant votre projet


# Spécification...
# "Students" auront des "Attendances" pour des "Sessions"
# Utilisateurs, lien vers une ressource
# API vendu à des centre de formations ... "Center" -> Sessions + Students -> Attendances
