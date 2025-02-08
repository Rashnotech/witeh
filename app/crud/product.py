#!/usr/bin/env python3
"""CRUD operations for product"""
from typing import List, Optional, Dict, Any
from bson import ObjectId
from fastapi import HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from models.product import ProductCreate, ProductUpdate
from datetime import datetime

class ProductCRUD:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection = db.products

    async def create(self, product: ProductCreate) -> Dict[str, Any]:
        """Create a new product."""
        product_dict = product.dict()
        
        # Check if SKU already exists
        if await self.collection.find_one({"SKU": product_dict["SKU"]}):
            raise HTTPException(
                status_code=400,
                detail="Product with this SKU already exists"
            )
        
        result = await self.collection.insert_one(product_dict)
        
        # Get the created product
        created_product = await self.collection.find_one({"_id": result.inserted_id})
        created_product["_id"] = str(created_product["_id"])
        return created_product

    async def get(self, id: str) -> Optional[Dict[str, Any]]:
        """Get a product by ID."""
        try:
            product = await self.collection.find_one({"_id": ObjectId(id)})
            if product:
                product["_id"] = str(product["_id"])
            return product
        except:
            return None

    async def get_multi(
        self,
        skip: int = 0,
        limit: int = 100,
        filters: Dict[str, Any] = None
    ) -> List[Dict[str, Any]]:
        """Get multiple products with filtering."""
        cursor = self.collection.find(filters or {})
        cursor.skip(skip).limit(limit)
        
        products = []
        async for product in cursor:
            product["_id"] = str(product["_id"])
            products.append(product)
        return products

    async def update(self, id: str, product: ProductUpdate) -> Optional[Dict[str, Any]]:
        """Update a product."""
        update_data = {
            k: v for k, v in product.dict(exclude_unset=True).items()
            if v is not None
        }
        
        if not update_data:
            return None

        # Add updated_at timestamp
        update_data["updated_at"] = datetime.utcnow()

        result = await self.collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": update_data}
        )

        if result.modified_count:
            return await self.get(id)
        return None

    async def delete(self, id: str) -> bool:
        """Delete a product."""
        result = await self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

    async def search(self, query: str, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
        """Search products by text query."""
        cursor = self.collection.find(
            {"$text": {"$search": query}},
            {"score": {"$meta": "textScore"}}
        )
        cursor.sort([("score", {"$meta": "textScore"})])
        cursor.skip(skip).limit(limit)
        
        products = []
        async for product in cursor:
            product["_id"] = str(product["_id"])
            products.append(product)
        return products