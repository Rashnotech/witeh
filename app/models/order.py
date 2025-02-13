#!/usr/bin/env python3
"""a module for order models"""
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field
from .base import TimestampModel
from datetime import datetime


class OrderStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    IN_TRANSIT = "in-transit"
    DELIVERED = "delivered"

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float
    total: float

class ShippingAddress(BaseModel):
    address_line1: str
    address_line2: Optional[str]
    postal_code: str
    city: str
    country: str

class Order(TimestampModel):
    id: str = Field(default_factory=str, alias="_id")
    customer_id: str
    items: List[OrderItem]
    shipping_address: ShippingAddress
    total_amount: float
    coupon_id: Optional[str]
    affiliate_code: Optional[str]
    order_status: OrderStatus = OrderStatus.PENDING
    carrier_name: Optional[str]
    delivery_date: Optional[datetime]


class OrderCreate(Order):
    pass
   


class OrderUpdate(BaseModel):
    items: List[OrderItem]
    shipping_address: ShippingAddress
    total_amount: float
    coupon_id: Optional[str]
    affiliate_code: Optional[str]
    order_status: OrderStatus
    carrier_name: Optional[str]
    delivery_date: Optional[datetime]

class OrderResponse(Order):
    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "customer_id": "user123",
                "items": [
                    {
                        "product_id": "prod123",
                        "quantity": 1,
                        "price": 999.99,
                        "total": 999.99
                    }
                ],
                "shipping_address": {
                    "address_line1": "123 Main St",
                    "postal_code": "12345",
                    "city": "New York",
                    "country": "USA"
                },
                "total_amount": 999.99
            }
        }
