#!/usr/bin/env python3
"""a user model"""
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    age: int
    email: EmailStr
    is_active: bool = True
    password: str


class UserCreate(User):
    pass


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool
