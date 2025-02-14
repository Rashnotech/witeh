from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase # type: ignore
from app.core.config import settings


class Database:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

db = Database()

async def connect_to_mongo():
    """create database connection"""
    db.client = AsyncIOMotorClient(settings.MONGODB_URL)
    db.db = db.client[settings.DATABASE_NAME]


async def close_mongo_connection():
    """close database connection."""
    if db.client:
        db.client.close()