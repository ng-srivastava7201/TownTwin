from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, get_db
import models
import schemas
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Twin City Backend")

@app.get("/")
def home():
    return {"message": "Twin City Backend"}

@app.post("/cities", response_model=schemas.CityResponse)
def create(city: schemas.CityCreate, db: Session = Depends(get_db)):
    return crud.create_city(db, city)

@app.get("/cities", response_model=list[schemas.CityResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_all_cities(db)

@app.get("/cities/{city_id}", response_model=schemas.CityResponse)
def read_one(city_id: int, db: Session = Depends(get_db)):
    city = crud.get_city(db, city_id)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return city

@app.put("/cities/{city_id}", response_model=schemas.CityResponse)
def update(city_id: int, city: schemas.CityCreate, db: Session = Depends(get_db)):
    updated = crud.update_city(db, city_id, city)
    if updated is None:
        raise HTTPException(status_code=404, detail="City not found")
    return updated

@app.delete("/cities/{city_id}")
def delete(city_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_city(db, city_id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="City not found")
    return {"message": "City deleted successfully"}