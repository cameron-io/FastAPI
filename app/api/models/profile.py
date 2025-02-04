from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from .common.base import Base
from .experience import Experience
from .education import Education
from .social import Social

class Profile(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key = True)
    account_id = Column(Integer, ForeignKey('account.id'), nullable=False)
    website = Column(String(255))
    location = Column(String(255))
    status = Column(String(255))
    skills = Column(String(255), nullable=False)
    bio = Column(String(255))
    githubusername = Column(String(255))
    experience: Mapped[Experience] = relationship('Experience', backref='profile', lazy=True)
    education: Mapped[Education] = relationship('Education', backref='profile', lazy=True)
    social: Mapped[Social] = relationship('Social', backref='profile', lazy=True)
    created_at = Column(DateTime)
