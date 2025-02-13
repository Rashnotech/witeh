#!/usr/bin/env python3
"""a module for request methods"""
from fastapi import FastAPI
from typing import Optional
from models.user import UserCreate


app = FastAPI()


@app.post('/users')
def create_user(user: UserCreate):
    return {"message": "User created successfully!", "user": user}



@app.get('/products')
def get_products(category: Optional[str] = None, min_price: float = 0.0):
    return {"category": category, "min_price": min_price}

