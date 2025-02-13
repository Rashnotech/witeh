#!/usr/bin/env python3
"""a module for response methods"""
from fastapi import FastAPI
from models.user import UserCreate, UserResponse
from fastapi.responses import PlainTextResponse, HTMLResponse


app = FastAPI()


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    return {"id": 1, "name": user.name, "email": user.email}


@app.get("/plaintext", response_class=PlainTextResponse)
def get_plain_text():
    return "Hello, world!"

@app.get("/html", response_class=HTMLResponse)
def get_html():
    return "<h1>Hello, world!</h1>"