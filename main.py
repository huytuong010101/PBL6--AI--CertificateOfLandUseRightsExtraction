from fastapi import FastAPI
from routes.api import app as api_router

app = FastAPI()
app.include_router(api_router, prefix="/app")
