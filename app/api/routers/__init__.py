# -*- coding: utf-8 -*-
"""
    :author: T8840
"""
from fastapi import APIRouter

from api.routers.v1.endpoint import blog, login, utils, users

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(blog.router, tags=["blog"])