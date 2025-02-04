from sqlalchemy import Column, Integer
from .common.base import Base

class Post(Base):
    __tablename__ = 'post'
    
    id = Column(Integer, primary_key = True)
