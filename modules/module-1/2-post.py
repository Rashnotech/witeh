#!/usr/bin/env python3
"""a module for post requests"""
from fastapi import FastAPI, HTTPException
from models.user import User


app = FastAPI()


@app.post('/users')
def create_user(user: User):
    return {"message": f"User {user.name} created!", "user": user}


@app.put('users/{user_id}')
def update_user(user_id: int, user: User):
    return {"message": f"User {user_id} updated!", "user": user}


@app.delete('users/{user_id}')
def delete_user(user_id: int):
    return {"message": f"User {user_id} deleted!"}

users_db = {1: "Alice", 2: "Bob", 3: "Charlie"}

@app.get('/users/{user_id}')
def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user_id, "name": users_db[user_id]}
