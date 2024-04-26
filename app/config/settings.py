import os
from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):

    # App
    APP_NAME:  str = os.environ.get("APP_NAME", "ShariaScreener")
    DEBUG: bool = bool(os.environ.get("DEBUG", False))

    # MySql Database Config
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_USERNAME: str = os.environ.get("DB_USERNAME")
    DB_PASS: str = os.environ.get("DB_PASSWORD")
    DB_PORT: int = int(os.environ.get("DB_PORT"))
    DB_NAME: str = os.environ.get("DB_NAME")
    DATABASE_URL: str = f"postgresql://{DB_USERNAME}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # App Secret Key
    SECRET_KEY: str = os.environ.get(
        "SECRET_KEY", "8deadce9449770680910741063cd0a3fe0acb62a8978661f421bbcbb66dc41f1")


@lru_cache()
def get_settings() -> Settings:
    return Settings()
