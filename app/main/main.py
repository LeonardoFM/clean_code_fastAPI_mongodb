import os
from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv

from app.main.routes import vehicles_routes

load_dotenv()

app = FastAPI()
app.include_router(vehicles_routes.vehicles_router)

client = MongoClient(os.environ.get("MONGODB_URI"))
# app.db = client.get_default_database()
