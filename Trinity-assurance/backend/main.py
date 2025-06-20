# backend/main.py
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from dotenv import load_dotenv
from backend.routers import tests

load_dotenv()

app = FastAPI()

app.include_router(tests.router, prefix="/api/tests", tags=["Tests"])
