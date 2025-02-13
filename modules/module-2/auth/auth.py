#!/usr/bin/env python3
"""a module for protect API routes"""
from fastapi import APIRouter, HTTPException, Depends
from .jwt import decode_access_token, oauth2_scheme, create_access_token
from datetime import timedelta
from engine import db


router = APIRouter()

async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    username = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid authentication")
    return username

@router.post('/auth/refresh-token')
async def refresh_token(username: str):
    stored_token = await db.stored_token.find_one({"username": username})
    if not stored_token or stored_token != refresh_token:
        raise HTTPException(status_code=400, detail="Invalid refresh token")
    
    new_access_token = create_access_token({"sub": username}, timedelta(minutes=30))
    return {"access_token": new_access_token, "token_type": "bearer"}