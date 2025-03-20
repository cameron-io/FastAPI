from typing import List
from sqlalchemy import Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .common.base import Base
from .experience import Experience
from .education import Education
from .social import Social

class Profile(Base):
    __tablename__ = 'profile'

    id = mapped_column(Integer, primary_key = True)
    
    website = mapped_column(String(255))
    location = mapped_column(String(255))
    status = mapped_column(String(255))
    skills = mapped_column(String(255), nullable=False)
    bio = mapped_column(String(255))
    githubusername = mapped_column(String(255))
    created_at = mapped_column(DateTime)

    experience: Mapped[List['Experience']] = relationship()
    education: Mapped[List['Education']] = relationship()
    social: Mapped[List['Social']] = relationship()

    account_id = mapped_column(Integer, ForeignKey('account.id'), nullable=False)
