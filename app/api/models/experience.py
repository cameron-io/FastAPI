from sqlalchemy import Integer, DateTime, String, Boolean, ForeignKey
from sqlalchemy.orm import mapped_column
from .common.base import Base

class Experience(Base):
    __tablename__ = 'experience'

    id = mapped_column(Integer, primary_key = True)
    
    title = mapped_column(String(255), nullable=False)
    company = mapped_column(String(255), nullable=False)
    location = mapped_column(String(255))
    from_date = mapped_column(DateTime(), nullable=False)
    to_date = mapped_column(String(255))
    current = mapped_column(Boolean, default=False)
    description = mapped_column(String(255))

    profile_id = mapped_column(Integer, ForeignKey('profile.id'), nullable=False)
