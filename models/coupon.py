#!/usr/bin/env python3
"""a module for coupon models"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from .base import TimestampModel


class Coupon(TimestampModel):
    id: str = Field(default_factory=str, alias="_id")
    code: str
    description: Optional[str]
    discount: int
    type: str
    times_used: int = 0
    max_usage: int
    start_date: datetime
    end_date: datetime
    active: bool = True