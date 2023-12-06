import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # db_url: str = Field(..., env='DATABASE_URL')
    db_url = "postgresql://root:root@notification-db:5432/notification_db"

settings = Settings()