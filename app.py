from fastapi import FastAPI
from routes.hero import hero
from routes.github import github
from routes.medium import medium
from routes.files import files
from documentation.docs import tags_metadata

app = FastAPI(
    title = 'API con FastAPI para la recopilación y administración de información sobre diversos temas',
    description = 'Esta API es producto del proyecto final de BDD para la integración de una Base de Datos Distribuida',
    version = '1.2',
    openapi_tags= tags_metadata
)

app.include_router(hero)
app.include_router(files)
app.include_router(github)
app.include_router(medium)