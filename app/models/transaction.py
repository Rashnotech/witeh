#!/usr/bin/env python3
from enum import Enum
from pydantic import Field
from typing import Optional
from .base import TimestampModel


class TransactionStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

class Transaction(TimestampModel):
    id: str = Field(default_factory=str, alias="_id")
    account_id: str
    amount: float = 0.00
    status: TransactionStatus = TransactionStatus.PENDING
    reference: Optional[str]