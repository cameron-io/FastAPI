from sqlalchemy import Integer, DateTime, String, Boolean, ForeignKey
from sqlalchemy.orm import mapped_column
from .common.base import Base

class Education(Base):
    __tablename__ = 'education'

    id = mapped_column(Integer, primary_key = True)

    school = mapped_column(String(255), nullable=False)
    degree = mapped_column(String(255), nullable=False)
    field_of_study = mapped_column(String(255), nullable=False)
    from_date = mapped_column(DateTime(), nullable=False)
    to_date = mapped_column(String(255))
    current = mapped_column(Boolean, default=False)
    description = mapped_column(String(255))

    profile_id = mapped_column(Integer, ForeignKey('profile.id'), nullable=False)
