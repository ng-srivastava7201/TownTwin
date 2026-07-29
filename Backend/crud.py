from sqlalchemy.orm import Session
import models
import schemas

def create_city(db: Session, city: schemas.CityCreate):
    new_city = models.City(**city.model_dump())
    db.add(new_city)
    db.commit()
    db.refresh(new_city)
    return new_city

def get_all_cities(db: Session):
    return db.query(models.City).all()

def get_city(db: Session, city_id: int):
    return db.query(models.City).filter(models.City.id == city_id).first()

def update_city(db: Session, city_id: int, city: schemas.CityCreate):
    db_city = get_city(db, city_id)

    if db_city:
        db_city.city_name = city.city_name
        db_city.state = city.state
        db_city.population = city.population
        db_city.famous_place = city.famous_place

        db.commit()
        db.refresh(db_city)

    return db_city

def delete_city(db: Session, city_id: int):
    db_city = get_city(db, city_id)

    if db_city:
        db.delete(db_city)
        db.commit()

    return db_city