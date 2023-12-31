import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url = os.getenv("DATABASE_URL", "")

settings = Settings()