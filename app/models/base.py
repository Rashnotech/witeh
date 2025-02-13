#!/usr/bin/env python3
"""a module for base models"""
from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel, Field


class TimestampModel(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    updated_at: Optional[datetime] = None