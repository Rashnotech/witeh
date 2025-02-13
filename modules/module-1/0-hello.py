#!/usr/bin/env python3
"""an entry point """
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}