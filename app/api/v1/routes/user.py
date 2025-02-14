#!/usr/bin/env python3
"""a router for users"""
from fastapi import APIRouter, Depends
from app.core.deps import get_current_user, get_db
from models.user import UserCreate, UserResponse
from app.services.user_service import UserService


router = APIRouter()


@router.post('/signup')
def create_user(user: UserCreate, db = Depends(get_db)):
    """create a user account"""
    return UserService(db).create(user)


@router.get('/me/{user_id}')
def get_user(user_id: str,
             db = Depends(get_db),
             user: dict = Depends(get_current_user),
             response_model=UserResponse
             ):
    return UserService(db).get(user_id)