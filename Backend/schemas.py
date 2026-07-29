from pydantic import BaseModel

class CityCreate(BaseModel):
    city_name: str
    state: str
    population: int
    famous_place: str

class CityResponse(CityCreate):
    id: int

    class Config:
        from_attributes = True
        #orm_mode = True if using Pydantic v1, for v2 use from_attributes = True