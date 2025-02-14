#!/usr/bin/env python3
"""a module for auth routes"""
from fastapi import APIRouter, HTTPException, status, Depends
from auth.jwt import create_access_token
from core.deps import get_db
from auth.password import verify_password
from services.user_service import UserService
from services.token_service import TokenService
from datetime import timedelta

router = APIRouter()


@router.post("/refresh")
async def refresh_token(refresh_token: str, db=Depends(get_db)):
    """Refresh token"""
    token_data = await TokenService(db).verify_refresh_token(refresh_token)
    if not token_data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    new_access_token = create_access_token({"sub": {"email": token_data.email, "role": token_data.role}})
    return {"access_token": new_access_token, "token_type": "bearer"}



@router.post('/login')
async def login(email: str, password: str, db=Depends(get_db)):
    user = await UserService(db).findby_email(email)
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token({"sub": {"email": email, "role": user.role}}, timedelta(minutes=30))
    refresh_token = TokenService(db).create_refresh_token(email, user.role)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }