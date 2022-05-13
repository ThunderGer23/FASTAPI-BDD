from fastapi import FastAPI
from routes.hero import hero
from routes.github import github
from routes.medium import medium
from routes.files import files

app = FastAPI()

app.include_router(hero)
app.include_router(files)
app.include_router(github)
app.include_router(medium)