#!/usr/bin/env python3
"""a module for product models"""
from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    name: str
    description: Optional[str]
    price: float
    category: Optional[str] = None
    in_stock: bool = True


class ProductCreate(Product):
    pass


class ProductResponse(BaseModel):
    name: str
    description: Optional[str]
    price: float
    in_stock: bool