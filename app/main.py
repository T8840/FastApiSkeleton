# -*- coding: utf-8 -*-
"""
    :author: T8840
"""


from fastapi import FastAPI, Response, Request

from api.routers import v1
from db.session import SessionLocal, engine

app = FastAPI(
    title="FastAPI-Platform",
    description="Author:T8840",
    version="1.0",
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(
    v1.api_router,
    prefix="/api/v1"
)