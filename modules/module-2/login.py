#!/usr/bin/env python3
"""a module for user routes"""
from fastapi import APIRouter, Depends, HTTPException
from models.users import User
from auth.password import verify_password
from auth.jwt import create_access_token
from auth.auth import get_current_user
from engine import db
from datetime import timedelta


router = APIRouter()


@router.post('/auth/login')
async def login(username: str, password: str):
    user = await db.users.find_one({"username": username})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = create_access_token({"sub": username}, timedelta(minutes=30))
    refresh_token = create_access_token({"sub": username}, timedelta(days=3))
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.get('/product')
async def get_products(user:str = Depends(get_current_user)):
    return user