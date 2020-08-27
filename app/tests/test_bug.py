# -*- coding: utf-8 -*-
"""
    :author: T8840
"""



from sqlalchemy import create_engine,MetaData,Table, Column, Integer, String, Sequence
from sqlalchemy.orm import scoped_session, sessionmaker

from core import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)# , pool_pre_ping=True
META_DATA = MetaData(bind=engine)
USERS_TABLE = Table("users", META_DATA,
                    Column("id", Integer, Sequence("user_id_seq"), primary_key=True),
                    Column("first_name", String(255)),
                    Column("last_name", String(255)),
                    keep_existing=True
                    )
META_DATA.create_all(engine, checkfirst=True)
#
# db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)