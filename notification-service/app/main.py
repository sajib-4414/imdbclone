from fastapi import FastAPI
from app.kafka_consumer import kafka_consumer
from concurrent.futures import ThreadPoolExecutor
from tortoise import Tortoise
from app.config import settings
from app.db import User


app = FastAPI(title="Notification service.....")

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
    await Tortoise.init(
        db_url=settings.db_url,
        modules={'models': ['app.db']}
    )
    await Tortoise.generate_schemas()
    user = await User.get_or_create(email="test@test.com", username="test")
    print("priting new new user")
    print(user)


@app.on_event("shutdown")
async def shutdown():
    global kafka_consumer_task

    if kafka_consumer_task:
        kafka_consumer_task.cancel()
