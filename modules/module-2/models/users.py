#!/usr/bin/env python3
"""a module for user class"""
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_active: bool = True

class CreateUser(User):
    pass


class UserResponse(BaseModel):
    username: str
    email: EmailStr
    is_active: bool