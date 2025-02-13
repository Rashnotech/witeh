#!/usr/bin/env python3
"""a module for database operations"""
from motor.motor_asyncio import AsyncIOMotorClient # type: ignore

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "ecommerce"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]
