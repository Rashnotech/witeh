#!/usr/bin/env python3
"""a module to store token"""
from datetime import datetime, timezone, timedelta
from bson import ObjectId # type: ignore
from typing import Optional
from models.token import TokenData, StoredToken
from motor.motor_asyncio import AsyncIOMotorDatabase # type: ignore
from auth.jwt import create_access_token, decode_access_token


class TokenService:
    """a class to manage token"""

    def __init__(self, db: AsyncIOMotorDatabase):
        """initialization method"""
        self.db = db
        self.collection = db.refresh_tokens

    async def revoke_refresh_token(self, email: str) -> bool:
        """Revoke all refresh tokens for a user"""
        result = await self.collection.update_many(
            {"email": email},
            {"$set": {"is_revoked": True}}
        )
        return result.modified_count > 0
    
    async def create_refresh_token(self, email: str, role: str)-> str:
        """Create a refresh token"""
        refresh_token = create_access_token(
            {"sub": {"email": email, "role": role}},
            timedelta(days=7))
        
        stored_token = StoredToken(
            email=email,
            role=role,
            refresh_token=refresh_token,
            expires_at=datetime.now() + timedelta(days=7)
        )
        await self.collection.delete_many({"email": email})
        await self.collection.insert_one(stored_token.dict())
        return refresh_token
    
    async def verify_refresh_token(self, refresh_token: str) -> Optional[TokenData]:
        """Verify a refresh token"""
        payload = decode_access_token(refresh_token)
        token_data = payload.get("sub")
        if token_data is None:
            return None
        
        stored_token = await self.collection.find_one({
            "email": token_data["email"],
            "refresh_token": refresh_token,
            "is_revoked": False
            })
        if not stored_token:
            return None
        
        if stored_token["expires_at"] < datetime.now(timezone.utc):
            await self.collection.delete_one({"_id": ObjectId(stored_token["_id"])})
            return None
        
        return TokenData(
            email= token_data["email"],
            role= token_data["role"],
            exp= stored_token["expires_at"]
        )