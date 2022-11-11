from fastapi import APIRouter

from routes import full_pipeline

app = APIRouter()

app.include_router(full_pipeline.router, tags=["Text detection"], prefix="/app")