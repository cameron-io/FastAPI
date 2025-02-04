from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, relationship
from .common.base import Base
from .profile import Profile

class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key = True)
    username = Column(String(100))
    email = Column(String(70), unique = True)
    password = Column(String(255))
    profile: Mapped["Profile"] = relationship('Profile', backref='account', lazy=True)

    def __repr__(self):
        return '<Account %r>' % self.username
