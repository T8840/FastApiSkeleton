# -*- coding: utf-8 -*-
"""
    :author: T8840
"""

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from db.base_class import Base
"""
bug：class User(Base)：会导致
sqlalchemy.exc.InvalidRequestError: Table 'user' is already defined for this MetaData instance.  Specify 'extend_existing=True' to redefine options and columns on an exist
ing Table object
# 解决方案：https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/table_config.html?highlight=__table_args__
# 在  __tablename__ 下方加入 __table_args__ = {'extend_existing': True} 

"""

class User(Base):
    __table_args__ = {'extend_existing': True}
    """Model user"""
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(50), index=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(200))
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    post = relationship("Post", back_populates="user")
