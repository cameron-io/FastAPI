from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm.relationships import Relationship
from .common.base import Base

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
    experience = Relationship('Experience', backref='profile', lazy=True)
    Education = Relationship('Education', backref='profile', lazy=True)
    social = Relationship('Social', backref='profile', lazy=True)
    created_at = Column(DateTime)
