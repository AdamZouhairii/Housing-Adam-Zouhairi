from fastapi import FastAPI
from app import routers

# Crée une instance de la classe FastAPI
app = FastAPI(title="Housing API")

# Inclue le routeur du module routers
app.include_router(routers.router)