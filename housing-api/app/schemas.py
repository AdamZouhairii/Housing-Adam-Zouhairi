from pydantic import BaseModel

class HouseBase(BaseModel):
    """
    Classe de base pour représenter les informations d'une maison.

    Attributs:
        longitude (float): La longitude de la maison.
        latitude (float): La latitude de la maison.
        housing_median_age (int): L'âge médian des logements dans la zone.
        total_rooms (int): Le nombre total de pièces dans la maison.
        total_bedrooms (int): Le nombre total de chambres dans la maison.
        population (int): La population dans la zone de la maison.
        households (int): Le nombre de ménages dans la zone de la maison.
        median_income (float): Le revenu médian des ménages dans la zone.
        median_house_value (float): La valeur médiane de la maison.
        ocean_proximity (str): La proximité de la maison par rapport à l'océan.
    """
    longitude: float
    latitude: float
    housing_median_age: int
    total_rooms: int
    total_bedrooms: int
    population: int
    households: int
    median_income: float
    median_house_value: float
    ocean_proximity: str

class HouseCreate(HouseBase):
    pass

class House(HouseBase):
    id: int

    class Config:
        orm_mode = True