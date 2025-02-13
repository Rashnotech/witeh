#!/usr/bin/env python3
"""a module for database operations"""
from motor.asyncio import AsyncIOMotorClient # type: ignore

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "fastapi"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]