# -*- coding: utf-8 -*-
"""
    :author: T8840
"""

from starlette.requests import Request


def get_db(request: Request):
    return request.state.db