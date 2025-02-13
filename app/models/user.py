#!/usr/bin/env python3
"""a module for user models"""
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from .base import TimestampModel


class UserRole(str, Enum):
    AFFILIATE = "affiliate"
    STORE_OWNER = "store-owner"
    ADMIN = "admin"

class UserStatus(str, Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    DISABLED = "disable"

class User(TimestampModel):
    id: str = Field(default_factory=str, alias="_id")
    first_name: str
    last_name: str
    email: EmailStr
    telephone: str
    profile_img: Optional[str]
    token: Optional[str]
    active: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.AFFILIATE

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john@example.com",
                "telephone": "+1234567890",
                "role": "affiliate"
            }
        }
