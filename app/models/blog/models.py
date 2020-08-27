# -*- coding: utf-8 -*-
"""
    :author: T8840
"""

from sqlalchemy import String, Integer, ForeignKey, Boolean, Column
from sqlalchemy.orm import relationship
from db.base_class import Base
from models.users.models import User


class Category(Base):
    """Model category"""
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    slug = Column(String(50), unique=True)
    is_active = Column(Boolean(), default=True)

    post = relationship("Post", back_populates="category")


class Post(Base):
    """Model post"""
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    description = Column(String(50))
    slug = Column(String(50), unique=True)

    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="post")

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship(User, back_populates="post")

