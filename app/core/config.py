#!/usr/bin/env python3
from typing import List
from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    PROJECT_NAME: str = "Witech Ecommerce API"
    PROJECT_VERSION: str = "1.0"
    PROJECT_DESCRIPTION: str = "Ecommerce REST API built with FastApi and MongoDB"
    API_V1_STR: str = "/api/v1"
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "witech_ecommerce"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Setting()