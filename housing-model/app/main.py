from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import numpy as np

app = FastAPI(title="Housing Model Inference API")

# Charger le modèle depuis MLflow (chemin local ou via le tracking server)
model = mlflow.sklearn.load_model("model")

class HouseFeatures(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: int
    total_rooms: int
    total_bedrooms: int
    population: int
    households: int
    median_income: float

@app.post("/predict")
def predict(features: HouseFeatures):
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
    prediction = model.predict(data)
    return {"predicted_median_house_value": prediction[0]}