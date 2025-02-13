#!/usr/bin/env python3
"""a module for the tier system"""
from .base import TimestampModel
from typing import Text
from pydantic import BaseModel, Field
from .base import TimestampModel

class Tier(TimestampModel):
    """a class for business tiers"""
    id: str = Field(default_factory=str, alias="_id")
    tier: str
    price: float
    features: Text


class TierCreate(Tier):
    """a class for creating a tier"""
    pass

class TierUpdate(BaseModel):
    """a class for updating a tier"""
    tier: str
    price: float
    features: Text

class TierResponse(Tier):
    """a class that handle response"""
    pass