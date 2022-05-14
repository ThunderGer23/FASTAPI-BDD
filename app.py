from fastapi import FastAPI
from routes.npm import npm
from routes.hero import hero
from routes.steam import steam
from routes.files import files
from routes.github import github
from routes.medium import medium
from routes.programming import programming
from documentation.docs import tags_metadata

app = FastAPI(
    title = 'API con FastAPI para la recopilación y administración de información sobre diversos temas',
    description = 'Esta API es producto del proyecto final de BDD para la integración de una Base de Datos Distribuida',
    version = '1.2',
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "ThunderGer",
        "url": "http://x-force.example.com/contact/",
        "email": "ThunderGer@outlook.com",
    },
    license_info={
        'name': 'MIT License',
        'url': 'https://opensource.org/licenses/MIT'
    },
    openapi_tags= tags_metadata
)

app.include_router(npm)
app.include_router(hero)
app.include_router(steam)
app.include_router(files)
app.include_router(github)
app.include_router(medium)
app.include_router(programming)