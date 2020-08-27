# -*- coding: utf-8 -*-
"""
    :author: T8840
"""

from fastapi import APIRouter, Depends
from pydantic.networks import EmailStr

from api.routers.v1.utils.security import get_current_active_superuser
from models.base.schemas import Msg
from models.users.schemas import User
from models.users.models import User as DBUser
from utils import send_test_email

router = APIRouter()


@router.post("/test-email/", response_model=Msg, status_code=201)
def test_email(
    email_to: EmailStr,
    current_user: DBUser = Depends(get_current_active_superuser)
):
    """
    Test emails.
    """
    send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}