from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column
from .common.base import Base

class Social(Base):
    __tablename__ = 'social'

    id = mapped_column(Integer, primary_key = True)

    youtube = mapped_column(String(255))
    twitter = mapped_column(String(255))
    facebook = mapped_column(String(255))
    linkedin = mapped_column(String(255))
    instagram = mapped_column(String(255))

    profile_id = mapped_column(Integer, ForeignKey('profile.id'), nullable=False)
