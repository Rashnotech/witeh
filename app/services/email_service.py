#!/usr/bin/env python3
"""an email service for ecommerce"""
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from fastapi_mail.errors import ConnectionErrors
from pathlib import Path
from jinja2 import Environment, select_autoescape, FileSystemLoader
from typing import List, Dict, Any
from app.core.config import settings
import logging
from itsdangerous import URLSafeTimedSerializer


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Email configuration
conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_TLS=settings.MAIL_TLS,
    MAIL_SSL=settings.MAIL_SSL,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    TEMPLATE_FOLDER=Path(__file__).parent.parent / 'templates'
)

# Initialize Jinja2 template environment
template_env = Environment(
    loader=FileSystemLoader(conf.TEMPLATE_FOLDER),
    autoescape=select_autoescape(['html', 'xml'])
)

class EmailService:
    def __init__(self):
        self.fastmail = FastMail(conf)

    async def send_email(
        self,
        email_to: List[str],
        subject: str,
        template_name: str,
        template_data: Dict[str, Any]
    ) -> bool:
        """
        Send an email using a template.
        
        Args:
            email_to: List of recipient email addresses
            subject: Email subject
            template_name: Name of the template file
            template_data: Data to be passed to the template
        """
        try:
            template = template_env.get_template(template_name)
            html_content = template.render(**template_data)

            message = MessageSchema(
                subject=subject,
                recipients=email_to,
                body=html_content,
                subtype="html"
            )

            await self.fastmail.send_message(message)
            logger.info(f"Email sent successfully to {email_to}")
            return True
        except ConnectionErrors as e:
            logger.error(f"Failed to send email: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error sending email: {str(e)}")
            return False

    async def send_welcome_email(self, user_email: str, user_name: str) -> bool:
        """Send welcome email to new users."""
        return await self.send_email(
            email_to=[user_email],
            subject="Welcome to Our E-Commerce Platform!",
            template_name="welcome.html",
            template_data={"user_name": user_name}
        )

    async def send_order_confirmation(
        self,
        email: str,
        order_id: str,
        order_details: Dict[str, Any]
    ) -> bool:
        """Send order confirmation email."""
        return await self.send_email(
            email_to=[email],
            subject=f"Order Confirmation #{order_id}",
            template_name="order_confirmation.html",
            template_data={
                "order_id": order_id,
                "order_details": order_details
            }
        )

    async def send_password_reset(self, email: str, reset_token: str) -> bool:
        """Send password reset email."""
        reset_url = f"{settings.FRONTEND_URL}/reset-password?token={reset_token}"
        return await self.send_email(
            email_to=[email],
            subject="Password Reset Request",
            template_name="password_reset.html",
            template_data={"reset_url": reset_url}
        )

    async def send_shipping_update(
        self,
        email: str,
        order_id: str,
        tracking_info: Dict[str, Any]
    ) -> bool:
        """Send shipping status update email."""
        return await self.send_email(
            email_to=[email],
            subject=f"Shipping Update for Order #{order_id}",
            template_name="shipping_update.html",
            template_data={
                "order_id": order_id,
                "tracking_info": tracking_info
            }
        )
