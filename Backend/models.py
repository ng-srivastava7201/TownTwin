from sqlalchemy import Column, Integer, String, Text
from pymysql import Timestamp
from database import Base

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    city_name = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    population = Column(Integer)
    famous_place = Column(String(200))


class Area(Base):
    __tablename__ = "areas"

    area_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    latitude = Column(Integer)
    longitude = Column(Integer)

class Accident(Base):
    __tablename__ = "accident_history"

    id = Column(Integer, primary_key=True, index=True)
    road_id = Column(Text, nullable=False)
    severity = Column(Text)
    timestamp = Column(Timestamp)

    __tablename__ = "accident_risk_predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    road_id = Column(Text, nullable=False)
    risk_probability = Column(float)
    generated_at = Column(Timestamp)

class Energy(Base):
    __tablename__ = "energy_data"

    id = Column(Integer, primary_key=True, index=True)
    area = Column(String(100), nullable=False)
    power_usage_kwh = Column(Integer)
    timestamp = Column(Integer)


    __tablename__ = "energy_predictions"

    id = Column(Integer, primary_key=True, index=True)
    area = Column(String(100), nullable=False)
    power_usage_kwh = Column(Integer)
    timestamp = Column(Timestamp)
