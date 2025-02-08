#!/usr/bin/env python3
"""crud operations for user"""
from typing import List, Optional, Dict, Any
from bson import ObjectId
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase


class UserCRUD:

    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection = db.users

    async def create(self, user: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new user."""
        user_dict = user
        if await self.collection.find_one({"email": user_dict["email"]}):
            raise HTTPException(
                status_code=400,
                detail="User with this email already exists"
            )
        result = await self.collection.insert_one(user_dict)
        created_user = await self.collection.find_one({"_id": result.inserted_id})
        created_user["_id"] = str(created_user["_id"])
        return created_user