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
    BUYER = "buyer"

class AuthProvider(str, Enum):
    google = "google"
    email = "email"

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
    password: str | None
    active: UserStatus = UserStatus.ACTIVE
    role: UserRole = UserRole.BUYER
    auth_provider: AuthProvider
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john@example.com",
                "telephone": "+1234567890",
                "role": "buyer"
            }
        }

class UserCreate(User):
    pass

class UserResponse(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    telephone: str
    profile_img: Optional[str]
    active: UserStatus
    role: UserRole
    auth_provider: AuthProvider
