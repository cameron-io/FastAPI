from sqlalchemy import Column, Integer, DateTime, String, Boolean, ForeignKey
from .common.base import Base

class Education(Base):
    __tablename__ = 'education'

    id = Column(Integer, primary_key = True)
    profile_id = Column(Integer, ForeignKey('profile.id'), nullable=False)
    school = Column(String(255), nullable=False)
    degree = Column(String(255), nullable=False)
    field_of_study = Column(String(255), nullable=False)
    from_date = Column(DateTime(), nullable=False)
    to_date = Column(String(255))
    current = Column(Boolean, default=False)
    description = Column(String(255))
