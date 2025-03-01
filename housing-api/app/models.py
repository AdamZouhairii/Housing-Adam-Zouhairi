from sqlalchemy import Column, Float, Integer, String
from app.database import Base

class House(Base):
    __tablename__ = "houses"

    id = Column(Integer, primary_key=True, index=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    housing_median_age = Column(Integer, nullable=False)
    total_rooms = Column(Integer, nullable=False)
    total_bedrooms = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    households = Column(Integer, nullable=False)
    median_income = Column(Float, nullable=False)
    median_house_value = Column(Float, nullable=False)
    ocean_proximity = Column(String, nullable=False)