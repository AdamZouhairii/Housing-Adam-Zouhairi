import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()  #  charge les variables d'environnement

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
# Modification ici : "db" au lieu de "localhost"
DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "housing_db")

# construis l'URL de la base de données
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# crée le moteur de base de données
engine = create_engine(DATABASE_URL)
# configure la session locale
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#  déclare la base
Base = declarative_base()