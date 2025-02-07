#!/usr/bin/env python3
"""a module for product models"""
from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, Field
from .base import TimestampModel


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

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "product_name": "Gaming Laptop",
                "SKU": "LAP-001",
                "price": 999.99,
                "description": "High-performance gaming laptop",
                "category_id": "electronics"
            }
        }
