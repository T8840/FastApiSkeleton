# -*- coding: utf-8 -*-
"""
    :author: T8840
"""

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from core import config
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)# , pool_pre_ping=True
Session = sessionmaker(bind=engine)

session = Session()
# A = session.execute('show databases')
# for i in A:
#     print(i)
Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    id   = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return "<Person(name='%s')>" % self.name



#创建一个person对象
person = Person(name='jack')
#添加person对象，但是仍然没有commit到数据库
session.add(person)
#commit操作
session.commit()