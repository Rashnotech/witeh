#!/usr/bin/env python3
"""a router for users"""
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.deps import get_current_user, get_db


router = APIRouter()

@router.get("/")
async def index():
    """Get a specific product by ID"""
    return {"message": "Hello World"}