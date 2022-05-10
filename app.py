from fastapi import FastAPI
from routes.hero import hero

app = FastAPI()

app.include_router(hero)