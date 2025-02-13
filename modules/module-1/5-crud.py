#!/usr/bin/env python3
"""a module for CRUD operations"""
from fastapi import FastAPI, HTTPException
from models.products import Product
from engine import db
from typing import List
from bson import ObjectId # type: ignore


app = FastAPI()


@app.post('/products')
async def create_product(product: Product):
    product_data = product.model_dump()
    new_product = await db.products.insert_one(product_data)
    return {"message": "Product created!", "id": str(new_product.inserted_id)}



@app.get('/products', response_model=List[Product])
async def get_products():
    products = await db.products.find().to_list(length=100)
    return products


@app.get('/products/{product_id}', response_model=Product)
async def get_product(product_id: str):
    product = await db.products.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.put('/products/{product_id}')
async def update_product(product_id: str, updated_data: Product):
    result = await db.products.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": updated_data.dict()}
    )

    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product updated!"}


@app.delete("/products/{product_id}")
async def delete_product(product_id: str):
    result = await db.products.delete_one(
        {"_id": ObjectId(product_id)}
    )
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted!"}
