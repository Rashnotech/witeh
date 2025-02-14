#!/usr/bin/env python3
"""a module for refresh module"""
from datetime import datetime, timezone
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Token(BaseModel):
    email: EmailStr
    role: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str

class TokenData(BaseModel):
    email: EmailStr
    role: str
    exp: datetime

class StoredToken(BaseModel):
    email: EmailStr
    refresh_token: str
    role: str
    expires_at: datetime
    is_revoked: bool = False
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))