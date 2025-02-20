#!/usr/bin/env python3
"""a module for handling payment services"""


class PaymentService:
    """
    a class that represents a payment service
    """

    def __init__(self, db):
        """Initializes the payment service"""
        self.db = db
    