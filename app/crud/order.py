#!/usr/bin/env python3
"""CRUD operations for order"""
from typing import List, Optional, Dict, Any
from bson import ObjectId
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.order import OrderCreate, OrderUpdate
from datetime import datetime

class OrderCRUD:

    def __init__(self, db: AsyncIOMotorDatabase):
        """initialization"""
        self.db = db
        self.collection = db.orders

    async def create(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new order."""
        order_dict = order
        result = await self.collection.insert_one(order_dict)
        created_order = await self.collection.find_one({"_id": result.inserted_id})
        created_order["_id"] = str(created_order["_id"])
        return created_order