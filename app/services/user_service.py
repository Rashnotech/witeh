#!/usr/bin/env python3
"""crud operations for user"""
from typing import List, Optional, Dict, Any
from bson import ObjectId # type: ignore
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase # type: ignore


class UserService:
    """A class for user service"""

    def __init__(self, db: AsyncIOMotorDatabase):
        """initialization method"""
        self.db = db
        self.collection = db.users

    async def create(self, user: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new user."""
        # - buyer, affiliate, store-owner, admin
        # - google, email
        user_dict = user
        if user["auth_provider"] == "google":
            pass
        if await self.collection.find_one({"email": user_dict["email"]}):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists"
            )
        result = await self.collection.insert_one(user_dict)
        created_user = await self.collection.find_one({"id": result.inserted_id})
        created_user["_id"] = str(created_user["_id"])
        return created_user
    
    async def get(self, id: str) -> Optional[Dict[str, any]]:
        """get user by id"""
        try:
            user = self.collection.find_one({"_id": ObjectId(id)})
            user["_id"] = str(user["_id"])
            return user
        except:
            return None
        
    async def findby_email(self, email: str) -> Optional[Dict[str, Any]]:
        """find user by email"""
        user = await self.collection.find_one({"email": email})
        if user:
            user["_id"] = str(user["_id"])
        return user