from fastapi import FastAPI
from app.main.routes import routes

app = FastAPI()

app.include_router(routes.vehicles_router)
