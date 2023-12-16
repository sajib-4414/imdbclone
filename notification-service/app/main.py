from fastapi import FastAPI
from app.db import database, User
from app.kafka_consumer import kafka_consumer
from concurrent.futures import ThreadPoolExecutor
app = FastAPI(title="Notification service......")
# Store the task globally
kafka_consumer_task = None
import asyncio

@app.get("/")
async def read_root():
    return {"hello": "world......"}

@app.on_event("startup")
async def startup():
    global kafka_consumer_task
    kafka_consumer_task = asyncio.create_task(kafka_consumer())
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    global kafka_consumer_task

    if kafka_consumer_task:
        kafka_consumer_task.cancel()
    if database.is_connected:
        await database.disconnect()
