from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

@app.get("/")
def home():
    return {"message": "Backend is working with DB!"}

@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database_response": str(result.scalar())}
