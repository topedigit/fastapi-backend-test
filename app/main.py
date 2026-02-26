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


from .database import Base, engine
from . import models

Base.metadata.create_all(bind=engine)


from .routes import users

app.include_router(users.router)

@app.get("/tables")
def check_tables():
    with engine.connect() as connection:
        result = connection.execute(text(
            "SELECT tablename FROM pg_tables WHERE schemaname='public';"
        ))
        return {"tables": [row[0] for row in result]}
