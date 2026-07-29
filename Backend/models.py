from sqlalchemy import Column, Integer, String, Text
from pymysql import Timestamp
from database import Base

'''class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    city_name = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    population = Column(Integer)
    famous_place = Column(String(200))'''


class Area(Base):
    __tablename__ = "areas"

    area_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    latitude = Column(Integer)
    longitude = Column(Integer)

class Weather(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    area = Column(Text, nullable=False)
    temperature = Column(Integer)
    humidity = Column(Integer)
    windspeed = Column(Integer)
    rainfall=Column(Integer)
    timestamp = Column(Timestamp)


class Pollution(Base):
    __tablename__ = "pollution_data"

    id = Column(Integer, primary_key=True, index=True)
    area = Column(String(100), nullable=False)
    aqi = Column(Integer)
    pm2_5 = Column(Integer)
    pm10 = Column(Integer)
    timestamp = Column(Timestamp)


    __tablename__ = "pollution_predictions"

    id = Column(Integer, primary_key=True, index=True)
    area = Column(String(100), nullable=False)
    predicted_aqi = Column(Integer)
    risk_level = Column(Timestamp)
    predicted_for = Column(Timestamp)
    generated_at = Column(Timestamp)

class Traffic(Base):
    __tablename__ = "traffic_data"
    
    id = Column(Integer, primary_key=True, index=True)
    road_id = Column(String(100), nullable=False)
    area = Column(Integer)
    vehicle_count = Column(Integer)
    average_speed=Column(Integer)
    timestamp = Column(Timestamp)


    __tablename__ = "traffic_predictions"

    id = Column(Integer, primary_key=True, index=True)
    road_id = Column(String(100), nullable=False)
    predicted_vehicle_count = Column(Integer)
    predicted_status=Column(String(100))
    predicted_for = Column(Timestamp)
    generated_at = Column(Timestamp)