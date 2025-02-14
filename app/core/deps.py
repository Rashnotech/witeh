#!/usr/bin/env python3
"""a module for dependencies"""
from fastapi import Depends, HTTPException, status
from auth.jwt import decode_access_token, oauth2_scheme


async def get_db():
    """Get database connection"""
    from app.core.database import db
    return db


async def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    """Get current user"""
    payload = await decode_access_token(token)
    user = payload.get("sub")
    if user is None:
        raise HTTPException(status_code=400, detail="Invalid authentication")
    return user


def require_role(role: str):
    def role_checker(user: dict = Depends(get_current_user)):
        if user.get("role") != role:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No permission")
        return user
    return role_checker