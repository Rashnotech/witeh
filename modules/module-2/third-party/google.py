#!/usr/bin/env python3
"""a module for google login"""
from fastapi import OAuth2AuthorizationCodeBearer


oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl = "https://accounts.google.com/o/oauth2/auth",
    tokenUrl = "https://oauth2.googleapis.com/token"
)

