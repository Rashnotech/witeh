#!/usr/bin/env python3
"""a module with parameters"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/products/{product_id}')
def get_product(product_id: int):
    return {'product_id': product_id}


@app.get('/users/{user_id}/orders/{order_id}')
def get_order(user_id: int, order_id: int):
    return {'user_id': user_id, 'order_id': order_id}


@app.get('/search')
def search_items(query: str, limit: int = 10):
    return {"query": query, "limit": limit}
