from fastapi import FastAPI
from routes.hero import hero
from routes.github import github

app = FastAPI()

app.include_router(hero)
app.include_router(github)