import logging
import sys
from typing import List

from databases import DatabaseURL
# # from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

# from app.core.logging import InterceptHandler
#
API_PREFIX = "/api"
#
# JWT_TOKEN_PREFIX = "Token"  # noqa: S105
# VERSION = "0.0.0"
#
config = Config(".env")
#
DEBUG: bool = config("DEBUG", cast=bool, default=False)

# DATABASE_URL: DatabaseURL = config("DB_CONNECTION", cast=DatabaseURL)
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)

SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)

PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI example application")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default=""
)

# logging configuration

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
# logging.basicConfig(
#     handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
# )
# logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'testgroup'
PASSWORD = '123456'
HOST = '10.201.5.161'
PORT = '3306'
DATABASE = 'wang'

import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'
# SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')

SQLALCHEMY_DATABASE_URI = f"{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = False

import os
from datetime import timedelta
# SECRET_KEY = b"SECRET_KEY"
# if not SECRET_KEY:
#     SECRET_KEY = os.urandom(32)

# Token 60 minutes * 24 hours * 8 days = 8 days
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
USERS_OPEN_REGISTRATION = True

# Email
SMTP_TLS = True
SMTP_PORT = None
SMTP_HOST = "SMTP_HOST"
SMTP_USER = "SMTP_USER"
SMTP_PASSWORD = "SMTP_PASSWORD"
EMAILS_FROM_EMAIL = "EMAILS_FROM_EMAIL"
EMAILS_FROM_NAME = "PROJECT_NAME"
EMAIL_RESET_TOKEN_EXPIRE_HOURS = 48
EMAIL_TEMPLATES_DIR = "/app/app/email-templates/build"
EMAILS_ENABLED = SMTP_HOST and SMTP_PORT and EMAILS_FROM_EMAIL

