from pydantic import BaseModel

class HouseBase(BaseModel):
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