from fastapi import FastAPI
from app import routers

app = FastAPI(title="Housing API")

app.include_router(routers.router)