#!/usr/bin/env python3
"""a module to rate limit number of requests"""
from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request, Depends
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.base import BaseHTTPMiddleware


limiter = Limiter(key_func=get_remote_address)

