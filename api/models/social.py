from sqlalchemy import Column, Integer, String, ForeignKey
from .common.base import Base

class Social(Base):
    __tablename__ = 'social'

    id = Column(Integer, primary_key = True)
    profile_id = Column(Integer, ForeignKey('profile.id'), nullable=False)
    youtube = Column(String(255))
    twitter = Column(String(255))
    facebook = Column(String(255))
    linkedin = Column(String(255))
    instagram = Column(String(255))
