from fastapi import FastAPI
from app.db import database, User
from app.kafka_consumer import kafka_consumer
app = FastAPI(title="Notification service..")
import asyncio

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.on_event("startup")
async def startup():
    asyncio.create_task(kafka_consumer())
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()