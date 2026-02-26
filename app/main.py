from fastapi import FastAPI
from sqlalchemy import text
from .database import engine

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is working!"}

@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database_response": str(result.scalar())}
