#!/usr/bin/env python3
"""a router for products"""
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.deps import get_current_user, get_db
from models.product import ProductCreate, ProductResponse
from app.crud.product import ProductCRUD

router = APIRouter()

@router.post("/", response_model=ProductResponse)
async def create_product(
    product: ProductCreate,
    current_user = Depends(get_current_user),
    db = Depends(get_db)
):
    """Create a new product"""
    if current_user.role not in ["admin", "store-owner"]:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return await ProductCRUD(db).create(product)

@router.get("/", response_model=List[ProductResponse])
async def list_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    category: Optional[str] = None,
    search: Optional[str] = None,
    db = Depends(get_db)
):
    """List all products with optional filtering"""
    filters = {}
    if category:
        filters["category_id"] = category
    if search:
        filters["$text"] = {"$search": search}
    
    return await ProductCRUD(db).get_multi(
        skip=skip,
        limit=limit,
        filters=filters
    )

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: str,
    db = Depends(get_db)
):
    """Get a specific product by ID"""
    product = await ProductCRUD(db).get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product