#!/usr/bin/env python3
"""a module for account models"""
from typing import Optional
from pydantic import BaseModel, Field
from .base import TimestampModel


class AccountDetails(TimestampModel):
    id: str = Field(default_factory=str, alias="_id")
    user_id: str
    bank_name: str
    account_name: str
    account_no: str
    balance: float = 0.00