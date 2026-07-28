from fastapi import FastAPI
app= FastAPI(title= "TownTwin Backend")

@app.get("/")
def home():
    return {
        "message": "townTwin Backend is running"
    }