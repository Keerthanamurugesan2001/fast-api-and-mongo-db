
from fastapi import FastAPI, Body, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager

from model import User
from settings import connection_string



app = FastAPI(
    title="Course API",
    summary="Mongo db try",
)

app.mongodb_client = AsyncIOMotorClient(connection_string)
app.db = app.mongodb_client.students_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup_db_client(app)
    yield
    await shutdown_db_client(app)

# method for start the MongoDb Connection
async def startup_db_client(app):
    app.mongodb_client = AsyncIOMotorClient(
        "mongodb+srv://UserName:Password@cluster0.abc.mongodb.net/")
    app.mongodb = app.mongodb_client.get_database("college")
    print("MongoDB connected.")

# method to close the database connection
async def shutdown_db_client(app):
    app.mongodb_client.close()
    print("Database disconnected.")



