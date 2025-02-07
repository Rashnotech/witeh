#!/usr/bin/env python3
"""a module for category models"""
from typing import Optional
from pydantic import Field
from .base import TimestampModel

class Category(TimestampModel):
    id: str = Field(default_factory=str, alias="_id")
    name: str
    description: Optional[str]
    thumbnails: Optional[str]
    path: str
    active: bool = True