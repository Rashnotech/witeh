#!/usr/bin/env python3
"""a module for product models"""
from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, Field, validator
from .base import TimestampModel
from datetime import datetime


class ProductStatus(str, Enum):
    SOLD_OUT = "sold-out"
    IN_STOCK = "in-stock"

class Product(TimestampModel):
    id: str = Field(default_factory=str, alias="_id")
    product_name: str
    SKU: str
    price: float
    discount: int = 0
    quantity: int = 1
    description: Optional[str]
    weight: Optional[int]
    category_id: str
    tag_id: str
    published: bool = False
    status: ProductStatus = ProductStatus.IN_STOCK
    images: List[str] = []

    @validator('price')
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError('Price must be greater than zero')
        return v

    @validator('discount')
    def validate_discount(cls, v):
        if not 0 <= v <= 100:
            raise ValueError('Discount must be between 0 and 100')
        return v



# Properties to receive on product creation
class ProductCreate(Product):
    pass

# Properties to receive on product update
class ProductUpdate(BaseModel):
    product_name: Optional[str] = None
    price: Optional[float] = None
    discount: Optional[int] = None
    quantity: Optional[int] = None
    description: Optional[str] = None
    published: Optional[bool] = None
    status: Optional[str] = None

# Properties to return to client
class ProductResponse(Product):
    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "507f1f77bcf86cd799439011",
                "product_name": "Gaming Laptop",
                "SKU": "LAP-001",
                "price": 999.99,
                "description": "High-performance gaming laptop",
                "category_id": "electronics",
                "created_at": "2023-01-01T00:00:00"
            }
        }