from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal, engine

router = APIRouter()

# Créer la table si non existante (pour développement)
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/houses", response_model=list[schemas.House])
def get_houses(db: Session = Depends(get_db)):
    houses = db.query(models.House).all()
    return houses

@router.post("/houses", response_model=schemas.House)
def create_house(house: schemas.HouseCreate, db: Session = Depends(get_db)):
    db_house = models.House(**house.dict())
    db.add(db_house)
    db.commit()
    db.refresh(db_house)
    return db_house