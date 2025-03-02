from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import numpy as np

# Crée une instance de l'application FastAPI avec un titre
app = FastAPI(title="Housing Model Inference API")

# Charge le modèle depuis le dossier "model"
model = mlflow.sklearn.load_model("model")

# Défini un modèle de données pour les caractéristiques de la maison
class HouseFeatures(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: int
    total_rooms: int
    total_bedrooms: int
    population: int
    households: int
    median_income: float

# Défini un endpoint POST pour les prédictions
@app.post("/predict")
def predict(features: HouseFeatures):
    # Converti les caractéristiques en un tableau numpy
    data = np.array([[
        features.longitude,
        features.latitude,
        features.housing_median_age,
        features.total_rooms,
        features.total_bedrooms,
        features.population,
        features.households,
        features.median_income
    ]])
    # Fait une prédiction avec le modèle chargé
    prediction = model.predict(data)
    # Retourne la valeur prédite
    return {"predicted_median_house_value": prediction[0]}