#!/usr/bin/env python3
"""a module for api models"""
from fastapi import APIRouter
from api.v1.routes import user
from api.v1.routes import auth


api_router = APIRouter()


api_router.include_router(auth.router, prefix='/auth', tags=["auth"])
api_router.include_router(user.router, tags=["users"])