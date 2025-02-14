#!/usr/bin/env python3
"""a module for configuration settings"""
from typing import List
from pydantic_settings import BaseSettings #type: ignore


class Settings(BaseSettings):
    PROJECT_NAME: str = "Witeh Ecommerce API"
    PROJECT_VERSION: str = "1.0"
    PROJECT_DESCRIPTION: str = "Ecommerce REST API built with FastApi and MongoDB"
    API_V1_STR: str = "/api/v1"
    MONGODB_URL: str
    DATABASE_NAME: str = "witeh_db"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    MAIL_USERNAME: str = 'help@prospertyhomes.com'
    MAIL_PASSWORD: str = 'prospertyhomes@2024'
    MAIL_FROM: str = 'prospertyhomes.com'
    MAIL_PORT: int = 465
    MAIL_SERVER: str = "prospertyhomes.com"
    MAIL_TLS: bool = True
    MAIL_SSL: bool = True
    MAIL_FROM_NAME: str = "Witeh Ecommerce"

    class Config:
        env_file = ".env"


settings = Settings()